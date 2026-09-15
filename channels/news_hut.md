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
<img src="https://cdn4.telesco.pe/file/WygcAuCcEozahrsNiYhKU9OCl5yh_ztITpu-NnznMYi2Oc9ZKIgyMazgJ3MHYtOJdbtXRymoKLCh2NZvrFtyf3WItFSA2MgsaKuUSf0iU8oRnIyPH_C8iofPItrGh3E7wtKpN1Q4Qc4Q-lcvqPadrwNe0m7Fv6QNx-9l0LQ7F_ZPsj0WylvwmIM-4-F1TkiyJ6Z2zC-2-7YY_TXLHP1jTd1UtUHbwwVCuO9n4OIwBA83TSPuoPX7aB3ygnQmtPBdIrDEh2CIrcBlCL2FZoC7TNcEoi-_YM-uqCEnHa_b_z-V6x5K0JWqrc7juPdwMYAwpho4lNhJJRIy0Mj-rO03_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 107K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 04:34:56</div>
<hr>

<div class="tg-post" id="msg-71650">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71650" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/news_hut/71650" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71649">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0jDSmw3T03usGSjOL5uL5MXBgIMZu2B4KznWCqw820l9B7AxAiXpODuQLPS1c5PSfTA89OFY9Ks3zy-R3CI3NxpdFGlkxNZ26Pe-ZcUbr00BqgPBkUZ04BNPl3sTXuNS_TlnJXwf-RwSyb14SuAZQ-bsvQGPVnCHVci-E9HzwW5MFV5FGryvvR80usES8UrSWBqF07UQStqYppU07pprbDMmjTPuSWUcDeYPFfKt_SO8cPB2Zmdf432gD3q5AlcRuocDegUtQ1kPDf4ugyBckwpOEdnKijX1BVVP0wquBADDmjXTQqnKKWVwd3Skh4bSA0tg0_u3C1TDLiHKGEYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/news_hut/71649" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71648">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=ougQtyWAoe3dXeUaF3inUPRvlvUX99hk3IJdIxY-JIIkOW1ajYe7PD3x9DkLlej7s-klAxRUPKg7d14BRVW0Ihu8_mahXSLljZb8jV2kHb63CFU-WT4KqqYgvssMBNITKz9CM1AbolwJA5_UKayvkqEfdky7VvIdKPjjmCTSqp1wXOGa2nbhgANF9ShTJlR99uNKNyMnp1vIkxgvOYBVgwkS5Bb7LrCXWm9esfHZHDbyHtn7Ch24JX387yzt7h9VMvPFfW_5SUhVRiSANxi3r0d19ILH3RIE3fJQd_v44EXq2m3TLS5NNzbBGBwu8ZEh3emka9WtdvLllMZYbuSAHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=ougQtyWAoe3dXeUaF3inUPRvlvUX99hk3IJdIxY-JIIkOW1ajYe7PD3x9DkLlej7s-klAxRUPKg7d14BRVW0Ihu8_mahXSLljZb8jV2kHb63CFU-WT4KqqYgvssMBNITKz9CM1AbolwJA5_UKayvkqEfdky7VvIdKPjjmCTSqp1wXOGa2nbhgANF9ShTJlR99uNKNyMnp1vIkxgvOYBVgwkS5Bb7LrCXWm9esfHZHDbyHtn7Ch24JX387yzt7h9VMvPFfW_5SUhVRiSANxi3r0d19ILH3RIE3fJQd_v44EXq2m3TLS5NNzbBGBwu8ZEh3emka9WtdvLllMZYbuSAHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل یک عملیات ترور علیه یک فرمانده حماس در غزه انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/news_hut/71648" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71647">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3D_mGOTMAd6OYgGUNceJA-gfd79ZV-gO0OckN8p8MSO_lawfzei3IS7a2miv_eT7Vi-RxfyM7eLHP_f-h6mW4HivsFYLgDKc7G7_Vsq5shdiPhk0U7rTYcTduP9qP3e1mdSh123UoczRf6U3ZrneEhkL05bLc_ohm7w8QACnGP_03wJElSAcNNj0stnO5QsPzHTyFhrbjysbf7w_6-NzqH8MEROzctLTY5NnTZyUGg_rkfc_g4ULsw5FHZsz4PfPkUg26_3otiTVraqJuFbkRYyX5XJJZxNPwiYF7K4yCN5Ep0mTvEqwNbngBXdxJoD44zaAxLcijexrqLDmYqMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم». معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در‌راه است را نخواهد گرفت.
تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/news_hut/71647" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71646">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس.
تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/71646" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71645">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itiUeTnsu8Jpb10RE4Bvb3H9ZCLhouTwXCfOiJMOOlBY3OlEFmfTj5MRvPY8uDGpq0W1VvfPeN7kpmEZknCKbEStpm93foMsSN1oZ77rb6Y5G_iW4TqJP2V3-LqcSUHb273ylFTAK5O54eSe9kdvtXLgWiGxTi2N8pPNEbGAeJxaRuI4689z1YtWyyTx1bfE2EyCGaNwHcUgXjJJH6X3svaH_a8fhnl8XoOnPaB3na4HKQg76k-HjJS6DUEjnVOECBw18d2FaMJpLnkUBLL-2bC9KXOcUakFHmWv7HYMUWfCtotG1Yk3SLpcHwmEOlMm9Dx_wz7q1sZcZK_FoHuszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
ماه گذشته، نفتکش «ال‌گایا» با پرچم پاناما هدف اصابت موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، در حالی که این کشتی در آب‌های ساحلی عمان لنگر انداخته بود، ایران بار دیگر با استفاده از پهپاد به آن حمله کرد.
این نفتکش هم‌اکنون توسط یکی از شرکای منطقه‌ای در حال یدک‌کشی است. ادعای کذب سپاه پاسداران، نمونه‌ای دیگر از دروغ‌پردازی‌ها و تلاش‌های این نهاد برای ارعاب و ایجاد مانع در مسیر تردد کشتی‌های تجاری در این تنگه(هرمز) است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71645" target="_blank">📅 23:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71644">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دیروز در بروجرد گروهی از معتادا در اعتراض به شرایط بد کمپ از اونجا فرار کردن و با این کار انعطاف و آمادگی بدنی بالای خودشونو نشون دادن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/71644" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71643">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/71643" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71642">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/71642" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71641">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMEtLvAVRW9t9Gxi9ORM61Dp7Mc7BA-dnJY4Cxr-2pD_egKR4_LkPqTmEwVvDYebPkU8MItiLL26QikxLtgyvwzBtmyPFb75eCIK4r_D5sfbX5moWG5BFuStVh_hcTGcEbeySN-WL4-v2JpnAUDyHxL79URtERVoRocrA36WtsjLOQZpfnu-f-QN75ye96Lk6wZzzPyAS7l0Lvb-LVRVNeFAsOveBzUeOSwf2aP1xGnvfO8FbV3QQncMJniL_G8wHTqomxVQ9HdgOt7X5TBX7uLOIskPQgOBZlHGz55-tRLNXX56KLorYGC1iaHM6763uYq17Q9Ii7xR4-hKDESdww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
نفت‌کش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در جنوب تنگه هرمز، با یک مین دریایی برخورد کرده است.
تلاش‌ها برای مهار آتش بی‌نتیجه ماند و تمام بدنه نفت‌کش در شعله‌های آتش می‌سوزد.
سپاه پاسداران اعلام کرد که پیش‌تر درباره خطرات این مسیر غیرقانونی هشدار داده بود و تأکید کرد که تنگه هرمز «همچنان بسته و تحت کنترل هوشمند ماست.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/71641" target="_blank">📅 22:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71640">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=YZuISWFjPNzvGBkv4oImMszy2FsDuUKMo5VZqcfdOxTzQPbg-8Q5_CN3a2cHsmpvRN25byoGtD8xj0mpVkmvM6pHPIyF7nmKIocnm9ijdLj4mciq6bzF1WAQYbK9l6uT3bcu7hC9bckqimE9268U1FCai3wnl3hYCC5MToalm7M4wsmPJeqesvVIqZJs0V1bpudbtfohDlMdeUOo2Q0vFe0ujnufs0hk_QuBEkHHONXvts6B8wwPK3ZHo0QwlUfaCMv6Pauh18LSDYX3ADMgVzpBiOSLItGshz74ySyvXloL9wpA8ZWV1CCqoTU2_gqkGyKASs5OTPjdBusL-xCG1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=YZuISWFjPNzvGBkv4oImMszy2FsDuUKMo5VZqcfdOxTzQPbg-8Q5_CN3a2cHsmpvRN25byoGtD8xj0mpVkmvM6pHPIyF7nmKIocnm9ijdLj4mciq6bzF1WAQYbK9l6uT3bcu7hC9bckqimE9268U1FCai3wnl3hYCC5MToalm7M4wsmPJeqesvVIqZJs0V1bpudbtfohDlMdeUOo2Q0vFe0ujnufs0hk_QuBEkHHONXvts6B8wwPK3ZHo0QwlUfaCMv6Pauh18LSDYX3ADMgVzpBiOSLItGshz74ySyvXloL9wpA8ZWV1CCqoTU2_gqkGyKASs5OTPjdBusL-xCG1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره سرگرمی های روزمره :
سودوکو بازی نکنید اعدادی که کنار هم قرار میگیرن یه رمزه یه چیز نهفته رو آزاد میکنه
فضای سیاه سفید تخته و شطرنج هم شدیدا جذب کننده اجنه هستش
🎙
مجری:
اونوقت بگو هیچی بازی نکنیم دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/71640" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71636">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bxt0EQCo-qljsgizjuqdw7phKAME7cLi8bzL34_Lw-MxUHZ7J8T38SetEZ7ImTIA545aGv0MTy_z7UNpMkrfhVLMlHe7H_57Yk69YZcquhnLxF-N_q03Kg2aOzn1KVwjllfCg0N0hR8xQVXZ1_nMRQGBuU6boKYwLBRpx9tsZXOD67Jv_QyI66_YZs77KWAoqMITGDBQRaFyzAB8A04q-phhfpDDIFVTUlOVjfN1WIasT92DKiD5l9x3deQJ22UcdNzypaCOP2Ep4d1zKtI1OQx6XvxKWfArqqktc0ToxBDl22nMUzct3KHgLr7_WArlcoAXC_22KduIJjEJ5bbYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Vo9MfpysCYX2Rn-IZDlq5CYtHezPBT8p2FKKzoV4cV6_SRfdp2jQ6lvEFydWg-x30McNBVAGPZLRRLYPKuUoe_VnlwtQsUKFQjJGzcbbLSYCyYd3PScJTojb-FRitivn9LOWLz6kVb-hj_G7bY6hb2_emV2deXPtUDpZmRNcRj5DRFzswseMxiY-gsAT08Q-H1qzjfLWiVPOfOtpiBQ0d4nLpS_W47QquEeSLdVm0wnUEla_HECHeHbu9C_AvXRKE9QEk3RvWh7FVohxySZCxhCGpPDU2s_nYAiGmEJSd4wLNOHgvsYEqQIAn3S8elfKaIvkai5m7-aByS6lZ_iZ6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیامکی که داره برای مردم ارسال میشه، از فردا رسما جانفداها برای شرکت در دوره‌های نظامی و امدادی، اعزام میشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71636" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71635">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9266483.mp4?token=bJ03AZ7_efJ91XVgIr-7fyMqReGTgNXAyKPDrfrgHylvDrqyV-vN3IsAILlOknHQQSTIKjdLqj0yfS9PlG6F8Ph3sEc6_clLy77-Lhm1MtOFWbOI-EBhz6zW8g5vlQeqr4ytwjf5YAtF_avSyqfNwNo0k1db8ouo9clNrN17lj3qnHA8QpdFz4s8-k2GaAIWn4MIyL8X5gdoLrtC9uuSn1ePlRADzDsrKazkn9Sn117eeTW1wxMpLXxHIhl0M1sRCQcmIhrfS-4s_oeNib7xushj_ffSXfLaL-26RgLLnZyQ0f7FU39uAVdkPzASbi8tHVXDyCYgBU7xfSCSMQ2ndA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9266483.mp4?token=bJ03AZ7_efJ91XVgIr-7fyMqReGTgNXAyKPDrfrgHylvDrqyV-vN3IsAILlOknHQQSTIKjdLqj0yfS9PlG6F8Ph3sEc6_clLy77-Lhm1MtOFWbOI-EBhz6zW8g5vlQeqr4ytwjf5YAtF_avSyqfNwNo0k1db8ouo9clNrN17lj3qnHA8QpdFz4s8-k2GaAIWn4MIyL8X5gdoLrtC9uuSn1ePlRADzDsrKazkn9Sn117eeTW1wxMpLXxHIhl0M1sRCQcmIhrfS-4s_oeNib7xushj_ffSXfLaL-26RgLLnZyQ0f7FU39uAVdkPzASbi8tHVXDyCYgBU7xfSCSMQ2ndA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
سیاست ما روشن است: ما به نابودی زیرساخت‌های تروریستی در «منطقه امنیتی» لبنان و رفع هرگونه تهدید علیه دولت اسرائیل ادامه خواهیم داد.
به دشمنانمان می‌گویم: اگر تا به حال درس نگرفته‌اید و تصمیم دارید دوباره به ما حمله کنید، ضربات سنگین‌تری متحمل خواهید شد.
هنوز کارهای ناتمامی باقی مانده است و به یاری خداوند، آن‌ها را به سرانجام خواهیم رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/71635" target="_blank">📅 22:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71634">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7k7CjUnQWFPTnRb5gQCV8e6QbSye-4wtiwkqaIAX3PAFuNjqlYWubrVPdNXOjpJUmzj4x8dTIqGpHnZyqMZ4xlafQwVuvCbWgKaVWHrdjhJrWYAv240sCTLW02TGrlImsOAJLJIbZ_8Ofm_uBvcbC9DimD_as_12zkJF3WvydlvgXBaKxEqnNbFgvBG_4xNU6yoFKUGFd3OG-23eBQWMoJ3pAZM7aDvdajaB_V_yx36759cpmd4WfAQXzTvwSstfDRc23mX56vWzeX-rOxR79vn6C_8h_vHWRdcPulf8ucFeLf6KDwbcgR9YTU_mPiLaFOxyUEGiRntMoqTRNCESw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری «عملیات طرد اقتصادی» (Operation Economic Outcast) را با هدف قطع تمامی شریان‌های حیاتی مالی رژیم ایران و حامیان آن آغاز کرده است. به همین دلیل، من فراخوان جدیدی صادر کردم تا افشاگران اطلاعات خود را درباره کسانی که اقدامات تروریستی ایران را تسهیل می‌کنند، ارائه دهند.
خطاب به هر کسی در سراسر جهان که اطلاعاتی درباره این شریان‌های مالی دارد: این فرصت شماست. اگر اطلاعاتی قابل‌استفاده برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید؛ فارغ از اینکه کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند. اگر چیزی دیدید، اطلاع دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71634" target="_blank">📅 21:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71633">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4USVGQQ8wh6geSIohNIzunH9IHGvvBpVq07lyrGh_rRXQPOBvKFMqeg8qp3Kap0skgr3oIFDUuvSipRqOIW3lMqY4HdLJ7gtL48mkvPYO1BzyuNRl6paCaQ2875ccIIZbNAPqGP-pYZ5r887Vjmi2xMhh78sAwSpZU6g0cxu3IFvG9Et3Q6o5HmjsW3uoG6U-ye9ntYpEtOif6Carr8OtFVg438XeQH0EWsD7mY2carp8ihqER3X7X23DqRdvkdLILYH6-PPELdBQEUkMlutrO_6VwbeqY9umVoM_emfyohLBrbpN14gT1vfqVVCjaOVJFWP_9Rz9Gq2_GM015mwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
نفت در حال عبور از تنگه هرمز است.
کشورهای جهان — که هیچ‌گونه کمکی به ما نکرده‌اند — باید پس از پایان یافتن این غائله و فتنه‌انگیزیِ ساختگی، هزینه‌های ایالات متحده آمریکا را جبران کنند؛ و قطعاً چنین خواهند کرد.
ما این کار را بسیار بیشتر به خاطر دیگران انجام می‌دهیم تا به خاطر خودمان، و نسل‌هاست که چنین رویه‌ای داشته‌ایم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71633" target="_blank">📅 20:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71632">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSVoZlF1LlZnWROyvtLqR2XX9g1ExyS0Oeehj-T0vi6fdrR1VmIKYgS7nVMNDuEcq9lxutYbIppQ5Pv7_pQ3JiHKeS3D3jCJDbCfs4e4XEVm0CGJPLrKO5LM7NcCtkAFwHN7pVltTfn6eETY06LegrjmfuvxfJQgqfQRB09jY2kTGtZ7n83B218KfCXunapHIDd98wmKXaT9vNAbo360kCbebbsdg-juSudBj8NZ5JeOm07L86jKzrtDi4ev6-sV02LNJai7UjuwoXtxk_5JB1DXi-gGKECEH7tPJpa3azze7CYwokX9CextIZN5Fj68QlAwjT4IOIPQxznbGKRI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
امیدوارم همه متوجه باشند که افزایش قیمت‌ها در سراسر آمریکا ناشی از عملکرد «جو بایدنِ خواب‌آلود» و دولت او بوده است، نه «ترامپ».
حتی قیمت نفت در دوران بایدن بالاتر از سطح فعلی بود، حال آنکه ما مانع از دستیابی ایران به سلاح هسته‌ای شده بودیم!
به‌جز نفت که فعلاً وضعیتی متفاوت دارد، قیمت‌ها به‌شدت در حال کاهش هستند؛ قیمت نفت نیز به‌محض پایان یافتن درگیری نظامی با ایران — که زمان زیادی هم تا آن نمانده — به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71632" target="_blank">📅 20:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71631">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoupUfQCa6tfug5nINqMNv57_tdZHGiMNexruJSJdjPuGCLHGcKsYLZwNn-DUMScoxcEKvarOuDORAiV7FGG0c3KLZuPVV-s3p9Oz5iFlvZdxkkRkZ_JCcChmCumw0JZeXSG6Z5zQz9oRSbit2gUQvT-BbA5any0SEeTTiKHI8aeTHXj5DxMFLbIrfEehPqNLo203YnLGxM6BMayzdh_RtJEzlmOCq8F778ERNKH69NjTXLRifsddT7fFu1QuVKzo8Fs5e7jZMuNhZUyjKefAwMbeJb5EQ2WnAdZTm7wREJkgi_KzwxCpzLW93KVOgjf8nVB8TjzX5gT3fhz-MeW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
من به تازگی گزارشی دریافت کرده‌ام مبنی بر اینکه ایالات متحده بیش از هر زمان دیگری در تاریخ خود، سلاح‌های نفیس و ویژه تولید می‌کند.
این سلاح‌ها روزانه به نیروهای ما در خاورمیانه و فراتر از آن تحویل داده می‌شوند. کارخانه‌های شرکت دفاعی ما به صورت شبانه‌روزی در حال فعالیت هستند و همزمان به طور متوسط هر کدام ۴ تا ۵ کارخانه جدید در مقیاس بزرگ می‌سازند!
تمرکز اصلی این تولید بر روی پاتریوت‌ها، سیستم‌های THAAD، تاماهاوک‌ها و سایر سیستم‌های موشکی استاندارد بوده است که ما در حال حاضر تعداد زیادی از آنها را در انبار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71631" target="_blank">📅 20:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71630">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
تسنیم:
ایران بارها اعلام کرده است که به دنبال مذاکره برای رسیدن به توافقی با دولت ایالات متحده نیست.
ترامپ همچنان ادعاهای نادرستی درباره توافقی با ایران مطرح می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71630" target="_blank">📅 19:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71629">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  «ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد. این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/71629" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71628">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgt3dCQEOp8-kO3RgfzO4jGHzoWbnWRcxaMGiUg6cCNvHsvRxUxGUJDNHU7t1C78QsEDl1CVJEmgKKqphoug2aQo7tfSPjRtqmuPWBqfyMQKN7WRaoQfDdeGLx0Eiy1sn_nixbQHdkUtfG8SerO1eion4zXmhN6L2YolQIBBe23cwm8__FDaJF91XKtcfDI6mFXjqBchAcKlubxSX_YGJbbKXwrpgj5V3QyR_W92Ic7OARYeiRWUIwXF82R-panCX6P1WX0Li1A1j0b7yfJeqN26Nxi9DlzfJMCktnYIPzEm2TsG6VXh7-tAU6oJu-XN6ep7euPxqd1m8WUooGtrnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد.
این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71628" target="_blank">📅 19:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71627">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=sKsOEKf6MesSJtz1KUMS9if6uvAFYYCLCu2inubSU6NGQLsc_RzkmnFJB6GKCSbHmZz7IzmEylEdRkgBh4s8HCTvVM2b3UhzqRPczCV0hcP_2XitHVl_Xvn_aqgX9mfbtBqlCSynZd-B7ZiXK2b_6QBu5gcjMV0zjtTFZlMz6RnXXitiSdskRvkCSBGh02uiynENBqFchub40pXOhPd5uLzr_9XFiW_EQvhXIKpZ8sPg2UvSVRxpBfyVzaG_mIYodY_54pTY05dJIaSwnFb_GA_kpYg3iBZqniXDDcZnv2StpK0QKSp5CUX4ZnvWLAdbkaqQXkGqPgqIIuQcndcqOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=sKsOEKf6MesSJtz1KUMS9if6uvAFYYCLCu2inubSU6NGQLsc_RzkmnFJB6GKCSbHmZz7IzmEylEdRkgBh4s8HCTvVM2b3UhzqRPczCV0hcP_2XitHVl_Xvn_aqgX9mfbtBqlCSynZd-B7ZiXK2b_6QBu5gcjMV0zjtTFZlMz6RnXXitiSdskRvkCSBGh02uiynENBqFchub40pXOhPd5uLzr_9XFiW_EQvhXIKpZ8sPg2UvSVRxpBfyVzaG_mIYodY_54pTY05dJIaSwnFb_GA_kpYg3iBZqniXDDcZnv2StpK0QKSp5CUX4ZnvWLAdbkaqQXkGqPgqIIuQcndcqOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ رفته ایرلند و چپای ایرلند هم برای اعتراض این حرکتو زدن؛
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71627" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71626">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71626" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71626" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71625">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmQkFJkRe5LWxwm6MvnTs-IJ1E0Wxbrupm2bPP99PwjXbKIERdjOoN9znp5IKFLzrERbfhMswcgiP4WcnNRYWG99KMnrceV18leFnasOS0MR2kafd8Umr5KwXuq5UfSftRlo0scw1QMY1VH-saTQEPFWn6x20Hr2mgM2pB3qbt7ogIfwW5DuSGW-O4csyyJJxNkWgCGdnnMJFPIwy2msVmgL7lDRwj4nRsn91hd8i-gEDT_m0WibCeFVQJ2jOkkUHqxWBiA6j_N-WnR1dPQqFoq0qk9yzUQZoMZdvCr1LvX8v37vz4WTwHM1we4tk-Z6XtNCe5NDQ0COul8mRx9-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شب بزرگ فوتبال آسیا !
نبرد هیجان انگیز
⚽️
السد
🆚
استقلال
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل دو تیم باهم:
⚽️
السد: ۲ برد، ۳ تساوی و ۱۰ گل زده
⚽️
استقلال: ۳ تساوی، ۲ شکست و ۶ گل زده
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71625" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71624">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9hTaQzWvXPzyy1LLLkjhjRnRLiMhDm0uYQxKxxfwnhC7QrepdyVUAMkxRFZBn1bNNhGyutyUGJ9D4O1GxcrGbxE9UtoH6H2QoUce_z6Qxxw7QV3h_skXOTi7kzgm0zHSLDKmlthqysv_L7rcwnzvtPL-OmTR5Q3B-lHLwFFREyIVzKS7pOyxjbGKO_YqXiWaj-mJf8eg7ESF-iuVBWbyfiiTKxBKNPiN6hMooLQJb67EnlbaSlfwnSpC2x6jPhSNDj9IpnOFqkbiC1fhljh5mKsO9Ag4vz-vUgKxBN9EHZJs_LcRwWhkxmjQaEWh3rfH_XVb7BJLeRtgdIt9OMcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
اوکراین موافقت کرده است که به تأسیسات انرژی روسیه حمله نکند؛ روسیه نیز متعهد شده است که همین کار را انجام دهد!
افزایش قیمت جهانی گازوئیل عمدتاً ناشی از جنگ روسیه و اوکراین است، نه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71624" target="_blank">📅 18:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71623">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
دقایقی پیش چندین انفجار سنگین در چابهار سیستان و بلوچستان رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71623" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71622">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
ویدیویی از عملیات نجات افسر تسلیحات ملقب به "براوو Bravo"(زیرنویس فارسی)
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71622" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71621">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctcEcPGIehp7Kx4Je-u6VzKJejDoST3uZswmPdmBM38cC6naCeK-F79SRlM-6vvYYFJGWZPIGSOdIbOzzuMhFIr5ClCQzbi-f74SoSoEgRpJpRltCF4_k3XNiFXyZTSs6Jn5RK2luD0r9QX4-2se78buC9SjfDNoQS-4-cijyxLsHN6DVeUn0VsAiLkWb_ZS2Bq7Hl7BggDG0S1TuCa30RcJKV-st4CWjQTsHpEePgYYov3xDZPN2bkMDTXweNSE5PkXHR0UYmkn-W0sb5c1l0DtM5s7AhoRNP73NdUFB3e94Q7izhvPc7tsFCx5SY-N9WeVH3FeFa4crklNEKTFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو هفته آینده برای سخنرانی در مجمع عمومی سازمان ملل در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71621" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71620">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=d1ZxyzES8ByhpN74Uv4BAmoh0OgVkWXBXmNHYUYf5DlVjJvYWlJDUiLqMcLNuquWz-qD6qDQYCv8h7VpW3tlOXKdUl3HHwitmoew30FsqfAWxI556VWZFu2G4NH3yHMWNVdrJIsQr8d0VNEb26zePxCOAy4AP2Okxni0xpVGKA6TAxQfqq_xXB-Bunrie00pFgqSWMJhj1R-tcPngCQQJaLP0t04s9txn1ycjicxjlcrf3BA_KY5ZHcls7q5H_KyI3GzFQFswDzQyB2erUZXscNnEy9oO-Dmfmml3bSwAhOlRHKYDSrNuLe28YFftg7xeqSzNc694OMlxY0Ie0tXRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=d1ZxyzES8ByhpN74Uv4BAmoh0OgVkWXBXmNHYUYf5DlVjJvYWlJDUiLqMcLNuquWz-qD6qDQYCv8h7VpW3tlOXKdUl3HHwitmoew30FsqfAWxI556VWZFu2G4NH3yHMWNVdrJIsQr8d0VNEb26zePxCOAy4AP2Okxni0xpVGKA6TAxQfqq_xXB-Bunrie00pFgqSWMJhj1R-tcPngCQQJaLP0t04s9txn1ycjicxjlcrf3BA_KY5ZHcls7q5H_KyI3GzFQFswDzQyB2erUZXscNnEy9oO-Dmfmml3bSwAhOlRHKYDSrNuLe28YFftg7xeqSzNc694OMlxY0Ie0tXRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک پهپاد روسی «گران» (Geran) در بخشی از جاده در شهر «پاولوگراد» که مملو از خودروهای غیرنظامیان بود، سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71620" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71619">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=fiZKPsnoeh_oX4delG2EEZnwcnwXIqrp1nvX423vbh6zhhWmLjYz6lgcQeg8SxFelw9JZqME9MDvk9UPe_k_zOxVInCmDwNZKYXCbJYqs2fjdJXnnP2A4B6i4ICGkB2yiH_wD2CZVBSQ48UB8h1v87tvMfjzRuA54TxbTQQvrSIom6HcJ_sDIdunNzrIYy_MPAKOy2V8gtMFn8zQQ9MWDqfAINyUVAbHXdXae--UzurSwTO078iGmDQIv-jvIgmkmNvrfO9okCss5K7iX1YECH7UOhDoGdcObnILOf8ADhEhyVP5dXff28bAP57C2P4QJY-huNEY9cHQ2qGbFljleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=fiZKPsnoeh_oX4delG2EEZnwcnwXIqrp1nvX423vbh6zhhWmLjYz6lgcQeg8SxFelw9JZqME9MDvk9UPe_k_zOxVInCmDwNZKYXCbJYqs2fjdJXnnP2A4B6i4ICGkB2yiH_wD2CZVBSQ48UB8h1v87tvMfjzRuA54TxbTQQvrSIom6HcJ_sDIdunNzrIYy_MPAKOy2V8gtMFn8zQQ9MWDqfAINyUVAbHXdXae--UzurSwTO078iGmDQIv-jvIgmkmNvrfO9okCss5K7iX1YECH7UOhDoGdcObnILOf8ADhEhyVP5dXff28bAP57C2P4QJY-huNEY9cHQ2qGbFljleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگزاری این کنسرت خیابونی مختلط توی کیش باعث شده صدای طرفداران حکومت در بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71619" target="_blank">📅 16:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71618">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=QVNeShKHLR8pdQKUFTw11PWVwtIsYLKWdGUhi-xByGyqeieAm1fh4tGBhIJ_7iCh3CMMhWTx3sLv28dPel22KLtBVxKH9uwooFmO2xcdGmtaY-qA_r3cqdneM_JIVFqWQg106I4yo7R4_7u1f_UbeLdZamHYnWxPInLZAwfERJcJopPeqGNpgeltkhezQIsTtpOcjFIuSpmVUqD29TQpgRFuWChJqVe5D1skplmgHadMCvRfZ3QFA9tkdqHmNfJ6Av0eRfZvusmUdAyrnpnXvSIDp-zSNLG4UjbtaVdqfODebC0kRmoGjFe_h7AUjRaNyGg1Nc9YSJ3UG4w5osf4ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=QVNeShKHLR8pdQKUFTw11PWVwtIsYLKWdGUhi-xByGyqeieAm1fh4tGBhIJ_7iCh3CMMhWTx3sLv28dPel22KLtBVxKH9uwooFmO2xcdGmtaY-qA_r3cqdneM_JIVFqWQg106I4yo7R4_7u1f_UbeLdZamHYnWxPInLZAwfERJcJopPeqGNpgeltkhezQIsTtpOcjFIuSpmVUqD29TQpgRFuWChJqVe5D1skplmgHadMCvRfZ3QFA9tkdqHmNfJ6Av0eRfZvusmUdAyrnpnXvSIDp-zSNLG4UjbtaVdqfODebC0kRmoGjFe_h7AUjRaNyGg1Nc9YSJ3UG4w5osf4ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ و بی‌بی ترسیدن نکنید اقا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71618" target="_blank">📅 16:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71617">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=mmG8xpD-VOug-25w65dAxtHitzV5iVOWQMVYravxcecCBzERODGXOyxqPP6Tnniaz0y0kwMumYVywI7nLob9F6P3m1GjCtwc4Yl7_TMpN-8xZkeR6LGWNqeNhde6suT3ii5JsemNaxFbsXP24iOVwxq1-w5rF1Bn3-FMt-jhQfCimfenpN7aE7EAp_kPtDBX3laieSw-ZxSnDPNpnwPPpULHc0yPwCoXCr41i2wjG4Fo2_FskLz_T90036hBzN23eG-9GYto67VIf2MZK4DM3DcuvxQoWYNUaidUy-wq1ik0zZM2uvAtGc1ckBRaEfo0lSZKmdtQSUDI3GRrvVEBOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=mmG8xpD-VOug-25w65dAxtHitzV5iVOWQMVYravxcecCBzERODGXOyxqPP6Tnniaz0y0kwMumYVywI7nLob9F6P3m1GjCtwc4Yl7_TMpN-8xZkeR6LGWNqeNhde6suT3ii5JsemNaxFbsXP24iOVwxq1-w5rF1Bn3-FMt-jhQfCimfenpN7aE7EAp_kPtDBX3laieSw-ZxSnDPNpnwPPpULHc0yPwCoXCr41i2wjG4Fo2_FskLz_T90036hBzN23eG-9GYto67VIf2MZK4DM3DcuvxQoWYNUaidUy-wq1ik0zZM2uvAtGc1ckBRaEfo0lSZKmdtQSUDI3GRrvVEBOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سرقت آیفون ۱۷ پرو ، در کسری از ثانیه در کافه ای در اندرزگو تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71617" target="_blank">📅 15:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71616">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=TnZlxOln6nIz5ukeqhw6-MSHGRas2vYRPMetoZL8Tw5PtXa8e9wg8zpAV_VoLsUYdfXLCrUInpkL63Awzw7lLY9yn7DmzXk5n-zF-Wb1n9fJkItY9pxsrvxutcZaFkxM1dc93cgsTQfAPXDTbFEtgvQTKnQf7QC723IKA3_M2o96FboOks3rlogjiqddLlTFOJPj7stDMhfyg0qUJEe7Ms_I-6ftU2j5EwfHw0lJe_dTIjHcSafUVHrmxJT1AHCW_l_PvJweLwuzjguOU5S6cRyERLagfShYyn7C9R0YAPy_dwisfGwjegCoX2zbg82CXOy8uqsKp3IqAb_0qaQN6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=TnZlxOln6nIz5ukeqhw6-MSHGRas2vYRPMetoZL8Tw5PtXa8e9wg8zpAV_VoLsUYdfXLCrUInpkL63Awzw7lLY9yn7DmzXk5n-zF-Wb1n9fJkItY9pxsrvxutcZaFkxM1dc93cgsTQfAPXDTbFEtgvQTKnQf7QC723IKA3_M2o96FboOks3rlogjiqddLlTFOJPj7stDMhfyg0qUJEe7Ms_I-6ftU2j5EwfHw0lJe_dTIjHcSafUVHrmxJT1AHCW_l_PvJweLwuzjguOU5S6cRyERLagfShYyn7C9R0YAPy_dwisfGwjegCoX2zbg82CXOy8uqsKp3IqAb_0qaQN6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
در ۴۵ روز گذشته، ۹ آتشفشان فوران کرده؛ انگار در جهان، یک تغییر بزرگ در جریانه
!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71616" target="_blank">📅 15:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71615">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=vc8aAvw7g8vFR7keZ14nctRzF3M2g00H3Gt-Yaav7MkyKU2ybXNnitdsWEVfCzWDr_EklrQqVJIyYfjNfAeSi9zLGyAWYBXtXVHjPNU6LdMlkPFY37E383FiAKJ_uz_JIB3WK5e2ytjRmeZr04JZ5_XYSn9wgbTMczI7Lh2CX9yfTZq90M3kP_8xUBm9JdV1QGRqcpArzDrGopJFtWkyvubUBrQXstGK6SJXftkSnqpuM70NIJolUL9CzURHGjRtsl9dzXefpKcJ4Ts0PKcYodzK1kwNyXrLPvR4VXFg-o-EMqesJCqXcuLcsuZ5zbriReKXcIcBZPyWrSsF1w0HpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=vc8aAvw7g8vFR7keZ14nctRzF3M2g00H3Gt-Yaav7MkyKU2ybXNnitdsWEVfCzWDr_EklrQqVJIyYfjNfAeSi9zLGyAWYBXtXVHjPNU6LdMlkPFY37E383FiAKJ_uz_JIB3WK5e2ytjRmeZr04JZ5_XYSn9wgbTMczI7Lh2CX9yfTZq90M3kP_8xUBm9JdV1QGRqcpArzDrGopJFtWkyvubUBrQXstGK6SJXftkSnqpuM70NIJolUL9CzURHGjRtsl9dzXefpKcJ4Ts0PKcYodzK1kwNyXrLPvR4VXFg-o-EMqesJCqXcuLcsuZ5zbriReKXcIcBZPyWrSsF1w0HpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
ما امروز از قبل از جنگ هم آماده‌تریم!
تو حوزه مرزبانی، انتظامی و خدماتی آماده‌تریم.
با امنیت مردم شوخی نداریم، ما شرایط‌مون جنگیه، اگه وطن‌فروشی به دعوت دشمن بخواد ناامنی ایجاد بکنه، ما اون رو مثل دشمن می‌بینیم و باهاشون برخوردی رو می‌کنیم که دارن با دشمن برخورد میکنن.
دشمن میخواست چهارشنبه آخر سال 1404، همون مدل دیِ 1404 رو راه بندازه ولی حضور مردم تو صحنه، متوقفش کرد.
مردم ما فریب دشمن رو نمیخورن، 30 میلیون جان‌فدا داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71615" target="_blank">📅 14:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71614">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OycgADxJvm3xeKHGQbE_yHDoUjtLQ4iZvddirRnnYPWlFblW9y-pbIjhAbYhC1dC4CLQpiIjyLFug272yyijOxrWRK3FOk3k9WNSqyOa9fQPyZaTe9GASQOS-ZtHQByvXSqwzAFPdWelZqlhNln38o6XUAyCM2yei34KN49FT741QFKLPVkyHfiZvQ7XHroHMmb3BttUWmDIw-dAyF9mzcNivamRnQXQt2_ZEo_buHm0qbZmUmJT9Ni_Dl6RzUY2fFgdFPgDuPR-gtUIrIger7pVfAZScBrtZN9GWaquxSUd0KO1zfmC8BZr1Huy0gEdgaYnWZZf5S21D707TKs65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🇮🇷
🇺🇸
بلومبرگ:
پس از آنکه اتریش تحت فشار دولت ترامپ از ورود محمد اسلامی، رئیس سازمان انرژی اتمی ایران، به این کشور جلوگیری کرد، حضور او در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین منتفی شد.
قرار بود اسلامی روز دوشنبه در این کنفرانس سخنرانی کند؛ اکنون احتمال دارد نماینده‌ای دیگر از ایران در اواخر هفته به جای او سخنرانی نماید.
انتظار می‌رود کریس رایت، وزیر انرژی آمریکا، در این کنفرانس ضمن تأکید بر اینکه «ایران هرگز نباید به سلاح هسته‌ای دست یابد یا آن را تولید کند»، خواستار همکاری کامل ایران با آژانس و دسترسی بازرسان آن شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71614" target="_blank">📅 13:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71613">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=bw_UZOAp6VTlOXRmrolZI-kOd5pncvfE_vXuTCyjnJlEK__rrKB3PVu1JfI_eV-v4HdNAQH56Lm5iLJvzTM8O3K0FIV17uDubWnp9xEHQ5qjzv-eQB7RcN6mJq8_X-LVVEC2coD_PK4n0h1nXmWtzNTGKwR-KcUakdwl6tULR19RUYRDU8JzZIaqTPoctvvmnIUtEv297P5lv3966zBcD48W10O1cdPuicq38gXLrq8ndG74pXtkTnrbZyD4eXXTvBz8-Jw1NX3tjV95xb8n045cfUUpM_ZbSlFI5hnOU3nnhfxX1YW9KPMpok8L6coy9ESqjRtXWtrLjwNoMrBwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=bw_UZOAp6VTlOXRmrolZI-kOd5pncvfE_vXuTCyjnJlEK__rrKB3PVu1JfI_eV-v4HdNAQH56Lm5iLJvzTM8O3K0FIV17uDubWnp9xEHQ5qjzv-eQB7RcN6mJq8_X-LVVEC2coD_PK4n0h1nXmWtzNTGKwR-KcUakdwl6tULR19RUYRDU8JzZIaqTPoctvvmnIUtEv297P5lv3966zBcD48W10O1cdPuicq38gXLrq8ndG74pXtkTnrbZyD4eXXTvBz8-Jw1NX3tjV95xb8n045cfUUpM_ZbSlFI5hnOU3nnhfxX1YW9KPMpok8L6coy9ESqjRtXWtrLjwNoMrBwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇳
سخنگوی وزارت امور خارجه هند در جریان سخنرانی مسعود پزشکیان در اجلاس بریکس در دهلی نو، با خوردن یک‌نفسِ یک ظرف آجیل — شامل خوردن، لیسیدن انگشتان و برداشتن دوباره از ظرف تا زمانی که کارکنان تشریفات آن را گرفتند خبرساز شد
😏
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71613" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71612">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567356c89d.mp4?token=BqTS8dMJYN5MIpiw4Rc1s9LHQuKEpS8J8pfFPFnOEhsC38UuFjG20bkErpWwTikFGmtscpjMUwWzLqXa7FXSJaYnX08RM_28T8kkGc44NdJoeekg1Rr90bXqTNxSoZdqYICEM0uGeh5QfmIPBdOAXxpF8PJICIE5Q6KnrL1Q2_ycBqHFmMeAeEE5MIGIp77LJld04hNOcNpHPaqMoayBD9gHMGxSB1wxQIgFrGbk3EXycB-gYss0HdW7ysNQfAB5NTaYkDi4gNuD_BRtwxlK7Du3CWsnjv_JAKQA1LFFlAdCvgJDWFqjPKu24lyPBgumQU6JT0p_0DaB4QG23hctUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567356c89d.mp4?token=BqTS8dMJYN5MIpiw4Rc1s9LHQuKEpS8J8pfFPFnOEhsC38UuFjG20bkErpWwTikFGmtscpjMUwWzLqXa7FXSJaYnX08RM_28T8kkGc44NdJoeekg1Rr90bXqTNxSoZdqYICEM0uGeh5QfmIPBdOAXxpF8PJICIE5Q6KnrL1Q2_ycBqHFmMeAeEE5MIGIp77LJld04hNOcNpHPaqMoayBD9gHMGxSB1wxQIgFrGbk3EXycB-gYss0HdW7ysNQfAB5NTaYkDi4gNuD_BRtwxlK7Du3CWsnjv_JAKQA1LFFlAdCvgJDWFqjPKu24lyPBgumQU6JT0p_0DaB4QG23hctUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
توافق میان ایران و عمان حاصل هفته‌ها مذاکرات فشرده است و حقوق حاکمیتی هر دو کشور را به‌طور کامل محترم می‌شمارد.
از کشورهای همسایه انتظار می‌رود اختلافات گذشته را کنار بگذارند، برای تقویت امنیت منطقه‌ای گفتگو کنند و نفوذ بازیگران مخرب فرامنطقه‌ای را محدود سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71612" target="_blank">📅 12:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71611">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rD3B7HUyyDCamfdVArpMSVlCQOGzdjsLupxubGgscFwFZ_yScz7XsZnYWzk8SDC7SkmMVQA9tHUs3pMIro-sEyGubTpMKVubCtDQcqtXIDGX9OUaPvp91xv_XG66j46vFuJMjo-BDIbyWecWu1fBIN44Y7Q5IWGqGq7dzBUsZ_dFJy8urkkgHAsNFvVhe-kWGDZdCO46g-SwFFcUX5Lvq0LbNzfq7_D3UkoqxZW9JAmq2oNrOu9hCVm9ExuxQ3z_4N34OaO0L7CtMAbLbonIYT8JOs3rRbQFYX9cODdiJGQzoUinoyU6592GQC81DKMrTryFcF_lWyKEGYHktobCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه دختر شماره یه پسرو که روش کراش داشته داده رفیقش، و رفیقش تو نیم ساعت این اطلاعات رو از پسره درآورده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71611" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71610">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71610" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71609">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azrIIJ2QPp5N4ho5LghiC-iw2JX5jPK0ZDYjzbLH6VKFQbJfpbrH9v-iQB8hVRNA1JY_9nScb5irC_D50ctodfQG4Q96Qj9w21wj-RiLKGsIA2f5t5AguRddw5ZPlwnn0qkO6740t7cVO7MQ_7kNxhbpdmwSV382bnij4rN8YOZ7OaodlvXQ-y2M2ATvOVJkZ4Gkf6Y3VmwmDP0ruidlUUrDrjviPT0gzeJP7kTDsaXhe4Y25gm6WRr9HRmyfSb6RgXmvQ0eQD1-XGgk8D06tMm05usnPqqLS_xTOItF8YBb6S_Q2BEHkcf2ufLoo44DOyNE-0-rztqO-rcuKAP7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
لیدز
رم
🆚
تورینو
اودینزه
🆚
اینتر
السد
🆚
استقلال
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71609" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71608">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001bfae793.mp4?token=aTfHQ0gHkgUvpIN4K_F06BaQMUUcM3UMYCJ47M4u5q6xUO5_D8xnv0dLbiPX9XP9slSU1hdaSlUo3BKL6y6PSSOO5G8iTTkzQspV8QhsFtZrUI49UijujjSkBwbM8jOgvYr5wnGTsyJFmFJdLfjxvVXKolupcQE0KHb8E8cXOAoyVwqaNjKANBgv8sAGIVu0HXLrhckiaFDIR-PCLLH-C6WicRrRLmFza2zw2kc4Fz4QV70PV4SlIy9XfBPV2CRrASIETZcyfUiEjNGXqdeoyvkNMjeOz-4ldUZke42zz8S79UHroYOhMf7c562iDNWVV-Mc6bBxjTHuvI7SXRD-YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001bfae793.mp4?token=aTfHQ0gHkgUvpIN4K_F06BaQMUUcM3UMYCJ47M4u5q6xUO5_D8xnv0dLbiPX9XP9slSU1hdaSlUo3BKL6y6PSSOO5G8iTTkzQspV8QhsFtZrUI49UijujjSkBwbM8jOgvYr5wnGTsyJFmFJdLfjxvVXKolupcQE0KHb8E8cXOAoyVwqaNjKANBgv8sAGIVu0HXLrhckiaFDIR-PCLLH-C6WicRrRLmFza2zw2kc4Fz4QV70PV4SlIy9XfBPV2CRrASIETZcyfUiEjNGXqdeoyvkNMjeOz-4ldUZke42zz8S79UHroYOhMf7c562iDNWVV-Mc6bBxjTHuvI7SXRD-YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
مجری صداوسیما:
اصلا نگران نباشید اوستاد خوش‌چشم مجدد توی برنامه ها شرکت خواهند کرد و انقد پیام ندید و مارو نوازش نکنید که چرا اوستاد چند وقته نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71608" target="_blank">📅 12:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71607">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=JEOdp7KbZeSxgr9CyYfqh9KclQkLdwwJPxNX5-QMDtAT6Of8RC3v7dBfwklNblYPDY6COCUhNyqhOEAsVYIWN1VT-9HXXshaFs0bfyHMV9KJ1nsJsw3t_SsjF64pMarJjHj686k7VMck6VMWH0cpOnHVYP6_T7cEjF4yBd4OxHrTQRSM4OSnsSX1h0efWH5_WTBlSHrjPrc21JL8uZMhbznryJFQq7MfL5ilLxes5uCmqcziIGlptN6vYJAk5lEiRlGLUVmubMiR9NguQgpMdoBe1bTT_9rW_o2K7Cqf59RVtBhZrDMvZ9m_gcExAAP2nWIvoWocbyW3vbHSesFf6x_MJL0HN2OzVoEV_4z0Re1RUQN_fvy4ylxuBd85ite-5wghZM5LMnaxfRd4OtwncKnKP34DJsX1Nk5dGbVADIJL3-kh__SUlTFia_30HtkAIt4e1ksg1lKJtIoESCU2rjFobxl7SSYv6DHlTcv6rrsihc_APPVxqJbOVDW-cgawFjhQDVZl3JUWV6QbYBzuVeZ-UfSNPGwjIynXOjpoL2l8YVEXTaJdN4nvhZvt07oI6eLb4EC7W4dWKelmBBDEIbWLOnUO9s0tw3IZNG-klTu26p2J9HYAvp4Rlm_Ys9YG35ahdu2EuUu-nKpt_Fz5alBVBO_BW7FJ4ce7qo4Hoxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=JEOdp7KbZeSxgr9CyYfqh9KclQkLdwwJPxNX5-QMDtAT6Of8RC3v7dBfwklNblYPDY6COCUhNyqhOEAsVYIWN1VT-9HXXshaFs0bfyHMV9KJ1nsJsw3t_SsjF64pMarJjHj686k7VMck6VMWH0cpOnHVYP6_T7cEjF4yBd4OxHrTQRSM4OSnsSX1h0efWH5_WTBlSHrjPrc21JL8uZMhbznryJFQq7MfL5ilLxes5uCmqcziIGlptN6vYJAk5lEiRlGLUVmubMiR9NguQgpMdoBe1bTT_9rW_o2K7Cqf59RVtBhZrDMvZ9m_gcExAAP2nWIvoWocbyW3vbHSesFf6x_MJL0HN2OzVoEV_4z0Re1RUQN_fvy4ylxuBd85ite-5wghZM5LMnaxfRd4OtwncKnKP34DJsX1Nk5dGbVADIJL3-kh__SUlTFia_30HtkAIt4e1ksg1lKJtIoESCU2rjFobxl7SSYv6DHlTcv6rrsihc_APPVxqJbOVDW-cgawFjhQDVZl3JUWV6QbYBzuVeZ-UfSNPGwjIynXOjpoL2l8YVEXTaJdN4nvhZvt07oI6eLb4EC7W4dWKelmBBDEIbWLOnUO9s0tw3IZNG-klTu26p2J9HYAvp4Rlm_Ys9YG35ahdu2EuUu-nKpt_Fz5alBVBO_BW7FJ4ce7qo4Hoxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ℹ️
باز و بسته کردن (مونتاژ و دمونتاژ) کلاشنیکف AK-74 توسط این بانوی روس
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71607" target="_blank">📅 11:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71606">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
اگه نیسان کشنده ندیده بودی
این ویدیو رو ببین تا ببینی همچی توی ایران ممکنه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71606" target="_blank">📅 10:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71605">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=i3mSjgLllU3EkEnSNFlIVPpl8ZmBsoiOI_wfHhtrB4FmIqaKxo5qUmCPJ2290mChabES_PZWuODu1OtIGm2rIGMAJlu5dqfHj-2p02IWdKVIdVIQ1Oz0h8YTzeF_8OdhdQt6fm5jGmwrPHE-oKSw4JiQL18GROABwF5bhd9uyE4vlfOtAMGbMNoKY_Pmuf4KHCe6SHN4BKnAh3kEyUycCvJpLqdqTzTQV6pIoMuKahenjOaoh1cgkv2cSWo8yuV3wpyCWmgC1NzX7RPX3aQI61fboUn_gWY4Azo3kaNs2ZofiYp295BkmtpTLkJ5cgYJ66iEGg8BONs6wNRkHwGQkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=i3mSjgLllU3EkEnSNFlIVPpl8ZmBsoiOI_wfHhtrB4FmIqaKxo5qUmCPJ2290mChabES_PZWuODu1OtIGm2rIGMAJlu5dqfHj-2p02IWdKVIdVIQ1Oz0h8YTzeF_8OdhdQt6fm5jGmwrPHE-oKSw4JiQL18GROABwF5bhd9uyE4vlfOtAMGbMNoKY_Pmuf4KHCe6SHN4BKnAh3kEyUycCvJpLqdqTzTQV6pIoMuKahenjOaoh1cgkv2cSWo8yuV3wpyCWmgC1NzX7RPX3aQI61fboUn_gWY4Azo3kaNs2ZofiYp295BkmtpTLkJ5cgYJ66iEGg8BONs6wNRkHwGQkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست سلاح جنگی بر روی شتر توسط یک عرب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71605" target="_blank">📅 10:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71604">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=rzYgSS67SuHatGv6nG-BVSKBt6LPq6zhWCBYZIFlLpRl7MwM8YB-fnxsnlJZJL-vrQExRmuHAYBPqn6jtvwJ2mNDB7WWnBQepoqTpc3n4ZzawbvAwXPPhMFo3yjq6D6o1aVI2sRex2_4zcUTdbca9Rmo79K2oMRCH-YFt4c_4gDZvj10JEEjCwEHsVETBGABNUhbXAzxYHIqiRZJcDD0prdJys3G7gIclNLxxDw402Yt2kT0t8KWJpG5s-0BKHP5D07-d5BYq5tr_XQA2LtsgLP8DVj7CU0tNWfPrFM5bwVgO2VDObWf0pfmLbTpSsB2yn5PD9S5wIT3iC1a_uoviQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69e312dde1.mp4?token=rzYgSS67SuHatGv6nG-BVSKBt6LPq6zhWCBYZIFlLpRl7MwM8YB-fnxsnlJZJL-vrQExRmuHAYBPqn6jtvwJ2mNDB7WWnBQepoqTpc3n4ZzawbvAwXPPhMFo3yjq6D6o1aVI2sRex2_4zcUTdbca9Rmo79K2oMRCH-YFt4c_4gDZvj10JEEjCwEHsVETBGABNUhbXAzxYHIqiRZJcDD0prdJys3G7gIclNLxxDw402Yt2kT0t8KWJpG5s-0BKHP5D07-d5BYq5tr_XQA2LtsgLP8DVj7CU0tNWfPrFM5bwVgO2VDObWf0pfmLbTpSsB2yn5PD9S5wIT3iC1a_uoviQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
زنده یاد مانوک خدابخشیان:
تنها برگ برنده دونالد ترامپ این است که پرونده رژیم جمهوری اسلامی بسته شود. این بزرگترین پیروزی است، درست مثل فروپاشی شوروی؛ این را فراموش نکنید.
چرا او باید وارد جنگی شود که سال‌ها طول بکشد و دوباره در باتلاق خاورمیانه بماند؟
هدف این است که از خاورمیانه بیرون بیاید.
شما به اصطلاح آن دکه جمهوری اسلامی را ببندید، همان‌طوری که دکه کمونیسم بسته شد و همه فرو ریختند، تمام این‌ها هم فرو خواهند ریخت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71604" target="_blank">📅 10:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71603">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
لحظاتی قبل یک فروند پهپاد پیشرفته MQ۱ توسط سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور بر فراز آسمان تنگه هرمز رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71603" target="_blank">📅 09:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71602">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
یه ایرانی رفته توی تجمعات حامیان فلسطین توی خارج و بهشون میگه <<کص ننت فلسطین>> یعنی فلسطین رو دوس دارم
😂
اونا هم بدون اینکه معنیشو بدونن دارن تکرار میکنن
در ادامه میگه فلسطین رو از حماس آزاد کنید
در آخرم شعار جاویدشاه رو سر میده
👑
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71602" target="_blank">📅 09:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71601">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
مصاحبه کامل و ترجمه شده افسر تسلیحات نجات یافته ملقب به "براوو Bravo" با برنامه Minutes 60 پیرامون عملیات CSAR که در ماه آوریل در عمق خاک ایران انجام شد.
@News_Hut
|Cataphract1</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71601" target="_blank">📅 09:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71600">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
⭕️
تصاویر تازه‌منتشرشده‌ای که توسط برنامه «۶۰ دقیقه» (60 Minutes) پخش شد، عملیات نجات دو افسر نیروی هوایی ایالات متحده را نشان می‌دهد؛ افسرانی که با نام‌های عملیاتی «آلفا» و «براوو» شناخته می‌شوند و جت جنگنده F-15E آن‌ها در ماه آوریل بر فراز ایران سرنگون شده بود.
این دو نفر در حالی که نیروهای ایرانی در جستجوی آن‌ها بودند، در منطقه‌ای کوهستانی در جنوب اصفهان و با فاصله‌ای حدود پنج مایل از یکدیگر فرود آمدند. در این گزارش همچنین تصاویری از حمله به نیروهای ایرانی به نمایش درآمد.
آلفا» هشت ساعت پس از خروج اضطراری (اجکت) از هواپیما، طی یک عملیات پرخطر در روز که با مشارکت ۲۱ فروند هواپیمای آمریکایی انجام شد، نجات یافت.
«براوو» حدود دو روز در پشت خطوط دشمن باقی ماند. او با وجود شکستگی کمر و سایر جراحات ناشی از فرود سخت (به‌دلیل نقص در چتر نجات)، از یک خط‌الرأس کوهستانی به ارتفاع ۷۰۰۰ پا بالا رفت تا اینکه دو تن از نیروهای ویژه امداد و نجات نیروی هوایی به او رسیدند و وی را به بالگرد آمریکایی منتقل کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71600" target="_blank">📅 07:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71599">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71599" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71599" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71598">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0X5bab2KVq6uSLj2SlAObR7hSxAB08mTCPoT-zLa5UeGiL8ap62Bi9n3g4u3xTd6vIbyjfDiVmX8QxnSrdgnj1kzsXMJRVZUzcdd6HWcZH3VtFM-MYBKuHlv-5fuVqnRLgJqql_7_KqRBjoiWmFt_4P2CF72vWN6L-OxYzSZ-AksMrb0SSqN286a5fxiuQhaby96gmZQ7NKCXKUW_tpYptsotGrYGSzoC6Sk6wGfTfhR3NegbE7okBLLes-s9Bdisdt83nwkPIwHDHai7k9G4msuHLN8ptEuCvDgWGNZpIQV6qavlMpPnpS2XbF3Sl7vJ6dhF1UADe1qlm1oAlPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71598" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71597">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=qusjZ2gS8JH_djt1EZR13PcY5LSV5cTR6rBpGq6h_ry6TiMB_Saoxyn_wW2VaEJGhlrWRDLKcalLcfSNXD71ecsJKIB8TLx6mFDBGoKQFcW0HDhhtW4UCzTy3N6HPheoPCywJoxmxLV-9oSSqazH5ABsNk_VKIgyadz8ET3e2ufcj5PYk9WJB4zqG1Dh-DH2S66wGmF-HpkNySFdUywDEffzoI2YZulnHJYZSMdoRmstwd9PGl192r3QfBMAZhVhU35BxgG-cr4a1xc9gqQkDTaDIcFowkVFo5fkZ68x3oTNv9EQiRGFwa7Tj4qbyzt5XUfVku2DCnRjcl_Gt6Zelw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94dc744f.mp4?token=qusjZ2gS8JH_djt1EZR13PcY5LSV5cTR6rBpGq6h_ry6TiMB_Saoxyn_wW2VaEJGhlrWRDLKcalLcfSNXD71ecsJKIB8TLx6mFDBGoKQFcW0HDhhtW4UCzTy3N6HPheoPCywJoxmxLV-9oSSqazH5ABsNk_VKIgyadz8ET3e2ufcj5PYk9WJB4zqG1Dh-DH2S66wGmF-HpkNySFdUywDEffzoI2YZulnHJYZSMdoRmstwd9PGl192r3QfBMAZhVhU35BxgG-cr4a1xc9gqQkDTaDIcFowkVFo5fkZ68x3oTNv9EQiRGFwa7Tj4qbyzt5XUfVku2DCnRjcl_Gt6Zelw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سپاه به طرف تنگه هرمز موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71597" target="_blank">📅 01:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71596">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_Z8k1xW9e4tRbnlwjfYAEl50SAtgBUtf-MyEvT4MS0oKLKe27dGsNsUZYpk64z6hB4YrdIYG7bmdeQ02jrbojcmPhKVVX8wqQe4e1pSAjB_s4vIgxtlnKpF7Sc8QblDNGrRatNKkbRxgbk3BBDQ9wEgsQjEddrLzB-sdumQksoLRhIvRk6pWF4IL5X4qiQhC_FhTGFJcb--jRkWyAuc2jb3udHgaa44RbC62SLHAFIrqgINN8ENmmJOlkYbzHkHCBnoeZ06rrv9Dp476ZcbNty37ZMW7v4-D8Qs5I0ahqbcdWtSruUy3owwSaY9TVoMmxlMJMwq8hGSoG1nvn-zlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
❌
🇮🇷
🇴🇲
باراک راوید:
یک مقام حوزه خلیج فارس به من گفت که عربستان سعودی اصلاحاتی را در طرح پیشنهادی عمان و ایران در خصوص تنگه هرمز ارائه کرده است؛
زیرا نگران بود که عبارات پیشنهادی عملاً منجر به ایجاد وضعیت موجود جدیدی در این تنگه شود که برای این کشور یا سایر کشورهای عضو شورای همکاری خلیج فارس قابل قبول نباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71596" target="_blank">📅 01:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71595">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=dJ06ixCO6GBY2r-7ab4uIaZj6Jr5fVafCo2yqSmf_j8IOI8xYoDHKJXBo3ibqQrNycJljLFsNx4XQi0PzDut1Rw4ub1gPHHuiMkJqDMklCSSn_gclzvDTM8sUnyRPudWwfKpD_XYPpZQ8Z30cwHAiU0V9AjE8KajIkfQoSjbGkRTzPaFMuY3W1vQR_f-zfgoK-TaH8muk0jEXiSKpTMIvVG9K2TAyZuTeeMVTrE7cii651-8G8LVkgV2zvvtDfDvAnsVZPAAedETspTq9Et1tzI1-s6vdBWMF5m_Jaq-hOXjzQBP1X5g6YQwa9s_WS56uRN-cZocsbaki8bV91LA8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c7311729.mp4?token=dJ06ixCO6GBY2r-7ab4uIaZj6Jr5fVafCo2yqSmf_j8IOI8xYoDHKJXBo3ibqQrNycJljLFsNx4XQi0PzDut1Rw4ub1gPHHuiMkJqDMklCSSn_gclzvDTM8sUnyRPudWwfKpD_XYPpZQ8Z30cwHAiU0V9AjE8KajIkfQoSjbGkRTzPaFMuY3W1vQR_f-zfgoK-TaH8muk0jEXiSKpTMIvVG9K2TAyZuTeeMVTrE7cii651-8G8LVkgV2zvvtDfDvAnsVZPAAedETspTq9Et1tzI1-s6vdBWMF5m_Jaq-hOXjzQBP1X5g6YQwa9s_WS56uRN-cZocsbaki8bV91LA8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
ایران می‌گوید دیشب به یکی از شناورهایش حمله شده است. آیا کار آمریکا بود؟
🇺🇸
ترامپ:
نمی‌خواهم بگویم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71595" target="_blank">📅 00:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71594">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np_S9lFWo8SMvJHsBEwEd2emIjJDcOsWocJHAi6NZtoK0lWVE8h_I1z_rEZUbgVtYJ20ua_byiOpDk-2M6l2aKrOpDuREctfEOagjqZM9qjPUnlkkRjI47xMhArNHWSYSgaS971yImdgkBnyTqss35xpCAsFGJ806SnmuQMc5ADE1CSs8sPyp1pXH-YLzZMCuLrLwi95BChltLljvtxv-Uz9e0JgIfFO6kBQ2lGQJ8w_U0pCjgmY3g9-OTA1ZBMYdykM-918NiNCKejmByN0dUgoPK0IKAT1qqn3fRgVtnmjUq0YkKXPg5-JWz_qVoJ_aQy28Cu59XAQQdt4BxieTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇴🇲
بدر‌البوسعیدی وزیر خارجه عمان:
در راستای دستیابی به اجماع، نشست منطقه‌ای که قرار بود فردا در صلاله برگزار شود، به تعویق افتاد.
ما همچنان به ترویج گفت‌وگویی که حامی ثبات و همکاری پایدار در منطقه ما باشد، متعهد هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71594" target="_blank">📅 00:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71593">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
⭕️
نشستی که قرار بود فردا در عمان میان ایران و کشورهای حوزه خلیج فارس درباره تنگه هرمز برگزار شود، به تعویق افتاده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71593" target="_blank">📅 00:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71592">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoMBUcjjSM_f0yZzlyiWfkq6-JETd0zJgvM78zHWPLmkkgmUEPBZW4Z-ubUsuMRset8MzzwADphHkghSgoikCSzYKLGHDg3rjkBCLhe-BSr9VcDeTWG-s8Ql7w4a2KQKWPBDPFKU6b_h26SKN1CKBmYuTJhJVucRy0Z8PwhV-qGQeL_SjfUTJWoSf71PEpNh1Xcm-tHV5i8oUk9CkQKXHIlM0BMHKa5gE7wv9H4pLxmuB31cdMWx3TpvM9F9lcuW49IhLZN8QtI8-ylidUPqoeS1RNvd4fY7bGRJ5cQC4_axMKTkVKPCihYi8AUFeCbfCY_nwwpkYuBce4TjI42fOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های عجیب پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71592" target="_blank">📅 00:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71591">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=KXYSY11i2kikyHJybMRgnfenTC9CIORXWfNkxI8jjtpVssfXwETflvyN9oUBjizWEh__AQ-aOIn500u9HkgF0Kes9IC2QwOeR7ThFZVwKxaS0y2bSpespU4PL4nAshTLq4zwi0N-9VmyF7LsqGrWMykbZ1wKRab3PcKh50u9EmQsAO2O-8W_zWCQ7hUMMVXbxPUyUVJhxli5fcjyqacmrTv76OrfizV575x-l6UlyHou7aFbpGT4GqelvWey_qDopGUYrt701j4EexZOKnXoLOh51y2l7P8SFgJujt2pwL2ctojWDqSdxfTJC8SU6EkFvOjYtLwTSeivVZoIkJWm_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec76e7285d.mp4?token=KXYSY11i2kikyHJybMRgnfenTC9CIORXWfNkxI8jjtpVssfXwETflvyN9oUBjizWEh__AQ-aOIn500u9HkgF0Kes9IC2QwOeR7ThFZVwKxaS0y2bSpespU4PL4nAshTLq4zwi0N-9VmyF7LsqGrWMykbZ1wKRab3PcKh50u9EmQsAO2O-8W_zWCQ7hUMMVXbxPUyUVJhxli5fcjyqacmrTv76OrfizV575x-l6UlyHou7aFbpGT4GqelvWey_qDopGUYrt701j4EexZOKnXoLOh51y2l7P8SFgJujt2pwL2ctojWDqSdxfTJC8SU6EkFvOjYtLwTSeivVZoIkJWm_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو تبلیغاتی بانو سیدنی سویینی برای novig
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71591" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71590">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZvk9HeM4RxvTdx50hKhzFZPoqzge9HgMwjDH2khWnixZ4QAL3qSOm5B_qAk0t3nsyLZqbqD6McWBlsa6ZWQ3G_MYVpVEo1jld4q_Okwyo-R2bx67TNc9Q9axt2vcftVLFpyK4Ja7VgHXM_5AhwsiPB7BA75XWssNp1LIWjAm7IByVxPPpxnRKNEZjsQvA0Fo72HPAPEdqvXOdF_4qlvr_-DmRqej_fmmmwYhlz58zlxdhaX-57gRIS6J0xLKVudE7Y-8r_HwZz6mTkwkcdIx39dYTbtDjmmt40bFJk7Imxg-nYhuDyUfI600fwcIwCD6BumRX8oGDuWoxcbnLljrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇺🇸
نیویورک‌تایمز:
مقامات ایرانی می‌گویند که رهبری این کشور طی هفته‌های اخیر بر سر دو راهبرد برای شکستن بن‌بست با ایالات متحده دچار اختلاف نظر بوده است: بازگشت به مذاکرات یا تشدید درگیری‌ها.
بر اساس طرح تشدید تنش، ایران حملات خود به اهداف آمریکایی - از جمله شناورهای نیروی دریایی و نیروهای نظامی ایالات متحده - را افزایش می‌دهد و هم‌زمان تلاش می‌کند با بالا بردن قیمت جهانی نفت، طرف مقابل را وادار به پایان دادن به محاصره دریایی کند؛ محاصره‌ای که تجارت ایران را فلج کرده و صادرات نفت این کشور را به صفر رسانده است.
ژنرال‌های تندرو، از جمله سرتیپ سید مجید موسوی (فرمانده نیروی هوافضای سپاه پاسداران)، طرح جنگی مفصلی را به شورای عالی امنیت ملی ارائه کردند. این طرح خواستار آن بود که ایران و گروه‌های هم‌پیمانش - به‌ویژه حوثی‌ها (انصارالله) در یمن و شبه‌نظامیان شیعه در عراق - دامنه حملات خود علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را گسترش دهند.
مسعود پزشکیان، رئیس‌جمهور، و محمدباقر قالیباف، رئیس مجلس، با این طرح مخالفت کردند و هشدار دادند که اجرای آن می‌تواند ایران را به جنگی بسیار گسترده‌تر بکشاند، موجب حملات هوایی سنگین‌تر آمریکا شود و بحران اقتصادی کشور را عمیق‌تر سازد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71590" target="_blank">📅 23:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71589">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=uZ_pmUv_ADdYleC5ovkeh8QKYbpyxEBB8SKqCRK3qlxfM_0_Iqx0eV0XErfYWT53vLfa5wUUqxzbvFn5rSJWJQKyCCASxcONJ7lVqNO1XmKSE5sZCAugUwxEYPwZ02nWcpD-YopSf7n3DvJvE_W0guKhxLwLW3o8i5bB-hqOfsGAX3n9MS4iERDzlo3tmo32RxwkeI_W0DM9RubKbcfx0wAbj8X4Mm4G19PK9b9LKMDIP4JMfRig_2zGjOXV2shVLtB1FfdfWd84DfRS0Jd5HfO6n5QuasOkbOql20oz02mFYxyeKu04tiVPQaxeajMrZuCTU4rpIZSTcfXWQPaT3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02f69702f.mp4?token=uZ_pmUv_ADdYleC5ovkeh8QKYbpyxEBB8SKqCRK3qlxfM_0_Iqx0eV0XErfYWT53vLfa5wUUqxzbvFn5rSJWJQKyCCASxcONJ7lVqNO1XmKSE5sZCAugUwxEYPwZ02nWcpD-YopSf7n3DvJvE_W0guKhxLwLW3o8i5bB-hqOfsGAX3n9MS4iERDzlo3tmo32RxwkeI_W0DM9RubKbcfx0wAbj8X4Mm4G19PK9b9LKMDIP4JMfRig_2zGjOXV2shVLtB1FfdfWd84DfRS0Jd5HfO6n5QuasOkbOql20oz02mFYxyeKu04tiVPQaxeajMrZuCTU4rpIZSTcfXWQPaT3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کشتی که امروز صبح در نزدیکی جزیره قشم در جنوب ایران مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71589" target="_blank">📅 22:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71588">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=EAI8abFafr3rpibOchtU4FE4JFA0KeHc4_fx-QiU6eb_K7OpcbPAZ3XbdzhMp0o7SgknfiCdim0R1zXMIQWnILI_1OQSlJQWzAAIqMGWwEx3Wj7ct63zFR2W-H-CSKsPUQkRtTki6PbgtRE7WPhfPO2ndMPIcdQ8utFGvarNmqpCKwmARCUsWDmNQrUjwjoakTA3XnMyfNe0jjOTFQjiIcd7SMEyimC6s962VymfnxLr-YWuGHC55n1Bg-iv0YKym-U_PVp22ox0csU3SVsaUSioo-M_SBAfMQzhE6fegYEY6JKtxYP7kAwMZhBE3QRIew6ttINuYFoI5UiX5XMM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ae06116.mp4?token=EAI8abFafr3rpibOchtU4FE4JFA0KeHc4_fx-QiU6eb_K7OpcbPAZ3XbdzhMp0o7SgknfiCdim0R1zXMIQWnILI_1OQSlJQWzAAIqMGWwEx3Wj7ct63zFR2W-H-CSKsPUQkRtTki6PbgtRE7WPhfPO2ndMPIcdQ8utFGvarNmqpCKwmARCUsWDmNQrUjwjoakTA3XnMyfNe0jjOTFQjiIcd7SMEyimC6s962VymfnxLr-YWuGHC55n1Bg-iv0YKym-U_PVp22ox0csU3SVsaUSioo-M_SBAfMQzhE6fegYEY6JKtxYP7kAwMZhBE3QRIew6ttINuYFoI5UiX5XMM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
زهران ممدانی شهردار نیویورک :
قربانی اصلی حمله ۱۱ سپتامبر عمه‌ی من بود که بعد از اون اتفاق نمی‌تونست با امنیت از مترو استفاده کنه چون حجاب داشت
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71588" target="_blank">📅 21:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71587">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezx5_pUbU18oJCbfiJjq3hkSRt5usjAY7IxgybZ8NQozNBmXR9y5O_dU6ZbXC256aWfKfdHD8M-teNDJtwudXXQ6I1R_cIVX2-2AWRK7CgbfuKcWYQ3f7rNbsV4ydJhlxka86PX-z41rALhAYnz3tQbHu85HvbSE2dlL_MC1r8otJMbtg42W1iGRFaPfuiWcjBDHzgxwshq7KRLdS2teESuwlzcXakpI2J_XrUZtYLijkIOR29I_OtYSeDC6BVD9R7N34b5lwihjVXIoeWs0EltLVc0qtzV6V3bZpGtsSxHAzsOU9GDcXVlWGHYNNpDgWjeRs9n9acy5egVDBExw4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧩
🎮
کنسول بازی ps5 pro به قیمت تقریبا ۳۰۰ میلیون تومان رسیده!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71587" target="_blank">📅 21:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71586">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643027f01a.mp4?token=P8dSbQcP-D-0jlcv7r-xSUM3BJcEnyQB27Uoi5AF9xBHrxqUSDsBSx6mnXJt0DoB7VTY29Ed4a7pga-rzg11q-SBgw4S_nGmtg_BvJ3DTRQ9WqNK583AdlCRrdzRz5izMQkOThmPjr-rlySRFugj1ZRPo-CbdRxKESfzou_AZRJNrhJDBSrf41Do9462VcvS8rPZffXVzpU9exuy1ommCXZqRKprn4r0ahbwUm1das2BXpKpZTXGmppEn84rBCh8GLke01MZJLNnL0uu9Y7qMdnujv4KPhOL520MJ46-bEUNixUWKMfHryxecbt6LqtS-vMI0IpAAaky8XnLClUseA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643027f01a.mp4?token=P8dSbQcP-D-0jlcv7r-xSUM3BJcEnyQB27Uoi5AF9xBHrxqUSDsBSx6mnXJt0DoB7VTY29Ed4a7pga-rzg11q-SBgw4S_nGmtg_BvJ3DTRQ9WqNK583AdlCRrdzRz5izMQkOThmPjr-rlySRFugj1ZRPo-CbdRxKESfzou_AZRJNrhJDBSrf41Do9462VcvS8rPZffXVzpU9exuy1ommCXZqRKprn4r0ahbwUm1das2BXpKpZTXGmppEn84rBCh8GLke01MZJLNnL0uu9Y7qMdnujv4KPhOL520MJ46-bEUNixUWKMfHryxecbt6LqtS-vMI0IpAAaky8XnLClUseA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
مدیر سامانۀ هوشمند سوخت:
خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71586" target="_blank">📅 20:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71585">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
اطلاعیه قرارگاه جانفدا:
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71585" target="_blank">📅 20:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71584">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=hqog6Hhmhfv2U6jODnvgkyqpKvTP66jA0-IOb4nHodcVqnq3hKKwzLy5cdwQioexhB0ktKDEqJfFnwERKGPWNiUa-EvrOmvunZZvC--yrJWRzW12KSmlNjR_zH67sF0yxg3ldtkt34D0HfcDQ_ctY8CRv39d6xpISpEOhIVhh6N3u8Le18STuwtnCXyvRCUCbMQx6QiDuh5mxSqCX63ikSbFJBF3SzVtoZaIqRXzIZa60ftzkr15PT4Bfkh3LKSXlapJTL-JXH-2dgzdFlZS-r2yyDsO81DgGZ9LfxoxaSlaZGQPHHzVxms1IGcdUSJjOzLcMO-1hCEUQw6f-_WnZhQsTFVw8bbsiyeWv4MefCIrTeYDY6e32F5YDt22e52pCJeMb2VeIiDHUDQ6CGjippHxnDQfGt4IN4dNj0PW4tMce5bGA2XIJx_qyCgB9rLux5z9wRhb4HPChPBx9WX5nP3VPMNYF1lOomQvzdxFRKkL1UoVOnou8nBssSqCUogDcbZTz6vLYDkde964eMglqJlYaXhACSiCa8FI9KSr4SOAcLwKQN3vI7JIitvHLI2up38Mg-4clM1lb8RZ1dhlv7z-EizgTBYO9i5ACtyJYDpUFktYle0Ds1OYkaTJBrxEJO6vltUr5yDO-JIcuVwTmEGfq4g5u4jlUP03yNfrqxc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c23e20e2.mp4?token=hqog6Hhmhfv2U6jODnvgkyqpKvTP66jA0-IOb4nHodcVqnq3hKKwzLy5cdwQioexhB0ktKDEqJfFnwERKGPWNiUa-EvrOmvunZZvC--yrJWRzW12KSmlNjR_zH67sF0yxg3ldtkt34D0HfcDQ_ctY8CRv39d6xpISpEOhIVhh6N3u8Le18STuwtnCXyvRCUCbMQx6QiDuh5mxSqCX63ikSbFJBF3SzVtoZaIqRXzIZa60ftzkr15PT4Bfkh3LKSXlapJTL-JXH-2dgzdFlZS-r2yyDsO81DgGZ9LfxoxaSlaZGQPHHzVxms1IGcdUSJjOzLcMO-1hCEUQw6f-_WnZhQsTFVw8bbsiyeWv4MefCIrTeYDY6e32F5YDt22e52pCJeMb2VeIiDHUDQ6CGjippHxnDQfGt4IN4dNj0PW4tMce5bGA2XIJx_qyCgB9rLux5z9wRhb4HPChPBx9WX5nP3VPMNYF1lOomQvzdxFRKkL1UoVOnou8nBssSqCUogDcbZTz6vLYDkde964eMglqJlYaXhACSiCa8FI9KSr4SOAcLwKQN3vI7JIitvHLI2up38Mg-4clM1lb8RZ1dhlv7z-EizgTBYO9i5ACtyJYDpUFktYle0Ds1OYkaTJBrxEJO6vltUr5yDO-JIcuVwTmEGfq4g5u4jlUP03yNfrqxc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی آموزشی برای دخترای موتور‌سوار چنل که قطعا بکارشون میاد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71584" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71582">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p0culsymbWbBM5du-0_vY2fIxUrNH5UwtwsDws1xZYYN7xt65TxPV47t1uq5_L3LCh4V-M-b95GO4E4WEuUz9N9I1PgESDVl3dibkyYQ_eDwDpW52HvilO1AwbSFKvdBO6kXN-TMz0hhDmnwael6gd92W4XhgjV20wghzadIKLoIGw69uFHTM2mQNeC-k2N5mEcW2fEM9f0_2i8P4W-dNH5vpk2EW_Ckr-goBZxdfj-LDb4xCPJMJQWKlPYCYbK-HphVh70HnnHw5P9D7jpwVYLof2xpfR6r1RNGMH3vSus0K_B34TSp1GalRw5hLHx987CVFneAQwd6t0ZZqDPRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u13Y0blFY04SjX3TDW_NWwYWxLGawpicRhMnFXOHYJFJtVF6mZU0z-3v--ZcePUZWUbri1JUVmXjMRDFCJH772blVc3oFljxpVAwxh4mq_5jJ48CAepyHZUhmlXUvIdESMnP14iHBmk1iEQrkL_I2C7V9QCH6eURbSuQIYScHAQFeNin825PsdS3PS7RzNHNNfG1GnI4qrRiIl6j-LOWSDkP5y3xNXwke39WDS-AyZm-iD2gp2xcG9FXUA8KHre2tpBLhkfQeflbvvtbBItX2OoLoJzM8AQ8kcgruAUBei6OLVSs4IBJkTyO-ovuqwB-y6u__Dh6ASymjbUDRc1JhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👑
دفتر شاهزاده رضا پهلوی:دستگاه کشتار و سرکوب جمهوری اسلامی بار دیگر قصد جان یک زن جوان را کرده است. سودا (مرضیه) ابراهیمی شمس‌آبادی، بلاگر ۳۳ ساله اهل بندرعباس، پس از ماه‌ها بازداشت و تحمل شکنجه، تنها به دلیل فعالیت رسانه‌ای، در بی‌دادگاه رژیم با مجازات اعدام روبه‌رو شده است.
صدای سودا باشیم و از همه ظرفیت‌ها برای فشار بین‌المللی جهت توقف ماشین کشتار رژیم استفاده کنیم.
سودا ۳۳سال دارد و ساکن بندرعباس است.
او در تاریخ ۹فروردین بازداشت و اکنون با اتهاماتی چون "عکسبرداری از فاصله دور محل اصابت یک موشک و ارسال این تصویر برای یک رسانه فارسی خارج از کشور" به اعدام محکوم شده است.
او حدود شش سال است که به بیماری ام‌اس مبتلاست و علاوه بر آن از بیماری‌های پسوریازیس، نارکولپسی و کولیک معده نیز رنج می‌برد و نمیتواند در زندان بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71582" target="_blank">📅 18:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71581">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dU2mLsPneF8yPhi8jPzlgVv9pIvvK-r5uLiDjqqvEIfnKRYcULNrI6HzG1IMZTzVenly9LgIp0ukYgkrrVC0DSTDL-sbvMWxEAJABZh_7MRZ291NSECcGrubNA39FyscXaqf-VFCc9Zle9f-MIcD8OvIXd9__JkVTdWbcwqdmtXrGKNQ3x6tCOnaGJHhGmKYhdXX48AKXx10UmZTeM8iTD1MiKikxZJjeThFS0-czSy7EF7is5PkO2wPMnYdI5SM3wVhEdEhozsVWahZCwbXugCAM1mZFxLOhCHsr2Mk2PAODpEGq6IJJJeXScwQRVTqKYI5hxqNU8p-RhFrIDQXcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
نیویورک تایمز:به گفته مقامات ایرانی، تندروهای ایران با صدور دستور حمله به سه کشتی تجاری در تنگه هرمز در تاریخ ۷ ژوئیه، مخفیانه توافق صلح با ایالات متحده را که اوایل همان ماه حاصل شده بود، مختل کردند.
گزارش‌ها حاکی از آن است که مسعود پزشکیان، رئیس‌جمهور، احمد وحیدی و بخش عمده‌ای از رهبری ایران از این عملیات بی‌اطلاع بودند.
بازرسان رد این تصمیم را به جناحی مرتبط با حسین طائب — روحانی بانفوذ و رئیس پیشین اطلاعات سپاه که از همان ابتدا با این توافق مخالف بود — رساندند.
حملات ۷ ژوئیه منجر به حملات متقابل ایالات متحده در روز بعد و همچنین یک کشمکش قدرت بزرگ در داخل ایران شد.
تا ماه سپتامبر، ژنرال‌های تندرو دست بالا را پیدا کردند و به جای بازگشت به میز مذاکره، راهبرد تشدید حملات علیه نیروهای آمریکایی و زیرساخت‌های نفتی منطقه را پیش گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71581" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71580">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71580" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71580" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71579">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp2xdmMaoc3FiSRa6Ft2g8HUMjxemKbD0AHEwAdn8ZAGGuKWgpaNr0pSbd36oOIgzeB8qhejsW6QqKJK2831Pp2c5F6dMXSPVpTGeXApmqWk08jrVT9W4wEdvFpMpVQn19Z-KT7-Ow_EinCS6riwxlPaCt7_-3qqBnMKXOMaQfChfA3wNy1py26M0lONk9e9Uw94J1a629Rz1PmyfgG6nELJYMyDDJ8GzVPvalMEnoc3u5USqzyiQhIGsu53hA2eXuYZhIzHK_kUwU68572nmdsuTXkWxY7Oj39SZ_qVNHdgaTNGVKwiWej8KSiGLv1KR22O2680NWYqaRGq_H7BSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71579" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71578">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=MQlXzM0BWzwFKiWsqrc_7_edK6NLAphAsd_L658NtvTq6ogPZaPyZ5FnrWfJcBaCJNCLWYRmIjr9rjncnaNtMlHvJsGJW3bPJCJdZPBuvL8Liq0ObdHFo4RD51A-b0oehH7-47XALJU7p7YRLf7DsqTLmlQKOi67gvZncCbZQ4p1ngue1X2QuYRXp7Q30FzCJsam8_51z-uIoHcNIHgLHzqvEtT6fqsq5uykDm645jq_PYC-R_7EFba-sMd7rpTu6uhL-VGbcGYK4_LGAbJ1W-4wCDMiwbQ69jYKQgWszr4FQ09LIM-6DfKy7dZMCdhxmzDinfNix50vEY3KXYJAbhjFmCF1IKCdrnz3tdp8StZk70opq69sd8mKOzDeL431chdp-KDgXi31VJiTQQy5_kQj--KGdg5YFlA4ykmnPijvabMln7FbtYLMGkitgCguZNfnLQzHOshlE350GKz4YfPdLP-4LJc-5lVHgnbSIJK7Lf3qJvBTrNeGqcbWR4cQUEJAzHD7J4PDLs3AZeXqBee6T95zSLA5J4pubyc5RiVPuL7dUOZMI4xiNNBAwEo1BJjvt8zlaFHB0JgQZHlWFlzN2fQUjZMbePsoXWfWqunzACol9g_dhh0VOGeGmBP2WeI0sYqD6mFi_N7zCGgpC1XVDqRWdp7wKiEdsdZFbfo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfc5dc935e.mp4?token=MQlXzM0BWzwFKiWsqrc_7_edK6NLAphAsd_L658NtvTq6ogPZaPyZ5FnrWfJcBaCJNCLWYRmIjr9rjncnaNtMlHvJsGJW3bPJCJdZPBuvL8Liq0ObdHFo4RD51A-b0oehH7-47XALJU7p7YRLf7DsqTLmlQKOi67gvZncCbZQ4p1ngue1X2QuYRXp7Q30FzCJsam8_51z-uIoHcNIHgLHzqvEtT6fqsq5uykDm645jq_PYC-R_7EFba-sMd7rpTu6uhL-VGbcGYK4_LGAbJ1W-4wCDMiwbQ69jYKQgWszr4FQ09LIM-6DfKy7dZMCdhxmzDinfNix50vEY3KXYJAbhjFmCF1IKCdrnz3tdp8StZk70opq69sd8mKOzDeL431chdp-KDgXi31VJiTQQy5_kQj--KGdg5YFlA4ykmnPijvabMln7FbtYLMGkitgCguZNfnLQzHOshlE350GKz4YfPdLP-4LJc-5lVHgnbSIJK7Lf3qJvBTrNeGqcbWR4cQUEJAzHD7J4PDLs3AZeXqBee6T95zSLA5J4pubyc5RiVPuL7dUOZMI4xiNNBAwEo1BJjvt8zlaFHB0JgQZHlWFlzN2fQUjZMbePsoXWfWqunzACol9g_dhh0VOGeGmBP2WeI0sYqD6mFi_N7zCGgpC1XVDqRWdp7wKiEdsdZFbfo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ایران به‌شدت خواهان توافق است.
آن‌ها مدام تماس می‌گیرند. می‌خواهند توافق کنند. اما باید توافق درستی باشد؛
من تن به توافقی که خوب نباشد، نخواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71578" target="_blank">📅 17:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71577">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=CYwMjsk4iIqfmzFN6pzbuF-vcZrXxvcqviYqALRwpi9MyUSyMXlYP5qN-oDfFgOMeMWAf3vabkcbpGyukzW5p1v4GR6IO-T83SaVfb3zUSmKGTu6kER9UILmm2eM2nfWGu9W3d97PMqOcjwSN95q4iqcGL3GaVI-lMcFTJ6bEoBXvDBEuXHRzUvpN8J5oOsWUnUNuGWTpwlY8UFiVmGadb2qAoSjXJtDrLEx5Gu65Du1VZ-eSenzRvBKtJGSsxqtBzfPYSXDPdqf4zB4bzFZsW3DyrW4oAxSGQmocKPY6PyQhAnBJC5npafDqqq_uwhExEBdtiptRFrMtEzy82THeZ1peRHjl6ZEVRHnBqMh2kZhfU03vYSOhxAB8Dz2bFJug-kJPldydfe3AwmAfEiFxrWjS9T_cw19qXJrjmVskSC80SH4DjhOWljb0hGjDXMEqtym_Zasi2KJiY8HPlodW7IcNbciTFEb-hXbOkk7uFK1ysIRF_Q13BCy7d-Zx968d6pD_0-WL6ydrUJN9fRGIlNOrRlsdZvVOIc6NwkyQwPEpRxqiMn9CQTBX35AWlRldnJ83uglSFSbl6CDCXISl8XTEUpTYcUz_GG-TdU_nzK0TyNZwv_GROOGa_dE_XuyZzAnv8FLR5IrPvfr89KHi-tukbejT0IYtRBf-jZP9RI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b70464e.mp4?token=CYwMjsk4iIqfmzFN6pzbuF-vcZrXxvcqviYqALRwpi9MyUSyMXlYP5qN-oDfFgOMeMWAf3vabkcbpGyukzW5p1v4GR6IO-T83SaVfb3zUSmKGTu6kER9UILmm2eM2nfWGu9W3d97PMqOcjwSN95q4iqcGL3GaVI-lMcFTJ6bEoBXvDBEuXHRzUvpN8J5oOsWUnUNuGWTpwlY8UFiVmGadb2qAoSjXJtDrLEx5Gu65Du1VZ-eSenzRvBKtJGSsxqtBzfPYSXDPdqf4zB4bzFZsW3DyrW4oAxSGQmocKPY6PyQhAnBJC5npafDqqq_uwhExEBdtiptRFrMtEzy82THeZ1peRHjl6ZEVRHnBqMh2kZhfU03vYSOhxAB8Dz2bFJug-kJPldydfe3AwmAfEiFxrWjS9T_cw19qXJrjmVskSC80SH4DjhOWljb0hGjDXMEqtym_Zasi2KJiY8HPlodW7IcNbciTFEb-hXbOkk7uFK1ysIRF_Q13BCy7d-Zx968d6pD_0-WL6ydrUJN9fRGIlNOrRlsdZvVOIc6NwkyQwPEpRxqiMn9CQTBX35AWlRldnJ83uglSFSbl6CDCXISl8XTEUpTYcUz_GG-TdU_nzK0TyNZwv_GROOGa_dE_XuyZzAnv8FLR5IrPvfr89KHi-tukbejT0IYtRBf-jZP9RI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ماجرای ایران درست بعد از انتخابات میان‌دوره‌ای تمام می‌شود؛ شاید هم قبل از آن، اما قطعاً بلافاصله پس از انتخابات میان‌دوره‌ای پایان می‌یابد.
قیمت بنزین به‌شدت سقوط خواهد کرد،خب، من می‌دانستم چه کار می‌کنم و باید آن کار را انجام می‌دادم.
ایران نباید به سلاح هسته‌ای دست پیدا کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71577" target="_blank">📅 17:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71576">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=shbBRENTTJnifuDiul-SfQ4Hk1HusPzjGOOStHBWaw3bt_4sIzuccNLRcWHmGFAkjGShVYk2ggxpDA6_c07PqwaLfjN3S4OYXHiVIkjMQDBpcFnMqPnWX6dT-xvabS1wEhaw0CF5YHa36K7pl5ZmMGd4rFCj4wK-2lBPEfZHWDD5awNrhHngQCVlXgxwq65R1PICvL-729LP1hKA-58YufBHW_kFy1en1MhpVSIxoE8aERg3zJhpUJaCy_ciQX_VwX08G6--RLVhn29C3ge3G5UFNZw6Gr4weOOd37CvO-EzOJGCVOUngmBhXLK5jcXRqEZXx0YgjwmM1VCxtXJgj2M253GxD95R5N2StrH_Kep0P9zM6tPKppWh3lTs3thfLdoqTb8FnYl-Lkyi8qh58tsj1Ct5JaeID_V1-9lvX0z1IG83DPIoLhg8IP-FaKlNchaIe3bYilpkBuOSjX0jSwEAEL8b4EY93wAtg0cMmjZbJ13IzEYmaZoAy9arsrX3QL_GkkjzT1uzZk8nMp_aBlHMNqnxW3MWAasgBRjbFyYbHThk_hamr80tULlApGpbsYOPQaJQaKEBVu8mKA0QzrWisTRER4kPVQJKFkZ56D4fP7WoADMrg9cOKiMzIppSFjvZOH8RXf5hB_aqhNxFOf-c8OBJL-PLCD8JiCTQOWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a78bb4d113.mp4?token=shbBRENTTJnifuDiul-SfQ4Hk1HusPzjGOOStHBWaw3bt_4sIzuccNLRcWHmGFAkjGShVYk2ggxpDA6_c07PqwaLfjN3S4OYXHiVIkjMQDBpcFnMqPnWX6dT-xvabS1wEhaw0CF5YHa36K7pl5ZmMGd4rFCj4wK-2lBPEfZHWDD5awNrhHngQCVlXgxwq65R1PICvL-729LP1hKA-58YufBHW_kFy1en1MhpVSIxoE8aERg3zJhpUJaCy_ciQX_VwX08G6--RLVhn29C3ge3G5UFNZw6Gr4weOOd37CvO-EzOJGCVOUngmBhXLK5jcXRqEZXx0YgjwmM1VCxtXJgj2M253GxD95R5N2StrH_Kep0P9zM6tPKppWh3lTs3thfLdoqTb8FnYl-Lkyi8qh58tsj1Ct5JaeID_V1-9lvX0z1IG83DPIoLhg8IP-FaKlNchaIe3bYilpkBuOSjX0jSwEAEL8b4EY93wAtg0cMmjZbJ13IzEYmaZoAy9arsrX3QL_GkkjzT1uzZk8nMp_aBlHMNqnxW3MWAasgBRjbFyYbHThk_hamr80tULlApGpbsYOPQaJQaKEBVu8mKA0QzrWisTRER4kPVQJKFkZ56D4fP7WoADMrg9cOKiMzIppSFjvZOH8RXf5hB_aqhNxFOf-c8OBJL-PLCD8JiCTQOWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آقای رئیس‌جمهور، آیا فکر می‌کنید کنگره باید آن ۵۰۰۰ دلار را تصویب کند؟
🇺🇸
ترامپ:
همان‌طور که گفتم، نمی‌دانم اگر جمهوری‌خواهان پیروز شوند، انجام این کار چقدر آسان خواهد بود.
صحبت از ۵۰۰۰ دلار برای تمام بزرگسالان کشور است و ما به‌راحتی از پسِ آن برمی‌آییم، چون درآمدهای کلانی داریم؛
وضعیت ما هرگز تا این حد عالی نبوده است. دموکرات‌ها نمی‌توانند چنین وعده‌ای بدهند، چون در آن صورت اوضاع بلافاصله به هم می‌ریزد و نابود می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71576" target="_blank">📅 17:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71575">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=VdXPuNdHUl6VJn7q7AbmIfAQ3lHx5JvKQQGMwXWDRhRWNxHEFZkkIItOvKALWVI8u1KCMu1oZUqDglY8V_Lv67g1Pdz7xD1IGRi79jedz9yMXCwWBK7YCz5mQy22utFVxMcdZPeDDzt8Zf2CtPi9jL-pxvO7dTe4HVNrqmNfrcflze3OgEK9rpXMYMwhCyzAjNW-L-F6ppcNgX4RcNjASCIg-uITPc-KJKYVOU_cQn2ySBx3suuVZ_qO_v0tnj7c1P1pI9li4m5EZyQuqN4qTBtXEZHAWpEkrC7MTDjUtYvWMwNbSKe76EG3958E1K7XnA-tuApz0p4ZtoXEO1ScqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f2319501.mp4?token=VdXPuNdHUl6VJn7q7AbmIfAQ3lHx5JvKQQGMwXWDRhRWNxHEFZkkIItOvKALWVI8u1KCMu1oZUqDglY8V_Lv67g1Pdz7xD1IGRi79jedz9yMXCwWBK7YCz5mQy22utFVxMcdZPeDDzt8Zf2CtPi9jL-pxvO7dTe4HVNrqmNfrcflze3OgEK9rpXMYMwhCyzAjNW-L-F6ppcNgX4RcNjASCIg-uITPc-KJKYVOU_cQn2ySBx3suuVZ_qO_v0tnj7c1P1pI9li4m5EZyQuqN4qTBtXEZHAWpEkrC7MTDjUtYvWMwNbSKe76EG3958E1K7XnA-tuApz0p4ZtoXEO1ScqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
نظر شما درباره دیدار کشورهای حوزه خلیج فارس با ایران چیست؟
🇺🇸
ترامپ:
برایم اهمیتی ندارد. این به خودشان مربوط است. اشکالی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71575" target="_blank">📅 17:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71574">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=SOqb7D8gPWcKn0ESAvcXg38hUSotIBXQFEaY-e2m6rAdRrgIRznOTADGrz4WNpNlX7Gvr04nVf9SCcvAFe_Lx2cn5euSw5tFeSjsSWRlRlJnCWqB2uGWiQO8-udgFP3r9jTjloo4EDA5OMF2uho76QIbWwfH0T0DBi3zfMJLa_F7gvw2nD3pftR9LeDER6JX_ci0jsl3h3gKw761ng7l2Ql1qwiDyv3x_6xDR1KTZOnlpgpab7OjNt4upZeYOxKIZYEGbtIW75PIAq6RcVpMA8r_Oyk4RK7MCmomKgNDXJPJpolz8OrHIo31K_CfB58t-vXe5-UPkW9OcUQibev6sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e5ba3545.mp4?token=SOqb7D8gPWcKn0ESAvcXg38hUSotIBXQFEaY-e2m6rAdRrgIRznOTADGrz4WNpNlX7Gvr04nVf9SCcvAFe_Lx2cn5euSw5tFeSjsSWRlRlJnCWqB2uGWiQO8-udgFP3r9jTjloo4EDA5OMF2uho76QIbWwfH0T0DBi3zfMJLa_F7gvw2nD3pftR9LeDER6JX_ci0jsl3h3gKw761ng7l2Ql1qwiDyv3x_6xDR1KTZOnlpgpab7OjNt4upZeYOxKIZYEGbtIW75PIAq6RcVpMA8r_Oyk4RK7MCmomKgNDXJPJpolz8OrHIo31K_CfB58t-vXe5-UPkW9OcUQibev6sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
در نهایت ما آنجا را ترک خواهیم کرد، مگر اینکه تصمیم بگیریم بمانیم و نفت را برای خود نگه داریم؛ درست مثل ونزوئلا.
دیگر درباره ونزوئلا حرفی نمی‌زنید، مگر نه؟ خوب به این موضوع فکر کنید: میلیاردها و میلیاردها و میلیاردها دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71574" target="_blank">📅 17:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71573">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇾🇪
حوثی‌های یمن تصاویر مفصلی از عملیات نظامی جدید خود با عنوان «و خداوند از نظر قدرت و کیفر، سخت‌گیرتر است» منتشر کردند؛ ویدئویی که صحنه‌های نبرد در جریان تهاجم اخیر آن‌ها در ساحل غربی را به تصویر می‌کشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71573" target="_blank">📅 17:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71572">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=B96girSxBCcaCu9pctxMbpgkt-iGbKZcTcXFBs7ocyDN8e6ohrAGHDnLHaf0RrkoZNm38K84Ix7iWn88Yo_N80QHnOCYpRUI2gHLO2W5RJ7wEPTRVHwerhXRqWqhllzHGRTIEVdT3xPf4XByTZyYE4tW7A20lrtmpU3VY3JQM-m7LaLd-XOZ_htYG69FGUxK1oJG0zLBiNM5KyO0HEckplkchIk8pKUCEXJji0Igg2AfQq2s_jnTlsJgopgx0wr4GIIaL1wv5ZElsxnOkNpcngS6gYXiatL3Koiw7bgXriC4aUBxDy6yVx-EJOUexn3i5o65u2b2IWFy-KXuFZz9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fa2fdcc9.mp4?token=B96girSxBCcaCu9pctxMbpgkt-iGbKZcTcXFBs7ocyDN8e6ohrAGHDnLHaf0RrkoZNm38K84Ix7iWn88Yo_N80QHnOCYpRUI2gHLO2W5RJ7wEPTRVHwerhXRqWqhllzHGRTIEVdT3xPf4XByTZyYE4tW7A20lrtmpU3VY3JQM-m7LaLd-XOZ_htYG69FGUxK1oJG0zLBiNM5KyO0HEckplkchIk8pKUCEXJji0Igg2AfQq2s_jnTlsJgopgx0wr4GIIaL1wv5ZElsxnOkNpcngS6gYXiatL3Koiw7bgXriC4aUBxDy6yVx-EJOUexn3i5o65u2b2IWFy-KXuFZz9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی مملکت یه سری کارگاه آموزشی گذاشتن و به افراد بالای 60 سال آموزش میدن که چطوری اسنپ بگیرن.
هزینه شرکت تو این کارگاه بین ۱ـ۲ میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71572" target="_blank">📅 16:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71571">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=HMq_zF86zAkY3oSOoGcW0uTHjM0PhPe1GkQBnh9XwhwNVELTFNQjZXpfguTLX3mJ0B3T9q5HMQ1Kd5b314wUWRlyyWLUQSvDzUKE_wwuIrYKQwEtdNF4YiXEf4nsOzSYaANBA9wXY_pqoy5t1dwI6O-iSNaNRDkidbqi78nYMmjJL048t3FOIwRGyZY49JUF8iL22vGg5t_VXx045_RgDhNgkD0ac-2SU8FrZrzC5bPHw0NulHzWtvJDYXxBrlMLJyNuI_jxJGaD0Rjhod4ljkplSTKZ9kWe_iMN3AmN2LgSlFmFDcyCXdQwB8PEu7X9ooUgq31IQ4AN6vpGPtlnWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc03db8a0.mp4?token=HMq_zF86zAkY3oSOoGcW0uTHjM0PhPe1GkQBnh9XwhwNVELTFNQjZXpfguTLX3mJ0B3T9q5HMQ1Kd5b314wUWRlyyWLUQSvDzUKE_wwuIrYKQwEtdNF4YiXEf4nsOzSYaANBA9wXY_pqoy5t1dwI6O-iSNaNRDkidbqi78nYMmjJL048t3FOIwRGyZY49JUF8iL22vGg5t_VXx045_RgDhNgkD0ac-2SU8FrZrzC5bPHw0NulHzWtvJDYXxBrlMLJyNuI_jxJGaD0Rjhod4ljkplSTKZ9kWe_iMN3AmN2LgSlFmFDcyCXdQwB8PEu7X9ooUgq31IQ4AN6vpGPtlnWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیویی جالب از یک پهپاد اوکراینی که به سمت یک کشتی روسی در حال حرکته و یه بالگرد روسی تلاش می‌کنه اونو بزنه ولی، این پهباد در نهایت خودشو به کشتی میرسونه و منفجرش میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71571" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71570">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=QyhXTgdr6_Nhqdxt5YSmORXYxoUYWp0mSMfiqz_uDbFUqoGHQtrnphet3hSmwpDPX9LOcTgi_OT26KzW4edlHlMLI8Ulm4ezcgrPb1azUhbZyfTsZraljxtnmwccy0XcjxztO3x9zyiZsnamlghQEAypIyK-pQsYLkylQnz-ie8jzC9b_Omc1UCEEfUQRIbYJF0g-puXzk0ej3GXnAo4OF-UbK-SdR_dNAdtDTY0iW9tHtt9_u2hedPJrMb-eAlYM6GtplTsMpGUFPtXnQQ5HQOW0URxrWd6ei0hFXqf4DRIR2HFfDhsE87RVObJDzNcDeLjQm2j5IkXbeU0hnI4HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fa8bd2c9.mp4?token=QyhXTgdr6_Nhqdxt5YSmORXYxoUYWp0mSMfiqz_uDbFUqoGHQtrnphet3hSmwpDPX9LOcTgi_OT26KzW4edlHlMLI8Ulm4ezcgrPb1azUhbZyfTsZraljxtnmwccy0XcjxztO3x9zyiZsnamlghQEAypIyK-pQsYLkylQnz-ie8jzC9b_Omc1UCEEfUQRIbYJF0g-puXzk0ej3GXnAo4OF-UbK-SdR_dNAdtDTY0iW9tHtt9_u2hedPJrMb-eAlYM6GtplTsMpGUFPtXnQQ5HQOW0URxrWd6ei0hFXqf4DRIR2HFfDhsE87RVObJDzNcDeLjQm2j5IkXbeU0hnI4HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری صداوسیما:
از جنگ تحمیلی دوم حدود ۱۵ ماه اینا هست میگذره دیگه
مقامات صهیونیستی و امریکایی پر تکرار گفته ان که با حمله به ایران ظهور مهدی موعود رو به عقب انداختیم
دلیل اصلی بمباران تاسیسات هسته‌ای ایران به عقب انداختن ظهور بود
اونا نگاهشون آخرالزمانی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71570" target="_blank">📅 15:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71569">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4R3JinRh3Fkl4vtS5WC1lqwmArASrgBO1bJv6ETvkkY4SbjnbiNjco1jRLuEw4uurxzC3Kg6goatnNZ-6w84CVl7eXLY6NWJE-lb4ZvfXqsuZdn92dN0tMx6ht-ZneukmRZwU9pG_7ny4w1eblHX6br185AFakRAWEAoPZ7mKvveJGufftp26syv4lv8YgZEtMkpNWc8OG51MfWTRgOPjqykAJRPOkf4AGuOXV5w8S3m1XUAn5dYe5fkrvjkU23W53-SkJOxl0o-02PadOu7dIwNJGFloWki2ZqvxAUaw497PTjDsi1q_9Xwp0Uz9hJ90a9B19CZY_DDdctOrq96qOkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d522fc2430.mp4?token=cAAEdZTFPJ4vICtfg278BLKLUEiA2UKp8i6XH491KBwFqdz4ZYiTge7qcqHxqFKDMnDi3w96Mw_w1GN7n-I2FjDvzaQpZsz3Ur9gpM336yd-cNU8uwl1gLBWjqZBeBkaYCLtDZ7v7kv7Hj98bmMHznvyt4G6w20WjhDRmFzuSJe6dpjXicMq_0OA56-EgpSuEjAXvx0D2pHvHLn9hWoWnKeyFVFRs-DG7Slv0lsA08LnrrxiDAKgdhrj0qGXPVgHkAJQG-t2VLccUuD6HnNfQDMLnb33yYCXoszAnjeO0bZT8lrSS0fg4oX0vYLcDaXBscDls0oQeRHtK0Bmm0D4R3JinRh3Fkl4vtS5WC1lqwmArASrgBO1bJv6ETvkkY4SbjnbiNjco1jRLuEw4uurxzC3Kg6goatnNZ-6w84CVl7eXLY6NWJE-lb4ZvfXqsuZdn92dN0tMx6ht-ZneukmRZwU9pG_7ny4w1eblHX6br185AFakRAWEAoPZ7mKvveJGufftp26syv4lv8YgZEtMkpNWc8OG51MfWTRgOPjqykAJRPOkf4AGuOXV5w8S3m1XUAn5dYe5fkrvjkU23W53-SkJOxl0o-02PadOu7dIwNJGFloWki2ZqvxAUaw497PTjDsi1q_9Xwp0Uz9hJ90a9B19CZY_DDdctOrq96qOkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇾🇪
تصاویر بسیج قبایل حوثی، ستون‌های طویلی از خودروهای تویوتا (تکنیکال) مجهز به سلاح را در بیابان به نمایش می‌گذارد؛ تصویری که نماد کلاسیک جنگ یمن است.
قبایل «بنی‌حشیش» برای پیشروی به سوی «مأرب» — آخرین پایگاه عمده دولت در شمال — اعلام آمادگی کرده‌اند.
وانت‌های تویوتا مجهز به سلاح، همچنان ستون فقرات نیروی زمینی حوثی‌ها را تشکیل می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71569" target="_blank">📅 14:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71568">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4HG_CYsh_wt0NgPzACiTDki786qjUhYulsa5mm_cJnZYUksLP5GcpR0tIloTIsBpEE5b8cwDOjm-h9v6bhC7GLKhxLXE_4T61vHRVgrFi5d5XhX0qtURw0zz9DWmWdC0tsIRVoFPaTsflcGxUegg_-c9z7fIbj3mIjQmZr3mM_O5nRP4VNlLHIz6zfACwH6-_jSQRo2XW0req-ATUbpHGPf6AhwldI7YX_nzzOBSk5h6h5I7hc68Jsn8ryhoc8TekwtAHwuXdLLE3L6RBIywWgcimSyVhvqe_yxs4u18qLS4DuO7kAfxYV7La-SZAyA5Cj5BxaI79_eNq6uX5TkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
📰
اکسیوس: محمد بن سلمان، ولیعهد عربستان سعودی، روز پنج‌شنبه دو بار با دونالد ترامپ، رئیس‌جمهور آمریکا، تماس گرفت و از ایالات متحده خواست تا هم‌زمان با پیشروی حوثی‌ها به سوی یک نقطه راهبردی و حیاتی در دریای سرخ، به آن‌ها حمله کند.
ترامپ این درخواست را نپذیرفت و مقامات آمریکایی اعلام کردند که در حال حاضر هیچ برنامه‌ای برای مداخله مستقیم علیه حوثی‌ها وجود ندارد.
دریاسالار کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، نیز روز پنج‌شنبه برای هماهنگی‌های اضطراری به ریاض سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71568" target="_blank">📅 14:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71567">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=dC-uf5NQDszNyLqZT8HyeqGF4y0Ex5Q1oB7onzpJlCM-YAQSYKsWuq67Tg7x1y7GVSjQx3PAAm_0P5eZh6dukQGp9z-GZdLk3k7UcLeoQ0Xy1dPOko1UV6sukQTZgfHLXJTPEZjj1iaoTM4nWTelEJzq_E6M0rFi1ilBs-JrappowHDliiY7g6_zRawHiQH87CohvrzK779Dx75G59W4EjD2ofXDyZVFsjg6evY0jhcsX-FynoALFNCQSoRq5Vx8JYXvwOy7edg1vpb0oPGyzpouvnYWi3ODcrTSzw4w4sbDAFu0KRH2NHf2mi9fCC4sPWWl4CKrnS5bs-4pYMvllw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363bcb9915.mp4?token=dC-uf5NQDszNyLqZT8HyeqGF4y0Ex5Q1oB7onzpJlCM-YAQSYKsWuq67Tg7x1y7GVSjQx3PAAm_0P5eZh6dukQGp9z-GZdLk3k7UcLeoQ0Xy1dPOko1UV6sukQTZgfHLXJTPEZjj1iaoTM4nWTelEJzq_E6M0rFi1ilBs-JrappowHDliiY7g6_zRawHiQH87CohvrzK779Dx75G59W4EjD2ofXDyZVFsjg6evY0jhcsX-FynoALFNCQSoRq5Vx8JYXvwOy7edg1vpb0oPGyzpouvnYWi3ODcrTSzw4w4sbDAFu0KRH2NHf2mi9fCC4sPWWl4CKrnS5bs-4pYMvllw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کنعانی مقدم:
اگر رهبری اجازه دهند، ظرف ۲۴ ساعت از سلاح هسته‌ای استفاده خواهیم کرد
خرید فیوز هسته‌ای از کره شمالی، کار خیلی ساده‌ای است و ۵۰ تا فیوز می‌توانیم بخریم
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71567" target="_blank">📅 13:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71566">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=lJ40MiiYg7OhJ6pG-NR6-tBltVtWOxzeOhEvlMUlM9K1oPB6b5WlDazZHnbOUD9JnLtn-YKvv118UP-D9YGug2Co_yNuPl0onLf8A-PhJFtgD6033ImePRaGNrE9xYCS4_I9LWcvlMSX9cKmLTS05gMDentmvUBeZPnWgOZpadgMwkANIuQeb_W6JLi5CVVM1RzLeUEczamAKgEvirH4JYVXdGG-Bw38c5quqty9gRv1yL3driV2bd07Ub6ux_tDlBfSyp7FJHl3XmHc_U6W31NJLAsiAD4482cq0krGBy16RXRTy2T0_ogfLtqPCeFkPGzrPnbj1lh85X0dBneiqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67e4c7321.mp4?token=lJ40MiiYg7OhJ6pG-NR6-tBltVtWOxzeOhEvlMUlM9K1oPB6b5WlDazZHnbOUD9JnLtn-YKvv118UP-D9YGug2Co_yNuPl0onLf8A-PhJFtgD6033ImePRaGNrE9xYCS4_I9LWcvlMSX9cKmLTS05gMDentmvUBeZPnWgOZpadgMwkANIuQeb_W6JLi5CVVM1RzLeUEczamAKgEvirH4JYVXdGG-Bw38c5quqty9gRv1yL3driV2bd07Ub6ux_tDlBfSyp7FJHl3XmHc_U6W31NJLAsiAD4482cq0krGBy16RXRTy2T0_ogfLtqPCeFkPGzrPnbj1lh85X0dBneiqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎯
ویدیویی از هدف قرار گرفتن نیروهای انصارالله توسط نیروی اسنایپر مورد حمایت عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71566" target="_blank">📅 13:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71565">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=O_HzewizNPOU1Nu9w9sefJ9GrBqNp-1J6BDVygMUIvNxeKfg6ZIIs9CUrI0NUIGuLxJoYyN9Syd550GIFBsKgooFe4RMulg8u9tB2BzUMkzKbmvyPSmb_d4F4Gt-PTwlnvTLNlWZ2X9dO23oMhxZ75CUmts7mqoQd6Rac_U5FTcQxJGd009v_jopbsKk_DOBmMbDdpHu3zZv23FnrOJa6VBPe52jFEIPatrK2Omg8iU2y4gN3EY2zKL5HBFKLYBVf-4ZTRVcZXrxMAluxcpnP8EefKao5BR2DtWtVw7xX5gDOM-4hOJeY85n7zLkcVDeriLblQKvXJnQ7_bu5j8Mzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0000373bd7.mp4?token=O_HzewizNPOU1Nu9w9sefJ9GrBqNp-1J6BDVygMUIvNxeKfg6ZIIs9CUrI0NUIGuLxJoYyN9Syd550GIFBsKgooFe4RMulg8u9tB2BzUMkzKbmvyPSmb_d4F4Gt-PTwlnvTLNlWZ2X9dO23oMhxZ75CUmts7mqoQd6Rac_U5FTcQxJGd009v_jopbsKk_DOBmMbDdpHu3zZv23FnrOJa6VBPe52jFEIPatrK2Omg8iU2y4gN3EY2zKL5HBFKLYBVf-4ZTRVcZXrxMAluxcpnP8EefKao5BR2DtWtVw7xX5gDOM-4hOJeY85n7zLkcVDeriLblQKvXJnQ7_bu5j8Mzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
این رهبران جدید و رهبران واقعی که رئیس‌جمهور ترامپ از آن‌ها صحبت می‌کند، چه کسانی هستند؟
🇮🇷
پزشکیان:
به گمانم باید این را از خود او پرسید، چرا که هر روز حرف متفاوتی می‌زند.
یک روز می‌خواهد ایران را نابود کند و روز دیگر می‌گوید ما دوست ایران هستیم؛ یک روز می‌گوید ما را به رسمیت می‌شناسد و روز دیگر می‌گوید ما را قبول ندارد.
بنابراین، ما مطمئن نیستیم که باید کدام اظهارنظر را بپذیریم و بر اساس کدام‌یک عمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71565" target="_blank">📅 12:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71564">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71564" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71563">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm5U3b2lIlnQ1iMhAamgrok_aJBLgM9XBdPcPgwX-xhLXjUB0z2ULSHRL9OmZbuHa3YUTJobT81AsiOqh5iEnOKpuqLdHxdh4x0plx4gNZqnI1fDH3GWcnGzRPVUbMIFpFpw7MwA1LUtIdVHnddzCmMBM81YieMMLdrqyygc1vEN2GT_VCgj5bwwbhTHSZzApcIPRcNrOs19Dr1DQyI-E0Z-OPbL_PudxPqahSY0oR1HPZRUQw-1VP6NNcVRV-3lZwhXCit7-PBFlQGDmzGotOo3hzWu0tgoH5sm4V6Syf26zc0yHRZc6cdalXBNDf3WdrIe-fIygJbhR3VQyKV6ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71563" target="_blank">📅 12:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71562">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npmlvtMOo_S1lMuGoBk89SjOj2x2a-i27urjEH6_Hb0VIcfdlHmUdaaDnzzBr-jCMLMQl-3pSI-nZY9h3yyYUlAH4jQBd1xXxDIFxOpfaLre9R0tlQTcm2271a-Z-Q0iRtmfzu-xJQhLp_5zIdwAJK7jwdh0FYNHDLG1vEQ4_s8tQb942LmM7GBHi2R2_ynL8c46B3YYrxJRAY8tJ2o9gmZzYh1Oj6j1MS1mrklBLqSFkr3cRjVAhBLOVYbcwNkFKdJWdF8L637x6GmyOz3kuDhnnp3FJx-6iV4NF_-cDUQ6FKzTcRcJrQ38eTDUZh8Q_Ew_VIG64ascJY_NcNYqag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
روز یکشنبه در گزارشی اعلام کرد که بر اثر اصابت یک پرتابه ناشناس به شناوری در حال عبور از تنگه هرمز، در آن کشتی آتش‌سوزی رخ داده است.
این سازمان اعلام کرد که مقامات محلی در حال کمک به تخلیه خدمه کشتی هستند. در این گزارش، نام شناور یا اطلاعاتی درباره تلفات، خسارات و یا پیامدهای احتمالی زیست‌محیطی آن ذکر نشده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71562" target="_blank">📅 11:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
🇯🇴
ویدئویی از پرتاب انبوه موشک‌های رهگیر «پاتریوت PAC-3» از پایگاه هوایی «موفق سلطی» در اردن در سه روز گذشته، برای مقابله با موشک‌های بالستیک ورودی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71561" target="_blank">📅 11:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=rYaXrPBFtfUPglTaVpOxyi1ctWSgCVJ2eYq97tXg0pdD_R2Xa6SvTL31rDiizRoZvYl50bgxfWDGb_DZz6_IEaYlaBi205NCElAn-J2ThJ5LfKNZAKaQM1RU7fmG_OUt9PTyiiRON9rCBpzGChQcY-F31WE63443b5teRQsAWzcstJRaNob5OcDjuW1DyYIeiKkkN2zwxPB1yD4U2He2VqGEQmXuJjPte1LCtpbSqV5T0HpSKyvw1Avp0SwoADdrvhHdfR5y8M5iDHPASWwP_4OGpU4z4Q9GAK8SYetP4sHdDyMWrfVp61SR5L7SgUpcV_mWUFl8lV0wgLz38eu_JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c7237eb3.mp4?token=rYaXrPBFtfUPglTaVpOxyi1ctWSgCVJ2eYq97tXg0pdD_R2Xa6SvTL31rDiizRoZvYl50bgxfWDGb_DZz6_IEaYlaBi205NCElAn-J2ThJ5LfKNZAKaQM1RU7fmG_OUt9PTyiiRON9rCBpzGChQcY-F31WE63443b5teRQsAWzcstJRaNob5OcDjuW1DyYIeiKkkN2zwxPB1yD4U2He2VqGEQmXuJjPte1LCtpbSqV5T0HpSKyvw1Avp0SwoADdrvhHdfR5y8M5iDHPASWwP_4OGpU4z4Q9GAK8SYetP4sHdDyMWrfVp61SR5L7SgUpcV_mWUFl8lV0wgLz38eu_JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نظرات متناقض هادی چوپان درباره هانی رامبد:
بعد از قهرمانی
بعد از جدایی
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71560" target="_blank">📅 11:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097559287c.mp4?token=lBGqms85x9ifOP-gP1Te_puKgrecHGK7iOU0YoRsQ1AVaZsdkP54Xg5d4Fi3Q_MXjv6eR6PDAEtLd7nfsPe0Lqn8z81YPZ6XmW69ZsWTepClM4kE7FpDn23xl1S-hVPjprKENXBgEFl_a0QNaIg_El3mwV47KSOH1CP4yB4dkO8kiRlUqfosqEeyeWSVM06vBUcM6GqQXs7SVx3I7KMLh3moDXMi-x8gaY1hFCLnCOCAfK2mOVRr5jhYjhPcu_zj2TipRQTJvp0cHiqRNX4UELFx03AHmdlaRfJFoR6i30cSqf79q9yGd9VC3zm9Jij-ELuTpD3FAWXICdAVosVG5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097559287c.mp4?token=lBGqms85x9ifOP-gP1Te_puKgrecHGK7iOU0YoRsQ1AVaZsdkP54Xg5d4Fi3Q_MXjv6eR6PDAEtLd7nfsPe0Lqn8z81YPZ6XmW69ZsWTepClM4kE7FpDn23xl1S-hVPjprKENXBgEFl_a0QNaIg_El3mwV47KSOH1CP4yB4dkO8kiRlUqfosqEeyeWSVM06vBUcM6GqQXs7SVx3I7KMLh3moDXMi-x8gaY1hFCLnCOCAfK2mOVRr5jhYjhPcu_zj2TipRQTJvp0cHiqRNX4UELFx03AHmdlaRfJFoR6i30cSqf79q9yGd9VC3zm9Jij-ELuTpD3FAWXICdAVosVG5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
تلاش ابی برای بوسیدن دست یکی از بازیگران برنامه عشق ابدی که ویدئوش به شدت در حال وایرال شدنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71559" target="_blank">📅 10:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71558">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=aC6hcoLPrHIfn7whmeAIhOPhr0S962_H5VxGHr7Lh4P6Z4yKyotpA8GmrQ5kFgzL9RsJo1qRLy-D0oky_8dGEMgTz_zR26zy-jIg8aG9SuCnL87_X5X49GHH7vdngAIcFtZY3UvdkXyihfrBWQvYvIuYkfOsEPESOLIMHNgl6ciemU0O5VoZhJt0-2W-OQq4Ba1wL_PD81Mcu6JLKsYwqNAyOHFbRXEXWhJJrViE71aKJKo-GE1j7b9aBzuL0CjYXnBhdRi-g0C8p-7361o3iESx3aAFOCcMPRlqsIugxLSFJn84tlUYIL_iJLOvh47TOdCYkP0pcF2gIkoMkfPgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427cd49fec.mp4?token=aC6hcoLPrHIfn7whmeAIhOPhr0S962_H5VxGHr7Lh4P6Z4yKyotpA8GmrQ5kFgzL9RsJo1qRLy-D0oky_8dGEMgTz_zR26zy-jIg8aG9SuCnL87_X5X49GHH7vdngAIcFtZY3UvdkXyihfrBWQvYvIuYkfOsEPESOLIMHNgl6ciemU0O5VoZhJt0-2W-OQq4Ba1wL_PD81Mcu6JLKsYwqNAyOHFbRXEXWhJJrViE71aKJKo-GE1j7b9aBzuL0CjYXnBhdRi-g0C8p-7361o3iESx3aAFOCcMPRlqsIugxLSFJn84tlUYIL_iJLOvh47TOdCYkP0pcF2gIkoMkfPgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئو وایرال شده از 9 اسفند - روز شروع جنگ و بمباران تهران و واکنش  دانش‌آموزانی که خرکیف شدن
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71558" target="_blank">📅 09:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71557">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇮🇷
امیر تیموری فرماندار شهرستان قشم:
یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
در این حادثه  یک نفر شهید  و سه نفر مجروح شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71557" target="_blank">📅 09:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71556">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCx5NPxOXN9NTbmgBPQlx_d0yr20lJFVKj5mN-X0sC5Bl6W_GNxbtDnMBLQ6TJ1q5olliSg4yW2tNHjR_sWJUPmGBwTm3qMn809jSTltXXI3DdOXkNcJ7-dbKjVc--c5Ix6wai3RNhCnv5jO19razScLC73dyB1xmW-EPsrJxMxn-aJ9U-e59JCeo4RCfYLH3V-CFS7Dl9-1qE_JMmRov45O5MbgzSxsqOQKrazVKOMCvinK-zEq42xrjqxhOmVsIOleY9SDt5ocX6JXbAhLKxVVN7hAceVNAjECZbanl1pGDs0y5juIKT4oerXY77Wly2wuzo1UgIAezXqlBP5hEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇮🇷
📰
وال استریت ژورنال:
مقامات آمریکایی می‌گویند ایران پیش از حمله موشکی بالستیک ۱۷ ژوئیه به پایگاه هوایی «موفق سلطی» در اردن — که منجر به کشته شدن سه سرباز آمریکایی و زخمی شدن چهار تن دیگر شد — تصاویر ماهواره‌ای با وضوح بالا از نهادهای چینی دریافت کرده بود.
این مقامات معتقدند که تصاویر مذکور با این حمله مرتبط بوده و احتمالاً به ایران در شناسایی دقیق‌تر اهداف ارزشمند کمک کرده است.
آن‌ها دولت چین را به مشارکت مستقیم در این حمله متهم نکرده‌اند و هویت نهادهای چینیِ دخیل در این ماجرا نیز مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71556" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71555">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی TREXBET !   فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛ اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی، Promo Code یک‌دلاری رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی! …</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71555" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71554">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRgxi9kNPc0yoFkKOYqcfwnfV7GnQi_252QGJxS1pkAZTbLrX7Gmbn3Dt7NffcCxnDK6Zmr9WO6pW2fNJgyJTf2KsWxxcWdV1aERDhInuncCaHIgb7bVoOPVqczsc_yY5ltTMrHJkFPP4o1Z5n6l2T_Mm_2HwYLPrEIrY2laWXwNLcWRsVC95MD1JdHK6cfyAOKbg-qoZqZTYuv8AFlUdVgFSuyIr9_GOZmoLTkDjCdXb0TbtPE61c9vxtLLenNam8X9UascDxztYj8V_3wjsU8J3ii3GwDq5wzXc4iNBeLDbtU-gWbKoiCBwkxhME_HA-bSzaSgNk27rNOHXcgLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
2 چالش، 2 کد مخفی، 2 جایزه 1$ در سایت بین‌المللی
TREXBET
!
فردا در دو زمان مشخص، عکس‌های چالشی داخل استوری کانال منتشر میشه؛
اما کدها همین‌طوری به دستت نمی‌رسن…
👀
🔎
باید با دقت بگردی،
Promo Code یک‌دلاری
رو پیدا کنی و قبل از بقیه داخل سایت ثبتش کنی!
⏰
چالش اول → 18:30
⏰
چالش دوم → 20:00
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71554" target="_blank">📅 01:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71553">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=mRJlVsjnBtfMD2bM7Nq6jNug4WipOshpSaD99VJ1n_5qapiEC10K82EO52CVCdOif7BGstHOIPJCb7bNE_xk7kbLW_gQXDeOGmygtPy1pESIZigOyNQ6i86iEfM_OcQREzWkuX2Vg0DHU7bpeH-wNxCk3sc3Xv_v1-kFXv-VV9YpQUD8xY8L-k3CXsAlZYBXBRJIkAnPGVD1KYF7eTFME3Iklrl87fl61J0feTNoImtSR3hvclTLmL_j1-NcjlFbjk63fZuDgetKeBXeUrs3MWZjrRwaYrPExRjlJJFfKcUhkeo5yK9JsqPZp_NtzAb5IphI_TQoL7zhIgNaCKfFOof3tYVtC99fF-5JbbTXu0XAnkUCmjbbeRHCaLks05vhAJ7KsOrfGM-eCw9L-PQkq-MnVeHzsoAgotKHrmkqwH7gA2MdmtInAokcNg4xCTm2w-706VaOEIlyxER0YI6GxoMnzTtoEv-dXg-J-RsEK1DA41AwYWTuiK736izUDb2NeGMKOQu8m2b7DLrR-HUiIsd9OI2w5qh2S5eGZ7XiqrvlgA8O7ViJl76_04bl7g3CIvcEY5m8TkM5gdj2lyK8rF5NWw_c6KgKebqLBiBXSsz1pgz0jMUaMUKAC2WbAJTgYiexO5oD3ihSXklz1AKJL_LZDKA7o8giAX3zL12VWUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad61e1e00.mp4?token=mRJlVsjnBtfMD2bM7Nq6jNug4WipOshpSaD99VJ1n_5qapiEC10K82EO52CVCdOif7BGstHOIPJCb7bNE_xk7kbLW_gQXDeOGmygtPy1pESIZigOyNQ6i86iEfM_OcQREzWkuX2Vg0DHU7bpeH-wNxCk3sc3Xv_v1-kFXv-VV9YpQUD8xY8L-k3CXsAlZYBXBRJIkAnPGVD1KYF7eTFME3Iklrl87fl61J0feTNoImtSR3hvclTLmL_j1-NcjlFbjk63fZuDgetKeBXeUrs3MWZjrRwaYrPExRjlJJFfKcUhkeo5yK9JsqPZp_NtzAb5IphI_TQoL7zhIgNaCKfFOof3tYVtC99fF-5JbbTXu0XAnkUCmjbbeRHCaLks05vhAJ7KsOrfGM-eCw9L-PQkq-MnVeHzsoAgotKHrmkqwH7gA2MdmtInAokcNg4xCTm2w-706VaOEIlyxER0YI6GxoMnzTtoEv-dXg-J-RsEK1DA41AwYWTuiK736izUDb2NeGMKOQu8m2b7DLrR-HUiIsd9OI2w5qh2S5eGZ7XiqrvlgA8O7ViJl76_04bl7g3CIvcEY5m8TkM5gdj2lyK8rF5NWw_c6KgKebqLBiBXSsz1pgz0jMUaMUKAC2WbAJTgYiexO5oD3ihSXklz1AKJL_LZDKA7o8giAX3zL12VWUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🟥
گزارش فاکس‌نیوز:
جنگنده‌ها از ناو «یو‌اس‌اس جورج واشنگتن» (USS George Washington) در حال برخاستن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71553" target="_blank">📅 01:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71552">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T224S4En8xg3R35rLb7Af57sFJwEc-izlAMO9FPSXNrzqMgxP29P9b_Gv_3XcRk-Sh-WaWB5IPnQVsR8tY9VXZQSbChCvNVRmATCgo3j-L3b5SegcOgy1mZpFN91tTOSGGTK4ERH6q5y82UtHNkj-BAFmaIu9dKY_ojcYMPwPpCgCqhKCxwWUtvZ8Y2oMkbCLqy0gZivwC7sVAngz2DYtLM1jDiyKu3AfIOFCqoM9dL_4FFcZjYTx7WsmHshA5MGXUYXPN97E1kNpGaWJjqFMK_srEbbZP-b4ADr20iwdcrwH3xFjxZTFKY4_hEwnqUcB_Zqdc_U5c5ukwa6601zxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛کانال۱۴ اسرائیل:ایران برای خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) و آزمایش بمب هسته‌ای آماده می‌شود.
حاجی‌دلیگانی، نماینده مجلس، از آماده بودن طرحی با قید سه فوریت خبر داد و افزود: «باید هرچه سریع‌تر آزمایش‌های لازم برای سلاح هسته‌ای را انجام دهیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71552" target="_blank">📅 00:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71549">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igDa2FHqk8lUllxkqWP-PU877RVJXGGLd_RhY7Z2O1XEYzwuAjq4k8gxVMSGe0giTsUJLrNLbUtRKED8si26FLyxC5LTsezluipr9RdbVerj4yaZihWvrJ9_gr3Fm-T5zSmHy3n3y39ENaOyHfEfoa2EfJAtrIlIfvi2a25RWMQjQNrH28_qkI6fKDo_bbg-LLZo-UY3EqeYbC9M5Kz9tU4NrqGio31j-zDNtkcBxP98lE2KIb2ujuu_3vZyS0KYfk45N0wqb2SOZfaBzaf0xp_vqmSyu_7DOyNVahsJ2lPZAJyP3N_ChvJnovbntWM84sZJGFszgfa4PAew-EWtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=VX21T1qWW-aF5RpodzotXabW8owo41Dz7sgIEUSEckCByeT8D1gIwrZBSEhOZLTuh9-vMrr8F8bZJK9rwzPBAnsRDu0mI_-6cYfXQjafAYv7jipdYuXShMmWsXuTmyNb_KBTNdBFENdpuWPknl_oH9ITSXey7YwogLUhhgAcqcaewnFvaOUz8Yn9HWKQR8l8mwMxODuYTdOuGlqntVQnNAobeM99A2qu0doAdWwLCvOVybWFoG28nfJ5xOXElkeWvB1BWBlHqbN0jnrQfGkxpAUeD46NsHnJmejY4HWO1-tCF0ta3jQPWQCpay3uuK3T-qGbVGkpACCeGg1c2dQcsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddef7d0b.mp4?token=VX21T1qWW-aF5RpodzotXabW8owo41Dz7sgIEUSEckCByeT8D1gIwrZBSEhOZLTuh9-vMrr8F8bZJK9rwzPBAnsRDu0mI_-6cYfXQjafAYv7jipdYuXShMmWsXuTmyNb_KBTNdBFENdpuWPknl_oH9ITSXey7YwogLUhhgAcqcaewnFvaOUz8Yn9HWKQR8l8mwMxODuYTdOuGlqntVQnNAobeM99A2qu0doAdWwLCvOVybWFoG28nfJ5xOXElkeWvB1BWBlHqbN0jnrQfGkxpAUeD46NsHnJmejY4HWO1-tCF0ta3jQPWQCpay3uuK3T-qGbVGkpACCeGg1c2dQcsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
درحالی‌که شرکت اپل ایران رو تحریم کرده، قمی‌ها طی یه حرکت عجیب، همزمان با مراسم معرفی محصولات جدید اپل، خودشون هم به‌صورت جداگانه یه ایونت برگزار کردن و از آیفون‌های جدید این شرکت رونمایی کردن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/71549" target="_blank">📅 23:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71548">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=PJ6mHfPKAHkXN-G_r7aKXPI9dX7Y73YYTz8KaS12gX0zo25cSYwll5RDd9GuuwxviOmuV_-WERAafaO7QsviGB6zIbey4UMxwOw-ZHlFTcAsHmjKvZ1TL8vovA5YHe0n6NH_hN2yf1W-FTxT51oSU5eFJCcsz9uQ6lyzl7vHG2zqitUaMHYHiw3ExF9KKRF8rV26Xi8_3_kVdGD3VoUY00StcICBWwaG2GMxlZMwGnBGb_Sm6q5swetKoTkf24WA3n4FE13_ZxR4j9cFbUoSQIjjF2vCCH3hePYVwMFKxsqYnPkqlbq_x9BNCu8r6WTAPFXYd2yr1457tHx4J0tQdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8d39358d.mp4?token=PJ6mHfPKAHkXN-G_r7aKXPI9dX7Y73YYTz8KaS12gX0zo25cSYwll5RDd9GuuwxviOmuV_-WERAafaO7QsviGB6zIbey4UMxwOw-ZHlFTcAsHmjKvZ1TL8vovA5YHe0n6NH_hN2yf1W-FTxT51oSU5eFJCcsz9uQ6lyzl7vHG2zqitUaMHYHiw3ExF9KKRF8rV26Xi8_3_kVdGD3VoUY00StcICBWwaG2GMxlZMwGnBGb_Sm6q5swetKoTkf24WA3n4FE13_ZxR4j9cFbUoSQIjjF2vCCH3hePYVwMFKxsqYnPkqlbq_x9BNCu8r6WTAPFXYd2yr1457tHx4J0tQdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
لحظه‌ای که جورج دبلیو بوش خبر حمله به برج‌های دوقلو را دریافت می‌کند
جورج دبلیو بوش آن صبح در مدرسه ابتدایی Emma E. Booker در ساراسوتای فلوریدا بود و برای دانش‌آموزان کلاس دوم در یک برنامه کتاب‌خوانی حضور داشت.
نکته جالب این است که بلافاصله از جا بلند نشد و کلاس را ترک نکرد. چند لحظه در همان صندلی ماند و سعی کرد آرامش خود را حفظ کند تا دانش‌آموزان وحشت نکنند.
چهره‌اش به‌وضوح تغییر کرد و حالت شوک و نگرانی در آن دیده می‌شود. دانش‌آموزانی که آنجا بودند بعدها گفتند تغییر حالت چهره او را به‌خوبی به یاد دارند.
جالب‌تر اینکه او حدود هفت دقیقه دیگر در کلاس ماند و بعد از پایان بخش کوتاه کتاب‌خوانی، از کلاس خارج شد و در همان مدرسه برای خبرنگاران صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/71548" target="_blank">📅 23:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71547">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=vZjatzDv_TPQ-wpBml_UhitI-OBdcSwwY0hMwOYfxvf55DBeN3Sm_mlgrGqKlLk_EIA29dUHPP3oWGdTO1H2iVK4eznvu5ALzI_zzgWgUUA4rb8HCnrPQe6El_lVhD0-QuvY33iLuaUEQUjh-m8hZzvMtm37_4Twi6bm5mjxq6Lsssi3BtfTJL0gPe6nXxtrl_rB54YdZzYwwG-PGLIup-PGSZQyJfAkATymXZ91xQV93w_6vAlMBTJkukPKDuyL-uDOHCunNOzqgXb5HdgPqCWIyTgU5eP-GtC9MbmWv91M4B1Jzc3-g630RO-O6mmavMR7sq4YUWBdY8mS2QZORg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e621bd826.mp4?token=vZjatzDv_TPQ-wpBml_UhitI-OBdcSwwY0hMwOYfxvf55DBeN3Sm_mlgrGqKlLk_EIA29dUHPP3oWGdTO1H2iVK4eznvu5ALzI_zzgWgUUA4rb8HCnrPQe6El_lVhD0-QuvY33iLuaUEQUjh-m8hZzvMtm37_4Twi6bm5mjxq6Lsssi3BtfTJL0gPe6nXxtrl_rB54YdZzYwwG-PGLIup-PGSZQyJfAkATymXZ91xQV93w_6vAlMBTJkukPKDuyL-uDOHCunNOzqgXb5HdgPqCWIyTgU5eP-GtC9MbmWv91M4B1Jzc3-g630RO-O6mmavMR7sq4YUWBdY8mS2QZORg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مشهد اردهالِ کاشان، از " نمادِ مشت گره کرده‌ی علی خامنه‌ای " رونمایی کردن ولی انقد بد ساخته بودنش که صدای طرفدارهای حکومت رو هم دراوردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/71547" target="_blank">📅 22:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vYtMeYLsvMWGEcZVxpfEwTDpOv3yIKkV-AvWZlBb1F5rNqVGlluS5bhN8sPvGw0YnSNrI9yJIzlqwF-5g4Su9wKOIf1r_sSJiZHSG9pJc_2UJ7PyqWLESt2eHChNfNG2nXUWABMntScBqo0AMpI4vkwZGnZJ-X690qibDRGspLAT7D0vPCZkntifLpCVkxytVjNWZy9r47asjqHW_xtVePrJ0EybMyNglENyhFZRqkmQUYBlYOrtvigpHJo4zPZOKsGhnLEhUz1DRhbPHZaGf_xdN2vMYRTdAtP-m5vL9E5xfw2HXsLgUdXHVkidX7p7_q17Fu7YsD6oYuL0OZMXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SxbW6NSp_cHow-ZgCatJEcISGgyF0h2SpzYRTsAZ_DOniJmzPy5dwhIc5n-R0Wss4q1jYNPZskS8SlO_8L_izMsr9cHE_HaYTNgZDPq4H0uGo_J9T-Yu-MLb-V1HwOK2UVrx_u4KJuL3aa-Bu9ByrsBcH0-g6_7TUC4OovTRYkCBcEij8S7sIqPszojFhPBgGFJ8jHsS6PmHH8cS5_Z7w9hLSYp7EkA0wTSU1y4WLsiaLzTtwdCuZKMO7_Syw3GXcn9t28VsTR5cxs03roq939OCFtyu1oWFpySzoZve1NyRQjMjOlTqbgDt9LqTFyAk32O_s_mUGy0rcOCb2m_FDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aNkNBUkOyN47_dz7uVffuvyL7-vzw7yw5Ch0hZuHtW7ulTasxYhrF8B8zETqOCCWZmOCVQVuzzGIl4Xd0P9XMgU7VUEAJ94FTwCvq0f1AsXkE7vrseuHxhjHq4Dsh65Im8TiG5ORI3tjDuXWVjEOcHGQIwD1EOLZ7GCOa5ghHLWH-X9hxkImMg9FMT4kqLqeOCpeLWK3CrTeX_50DBHUK9mKElc46Q5TEf9GtBNcL1LBqfKsm6vwOcirYJ9QlwP2Xbpz24yTNVRB59FvSrwrqoyHjOYlagUJfEF1k67QI75RBf5VXBJ61yRlAQ3yGawvEiyDcWpbpjXhIcoh9g8qAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
کشتی‌ها و نفتکش‌های آسیب‌دیده ایرانی در خلیج فارس.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71544" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
شلیک یک موشک/پهباد به سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71543" target="_blank">📅 21:07 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
