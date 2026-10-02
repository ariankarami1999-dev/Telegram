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
<p>@persiana_Soccer • 👥 421K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 03:23:49</div>
<hr>

<div class="tg-post" id="msg-30886">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpdzsFYS4gacJtCfBQ4K498KlhCJGzE3_NRJNE9cYcGOpclozrckXjBYiuyb4JbnwO8m7ZoeVJuC-T74XKQoBZdXzw2_Yk4psMMEVPpANUjDtX21WksJ1jdxgjjX_mQYKszJkLZGoWJZM186GPboEV0h5e_GIiOjFepTwzrvA1tL1lyDLfWJNPXPoiE_UZyL06SSZ306EDOJ1UtMTpfTuNA-l8geSYTADJKKuPsrV_eTS3J1w-mNuD4kaHvmXVJIkhD_xvPJbOrQSM07MjLw4Je1xcPg9XrxmfUEZL-_TSUf3tm4tKaQi7BwImIn1npWLg5P1dhWROTZzAk2XYSUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
🔴
معین توی کنسرت آخرش اجازه ورود پرچم شیر و خورشید رو نداده؛ وقتی تماشاگر شعار دادن وسطش آهنگ خونه، ترانه «بی‌بی گل» رو هم اجرا نکرده.
🔺
این اقدامات زمزمه برگشتنش به ایران رو جدی‌تر کرده و احتمالاً خواننده بعدی که باید تو ایران منتظرش باشیم معین.
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/persiana_Soccer/30886" target="_blank">📅 01:57 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30885">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇧🇪
🇧🇪
ویدیویی‌زیبااز دوسوپرگل استثنایی و محشر کوین دیبروینه 35 ساله در مسابقه امشب تیم بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/persiana_Soccer/30885" target="_blank">📅 01:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATpUL3dgGz_kH4E1k0NCgD1KWv8Z25CPC-6EiQ0s33ewqr5Yf0Old2KQaWpyhRw2raWOcNW9KqATT1zBiGM_H4I7ZTyOHKMOONqfwiNLwDXCdp1stvr7pJfMEmhv7EM3IKIEUSkT9EBytHMNR7XhxRuIay3QbKjHsI2vgdGw7R3sWedYRvThx9VCx9A-pITIVbLGFOcTEIDHUEPEFTZj9raW9olQlNiRWV4NShwa0kEMeAvtR36RYxYtGT3s9W_RSbuJJqbkukZ6s_t-puCRBz-GPV3s20s6JFvVQ_9UtGT6Gedjyg4XGTfLWJUM_L-lGmsiPlqPXWwoTaNlZg9gug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی دوباره انگلیس و کرواسی پس از تقابل جذاب جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/30883" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEKUn9PtGWUknrfkSzvHdtXd7Vm3hPFaSwjSju1zgPn7TvlwQQORdOTh0Fp2a4OFxOY1Ms4IkuZ4zhoBEZXGETS1rfnmBEGcfUJfYjsx6rua6LxUIbTGjZOiMdx3zQAwOfXIGwbObyEYhj167zhj8z2SuLGVru6RVhM3rM728Go1qn2zPMRE3qBgfTlSYbTGFDigNhUDS-zUsYxLa8x2kzxFS7ABuS1u50URztjb6vZS1vT8SMSxDT0ceKyY15Sc2agQHVqRKb7AiRH9t3H-iUhZ7bb1kNzkrNIKCQILTrMlms8gZFspQoogF-_vNzuh5IL6B1d7c6Zt0DeLyi5RMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
توقف‌ خانگی‌ فرانسه ده‌ نفره‌ برابر آتزوری در شب درخشش جی‌جی دوناروما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/30882" target="_blank">📅 01:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30880">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب ایتالیا - فرانسه، بلژیک - ترکیه و هتریک دیدنی رابرت لواندوفسکی؛ لوا با این هتریک در تاریخ مسابقات ملی 92 گله شد. گل‌هارو اصلا از دست ندید فوق العاده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/30880" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30879">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX5Bf0fHXDzdP93JY0u68ELL0sMMNg8liPLfISVa_2MYE9rIoreN29tpfBllzwLKtPeIhXJJq2tehxVH9bfMD82eNb8fU4Y4Sj2SgWJavLjA6Zihk4Ew2ATquODvpL0pygQ4OeICH-2FW0k5iTAMOoDJXPUqm2vdMWiCCH8qIHpw7Qt_2V52gauB_6yBMLz0FBp6wCdraun8wzXSS9AVCI5fDZNYypaF5xgT7sZ8xWpE3vttVoCI7JAwhWP7NpIjDswh9aQmk9cNBr3NEP_u6VG4yGiaYT3MIm8mmttGGYfMZC7Gxgz6WX9WQe_3CQj5gDgsrzCW9jLt3t09VShriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔴
پوستر رسمی باشگاه پرسپولیس برای زهرا خواجوی گلرسرخ‌ها: 2 بازی، 2 کلین شیت، 8 سیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/30879" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30878">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxWFQPhgMUodx0DoM29WbV4ucdB_jfnMvQPs6NnnbgxLR3fRFrUG1EISmd1Iteq34etNRAwB3e1QIt2xSuvEx8wUbE-0o_Bv8NyQ8fPLfc9xL7A9FZkAtHoQOy28kg6onoIMRpdbSksEBA40mCAEH101QwKiBwUJzQwgox3UZeP4LGkMhI2gNgHZeTdPvRDw4MSpAhzmIUbt3Lmsu6Y5um6C-GzWO-tVMLfXpgAMCbRrGUzbl47abA7KRBT9qr8TRrFFr3I_d0K52NVDixyx0jk_NDTfUbzc7ac7BIeXEjiPgHzl6A3I3YAIR19AzmNZgkpDsYwzCEGP9HLK-x7kLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های‌روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های‌مدیریت.سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر! P۱۰
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورودبه‌کانال‌اصلی(آنالیزهاوفرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه(چت‌وتبادل‌نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/30878" target="_blank">📅 01:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30876">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKoARRh2U9b7BrxcZrzp8tJaSaJCFQmkKHU9TRmV9PE47jyzTJGvAX06r3IFZnlhZBLPS6sV3CmoIuLMJWUZMsRtFLgwNZ-6Z60LeWiwtZj7nMtg3R4M_Ja-f4c_Zw9-hx8I87ltjzujrSQwU6oxRg6mVtUE-2rkeMJ2BtyA8Ln7yatwlhIv5jK_mqeNNh8WP7t0asW0pLfR-oArAjdhpvCFoNYVU5Sd_EPM1w6n_IgJ5UCC6Xv7w1MLHYc3b7iMUKRxFhdD6rPxxnL6NpjRKdwuhqCBnUAuRVFjQaUAocXmst43RM5ohDRIyXOjltA7zjV1-GNzeXIO9agTipjyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه A لیگ ملت‌های اروپا در پایان دیدار های امشب هفته سوم؛ فرانسه با ایتالیا مساوی کرد. بلژیک سه بر صفر یاران آردا گولر رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/30876" target="_blank">📅 00:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1WhMUhwsFvDr2ANcDhuv9U4fBOGSaLrhBqGdTeGw9oRT267ItoLaKQssXmlOs2Jgc0DM4D3JG1iIoNkH09ue4zFLuy5Z1TW_9t6-L2FmFZBq7hlyXc9WCO5FSpTn0KQmzW97wVAQXz9IG_pEP3K3TVxJ7fJvB4gcBXCzxfS-EYCwuRSAmEVcVYZn9o5R8gOh5boGEkCBZZWO7WepLNcva9l_1zzNm77vVzlIafV9ZASwZ1tRA4Fo_Nm6p4D2UgoC6AZpUJAXJd1Nx0g8cnR2cK9iOXMXdEqcLTF62Pw9UKmA383gRYNTnfZGBy6FN0D3zwGnCCD6byfBD4cUYztug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/30875" target="_blank">📅 00:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30874">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKyc7dAZqqlR8AkIRCcpud95jHCsBIpUdiZqhSAbUA7k9OZdUGtiiUl8iC3Hrz0H_6Y1iKK6h3bFHKomnedDH1NvBss2w-p1f_rhdaQoAS30K6qOwHADgvJPti9Tb5gnyayYboxkTPweeLfi6lv2keRSjmR8o9WKNxQ7v7rRHj7LVSv9IU18njQMtUAKgadnoNQZMyQT6VIK4vRjggNIqWFWPHoIRRP_Flc3p3RLVKGOIob3KNwMOHlpUo6wSpvA5SFOdr4G-t0buVEz9PNHpQmu43E6iPHypiDswrMOWBZNvNP8w9Pcv2aWei4WBkHlbdy65vtTsaXVizVv6zOREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/30874" target="_blank">📅 00:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30873">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnhg4x137I4BB_Wht8ZkNRj4CW5fVGXYE98ZwJg_JQb34oqLyGTuqvk3-UjfP1w4B82OE3Uni4bUvvp9di5zX6sq8O8qJ1au5SHNkApxDaoBr4kfeKUmos0oDyw5LlV2nIQB3eL2i8GOZPx_PphXLvJkUpj8GNo7LIhf51aT1kgJLALPwkoSDCCv9Yx5j5p13XXt5E4TtmA6FBmUQBhbXoQCoTF8oXUKZ_Ux3GcKBH5QqSkRBOM2qwXfNJm32sz6BpFf20hxYPapzMEMOM3jy11MTvsdHlsR9w-G8BSDyPlxLRZysmWlS2B1kIp3kAKB4jaGp9zubDiVrC7aMqIALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال فوق ستاره تیم ملی اسپانیا برای دومین هفته‌پیاپی بعنوان بهترین باریکن لیگ ملت‌های اروپا انتخاب شد. اسپانیا در دو هفته ابتدایی تونست بادرخشش یامال انگلیس و کرواسی رو شکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/30873" target="_blank">📅 23:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30872">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWH05AX1h6DMdG9s_Cb_8hjE60c0ixGEqPgXnpal6Kp2lc6lbMC2bpb9XRQW_nyNOvIz_xx8SxW1mz3VLEx9E6iyLnFoWRqfXIBEX0cjjCKqp1Z_F9TNqEB7kkKh1hdkcgzgjm-_yso0-dabceQNdPR1Te-srZxwZT_nGFv7_00TlinGUKN3A0CchnJDl7WcuLoAJ8ar4UIi9hHRrfA2iSIN6aPLmOs5LebSkysd8gZP0v-1-mA_ADnSAid0a6W67H1fbpgBEw7KagL24sB8c_q4t-hGND-k5jCKt_HvaapaZjed63ToNenzbR6mApWGBr-3tCLpe1G8qpDBPznstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/30872" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30871">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQlh5E9IqppVLlBZLXdwmLakWcQ96wQMnNPqq3TmKqTR2EuGzZqml50PX-e_fBC5gzObaEhYx-4oG9WImm1lK-wvmVdPrUdv8T8jZADVKEDGB3E9RQGxxBTryfdowTLXbp9t8i2CPhxc8Sg385jmVihvf0_01Ybt0_ljq8AgjOdyGV29V6--rQnSKUbjbp_jCysXMLelGd2nHcGHl0rPqOG8KGa2J-xfmL3F9CJRE12BNKzu2I7doosJCzBQPtbHp9x5zIbUnBfgkLWkPM01U70P4EG266nUezM_XlkZYhqhqNFRWTd67X6NBv7uii6lbQcKu5zIubLjzCDaRNgJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/30871" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30869">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apjGryAQ5uVe8wnJP_eHUfXITu-LoiCVobVwgTkspMH3nlnutn1dIxWN_y6z09s8bv6ucHCdyOnTFUSxXfjAyUvL6wS3LlpAHPGoE941dt2jbD4h3liaDrIv3Syq1XgMC3__TcK8pFZEQAmvtCFMngRq8YnQVvZQE34KEw2QOyYZbo_MzRRxWhCkM5Vmw7uJGUqpyW7CsV2pKB077XHf72pjqXP4npxqGnLfQSpG6PUemmFIIWavoYo73Lgk_r9n0rHHCPCLgpa3wfkruv6YmzlcxtwzBGdf8KTGJ7lceBFVPxomGZvTdoNAAdJxy6KI7XwRqDvM56c1STZI48lIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQOy7K4uY-qn3MqRntQJSNt2OEHYtwL_4d-CQTVU3LJGJh73yzUFA8sg1pzM4EgLdAGwI8kLXJJ0Ln0HIPexiZWJInvBwcpQ4Q3YJUcdVnecmGFUc5b9JI8dgqhkpDOmDamPsXKvp4DT_WhsVIlwsdn_kv4JoRz9IGy_qwEJb2aM_Jq2Gf_Xd0GA-f50X6_hHQHBIyqVw66X4RQUto4wW6ci8r_HbEIieVXeby_wq9w5SJ9euQvSAQwbAjN9Y9Zwa0om6t-L8C_B0uQ2pbrjjgsCP7llRPY5IUBzz-Vv8HMwn_oZgx4kS9Lcv87bJbSYCsThtCOF11AKbhaBuli_aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تعطیلی مطلق استقلالِ سهراب بختیاری زاده درفیفادی؛ ۱۷ تیم بازی‌کردند استقلال تمرین کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/30869" target="_blank">📅 22:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30868">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=EQXffSY_t6yFcv1xBbNuGfIb3sGo-XvmZM9se4O9tr9ggz7DlBb76l9cCIaKf9jFL7k-7YTYV7WH5pgCHyjGOczKj-dHqU2CYk9_DXxGe2hHHzKAAvkLLhtcp_BWpsFHWjQ0rIQ7dEqonPIEpo_3IQugg8XcHE6is9r0rEbYG9DLvJqpeMrNuuLi7fokWCii5LRn30fYipK35x5PJ-YgtM-tMkpdw1M_twfx5t9oQ4v7Ae71pqsxcMLCUbtpJkj54EgWibxv_pEChd8g0KHfMovG7k4xSYECBAq7WTFVOjt8hL3b8qRHy5CK4v0440OnTNfqnWUNyWg8eYefZHuCRLgLUI-ECPtIl8VXzODBPUfy-jUZIz5Ge_etTY6a1YMIOrQZulns6D6ejeTcz-4n11Z0Wg1kKI44ysLtfXOVtcpbo6ui_IkN-qMJAyeIUuJLzd6VCwxUgKMKIAR-DT9PX7nwfbL7-w-1lfCP-JPw5jCPqUJrhyzcJ-eG3uuBszaPUY6I9Wkav7LnOrwYWMjkQY3bxax9lCROwDDX1foeEFIR86Q_uxABi8y3JgelD9d6J1kstR_e1Pt1vWOn_mhutO2mMTlVXdHy9aTaTOpNXF-WH9i_9KqKTgCorvJQeArlrl7Wpb0JobOWmY_HiT60f9DT_FmW_iKGxPwJFFhFehU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=EQXffSY_t6yFcv1xBbNuGfIb3sGo-XvmZM9se4O9tr9ggz7DlBb76l9cCIaKf9jFL7k-7YTYV7WH5pgCHyjGOczKj-dHqU2CYk9_DXxGe2hHHzKAAvkLLhtcp_BWpsFHWjQ0rIQ7dEqonPIEpo_3IQugg8XcHE6is9r0rEbYG9DLvJqpeMrNuuLi7fokWCii5LRn30fYipK35x5PJ-YgtM-tMkpdw1M_twfx5t9oQ4v7Ae71pqsxcMLCUbtpJkj54EgWibxv_pEChd8g0KHfMovG7k4xSYECBAq7WTFVOjt8hL3b8qRHy5CK4v0440OnTNfqnWUNyWg8eYefZHuCRLgLUI-ECPtIl8VXzODBPUfy-jUZIz5Ge_etTY6a1YMIOrQZulns6D6ejeTcz-4n11Z0Wg1kKI44ysLtfXOVtcpbo6ui_IkN-qMJAyeIUuJLzd6VCwxUgKMKIAR-DT9PX7nwfbL7-w-1lfCP-JPw5jCPqUJrhyzcJ-eG3uuBszaPUY6I9Wkav7LnOrwYWMjkQY3bxax9lCROwDDX1foeEFIR86Q_uxABi8y3JgelD9d6J1kstR_e1Pt1vWOn_mhutO2mMTlVXdHy9aTaTOpNXF-WH9i_9KqKTgCorvJQeArlrl7Wpb0JobOWmY_HiT60f9DT_FmW_iKGxPwJFFhFehU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ صحبت‌های جنجالی و عجیب و غریب حسن‌روشن‌پیشکسوت‌آبی‌ها درباره ریکاردو ساپینتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/30868" target="_blank">📅 22:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30867">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yo2sxQdwBEzwd4n4e3YUqR93lAtOB2670w4M62IranlkxkqmtdajesIaU4fHb4l6hMFY14k3_GrixibOxQtXJdfXtmLJHlmj-oDErNTnEg8D-1nz5jc935xfzNG8iDFngEwiN6OJn3JE1_oh0pD-ZYi8MAOJqXB5H1dJsWpi0zyjI7ntbGXC8-7lBPAHLzc2kF9RI4_7m_6L_SHZaY-uNyrsJvJVHU6Ru1YQ53az3Ffs9uyXaMVixZBfU83v2Ru29qmltZOTjHdXgiHMxdcn3rv34uXq9e_HJzdVPGJsLgEZakbISD5cGeIkxzwODRNQtrWZ8XSNRGchR2jqVzpLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30867" target="_blank">📅 22:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30866">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYBmGMHPZ83PbM3fJbMy-kdr0OrGBjPli3JDJ7sWpo2ymjFVPdQRCsIEBpXg7TdkZAYQP5ZvIjKADykYu2YCOyJlEevUbGra2QFwas1r8JZw3jwfecPSzd5hFjdzCnhUdJ2HuTOoiezTDGjI4GJ5JojMxsySa7yFDkcfSxrNshgy9FFu1zd0p7vithRWOo5V3Cbxzi2Fw3Ft9PIpeuG7_uAtKcTZDg1E3_TqlwNXihVc8ivaVq3P8fO9gtrUlHrs8CcF5Hc0EoT4vOgNenvj6im5HzKFjsKoTsW18Czr82qsflv5EK24CrN0vzrpPWMUq2sspfviCiYPbvAIx6JxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30866" target="_blank">📅 22:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30865">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJIjR8DtktUepmy_XUoMvEBN31xQaEDY03AXeIMC3Nqr3Oh-Ogv7ANuSr1OLEJW4jWQAxFbSXR8LXlQAs2NgPtZMZz7rFTQhU4Hf4l8NQhT47wk5FJWrBlKT2ApkYsFpIBXliiiupbCf05VgShHIWMB4n0iL430rZXHRU8DqcpZoGPxbEmt_BK8anMTqYXC0Nf2yr082bAs64k2aH02Wb26jaxWvq2493bc7ImQhfNpBk1iNHzmrGf0n9JHdN8lJqIaVz7nz-3pvnm7eaxupIh6Qjht7KfyA__5PUWiRvjaV7dv3XzLB_1qZq7Vh9wGzzfKcK2xaASSXjYtZ9Skhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ به‌احتمال‌زیاد رقابت‌های این فصل جام حذفی بانام یادواره شهدای میناب برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/30865" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30864">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0w2dcaRotsHZ9T-vnWz5eyeOVOAUVukmy9vdpGBtESiPvELcLY0VznKCacU-UnbI53fsP-CPHL4OoOznFgqnFVresC5dccYivpNhg3hTaXmC13FibgN692fR-RaoYBEw_Sa6yELOqC3ev7VPM7xRvLoejooItdTNK9UcUsn7EoBSISzQqcCc59Epq4-17MsWFYdcAi2N6_q2sqoW8zFo3DxeOeSxVht_ybvX_zBe2kECtcC4yxcCyJXAqATbnZid-bWd3QJKAIB9N0agVIA0-1J5LD52oiyQOUHA-3_8iNh94zR5vIXNhckiWlr7hN29oyJD0cTDgyYjPImgJqhgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
#تکمیلی؛ درصورتی که حکم نهایی منجر به محکومیت منچستر سینی بشود؛ ارلینگ هالند، انزو فرناندز، رایان‌چرکی، دوناروما و دوکو بازیکنان‌مهم این تیم از جمع شاگردان انزو مارسکا جدا میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/30864" target="_blank">📅 21:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30863">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s35ZfaxacP2bhzredafk8Tpj1Olq2H2yBNkn7sxPtByXpCeARM52XlwDhSAPta2OIw2d2s9fFGMCByLYgWg_HRXfIr29UeSGyzk98K8DqKX9RqsgktUjdKqEwU9G1FKxhyPXwjHs6O43Cc5mcEsDcbJBnIh6Hhd-qbTPg8DD1TViS2y0PdcHG6mRcjHiKGHiF_JyQ1tRmfmIXwGQovQ5k4hfg6BRbtJBpe7FeXWJ3N5tSPbSzB51Ad1EwOBIS-eNR3qisYjWbZBrTZlbecNTQIpDRaPifM5U_AaVlEVpln3gtC_FLnUHhnLcq-u6Gt-43CV_PFw3YufIu5N3M6UroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین و خفن ترین ترکیب منتخب تاریخ فوتبال از نگاه دنی کارواخال کاپیتان سابق تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30863" target="_blank">📅 20:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30862">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw_hw1cqPJsy2PP9LTBocbbC4YHErOp8KXGHKiBBuiD4NQynSxXZ7lm-YKPIpz2BLmH4MGlYtpWOap2erL8ZAxiSRjwkQughulZbAOg4p73lyHwlsBiC44GIsOyM7H3YEtBb52pSqYqVtta-G3t1Us-zJJ7f1WpgQCKEe9is3e40nR8Qp0cW9Tem483YlU1BlSMHy-E0y-b3pm8nOgknc2k0xVa8vSqoBW3rKmnnl56RlClaEsYXfTU1BhGzK_cu-eJRiWjFoLJGVn5q3IRFZXM-EzjowvqZK_zpu7n3800un4zVeifjvnIJB7bFPXkwIa7LS5EbF74deL5zIHM1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30862" target="_blank">📅 20:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30861">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg_69NKyVAINgwfeRJJWTRGhNXhjbDmyvu8H0-bACD-MV4qlq-pPI-DIApfqcmOGWezIUos57Xo0vtoXgdq9nsOLBDM5YNmklWGMRLm0QhSKwKrRTt91Nueb16i1S1ipoT0c0__aM7pvcchxQJG6hFTiAzFq_KWua1rfOSWwcZ75oL7wo6T0FmkraJaboTCTaY40tHYru9qlH8U2khNN6AEUPiEvGP4awDuqT-PWD7QpgaPheBdVEIKQJD9AD-U3Qtled6_Sj2O01_odSf5ftqKSGM8Eu8BTK8ZTEeUAA4FsIRa3tgoz_a5BiS-tQsGQJU5axdjuqvcJAzW_lt15Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/30861" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30860">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grvGT7dbuUFOiiatpjQiAqrHbAn6DKCyRa30cFk1b0SifM4KsJ79sK19PTDNgQCq5eWEMVQbnIMGb7eHMN4kamNOFxB5O0tOWX0XAOhoXvwTz3sDNNYvt4eRtttGFaqv6YfX0JkENd9VPBuWc9_WBnordmdleSKooYLKyi4hpWeuoHMjz8oJEAwaGr8D-L7qXVgT08g-yT9EiKNAUZfs9B4OKIfleJ7-o_lX4_BBJKMckR8QgSiOon2HJneET-KmXvFqEAMqE6tKp5ibRvjXAEdZlFQ1Mnrc9Yxn4O-vHFWAyrH-o7DlBpM3IH-JRJoI4CNUzD3w4DkWfQViarYzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30860" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30859">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6FoldrX-qZcb1-CjxFyFNT2sP7IOhmkTtkMBFPUwRX4XeOmTdpO5cknsjxntitYuViL6w43IwLtPTfRUUa7rfzxabq40lLhB9bqCJEDb8iROy1J-JZynyuHpnhleOKXuRSV4xosx-M9hXxPCjx4RS8fQ6alT2wMUa1tmOT81bE9MDwEaPQuDhfFZ7ms_9n4V_dOX905xiRruWJXtY7H28i5rtYxeW-ueBoK3VULHeQWgslKYsQPu0E42fFA1ZOoImo3pcCko23xjx2_krhtvJAitEjc2ldPc36R9Dl_6HztJcrb1vhBcfkkbqXUw8AuCN-ciPGcRx4vwBzozjU_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
g10
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30859" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30858">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=fxUbLTbbDFQXxJQkm0Kmn3L43FkeGpRFOTuwNHxoF0-9vqcQICqkTiEvf51zJ3a4aZTuv02dzfvTqS29yErAqDwtBBkuTpVCJnBREOeMmPc1oz7ATqp-Be33_qCzQYwuDisPDhMelQeOoEJoBmng0TLYKFbqCccB0751d6pfyjEO4-VB7w6xw1dHIprPy-tF_X80tcwmYDAYrtQ0-MExE73SPr9i8OBAmZH-bGsxsIgKRIvEVXCpxGuxcFmA-hj54QGGatAyrrwFPGaeITDR4t3jbz0-P204woLzATgaeSuVbeXYRTgqSUpf66jRmM-3g-JriZ49Mwzv6jIYwwitcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=fxUbLTbbDFQXxJQkm0Kmn3L43FkeGpRFOTuwNHxoF0-9vqcQICqkTiEvf51zJ3a4aZTuv02dzfvTqS29yErAqDwtBBkuTpVCJnBREOeMmPc1oz7ATqp-Be33_qCzQYwuDisPDhMelQeOoEJoBmng0TLYKFbqCccB0751d6pfyjEO4-VB7w6xw1dHIprPy-tF_X80tcwmYDAYrtQ0-MExE73SPr9i8OBAmZH-bGsxsIgKRIvEVXCpxGuxcFmA-hj54QGGatAyrrwFPGaeITDR4t3jbz0-P204woLzATgaeSuVbeXYRTgqSUpf66jRmM-3g-JriZ49Mwzv6jIYwwitcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسن روشن پیشکسوت باشگاه استقلال: ریکاردو ساپینتو تو اردوی کیش هر شب دختر میاورد تو هتل و ترتیبشون رومیداد. تو سعادت آباد هم خونه گرفته بود مکان کرده بود. بعد از تمرینات میاورد تو خونه و شب رو تا خودِ صبح با اونا سر میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30858" target="_blank">📅 19:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30857">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Fi1OuqewximiUnwO34HgmVi2UrEw-L6uQZFx-15tyzOOlDxI2wIrTpZRapI2K6kPFGz_jyIFxY0R57is9F2-6umcPIX6Nhcv_xU6aVcRsQaXoX9-p5EUUX1dqEGWzUPk_p8pqJy6fRxma6hyiENPsxbegZA5nytT44nOh5McXyrUmBA8Wpd-bWD4Qdzbe1AhHd6-39zPiTOmODPh6TnP891fBO00dlTulW1a_6Il1USpMBEwr6ntllOrV-IG3BdSCub6wexyBkxCqz9jE8nCXFK7uPzQ6e3bFV8YfklU8fmQsbCzJeYfJRpWD1zz1kbWV2Bp23_4YewPGcv-DKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30857" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30856">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFcSD2lCyPVoiuTER3-fiSukSsRw-S7KA8iewf2Y2orYHb94JOxndUKuyyWqt_KC458QlTQ_AZnXz9ZiGCX4UjA5XdrXKPmUqnW23BhgFcDxohL0tMWrtb4TfNWe9zghxptABa-sbb0N4ENf-VtXvgJ7iGxKA9_qZIMHOqunnkVqUygonU6-nr7tny5LD4elfgtZk6mcXB4YjX-O_Dh_1YMWn3pHx-W-8y43sYfy0VixOTwEacYwAdUCiEj_VBQXY7MW4kErbgZVDWeaKjQgEwsJOLI48K7VNHzxPfFYznl8jgIILhI_y8Xr3YPTrohgx5HNpAxrxLFLjNGK2LgMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رضایت‌نامه ابوالفضل‌رزاق‌پور و یوسف مزرعه رو هم300میلیاردتومان خواهد بود که باشگاه فولاد خوزستان درنیم‌فصل با فروش این دو این رقم برگ ریزون و سنگین رو به جیب خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30856" target="_blank">📅 18:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30855">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2DqSfA507iYFmVsQRnOzCDeGzu0BIRJTsqYTmQAcNFdefOIBPOMmr9bKid9BEqq4TzgdDYGC3icSLUJF83KO8lhoVdR2ScSaGkkLSvQNzkFu50T0lY2Jg8H8BmjrjnLpjGMNMvbybZlJpljUMGDAaA1OQabNWRmr60tA7tO3y58aQZC_zGuwzVpClAOSQc2nbLQpVUi1zT5lcePP89DyCjwrFAc6ITsujswtKGFwe485adPLIzwehu7rdO53g5GNsunHRvo3T0kqm9cJisxkt0ADLvMKNiNkqroI0OdxlLoFBk656Nbzv044wyARC-zx6XvgXPBRUSunvETSH5xOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
هانگ کانگ در شمال نروژ، با جمعیت 2484 نفر، جایی که خیلی سرده و یک زمین فوتبال زیبا داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30855" target="_blank">📅 18:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30854">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks-YBdptQyimX1T0srG6d1zTiVl0vGSVFrscuva4oQYqeOL6wFYzJk3B9193tijlIMOtX2k3FEXaOrhAvjk85K7biv8w8tGOM__O5h5V5DC_1mdzpWKLrm3p_elIeISq6UBRxZnxYNb3HOBvodNx2CfCHgsnCBbKen08jM9FR6I9XV9QYfq9tOXsHaiPvnV8HF_ChKo9DCS4K2HYLZZd3Yqcg5ZYsT7FafpPj8XYIoGhtjGazdaZgICWE6sdkQWSNwFKmTsqKmVSaDCyBJ6OAuXlWgiQjGOzXEPX-HBWR0VitV4qmGyBQIElp2lyYUoEPUI4we9GDdlOqs8WHP_riQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30854" target="_blank">📅 17:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVZ17Fjeo4ryLZGvRwJ058HTG7GjbRaRGgKqF7XZrrTtPGtoQmWiNp7IblkcjWloKTVF7OvjLCNJH7beTvSIfkOdJqltlLkeUfA6Rj6xZnDzkVLgvekpubkUvqASaOh3-iA7m_bfyJ8AaOwK29Cb6kVgKcL6jjYpbZQyjpEzEVf8gnhLnQ8_QkYZENVu39v1J2W7J92d0B50tHqysTFip4tdY8bwLl0PT7BRGj2LTPpGDn2wRhqLZhsG9GtO4TP9d2_K0CRI4AnkhYKzN2Dwi1RPerxUeYH82PT27LAW6qPvSaXgpAPOEhTh_WdeAH7ojOrV16-_mEsr0wBzaerw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30853" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30852">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUvVWhHGSekgypz0utF-3YYUhU0YSh6LLBcrusjhq7mCxppbHcFDgZtRRjxNeVTyt4NZ-T0WVTQnvOEvUZo6UzjVYfCngS00NgBXLhY9OMbNgOEiwRICSXZSkOuazJESn4AJKz5Tt-EgfZ1zAmBJcBbcd2MugVTu6JhgCzMl-sogwJbbi8g0LyVUnre8v_iR40BcZBxKKuybX0dcfDCEgxidVZP5UouZtzov6SRKaRyA1Q9v5T87uCBPFC3FX2JjkdODYSQhopTAQ29wWpy_cbagmCDljeHC6zkG3esU9lf27S2_shsD5yPXiO5sDIKHqHbxQYBEuGBdQwtTi9PDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌مولر درباره‌بازی‌معروف ۷-۱ برابر برزیل:
بین دونیمه تورختکن‌ما به هم نگاه میکردیم میگفتیم چی شد اصلا؟ یواخیم لو بهمون گفت نیمه‌دوم کارای عجیب و غریب نکنین. نه برگردون نه دریبلای اضافی نه هیچی. باید به حریف احترام زیادی بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30852" target="_blank">📅 16:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30851">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGyZ3Qd511nBD6YZvkZuRJLur0bTua236lKplKjhfRo8UaebhmBKQZvqplasoFTW75Xo2CZ9JCpK-HxvYvA5WY-iAwHdqu5Wnrc2dGLtkfM_LJXNjTSo1y9KrxAE6IVOD-YcAxNiTy2sUPTkkx3dk8IxEqQ-rHadralg9U5Cyj3HcidDIlZMOMloYXsrnXc5ubkMPrCY5xovU-_cUytFo5NfNhrZxJvvlett5YIGiz6fOO1zGdm_Z2KG36UeGNZQjur7rCZPaDmB_u91OgO1k-3WeH5zSwXSXggx4lVFXK3d1469ulVXCLt0arZFvngOcEieUECnnE6HUjFWZ3SS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی که گفته میشد خورخه ژسوس در پایان بازی‌امشب‌برابر دانمارک درباره کریس رونالدو خواهد گفت و از او بابت‌ این‌همه‌سال حضور دراین تیم تشکر خواهد کرد اما او از هر سوالی راجب‌ این فوق ستاره پرتغالی طفره میره و جوابی به خبرنگاران نمیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30851" target="_blank">📅 16:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30850">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqqSF1I-aYsevE5Qi0_OhHwgIBV_kDGELgwKWOg3uBVP_3ntEPJrN0irghcCKqw-eN6CxPVvWZT9SNvUwLpIUqBZmksEO9Pe_NpKT8ZRFr5KvMNbSaqOULEviPEyeMAW1zbW02v3UOSasCALA8-nWrjUdaCXiQsixdPGf439xzDhpOD1ORRwZRriQ-mVRYWPbeG8h9i_s0a-A8JhUUOpL5fW_gNRa4miOPWKBnXgOVJS1zo-hLr1i6s7MoV-ImzByJK8i3se__SFUmQrpeWKNcKz6qGsyK_UJV8JE6ihktBKXT-zp9ZWD7vEBri3Hc3IjEdu-CZb5pmnTdqPFrThIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت‌ جدید ایلان‌ماسک:
اینستاگرام فقط واسه دختراست اگه‌پسرید بایداینستاگرامتون رو پاک کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30850" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30849">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKV4EWsFiGQn6rF31W57fc3MNmtj7RJWK1R2qDu-5S9uGYnJZ65C9JT1M-EtXt9h8rYu1EiYzuD9oiO-18-nyEUIO3izNvx0sVXkSh53wMuMTqNoZyulRaSS3COCYOUGvfPecr9Vyq3JzMCCCdbG2VOrwsn4pyTcEpMDtXBFE6KuqMvorWTYYWJySzv_ZgrH3P_w2u3srns_G6EsSOSg1DFg9JvYQvYi88jDOj25Vq1YD--cIE-Fgcfgg5hJj_BFbKDST5QDHIRyFZquN-3unoiBoI30M2pB5mZzoz9nGDay5XmUJWo-iYcpDjUhtv80p-8TXbJ-rFnqUWS-UlLoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30849" target="_blank">📅 15:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30848">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4PQTd6peyOG953AwLECHhCEtVr8r3v1g9DLcIoxuG7WVR6eKnI-GvXLTCmoCuQt3tzR_SrpwmMo6wnVR6l9pDfJRWFBMTK9Hobr3fwNR2W5nckUycF8lXExFBzrC8bjk-5wseqh_9KrVLgozWsbRo898kimLcNPAta67tIv7QNn0XbZWPrlaG5f0W54cXz2GDmxVGgD_7VCBUennMw26wx9DRmrfoR1twVo2Kh5pVv84be4SVh6TZtiZjm-AaBxOkc62pr5ZS3FxYWtTHilH7Rt-fQasQGgVP-wi7pXF3mjPFZRk3tk8j9Od3KqIGOZ0NFXHsxe5SFKB1t05I4YYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇭
روزنامه AS: باشگاه‌رئال‌مادرید گرگور کوبل دروازه‌بان 28 ساله تیم بورسیا دورتموند رو به ژوزه مورینیو برای جانشینی تیبو کورتوا پیشنهاد داده‌اند. درصورتیه ژوزه نظرش مثبت باشد فلورنتینو پرز با دروازه‌بان سوئیسی دورتموند قرارداد امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30848" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30847">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tloNP8aI9b1M1eTiU50Tdsvi43DIOisPJ_V3NlKXDR070NX1sHDlon52EGf34LQxTD-5zVAuk2N5LtLe4vzfmLFnmgw_yzlmv32WG6_VD5QqawajhLnbWLQfuojhdf1Xecox7MCHSCEH7MWAzpV1YVNRgllgT4A2kZwz7-EIObWh2kInrnyNtHUqmIdaGNUhPxWs5FUmNtnpKfbuv5OYSWcmKAdKIe2ka216gAhSdVzrrYDwzkx1PtSwbRj1hhi04xUtv69McySZzWdCyBvyA5cqh-WfUC9UQM7FEuncL_qy3XkfmSvkxYTlr2sf2ymG7a4aJGMbOB53P6duNjapcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دانیال ایری مدافع‌میانی پرسپولیس به دلیل مصدومیت از ناحیه‌کشاله ران در بازی اخیر تیم ملی امید سه هفته دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30847" target="_blank">📅 15:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30846">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE1CY5W_G0eTQkjy3BmpKPyjM1q74if4vUiPIWcr6fNLR22KXCzBTLC3EWGZruVMqupFgLgVLIsOH9yvQaEWWuVePTcB0txeiO5BmIuqYhSnGNGDO--y8IpF_ROYaYEPl2pWBv_aw3hHdIg6jVzvDhPREx4oFD941DuWY99SUd7H055J5i5yC_PSBnKIB1dhYyy0GCv-2iUFG_NX-Usc-gGyGwivT0m0flXbIgr8G6lvvUWLpB0YYeqLNC0M67qsfzu7bpKQl22070JWBsyEeIQu5rb_0IufTB_UTtMyz4YAqmHb_1b33NUComIk2qGWIfTI1pamPa_30Cn1dpJc8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30846" target="_blank">📅 14:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30845">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PP41Jaa1zk_izOdfdAAaGEOIMITP7jjirajETkQbIgKl7MlhVww6gBKDoIeXyAjfxZ0keoYTK2OFaVADAkRlx1i7WvNtR53CNqvKaTILmqM7zPtpFQ-GSEtQeaQ3UypIzoCkwSF9KRrILW0xmof1l9HSDMesdkmE868E3nY3YfzgE8Zq7ceGYy4QjcinycIRTPlONQQHkAdZU2EeuJd66rLpsxCP8G_oy5w7C_fe4GFIaoxhzYwql-WD73STTD9MaSRIxmuhqGmY_ZrdtRiOEGNWO61cI319yrH3iJxsbAeH_C5FdO9oX2OQlmDNikTWmFah4UgR8cU2YMiS9sCjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه پرسپولیس؛ دانیال ایری مدافع جوان سرخ‌ها در اردوی تیم امید دچار مصدومیت از ناحیه کشاله ران شده و چند هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30845" target="_blank">📅 14:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30844">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=l3QzzTbzkQ9MS2X6t6kjdAWuaWUBYcfPSfk1JIULSvxzFNZBfuYKnJXipCHHBOvlFltz8AIkBgDf9PuhOyfpjMRv2CJHis75Rs4bxfepGXANEDYvda8B61SMhUfyZ0YkzbK6UqFFWLPfRAFMTYr4312G0sc-1U4ymQYNr86j_AEXmiEQ49hwaqt08M9aOD6zIHFC1cQ55SlDfoEbvkDYOCyLTtwvf2m_ddmpkdH4_itmcfF4lXaaxPEqgbD-_iXjMcI9FT_p-sCYd59DG4GGZAa-gkHxO905Bwi6CAQeFvxvI6FXhBNQvE2NTxBppaCULG_uoOpH3PhpLnhdrPRu8WUTy42zyjSAv51dyFW-WrZYhchmhOi5xUQ8LUGFyfb2zifuGfyjNjj0g7d1KqyECBT9Pc8edQ526jnQ_alCbx0Qm5sXupEQs5YMf3YJIF5FuP5tCGTXUNhjXQNzIhgfBb00Awo0X4YiqY0HfV1D-ihoCQN-cV3eJW7TIFg7RoemOWem_xLOZ6XF04I3nR_Mg1g_GCMUsvzqrdf864RKDpMF2I0etsJuVe_fk236rdF8Dw_i1_vwT4WFAp7l35cKCGsMWx3wXCjoRARf-XEM3pPaDlaNNTgoi52QTs_uRGh1Lqu24erLhY5aRu4P5SJZFDCKtwCUv5g1fpKLrldc63Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=l3QzzTbzkQ9MS2X6t6kjdAWuaWUBYcfPSfk1JIULSvxzFNZBfuYKnJXipCHHBOvlFltz8AIkBgDf9PuhOyfpjMRv2CJHis75Rs4bxfepGXANEDYvda8B61SMhUfyZ0YkzbK6UqFFWLPfRAFMTYr4312G0sc-1U4ymQYNr86j_AEXmiEQ49hwaqt08M9aOD6zIHFC1cQ55SlDfoEbvkDYOCyLTtwvf2m_ddmpkdH4_itmcfF4lXaaxPEqgbD-_iXjMcI9FT_p-sCYd59DG4GGZAa-gkHxO905Bwi6CAQeFvxvI6FXhBNQvE2NTxBppaCULG_uoOpH3PhpLnhdrPRu8WUTy42zyjSAv51dyFW-WrZYhchmhOi5xUQ8LUGFyfb2zifuGfyjNjj0g7d1KqyECBT9Pc8edQ526jnQ_alCbx0Qm5sXupEQs5YMf3YJIF5FuP5tCGTXUNhjXQNzIhgfBb00Awo0X4YiqY0HfV1D-ihoCQN-cV3eJW7TIFg7RoemOWem_xLOZ6XF04I3nR_Mg1g_GCMUsvzqrdf864RKDpMF2I0etsJuVe_fk236rdF8Dw_i1_vwT4WFAp7l35cKCGsMWx3wXCjoRARf-XEM3pPaDlaNNTgoi52QTs_uRGh1Lqu24erLhY5aRu4P5SJZFDCKtwCUv5g1fpKLrldc63Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30844" target="_blank">📅 14:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30843">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t61BBGKELvmlC_3HrKXGuPbb7RA69zElUaGFtocLjrLpK8a8zyLdGdGA9vWNdKcQntAnq6AsJ83U-LMaiq3kFtvyLrhNRjY_6zSVEuUcVSpRCBtDR1XQUXDh5Ji-495x9CcytAA2H4zDSvV84hwYwUc46Q1g4MOzg4ndXaDXCw2LqJKAqXdb-TsD6U4czHQqZhX5KmT5E8Kbq_9fUnUxwB2Xy87lK5WXXVsENGiiqpZlrqRfcWSce3b2susH43G5T-MBkORE1lnsQsSf6bMuKzrYFK6uMPuUzxsb7v0hbMdOjRqfDBE9m7NCYJyp-ci7gIQI8vKjpp8uEGt1SL4ubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نرخ‌امروزمدل‌های‌مختلف‌ کنسول پلی‌استیشن 5؛ قیمت PS5 Pro درعرض‌تنها کمتر از یک سال از 40 میلیون تومان به 315 میلیون تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30843" target="_blank">📅 13:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30842">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxJNovGMklyjUltYFr-emZtG_bFqGTWHk6THyEwI8wivbiUjhfz7rpauAC5YRK-2IckaFOso7NrmmRLULqv0Lu9-TdqbnyDbDTYJGHNwFk0DrqNj3OIujUz-Y7QBDHoipMspXr9krqnIvTO0cMVATHWZic294RZ1jJZ151QtpWp6XTDrK5i4npyXGwT6mfGtIqVnRRKFhIC-PjGUBkXGREO8dpEqAEDBqo5OXy5pYEUNM77vefsnOjzNK3xpOyIXTN3ZMuzRcSe1fbV5MUnH5M2c1P054kisQ5UYBvwZqQzyoilZmAPeG5l1XYg3VTg20212pdHlRsIO-CDGBtDaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو:
پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم. از این پیروزی خوشحالم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30842" target="_blank">📅 13:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30841">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU6x-lYRiKcR1I3oSVEnJYF3FO2BZULUJKkDDRGfcA2rnZiQ5AZSb4p0iJUxIQlhm_osXnlj-bSi3xyQTyJE6pIr27TjdnYg-RpNFw4_4hCnJx496m5hwAZMP1K9zwLcB1pFUsF83JDgWHKqSpHJZnz4cElq03qr-S-3ynh7mGovsIsPsJuTzbLX25rn9rU0z0zvKYhwbfUUAWIHJm7TDTBiPfipG2ryM6WxeKYRxsTG1fDqNW3GEtuqddsgc8j1206qSHGnGq7ADKm44XhSGxnkfEFG2-sbJZ6W8ai9g2y3I2lBhC6h7xfgV8J_uEZm6q_kum8vAAWsmH7EVBJ16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین‌شماره‌هفت،هشت، نُه و ده تاریخ مستطیل سبز با اختلاف بسیار زیاد این چهار نفر هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30841" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30840">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2o4wLeR2tytuo-h1oSbp00cIT8ARDN1D-9e7pt9N2xIzNQqzh5KBsPdjTrxYuYmU4XGD2IUqB0OI6k_ihLmYu2pj7g0V4vHQBfrLyV66TEcI7M8Nok4TPe39F40ZyQQ3WDFGePp_IVmDTlC9J0R-BHv4l2Yctzg_kZCWCWFZ31kRSatLMzAB2PGDYXj0CVOCPkY30jFmzvEUEjUSIRlGdUIH7H-FSjOHCY1Mo_eCUqzyttjMUDLmagN_nfEr62AUcF6vPkAcBkZ5tABN0QioU1uMXPjCuU1IVgdPumvCNFnW6LeMorHMUHz9RmQEXhtlQjCCa1-XLGZCcif8ZZgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لیونل مسی، کریم بنزما، نیمار جونیور، کیلیان امباپه و وینیسیوس جونیور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30840" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30839">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXQftEmvtICwgLvthlOoVFoON3v7J11CJJlEClKsBX38jccyvUZai6iPc_lK8SFyOAXDJsNCAjZlEvCOrHEKtyga2mme1CSmWDxmb9qXb470rG0TjX1D3K0NTCX6WNQ4LVcq-MLeueeUAq9MrLI5kqk5VYgdEn9FX6U4Qx_Hzhc0R5twtDCUdG5LRy-_Ctr5CBYWj8t7bRJhQSa6qEmlZaUI8hVZTpTAR9SHTkfNEcXa7H9IZti-yv_8TQeO_qOxojr0U_xqqk0uywCS9fUZMaxG9MvpMRsOSjl_F9fV9A69mzBep-MPCbzxwGNSmTqV27XiLpqsl2J6kdYTa9a0PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو ضریب 4.02 دیشب که به راحتی برد شد
✔️
✈️
@best_form</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/30839" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30838">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuVtWkGpSrbGHsYdPZturXZV2ZDRklO2KKVxAqKvP9spDre_qICVZJfRNTD6qMi7BzsVkvme6z2ziDHlV_v8buhgnMugrlFbxeEotRRbK8onfTHSJ9ix2htWirimBrXEFuEHvjprJcP6NpopjyZLgXOL-b330rZnpcwAvXKmk_XQ-CRJwocqcnQZoVvrBRdrcAXpe-icLq2ECaUaIU5CbY56VlF9dyc1EBsRYIH7X2cXuTpnBEwRCt8liyAFwPf0vv_3pxTVZEafoG-KiTGLnFHynsLJOJ-tWqujcHQiVH_zwvbkPLEZV49jrd4PxRQJSAmvd02lXUmlyclAL8vtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه بیلد: سران بایرن مونیخ از موندن مایکل اولیسه دراین تیم مطمئن نیستن به همین خاطر دارن تلاش میکنن که فلورین ویرتز ستاره آلمانی لیورپول رو جذب کنند و جانشین اولیسه در این تیم بکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30838" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30837">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckmbfzKHlumQtRszo_rDzKpDN1bmZxioxTU_OSDo3VA0qN32vUfiYx9FAl26FG2q4PUsrwuCpmJroOdmVFN4QxMnnWt8NwBzBlSCoB7Zakf6bjlLI6prLsJvd6jLWZvXOlMpGyCn699j4A-VRYQAXpodGHFZinG6AUlizp20GmZHfKQJ-JipONDiAssKEjw7e9XB7jrXUDa1KGas2PDbd4JdNfJPWlQihPnUts0kt9hcw7wXBq7xbCKQqqoLSXtfN9Ip9UL2WOUQ6Ucub2T9FOnNFQIcP8ODxmXZ_BFTCeT5jPbI9zCO4sB4HmzI7V3EhLs0ilcsnjtJvEfSvK8l2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30837" target="_blank">📅 12:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30836">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=nzvfH_DOZ_sBexPzac9oxqqqLc55aRfk8mw-0IV8dk_W_WJM98DqfY7ysN-pf9Leb4FBWBf0OUZBJT445xsKXBh-AyrFkhCHSUkJqiFyVNbtP9AHe6T_l_TiIV8eSCxkRxx7w-MeNdTUUpVwzAqGoURJ-_H2l7MHBvdKs0eyyDszWoKsjbHdCkzHXj0vUvC_U0gDRxRbwVecfKoUP0IUYYhSiTtgL5XcXdIRaRlUSgCmqojCjtvENFizxqHqofbP5M9UnrijYv_qQyk_PhJXo3UY9avX8gbEvm9LelfhNbfM-SJLTfmQYqD9u0aUIosS2MfU7V-T-MSXKUwEcvrQDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=nzvfH_DOZ_sBexPzac9oxqqqLc55aRfk8mw-0IV8dk_W_WJM98DqfY7ysN-pf9Leb4FBWBf0OUZBJT445xsKXBh-AyrFkhCHSUkJqiFyVNbtP9AHe6T_l_TiIV8eSCxkRxx7w-MeNdTUUpVwzAqGoURJ-_H2l7MHBvdKs0eyyDszWoKsjbHdCkzHXj0vUvC_U0gDRxRbwVecfKoUP0IUYYhSiTtgL5XcXdIRaRlUSgCmqojCjtvENFizxqHqofbP5M9UnrijYv_qQyk_PhJXo3UY9avX8gbEvm9LelfhNbfM-SJLTfmQYqD9u0aUIosS2MfU7V-T-MSXKUwEcvrQDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طوریکه‌قراره‌علیرضابیرانوند دروازه‌بان ملی پوش تراکتور بعداز اتمام‌معافیت‌اش به خدمت سربازی بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30836" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30835">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30835" target="_blank">📅 11:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30834">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=W4jvTUdpteOQxwwaN9ZO4bXHJNIqtVZpgDiwDqeFv9J_u6qg8bA3FbNUQBOFZZBF1KkU4VtIhjeBZwVrEUcjB5dOEhHte5LRxaMSpUG5RcCbu4fc2iUtNIRhg-0aaBxr1DFwj0hPFVMmEALS731PAkiUSnZjWWR5on0-kDFeDWp7G5Urs7r2RD0D7SNQjNJ5qLLqITtXBi6c9W7AzOSMqZX0JKoDigwht-reZKqIQ036FrngqXoOSjwZcZuH6igjxoMHBaYoYb7yCL9_NAy6C6wiukgzmgbCu8y2Aks-Sa9lC9kNtDI_C6s6o4M4yKLXdVGDXOEQxdptORO8EImGEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=W4jvTUdpteOQxwwaN9ZO4bXHJNIqtVZpgDiwDqeFv9J_u6qg8bA3FbNUQBOFZZBF1KkU4VtIhjeBZwVrEUcjB5dOEhHte5LRxaMSpUG5RcCbu4fc2iUtNIRhg-0aaBxr1DFwj0hPFVMmEALS731PAkiUSnZjWWR5on0-kDFeDWp7G5Urs7r2RD0D7SNQjNJ5qLLqITtXBi6c9W7AzOSMqZX0JKoDigwht-reZKqIQ036FrngqXoOSjwZcZuH6igjxoMHBaYoYb7yCL9_NAy6C6wiukgzmgbCu8y2Aks-Sa9lC9kNtDI_C6s6o4M4yKLXdVGDXOEQxdptORO8EImGEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30834" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30833">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AU34dlGK3kPqZ9JLb32Dpfb5IkKIf6rmea-1s18-E0PqEW3p9uaKbD0RXaqGNqTdwwYocCnRIxkhB9PIfgLI7v6pm47PETLRvi4JvMiDDUMXZlyiC-PxJArd9TnAhWvXY2DbLjI3zEQrqVBQ5DcmsE7u9K6RZprfJIJL13E5pBxlleVg0lPhnVFlUVFoPUk6VowNNW-KxneQjSGCpTtHNlztluMu9NnI5PoJPCRoNruqsKJ1UK1CwJsYSI2giPlUUbtdQIeF9dkH6c6sf7eEs0OTU-TDCXorStYiA7XXs8S9oi6ZvXZRLCfBD8nOsvRm4ytTQgtWWERxknY8AhRHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
👤
#تکمیلی؛ مدیرعامل باشگاه ماخاچ قلعه روسیه رسما مبلغ فروش محمد جواد حسین نژاد در نیم‌فصل رو به رسانه‌ها اعلام کرد: یک میلیون دلار با 15 درصد از انتقال بعدی محمد جواد حسین نژاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30833" target="_blank">📅 09:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30831">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPazwzWQrap48Le1dtPBm_Z53C4r2ocZzLA4IUE0vZdAKkh6IqsmdZQ88HaDEGc-KRx4qoaoZyRtsT_bcOF9gjdmSEBTp1rsbUKyVphiga2r2vLNbE8OAEuCZZZVxtK98nniax6JnWThkJo_nQyTyeNn3bOJKP_d1uUxmzrgKg7VeQGKZPqOY8tEW0jmD8ojZ3XvztmyiukZvs9TOBHybd3uC85ejuM_G5woSPLoM8rOU6eskST1dq0GIdnEauu0be3VShRq8wXw5fJQ-92HQ8iAXyBhp6OlQRr1N44TOCjWKhhB_PT649PRQzPJyhMG8SX5GJrtcuO_pErj2xnT31kU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPazwzWQrap48Le1dtPBm_Z53C4r2ocZzLA4IUE0vZdAKkh6IqsmdZQ88HaDEGc-KRx4qoaoZyRtsT_bcOF9gjdmSEBTp1rsbUKyVphiga2r2vLNbE8OAEuCZZZVxtK98nniax6JnWThkJo_nQyTyeNn3bOJKP_d1uUxmzrgKg7VeQGKZPqOY8tEW0jmD8ojZ3XvztmyiukZvs9TOBHybd3uC85ejuM_G5woSPLoM8rOU6eskST1dq0GIdnEauu0be3VShRq8wXw5fJQ-92HQ8iAXyBhp6OlQRr1N44TOCjWKhhB_PT649PRQzPJyhMG8SX5GJrtcuO_pErj2xnT31kU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30831" target="_blank">📅 09:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30830">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uApgF542Qr65tIvJxGK5sRJB1XklSpyXUMMMO2ORHzlGgnebY5mhK8yLlyf30Tnee8EsVROpVfHDA8bOOxs5nRti17wOD7-FbEs5R_B9VzV4jxzhctCS7pyEZV3qmeO8Vr47KYnyb2U_tmx6S4eviVCeO8XVexaoLyHeGlUpTMOTTxaHuVW1um-Vb7p2ZXzlcvhO4MSe6C1V5wYPp3cKJNPeOK8pUO-UPGIgsi4z0u3PxgNiMfuP0UcV00QOJtY379Hz9ll2eIF-1BwmDSYpGq-OMLp9bG4mBeHUpeVl2ZrXQt5Cij3Eka9Z_EMy4pIA8cEIXBHXqprUCP9UknhCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30830" target="_blank">📅 09:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30829">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrhP1fPrEc9CbcgI-qO6mn02V50_tZuNYWeYlSC1AamGn1NNxnEi0N4-DMmLrz1_ztkEOqGjrplIt9D1CSM5Iz6kx0SAXDc5qs6v2fctng_SW4Vr_8y9L7_VD3sowf5HHXTjiXcS37HJVagRbhSntIYnqgjy3VbvTc9YatpIgj_mFce5dzKkaM0XVvjM5jY9n-jzmKlcXn5F4_IhH3lmdaJapG1iPtf1Ic4JQQyemK1Wlw7XgcBrelh6xsY15Grr-MtNE07lcgCiKUkdKPYLzqCyv1EIZ8GOZDjsEYeFxjV8ZoZu5Vdxf16HWsMQKRxBXtc5_vO-KUYkSTCDLC4jAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/30829" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foX2aK32ubRL0WnSBK719yW6tIA4Tj0-iG7pKq1EBaSBWgCcP_-lEi1x6f6vczfsm3jxPYIab-8UHrG5Fo3JkNybg9ELqyGZUqL7hdzwMTGL7D_HgeQsllEJNpGT394UQDNi_KsIqodhauK_2es5S0QeNk7xn-q7iSAKqHQidGXQKcWzlKsKObhWIUPI-NVnt8BKdnW299OsAfl-z9LDxpQlMD7lPBcWmkGa6WEFSazzyFKTQsfeH9Fo4XPmjHwnaY-AAGGqP88aq9Jdq0DCFLuW-uijjC2ABoYq1OhQA3tvdGCf-qYk0xRqf8z4SAnJZhRtN7QhmEqLNwU0Uxt_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30827" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30826">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnppOFF9zbmzD8GHTlr-pwCD38L3LiiRPK7k_AgEMfE25YAOFwii1yd-jA0LBkL2CxHeKb4ne9vOWFCkRMqqaSIE_oMVyyTCXQOb6swrx91q8ncdC1tzEzvrou7SO16K4M5He5OAOMA6S2KHEDqzEhA5jW-tiUlMlPXbIBDFl5ngnaz3n6zNhxm5X_144_w9DNdcv4cfUUB8ixr6x2lFN1Jywm3uEnzRJJ8GaL7EcizPB97gR4_T4uKaD8dXO0A0WVJlARGAaOFH4KHQtBQvMWvIAaQCGkHWC6zcBg5tQMn0Cawlp0XTksKB1UlvWfgHTMf2fT3skwWix6T3gC-fhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
از اولین طعم برد ژرمن‌ها باکلوپ تا سومین برد پیاپی شاگردان ژرژ ژسوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30826" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30825">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5KAWMs0Jo00CQruDl5vNEWeuhC_wYQlho7xznTXyMyEJdhu7wJsdfT1xfb35gk0eG4IJqD3prw727PJ1snMnY0xsMmOhj8LX8oGbD4h32TIo_c5DZq59t1dIKaBfj--AOnKlIvbhIUiA1j0YSNTtA1wGxnSnRIgZ0O3uyYwNSTV90l1KfqYYhqosPPsqWyJsRPa73_DDNX7b84ukk3_5Psi-auCYx-PD9LIeItBBneZcXB630ZHxIWdNVaI9Ryc5kBZSE6_qpOmMNhLhjM7Dnl3fvFBIJlUIH-UOP5qF5PNCicPtjrjoNQWK5yobmYqoQjXJmsTmzbzOSB6Q5xPfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30825" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30824">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXZGkaQp96N881IlMRRg8Vg1SAeRjgz0NnmVzjG-ItlAHO9FJsDrCgGeRMiwnY6peayUkz2T6WiiWpkV-HTwNwy0k2kxdtAXiDcFAqIWqDN4ZOzsElIR28bKeRx1iFhdUG00SvzaGa3iMjCkTvzk0qMlSi06l9U5UDHto975P-v9xd5qdInJGKhFafSD4rUMqCKSiu8vW_hyxIz-mLpQ8ClPsxdXlFG38nH2aY9rdQvkljhcw0mIvxjW2rOiWPeFDMlPR_QC6iUMpBJUZ___jRwIx2khGNbSl3ViFE8bEOwrquTaI8rbZcxdtVPvAVsNyHrADnKSwGYDogPAceOfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رکورداران بیشترین تعداد گل زده در بازی‌ های ملی؛ کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30824" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30823">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9KLizT38GSomtQ54kr6p0SaHayiNuu8u8-_9EZ8-E2Lsjgkv_QfoK4A4jzJiq7iKtKdhqPT8mAkUWq-zM2V0zqcdROqBugKUXOv1uL-wev12S54Xr_XOcGRrypKxfWoplvuVm_kjzXA9itvtiDFKyAnICecbo4IQA8Ie_qYCnCbTqTL4QImVIVuX19J7d9C2muq6zXmAsdSW2lABa-fqZoy5wNsMP1J62GG6V-9rvE5kQJ6uuEaKyCD5HU-zEECkzjdSEUMYfJMZLUtH2caMNh2ArpSFjMRbSRRKs9GOJ6BJEyCjf62RAPlGz2rqowWLaPdYPg3Px2RRd7okUDhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ابوالفضل رزاق‌پور و یوسف مزرعه دو ستاره 29 و 21 ساله تیم فولاد خوزستان به احتمال قریب به یقین در پنجره نیم‌فصل به ترتیب راهی دو باشگاه پرسپولیس و استقلال خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30823" target="_blank">📅 00:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30822">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhwk8MPfZDkPTqC19Mo5HtNqerD4PaX3eA80k2fCrKp0oRC-VWHqklMXaoTr29s0jepkHGdGphVPr1IuHtg0LCHpnrvcB05-b4R5PDH9X4P_Cr871f7XFnT69h5wxyyW_K0T6QzTE28ezRwmDVnHYk8_8Ku3D4FW7LZEPIESy5-ZkO0-dAg93Urxkm5QIPXXEdKNb0lOnSRD8FletyK61t1PxN5H9_QBweICl_0IiilDBDMtc5lT6EQ8UVXebjDTAkDOb8YXewNj2P0WGjlTiAMrMpk_QBRqOm-Lt_bXJ9ZEtqV2DuXtT-YWqJdhXR3YJLjcYH2GcCQbfaba7LJdJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ برخلاف پیش فصل؛ حمید مطهری موافقتش رابافروش‌ابوالفضل رزاق پور به پرسپولیس در نیم‌فصل بادریافت 150 میلیارد تومان به مدیریت فولاد اعلام کرده. بدین ترتیب با پرداخت این رقم از سوی بانک شهر رزاق پور پرسپولیسی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30822" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30821">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_D6JNXsSYjmJgZcq08rEiPGMfAxg6b56F3hJ1WTmdGvIzoKsLr5wPZLSe87VhEtWYR3XVb2a3PC6UHUaQB269kXNaY6ch5lkVP_vKRXGr-_rv9-5M0CGSokwCoNruQgJ6DkYagvayRhoBzWDAeJ2YSvWEoeAz90VLVoM0Y5s11o_fqVly1xLZJHAxvltBY5oYY01L24HB8LmhRVUFNDaSgbwiqSR0Qd44tgyCqxR-4BE9LKWdX05cM1NOsg24fr3a8I7vXG_5pQEewvRBjGI9L5P4ZqIUH5qIJ7lqtpclNcdfquIQ4CGsScVHhWpuxKJikBBZveYyj5Ak7ZyXahZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30821" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30820">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piW3aH0mncmkU-980DS11oRrZDuUbJqR1eBADvVGSy3Xah6ZilB36FHKU23898V97P2RSLOA1s_MsCZSpt4bxuUFsdiyzLW6i3UkEXA2QuoZ8GY3ZzW9q2YMwdRipuT9LeSexplAQDye_8KgxaK7WL-I3YelWxT-rz--_M-f2qB9SIZ2VlQW_St8RFyh4zODp1a_OEy6KeYFN-Xg2TGr844SDPVTZGlJAiNlunku3Ytus0WHTdKseBM5CPbb1DAzFoOw5OiFbO4keXUD8y9mBXmesq4YEySJEMjtAUPD44u90TLsooLvLwQ2z8VEMp9bmRPJ8bscgMTro0nf1Hmqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛طبق‌اخبار دریافتی پرشیانا؛ باشگاه استاندارد لیژ و دنیس اکرت برای جدایی توافقی در ژانویه به توافق‌رسیده‌اند و این بازیکن درنیم‌فصل به احتمال‌فراوان بعنوان بازیکن آزاد به لیگ برتر خواهد آمد. استقلال مقصد احتمالی این بازیکن خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30820" target="_blank">📅 23:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30819">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-Fz18ZZBjWL_UvO-Qv8S6V77-KEHhF8_FmMm80_MwdeJ8Havg5cg-taCagDsi1ejiQjCppqeGC2sR4qa7glt_eIotMIFgYJc4y_fkB3gkylF2RAJ9Eukgv7IR-8OLURBpoAc1xFJQBfAZ4OhlhUucj1PR5SeRkEqiaLEfCoxiPR0ctDt-9MfAft_gDiTYOD1ZZDGcJiXP5Qn4C3x_nvZ23ZyL63qgWnRnMQc_g6BH2DuuPHaw81AncKXyIb6FN2x6ymXqtk_xeCijoVL61aQ_ggKIfLFYIeCjX_BcuJWuWRALzVGdN6PGTG5ChaokBx-xk70iu5XRwXopsg5ut77Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30819" target="_blank">📅 22:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30818">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEqK2YMDJ_YWXxBpsKGykATsKFN9IK8UHJqh_Fd196sjxZMqsXlK_DQqgLTB5bC1E40xJFmqQ90A3NI7vEKXkG03QixRKXKcym7AIcuLT31Dcde_N5tFtkx2siKowsO4zubxn62np3zV6Ei8sljPUhZ-Kwco2oaW9NrhrGqy1Rh4QTfpEue4sVLWSfu_nGoxrpNTsiU9NYv_At0QdMd0rkTiJKq_6RyO_eXBYPEAHvNyCRbsCUuBzf5O4_vfMcz9j1Ypk-fBxkYmyNUg0xh-RuQLLbFgCyEFsY0VQfWAkC1xFwsgBMBbEug0BPOSbvTxZr5up_jsS0avsDTpyGeZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک 146 گل کریس رونالدو در بازی‌های ملی برای تیم‌ ملی پرتغال به همراه تیم‌های ملی که بیشترین‌تعدادگل‌رو ازCR7دریافت کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30818" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30817">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruGgT2lhmIDBCsSBzOK8MJJ7pXLhh3SI6eP4kc6yeaG9R_sqKSTDfAYsrqPCJS2krth-dDTXsPg1wxdORJ05VyOO69FeW_sJTJfDXOq2d7JeeTMi18DS3pyW_PtNJf7fFR80wUo-Ef3o0NVlpVC4u-5OdK89rGp13J5Nq2nHHGYFoiP6pYY0xrP3d4BL44V7mQNP63tcFFuHIuy0SijkCzFJstcovlkc4nLCyoKas4P1jy3B57l7r_jOe6xZLOkQwHM8Nt0a0j5mBOK14L2yGjPdQKX3yqB4Ot0bhuqD7AzTk03pVEJ6GV5akkKqvyzDeQ4pnNECWPVaE53qe7EcfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30817" target="_blank">📅 22:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30816">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRUYedLhLnuqJUffLHJjLJXeWaRX_YxFqv_KAbZSn0ptrMFkDKFBcbjzr8BJRKQTz2hmPqPlu-4wQ6uLz6-OroVPBWdeTg7TF0_mSuuEiON0s969YXPHVUgFIC8kanm0GVqBjW1BdvY640MaBtJel0XS3N4_Rwz1ZyOym_ISEyis2mUR1FAfHciu4x9qsDje_FEJ6OF9oIs1sEKejEmPezAauePEmdEnfMHUr-wee99nLctd1tyZ57p_1R2tpCtn6pl0c8KSRliJjK5tC08MqjjJLdXPtdagOR_GrJsDgENwpUndpd-PtQKCEDR3hNT8ll7VoaFD0-WM7u5HoilB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30816" target="_blank">📅 21:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30815">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-AgwI6fdkzDzIeoccdvNS10o3-zIyEMFDRafJVg_cwx2tERf0boCrezJlPdaeAsGLiFnhG9B7cG9ko1vpcJl4CHBWBhOpKcbbvoQIDoVxzClZJ508iEHFkqp0gYZZ0NrYb5vM1L8z2y-M8WbCxCrZyW_UNb0EsP1H5WtsiFeX4A3spIpTT8jgBZlrZUS0xAU0eIK5T_NfTILhND7ag0qTR5pko-AKGNxZrqRKl7aMeZtbWo37jvbfGE_tbmuN7DwCsamG9vzjd_t86yXXYS9Q46znWysfnyxS1DIe8wDaaHANUoGmQfTHRXJ13AfPqDES7XZU29QLo_O70Subb7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
در فاصله 48 ساعت بعد از خرید سهام باشگاه آلمریا اسپانیا توسط رونالدو تعداد فالورهای باشگاه رشد چشمگیری داشته و از 500K به 3M رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30815" target="_blank">📅 21:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30814">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luCPk9blON8sgUxd5yl3-6vQQlXC2b3PeuY_IpyjD17tY_9Z82No4gp7catzrVKQeFY3Ga7jwCW0XTDe99HVpNRNbPoiJgfpzgbzyUGuXydi1YvTRAJlM3noL1NdRkPczue10L4XBRKM1ympMiVt3JIHYXJJ60VdFxvZb6s1CD-pa3GplrfgDcSRhaR01ay4ESgVeNlIMXQfCiO8xMRkNbtNpGKZ0VEbskY_u6rm65nUKVTgyLUR6BLsa5DtD2OHhooSjSyVN8DYjPfVJ1KR_tc0wPhWaDcWW3btCkay-INO-BoRcIh5bYl5oOaJpHWeBCj0s2EPs-7nYJSxLtR9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولیویه ژیرو:
روزی‌که من به میلان رسیدم زلاتان اومد پیشم و باهام‌دست و داد انتظار داشتم خوشامد بگه ولی نخستین‌جمله‌‌ای که گفت: خوشحالم اینجایی ولی شهر میلان یه پادشاه داره اونم منم فهمیدی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30814" target="_blank">📅 21:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30813">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93919f9336.mp4?token=e9qIxl8BZxFVp5iZPwc3DlgKUzH3GDlqHdd9rIPnkSk2LDg-TVpHhfGrGmqISsz9RLdxZlFhmoLnjAkgoEBxwswNpweHdLCwAMjeKZTKlrMVINbYS18AW1hs_sOIWyd1duvf7aOYFZEk9bFI78DU92-T0JuE6yH2LzFZosRisu1_ENKHptUUq1oZTMdmaP0CY1EH_NwxOHAZj6RVR3vQr_UHhTCV8lQe2hb1-MtCf_Y9pP-5r9oT7kazznTuLm_vJSjjKsNGWzvxFyVwO7M-_SwQemxt6FbiC2kEAFkrgoka13ybX6KGFfujRV5B1PnuNZZm5O4TthMoBTcsxCH6Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93919f9336.mp4?token=e9qIxl8BZxFVp5iZPwc3DlgKUzH3GDlqHdd9rIPnkSk2LDg-TVpHhfGrGmqISsz9RLdxZlFhmoLnjAkgoEBxwswNpweHdLCwAMjeKZTKlrMVINbYS18AW1hs_sOIWyd1duvf7aOYFZEk9bFI78DU92-T0JuE6yH2LzFZosRisu1_ENKHptUUq1oZTMdmaP0CY1EH_NwxOHAZj6RVR3vQr_UHhTCV8lQe2hb1-MtCf_Y9pP-5r9oT7kazznTuLm_vJSjjKsNGWzvxFyVwO7M-_SwQemxt6FbiC2kEAFkrgoka13ybX6KGFfujRV5B1PnuNZZm5O4TthMoBTcsxCH6Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌پسره‌امیرمحمد‌خواننده سنی نردن گوردوم رو بردن تلویزیون ترکیه تااینجااوکی. بهش میگن بخونه، اینم میخونه. اول همه تشویقش میکنن ولی آخرش بهش میخندن. پسر متوقف شو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30813" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30811">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmKFKAGFqmOYKTSMsrNdUilU47PSQ9aXf7ZYRayIvAI3s1Hfvp93IukI7VThbQLmANiYwdzo90ncK8b3z2ogvC-WHOqSG9x2nC_F3csThQHbP5vJoSAc25Lq0wtakCg14zgEhIMhx8f1nCtIACZnZPHImiclcAi0fcgfwSG5Dh6xZI_1iq-YLqX_Dr5pbaFZQXGiV0xNrDLsTazL_bpvb2TEHQLnv__AZY-9lWVPoQLfY5-gwQwv3tLdYVmb6X-JEkTHqgv1TGt8emLBuh_M2WIGb1P86LdLHHSmlZAOGCCUJJVZj2A4RM67_FQEBNyh8oER63HKQ6iEGv5ZJMB7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rqps8y-I8FRNXNEMCgkKTzc00FniGByL7WqnafU3q2orDzWrfw6jdpcY2VWe1q-WAvWep0yrmdB7JlyphYu6E0vWPkLgrlHAF5W2XUqQ8BMY-P4njj0jigS4jSP7Fypx0Nchhw4wHxFdF-8869Yd-d4yO4zAmkLnsNz_zyoRCpOWnhI6PSEyyAlkZQLZKDyaZU8rOFcW8KjdRXrZAlsJ9zJuCs8n8Runo5RWJaFt5CQRN9QqYXCQWkJ81TrHuJKvQAtTJjopIygwMXh2NOqAm-YRjn5CEPEF6Se-Iy9hnrHjI82qss0-EWl0UqcMFv2vfniCrRJo8rizBL258NUjUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30811" target="_blank">📅 20:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30810">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wk6Pj4Ll5CpjYMSbrBzvoW8OZjZZJnzYz-GjUeTGH1r0eAioyLwEHvmRUiUeG3-OF9e7MlRdQEm7GhgjrOndoYm0k-wjjd0DJ4a2y3nhFwfHi1K0temZAvQwZUxGYECsfKLHd3PwyoUAztQIHUJtMkdajmI9nk2R3TmST3a8v8nw_d_IzqSlwTwTxOjE0T1NXSlKpCjrD1szpobx4bbaVK8sM92d6zSAoi7LY6i_g68UmHzTI0FRdKuqVRsxp0V7_Jy3CHJjfSkTXbn4PlPiuynpHwTLRv3kFl86_yW-rOvJgVHEdApbsI_OmaRvCbp6pr0cj2Js7XvpZpg6RSSyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال ستاره 19 ساله تیم ملی اسپانیا که شب‌گذشته‌نمایش‌درخشانی مقابل انگلیس بعنوان بهترین‌بازیکن‌هفته‌اول لیگ‌ملت‌های‌اروپا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30810" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30809">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRgqfhyH_vRRGNNa52IAJcdHI_lntkqk5FPUPcbyFZDDF9jqSCaIJwqSb8KDpYFLs3VR2YpkadNFhteB63PaIyx_L_AOoF1pyz_7O2GL3bdUDHZj3lk1o6eaI4wL-btFebklNPu2sCNhqmP61aANWP9gpd-VKl9ivDCfE3mNDKd-7DYD--YJeZrrK8XnJI3HujjjfEQOaQzQlhxWuBkKT3On5KqaCdYf3xVIDV0BqZSv-sqeSlk750sZyafjiDeRITH8PxtcD942HJapuTtNedI5Obr4FQ59E22Hm1b82je-ye2NBG9BUnqOQpetDp-PMIRua-XMgMX0oIkilNEJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
نگاهی به‌شماره هفت‌های تیم ملی پرتغال از سال 2002 تاکنون؛ رافائل لیائو وارث جدید شماره CR7.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30809" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30808">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐉 | 𝐅𝐢𝐱𝐞𝐝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Seh5KvrqhrNIyvKVj_JU2lSpJ-zDtvsOM_ivfkJkialQyLN8lyaY4oHpUdRIKDCLvDu3lXs_Egpb_DhsqrX9kmfwx2imJDbCPgw9LQOVck923KN-X2rsn20-02H33KqXgLoPDeq8wHKHC8xnK9nHix2YgkB_wM2Wys_QOHVlNLgENTC9BaTC5jJUjcc52g8OE5fthd-6XYkyoiNQ5wUQ3lgApZAbxRBvjDjdLSv3e4_ijrwmmaQLz_rIzyoh7yb66vuTpTc64c8-lK9RPDZDJ3sxxOmpwledvB8iJn-pq3hhjK86o2uHaXdy5eT6StqvPM9sxImdEohIOFk9YQ1xzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30808" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30807">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3ixvh76gluVUQhpDSbD68S5XipmohCYAq0vYgdffZvlEczvPIPwAKP4MMS0vGvEDO1cwFurftFrVrQbAyAHbSbufMfT6qrl2CR9bzGUrnStE2QOOwuEU6Z3efxWjDFbwia4VABTx6ZD5cYavBZZ2k4jl4V7L7aJuomsgVHTY-ke6PgG--U-emsGs0c1ouaP1Lsn2lbECPne8H95J8jgdp1aJpNpifIfzPTcwxf0JWnQRsTOBYS2yoiYJRPgGbhTRgiy_fjAdkmZEJ0dH4yotYW8M-XnW2pXiinX9ITVr6WsKsLI3_hjqyYo4zJyr7OgSPxGuCQ5Ob1Zev56JiFajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
نقره‌سنگ‌‌نوردی‌ناگویا بر گردن رضا علیپور؛ رضا علیپور در فینال فوق العاده حساس سنگ‌ نوردی بازی‌ های آسیایی ۲۰۲۶ آیچی-ناگویا با ثبت زمان ۵.۳۶ به مدال نقره بازی‌های آسیایی ناگویا دست یافت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30807" target="_blank">📅 19:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30806">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCMp2vzw3NapdWiArhX_IJLiyFRZmJzn1Re7CI5wx4OutNyLgv3NDPgWznvRhGEwfGlIqL-yUVuKmscMgy7i-P-fk8Qg42QKNimeDzIDxbul876cCsMJO1C4J-OfxY2ePrRDCKvSxns6WHUrLjF-DNXQ8qxOQDY_bAXKA1yaQYLwyiPkvxLzca01xXm2FK8uiwQiAeQ2-2iUbxIa0Hcr7h5NmQNLBBVzFwzQlUNQW_mVnkQ_7Ah1klwr4xLlr8S6bSoiN4jyzLWkq0YOBiB84dQH5LiOfGZBQISU3nd10SSWTfFleRbQUuwyLk2Yff_sstQzdbjtiGAAIBMnLHqiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فران‌‌تورس‌‌ستاره26سالهPSG
: باخدافظی مسی و رونالدو خیلی ناراحت شدم، ولی طرفدارای فوتبال باید با خداحافظی بزرگان فوتبال کنار بیان چون یه روزی هم قراره من از دنیای فوتبال خدافظی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30806" target="_blank">📅 19:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30805">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdm4lUwrsHkx3Q3B2nMrXvi9NP1xNBG0ANkxSIg3lOyfWb-G9AN-fYKvd-8RLhGjD0N1g_4GSRQYb-givv6R0NyaLb2LF1y6sGgtdfYWPChNx9opVTsEkeBYYyev-i37CxShxcZUqq9IrwlQJrT_woIXeB4R2VQPTbMnn_RgdfaLfdmm9R09EAtZNZGlB3gO7lnrEGWpr7wE515QWUoJivFwhyLDA3ZT4AAodmA2zIESBRdJYywCrgjsc7Rs0-1_6-7o6AVCv4B2hkINT-O1Q9_qS93HZERWmZFgyNiafhLJ8jL2cQBZXxRR3BMdk3yDjYCaJjGNYvGymK-eluOQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30805" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30804">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr-d4kiNq0aYcqIfe6w68UbDdd5blcCYlA_x4rRrHCV3_bzuIKsDHfxCqw-apJecjzXL_l39BVNFfMAOhX1tKt75na989qhskDQ5wHz935fHOCvnWIF2Nz-79m5p2V8YmNThdOomg5TUQCC_E7NDfS7-FRnR3vrJJqbTsjuT8MBkVoQZ6DC2qMt0dHgKm0RICAkSbA0BE8YKwKSGeoKM8lGoPuX6pmGETisI6g1ryKE2T1loTEf4kyh9oUhC0Dgh5XFs8BdjoSdsDfyohOSKmWqcXK8CL_QLWq6Y3jmTLBQSlVPUtuBPKPPfnOEJkWAgPeHsaGfPx3RGYbSlofs7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30804" target="_blank">📅 18:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30803">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuSVY5e03Yp7rw8qbCWh6zuMVR_LiTruguOPf-lnjOcQNHAboptQOcfZ8rkhARkMoKnnDoB7BbNco7z-i6negIFhTjUaEHennjoYLImqkaS50c1BGcpodR3x8KFc3yskJgJwdPF_1PV7gQ7wXtrIH0JH5-lKkvaPkuiplumpYhyKZRxXyAGCqrBhWNThRzXjeKrvRqAPgSX_5BZQ0ZHShKMG-yqTzMXIEnIQml4pqw2MySCAk5Pp07_ZXkzTEaCPiDbQCf_5kGqnS9ZOnGkHDwA0uuZSkHsc1L6omWPoeFmc3MSlOyPOSOXIBXNyJdfBJQtHcrKrRtDfENMGEeo0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30803" target="_blank">📅 17:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30802">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dekds7U0UT9yqbICrWg6V2V9QWfAhmMXOWtxwAshkOT_zidSTjnOkcwqmXRe6kYg1F10Uo45D6Y2v0OuNuXCpdrffYtubr0U5MmLkysfi3168O48WVXEaNOeQ8tocit8pRtamVp1ajkumrMsy5lfDzYEeLbW7zPUOGIp5BTnMUo1C7oNVjGepuvLhYXs03Z1MvqBHxwsq-Na2LqsGRL4DuEKyxB-0YfX-SXT7OFymAGvlkQZE1fVVF5L9o3V_loX6RDf3bEs1J7iDjA56OcuDtpfqZN3_2wuyIGAbtnBxPGGU4CHgw1rsJSXSvkWlD-GCOSoFtvTY0ytSvgW3iUo1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30802" target="_blank">📅 17:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30801">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇵🇹
🇵🇹
نایب رئیس فدراسیون پرتغال اعلام کرد که کریس رونالدو دیگر به تیم ملی باز نخواهد گشت‌. رونالدو بعد از جام جهانی میخواست از دنیای بازی‌های ملی خدافظی کنه اما فدراسیون بخاطر قرارداد تپل‌های اسپانسرها از او خواست که تا رقابت‌های یورو 2028 در تیم ملی بمونه.…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30801" target="_blank">📅 17:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30800">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNC9_rKaKYm6S41Q_nPV6FptdcP0GnsFxcgWb_qENhe0LFF5JsjC5AABYq5tVLZqMNxSrO2IkkIiazdX-EHaC0Lxbo40fihsoOchZnHPE_Pezuhh4JuLPH0pBYKU9yqrknuXcPrpE4EfxNHG7S-CIhHT1m7AjUirCGJQrLBusGm07IoBIwB2xBcSxNIQ6ypVq5cihJa0xeaL0DiDKvrFcvkqwHyz_0eDjLJ64TGjFJEOMS_8R3KCJB_fWUCKze17b2LXiY6Kn5nYJz5HMYWak9x9eaALMT0c7b5zchPPjJ46FIw6Xt-rHuelKUYigjL5rQMFYOnIzoHVSA8yjAkZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی بعد از آهنگ خوندن برای کودکان میناب و مصاحبه‌زنش‌بامجید واشقانی رسما به ایران برگشت. جالبه چندروزپیش که خبرش رو کار کردیم تکذیب کرد گفت برنامه‌ای برای بازگشت ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30800" target="_blank">📅 17:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30799">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDFqFMfW7n0Blha-ZsEDirhrNr5HvsC2Lqwp6o7pLtQcXszq8jfZMMGmS1DXVIFW9ETpEP8hBeISOdHJajPZ4INaADjBF5fTfxNsvi9jNOMgPgQ68VuMQVFAnZAQ7zdlMgpZC1OT1XuYY_oy8SsslqxnfjbZl76RDgz9Gd2g4EyQXPFDRnRN3uz1cQqcX9H4eBcIpW8wqBS3d5BiSdBJvzoOy4Iu2mQrQTdiB9EyTSlra0PPR12lDYtpipU4ki66zTHp-SVTG1d9g7arxua2Euejssk7cMDscUC8XiVhcN-87RxTJJjlihtLpvwNDi_7RFOfOVFIMaiA1umRC8WB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30799" target="_blank">📅 17:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30797">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djXiNH2UGn8poe4Xm3LahzMtEUUMBTJJz0EjR1kwSF5PbN8jMX55MNZb3iW8TYNCdRwP4LypBGGnWuO0i2EDx3l15nznyGEHrPRkrnEUpcsUlUWKTTUeVtMb4jm777GnLZQdpxFdGkY3jR2ozcJHPwj74DqeJNpUBJA-PC-g51FI8_tkgWJm-qQfBTdbKa1R-owq8m26ha2kFdwQtoUbMA3dkMi8nMb1TXl6PFcpeitSGyhnXTVn4ZqhAU8MjRP03UvRnYh5mpRdStwOJe56HKn_JK_Gdcm2gYbjz5vavkjipvbMtqCL-pOrOiUL4HFCOoHzgZMzlMByuQBM-_Zi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=XOaX5ySHaBy_z1lsPA9A8Bh9sQG0gwtq73cyeflBK-GwpajrSn4_aBwg4tmp8eBBwyYI-rzZnRHtXRFp-6temQEYWwO9SPUilReIc5tGxt7hzeyzxExr0naBHfbh2EljF5Bj32RGoa_r3-aq21m03Cv2N9O1FpNr7TeYmsJDzm_q1dWQcR6MdNR7yQaKaFHqFKT0mCQ7OgmZR7C64Vns49eXCQ1UnSzIGojfqSpZT2B3oF_iclr-VO83yFtKFWfBzAN1M1U0GxANYthZiyenKk4kqLKfXs6NRnNtIWRdruI_DxdkuV0gPCvL-JWXcl_5-ZP4BsfBTAXVmKh0uESHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=XOaX5ySHaBy_z1lsPA9A8Bh9sQG0gwtq73cyeflBK-GwpajrSn4_aBwg4tmp8eBBwyYI-rzZnRHtXRFp-6temQEYWwO9SPUilReIc5tGxt7hzeyzxExr0naBHfbh2EljF5Bj32RGoa_r3-aq21m03Cv2N9O1FpNr7TeYmsJDzm_q1dWQcR6MdNR7yQaKaFHqFKT0mCQ7OgmZR7C64Vns49eXCQ1UnSzIGojfqSpZT2B3oF_iclr-VO83yFtKFWfBzAN1M1U0GxANYthZiyenKk4kqLKfXs6NRnNtIWRdruI_DxdkuV0gPCvL-JWXcl_5-ZP4BsfBTAXVmKh0uESHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30797" target="_blank">📅 16:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30796">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5gpmeKVRcjS-fnE1QS4yQ2ejgCZ5q749jV8t5PngZb6FRVHAjjQx1cR7j9LK49XB9mSYOA1dVGZKdfb78_A4JCJnmWtqwC-R1mwYN5zk1BmljNcez8-GNIqnyxp2GwHS_GLvyplmNTI28pXwdADb_vzw0-E1lj_vKylozGlVSai6UD4BRD-4VffIc6qqwC0cdzeZ2hJGeGADYZ-fXxLqXC29xeb4yDefLVmp9NNaX_YZnBIOHrGU_tFVlcvZuBhJatHt9zGKmGehyd72KLosLAiB8fpbFQbDng9ohp9dCh54wWG4aQVnSpwNDPGiEQTZWabnoKtJocRDNuhlXeYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30796" target="_blank">📅 15:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30795">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6MTCfgjlFawudw_6xTGabdFx9uEHtqMAMW_w7NaXYQv1fye89PD_9sQpEZCj36kmnMWrfq_p8QLnV8-AgTxcgMcYxgsAbSJewUg7ghmQi_Z7oDoAQ5RueUAEyPl8Tkw69WMDzBFPFNUqK7qK_bV2VdQKjGD8fkpJozERyY4X_hkwvsuCyObY8AWzbW0M18QxbPOMgaBrACj7cwSCEDN25InalM4Qo-kk3f0LJUC3_K0kJ3ndCuYHSbvGi1frWrG7F7mnLetNMp4r3A8KktK4Jb-ol8e0XCmGKr4DuxfBpq2R-MVGS6HdBq6rLyGKCBxfbR4AZQGBFNxL6QOE0vmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30795" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30794">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLH2GVCSmMZpGzHbHF-XKgb5uS8dIJMjdA1Iq8Sh36PufmGEaklIqAqp5pyG_DxS1e99R7SAqCyjePCv7n2tzjart2hkWZ2ZprJ4b61UAUYL9Y2Q8-OwIR947x9f8bWz8GMz5EH1Qi6XKoOx05FRWiEfRB8pB8PW84txydv709YnV7AaP5frjpTWb_KXRV36yULDQwaWuXsso7OD_QUs-1RQieHT_D_NVbdETmYT-BIx4nFLtEfVL7ls4c9wM_bPGMWVixnMv2nAskha1irr_iNcRgSwUVf6pKP7ZFzntgRvXcwRtbzsXJelrXvMEPKuASmftuCFwQzTrelb3Z0znQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال‌پرتغال؛ بعد از 20 سال که شماره هفت این تیم برتن کریس رونالدو اسطوره تاریخ‌فوتبال‌بود به رافائل لیائو وینگر این تیم رسید. خیلی خیلی بی معرفتی شد در حق کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30794" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30793">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=qHqTwNpKZTpa18uySLHGhKATrs2vYKJZ40FLcEB2oGpmfTNimQA4n7D0KgBFfpvES6Bj4hBOypXNf05Q_mMPnDz-uDLOAVx3sxlQMALpFRgaOVrTFAUij-GIhaFQdSi_9Ah-xDCzFboA416Mm80wPJgOWJ2mMtcqh89ZSJ_Z5muYRZHEHw64znBFrspfIqJg8xCu7GBYAm4adpz5yS9JkyjtXNQidIEW8jkHnxeMwOzWAOJWHg35SR2X0dM5W9Z503mpmbJ4KjYn6wSdajVW27iaDdl0EiypwzD3veP1BO129dZApRlyug8-qUnOC9SWceoyh-z4dBA6jZ1-Jsr3woAEmuuEP_JfTwQL2kIetg9gMlg0ih0Cj-_ExZCKX2qWL1D0C6iYDLRiymcpJB2Y5zk53qOc7NCAM9cAp_7mIsY3am5HJ0oSSHabWheN3eF7f_NRGZk1VM6JA6_v1MigcqT5q6qKksRrg91WIyBHu801X9WMShAisD2uZ6Zc8pxGACXv4O4zVU_aBPfrElYZOZVqFtpfTPMPGv8I-6PNNq39ItfWYpWR-ciimNSJPZlJVAq4XhG7SLS8OE8i1DLz4HI24S-JItsijvx0TkIIA2OcEapc3KIlRFwI8NS_WtTn4BJ800gOwd7lwKW8j53llbmTNj1kW8vdlg_lYwQx55E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=qHqTwNpKZTpa18uySLHGhKATrs2vYKJZ40FLcEB2oGpmfTNimQA4n7D0KgBFfpvES6Bj4hBOypXNf05Q_mMPnDz-uDLOAVx3sxlQMALpFRgaOVrTFAUij-GIhaFQdSi_9Ah-xDCzFboA416Mm80wPJgOWJ2mMtcqh89ZSJ_Z5muYRZHEHw64znBFrspfIqJg8xCu7GBYAm4adpz5yS9JkyjtXNQidIEW8jkHnxeMwOzWAOJWHg35SR2X0dM5W9Z503mpmbJ4KjYn6wSdajVW27iaDdl0EiypwzD3veP1BO129dZApRlyug8-qUnOC9SWceoyh-z4dBA6jZ1-Jsr3woAEmuuEP_JfTwQL2kIetg9gMlg0ih0Cj-_ExZCKX2qWL1D0C6iYDLRiymcpJB2Y5zk53qOc7NCAM9cAp_7mIsY3am5HJ0oSSHabWheN3eF7f_NRGZk1VM6JA6_v1MigcqT5q6qKksRrg91WIyBHu801X9WMShAisD2uZ6Zc8pxGACXv4O4zVU_aBPfrElYZOZVqFtpfTPMPGv8I-6PNNq39ItfWYpWR-ciimNSJPZlJVAq4XhG7SLS8OE8i1DLz4HI24S-JItsijvx0TkIIA2OcEapc3KIlRFwI8NS_WtTn4BJ800gOwd7lwKW8j53llbmTNj1kW8vdlg_lYwQx55E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری معنادار رضا علیپور اسطوره سنگ نوردی ایران: باخودم بستم که. گفتم رضا: ساطور میکشم اون شکمت رو که اگه بخواد کباب مالیدن بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30793" target="_blank">📅 15:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30792">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP1XGRhYyAcbHE2OrqKDipS47r-2GbF6XffOdWiA074Us6T48nkzgzvlorYokn4jDwSETvcAYmxNWn01xtU4nMtWqM8M2uzclthO_n6qgR6Gn8GptVUrN4ZTdtZ47hwaQ0jle2W1PsHZXDPa5fL0kP2kX6GX4Pjt8DA_gmR11qKz5TFcnjiYTLv8apFJzBvloPgsVZhxMSHVE0HO17UI0P6EbY9Psp_AQiOxF2ZhAixsfDZQb2bbGLPI2HXxtkP4uwr-mZIBGNDXD2DG6PZ5UYyFfe5I6LC3OiZu0kGDZcFZNFIsJcTDXVnESf9_ozSXoWSppoSXjwgfL1yDc_F-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
با خدافظی غریبانه و تلخ کریس رونالدو از تیم ملی پرتغال؛ بلافاصله کادر فنی این تیم شماره 7 پرتغالی هارو به رافائل لیائو ستاره گالاتاسرای دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30792" target="_blank">📅 14:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30791">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4ZaiVRVLyPYocVFfEjrNEbItYZUMSfJ0enQRtnTE7BMidpwuqfF4gBE-55ruYroAV7qPr0v2uVGUs4MstAutMYqbQj2pcZxibZ1f4OlujOGJHZAi_Ovr1vfOWhzBV2CMCeAgr1vPZwwTrvZv4LPn4BpT3x0OY7eAWlVTquBjtvu-R0c70RaVVt6VEbKiBS7gY0jK7LqqmLLwGpEjhbrkShJwd450B9KEbVWj2f_4nWVpYsLq3L6KWBAN4bnKEKhKF81gofCP6B2bVIue_7hKlWY4nq6mGRmyPYgqvQsFDH3-lfoZEyMoCGso1WbMQQEvPwMZ8ZLI1yV0OFXzwkh4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام باشگاه رئال مادرید؛ امباپه تنها دو هفته دور از میادین خواهدبود و بااتمام فیفادی به تمرینات شاگردان مورینیو اضافه خواهد شد. بدین ترتیب این فوق ستاره فرانسوی مشکلی برای دیدار حساس روز سوم آبان با بارسلونا در الکلاسیکو نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30791" target="_blank">📅 14:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30790">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRrUhgKRtqZ7r8E5Rf1BuhbENbwDkNLVoOAB5ifoYHgQNz9Di-s3aq94QUhgBXNxkYl9eaGhrQ-FalCSCNojPMt_FqVoQe6Ky8oCjS_cGGgTWSUxacTkZwvJAgrKmOv_MhHvzIkrHjFweqhcieetzs2eUjaJPibFVMCNKgRjQu_4ubFRBIPyK8eVUXXRoW_6XPn3LCvvJol1y4ehNapYG3_65LDVvRqUXoootk4vbZZrMR0JdXLF1OlqzbFtBUrZAPcM_Y7cSX4l3DaA1xbjVlQEIgd2ciGM35F7AqEHkhQ-GC8qc3KmnUKQZv6OlMzVsRRFVzi3EfhdQ0ISaW-Gqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30790" target="_blank">📅 13:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30789">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE2GjLI4UdrDX0EX_8T3BBxmVMWMAHtJhrM6A-HUCGHbzGvBDxHOI1u1CY9FgkMm85ZxOTi1GUHoS1xvf-I9D0lpzVM912Ik7DRkcOg4W3k3JGea0f_5Xv5KSfn16JhQaYzzpREQu7X3KK-7bsXJ-9-KuKyBL3xq6LXnceYWZGi2fbSsTcxTVvxnST8LpJzATr3J5hyRzy3QEaFa0BZknHQ3rfn05pGY9cVYbHDv935jI7Lf-yyJokUXdj1zWoWsOAYYKCUuFd7hvrv6spqRG1nbzBsU4sdEbK0AuNqQfwzt8xDG4OiGGG1Hp1gnSIF1VQ07IBBC9eLhdEIfJ-LTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایرانِ امیر قلعه نویی
🆚
ایران کارلوس کی‌روش در تقابل های خود با تیم ملی ازبکستان رو ببیینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30789" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30788">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDd2hvQefCmIG6n4GlOTqoenegVjR_sy7PlSxIdbj4n50XZUaP7OnIzPmDKNn33ZyKWtIv8KYnlG1gZW6Oji8ob9xcRgqQFNevZfTvYXi-c3TO33PuZYUBny4iHATj7vFO4-2_UIMafTk3FBJd1lGErAN5_jn3O6R1gs1FvAg7vu6nJ2i7Y8Ohy6xNvw_ehqfeJN3btzgMpul4Y78lBPyTlgMtyBoTHreb29cLQibG7OIy0wlraaysIFCJoZO4d1d2VGdQ_c0e75vnkFy6rgiLJxwmpqM1CV3eVBKZb5DGqhWpsIynbRHnQ8aW4j3mKMzDSG02_6HiR8mKJq2OTy3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30788" target="_blank">📅 13:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30787">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK1g6tP3KQgVnDpZxIION6ngUTZFrnWwrDy1-0agdb1nkftIfbArVqG8fEsECcf_FRApFE5Q_0ZsHG1DTOTN0qFne3dtnKncU8mDHedrUMamipiANdSKWFf3rX8G3J_WpJ63rtQ0CHri_VAElI58hFrtEfzUq44gp9alJYPS9NwYmk6wL_rTlgOYGYrY3C-O1idNmzNwQmcNqf8ZNhkNHetrr-wRqduVoJGfYFFEPiBeQsOB_BP6RAtSyqKhrniDf-KuZx4g_Ezjxz9zntxyAzvYnpOUP-hLAcYxJvmZQvc5sXhUMbICn5t5hqr4xmUmnUiQ-bBophoG4T9hpS5JJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30787" target="_blank">📅 13:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30786">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAromJQneE2Tu7Euamc8yatwOIOmvilHfOL6QRs3kpsg8beiStxwawNb76jyyW5Rou3Ms7QKDJ280ZR0j3lfVUf8mzBozj9vWDAWxAonsdQBw7BcH93RJRti8zG0x7F_ZjIo7HqbYqA52rcISFZ8-4-UKIclmJ4HNt04KRYe8sLpzUvOy12Zn8sOZfxizumGUMGBaSbqEDhAWhhE0393K6b54CoSeeKnb3BdY1423ZfvOYs0-DpLKmBiyLxmxRtE7o35IcDwn0bgrVe8-qKahKHKLn6BJ0p6rsI3sXgGxgV1JfD1vWJFbvHTo2GyRup3yykynflcrpdPs_0_XfJRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30786" target="_blank">📅 12:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30785">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyJstjSqoRONR9hgbyc9sgUBMRbw47lu6RstXW5dwO1PcCa8tx-F0qr4Zwvlx2wajr2NcB_O5aIM6fKbln051ol-2gqPDq1i4XHYRDsamyfTFGPUMerr8iOQ1FQW6b6iHFLDBoQ7EltZJtSJzQa2Q3AbP33-jAo9BKI4TtVA8o7KfdueecrDJpCikhfd-05PgrS3qc_UACvaLfupWwFaeDu9uQ-yXXhz7hFQwjw3n_u01qyqghHjkrNGurfyAd4wuzOb5knYLhV9k_w8nAhl3lxKpRus9VdZnFz5KrAHq-i-EGRaA8StlbPaYgKlj_9La3Ah3CZG2il0_hQapL_FXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛ طبق پیگیری‌ های پرشیانا؛ مهاجم‌جوانی که مدنظر کادرفنی باشگاه پرسپولیس قرارگرفته رضا غندی‌پور مهاجم 20 ساله شباب الاهلی است. تارتار قصد داره که در نیم فصل غندی پور را جایگزین ایگور سرگیف 33 ساله کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30785" target="_blank">📅 12:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30784">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=O91QVTA3iZ8-4FJh9I_R1h13YkHO7RPLLl5ST9Yy5QfRHkOzL3N5j0xcg_37ryuXX-K1ix4-nltp-Gvo01g7bEJoyuvJS3x1xyL0xhY6BqPADXkfrJaoTOQJva-H2_kr5vgjv9POpyg8dIl7CwymtRwvE5a1FY27bK53kfqwGJFZY1rbZbDfoCY7b3b-KFjn2C8CcfwEDdCnnrMHaWwnWyJScJchP99trqKZA8YUMgDUuMYWL_UKge4hgmJsurELm1CijrVFnIi9WQriy1frSaD8ScU_6YWm_1sJSQWDkHtThIZevtKUwVDhbcpOYT4XvUupCt1SZof4220f0aVFQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=O91QVTA3iZ8-4FJh9I_R1h13YkHO7RPLLl5ST9Yy5QfRHkOzL3N5j0xcg_37ryuXX-K1ix4-nltp-Gvo01g7bEJoyuvJS3x1xyL0xhY6BqPADXkfrJaoTOQJva-H2_kr5vgjv9POpyg8dIl7CwymtRwvE5a1FY27bK53kfqwGJFZY1rbZbDfoCY7b3b-KFjn2C8CcfwEDdCnnrMHaWwnWyJScJchP99trqKZA8YUMgDUuMYWL_UKge4hgmJsurELm1CijrVFnIi9WQriy1frSaD8ScU_6YWm_1sJSQWDkHtThIZevtKUwVDhbcpOYT4XvUupCt1SZof4220f0aVFQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهره‌کسی‌که تو شش‌ماه‌اخیر فقط گامبیا رو برده که باچهارده‌بازیکن رفته‌بودن با ایران دیداری دوستانه داشته باشن و الان میگه بهم فرصت بدین بهترین تیم رو راهی جام ملت‌های آسیا 2027 خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30784" target="_blank">📅 12:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30783">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=V6CGf_U-8pQ6b3IEbIsgPTCYBwgxgL28i99VMSD9VEvGWvWeyNOBbBdUoFfw1pt9RkWpuwVn80hSITsHK_nUbK1oZzWHUWnegXFh96uXWzKDzTqw6Wfg11jbchgTI_5VT2KPpv7hoPcWb3FaqR8U0rTbV15oWse7bE1pEojgephONVMHKgQlVY6k_HDDQ0ARB37yv-qpDMzmCHURXEXXIVxRoClfqLIZ-JFHSMc8ZKGc-Li5IboFQ67N1QIuQXp1Tm81ZoEVyfAU55WHMY1BLwcXaiVS5yu0Yi8dry8hdoaLVE2-SmU1gXdlVeS-2jF9BoUlPZOIUvi78aDLlG7IzoFnzBeZWhx7EgatYjopeVL8BI-Hhla2Gxl7TzIVdiCpYWZdSm4jLvs9ZdGjx5uR9Jw0k112vQDfcvZc-LK2dtnqeEEkCFwYDSDs5-aXDxzxlnXgnI_y6XmpLX0RYCdp6Y_rCU5hx4TESaKr-wlyTFy0CJ6_OKl2-TrRrOewgLIiyAvDhi2ZRaKtJbEiWdoBojnGzbVz60mhin0-VO9UGObPhE__dEToQSQQOU_EID-LyeaJxe_EEpLbgFiUldDTCCa6UVKwb7gRTmHNM8F6Yf34JZEUOgcM5ojeI7SbV7Lu9O7Au5vvOdf2oH_SQo-44KgKH2OdB0fZEGo90TeA8dY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=V6CGf_U-8pQ6b3IEbIsgPTCYBwgxgL28i99VMSD9VEvGWvWeyNOBbBdUoFfw1pt9RkWpuwVn80hSITsHK_nUbK1oZzWHUWnegXFh96uXWzKDzTqw6Wfg11jbchgTI_5VT2KPpv7hoPcWb3FaqR8U0rTbV15oWse7bE1pEojgephONVMHKgQlVY6k_HDDQ0ARB37yv-qpDMzmCHURXEXXIVxRoClfqLIZ-JFHSMc8ZKGc-Li5IboFQ67N1QIuQXp1Tm81ZoEVyfAU55WHMY1BLwcXaiVS5yu0Yi8dry8hdoaLVE2-SmU1gXdlVeS-2jF9BoUlPZOIUvi78aDLlG7IzoFnzBeZWhx7EgatYjopeVL8BI-Hhla2Gxl7TzIVdiCpYWZdSm4jLvs9ZdGjx5uR9Jw0k112vQDfcvZc-LK2dtnqeEEkCFwYDSDs5-aXDxzxlnXgnI_y6XmpLX0RYCdp6Y_rCU5hx4TESaKr-wlyTFy0CJ6_OKl2-TrRrOewgLIiyAvDhi2ZRaKtJbEiWdoBojnGzbVz60mhin0-VO9UGObPhE__dEToQSQQOU_EID-LyeaJxe_EEpLbgFiUldDTCCa6UVKwb7gRTmHNM8F6Yf34JZEUOgcM5ojeI7SbV7Lu9O7Au5vvOdf2oH_SQo-44KgKH2OdB0fZEGo90TeA8dY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی‌ازسوپرگل‌های قیچی‌برگردون فوق ستاره های فوتبال در مستطیل سبز؛ کدومش خفن تر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30783" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30782">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏅
ویدیو باشگاه پرسپولیس برای یازدهمین سالگرد درگذشت زنده‌یاد هادی‌نوروزی اسطوره سرخپوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30782" target="_blank">📅 11:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30781">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB-Z8iIys2Ib9bXZjkvXBtrURj4sMg510sv8kL0mGCiqWgsp_MSelcTEz6LKuVW4daJAvit_JZLEJGiFR7B6Tmt8Old6xb7AtGPd6SJapazyh9tz3F1ebeUoJaJxTip4OPVeL2ugmZPpsvC7_SbDA4TtCuEaEaOHEtlNtJInT7I5Zvioch7kV5JByefvoa39aF4Zfes-6hmSqAbjxMyKtbJvqVQHT8jyOrJ9vZR2zq2QQLKD-5XL9VOwNIXEplchvhnaismX4aVCQGyaXQErnkmykak6elWkOha7pOuW0M-ByX8TuabAs3-6NsdKjARAdcjF7T_BYWjRWDa9h5SPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30781" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30780">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=rA96B9Pd2-sDB_Ezz6IWfX41I6FZab-c8DMSyhUSh4KtKcNqhPijGibx6m81mVyRbhLKgntGNROdQr9aTwB5sQetRIzmZYWwBjv4XI-SfKaMmBSe61hTOy7tLoRjtsZJ3w55ZM7vpO8ErNnyXInhknONnnu7DAo6a0EXiiMvTx34MuvYKXLAhQfShKq_Zit1E6KSrSU5LllxoNK1ykazzkE0DJr3Wrd-SD8ZE77ITS4t-1bi_XAogvLCpcBtyc1GNbQbKIuSqtfM0iOjf0W0kpUZmdLcFS1t25H8qHr7eOWAFjBKoaRvPdyO4CrsM0-PRTTcYCU0-GMMcK6m60feQ38mP25oG5E0fcqV2hzAKJOSByypbqMwdAjYP8XMui7ZlIXgTfZ3kT072u4KKfisGZ6tiINgk4rXkEmyoZNteKlYT0yb6bB6bCbc2BldZrZi2oiSZjdum7V74cK4HCVe30oPDvO7rAHE6hUEux5G13wR8aWvRVCHy0wYO_6QAZlzghUhcD9O1nuKP7Hh8Yy5O6DSMqsgJVl1JYvm4r1rU1k7nnyc3HN21ggmW0Xuyq4kpiU5He5T7oPNg4zQWqXIp_zZa7SqnmMf4E5gGtKWHR9vR87trOgnTTvNrIzyrGREmKrV96aoNcv-g5x4a2YbHm1DpTesgytniCG1l8oW-gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=rA96B9Pd2-sDB_Ezz6IWfX41I6FZab-c8DMSyhUSh4KtKcNqhPijGibx6m81mVyRbhLKgntGNROdQr9aTwB5sQetRIzmZYWwBjv4XI-SfKaMmBSe61hTOy7tLoRjtsZJ3w55ZM7vpO8ErNnyXInhknONnnu7DAo6a0EXiiMvTx34MuvYKXLAhQfShKq_Zit1E6KSrSU5LllxoNK1ykazzkE0DJr3Wrd-SD8ZE77ITS4t-1bi_XAogvLCpcBtyc1GNbQbKIuSqtfM0iOjf0W0kpUZmdLcFS1t25H8qHr7eOWAFjBKoaRvPdyO4CrsM0-PRTTcYCU0-GMMcK6m60feQ38mP25oG5E0fcqV2hzAKJOSByypbqMwdAjYP8XMui7ZlIXgTfZ3kT072u4KKfisGZ6tiINgk4rXkEmyoZNteKlYT0yb6bB6bCbc2BldZrZi2oiSZjdum7V74cK4HCVe30oPDvO7rAHE6hUEux5G13wR8aWvRVCHy0wYO_6QAZlzghUhcD9O1nuKP7Hh8Yy5O6DSMqsgJVl1JYvm4r1rU1k7nnyc3HN21ggmW0Xuyq4kpiU5He5T7oPNg4zQWqXIp_zZa7SqnmMf4E5gGtKWHR9vR87trOgnTTvNrIzyrGREmKrV96aoNcv-g5x4a2YbHm1DpTesgytniCG1l8oW-gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی تیم ملی پرتغال: در تیم ملی اونیکه حرف آخر رو میزنه و رئیسه من هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30780" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30778">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8hMxNS-PEvGrl3WqHYXQAAlR3aka-iRI2PNmbJd3au_gK2I-ppI3b5mTLWsF9Im83-_RpuHGOWTdUGEtDrMdwF7U0jCqmz-Ewf2CgbNGvaWDVckk3QYGf_oNpfzpRzG3MnJ4uhTu8N0g6uZn1qg9OiYYMFUyqP-PYAQ-Ibvhh5eppt9GxedxklsQwztPTWhx5_FOw4Xlfz9VI0Y_KHHwDaF19J-yTHA28KUPD73MUzU3Nfb-T-qPNoQnU_T37REW_vdK8hQY0z8eH5VvmaFiVncxTWaypfjm5ZEIY8Z3PxZx_kVjnFxT94i-Q65GCaIvzg8qgNT1kVwt40MPURkNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تکمیلی؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ دو باشگاه الوحده امارات و پرسپولیس در آستانه توافق برسر رقم رضایت نامه مبین دهقان قرار گرفته اند و احتمال دارد بزودی رضایت نامه دهقات با پرداخت 500 هزار دلار از سوی اماراتی‌ها صادر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30778" target="_blank">📅 09:46 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
