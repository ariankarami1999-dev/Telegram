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
<img src="https://cdn4.telesco.pe/file/ceML0zhtlD_dDClh53uFW7cgMw6-_RudnrZLzcInUCmVt9F_tNUuuqkHlyntAD5mOpn5it87DxDuT4xQC-Dyyf_U7_L0g1LjZemaM-r-UEqZKNOgB3-fESs8wXk0M_QXzbrCRufJPvPk7dZ6319wVb5MAVp2t-OUSkrnvCQCy7KMg8yozWvQ00Tq1tpexL3EBdYHBcPuUg4c0Zcq_D3BDQa-J6Nn09TwBrAFcl7wPRHQD0BdGf9vfb7wsYNOSV6USJVH7Bvp-Ow6831c7kT3ssV3hGTerkvhIo0swPSfpOF5EzOrulCPMS_x1-kwhFAYyOUpO-VShDG5ck2hmZe1Ww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 00:16:33</div>
<hr>

<div class="tg-post" id="msg-139787">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
✔️
✔️
✔️
✔️
فرهیختگان: دنیل گرا طی ۶ هفته که حتی یک ثانیه بازی نکرده ۳۳ میلیارد تومان پول گرفته!
😐
عجیب اما واقعی: دنیل گرا بدون یک دقیقه بازی برای پرسپولیس در این فصل، ۵۲۷۸۰۶ ریال قطر، حدود ۱۴۵ هزار دلار و یعنی ۳۳ میلیارد تومان پول گرفته است!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SorkhTimes/139787" target="_blank">📅 23:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139786">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
شرط سنگین گرا برای جدایی از پرسپولیس
✔️
✔️
شنیده‌ها حاکی از آن است که تارتار نگاه مثبتی به استفاده از این بازیکن در ترکیب تیمش ندارد و همین مسئله بار دیگر بحث جدایی گرا از پرسپولیس را مطرح کرده است.
✔️
✔️
دراین‌بین گرا برای جدایی از پرسپولیس خواهان دریافت…</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SorkhTimes/139786" target="_blank">📅 23:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139785">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
بازی رئال مادرید و اینتر هم شروع شده که رئال  دو گل زده تو سی دقیقه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/139785" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139784">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
اگه اینترنت‌تون امروز بیش از حد ضعیف شده؛
✔️
طبق اعلام مدیرعامل شرکت ارتباطات، دلیلش اینه که فیبرنوری تو ارمنستان
🇦🇲
قطع شده و دارن فعلا پیگیری میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/139784" target="_blank">📅 22:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139783">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXUFnqnNnHxJJGCA58yXSDjB9YDU3nj-wHn7gnB6tVstOe-2sSz9zoyCAlwBNnSLvdH4KjKe2pdVyrwoxDG0x0hruOz9tYcw3XAjIuxJ01xXpkCeKSsG-2MeXMQR4VRVeBh38bdaTxLWFs31Ipabv1oHxMwmhZCBtFHnBrb-hcSXb5u2ka4YRvdSN4Rog3lS_R-1qKJ_hgoOtbhD32yDRQuDDENvK8RTOXgnAsVLpny_eo87izeeDFJ8kv5tfIAvUzircP1ABCRPGNFilEfGHJaYdnst56NlX9qN035y6Z438Mx_82cucLW0xAdG5ikd05fn6LxrmoMMNBgisNCL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه اینترنت‌تون امروز بیش از حد ضعیف شده؛
✔️
طبق اعلام مدیرعامل شرکت ارتباطات، دلیلش اینه که فیبرنوری تو ارمنستان
🇦🇲
قطع شده و دارن فعلا پیگیری میکنن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SorkhTimes/139783" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139782">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLgVa0Nj_0D2jA0NXbXLWbUnId-hhbAEwOKHtI5KasQPk8aFsEm_rxsadpYiwQBD8FHEMx0mE6pda7ElRz949TnE3yyIvkFmQyyZDMDaHYCcB4bNo9hJH8kfj6DD4kFwQoamwnDyeNhnbxqBoz_H_I03ZJlrH9vuDGnK6VD6Rbe8okj41oLteSWTrg4F5fyY403f9SCSdu9lyhD9ixTpoQsNyZ1Mqn2zpRr1RM5RIIP12jcUcYC6dVDfND7rsEzsorzgffz9olzMI9SOvV7MvS95sX4HKQgTxeTrzADFqhAhJjJ541y4MSapDnrsle-1JjwavAXedUGfqQwluL1kdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
تیم ملی امید راهی ناگویا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SorkhTimes/139782" target="_blank">📅 22:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139781">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
فووووووری
🔄
با اعلام سازمان لیگ؛ فصل گذشته هیچ  قهرمانی نداشت و یه موز به استقلال رسید
😅
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/139781" target="_blank">📅 22:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139780">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
دکتر حقیقت: پارگی نسبت بزرگ بود اما سعی میکنیم به بازی خیبر برسد حالش هم عالی بود تقریبا بیست دقیقه پیش مرخص شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/139780" target="_blank">📅 22:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139779">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/139779" target="_blank">📅 21:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139778">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lnm-ZvgAQq-Vt2IbvL65FfE_7LzdZBeyzTzLujoRzGhV1hIHDpuZ8kgCkWRqZHDlgSh4bup_V7lMqkVPH7KYyXQqRar-EFZdmtAZbGUsZMoy9Rbij3VyCHLjZrh1D11YrFOwXQIgvykrdcv3YFMhXfrJkhyJ_fjLRLAKYpWmPP1C1RQiRFG-z7u8MFrQxRxRSF1pYn612oOk9m6JdzKKTuCjL8XbfuFjkKiXb9R2EwU6HNF6yvL-TETOHWep92XuMj3cGJucmNgWY3qYxH5Rn9DmO2zzTDMrlb6GWTJtb62iFa9RwYKg0YbznuR2sm4XP02BBEpbN-IxsLVgNPSEcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
💢
پاسپورت ۱۲ پرسپولیسی دریافت شد
💢
پاسپورت ۱۲ بازیکن پرسپولیس برای انجام امور مربوط به تیم ملی دریافت شده. نیازمند، کنعانی‌زادگان، ایری، زارع، لطیفی‌فر، محبی، علی علیپور و محمودی، هشت بازیکنی هستند که نام آنها در میان نفرات موردنظر قرار دارد.
💢
همچنین احتمال حضور محمد خدابنده‌لو و مهدی تیکدری در این جمع مطرح است، اما نام دو بازیکن دیگر هنوز مشخص نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/139778" target="_blank">📅 21:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139777">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/139777" target="_blank">📅 21:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139776">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/139776" target="_blank">📅 21:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139775">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acWNX29u4trm79IsWi3qDl2JagXQODWvYSNOC4Cfc7I-KA_ybF58a6lyttuW1bn_4g8VpMyjsQhWbDIV7UgS9f-sjuICdaOMWtOMotdcU7KJiEtfYTruu-8PrEV2HDMuL8mrjbf-peWjy69GVEoQpYBHMP3jQ1CelFbij8YscSwQ_3LdJ-ARrqUiRXq9Iyb5n8LB1wUGBe41L_Zf2lvj8sVxIUYUJfzwOoI2_2AzpJLEg_D53s8zRV_5RyNkTY70LMkng9ZPMKe-goa9PPze5ttkcvGxswB06_bvUXYv0IVy1qtHQ_O1SilFB7MP7YWAXD4QgY_PFNtfiYy5p2Rh3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
تارتار به ابرقویی آماده باش داده تا با تمرکز و آمادگی لازم برای بازی با خیبرخرم آباد آماده بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/139775" target="_blank">📅 21:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139774">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PFYnWkcURelLpB3vGAdRSnDL5M2ySUGUEEMteSSiYBr4bINUkDCbgMBsRFIPbNpddiT9IliPt7hu2j999r4gqXf-xru8Wgrp8RdFEcIQrZ9D95mwU3Yp-86eV3ufN7mAi-evycNMQV08dtzZa3h3eMQ9VZ4OIiv1UKI_au9a3xPn0bJfnhl-uNW2qJx9dHDlGmIpS_Qgprb9AMdNl1TyRZPSELe798oDSEyn6KreG_xfLke2_mA-JTpKVqbgPH-uiO3N2dxTMvcQOkBIuWCicD9feqkmDelABSRvMncoWqkK5SfDr-BchJ12gz9xguS_vSoc7x75_ZjPRpn3Utp1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پوریا شهرآبادی جوان ضمانت کننده آینده خط حمله پرسپولیس؛ یک خرید بسیار هوشمندانه از گل‌گهر که با استایل مناسب و دوندگی بالا در همین ۶ هفته ابتدایی که به عنوان بازیکن تعویضی به زمین اومده، نمایش قابل توجهی رو‌ رقم زده. امیدواریم با مدیریت درست کادرفنی و فرصت‌دادن دوباره به پوریا، شاهد درخشش دوباره این بازیکن باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/139774" target="_blank">📅 20:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139773">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAcQhwCMkN5f7TcUlm_XuRpJyYi0JPSjkRmSX1pnD0v1ypiqQ6ljTgZ0XHyv61Ly3kHet4EdKQVxZjT4CN9d4DqeXtJce8THD0eUJ7plPsV0sSi1ruC22Q760s2d0LiNAkpF-CP5ZkRtK5fqOeJPvwE60rMd6iygesmMqUFO2Z24_rAV7-J0WvrvclvYDzaXzGwk-I8Kp_A0QgpB5w20PGXbg0VLXx_ZU98IOQDW2c1vkZnwDtjlyruqVgO1ArwxznEUVHYgpI8pnRLI99q-JhLt45epVNZPHH_1sn0dLxKOrAc9Wkc95GdqP9KnKTIQsg-uGnpw73msOPaPQmiaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری بازی دوستانه پرسپولیس - پارس جنوبی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/139773" target="_blank">📅 20:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139772">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
با توجه به مصدومیت محمدمهدی زارع و غیبت احتمالی او در بازی بعدی، ممکن است پرسپولیس با حضور دانیال ایری در تیم ملی امید مخالفت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/139772" target="_blank">📅 20:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139771">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPNn1c1pPOejTPHzIEhnlYE7IihnkJg1s7-oG0NgbvzyrtXiSMZSX26ZtHiOSsM11eLygm8WcXCsbvKQMxBGO1c5wwrTjsZAy-Tpl67hKkMUeID1tww2ajzTxjmFg2zDJ0t9OsF9GN0gpCqqh7fRhXCHFGJQb7ksEqvB3rK0CwvRcJsTsjt2wK4Qi4LrNjPJYmrTMhC0PwBEr56hmqsVpC1VDtSz2wjiy8UkMXLiaU7QhaCLHi1QBKqZK6eu-LLVlrUUfH4-U9tSj7j-vF06By24OTyyGc-EgApjHgfP9AGfyGNIWKnX-GIahrSjhvf0Xiu9UgCC1vpsivQ34wRWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شب‌های باشکوه اروپا در راه است!
جایی که رویاها، ستاره‌ها و جاه‌طلبی‌ها
برای فتح بزرگ‌ترین جام قاره به هم می‌رسند
.
⚪️
RealMadrid -
🔵
Inter
⏰
Tonight 22:30
🏟
Bernabèu
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
⚽️
برنابئو در انتظار یک شبِ کهکشانی
رئال و اینتر؛ کدام تیم پیروز خواهد بود؟
فرصت رو از دست نده و همین حالا وارد وینکوبت شو و پیش‌بینی خودتو ثبت کن.
🔗
لینک بدون فیلتر وینکوبت:
👇
🟣
wngd3co.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/139771" target="_blank">📅 20:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139770">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
فوری| زارع مصدوم شد!
⏺
محمدمهدی زارع بعد از تمرین و هنگام دوش گرفتن، پایش به‌شدت برید و ۸ بخیه خورد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/139770" target="_blank">📅 20:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139769">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
پرسپولیس امروز در دیداری تدارکاتی به مصاف پارس جنوبی جم رفت و در پایان ۲-۱ شکست خورد.
✔️
سرخپوشان در این بازی با ترکیبی از بازیکنانی که در بازی شب گذشته مقابل ذوب‌آهن حضور نداشتند و بازیکنان تیم جوانان خود این بازی را آغاز کرد و در ادامه به دلیل…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/139769" target="_blank">📅 19:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139768">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
امید عالیشاه: بر اساس چه مدرکی من رو محروم کردید؟ من فحشی ندادم و چیزی نگفتم! اصلا در رختکن تیم ما بسته بود از کجا تشخیص دادید من بودم که منو محروم کنید؟  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/139768" target="_blank">📅 19:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139767">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🤥
🤥
دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/139767" target="_blank">📅 18:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139766">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
بازیکنان دعوت شده به اردو  تیم ملی بزرگسالان از نگاه ورزش سه
✔️
پیام نیازمند
✔️
محمدمهدی زارع
✔️
محمدحسین کنعانی زادگان
✔️
مهدی تیکدری
✔️
محمد خدابنده لو
✔️
محمدمهدی محبی
✔️
علی علیپور  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/139766" target="_blank">📅 18:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139765">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
پرسپولیس امروز در بازی تدارکاتی به مصاف تیم  پارس جنوبی جم می‌رود تا به بازیکن هایی که دیشب کمتر بازی کردند یا اصلا بهشون فرصت نرسیده، بازی بدهد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139765" target="_blank">📅 18:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139764">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CH9siK_a4tDSyAMnENC-Wl-arB9t2Uha1t-hz8YUZOunAkRFHV-_migWuZfDr_UWZHaaK55xrD7spmE82Dqz1TWa06bP5l5ryN2Uo9BvHAD67wszVAp0nKehGE_aoScAoHNUVuYYCdU7K2bbwhy7DCsKorD9zAJiBOKjYm7tWyc1g6YNEzK8qhkaJbE1sQSSmUi6qSZnrr3m9y9HqBb6GXGqEc0PMYzoa2c2oigHjn76MQ4EIxuW9rIDoULFizCTwHZ9-uK9HCn8Jn_9nLQ60m3dVePMAvta-uzslKX9vZBkQzPLfbpw84m_cQBBilCJaXfAGTWRTw-09EB-EA-5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
تسنیم: پرسپولیس بیش از حد به بیفوما وابسته شده؛ بدون او سرخ‌ها توانایی خلق موقعیت ندارند!
✔️
نظر شما چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139764" target="_blank">📅 15:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139763">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-GX_NoKkIXp9uZvI7ZfA5fB0oZfF-kbC2wjqCrxL2xPpR103h6CYJG-lZS0fUAXQk_U6dj6T5zIHwnhTgukBFu8mF_57Y5ZOwF_WHHAaPUIKPC0U3QIG9giO78MSq6HHxHeJZSgCSnhiq0dYhfah6oTMuWJgMLEWzD414Jxvi2cpWo8nYWNtoPC1Nr_v_GKYB-0Hc1Mm85annK54t9ZciVzYNq-oTNpYXJ-KwLwgAeNxtF8Gb30vt5Lsu5z-iV0XLYznxcSXfkvhFuUtoZQdDqUdjE9z_0FcwQfEwJjIjOahf9dN791R58X82lNJ6xl6hwSaQdJ5nenf2E1nfX2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
شهرآبادی، ایری و لطیفی‌فر به دلیل حضور در اردوی تیم ملی امید، بازی با خیبر را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139763" target="_blank">📅 15:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139761">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7ifI-G8Q74PuxLVi6ui4YM0oc_r5tueM_8CqbuFvW_ABdYgqbxhcUZWjcb82VrasXdGKAoO9gaXkm2ES366EPsdzzTVwYFlP3CewAQM98vtDbKqC4aDvrmR18qBwpo75M4F6GRSHr8eA4aTBNnpQl1NXLDJIfym4_g3LIUpjvcA9MnS3rA0ETyORn4H32E3Z6JLmBzoYCkZeLRQN7Qk3hd8oI_bC1doG94_rtmPLJ2W2rNZzwKa9k3fPlii7tK0hpVjSFT05l0YVxzQobCmjw3t9sgsqiC4GsE31k_BeS3ZPT9DgrL7ZIpUvA8_JzkF98chVKrwaHSV7lFGvNIOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🔴
میرور: فوتبال سرژ اوریه به پایین ترین سطح کریرش رسیده و می‌خواد در لیگ دسته هفتم فرانسه در تیم محلاتی مونتینی-آن-گوئله بازی کنه و انتقال اوریه به دلیل تاخیر در ارائه مدارک از سوی فدراسیون فوتبال ایران به تعویق افتاده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139761" target="_blank">📅 14:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139760">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139760" target="_blank">📅 14:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139759">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139759" target="_blank">📅 13:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139758">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❤️
❤️
بیفوما که به تیم ملی کنگو دعوت شده بود دعوتو رد کرده و گفته تیم ملی من پرسپولیسه و به تیم ملی نمی‌رم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139758" target="_blank">📅 13:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139757">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
پرسپولیس امروز در بازی تدارکاتی به مصاف تیم  پارس جنوبی جم می‌رود تا به بازیکن هایی که دیشب کمتر بازی کردند یا اصلا بهشون فرصت نرسیده، بازی بدهد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139757" target="_blank">📅 13:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139756">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2FsqLXzCjyKrziXD8WC5ehB5dbhWb93LZDepPD4asL2eH_lk60Nx4bbQsh_2YOZV8nxjngogaTRbeyOg8vvH_p7JDT_btAUYXFkYdfIp-BYtWp_Z0a57s8oY9snDseqpMEu51_e3JezIcrdFjVTnWceIRKi81FPtayUUFl-0OIwGJRkl9ezAfnMEW_xjaQarZjtysfPL8tDay9Yvv-c7ejewMypmAKfQsmBLpMxiGjRpn7OzuYPfmg34nwogNVxwah1hey-5NOg5n59PVMQUeVgj_USFNbm1jfUo2GXITlR5gTHjtG1SyfnWpZs9oVDez6U9ZDjwtivwLBIS11JeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئال و اینتر؛ دو غول، برای یک شب بزرگ
⚽️
رئال با تجربه و کیفیت فردی بالاتر، اما اینتر با دفاع منسجم و ضدحملات خطرناک؛ دوئلی که می‌تواند تا آخرین دقیقه نزدیک بماند.
[
رئال‌مادرید
⚪️
🆚
🔵
اینترمیلان
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139756" target="_blank">📅 12:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139755">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❤️
❤️
تارتار از امیر حسین محمودی خیلی راضیه و احتمالا مقابل خیبر زمان بیشتری بازی کنه//ورزش سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/139755" target="_blank">📅 12:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139754">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
تیم خسته اس ..ساق بچه ها خستگی داره ..امیدوارم نیمه دوم با آوردن صادقی و بیفوما و محمودی بتونیم از این خستگی رها بشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139754" target="_blank">📅 11:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139753">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
محسن خلیلی مدیر پرسپولیس: ۸۰۰ میلیارد بودجه لازم تا ورزشگاه آزادی تا چند ماه آینده آماه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139753" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139752">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUQHSNAMyDCyYsR5OuLA9J4EyOJUllmcM_qFG9uJikRuMQjeomT4pkbNnmZOnSEgN7fwx5k8ZY0vrnrHyTQnxJSpfCZXJyqqt4eBZ-qXZnbrkFEe6vgRdxITUEkdab6dRoHz9TK_GewSE5WKCLXHrvHC96P07u6sx0jI2nwmnzzbYaOnybUCexsNQ6YppQWOqsCrSUGSw5Xfs9lED8E-hWXZ5_w2Hn6Zg7V-6E5_ZQS8JWAkM4VEyP7au3cR4Yotqkmck6seVFBvda6c290TfizzW165GYVUZzxHCfcufUCnbpmD161ONmIHx-EqIWsuZefEhnZu5JLOd5FZJcT72g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ایری در پاسخ به یک هوادار: تا روزی که جبران نکنم، شرمنده شما هستم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139752" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139751">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139751" target="_blank">📅 09:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139750">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🗣
حجت موتوری مدیرعامل ترتر: به شجاع خلیل زاده و علیرضا بیرانوند در بازی با چادرملو فحش ناموس دادند، آیا این درست است؟
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139750" target="_blank">📅 09:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139749">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZ0_KEPh6JkfUonRmaro276Hh7UaTOYZgd-v0TzhDrq9cP-Qeic-ZB-lXKjrEOuuseOw8wmN00vVEAVSfPsV_4C8GBjY9Z9dXlKrFyGxwiluu2b7lPXI9EPwEAMDha78GRlDa5aE3JKqm_FX-f1XcNJFaXi6MTr-vVhi7wbaXv1QV8s3Tt0ZQDmBsSGG7Db77jQDn29IKMFI8vjeI38DTpV9ljClaocnIFUg1XTNmgoWicYcuRCfxOCNw8rgJI5A0qG8GnU3vDvLjPERqi1HJEeyb9bqmpo8tSEwjsPmB2kJxVDMOWuWUrLUeTvmNPySIT_HaazfYRIKn8d_C0XP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
امید عالیشاه: بر اساس چه مدرکی من رو محروم کردید؟ من فحشی ندادم و چیزی نگفتم! اصلا در رختکن تیم ما بسته بود از کجا تشخیص دادید من بودم که منو محروم کنید؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139749" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139748">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و اومدیم دوم جدول و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139748" target="_blank">📅 09:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139747">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjhTRh72GR5RKPPJRY1lW2hOtZQQMcaQtjVeln7uPrVGN-zN4F0ME8_Hnh3iHTMzc_5L5geMIEWL1GJkCqHbPjnsIG3oJGbVBsTeBCpDePRDV3DWE9etQ4c3oWvaUxtpXlGMyZK9Hc7yWo_kqwIiAMWS4XptpYvh8cOwy8hWC0zJ8NyCgYeSaBZXSd4poXmbmTmFVwNp4-BytA_pYdUhlakwC53FSaKkCFsFVC1Y-QzEHOyOb1FvsoFvd_1H9i414FyDq3rmuEeD-DialjfR6fUQQ-IXYJ8y62shrGghKUvc7avFHdDuH4yAYex-2AZKoFk7BufEgDg70aWn3HnC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
جدال جذاب در یواس اوپن
🔥
[
الکساندر زورف
🆚
لوسیانو داردری
]
⏰
بامداد سه‌شنبه ساعت
۰۳:۴۰
🎾
زورف با سرویس قدرتمند و تجربه بیشتر، شانس اول پیروزی است.
داردری با سبک جنگنده خود اگر ریتم بگیرد، می‌تواند زورف را به دردسر بیندازد.
با این حال، روی هاردکورت کفه ترازو همچنان به سود زورف است.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139747" target="_blank">📅 01:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139746">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✔️
✔️
✔️
پیراهن پرسپولیس را بپوشید و به تیم ملی برگردید
✔️
در دو سال اخیر گولسیانی ، گندوز ، باکیچ و بیفوما از پرسپولیس به تیم های ملی خود راه یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139746" target="_blank">📅 01:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139745">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139745" target="_blank">📅 01:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139744">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139744" target="_blank">📅 01:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139743">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ae53c901.mp4?token=N-c2iBEQmt8c6AjqcIc0BE2bjOx0pMTSC34t-mIQQwoSO-T792BWa2ijSCiouN8izOjXL13t8ityzYMb0fdyq_gBhmhopelbm9H2iAkH4sjpKMRAlWjL7H3P9oGf_ePz1_1CXtBWXbHqZy3sE5L7GEBy-_NntC6bzPe5Qk4jH6yDxCdd-eWVEPGvSez3tQdbSpZMlzesWbmCogTdpBxJANT1K5GoRuK6PSq_4nMT5_lWCBm0b8ef2-EbyKmENoB4HjKnbvwALRe1BoqTUEUw2ml-nqW9Oir1WpuTBK8ddYJ2y9dKAt7cNfkQMcnwPv9y_piObUzm0bZLRprxxJFzkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ae53c901.mp4?token=N-c2iBEQmt8c6AjqcIc0BE2bjOx0pMTSC34t-mIQQwoSO-T792BWa2ijSCiouN8izOjXL13t8ityzYMb0fdyq_gBhmhopelbm9H2iAkH4sjpKMRAlWjL7H3P9oGf_ePz1_1CXtBWXbHqZy3sE5L7GEBy-_NntC6bzPe5Qk4jH6yDxCdd-eWVEPGvSez3tQdbSpZMlzesWbmCogTdpBxJANT1K5GoRuK6PSq_4nMT5_lWCBm0b8ef2-EbyKmENoB4HjKnbvwALRe1BoqTUEUw2ml-nqW9Oir1WpuTBK8ddYJ2y9dKAt7cNfkQMcnwPv9y_piObUzm0bZLRprxxJFzkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
حجت موتوری مدیرعامل ترتر: به شجاع خلیل زاده و علیرضا بیرانوند در بازی با چادرملو فحش ناموس دادند، آیا این درست است؟
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139743" target="_blank">📅 00:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139742">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa88055fa.mp4?token=fwI8wJHOHN7CPzcl5IjAZt7_X_zKNR_Yk0TR4qbWdAHv4_P4F7IfrLUSRC_OZv1yGkCscSxhfyFhoqFoDHFvrVXTvg_rpDDJyEojmFeaBClLHiWAaoEJlX4emdC62xTv-jGg2-Lv-M9rEU4vQ2TsfTt_ds8ke3Qriw3FmQ54afAzeqHg5nlxyT97gzKnkuM6hgWX3JaIkI0TNcFJg2o2LUjTPY1m-HR6cEUFtFnH5VD7YpwM_l-9vx9N_Z0JFgpWbyYVVuN9hdIFTtxkUBOiJJdHXOWRQeXvhBt6h1cKlivaDi_ly0T7Rlbm2rcfvjgATVBUjs7mD542Ls4Dhh_gwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa88055fa.mp4?token=fwI8wJHOHN7CPzcl5IjAZt7_X_zKNR_Yk0TR4qbWdAHv4_P4F7IfrLUSRC_OZv1yGkCscSxhfyFhoqFoDHFvrVXTvg_rpDDJyEojmFeaBClLHiWAaoEJlX4emdC62xTv-jGg2-Lv-M9rEU4vQ2TsfTt_ds8ke3Qriw3FmQ54afAzeqHg5nlxyT97gzKnkuM6hgWX3JaIkI0TNcFJg2o2LUjTPY1m-HR6cEUFtFnH5VD7YpwM_l-9vx9N_Z0JFgpWbyYVVuN9hdIFTtxkUBOiJJdHXOWRQeXvhBt6h1cKlivaDi_ly0T7Rlbm2rcfvjgATVBUjs7mD542Ls4Dhh_gwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
حجت موتوری: ویس های فحاشی خداداد را دوستان اول دادند به شبکه های معاند، اول آنها پخش کردند
🤣
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139742" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139741">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
✅
✅
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139741" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139740">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139740" target="_blank">📅 00:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139739">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b0cebd97.mp4?token=XGAoGwgal3bqrETVrJp_ZnYbiQfKsdr0hG7McMiRLze7v4T37SI7Ganv7CwDxLnWWrk2uwtkVMrkkYfg1LVyO6_4RfGdi-h91c18ZZnFHcJO9UhLPflB4dSKbo2fTaIykxuE7ZgS3AclFGKvDCmJrrlb2s2gSn-k6k3jtxFLvLx9LAuAl7K1WOAbTGt88R15mxG2Pj4Ds6EPiVJsHvwKSvN77L-24xReDWBj3mkBn-NMn1aOR3KNgQzJY4WA2N6lQ7avXtNY0KeCCALZOIvzGKKqlhW_BZicO2RVfy55VqYvkITptjbSpafW6iCDTOpsM34nSYyYfrTZkiDLQMaA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b0cebd97.mp4?token=XGAoGwgal3bqrETVrJp_ZnYbiQfKsdr0hG7McMiRLze7v4T37SI7Ganv7CwDxLnWWrk2uwtkVMrkkYfg1LVyO6_4RfGdi-h91c18ZZnFHcJO9UhLPflB4dSKbo2fTaIykxuE7ZgS3AclFGKvDCmJrrlb2s2gSn-k6k3jtxFLvLx9LAuAl7K1WOAbTGt88R15mxG2Pj4Ds6EPiVJsHvwKSvN77L-24xReDWBj3mkBn-NMn1aOR3KNgQzJY4WA2N6lQ7avXtNY0KeCCALZOIvzGKKqlhW_BZicO2RVfy55VqYvkITptjbSpafW6iCDTOpsM34nSYyYfrTZkiDLQMaA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139739" target="_blank">📅 23:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139738">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✔️
✔️
تارتار سرمربی پرسولیس: هوادار دوست دارد تیمش هجومی بازی کند/ قبلا هم گفتم اینجا پرسپولیس است و هواداران بازی زیبا و هجومی را دوست دارند
✔️
✔️
واقعا یک تیم کامل داریم و بازیکنان دارند روز به روز بهتر می شوند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139738" target="_blank">📅 23:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139737">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139737" target="_blank">📅 23:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139736">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139736" target="_blank">📅 23:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139735">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139735" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139734">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk4p3JQy4fIw2VP9MdCcQSdPLqtaNtWsRSlVowswsZ_EY7thIAOmjlAiMhe00jRgxnGJY-fthH3mfGBpfoURKBiD1UukhPfHVyMbQUurWp7KyO9YE77gizvABV2todYp-M_6oa3u9VF2S0jOBjhKKrRUo5GXCxDrigblzoazw9mpjLNKZphJAGHpt01WiwQf0uWgQ1KLRBZSlyXhUOQgUtb8x1mLMw_LhA9LGKnTz2QdJT9wRyrmEpujxN5Vo2qOub-ICfcGy4L0iANKOJtmmOKAh1pe8_gTBgBie6ST2w2Z9k9n7AeT0ZYryMl-3xIvhFBWBOQ1PjaPxCmrn7N2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک به اوج خود رسیده!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/139734" target="_blank">📅 22:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139733">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7Lp-z7R4ONAdisPkmIZlxc4y2jil3TOg0OMPM55dRTX_nnwBdfYPwg7pQENoalUnbG9LXBpIo5uX3vzWWNmKdBpoaDUk2umQ5qOnH9juBcl8AZ_JWBA5ZxR_C9gvYIJ00h7sGX1L274KRh-neAhpFpvEc98ZGXUjok4UY0pk8TpgZFO0zxuG1JIyFOU8-vvc8cLTlaMytWUni4wuORDvuyWAFfov7J_rIW7pj7BqqLMcmgu0tdzM-qWJfal425flQ7DIgOyiyQ1V_3REFyy6ATKcOxMm8RSSUX9O31o-eYxI9CCdQFXAVktIn-HMx34Mm4ah5vl4fvBDtFah2icgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج هفته ششم و جدول لیگ برتر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139733" target="_blank">📅 22:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139732">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139732" target="_blank">📅 22:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139731">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139731" target="_blank">📅 22:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139730">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139730" target="_blank">📅 22:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139729">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✔️
گل اول پرسپولیس به ذوب آهن توسط علی علیپور
🔥
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139729" target="_blank">📅 22:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139728">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
تارتار: فشارها علیه پرسپولیس؟ هواداران ما امسال اتحاد خوبی دارند و تا زمانی که این اتحاد باشد ما آسیب نمی‌بینیم
✔️
✔️
کری‌خوانی نماینده‌های تبریز؟ فوتبال از سیاست جدا هست و درباره فوتبال، فوتبالی‌ها باید نظر بدهند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139728" target="_blank">📅 21:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139727">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
تارتار: در روزی که خوب نبودیم بردیم
❌
❌
سرمربی پرسپولیس در روزی که خیلی خوب نبودیم اما بازی را با پیروزی پشت سرگذاشتیم/ چمن ورزشگاه شهر قدس خیلی خوب نبود امیدوارم این چمن را درست کنند چون امروز واقعا خوب نبود
❌
❌
واقعا جای سوال دارد که چرا کیفیت چمن افت کرده…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139727" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139726">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
کنایه حدادی به خداداد عزیزی : در این خصوص نمی توانم حرف بزنم اما فقط به آقای خلیلی جنگجوی و با ادب خودمان خسته نباشید می گویم. این نتایجی که می گیریم او هم تاثیر گذار است و در کنار خط در نهایت ادب با جنگندگی حق تیم را پیگیری می کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139726" target="_blank">📅 21:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139725">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139725" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139723">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
🤩
دکتر پیمان حدادی، مدیرعامل پرسپولیس:
❌
امیدواریم روند پیروزی‌ها ادامه‌دار باشد. طبیعی است که از بزرگ‌ترین و پرافتخارترین تیم ایران، انتظارات بالایی وجود داشته باشد.
❌
با توجه به مستنداتی که در اختیار داریم، درخصوص پرونده آسانی از باشگاه استقلال شکایت کرده‌ایم و در صورت حاصل نشدن نتیجه، حتما پیگیری‌های خود برای احقاق حق باشگاه را از طریق دادگاه CAS ادامه خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139723" target="_blank">📅 21:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139722">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139722" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139721">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=XkIeWRxVzoHQvdQ7l5aCjglK83yibtu9tfiCazkF1VDwWwTaAY6iMrKHyj43pnmmVsCg2pdbpWSt2NbkVTDkewveOFAqZHgGDaG-KVDhD72tvTdBM1BRV0si4pA7vjaTICBAS-qphORYBuw4_sHalE3vHWAz4mU4IJGUI5A4huG6z_DNVI4JIFWHqqnsUbS1POgBZw4mstS6azKALmedRT_LS3HZS-P0WqhuX0yBlfpxbg6mIU8AlJhotqv9oNnVRXHJu3nW3LlYkyJnrIG-x6qCVfWYGaSVwN0NJyDKO8ck8dAKTKe0Ua71JrEeKnk-MCxyPj3hlAmiz9CJTwn0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=XkIeWRxVzoHQvdQ7l5aCjglK83yibtu9tfiCazkF1VDwWwTaAY6iMrKHyj43pnmmVsCg2pdbpWSt2NbkVTDkewveOFAqZHgGDaG-KVDhD72tvTdBM1BRV0si4pA7vjaTICBAS-qphORYBuw4_sHalE3vHWAz4mU4IJGUI5A4huG6z_DNVI4JIFWHqqnsUbS1POgBZw4mstS6azKALmedRT_LS3HZS-P0WqhuX0yBlfpxbg6mIU8AlJhotqv9oNnVRXHJu3nW3LlYkyJnrIG-x6qCVfWYGaSVwN0NJyDKO8ck8dAKTKe0Ua71JrEeKnk-MCxyPj3hlAmiz9CJTwn0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
واکنش جالب هوادار تیم به عملکرد پرسپولیس: بارسلونا هم بیاید در این زمین شکستش می دهیم؛ 2 تا به بارسا گل میزنیم 3 تا به رئال!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139721" target="_blank">📅 21:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139720">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809956e0a8.mp4?token=m8NZGpiBemBX95SuGaFIUlfqk2Jc08Ul2tSBXuHehaK_dWKkkG6zTP2bGimVEs_6FKWck_Hi7llOk4b3eGEMOkIxisXmcYiZd1Mdh4DZs3TNIUtyFzVFpkPapexXPk-KonTFtNTx7NrUxwBca5KIvSQMMMHZlud7QeuXEomjKUbt17YaLorXQGeI9m924_M6ucBVVKLp6aZNt5Es74qbFAoj0iuKQ3e37CFKF9-HfQ-4uB2eOCoAfC7nnD-NFGa4Mk_WBB5ip1wSaM27N2UFWGWsMr9P9xGUmgjEPxVe0Z7ZWTpYOlXMEKxEPopUh6UfLG9WekfNuxEeYP1roa8lcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809956e0a8.mp4?token=m8NZGpiBemBX95SuGaFIUlfqk2Jc08Ul2tSBXuHehaK_dWKkkG6zTP2bGimVEs_6FKWck_Hi7llOk4b3eGEMOkIxisXmcYiZd1Mdh4DZs3TNIUtyFzVFpkPapexXPk-KonTFtNTx7NrUxwBca5KIvSQMMMHZlud7QeuXEomjKUbt17YaLorXQGeI9m924_M6ucBVVKLp6aZNt5Es74qbFAoj0iuKQ3e37CFKF9-HfQ-4uB2eOCoAfC7nnD-NFGa4Mk_WBB5ip1wSaM27N2UFWGWsMr9P9xGUmgjEPxVe0Z7ZWTpYOlXMEKxEPopUh6UfLG9WekfNuxEeYP1roa8lcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139720" target="_blank">📅 21:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139719">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGfnoYxR3GooyhcBUwKKCq69F7Zjk85MYIVhMKsOPWW31bg4L8dz7cH_eUSNK3P1ShwRI7X_99XDwfD-O0TaNyI-EgvmGkfNi72p1XAWtI76XRfUV7YUkpUisOtakbr0PCHF5nZKjV2mJzqg1oLfbdAvCVlNSJSvH0fqyX0spjf9EwwIAZHsT-ElimRzwUrBB235MEOdXzW3MqJoQPAHfTHQk-Bgeqq49msVFJNr1nQ2dLFzhx2eqenJyeaJkzVsQ3KjblaPD0OZTxm71HvdLNnJgqM7UdjPFwH0NGWvCtqNt0xy319C4KOo9TWTnsDzQjVpKW4jnRCSGCWGpZKu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
علیپور تاثیرگذارترین بازیکن کل لیگ تا هفته ششم
✔️
6 بازی، 3 گل، 3 پاس گل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139719" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139718">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139718" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139717">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=a8xAyW-Pqc6pu-qMiJebVqb0gK96WeyvBwYlCspQ9j3HsaDZIYSAZSDdhzC3brlwYwaZrXwD9HzxWRJzW1MxoivhnqZfaCpSjgiuyOHQzc7Phe1NTTqiANXVWJVxGh_3SzPzIL8EmhQaeV-WLba_Z-fNOjrOTcZPgJkFoYIdv5yzeVcyaJOq1U0IseHab5MQGiw21tSZq4GncHJrP6TIB1lxhkeBQJjcWK9af8DrInQRQwIHS3RLSpFa9ArcW-lE8x8JgMXwSjB1OYm4INigL-XuX4EzXlmtCpArFA3df9xcOlRnMOjM-oN6I6aKxlz-1ZtZIz2wjN3pXV1-Ksi0oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=a8xAyW-Pqc6pu-qMiJebVqb0gK96WeyvBwYlCspQ9j3HsaDZIYSAZSDdhzC3brlwYwaZrXwD9HzxWRJzW1MxoivhnqZfaCpSjgiuyOHQzc7Phe1NTTqiANXVWJVxGh_3SzPzIL8EmhQaeV-WLba_Z-fNOjrOTcZPgJkFoYIdv5yzeVcyaJOq1U0IseHab5MQGiw21tSZq4GncHJrP6TIB1lxhkeBQJjcWK9af8DrInQRQwIHS3RLSpFa9ArcW-lE8x8JgMXwSjB1OYm4INigL-XuX4EzXlmtCpArFA3df9xcOlRnMOjM-oN6I6aKxlz-1ZtZIz2wjN3pXV1-Ksi0oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139717" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139716">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139716" target="_blank">📅 20:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139715">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139715" target="_blank">📅 20:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139714">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
گل اول و توسط علیپور زدیم با اینکه نیمه اول خوب نبودیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139714" target="_blank">📅 20:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139713">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139713" target="_blank">📅 20:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139712">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139712" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139711">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139711" target="_blank">📅 20:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139709">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
این بازی و بچه ها با سه امتیاز بازی و ترک کنن برای بازی بعدی بعد از مدت ها یک هفته تایم و استراحت داریم ...و بازی بعدی یکشنبه هفته بعدی با خیبره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139709" target="_blank">📅 20:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139708">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
تیم خسته اس ..ساق بچه ها خستگی داره ..امیدوارم نیمه دوم با آوردن صادقی و بیفوما و محمودی بتونیم از این خستگی رها بشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139708" target="_blank">📅 19:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139707">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139707" target="_blank">📅 19:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139706">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🏅
پایان نیمه اول
🏅
پرسپولیس
1️⃣
_
🏅
ذوب‌آهن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
0️⃣</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139706" target="_blank">📅 19:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139705">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1X0oWdhiQdp-Rqzj1s62351T8z_TqMkdLXK5LAqv_wNW4YNCXHrqOlNtxbgm8m6DD3dvJMLTkIiyxsVzDyv47adn104rmdw3M-ddF4fOdxxlhgxOld3pTgiJVC8g7UTEJPjqvNjvzGdQedeNTV34J4Hoo4NKpwyJTVSulq5zxFpi3GOYWSavFQmrYWOIAZdKUFMr5RE8a9tl2aZDzU36BMnPorEFs8Uht3LiboB4jfoIC8fG5j9SPm3cZ-ITSe5w8qg93d355bcuUfjdly6Fi8ZA2fkgE6r6oBXUq_PgA3ycR1v4qpi-YDBUz9WcoKjHR2ybSj9biWAO75RmZcajJ_gE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1X0oWdhiQdp-Rqzj1s62351T8z_TqMkdLXK5LAqv_wNW4YNCXHrqOlNtxbgm8m6DD3dvJMLTkIiyxsVzDyv47adn104rmdw3M-ddF4fOdxxlhgxOld3pTgiJVC8g7UTEJPjqvNjvzGdQedeNTV34J4Hoo4NKpwyJTVSulq5zxFpi3GOYWSavFQmrYWOIAZdKUFMr5RE8a9tl2aZDzU36BMnPorEFs8Uht3LiboB4jfoIC8fG5j9SPm3cZ-ITSe5w8qg93d355bcuUfjdly6Fi8ZA2fkgE6r6oBXUq_PgA3ycR1v4qpi-YDBUz9WcoKjHR2ybSj9biWAO75RmZcajJ_gE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول پرسپولیس به ذوب آهن توسط علی علیپور
🔥
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139705" target="_blank">📅 19:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139704">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139704" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139703">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139703" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139702">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
بریم برای بازی شش امتیازی ..امیدوارم مثل بازی های گذشته از دیدن فوتبال پرسپولیس لذت ببریم ...الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139702" target="_blank">📅 19:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139701">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFGBAdDtDKnN7S-z8BIDQs2H1jxqWrm6BUNPCJFZmEBIi4G1e_5dAID0GDjTi_ScwBlX393e8tsbxNYnFnldfwWU-8gmAPvXcNPRYgrkLsTZf_hKXm2KAq2jP5YPr6cUikewPvbfXTJxBBiF6jpExmZc1Qeq-hIQ2quSGWejaeYRjbeYnCPMveqyfzZx4nAFX9jSlN9nj_J14HG4qH_u7c5bBzJos_Q0W1yhmF1HFDAKn2dahNc3dHIFtDYRmUtb_tJuXXHK0soW0st1Affw6rCEnzpni_LUOPjUu_sh6AxePj-roALtibZsxyZkVQtW4Zaops1PoTTVXO5DUDaMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک به اوج خود رسیده!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/139701" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139700">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
✔️
شماتیک ترکیب پرسپولیس مقابل ذوب‌آهن
🗣
اورونوف دلها فیکس شد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139700" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139699">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
هوادار پرسپولیس درباره جنجال امید عالیشاه و خداداد عزیزی
❌
❌
آقای خداداد عزیزی به قول سیدجلال ما پرسپولیسی‌ها هیچ چیزی از یادمان نمی‌رود. خدا نکند که ما پرسپولیسی‌ها با تو رودررو شویم؛ می‌توانی از بیرانوند بپرسی. مثل خودت با تو رفتار می‌کنیم. کل افتخارات…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/139699" target="_blank">📅 18:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139698">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✔️
✔️
✔️
صحبت‌های هوادار پرسپولیس درباره اتفاقات بازی تراکتور- گل گهر و حواشی ایجاد شده میان عالیشاه و خداداد عزیزی!
❌
❌
از کمیته انضباطی سخت می‌خواهیم برای یک بار هم که شده رای درست بدهد.‌امروز نشان می‌دهیم که هیچ کسی حق توهین به عالیشاه را ندارد. امید عالیشاه…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139698" target="_blank">📅 18:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139697">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139697" target="_blank">📅 18:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
ترکیب بازی امروز همینه و تایید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139696" target="_blank">📅 18:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=QvYImc28uYZKXks675ssu62nuZi1nYgGhNU8qktlRT_5VbJc9zZnzvKZ-mOPbj8ny0phKMbzvPJWteens_vuy571DhjF0UhrGrXRwREWCHlDe8w7CIzLE1Gay715GEN3SEUfn6OglowtBkIYljK3hC3fNShjCJSV5x2C6llL312n0WtlsPmEYVo8KUiMb3eSXaj__iAJH3GKogpsQ8yTEfAs5Rx_3tllxUqNFcmhE0Z2oRDMEJ8aB8o8f77gtfdO8rHsN8j36jfz9KMqy25DeHOoJ79bXi4MxUey7bR3loA8x4v2F00tynExZPzHOrRdCfcy52kRhRIrwo_N97fHCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=QvYImc28uYZKXks675ssu62nuZi1nYgGhNU8qktlRT_5VbJc9zZnzvKZ-mOPbj8ny0phKMbzvPJWteens_vuy571DhjF0UhrGrXRwREWCHlDe8w7CIzLE1Gay715GEN3SEUfn6OglowtBkIYljK3hC3fNShjCJSV5x2C6llL312n0WtlsPmEYVo8KUiMb3eSXaj__iAJH3GKogpsQ8yTEfAs5Rx_3tllxUqNFcmhE0Z2oRDMEJ8aB8o8f77gtfdO8rHsN8j36jfz9KMqy25DeHOoJ79bXi4MxUey7bR3loA8x4v2F00tynExZPzHOrRdCfcy52kRhRIrwo_N97fHCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139695" target="_blank">📅 18:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
✔️
✔️
نیمکت
✔️
امیر رضا رفیعی
✔️
ایری
✔️
ابرقویی
✔️
جلالی
✔️
باکیچ
✔️
لطیفی فر
✔️
یاسین
✔️
صادقی
✔️
محمودی
✔️
بیفوما
✔️
شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139694" target="_blank">📅 18:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
شماتیک ترکیب پرسپولیس مقابل ذوب‌آهن
🗣
اورونوف دلها فیکس شد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/139693" target="_blank">📅 18:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2J_5As0C-XA_TCuTXSlEe88ND5y_Zq1jzmA0Peq8W9zTiAiGC0MysjWpxKa3LHpcLLnc0ZI0qjfFYtY6g_kGzCptdF6vL1Yi3yfhgNEr-ULpEQ6xLjJQNRhAx22SvfjRhEu7_QX1pWrvcURkpENLZU58zxibqTixELDHQZSGZ8hzwjc4g0_aNXrpcktJr9cngYoTTnlQzUzA6wer_Ry9COU1xGPWDg7XtlSe_dCAS1nJk644VO8PMSfSfsv0HQCoDvY5MmgTyf1Jeqw_O4EY0zDdPkIb4Q7qP-8TUmqxjp5oc_tGKm3YYAJtro4Nv3gsKcfrAmJrmEJZytoanU7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139692" target="_blank">📅 18:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139691">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/139691" target="_blank">📅 17:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139690">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7939cefa83.mp4?token=mwgDtmtSE0yrYMXtgszRJrgm6HEfzV59EoXXE6wTAj_rd8vYfkYXIpMK3Jo2PYhvCnh8Mjv0M236sXcNiRwhf54oc3Sm7WE7-8iOF5gtgcpznbTnNz-YGfi6jN96tpoS87fBpVJ07XMT8tdp-jhgR9iMhOhGiKeTPmQ0qjLz3m5pIK54XszMr9Wn5mzJlGj-z1UODOzk3MRt72Je8ZPXsxp4RLvIvOdksIBo5QCDclhBU0-hxsO8uN1mIvlbwzF7x3TIP8tOUCropMPlsb5SiYkUo6qR5F2YGtGCrrcvZfCW36hzj4TXGfA_s4_rfhE-Vl7eoUlslD1JWDNxipA0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7939cefa83.mp4?token=mwgDtmtSE0yrYMXtgszRJrgm6HEfzV59EoXXE6wTAj_rd8vYfkYXIpMK3Jo2PYhvCnh8Mjv0M236sXcNiRwhf54oc3Sm7WE7-8iOF5gtgcpznbTnNz-YGfi6jN96tpoS87fBpVJ07XMT8tdp-jhgR9iMhOhGiKeTPmQ0qjLz3m5pIK54XszMr9Wn5mzJlGj-z1UODOzk3MRt72Je8ZPXsxp4RLvIvOdksIBo5QCDclhBU0-hxsO8uN1mIvlbwzF7x3TIP8tOUCropMPlsb5SiYkUo6qR5F2YGtGCrrcvZfCW36hzj4TXGfA_s4_rfhE-Vl7eoUlslD1JWDNxipA0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
هوادار پرسپولیس:
✔️
ورزشگاه آزادی درست بود، بی‌افتخار ترین تیم لیگ (تراکتور) عمرا قهرمان نمی‌شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139690" target="_blank">📅 17:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139689">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8432a81f4.mp4?token=eq1U1rCtxTYUewJqPT7LacguA4b7cThQ4wy447n0hkzs3de1AVhGiFVwJpoKWeFpTY984O9yhFihxjJtx5GS_MFZ1xpsv0a_MVyKm5mnir5LmAjhbscqCDsWqnMpQJDxtHptVtHbeFXIZV6utB9g9JaC3JxWdFFxHG-XUQeNZnX-4hXLH_tA7TPOb_Nq0IGlQhLTtGLZNvnoDOTONFIz9jqQBhuUUH5ZxnyHqu0P67RpHmb4lh4-xa65_KhYbHZaVgZHf_-DOKHO5yX6UIX1ZUY_mSg4f-LMRcII8jtqonDTR6hLRWCuEuQyMijaShhIUCjYXrBeYvfbj402MkhOuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8432a81f4.mp4?token=eq1U1rCtxTYUewJqPT7LacguA4b7cThQ4wy447n0hkzs3de1AVhGiFVwJpoKWeFpTY984O9yhFihxjJtx5GS_MFZ1xpsv0a_MVyKm5mnir5LmAjhbscqCDsWqnMpQJDxtHptVtHbeFXIZV6utB9g9JaC3JxWdFFxHG-XUQeNZnX-4hXLH_tA7TPOb_Nq0IGlQhLTtGLZNvnoDOTONFIz9jqQBhuUUH5ZxnyHqu0P67RpHmb4lh4-xa65_KhYbHZaVgZHf_-DOKHO5yX6UIX1ZUY_mSg4f-LMRcII8jtqonDTR6hLRWCuEuQyMijaShhIUCjYXrBeYvfbj402MkhOuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
بانوان پرسپولیسی و تشویق امید عالیشاه در شهرقدس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139689" target="_blank">📅 17:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139688">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVjRPUqiHniWndz9g3RmRHMdar-bSC4XTsI13V-B0d109QZDKxxkqWXUUYWE1TVibZwom8izuo-ErdydicuiO47V69nad84JuIvyq5Y9pYXFDVacxe-2m62IbTGPXi6qZ-5j8NPS0Kn22emw77UHj93bCDz9oXPkE34Vl9JQbR7xtElnRJ1mR1JNI2ZSjRrlnxRR2K9gvHlq8H4uzaRXieujX-vma5YV_Ntf7cnod4YaBk0Jvzn3xRqt0wtpNaO2rtGzdCSrbeXbx0aztXTA6WOyfSoWxE7-y8mT8PtM1rBWySMg8K11n72LP3OS5jhy2mS-vmwV0PkUkFlJiO0GAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
عالیشاه وکیل گرفت
❌
❌
شکایت عالیشاه از خداداد عزیزی به زودی در مراجع قضایی ثبت خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139688" target="_blank">📅 17:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139687">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxtU9KDxhtdA4tH7ZLV9TF6J6PmN1hO_5HrsyuEnCdUbADZuIvdtBBQKAwPSLvNh7z_r9kjpidV0uMChDwBB5Sz03c8ZUFZJV8K-tQmfIhIkIj2Wi47tpEguP-lukNbEZ52iISyuHtfQKfEZf_jh_Wut_SDv6FI1qFeVirIpForNj6aYveLl9k6bRR3CYuhInKeIAmItjVmlf8LTy0JpTiBZyNowefmCVeJ40RD08nNkVRo9GCw6gEsYlILaExX3vf5ps0Da8jMz4vyeKiAInBFW3OXwiijD5YfbwdSF1S1qgwN_WvFlJP1UvlCdk8CZXp9EHx2oWEeTN0OcaiOmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
هوادارا دم در ورزشگاه شهرقدس
😂
🗣
ورود بدون کارت ملی ممنوع!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139687" target="_blank">📅 17:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139686">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
گفته میشه که ویسی از که از خداداد عزیزی پخش شده فقط بخشی از فحاشیش به امید عالیشاه بازیکن گل‌گهر بوده و بخش زیادی از فحش ها و صحبت ها پخش نشده و قرار است به دادگاه ارائه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139686" target="_blank">📅 17:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139685">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
لیست تیم ملی امید اعلام شد.
🔻
اردو برای اعزام به بازی های آسیایی 2026 ناگویا از صبح فردا دوشنبه 16 شهریورماه در هتل المپیک برگزار می شود.
✔️
✔️
اسامی دعوت شدگان به شرح زیر است:
✖️
✖️
محمد خلیفه؛ادیب زارعی؛آرمین عباسی؛محمد امین حزباوی؛مسعود محبی؛دانیال ایری؛یاسین…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139685" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
