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
<img src="https://cdn5.telesco.pe/file/UBNIVpxf4FvS2rIN6QVoufTh_hwWFV9w9g0GpKpalLqYCMZwloDseJscb0f--MArqt5Yq2DYNeFQXq50mppWj0BrcpfnsPElqi-ZbomdYoELk_0nUXRbylUjLT41ka_Yedtpj8FmUTd4Ema1zOd7RsfJ72PdGsK2p_NgVJpKuE-5lwNjywTjr4fYRM1AJK_QFqetUonKFtJlW3Ean20XeJoA-NOnDtS6_4UewVd0XTxhIKgq78koBs23bbdVtKoVEhh0FuFkwjJgoG5DZU9KwQiIpZHqL4Ox8Sqp37VxmyQKuycyrYfFGp4wh0XG4l3H9y9QkODK8OU-hnWYDfb2DA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 617K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 02:30:10</div>
<hr>

<div class="tg-post" id="msg-93742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sX_nTcd908eNo9H0fAB3J763hnJ6qfiEFP8JNj99Z8QIAPZYY2TZEAM6WzHj-yUD_Y3nyJIUdNB2RdfSHoUTHt5sqwBVAkL6hIE6qbZrVoaNtEmh3tsKXderrWaFnH9krWNyxorv7bFBCPd1_FDzS-Ocy_dnAWfyijcZYHbEiah_5Qd1B1dDw7P4SzxhucOTsDFxp_Q8Ri8o0L1j40Q-1i3XwP7jnp7xbpnKcgdkISZB3Or7jBzdDbmvoOKBHBiUiNBzVzStvnjoNLd-5NSCyQoCzJVt9BKVqjLptRwrz9d_Z5vc3IjIBz-fN1Ix8CGFKln2Dsktl3PJN53wd57W5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل تو اولین بازی در جام‌جهانی
عجب غولیه این ارلینگ هالند
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/93742" target="_blank">📅 02:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93741">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پایان نیمه اول
🇮🇶
عراق
1️⃣
-
2️⃣
🇳🇴
نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/93741" target="_blank">📅 02:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عجب بازی‌ای شده</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/93740" target="_blank">📅 02:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93738">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2442e86f3e.mp4?token=dQi7IWlTVdNRfWPeaDA6q6s1fZ8dlFOcJDWUOSW1uPBnxhVsItsM1o9kFZAOKzRoODCMDBkfNhqhvB9RL44y-cPHt5NMBrXHGtRnAYOKYDsqYRySO7hzH8PBivRsZPN9RlABRaOWeQQ_iwp34oFTsSXULDvherMWbtwjOQwBMUW1UjVW3F5N_pBIOc8KCRsWNUaeQto3UWbDba79ZnR4lQ2Ihh7R61K9yH3l1HkxkSfBKbf8QRPVK_zpCw17vLwP3xqLHnDAHOhV-t-zxPCFmovj8CXVljNyDeB0BKjCAughohcEotRZFEjNt85L-cDUe_TOFqovlFDMwFGgoIW3UTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2442e86f3e.mp4?token=dQi7IWlTVdNRfWPeaDA6q6s1fZ8dlFOcJDWUOSW1uPBnxhVsItsM1o9kFZAOKzRoODCMDBkfNhqhvB9RL44y-cPHt5NMBrXHGtRnAYOKYDsqYRySO7hzH8PBivRsZPN9RlABRaOWeQQ_iwp34oFTsSXULDvherMWbtwjOQwBMUW1UjVW3F5N_pBIOc8KCRsWNUaeQto3UWbDba79ZnR4lQ2Ihh7R61K9yH3l1HkxkSfBKbf8QRPVK_zpCw17vLwP3xqLHnDAHOhV-t-zxPCFmovj8CXVljNyDeB0BKjCAughohcEotRZFEjNt85L-cDUe_TOFqovlFDMwFGgoIW3UTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دبل هالند برای نروژ مقابل عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/93738" target="_blank">📅 02:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93737">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هالند دبل کرد پشماممممم</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/93737" target="_blank">📅 02:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93736">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i40VCvX4KnSE-UmPiunqX_herTHH-1nhBD78DQiAk6KH--T66IYs-OntP5FRsKDKYX_RW11so8-f2gzNNbAIrbC2DKzSSY8cNb3vjs6HLOCxpb46qCr3uzUXr-5D2dP5dV2LRxBYMWwqm1IGUdEFjDV-8cPtUaFT_mpuM2sdUo4K56r6Ka3yuwEBqUc1rL44W-lo8jXIOnLa1T2XdPSauFg8RAusyF8ccsX3rgm7HSVYqab2WsDLoJCjaLAvCxrbDAD4JB4PCMERBIGQxnbo2R00R8W_c4r-4e4xiJwpQxlPAezf3PgczTiFh-wtKIsoaZLEQKxkfeOcSVAkdN3Heg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایکینگ باشه کصکش؟
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/Futball180TV/93736" target="_blank">📅 02:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93735">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nASkYjmFrodGACgkmUr6v40-5ijSbSahn50So4kiGgCqGNi3vzFaCRlxxbsHuOCsptZNsUBMMw6uFTztue401h1f60421ZWT9prsew7wimytgfmPHpLOqp7Cud1zJbHrtxkRE0KqA7VRQ422UFY6jLBNyMO1KW-RrIuCIETn5I0yL1717c7zRr2KAj_RuplcjCC1W_Q0pRUBPG0Jr3ZXISZu-J1FSN1o9_HS09ZDcsx0Jh_YlRCmxW4DLUocoB7VOLGXw97ZliLHHmhxIG41u7GNbuSp1wy2KpTl-UlEi4RRxKfZkVGPMcdwGoYQCmxyvopsYe2KxqkIyRm1E3XMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گللللل بچه غول به عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/Futball180TV/93735" target="_blank">📅 02:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93734">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54ce7a982e.mp4?token=b-VouH5_Krnm_q_t2BQIzaaTUxBJLxkzVqUUqRfperUsg8adxShh5JrS6wpJMI65yiodwfN-5zWCyhvh8I1loIfMetPp7RWJgymC--iBXZE9n2V9Ao8ai2okvTjy9k9fUVhuk7_VjNpxQaNDmIFCQzPmgaNdfcLZqyjO4Ar2NLMDvQpR69sGmPcCeuJCxOyC_lzrxCvDOsdknDs16o1m9pD7e5UX2S5EWnpPusNjyyt_xBjTzyE5oYS_TTandpDMIrVPd-nAAEB5k8uIpFT2cajlsAHzH4WoVx9pZgksb-FH2bT0sIFwrMFBjcZpRRlhRyJYQDvsmvcCU1Zh73PHCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54ce7a982e.mp4?token=b-VouH5_Krnm_q_t2BQIzaaTUxBJLxkzVqUUqRfperUsg8adxShh5JrS6wpJMI65yiodwfN-5zWCyhvh8I1loIfMetPp7RWJgymC--iBXZE9n2V9Ao8ai2okvTjy9k9fUVhuk7_VjNpxQaNDmIFCQzPmgaNdfcLZqyjO4Ar2NLMDvQpR69sGmPcCeuJCxOyC_lzrxCvDOsdknDs16o1m9pD7e5UX2S5EWnpPusNjyyt_xBjTzyE5oYS_TTandpDMIrVPd-nAAEB5k8uIpFT2cajlsAHzH4WoVx9pZgksb-FH2bT0sIFwrMFBjcZpRRlhRyJYQDvsmvcCU1Zh73PHCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گللللل بچه غول به عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/93734" target="_blank">📅 02:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93733">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">فاکینگ ارلینگ هالند</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/Futball180TV/93733" target="_blank">📅 02:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93732">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گللللللل هالنددددد</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/Futball180TV/93732" target="_blank">📅 02:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93731">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzsPHKGVX51UwJqm8fAQdkXibH8iYmulSgvH3CeePScKsipHEtWudrvX8qrVEqVl5CDnMZObvwkfLpc0rnSqgMhXIadOI1OuO72Q9jkInEKMtXN6gbhck8etn4AbcuVWMFeyzFjCRbT2yBvT52FsxYQQuCP5K2854z0ttt_vOHUKCZEXypELBgjyp7iOwRIOsisvYJ88iuCGSSDCI382np4LVffa-SJTp0agIek-SR1LZpSD23ArLZw628O9gLo3tHBQ_lrvkJ6YDFvg4C_lOtTEU2DJpXy1r1IV7ZZEb_rVUB2rSaa_k9vGkpADcCddF62HN2VFkZ5in9HChsvilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جووووو پشم ریزون رو ببین پسر
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/93731" target="_blank">📅 01:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93730">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بریم برا بازی عراق - نروژ
🔥
🔥</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/93730" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93729">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🇮🇷
#فوووووری؛ فدراسیون فوتبال ایران درحال رایزنی فشرده با فیفا برای صدور مجدد مجوز و ویزای نفرات ایران است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93729" target="_blank">📅 01:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93728">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c228d26641.mp4?token=llVfVhsbh0x5nilh_UIGLZisH8Ks4bGRaYv2kLAiyXetr43k7z8hdqg1R0QB_T8_cxffM_fyhBvy3gZUF7Bq_fnvYW-bLS-3PgOktc7L-pto5bDseGfIPAW8hLP_iJPIILiMLZuYg6tSUnV-adTOhhDm5AYsLcic-twai0Z62fIhcDXnc631pmqZiLc1yJ6VM1JoP89YdWMHPmI_JSz7bFw-fPkYMce3ZRvyt6SFJc0tApvCgcIPzA9KvdN5E3Hxs4tyKhEcQZRXBIJBUheg66yDSFARf2HFpVXHDxNPiiXzOG8_YAvz98SwCnQBtszbHgQYD-oBDsfZfAbk55KA3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c228d26641.mp4?token=llVfVhsbh0x5nilh_UIGLZisH8Ks4bGRaYv2kLAiyXetr43k7z8hdqg1R0QB_T8_cxffM_fyhBvy3gZUF7Bq_fnvYW-bLS-3PgOktc7L-pto5bDseGfIPAW8hLP_iJPIILiMLZuYg6tSUnV-adTOhhDm5AYsLcic-twai0Z62fIhcDXnc631pmqZiLc1yJ6VM1JoP89YdWMHPmI_JSz7bFw-fPkYMce3ZRvyt6SFJc0tApvCgcIPzA9KvdN5E3Hxs4tyKhEcQZRXBIJBUheg66yDSFARf2HFpVXHDxNPiiXzOG8_YAvz98SwCnQBtszbHgQYD-oBDsfZfAbk55KA3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش اسپید به سوپر گل امباپه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/93728" target="_blank">📅 01:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93727">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cdb4ce8b6.mp4?token=Mf6qSX3RWmE7x7tguwMOwXPwBQZLbWirZF9oHtPDpNZuTtdt8UQna9xqRqFNt95NBCUBDUAy2xMdziG1V_CP7CBAav9418GDQwG5wEg69QeKPYdhQHFNwp6WGT3jnZSb-quj9e_GuFnmFoiXwk0s4S8sYC5Pm20gRnyuQu84TPS4SCwTrK0FtpS_RdMPQ159W3q_Xo9-MhpaQEtMnn27-9qWIamib2YPJK9uGBw6sYuf9fp5LaN9747GjZxHNXIs9qaUqIdQiJoRcz5SeIGQJwdFW5Q-9gTaaai8Y1euhI2ABxKbIZHq14Yw3cyjugNuim0JQp2JBrN4_9vfP8qmfmJP8f-B224zn6wZ1EX99Ra1oqJ6b1_bb0IY-GqQ7LmphBX5YRIp4mmmr-tqgzFQM6m9fZ4z7gd9uvdVEevgNyHlFoxSSuMB7KwTOWU_1NNyw7SxKIZ6KgwaGBgzN9R496inRqqIo6ITl4asEykY1Gj7kC9Rwbu1g4Ul1mmboFlsEzE9CUUjTYX9JtcLO-7RR0s3q57NdFAxTjCzkKyAXPIbGV15xW2CnHVle_AkXJuYvRKdM1y8Ktr-c-JebHTWvyPtLoGrXZDsPxo7rQpf1LZk0xliDD5T9OCpEgSV51-KdXdGo__Y9MqL2yev4QQR63nKNEwmA87c-J8QNiTuJ4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cdb4ce8b6.mp4?token=Mf6qSX3RWmE7x7tguwMOwXPwBQZLbWirZF9oHtPDpNZuTtdt8UQna9xqRqFNt95NBCUBDUAy2xMdziG1V_CP7CBAav9418GDQwG5wEg69QeKPYdhQHFNwp6WGT3jnZSb-quj9e_GuFnmFoiXwk0s4S8sYC5Pm20gRnyuQu84TPS4SCwTrK0FtpS_RdMPQ159W3q_Xo9-MhpaQEtMnn27-9qWIamib2YPJK9uGBw6sYuf9fp5LaN9747GjZxHNXIs9qaUqIdQiJoRcz5SeIGQJwdFW5Q-9gTaaai8Y1euhI2ABxKbIZHq14Yw3cyjugNuim0JQp2JBrN4_9vfP8qmfmJP8f-B224zn6wZ1EX99Ra1oqJ6b1_bb0IY-GqQ7LmphBX5YRIp4mmmr-tqgzFQM6m9fZ4z7gd9uvdVEevgNyHlFoxSSuMB7KwTOWU_1NNyw7SxKIZ6KgwaGBgzN9R496inRqqIo6ITl4asEykY1Gj7kC9Rwbu1g4Ul1mmboFlsEzE9CUUjTYX9JtcLO-7RR0s3q57NdFAxTjCzkKyAXPIbGV15xW2CnHVle_AkXJuYvRKdM1y8Ktr-c-JebHTWvyPtLoGrXZDsPxo7rQpf1LZk0xliDD5T9OCpEgSV51-KdXdGo__Y9MqL2yev4QQR63nKNEwmA87c-J8QNiTuJ4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
جو پرشور آرژانتینی‌ها برای بازی با الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/93727" target="_blank">📅 01:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93725">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKsegbSM2Jt2Ac2iFz_Xj05e7WVNGYvTtDpcbquHiulIrbx6KxtmbrBj0npRXLmJracBEQ63LDSwkWMQ3dcV5Vvaa7VOF6JnNV47gt0fTRPydmAhO5JVIo20HuahgRZrLA_OcrGVRfHvrG3XTa6rAVHC-6zjG4fs2OAdu3GuRcvPK_fH8rMmk1Mb03O-VQ5nRH6PNOujMaPnmUcsJ39jeekNU1dvSsnbxRDN9eTLUWjLE3D8_RCQPs6c3Ri7F2GbNZUZqpD1o74NYT3PUjFyNhcMn6Br_WtQbfcZBU67TVfscVPLq2hhBuK0r17dczcSEzD4Ctg_cXgJWr8BfYWAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
کراش فلورنتینو پرز بهترین بازیکن دیدار فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/93725" target="_blank">📅 01:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93724">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2408168513.mp4?token=Q34leKfUQFPygdX-8E9dDK-OKQfIZSflaoABPXtj4-LRBQk6yX8X4iHF1TpByou0_dATpamd1nbmFEHszzI7eA-FycOhuPQieAc6_b0DvkVIhsM4CC8TK9kc-namESh9IlnS_YshIJ-t1axf4Gt401FqMse6pPdTCXGfK1znOvEegC8VTu5RSd52_8USYMdVoyNzCWFfIGzPs69pH0nSSflLKaMtXelolU5217rHUNr3yzgAplEsyNqs3MPlItPz47YQgh7_yngsqHvk2pZS01dun6egCJ_2fZquTDwUY_SJY3NiBnlWncGAFdK6PWB_tArVksVc-D_pYDoMJQgwmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2408168513.mp4?token=Q34leKfUQFPygdX-8E9dDK-OKQfIZSflaoABPXtj4-LRBQk6yX8X4iHF1TpByou0_dATpamd1nbmFEHszzI7eA-FycOhuPQieAc6_b0DvkVIhsM4CC8TK9kc-namESh9IlnS_YshIJ-t1axf4Gt401FqMse6pPdTCXGfK1znOvEegC8VTu5RSd52_8USYMdVoyNzCWFfIGzPs69pH0nSSflLKaMtXelolU5217rHUNr3yzgAplEsyNqs3MPlItPz47YQgh7_yngsqHvk2pZS01dun6egCJ_2fZquTDwUY_SJY3NiBnlWncGAFdK6PWB_tArVksVc-D_pYDoMJQgwmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇳🇴
کشتی وایکینگ‌ها به استادیوم محل بازی با عراق رسید
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/93724" target="_blank">📅 01:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93723">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB4QKWPUh-qWi1J5mQe2bO_fEiv4Ytl7GphtDUjK9ujGzxrXRs8e7eMAslqzcNZrURJHL6FCtQcF1KgUinR8OTk2qjJeqFosvKc_d54FFoZSAPOEiK9PTLZODwv-Znu7K6_bKPuxd37QSLU5hcBf0bfzhqe--70GVgzgn403E56ICoPIwai4IXiJkKEY7cOTDhYfC9_Z9WQ-RV-_8biT6zj319mCW2vOgZM30d2kSw7j3Nmk1yxILk4sqYFAK4gqjIq3eNlq_4bH5zLxaGKjoQUu4-y7qrRmiNZoOhDXjhncuxbFFHUgxn78CJ5l30MPLqtxp8W4JIgAWd22s_nC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امباپه:
اگر برای ساکت کردن همه منتقدانم شروع به بازی کنم، فکر می‌کنم باید تا ۸۰ سالگی بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/93723" target="_blank">📅 01:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93722">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRBvFchdHR9mkJpyuGItUeOE5kw4YZaH2hSN1zxgnMHFNkCThIy-n05Y96sapHSCqMLaJk8hePNlJpnbF_vDQN4mnnnrSZCC26Yk11UbT0Syhcs95EnqPehCnyI8x1bc5xNVBH_5z_Ow-MJEGaW6nuOBQuXsI7tcEd9J4NBKaSTjZtfCypn5HDn4b1Rd7XGNCzGnreApLdEGILM5xRZUS8pHvhq-i3zLjLwGWnFzhn5lQWlVKJoeVyudzuqlGJM7vmi5m-GAToiBA1Evq-nnQTO17Y1PBngnl6-No3HhX_anRnJZS0oQix0vONlK-LhvwAN5W06KAdidIJd_Bsk4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇩🇿
ترکیب الجزایر مقابل آرژانتین؛ 04:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/93722" target="_blank">📅 01:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93721">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
توماس پارتی به دلیل اتهامات تجاوز جنسی از ورود به کانادا منع شد.  او بازی افتتاحیه تیمش مقابل پاناما در تورنتو را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/93721" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93720">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtZ4_0-o40mMQmMhlED87dziI4UDpCS-gWOC6I53v0cwJJmGhi1Wv3Ban7l6wbvl07CuCB8wKU3OAkyUkuWhvb892xBsDRZuIWFopEpz4gm27ZRpYOfi4Xd8-BK9wefGdoGnc8oOIlMv5Y27rZd9wZy-vH2O2EJCNv6UvpFMJ2Yi0L-DnUEsSbGJlmSfE3X2OPTJ07-6bEjsGhpZE_5LbJNq_LNcbpPbj3z69Fl-0tgZFl7WUqQN5CcKxQeAw_Z7ajm32NICey4bLBo7AvI6SS8J3cOvaDvMIosUAmFj1R41dcp3cgSegAhrdBA5PAwyEQeMTxt-OGMALURSCcOddA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بهترین گلزنان جام جهانی 2026 تا این لحظه :
دو گل -
🇫🇷
کیلیان امباپه
دو گل -
🇸🇪
یاسین عیاری
دو گل -
🇺🇸
فولارین بالوگون
دو گل -
🇩🇪
کای هاورتز
2 گل -
🇳🇿
ایلیا جاست‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/93720" target="_blank">📅 00:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93719">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbPbHExNkETAviCEFfne3NJEDmRBMhdHPVS9q9BGxfvxarTdUeZVoQQtyrl2qZH0e_6cYGJwrNxZ5XnaAjanLgDyKVnx71BQ-U606w2Ev7GboByWfu1WsujkM4tDa9CoY9Zav1l8s-5BhGaFCzoc924VImWhNv3pv28exkau28KVAjekR-zYRTRUnz12NMTxdzf3bebhWDXGna9j7NGnvBZsL4jvql9xaRkHICKZoN7CadhfTOfH-lw8LT4tGZFAo-jgiX53hn9MPbB7ifTbQOJqVCVtTI3kwlV_EzWTc9hWWrCUasUqdr16fqZeRtYrhyQ0NA3V2NbI-US7KkCvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کیلیان امباپه با 14 گل بهترین گلزن تاریخ فرانسه در جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/93719" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93718">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93718" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93717">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QM0eXHoPQ6b3ZilAg5HJ2ZjoS61grQoiQUsvH1ksf3nme7XpkBDlSScLJ9Wc8MZ8YdwbqYPpwHtW_0K7ry6OfsRM1naM7iNkG5m_ZtWrlH0IVw2HRVMT8Ql5YGqQ4apJQmTBVsfKMT6AQS5gqMoIHCkFsxt6djqsmBgGanTAe6K-GVKLjlKYUAl8lGdcrSNo0kZOHhu06WBxbXj_QsWpNhNprts-vrpQPRDRFlEFQ7hyF5WZBtly7YAglz5tOjQkj1ff_eVlpc4DR0XsRkGiQehXCev7IACilgWHRQkyRvpxHb0rHjbqFbsZ6IUvMBZSQzLh37H5_PN3_HcJ6pvakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/93717" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93716">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5Grt75o_phKCGH31jmAqyQgMjM60-JMBxIrkVY4x_2YE2kmCIFDzfdH98U3296F9mVaAW117idx85b_gvmXrLprKzs_fX7uzH3B8A40ixCJ1W_XO0Y-S7Pol-Vjh9FKMaEoNCIrz2GRJZ1U9spC7EyfqPc4Q0xFGaXsUUO0w0QJFptrSHDGcS7XoyULCH2Fb1ZuujQcILjtLZcvfYtdTc9ENBayDiH3wC7oYqyqLdrR03suRWDLMU9COQJ0pVxbDPuBW0KtuFRLt25enugRgLXOH8aOWKamFEz2Ko3hOjWZkyNfiupfRIj_v-FIzJzPPwROzCVSrKL53CQSVebNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | خروس ها گام اول را پر قدرت پشت سر گذاشتند
🇫🇷
فرانسه
😆
-
😃
سنگال
🇸🇳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93716" target="_blank">📅 00:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93715">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سوپر گل امباپه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/93715" target="_blank">📅 00:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93714">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f0860cfe4b.mp4?token=NjAEDyOdfLrD3I43SxXtxBQRKpQUWaOVYbloTGbr-U-Y9PrIh1VEsoF-dGdiykHuIMMZcOFfVrhmCUSwtE3eeCnw5lLqtFMw6GYDOoKhdXGkOeKXY0bV80nzAhjvXi5490NzhwfA4EM6_o29kV4xVFFkvA3uGP--cVGYVkhorkSwDaWRUk5OjvQkdxciO5r6B55JUCsDDgXT9Frw7gBjz3ZLqPOgCyuWR0JBRIjyIPgSfEvD3udqbShTASEjDpUiagLg_zE4J0wxJ2ak__0YgaGwnxjUFIjONubg-HjBt6bEtu14je0-DV8tJOBHwy4f_9F7cmWNigNbDqIOKAZKmD5CCp8eqslIL32Tt16xbApDqG_7PRRysluy2bT2me-olRykNlAnqfMhZ5ry3zx6pSMeNf23uBArEKOXNi_HgIsTWSIhX8CHQKWJpUDJUiYRBJ0wzxLN0mU6hyYyQO2bO9HWW0188gxATktKGz2O2k8qfN9PYRr60FUJ3kV2zJJcu2Y45_UVp8RuQvIHV2RuX3V5kSWAIMh5Agh84rf9h-7xjrB7xIsReB2IG3ior3ggE2zAWEOIUxFXhwWboArSAR5uJqdtPEeQ_J7d9hyQrcFuYOj03Ngw0SmG5a69qfabxOBAZ_-gIcLXD6f58_jo4AttTS7PYOhiZL0YxORGoao" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f0860cfe4b.mp4?token=NjAEDyOdfLrD3I43SxXtxBQRKpQUWaOVYbloTGbr-U-Y9PrIh1VEsoF-dGdiykHuIMMZcOFfVrhmCUSwtE3eeCnw5lLqtFMw6GYDOoKhdXGkOeKXY0bV80nzAhjvXi5490NzhwfA4EM6_o29kV4xVFFkvA3uGP--cVGYVkhorkSwDaWRUk5OjvQkdxciO5r6B55JUCsDDgXT9Frw7gBjz3ZLqPOgCyuWR0JBRIjyIPgSfEvD3udqbShTASEjDpUiagLg_zE4J0wxJ2ak__0YgaGwnxjUFIjONubg-HjBt6bEtu14je0-DV8tJOBHwy4f_9F7cmWNigNbDqIOKAZKmD5CCp8eqslIL32Tt16xbApDqG_7PRRysluy2bT2me-olRykNlAnqfMhZ5ry3zx6pSMeNf23uBArEKOXNi_HgIsTWSIhX8CHQKWJpUDJUiYRBJ0wzxLN0mU6hyYyQO2bO9HWW0188gxATktKGz2O2k8qfN9PYRr60FUJ3kV2zJJcu2Y45_UVp8RuQvIHV2RuX3V5kSWAIMh5Agh84rf9h-7xjrB7xIsReB2IG3ior3ggE2zAWEOIUxFXhwWboArSAR5uJqdtPEeQ_J7d9hyQrcFuYOj03Ngw0SmG5a69qfabxOBAZ_-gIcLXD6f58_jo4AttTS7PYOhiZL0YxORGoao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر گل امباپه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93714" target="_blank">📅 00:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93713">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">عجب بازی ای
🔥
🔥</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93713" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93712">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرانسه زد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/93712" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93711">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/93711" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93710">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇸🇳
گل اول سنگال به فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/93710" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93709">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلللل سنگال یکی زد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/93709" target="_blank">📅 00:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93708">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5vyU2dACaeDD39pr3b1Yy2cNKgvYIZoz-MfVIlF5yeVhHsjwCil_8ACnzcbXvLj9qsK6akNcltY1bEn0tD0s_VN9sEONGW-yxFlvCTuyOmMaP_LLSxxNX-H-8j4RtCPCG8BB3sdLq7KktAB96PvVrKUdU7Vdj5SGe-SsBSWXxPffVCOmYvWQT1VIHyErBdREu6qNb0ldx2T0zbzmP-p1w0NsozC4BNYEaRKNZYaREQYo7NohFhQsvP7REDmWM8ooUfPvnQfjrqFhNPSnqnlxxfE_y75Dp_QABBjiJXTtZto7_gQRyTuSfHAhn6cvIe_FK0CfJ18yTZzakTFJmQzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
گل دوم فرانسه به سنگال توسط بارکولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/93708" target="_blank">📅 00:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93707">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdxysGvEX0J6ZCnmOUdvuO8IKJOXywwnpE3-gk_cEhBrNDit3V7P5OLkzKxrpkOlCCvDLxAOrtGd-xJIk3T45-5nVa30DIiA58W-zMZyfAx5y-j9wH5juBu82QWe-w8bFsUGSMkrf6nIag7lUrejzFR8tXHkMYcY5N0loOfZXTeaBHV5OITXFMDaMimx0gAkysNe16anobqLGtnAA7Vh-b0otztuv4U75WhWDRwfE-tH8BqwN3fd8aODjk7HDA2JuCr_8QLkTuTS3JIMEcdCPyUcGupWKlbxGRFi1j_qEwFqtIHnNncCYlsKX859uaD4HOy66X8Wz2kfKEo7VONYZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
گل اول فرانسه به سنگال توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/93707" target="_blank">📅 00:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93706">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇫🇷
گل دوم فرانسه به سنگال توسط بارکولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93706" target="_blank">📅 00:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93705">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بارکولا</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/93705" target="_blank">📅 00:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93704">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گللللل دوم فرانسه</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/93704" target="_blank">📅 00:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93703">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5QxT3hF2nmNMysArGv89-D8gugf0jfa2yP3koMmdkNfN2oFSJww2gFh633C8ZtlGi1YRUwI8vnyoFGg3VkD4yUcv8M4usu-g2S0PLRiFvUW56S1vrvGiUaKUEd0q7vLiM2ZAV9prnyGzy1R4ebs2g3z7vMaYtRniKZsxq28GiNK-0I4itflo-g-U38BzTjcIOZcEryE5KY5ZTMLd8YCoM9YY3qEzvL8r4FwDbFLPy_nb4LqGFfYtuXo4pNNDF3lL3oEHV-bxneM_uOvcCJfLbP-yH2UDsshhwLDO_DafmDftu-4YDW3a8hFg7AN8VF6UZiLOV1sDe718Ytl4xTT-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
ترکیب عراق مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/93703" target="_blank">📅 00:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93702">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLMUG7WgnX6VmeWrCX4aLLI3xyecPMv2fZ9JCqWzNuf3pwbp4HwwnKjT6dn71WV4D3s8sa-Gi-zUhwIqCDF4tg6pFPRGG5J9brrwklFuZ3nemiq_K-reTibgnauYqAYfxoK5HstbfRXw52kLZW3cyAQ8y3PYOXH6Y73iIUPcaInjXpYECZXKKs9_oR03Cgr2OrPywhWrHnSDlx0Y8lfeETP7iFtvT8R7woRi5CHUBKQ9HR7epaqH1BD-O2OAz_LfSMqmPJfMUgdaVkFJw8VhcnBwQI41ZjAClpIHOVhcwpMuRbDONKzApjuKBTgACon3u7aHuBQeGPrRghU8HC8uzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین گلزنان جام جهانی:
1 • میروسلاو کلوزه – 16 گل
2 • رونالدو ( نازاریو ) - 15 گل
3 • گرد مولر – 14 گل
4 • لیونل مسی – 13 گل
4 • کیلیان امباپه – 13 گل‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/93702" target="_blank">📅 00:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhjhUtUGN3PLLZR2sCwb83g3AoyYyTNVjZtg3gPqqd484vNHWCSCq8rN-vNTJsj2RLsqlQoDSPiYaWC1v3Bosr_PsHWrjliQj2HW_JZwBoOYLvJ-YcmFVeJFCjamQMhQiy2fDZzdXUQvgGzRLYPZ8DBRiHbGvnHqXMbKqWzqqRyv6WBvohzODrVX7YdmSLS7D7brBCHfIt6EyBG3ky4WM_x8J-bUQMxSoj6dDE1IJbHmgyDSrHIMHDGb_3SsL6wcShlGpRcGaktaSrDD2KJIbgqopAKGarnYzNvpl1ScqPQt62NLwuZJTOLycLl-_VlP1YrLYpVXbfjw-EEA2i6uew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
ترکیب عراق مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93701" target="_blank">📅 00:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93700">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جکسون کبیر گل زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/93700" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93699">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇫🇷
گل اول فرانسه به سنگال توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/93699" target="_blank">📅 00:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">امباپه بالاخره زد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93698" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93697">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/93697" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93696">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بازم لاکپشت موقعیت خراب کرد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/93696" target="_blank">📅 23:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93695">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">احتمال پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93695" target="_blank">📅 23:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93693">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">احتمال پنالتی برای فرانسه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/93693" target="_blank">📅 23:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93692">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مندی بازم واکنش نشون داد تا فرانسه ناکام بمونه</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/93692" target="_blank">📅 23:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93691">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سوپر سیو ادوارد مندی نزاشت اولیسه بزنه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/93691" target="_blank">📅 23:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93690">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شروع نیمه دوم</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/93690" target="_blank">📅 23:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93689">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxN9B12D8CkdW0dhxNThsP5_9189LcauSQ3VR88WP7MxMcjjebnyPqqDTWu-bMVGLnY1AiL6mBnTdNx4-_haC4pbL2ToiEc8urMHieY5WXjb1bd2Bk8CUcI6AXeFAyEmLW723x43cwPgM5Cx6D-FeAe9LC3_3fnPYKq9VEt18nY6Xf9pCbBJ0UFFt7KkoaYS79u_raQIFmrlrGIrPaMMVeCjvHnFvV6UNHa1w8ItWmobPmUXxy20MAq_oCLd6W1yYQiEGyFMNCzFjNFqxq1vuy-LBO_LmD3xyyQo5hE4aLgxm_DaLFaMsxQ92EAbXi83stABnAZfAy_g4N9qbAGyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سار چجوری این توپو گل نکرد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/93689" target="_blank">📅 23:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93688">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پایان نیمه اول
🇫🇷
فرانسه 0 -
🇸🇳
سنگال 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/93688" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93687">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چیو نزد سنگال</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/93687" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93686">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارشگر صداوسیما اسم فغانی رو کلا نمیاره</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/93686" target="_blank">📅 23:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93685">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نزدیک بود سنگال اولی رو بزنه</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/93685" target="_blank">📅 22:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93684">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بازی تا الان جذاب نبوده و موقعیت خاصی نداشته</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/93684" target="_blank">📅 22:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93683">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK0QaauxCriZAITOpg3IGieJ7gv8RgQU2N7HfsdgrqZr-7NboUUXmbGm5pQ7bvmFPhTSnHYgJ1eqqGB8twZp2BcxZ5k_5b6XvvSqwlWE_uIgNxq_mmu3syAVqXN-T5AubTgQROniVKiGkXZOSR4llx_q6KSlQoDcZ1bYpk8wAhVscqGa5exkKb9OCYYhxk0CtBPQfull7-iq8Zm3Wx5gUOCmk_hHnJBISBmb1cQMyIMdO_NKZO1A2Oo9ro3_fdBz1a1fh2YcrCFpvEnPGC6aNMkM1ZEQVosm9Bu5qr5vpIBDJXGL-h1BXvlikbqFiX-rhQKpqcu-VqaX_S6R7rGvHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
استادیوم بازی عراق و نروژ استادیوم ژیلت نام دارد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/93683" target="_blank">📅 22:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93682">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بریم واسه شروع بازی با داوری فغانی</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/93682" target="_blank">📅 22:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93680">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzKJQfIvVTI67GLBZLv7_3jgyMsM15kqDYTQPEFIc3AZVKF08wDkvdQbHcqA7ijIfVmNjpnLVvAiv5qjL9P_LY64ZwZuiTLXo1o9vw10wzjjY9ZIw4ovjWR8acXkb6dcRUPlODfuWBsNDm3E0eo-8KdYRDMD0_2yhKi60eTvFpJ4tM7Ub_cI4uJFNkL9A1p1IsAYyhqTJ4rYg4ZogutPonynfupTpzEipFTfbDVSwKB0_RhP2j3MvWcI0ypFtb6o0ELm26Fe5oWEDduCkDazPygqXKsWS4yAZ9qmkWFaenebGqcxgxFysvynVf2CDmWiWlCV0hMwfzbN9l8nT8zpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJ8z6O2Y3YmyqfL3l09pNnP1OHHX-xksriXevdlKty_Mzr55Hcb_XB3Qro4-p839RR3WEsjGPmRXA-YRUdG66HsLFfKBubSriab3Rph5BRwWGCPR6hlwpYizWJd_j2mxm-qxxnec1RTEwCh86RIzhj4QsrzASEil3ntP_MEJRuA0JKTDlwtnlc3hx3JRIdnnuN9KFZelJKPvyPGlNjWie0-NAB5TCH6dhM5dDKcZbx_jnUaAHvcyxVHWbBWOahiZxwrMjAlg5h79taI9EFq5kPHyaTwxAIOPvy-yoleloePcECIhAtIxr0M5xPi72TxQceQ6O8GcoaPeSEWpyIhLig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🇫🇷
کیلیان امباپه در جام جهانی ۲۰۲۶ با بازوبند طلایی ویژه وارد زمین میشه؛ پچی که به خاطر آقای گلی او در جام جهانی ۲۰۲۲ روی لباسش قرار گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/93680" target="_blank">📅 22:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93679">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Poy6prfORc_D1wN23bELEFoGbjcHnZ10f7fT8W1hU4w7wsr7ZIWEH1sceBjFntSsJlrBvWKHZggAH6NOUrDuahiRLSPQuHgvT5wH481-5uJoQkBVOlf0TUAAXGHUrCD3wNadS3WsPyMMsQ7PS2eXaXjx4eh0XI88O_MO3PZmT6GtSN35RcUwZcejgIgQH9QjX24S5nTLzMScuDdj8PiI47DMrdx-e36SMsmX7RBM6MFkCp4kMtN0f4Z6soSN3tvr6Ip7zwBMDgGFTsKRka9Myw27MY9rKUKsaBMhmukJ2iVqy3cMXMOmNVNKCT3h4kk8kug0Tn2ZG9-20JBOF_ElIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
سادیو مانه قبل از بازی سنگال مقابل فرانسه:
«راستش حس نمی‌کنم این یک بازی در جام جهانی است و بیشتر شبیه یک بازی در جام ملت‌های آفریقا است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/93679" target="_blank">📅 21:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93678">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU9SdDWb49p90RfE6hmVFSHdYiotc5aSvS7JJXiXTuBf77lZ0O0dAQ6zNDreFiY26B1Fvt1-9rMKJgrI0OZZX_O9qJXDs_KQTXgd1HjleuvjWZyA73Db-xeXGTmzJCxQVi4_CmMOBqWiobyy49ZxgZs2k-MDNlHaKR6Xxl5YuH9QBvLrhQ180Wn9HlPnKeSWHT1cJOzgHiGWsw5DhcdFFLnWOKvtW4-groIBV9AkK9GrJDPPp23sgWD6nG0RGd9tFuFgfsvBie5gVxtgDen9SN77aqgOQTJHJrt9FzXK23AMMAPUn9e8r1zxfuv9c8ODt5gRtIgjr4QGIVNBgSXMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نشریه‌ معتبر ESPN:
علیرضا فغانی که‌ داور دیدار امشب سنگال و فرانسه‌ است اصلی‌ترین گزینه فیفا برای سوت زدن دیدار فینال جام جهانی ست، و اگر اتفاق خاصی‌ رخ ندهد علیرضا فغانی فینال رو سوت خواهد زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/93678" target="_blank">📅 21:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93677">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaFSRjNNP8iNOQam-oDkyDNtwoZiUHJ3awpDiz2wrnxEyqs18yMRBh2qG1ulMtQWYDiahvdqTXLE3cvzqRJdQ0QmRdu4YDB9y9fJhlZysZr9RogelyGtUHLplUl98v0Ue9mqE60FI4XMC8hBdWfYfohsLAakGF_1OGRT8h8fkBniMfydtiWaPOrUt00-dSEAVy4BBeV2pJEe7-EYCwPhzKZ97nNE9-NorWaChleAX6ksAgm2kolE8GZotCiUHkjE0giN3lBco-0G_PZKjSpVpTriurt63dmiB7D_l9g1SmHPL6lJKKJL4dM_uwkcd50j5jdwfa1Z44PgQxhYL0uy_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار هم بالاخره به تمرینات برزیل برگشت
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/93677" target="_blank">📅 21:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93676">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa7c65311.mp4?token=JoH7At80ZXyf2UhcvXpcUfJJRcpe6E9ePmiYO-ygxTxqs_igxEhifw3UrnQ6bffO4I87RldfzmaEThD2wJmgz77e2sZmOOsG3qSc8erJj6FdJerQ-2S2pRwrRE7_IhEMYbg5Fv89N7ZqIUpxjcf4h_xyvpJEi44oHaFdwWW60jQdRJUKsz6aCmvmUJV5vwrOXSv9hT-Stb54Paf8xTiRpfTy1QDZGSYaxXgNXE2E0WIzM2Egv5_K-1SaKWlT9jtEC5EFqg-vjHipInFj1K6uQ-NitohCUsqXOEw6v65lhoKt7PK-keTFKz4NHYo49ZsMqbFoSZE2LDkfK3NeSOInYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa7c65311.mp4?token=JoH7At80ZXyf2UhcvXpcUfJJRcpe6E9ePmiYO-ygxTxqs_igxEhifw3UrnQ6bffO4I87RldfzmaEThD2wJmgz77e2sZmOOsG3qSc8erJj6FdJerQ-2S2pRwrRE7_IhEMYbg5Fv89N7ZqIUpxjcf4h_xyvpJEi44oHaFdwWW60jQdRJUKsz6aCmvmUJV5vwrOXSv9hT-Stb54Paf8xTiRpfTy1QDZGSYaxXgNXE2E0WIzM2Egv5_K-1SaKWlT9jtEC5EFqg-vjHipInFj1K6uQ-NitohCUsqXOEw6v65lhoKt7PK-keTFKz4NHYo49ZsMqbFoSZE2LDkfK3NeSOInYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این وسط سم جدید طرف رو ببینید که مشکلات تیم ملی اسپانیا رو براتون حل کرده
🌟
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/93676" target="_blank">📅 21:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93675">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان جبهه اصلاحات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx84ZjWErqitjUbsrT2ioe_QGo77VVNTJRFmF3RWsSEuZhFjDnMBP5jXT33fOYcIGsn8QkyAuau5zzpfWL8JfgPk_OO2DNE5-vOUUqaYbDQJV6uMHmSORlnVx7E3X0i2iEeeKXDieJD6ddWoa-ySlUYitWEEbnWDM--VgRKhmbwFP_53iCNrSB8ifR1Lo7336ksSN-xkK1QlEG11PXBMdIN5Gcti6NxsbQ3Wy_Wk86mQa4a44jZhuiEn5qHqq4jWQzNj2OoPTgYnWkODcgwioO85ILl_QIeF1OgKKxVcfGFKdnEgwg13w-YAryyKf7iHTVf7ncD2-_EP1cw9g_LsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح!
@iranwprldnews</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93675" target="_blank">📅 21:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93674">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-kQrjyBfwoI36M-yE986pRnp-TcDjO6hRiytYB3JNnDRVgrqzHEc9bNYiIHOWKqCTkhWOVCuWIMtmRfACXMWe138BaVYo3I2bkJo42r75aq55g9gzIsNPQhq7rOscOI-fWlWrMLsfR9zUK60ELDJ0zUb4QUW7l1XCwpvoJLSeP1equjgoT5gBJ_wMpdf6wzynt5cn50I7Q_K5hubRORyaLUNR9ivnLMIXhOPN7IqLIZINj51oAgXyagBIo5eVnuJVWYHuSXBZwPmuTsJIGxh1X28Tage_r05c_LSr3AW9ZWZQwhlMvwle4YRSJj2uQnVEmEVcziBxpfki2abpnBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ منچسترسیتی با الیوت اندرسون به توافق دست یافت و حالا مذاکرات با ناتینگهام برای تکمیل قرارداد درحال انجام است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/93674" target="_blank">📅 21:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93673">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4x_mkBzWhdTWeXgCARZYCCAknDQ_F_Zr8DvqkbyplQ9yVWjxaQJWY_OZ36T258EikCzfTfxq7gHqaNxW59I713XlAUg4d4u6SQN19YXq1c0Ld8pb2xlcBfvlg_b4TbVwI3LSWiTUO0laLRZ-GDYA2_x3eR2cbiacc6TY_IhSCOcpEl6ZoJTA6jLWzyPmeeUwmNy_JoijaCuW2G9HeCxU-P7t2qjhDt5PodBs09DGDcDVZ_zxHdsGWkuwIpWBSuofcyzbaZL_LfIOe5rAkjnRy3XGJuWzoQps-QIUgBlu2lGrYXcIsX9rsWyW5R7_DCVTs4q0YbV8SI0M74TuZWjSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
امباپه امشب نود و نهمین بازی ملی خودش رو برای فرانسه مقابل سنگال انجام خواهد داد
:
🔝
🤯
96 مشارکت در گلزنی
⚽️
56 گل
⚽
40 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93673" target="_blank">📅 21:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93672">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIQAqUJNcGrSOi9GnOlF_M3Dxe_c5u-r1oxexiWpBBnqT5YULrp20qkVrBJ3R07YcTL5-62pXy0uzWm_3V-hV5Mns3_pCADIgXIFQ1menDElyINv5lZUF2hRYqbg-FEk5N_fpA6iCFuS-yyR7c0D6RVgIpzJehEXckMKNDMNNcXM_LgvXA4mj1eoTthEguN68xCxJZ1vvVLbbqAPnqm_rvhizJul5vIqOD5BDRwDqM241gqyPFpO4i_3sbiF01NC4ROzLT1T278sQC1Cg91lg3_VCvUP7xxufxGlJqvGdnkhPfK5D8e8cr60uDkIxbx_oqs5EGaX6wxb3rzq-R8ZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب رسمی فرانسه مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93672" target="_blank">📅 21:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93671">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWamgFwCSPqOgWC3b4X7C3NT78PAqOjvD1fYgaoLsb_IptrGZXxtqB4N0mLUQGCU7N8PBvsSfDiE2snGpWXf37TXqeC0Amocz68Gu4gPJH6klMEdNySg7T9RlNPxEzvQEmrDgQqm_fd85DAjPRkzmTAtkyml1KuL6V6rqOvieBqv9LfJeSC2zGApTLp9HB6DTuiEgN75eG0KTbkNz3FVB6AuDsLTgoHoOh4ypQdJSCiwa3aa06HpbCCLBu_yY3VCKdr9fHO7rqQwcxvYu29Ysy-J9FORLKfeo8kZAl3e-JjShbZv4BqLDBpXE3Fv1vEloGUhxjOc9iPlK317TPTrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب رسمی فرانسه مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/93671" target="_blank">📅 21:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93670">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNqBvNVfX7DSDgBsWuD3jjvvhqP4eND0JGXOzcpeIJGFyG-hPFZ3K_yGhwt8-wTbfEPdljIrGRk05qImJDXYUBBKPwaDBYh3wxooTiDRYE_nvpgRyXgC6OOXAVdM4Lc1OMSeLVGul4c14piZhmxGZbce6k2zkBm6CjQVUY-gYgKzZBI21Q36mTx1tM2kF98EfL1itxokTadAWVup8tmG9G1OFKKXvYpdTSTCvcsMyYp7L9JvD2XMUQQ1aEzTuZnpMiNPnOzPk0KSw6LTuVaDy25PoYaeBzB9ziU8ZpG-rGLEv5vLsSH_KJ3LSNvlkN8QUuIRjkEzQOCK0SWuFgDW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب رسمی فرانسه مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/93670" target="_blank">📅 21:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93669">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TiqC7n6AMnt7vwy4Y59_Thh3wF44G8WPYtdf-0-9xL24hxkKO-gLVr4w9R6v133tkHtFZ8E-UWOzHDa4Hnkpcp7tCwjoo1XfZGSrSOIohb3Jg7xeIaYfBjMndvjM51Q_m-A4-oLebOeTLnrQ1fYXjRrEui_o2todiCB9cbWGaiOOpiaR6LNtyhZUizkPsKD41PtkS68pW0zk30AaWSbwWxLmW_5Guf8b_e2h9iJ61M6gclgsQ8WslRDyyGwZoqX1m40z8w9hI3amWbdjYOw4J8oz0TBu09-vA8AVJt0m7McYojfovVBNIzFAG9-i6YvCNuV671qZv6Y0DSdS_PbJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
🇪🇸
آقا پشماااام
🤣
🤭
🚫
✔️
این هوادار اونلی‌فنز معروف اسپانیایی قول داده از این به بعد به ازای هرگل اسپانیا یه عکس یا فیلم رایگان از خودش آپلود کنه
🔹
🔞
💧
🔝
👅
🏆
عکس جام جهانی قبل که خیلی سوژه شد رو داخل لینک پایین گذاشتم
👀
💥
🫦
🖥
🔞
https://t.me/FoootyHub_Bot?start=VjSpmD5b
💧
⚠️
🚨
🚨
بدووو عکسو نگاااه کن تا پاکش نکردم
🗑
❌
☝️</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/93669" target="_blank">📅 21:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93667">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TrSL0A8zECJw3aGnoeGZ2A28E-hcBPo1VdSVvxd00EIkvigF-IWHLU4l7Qej01HbULLiBGzz7mzQ20ZM_pHB0VWOwsbXP4yUDC-sgm8cn9T5YEZsKZV8yuz5XpJFZycvgP2cuth_464c-3KNtfJCeAqSt2Nuc5LZT0bbpmo5vSZZFCp8yvLB7ZDU37pOcylQpq1LnJLLzi37ATmoUHeF9KTERfejhTC74hiQUJqvn8tXI7VJzBWtrB0my8Jf9YpFxpQyYhpz31l9Mj5mtpe7iNlVcQl3JiosdF8mpfxjAhV6ysFeIJT7pEGouABE26JKJXLllRAHGRXH_X18_Wtb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOHHhxWvTsV8CCR1tCuO9U6Dwbp1pSKfQj9lS_026ReWBfKIF0Wi0aso16bkEs8nGx4C7-uH62QzlM5Ck4XIle5muPLHq-PDWqEci5RceKEXHkR2BYPNF8g2Q_RLtZKgd0SFeMzVxCqCGUL46CMQtCtwT0xsY6pE08bUavFE4dA58DmkTWcLuWqer8GJgnl3_K00zCwfWByq_AoXNvIz4U_svK_irdNNdynlreyxbyvJWkCt1auLy9nGK51wz1hBsdwH2Ekp9tnK6yZMyapnOEbO1fk4uXgclRiF6TpOCt7bsa9sHIxzg-pcZuhyRese9E0g2QvgeZyAS49oKohp_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
جاشوا کیمیش: «دیروز در زمین تمرین یک مار سمی دیدیم. در آلمان چنین حیوانات خطرناکی وجود ندارد، اما اینجا هر لحظه ممکن است روی یکی از آن‌ها پا بگذاریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/93667" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93666">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpxgsvDfVA0E7gIAl9BgB3J0aEOWdo8pSr_JZxbDrXegQPWsXeEu_cfxNpWQwdp59ivGF27LI99ezHOq_uOp2pNYin_FiiBaUo2sd-riadGVtBbAndob3Y5QH6QMZq6R7uM3OGn4yCUoYmGTRLy0wWFLKaddQWSGz5EhmXIFDFudaY-tgGNBp7GlEfvcc7KcUVFjulW6pG3DmOp_WuPRtL9HfzSU-qLKlNSjuM8JwbZo1Er7fG4NJn8zolkJbu62s0hjLHKeISMaVX6C_olcb8dkNdNum5mVLFjCfWjEezGKNecwtoUoi9BQImyK25u8thYyDVrn_ippNZziZRcepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووووری
؛ اسکای‌اسپورت: فلیکس انمچا ستاره تیم‌ملی آلمان مورد توجه رئال‌مادرید و ژوزه مورینیو قرار گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/93666" target="_blank">📅 20:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93665">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a295b95196.mp4?token=ne35GPzToioSfe21L5IAP5l34ombYHactZ2QkWBts-jy18ERr1ZSgkawWTY26QP9QxL0-TPZDkohGN_v0s8_ECXF3Pc2RBGROqpqeh7CLBSIGE6cd00Q4Tz4jMKoXakI6fk44lc-ypNsDnd0auo3CrwtVhfOIVa1pKWALIRCCi1nyidPHSKlWNf8zuP5AUXMF0ZVFcC6vxXbxZ1b_6YgXORp2j_k1Izlze6jHF60W8AKEUS7TrfeQCsR9jH9cMdZORMHLoIiwJ1fFvpWHfSf2WuZgPEnmr1D4w4KFnK0x0Rx0xBXYlDKuLQ6a1_T90HF2dGeVGZZAuZ0bUzzJCdGvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a295b95196.mp4?token=ne35GPzToioSfe21L5IAP5l34ombYHactZ2QkWBts-jy18ERr1ZSgkawWTY26QP9QxL0-TPZDkohGN_v0s8_ECXF3Pc2RBGROqpqeh7CLBSIGE6cd00Q4Tz4jMKoXakI6fk44lc-ypNsDnd0auo3CrwtVhfOIVa1pKWALIRCCi1nyidPHSKlWNf8zuP5AUXMF0ZVFcC6vxXbxZ1b_6YgXORp2j_k1Izlze6jHF60W8AKEUS7TrfeQCsR9jH9cMdZORMHLoIiwJ1fFvpWHfSf2WuZgPEnmr1D4w4KFnK0x0Rx0xBXYlDKuLQ6a1_T90HF2dGeVGZZAuZ0bUzzJCdGvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇫🇷
پل‌پوگبا قبل بازی امشب فرانسه اینجوری بازیکنان کشورش رو سوپرایز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/93665" target="_blank">📅 20:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93664">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS3Rub1-cGv6AefqNXwuFeC2D4c0JaxVamx63alVfFPaF23LdQ8Un6rxC57HI2VCUZe9RouhXtANOx62U1jzsMw50iLu97fCf7YmlPlbz3TSnNc4anhcNphtviWR_wcb-olyNXxcULdC_XTHChuweJNc6kDf9BnDdm9XmMXVVXf6wLRQWJ6YcUlS_MsQ7dPo6ykELKRC0ckXsnqoRuFAOjunA4sz_bHjTSSWErI_apkPux83V6rPj3X7qnUnlACdh3BdjcR-hVG1YdR-dFNaHeM6bP5zZ9yPkhN7nzoIjHkH4auqdiC3kFm6RpVHu859OKNIBagUaOeD9O2YXdhGlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
استوک‌های لامین‌یامال در جام‌جهانی با پرچم گینه‌ استوایی و مراکش که برای احترام به پدر و مادرش هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93664" target="_blank">📅 20:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93663">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab33a3bc9a.mp4?token=FQHzMm34THCGFc3wKgcbTCTXM2FsDwE0gOW5qTQGb9CzxNHIa-PRihd9xkC9UrkrlXVCnWownJ2doslU06_Htsb2MSy40wH2J55POnfL7yrUKBcDfHutXr4bP_PNU9n7yvQnu8Qu9Otn_KfndXk4NYTrrxC8jWQuZaa79v1lXsLJEXykFrFTjwCc7cOlSH4iR30CRXKZE0STLsCNIxsX2Wf4BlDU1bulZpc4nqgQOXrkHA3QE2J8bbcryXstuW7fobtmeflGmAakaGKaDAkJM5MoqUnJ7KDcjYB2Oh80GGMefMvxkJ8i7bXvPP4M5l5V5vAYTku0DvOrk6OneoyGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab33a3bc9a.mp4?token=FQHzMm34THCGFc3wKgcbTCTXM2FsDwE0gOW5qTQGb9CzxNHIa-PRihd9xkC9UrkrlXVCnWownJ2doslU06_Htsb2MSy40wH2J55POnfL7yrUKBcDfHutXr4bP_PNU9n7yvQnu8Qu9Otn_KfndXk4NYTrrxC8jWQuZaa79v1lXsLJEXykFrFTjwCc7cOlSH4iR30CRXKZE0STLsCNIxsX2Wf4BlDU1bulZpc4nqgQOXrkHA3QE2J8bbcryXstuW7fobtmeflGmAakaGKaDAkJM5MoqUnJ7KDcjYB2Oh80GGMefMvxkJ8i7bXvPP4M5l5V5vAYTku0DvOrk6OneoyGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇬
ناراحتی محمدصلاح  از تعویض مقابل بلژیک که در رسانه‌های مصری جنجالی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/93663" target="_blank">📅 20:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93662">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7qxhu3KxA2FBMn_uvkKekjROgBXktFbx8M4tTHh_q5OI7e05vAJlexswTPIX5Z_qeuERaFoU6q6A6ZvJJ35aFjzCJQCvu4rpefYtSUirLu71GwMX1FLFaRVi76q98IQVHYxWLpcGH71fltqQC32pLmUcigTW6GCmlUddQsJ71V5Q86HdhYBDOxMsZ6dyTlTLzA2Qs1-CidRPIPjKWHUCVU-YFV3YNb7i4VgTU3GIwRkJY5jTd6JsCyUYcesmIRM5fHLXDBItVhn_gFYrm2536OAsbSp6uQwCzHWRXHqre8ualE2vYjooqvYd-fxyp_LYfYDol-dF9D_MFTAM6NZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
🆚
🇫🇷
۲۶ خرداد
🗓️
۲۲:۳۰
⏰
فرانسه
🆚
سنگال
📌
دو تیم پرانگیزه از دو قاره متفاوت
؛
جایی که یکی با تجربه و ستاره‌های پرشمار برای تثبیت قدرت وارد میدان می‌شود و دیگری با انگیزه بالا و روحیه جنگندگی به دنبال رقم زدن یک شگفتی بزرگ است.
⚽
🔥
فرانسه، نایب‌قهرمان دوره قبل و یکی از مدعیان اصلی قهرمانی با ترکیبی از ستارگان بزرگ و کیفیت فردی بالا
در مقابل
سنگال، یکی از قدرتمندترین تیم‌های قاره آفریقا با بازیکنان فیزیکی، سرعتی و روحیه جنگنده که همیشه خطرناک ظاهر می‌شود.
🚀
⚡️
آیا فرانسه می‌تواند مسیر قهرمانی را محکم آغاز کند؟
یا سنگال با قدرت و انگیزه خود، یکی از شگفتی‌های بزرگ جام را رقم می‌زند؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/93662" target="_blank">📅 20:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93661">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4yYjoXfpiHF3uhDt6-0haWLmcuDaN_JLeu7_OmE6la8bzGoHnibAksqgex-U6qrTjEFiNdbrEEIsPE6ErMrZwjq01dmc2tRR-M5HTQaKdA__5LusBXPD0W8ORgjS2zbdCQSXTM-e4WenCm1k2T4AVF3gJHv44w-UeVM_pTFPcMYtU1qeLwkxsHCIj8ycIMuF1VvSlSFkJwn0UMvo0OYlXR-LGbP729aFHX5uml0qqZ19cIBfmAlzaJ1sce0NAIuzXshNbwPzR5FMOe3W_gLolovBgfB0FBk9G2HZ_j7YGQNh-e7xZHbHIgvTtk0qT-bgbalQCGeXzHzh6Ni5TRTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
ورزشگاه بازی دیشب مصر و بلژیک واسه خیلیا آشنا بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/93661" target="_blank">📅 20:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93660">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA-iYr9jAsPN2PdvPyUoGoHOnpecF4Z8Rmg8RMfjZVD8Cenr2-fPKMeGqvHPLrRtbuTlnyn5Er-eaTjI8UFVrcy-42MPWNvIKpuHej95XGv8KZM9-EW4EQiczRQBOMUZ0GHCNIWm1IG_vq8EUA3DvGD_Paan_URUKQQlPfhOpesyfYdJ2-qpkZUrHPnzTlmHg3p-DxIMosjn094uZAl0aF-7VqM2N-QFGO2PPCsEJWep_ieTx4xE6K1K7fXaWHBhCgFs3NPdhUnLFUuyOYm3zk78r0okmqeNdHSbmh7qwW2neSS6Kw1kElM4ya-Xrj_VJhFyuwTdZ0k4vyuzpmMnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
بازگشت نیمار به تمرینات برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/93660" target="_blank">📅 20:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93659">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6713aa8d1d.mp4?token=Ia6voMxKUGSxcR4SVbh15uSRukjDzSGoEMc5uLgruoHW4q9U3Bn8SUJXdTZe9eUzhOJjRxAljDZuzNbCQaycYti-g6to4FLQn9m_EcrYta8_O9wHMJ0wK0rz8YsDurx1bxZQKIvuE-v5HigKkXBver9e8NG-1XKNgoIHmk5eu001WKVufejIFzUJRS3qU16-HSr-BUkvLVq85besH3oRyCXtOcE6Bj6xRPni0o-RHwzJV_eTF2M2x0GZy8MG4GvgQgLcdYxQnh4wAz3j9ezUesU0KAN8_8ecZmimTt4NRuIyDmJJACB6sCv5ZUmeWgK8hEHOfc8Pz_wjePt8gdohhYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6713aa8d1d.mp4?token=Ia6voMxKUGSxcR4SVbh15uSRukjDzSGoEMc5uLgruoHW4q9U3Bn8SUJXdTZe9eUzhOJjRxAljDZuzNbCQaycYti-g6to4FLQn9m_EcrYta8_O9wHMJ0wK0rz8YsDurx1bxZQKIvuE-v5HigKkXBver9e8NG-1XKNgoIHmk5eu001WKVufejIFzUJRS3qU16-HSr-BUkvLVq85besH3oRyCXtOcE6Bj6xRPni0o-RHwzJV_eTF2M2x0GZy8MG4GvgQgLcdYxQnh4wAz3j9ezUesU0KAN8_8ecZmimTt4NRuIyDmJJACB6sCv5ZUmeWgK8hEHOfc8Pz_wjePt8gdohhYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
✔️
🏆
وقتی زبان فارسی در قلب لس‌آنجلس درخشید. نمایش شعار فیفا به زبان فارسی روی نمایشگر ورزشگاه سوفی و طنین صدای شیرین فارسی در این استادیوم باشکوه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/93659" target="_blank">📅 20:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93658">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxpwyNKP6_R7y04BeqWq5exMGRzxCRz98hSHhd9kDpZWhmyXY7xqcAD12J_6Vh3X80J93CY9K9HpgMeaNL0hNgy9X_N906DY4abpxwXEIPcGg42aEI-0V0P_q4qOr-SXonezg2v-FBiXKd5LPvB_-mP-phRqKysM08DjJQk5hHhRLBf4LGSA7APn0P3ZqAk_zGQ53C8v9rSXqVy2wb3EGIUgCy3oVQsXXdXqDzJS_rfJUXoUNPIvHiMK9b_SPRj1HGBMsWzIQJXPTgMC3ET7NoLMHKgeBWR2lmrXVf8trQdfiD-0HsYRPFTIIG4UokiVuzxu_5dNI0mpcd8DvogM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
جان اسنو از خوبای طرفدارا مراکش در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/93658" target="_blank">📅 19:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93657">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🇵🇹
#فووووری
؛ بن‌جیکوبز: روبرتو مارتینز سرمربی پرتغال پس از جام‌جهانی از سرمربیگری این کشور کنار خواهد رفت. مارتینز علاقه دارد که در پریمیرلیگ به فعالیت خود ادامه دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/93657" target="_blank">📅 19:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93656">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDwz7j49Y4cQg-srlTBYMHfhXHSB1ncVDhNFv2Oe97cD9dW4-haoWFBdYvFMTk95qd75XB2E7WmqkhQcLBoPwuVV9s4sWQnNUmn4cCMxZMr0hJbWxGgN2RD-tzcXog8Ilm_K5yZo-qVaigEHT6J0vRVvxI47KuRtmNDJgF4ENjDWyby81bYc8n_aOHpIA7Xe9DcFdXJ-Z7uru3qZQ75SHQzFGBmG_bBl7XZrs-2NXRwRz96-K_2xkltzMtptPhruffqvfkI3dnvk9L48QoM-Zz-T_4Xn_NALSLpjXRhBPrfPKwURV81fTLmDxp5VocOHHCSaFJ8Hd1jWJZ5sZ5oCRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#رسمی
؛ آموریم سرمربی تیم‌میلان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/93656" target="_blank">📅 19:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93655">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3c97c7e4.mp4?token=FWWx2mAV5Bm99Quh5jchiJkLp6obGfXmhMOsPsoxsiHfkLRf4OOwVaNjvWvI-XvL6VqGz7Y3zT88LKT9YnTtP1XJj-11v9lsjEab3BaPsBkD3TreXGnlDTJdvX-y48KLzDi6ShQhjnrL4rdMRIhw0IUeb-b4vv_xVeM_3zkHgssjn3sVdXNqzaFaknpkL9xJLqmH3ETNOIg-xBCa-XupJeNpkAEval06HywdkyF3UY3Ow0Fjxaa_wcQUGFpjPoWSe0nvy091Q4QJpjNJNPXERZaeNOE3pm7zPmvXMsUD4QAHdfvm0kDxSeQeERyHi2kQZ6yoCQZghF3dO8jm4Zg_zIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3c97c7e4.mp4?token=FWWx2mAV5Bm99Quh5jchiJkLp6obGfXmhMOsPsoxsiHfkLRf4OOwVaNjvWvI-XvL6VqGz7Y3zT88LKT9YnTtP1XJj-11v9lsjEab3BaPsBkD3TreXGnlDTJdvX-y48KLzDi6ShQhjnrL4rdMRIhw0IUeb-b4vv_xVeM_3zkHgssjn3sVdXNqzaFaknpkL9xJLqmH3ETNOIg-xBCa-XupJeNpkAEval06HywdkyF3UY3Ow0Fjxaa_wcQUGFpjPoWSe0nvy091Q4QJpjNJNPXERZaeNOE3pm7zPmvXMsUD4QAHdfvm0kDxSeQeERyHi2kQZ6yoCQZghF3dO8jm4Zg_zIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
همچنان از درگیری آرژانتین و الجزایر که یه وضعیت فوق‌کیری رو وسط آمریکا ساختن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/93655" target="_blank">📅 19:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93654">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkipDYYlU19Rd5gD5K5Rd6pC1V7ILmc0xIjsB1XbL_dsxAOt_dLHdK3X6_0er-1K6vZHQv7HIeFKopNP85TlflRBkrS_Sv_SnKTHYgLgrmH6pnSPdtbKmlXYZGS1AjLBm0smuAoYyFQAmgBvVDwQGUJjyLVNO72nuSOpVtHHi8i1rHxv813rfCsgX5DLL-4R1m95n_c3q5h43iwuxb5tzbaPrPAqRLUs7bDdi4wK58LL9zv3EmtlJZoAONXzfHhWyZew6nUxPmntlkRMIN5r50QC4lEQwjNV_zR_uq6arjXjhGGqtyeVaSdsovlPMXBrFhYXoZ8UkhemQsGSDb0UWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شات جدید از درگیری بین الجزایری ها و آرژانتینی ها در میدان تایمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/93654" target="_blank">📅 19:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93653">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🔵
گلوبو برزیل: الهلال قصد جذب رافینیا رو داره و میخواد شانسشو برای جذب این بازیکن امتحان کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/93653" target="_blank">📅 19:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93652">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91abdfa63.mp4?token=M24oqolXUXqybr5H6DbXgQ_eUvBjy2LBAz8QpOsTODsd8QhUSBk4NENvNKqV_lRpufseJKTX-8zqGWM2W2CG4eDdhRGBj_4SxjiK1MsaHZz4RCEOS807ab9zp7_96GbCeBfwjQE2OQi6iAEUVofYrVoCjKZ2Q3cd9rIdcXXIGVmKeX11hwDLGpLwO0w2rOyZ7leEtdQ3FDlJloF7zsqtphWw1Y-esE32ccHMM4Zjezme-307k1EHu-fd9P9iTgNutso0jQ0srJEjg9WA7AgYjJwx59qQ1BbDZrJuyCGuhx79Heu8c9KsafoMviPJdIshKKsfcdqcJ25wfDGAaNTgYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91abdfa63.mp4?token=M24oqolXUXqybr5H6DbXgQ_eUvBjy2LBAz8QpOsTODsd8QhUSBk4NENvNKqV_lRpufseJKTX-8zqGWM2W2CG4eDdhRGBj_4SxjiK1MsaHZz4RCEOS807ab9zp7_96GbCeBfwjQE2OQi6iAEUVofYrVoCjKZ2Q3cd9rIdcXXIGVmKeX11hwDLGpLwO0w2rOyZ7leEtdQ3FDlJloF7zsqtphWw1Y-esE32ccHMM4Zjezme-307k1EHu-fd9P9iTgNutso0jQ0srJEjg9WA7AgYjJwx59qQ1BbDZrJuyCGuhx79Heu8c9KsafoMviPJdIshKKsfcdqcJ25wfDGAaNTgYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
🇦🇷
🇩🇿
درگیری شدید هواداران الجزایر و آرژانتین در آستانه بازی بامداد فردا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/93652" target="_blank">📅 19:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93651">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7_X6FMapp24TFozvEih0PU7HFGthwu6bH4B8FhSQy0R3LPQEdg8njJ3H7i5_FVYQ_BNs6WyKPAwOCa8FnOjvZlLGutHJZr2oVrOYmBS5N1lP49flnYeIRNiDVq2ArYaNhIF3IRr-1ESNEmULo4350vMWL6cLE_cpP628oC3_ycdoz6aGJZWNn_uFrka37k6pOslNU2Un7Lx-4j2dgWLEPP2vD8aMRVAbz4pvEi9cJLx2_3Syt7hjSjF3_EZxqrVoONG-GfPFhQ7QLVA3IoWybdEeEJ3OnDb7HUd_Z4kQQC1oZwDwjLy2eH6xn2f31sKELI84mn30OBLPVoJzf3IBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🏆
۳ بازیکن از فهرست فرانسه دارای اصالت کامل فرانسوی (پدر + مادر) از مجموع ۲۶ بازیکن فهرست هستند:
—
آدرین رابیو
🇫🇷
🇫🇷
— رابین ریسر
🇫🇷
🇫🇷
— لوکاس دینیه
🇫🇷
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/93651" target="_blank">📅 19:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93650">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/93650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/93650" target="_blank">📅 19:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93649">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnvvCdW9LBIRMjJINYnFsd5P0LEUyBn9wuAh0qJqeCdUuYTQzrkG8j6bVws9rP-kfyYE15R2eSVZjryU9SV_d_mTOO_lq4YfS3Vr8XbAO4Tai_iU7HFRlH9gvXEaAVr-_fj_c3_lZFlP1Urx8iAJAUE6ojwvAjHk06d4rZxJM39zORagkrqb3ibbgWpB9t7XkeaDmB3sgU_aZm62LSHEG2pTQG0gPdRqgKXy8kaZHEGsn5ysS7w0sDFdOGPCH5JxpTlZnz0zVOuHzzETv13ThTqVyufFZhmQTUUwWdsUl19N3pUDWwGXh2L-f18yYT9PbGvQmT-1js1LXnezPCnq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/93649" target="_blank">📅 19:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93647">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90ce77b46a.mp4?token=Fwh_U79QUzgQMM2Aae1Gq44iP3gwJr01M_QkcBl3bUjqESu5wwUgGN951iUdAqJ-rk0sFIL6IKdtA6qxZrhTPRJ3AMlQh1GDL9dgULGoGEBXEBenkS7YkwdfkVfU60dulSO-wY8d41au1Vl64nyzwOIEtNZZv-GnzaUvIulLt4laWGgPbRQJieXaklZyqvbptxTadjv1cout_krd_KP0779fyQBvJQisRRmHMajXfC9kPdV_1iLrfwOPUtIkVMMKcgXD2tUzWtYA8tM1Jxo8h4p32uXDbM5sQ3Vg3roKVZ1sx6r6_dL8xU2UEIfIAtwdoUlzfvvo41Hq4YcRKzoL6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90ce77b46a.mp4?token=Fwh_U79QUzgQMM2Aae1Gq44iP3gwJr01M_QkcBl3bUjqESu5wwUgGN951iUdAqJ-rk0sFIL6IKdtA6qxZrhTPRJ3AMlQh1GDL9dgULGoGEBXEBenkS7YkwdfkVfU60dulSO-wY8d41au1Vl64nyzwOIEtNZZv-GnzaUvIulLt4laWGgPbRQJieXaklZyqvbptxTadjv1cout_krd_KP0779fyQBvJQisRRmHMajXfC9kPdV_1iLrfwOPUtIkVMMKcgXD2tUzWtYA8tM1Jxo8h4p32uXDbM5sQ3Vg3roKVZ1sx6r6_dL8xU2UEIfIAtwdoUlzfvvo41Hq4YcRKzoL6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
خارجیا بعد بازی دیشب رو رامین کراش زدن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/93647" target="_blank">📅 19:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93646">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaaE_cJ2C0JSxyGbwPEdz_-novXp1pWwdzAGUv42Uu-s3SNih5C_IXGy5vcA-oCboo3jOGjYcaXCP9j_nBv_bvW5MWaV1UzIwVPq_FwZHcGLzXe5Z4x1TWeFvOTvmlz1DDButD3yG_Ers2xzo8haLuKXPyhvEIKV6CE7ue9eXDpZzb1MJOaVvZMrGNOcHFnVLQGC7V-Uj1Cig3eKAAC-vcyUfli_pac1Mp1c413Zcfg4bhNT2iZFoUAreVWvY0Wn8sgLlUb3QmSdAkj_s89hCWbSsTZ56zliYdaxmDDFL9vrLLSrA6T9hmIbYvvUu3US2CLiUzTCXublDpFNPEpUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇾
اروگوئه هم تیم خیلی خوب و بزرگیه.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/93646" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93645">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHAyhh-9o_fNOJVzOT_Q2n8tREBcdab96x6TtUxhpcWxf9C0xgAg96n_ERsYhcwklSziSQlJYb0LCGQao2s--EQ3hJQkfXKPj0LG_RUMGcFhZSwA7kf1SQpqjQVUDeTUcQr_exz0jzjByb9Xg2jPz2Ix2cP1F8C_wW4TApaoLxN30Emluugn8bpycBMVXGoHgqBNC2L4t018Kv5PxAGklH0GmEo8nH6RdIUCSyxQ343r-xzqAqdAuu4O6PuYZotoMuVlMVGAQOkXexc8t71mSI6CpCdjhXBkcC9BCTZJTk8BeBupon452rk4awL_qO9MsEEWOpzCMhvYyviicJ4jRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
🇨🇻
کامنت جی‌جی بوفون خطاب به گلر کیپ‌ورد: به تو افتخار میکنم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/93645" target="_blank">📅 18:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93644">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYd1xBJqsdspaTfYWInjdYQgYYiEmK_oEZghakLFsDi7MHFVXngWllnUu5ks1QRJY9FcOD03sUiyiN2LnwfCHXU6tgkbdaWzRypqtRlULQzxSK6r0tsuPvSezwrNJ6EhWgPqOXy4W7sCRWuKwAECmXsefN8bXIj3Kv9t4Npuc9KN-38KLUjWq4eTktQXFwt72LeCmon3pWO9fOk0CmV5YgWy-ZdAz1Go_c6ct4L9csmvTbWBilx4oNJKZ3oC8vWzKQEEuDFgtwT58Nj-S4gxrH28Q7U41KPEQisTeCqp9gp-SQnbHiJ8wdzoL6thK3sBFNfQDTk22T19sHSo3LZk1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تعداد تماشاگران جام جهانی ۲۰۲۶ از مرز یک میلیون نفر گذشت؛ اونم در حالی که هنوز هفته اول مسابقات تموم نشده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/93644" target="_blank">📅 18:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93643">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bbeb3adf9.mp4?token=LQvujjMXizCnZ0_-zPxKA0grhp_nnXlz7Y_Nxckhsw8m6uRSvh-d2_-Odqp3M_yDR-4V0QVZ9WRRceNhObti7Mt5k7W5lZ3ICXiv5zBRw6CfbpSybCxOXwHQhPUZITDDiUpjFAX6klgblauy9NprW5M1yCbVzDffnA8Bp-bVpucQW4dMgS0YaiaqL4M5E22lEAXstbJ2UmC_sYJuP2RgPtHM1ZcWcsAplQBIHySQOYyU3M2AijVZk0ck_Hdw_H4lKDnsXAutYMi1K5LrxLMadqpHFy6EtSdXUPGwVUFBWmSZiliQuBEy4Ldut4GZU1bo6DrtruY0OO3NXFNn3AmrEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bbeb3adf9.mp4?token=LQvujjMXizCnZ0_-zPxKA0grhp_nnXlz7Y_Nxckhsw8m6uRSvh-d2_-Odqp3M_yDR-4V0QVZ9WRRceNhObti7Mt5k7W5lZ3ICXiv5zBRw6CfbpSybCxOXwHQhPUZITDDiUpjFAX6klgblauy9NprW5M1yCbVzDffnA8Bp-bVpucQW4dMgS0YaiaqL4M5E22lEAXstbJ2UmC_sYJuP2RgPtHM1ZcWcsAplQBIHySQOYyU3M2AijVZk0ck_Hdw_H4lKDnsXAutYMi1K5LrxLMadqpHFy6EtSdXUPGwVUFBWmSZiliQuBEy4Ldut4GZU1bo6DrtruY0OO3NXFNn3AmrEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خانم سوسن پرور شما حرکات تکنیکی انجام ندی هم تو قلب ما جا داری خواهر
🫡
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/93643" target="_blank">📅 18:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93642">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCbYLgjHuQMkbJbZswbOLsjLygmuixlIYa_whbyA_YeTj_ljRoqopuBp7NSHq-HZ5eiCw3DmXQIky56m8h6QSvPYv7HAC2pHIyIJuEbNxWzyIUPAq3XiLP6GgYkYcY1T_2RHXy-tn-JPqXCUw80qM7OiNPuFDM8Udud3km9GTHQJxTmNV_TjdPx1LH9YEfrRxWeSxebj0_l4K9xQQAlDgy5M-Ut6tSZm0s0HFoOhcm7xiIMGCxOZLQxGxZ72MRiWjdjGNMpsa-hTwBlDphemr7vqo-Rs6h_Iq59wk48R1aAnUwcE4OdjqYHCHE7SxV_f-mL0FtrmBkB6CPgTtTiHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیرمرد ۹۷ ساله اهل آذربایجان خودمون که تو‌ تمام دوره‌های جام‌جهانی در قید حیات بوده
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/93642" target="_blank">📅 18:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93641">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb793D2QtOpAs2Z9hg8fqR3PYLQIb4DMr_NENsNnGZf2VwxNL-Vgjc2GFyL10rFhti-XEEEtBdJRMsVrSIH6ffweAD_E2MQf-WoSxjvztDBU0rQDTpu6RGMM-CCinrIEEjpGUVPxn99sI6ElcWPTZ_SLFTGPwK3hwG2fVG8KBRZOtCE1rSKkAp761N-ekLjRjop2C7-I4oSGg0MtobYzYu8OVHnVBPFBg8DKOOYR_rgcV6vAJ-ppdXr9-UnGqFAQoFNKEpzdPehTfkgfqxJrVkHlkQQVfdw0jFx1ZkoFuhm4OxX3TRLswPCTLBh1ubWPeBmGmWQ-KPV3xCiAbP1S7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇭🇷
جوردن‌هندرسون پیش از بازی با کرواسی: قصد کسشر گفتن ندارم اما لوکا مودریچ بهترین هافبکی بود که در طول تاریخ فوتبالم مقابلش بازی کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93641" target="_blank">📅 18:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93640">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4lChbatuocfytCuNu_LEGhEeHEGmCHu87KyRLuNZ67Fs-IZzId0M-OxfdYQsgtq6mf1NadI9bZimWb2iKlpFvH5MoCMCJcqhyTYPT-qt0-GbfsFsAAYsKVWv5hHmqp7OoAMOGsktUVLZ-UzWIBXElD6a78nXVo3u78kTM2y0P1vTXeI6jwLhOFfc6UfkuVM4Pkyj87bS-kRsIsSDqhAG77tiyWaCm0xlp8J-LsXbZDSBdgbksj1UMqgRDHFouUhD9XKYmsj8YL3Nzm49d_XdJv1bGaiCHaWU3Lw1XTBqH0Y62PYgF3abmlbDiUx_-tWTwP8SkfUWcLxBikv9BEYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی رو پیش‌بینی کن و جایزه ببر
🏆
با ربات تلگرامی «نتیجه‌باز» می‌تونین بازی‌های جام جهانی رو پیش‌بینی کنین و جوایز نقدی برنده شین.
😎
۶۰میلیون تومان جایزه برای نفرات برتر
⚽️
تازه امکان دعوت دوستاتون رو هم دارین و به کسی که بیشترین دعوت رو داشته باشه هم یه جایزه ۱۰میلیون تومنی تعلق میگیره.
فرصت رو از دست ندین و همین حالا از طریق لینک زیر وارد ربات شین:
@NatijehBaz_bot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/93640" target="_blank">📅 18:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93639">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Av85s-pe3mUw2_3QES3cAwAlpIN8XRHUarJVzrdNhb5la8M9G6kJ-d0vk63pBBOtKisTDt5SdQmKKEpHQ_GIT5gQQKgUrmAih0S6hQVzAURVOQym2UeJXmJYNqrSUak_H7UfR2OQEokF7PYro9gIMWHEv-sU-fXc45lls1A3DM4ngKGtZHtWqnlY8LSRFJMMewSsv83ran8Mzsx2ly58cHM6bFAr28HbFzPZA72DJ8QutrmG49CKag5rpzdDllwl_RYSJGVy5mcikWwWOKhIPYwpqafgsHRFjRXKi_nNpe34r_B-6MlK3Q-2XOls3vmGzibr-ZmuuJcF5qav1d5yTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
۴ خرید رئال‌مادرید
⬅️
هفتاد میلیون یورو
🇪🇸
تک خرید بارسلونا
⬅️
هشتاد میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/93639" target="_blank">📅 18:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93638">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeaYV47C6JPghSOV12mZB_RLFif-wKxCEbE_R3QTWhVQKT34jPQA_NDKAj-K8m79VZ7YrotYx2rLxQEuCLp2nA7q9B9Ecc5TodOxUTFPyfi__9Jqh25jJf4-kGsW7wsvEnH7htUJk6QE_Hbii3lkq94FqT0sl1RNc-6ZoeybDIVq07ygjAVyOr3YHwWNFSVKlKZkikDQnQYQRuNu6j3NdSWHIgSvRfqeNEZE66MbMdkSQuKKkuWPRJ2yGAP2QRxPyxFuLhtlzRPa1eMvaH6Cu15prKhrc2iU1MMWoHAIfi9Ggx2N5VYyVexjF84LT6_Geez_z_aFpK5YxalfSkWqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#
فووووووری
؛ ژوزه‌مورینیو درخواست امضای قرارداد با روبن‌دیاز ستاره منچسترسیتی را به فلورنتینو پرز ارائه داده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/93638" target="_blank">📅 17:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93637">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh4n6yiEl_Ds-n-lBQrr4aig1jmDCWBhvFpP_OymhXTCsFnXjIVlCoHK_9fGpJSceNi4AEu4X274dgrBrkcw-lVtT9KaFHB335cPmmvUJct7YInmp1e5Gf6BNm6uE3lh8dtMdRdiEIO1VuL0N7G49HmgtXkaNkP4UHrsxRsOJBKAfU7Ojad9Kc_3M0A4Z9Eplb9jS8vlLlCWSTggaMgfkPpE8MJKED7sxV5mbArzWA7pMORT1YGulFMYMpe2QNBW2BnbFYKweqaKnWpNfgBcvQcZOwp6TqTesv7hhIM_zM4Sv6MUpK9I-6oTEZ6f8oDITtF9SmV8JUOQ-eC9kDPOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🎂
امروز تولد یکی از دوست داشتنی ترین مربی هاییه که دیدیم. تولدت مبارک کلوپ دوست داشتنی
❤️
🏆
آمار و عناوین یورگن کلوپ در دوران مربیگری‌:
⚽️
• [۱۰۷۸] بازی
✅
• [۵۹۶] پیروزی
❌
• [۲۴۴] شکست
🤝
• [۲۳۸] تساوی
[
🏆
]
لیگ برتر انگلیس ×۱
[
🏆
] لیگ قهرمانان اروپا ×۱
[
🏆
] جام باشگاه‌های جهان ×۱
[
🏆
] جام اتحادیه فوتبال انگلستان ×۱
[
🏴
] جام کارابائو ×۲
[
🏆
] سوپر جام اروپا ×۱
[
🏴
] سپر خیریه ×۱
[
🏆
] بوندس‌لیگا ×۲
[
🏆
] جام حذفی آلمان ×۱
[
🏆
] سوپر جام آلمان ×۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/93637" target="_blank">📅 17:53 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
