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
<img src="https://cdn4.telesco.pe/file/YmTo2vbAPHUs7Ewjf6wBukuQeCaUV89NJIeYhmJUo--oOPAQcqZE_bHEkq9N95BfLo7oihm35V4OW9a1IsQ7qFTV9uLyk-gXgEucPMxjD63iAnUaTUlZ_SvUpVCoGLhNdY3yYLZ6FZep7Cfry18RsksyP8OnT__4BdTIcjlrlTPufg_F2MEmx4QLjSuDUHg7L_yz-ZQfpY14wgtHZHDQKd71is4YrEusYhgT4QeZa2CAavrrEVu13NAaM1CGPSPQVGWTLXAhaastMlCQ8n2KVJIdcyt2vl6N91GKVu4zbXrDTHUcDesjA2j3oaC2lE3KmAKbA9vY0HaS7s60wPy6Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-30855">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2DqSfA507iYFmVsQRnOzCDeGzu0BIRJTsqYTmQAcNFdefOIBPOMmr9bKid9BEqq4TzgdDYGC3icSLUJF83KO8lhoVdR2ScSaGkkLSvQNzkFu50T0lY2Jg8H8BmjrjnLpjGMNMvbybZlJpljUMGDAaA1OQabNWRmr60tA7tO3y58aQZC_zGuwzVpClAOSQc2nbLQpVUi1zT5lcePP89DyCjwrFAc6ITsujswtKGFwe485adPLIzwehu7rdO53g5GNsunHRvo3T0kqm9cJisxkt0ADLvMKNiNkqroI0OdxlLoFBk656Nbzv044wyARC-zx6XvgXPBRUSunvETSH5xOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
هانگ کانگ در شمال نروژ، با جمعیت 2484 نفر، جایی که خیلی سرده و یک زمین فوتبال زیبا داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/persiana_Soccer/30855" target="_blank">📅 18:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks-YBdptQyimX1T0srG6d1zTiVl0vGSVFrscuva4oQYqeOL6wFYzJk3B9193tijlIMOtX2k3FEXaOrhAvjk85K7biv8w8tGOM__O5h5V5DC_1mdzpWKLrm3p_elIeISq6UBRxZnxYNb3HOBvodNx2CfCHgsnCBbKen08jM9FR6I9XV9QYfq9tOXsHaiPvnV8HF_ChKo9DCS4K2HYLZZd3Yqcg5ZYsT7FafpPj8XYIoGhtjGazdaZgICWE6sdkQWSNwFKmTsqKmVSaDCyBJ6OAuXlWgiQjGOzXEPX-HBWR0VitV4qmGyBQIElp2lyYUoEPUI4we9GDdlOqs8WHP_riQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/30854" target="_blank">📅 17:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVZ17Fjeo4ryLZGvRwJ058HTG7GjbRaRGgKqF7XZrrTtPGtoQmWiNp7IblkcjWloKTVF7OvjLCNJH7beTvSIfkOdJqltlLkeUfA6Rj6xZnDzkVLgvekpubkUvqASaOh3-iA7m_bfyJ8AaOwK29Cb6kVgKcL6jjYpbZQyjpEzEVf8gnhLnQ8_QkYZENVu39v1J2W7J92d0B50tHqysTFip4tdY8bwLl0PT7BRGj2LTPpGDn2wRhqLZhsG9GtO4TP9d2_K0CRI4AnkhYKzN2Dwi1RPerxUeYH82PT27LAW6qPvSaXgpAPOEhTh_WdeAH7ojOrV16-_mEsr0wBzaerw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/30853" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30852">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUvVWhHGSekgypz0utF-3YYUhU0YSh6LLBcrusjhq7mCxppbHcFDgZtRRjxNeVTyt4NZ-T0WVTQnvOEvUZo6UzjVYfCngS00NgBXLhY9OMbNgOEiwRICSXZSkOuazJESn4AJKz5Tt-EgfZ1zAmBJcBbcd2MugVTu6JhgCzMl-sogwJbbi8g0LyVUnre8v_iR40BcZBxKKuybX0dcfDCEgxidVZP5UouZtzov6SRKaRyA1Q9v5T87uCBPFC3FX2JjkdODYSQhopTAQ29wWpy_cbagmCDljeHC6zkG3esU9lf27S2_shsD5yPXiO5sDIKHqHbxQYBEuGBdQwtTi9PDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌مولر درباره‌بازی‌معروف ۷-۱ برابر برزیل:
بین دونیمه تورختکن‌ما به هم نگاه میکردیم میگفتیم چی شد اصلا؟ یواخیم لو بهمون گفت نیمه‌دوم کارای عجیب و غریب نکنین. نه برگردون نه دریبلای اضافی نه هیچی. باید به حریف احترام زیادی بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/30852" target="_blank">📅 16:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30851">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGyZ3Qd511nBD6YZvkZuRJLur0bTua236lKplKjhfRo8UaebhmBKQZvqplasoFTW75Xo2CZ9JCpK-HxvYvA5WY-iAwHdqu5Wnrc2dGLtkfM_LJXNjTSo1y9KrxAE6IVOD-YcAxNiTy2sUPTkkx3dk8IxEqQ-rHadralg9U5Cyj3HcidDIlZMOMloYXsrnXc5ubkMPrCY5xovU-_cUytFo5NfNhrZxJvvlett5YIGiz6fOO1zGdm_Z2KG36UeGNZQjur7rCZPaDmB_u91OgO1k-3WeH5zSwXSXggx4lVFXK3d1469ulVXCLt0arZFvngOcEieUECnnE6HUjFWZ3SS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی که گفته میشد خورخه ژسوس در پایان بازی‌امشب‌برابر دانمارک درباره کریس رونالدو خواهد گفت و از او بابت‌ این‌همه‌سال حضور دراین تیم تشکر خواهد کرد اما او از هر سوالی راجب‌ این فوق ستاره پرتغالی طفره میره و جوابی به خبرنگاران نمیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/30851" target="_blank">📅 16:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30850">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqqSF1I-aYsevE5Qi0_OhHwgIBV_kDGELgwKWOg3uBVP_3ntEPJrN0irghcCKqw-eN6CxPVvWZT9SNvUwLpIUqBZmksEO9Pe_NpKT8ZRFr5KvMNbSaqOULEviPEyeMAW1zbW02v3UOSasCALA8-nWrjUdaCXiQsixdPGf439xzDhpOD1ORRwZRriQ-mVRYWPbeG8h9i_s0a-A8JhUUOpL5fW_gNRa4miOPWKBnXgOVJS1zo-hLr1i6s7MoV-ImzByJK8i3se__SFUmQrpeWKNcKz6qGsyK_UJV8JE6ihktBKXT-zp9ZWD7vEBri3Hc3IjEdu-CZb5pmnTdqPFrThIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت‌ جدید ایلان‌ماسک:
اینستاگرام فقط واسه دختراست اگه‌پسرید بایداینستاگرامتون رو پاک کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/30850" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30849">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKV4EWsFiGQn6rF31W57fc3MNmtj7RJWK1R2qDu-5S9uGYnJZ65C9JT1M-EtXt9h8rYu1EiYzuD9oiO-18-nyEUIO3izNvx0sVXkSh53wMuMTqNoZyulRaSS3COCYOUGvfPecr9Vyq3JzMCCCdbG2VOrwsn4pyTcEpMDtXBFE6KuqMvorWTYYWJySzv_ZgrH3P_w2u3srns_G6EsSOSg1DFg9JvYQvYi88jDOj25Vq1YD--cIE-Fgcfgg5hJj_BFbKDST5QDHIRyFZquN-3unoiBoI30M2pB5mZzoz9nGDay5XmUJWo-iYcpDjUhtv80p-8TXbJ-rFnqUWS-UlLoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/30849" target="_blank">📅 15:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30848">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4PQTd6peyOG953AwLECHhCEtVr8r3v1g9DLcIoxuG7WVR6eKnI-GvXLTCmoCuQt3tzR_SrpwmMo6wnVR6l9pDfJRWFBMTK9Hobr3fwNR2W5nckUycF8lXExFBzrC8bjk-5wseqh_9KrVLgozWsbRo898kimLcNPAta67tIv7QNn0XbZWPrlaG5f0W54cXz2GDmxVGgD_7VCBUennMw26wx9DRmrfoR1twVo2Kh5pVv84be4SVh6TZtiZjm-AaBxOkc62pr5ZS3FxYWtTHilH7Rt-fQasQGgVP-wi7pXF3mjPFZRk3tk8j9Od3KqIGOZ0NFXHsxe5SFKB1t05I4YYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇭
روزنامه AS: باشگاه‌رئال‌مادرید گرگور کوبل دروازه‌بان 28 ساله تیم بورسیا دورتموند رو به ژوزه مورینیو برای جانشینی تیبو کورتوا پیشنهاد داده‌اند. درصورتیه ژوزه نظرش مثبت باشد فلورنتینو پرز با دروازه‌بان سوئیسی دورتموند قرارداد امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/30848" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30847">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tloNP8aI9b1M1eTiU50Tdsvi43DIOisPJ_V3NlKXDR070NX1sHDlon52EGf34LQxTD-5zVAuk2N5LtLe4vzfmLFnmgw_yzlmv32WG6_VD5QqawajhLnbWLQfuojhdf1Xecox7MCHSCEH7MWAzpV1YVNRgllgT4A2kZwz7-EIObWh2kInrnyNtHUqmIdaGNUhPxWs5FUmNtnpKfbuv5OYSWcmKAdKIe2ka216gAhSdVzrrYDwzkx1PtSwbRj1hhi04xUtv69McySZzWdCyBvyA5cqh-WfUC9UQM7FEuncL_qy3XkfmSvkxYTlr2sf2ymG7a4aJGMbOB53P6duNjapcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دانیال ایری مدافع‌میانی پرسپولیس به دلیل مصدومیت از ناحیه‌کشاله ران در بازی اخیر تیم ملی امید سه هفته دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/30847" target="_blank">📅 15:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30846">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE1CY5W_G0eTQkjy3BmpKPyjM1q74if4vUiPIWcr6fNLR22KXCzBTLC3EWGZruVMqupFgLgVLIsOH9yvQaEWWuVePTcB0txeiO5BmIuqYhSnGNGDO--y8IpF_ROYaYEPl2pWBv_aw3hHdIg6jVzvDhPREx4oFD941DuWY99SUd7H055J5i5yC_PSBnKIB1dhYyy0GCv-2iUFG_NX-Usc-gGyGwivT0m0flXbIgr8G6lvvUWLpB0YYeqLNC0M67qsfzu7bpKQl22070JWBsyEeIQu5rb_0IufTB_UTtMyz4YAqmHb_1b33NUComIk2qGWIfTI1pamPa_30Cn1dpJc8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30846" target="_blank">📅 14:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30845">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PP41Jaa1zk_izOdfdAAaGEOIMITP7jjirajETkQbIgKl7MlhVww6gBKDoIeXyAjfxZ0keoYTK2OFaVADAkRlx1i7WvNtR53CNqvKaTILmqM7zPtpFQ-GSEtQeaQ3UypIzoCkwSF9KRrILW0xmof1l9HSDMesdkmE868E3nY3YfzgE8Zq7ceGYy4QjcinycIRTPlONQQHkAdZU2EeuJd66rLpsxCP8G_oy5w7C_fe4GFIaoxhzYwql-WD73STTD9MaSRIxmuhqGmY_ZrdtRiOEGNWO61cI319yrH3iJxsbAeH_C5FdO9oX2OQlmDNikTWmFah4UgR8cU2YMiS9sCjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه پرسپولیس؛ دانیال ایری مدافع جوان سرخ‌ها در اردوی تیم امید دچار مصدومیت از ناحیه کشاله ران شده و چند هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30845" target="_blank">📅 14:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30844">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=l3QzzTbzkQ9MS2X6t6kjdAWuaWUBYcfPSfk1JIULSvxzFNZBfuYKnJXipCHHBOvlFltz8AIkBgDf9PuhOyfpjMRv2CJHis75Rs4bxfepGXANEDYvda8B61SMhUfyZ0YkzbK6UqFFWLPfRAFMTYr4312G0sc-1U4ymQYNr86j_AEXmiEQ49hwaqt08M9aOD6zIHFC1cQ55SlDfoEbvkDYOCyLTtwvf2m_ddmpkdH4_itmcfF4lXaaxPEqgbD-_iXjMcI9FT_p-sCYd59DG4GGZAa-gkHxO905Bwi6CAQeFvxvI6FXhBNQvE2NTxBppaCULG_uoOpH3PhpLnhdrPRu8XcY-XK5wLyHV9xv3cj02w5xzfMw0JBEzc-UEejqiIM52byEp1_fWzpFAYsI7EjfxzNQjoy5uh8OFvTGIhoai2bd6Vp0icgNYgNquPzPEjXJeE9E03ptGd73eLOP4yT1Ct1FvI8Tt9fyiKJff4Y-iLDeXigJ8Fo8QJuX7ZtFNRWXFLrhQIAtkQtLymQF-rOG3qwHsWaNU8qJe4s8jUQqr2LmHZdjPKqwELKUDlwJ3WNPlY5xIp1FR49escu-ZLttfLNs4NkQtdKKNdBH3F53FjtDUzNpQ-FHnU7tUxL-hTFJVph4SQUMz1OrOkZW2Himai4nM3UfuHpD8Q6Izv6V1rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=l3QzzTbzkQ9MS2X6t6kjdAWuaWUBYcfPSfk1JIULSvxzFNZBfuYKnJXipCHHBOvlFltz8AIkBgDf9PuhOyfpjMRv2CJHis75Rs4bxfepGXANEDYvda8B61SMhUfyZ0YkzbK6UqFFWLPfRAFMTYr4312G0sc-1U4ymQYNr86j_AEXmiEQ49hwaqt08M9aOD6zIHFC1cQ55SlDfoEbvkDYOCyLTtwvf2m_ddmpkdH4_itmcfF4lXaaxPEqgbD-_iXjMcI9FT_p-sCYd59DG4GGZAa-gkHxO905Bwi6CAQeFvxvI6FXhBNQvE2NTxBppaCULG_uoOpH3PhpLnhdrPRu8XcY-XK5wLyHV9xv3cj02w5xzfMw0JBEzc-UEejqiIM52byEp1_fWzpFAYsI7EjfxzNQjoy5uh8OFvTGIhoai2bd6Vp0icgNYgNquPzPEjXJeE9E03ptGd73eLOP4yT1Ct1FvI8Tt9fyiKJff4Y-iLDeXigJ8Fo8QJuX7ZtFNRWXFLrhQIAtkQtLymQF-rOG3qwHsWaNU8qJe4s8jUQqr2LmHZdjPKqwELKUDlwJ3WNPlY5xIp1FR49escu-ZLttfLNs4NkQtdKKNdBH3F53FjtDUzNpQ-FHnU7tUxL-hTFJVph4SQUMz1OrOkZW2Himai4nM3UfuHpD8Q6Izv6V1rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30844" target="_blank">📅 14:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t61BBGKELvmlC_3HrKXGuPbb7RA69zElUaGFtocLjrLpK8a8zyLdGdGA9vWNdKcQntAnq6AsJ83U-LMaiq3kFtvyLrhNRjY_6zSVEuUcVSpRCBtDR1XQUXDh5Ji-495x9CcytAA2H4zDSvV84hwYwUc46Q1g4MOzg4ndXaDXCw2LqJKAqXdb-TsD6U4czHQqZhX5KmT5E8Kbq_9fUnUxwB2Xy87lK5WXXVsENGiiqpZlrqRfcWSce3b2susH43G5T-MBkORE1lnsQsSf6bMuKzrYFK6uMPuUzxsb7v0hbMdOjRqfDBE9m7NCYJyp-ci7gIQI8vKjpp8uEGt1SL4ubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نرخ‌امروزمدل‌های‌مختلف‌ کنسول پلی‌استیشن 5؛ قیمت PS5 Pro درعرض‌تنها کمتر از یک سال از 40 میلیون تومان به 315 میلیون تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30843" target="_blank">📅 13:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30842">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxJNovGMklyjUltYFr-emZtG_bFqGTWHk6THyEwI8wivbiUjhfz7rpauAC5YRK-2IckaFOso7NrmmRLULqv0Lu9-TdqbnyDbDTYJGHNwFk0DrqNj3OIujUz-Y7QBDHoipMspXr9krqnIvTO0cMVATHWZic294RZ1jJZ151QtpWp6XTDrK5i4npyXGwT6mfGtIqVnRRKFhIC-PjGUBkXGREO8dpEqAEDBqo5OXy5pYEUNM77vefsnOjzNK3xpOyIXTN3ZMuzRcSe1fbV5MUnH5M2c1P054kisQ5UYBvwZqQzyoilZmAPeG5l1XYg3VTg20212pdHlRsIO-CDGBtDaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو:
پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم. از این پیروزی خوشحالم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30842" target="_blank">📅 13:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU6x-lYRiKcR1I3oSVEnJYF3FO2BZULUJKkDDRGfcA2rnZiQ5AZSb4p0iJUxIQlhm_osXnlj-bSi3xyQTyJE6pIr27TjdnYg-RpNFw4_4hCnJx496m5hwAZMP1K9zwLcB1pFUsF83JDgWHKqSpHJZnz4cElq03qr-S-3ynh7mGovsIsPsJuTzbLX25rn9rU0z0zvKYhwbfUUAWIHJm7TDTBiPfipG2ryM6WxeKYRxsTG1fDqNW3GEtuqddsgc8j1206qSHGnGq7ADKm44XhSGxnkfEFG2-sbJZ6W8ai9g2y3I2lBhC6h7xfgV8J_uEZm6q_kum8vAAWsmH7EVBJ16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین‌شماره‌هفت،هشت، نُه و ده تاریخ مستطیل سبز با اختلاف بسیار زیاد این چهار نفر هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30841" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30840">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hugfj2yP1LmuWwOqCsBxLOrxzprIMLH7vWTsUlevV_68QKSxLpYKRwHyBhz44o_Hqqpu3w3Lgvbjn74yRFdE47rALLjFywcNuiLLVTvEj_T6L_z7XtkEaxEu2mahZSP9BEW5poPiHAMnBuhwiAsqu88ivAlxpSsXNK945ExizxcX0SO-h78VPPiox_XuIPMg3uUIVGIcix0B6CjrvkojQUreJmF79NrPLMSpiybg4hhFS0CeZgKXYfz4xTGVqJ6UlcNhIAXuMpjd70eBZ9l9QBh_-y0R0UjRf3verHXGl7UjqfVHJs_mctg1qGaiI6iAhkcWPlWQeNSHm80o-ewWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لیونل مسی، کریم بنزما، نیمار جونیور، کیلیان امباپه و وینیسیوس جونیور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30840" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30839">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZBSNgsOBHc0TlWPE7Pfy3m4KaSpWl_ktBu7XATz2v2qXKilTCc_HS6vCibXL30JrYf-PrqT0DKpHjU6MHI6AvqZbj3Wt0qk9ceANfZb2itMipM4_mBmv_42Ft9flXY2qBhfSmS89liusIcV_6g5FTlmq27rgcQ05_fPFBlArqr6LQxPJwwbLD_E9TtpPUxH_o22Ow7HzjZimOwOsBj1NSdVSscA29HlmMzfKegMDEiYhsMKZfNcMsvi-vhW-t6cT1df679Vd0PH7ZRfp2DZnZ_V8Deg756tt5xbbXqgK9FQI31eJ1KjGkHkEpien20A0kjdYm1vKhSMv6D39OS6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو ضریب 4.02 دیشب که به راحتی برد شد
✔️
✈️
@best_form</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/30839" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30838">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICx_SnvNyE3owLYMt36DC5pKxzTy8ZVeXekl1CpuszIDEgGqovJUzBn84YgFi4DXJZshZ5owtGWEaPlB_qAI1JJ7OuXHu0IHiQnr62uYICq7w1F9DUk7L6cz9jo01zSlkhzxdmLAENDc3C3TdI_rMBxvc4ey9BlxDLHrpkO4sqwADyA9vGTCuWDVr2aSEvyKDroiAtW1SXqDhE-NSFm9vFq5d48dBoPEwRp87Cwjte6QiVJrMjv3jKH8EZOyWn2hSHEAm-WcKSjRpzXtlGsesSuPiVbperMEpJ1MMRzogimJfDBdEfHnKHq2vvxJmEO8KMgnNrck5uyfVemJJn10JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه بیلد: سران بایرن مونیخ از موندن مایکل اولیسه دراین تیم مطمئن نیستن به همین خاطر دارن تلاش میکنن که فلورین ویرتز ستاره آلمانی لیورپول رو جذب کنند و جانشین اولیسه در این تیم بکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30838" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30837">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/od6EOn7qrtrKhcBf6majQCDXtMthA9lFGaRMchgZT7mUt2EdyfFcE35oXvDXNxwu8Mm52wlzZIFKjTiiBIfYZ80sRIbeldAxw1MdCnRA7kSFKtrYu7S0jVBSDdLBkgmDeNSZTYtAyjHx6vrhspED4iC8aj1JUD_B3YBf2iX0LB4zO5eDrovNw8IdIxcEY8mmwp_OFJeIrINFvYsAJx2HFfF6heVWAm_Uz_A7qymvF2MzUDUWeoiTR8lCgq-1tUbO8zHCeleDyGkt7_Q51Ch6uQ8svgE7ZosZAgq-zNHl90HibOmfUATuae6ZCcCO293HPAExBqQFBTN6B94tgQ9ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30837" target="_blank">📅 12:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30836">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=ld-P9f7aC0I6-a6MKm0Kp9C3SInoJom-_aw0IkuFgzf4PLfhyjoH5uy1M8tV6s8tZc3iej0TsyKrs6WJ7NivU6a295Jl9n68yVFYcV6Wn1NmIYQDuRgOw-4lgP-bzB_U2oizLKoTWOPEjKfZ-B2mpbhS4ZBJcAEiZQ4N2SalUTm7eh10H675-f4n4YOodKUCxx_Hc69zFUcXjIAyNuwE2zHiirFSAOEsuB18w34yFmYl3BZjXOx1imckl4-BD93KQpASJJvctJ__mPBCCXTeXAXyy4ciqcJEDvLxehx324dbzX-lFN6QydyHPw_aURsTBxr2c58O3EDpG-3X1K2DQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=ld-P9f7aC0I6-a6MKm0Kp9C3SInoJom-_aw0IkuFgzf4PLfhyjoH5uy1M8tV6s8tZc3iej0TsyKrs6WJ7NivU6a295Jl9n68yVFYcV6Wn1NmIYQDuRgOw-4lgP-bzB_U2oizLKoTWOPEjKfZ-B2mpbhS4ZBJcAEiZQ4N2SalUTm7eh10H675-f4n4YOodKUCxx_Hc69zFUcXjIAyNuwE2zHiirFSAOEsuB18w34yFmYl3BZjXOx1imckl4-BD93KQpASJJvctJ__mPBCCXTeXAXyy4ciqcJEDvLxehx324dbzX-lFN6QydyHPw_aURsTBxr2c58O3EDpG-3X1K2DQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طوریکه‌قراره‌علیرضابیرانوند دروازه‌بان ملی پوش تراکتور بعداز اتمام‌معافیت‌اش به خدمت سربازی بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30836" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30835">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30835" target="_blank">📅 11:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30834">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=jPwK9zcDUbtB1ZhBbwmXIC5w8Cyd7np6Qhtx0qyEb4P2juV0HXVv_ACoQa1fdEUvT0dY0X4DccGRlen3BXFeXoDvlWiE5iEVb-dNY-RdSZiI52jQ_wrZzqwGy_6w9JajF3Ls6TumppM52vJhl-jUSR9CMvc3iBF8IB1kj6n7S9es-ryLzrWC9qy4SPUCfgATl7W8ip1nM0m2tSyqCI_PzCzXLfBKfFfh2hOm7eQa_ldizQ4WCXGVN7Hix_A1QyYkYS772WwCaBHrfBv01qKEB8wZE6XB_osAjFm6_8dysrxNUa29Fv1jS757Da72w7nHwU5jfJacnW7K-_tLnP1ArA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=jPwK9zcDUbtB1ZhBbwmXIC5w8Cyd7np6Qhtx0qyEb4P2juV0HXVv_ACoQa1fdEUvT0dY0X4DccGRlen3BXFeXoDvlWiE5iEVb-dNY-RdSZiI52jQ_wrZzqwGy_6w9JajF3Ls6TumppM52vJhl-jUSR9CMvc3iBF8IB1kj6n7S9es-ryLzrWC9qy4SPUCfgATl7W8ip1nM0m2tSyqCI_PzCzXLfBKfFfh2hOm7eQa_ldizQ4WCXGVN7Hix_A1QyYkYS772WwCaBHrfBv01qKEB8wZE6XB_osAjFm6_8dysrxNUa29Fv1jS757Da72w7nHwU5jfJacnW7K-_tLnP1ArA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30834" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30833">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDkhm-ykVvd1REEPrGqLGMsqLjvkoBibnZI_kVWRTM8sDTSu6OLQMotH7a5e1zninX1-K-XJEqQupND-9sQ8gUJwL7ahO5uKGIMikT2l-7uqi-gvFOpDlGhb1rRKgzY6JgOBPYSbvaE0Ng1M38wJHsXfBdUlBok2sTlFlp5cttdbObdLx3kTuZVBsNPyaOEcIJlAH8v9d4WFkrS94_BqciVjoVHFjVoGsqdSxAFw-GTY5saG7hFx_441xfaGeJJECRtCRjxuoaJnqtMNr3itGuu4cMuV0J-fqvDbL9kjxKx3kW9Sq_1fJXwhF3xgSDmZmkYltilqzRX_suKhVpKcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
👤
#تکمیلی؛ مدیرعامل باشگاه ماخاچ قلعه روسیه رسما مبلغ فروش محمد جواد حسین نژاد در نیم‌فصل رو به رسانه‌ها اعلام کرد: یک میلیون دلار با 15 درصد از انتقال بعدی محمد جواد حسین نژاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30833" target="_blank">📅 09:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30831">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPWqEHesz03LpMutdvLfRpIA-a_uGdjvu8e_23vyBFQZzx79o6gblnrHvs29iB68Ldq8dYe22nYz4CD0GeJlYoM5liHgRhRhqyf0e0RiqZzZ7SRgPRlbD7AO1rgnQNPrUcelp_bsZPTJjmfDNz06WYwBqX8GtBsTknH1Gm_-cfqsjrfMxmtDrWp1VLlT2CdGu1iGdlYQ5HxxwFPC3ENa6XtVI8OwVSU8ISsbUgYDdmht8bZ1RXgxeFb91WuR1fxbe5DdwwfQk4rhzoljpUSUhavznfRfXwUAMI_fRyF6_I_3ycphWizON1plCu1eLvQ_o0gVsZfZ3gi7NFsaiYJvnUsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPWqEHesz03LpMutdvLfRpIA-a_uGdjvu8e_23vyBFQZzx79o6gblnrHvs29iB68Ldq8dYe22nYz4CD0GeJlYoM5liHgRhRhqyf0e0RiqZzZ7SRgPRlbD7AO1rgnQNPrUcelp_bsZPTJjmfDNz06WYwBqX8GtBsTknH1Gm_-cfqsjrfMxmtDrWp1VLlT2CdGu1iGdlYQ5HxxwFPC3ENa6XtVI8OwVSU8ISsbUgYDdmht8bZ1RXgxeFb91WuR1fxbe5DdwwfQk4rhzoljpUSUhavznfRfXwUAMI_fRyF6_I_3ycphWizON1plCu1eLvQ_o0gVsZfZ3gi7NFsaiYJvnUsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30831" target="_blank">📅 09:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30830">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFHXTpQnst5QdA5iIQrAi6QqTAZ1fHVA0RL62KD43bDGDRXTHSze9R_edKOZHQSlygC8OGJKsrWnYFu46ZTA7cB6aq_HkTIg-87L0v3Bb6JgSABnmLSZyy2NOyqEgEe__Q68b288Peo7bQImexONiQD0pIYWD_tA4qRNdMOEdJa8cKWyAPG3TMDjk_og8INv3GaQCXDBfhbYKhgnju2JI5MDmw0TwF_TqlCS_in87k8dSQlhOAf5dwVt-XbW3xmffw1dOGhn4cOUrqot5yfienUM6zmeUyIdkaAVke7_nodlv1N2TsWXj1o6Faka5ytk2lHNiaVQ7YpOAOm2F7h0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30830" target="_blank">📅 09:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30829">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFWbiRVZLG3ksodUdNnCMwT1nHir1BfNmS14hg1JiZNj06nd_DuyFUEjbarOO4BkyT5cknCRGMudommTJGQmo30pjjyGQLLoE3aocgtfDZPWWfU-4BxhMMQszaBHBXsGjNjDnJSXQH4gSvVdy9g_7sW0FoZD6aONojExHzQ5nf2fVvLZ8FXY-bNuusRzbXQWP1TYvAwoNu7nP--3357nCCS8fcKUOlzN6cR6f8IjgKgt2pBP6FL1llmrNM3hx-hsdnAzwc7p9CM63yZJWAT14XiVt-e8WLkSrOhMaivk0PwVDe3oEd0bwRnTNEqCrA1l5ZoQ9cMd2wEesey9kd3l9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30829" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30827">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDwjsWrj4mLK3u78jH03rK7wB1AfXVogNwQo4NScbwUPuo_MrpTObn05NCHPfOwawpjZNEkSjhSrRN2P7RAw0Jx7PhczVt4JiE4zgjJTNt1Dt30s8mFdzOJPoqG55zbjLj0HKR271Td8J7SgSLYU7cczWWw0A788krj1Bo123mCE36upHB13_MFI6dFz_KFBWFwk9oAgWZXAhBxtKC4wl931V8jQI60WyaWNFATuoOMIKbGZzzaQZ9ZelDhbK4JFuMkdU0X1ZdAUfAgDMyfmhFPPmP61UdXcwrgtYa1zOiAYyv3-ZBXS__qSYHqecevjfPK-Xj_CcPxmPXL1YzYT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30827" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30826">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4l6JvY0Byrj5myriIkLlz0ekUJDCLpLr8S0hqEtd13G8EdaY20HMp1_C_kO6XsXvvww4lCxNTPdI9S9QHWQ4zPNwo3NWy91n2M8ylnThQh_Ga4aX9zbWcmsbA9lpJzocMMymFA26s44kfY_9FdC8vX2Dd7zJ0McSMPxoSI2jWemruNLMr6bI23Yyji3cEIJKLbbj50oWmL4DDnr1URUsTNMq_LGXJmjr3Qwr3ejhlmJ0aX28GPKCJWC3kK8aK7hexj7VAG-P8qlqAvRu2rHAxF30SJhiewVE6tzdwuNHNs6qBDYemAxQ2O2dAqtWWEYFQMkvfkHqYkcEMloZNhtoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
از اولین طعم برد ژرمن‌ها باکلوپ تا سومین برد پیاپی شاگردان ژرژ ژسوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30826" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30825">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQW2iK39y970PPfTRkD-sFQNMKOAnieXuWMRmmBxNd1YU8gpU2xm8tXy0HMxnZ9WUlakleM6lGys_tVsqocHSVOPFT-0D0JpBVs0qsUJxXtC6mI2yN7b3-50FnCs10eiMQP1yMH_YayPOwHrPE94S58iEegxXhRlZ4Kn8FPegjBPMwSHZ5oNSIy4AwwRd1Z-RbsTgfW1q6Qvo-042DoeeKXyRD-XbgdSU6sdXvKno52NOpbILSrvpDPUjbF7cArAZThfX4Bw0GGm-Mh34LuQO4eTenjWRitt_39OPJSxICW694CTNKwGdEAIhPA4dXba8QVGjEvxg4t3NV1QeVUiHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر! P9
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30825" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30824">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teW1CJbbz3U5x56V74e3AB4hJf3QUyknxmBJnbpBEwDAHQUQ2RzjikJCSbboUF3jo4m8J8GrT8M2YL2Sd5uu-gt9W4OnnZ-yEo8_fWZCPwVuwIkLk9dyHdHpM-TA70zFzWSqcnGfiViXe-SHb36PRyQJfWlCMgVqPwOxCo74XA10R2zojbOCOF4HH7uYhxwtJ50LWB8m3A3rTKyiHgdTDBGKkDBQ79ApN0lv5oww1RzqMZRyotydOjWufKaitwgH-xS-Z9aj8Z-Sd9I1TF39ooNQjwUc5q0ySIDpfnZ_A1FniGPmjPeBPX-0oLQwTn_4Gri7l-mRJhIbyxbNGARk4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رکورداران بیشترین تعداد گل زده در بازی‌ های ملی؛ کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30824" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30823">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc5r2pkM3aQFU8rXxOAiMsn0YsYnQ_2ryOXQUGdTNF6zFOS8ygeaVrBfvC768BE5V8rS1aO61wPk5X_U3DS6s8vtVmnqZpPVinqgT1JVIv3Onm48cOZpgACqZKPu8Bxyt29X8LY4pXvbp4f8RMJOVEh4FzboZYaHME95ZckDqm1RfjOc7bDvEk5l-GmZTRjUkDmFkW9DUBhKIQsafvudtY5k8TsSACt0G1t8xyZICcjkfl4cfduYsRaSvDsiUF9CaYifIHxam5f5KvEkZAltzqSr7SnQlAfkF-gXp0kMylbSxHSPd73XVst4_rKmmOFWnl7leDvYXR_SolQuHNvunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ابوالفضل رزاق‌پور و یوسف مزرعه دو ستاره 29 و 21 ساله تیم فولاد خوزستان به احتمال قریب به یقین در پنجره نیم‌فصل به ترتیب راهی دو باشگاه پرسپولیس و استقلال خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30823" target="_blank">📅 00:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30822">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAE9CxqK1yqtos50jP40p2zZoqrUW31GVPuxED_YsA7x8RTRWRJu6ny7Y1aYsHY17U7nDvwr900Gs72bMDI1qxcWUm6opqZxl77w_u-ilFSsxSFwX7hwfIX7jkFq27w6jATIW4URMvCfvvcYf2Y1TG-93TMVGItdgVQiFN-5nXIeyfjJiyHSfsxVxskMsCp9TgKUCvTVfbXmESB7cH7kSAziS2RWeQsAnpB8ngfzXAI5MM0SshifxZkzT1N-9y3YlqociEEZj32UvRog7f_CAp_doQGEkPuRdQuu1kYX2AzofJxbWNTvacLxQTQZWadJsiLCnfsW_J08o-KPtC46pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ برخلاف پیش فصل؛ حمید مطهری موافقتش رابافروش‌ابوالفضل رزاق پور به پرسپولیس در نیم‌فصل بادریافت 150 میلیارد تومان به مدیریت فولاد اعلام کرده. بدین ترتیب با پرداخت این رقم از سوی بانک شهر رزاق پور پرسپولیسی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30822" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30821">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJlfRXtm6USyjzzh3YKEVU5Qo3B_3B1L7LmDQyCWMbCwlSfFCfjQOsNwGfS_-0kKHydzImtrx-8e0dyCBxbg8lec3k4_yaSqSJpX2Yn-6xm3d0Wejbpt_Nk58R_45ZUEM8pOcIAVgKWEzVvLbqOSlm3-dMpSs2gctq85dX0-mXvggMfNNBTW2LUkZCrfoOdF-YUS4QQpZX4Tw2wDW8aasf-0LUSG0raWch0Pa7kAESvyZa9k23Jyvy8TundGTbhS7O7blz_ae9bS-bstuYPiS_iM0IkvNXPYfjgwhBS_kJ3qpAPitZJKbtRnXWfzoQykWzqedZ4ziO4vSghsFjjscA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30821" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30820">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aI3TIisJSIwDUyX52mwOIvRCmXsMJaSppxpkPgRQAgwfAXISSW9f9HeLLyLQa-xXRbpn88tHp3Kd04dbqgu22-AmBufeLAskaxIwz3ZapchUf1KM86E7gRIOpLT38GMcxGNTIohdDrlXIDwGEVMfSPzf6smAPZblrRO7ibi7THfzMuHl5EeZcIMKOYQLBWIzNWejBAv-WVvyvyLFGZhLJzWS3z9Iu8sAx1WDuxWz9S5ZE2QuZeB6lnZmo-DwDYv6pVU6YtftJ2obHXOsOoTo0TWS8R_s_bghw_5eUtFWmzRVhE-v_ns1hDimdkY25ceSyhePXtHDEx_g6-PZY9DxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛طبق‌اخبار دریافتی پرشیانا؛ باشگاه استاندارد لیژ و دنیس اکرت برای جدایی توافقی در ژانویه به توافق‌رسیده‌اند و این بازیکن درنیم‌فصل به احتمال‌فراوان بعنوان بازیکن آزاد به لیگ برتر خواهد آمد. استقلال مقصد احتمالی این بازیکن خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30820" target="_blank">📅 23:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30819">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm_pq_N-vlDSzTJ-DfdrxSZfWQ3GxRdqSGa392BSZ5oW4Yc65YsnTsyOKg3H6SWaePvEODHcBZNarFNUimJAY4cvTOBDsDwchAqsVJ9rZVCaDW2B50n2V_CYN4yJOfq8nko8YaX360QQIGxmmzI0uKb8vuW7ykyWZ9Ydo9jUcOMQnfHoPScykApK-CwyMvdfUsluIv3uAK2heMvB9z0NHMWlg5dqIYrnB7duNwqfcDFPlpqyKED_D-BjwuC56s8kYRS8WX05WJzVyE34m1ya_0A8lQ9o6uY45fDZvRG9007ls4KBXmrtsv2w9YhQyFJUMd0tlasfvZ0F1KHLeJir1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30819" target="_blank">📅 22:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30818">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzW96If0EZJf3Ch9Yc26PASJOx2rbJjYslmMkR1MWYTnieg9GeDxLMPAf0CBV_xJqMoH3ydfjTQENhVhF4vCJY5YT6kTBOUDIahsrkv82D5vN2ytWYbx0z_bmu7WD60S-2Bv0wdPXN7X1-vTBSvGzi__lOE5BEpk0t0-irlvd7iSyhVKwFDg6oP1JM3QTJwNOoWZ_4FP4IHc72H2MhNvtQVwrp2jMsazZtx2PAth35xRFvcCnQNChDQV3nvtHlTZP4DLRDeMlTBstbEad-JxkvTbOCekvAtp0KZM_uEJaMeNVLu44poc63m33-cXO8ifZ-uH9d9AzA6WkMJri2TX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک 146 گل کریس رونالدو در بازی‌های ملی برای تیم‌ ملی پرتغال به همراه تیم‌های ملی که بیشترین‌تعدادگل‌رو ازCR7دریافت کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30818" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30817">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL9QjIslOfJB09Fy9X_iW1aL3xQLF2wcCIsef-SRCLqFzrURCd4bBfKpHCqTNMmMLnGoaKI26U0zrm61M5Ug2fXE5p8lcCPab7tx3lNFFuN2FBu13_s9hlLPcSR2Xjx8qL16lUBLFwMcwLykT95hosMDK2jWv1L9Itx2MuY0LobEwE6YdJu2V7LqIj-71AtHAYneArBMOGMVMZYxM9T5U2chbKUvZ0erOVsZ48GRpsz4dH7q5s9tWmpHzyJQVZ3jfItmyEHHuzlqhJ3X20itdtRUssOrnYCpK4RjXToor6AIevd5opR91Vj0PBX2jTF-KcD8teo9crgOiojLnWF5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30817" target="_blank">📅 22:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30816">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htF6fiiIUNlwEMhQ5iO5smfmK5PwvOKIEd01PSKd96TQvkzsRb24i7Q3o-eC9rxRRPVGeEZFWaWSCpBPT0x90tDjjgrHYG4lfS0WAW_QfjH9fHeWmuWEL6pIr36meOi0LuH0b-H7OjDvXmjvTHTsbmka0ka9MKPr78PbuDbCwnysKUmT5CEDb9xktfyahOATA-4dm5k4naLDxwEwXASlvJTHHN1Q6o3zElnup3m8u5Haq8AfLOZ8ufNhKEVXGbc6dgyxrIczWraAmQsfFhNuDKUTYJ_0M6qNB3AB_kSnOucistGn4nMnZDgFrkFhgYzHGFkFicNSc0xkuHTom2EEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30816" target="_blank">📅 21:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30815">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5QEdCuxOxXlJTsOaBSwNlUZxg_ku7YiCqqsYrxMLhx0kO4d1916elhqXLwTQltAxuvm6MGgLvc2s9CAi84wPfO5PyR7d72iCnHfCVwYQkezQ8vxyeN-_pk28NnpumKGjJGamdMblOMjVM4LmGRRSfUnFoMtaT9fo8jeZWH8c8vz_lvBurIVKvyWgCJ6ITk3HnggbEFKa3DOL05zowrCjB_gbLs6CHs5ESTeKTVPDfci1CWiRco33GD4XyUvJD8bg2puVbyVOWJwUInxOILQVzqLdzknDn3fg_FkQr2EHoSAkBdbGihRH-3FXJCmpwhdeYzMcmHFL49vz_CADKr1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
در فاصله 48 ساعت بعد از خرید سهام باشگاه آلمریا اسپانیا توسط رونالدو تعداد فالورهای باشگاه رشد چشمگیری داشته و از 500K به 3M رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30815" target="_blank">📅 21:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30814">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2pu6ekjN8aUOOBE4rC-F6tJBg_Dya9U6MAYdA2RtqWO65x8Z1lYlfdRGZtGt3_9hGqipj68285ss_O-vH2R3GQIJS-ZWEK2X6UQrdCEeyHftNyu8p-ujJNcaWABdZ1Kt-psBbC3I0WpqNRN4iNWnMDcwxOXB9R7HAHutf6pkTGzeC19dpJ7HwveMinHG2zjf05QjgKTLwfEx-fEoZLAJUzcILzUl_9OxplQyxX0hHjQk_0wVv8xdnHi_ElVQWTg3R0iEZSr_bNTJMnYTXjUhfV-IICd9dWm6pdB1ykHPTEaDxr6LbLJq-GtoVCBH7W-qchWVfL1rOYDst7zb0gLAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولیویه ژیرو:
روزی‌که من به میلان رسیدم زلاتان اومد پیشم و باهام‌دست و داد انتظار داشتم خوشامد بگه ولی نخستین‌جمله‌‌ای که گفت: خوشحالم اینجایی ولی شهر میلان یه پادشاه داره اونم منم فهمیدی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30814" target="_blank">📅 21:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30813">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93919f9336.mp4?token=vY5q7d7TtKsxpihadumKiWtbXWzIg4dOfBHlSEOfHqNYxo5npHCqKK-Ceta-KskYG7DtvRS5yap39IRay2EjsPHO-h55zKgdXtcgRN37Fj_fUAtzPBS71h3K2t6ZSWsSHLakBhx1MvQnxaWfASOBBj4TYMemvO0ZBtLCgeC4sDucMyBSciD3eeWn1pHQAq-7qriJ71Pb0I5meDvBudhmu-ldaYSGtNPOXQZ5yvoDVWVQRMgaK7FltpEwsLVo9KZh9KwWnrSAUnxLplN506lrGVCzJe06gwO_VWLM66TcGthNSHUlAp9YLwPhDlEwmBR-U9pK7DoOVwsRYlKf4GcXsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93919f9336.mp4?token=vY5q7d7TtKsxpihadumKiWtbXWzIg4dOfBHlSEOfHqNYxo5npHCqKK-Ceta-KskYG7DtvRS5yap39IRay2EjsPHO-h55zKgdXtcgRN37Fj_fUAtzPBS71h3K2t6ZSWsSHLakBhx1MvQnxaWfASOBBj4TYMemvO0ZBtLCgeC4sDucMyBSciD3eeWn1pHQAq-7qriJ71Pb0I5meDvBudhmu-ldaYSGtNPOXQZ5yvoDVWVQRMgaK7FltpEwsLVo9KZh9KwWnrSAUnxLplN506lrGVCzJe06gwO_VWLM66TcGthNSHUlAp9YLwPhDlEwmBR-U9pK7DoOVwsRYlKf4GcXsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌پسره‌امیرمحمد‌خواننده سنی نردن گوردوم رو بردن تلویزیون ترکیه تااینجااوکی. بهش میگن بخونه، اینم میخونه. اول همه تشویقش میکنن ولی آخرش بهش میخندن. پسر متوقف شو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30813" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30811">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsGEkIHqai8-yf_4VIq1ntvuQ4NQZ-KPhkepsOQimEUAOjm_Pd83j8o__BMO6IuaB_daOv_5bo_MqTR1o0kfz3VVIeOM-X3dsLB_wyqxUwBv9qluiI424KBCY0PL0U8RJNAQoZ5XQxCqtOLjhvnuO2JeAbj0Asz804hkuCA8weLaqdbFIw53XC0nI7AQnny00Vs9IiMuGmRbwbvQ6bt7rcEfee7PCdOcp4pld6hsmTKEw3nexd_u_mMLDZnLy5SWMmT-dk1p4Pw0i7B0qO3M2ooQ3hoQ8QYWZy0pXwcSJGNFj-2XjZ2boktLuqasX-AKi58uJaP40RJBsCx_9XtBoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLvVWRbAfQ2nYzSIMPQDjCCs5RezsRe5D668C8w6b8dqJTxqaItn-l1KTG76sNSb4-UpPVIySuTOZTdtqfoBZNyHTD7ydP6qo9SPhRJg_OTbtZI2FVXSsCm1q68YFhShS8SV7tFfwkHdT7LDjHcrwSrzoBj1USrwmYCOitcDzgNvZlLYTQ6NcekNUOutIjI2tYG0IomPBDr5CBqW5W27UyamxD3iCqvkdtUNAIcz4aenaBybyrdaxqq8OKXjuScQk5hES0PodVBfzIeuCxz8gZrF9b7eTReAPUPojOjCAt6M1jAhw8gAmRe7c7tQPjBxm6fBcsMzNE3XEdqRIUhvRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30811" target="_blank">📅 20:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30810">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbr5YuSW9ttZ5QgJBVQkaJkokXMa03t3457jOSaW-ubIy8HuqgCCxMwCAJHi0N7gVraPbmvmT8pm6KAwsb0J7Pb2EfJk2pAWH0pCjAeTTD69xun1V5hbGmEFTwL_vmQ3GMpJDviHm0jt5LkLZErpg5VfwzaIFsgBZRWM6srd07_dNdN4bsIXk6Q8V2mkiEfk22wOoT0EV2-1l63fqA5IimM0rR4LB0IHgDbp1PEIFG_eJ86G3IzE9JtksgGwGnPpYJ44-sSM3UblVbAKmc9zsz_1VYXjzjn_xanc_O_CYnvVDpdG4QPe27vslQ67DwYlgmn1U1lptjCUQaJ7xkhFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال ستاره 19 ساله تیم ملی اسپانیا که شب‌گذشته‌نمایش‌درخشانی مقابل انگلیس بعنوان بهترین‌بازیکن‌هفته‌اول لیگ‌ملت‌های‌اروپا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30810" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30809">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anjhSF_0bdaCgQSUc82vfHxYae-6-E4kNspUYc1ZltIrjG-YLWX-_LD5b5ustjJKamOWH5pXlzsiqG-uYu-h_J8vpG3d35XdigEPapn70Q68dLd9OR52pf6MxspPhAoCAzKzEOcvVFV6ZB1mgPkNMEKY3zzk7jyd_QxkWuOJF-OxUUZx34sGyfE8roZkX34h51b-qbuqksvB945t3SzgUhEbiTBo4pZhLiRpabMS7IrOwD7GfFge0iUhtAiKR_LixTwqTfmxFmBq0ymGV8pb6VuQomy79CnYbnhM1TKhW29elETk-1uJd0SUS6L1B7Ltww_MD8zmt_PDe_HZtjWYsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
نگاهی به‌شماره هفت‌های تیم ملی پرتغال از سال 2002 تاکنون؛ رافائل لیائو وارث جدید شماره CR7.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30809" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30808">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐉 | 𝐅𝐢𝐱𝐞𝐝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS-3i_8rqtJrXC1vJ4NKHwMM2h2ifJoqBbYmhZbtFAe6DM92sF-WHgE6LrpACNhoRewR5EDjfWkXo0-Pxg93osuX7gq9k-M_JvMJIyWc07eVUnUEviTZmWSMItTD9aZ6zuzqBh8ASGXnE_HkRem4W2gDSD_hVwwDiHUxk6JkPWsNnhzwwcJ9dg-87fsB3TedaXXzdVhcyN4XJe9FOFxfelBvxp2RWAFM0HtF93OgX9H2w7YDuJ2ZbHP48e-lFtJVL7YJ0V2AWqKBQQ10ipqxyx1J6Pv8TkwSyRGh2VxPzbNGKTuZWv0j8AAvZOPtE3vAloUruDol7MEq6_M2ugT39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30808" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30807">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umI4StGFpV01F1QQ_pIrF71mDhEE_14ZGB4XYMusuEt5Odb5c8drc5PJtZSKnHlouC94wRSQ6A8aTE4cLVWacbkCOegm1FDNHZ0aTOU8mAO6IH2Fis3xV-J2XC3IAqc_mVCYLoqJKBfyoNLcOmSpSl9lmZ6r3OOOiAS8ldegUm0dnUuEtaxif1VWDxIl10d-nXAsahMcup-VDhPDFABXx1NDpj-awF8MixiTnZtuLJhoswdkBFg1ev5fs8gKSskviO-g0chOEBnmCNGneRTfg-UbmpsoPAHk_l6Av0fkT_sM5fGemdoFMfZHsR29JB3F2KhteWRNDdVxZaolEjwxjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
نقره‌سنگ‌‌نوردی‌ناگویا بر گردن رضا علیپور؛ رضا علیپور در فینال فوق العاده حساس سنگ‌ نوردی بازی‌ های آسیایی ۲۰۲۶ آیچی-ناگویا با ثبت زمان ۵.۳۶ به مدال نقره بازی‌های آسیایی ناگویا دست یافت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30807" target="_blank">📅 19:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30806">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlHURE8F1_t0Ku4uKT1-zselt4mxnCkdGYxQ2oKqSInB4ChJHucyZDgQji3VnMOljDdjDKz94l92g7cm1hYcX-s4xoqff2ADiffDoiMK_mYv1vWZVs_kZvA9QlXFSTJm_wLCdmXJtHW2Xb-ztn5y1ObewZi-nA1ZPfRA0LzLut9jQ3CNvwhjL6KW-pkj9k1X8in2HSWBKeEBlDSVplWHJLQmIwXpeHcqf6Ce0gHpGfi39cZSWA4U5HKBf37RCe67SkELb3M-vSFJaeogePxOQTZ5a9smgL-2ZNFwVSoDeJC8wdC8Ve3YeGqLqEyhOtaO6sWLExvRBNfNA69YufyxwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فران‌‌تورس‌‌ستاره26سالهPSG
: باخدافظی مسی و رونالدو خیلی ناراحت شدم، ولی طرفدارای فوتبال باید با خداحافظی بزرگان فوتبال کنار بیان چون یه روزی هم قراره من از دنیای فوتبال خدافظی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30806" target="_blank">📅 19:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30805">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA1NeJJH6d8WQVjdm5NhszZrvxRhrrk5wZhV8Jc-Qhlhmb7UMgHNIowT42sWnJPowLmEYjrMXNe2FtXg8jgCeIO35rP1eYIYuJYzrHqQ-isBeBeBadFnOjXTHjVUCxi-YBTHkv9U6NBGhcxjw9xJPOD2hRFxxymQAqDAkCpbzy1d_yiGNxbaS8zPo34IRYDdIxyoDKkp8oRTU6NqQ68H5Zf_raQdBrIwWROXHcIOAv9Yb8FyUU9FYXhjSzzB0yBCGejZsN4tyymNv5k9GNscIP_wC-PkCiKSUEyHJkC4qReJLnzcarDXSBRz6O3aVDx4Da9UV51GTnHAFQFs9vwZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30805" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30804">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRMuoybeE1yxbZXLtS6YJfyqtw9V2aEodMB_Kc_9VeagMKV0kWrNMl5NE7OUqL85gvHZAaOyb2nzd_mwza4H1zY9IBbzmj2t6-uJ6qlqbCJ9v72U_BFTiBoARfXqAGAtxq5pQXSzbLK3fBTX5-R1pRKQSmPUyra6B-2ZoOwFYXqLd4anmPs9_zWeIMwLQNYN1z7drsQIKy3AuV_4F596sQpbKx7gZYaOaqL-HRwiBDwVP-PMidMC0nSycVak_S2m9hc3AfHi8La3ceLe3mo1f3riyYw0jb-7ugMFuZF8GR-4yWBaMbqfo99qjb7ukHtZmIN6JxbcJeibLueUdjvrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30804" target="_blank">📅 18:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30803">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aa3CZqxMeMoePmmIamC7KODmb52R9WPUfn4JkNQtlUy4BmUr5_Y7ADLQHey8RTSy4hS_bSAUw550-Nsx6vvDBUFH_MwbnvYwlOMjrExIC2xCnmQaxpwO0rDRqjCbfnD6pwzel6MeB8FpvqlMseifouz0DCPm41r7BwKlIoDMvKkffPwIxwZX7_W9kRSFb8kD8AbKr6Ji8CrT1GcgeDFY-WuQbHfxnkHFDrOZV9rVgUFjIGXNvAjVRqeShgKKhjOOAwH3t4xh4jS8NXDiT9TbtiQHv92yY-jndL5flTXq799MI3DfP_A7t03zr7nytCDuNkxh7DUgx-9zG3E8yrA9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30803" target="_blank">📅 17:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30802">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ01B-6xZ_6yiRhDugz60rtiDq1oQRkNx4OaHmC23Ij474e-ohmFGSYwO32l4mfQs5MNLbAh_1Lc-AzqHM3OJuxP4TDE9GNa1XYvVkJO2K3YPTLmAls9gwrGezUKqlZgzbGoN3zPfYYTwWZrksP9ZSGtz3a2ofVP5xmO7AEELzDnT3BDdeJ6pSNaasVdJ-kbL2FtwZLC0Jwcs_0cK_9hgb_L4P6ujhpoIrfDYQY8X1z26-Pqrq61jQAjPrYKj7trZ_748WS8ckilUs1mjgcgyQe-BpHgnn_adHUq1DKD0tRRc-fCYHcYyr0DNZNfsrW84lgRsM_yGR7JC0LPyZ9gAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30802" target="_blank">📅 17:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30801">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇵🇹
🇵🇹
نایب رئیس فدراسیون پرتغال اعلام کرد که کریس رونالدو دیگر به تیم ملی باز نخواهد گشت‌. رونالدو بعد از جام جهانی میخواست از دنیای بازی‌های ملی خدافظی کنه اما فدراسیون بخاطر قرارداد تپل‌های اسپانسرها از او خواست که تا رقابت‌های یورو 2028 در تیم ملی بمونه.…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30801" target="_blank">📅 17:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30800">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqplfBKMwtdaJDDqYnZEnq-TAfzDCUAEHp3AiQ5WDR8u956p-xEYFJtvXOXnqMqMLkBtFY0ROA9UwrFiWtWQHXAL2Sr1BhhB6gZmCSHcwIzEvwtlCLLvv3g35ofgNPMjHtZZCZRP299lfIU_MlzYJ-tsPm0cvGaJIp4IrhXMLXwQ792bG6zFuTbza3JC1YG8FYaeV7HBnguIVUpCmMJLEgon03ECZVgDTihut5eBELfmoJH7JniuCLcItHi6QZLI6H8oys-xk7rOMZ3sUFAv_t1lqkBXhDY3dDp5jEMUJmzsBReEcuWdzMZHDfP3KLUqL9O2VU_Hth_uq6nfSoRFKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی بعد از آهنگ خوندن برای کودکان میناب و مصاحبه‌زنش‌بامجید واشقانی رسما به ایران برگشت. جالبه چندروزپیش که خبرش رو کار کردیم تکذیب کرد گفت برنامه‌ای برای بازگشت ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30800" target="_blank">📅 17:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30799">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-zhaOigqKekYl2kuRxySHy0fa9mMHXT4ZmamuKP5NVi2vlAju7EQWRDUxhVg0A5rtjWyLgiI-GLl75KHb2-hRBjWka7Yo1DDXtQFEZDC3Ya3-oKw_hkC5MIMXS9rVWT_BcpHNk5i2wMblt1eGQv4xx-i88X4AZDxcwDUFMYA67NikqiCMHu0NV1znjXwL7xlqnyGZR1PzSfUmwYxDDu2Y_3e2F4pPetuO3E7OVsxzX434qiWw7wYCqIVps5azOcqOgP-FtwKjXW6D_qqPh_FRniBTpv84B_GOyorpGC_cCh7Xmkblwh5gexx6Gox1gIW0gRg0LJcqCWj7dtqcBwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30799" target="_blank">📅 17:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30797">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYzMy0AUrKAzrPsOihg6A-raip1cn6L7diFDJMtlqDTL7l3D8g79c0SgdPiyhozzIVtJkyUbdG62SU_eN12FMronl1PeK0DI8TKW8DYsyTYhLmUgyhF49dl5e_t63TV2aSvwLqeBp2RIodcgzN5N65nlKcC9u4nU9rtG4E5liVyIS0CAI0Duaond8APSXRxNHqxi_uTKbmqbr91d9rNlO3eF_Kd34uUPGZvKHeuljKk9fL-YVYdkidiaELArVpMfm4b4Y9WP2gb_OX8dbIM5CXR-zQCtqE0IVuZ0IR7SUa6h1KnTXyyvUtTShFk52OXmggDpCH0qBsMxdM_WXh72wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=XfNQx0EqQU4Mh-Vq7LkWdYi0B4oYc_WaSxJ-vxLELEqxKdhvtNoIsLbwU1TxZugsQR2NGIossgnhbBi2lEMjr7KfDq3-utsRteGKcrAjvBa11Wf-3G-jcf7gyuy59hhOvlwwwzvUHde0B_gjAiGD9pzDfwYaaNYJZ2RhPuj-3RBDYXVFuX3UwSVhdsmOWM7wZf-aPzzrLUNrgLwAdbr1KqCUvEFyYuyVwBWuF_gaxEqcRTb2_1ptgdvwufvoYbKumLn6hZ4mv9lCzMiy80Br8q_OQWDEOmsykWSV8LPBXX4rONk2Tt04HMYJRKc__ZqlpvzDc_Azseg7Pl11tnwtaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=XfNQx0EqQU4Mh-Vq7LkWdYi0B4oYc_WaSxJ-vxLELEqxKdhvtNoIsLbwU1TxZugsQR2NGIossgnhbBi2lEMjr7KfDq3-utsRteGKcrAjvBa11Wf-3G-jcf7gyuy59hhOvlwwwzvUHde0B_gjAiGD9pzDfwYaaNYJZ2RhPuj-3RBDYXVFuX3UwSVhdsmOWM7wZf-aPzzrLUNrgLwAdbr1KqCUvEFyYuyVwBWuF_gaxEqcRTb2_1ptgdvwufvoYbKumLn6hZ4mv9lCzMiy80Br8q_OQWDEOmsykWSV8LPBXX4rONk2Tt04HMYJRKc__ZqlpvzDc_Azseg7Pl11tnwtaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30797" target="_blank">📅 16:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30796">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJnCiF60j5WnhFCSWkQFM04WLtOvuSo97s_NzU_E9bqA6cOjvjyFm0wwh82aFW1ISsbvLzZtmjtCKlmXmlpXJBA1wwZIZBdpQCEEQpFsjW6j7ilM_TZqHyRhv0YDkLBjQukKJjrHIGlEgYnPZL0ChJbbtlqmJhU6GDqbdii_Hda77aAOopvI6bgFqiVqr93Lhla0Zahw4H0yTwsXkjJBV8XE39-Uerf3_Oa4D8wKLx2lMWaen4XW0urXZ9pzI7ZGRFXWedmySW5WpwXDWf_ozYzZK9fD1T3yEZG1M9Y-wBLyVk5b4IQYsQpWgkoNwvklk1BBAf3VjIOrPby8Jj8A-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30796" target="_blank">📅 15:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30795">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkWNipVFqiujk_ZaA8xR_aMPGkIWg8PYRi5_uP6K27FvlBuTQ42NF85m1AgZUGbebtZl-mtjXPf1mIMCcqrfOQ5dney2kL-fjHLlO9WA8boVxdv7_rsjOuwxh95jezoN6ocHn61GBDWShHX8EfF3LdnMu6eFNQ0ejPguJzXwgkZHyCv9G3N-K81L7eHQrKyM_jyf0WnIZxVCSW3WkBq89fE_gQBKaMHvpXf2pU3sBxYHCfVlEcb4iWgoDCyYsfZiho6-PJEZ9HDtOmFJUjraVyGdY42SpizTr2Ph2MW7Ura2UR2X9G62a2t9lrnX-SQYlVLy8tcqBdSJBYF9IfJ_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30795" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30794">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbBo_G9qmtinIBaN8sDUm3sGD8meNAgHnySDLIOzLFKYySItXTGiCurC6ZFDvB3bhUdZrtrJX6mr9TNB_Lk8mpn10t-QTIuZhgTho57Zl4g8v36yrJ9Kie2zv7_BEpIp6Z5TleLpGpdvZtp_Z_wP4kDBibPuRhKpsSLmgvBdZgqr64ZGXtJrF9xQOJtq3mgDBXvLd77FrVppi2TYABbwOwCCwtHxVEscpwIrO4JsGBu1tI3PQVMTpzFfy-RAlPiU5UWjwfRbIAeqGTvUAXuf99dUP0Meuc7fodOkAbMtjFAgFWrOSvosJ3wrVQEkVnn_l9sXZ_ZNFm4vI-XrKsjJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال‌پرتغال؛ بعد از 20 سال که شماره هفت این تیم برتن کریس رونالدو اسطوره تاریخ‌فوتبال‌بود به رافائل لیائو وینگر این تیم رسید. خیلی خیلی بی معرفتی شد در حق کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30794" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30793">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=WafndPCbPzoOU287Vg_Bv7Fcxb5s0toxyvAjtxtIkGPHXkc6XW6hwM5yQP-wQU26f1DTAE_aABUXz3KlgEuLr6qzPc8jdwM3Wsrc_F9jxtiUjpOyf3xW8YBezkGra-6ziHh8apKG4oTc_BFiTYRivsD7ta9z9vip7gpit5xQgJa8vgWerBpe3-e1HiCnkCZlUGWwRbvTWkvCWAmFIrN3yLEnKppKvYOlB2OufK8DMRPKvyszvL0RlhTGwez2mK5LkvB7wpsSmUUQyzq7hco3As4_u1jrVanx7t4NUjsYv4rVRBW5lUxQ7twnRPA7H0Nt-aFEihwKNVzIpP8tMLBgxLtyQmK3Eya256vwgknm2MUr_ucDPAPb0JVwfjRLSZkSWk4rH8dHf3LOI5b7FTrIQMQWhcoRn6mMHvtcpK6kJsAvfBd7M3S0OuEqOsv_rR_U0ZEJx3igUOL8HOYTajIkB1o7u7enJktoL2hwQkK4RTU0zw4us441rlY1SnbwEL9FCL1IJ7lyaM5JXx45SmzgsncYsJ-Q7633a_Nz0GSJXaUrX70De4AJ6hdNkXkkMiBccJ_dg8Sgtl0I8XEFVA5nVU9vwFMDieSOXyGXjH5cCnQUHY8DsK3ugnm9RTNZfrv1sW0EOAhnxZTcMMsZzCNLVQQUdEFVvGm_nuibLmjueho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=WafndPCbPzoOU287Vg_Bv7Fcxb5s0toxyvAjtxtIkGPHXkc6XW6hwM5yQP-wQU26f1DTAE_aABUXz3KlgEuLr6qzPc8jdwM3Wsrc_F9jxtiUjpOyf3xW8YBezkGra-6ziHh8apKG4oTc_BFiTYRivsD7ta9z9vip7gpit5xQgJa8vgWerBpe3-e1HiCnkCZlUGWwRbvTWkvCWAmFIrN3yLEnKppKvYOlB2OufK8DMRPKvyszvL0RlhTGwez2mK5LkvB7wpsSmUUQyzq7hco3As4_u1jrVanx7t4NUjsYv4rVRBW5lUxQ7twnRPA7H0Nt-aFEihwKNVzIpP8tMLBgxLtyQmK3Eya256vwgknm2MUr_ucDPAPb0JVwfjRLSZkSWk4rH8dHf3LOI5b7FTrIQMQWhcoRn6mMHvtcpK6kJsAvfBd7M3S0OuEqOsv_rR_U0ZEJx3igUOL8HOYTajIkB1o7u7enJktoL2hwQkK4RTU0zw4us441rlY1SnbwEL9FCL1IJ7lyaM5JXx45SmzgsncYsJ-Q7633a_Nz0GSJXaUrX70De4AJ6hdNkXkkMiBccJ_dg8Sgtl0I8XEFVA5nVU9vwFMDieSOXyGXjH5cCnQUHY8DsK3ugnm9RTNZfrv1sW0EOAhnxZTcMMsZzCNLVQQUdEFVvGm_nuibLmjueho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری معنادار رضا علیپور اسطوره سنگ نوردی ایران: باخودم بستم که. گفتم رضا: ساطور میکشم اون شکمت رو که اگه بخواد کباب مالیدن بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30793" target="_blank">📅 15:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30792">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSWLilJJ15-bTFnlfoJGHl8XvhpcGotPZtjaJKRRRm8PrAh5MsrXnD5GBJ4ITP2Z0klclpMGz9toiBM3wunNt3Qe8S-gRhCzbUWmMnL_UJuvCqjUSMGcJeQhuI8m-BGjynQEmIB6SqG8IQJ07Mt3GkvZ0EYL-2dfi7UkO0YyYvzLOqTy5EpFF4hESogeFjNgUyTaIzjLCDneXqqHuNt5s7uV8ch0lFGn0pXZMJT3IqCtr5gRrGhjz7Z0eTZ2-1nI7XOf2V23LMm-Deu_locg1Depv1iDL6KgcFQI6QsW8jV4DrYg8vR4-CdvPRwjANekqSaxScQ3GCG3YrGdd1s3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
با خدافظی غریبانه و تلخ کریس رونالدو از تیم ملی پرتغال؛ بلافاصله کادر فنی این تیم شماره 7 پرتغالی هارو به رافائل لیائو ستاره گالاتاسرای دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30792" target="_blank">📅 14:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30791">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJRZqQYBb8IPwYzl5y9I9sf1DMu1QW8TWvKuPj4HDyVxuRh2spFwTATnAlgMksS-kB_u5IwCVGUkRBJO0Q35jKf7bgVYessrWMEdaDNhH3XUTbKuAoByxenbbJZWtVK0ju-_nJIeA54bCQTjhhwBK3WO21GVFusZaE8AGxlrb3172vdXbRYzKN81_ErilWD7PNi-2bFYS4QtezZl097VPPulhsAol4NNcAs1afpqgOBgE4KiORD72Zc0D1qmfPZK4EGeAl5DKxqNrxDSNSZcbkxsnRld407ZqkRWTB8xv7IxiT_Oh5a2RSgnoECVBHWG8B4naeNZrj_eVtm-IoKlLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام باشگاه رئال مادرید؛ امباپه تنها دو هفته دور از میادین خواهدبود و بااتمام فیفادی به تمرینات شاگردان مورینیو اضافه خواهد شد. بدین ترتیب این فوق ستاره فرانسوی مشکلی برای دیدار حساس روز سوم آبان با بارسلونا در الکلاسیکو نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30791" target="_blank">📅 14:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30790">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APFMFFo-EiDoaOD2HEI-NlFIIS2ltQ15GmBlRmGrWFpa4GGlBfYXIXivLSGoez0RlEc4w_2TPrwrLt5l8cC42w-DvNZEWBTFXITHI53SnbHG0f3Ol9r6Pz92Xf5GNvw3FApfp1gcH966v78uDDHRg_oQw0JZfxlwE9AfzQnwMNJQuaZwi4Sbx7B4Uu22jZZP6VYww5HFIep4ziC4hhZfhgENTY-fq6loavRtkPVoI-JcwRk7ypreeuwDdRIEZs858_kZK1Fnr08n5afAWI5j1tX0VPwCpjQFyaD0murxSV7nZ8lE06lbnUOL_afUz41lmS8W-7_nET7M8b_aVtdzOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30790" target="_blank">📅 13:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30789">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C81IZlvmbUjrBSvLzmiJEJ0HT6J-H3-3Koh2d9m641mqgHrZfuetlChJ6L85rWO93ZnJonNkJ3p2ohEc40i8al2tTe8EuCs2P0JuJ_96BaJfLQ7CqpfhWPZxhe-_hGQPlab2xOkquKxHx-7p4-fwv6LpwVQZA8miGeQGdLFdWW9FJlSP53kNyxQWo5OEEM4X7iy5gfPigl3hc-waCAxeshi3MVf3S8fHoswMjpv50ygWS85fr-yuHlMImOC0pFG5U2BaHuK8-aRUueFWu0qahxvk702BT98uRFD0rFxjcND0Wbw-prdnEYZbb58H-ruHvHBpC58vUN_BXO47I8UOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایرانِ امیر قلعه نویی
🆚
ایران کارلوس کی‌روش در تقابل های خود با تیم ملی ازبکستان رو ببیینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30789" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30788">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSdmNNlIucwIfNRDDbsDVdxAqcN2LycPwf2LA7QzG7VC_gLpoFm91FxwQ_iTp51lSUy350bWK-8joEL3qg4d_LNuNbxjTvUhuGZUxsmbWJsMQQMDHb4HB8UzmDHZch1G88GtYz-4mbOI-5Q1-eIs-B2XEfW_MKW5RXVQnY6LNsAhTt_8McqkDoFZcWn7x2zWsQu-PO52t_KpFG2lkOaB3Jh_ZbO0NC0nsmIVVmHUfKzg1grD0Ybj9YKgXuOAASWIJqldn-qPJyayfyTVZvYCZ8XevEkOQzlAKjMgmbvv2ASjsii8i8ACEAcfOruW5xY3orlWZ8jn7bPaVFSPXeGzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30788" target="_blank">📅 13:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30787">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHZxQc63AGlVYIOCUMeeBlNk7mvgchltB3q7MX57XTD82NteTE2z8iuFDo6C_V7r5QSaqoouTWkUbZHMfFE9ZuMy9r5MJKkqKozJ5IwRQ9mqeu_2Smsnem1HjMTzTuZ9aR5k-0bC-PhgChlVcKdKqsoGMca1VN-jFQo8uldF-AsaIplQLjajvXDRcT0atVghKk1XAJxNos7DbcWNCeCurGJ1d9PqY-oCivaCcjm_9DUoj7DmgFUxQzeLgCJE7nzhYOH9bFaWc1653SIlY8eXGrQHZGkfKj5yZetjBVeKNaQicLDgLp8pUKOLw7cN4LHkbYderCwWxSmvrCbCvteaqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30787" target="_blank">📅 13:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30786">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pskkNFb4uwCGqBKQaTFvsOkGzC4OwC3RuFfEm0vOOMY-4KHvC09fVbgOC94Af0yXnsnSmaTpoOrSDTD9Z3bEpqKKrVPiz2hC3bdVFR4uCe9bHeVYpjJYhMK4WoN4ttLlz3SIo-IiM47Aftvk9NTe3CtP8bWW6bsHfE-qXbytJ3iG_rLuQdJcK9iEA6UsjXZZhkJS0JdWgk0op43DAoQZ7ykcIwAn4uj4krlEv8itgm_tEqhzwNG97-KFNgkkl-MjeQQRA_Wkw1o-MHAVIrgFvMr_3Vz1flon9QIgKeFnPd76K4B2s9xfzdJqzi7arYEE2aBu1topTIrATiBexiqdyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30786" target="_blank">📅 12:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30785">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDdvVUrzwf_ZCgOPoueBntasFQmM4UySP4PaveAQG4BxjV-e8y7PakCFlp2jkO_B4qF0jK1AuiZ9KS-XN4F6MhgkmUVGgRIN-9i_i2O-10Cu7iXEc3BqBujC2z1mvMukNTdhgkUo3OlrIW2WlnHNVZli8azwzXfL_5ru08y9oscLtZeknsWI-LD_lw4kHZ16DJdMKOyBOfiBR4gqJRWdSepg3JgI6nmk1Ca-S44QiFHWWC-5oXViIur8NRZYYtRm7nF3LFk4zHL7S6V5PU-Vs8gWu7_ja3hGELtBDas4-gRt5JNeE_GH0oUYOP3Ud7n53WHp5o0NaCmOMhp0ViQikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛ طبق پیگیری‌ های پرشیانا؛ مهاجم‌جوانی که مدنظر کادرفنی باشگاه پرسپولیس قرارگرفته رضا غندی‌پور مهاجم 20 ساله شباب الاهلی است. تارتار قصد داره که در نیم فصل غندی پور را جایگزین ایگور سرگیف 33 ساله کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30785" target="_blank">📅 12:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30784">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=WKtECHAa8HkDgP4UofvjVL3pWh3qgm72s8Fi8e3PvUafFydSydPFe17e8CNiAhjWe44Cd2bfhv_LZtq9tE6IpNdZnvJ7Yhbte2uGPQ_D_fV0exxBxswv7GiZ6q8duyx9f0A0LXL61q9xOlKasI_HOum1TvMQhwYhBYUgUaBgTJmuqX2wlvjCw-cdnezW1dEQRM9nlzxndU3_5N3Ldlb8uXrvTRjIeD1R-3ck_bvbBQ0Z87ZvwCVxfGM1ACpFnjwL5JDYVEsb1_C5ZZsGVDjH9ng-mCofvo2eoh-1uwNWoouq4ceLV8NpWLbFIQ-y4jo-_j6L2lILCun5DmoT4uzkMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=WKtECHAa8HkDgP4UofvjVL3pWh3qgm72s8Fi8e3PvUafFydSydPFe17e8CNiAhjWe44Cd2bfhv_LZtq9tE6IpNdZnvJ7Yhbte2uGPQ_D_fV0exxBxswv7GiZ6q8duyx9f0A0LXL61q9xOlKasI_HOum1TvMQhwYhBYUgUaBgTJmuqX2wlvjCw-cdnezW1dEQRM9nlzxndU3_5N3Ldlb8uXrvTRjIeD1R-3ck_bvbBQ0Z87ZvwCVxfGM1ACpFnjwL5JDYVEsb1_C5ZZsGVDjH9ng-mCofvo2eoh-1uwNWoouq4ceLV8NpWLbFIQ-y4jo-_j6L2lILCun5DmoT4uzkMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهره‌کسی‌که تو شش‌ماه‌اخیر فقط گامبیا رو برده که باچهارده‌بازیکن رفته‌بودن با ایران دیداری دوستانه داشته باشن و الان میگه بهم فرصت بدین بهترین تیم رو راهی جام ملت‌های آسیا 2027 خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30784" target="_blank">📅 12:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30783">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=LOx2qgGakYO365jitwHYe70YKsXNbtCjqqVSVDgphA2Gzhku9Kx0GWGJ21zEvLex04eUkZK_y9h_btV8n-ACsAzns-p0L2gVB5zhF7LACC76_LRu6zdvWOvfzqLAlQzbTpun8c-Bm485K9pD4TB2aX_770rXEmvBmvNyf0zPulX-XQuHehvSc-nBRwglFyW9NDU-v7yoBwNZ5zyCmajKnfpmI9BknfMNIbo-yutwTYosrfxikSXKRSFhCbisUhArw7PG6lb39Sidglg0xVbLOauFr_NtfewVhy8MmoVie1nAAGIYV4baS43tknI7kUuMxBR52PGTZhPpBEBzgCDQ7iy6wKWV3ygrSjdOu6cjeyBPcaHCajlhrNuU-zfu_zapRuGoLymfxEMcJOSrqYJYQQxzW6ZS88jwtAh1_-p1eG1N_8zVK_TLeHYbXSoaYO24T6xsi7mHw3uvYsjWxblIthL1znvJtlX4FzuowwWX3-hX0twZ5XGj7mS6Uvub37uQqRBpojgUuO-2hMUoS9X4UQ3S5eUQwZYFqaWomjr_I3o3JwR5POVaqaT-zg2_0zHxGe-AZZ4kWDNeqfkIVjnqZjrftmxPbaOzf218UCcrANz2j9Wqou6_SdbZGwcCI4my9xuvlKfUM-EUffbTPU2mKzVuDBh90rPns4RLxlNeTi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=LOx2qgGakYO365jitwHYe70YKsXNbtCjqqVSVDgphA2Gzhku9Kx0GWGJ21zEvLex04eUkZK_y9h_btV8n-ACsAzns-p0L2gVB5zhF7LACC76_LRu6zdvWOvfzqLAlQzbTpun8c-Bm485K9pD4TB2aX_770rXEmvBmvNyf0zPulX-XQuHehvSc-nBRwglFyW9NDU-v7yoBwNZ5zyCmajKnfpmI9BknfMNIbo-yutwTYosrfxikSXKRSFhCbisUhArw7PG6lb39Sidglg0xVbLOauFr_NtfewVhy8MmoVie1nAAGIYV4baS43tknI7kUuMxBR52PGTZhPpBEBzgCDQ7iy6wKWV3ygrSjdOu6cjeyBPcaHCajlhrNuU-zfu_zapRuGoLymfxEMcJOSrqYJYQQxzW6ZS88jwtAh1_-p1eG1N_8zVK_TLeHYbXSoaYO24T6xsi7mHw3uvYsjWxblIthL1znvJtlX4FzuowwWX3-hX0twZ5XGj7mS6Uvub37uQqRBpojgUuO-2hMUoS9X4UQ3S5eUQwZYFqaWomjr_I3o3JwR5POVaqaT-zg2_0zHxGe-AZZ4kWDNeqfkIVjnqZjrftmxPbaOzf218UCcrANz2j9Wqou6_SdbZGwcCI4my9xuvlKfUM-EUffbTPU2mKzVuDBh90rPns4RLxlNeTi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی‌ازسوپرگل‌های قیچی‌برگردون فوق ستاره های فوتبال در مستطیل سبز؛ کدومش خفن تر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30783" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30782">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏅
ویدیو باشگاه پرسپولیس برای یازدهمین سالگرد درگذشت زنده‌یاد هادی‌نوروزی اسطوره سرخپوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30782" target="_blank">📅 11:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30781">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcLrHH3AuAiOZzjjtz92Xj1tixkqCMHXgYDGCrEMhxlyPgZwgQLhuuErhFgJWYgmg941-jrP5s6QGcwT3HRirD_NM8_ZHymI_qN9XREaHiNGRKjLywu66mHyDWIJHIeAieesLrEFoA7jy0zQyoPoemYSA6Q-ZWJIr56I60PT8mij2Cy-nFp2yQBkUJERoI7a86aklHtyP0nWW-WYQKmQkHjbwNyT16mYL-HL4WX0YGcEpwdUTwSU0A8_gA5FYZ4ndFYPbGLNkPg9NwZ5Y-l4tOSpTlGPMOwsXB3cBLsq5D539vk1cUjFHnveeg3Oq_ssl95cfzT6wkDhiirwJhFXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30781" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30780">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=Cx9Ueh7PHUtHP2px6dFjD1TsmAkx5Rs80p2zdCtN95h-Jv4jw39lYz88rcBaqfK_OUzCi2d23QhT7vH0tz77U07D13WAFzEAvRJg9X1QeK_b1Xa_72TdkOqPTb7XN-4N1m4F_FHS4egbvhTejgjyMPNE-HacuSm9u5So_Uj7Bdq3yxlV1kK6pWHdOdXS0RMgl9_t03yDeB178TMCgTNNC_ZOHtZqu8bIi1Xm2aYOdnbwWdhbbYxHlQkl5mHwrShmAHEb4rQc3_Op1fcfIy5SmhndqoqbG-AT9xmG85olU8h3W5gFwLkG2WpXq9rndeyrEQaBGUrf6JAfNq1P1PQpLLUyAGBqMNFqgMPlzoqWkLjSjBbphgKb5h_uwdhOFHPjJRs9xbn1DBkI0Q9Z9lHcWXgcKMOvbSq3FJVh45AQUPcjhJ8LdiD2XICA_NlvCR5R9Qtt1l0D3M100AiBMmbuReHcEfdKi4eseTAauRC5d1gZAx0-ooslNqTB_FJzD5J01gDwXzo6jC-T4uZQo3tlt1pZ5hVLfpHswSLSZtqu_n9dDbHTsAO6NtU9aaH4AILwSVKv739tuMJRHIQiTMjDS3M-RXK0bTvRL7HPnWz_FbgXdtq3LxRrkDcwx1If-e16d533ajF_4nHeuQsIrFsMTc2PEbgA2oOfYOUxEaPJE88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=Cx9Ueh7PHUtHP2px6dFjD1TsmAkx5Rs80p2zdCtN95h-Jv4jw39lYz88rcBaqfK_OUzCi2d23QhT7vH0tz77U07D13WAFzEAvRJg9X1QeK_b1Xa_72TdkOqPTb7XN-4N1m4F_FHS4egbvhTejgjyMPNE-HacuSm9u5So_Uj7Bdq3yxlV1kK6pWHdOdXS0RMgl9_t03yDeB178TMCgTNNC_ZOHtZqu8bIi1Xm2aYOdnbwWdhbbYxHlQkl5mHwrShmAHEb4rQc3_Op1fcfIy5SmhndqoqbG-AT9xmG85olU8h3W5gFwLkG2WpXq9rndeyrEQaBGUrf6JAfNq1P1PQpLLUyAGBqMNFqgMPlzoqWkLjSjBbphgKb5h_uwdhOFHPjJRs9xbn1DBkI0Q9Z9lHcWXgcKMOvbSq3FJVh45AQUPcjhJ8LdiD2XICA_NlvCR5R9Qtt1l0D3M100AiBMmbuReHcEfdKi4eseTAauRC5d1gZAx0-ooslNqTB_FJzD5J01gDwXzo6jC-T4uZQo3tlt1pZ5hVLfpHswSLSZtqu_n9dDbHTsAO6NtU9aaH4AILwSVKv739tuMJRHIQiTMjDS3M-RXK0bTvRL7HPnWz_FbgXdtq3LxRrkDcwx1If-e16d533ajF_4nHeuQsIrFsMTc2PEbgA2oOfYOUxEaPJE88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی تیم ملی پرتغال: در تیم ملی اونیکه حرف آخر رو میزنه و رئیسه من هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30780" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30778">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvBRy4YLfxrEN28ZDIdFC9LGf2ixSiJv2x2bfuDJnu6MdzSr6pOA9jtPq-nHNx5G75XQAlb1K-NrEPyhbiqICSxFPZUM3MVtJj1OhXoTHThyZNvf55fdn2uJUMGk5yoLa68QDnuua5nFLxgvWWHIQpkAu4UffdOTnWRsg3SK44BK_jIt2MU1JcVXqT0IepTii6sObA52FSsjFik4Kmkla5iPxne8qsMo0dSY8phohZ_6GduA1naHQYehfRmoOl093jmazTtc4qTVEm6dYvTMP6XyuScXNLRtFc-y5rt8XKa2vrOd9gTf1mOlwKGJ394Yxohqyd64E6HfIIciggHyWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تکمیلی؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ دو باشگاه الوحده امارات و پرسپولیس در آستانه توافق برسر رقم رضایت نامه مبین دهقان قرار گرفته اند و احتمال دارد بزودی رضایت نامه دهقات با پرداخت 500 هزار دلار از سوی اماراتی‌ها صادر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30778" target="_blank">📅 09:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30777">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=I_OytEuZy5pmnccSf3L0q6xquXoDNexdRwJ_LUA3bwhWai3qTDXgk7B2JzYVg9Cu2CQFEDSX4U6r-RQw6G1Y9mY65CRLMY9o5nOHP62YsE-6Z1RplaZJcfWp2P4oQY8LGtpUdJwKRxNK9m3yDI4GtMbg6r62THq-WwCilKGn-TPhCEaMdr_VFqKDYTnboArsCFJtfo9iCpmOZNlzPdHn5MIEpGaHo7J5qQ8tOlUW_wDR4YcV0yNOJpCb0_mkx5XCq7qpRXiJl0iWPum7d_FiNdxsAr7n56QVFsk6zEOqv15WcrHQMfoFDVTBlzD7xsKsN1dUXvNqZ7ej9a5AhAt9r7KuLNcsKr6pPoEkBtOgOJAgAlSI0GpYkRJVrMOmOla8vFMOa_7949R4eeTp23IGXv8iZTdUE5R8pO9NBB59ikqK3PisZ8MWUkJTYo-Okq-kKFyDruqxHf-XUPaIEzId-HQ7G5DYXNDxeIpCyN6FrU6r-u9jZATwKfABW76DODox2IkhuM7zZE9KyN16zw2mgae840Fz8JgtuuaZLmAnY_k0kiquldz4E6tboYt4PDBKUMtfqt1cP6_XjldIuERFqPdk7_MSyYS_nzSqbsCumMMIagcHgHbrjt-hOvTOxI-5kNB7BBtTIypEeGGUozIp7QJcbBhXm0a26c6Cr2JBtmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=I_OytEuZy5pmnccSf3L0q6xquXoDNexdRwJ_LUA3bwhWai3qTDXgk7B2JzYVg9Cu2CQFEDSX4U6r-RQw6G1Y9mY65CRLMY9o5nOHP62YsE-6Z1RplaZJcfWp2P4oQY8LGtpUdJwKRxNK9m3yDI4GtMbg6r62THq-WwCilKGn-TPhCEaMdr_VFqKDYTnboArsCFJtfo9iCpmOZNlzPdHn5MIEpGaHo7J5qQ8tOlUW_wDR4YcV0yNOJpCb0_mkx5XCq7qpRXiJl0iWPum7d_FiNdxsAr7n56QVFsk6zEOqv15WcrHQMfoFDVTBlzD7xsKsN1dUXvNqZ7ej9a5AhAt9r7KuLNcsKr6pPoEkBtOgOJAgAlSI0GpYkRJVrMOmOla8vFMOa_7949R4eeTp23IGXv8iZTdUE5R8pO9NBB59ikqK3PisZ8MWUkJTYo-Okq-kKFyDruqxHf-XUPaIEzId-HQ7G5DYXNDxeIpCyN6FrU6r-u9jZATwKfABW76DODox2IkhuM7zZE9KyN16zw2mgae840Fz8JgtuuaZLmAnY_k0kiquldz4E6tboYt4PDBKUMtfqt1cP6_XjldIuERFqPdk7_MSyYS_nzSqbsCumMMIagcHgHbrjt-hOvTOxI-5kNB7BBtTIypEeGGUozIp7QJcbBhXm0a26c6Cr2JBtmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌مناسبت خداحافظی غریبانه کریس رونالدو از تیم‌ملی‌پرتغال؛ یادی کنیم از این هتریک تماشایی و خیره کننده او در یکی از بازی‌های تیم ملی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30777" target="_blank">📅 09:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30776">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6wVnNNsh4kJA-rGUFPW3G7FiQUIbzmRKUAaeI0284PqyBX4VCoF12SQjlonE7scMM6TkWLXD91W0rRvf0nw63bhJwRydEPuPP-A2gG8la1mIbfwmzyHs-sg4Z79z5kKkMynsHDvstG5_jO3IwMAEdrho_OFyHLVGZ9d6GIa8f5YJTVWKijhlKYlrrR6p-GsEWINnd4ozBDJ5wulh9ousoiEs18B0B8L4EwBincKVslB1TNgYg0og8PzSb06gRgAYmWceJFDMaRfq0M4ynnPZTefmSTwGdbxpruBhEdNGf4_PiYF4GZDv8Bwy5buv5gMODc5Gg8VtAWZC7Db3BXAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30776" target="_blank">📅 08:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30775">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y69SnA6cnpjLd5_n6ZuUPkL8gTl2y4lc28XA3Q64SnNbKx8eechE2HhW7NhiDlTn8LIjHFoTYZVnhAWsVyoa4YIG4JFwvZ_Gt3YErgYngNxBl2pOVqHYLHgg3QsQB2jPLIVleHPc-2AnfH2tVELzNmSHBOfh57U2BwrTwX2bTF3udKLoDHwPomVnwa9vCZ_Fl97IdF5Bv7E3INNs-wjz1urjQCeyahlJ0RsklIrnwvTNT7LzM4yjSC-LY9VIDHbs_zdz-gofccKGw3wnYnao0P_uKWAzPNsfE7xdd1tiRlfyYIfxeJW9YVDBryX3Be4cNqbK7cCY5V5kNPyRTn9lZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/30775" target="_blank">📅 01:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30773">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR7M2a_kg6B9v5OE3C3tSKT5a4XsLTBuTy4qymNZdvE1FDsaez6L6RylsFgeWkROIYZQsUjzk53pVFbjHoG5wXrhLrrD2bwAvU7PAjDSKk8bpyc0PB42t8q_-rC6qYRaTKk8cBfpNBZV0tLGDCF91GN0PgOvNkrY-5yi_n7jABUSXizYf1IAPVhiMCsU8CAewv8SQTpPyAH6zObpN26D3jDEX_g7TWvEAiABvuSD26g5ysRUHaOksjyYv7ABl5DzQyxv-OgziY2izVGFKgMMVosWSfZLUwmjyVCiuJScmpFbxYsSW83X-_7IeGCpnHkrrIoc_-1I1cm0rAENaXpcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از این به بعد جای این دو اسطوره تاریخ در تمام فیفادی‌ها خالی خواهد بود و بعد از سال‌‌ها دیگه قرار نیست آن‌هارو در مسابقات ملی ببینیم.
🇵🇹
💔
🤩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/30773" target="_blank">📅 01:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30772">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyNKT6Q-kkgkNANW0QHDMwbqRuaADMP0hqV2lpZ0Q3vdOWJaMLfKT7EjJhrhgnNZF57K6Oa0eNznKBsipg0WLXAK4rV3mfbp-KvVwyUS-z1c-FfceQw8YT8a8mm2HQH9SiXlcoLj3jF3kaRsukKraw4_WZGKCwFnw7uNkNsZokrf909OMGQwUpkhpTGE8ztbtvAwVQ2W91JEk2tFjoV_6wVQVrhYInambDvKA-YkisVMsw5LsTmJ3WTqiOqVBJxIcPFLIhfu1ouggY_-74t3n4WMyv8rXSiFud61XR2nfkBdAR18iOylG2VHkkmcS-DinsDYklPskBdKokfemo65Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف آرژانتین و پرتغال برابر بولیوی و دانمارک در غیاب لیونل مسی و کریس رونالدو دو ابرستاره محبوب تاریخ مستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/30772" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30771">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuauMffGhEdbOIBRe2gmMVZ1vXADM6XmGG5mWuWR9poQT21Lic2vn19ACmK2acCoNoP5X6jE_g_-6ZycCvVtcJ60EedNgL4zX7PfaZ7JXNvQa4A0_CYwrrk3it56f5CnrY2FGD2HtJlaR8U83MI274wBvJsg1bjZwS9BVr74qmj4isam6c5fw-EaX2vc8DpFbYR1xjF0YyhBJjLo_9PdSkhWME3QpY1kfRj64qjl_kKftiT99ygLBxxB8KrICqKFvHb0TMV9Ka2jiSwZhbxEJ4FMEZ_sc66SyV2OeNKPavdiVH9P8wp0BUQWq3LIl_nbjgnirUurgAT0Nu_-8KQn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
برد خانگی یانکی‌ها مقابل شیلی و دومین تساوی مکزیک پس از برکناری آگیره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30771" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30769">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIsfSXBbSkSDwgXDe7A92LeDzTj1m9F8Bmx8mzHbT9MJtwKVY4TGlyKONuGo4h2UxhH3jRMKz48XgV0AOEdeuQPvPB__G6wll3ytYpPoXXXR9A6D3CLQkLIvmpjzpzo6L9zZduvtno6wE7uCy9UJ9khz-66Es2hMIU0uK12Pv6Tk3HejJ3NPOw5y7Ru7P2GMwWYaKsuJzMt9wsJH2l3jf0rpO7X4jYqlJSjn1B0tvAAZ2OUA1Z0_KlHwvo1jM9dw7RCApgGLmQhK31UdYE-cSf9G7dZoSYqSgJu3OmFzAkpWXaqCH49XkYmO90NKJ8Aqs0o9UDzLbMtC8l-Eo51Yug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30769" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30768">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7xUXMXAGtmtH156E1Qn2npGp2DY4RY6QnkMmASBVNMhKAGdglpMNrDC0-uUQeEKBXjlR3Mr6vNexz2OBX7Vl3zyrhVXZPr2aVawo-k5YimDEQgIr7EeVD-_tH6_-mjIY_zzo2uV96mNpC4dIjy6K2bwQn-oi33D8d0PaPGRedai0K5ga_YQdEa7IcKSkk8GpCFx1nlOiwWiO_o68pw3F5FKbJ6ATnDV4TM74Ho8L-qLnkW-1VIUaLFe07YBJRn0bMif57ZASyOg9jvJ8wpVym65iS9mOge-s2IsKWS74hiyprLy8emCdoDZ3eWUxAHtGbG6Y5SPIckO5Bjl_ItFPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
روزنامه‌ اوجوگو: کریس رونالدو دیگه قصد برگشت به تیم ملی پرتغال رو نداره و درآینده نزدیک هم بصورت رسمی از تیم ملی خداحافظی می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30768" target="_blank">📅 00:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30767">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcwq4WjjGtQlJj6I1z_Ja9JIbC5A50jbudkCyCSXWRuK2rQhaWg34PLDpZjjs4JZ6EcdUg5KzV-41-Fkw_XhY7OiZkNbb0XkXEelha1SSv-N1NUi544zXs8vF6Wji4tib-swBPetlnTrn9oyyjzkOWbtflDYzZ8GruNPFD0BVQ1r_GO1QxwYyWVu0jbcq-IeuBWOOqLe97NW_xV0oZPa4XhSgP58Eqwyx65hNWHdK0-P5wYVbABiqMmzDzpQrMsiEbdq1LOdYc9d0AS4cQRlKR66J5SEjULetP5IWUgWUtIhJysjlG8qk9htENyLsgKKMk6y6KjQIGDLi9xkzDomNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30767" target="_blank">📅 00:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30766">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onDg4_-DAkCkp-kuVtCXK8VTrOFoOqt0vG3H6oCf2_0lWDTDzQl9y8_wIODq_fgPC2e34S5iQKj5Kwd8IvW0kaeHo7E7Pv0OtbltibXfqUbPMNIc4xkuYmK8AoVPGvmwmwd0wSuuLEqwqSzqA0Jpu6KPU7VcySv6FF8PnfuDoBTeXa6wTKucCg1WU09lbWu7yXnYettfXNtUFdmztl57M-HtBN3EqUZVImp0WUuD1loUTNmTV8swhcxqAM1PaUwq6YtbEe-x6ZaG9veGfID41fZNQp21stfe_qgrVttZRl-OlaNvAbLk6mlhmMF7GoZlT8nJFlCly-kNrxZax5LKsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30766" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30765">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=NGrQxebq8Tb1AW-fO5kAHQIfA-Az4m2z-Q2XlDkRhArebTGsSH4fRa49ywTAvQ5D1r3ltk_EoJIZzP_jgueBjperwKNqWq4AOHR9Auwwjkrl5Lfj1fDdvfyp8ShGqz_zGMYodR10qxpcr9gH7lXzwsaYmO5LgC0YCz_nAEcPdw_tNUEGcZL3VJQ03D4RXk87mtqF-ig-U7PEpG27bjNgW-5uFzaEJirnKL7TN58-V24-hg5NgL8j9suCa3RYJHxqLQoVyDLQjc1XorWhBfs-f1ZqcJhUZd8aUQOm4YSEPjXF-9ene6-TDFfsOQNwK2iqT6rAABeppNbNv7WC6-5dDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=NGrQxebq8Tb1AW-fO5kAHQIfA-Az4m2z-Q2XlDkRhArebTGsSH4fRa49ywTAvQ5D1r3ltk_EoJIZzP_jgueBjperwKNqWq4AOHR9Auwwjkrl5Lfj1fDdvfyp8ShGqz_zGMYodR10qxpcr9gH7lXzwsaYmO5LgC0YCz_nAEcPdw_tNUEGcZL3VJQ03D4RXk87mtqF-ig-U7PEpG27bjNgW-5uFzaEJirnKL7TN58-V24-hg5NgL8j9suCa3RYJHxqLQoVyDLQjc1XorWhBfs-f1ZqcJhUZd8aUQOm4YSEPjXF-9ene6-TDFfsOQNwK2iqT6rAABeppNbNv7WC6-5dDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خواهر رونالدو: ماپرتغالی‌ها نادان و ناسپاسیم و لایق داشتن بهترین‌ها نیستیم. تیم ملی پرتغال هم به همون چیزی برمیگرده که قبل کریس رونالدو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30765" target="_blank">📅 23:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30764">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teHEyG116j4bCwUTyWTdq_oX7VuYR9fD4DMQ-9yMwHRVxbW70yW_Dd7_PDfuoJwQFgdXE-zEPduqgQTXyNxDBJvqJjWlE0lIfe0uS9B3ioUJ08L-QgkMiFPTFL8s_M0v6jsGX9Al3GRplNVsroJaKcD8KF8AWc_06NdTZ11muijZ3y-F6ibYUr_ASFJAh1opM8BvB7Pr_bnTsmQhP2sn7yRoOGOUpGfHcvRz-PWa_3vNfZ-Mt1tKprjzE1BSo4cxQuWmeEVfuXPnYJTKr4W6OMenkDRZfvjtWQEIzpiiiqNO3-Lwc9mb9bEfnWfPUDnXc7phrqlYuQujPEbVFRcliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30764" target="_blank">📅 23:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30763">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=OpZRoxV2OFBQmLywH2NqROxmGL-IX-c8PHpMrDg28oLQSN82g4HIwRLIxQsAkQdmedxzjJBFHhGss_AD7cp4dMiCQIJUSGzYXViBXA7v4w6cjuN_AHDJw-jNoOBro5ya2Ub1WsFVrWgWkKHyB-XOCnDR7wDM4x-mzj7Qt07dllJOxc0by6iE6GnOcuO1PlkSBb7ATbFq__EFFEhPBCOF1xSYfWxoR9aTXWu3TcU1WXCpAjxPJQ9AlpN8pYESbUfyfO1NcZq8UNL8A2gk-vzcOB9Rj1uutD1syzDwaiIx_zttH-nPLl_LjArT4R1tOjOgpvxS9gRdWH0o8tQLQBcsBLk5ULxnxmHQul3VCb4lKe0hc9clIR3IuCVxOHwEnHUXCyXaz3EfKADOHybVjlgZb99c5rIajV62fr3J_qsNFrWjVA5iHOIuT6wthuy3I7jA_YBRZSwYWbEqI-o03AUFFOMGXb9BRJFHvg8iY9PIG61DV7ycU3eAeK-kX-KgL6tJmr1IDYMujCGrq-ZfiKwj4mlA9UPX7EsOkGkZ7h815NP8UWuyu6zW_Imh6TzYOiovXwmGv12ygSjFKSGi30QkvH3VkbgjkN5UV4sAvkbUVON_caCWi-BEnAFdfVWtz4gTfeV5VFbOMeHfU1UvI0arJpmdxnewLAzFjrTCkbUHYIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c6b3c35f9.mp4?token=OpZRoxV2OFBQmLywH2NqROxmGL-IX-c8PHpMrDg28oLQSN82g4HIwRLIxQsAkQdmedxzjJBFHhGss_AD7cp4dMiCQIJUSGzYXViBXA7v4w6cjuN_AHDJw-jNoOBro5ya2Ub1WsFVrWgWkKHyB-XOCnDR7wDM4x-mzj7Qt07dllJOxc0by6iE6GnOcuO1PlkSBb7ATbFq__EFFEhPBCOF1xSYfWxoR9aTXWu3TcU1WXCpAjxPJQ9AlpN8pYESbUfyfO1NcZq8UNL8A2gk-vzcOB9Rj1uutD1syzDwaiIx_zttH-nPLl_LjArT4R1tOjOgpvxS9gRdWH0o8tQLQBcsBLk5ULxnxmHQul3VCb4lKe0hc9clIR3IuCVxOHwEnHUXCyXaz3EfKADOHybVjlgZb99c5rIajV62fr3J_qsNFrWjVA5iHOIuT6wthuy3I7jA_YBRZSwYWbEqI-o03AUFFOMGXb9BRJFHvg8iY9PIG61DV7ycU3eAeK-kX-KgL6tJmr1IDYMujCGrq-ZfiKwj4mlA9UPX7EsOkGkZ7h815NP8UWuyu6zW_Imh6TzYOiovXwmGv12ygSjFKSGi30QkvH3VkbgjkN5UV4sAvkbUVON_caCWi-BEnAFdfVWtz4gTfeV5VFbOMeHfU1UvI0arJpmdxnewLAzFjrTCkbUHYIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
#تکمیلی؛ یکی از شروطی که فرهاد مجیدی سرمربی سابق استقلال پیش پای فدراسیون فوتبال گذاشته در جام ملت‌های آسیا روی نیمکت تیم ملی بشینه اینه که مشکل سیاسی اللهیار برطرف بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30763" target="_blank">📅 23:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30762">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzF6X5mwhZiJ40nZ3Y85cAtQ77z-RUQc6n0cNdNfLuFYOTG9Y1VDDoZVebNFf8J9xho7WSzk3Vm0xZ-av-5YgBHq0DuaGgl9ro_3IxjOTtzXdWtE5W4KDF-7xcZqBOdd_eUTs9T_lO7LhoyUG1YVBx4BeP3vlYQ2lP2i1PtxU34US_lUXhY_Q8ade5-htrZEi9uyM5hay93Cd97Euvp5rnipgXDNrKbap079xG19xPafKr8NfnGq5nMoBL2_fJAGpVkUu6cy81lQN5TSXrrIgpK54oVxACl4zLtFMagKo7c0UxgogyKHH5sXOzPFHLoSQ1S4hEKRKOTpKBpXb6LFfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
نگاهی به عملکرد و افتخارات کریس رونالدو در تیم ملی پرتغال؛ بزرگ مردی که یک اسم میوه رو تبدیل به یکی از پر افتخار ترین تیم‌های اروپا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30762" target="_blank">📅 23:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30760">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLPGYqlFESkoFYXAmUpJEZLnCeIVm5SFsRKoIrUFOiFhCmFd0lHpu3fj6eCcMvrtmSUuohc7xWs7zmPIPx02Z2gI1nYddXFjcb_P2NNkKUsKcgSJuGL58fo1-PD_iVMn4hGGGcE17xOPlIrkE6_u21zGnMigYCcIQT8k8HFsGu6AKIPTDLg8J0J1W47K9ORaqUDXM_FLuOvDvQpnIvUEWhHtigqYOe-2yQ5QnjPtzOjqm7vZK4bESh8_b1zhEF-1HL06vy2CddaPnFY_6bVYPy-KiXYQzEf7w-ueSpMkkQAMs5Q__hyCScMpEDTIZQIf5BVXkZB6XhNWArbiEB5PRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اخبار دریافتی پرشیانا؛ مهدی تاج رئیس فدراسیون فوتبال علی رغم حمایت‌های خود از قلعه نویی در رسانه‌ ها اما پشت پرده بشدت در تلاشه که فرهادمجیدی روراضی‌کنه‌که هدایت‌تیم‌ملی ایران رو برعهده‌بگیره. اگه سرمربی سابق آبی‌ها اوکی رو بده قطعا سرمربی تیم ملی در…</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30760" target="_blank">📅 22:56 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30759">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPYIS1QFFsNBPHD0wUGkNMGeoJfS_0LTjHhVOxHwWjSvp3kRS2sfRL60dq60cEa5HzV_gmbZDKD4ifNFuu6G32diTc5JtQ_PqvG-fGvFN_cW2XeAowdjUPOfbusYuM3PEphrQ_7iepGZc993wLM_dREPw3htjjLGHjA1-g55nt4Hj7lR9VIpHRyabG8yw2d9wrvSWHfJt-cdh-ZzwiKPmnEAA1LKTdL6ISAywDFBgRD0a0ade8dhQWF_zVMyxVPt9aNGJI7J9Qk2A8sRlkEW0sNb1vGpdW7uoSyzgpXzVvDR2CX71UjXo56pKXYRPT1Rekb86_8wL8yoRWzcXTc7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یورگن‌کلوپ‌سرمربی‌آلمان:
توپ طلا؟ اگه تعصبو بذارین کنار و آمار امسال رونگاه کنین متوجه میشین که‌توپ طلا باید به مسی برسه. اون تو 39 سالگی یه تیم رو تا فینال برد و نیازی به حرف زدن نداره دیگه. چون با بازی کردنش همه چیز رو بیان میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30759" target="_blank">📅 22:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30758">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBMSez5JYlCf6LRNIIyL9skZ7JBYvAw0npInneyrb0XFmqI5fkSaBX2L0MoSdSfdcnAK_bSL-f1T45r06mYXUetlBjX-PSikGLtcsEanN0ZnTC5az1R31f939-s0EWz1U05kbVWJP137tcezzUM2-wCdPXCvPv9QxcrBcsO7IfmCXukOFV9xC6PUmRdJRLKSHCwDrg_XEKeVNmiZ-iGtvv698Cgnsqk2YeeHyoRX339Sw4ybuFZQbtKbXWf1Uee2X_PZIaJ8St0sSqycqdhdZUg0wUUKPXvBN5uuCe9Cv2x8QuXqZlutm9dSyvkE-8Rv2vB3DM-kkhnQ9dsc5RqBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کریس رونالدو: اگه کادرفنی‌پرتغال نیازی به من نداره خیلی راحت این قضیه رو بیان کنند هیچ گونه مشکلی بااین‌قضیه‌ندارم و خیلی راحت کنار میکشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30758" target="_blank">📅 22:18 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30757">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFH3j5RQ4MxssIkP_zWOJ1L33kAuIr0CnHv0mlNgDiv6NsiZgdz1WboDPC0SMyPbNF8_7_yI6L54t7Cec8q1Lkh3pu62aXBX3E5U4VLzUNluTvZgTDwx52JXSpzuf8Wo4DY6K2bQAl9_WZOQjfWp6KlVRqMoULBC5hMuOTLVj7O6dVlqHbnOGWSiijCAOwel712r40F1BospJhX-tKXLg-68_OEpA1MdONqCZgzNHEaY0IBM_3pDfUpQbjKphIpj8zCWXUp6CAwvk04tAbGxaYAul_oDe3G6d_5lXp43fYuiNcmPYcdsvbaLzfFqc_FOFhsCeStsoscM77rZpyVAd55Cs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0642770280.mp4?token=BGzAuAH3HopiQ4QjyhxAp3-znkGEpst5tZpIoWARhqLoq419G1p_5RsDWr84BZSgx-7T0xbkE_nlsemWZh8gnntzn_UT6yOetRJ0JkLAOxsKk7sOrlWfBBAggRALUJH8vr1rVL5yOjIwAgQ7NvqBeamuIjt0t-3ohSxSjym6TLu-u2rh-1kFnOB-psE4fv9mUfI7oZftLanem0-V_HH2SLOtkJcH1cZ9BxArLFyZS4BCFcNNcIx71bZbD2_VYTYtjzfSsZyrzUCOLAN2yv6qy73v8T_iz9vQOHn-fLGbSC1L6XDTKK17SkwFd6xbarZ_2Fko-2q5kpyur5I9ijpFH3j5RQ4MxssIkP_zWOJ1L33kAuIr0CnHv0mlNgDiv6NsiZgdz1WboDPC0SMyPbNF8_7_yI6L54t7Cec8q1Lkh3pu62aXBX3E5U4VLzUNluTvZgTDwx52JXSpzuf8Wo4DY6K2bQAl9_WZOQjfWp6KlVRqMoULBC5hMuOTLVj7O6dVlqHbnOGWSiijCAOwel712r40F1BospJhX-tKXLg-68_OEpA1MdONqCZgzNHEaY0IBM_3pDfUpQbjKphIpj8zCWXUp6CAwvk04tAbGxaYAul_oDe3G6d_5lXp43fYuiNcmPYcdsvbaLzfFqc_FOFhsCeStsoscM77rZpyVAd55Cs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وکلفت ابوطالب حسینی به رقم قرارداد امیر قلعه نویی در تیم ملی فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30757" target="_blank">📅 21:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30756">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce1iLFRtL5lb2eaOKER_NbaQeipOs6H6f-YnVo34OW3mYahaEx7l9rtX5IsD5_W6oyPorx2SqIv5KXIeE-Fdf9mvSEAbddnTPWY-2tN4mo9UdZjAFTovdoOxdQtnKMF8LftqwbVZM9Ig4FEqfpCO9plF-fA7xrlm66gJ9uBATx4up4ytbHvf3_uSqDOauKn8ic6sg-V-lBDWf9DqWxKO1MTYde4GI3yA3gyqXBr2rSNKnr3E3OpzF4wW70lrViObg6ZF5v98Y6a5sjMKbvTdMioBn1WOTPh7HJIbouf9Ppx0DxHGtL8yWb6zOftvHEJ_uhmWAqP5K0WaUxxykL9JjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30756" target="_blank">📅 21:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30755">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E17-aAdjBnWqkNuC_oi0ITb-fOg_uxqWa7DsMI0cF4bjig7kDaHbXg5g0qptHBsJ9c96rC4hEVAm-4G_N9kZ0FhTsK-rCXaCjqpo2h44jtLU-QNw9Jth_0NRmox0vygJoux3Cxj5J62yJx6BeezJANMvIznOJFUPBUmIStbZtDujol6DioLI24Q_pN9WZt9V4EgYkeTF8nv8t4ZYcRkLlvo7shm1ck7X-_xHwt4SdmPCkAFBnUiQVFLvFabBg140RHHTlPrt3MsRkr0Crs_DcOevcsXqNPfrImHyEST7YwG0HiTB6C-O_d5rREPdvzmCN2bRGVl3xpplxxw_mT_zTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30755" target="_blank">📅 20:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30754">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzlGOnabpb-3pnQOroCd9Vqd-vh3wjNOwpqdpZPpEBVIgVCqM9grXfHsvgDrTn_3ON2SMLn3RCr7RTquLMEboPsTUCmKPQlTtsSyXU5xf58hTo4S4sxrq4UTZrDUhni9yVv10B8m21Sfy_otlwI-JE-RrMwU9ua8PdH_n6lyQz0bWXGHvLGh96-ieYYScaUtGOKtb_bz_mFBOzVt_-guoktBkr5I1F-8n4AfgXt2AfvHNkkR2HA_9BW7a_qgJVn3wctAtp47Z-VVb18ncWnvJyaXif5P9-zvmyu6RCGt8LZA3ICT7rkedMWPPKrvh1-OEOFym0PjmEUmBEI_rGFKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تالار افتخارات ۴ تیم مدعی لیگ برتر؛
استقلال و پرسپولیس با ۳۹ جام رسمی بر بام فوتبال ایران؛ سپاهان با ۳۰ قهرمانی نزدیکترین تعقیب کننده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/30754" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30753">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=XZpQQFepTY_1blHwYzC7ACzGx5H-AWg-gXnH3F-QHKZRzIlldZiEGQiaV_joJRUjdAdbJtB8pqKRT7YSC0_FCBQUHU94cOQ5PC4Fd2MM5Xa_isvbODrkQMqLLAIjZyTuYrIgIPDfzo8NoQDlyeNIEY1DozaYpZs7tN7rTgVNU78k9TZeKp5ccgJ14fDpFcd-yk2z9XmllbCV0vKacTJbPnvxCm3P95u9dcPEQI1cd6b0UDAkGyO5BKa0dn4wMCCbckpE9qwuOB_ltHLyB-by4bVM46o2veMA004fSrYg4SIRVe9uN1Cor3YxeDrgxneYsBXN7qnWFhPUcNnvBo3CJSA5EOC9JegNHUx2JqV19_zkRCPAMOpAaGHmw39PlIYvIr4-Aoh6iAyMvdyvNtuKiSncn7-N-YC2fJkZ4Q3ahOkO1qMiIWlNFnm15Kn74iruje9wqH986wmaXGGi183F1EZdp4FvlcAFtJ5SCfB9SFIjdZRMDg93thVfy6FkOlp10_s4WbWVZ1mR52dQRRbxbPAfhZ2__E5ehvcS058JMgIcdNqTU6vdA39u6jFvmBfnRGBtNO9hVJBpJEEJwDEAbfSTLaAW961qAJATkEtxGrfvytBUOlUwHCtADz19MgaoEM2Q1u4aj3cucJWHlG0eUzwDJwbQdZakX3aRWQd5_WU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6481f7331e.mp4?token=XZpQQFepTY_1blHwYzC7ACzGx5H-AWg-gXnH3F-QHKZRzIlldZiEGQiaV_joJRUjdAdbJtB8pqKRT7YSC0_FCBQUHU94cOQ5PC4Fd2MM5Xa_isvbODrkQMqLLAIjZyTuYrIgIPDfzo8NoQDlyeNIEY1DozaYpZs7tN7rTgVNU78k9TZeKp5ccgJ14fDpFcd-yk2z9XmllbCV0vKacTJbPnvxCm3P95u9dcPEQI1cd6b0UDAkGyO5BKa0dn4wMCCbckpE9qwuOB_ltHLyB-by4bVM46o2veMA004fSrYg4SIRVe9uN1Cor3YxeDrgxneYsBXN7qnWFhPUcNnvBo3CJSA5EOC9JegNHUx2JqV19_zkRCPAMOpAaGHmw39PlIYvIr4-Aoh6iAyMvdyvNtuKiSncn7-N-YC2fJkZ4Q3ahOkO1qMiIWlNFnm15Kn74iruje9wqH986wmaXGGi183F1EZdp4FvlcAFtJ5SCfB9SFIjdZRMDg93thVfy6FkOlp10_s4WbWVZ1mR52dQRRbxbPAfhZ2__E5ehvcS058JMgIcdNqTU6vdA39u6jFvmBfnRGBtNO9hVJBpJEEJwDEAbfSTLaAW961qAJATkEtxGrfvytBUOlUwHCtADz19MgaoEM2Q1u4aj3cucJWHlG0eUzwDJwbQdZakX3aRWQd5_WU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30753" target="_blank">📅 19:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30752">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx4vvtVk1FZT4S8auz9QXOt9I3EeOMnPC8RLayMpBZpI9fluXq5hbNUvCTWyrXGTf0z2znoI-ImUydQE9J73EX9mjxUQ__WY-qGoHNbQd2H493NkUiKFMgwGHHsZ3Foyow3TvCkIm02caR7TrESEewL04OsnJjWNVEZzp_zhv70_mpnnmgPS3fF6vpf7oUtAgDZA4w0sMoZl294ACFfjDgdlTQ4wRN_35EfRcO-wwcmmncF6ZgtiUBHu5p-vOJ0wMkfOZcgxq3BAXhTJgIRFxix5JvWQuavkCxoMQzs-cAvnXJRaAVqmB_rD6lHHumBdzjNEC8T3cdZpdP_pZ1LBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30752" target="_blank">📅 19:47 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30751">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df42ded691.mp4?token=ee__aMiKOF4DoNJZ0fbinUoGt_Y3cy5sNOZXar1dqn_CBb-jtyFf-e4jXV39u4m6-ESNmZ4L6BkOxAGDD0y77jmTcJx9GjkM8NklFFHR979NFc3tYSoPmE2aDjVXnwfn1k83Roa8D1oRMvtO_3r_HdawUUYUK1lTM4_eC0JdG95xYkyNq88ijyJPIo6QseaGu679dH6zhI6_DSm8IDhMjlC64sDgYOkaaZwq77EuBDUpk31cxN_q6Z6cuQxMT4_0TyhvEtG52yNXz-qKWXK6JyB2vUfe7YIT_y3ef-Cwy7G22cdvJdN1yl6yU_WcXs_XMnd95zGQ-123gdA6B9BVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df42ded691.mp4?token=ee__aMiKOF4DoNJZ0fbinUoGt_Y3cy5sNOZXar1dqn_CBb-jtyFf-e4jXV39u4m6-ESNmZ4L6BkOxAGDD0y77jmTcJx9GjkM8NklFFHR979NFc3tYSoPmE2aDjVXnwfn1k83Roa8D1oRMvtO_3r_HdawUUYUK1lTM4_eC0JdG95xYkyNq88ijyJPIo6QseaGu679dH6zhI6_DSm8IDhMjlC64sDgYOkaaZwq77EuBDUpk31cxN_q6Z6cuQxMT4_0TyhvEtG52yNXz-qKWXK6JyB2vUfe7YIT_y3ef-Cwy7G22cdvJdN1yl6yU_WcXs_XMnd95zGQ-123gdA6B9BVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از ابراهیم‌شکوری درتیم‌امید تا رحمان رضایی در تیم‌ملی؛ درجواب‌ناکامی بگویید: یخورده سرما دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30751" target="_blank">📅 19:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30750">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8_dFnCan4xeTNw3nEEm8DMr7djhvLY89jtigKAUPTIMcIzEcCGYQMYpWDL_1RGxmiyrXqaDtEOSTJzMF8MUSsI3B4q81LziPEb7_y-FlOluCRsUE-H61lP_fIxVMW4ZmiF3cWhnvn-nDcn5oK_sZg-mDm4lrRcm0t6TZOxlLV7e6MTY37hkAyWhlW315MQysHUWIwVnsYK0WlLLxjIWgHf6rTolpbGpqqqw4oxAG8Qg_Cz3cGbRSSQRsAttFCbf7-0I12C532x122vRR7gIhk7AwCqFkmqixgChuU2sq884_qggNXnnLPGc4FB31d_I0r0ZBLp4VByqmzBIQJtE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رسانه‌های‌پرتغالی: کریس‌رونالدو بابت اینکه دربازی بانروژ30دقیقه‌گرم‌کردن و وارد زمین مسابقه نشد دلخوره و درخواست‌جلسه با فدراسیون فوتبال پرتغال داده تا تکلیف او در تیم ملی مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30750" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30749">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=M6VxxKReQPo7ZULVkhPMN4MqplPbWT7kw0P48mZenczJXp9xHBq_xpN6CZg9WAZ0kp3m8hrC9T_g2FpvBrADoStBGcqncpY6vDy3WL40TXsGdynrvdzVdfaaMiPMy_VhSsvQeMUmSOTjFNeEa8vb9G45WtBjRrjjkGkOxNB3QimPdbgxeomkKAa9MEqf81viLEM8SGsOajFhs5xJs42GUjd7cyJWxIGSl3nQi-ZOeTP1PyCoNI93xbWfc-OKHc1hZ6BQ8IeOk_3Wc5nnu5v_nMZslILLrZWfurTn2ROcWrzJ8g1AKE9Bd-yZm06GEebKLtjpQC8DYGiU4QPnixavAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9eeb9930.mp4?token=M6VxxKReQPo7ZULVkhPMN4MqplPbWT7kw0P48mZenczJXp9xHBq_xpN6CZg9WAZ0kp3m8hrC9T_g2FpvBrADoStBGcqncpY6vDy3WL40TXsGdynrvdzVdfaaMiPMy_VhSsvQeMUmSOTjFNeEa8vb9G45WtBjRrjjkGkOxNB3QimPdbgxeomkKAa9MEqf81viLEM8SGsOajFhs5xJs42GUjd7cyJWxIGSl3nQi-ZOeTP1PyCoNI93xbWfc-OKHc1hZ6BQ8IeOk_3Wc5nnu5v_nMZslILLrZWfurTn2ROcWrzJ8g1AKE9Bd-yZm06GEebKLtjpQC8DYGiU4QPnixavAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
به بهانه سرباز بودن دروازه‌بان تیم تراکتور؛ وقتی‌بیرانوند از خیابانی تو خدمت مرخصی میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30749" target="_blank">📅 19:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30747">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nye3yVewgxaXcT2mgHbfgeZHka2gNY7I13ybNGcZCR3Op-KQy5Evw-OGrlvckIx9hjodZQIasM6u3OyMsv1DN0UVWScjkVVm1szI1lXLnD_0pebD2lLQxA1tgj4wONZF-n7PyjTEU-GST6_sUd16JjckJk-nZS0btLUgAmlIj6mG_XmnmpmVxy3HGYVyb86g6X6oZpelED4Z0hi1oQsU_h02aQQDhI_KkV58AxCPcfDTKkAaJ8IetGnpkY30pgqMr74pDIRgoxpfTXQqbkY1M5mg9e_5P75TGMDhCV6DrKNP1RIglO0NJChtlnf4Nl6ZIxTGiizKP3w0SwbPIzATiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30747" target="_blank">📅 18:53 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
