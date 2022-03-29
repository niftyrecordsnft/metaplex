import log from 'loglevel';
import { basename } from 'path';

export async function customUpload(
    file: string,
    manifestBuffer: Buffer,
    index,
  ) {

    const baseAssetServerURL = "https://assets.niftyrecordsnft.com/niftyrecords"
    const niftyRecordId = (parseInt(index) + 1).toString()

    const filename = `${basename(file)}`

    log.debug('CUSTOM file:', file);
    log.debug('CUSTOM filename:', filename);

    const mediaUrl = `${baseAssetServerURL}/${niftyRecordId}/${filename}`;
    
    const manifestJson = JSON.parse(manifestBuffer.toString('utf8'));
    manifestJson.image = mediaUrl;
    manifestJson.properties.files = manifestJson.properties.files.map(f => {
        return { ...f, uri: mediaUrl };
    });
    const updatedManifestBuffer = Buffer.from(JSON.stringify(manifestJson));

    const metadataFilename = filename.replace(/.png$/, '.json');
    const metadataUrl = `${baseAssetServerURL}/${niftyRecordId}/${metadataFilename}`;

    return [metadataUrl, mediaUrl];
}