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
<img src="https://cdn5.telesco.pe/file/fKriYYvzTOiAeuufOsxubZX_fSB5eZK6sDHlveIFM3P0s3lutitTCmQbMztfOeGuuY8NM9VLh834NtwtuEaTCpofk_3CiMoG2MCQLDBdtoZ9anvYiZoAGueW9bhfia6EUZYZkqWrhT1pyrJiLe_LNK7OPUpdEM8teBgmz3BdSPI4QfjIQTuQMwPkXUoyJJ2_xTI31cmCErv1-lJ2uDX39YyhiYjb3gVbHYim-ZLMQsctTiekOJZAMlwV4X8IwwT3VO5PrYKmMvzkTfLpYvfyETOKNjtBenZsQctk6XUF0s_SeqQS4rz9S4537G58MF8_-apzpI2dqMUHNul-THt2tQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 719K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-95261">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHNETGaz-zn_48Y-qX3A0nw4bk9C8f-qZFBNJcmdXZGMttWlB6SCBeIXt956rCWY0KetRRqmWHgvPyjxDR-x9_ZI4LdbyO7Vu7ts-jgemIzuImtPmSKgCjuO7lRMQaZ1Rxsb1GE4tn_GFjT_VcsTmOVD_aI8T2k6f3ocQXP56SqlZkHMZpZBZ_g3Cy_NBPbXGanlFrZC3rXd1GPLeL7nHglpVoJaX2S8wN67CGH2A7bPxmMBfXhHpoqjVT-Cgj5HRQ-7eIcXFiBI9HpAMjRtwMA3a2F52XYO2VoNlNOZZsMLdEdbkjktRTRGBoidPZ9JizKfUW8lRyJBmIA8k029UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
بهترین گلزن تاریخ جام‌جهانی رو مشاهده میکنید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/Futball180TV/95261" target="_blank">📅 21:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95260">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇦🇹
🇦🇷
پایان نیمه اول با برتری تک گله آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/Futball180TV/95260" target="_blank">📅 21:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95259">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrocaon0cfSFPDYcP3lctbLeyfke-TIvreOqFruC8w1sz7pR2GksWGh1x0YQaNa8EgOliYNVwQAzToPag9KsDXqaZeiEV3oiPUfGyZyofNzpHBzRoi7bhzR89BbR8-onW97xQMu6MH9hSlk1NAav6w2WKkjC4VZkbtWhxej9muKWdhnb7HvAG2Mphf32IydMGaRT_ri1MnedX85TF3lHw7Z7XdMIP57txqW9aZULIy_wbMTRAxbjF0-iAEeD_zhqyij7qwOEqvnmiIdp_QYcPdcx1a5k7xROwAAwvL-lQQ1vHm0uSI0dRZDGcUPdcqWMvGNX76-t-neTdMNngwXrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
بهترین گلزن تاریخ جام‌جهانی رو مشاهده میکنید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/95259" target="_blank">📅 21:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95258">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇦🇷
گل اول آرژانتین به اتریش توسط مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/Futball180TV/95258" target="_blank">📅 21:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95257">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رونالدو فنا یه ذره خوشحال بودن سر پنالتی ای که مسی خراب کرد که باز ضایع شدن</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/Futball180TV/95257" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رکورد کلووووزه هم زده شد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/Futball180TV/95256" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95255">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شبش هم نباشه گلو میزنه
🔥
🔥</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/Futball180TV/95255" target="_blank">📅 21:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95253">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گلللللل آرژانتین مسییییی</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/Futball180TV/95253" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95252">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsNE94wRXbfjcXsO-qZozkpV-AsJVSfFp63fui9tAR3JRzjPLhF6XalVUZrhm6MSzDUJnIuZBeMvSScrsEUWA-P3bnk3Nx44gfJ2uXlmAQLLkbdye5Iktl-O8yO-zzUjRXRctVOt2hTAWsHQyIUwQVD0MzjXejr7O_k0Atd4uvoYzDCNS6IVRHlXpn3k-F4CTva5cfBJyeu4OYVYcOjZcw4kgS4mcoV_2N1f0twNPlrhW_i1l3AL5N8P7lqHAMGAMUG8dPmgq9f7BGGqAkx7Tvo-9hLZdPRgtHIXf_zYcGIb5o6Mrr3Dyy6RrK9OpHObUV3eAdzogapU1XDbcbW9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی با ۳ پنالتی خراب شده رکورددار خراب کردن پنالتی تو جام جهانی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/Futball180TV/95252" target="_blank">📅 21:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95251">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
لیونل مسی اولین بازیکنی است که در جام جهانی 2026 یک ضربه پنالتی را از دست داده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95251" target="_blank">📅 20:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95250">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اتریش داره فشار میاره</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95250" target="_blank">📅 20:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95249">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مسی داداش چیکار داری میکنی امشب</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95249" target="_blank">📅 20:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95248">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5cd500ea6.mp4?token=UxCdzJrt6mjuRf_qhgvTtrIKQza4ANuHN1oHW7fOMETOarlFM8N-_Ku168rC9yKi29yYpjas9rtfAGkYaDnrL_hLCiOkHFOM0BM-Vd8_u3zTSupp6DNFrjN7zLMK839p7gJEG4ncjaLIxYv0wsYAMtbxSiOwlqlzpiQkvWsjEU2o8sJj37Js_GUTdiXXjgWCnhmXiXmpikFh7v21dfweS8vpdp8DmGcbq6OrV2cRjHpqVui4-F4B5sJcnnbOvftbHb83sxpo5sSoYMU--PtYlegqupWmt1Bbh5Ee_rmsY1wQiFPtvFeMBrYWEhPIkK7C5yyevlP1na9IK_Zn07YBgXu9UfJyMTuvEqs4p2Tn7KwQ93NqnZ_AV4617kB3YSA6MWSLuatRqxeGDbjLdqm5jyt_8JhwMDxrG-5MyQ-UhW7SWmv5beBkuq43jkfJ-epzEjOcdXWLsj0heDnOslMWlv5g2AJblWjQ-zyVRfHivwtT0OeFCiWoRt1x31Gb7TVerPOKlbNz03eVNdqHrz5lXhJv57j49ZMaQCNYveHVzXRsCUgwTDiDsrxpmxSHkxEg9cHXPwOIC4mrNmM0tTQz1mdtnyQUv_NWB43gEWgsqhopTrd16uBIeOLqnyQ5u358rU3ibPSFxCsvhCYlx7k_MjG9K1j5FE_SXQSTHVMF34o" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5cd500ea6.mp4?token=UxCdzJrt6mjuRf_qhgvTtrIKQza4ANuHN1oHW7fOMETOarlFM8N-_Ku168rC9yKi29yYpjas9rtfAGkYaDnrL_hLCiOkHFOM0BM-Vd8_u3zTSupp6DNFrjN7zLMK839p7gJEG4ncjaLIxYv0wsYAMtbxSiOwlqlzpiQkvWsjEU2o8sJj37Js_GUTdiXXjgWCnhmXiXmpikFh7v21dfweS8vpdp8DmGcbq6OrV2cRjHpqVui4-F4B5sJcnnbOvftbHb83sxpo5sSoYMU--PtYlegqupWmt1Bbh5Ee_rmsY1wQiFPtvFeMBrYWEhPIkK7C5yyevlP1na9IK_Zn07YBgXu9UfJyMTuvEqs4p2Tn7KwQ93NqnZ_AV4617kB3YSA6MWSLuatRqxeGDbjLdqm5jyt_8JhwMDxrG-5MyQ-UhW7SWmv5beBkuq43jkfJ-epzEjOcdXWLsj0heDnOslMWlv5g2AJblWjQ-zyVRfHivwtT0OeFCiWoRt1x31Gb7TVerPOKlbNz03eVNdqHrz5lXhJv57j49ZMaQCNYveHVzXRsCUgwTDiDsrxpmxSHkxEg9cHXPwOIC4mrNmM0tTQz1mdtnyQUv_NWB43gEWgsqhopTrd16uBIeOLqnyQ5u358rU3ibPSFxCsvhCYlx7k_MjG9K1j5FE_SXQSTHVMF34o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
صحنه ریدمان لیونل‌مسی مقابل اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/95248" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95247">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این چی بود مرد حسابی</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/95247" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95246">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مسییییی ریددددددددددد</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/95246" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خراب کرددددددد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/95244" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پنالتی برای آرژانتین اعلام شد</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/95241" target="_blank">📅 20:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95240">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">داور رفت وار</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/95240" target="_blank">📅 20:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95239">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صحنه مشکوک به پنالتی روی مارتینز</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95239" target="_blank">📅 20:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95237">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">برریمممم سراغ بازی آرژانتین و اتریش</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/95237" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95234">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFnmDdA3XwO0i8TZhJpYhnXl2bgJiZsTLKG1UptM1-dnPYQemLGLHT3N3QNIhbZccvXCYUj88fTwp6kRvAwS4mWw-2wX05G0PCYrUW1o4Z8OPTJPmgsZVBjCvYBl0N0F6o-P3Zi9i4RFOcVsugjAeqRwXRwJRbkkvo_Urfsjhal1mO7Bk5OKhEzhr1w9A08YzlnRzejqeRGp9KVzut8XF3HAI81gPismUT-yTKXlPG66wEJk37-t8pXHTyDn_uPfDnR8TfzWVYVdtxo4gF9zUIH3FsGuyoCS7Iw1NogXSo36mM1liERQlbp9mW2JNRpVPVM1gHf6KtT5TD735CpflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6paFvOdk72n6nf5iwNir0HFyrZoNiXNwpj5RdaVwHFAcRKCNnO82qtt6ENIICCE9p3qPK5ccYvOLCaTAg-wbJAv25E0W4Panh2Ef0VVdrY88flm39Th_jr982V8VAxHqfje8gyWKfmyvc75qIsSI-eAv8pgLkNMBMQrH5xRsYbX4GfFmS10v81aczpuE-GnPIp9jZUXdCcl3be-3V1CaKinDGuqnazIblyobM92FKuSV7fSB1LouZqPOEDexnBOTYVWKViO1KR3t2_TNkrTZO_BjxoRnTAF4q0vTbSkyCFkq5iTeqcweH5DpjaG8ncNQBtZrXRJlFxPOrbPxBBzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JghO7Nojj3wAUpSkd-4w0vG99yCbonySDuO_2I5fa8dS7sqfw44W92WDJxnqu0bqAFn3b6FAQDn-bA0-MHYxIPR2qSZD4ULg7cOnes4d_tlh25sTwstpTanfYCuF5K0UuRfKpblYWlNnYsJrSjkI5REYuUTFU9hVxSjIHUF_Lar3JD2M_mylnGk9m5CopwoPpFJ1CZ8cDNRYdkL5MsNlKGvkY_10om6KK9oMO5WLD0asidf5Cew2Y_IfgYtHjG2rZaohNgH3r-2uXkuOkb5qrm4J4krrQ_JGhLXVqWZWkjBGjDkkdep8pbl_urdNyJAB06gBssXwIDLjdiq-FZcxrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇦🇷
🇦🇹
استادیوم خوشگل شهر دالاس محل برگزاری دیدار آرژانتین و اتریش
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/95234" target="_blank">📅 20:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95233">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5k9AByUT9DtT88kPfflFODWzpsvhAWbzzpcP910Rqsetgw47kZhMlfrDJLzmJfYTG0laejZoNuc8UnikNasM8HzQ7Hd9pxLWsb8bzVPDTiYioIAFH1Ph_wahtVgQfck40NbMsbg_mm3gAsQ0zRya44udQP6OI6AS28CtmgnFCzA0kyZEpDKTvwmlk-scynP648FQTa8THJYpRveXbRRfzO6BB4wpTQ1xQqx8q-u5tXvG5UlOy4P70RkFErmD3vcJS48zMsyxWkkEMEshQYapJlwY8JkZanmt69LgXmRkMto4JZ5FirPbf8Ua4KOzamIYSM8A1c4vXzniPuBppSYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دقیقا تفاوت رفتار بازیکنای آرژانتین و پرتغاله.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/95233" target="_blank">📅 20:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95232">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/95232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/95232" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95231">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1o9YC08PsavFJEpljRleMdidkPj-P-D4HUSDXTu83oMVoSnXHKS21ZmGGAv_zGHSmBq8Kg5bIIff12yQBRsXikQA_WTmv9JHtosMHEsY_i07P7T9Y5yvOgkrS8D4myCfwor_s1dZoSaEJfIODSls_Zp8Gd5-GLqAnm9ASshHvrjCFeAmZyCBAsLd7tSNTd406LHdVuKyZUeK-SUvQMYdNbAjMugpPxTp_G5TkBzxDJZ6jS6LouYnoVVXVOIInnHIGxaMmWVKhnN9Z8bvppuRUTuKGhfx-pKh7kMLC8UwzTTcsRegMznBSHiTaUVahsJFUwq8ep2BYC578T_NlmttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
پرومو بزرگ والیبال Ace Arena با جوایز تا 5000€
🔥
🎁
جوایز اصلی هر مرحله:
📱
آیفون 17 پرومکس
🎮
PS5 و Xbox Series S
💻
مک‌بوک پرو M5
⌚️
اپل واچ سری 11
🎧
ایرپاد پرو و هدفون سونی
🎟
کد تخفیف تا 50€
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
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/Futball180TV/95231" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95230">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joe3Uc4wrVU21CLQEmMU0aA4hazmTyqzjpJkgI2_bFOFIrlP7R4Q68u1Euufrlp1Lx1aYtyh7IkAJZ2Mu275s7ToddRkZkm_G8SBdMFw0IjdflOzuIO7Mx78CLOdS_msYXVnTE8oVdSrpKzbF5YE7yaOyk8PneVt_0Qo5-6qsCqw2Vub_jQlCrkn1Wt56fvW_4IOYfP7DTabo35X73D4-LsxYf6PoVOijrri-7Bh-hH4yp-OUIqh-e9-5TlAHPlfSu0-PqFllhpAlJENCkjIS7m1gK-q8TE2Hsnev4nnD_lmm13Dap6IdQI9l2RGK3ksWVbty9WXN0xjB6MeVf_7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات گنگ از بازیکنای آرژانتین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95230" target="_blank">📅 19:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95229">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxTUCrCOe4kCLOuj8NVIfZJ8SwyDnvEv7whSwkPzqbC4Erm9Tx7q-A7v7rqxmcrLVRFaVClvqBJKpPYzxu-MUFB9Y30-r2-Ua8qSmFQIcBul4izg-D0GMwi67ncX2rFAn_IHlOw4xw8KXbjCTVWRera4o_LtejUOY2lkbwztPvD_dHT_pdmebf7CTH1RYbdxGzDqNtYOTnxymnvLs_enZxMPKrvAyYrJ_BQZ0ApcgmlqyrtK1-5QyEkuwlGQq4KhUvh0hfbz5vhGoCsruC2lUCOYK7DGd0uw-jGnj3QMXeDGTkqzi-lCNhvagZDM4I7CQie2CVH8EFQ-YrPf8TvX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ:
قهرمانی دوباره لیونل مسی در جام جهانی چیزی به جایگاهش اضافه نمیکنه، چون اون همین حالا هم بهترینه. فقط یک جام دیگه به ویترین افتخاراتش اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/95229" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95228">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR_j87sp2K7UApjTXOLo8x0F0QB-L-aatbDvdxiNi-32YssXYR068cWACq4l2jRBM30tImmTm2DcUTxejvkMYu2MmSbgBX0XYK9idYu-ix6yj5rn_Sw2L8nnmakZejh1O_V-lIYcMjJnz2uBsqjf9uZaN7M7_F-tMv0O5tn237RpIyfM8AJd7Qf8q4dH2ock-A4KeXMUoQT09_oaGvs8tzfa85yGs-RWvUspvHenI6mSKl8VKP660694B3LGnGokBpwi1yOcyg2hZSJ8RWnCldsOcq4CMKzcZvkIQlAEno21zFS2lgCyKYIM7M3LUh1_ei2B1r3-z_m0ZbomZufoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروازه بان اتریش با 2 متر و 5 سانتی متر قد بلند قد ترین بازیکن جام جهانیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/95228" target="_blank">📅 19:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95226">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV6EieWia7FON7AWLna6vgdsDn1-hpo6xOWEn0-hX4NsXQVA6taR0oK0xtpxPD21LBZMThOyErZd-9Rf8c8CZVeQlyc87lycBnWynDlnNskPGH2vjBfclk1-ZtLQbvzgrv8ubR-9gW0yn3dj40NkFnFiH0pB3i6j7tpPt2CP8QXuyX2WMTgqKk5xa4qU2Yn6n1N2ubKLn5cf3eQRP9mNF8wbgY8mV5MhsIn9PDieuoTpp3iYvfWB53OGGXSVMiCHXqVSIp1l8cWObBGBOYXZJJ9EUW1jUo5DaFFVquxkk2-2Z6xD7C-LUI6ZM7cimg6ChMrHgZtbIo_dr9SFkkNsxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو به ورزشگاه رسید.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/95226" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95225">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiAzA42XxBGZPgc1kOYHN7hr0DogMkbM4SZBiGdIlG-QvKK81u8F7dgFnt01J2cP0n5DL2Mw3LV9oDr6ChzDy8wjbI9g43urMWTmp_3tX8AwNXDO09jtYZlhO74WXfbkaojsBQeYQOq1jFknJRhpeVT-vxGY-Zn2QO_xpQQPU4d4PR1J_ErE1UA_QNxiYkqss9uaOzJKbS-P6Y3IkU5H6jRlIY4Bxx-PMe_2ZXtp8qTC-QyP941GMrtkcFDgiB9BCtumiKKlKEgZbiFHu6X1jaYMcIo0DR30Dywyk6nhht23DjEF9oiwY9mpmXIPN2Z2tso9icMvwMFqG4tPgAKoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار مسی در هفته دوم جام جهانی در تمامی حضورهایش:
- 5 بازی
- 3 گل
- 2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/95225" target="_blank">📅 19:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95224">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtJ7GrFoY9rnV7vru-H_v7TFM2Nd9B2WKY6IJwq2EWLDPVuZ59JFan-cbGH5IsJUsKvk9G6feCZ6cZSpEPrvjpLx1sGnOPEe1gdHJaoaC2j8kHK3YYcDb_h7JevYFHnCluTEx6O1EcUptbZaBePNRydPiQlQ6jCWI0j9IDtJaveNbGrSDkH37a8-MJDbvrXScv321pu2GK5cRo4E3wqNMMFi6VxyF54N0YZ_2UxbLuV318KOo9orSgz7iGZuUU9nCJbOBbu6meZL6vsIJijGCSZw6Ri68_8HIJ7N1RY79Pz9-3jbkV7GTAJxz1uyiJ_-7tuL-pglcWWPIn8PGHhpRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🆚
🇦🇹
🗓️
۱ تیر
⏰
۲۰:۳۰
آرژانتین
🆚
اتریش
📌
مدافع عنوان قهرمانی در مسیر صعود در برابر تیمی آماده و باانگیزه از اروپا؛
جایی که تجربه، ستاره‌ها و انگیزه برای تثبیت جایگاه صدرنشینی به هم می‌رسند.
⚽
🔥
آرژانتین، یاران مسی که پس از نمایش درخشان در دیدار قبلی و رهبری کاپیتان خود، حالا با اعتمادبه‌نفس بالا به دنبال کسب دومین پیروزی و هموار کردن مسیر صعود به مرحله بعد هستند در مقابل اتریش، تیمی منسجم که با پیروزی خوب در بازی نخست برابر اردن، روحیه‌ای بالا دارد و نمی‌خواهد تعیین تکلیف صعودش به هفته پایانی کشیده شود.
🚀
⚡️
آیا آرژانتین با اقتدار به مسیر قهرمانی ادامه می‌دهد؟
یا اتریش می‌تواند یکی از مدعیان بزرگ را به دردسر بیندازد؟
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/95224" target="_blank">📅 19:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95223">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3wOqyzsoNFg_V6jwTwi0p3zBqKhUWZtJ-LR7pXJZMuQPujTMDdYmCnWC9Y1w6I60o9uazpa_WGDlbkrMiyeuehK7eMVMHICwhuJaJMIAFJTlIIabCL7OjThFIIJXGvuRcDspIpA3woDou2vjBDcny5LwWVU_4YyF5YreBSDN_DpGJb-j_o0yiHtHqvwsPOknKsVS_L8DIv3MkqZGA9NqpKbVERD1B5lwnHHc6nQqOkxb8d_svkccud9rKbj6LXaTm5yGMcW0hvn14XewDf8S4pvdyoBs1gtKEu6puufnMXxh6T_cWZGQQYBHDDD3dTyuHe6zIJDf3tjd1egeEpjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
مقایسه برزیل و آرژانتین؟
🎙
روبرتو کارلوس:
آرژانتین الان از برزیل جلوتره. اونا یه مربی باتجربه دارن و لیونل مسی، اسطوره فوتبال جهان، رو در اختیار دارن؛ چیزی که ما بعد از رفتن بازیکنانی مثل رونالدو و پله از دست دادیم. مسی بخش مهمی از سبک بازی این تیمه و چون قهرمان فعلی جهان هستن، کمی از ما جلوترن. آرژانتین تیم منظم‌تریه و خوب میدونه چطور بازی کنه. ما هم داریم تلاش می‌کنیم فوتبال زیبایی که در نسل ما وجود داشت رو دوباره برگردونیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/95223" target="_blank">📅 19:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95222">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xli4Mz3uPV-zoIp4-wUdbHq1XE6wUprv3-pnGDPQyt18oHffxGmGP3tAAKaED1iT95GGs7fNdE6qTiUSNNl0GNVAyYanFkaU9yFGlxie01bKGQ9I-zIKPJLY2wwfyktwfH4bpRHDlrjbkFWJtGl_Fnhu_zMJR3D2LvKOGKNo8hvDKvgUGtoGIY5W-JfvbT5XwFYWjPimjIQQejOVxVcD98t34gEotu-XqGpMovpt75giMRkozDToZxx08NaHTJGlWdYKqCpgGs_AdCwokVP2tIzVomRonM0jmyaHQtBrLJUcqyBOfhIZl8F9DFlrRB-K-PI4XHtsClZa6C0FawFAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
کیت مسی تو رختکن آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/95222" target="_blank">📅 19:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95221">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dde8e1d74.mp4?token=qYpihb6PW944RttX-PQjsucAJIcg_ls96jQPwY2FPkm-EAMzqA6BmTdaKk9FWP2ibfh7TE7gb2PC1t8bpdj0MxGhtKCNKphzynQDoLwX_hsUd5WPpcp85UDIVvKnR7qGZDLqKZKFFUo6j1vwPQ_srbksDzVd_8TSeHvVL05-tmzcdcjz7XChG3UiYgowUeZpHrPczNr6gyegTOPNt0tfvByJFDlCQd5y8MhvrUwCYDoD-3IZ7SBvWfI7GY-8AFW5fi-7wiuafxQkbvHzmwRtzryWXBFxrpxXj0eYj_MldhYVBHTF4Riye4epVsX1-4NaLaG50GQJOqMvjb1hGtCaBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dde8e1d74.mp4?token=qYpihb6PW944RttX-PQjsucAJIcg_ls96jQPwY2FPkm-EAMzqA6BmTdaKk9FWP2ibfh7TE7gb2PC1t8bpdj0MxGhtKCNKphzynQDoLwX_hsUd5WPpcp85UDIVvKnR7qGZDLqKZKFFUo6j1vwPQ_srbksDzVd_8TSeHvVL05-tmzcdcjz7XChG3UiYgowUeZpHrPczNr6gyegTOPNt0tfvByJFDlCQd5y8MhvrUwCYDoD-3IZ7SBvWfI7GY-8AFW5fi-7wiuafxQkbvHzmwRtzryWXBFxrpxXj0eYj_MldhYVBHTF4Riye4epVsX1-4NaLaG50GQJOqMvjb1hGtCaBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که مسی تو زمین هتریک کرد و بهترین گلزن تاریخ جام جهانی شد، آنتولا اینجوری روی سکو ها متئو و تیاگو رو جدا میکرد دعوا نکنن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/95221" target="_blank">📅 19:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95220">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فوری/ کری خوانی عجیب امیرعلی اکبری قهرمان mma با مجری برنامه جیمی جام، ابوطالب..
پامپ که برنامه جیمی جام رو ساخته، ترمز بریده و داره یک کیلو طلا بین مردم پخش میکنه،
هنوز سهم خودتو نگرفتی؟
این کد سهم تو : pump
توی اپلیکیشن پامپ این کد رو در قسمت بازی میتونی وارد کنی و تبدیل به سهم از طلات میشه
اینم لینک :
👇
👇
👇
ثبت نام و دریافت طلا
دیگه خود دانی...
@pump_vod</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/95220" target="_blank">📅 19:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95219">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31b551cab.mp4?token=Y7RFkQf-aX3jW_UHzg5AzEn92xcRyRacd7bcss792K49Uzp2lpdiVf7dkUvklaSMKhVpWRpa9e-2WTiNRLOaZ5WIiPR6XoJkMLedTlNrKGRnN3bCz3CKZgE3V_gRBtbmEDNwod0VULrRdjBKxpNNSV3cxrD8kLT3sR6z_N8mjgiaRGa5X2MeT2mYUpokmF7q9mkoKV93Iqn8pAiBXBTYYG4DDsKEpigg8crqavpJg1uesyAocvYEAiEQy0x8sGckjmV1Mz89Ge14gv2jQEdwTX0vSZwdpIQ7efd9mVWdWVCHZ-gJfZYBGVpxoxDXmL1mM8Ym-0lsN69RF1vTzV2BvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31b551cab.mp4?token=Y7RFkQf-aX3jW_UHzg5AzEn92xcRyRacd7bcss792K49Uzp2lpdiVf7dkUvklaSMKhVpWRpa9e-2WTiNRLOaZ5WIiPR6XoJkMLedTlNrKGRnN3bCz3CKZgE3V_gRBtbmEDNwod0VULrRdjBKxpNNSV3cxrD8kLT3sR6z_N8mjgiaRGa5X2MeT2mYUpokmF7q9mkoKV93Iqn8pAiBXBTYYG4DDsKEpigg8crqavpJg1uesyAocvYEAiEQy0x8sGckjmV1Mz89Ge14gv2jQEdwTX0vSZwdpIQ7efd9mVWdWVCHZ-gJfZYBGVpxoxDXmL1mM8Ym-0lsN69RF1vTzV2BvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همچنان ببینید مردان عزیز بخاطر دیدن جام‌جهانی چجوری به بختشون لگد میزنن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/95219" target="_blank">📅 18:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95218">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lq-HORrKWJrhUgFWgVsxSWwq_9FnYoLUzdpa9UHy5lN8T0Uqnm0shceCRWXY6s-XhCGIdwsjZqT3TFODtQ9q_-7zB_RZGuzp-aCAJr8EtMyQjPubi63R8gEDB08RXgnhdmDBF1EX8PC9SP2niwtaVsUAwF3ksDuAyjQFmiohq3fTVoy1dwc_GiUnRd27rgDJikDHZj_Gz32YYvqx6bdr-DtlwCkMvfAvHqqxdKq2XMpPsch8YQHthYs0bZnWaB_tBtXlkIi-LzGT57gI43jc7X_q2ldg7ur6n0bX9iBhrLoQVS8JrM0G-3-TuVwLU3q5Srl-PA7WAPsXv4FbLMFF7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇷
ترکیب‌آرژانتین مقابل اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/95218" target="_blank">📅 18:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95217">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTHFj0S8yFgs4Z6hUzygLI1iXSsGNHdYugKMzbWE2m9-LDAlftjlxs1Jhp3Ui0p2XiM1M-YZsbRj2UJz3lLxHGsaNyD7zq3oF6rP-zx_j8-EOmvaGTp7VRXwqeqcc9tqwM7f36x_rOZaiBbaVO4K4pwOKfcPHWZE4HAeu2A0rxcH-Xwz4-HM97eY4R7eCX4MKBRpSKhdVlaMoONDgb58uVvt19zvUpE8c3jIi-b75BNmbE_AwZNATPWDecASlOmqTGyuZ-2ly0F78sMlXBrPSLqY0GoqQp6Cgu2O3dN0JEj3tL-Jg1ZW116Q9eSD_soACtaQRH810AmVUQETuAcMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🎙
کیلیان امباپه:
بازی مقابل عراق برای من تاریخی و خاصه، چون صدمین بازی‌ام با پیراهن تیم ملی فرانسه خواهد بود.این یک عدد تاریخی است و برای من اهمیت ویژه‌ای دارد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/95217" target="_blank">📅 18:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95216">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da647ab79c.mp4?token=i-i1rqbsQG0OmjaJHjXcjxQPmPsVtqLKgW3f55tEuYpplCgTMBwXsrO6TDvdUc0TNjFkdwkNOKg0xL3bN-HsxEsK8CvpvtYUTFOJffmf8cyIXuN907shP8B_cw0YzwXYZCpXW4TihOc32-aqUur1nDH-eOmVxmor8Oe_MgcuD_lzxnvn74GZcjsSEfgx1muWiXfB_6thYXxtVWIVOCDhi2xhHcHj3HMwcjw-DY32rWpan4RUJ-YAtxYqx4-joMQFMiTeFrMoqgYRzviDF3FH1SG3DBJifxtVo_f6MqPa-gXJq10__pi_lTasOI1kYppsB_ijWu5J-1rvOWnIdl6Cpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da647ab79c.mp4?token=i-i1rqbsQG0OmjaJHjXcjxQPmPsVtqLKgW3f55tEuYpplCgTMBwXsrO6TDvdUc0TNjFkdwkNOKg0xL3bN-HsxEsK8CvpvtYUTFOJffmf8cyIXuN907shP8B_cw0YzwXYZCpXW4TihOc32-aqUur1nDH-eOmVxmor8Oe_MgcuD_lzxnvn74GZcjsSEfgx1muWiXfB_6thYXxtVWIVOCDhi2xhHcHj3HMwcjw-DY32rWpan4RUJ-YAtxYqx4-joMQFMiTeFrMoqgYRzviDF3FH1SG3DBJifxtVo_f6MqPa-gXJq10__pi_lTasOI1kYppsB_ijWu5J-1rvOWnIdl6Cpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
رختکن تیم‌ملی مصر بعد برد جلو نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95216" target="_blank">📅 18:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95215">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e631911e7.mp4?token=Ul7n3pQg6JAjC1gZgcvDdxYuJ5v4DHUNJkEkAsy4LVYEJxA72raFtvTmLcq-X0IfY23pyEfJH-9gstU7xlxsi0LkJ7vpsBCTsSjz_DSXcWpv9DKncWSi22QgolnB87TOA_c66SUxs1p-BOh-Jdcrr7SyJ8IuSRangjy5Ht8MRWWhvjAdCchnX9XELLxC5o9aUzy-RfTEyXy10GPnAA-B8uZVRyv_9iBHa7-xNNgmgtsROsxvIW1W94cpUHkmw8ZP4uFKAsoDUJEo2PRgL0-dV2qjV6zUwiXnQChCTu78thwhUQYo9q6g30Ok7PFHEDRGxku5VidpheIL-8272Jim9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e631911e7.mp4?token=Ul7n3pQg6JAjC1gZgcvDdxYuJ5v4DHUNJkEkAsy4LVYEJxA72raFtvTmLcq-X0IfY23pyEfJH-9gstU7xlxsi0LkJ7vpsBCTsSjz_DSXcWpv9DKncWSi22QgolnB87TOA_c66SUxs1p-BOh-Jdcrr7SyJ8IuSRangjy5Ht8MRWWhvjAdCchnX9XELLxC5o9aUzy-RfTEyXy10GPnAA-B8uZVRyv_9iBHa7-xNNgmgtsROsxvIW1W94cpUHkmw8ZP4uFKAsoDUJEo2PRgL0-dV2qjV6zUwiXnQChCTu78thwhUQYo9q6g30Ok7PFHEDRGxku5VidpheIL-8272Jim9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
🇺🇿
پیام خامبروبکوف بازیکن ازبکستان به گلر تراکتور از کف لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95215" target="_blank">📅 18:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95214">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKVC3gvY_cAIm8n9_EawtRzmYSrAooWsTrDB6D5eaZPZIUR-O5y5NEh1ZDAot5eQDHSGHii9kAha7FiisOW8wmhpm3at35U80GfuPEixRb7sHA6B6is3DQwM0fwfBKACU-dITDvdHNf2LPt-___s0bwWVFfNj1I9ubN4bZGw8QJ0mp0cav-hIu6nwvAu025iE-3ClOpS7G7vxBYwCpG6NQHbFKWTzpDSL_5rFtO2knRQ2lXRPl9b5HI37As0JdtKtLlzxNbTPgZcWuc3QKZ_SlwXyt7_7gKMBixJy91H-dO_AiFUu4EvnZWI3LOVH3tNyZYKuciQ-sEpImSA-kdwjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
وینیسیوس بیشترین تعداد دریبل ناموفق رو با 13 دریبل ناموفق در جام جهانی فعلی در اختیار داره
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95214" target="_blank">📅 17:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95213">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f259a130a5.mp4?token=LJu2yVL2dxUhyVMX1Xpv4Uto4--5SjQHRik3Aw8ac3aHl4o0Yjjet7hvpqt4oAx3bgLw5CpConk4Y6dUGI0loE_JVARJJLn7Xuj8b6-4jRB0qmz5XJTwsChcDsorE7LsBoiQhBOyCh87KgWHwU0QaBzUaxkai1SSUZFChD8AKGPNmB5W6qejiHVun-MKk0sTxzxSrDQlbI9FY_2vxw8gQYGvCMahYSYpjr6LDDgx9LMHZS1hVmamf9ri84PQE4-6sGl9-oAbojiFd5RvXuqZTBIRSZXWeawl3AZ5dFGoXNTA8ueYjJdVRQYTO9UZFOp58P-M-mCneE73-wiCQ7cjww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f259a130a5.mp4?token=LJu2yVL2dxUhyVMX1Xpv4Uto4--5SjQHRik3Aw8ac3aHl4o0Yjjet7hvpqt4oAx3bgLw5CpConk4Y6dUGI0loE_JVARJJLn7Xuj8b6-4jRB0qmz5XJTwsChcDsorE7LsBoiQhBOyCh87KgWHwU0QaBzUaxkai1SSUZFChD8AKGPNmB5W6qejiHVun-MKk0sTxzxSrDQlbI9FY_2vxw8gQYGvCMahYSYpjr6LDDgx9LMHZS1hVmamf9ri84PQE4-6sGl9-oAbojiFd5RvXuqZTBIRSZXWeawl3AZ5dFGoXNTA8ueYjJdVRQYTO9UZFOp58P-M-mCneE73-wiCQ7cjww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙁
🙁
یه نگاه به پشت سرت مینداختی بدبخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95213" target="_blank">📅 17:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95212">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUKHrHfkUBbz2xkDXnzf0-8Io1JsGgtRplnW8vD7I98W9cTIW5TQYmF8uoIj51ZArrV-Km7p1n-w4NLHruAz_jvY6ihdOzkEqamjUF3gKyCPW-KCkQZtsafaxa8A0cg7bBxz-a9kHnR-i14SPQRCbPPStBMFve-hK1RMXnCjqyVV8njCCEsAr1yOC2EkC-kk32cCm4dT8IOSd2cNdUjh9QHQukseoN4N0kZRIw6OjbrFvO3i7FLdOcToQ7nRdk-FT7GwNHf62uokQMVYDM_st_HWzeocPM109JAAbbJITYwkVrE6hmnllIhCNxc-lS2d4Esdln8BYXIxB7fNemVoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آلمان در هیچ یک از ۱۸ بازی آخری که نیکو اشلوتربک در اون بازی کرده بود شکست نخورده بود (۱۴ برد، ۴ تساوی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95212" target="_blank">📅 17:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95211">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03064bfe95.mp4?token=ehLznoMshQCoO2fpZQJSehtPaQmMRLL-e4VfSdawI5nU_KUm9XlI3DtIiBmhOtGCWa4nMJduwSbL_SjNAnk308GRQQuUE9v_ZQ-PntY2zeMZ7CoCc0uxdb_1dZ8c3fgevYHZ10kstS9voEvYZP12KoqqM5ml-aqc7JNFYZ2YCu8kGPR8EZ28QcpAn4D_P7iGY1-ZmJaG2_TyKCYH62eunDGq2UhUCqnUst66KnxMXpzLLV7VmmgjWnbm2WSD9KdwJ7oAiuRp8a58i6HR3BLo29kZNNv4dcKjr5kBxgSKlKAUsffU5XXi246tbQBd5OX7684sL7xKXmfFKM_JSbhH3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03064bfe95.mp4?token=ehLznoMshQCoO2fpZQJSehtPaQmMRLL-e4VfSdawI5nU_KUm9XlI3DtIiBmhOtGCWa4nMJduwSbL_SjNAnk308GRQQuUE9v_ZQ-PntY2zeMZ7CoCc0uxdb_1dZ8c3fgevYHZ10kstS9voEvYZP12KoqqM5ml-aqc7JNFYZ2YCu8kGPR8EZ28QcpAn4D_P7iGY1-ZmJaG2_TyKCYH62eunDGq2UhUCqnUst66KnxMXpzLLV7VmmgjWnbm2WSD9KdwJ7oAiuRp8a58i6HR3BLo29kZNNv4dcKjr5kBxgSKlKAUsffU5XXi246tbQBd5OX7684sL7xKXmfFKM_JSbhH3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇪
بنظرم امسال به بلژیکی‌ها خیلی بی‌توجه بودیم؛ ایشالا به مرحله بعدی صعود می‌کنن
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95211" target="_blank">📅 17:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95210">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09841eb1a7.mp4?token=TkPEF3fjtVUZZQjDKmil6rVy24e2c0WbtDdAclLmgUWpCHEsV9JzLEJ1_XU0Nnofjc1YkPLddqY5X7jEmOw5m0D0C1YDVwKyzv4dXN0UP6sVhcAPJJIcMM-UfDL2qnakT4K-tbbVrnAHQfqN__RkeP99tHNRs2qHQY7t6D-tY6D__qHbQtkmoIfN-mQ8kZgp0dP6hL02l8y064g32VKwT4SC6euZ0bn4sQVu6fElKB1XuqTMPu5IAedDQKwEewWe24Rq90U9jgS521qNKq7C8S2egKUxle4cCouHxR8lVllVnyvWf2GhkEEv1uj9FTTBx029AUPlI2VwrQ_A8dsXdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09841eb1a7.mp4?token=TkPEF3fjtVUZZQjDKmil6rVy24e2c0WbtDdAclLmgUWpCHEsV9JzLEJ1_XU0Nnofjc1YkPLddqY5X7jEmOw5m0D0C1YDVwKyzv4dXN0UP6sVhcAPJJIcMM-UfDL2qnakT4K-tbbVrnAHQfqN__RkeP99tHNRs2qHQY7t6D-tY6D__qHbQtkmoIfN-mQ8kZgp0dP6hL02l8y064g32VKwT4SC6euZ0bn4sQVu6fElKB1XuqTMPu5IAedDQKwEewWe24Rq90U9jgS521qNKq7C8S2egKUxle4cCouHxR8lVllVnyvWf2GhkEEv1uj9FTTBx029AUPlI2VwrQ_A8dsXdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلاتان: من فالوور ندارم بلکه کسایی هستن که بهم ایمان دارن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95210" target="_blank">📅 17:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95209">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddbdd43d54.mp4?token=G_Tx-SMPGklfPt6JtADz0BHT8nkmInM9XYmK7mUkhsb7C4PiaTwcGTXtWd6mOWh7bP8a4ylVea8-5nsOZNz3WfHRgS4ykjzIFV0kkPQix_0iyMoSznBWJkEraKKEnHFVIexyniSh7GqKUrS2lS9p4LpNHGbTyFOXyj9HeXXMisL9e4vESkcdiM_6HpE_QPEZ6WLOhmFoafx6DwtdaYb0GBRE6uh_JpilJwpJjaGgAP_oHfxZypbXuhfEIOp2_I9OWPj84u7LjNjbIDV0077u7_t7v6yQ5o_30eIACUJ5qWl59c4xmEeOj8Z4TYqHCFoLEo3J-chE2xNh4i4sdjxqtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddbdd43d54.mp4?token=G_Tx-SMPGklfPt6JtADz0BHT8nkmInM9XYmK7mUkhsb7C4PiaTwcGTXtWd6mOWh7bP8a4ylVea8-5nsOZNz3WfHRgS4ykjzIFV0kkPQix_0iyMoSznBWJkEraKKEnHFVIexyniSh7GqKUrS2lS9p4LpNHGbTyFOXyj9HeXXMisL9e4vESkcdiM_6HpE_QPEZ6WLOhmFoafx6DwtdaYb0GBRE6uh_JpilJwpJjaGgAP_oHfxZypbXuhfEIOp2_I9OWPj84u7LjNjbIDV0077u7_t7v6yQ5o_30eIACUJ5qWl59c4xmEeOj8Z4TYqHCFoLEo3J-chE2xNh4i4sdjxqtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
آرژانتین عزیز امشب بازی داره.
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95209" target="_blank">📅 17:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95208">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b38f207fd.mp4?token=QgS2afHWgRDAOezY29REy6MfYLelOY-CtrMp_wFIgzUqB_5NWCePBrVTNeNcYFHgx4XS0aqIwZBOjESZE6waLYoCiEpJ3-JUrkv3Imz7wBq8yyRTmKj7aMzZDerc-47luN2Gs5JbZ_SnLBBcEHaczPKtCiZfs5_3Opr8yeXsOTITIuCMX18dhPAKlqRNwkv6tZwTvx7Io86UI8Byp2uuoKk730LrTYl6L2zx0bT4Jg35fFR-3Gym0nlwLT9HAMzZXOheHY0I5nMsu3hU02wcgY4B6jmjFOLZLK9PHVRNyQgGAbaFxt4O0Di4e0JqaHsT6XjDoJkKb5L6cA-3wxwAJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b38f207fd.mp4?token=QgS2afHWgRDAOezY29REy6MfYLelOY-CtrMp_wFIgzUqB_5NWCePBrVTNeNcYFHgx4XS0aqIwZBOjESZE6waLYoCiEpJ3-JUrkv3Imz7wBq8yyRTmKj7aMzZDerc-47luN2Gs5JbZ_SnLBBcEHaczPKtCiZfs5_3Opr8yeXsOTITIuCMX18dhPAKlqRNwkv6tZwTvx7Io86UI8Byp2uuoKk730LrTYl6L2zx0bT4Jg35fFR-3Gym0nlwLT9HAMzZXOheHY0I5nMsu3hU02wcgY4B6jmjFOLZLK9PHVRNyQgGAbaFxt4O0Di4e0JqaHsT6XjDoJkKb5L6cA-3wxwAJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
🤣
صحنه‌بازی دیشب که قلعه‌نویی در آستانه تجاوز به سعید عزت‌اللهی پیش رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95208" target="_blank">📅 17:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95207">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
وزارت خزانه داری آمریکا: تا تاریخ 30 مرداد ، تمامی تحریم‌های نفتی و پتروشیمی ایران برداشته شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95207" target="_blank">📅 16:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95202">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eao2Ip08J34y8ZPt2kCteFSVd6Qd39iWwuVRpjXHPT_pguL2hWCVkjuyF_-Xp3J8sYZBd_8MD92PfkkRoNJgrq8cS93h3ah2T1EUPPkUloI7kbbSVOAuwvYJGSKmaHYQURCf2S5Vqp23atJs29xsBuGZLaQRB4vHBOYq0NqHB06wSPQwmojDwdL57hblASJtIbaS6WRR24mldCc6NH9kr5Xq-DtNNkppQ0GsKpiwjaN41XskTBxsM_vme5F_IKNTtrkWR_tGKhSt7bDNOpsLcYFI1CRxoaEj_SdrkJIBihcUaDuzDSF0lYQEAyPmZ74u_IwLKQxP4LaM2MscJ5LnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/godXykgWVxdEtCTrgl1-2kKOvUUoqsGF4dRsSoNLYq7fb7QmaDrbFxTApEID3cenyt734Q8ZL1kPn-V8F0fS8Nr0h8dT-kF58LQFqKzHB1BlaS3ObelVSTJQ1XuPuXrlXhRlnY8JxrzCC7uB5HqtaDP_AVEZk6TQTn_-HDEbJXhQuaMnb5vc49eh6h5g9WTPqd5IsApvU7VJwQZeVf5dcYbf-ySIwa_BN011BdprS33CNiQYVJ8sEMgMvD6o6LFWW8Z-ZK-FwfndOwJD3JtGwagUFtcX8-JLg2RyjIaLBm6UHGmKItKQ-vTZlvHLXFW_k4wrdo4DrwaGUP20fldMAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyiE4-0RvIwLoXAaioDvMh_KSy_QHBYwwNF2qtldgOlQG4dkkARmZWXY6mZMhL7pI5onW6WFWIPsrSWTKdc9SnM8_FIxYzOUBNsNSdjkC-pcg9mh8LbTHaTUrdVWeHVkMNxI-rxzBNniZYwfck3jpdqzY5kTs5BwrAR15IgUaJSbTTsdzVcoRziSmWW3_9AjuXJOzcAXf0O6fVa3eZUYJO4Ipn9icpEZa6XupLG-tdIj6XJYw6MY5A6jgVvF1uzRroe1ttj8chVIEZWI86sxcYqAbqfhD4wdWU8eepnMSjQEbrrPXCHC6BTG1EOfhWnX3BOsZRT4sEgv3rX64W9G4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYRDMZ5smONWIFG-pzk7mzjXITndgsCAoiOeNypgm3xBBdevGVNlDJyXup1AWbZKUe6loqMhWcZRylSlJfRe60uAQtiumWX8pumyY-yaJVt-EWPWBBmPGGZbYJ2KPR8YZNfV08xBGib_ceKgowsJzmtL5XWF4aYpAE4mTRoqd77E0vHQjQVFSahkYCeyLS9LgToUu4y9NpCJlxvFLLkXhuXqss4j2Uk794LKNEOpYdmFLB70jFiIZKKcxNwk9W0Mndpgt9NPT3vDYwxl2zZl3EghoJ5b_el3eErXV9v2cZhEJ591bK5-deNAmxbCHajKTHOAILTUSiMpw1prJPWrYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuZ1EeEDR1SfM6iycckJ0VuoCEx6WZ9GVYVBVReZWGfUerllJJdn6Y3ujFVVv4nP7CUGum4irzmRsmKeI_bcVxa2eYMFMhQtV-OtilMc1avMJFaRMQFun08jSvFiOEwwdBE0pjEVpy7iq7h3SQM1NkuasHqL9uw7cXT26WVvzvxCKLeMsDXzDs4VHw--_0h9TorCYa6j961bB4ga3VqXZMhfUdgmesvzff744kHB-lsCGvCiBhSeG1OqVdW7X9Dgk7TggiDhs4P6A_RCwrLskK2IlpgSdhxsxwbciD-c9RNvmE6WcyBc59ZqYJeMJJ55zJ4IM0epZOxsa0pLbH9JCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با شروع مراسم دارک موفو در استرالیا نزدیک به 5 هزار نفر لخت مادرزاد رفتن تو آب تا این روز جشن بگیرن
‼️
◀️
زن و مرد قاطی بودن تو این جشنواره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95202" target="_blank">📅 16:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95201">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPTiQtA6sBrgu1WIxfavdjwWYhq78D-HqnR8CW-VOyvHq3lpm7MMoBTqo7k5offRr_c2DP2Z9Wcm3cypEzP0iviINXAakQcmL3iSfwUrWCuUUEP6P6EpdXazaHQ31ZVFJTRSiGndBtqvtbssdNCjPSfX_4RZi8ocHsgDGBG3WgGSYf8DZGgxIuSVG__MtZuVolARZPrnmoETdZx8l5Ab8GvEH81zmFs4D8xpkQmegu9h9T1D6ehu8Sb7uGuVwvlx50EK3zUaOoqvyAJQa5jlcVimBhOrlh-xYMlAySruTVVCyXkyQY9vC9oyO-c-uSZQtxjgeqDrGKxe6RLKk3xIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ریو فردیناند:
اگر گل های کریستیانو در مقدماتی جام جهانی نبود، آنها اصلا به جام جهانی نمیرسیدند. حالا مردم می گویند او نباید فیکس باشد؟"‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95201" target="_blank">📅 16:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95199">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqIfJMVziZpvl4uWp6w8tiy-8O8P6dYOSt9moS8fbDnHTQKlxAt3ji_H69mKoBX4HuLOqNZgTWgOsyGB_euED3LdOJSn85zydmFwENR5ugeF3t6k3PcGnwo_69-vgbrQqXrRJkpcbWtMOnXuvN_E7DMqaNuS5uTABEC6EqUrn8xJHVOPn5_LLTCKFkdnxXgVtJsGCWjbz6hmCs0P2Khh-nGWXrYCU9oMD_V8iRPWG3jJU4ogiuQMP2DQgchnjYC_Aia1tvl6VMBx8-KmNgO-fknc9Hb_D5PbVfroYPoCA6ynHwQA5f6aiNvwSN3Op36u7XXSb_4N3Q4lgaldx-OysA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زلاتان ابراهیموویچ:
لامین یامال الان بهترین بازیکن دنیاست. واقعاً شگفت‌انگیزه، هر بار توپ بهش میرسه یه کار خاص انجام میده، فرقی هم نمیکنه دو تا یا سه تا مدافع جلوش باشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95199" target="_blank">📅 16:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95198">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0ELUwlW2PY3jcatNC9sFgKRUFzsjRO5IK0FApETHhIR1ga2KVYcZFhOX_FpxmjLyzItM-4qIjLlenKfx-MrdYXYIrgW1iCisnRvcvqGD3VVJmA-qr01UgpMWY9fkChKwwlnSU_iI33imblVmTV_m1lK2gzNfdfgh8FYyVXBWc8IizCrKOBFvILt51E_ANQdpvZHSJ2CyopqR_mc80ISH3Cy7Xxfc31jYkRoyv8x1cra9y13o_FpSEwbEfzRsncqVMhNwhPNXDAfQTEONeXKNZwmdy3KNohL7S8ccYioDav2UkHJ2Q2pcNczTnX4kGiUKqQh_uQ-32l00uUkmNtVug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونو فرناندز : بچه که بودم دوستام میگفتن من مسی‌ام، من فیگو ام، اما من همیشه می‌گفتم من کریستیانو ام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95198" target="_blank">📅 16:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95197">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfOIPH142D-X8_Rnc7w586HoBi1y6dx_N_jj1OoeKSOYMj424fReRkgH6ot-BCJAd1hI3H8RfPenlSkLM6NWRug0JFe2PVnEnHAETQkLxCxb-tl7L2hjSQDv6RHsCi6stHBkNmg_9KPfnlxTQTSymRgS0Lz5TyM8kLlp3bNYbbEEQX6YIjrg7VVnk9tIhnzi_OQ4c01vDPgINd1_XAffxzxmy1krv1rCYDLuC0txWb3zmfE8h0tDET1myEmxH3xLN8fhtgQo_dp56BSPLEuTyZ_ilHjmrbDW24IGtAtuxgf0tefGVtpz4qE9GzcyEmuUGzVXrZnukSIZSF1RQMYgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطور در لیگ پیش‌بینی «همراه من» امتیاز جمع کنیم؟
🔹
اگر در لیگ پیش‌بینی جام جهانی «همراه من» دنبال بالا رفتن در جدول هستید، چند راه ساده برای جمع کردن امتیاز دارید. اول دعوت از دوستان؛ با ورود هر دوست به لیگ، هم شما و هم او ۵۰۰ امتیاز می‌گیرید.
🔹
راه دیگر استفاده از سرویس‌های منتخب همراه اول است؛ فعال‌سازی بسته‌های اینترنت و مکالمه، بسته‌های ویژه جام جهانی یا تبدیل سیم‌کارت اعتباری به دائمی، امتیاز اضافی دارد.
🔹
اصل ماجرا
پیش‌بینی مسابقات
است؛ ثبت هر پیش‌بینی ۱۰ امتیاز دارد، پیش‌بینی درست نتیجه ۱۰۰ امتیاز و حدس دقیق تعداد گل‌ها ۱۰۰ امتیاز دیگر. پیش‌بینی درست قهرمان هم ۱۰۰۰ امتیاز دارد.
🔹
در بخش «کسب‌وکارهای امتیازدار» هم با دیدن معرفی هر کسب‌وکار ۵۰۰ امتیاز می‌گیرید و اگر همه آن‌ها را ببینید ۱۵۰۰ امتیاز اضافه هم به امتیازتان می‌رسد.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/95197" target="_blank">📅 16:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95196">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4966aefd9.mp4?token=Z-wm8-uNEOIvGHng3SrwwBcVhPptlFz7klpogXHJ8DtINDjkQK7otYhqy60Jugeig73LHMst5dfJvm1eETuPat8y2iemJaUS7sSbUixBlWOGH0KF0ZfqNENUojkNEIY8mC-Ik8QizmfjbW_ketnDQoDaXelW7-WJPGGTuXFPu6DsOsUtSWzXpS7QzTFTWuz8QnmnSGkMhjpkn6iRuIC_rPCk448xgwx9TgPWz0N15H2RLXhWBi-WT8pUMKb-wB2BadcmmvC36SJJmA3MNWV5Jw1YwQg0UYdOUPXtc844dwABqHNe5wouPEqMSuO-pdV-VkuNhVvuoPymn22hzm-Uow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4966aefd9.mp4?token=Z-wm8-uNEOIvGHng3SrwwBcVhPptlFz7klpogXHJ8DtINDjkQK7otYhqy60Jugeig73LHMst5dfJvm1eETuPat8y2iemJaUS7sSbUixBlWOGH0KF0ZfqNENUojkNEIY8mC-Ik8QizmfjbW_ketnDQoDaXelW7-WJPGGTuXFPu6DsOsUtSWzXpS7QzTFTWuz8QnmnSGkMhjpkn6iRuIC_rPCk448xgwx9TgPWz0N15H2RLXhWBi-WT8pUMKb-wB2BadcmmvC36SJJmA3MNWV5Jw1YwQg0UYdOUPXtc844dwABqHNe5wouPEqMSuO-pdV-VkuNhVvuoPymn22hzm-Uow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
لب‌بازی لامین‌یامال و زیدی در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/95196" target="_blank">📅 16:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95195">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpOQ9ck_4UwzxGiJwwoaqHJLe5ItGmigx9yXdLV45fuAT0dv7qEcHRC0AR0yPU4NulGDlHe_WB2jZuq-3h1y9pmg03hcYiLW_g-Bs2GN4KdjjFjArXFApRMJtdpTAAh7DpmTJS0ltLf57sUCPkt8CURmjX1u9l1Q2bs4AIq5fjTYzu8Fbm2qHHALRMvjhHG4Bp6ilSYrLEoAvpMaZV9gJMd3HNluqqxj-J07HL1B00R-HTWOe5bYrYew3vciih5x6ARCjmMBU13eZIkttFQ3hsbOU1fBM_m6BMZR4WE0nuVZrhv2rj4nflxEo_PQiFYyzjvpxpJp-5-rkSl8R1Tu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار کلی لیونل مسی در برابر تیم های اروپایی در جام جهانی :
17 بازی
7 گل
6 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95195" target="_blank">📅 16:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95194">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwPk2FGLz0Cx_P3_JeObP7S3ChNnWl4KcaWzFa-5WbLTOmYbhS9iiXJAIcUwi29qZQMewOkc_I-4fXdJrwoA_myk6PzQe23y5wLcyamm14Zs2nEaquafAStJf1EKMVXH2OpaLGriHHX3S6cY4Ic4fw2NAji4RuFZsWphbsGbwEB9yZ0jIdpgLviEAEnNMW2oqJ4NPEA_79_-MeXCpL7a3DkpsFzYLNcLF-ucdPFG5Da6URVeMiRxFJCGsOS2HQljcvvLx11JGLGzy_ENr5_tS7cvwPnnm8ibay-u7q91ioZOJnJE452rr3BWXL9dFzhR5lchMJ2cHUwg8_WkE65itA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدوی برزیلی:
درخشش مسی توی این سن؟ من وقتی ۳۸ سالم بود، چهار سال بود فوتبال رو کنار گذاشته بودم و ۱۲۰ کیلو وزن داشتم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95194" target="_blank">📅 16:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95193">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7f6b7006.mp4?token=pceT8iJMA6rMjp1vafaN3nFeYYKtzpI_gB9OTzHSbtdqlQCsFp7c6g2SFzs2eq9FqOyGIRStKqbVyexJBKydoDsHeVXBlLrWJkS9sZqOd6Ou4iQ3-excb1F_U2rOYQKBlulw5ttlKTp4YCVbaYqCnfrjoWKbmezG79vDUjtfYcwrrxhdleB95NSg5hy_4uEG7NlgJ11hXA2wyJw9fMf-kPMmm45MV9I5HPb-qLGRiVP9CZNhY6NmsyTAsSvbalSuvx5noHuICLpxc6bFiG7AWtKgQCO7_ZXOyFnrn2chF8MbgTutclNbW7WpwGDdiiCnr5K5oGLBvtGvYrRqgLGlcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7f6b7006.mp4?token=pceT8iJMA6rMjp1vafaN3nFeYYKtzpI_gB9OTzHSbtdqlQCsFp7c6g2SFzs2eq9FqOyGIRStKqbVyexJBKydoDsHeVXBlLrWJkS9sZqOd6Ou4iQ3-excb1F_U2rOYQKBlulw5ttlKTp4YCVbaYqCnfrjoWKbmezG79vDUjtfYcwrrxhdleB95NSg5hy_4uEG7NlgJ11hXA2wyJw9fMf-kPMmm45MV9I5HPb-qLGRiVP9CZNhY6NmsyTAsSvbalSuvx5noHuICLpxc6bFiG7AWtKgQCO7_ZXOyFnrn2chF8MbgTutclNbW7WpwGDdiiCnr5K5oGLBvtGvYrRqgLGlcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇸🇦
هوادار عربستانی بعد ریدمان دیشب کشورش اینجوری یه تلویزیون رو پودر کرد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/95193" target="_blank">📅 16:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95192">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🤣
اینو یارو رو دیگه حتی خدا هم شفا نمیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95192" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95191">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7kzNsnqp8eskd1T4dz_1zcebCdp0Omb2Z_WpOIe5L-l73YZd1QDH5zYXOAVn18AHMrauHbPOguzFYO6vRJ69HChzZq_Rqk3QrMgsesWryjPXVyVS2EMro6BNiBLbYVaHAwhm4XKE2DjjmIOmOJWgkZNoGu1xkZ7dc5vDoOyq_JyoiAbYbQZxVa-pmKGq08nMQ02j0BR78YE5yjWvtkYd-YHSePsBhM-Rrl3gcef2lch3FlX8BMMkMWsCLcVrjLC9V_2VtxA7Yj9I9l1rkLOtdq3HRw9SfN59Tw6JGSDDubvMvBCJw2egN8Fg9vHqNC4BKVllUAvMtSYLrHfx_5rBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
افسانه لیونل مسی امروز فرصت دارد تا دو رکورد را بشکند
🥶
🐐
💥
پاس گل دهد تا بیشترین پاس گل را در تاریخ جام جهانی داشته باشد
💥
گل بزند تا بیشترین گل زده را در تاریخ جام جهانی داشته باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95191" target="_blank">📅 15:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95190">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8m-KxB0DR9DtOcwe0zWyqqTGgM4qDNX50ib2VdYU39SOzIr9c7ZqCHdWuUgyhxfvKEKP_WeofBM0mwe-DTl4BmlIKmgro2LZY5io3QDc4gwAi4747TX1yxfH38mfzYLWAO01fLhlSYxEhxUE7LpvoO8Yw9p1KZMzn9g75ByjoRxrSSzvQpTXaMrjIE8KcwrH18dX-mtru3Trl3NsInCNLJERGvnXMOGzhPbKzXrBJ65WyS5BeBb6CVIqXI_vqCLtyNKM_tnP_sDuHxPGJ-jFk-xoH4AQyGPkndJQGeQAVpIclYxCahtZ5y7d30uYUOWEKbD_44G4PVCxsay3vBKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت کروس برای رونالدو : کاش من اون صخره بودم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95190" target="_blank">📅 15:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95189">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhyVlrcG83EKI5IMWpg2XcLGxqGauK3wYYZzAZOQq-nTHoy0Cy9U3F1D-fsJq53rCim7AhK6J3GWYxlvTd1LVlLaS0ECP_PebBtHaicw_dEp03lCq_TobpGWe8ERheUzgZ-qeq6y351E-jEAN-DK9T-7evlFpRzdF7lbERgIscHfB7OPhfAKMoG5m_YXlg6XnRIMBBfbnh3LzIfRSCj978kKmdBJo0WjUp5z8S4hgX40vyF983ezMYDjqG8vQCQaUfuYXw6obnwaHPjEoAgBpum5DesZQGlJr5poniptP_mo6CQ7lAJR1L5lCrqhcxm-QnNWgcfhY8wvcf5XwxOzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😐
تیبو کورتوا، کنعانی‌زادگان رو فالو کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95189" target="_blank">📅 15:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95188">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDvvnCpj5EH7adEk09nDzOR9CnaZSIRKNIELymKNTioGvVtLU5pWwF9uCu6pm6xqdiufu_rIJaklCKgZLavQBW0AllzPaRpDRoZADW8u6WYmA9AjLI6cMXKshh6IiphCPZGibpQNUTG-EWjuW0k1a7Mvv-d9EV_jG5UVo_DJBOzfHckR1JljNQ9J4VoqcxLMsPlOT9QstFHwnmI1Ql1erV2ll5FtQ8J31jbBEPLeI33xoKUgRlU0M1yh-lVnxVjwy1XJefVp9irx6HzfJ_P3W9vrEtnOnnXJ9HDVT-wWBMz-eMf_58ukdrJpXfPZNV8byeN3KGuhMSC1RGX7u_Z_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇪🇸
زید دنی‌اولمو در بازی دیشب اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95188" target="_blank">📅 15:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95187">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77bb57281.mp4?token=fIEGSeuFU2XmPYEyQfbysBlQWcrspHAijjxOuz7pk56leYMZF-LVIOvxwcCiovuAQ25dQTZNBrYsEIznIEaZetPJtOkGSgooNk42tgIjL6JMTH-2NFqhvKJkatVQpkUsQCmdoo5h-KuQJTuFh30I7r4pJLvj937raTFBE2UQu3Y3rG5s9NbpxLf_UE_ZmxId5zSnJ_3ZMAY5mr_9b0rw0_yqLyooON_57QB7II3lP_hh22DUnItD6KnYHpMRgGHHe6qpSZhoX9EGVAAaviwVsL9_nzUk6H0t2iqSNIHg0tUK22VNnW1KL-pGeGap1XrBQRFa9G-Pq664w42vR9d4XSRaVp36zQVd88cmjCnFMv6AxtBl4A3_NRDigeHTlPhEJ4cQ6yx88Ld1LOZZopjpdqNIe21PO-60-_2avhGwybFXerdbkDjTDWog00NpOdKJ5EU85yD-jJw1UnbhgR4gDxjhQM4a4daLct3kQhCPcl2F8OkU13fFf0YiowwD5cwEvh1o4bhHufeIy8nDy_mZA1ndqFa_lOccUe2VLhfa89bLMVcZJQM7pgXILj3v4OYsBjuyj4jLf2dUig3S9jSeuWxlQQ71ODkeD7kAjDLcxBidFjJTEGSfIm8GS1xnOgiTD6YpEW0WfZd9HBvJbiKEHlcTY8T4zs1Ubl13fAGVCyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77bb57281.mp4?token=fIEGSeuFU2XmPYEyQfbysBlQWcrspHAijjxOuz7pk56leYMZF-LVIOvxwcCiovuAQ25dQTZNBrYsEIznIEaZetPJtOkGSgooNk42tgIjL6JMTH-2NFqhvKJkatVQpkUsQCmdoo5h-KuQJTuFh30I7r4pJLvj937raTFBE2UQu3Y3rG5s9NbpxLf_UE_ZmxId5zSnJ_3ZMAY5mr_9b0rw0_yqLyooON_57QB7II3lP_hh22DUnItD6KnYHpMRgGHHe6qpSZhoX9EGVAAaviwVsL9_nzUk6H0t2iqSNIHg0tUK22VNnW1KL-pGeGap1XrBQRFa9G-Pq664w42vR9d4XSRaVp36zQVd88cmjCnFMv6AxtBl4A3_NRDigeHTlPhEJ4cQ6yx88Ld1LOZZopjpdqNIe21PO-60-_2avhGwybFXerdbkDjTDWog00NpOdKJ5EU85yD-jJw1UnbhgR4gDxjhQM4a4daLct3kQhCPcl2F8OkU13fFf0YiowwD5cwEvh1o4bhHufeIy8nDy_mZA1ndqFa_lOccUe2VLhfa89bLMVcZJQM7pgXILj3v4OYsBjuyj4jLf2dUig3S9jSeuWxlQQ71ODkeD7kAjDLcxBidFjJTEGSfIm8GS1xnOgiTD6YpEW0WfZd9HBvJbiKEHlcTY8T4zs1Ubl13fAGVCyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
England is back
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95187" target="_blank">📅 15:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95186">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce785e516d.mp4?token=E3akmp_EVISHGvemBS8qtlDfdI_590j8R7hEvuY_rSkS_OGEaQKebWtLMP11AAf3fIa6g0NQT_8uQ1SlssWFBPEE1Njjn5DwlxliZGq038nnxnLO7eNaUvTCtBiSiwOoHDW5j1nrVIuG4leHbsojaB4ncCo_n-QGUR4jhvn28KmTAFXGqqiHtntpEHuiy8r8-Vu6wonNANADGm7mfo9R8bEOeThR9Z3G9TaJIWfzffsoPHyq9sHhQEvRMQs0-FrzaSbfcWg8dTGv0JjvdOyX9vGSYRgoUmj6P1O2QDe5IsLXbKEdoZolQFy-fon-Uo86oUPnJj4U3ZGcUn9dIKp1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce785e516d.mp4?token=E3akmp_EVISHGvemBS8qtlDfdI_590j8R7hEvuY_rSkS_OGEaQKebWtLMP11AAf3fIa6g0NQT_8uQ1SlssWFBPEE1Njjn5DwlxliZGq038nnxnLO7eNaUvTCtBiSiwOoHDW5j1nrVIuG4leHbsojaB4ncCo_n-QGUR4jhvn28KmTAFXGqqiHtntpEHuiy8r8-Vu6wonNANADGm7mfo9R8bEOeThR9Z3G9TaJIWfzffsoPHyq9sHhQEvRMQs0-FrzaSbfcWg8dTGv0JjvdOyX9vGSYRgoUmj6P1O2QDe5IsLXbKEdoZolQFy-fon-Uo86oUPnJj4U3ZGcUn9dIKp1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمار درخشان شجاع خلیل‌زاده در مقابل بلژیک در ۳۷ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95186" target="_blank">📅 15:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95184">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQ5_b8IZ3B4DjCqPNPq-OMVmfOPcNKGfqUiuAg2rMx94k5_Ixs8V2GcWxsg6RMoT91qoXGsUD-5AACEG9lQ6TED27RdvDC3wByaUe_wXMROW2m2R5wqXvCxQ2geKLWl_soZSfelNuXOusuIiLszfjS01oRkDWWHQk1K1djxwDLAyitEO8L6LL24CMNPk3sTgfOI1fV_NAYCaPdcbU4OSUTqGRUMHGfabDe2rU86NjN3j5dOpsm-Cg7NEpa1tXatabox66bibxhEIvQmaXCah65RxkzT6rRAWJjM-_-1br6-5vGPK_AxYgi4v92v-Uj9qLi1tK3R2mMgeMWG6sWSC7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👀
#دانستنی‌های_کسشر
: کیف رامین رضاییان قبل بازی دیشب از برند Christian Louboutin بوده که ۱۱۲۰۰ درهم قیمت داره که به پول ایران نزدیک به ۵۰۰ میلیون تومن میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95184" target="_blank">📅 15:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95183">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTm1wmVT8nis8EqJQJQE4sWZ-miwkyFCu210nGUA9yt7DtIvWbYGGQh-wPIqit33rkB6KExB9GbYSsg-JBSAuO9N-RmeT70lDejJpPilJ-wwUukdS06ZIKb75BpUeP5FM8RZur8HHzNNTSaBAphWqMt1PtucdE5a_NOJutM5lEpsMvJ2u_0meM2Ucbdow3rIK6PPne-LE-UCL29g8Iy-iJ9yv_g5BoZvFDkH7Q5wLUjen8etDelEMeILUtxUMGfIndOk7sIEU3NrPjig9DI9eL1Ot5B8a9wavcGThjYhSvjDoiLcUiz-awm1zJK0zszK7UG4IWX-6DakLBPX8rclSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مقایسه مسی‌ و رونالدو در شروع جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95183" target="_blank">📅 15:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95182">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22bcd95a4.mp4?token=uNqDquQufSlLEGz_oeTBs9nW3H45c-IZaX_FcpQHhT8i4a2leC2ToLBuDXHHiug78MJ84IdZZm9wXnYJicj-R4eSWZQ6hmjOGAW7eE8e9BnntJvvt-FqIc3icPs7QPS2hHBdtrOg-5zxrVKaxEJevj1K5aGVXvU85Hr-9AVzNgWhtqFgtaXv8KuUbMszVSZ708CLgn4Gc5_YMJSQM8FoyUzxGEVp55x5spiCBL1iuCB1ev00VmQC7byfN2ZDgQnRy-PjUwkpY7JiJrASCjpZ6qT94WqgPPD_nVkBl9kouBSuV2OdlgAkd7IKSOvCwdFDMSn1jUGLsvfzsTqMZCKfww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22bcd95a4.mp4?token=uNqDquQufSlLEGz_oeTBs9nW3H45c-IZaX_FcpQHhT8i4a2leC2ToLBuDXHHiug78MJ84IdZZm9wXnYJicj-R4eSWZQ6hmjOGAW7eE8e9BnntJvvt-FqIc3icPs7QPS2hHBdtrOg-5zxrVKaxEJevj1K5aGVXvU85Hr-9AVzNgWhtqFgtaXv8KuUbMszVSZ708CLgn4Gc5_YMJSQM8FoyUzxGEVp55x5spiCBL1iuCB1ev00VmQC7byfN2ZDgQnRy-PjUwkpY7JiJrASCjpZ6qT94WqgPPD_nVkBl9kouBSuV2OdlgAkd7IKSOvCwdFDMSn1jUGLsvfzsTqMZCKfww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
🇨🇭
سوئیس رو در جام‌جهانی دریابید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95182" target="_blank">📅 15:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95181">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6Rnzflq7ktFqbDjb4Nzd7IfXltpt1k-sgV4YFHqQ8VYhhHuxr4G7G1YjliRGnuN8haX9lts_5cQ-6z4fD48qrTsvLa0L4Ar61b0L74CGOZyke781EkBw43RIPN20sUFnK9HUmNnfCEUG2clvhCS8IMgoOhVbWqWi7MinQN0RIRtOn3_66IjOMIVMySClz9XqNxzIdwFzunTbfdg4oAUiQUrIZeQzVlStB6FCIiEAEpu5RSbjC8isZRtmmUPHIm4yDGI3Bl_QEmWfDczWcYNKSc4QAcKJHh_oxzXNoGC78xa6X5TgWOrU_ho2khPLgMpNJM8dHE8R_b3yh3TkeTHMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایناکی‌پنیا گلر بارسلونا با قراردادی به مدت سه فصل راهی پاناتینایکوس یونان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95181" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95180">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU0agXfSfNrrcMQ8c4Cja5OpbTbNGyw_3y0Nmd64d2h0J8lvqhiLuwof-OXfh3tJjVfSHi9JYfGrOgtXh_gDhggPXMGRMp1x9RFnm50obGp1X2d_QOZcdUnAqzUykie0m-oU_AIhkvH1TxNJIHr0WGVy44PAB6K4wyricT3m16FAiUjrTK_cSs1vh19hGQ4or-8wCU7Vmo33XYPuJgIlSj2bzL_R5PVCWO7kWmVlKwdrCLg2QPg7tGN_j7gta3pCWAqBFQgsMSXdPszwmYIVee2Exb8pUUiPlFkIoT60R0g06mB87JFiCcSbTuqrSxuAqZoBv9VXa0jxrd3LHQYgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇩🇪
❌
اشلوتلبرگ ستاره خط دفاعی آلمان بدلیل مصدومیت از ناحیه رباط جانبی به مدت سه ماه غایب است و در ادامه جام‌جهانی حضور نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95180" target="_blank">📅 14:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95179">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzNDqiZe31qo_GT38kIBlrO7_00Mk8JbNkLDbO-r3XsSG-O6bZ2N6MIzrNDlxv5rvkzBMUSGEvg_330t3ezyqqVly6VZZLSmEJ_o0jsboKRkbgSZxlRC0cMA_Pfe78U6_CbYMsBUI-u6m-LQy3ud2H5tuhQw2pFc-HnPflbLyXdMV0WyD38Q4vIIL_nwyobrOPf5Yp8IMZBsbEmh75psClpbcbTy9qTlVvTehNCZRoyoteQyHJ10yy6jloL-njEzz4IpBIXn-F1gDffXxSGmeK6GtITTqwjLwu5XJdmj7rQu96G54QwmBrYBJGiqa9mRFNWgF9ERyp3aPrefLFscsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
لحظاتی قبل جی‌دی ونس در کنفرانس خبری خود اعلام کرد که ایران موافقت کرده است که بازرسان آژانس بین‌المللی انرژی اتمی را به کشور بازگرداند. او همچنین گفت بازرسان هسته‌ای احتمالاً این هفته کار خود را آغاز خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95179" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95178">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsHlJUO-_38mT2Lwpn3uSSdJQM56Wmd1qmvidHFvNIOOGvRf24jZDfF6qEDI9mXSQi5pmwHdFnRwdyUimH6C2iBS6Te-j6ziEyoK68B4MGs6FED_ys5Aw5XFEBhIUsLW7ed_l6U5jnATXK-EFYh3ZuP1t969CJKsvjDEb6pAdY8MyLtkTSG1Ea3-EvksfbZeFFgDYK-rQPklx8duwsIgmhOWX2LTWurp1-ZRcEZRz2MF2xI4rgK-lf6hoZTC9YJjVlm_c4OplC507l1f7e7nyytk3uzJCTrYXkWbbvQfTi4kwWVqHEMPznk11x6HFcMSKZltGp3eONYI4CHCnRaKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود بر اسلوت کبیر.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95178" target="_blank">📅 14:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95177">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh_ZKJ4fPAR1QaftwRYWqAd7UAWHQ2xtA_uFGtQ2pTCoEtbxnEZ3WoctUTkc0nlX2BHh8JqJW4YwuudOVx6kVXbU0fml7CRqenO-UNSI3FI6NyS9MhUVC4F4cpvhDuP6_d3FrFJZXGMWibeDg8Q5CaQA7yy7pit6pCpTMZcrszjFeBIkRW8AMgsFSrdUSRDSwtZs1SXZ_crthojZmhcJlSHZdBlscD8lbPZNZVHUTa_epr6sDeNpYHUShjoXJ7kmw4_86W10yQfJ1vbEEFADiXHEqEyvRRQ4AEzZUvKu221VREcXc0916BGWZrI3Y_WxlY6swCGPLFEOWatKG6Dtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرناندو پولو: خریدهای رئال مادرید در این تابستان:
• برناردو سیلوا
• کوناته
• دومفریس
• کوکوریا
همه آن‌ها خودشان را به بارسلونا پیشنهاد داده بودند. باشگاه بارسلونا آن‌ها را رد کرد.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95177" target="_blank">📅 14:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95176">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13fdaf80ae.mp4?token=JhV-AZSmEVUF5RusolVmlhCgQEcZuJPuUk-FD6P_tzS5JQ-Rh1sM7FgLX6dalDO_rCF5woU1VsKUdkQsPmJWx3GRB8vUvqvy2SHdcY5JFnCvRqYb6MPMFhR9bo7YfwIN6-lzk3ZD0h_WUJMRXqgZFOfID97erTuARy6Gdj6eJH7TQijhdlP2gNIEplygxAuj88Bqi7i93STp1Vo1HRY0Jtjco9o2SEb4ikKRm9AbS--7hVyutPPCIOGtLvxYE5Xhf89ITamSU5aSv_Ms1iMMw5G7o5QOQAo_tDAgQiJuCEpuOfQj2io2R1bLNKeTakwYQ0zMM8bTEu4yT23f9rl_TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13fdaf80ae.mp4?token=JhV-AZSmEVUF5RusolVmlhCgQEcZuJPuUk-FD6P_tzS5JQ-Rh1sM7FgLX6dalDO_rCF5woU1VsKUdkQsPmJWx3GRB8vUvqvy2SHdcY5JFnCvRqYb6MPMFhR9bo7YfwIN6-lzk3ZD0h_WUJMRXqgZFOfID97erTuARy6Gdj6eJH7TQijhdlP2gNIEplygxAuj88Bqi7i93STp1Vo1HRY0Jtjco9o2SEb4ikKRm9AbS--7hVyutPPCIOGtLvxYE5Xhf89ITamSU5aSv_Ms1iMMw5G7o5QOQAo_tDAgQiJuCEpuOfQj2io2R1bLNKeTakwYQ0zMM8bTEu4yT23f9rl_TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
انتخاب تعدادی از مردم بین پول و صعود ایران به مراحل پایانی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95176" target="_blank">📅 14:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95175">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By5KDbgYyKq7w0V5nLLYL38xjG1bNXGhVCSsWSAj1XDoSE1esWg88GJgxZMmWxo3rvJ3aF6sLh0Ds6BZbD9XK8mXxUvDa23v-OR5WLrTwkIXvI54xymz9KHrmAdOMo8YZoKzoy4Ud66KArl2vvFdHwSOFvBzOxaZKvM8MJnmxhEiYZ6MAfbTQ7Ic3gx79d1F38mJsc9MLWajgBbspzPs9EzcwTlha6q_ISTRd4cqow1Aysy4BaBC4_nyXssNTJuEucX4lz0S5YUMabHYOMEiMYMi_8qUdfG8ZYFMg7B20-G-adaHmruwzCFn1zbt6ZBJamIQ0UIpKfYOt5mh72OJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
📊
لیونل‌مسی امروز آخرین بازی خود را در سن ۳۸ سالگی انجام خواهد داد..
❤️
🚨
🚨
آمار افسانه تاریخ فوتبال در سن ۳۸ سالگی:
‏- ۴۹ بازی.
🏟️
‏- ۴۸ گل.
⚽️
‏- ۳۰ پاس گل.
🔴
‏- ۷۸ اثرگذاری مستقیم.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/95175" target="_blank">📅 14:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95174">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e16e4dfd.mp4?token=j-4E1goP3ltirLwUo23BOijzXOVQr-vPxbz0QZbMoAZ04PNlPc1Ln2UZUAGxIHKMBF767Q46pvBqnToT7qfKxK6UDu_fOyAmKBQWkEUYTHN9BuAz9nJfnxnWc0SYzMbtRPhjoX53bPdQB77uWL1Z3rQyoSm_UMbPFdhebLh79gOG0-YQmEfnH4iET7rkjWI0xsGhDuPe9nm1roN1zO9ezL9PncszJwAZyo8g6kHca-HoxAywL0fsZngB6UEqgaGniz8CCV-rJ0f9Oi9d9rgdD1WdsU9tbPiJp7flIs_7wiXhqEsqGRofpeosiG8G3zeNUd8LQ03NAnJsJOyF5WDsPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e16e4dfd.mp4?token=j-4E1goP3ltirLwUo23BOijzXOVQr-vPxbz0QZbMoAZ04PNlPc1Ln2UZUAGxIHKMBF767Q46pvBqnToT7qfKxK6UDu_fOyAmKBQWkEUYTHN9BuAz9nJfnxnWc0SYzMbtRPhjoX53bPdQB77uWL1Z3rQyoSm_UMbPFdhebLh79gOG0-YQmEfnH4iET7rkjWI0xsGhDuPe9nm1roN1zO9ezL9PncszJwAZyo8g6kHca-HoxAywL0fsZngB6UEqgaGniz8CCV-rJ0f9Oi9d9rgdD1WdsU9tbPiJp7flIs_7wiXhqEsqGRofpeosiG8G3zeNUd8LQ03NAnJsJOyF5WDsPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😬
👀
واکنش دکی به گل ایران که نمیدونست آفساید شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95174" target="_blank">📅 14:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95173">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc9b9ff0e.mp4?token=lL6fW-COYYc8UoNr-rRfDcAouVCnDK3k1MHtfDFAkQIcIrRXxfuiTFuFGKWXQqfLPdUkeKQ_gm4yj4WmWO-B4Sv4a5ZrRaZ2xTqsOTbVtY8NXlHGGXZfZBFjdtRthlCI8muwjgWYCvFu4To01oXcBxdc2rB9GAZvwZniun_O8X5pNNksaNAUrq-JKIDA9I-KFD948xtYoI2j6Ui3ftmV2XAhSxlGNRo3a0vtoUQh4FcNP1FirztpvxKoy_mFKA01Vg9sUkEvFxPTBzlQynCKqMYlV5lDFq4vt9jnCQkwtDjatbMBOGum3EOyTHi03RzGw8g5YINn2maKMJJwNN5U7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc9b9ff0e.mp4?token=lL6fW-COYYc8UoNr-rRfDcAouVCnDK3k1MHtfDFAkQIcIrRXxfuiTFuFGKWXQqfLPdUkeKQ_gm4yj4WmWO-B4Sv4a5ZrRaZ2xTqsOTbVtY8NXlHGGXZfZBFjdtRthlCI8muwjgWYCvFu4To01oXcBxdc2rB9GAZvwZniun_O8X5pNNksaNAUrq-JKIDA9I-KFD948xtYoI2j6Ui3ftmV2XAhSxlGNRo3a0vtoUQh4FcNP1FirztpvxKoy_mFKA01Vg9sUkEvFxPTBzlQynCKqMYlV5lDFq4vt9jnCQkwtDjatbMBOGum3EOyTHi03RzGw8g5YINn2maKMJJwNN5U7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
علت تفاوت بیرانوند در بازی بلژیک و نیوزیلند:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95173" target="_blank">📅 14:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95171">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/95171" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95171" target="_blank">📅 14:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95170">
<div class="tg-post-header">📌 پیام #24</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95170" target="_blank">📅 14:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95169">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyNA5kRy_1oKP7yMt0dSHwGfjmcZxnhSInPaLpvvnKWgo_EuRghxnQaWDBt0676a8yexkowBkbvzAfWD9LQIRGRwosupn4_eEKOMXjKxhcOwBUanKKgRDqKk9z69ROM8aggZiudP91uu_-qJbVtYgxrcj7oSW7aNY85jXDgfmLyiiSDMZRhf_8fvlzjsdSKEfepU1EpLMiOTrhCIpmj4dxYCJPzXO_6GDAFCbFB2npKFmw6BwLFak05MbIYU1vQh-ITKURcSpnrdnaPx2_PXwttLYjAN3U_3VBviHtH6LcPtJ_IuW6RfkjXSePtoM54YA-mP7gE4H3tNaxaHDpQxOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇯🇵
پیشرفت چشمگیر فوتبال ژاپن در دهه‌اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95169" target="_blank">📅 14:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95168">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0_IAEaUjfNxE6S90OW8LDWJbF901aEENwxalbODADO3vjBKgEVXzufmLZhXOC4ZCxTOGlyV68S1IWThY-e-hol6ClE91kvqj0o1WYp0ssi_23KB3Pzx0ni3SNWZ4rZxFyh_13V_hR3f9OsytWfSWug9Emur9LFZ4EuBdSk2cJyQDJIHAQIbRDy3Pe1s8juVw0Sb6Ff1Ikf43rZJ1-Qx3XtsXGEpkBHFbYFLO_EIAVQlsBJttcmFPvTNoEc6RdW3hd0rFi1KN22aC1eFiseHcXtb5EbVnSrt5O5iYuihKX7wF6oGP55kv2fGnW3SDCFacqOzWyyV9kyxacGcEx1FJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔺
اسپورت:
بارسلونا گزینه جذب کین رو به عنوان جایگزین در صورت شکست معامله آلوارز بررسی کرد اما کین تو بایرن خوشحاله و نمیخواد جدا بشه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95168" target="_blank">📅 14:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95167">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0a1fb2cc.mp4?token=ifpLEy7V8sl8GtCJCCuQ6qO_0NuQHSB7wDD4GVqoAj5_fjVLB_z0Hg0712YOmoboKsf-uULBKw2k8PP0iplaJnwQyxDO2IuhCV9mdzKe194jP9uxa6RauyP-ngW09ruYeZgB_RcOptEk8VTIzLHfS6nZmi2OXnHke1S6JI7WD32zBGAx3aQmi6HAmvC7FC9KRKoiDrBQJ4OhT5hl1Fl6DnEXmPAoIe5TokOIXFF3HyHQKoI5rJieJsYD9Mm962d-BI9nHswViPDIgHf_ZzS6dZ9_icfx3F9E4gmPQOKANLkOw_mVAjF2j6o-eJfSfAqiHMEAGGRxB1x3QD_o_O6YTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0a1fb2cc.mp4?token=ifpLEy7V8sl8GtCJCCuQ6qO_0NuQHSB7wDD4GVqoAj5_fjVLB_z0Hg0712YOmoboKsf-uULBKw2k8PP0iplaJnwQyxDO2IuhCV9mdzKe194jP9uxa6RauyP-ngW09ruYeZgB_RcOptEk8VTIzLHfS6nZmi2OXnHke1S6JI7WD32zBGAx3aQmi6HAmvC7FC9KRKoiDrBQJ4OhT5hl1Fl6DnEXmPAoIe5TokOIXFF3HyHQKoI5rJieJsYD9Mm962d-BI9nHswViPDIgHf_ZzS6dZ9_icfx3F9E4gmPQOKANLkOw_mVAjF2j6o-eJfSfAqiHMEAGGRxB1x3QD_o_O6YTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
درخواست سیگار برگ هوادار مارادونا از خلعتبری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95167" target="_blank">📅 14:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95166">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b2bd55cf.mp4?token=PxC1xRA_9OsmD30D6u7F6yUdZl5GaRfCUwAzsnLKKiToh38CdNyjNHTMTCyEaKwLL7kN9uTGErCEnwf9UkM2goA-TRY3xPoM2bEs4laCoOlX9ubYiWckvLBQxQeQD6YGFnxgD4PevbWAmq7XmcljWXkpjlRP5Q9FbfdtHAFkgRmy9d1bhqB-tpbc6vjIjCu4okmhhWrsE09F8VYY8D2AqZu09fHhWO9KSUD1KLVxIZkDOH5Cpcoamk0nodFUqh0V3i9s7IjA55iCv25Ss6RgwL8YwtyJ5nxcNt95Mao-uEv7Z5OPXLN7YXg18mqTEe3yyEaItN8jmBSt518KsgXqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b2bd55cf.mp4?token=PxC1xRA_9OsmD30D6u7F6yUdZl5GaRfCUwAzsnLKKiToh38CdNyjNHTMTCyEaKwLL7kN9uTGErCEnwf9UkM2goA-TRY3xPoM2bEs4laCoOlX9ubYiWckvLBQxQeQD6YGFnxgD4PevbWAmq7XmcljWXkpjlRP5Q9FbfdtHAFkgRmy9d1bhqB-tpbc6vjIjCu4okmhhWrsE09F8VYY8D2AqZu09fHhWO9KSUD1KLVxIZkDOH5Cpcoamk0nodFUqh0V3i9s7IjA55iCv25Ss6RgwL8YwtyJ5nxcNt95Mao-uEv7Z5OPXLN7YXg18mqTEe3yyEaItN8jmBSt518KsgXqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتخاب سختتتت بین تماشای فوتبال و ..؟
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/95166" target="_blank">📅 13:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95165">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd7adc8564.mp4?token=Ah-9GsM-nk4VuWTI1l_qLEi5IjFpdA4LiNP5oiUG3FoJxOnCRuqrobTt5SlC0qD3PF83mmt4UeQ-SbCHdQ15Zhh97B-9Xp2sAeOB9xs34jqlYtuA4CJyjDL4pyn6RenuKzesBcytBzrLjo9MN-T9p3oRa6Z1_09SmVLC0W-wEO6_AIRXR_a0S1dUb1KdFsEODLfHoDZSbpYyUFWzlLjS7yc2h2O3KQMapJfXvXx9sABG_fzE1d9Bo-HmeG5FTMNwjbudEdKrmcrWwEXIHBdKwmHNo0NlVUvRLXTV5--1XibwsO0aX5czvuXztcIRN51AML28yndJS4kE9hzcWFPXrKWiLU_HcHsiUCJV8qrlRq81PzCftv6w98le5QmJc8Kdn-tixzHPGBhiLe4vjfFAO4MaAHARIPln6pqiZiZNGxgRL6NDi5SRcn-WVR5I7FSO7irOkXzr-zuJEVCDr0tCCaFc9Qz2I4lO7ZFat1vUpOYWh0YJoq8SK1dgUGWGu6fFDVUD8lVL3QBZS-S80SX5IkWdIN_VuA_MVSfG-re0-RKbpsw2msHBwo7TBuMvZJ0VXh2TtfFPVrpYBnFrn3emypBNl-aITOosi1UG8ifdCqoKeAYRY_yrCimA-4TOSsWG3WTJ4cdZ0FIvX9e7Jyra7AokafR8lRjUwa5B-76Uxlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd7adc8564.mp4?token=Ah-9GsM-nk4VuWTI1l_qLEi5IjFpdA4LiNP5oiUG3FoJxOnCRuqrobTt5SlC0qD3PF83mmt4UeQ-SbCHdQ15Zhh97B-9Xp2sAeOB9xs34jqlYtuA4CJyjDL4pyn6RenuKzesBcytBzrLjo9MN-T9p3oRa6Z1_09SmVLC0W-wEO6_AIRXR_a0S1dUb1KdFsEODLfHoDZSbpYyUFWzlLjS7yc2h2O3KQMapJfXvXx9sABG_fzE1d9Bo-HmeG5FTMNwjbudEdKrmcrWwEXIHBdKwmHNo0NlVUvRLXTV5--1XibwsO0aX5czvuXztcIRN51AML28yndJS4kE9hzcWFPXrKWiLU_HcHsiUCJV8qrlRq81PzCftv6w98le5QmJc8Kdn-tixzHPGBhiLe4vjfFAO4MaAHARIPln6pqiZiZNGxgRL6NDi5SRcn-WVR5I7FSO7irOkXzr-zuJEVCDr0tCCaFc9Qz2I4lO7ZFat1vUpOYWh0YJoq8SK1dgUGWGu6fFDVUD8lVL3QBZS-S80SX5IkWdIN_VuA_MVSfG-re0-RKbpsw2msHBwo7TBuMvZJ0VXh2TtfFPVrpYBnFrn3emypBNl-aITOosi1UG8ifdCqoKeAYRY_yrCimA-4TOSsWG3WTJ4cdZ0FIvX9e7Jyra7AokafR8lRjUwa5B-76Uxlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
مروری بر تاریخچه آدامس‌خروس‌نشان به عنوان اولین‌ اسپانسر ایران در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/95165" target="_blank">📅 13:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95164">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c27b7293.mp4?token=vrd6FFrys6VXBu1MqkihE2SMkTLh2K7SekT6kZ6QvdEUGwa_r0zfzFn3TDfHh0wZOb4wwAVYMtbs3jTU1TcaYQaCU8KkAiTLFGanJ7ne4pqTJdfBewcnITsHYEFIep0B5un0C4zbuGhy1F6sVl9vgQxPF94WzgVKP982SEdDFZ0xCH6LAHSPZz5UDqYx_X5olUnKjjv9luGPglgClB1ERMt_zXYABj7-vnlotuiKXJ65l4LAHVSz0FRa_1Vb5Ns_RnMLr0xqcBjk4JgcSQCMaNYMF7LmFYaryikNhUfNMuDnS6NgZmrmT9U--PC-Zei3PjoWcHg4Dj0QLHcYVBGC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c27b7293.mp4?token=vrd6FFrys6VXBu1MqkihE2SMkTLh2K7SekT6kZ6QvdEUGwa_r0zfzFn3TDfHh0wZOb4wwAVYMtbs3jTU1TcaYQaCU8KkAiTLFGanJ7ne4pqTJdfBewcnITsHYEFIep0B5un0C4zbuGhy1F6sVl9vgQxPF94WzgVKP982SEdDFZ0xCH6LAHSPZz5UDqYx_X5olUnKjjv9luGPglgClB1ERMt_zXYABj7-vnlotuiKXJ65l4LAHVSz0FRa_1Vb5Ns_RnMLr0xqcBjk4JgcSQCMaNYMF7LmFYaryikNhUfNMuDnS6NgZmrmT9U--PC-Zei3PjoWcHg4Dj0QLHcYVBGC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشاورز بوشهری که با «قبر مارادونا» در حیاط خانه‌اش خبرساز شد!
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/95164" target="_blank">📅 13:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95163">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077ba9b0fe.mp4?token=U0Qg071dGlLBOhbs1Lf5XHdqCCe5qvAQKaOH0Mshb7clSSXpobMgm-fzTB2exrYXY2gfMMwXAQXHa0raE0Ir6WIGmAX5h-C7_yQP2kEqva6_Z4ZwDUGw1LFVPKCzihJ4d-2YAV09B_a3_wFD-1BqVuF_2c56oMfaF4uRaEDgr--_jma-CdBbpDZL3D7nsyn_nPbpcQEyhns0tVD4cOS7b0dH7kym9-piUqPLXjnjnBDaSgq5JH_hMW3mQ-4ez9vCd45t1lZ8afVWaf42bHaNIHJgn_CHhfDzmfa8evkuxpplM3fWZlQSyjW8OcsKjbg6QnT0SrefCtSsUVLV-Uk2Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077ba9b0fe.mp4?token=U0Qg071dGlLBOhbs1Lf5XHdqCCe5qvAQKaOH0Mshb7clSSXpobMgm-fzTB2exrYXY2gfMMwXAQXHa0raE0Ir6WIGmAX5h-C7_yQP2kEqva6_Z4ZwDUGw1LFVPKCzihJ4d-2YAV09B_a3_wFD-1BqVuF_2c56oMfaF4uRaEDgr--_jma-CdBbpDZL3D7nsyn_nPbpcQEyhns0tVD4cOS7b0dH7kym9-piUqPLXjnjnBDaSgq5JH_hMW3mQ-4ez9vCd45t1lZ8afVWaf42bHaNIHJgn_CHhfDzmfa8evkuxpplM3fWZlQSyjW8OcsKjbg6QnT0SrefCtSsUVLV-Uk2Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارا قبل گل داشتن شعار بیشرف بیشرف میدادن، موقع گل خوشحالی کردن، وقتی آفساید شد، بازم خوشحالی کردن! ایرانی جماعت همینقدر بلاتکلیفه و مشخص نیست با خودش چند چنده.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/95163" target="_blank">📅 12:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95162">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d2cfcb46.mp4?token=XK9CeCFQm8RcXQBII_-ZO2Vk7zMdJNYFxOTxTN_xp0050JKwZpaADvoDp7zz6HRNukoRgwclybWO161BRPq5pjptTAUROlFiMzB455nx8iRLpVUFKfT-WDvDYzmpq6vJkQYt2sRix6pABHBGeJEtfHrdreVhJCoFnsseqLJl9ySeoG4pqXFDdhmABu4dgdsVHa8mGy_DmYINIfexxeRRf_EbxEwD-eAym7xzwODQ2ukP3SnSPWOiKxrDffypjuq7NCp2wc2DROI9kaE62n1-IrVc29F_XI4_zEiw8L_Ys-gRa5xX9ULaBPsw070EW91DvUEE10CFguzpnsuSuYkG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d2cfcb46.mp4?token=XK9CeCFQm8RcXQBII_-ZO2Vk7zMdJNYFxOTxTN_xp0050JKwZpaADvoDp7zz6HRNukoRgwclybWO161BRPq5pjptTAUROlFiMzB455nx8iRLpVUFKfT-WDvDYzmpq6vJkQYt2sRix6pABHBGeJEtfHrdreVhJCoFnsseqLJl9ySeoG4pqXFDdhmABu4dgdsVHa8mGy_DmYINIfexxeRRf_EbxEwD-eAym7xzwODQ2ukP3SnSPWOiKxrDffypjuq7NCp2wc2DROI9kaE62n1-IrVc29F_XI4_zEiw8L_Ys-gRa5xX9ULaBPsw070EW91DvUEE10CFguzpnsuSuYkG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
هوادار ایرانی در بازی دیشب با بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/95162" target="_blank">📅 12:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95161">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca35f6f9c9.mp4?token=Ya0yBRtJnsdNp1PAiAM4Vm_983FRBHYHk8_Pp92b655sSGPoY5Y_0_Fb7cUBTMOmilKHlxM84HRvrAm0b-VQ6alKKWCKi2_TNLxvGWQtMjYcT5nNZ13qIsm23R_7oMH7n37b4M8uU6L0k5HTBbQS2cuWw2BszggrQp5UujNPixdu08XGaSI3LmqpBUnaIbSBZ37L4FOSLdNO_b0U9InhKtpGC7oQdPeH5P8ujpNfQ2EzJDmWxHpTirkpVhZplxZthk0uMlW1TOP1s-cJd2joJWnj9XGaPX3Ba-ag70ANPaDl41LiHEHY84ywZ41K_6Lwu9KgUAG94G6I2CguAV-53g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca35f6f9c9.mp4?token=Ya0yBRtJnsdNp1PAiAM4Vm_983FRBHYHk8_Pp92b655sSGPoY5Y_0_Fb7cUBTMOmilKHlxM84HRvrAm0b-VQ6alKKWCKi2_TNLxvGWQtMjYcT5nNZ13qIsm23R_7oMH7n37b4M8uU6L0k5HTBbQS2cuWw2BszggrQp5UujNPixdu08XGaSI3LmqpBUnaIbSBZ37L4FOSLdNO_b0U9InhKtpGC7oQdPeH5P8ujpNfQ2EzJDmWxHpTirkpVhZplxZthk0uMlW1TOP1s-cJd2joJWnj9XGaPX3Ba-ag70ANPaDl41LiHEHY84ywZ41K_6Lwu9KgUAG94G6I2CguAV-53g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
حتی اگه مسی هم باشیِ، دلیل نمیشه که به تراپی و مشاوره با روانشناس نیاز نداشته باشی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/95161" target="_blank">📅 12:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95160">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0820af51af.mp4?token=eN3SsgGlaiuRPp-SUl1aiowYqBLd1tYVaVeV_fflmZ4OCTf7XAmhdrwnfy9lOiwNgVKGbnfXicikB9qyDgG0JsqfSOySagZNYpTTRzGMiK357SmruVDk6u4zER54i6vQRVdJqEgUXYYG1i_vzLttuMDvSNwZ88MJPWMxFo2mfQwo3nIi8MmAiJVGFXnGxHvFd5dFLhd4jK1Tsr2QnNQSGV1F35Yvar7mGseNcs2qt3J-FEqct6oBIQPngPmGMvS6dHmCLixD1EvLh-BiCPukXhgTE_6VakZCY4uacO6O6DOJsPYo3GPVTUng_qFXYs4M_NVPSuk-SiWuoi7uL3aXQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0820af51af.mp4?token=eN3SsgGlaiuRPp-SUl1aiowYqBLd1tYVaVeV_fflmZ4OCTf7XAmhdrwnfy9lOiwNgVKGbnfXicikB9qyDgG0JsqfSOySagZNYpTTRzGMiK357SmruVDk6u4zER54i6vQRVdJqEgUXYYG1i_vzLttuMDvSNwZ88MJPWMxFo2mfQwo3nIi8MmAiJVGFXnGxHvFd5dFLhd4jK1Tsr2QnNQSGV1F35Yvar7mGseNcs2qt3J-FEqct6oBIQPngPmGMvS6dHmCLixD1EvLh-BiCPukXhgTE_6VakZCY4uacO6O6DOJsPYo3GPVTUng_qFXYs4M_NVPSuk-SiWuoi7uL3aXQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇦🇷
آرژانتینی‌ها آماده دومین‌بازی امشب تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/95160" target="_blank">📅 12:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95159">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn13V4waDQkAbgVL5yKByaF3VKUHu3cc6F3oZITlBOLpW95rsa6bH6Gxj_MKfxOb_B10zKSXmAD6c0LRDRPRUBUAb495M90hlSr95cMEym_HuGXzCikuRNEcaxHm4moLaobNdTYWTqHQxK7_KfZxEYjCr-YQY_pdBqxGJir6nnJ-RKsq10ZSaUp5l5RkamMujZn-ck0zxUOX-sIjIrf-CHDXGVEtKvD257UBb6SfdKN796GvyULETfaNUct7NoUnXZ-CrCYb0HEYNOodHLWscHIznJX9ezwyB4pNYJriqlRsaWsTSKKsGNdU4wVYoU299vZKXowlMs0FD5242U7d2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرناندو بولو |
جولیان آلوارز خودش را برای برداشتن قدم نهایی آماده می‌کند و در حال بررسی بهترین زمان برای اعلام رسمی علاقه‌اش به انتقال به بارسلونا است. داخل باشگاه انتظار دارند آلوارز به‌زودی با یک مصاحبه یا اظهارنظر، سکوتش را بشکند و همه را غافلگیر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/95159" target="_blank">📅 11:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95158">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">▶️
👀
وضعیت یکی‌از کافه‌های شاندیز دیشب سر صحنه گل مردود طارمی به بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/95158" target="_blank">📅 11:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95157">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuvqkLUsnLhjdlocMTaXyS0gJLPLmf3ctuKPy7Wjn6Hz-gNzurWmDi7Giey02yRLWIG0EkfBtwN_A8zjtV_DFebBzVf-SHdNZXSyCIBLGb_mEZcIK81ZcD7mmW-JziHWvafaZgzJN0zIFwAJss2z-wMP68ypRckjSrpOcxWa1zfw6reNgz8UAiFdoJ16I3QhmyM_2VXXP1YUnA4SuTSbl0KAIaTjV3Wabi-_shUKPXjTauzy0Oiqmmt1IXCRg9sYo4RpyICaB-o7_MPOWdZHf65Ynx27l1l_TJHh-3HiclHVWOrNVum6GAmbiKy8WEi4DuOWD0oarpYVeD4r2zuwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
مسابقه فرانسه
🇫🇷
عراق
🇮🇶
بیش از هر زمان دیگری به دلیل شرایط جوی سخت پیش‌بینی شده تهدید می‌شود!!!!!
⛈️
انتظار می‌رود از ساعت ۲:۰۰ بعدازظهر تا ۷:۰۰ عصر رعد و برق ببارد، در حالی که مسابقه ساعت ۵:۰۰ عصر به وقت محلی آغاز می‌شود.
و امروز در منطقه فیلادلفیا ایالات متحده انتظار می‌رود:
▪️
رعد و برق شدید
▪️
بادهای مخرب
▪️
رعد و برق و صاعقه شدید
▪️
احتمال وقوع گردباد محلی محدود
▪️
باران شدید که ممکن است باعث سیلاب ناگهانی شود
⚠️
طبق قوانین: در صورت مشاهده هرگونه صاعقه در فاصله ۱۳ کیلومتری از ورزشگاه، بازی حداقل به مدت ۳۰ دقیقه متوقف خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/95157" target="_blank">📅 11:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95156">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda9868a88.mp4?token=rVURW4KdXfBUznxvkA7GnwigImIY8VBbp_u_-RfCn9wQIDzNoOsHzrNFgTxFFFC7Rck9THT6DXQOE3V22Uw0VmG0azJ2M1xnAz45GA2C86Xh_ws6PC_1AvPUgTCTijpHQwUv5d3WjZo945tngE0TdMNAOmtpCa4WCXIoHrPedN2WVcGdDQ1I8RMBjYLk5VGE6F0qUmnWtHa4fOcUjT6KvE46zadCOFS7yTGtx0Ud1R_waM2bTgRjyp23wR4HdyLmqlBmc9KLpDQEdWzMNWtJK_o4-ke98DVqassElWw4OKZxNvoYF0sWyOKCn_c-zocK4eJ-MH9eZCFsPP9gv5xNnaZsjXvmuLmGuivofhn7NXDfRbnSrSpJqULStd0T5KTfZpzwXZEvS07RlMRzRp6Onh2OruJH07xyuIZo5akik52B4z_U3YpAQpjqSLlenZDzwcRX8UoJEbyUo08EX4qg7yzFQdhnlCSY11yQgfXeTFpAc8XZv1kqU-6FES1CIim8jppYwCzW1ulutho9WCsfPRdgB9kJ6NGrDHL8IiHe0qrImPQxtWxDGOxpMSfzjGHN0H6EoC0sOqC7vZztfsY3cfrS8U_r2VoD_fcdSHoEYWAg7p64NNwdnhWUrbpPdFbjRAyIH2i3N4XUNxNvtm99CVNGr9zoN2DVy99M7rp-NAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda9868a88.mp4?token=rVURW4KdXfBUznxvkA7GnwigImIY8VBbp_u_-RfCn9wQIDzNoOsHzrNFgTxFFFC7Rck9THT6DXQOE3V22Uw0VmG0azJ2M1xnAz45GA2C86Xh_ws6PC_1AvPUgTCTijpHQwUv5d3WjZo945tngE0TdMNAOmtpCa4WCXIoHrPedN2WVcGdDQ1I8RMBjYLk5VGE6F0qUmnWtHa4fOcUjT6KvE46zadCOFS7yTGtx0Ud1R_waM2bTgRjyp23wR4HdyLmqlBmc9KLpDQEdWzMNWtJK_o4-ke98DVqassElWw4OKZxNvoYF0sWyOKCn_c-zocK4eJ-MH9eZCFsPP9gv5xNnaZsjXvmuLmGuivofhn7NXDfRbnSrSpJqULStd0T5KTfZpzwXZEvS07RlMRzRp6Onh2OruJH07xyuIZo5akik52B4z_U3YpAQpjqSLlenZDzwcRX8UoJEbyUo08EX4qg7yzFQdhnlCSY11yQgfXeTFpAc8XZv1kqU-6FES1CIim8jppYwCzW1ulutho9WCsfPRdgB9kJ6NGrDHL8IiHe0qrImPQxtWxDGOxpMSfzjGHN0H6EoC0sOqC7vZztfsY3cfrS8U_r2VoD_fcdSHoEYWAg7p64NNwdnhWUrbpPdFbjRAyIH2i3N4XUNxNvtm99CVNGr9zoN2DVy99M7rp-NAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
ادای احترام به رشید مظاهری در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/95156" target="_blank">📅 11:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95155">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-o6S7iiLdA_8WA11wyVMNSD4wuQNriiLdFT1zxONCYf_FTAzlnvDMcKsaLAzXV6CLCiQdwj0rg77njbogu27kuTL9UWhFXM-PX0qIyLsPkOrupNZVCwGiqanfOwd6Uj0ZgQQShw_avV_fMQ5z2lfsQ0Per7sasnexF0PBq_m-7EExxiSdHh5NEi3oo3fLsDTZ2rUvvcpGJ6oYzKaoO-nF-3GD7MxNtXsMYYwD92KSwtzM_h6HxJ2IgYI9Wfi_BVe4CcVN4Zp7PsZ2gJKRPMCqsYZVuo2fzHSl7I_2Quyh1YVZ10x40c9dRYXVtHqME2XX92UBzVvPgi5nDcwuRfDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولو شیرا:
تاتنهام در حال آماده سازی پیشنهادی 100 میلیون یورویی برای ساندرو تونالی است
منچسترسیتی، آرسنال و منچستریونایتد نیز برای جذب هافبک ایتالیایی در رقابت هستند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/95155" target="_blank">📅 10:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95154">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f33346775.mp4?token=AQCAw4z782p_EMuI6mes7_DFN2_ao_dqeSlncHzuTneoH1YkTHBRnb3PE8C3W0oXsJPBkknb7d35eZa23JmzDFqISlIk6FarHDlfmF6xFlZ_LOKZXG_n3DXHZL4Z_3qfVusxnb3DbdASkBkTXkmHkzMDYWC0QB-2YX0UDdeODHArirMoSI1Cvi-izaEqIbhmWJa2VukjgK2HHWL7uLIkTi-93ykU8NMoFeMkfCvW82ek2X5795tAB2oR3YOozWTkrczjet9OIQxEqQj-qYa6dWoaorrVVBrZTDCjOSa2K6_i7rxBL8wI57y8xGbZZJvnh0IYn6iaebizyYSVhswkVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f33346775.mp4?token=AQCAw4z782p_EMuI6mes7_DFN2_ao_dqeSlncHzuTneoH1YkTHBRnb3PE8C3W0oXsJPBkknb7d35eZa23JmzDFqISlIk6FarHDlfmF6xFlZ_LOKZXG_n3DXHZL4Z_3qfVusxnb3DbdASkBkTXkmHkzMDYWC0QB-2YX0UDdeODHArirMoSI1Cvi-izaEqIbhmWJa2VukjgK2HHWL7uLIkTi-93ykU8NMoFeMkfCvW82ek2X5795tAB2oR3YOozWTkrczjet9OIQxEqQj-qYa6dWoaorrVVBrZTDCjOSa2K6_i7rxBL8wI57y8xGbZZJvnh0IYn6iaebizyYSVhswkVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
امباپه:
«از وقتی فوتبال رو شروع کردم، هر دوره بهمون می‌گفتن باید از یه روشی کپی‌برداری کنیم؛ یه زمان بازی مالکانه بارسلونا، یه زمان خط حمله سه نفره رئال مادرید، یه دوره هم شدت و قدرت بازی بایرن مونیخ، و حالا هم ازمون می‌خوان مثل پرس شدید پاریس سن ژرمن بازی کنیم، پس تیمی که میبره، همیشه الگوی واسه کل دنیای فوتبال میشه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/95154" target="_blank">📅 10:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95153">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8977a43dd2.mp4?token=DkNCb1LA7xt8lu2zom-8TdvRWjHv0X6OCijmAIYcmy8pwu3tdrLCmom3laFpbRKyt3xhzUm3WhsMgSSunkKS3FkRsynsrjhrX1sDNzCyux945ao7a-QoiFoRKLN26u-YdcOJPozttl4oTdu-cVaYpxi94baRwz50ivhL9hJYO-zsj9dqcOC7jWVbGzRw0x0lY2nzROlcM_WPyxTbzHYn3FRaj8NSHZ4dj_Braraev5z2DOFxJylYx5jqdo1SwiDVOaJ6DdiSbM9E904Z47TE5hfJ3Nqz7b7fkiQSqtdwbgmjRrAKXsa7FfMXjCJYUaY3-Vk-HBUc1ZZaxGwKsah1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8977a43dd2.mp4?token=DkNCb1LA7xt8lu2zom-8TdvRWjHv0X6OCijmAIYcmy8pwu3tdrLCmom3laFpbRKyt3xhzUm3WhsMgSSunkKS3FkRsynsrjhrX1sDNzCyux945ao7a-QoiFoRKLN26u-YdcOJPozttl4oTdu-cVaYpxi94baRwz50ivhL9hJYO-zsj9dqcOC7jWVbGzRw0x0lY2nzROlcM_WPyxTbzHYn3FRaj8NSHZ4dj_Braraev5z2DOFxJylYx5jqdo1SwiDVOaJ6DdiSbM9E904Z47TE5hfJ3Nqz7b7fkiQSqtdwbgmjRrAKXsa7FfMXjCJYUaY3-Vk-HBUc1ZZaxGwKsah1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
شوخی‌های جنسی دو مجری خانوم با نیمار در ویژه برنامه جام‌جهانی یکی از پلتفرم‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/95153" target="_blank">📅 10:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95152">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f153f9102b.mp4?token=UzqjA0Xi6KlvNPWU_bWpLEYC8Henp0SMOg6cPi5_pbRN_LcaXMWDaasw_JfPWVRk6E-ZGovg4UGzYlHusWJqCOiwoLAMnfaCVfpeJqfflhYXc_nwa2OEZUNIcDDwWChMoDRFRAvHo762qmsBxYRzw56B3eKCUPuNa09eELV9HYhPe1lU118bxuWuC1knSYA6n1eNOzeRpdaR6Y69MUPoyrbTW8u-LK-OlmKamfH36weV2yPGuZMCt6r2fjEnX9LErEyMCVm3ZKJUzbQbQHh4lX6rWqCgRUsBpYE0z9KH0KDMZYoUCPB7yb37GzhYOUd9usqaufJ2sqUxiQjM0QW8Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f153f9102b.mp4?token=UzqjA0Xi6KlvNPWU_bWpLEYC8Henp0SMOg6cPi5_pbRN_LcaXMWDaasw_JfPWVRk6E-ZGovg4UGzYlHusWJqCOiwoLAMnfaCVfpeJqfflhYXc_nwa2OEZUNIcDDwWChMoDRFRAvHo762qmsBxYRzw56B3eKCUPuNa09eELV9HYhPe1lU118bxuWuC1knSYA6n1eNOzeRpdaR6Y69MUPoyrbTW8u-LK-OlmKamfH36weV2yPGuZMCt6r2fjEnX9LErEyMCVm3ZKJUzbQbQHh4lX6rWqCgRUsBpYE0z9KH0KDMZYoUCPB7yb37GzhYOUd9usqaufJ2sqUxiQjM0QW8Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇲🇽
مکزیکی‌ها دیگه خیلی تو جام‌جهانی راحت شدن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/Futball180TV/95152" target="_blank">📅 10:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95151">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226f9c8160.mp4?token=WekTErSrM819z41lcQPFR12qftlQlp9MzF7Sw24d3Yi46IZJ5AbhnWt6k8tIu5bDvQc1a8LOKV50Keg7UkH1N-5Vues6hegUkM6HV5CY1U6F2ajDyvbYnnSI6RYyP-tXY4W_HrZlrNORDVZIZ8EJkfVEZFKA44Cf1IgBi5Y1JZNdRTjuc68LbklmzsvZM5AlseMvYjVycWmKVf39sPz60WbfCdo9KyecwGR_scbwsv62ITXYDKtBVa53oK6UtsRhenq_A2Wb24Un6ANEymDzO3N3_13tpwOBzQzOEAAUk-Z1twPab_9hQmtI1oDhcnidND2DVJk1biD4DeAgSRUo5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226f9c8160.mp4?token=WekTErSrM819z41lcQPFR12qftlQlp9MzF7Sw24d3Yi46IZJ5AbhnWt6k8tIu5bDvQc1a8LOKV50Keg7UkH1N-5Vues6hegUkM6HV5CY1U6F2ajDyvbYnnSI6RYyP-tXY4W_HrZlrNORDVZIZ8EJkfVEZFKA44Cf1IgBi5Y1JZNdRTjuc68LbklmzsvZM5AlseMvYjVycWmKVf39sPz60WbfCdo9KyecwGR_scbwsv62ITXYDKtBVa53oK6UtsRhenq_A2Wb24Un6ANEymDzO3N3_13tpwOBzQzOEAAUk-Z1twPab_9hQmtI1oDhcnidND2DVJk1biD4DeAgSRUo5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
👀
🏆
هوادار ژاپنی بعد گلبارون تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/Futball180TV/95151" target="_blank">📅 09:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95150">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZJA9QiW-AFjAu5qsAanqGwDHuTF1x-GOssY8Y5QZzfuPRiOFp2oK5tNs0bV7Pbi2o_aFW68d6FiRudVmaAZcS7cGwk9yJX1889DbMnYX7LlaSK6652Cd7gls1gYF6MvEsg5jh6AYMyGKh0YcMEc59-6hHmndMZbTFnn2I0-DHlSIkwRKDzM5CksruV2q71k60zGCJ6TU4RI-9wr13xtA2k9FBFuxB730WQ_9brEvm2F_UMJWXH-3tma229ZArp8SWGjPbxvzgQiS6OLdlYaZ6u9Bm3TMcFQV3YPqpMIzu-JI9FMGFJBiL5xgI5VqiYvcWpi-EwJFIJsHWb1y7BW8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
پیمان‌معادی دیشب در استادیوم لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/Futball180TV/95150" target="_blank">📅 09:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95148">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQvzjK81RzXPae_zoHUnpQ90GGtNw3Ko3dF9cXrL6c6hNFhSzaZArNCix3v-D4WbpJ2vXoBzZF7rOcGh_1Stdk7KkWtGi5B02dbqNfVo1WyNmFwLmIT1E37jKGBd2G5vsmcnqZuxNtcl00y3xW69xY7YEvId_g44sOFDqf1IJnD_AmrjXlHliteQiIiIoJsMFXSuths-RaLoa3J4xyrsaO32jf-SDCylec2ZebXMJdkFKbchyvhOgBzmfW_63PQ13ODBkXoq8wMmc_-mHA_8c6EUjfJE0_cafZZfwRZoLnhgtpuA-6yMjdw4QqTYMi7lz_53ipn6Lma4fFKGaLzWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👻
به امید صعود تیم مردمی سوئد
🔥
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/95148" target="_blank">📅 09:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95147">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3243a4ebbc.mp4?token=lKDj4iZQzIv_kH_rY_g9YRM69XEevY_5ak0yoAxKMjZWpPt8kHxBF_NmPBHVzA-WbNKGUrKbW7EnCW_2pmYhq9HpfuucUU_MBFRdIa5bTL03aix9m2MUpQKrjEaumxoKb-HP-DGAjXcck9Zs4FbFhl8rU0bvptbRD2V3HQB5RJ7FWQByR1eC9aVR7PJHuif2tykmamXLOPyTaUUkSlBjPxluUZVJnU6hZUfsVUlv0E2QAL015jB6_QOOdba_ZpB_U5W63-VM57v_vuV_ZX1MesavhHVNROrZSdjQdt2Hq3_rqfTXnFs2FeqLe_9GKiGnMuCIRLRfOSQ1Wqj4nmHyfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3243a4ebbc.mp4?token=lKDj4iZQzIv_kH_rY_g9YRM69XEevY_5ak0yoAxKMjZWpPt8kHxBF_NmPBHVzA-WbNKGUrKbW7EnCW_2pmYhq9HpfuucUU_MBFRdIa5bTL03aix9m2MUpQKrjEaumxoKb-HP-DGAjXcck9Zs4FbFhl8rU0bvptbRD2V3HQB5RJ7FWQByR1eC9aVR7PJHuif2tykmamXLOPyTaUUkSlBjPxluUZVJnU6hZUfsVUlv0E2QAL015jB6_QOOdba_ZpB_U5W63-VM57v_vuV_ZX1MesavhHVNROrZSdjQdt2Hq3_rqfTXnFs2FeqLe_9GKiGnMuCIRLRfOSQ1Wqj4nmHyfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
واکنش صادقانه یه هوادار به بازی دیشب:
❌
❌
❌
❌
❌
صدا کمممم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/95147" target="_blank">📅 08:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95146">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPsSSu4O0eWH9QqG4Ae8vsI5nupi4bCRoU1nyjGRSA9CH_Dyl3I9pAE6Ukrawk5PfTcgKad2BIs9aS-ywviwx01_NvQqLvz2R9wbwzsLvxPSQmIRxxDeeeZAjG3cYuKppPzjKJuj_-4JUAzGazCFPnHgAcE8YPhYB5F8PNNBepxDeBLu1nOYTUltlKj4I9rSvzdvtTdZO3cOuLHdfF8xTzzTHqRe0JCXphLFPGx8ZKWJHsI8FvVv7iBACuwD9hRmDQk8TjIq9_8nAyagsbKDtNGsqtQ8GfmsJ1R1ADCZF8A9CBGWJ-dcMyQyXYnItmYUnbd23BhaE1NyF9D7skPkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇳🇿
🏆
🇪🇬
اسطوره‌صلاح بهترین بازیکن دیدار مصر و نیوزیلند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/Futball180TV/95146" target="_blank">📅 06:47 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
