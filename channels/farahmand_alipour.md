<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/S9peqB7avsPA_Ca37i3PZ5VcdK1h5ou3Mf9zIIHOeyp-3Dwnz-sRBxuDYjhLgA4WNLdeTYf1NCa5vg28x6Xuu4xsl_FQfwLXRCs39k0-HzZQgCObm98tyvjHBv1cnfijj61PJZtF6Kl0XIp1OpUcqfs1yrCxisGNj50t0YOnCJpkxcyTeqkFeYwkNAD5VCnmJLoqN2U5tLwWyDMp8oWzgS_-sRTOctiF2CoMeqfG2pvF1RhGQwWW7yUHYuPa60bTwGzWSH0EMUNAZUiL9bsbOFgRCG9NZ3osg4AR9ODUbq31uw5j3PPuZIg1QCZkEi70soXCztaNoMN1wPBBCzZCQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 06:23:54</div>
<hr>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXPNd-sjAK6k0FHjbEUDhvF1E6vdscgOFSJbeTN7yZuVUV-0KxyLKq1qOWkqexFwk-8uukZVbXrW0-m4ElApBznnLTNFTngMxO9ex6FVcg_BKQA9A2zK6H6strq0Zk6o9YPvJCvirBtcT0JN72ga7DTwgPg_h1ISOFoMT4zCdLxKtgAxdXL4UiSMX2cSR203d58Wh7FWlv2HtK7FchT2zQhM-kwO79Tx584swtoTWVuj-SbeDb2nA3DMuYal3WLb02tojAHUNIic672lJ7gG7sFp4b_ij0_WzZc4wkClfJzFdGu-UYfgg3NwGDDnCvu5duseOthqSl2SpURMVVAGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=d80hczskAdSXT_RM79irlTeHDBSNlHOFj5HMpZVRcmVQxzICMTMVinXIe6mvt3hVSSRck8MRUMyVc8lXkzPlySQj4uyg3tESVr1k61bf-yMM1qeXBydQpliQrDwreqlsowStr7YwDlTSIi1Gz9XdrvT0yQzKFjEB38OzLOswl6cVOGVPQFqk254OfU3V3LCypujDKptj2aEoFvRGpSeEP_hjyrkldI-QQHukZdhpU68zQudGEGlJQgbUR35F8K8XlbPLxinWDLqNsBN0On0IcbtX4DvGv9gB6FFY9lLS8M-46dypsZMer192FKMbSc7f_MKbSOCjNzYfmcVhLCMgL18NHzQwFT67J3cDuyOJaxOl9d-UC-7S_GGoI9DEY5Q6RXLNleYdxMlKinF8hFOTqxArOBKiWTg4EGS_i2Yh5HtUbKSW0J5MR92oNqHWuv1x3EAE4UpQ2DosVA6D7C3aFiiSU3aZEkjsxnOSCZocXV4O1zsmGCwnpn1o78NRxCEoiCpQkjqs_T1WHOEeXpN0mm9YP-x8k6sZH5IX-K0vEiA89uwMlcEM5NXLQz-zreXHsHMkanYd6ArDb6xK0XIRhHPm0groXobhdUey16YUaM4kjqy7B28M3flHqdXm1DidT0IjU_LI9LfjjBPF7HrtOatovnD7QbYS1Glaou8JYB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=d80hczskAdSXT_RM79irlTeHDBSNlHOFj5HMpZVRcmVQxzICMTMVinXIe6mvt3hVSSRck8MRUMyVc8lXkzPlySQj4uyg3tESVr1k61bf-yMM1qeXBydQpliQrDwreqlsowStr7YwDlTSIi1Gz9XdrvT0yQzKFjEB38OzLOswl6cVOGVPQFqk254OfU3V3LCypujDKptj2aEoFvRGpSeEP_hjyrkldI-QQHukZdhpU68zQudGEGlJQgbUR35F8K8XlbPLxinWDLqNsBN0On0IcbtX4DvGv9gB6FFY9lLS8M-46dypsZMer192FKMbSc7f_MKbSOCjNzYfmcVhLCMgL18NHzQwFT67J3cDuyOJaxOl9d-UC-7S_GGoI9DEY5Q6RXLNleYdxMlKinF8hFOTqxArOBKiWTg4EGS_i2Yh5HtUbKSW0J5MR92oNqHWuv1x3EAE4UpQ2DosVA6D7C3aFiiSU3aZEkjsxnOSCZocXV4O1zsmGCwnpn1o78NRxCEoiCpQkjqs_T1WHOEeXpN0mm9YP-x8k6sZH5IX-K0vEiA89uwMlcEM5NXLQz-zreXHsHMkanYd6ArDb6xK0XIRhHPm0groXobhdUey16YUaM4kjqy7B28M3flHqdXm1DidT0IjU_LI9LfjjBPF7HrtOatovnD7QbYS1Glaou8JYB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYhOO-R2LUKnhklu74Id45BTDEudSbOxk-7gL-KOCxQkyR8qEy_Ez-QuzOpLMpwC42OCS6v8NNhaCRbUi5pRQKbGOlp9eJWQz3jiGZ7LR5ss_7t4zuGYBjuijWpkjLld5KcDnnmyT9tRbeVSS8KR66zMzfGdkanvuglAjlb5R8eqTxaIslbejMCerhT1bhfOeiq1rn-gVIbwk8JSwwfK3vGamkmqXw0NbHIepgNvAVuToVf4X6QN6qBb7pPDS4t9ER0MNvlCqknelaaTaTwaNAG8H6wfqCcaRMXMgEXu_SR0dZYlasx53n0uRZgq3u470hTExviIqLdWGd5DaN4WDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=IElFrMxJG1OtmGnM8G_XKJYAxgog6m1OnM0dhnk2yXZTbT_JwJaIBRTRbAVODmAEJ4AYnNDI7yXlKFR0eKz2WfFJhQX_LBzrsyJlFPOb75DGLGF67ChufS5j7goZ7B9XP2qOhnae54kWB0Fd7fpdUTvaNgMVrMwMN_4YoZjFsy5pfLk7wCL6W7NVPMDp2sIGeAXCwmtvpJjBOc8OdR1LZj5EYMXXDg69G5Pl3ZYrwpuTajt8MpEtkPcefrNTcA2TDVzNfMXcWTXRJg8Lvb_6DrSd7hwOfYzDgwT3YXf2oIv5G_NkWZnUghYoariRcL9FxDix5VDCGOi04lWSVuhzEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=IElFrMxJG1OtmGnM8G_XKJYAxgog6m1OnM0dhnk2yXZTbT_JwJaIBRTRbAVODmAEJ4AYnNDI7yXlKFR0eKz2WfFJhQX_LBzrsyJlFPOb75DGLGF67ChufS5j7goZ7B9XP2qOhnae54kWB0Fd7fpdUTvaNgMVrMwMN_4YoZjFsy5pfLk7wCL6W7NVPMDp2sIGeAXCwmtvpJjBOc8OdR1LZj5EYMXXDg69G5Pl3ZYrwpuTajt8MpEtkPcefrNTcA2TDVzNfMXcWTXRJg8Lvb_6DrSd7hwOfYzDgwT3YXf2oIv5G_NkWZnUghYoariRcL9FxDix5VDCGOi04lWSVuhzEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=nS6rrCTyqcpZT9Z-lLhSCM87kh5ipNRfSP7WvEBRF054PJ17UTfVaKfScvErgO8EuxxdVUnum9zHl-99-V5QCowpxou0ICjoIZCPLnHxXAgRZ4xgHLOaenesQHPwbtDECDOgCO4uMA-UVhI5uWDinWLSejUn_YjzRlwPNQ2wzAigwA86ePgyhW5yccmVHyVQFxgNK0vL4rbVoNqM6KPaf2hQfqqbQC48h5YGph9GTpXs7YX0mFTmNaMJJLwUzFczrioQBb7HkcfiUzNzou1tGIca_IL5_8FO7EbmXoG2Nter6hVzTfPUyqxqVlc5NyYxc5L-MeXOLWjxEE_qiLfbrHulddS9G_CIpYwRRxMKVi6dFn1jormbE_G0baDUXeHBA-7FcDBWppYbjmYLKNqs6RlQe7ZSIOC3b7dQycppjrMemAaVp4BLTGKkGwpAvxrefxd2jKhZnoNysIu6k8L8vcYhajRrgkMS2Tfs2M9OTX9jlzNOobD_RzOqkOT62gmsstP-x-EUFJ1Ql7P6Z8-du9QOt-BgnMTYi_8MyyulJZyHdBgzSIi5GEBTUoYvWxovaCN7zNGKop4MRt8k8iHj6kgTWGtdKZttMBaZwPeINHRuxz6gOUG-9Eh5BIEBVrARXt9RBfE0uOZZL80ckPsK5k0foYajVvV068TkKaRVFPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=nS6rrCTyqcpZT9Z-lLhSCM87kh5ipNRfSP7WvEBRF054PJ17UTfVaKfScvErgO8EuxxdVUnum9zHl-99-V5QCowpxou0ICjoIZCPLnHxXAgRZ4xgHLOaenesQHPwbtDECDOgCO4uMA-UVhI5uWDinWLSejUn_YjzRlwPNQ2wzAigwA86ePgyhW5yccmVHyVQFxgNK0vL4rbVoNqM6KPaf2hQfqqbQC48h5YGph9GTpXs7YX0mFTmNaMJJLwUzFczrioQBb7HkcfiUzNzou1tGIca_IL5_8FO7EbmXoG2Nter6hVzTfPUyqxqVlc5NyYxc5L-MeXOLWjxEE_qiLfbrHulddS9G_CIpYwRRxMKVi6dFn1jormbE_G0baDUXeHBA-7FcDBWppYbjmYLKNqs6RlQe7ZSIOC3b7dQycppjrMemAaVp4BLTGKkGwpAvxrefxd2jKhZnoNysIu6k8L8vcYhajRrgkMS2Tfs2M9OTX9jlzNOobD_RzOqkOT62gmsstP-x-EUFJ1Ql7P6Z8-du9QOt-BgnMTYi_8MyyulJZyHdBgzSIi5GEBTUoYvWxovaCN7zNGKop4MRt8k8iHj6kgTWGtdKZttMBaZwPeINHRuxz6gOUG-9Eh5BIEBVrARXt9RBfE0uOZZL80ckPsK5k0foYajVvV068TkKaRVFPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=hoZ28OcrtiqdC_ZVGG0HZ1A6boMEhvLEPF0ivGdI0lauxsYIAVRCfa2LsNLA4ZceuEDpcAjTlj0-EDVLbe3IHgZljOlJ6lJx8nTjtBnWzU8GLLzbQFaRwVEJ5KgwNBmFORHj2Q7-35oKMMZkhZYbBaQtGSBDp1u-cwB5d2CsEDmNvHGLtRgaZyla5erJ_g7kQ9AfszzRm6p7Zg4d7eVbe8g4bAM2L8PEKwwNpUufQlP80cn7nyzO6Wtg3vPP-tmwzivjr9mdfHF32QUFvdKp8ncIIps5kSwIn7bTWQok_xnmsShzciWTeWpzS5elEoSuzecj-JkRSxYC7p3atkAXQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=hoZ28OcrtiqdC_ZVGG0HZ1A6boMEhvLEPF0ivGdI0lauxsYIAVRCfa2LsNLA4ZceuEDpcAjTlj0-EDVLbe3IHgZljOlJ6lJx8nTjtBnWzU8GLLzbQFaRwVEJ5KgwNBmFORHj2Q7-35oKMMZkhZYbBaQtGSBDp1u-cwB5d2CsEDmNvHGLtRgaZyla5erJ_g7kQ9AfszzRm6p7Zg4d7eVbe8g4bAM2L8PEKwwNpUufQlP80cn7nyzO6Wtg3vPP-tmwzivjr9mdfHF32QUFvdKp8ncIIps5kSwIn7bTWQok_xnmsShzciWTeWpzS5elEoSuzecj-JkRSxYC7p3atkAXQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCeY_I6ZeHmowhf6WSFQldHus8QaITXuVMBt7wfR7KyhMcmpiKL-TitEfrUgO_IX-BJPAOXc8wvaXh45EKEb4bj-hFM3PGn4YvMAGB6j2EF4UKe9Tq2GfjwKD-5QlfQ-xgaRfOx_u9cF7172-TESNyt_q-k8sFXiVYDxsVmlchmb3EcJNA_nDWgz5iYf83Iffd0xN_sG55o-rwC6SvZQCqCvAaZ96Bx45sIZmrafFC-0XVk7fq2kADWqk88buDahgu2qsrBzvjeZflgMEljUwotb-KjehHgw0cH9WTCsg0Xbh0otsftgWo7_9c557dvjF1DgTerIrvqZICjWVLVzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzOsHTYpo_JOqRS_pLj7DSlT-gcBF7nS2c61U5AH0GK4N4AmG99UFkk4ESWwTADBVDB5XfYDCQ4L70jw9w_gFGwosxzQK_9l6Ya5UoccO09OPZOvw3acR9Ben0MDTgJrDxMT-Wb9tZ0TyvJRWFCrYJH-dESYua3D5s8ZWT8fjJifoREVe2prTnz0JhJekHSoaRSb4p_IDVCHUmLmS6r-_I2zCn_d6s9XHhykbs8fpfu5dfZfvOlym5_382Dhl1yX5ZHdCdUrE550XMKobp-0LttMabgsHIYSiuPV8xPgn_TKR7LeW1MqC2DVAs1XIilxzMovRoqUuPyzZK7EHwHImQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4F_6F5Aa2Zvx1bf6wMEbKIfsbubOSZ46j1fmUr0dASQPfltrhG8UR--PfE2Hd-HF4DFo0uw4QQmJ7SzY5-XB2-u1frziVWW9IUu2TSdTlHTcpcCD1gbuQT1PfzEbqShX3lDD3SKHKHQ0qdTseRxA6tQkuVh6vvcMUDejLamnqcaXmn1Z8AJZDdUZ6yfSZtD9ZKzhjEgoip6liCjhmt0UbJ0-x2jWXjZUyNVnM1QcsKiHvI3f5XPeg0z5RxPq9omv0fQubvDBgT147u9NzDgrGxw-9YZNvrWWJMZW7zaHPO5UgGzwQkyKnH1YZJwxPMLgaHVcU41GTNITZW1aqKG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-W6O6I1KeX6NbbXk9akso76C05rdaw9_jsnyzfse0ZjYLOSikD46nUKu5zA7YiXFtLUaQ_duoXXIDrmOcY2uGmMsgIMuYngjUzP_ptm3C_hxNua2SNeFchdyWEgf_ghs-O4xGfhT6fQCRZxddI0OVyU2f_AvSTQRe1gJUoPHJyNEE7O_O0MNssF3LMHHceKh2FPE2zTq2TjTtvoVymAY7VFUrSeGKA0PuOErEIs6YVMsPQZbN0LMymHNfs1QuckvsnosuBLbaLIpFP-XRKWCpocMTOCnWLys_t2EvvNVQm9gZc40leEiyh-lGFMy0P6ua9N5paF2_jWYs_a5pUleA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sd8n2E54zJ8YhoaiObz1oEyyyKdT4EljHv5C-oa4YphBW4e2PYCt-fTfOzgimFWexppyieUUXbU2PR0Vcym-WEXEXw62WlMzAsURgvkxWbzViMTGBevPVKqgoMcyRStRQaRXs_G3xXC6epTo8byI6NG0KDMzU81LhfNrcXdBuFemT5xUZvqXcqq-P2Z5nBbWlC_wXjU09FXDqBhftj3v-hafODV9wt9g8Qq_fP1DwB3_PhzEXEsmOfeIrsPaYjfWD6dDVtVULey8wk4gfYcA2HGNIibG9DOyQhw21SCvX9CeGLFJ_SIvEV-Rxa0ZPkAh1ATUxYeOeZ4S-g4-KO_MGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=Q64MqjCLGC_eFnp7y-4Nv3eRcGbbJfXqD2rn4Aqx1a4BR-Ue4ZfSfpGGeRr0MFyLmBx3Q4YgqZO3wwsxHez0cwWuHPRi4DS9KkdtVwbFq3ASCp1CB91CX_rGbsHtAxXoZJPqPeq_NdQFRxsEp95oKmOMgCnT71sNbMMqcBnN_aCFlceXAhBr5kzaKW7fUyOmRUwU9fYd8uG6zxJtrepVMxk41y-vc0tZzfyLEqsY0PnEEJr4e82OK8C6AxPRKH5N4l_dIoVvhJb6fnbHQpDC7oPEzT-bLuMEioDIGtnzTqITOkN8RjQRxYAE4j4BV4TWDLWnZpXeuLJghnETpWgS6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=Q64MqjCLGC_eFnp7y-4Nv3eRcGbbJfXqD2rn4Aqx1a4BR-Ue4ZfSfpGGeRr0MFyLmBx3Q4YgqZO3wwsxHez0cwWuHPRi4DS9KkdtVwbFq3ASCp1CB91CX_rGbsHtAxXoZJPqPeq_NdQFRxsEp95oKmOMgCnT71sNbMMqcBnN_aCFlceXAhBr5kzaKW7fUyOmRUwU9fYd8uG6zxJtrepVMxk41y-vc0tZzfyLEqsY0PnEEJr4e82OK8C6AxPRKH5N4l_dIoVvhJb6fnbHQpDC7oPEzT-bLuMEioDIGtnzTqITOkN8RjQRxYAE4j4BV4TWDLWnZpXeuLJghnETpWgS6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BySfnmFR7PiHaL_nK0z9yYdJ1lNAAbPYgpipzNB2OjUmNc4bwit7a3dARWQ28RyfYMdXFMQxMuGaZAo_m00_-Et9OrnPPgzYRCUHdEQYqZaB6h7yhk0QtCn9_tOADL9Y4f7Hv_F0k76uEOVSdM7xdsIuFWP_srqK2l_oCfD0bVt09kYFxq6oodBbnx_o-D_9f28ibD_UtVP7bvb1q0h64PNkh10pqS_0dwD0wK9NHwGgx50Vw4ulJZ7x1LRdZoxzIbvK08oj8tARqs0K_mUx86NDNSOG4dHI3mOMGK6XGWJj1bvDSvwRMweWkGtgjaXhi879vYI4pwh0g7RwXJgENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHQgtfUqeoDZlQ-BNJstDIHW9gm4LyeT_Ttld12rMBTCa8ipJvrvHgBcacptBwsyIYl3IhGf_4a0e0u9eiqnANbDa26d7jAWDkSxgl03e47jlYSFApaVBpOd3ly2BvVYfAJw9V2GHH6fF8B84LbGWbMogP-6hXal9kQaAG-Zh3AyL_3lkIS_74kC0zIFHraYaxmFLnYjwth9lAxmnGkbJBpeJMX0l9Xva6mvtf5-p1OMlT_euG8ZXptxvAGG8VBa236nID-GOqulOngD0RDwe8vyoglIpRxx-RWHAg00ibtxQvFYQYqVAX2mMSQttVq5feU5zvNhD4_H2wVq6yEV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6b40iKSMmSLtdaJJ1C9XjDdHRpp0_bLxWfNssEw2TXs4T_GKaNPUGsReKWdz1sVhxa8U1E_C02g8_wLyhigR9mAiFwzOdZL3XDGSlQbsql0hYA-p2eD0Vza182x2E6HpfI5mFMlzamQEC2y2OyQIIjICFAlzk4CE-Y87X308NGlItWu7rJFOIDetSavHbXrvC7ycZ1sD-g1PX0ZSzFlygCQ3-9P-xN4GS_XpMlmDwZwAD-umQ8EzMQhPPkpg9T3yF4hDhAhNbLSApR5d2KMcKQKbtI9oxvf36mpMBUCtcGs2W2Rqs_XzIQTi0_LE8TBgYLjw3ghL3ssG9wlP6VRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmvdHAO4pU_4f06Fr68SJteJeDlEdNBymYvXLWssp7krHRzwaeU7OfdCmnaVjHicsfBavaIEm2EZ59K5beqOIJKjU4WwRgIA6XAHg3pmvBbw5xte2MItPLeEzeRxN_RCL6Q7-mWw9yfeoj5SgpbEjjWtUDFd3hbTmHhuCWPdvEfB2EGojAhrrCeVKgGfmcmYKSDdIavnVjhgKtFpCdR-a-FPQ4hrELlvvhreMPlb9IJG_N9X2YF0NSa5v_tmoQGj2ATL960BcrbKjsXSrW3_saHdcfkYH3wp_22ysy8V-EB2xOKmQIg9gdUda-5PcSDin942Yig-G8ZbMp1uUSycJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WL8KzmqA8alOx_-hKTNHGWqia5p5hzmV_es-yNxI_f4HJdd8sImbr_m9lHfROteHvfmY1aGz7Uruc2kqCr7IwiLuejf2M33I_mYi1y5pnO5RFpdPQaBFVNT2R3AG4mLgux0epC5kQUWUDJ1kWIabl73ioXi6xiJTI5nEYLZUd0AhKVjk3AM8KlF-sOIV54zJXjid2nE10bLE5bJYQigE4aHDhG-wtaRsiBRWZ7T1TeGA0SAf7YwZAzNCu-slnrCSuYoyx1rFOpZ6jgrZbHmb76NPimZksxVHiDPQ2HDvZT1CBb1fe9VDUtRdkFsn15iW6cpqBYiS19VhiROaqRnxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcptLHubu-tLQS39d_Oab8L7RLOTNwSwKXE-Yt8pX14TNQFYCz2u9sDTtYanQHOCLVC8s0dJFmCbj1eAu80RmZ8B1p8FsWM6qAvn9oGB1I7OP6wrLLnrWzK_chobBHnyRRZ_qezP2cCx1AoWCF5M7ndDMX0jCwzjLhGR_ivUyqi5yjbpNdEgjqkP4-pwK-n5MraIumiKmX7mGvEbzAisOUvD7qmDUnRuyfoly2AfiWdxzdPwLEPHzUfUC72WR8xTSJImPpCAlx_FbPtVTPyN897daOG0Fb2tnQHZasjXxGo1qHUocMByrbYyK-v6UO8zHLltU48dFh46Smwj9VOpQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGPRAFolhm3ScczIpS664b9SjnK3LOJZwd48eQcmvPqN0dMLTJXLadCGiXXEQksVQGMCxyQvzUjrbFB-JWPhjJ8hw2gKfFxs5yDQxaeggzDOdfh2FWr8uDpDZi3CrLyg8WH8sRN2aL7nX5jLD1Ok29XsF1lYZLjCdeYWzSF1rBEFG04LphbmrPLYsQHS6AxaE18ulZhgcnR4pUe7oSaEmX-1KGoLtJ8H5W_6LDmMHtupc72m9P5jKZQFfiItJdEIybWS1X2NI5I0hgQD5C0gmSM3YQZa9nRGEujtsRpGy2blBGHszHw5PG0s16gz8QhviotNllE-Adk90QshAFI5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-A13nyQvkGOJXnC2i1wIf-6oIIj9yh8g4Z8zm8rfl30lYunmAyqEFW1fO-Y8BEk4N4TVAIPCIyaQYQHXwHG9tAadC8Qhx2GN6cpGrzJ-BYqbUkWLfSuUe2f1I51CuqIa15LT2TOMJaMq4qA2MQFYwzJiv_0vLXY2bgVca_1lL7I-ZuGnFGSFOVAEpr5Jm14Pz0UvRsMsrivpyWaO4iccOsnoxm3y3KAwzVwMR5b1bxqC6fn9ZEsSD3RjNauD9mfKiUpbkpjPK-BsFDWyPk0rVHmx59OFfFbHdD1fXLcFOQG4WbE72KDY1MqUIZuE1ZTnXyggXE9Ug-c5blYb99Law.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=OaNAdnMELLDrpjUJI___2Kmo3zuoUh8MlkgbBXpQCkUwaxRJYdQ0ohGKTtUHG36On8_MsghWpD9pTnG0gqYE0NAGFfNMtyY3xJ4eMdsuVkWsuY4yboffLfOWCeBxIShXOfxAaqbJvY8P8iNsb2DtqkrxYA73AhqztURiM7XlX9MruEh78FkAC8QB4FGCq34PLuufuhKbt9ohvCgLmeguEiQLAN9_PMNL0niBN0s-lskzFazxAfCfIGH6sWC7QCt-0YtGnsirgyaCP5ElggiQuZCRcNo-WmnByNBY4RJ5E0hKCZx-20gMql5-gwXtojfnDwwTk0MMcruJz5YpnAPDnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=OaNAdnMELLDrpjUJI___2Kmo3zuoUh8MlkgbBXpQCkUwaxRJYdQ0ohGKTtUHG36On8_MsghWpD9pTnG0gqYE0NAGFfNMtyY3xJ4eMdsuVkWsuY4yboffLfOWCeBxIShXOfxAaqbJvY8P8iNsb2DtqkrxYA73AhqztURiM7XlX9MruEh78FkAC8QB4FGCq34PLuufuhKbt9ohvCgLmeguEiQLAN9_PMNL0niBN0s-lskzFazxAfCfIGH6sWC7QCt-0YtGnsirgyaCP5ElggiQuZCRcNo-WmnByNBY4RJ5E0hKCZx-20gMql5-gwXtojfnDwwTk0MMcruJz5YpnAPDnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=bahpqrMCL70pqSX5XoeeqW5ON3jdAgXF0IIw90rGM_LRk_pY98SmUxmg1830mVCyK-S3rHHepzGobk_V-kLCz1PY3INL9Mm44tjFpBmXzFSRWWOKYtRChY3hHkhwm7ZbP_pJbTpqQsJ8FEECSpzTbrDlBE7ouj7cmFTnSXg7WrEr--1uP-4VcyZjPAeOJsWnFfX9rwwvlmht1YNt1soKtTAIl0PirJWXcn6EdPnJSfV-hspkPBj8R0T9xciJIdzndihcId2D-pmdrTA4UrsArfkL4MpQkCBoDzVhm4F_e6UxAa4lrm_-phgBMdLGLav3QlUxGRWrtVUrWzk15mtfXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=bahpqrMCL70pqSX5XoeeqW5ON3jdAgXF0IIw90rGM_LRk_pY98SmUxmg1830mVCyK-S3rHHepzGobk_V-kLCz1PY3INL9Mm44tjFpBmXzFSRWWOKYtRChY3hHkhwm7ZbP_pJbTpqQsJ8FEECSpzTbrDlBE7ouj7cmFTnSXg7WrEr--1uP-4VcyZjPAeOJsWnFfX9rwwvlmht1YNt1soKtTAIl0PirJWXcn6EdPnJSfV-hspkPBj8R0T9xciJIdzndihcId2D-pmdrTA4UrsArfkL4MpQkCBoDzVhm4F_e6UxAa4lrm_-phgBMdLGLav3QlUxGRWrtVUrWzk15mtfXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=X6SxpooUKErZ1eGnSp3x9ms8iAOUL82j44GobbXf9ROtJWPKSmxJA6N8Kr9EgcpFWxV2OHcWsFobazxygEEuG8aC_RjUSeys0s4rVpEVjzLjeHi48m_Q1fuVETmBCTArwrweUu7FTMDMP6fJB4ZvxdSZA2CYTJCjpSnPXHa3aatvLFaxD2iEzkWbGhFkSJRmSe0RheXbe-Y6otm22wW9gHIY3qKjtoU14loSuXJxePFogCQ0gTtaBWzCFlbKGH2shhoPRzfTVWroGcE8QwD1m9m3Aa8yERmY_YrzP9wjW_PSjC8qNGzXvWS5wur6bpLA5DlZtMq8WtfGmVymNqabsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=X6SxpooUKErZ1eGnSp3x9ms8iAOUL82j44GobbXf9ROtJWPKSmxJA6N8Kr9EgcpFWxV2OHcWsFobazxygEEuG8aC_RjUSeys0s4rVpEVjzLjeHi48m_Q1fuVETmBCTArwrweUu7FTMDMP6fJB4ZvxdSZA2CYTJCjpSnPXHa3aatvLFaxD2iEzkWbGhFkSJRmSe0RheXbe-Y6otm22wW9gHIY3qKjtoU14loSuXJxePFogCQ0gTtaBWzCFlbKGH2shhoPRzfTVWroGcE8QwD1m9m3Aa8yERmY_YrzP9wjW_PSjC8qNGzXvWS5wur6bpLA5DlZtMq8WtfGmVymNqabsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=S7cQPZ3k7i5iwpyC3gpeQO2qJ_r5khN8YBa3ZGIW9J8JZALjkGP1ml-H78tUDSskGbuvw7ni8yjBs7xN-I7E6p_AKiOa7gKqyFkUIr2VONHxywK68gy2LPDOha6SMJAe3dbLLu5JOq1AK6RZTdo8hey4Jzx_ySzwObpkW5COHYRjSEkUeKLuSMO75God3BpizUSmu6cxMsP4kcsdXKnPzwkpuDx_GkwsxsaLxyG1n9kbf3Lu_koA8R3W6VKpZxOnhmOrhhpEvp5ygStx_FvuFXmvcpls35xXGoRxnn4eRpzU7EsSlEBbzLWgljqXzodpi3URVTx4z24b3ojzfvLDbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=S7cQPZ3k7i5iwpyC3gpeQO2qJ_r5khN8YBa3ZGIW9J8JZALjkGP1ml-H78tUDSskGbuvw7ni8yjBs7xN-I7E6p_AKiOa7gKqyFkUIr2VONHxywK68gy2LPDOha6SMJAe3dbLLu5JOq1AK6RZTdo8hey4Jzx_ySzwObpkW5COHYRjSEkUeKLuSMO75God3BpizUSmu6cxMsP4kcsdXKnPzwkpuDx_GkwsxsaLxyG1n9kbf3Lu_koA8R3W6VKpZxOnhmOrhhpEvp5ygStx_FvuFXmvcpls35xXGoRxnn4eRpzU7EsSlEBbzLWgljqXzodpi3URVTx4z24b3ojzfvLDbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=veKNVRVaumLjM3oCj4W9SpURUS6f8wrvOjvtaU7ylTjG431dSUhOJ4RpWeFAFK34C62znlVxiM3F6AYTxKP2ZqMhpz_mzyj-8rnJ_wu8lDYN1Bb4QDz65XwDNJ56bmw7H1eNwXKl9N9t_FBsvAtCh_HcYK6JUV-pMSgD8s_tTHR0jsXw6tSKYk4oW4CuFAINsadNaw_RKlZL-bZUag4tVAE5Ouf_KdD9X5ufkMk-Q6t-GzsWqRAjxk7-YW_1tOXoAQAPaLmcbSBq_Agh88UBGty4ukULGujCIwYIoli3jJRWaJCNyclqsUF6ZWEq4kGYw_l5G_lv8A5BzbPqrwD_iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=veKNVRVaumLjM3oCj4W9SpURUS6f8wrvOjvtaU7ylTjG431dSUhOJ4RpWeFAFK34C62znlVxiM3F6AYTxKP2ZqMhpz_mzyj-8rnJ_wu8lDYN1Bb4QDz65XwDNJ56bmw7H1eNwXKl9N9t_FBsvAtCh_HcYK6JUV-pMSgD8s_tTHR0jsXw6tSKYk4oW4CuFAINsadNaw_RKlZL-bZUag4tVAE5Ouf_KdD9X5ufkMk-Q6t-GzsWqRAjxk7-YW_1tOXoAQAPaLmcbSBq_Agh88UBGty4ukULGujCIwYIoli3jJRWaJCNyclqsUF6ZWEq4kGYw_l5G_lv8A5BzbPqrwD_iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=O3XesSbDVMp-WjNpZ1h8qwlKgoDdJnZ4cuZbQplTfAEUA51EPoBj8DSz6mlYfyC3M6n17Bm-oPPZrdYOqVi4XJeF6-JRKVYhF3UGk5oJUmMOIAdx_tezpg2R1XXdqBCNbXPdDy8HY1cYb2YPJ2CsNqeUCwxCNFoEGNzSkpdJ2nXagX5HfMGPGtRX5Pv4swIHHYNu7slYqFh8l8qvY7oNqaUp-Rau4-QFIbE--NRnmAzv9zrkNH8uY5_hLkbUnms_NlDyBz-gUAGC13PPniZrHkT53LV8IAH0FMrJO0iSqVF-v32ZM8N2VVh5G_r4NyIsnJrr_pUiw7zganpWPGiSUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=O3XesSbDVMp-WjNpZ1h8qwlKgoDdJnZ4cuZbQplTfAEUA51EPoBj8DSz6mlYfyC3M6n17Bm-oPPZrdYOqVi4XJeF6-JRKVYhF3UGk5oJUmMOIAdx_tezpg2R1XXdqBCNbXPdDy8HY1cYb2YPJ2CsNqeUCwxCNFoEGNzSkpdJ2nXagX5HfMGPGtRX5Pv4swIHHYNu7slYqFh8l8qvY7oNqaUp-Rau4-QFIbE--NRnmAzv9zrkNH8uY5_hLkbUnms_NlDyBz-gUAGC13PPniZrHkT53LV8IAH0FMrJO0iSqVF-v32ZM8N2VVh5G_r4NyIsnJrr_pUiw7zganpWPGiSUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVVz16DLBXDM4sjzxtHheopVb3me4YZGJJO7VvgWWVtOFAKhIp7c72uP2hF_FdzXpFINdIAdO0d898Vy-BMx2Ba_ymwdmC5FWVbrapKlAZ6APbR7KbpuwrcZKjILzeqeHb-qxCmk2o-iDr4Ln__53GfnkN1B0pfXdkVestRip-0LApB_oWKLJ3MObjBQOR2ZBoK8OON9Khf-0YxChjez7okk-E4wJZdYELskeu1c6rtR73C1Lmzl1L0vmNY4KCj3olhFRxrm8aWlS4L-sPZATlEe8SPmoxQfb_Oyu8L4w_gGZcWwA0avg6P_cPDbC9QXvYExtnjPme_Lli_LC2oVnePE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVVz16DLBXDM4sjzxtHheopVb3me4YZGJJO7VvgWWVtOFAKhIp7c72uP2hF_FdzXpFINdIAdO0d898Vy-BMx2Ba_ymwdmC5FWVbrapKlAZ6APbR7KbpuwrcZKjILzeqeHb-qxCmk2o-iDr4Ln__53GfnkN1B0pfXdkVestRip-0LApB_oWKLJ3MObjBQOR2ZBoK8OON9Khf-0YxChjez7okk-E4wJZdYELskeu1c6rtR73C1Lmzl1L0vmNY4KCj3olhFRxrm8aWlS4L-sPZATlEe8SPmoxQfb_Oyu8L4w_gGZcWwA0avg6P_cPDbC9QXvYExtnjPme_Lli_LC2oVnePE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7JnG0cneGWU_M0NvSTZs9HqRyrZw7X-qCD2EZZ5ykKFb3fbSsjyXjsvI2tNKleG50MaWPt8IPNUJssH1_jGB6cFI-CSfeN-2sLsq6Vwlyqda9ptvhisQDUXlSIWWmyiY6lDzQpz3jyWSfaaYxwXd881zwh5QWIRWnJz_z2lnsbm9V34nGAFj9sMRnz81F13c2DH47EfXSGDh8nPTQB7B37nNhmalTXM7B8rq4XAXs2QPqfsyQmFv-z_EU4KKp6imU2oUbYbZ7WBg8Guus-9js6HSTTA6yXD0MhrUJRAXfVjosfuYPOINoESaluzuqDKVxViQtiTZn2Ojz97ZbBm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=FBbYPv8Od7aRZD2c25kLTJFW4WiX0xHNBecKdRpyIjHbr6IVeNMNcuQB0O8IU7S8Tl8e6Xo0mLEtalkrffoXEmf9ZSDygrFBcX4XWQeQeTNOqjgf48TNeVIowew74TjR8Yl6aCpUePJjU9fSd56eg9G-yBt_nGKPCt9oSvc8ULZn2T0cqtQ3ad78Z8h8c33ga4qE-U0yChzQ2bZioqFWp5JaKVTIxQZH_LnKmMZieG_JfTeAFPmiFhZdyJfJqnVKLf8WgUz52CfD5ASUEAoN46ZXXAZNNMemA8CAD6LBQWMVUNGfb3AaZV5QaUkQZ-W72d2o7MYyRN5g2e9d1o8Rng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=FBbYPv8Od7aRZD2c25kLTJFW4WiX0xHNBecKdRpyIjHbr6IVeNMNcuQB0O8IU7S8Tl8e6Xo0mLEtalkrffoXEmf9ZSDygrFBcX4XWQeQeTNOqjgf48TNeVIowew74TjR8Yl6aCpUePJjU9fSd56eg9G-yBt_nGKPCt9oSvc8ULZn2T0cqtQ3ad78Z8h8c33ga4qE-U0yChzQ2bZioqFWp5JaKVTIxQZH_LnKmMZieG_JfTeAFPmiFhZdyJfJqnVKLf8WgUz52CfD5ASUEAoN46ZXXAZNNMemA8CAD6LBQWMVUNGfb3AaZV5QaUkQZ-W72d2o7MYyRN5g2e9d1o8Rng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6GszRCQTiJiLj28kFJeRloggtJaQGGHAYX_pov6MWdwtJep6JnrczuwLduuXlks2zKcXg0BdmN5EyvFfju0mTVuWSDd5AIjpf2Jlkl9_uuoYAf2Eeguv38zUIJeYuAg12n3N_n4Mv_80vgKAEu8MgjLf5Hc-oTGxBeqh5Avj5Wr70fdkav53BgKsh99RGmu1sGS0UBdFCkDj3XsIk5eYwW11xFgO4jLYienFouWckUMRcswduNjqbL3__nLTpn0HCYrRU3ISN6F0iYE6GjqYR9X0UnqKqgVTXiACBMf_GZvtAU3ptb2IYUYG1m7U7GBA4yLy2c0t4Onma83Bz2-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Elvfz3fYR4rbwQZOrMPIBi1SWWqzvfJkuT7MFU_KC3ATe11vqbKMoxFNq6MlrD9JWWSMQWsDLGJ2uDgVvsuYylWOyLq9ahM-hknz4HPVbBw5fWm1iWk7v_JQ7w_tTvf2WAUO-1FAERgEXYjXeDe4UGVjfNSNSBOwIHVEpmmwpeQXFKeOm3F5dhS7uPmlDO2wWQJFTNB7X6DfkdyCMILHicu_BX-iGdkr-H6BKPG8q3ZOcs5w038fIo3NoBnkY4RkXu4Abkc3hv4s0RoKTYEMPE_3ceFD-6rqf9EkG4TDTCWmO5wzNVa8qERIpk2xoVnzjUsehM6VwcFB7e4FtN332g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoYEQv3xBaekMuthQ3Q49Ie8-lqhAHZdrYbUgT0j6v5QMJY_nktyLk1egOH6Y7LnLxKjCPTLaKlQc1BOzu1hJzBOMD4DZn-QFgj99pnAN1jINrnAXRsN886-bVNz0Zsf8iKp3K51xuYx-a59AIVCGURd2bxezw2vjsjygkkZ4eg0tFTtWmgU_xui7E_PDXmpAtVin15LiXn0B_poARLYaitapLEJ6awJEPV4TndQZZgjpIpLk4nCq4iDcUOMOV84t6dmrGt03KIaH2AAzvAJDnZaH-AgRXIQijPZBOGyZY15NMlR3-vs2fRzNc6KsAJesI7c8nXVUdU2HiF7hqBr6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=OgHI51Qp59h3jHer8zn5xj824Q0z56HxO60PZJSsNg0A409FErXK0N9udX3AI6q4lMOfBiomy65OFRDww8ClfXPs5csRzpCSbcUszeab7UA7KWEBjqP5pl6IV2XoVl_POA98miohSWQsvygT3KNMRfVkN-nDlzJJUBWCDNIxeOcnFsdFTavnTCC3MQB1TAj-PmFSjFSeVTauwMA7Wi5qMISEG_fE78fbUgsQOo_3IV9jKCloxIVCvJheGThduZ8kBxSHRU2-ey5bezX1XMJGIkfBaU--HeS4pqfP2HusGmytL_fE0Df8tHgxYPP0fF9xcLyEtWLUyc5JLBRfDxmYnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=OgHI51Qp59h3jHer8zn5xj824Q0z56HxO60PZJSsNg0A409FErXK0N9udX3AI6q4lMOfBiomy65OFRDww8ClfXPs5csRzpCSbcUszeab7UA7KWEBjqP5pl6IV2XoVl_POA98miohSWQsvygT3KNMRfVkN-nDlzJJUBWCDNIxeOcnFsdFTavnTCC3MQB1TAj-PmFSjFSeVTauwMA7Wi5qMISEG_fE78fbUgsQOo_3IV9jKCloxIVCvJheGThduZ8kBxSHRU2-ey5bezX1XMJGIkfBaU--HeS4pqfP2HusGmytL_fE0Df8tHgxYPP0fF9xcLyEtWLUyc5JLBRfDxmYnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS1vOUKyh4W0dpjQTg0_f8j30cHd-KnTscAWUJQ8Kc3lciOWdnlMZJxKegWdqVeSrO_UCxXTNvmL5Sga0VwNOdmtcjo89R3z3b-_7CEJW16L51NkDNQCZdPKL-NYrgOEOA48XX7xCVRwqwv6ZWGis_2JSMGwkGAvMXjkeo-hymyoRluKYLioiHnNrzCh_bkt5zAvMa8LZkmxF0HwgCpj8TvRhmFIBPxoaVOrgKajo7Ig0xxdLoeYFyu0yiy6QSYZNAT_pCKxT0Ouw5whQPc-9q8hD6Bh88POsBkNYssUaqnuejBuJhImtfM6JjbSoAgh8c-uqKj1i5kl464lM-3kNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph933vb_PS-adD6aPzCXkUDRMNfW_CKjx439VG0skw_j0fEhe9CmELgSubeDlQV2PlRCggWnYUafYDlC7qt5Je2LEO6eDf8Xq9WnbdLE-fMJB8bFnUYazZeCSHlUL_oYMKvtCNhQq4udPYi2jADmgzaeRb9lUZ0qUaUxNUBJ_tEbCDd4MCWLL-PZTNqiORNWhowuLTmdmFvEzKJIUVeomaRWbdiagQhLL8Gu_2BZnpqoNgHoTdvJ-l0M24P2f8Oaj8Z8PBA1YVaKzh3C75dZN9Cg8qyzicA7_393BdagRLRzj0fXXHeyu-S6QrSbm_IGAqMBnIennvLfHy8wn21Uaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blAk47qgnkPc7w0EHmhH0GzAzmfpQLlSKpyuXJHkucaDJYPXD0cYY0ax3W1rTuCbnfio8fkWvxkGVdJtr-2hhC7X_woTJqBtaQoMiN--p5XPsn2wy_KbhSYnDgb8kNXZHVqMMPU4e5-TWYT-seG1eofLNOvpB4_ZY35DFQh8TeZMRK_672_QaCuxXsty4Szytj-IaTwGgpwFYq6USTqQPYyAY1okLkjXa195EXqGxzspylK_78F7wGqx5IcUOA3SHQcIlnvZ_CTH8CB3Owtf8gLCHD-wNgX0e4JweGry41ywaHVW4oJ_Tf2WM9jII-exXLe9fS80HSKs_ZSqLYM64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkY6g2MtnYEJuHZmvaLGw47osTieHSkbxpnm7DBYk_IdYHV5ukuxDZ6XltsDeusSfXWpJtQPXHPD7Wo5NcL9yZiUeDbDoNjNiCQetfFWg4SEeZ3Une13peuw3PJawGHtKCYkB0TYlb0WK6w3XxU8C-HSjUdLs9qI4tbX1d4bGIizqrTnkVjpv0AnobfDH2MDP5iJaxcQ0f7_85ldmZuPkagGuJbAo3zWiSLnOF8TiYcN_FyeBzyHMjO-ekv4EnJ0Z2Qxsrq12BJrjiP7L-O8q8K2y2IDxTso-MbXY4p7_3KAgHHwd6ePONJBrlqHzmhDwsV9qanJh0Sr07YU92mR7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=j6kCOl-b5-t4dL5uWQpjGSc6kdOR3Ei-rwvTDcP4zbvccvMqkS91bFaaOJ2Er-lHhfGxNPSurbl6AkmjiWDg15YNHYEb0xbCrB9JKPPngL7uuvPeLdAN6DebvnCKyva5S7v_wzbmIFKb92sVpvB8MZrDqfs1GxwzqI7nkXwvW54NfdJ9SYnUU3pOhQllxvzhi316GT7MnSqnqV3h1EutnkRxpRgl4qwXMUZrep80Gpa9HuEFpvejFy1jd2rhkYa09to8hYQIqy1kFjCnbRTtaA8rHxP3PxuVat4G2gix_d_8lE6GnvLInZ0gUfR5mxcw24H7hwDT1LQaphohKUGalQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=j6kCOl-b5-t4dL5uWQpjGSc6kdOR3Ei-rwvTDcP4zbvccvMqkS91bFaaOJ2Er-lHhfGxNPSurbl6AkmjiWDg15YNHYEb0xbCrB9JKPPngL7uuvPeLdAN6DebvnCKyva5S7v_wzbmIFKb92sVpvB8MZrDqfs1GxwzqI7nkXwvW54NfdJ9SYnUU3pOhQllxvzhi316GT7MnSqnqV3h1EutnkRxpRgl4qwXMUZrep80Gpa9HuEFpvejFy1jd2rhkYa09to8hYQIqy1kFjCnbRTtaA8rHxP3PxuVat4G2gix_d_8lE6GnvLInZ0gUfR5mxcw24H7hwDT1LQaphohKUGalQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFPdVAPBqmKX1Ve8AFcExXlCx8mlHYorgWH5tcygEAm_8r-KWefBwHkPXFbpU94wccaN6cXQcKzRRlR8ZLJor_DWpxtyOof3AF5SjwUyyeR8QfPbzy357UAqsN6UsXl0RSIj_fxE7wzN-efrrs4lj4rCnWVryV2q4Pnci5bgA0tzHzQ6heywUxzOSwYDaN7WtJlMjjLtWMHx0d_gSHBDLwydT-GTHdnDO7dMqH7YagQXbj-BdyiKOpA8pvkqT0F4PqHQAyj2cV6KzZfFcd4a8aHhc9tK1qh1-cfD6F41HmNnUG6KNPsjcHc5iwVzKN43CCNDY4WBiM9GdPM7df-Keg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWfp5l4HcYf_r8XY6PtRSVUwunBJhvIDfvqyE1kXfQkBlq4xyeyGUsh6QAXAxwu2Aqq199tybHkZwkXVZgPgBeoMjnVqCKEcwFEQ1XZPjsavKsk5AIgDjGnjhw_E8NFwxQZnaA2852berEx-gexh-C0Iq19kS7JEh21QVfjUB6IiKctvAYzJi89yQv7Ih_uc2NODuac93C-TpaS3g0rvMTeQFkhCxgdI68dD4uxzfTUBH0QaQPXGCvi6aWtODZtQZ-B0cXvMF3CX616kQkzTiavD20tvbPpPi7Ifjpdt9Y4fNj4VeXBAQnEGWYJoC5h6o6fb0zE7dY7mFSa0lDBvAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=RWjIMvnas1wvvqZ-ec8Szn7sddM_o9pVrN2PohVOYyvHQJEzRlbFN03UitrXyO0v_VLAbce30_ulVHxBrVwkJrG6CfJ7OY0-dJx-Sa3BGMiUd1TTqbdELAMs_DyU4PsCIZlWXUqnKjzGLh9HVwgzSWuRkz7sIL2zYmuQdxB45TM4d9WBUi4e2AcHmirOlO6OGVlAXV2d7Pa90OqHz45eRo8BCiZheLyOnDVh2q98A2bObB-dVO4YjDE6ZKaVuw2ssB8Da-tmDW1UU-qrQj7vT25i7rifGfsHnpnzuZrdpRwrlMnz1Wzbl6II3Gg0AM4LM7AdN11UECE2_KMBPrtGJw252eqozv_SrPqt9Fd_PKY1XMk5-8gLvR-AkPoug8AEU3oo67cn9Uh7hf_XNpCmcR3gL1Sz1cYl6PySw-UTPBSgEGi37AucwnASpPVC-7vNSV3twxePVOeY-SgfxO7iN1LGOgtqYApiPJfu3bY2VEiYx6jC_9cAiXKiuh3nENneoW1LkxOny3-5wON_tTY4GmWavkSbHfrtwNZpD1Nl9Y3xFJD4q5omWc_bsJASGYkCasQC_UH0piKvd8cbNHRHrDSsQcpZUrSVFKUgO_nE3o5bOTn0jeMpcpoM6fqWL2Jhuh2JURpymXJg6fQD7_9bQO7S9wAgoSKKQewtScE8EWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=RWjIMvnas1wvvqZ-ec8Szn7sddM_o9pVrN2PohVOYyvHQJEzRlbFN03UitrXyO0v_VLAbce30_ulVHxBrVwkJrG6CfJ7OY0-dJx-Sa3BGMiUd1TTqbdELAMs_DyU4PsCIZlWXUqnKjzGLh9HVwgzSWuRkz7sIL2zYmuQdxB45TM4d9WBUi4e2AcHmirOlO6OGVlAXV2d7Pa90OqHz45eRo8BCiZheLyOnDVh2q98A2bObB-dVO4YjDE6ZKaVuw2ssB8Da-tmDW1UU-qrQj7vT25i7rifGfsHnpnzuZrdpRwrlMnz1Wzbl6II3Gg0AM4LM7AdN11UECE2_KMBPrtGJw252eqozv_SrPqt9Fd_PKY1XMk5-8gLvR-AkPoug8AEU3oo67cn9Uh7hf_XNpCmcR3gL1Sz1cYl6PySw-UTPBSgEGi37AucwnASpPVC-7vNSV3twxePVOeY-SgfxO7iN1LGOgtqYApiPJfu3bY2VEiYx6jC_9cAiXKiuh3nENneoW1LkxOny3-5wON_tTY4GmWavkSbHfrtwNZpD1Nl9Y3xFJD4q5omWc_bsJASGYkCasQC_UH0piKvd8cbNHRHrDSsQcpZUrSVFKUgO_nE3o5bOTn0jeMpcpoM6fqWL2Jhuh2JURpymXJg6fQD7_9bQO7S9wAgoSKKQewtScE8EWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=Po12b6j2dzxfBVCFEVbFNo_R6mPzWHzhyTKwqnfkBNJtjwAJi9AK24VtjQ7ElVmtr6NeZZKv-aQawsVrF5T6HUGpXSZddRi3O8-w53gRPEnQE24Y2wnyV0RJc5UJqK7rDLl11-Pr2McXkwkvff2c06uFi5UBdZcfSVq5h-lTkg-aclWUdRO5V9kEUr1glkhgLm94AbQisP5GUUYuN-lCuKnlsnzr8t_amyiFfXIGiRilPuj_46JQCkEuy6VuZlFPEh_GxSf3d-kPfTgkAUCUUqiJVLRAIX4MfNlYZrTpYZgNANlzToMDuLTuukz7cj5oRlrecdF0IQAfE3YEYLq6mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=Po12b6j2dzxfBVCFEVbFNo_R6mPzWHzhyTKwqnfkBNJtjwAJi9AK24VtjQ7ElVmtr6NeZZKv-aQawsVrF5T6HUGpXSZddRi3O8-w53gRPEnQE24Y2wnyV0RJc5UJqK7rDLl11-Pr2McXkwkvff2c06uFi5UBdZcfSVq5h-lTkg-aclWUdRO5V9kEUr1glkhgLm94AbQisP5GUUYuN-lCuKnlsnzr8t_amyiFfXIGiRilPuj_46JQCkEuy6VuZlFPEh_GxSf3d-kPfTgkAUCUUqiJVLRAIX4MfNlYZrTpYZgNANlzToMDuLTuukz7cj5oRlrecdF0IQAfE3YEYLq6mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSZvipTiRylZjgu2qQe3npfOtI4JRa1Y4F1_pU_nX6XSWWIlWJWxMoJhSydLcIkaIGsT4_7C1h9RDPI9wk1XVirHwjqjb0ysx-ALL2wzIlzbzB-8ft0S_-5ZoBwJZPtsY43j5Hcz6eXbw72l1YEVKSDIT4V7bvDY__WMWIYikRZ0xkz4ojwpqEkLhRYOKuTYNdDKUlfyXiuB5TpHwdv0m6kYLI9bbW-TSflt7zYy2SctbS0SFLOdNfclyqY7yo6GX3y9hEOTExRsnx19AgEnHwvAAFYtPelMDWdeJbiYUeBApUUuI2ahthvEBkh5miR2UL0y3WUQWiErsxkfoh5KvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=S112uEDKduzFmRP_yolWHjAsKzsoGP_945QIY5OKje76ph-lFMS60bDuEGK8wZWrtTZG3LHPFVoNqOuzPJ8NiYCK-S6W5L0M8c4rPaTiAwP3w0jXu1DMfgIgK8eTQ9Td0r3wevQEn-tW5wHZR27Gp1uJkwZCfsYOJ-prDLCbEIN0t4Nt_iJh7AYGBUra6iuX7GBcrKmwbwyRJaz1neC8u4J-CcUALFqaHEiRDXo0b3oF4yOcWZdT0KwLjAtOqoiNFdIYWapGh5A-IooaM9ohlsEW9uLUDuCQqLxnh6sd08ZyajmaOm-2vEDvZMsltvWadzyyzuqT09-_qZ7qYmamtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=S112uEDKduzFmRP_yolWHjAsKzsoGP_945QIY5OKje76ph-lFMS60bDuEGK8wZWrtTZG3LHPFVoNqOuzPJ8NiYCK-S6W5L0M8c4rPaTiAwP3w0jXu1DMfgIgK8eTQ9Td0r3wevQEn-tW5wHZR27Gp1uJkwZCfsYOJ-prDLCbEIN0t4Nt_iJh7AYGBUra6iuX7GBcrKmwbwyRJaz1neC8u4J-CcUALFqaHEiRDXo0b3oF4yOcWZdT0KwLjAtOqoiNFdIYWapGh5A-IooaM9ohlsEW9uLUDuCQqLxnh6sd08ZyajmaOm-2vEDvZMsltvWadzyyzuqT09-_qZ7qYmamtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PE9P0tIIEqok2UynJcn8D7XWiGixqda8cCObmJ1zH9l0hptflMhpDiASO5SD7qTmHkuqH904QAILXx-_zZLbnHH_fv9f_h5EuOryWt329UTYoLnomJnjF-0H6w5vqvCpgBXZfRFxI6IOrX3ozfm0GrktFTbHSE92uYG32Oa0V_hDbxfhmqbmCrGGv5ILKAAop-T1xP5y76DZLaZI-1Gqtm_ZyuVDOvFLIvBvDQjTT3Wy9LjfJ_9BPkJi5QVfJtV8mxY00Upn7WS1n-NZn1eNSAm_QjHjNcRbtbzcnSjCMF0jioHH4Opp3aaeiOf9zvKfJmAk9Vs1GvWs5N8jSy3sug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=rzUmL_ldFdCInC2G2wt3vYrl3MxSK5geUbObZR0vlt8dEBOLHk6jSFJyjpLPpE6zVmwGntPWfzNcfPmW3PSrGy2lFhiBkMvH_1oRSYbq6d2ob830p1SkXPqCYJGT2k7m2G1qVvRovKpJ3LpPYO_siDp7cPwoH1nksvC_l75E0-TYS4HDvvz8BBhPLCJAKb23feedUkIOb80RRHzFEnm_QYbjLi-MTbHS8ecHgwFWCAEUS1HjIOo99sBYed3gyoSPuvsg89bNPQfHDn_4LXUEhdGJnKHANjBneyJsJzoRw0oHVMZAnYd8MKrzY2H0LHWhngBQYEP8ff3J9YTgcwd8Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=rzUmL_ldFdCInC2G2wt3vYrl3MxSK5geUbObZR0vlt8dEBOLHk6jSFJyjpLPpE6zVmwGntPWfzNcfPmW3PSrGy2lFhiBkMvH_1oRSYbq6d2ob830p1SkXPqCYJGT2k7m2G1qVvRovKpJ3LpPYO_siDp7cPwoH1nksvC_l75E0-TYS4HDvvz8BBhPLCJAKb23feedUkIOb80RRHzFEnm_QYbjLi-MTbHS8ecHgwFWCAEUS1HjIOo99sBYed3gyoSPuvsg89bNPQfHDn_4LXUEhdGJnKHANjBneyJsJzoRw0oHVMZAnYd8MKrzY2H0LHWhngBQYEP8ff3J9YTgcwd8Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=quE4pxSOUyRdYzeXzBC1SkyvB77j9nR5KgcywrN9391Zc1CsB3yXREDl0GeOEyqjvug7uS20irpGXogrsZ1_RUlDr1mPEksflpX0QiCcITo91kgEu7Z5MsizZpMiev_V5la4xjr2OdtjnVorWhS9joZT3ON3Cpdj_JypmECaRhOSGr5WHGTsIe1h9wnpZNGmcmghU2giF9h2H96fpl5oIDlEp-Zz6nZX_hxWHV_IzKG9eSRRF5P5teo0VvipFwjkrjDyFckEyDMim-8GGRV1ON0enhlLPtSQIPKsn7r_SzixRzDwpgHkGFq_bu_EBHsmTycsUhLM-X3mMvO5C-uZhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=quE4pxSOUyRdYzeXzBC1SkyvB77j9nR5KgcywrN9391Zc1CsB3yXREDl0GeOEyqjvug7uS20irpGXogrsZ1_RUlDr1mPEksflpX0QiCcITo91kgEu7Z5MsizZpMiev_V5la4xjr2OdtjnVorWhS9joZT3ON3Cpdj_JypmECaRhOSGr5WHGTsIe1h9wnpZNGmcmghU2giF9h2H96fpl5oIDlEp-Zz6nZX_hxWHV_IzKG9eSRRF5P5teo0VvipFwjkrjDyFckEyDMim-8GGRV1ON0enhlLPtSQIPKsn7r_SzixRzDwpgHkGFq_bu_EBHsmTycsUhLM-X3mMvO5C-uZhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO_lweraYC6CsxmBjpnHRuOaX0r-kSyLmTHFkSoVz0boqekbeRFBYSgd4Z0eX9OUQ__ix4qSE9lMit2ZEHXOtuN16vxF6hevijtv_C9701kmwet-Udprg5_rPA1kmpMpsHK1q3OVvvdCnYE1k8Bv1ztYsC8BYTfovtzR1gR4zmkAgf4utLe0nsCMC0rh9kqnwbzSdbQQylzrTXhI4-K0h8cObmjqUN09fgqii5OZGtj7tedEYyqFXR8Gg2iMoKTNSYtJrxiC8_dEqfDM6TUPnlhLgQtB9FlBZ5F6a-3g-qw7b0jIFKFA3K-G98IMUM-nYjOa-DUOOwrfGArMidhCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=Ek5g_cPdMyyLt0HpTqP82l7JjNlMUjyWX5LICVq_NJrU4EIlvGJbxSepck7iwfstnEDBebguLwpifbSLronzNdHmpHma8sEZPY_OPgrUmOxxUJShyac7M-9bwQ1k9V5Njzic6GjSV7tQTUMLTKL8da1iqVZx2FFCZU2Dvt7DJl04DUWuFcDPPqz4D5Y_4Ar36m2CZJZgk79qjAjDQAmZK9pOgXkfVg3Ei-ctfLQMhU02f_ZTS2et0X7o7kCFPAq884kCXu5WtP5rKSMX9Xqi-7w_yVOZsiPVOKw_i3GQXl_R5QpP-yTqWcS1XffRd2iprzUkxfG_3INGGaj_Qupyaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=Ek5g_cPdMyyLt0HpTqP82l7JjNlMUjyWX5LICVq_NJrU4EIlvGJbxSepck7iwfstnEDBebguLwpifbSLronzNdHmpHma8sEZPY_OPgrUmOxxUJShyac7M-9bwQ1k9V5Njzic6GjSV7tQTUMLTKL8da1iqVZx2FFCZU2Dvt7DJl04DUWuFcDPPqz4D5Y_4Ar36m2CZJZgk79qjAjDQAmZK9pOgXkfVg3Ei-ctfLQMhU02f_ZTS2et0X7o7kCFPAq884kCXu5WtP5rKSMX9Xqi-7w_yVOZsiPVOKw_i3GQXl_R5QpP-yTqWcS1XffRd2iprzUkxfG_3INGGaj_Qupyaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsxkIhsvthNCJyvUBObSq64QKRGdnXSxqDiHrLyvhVENdBzIn-EeESxEkjtLQzRdlRNQ-Qd_wiqNeMFGTk6eDk6P3ay-_sR_0-iMVD0rR1QKJie-wHl-Ksqlu6bSys2Sd76yJPhGF604YuZDG1OaLmRtflbWIJyoNiN9TcWpWl3H93-REc6mu3-KrVXdYdxncz-CGsJ-kUBTL86vyyZjAjfHyPziRcokWGN_pgLjMSdRuG0_5rw4JRgn7fhC7vVR8XsZNZjMjFMrrFowa6m8ihkRGSnbCnUItdn1HkvzUajIdTm2hSn7VL3-Ou7kfHU3tz3TYFv3oOXYm_Jgp818CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zat-2WAw5m27-4uGaEcDmSZUCk9l-SLOUmriMPR9Hq7GccmwaumZ5kf_jgA659ONOtDSD1WlqO-bNAH76DJhzwmjTngT45LX2BKR-Agti7jQHe837CnaNUqRio1JQ6AcgNo0_wi5vBdepTISugxDN9fQujFVYmZ_8JaLS1OVohQxCDQ8xdij1AdbkX__9cNVEqhIFN2CFoorK1MLcvnGuSrdUjp1GEeplt8ZJ-7E7Fo7UD8OB1WkVUVhonS8assgJvAUFkVBk87UHdyfyFZMZqVyrCZmlpMRpBLAS68jbFjq_5TI2Lr8vzZ0nWNq-YNfECwFbQazv5qWjN3AbSGMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKpWL9Xg1UeADru-RgzrIOXkkqWVb4HYtR8U9QFHOEvaALCbpUgVRlnJT8lPlZSrL_uXNAwkWD6AUztiOlgnsFGOS2WYgggY4pKbEapF6eqCJ9UPtwi0VvJuiscOPvJRrR6qV_tUfLXwR-fJp2-C_6sLmGtiViOEAANy-v4W6mn7Ga5hKt1nC_Xi0hq2NYETdpu6KtjJUm4VboVnZA05aKxu-mX-LzG2qAVr7Epi4_CaTPn_BKIQOK6skXgN5BTXLDD5X4VGfVZqtC69qrtQznRV5yMhXbgorBMnheuUDKOOtUhKWNe7yEQ8qxjRIyySMw5__AbbjXHhw-3N9-Loww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVNbtR_Yk5RXjxC_F0gS93m3XhQlX_IueTlDJvZHGq1jYIMFlsddCg7p1_JUch4Fp4_f7Gq2mcmi6vZ8zj3fHqxIaAqrz7WknnYuRyAf0LpEvdhk_e6VK9pvICSicyYuyCcFslcu92DzE4Yr1fHDMS7D4i2rnFrLaPvjIxvQ6ZnQzLKF2N8boSYna3zlbQdCJMdT3-x1i-nEVKk1Lo6jX0q9cmIydScQrT60fmSVacQKLXK7tg1MKGqbZ0N0RE-sJwlquKoRzpdD_hGW1iUkqq6fss6jdLUyEOzl8GZegAaeEWDep99NNiY6_CXdhy6T68jadG2Ax7Py_zQNtL3kfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuwwe6KAIHJVU7e9qJUO3iO2u60YhtNwB-qkKA2_7KTYxUkZVKHfheszrSe8sCDC0M7MmsmNa6yej2HsqmVqH6_ikwRBSig1hhKEUIYRpihenVDzj9nh68HHpDrTq2vLvCTMhcK1cNJjj6oHs0E_5CY3CwUtPOrp3rp0cRuWtZmlvA1tedGhERuEaK6QcxVOfuNXdC5397wwap0RxxNgPeLJQdq2vC91PlC14JZdmBga_XhWacfFIuahdOTJ9DQ4y_dvHBTDe1r_uSt4qkS5xv963ABHwpEj9jYIcqf7v4Bx4Vvgz3_0H0LYRcqHXmK7G9ojLlzHq66Uy5IhgHwvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sdo9-QeIVc4SSROY8YWjp5UKZhmULp14JjDK7zuyxcRzRZzsinUBY2283EFFKN-d9WZquM3QVNa1kOZxNrixLhlg9yTacJYLNOTnUg3_o2nUUfHr8uSnhRawavaY1LB4I-qyHnzxg61duo6fWxRzS9RSUPjsNQoral6eP94P-qlrBGz4H6k8vYjFJt4KLvVni8G-4QuxjonMZToxUWY7y4BHzTTxNELdW_1bN9Lu_MC0XIBxMslI8kog4ZeN6eu70adKE8c-F1rcQq8OGaea6ICw6YO--1P-wyUhM23G0yFu7QKydAseAR1PgVlYoADPvc0LWYydu2Xfzz_MbgOlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=A4feaHHAy6iRGaIxhE2bgOqTIwMbIPG2XlEHPUxpnO9Z__jRe4ER_nGL6svQCYOTFtCyeusByrX6ctEPcp0TbM13WlqJlPfJGpFlZ9b_w16kUwN2WrYMPJQBr_0EFL7W4Oku_JZ12xpoWOaZPxRcTZllMRTlHHq1_Re4pTFEM8ovVKFMx19W2uCgr3FIh0g1iQ7s8RYmoiQG_5KqEo7_3Rm5asNonforNNYfa9jNcotQS7mLSqJ2ggCxdDMmPCNm5Mk8K6trwyhOVYHXojI2Tmq56L3jPnrdbstEEuBYUwHKoMC2vYMSfOLWtEUipLG-bzaYpQ-eP0xGE1u326HsjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=A4feaHHAy6iRGaIxhE2bgOqTIwMbIPG2XlEHPUxpnO9Z__jRe4ER_nGL6svQCYOTFtCyeusByrX6ctEPcp0TbM13WlqJlPfJGpFlZ9b_w16kUwN2WrYMPJQBr_0EFL7W4Oku_JZ12xpoWOaZPxRcTZllMRTlHHq1_Re4pTFEM8ovVKFMx19W2uCgr3FIh0g1iQ7s8RYmoiQG_5KqEo7_3Rm5asNonforNNYfa9jNcotQS7mLSqJ2ggCxdDMmPCNm5Mk8K6trwyhOVYHXojI2Tmq56L3jPnrdbstEEuBYUwHKoMC2vYMSfOLWtEUipLG-bzaYpQ-eP0xGE1u326HsjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llSb5EzPEUHHLuiH8DI3_eDlsLj-KIIabyaiOo4QCwa5LxMHQJxS33wGd7N8fEGF2v5weI7ayHwDCe2NLR3dUi2O5CTduKSmchK33bo4jmUeXOSg_lM_XF6odtYiYJYjZ7TTh4SyDzuZbG6nZZw68nEYMev5cTQxa5F1HoVCda2uAvdJD4nGYZL5Wx6M3op1_ssxrdRAafTdDH1e803eSMs0iu9dieYMU6U_XDopir67Ew7jR_uiHEBLs4HvBdxvjJ6JI94Qet9WpiDk-HA28pQFMH9jAAI_-pb7sLSR4oqkc153SF2bOoIe7e1tcYnlR016h97amTmbyog01X6UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7nFmOQy5RPsLXmpbhvGBkwDs57Pjktpzbj4VYjkVHMxaf-o54-W8vXrbXwmSedCmELZSPxQRntzXHMP7vNMIqhG6N55uvwcwkxROREKZ5_RW3Xmzx9jRHcXn1iT6JXEPRk79wBHCJ6qNhMocg1-yR0hcXD7RTwuT0v1OuIFClNXNg0CkrRg6wTO1N2eJVaew_sxBZV3rb6rd56-CQTfBMSRS4dl_yIMPmb82e7eGo2yOr_smyiwlfT71QqSJB5VKTI3v7Qn1CFGPdpmmxsIzRFCWzLpJy9OUbMdRZBru_AcU2nw5ERUCuZLrsapkGylhxdLA7Sab45BvAGWkB8c3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8-H3nGjBDrfgdopT3F1I8nOyQVy5lPaIVYavxwNG-t5RptwIWKqMhAcYJibI38_2wwfO2_XC0EaUVfhzh3b6xvvh9GjqR8akDHciFwRmdcdzKN2R56M0cXSuAPue5eAd8ZYybalz764eQNw4jTobrljxbV_eCIyQHtMrkpZF3kOfVElkCrsuWs-jpY91dBY40sgFWMp_zc3KBvThbi1k534dih7W2Qvu7vmkEa_ekEIO0Kb6l3v79tawl6aMzLJeXnbVVFRmunnv4tZPhl6ycEXq9N88ZkAswjwNBgtbFicJIUMCHVsyB-nujEO8p1lFO0YNEAP32WpuFKUeVZCqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_uOs-eiRu6Jr98DebHHE1_9mtq9606k99PlC_SRqNejNgJMPDL27THEiBFO4BPmraah3tLBeZAW89i7dk44P_cPtDhq9qKyxE9UMzlw8uxUCieNukeqr2ZpacYncQ6H3OCeqpZjD_l-0xt5Y3aC9kCxw2MRdjCMKa8LsHFN217xQmCIq6bSyVgBTnRDks6Bfz-qLJfdUdWnhswYz1BqrI5kJvjiczd0UXcY8jJ9t1Oc_UzNBxM0Nvs2HbHdBp2_5t-WUI8cAD9d6K13Tv3y8It2LRtHfguI1lEdMb6j3oyqVOO5Nym4spjIFe5Zi4UJMQX_1Q6JbT1etO2J-WRIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
