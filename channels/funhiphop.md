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
<img src="https://cdn4.telesco.pe/file/ginW65TtoNAGL0srwEef1eNtnMGLJzzqnH6I-o7rExEYGdYL52VMGVan9OSVpaqXna1oEYNkSUun4nuPVv2WNuyUqFUQF8U6yJx4J1bKKbBikBcFdEgvYgGb_KnCxQYkPtbQM5xyfx2AQfYFyuDx-CbonknPZluWigO8BdD-7pg9CzVhTM70j6ePsry6aqUqsJOnlATU9GAI2b4LC7l3yxVyTkJ1Q9Et-UQ7YWH9sA6jcLBd7u_YZXAcZAyc1AIoWuSB9usyFcr92IXVxWqt-mccHvYNMCRS44aTdg_PxFtlEPYLq1L4sH7JRUfwt0xQbIlwkL_MCPC8OGDeZCvWHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 254K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-11 17:51:23</div>
<hr>

<div class="tg-post" id="msg-84368">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qts9kM6_tdn5tNvUeuuq8gADpXjGXxBHH-M6yYbnkv9pWZ_q8v0K1CC8bg7-gtmO_Aq5k0IT2cipo8rXcs9kZ4NqcVTYBp9hTqocy1F79vQOoiKpK8yhS_UeQAV0XBuM6xfjuOmvxytdEfhYUO99FPiYBV3IupwgrS3zGGOx8A1HSSvNt5rARv4n0pBdcxet7i-uD7fPu0Yuzsau5mpZFzf2ptPwkkcRg0f7YjBOK-mikjCGgv5mopbe60cNG3_nCsWCDUVr-iKXELzBEbxqn-us0MOZeM73ueo9VwuixEhR1Z_vxu9g9K0uc5qoZYIBK0UqMNIK-RIx4G6xmPFuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال the gentlemen پیشنهاد میکنم ببینید فصل هم ۲ تازه اومده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 281 · <a href="https://t.me/funhiphop/84368" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84367">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اگه مصاحبه فرهنگیان دعوت شدید همین الان بلاکشون کنید، بعدن میفهمید چرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/funhiphop/84367" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84366">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این میمای کنکور چرا آپدیت نمیشه، هرسال موقع اعلام نتایج همین میم ها تکرار میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/funhiphop/84366" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84365">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/funhiphop/84365" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84364">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk1iyzdtE1orgX1mY5GhF6y6vdeH8EvJCdCO3tS3jcZ551WrC94Vcz6RBSHTYlwCb6nH4dz83qMqOUE3uIRMgvCtayQvDbSr3EVB8s6swUvkgllC654eCPBVGU1dijpjpCUTlxR5gpS67foCUFPvTM_4zFzfQaHTnM4ugtFt_H3ZF0ZrFx6-0_NWMIsYC9C3-WxoGEmOaP7L_LFYUcqyZmfpmxwXJLNIAQhAC7HVmkhANLZllEYR8XoAkxV6QF3pBg4I4fYa0Bgf1EPww0pBs8Ot0JfV7xZkP_fKxkG6hUWJpKn-83W9fjR_1YwACRxKAa9zv99G9wgsV90CwmIPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/funhiphop/84364" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84361">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ik-7VwS5QIswV4lu78894fKwVT9gmZNWaFQES6vBH8iLpp4oCjS8RxZ0KoLVGlpAiCPvvRpa6E-xfQZVmSxIJXupca3pGOEZ9bCFXdd_in11YIeyot3dfvdckkvJLop6CMOhsHWKdWRhklsGDzdD5FF6hNluAdA-Mt_KtJYNQ99SEyfEpcG12XVWIEbUirZPeGeD2oFdC5SrFN7_RZrQ_LzPdwdzYGwVM9-Om7IJGqjCL6yNqEB4Kv1AXyBKwHH9qnhi0zKjQJiqgyRfqW1z32WLbzPHxVYFVtUtP0euOnsk8mjsS1uk4oAH9ngC0THwatonM5y_Y74s2micpTdLoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/funhiphop/84361" target="_blank">📅 16:31 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84360">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTileKhersuk🐻</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnFEjoq7H3OGfgaasW3Gsa3iaW6oTyWCgYG2ZmJVvWnf6MwxKygO0tmHnG_dPzCPD9JXPMaknlfNTavai44MzLswQuueH0xAhLmYVUAl7nxHQqbMaXd6MCO9ThWFcI-tIFTLbi1bX2I4zBAVtku1b7njc-OQYNKhXDvZ-HNvjPZwtBcE_my-RnqiayxyoX0AwD72y9O_JI8nv_UkVg51Db1c5_n6BD7bv9OXs_8SSJ53_oOGOXbawxWGhze_7YYgVwtGmOk843ERsD9-T185x2ocoVRdArm9faQRSHai-ccifuHxp0jfjsFJVyBZK-lg8GUkyNluYRLWBYyc3h-6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر خوب</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/84360" target="_blank">📅 16:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84359">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نتایج کنکور اومد
بفرستید ببینم چه تپه ای فتح کردید</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/funhiphop/84359" target="_blank">📅 16:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84358">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جردن های تولید اسلامشهر که مسخرشون میکردیم هم دیگه زیر ۴ تومن پیدا نمیشه، های کپی ها هم شده ۱۵ تومن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/84358" target="_blank">📅 15:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84355">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بسنت اومد گفت تو دوماه آینده دلار ۳۰۰ هزار تومن میشه، همتی در جوابش گفت آمریکا هیچ گوهی نمیتونه بخوره
حالا دیگه خودتون حدس بزنید تونست بخوره یا نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/84355" target="_blank">📅 15:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84354">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستان استرستون برا کنکور رو درک نمیکنم
کنکور فقط قراره انتخاب کنه یه بی سواد بیکار باشید یا یه با سواد بیکار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84354" target="_blank">📅 14:08 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84353">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ux7WyYkqbF4xlNOW5NuGg2qTdIyYqLb8njU8ZZzF7SaCDRWVhiavj56QaSnhTbIk-A6qrqg5uIy_rEgNHRYsgMuWaKw92LDjd3cOGTHWNxdN-N8wD-WAthKZ8PceSw8uKhrKI-HsRQNCjFml7d4CqrHlTRH1ZhLwQtnmhmx7rcwCaAd3ymh2SUPKtOBx6ABJpWv7w3CVBpPzbxq62OjqTtHSk8-7kNlPjaSc1Hy-PeKzuDN73ZeJSdeS_X73BmkKH0QODv7QZd7dZo_dJKqnA1_j2uzi9kfDuqmXJzF3J6q5oedhokRQAb_ydPZrlBhR_mA5IBJgmSkkyci9o_T8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنشنال یه گزارش جنجالی منتشر کرده که میگه یه جاسوس موساد به اسم «مهدی نادری جهرمی» وارد دانشگاه امام صادق میشه.
بعد از یه مدت وارد سیستم حکومت میشه و انقد خودشو حامی حکومت نشون میده که بهش اعتماد میکنن و نفوذش بیشتر میشه.
انقد توی فسادهای حکومت و مالی دست پیدا می‌کنه که دیگه از موساد پول نمی‌گرفته و حتی بهشون کمک مالی هم می‌کرده!
حتی توی یه مورد به یکی از نمایندگان مجلس ۳۰۰ سکه رشوه داده!
طرف توی انفجار کارخونه موشکی ملارد، شنود فرمانده‌ های سپاه و نابودی برنامه‌ هسته‌ای دست داشته و در نهایت از ایران فرار کرده‌.
و یکی از مدیران اصلی برنامه معروف هفت هشتاد بوده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84353" target="_blank">📅 13:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84352">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هروقت میرم اینستا میفهمم نسل چهاری ها بیشتر استعدادشون تو بلاگری بوده، شانسی رپر شدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84352" target="_blank">📅 12:12 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84351">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نیگا ها و فلسطین فن ها فرانسه رو دارن بگا میدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84351" target="_blank">📅 11:40 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84350">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1jmAaoHeU-P8YYUnvAVvhV2rNJYI2gaj0Fgi86tYsFUvhGXzWlpQocNU88CGEaE2PpWcNsRDBvXmARdQycTAzXL4ZLtRb7aA0hXGEFyRD2YOJkHLgOfDBIVCHUB24lydvCSGBlpXs4v818ljBlY6vL6Ta8jsIYXDf9V2lmIdVYAZ9JRmvfzuTxK9wGSCq8b4RPN4p1Jr70XIDkCnnqJabV6hPNtEx-7_sjaPSLCrL491R9JogVneSqBdKhjw0-eGs0Iot9MsJsNkoO892Y88wJY2IEfap0FZHDdOTSqlTX8VfEsIFnLpX-QV4aBOKSNehor_sM81mdi4j7NDve4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا کیرم تو این اکسپلور
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84350" target="_blank">📅 09:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84349">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c459c9f9.mp4?token=q5-Y3OZF4bD9dekC1JHi3uHOWaWsW10cUZYfTU2yDZ49bBdtu8dO1RnBqK0sNG7JdrBg2A4UVhEwVUlhdHNSmUl9E1EDxbptYLmGIc5fiBBc6vUb3yZX6UBEgqsx2h3eQqJEazMcu8kBldveds_0u3A2MblnRZXdfh1ttvmC8j5IHfLDUUtqND2NJE_COeStRken40M-XVG8---WJh6o2En_Gv8f61aXxHkz05Ol1nfCFsgZzXIxezJp17go_GGm1gmBWpYfKZEpsutLyGySLu-CrmzGWuYeHdmzkf80K8xO-oeEfI8212wAZNRGefcPaBTVOvvPvjFLSOAXvhxK8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c459c9f9.mp4?token=q5-Y3OZF4bD9dekC1JHi3uHOWaWsW10cUZYfTU2yDZ49bBdtu8dO1RnBqK0sNG7JdrBg2A4UVhEwVUlhdHNSmUl9E1EDxbptYLmGIc5fiBBc6vUb3yZX6UBEgqsx2h3eQqJEazMcu8kBldveds_0u3A2MblnRZXdfh1ttvmC8j5IHfLDUUtqND2NJE_COeStRken40M-XVG8---WJh6o2En_Gv8f61aXxHkz05Ol1nfCFsgZzXIxezJp17go_GGm1gmBWpYfKZEpsutLyGySLu-CrmzGWuYeHdmzkf80K8xO-oeEfI8212wAZNRGefcPaBTVOvvPvjFLSOAXvhxK8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش هایی از آموزشای جنگیری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84349" target="_blank">📅 08:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84348">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/84348" target="_blank">📅 08:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84347">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1NCTOD08nKafPTtIY4LgbgzMAoeCeuIwdxrWg4nSYRauWX10--hGa3PvspytR50FA5ThjhAy4EebDFm9FoBm43EbszWpdJtwe5GeacBTlYpQ_yqWwFjXfli6FDe6hvawOLM0EurPvmJymnTLXynBy4Ltcr0FhqQy8bLBUl4ggTUBAP2TWYyFZ_re6C3NhO_Jd-5eDRQI-sM43Sr0D9zeJ_GqZ-8Cjpfu10h_zGM4LzJn7w7fcJSM1wQrniq21zgGZYaaTM_6Uj1CDyuigVuKGmiBaJHBVTFIaOD4vGAw1x8v_kuRX_Xj6qX83eHM8TJz6vgV4x0G1Cq3fTAi3Q91g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اسپانیا - جمهوری چک
⏰
ساعت ۲۲:۱۵
🌎
📲
مقدونیه شمالی - اسکاتلند
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R11
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84347" target="_blank">📅 08:55 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84346">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d924213c.mp4?token=e9EOPLZfY5vxhfpxWoDGcSeRG_2Wcco9wM7VHfKgViXKLgkW4HOkwwd_UKcOO8155RG1tgTySpUR03IwRfvxStLWMgplIXgSgkVtzVbOVMb8naXGLM8BhiHQ46wztQOI-TWz7MkZ6v2vk0MXUyKxcnmxguORJU52bIhm85T308_w-Y4BlcRVZwznY83GjPMWDvlaYGB0p60ONmdHsqECqBxrVHWype-YOXh-JoseghkfKMcluPpdswTcwHBgDC6f8AEDsj-ZcfLV7Mw_0GgcMX5uJGYpvQZVAztS7Z3YiYM9MoyUvuqmkbrrU8cx1hRBlvYlMhLazeBiF9FQBJ9M-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d924213c.mp4?token=e9EOPLZfY5vxhfpxWoDGcSeRG_2Wcco9wM7VHfKgViXKLgkW4HOkwwd_UKcOO8155RG1tgTySpUR03IwRfvxStLWMgplIXgSgkVtzVbOVMb8naXGLM8BhiHQ46wztQOI-TWz7MkZ6v2vk0MXUyKxcnmxguORJU52bIhm85T308_w-Y4BlcRVZwznY83GjPMWDvlaYGB0p60ONmdHsqECqBxrVHWype-YOXh-JoseghkfKMcluPpdswTcwHBgDC6f8AEDsj-ZcfLV7Mw_0GgcMX5uJGYpvQZVAztS7Z3YiYM9MoyUvuqmkbrrU8cx1hRBlvYlMhLazeBiF9FQBJ9M-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز خوش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/84346" target="_blank">📅 08:26 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84345">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgdTcaGDZgpMa2f7S9F_wmtS5Xx_oqw6IDOiU3AhCZI1U1lxH3jHrxConvmYsbL4CS4Ti_H_IY5PId9oS_M_e4RdA7sOOWYl9-8eSjEYgVcz_C36IPUCQx1tTDGsfllvx7Jg_s6TyuHZ-kd56-aamDOCzLHLtM-Tc-o_2ppIklU4JdyJOqz21WjwsgghymUfFHzYFNieryyOfbQfV5M888Iy4p5PTzbmYsw36sRJaBVDtZhHLwL9PVBPDuhLs92YUMBTHpamlaoCKFm3WCE94FextJwj-JcRVApc9i67cA769ylDTPG5ok8tZ-nPJ-F5c1-eJCK5Ntqx2TWi_9R7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پوریا عرب نامبر وان یوتیوب فارسی
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84345" target="_blank">📅 01:07 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84344">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR3x19B9mdH5BbfFTm2gWBWbCZa7oXQalpYDPRG7LtlIkVACz1JuqL4k1ZNrxKaC0TrPYr0kA5E509LBlS0Pxfevady-ehrROYL3bE3wU4oQPqxmCCroi9hLeezuAiTZOOzLMYN_ajeYYKATsUU28DIkq9-0GORRIIAs3jGGr7iK18MGIdoB165D5J5w4BVj0Fv1io96eWJ1bI301AeuxrOs0OarDLjc1JEzTEYJGYf5EhnLq3nODvhmdP_SGyCT1mSDkp1nReaGqqU2TRRgeYJsllQQyu65NDwtQK_4JjWsOrbI68rmG4kOw2o_nTI9KGC0RgqSzEK_EL6A5qjCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Batman: Iran knight
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84344" target="_blank">📅 22:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84343">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a0a505ce.mp4?token=Uos6evmOWm19bidtfPXjmZcpjYMEd9_Xc2__jznpbwjWe9yFIywJ6Iec59hn29Zak_BdKigSKcfdDx5QNCKbYPGVx1pxQ8B7-2VbmZ5y2nawTZUYP097uooQFCyYVHa9dhnzSyUDvJzCqDOXMsA2Pon-qCJt0a9SYo_ZMSRvlVBulCOHq1S__dLZ6TgWEg2X4tFvYpFJhsbFFXDubtdFmg8SW__B8pQbswY1ophTIHpSlwhZ4cBzSTpI-U6x8uUomilGmrLE3KAbax1h9YwHAiUpFbLn5V7eZ2EqvIHra_3Jmt6QG9s3Q4YDrKOVhi6LFfKasFLo4e67vkp5-h4ilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a0a505ce.mp4?token=Uos6evmOWm19bidtfPXjmZcpjYMEd9_Xc2__jznpbwjWe9yFIywJ6Iec59hn29Zak_BdKigSKcfdDx5QNCKbYPGVx1pxQ8B7-2VbmZ5y2nawTZUYP097uooQFCyYVHa9dhnzSyUDvJzCqDOXMsA2Pon-qCJt0a9SYo_ZMSRvlVBulCOHq1S__dLZ6TgWEg2X4tFvYpFJhsbFFXDubtdFmg8SW__B8pQbswY1ophTIHpSlwhZ4cBzSTpI-U6x8uUomilGmrLE3KAbax1h9YwHAiUpFbLn5V7eZ2EqvIHra_3Jmt6QG9s3Q4YDrKOVhi6LFfKasFLo4e67vkp5-h4ilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو کمتر دیده شده از رپرای رپفارسی که ریلز با مضمون پول رپه منتشر میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84343" target="_blank">📅 21:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84342">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj5iCjfsMu6g7BcDWi-kZLaek1tPio3Xhn9sPvu7p4CFyz6qz5je7GpWWuv_uiLLcQi7cDpVNZSGqKWZB567E9-UbXsWHQdanH5Ik4P_zSq1kD3KCGQUFkwe0D2oD8jSybK_075bQc97tGS4A4RAoYZd5h6dD0X6NgvS-EyEjVnnzdDqDmni-3KI2gxsCcnVLBcWG_EUNy2NJGCn18fnUn-3GZVERfx1viyqHhDHFZ1-0omRvdDpx2Xuc-jCOLRuMIe94IEWorYx2zv-d2WQ8Qm3QAyqzNKX_o_QEgoOr094yV-zIgz2t81BzS2psowxNLWhzVzBEyHGWpPIF-ETTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خلیج_فارس
جهانی شدیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84342" target="_blank">📅 20:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84341">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چه عجب آقا دانیال تصمیم گرفت بعد ۵ سال یه موزیک خوب بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84341" target="_blank">📅 20:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84340">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترک جدید دانیال اصلی به نام "ADHD" منتشر شد   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84340" target="_blank">📅 20:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84339">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpgaVaefplNX5nLA_ufxLPpusnWQSMlZdcAGQzRP3G8mibxlZi_1EaU0c0vW0YkPEspk3C5TqCEEpDPzTNhVmHEySAXBCG2Su4GnDI6fDmk2h-w84GUsZWheHSfws8AJnJv3iMRQLRheE-1HDBb7lG1MNbGBDRuTYHu_f_RGKSeOcsDvZL4uN843NwGRr_tgOIMzEhX0-BJopSe4kDW3GghMRncjP4i03_mZjrMWysvastKWCvGeRwdbqwYsvDmOpEvxnPzYWmBWEUgtp968lXpSA2VEpwuxgbRvsOa87WlSVa9dZkLoFhDtj4vtCUf_p6YuE_3U12kBB7khBxFRoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال اصلی به نام "ADHD" منتشر شد
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84339" target="_blank">📅 20:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84337">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVbWepG-HVWXbFK6ekE8X8S37fA3A1g2KA5OVMPvzlfICmvgnB1H_CeQFDvwED_tSox23zDYL8XdXIS2l2tytQKM3kLqLPolgtTNbLWwcLJJ0IWjurAbPC4RPzSRYuPuZ4U4-pKb0etM3NW_vtFx2Mzh_ONcqABMm_wTJgT8NrYCEPqnDBksKjc50ff-wJRDUK0mOJkiaoAX_fPJK0IYgirWXIBtMRLKA0-OG3qQUKMpQa-3cXxlxie3gcwzl53utW68xqUWD8gecZy-Mv2tvAArmJ3OHoR1vPRG_XWFh1vmIiPhLIyaWxoA0rXvQRE5MukCx62CVeyIEOVWrY5Ryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e52f441c3b.mp4?token=FYbEvfCxWcTWzthcSbjp1rkpolPO0Rakj2OVyEAFNcvLGf5Lw-F-Vu8HAvY0TTHO4GnAp8dAd16-rM3404iBo3kHpppk1cchBZvyzBEVko0zU_l6rKjXf6RtE9CBUdg8FFCVV3bGddsWOAsWpjwcKvnKp0nXp7kVpGelhwvU8aR5ezwtsf_v3oXbnLZjjKJBSpyZvhUl9eVXnWBe5ntrJZZ26fO3E1zXd9v-qeqWCnpGgtotKoXVuyXsAGa72MEWBkRdlwv61zRRNMn7rblRrGYSAc2FVC2x_tCoosKUw4k3XW5u3WydAEzNdlvmXMJZtgkNN0EhXsbOV_-fZNB9Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e52f441c3b.mp4?token=FYbEvfCxWcTWzthcSbjp1rkpolPO0Rakj2OVyEAFNcvLGf5Lw-F-Vu8HAvY0TTHO4GnAp8dAd16-rM3404iBo3kHpppk1cchBZvyzBEVko0zU_l6rKjXf6RtE9CBUdg8FFCVV3bGddsWOAsWpjwcKvnKp0nXp7kVpGelhwvU8aR5ezwtsf_v3oXbnLZjjKJBSpyZvhUl9eVXnWBe5ntrJZZ26fO3E1zXd9v-qeqWCnpGgtotKoXVuyXsAGa72MEWBkRdlwv61zRRNMn7rblRrGYSAc2FVC2x_tCoosKUw4k3XW5u3WydAEzNdlvmXMJZtgkNN0EhXsbOV_-fZNB9Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها یاسو دیدید چقد متواضع و خاکیه؟
یاس:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84337" target="_blank">📅 20:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84336">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26448031d.mp4?token=Nd045PCHGN0ONaU6G3tPc_RHJW3tY5Uv-u5vWZ0AhI6jV8RGCnJeXdIhug0p0hMSReDwxFDiOV_ZlLpE5VztJG872LxH0vTjZbvYL2U-0fteFtQI7mfbwr3lGfuRSJ33iggzvTiiMpcoVeMTg1gmFZXgXQkcrwPlRh6Z53HjatL2XsRhU_nbYx_R9BJrfCTcfkUzvU5KcxWsdZSHe_MKYgLad46rA0SvpksfZMk7ohHxqf33q97EXr4v-k5i4E9hkKNpRkOu2irGldllgxMS4eUtQ_HV9FzYSWMP821_ll50zD2h8N8gOd-Yqb379Zv8Glij63DXwiJ5lS_3yOi4ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26448031d.mp4?token=Nd045PCHGN0ONaU6G3tPc_RHJW3tY5Uv-u5vWZ0AhI6jV8RGCnJeXdIhug0p0hMSReDwxFDiOV_ZlLpE5VztJG872LxH0vTjZbvYL2U-0fteFtQI7mfbwr3lGfuRSJ33iggzvTiiMpcoVeMTg1gmFZXgXQkcrwPlRh6Z53HjatL2XsRhU_nbYx_R9BJrfCTcfkUzvU5KcxWsdZSHe_MKYgLad46rA0SvpksfZMk7ohHxqf33q97EXr4v-k5i4E9hkKNpRkOu2irGldllgxMS4eUtQ_HV9FzYSWMP821_ll50zD2h8N8gOd-Yqb379Zv8Glij63DXwiJ5lS_3yOi4ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برام سواله یمنی ها دنبال چی میگردن که با اسلحه ها کاری ندارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84336" target="_blank">📅 19:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84332">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سلطان حمید رسایی را آزاد کنید حمید رسایی را آزاد کنید رسایی را آزاد کنید را آزاد کنید آزاد کنید کنید  آزاد کنید را آزاد کنید رسایی را آزاد کنید حمید رسایی را آزاد کنید سلطان حمید رسایی را آزاد کنید  #سلطان_آزاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84332" target="_blank">📅 19:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84331">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فان ژوله غیر فان ترین شوی فانیه که تو زندگیم دیدم</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84331" target="_blank">📅 19:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84330">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxjNlCX8pCB9OyLbDg68PBBjEAU586hVKsC9HLuwEqO3v-PBVkGZPshHJRaQwn2oVawk9ACfUNx7x7Y-5Z1cIBG2hD8A8vhHuF1AGxqQ5ffimpVvpJr-PzTH8q7AsMBg1BKH5ZRko2aqpcTcaPyvguwHRyEnsTacn9e-8JyxLXLZbW6CssZOoznAhxH2Dy68rfxDSfMcdxmAaaid5xpHDZeuzXhjyg0Ew0YETuVW_i7Q-55hkrGdnj0k4MbRAitWU9e4jqKc4aXXnSnBoSY3cEAzHvPvzGCxFmfKr8eJLrftikuhXvIi3lHrLT0pID4LDeZLcwHyF5TZ6rrDROxsSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران حتی تو معروف کردن کصشراشم پسرفت کرده پسر، از این رسیدیم به امیرمحمد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84330" target="_blank">📅 19:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84328">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phCBl3M-dPHSKn6wXhfe46GbDzDvv5apOUwF9xPhguVfMhrlsnrJt5qmHucM-unOQQkuFCq8ayVHDXWAEFZxD88ut7fPxJpIQc2JqOsYmbalATRlSkeshh5hmT8MEuxKm7t6heE0ly1E3xeCaUP6EsTGFFSVWwmji55FX1N70eKVcEL4ciKQpPr78aqK2iMW7aT60lQsLZmESx3NZT8Fls7LjBRRuyJb5MiJC5bnojbI3nNCXYL2YxwSnaM0AY2Jia5kbzSWVMfFkVnuzTtAkKiv5Y8a3TRLkfB7_aWvQ3tcQ2o079uTA5oQw517IHT99mfBmz_apWuixwL0765H-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XPLZathFVdD-0q8tIiLmFS7ESmwTU7pDlY11BAsf8sspcR3uk4Nej1Y8nKbKh5W13HkoailMIyL0RcEmrgEK9hOVs67lFgQUbcI33mXOPt6ZVSwNMpZe7zzoRS_pVBqj3HCbveDXTBLQyGz39dutj0sRy6PZ3z8ER0z7c2zKg9aLpZPrGbuPhIFiTQnmbVhU4J118_8lyzuL9iiHqw-dAh5EzXOSG1ui5M6TNrhuTtdFiGaUY3yIb9kDx80LnBs-LrjLPW184NEsbn7z_bV8sCmXF73klUq61Fls6-tKYGpxoCeX9WEW42oXZ4sInUwZDM_X7KIZdOGtE-tqSdf8WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترند جدید اینستا اینطوریه که دخترا دارن کامنتای کلیشه ای و کصشر پسرا زیر پستاشونو متقابلاً برمیگردونن به پسرا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84328" target="_blank">📅 18:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84327">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0sNDQjHHsZufjzm-HbrjMr0omOZtfrjC2d7Z-pepp8qhWWYnyWWJgW3TJYW5G-9JndgcPdpfaqR72EO93dYxLQxjdkfBGhT6untvwc9b2bBTWjwvqAzoLDfiamZgLhh83isgbcMyukYlTj6q8MbfwihE45ksfzQo7-_lruclJAsPuxqzFsm2Is9_wdzbM2tCCaWd94TN4dq-wXFr0hBpMoVp_FWLm7OqvRayymITg8DI2ht-mLPPJt7q3fcZe93qM8l0d6R4JuZSxgsVecKClCVqIwBF18r7lYg2f2_-i6Ys6dx0XOxhB6ZDbYfud3gcGwyv3D88ffvqsfUFkaSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G10
🅰
🛒
ورود به سایت
👇
✅
https://ewreioxko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84327" target="_blank">📅 18:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84326">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چرسی: شایع اون تایم برنامه گنگ گوه میخورد که من اطلاع نداشتم برنامه قراره از فیلمو پخش بشه، اشتباه کردیم ولی همه اطلاع داشتیم که ضیا داره با اون پلتفرم حرف میزنه که از اونجا پخش کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84326" target="_blank">📅 17:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84325">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6261d1f5c.mp4?token=OmyADvxOUtIQ6YH_V6uDgEi9E9rJAea62zryOf6MqPRan4TOvmKHX35JeedJIptknaei5teIvoPyMdkLv5w2PXp4zGqIsTmie65LKLrvhzex_AMajSDHYMJKP29TTdxOWZ9EZQ7cMTEckStCG_5z5WtvV4u3kpPT-ySwWIIQeyW9GX_8Iy3STL683OsuTRtS4KGuZTgJqtXRlNVzbEZhxF4p7cVNrBPw1YGg5QFMVqGc3gC2W2icD7FduTIfxVDPJNy6xJpnegV75nXOZyFDTvf1FFMoZvrTmw_h7i5kHL_iwudWL6BPIf4zcW6YgTObVQGyXWb_Imr3gik40u0UXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6261d1f5c.mp4?token=OmyADvxOUtIQ6YH_V6uDgEi9E9rJAea62zryOf6MqPRan4TOvmKHX35JeedJIptknaei5teIvoPyMdkLv5w2PXp4zGqIsTmie65LKLrvhzex_AMajSDHYMJKP29TTdxOWZ9EZQ7cMTEckStCG_5z5WtvV4u3kpPT-ySwWIIQeyW9GX_8Iy3STL683OsuTRtS4KGuZTgJqtXRlNVzbEZhxF4p7cVNrBPw1YGg5QFMVqGc3gC2W2icD7FduTIfxVDPJNy6xJpnegV75nXOZyFDTvf1FFMoZvrTmw_h7i5kHL_iwudWL6BPIf4zcW6YgTObVQGyXWb_Imr3gik40u0UXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی خدا لعنتت گنه بیماریت واگیر دار بود فک کنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84325" target="_blank">📅 17:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84324">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یعنی این گیر دادنای امیرحسین قیاسی به مهموناش برا ازدواج کردن اتفاقیه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84324" target="_blank">📅 16:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84323">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دلار 260.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84323" target="_blank">📅 15:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84322">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84322" target="_blank">📅 15:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84321">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شماهم جدیدا ترجیح میدید یه سریال کصشر و آبکی ببینید که صرفا زمان بگذره و دیگه دلتون نمیخواد سریال های طولانی و با محتوا ببینید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84321" target="_blank">📅 14:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84320">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTizZp8aByWGqDu1stdS2mlEKURjPM89Jryibn-2iW8h4C9zdiNR4LwJ9or6T63aehM1YLlYWzyTZMvxhohDEuLFXilt9oeO_Lhb77a_t2QhdG7k0w_FFPi_ub4k7tRQj49IKmIc1SGbaP4xTXCTu6J5qeny08pSzm6hmoWL2mxRKkkT0iUCqT6TzZKGSvtU4iCrWmQFow3-CoaL7--xGBuAxaXZE4clKNuO3sxpmKf8g4UPzeeykfseQb-C4UeVdg8y6dhuvZnDk4INuuLarfCPc2V9I64gmSwmAhJ4OvapIFgHB-4PhTrPE2HMzo2NhcEXPw2DxEcWxnX-YxSXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسرا بعد این که کریر همو گاییدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84320" target="_blank">📅 13:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84318">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVGsrHb-apASe-rFelOYJjrxrGkVd4ISL1kM3YEIPAB_a455Z5_5eVoUeZm-nWSq4rNoQQiBmSgMeFKTGzkJ4MLpi1hbRXbbHmJhexRH3g_ajfsGvBDgafbcmRld_HfLZ7iCChgGQzRUQfwpzCSuTiODaqdNRt9QwX-oi00Cjjd1tucS5a_RJ9kvMHvu71Rrb0IkLiMG3sXkW885sX53mHRKilnXQNCsc_aSVYhJ-92T7zJzuufKvR7tgIxwbNvVhe7I0yTYD2ClKvwTgCX6iUgUkMLX24436BQFYcPzVMnna7BTFcoMMo5uydCd1A-M7xr5vfdyndevM0N3030wOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداروشکر داره عادی سازی میشه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84318" target="_blank">📅 13:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84317">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7384d8a494.mp4?token=Kq3YUMrYZ0RKWESw15_x8AsFZACnd7iZL3MZpD7M-0FSnExIxR2g6khjexPSjjvZ-DChTzNSlxbhH-9k3jgyN-i5EIqJRTE66k6n3RckOFByn6aFH4wMC6ewOEnr6gtbE5dRPEmesi4Pp2jLIGeHneI3-ZOXzzCGptuEALpl_0jLUzp5jaBJyetkl6Y4koIslSS47w3f0TbQ5dcMMj2huQrAXyep_bfBTddXVjdqHM1fhyIVykDQVtRUn10YrV8v9wBpzFoLpVKVcy0oOimY90ePgPgnBm89yWzOU7JfpUTCz4lbp0pEdrCWbViDa5xky8ER1VYbmOMfzbst9N-OVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7384d8a494.mp4?token=Kq3YUMrYZ0RKWESw15_x8AsFZACnd7iZL3MZpD7M-0FSnExIxR2g6khjexPSjjvZ-DChTzNSlxbhH-9k3jgyN-i5EIqJRTE66k6n3RckOFByn6aFH4wMC6ewOEnr6gtbE5dRPEmesi4Pp2jLIGeHneI3-ZOXzzCGptuEALpl_0jLUzp5jaBJyetkl6Y4koIslSS47w3f0TbQ5dcMMj2huQrAXyep_bfBTddXVjdqHM1fhyIVykDQVtRUn10YrV8v9wBpzFoLpVKVcy0oOimY90ePgPgnBm89yWzOU7JfpUTCz4lbp0pEdrCWbViDa5xky8ER1VYbmOMfzbst9N-OVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر ایرانی وقتی میره رو کار
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84317" target="_blank">📅 13:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84316">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6273e63d25.mp4?token=LZs4PHGq-PeOFOqK5dxpUl6Kj70je6r6piPIzhDaH5dSHiv6nkrSeBjkdBvrKXlz-I1bITQ-zTMt53O3mAQVtRTEBDD6qMq3pv9G1v6-GBZc0_uSS4gTJ381bByHZl3uzBRz3ZytsfHxq9mvYQ_V9KOy5LPnehq-p3d31I_2pBHN-gQ3COz7VuTjlv8zNzL4UlZ30oAJDNnMz--TNb9Y6Hr9MhqlA133CrUWAhvPPDrMXIze4JPGXRnb3LfaevCi4gk9zfDkBv_VUu7uRROsXtxFFr4PDHSUFf-_J5OiXu6JhKgErwZOyuJDD3FedLk9QfMDYDrxwuZsRDoXGPeutg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6273e63d25.mp4?token=LZs4PHGq-PeOFOqK5dxpUl6Kj70je6r6piPIzhDaH5dSHiv6nkrSeBjkdBvrKXlz-I1bITQ-zTMt53O3mAQVtRTEBDD6qMq3pv9G1v6-GBZc0_uSS4gTJ381bByHZl3uzBRz3ZytsfHxq9mvYQ_V9KOy5LPnehq-p3d31I_2pBHN-gQ3COz7VuTjlv8zNzL4UlZ30oAJDNnMz--TNb9Y6Hr9MhqlA133CrUWAhvPPDrMXIze4JPGXRnb3LfaevCi4gk9zfDkBv_VUu7uRROsXtxFFr4PDHSUFf-_J5OiXu6JhKgErwZOyuJDD3FedLk9QfMDYDrxwuZsRDoXGPeutg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقریبا هروز تو شهر های مرزی درگیری مسلحانه شکل میگیره و سپاه اینطوری یه خونه تیمی رو با rpg ترکوند.
امروز تو درگیری ها حداقل ۵ نیروی قدس-فاطمیون کشته شدن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84316" target="_blank">📅 12:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84315">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e0832652.mp4?token=NlJv2UlaKQM-T2RvWRaU3N_erZXP4YiZia1onmMMyCCbPkKBrGouElL_-dA2W3U6rORh3g_Z5lFKZNIPA-cJS_4CdUMwYDRzYZFvOxJO2n6upd2dmvJrBVu6cmw95fOAVWNphwqrVay5qsKBhbRzMYawQHRcqqtmxZg-cFGyXtH5oPPfNFXEdAD-oW__JghgGr9iXi0mj5_Q8woyV9GKr6wvsfYWH0zwrVoD11R5BjPQcPdXZQA_pZ7YfyHdqc2LAi6NN6wguEAmbe4wzIj4iUTP67KP44XaWzzUqFrKMYQ3dsiU0yzQ12pSsuOPz27j-tiv-KibtuOwy3jNqTehDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e0832652.mp4?token=NlJv2UlaKQM-T2RvWRaU3N_erZXP4YiZia1onmMMyCCbPkKBrGouElL_-dA2W3U6rORh3g_Z5lFKZNIPA-cJS_4CdUMwYDRzYZFvOxJO2n6upd2dmvJrBVu6cmw95fOAVWNphwqrVay5qsKBhbRzMYawQHRcqqtmxZg-cFGyXtH5oPPfNFXEdAD-oW__JghgGr9iXi0mj5_Q8woyV9GKr6wvsfYWH0zwrVoD11R5BjPQcPdXZQA_pZ7YfyHdqc2LAi6NN6wguEAmbe4wzIj4iUTP67KP44XaWzzUqFrKMYQ3dsiU0yzQ12pSsuOPz27j-tiv-KibtuOwy3jNqTehDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پورعلی : مجتبی خامنه ای شبا به صورت ناشناس تو تجمعات شرکت میکنه. دوشب قبل نیم ساعت اینجا بود.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84315" target="_blank">📅 11:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84314">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=OGcLmrPtf2Bvl61GHGTj4iPquEWj9XjOAkkotQ5f2GxOag99Cu9b0X05TJrQd0MnYHKZ94MvCFr8MWHHZj7FE-AIJR6Lj-3aaAJme9DnCtZtsqKjdwtMmDZjtFdCda8Q5ak6NCcWi5bQP7NoILg6kR5YUiZpEywTAnvSQnyPa5oeAuqg1SfsIhwIkS2pkdw2y7AtIK1sXv61JixC-LZ6SDjdLDFwbUFSvIlG_W-z3qh8Bxf0zs79ScFIHy386XEpLlZG-LIvH8p590MFCi3-N770zg2sr-bfc9wtjsciVqdXPF3Xo4ECB9sum-Zyhaf9zWx9RYp9PUKSQnePJvFJ0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=OGcLmrPtf2Bvl61GHGTj4iPquEWj9XjOAkkotQ5f2GxOag99Cu9b0X05TJrQd0MnYHKZ94MvCFr8MWHHZj7FE-AIJR6Lj-3aaAJme9DnCtZtsqKjdwtMmDZjtFdCda8Q5ak6NCcWi5bQP7NoILg6kR5YUiZpEywTAnvSQnyPa5oeAuqg1SfsIhwIkS2pkdw2y7AtIK1sXv61JixC-LZ6SDjdLDFwbUFSvIlG_W-z3qh8Bxf0zs79ScFIHy386XEpLlZG-LIvH8p590MFCi3-N770zg2sr-bfc9wtjsciVqdXPF3Xo4ECB9sum-Zyhaf9zWx9RYp9PUKSQnePJvFJ0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84314" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84313">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84313" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84312">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyL-5L34TKX0RS0x237ybUzxsTof8WcXclIxJaHvX9VKv8VhM-DMsuV_yEvF1odielaGEypnNjBPywyDaTqfG75Av_eaHudnQx42y2sb1CmdUc08jmWktWKIlYS_B3r7R1F4ul3LeftQw4pt__qShEoyOzaIInCM-ELF6DI59SKSNoNO42wi2D3AAvvOXYmut-4Hvl9iOpLBHQiwLF0LAL5M5NuQZQK5zzMpAZ-PAKxIzJXH8-mDJuH98e9uKEiL8Iothf8MZ55nYlSPxiH3tcLN40fpC1Fkn05TkbjmMkqA4N6baJeVHPNtotCvnp6QWMj3T89aToGkm8SyIBLdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - ایتالیا
⏰
ساعت ۲۲:۱۵
🌎
📲
لهستان - رومانی
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R10
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://ewreioxko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84312" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84311">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=Z5U93tLlzqwiCrrmYXj7mED035c7P3CfJz4c-AM_002QqXV2RksCpOBPsx3RDPzefySLql3Igml0JY6fRrosQ9aKPt4IMLygjavdMKkVYbECx2Xk51eQjPOGYejTHVxB6LnAvk1BBCj9f-Am_AAQkRRxeIg5A4NWEytdDvaek2LuYThQ7RO7ZdP8TTeF_0ge62cf13zqF_QTAlz16bWwYXDJjwEV-QPu0XqnMlJgzRLcG1H1oKgchlECCfh27a6nUADm4mw2_tEGdyPRZM75wP2-dtYhVuutpp-Um9Ja3F1VRIC5Bv93mFFNT4qP8QN8ieHpHozYatKSG8w1qF6CSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea0a9e79fa.mp4?token=Z5U93tLlzqwiCrrmYXj7mED035c7P3CfJz4c-AM_002QqXV2RksCpOBPsx3RDPzefySLql3Igml0JY6fRrosQ9aKPt4IMLygjavdMKkVYbECx2Xk51eQjPOGYejTHVxB6LnAvk1BBCj9f-Am_AAQkRRxeIg5A4NWEytdDvaek2LuYThQ7RO7ZdP8TTeF_0ge62cf13zqF_QTAlz16bWwYXDJjwEV-QPu0XqnMlJgzRLcG1H1oKgchlECCfh27a6nUADm4mw2_tEGdyPRZM75wP2-dtYhVuutpp-Um9Ja3F1VRIC5Bv93mFFNT4qP8QN8ieHpHozYatKSG8w1qF6CSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رپرای جدید تا حالا واسه زلزله های مخرب تاریخ مملکت خوندن؟ نه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84311" target="_blank">📅 09:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84310">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=YrKhOHSfdARpGaDgnMkuJW5RnZkELWFl55p01VIdmjVz3ks4FLhkK2a4WYuUUog5WSEveIV7jvCDhQyRUxXLEeA-Em31VrwpujVd6Cfl7qIpoOF9w4PpCUg9WnYKI3eOvwnB0eKy7wkoe5eyepOuc5oifXXI-dOcdu51XI1H-mv46n8YO0O3hyYaEqLccPCGOTC3I3fHy_oAz80BtQcG2pSatrXJg7MRPaI0xQFWikm7DHAcJaoGARmHf-ozrFyNrF-sud8arYl4oIr2vuXg64AJcR7XgZS1pjzLlW938ciZ4yh834E7Cglvg15NegdcH2pR2CH-nz0jMUPJGNfmpFguwbjG-DqVMwqn3CViQIOsH6xxijwJE0YO-zJwXya3r4QK8FButjUUC9I4mD_qmrUYHMuDtZTwDIqje-Jop_U4uk1ensbGHeeqwGpeH1asycZKRFBXeeFAlIN-EBpveKhjYCViP_qnbUabXwJoUYqXxfdln7KPidBrDrUpyjw156q5gSX8b4GAFP-mxIBsmZ9mP8erTPoEWtp42VLMUeMc4FaGPsPzPCLmSm26dkMOPBztyNyYXJIF1yDW40PyxDV-xbIyrCrSjbkMgyPGiAxfRKb1Et_-ORXy2PJY1jAGxdRY8czx2h0C5CdLQiyfY7O3SvJLQHV3GJRUzsDzu7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e286f8be43.mp4?token=YrKhOHSfdARpGaDgnMkuJW5RnZkELWFl55p01VIdmjVz3ks4FLhkK2a4WYuUUog5WSEveIV7jvCDhQyRUxXLEeA-Em31VrwpujVd6Cfl7qIpoOF9w4PpCUg9WnYKI3eOvwnB0eKy7wkoe5eyepOuc5oifXXI-dOcdu51XI1H-mv46n8YO0O3hyYaEqLccPCGOTC3I3fHy_oAz80BtQcG2pSatrXJg7MRPaI0xQFWikm7DHAcJaoGARmHf-ozrFyNrF-sud8arYl4oIr2vuXg64AJcR7XgZS1pjzLlW938ciZ4yh834E7Cglvg15NegdcH2pR2CH-nz0jMUPJGNfmpFguwbjG-DqVMwqn3CViQIOsH6xxijwJE0YO-zJwXya3r4QK8FButjUUC9I4mD_qmrUYHMuDtZTwDIqje-Jop_U4uk1ensbGHeeqwGpeH1asycZKRFBXeeFAlIN-EBpveKhjYCViP_qnbUabXwJoUYqXxfdln7KPidBrDrUpyjw156q5gSX8b4GAFP-mxIBsmZ9mP8erTPoEWtp42VLMUeMc4FaGPsPzPCLmSm26dkMOPBztyNyYXJIF1yDW40PyxDV-xbIyrCrSjbkMgyPGiAxfRKb1Et_-ORXy2PJY1jAGxdRY8czx2h0C5CdLQiyfY7O3SvJLQHV3GJRUzsDzu7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا لحظه آخر منتظر بودم بزنن زیر خنده بگن جدی این کصشرا رو میپوشید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84310" target="_blank">📅 09:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84309">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337199248a.mp4?token=QP57prilo6ceNTjOtDntZ0-t60fSfr1FTBi8c8tyiH67pkbz1mjCcq6k-bsNzPXcah9a686eDwFVxoHoRzybMa8MpVNrBxcS-3uP6ubeotle8lm2Aw13iAUmk7TqYYvpZ5vRNRIE7BQlX9B4RECEFzv_SM-9FEfcpLXlmSTqJEvknTkqhR6lwKN1QfgCF1G602qWuV1jKQNXraix3DMSX5gX2aRMAmWFMq2E3KRQekuy0D6w4HDTEwYe1whDP7Q1yuJ6bJ5Y5EChcguZM5pCQUnt7qx4nzeseM4XDlZNcTKYfLpsAtocCfF4MPF7rhHPGWNpuQ_gLz6BK3K5bH3Upg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337199248a.mp4?token=QP57prilo6ceNTjOtDntZ0-t60fSfr1FTBi8c8tyiH67pkbz1mjCcq6k-bsNzPXcah9a686eDwFVxoHoRzybMa8MpVNrBxcS-3uP6ubeotle8lm2Aw13iAUmk7TqYYvpZ5vRNRIE7BQlX9B4RECEFzv_SM-9FEfcpLXlmSTqJEvknTkqhR6lwKN1QfgCF1G602qWuV1jKQNXraix3DMSX5gX2aRMAmWFMq2E3KRQekuy0D6w4HDTEwYe1whDP7Q1yuJ6bJ5Y5EChcguZM5pCQUnt7qx4nzeseM4XDlZNcTKYfLpsAtocCfF4MPF7rhHPGWNpuQ_gLz6BK3K5bH3Upg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمدی شاخر : (شاهکار+فاخر)
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84309" target="_blank">📅 08:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84306">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=N4YLekUfuDofTerwz6R7eq-LHinIeNklox7xhQ4UzlQthcaobOSLFlwIHvZLaz0wy_0bnDWmdqLLWhMDCyDv5VcR4BNcUmb2WTlw26_l9LIv_EbwUwr9JJ_u9lZoaW1FkRanhLiDn9QmTpQrEAVqfg8K9VClEOXehj0MAUqY6pGthSjet2kMD-9eSHs8otySH2394O1Y3t1kAtWuUQfuLoR7sIywFzZTTHnqRGvkNc2ImmRKu1U76KgLsPFoDolpRpINexiZXVm3PapzUtI5zCGfnNnU5roq8k7Fq7OAdJiBlgAnddSjlvcBxEEHI_1MKvT27z7v__ffAIS6smqP9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90438c76b.mp4?token=N4YLekUfuDofTerwz6R7eq-LHinIeNklox7xhQ4UzlQthcaobOSLFlwIHvZLaz0wy_0bnDWmdqLLWhMDCyDv5VcR4BNcUmb2WTlw26_l9LIv_EbwUwr9JJ_u9lZoaW1FkRanhLiDn9QmTpQrEAVqfg8K9VClEOXehj0MAUqY6pGthSjet2kMD-9eSHs8otySH2394O1Y3t1kAtWuUQfuLoR7sIywFzZTTHnqRGvkNc2ImmRKu1U76KgLsPFoDolpRpINexiZXVm3PapzUtI5zCGfnNnU5roq8k7Fq7OAdJiBlgAnddSjlvcBxEEHI_1MKvT27z7v__ffAIS6smqP9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84306" target="_blank">📅 00:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84305">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=Aks7tEGINXvGswGM6f4Mqc0SNNyfWHgGarjamJDZuv9CpnvJXoZ3IKoqcD85VfyNuJlHbooh1nwtfQzmC-BQbF38Rfh7xB6eJBhYP1y2vEYVxB8jUgZsWN4Is65wqtpIus2UXU4PGRQLanRJDqDAeS9C6QIYa052MX6oTkFZerFcIwPgX6HlOU49MMTNGfdpadkJQxygwt6wYaQEHk4Y68buy-TRvOZTInx2rvUckIpxD9CFGRIAZh4jXTZo6KtZIJLvPM6nf-GFPyKJywfo6s6F-S9pc-WN3vcBHDJp_S9K1S7LJ3HSq-YSTEF6B-mLFozJYTkltGNBFvFs0Va7YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8253be66.mp4?token=Aks7tEGINXvGswGM6f4Mqc0SNNyfWHgGarjamJDZuv9CpnvJXoZ3IKoqcD85VfyNuJlHbooh1nwtfQzmC-BQbF38Rfh7xB6eJBhYP1y2vEYVxB8jUgZsWN4Is65wqtpIus2UXU4PGRQLanRJDqDAeS9C6QIYa052MX6oTkFZerFcIwPgX6HlOU49MMTNGfdpadkJQxygwt6wYaQEHk4Y68buy-TRvOZTInx2rvUckIpxD9CFGRIAZh4jXTZo6KtZIJLvPM6nf-GFPyKJywfo6s6F-S9pc-WN3vcBHDJp_S9K1S7LJ3HSq-YSTEF6B-mLFozJYTkltGNBFvFs0Va7YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84305" target="_blank">📅 00:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84304">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAnPV8yKDA7Rol2KMGW8TaKKhtV1M79vqwv6DPCVVFiPXG4CmCXVe48zzbB_m3dwxikIE5dTdLf00HjEFbOnA4niUqgrFfHDTtIPU8f_UX-aoSVntpEzj54cQbeZ0QOGVOeayPUzX45-1Vw6Nx1MIi5Jy_HwSTywy8oF8cu1im9UDBlgAmxEbVykhukVJHR5x7QIcBdn4v11JO08hoZNC5lkW8AYlHuJwxLtj3FYBiQkLp_kWO-gxUNa-M69AiRpqu0r23lBUekciORpd7tmevfvgfj3y7zlFsI8GgHOino5ajA9TRZx1plCkstod0kEBE8Jp7F0pOQ2Y_Ge55Lk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا دیدید بدون رونالدو هیچی نیستید؟ رونالدو بود دفاع میکرد دوتا نخورید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84304" target="_blank">📅 00:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84302">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دقایقی پیش وزارت خزانه‌داری آمریکا شرکت های ایران‌خودرو، ایران‌خودرو دیزل، سایپا، پارس‌خودرو، زامیاد، هپکو، راه‌آهن ملی ایران و شرکت قطارهای مسافری رجا را در فهرست تحریم های سراسری خود قرار داد و اعلام کرد بیش از 30 درصد درآمد صادراتی ایران را هدف قرار داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84302" target="_blank">📅 22:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84298">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43faf33322.mp4?token=oYKUVaFkHoJ8zY25qmPSr3NXcy-Gp8hLkXQWV_xUslJAV9cVCi0z1B2S24pMe7kinZQxikT_XFRmSWKOKblFsZCmM3VxNzfVxf7IKRFKqnHhoJb1TPmqxwzQGCALpeDR_lezcjzsR6fn0l31LDuabLWh8jaOLYVC4t77SOJLLka8wU-C0H7XKponZg52XfvbFG4ShIalDailuHmWqebQ4v177-qhcuqA6NB9uittWGcDwlz4qS6KXff0nR5G1hYmMvzUnaBmCF0U7l43XVdRq_DWhetULFr0Q9MDFVIHU-Gdh9Zxsc23gJd67UmjsN_tevipcPUpOf-F7wYKrJ8n-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43faf33322.mp4?token=oYKUVaFkHoJ8zY25qmPSr3NXcy-Gp8hLkXQWV_xUslJAV9cVCi0z1B2S24pMe7kinZQxikT_XFRmSWKOKblFsZCmM3VxNzfVxf7IKRFKqnHhoJb1TPmqxwzQGCALpeDR_lezcjzsR6fn0l31LDuabLWh8jaOLYVC4t77SOJLLka8wU-C0H7XKponZg52XfvbFG4ShIalDailuHmWqebQ4v177-qhcuqA6NB9uittWGcDwlz4qS6KXff0nR5G1hYmMvzUnaBmCF0U7l43XVdRq_DWhetULFr0Q9MDFVIHU-Gdh9Zxsc23gJd67UmjsN_tevipcPUpOf-F7wYKrJ8n-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید میلی گلد بعد از حواشی و شکایت های متعدد مردم با کپشن: این طلا، بخشی از طلای میلی است که خارج شده و حالا با آن، تسویه کاربران در حال انجام است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84298" target="_blank">📅 21:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84297">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">لیائو کصکشو تا ۱۰۰ سال پیش ۷ دلار میخریدن الان شاخ شده شماره ۷ رونالدو رو میپوشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84297" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84295">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIxeuI-ULNs2Xgo2noIeBdIIiuLD5bE0_GcMK3g_RUFt96GXzlclW1t-eEae1JLhpseq8ICjC__oTm2txAWUkm2_A7GvHH2blyDXI63zN9L9xy7uJvl6vGqg-AErkOE-cZrs4MCPc_RD2uPxD8kjBhWBV2mhMxXmTS8tJdIfdXIC52UPeEp3uxfjqaTUm0H22sQ6xUnZq27YT0VXf-0L6sp6NavyH3GPDHspGxI87hG4MwS4lQ14bDA7nbfxBBCab6UOScYdlzyPTeKHxupVIJch1nwhsoPb7OARNB-ng9diXiYjC9nvW-nfXF5OEpwfn-NQlGrSt0DG27aIIenRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا جای این کصشرا یه شیر چای تریاک نمیزنن این شرکتا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84295" target="_blank">📅 21:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84294">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پوتین رسما ناتو رو به حمله اتمی تهدید کرد، ورژن ۲۰۲۷ کره زمین قراره هیجان انگیز تر باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84294" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84293">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پوتین: کسمادر هر کی که به ما حمله کنه نقض هم نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84293" target="_blank">📅 20:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84292">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مهدی چند ماه اینده این ناوی که زدن چند میلیارد دلاره
یک مقام آمریکایی به الجزیره: تا پایان نوامبر آینده، ۳ ناو هواپیمابر و دو گروه آبی‌خاکی در اطراف ایران مستقر میشن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84292" target="_blank">📅 20:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84291">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝖕𝖆𝖐𝖍𝖆𝖜</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYFXfTSr0JGF2J83lW4pAzFf9vj3d6c5XKqA-niG3xzxTKVLMEKpEWTdvhcSTd-K0AjGqZ0z7qALsP8na2kmXzblH7DSNAeQQNuus8ZvG2GrdCL0AsGK2xv4tfz3dHI8Ma5ZG2zqK429KMjs-yYrPbll4peuqiBRS2vLK5yxG6C3H7KZleoxE29j7ZEZdw2NUG0qLTxMZOUQSSyFhm19rg8QFF7Swa_X5jOBGungC_HWJMyTIMStuAFcTQEsb3WDUqcrg5T_VAUFpyJVBYr6qdjSuKLABJCu7HiWTM9WpdOWkHNvjzY5xRpCVRiPFALUcHMzBgQS45QOyI-OViSg6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84291" target="_blank">📅 19:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84290">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZemjE5RhoTzKGSsynaV2bv8GSN_FZSx4zWm29ZjVqCbvlOofpBgFJcTUHC-nhWGrmPBA6n8bcYo3WUmPiUzj-G-NxC-qIN4YiLabNlrvEwtFYmREywX-py8NwUD7B832OnEt6fNWXwxpDnKakbXw2Ezdt5on8Y4V64UsiXKs1qgvosQkc29gInc2flkfbjtQdosNzWH67ZbtK4szZYRgnT0Fq1RGtneaXeSHkhLoiYvEO_x6qmgydyOTXenL6LHQprY97_RMvdIX4kMDbXGF2puuRaioEuZqKZnozVLqaJdUbYzQ57o7XT06IaVI0u3i-SLpVyYPxpMqF9uX9uV1MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این فکر کردید امیرمحمد هرچی دلش بخواد میتونه بخوره بدون این که نگران چاق شدنش باشه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84290" target="_blank">📅 19:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84287">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MF5l-Zgsws2WJ4f5dZGGlm6hLS0jp-ZO4agCVxos2y8YXeev2lesKly529VI9tJOHBEu5Fw1mf0owy7-X22ScdhEEpR7BnTwc05KRvvI-kIpIvDFXrhcqGmRg50MwQN9MSqDivt0G5jcFbedz2vVLG4tIkt5XUc_tiUAxj0LUS3HHDgMI6-BvRwRySnNSp1dfQ2pN3aHea9FVyo3eqOD6EnCoStdtOOjK_ifG57q5u6HnMSn1CAUrFCe35Hy7NzDz5ivOPeMiBYuH1uB4ef3Sj75SktUgCAtXBqjH3eWmAQ1fnUWxmDIsarHvDGF6J9dT3vEVbAKEyfWVTrhLOxuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJQsYaUcs_R_ezHxC8WRXgsrBL0tiQO-WTGYrsKQujM7lQSn_E1srNZ_tTrl-KfuA0MWaDYPk1T6FndrbLPJfTNjOqqQV7vUk0GQhBFdEy2lU3QU5e4OCRtQ8CJKBPlzQ2T88dNEn56IlnYrdS9K5vuRNjiB5D7N2lDQCNpSUD_N-ljKVLXNMLEG8yj27UB3MA33A5my6S3Mce8ZgZTouc1evhv0zhBGTAiz7bF_0ivThJld2a4BSy1j0nnoy_fOFIJwa60MjTUQI2v1sZ7BcIoSaX3KQkmClmRbpXE8ptrMb1ay1oKyfgaYIIdMkZ65qzTaPpJ4cAS_qvIDgzALoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kinYDUTpWfAPiYOPQa-7Ty9PGpp1OdP7jAic4S4RsQ5mwRmmUTJJJG-pXHbBtEix9CD_gx-KpmZIbOyAOJqpfjDzHVToTbssPRR_62b2S_kKpbkghe5z1x7pYl_8808lPCinJkzBcQvZr2qLET2EbdpFOnUakVTBwYrQ_JZhS0Q5yQ-1hyEwRcCn5Ec7S1j3ITFeA8hyHKlLsvas3P5eNuNhiGjbVMTsPjWJO7wB57vprkTJw-075U1H4-C2gVNfxLO_apOqLu9QdbljGxXceG1366u4Z7qejcd_zwIetwHF-3sfa7ckmSeAc0ysH83Ru6mgbWlCL1Y97hUukKRntg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ریری یه جزیره رفته، ۹۲۹۱۹۹۱ تا ازش پست گذاشته اینستاگرامش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84287" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84286">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84286" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84286" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84285">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCpKI5A4fxKNDO-cyeRBm953ceS1uoXkvUZTVqhDJSoRs1VVWKefE9XEQXVbj-11KwS1hb4uhDjG0B0YVxGyJxaKDZ0ZdBqLUniVrRpT8nwvU-ghJs2y-sdQkymO-Yy47RHyKf9qCPyBMqUtHRV3Moaw7dLcwQwqRS990hUIv5kd_OGJU91awfrnXtfubY7_SapggCAoRcI1v97SyGIVKIc9o7WvnyU2mpoY9IPhpPSV_MfXxzRJh_pkvYkA2Z83FLpFWdNYZYvE6mg2mMULz-esUnKQvaYsnnqFLbuaEhzEKzKZdSVSCCMiu4i4LPqRwi-IpZGBMkL61GHm0B1Ohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
اولیتت برای انتخاب سایت چیه
❓
امنیت مالی مهم ترین چیزیه که یه سایت پیشبینی باید داشته باشه
⚡️
ریتزوبت با انواع  درگاه های شارژ و‌ در گاه مخصوص و اختصاصی کارت به کارت امنیت مالی رو به کاربراش عرضه میکنه
⚡️
از همه‌مهم‌تر واریز و برداشت در ریتزوبت کاملا خودکار و اتوماتیک انجام میشه تمام پرداخت جوایز زیر 15 دقیقه س
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g9
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84285" target="_blank">📅 18:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84284">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ناو هواپیمابر تئودور روزولت آمریکا هم پس از نهایی شدن مراحل آماده‌سازی راهی خاورمیانه شد تا نشون بده دکتر عراقچی حتی تو نیویورک هم با تعهد کاری و تکنیکال عمل می‌کنه.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84284" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84282">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جدی باورم نمیشه یسری آدم هستن که موزیکای قدیمی گوش نمیدن و پاپ جدید یا رپ گوش میدن فقط.
فک کن حس فاز گرفتن با موزیکای سیاوش قمیشی رو درک نکنی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84282" target="_blank">📅 17:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84281">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترک جدید ویناک به نام "سرت میاد" منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84281" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84280">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pS5ccnHNvYoeT7qUz6n-WIfoCK4-6LN34xNVNL1jUqlNZgXvadYu5y4oPSDQxxVzKHMh5ubGBJGBhgZ0Q2Gr6nSRkw2sXaMHgF5FjxjFEftSt-1JiWasO-Pdnltwk-S7rBbAu2-E1an0pJk0RU1541RCYg5Nlx5JVXyNb1PVol1QYJD9lpeaU59PsIHS2b2ZpMVPKFhOf-bABH8lB9sPd1dXqZzuiPDTemZWGnJALO-I2fsrIcWBNyI-317nTSfx8AvnPC0ua23kEJWUFO9hbUamLJmw8pZpS26SPwEFxdJoTxlAkpFvSMbCHQfseFuubmo2OmDnthHG7kbZKMRAvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "سرت میاد" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84280" target="_blank">📅 17:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84279">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcRyIODAiw7N72lF1HxEONQ4gYb2LYuvpskSPpALUhCCfcWJIS6wYn1mpwwxBSagIjah3ALHrn5_7cWIF-QMxp5RbiuqOYLG0BPdK-AifD6tbFsCo1fXvDM4khqU_1exuKQLWYzUB0NTBQ03Byb8yUg3ZeFNJ_nhnh7cvqGQ6W5KYFB6CUSkWHH359yvBccu-WB-045HPSFeBLvztzmP0GnsRl54apPrCVmGkOO-44VUbD2F3t-4A15zEDL_d0KFcgcbTQiNHazjqIfWm7ZdePVyMGKhlf6bnwSpB3NlqEArCX5LyEqb2kggw0KOEBo68byKlsvQT8MWCdH0sBnK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی انقد شاهکار شوخی کردی که مردم با شماره ناشناس زنگ میزنن ازت تشکر کنن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84279" target="_blank">📅 17:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84277">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ph_FxaUTmu_-GLVSws9NnPr-t0tW1GfeCO2aLoEhNuLZMK_ygGDN4XAb69ZDmad94-5PnRNrUpwYNBL_V_Im6pUwfmSHBIU6yT6YBvV6DHlhTOp0DERzILKaexgtRaxCKRi7BZ2myXj0yD3iujQDIrWC9I14tpspH0kj7W9dn3OlgjzTdZCJdz28OcPQmDIyWGygpkB4EUymN_0_YUzYkX4hhq85c4bF0MzG6kPsGbyfdCg5PvBGIRHKX5bQJi14mlrl-12f66pc91Nj4HB0i85O1bwcj4X0PMOwxfSLdscOueD-ydPPQx1Dv2zsTzo_dT72C2VQb7kEsAObNq1KZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=XSQEeo1fTgYXji3njPJ9QzC-hFo5q22W9GaLDCIcy7Lur-PJaYwUi3Xk6pyz7m0lj8Cq1wcIMIMALVxKST_wid6zhQ8FdiJd8DzvRukswGLNp55DrPJ8kTSMsyFHh1-QYCAmPP2MEVqqh8gtolWdxCJL1sm5fPFpQ9Esp2guw7u1N2f6GvHMMgn2B0cYVvMFe6ZbBMdWMZdq9oV74vmg_sHtJI7ora0oo6-aDvuW2akp-KQVY6oAjJH9IXJCSrmghrGR7XmE8h6_U2z9Kl49st8fcz05HZ5nkH0SXeZUSQVPmqD5wrAXDbdhafPPDonBuvMTXOFvy12G6z1T7_evsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f25717c9e4.mp4?token=XSQEeo1fTgYXji3njPJ9QzC-hFo5q22W9GaLDCIcy7Lur-PJaYwUi3Xk6pyz7m0lj8Cq1wcIMIMALVxKST_wid6zhQ8FdiJd8DzvRukswGLNp55DrPJ8kTSMsyFHh1-QYCAmPP2MEVqqh8gtolWdxCJL1sm5fPFpQ9Esp2guw7u1N2f6GvHMMgn2B0cYVvMFe6ZbBMdWMZdq9oV74vmg_sHtJI7ora0oo6-aDvuW2akp-KQVY6oAjJH9IXJCSrmghrGR7XmE8h6_U2z9Kl49st8fcz05HZ5nkH0SXeZUSQVPmqD5wrAXDbdhafPPDonBuvMTXOFvy12G6z1T7_evsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید جان ناموسا تو یکی دیگه بیا برو کونتو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84277" target="_blank">📅 16:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84276">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84276" target="_blank">📅 16:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84275">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">واقعا فید کردن موها یه کلک مارکتینگی بود که آرایشگرا پیاده کردن، مجبوری هر هفته بری پول بدی بهشون وگرنه شبیه جنگلیا میشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84275" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84274">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کصکشا انقد به پر و پای بلو بانک نپیچید و نگید بزودی اونم پول مردم رو میدزده، یهو عصبی میشن فیلمای ثبت ناممون رو پخش میکنن بدبخت میشیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84274" target="_blank">📅 14:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84273">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrie0zkloKSw0coKpI7cTeI62X_h3K6NjH4diuGnlmZKlARR89Yq2OwLCcQtE7X_XXYg7pNdn84vpV76YXNCXI5b-Gdj9lzpuMwMfa9wqcTw_MKqQUtEdHZZyAI0wacrRpmefmGhsu5E5NgRPru7BOlas5pc9v_6FdqvG6uRSeoGNJ0ud1yLDrewJaNrvlzIS1g-5JMAZJH-UOmJKcV242QBF2pYY4skG3s-Myr3Dz3R7UbVRDeaxogwsra-B4XX-s9VS13n_XyixXjiiAwPXBzXwBJnQxQdzldJeMBXyCnZ9g3P65RrUJvnOZuUXZwYbaRweobC2FYpTTt7P2CVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بازی دوستانه دیروز کونیا اسپور و تیم ملی فلسطین بازی رو دقیقه 89:59 متوقف کردن و گفتن ادامه بازی زمانی برگزار میشه که فلسطین آزاد بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84273" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84272">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=btULWSzFhyINl8QVh3sFUIW1PK9M6mCo36zBK-J6SxSnK7KFRq162ASrRHeNnep3PNLOZgNUgyz8TDeY7-B-kipvslfLQKH-hCRbtkKuQGPWkESLJqqK8DiBcMlSeGvDq8KBwcE8DCi5poBRo2Zqqmt59eTIHmORLCra7FASSoqwQndAAjFZzsZYGLaT4fdvVwLc_DNlQsC-_li8B-YX1LV0Swjc0qn_zF3WGvyJh1CnS2VXsg866CHk6GKlA1a7t1fR76PnHF7PSdd0u-QcwQC6rMuoPS54xs2TNsF_5AcmidMsf5JOtzNnVp5N6Xw7AaFkkfIQcbYqyh1tqQmEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e053e973a0.mp4?token=btULWSzFhyINl8QVh3sFUIW1PK9M6mCo36zBK-J6SxSnK7KFRq162ASrRHeNnep3PNLOZgNUgyz8TDeY7-B-kipvslfLQKH-hCRbtkKuQGPWkESLJqqK8DiBcMlSeGvDq8KBwcE8DCi5poBRo2Zqqmt59eTIHmORLCra7FASSoqwQndAAjFZzsZYGLaT4fdvVwLc_DNlQsC-_li8B-YX1LV0Swjc0qn_zF3WGvyJh1CnS2VXsg866CHk6GKlA1a7t1fR76PnHF7PSdd0u-QcwQC6rMuoPS54xs2TNsF_5AcmidMsf5JOtzNnVp5N6Xw7AaFkkfIQcbYqyh1tqQmEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آ
مریکای جنایتکار با انتشار این کلیپ و نحوه شناسایی و منفجر کردن آدما با پهپاد، ایران رو به جنگ زمینی تهدید کرد
.
تو این کلیپ سربازای آمریکایی وارد خاک ایران میشن، و دو نفرو با پهپاد میکشن!
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84272" target="_blank">📅 12:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84271">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مارکو روبیو، دیشب هیئت ایرانی که احتمالا برای مذاکره مونده بودن تو آمریکا رو از خاک این کشور اخراج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84271" target="_blank">📅 12:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84270">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">محسن رضایی: قبل از اینکه انتقام آقا را بگیرم شهید نمیشوم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84270" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84269">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
خبرنگار حوادث : دیشب تو تهران یه مرد جوون بخاطر اینکه زنش قصد داشته ازش طلاق بگیره با یه گالن بنزین وارد پاگرد طبقه اول شده و آتیش بپا کرده
تو این اتیش سوزی، خودش و خانمش و مادر زنش کشته شدن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84269" target="_blank">📅 11:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84268">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxwEpDC3g771YTxkyl_V41Dky7IbOgeua3kuQEumUHcLlf6Sbf64WJ4DryyClbV6cd_Y-FXlIWuNTexVWKSGWCCSFQ3vycnuquP2rz3a1g3k37spLXH9D7wdypXezAGdxtfVHxjArm7jFJXmjgj4UUE5mY8davlffPVTTUGgV3MC2lrBn5GM9p8QDXqS9EsQVk9mx1jr-SiIBRnWNadS4IBxyFh8mkvOLZm1Q2cfjyw-JpNaEb3P4KWTrYDdMevsYakO-K-LYkDVUqvi5M1xXotdM5suhps81lDs8BCJomFEybbOOPT2Btv5pH41iBSyBOk6iPrEsz3okZB6yNH4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط بوراک میتونه نجاتش بده
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84268" target="_blank">📅 10:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84264">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZjS9cm89hqjuijBf021QQOaTGW2dtQbnQR9J0o5p446DhDBszU7z_jI9pKnNH9jOxoy3oWILQ5oKYh3E1GGhhPy7NWb7dSOl1Y69JvdD6zXj-FOxuPgZO6wApR7-Vs9k84JFrEN0FwIn2dPjpfhiPaIQhsJmUjURab8hNqp68XgiKfw465QNvMHotd1Gj8OTSFQTOdhXKpo0Ww0o1tSYLRXzufxno47RHvacYWb9MQmclq6OmkHrwHpK8vLIn16xW5NA3kpp-SVPDQOAOtHDx8iKYl-nUsjn8bOCOhGFKb2ggObseM5IFaJAPH3dz_JblVTQMtjhvdGXdFPZfMN8ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WesATrYgERvsFVHoSchVu1QOjWE3txQDBdJlYlrThQZqKEgYTuwwUv_0aDqLrnBtChi0OCIRitpR9G_plHyZrzCnvRtzGGe2fS8zKJ-C2mBqWjm5HQW2rDt5bDeLtMPgP1de3keplv3qloIxKZoU7Hg0SyozdVXk8HrYBGGoz1Y3ajelXlZBJwJruELa__ayXTruRdIQFqH0YK-0gSetfqOuczSHA9DbjA0kRNdxScCyNYUpLPvU9hj4akZ7m-PDLozkEqjiYJLeftn40GiDyZwc51qAwy6gOUNEcecAeIe-GDabIjbv54TdMrStwtwBI97xG5WGlhsHpO1LBpz8ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxrshsMGd5X_QdCcPrh3yZHBSEUp-MtI8TrbuKQR3xwM7trZv2uQNVu3FH7DBnlscTXES2l5Tg1rhlmYldyaJNo8Gia80ICsZWZHrBuW3UBgd0zU8GJ8Bh5LS7yzTht542fvrBMt9W_ROwYgxWBIjjCjRvjNVNUFLHPvq3VU0rsMY_dftYzN8MTdV8X51fmv1omWCf6hhriMXyTZDk_Y33CSMl3Qf2VMQAiqaTi8z6MBQS4zgrx6jYsfu_1jB2ATpvaArHRlF6cFN2rK1YwJKhUzG9-VELizIXrM6XUUbMqNwyq2XSe52XIwOlYFXTBtTc8wFNc4-lrCKBFengrJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mb3A4Pm6fFCC0f-Ieobw0jiTPJ--CowahZ2_8tQ55XWWvCBhv6IqfVp8wtpTffAo_gScbOHuF2CaK1kcpnMtPlCAbKIoa9xAkngt7vkOchN_WPaclMYiAiUHN13IwZvJ1Z_UUdlaht0KuCZcGKy8fxByF8X_hbAz_ON5zj9Mo7pcuFmrxBics_u8R0Em-qT0gc4fLws-LOxDvjkzjn5HOOCMJz-mo03vfJPHJ0xWobK1vG88-y3b58rLMyknnu_cU3Z6B_6TQefNjiDu_Il-MyohoF_-nhflwe6_hlbc-oeTgEE98ubmxDvrBfEVeGhs4hVKMiwocLrWTfmlae-kSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های جدید بوراک
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84264" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84263">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84263" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84263" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84262">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5j45AwC7CoBkJo-YWnX69vAsEM2_zoIKCIosNkyesro4MkGXsNpfivdF1IBsrPxECcJQx-u_cLbB6JP6LVF6QMvRa_IKy3T7Zpiy3K68CI0cy9qXlK0Z45Sif1p7b6d545nYzKWYBg2PSf5D62k1ebBRf3XD67OwYah-PGo_M8nSRcsX6tcKKBIy3jrGlF5Y0pCAzvKIG4xrSZ-eGNue3YrU1IdPExocEjpLQGS7XjOCJMvBnYVrILjHpEhV_4YadzSeOWIzBP4sa_QwS8KNekZ3L8ImEl_cOLsyupKzPxxLGhWmluYXPkf_cWQR5VgJt04pu4WCTjwALEUU0-3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r9
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84262" target="_blank">📅 10:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84261">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در بازگشایی مدارس امسال جای خالی یک نفر شدیداً حس میشد، شهید رییسی اگر زنده بود امروز بعد از انتخاب رشته مشغول به تحصیل در دبیرستان میشد
💔
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84261" target="_blank">📅 08:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84260">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49c29e72a9.mp4?token=WRj8b8s1fmwXChZlSyObsgaQsSBfJA0uZm76TpMdr93Gp7Zl20a0-Mm6ecc6LtzgTdbaNfJNQmTkOFaVwVMly3ir2ejwh8QJ-NgpBK_v6rftJgqmOjzHOxZymFyZLC3ydS9dNSbKvZTwWsumjyqhrE6r4GodoS-SaLSTwU76isKXtk29zUTa1lx0nfoUct_LufB-Kt5qrX0fKdI8F2xGHgH1hcCB0SPQgJPUlDLYOTF92gvHlJnSVDVIXYoRWWAFnGurI90TK84EiDGXzOaXM0W7bm719r0XdHOn0wUm2cAdY5gDuKhSKLdt-JxRoBKwvYsmTOhuBR-mvWZB2OnAXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49c29e72a9.mp4?token=WRj8b8s1fmwXChZlSyObsgaQsSBfJA0uZm76TpMdr93Gp7Zl20a0-Mm6ecc6LtzgTdbaNfJNQmTkOFaVwVMly3ir2ejwh8QJ-NgpBK_v6rftJgqmOjzHOxZymFyZLC3ydS9dNSbKvZTwWsumjyqhrE6r4GodoS-SaLSTwU76isKXtk29zUTa1lx0nfoUct_LufB-Kt5qrX0fKdI8F2xGHgH1hcCB0SPQgJPUlDLYOTF92gvHlJnSVDVIXYoRWWAFnGurI90TK84EiDGXzOaXM0W7bm719r0XdHOn0wUm2cAdY5gDuKhSKLdt-JxRoBKwvYsmTOhuBR-mvWZB2OnAXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده امارات در سازمان ملل: «تنب بزرگ، تنب کوچک و ابوموسی، جزایری هستند که بخشی از امارات محسوب می‌شوند و تحت اشغال ایران قرار دارند»
پ‌ن: بیا برو کونتو بده ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84260" target="_blank">📅 01:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84259">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: میخایم بزنیم ،بزودی تصمیم میگیریم
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84259" target="_blank">📅 00:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85208a1d9e.mp4?token=NbW0ypTVKbdeQbBgfxbacU7ADFw16s4moJmOTb3AbAY_wtd6qKQlEXVciuC-02BuapZNQjwF5kHi_-QQC5Tg3SxZo2DQ_uPN105MH8xo36xEQG91Mw_DlzoDKJ_T64miQ1mDmBzD2Qkd2b1Uq5NEhXzyUexhYP5wWg25whgUOyvk3FEqTy91d6b37SIoRC2ASHCelKF5TGx5iyFO65K35PUgeDrwqCLTEZ3_uvg04cQtfBmdd9xB3fcgm4OiCB-qWUidFl6ljBL1AjDl0v_Lg2m-UbiQ5PtLJNIgrDTbe7yvkcx7h9iozvh-0742TzID7DUJnDgxfmC0x2WNCBiCNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85208a1d9e.mp4?token=NbW0ypTVKbdeQbBgfxbacU7ADFw16s4moJmOTb3AbAY_wtd6qKQlEXVciuC-02BuapZNQjwF5kHi_-QQC5Tg3SxZo2DQ_uPN105MH8xo36xEQG91Mw_DlzoDKJ_T64miQ1mDmBzD2Qkd2b1Uq5NEhXzyUexhYP5wWg25whgUOyvk3FEqTy91d6b37SIoRC2ASHCelKF5TGx5iyFO65K35PUgeDrwqCLTEZ3_uvg04cQtfBmdd9xB3fcgm4OiCB-qWUidFl6ljBL1AjDl0v_Lg2m-UbiQ5PtLJNIgrDTbe7yvkcx7h9iozvh-0742TzID7DUJnDgxfmC0x2WNCBiCNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یجور هرکی که فکرشو بکنی خایمال داره فک کنم اگه استالین هم زنده بود خایمال داشت، یسری بودن که میگفتن قضاوتش نکنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84257" target="_blank">📅 00:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84256">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وقتی از زندگی خسته شدید به این فکر کنید یسری هستن که بصورت جدی موزیکی که توش میگه "بِچه ارچره من بربر" گوش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84256" target="_blank">📅 23:36 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84255">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9caab26da7.mp4?token=gFCA8zCgOwZvimrIGCU4Ux136N8rjc-jQnrcX6qJAukwwDXdavpka90Bsf2z_5ybgP-re2pLN97FXhIifmglvtg0aMHP3E2uOTBei10yJH0W4C4tMxe5JTOjFXRL0r86DOcRNjjpyIEzk9SgOCK4S0zL3eMeEGq-SJgQcyJBJ0unl5evzAEN64CdJvSvIJZnAB6ZgckUkQKXU5kbN5uYLfzQcfy6ZKmwGJg1JGoaVgxSBoFzJELkBQZXdt45rCUETXJOCB_PQveC8MkiQI6__7QpIL_ASe0Zq-KSZK9NXrpH4OanQxllo-ANvz9eO0kPL7Yjnb_4OUIn0gdsw24zYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9caab26da7.mp4?token=gFCA8zCgOwZvimrIGCU4Ux136N8rjc-jQnrcX6qJAukwwDXdavpka90Bsf2z_5ybgP-re2pLN97FXhIifmglvtg0aMHP3E2uOTBei10yJH0W4C4tMxe5JTOjFXRL0r86DOcRNjjpyIEzk9SgOCK4S0zL3eMeEGq-SJgQcyJBJ0unl5evzAEN64CdJvSvIJZnAB6ZgckUkQKXU5kbN5uYLfzQcfy6ZKmwGJg1JGoaVgxSBoFzJELkBQZXdt45rCUETXJOCB_PQveC8MkiQI6__7QpIL_ASe0Zq-KSZK9NXrpH4OanQxllo-ANvz9eO0kPL7Yjnb_4OUIn0gdsw24zYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این رفتار ها در شان مردمی که چهارم جهان هستن نیست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84255" target="_blank">📅 23:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84254">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کاش شرکتی جز دلپذیر سس فرانسوی تولید نکنه، خر میشم میخرم بعد پشیمون میشم</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84254" target="_blank">📅 22:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84253">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPDA2ja5-k8XTXtIWexKuAR7EmqqgPLlkgrMCHiK5v2X-qhBOlz2ORPCxEADjdFiQffmLIeGjyRCf7OPSJJXXQX2UGKAI1fovIffk-Yd1AJ8m7LPq9WBP1XrChEObdpXxvrhIq7HBCFnHVUxB6RVnNp23IIDO841WXd8DA0jIZDMoI6mmY0uWuZ-0ZSLhWkc6Y_vTS6SEOnYKmDikgU7Ijvwmol6zGYUfhq1KiHRpYFObdn7lzBeqHNogLL8bzVLR5MSMMCJ89yzzMtaOd-oDiYEyD53AmvxNWZB_-Mfq3A3IDivmO3AgQkY3Zf9i-_Mshgy8M6m9X4A4KfkMAt5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین موسوی مگه مجبورت کردن آخه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84253" target="_blank">📅 22:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84252">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شاید همه اینا امتحانه خدا داره رونالدو رو میکنه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84252" target="_blank">📅 22:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84251">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رونالدو رسما خودش اعلام کرد که کمپ تیم ملی پرتغالو ترک کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84251" target="_blank">📅 22:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84250">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رونالدو رسما خودش اعلام کرد که کمپ تیم ملی پرتغالو ترک کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84250" target="_blank">📅 22:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84249">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt2hb0762wt_mBW5uNCP_BRNpxiOEZdbkcYWd8fcv4L5Fz41yvG3KK9UFidrAQvyXqFSiIvjulr33hfyhfwF1wJkShlaSlRATzTFsS8LrtCroMfGGNKqrsL-EzbfkfbItXow0UhhAU6OLop4I_Wl31NnMTMUCveXkHg2bBE1MPsh-mosibZ9gUrcwQqP895PWhWMEDbb5EFQqljFCZ_huRKISCNQd28mdjWk72_bXGCCxjgUb8ULB48PoLPgdRzVz2-C1QQdPtaXp5h0nG1oZrS5NuqtX7BkcpHwe6SfR9fwqo1t33OJqmRklMWi45WSoC-pymTXNXF_SKM3nhDfKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84249" target="_blank">📅 22:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84248">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzdg1JEIhW-4ht5NPQjuDJa3cNhTmn4nL4VxDyHGArMcvGv7_ssqsFoe_FYxX-VQ4FoQsBKoyHfihlNq4evimVv98VU1HdzEzPAJfEVazbXhwpA4npYkI8uW6iPFr27BXv8jS2MQYR91MSAfXY-E_K6hkzMz-B3MDTnauTc-XOF-az41-PLVbU4U-BVKMqVPYTDToiS45uEUavspnLPAtw47ld8g5QZNS2ChUb_UTDDLXIFewAKk-vSoMz-h5xZNoBetvoaYICvpI6r-6LU92Wbtb2DB8y82C0rk5zwaIQHu9SQi3H4YWCAFymnDkCGFV5bv5FaujzWVJ5GTo_H3iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعی که من پذیرش گرفتم با دلار اون موقع شد ۳۰۰ تومن که رفیقمم میخواست بیاد نیومد الان بخواد پذیرش بگیره باید ۲ میلیارد بده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84248" target="_blank">📅 21:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84247">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNZJx9GbY84SZ908Levq2lfIaZfW1YNyfOQdsB6uhulHCOh-27vergDXH4GXJACUIWIKBnM2_7Tw9CTvp1N4lQ2a7L0f2tKEAnBsw8jQUTGriwuZT7yxg3WBawEIN4hl2nLm9wDgocWmCDW4as6WwWJWVlL7qnPjnpwov1wRFQezicv39XwWPNK8iXuuy1F5baFykHw6L10nuKHBK1Ggr-2CaaGZR8se4mCPmeF7SImwSDWJ1SyuAAUtDZXEmuwhFg5GbqDjUwlfKkPggVsVU1igwEybSpqBTNR5VmKkldXOj_8eySoNFU5YAbK-3kGqC6MySEXgmSCIJafIPz6B9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار میخواد بشه 420000 حالا اپلای کن ببینم چاقال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84247" target="_blank">📅 21:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84243">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رونالدو چون تو بازی قبلی بازیش ندادن قهر کرد و از کمپ تیم ملی پرتغال زد بیرون  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84243" target="_blank">📅 21:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84242">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رونالدو چون تو بازی قبلی بازیش ندادن قهر کرد و از کمپ تیم ملی پرتغال زد بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84242" target="_blank">📅 21:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84241">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK_U-79vd15KS40gO8vtXB0SCwit4pWl3W-_mmlNs8DfPUzgQeAiPIHKXPna6qPmDBDkLOsz78uYrSY9ZQGYqY_P5LTYdeWHhXNAZh6yPiejWKHJjnW09quqfKkc_WqNsQF8ZsBYQJ_-Pvg_pjhZ8fCr77O-_yl6ZBQmc1X7Z3Utdr6H52apH3Cc2KEs5_EF4ArME-lfH0t5JyFhhl0UE-zsWTKs7l4GO_ng_AIirstT9aBpXerJuETWNsUfXOjEFgGd1FJ-hPiJX-Ix4A4_BtNxRcUFDmUlLRD2keuWspm1fUqMkpAfhGD4fHzLiJ8CTqAlYQzBY8ejAOyeHFHaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش تا حالا شده تو آینه نگاه کنی و از خودت خجالت بکشی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84241" target="_blank">📅 20:37 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
