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
<img src="https://cdn5.telesco.pe/file/s8SpB_CmshFs-nxdSTGTlUtibTgEGp6YFOcJpmP1o4qdKfImRNTy7T3IgbK1GHtfZxil2oCx34oWUnNhUsJzYD-SxEMdyTmh2Vjqseoy29tjsXtDRMA3aYjQiAXa6ctKkEn5jaKUThwZQ0lzYlZktxVyZoGOCaQ49NJq4fSrRfv8HIXtDZxvkmoRdtWmw0c4iHYjFZDCRcar0IVwZAc3Ak_llMIk6gMTKk3UR4c5KWFug2S8yUFO5-eiBzawdDNVtWhDusO27vReKX_ztbfhEyHzeoaWLTUk4DyopGmjds5SQoSCgKUOn1FNI4GDWryX9ixllNN3aH2oZVV9iIomDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 415K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 16:28:12</div>
<hr>

<div class="tg-post" id="msg-106356">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l12wq_pJ-fIBGn6FdqpK-rVirHV0KxIgn_R5GS4NgncM9VERTUiHwlADekYQ0J1DKtQCy33dfm5UUqErEKPq2K-uaqJnwmZlm2wfFEVjzimmeyETMLdxvy8DpMFcfbwSQ2ugOPjQCNUhC-UNi1k_dWMT_MHjIOkX7KXj3ODQdkEw2VTuumvCtphCJoKK-dlceRU4BfFPnKNJ_eJ7VYN6EMDaUQnu8D_YFhpDdRraIi4oJiBq6rA6jnf9DTJMd2Y17Z4g5i9ch-2y8w95oy5wrqJe9_Qcz47aEJYFT0c8t3hlJrKpKOJXfr8x5J_YSjFHXkudTfzWAGHyu5ZtTAA4vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇶🇦
السد قطر پس از هجوم هواداران پرسپولیس کامنت‌های پیجش رو بست تا درباره یاسر‌آسانی مطلبی کامنت نشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/106356" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106355">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfgMUW4bzw3Dk9eEugH7Yr4-nVd0Ia_SRsn7YfwSctoxd-7lZMCpb_-LAyjzU9kKyuVP69YeG4hKFxj05XlH4hk7A5GCN1PXF3BDVffoEILnCpRZ25W1Bb5cGCU7YmkB1MQh4romK2vQoq2oChLn6gczeiO-CRgIVDUCvleiO0jMw1cqkix05PUNW-7arZlQt1OwzMfm7D0pMdEgqiSjsSeZvZYCrQEFTaO82-SlC7a0HQMpfMNo3Yw7jgEQzoJ6b0oMutTxZV7RswnL5wqkZ5tsT3FU1LmQCmEbGMSz03VnMGnBY0t7GzlTLypG-RrWcr-Ojad9OMW0dFSQw6samQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق معمول ده بازی گذشته، مقابل والیبال ژاپن شکست خوردیم و سهمیه مستقیم المپیک به این کشور رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/106355" target="_blank">📅 15:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106354">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری داماد سابق علی‌پروین بعد از 22 سال؛ آرش فرزین: رهبری فرد و باندش، سرمربی پرسپولیس را کله پا کردند!
بیست و دو سال از روزی که آرش فرزین حرف های راینر زوبل آلمانی را ناقص ترجمه کرد، میگذرد و یعد از این همه مدت، حالا داماد سابق پروین، پشت پرده آن روز را افشا می کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/Futball180TV/106354" target="_blank">📅 15:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106353">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1b2c19a26.mp4?token=pE2FNaH7_Z7u8OU76i922g34h40xrQK_32FCfDlhLokGzFHYQ1YYVZWFiRIaDp2QLcB3TI_kUdR_zOrB8KXtvXjXPZ-a7mzUJlwl7VMidzfOvi2TGcDg_eYBV3ZRmvZJfgAc_ybwd-U92Zz5hib9DMIv9nHWPrDbGjsqLtyMEC5I7H4UcrtNQzV6I6dDXQVu1BJ1YRIn3eCOLgz2YdUEx4Da7IR1VBG3Szm4LZDr76DPH5OvTuGU5SqSGJKM2WxTcPWMZPMOswQIm2-PBfMD-OlSIWWzFY2N6c-QzLNT9vwjTd8kHuGLE2b_7To0422NQ8DM5XhT4jaMKIQpHyphr0dG-8VYmRHoD3CEGbHAvJ7DEzdmL_EO25bnmbLQbGiZYwPuYvTe8mN61ZOMINNvJFOyKhEX-elFu6qOxJDHet6-WFXqxS8hOVTy0NwXGCnjIoZg8MhqCgeGx4q4stSa2Kym_rqCCbAANs6LdwbmZYvPWfTN8TYL--_jIWf5iFGj-GRX6hSPQ4baX3Fauwejsjg1hsCtsA-XR_MaoN3-8tZw9qPT0bCj_q63jAzlGf-y1IQK6LoDKiI1_FpPsBHhyl-vi7VgNSWE0VrozUc7swLELi8Y1cD2JVCIkcvHcnZRsjhkDL2lNhr6dRZ_sS1y7_5EOSNEwj_HvF96q4Hz-2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1b2c19a26.mp4?token=pE2FNaH7_Z7u8OU76i922g34h40xrQK_32FCfDlhLokGzFHYQ1YYVZWFiRIaDp2QLcB3TI_kUdR_zOrB8KXtvXjXPZ-a7mzUJlwl7VMidzfOvi2TGcDg_eYBV3ZRmvZJfgAc_ybwd-U92Zz5hib9DMIv9nHWPrDbGjsqLtyMEC5I7H4UcrtNQzV6I6dDXQVu1BJ1YRIn3eCOLgz2YdUEx4Da7IR1VBG3Szm4LZDr76DPH5OvTuGU5SqSGJKM2WxTcPWMZPMOswQIm2-PBfMD-OlSIWWzFY2N6c-QzLNT9vwjTd8kHuGLE2b_7To0422NQ8DM5XhT4jaMKIQpHyphr0dG-8VYmRHoD3CEGbHAvJ7DEzdmL_EO25bnmbLQbGiZYwPuYvTe8mN61ZOMINNvJFOyKhEX-elFu6qOxJDHet6-WFXqxS8hOVTy0NwXGCnjIoZg8MhqCgeGx4q4stSa2Kym_rqCCbAANs6LdwbmZYvPWfTN8TYL--_jIWf5iFGj-GRX6hSPQ4baX3Fauwejsjg1hsCtsA-XR_MaoN3-8tZw9qPT0bCj_q63jAzlGf-y1IQK6LoDKiI1_FpPsBHhyl-vi7VgNSWE0VrozUc7swLELi8Y1cD2JVCIkcvHcnZRsjhkDL2lNhr6dRZ_sS1y7_5EOSNEwj_HvF96q4Hz-2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
ویدیو وایرال‌شده از آغوش گرم دو بانوی ایرانی در جشنواره ونیز ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/Futball180TV/106353" target="_blank">📅 15:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106352">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ecf94960.mp4?token=O2reTrM7AV-qMfW_RZSSnOdmmvRJuyG0AWVBo8qaUScusLd-J3_MqnY4kRkSaA5Ewggr3jWOnXBTnJ36uEnvsDaUrIfiLOt1P47pBdciHTcBqk2Aj6DJ1rmHE6nPty0vnUiZcQANROXwSiox-YSswG0HoiFZpSmDzthOLRHCe2uPhirzAzPig_qigbYHZUV59tuhmMwG4M_rE0xigwT8Bg4RoZtZFTcgkO6Mf4mLU64Sm3p_e8w7hDbmqWGe8IfQ1NkDHgv16oCs6nJntTGjsNGBSVP84isCXkOVX1RMDhE8jqxb4SHnP9h3iZuOl_OzwXG_69l95cJ8msdOeT_ykQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ecf94960.mp4?token=O2reTrM7AV-qMfW_RZSSnOdmmvRJuyG0AWVBo8qaUScusLd-J3_MqnY4kRkSaA5Ewggr3jWOnXBTnJ36uEnvsDaUrIfiLOt1P47pBdciHTcBqk2Aj6DJ1rmHE6nPty0vnUiZcQANROXwSiox-YSswG0HoiFZpSmDzthOLRHCe2uPhirzAzPig_qigbYHZUV59tuhmMwG4M_rE0xigwT8Bg4RoZtZFTcgkO6Mf4mLU64Sm3p_e8w7hDbmqWGe8IfQ1NkDHgv16oCs6nJntTGjsNGBSVP84isCXkOVX1RMDhE8jqxb4SHnP9h3iZuOl_OzwXG_69l95cJ8msdOeT_ykQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبت‌های شنیدنی سعید دقیقی درباره تفاوت سبک بازی اوستون اورونوف و تیوی‌بیفوما دو بازیکن پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/Futball180TV/106352" target="_blank">📅 14:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106351">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbtjXi5EZ501AFfylB1aikgC87Z-9VYYsLa1XNhGpnQRHjUvYd-UHVPhjvm-pzfcqfDRIkpgnTB4XEgWz5Am4RqGy0-GLdtNHULufGUoc-qGsq6Dj0xSp3rgK6QwWfzlD-jjh_4jG7IL_fG4rzeP0EE87GxEBkopmr931c0mgyZHrIamgSw_P8rUYimROwqzo-vR90pacI_cUOGQu2FIuKRLb05WYCY29nlFWrtrmwuVjYY-RhrMpHQFhxoqLG75jUYynIBMIcyMwwax_Klr9IsloZH-ChxUKeCjguqPOZvZyH5ncYVEQOyTUQbLRlhfdloOaltnQXnHKo_pmk3jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
هوادارای التعاون دیشب برای اینکه برن روی مخ روبن نوس، بازیکن الهلال، اسم دیوگو ژوتا رو که دوست نزدیک نوس هم بود فریاد می‌زدن.
✔️
👏
نوس هم بعد از بازی درباره این کار مزخرف هوادارای التعاون فقط گفت «امیدوارم حداقل بعدش نرن نماز بخونن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106351" target="_blank">📅 14:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106350">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2eae5e40.mp4?token=Hd4FLTet57xF0tK8lCqMq0eVDqAWZPv5ZCqeaRbsKdS8nsVs8WAKHhVKTosm0S_hdqfAJIOZsR_9ibHyypo88pYHgmRCsGRCey3sg9A-LkkoWNZLkHlGnvE0nPbL45M-A4ZiaaaTOhjGf9NOwCRdYsM7IMukDqXRp-BE-Qkz_rJpPAVbL52S--QBLexn6U00v0zltvtW5tW75j_1Tpu5P5_ZjwBKYyYK_0a_iY5y6EC0XVWk4gnidZoVCBY5e7OwS4Jx-KmSWwiWUQ_tgJGh9ormxTfKzsMUx3RScRQ2vwkTaImzNY82kPis0D2df1D2SnIDUxVTqvu_V_CHlXarRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2eae5e40.mp4?token=Hd4FLTet57xF0tK8lCqMq0eVDqAWZPv5ZCqeaRbsKdS8nsVs8WAKHhVKTosm0S_hdqfAJIOZsR_9ibHyypo88pYHgmRCsGRCey3sg9A-LkkoWNZLkHlGnvE0nPbL45M-A4ZiaaaTOhjGf9NOwCRdYsM7IMukDqXRp-BE-Qkz_rJpPAVbL52S--QBLexn6U00v0zltvtW5tW75j_1Tpu5P5_ZjwBKYyYK_0a_iY5y6EC0XVWk4gnidZoVCBY5e7OwS4Jx-KmSWwiWUQ_tgJGh9ormxTfKzsMUx3RScRQ2vwkTaImzNY82kPis0D2df1D2SnIDUxVTqvu_V_CHlXarRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدشانسی‌های لیونل‌مسی برای اینترمیامی در بازی بامداد امروز تیمش مقابل نشویل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106350" target="_blank">📅 14:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106349">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6ed3f485.mp4?token=cEHyDPTHR6SwJ2hjSnf2EaKmMPBZY4CkI-5blwuTIotHByLp7zSQF6w13qgnntcIj43tP2UHWVzSl_ubKU_UVLoPMDN42BpSqbOHufogLHqRbfveGNTkiNYYZiOrhgDn3LBFzbPsAvgH2IiwttnWCsq3YLKHRn6K6v_DIv3L1VZfYRx8xgrX15ZGk01jNPcdqRGtIMmNUxikPCU4G7UepUuPp9D6FpoxCfggvQvWbr5wqw8cSWUULOyX_hKxGUPQPynhgcUO5OxPuauc1vbS8n_pUsFgUo-47afRwCz7HbidZZhyII7-E4KQwKz40d6CJFFDZPfpjutgXjLBHjofcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6ed3f485.mp4?token=cEHyDPTHR6SwJ2hjSnf2EaKmMPBZY4CkI-5blwuTIotHByLp7zSQF6w13qgnntcIj43tP2UHWVzSl_ubKU_UVLoPMDN42BpSqbOHufogLHqRbfveGNTkiNYYZiOrhgDn3LBFzbPsAvgH2IiwttnWCsq3YLKHRn6K6v_DIv3L1VZfYRx8xgrX15ZGk01jNPcdqRGtIMmNUxikPCU4G7UepUuPp9D6FpoxCfggvQvWbr5wqw8cSWUULOyX_hKxGUPQPynhgcUO5OxPuauc1vbS8n_pUsFgUo-47afRwCz7HbidZZhyII7-E4KQwKz40d6CJFFDZPfpjutgXjLBHjofcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یک‌شهر و دو تیم برجسته؛ به دربی جذاب شهر منچستر خوش‌آمدید؛ امشب ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106349" target="_blank">📅 13:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106347">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kfz_EmqPDBwHVe3MkJoq-k8DdQyH2O4SXWTCjtS3LJH5fHkU6sRflvWBnnmHtssk_MWGFDapaDBMJplArDy-S7pauHbuosgN1IVp_swLf_l8wqigi_o4Kh4EGIq-tm2gc7ODsWgrk_qUWC1XORWsqr2Ar7-oj-IhCxfGtMDuAInumxxqXMXxwpGPba73Vb0VjPLs7f3gXWBhx1kpK_maJoY665RxMxyHD36TUyeTGoNZdQnMJZOeJM6fQtbu2e4MlbOKwr2OaB6oBGmRdZ7G1co_JO31f9InaDDePvULhxdsnsXg1m61QQIpvOAX5Df1ufQVxXE2mJM_nZ4GMcKr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qqn6Tts0RyMeR-PKWuTt2RJSfeegebNBLT58YQhCICSrObmP8wb71WKklM5XAVuReAz8OSdd2U14IW_3iPsCwir-KXPdHyr9s-MQE__hVL_aPV3P7BG1QgjtRUKFgI-UgtocMz6xFPMQrJfh5MIVMJZ2zIJpJIvbH2yvu5UikYZ-IhTFFfl-rBRxywlg1TyxsJEycKCCsQLvdMleOdc5NY4u0Q7Nx88jXOx6Dm-3_5fx4Zj4p3fD0nMeu0Cl3IBnUNqu5mNFf7_4zId09RPsF6dWCANCnR-MmjjQN1k4BJ78x61Le1bh1QKJPXBXKUEsFE6eti9hQcUsjErsYPsqSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
بر اساس اسناد منتشرشده، فرشید میرشکرایی، مشاور عالی و منصوب جدید تاجرنیا، پیش‌تر در پرونده‌ای شخصی با موضوع «خیانت در امانت» به یک سال حبس تعزیری محکوم شده است.
حالا این سؤال مطرح است که چرا پیش از سپردن مسئولیت و منابع مالی باشگاه استقلال، استعلام‌های لازم درباره سوابق افراد انجام نشده است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/106347" target="_blank">📅 13:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106346">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLfYg7S4hKpqYRRyPzrBjb9-st2g0K6qxpGSH2LAFZ0R00UNzCwG-qCHXNe9w3dycwyQQocY5Lxv27Cdn5XnD4bXkJxQ6c1tz232GsMMcM3533AEFvmKu8A0rSHXNMdM62QkSmfCVEd9H7ZuKaoNvkegiJqKpzOuA49FHrNc_1UNAoqbJ9BmrT_2dfRkg4nOyVQI49jR8z6dptDxOJFQoa2AhKKHfW9UBYv24wXGfOskTJkCBOOEc_NBkvvglaINa8OghM7Twyo_KthSNMi4ob-2Lv_h2FExC3Cch25JrhYLYrzmRx60aYDy5C6J1Ld_nqtzn5TfDw7tvjl25-2RXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
فینال قهرمانی آسیا 2026؛
🏐
🇮🇷
ترکیب تیم ملی والیبال ایران مقابل ژاپن
؛ ساعت 14:00
🔥
قهرمان این مسابقه سهمیه المپیک میگیره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106346" target="_blank">📅 13:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106345">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddad7e35de.mp4?token=jKRA-WTdINLeigEDRuhwsEcvAYREPiuEU_5pIpQwwMJW7-U2G7jNaD27X2ajwQeNw3OFNmUbGgEt-Ihe9CRGszsMJ2u6CXaJPmVGIyqidePoiOab6b74gzkXmMcOlBt5aNKaWNFKnYwJflk0d2ilTpfkSWvMkfY6tg49k5VP_U6dpa5Zr1-SFO81MNgVWXBGC5vH_H9bR1Tpe7iYJqvCgEPRCQD3lseRihC1F4UCNZGR_L0pqRpfCYdF2tV6DMAsYpwzFwGRTwKS5PhUe2SCiKQFDzcuExEtKisZ-_UIoukNhJKEnMClHRZJ8swroMIyKt_5viQZVamOKbFoDAUhpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddad7e35de.mp4?token=jKRA-WTdINLeigEDRuhwsEcvAYREPiuEU_5pIpQwwMJW7-U2G7jNaD27X2ajwQeNw3OFNmUbGgEt-Ihe9CRGszsMJ2u6CXaJPmVGIyqidePoiOab6b74gzkXmMcOlBt5aNKaWNFKnYwJflk0d2ilTpfkSWvMkfY6tg49k5VP_U6dpa5Zr1-SFO81MNgVWXBGC5vH_H9bR1Tpe7iYJqvCgEPRCQD3lseRihC1F4UCNZGR_L0pqRpfCYdF2tV6DMAsYpwzFwGRTwKS5PhUe2SCiKQFDzcuExEtKisZ-_UIoukNhJKEnMClHRZJ8swroMIyKt_5viQZVamOKbFoDAUhpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
دلجویی آیسان‌اسلامی از هانی‌رامبد پس از مصاحبه اخیر هادی‌چوپان علیه این مربی برجسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106345" target="_blank">📅 13:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106344">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0dd00f3a7.mp4?token=Z2onH3RWCs2Q4L3YjPjFAxo1NFRgXKxxmbdncrokW55CMS_oZr-cIEJSt8IOJCXCKsYfuo7C7hKI6YI7oLMv4r6WDBqz-_iF6zuGYY4N5rH9OqvREHUsECaYR5L8MPeL1DfYSS0AUlF-JleoZkYCswruhbF4Emh9goL-AApiBRRmSDLCtkQlL_19CeiA33hTy3t9wR-ZS4oy06NAYWpZgdDdt3dXnQpo2TFvGRiLYB3XJQTDKlzYtRRc1qX-Pt1GDyA0bKW4jOUu1vxX6cjNbTWFXjKFDKeIGnwgquaKFq1Jfg8sJ1ofwFawbfcnD0bLabGG96yEuoAewFYcSg_lGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0dd00f3a7.mp4?token=Z2onH3RWCs2Q4L3YjPjFAxo1NFRgXKxxmbdncrokW55CMS_oZr-cIEJSt8IOJCXCKsYfuo7C7hKI6YI7oLMv4r6WDBqz-_iF6zuGYY4N5rH9OqvREHUsECaYR5L8MPeL1DfYSS0AUlF-JleoZkYCswruhbF4Emh9goL-AApiBRRmSDLCtkQlL_19CeiA33hTy3t9wR-ZS4oy06NAYWpZgdDdt3dXnQpo2TFvGRiLYB3XJQTDKlzYtRRc1qX-Pt1GDyA0bKW4jOUu1vxX6cjNbTWFXjKFDKeIGnwgquaKFq1Jfg8sJ1ofwFawbfcnD0bLabGG96yEuoAewFYcSg_lGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
برخورد ناخواسته علی‌حاجی‌پور بازیکن تیم‌ملی والیبال و یک هوادار ژاپنی در حاشیه مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106344" target="_blank">📅 13:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106343">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUVLMX-pmu-unzU2oE1JsA-9x1K5jg9oyKqhZboKKIA39gGLPq8Ofe1PJx1eiZMtlKg_85Bou_0ObzR4jQGQnrZBykMyEKN6olrdWWxJ2HJa2J4rrmpZ6oO2O29xaQyJ9hr6ZSRE66d-AAfLBn_nphDNkkUg67d0q84Oyq4QkjaAHFfm6Ns8hk6Lc74_spZK9wXv9CTZ8XnevGCPq8qerSDjYz8Rb-bOcedAa7zUaTiTr0yDfa0wuEl-H8Rdc0Kln8rCZjDd8VsmeDz8FjkwjeCKuOnSVBrsBa2aUpHj3V0Sm7LP_XnbzphF358kS0U9Jno9GOonwe3jcyYWuq3xPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
‏
📊
نتایج دربی منچستر در طول تاریخ:
‏
🏴󠁧󠁢󠁥󠁮󠁧󠁿
81 برد برای منچستر یونایتد
‏
🤝
54 تساوی.
‏
🏴󠁧󠁢󠁥󠁮󠁧󠁿
63 برد برای منچستر سیتی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106343" target="_blank">📅 12:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106342">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siCCvRBTJz27HNH9lutmEXgSD3WKz0tdF9tnlHJNBQ2oCI9_Ec5VDeJfIqGld1JrJvNUUZETIfjDt2saXznjn7PclM4yVa-Hlik2rkGTR2LFY9L50md3WYn1vyc6y-XCUc182B4uNv-yNpzZ0NHESrvt_3acPiuNe7T0EPFQrPNpKfT9e5OlYAa-0Htx3FoZvgJfJmZXsbqSvvufcb3aAeIbMdafMQI6GJdGb1XXf2vJsK4-8hknVd7AQKny8kNLRW_zE-LoY071-BgWTHd1NuMkBjGyS8gjiJ9GlCCywi42aiMpMT2slnW4rKKXjKnZs58wypvfKEs8buXVJk4Z8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار یاسر‌آسانی در رقابت‌های آسیایی:
🟣
آمار آسانی با گوانگجو در لیگ نخبگان:
🏟
۱۰ بازی
⚽️
۹ گل
🅰️
۱ پاس‌گل
🔵
آمار آسانی با استقلال در لیگ قهرمانان آسیا ۲:
🏟
۸ بازی
⚽️
۴ گل
🅰️
۱ پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/106342" target="_blank">📅 12:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106341">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3XwrH_TfICVyQwlALcuBIPqHRwsk7u2tURNwt6YZGKy1dR4fXy0_FkFT6MK7-EXfaiifj5QyBH6BmxSARObpQ_r9uKWuWGp_tdiCnnqL_6G97gXRdNyTjQYaJDITcKWXE0OCTps41pGcZT9XQTkc1A18K7oWhR8bueIf61OKckFY2PSfmVeFCl_BiUu-Mmjidy8FNtTZl2ebfSY4q8w40d3ctymZ5WHPqV8soH_XuQ6xvhW9W6wYrY4Vc3pbt9vzF9TgFKZHpRT3kNBo14WzhSBVFWpoVWvebSnj3X04NQ_IYgxldamjITZEEF3YlVtIGgYXGUGmG_hbtqq1r9Rlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇪🇸
خولیان‌آلوارز از لیست اتلتیکومادرید برای بازی با رئال سوسیه‌داد خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106341" target="_blank">📅 12:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106340">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2faf6374.mp4?token=Qd0MG9aGkmVswI8wuROK8RobuQ4_edi5z47d2Vcjh2tBj0IQuCrT0vH1IqGv0lkusVYfC-9JmEEv4-3lq9n3e2cxJfE1ImQDkSgVVWzdPvtvQk4yRchN9B1pu5VYQCjzZ5ox9ijjSmM-7bk7BnyZAVz914vlFL_qfTDVXiSfBTvRCmP1s3zgKW9r1mhBkxTw5qu9U42u2IFy4hriHd15L3xd8gMbujFypF8IFGrcU6lROA8Vb7ty8VoPWpnq6Sqh9Fuxrsv2SEZcn8x4rkjs_v6Q1oaB0vOCnVnHX5S7StdCFahwOc_UAqg7Cqt_ZwVfMNwAQggpA1aLureLqNPh2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2faf6374.mp4?token=Qd0MG9aGkmVswI8wuROK8RobuQ4_edi5z47d2Vcjh2tBj0IQuCrT0vH1IqGv0lkusVYfC-9JmEEv4-3lq9n3e2cxJfE1ImQDkSgVVWzdPvtvQk4yRchN9B1pu5VYQCjzZ5ox9ijjSmM-7bk7BnyZAVz914vlFL_qfTDVXiSfBTvRCmP1s3zgKW9r1mhBkxTw5qu9U42u2IFy4hriHd15L3xd8gMbujFypF8IFGrcU6lROA8Vb7ty8VoPWpnq6Sqh9Fuxrsv2SEZcn8x4rkjs_v6Q1oaB0vOCnVnHX5S7StdCFahwOc_UAqg7Cqt_ZwVfMNwAQggpA1aLureLqNPh2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کاش دوباره برمیگشتیم به این‌ایام شیرین...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106340" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106339">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106339" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106339" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106338">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9yDLyTFd680Q_28z4R9MJPRSsuVDmjfbhnxaf1pZhgLxftMvuK00Us7a30beX6L4POdZ_FvJ8CnXOnfH_LDcizak9ZgPcuQfwi6jmtZkFLA6To9gJCbJzydcRyMBpV8jLFwI8-eQuJl0UK7U5lWwB7G7ciwbhqrOkI0BNAs76afyWSit_33JX09AF75ybM0JV0L-83LD0NXYTx6vEMAhJFxGrLp1HncBsWbM6ev1wGR92RWuVgyidX0BYpCIv_Dx6M1cfJ4ugmXZEJHYro8kZs_KDaHyq3fEnGIRjwyu7a1KUsYO_DIsX_CU3Yy5tHHsvHVJDGDtyQu4Y2iswPvhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد بزرگ منچستر در راه است!
نبرد هیجان انگیز
⚽️
منچستریونایتد
🆚
منچسترسیتی
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ دربی اخیر منچستر:
⚽️
منچستریونایتد: ۲ برد، ۲ تساوی، ۱ شکست و ۵ گل زده
⚽️
منچسترسیتی: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106338" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106336">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJuQ4AVCQoIp9FLDcQ3P9qxQCsCR9clY8qCOXwa1x-dJuXMKcKgKjMT9JStddCkcfnoWFvCSBMfslONAroqafPB1LIvBzWMPaFeupTXLWcPmYGZhfUcSuKjlr1elXAoSq8ZMrv-14Sh-JO30d9SFLqzRaGHotKKWfa6_MQcowSpPpF_bqYPU44iLGkjorcTjUNR61kyjEFf8sJcHUrVo8En0cvDv5J-7tKbYE5dfd9PVdAI58Pi6ot91Ojv5fW_qEMh0pYuku6SH8kJhikl2sXeVoSbnC7Ebk5h4iWv_dyM787xL0ym8zeu8PmWSufvhJ19jhiS64Z4b9sp_XWxtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇮🇷
پوستر باشگاه استقلال برای بازی با السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/106336" target="_blank">📅 11:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106334">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe38a96709.mp4?token=XrYy3H_ad7iSZUVjXnWbG-W8CFkYipBqGjuk6E5Ho8S5VfMXUpj4UDA4G7qSHzIT8BmH2THmVx4sVpLAzwBTBfkkmWnaL1zhVW9nX1PYcEmJVHFjaKtcajxNJuF6MAMWOfBpvIMkRgEm5YzN5hmqmd4xB6kVVEEdkPrwyTlS7ujs5QaKR0vPmoxsRwI6yJor-TnZcro8JBSicCsIe0WIYkpNwH6NBxmLBXn-TRXwGW9onuVWl3gjHDHSzpFUg_VsDgOhewlviJ4CV-IFumBknPxlX9qKss6H6PkV5td4Km2wM3Te2q2nZUNhu23H2qD4zRuHEqM0dZKeTQq_XK_amhR4S_3vN9mCeLRZBbQU5Pp77Gdub4_7oEbJ3Q4HwxUL7VblIi8NRBvW_4SiPlVbbK6OlQfUXsx961akj79BMFqRwhFRBQRvhq3355h8JzIrtDa1jJzu2nfm9sA_mP7D99-h-NnCZs2MAFU8IiAqWdDOKCGZzEaAydbjVjEuUIt4cDUsdZAyL1ss0TrLuYxdP6qyfCqHUbVJRIHDLW8rnLBq4n6PadoHq7e0o_69Z50D5eUuI1LAxZ9SR-6kMLAxvpLdAFcgu13qQdRTFNDLYWTUj1N_hLuyBt3MjcB9p1xqBTcEVVzsFHCOvuNdK87MVqtOakjszZxl8-e1vuI71Vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe38a96709.mp4?token=XrYy3H_ad7iSZUVjXnWbG-W8CFkYipBqGjuk6E5Ho8S5VfMXUpj4UDA4G7qSHzIT8BmH2THmVx4sVpLAzwBTBfkkmWnaL1zhVW9nX1PYcEmJVHFjaKtcajxNJuF6MAMWOfBpvIMkRgEm5YzN5hmqmd4xB6kVVEEdkPrwyTlS7ujs5QaKR0vPmoxsRwI6yJor-TnZcro8JBSicCsIe0WIYkpNwH6NBxmLBXn-TRXwGW9onuVWl3gjHDHSzpFUg_VsDgOhewlviJ4CV-IFumBknPxlX9qKss6H6PkV5td4Km2wM3Te2q2nZUNhu23H2qD4zRuHEqM0dZKeTQq_XK_amhR4S_3vN9mCeLRZBbQU5Pp77Gdub4_7oEbJ3Q4HwxUL7VblIi8NRBvW_4SiPlVbbK6OlQfUXsx961akj79BMFqRwhFRBQRvhq3355h8JzIrtDa1jJzu2nfm9sA_mP7D99-h-NnCZs2MAFU8IiAqWdDOKCGZzEaAydbjVjEuUIt4cDUsdZAyL1ss0TrLuYxdP6qyfCqHUbVJRIHDLW8rnLBq4n6PadoHq7e0o_69Z50D5eUuI1LAxZ9SR-6kMLAxvpLdAFcgu13qQdRTFNDLYWTUj1N_hLuyBt3MjcB9p1xqBTcEVVzsFHCOvuNdK87MVqtOakjszZxl8-e1vuI71Vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
هوادارای التعاون دیشب برای اینکه برن روی مخ روبن نوس، بازیکن الهلال، اسم دیوگو ژوتا رو که دوست نزدیک نوس هم بود فریاد می‌زدن.
✔️
👏
نوس هم بعد از بازی درباره این کار مزخرف هوادارای التعاون فقط گفت «امیدوارم حداقل بعدش نرن نماز بخونن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/106334" target="_blank">📅 11:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106332">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933458c59b.mp4?token=fU24EJzIPm7gzda-O3h2w33RCnb1mGWl4X3Iak6d3tcHf1x_TLH0SJZXR2UZqC2umsSKQaGm7ParCadmbHscl_J35gaD_YGU4NJ0CTE2vq3aBcNP22fWq8Z98fQF1kpT-34Sfrajy2G6EqHdAjt2tbx4KD3zYPP4WgZXrZtXnmQXPw5z6dr8GuDTazgTQCWXSn4KdGEuoasXouCqW7qsCmC-h4OFmTwYMvXezHdepmDaWhFuEhRYsHLwdVlHiZHlupBuJtfS18XkDnUHNhBP4GcHJJmQlZqYWOlXxaOgNuGGqLWoTzfUl0BlXTYLCuMWS1K8VbGozLrXzz8WWBul5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933458c59b.mp4?token=fU24EJzIPm7gzda-O3h2w33RCnb1mGWl4X3Iak6d3tcHf1x_TLH0SJZXR2UZqC2umsSKQaGm7ParCadmbHscl_J35gaD_YGU4NJ0CTE2vq3aBcNP22fWq8Z98fQF1kpT-34Sfrajy2G6EqHdAjt2tbx4KD3zYPP4WgZXrZtXnmQXPw5z6dr8GuDTazgTQCWXSn4KdGEuoasXouCqW7qsCmC-h4OFmTwYMvXezHdepmDaWhFuEhRYsHLwdVlHiZHlupBuJtfS18XkDnUHNhBP4GcHJJmQlZqYWOlXxaOgNuGGqLWoTzfUl0BlXTYLCuMWS1K8VbGozLrXzz8WWBul5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر به پوچی رسیده و انگار دیگه هیچی قرار نیست خوشحالش کنه.
‼️
⚠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106332" target="_blank">📅 11:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106331">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3qP0nKBAgKytSx82kR5n5G0fJd9CEHUHJpLhoJ2MX37L3_ECeszKAyNM1S5iflC27NRzAl3v-p82DBscmeI5DHL6aAeVHiLg7-QrbiqPuyzoNhwynMhNgc3_CE5U1zKzy7LLyP6y7ncgdOs7VqFxjGCqFO8tJkCg9kzBw0ZAQVuiw0DFC2HHLg8V2SzrOCQ-H0YeBY3c3Tt7ugbggL2CRbjKAnBOCTLz81gM096y9Qe8Mw7jAXhV8zxlXnlpfDEy-xehLaVl8-hX3gx7VrWlGQ3ZH11rsm9yop1D2V2aFWAKyeCHdZaytKCh0GRRkllg5s_K1HS-oJfQCVo5IkjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
‼️
جدول بهترین گلزنان لیگ‌MLS
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106331" target="_blank">📅 10:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106330">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a30251b5d.mp4?token=Qsx7luB2N7bETlKx7j-r5tYHQ3ZjIfX4Ti8op01j1bZRkYZDpn-x31tNCJtr0DIdz9-527Y_zqN6Di9_cOos2wst7pC7CzpO2KJRi4qrrie5i_c7Fy9-myX3NNwOGMIjJuGNP1Jc_aV2sTCFa4HK035uvRU3hkHWHKB7dwiWMRk6qf47W3L0RBlBuJK7vxcDA_Kk6QDR_062ypFo1MxkczYbHDTuETLJhB63lKXAoEdz0lhZGudyb2b7LgtgOQ-Xq4Jefuy0I6iwXN5mrRtt_rlngHUp5S3MuZqo4zF_jCQhxDuPYybMHucLH1EUG579Q673uvrefDM-aGMfu5s5_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a30251b5d.mp4?token=Qsx7luB2N7bETlKx7j-r5tYHQ3ZjIfX4Ti8op01j1bZRkYZDpn-x31tNCJtr0DIdz9-527Y_zqN6Di9_cOos2wst7pC7CzpO2KJRi4qrrie5i_c7Fy9-myX3NNwOGMIjJuGNP1Jc_aV2sTCFa4HK035uvRU3hkHWHKB7dwiWMRk6qf47W3L0RBlBuJK7vxcDA_Kk6QDR_062ypFo1MxkczYbHDTuETLJhB63lKXAoEdz0lhZGudyb2b7LgtgOQ-Xq4Jefuy0I6iwXN5mrRtt_rlngHUp5S3MuZqo4zF_jCQhxDuPYybMHucLH1EUG579Q673uvrefDM-aGMfu5s5_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کودکی‌هممون در یک‌قاب
👍
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106330" target="_blank">📅 10:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106329">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a4aea1dc.mp4?token=QPk2mzSOnKhs3EAq13uGvY-bIHPApSMRiZK4QYhflGuy9kyN1Wn_hb24JQH3TSQJuWk4mmoHVGV3oo6UcspqNQiHcZr-vGRGWB1z-KtfTV6Mla9O_m-xPR2vd6MoS9tfv4k8FRjCZoqmyW1ijiol-fFiS4QDG3wLldK7g5gYoqPLSk6Mtr4_pbEV_-3CaUqkAs0Af-vyRs0y_0kSJsiNOJl50YM42LNwTR4dDyeeDaZ0lOXFf59DzKt19vxMiFleVyrxF_lznVLkve4HBiLV7O2iz-7oXlPEmrRATTv0kdkg0GMvDwUgfxMgd-fCVYC-1EQZ-51HbX8xBZWpHufHcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a4aea1dc.mp4?token=QPk2mzSOnKhs3EAq13uGvY-bIHPApSMRiZK4QYhflGuy9kyN1Wn_hb24JQH3TSQJuWk4mmoHVGV3oo6UcspqNQiHcZr-vGRGWB1z-KtfTV6Mla9O_m-xPR2vd6MoS9tfv4k8FRjCZoqmyW1ijiol-fFiS4QDG3wLldK7g5gYoqPLSk6Mtr4_pbEV_-3CaUqkAs0Af-vyRs0y_0kSJsiNOJl50YM42LNwTR4dDyeeDaZ0lOXFf59DzKt19vxMiFleVyrxF_lznVLkve4HBiLV7O2iz-7oXlPEmrRATTv0kdkg0GMvDwUgfxMgd-fCVYC-1EQZ-51HbX8xBZWpHufHcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عاشقانه‌های مسعود شصتچی و خانومش در مرد سه‌هزار چهره؛ عجب شاهکاری ساختن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106329" target="_blank">📅 09:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106328">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOdWQ6UNeqqRMklwmT9r2tEt6o6ZGmLQVCh89_1zXDjoVaScjk4kXzTuJBS2WiImLlYQ5xY7uwTr79BqcL7luHtgeK-PueXSV2fAHlj6SBTcuozZ8d7h4miNed4HmbGV4lSbsMxnHrhuzZjb8ZngxLRy3u7X__lxPQtXY9u6ibEX6h4QSI5Uz8jzgGGb1t7yT4Y5Dani6lAKWv4_kS4dmi4ju69vD4PCtxIOyI4grXUiDGbv4hgdlvUl2b9eIEVSxDbLIBgOonxWU-2ISiwHatOIZJlqCbuQSgMNSxUC2VKX6ZADoJuwNx6ft0Wme6s19t2TtASs4X74IyTPx-9Jqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مقایسه آمار برجسته ترین گزینه‌های معرفی شده در بین نامزدهای توپ‌طلا در سال ۲۰۲۶
🇩🇪
هر‌کین 73 گل و 8 پاس‌گل
🟣
لیونل‌مسی 45گل و 30 پاس‌گل
🇪🇸
کیلیان امباپه 58 گل و 13 پاس‌گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ارلینگ‌هالند 58 گل و 11 پاس‌گل
🇩🇪
لوئیز دیاز 30 گل و 23 پاس‌گل
🇩🇪
مایکل‌اولیسه 27گل و 35 پاس‌گل
🇮🇹
لائوتارو مارتینز 30 گل و 10 پاس‌گل
🇪🇸
لامین‌یامال 25 گل و 20 پاس‌گل
🇫🇷
عثمان‌دمبله 26 گل و 14 پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106328" target="_blank">📅 09:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106327">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0452f0d7e.mp4?token=MD9YWisfGMMF1HNlZ-ZQ3HrbHCwpEf97pHMbTTztQsM67CmpHP8-yWC9ScnD58Z1QXsdDlm6MrIGyKvGF3ZqM1DsAMeKsqrvKKWhDV8BGBIJiieuK3_i5z6-QFlbceHrkPEIcZcqk1JEUQRGCZnBwk6ehwaQ2KR5Fv9GC2EqN8dINoWfgurOXwa6uA2lZSOCk0yMzzxHsbxkMIJAJsdlZGbLPOP0jYl5Mi7c2unVjj1mjvYmRGbWT1yDV-lRXr4aqJI1AaGeCp77Xd12URo9aJOQQO51AkajR0QnyXcdx9FV-tKyP177C76Id76ln2ARv7_MZlzBM90dNq8OzKZ_eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0452f0d7e.mp4?token=MD9YWisfGMMF1HNlZ-ZQ3HrbHCwpEf97pHMbTTztQsM67CmpHP8-yWC9ScnD58Z1QXsdDlm6MrIGyKvGF3ZqM1DsAMeKsqrvKKWhDV8BGBIJiieuK3_i5z6-QFlbceHrkPEIcZcqk1JEUQRGCZnBwk6ehwaQ2KR5Fv9GC2EqN8dINoWfgurOXwa6uA2lZSOCk0yMzzxHsbxkMIJAJsdlZGbLPOP0jYl5Mi7c2unVjj1mjvYmRGbWT1yDV-lRXr4aqJI1AaGeCp77Xd12URo9aJOQQO51AkajR0QnyXcdx9FV-tKyP177C76Id76ln2ARv7_MZlzBM90dNq8OzKZ_eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ال‌نینو دوست‌داشتنی چه هیولایی شده
🥊
🏋️‍♂️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106327" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106326">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8UlPNlZ6LCJz6GNPwTQuZBx03JJ-ONgE-sLKLVgdaIWA1m0zINCnErvQ9niF6VHel8ZNmb14mU1uYtQtguSlNsBaDaFraFcVY_qgmgTQeicD-je_CvVv10NIsrdwNjNZ01MgwovLPW5avoVFUIJ56AoiGpQVrUJUnn6mrXB42xC7YKVqa0mRqQgjufb7wSUkewcifhY7OdU6p_eyf_yXlr9Z9MYLVq0YR6S-Klxdtb_Wx0iOmonKay8auKck6kG1NfGXAXuvLBk_F752bziDgBRbWBTS4umtbsaUwzT5x1XbI2N3baQJieA8rEgiy6gm7x2MbPZ5MSsjnJmARoOSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇶🇦
رافا موخیکا بهترین مهاجم السد قطر و آقای‌گل فصل قبل رقابت‌های لیگ‌نخبگان آسیا با ۸ گل زده، بدلیل مصدومیت از فهرست تیمش برای بازی با استقلال خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106326" target="_blank">📅 08:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106325">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde925455e.mp4?token=Oy0vOBizwFxHaHdjeQYZHLQFfwcMhLd0T4bIo584g1oWCPG2_zhJfIFWPVj_JMNCMWwbVb4pJnh6KloUj5lG6RINEaBVv8O8iyoWY4wZG5Bhv_fvPUP2h5eohjmL8WIO2eQsouq7gi8q_dbmARJ4af-BoVjs4Cdhlr4KyMo8lotbXTr0BJ_y4Te_L-RCzsPz4pUc8PIXL6HZRz_7eIf5QC4F5Jadsxh3O6ZvY1GrdoL_cF9XVcGxPBRx_FDJrH4LXzm7pdu81sPSoT6IGZnYH2N8aHbgIYUknPHSIuYmEQWEC2wgqHP-dM_hG-XIb64VWvWfr0mhbVhtrlz7-YKFKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde925455e.mp4?token=Oy0vOBizwFxHaHdjeQYZHLQFfwcMhLd0T4bIo584g1oWCPG2_zhJfIFWPVj_JMNCMWwbVb4pJnh6KloUj5lG6RINEaBVv8O8iyoWY4wZG5Bhv_fvPUP2h5eohjmL8WIO2eQsouq7gi8q_dbmARJ4af-BoVjs4Cdhlr4KyMo8lotbXTr0BJ_y4Te_L-RCzsPz4pUc8PIXL6HZRz_7eIf5QC4F5Jadsxh3O6ZvY1GrdoL_cF9XVcGxPBRx_FDJrH4LXzm7pdu81sPSoT6IGZnYH2N8aHbgIYUknPHSIuYmEQWEC2wgqHP-dM_hG-XIb64VWvWfr0mhbVhtrlz7-YKFKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
صحبت‌های شنیدنی لاله‌مرزبان پس از دریافت یک جایزه در جشنواره فیلم ‌ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106325" target="_blank">📅 08:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106321">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pj8-yzh08oWchO3F9RIQWFPNSfMVnBjA5GgG8ExYqTjt5-afhDTtH4uRv4xumzVYXd1n8P4MWEQNjsFQ6U5LAiaLgF-Rv_938pJq5oqHFA72cS3X04_gAq_VKGpWH9Ro6V_JDhPkHm5yJ7zcpIjWrvHtqPCLyOK8T09JINOExMFzviooUAK06r9VbTJIWhM9b4WqE-brf-1dvuRFtBwx6uvXCcKzYh7m5FeECWzd3SpMsQuRG-Q4r6l85ZHM2YWnldON1dAUXxFS_gFAJDebpowz5sQrugJQHOgxHDiPrfF3se3MeOzmw9B3ykzZ1-od6K5xDZ4eoBi98eo3QiNHaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ آرسنال همچنان درحال یکه‌تازی؛ ساندرلند هم مقابل تیم آرتتا زانو زد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
😀
-
😏
ساندرلند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106321" target="_blank">📅 00:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106320">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fir6rL8COZSpg9jBsE_dCqG00c_u923dgnLr2hIoTaD7L8g51OQHmzzSP9b1tr4vNxFjmqKf1wZOi5tNPVPcFtmQO6zWP5ZepdtZ9ZqpOtVpPxgyBkeyFnt6umqF9nRAOJ_vENZ1u2DOQRyUq55TPFtru-YNmRR6AXuAoghkN6r_dgRf4RNnflqm9I1PiEzy_XrRU2Sjw0bl7ivCjxrQWLjc7Z8ZDNkrJhJ_MY0HojeQ5jn0XQJgO10Yb0i9AYZVpp2wCX-2RB3n-HZeHlAXOueISj9bCNLZumv5ks7aZ9S-egxp3qzfDSX9YfvRkwVDpyYVUgvgKFxtPvpdBYmrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
کیلیان امباپه با رئال‌مادرید در تمامی مسابقات:
🔺
۱۰۹ بازی؛ ۹۳ گل و ۱۲ پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106320" target="_blank">📅 00:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106319">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTFtzg1lQleQuioZbcXCMZEu5ViBWD-JnaAGXKf7-xJhOJHW6HdZSHGx0jbbB422DF1ocgNdy-_8kbKZu0yW8sA9ivbXZzAn7PeYbNSvnvYXrkYz1gqjXBF_-NrKu3TrIjYH-JF-CSSiLGoIeH2fgOlpNLUXguC--6SIIm69u0wYi7OGpPn7YbGnFJIHHjqy4Fz0takm7nwXUs4kfbWX62pBHDEFm6y2Mh8BxKBTfJiUp28EzlGoRwLm6CepkH1Gx8bq28xP6iAnGXNnXHNI9-IBxHif9-hKV3xDp3QSbIokbUon878ps9yOfunA-wpNxDLTiY56MFHCAT8NNRaxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
گلگلگگلگلگلگلگگلگل برنده واقعی توپ‌طلا</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106319" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106318">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiU8Lrck6PZxOyHMXk23uI63J1GTBw4qMh_oq_tbyChPaIAQtTP_qeq1ckEl51BPvfD2cir9QMJG9-k7v__De5zW-xAVWMY06DJCJdeKE9PrWntVcgmUEK994B4iOY77xFnzQ3_NjAkWwmz1f5mYKTvfUTu9Zfgrn_oZiMG70JhgXimeMMbdwP2wTeOXdwM2yDmsdkLG7nCpEGXbSM9LZlYuOVMOgahnn6KG1T1g9LI8BYStttcgtwFRJp2G_n74fY9uAYAhwoySmbgwDndkc5mJjuUmasHZQDinXH2y7qoAvAp8q9ujmZhcugcrPFVoudSM5j1fde6-nbLvkDsOZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ آرسنال همچنان درحال یکه‌تازی؛ ساندرلند هم مقابل تیم آرتتا زانو زد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
😀
-
😏
ساندرلند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106318" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106317">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f6e034671.mp4?token=idX_bdgY_iKW6y-WsDyY2CXXGxVyVLyBQ-bVIpDrrEAOnLBQuXajQQxhOnucP5vf6Jli7KeP3iaQTPnWljfyR8g-hB4HcEIpUFyp9Z898rZ6ioiNORl0tTH8hk97or-dpWGatt3WA1HMNFw14wonmSlwaloVO145Ml8udNF9hby4t1Lb7YelOfIjeXISQETqTbGAb_u_7oI276uvpwcN3GCBzzi-HUl9e2JOK4sD6m6AVwz7np9OIIcEYrMAo2Y90SeGDiPAlCZPxSDIQlA5UfvY5UCZQJHebUxk9xmiGWQ1rjWcFIq70DCOjkvGPPLjuLeZ6ru-yrxJCzqFxSGhzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f6e034671.mp4?token=idX_bdgY_iKW6y-WsDyY2CXXGxVyVLyBQ-bVIpDrrEAOnLBQuXajQQxhOnucP5vf6Jli7KeP3iaQTPnWljfyR8g-hB4HcEIpUFyp9Z898rZ6ioiNORl0tTH8hk97or-dpWGatt3WA1HMNFw14wonmSlwaloVO145Ml8udNF9hby4t1Lb7YelOfIjeXISQETqTbGAb_u_7oI276uvpwcN3GCBzzi-HUl9e2JOK4sD6m6AVwz7np9OIIcEYrMAo2Y90SeGDiPAlCZPxSDIQlA5UfvY5UCZQJHebUxk9xmiGWQ1rjWcFIq70DCOjkvGPPLjuLeZ6ru-yrxJCzqFxSGhzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گلگلگگلگلگلگلگگلگل برنده واقعی توپ‌طلا</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106317" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106316">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اونور آرسنال دومی رو زددددد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106316" target="_blank">📅 00:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106315">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برنده واقعی توپ‌طلا دبل کرددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106315" target="_blank">📅 00:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106314">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رئال چهارمی رو زدددددد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106314" target="_blank">📅 00:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106313">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jizIo77QJYHP1uClSeFu27dvjUJBpiGFD64Wb-cBBQiIcWtqOGbQEhxRNWMFzEP0tA_lfBnoqgs63moqpYRHQA0oSrqx4wTqOh-7RJite6gOazKZbkzd8FkUJmBV7eQPdBcmhYWbC45otrjhnRFAtYa0k2mPaKgSUC57ZEAL8oFxecupGbvRcLjOgrrODyOskcOQCZJz78jyABnls4QBFnv1IE28EdfOWjaowStu-FcYrNp1B89zyB7l5GgyDR7KgvaEi1vaDhngLZEM4cXkWJT8EtkVb3LOT-41HmDb3xrjPKFfse51Sko5lRBOZgmKJgDTRGcb04ElFkC7ib1_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
استقلالی خبر جدید براتون اومد؛ مارسلو بروزوویچ از النصر به السد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106313" target="_blank">📅 00:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106312">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q42ODp1aPT_e5Vu4SWmoE2AGWtw78SXVDWlRu399mfAILLD2aVrbr3Yvs6wAJjaIn0xXS6IunMqR4HXn5A5yWWFPsScsDzYLHdBEpW0AOKk2BSAjI4mXazIlZN-v86jWXmUhOI5rrx_flyGDHZrl8nG6zxCWYb8-AcpHIvkmFwcttLUbdiY_VkslKCWGioclQqXlOpeNdS-10aMF3XghEqH_zaawHG3DaFisYSHDMChYTGtsLaggcofvgNkVYfUJrR50H4UiZTT-Why0pnp9yodQwEoiK0ZlrEJHjPjTdCtMtbTm-JH1X6hyoVdV_01_n8bDBdfrtkLck5YvgP-4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صالح‌حردانی چه دلبری از سهراب میکنه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106312" target="_blank">📅 23:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106311">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d53729e95b.mp4?token=DIvcKXLxXzSbMF85eBHzNBZVywD5shVa0Q-WgeEA3vSYKYt_f6WPTbW4bfWQ0L1LPWkuxYnqNyxoc8HPR6qX3ZsRyypQNdvN_YevExPwie3WEM0MGKADCi35oHJJzThGxu7DSgvmFjSyVMVA1fEjDLuamJ8V63GUcQHQaHbZ74wkAmA6bnitiozqaIRPoh9z-C88WmoOIExcQ-FDMXq2i_AEXLsuZm7psDAdOYTZsieRWOFyotuuoB3iLFTvfN8iDL7kABprutzp9HSdOA937SjOxy8u1Yp-YZmtPTCDTd0_tYka76XeD6HozTUkx4Amk7IOCvZHololcTl7_7DHDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d53729e95b.mp4?token=DIvcKXLxXzSbMF85eBHzNBZVywD5shVa0Q-WgeEA3vSYKYt_f6WPTbW4bfWQ0L1LPWkuxYnqNyxoc8HPR6qX3ZsRyypQNdvN_YevExPwie3WEM0MGKADCi35oHJJzThGxu7DSgvmFjSyVMVA1fEjDLuamJ8V63GUcQHQaHbZ74wkAmA6bnitiozqaIRPoh9z-C88WmoOIExcQ-FDMXq2i_AEXLsuZm7psDAdOYTZsieRWOFyotuuoB3iLFTvfN8iDL7kABprutzp9HSdOA937SjOxy8u1Yp-YZmtPTCDTd0_tYka76XeD6HozTUkx4Amk7IOCvZHololcTl7_7DHDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل اول رایووایکانو به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106311" target="_blank">📅 23:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106310">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/152a6c453c.mp4?token=VDDwg45HJ1d8ZM1M7fEqY9TYbSkQGrVBEGJu0FA6YQWTTnIbkvvvk5y6mjfR6UcOf2eNa-pkRx6pygqRXrrgTUECgY3keREwIhhjgZb3RccSkgXozOKg06sZ7O_RsPQzoOpARngmbKi7Go-b8JRXIZAET7o1Jd2qGlnHm6C9p8ATngCLiWYGrbp4hUjB1FjHXoyqjXVpqqE5uEpMVm3YUxk6gJFoG_fSET62cDbItzSuMiBYonUMQ0D8XGHqkVXWm4qAHT8AYXhOpFzdG-HZteHmIKt25-I3WJIJOGFVOYmuXRP1cDtUDRkpBtBAjlK_CJXU4RR_QHo_PthbpoUelw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/152a6c453c.mp4?token=VDDwg45HJ1d8ZM1M7fEqY9TYbSkQGrVBEGJu0FA6YQWTTnIbkvvvk5y6mjfR6UcOf2eNa-pkRx6pygqRXrrgTUECgY3keREwIhhjgZb3RccSkgXozOKg06sZ7O_RsPQzoOpARngmbKi7Go-b8JRXIZAET7o1Jd2qGlnHm6C9p8ATngCLiWYGrbp4hUjB1FjHXoyqjXVpqqE5uEpMVm3YUxk6gJFoG_fSET62cDbItzSuMiBYonUMQ0D8XGHqkVXWm4qAHT8AYXhOpFzdG-HZteHmIKt25-I3WJIJOGFVOYmuXRP1cDtUDRkpBtBAjlK_CJXU4RR_QHo_PthbpoUelw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم رئال‌مادرید توسط جود بِلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106310" target="_blank">📅 23:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106308">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بلینگهام هم سومیو زد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106308" target="_blank">📅 23:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106307">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a23278bfb7.mp4?token=p5GVtIN_eovMtiTUNHRCA8xN5SQHnRxZY4gJD2w2em8ipaDNB55k9dnDybfCSAu6m_zkv--5UarKDMmfQyALBOIj3voS-dQMGy6gl37LoRdZB33yqq0aEb0zBguoMNkcXzzwk6pY0-xz5ZTssHMLCSqDXPVH02bQO8YK8-2ZioYi4rJPya3G5t2p_78ren8mzFZtpgZSvX46fkcxkWLetcTpSQxYSFs-d83e2rBQSNW619MI2pszNxMSTvmCkppE33klA_FsMKcMMJzLv3iJnu_XjcxrD3ZZmt8HgxRgEWqDbeaSbunKhgx0DMuEdPa_WbdJ-A1aFDpeww5D3lgKUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a23278bfb7.mp4?token=p5GVtIN_eovMtiTUNHRCA8xN5SQHnRxZY4gJD2w2em8ipaDNB55k9dnDybfCSAu6m_zkv--5UarKDMmfQyALBOIj3voS-dQMGy6gl37LoRdZB33yqq0aEb0zBguoMNkcXzzwk6pY0-xz5ZTssHMLCSqDXPVH02bQO8YK8-2ZioYi4rJPya3G5t2p_78ren8mzFZtpgZSvX46fkcxkWLetcTpSQxYSFs-d83e2rBQSNW619MI2pszNxMSTvmCkppE33klA_FsMKcMMJzLv3iJnu_XjcxrD3ZZmt8HgxRgEWqDbeaSbunKhgx0DMuEdPa_WbdJ-A1aFDpeww5D3lgKUIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم رئال‌مادرید توسط کارراس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106307" target="_blank">📅 23:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106306">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2689afdf46.mp4?token=LppqXmVlAxUgh1z0gMHNxaxYsuFKtFP8TMnhraLBUH_G5myz3Im4NBfM0UdtBGWFxZM0Foy0S4F9vA201X7XCYAHlWi-96M2Rk9wXa7WgP3Iy8bDOeeaSVOfov48HvSwF_YQSfxSvzp4fH0AxwEMefMcJMk4AkZ-sYHdw7w8hqCf7XM4GiROVcU8OYRHcPRaF1FyGYYwxumeYm1C453Bf9svKpcNpYSmrNu2ay4UmekBAsCfPVnlhVP7Xu991_AvbwzgakCbIGeNJOGZ_od7ZCUBWTqACGGPuR-g1MCZSLr57_OlZhC08_h84BVmG-SfBnihUfkJhI7xGT2YX3oqdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2689afdf46.mp4?token=LppqXmVlAxUgh1z0gMHNxaxYsuFKtFP8TMnhraLBUH_G5myz3Im4NBfM0UdtBGWFxZM0Foy0S4F9vA201X7XCYAHlWi-96M2Rk9wXa7WgP3Iy8bDOeeaSVOfov48HvSwF_YQSfxSvzp4fH0AxwEMefMcJMk4AkZ-sYHdw7w8hqCf7XM4GiROVcU8OYRHcPRaF1FyGYYwxumeYm1C453Bf9svKpcNpYSmrNu2ay4UmekBAsCfPVnlhVP7Xu991_AvbwzgakCbIGeNJOGZ_od7ZCUBWTqACGGPuR-g1MCZSLr57_OlZhC08_h84BVmG-SfBnihUfkJhI7xGT2YX3oqdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنالتی امشب اسطوره توپ‌طلا امباپه
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106306" target="_blank">📅 22:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106305">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ریال امشب حشریههههههههه
😍
😍
😍
🔥</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106305" target="_blank">📅 22:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106304">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کاررررررااااااااس زددددددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106304" target="_blank">📅 22:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106303">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل دوم رئال‌مادرید</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106303" target="_blank">📅 22:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106302">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9x1sACUpSGZ4qqngw9dAPtCj4MFhOmlsCnOO96viR5E8OHf7NFCn8H62mrJKBnF3SpWPx8QKbLYWJGwEWhZVMf2jJwz3RrlKx-AEQXDwNgqgOwjFkhFwVpDsNH9a0nYfVzOgcx0UVO8PdgzT9-CW1fY5k2fooThp-48mq1_ZgE-FZhF-czZCkoOUIMNAoTeRROgN10ITgT_sKX6tYlK7OfdDBh14HTQgPgK3yV4QAqf3A8BiaOAtwz7Sc3kig7D_pf0WWsZbLhT8bkElKV3JgKxxSx9bp7A7hIcToLLUrcDF-TTv202p1kVO2yYHyk_ONEiN5JPTgQmismdy8L1Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده واقعی توپ‌طلا
🔥
🔥
🔥
🔥
🏆</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106302" target="_blank">📅 22:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106301">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رئال‌مادرید زددددددد کیلیان‌امباپه
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106301" target="_blank">📅 22:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106300">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106300" target="_blank">📅 22:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106299">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پنالتی برای رئال‌مادرید</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106299" target="_blank">📅 22:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106298">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTSbbV5KFDvWNQarFKZVo2NOQ6ewZCTYdI3otUZIgOBMA_eV8Ft5wo_Gv9UvcMnlhVtRGTWpUVTLjXpTFIcLvBhvaa8-UNxWnkSqg88SbmbyNe6kRQ1YqOSvnzpbhVqDnFJFZE67sPbuEp7LrCZCi6t2RnR_m_CKjBtZdyfIndT8EJBnclbR57MBv4ip_9wBKFTxOK8psCeqgXF2nH7wUCUyKweU1bcb3BvUtzUIs8bnSfQV6stbk4vGazP9y0JH8Wsj7IfWqukD8pj2BV7WaGsfYeHSCK2a0BnXhuCK8E52M8-jHYWKdH3K-JjExqM5Q0vxptou270dmk0k7HL3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
شماتیک ترکیب رئال‌مادرید مقابل رایووایکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106298" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106297">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
یادی‌کنیم از فینال سوپرکاپ جذاب اسپانیا در سال ۲۰۲۵ در قلب عربستان شهر ریاض!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106297" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106296">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBo172705bT2zbV0Sj3F0KKht0mre5b3H_I_9HrGxMff-qh45L5GCMDQA1h_kzQyeYJIIZ9DyVGttkE6RXORYWUu7fG5kkVtdoriE8tVbiwZHzpnvHxuOVfdi9IP25rFRvcoHheZK0N3e6iSgfBEsBHbtQZyz36FQut_g7lRoJe52rTIdRBVAYuVVDttXDbfCrYiUantaILz50d50_k88UflA9emDiuDvBE0F1PubWHDiz8MZ4Xb9qUowB3IjYzhcC7EFVxIWzHCuBh2M7x4lIbRI_xqBEWEUjh7Y-jN2irorCQme3SQAzGbz5zTHN9KIxTgB3Hgxxua2DQEXaqBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇶🇦
پوستر السد برا بازی مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106296" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106295">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOz2XwwmDJ3RUsTlnoJA0sFDpuSwjCpne0vR7WALwLZ7f4_J3H6mvt-rDbF7a9N9BuJP0zzIYr7AxD1IPn7CIyMNoE3-bkPy_-o_0z758IP63hMj1MfnV9zrOlB786PoL4AlA85Co94dp9zcNo_1JhQk6mvbBRBkjtq-gyJtV0hp2i_e1qATNpNZ1sSCO-_j_qBYpfB5CFMcM49kS_-Qm4ns0RIQqKnkkzz8X7lC0Q6vT-4s_YWPQQ9bBTUq66MIQAzDkz7IGeaMVgMO0wp5fMMxvuPMWK_NMgVPwJX5EoLmt_3amb7MCOhQy5WSos3D9FPdlLt9MmAaFqOelFPI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
😱
قیمت PS5 Pro در ایران به حدود ۳۰۰ میلیون تومان رسید
🔻
قیمت کنسول PS5 Pro در بازار ایران به حدود ۳۰۰ میلیون تومان رسیده؛ در حالی که این کنسول هنگام عرضه در ایران حدود ۷۵ میلیون تومان قیمت داشت.
🔻
یعنی قیمت PS5 Pro در مدت نه‌چندان طولانی تقریباً ۴ برابر شده و حدود ۲۲۵ میلیون تومان افزایش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106295" target="_blank">📅 20:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106294">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReveQs77sKCxVIKZ3fpffNtNJNlu53is-4qP1c_wymw6R8gKmY3eubVAocIu275wk9Ie9BWqHG5aMuTVd1vI02Hp4W75vecp4NPQEjoBdGqUwvZjXFP-HwADNDO4zYfob67irFioBy-uaBos2ntYKLWoGaMY1jDWG9WXIwf332YC58yFxcgELqX1W-MwhU7c02CX6E6nbeZA8xowGskgwgGlJKbMA6xIZhlw7V0Vrs1DwQjF7aOxup6aK9sxWnc_5yD1uGw3o7kLuGy1HgY9MM7Ecc9GztvyCbVzXI5zwsrEqxHTz0YqyFUrZob-IQphfu2Cj7Xpzip1yfyJbc4HzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب النصر مقابل الخلیج با حضور GOAT
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106294" target="_blank">📅 20:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106293">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMUmauHOnW9KsuTduB6N_khWFkDVx8OMEpLcT-V69UiaDaGoEI1FRMLJC_bV8zhfl2vjU8g1NTKmnAuMwo4qbw2ZPaAjfvSwwf5K60WA7ILThBa6kUrBME2a0Pzt2ED49xu3CcOr1104LxNv-gLOYzmoD8sgweEGie0glwVIaV28pymOWFOX4-Al_v1_-1TpiuAsl0EJEZngVxePtoJbRRQGJdBke9sHyhmHU36fBrqSAc0wpDuWqvjgQmrEO-bB1USuUou8x7TqWVoK-x3hUO4Vw5Hak--zsc93ne4jrvfoBdBPrRLcjEiKV1Jc8PP4H2Lr5JrDrT5rH-q_OaZtSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
استقلالی خبر جدید براتون اومد؛ مارسلو بروزوویچ از النصر به السد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106293" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106292">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
▶️
صحبت‌های‌جالب یک‌بانوی ایرانی شاغل در آکادمی باشگاه چارلتون انگلیس که بسیار شنیدنی و جذابه. حتما ببینید از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106292" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106291">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/045726ccbe.mp4?token=BTfYLBLNZZ3nzqTmxR7M5KeBrIL6zjJcCs2NhDkInU4-_8wDLjD6AnaalIwUEV6HmIbqzWfBd0D9kd48kJLEe1CWNVZI-lGClirusRIG61XhpM8m5tyoAFXSY3gGSbTcoExecpW5vAPwtiYJUUgF4Cp1bOsD8_YhJf_PcGB6tfvoSJSeg3c2_2kVpAJ1VWqStWL6UvnDTnikYWw4rHbQSYJYZMpqpPnocfDijBm7mf2R-DSepvds99PgrpH6D8gQ3tKuxgShyb2To_l7Q8O41QKo-o4TLnBtw-cmQin7G36uS8Lj_barmWgAFrunilSk7tzNwxmSPafOzH9gGEe-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/045726ccbe.mp4?token=BTfYLBLNZZ3nzqTmxR7M5KeBrIL6zjJcCs2NhDkInU4-_8wDLjD6AnaalIwUEV6HmIbqzWfBd0D9kd48kJLEe1CWNVZI-lGClirusRIG61XhpM8m5tyoAFXSY3gGSbTcoExecpW5vAPwtiYJUUgF4Cp1bOsD8_YhJf_PcGB6tfvoSJSeg3c2_2kVpAJ1VWqStWL6UvnDTnikYWw4rHbQSYJYZMpqpPnocfDijBm7mf2R-DSepvds99PgrpH6D8gQ3tKuxgShyb2To_l7Q8O41QKo-o4TLnBtw-cmQin7G36uS8Lj_barmWgAFrunilSk7tzNwxmSPafOzH9gGEe-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔵
گلزنی گابریل‌مارتینلی در بازی امشب الهلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106291" target="_blank">📅 19:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106290">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMAjTQC1cmkn4DC5eoeKRDFfYLy2o7vkCwSOYV9P7TeSPnpuh_yH8zHnok8FWhpr2-Z0Yypn-dmGbVD7u7fKTVrrYZZTLT9SR_tCkwdzYoT87f0NC1sAk4Gcc6di8BZ6Wcy1zs4GBQPqjwwsrqDKscrc0kH66TsnsjLO_mM3g8GXCi3jbS0YCzZ2naFL0ipwIut3r1HcZacvKSiijreXz7tV6Yzc3D4ofCswVtfou9IbX4sCxh0mjVCLoK42oPg-SxWvLlNLd5Fgvt0UXSaKjuOrXR5RSfAkOw7eFWks4zzoYX06Nvvuq8CCksSpzrphopBqyEtr-N3TjaH8eh9zEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست بارسلونا برای دیدار فرداشب مقابل لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106290" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106287">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e5692356.mp4?token=AFzTt0uq5r5N_10CAnhZPCTqHMUxq2Ay6_XJwUItAll0HrsgDd_rWj-MKZXYzAwk5Avuc35mAme0siR_WB4DxEm5Izg_nLGiWkZkPLfX08j_3bKeifN9tvOqhBOsQWtWizHTtB5oFbTlqtAQlOo_JEhQhrHQEvIdVGmhCbAH3IigG5pR_ws8PcwpkDaf8wqNw7715PSJPh42t4hDa0AgOD3VFfRr40u8CJyJ48hKNo5v9NfJTphe-zlfuQ5BsxrzcNU1TLvoCEpBtfWkYziD6uAHQ9OOZMdUwQ0xnWQwPgJg6cwbpEAKreR4jCg320ostk1wnkI8t8xLmZMPuNc8XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e5692356.mp4?token=AFzTt0uq5r5N_10CAnhZPCTqHMUxq2Ay6_XJwUItAll0HrsgDd_rWj-MKZXYzAwk5Avuc35mAme0siR_WB4DxEm5Izg_nLGiWkZkPLfX08j_3bKeifN9tvOqhBOsQWtWizHTtB5oFbTlqtAQlOo_JEhQhrHQEvIdVGmhCbAH3IigG5pR_ws8PcwpkDaf8wqNw7715PSJPh42t4hDa0AgOD3VFfRr40u8CJyJ48hKNo5v9NfJTphe-zlfuQ5BsxrzcNU1TLvoCEpBtfWkYziD6uAHQ9OOZMdUwQ0xnWQwPgJg6cwbpEAKreR4jCg320ostk1wnkI8t8xLmZMPuNc8XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
تفاوت صحبت‌های چوپان قبل و بعد جدایی از هانی‌رامبد! نمک نشناس هم که هست ظاهرا!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106287" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106286">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt2ObcPcNbvoBiVjsNnx7-CMPSp3XFPPve-x6pIvnWuU_Gxi1ibvrsw0N9ORmXC21PsMyNlpAaZR1FrN_m4z3Ka3IA3OrlUNT0LULDaVgRJGO6fVs250l8d-0rQGBm4fbaqT9pgSPu8xoTELF8XwOYVXvG2sl_p0Scx0LrvG9-FNrAjfcyVmgONrF4esknjoY-bZYON3zJSnLFBOxuueu6i5weOBT0vSvmGaoI_jSH5KWqbZ_iAqLHkY5pi3T4rLJjssjCQnc1Exo54FDBRPWrG5acPkMy7yxna0RVBen_dvdjf200mfMJKQ9-F2inH6T4T14w6paZXjUf7Hes2_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
جدول بهترین‌گلزنان تاریخ لیگ‌قهرمانان اروپا؛ هالند و امباپه با همین فرمون پیش برن به راحتی رکورد رونالدو و مسی رو میزنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106286" target="_blank">📅 19:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106285">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c64420bb.mp4?token=OYJmeJ2HPSb5aefobaE1Z0VKEIlNQYVzcO5-NnUwOa8R3GDk-8_XQmGY_2NpS0q_7HPLzdIiZvl6kEV_Xo484TRJEo57JgcCAKfadp2j-81vSTzrMoWYfhnqQ8Ovkx7asfN0sUBAyZbYaO4C3ZgburoMLuXnHtydGCLUGAcb-4Yg4oPgcH5V9MdNUQ4A2Ssfwd0F9TePSVbnQS1sra7pKPK-39lCXW2H9t5MUfbxZ9jxg2a4bLbTgH7qKJeHHfQN1t7Rm-Ju95IQiYUliYN-Iha1R5Fk16gJetQtPge6rSUmwPoOE5GTUOtndlLOMO1vdQN1jqmbooxoygIp4GQbjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c64420bb.mp4?token=OYJmeJ2HPSb5aefobaE1Z0VKEIlNQYVzcO5-NnUwOa8R3GDk-8_XQmGY_2NpS0q_7HPLzdIiZvl6kEV_Xo484TRJEo57JgcCAKfadp2j-81vSTzrMoWYfhnqQ8Ovkx7asfN0sUBAyZbYaO4C3ZgburoMLuXnHtydGCLUGAcb-4Yg4oPgcH5V9MdNUQ4A2Ssfwd0F9TePSVbnQS1sra7pKPK-39lCXW2H9t5MUfbxZ9jxg2a4bLbTgH7qKJeHHfQN1t7Rm-Ju95IQiYUliYN-Iha1R5Fk16gJetQtPge6rSUmwPoOE5GTUOtndlLOMO1vdQN1jqmbooxoygIp4GQbjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫣
🥲
دردسر‌های کیلیان امباپه هنگام دیدن سکانس‌های فیلم زیدش اکسپوزیتو :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106285" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106284">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833fb28b6e.mp4?token=NpE7eJ2DmY052v2JTsFFfYHjIKd9gCNsGNMq45mSu6Cgw0FqRB4fSx50i4p1ciCcijGKUdz2dlB-jwpJ-Bsq5vTK10NiXD7O1GWjAYfGw6sX9mgd1RpffJAFOQky81284FRinH5DWJjx3EeTAvSnJYOXBvFJclfz-2h41bJPWnnAXR9i3qZdOFBKiV2cUbMyoecp34WhvZDn1sZ6itzuRRpfhQLPxsDkJmDSM1O_IQIwdtj8s2Qqz3PcNEUc_BEWVb7L77EFBP46nx3NeGfjZVhz5JWTg7crM6QZAFyXED8uT1IAGfiQ9t1VatwzP6qjawVhSkZte3U1HXza6j-BGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833fb28b6e.mp4?token=NpE7eJ2DmY052v2JTsFFfYHjIKd9gCNsGNMq45mSu6Cgw0FqRB4fSx50i4p1ciCcijGKUdz2dlB-jwpJ-Bsq5vTK10NiXD7O1GWjAYfGw6sX9mgd1RpffJAFOQky81284FRinH5DWJjx3EeTAvSnJYOXBvFJclfz-2h41bJPWnnAXR9i3qZdOFBKiV2cUbMyoecp34WhvZDn1sZ6itzuRRpfhQLPxsDkJmDSM1O_IQIwdtj8s2Qqz3PcNEUc_BEWVb7L77EFBP46nx3NeGfjZVhz5JWTg7crM6QZAFyXED8uT1IAGfiQ9t1VatwzP6qjawVhSkZte3U1HXza6j-BGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
ریدمان دیشب داور اسپانیایی بازی لیگ عربستان که بجای کارت زرد اشتباه کارت قرمز نشون داد
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106284" target="_blank">📅 17:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106283">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9242df0ef5.mp4?token=c0MpQQP4OptSRX9aFwJkYzd3WvutngxANuvaxIOchhEenwvr87L0dW4zm0MJm9i3EFCJ6zxunUfguNoN0cjy2mMhLqzMquD7lTEBEmd4MPGCVJKvr_YjCVQg1ieFacNyts_yGg29karF68IwhXE50iesplFh3LaPycrC-wao3Rf0kRZIbFxzdHPCuIxD4cIk1Adg9q_jF2ARqVxUWo7ZjBOhxDojjSx3tG93-9zRZ7sRQ7IwYaMKZ1pX3c0jYcXC73iRvCrC22YpXqgR8W9X6iMOV3LITTa-IBEGbJgJe7ugTCZ9jVy6gHzeSsT4hVS7UUN0v9fThZPxhx8Bw4RwhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9242df0ef5.mp4?token=c0MpQQP4OptSRX9aFwJkYzd3WvutngxANuvaxIOchhEenwvr87L0dW4zm0MJm9i3EFCJ6zxunUfguNoN0cjy2mMhLqzMquD7lTEBEmd4MPGCVJKvr_YjCVQg1ieFacNyts_yGg29karF68IwhXE50iesplFh3LaPycrC-wao3Rf0kRZIbFxzdHPCuIxD4cIk1Adg9q_jF2ARqVxUWo7ZjBOhxDojjSx3tG93-9zRZ7sRQ7IwYaMKZ1pX3c0jYcXC73iRvCrC22YpXqgR8W9X6iMOV3LITTa-IBEGbJgJe7ugTCZ9jVy6gHzeSsT4hVS7UUN0v9fThZPxhx8Bw4RwhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری جنجالی محمد سيانكى: برخی تیم‌ها در سفره خانه هاى تهران بازيكن جابجا ميکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106283" target="_blank">📅 17:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106282">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYqIkizJIPVsENCjM7SmcmwVJXs7Xh2A9bw1b8z1IukKGHgXo3Qoqz_jiRikHITN5SDQWCzRQyyZrt7poNfR5zIXajVE6pCPY8lGi4TM0qYaco5aVSxTOeKPaREo_ENdQImxEDWXG8o4EOPfGJRadVs-DABedgxgtujP_UCoYqiW7qDd5Zq3E1qhr_8fw2zQRbNAVCIwdbzR9UQ0c2e5MgdEbEWqnRACcxZPy8TwREal08nqU38YVB500L_y62sYyvDJcKr9uAm4gjZHFIvo9OKfQzN1eVGWH9PiSa93U3OGnUL3DWtIwf8gwd20Q4GoMOG8E3-R-nMqpByFQ0KMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🔥
🇪🇺
عملکرد تیم‌های انگلیسی در هفته‌اول UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106282" target="_blank">📅 16:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106281">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8b60637a.mp4?token=CKQY72CWgA7R3NVI7jHG8ibwFRxrXgz7g0GxcJmwRDrKDBcYlljIQJaR_iwdSnd9PgWUYhyzjg2h9w558GDNV1-p7XtJf4pAlUwKPHA4EhrFouyeuozS_eTyVYk-4jDdByTGTSU5M5tWmTjkIYTis8IuNkmL8h93gpbJQMaPxvKVvG8BZ4phN5B7aOMyPAZOa4GYFe6Bc2ghcVlxMD7Znlm6RfL0cqqgBxb4wXFuuaX2RhbmFWMkjjhxu_rqvwfl5HHWO3W5PMJwxCPMwVjCWapu7g9ACKBd5ntbIBlV1rRKOfvDM7-2i4eD5HQFzgotxevvpe8HuMMivpFBAvvWTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8b60637a.mp4?token=CKQY72CWgA7R3NVI7jHG8ibwFRxrXgz7g0GxcJmwRDrKDBcYlljIQJaR_iwdSnd9PgWUYhyzjg2h9w558GDNV1-p7XtJf4pAlUwKPHA4EhrFouyeuozS_eTyVYk-4jDdByTGTSU5M5tWmTjkIYTis8IuNkmL8h93gpbJQMaPxvKVvG8BZ4phN5B7aOMyPAZOa4GYFe6Bc2ghcVlxMD7Znlm6RfL0cqqgBxb4wXFuuaX2RhbmFWMkjjhxu_rqvwfl5HHWO3W5PMJwxCPMwVjCWapu7g9ACKBd5ntbIBlV1rRKOfvDM7-2i4eD5HQFzgotxevvpe8HuMMivpFBAvvWTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی تو تاریخ لیگ‌برتر ایران هیچ‌شادی گلی مثل این نبوده و نخواهد اومد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106281" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106280">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5318ea7807.mp4?token=fIqU2PyZDr-RaFCb_oTDgtMFYjNuJH42ZMZ70VJ--FWCpJKAr1CS9FmpvDl9xHAyFU7k8zfyWOaIk6c7HBqvAFDTqfkedjdMskqTSM0PZcoLzZBANIrshNO0e8iykdMgFLvQjMB4K0uvgefONUZITTsbOV4B1kWsrzKJuf1yZAaSY2mN2QA_sDjepxi2OkJDW9sRP7dejkNgwMvUM60FFKKQHuS21iUG9vXJ0bf6pwMiSyExTuhMKH-kjle6dQ1cFuxRIj3o0Vu6IFvYFl03DY0fXD6FU7y3vnm4ASh4ZLUmeHTR6xAUnIQ3LP5nrHiHEN6fult4tBkA24OTavycEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5318ea7807.mp4?token=fIqU2PyZDr-RaFCb_oTDgtMFYjNuJH42ZMZ70VJ--FWCpJKAr1CS9FmpvDl9xHAyFU7k8zfyWOaIk6c7HBqvAFDTqfkedjdMskqTSM0PZcoLzZBANIrshNO0e8iykdMgFLvQjMB4K0uvgefONUZITTsbOV4B1kWsrzKJuf1yZAaSY2mN2QA_sDjepxi2OkJDW9sRP7dejkNgwMvUM60FFKKQHuS21iUG9vXJ0bf6pwMiSyExTuhMKH-kjle6dQ1cFuxRIj3o0Vu6IFvYFl03DY0fXD6FU7y3vnm4ASh4ZLUmeHTR6xAUnIQ3LP5nrHiHEN6fult4tBkA24OTavycEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🥶
باریک‌ترین خودرو جهان با عرض ۵۰ سانتی‌متر ثبت گینس شد! وزن خودرو ۲۶۴ کیلو هست و حداکثر سرعتش ۱۵ کیلومتر بر ساعت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106280" target="_blank">📅 16:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106279">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c27ec481.mp4?token=pPxJaDe3Tvb_4pliFB97ExH4FSHdAjPGqC8_i0Rei97E_dJoV_ogTkcX691cIoh6PM2IvKRoS6_58IUVdu8r1P4tJXVdhfMd8OZVGO2FxWgzi3B14110d6dxlhQ2RWPLUJu_KZZGeto1uc8L1ISDyxn-66kaa5Fd5xbzUVOAcUGe6FMeoTk6dGBqIJDVjl8ZDD9Ih1YTaTI78jngYKosPN6jjtHPQt_Xrg3AkxLQurzjH7JWvOGEqjZORMHLDpz_Zvd1EtbEHLHPA3TeNuXnc9eouxFEXvbrrWsnFFzGMi0d4kQaXYe2Ejhr5bpzTTfLRL5Ev9GdzlrgQlQc1xI8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c27ec481.mp4?token=pPxJaDe3Tvb_4pliFB97ExH4FSHdAjPGqC8_i0Rei97E_dJoV_ogTkcX691cIoh6PM2IvKRoS6_58IUVdu8r1P4tJXVdhfMd8OZVGO2FxWgzi3B14110d6dxlhQ2RWPLUJu_KZZGeto1uc8L1ISDyxn-66kaa5Fd5xbzUVOAcUGe6FMeoTk6dGBqIJDVjl8ZDD9Ih1YTaTI78jngYKosPN6jjtHPQt_Xrg3AkxLQurzjH7JWvOGEqjZORMHLDpz_Zvd1EtbEHLHPA3TeNuXnc9eouxFEXvbrrWsnFFzGMi0d4kQaXYe2Ejhr5bpzTTfLRL5Ev9GdzlrgQlQc1xI8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
🎙
هادی چوپان درباره کلیپ رقصی که در دی ماه از او در صداوسیما منتشر شده، توضیح داد این برنامه دو ماه پیش از اتفاقات دی‌ماه ضبط شده و ارتباطی با حوادث آن روزها ندارد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106279" target="_blank">📅 15:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106278">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f692d60102.mp4?token=fCnCcdpD32fHuSv-xX0c16cOs855ZzBBY3aRcSRYswV6Qytoh8cwMYfp1JLu1fCR0_4Gp1uZ393nHnEQkFa87j0gIBcQTWYtSxNSaMOmjYy4_emCnhDwHF9JGMrtXPFpDK3c6x_XjT6ZBaleCTu1MeeKL4hnTKVx6PGT-H9a9QfRaOMeH6VIplhGhNMuqAwdIpqkvynqahEYC5Vnu-KnOLr2OWP6Fj3lhImbbUrEabZlV7STkWgqEjWNpm7UhATvUo0j-V7AiqO4DyU0sx7Puouypsx5RQf9cwVFszi94QkfHgencjhW0xOzC3tH4mkZPJbrN6P_K4FTgirAqnaKtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f692d60102.mp4?token=fCnCcdpD32fHuSv-xX0c16cOs855ZzBBY3aRcSRYswV6Qytoh8cwMYfp1JLu1fCR0_4Gp1uZ393nHnEQkFa87j0gIBcQTWYtSxNSaMOmjYy4_emCnhDwHF9JGMrtXPFpDK3c6x_XjT6ZBaleCTu1MeeKL4hnTKVx6PGT-H9a9QfRaOMeH6VIplhGhNMuqAwdIpqkvynqahEYC5Vnu-KnOLr2OWP6Fj3lhImbbUrEabZlV7STkWgqEjWNpm7UhATvUo0j-V7AiqO4DyU0sx7Puouypsx5RQf9cwVFszi94QkfHgencjhW0xOzC3tH4mkZPJbrN6P_K4FTgirAqnaKtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
تو این شرایط اگر از اینترنت زیاد استفاده میکنین برای مدیریت هزینه‌های خرید بسته، این ترفند راه خوبیه. برای دوستانتون هم بفرستید
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106278" target="_blank">📅 15:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106277">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9d15a53b.mp4?token=VMsfB2lLFanWrUr5cwgl0LnoK_BCfgCOWkqu3w5pLHbr6JvYYoyXeuCKkAru7yTxovPwSBJAmb00ETXHCBegW5wIf67oNFqy1DyLlwYMirAlYJN3hGPMl0UfbMN8Wi_Y3LePdwcznArt_wft713oRva7YKQ6Sh4CL3n5Om2HQmeqwB8eKOBoLSBzslKRXmj1VDRooYME9H0wpjIp6wIOvwwL9BglMwHofdHOXgnp5UCg5sYUKYt5ucSLUw9LiYMggha3zoXc_dHaV0a_xp-wJv62KYg5YOBX7mG9Gw5tRq48Oagn93LYdiLTCzDWaSoONv7JgyciDyC8sryo4dZHsSjqOQlo96KKodf2mO4HwCwh-EhyOo4Ot1pPJnJxD3es_bWXQfG6RFQQNoG2wxyOChsUVuJabM_UiPy_1JrYvvvI4voQSbYW3nFhAq4yeAqvekRkd4fosgne71jU_E2ZL-lHuxPK_SWcOIkDV3Tyd_WMCxUVjAYoOGB7Bhg6-1FLlw9vWc0SgifumNFnkxL5U0PPBUxeqR1zMTxypmgcMmFjGj8tybxkJq8z4xOarMI1VK_e4qFgx8IcvP9BLkVUH0VqnxJKQZPoVWTOTuz_bGcIQJi-DTGxmky3NZkUX7xUIde2ocVatKy2fOktrImY9VI6jr5FCNR4JuXYWTbE9Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9d15a53b.mp4?token=VMsfB2lLFanWrUr5cwgl0LnoK_BCfgCOWkqu3w5pLHbr6JvYYoyXeuCKkAru7yTxovPwSBJAmb00ETXHCBegW5wIf67oNFqy1DyLlwYMirAlYJN3hGPMl0UfbMN8Wi_Y3LePdwcznArt_wft713oRva7YKQ6Sh4CL3n5Om2HQmeqwB8eKOBoLSBzslKRXmj1VDRooYME9H0wpjIp6wIOvwwL9BglMwHofdHOXgnp5UCg5sYUKYt5ucSLUw9LiYMggha3zoXc_dHaV0a_xp-wJv62KYg5YOBX7mG9Gw5tRq48Oagn93LYdiLTCzDWaSoONv7JgyciDyC8sryo4dZHsSjqOQlo96KKodf2mO4HwCwh-EhyOo4Ot1pPJnJxD3es_bWXQfG6RFQQNoG2wxyOChsUVuJabM_UiPy_1JrYvvvI4voQSbYW3nFhAq4yeAqvekRkd4fosgne71jU_E2ZL-lHuxPK_SWcOIkDV3Tyd_WMCxUVjAYoOGB7Bhg6-1FLlw9vWc0SgifumNFnkxL5U0PPBUxeqR1zMTxypmgcMmFjGj8tybxkJq8z4xOarMI1VK_e4qFgx8IcvP9BLkVUH0VqnxJKQZPoVWTOTuz_bGcIQJi-DTGxmky3NZkUX7xUIde2ocVatKy2fOktrImY9VI6jr5FCNR4JuXYWTbE9Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
داش‌علیرضا منصوریان درحال یاد دادن ترفند سرمربیگری به اسطوره سندروم‌داون استاد علیرضا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106277" target="_blank">📅 14:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106276">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa2c3aa1e.mp4?token=grW_G1ST6exFLd6XJruhhLe5dT-xoyKo-fbxa5KGSw3-ohkh4Qxeergw4mdFuceqG-BSoOd_ZuJQ38ZVqZXwKeaqyBIXyl1_J3x-_IKdN-oJss2AVBMMxdVpJ0EkHbpK3JB2VyvNCfij4_12VT_sRq1hesdj03vjgwUtAWM60zwoohQ1DRJmZV9688c3CxgFKt_aU1oTuJh7WUQjbjze48VRCjn2bOuAdUSTVqQjTRHxVQHVdcktVafU1TgASg3oQtuj_eUjGH6rNiRJUDvHNJfn3NmPaY9MFyhXOT7PQLySfd-PyA0hGJj0wfY1ZQLsGO03Bz-zjjA3RZW0FvM5iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa2c3aa1e.mp4?token=grW_G1ST6exFLd6XJruhhLe5dT-xoyKo-fbxa5KGSw3-ohkh4Qxeergw4mdFuceqG-BSoOd_ZuJQ38ZVqZXwKeaqyBIXyl1_J3x-_IKdN-oJss2AVBMMxdVpJ0EkHbpK3JB2VyvNCfij4_12VT_sRq1hesdj03vjgwUtAWM60zwoohQ1DRJmZV9688c3CxgFKt_aU1oTuJh7WUQjbjze48VRCjn2bOuAdUSTVqQjTRHxVQHVdcktVafU1TgASg3oQtuj_eUjGH6rNiRJUDvHNJfn3NmPaY9MFyhXOT7PQLySfd-PyA0hGJj0wfY1ZQLsGO03Bz-zjjA3RZW0FvM5iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
دلیل جدایی هانی رامبد از هادی چوپان: اون مثل برادر بزرگترم بود ولی یه زمانی از من خواست پشت جمهوری اسلامی نباشم که من قبول نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106276" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106275">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg8qC3zwo4XRtdP15XZw-3cj9bxmBfr3K-FkapsO1eCIF3Cz1N1pR900f6vAh39G1IarzLG0OgflAc0_OmRsLk-XjAe1-9t8FWes2RyiiDjT6ysYiF2jLIRztBUaQ1azmD0FzEX-WQ3wRaUW10dH4FZ1NU5qgx15CDeFsFo1X6FYfKSVe2cHSy8GNHrrq1DnScX2545dx58mCMfYz8UqsanN2e_69vU4VXV41LFYUD76ivDteOrWO0_8GL8xj9GktfwyRGmBANIBd9eVT_yXCgqQ-Bh_qtsox_qTsdUhPvJVOfmWCiMxjXzjb5NGXwZ5cZYhc4SGdhwzAmLJmjEkOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لواندوفسکی و دی‌پائول که درگیری‌شان در هفته‌اخیر جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106275" target="_blank">📅 14:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106274">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJWTtbLv4yZ9riqVyUvZmlsS70wvodYf8bDV-aQsevivtj5j20WHciJSXeDBKWdYyjFxiOS_Yxk-nXZDrP-dVgcGMmrIb7IpiUb1dqLEjC_-cJm6QQnRmjShYxS6SQvOJ1aiaJKqCpISXa0HPdGBT8UOmm2rPPS_nIzxvA97czsmyx26nGCvXS4OJfEhkdx0fvyg3QjNEAI_tnXqpOk8R4opRH-Bc802FyDWQpe8JrMTE9u0dSu9o3qV9lhA0bX4QZrn5PQM7ez5UHrCsi3nn1QwURNBELapEnCYN_RqOSGa_dytgtmx-7SOxpIf1pLnrroGwaxgCQpekDZdkIJAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
درخواست تاجرنیا از هواداران عراقی برای حمایت از استقلال در بازی مقابل السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106274" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bcc13d5f9.mp4?token=tFCPqlDNPW6n1mXK4NbIQWwyudN4CXaJa7f45WyBTRtaNEpr8e1v5J7QNeOxI3fuVEGG1e4X9wzCSGsKKO7bytlztp8xkPRqmpARiyOd8a5bjh_BL-dbnVFqjC2bS-_s9No7vrBCxpzOchlMxe2ddHUuj0SulkHFY8CijgXFm_zj-S93kvBXWUiQd8FGJKHMm5iLg2P6FZZ08bj4l3Qm7jFpUFSbZFm1eKxxf20nf5XZ4XmeC66E7x-USy-1vwilNeoBv_14zaM94HPZYcla6Mv8F1Q-jfn4arroahOJlVrOxhG4R31DMbnlCd0YLeUsGCgkaxDF89kDSA6c7sa6OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bcc13d5f9.mp4?token=tFCPqlDNPW6n1mXK4NbIQWwyudN4CXaJa7f45WyBTRtaNEpr8e1v5J7QNeOxI3fuVEGG1e4X9wzCSGsKKO7bytlztp8xkPRqmpARiyOd8a5bjh_BL-dbnVFqjC2bS-_s9No7vrBCxpzOchlMxe2ddHUuj0SulkHFY8CijgXFm_zj-S93kvBXWUiQd8FGJKHMm5iLg2P6FZZ08bj4l3Qm7jFpUFSbZFm1eKxxf20nf5XZ4XmeC66E7x-USy-1vwilNeoBv_14zaM94HPZYcla6Mv8F1Q-jfn4arroahOJlVrOxhG4R31DMbnlCd0YLeUsGCgkaxDF89kDSA6c7sa6OzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمود فکری: سهراب بختیاری‌زاده از دست صالح حردانی حالش بد شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106273" target="_blank">📅 13:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106272">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwYDXZW6h1oJ-IoiEX06honMHc_zzizBuZLobIr6RV9YXo4oEeDsQMqQGPkv14aOqPpsvCQyVG8cBBIdOdVrqeMTC5jTRULufUVQtM9e38juG3aIrmPiCwuS4li-O8GRZKuHO8uJlgoDt5RAfn2k_jm2PanWZEh2kX8cTIFdarE4fzyI4aNt00jz3PFm46-3TcIfO-JfHC5DQ3vaKhDrQhFgvf33oc_dlVQRElhdd88L1F29bEOK_CRSeu2tRx-_7mxoM7G5ZEOzFaK6Scah_zC3g4jNCb788FiuaNKRxo_-1bjRRJfX0Sp9KpdBgqdL4q9C-ouEr0S8KuL4md06SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان‌امباپه: اگر عدالتی وجود داشته باشه بدون‌شک توپ‌طلا امسال باید به من برسه. درسته جام باشگاهی نبردم اما در جام‌جهانی تاریخ‌سازی کردم و این جایزه هم برای عناوین فردی هست نه صرفا تیمی. پس مطمئن باشید به خودم رای خواهم داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106272" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106271">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ae35Pj4xJMkn25QQDoYMdBAxgNkFSWB3xtZhCawfhxq92xkv0-C4PWWqMO60fJdTSU0rTNAXr3VA1KKA8c5X507GFI2EPOT72_R_s3u1mJkLSA8TiNuA6gDQs60C5SnSON1t4OWmcQzTLVyIKX-KY0GvepuHHMOx_H83DETDnEdnyYiHliEDAcd8tL0pt8i6KWlecJKDb3-LV2xx0UlKd_gscwarcwsX82vuUY5fedSxTPfDcyZox3ROP_FP3BD_dnaWa4390RW51VgkPD8isCcY-dNsBDLvyyzf_5Sw97bIhx_fMm53siHfThnhXch3qwHm1E6WrQH9-ZwpuWdN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
با رایزنی صورت گرفته مشکل پرواز استقلال به بصره حل شد و کاروان آبی‌ها تا ساعاتی دیگر عازم این شهر میشوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106271" target="_blank">📅 12:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106270">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b41d0adb.mp4?token=bb_qNFrmiufqOjVEG0OGLuVfQFT3v_prO8Lt86o158SWzV15FTs9WmWmXesiu_1iQYBvBEyOWHPNC8XUnCINOb2w45kwpjU0eP68V5WSE4HsnM0C4L7hd4jrs6b-Ls7fvHdkK4xBken5t5-LVMhfFCti17b0JlLDUOTGwl_QQ1oxEzot00-WyRs_Um7ZyHADQ9PDfTRtLOGO_viWtJRWat8k4WJ1VkFY_krLxtyR5jTSwou7g5ttMoEHdVhF9KNBHmrUjZlhDs_Hw8P4kIUkLyCaVWYRhXwjxdM47kuf0g6De9_cLNcxeHXoAyDLsRANe-v3R4sQSo38e84KHULC-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b41d0adb.mp4?token=bb_qNFrmiufqOjVEG0OGLuVfQFT3v_prO8Lt86o158SWzV15FTs9WmWmXesiu_1iQYBvBEyOWHPNC8XUnCINOb2w45kwpjU0eP68V5WSE4HsnM0C4L7hd4jrs6b-Ls7fvHdkK4xBken5t5-LVMhfFCti17b0JlLDUOTGwl_QQ1oxEzot00-WyRs_Um7ZyHADQ9PDfTRtLOGO_viWtJRWat8k4WJ1VkFY_krLxtyR5jTSwou7g5ttMoEHdVhF9KNBHmrUjZlhDs_Hw8P4kIUkLyCaVWYRhXwjxdM47kuf0g6De9_cLNcxeHXoAyDLsRANe-v3R4sQSo38e84KHULC-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
پاسخ جواد نکونام به سرمربی پرسپولیس!
جواد نکونام سرمربی تیم تراکتور در پاسخ به صحبتهای مهدی تارتار در کنفرانس مطبوعاتی پس از بازی با استقلال خوزستان صحبت کرد و گفت که «آنها از آب گل آلود ماهی گرفتند!» تارتار هفته گذشته خواستار برخورد شدید با خداداد عزیزی شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106270" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106267">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد
‼️
‼️
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106267" target="_blank">📅 11:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106266">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d37095ed52.mp4?token=BkM7vvies6FLs7tpJtIm0tqw_g1NFoQH9y9x9xCv9Q_7dvknguHylIvuR07Wx36U7DD3Vjk7ElpJWDZ45Kt87bXfNK2mZCy5AoOcuw_KtFIUG84bNdBxbdbbaDiC8RzdSzz7iiCKN4kcry9NdwVxODzBJJ3fR_V7cBxReCKfjZeUjU6UEpqVx0ytGgaEeQCowzT7flAF1nMCX9ms_QkLcCDAkwLKTnxD5r89vMkec_r2QVrR2UtHbB03Tqaaj5i6zjjxt6nmS36kPNkETWc4IyD3F6Jf22_GBMTz3LeL40XfRfNxr_mV513SIOPZdPdWXj7UTwhA2sOoOCc68xTLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d37095ed52.mp4?token=BkM7vvies6FLs7tpJtIm0tqw_g1NFoQH9y9x9xCv9Q_7dvknguHylIvuR07Wx36U7DD3Vjk7ElpJWDZ45Kt87bXfNK2mZCy5AoOcuw_KtFIUG84bNdBxbdbbaDiC8RzdSzz7iiCKN4kcry9NdwVxODzBJJ3fR_V7cBxReCKfjZeUjU6UEpqVx0ytGgaEeQCowzT7flAF1nMCX9ms_QkLcCDAkwLKTnxD5r89vMkec_r2QVrR2UtHbB03Tqaaj5i6zjjxt6nmS36kPNkETWc4IyD3F6Jf22_GBMTz3LeL40XfRfNxr_mV513SIOPZdPdWXj7UTwhA2sOoOCc68xTLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
بختیاری نویسنده و کارشناس اقتصادی: چند سال قبل من رو به سمینار دعوت میکردم تا اقتصاد رو با انیمیشن به رئیسی یاد بدم؛ گفتند ۳ دقیقه بیشتر نشه چون ذهنش می‌پره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106266" target="_blank">📅 11:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106265">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe7ae3e84.mp4?token=cnOPxv9he67PXJBCZo-nJhU2jgYE_Xbn04nzfmtRJB6-kU1uwKME8OF_-_P-mvgeNhsMLiNtXzVZtoOAEodhaEpM0NCBe7ZNKSSdgTq8H5Ku5wyLQ7ByyQIdA5fzm3Ab6bvc5-FVGPrxv0RLtKs2rLv1sK1WBfh0VeYHqt7EMCuWUmxtFb8gqIvGtVQuB8QetTFT3T9tHwrOXESP86gqTUZXFxBNBRvsOvuYUk4TCCcG6V1gxeyRzEL-jT09GS2Y7WPpwj_-RvkEHIyw5y30A22fDkkPgMTCjPytknAk8r-t-eHWlY8Yh_zWZqY3-ZI2eNwwWs9czic5iwexiWkAbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe7ae3e84.mp4?token=cnOPxv9he67PXJBCZo-nJhU2jgYE_Xbn04nzfmtRJB6-kU1uwKME8OF_-_P-mvgeNhsMLiNtXzVZtoOAEodhaEpM0NCBe7ZNKSSdgTq8H5Ku5wyLQ7ByyQIdA5fzm3Ab6bvc5-FVGPrxv0RLtKs2rLv1sK1WBfh0VeYHqt7EMCuWUmxtFb8gqIvGtVQuB8QetTFT3T9tHwrOXESP86gqTUZXFxBNBRvsOvuYUk4TCCcG6V1gxeyRzEL-jT09GS2Y7WPpwj_-RvkEHIyw5y30A22fDkkPgMTCjPytknAk8r-t-eHWlY8Yh_zWZqY3-ZI2eNwwWs9czic5iwexiWkAbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
🇪🇺
🇪🇸
کارشناس چمپیونزلیگ: امسال نوبت بارساست که قهرمان این مسابقات بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106265" target="_blank">📅 11:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba46a4ad.mp4?token=D35fAuO8ETvcza8TDryjY29gkQJTQdU_I8W4pu_vwyXkqh1ccXX_FS7UKDgzSZdSFE8u9fIbaiHRYc84TWkeFWaLldzmAQFIgtfNU_waSKzuhsq_QEv14-Fs3HGThQXtZf8Pbz6c6mINjE8G0pwx2OCLzjQQgc1jzRTR1iAv2cvF_SX1AMHejumaZuZXXqtwLVonYwXxaQfINgXG5qSx1EtxiKH5APHGJ3cNSLvc3HcSG7VAFKTllI6YAKiIkiuRYpkT0Z-27_xTeHMAKnICnBMqXzo7iIr0mGYAJHUAQvh-tzYwgFXD1ss0OexcfjMQlG29LgH83A5prscxA1eaSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba46a4ad.mp4?token=D35fAuO8ETvcza8TDryjY29gkQJTQdU_I8W4pu_vwyXkqh1ccXX_FS7UKDgzSZdSFE8u9fIbaiHRYc84TWkeFWaLldzmAQFIgtfNU_waSKzuhsq_QEv14-Fs3HGThQXtZf8Pbz6c6mINjE8G0pwx2OCLzjQQgc1jzRTR1iAv2cvF_SX1AMHejumaZuZXXqtwLVonYwXxaQfINgXG5qSx1EtxiKH5APHGJ3cNSLvc3HcSG7VAFKTllI6YAKiIkiuRYpkT0Z-27_xTeHMAKnICnBMqXzo7iIr0mGYAJHUAQvh-tzYwgFXD1ss0OexcfjMQlG29LgH83A5prscxA1eaSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هیچوقت این دوراهی سخت فراموش نمیشه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106264" target="_blank">📅 11:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106263">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d171b8e1.mp4?token=S-JvlhMJjzfH3rjenChpZiPOT9AU0ohZEzbrfz_DK9lNP7WtMWKwSkXZpB1q1dfN5jEHH3mn-Go-V5UvuxthTE4H2lCEvphRYTtQbuxF_-E20l_v4ozad86EUx13Xdz_HM-NC0nUfQpXVe1Hd_THcCToRc9NdHRaet9uVfpFtqwrNdg-z_Gw3XjDx1ubBXCGpD301IuHjygY7CTgSs0LNNWBaNLSyfspWa0aluHBgTJKKdF96b1PIsamHiu8-r9yTOGa6_1_XSOE-gKK0fnKAmQwQrDmV6KN5UB0rTyk2bWvoGg_opbiA85NK9vKahBQkYZhQQb2fSKJ8pjTMNBh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d171b8e1.mp4?token=S-JvlhMJjzfH3rjenChpZiPOT9AU0ohZEzbrfz_DK9lNP7WtMWKwSkXZpB1q1dfN5jEHH3mn-Go-V5UvuxthTE4H2lCEvphRYTtQbuxF_-E20l_v4ozad86EUx13Xdz_HM-NC0nUfQpXVe1Hd_THcCToRc9NdHRaet9uVfpFtqwrNdg-z_Gw3XjDx1ubBXCGpD301IuHjygY7CTgSs0LNNWBaNLSyfspWa0aluHBgTJKKdF96b1PIsamHiu8-r9yTOGa6_1_XSOE-gKK0fnKAmQwQrDmV6KN5UB0rTyk2bWvoGg_opbiA85NK9vKahBQkYZhQQb2fSKJ8pjTMNBh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اعتراف جیمی کرگر به اشتباهش درباره لیساندرو مارتینز مدافع منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106263" target="_blank">📅 10:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106262">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d19807ddf.mp4?token=VjRbdEpaq1C6r2X5IaqM_FdQZTCuIsTFO7oX6ZW7w-BBf_3VN9czNXEVp6aOJBm0VyWjtoq76P9vLWb2FFaXTRQyzYZSmPI3Y1AMpcEdORzIKt1nCR-gMd5Y6dl9_Ac0DJhxBiv7upqwudj_Eb0l5TImXhPg3bgh5U_1D8WQRvN7tDQm7Ok2x5340tjidOZXO-fMq9kTBaKeaVelVQaam4FFvySYVMhVsDq7kKIc7dPk_20gXacp0CMVYeBFYGRxV_nREKVp4xwYoYS4b_N1teGNefoijxtTGn4nIewT8-koTZdqhKQgwrzVc0BoWrG6w2Ak71fZP90Ig4_ohrDjvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d19807ddf.mp4?token=VjRbdEpaq1C6r2X5IaqM_FdQZTCuIsTFO7oX6ZW7w-BBf_3VN9czNXEVp6aOJBm0VyWjtoq76P9vLWb2FFaXTRQyzYZSmPI3Y1AMpcEdORzIKt1nCR-gMd5Y6dl9_Ac0DJhxBiv7upqwudj_Eb0l5TImXhPg3bgh5U_1D8WQRvN7tDQm7Ok2x5340tjidOZXO-fMq9kTBaKeaVelVQaam4FFvySYVMhVsDq7kKIc7dPk_20gXacp0CMVYeBFYGRxV_nREKVp4xwYoYS4b_N1teGNefoijxtTGn4nIewT8-koTZdqhKQgwrzVc0BoWrG6w2Ak71fZP90Ig4_ohrDjvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
جدیدا تو صداوسیما دیدن که مخاطب زیادی ندارن دیگه خیلی احساس راحتی میکنن
🎙
مهمون شبکه دو: زیر کونشون میزاشتن
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106262" target="_blank">📅 10:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106261">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد
‼️
‼️
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106261" target="_blank">📅 10:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31134b7828.mp4?token=UjLlUCgB9B-oYTD0l_Vm6ep7FF1GDskOYAbysuLorCpDH8sWnKNMApzYN4TPYbvbJYJZcSyGUtslwAguJ-hDI63cbj7Xkjn-NYWsDBZ-olyei6J7NS7xN3H3HCI067r4N1GZHPu6BTTyEg1CaCI5wWD2nVGMGjFe7Ht9Qzy8xqIxgCudPsNr9YkjuCDN4kuCtAKcXsBYTK2mcJb7PEAQGk4ZdujrqKsYb-7EJMcMoCVoDI_Vmg-FgmE8PE-2WP5cKy4uwkaO7ABzy4UdFhdmt2_LfpyHZbfgro2E7Ujg22cU8r76_WSmBUcZOfWhMBUirA9QD-TsK11cRmGUTKxy4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31134b7828.mp4?token=UjLlUCgB9B-oYTD0l_Vm6ep7FF1GDskOYAbysuLorCpDH8sWnKNMApzYN4TPYbvbJYJZcSyGUtslwAguJ-hDI63cbj7Xkjn-NYWsDBZ-olyei6J7NS7xN3H3HCI067r4N1GZHPu6BTTyEg1CaCI5wWD2nVGMGjFe7Ht9Qzy8xqIxgCudPsNr9YkjuCDN4kuCtAKcXsBYTK2mcJb7PEAQGk4ZdujrqKsYb-7EJMcMoCVoDI_Vmg-FgmE8PE-2WP5cKy4uwkaO7ABzy4UdFhdmt2_LfpyHZbfgro2E7Ujg22cU8r76_WSmBUcZOfWhMBUirA9QD-TsK11cRmGUTKxy4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇹
اولین‌حضور کومو دوست‌داشتنی در UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106260" target="_blank">📅 09:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106259">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0128cf1a.mp4?token=GitO_8roqwekndX2twt6dkS4IgddSeh83lME0FqVupdof5bO0CroNoH07vCGuvb2j0OL9lobOzNesD_dRjUYnRbtFb9X2P_ium7FOyxaoXhNNktAkFfH4w-QTwytEnBe5jIgETmzdELOKeV2EpTbk_eT8fqRWnTI2CUwdf5YolAk1eNUI_fuAk6HYrY7DV4KRrSBTZAaPjrpVeK766Y045hIXs4GRGdE4Ls5VZo57JjfLYnB9aGSbLGusQqpQgg4qKHm4b0aCMLEaWVPtXz24u85A2ov9B_BqJlnw3FYr9VOWUBfy3fZEorYRZ7Ciis2vw8R0lTs8R-kUqOlEGKQOATOays6_NYAtCLP4KCTusisr8ETxZAwoeZ4eL_PSOj1S8gY01GdFph5htlRcTVlUoIGGXWBUlgkZk7sOjtYcH-xyZ-DlYA4wcol2aXCha-UnvSC4wnV0mF3T6edb9PWsp-gJE56Ku8vii8t7fQNwGQgoMj5iG559sn5YrvkJ_jnEDJOuJkK3bgWFMPHC9a8zyhc0SwTQGfQ9JTngTtTmluYQbWzu7N15_ZcviY1NxhTiUNZOr81nhz6VRDC44GFsb2JNy9EnpF8zpswQWUbKGj8prQ4dg-h1hF_IBjLMw4rjVnu3IEDeXzzW3isQf3wJ6z2OVrFGx3Aj9yP9W7fUQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0128cf1a.mp4?token=GitO_8roqwekndX2twt6dkS4IgddSeh83lME0FqVupdof5bO0CroNoH07vCGuvb2j0OL9lobOzNesD_dRjUYnRbtFb9X2P_ium7FOyxaoXhNNktAkFfH4w-QTwytEnBe5jIgETmzdELOKeV2EpTbk_eT8fqRWnTI2CUwdf5YolAk1eNUI_fuAk6HYrY7DV4KRrSBTZAaPjrpVeK766Y045hIXs4GRGdE4Ls5VZo57JjfLYnB9aGSbLGusQqpQgg4qKHm4b0aCMLEaWVPtXz24u85A2ov9B_BqJlnw3FYr9VOWUBfy3fZEorYRZ7Ciis2vw8R0lTs8R-kUqOlEGKQOATOays6_NYAtCLP4KCTusisr8ETxZAwoeZ4eL_PSOj1S8gY01GdFph5htlRcTVlUoIGGXWBUlgkZk7sOjtYcH-xyZ-DlYA4wcol2aXCha-UnvSC4wnV0mF3T6edb9PWsp-gJE56Ku8vii8t7fQNwGQgoMj5iG559sn5YrvkJ_jnEDJOuJkK3bgWFMPHC9a8zyhc0SwTQGfQ9JTngTtTmluYQbWzu7N15_ZcviY1NxhTiUNZOr81nhz6VRDC44GFsb2JNy9EnpF8zpswQWUbKGj8prQ4dg-h1hF_IBjLMw4rjVnu3IEDeXzzW3isQf3wJ6z2OVrFGx3Aj9yP9W7fUQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇪
عملکرد درخشان اولیسه مقابل بودگلیمت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106259" target="_blank">📅 09:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106258">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a312ae120.mp4?token=ScYw7e4IxprkRt0I4GrXc2W0zU-K5nCP70L_AeGHSu6YkJS92mnSLInZaazMouZiqM1lhUTFGyh8U8jEWEjMFHN012sTVEYIcYUyv64MgfJ8JRdO4015soumKG40gkolWAPaVWrEcgy6eZLVXl46kT8v4s0BsFhVB3X5pyG_rPv5AZ53aLUon47AQsdbqjKr7HJbhMHioIJX4iNlEc4b4TgzZhQnXje2w3A8JcNyD79c1Vt2wNeeDGZDQCjvfU9_XEKk3LC1VyjYZoaEcJEBBdOAQjsmUkNuqcse3zb77V5c-TC29zkiEvmfsh1w--m2a7Bda13A_w80tXEIMVTRREoriiUFlpGcj3DF39fbYa7PkldklSySVsCAXviX-ey5VAlUqlilbaCznCX2XHXN4j7V4WMBI6G-xe1rKp4-t9eOxaqMgt58j_-kggMRhmEBKotflM_XMQUTT2NqjibrNEeQKCkn1BQajgXNp-9QYNvWlKW4ISCItnoQ6HCFs5qtDQ1qFH84lT4l4DTPA496l-F5VMQ3cCpXX8Z7Hw-bR5E5YXn3U_KGzjUVUpXtMZaSsET4C2ontDKSO0AEvUnwa8EgRB4nyzm7e1p6G83PJCHdJPnF8Y93UkUWnJiU85Br6-m42uU0jePWweToo4rogaBGj65N14wI2g5Aj6JCsB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a312ae120.mp4?token=ScYw7e4IxprkRt0I4GrXc2W0zU-K5nCP70L_AeGHSu6YkJS92mnSLInZaazMouZiqM1lhUTFGyh8U8jEWEjMFHN012sTVEYIcYUyv64MgfJ8JRdO4015soumKG40gkolWAPaVWrEcgy6eZLVXl46kT8v4s0BsFhVB3X5pyG_rPv5AZ53aLUon47AQsdbqjKr7HJbhMHioIJX4iNlEc4b4TgzZhQnXje2w3A8JcNyD79c1Vt2wNeeDGZDQCjvfU9_XEKk3LC1VyjYZoaEcJEBBdOAQjsmUkNuqcse3zb77V5c-TC29zkiEvmfsh1w--m2a7Bda13A_w80tXEIMVTRREoriiUFlpGcj3DF39fbYa7PkldklSySVsCAXviX-ey5VAlUqlilbaCznCX2XHXN4j7V4WMBI6G-xe1rKp4-t9eOxaqMgt58j_-kggMRhmEBKotflM_XMQUTT2NqjibrNEeQKCkn1BQajgXNp-9QYNvWlKW4ISCItnoQ6HCFs5qtDQ1qFH84lT4l4DTPA496l-F5VMQ3cCpXX8Z7Hw-bR5E5YXn3U_KGzjUVUpXtMZaSsET4C2ontDKSO0AEvUnwa8EgRB4nyzm7e1p6G83PJCHdJPnF8Y93UkUWnJiU85Br6-m42uU0jePWweToo4rogaBGj65N14wI2g5Aj6JCsB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
داستان جالب منیجر ایرانی مسعود اوزیل؛ مهدی کیا: پدر مسعود اوزیل باعث پایان فوتبالش شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106258" target="_blank">📅 09:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106254">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAqqxJ356JdMJcEcoE3Ys3COw3ZSij4z2A9m4zHRTQdpKA2rRR6JbD6qB2xhT_pwBIESRK8ZLeBNcYD7iWZ4vwNihLfeOlH_ICnkhgv_1mHa66ic063RxCM-6mQ8ihGR_n7Awm-JREVb8l0mQassExa3cJtginuOW_D732JIjWI1YzNG0qj2bSWai5Y7-MDwd8W_1IEb1pbMsU9UIU2eGa603nbmTh-a9vOP4nsUyz7aEA3mLWMvJniLVffTHO6pQsgr9b1Uv643_8Pab9kwCQylFKowlri5Njl0gm--mbqv7XEPSgdQwWOlvH7lHenDWyx28qVYEVvADFKEVaI3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
✅
🚨
کیلیان‌امباپه:
🔻
من سال‌هاست که خودم را بهترین بازیکن جهان می‌دانم اما اگر در مراسمی توپ‌طلا به مسی یا رونالدو می‌رسید، اصلا ناراحت نمی‌شدم چون می‌دانستم آنها چه بازیکنانی هستند. اما درباره سایر بازیکنان و کسب جوایز کمی تعجب میکردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106254" target="_blank">📅 01:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106253">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMC53DmPGaxC0H3PAYDGutkBPB3rHIu0YhnA3jInaBULFQiJCFhFOlB9pdYJ2qdMxZNgVEhDM8WgxduS1kjP-pTuWoFQsafz1HpV8H-r3yUE83sYGNM_QIkmrRGHo9xwQtTeTiAbvYDbFlA3gGa_oP0D2PAT7fq8wOlKpCsO6_ZVNmD0yrDxRhfMlLW6ci_Qwg1TT37VuqXB9E2-6j265GxyvEE2kpgreCcNSs4sjUAiDXuzOngF2jTmx7w-GLOErmusef97AX60eu57az1UXgcwvRHUMekTght2lO_H6ZjB6n3uOm22mEUILzUfAswnogb786UsePU6cRx-d5hkrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:  اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106253" target="_blank">📅 01:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106252">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PY1RgRgSAdqel0tVJ4ds6nVgwnwGGyFlSK7bHf1zAkbx6GRtJP61SnA5JMoaiWEcZXiUKQRX7DToTbQxk6GQTIS_OdLb-s_Yd-P9uble-v2Jw1cvcHd6HZrmmqfOnUpG139O7-uRXYHqOCejB9o8RUzDf1WdUA_BSxjuRiJdipj47oAZoffDypbcrtZqysItZNMEdjotUo4eQa82A0MeZMvOkyEpuJsus2H3HWdfnx9rFkz9b5vLylSyBXW8xIyP3Kk7g-uMVWR69J7ei7C_ovOLcD_wvzHGHkXombAmm5OzsmA1TKVed0xlmDp1zpBRKpcXsjSmbEGOxH1k9eMuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:
اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.
🔻
او نیازی به فکر کردن در این مورد ندارد، چون هنوز می‌تواند این کار را انجام دهد. ضمن اینکه، مسی خودش یک بازیکن فوق‌العاده‌ خاص است.
🔻
من خودم را یک بازیکن متفاوت می‌دانم. اما او هم یک بازیکن متفاوت، در بین نسل‌های مختلف بازیکنان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106252" target="_blank">📅 01:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106251">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0rkcu1uQLmn9DtAwInGbF7KwQkLqSOpHH3Lxtw_dga0QafAwf8gwo5spdZwVXU5PXO2OCQJBjJEbrE2PdOE3-VUJMf70EQi8hGYOaj6TjkqF34rzwZIiIiYaLnTB15ZRHIeAxY4dPuBkfKIqTVGC_rmBVkHYnzTAb1jDG3lZJZB6Mjjx-Dom3Yfom95mmgvusmuExIFbUYczj808RHNSICtJeRKloe66N_BapHhVmKTJXilT40TFxxj0wLdps9QicnS68RTQfRtk8METX2H02Scqd8soILoPMfbw7VV7hUeUoIqBJs1-HQ1FT4bZc4pYz2ZZoupxvFsLYsCo64RWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😆
📱
استوری ابوطالب‌حسینی: ما نبودیم دیگه تو فوتبال حاشیه نبود و همه پاها موازی بود دیگه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106251" target="_blank">📅 00:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106250">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=RPLAcn7dBZKrA4o4FOxGLlNAv49mLNULdLo9MVLmtmItp9OTc0OiU6qv7AwBK2yIdKcG8euXYO-zXDeZsAEIBKWFOXDkmlEYH2alMTxTe6moSGdmz4_eMVfZv-z5S7sh32AHq5HNDhah6hHrc8r7Nuev3nO8NANsOCLiKSLzlCV65Pa9ZwBN_jK6tBWPSN1sON5wWtddxGX3YN2ftiq9lpTzX32b4ibLl-_HQxb3Ncp0A0ARgsj9GJO_rI5tu3e6KgoTnJ6V4D1D9N1pdEAe9SuWAHvdh7Vw6m_7V9yFElBVeNL8t8Gn7ESNgR3rHrD0qLrvzegANER5jphikI26kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=RPLAcn7dBZKrA4o4FOxGLlNAv49mLNULdLo9MVLmtmItp9OTc0OiU6qv7AwBK2yIdKcG8euXYO-zXDeZsAEIBKWFOXDkmlEYH2alMTxTe6moSGdmz4_eMVfZv-z5S7sh32AHq5HNDhah6hHrc8r7Nuev3nO8NANsOCLiKSLzlCV65Pa9ZwBN_jK6tBWPSN1sON5wWtddxGX3YN2ftiq9lpTzX32b4ibLl-_HQxb3Ncp0A0ARgsj9GJO_rI5tu3e6KgoTnJ6V4D1D9N1pdEAe9SuWAHvdh7Vw6m_7V9yFElBVeNL8t8Gn7ESNgR3rHrD0qLrvzegANER5jphikI26kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز بازی استقلال و پیکان توسط تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106250" target="_blank">📅 00:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106249">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB8PrJdIHvNRlPYaK1dtG93c6sQxWer6GXXT8WdNU9UK4FRQRw929uK34eCzg9es0qih6z_BEoAIcgs8OR2YB9tx3PlMfRBm-lxMGS1Q2z1GxdeQhiHeHQv3tb4cEg6I56IumjuF67pJMd92-oEBay_ioGWbx5JJG6QV4ss5uTa3GRiInDnzcsxvNx2G1fBoKaO49jkRnxRtzCbsD5CR1otzBfl5fgClkDTU7hp5KxkHa5bXrbCTdWhiyxNwbkx7ZEfvATmvRwLDfZ5m7mfKb6jQOUdZYD0bDxLlHg6EulFM3ar1DiH-cSZjVTmlH6uBMNrUvPMdlCESEKfdFpAHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/106249" target="_blank">📅 23:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106248">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T441KndtdCL-q9f9vN2gRn_3w_G3ZGH3GDOlrnHKUzor5l-Dvtfs4L34N_9ViggG2nm3wmScDVctp4A2tB1I2NHhQdmNUBmDsufFrWg9lJrsNa8J_lLYHeVzQSHuroB_2ZROA160_JQ-4zj_zCpW8mPfkXPRhpI_kAbMssoMzVLtBl-cJGP9osjPClAECY7g_AMi8rYLyeyy9_qrL14_Dr3IAf6SCuoeXOYR4bGUdW3Xex29DtFOjXlekzWz2OIdCS9B9yKBkLAOvM5DgtGphYco6F2iuzfQ6RytprvkNrjW72JpGsw0O314W6kkOJI1uXVYew9h06J4UJe3AEIW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/106248" target="_blank">📅 23:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106247">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=UutTy8FjF9cUDW2aoIlqfDZV3vjd5lf1JK--cf8Sg-exJYivS6FAnR2awcmAeBoB_APIxgDlLQgRq6-sQ50EuGTG0Mgktq5Wnc0CGwuohn7i9wYcrC1Z3O2zWeb8MkVL6AQpH4PIMZGzlc2t6UB5S2sTjBc01pXiTPWcPphWSOkcVlh_AevkD_woIuX96qfpYaQhJaNaKglOuu18WU_Ls6UgeDCyqjhT5FCb0Wu8Xa1xuI0FKKulO4aIjuVrUaHzGNAZifLUt6pGTn21P1zhxx4Pcn3okbiBSiIkeiUyBjboP7pbUlflVhQkTsxvUsbCaZaLB0xS2Dl7uoaJKKT66yOuGUn4OCZ2Q4VAdJDwDOP8An7AvEhP-DYavUC1FXwEESVEHVTsOKdkiOc_chPM5AO4Ehi_blUnOtpZA0Pgong4Uo-wZXWnYTWuX81Ejha8NlxxYK-HLR2Xq1zmfHeUWblqoj62Dx5A3gx0kOFOXC9v1zsHnb-Eb48hdfqM7gqUoPuhP7XB7UO4u2Lb-rkrkvADN3-u_udjh_JnXyUq73lbJmfnT6VOnpAzQloBZrs5XicTDqSWzjRExTttjfmXrIcbOp5lJ9IYlJXKRINU6fVaNvQAZ3kNVvn6ykddtM86YZNlyoc4LvXy0AZ5DimPUt_CnxUWUBtvwHzTFPAG1Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=UutTy8FjF9cUDW2aoIlqfDZV3vjd5lf1JK--cf8Sg-exJYivS6FAnR2awcmAeBoB_APIxgDlLQgRq6-sQ50EuGTG0Mgktq5Wnc0CGwuohn7i9wYcrC1Z3O2zWeb8MkVL6AQpH4PIMZGzlc2t6UB5S2sTjBc01pXiTPWcPphWSOkcVlh_AevkD_woIuX96qfpYaQhJaNaKglOuu18WU_Ls6UgeDCyqjhT5FCb0Wu8Xa1xuI0FKKulO4aIjuVrUaHzGNAZifLUt6pGTn21P1zhxx4Pcn3okbiBSiIkeiUyBjboP7pbUlflVhQkTsxvUsbCaZaLB0xS2Dl7uoaJKKT66yOuGUn4OCZ2Q4VAdJDwDOP8An7AvEhP-DYavUC1FXwEESVEHVTsOKdkiOc_chPM5AO4Ehi_blUnOtpZA0Pgong4Uo-wZXWnYTWuX81Ejha8NlxxYK-HLR2Xq1zmfHeUWblqoj62Dx5A3gx0kOFOXC9v1zsHnb-Eb48hdfqM7gqUoPuhP7XB7UO4u2Lb-rkrkvADN3-u_udjh_JnXyUq73lbJmfnT6VOnpAzQloBZrs5XicTDqSWzjRExTttjfmXrIcbOp5lJ9IYlJXKRINU6fVaNvQAZ3kNVvn6ykddtM86YZNlyoc4LvXy0AZ5DimPUt_CnxUWUBtvwHzTFPAG1Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کنایه‌های تند وحید هاشمیان به حدادی:
🔻
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106247" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106246">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=B5rhYNlt0xBmgNpMUQhcdisS2BdV78PVHOSBuTJcYzdhIUQFAbWToC2Sw-VBwd8V-5IBDia4RvlbD0OL_f25lSCI_Oj7Qqcd3YWXlGKGrp2W4dkHoOovyOx6CoWwLemcUR33acaX-71GHEtyajqLy-97-EBOWWKjIsY53G1_qzI0R0j_j7utUX9_87bAdV5kVC9GIZfYZUbjt2wOvcH3MKcRWQ-KaOb5mDJclAUkKTggqDtmLUq8HD_duhcnyo9zQcLNz5JCr-MV_WqlmcEkhDkcv_G-bgTajj-ou0bErZMW6UV3w-vDsfzuoDaKBlaehITdRZfmF-Mw91DJsLACeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=B5rhYNlt0xBmgNpMUQhcdisS2BdV78PVHOSBuTJcYzdhIUQFAbWToC2Sw-VBwd8V-5IBDia4RvlbD0OL_f25lSCI_Oj7Qqcd3YWXlGKGrp2W4dkHoOovyOx6CoWwLemcUR33acaX-71GHEtyajqLy-97-EBOWWKjIsY53G1_qzI0R0j_j7utUX9_87bAdV5kVC9GIZfYZUbjt2wOvcH3MKcRWQ-KaOb5mDJclAUkKTggqDtmLUq8HD_duhcnyo9zQcLNz5JCr-MV_WqlmcEkhDkcv_G-bgTajj-ou0bErZMW6UV3w-vDsfzuoDaKBlaehITdRZfmF-Mw91DJsLACeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
محمد تقوی، درباره پیروزی استقلال برابر پیکان در هفته هفتم لیگ برتر گفت: «استقلال نمایش خوبی در این بازی نداشت اما باید این بازی را می‌برد. خط دفاعی استقلال آشفته است و با این شرایط در بازی‌های آسیایی مشکل بزرگی خواهند داشت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/106246" target="_blank">📅 23:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106245">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=hSj_OZoBlEnKxrIVT1yT2la3mYWtmTSNIlpD2_y9BF6H4H4c_8agbprWlMpMdW8lJA4u-BCrDjffRIV68NbRrDhyuYgmnHqqHDkeqT3hegDyzaSyTqSM_yzyuCkHUSQFN8gpBeyIrN-iXOaiAFSomM3x7bkPCHD3x3RonD2IuHQilP5SvOqP-hLzWCKlFuUaf94INeWBUgrEXnBwTC5yd4dePlLLYqNV3NnTfpb7XWP-pEJ6bh3t9SLgzkTvXFlNaI2YSEplRi6xXOSGYsvMZmm9FZEop9GJhbItYKXJ8e-e6X5z5Ypg98xKoEpN12RUFFeh3iDFzR7y1Oi2nGcW7mog5NPgHyyStum6S-eWXhZQjX_EiJLvWwDCxkzBR672J5wcgEZxdZ_UmLfIqrVXs-WKwSwl4O8BJj4xUurVuCbIak8SpzWE7-GLbbs1_VmvSMMq-qvHbdYsm0N33LNpfmg4Edrm6vBLxPGJTAv9fUHmG3saZAO5lzGC1MT9DSlL2kCjbdZ5w6vvjt41oBZ5LlqxG5cK-wLIpN3HV15KfdagDhEQL4rSAxjhkAmX10OLlswngdgGeeIEV0VFfOcqS4RvAesW5WpFk0lUplEeTSjQEPI-y7x5WDWlUrJCgTo8xQexvbHl1cJvFTNmjqQWVJS_eZGmcM16_w3Bij0sRuE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=hSj_OZoBlEnKxrIVT1yT2la3mYWtmTSNIlpD2_y9BF6H4H4c_8agbprWlMpMdW8lJA4u-BCrDjffRIV68NbRrDhyuYgmnHqqHDkeqT3hegDyzaSyTqSM_yzyuCkHUSQFN8gpBeyIrN-iXOaiAFSomM3x7bkPCHD3x3RonD2IuHQilP5SvOqP-hLzWCKlFuUaf94INeWBUgrEXnBwTC5yd4dePlLLYqNV3NnTfpb7XWP-pEJ6bh3t9SLgzkTvXFlNaI2YSEplRi6xXOSGYsvMZmm9FZEop9GJhbItYKXJ8e-e6X5z5Ypg98xKoEpN12RUFFeh3iDFzR7y1Oi2nGcW7mog5NPgHyyStum6S-eWXhZQjX_EiJLvWwDCxkzBR672J5wcgEZxdZ_UmLfIqrVXs-WKwSwl4O8BJj4xUurVuCbIak8SpzWE7-GLbbs1_VmvSMMq-qvHbdYsm0N33LNpfmg4Edrm6vBLxPGJTAv9fUHmG3saZAO5lzGC1MT9DSlL2kCjbdZ5w6vvjt41oBZ5LlqxG5cK-wLIpN3HV15KfdagDhEQL4rSAxjhkAmX10OLlswngdgGeeIEV0VFfOcqS4RvAesW5WpFk0lUplEeTSjQEPI-y7x5WDWlUrJCgTo8xQexvbHl1cJvFTNmjqQWVJS_eZGmcM16_w3Bij0sRuE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
کامنت‌ هواداران پرسپولیس زیر پست‌های السد: قرارداد آسانی غیرقانونی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/106245" target="_blank">📅 22:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106244">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=iW1yiU3zMBSrozyELOJ3Be3xaINJdP0zXFhfinmw0g6VqIqMzlSZGvt-udz3wsNbmqCfzfzHQrgPKscyozdnQClBLeHbifURMuZkpdUYXylh5o5hscS7-6-aSgyKsuHRRhcBsdQXkLA9LBI6BddCm05AlPsonfgX9xI0qrOjx8fh7BX7GuYBASeWuw2vEQzgwb3Jt_rw7qh2MbJLq70nZ4oUyoAlccTKz01mNbgSvVX4shgDNxkFbOg3no4aObcOBCts-5z1X0zAgXmb09ISVTtcu5_do8wwZBwBzThiel9x4EpIDgERg46buZPK09o2FkD4yQiQkwoLZjQFAJyWwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=iW1yiU3zMBSrozyELOJ3Be3xaINJdP0zXFhfinmw0g6VqIqMzlSZGvt-udz3wsNbmqCfzfzHQrgPKscyozdnQClBLeHbifURMuZkpdUYXylh5o5hscS7-6-aSgyKsuHRRhcBsdQXkLA9LBI6BddCm05AlPsonfgX9xI0qrOjx8fh7BX7GuYBASeWuw2vEQzgwb3Jt_rw7qh2MbJLq70nZ4oUyoAlccTKz01mNbgSvVX4shgDNxkFbOg3no4aObcOBCts-5z1X0zAgXmb09ISVTtcu5_do8wwZBwBzThiel9x4EpIDgERg46buZPK09o2FkD4yQiQkwoLZjQFAJyWwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سعید فتاحی رئیس سازمان فوتبال استقلال: به غیر از خلیفه و گودرزی در نیم فصل هربازیکنی سهراب بختیاری زاده بخواهد باشگاه استقلال جذب خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/106244" target="_blank">📅 22:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106243">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=OKH5FCjwYsNvJSgDjKYbXfarP-T5xfcIbjydEb8vjeKUubrek_zDRuCIxQlr_KOJzpip-Rji8_-6DkFyZ4sUMxAJu2OQOI4FRf-LNjfkxx6QnrcG_KsFdjITMoJXh7aCaO2meL9LGwvyEClLao2uGLFJJKPlErG0UcX3LQqh_gUPKQLW76WL-iANfr_nD_1XgaVkBjD5dxTSJlodEvztOEAA5rdsmvvXWGvpjXHglhS-Q0_lOd4Y7pppMtzTVeA2TuSbbwQUDet_1BfGxRqiPo1tbo2UWJpBm1NbPqyvEf3T8MrIaOZDPjXuABWtwFJXCZrSTZ_OxJvuwPh-1GSZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=OKH5FCjwYsNvJSgDjKYbXfarP-T5xfcIbjydEb8vjeKUubrek_zDRuCIxQlr_KOJzpip-Rji8_-6DkFyZ4sUMxAJu2OQOI4FRf-LNjfkxx6QnrcG_KsFdjITMoJXh7aCaO2meL9LGwvyEClLao2uGLFJJKPlErG0UcX3LQqh_gUPKQLW76WL-iANfr_nD_1XgaVkBjD5dxTSJlodEvztOEAA5rdsmvvXWGvpjXHglhS-Q0_lOd4Y7pppMtzTVeA2TuSbbwQUDet_1BfGxRqiPo1tbo2UWJpBm1NbPqyvEf3T8MrIaOZDPjXuABWtwFJXCZrSTZ_OxJvuwPh-1GSZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🎙
نادر محمدی منجنیق: به صورت اتفاقی این نوع پرتاب رو یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/106243" target="_blank">📅 22:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106242">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/106242" target="_blank">📅 22:24 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
