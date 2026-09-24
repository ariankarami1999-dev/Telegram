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
<img src="https://cdn4.telesco.pe/file/JzTTUbvcODRElHB6mqxVtr5M-zb0m6b2628DqRrHgBUIyveZQ2muFMyUOvjzm5YUF4kCm0ZiTNvhdt7IZLfUsUI1h2TWuTF5qarq7hRqmPCUJ_g4w6-NAOQ-5q0_RVRrAqTLRkiOXjudy1WCSfsXsKtVRIOyXCfRaqQxX7yUJjd8fU6fEtgQRVLHb_Zs3WXgRX12ag8JfJgyqPFKNPRrhALBCQPK_S4ZqYWPaxeJaRu70xJOL6J0IHJd6ROvAUtqJJmJSR4AYdnmN0acNzlRQXMfm3z38DjQarkm9xI2zBHAkO0HbsoloYZSVxQ0Ws2tzcZQ8M1nUF3Z2RkeMeV92Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 453K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 14:17:46</div>
<hr>

<div class="tg-post" id="msg-30345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ft67o6_JyNJBVqq81AYE38__37wKcw99jiP_O3QUBAYp4sqDVoxHRD-ty6NGQWe_o5TCBsT0vhGa3LcSRVmS7-4q-rCukcr0eSHMYyHyCblHBcfr2mS-eB0_BojY_tBjEY4oLeT99hWdxCZaXEyUy7SaHXyFgBFkcbRv6_4MGP6PvF_lKn2YaWx2_nm49kVUAim4JFR8NifnIhfYNmc9W6t7B2_rM-qDyXpTz5rC2L5n2mHP62pkw41jJJU4EsTYalsyA8BvAysxuQxp3a3TfyxSp6JpNdWTOOUEnk7HkC92Aq_1pgJocmI0WwRBYKS5CoT4guYr_bnu2eqdIbETfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعود بنیادیفر بعنوان داور وسط با کمک بهمن عبداللهی و فرهاد مروجی نماینده‌های ایران در جام ملت‌های آسیا 2027 هستن. علیرضا فغانی هم به عنوان نماینده کشور استرالیا حضور داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/persiana_Soccer/30345" target="_blank">📅 14:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30344">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kImhB8l5yhIB5xhx22Uyw1-rETSup4beDHGq-tTGxi7_idLQagCQv1oSV3oAiqtGYw_wPp4nIJZ4NUAiux5MpbwpN4j7I_ksLFfTyUOGXl0JaC-a-VPlQyQIFVa0TrurlvB_kZPZW_I_eEbbJxbzqKTZ6b0HRHITZIm2-v-8vF4TZqp_HZHD8KoZeaslePywsrLxTD_Huwxx3_iKjkB9d9PbNNi_YUayOq8Iu1a9xcDRQ71rALr0KZKsiuhwhdstEtPVlQiUER1M6nfUps82AOQklMKdan-btdJpb2s9aj4k28IvHLP8C5bfC35nLhKe1Knf_qpnHyKatO9VCQGZ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدیه اندونگ برای‌عقدقرارداد 2 ساله با باشگاه تراکتور درخواست دستمزد سالانه یک میلیون دلار کرده و اعلام کرده هیچ مشکلی برای بازگشت به ایران ندارد و حاضر است با تراکتور قرارداد ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/30344" target="_blank">📅 13:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30343">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxNxfVuH0Z3MhzY9OTu9HQfWt_ft_tIxj4aDw-GElXjq0rpLrme5ko_Ce6p133U239tDLPZV2pnYBTZymB-Rlb7CU-d_NtBil8SCZo2DxecZ-XVDxz_Pe9afwaKD8nq6KYflm0LMWzNbA3TV13TZbzJnvOkQRYEVLsujBPtQM-7cY5WJ5AjIHxDSFI0Ze84r8Yg5lk-zlv11Oi_-PEPnNKM_0md1tiMWJiliN0hdRHGb7FT8nCoqj6AqMIUxdNtz7ECqKbJkr2k80OjOBHvCuVgZ4-IWRVLx9oiIt_ALRf43WS9kwgSpf2UNLnnuwKj_RvFkaQwqXcEh2Pm-1Pwq7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
تیپ و استایل متفاوت بازیکنان تیم ملی فرانسه برای اومدن به‌اردوی‌تیم‌ملی این کشور برای فیفادی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/30343" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30342">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXHQI3rwzIVntOE2VYiT9qfmG_nSOYt88_ZLwh78t2A2BstfV_PGwe-CnJhwQCP2dsZdnPKwHEsYb4L0Pdc4NyGypZcKFjZvZOZWHdme5NWFOTnKrHA_zPPsd9hkPXYpmBs44XIZTXVsXdiUnrCwRQZWcMD3AH9kAgyOEISOcUZnR46czSB6z8-e9oqQDfnuQoX3TUcEcdR06TbrBpS7xCH1PZ1BES3QlF_lQnPErd4OaPvDPS7u8Uwd3MMtWpteGNgKU83F0WKwDdJiJEMRv8DdRffjAoVY9-y7q12sxLQgZ7iYBFhNBD18i_2tx32C-u5y69Rg856W3re4nvI4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/30342" target="_blank">📅 12:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30341">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdp4qWhbV19fq0xJqzGD5KrnJ_dEbWmBV-yAq2R2TzRrmu7GJ-bkrqNgZ9HJ_5K5bgfDoIT5zGV-ZmKhOXr0gXfdIaMe3Dz1vBSnr047K29pnMm42caBt89jTzTfWSYYgq6l_oHxn0dC6HSk2BBxzYwU30PDfgGtjG_TlQPCI6MORfuXbqL5f8IN8cfnvYqRkrC1jWs21X67EvgAfNDz4u4eh6S3ZVzmmC-PXB4cwT_HmnAfipgbqqpwbWgjI7k6GRnXOmCFxQA3pRqzkYM3-g2TP4TxFeujBnO-PjOzbg2Tz156lnVvSXz65ebaHV3Qe8LUO4NJN7eqF9_9gmFCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئالیا:
چهارتا مربی عوض کردیم این همه بازیکن جذب کردیم پس‌مشکل تیم چیه چرا نتیجه نمیگیره. مشکل تیم از نگاه کارشناسان و پیشکسوتان رئال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/30341" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvL0fVMbd3rBp8i0S6p50QEWfiEwZypOfGu54OKyuNoSetYSrxH15CI_xG2LsueuBwAsiwBf0t3gSjSsBlLtQ0WQO6mWZk0WSuDb9cXgmo7Gbt-aw-wkkIPK6JGXFNZ7ZkNzcT44hQLzj2ZUdPUsfxge6QjCeO7bSkL8Y4KzsBK715WYsJ6JOaKA8r4t0mmc-MWcAwUYZi9Z9Iw_5sjLHLHlL83EblTFMwhkW1cT1uZ-f62kuVUAUvUf49E1GODeEdGtRW-aysG9amQa8TiGMe1X9OI59Yrq4lOKsJgKa5WpbSpiaRkkxdjKYUa4GtbqjvrDHiXdWzM7ftIpIT7kNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛ تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/30339" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-8gQYirwy62f_37GxM_Oe1JRtjCMDj2fM5yyovrfxDPTrTf6Xnm6cPCLg5kQc3EFRTYBgKwu0vDWa56BSbo5eoBOCkAJ3l0kGjMekAvhz_MvFyZTZ8P5uLCl9JRaNjhV1H8wWr8WfgXqimUApmagSNeQ0BweDRQsrcihqiF50PjLj2k2vNlQ1sMtjp9FSyX_vwSwrPDCWqzebKMjuaP53Ed6h2rFEefXsNIwsS1oD3KI2-h-71jS91KJ1spd3zqmfccJ2CfmgRrfSQcMMwEq63wnuQli6sgYEGx1KhYsO9WBsmn8Z6nUc6gtiM6kq1Ss5hjchKJFCfMBEdelUcOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛
تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/30338" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30337">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P24_0pES5NMJNJboSXm57oWSzXIo8eCyfjjvWAS_Ar-ogSqgA8kTfsuvvtpWEIaA_EoW24OUvdl-UL4gBhNwulBWS-1FdHfUfsYpFGKta-Au9OK1tjYSo6jowcVndbRuyKQ-Tu36yPcSi7HqxVUHO7IkxzkwcYqJFJ2qtNvhp6FZd6sOqgIVdy_UtGKb5JHH0H3I3jmZCmcR8DjyI90syzFBANDYfBbFxbR5WsrjpJiGeXwPqK8HmOxR5KpLb1sYb4366iqKnV21Tyo2CetNhivddBhrHgIvnx2AaW9wT1qHoa6dkTkv1O4s-XNhMGj-YH0n-OyyfmkUcblc8yFTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رونالدو 101 بازی بعنوان کاپیتان تیم رئال بازی‌کرد که رئال هیچکدوم ازون بازیا رو نباخت‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/30337" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30336">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPvIfhgN8voHYeKwT1VVnIxyhHiv6w3UzCgDrZugUmduLl6rKOIi36l4ee8HInKPYvw9SgJ2hegSxkybe5xTlNxe9XZ2ssg-YP31BeFGNT1fz2xgKbW61Hfvch924daqCvRI0ghrQyv7TcP4X4atk-wthPdpWVUzCsx7H6dV1HxOmCmH0WLCSktpzklAKW7kcQfFDYVZ5Hof-L0lnjCPgmysDugsGwEmvRwmhypK7ugcaOfu7_D6vGdCQtujoaZh95YhbcOFOVwUzXubIn0YqHUMqPnXJqYsdXfcFpl3y2sqr5cQghZNCZ97Dwt_RlNzxe3ghU0qqzeMqWwbHUx07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
میدونی تو این اوضاع بد اقتصادی تنها راه رسیدن به آرزوهات چیه
💵
💵
💵
🔥
سریع تو کانال زیر عضو شو تا با استفاده از
فرمهای آنالیز شده توسط یه تیم کاملا حرفه ای
یه قدم به آرزوهات نزدیکتر بشی
🔥
⚠️
توجه داشته باشید که تو این کانال به
اعضای خودشون همیشه‌هدیه‌ی جبران
خسارت به صورت کاملا رایگان داده میشه
⚠️
✔️
پس سریع عضو بشین چون عضویت
محدود میباشد
⬇️
⬇️
⬇️
⬇️
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/30336" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30335">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw2DgXT2vSL2XfM6E1HlRrsOQhKdFkRye9SgNANgO5Az3a7LM0OgpYmmmccgp7MHypNI-U7MryHhXnIF4pogkqTYa_3QU8VBQqP0eE5fzioDMe04kfPXB1IHImnkfwp9k6Q1D2MYLbsnLbDe5GsyEi4EimaIur4jysghTXupGAimvX7z7M8DTzI_1CzsrdwnkZ1Mbjms_llsadG5-MtXzrTsROyZJL0Y4FrdfcTIBKiOJJ1-l4D8r-TWoRd_DljRF4-S9zXHQnZJsCrB5h1XrH-LkTaWXQbOWg3z0i7R90Smu9-n2UF_ChRhXr8etsdED6T3patXtVWtYq6nShxRBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سابق سپهر حیدری: من زیاد اهل فوتبال دنبال کردن نیستم اما در حال حاضر بهترین بازیکن ایران چه ازنظرفنی چه شخصیتی رامین رضاییانه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/30335" target="_blank">📅 11:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30334">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL9n4w0Osj0hbYxCPWKkTbhQxUXNDuIBa2ixQFjsA35mU2sV1b83hvqivHG8z8iDc-yasCYJmeeDZnmIF5q_Z76DnK0pQUPwZZsfBSG3RfWvOezH_ouiFLa3rcJRJcXt7fGL29c9EfpPVkIJEMq8DEclE-Af6P8YfbcskL0jlmTqFuYBVuEAkLIUq5mXMp-Vgq4LA6CqCgY9QzNZzAgJx_6V6TARe3144R_s5WGh2mxdFvItKUvZ_eAzXzzSjh2plmu2WIuFbVkrUIxuRo2FElOqqdhOmgZlFDOhCrps1zClLRYefPxyK_DUBNWOaiMrMyDR3cON75RKe_mpraZlFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعد از عدم علاقه مدیریت باشگاه استقلال به برگردوندن دیدیه اندونگ به جمع آبی‌ها بخاطر مدیر برنامه پر حاشیه اش؛ حالا از تبریز خبر میرسه که ایجنت اندونگ این بازیکن 32 ساله رو به مدیریت و کادر فنی باشگاه تراکتور پیشنهاد داده تا درصورت توافق با این باشگاه…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/30334" target="_blank">📅 11:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30333">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=WTe69SpMlDwbf6JUloreDX-lcdzgrp-7YKCLeA5SQivLTRYa1AgBo7o8dsgilVhDNxNFM2-6FjRrCNXMHxjhWkmyOjmodPS9pzeBs3gKaN9kqjS4bLzyFixv47rCP5K-ZJjD8crlwbXKw0J-GHA-luiMe-ropcf76cfyzBnzN-aIFCs0w6LV4FEZk7QnxTSZ409QGH9Umf3DOusDgWlIR86GLOgCAEoTDKQdSE4y4yokeVZkbId4qB_7vMU92eDYdMaNcVaDZV_mnDAPVOnhqrF4Al5jCkCIrjIlrQhWv77NgsIM1L-ULQZyceq4x4Yk0Gnq1uIXBQqUKBPFy8fkcjZAgNuyYfknVQg5bv8vY5uPvl4v1_GUf25Cub7yIbavVoelF0w3vSZpeTmI9BJSG0BZ9rgFpryFo-UnHS_fwUyO-zcNBOOEqvSJA_BN8hNdIK5ygzIlE5FvPE9slcqzsZov92Bh9dMFxerOZAXYocq3-YxVqLTWgOSy-tn33ZQl2A5kkYXB_evCgJG1v50YYdV59-rYbNetjxVzSXt2Hl9TA9XV5wr6FMASsJPK6_4cB-loA8GTLrBoo8Io4pqYD7oCXuYE9bWaq9hRrtKp-pEIaCVrMkzigEY1HW4mpcNikJhTLkdjN5gd5Tb3jFYzFyAciFqz15IwtgLYzlGZJbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=WTe69SpMlDwbf6JUloreDX-lcdzgrp-7YKCLeA5SQivLTRYa1AgBo7o8dsgilVhDNxNFM2-6FjRrCNXMHxjhWkmyOjmodPS9pzeBs3gKaN9kqjS4bLzyFixv47rCP5K-ZJjD8crlwbXKw0J-GHA-luiMe-ropcf76cfyzBnzN-aIFCs0w6LV4FEZk7QnxTSZ409QGH9Umf3DOusDgWlIR86GLOgCAEoTDKQdSE4y4yokeVZkbId4qB_7vMU92eDYdMaNcVaDZV_mnDAPVOnhqrF4Al5jCkCIrjIlrQhWv77NgsIM1L-ULQZyceq4x4Yk0Gnq1uIXBQqUKBPFy8fkcjZAgNuyYfknVQg5bv8vY5uPvl4v1_GUf25Cub7yIbavVoelF0w3vSZpeTmI9BJSG0BZ9rgFpryFo-UnHS_fwUyO-zcNBOOEqvSJA_BN8hNdIK5ygzIlE5FvPE9slcqzsZov92Bh9dMFxerOZAXYocq3-YxVqLTWgOSy-tn33ZQl2A5kkYXB_evCgJG1v50YYdV59-rYbNetjxVzSXt2Hl9TA9XV5wr6FMASsJPK6_4cB-loA8GTLrBoo8Io4pqYD7oCXuYE9bWaq9hRrtKp-pEIaCVrMkzigEY1HW4mpcNikJhTLkdjN5gd5Tb3jFYzFyAciFqz15IwtgLYzlGZJbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری درخصوص دعوت‌نشدن برخی از ستار‌ه های ایرانی به اردوی تیم‌ملی توسط امیر قلعه نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/30333" target="_blank">📅 10:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30332">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f00468324.mp4?token=V7xgzg-c6_wyy3OljSieqO_7tb86lXrPytOfTHVlpe42eAucmP-e5hrxQ_ne5c1h_-P8rf3X8EVJ9OgikeSWmPdLJvvEMzO2rA-FTFBCZ1gPpnSsnWcfMyumpmPCkrjCchFQ6f9f37f-YkgKTLC59Paui6FTma5Tk6LC0ZPVjh1MxkKL_YecDIJAdO1YC52uWOTOEbTxjYKwYy5VMFu5KHHlYMIcz1LA0qouyxfpxO79hgtIX2Z_MfW7uJya8JnZ5Ety_uPS2vSlIQr3UB4RxngKGU5pRseKooZAx78sMQR30TjzFEbD5AISU0lrNE2yzNijl9VAErnZpOzvAnri1oYdfxREfTIoHcFKoys1EN0rJjFeZOB2zn4Aib2vwSwA4k6lgbodk9H6Ex21o4NLbCwqQEhuVfWt7Rpuk4rlwJHTXYU9C4jxXKbuKXd9vwZ9276pFDJEsasDDQaiLjEpjfcjAer5Eh62zxMjcPgqjOt2NiyO-IB5oPzeEU6rElb6MCwSihdsWu9gsjMwNNrrDXJmAZoYC1aC_SeKGRveWtXxpFqmZEzArvTWqYflARflUkuiA5SVbxgqCYYOO3CVE5OIdUrlMAOLZIWBHCwAmD7JbD4ykTDRanBHd7CxAYyPfLEx8k9NqMXy6ZtcTJy9RSnfj4lw9mYZm_YU0HTnAkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f00468324.mp4?token=V7xgzg-c6_wyy3OljSieqO_7tb86lXrPytOfTHVlpe42eAucmP-e5hrxQ_ne5c1h_-P8rf3X8EVJ9OgikeSWmPdLJvvEMzO2rA-FTFBCZ1gPpnSsnWcfMyumpmPCkrjCchFQ6f9f37f-YkgKTLC59Paui6FTma5Tk6LC0ZPVjh1MxkKL_YecDIJAdO1YC52uWOTOEbTxjYKwYy5VMFu5KHHlYMIcz1LA0qouyxfpxO79hgtIX2Z_MfW7uJya8JnZ5Ety_uPS2vSlIQr3UB4RxngKGU5pRseKooZAx78sMQR30TjzFEbD5AISU0lrNE2yzNijl9VAErnZpOzvAnri1oYdfxREfTIoHcFKoys1EN0rJjFeZOB2zn4Aib2vwSwA4k6lgbodk9H6Ex21o4NLbCwqQEhuVfWt7Rpuk4rlwJHTXYU9C4jxXKbuKXd9vwZ9276pFDJEsasDDQaiLjEpjfcjAer5Eh62zxMjcPgqjOt2NiyO-IB5oPzeEU6rElb6MCwSihdsWu9gsjMwNNrrDXJmAZoYC1aC_SeKGRveWtXxpFqmZEzArvTWqYflARflUkuiA5SVbxgqCYYOO3CVE5OIdUrlMAOLZIWBHCwAmD7JbD4ykTDRanBHd7CxAYyPfLEx8k9NqMXy6ZtcTJy9RSnfj4lw9mYZm_YU0HTnAkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های محمد احمدزاده سرمربی‌سابق ملوان درباره سختی‌های عجیبی که در زندگی‌اش کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/30332" target="_blank">📅 10:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FpV5xSGqbFCY8qLPh_z8WajL-4xPP9ODVmTW3Wrrwg_nNNikMm_WajcLW5qeh-6oI0U-7r-U1mWWPWLtcD7xpMkVf7BsTjAZC1E5F_fXUlhP56KB39jrBaJP02H_89Qo_ytz-Sflb7DBY925mlbfpWf8xBbMukWxEYF9yBe_Scu6ud0pqZU7jDg81uCx-NqYVG9-_1vFevhiirtHnoJM75npHG9YY2gmDiP1VtfZNZ4ynK5iLXe3RhmWr41b5Aywym8a3r-t_P83taz6w3dTjIHh0CclhVEweL88w97dnmkxIZw0UG-0U4SowBn3VZCXtnebIEVI8S8BUvKG6COYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nysgr97jgw3bbgA98_sT5eJxEv8C9u7k7ee3Vj-w_zFrMnxe5Ka7SaXeu4zCYOkSi5RxKDYgJ3Np7apnAFZ5lNvUhALuJae-6deUOzY_qAWNn5hUIFS_Nuwhwbcji5vmevcXYg9T73mTaEum3rzKHSsIgRzIYqCZChEhEREAZi707rVPYeLIViVLLzFjeqK6hdoMKFflWYgLa8RtFypYNaCg4iwXQy90VtWglg9gEL1s3S1YctElinFKumUcishleWKENZ66irQoYWKC1pG_WmeEuVTdKdvOowFB33aQoVbTSc2lFL8UFqvZPZ_ZWjlxgp36_2PSn7lU9wYt6MjYsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
فلش بک به سال 2012 زمانی که:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد 85 گل به ثمر رسوند.
🔵
پی اس جی 86 گل به ثمر رسوند.
🔵
چلسی 87 گل به ثمر رسوند.
🟡
دورتموند 88 گل به ثمر رسوند.
🇦🇷
مسی به تنهایی 91 گل به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/30330" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=rb0602vtO8wFqzhToBzi9XiaiQfwPWR2wmOBGbg-7jWziT5Cn9S9el5SXZMyHfLLTcL0UFvSQyysIJ41N78Kvb4L8iieVAKZ9n7CokBvFs1HQhSZdxS5Px1tGne7Vjiul5tFGW_gvxJh4Q_PVpFh-ph-DNvZsDIdF9YW-ybKdfu8JQNB59lEKnhdCn6BYOf7LQBK54fNeUYW4_LUOu_m7AbKozbu0ryvDByd7I4YUCdC0k732ZbvesMJoWBTfnIJHhl_JvTv38-VAc-KvZS8u3RN3cUrTovIOfHsDLnf3EuVuB_QZ3aDdxaKcIfnYVM87zG1b3mnuq3HAhKnePaKgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=rb0602vtO8wFqzhToBzi9XiaiQfwPWR2wmOBGbg-7jWziT5Cn9S9el5SXZMyHfLLTcL0UFvSQyysIJ41N78Kvb4L8iieVAKZ9n7CokBvFs1HQhSZdxS5Px1tGne7Vjiul5tFGW_gvxJh4Q_PVpFh-ph-DNvZsDIdF9YW-ybKdfu8JQNB59lEKnhdCn6BYOf7LQBK54fNeUYW4_LUOu_m7AbKozbu0ryvDByd7I4YUCdC0k732ZbvesMJoWBTfnIJHhl_JvTv38-VAc-KvZS8u3RN3cUrTovIOfHsDLnf3EuVuB_QZ3aDdxaKcIfnYVM87zG1b3mnuq3HAhKnePaKgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/30329" target="_blank">📅 09:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWE7e7L1rIWXmKj2QzlvqRPjDjta7gZ2-rUBU9UwMLx28zaZHxIGo9BwZ63MKEUtfXP6wXW_mT1RXp27VeeDVDAK3lNGEhWfBOiWZTa8t86HteuYDMScE2S9ZNsmUJi6cx9YE8xMyWJYszj9j-fIK_o2Xg8zGh3hLp-LSnloN78irKq4lgAwQnBQHqX_4H4wd1R0Vz7FX42xYu6ENU_D6-nGn3Yc9WU0fVcs5OZ-Q34QOFXJ6ryLwmk7QAPjqVZqu8vaRk0P3nuUuYbCedh8WpT9CgGG19-mI0gqIgaBQqmse6plzAgpimQgSTPmIrkBcfgedaHqbOXbZdx1VPb3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب ستاره‌هایی که علی رغم درخشش خیره کننده در دوران حرفه ای خود توپ طلا نبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/30328" target="_blank">📅 09:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky8pdZlFdpikM5YYFFJAwV1L1soiCfFc1pcCsB0Nl-Gi9eEvVOfR5ZkLaNo8UX2aIF7k1rdXnHJA14zyCbIZQNSnKMhjtmKJsXwvsmFlXRbxiFVHoBTosqHmI2WT53IJJbVCPrdxR6IyYeN1J227VdmSpJAh7OtBQYw9B5ZD6aiQ3P0hoEaxbSCzNlUFzR8YzL3n63lZ4TE4bWxf1ddrkft7NDLMDz7LCD5TWS256F_qR5qqSQwcVSgWfu0npTshTKob4bnWp1hjsx0LR3u2Sp5lysqaOUiZKqbwJ8BJFJ85CD_z9rDVRpg1kI7USg6J-7DQ9c2KDfBsAt4AjIIRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30327" target="_blank">📅 01:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPIjtwh7uEHvnAtencPEl-eoV5nYoKoimUZhD-CCdkyp_EX-VDVjAop1IJFOFshQ2ruE3K-FvQaDfZ2F4BygEhp9BW3hKRZhDuMwDrp_YwAyDyvGS1sTqRaQdWe3DRzyJe6Pa-dq7zVFEb5-p_qJWRFqkkmwnfwBzgfGJGT4dbpiWuOhhjyR3iDWLqX8c3374jfaG47_RRgR6aQZJ921OSBjEvK_dbzX0X7bnlPDdJUU6BCwWops8AAhBR8zOCZ6HBnGiSs0lWyMdwj8OljZF_QlwrTBsBDXFSb4obCV_PlG1xUYMluG2e0ofZ_5G8SbqrZtzqta0PuXf35zktjUkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JV35uMZa3OBfdZHfkAhRMuwyNDUPGJmbgCziJUfJznQIbvpxpEwpBI06aRL4JpD_KRR0nnJA_JlueXqgY0RWe26mME5gxlKTXIir9H6uZi0JjSkBClifixUzUBr7ILiBashO75a91fW1X1_IjbmnZftqgvBY9HgMWtI6ielDoheY5GhvHi8bm7eQZ6rVs2SpCdnvsVSRIFMcE5jsgXgl6JG9zEIWkgCB2C-zCPXPDE6xydgTAwlhocw1sHpSZskqRPAoHTWhABLEbtNqDo8kYycOkDMhRJgBZSoZ4Jt03qcdQ1kkCx8oNjrtvxpeb4tQJlZgPSaiVQscqPLeOHucnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آخرین رنکینگ بندی تیم‌ های ملی پیش از شروع مسابقات‌فیفادی؛ اسپانیا بر دنیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30325" target="_blank">📅 01:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=TgZZFMLNBdt3Ed5Ptj-GmwXRjSMQ_COhYhndRxoU4wkpEkZDo_08wejYK-5a0vJO17SJSKNcEjXRVUYy_ES1F5BC1AjCrOVKTmsLj0qw2Jfk3KflD7sa2h5uGO8YHD1C2zYQqIHJD5vQdMkRRc5Lrs3lAwYLhm7z3nnDpOU8ba119iiikqR7wyXv3BpvhCSHsMx76smfnu5I1lnfz2HcRTgUuJHxFH2hoz5E_z2zRf11EVpdmM6VEhBZIOojAngS8uNayWsDfTGntkuPBqJn96KAbOJfJYmK6G-YNWtZwwlQuNfVP3dH1n6gKmqy709AR3AG7zh-6ToZGncEkX-spg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=TgZZFMLNBdt3Ed5Ptj-GmwXRjSMQ_COhYhndRxoU4wkpEkZDo_08wejYK-5a0vJO17SJSKNcEjXRVUYy_ES1F5BC1AjCrOVKTmsLj0qw2Jfk3KflD7sa2h5uGO8YHD1C2zYQqIHJD5vQdMkRRc5Lrs3lAwYLhm7z3nnDpOU8ba119iiikqR7wyXv3BpvhCSHsMx76smfnu5I1lnfz2HcRTgUuJHxFH2hoz5E_z2zRf11EVpdmM6VEhBZIOojAngS8uNayWsDfTGntkuPBqJn96KAbOJfJYmK6G-YNWtZwwlQuNfVP3dH1n6gKmqy709AR3AG7zh-6ToZGncEkX-spg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل فردوسی درباره زندگی سخت یان دیومانده ستاره 19 ساله رئال مادرید در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30324" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=a2IPuXUHjYFTgs7KLUWiiwo4NbDpqXfH_WXVD_PAKgejupotX_D3uGnpbFP-a_WTzccUashlh15gB5QqW3IBjwvIenqesJlqVJxrzz5-YyIAG1wQLGwCJiRm7bXdS_Ot9Wb38mmajcYajT1unXeKx4wxZbN8yCaF2qHzm2BmjlP5wu9pFsdstQ50ttn0AvFb9gBJBikWYHs5RbZhBx8K8wAp0nNj3eSXiknkPZhkReo9RhNb8_dWDCm1gVeEIfZ7lGHynftgbgtxUgCd8m_ACd4-AszG88f3ZavMrnFV82jXK0WCwTp-arCRdJ_Wb6vrZU_mfmfwN8478iuKz2Vw0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=a2IPuXUHjYFTgs7KLUWiiwo4NbDpqXfH_WXVD_PAKgejupotX_D3uGnpbFP-a_WTzccUashlh15gB5QqW3IBjwvIenqesJlqVJxrzz5-YyIAG1wQLGwCJiRm7bXdS_Ot9Wb38mmajcYajT1unXeKx4wxZbN8yCaF2qHzm2BmjlP5wu9pFsdstQ50ttn0AvFb9gBJBikWYHs5RbZhBx8K8wAp0nNj3eSXiknkPZhkReo9RhNb8_dWDCm1gVeEIfZ7lGHynftgbgtxUgCd8m_ACd4-AszG88f3ZavMrnFV82jXK0WCwTp-arCRdJ_Wb6vrZU_mfmfwN8478iuKz2Vw0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چالش‌عجیب‌وغریب‌امیرحسین‌قیاسی در قسمت دوم برنامه جدیدش با خوردن آبلیمو با غلظت بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30323" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30321">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXbLZHmv2oNoLuDyiW2eqb8b_XRnHzvKvxWmS6QBpvfeN3ZpVC5EpzQYgxUj-Cfy8AKeyoDkE5bBHUo6_eyooyJovQaAa8bOCjrYnf9CuznChgsw7SYV8xqPB8eQbjUPK7e_1vV0J1lhlE6PagBmhx27yTlrhdmCmKjHfKDfEwlqvr-2QTXnQGnGz82RM7T0DdUkpU67dP9-0r3PAKkKNuxxwHoPsKfalbMn55Tmr9RBunv3BMzwmohig4i58p0pdqSwcbw7b24XNhN6rgI0dqWW6Plzv1zJeXSbTZuk1Z0rpkDpFqckHBTqZ3KWKWeYneNHuX2Oa3wPZT-3FUdKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30321" target="_blank">📅 00:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30319">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY37bJT0LjFJWQEvaCJkMefm0IjdiFDbWpehMKdrtZ36DzP9s160-0vQ8rqXRAAJv132J3cWmYsY74UgtiArcRnG-IXflAKwabRRUc7XnqjOD0KOnjWEzMyCTnZsAIiTfgvlCwTKbJwn_fhoLmojImoq9RbFlcEJer-kink-eOo9qQiSkFcZ7UZ4MuOzb9dMNlMoYz1ZCkk2UQU3hlYaOAvfX8njzf8RC8-F7jPUJXseoKbwcO2m4ZJZWhjQp7Qs4N8qkCk0wutkk6UtPlq7PDlwwQrNLY4Efl6WcXd8XtchmxB6K_5a2Wvb1s_ZOYzdRwYaO6ED7n1llJw8NH96OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30319" target="_blank">📅 00:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30318">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8eN1SJxjFQzHdy23r21Qf78KrUc2B7vHjATcaSiJ7mHkadZyWHXtvMLW6FAdS03UwcwKgyZ8_ciQYPhpT2etL5jCepPbKZvE_qpna2sZFX4v-PXDAJBKpwempjxVSMFjmJ-aXlR-8kpJfoj2eA5LYCu9W_ykrUOLMQSZaAAfAy4qBGRp6EKhgpiJmvNzwR3LkNn406JKGILgbzLWhgwXj7nNBl2pP30zFXK72kd3TdwtGjaqn4FhZabiGriEAj16U1sJSvBQON30nzaTfR-VdZ5Qft13osX-_bunSklVOFn4trV1KgKCweVi053PaGHAWoqDLe7FdcoYhzyQBKN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌‌‌‌‌‌تنهادیداردیروز؛
شکست‌مفتضحانه تیم امید مقابل کره و حذف درمرحله‌گروهی بازی‌های آسیایی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30318" target="_blank">📅 00:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkqWrJhRADvI3RkCq6vo9VG6fKY6AJ1ke0xmEMxSBan6vMfL-ap0J0b6HdgBug6vnRz7xeCf7EbAoDP0lQKAr0HqnW7Bo7ZIH4uFQEtvXtOV08mg8sF_Z3nj46EavjZfEVPjonhuk3-5Giild7v4ihcUkVWxngs9kAymp8j-GAcooMfrEuUHme7Dj3hsMTrzUj_RtkUFURUIA63eqFQouEUwLTEN0HviyCHkYeFYYBxjYlJf_WxNEUa8quNwbiF-Npa8jWZk71-QG2w8qlwrb8ksGDwJpHmlTtD01y9GMG8PEOlySeoTCcihMAJotWYiDRKV8Awj1xwIxv631RwRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30317" target="_blank">📅 00:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=wAnzQ15Zsu3Gc67BrykscggyzT8TWfMR4NKhhurMr446WcW-yFQJZrHl2REJtDc-bGTDXOrR-Fh8WEAwmdSjugwGbihzWstqgO_QUtQCIhrwgxegKmJqHCjsSAFde6g6MvwE_lbD2XTKn8JzFktYaMJ0PymXJ573slDEC5TscXpHMJ6Wjbuf9NjAAxZ0TTKxG7TTeZ48lj5lOzmHBW8Reyor_9awe_OKIdNHjC7bbpmKoy26a2ZMjPmHmT6chKDKww6nHpM9ofPEDiboYSeb_Y40jCsQ5WXx4U_rv1WoYut3TRKA8f2hAxy3r_F68nEB8S4a1YtqVEmnsaBtre8fZY-W70ZovSOapHMRBY-d9awL9cN9PlCL_QIfazhiy8H7f3Dyy84Rn3koFGSbvoRnGzZZFV23IseL87TcLHLb4NRmRXjL5BhZ2F2qAxa4AnV3Kd3qeInU26WADxETb-Z5PIHWd2mIIQ_NhzjMCKo6xzKZIYoU8SejXU_eW72PBSY2qJ_4JsveQPe97U2LiZ2WX577JodMZ7Rj6CzvZQR6i3KR6vddIw_0_wx_vYECStEUn3VCntqFwuBMTYF7tUCmKobLpIeAyRjEPUzX5Z-0ZK0p9kFEq7izZ42BHdoyi_jI2MtiDaRDZQRAfNVpBRGFwT7TFX267M3hFTiy2P-5fd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=wAnzQ15Zsu3Gc67BrykscggyzT8TWfMR4NKhhurMr446WcW-yFQJZrHl2REJtDc-bGTDXOrR-Fh8WEAwmdSjugwGbihzWstqgO_QUtQCIhrwgxegKmJqHCjsSAFde6g6MvwE_lbD2XTKn8JzFktYaMJ0PymXJ573slDEC5TscXpHMJ6Wjbuf9NjAAxZ0TTKxG7TTeZ48lj5lOzmHBW8Reyor_9awe_OKIdNHjC7bbpmKoy26a2ZMjPmHmT6chKDKww6nHpM9ofPEDiboYSeb_Y40jCsQ5WXx4U_rv1WoYut3TRKA8f2hAxy3r_F68nEB8S4a1YtqVEmnsaBtre8fZY-W70ZovSOapHMRBY-d9awL9cN9PlCL_QIfazhiy8H7f3Dyy84Rn3koFGSbvoRnGzZZFV23IseL87TcLHLb4NRmRXjL5BhZ2F2qAxa4AnV3Kd3qeInU26WADxETb-Z5PIHWd2mIIQ_NhzjMCKo6xzKZIYoU8SejXU_eW72PBSY2qJ_4JsveQPe97U2LiZ2WX577JodMZ7Rj6CzvZQR6i3KR6vddIw_0_wx_vYECStEUn3VCntqFwuBMTYF7tUCmKobLpIeAyRjEPUzX5Z-0ZK0p9kFEq7izZ42BHdoyi_jI2MtiDaRDZQRAfNVpBRGFwT7TFX267M3hFTiy2P-5fd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برای اولین بار در 47 سال اخیر، یک ژیمناستیک‌ کار زن ایرانی درمسابقات‌آسیایی شرکت کرد. هنگامه هادیانی؛ ایشون درمسابقات رتبه خوب 13 ام گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30316" target="_blank">📅 23:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIRtoz-P3TNbusXQegTm-fofbC_PzG4W6_fjj-3liYqTeHWOITsg30JGFd42w1e_aftbjWCwf_0k90qsoNqKuj9rV1E77n_-1VmDufJet9ldoLxpH4QceW5f_grneaCri-eYsJgy34VvncsVN_X7vpceAT67WlN_JoeB6Ri4DdEtBBKA58NL7WuEX-m3QCqm8YKMpUIh6KZHbfN-jJjX637FdE7-IyHURTuD69BVX6_3SYxxSdsegMouW-2f73kG7EoPBR3liHzUTGSyUjHFE8h77Fc7d-0lCgD_nXWDLuyNet11wKmsGb2cfyPZNy4sfzi5L0PSaiBIVhBJdwSKww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
صحبت‌های کریس‌رونالدو کاپیتان پرتغالی النصر درباره زدن هزار گل زده در کل دوران فوتبالی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30315" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30314">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpk-ckfddWqn0SVJ49mFkm7IlcuclJ8K5qoNxTaDdpw_37R15SPGW8MjBzTCO-aW36mRiBsdDp7wVqozPUjaQHqDCbMRzY_vLnzXWs7-pBNCzps08WSDnBzDeJfD3cnYFGYIOjONYLQg3R3i8P5AauS3OTx8Mm8LvsY-APS0gPEcbv3Z6SbWsFQDscgwBbVTwyx0F2iEZdIzBzUI6xv-fWQLcSGl6cDiAqpP4Uxpbr6EVLZixf7Q15QGkbt6qojJ2YPgVZB2qpyYHbVlxeVALxr4ZmQiJHxmSmBq2YCwSzWeYvyA2tvgHparmtLZbb8NtV5LJuDu8tiYYxBOmIguRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30314" target="_blank">📅 23:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6C4ewsx1jMvVZfEFBufbolFa6MATw8TbRCifLmwm5iB-wNw--hpkcG617DXwjAeFqOnvEN9GkxD_xTHnyPkgDUDuHw1AUfPy5FJe3CdB-BzJJM5qq4pHecivglKqYneml0XkljPYIaKLZWRNCQXl3alu02TQsYG2XL_YIx7gMl3sftw8YRC10BZQfihswEeLiQutpYay9ouP5na0D9KBlMm4KOfIYzZYcf65j02eDQYR6-wdw7GsXZGQEFDGksNjrGnzOZnq3EqCrAtexel2udKSW4CLfeICvZXoBiRPSguLB0J1E_g7ojnpHPdTHMO0V1f9_4EA-mpgWC-PuWrhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال: باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30312" target="_blank">📅 22:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI3okQLUpKvBDEXx5ZFq2ws74Vv-T0Vfu2yDFK_i8ES1QhnR28dmArTebQlNVqxb5ZInlof8AUIshCebOSp79OkfhkzXNVtBNYzAgfuf7D8Ja5LHrtbXSWcouot2j8gzDW18ZCuWtcc895MScCJLqqPNMbHCkL52YEcejpatkgRWrAeqfwvv3YVNElO0M-1G2QBW8WSB6hVN7KiucXmm1cwtoQgxjVhXDRXeRDh70PUZRSUgdNH5ph1_914RYlbbyYRzluIPTn0ZQzxLsGHTmXpqN3dyESDAzC5KDG_hi7c_YYBeEYXN5a6DbmGJLfFdRDHxFXJ7hhPj3EavUI9CAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30311" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=AqYlFfS-igmH97qa7HOEHjZVgT0brqrqih6TFM7SKU2vVU2ouEvjG9XdMLOVaT2GBwDiELkDMdJ28XLEiwUvbggnpw8Y52hbqYWyrG2rSjoFYqeP47WYVujDOxHU4NZRWxvbnGK4eaqLmFXWosp3u69Aw-QhGJSPCSgE-tDKF9DQQzTl1V3l_1QC3qUWFNUarSe4JP9wBsfDycBsorujJsS2puVl_EoHVYCxS_3843HCO3IVgGgUJBCG1mTMQB_x3OQoV0Me1PDP2xgMtbhiLDOfCtPJcWKROPQLrgSZLjWhIc0pBE_yj9N2dIN7NAzN6HaAeCF2fEDtrYTV7A6b2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=AqYlFfS-igmH97qa7HOEHjZVgT0brqrqih6TFM7SKU2vVU2ouEvjG9XdMLOVaT2GBwDiELkDMdJ28XLEiwUvbggnpw8Y52hbqYWyrG2rSjoFYqeP47WYVujDOxHU4NZRWxvbnGK4eaqLmFXWosp3u69Aw-QhGJSPCSgE-tDKF9DQQzTl1V3l_1QC3qUWFNUarSe4JP9wBsfDycBsorujJsS2puVl_EoHVYCxS_3843HCO3IVgGgUJBCG1mTMQB_x3OQoV0Me1PDP2xgMtbhiLDOfCtPJcWKROPQLrgSZLjWhIc0pBE_yj9N2dIN7NAzN6HaAeCF2fEDtrYTV7A6b2DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های خسرو حیدری کاپیتان‌سابق تیم ملی و باشگاه استقلال درباره حضورش در سریال پژمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30310" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETe4zAZsiuf8XA50eZ7n2UayqnpYFpOF06ljJ-pdGJunD-dfKJr8fyybwUyrQhSBitKBeRDvnaTP1q9vG3dG6UQKgnn2XxkwmwHZGVq5QCTlTBI5mwM_fYcfZXTrVYfdLdP3vGPC_4Isn96pwjz16PN0Oye-8ecaV6LZZ5PxWpR0XRtnK-Y9XnW7trGOXGWt3590b-Dj2SfdRSrUEYm7ThbNHtIAJqsBzqBTMdhHniayR-a6NxXMKRpezezSoWGMMZPzN-bYvsMVnzIEYKZI7D9hJHMyyWV9eC9cS8_5MCY3239zCFHmscnwqFMCek_7Fy0aI2pATT4YlTPJBadnYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرامریک‌اوبامیانگ‌مهاجم37ساله‌لاکرونیا امشب به‌این‌ شکل گل پنجم خود را در فصل جدید لالیگا به ثمر رساند. انگیزه‌وچارچوب شناسی‌اش‌خیلی قویه. این 414 ام گل کل دوران حرفه‌ای اوبامیانگ یود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30308" target="_blank">📅 21:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=Y1DDz7Knckk2OuYD1Cexyu5EP6E-IG_o5_f-PxnHiHWJOpuZFfzs8oraXggcl5Pzh5MVLsDPEkXsBE2AnnFaGzWgbp0KBycQanu8-K53OjhzPdmI7pw5Y3uSdNF9rav0bOrQPuv6YAUOb9er8Sf-g5ctq37_4K7_XNRSwRoYRDqBDblpFWAs0ITVRO5budP44s5u7Z6KJhD6hSMvFmoYRCN1GbwmGrPexN7MW6MZsfNRKQi2UOUArb2d7o2dKxr25liVhH92v5noVx4ijznFchjxiftrXIy8preyV3lGtnx0zRf_cMp2id-3PI8HeO6IcNeB4g9KDwUBUSmCBW99Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=Y1DDz7Knckk2OuYD1Cexyu5EP6E-IG_o5_f-PxnHiHWJOpuZFfzs8oraXggcl5Pzh5MVLsDPEkXsBE2AnnFaGzWgbp0KBycQanu8-K53OjhzPdmI7pw5Y3uSdNF9rav0bOrQPuv6YAUOb9er8Sf-g5ctq37_4K7_XNRSwRoYRDqBDblpFWAs0ITVRO5budP44s5u7Z6KJhD6hSMvFmoYRCN1GbwmGrPexN7MW6MZsfNRKQi2UOUArb2d7o2dKxr25liVhH92v5noVx4ijznFchjxiftrXIy8preyV3lGtnx0zRf_cMp2id-3PI8HeO6IcNeB4g9KDwUBUSmCBW99Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس رونالدو: ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30307" target="_blank">📅 21:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30306">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr-IiGRDXsf7xhxFE5caFRPUqGvlFwM554QaKSOf4FO65iHMH6CnkCsiLdJHr28GnjqJxS1EXbfQHyhatmB13KCHpEmZK59GJ0EXOkXvQYnEV8XwbHgLK_k6ucOtcl_kCZ0UuGe25027dOjOYwXLVbWI9gXxzn7EqjC2ZNL7B8RLKSze7Z9D6gYeFpiVaFIFeajsBpSu-9vf0fHDUMYOLITb8CyMpyyqHyM37GPLKnuwzFg70z348BdvPSSdpUlgXqso3rb4GLSyZZ-RL2R6I1qVDXqoNMaKYadx8WgzgFZmVTqMRffAVQdGX1J6wuVNDdxlzBygCGIWc9HxX-8K3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بهترین شروع مهاجمان بارسا در تاریخ؛ رافینیا با ثبت ۱۴ گل و ۳ پاس‌گل مجموع ۱۷ مشارکت در گل درفصل ۲۰۲۶ یکی‌ازخفن‌ترین شروع‌های تاریخ بارسا روبه نام خود ثبت کرده و مستقیماً پشت سر شاهکار لئو مسی در فصل ۲۰۱۱ با ۱۸ مشارکت ایستاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30306" target="_blank">📅 21:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30305">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cb8e0zelytJ4mMqmGsaOEmEiQbkVtUKuymjq6Z5Dm_88rTFBz4WhwCrRfhlQdmkVhFDTuNIU47qZrcyjbM5guER_75OI7imhxiVi25x2B76MEK3kdeY27egArbmDjroz0E62sUt47uORqx4fYD-8krpA61lFNrPdpRtZkd_FzvgBoB9JEdnNqRVr9glQUUkLUDk9dVs3i2El0bEsQV2xFTWip_6aNCUs1p4dvezgJ60cGuHHC7-3wD-Od0Kvn_pwGdH9q7EyBgSQ-XdJWO6FnDD1BkmYWJ3RwM75js7844oVobEBjdyYkeEr21IrTDw41dpZEVenqmVWXBBKRXSpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو:
ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30305" target="_blank">📅 20:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30304">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
موزیک‌ویدیوجدید ابوطالب حسینی با بیت کاگان منتشر شد. خیلی‌خوب‌میخونه لامصب حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30304" target="_blank">📅 20:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30303">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=Z16NiLsKlxZzaLouKnIHLfUoz29lZ09VDUwnhBB4RgqjHxAl8L_iSnApgOQGqhWpDK8sgAgpQrtdwuUKm0ljE9Wy4HJcbe1x7VGmDYQptXl0cntIMt5BIYtyGQ32qT5zr8zqaEwMwWCiQBkyz3v8jUvilW1uf2jCJ9bYhFEuH4kSSleu3E3ha8ACQ82cWu2vc6HfON5a3sxJhSVvJB1EyFEi8Fy2FDnDQVQrlCyAtqJsm6U9dXlu45QCw7G6CauPexHsLAfuzzvhM-oFzVqwvTu5Zcg6IN9PwyMYilSWU8PdrsEwrgahqMFhkF0aPYFcmtsBrhMc0GnVXP0XE-zJQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=Z16NiLsKlxZzaLouKnIHLfUoz29lZ09VDUwnhBB4RgqjHxAl8L_iSnApgOQGqhWpDK8sgAgpQrtdwuUKm0ljE9Wy4HJcbe1x7VGmDYQptXl0cntIMt5BIYtyGQ32qT5zr8zqaEwMwWCiQBkyz3v8jUvilW1uf2jCJ9bYhFEuH4kSSleu3E3ha8ACQ82cWu2vc6HfON5a3sxJhSVvJB1EyFEi8Fy2FDnDQVQrlCyAtqJsm6U9dXlu45QCw7G6CauPexHsLAfuzzvhM-oFzVqwvTu5Zcg6IN9PwyMYilSWU8PdrsEwrgahqMFhkF0aPYFcmtsBrhMc0GnVXP0XE-zJQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30303" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30302">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=U6n3sKQblTp906xmupJr0Vhy2SA0yni7iNM0A4p1RW91gW6Zc1kcW9kb1tAOB-2ASNsEsIoUL3PAtR3kk_qrguigbCmIa2Exlk5cxTf7FPnSVcrkt5WH7VdeVRcpOfRvCRjA1R1tnE_jyZ5NRpVoL39gff3K1oEgvGHuf4dpameH3P1-z0OsGUDBRmxQuDJWlRexkECMj3QdwmEfPiENVeJRVhY8psPGy3yfxhhTXPBb3Lrn_5ux1oiO8XhEKbP82Geml4EFHbzNcKbgWPiee1Ri_zJfL_IftPNJ060aH48nipe16cghY9czQHUaaDtqF3Kmr7V4kJjrODps2QlbDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=U6n3sKQblTp906xmupJr0Vhy2SA0yni7iNM0A4p1RW91gW6Zc1kcW9kb1tAOB-2ASNsEsIoUL3PAtR3kk_qrguigbCmIa2Exlk5cxTf7FPnSVcrkt5WH7VdeVRcpOfRvCRjA1R1tnE_jyZ5NRpVoL39gff3K1oEgvGHuf4dpameH3P1-z0OsGUDBRmxQuDJWlRexkECMj3QdwmEfPiENVeJRVhY8psPGy3yfxhhTXPBb3Lrn_5ux1oiO8XhEKbP82Geml4EFHbzNcKbgWPiee1Ri_zJfL_IftPNJ060aH48nipe16cghY9czQHUaaDtqF3Kmr7V4kJjrODps2QlbDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره مهدی مهدوی کیا از قرارداد یک میلیون پوندی اش با تاتنهام که بخاطر سربازی او لغو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30302" target="_blank">📅 20:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30301">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=jvITuig-2B-OcVBKQPeaACGQQBbswBZrewl8Nhqipyl9fBQUuCAIWogO_vu7dfqleLw-UggOewgE1kehjCGFRlYoTM9ozpctUM9EZu8tnGFf5zlrkSw5n-WSO6J-mYu6ciM2DcjbJ0m_bMxbBsis6EA5V-JcX93t-DOPNUKn_uh-3FlnAtH_uZ2yBFMoOGlanw63us7m7cM6tsukj8vUctajl2icHjff_n_z4184NBjDKeztNSrDit98SQ3_XTMuhYv6H5BAyLgH5iX5DBlEWbH9pqDuhsaLyHxIWUVqMdusj_WcGDcdiJ9wE2nMVdAJCvnR-miQ_XJOwkUhvV9SewZagqgV2ovRRRKvj-g0UOd9g7bYAjYAETXtnPgChBH51Mh_VAE1nZhQa5byRUPp3UZZVrRwJV4C0hfCMkg3TBwZSsRaG3fShiVpUI1me46EpxLRlwhy00yZqEuqQQh1gWzsTIavnJfejGbqn206l18g2JwQSITd0U7PkvNPNB4-WukM61loI0zy0w5pgWcgVfm1q4IWGxaBL_IyuSMTnp1E-5IIswc0QZW2raC-TTREtgx1jSxKGSgt84T_u0cL3yl1PbGPYiwsXkooZRYJgi3CQy7q5jQro_L-I3rdUwYBh2o7hS2Lh_Jr_5gTy5jlNagueWtd9LSjNL0NedA-NlU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=jvITuig-2B-OcVBKQPeaACGQQBbswBZrewl8Nhqipyl9fBQUuCAIWogO_vu7dfqleLw-UggOewgE1kehjCGFRlYoTM9ozpctUM9EZu8tnGFf5zlrkSw5n-WSO6J-mYu6ciM2DcjbJ0m_bMxbBsis6EA5V-JcX93t-DOPNUKn_uh-3FlnAtH_uZ2yBFMoOGlanw63us7m7cM6tsukj8vUctajl2icHjff_n_z4184NBjDKeztNSrDit98SQ3_XTMuhYv6H5BAyLgH5iX5DBlEWbH9pqDuhsaLyHxIWUVqMdusj_WcGDcdiJ9wE2nMVdAJCvnR-miQ_XJOwkUhvV9SewZagqgV2ovRRRKvj-g0UOd9g7bYAjYAETXtnPgChBH51Mh_VAE1nZhQa5byRUPp3UZZVrRwJV4C0hfCMkg3TBwZSsRaG3fShiVpUI1me46EpxLRlwhy00yZqEuqQQh1gWzsTIavnJfejGbqn206l18g2JwQSITd0U7PkvNPNB4-WukM61loI0zy0w5pgWcgVfm1q4IWGxaBL_IyuSMTnp1E-5IIswc0QZW2raC-TTREtgx1jSxKGSgt84T_u0cL3yl1PbGPYiwsXkooZRYJgi3CQy7q5jQro_L-I3rdUwYBh2o7hS2Lh_Jr_5gTy5jlNagueWtd9LSjNL0NedA-NlU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنالیز دیدار هفته‌قبل دوتیم اتلتیکومادرید و رئال مادرید؛ ژوزه مورینیو به‌این‌شکل‌بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30301" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30300">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErWr43nWAsPgzYIvbZ_ng5zQrLJzSvFoqKNd6nt2AP1E-GVthocd3Qq0dg9mTDP_aV1gkSJ3IGu0uMu9Svxf60M13fC--TT0gnJSKGnqf9dsehihLig2EKlHBQSFgD3oiMzy0vt461knstEWhfh6I-KXMW3iW2tjatMQbaaE_BmZzzgwO3J4k4v__RXhTJVaC5Ag77_oAFFyjK-igWGRXiM1sFJADtj-7Z_7R7SCHjXwm6fElm9xNnxJq2UMPewewEjd56PWiGdKTkf8RK4yW7CiiKfLnD1LHqbZKe768fyJAr4-d8OGSbkJKgl6U0yIvlo1IsG9CS8bESf3FInWA2yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7539f4c8be.mp4?token=Pkt8NG_JHNCXVqEG5gQtvMHwo8GW0g4wgogRi559MHEgPKw_0SPK1BUBsJJePoTv4dAifwfqqpjDOv1DGlEt3ZPQwP9kre-6aQFzWaHp8uq3tueg1r6UtRmr7_QhdMEjwzRohxV-Hf7PdgmqHYerYvfUegvBCP0WYCjrZ-wFTYuVU-QouyzdTq7dn5dCffaKmXdvzZeGClYla95fILP9j2wqT3DsQWAUtrur6BJ2_4M7lMULtI8sS1VxRPEVGumdnEN1DVTF5Hp27-U9sr0yApGOTv5ou5dnLWdiWbHYG3e5kvPZDbjeM4AfZ0LwNd75d7jFcnkffXH6-yiKHuIErWr43nWAsPgzYIvbZ_ng5zQrLJzSvFoqKNd6nt2AP1E-GVthocd3Qq0dg9mTDP_aV1gkSJ3IGu0uMu9Svxf60M13fC--TT0gnJSKGnqf9dsehihLig2EKlHBQSFgD3oiMzy0vt461knstEWhfh6I-KXMW3iW2tjatMQbaaE_BmZzzgwO3J4k4v__RXhTJVaC5Ag77_oAFFyjK-igWGRXiM1sFJADtj-7Z_7R7SCHjXwm6fElm9xNnxJq2UMPewewEjd56PWiGdKTkf8RK4yW7CiiKfLnD1LHqbZKe768fyJAr4-d8OGSbkJKgl6U0yIvlo1IsG9CS8bESf3FInWA2yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 88 روز از این‌ویدیو تاریخی از خوشحالی مجریان شبکه دو روی آنتن زنده صداوسیما گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30300" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPufOWyrNYxBjfUgQKhEnyxqrIiNe6JPbDJ8b4Z1CHenU7q2jnmeZmc-TyUlaKLDiUv7xR6b65S44sB4E_Q9MJhYChEJOiL-PyhlTk_IJeaY6yTAD7Ykw8P1t4qIt4-aKLkASzVQuAF_l56HXW1kWASiS47RYr3BuD7luSq3SuuD_HEc2NdygXZlhBPRsImbGbOXH_GlxJ6FuthX_xkFLpDobsFApijsB_JIezdQyTbLePCyC9xTsiF4U_NLclWJLgEBun3PUuR9dlZ5Js57-ISOJpfv2-4x1imYHzaonb6FQT9-ihuXcVehX6BltjziBY1KpT2eXd8Cyeba2pi_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادگل‌های کریس رونالدو و لیونل مسی قبل از جام جهانی 2026 با بعد از این جام تا به این لحظه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30298" target="_blank">📅 19:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbQ6mamsydrF48lmLl32XcaQ-x7KS2kQrt4hqDfu5FkcRY0GO_fouNtb44gnD8YePC7BOlW02wCqIUYxZMcwI6U4b_gIGjSzfvp3MLYnVDjv9bzTFNCSIrxah9qbyUypeJnY8cHSSUTInzY6RpQAeeVtS1rrG9m_FpZb89Fft8OvJC9Qff0HeVj80XaKvdVfuXBcZHGilx8wLkIBP8aaR8q08xvnXdUBDMC58ERQRj5jTRA-cIZgvH0y8PKYj7wYcXUVoSDki2w-6MrsuAKw4u64kgUFQ0J3LjnbnrvSGUbNHFqsDdng79XdzWCD581tVrqi_RLRdLej4r51pKC6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30297" target="_blank">📅 19:22 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiGDuBkYnJWEnNT7ph4FHBsL6BBIBwDGtGf6dR4UssVYklQ_hJ7UkKr1GsFGGv9mj1aAwkv_M3qMaOmQO71PDfTxo4quI3KoGWiUHHGTuHVEHdrqq2xJq5jwI1F7SK1rloQiW-p4QbCXfVPaCc5Ey5wLxQS15ul4I2P95lM4b59SC_qj9HNerLWE5o1CGek3A3DOLiT9fIPw1ODDmFnl-lEVJ7fdjXH4TAp33IpDNgFkiXbu9K2XcX1nakytbBS3EbJ0nSoMKwL9ayoPl_2yLt2hvyGxJ1ibbQg96pmyKqMXDNGgWeX3aE2paq9ejnuh3aZY8TCXgHpGbrKRYpNvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30296" target="_blank">📅 18:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYz-uKNQN2a2MfKKjrxb1c-CNGuuGvSZp-W-raNfIH-bQJxU12aLl8GivqJTn2Vjk7NH1D797jq8-rC87VuQXHfDl0Ojmcpzlrg24lkVrfcRebztuveAzGOdca6zuiArnD58dFKBgSiMjhr-801UkdGqtTc1Anx5bbS87Unw0HSsSWWKT_wYM1NQWw_dN-Ke8sOCF4IMnr2uTwfXIJqAtq8bvkQhf-fB_JEMcxuVgHExEWXjFRJdM6wNGoQ9ehUx1qHY1hRKfwj5S0ZDWTScMSAVlMrzDJld0XmwAQs9niI1wyaKyQQXf1dtOBs3K4Yy_YxHFCvjKq-gwMEFDnHf0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30295" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=t_lWrczdLQHBy3XjoJ8YcUhc3ahr3kTn1ZudzCUpaCR9AEXvNB4SR18n1slalMHni59pqhYuzqEM___1_SPGL6RPauOP21TCK_0c5zdqtc0l4eOE8qiVT-Cj_VQwxRkVkKXyek_MNPwJ0PEIUqfPMdogLVf_-YFZ7IYTy-XhEOchjXhvZ1d_y9JR9V8og_oEvXNI3AfY1LbDbpRlddG-rIt3rZrGotA4WNmt1JXUd0GKHXZcJcCklxBAQ5kPXnxPP8oeBS0MsHBMyEh_c8cjBvqlHIrbnfSm-_G_pp1-2NofuWNiptl6jL1diRLRlOfnYJNDs476xI_Yg9pKHUrLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65d70b248.mp4?token=t_lWrczdLQHBy3XjoJ8YcUhc3ahr3kTn1ZudzCUpaCR9AEXvNB4SR18n1slalMHni59pqhYuzqEM___1_SPGL6RPauOP21TCK_0c5zdqtc0l4eOE8qiVT-Cj_VQwxRkVkKXyek_MNPwJ0PEIUqfPMdogLVf_-YFZ7IYTy-XhEOchjXhvZ1d_y9JR9V8og_oEvXNI3AfY1LbDbpRlddG-rIt3rZrGotA4WNmt1JXUd0GKHXZcJcCklxBAQ5kPXnxPP8oeBS0MsHBMyEh_c8cjBvqlHIrbnfSm-_G_pp1-2NofuWNiptl6jL1diRLRlOfnYJNDs476xI_Yg9pKHUrLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛
خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30294" target="_blank">📅 17:40 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=qF6Nadzpu_w60pAhiKwZXjFjjd5vp24U67r3tQgjYKV9AOvnTJ7xS9WVef09lqQeKdWOvgOyfuyU4P7tADmzOkCE2T4vL3Fg_S4F5rM5k0m2RRv0I1QztmPvh3MosXFM8j-V4wrBs4wsR8bpLYSHHfez01dLt9Rgnt_sxKIJCXitcuvmj6owlEfcxKzV41B36BAXvJCkjceew-S2hi3fR6Q-gf5_VC4plY3jxjBvHeQwXVUDseGsDuhKhtyxErxFj48lweRfgsHaFixW0L3NtLVYo1ZPhD6RjEu4CLL7ldGXSbhTbtREpXnGmsuaArZjfmqCHCbEylSq4SHkgDavkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5801a724fb.mp4?token=qF6Nadzpu_w60pAhiKwZXjFjjd5vp24U67r3tQgjYKV9AOvnTJ7xS9WVef09lqQeKdWOvgOyfuyU4P7tADmzOkCE2T4vL3Fg_S4F5rM5k0m2RRv0I1QztmPvh3MosXFM8j-V4wrBs4wsR8bpLYSHHfez01dLt9Rgnt_sxKIJCXitcuvmj6owlEfcxKzV41B36BAXvJCkjceew-S2hi3fR6Q-gf5_VC4plY3jxjBvHeQwXVUDseGsDuhKhtyxErxFj48lweRfgsHaFixW0L3NtLVYo1ZPhD6RjEu4CLL7ldGXSbhTbtREpXnGmsuaArZjfmqCHCbEylSq4SHkgDavkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود 3.5 سال از این‌گفتگوی تاریخی علی فتح الله زاده با محمدحسین میثاقی روآنتن زنده گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30293" target="_blank">📅 17:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkkIlcqtO_AW43YH3JFirO932tuI13DiIMDHiFcYXJxUbfrKnxuqaKm3Ssqu_7P0l2iZXenJgVUemidca-yleGWNkGzb51KB2YtCoE3hABaDKjpVkjeZldrpMC7LvKz7j14Mtbrn4jqrTbD00OYu5x16LXnlyk-4GMr5Ppo_ot5Loo5cwcLbQp5erxbxVvOki-QHmGC2fyqmeh9H8k-X2-n8DSB8We-WIU1_V-iGRkBkBAOn-kd_r1YCC6if3GQBshqy2uhPDdD7FhrL4fre7Kz6wIeS4VE8D32OHpNSIvDcFXLDWyAn8JDwE3mfhVCxGEFO9x8ZSWu_7oR9tX-RMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی، ستاره‌ی پاریس، با رد اتهام تجاوز، مدعی است که این پرونده یک سناریوی ساختگی و ارتباط آنها فقط در حد بوسیدن بوده‌ است. در حالی که شاکی بر ادعای خود پافشاری می‌کند، وکلای حکیمی می‌گویند امتناع او از انجام تست DNA و بررسی گوشی، نشان‌دهنده‌ی دروغین…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30292" target="_blank">📅 16:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBRfuX-6DAWq98Ph0Kgp68aqUwb2DX4oXWh-ybHzxkzrsCAZkkRQJPyalHLIBJJteqiF86k5BGCzXF5jjVXOGK3viv49sJkBRNa0G95NwG9YF3FUk4BT9Iae1MWKDSBTYTNXPMgeiF7X1SrrssPY12xlVB6OaYoupg2g_FWQ1W8v7Zu4jxpGyj-MMpLDY0aplvtuV9kGFhMZrjQ4wxGQcJ68vxwWeqzsUnmwM1_qecMQG98dqHjrqMnHeaF2I0jmAbW8xn5jYvON5ldmub7Fp9w_isZfsNF7GcooFDlcics6Msq56J0ZZwXU47nWefuiNcO3oTc23GeGrSs5sJj0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طلای‌ناب ورزش‌های الکترونیک بدست آمد؛ قهرمانی‌تاریخی‌پلی‌استیشن بازان ایران در آسیا؛ تیم‌فوتبال‌الکترونیک‌ایران در فینال بانتیجه 4-2 برابر مالزی به برد رسید و برای اولین بار در تاریخ به مدال طلا دست پیدا کرد. گل‌هاش تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30291" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2ETuzSUYtSqsdEZM-P03Snw8OkxWYrqeXJUCpRSwtprD2T1IZrzl_6praV37JkMhOK9TvXYdVzsJi-zwrxr3jGWUhof6bw-59kfsrav0jC60J_p-tkSoNr-pX_9YHGLpNuCkzK86t1NdrdPCL5-D_yVCv79-wgklRnFaDsiUSq9YjlX2BV-OyZqoPCgO0xc1jOywn-qXLdEBtvU6muOQHvml6eT3yMEUqDEc1tEko8FkCvVMH0V9FEwd94j9CUed1LB0h7dgQDgBP_p8afWnKj79s3FlZeRopyjH2_6REBbfK8S8rkQ5uzn_-iwTL014j1iAeRaBg-3vIaXWmAycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ظرف24ساعت‌آتی رستم‌آشورماتف، جلال الدین ماشاریپوف و یاسر آسانی 3 بازیکن خارجی استقلال برای حضور در تمرینات آبی‌ها و دیدار حساس مقابل تیم تراکتور در هفته هشتم وارد ایران خواهند شد.
🔴
اوستون‌اورونوف و مارکوباکیچ دوبازیکن خارجی تیم پرسپولیس نیز تا پایان هفته وارد تهران میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30290" target="_blank">📅 16:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S66jAn7et6FejVx8cZZM1VjaDRiRP2ey5afYfPEWfMQCEWDXPV4nbPIf6ryJbPYpXFoxg_NijG12_JpJZaHbkBx6x_-RRvx_rzv8vuFUiouxRbI9tUGHf59yMYnt61U6HcWr4F6_87syQlO3zg379HGwiYlpphrvB-2Hyy2mHRxuNq8mOwZaXIgvjLs3jZvKgsjvIOaV_savbhjJH-0Msq6yR77fGXRvYIwB1hYyi9hwmjCrePbrAHemneFzWoqqFYuR3dPSqhjwYNwwj_VkGGmw46OuYIOyURYX3jMiJdiqQzf4LBJUap-7-U7s_mmtsC-dsUB7CzoCehMPFSQQ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تیم پلی استیشن ایران در فینال بازی‌های آسیایی مالزی رو دو بر یک شکست داد و قهرمان شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30289" target="_blank">📅 15:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWfjEqkHJFdjMYrKDyLhNSSnu5aFl6GohmUXWOvj2AabaDq3LvRq7Q6hIwKcpIxPEbMA4SzSiDgk22DSBGJYwMlE0gkH5jv3J2ixryZmtK0Mjph0AOqJAzB118wBle0bUscUlZ1sFDzjQKof1nYFgsli260YFGVLL0IfDFrNqyXCBFIzvDJC-a0yxZrs-ysIfNo9gcxQmGyJ3u6zUAOL3jNKds8HvLR_z62XXjCxFt4O4er_gJKg-GhS5UF2FypZuiDytT_WP86Ufdt_rHuyNg6kqZFWTCZqAgyI9Om03zWZxFRdCxEa8EoiAZfhoS2EU5Xpcv0tVLsHP3twWKqpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه.تعدادگل‌های‌کریس‌رونالدو با مجموع گل‌ های رافینیا،امباپه و هالند درکل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30288" target="_blank">📅 14:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30287">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrP2RwdDwdANvcmWLAsy_Jgcpdo7y9rzqT-Cv67Zc3oT1mPqF1jJClaiQZqWBAPZOUQVoELPC8f5l-HxGHpZZ9cTaOh3yWxe8CHqcz_ZJvD5r_Hw_GGtUk3I0XJ40vGF5L1fYKbHclZXNeOW4wx7YHGea10j3gxJ6RuVWedhpRRN-qn_aOxKt4Y5TezbkK0R_1UIXbGPadcfqrKI0d-I6oJmbjQA0VssJGAmKzi-GGV0YBGAKIj_AT5c2_lz0TueVBKEDcYG5xzKWd7EAunoqrm-xuaCaqT5wKJF5-lDdRhYgXbdJqjpl34KsFSCjhXMOSFQBE7XW4VtWC-FRvMeuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛ لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30287" target="_blank">📅 14:42 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7GaLUhaogIXL_lGBaVzWoPNVCq2KprvpCdDXjUaE0cRKujMGFFE7XoeB0oGsbJSPjHZyXPIJJXRmVBvWA3v-RfqwkSu3U0WqevGAFInQOhEodtbUsbT1MJPXCraA-z3FdQEpulefUWuqdUwIm4bmqtqlwaY5GCLMAsaxiq4Dz1vMCffg3MlM3B00cmBZo77mrVXjZlkvYlrM-6AAIdhdO2uDeN20bIAsHJ0UhUk1JCvDznl9WkeoPXMSAj2c15dwOA4RPRNGLDKzbyTF_EYAjgRE2gcB1r_HQflGhFucquUGhpiQ6tdPaHGNJqn_Msu_k3jgjPJz9-TxelTyCR6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30286" target="_blank">📅 14:31 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVPOBr3j8sJi3a9AntnFT7aBDBxUVwilWudesikSzP-hK7ilkEMc9ps_oa1oBUYLHrr_jum8bQmanVGVPUecWiFt3ULYDPEnfocKQPfzLJASjOS3OY3GEcE7xkGHT0u_DWsjjIUC9JDrldfF7F57m5YOgE9zzkAZrsUX6JaRTpdlCNF8dIzavv75uhL5Jv1udcwk3YrdmMDIaAjgO_1wqI_e8jwn6giqGgjXpe-FhBCNKzcYoadDvBUhgqeJg8hsDQdsa51JuMY_6nOcxv1uIX9F9JqDeOOm3zFRmTX8_Ql9L9MvZcLxoJpuJE0KxLvWk4OWNOB7o7E4FdsyMIFluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇳🇱
تیجانی ریندرز ستاره هلندی تیم القادسیه:
نمیخوام وقتی فوتبالم تموم بشه باز کار کنم به همین خاطر تصمیم گرفتم به عربستان بیایم در کنار کیفیت بالای لیگ این کشور آن‌ ها دستمزد بسیار بالایی رو به من دادند که زندگی خودم و کل خانواده ام رو تا آخر عمر تامین میکنه و نوه‌هام بی دغدغه میتونند بهترین زندگی داشته باشند. یک‌سوم‌رقمی که باشگاه محترم القادسیه به من پرداخت میکنه هیچ باشگاه اروپایی پرداخت نمیکنه. از انتخابم بسیار خوشحال هستم و میخواهم سال‌ها در لیگ حرفه‌ای عربستان باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30285" target="_blank">📅 14:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1454042688.mp4?token=rrA8wrG2Xsg5oE_A7Tte546suuq1P2q7xpmHudcd57D-zI_zDiZcq90tpYXakr4BoxTK2q8AuQs2rWHRkuQmvrbzzosDpxcbqzPORmteMerQpYh9QNtQ33kLTO6nV4rcZ8BkADi8hNnxyHurpI_-p0FRk059fHfb5lPPYkQ3gwY-XOCAvZ69ZzBGiboz7bGlDrP9FgHNJu9GddhnxidTanxnh8sKRU0c8IFo6rUavlXz9s-_NCPo34yelTN8PPlpuLetWxV3mNOBuam5YxtVx2LxXjd9KFxwE78CZ5fKrXFdcRYdy89zdhZRaHsf4TCK0daUmZl-NUGEhc3W2I0VDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1454042688.mp4?token=rrA8wrG2Xsg5oE_A7Tte546suuq1P2q7xpmHudcd57D-zI_zDiZcq90tpYXakr4BoxTK2q8AuQs2rWHRkuQmvrbzzosDpxcbqzPORmteMerQpYh9QNtQ33kLTO6nV4rcZ8BkADi8hNnxyHurpI_-p0FRk059fHfb5lPPYkQ3gwY-XOCAvZ69ZzBGiboz7bGlDrP9FgHNJu9GddhnxidTanxnh8sKRU0c8IFo6rUavlXz9s-_NCPo34yelTN8PPlpuLetWxV3mNOBuam5YxtVx2LxXjd9KFxwE78CZ5fKrXFdcRYdy89zdhZRaHsf4TCK0daUmZl-NUGEhc3W2I0VDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کنایه‌گزارشگر به قلعه‌نویی و حسین عبدی بعد از شکست مفتضحانه مقابل کره شمالی در بازی امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30284" target="_blank">📅 13:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30283" target="_blank">📅 13:13 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=HfRZwZvo9o1zL3kJ1PBbbMQ-ekcgXlSgjwUq1QEBcR23-6m_Gv0XHvFvPNiYo4Ug3l7qQQg8s-DNb85iS48ajRCT7W62dFo8EYUUfNaJVhi3GWQKlnFN9ZrJjLe6Yz3M6a7r_oL7wFkNJzYwFvfOmkz_au38OUefFvg0EkjI9C3SwH7hZ6XlAwIbt9wrwC3tKtCJmw38V4QkvEVkE5E9kwSUIkHdo9kN2dztGVj-JRH7GlihbPPMWQI3WsHbOySK9tzsIFsaW7aV0LL3pWYRycxj5hK93g3sHmz45ko2BhnlStjFMzgdGJ065XhMQiNmMPq43QpHTgTXChsgQqsX-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef1cb476e.mp4?token=HfRZwZvo9o1zL3kJ1PBbbMQ-ekcgXlSgjwUq1QEBcR23-6m_Gv0XHvFvPNiYo4Ug3l7qQQg8s-DNb85iS48ajRCT7W62dFo8EYUUfNaJVhi3GWQKlnFN9ZrJjLe6Yz3M6a7r_oL7wFkNJzYwFvfOmkz_au38OUefFvg0EkjI9C3SwH7hZ6XlAwIbt9wrwC3tKtCJmw38V4QkvEVkE5E9kwSUIkHdo9kN2dztGVj-JRH7GlihbPPMWQI3WsHbOySK9tzsIFsaW7aV0LL3pWYRycxj5hK93g3sHmz45ko2BhnlStjFMzgdGJ065XhMQiNmMPq43QpHTgTXChsgQqsX-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانی بیخیال هوش مصنوعی نیست؛
این چه سمیه که از مریم‌امیرجلالی و حمیدلولایی ساختین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30282" target="_blank">📅 13:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R10PyQXAJRSPpcfXCSlfs9VITMLJ-U7A-6_Is6yJpLuURor3w-DLu5GuM02vQwrQ3Q1NQ53nOIOduW253wT3dUXFw2ChrQN-o_sxSJL6B_Sr9xfTkVicKy-BEcu1nq2o2QfBIycm0beN-FFVOnH6AI7faNubwnpc5KTiG7sCzp5iYLX2ptW_ISHLmuRivyNDhgYcmko_fUJQHigD3AYHjq-kBvhRSUMgFihLRJVJN8rk7slnxtzSmW7NRlFVG7MHte4A_bWcaQ28QbHP70dTYSjJgKoDLx-AiNldQwZG0vVqpJE7B1sllkWCoSX6N1Lr-1tbso6-0ILDOiWCO1KeXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب بوکاجونیورز برای دیدار خدافظی کارلوس توز فوق ستاره آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30281" target="_blank">📅 12:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30280">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwx8O44m0t2Rzc6DtYxfnIbu2y0pynira0vK__-sThS33fVPKeDrPOjLve1qkBq1QV5WgdqOoKftnmiJD_yCTIyOZVRKYQae2MIKo5T6XQ_As5RWpjoFcRc6ENiuqZgFmt6sqNHqMECirof056UmHX8QvxADzK_Rf2YJaDAK5RrtgDs_-FvfYFgjqVMqrHoK1eIbhv89DA-ImApS9VEcvC9qjAJy--KXkSPeNfXMovP-aolVeSoWQXpD6rvqsUuMlG1qp8EytkLXeDVGmLj_RNUyKjUwHm1cWAYJ4p74DvPkreGp4yUbKMnTHVq8A4q1sYdJQFNeJ2t62G08ys1lMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناس شبکه CBS ترکیه:
«رافائل لیائو فکر می‌کنه برای‌تعطیلات‌اومده ترکیه. اون به دید حقارت به‌فوتبال ما نگا میکنه انگار ۵ بار توپ طلا رو برده.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30280" target="_blank">📅 12:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30279">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE9o6sE93sZFAAomBZRnJwVWFciksi59S1t29RaupBgXGcXgTJgVlA3pltR0xAYu7YYP-pauZk5M8X3Da4HRrzXCG_hoJzf5qMoLRHIQozDeY0IZx3WKx8p2eQE8NQyDno9H9oY6z1wDg0EnVWlkS5QgpFYcsZBK82CiLkwJDT59a3QAv0ChEPgL_N1R-EdwIkKyEwmQZxFK1JWE626zj5wE0JOhD4a7ACpgltgo_Fi15mebOGG32H2WVyfJMcGRWAr3NYdHDVaeQ5dXZihoKY3cpkYdiqmJMul5bUfF32MiQlBbd_X4lyT3eIIpcvGeYYSMt1Kg0HvpKctRLqSc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30279" target="_blank">📅 11:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30278">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSPtJmPN7Qjn_841_IV6Y07RxBA3nj0iP7sc0kCbEgtf7MC0TLDH7OZ1011qYxb_YU1Rl5Ok9V-jfVRWfl886ornVm9Zvj4EqfJukf5-8BDY0Vw3JO2ZnUZFkBcCEn7IASqkhOEwbhMCD_J8AHOnkeMq2LpkHrLGd1RlgA36G3r0Qkl_oOazzzn7oUgeyzipZHoareUVBdtJELI9RFYlr6naMB3YM14YiKAfkxdVceq9SU4952EoxTfbAMFzoO7kqWqdxtj2FGo-YBbGuyWyTyIeJ_WjHWMwE_cnVlBfdJnDOmvWRnjq2Wsu981zeuNhX88KaR-qKrBxur5mFjWwRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30278" target="_blank">📅 11:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30277">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhE8zNYXiDM4y5Cks9xeK9GBUzeZCIRK5fEIyG0uk5VF9pUlZi7dgSNVVkyQa8jQq4geyChOIRrmL90cRnIGRWCJgKG8TzH7Zht0N9x1lXOwKq7aTGZwWdEhIGY91W9osIj_0ATb4_nGsWPNqOyGOifMAHwx3MmuH30a6EAY12ci3ZL0IpD243BphJbcMD3TcXX96pJHpsssfluexKRoTuscVqkJn-Ilt1IdzuLU41TQZhk6ybne90MStFHRK9yRkS9hmWbY4BGcQSWmaQkXAvdEmY_3ic6j5Q1oC4YoR-203M9z4loEaIHGQ7cGLapqD2aB8RMK9HhUu_3_ZHr4WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم ملی امید ایران تحت هدایت حسین عبدی مقابل کره شمالی تحقیر شد و با قرار گرفتن در رتبه سوم جدول از دوراین‌رقابت‌ها حذف شد و بازیکنان بزودی به تیم‌های باشگاهیشون باز خواهند گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30277" target="_blank">📅 10:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30275">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4Gk24iU08KXeN7DkkDKkzuC7PNI7NYiQ-eS3-jShaKcGCsNRWPjncJx00KLdxDABJRGQoIZDTsSpRI8r2Zjv-lpCVuiMwcGB1zf4yFNdttbkehv2jo8e72YCSNdGXYfZjaVhBcv77Fx5pyle5GNO3YNS4zdjYjXAEsilW-KDA3IHJ2CMrqrmSm1ylHqZrZy92WhIzrHE0OkbA4NlEsK5BjSrieMWTMQScEMrIwiPO6f3s_nEK2rXFWTyljvXhDp5aCFexPM94KtVFV8pAqjBHGjM_YkUqepoNVvFPdHjbEl1aL1CKiFASiyDhIIOFAVVZowoeHXg-SS5zrqI8JQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dB2S5qY_5MQweVoF9ge6teY5nr0flNy5n4uEYlPtcFUV6yVW1M91EHsVvkdWbtBDFw0cVtim53dKHbIMkoduiLeA4EWfnIvArQvH43Ozt1f80p1YJdwJhWy9xsE_9zuHehhOa_5Nj2ZJFrDv6x9mYU5FjJ7Yx1T5wJ7Z3nUvIR5WqH6Hfgwi30EL7syfRZAub7nuzSrbHtJVQw-XOLCUooo8bLiDRGztAA2hNttbdvOJlHS28Uq0eBSV2m70Zzma74d1K6CUgYIk-Y3fyStLgGRPCs6W9FIfl6PVxK-3y53KMw9_5hkPZPL7XtxXkRKJQtyB4_0etQAiOLHfWuJ7Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30275" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30274">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIHmg5XcH6Vz6B6TrdenuL_jX9iO41Kjv1MVn2o2bWucDAzpZTqB-eAmleRBBL4g3WxvuOUrP2JUCXtTCM_-AReIq1WZxI-K_Rs6u6ghqPSKItA-qnR3JiTxsbmt2vWjC-Y31gQdXBSVts5nTTCWf8Bt6b3SAcvHt8UCPPTIO6WjMOblRTywhQej-DWQag5a6vPu6xhQTxB9Xvc09J3dul3l8bRxwLiXphQ2I6pZLw-hnS_9frBVjxmSY_jg1P5rrDqYO1ttVLEjjpJG7AYqchxk85ztdfUAlrUPsQaA3ln5dN96F5kTiG2dm2jYf4_MRJda15l8XY91oarZ8-9-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30274" target="_blank">📅 10:52 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30272">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkQZhmz7jxgxfMp9BKYi2pkZaSLoyRXEvB3FZGw_x0pdRZ3CZvkvVoZsi9CLJQFzEUgKeF_nCelyTujhnZZfzfr9Xog33eJI89wKpywJ-UyHKKIgbWL3Z0ZL4LzSlA69bYeVU36s-KyOTSCvjhrRvU7dcD-Rx3gwhdzLyZRr9x0dOg-xI73uJVAI-BJKHZA1KSSpCldr0eACADoQ517y3bsKqxBWthok4teduhx7_gUe5SoqWlgY6waLJ1JueToYRxmNMziY6Ym4Zb5M3Hh4f6aKVVUy0lt0eyEAJb0SO6LDrg1aFBRq1DlIcMIXR8IJZrybnK3zktO6pFnDNMr_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مثلث خط حمله بوکاجونیورز در بازی دوستانه خداحافظی کارلوس توز آرژانتینی از دنیای فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30272" target="_blank">📅 10:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30271">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=cb6JD6IKooLO5Ja5ElbIbsUTpmiRH6V8GFiDvjVTRSn96WDZVIB3en9i05_RlrkowmoBwP2lodJesS2A3IXZjw8mSHMCpDqKhpXWXswYkvNLWtPGxCpxbe5wpxAf0LVcuzAScpGUtKVL5RP-WCRPNdM-ABQnPJcPK66-MTAEJ3GYnXRlesToBLPG9nHQMEc5dKFWg9Sv0A6Kq9ShI3RlCA49BYJU0ub4rOQmAtMe1WH8ZleUz_m7TibxXvX7pC2p5xiNkxm61qN4MH16WhS9g3IdUxfCe0c901EQJbrsutAtxvTIXcOyP8aiRfY2-s_r85070xyJZm9sGAlaUsE6CFxeoWaixLBqIxw8q12Kmz0ylELcKmtnO5b1M7N65xJmAaf8qgRtZrNvNbInPMX5j_mZP8HWUL8h-Sz5ZsxA9YTLEGmR2xqX9htTEHQ7r7MYnUYp9s8D54cDJNrQjCAlSC7hEYAUWbCV6kT8mVHj-rovqju-8FtVdOyHCdxQtIgGiQpjQ3n1uaPyI8kyLDU_D_EOBFrsz9kiUdsBSJhFm1bTQWrBnrX1B7LJTZBj2NeZ40ZRNhiHYWDG3M0W-1Cq8VU_rJ_wEgo8octT8VUdjqjqdxomztGfIGCgZDJsBsm6fRn9APPgGcbkEyoB9NTsW5AHD7lonpS9e7QfbKHl3I0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f64463b5.mp4?token=cb6JD6IKooLO5Ja5ElbIbsUTpmiRH6V8GFiDvjVTRSn96WDZVIB3en9i05_RlrkowmoBwP2lodJesS2A3IXZjw8mSHMCpDqKhpXWXswYkvNLWtPGxCpxbe5wpxAf0LVcuzAScpGUtKVL5RP-WCRPNdM-ABQnPJcPK66-MTAEJ3GYnXRlesToBLPG9nHQMEc5dKFWg9Sv0A6Kq9ShI3RlCA49BYJU0ub4rOQmAtMe1WH8ZleUz_m7TibxXvX7pC2p5xiNkxm61qN4MH16WhS9g3IdUxfCe0c901EQJbrsutAtxvTIXcOyP8aiRfY2-s_r85070xyJZm9sGAlaUsE6CFxeoWaixLBqIxw8q12Kmz0ylELcKmtnO5b1M7N65xJmAaf8qgRtZrNvNbInPMX5j_mZP8HWUL8h-Sz5ZsxA9YTLEGmR2xqX9htTEHQ7r7MYnUYp9s8D54cDJNrQjCAlSC7hEYAUWbCV6kT8mVHj-rovqju-8FtVdOyHCdxQtIgGiQpjQ3n1uaPyI8kyLDU_D_EOBFrsz9kiUdsBSJhFm1bTQWrBnrX1B7LJTZBj2NeZ40ZRNhiHYWDG3M0W-1Cq8VU_rJ_wEgo8octT8VUdjqjqdxomztGfIGCgZDJsBsm6fRn9APPgGcbkEyoB9NTsW5AHD7lonpS9e7QfbKHl3I0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛ مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30271" target="_blank">📅 10:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30270">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=BS6Ozl5oWY4eyUXosLC0l6GOMS7mYMb5pWq8GCQsRIB6qosrqcV6rQKlecMrVK-_VdcThTzXXtJ9Hsn6GzakPbLTTvar6o6TnRXCZcp2Nh3A7zXTQidn4LJKZ5woqc9FG74M0HWR9IgYEn4AGNFmv05JowyJS9WEKMHHOdIBk572HVvIHDmxlCTJM3oNJV5sZRXTsaODnOyY-xyk_WOMn1RMvFF_oQ2cZ_R8UJ7Sw01T1pE_HzCgLUaNEN2tL8L1XpS8WvdBxNGYsM25wR_qmSsD_TjMJ4q1q5TIV_UULCUgyGZInIbr9LUuUZ__KXAi4k8HFfES7i9RBK2kRuyPIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2f2dad5c.mp4?token=BS6Ozl5oWY4eyUXosLC0l6GOMS7mYMb5pWq8GCQsRIB6qosrqcV6rQKlecMrVK-_VdcThTzXXtJ9Hsn6GzakPbLTTvar6o6TnRXCZcp2Nh3A7zXTQidn4LJKZ5woqc9FG74M0HWR9IgYEn4AGNFmv05JowyJS9WEKMHHOdIBk572HVvIHDmxlCTJM3oNJV5sZRXTsaODnOyY-xyk_WOMn1RMvFF_oQ2cZ_R8UJ7Sw01T1pE_HzCgLUaNEN2tL8L1XpS8WvdBxNGYsM25wR_qmSsD_TjMJ4q1q5TIV_UULCUgyGZInIbr9LUuUZ__KXAi4k8HFfES7i9RBK2kRuyPIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سال 2010 درچنین‌روزی؛
مایکون مدافع راست اینترمیلان این گل دیدنی رو وارد دروازه یوونتوس کرد؛ دروازه‌بان بیانکونری بوفون افسانه‌ای بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30270" target="_blank">📅 09:51 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30269">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=WbA4xajHXBKPQpZSQl3Pu_uB7zRcrFk2cQG9bGyOZd547GdaW6IZe3MGPUveC2Krwdk81ULQ5xHGsl9RcM2o8Z09E59r1n9gi701-ppZECAqep6Ji-VbomZDtlR1xn2_l0_9FxXfRndU0TeYHBVU-CydD6YccdIhY5wFMpRZs8TyziUduA3V3x1Nl-n11QD7Q5Ks5kkAuTZkZZEnROo52w0dIhrD3gTHLXl4XOM_QW6DXA5CGmF69zN9GSbpKI2FxpJHdDHMRdQFeZbIt9-iMCch5pxBVlRbHHOqWoRzf0vZefubKXPkhpo5bNSoty29R1CSVTNQg-3ko6POB07img" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204e06fbc9.mp4?token=WbA4xajHXBKPQpZSQl3Pu_uB7zRcrFk2cQG9bGyOZd547GdaW6IZe3MGPUveC2Krwdk81ULQ5xHGsl9RcM2o8Z09E59r1n9gi701-ppZECAqep6Ji-VbomZDtlR1xn2_l0_9FxXfRndU0TeYHBVU-CydD6YccdIhY5wFMpRZs8TyziUduA3V3x1Nl-n11QD7Q5Ks5kkAuTZkZZEnROo52w0dIhrD3gTHLXl4XOM_QW6DXA5CGmF69zN9GSbpKI2FxpJHdDHMRdQFeZbIt9-iMCch5pxBVlRbHHOqWoRzf0vZefubKXPkhpo5bNSoty29R1CSVTNQg-3ko6POB07img" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌‌های ابوطالب حسینی در قسمت اول برنامه جدیدش که هر هفته سه شنبه ها قراره پخش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30269" target="_blank">📅 01:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30267">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oY9hfu0jKoB0HmVPUHSuJvKMHZF8j-jzLYMfvLskX4Pga6kQwNZshVIntg3nuxTT8eVV_BBvippiCHIliSdsvrH4biLa_0AHizHepaF7Bp-QUcOi_w3tosiK_vIXLaJ2A-HEJfamG_bhPAw00KE84xb5foohDE2-fF1QLJncf9DVU4INIikUGItXeWZY0RI8iuYszymLbovYOQ3ZypIkp30ah974dhhrUuLI76vBGbsfPWNgSm71RhzXSEjW9NEhTl-OII0zmtxk-Lzk9VYsqXEKxzj7oOLbUFN7DElcH9EegqAGGaUDz_LG21a6Z3lI4DodiGGF6TmnCNv2MiIw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ بازی تیم‌های امید ایران و کره‌شمالی برای صعود به ‌عنوان صدرنشین در ناگویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30267" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30266">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=I36J86TwG2PGH5fakpExFuoDYOZ1J2RTQMs82-DUwkdrHCtPpC9hjLt0-Hnb6DUoQGY5T0OdRtgUfyWhISSM-ah0d8p8QPJhMHYoBFAkf6owa12iahBxGc6ed68inj0W6NIkNCxJ2oLVQ0g-P9_bxg_fUw-LXiv8KnXWEI0q-7bLgoi8uxLyhconpjpzmWoOx8YhIEFtJuaEamA8LnRicJv95L6PWsCawr1wDW5LIiSiMRVz7MbYRmT3J0AgR-ice0mDv2viCrgKeZkwsgxdEzJ28MREw8yZjL4CMENMlWcBUkmZXBPcEhlQq-QSvlSp2yb0Xm400iqpsRnL4uAQwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0067ddce.mp4?token=I36J86TwG2PGH5fakpExFuoDYOZ1J2RTQMs82-DUwkdrHCtPpC9hjLt0-Hnb6DUoQGY5T0OdRtgUfyWhISSM-ah0d8p8QPJhMHYoBFAkf6owa12iahBxGc6ed68inj0W6NIkNCxJ2oLVQ0g-P9_bxg_fUw-LXiv8KnXWEI0q-7bLgoi8uxLyhconpjpzmWoOx8YhIEFtJuaEamA8LnRicJv95L6PWsCawr1wDW5LIiSiMRVz7MbYRmT3J0AgR-ice0mDv2viCrgKeZkwsgxdEzJ28MREw8yZjL4CMENMlWcBUkmZXBPcEhlQq-QSvlSp2yb0Xm400iqpsRnL4uAQwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
توصیف‌های عباس قانع گزارشگر مسابقات فوتبال از لیونل مسی فوق ستاره آرژانتینی تاریخ مستطیل سبز که تنها یک بازی باقی موندهه که از دنیای مسابقات ملی برای همیشه خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30266" target="_blank">📅 01:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30264">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT63eratBx9Sesz7v-72aMjJWhEVIH76YPIcD4OgZaAt5C12FBx2f6l8XUtbZyxghvcrIzjBlVJhY-knN2tmidnKKnJMIHNhcWCutJKoeW_NvVSbbqqDHtTHpxJTwmGyBStgRaHMPUCtnaFCYPlwKcGK-l4_hblniSPDm5BQA12p7uKDrPuxkwZm3QbGd11Q49RNGludVUVWgBkg5aPSOctTmjb7quDT4LXGNtwGqYcyImOIeQxNweA9POPpT86qwfGNM0lhtg6dmQ_R4OThLODxKlT50K0iCQX7zef_-SJOKPOXuwB1iLNPmNxU4NOCueg-CxRFcxMOXlGX211R0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30264" target="_blank">📅 00:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30263">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=QjdnFNu4SRygeYMNMELUk6ZQK-fmiFdD80MsIuNDwhAYa_Qhsy41-QGJc_ZYz0U7UEzblgQJJXGITJjoW6MReGjzxLgoeDUsW1oyKPkubLWcZ56W067SxUfc53Tkx_ul7lHi1xUCHCWiTHcw1rY8KsJVHAMelJm1Kmcn1CBQLP039VeWzGxk5KFbmqZo4cr3HVz1FCQrVFsr21xlrZiZZ6V3h-r1bYtMPStUMgW-7D60yGuHQ9AFz5Odqy_RTcHNRw3XQbi0tvSjfC7-k6tlpJGLTpOlmaWHkObBSyiA5pU58oYVW9dBw_SYeeEZ9yo9d23VenBEsrVkSW8oUL_XYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a798b5e.mp4?token=QjdnFNu4SRygeYMNMELUk6ZQK-fmiFdD80MsIuNDwhAYa_Qhsy41-QGJc_ZYz0U7UEzblgQJJXGITJjoW6MReGjzxLgoeDUsW1oyKPkubLWcZ56W067SxUfc53Tkx_ul7lHi1xUCHCWiTHcw1rY8KsJVHAMelJm1Kmcn1CBQLP039VeWzGxk5KFbmqZo4cr3HVz1FCQrVFsr21xlrZiZZ6V3h-r1bYtMPStUMgW-7D60yGuHQ9AFz5Odqy_RTcHNRw3XQbi0tvSjfC7-k6tlpJGLTpOlmaWHkObBSyiA5pU58oYVW9dBw_SYeeEZ9yo9d23VenBEsrVkSW8oUL_XYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بالاخره‌تابستون‌لعنتی با گرما مزخرفش و قطعی برق پیاپی اش تموم شد و وارد فصل دلنشین پاییز شدیم. باشد که روزگار هم روزی به کام ما بچرخد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30263" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30262">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vymwk_Zw8t7UPcM43hWS0YOadbrqUeCM8Ugplq2K-m3muS0nKbdSaiOdKdUBdCmnb1HpQB_V4cpOTcPwHRzlZARHzQFwrjTMThPvfiu10pZBV0wwkeIKjczBJ8RHvbFpuQWlxZeoY3BQkNT8yXDLDi5eiKALe25JmXKtuDu2EekuSKziSey5AUu7yOs8QQ_J1cBwvXJxehgLRO8ZC-vahjck_Ti8VO0bq42OwIdDXkl8AIQxH_EZ2N337g3frCeQRwno39a3whpAs7-hItYBDlaSoxHLpdxL4uA5XITS_nEhMM1KLyB5hfhhCiqo46YLo6Z4AdtuBpvVZjXtW8NLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
شب گذشته تیم زیر 17 سال النصر در لیگ برتر عربستان با نتیجه 2 بر 1 از سد الاهلی گذشت. هر گل النصر رو پسر کریس رونالدو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30262" target="_blank">📅 00:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30261">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1hxB0FM6q-65-SF9DDC8i_r8VsWRo23y4Hgd-1W5gZsIcqs0yHTHPC_r6Z1p_oT-zHDICYazwHpQnQsAi-uYyuWAIQHGE8tL5UO0PXurhqiaQwimNm4pQPYjf3eMELDyCefe6zYB62BpAEbuJo8Z7kAMbpzc2Slhsk3D3TKELDVylyiGWPb8I0vMsyU1-T6660qOYCkHB-ENhTm6-Ap-r1tIMec3gR33XsYwEcK_v0ps0k2_E1e43sVoCodYDjTnPY5ft4z4jfA3ceRu41l8kerQ62g9UGiBlyaC7EcN08EfxEGI2DmQaHUa5nfbHgnnDAmq6mg-E9XPK1Gobqllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام کمیته داوران لالیگا؛ لی کانگ این ستاره کره‌ای اتلتیکو روی این صحنه خطا روی فده والورده کاپیتان تیم رئال‌مادرید بایستی اخراج میشد که داور جرات‌این‌کار رو در ورزشگاه متروپولیتانو نداشت. به احتمال فراوان مسابقه این بازی محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30261" target="_blank">📅 23:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30260">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6TXIH-hCLEuk9UWQBdwftWMyKiYrogoAgNG95t6ydoWkH-nChup6uwA8OBftxVD9SCkZCPRLTVzeBsuMiIinhJFE3P2l-6iErxISpMjgPfYzv6EcVVGJgtAgPCu-HAaDHOMeBkwivW3nKygrxkdup70gABS45FkWXx3fDG9fQFwBeM2v1OtlYkT3kmWqaYTSKZiURflCN_2r4zWiKqWMHkxanyOle0t_QmFbNRXhkm1dHt76monRnWommPRYkzJ-92XR0MiN4l_LOTdYBCjO_9_dmVGi3vFCi02oWCmiDhTvvEKtZfHfde7aiJr9wH5igY9Tc7EJ4aOkw3ZO7t6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30260" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30259">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
چالش فوتبال دستی بین تیوی بیفوما ستاره تیم پرسپولیس با زهرا خواجوی گلر بانوان پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30259" target="_blank">📅 23:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30258">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo26cELKau4h6JYD0ai7p4gUqVFkMEaCQLFKklsPQHz2_ehuAqfSL-M-vAOA8iZIAxYv0QrYNqWd7nnGs7RSosMZM3xp8jUJrK64aNGMEt1_5-vOiQCc9NgQijABUVZUJP-AYljLp7KPyH_TZrsjZ7t5vn0eCZv__UhQeDpgeIcA73miD-0BXIEP7UJWZnk6uzSOTPa2b3HCGMtkDMYVeAlyA7Z9ouin-zJTcorkfThKQw0z2ocmwZM4yt_Jgca-vcnglnLPGn5C0V9z9iZSZuQb1eDHePUc-vSEto7yyO28KZajUMhBaSKk71B71NohbgFygvEtqpu1Nhb3Hhsu2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
در جذاب ترین دیدار دوستانه امروز؛ تیم منچستریونایتدِ مدل کریک مقابل شاگردان روبن آموریم در آث میلان با نتیجه چهار بر شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30258" target="_blank">📅 22:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30257">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbRDwrHxwTqDT_uRJWzFzqJK2A1WTy4gP0BPlwxvHznFPaP7kyFoj-6GA-73Os9eBbT12p4jwA9s26dTMd5_8oIrAt0INAYkqSAVSbeHuo0jANJhf_3FrMNzxvt4D7aVdFxkWReNEVbYOTBApaItzB1nVptbwAPnFe2uupVkOfbS5stroKQuF6nw337jU8dLN7wz_LAG9FPUJN2YqJZJwoG1Gwt9NrYROMC-zxuNNZndPk4CEyzXXaziOQOo6C-Pgnz5bb9YTjbJRQKdBW3CBHxVUbwzCan4dp28kOMfFU3licpbtoiM237uTCDFZSkCMYG0DiH2nsqpgs2L-Rca3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30257" target="_blank">📅 22:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30256">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=knJ_pRtz_KKhT2JhlKId_EkClztpjnML6t_8UyQsnvb0a3KbSV1pRhxszn4PvvrsDUZFeAZpjCmnbdEWYw-x61nbfve4jiUP7fN6NuQgmVAJdDpQVAEYh2POG_FhPqKxW6lj7DTf2cteqKgm67wD82nGGkP6AbqBVKG6O_AX4rqdyB_yc4jzE7-sQ_hGxeKF4rBHrQcxPD1rmCL80r18M93X7kHdhjItacOtoNFcCwlKaDzyfxEjjAcaSjGi_fbDAoZgpup1KSX4b1UFQA1jKKT6Pb1JkPSobk-ScG6el9Tg4_AIhuKEG4vjMhrrx68R3LnPoE4SUMbmrlpvpWSfTH4NCTPP2jCEjVGzIGgj-Y8Xo6XMHlCuZGrXV0pQrh5oDX66TsSmMn3vw55gQcKYuZTdc6ByxQPbKMaaaK7g6nBqjjJTrMp76IcFoteRFselmVBQ3Jl2ywm9HNEmAkQlK1j1cI5UucWucaTRC7JM6gVOk_Uhh1S7PDXiY2bIi2z_I5AKUgYkMoHxR0j2JkIGP94MA61Mv_jMK7WQdsuIuppbxBxRP9XX7L9bRNx3A1Hz3630edhqQDH3yYWiQ_q-z0znfMlGdRrA6Wuq-h85z8-6pToaxGqgq4XqgsNN9WEekgKO1WBrFDfEEkBGj6ToIcWoBmuAXbH8peDm7IfghKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eeacd25b6.mp4?token=knJ_pRtz_KKhT2JhlKId_EkClztpjnML6t_8UyQsnvb0a3KbSV1pRhxszn4PvvrsDUZFeAZpjCmnbdEWYw-x61nbfve4jiUP7fN6NuQgmVAJdDpQVAEYh2POG_FhPqKxW6lj7DTf2cteqKgm67wD82nGGkP6AbqBVKG6O_AX4rqdyB_yc4jzE7-sQ_hGxeKF4rBHrQcxPD1rmCL80r18M93X7kHdhjItacOtoNFcCwlKaDzyfxEjjAcaSjGi_fbDAoZgpup1KSX4b1UFQA1jKKT6Pb1JkPSobk-ScG6el9Tg4_AIhuKEG4vjMhrrx68R3LnPoE4SUMbmrlpvpWSfTH4NCTPP2jCEjVGzIGgj-Y8Xo6XMHlCuZGrXV0pQrh5oDX66TsSmMn3vw55gQcKYuZTdc6ByxQPbKMaaaK7g6nBqjjJTrMp76IcFoteRFselmVBQ3Jl2ywm9HNEmAkQlK1j1cI5UucWucaTRC7JM6gVOk_Uhh1S7PDXiY2bIi2z_I5AKUgYkMoHxR0j2JkIGP94MA61Mv_jMK7WQdsuIuppbxBxRP9XX7L9bRNx3A1Hz3630edhqQDH3yYWiQ_q-z0znfMlGdRrA6Wuq-h85z8-6pToaxGqgq4XqgsNN9WEekgKO1WBrFDfEEkBGj6ToIcWoBmuAXbH8peDm7IfghKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2011 در چنین روزی؛
وین رونی فوق‌ستاره‌انگلیسی تیم‌ منچستریونایتد این سوپر گل دیدنی و به‌ یاد موندنی رو وارد دروازه سیتی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30256" target="_blank">📅 22:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30255">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr599flxXkPaXjo89EZucGOKiHuDqooijIjf5r4jCOvS3bL0t6mpMmTYCK9PHGpb_WzOBACHNDVFJEA5KR4mu7oAnBQV1lelzsr5XP4TXmoZ2JQ4_qstcAO4lueCSy4Dd5_PNT8U-1HtOTGneshss2HPHfT8Ymuj3h9ihBWUZCYfApLdt-j0JaGsUinhp81YUJv8l7iB2baWWZ2s8u5FwMZIgcbMaFOSpZIZ26603Htury2CAF32yrAyuie4TxnZhEiRF-SbebVuUTmtOj8L024Ho-mGAvp_EXFXeuXQbg6b_u7x-lY2q-TNQqRrMpJ1rT-jBsUG3O4si3Km2E_LQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
تاریخ‌فراموش‌نخواهد کرد که کریس رونالدو فوق‌ستاره‌پرتغال تیم ملی کشورش رو با این اسکواد و در خاک فرانسه به قهرمانی یورو 2016 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30255" target="_blank">📅 21:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30254">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfdrVDr5aIs3zd1fienvxR7Vu77ejSyuFWSIPu7v2bi_Q1Avh99yYmyq5KheR0ToimFPeecbrKIKVAxRUW5Gx8kmC3a0gK0ECqeCMPwyVVifa2orcB4zCcoHS34AlE4WY6gzNch4QfudwcZvYgD6aXGIk81NThE0YNKVwIL0am1yc0QnklXdGypU1lkzVcMa3O__Jj1lBcljDUuZZR347hYL61KDz2Ana00IAyhzGMYKMHfEN6JabSSyPKaDcPdJG26B3VsjbKAHp1o4jHT3L02SrPmHGf7IZObfet32LPRl7qnFwVLntbi7Rm8wbB965BgjhckUzklz9h_TKoalUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
دراقدامی انسان دوستانه؛
لیونل مسی 2.6 میلیون یورو برای‌کمک‌بساخت‌مرکز مراقبت و درمان کودکان مبتلا به سرطان در شهر بارسلونا اهدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30254" target="_blank">📅 21:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30253">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDOo3cjyXLUA-u0dNNb1gBOyOG4CGQJKneT1H-g5f6lWROCmJPYLIcaEQmP3wItKWARP0IIRp7claCaK8Sr0j1ZpkhHIWRFdfVIh3q3m3-7Z3cLf_Sie2JJ1JkjDs_vIiTFJFC-0H-r2mg8cYyLP9S6Hv_PMFrjfBfxfUyo7qHDlbf6AINo8WLKRnNZKqCY7chDIVw4D1MBPU1e-Y9NjG5sHg2Uwn-UC7fjh4y704ax1THgneqBdSjSMyKyuvObV6yebyRjJ7OzJZ9uyCoy9fJm1gTiXQZsCVu-oaGLQNZlL19VdqHSS8JZxTnHIuz960JyBqzSEFtLqEMT7BBLTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30253" target="_blank">📅 21:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30252">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJuc4Bf7zLVK9tjcxHNd2kVaHga2GtIZoYO2Qj1v8zwoUIBDlluM8Rb9peRWCh9lDCOSMf1UMFWqJEQzwKV2sKYFtYa-FljCV0xW7pN5m7Ob8YixxUUVdppm7pXkcG2GP8HgsR6AslVoy4C_p-FWnLS-QXI7FvwgNnV-8BAjfWPKp4_y_N_CVl5OSR1bPv-D2gHcxPk93mvNlXUYkAbfDdeS2HN2yTjRGVy2CAkr6o6r0lgB9-OYj9Rpkukwk14Lg7m4L3kKxq5O7DLnFXWZZSr2A0X4yYZI-r2CbW66cGoBVWI-xHG9hwat1B2qvNq0PJj6xw0jZPILl1GQz2TgFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ خدمت سربازی فرهان جعفری 28 آذرماه به پایان میرسه و با شروع نقل و انتقالات نیم فصل از ملوان انزلی جدا خواهد شد و راهی یکی از دو باشگاه پرسپولیس یا استقلال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30252" target="_blank">📅 20:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30251">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80H0UA8N99o4WWdddoeYpj5LK6pv7KZeKruwvwFUDWp4O539cUdNLlFG04-AdnK6OJkCDDY6IYpEeOnVbrYMFv4eeDMKv6RJgHUx4PeMyobwalJYy0nnY6j-sgJDvsQCL6AAEQFS9ZvjXsCNcYraUdR0tiVkhWNM-Vud65gOPfB3Fc7bAgZJ9mKv73C3pZZZuxG2woarUhU5oEOcLY6JvUz4u4KL7x96bjZU0Jj8BqmRViZfINaFwSWAuuGDnuVOoJ2iU-lN1BxqIIYTMCiHY7xibfccm1M8jQEo5lDXn5PoO8p3V93LpHEz8FBk8aAnF19b3eiw6EQAc03gsp_OenpwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95eba0c95.mp4?token=KVDFMjLEStyEtv4sv8N2djgkr0hBUoVbmyUQuGKie1F4LMrAjioST8iTAPcSNyjTxZK4zDUw-zWQvsQf5EBzFwwSUj4eTYOICDwB2N5Erp_yoFMa1h0AJxCYBXHfyezXPBXKlpjxKxTAjnR38kkvfP-DF411AiVCuGKKe_aYqWHlKgi_G_2nHYdJDOWpqeA2kQl4lfILseztGkWQMsv2n_J9EkueA19QF7xkUv0PM2ghee4kdwp9WCTcMoiBqW5C10WGSi8Zsn631-Np7NkhottbLct6gJBvuKIjBcFflI6E-eE5q_aIoICnfcjq4EmOD3zfTPsvw2HisboyYU80H0UA8N99o4WWdddoeYpj5LK6pv7KZeKruwvwFUDWp4O539cUdNLlFG04-AdnK6OJkCDDY6IYpEeOnVbrYMFv4eeDMKv6RJgHUx4PeMyobwalJYy0nnY6j-sgJDvsQCL6AAEQFS9ZvjXsCNcYraUdR0tiVkhWNM-Vud65gOPfB3Fc7bAgZJ9mKv73C3pZZZuxG2woarUhU5oEOcLY6JvUz4u4KL7x96bjZU0Jj8BqmRViZfINaFwSWAuuGDnuVOoJ2iU-lN1BxqIIYTMCiHY7xibfccm1M8jQEo5lDXn5PoO8p3V93LpHEz8FBk8aAnF19b3eiw6EQAc03gsp_OenpwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
هایلایتی‌از عملکردخاطره‌انگیز و فوق العاده لیونل مسی درتقابل‌خود با منچستریونایتد و کریس رونالدو در فصل 2007/08 لیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30251" target="_blank">📅 20:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30250">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=jA2J1eUPdQ_hRhQRW9Al36-8slFjRzn6eQlLVaYd-NkHCAIi3PJrDPIMm28ReLKRGUimCbagZnNt5byoWxwnxYfzr98Kj_y_MTcl97PyRXuzS_Dls4Q5SAFl5ce-7oNs_C9Vfh2CPFs5P2T2ghDsoAfqO-9V2wUtiJKyuFKfBuH7CmHcyPqF2gvzbm4LdDHNpr2TgdFx-QgxGFY3XFxM_WoLmLoCwBAADx7TDIpepGNKpIK6wASI3pktTIHAjHb1hYvxoTLS5WidmrfY63k1aRjmVkge20MMKLfK3A7e9LCxVi87CKfR5WniUFgRyPrfHJwiwFbx4TLKogSX9jPm-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bea7e3926.mp4?token=jA2J1eUPdQ_hRhQRW9Al36-8slFjRzn6eQlLVaYd-NkHCAIi3PJrDPIMm28ReLKRGUimCbagZnNt5byoWxwnxYfzr98Kj_y_MTcl97PyRXuzS_Dls4Q5SAFl5ce-7oNs_C9Vfh2CPFs5P2T2ghDsoAfqO-9V2wUtiJKyuFKfBuH7CmHcyPqF2gvzbm4LdDHNpr2TgdFx-QgxGFY3XFxM_WoLmLoCwBAADx7TDIpepGNKpIK6wASI3pktTIHAjHb1hYvxoTLS5WidmrfY63k1aRjmVkge20MMKLfK3A7e9LCxVi87CKfR5WniUFgRyPrfHJwiwFbx4TLKogSX9jPm-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از اولین‌مصاحبه‌کریس‌رونالدو 18 ساله با زبان انگلیسی بعد از پیوستن به منچستر یونایتد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30250" target="_blank">📅 19:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30249">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f90neSjEg3a5YOg5NzhVbcfu-zFykIdGH_n6_thxW-JKPNbxLvCL14vp4-x-yeARNDodrqMqgqBlgeiT-RaBf_1AWJG5sEqa97CJJ_1NPNcl-nUrNV8rWoZcI-JaXCl5kPVuNg3reee6hrC_YthXyZdCeFrWf8ugXmyYH_z7Qro9NtyEfKs9A1Un5IvsME0uZHBgYTZeZfl56uW4MODtvX1yJyXx-AEEd9C8A2eqNyysrpULcDSWuEMY-UxIeCJX2dqlO8FhGdvPGwA9MNT2Iya7tnEpL0bDu9FtWadOSZzHfMga_0gSE-iouqu-DgUY6ou1DqE0ox19fXaXZNUkBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شیخ دیاباته آقای گل سابق لیگ برتر:
استقلال باشگاهیه که حتی آدم مرده رو به بهترین فوتبالیست تبدیل میکنه. حقیقتا من‌قبل اینکه به باشگاه استقلال بروم هیچ تیمی بدلیل مصدومیتایی که داشتم باهام قرارداد نمیبستند اما اومدم استقلال پیشرفت کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30249" target="_blank">📅 19:37 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30248">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=uFnWIPMs6aIgFwTaii6OrdwHfT4dmD2eMUXXSADet_C-OVf1RliRV6MRE7jR6GwaPsqtTDHKkcZHxKHHLHMTi4nvXoITT7E_zTvH5ISbPXdRzj3tRaD5LB_uhL2pXrPrquG4pDZZYKl2VIGcmpOhyyUb49DuxZQu5BWGiMEA45AjvWiYh5g5Vg3qsEnfaPWhdtNyjzZav14ZUDGVOEoaDn5F2PmEq3t9G4YIcua0cjRlAYZPKDHVWbk8DaqwW85z2R2xNiaSHt1GaIiDZ3MjK9KkrI8JoDtOEcY9Lf18wRMgavI_zq0Ma17pDCnKBH9F2N4oHgv5mWKpz8ZFrO7UkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f2af2337.mp4?token=uFnWIPMs6aIgFwTaii6OrdwHfT4dmD2eMUXXSADet_C-OVf1RliRV6MRE7jR6GwaPsqtTDHKkcZHxKHHLHMTi4nvXoITT7E_zTvH5ISbPXdRzj3tRaD5LB_uhL2pXrPrquG4pDZZYKl2VIGcmpOhyyUb49DuxZQu5BWGiMEA45AjvWiYh5g5Vg3qsEnfaPWhdtNyjzZav14ZUDGVOEoaDn5F2PmEq3t9G4YIcua0cjRlAYZPKDHVWbk8DaqwW85z2R2xNiaSHt1GaIiDZ3MjK9KkrI8JoDtOEcY9Lf18wRMgavI_zq0Ma17pDCnKBH9F2N4oHgv5mWKpz8ZFrO7UkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
صحبت‌ های جالب و فان ابوطالب حسینی درباره مایکل اولیسه ستاره فرانسوی بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30248" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30247">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TM4I7AwM86ore08KwLybLPX-TOuwOYSUmrjHbAT4YqAVif_qDgv79wFfmSHxg0ZSinY6dnk8ToxzEOTXB4dtXmM8vPCX0FRZAqTBVTKQi1dQFtHU648lcHMLZIO8ZGC3ZvPfb9p34nrvUaLlZ9gMBYKoEwJmhgWGP5revE0ol_U9e7Rh2A-7jKuQOz7XyeQSwWDxnIlC-XqM8LjcLNe3kf4JgmHyIJS-aR7i85qaApehD-jM2M3aATxNoav1HIuI5v1ez-tBtzB9vw4IymQx2f2sEG7UnfX2Mn1fcLq2-xYinXLt9XoOsbMHeRlj1aFptozkmOO3n037zqS2GuDpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30247" target="_blank">📅 19:29 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30244">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsVH7ajrR46VtL8yEwrtbP36CZ9sUMCdTmsFOeQCjThxbztBf_13b9ODg2jFYeUnqDlxYoIhvhx1xusC1zsyq1xhk7pOfy7RWjingup3OYPfW1zu9dBO-3TDMIf5BpM5F-hQ-nzpQRxEUmCRbZqTSh8CLNhOS7jNGcseJhHId4Zvss_A27tiJBpO9IwJIs1fOcf8E7pKQUHpWKjnSLwSY9PESlbEtvWGiBo9e7E-79vF4fxLpkTc_LGpKcePGcD9GLR6NnZfEwJAZDkLf8UZHLO1zmPMqx9_sZs3YrKp6tB9oVTjr__yLe-mXQDvGmhhxt89Tqu5UT0Ien9_BHIVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCjFyjNf1XZ5_GxevCZRMzC5Mt0MRLr68GCN2grHHc91d8u7Vw4-EffxgQUONuILSLteD3TtPL-9B1GuCX6phVLrrGigpMHByydchAlJSVuknWLIUPiF12Souoa2u9LXDfWbWMYHKKHBU8BDdK4LcqZ-vYEBfXUapUSb2RUdOinMpzPnNiRuqBVctpjEDt1yRzbpbh1G02066_w9PXC7bqrsXE5P6-uLmeKHQryjKNsYNFWMz4DBUn3s9GVEW7xLBsnEhErEKCaZOlz75Z-SGUlQBYThVPQumMcsgYIrt0IL4_9mEXMQ7Oqg_jQyKDRxI_F7rhg6S-7YuKjR-nv0rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔴
برسی عملکرد خیره کننده خط دفاعی استقلال و خط حمله پرسپولیس در این فصل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30244" target="_blank">📅 18:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30243">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqOStUNSrmyQ_pkV4_BQBBw-axbdMPS78LWriEs6dOwQC-gXBsH3rXbQOEIiA4oS7jAnZR07HieFPtj0sFdGIerYjBSmKEaYN6ZVPjR0S2KVZ6gUaYladEqnS8eIfZa6QHBm8BVLTc_DF5GREpuDLiNSnYlFXrXRRbL-K4SHCK8T_ZEDwEc8lHSoJ9EFqa4ZtOmJh2BrgJtdaFFy65PixvEXJvHLpZRDF8TLD9EWsDNTLYD3iBIjvUdn9RQrmH_EN0AU9HnPo7kz8WxPSjzu2fQY2PZv11ZOygB6-z4UQEgANAZNHNmxN1uIYfZwTLmgrQxnyMSTlM4fQLsarQkEiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30243" target="_blank">📅 18:42 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30242">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDQP24qsxO9H6vuA4pEE95xSxprb-hxF7J0aRKsa0AMIjCVjT_2-UM28iBreM72slDJmLg529Z8Ewc5GBF678j5inP6hpVrsk9kC8Xu48CHjEevN-75HgH8cJ9O7m5VFXdczZFQGEYCjQNDFPMdrjMDVVNTLQBeKOe_o-3-uKq9x34gjAiqQ5zifxfCEmJuejEftODrzdNsDGQAxId295h4r63nDmPB62SnsL11T77wbitWp0x9Sa-lVYSRAlOoR2LIuRY_WfsF3dekdWA3nFDUbrQQtCNI8CrVfKOm2ZO-O7yxFj81QMOWEZDU58z8upjm0ls5EI0hR0rRpgLOAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیلیان امباپه ستاره فرانسوی رئال مادرید رسما داره از تمام تکنیک‌های نامزدهای ریاست جمهوری مملکتمون استفاده می‌کنه برای کسب توپ طلا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30242" target="_blank">📅 17:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30241">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3ZOuowbkKWajMiV2HztBcteg7-V0-0eQ1mv6aogRwDElpZ0nIVOMxMk-uVOadKx1WQcqONVO4WLfQ3R66H7et1EN1CJjThSYzKJRA7ZaJYPTI_x4hW9XUpJQs14SDAsCYUncYj6up19vkmdAAsVYWiEwCZ_VSvkawkyr6sbvjT8Gkm2RfH3md2xJVyxqm2A2QxGuwxI6mGl9prRaXHo4_7Vmnd9KttucG-9By2Ky8ElpETFrJxNpSt_otaf-rRqBTx1gisiZQdvt8YA-UihOnLnel9sWHIRc9kdfsS0k7fat2eE2TSsH3kIQR0UQuoPhG46GV0TYr7-smhu61JtqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30241" target="_blank">📅 17:38 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30240">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOnkI7hpYl2_6OZcM6x00iTaywOvDkmlr450DqkEGlB9yg3oDkqxgSZ2aiLxCA5iQbd0i91RYX8HHUirxfzCTtpWZidaZD0Ga90TXDBpOPp3rWUuC-a0oCXDwbovys2hI6ikx0OlhBeAcz46zhmC8YvPFxV9TJ-neW4jfPuCXE6cqzVdBuIuCPXNEZzoBwh7DZLsBDnyh9iibtyrTkydOoaM8ytynWfb603KXHCQRnjnC_4nbzFnLeJrXV2xuiKIau9_ccgkYNcPjKTL-7gNkp07OZGsPsZ87XkXfvG-K2QccZwNuZH52f60mM23_odO7LpaZIdAbgTt7dERHuDO8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌حضور دریک باشگاه در پنج لیگ معتبر اروپایی: رایان گیگز ستاره سابق منچستر در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30240" target="_blank">📅 17:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30239">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=S2F-jH7Sv878pd79aIyD9GsSAl3krd8UHqe0l5TEDHaamfdsB4Vp8DfOLzsuGTdf0NiBYZJjqcalCWfFqsHevk-xx45IO5gS86fZWGf7chqMF3WBxsT0Nq5fEarQL3Y_zFnBb9BqR4JaxhHM4FwRLlHnWQhpqVqfN2Qw_YReXAkzhYAaSgZWVWkjR79FvaX5RTavMgK4PtkWmbg917O-6KGK_bVjcI8yk9Vw4GH3wYeYPNVjIWK8KFZA8L6sq0fYbZtopC8ArgsyzcAMeEamn0gVAGAXf9KXht0ySIRpF9MolMPBdt55lwedRzyh9Pqt76y7U6ktE4ozQLQqqByL_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c947cd77ba.mp4?token=S2F-jH7Sv878pd79aIyD9GsSAl3krd8UHqe0l5TEDHaamfdsB4Vp8DfOLzsuGTdf0NiBYZJjqcalCWfFqsHevk-xx45IO5gS86fZWGf7chqMF3WBxsT0Nq5fEarQL3Y_zFnBb9BqR4JaxhHM4FwRLlHnWQhpqVqfN2Qw_YReXAkzhYAaSgZWVWkjR79FvaX5RTavMgK4PtkWmbg917O-6KGK_bVjcI8yk9Vw4GH3wYeYPNVjIWK8KFZA8L6sq0fYbZtopC8ArgsyzcAMeEamn0gVAGAXf9KXht0ySIRpF9MolMPBdt55lwedRzyh9Pqt76y7U6ktE4ozQLQqqByL_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
واکنش‌جالب‌ومتفاوت کیلیان امباپه، لامین یامال و لیونل مسی درخصوص جایزه توپ طلا 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30239" target="_blank">📅 16:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30238">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vr2CVs3La96tNWkgzsAY3AQgCOKRYuZzw2V8P-QkCouuTVvYsttE4LQ0v_qIN4MqqGM2-q-WsXnKutG_q805OogKNiHZaftZhtNLDtKll0lGhsg8RQHFbTwOrjMkOEheLQuJGV1wxvHAlnUDSWLq451637csdVhvKhpi6x3KeV1njmeeAyrn95m3uWnMJe_UMjxWI5_GRrUADO4wSeoVNynUCdmmA3LBFE-AjorOcSi9udjGwMUdva3P1_m9LbzeUo93fqiAZz0mfdRKVYVRZxOvtA2jMTTYAsh69S78AGTTmmtax1aBoyk1x9CTU2EhcUCCcVYt7i83k4SS-17Dsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌مارکا: جانشین‌ خوزه‌مورینیو سرمربی فعلی باشگاه رئال‌‌مادرید درآینده یکی‌از دو نفر میکل آرتتا و سسک‌فابرگاس دواسطوره اسپانیا خواهدبود. این فصل خوزه مورینیو برای رئالی ها جام نیاره در پایان فصل قراردادش با کهکشانی‌ها فسخ میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/30238" target="_blank">📅 16:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30237">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=hakoLpsuwkL6RJ6829Uu7TTe1y8Z3sNniaPRtW4-J8KEmFX-Zg-bFiH5ubp3YxQ_Z7QC1fwNeAU8gENjECQ2aPtyjzl36_7N_prYdycos7FxRItc7Jws7Uf3FmUXs4xTk7DAIM2yu0c86QaZRX7D4xXZfk8VgIZItzAoIzq2GzSkfSfdW5YgT1PqOPzMAp3lY3Ldbfrw3bRpLmprTGoOi5oTcLHUo-TwErhxYv9os9TOboPMXED_GeJrt7rUUwv9ovu5gxl9PK11_IMYGImfEbQb1CUlSp2kJtdICIv5bBis93TQ2gXzzYyrJjsNKbxVYlb2xJryz2VC4J40iViA6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc524ab0f.mp4?token=hakoLpsuwkL6RJ6829Uu7TTe1y8Z3sNniaPRtW4-J8KEmFX-Zg-bFiH5ubp3YxQ_Z7QC1fwNeAU8gENjECQ2aPtyjzl36_7N_prYdycos7FxRItc7Jws7Uf3FmUXs4xTk7DAIM2yu0c86QaZRX7D4xXZfk8VgIZItzAoIzq2GzSkfSfdW5YgT1PqOPzMAp3lY3Ldbfrw3bRpLmprTGoOi5oTcLHUo-TwErhxYv9os9TOboPMXED_GeJrt7rUUwv9ovu5gxl9PK11_IMYGImfEbQb1CUlSp2kJtdICIv5bBis93TQ2gXzzYyrJjsNKbxVYlb2xJryz2VC4J40iViA6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعریف و تجمید عجیب و غریب علی رضا علیزاده از نوید عاشوری بازیکن تیم گل گهر: اگه زن نمیگرفتم میاوردمش پیش خودم باهم زندگی میکردیم. عادل میگه چرا تموم مهمون های ما اینجوریهه.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30237" target="_blank">📅 15:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30236">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHk0XPUXETBYG2vBsb1hS76_nYgZ81Cz_Es5s8cdJmWdPVDFnfDZ4zsr8wM6IROC1NUtsCYzyHSIqfHLtUep3Kon7zF8SsgmDCCAs5glIxZiCV1mD1T_dWmZUDecIRov1UE1tevOqXyi3Kw1TcH3MdFkyXF8vDmBc2sWwdn0h58ryMZ2n6EAp_XtEmGxpyJh-wDFILINUmVzCZbw5uoSSYx94I5jM-eHQYihei5auaj6M3Is2C02FPoVUG5hMBaN2h61wwVPD9wLyoadR6D_5GuY_D2vAlM3oZWlr2ddKICroM9VZBGLExQmVgy5uNFiw_qZr8Y_56Q8LDnFU0mqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
درشب‌پیروزی پرگل و چهار بر صفر ترابزون اسپور مقابل گالاتاسرای؛ محمد صلاح ستاره مصری ترابزون با ثبت 3 گل و 1 پاس گل یه تنه سه امتیاز ارزشمند این دیدار رو برای تیمش به ارمغان آورد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30236" target="_blank">📅 15:13 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30235">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQyPMtDzRgeWR5hTgXhC_Icz_ZL_kRgT3t-QtfVClzFJLOMmTEQahaa5v8IQd7MC-q_jRRzuC2enqj0StSpCc5NTXOWBLXs16OZFUc2n4eOIi83l_YuUJsz0xpoEImWdiHXbF6nNp-ZByuuFA1FPF58gtt-qz4V2LEYb6Sil9uS8Pd7--6U4WsuKHnXBYLJQGBQRa9A_wCVRDbzHQNsfJajK0kJi27HEDPrFTtM05JbVytiqJTYjBTpOx7Sa2u2VwtAAIgrAgUa6nwsEfwpzSVKftZlBltJcJX9-8E2bEm8zKY-P7lAVjNZ2yAcy-lARYFtKi-cDaDZhBbND7XUDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدِ لغو بازی‌ با خیبر در هفته‌‌هفتم؛ شاگردان تارتار درپرسپولیس امروز عصر در دیداری دوستانه با نتیجه چهار بر صفر شهید قندی یزد رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30235" target="_blank">📅 14:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30234">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=riCCmUc3GkkwykGrf_AOPIJ1nBFQoe72lx4uTDJ5K_uw3qMbNk2TGzStDAazAGkpvFn8cemDaBFqEaBQLTy8cPTtmvdzomOTWOelm2slTMuTwIKvZ4E0IXI2MkTfa-ytyGM8fD7QDKaoNMgpMBhvRO-5MuYsmcEl47s_mgpOsNQhup4YEoG_jgMOfCI5tVeXzkuSCr5ks7DGY0zGaPUOcN4FDnINcX8ZAlniWU-JepYuDucbRwMclLXPKhRNPVNAp9vWgS2gJgcrHSlg5Hp69pDP6d0rhyjCQmfOW5DqN8c17NFMFtQVvQYeNa8YSYpyDDTE-Ple96tzdUy1PA2Gxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab687654a6.mp4?token=riCCmUc3GkkwykGrf_AOPIJ1nBFQoe72lx4uTDJ5K_uw3qMbNk2TGzStDAazAGkpvFn8cemDaBFqEaBQLTy8cPTtmvdzomOTWOelm2slTMuTwIKvZ4E0IXI2MkTfa-ytyGM8fD7QDKaoNMgpMBhvRO-5MuYsmcEl47s_mgpOsNQhup4YEoG_jgMOfCI5tVeXzkuSCr5ks7DGY0zGaPUOcN4FDnINcX8ZAlniWU-JepYuDucbRwMclLXPKhRNPVNAp9vWgS2gJgcrHSlg5Hp69pDP6d0rhyjCQmfOW5DqN8c17NFMFtQVvQYeNa8YSYpyDDTE-Ple96tzdUy1PA2Gxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30234" target="_blank">📅 14:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30233">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icJW47oxLgVbXTfTrA6xwdbYdO5aW5aAdT5mb0FXaZQRKGmAmb2OeeZ47cbjanmzOtiTUuOviSe4ymtnstw6KMu2mFYC1Lz4fqUIs7dRvO1fxzG2BFtijqxQSJBQ4_LASsuPHTHx5asS0xiW1iF1j8AjSjUlgVVe6ZEsbDu25Xq5uYYYUw7s5UL3X5eR8AANpihJB5biSf5EIPfZhjxBrbF9TNSPyhO5_LhemFGTllKxW8CLSMFP7x2JiZiHi8gAZ8O6AFP8vbl5OWBwtfriwQpF0xtYZEXbmXPZ5YQv6SFx3u-EMHkFaGBOph5PL3FCC5H2730ZJdY9qkk5M_erNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
👤
#فکت
؛ آخرین بازیکنی‌که تونست تو یه فصل باپیراهن‌باشگاه‌یوونتوس 20 گل یا بیشتر بزنه کریس رونالدو بود اون این‌کار روتوی‌همه فصل‌هایی که برای یووه بازی کرد انجام داد. از وقتی هم که رفته هییچ بازیکنی دراینمدت نتونسته‌ازمرز 20 گل‌هم رد بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/30233" target="_blank">📅 13:44 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30232">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=K916gOgIGO61L04KXVTAmfPx1ZUaW2ZuEyGtKcUWBBJLYJf1T4-nGkdWin13xetKcjL64nDtpKdsUnpvEaeyjFhb314TpxoYD50623tMMF9IJyzBhgsrsBxFOpAM0PGXxaDqkbRxf6c2wlbubO3Ksb_oUfj3HyMHPJKu3yNeAqggx3uOAY3rVTFKcCir9sm2F820RJkDNk616YcuSYLD461iO0zdm9d-GgshNHuHjqtKZkKBJLRPLxTWG2KqJrmWCjIufgnS8yWkpOcmMGK-5t5n_7uEWpyt1gImS_BhJeaC9iPR0TjfYwsy5SBkNzXqvbJapejcivQGdAxTObuk7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8babc4d6af.mp4?token=K916gOgIGO61L04KXVTAmfPx1ZUaW2ZuEyGtKcUWBBJLYJf1T4-nGkdWin13xetKcjL64nDtpKdsUnpvEaeyjFhb314TpxoYD50623tMMF9IJyzBhgsrsBxFOpAM0PGXxaDqkbRxf6c2wlbubO3Ksb_oUfj3HyMHPJKu3yNeAqggx3uOAY3rVTFKcCir9sm2F820RJkDNk616YcuSYLD461iO0zdm9d-GgshNHuHjqtKZkKBJLRPLxTWG2KqJrmWCjIufgnS8yWkpOcmMGK-5t5n_7uEWpyt1gImS_BhJeaC9iPR0TjfYwsy5SBkNzXqvbJapejcivQGdAxTObuk7oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و تماشایی‌از سوپر سیوهای تماشایی و خیره کننده دروازه‌بان در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30232" target="_blank">📅 13:38 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
