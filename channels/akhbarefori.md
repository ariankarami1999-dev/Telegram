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
<img src="https://cdn4.telesco.pe/file/iZsXwPdPZ052qUWAgpQndPbZKpmRboQsNroInN6az79fTNcIErNv3xGA-NW-N5ILa52Cv3B6I8hlnQDQIWJkX_6-3-yipmukXmguPF_4BjDLQPqwhE-L2t-bFo_i1r0vu4ZfAeYNfkbM2BHxiQrDLeGxLovVEndaNI_4XbpN2iMP87p-VOEF59p47tcWvZZf1peejuzab0rIbM9gEw4vAOc2NfgdcyhrYXUd8SmaTwDIBQCUR0ZGmoiWwg8W1AiLnhqDNR2iSD8wGQfkiVZ6rdIfGUC1Lbtef8_EcHUIyowv8DrqF9_UswhrIC-Ogw_Tt6aDIvF9x6-2b5VUGFy53Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 02:17:12</div>
<hr>

<div class="tg-post" id="msg-693846">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=jgI0Vt9yZlqYTNIsIrR6BvQwUSKt4S-SV3fCc0QD2yhR6gfeZ3YS6yKtZne5SWGyB_mUOVT6PrKdxX5a6e8i8a9j7hL9fTn_PNJFK4C0CgStA2SHaD1gf83y34SL7DcCmcY34Qbrlx-PgrEH-WF8kK0ymuu__I6TTnSG-Kb-ptH4ETNiaLdYkaW4fFSVO7jIFaynF-UiA6_0I5tOFBBKHpVaPH_rCNQg_lr9UwuoY6X3J4OcLiZClIbLJRNT9zazzYmxbrpRNFq-ul5LhdSRlalZSGp3d5yFBNKCVIyDgr_3PZipxwwyo4DZ9WOi_sAhWAu-ZAt0J7j5eDzp96chbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=jgI0Vt9yZlqYTNIsIrR6BvQwUSKt4S-SV3fCc0QD2yhR6gfeZ3YS6yKtZne5SWGyB_mUOVT6PrKdxX5a6e8i8a9j7hL9fTn_PNJFK4C0CgStA2SHaD1gf83y34SL7DcCmcY34Qbrlx-PgrEH-WF8kK0ymuu__I6TTnSG-Kb-ptH4ETNiaLdYkaW4fFSVO7jIFaynF-UiA6_0I5tOFBBKHpVaPH_rCNQg_lr9UwuoY6X3J4OcLiZClIbLJRNT9zazzYmxbrpRNFq-ul5LhdSRlalZSGp3d5yFBNKCVIyDgr_3PZipxwwyo4DZ9WOi_sAhWAu-ZAt0J7j5eDzp96chbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🎥
#_این_کلیپ_را_حتما_ببینید
سلام و عرض ادب و احترام
💔
یک بچه نیازمند 2 ماهه ساکن روستا داریم که مبتلا به بیماری هیدروسفالی شده و نیاز به عمل جراحی داره،هزینه عمل جراحی160میلیون میشه ولی هزینه شو ندارن و بچه داره عذاب میکشه‌ و روز به روز سرش بزرگتر میشه و باید هر چه زودتر عمل بشه
😔
😔
🔹️
این بنده های خدا هیچ کس و کاری ندارن،امید شون اول به خدا و بعد به شماست تا کمک کنید،فکر کنید بچه خودتون هست هر چقدر که توانایی شو دارید کمک کنید و بفرستید به دوستان و آشنایان تا کمک کنن،خدا به مال و زندگی شما برکت بده
💳
شماره کارت
#رسمی
بنام قرارگاه شهدای گمنام(کلیک کنید کپی میشه)
5892107050067480
📌
جهت اطلاع و ارتباط با مدیر قرارگاه
@Hoseinfahmide313</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/693846" target="_blank">📅 00:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693845">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knpQVj3Y0l8Yj23n5Skvwdwc5rBJbd0g9tUifIUc16XKMWTgwXUfJ6Tk2WdER2erbC97smmMt8xO0j_dbWuJG8mM_hQ3AYhqND1NpuA1bKepwD75togFCml6Jw15HBwHumBbtH9TFD6VNmJ_BnRtoIV_UQ7DibP9On0lE5qCOd-hjJwez5i_R5TUbMi_XA8mJOLo1IKhlJIluCDgeXouRD21XEtEwtwm4bG7-GLOzWGfv81yubad0kteEOKfrrV_hlhxUMfSvZrxwMLIwtof3qe7HUiSGnVAYK5uadhs8YmBQgyf_QxyqbNi5uKnjXycEVecP_dWZSK_7m6MqXj2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
تخفیف ویژه در فروشگاه لوازم خانگی گناوه
🔥
🔥
😍
اگه قصد خرید لوازم خانگی داری، این فرصت رو از دست نده!
🛍️
انواع:
❄️
یخچال و سایدبای‌ساید
🧺
لباسشویی
🍽️
ظرفشویی
❄️
کولر گازی
🏠
انواع لوازم خانگی کوچک و بزرگ
💥
قیمت‌های استثنایی و تخفیف‌های ویژه
💳
امکان خرید چکی و شرایط ویژه
🚚
ارسال به سراسر کشور تسویه درب منزل
✅
تضمین اصالت کالا
🎁
همراه با اشانتیون و خدمات ویژه
📞
برای استعلام قیمت و ثبت سفارش:
09175959374
@genaveh21
📲
فروشگاه لوازم خانگی گناوه
🔥
خرید مطمئن، قیمت واقعی، ارسال سریع
🔥
لینک کانال
👇
https://t.me/+UwTOb3oQ3sRE8GDP</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/693845" target="_blank">📅 00:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693844">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigikala | دیجی‌کالا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPy2Rfr33RZKWGHzJzxBVyD64vcZEhkCGFhVjb2l6-JAIWdiB_aOII7Zjh18WTBxKxZjhNMBW8w_rmnNQ566UVNvTBqVG8zBw5Ybvf2CTcYmMuTvIFZdDGurB3gDAhNc-LyS7JDPkmC2HwuazUWdVyt206Yc_sHSxdY5Y4PCu7MbtA0CFkuLMRUWwdf72TFlvYjIw5YeHLGscMvDXnxFu-dLiDvioy3TDg4StIIySs35pW_0kDjXJrE38LjjknmaO4xV-ooqwHyxiqgTKffp_HT-D9PXkHmrVSCkm5caWpQjCF5L7JtNI1mTdHCqw_4VpcJtLzu1Ho0aY3DpaNocBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای پاییز آماده شدی؟!
🍂
🛍
هرچیزی که برای
فصل جدید
لازم داری، از استایل پاییزه تا لوازم منزل رو، تو
حراج سر ماه
دیجی‌کالا
با تخفیف
بگیر!!
✨
با امکان
پرداخت
اقساطی
و شانس برنده شدن
آیفون ۱۸!
از لینک پایین با
ارسال رایگان
خرید کن تا هر خریدت، ۲ تا شانس حساب بشه!
👇🏻
👇🏻
خرید از حراج سر ماه دیجی‌کالا
🛍
✨</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/693844" target="_blank">📅 00:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693843">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f129a9c7.mp4?token=kdfxUq8FeYf9xaGXgWrX3tO8EwHrMOcFjBK8RtgQ0STVH1ZkOciqblNt2f67eXrp8XiUwTCK_XvHuWB_qgD6fdmSfgnI4n-a-076FpSF0O-kXL16HcRCmIHYR99RtgYadGH3SoRY16p2naWsCt0vJkcpdj1f01mHBAJQI27SdspQ6oEWBVoUhcLnUec-VB76YqBkkXc-S-FJ-yQLp4ZsUZdKqjTtpXKq7y3z5W97IHCW_xJiUs6gnbWRXmV57Lf-inVE04h-Rh_W0XK6EWq_AOH1uMm1rnkBprtSWVlvfqdVXxnA23hFjxFnENGcTBntd5sG3R5_dm97g2GTw_rGJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f129a9c7.mp4?token=kdfxUq8FeYf9xaGXgWrX3tO8EwHrMOcFjBK8RtgQ0STVH1ZkOciqblNt2f67eXrp8XiUwTCK_XvHuWB_qgD6fdmSfgnI4n-a-076FpSF0O-kXL16HcRCmIHYR99RtgYadGH3SoRY16p2naWsCt0vJkcpdj1f01mHBAJQI27SdspQ6oEWBVoUhcLnUec-VB76YqBkkXc-S-FJ-yQLp4ZsUZdKqjTtpXKq7y3z5W97IHCW_xJiUs6gnbWRXmV57Lf-inVE04h-Rh_W0XK6EWq_AOH1uMm1rnkBprtSWVlvfqdVXxnA23hFjxFnENGcTBntd5sG3R5_dm97g2GTw_rGJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چراغ‌قوه اضطراری چندکاره؛ فقط چراغ‌قوه نیست!
✅
نور LED پرقدرت |
🔋
شارژ USB + پاوربانک |
🧲
مگنت قوی
🔨
چکش شیشه‌شکن |
🔪
تیغ برش کمربند |
🚨
چراغ هشدار
🔥
قیمت ویژه: فقط 1,198,000 تومان!
👇
برای خرید کلیک کنید:
https://memarket24.ir/product/fast/30291/180124/
✨
تخفیف آخر ماه؛ فرصت آخر برای خرید با قیمت بهتر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/693843" target="_blank">📅 00:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693842">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
منابع خبری از حمله نیروهای مسلح یمن به نجران در جنوب عربستان و اضطراب در فرودگاه جده در پی حملات نیروهای یمنی خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/693842" target="_blank">📅 00:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693838">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmZz6krk-nomwg2c34LxlvZtCEpHK3vnFi9EcbO3-MexepxSeXxLeX-fcinxARS_sVj4xZl9V7wsJUOQRbQ7P0hr108mKZVdVqmdmwOzGk8-TD50Ix9SrZ3uWbVniBUsWTO9P4VtNK0w82bUNmodBN5ypOEAIg65lUMpNOH6gf51wO1y2-RKR3-IB0R7yQunGZIGS6KBXofluLQrd1jG119HgA4tCejbOcpShTfAeixQXMJqhx942H23JqWbrdrTGBNx7mas4ffRL779vFfIRIATu82ZhJfbX7QY0wa84q1MdHbSE6DhS28Xs9sAIs-si-CUS0EY93m4MrJWqggFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lB1laMyWDfAxJ8x4aQbh1oTPcu9lUd5AQ6DkoMoIEBcQQPDEtcwvhfV9ff_ZBuelAGgBmklz4PGRG_6K8rmOGop_azbMNEAMu9A9N7tth_wIhyJ9NVlHLbu0EBJzmk4GrpCi6vFELF5K0OXkzRuTWtyYtbrMVH3FqIuwjgtcoTfvuBKE3AGQV9NaIdvFdOxfL0GvrQluVg-8poedILaXUa_h-YxX3Wmsg3qVP4qMvH9mG6lxwKhkUEeuR46OOALkYxryHj2XdikgYZ9gVzOQbnkHoQaH9iTY4Keu49kSPAhAI5r4DJeDaB6KnEmPn7LjjSfA6mF-QTXrG128oIcDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xamfv3_4eyqGdRcoiuzVdlbsMEDZstY6lu6kNVX8EywRdX_Zvo9eAgxz0Mwrm_WCusjIkNrU-N80mKakwwZvzIN_RklPGJHlVeFUx8BhHZGD_xeZHHUggGK2mwz44gggnAg_zb_veaJzU-SRd-BIxRunvE3W4b3yBA0zvnHN2aI2w2zejKqhyvi50LV6diRBd3cgtkPhBdPVXpstoNBxSlU-FqQGNsQXahWUQq2Qci5bDyhgl0ujZVrsdSUeDB33aNkmhFdYWVj-29NA6vQmuKFEj5OjN7EymFooByVb1SFrj0IPGevGTZ7Qz-8J6Mh_WaiRJVc98w-YGPs01It3fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۳ گروه خوراکی که می‌توانند به کاهش سردرد، آرامش اعصاب و حفظ سلامت مغز کمک کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/693838" target="_blank">📅 00:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693837">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
واشنگتن‌پست: پایگاه پشتیبانی دریایی آمریکا در بحرین در نخستین روز جنگ از فعالیت خارج شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/693837" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693836">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اختلاف قیمت حدودا ۳ برابری سیب در بازار!
رضا نورانی، رئیس هیئت‌مدیره اتحادیه ملی محصولات کشاورزی ایران در
#گفتگو
با خبرفوری:
🔹
قیمت سیب در میادین عمده‌فروشی حدود ۱۶۰ تا ۱۷۰ هزار تومان است اما در سطح شهر تا ۴۵۰ هزار تومان هم فروخته می‌شود.
🔹
اختلاف قابل‌توجه قیمت عمده‌فروشی و خرده‌فروشی ناشی از ضعف نظارت بر بازار است و هر میوه‌فروشی قیمت متفاوتی برای محصولات تعیین می‌کند.
🔹
صادرات محصولات کشاورزی به عراق فعلاً به‌طور موقت متوقف شده و اثر آن بر قیمت سیب‌زمینی و پیاز در بازار عمده‌فروشی مشهود است اما کاهش قیمت در خرده‌فروشی‌ها به همان میزان دیده نمی‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/693836" target="_blank">📅 00:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693835">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
واشنگتن‌پست: پایگاه پشتیبانی دریایی آمریکا در بحرین در نخستین روز جنگ از فعالیت خارج شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/693835" target="_blank">📅 00:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693834">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLLUy0ULPuyqutcRI4zD93vG4gB-sNbdyGEVnnBBHwH0NFCIE4ZtBze_miXDI1Uf973-4tHmYg4AQPcrUBQ2ng_f4SyCi5ILHw-ANXOv-ZvmYe7vvsefTkWsukOR_QajNGranq9n1LSbZ-cFCjSd2N8JmUg3JSs55tQAw8SvXiwaWu2qjfGFoQkN-_QB2kvqOOf1JE04bL6JkjM_y3oA7vR2M6G91AYhRuOij1SGWoHEZ5k5CI3jtuZg8ubQy7HkrqDw8M6O-TFz2hJVDkqzhMETweQHqBlhaOhvYYBj2nzZR92jZge7ENbeLTwGEE45pl65iOGVIhdZfwEXskIxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/693834" target="_blank">📅 00:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693833">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6cf54c5.mp4?token=YnWRE8le3u722JGJUm0fAolp-K6LPM5CsHnQMAM19Z4q0MGp0AQSO3Zg6HoRYJ4nYuWIzzUnFY9iQ9GQAfZftxT_yYSKu2ydBbdjvNBW4t9jK64Y1GIuLy_BetVom1u8AI_UHcFZ8qAxwaBWKmaDt6ooant08K-OamPjxqdBC-xP-QxxdVqwiMvjejRI1Q1hVPlD4Bm0xkqpL2kz4Nh7X8WxW4NOLmJYurFEVoH6Fqsi1GqhRSkwIuVY3Tec-D9WC1k15tgcWiOkkaA8lOn4D0aFdxndmfAhJBKyo6c-FXXEglcCtGh3y7PgV9bGUFKIHD_63La2LNAKtayXv7oqUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6cf54c5.mp4?token=YnWRE8le3u722JGJUm0fAolp-K6LPM5CsHnQMAM19Z4q0MGp0AQSO3Zg6HoRYJ4nYuWIzzUnFY9iQ9GQAfZftxT_yYSKu2ydBbdjvNBW4t9jK64Y1GIuLy_BetVom1u8AI_UHcFZ8qAxwaBWKmaDt6ooant08K-OamPjxqdBC-xP-QxxdVqwiMvjejRI1Q1hVPlD4Bm0xkqpL2kz4Nh7X8WxW4NOLmJYurFEVoH6Fqsi1GqhRSkwIuVY3Tec-D9WC1k15tgcWiOkkaA8lOn4D0aFdxndmfAhJBKyo6c-FXXEglcCtGh3y7PgV9bGUFKIHD_63La2LNAKtayXv7oqUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی وزیر دولت امارات: امارات خواستار پیگیری اشغال جزایر سه‌گانه تنب بزرگ، تنب کوچک و ابوموسی توسط ایران است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/693833" target="_blank">📅 23:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693832">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رضایی، عضو کمیسیون امنیت ملی مجلس: دیپلمات‌های ایرانی در شرایط فعلی هیچ مجوزی برای انجام مذاکرات دوجانبه یا سه‌جانبه ندارند/ تا اجرای تعهدات آمریکا در تفاهم اسلام‌آباد، مذاکره‌ای آغاز نمی‌‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/693832" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693831">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار در جزیره قشم به گوش رسید
🔹
این صدا از سمت دریا بوده و به نظر می‌رسد اصابتی داخل جزیره رخ نداده است. منابع محلی تاکنون در این زمینه اظهار نظر نکرده‌اند  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/693831" target="_blank">📅 23:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693830">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
نایب‌رئیس مجلس: مجلس طرح سه فوریتی خروج از NPT را بررسی می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/693830" target="_blank">📅 23:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693829">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f868d2f383.mp4?token=mPn0iDAIs0qoNhwPdaoo_9mYI3qNfjhx5Gtj_A7L2XPEOtHERRLM3mdwUYcoY7FB6taHZAS-cNBc5vKSuc5Zn8H0O4kad6AfHH6g7TeGq8nAzqEENFW4VxFubOj9OrftxVxF_rf0wVVjyU2JrwbWPnf5zwQuvM_FA0bru0clOmPoxXXam1_Jl0szdNnthU80XAyczj3G1VcuhawbcZnvGCLJTQ-HsqGW-2gyLuDAseoh1oax3NTVDUhmvYlW4Z0nyP-7OfCVxAsFf6Po6cptGrG9mZ7H2px_YLlJ6y4HWzGSpIfsC_TuUVR_7K21cRI-5_V_kj2SwLRcTN6juDHsC4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f868d2f383.mp4?token=mPn0iDAIs0qoNhwPdaoo_9mYI3qNfjhx5Gtj_A7L2XPEOtHERRLM3mdwUYcoY7FB6taHZAS-cNBc5vKSuc5Zn8H0O4kad6AfHH6g7TeGq8nAzqEENFW4VxFubOj9OrftxVxF_rf0wVVjyU2JrwbWPnf5zwQuvM_FA0bru0clOmPoxXXam1_Jl0szdNnthU80XAyczj3G1VcuhawbcZnvGCLJTQ-HsqGW-2gyLuDAseoh1oax3NTVDUhmvYlW4Z0nyP-7OfCVxAsFf6Po6cptGrG9mZ7H2px_YLlJ6y4HWzGSpIfsC_TuUVR_7K21cRI-5_V_kj2SwLRcTN6juDHsC4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعت هوشمندی که بندش برای اندازه‌گیری فشار خون باد می‌شود
🔹
هواوی در ساعت هوشمند Watch D3 از روشی متفاوت برای اندازه‌گیری فشار خون استفاده کرده است؛ داخل بند ساعت یک کیسه هوای کوچک قرار دارد که هنگام اندازه‌گیری باد می‌شود و با ایجاد فشار روی مچ، عملکردی مشابه کاف دستگاه فشارسنج دارد.
🔹
این ساعت علاوه بر پایش فشار خون، امکاناتی مانند اندازه‌گیری قلب، سطح اکسیژن خون، ثبت نوار قلب، پایش خواب و بررسی برخی شاخص‌های سلامت را نیز ارائه می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/693829" target="_blank">📅 23:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693828">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آلودگی هوا در آذر و دی امسال نسبت به سال گذشته کمتر خواهد بود
محمد اصغری، کارشناس هواشناسی در
#گفتگو
با خبرفوری:
🔹
بیشترین آلودگی هوا معمولاً در ماه‌های آذر و دی و همزمان با تشدید وارونگی دما رخ می‌دهد، اما احتمالاً امسال میزان آلودگی هوای شهری در این دو ماه نسبت به مدت مشابه در سال گذشته کمتر خواهد بود.
🔹
امسال عبور موج‌های جوی بیشتر خواهد بود و این موج‌ها با ایجاد تهویه طبیعی، می‌توانند از ماندگاری آلودگی در شهرها جلوگیری کنند.
🔹
با توجه به پیش‌بینی بارندگی مناسب‌تر در خاورمیانه و مناطق اطراف ایران و تهران، وضعیت گردوخاک نیز امسال می‌تواند بهتر از سال گذشته باشد.
@TV_Fori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/693828" target="_blank">📅 23:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693827">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
مسئول امنیتی کتائب حزب‌الله عراق؛ ضرب‌الاجلی تا ۱۰ مهر برای لغو محاصره هوایی ایران، اعلام کرد
بیانیه کتائب حزب الله:
🔹
در صورت تداوم محاصره هوایی جمهوری اسلامی ایران پس از یکم اکتبر (۱۰ مهر)، موضع ملت عراق قاطع خواهد بود و کار به بستن مرزها و گذرگاه‌ها با کشورهای شریک در تحریم ملت مؤمن ایران خواهد کشید.
🔹
مقاومت اسلامی بر آسمان کشور نظارت خواهد داشت و ابتدا هشدار داده و سپس پرنده‌های متخاصم را ساقط خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/693827" target="_blank">📅 23:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693826">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
نایب‌رئیس کمیسیون امنیت ملی: پیش از هر مذاکره‌ای، آمریکا باید شروط ایران را بپذیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/693826" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693824">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
برخی منابع یمنی از حمله موشکی یمنی‌ها به اهدافی در عربستان گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/693824" target="_blank">📅 23:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693823">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار در جزیره قشم به گوش رسید
🔹
این صدا از سمت دریا بوده و به نظر می‌رسد اصابتی داخل جزیره رخ نداده است. منابع محلی تاکنون در این زمینه اظهار نظر نکرده‌اند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/693823" target="_blank">📅 23:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693821">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVYLeeV6gCd7V8MGvq7GNwStk-7oXMGwekkjuU_amifGQcFJVBKEQ109X6vdKIw73HeJFWmuhFPzk5kKmxmecjge-EeSeaYyOD9yR5fVQd8hJ4rtw1FhgeOa90GjwtnjhYuAAwOmm4jlIL6R3FQK7ybzDDo0oftEVpU-uFoqYhj96oXjfYZzUJs1vkVEdy_VbGZqt8Gum4ig492IeCzbSbDJVLgzGnjofTZdmu0aBD7DMEH4OkVRUY32_I66ELLG61wy7VzxJZuJ29oQcu0jpsVHDYwKKCxzaCXskzLpOmvKWcGn-Jp_RUi7bmFLGBG-PJE8m41lsSFtWM4z8JkMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G63u3xVdJK8bkIzRZqz55eQhyY9oDer5QktXZ0Vbllqkc1VzcTIruj9s4O-E52-KuQKa3dZY4uW7BQUoGhRpUeKRWcQqinFAK6ZkmB4XBVUQASrkv2HkLHuKNW33uYpwP6av-uzWTa8pDIIqs9mBzQ8xO0YY53CKvLveT9mFjCHdz_Z2Vkf29qUVBT1IlpVZ62hE3-hwMayW56uGOefBqAdFQUDHCE4fBJyUZN7VCYbAf1YfTraFPnIXfl9DGc_WThHvQEO6JO9Lhus7ULkQz9PLNiWYANlihFcV4n6gVN7geBWvLhdNW5F9PgmfH8FbF7Wab3LbNklU_hmOE-eguw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قهرمانان تغذیه برای رشد قد کودکان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/693821" target="_blank">📅 23:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693820">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نماینده آمریکا در شورای امنیت: واشنگتن با الحاق کرانه باختری توسط اسرائیل مخالف است
/ الجزیره
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/693820" target="_blank">📅 23:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693819">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONz2nkSsWBuEo9AColo9lzXWg7QxDUEQwgXm0nEQwQnZ7vfQPPOUfRRDXsCDvbZBNnqmBx-wjxWuw_WMNh_xnPYt6X5JNVujsjJZYRLdsp2wHTLZIp9991kLoraq_VAmdXabnx8OBTsM50F17sty8SI3Mg2paSz5YejX5Ffl57D8eqEJan7z8vpfYSBjQ6klVS7DCQhCqwXXtaw7mGfL57KW8Hoh4QT9UpYspFny3seUsIJvvk1hk3j8U-lqzkVnBPIIUAfuZ-lUK7QW6_1MtNBeAS_d0ItuDdhCE68BEqwNIxozApGgwae8lhIDPX_r2z02kwGzqaABwSZX1ikafg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میلی اسناد تحویل طلا به خزانه‌های بانکی را منتشر کرد؛ روایت از کارشکنی در تسویه کاربران
🔹
میلی با انتشار اسناد به روز تحویل طلا اعلام کرد بیش از ۸۵۰ کیلوگرم طلا در خزانه‌های بانکی دارد، اما به‌دلیل آنچه «کارشکنی برخی افراد در پلیس امنیت اقتصادی، دادستانی و بانک کارگشایی» عنوان کرده، دسترسی به این ذخایر برای تسویه کاربران با محدودیت مواجه شده است.
🔹
به گفته میلی، طی یک ماه و نیم گذشته حدود ۳۵۰ کیلوگرم از ذخایر خارج از خزانه‌های بانکی برای تسویه کاربران مصرف شده است.
🔹
این پلتفرم تأکید کرده دارایی کاربران محفوظ است و موضوع محدودیت‌ها را از نهادهای امنیتی پیگیری می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/693819" target="_blank">📅 23:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693818">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/510e502a72.mp4?token=lsh29WSWH34B5yynrx7GZV0ZsrJWR-Gf7ETuGdvT0JaLp1igxhwdllftsTlEOXzLYu2_j3cSgfrBa5oYYH0KCdP6Air3dtl4ADVYk9Nvkq4WwWbFEUw2o6QuM30R9tuGwUNaNzkPIAwj8LvFTdiq-WqgH5yBeOv-ocF0bYqvLSjQ6ldB1uRoIzIuZ961yfqO9ypMtNGA8YFbUFqodNN_9BkA6gbcXwuH1dpDq6vbldOA3vK9sRG5GLWuUWflsT7rmlv03iDAXp_DqLevyza0qwdsyR6HZ7td-lkfdqxKzhn6Yxi6ROCErZYYvKQV_ecwFZka73QcTqvvTyZ_UTdQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/510e502a72.mp4?token=lsh29WSWH34B5yynrx7GZV0ZsrJWR-Gf7ETuGdvT0JaLp1igxhwdllftsTlEOXzLYu2_j3cSgfrBa5oYYH0KCdP6Air3dtl4ADVYk9Nvkq4WwWbFEUw2o6QuM30R9tuGwUNaNzkPIAwj8LvFTdiq-WqgH5yBeOv-ocF0bYqvLSjQ6ldB1uRoIzIuZ961yfqO9ypMtNGA8YFbUFqodNN_9BkA6gbcXwuH1dpDq6vbldOA3vK9sRG5GLWuUWflsT7rmlv03iDAXp_DqLevyza0qwdsyR6HZ7td-lkfdqxKzhn6Yxi6ROCErZYYvKQV_ecwFZka73QcTqvvTyZ_UTdQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگ‌ترین دارایی ما در این سال‌ها چی بوده؟!
@TV_Fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/693818" target="_blank">📅 23:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693817">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/693817" target="_blank">📅 23:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693816">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmRw1VYtSObeg0AE04Fi0AgVwLlXW6tBapRTbA98bJA3PkmN9rrfJ7tzHctqZfpFtaa57-8s5VdnxFf_1EJzDdGY-orzJ9hV2YUm2BpadWOqhIH658ND7zZd2zDkjTDrnV6A92_l4Qm8zGccu5xMxW6d2pVo8yVEO7grvKe49H0YyOgQxjIEPo99Eny0lJd3Kz7mgL8HrNhfU_MO479tBcHuw4ikM0MYgyW9jKUeGChkNdskMmNpTckOpqxr7u6_oZeEgBsM-dTHdlIl_EO236KUokSS9fmNdlrSFObA-Rj6o2qnRuEPSLkyOXWczxPXRuTCJ1LEf9mn6BwGeEqbTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیروئید فقط خستگی نیست؛ این نشانه‌ها را هم به همراه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/693816" target="_blank">📅 23:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693815">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه هفتم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/693815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌ گذر از دجال
جلسه‌ هفتم: تفسیر دعای تقویت حافظه
🔹
تکنولوژی با فراهم کردنِ پاسخ‌های آماده، در حال تضعیفِ بخشی از مغز و توانمندی‌های ذهنی انسان است.
🔹
هدف نهایی دجال، «کم‌عقل کردن» و «منفعل کردن» انسان‌هاست تا در نهایت انسان‌ها قدرت مقاومت یا تشخیصِ حقیقت را نداشته باشند و به سادگی کنترل شوند.
🔹
دعای تقویت حافظه، دعایِ کلیدیِ افزایش فهم و بصیرت است که برای تقویت مرکز ادراک قلب و مقابله با زوال عقل توصیه شده است.
🔹
چهار درخواست کلیدی در دعای تقویت حافظه وجود دارد: «طلب نور» برای تشخیصِ خیر از شر، «طلب بصر» برای دیدنِ حقیقتِ مسائل، «طلب فهم» برای قدرتِ تجزیه و تحلیل اطلاعات، «طلب علم»دانشی که ناشی از اتصال به نام «علیم» پروردگار است.
🔹
آدم جاهل و سطحی‌نگر، هرگز به درکِ امام زمان (عج) نمی‌رسد، شرطِ رسیدن به شناختِ ولیّ، داشتنِ «کمالِ عقل و فهم» است.
🔹
برای ترک اعتیاد به «غم‌خواری و نشخوار فکری»، باید ذهن را با موارد متعالی مانند ذکر مداوم و حفظ ادبیات حکمت بنیان و اشعار پر مغز تمرین داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/693815" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
مقام ایرانی به پرس‌تی‌وی:
انعطاف‌پذیری ایران در موضع هسته‌ای نادرست است/ موضع ایران در مورد مسئله هسته‌ای تغییر نکرده
است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/693814" target="_blank">📅 22:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل ادعا کرد:دیدار نتانیاهو با رئیس‌جمهور امارات حدود شش ساعت به طول انجامید و تمرکز اصلی آن بر روی جنگ آتی با ایران بود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/693813" target="_blank">📅 22:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693812">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ترامپ در حالیکه باز هم در جلسه کاخ سفید چرت زد گفت قیمت سوخت کاهش خواهد یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/693812" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693811">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کمبود ۱۰۰ هزار معلم در آموزش و پرورش
بیت‌اله عبداللهی، عضو کمیسیون برنامه و بودجه مجلس در
#گفتگو
با خبرفوری:
🔹
حداقل حکم کارگزینی معلمان جوان و تازه‌ فارغ‌التحصیلان فرهنگیان، حقوقی بین ۱۸ تا ۲۰ میلیون تومان است و با احتساب هزینه ایاب‌وذهاب در مناطق دورافتاده و روستایی، دریافتی آنان به ۱۴ تا ۱۵ میلیون تومان کاهش می‌یابد، این وضعیت با هیچ منطقی جور نیست.
🔹
این وضعیت محدود به معلمان نیست و کارکنان سازمان‌هایی مانند جهاد کشاورزی، صنعت و معدن وزارت کشور و حتی بازنشستگانی مانند فرمانداران سابق نیز با حقوق‌های ۲۰ تا ۲۸ میلیون تومانی مواجه‌اند.
🔹
آموزش‌وپرورش برخلاف بسیاری از دستگاه‌های عریض و طویل که با تراکم نیرو و خروجی ضعیف مواجه‌اند، با کمبود حدود ۱۰۰ هزار معلم روبرو است و به ناچار از بازنشستگان برای پر کردن کلاس‌ها استفاده می‌کند، بنابراین راهکار اصلی کوچک‌سازی سایر دستگاه‌ها و تخصیص منابع آزاد شده به آموزش‌وپرورش است.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/693811" target="_blank">📅 22:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693808">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c36539f53e.mp4?token=Qb6oXicwrUcHFD1_Hz3oSuNhz42foltTlJK6JnCldzU4uW50VGlF0dmtO4PK_zUIvOEhK85GqYBttbZM1ahMCEo95di0lov0uwecVNj1EWs-r2vPUQ-n5YCn5x2yUZSYHRnSdaeyxJDI4e6-HyMRSBurRFTIqLDwoTIxoplSgVmO3wOCAT-eSWnWeu-tK5yZ79aMmRAjNDLGUs-KoBMO5keAy05_VtRw3QO9yJQo5b40xnsWM3gIe4PEUkxe-eL-obpWyqw-T-jaQH4TWSlwJtjH_eTC8dLJBEoJ1BMu5-QdJRuWwlbkMc460OQV1AOxfVvrIkGmlDYlgz70A03-vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c36539f53e.mp4?token=Qb6oXicwrUcHFD1_Hz3oSuNhz42foltTlJK6JnCldzU4uW50VGlF0dmtO4PK_zUIvOEhK85GqYBttbZM1ahMCEo95di0lov0uwecVNj1EWs-r2vPUQ-n5YCn5x2yUZSYHRnSdaeyxJDI4e6-HyMRSBurRFTIqLDwoTIxoplSgVmO3wOCAT-eSWnWeu-tK5yZ79aMmRAjNDLGUs-KoBMO5keAy05_VtRw3QO9yJQo5b40xnsWM3gIe4PEUkxe-eL-obpWyqw-T-jaQH4TWSlwJtjH_eTC8dLJBEoJ1BMu5-QdJRuWwlbkMc460OQV1AOxfVvrIkGmlDYlgz70A03-vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در حالیکه باز هم در جلسه کاخ سفید چرت زد گفت قیمت سوخت کاهش خواهد یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/693808" target="_blank">📅 22:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693807">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: ما خیلی زود در جنگ با ایران پیروز خواهیم شد و آن جنگ تمام خواهد شد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/693807" target="_blank">📅 22:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693806">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
دریادار سیاری: از خلیج فارس تا شمال اقیانوس هند مال ایران است
🔹
تمامیت سرزمینی و ناموس ایرانی خط قرمز نیروهای مسلح است و وقتی پای ناموس ایرانی وسط باشد از هیچ چیز و هیچکس باک نداریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/693806" target="_blank">📅 22:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693804">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5922f04ef0.mp4?token=YkdjuKn_4ltW9ux7RB199_ZPXxGjLOGdoCcKOwwzYsZ0rbolvu_QOqeyCSNNt-hN_0NsIQ5us7xLgilwnbBQvtCEyj9GbmgPDSH__joBM0EGWQiJR2__IieAMcnRUpJlpq2z1qaoOrHbign65pV7ydQjnKziOf718uBoCmzUAAiBtJo7AE_HtvtGkEMgCh3CAL3czSr5SecyTMfu8uNzKxC2kfmn_oOTZ9DKORzb0qDo7DcDLG-N8g4nrUUdpGXJ7BZi3hjA40bjd9ZSKRUuZN3Q6s6K2_pRLSb5jxAfFMrfy6d2__Tnvid4ajOmPxqdHQ2h2dY7T3J7jY3W0otVPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5922f04ef0.mp4?token=YkdjuKn_4ltW9ux7RB199_ZPXxGjLOGdoCcKOwwzYsZ0rbolvu_QOqeyCSNNt-hN_0NsIQ5us7xLgilwnbBQvtCEyj9GbmgPDSH__joBM0EGWQiJR2__IieAMcnRUpJlpq2z1qaoOrHbign65pV7ydQjnKziOf718uBoCmzUAAiBtJo7AE_HtvtGkEMgCh3CAL3czSr5SecyTMfu8uNzKxC2kfmn_oOTZ9DKORzb0qDo7DcDLG-N8g4nrUUdpGXJ7BZi3hjA40bjd9ZSKRUuZN3Q6s6K2_pRLSb5jxAfFMrfy6d2__Tnvid4ajOmPxqdHQ2h2dY7T3J7jY3W0otVPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: ما خیلی زود در جنگ با ایران پیروز خواهیم شد و آن جنگ تمام خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/693804" target="_blank">📅 22:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693803">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2799f390bd.mp4?token=Nmzixjo4PTZKL8MbIAIx9jeNuT0t1SWPrxmuT8bMdrZ_SMykZPCs5LSCzgIx8GhsevteI7kHVQOsNhF2HiZRkGwrovKjaIkquwIQ9CadS5rX_GpqP-TygqkDwGZb0Lx90-diU5g-NIIu--PO1ZIGOzvDplb5JKT6ZRsQvB5yfHkG3Q2D-1a72ahiZgwcrtj9LHMMIfaW22r2ywAlXzjzr49BIxH9V0R6itmVd1zrhh_0tA6Hp87kwO8FrWTZxYQEfnrUVJZbbiqs_V380dlycopC91jvYkYj9OIF5v6ZpdW9SE5RyVt4eumpF6ZB6_g4Ssd9Hql_dfdJ7qsXRosygQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2799f390bd.mp4?token=Nmzixjo4PTZKL8MbIAIx9jeNuT0t1SWPrxmuT8bMdrZ_SMykZPCs5LSCzgIx8GhsevteI7kHVQOsNhF2HiZRkGwrovKjaIkquwIQ9CadS5rX_GpqP-TygqkDwGZb0Lx90-diU5g-NIIu--PO1ZIGOzvDplb5JKT6ZRsQvB5yfHkG3Q2D-1a72ahiZgwcrtj9LHMMIfaW22r2ywAlXzjzr49BIxH9V0R6itmVd1zrhh_0tA6Hp87kwO8FrWTZxYQEfnrUVJZbbiqs_V380dlycopC91jvYkYj9OIF5v6ZpdW9SE5RyVt4eumpF6ZB6_g4Ssd9Hql_dfdJ7qsXRosygQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پول زور در مدارس ممنوع؛ ثبت‌نام را به مالیات گره نزنید!
🔹
هیچ مدرسه‌ای حق ندارد به اسم «کمک اختیاری»، خانواده‌ها را در تنگنا قرار دهد یا اسم دانش‌آموزی را به دلیل عدم تمکن مالی والدینش در مدرسه مطرح کند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/693803" target="_blank">📅 22:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693802">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E57geqG75A-p9PMnWcFwsxRRG_RL6IQrEEy1CpJu4Q8959PO5L9QtCrrAUG62WonaDmw5sWLM4_HEouQwme74yIPbXbAczDRV3rN8nDo4VG3aPSh8Rs43D8PVGUgaOhVC4xs0j8oi9r3K_69LYQgbS8NAXNoW7YW9icXpp49xLETeUXF3_dth1Du3f_2e8zjvaJOyse_xXiGx5Xa7gVUdWmNOSqYRzxL7kwdl0D1kFflgVAYoPVafau9TxdJHcsZHJhzEk0KxV6ctr56Lp5mYLXbWAnIItgqfYLZP57pZ6FzaoJfWCJ0kk5-4uVcrQ8_X1MvFbpJV9LWaIH10wv7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تببین قدرت ایران
🔹
رهبر معظم انقلاب در بخشی از پیامشان به ‌مناسبت هفته دفاع مقدس و سالگرد شهادت شهید سیدحسن نصرالله فرمودند که این روزهایی که در آن هستیم پُر است از پیشرفت، عزّت، استقلال، و قدرِ اَعلای اعتبار در جهان اسلام و بلکه کلّ جهان. امروز کسانی ما را ابرقدرت چهارم دنیا می‌دانند. البته آنان بر اساس محاسبات دنیایی چنین می‌گویند؛ ولی محاسبات الهی، کشوری که خود را متعلّق به عترت طاهره صلوات‌الله‌ و سلامه‌‌علیهم‌اجمعین می‌داند و عمده مردمانش دلبسته آن والامقامانند و برای اقامه حق هراسی ندارند را قدرت اوّل جهان می‌داند. ایشان اظهارداشتند که روزهایی بود که دشمن سعی کرده بود عقبه اجتماعی نظام را دائماً ضعیف‌تر سازد ولی در این روزها انواع اقشار جامعه با تفاوت‌های آشکار، بر حفظ مواضع بحقّ خود و از جمله حفظ تنگه پر خیر و برکت هرمز پای می‌فشارند.
🔹
هشتصدوهفتادودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/693802" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693801">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55493978e.mp4?token=D52ym5Ene0SypTzA_ParlElpbD3do9ffX7KDfuOnPqRDJFDkkHTtc2FfGdEQsY_kKwUNiUJhHC8f1gJ3AehocjmcezlgUpQCtQyhZ3kRdlrw2tAkipHNk1Dszwsqj_oL87p4ZjlVhUxv4_eLt1j2aA5Php_wA4ftOK-ZnH5K5b2lbBqH_bO7Iu-rS0CjpCCf7JD6W04CD2KDK8yR9KLF1Cahbil9dYgM2J0Dzp3T3fevU0yLHkylpD0RZfE7GH9V1dxXim3unlwaweNiTPRwmLdpPLwT9XT9Det1n21E44ztVB40uAj_g9CuHHGgoQOpnOOGCEPAn2Ch19NDOvgIgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55493978e.mp4?token=D52ym5Ene0SypTzA_ParlElpbD3do9ffX7KDfuOnPqRDJFDkkHTtc2FfGdEQsY_kKwUNiUJhHC8f1gJ3AehocjmcezlgUpQCtQyhZ3kRdlrw2tAkipHNk1Dszwsqj_oL87p4ZjlVhUxv4_eLt1j2aA5Php_wA4ftOK-ZnH5K5b2lbBqH_bO7Iu-rS0CjpCCf7JD6W04CD2KDK8yR9KLF1Cahbil9dYgM2J0Dzp3T3fevU0yLHkylpD0RZfE7GH9V1dxXim3unlwaweNiTPRwmLdpPLwT9XT9Det1n21E44ztVB40uAj_g9CuHHGgoQOpnOOGCEPAn2Ch19NDOvgIgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درحالی که مدعی بود پیروزی در انتخابات کنگره برایش اهمیت ندارد بار دیگر وعده ۵ هزار دلار به ازای هر رای را تکرار کرد
ترامپ:
🔹
اگر جمهوری‌خواهان در انتخابات مجلس نمایندگان و سنا پیروز شوند، به هر فرد بزرگسال پنج هزار دلار پرداخت خواهد شد؛ و ما می‌توانیم این کار را انجام دهیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/693801" target="_blank">📅 22:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693800">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
دریادار سیاری: مهاجمی که به اهداف خود نرسد یعنی شکست خورده
🔹
کشورهای حوزۀ خلیج‌فارس در جنگ ۸ ساله به صدام امکانات دادند و در این جنگ هم پایگاه‌ها را برای حمله به ما دراختیار دشمن گذاشتند
🔹
صدام فکر می‌کرد زمانی که به مرزهای ایران برسد از او استقبال می‌شود؛…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/693800" target="_blank">📅 22:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693799">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/435c672b32.mp4?token=mDcNJ3eiT1wLJWe2TtIf7svsa9LeIckA6Yr49Z3AIAqhwkZDRvTnEVeBprN2N1S7wcbqH5SFq47xCfAWert3urrVVLnUjpX8eu1Siw45r2LVza3pUhCH2jz6T5kxlMpQKO07SFmCwrtIATJQSEAmSC3ihjm-jEGb3XQq-O4NxZOdHsYaubW4OsEEjZ9pNYG6O0hDKPFb-DyneIKlDlIBNgwT2ioM2O7d3yXsAdq2DZOhwJtqxo3NDWqyDN9O4nsTjyYmVKYjGYoLKioSUDZMYCG2vPnVuCcWHqoPCCDFnrnEn2vN47sbcWS3jYFvrQ4QNVAEhfqjWGoBfpkQnteosE4QMlavJRUXgyMcnZ9o7NphRpxyu9yU7DLH180obulLnCxYJ1ZJEu9RwPC_YH8HaQhFQ0CIAAq6fapYzDYDyi2AYOuA0UTuCvLsy8MzXePlo7ukAlzTDt0WGC8e73pkKgkNyDQyHw7wIkRmh-e22J3ato9fA2WheZcSO6rZDGj8808mf7Y0mSU1ZIy6X4zA58Sj6_n2q9YmFdYD7VYpYqQOi548txLXd1FANIHQG5r6RWXh53_qIA7myce9FnF5ol8WrNn5B_s1NFtYzWt2Kxg6FpN1wp73AG5l-OTDV5A5U03y_-eUmvOoQVOiKkghDe5ys9-ifVtOqmP4MhI8MqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/435c672b32.mp4?token=mDcNJ3eiT1wLJWe2TtIf7svsa9LeIckA6Yr49Z3AIAqhwkZDRvTnEVeBprN2N1S7wcbqH5SFq47xCfAWert3urrVVLnUjpX8eu1Siw45r2LVza3pUhCH2jz6T5kxlMpQKO07SFmCwrtIATJQSEAmSC3ihjm-jEGb3XQq-O4NxZOdHsYaubW4OsEEjZ9pNYG6O0hDKPFb-DyneIKlDlIBNgwT2ioM2O7d3yXsAdq2DZOhwJtqxo3NDWqyDN9O4nsTjyYmVKYjGYoLKioSUDZMYCG2vPnVuCcWHqoPCCDFnrnEn2vN47sbcWS3jYFvrQ4QNVAEhfqjWGoBfpkQnteosE4QMlavJRUXgyMcnZ9o7NphRpxyu9yU7DLH180obulLnCxYJ1ZJEu9RwPC_YH8HaQhFQ0CIAAq6fapYzDYDyi2AYOuA0UTuCvLsy8MzXePlo7ukAlzTDt0WGC8e73pkKgkNyDQyHw7wIkRmh-e22J3ato9fA2WheZcSO6rZDGj8808mf7Y0mSU1ZIy6X4zA58Sj6_n2q9YmFdYD7VYpYqQOi548txLXd1FANIHQG5r6RWXh53_qIA7myce9FnF5ol8WrNn5B_s1NFtYzWt2Kxg6FpN1wp73AG5l-OTDV5A5U03y_-eUmvOoQVOiKkghDe5ys9-ifVtOqmP4MhI8MqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام موجودیت جنبش مسلحانه حرکت یحیی با وعده انتقام از آمریکایی‌ها و اسرائیلی‌ها با استقبال گسترده در شبکه‌های اجتماعی مواجه شده است
🔹
به تازگی یک جنبش مسلحانه تحت‌ عنوان حرکت یحیی که برگرفته از نام یحیی سنوار، فرمانده شهید جنبش حماس می‌باشد با صدور بیانیه‌ای و با وعده انتقام از جنایات آمریکا و اسرائیل، اعلام موجودیت کرده و با محکوم کردن سکوت جامعه بین‌الملل، دعوت و درخواست مشارکت از عموم مردم در سراسر دنیا را برای همراهی با این جنبش داشته است.
🔹
در کانال اطلاع‌رسانی این جنبش آمده است: ای جنایتکاران، ما نه در سرزمین خودمان بلکه در سرزمین خودتان و درب خانه‌هایتان به سراغ شما خواهیم آمد.
🔹
این جنبش اعلام کرد، لیستی از صدر تا ذیل این جنایتکاران تهیه و افشا خواهد کرد و آمادگی این را دارد تا با بکارگیری کمک‌های ناشناس مردمی، از اقدامات عملی هر فردی که قصد عملیات یا ارسال اطلاعات در مورد عوامل جنايات را دارد، حمایت کند.
🔹
در صفحات این گروه در شبکه‌های اجتماعی، هیچ نشانه‌ای از هویت و وابستگی به جریان یا کشوری موجود نیست هر چند در شبکه‌های اجتماعی، گمانه‌زنی‌هایی از نزدیک بودن این گروه به جنبش‌های مقاومت فلسطین وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/693799" target="_blank">📅 22:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693798">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
دریادار سیاری: مهاجمی که به اهداف خود نرسد یعنی شکست خورده
🔹
کشورهای حوزۀ خلیج‌فارس در جنگ ۸ ساله به صدام امکانات دادند و در این جنگ هم پایگاه‌ها را برای حمله به ما دراختیار دشمن گذاشتند
🔹
صدام فکر می‌کرد زمانی که به مرزهای ایران برسد از او استقبال می‌شود؛ ترامپ هم فکر کرد مردم ایران اگر بگوید کمک در راه است و ایران را بمباران کنند مردم از او حمایت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/693798" target="_blank">📅 22:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693797">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2zqkk8YSTFD418W7mj7r-aYTHtfW4FAhb48OCOXJiGZMCZB8MNaw6ln2t00Dnkb6HVmUaRVQNfKtIWr1yyW55AMvc2l_U5QSvRG7DXtfFWJn1wFhFK11K2rRlQOatdmjegc4y2rd69EtUQk02E1awh8J8GmJReLivbvvxxKvAbf1BuV2nwsAzyNkiiLlKFV_YEIHAWmxEvIMnzf-yb4I-X6kbLxrVU-xaJLcRMd1uPzuzVLTIZdrbiGdy2o2af9wztYdlN_OuoJiWcH2xCLEADwoNV95ua3MBMTy3WUACFrxPGpDXHRGHKbFBSJzqRGkCmX4YK8xdIi4AJrtESzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه رهبر انقلاب به برادرشان آیت‌الله سیّدمصطفی خامنه‌ای در دوران نوجوانی و در هنگام حضور وی در
جبهه
بسمه ‌تعالی
🔹
خدمت برادر عزیزم، رزمندۀ گرامی سیّدمصطفی، بالاخره پس از مدّتها که قصد نامه نوشتن را کرده بودم موفّق به چنین امری شدم.
🔹
جای شما خالی، ما در مشهد پس از زیارت و دید و بازدید از سبزوار بازدید کردیم. استقبال مردم خیلی خوب و دلگرم کننده بود. امّا خوب، جای ما هم در آن محیط صفا و خلوص و عشق به خدا خالی. ای‌کاش باز هم توفیق پیدا کنیم و در آن مکان الهی حضور پیدا کنیم.
🔹
بعد از اینکه به تهران آمدیم من دائماً در صدد تهیّۀ کتاب درسی و اسم‌نویسی در مجتمع رزمندگان بوده‌ام تا اینکه دیروز موفق به اسم نوشتن شدم.
🔹
قرار است همگی چند سطری در ادامۀ این دو نامه بنویسند و من از طرف بشری و هدی هم سلام میرسانم. امیدوارم در پناه توفیقات حضرت حقّ انجام وظیفه (بطور احسن) را بنمائی. زیاد وقتت را نمی‌گیرم و تو را به خدا میسپارم./والسلام. سیّدمجتبی
چهارشنبه ۹ مرداد ۶۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/693797" target="_blank">📅 22:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693796">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9JD2Muo_ZipcQ9Fk-eYbCCppBzNvC1J64UsWE0ixqQJtdkzCEWNTdplmek7dSvKN_9FbJj9YYBsh01N1keXMYcdO75ETqot4QiQmGRDCD1-Dh3q5T2BC9yOgPAyHzPxLUeNCORsohSrxubzh2WNuFdPClRXLP_ciWyqjONHdC4jdc4s4ii9hnQscZfcG2dr5iTdpvDaMZGoNulvOKmYNfjufxHxjXBMAeofqogYHRW7pqnMY5hXRvj3C3gVM9KdSpbszwAnaPmdqo5r91sycqHL_Wsa8a25Gob7KjDDe7AojQXWKJEUWbp53KtREpwacrhDvO8nm5UWVj1Ow8xUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی رسمی از سامانه پیامکی هلدینگ رسانه‌ای خبرفوری
🔹
همزمان با یازدهمین سالگرد تاسیس هلدینگ خبرفوری، از "سامانه هوشمند پیامک خبری" به عنوان گامی نوین در مسیر اطلاع‌رسانی فراگیر رونمایی شد.
🔹
این خدمت راهبردی با هدف دسترسی بی‌وقفه مخاطبان به اخبار مهم…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/693796" target="_blank">📅 22:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693795">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: میانجی‌ها برای امتیاز هسته‌ای، به ایران فشار می‌آورند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/693795" target="_blank">📅 22:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693794">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4952d610ef.mp4?token=OAhiAZ-QO6qb6dIlGeqx6hsMm8ubLc0h9m5gvKK-QfI9bR-ZWnXFosLM4Aw_JWKXn2hT94sTyH3l9CYSsqXYqXIzZQrDO6FM3M3Ou09xx52CB6kypjWkLzKcszRUrhoVEkW3ZknIPgeZkD84pa32T1bt86D2DN_Ggy5JPpk3VNsvcQAKPF8gdC3sGhqtDh5lW6VGzrZF8han-lkhytlmfwSrBjweK2rexi4rCAK40CCMpE-UfQOpIMbZhkCNuwndIN6uv0s7vNIAEDHGxA6BIkC1VqYrOCaaJ3EkgNyxKHogU12Xek2iXToHi0RzYVk_PHWK6KoPhU2-5YG9OHiUbKTxxuo03nhIZa5n6xwJskhSGrhr0M0jedbm_HnTPOlKn6EANIuhG0SDLcrurtdFdd0Z6eI6tOM155s6_lCXvwByqYYXps7KH46V8I5hyq04mFZcvjzauvaHqy25fBGpW1V8bdRENls9MTh5jZIuyRphnshb7qqT0vhKcGswugTAyOJ2W0T9rVxeKzLyH5dLptfsRpKH5MXZSMkwhbaUhXWNVIlLrLtcd4LO7y0hF_9dgLchm-T1euETwO6NSPdIQ_57fHhP6p9H3QOQcj6qhr9ao5Bhw9DcGUb9QpjvFBDeueCusNziglIny1UkozFcmwMF6zX0WYMIDc6-dNmKBcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4952d610ef.mp4?token=OAhiAZ-QO6qb6dIlGeqx6hsMm8ubLc0h9m5gvKK-QfI9bR-ZWnXFosLM4Aw_JWKXn2hT94sTyH3l9CYSsqXYqXIzZQrDO6FM3M3Ou09xx52CB6kypjWkLzKcszRUrhoVEkW3ZknIPgeZkD84pa32T1bt86D2DN_Ggy5JPpk3VNsvcQAKPF8gdC3sGhqtDh5lW6VGzrZF8han-lkhytlmfwSrBjweK2rexi4rCAK40CCMpE-UfQOpIMbZhkCNuwndIN6uv0s7vNIAEDHGxA6BIkC1VqYrOCaaJ3EkgNyxKHogU12Xek2iXToHi0RzYVk_PHWK6KoPhU2-5YG9OHiUbKTxxuo03nhIZa5n6xwJskhSGrhr0M0jedbm_HnTPOlKn6EANIuhG0SDLcrurtdFdd0Z6eI6tOM155s6_lCXvwByqYYXps7KH46V8I5hyq04mFZcvjzauvaHqy25fBGpW1V8bdRENls9MTh5jZIuyRphnshb7qqT0vhKcGswugTAyOJ2W0T9rVxeKzLyH5dLptfsRpKH5MXZSMkwhbaUhXWNVIlLrLtcd4LO7y0hF_9dgLchm-T1euETwO6NSPdIQ_57fHhP6p9H3QOQcj6qhr9ao5Bhw9DcGUb9QpjvFBDeueCusNziglIny1UkozFcmwMF6zX0WYMIDc6-dNmKBcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی وایرال شده از عروس مسلح که در مراسم عروسی اقدام به تیراندازی هوایی کرد
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/693794" target="_blank">📅 22:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693793">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gszrx8DQIDktviCfP3m6RBFZNs6nKcLY1FhDV6iysOMcHBV6c0MYpyM8i3HnM3OMdCl5l-u5pEeajdoIJPftV6f0VBZ-Lv2tQfLfzct_bUOzgBLVJKB9YtUvWKekjr6dfvesOuJ0LvRh2xyYdujbCotPcS26IW6vvr0lq58r12_lnqCiHw4DUn073nLBloWPTf3skXANRQKaEDE2r3JyGps75M3eJZ2I10oeXgULdvBp2Vy3XI0u7u5YjmXUGuCyj3IDJK72KtQc4AuxnAjiUN7gfMS_OJakNfjVOg25pQ7lBqWZXq0EiFaxbeHT9ISCI5iYlb89J58G3Qm7CU5e4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
یه وام جدید منتظرته!
💰
✨
💼
مالی پلاس | خدمات تخصصی امتیاز وام
🔹
تأمین و واگذاری امتیاز وام
#رسالت
و
#مهر
🔹
مشاوره و راهنمایی تخصصی رایگان
🔹
همراهی و پیگیری تا مرحله دریافت وام
🔹
انجام امور با سرعت، دقت و انصاف
📌
مالی پلاس؛ همراه مطمئن شما در مسیر دریافت تسهیلات
🔗
عضویت در کانال مالی پلاس:
🌐
https://t.me/MaliPlus1</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/693793" target="_blank">📅 22:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693791">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLYggKHW2ByKdiErf3YWyU5Gx7GL8nTgoq1TGRm9TCjA1_pTOuuf8ChaPINndt6zve1xEPcklsrsd01nN-_U3cAy4cu5Joz2J_QWgaddXJ2_JKQFDUWp6jwWxysQho4sVCIOR4qa9CCbbN1qKxq1Nb9L9zchE-KIMH-FwaJk81NpmJzrHnb7uBeRd6jRX2ZrwPyaxdsHQzOhhiqymx0zpjzUSSEYC7nEQEuCCUMEnYXc1wBv7SwMls-DY6wo1uffXb-HdXhi-ni9GYIw0nbL8PuId-zOtczFuN6tzDfb3Huy02MNWuas5K_tEP0e7n7ptzHJQIRFRnl-CgKv4G3JVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام_رهبر_معظّم_انقلاب_به_مناسبت_هفته_دفاع_مقدس_و_سالگرد_شهادت_شهید.pdf</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/693791" target="_blank">📅 21:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693789">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6779a72c.mp4?token=nIdt56aD1cETPKC24oEQGF0i8uskyp44gxwAzepdpcWDHCPJi64LGYxVN7lDg70CnGO7ucySehCahgX31NWgyc9QW2CC8t07zqUPnYSxR61P19OgA_nQpNNmLe-tL7BQ4aakTcQY1inLCR-pa1YItOiFH2Pij9wg0Gk2xCcOBug3EJmV0pN244ubXVELAw2iHeviiokpU8nO9vlAs60Ng21qQa793ZArK4NVIxFG65ouQxdt-8bcEnk0m3QModgLmZP4y8A0Nc1ExjmAMmB5ZxIImD5suPTAK65KioQs0S2cs3JvdoPIJM51NxmV4v2IQPgB87x4VLLCzBc8epmNcTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6779a72c.mp4?token=nIdt56aD1cETPKC24oEQGF0i8uskyp44gxwAzepdpcWDHCPJi64LGYxVN7lDg70CnGO7ucySehCahgX31NWgyc9QW2CC8t07zqUPnYSxR61P19OgA_nQpNNmLe-tL7BQ4aakTcQY1inLCR-pa1YItOiFH2Pij9wg0Gk2xCcOBug3EJmV0pN244ubXVELAw2iHeviiokpU8nO9vlAs60Ng21qQa793ZArK4NVIxFG65ouQxdt-8bcEnk0m3QModgLmZP4y8A0Nc1ExjmAMmB5ZxIImD5suPTAK65KioQs0S2cs3JvdoPIJM51NxmV4v2IQPgB87x4VLLCzBc8epmNcTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴۰ کیلومتر تعقیب روی سقف خودرو؛ افسر پلیس هند برای توقف قاچاقچیان به باربند چسبید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/693789" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693788">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
منابع عراقی: ازسرگیری پروازها به ایران از فرودگاه نجف آغاز شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/693788" target="_blank">📅 21:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693787">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/693787" target="_blank">📅 21:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693786">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تامین تجهیزات مورد نیاز حدود ۶ هزار مدرسه برای نیروگاه خورشیدی
حمیدرضا خان‌محمدی، معاون وزیر آموزش و پرورش و رئیس سازمان نوسازی مدارس کشور در
#گفتگو
با خبرفوری:
🔹
متوسط هزینه احداث یک نیروگاه خورشیدی ۵ کیلوواتی متصل به شبکه در مدارس، حدود ۵۰۰ میلیون تومان و بسته به پراکندگی جغرافیایی و کیفیت تجهیزات اندکی کمتر برآورد می‌شود.
🔹
تاکنون تجهیزات مورد نیاز بیش از ۵۰ درصد مدارس تأمین شده و اجرای طرح، در چهار فاز برنامه‌ریزی شده و در صورت فراهم بودن شرایط، تلاش می‌شود هر ۱۲ هزار مدرسه هدف، تا پایان سال به نیروگاه خورشیدی مجهز و وارد مدار شوند.
@TV_Fori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/693786" target="_blank">📅 21:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693783">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3dc67a530.mp4?token=lwXP73Dpn1hCw_-Debi0XcrmSY8JdmZr5AgQmi_1X74ZnENlyzjr_7TczNUCv0ujyPJXw4FtolSFrjq9k3qraAYuFI6qCWjH8iaaizjjtTgxFVRxnIEOVR5a6-Ta2KOLhewCY8e0IssIFdvc49B8PIsH3x_WDEQexVhfw-Vcq-zHoQH_ECC__Lp4gRjCo6YklGoCUjqjck1k1C0_MXjvflhJuIjmcJqApHLYVX-US8FOPq1YLFQvucaZ_6aFYiFAWQoX3R0x7plndcT9ragU3shu4MGnFqPd7wNfglSmwnrhnPo_p1-p0D32hFsIOwMHw-Iz5RKFLpoP078IW3duww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3dc67a530.mp4?token=lwXP73Dpn1hCw_-Debi0XcrmSY8JdmZr5AgQmi_1X74ZnENlyzjr_7TczNUCv0ujyPJXw4FtolSFrjq9k3qraAYuFI6qCWjH8iaaizjjtTgxFVRxnIEOVR5a6-Ta2KOLhewCY8e0IssIFdvc49B8PIsH3x_WDEQexVhfw-Vcq-zHoQH_ECC__Lp4gRjCo6YklGoCUjqjck1k1C0_MXjvflhJuIjmcJqApHLYVX-US8FOPq1YLFQvucaZ_6aFYiFAWQoX3R0x7plndcT9ragU3shu4MGnFqPd7wNfglSmwnrhnPo_p1-p0D32hFsIOwMHw-Iz5RKFLpoP078IW3duww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در خط لوله انتقال گاز دیرالزور سوریه
🔹
یک انفجار شدید در خط لوله انتقال گاز در دیرالزور، سوریه، که در مجاورت مرز عراق قرار دارد، رخ داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/693783" target="_blank">📅 21:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693782">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
فعال شدن پدافند در شمال فلسطین اشغالی
🔹
ارتش اسرائیل: یک موشک رهگیر به سمت یک هدف هوایی مشکوک در منطقه‌ای که نیروهای ما در جنوب لبنان در حال فعالیت هستند، شلیک شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/693782" target="_blank">📅 21:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693781">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsAY4uXAbGGsZN9rNQaVzaVmQ82lw5Xu7Tj95h1H-Mnmo4JjsdgfoduuvnLETdTd3r3TI_lEGVYQrFAPyyn9dlLcLXpmoPMtc1WPClOuTDXg3X1_pm6_AHgondYMq4igC_iHs4A8xyPOB477O5dGt5Hstw--1mmqIC9qQKWE7TSwLYJxo6DPWhtC53uUk0imi6SCFsFGvkLBrjkN_m0Z7j1eu9lexE-476P33-9Cb2BjazmHv0T1H53kXEsRrhk-aVAAGM-jLSUXV6TAHD3nXYV0tEggapTMEZXblM5cmBzhW-CYGZeCpuiFSaU-oY58hpyu9z42WJXgC01WXkbozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین بارش استان‌ها در سال آبی ۱۴۰۴ - ۱۴۰۵
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/693781" target="_blank">📅 21:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693780">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
‌ حمایت سران حکومت عراق از بازگشایی فرودگاه نجف به‌روی پروازهای ایران
🔹
ریاست‌جمهوری، نخست‌وزیری و سران دو مجلس عراق از خواستۀ دولت این کشور برای معافیت فرودگاه نجف از توقف پروازهای ایرانی حمایت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/693780" target="_blank">📅 21:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693779">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5ZjcVZhQBn8yYE6m5oPYq8AphCqq_NyJo3Hl9bPLvb6gNUv3YWEgUY_s6k0Ns1H6JjiXoE27xNES8LNc3wVpw6DSUDfiVqCTCXSS0-IvzuxzIICiTc_VVk8lE5CU6qJTTAkWvmxGQj5XHxBGrO1UCTbUKAKZM8RhPJ6QWbGHn9yAUGDp6J47YK6SzLFefpWO6CEENjnYNU9SNpHURBt4LNxVEaRV7sPbitOEi9Z0gcT2oqFWQPekXsvbfID0S3tf6URFXnGU7fTDBbHFZrsxxBS2SMSDEJkHH3G8kTs6mBilrf8qRKSYfi0egfB6CVK9yju_Hgt4-qe8RbAQkewgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت قیمت نفت برنت؛ ۱۰۴ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/693779" target="_blank">📅 21:06 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693775">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqTSpnFE1xHQhwlgSKSBnFvQjOCPdQwMma_RDIgYTvVv_SpzuVe1HdEp_r9fvtCvFxIcuaVe-SgfGSZRvvu520i4NCxvVh_0tTSNZ88zZvUBQFJPG7tdPj6h-nJKbz5_7hbGi6EW5myjFvj-AXuI7N9BEiZ5WcHTAQpftMfmOSf4ftm7Pl_NsiO04mWEoxITyw8rdyJjQI8GIIwCjcvCQgJjAujFWC0bSKch-tTrzyDDJ8vJhl6Ksovi48wwBuC3X5Jet2XmquKBcm0-augF-kgL18V-LxxlUMHM7gl22_cKxpuY-BkJiJuhJSy2223md4ACysGkyNTCqGWqYCacCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIj_s8MNHCsqBXvfk8sUieO6pB68Lw8rZYpxXJwmR0hJ4QOC3FD_LfwwMzpuOKrC2VBnpXvgEbfnzFktUEUMH8Sm_uzLYJYl7tsc9WnRQoFvc1kvKhCeXZxOuz_ok9VS4JTBAd_zQ6Dvf55QHGmdt0AUGtJeU4y12O6RAcloOYc-G0PfklFPyvG043Gedx2dLRKQYEUtlpTtKVwEuRn12mcPD_UaBvwtSFcuxBpPoNT6j-60PIjdC4bGmlJ3QlhADDR3dzoOjpdnU0fjJFvD0mjWvBzA5JRP_bFs-nri35eLviYtvYhY8xz0w0BFrbkDW4VplReQtAR9ynpa1WFRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBUKn8RFJeasrGiDgls_ID59b5_WshOw6d6JK5yCqC48D5jqnhEM6kjCxEgGqhdfC9ZY1INXKOswh6leNuRqzUHbYWmWJ-lGkteVgJ2rLEUta3PUnJ54gr2EBBe1QSyf9kERxwVKBvdnoMWltitp_Sq3ZE6U1fWq4CVUP9ePk7QeqGTmLI2iUlEHy7dwhoTpnMLrf59YBnl-Rgldc4BWor_oNguHRXFbd2RyuEC-xW9WZUVt1eYI-O2qAGjHVoF09_c1leGs-FdZNpO08emsXOUanu9E0nG4T0RmwNlj9Pg1bN0TEcIy-3keqHVonZHJU6keFxAdDaSfv0G31BKTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/upwsQtEidjphZua3KGdDGUde1fNXyYmrOTAsvqe4zv7RgusEtO0a6biJTSpgg6qbsM53LLG2Bg_ZzN7HCuQmQZk8C6eOU7D9TCBM9MNFy5LgyP4CsPzqetFGIhRyfXIaxFQyI7sO231QGTuIXNbUitY_JS7uVGG58b3Bb7VhOhumY2aEUJXAmsBBT3hrj3E3rVQspHeNDAd_xBK2nvoCjl6w4I-EY37Cw53Qgy-r2Z4MLCV97V3RA9xD_Qjjkr91goWmH9uRPZvj5BlWswOHZYg8DvPrG7cOHV2Vg1jWClyC2VwfJMHEMq-1FlV243IZgePlXS3i3D-wOERloMvUfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵۶ کد مخفی چت‌جی‌پی‌تی که کمکت می‌کنه بهتر ازش استفاده کنی!
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/693775" target="_blank">📅 21:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693774">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzUt-My4CC5eja5t3V507m7H5zRBoun6CZfbn62OGEzes7lXBvVyx4LV_FOJGJNIivn4OxZBYU46_FrYLXUu5ELBWrzp2NRqdOFvIFDnDJ2B4shc-CquoiGNshXJbrG-xxQdLW5O9fW84KTOaClrH-ipQq1Aejk-7mUf1XqUC6wxZBOao8K7M8BSd4DyPYzaEG-2yD2-SqtW--Uy8AGZrKA8_5da3lw1U6aVeif2PQ8LpvhFMh-wsCGccQBLGR2iiJeJkq106SI981ZwHtivqqpFQULfYNYFFTGX7TJjCguJnAVplaoqZle0uH72XIKZtsKzHzPMtq5j1xyYFkIvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍃
☕
دومین جشنواره ملی رسانه‌ای چای؛ روایت  چای ایرانی!
🎥
📸
📝
محورهای جشنواره:
چای و تولید، اشتغال، هویت فرهنگی، سلامت، گردشگری، محیط زیست
بخش ویژه «نوغان و ابریشم؛ میراث ماندگار لاهیجان و گیلان»
⏳
آخرین مهلت ارسال آثار: ۱۰ مهر ۱۴۰۵
🏆
اختتامیه: ۲۳ مهر ۱۴۰۵
📲
آثار خود را در قالب‌های مختلف از طریق سامانه زیر ارسال کنید:
🔗
pressfestival.ir
#جشنواره_ملی_رسانه_ای_چای</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/693774" target="_blank">📅 21:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693773">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل ادعا کرد:دیدار نتانیاهو با رئیس‌جمهور امارات حدود شش ساعت به طول انجامید و تمرکز اصلی آن بر روی جنگ آتی با ایران بود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/693773" target="_blank">📅 20:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693772">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6ad181ed.mp4?token=tjGlbs4SdCcHmZPX4sbuU3W9VJcLIWgukpD0-agGQXH2E2JMMPFALdh8vTi4LqGDXW2vD09sprsNv8uo5JyKoDAJVofTkDdXpZC3Gg7IDD8qfIx-ZkC1PCJqb_G4CLKeh4zDgXNrL6z5QkT9G34ei8U7R_5PxO7d13zZpE-M3ognvolVzssmgmjOADluinl-oRbrrsE-Awo8_SC7QpQ4WkU8LOnOwnqa6dxjdb5GrUGwYBVEdp5Va9vG4pl8FsiWX2zPLl9-D_OpvGHnTYm3H73kK2DLwWExydzoX8G9BE-o3LOCXOHSn0fBtqFrO5U0GQZvi3w9_1dGIqhbQPZu75a8WByokmkpDlJ0eCmEem-VtJlbnUmWzw0TRCeXX3nQ4CsCUaN17AKAwmSktmi_pxk41f2_H-j1r-L9JILKxJhCtq1R0wy7pq3YdGEARHPpq9Gt_5sv9FpZlQJsoGjzQr46-43td5552eI1SdTZsxVNlRHikR6E4w9HUaDI9uZgajUMz4pe9IHtAohptRu74vcrxmYURrjcl3n9rx6Z77QGsI7ySbXVihJpinesVt6pokyHBmy8T07Q19p2ElOiMToo3leD9tB7nJ9eQdnoIHCuFdyZ9ytSvbsR14tejvueiHo8gNZH6h8WtRoEodG459FH2JIwdx_LBG-23Q2Dfd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6ad181ed.mp4?token=tjGlbs4SdCcHmZPX4sbuU3W9VJcLIWgukpD0-agGQXH2E2JMMPFALdh8vTi4LqGDXW2vD09sprsNv8uo5JyKoDAJVofTkDdXpZC3Gg7IDD8qfIx-ZkC1PCJqb_G4CLKeh4zDgXNrL6z5QkT9G34ei8U7R_5PxO7d13zZpE-M3ognvolVzssmgmjOADluinl-oRbrrsE-Awo8_SC7QpQ4WkU8LOnOwnqa6dxjdb5GrUGwYBVEdp5Va9vG4pl8FsiWX2zPLl9-D_OpvGHnTYm3H73kK2DLwWExydzoX8G9BE-o3LOCXOHSn0fBtqFrO5U0GQZvi3w9_1dGIqhbQPZu75a8WByokmkpDlJ0eCmEem-VtJlbnUmWzw0TRCeXX3nQ4CsCUaN17AKAwmSktmi_pxk41f2_H-j1r-L9JILKxJhCtq1R0wy7pq3YdGEARHPpq9Gt_5sv9FpZlQJsoGjzQr46-43td5552eI1SdTZsxVNlRHikR6E4w9HUaDI9uZgajUMz4pe9IHtAohptRu74vcrxmYURrjcl3n9rx6Z77QGsI7ySbXVihJpinesVt6pokyHBmy8T07Q19p2ElOiMToo3leD9tB7nJ9eQdnoIHCuFdyZ9ytSvbsR14tejvueiHo8gNZH6h8WtRoEodG459FH2JIwdx_LBG-23Q2Dfd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمید رسایی: نه شرمنده‌ام و نه عذرخواهی می‌کنم؛ بلکه در برابر این ملت باعظمت، سربلندم؛ کسانی باید شرمنده باشند که کودتا می‌کنند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/693772" target="_blank">📅 20:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693771">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/693771" target="_blank">📅 20:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693770">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dce2a39e9.mp4?token=htgquutX0XV1-qlh3JIWSqVDMM3xmRhSAwO2h1hHI2tFSUyqd2lSGBPZiev9xDKNaN6gfl-SZEoiaUWyd1zGY9N-eUX4nburEXqJvXYPtM57VWHXlWKCq2DFGArDvcja01yi8qC6RDKFq8eipawIQy0wHgajAJr1DTyvjCM_Ys64QJsW0FJnYqDEqy7EpCdVJqJd-gdbYu0zdQSDtWZjHB7qvfOgBxedaeXBem5aXKt9_11BXNjNDT2dxmLvDUigtPhNWBbcsVRTQUT0CXGop5ECln0A4gW_kytiOizL9ed6uDPDfEQf0kbZMT9jWjV3jP8dJRk0TR-vKNw7p9w6kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dce2a39e9.mp4?token=htgquutX0XV1-qlh3JIWSqVDMM3xmRhSAwO2h1hHI2tFSUyqd2lSGBPZiev9xDKNaN6gfl-SZEoiaUWyd1zGY9N-eUX4nburEXqJvXYPtM57VWHXlWKCq2DFGArDvcja01yi8qC6RDKFq8eipawIQy0wHgajAJr1DTyvjCM_Ys64QJsW0FJnYqDEqy7EpCdVJqJd-gdbYu0zdQSDtWZjHB7qvfOgBxedaeXBem5aXKt9_11BXNjNDT2dxmLvDUigtPhNWBbcsVRTQUT0CXGop5ECln0A4gW_kytiOizL9ed6uDPDfEQf0kbZMT9jWjV3jP8dJRk0TR-vKNw7p9w6kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آجرلو عضو کمیته رسانه تیم مذاکره‌کننده: چین به ایران گفته مسائل‌تان را حل کنید و این جنگ بالاخره باید فیصله پیدا کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/693770" target="_blank">📅 20:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693769">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رسانه عبری: دو اسکادران جنگنده آمریکایی وارد پایگاه عوودا در جنوب فلسطین اشغالی شدند
🔹
شبکه ۱۲ تلویزیون رژیم صهیونیستی گزارش داد دو اسکادران جنگنده آمریکایی طی ۲۴ ساعت گذشته وارد پایگاه هوایی عوودا در جنوب اراضی اشغالی شده‌اند که استقرار این جنگنده‌ها در چارچوب تحرکات هوایی آمریکا در منطقه انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/693769" target="_blank">📅 20:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693768">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
یک مقام آمریکایی در گفتگو با سی‌ان‌ان: مذاکرات مثبت و سازنده‌ای را از طریق میانجی‌ها با ایران دنبال می‌کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/693768" target="_blank">📅 20:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693767">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Live stream finished (1 hour)</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/693767" target="_blank">📅 20:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693766">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d5bbbe83d.mp4?token=qQS5wcYimY7OHctDhFR01tlrVdinz06HsJRrADN1UlDGg0B_3_3jffMYm2tm3yJvW_nzcH_AbSxY5oMWc9eQqOfmADvCHy7S9XYQQlnehzaaOjyMLyWIMmFywHaQpBecT6rScb8qZRZoGK7IQmMrrIQDC8BeU3Bhirdt15heMa2snuM1-ty6AHDUa9ZcI59aZkGQwkEaR71ipR1XM3Ny_a6qNwRQRgmbfs76UaQlTVD6L-bRCfPipLkDNSv9RwtJ9jxlykgszqs0FyBZeer5X1okv3tJjY1QS1eFMJPM3HzT5T9kxT1bRO5Kf7TnZ0d_HdpsHdz5MPNP9rv8J9vrOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d5bbbe83d.mp4?token=qQS5wcYimY7OHctDhFR01tlrVdinz06HsJRrADN1UlDGg0B_3_3jffMYm2tm3yJvW_nzcH_AbSxY5oMWc9eQqOfmADvCHy7S9XYQQlnehzaaOjyMLyWIMmFywHaQpBecT6rScb8qZRZoGK7IQmMrrIQDC8BeU3Bhirdt15heMa2snuM1-ty6AHDUa9ZcI59aZkGQwkEaR71ipR1XM3Ny_a6qNwRQRgmbfs76UaQlTVD6L-bRCfPipLkDNSv9RwtJ9jxlykgszqs0FyBZeer5X1okv3tJjY1QS1eFMJPM3HzT5T9kxT1bRO5Kf7TnZ0d_HdpsHdz5MPNP9rv8J9vrOoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده انتظامی کردستان دستور رسیدگی به برخورد غیرحرفه‌ای یک مامور را صادر کرد
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/693766" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693765">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای دروغ اینترنشنال درباره تجمع دانشجویان دانشگاه علامه
🔹
رسانه ضدایرانی اینترنشال کلیپی قدیمی را به عنوان تجمع امروز دانشجویان دانشگاه علامه منتشر کرده است. این کلیپ هیچ ارتباطی با تجمع امروز نداشته است.
🔹
این تجمع در حیاط دانشگاه برگزار شده و عمدتاً شعارهای مربوط به مسائل اقتصادی و اعتراض به افزایش هزینه خدمات دانشجویی برای سنواتی‌ها بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/693765" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693764">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8032c7661f.mp4?token=ZQlZt8Ot88AIuS5_egkEhPU-_kVGV184vB0nWXn5HoPWx-3OZg_k3WqSG-Sbw4QTG5owHepDHCtDk5b3P3uHmwFEGTrgI_KQc7elX6-amaMH_dxDuPtpd0s4mPBFNaio44gtOZmX0q4JziFdsP5NlbAfsd5uXwLv7f1yM0HFpFKBxj0zBuaB8YFo94N3GbO2FE6h3m54IPb7wf-SzraPHTcaSXDUaH9Kr8JYCfCC_--kX4GluezqQik7FpGj2ElWBiKeogF1TFwLy0eRc234Sn_3nTR-kiZi8ZF6Cgu-oDnVifhaVX6x-NAR00qaAmZBPQ4l0avzV6zsKjm4p2qxfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8032c7661f.mp4?token=ZQlZt8Ot88AIuS5_egkEhPU-_kVGV184vB0nWXn5HoPWx-3OZg_k3WqSG-Sbw4QTG5owHepDHCtDk5b3P3uHmwFEGTrgI_KQc7elX6-amaMH_dxDuPtpd0s4mPBFNaio44gtOZmX0q4JziFdsP5NlbAfsd5uXwLv7f1yM0HFpFKBxj0zBuaB8YFo94N3GbO2FE6h3m54IPb7wf-SzraPHTcaSXDUaH9Kr8JYCfCC_--kX4GluezqQik7FpGj2ElWBiKeogF1TFwLy0eRc234Sn_3nTR-kiZi8ZF6Cgu-oDnVifhaVX6x-NAR00qaAmZBPQ4l0avzV6zsKjm4p2qxfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رانش هولناک زمین در نپال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/693764" target="_blank">📅 20:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693763">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyxjgGJKbajQO1PmDpVkGBo3a4UAUg5bjrudJBjpOGHlii-niJfjNC5YGruABATp9KBKDNiHe9rZkUm1b8ZKmgLocQHrkyERk11xSKEEOWIA0_sL2yC1I15n13FkzRG-CVkxt0WjAUxBRNxpoIbuyv5swaTilQwOp2RUjE3u2R2aEc5XQyTFKHMtFeuiiGP9YmF0LAT1mS2muzFFCJsfK4PckRMNIuuldUY6D1ctkwXY372-KmVleKW9IwiLvHfAkxArRE-H9xI6bg3aZcMljpT1ZqjceL6Jw1CYey5A3rO3npWqS-KZIQxczV6l8HU8CNAUAOa6TtWNV1BLH7OLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصلاح تعرفه‌ها، راه تداوم سرمایه‌گذاری اپراتورها
🔹
علی حکیم‌جوادی، رئیس سازمان نظام صنفی رایانه‌ای کشور، با اشاره به افزایش هزینه‌های توسعه و نگهداری شبکه، اصلاح تعرفه اینترنت و مکالمات سیار را برای تداوم فعالیت و سرمایه‌گذاری اپراتورها ضروری دانست.
🔹
افزایش هزینه تجهیزات، نوسازی و توسعه زیرساخت‌ها به‌دلیل نوسانات ارزی، در کنار رشد هزینه نیروی انسانی و تجهیزات داخلی، فشار مالی قابل‌توجهی به اپراتورها وارد کرده است.
🔹
ادامه ارائه خدمات باکیفیت و سرمایه‌گذاری در شبکه، بدون بازنگری و متناسب‌سازی تعرفه‌ها با چالش‌های جدی روبه‌رو خواهد شد./ تابناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/693763" target="_blank">📅 20:32 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693762">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fd7004a9c3.mp4?token=JD2cT6NyP2sz9SDoUjYHiCE6b4n1CjuRb7tSyBUJFuEk9T2HiRUCPbS4e2RrF87gKWH3Wjl65Z85Y5Nh0rION1Mt_waE3iw_8p9qkczoFLPNzAXt7q2HsdJvURl54uLS39dL1XJal4oN8IMS8Edn55302ftHFZ5OTj-BgvuIezwlEM_BROm_QXdLfGgyKJ9x-7qkt_0IlT1X-5gtOItEVOSocNgiA2MybWHK0ccPD0pQMVmNlJlYDj_X8J5tG9KmcJxuNszwiwcpJLs1DmV46RHBH51qeo7E-BeyiEBBLQdMuouWTSftUvvXEZJmAapOyst2utzF71V0n0WI5tNsYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fd7004a9c3.mp4?token=JD2cT6NyP2sz9SDoUjYHiCE6b4n1CjuRb7tSyBUJFuEk9T2HiRUCPbS4e2RrF87gKWH3Wjl65Z85Y5Nh0rION1Mt_waE3iw_8p9qkczoFLPNzAXt7q2HsdJvURl54uLS39dL1XJal4oN8IMS8Edn55302ftHFZ5OTj-BgvuIezwlEM_BROm_QXdLfGgyKJ9x-7qkt_0IlT1X-5gtOItEVOSocNgiA2MybWHK0ccPD0pQMVmNlJlYDj_X8J5tG9KmcJxuNszwiwcpJLs1DmV46RHBH51qeo7E-BeyiEBBLQdMuouWTSftUvvXEZJmAapOyst2utzF71V0n0WI5tNsYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه گویی نماینده رژیم صهیونیستی در شورای امنیت: ایران به حماس آموزش و امکانات داد تا به رژیم صهیونیستی حمله کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/693762" target="_blank">📅 20:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693760">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
منابع عربی: آمریکا در حال بررسی معافیت از تحریم‌ها برای پروازهای بین ایران و شهر نجف است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/693760" target="_blank">📅 20:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693759">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
تظاهرات در استان نجف عراق در اعتراض به ممنوعیت پرواز هواپیمای‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/693759" target="_blank">📅 20:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693758">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
تبدیل پلاستیک به سوخت هیدروژنی با کمک نور خورشید
🔹
پژوهشگران سامانه‌ای طراحی کرده‌اند که با استفاده از نور خورشید، بطری‌های پلاستیکی را تجزیه و از آن‌ها هیدروژن تولید می‌کند.
🔹
این فناوری می‌تواند هم‌زمان به کاهش زباله‌های پلاستیکی و تولید سوخت پاک کمک کند؛ در حالی که بیش از ۹۹ درصد هیدروژن فعلی جهان از سوخت‌های فسیلی تولید می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/693758" target="_blank">📅 20:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693757">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL5N4UthS33XjB3_InB_EXEmzzFXdzVdDRwbE9bf4yWCD1hY9K5vKE5RIHI4kKkwOZDVR8jna5QCpJYvmXBX2-wqDM4AFF_M4gS3iL0B3hzs51BZ4pmtvnusiKP5SAlgjdUOKHQTzLaFvcSal73G__RUJu6GreT9ApLg1bTwqaf3GRDGKsAQntToeRQIT_cL3To6DX0jT3XP8KKbz_fyQgPVAJc-NxaiWl13tnrXJpECto4sLsW--2lSDeWPJBCHzLDrDHbOse6a8ZiDuzIfUDMG4C1VhAaNnes8-s4-a9y9OtCi3pnUTG63VldtbJS7O_lye88FZCDxl5Vnlf22cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاییز شگفت‌انگیز جاده چالوس
🍁
🍂
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/693757" target="_blank">📅 20:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693756">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">19-2 Ane Manaee (1404-02-06)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/693756" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه نوزدهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
خاطره‌ای از علامه جعفری و سبک اخلاقی و معرفتی کم‌نظیر ایشان [00:00]
🔹
از نشانه‌های رشد انسان، تسلیم شدن در برابر حق است نه توجیه و فرافکنی [05:45]
🔹
نقد فیلم "مصلحت" و حساسیت انتخاب در بزنگاه حقیقت و مصلحت! [11:47]
🔹
آنجا که حق، قربانیِ طیف و تعلق ‌شود؛ بیماردل از مؤمن تفکیک می‌شود [16:20]
🔹
اجماع، مسلّمات و فقه، ابزار قدرتند در دینِ گزینشی برای منفعت طلبی! [24:43]
🔹
نفی قضاوت‌های سطحی و ناعادلانه؛ روایت قضاوت یک طرفه حضرت داوود علیه السلام و توبیخ الهی [36:18]
🔹
دوگانه "هُدی یا هَوی"، سنگ محک پیروی از هدایت یا منفعت [42:12]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/693756" target="_blank">📅 20:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693755">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLbtezHuUkW2GgQ5cyDq2zhyR3tNzPDi5ef3q-wKIrAPLiuP3JFtEp_F2s0QrXhBv66mxhbXdO23V3HlaiOBvO_pQ5ZwFtdIUE_JxSWqrZC2e9jZd_QBP1lUEd8hEld3TiGk3mgopUaVU21Gh-_5rdw26tE5tQLNrPBRG8DwJuHL00Z3-R6JPGgrnRXHB5gNx3m3dRl-UEd_XfxtsC1wsrAuG_iBHD3SQH0EiA7LMYDaevhAXC5QT5lJJ7zZj1CVZYArzYCRIUMVs5svn8oYAbBGhNJ9k6nUQ_aV3-0vjIB-meTfUod_EKN0NdvcUlQbHNqBuM8OqhrHn0C-h5FLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار آکسیوس: یک مقام آمریکایی به من گفت ترامپ مایل است در ازای پیشرفت ملموس در پرونده هسته‌ای، تحریم‌های ایران را لغو و دارایی‌های مسدود شده این کشور را آزاد کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/693755" target="_blank">📅 20:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693754">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbPheh9JbWmKBd6QxtaaoPIrciGhyyccflCmBQKI0I1Hbief27XP2YtTpPngH7cdxZevbXjBn7iPrNIgOEMd-46F6Z-cj3lEOr9UW5riOvzafpOEq072bTVLvO003u5NNs90EBhLAZ1vdO7Y1GitfcQyPa9uTMWSExAcNIXHVXbhrNBox7BonqhX3zYJyoED4E_UIMlmdLyHdhQI2W2qlAfwoNa38cEtz6zn3GRd91S26KGPGEUuDqgMPm-1qBqEPurqYM0xLtlA6qbLfjdGmJlNwRBpZi2H-rAJHY3QxGlOcw8Do1QrNfH9VtSp9jhP6vBOQ-h_4fK9XGo7nkLeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این فرصت را از دست ندهید
❗️
اگر برای معرفی
برند، محصول یا خدمات
خود به دنبال دیده‌شدن گسترده‌تر هستید
با ما همرا باشید
🔥
۵۰٪ تخفیف ویژه تبلیغات در تلگرام
📣
پکیج تبلیغاتی گسترده در
۳۴ کانال تلگرامی
👥
دسترسی به بیش از
۱۴.۶ میلیون مخاطب
📞
دریافت جزئیات و رزرو پکیج:
09923104314
📲
ارتباط مستقیم:
t.me/Farahmand_p</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/693754" target="_blank">📅 20:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693753">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sR5l8VW-E9j_PpbMAGwRQHYF8Gk85BpyqwzHmRhUJS_H_Tc62tg_StJ5kRm4VTZW4yDxXX9Zq3zdWUNnvqsEJlLVO79zqbsy4JOOGFMuIGoOb0E9VeyzhVYq1zFQznEFQuf7uWnTfKNz-61VZVVnvV59j3EAwXyGDlrQCAozZDxPui4lXA4i9MPf_AHYlcQf--iSeqQ81FltKMQmUvEZSmD2EOBhFT26hYXkbZ8F2VGvfZ-sC1I78zfFDyoolGXF7g2yyF-vIL4zbOZyekwd07Br9vCWetSVAJ4zlhYTV2OzWYYPU9fHiXmPMLfGJ7VmKvIzBtHKC1Lt7sDJv-A1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥾
نیم‌بوت مشکی مردانه مدل Sorush
یه انتخاب شیک و کاربردی برای روزهای خنک و بارونی پاییز و زمستون
🍂
✔️
رویه چرم مصنوعی
✔️
زیره PU
✔️
کفی پرسی و دوردوزی‌شده
✔️
سایز ۴۰ تا ۴۴
🖤
رنگ: مشکی
🔥
قیمت: ۱,۸۵۸,۰۰۰ تومان
💳
قسطی هم می‌تونید بخرید:
۴ قسط ۵۲۵ هزار تومانی
یا اگر راحت‌ترید،
پرداخت کامل درب منزل
انجام بدید.
🔄
ضمانت تعویض ۳ روزه کالا
https://memarket24.ir/product/brief/63746/180124/</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/693753" target="_blank">📅 20:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693752">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای یک مقام آمریکایی به الجزیره: ما از طریق واسطه‌ها به مذاکرات مثبت با ایران ادامه می‌دهیم و بدون پرداختن به مسئله هسته‌ای هیچ توافقی حاصل نخواهد شد
🔹
ترامپ آماده است تا در ازای پیشرفت در مسئله هسته‌ای، تحریم‌های ایران را کاهش داده و دارایی‌های مسدود شده این کشور را آزاد کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/693752" target="_blank">📅 19:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693751">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMwyW4VSSnJjCbggF_viQUl86APUVt9kYPQTK8IYahGQUFANxR5CMefcQb08T9u13iDC2Kz0rNDFSJkqGiTp5kV9SgsfjGeOM2gsoa0eUHYh2LcE8WQccPRe8y-75Tue9z0IFhJ119CJV2rSVnUjyFZL8qGWIcvVTdU635IujLjdu8I1iQZ7Vwj4ETc_gNgH0Fb-oOv3RYirhLgcq7BU10zahQ4FhEvoz9Nv5lR40-K0OLFOEdp1QGLZu5QfH9ad95wiz4bmdLWPGCwPOgKlkcO1T2tbF5EIuoa25xel0rs0jnBsyCX5wzJU5hlIb1nbP5Wq55jtGijgKrwrM2xUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«مرد عنکبوتی»؛ مارمولکی با سرخ و آبی خیره‌کننده
🦎
🔹
اگامای صخره‌ای لکه‌قرمز به‌دلیل تضاد رنگ قرمز سر و بدن آبی‌اش، یکی از مشهورترین مارمولک‌های جهان و معروف به «مرد عنکبوتی» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/693751" target="_blank">📅 19:53 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693750">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
سامانه واردات خودروی ایرانیان خارج از کشور غیرفعال شد
کنسولگری ایران در دبی:
🔹
بخش انتقال خودرو در سامانه «میخک» موقتاً از دسترس خارج شده و صدور کد رهگیری این بخش امکان‌پذیر نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/693750" target="_blank">📅 19:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693748">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
عراقچی امروز در نیویورک با میانجی قطری درباره پیام‌های ایران و آمریکا و شروط هفت‌گانه تهران برای بازگشایی تنگه هرمز دیدار می‌کند
🔹
یک منبع نزدیک به هیئت ایرانی نیز گفت برنامه‌ای برای مذاکره مستقیم با آمریکا وجود ندارد./ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/693748" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693747">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS_A0Q_mrOdVKI_GNxBFAzZ8jSbJD8hg7ajRCBbEWb6wtD5A9MqyU2BMuWnQ7x6CdoNyOUp4K6sUOryAQqyOWvrIHQbpwY6140lpix-Ei4K5c_FN9UNOe_LsrB1t8KyRIk1frVNW8ZzCvjgH5pDH06D0OPs0EnH2qLFp33EB2G287GFDszEwWPSMrmJzlrMrVLMpJBuG1FIgYDBLiIvLgDU8x4V9uWPQW0N0mOMe9Cf0FQwxcJ6vtDogVJUjU6Og_3Yt3zAflIPTgh5c13O9aXnsQymzgcRW5jzGCO15vTBnHk4LJMg9U9waAEGfB7vARqxMXcDq9wxJncIXx7RFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثبت بی‌نظیر از لک‌لکی در لانه‌، در غروب دزفول
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/693747" target="_blank">📅 19:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693746">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای دریافت ۶۰۰ میلیون تومان زیرمیزی برای یک عمل!
محمد شریفی مقدم، دبیرکل خانه پرستار در
#گفتگو
با خبرفوری:
🔹
دریافت مبالغ خارج از تعرفه به یک یا چند مورد محدود نیست و در برخی خدمات درمانی از چند ده میلیون تا چند صد میلیون تومان مطالبه می‌شود.
🔹
یک بیمار شهرستانی برای انجام عمل به بیمارستان دولتی مراجعه کرده و جراح برای انجام عمل مبلغ ۶۰۰ میلیون تومان به‌صورت خصوصی مطالبه کرده است.
🔹
در برخی بیمارستان‌های دولتی بخشی از اعمال توسط رزیدنت یا فلو انجام می‌شود، درحالی که پرداخت‌های اصلی به نام پزشک متخصص انجام می‌گیرد.
🔹
خواستار ورود دستگاه‌های نظارتی و بررسی شفاف پرداخت‌ها و منابع مالی نظام سلامت هستیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/693746" target="_blank">📅 19:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693745">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادامه کاهش ذخایر راهبردی نفت آمریکا
🔹
ذخایر راهبردی نفت آمریکا تا ۲۵ سپتامبر به ۲.۸۳۸ میلیارد بشکه کاهش یافت که پایین‌ترین سطح از اکتبر ۱۹۸۲ است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/693745" target="_blank">📅 19:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693743">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odChW0EE0tO20Ol7F0uwwU48a4I-aK4IL8KuFBB4Bj3qdnTh4FQVrxQovK448nyCSRBknyxrLnFkUk7SbwQk8pFnsZhvUmNbGl7p4JAoYzqAnPc7qUeHBSn-rSHsz2hDZGz3fQbQiPMV5YuMjg17gfEr1pNVdYwSAb1ZGvvRZtEu0y64_cDIRQifW1IK56iLcFCYgElcTKx7qdiJ1KCx3e4egsp-_kMKe8kNrpUlZ8nettst6qhfqUWGnQ_S8JyaQ556hxmle5SEbRCLEFhEPe5I47ciMOEx9sEw_UGrUskaLFFFqWAiyJo0dZI5LG5qfor0Dq1yH9WsxIEgDz9Fyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون وزیر جنگ آمریکا استعفا داد
🔹
سی‌ان‌ان استعفای «دنیل دریسکول» معاون وزیر جنگ آمریکا در امور ارتش، بعد از ماه‌ها اختلاف با رئیس پنتاگون خبر داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/693743" target="_blank">📅 19:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693741">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سازمان هواپیمایی کشوری: ایران با هماهنگی وزارت امور خارجه، اعتراض رسمی خود به محدودیت‌های اعمال‌شده علیه صنعت هوانوردی کشور را به سازمان بین‌المللی هوانوردی کشوری (ایکائو) ارسال کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/693741" target="_blank">📅 19:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693740">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faddf05fe0.mp4?token=WIC5wM3edE8wxX35lUZtPrtu9UHcux9zEfRHHlPJOSxnpTk0-rQmWwMZ6YUSOrvBvUEAYuXB7kpLKD9aeU4W1epW5IgCLTxnqEeHKMRJnJcFPymE4g0biKxLWUu_RZMyoXVtethBOynNfTmJ0cDOIECKVGB8PHI0mB2nbxmwR9c211G5K5a_Xxp_YzbBjevntoKCaWvi1ayUCmC2gIVM2Vhw6_jyJAEI80EyWxAo_dBhsXxKMr1c6IB7nRWoIyUVpPmN-KWdhkaVJS8_3Yp8V584Cl5Q6W8gyyEpI49abSzdnU3yFFp2tIxCtN2fO_BCLYZQInFE9M7RsBD0v5TphQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faddf05fe0.mp4?token=WIC5wM3edE8wxX35lUZtPrtu9UHcux9zEfRHHlPJOSxnpTk0-rQmWwMZ6YUSOrvBvUEAYuXB7kpLKD9aeU4W1epW5IgCLTxnqEeHKMRJnJcFPymE4g0biKxLWUu_RZMyoXVtethBOynNfTmJ0cDOIECKVGB8PHI0mB2nbxmwR9c211G5K5a_Xxp_YzbBjevntoKCaWvi1ayUCmC2gIVM2Vhw6_jyJAEI80EyWxAo_dBhsXxKMr1c6IB7nRWoIyUVpPmN-KWdhkaVJS8_3Yp8V584Cl5Q6W8gyyEpI49abSzdnU3yFFp2tIxCtN2fO_BCLYZQInFE9M7RsBD0v5TphQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین اتاق دنیا؛ جایی که پژواک ناپدید می‌شود!
🔹
اتاق‌های بی‌پژواک با جذب امواج صوتی، بازتاب صدا را به حداقل می‌رسانند؛ به‌طوری‌که افراد ممکن است صدای تنفس و ضربان قلب خود را واضح‌تر بشنوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/693740" target="_blank">📅 19:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693739">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3168aaef59.mp4?token=AzbuPLdHWeUuu1nUmzo3tPjSr9prNGUvTe6zuAclGkvnUnoL6Ic8GUQ33sJ0L7HVd92CI9vGemfZeBW8o3EcnZKdlph2JYF78U0cMfELJuwhokw7j2fJWgT5yutlzOjM6AnGcsAteIOhoPFE-h2vjZP_9gvI9E28-csbmi_3jB73ewKy4a-Z_X7x81qZro4QiEGCfhpzqeDjCYPGCMZCARoOHmg5OQ32RziYuqRz5ktLwFiTNlDSwTena1F9O_zpXTk1K1UqsGcy-TxH2QVvB2Yceahrm-MvVUcmWvbIZcq1twCwo5_eCgV5R7J-gudR1F8RNbizWikUDLEXwdddxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3168aaef59.mp4?token=AzbuPLdHWeUuu1nUmzo3tPjSr9prNGUvTe6zuAclGkvnUnoL6Ic8GUQ33sJ0L7HVd92CI9vGemfZeBW8o3EcnZKdlph2JYF78U0cMfELJuwhokw7j2fJWgT5yutlzOjM6AnGcsAteIOhoPFE-h2vjZP_9gvI9E28-csbmi_3jB73ewKy4a-Z_X7x81qZro4QiEGCfhpzqeDjCYPGCMZCARoOHmg5OQ32RziYuqRz5ktLwFiTNlDSwTena1F9O_zpXTk1K1UqsGcy-TxH2QVvB2Yceahrm-MvVUcmWvbIZcq1twCwo5_eCgV5R7J-gudR1F8RNbizWikUDLEXwdddxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از عجایب رشت که از درخت نخل یک درخت انجیر رشد کرده است
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/693739" target="_blank">📅 18:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693737">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dmp1G1N7sH5KZVeQHzNR3USGFbvTR-wsLbL6ARUnq32r3O5-fhhFg-dU4Bl4EXntZhjKzcnAll2z604UJ6TlciFpkqFubsGkQ0Uk__VD8n71yjKzOIjv-V_DmJ9JT-hQHm6t0ejozBxOz5bDeGsR_QtQ6RWPKSM5-hTsE5Djuphs-eMJY5MiQ_G4cz3GuTkwZxizvW9yj5hTGQXb1mi0L0V0ebOypfqHBTny5eqZALTCEQEYFz--N6qEDfsVKCE44vRHWehUwdpd1xgAdskWP4powwMcZrVE9FZNcp6SlDM-9fSP3bTw-09NpTyAbD_H-hQKl4SuCBZJVyRaD-rqmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qte_Z56Q432qXwOioqYCHp5nblMsswpiOqhywP4bMnNRQgn8lco1MAiksXkyKZ3kvjiPGz9AIZWHR1848GEpcCN0SbCXpeidfumcW4ZgLD-J3gXcbqtOdLZW1C20anddevIBkh0JjqblQjNKKAxQwzIbDDpLP21XruUDCqgJm6luBXkA2aset4zcopCoZ3FOMlHwq3ooM3e28GU2mnD3rFzwV-kuud05Osv0aeD3E0ynSR1ncqNATyGG3SsghEaxchnVOxs4H6CnPmQbCFhz7AurHhG5i168BfycezUgKtFXMyIf2frCRTh3IrXeTLtH1BmLuLy8Fj5FN9A2QOaI6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
امروز روز خوبی برای طلا و نقره جهانی نیست
🔹
طلا و نقره امروز مجموعاً ۱.۲ تریلیون دلار از ارزش بازار خود را از دست داده‌اند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/693737" target="_blank">📅 18:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693736">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruO_Wek4YinIvygRed_qknHs887YtqZv_lEAB5qI40fgAkz7xMCFyR_CSGgWm5rdFv5VNgrPoTTsy7wP3mh0RxiE3St29KCnm25Dttv2bzZllj6bz1hs9j9HT_2_xCif2UmH9dKUkdVxdjsjzrqriDT0tgqZixU9EE8p72GWC3LV6v7RSeR81K78Wo-t9SoGAvFle_dluSilq1eva2M_2p4ZxeAVvm8JouwADvo58rpkjD9OUAxVs5rvrATsWWjVXnxSBiWAwAS4TBvQlWxpHA_FeJouIfGhpsB_ao7Co9NIwdqP8tC4sys6AAmmrO5FIGuXx1PhgXQraQru5YmV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیابان آتاکاما در شیلی، خشک‌ترین بیابان جهان، به‌دلیل بارش‌های شدید ناشی از پدیده «ال‌نینو» به مزرعه گل تبدیل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/693736" target="_blank">📅 18:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693735">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
پرونده قطر برای اسرائیل باز شد
🔹
قطر از میانجی مذاکرات به یک کارت سیاسی در انتخابات اسرائیل تبدیل شده است.اما این کارت به کجا خواهد رسید فشار سیاسی یا جنگ؟
🔹
جزئیات را در این ویدئو ببینید
@TV_Fori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/693735" target="_blank">📅 18:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693732">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/693732" target="_blank">📅 18:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693731">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
عراقچی امروز جلسه‌ای را تنها با میانجی‌گران برگزار می‌کند و قرار بر مذاکره با آمریکا نیست/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/693731" target="_blank">📅 18:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693730">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0e414fe.mp4?token=SH7gParEXaE0MkdBxzT4l59trKRFhle_9aWjET9eeLh2uidmIe9Z9BWehmtLDITlfW12raY1jLezE2uK2hZk3eCMRxOPBdIyean_NNAoypS2YflmsEuMxXy268VDiTN9IhKuA0jtwa-fupCMt-QiSIuE6PgPwuMecmSLMelT-CkQsbxtwdAfM1uk3AlGCc7cbQ9gWH0e1El6kXeIcH8uPHyPwlcvce9GzjRed7gznqpmC5AL3El3KxdEmddZk-KOzRHIpDHm-9F28fEBbauUzFsdv2ZmkR1IUPwQj8VElzfDQh8nScZAgpOngHHuRlKG_2Blcr6cug7VBKWE0UWI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0e414fe.mp4?token=SH7gParEXaE0MkdBxzT4l59trKRFhle_9aWjET9eeLh2uidmIe9Z9BWehmtLDITlfW12raY1jLezE2uK2hZk3eCMRxOPBdIyean_NNAoypS2YflmsEuMxXy268VDiTN9IhKuA0jtwa-fupCMt-QiSIuE6PgPwuMecmSLMelT-CkQsbxtwdAfM1uk3AlGCc7cbQ9gWH0e1El6kXeIcH8uPHyPwlcvce9GzjRed7gznqpmC5AL3El3KxdEmddZk-KOzRHIpDHm-9F28fEBbauUzFsdv2ZmkR1IUPwQj8VElzfDQh8nScZAgpOngHHuRlKG_2Blcr6cug7VBKWE0UWI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات در استان نجف عراق در اعتراض به ممنوعیت پرواز هواپیمای‌های ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/693730" target="_blank">📅 18:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693729">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd2be7225.mp4?token=QAyY1tUMqi-zBcM67ua2-YIdyreOzRsO4NgipJhYSdH2gZMLEirYAjYlPov0GoLTBGfN3Ok7_ctjUoHgSVvIoURnWK0gJGkFUp4HqGVEi0oX_mYaUwI9w0BmIqBBW5p0Ve4No4a9UWHwpUSwTuHenJy0LOgz_epvIuuwZ8hN7ETlBZhyv7BepucLhI3xGd4CbcCY8ppQzAsCNqw6kDQMdfhyoJ-PPBX38R3TzYcR_QE9Ous2734wESqOAeAXzTbOkMP5xW9NhyLTDhEAn4s1-S4d1REMFgoqPMYONXP6FAdmUTOrxth_F_Q4ix0A17NS4uoEw1Ljk8LSbJvnIyJUAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd2be7225.mp4?token=QAyY1tUMqi-zBcM67ua2-YIdyreOzRsO4NgipJhYSdH2gZMLEirYAjYlPov0GoLTBGfN3Ok7_ctjUoHgSVvIoURnWK0gJGkFUp4HqGVEi0oX_mYaUwI9w0BmIqBBW5p0Ve4No4a9UWHwpUSwTuHenJy0LOgz_epvIuuwZ8hN7ETlBZhyv7BepucLhI3xGd4CbcCY8ppQzAsCNqw6kDQMdfhyoJ-PPBX38R3TzYcR_QE9Ous2734wESqOAeAXzTbOkMP5xW9NhyLTDhEAn4s1-S4d1REMFgoqPMYONXP6FAdmUTOrxth_F_Q4ix0A17NS4uoEw1Ljk8LSbJvnIyJUAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی هوشمند شفاف، طراحی آینده‌نگرانه‌ای که مرز بین فناوری و دنیای واقعی را کم‌رنگ می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/693729" target="_blank">📅 18:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693728">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFx9NtTye3lvszgGPN_6psWIleCaF5udY9Rd5_ZTOIWNK99WKq0vFDS0ONUJMVAM_J4Vwb4ES5fea1B57KKEeZzCd-Ku8j9GvecD6Lr6f1pcTsB1HnuGoGKTLcvGvl-rW4fNcSiCYh3mBdklqFpBWUTtZbD0eDn2vh6n9lp4t3GA9Yl5gQedvjovA0rsIa6qrZDp_Efu33sHX6B75csC3AWUpSBL5lahFO_6VIPVlAVIzgRkosRIqnVmFimx5E_urv-6htTWMaUmUCMIWCxi5tMTW0IMgmc0kn7q_Th37z5KihZdlXXSXX02vRoVIVQSRwpc_lSmjlQAHZWedK4Meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوگل‌ارث تصاویر ماهواره‌ای غزه را به‌روزرسانی کرد؛ حالا می‌توان ابعاد گسترده ویرانی و خسارات این منطقه را مشاهده کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/693728" target="_blank">📅 17:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693727">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: در برخی کالاها افزایش قیمت ۱۰ برابری رخ داده‌است
کریم معصومی خسروآبادی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
با افزایش قیمت‌ها و نرخ تورم قدرت خرید مردم کاهش یافته و افزایش حقوق کارگران، کارمندان و سایر اقشار حقوق‌بگیر متناسب با این افزایش قیمت‌ها نبوده است.
🔹
در برخی کالاها افزایش قیمت چندبرابری و حتی تا ۱۰ برابری رخ داده و در برخی اقلام نیز رشد قیمت‌ها به ۱۰۰ درصد رسیده است.
🔹
کالابرگ با رقم فعلی نتوانسته هدف تقویت قدرت خرید مردم را محقق کند و حمایت یکسان از همه افراد بدون توجه به سطح درآمد و نیاز از نظر عدالت محل انتقاد است.
@TV_Fori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/693727" target="_blank">📅 17:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693726">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/952dd3bcd9.mp4?token=cPj9H8GOoWkj5mz_pUh0m4_Lselcm58sG_iw-cDBUTpRRDfwTGo1U6CgaWmjNL2SUJllC-WLY296XZlp-m2cdLrM6LJejT3fYyLN7aU2BxpDilaGl7LzgO30MiWNfIqHCgiy_6Kx7erVY2GiAlsDsh2GyhjZJzH453froVnD4v4PAqB6TZkxbsZqpjnGmGCr07NSrzphgaIwfM5pgjJ8P59KwoE8EHc6UzLjqWj3ouBNtvR8ITuWyxWDaFE59yUiHZJuLwGVreUSHviU7SXG-GIlo4OtvSr8_3AhGSQ7JsHb5qdL7EhaOTIn_lGUX_nhbt9c1byV2bdUe0zM89QsHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/952dd3bcd9.mp4?token=cPj9H8GOoWkj5mz_pUh0m4_Lselcm58sG_iw-cDBUTpRRDfwTGo1U6CgaWmjNL2SUJllC-WLY296XZlp-m2cdLrM6LJejT3fYyLN7aU2BxpDilaGl7LzgO30MiWNfIqHCgiy_6Kx7erVY2GiAlsDsh2GyhjZJzH453froVnD4v4PAqB6TZkxbsZqpjnGmGCr07NSrzphgaIwfM5pgjJ8P59KwoE8EHc6UzLjqWj3ouBNtvR8ITuWyxWDaFE59yUiHZJuLwGVreUSHviU7SXG-GIlo4OtvSr8_3AhGSQ7JsHb5qdL7EhaOTIn_lGUX_nhbt9c1byV2bdUe0zM89QsHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان هواپیمایی کشوری گمانه‌زنی‌ها پیرامون برقراری پروازهای عراق را تکذیب کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/693726" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693725">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde8aae273.mp4?token=ia0KgHi9Y5TDfOdeUQEOZ1Lz86VfWmacXzEFG4spyj_Z3HkbLSAKsZaXp8Sr03vj0_m7xUMlH-9jfXR-fAcF_JGXwUmKCeR6SlQvEGzxi-zBtDa1Ay0pBO-81c8-hDv7zbQKxjDYY-CVHAqq0XNlkfOvqMKZ-1YpYYSIf8XwNkUiaGgfEp6oYmwR4_20N3Gz_2dOMApRfmNg7sXmT4KyQlCd0qE9DHbJWIr6ZKy77tsqD-3E5s5Y0QcAJYqyY1ff_JUUKYbA3zfP-P0KR7Lvn3dYGa97hrFW_-nKw4YyawV964MTIhAcRNaS52AkfW8p8A9nvmXyTICbk3JJxNWXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde8aae273.mp4?token=ia0KgHi9Y5TDfOdeUQEOZ1Lz86VfWmacXzEFG4spyj_Z3HkbLSAKsZaXp8Sr03vj0_m7xUMlH-9jfXR-fAcF_JGXwUmKCeR6SlQvEGzxi-zBtDa1Ay0pBO-81c8-hDv7zbQKxjDYY-CVHAqq0XNlkfOvqMKZ-1YpYYSIf8XwNkUiaGgfEp6oYmwR4_20N3Gz_2dOMApRfmNg7sXmT4KyQlCd0qE9DHbJWIr6ZKy77tsqD-3E5s5Y0QcAJYqyY1ff_JUUKYbA3zfP-P0KR7Lvn3dYGa97hrFW_-nKw4YyawV964MTIhAcRNaS52AkfW8p8A9nvmXyTICbk3JJxNWXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان جالب به‌وجود آمدن یکی از محبوب‌ترین خوراکی‌های دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/693725" target="_blank">📅 17:42 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
