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
<img src="https://cdn4.telesco.pe/file/HmsxHDhPuocH5cLFOPCvFIc55pEw_CRRkdzsNxfnSnEqjy7OpHOSuwlEsUBkh67PqGqU5hDTkl4rB5Q9vxXvKMKLv6LqdcxscMulP84h2KNLgXkBhII4fIHBEoz1bHjLxN3jKjFok8KYAgJ6DswJpwAQGuE3X456q8qNPTr0fEp0qPuZfRDvp5K1fvhL7yCj8ht_EGzmLjZWHAXstADl1wzS8KH97mDIk2QsXWZsT0CW8vECZLYrFntijYp8NVViu7BZlklop2DsL_fMfifldgiuXCH8VacErZ9jHEUREpL9LIwK6Ynzkau5UXtsHtGw8p86lEidJ4WEpuw6G_WKZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.6M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 15:23:01</div>
<hr>

<div class="tg-post" id="msg-658437">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
یک منبع نزدیک به تیم مذاکره‌کننده، ادعای سی‌ان‌ان درباره مذاکرات جدید ایران و آمریکا را تکذیب کرد
🔹
این منبع آگاه تأکید کرد که جمهوری اسلامی ایران در روند مذاکرات بر مواضع و خطوط قرمز اعلام‌ شده خود ایستادگی کرده و از مطالبات اصلی خود عقب‌نشینی نکرده است.
🔹
متنی که پیش‌تر از سوی طرف ایرانی مورد تأکید قرار گرفته، همچنان مبنای مواضع تهران است و پیش‌بینی تیم مذاکره‌کننده این است که در نهایت طرف آمریکایی ناچار به پذیرش چارچوب‌های اصلی همان متن شود.
🔹
علت اصلی افزایش فشارها، ایستادگی ایران بر مواضع خود در مذاکرات است
🔹
متن مورد نظر ایران، به دلیل تأمین منافع و مطالبات تهران، تاکنون با موافقت کامل طرف آمریکایی مواجه نشده و همین مسئله یکی از مهم‌ترین موانع دستیابی به تفاهم نهایی به شمار می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/658437" target="_blank">📅 15:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658436">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
سخنگوی وزارت دفاع: ایران در برابر هیچ فشاری عقب‌نشینی نمی‌کند و در صورت عبور دشمن از خطوط قرمز، پاسخ قاطع خواهد داد. او تأکید کرد ایران آغازگر جنگ نیست اما در دفاع از امنیت و تمامیت ارضی خود با قدرت عمل می‌کند و نیروهای مسلح در بالاترین سطح آمادگی قرار دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/658436" target="_blank">📅 15:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658435">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeEwExjRk1aznLvG0Eek_jhvcjKLe8RrZsyFS22pHCgkC-7aPS9xEUDOIFnZVWo017FLztlGw5eZuDrFhdVGXX5r-dmSsBDT2jAXhm0_AGfX67MIIInMXPg6fuwW1d2Hqfj8bN_Fx3wdMGS-4C_i9qlS4L7yMMUmTGBumJossv3hCkOQ8IIxM_OTwWPbRn0DY6rjYRglJQGn1QkVUwXHMjhyN9ixXbGJBobbhQT-ayasqzI7kE2foXTppvh1NBCctPH5ibqeMKWGGEQ9yIuR7aEoJIR_eMWd0zkID2a4r0LknvMNoDEqcp8w-XGG-gdUj3EcEK_wwj8OkorLmsWGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه مسابقات امروز جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/658435" target="_blank">📅 15:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658432">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RcvAkQRHDIPVWyfvPh9uEwCgKVqH3mLK739tb4TrSOQW8kpWY2nD-4g5WmjcWHQKjfU1dnYlNflRMrigpnDSCWEqeSLy4JIHMJu8BYPW_ISrg6b02KO4Bxhw64QX2e99vRDwgnz0PDS1uQhVqfUq-mzbpopiIfSUUaCesNnHZ967ooI2TllyqxqwYBZb4fIjA1EqoAxJ32MEkrgORyu3bzmTk1RtRuaIFv1_robhaEVBf6JwRbMbohIehc3T631CRD55vFQEcbor_uVKKwzhYCXUBFLiuTnAlTiHy7MO-wW41TkA5dEPFDW9vEfgoENlqOwQ6ITTJMYjWfzX0ytAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKog0doRnwU7jTlY3OMLqiBHhMyS7TYQNqX9OSSVrYdg_F6xWCe2g3CeNVnRXAqgkPuOeloqvb-KfaAiPQWtt7LXqzT9eD4cX4f1djfEgZlYzhIt2FE1ZB1kg10pc80WfKjZK9yWuSOyLQb_42-bJpAT31C6YHr4lwE6oSHv8PhIptjqciyMpTLVE6ju8wYbMhZBXhxl2y9NS9wVQRNkAbQ0hN3UP8BicwAHK8ct-Q6M23fJvw2QAtLoyxEkqQNJqiabxTZxf1LmZWQMJo9CUSh3KUni719lI3ftIdmkd-DEC7DqdztwpoBs1FdJdzcsMTITLuzZf7L_txtvP3HLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fo5-6axboqeX372OJ9Ux_yJ8wwcKcwef8TMNeGTRh6oHbqiBpCkkWF_lz0GsCR1UjMQM-Q3yOrjqJrWvxRJ7K67Caf0J3cFNT55GZ9l4RB7ibAZWKxzSnypgTVe0us-l_ziVr2JgxjJHLH-cJMvVPDOMfwiE1UaFtqUscq5MQ9h-269B0zZKFGz3iHjh1w4FBuu8rMH51s6Ab4B7_Eormw6aAP6thPAsgzw7G5zCyxa8AE7uMtz6d_piZXUzwkYpHUoA_taQnK9lASyYvbPQASDWfGSBch9FM5gQ5j6d_TNwCCAH8r4X-B3xGUVf5kkafBzd4FtdX9s0FylDs6TP3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از دانشمند ایرانی که توسط عوامل موساد به شهادت رسید
🔹
دانشمند متعهد و نخبه، شهید دکتر علی احسانیان که در تاریخ ۸ فروردین ماه در میانه جنگ تحمیلی سوم در شهر نیس فرانسه در حالی که مشغول تحقیقات در حوزه هوش مصنوعی بود، توسط عوامل موساد هدف حمله ترور قرار گرفت و به شهادت رسید./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/akhbarefori/658432" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658431">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حمله سنتکام به یک نفتکش با پرچم گینه بیسائو در دریای عمان
🔹
ستاد فرماندهی تروریستی مرکزی ایالات متحده (سنتکام) اعلام کرد نفت‌کشی که با پرچم گینه بیسائو در در دریای عمان در حال حرکت بود، توسط یکی از جنگنده‌های آمریکایی هدف دو فروند موشک هلفایر قرار گرفت.…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/658431" target="_blank">📅 15:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622f83f9b0.mp4?token=otU5IZWbFpKSd0X1ZfISKSlTlHbbJC1ENIDjKRj2JfL2Uia6yZsaxLG42LolGGl-psu9zUEFsn4FHg1B8eF6l_nR_518eDZmwmepM_jUuiC_zIgzs5epwJ0aQ3f26VrlTh6Qf_u19ItgH2p4WqXxV9-aESRm--dDkjKnSnfObxfvGa4VIV1qumkPUsfRsVxizKGGWN8cPMjR28mrR3wzmoyLH4E4dmWZU3nRTrQoUo7MuBADwDiTrLxl7-CWNVjq3aJQuG8vgVyjhaYdBBOUxBVl9_O4S-5DFWnFVpNi3kkOkJoJSFXoWhNRCTc7hOubWaWX2yd5HdV-6JuC711ZEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622f83f9b0.mp4?token=otU5IZWbFpKSd0X1ZfISKSlTlHbbJC1ENIDjKRj2JfL2Uia6yZsaxLG42LolGGl-psu9zUEFsn4FHg1B8eF6l_nR_518eDZmwmepM_jUuiC_zIgzs5epwJ0aQ3f26VrlTh6Qf_u19ItgH2p4WqXxV9-aESRm--dDkjKnSnfObxfvGa4VIV1qumkPUsfRsVxizKGGWN8cPMjR28mrR3wzmoyLH4E4dmWZU3nRTrQoUo7MuBADwDiTrLxl7-CWNVjq3aJQuG8vgVyjhaYdBBOUxBVl9_O4S-5DFWnFVpNi3kkOkJoJSFXoWhNRCTc7hOubWaWX2yd5HdV-6JuC711ZEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا همه با پرویز دهداری دشمن شدند؟ | من در خواب نامه استعفا را در هواپیما امضا کردم
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/658430" target="_blank">📅 15:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
حمله سنتکام به یک نفتکش با پرچم گینه بیسائو در دریای عمان
🔹
ستاد فرماندهی تروریستی مرکزی ایالات متحده (سنتکام) اعلام کرد نفت‌کشی که با پرچم گینه بیسائو در در دریای عمان در حال حرکت بود، توسط یکی از جنگنده‌های آمریکایی هدف دو فروند موشک هلفایر قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/658429" target="_blank">📅 15:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658428">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUWF4hJU1WwdS6diyjtP4wOkly-I8zBk6FhrXpxmWhSpnLLNBlK-3qJK0xDWavc-jH3HTM4TbZVyZl9pDH0lpk7pt2iPdQqUoAj1xBbMT8AdaE8Juzk-C7jS2aQD2VfXUvr7aBmc7g4BNGgLBN9Z_B3yKg9TW51m_YntQE7cH0ZR2YRseN9-LDr5WFHW3so2Bq5pGOm9EOtkep2pezYgsEBXpv0-ykCfvKOqM5u9veZ7fWxHQhcsDVKKyo_rFaNgeiw6QOEr0gDZB6hixt2YK0yS1TsXe4FTdwCiYlm5qzaeHWNObXtB8g7igYUZAoHfL_lCqE13Tf8nWV2pg0lmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسدود شدن دوباره تنگه هرمز چه بلایی سر جهان می آورد؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/658428" target="_blank">📅 15:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658427">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsdLHnrlCk31aG0z-3BOiAJWrV76sZKzUlmvvlTO_QEIVl314yjW4mDOgdgWTyJyo-OimDwWuapMVEzFNvg5OkvxFtt7CrqFvxwSS2BwAQhCIdaa1xAxe5vSxkRV9WzIrjm-01ocv3qp8INRhzJZ112TPJ5qGpCzjwCPo5oEdI_93ChP_-iXQrY36Sim8huWBn7rrge1re8cF7CcYgyC5hnlvyxp5f0aOvUPB--_S9XL7Jb3HIkG7EITnOdDW18wWIJkq508mK6yru3yVvRukSJ5_4-O2W6HsX7tuYOyWU7SKFA5GYW95PbKwhXY9atw3rmxcuBeBwb2lpqQ4rdIeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آینده از آن کسانی است که در «نقطه تصمیم» درست می‌اندیشند؛ جایی که یک انتخاب می‌تواند سازمان را تغییر دهد.
در رویداد تخصصی «نقطه تصمیم» جمعی از مدیران و کارآفرینان برجسته حوزه فناوری و اقتصاد دیجیتال، از تجربه‌های واقعی خود در مواجهه با بحران‌ها، تصمیم‌های دشوار و فرصت‌های پنهان بازار سخن خواهند گفت.
اگر به دنبال شنیدن تجربه مدیرانی هستید که در خط مقدم تصمیم‌گیری قرار داشته‌اند، این رویداد را از دست ندهید.
یکشنبه ۲۴ خردادماه ۱۴۰۵- ساعت ۱۶ – مشهد، هتل نوین پلاس
https://evand.com/events/نقطه-تصمیم-015774</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/658427" target="_blank">📅 15:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658425">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPOt5BI1He2RJYpHJ0rDXwauxoW3HpoQpOwrGiz2WGt2_tI-wU6kQ_HCFrNizw-4WfMnXpPGFgp8IJOhFQYiLTm-DEBRckVOd2RNtw5xRpjXMmUbCXRMsSd7Ginq5GjHfXGk4WaArLTy5L2JzRKI_AVRPAaU13tmwMCLdXu7CfsXINFOHOsaydYK1cTIsnNzcrIEYPuA6xHCyq0HWPoVBBHyD7n7RtfH0p9kbyWXJ3O0tHmbv6ME58618VVbny51LpTK5AanlBJwvteCBHZPZxsjT9krN3d0Rrqv9-Dm_LcszRnUnQuL5xGFc0pkq9mPnS_yeEu14PCcJNESBksa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmEF5DHf4KAY2ed_52mcDLdwknCt1Y0QFV8PsdRL1Or19WUnb-Usc5heLiguS_q5-QxjuhJMnaS0fFTFA0Liyx_DerORJT6gTQsHmzlgILPrpHl5mcsZsLmNlje234aKJsHnkWbeoQRy5BcP6ZpLie9eJ6hL-B207FKhdR2K-2xvx1WaR5U72aQKV_wHEKqIQtf817g8oRNOUNwgItqxuR789-bEZJ3yNN3nn4u3iFtaWFMR_dysUc5bC_XinLeSW9XAseE3we9FpWTs56qjswHDQvuxtvtE1-pyOOKv3CV_AhNyhhcfLHowl0exL3L9-CSDu9HFrIk5XMvpWTGbww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تداوم نقض آتش‌بس حمله رژیم صهیونیستی به صور در لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/akhbarefori/658425" target="_blank">📅 14:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658424">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ2f0T4Ixg1tEDOiK7zGawIfGcE5xb290udeK8tZPOb3C5GNVNQLF8SBO8G_RzZJDH1H0NKqRJ8HM3La1c3aTJSIwCqLN7LbnBtZMnwXVywAN8v5-4nj8lazE-nQMdlng5C95X4YpKbPDHa1hfBs4T8OcaW1D3_JuXPiPsP5a90TEHUjNj6MJfQNpUszcYYETtG8-kN9sDB85EHBmZSxLtBoZn0SNy4Flw_vQ8ebJ1jS_ep3NrERc6NZLgrG4qYnhMuXaGVlYeMjmk3SzPVD6hwB68TlKzIbidvXZ-RAIodkDWx0XKIFv1vFbOM3jbhSS1-LWqmTRjo8WwH1HjzVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین قیمت نفت ۹۲.۰۳ دلار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/658424" target="_blank">📅 14:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658423">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
وزیر دفاع انگلیس استعفا کرد
🔹
به گزارش بی‌بی‌سی، جان هیلی در نامه‌ استعفا، خطاب به نخست‌وزیر بریتانیا کر استارمر نوشت «برنامه سرمایه‌گذاری دفاعی بسیار کمتر از آن چیزی است که در این مقطع خطرناک برای دفاع و کشور مورد نیاز است».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/658423" target="_blank">📅 14:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658421">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8e9317bd.mp4?token=V_G1GmJrcGGBQf1FFYlvzA-FDDFLsNveF4798qzL9qYUrJRK7IBOn0ydIJCKGyU8xcb1PnAF4HfCxhw5AOoQk6hxBuvOkBCsIQObr5_pBbBh-DKzZ5milTVrjYCOpgM3hc1ubPLHI8yDo49JoNrzmBW7lMMeNCj29eUzfyHfec5Xv4ljffkNFR4PtdC2QKGaSmIMz6PxyrS3-zKkeQ7rhu6OHjTkqa1-89fint3cMoLmif3f_6KQWtSr2p10Hk_4wqE3Qs4OJAq0zkXU7K5WxGYA4rd7IyqLn4SrhpmnbL24V3KdPpJJ2Fjvw_e55Ufxn4i0rjte7dWMIIA24ZIITA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8e9317bd.mp4?token=V_G1GmJrcGGBQf1FFYlvzA-FDDFLsNveF4798qzL9qYUrJRK7IBOn0ydIJCKGyU8xcb1PnAF4HfCxhw5AOoQk6hxBuvOkBCsIQObr5_pBbBh-DKzZ5milTVrjYCOpgM3hc1ubPLHI8yDo49JoNrzmBW7lMMeNCj29eUzfyHfec5Xv4ljffkNFR4PtdC2QKGaSmIMz6PxyrS3-zKkeQ7rhu6OHjTkqa1-89fint3cMoLmif3f_6KQWtSr2p10Hk_4wqE3Qs4OJAq0zkXU7K5WxGYA4rd7IyqLn4SrhpmnbL24V3KdPpJJ2Fjvw_e55Ufxn4i0rjte7dWMIIA24ZIITA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی وایرال از لحظه عبور جنگنده و واکنش عجیب فیلمبردار در همان لحظه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/658421" target="_blank">📅 14:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658420">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7K-2l7iDHEcPsCmfgn-jaCvsKouzJ1iJ_jjcVo6Ytn7JYaRcWmDwp_No4mPsQ5l2mkFkNd6NG7EWq6dr4IpaYFliNYi2HDxGNAWN0eAI5ArStwMVGCzQADOf1IkiXWu4KSJGzdNg9BldUMY07uDKo61ByhBd7aVdynjV798qxdN8HPn1JaZC1fMXJe0NBcy4HNKQYkb_EqHK0FuebZIe-tbgW34IKk_PmCd8kONmkrSgRYjBb4UfVY4r1_Od2RUwOm81rOfDsDLnEMfVALLhT_ZksAqdXTdpiJaXHC9cyFKDOlSMasMW1pqZxUciYlrk0b3r2hXLEEQZ0iB1hat1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: آمریکا باید بین پذیرش شروط ایران و تتمه حیثیتش یکی را انتخاب کند
فرمانده کل سپاه در دوران دفاع مقدس هشت ساله:
🔹
رئیس‌جمهور نامتعادل آمریکا خیال می‌کند با بمب می‌تواند از باتلاق و بن‌بست خودساخته خارج شود. اما با موشک‌های ایرانی، بیشتر در منجلاب فرو خواهد رفت.
🔹
واشنگتن باید بین پذیرش شروط ایران و از دادن تتمه حیثیتش در جهان، یکی را انتخاب کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/658420" target="_blank">📅 14:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658419">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723170ae96.mp4?token=X8VrSw_cp3uuMnKRpzLM5SA5BcA4ZeqNR3zXkfuxSUGNBYO-zKL0NWUluIgVjP_eJOoFSVu4UqaduwrkeFVBC7IHzo68Civ0F7lH1yMl6MAsetx9r9yAFuwujlKcFjlgU7ygBuSHIcwxoTgFtWY_xVQHuPGqPx_2Cq1fNs1yfFYPC0IdTDKYZsy7LBvLv-snboaP3-2NnZzKONckh2J_yLm9LhFUWd1PWmDLf638zp5XCM4VTt2YZVfTon6_WsFXOw51NZOdw9H6PnLh6YrwK0PwuCDEae9mYbMx-nVIDCGO4jkuCGAIUaeReQKwUWuyUum0WD0MPpqAOQ1NAgKzxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723170ae96.mp4?token=X8VrSw_cp3uuMnKRpzLM5SA5BcA4ZeqNR3zXkfuxSUGNBYO-zKL0NWUluIgVjP_eJOoFSVu4UqaduwrkeFVBC7IHzo68Civ0F7lH1yMl6MAsetx9r9yAFuwujlKcFjlgU7ygBuSHIcwxoTgFtWY_xVQHuPGqPx_2Cq1fNs1yfFYPC0IdTDKYZsy7LBvLv-snboaP3-2NnZzKONckh2J_yLm9LhFUWd1PWmDLf638zp5XCM4VTt2YZVfTon6_WsFXOw51NZOdw9H6PnLh6YrwK0PwuCDEae9mYbMx-nVIDCGO4jkuCGAIUaeReQKwUWuyUum0WD0MPpqAOQ1NAgKzxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حملات موشکی بامدادی هوافضای سپاه به پایگاه های آمریکا در منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/658419" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658418">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: لحظاتی پیش صدای انفجار در محدوده سیریک و از سمت دریا شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/658418" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658417">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
پیام تسلیت رهبر انقلاب اسلامی در پی ارتحال مرجع عالی‌قدر، آیت‌الله حاج شیخ اسحاق فیاض (طاب ثراه)
متن پیام رهبر انقلاب اسلامی به شرح زیر است:
🔹
خبر ارتحال مرجع عالی‌قدر، آیت‌الله حاج شیخ اسحاق فیاض (طاب ثراه)، موجب تأثر و اندوه فراوان گردید و حوزه‌های علمیه بویژه حوزه مقدسه نجف اشرف را در سوگ نشاند.
🔹
سال‌ها حضور در حوزه مقدسه نجف اشرف و کسب فیض از محضر بزرگان آن، ‌چون مرحوم آیت‌الله سیدابوالقاسم خویی (ره) و تربیت شاگردان و تألیف کتب و اشراف بر جریان علمی آن حوزه و ارشاد مؤمنین و مقلدان، تنها بخشی از خدمات وجود این فقیه بود که فراموش نخواهد شد و آثار صالحه آن باقی خواهدماند ان‌شاءالله.
🔹
اینجانب این ضایعه مؤلمه را به حوزه نجف اشرف و عموم مقلدان و ارادتمندان آن مرجع فقید بویژه به ملت مقاوم و نستوه افغانستان و خاندان معزز ایشان، تسلیت عرض نموده و از درگاه خداوند متعال برای آن فقید سعید، علو درجات و حشر با اولیای الهی، و برای بازماندگان صبر جمیل و اجر جزیل مسئلت می‌نمایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/658417" target="_blank">📅 14:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658416">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52003f3ccf.mp4?token=nIkMPqrBUqVpQm_0FH-_E4Kj9chwVrXO1LS5qU72Hsl4gjqAJvBOozxfrCgaFfMS-g_FSXMlqaZrA8T_KPHYdDUzXnjKrfStkgl6IwS_iWWj0UrbZi3Z9t2wvJ4R69nFFJooW6H9_CGfqnigeQb_0Avq_cRowLlWQqWdW_2eybnaMtGTCzojLwQlsfvdMhN_crj8whnzCGmfHwxIk9fvIfqHXFUjG-Irzmk0MSLPeYvRQm5C2BiOq9M4Ymotzk9kPCOtqcd2eLIEgVXQjtB4Ka5bNp7cMcn1d4509IGWe3Uln2nsFdOLF_B1vNuVr3FPr0Pt5bVJULf6TbM_lFlCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52003f3ccf.mp4?token=nIkMPqrBUqVpQm_0FH-_E4Kj9chwVrXO1LS5qU72Hsl4gjqAJvBOozxfrCgaFfMS-g_FSXMlqaZrA8T_KPHYdDUzXnjKrfStkgl6IwS_iWWj0UrbZi3Z9t2wvJ4R69nFFJooW6H9_CGfqnigeQb_0Avq_cRowLlWQqWdW_2eybnaMtGTCzojLwQlsfvdMhN_crj8whnzCGmfHwxIk9fvIfqHXFUjG-Irzmk0MSLPeYvRQm5C2BiOq9M4Ymotzk9kPCOtqcd2eLIEgVXQjtB4Ka5bNp7cMcn1d4509IGWe3Uln2nsFdOLF_B1vNuVr3FPr0Pt5bVJULf6TbM_lFlCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای فداکاری عجیب ناصر محمدخانی | وقتی ناصر محمدخانی قید بازی در بوندس‌لیگا را بخاطر رفاقت زد
مشروح گفتگوی خبرفوری با مرتضی فنونی‌زاده را اینجا بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3222112</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/658416" target="_blank">📅 14:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658415">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhiX0nBZdjyvXHFEe5PELOqZGhuc2REFAXkAqh36kVsQz2i__FyYYc1squT-BW7KrIK4gC270K_AkSfjAxGwwzRyi7eH7fW0e_h6UtzXqI4MjxX-4767YO_BI-EA6UGx17Tya4krRvY_BRzW3-EQBvM3XIpf0TwwEm_cGIc8TFs5pX-EbUN0LlfTMcXbsuMPfLi_RVLyWE5rdNM4e2uTGRAmMXwj_oI6RzNAAhI_IBqtg4qi-mIfCbDExmQRc2uzwxtoGcHjiQB0eJpJuzOqK0MJ23S1Wub0JiusDQTq9i0DDUKjJTVgfHYd1sisJqQnhMVhBFHem9V2s4SuKz6S0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای جهانی در کف قیمت ۶ ماهه ترمز زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/658415" target="_blank">📅 14:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiqpJdm9AOibJFuVJEETBt1aRGWCVjBhgxSywLkzPi741oQs26jRtLXzQPiodBw8o3ruQRsEityg5nyfuSMHArmJzZnON5wt69z37VsTP_yNl5JylVMFGlZBlyZDOjKEdhY2dgmosPkWsypVe7t3KqfrdB8MO2e-Qch2CZoFjBcxQ7IYg4q_I1mYNTnK1jS98oH8WSbovZxGy87O13jGaEJoUEtDU8RKMk06DTUtO02tzDVR1OkFu_Fz3vePFZuf1jnBwC7zotzAZuXvLehZrowBRKrUhKkjHIhReLbVVqyJHFYXG4M8BKZA5lEAlAvxy2L1ct2dmK-8ZviwizjYKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب آبادی: در حقوق بین‌الملل تجاوز نظامی با واژه‌سازی مشروع نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/658414" target="_blank">📅 14:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658413">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
تیزر قسمت دوازدهم از فصل چهارم
🔹
در این قسمت ادامه روایت از تجربه‌ نزدیک به مرگ آقای مسعود نبی چنانی که به دلیل بیماری کرونا به کما می رود و با جدا شدن روح از جسم در عالم برزخ مواردی از جمله مرگ ۵ نفر از اطرافیان را درک می‌کند و بعد از بیرون آمدن از کما، به ترتیب مرگ آن نفرات که یکی از آنها همسر ایشان هستند را می‌بیند
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: مسعود نبی چنانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/658413" target="_blank">📅 14:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5531db40f5.mp4?token=BPk6OzM0IF-yAPL0Gv0e79t0uny-6s9Gkz2mxqxM35zOkNwP-g7pnml_gP8_E1v24teY8Y7xts42e--pGLOxXEaBS5KPKMl9KPntbpuSFElkpUBoKVu5R6pglQ4VWUa7_BMaDUxlb_xnMKvfViUYRWaPGOvMe23YMBb3WLKZo3KXKdBCATrW9ms5LIAc-t8Hr36YsyUhEQjf997tEC8JnX6mywQzTNJe5ZCyhSarBdysJfz4SF95GhH5M_8oDHU5tThNxI3PoGNw6ghsZAtGKkH1hQ0BcGC89iRCsfS_jrNf6CmiRzDwpddwQEKEvS5kzWudJGdJlwGgzdPtRRSbHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5531db40f5.mp4?token=BPk6OzM0IF-yAPL0Gv0e79t0uny-6s9Gkz2mxqxM35zOkNwP-g7pnml_gP8_E1v24teY8Y7xts42e--pGLOxXEaBS5KPKMl9KPntbpuSFElkpUBoKVu5R6pglQ4VWUa7_BMaDUxlb_xnMKvfViUYRWaPGOvMe23YMBb3WLKZo3KXKdBCATrW9ms5LIAc-t8Hr36YsyUhEQjf997tEC8JnX6mywQzTNJe5ZCyhSarBdysJfz4SF95GhH5M_8oDHU5tThNxI3PoGNw6ghsZAtGKkH1hQ0BcGC89iRCsfS_jrNf6CmiRzDwpddwQEKEvS5kzWudJGdJlwGgzdPtRRSbHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ایران گورستان تمام آرزوهایم شود، باز قلبم را در خاکِ پاکِ این وطن، دفن خواهم کرد
❤️‍🩹
#ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/658412" target="_blank">📅 14:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پیش‌نویس توافق نهایی تهیه شده است  ادعای رسانه بریتانیایی امواج به نقل از یک منبع با اشاره به سفر قطری ها به تهران:
🔹
متن آماده است. دیشب نهایی شد؛ اگر تا امروز به صورت نهایی تایید شود، به صورت رسمی اعلام می شود./ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/658411" target="_blank">📅 13:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2qvgB2z027nBV79lh63S-5bWhCbDzj7mZSZu0v64rJ4SEVTPly-ISdSmgpvi4xowN5Qs_rD3XkeEESybaYtd2LHoUe2pJtaMCFtUg4soLoCpFRaeojy18OOUtEW6PFq-17Tq_3bRI6mdtodV8vvIe18kACVzAIaaUp5VwysxYyxOem5tbxtMqFW3mmyXi0NlkC_k6mWV7mxoxlEfkUMQsfVorEOnQdcLkxPzv7rEsNRT7y-0wpOXikybgJoRTXshONwwyFrVYwbLe_zlPucdMacUxhDA4t_zS-BdPIibogg1t_PPDgM3BHtnFIxCJt63Xi3R61UoxXfHg6IX9TW4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از درخواست فیفا؛ تغییر لباس هائیتی یک روز مانده به آغاز
جام جهانی۲۰۲۶
🔹
فیفا خواستار حذف تصویر نبرد "ورتیرس" روی لباس هائیتی شده بود، چون این امر سیاسی تلقی میشد.
🔹
این تصویر مربوط به سال ۱۸۰۲ است که ناپلئون سربازان لهستانی را برای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه استقلال این کشور جنگیدند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/658410" target="_blank">📅 13:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
هند: ۳ کشتی مرتبط با ما هدف حمله نیروی دریایی آمریکا قرار گرفتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/658409" target="_blank">📅 13:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658407">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIDPedyYMBRho8o202C5xKaBxGKz-u098yD8abUlmq2e934OS-7A7ITboBcpeScGFNkQxjRkeJEAcvKGlCngs_W-5NipKYn-DGMbRgmeq8Q6K2qlI3inT6Q116jpKNw9nYpr3a36_rCPDYn0e2908V3YqQoOJ0WwtxF0aA5lrwwKJMhtWuXwfNbjoDI4ixez1r4rNzPIdVaBqcEkBCqRXHryagZ3n4pEkSkrAyjQb8hdqYwdmskKgG_5yswQtZYfralM0My863qxEDFwDYqZbaG6FkSRfY6tS_Vka7AHzlEsH1qD8NWAUVdHDEcXMgT1BV_Halsx60EguqeDWyKojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1v2aHZm-v4YS32OhtqTwMdCzXjpOA546NfTazqqE9vcZMRl9diTDlmWIXEII-gV41yia4eMoznR5gV1gZ_hAF7_LHyZOxPkHt4dXGHmCVA7RF7Y5M7wL87r9TChL6oC3r6Bo8n52YQs5PEaOiwPSiAY5iSg8qB2S4QzDfGffwMq1_kumsTAX4n-X2eMtfd5myJi-biQx7ZJXAiTRoPMyPnBae_caX4cBxYLmRsLo194vSBbsVHhzdhHmGlMLlikzPq-1wWy5WsV59Q-lScn_nSwOzk9TU2jVUWtHYceR9cRpBnPoIgmhZIFfBEd7YvnuR1-hcNKEVrILc2qlW2ZEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بقائی: تخریب مخازن آب آشامیدنی در سیریک، اوج زوال اخلاقی در سامانۀ حکمرانی آمریکاست
🔹
سخنگوی وزارت خارجه با انتقاد از حمله آمریکا به مخازن آب آشامیدنی سیریک، آن را اقدامی عامدانه و «جنایت جنگی» توصیف کرد و آن را نشانه‌ای از زوال اخلاقی در نظام حکمرانی آمریکا دانست.
🔹
او با استناد به نقل‌قولی از سیمون وی، این حمله را افشاگر ماهیت واقعی قدرت آمریکا و مغایر با ادعاهای حقوق بشری آن معرفی کرد و نتیجه گرفت که بی‌اعتباری اخلاقی، نشانه افول قدرت‌هاست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/658407" target="_blank">📅 13:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سازمان بسیج: نیروهای مسلح نقض آتش‌بس را بی‌پاسخ نخواهد گذاشت
بیانیۀ سازمان بسیج مستضعفین :
🔹
نیروهای مسلح ایران هرگونه نقض آتش‌بس یا تعرض به کشور را بی‌پاسخ نخواهد گذاشت و با قدرت پاسخ خواهد داد. همچنین تأکید کرده بسیجیان و نیروهای نظامی در برابر هرگونه اقدام دشمن آماده و هوشیار هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/658406" target="_blank">📅 13:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658405">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65cfee9959.mp4?token=rFF6kwMpnPzZEwlQxpMvssCMuSFJMpKt7xtd0hfAeA1zoK1O3LnUjk6sgIkoHlGWdsNrC4GhJnNqS3SIwxfMrV2yw0HBSkRx8GyNR8RJv0HrWpk9ru38VNxQiTSrnVUrgkt8sMAabeEcsUh1VY9jzwesjZDSt3CQoDVHXmcwqg6dw_8vVZfobCde9kh237ZohnqXes4FMUMIW82-Gxjf7GgHIDi4IQlIBTom7pALEi3--dhrarnnWkJcQtWQ6T9ctIrsVjRxXzKUrSRO4tZq5hoINHLI1g33-o_MdRnWkngo_xzc_qIzoUMkRk8OwpoYeSD07rlpjfJfx4eT4qwoeCJly6pBzOZkq_tBtZyjGp2nMfLkA_nB34EzDyMzJtO-At7-uDqcZnOtQdEjA8KV0l7kCuK37lJQ2EIQaywP2oCnPoTKGxUaCzOAPMFRT2od5PFmQsQ3p8V3EeFMHY5-7I1wFbJVHJxXbbx7HUO0CatIeEb5WmY21foONkUmaiE1zK9VQAJXF8Qs5a0XOTII8v1jdQ5EmSLq5kZUtbi1U24saegSgaHR7k54R6cI0ajumFnC2Gp2AEPGpQynvvF9zzCM-VKbnKLe1e9J5iSC0pR5IIpKEhTqdrSM9ZJwKbhVUTVO0s-GT5qHcKQnXvrBKSn5VCEayctgEJUni9GGWHE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65cfee9959.mp4?token=rFF6kwMpnPzZEwlQxpMvssCMuSFJMpKt7xtd0hfAeA1zoK1O3LnUjk6sgIkoHlGWdsNrC4GhJnNqS3SIwxfMrV2yw0HBSkRx8GyNR8RJv0HrWpk9ru38VNxQiTSrnVUrgkt8sMAabeEcsUh1VY9jzwesjZDSt3CQoDVHXmcwqg6dw_8vVZfobCde9kh237ZohnqXes4FMUMIW82-Gxjf7GgHIDi4IQlIBTom7pALEi3--dhrarnnWkJcQtWQ6T9ctIrsVjRxXzKUrSRO4tZq5hoINHLI1g33-o_MdRnWkngo_xzc_qIzoUMkRk8OwpoYeSD07rlpjfJfx4eT4qwoeCJly6pBzOZkq_tBtZyjGp2nMfLkA_nB34EzDyMzJtO-At7-uDqcZnOtQdEjA8KV0l7kCuK37lJQ2EIQaywP2oCnPoTKGxUaCzOAPMFRT2od5PFmQsQ3p8V3EeFMHY5-7I1wFbJVHJxXbbx7HUO0CatIeEb5WmY21foONkUmaiE1zK9VQAJXF8Qs5a0XOTII8v1jdQ5EmSLq5kZUtbi1U24saegSgaHR7k54R6cI0ajumFnC2Gp2AEPGpQynvvF9zzCM-VKbnKLe1e9J5iSC0pR5IIpKEhTqdrSM9ZJwKbhVUTVO0s-GT5qHcKQnXvrBKSn5VCEayctgEJUni9GGWHE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار ارشد بی‌بی‌سی از جشن و شادی مردم لبنان در برابر سفارت ایران می‌گوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/658405" target="_blank">📅 13:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658404">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e22766b2a2.mp4?token=c5S6n-NJzoXMjcI0eVQo4DN54PKhfTAXLjhQrFfVAtULBZuwywYZxnNkMcHcFpClZnTRfwWpnQKlV4KcAOTgMNOX1dBmvBnB-AD_aqUTij15BSnFa7gcYdsa5aGvXFsbSKBIQUP18uIi_spwJQEQ6gzh1qwSMokmwtWX47y6r_4sN4Rj9km5UVTX0kzutlAJkyiJ92Bz9Zsi8ZVr3DkRwwebaq-odTwtKRICfRPyPSF6qPKYSr4qDyxw5IrWuWBnQG065ho8r6WDgI749jABFCKVi6yfHV6cv11qtvV_rHGMJSWFTer_UNobgzmI0xGigxULYH3pQdeVHttkfRWQ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e22766b2a2.mp4?token=c5S6n-NJzoXMjcI0eVQo4DN54PKhfTAXLjhQrFfVAtULBZuwywYZxnNkMcHcFpClZnTRfwWpnQKlV4KcAOTgMNOX1dBmvBnB-AD_aqUTij15BSnFa7gcYdsa5aGvXFsbSKBIQUP18uIi_spwJQEQ6gzh1qwSMokmwtWX47y6r_4sN4Rj9km5UVTX0kzutlAJkyiJ92Bz9Zsi8ZVr3DkRwwebaq-odTwtKRICfRPyPSF6qPKYSr4qDyxw5IrWuWBnQG065ho8r6WDgI749jABFCKVi6yfHV6cv11qtvV_rHGMJSWFTer_UNobgzmI0xGigxULYH3pQdeVHttkfRWQ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دست‌نوشتهٔ شهید فرشته افشردی، دختر سرلشکر شهید باقری، که در میان آوار‌ها به‌جا مانده‌ بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/658404" target="_blank">📅 13:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658403">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a7a0f469.mp4?token=u_OWVjl3sh-J6j3VaVxqKqaShkuz31w5GM3M4pJJaFV0FvgfleONXeNgF3TVdkZJBCNrW6NQxwPxg1Gf_9sh4vDJrTajlWl_BBVik6GJEH4p1yr70JMMcUvDubS1xXtrV8wM3jgMgCAqXGwOjzxAF3VPyOMwk6LqSJJjBUiQtbNuxzYIwqQFnWE74QkrVhLXL-cxYH3sxTCBvCC6Mj6E0s3Qv2PrspO9XjViNeHrurTOQUM_sSqOEeQzrJ4RM1h4lFGaNxWSEzv6eVF-z4XII2Ic6WAmn-5dPUWTuRQl6ggLOlowiGlWcw9UPUUvVyzbkBRfzkEnZZiAOxHtxfLIoFLTzbutkbsEt-DF6WZHMxMCFaREKhIgIGt4BWdPvmeAfb79j4etFv3wOIKk8TxBL1zKmu4q90Rjww7NVMY36f2tO7lC-Pn85KtrHzPvj7pt18CCwxGe42Ck8bY0hanbrtK38-uQAIPTgpU6huZzJRivHcUN0NqgzSDdGBbrqaamp-LD5_87JxyoRTIkj3hpaFPaQ0QIq-sORpKjhf7KcoLusA89xcgOiCL6FJ9cF_Kiollq_eZsFVQ3U8UAChBa2_9PwdsV_8Gly33A9j4bexO6CzhWkBlfE2B5lYOQeeYhmciZbH5xjTj3LPUmQCX4uLD43xYXAIkrgVpUCbKKFRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a7a0f469.mp4?token=u_OWVjl3sh-J6j3VaVxqKqaShkuz31w5GM3M4pJJaFV0FvgfleONXeNgF3TVdkZJBCNrW6NQxwPxg1Gf_9sh4vDJrTajlWl_BBVik6GJEH4p1yr70JMMcUvDubS1xXtrV8wM3jgMgCAqXGwOjzxAF3VPyOMwk6LqSJJjBUiQtbNuxzYIwqQFnWE74QkrVhLXL-cxYH3sxTCBvCC6Mj6E0s3Qv2PrspO9XjViNeHrurTOQUM_sSqOEeQzrJ4RM1h4lFGaNxWSEzv6eVF-z4XII2Ic6WAmn-5dPUWTuRQl6ggLOlowiGlWcw9UPUUvVyzbkBRfzkEnZZiAOxHtxfLIoFLTzbutkbsEt-DF6WZHMxMCFaREKhIgIGt4BWdPvmeAfb79j4etFv3wOIKk8TxBL1zKmu4q90Rjww7NVMY36f2tO7lC-Pn85KtrHzPvj7pt18CCwxGe42Ck8bY0hanbrtK38-uQAIPTgpU6huZzJRivHcUN0NqgzSDdGBbrqaamp-LD5_87JxyoRTIkj3hpaFPaQ0QIq-sORpKjhf7KcoLusA89xcgOiCL6FJ9cF_Kiollq_eZsFVQ3U8UAChBa2_9PwdsV_8Gly33A9j4bexO6CzhWkBlfE2B5lYOQeeYhmciZbH5xjTj3LPUmQCX4uLD43xYXAIkrgVpUCbKKFRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جام جهانیه و توپش؛ مرور توپ‌های ادوار جام‌های جهانی از ۱۹۳۰ تا ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/658403" target="_blank">📅 13:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658402">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اصابت پرتابه آمریکایی به لنج باری سیریک در دریای عمان   فرماندار سیریک:
🔹
بامداد امروز پرتابه دشمن آمریکایی به یک لنج باری متعلق به اهالی این شهرستان در دریای عمان اصابت کرد؛ این لنج حامل کالاهای اساسی بود که ساعت ۵ صبح از شهر خصب عمان به سمت سیریک حرکت…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/658402" target="_blank">📅 13:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658401">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سرقت از تنها کلیسای ارتدوکس تهران
🔹
پس از سرقت از کلیسای سنت نیکولای، تنها کلیسای ارتدوکس تهران، پرونده برای رسیدگی تخصصی به اداره هفدهم پلیس آگاهی ارجاع شد.
🔹
این در حالی است که پیش‌تر سفارت روسیه در تهران با انتشار پیامی از وقوع این سرقت خبر داده و ضمن ابراز تأسف، خواستار بازگرداندن اشیای ربوده‌شده از این کلیسا شده بود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/658401" target="_blank">📅 13:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658400">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
حمله پهپادی ارتش به ناوگان پنجم آمریکا در بحرین
ارتش جمهوری اسلامی ایران:
🔹
در پی تجاوز آمریکا به جنوب کشور، ناوگان پنجم این کشور در بحرین را با پهپادهای انهدامی هدف قرار داده است. بنا بر این گزارش، در این حمله آنتن‌های ارتباطی و تأسیسات راداری سامانه پاتریوت هدف قرار گرفتند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/658400" target="_blank">📅 12:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658399">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حملات شب گذشته منجر به مصدومیت ۵ نفر در استان‌های تهران و هرمزگان شد
جعفر میعادفر، رئیس سازمان اورژانس کشور در
#گفتگو
با خبرفوری:
🔹
مطابق آخرین آمار ما از ساعت ۲۴ شب گذشته تاکنون ۵ مصدوم در نتیجه حملات داشته‌ایم.
🔹
۳ نفر در استان تهران در شهر ورامین، ری و ۲ نفر هم در استان هرمزگان جزیره سیریک مصدوم شده بودند که همه آن‌ها مرخص شده‌اند و حال عمومی آنها مساعد است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/658399" target="_blank">📅 12:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658398">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKIePsrFbnWcSct9Rz8GM2Cw5baC7J5tlC7K6OGKNBx9Hxawfb4DjhAkElh0lMr2EOrb9XKwOir1FG9YO63dGKITMfYEAXGrRbhdVVoXFgB0sQxth50Tlr9zOmE_o9RVlr7Lma2H4WhT312WlNK9Jncq2KiRDTEA-pZrJZvBzks3r2-AVUcfcVjWT7wEhgL_H9oAcHElNiUfXmSKa82w6kfM0116fTAPT0BKrCugvzsLzAYh3ZkJ652_bJ5MFZyqvNzflZnPmPNLUUcmrOhP1sPW19azfY17AGFQtjdWTwxaakDpzq2c0yKpOcGsLHAqMVd438JZDriQqEWIKjo0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بین بزرگترین و کوچکترین بازیکن جام‌جهانی بیشتر از ۲۵ سال فاصله‌ است!
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658398" target="_blank">📅 12:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658397">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a6b46414.mp4?token=nskKF_4lKLsrC8S63zXCaNqD_FR-J8INZSuCtKus9YTsuSZW9hREGcWCv8H2WhaaCLyY6kM7UueALREQ3s6HEwmey-RBOy2ijJwoBCp7JsZUDiTpIl9h6G4eLkpSUXLlZA9ZE92L--LWmwOGS1tk6k93A_GuX6zlIVQCqs7aFEhQMK7xV2AqmEDbQ6A3-xX0uz5wieizUQTPF_uMs3xdqvAvWnCYwfZd0w5UEvRJf824NHbi3D4Z3-Q9Tu4bCA-518crgy42G7VjQdOyUXjkASkB1NpKjfmjp4lIDjp-BVhXGWRDmhZTl-_-mJ5qdPDSl7z-9cfZMi3nDxIaNNlV051bojjQZVqZN3Dr1FCYf_x7FCPjxSv-QY0cLHX1pxaQZsaaLVhIAPAA6q5vviVRQo_alWR0as08hBEyXAxcAod7sti80DvcuaN5JHRKd4w1hn9OgoB-BnIi_O4_6hYyGMG6N4uDKRGdA7NI2DZikrLY0oJk0fQ1NpKTsNqWbzBHl3SIEi6JYarf_3YbITpctdGztGaxvxQLfZZXPzPVTM4OepBJsvm7XuxdjGDky3jF1I2HCDDs-8DFS8C6TXVo95VZ46FzKS6E2rowiR5U5_7HwBdRQf_HW18Ey8d2NsCewqedOatNMs8BOhnJadgugtItFIsah7tnjkLyCHxNzO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a6b46414.mp4?token=nskKF_4lKLsrC8S63zXCaNqD_FR-J8INZSuCtKus9YTsuSZW9hREGcWCv8H2WhaaCLyY6kM7UueALREQ3s6HEwmey-RBOy2ijJwoBCp7JsZUDiTpIl9h6G4eLkpSUXLlZA9ZE92L--LWmwOGS1tk6k93A_GuX6zlIVQCqs7aFEhQMK7xV2AqmEDbQ6A3-xX0uz5wieizUQTPF_uMs3xdqvAvWnCYwfZd0w5UEvRJf824NHbi3D4Z3-Q9Tu4bCA-518crgy42G7VjQdOyUXjkASkB1NpKjfmjp4lIDjp-BVhXGWRDmhZTl-_-mJ5qdPDSl7z-9cfZMi3nDxIaNNlV051bojjQZVqZN3Dr1FCYf_x7FCPjxSv-QY0cLHX1pxaQZsaaLVhIAPAA6q5vviVRQo_alWR0as08hBEyXAxcAod7sti80DvcuaN5JHRKd4w1hn9OgoB-BnIi_O4_6hYyGMG6N4uDKRGdA7NI2DZikrLY0oJk0fQ1NpKTsNqWbzBHl3SIEi6JYarf_3YbITpctdGztGaxvxQLfZZXPzPVTM4OepBJsvm7XuxdjGDky3jF1I2HCDDs-8DFS8C6TXVo95VZ46FzKS6E2rowiR5U5_7HwBdRQf_HW18Ey8d2NsCewqedOatNMs8BOhnJadgugtItFIsah7tnjkLyCHxNzO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بالگرد ارتش پاکستان با دست‌کم ۲۲ کشته
🔹
طبق اعلام ارتش پاکستان، یک بالگرد MI-17 ارتش دیروز به دلیل نقص فنی در کشمیر تحت کنترل پاکستان سقوط کرد و تمام سرنشینان آن کشته شدند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/658397" target="_blank">📅 12:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658396">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAj6n5BAj1E9tY4rgqBJTVNDNR3hhZX3oN0CZpuPL44WJPEVprP-OdUpk4A0WvOGzQ_gOSEE897GLLnkrs8XQoH1ry1GYp-L7NR_QHVscuPpcDNwttf_ShpFol2LWy_mNhzhTq7cr0zfk6bXsvXIYkyZOllGnqnWMsNQwl8TXDXIRmd3E5Tr3HH97L96IM4gdGa4PjJxeltuWvNwqv53jo6hE2vQWLT4IrHw5q0jDkNK0IxhS3YkO5l5mND4vc5FtuYLXBia4gyw3wCw3ZVrxZYDvEIb1Jmo1SdQNEp2C-st7rPiV0tzLrsb1I0v5Us0ovqSdwY-mezI2cZki-cZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نهاد مدیریت آبراه خلیج‌فارس: تنگه هرمز تا اطلاع بعدی بسته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/658396" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658395">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای رویترز: مذاکره‌کنندگان قطری پس از مذاکرات با مقامات ایرانی که تا ساعات اولیه صبح پنجشنبه ادامه داشت، روز پنجشنبه تهران را ترک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658395" target="_blank">📅 12:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658394">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08fa32d868.mp4?token=KbYxbrclsTdxzlRvkkftOI75LpwiOQFWCbMzL7HwKRX_4ThhOR15HNq_V0OUsYr2WvCwRojDqseCkHNMcX7Rt7fn0VssVIrRe4cagVGnwqzuF6ccxi3llmuJdJ85pg_-qFXh6_kFIJU-phGl4SGJn2FrvepP09alKggasWhj7k9A_Jc3oH_BGb4968szhrhlLXGKQNmMHmGfCEEsHhDnLwQSBw_blJHilN22aBcPNfigC_vVhGDub9d5hZl73h3blzug1goWH2jV8yzDiazrqPRccgWp3j9k6hOiuAb6L41SZ3u5nRxDmj3xJRvl30vHXVP16dOwz1X3sUuUCsTomw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08fa32d868.mp4?token=KbYxbrclsTdxzlRvkkftOI75LpwiOQFWCbMzL7HwKRX_4ThhOR15HNq_V0OUsYr2WvCwRojDqseCkHNMcX7Rt7fn0VssVIrRe4cagVGnwqzuF6ccxi3llmuJdJ85pg_-qFXh6_kFIJU-phGl4SGJn2FrvepP09alKggasWhj7k9A_Jc3oH_BGb4968szhrhlLXGKQNmMHmGfCEEsHhDnLwQSBw_blJHilN22aBcPNfigC_vVhGDub9d5hZl73h3blzug1goWH2jV8yzDiazrqPRccgWp3j9k6hOiuAb6L41SZ3u5nRxDmj3xJRvl30vHXVP16dOwz1X3sUuUCsTomw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزد، شهر بادگیرها
🇮🇷
#ایران_زیبا
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658394" target="_blank">📅 12:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54178dc8c1.mp4?token=dPTiwazcT7AZ8QPCcAGr98kryoP7XcYK9JlgD9nop46dvCEn-m96F9tvlZs8X_RwP2jTH9xWxK8_Z6Zz0ZO-4VSeh0bYls0PQcVa-Fr3ubwsSZCbZEODhV6zAvTHeb3qwIh_GDCYBdRAjQHPDPwY8MGQNt3N0rcmCASler2ycuepVPIIBw6xV_mqfaanlGd5wJz-blX1fRZxSzW8ytVJ5SfQUz1lOtW9Tae02SHUnS_OJ09Bs8YJXO_vGbXx_ulORS9CiVr82h0x7F-SbeovnY0OImJd8AKjf9Jx-_8Llm-g1hQ4lEY0awPhK5xVYd0VHtE99RIaA8OFlJtv6KgE4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54178dc8c1.mp4?token=dPTiwazcT7AZ8QPCcAGr98kryoP7XcYK9JlgD9nop46dvCEn-m96F9tvlZs8X_RwP2jTH9xWxK8_Z6Zz0ZO-4VSeh0bYls0PQcVa-Fr3ubwsSZCbZEODhV6zAvTHeb3qwIh_GDCYBdRAjQHPDPwY8MGQNt3N0rcmCASler2ycuepVPIIBw6xV_mqfaanlGd5wJz-blX1fRZxSzW8ytVJ5SfQUz1lOtW9Tae02SHUnS_OJ09Bs8YJXO_vGbXx_ulORS9CiVr82h0x7F-SbeovnY0OImJd8AKjf9Jx-_8Llm-g1hQ4lEY0awPhK5xVYd0VHtE99RIaA8OFlJtv6KgE4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اذعان ارتش اردن به حملات موشکی ایران  ارتش اردن مدعی شد:
🔹
بامداد امروز هدف حمله با ۲۰ موشک قرار گرفته که از خاک ایران به سمت منطقه الازرق شلیک شده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658392" target="_blank">📅 12:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
پاکستان: میانجی‌گری ادامه دارد
🔹
پاکستان با ابراز نگرانی از شکنندگی آتش‌بس و هشدار درباره تداوم خصومت‌ها، بر ادامه تلاش‌های دیپلماتیک و میانجی‌گری خود برای دست‌یابی به صلحی پایدار تأکید کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/658391" target="_blank">📅 12:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658390">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
همه حجاج تا ۲۳ خرداد به کشور بر‌می‌گردند
مجید اخوان، سخنگو و سرپرست روابط عمومی سازمان هواپیمایی کشوری در
#گفتگو
با خبرفوری:
🔹
وضعیت پروازها طبق روال گذشته در همان فرودگاه‌هایی که طی اطلاعیه‌های گذشته فعال بوده است، هم‌چنان ادامه دارد. فعال شدن فرودگاه‌های غرب کشور در حال بررسی است.
🔹
تا ۲۳ خرداد بازگشت حجاج به کشور به پایان می‌رسد و از طریق هفت فرودگاه امام، مشهد، گرگان، زاهدان و...برمی‌گردند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/658390" target="_blank">📅 12:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658389">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554c9942ea.mp4?token=JNMQHSHSnF4bz3BVmdu-qjwWDGPqtBpdhhXS6GA3Ht_CrFfb9S5IrWarZbUOAhF3PKJUzIVc5hfFNX8IPInfUXDUGsI3S4cUVDpPep0AXI70ZpU7XCHV8rBP75Gdcov0gjDnGMu87Yx1t4B7lRflfalZJ3VeCBPB92oExa-mGt3UYN4sGDN753DzU-Y5IMUOSPb8ZKHT1dAELLlE3JvK1LvmJvmK3NRpeODJfsDQtV3Kw9kF5zriWlmMmQtdFMBOgUgBx89fpXTs2lc8duYFtYdBxKk58GgBGHlBsC-t4qSivt7GOH0ztJRyUhr1FYH-zFtdQbBXTNqSLEXhdAtHkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554c9942ea.mp4?token=JNMQHSHSnF4bz3BVmdu-qjwWDGPqtBpdhhXS6GA3Ht_CrFfb9S5IrWarZbUOAhF3PKJUzIVc5hfFNX8IPInfUXDUGsI3S4cUVDpPep0AXI70ZpU7XCHV8rBP75Gdcov0gjDnGMu87Yx1t4B7lRflfalZJ3VeCBPB92oExa-mGt3UYN4sGDN753DzU-Y5IMUOSPb8ZKHT1dAELLlE3JvK1LvmJvmK3NRpeODJfsDQtV3Kw9kF5zriWlmMmQtdFMBOgUgBx89fpXTs2lc8duYFtYdBxKk58GgBGHlBsC-t4qSivt7GOH0ztJRyUhr1FYH-zFtdQbBXTNqSLEXhdAtHkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جواد خیابانی: سردار تو تیم نیستی ولی هستی، بعضیا وقتی نیستن، نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/658389" target="_blank">📅 12:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658388">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA4Q068bjBiT0a1a5q1WsG2EmZDiM814GxIH4foVlyeSeBWiPKdq7-J2-Nc8t9xh36qex-ckLhZu0G6RRPja71YStgs4aHsJTwQEP3PCTD37EpD6hlgSOLcuZHQ2j0RjZghVxHnAeXhDklT3zde8FjLwIM8trdoKG-f8sqJZTAp-KotxjY3vcZrjK9qpjGc7iCZxzPdc5_TOBsh6S8tapt3crGQGno2_SEWKkotfJByf9xeXRqW4JArclK5o_KlUiXIXmif_RSZsQX-C8suDNKghYvp7PAw4sSxoq-q463AHKZgb15I5FITFA6E67wGlOZktdWRF3SyKbAElXM-z4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/658388" target="_blank">📅 12:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658387">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تداوم حملات هوایی رژیم صهیونیستی به شهرک‌های جنوب لبنان
🔹
ارتش رژیم اشغالگر در ادامه تجاوزات خود به جنوب لبنان شهرک‌های صریفا، برج قلاویه و تولین را بمباران کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658387" target="_blank">📅 11:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658383">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbV7ox8cFqPl8ZESYDwzJe7raZAOlcfjt1BBjj-W4KMB9M1jHUDX875jZ7T29MoVWgOT7I60-As8k7SisHtFqv9BRrYyUvs2hESxu_mCfugL0ZY9BPeg7XOdxlpAxSKM40A5dBrU3JslBdbd_Apa3dBpgpi7Qb1EWVwJ2xIipAKjw_Aljx0jCIrENPFKPl_XrLqW5EmzrgeNJPiglgGxwUyHm2oH1JrW0pgks3Nszw1Hh6SkIgz6aqGUPPdSi9m1X6XDFJfE0W9EBqRVKpn72XeLuy6LOhjqJMMyTmCTTr-ufZDEzrdOrKvaPEl1k7w_iUL-u04Fo1T7ERHPDiA4eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SiLy2s7xsjoaIiS6vkXBMmtzhwlISapEm3cVnsimTGK2FaNvqAIHeascmu9cgkRGB6T9mP-SGbLuqHblOFhkLywwzUa4L5l4OBsJhqbJjPzZY3RCYbSkaoml7oQ2HSRnfUEWHo92dYg5w1Wt80zP-3tTupP0lOtqaI45gX1r0fuXYYm3zCSZuVC3Soi_MU5feZDRdLC6-HsBMGrAo4xJZpJPny-WyA7mrytaCIrbC3xmJM1Auwcq6M-uhCVFRhO7t1_HJ0ZkfvSMIF2oyRBqVjjlM9buJUWGpNksOp8Wi-8eadqWmJns_-MK6PodmJ48KEAjMPaQDZp4yFHPOkEevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSEnCQ1Nb3-zE-EHm00Y1HcwPxD01ZflJI_FawygL1nsT5gdfLNEt-0ugU9fcFVhuCyQjdjfBcl4uqaeWQYpbkGLsz36JCazv04i7YvnsHWymsD043ghtd1UMxrEMPgfe_8cE5zHglMvdNmgwVAfvuYTWMKxp-d1Y7esd0wLUB2zmBkBnyIuJwUnYxfCHP97sUyLwW-rneBLKFtLxTVkxisV0eNw-DBFLDBDP5cta2jME2jqn-lrKmUGd-K5t_t9O5pj1XVONj8ImPdlWikoqxbCxjNcSQSsotFhFnKdFwh1VTm9b6penplHpFUCywHukCxY9Jw1LwyMRlJRcxIf9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwExCyIupDUG0CvLnD2-MDuCkEZo3d07exESfy4EbzjeqK73SEaxyfCqkKXFfIDpMXekpfkWZOy4wTIYz-ROACGDpb9vefNqc9gXtHI-l59z0ZHf2YIpetZSVpq6C9R9Ta9wVpz3BL0Y1cVvMyp_uH-aX-H6CGq5Q5Qbpoge56oOmvpzewx6PAnIcpq5v1xeptZKFXKXxk1bl-Dq3BNyvGdRtyoEdhHOA-gnAojm0iMmNc2CoOHLSIf-9FG2AippKCVs8mgT8zyRZB1d4Tj7J8eD5zZwOTV0zurrpaVECAMo8BxeuHZrWczVjrD_qc6DJ_xtYM7c1ZAxtvmCKYXmsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رونمایی فیفا از جایزه کفش طلا؛ توپ طلا و دستکش طلا برای بهترین‌های جام جهانی ٢٠٢۶
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/658383" target="_blank">📅 11:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658382">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
مصاف ایران بانایب قهرمان جهان
🔹
تیم ملی والیبال ایران در دومین مسابقه خود در هفته نخست لیگ ملت‌ها ۲۰۲۶ از ساعت ۲۳ امشب به مصاف بلغارستانی می‌رود که در حال حاضر نایب قهرمان جهان است.
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658382" target="_blank">📅 11:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658380">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSocZ4BXXSkv7tkjvQhmZ9_YLlxcTO76b2-0kVKvhGJ0CTE6ltO9LEYVaxQVmmQ1JTcEzQbluzunLOa4fp1BROKjBWKGMyA-dLlwhPiJJebMzG8jghnYCOW4rHX4XjncF7a9IFp5nt7Sl1XTZKo1le5oB36B0tGhN3KLw18DzLHjz2_SbuPXn-PPEiKa64UuGH1IZJTXbwSEONZl23cLHRFAXM2FKhEDoEckhVAIjBMmt2o-efjpdLD61IYoCr8oFHRAB27zFMsCfIgm_DHUxers8P4wcB18HtSrNj5akj6xor1bqjSHM3mP1XkAjlEya3MSDYBc1rpOrqeVGDmzaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kz1HrncVhmJZE9RAptHr1OOSG8d7YZi0yQ5xqJ4AghZ_wEZGxvBjYHT_hDsQ33je7zTPLfBDHGuB7V8vdRhaYozthg_omr_gF1gpCBZYFsjYd-07oxM1LF4QgBmUPGzXiNbiqk_rcUE2WaGa9D6sH8T8_rcblVxhMWcV89hUFCPqiNm_TBE5OIA95L-ng5TxFwDAdp4BdS8w9SpzNU2m35b4LtD2OO_UfvjuFuVEBHDzckTt4DVR2gQP5hDVJ-4uPjPoWufqyWS7V64epvFlzCqvq6HsqsIMJEvAnAf9KHYHp5tnvKSDLueaw_XiUa-WKpoc8kH9OUGXKMCGGK3oWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تفاوت‌های روان‌شناختی و مغزی تک‌فرزندان نسبت به چندفرزندان
🔹
بر اساس یافته‌های روان‌شناختی، تک‌فرزندان در مقایسه با کودکان دارای خواهر و برادر، از خلاقیت، انعطاف‌پذیری و ریسک‌پذیری بیشتر و روان‌رنجوری کمتری برخوردارند، هرچند ممکن است همدلی کمتری نشان دهند. این تفاوت‌ها که به دلیل تعامل و وقت بیشتر والدین با تک‌فرزند ایجاد می‌شود، منجر به افزایش ماده خاکستری در نواحی مرتبط با کنترل احساسات در مغز آن‌ها می‌گردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/658380" target="_blank">📅 11:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658379">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdJLIu429mlAJTXlVvhYIZcAYLrAfmVWBLFeUoZI9WY9n1vV7SlqdlNP2fAHMUWX2wt1-lTpi55U72pe-rIRVBtFKFfxMRnkODTl7WlYarVN6J5YgljuwC4BCTeAZWl41OGHT5MwOTabOA2I_REsXvgsGlvyo7LZwbYU4ahZs96emaCqmUxTykrM74nO4WGB9izSE0JAQaggQPgFvZPcgLhh_AtvOZeBzrQhVH2FRuz0IcMStnjuXOTLNd0ma-0S4TxoMoZQ2LOWXVcRXXjT8ewlEUIuZnRDzTa9-0E26LDWMx5T5AxVERE7RMcRECaK-iATkgF8rf3tW050eL6DVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازیکنان بالای ۴٠ سال جام جهانی ٢٠٢۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658379" target="_blank">📅 11:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658378">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای رویترز: مذاکره‌کنندگان قطری پس از مذاکرات با مقامات ایرانی که تا ساعات اولیه صبح پنجشنبه ادامه داشت، روز پنجشنبه تهران را ترک کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658378" target="_blank">📅 11:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658377">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zat79mk-7KQw1nPv8Z4iiFY0rmZQOC-6SOAotEL5LaDZCFNk5xKYhwTF3BWmiNapUPOao-0MgOVddUcAsbg2UUnPRIXm7cNG-KwPwsuJF4li2T4hxVMndnCHKGWsN2bWGSrJRBymKAoY_iQ_YD1BUHObC_g_pKIDL4D4s6R8_OFymT-pV-QBz_WS7T6IVM9btG_DfgX0Ev46OK4W77WwVM1A5OOCxmArPm3Lt76IgIAsY3SvSqhGmzUUMtB1xyB2WVIW5PnHRDyW5QFnOB7jR29FBGLiZd_bmOL9DxhLPF_jkMJDpAZyGyt4euzS8sRuKSvJ-1lTY-Ws6qseUMXQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه در محکومیت نقض فاحش آتش‌بس توسط آمریکا
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/658377" target="_blank">📅 11:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658376">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان به نقل از یک منبع دیپلماتیک: گفت‌وگوهای آمریکا و ایران همچنان ادامه دارد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658376" target="_blank">📅 11:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658374">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad965b180c.mp4?token=U45dqAVwCPZPKyUtoC4IMauaxwYjpfS-fgqjtSjcSj3NEWCx9hnJVFy6c6QJ7-y7sBz_GTR6uhZubKzBWsKX2emq7ILlNXo1P7c-hD1vbjnsDUmp_5v7Qr1sqAev_yUL2dyvJC6uT5ZCjHJEQl9ki431AjiarA_DcrfB7ZaSbLfTbCiX5uje-BXXAKOjsbZjFcx_Cx9fB69hXEhJlDoJEc4Q6f0QpTT1iZosKFmKdu480p57n1_WdZuqDpGMkrYKDiMHiB1OWqcEMGf5DPzKCNNzydfjE6t0lu91XG2GRKXymmlHrZyI9ZsImH1ITh4Em6MxAxrkR39BlJiqdyfjMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad965b180c.mp4?token=U45dqAVwCPZPKyUtoC4IMauaxwYjpfS-fgqjtSjcSj3NEWCx9hnJVFy6c6QJ7-y7sBz_GTR6uhZubKzBWsKX2emq7ILlNXo1P7c-hD1vbjnsDUmp_5v7Qr1sqAev_yUL2dyvJC6uT5ZCjHJEQl9ki431AjiarA_DcrfB7ZaSbLfTbCiX5uje-BXXAKOjsbZjFcx_Cx9fB69hXEhJlDoJEc4Q6f0QpTT1iZosKFmKdu480p57n1_WdZuqDpGMkrYKDiMHiB1OWqcEMGf5DPzKCNNzydfjE6t0lu91XG2GRKXymmlHrZyI9ZsImH1ITh4Em6MxAxrkR39BlJiqdyfjMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی که در فضای مجازی منتشر شده، نفتکش دچار آتش‌سوزی در نزدیکی سواحل عمان را نشان می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/658374" target="_blank">📅 11:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658373">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuR48T2pa1CWZ2g1mn2tXt3qm0_qgZW0IFtkgQqZhlPhmOcnLO-FYDw8lGrVvtTs8UkQCl9GG7UiIKMBAi-SGwAKZ4O-cqG1dmwy6NhL0O194AwuJZlC3LPFJlQhFcn4EkqegeFcCWgafvgOo4pAaFs0AqXFFjZF2RVCW4DfNqMfsMA5T796UV4FYcK6srxsVjf-5T6Stnv1CY8PtbY5BaBW6PRmdoolLn2OuQ-Iql2FIrK0s3paanT-6L_y6XIF6yUkXDL6BtGWUCExO2YVYXYJ-wUfzkGa7KDnR8frQEQDQ4vBVaDrRuZDYc_8UTIghlDuhf7FaR_K7d3ons8mdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا دیشب باز هم ترامپ گفت توافق نزدیک است یا ایران به دنبال توافق است؟
🔹
ترامپ به دنبال ساخت واقعیت جدیدی در اذهان عمومی است، او می‌خواهد القا کند آمریکا از موضع قدرت مذاکره می‌کند و ایران مشتاق توافق است. ولی در این بازی کسی که بیشتر فریاد می‌زند، معمولا دست خالی‌تری دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658373" target="_blank">📅 11:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658372">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
جزئیات تازه از عملیات ایران علیه پایگاه‌های آمریکا در منطقه
یک منبع آگاه:
🔹
ایران در حملات بامداد پنجشنبه به برخی پایگاه‌های نظامی آمریکا در منطقه، یک طرح اطلاعاتی و عملیاتی پیچیده را اجرا کرده و خسارات قابل توجهی به تجهیزات نیروهای آمریکایی وارد شده است.
🔹
نیروهای ایرانی از زمان برخاستن دو هواپیمای بزرگ P-8 آمریکا، مسیر و محل استقرار آن‌ها را زیر نظر داشتند و محل استقرارشان در پایگاه هوایی شیخ عیسی در بحرین و پایگاه علی السالم در کویت را هدف قرار دادند.
🔹
ایران با رصد اطلاعاتی و میدانی، محل استقرار دست‌کم سه جنگنده F-35 آمریکا را در یکی از آشیانه‌های پایگاه هوایی موفق السلطی در اردن شناسایی و سپس آن را با موشک‌های برد بلند سوخت جامد هدف قرار داده است./ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658372" target="_blank">📅 11:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658371">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658371" target="_blank">📅 11:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658370">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اصابت پرتابه آمریکایی به لنج باری سیریک در دریای عمان
فرماندار سیریک:
🔹
بامداد امروز پرتابه دشمن آمریکایی به یک لنج باری متعلق به اهالی این شهرستان در دریای عمان اصابت کرد؛ این لنج حامل کالاهای اساسی بود که ساعت ۵ صبح از شهر خصب عمان به سمت سیریک حرکت کرده و در ۵ مایلی بندر خصب هدف قرار گرفته است.
🔹
این شناور ۱۵۰ تنی ۵ خدمه داشت که با کمک شناورهای عبوری نجات یافتند و به عمان منتقل شدند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/658370" target="_blank">📅 11:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658369">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
۳ مصدوم در حوادث مرتبط با حملات آمریکا در تهران
رئیس اورژانس استان:
🔹
در حوادث مرتبط با حملات وحشیانۀ امریکا در استان تهران ۳ نفر دچار مصدومیت شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/658369" target="_blank">📅 10:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658368">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
اذعان ارتش اردن به حملات موشکی ایران
ارتش اردن مدعی شد:
🔹
بامداد امروز هدف حمله با ۲۰ موشک قرار گرفته که از خاک ایران به سمت منطقه الازرق شلیک شده‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/658368" target="_blank">📅 10:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658367">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257539272b.mp4?token=lhiPBtABYb0uI5Sq5vCWJnKlz-BezLcTf3os3y6f4CuFn-9auUjrc7gNU3DO1ngJqjsfHNEfF5vmG14A_yqd-JhuOlk_U6KsyQ0WqucB7lkow0rC5oj-GNArJ0YHRO9Nf1fUyPEj7azWXdm7IaJA_04Y21P7sTwUeAzxtNeiTvofxqiuq8vy3xACiR1L8LlzzZPrwrLxC1FG_jSKokEPk4Jd7azkZEZts9btdCiPmv-LiSqJSzwf45HaYu39fsmmQQB0FeSvKHK9Bu3XEjBm9QdEVGt_VD-T3C3a9mAYXfL00Bm3oIVsVwn7ZgwLO4efvHE_gv_GfL3gCzPxqqLU7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257539272b.mp4?token=lhiPBtABYb0uI5Sq5vCWJnKlz-BezLcTf3os3y6f4CuFn-9auUjrc7gNU3DO1ngJqjsfHNEfF5vmG14A_yqd-JhuOlk_U6KsyQ0WqucB7lkow0rC5oj-GNArJ0YHRO9Nf1fUyPEj7azWXdm7IaJA_04Y21P7sTwUeAzxtNeiTvofxqiuq8vy3xACiR1L8LlzzZPrwrLxC1FG_jSKokEPk4Jd7azkZEZts9btdCiPmv-LiSqJSzwf45HaYu39fsmmQQB0FeSvKHK9Bu3XEjBm9QdEVGt_VD-T3C3a9mAYXfL00Bm3oIVsVwn7ZgwLO4efvHE_gv_GfL3gCzPxqqLU7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رالی تماشایی بازی ایران - برزیل
🔹
برزیل در خانه در نخستین بازی لیگ ملت‌های والیبال ۳ بر یک ایران را شکست داد.
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/658367" target="_blank">📅 10:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658366">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6eoCRY4ZYRZNpHLblbbSFhqpveRTM7XRWOqo-qi1c0Q1RFw7Yc18tVbfQzpp0KH-JLpigJ-37AmOihzyasuoniJBxa8YmuCOSkoJo4zHXLOpLmG5_K0YyskcVVPYm8xx2R3tdYZaifJ9XrMynVEsYwPFM9sj4gJydGSNLkLvY2OoYTbc5nA45UICUs5ddYXyia3DFqdBu0S1G9Y4_PZhKpKtMJ7hoEkyK6P3t8B_koOFcaizT0tLJtkFRP7N1XwA7gdCsu1Ae3ypk8kDTzt0gHMXwg5TAcEwpG4ENrhkUNwNYEMGbt8hhce5nIu1cTgc4SHwLfvVoZRphEJMVrUBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش حادثه در ۲۱ مایل دریایی شمال‌شرق صحار در عمان
🔹
هیئت عملیات تجارت دریایی بریتانیا از دریافت گزارش حادثه‌ای در ۲۱ مایل دریایی شمال‌شرق صحار در سلطنت عمان خبر داد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/658366" target="_blank">📅 10:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658365">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3494c4c7ae.mp4?token=ZC1wnEJOrsJAxgAIUD2XOg8OsbdiAsKFZneoexu3h5c-ko42NCkl2jDJXaZhlTT6de3sVdFsn0CKqSMZmH2dB66a54f3-WR_TbP3XuGLNaSjeL2t5T5MysVklVSLdb6P7R7FDyFejWg28FvP0iXN9R6tDGhm6Ts4ozVyg-RzbicgHlMXuJRI_J0WagZc4BkqeWRWV1z0mAVMOt9_LBGQ23CFArSjI0VrpJKvuxCaKb8ozcSDipiYfq37kR_7rTPyt3EliAKu8QiPJDhEkgejJ7y0GDLjimblOxTMgmBOZ-g4N3tfBX04t8m7AxKXH86e-g7dyvVAG9zzfDswKLwEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3494c4c7ae.mp4?token=ZC1wnEJOrsJAxgAIUD2XOg8OsbdiAsKFZneoexu3h5c-ko42NCkl2jDJXaZhlTT6de3sVdFsn0CKqSMZmH2dB66a54f3-WR_TbP3XuGLNaSjeL2t5T5MysVklVSLdb6P7R7FDyFejWg28FvP0iXN9R6tDGhm6Ts4ozVyg-RzbicgHlMXuJRI_J0WagZc4BkqeWRWV1z0mAVMOt9_LBGQ23CFArSjI0VrpJKvuxCaKb8ozcSDipiYfq37kR_7rTPyt3EliAKu8QiPJDhEkgejJ7y0GDLjimblOxTMgmBOZ-g4N3tfBX04t8m7AxKXH86e-g7dyvVAG9zzfDswKLwEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎁
اعلام جوایز قرعه‌کشی حساب‌های قرض‌الحسنه پس‌انداز بانک رفاه کارگران
⏳
فقط تا ۳۱ خرداد فرصت داری!
💰
بیش از ۳۰۰۰ جایزه ویژه در قرعه‌کشی حساب‌های قرض‌الحسنه پس‌انداز بانک رفاه کارگران
🏆
۱۰۶۶ جایزه نقدی ۲.۵ میلیارد ریالی
🚘
۱۰۶۶ کمک‌هزینه خرید خودرو ۲ میلیارد ریالی
🏠
۱۰۶۶ جایزه لوازم خانگی ۱ میلیارد ریالی
✨
به همراه هزاران جایزه نقدی دیگر
برای شرکت در قرعه‌کشی کافی است:
✅
حداقل ۹۰ روز، موجودی حساب شما کمتر از یک میلیون ریال نباشد.
✅
در روز قرعه‌کشی (پاییز ۱۴۰۵) حساب فعال و دارای حداقل موجودی یک میلیون ریال باشد.
✅
کد شهاب داشته باشید.
⏳
فرصت محدود است…
امروز حساب خود را تکمیل کنید و شانس برنده شدن میلیاردها ریال جایزه را از دست ندهید.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/658365" target="_blank">📅 10:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658364">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
سرلشکر عبداللهی: نیروهای مسلح به هرگونه تهدید پاسخ دردناک و پشیمان‌کننده می‌دهند
فرمانده قرارگاه مرکزی خاتم‌الانبیا (ص):
🔹
نیروهای مسلح جمهوری اسلامی ایران با آمادگی کامل، هوشیاری و اشراف اطلاعاتی، هرگونه تهدید علیه امنیت، استقلال و تمامیت سرزمینی کشور را با عملیات‌های تاثیر محور، دردناک و پشیمان کننده، قاطعانه پاسخ خواهند داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/658364" target="_blank">📅 10:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658363">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eccb52d99.mp4?token=t2mM7ZsomT6MLmfnnToDMkvCQPQYygKkIHRvgm5HMZQh_8GWyt7FnQuF1QObLIZBn8FDc5U9i56I19XtcIvOheB3fg7b2HNrt-1Ggce-jEPSiSZz9IOd_qoOe8F_S_IkFk3ErpF2CDRmZzSa_mHJOg8OhNgQBwbkr8KGrCw_w3dZTX4npZXNCwkuOKJJKhAFMSenOSSDh43COIy0cCrCp9hrA6xzL2nIF2goQlzundUJRko4YSr8Yoxl4DKuMN7Sv6SGipMBshD8oGljaGgvGJzahrAG_Swjf3uf3AI9ugfumyQmJ0qw4vq41X_sK_hqS45F12rZvC29oFZ_JF88ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eccb52d99.mp4?token=t2mM7ZsomT6MLmfnnToDMkvCQPQYygKkIHRvgm5HMZQh_8GWyt7FnQuF1QObLIZBn8FDc5U9i56I19XtcIvOheB3fg7b2HNrt-1Ggce-jEPSiSZz9IOd_qoOe8F_S_IkFk3ErpF2CDRmZzSa_mHJOg8OhNgQBwbkr8KGrCw_w3dZTX4npZXNCwkuOKJJKhAFMSenOSSDh43COIy0cCrCp9hrA6xzL2nIF2goQlzundUJRko4YSr8Yoxl4DKuMN7Sv6SGipMBshD8oGljaGgvGJzahrAG_Swjf3uf3AI9ugfumyQmJ0qw4vq41X_sK_hqS45F12rZvC29oFZ_JF88ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون هیچ نفتکشی درحال تردد در تنگه هرمز نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658363" target="_blank">📅 10:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658362">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
زلزلهٔ ۴ ریشتری در نورآباد استان فارس
🔹
زمین‌لرزه‌ای به بزرگی ۴ ریشتر  حوالی نورآباد در استان فارس را لرزاند.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658362" target="_blank">📅 10:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658361">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0ac0ab15.mp4?token=jDEXTv9n4j8N0vrgtgfbjgQcsJiVcs7jaisLw4lPPwcn1lnF0k5FNd_0W42BaDdD-mGmPZyUnTnp_bCfjcVm9y2J2O3xn69jyMGjUt5xF1E5jWMoMbBD4Rp0dh_AaxifSBXnYhP_jHZM0YPd78BzmGyfQ31DLLR946fWT1XFcDHVMVV77HPplIK7nQnWvYPuLg5d2goVTR7s6zH97qt7W3cdnrg9LNXjoVsvdAE5Fob6WTbZiFbSPmB9i3uLf7qGz9VnYzDaDH_C9-K3IhEO-0SGHTqk3B_9ts5RCQRCgpVlVsIqLEEdcPvUF3TaVRdpsojeE2h3zKaW_kFeyfvlgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0ac0ab15.mp4?token=jDEXTv9n4j8N0vrgtgfbjgQcsJiVcs7jaisLw4lPPwcn1lnF0k5FNd_0W42BaDdD-mGmPZyUnTnp_bCfjcVm9y2J2O3xn69jyMGjUt5xF1E5jWMoMbBD4Rp0dh_AaxifSBXnYhP_jHZM0YPd78BzmGyfQ31DLLR946fWT1XFcDHVMVV77HPplIK7nQnWvYPuLg5d2goVTR7s6zH97qt7W3cdnrg9LNXjoVsvdAE5Fob6WTbZiFbSPmB9i3uLf7qGz9VnYzDaDH_C9-K3IhEO-0SGHTqk3B_9ts5RCQRCgpVlVsIqLEEdcPvUF3TaVRdpsojeE2h3zKaW_kFeyfvlgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جشن مکزیکی‌ها پیش از شروع مراسم رسمی افتتاحیه جام‌جهانی ۲٠۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/658361" target="_blank">📅 10:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658360">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
پزشکیان: بخشی از دهک‌بندی‌های فعلی مبتنی بر اطلاعات به‌ روز نیست و باید اصلاح شود
رئیس جمهور:
🔹
ایجاد بانک جامع اطلاعاتی شهروندان، زمینه ارائه خدمات عمومی متناسب با شرایط واقعی افراد را فراهم می‌کند
🔹
داده‌های ملی باید با بالاترین استاندارد‌های حفاظتی نگهداری شوند تا امکان نفوذ به حداقل برسد
🔹
قابل قبول نیست که برخی افراد با وجود دارایی‌های گسترده، از پرداخت مالیات معاف باشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658360" target="_blank">📅 10:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658359">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ne1q8o5QPaKeJiu0dsyyJrd4AJ_EgPPIBD0oQDxnQNR0rVeLQFoWLJmTkzmAmznHy4cNWfhEt-4LvFUIy36Qg0OtS1amhFUOx1MZINFiqAymFCmhkLKXnsLZT2SsI59GFH6hDERsrCyXv70Hx6PvuoHw2Rg7JGJGCjwIeJz6EnjAUvZF_Lujsfp1uMz9z-iYBDmkkYCpXdgmA9VLLu9ob5BktZnd8ocqdtBnYxsoU2gARhRJReKgedRlWfwsvZ0Xr4E8wdNivhYr1XTtqHqbBe036POvDd4u30KK8YiNdrwgxfG7YlDMnRUKR5VYZx6uGbXMBPNmBWBVpA0XqImTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه کامل دژهای نفوذ اسرائیل در خاک سوریه
🔹
اسرائیل از قله جبل‌الشیخ تا القنیطره و الیرموک، شبکه‌ای از دژهای نظامی ایجاد کرده. این پایگاه‌ها که برخی از آنها، زمانی متعلق به ارتش سوریه بود، امروز به «چشم‌های اسرائیل» برای رصد موشک و پهپاد و سکوی نفوذ به لبنان تبدیل شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/658359" target="_blank">📅 10:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658357">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcXiqHpZNoQf5Xvjx_zS8ciD9-pjzQgQjNtcGNyYdZPb5NnVqMW7RLnkaHoMq-UTypneNfs3iLgc0E0U4Kr18bI1QQwcIOnmDTTCDlSI86aPcfZx4YkW7PUHd3b8HThnQuwvqfyXs1gSe5_DsEcgyqsOhhLvgS7ifb81a25trGGMxZMbfnjDrLqZlxicVHK2g95nfxc47f79DxStt6q76vpGetSvtfYUnT2G8bdfGKIG8Im04jzdMEwJzY3Sg8wp75W5iVTbkOGzTGnkUMuXPXRfaix7-OI73Oqhn2ms2Bp8Y3E1MFt1mNArzxr7SYL252YFT2Dm45yMiqcHkE5oHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDlZIpDdZCetiTvfUYnlz4gXhDk9H_bcl6LR4v6yKe95CDilXpRcdcZzuGGwPTDMyldlmHfECyJ6EzW2zMA1wI1le3AA-X5-ktV4FDUkrUvMq9OdZI43q5nIvFLQWdelPLwvd4_bd9EEZauOzD0LTHLc4J5touW7ULb77islSgHaFelz_k73suu4-OaAzLF76d9z5chWxzilKnQguiAlINee4PpvigIppTP_sT4tc-qVj2ef-PvNO_lQYohiRAeqJbiHYhiFouGetVdRVyR8GQsR-nPpFLCx9rYBSbpzok8tCD3VlHEZtj7Ib8136AVeEfgW0CXGMXYXje2VUIPNew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پاکستان؛ مرکز تولید توپ‌های جام جهانی!
روزنامه نیویورک‌پست:
🔹
شهر سیالکوت پاکستان به مرکز اصلی تولید توپ فوتبال در جهان تبدیل شده و حدود ۷۰ درصد توپ‌های فوتبال جهان، از جمله توپ‌های رسمی جام جهانی ۲۰۲۶، در این شهر تولید می‌شود.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658357" target="_blank">📅 10:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658356">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
دو خدمه هندی در حمله آمریکا به یک نفتکش کشته شدند
الجزیره:
🔹
در پی حمله شامگاه سه،شنبه آمریکا به نفتکش «ستبلو» در نزدیکی عمان، دو خدمه هندی کشته و یک نفر مفقود شد.
🔹
آمریکا مدعی شده کشتی حامل نفت ایران بوده و به دستوراتش توجه نکرده است.
🔹
هند در واکنش، کاردار آمریکا را احضار و اعتراض کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/658356" target="_blank">📅 10:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658355">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d06fe35bf.mp4?token=eFXUUg06TNpZly8BMh_hQw2CfRsQlvgV2gv6L3mn7_Y-YtsG_5O79SHLRy5k6AlPRMULx0PZmRYvBBcqhHiXNz1Kh4pfWNPOQbgWwfVj8No_D2yY6t9GxNeqUMCp0W4HNof3BYq0PqdOC5CIHGLkbOkpS4yI3aVEm46NTFqwDfUDC742_UERpWIGJucK20DM6WS6Ml8MZ0kzVUehpxyyNlLjY8tVFQ0bbPGeMAKtfPInKowBI7lsHExzEWnd1nTDebMBP57s2sbzYwk6-_jIaaEjw29LIR76lc8wQUSEBmaj1ZFpeXSjLZgyrltxHhTMKu_-LqHtnTCbwEaWDxEaaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d06fe35bf.mp4?token=eFXUUg06TNpZly8BMh_hQw2CfRsQlvgV2gv6L3mn7_Y-YtsG_5O79SHLRy5k6AlPRMULx0PZmRYvBBcqhHiXNz1Kh4pfWNPOQbgWwfVj8No_D2yY6t9GxNeqUMCp0W4HNof3BYq0PqdOC5CIHGLkbOkpS4yI3aVEm46NTFqwDfUDC742_UERpWIGJucK20DM6WS6Ml8MZ0kzVUehpxyyNlLjY8tVFQ0bbPGeMAKtfPInKowBI7lsHExzEWnd1nTDebMBP57s2sbzYwk6-_jIaaEjw29LIR76lc8wQUSEBmaj1ZFpeXSjLZgyrltxHhTMKu_-LqHtnTCbwEaWDxEaaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️
⚽️
جام جهانی شروع شد؛ وقتشه ردبانکی شی!
❤️‍🔥
اپلیکیشن ردبانک رو نصب کن و با افتتاح حساب، ۱۰۰ هزار تومان هدیه بگیر.
🎁
👥
هر دوستی که دعوت کنی = ۱۰۰ هزار تومان جایزه بیشتر!
🏆
تیم ۱۱ نفره خودتو بساز و بیش از ۱ میلیون تومان هدیه ببر.
⏳
فرصت محدوده!
✉️
عدد ۶ را به 7007666 پیامک کن
📱
یا #6666* را شماره‌گیری کن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/658355" target="_blank">📅 10:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658353">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7510f35165.mp4?token=l1gMPiLOnxecLBezt7fzl3owuKfAKU_AVHADx8i2CogyMae0VeISADJjL1kEaokJVDRX2YyPgPH09TUo3xtD7ioRexnBtmJj-dUxQ_6X9Cuwc3VKftrq_08Mvj0n_zvuSAlPkOPUPI0NiKw_Vk--hHXzsYsy8TGhbi-v2KltiGsailPcjZvYysSUoWH3KVueoEFuaQt9AsqOW0E0GXUR0b4JxTUpRHLtVsVkbcIanv-Ypq4A8rgHDANyHHls0nIZkvQNDf6O6qJUg8kV7yj0cwHn4wVrJtLWVGIMNFOVT5AuEURuTy6Nh9NI3XPNA1aWX5CxED33oDu8wT2ArP5-QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7510f35165.mp4?token=l1gMPiLOnxecLBezt7fzl3owuKfAKU_AVHADx8i2CogyMae0VeISADJjL1kEaokJVDRX2YyPgPH09TUo3xtD7ioRexnBtmJj-dUxQ_6X9Cuwc3VKftrq_08Mvj0n_zvuSAlPkOPUPI0NiKw_Vk--hHXzsYsy8TGhbi-v2KltiGsailPcjZvYysSUoWH3KVueoEFuaQt9AsqOW0E0GXUR0b4JxTUpRHLtVsVkbcIanv-Ypq4A8rgHDANyHHls0nIZkvQNDf6O6qJUg8kV7yj0cwHn4wVrJtLWVGIMNFOVT5AuEURuTy6Nh9NI3XPNA1aWX5CxED33oDu8wT2ArP5-QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلبانی پروژه گردشگری کوشنر در جزیره سازان را متوقف کرد
🔹
دولت آلبانی اجرای پروژه ۴.۷ میلیارد دلاری اقامتگاه لوکس در جزیره سازان به رهبری جرد کوشنر و ایوانکا ترامپ را پس از هشدار اتحادیه اروپا درباره پیامدهای زیست‌محیطی موقتاً متوقف کرد؛ همزمان اعتراضات…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/658353" target="_blank">📅 10:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658352">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6pbNJ7E9p5Uk02NAfb_YMXObWbrwRGFaYIOKqbSQvaVipW4VsD9SIzQtT3W1xdyyyRvRNdq6Tpe5n8Sn-9_wHpjnoX9ngV4NBfMV7Jyg6EhG9krWBMCj8ICvkJirgnF4y4B1zuyXG2OLjXaHuXM5XwBA5xybXqerm9rhcMdJMPTAHkMpu2PfINHBjNCgMxCYejLs78RJsRNjD3N4R_a8Uy_Il8MvOO16MZfiDmK-ijd9c4tls777-5dfyw96q2MF6Igs0Bxf5V-CEoVwMdnpr3l9T3NhwKz2Em7MaksojJDFM5azN8-w2WLAO4BiKxyZJMxcGHkd1oFt2A_PfzG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم‌های جام جهانی فوتبال بر اساس جمعیت کشورشان
🏆
🇺🇸
ایالات متحده آمریکا — ۳۴۲٫۶ میلیون نفر
🇧🇷
برزیل — ۲۲۲٫۶ میلیون نفر
🇲🇽
مکزیک — ۱۳۲٫۸ میلیون نفر
🇨🇩
جمهوری دموکراتیک کنگو — ۱۲۲٫۸ میلیون نفر
🇯🇵
ژاپن — ۱۲۲٫۱ میلیون نفر
🇪🇬
مصر — ۱۱۴٫۴ میلیون نفر
🇮🇷
ایران — ۸۸٫۸ میلیون نفر
🇹🇷
ترکیه — ۸۵٫۱ میلیون نفر
🇩🇪
آلمان — ۸۳٫۹ میلیون نفر
🇫🇷
فرانسه — ۶۸٫۷ میلیون نفر
🇿🇦
آفریقای جنوبی — ۶۱٫۷ میلیون نفر
🏴
انگلستان — ۵۶ میلیون نفر
🇰🇷
کره جنوبی — ۵۱٫۴ میلیون نفر
🇨🇴
کلمبیا — ۵۰٫۱ میلیون نفر
🇩🇿
الجزایر — ۴۸٫۴ میلیون نفر
🇪🇸
اسپانیا — ۴۷٫۴ میلیون نفر
🇦🇷
آرژانتین — ۴۵٫۵ میلیون نفر
🇮🇶
عراق — ۴۳٫۸ میلیون نفر
🇨🇦
کانادا — ۳۹٫۵ میلیون نفر
🇲🇦
مراکش — ۳۸ میلیون نفر
🇸🇦
عربستان سعودی — ۳۷٫۸ میلیون نفر
🇺🇿
ازبکستان — ۳۷٫۵ میلیون نفر
🇬🇭
غنا — ۳۶٫۱ میلیون نفر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658352" target="_blank">📅 10:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658348">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1wTbGUfR_si8GjoHo3Vz212BXfVHfkVlb5mxbm-i72JMrUJBhsFHQ90fCKLUUjugupIa5cD-Sd_LO1G7mrlH_WOAGfGVbegWvCKL1-NhW5RkeM8zqvzBmsneHoKyvJ5B-BXlNixjZr41ODVi5Gg1CYxdvlhG7RQzm9V-cwC49L0R_DXoz4ZyD0lvu3ctzL50PEtTyyko8D999wxqvylrgTo8DNzrywR1-ZjatIs-Y0Mbyr-0PBs8RnRCPeILGPL6zjHmAwwQh_CTrLRObyC_6wVezIT4gxNWwZp-gBJfDS_bLcQFpgAU9-MYFGFU41KGCQhveQSaPC6xbuIasJiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGpsxMaF1V02yaq9nl4riL_eK72yHYsKeFxRbr4nEPsmGILbQpk2B3OlQ68418-yHzdfZEi9E6lWmR-X2WagAxw_d334r0j11XSmGJctbSITBNl4Wr4pgppu_OgfmFGzhHnKEy9QDYJ3okqccLekDOm3eSIw_35faUf4P4TBJbSW7rmq4xniwo4yT160gGENhrE0-nh7fH1XgCOnz3N3sMVw1nUX9i9CZ10Sx6PKYzUNIcpJPEEjj4_rOGtWGpQUygVDtaMJX5u37uAtKzQQmy9qLMbrzu7XFEz8h0jCLXT7WpgD-d3J_SduWp5lxlru5cFXoJ8Eg5WL7QS7ECTQjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AneaNVqV1QrYottvY8CH6B0uEqYc09i1x7056eQNCaBMV1QkcfAqZt9YymkzpUsWzl3AggLYmf_DOZeQc4olbp30bhmaTmJykTEPopNvMKZqfwgvmV-DwiIR8uM3ctXASD2p0tQdZmt48M16liL52tBQ-olngD2oSZx-Q3jsMjwHwfICMZzvGY1uwAbo3k3AocKkKUNYe-LOnPJ9TxHHCo_30zaYj1m4pEqpxODrkDqc6l7qOWvdnsxPOpl861XWqicmMv2fKV9ze0Cv4TlWvli-ftPwBAc7yzONRFsD283iWi_mzjjCjDit9AuIjKibyUYLjWM5PxGEXBqzngNyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hBIBvwdfeSl1QVbJpUh_h9BT2dS7I6f3yf-ZhYi0BH0-NNKIQlNkg8ad4qmuzzc5vMbWhUk9LCEkvWf3yfP4keomTmQbdgz_Xmj4xJ5j2PCcWHzSH96i8f_3BNyb_GiiFr1rSf8i9DrBLNjC_FnnAlF_a_OgvT_33pezTY24ZeMl8sK2onIoY9LU-ddNwnjSkgEyNVzk4BnSHg2nJseem8cJfbJvFv0t3Qm5b5M3Os6eS_4zQbDZJjTRA15JOD-oW0jroUPUQtPO0cj1s_QDzvl5W0fQLY6JMsXI8OfUvU1EGULQeX3nQClk0Vyf6Cgvx24Wlx07cJTngxafUpwJ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا نسبت به آدم هایی که سردن بیشتر وابسته می‌شیم؟؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/658348" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658347">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28d94813d.mp4?token=M69Xz3c5PzqJ_Eca-Wk95RsUtJ8R-0LtirJRyk9wxijhaimuu9NAJNZKAHytPx2IJNCH57yyKFkC0xETz4G7e_gTc9qwMXIZDx4ib2nmfpDaOXQl6J2SoXh072EG6I-nYn_Ev5cAbxXVHKpyYGgEMwK9knLbC9cF2mLrEXoGM64m5Ntas30CBkaFEoUThBho-B-mCmiVoFtgcXdqeMImtcKVmcrlmsPPWoseogz4aDSyWn39Dm6s07bVXkaWkhX0adN3xKlM-Psuco0y5CIZthTPuxJF0Vr95hUL85p6e-S-krRCEUev-ags0FNDTrKCvtU2-ebwgQcFWzesTPZRwjArkI_ul377jNnfxPjB-WVQWSdNQUd_D7Mxs3EaiLuFLan424nJwGZk-9nxhHxH9mO1K_KTmgy05diX2Z6t8Yo18sOkORQXNwx-JjlO15MJQMhKWw-Q_SgAdbu-nArvT7hKK6TikAa83-rkSUD90vg0eXEti0J5mhmUXAMhAI_JR5tNCO5f8pwV5dsy48nehLJvYnh6Ck57wFGGrtRLPa_V35RzGrft_jTN2UpbPz2ZXYWwooyzpPx86Gp7IkBr7VAesvGNKW-9XmZxg_I0nCRgCAb_NVlLB3RDVa5KbyxUGF2YFiOldLrcbEvoS6DndpBu7vaawUpARUVZHOcPImY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28d94813d.mp4?token=M69Xz3c5PzqJ_Eca-Wk95RsUtJ8R-0LtirJRyk9wxijhaimuu9NAJNZKAHytPx2IJNCH57yyKFkC0xETz4G7e_gTc9qwMXIZDx4ib2nmfpDaOXQl6J2SoXh072EG6I-nYn_Ev5cAbxXVHKpyYGgEMwK9knLbC9cF2mLrEXoGM64m5Ntas30CBkaFEoUThBho-B-mCmiVoFtgcXdqeMImtcKVmcrlmsPPWoseogz4aDSyWn39Dm6s07bVXkaWkhX0adN3xKlM-Psuco0y5CIZthTPuxJF0Vr95hUL85p6e-S-krRCEUev-ags0FNDTrKCvtU2-ebwgQcFWzesTPZRwjArkI_ul377jNnfxPjB-WVQWSdNQUd_D7Mxs3EaiLuFLan424nJwGZk-9nxhHxH9mO1K_KTmgy05diX2Z6t8Yo18sOkORQXNwx-JjlO15MJQMhKWw-Q_SgAdbu-nArvT7hKK6TikAa83-rkSUD90vg0eXEti0J5mhmUXAMhAI_JR5tNCO5f8pwV5dsy48nehLJvYnh6Ck57wFGGrtRLPa_V35RzGrft_jTN2UpbPz2ZXYWwooyzpPx86Gp7IkBr7VAesvGNKW-9XmZxg_I0nCRgCAb_NVlLB3RDVa5KbyxUGF2YFiOldLrcbEvoS6DndpBu7vaawUpARUVZHOcPImY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون: چه بخواهیم چه نخواهیم، ایران به طور منحصر به فردی در کنار فلسطینی‌ها و مردم لبنان ایستاده است
🔹
بقیه جهان با وحشت این را تماشا می‌کنند و هیچ کس دیگری کاری در مورد آن انجام نمی‌دهد.
🔹
با وجود داشتن آن ارتش، با وجود ناوهای هواپیمابری که از ابتدا تا انتها ۱۲۰ میلیارد دلار برای به آب انداختن آنها هزینه شده است، ارتش آمریکا نتوانسته است آن تنگه را برای حمل‌ونقل به سایر نقاط جهان و کالاهای جهانی در ماه‌های اخیر باز کند و هیچ تضمینی وجود ندارد که ما بتوانیم این کار را انجام دهیم. بنابراین ما قبل از هر چیز محدودیت‌های قدرت نظامی آمریکا را آموخته‌ایم.
🔹
کارهایی وجود دارد که ما نمی‌توانیم انجام دهیم. جنگ ایران به ما آموخته است که در واقع در مورد مسائل بزرگ، افرادی که شما انتخاب می‌کنید حتی مسئول نیستند. شخص دیگری مسئول است. در این مورد، بنیامین نتانیاهو.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658347" target="_blank">📅 10:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658346">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5ib-dH_6abGdi1y1lAmOH5Srite0kHYdhRd5chI6g_gRyCIv8QTtiAERVhOvNfW_Dgzm3M3QinByfFSBB3B-hPr1d4dYeGzhQUIpX21HE7h27-DFMTihryE-PC-tfUvmYOb2TZ6BUNfLimiyVDg1XzMS1SuAg9UmIkSVKDHkeS6ECslZZH8FhT6ajAQV7GvDaJ-XBrUPkbRqRiyXXLnsbTGLozwE-9BAXaRJX-jkuxvXJgyS4r-p-HHrZHGYT-VtgSh_Do8acw8w4VhYdf5Ebdw1Vmen4RA6N3g6LmJJGQVZPMd4AdscH7iUd93ZhMnsl5KUXhQ3MCoORt5IYU7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👠
استایل تابستونت با mono کامل می‌شه!
‼️
تا ۷۰٪ تخفیف بر روی کیف، صندل، کفش، اکسسوری و البسه زنانه و مردانه چرم
💳
پرداخت اقساطی با اسنپ پی در خرید آنلاین
💳
پرداخت اقساطی با اسنپ پی، دیجی پی و زرین پلاس در خرید حضوری
🆔
@monofashion_co
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/658346" target="_blank">📅 10:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSw1VleBlciEoBO-nZShsI2SgEXytda8W0Ox4y-GmAlF4t0UlZJQ5T8fmTXpYH4R14JVvL9o06Al5ZTD-X90DPUQorsCrhj6mzAlZO1E5IVDQELGaabs-8_FUphgfbWcKNbEm0KXLTuMyH2X0YIWjcIT604ua5K3xKSpAv5WxA7USr_YQnS3P-YzVWgV9OZDshtsh__r8DrgR4eCtTN84fR0btRXDiabYP5pNv_9VC7qAtOEUFm_IixFYimUEX1GGbg8wXnm8ccKCXfX1fs-Xfuzv9UY0llIA2ajb2xWRoPE3IprZSFDPGx4LxFiIBw7Ro7NnJXFTKEKJO4iPzqD3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
جام جهانی ۲۰۲۶ از همین حالا در «همراه من» شروع شده!
برو توی اپلیکیشن
«همراه من»
، بازی‌ها رو پیش‌بینی کن و جوایز هیجان انگیز ببر
🤩
🎁
۵ گیگ اینترنت رایگان بدون قرعه کشی
🎮
هر روز یک  PS5
💵
۱ میلیارد تومان اعتبار کیف پول در روزهای مسابقه
📱
قرعه‌کشی بزرگ S26 Ultra به همراه سیم‌کارت ۰۹۱۲ برای سه نفر برتر
✨
3 کمک هزینه سفر به عتبات عالیات در هر بازی تیم ملی
پیش‌بینی از تو، جوایز میلیاردی از همراه اول!
🔗
https://www.mci.ir/-9VEQ3HH</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658345" target="_blank">📅 10:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUqO5FjzMr2OL0q72YUwXvf2fL4_KyQLWdxZyaOrqiBaaSFaOstvDNZvDyGFuTtuWkiVdriCkedub050A6GUIhrmBUKErLvBjO9SALqNDUz2uBDJCrvuOGztdk5r3spLilrGJLMHEmWz9aHZW-fwYeRqmHrKeOaKyjtCRBzxqABIlIjKWxj88E0cSSZqXIUfo3Y8roQtFh2oCvavn2-aeHhjTH6B18O-42fERErkJI3xzLZaiuZaCxYhsE3r1WaOFyVLBl-_kSsLnz0KKZADF3GCB8LPZsOkQMTRODPjGJNswqrhYN9gfhjlz6ZChiMLAGCjvgwoKils-vbNfJ7AMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهاجرانی: با تکیه بر توان فرزندان این سرزمین، ایران استوار خواهد ماند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/658344" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
سپاه: ۱۸ هدف مهم متعلق به ارتش شرور امریکا طی دو موج عملیاتی مورد اصابت قرار گرفتند./ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/658343" target="_blank">📅 09:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYzt_TW59oXWR8F63nEwe2InsoDdiJQ11Ec8eMFrMZGPX5-dPDgBIw_Np_vEUup2qlxaklUh1vEwviyDLs2oeoMzXrMwuPbpGlbQE69UG9qDx1CZrX5bykHPtTwLpikkfjWguQaRHR9-JvpnSbGJDvkLYh76FO5SMy_XpUBAaMe09iRNuq-CAayV02eBaXqxg-kmKicJEVTju8Iv6a2bDUSyib4b1x-DD1MnNaciezddlK5rFq4gvANtyCnNOl8WgbeTtQWT31hkD9Wm5C3vCaIEkmXVQklsoAzthoF_vrf-S__1UuOpJpBl2L7wsjw4VV_8wG44FeYZfCkaAqg04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جلد روزنامه اسپانیایی مارکا و استقبال جالب از جام جهانی با تیتر «ما متحد هستیم»
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/658342" target="_blank">📅 09:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNiHDsDcVNXHmnijcnJ8rhC0yWRFI4xCxmdoc7u0ok803pG8YpBPHsQgN00eolMfpc5kJWTaI4fak3_fJCFyKlOXRwcBJBiZhsSriTSlRYnTxgWOYiuyX21VCLBgamBNr9LUk6DvXVR312vySpTX_bfYeEJoe310DW-6aKp1_8_NLpMgXS9N5j588LTtMDIapXHKpQ8jBHuntkzhGie0UYNbNbad6p3b9I-i9PGAgk-yr5VMgHrd5b482yVBlHRoAv4jHwtrH9ZauvBZ4Ayxb0T405iu4TXCuB5oit9VLcsoA2JFKj2lop2XfIA_nSMBzRm1bu-i_2pdTXRGooy_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان نیویورک تایمز به احتمال جنایت جنگی جدید آمریکا در ایران
روزنامه نیویورک تایمز:
🔹
براساس تصاویر ماهواره‌ای، حمله آمریکا به یک تأسیسات آبی در ایران انجام شده، اما مشخص نیست هدف‌گیری عمدی بوده یا نه.
🔹
اگر زیرساخت غیرنظامی عمداً هدف قرار گرفته باشد، ممکن است مصداق جنایت جنگی باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/658341" target="_blank">📅 09:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658340">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpKA-td5yXbageXR7NS8HqiDtBFhevkYiER0ymQPtTj5A7yBGp6mJsgPuwEMurKZLMlrkiS21VE_6-zp51QljaK--5PsKOEE1sx9bys1wcnAcYc2zhXw_t4VF5DIJ1pgMRvUDKQopmoUuQ_hWQZzyoA98YiSS1phgT_x6snyV_7Ap48oqcmA_OLKOf-G5qrF4lSsWDW1qsdGq2Lo7xJApiUblTa83C-Iul-NVI7wI5-NyurVnev4JrROghpJyBBqXTdFO5L69eA70asGS1448o0wqaT0D_6O3-BGWyZoDS0WAl3Yj7aGwwwbRzb_mCFpJ0Eo6xS-X9gPON3l_9mCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت ژورنال:
علیرغم صدور مجوز حملات جدید به ایران، ترامپ دیپلماسی را رها نکرده است
🔹
مقامات آمریکایی می‌گویند که او در حالی که همچنان به دنبال توافق هسته‌ای با تهران است، از فشار نظامی برای وادار کردن ایران به امتیازدهی استفاده می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/658340" target="_blank">📅 09:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658337">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ac068b03.mp4?token=fcOUeXFuxsl5ty83M3rYBp8s0CyoP7IzxtdF83u-c4ir9lYd1GpFr1yLaLHD2ze-dAqZdH0TFgIprA4A6QAt5SPPzebM3ZHpuJrRhF-qArBRoCegbXTytLoL_SMbDZ9XLoHDJTLguFusn32fBbUu4LV70TEKFKVNUhzDIvr0cgcL7SjwbchMPYpd9iyHRozGLxhXZqNYWaGpkanjbxihsSZvwmHIiCIRGY2AZ1gtrQPOuhtB1Iq9vGGxx7YaojyPI6K_oyM2BOUuGt55taaS23igF7uAfbPEd_lrhvCUU6FLoUqWAtHqn0-kMeor6_jEr_seV6AD5CBg0oUU8iGaCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ac068b03.mp4?token=fcOUeXFuxsl5ty83M3rYBp8s0CyoP7IzxtdF83u-c4ir9lYd1GpFr1yLaLHD2ze-dAqZdH0TFgIprA4A6QAt5SPPzebM3ZHpuJrRhF-qArBRoCegbXTytLoL_SMbDZ9XLoHDJTLguFusn32fBbUu4LV70TEKFKVNUhzDIvr0cgcL7SjwbchMPYpd9iyHRozGLxhXZqNYWaGpkanjbxihsSZvwmHIiCIRGY2AZ1gtrQPOuhtB1Iq9vGGxx7YaojyPI6K_oyM2BOUuGt55taaS23igF7uAfbPEd_lrhvCUU6FLoUqWAtHqn0-kMeor6_jEr_seV6AD5CBg0oUU8iGaCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر بیشتری از پرتاب موشک ایران به سمت اهداف دشمن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/658337" target="_blank">📅 09:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658336">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b50b401f4.mp4?token=bSjQhQ0EGjHh_dgSrK1mZKStOhAACuc5eKOgyKoUSXiQDcd-VV5-C_TG6t837hmf7KGh8pSi8NbVVdre8X2230jD2rDCF7zYmvM_KwXneHEanMtdqX6r1-fB12vDdsLUnV50c_0hYgVobIZJbNDRJbicF7-XjcGPkPr2H6c_RHOUxNzuXyzM7q7eOC0AEl0YXAi1LBECjcdr6pTMcgauWLCTZOZBjIsVWQJeUWexDAuHmFQHuwzReE5cfuPp_JrDHE-XWE56f-MHE7D99JHkhIQbYgJlzjwZYSh3WBHRfZ93D7yUFf8KNXDJ-Nitwg6mE1CCODYX2adm7OjJdNulvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b50b401f4.mp4?token=bSjQhQ0EGjHh_dgSrK1mZKStOhAACuc5eKOgyKoUSXiQDcd-VV5-C_TG6t837hmf7KGh8pSi8NbVVdre8X2230jD2rDCF7zYmvM_KwXneHEanMtdqX6r1-fB12vDdsLUnV50c_0hYgVobIZJbNDRJbicF7-XjcGPkPr2H6c_RHOUxNzuXyzM7q7eOC0AEl0YXAi1LBECjcdr6pTMcgauWLCTZOZBjIsVWQJeUWexDAuHmFQHuwzReE5cfuPp_JrDHE-XWE56f-MHE7D99JHkhIQbYgJlzjwZYSh3WBHRfZ93D7yUFf8KNXDJ-Nitwg6mE1CCODYX2adm7OjJdNulvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز داشتن یه کوکی شکلاتی نرم و کافه‌ای!
🔹
توی این ویدیو طرز تهیه یه کوکی شکلاتی عالی رو بهت نشون میدم که دقیقاً مثل کوکی‌های کافه‌ایه! ️
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/658336" target="_blank">📅 09:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658335">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djWLoO4rAq6BH9NAn-ZuWKRzLGxnMcx1WLtU2YXIQUjlXWtfxILms3LZ6B6HipiAKDjIODenqcnQIdFrH3EoYdul1zVcU85Y85DxBMne7r_bzAwb7xXVpI5x267aI6s8celaiLLmt7HKz57gCRnkBp9B1DHxJO-1st9yPmen1l2762CRAxV0jaizEyN2u4A92DZF3bfyEKseKijOxlXaYcxH4W8dLziR7_kdoIkFayeT38niezovfc2RHte0NPOyQDCAU2dGM2glVhcgyfPamhjUVED7h02xyrqUgsTdHTieDKa9Ef_5wWCyiohvThtgdk_2in_bp_01dtTeOIurJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس قوه قضاییه: مشکلِ سردمداران آمریکایی آن است که هنوز مفهوم غیرت و حمیّت ایرانی را درک نکرده‌اند/ اکنون که پیش‌روی ما، ماه محرم، ماه پیروزی خون بر شمشیر است، بیش از پیش برای صف‌آرایی در برابر یزدیان زمان آماده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/658335" target="_blank">📅 09:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658334">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51e8cc2456.mp4?token=GSmFZ61A80j6622-QR-raMDYuDV-so7EP64y38qyNK6FC8-ekbbZ5QLk74bdNDZ4bFoW_30xmvRyoPgRYf0fDkSGSN4SnlfRA_r-rGV0Ht9YZFvmxsQ0RgrGz2P_vneL5MIhOTupNCSzD-RxnEucBtYeuB2YS_M0YaKeMDVcH6O27I2w7s38oWTZm3A8ce5Z2SARQKyn9aYVURk8Jnx3w1MzmcQ54-axHwN19geU_AmEGcHHx7LsD_UA42fca7_w4PYvIrf8WEBBdh6P6Xc31J9_WnCkZmWJViH4dTfrw54wX4biZpMYfxoQB2Faqf89yXyJVroX3YOq8n_Z8B337A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51e8cc2456.mp4?token=GSmFZ61A80j6622-QR-raMDYuDV-so7EP64y38qyNK6FC8-ekbbZ5QLk74bdNDZ4bFoW_30xmvRyoPgRYf0fDkSGSN4SnlfRA_r-rGV0Ht9YZFvmxsQ0RgrGz2P_vneL5MIhOTupNCSzD-RxnEucBtYeuB2YS_M0YaKeMDVcH6O27I2w7s38oWTZm3A8ce5Z2SARQKyn9aYVURk8Jnx3w1MzmcQ54-axHwN19geU_AmEGcHHx7LsD_UA42fca7_w4PYvIrf8WEBBdh6P6Xc31J9_WnCkZmWJViH4dTfrw54wX4biZpMYfxoQB2Faqf89yXyJVroX3YOq8n_Z8B337A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی وایرال شده از مقایسه استقبال دو میزبان جام‌جهانی، آمریکا و مکزیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/658334" target="_blank">📅 09:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658332">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvocYEEXbpSR06uPHX4A4IQBsBZKdsEn5swhGzGeMyx08JhwuXi1rJgBz13J1dONzMoGte5gGONM4Fbc1LliBaB06H-yjP9y0uJ7Yg4KJCKSZY8GtRQ4cxXyrUwkMqxoiBhMTsp1-QupBu2qn25OdZrxCqLoAUoPFgvBNVrjSD-LuZvekYkd-5LtzcT53MGn74daLlk6D0eCTe8LlVc33YNfLrLEifNhNgCDq_Aolk4dI_2RSVfJpWWsAJVzg5MPIvT4oNeXmu7GUItPbleFWX5paQnKPR-qDkzAGEx_A9QN1NRyqcMTh_UNKDLpKvkEnZR865cSw-YdeFi_lj7GPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تاوان همکاری با شیطان
🔹
تصاویر ناسا از وقوع آتش‌سوزی در نزدیکی پایگاه هوایی عیسی بحرین پس از پاسخ موشکی ایران به تجاوزکاری آمریکا حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/658332" target="_blank">📅 08:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658331">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2c2a641fc.mp4?token=qlXlANktGnEEiOX9ME6r3gHFz7h6x_KNxsI01vF_L7OkOwid5fNXpzUgFT4flccmGCO_9AOFxuvCkknVwDgIEP296Qg5SO_z4bAr3wzXWGbNHSFMRGhL22FhFN4jj1gRd6ZVpyztXCyY_ZokRwYbQmTDMoHNiyV3x2Y4NqE_dzN4l-dEAYESUgNoSXxlspWtANbOfzz5_FB-4qB0wEKo8DLBV_j_zdAnpMe__f54t1Ri_ra7i-5qOxQOUeleZEc5RTuyYBLGBslhv3eBjPijnWZ23r2N-FI5m1eLNCCtsod9gB-gG5SsJJ_1biXubLyzH4PGWV7j1Y-FkR9xE9gacw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2c2a641fc.mp4?token=qlXlANktGnEEiOX9ME6r3gHFz7h6x_KNxsI01vF_L7OkOwid5fNXpzUgFT4flccmGCO_9AOFxuvCkknVwDgIEP296Qg5SO_z4bAr3wzXWGbNHSFMRGhL22FhFN4jj1gRd6ZVpyztXCyY_ZokRwYbQmTDMoHNiyV3x2Y4NqE_dzN4l-dEAYESUgNoSXxlspWtANbOfzz5_FB-4qB0wEKo8DLBV_j_zdAnpMe__f54t1Ri_ra7i-5qOxQOUeleZEc5RTuyYBLGBslhv3eBjPijnWZ23r2N-FI5m1eLNCCtsod9gB-gG5SsJJ_1biXubLyzH4PGWV7j1Y-FkR9xE9gacw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دقایقی پیش انفجار در نزدیکی سفارت آمریکا در بغداد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/658331" target="_blank">📅 08:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658327">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzqR0L-g2xjlX2-uLZp9P89P2F0imAnYPkjKPgsLsvisow5FmSOfbLFjDDvX72RRhR22je4s-H-5UBldFaFu1qoCr_P-W-YAQb5QQPBBzhOSwFgjhu6Z33kpKy4V3nojj1I3Wjtpl80mhkbkldQfnN8HirQe9J905y4EuDtX8pDQc3QD_jxHOAjctyPM6b5Ut0uP1pQEdBn_CEDlXywrlBFokFJagvFAtXNUdsdaErOe3C6ObtEBzMwlzbnS7vG2RrRJMXC4UfbXWLM2vfLlvVWIME23cDTMHA6XYfO3kN3Ykxy8Gm87aGrkvzEGg4vGwARQerFKrBj1X7mXi0lc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارشناس آمریکایی: اگر محاصره دریایی و اسکورت کشتی‌ها توسط آمریکا مؤثر بوده و زمان به نفع واشنگتن است، چرا باید ریسک بازگشت به جنگ را بپذیریم؟!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/658327" target="_blank">📅 08:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658325">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9011bfe3f.mp4?token=usz5nzLnYQWyPt8oexnzZTzG3BAYeOAKJ5er9E6uw1o-Dqaiv0mRpiCityeg86Csebw16cCMp5ZJKo52anjSsAOjxO9itEcTMZmg1b2wm8XkBsBOy9ep_73l6sRnE5T-CyRXAC8wne1fAy4r33n_U8FePNmZYpI808H3KRtyXrCYUzlQe4UdyZ4sRimofkeB4oqoBXOyals8jOMHoyAudh8uJLr5b-DJJZWagPynHAObtP3TvsI92kpqG_BMUqS9bkkNgLOoCokg7oJiA8Go7_yceeBpEDzC7U3F8l81Sl3g5b-x08jGw-hbt_hPe23Dd5BeOc3V0iFhhJipqE3Q7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9011bfe3f.mp4?token=usz5nzLnYQWyPt8oexnzZTzG3BAYeOAKJ5er9E6uw1o-Dqaiv0mRpiCityeg86Csebw16cCMp5ZJKo52anjSsAOjxO9itEcTMZmg1b2wm8XkBsBOy9ep_73l6sRnE5T-CyRXAC8wne1fAy4r33n_U8FePNmZYpI808H3KRtyXrCYUzlQe4UdyZ4sRimofkeB4oqoBXOyals8jOMHoyAudh8uJLr5b-DJJZWagPynHAObtP3TvsI92kpqG_BMUqS9bkkNgLOoCokg7oJiA8Go7_yceeBpEDzC7U3F8l81Sl3g5b-x08jGw-hbt_hPe23Dd5BeOc3V0iFhhJipqE3Q7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرینات منتخب برای قسمت های زانو، لگن و کمر با استفاده از توپ سویسبال یا جیم بال #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/658325" target="_blank">📅 08:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
محکومیت ۲ دوومیدانی کار تیم ملی بخاطر تعرض به دختر کره ای در هتل / ۲نفر کاملا تبرئه ۲ نفر محکوم به حبس
🔹
حکم دادگاه کره‌جنوبی در خصوص چهار دوومیدانی‌کار ایرانی اعلام شد؛ دو نفر تبرئه شدند و دو نفر دیگر به حبس محکوم شدند. این حکم هنوز قطعی نیست و قابل…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/658324" target="_blank">📅 07:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mb8hY90jWRQqrNtsd8GxBbRYhQXo_Qf0Yxh7bOwjO8D2M35Lsb1lXWVFTwij8suALv_vle1l4Xp0d_gfJ9tFtju4rJdwo1oKOaxJt4e-f-2zjXC97IfKv4GUUWfNFNYNekvNQzCaHFm6ObgKUvjqeIiwZ1sF23J35h-LZl4hSeZleo1BKi1htr68Uj35PxLKyYnO02dpzdcPbMqXk7MWxZALqbDfYtTcz1hNi_MywkfXsQcwWZwVZtuGxJWid8ggKc6TNzjoS-W02yZrBl-plfqntvZ128RR4Wg0AuNmbgK700SUa20imImJQbVyUyFE6CtJ5D9uG9ngeFGQyBXXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محققان چینی: چای برای سلامتی مفید است اما نحوه نوشیدن آن اهمیت زیادی دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/658323" target="_blank">📅 07:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658321">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhC7JOUwqcw26L_0S6U8fzM3IcZD1jarW1fRn2tLW0knlt5Szk5NSMD1DHMD8L2QN03rhjMFnlD7fwxkuWswsfd0JH8arijKxi56vV-RwJbeETPJ3XZTmvKAbkAWGiNnqJbjA9qobQqAr1LPb3Q2taHdBayVv-IjNUFI2zunrfia_MWMlroQsXUlORTVc3xWZVacUvm3ieJejug-crO5QJPPLvi-q-jg-jl_JuZnQ40B5UeAZYGL0In48rbiMDHB_-eQOpTvb9ocMqmzW6XKC4OxTVG3uLYvfsJwVsoekQbH1G4UUVHIn1IfsE2N-PVJ7PIkj2u92Qp6-ji-pCp44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۱ خرداد ماه
۲۵ ذی‌الحجة ۱۴۴۷
۱۱ ژوئن ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/658321" target="_blank">📅 07:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658320">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
هنرستانی‌ها باید از شنبه به مدرسه بروند
🔹
آموزش‌وپرورش از فعال‌سازی کارگاه‌های هنرستان‌ها با هدف آموزش پودمان‌های جامانده دروس کارگاهی از ۲۳ خرداد ۱۴۰۵ خبر داد.
🔹
قرار است فرایند آموزش پودمان‌ها ترجیحاً ظرف دوهفته آموزشی به پایان برسد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/658320" target="_blank">📅 07:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658317">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkUOvkUTlIJE6Aiytd2CeBC0ERLcunat_cu2K1JoiuWtXymRq6eYvtogWl8moHdEzNktKOmpnXrcK8uF4DO03YgFuU5Ouulfl9_ayqCLTM4Z88KVQpAMgX9iYV8DGWJJJzIH5m7bsuX61k6wcSxxHkAn0m59VlQki83RAx6L3FMYQ1evA_bxkQi_4UQiJM5kuwUjtQ2wlwX7avzYHz98vCGWO5HsJ91YJ-GTxLkQ_fuO47X4TsccUDn5dDYUIeQtgsXRR19kEIMcTtiZIijesh7LOQD3jj1FbE7UFBcUgzIenB1HB9PoCht48pWXtzYEnnKJoQ-PcalARMgdq9diqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرگردانی هواپیماها به مقصد کویت به دلیل حملات موشکی سپاه در آسمان این کشور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/658317" target="_blank">📅 06:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658315">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924506c361.mp4?token=RkenmvkYOFFLNpNJsPN2EnalmsWnYt3m4RZFMfRQT9wmhjuz3al2pfkYwdF2mdj6vdfzsrxFPnfVl1C3XEjDX0ErXfhfrooWKR-ZxgtIszS8rQ4BDXvVo5JO65eVGWQ-Utol6ucQep3XxaNg2qGtmiHMdxqHrbREak5zqBJ9X5-wJnS_u3Xe9aZ4SXC0aQ4cIx9t8AGm-fGkEwjVN6btePaMNgOba8JBqafOcs8zNocxaLWPL9YgD8cPurkfZ156fUpZPpz4VePV7OCcGR-oIAHXwSLBJYHmvqYw7NPjIbhuIlFSuX5cWM6O81V5DDOXISNi_tPzOZ3fuc5D9p1p0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924506c361.mp4?token=RkenmvkYOFFLNpNJsPN2EnalmsWnYt3m4RZFMfRQT9wmhjuz3al2pfkYwdF2mdj6vdfzsrxFPnfVl1C3XEjDX0ErXfhfrooWKR-ZxgtIszS8rQ4BDXvVo5JO65eVGWQ-Utol6ucQep3XxaNg2qGtmiHMdxqHrbREak5zqBJ9X5-wJnS_u3Xe9aZ4SXC0aQ4cIx9t8AGm-fGkEwjVN6btePaMNgOba8JBqafOcs8zNocxaLWPL9YgD8cPurkfZ156fUpZPpz4VePV7OCcGR-oIAHXwSLBJYHmvqYw7NPjIbhuIlFSuX5cWM6O81V5DDOXISNi_tPzOZ3fuc5D9p1p0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادهای شاهد ۱۳۶ حیدریه در آسمان کویت به سمت پایگاه‌های آمریکایی در حال حرکت هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/658315" target="_blank">📅 06:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658314">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
محل استقرار جنگنده های F۳۵، F۱۵، F۱۶ آمریکایی منهدم شد
سپاه پاسداران انقلاب اسلامی:
🔹
در پاسخ به حملات آمریکا، با شلیک ۱۲ موشک بالستیک پایگاه هوایی الازرق و محل استقرار جنگنده‌های F-۳۵، F-۱۵ و F-۱۶ آمریکا را هدف قرار داده و بخشی از تأسیسات و تعدادی از جنگنده‌ها منهدم شدند.
🔹
عملیات تا زمان ادامه اقدامات دشمن ادامه خواهد داشت.
و ماالنصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/658314" target="_blank">📅 06:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658312">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در کویت، بحرین و اردن
🔹
منابع عربی می‌گویند که پایگاه‌های ارتش آمریکا در کویت، بحرین و اردن مجددا هدف عملیات موشکی و پهپادی ایران قرار گرفته‌اند.
🔹
همزمان با وقوع انفجارهای جدید در بحرین، ستون‌هایی از دود در منامه، پایتخت این کشور به هوا برخاسته است.
🔹
همچنین گفته می‌شود که آسمان کویت بسته شده و پروازهای فرودگاه کویت به فرودگاه‌های جایگزین منتقل شده‌اند.
🔹
ویدئوهای منتشرشده در شبکه‌های اجتماعی نشان می‌دهد پدافند آمریکا در اردن در دفع حملات موشکی ایران به پایگاه‌های «الازرق» و «موفق السلطی» ناکام مانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/658312" target="_blank">📅 06:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658311">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed62bd9527.mp4?token=vSU5zIeLEJOn5c8JvulA3xcUsXDC9uwzkviD0Lep0TCoweu1rnyvVlGouH4n9V64brUbjJZyKbpLbarlsY5ilKzefC0UzdxKn8aAJjolUjmT_Ywuq7RTaFaq-W1arwY70SHq9ve7qtxW-f1SkBe5Rxp9wmx7rr4u6Q3lfIjQZOrmfBLfBwFnbW9_zEBvfAm4tIFQHhJnlc7x5Dh5N76MiwEp26OHrPBVwBczSisCdopN1t0b3GtW1Ghj9fGyOQFlM8zIqvXfLXocSAMhHKgjKIH9kC99VNoq2azl8FVdWiFgoj5jI7-EhWyn1VZl4nr8V3EQslnoio8UgYCF_1zpYxPkS8Iq94jhmSubDgTst4FMAUgxBMP2vtSCV9G1a76TYXoqjc9IAPc2NHcC2z4vQyl3n9lTX90RSGXBjL3M9UX-Ldo2CnRjFBKsmwAQ_CrBk-3b11GPMzjUJEOB0Lq7Ys_UdPnn9V4gpvl5q4UREJZo70xQ0xq7GSMEhecxzjTqPu-IwY1HW0O5pc5Sz2x95xplY02wWDHYkyo4FkQclOH2zCI9aReke_oJ767o2_2q61zc0mDBqg4sbrBhMTdO6dRPGWcmUBFlatTTSI4HUcmswx5ug-GZ8nrnnfIMtJoEmgWRAbaV7Yq7LQyOm5S9hPOFJOTBTIaDAgDOJ5szv38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed62bd9527.mp4?token=vSU5zIeLEJOn5c8JvulA3xcUsXDC9uwzkviD0Lep0TCoweu1rnyvVlGouH4n9V64brUbjJZyKbpLbarlsY5ilKzefC0UzdxKn8aAJjolUjmT_Ywuq7RTaFaq-W1arwY70SHq9ve7qtxW-f1SkBe5Rxp9wmx7rr4u6Q3lfIjQZOrmfBLfBwFnbW9_zEBvfAm4tIFQHhJnlc7x5Dh5N76MiwEp26OHrPBVwBczSisCdopN1t0b3GtW1Ghj9fGyOQFlM8zIqvXfLXocSAMhHKgjKIH9kC99VNoq2azl8FVdWiFgoj5jI7-EhWyn1VZl4nr8V3EQslnoio8UgYCF_1zpYxPkS8Iq94jhmSubDgTst4FMAUgxBMP2vtSCV9G1a76TYXoqjc9IAPc2NHcC2z4vQyl3n9lTX90RSGXBjL3M9UX-Ldo2CnRjFBKsmwAQ_CrBk-3b11GPMzjUJEOB0Lq7Ys_UdPnn9V4gpvl5q4UREJZo70xQ0xq7GSMEhecxzjTqPu-IwY1HW0O5pc5Sz2x95xplY02wWDHYkyo4FkQclOH2zCI9aReke_oJ767o2_2q61zc0mDBqg4sbrBhMTdO6dRPGWcmUBFlatTTSI4HUcmswx5ug-GZ8nrnnfIMtJoEmgWRAbaV7Yq7LQyOm5S9hPOFJOTBTIaDAgDOJ5szv38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه عبور موشک ایرانی از سد چندین موشک پدافندی در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/658311" target="_blank">📅 06:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658308">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
انفجار در پایگاه‌های آمریکایی در کویت و بحرین
🔹
منابع رسانه‌ای از وقوع انفجارهایی در پایگاه‌های تروریستی آمریکا در کویت و بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/658308" target="_blank">📅 05:28 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
