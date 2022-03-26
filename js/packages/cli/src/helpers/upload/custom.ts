import log from 'loglevel';
import { basename } from 'path';

export async function customUpload(
    file: string,
    manifestBuffer: Buffer,
  ) {

    const baseAssetServerURL = "https://assets.niftyrecordsnft.com/";
    const metadataPath = "metadata/";
    const imagesPath = "images/";

    const filename = `${basename(file)}`;

    log.debug('CUSTOM file:', file);
    log.debug('CUSTOM filename:', filename);

    const mediaUrl = `${baseAssetServerURL}${imagesPath}${filename}`;


    const manifestJson = JSON.parse(manifestBuffer.toString('utf8'));
    manifestJson.image = mediaUrl;
    manifestJson.properties.files = manifestJson.properties.files.map(f => {
        return { ...f, uri: mediaUrl };
    });
    const updatedManifestBuffer = Buffer.from(JSON.stringify(manifestJson));

    const metadataFilename = filename.replace(/.png$/, '.json');
    const metadataUrl = `${baseAssetServerURL}${metadataPath}${metadataFilename}`;

    return [metadataUrl, mediaUrl];

}