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
<img src="https://cdn4.telesco.pe/file/TOn3M6IjdpmkKHQ0QjtKns5ZMTMuCx2PponC68cHUk_vsqGpCYCiHB5BMvpH7pWxysMaHCbybOfYYK5yFBUSogP8-LoeUIuH_nxYdUvZfW3yg7x_IMowagBGDHqP2FnQ2Od5RE5wxObDOSdalcyCarG-xsh7J1iCBmhYoH5lMqXLJdGTKNGTZm8D68YUAHTrKoNC-RyyURgXIoRB-YiCpWYRhktO4DWRqOWujyYuwK1QF_Z3ZxUcCXeoOp5LLBuZoJkpccDcL8XOS89XsendHetu3OftIeeBigA20WfhgvHz-DyHs7MqfXDvFjaT_F3r61Vea7QPiCFVlcZbkDUYLQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.12M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-665658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F16jXr9-NpDUmTK8NlOVXd2iDIDlenFW8GieL3IdPUefDaK-gNmo-HVE6fsO7pQ6AGIQgJBbzJxqAAT4TOvZWesl29ccaCjumBAWKwCl2dPs4HgOJcbK2cS3ktrBwG8muSgzM0X06w22Xrc-XCOVXC4czt-oBwsRdPmnLSztGeJaN62em4R6yME7P8YCAXV92zwr00zhFCU3GB8A2coN1X4pXRbzUhSxNt2ZLBZ62KvGQlrIAfEEIIam5j6sBZZa2udBT9fr4bG1_3LyTTlEGOdEnT0MHbWaVRcplz7rtgpAogcG-ZH5er2fx_z8_OezH9CrZhZ8J-w1ECyGQ7fwBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بابک خرمدین؛ ایرانی که بیش از ۲۰ سال با قدرتمندترین حکومت زمانه‌اش جنگید
🔹
۱۰ تیر؛ سالروز تولد بابک خرمدین از نامدارترین رهبران جنبش خرمدینان، سال‌ها در برابر خلافت عباسی مقاومت کرد و نام خود را به‌عنوان نماد ایستادگی در تاریخ ثبت کرد. روایت مشهور لحظهٔ…</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/akhbarefori/665658" target="_blank">📅 18:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cbbbe6d08.mp4?token=riHmn7aww6isU8293DkFfRXNIyadJBXdCjfp27Xf9gcXaH7As9SZUgAQkyf4PoDj_g4wM7-t6_Zt4hWrRBunKrB3Lb1UYvdld5n9rvX1fgt6ZKTwRRAjN7f9ioEsnFB7b8u_xJUbn4IPAPHVHud6yGuTu6H3s2uZkAn9OOYm91UKRojn0kHsqtR_Buzcr0VpeHz7xUe_CmdrKAve_26gWXoJEYJZQMW38ovS_xi_CsKie2nrDf2srGg6bhRQ8TBPwTL51b3c975VH40ewX-I69ET5yEnyGIPNVv-OzCgBAOIZpobBejbs7rMaa3X1GLC4-ahT5igPUbxj_kO9vz-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cbbbe6d08.mp4?token=riHmn7aww6isU8293DkFfRXNIyadJBXdCjfp27Xf9gcXaH7As9SZUgAQkyf4PoDj_g4wM7-t6_Zt4hWrRBunKrB3Lb1UYvdld5n9rvX1fgt6ZKTwRRAjN7f9ioEsnFB7b8u_xJUbn4IPAPHVHud6yGuTu6H3s2uZkAn9OOYm91UKRojn0kHsqtR_Buzcr0VpeHz7xUe_CmdrKAve_26gWXoJEYJZQMW38ovS_xi_CsKie2nrDf2srGg6bhRQ8TBPwTL51b3c975VH40ewX-I69ET5yEnyGIPNVv-OzCgBAOIZpobBejbs7rMaa3X1GLC4-ahT5igPUbxj_kO9vz-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیرهای ورودی پایتخت برای وداع و تشییع پیکر رهبر شهید | هم‌وطنانی که از شمال تهران وارد می‌شوند از کدام مسیرها استفاده کنند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/akhbarefori/665657" target="_blank">📅 17:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouJeQ4TgDa5ExyEMvVIXGBuKtqpWdxQHP5SkX_m5mcX9RGX5wDZtCOMv_bCoQa2udT4dAGAF6BWBogKaZ-jdC-H7RAsIHE5y4LIQJp9y3rU-FRKjQYrmqPvwTbxu8NrdoytemrBxx90Zj7EqsOwj-OLFMSbUcoHAhJKePkpHsTPcMZFqPq84gCoerubq4a6NIw6STVycZRhr4nwfOFRCC27qjUKYfNRpT8nYgmI8UGQe0ywVwpXMICwm3BpYy432igEIWFvUh4DhavGeRyWs0iCk365GKGVKCLM7pFohAwVGN_JPAJc8fFYvzgOpCOSiBuT9sDf82mZ5Z_Fl9YZZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: برگزاری نشست امنیتی با کشورهای منطقه، تلاش برای سرپوش‌گذاشتن بر سیاست‌های مخرب آمریکا علیه صلح و امنیت منطقه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/665656" target="_blank">📅 17:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09954aaaf.mp4?token=RkKqlhix2wlR43BA9Tr36CEMM9Pq-TPmDS3TKJPzzhViYRRzqaNxirfG4_KOzcijtvp01-j9pHVedkM6D7IFNqHUPA8fABLYrZTHY3WTW1OaCH1vma07fHtyBOWdthWel7qOJCPaiMFv6pURz2o-JVakCaRqdQpIdcIfFI2x4bW6RutmrT_aaVFBtic2xEiTI9ABzDQThJW8L5dgpBzTeg6Y1nLTt1mZ-D6hLGtIcAIY43w8ipE3Wd8jOOQdnkr2FS6SXLnwEIlySs2OdzlNIcLiIIoiWS4a6JH08uyIXA-taf8TkQjcAhprzxuwg3jRyejNWxwnkuoVYoQKiMRHwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09954aaaf.mp4?token=RkKqlhix2wlR43BA9Tr36CEMM9Pq-TPmDS3TKJPzzhViYRRzqaNxirfG4_KOzcijtvp01-j9pHVedkM6D7IFNqHUPA8fABLYrZTHY3WTW1OaCH1vma07fHtyBOWdthWel7qOJCPaiMFv6pURz2o-JVakCaRqdQpIdcIfFI2x4bW6RutmrT_aaVFBtic2xEiTI9ABzDQThJW8L5dgpBzTeg6Y1nLTt1mZ-D6hLGtIcAIY43w8ipE3Wd8jOOQdnkr2FS6SXLnwEIlySs2OdzlNIcLiIIoiWS4a6JH08uyIXA-taf8TkQjcAhprzxuwg3jRyejNWxwnkuoVYoQKiMRHwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ربات خانگی که برای انجام روتین‌ترین کارهای خانه طراحی شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/akhbarefori/665655" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb692fdf5.mp4?token=oRvynlIEHctk5iuZWy-hPDYDmZrNRl40Kp_zsGR6CFi8GAvCCJaQlLKMvu7uNG63n_LCgvCrQkPPhDjJ4ADOT1iGYIUaHutT5hAv0tieb_6ZyzmcF34D9-5ek6ni2qK_Zr0nIQchPNs2yYTsWNRXUDRcq3gfZRauCNSBdDzPWmGDHSeD7czYWLyhc3EKNhrGKrmDCh9l6jfubc__w-jJ9ZcQjgzJ4SwCI4llGq-yLRDZf5RlbUI9OETa69C1k9byLWG3-lispMYEhOtMyNEQoyrW4ElUVdfzulnvpzcMYybcaWBf9AOzykh_LaRr8vi5SkPe7rUaUO5d2kVCiQq73A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb692fdf5.mp4?token=oRvynlIEHctk5iuZWy-hPDYDmZrNRl40Kp_zsGR6CFi8GAvCCJaQlLKMvu7uNG63n_LCgvCrQkPPhDjJ4ADOT1iGYIUaHutT5hAv0tieb_6ZyzmcF34D9-5ek6ni2qK_Zr0nIQchPNs2yYTsWNRXUDRcq3gfZRauCNSBdDzPWmGDHSeD7czYWLyhc3EKNhrGKrmDCh9l6jfubc__w-jJ9ZcQjgzJ4SwCI4llGq-yLRDZf5RlbUI9OETa69C1k9byLWG3-lispMYEhOtMyNEQoyrW4ElUVdfzulnvpzcMYybcaWBf9AOzykh_LaRr8vi5SkPe7rUaUO5d2kVCiQq73A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز سیب‌زمینی کریسپی رستورانی
🍟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/akhbarefori/665653" target="_blank">📅 17:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdx1lkjYqSOYBV1woBuuEb8WM1EuVaLW_Z6f12ZOH9sS-f_XjwOymLT_YHp46Ix19FpAGopvhXKSO3pevwLNnTAbwlqnm3h05O_88_tM6M9LRMaa4rMDCP6JZLt9TI9K14EEX8pr6K00OsF3EYWdEUWQuSG5V1sPncxn-Uwt2UJWNhF6n1l-WoUT4H_7Zi-wbZAsfsO0RzQOAJbhjPO5ed-JwDiWGs5rrJ_aB8hEXtaMzQIIFoS8InspwWfp5rAl3DxDK6t_D6Yg9KLsDhFtqeWTC6g6n8D4-QpPuq-DNn86XXgpYD4SrsCDGyO9spuSwyp6wHcjV3SsQlXSeU4FuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعدام جاسوس و عامل شهادت فرمانده کل قسام
🔹
دستگاه‌های امنیتی نوار غزه از اجرای حکم اعدام جاسوس وابسته به رژیم صهیونیستی خبر دادند که در شهادت چندین فلسطینی از جمله فرمانده کل گردان‌های قسام دست داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/akhbarefori/665652" target="_blank">📅 17:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c24c6a03e.mp4?token=T3OAWrt77hdewG5giRkPvooeB848IIl7hPONa78dfJbsGk-cSQJQ3zYJxcq5RgaqihXq8huKSmtL38i4buxgV2yX7huMPp2aXF7imOzd2f_-BdW7JEouMhzLWUUZQQN47nWLckkid2M7gBEKht20oGLx_frcwHUsLnXHkNPcLRXOKOshGbMrCYrUik1_4x7GKwbRZr2marUOtzB6Rf2myaelN55PDcqCJ2cGqEZQjrmN-mDaitOH3v25uGJ8mmKgRw5Gwyqh2CFYkzwFzvttGlVugcXBvqpuz2zsuQtC6Nv_pyssXY7dE84TVjSPREEw_655JtoOZCqNevn0adF-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c24c6a03e.mp4?token=T3OAWrt77hdewG5giRkPvooeB848IIl7hPONa78dfJbsGk-cSQJQ3zYJxcq5RgaqihXq8huKSmtL38i4buxgV2yX7huMPp2aXF7imOzd2f_-BdW7JEouMhzLWUUZQQN47nWLckkid2M7gBEKht20oGLx_frcwHUsLnXHkNPcLRXOKOshGbMrCYrUik1_4x7GKwbRZr2marUOtzB6Rf2myaelN55PDcqCJ2cGqEZQjrmN-mDaitOH3v25uGJ8mmKgRw5Gwyqh2CFYkzwFzvttGlVugcXBvqpuz2zsuQtC6Nv_pyssXY7dE84TVjSPREEw_655JtoOZCqNevn0adF-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در تجمعات شبانه: ما با آمریکا پدرکشتگی نداریم، امام کشتگی داریم؛ شما اگه پدرت رو کشته باشن خیلی راحت کنار میای دیه میگیری ولی ما امام‌مون رو کشتن کنار نمیایم
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/665651" target="_blank">📅 17:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
درگیری عوامل انتظامی با تیم سارق مسلح در زاهدان
فرماندهی انتظامی سیستان‌وبلوچستان:
🔹
لحظاتی قبل، عوامل انتظامی با یک تیم سارق مسلح در خیابان بزرگمهر وجانبازان زاهدان درگیر شدند.
🔹
در این درگیری مسلحانه ۳ سارق مسلح به هلاکت رسیدند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/665650" target="_blank">📅 17:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a828e1d4.mp4?token=IizGwvO1TaisQATMqKEXSBw4e5ojCEXDFRwLsZr0V-uQPNtMJm5HsNHUGmiHPJ2CAftU3MX1Nqh1SJP5TJwWM_4kJM-vyn72UwjRXFYnJ3RGbzhAddBsapDtBP2Cw3RHCBX9b4zjtL-rhkBaB1_oWn0Es1BEXWd5J-7wH9kwfljiNh7rJWdHmX4hZadOo5de9jdo9PMqMlLji6KO-MkhRYAJgWFhu-FCUUqYZcAYj5WHZ3Yk4WAJwU4Gp5nw34Xb8xLVs4-KbHQ1IuyzI7hy97aPuE8xRnbKKO4MHeG-qvdyQQ5BNUTfZX2btWQV77FmBWk5YGROYR1fxdlw2l1diBPjQLj31NJVMN9sWBZlp1UgB65PLvJleY6wZoj7ecB7rzSbyFFGRpgJefFnHsuEY971nrvfOEEgh_4c98oTRnz4mim_FfuvA3PuSrYljyUvCqNv5Kc7azgwGsnin2ZZ4ld_BiiiMDqc9h-JQAXBAqyaCrG8O-m0M_2_42aG_cQUdk0Fqo4GdFmNq5iOvsQPakXogGIjUcwk0GwGGqhUlQoxgvxbDKShJ4YPEBSptLDfpovJ-mQyysSeJVBu_9OaDv88k4TX5FUeUXKHRp-RSo8qOzgMAEvZzeDnhRHdD7W1wfCb_Q8STHb-gk9Ot7WeoJytE8xkTcWWx_Qc0THj1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a828e1d4.mp4?token=IizGwvO1TaisQATMqKEXSBw4e5ojCEXDFRwLsZr0V-uQPNtMJm5HsNHUGmiHPJ2CAftU3MX1Nqh1SJP5TJwWM_4kJM-vyn72UwjRXFYnJ3RGbzhAddBsapDtBP2Cw3RHCBX9b4zjtL-rhkBaB1_oWn0Es1BEXWd5J-7wH9kwfljiNh7rJWdHmX4hZadOo5de9jdo9PMqMlLji6KO-MkhRYAJgWFhu-FCUUqYZcAYj5WHZ3Yk4WAJwU4Gp5nw34Xb8xLVs4-KbHQ1IuyzI7hy97aPuE8xRnbKKO4MHeG-qvdyQQ5BNUTfZX2btWQV77FmBWk5YGROYR1fxdlw2l1diBPjQLj31NJVMN9sWBZlp1UgB65PLvJleY6wZoj7ecB7rzSbyFFGRpgJefFnHsuEY971nrvfOEEgh_4c98oTRnz4mim_FfuvA3PuSrYljyUvCqNv5Kc7azgwGsnin2ZZ4ld_BiiiMDqc9h-JQAXBAqyaCrG8O-m0M_2_42aG_cQUdk0Fqo4GdFmNq5iOvsQPakXogGIjUcwk0GwGGqhUlQoxgvxbDKShJ4YPEBSptLDfpovJ-mQyysSeJVBu_9OaDv88k4TX5FUeUXKHRp-RSo8qOzgMAEvZzeDnhRHdD7W1wfCb_Q8STHb-gk9Ot7WeoJytE8xkTcWWx_Qc0THj1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدان با تو؛ رسانه با ما
🔹
راوی بزرگترین بدرقه جهان باشید. توصیه‌هایی راجع به قالب و سوژه به حاضران وداع و تشییع
🔹
از هیچ قاب و صحنه‌ای، راحت نگذرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/665649" target="_blank">📅 17:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f105af3509.mp4?token=lYbifZMt4Gpk1NyUOOBWUOJIq9iq9TkvWrxigIbjOc3MssfK8b1feSiXja8dNZ-b3Bew9imS2QOMseJmcl4bkq3NElG8PHt4zAlnucw2GeAD48Ozj4eMcJPMkL-nOjrCf54LhSMYWDJkiVFq6mN8fYp6nPofMYkWk1YQqJuDvIc2Y1TypK2RofEWnl-PGqsC9pG1d7nH1U-PPGcIinK_Gbfb_ryp-IJ-73LdoXivrYnPyNJ0CsH9O8cs766sRRAzXJBD_wfwro0GlPCMZ7-3BMclojykrEBT4eQ0kE-UqDxHoRECm6hnApJe7D3Ok04CdrGNh9dDwCINGgoiY8ECsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f105af3509.mp4?token=lYbifZMt4Gpk1NyUOOBWUOJIq9iq9TkvWrxigIbjOc3MssfK8b1feSiXja8dNZ-b3Bew9imS2QOMseJmcl4bkq3NElG8PHt4zAlnucw2GeAD48Ozj4eMcJPMkL-nOjrCf54LhSMYWDJkiVFq6mN8fYp6nPofMYkWk1YQqJuDvIc2Y1TypK2RofEWnl-PGqsC9pG1d7nH1U-PPGcIinK_Gbfb_ryp-IJ-73LdoXivrYnPyNJ0CsH9O8cs766sRRAzXJBD_wfwro0GlPCMZ7-3BMclojykrEBT4eQ0kE-UqDxHoRECm6hnApJe7D3Ok04CdrGNh9dDwCINGgoiY8ECsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت پردهٔ عجیبِ تعطیلی مدرن‌ترین کتابخانهٔ قم؛ تغییر کاربری از کتاب‌خانه به لباس فروشی!
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/665648" target="_blank">📅 17:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a32c19f6ee.mp4?token=TLKRNJSMBBRQl1t5fXbWg1Mu9l0OiTfV0MTPsbGrmAvl3YqleUSIg8vE9cKfJFU1z5s0I_nRXKdx4I9A_Rw986P-3uCsHYB5SdGImTVL1mMahkTEkWlxwKBl0g6Y48P4d5LLx3IOX8q8aD2Ynwi3Q5rcQ5QlcSGeNa8VKQtmQdagh7x_xyVCoQ7ern8MVYKZlQVyijv9e-2VlQx995Ayfuo-AM3P8WIgshxgBOz_vAYsWL5wuj0kiXm9W0p3OPKnksF1j-y4TsBonBeU9Qtp_AnIqz1ApwqQ8N9GafXvRq9NiopJSQ_fd2Bgq5fIMkX3twKn112tDQ3Ago1M45jjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a32c19f6ee.mp4?token=TLKRNJSMBBRQl1t5fXbWg1Mu9l0OiTfV0MTPsbGrmAvl3YqleUSIg8vE9cKfJFU1z5s0I_nRXKdx4I9A_Rw986P-3uCsHYB5SdGImTVL1mMahkTEkWlxwKBl0g6Y48P4d5LLx3IOX8q8aD2Ynwi3Q5rcQ5QlcSGeNa8VKQtmQdagh7x_xyVCoQ7ern8MVYKZlQVyijv9e-2VlQx995Ayfuo-AM3P8WIgshxgBOz_vAYsWL5wuj0kiXm9W0p3OPKnksF1j-y4TsBonBeU9Qtp_AnIqz1ApwqQ8N9GafXvRq9NiopJSQ_fd2Bgq5fIMkX3twKn112tDQ3Ago1M45jjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف مرگبار در تایلند
🔹
رانندگی یک پسربچه ۱۱ ساله با خودروی وانت والدینش در استان «موک‌داهان» تایلند، به فاجعه‌ای انسانی منجر شد و جان ۹ راهب بودایی را گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/665647" target="_blank">📅 17:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
امتحانات نهایی روز شنبه ۲۰ تیرماه در سراسر کشور لغو شد
سلطانی، مدیرکل آموزش و پرورش خراسان رضوی:
🔹
با توجه به تداخل آزمون نهایی با تشییع و تدفین رهبر شهید در مشهد و اینکه اولین آزمون نهایی مربوط به پایه یازدهم است، طبق آخرین ابلاغیه آموزش و پرورش، روز شنبه ۲۰ تیرماه آزمون نهایی در سراسر کشور برگزار نخواهد شد./ اخبارمشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665646" target="_blank">📅 17:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت آموزش و پرورش: مهر ۱۴۰۵ بدون کمبود معلم آغاز می‌شود.
🔹
وزارت بهداشت سوریه از افزایش تعداد قربانیان انفجار دمشق به ۵ کشته و ۱۶ زخمی خبر داد.
🔹
والیبال انتخابی آسیا؛ دختران زیر ۱۸ سال ایران مغلوب اندونزی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/665645" target="_blank">📅 17:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Et-iA67UTW4g5iJ2y-m2wpX4f77KpOUuKX24nuu1H_zGkDhm2mVaJaQjTE1ct5gLwPt1Ivd3LbdkvnXkTaQ8pPetQczjyaCAb3fZrv0szxs5JCkxYAhGf6m8ph-6mvUbyCTvgwRjfhyQG3AG4vt8OECVrrxLhUXUgGvActGVXXh5afxCsDbRLUAazxlVpKmWPB4_1_1KqfQEGlPoxQboqM9WI7RpR4E6iG5stQ_utxuXPYR7-cIRcsOqDOg02iFQoH05_vmYY0OrkkZQLqkxAgUZnqYQNwzQdkSDYZw5-3PpupfTkKAf00bCLN2ZwtJEbZoENN0HhzGPNMMkrVGobg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: ایالات متحده تاکنون بیش از هر کشور دیگری برای محافظت از ناتو هزینه کرده است، بدون اینکه هیچ سودی از این کار ببرد!
🔹
ایالات متحده ۹۹۹ میلیارد دلار، بریتانیا ۹۰.۵ میلیارد دلار، فرانسه ۶۶.۵ میلیارد دلار، ایتالیا ۴۸.۸ میلیارد دلار، لهستان ۴۴.۳ میلیارد دلار.
🔹
دیگر کشورها، از جمله آلمان، بسیار کمتر از این هستند. (۲۰۱۴-۲۰۲۵) مسخره است!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/665644" target="_blank">📅 17:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwNs1gMCu59vmQjutxZ-ppJ8BZB6bMvcfjlsycVGK8AffhLmSFmrq1ThFkmUJ_Ly4r323yhXWtDFybOTvnSyrZQrIbkQxfubmM_2KW_WZNVtZb-QuioO1VrjjiNxK3WWEdYhNEt1Jkey-ms7x35LGzb5rwKT2irRcyzOzAOCO8JRINwB-ArcXubGh7XceMTispy1XhyyOZEc4_mW0RqOOJSTMH5GKWQVQDWWrmEX-Grzs5kohv6KFKG5YWHdmx052qrGe2jfb43R57PJv94xRRvFtH2PD1u1jMmDyduWqG-UcpVpfpkoJKgjpBnh3bt1mMjVeMmoIoEjdPOM5bNxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌ها تاب‌آوری قابل‌قبولی در حملات سایبری داشتند
محمدصالح جوکار، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
در شرایط فعلی، دشمن تلاش می‌کند با ایجاد نارضایتی عمومی، وحدت و انسجام داخلی را خدشه‌دار کند و در این زمینه دست به بزرگ‌نمایی مشکلات می‌زند و یکی از این موارد مانور تبلیغاتی بر حملات سایبری به بانک‌هاست.
🔹
مجلس موضوع دولت الکترونیک را مورد توجه قرار داده و بر توسعه زیرساخت‌های فناوری اطلاعات و ارتباطات در کشور به‌گونه‌ای که از ایمنی و پایداری لازم برخوردار باشند، تاکید کرده است.
🔹
برخی از بانک‌ها تاب‌آوری خوبی در حملات سایبری اخیر از خود نشان دادند. ارزیابی‌ها نشان می‌دهد که برخی از این سامانه‌ها همچنان نیازمند تقویت و به‌روزرسانی هستند که به زودی مرتفع خواهد شد‌.
🔹
در کنار مسئولیت بانک‌ها برای مدیریت چالش، حاکمیت نیز باید نظارت و راهبری موثر خود را در این حوزه اعمال کند زیرا این موضوع مستقیما با زندگی روزمره مردم، اقتصاد و نظام پرداخت کشور در ارتباط است.
🔹
اقدامات موثری در زمینه ارتقای امنیت سایبری در حال انجام است و این روند باید به‌صورت مستمر ادامه یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/665643" target="_blank">📅 17:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
مراسم تشییع رهبر شهید در مشهد ‌قطعی شد/ مبدا شروع مراسم بلوار فرودگاه تعیین شد
سخنگوی ستاد تشییع رهبر شهید انقلاب در خراسان‌رضوی:
🔹
‌پیکر مطهر رهبر شهید انقلاب و اعضای خانواده ایشان پس از برگزاری آیین‌های وداع و تشییع در شهرهای مقدس نجف و کربلا وارد مشهد خواهد شد و مراسم اصلی تشییع، بدرقه و وداع با آقای شهید ایران روز پنجشنبه هجدهم تیرماه برگزار می‌شود.
🔹
مبدا مراسم بلوار فرودگاه خواهد بود؛ مسیر تشییع تا حرم مطهر رضوی امتداد خواهد داشت و تمامی خیابان‌های اصلی منتهی به حرم نیز جزو مسیرهای رسمی مراسم هستند.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/665642" target="_blank">📅 16:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
انفجار در یک کافه در دمشق
🔹
رسانه‌ها از وقوع انفجار در یک کافه در دمشق پایتخت سوریه خبر دادند. بنابر اعلام رسانه‌های عربی بر اثر این انفجار ۴ نفر کشته و ۱۰ نفر زخمی شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/665641" target="_blank">📅 16:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
بقایی: از هر کشوری که موضع ناشایستی در قبال تجاوز نظامی آمریکا و رژیم صهیونیستی به ایران اتخاذ کردند و از آن دفاع کردند و یا مواضع نادرستی داشتند، دعوت نکردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/665640" target="_blank">📅 16:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=R0uQ9pvRdPXdQh9mKUoQkof7Gl2Hh2_xCS8EL7StshC1sMdJCEN0LotRrgFrJN6qHuvsVXaL4AKBC_rWFtCB_r1H0iXyVZXR3yVrV1dYyTyaMPyhLKiWNfhYLcB5NEFXNDm9EkxoavpzLxU35O5yIZRpMHkB0lK7WeWLA9NSXkIexkIhzWmSypOQDu84CLUj3wABSXoQ6fKUlyKdQhqFK81jmCzPJ_NEVoZa2cITygFHUhLgq-JRZ4NVyucJ_ydhHhc_KmsVAw-FWPJu8T0d69H_4L_rEZ-237po6-KnTummhRnLD8tAFZ5ayKX8xNJprKAL6abRe1gLlUj6bRvfmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1c88eb50.mp4?token=R0uQ9pvRdPXdQh9mKUoQkof7Gl2Hh2_xCS8EL7StshC1sMdJCEN0LotRrgFrJN6qHuvsVXaL4AKBC_rWFtCB_r1H0iXyVZXR3yVrV1dYyTyaMPyhLKiWNfhYLcB5NEFXNDm9EkxoavpzLxU35O5yIZRpMHkB0lK7WeWLA9NSXkIexkIhzWmSypOQDu84CLUj3wABSXoQ6fKUlyKdQhqFK81jmCzPJ_NEVoZa2cITygFHUhLgq-JRZ4NVyucJ_ydhHhc_KmsVAw-FWPJu8T0d69H_4L_rEZ-237po6-KnTummhRnLD8tAFZ5ayKX8xNJprKAL6abRe1gLlUj6bRvfmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش‌وپرورش: امتحانات نهایی به‌هیچ‌وجه به تعویق نمی‌افتد
رئیس مرکز ارزشیابی آموزش کشور در برنامه پرچمدار:
🔹
آزمون‌های نهایی طبق برنامه برگزار می‌شود. امکان برگزاری آزمون‌های نهایی پس از کنکور وجود ندارد.
🔹
در نیمه اول شهریور نتیجه امتحانات نهایی به سازمان سنجش اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/665639" target="_blank">📅 16:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665637">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUSsngudjH0HX4SFjHKVJvK0Z6veA_y27RDasbzRXSmCpMaIyIHLnrolCNFngNEm4gJgkl0AdYkJu5SKK-GtpKgZOdclr0SKhZjzYlnFhuGlGcLlgCkOIyeL8Y7zPCv_6maF8V9DaVpggWj-0nTVD_mBbWi9G5SWdjNCZ3IDt_aNqKqLz9I2z6N7jECX_WUFxXkAV8lybf3rpZqiGW4tEqnmJmfl6m4NfyXB8SexoMh_dxLZ4VL11WsZoNJpSz7A1x1uokacdwU-Xt7eAn00hRjeHHerjHzOHFlJBrIyV6pQLG9-6432i4QSu2j49Ee0DIoT-JhXxCYfEMLqsfHQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌ها در خط مقدم جنگ سایبری
جعفر قادری، نایب رییس کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
بانک‌ها اکنون در خط مقدم جنگ سایبری قرار دارند و این نشان می‌دهد که مراقبت ویژه‌ای باید از نظام بانکی صورت بگیرد.
🔹
اگر لازم باشد بانک‌ها باید برای بهبود وضعیت دفاعی و تاب‌آوری هر چه بهتر، مجوزهای لازم را برای استفاده از نیروهای متخصص دریافت کنند.
🔹
در ابتدای جنگ پدافندهای نظامی ما دچار مخاطرات شدند ولی با تقویت سامانه‌ها، چالش‌ها رفع شد و همان‌طور که چالش‌ها در این زمینه برطرف شد، در نظام بانکی هم با این چالش‌ها دارد به خوبی مقابله می‌شود تا به طور کامل برطرف شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/665637" target="_blank">📅 16:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665636">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
جنجال جدید در خانواده نتانیاهو؛ سارا نتانیاهو همسرش را در حضور اطرافیان تحقیر کرد
🔹
انتشار ویدئویی از برخورد تند سارا با بنیامین نتانیاهو، در استادیوم «تدی» قدس اشغالی، حاشیه‌ساز شد و بازخورد گسترده‌ای در شبکه‌های اجتماعی صهیونیست‌ها داشته است.
🔹
همسر نتانیاهو در این ویدئو با لحنی خشمگین به او می‌گوید: به خاطر تو مجبور شدم با دیگران بحث کنم!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/665636" target="_blank">📅 16:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665633">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvQqzqRylVYXIyHolcBGKKJrGKkEjTrZqWjvy3TK3x8w4Nf5nrnB0qb2scBA-yhtKuCpP94j3fNckse8owaWMpPA3-LLzjqR6IQwOd6dxjBKW_qjWDjiLMrtW2DdVguF4PrwZjucQfQVQA9K7e9lK1xyou1WI0voDvd4ExBX2RrLd1WnbI6U3m2GU3hz5ll668F9xXtmH730m1k-vOddTCsznKTGGJDNM3FTsFoMKUFhiQFjSHxWmSJmp8KIH16NJbK8feFBnphbVPM4KpYjNpjZib9V4w-RmTB3y8JUVnHD8SCLUDQ80JUHScvV36G_4rwb8njO1CMA73DWkj204g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7Qg0FWSeX_YOY_TWw5wkgLAnNFL16F2hngjl0mefn3OVSZZmsTk_nO0rZKne_RnH6M5-osukqdJUSU1kRgJrWlNQIw8PjQ9EiPpML45kVYHVPmnjoO92rnfF2XSIRzd4QCAz5ra-oho1ess7Zu56bb-lS8tmPrSVsfntx8T10lrk9uB8chp5_oqqH_emD4cGCanVr_3-RDKamKAGJoXrP-LoXRs6y7ihhU1byziSvW1iGMO8UIMXj66lbOkf4sDKO6WBfiACHDIjANxWtpJwybkltDmkrr2RhkS_72JYzYH0rsHz9iqVNw1zGbK6M0V7D9z1pPXdwbqlnEWtxjseA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cy5h5juBhgH3qMnMseeP0VRb_DXCIJ21DLioOo4LzgmcXRqXR4r8EzqT4WhrrlgIRBWHqF1PLIFn0176qkX8YrWIBdalgQv3nfSfV13WtcvtKilELPATPPJVBYQEGURPTRZIQXDcmEltTlXIaPHttsgKLMLzjs7tTzeVWrt1B46yPGx_yBDPtGd4EYYLtaRMhjymK8KiSKGarbln0LCkJFHrB1_UY9QTv4kQl33cr5lLSOFtGCXO-9iqYyhzxnyDOdh-tc0MtGyKhsXQym2KzuzXpDcBTqbtP5CtGC-I6dN99zdTTs1Pk0J084o1M5zNkHtsdbDj9UcfjustvvdgoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چه چیز‌هایی از پول به کودکان‌مون در هر مرحله سنی یاد بدیم؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/665633" target="_blank">📅 16:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g24WmQl5kUVHBaYEWO6OtMybSMx3VDfIHU-YtKJnxu-YwBAFO1JGx4Et3kZPNGrMWn7MjcVT_45QBQs3VImkgyZerojyK9iQOj8iIaqbF7hFktoWfF7rVasLsb8zx0C9ItqbOqVU9WlLT1nlJjQYAmn7nT2KiQhRN0m0mLGfJrK9pBc43KWkSC1ntsogFmD_hrWKJbtq4KFdemEfs2qAkbVsKhKubSS7Z4kjRJsZMHJe6hnCKcTRaSHYhBofEOcCa_5nq1qpbfyzth6QYaUAj1dXeRr7Q-HwizjN4fOoJlZLcQNHh_2zdjmH15bqJ4OH1u_RER4FF-_Kho2e11YI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: در صورت تامین نشدن شروطمان توسط آمریکا، خریدها از مبادی دیگر انجام می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/665632" target="_blank">📅 16:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
پزشکیان: صرفاً شرکت در محل اصلی مراسم تشییع رهبر شهید معیار ادای احترام نیست
🔹
مردم عزیز اطمینان داشته باشند که صرفاً حضور در محل اصلی مراسم معیار ادای احترام و مشارکت در این بدرقه تاریخی نیست و تمامی شهروندانی که در مسیرها، معابر، خیابان‌ها و پهنه‌های پیرامونی حضور می‌یابند، بخشی از این اجتماع بزرگ ملی و آیین تشییع و وداع محسوب می‌شوند.
🔹
ضروری است خانواده‌ها به‌ویژه در خصوص حضور کودکان، سالمندان، بیماران زمینه‌ای و افراد دارای شرایط جسمانی خاص، ملاحظات ایمنی و بهداشتی را مدنظر قرار دهند و حتی‌المقدور از حضور این عزیزان در نقاط بسیار متراکم و پرتراکم جمعیتی جلوگیری شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/665631" target="_blank">📅 16:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665630">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECt97H-amaolhUBMt_vWAXKE1BTxdJDvgcttQ2g_yBCPjm2lIcvX4q4qevrM01kWFMHre8NYh6Pf49yy2v9rgiGjrVcqk9KGGQnrdB3XsWMLhx6DrWsNSuCje4qF087JvLHwlB6SF3VLJ25B2Ip8rLquiBrarz-pwnmeXRryjQSzGZySd82vhr7FSkObik4v2-6MzZ-kEZhJaaP94qbYVwgySbRS7Qz1nXPJ0-IPQuk7K4mdIZPzogMXKytgt1JgsOduZL-T3ih-bc_SI8sWiNr_e_F_YqpycrDPzr3cgDm62s_st3gheeYTAYMdWeQ-Aoab6-ez62RddwWZsw1gpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری زیبا از شباهت مزارع برنج به تابلوی آینه‌کاری در اثر انعکاس نور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/665630" target="_blank">📅 16:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665629">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در اربیل واقع در شمال عراق خبر می دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/665629" target="_blank">📅 16:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665628">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
آموزش‌وپرورش: مانعی برای حضور دانش‌آموزان در مراسم تشییع رهبر شهید و اربعین وجود ندارد
رئیس مرکز ارزشیابی آموزش کشور:
🔹
زمان برگزاری امتحان دین و زندگی پایه یازدهم از ۲۰ تیر به ۵ مرداد تغییر کرد. امتحانات نهایی ۲ روز قبل از اربعین به پایان می‌رسد و دانش‌آموزان می‌توانند برای شرکت در مراسم راهی شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/665628" target="_blank">📅 16:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665627">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی ایران: دو هزار لیتر سوخت گازوئیل به صورت تنخواه به ناوگان اتوبوسی کشور برای شرکت در مراسم تشییع رهبر شهید امروز شارژ می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/665627" target="_blank">📅 16:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665626">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrwuwLaOVrx86h_5JuCmKjfDzZJlu0Ok6ofQMir7293IrOAgkKSWJ0YUpUcUG7f-EPHxhy8LhyN8ru0y-7zc-LFyKmZu1XQmjsZ63JgOaqXmVWrUJceSZCkk0cRl9EeFPHDyu23YWNhIz8DLOEyw6fJXgt-vCLT7VlelGv0wc8zQWUjtH8BCEihQf_V7b6kBEdClshDPCOBZoPDuAaMannDWgCqkwU8OmSXn15CjdVF0dvbl3g_LXtEG9CUfrhZ7oV3ZLXJLxO2u6E7zDV16jBtGFFx9s9SjBQypamvqPzjol40cJr0rzTvzKTHVmneErYGZYOUV5buvdxCRjk-MOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پل معروف به «بین دو بهشت»؛ پل ارتباطی دو استان کرمانشاه و کردستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/665626" target="_blank">📅 16:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665625">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ade299394.mp4?token=e_vB3V6WCr6pIwEV2q5-OPX2S4afZ_sme5Wc4YiwxkPa2xOQqTperoTjAC5OZa4TZeMcuImvOxJSXEp8wFjwmRGZ9BhoxnU1Hk_3IEW9_p3eFjk1eSOv-vGH875LMMqL37SgGQ2yr4O7EptoAIywQycXW-NMwglFF3ZF4VvIlCy_445H4D7_oic5eI9wd7Hg7A7AbQO8RaApOpKF-lytlozuHNGQtxrg1CAWyHpt6jnayzuBnldpVmpHJqu71owrn2CjyZ_-42Up3F5Hiph4rlqKDu9J4L7Ex8WZf9kb97TNlVZTh4eKfjIsOlSx1CZu3E7dEjEc9jTI3tg8-4wWvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ade299394.mp4?token=e_vB3V6WCr6pIwEV2q5-OPX2S4afZ_sme5Wc4YiwxkPa2xOQqTperoTjAC5OZa4TZeMcuImvOxJSXEp8wFjwmRGZ9BhoxnU1Hk_3IEW9_p3eFjk1eSOv-vGH875LMMqL37SgGQ2yr4O7EptoAIywQycXW-NMwglFF3ZF4VvIlCy_445H4D7_oic5eI9wd7Hg7A7AbQO8RaApOpKF-lytlozuHNGQtxrg1CAWyHpt6jnayzuBnldpVmpHJqu71owrn2CjyZ_-42Up3F5Hiph4rlqKDu9J4L7Ex8WZf9kb97TNlVZTh4eKfjIsOlSx1CZu3E7dEjEc9jTI3tg8-4wWvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیس لاته انبه، نوشیدنی جذاب این فصل
🍹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/665625" target="_blank">📅 16:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665624">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
دقایقی پیش ٢ عضو گروهک تروریستی جیش‌العدل در زاهدان دستگیر شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/665624" target="_blank">📅 16:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665623">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9uFb0R4WUbkty1ynTxTnJ7P-ztjm6W_kE9nG59FDPuwdyAzzqGXsI0RJEg3kz8I9vG2-QrdJjkbEaTHpOvb5crt6xAyEiNjQ6OxfrcKe-d-ru1Om_sgxORHNiaQ2LZWy5FG7Gw67GAbIyNIaWIHBUfLw-rk5rB-Jy0JM4PKOzHZPtZyAdtvhmgWFKXBrBnxshCx7mmPaguUYVVticRKCtEYABEGW7wMw9tp6XbI5HUPnAfATAo0XcyTbLD97l1qmI5bI67M2fkzTeDH15REoUCgBBdxJvOwGN62kOi8If1gsMVOh1tZ3mSP1Nf7NcAtqZ8PjQKwrel8XVLaVghohQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه راهنمای زائرشهر چهل‌سرا در جنوب مصلا
برای مراسم وداع با رهبر شهید انقلاب
🔹
استقرار مواکب پذیرایی، بیمارستان و آزمایشگاه سیار برکت در زائرشهر چهل‌سرا در ضلع جنوبی مصلا و خیابان بهشتی
🔹
تماس با سامانه تلفنی ۴۰۳۰ برای راهنمای مسیر، مراکز اسکان، درمان، ستاد گمشدگان و مشاوره روانشناسی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/665623" target="_blank">📅 15:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665622">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjGZqDUvS448HJjZzpjC51v0gbG4JquIPM7id3-590JpMSE54E9cq-q8tf0b5gy8r5gLIha3t46ceEvru9d8TQCW7suGhX3GRLjlWb_8PIXVXm9nDhj4Lv8RKV7e1RliV48vfbKutn6o-N2aAhf2E1miiabV65_OQ7RGz-V55NVXAViatRcKmFb3QDmZ_r1G8iPmIMueU7JQTRAv0a690iQ94yMWUAZlCHa39jRttJFJpFX4NIMGOg8yHZe45RyT5H8FVT0cSdlZnS4AOlZcg0BzqLhV2nsAxLtGvZJrN8V9ys8peaIr_Lp8dAhAdRd1KCH9bKi2yQ6M4mtHW6FKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رشدی ۱۵۳ درصدی سود خالص واسطه‌گری بانک اقتصادنوین
🔹
بانک اقتصاد نوین از ابتدای سال جاری تا پایان خرداد ماه موفق به کسب درآمدی معادل ۲۷۲.۱۵۷ میلیارد ریال از محل عملیات واسطه‌گری پولی شد.
🔻
اطلاعات بیشتر:
🔗
https://www.enbank.ir/s/mfa8De
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/665622" target="_blank">📅 15:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f07b35cfb.mp4?token=WpZNk4aXjPXsRReS5mvgpuM-RUls0K6mgVFgG8h80b3TmXSoDjWMxUGdVIAdQGRKJS4CI5D-P4qiCJBSnzZul8f6n_N_XI8iySCXCXLifVJAm_KeQrY44PyydEcPys1FEdRVD8sGHqT68uBFBokQR_C4JCNd2oRzP8BS9TBNePmzhhe1ReIaXPNZaAaZ4d6zN2ubg6-ve8hHAc0__VbDV1d1CP49EHl_gLlhwsZ1Rdhom0Akvq3MTBFuEaxT9U5clt9xpTMBH-Fx4KtB1tDNg64FF2go91y9fEhb6aXJ_3WXF7AW9RJJb_bGZHJtn6_h5zoseiNHXlZwgxIjfqXWAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f07b35cfb.mp4?token=WpZNk4aXjPXsRReS5mvgpuM-RUls0K6mgVFgG8h80b3TmXSoDjWMxUGdVIAdQGRKJS4CI5D-P4qiCJBSnzZul8f6n_N_XI8iySCXCXLifVJAm_KeQrY44PyydEcPys1FEdRVD8sGHqT68uBFBokQR_C4JCNd2oRzP8BS9TBNePmzhhe1ReIaXPNZaAaZ4d6zN2ubg6-ve8hHAc0__VbDV1d1CP49EHl_gLlhwsZ1Rdhom0Akvq3MTBFuEaxT9U5clt9xpTMBH-Fx4KtB1tDNg64FF2go91y9fEhb6aXJ_3WXF7AW9RJJb_bGZHJtn6_h5zoseiNHXlZwgxIjfqXWAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نسل جدید سینماها؛ تجربه‌ای خیره‌کننده که مرزهای تماشا را جابه‌جا می‌کند
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/665621" target="_blank">📅 15:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9410720e62.mp4?token=LmMxfJbfwX3U-hNN7pSTkNosOGrKSzo6x10DGj5jpbfoTGA7B4zuLc-PXG-Hza1LGWyECiLtQzYVimQtiokg7YGO3wfvWgOV4BUST66ju19Qr4ky_xfJSIB1RHK2fRSNJRq0PH31MfrBm6JycIs77XWC1JFZ4cEuAEkZ-n9jR44FZ0yvWtU8i9M29dyiWfDdxVPwcUIYn-tZP_suGN8BGYUhKTNFXTKwMHcsMp2e_x26Vxz-QS8eGdBXMvWzIqs3EqPGIeFfXK2nayGD_Z_5Nh93X8NqboWswTZc0nXdH48dEf-Qxy31Id8mjXm7VlVjh47veNHFT5Cy6INvIFmT1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9410720e62.mp4?token=LmMxfJbfwX3U-hNN7pSTkNosOGrKSzo6x10DGj5jpbfoTGA7B4zuLc-PXG-Hza1LGWyECiLtQzYVimQtiokg7YGO3wfvWgOV4BUST66ju19Qr4ky_xfJSIB1RHK2fRSNJRq0PH31MfrBm6JycIs77XWC1JFZ4cEuAEkZ-n9jR44FZ0yvWtU8i9M29dyiWfDdxVPwcUIYn-tZP_suGN8BGYUhKTNFXTKwMHcsMp2e_x26Vxz-QS8eGdBXMvWzIqs3EqPGIeFfXK2nayGD_Z_5Nh93X8NqboWswTZc0nXdH48dEf-Qxy31Id8mjXm7VlVjh47veNHFT5Cy6INvIFmT1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار در یک کافه در دمشق
🔹
رسانه‌ها از وقوع انفجار در یک کافه در دمشق پایتخت سوریه خبر دادند. بنابر اعلام رسانه‌های عربی بر اثر این انفجار ۴ نفر کشته و ۱۰ نفر زخمی شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/665620" target="_blank">📅 15:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665619">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
صدور کارت سوخت‌المثنی ظرف ۲۴ ساعت
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی ایران:
🔹
شرایط دریافت کارت سوخت المثنی به صورت یک روزه وجود دارد. اگر هموطنی کارت ندارد و درخواست دهد تا ۲۴ ساعت بعد کارت را میتواند دریافت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/665619" target="_blank">📅 15:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b5acf4c9.mp4?token=pffwyJ1BhuJ_f-eUJNouqvh5YX4LDyZy_V5vg115DKxTWk6vC_Wvo5x-ZeM7tOjDx6Pqqb1HW4aYvfKropK_OZ5uNjMV08ky2qc17y594gh88369L7wWEqIDSZxZi1nASA_ZqvTs0Fx7qVQea5XSM-eJib8G38netIvdWNO8g8IchNxYAWGX7Y2hezODM9K48xtNN3crD-ub0YL4Blgd2SsmUp-6AVztbnpEUZV37MESWPySz3roQtNgpeR_loaoNXw2b39jINe0dbXdxwYoHW80bTSNC7F6-M7ZEcmOF2xA3wZS5aktmNJTBsiFJtECCvw2WCTX_obpFVNI7eJxwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b5acf4c9.mp4?token=pffwyJ1BhuJ_f-eUJNouqvh5YX4LDyZy_V5vg115DKxTWk6vC_Wvo5x-ZeM7tOjDx6Pqqb1HW4aYvfKropK_OZ5uNjMV08ky2qc17y594gh88369L7wWEqIDSZxZi1nASA_ZqvTs0Fx7qVQea5XSM-eJib8G38netIvdWNO8g8IchNxYAWGX7Y2hezODM9K48xtNN3crD-ub0YL4Blgd2SsmUp-6AVztbnpEUZV37MESWPySz3roQtNgpeR_loaoNXw2b39jINe0dbXdxwYoHW80bTSNC7F6-M7ZEcmOF2xA3wZS5aktmNJTBsiFJtECCvw2WCTX_obpFVNI7eJxwjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جدید ترامپ؛ دکتر ترامپ
🔹
ترامپ در شیرین‌کاری جدید خود با هوش مصنوعی، این بار در نقش پزشکی ظاهر شد که منتقدان سرشناسش را درمان می‌کند.
🔹
ویدئو با تصویری از ترامپ آغاز می‌شود که با لباس پزشک از مخاطبان می‌پرسد «آیا شما یا یکی از اطرافیانتان به سندرم ترامپ‌هراسی مبتلا شده‌اید؟» سپس می‌گوید «علائم این بیماری می‌تواند بی‌وقفه ادامه داشته باشد. خوشبختانه، من دکتر ترامپ هستم و برای آن یک برنامه درمانی دارم».
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/665618" target="_blank">📅 15:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45eb86f977.mp4?token=EDOVDLz1IoQpxD8kBImk6UtF9qxEKiAVFacuaKZoRymko-z3UtPCXr3P9NbNUiQ34OCHDTfC4SoeKoivEqpn0AI5mQBn0GVj4m8a7bB4QgIyjXhAkcgMr1X6C912i6lphNJX8VIfggC2PeB_-jxoRLp5Bgnuqe4bD_fSfFLYBh2hSHsKUe3ozL51NQsl73gPZL6WiFM-PlqRowacsxyLcl4oDQjb0SGnqBctoByZtdvRDJHVd3SJ3cUmova1DHHswZr3i9W6yl8gi4XKCK8EnWkvqN-BN0lLI43VxwRC8tvSBnYbxwIvoRk7IT2IOM8YaF1xS6zkjnbr13POmkwpk3eXsMT-pJqBv-kFPGgkLRsHL4OWxdzvhnY0xykldXWzM3uLhILBpvN3dA1LhtirJqzjtqTRUBdwMs1j3SBcf5s0EoiCQhEZZV0oX0C_NKVGL5xAgkAYXPx8JjXmrdSLPkdpzicj4EuXer0jubJTzzDRGr3mZxzvvkjUvUMKKePC_2hG1Nl2bRc1I5ZwecHW1mytd8cQC2xaVHXk_1ZF7r26_y6nmwaOmKKFJ0fB8SR_MAJxt5_dDdhqWFJgVDLyTTUkIllCW0q3da8CUFDCQkiPxzGk3_AN3v1krwRBpGYGgcolMCWeWiWXyQu3bgQW2kKWRSitNp4DPfVz0-GDtEY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45eb86f977.mp4?token=EDOVDLz1IoQpxD8kBImk6UtF9qxEKiAVFacuaKZoRymko-z3UtPCXr3P9NbNUiQ34OCHDTfC4SoeKoivEqpn0AI5mQBn0GVj4m8a7bB4QgIyjXhAkcgMr1X6C912i6lphNJX8VIfggC2PeB_-jxoRLp5Bgnuqe4bD_fSfFLYBh2hSHsKUe3ozL51NQsl73gPZL6WiFM-PlqRowacsxyLcl4oDQjb0SGnqBctoByZtdvRDJHVd3SJ3cUmova1DHHswZr3i9W6yl8gi4XKCK8EnWkvqN-BN0lLI43VxwRC8tvSBnYbxwIvoRk7IT2IOM8YaF1xS6zkjnbr13POmkwpk3eXsMT-pJqBv-kFPGgkLRsHL4OWxdzvhnY0xykldXWzM3uLhILBpvN3dA1LhtirJqzjtqTRUBdwMs1j3SBcf5s0EoiCQhEZZV0oX0C_NKVGL5xAgkAYXPx8JjXmrdSLPkdpzicj4EuXer0jubJTzzDRGr3mZxzvvkjUvUMKKePC_2hG1Nl2bRc1I5ZwecHW1mytd8cQC2xaVHXk_1ZF7r26_y6nmwaOmKKFJ0fB8SR_MAJxt5_dDdhqWFJgVDLyTTUkIllCW0q3da8CUFDCQkiPxzGk3_AN3v1krwRBpGYGgcolMCWeWiWXyQu3bgQW2kKWRSitNp4DPfVz0-GDtEY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به ما اطلاع دادند که شهید کمال خرازی ترور بیولوژیک شده بود  صادق خرازی برادرزاده شهید کمال خرازی:
🔹
دکتر خرازی دو بار شهید شد!
🔹
من منکر تلاش‌های برادرمان آقای ظفرقندی نیستم، چند بار بالای سر شهید خرازی حاضر شد، آقای پزشکیان دستور مستقیم می‌داد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/665617" target="_blank">📅 15:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZWhvECcYJQc9pKpizEiapKueOf3f0LBUYAbAkX4LMi-UxEtU-pjR8Sa80EwXNHJCchlTXQfOGOXY3ziLExgHrJs1lyTiw7lVtvaBgKJisAiq63tbrFw2TkGKm5l6-z_W3xVPLJ2c_Sl2_CCJZYlbcWRLB1a8I2zINoqybzYBoA_xWIxrmJUvb4urhPpiO8wDEhqWWeUJbcavuxQ4XqkYdoWnrtE3V0YodMqg59iIKZiy-TXjzlvDk68tWKB159EpxTv-7h355HZbE0bRDckeWQAMVUKLff7CMMovcprn0jKRhgQ2FuniN6FUB73ve29MOqOy9kPjHt-B9EDnwtlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی کشتی فرنگی جوانان ایران قهرمان اسیا شد
🔹
تیم ملی کشتی فرنگی جوانان ایران عنوان قهرمانی زودهنگام رقابت های آسیایی تایلند را از آن خود کرد. در جریان رقابت‌های ۵ وزن نخست کشتی فرنگی قهرمانی آسیا در تایلند، نمایندگان ایران صاحب ۳ مدال طلا و ۲ برنز شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/665616" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
اطلاعیه شماره ۲ قرارگاه برگزاری آیین وداع و تشییع قائد عظیم‌الشأن شهید امت (تهران)
🔹
هموطنان عزیز تا حد امکان برنامه سفر خود به تهران را به گونه‌ای مدیریت کنند که از حداکثر ظرفیت اسکان و ارائه خدمات به زائرین در تهران استفاده شود به عنوان مثال سفر را کوتاه کنند تا تعداد بیشتری از مشتاقان شرکت در مراسم بتوانند حضور پیدا کنند
🔹
مبادی و جاده‌های ورودی به پایتخت همواره باز است و هیچگونه منعی برای ورود وجود ندارد
🔹
زائران گرامی اخبار و اطلاعیه‌ها را از مراجع رسمی پیگیری کنند و به ویژه مراقب شایعات و اخبار جعلی باشند.
🔹
پیش‌بینی و توجه به محدودیت‌های ترافیکی در سطح شهر تهران و حفظ آرامش در هنگام حرکت همواره توصیه می‌شود تا برنامه‌ریزی حضور هم وطنان دچار اختلال نگردد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/665615" target="_blank">📅 15:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3ClRF-hEi_gt82dWu7KZ8ESRszrR7eNInkmfTwkLe1gFJa6J5TwBjYgUfUNGvk3idkwJKPpvOv0bOZutpvC8bAiY2JecfY6mhAkM3LTOwCTx_Y6LLwWfvPVfEJb9QYYhA091eToDkAXFeSBvZprM-GfVe1GteKO7F5eNkWXavZP4WjCtJFG4KO4Wfl57ZCaSSTWBg83F93Uy0MG2tk-VmyWloC1OFhYj5kCOLoELGrB1j0KCVhvI6gDN6lf0gq4w5_OhhSOEF1dxgtZNM34rsJgG-48gxRTeeqgaZzh0pby9139OMfhebsvp-t80X3zpqsxMiB88EsejO5WKtziHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور نفتکش‌ها از کریدور عمانی- آمریکایی با سامانه شناسایی روشن
موسسه تحقیقاتی HFI:
🔹
اسکورت آشکار کشتی‌ها تحت حفاظت آمریکا در حال انجام است. در این مدت، ۴ نفتکش غول‌پیکر (VLCC) با سامانه شناسایی خودکار روشن وارد تنگه شدند.
🔹
در سمت ایران، ورود نفتکش‌ها به مقصد بنادر ایران همچنان محدود است. تاکنون هیچ‌گونه تشدید تنشی از سوی سپاه پاسداران انقلاب اسلامی رخ نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/665614" target="_blank">📅 15:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665613">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت
وزارت امور خارجه پاکستان:
🔹
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند. زمان برگزاری نشست بعدی در اولین فرصت پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/665613" target="_blank">📅 15:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665611">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d3ad0855.mp4?token=Da0UkATK1mkhZ-SxsYmZ7igrrEJTJmKWo4z7auuzP2Qn5UFzfLmw_MicO-hy4-9hZj_CM1iRRXoQBHLDrTh_M1ykJ8Huz62V3TeDWwwTuW80RDNzTWoX-0DH9cu2dhVrXZzLPeprk0WX3y9N2xl9syaVpPWn-Qs7A37DsdanVY1b6R4iPURYq0sP03WjPhDljymk_0fCeYU2RukdbdE_Dc-Ai3R7H3yjaqG5smd9huoXBqI7VEsMURg5IiCmfj9Yn5_uuJ2JgCXNvN5EoxgKmtVaI0tFDSdJAZYyQlu3rN8GEcXdzEuR_LjO9qFrt6m90qmU3A_TRqc4FYMS4TonV3QYfQbz9c3oFBglIVhcT1yJsdJWzV1wYJbbzA_CuWwaIUMOqpm5DKDZ5KZSW7I5nQ4FuUekGkIWJVWXUfIz2CAtUi5fgfn5aT0D2Az5aK2RfPA-c3emN33mqg_Z377rtr-SchZfcq4CDZ91dd7eq8jnaA0DNxdLUnAuH-dp21dWx39YxvDeYY1WiK7M1AU8Iof9DaFfG4l663D0_gV3GGIhhNSEmHjI6hX5rNZT-RW57cD2vOSz-6fE7o_bPPHnRUO-_57GSdVgT149tt2uA3JUg5cSM0kvVm1i_uUNzGNhGV-Gz7dmfjDDe23Ai5be6s5Dv9FqTPmQxFI4K-csoRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d3ad0855.mp4?token=Da0UkATK1mkhZ-SxsYmZ7igrrEJTJmKWo4z7auuzP2Qn5UFzfLmw_MicO-hy4-9hZj_CM1iRRXoQBHLDrTh_M1ykJ8Huz62V3TeDWwwTuW80RDNzTWoX-0DH9cu2dhVrXZzLPeprk0WX3y9N2xl9syaVpPWn-Qs7A37DsdanVY1b6R4iPURYq0sP03WjPhDljymk_0fCeYU2RukdbdE_Dc-Ai3R7H3yjaqG5smd9huoXBqI7VEsMURg5IiCmfj9Yn5_uuJ2JgCXNvN5EoxgKmtVaI0tFDSdJAZYyQlu3rN8GEcXdzEuR_LjO9qFrt6m90qmU3A_TRqc4FYMS4TonV3QYfQbz9c3oFBglIVhcT1yJsdJWzV1wYJbbzA_CuWwaIUMOqpm5DKDZ5KZSW7I5nQ4FuUekGkIWJVWXUfIz2CAtUi5fgfn5aT0D2Az5aK2RfPA-c3emN33mqg_Z377rtr-SchZfcq4CDZ91dd7eq8jnaA0DNxdLUnAuH-dp21dWx39YxvDeYY1WiK7M1AU8Iof9DaFfG4l663D0_gV3GGIhhNSEmHjI6hX5rNZT-RW57cD2vOSz-6fE7o_bPPHnRUO-_57GSdVgT149tt2uA3JUg5cSM0kvVm1i_uUNzGNhGV-Gz7dmfjDDe23Ai5be6s5Dv9FqTPmQxFI4K-csoRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هجوم فرانسوی‌ها بر تهیه پنکه و دستگاه‌های تهویه
🔹
مردم فرانسه به دلیل گرمای شدید برای خرید پنکه و دستگاه‌های تهویه مطبوع به فروشگاه‌ها هجوم بردند. فروشگاه لیدل پاریس به میدان نبردی بر سر پنکه و دستگاه‌های تهویه مطبوع تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/665611" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl7JhEYsXGedy1mKQkD6MC_sm2tvYwdgFuWCt_6azQxgy1SOGmvmpi4HkQQK3_PV18IPrS3VxRhur4kGImlzjgzW7Jx3YPNw5_6F-ITZsPk5qbG-ooPdlaxYelhYMdwkVgt73siHRykUuQRWTu1DGOo0ANPkiP-CIRDASbN_CBCWDRlaHoeDpvN95oLh1FCWOtrO01qlQn71fnpa8br8VRVNrk8b8HUDSMkiNfpp8D1fprFa91d_s5aJcXtHdQB4Bvg0QBRjpUvQrOaB-xhZvG1PEB5S3Chvm3YH0qI-0Z32jNlajCOyB2_kvdX9LEF-RNQkQDZ7khgUwsYbGxqG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تفکیک زباله از مبدأ؛ اولین گام برای ساختن شهری پاک  شما هم به این پویش بپیوندید
👇
#نه_به_پلاستیک @Ertebat_baforii</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/665610" target="_blank">📅 15:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665609">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfpH6oy_dHKcZuis4vjyXVvctfGNNJxp2CtIEc-RvxmJdVzI0hWaoYo7_rcEBFVowx9I463jOstPGsBqBjpv5zXU4-NydKP6Lk2b3J4-U42JP1Mm640XnzYMlZ7HCJaLeU8WQAVqs9myFDh3SujArRWmf--f0IgkEc0Dql54bgilKoqE2CehbK_7yKJ8ZYy0Bd_MRi9AJ0S8LKT5zK1Q3xo_mBf4wv7y_foaWyvbgLl5NJDi9S1VA8LekAvQQ-mzIVVnbXa71GvJpwlLmDqRxrv6zZrWmchgCjpU-XCe532PZYzQgJ2bW3YpYIVcqfo-VRa6P1Bs40_rFZi_oP04Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست مهدی طارمی در واکنش به حذف ایران از جام جهانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/665609" target="_blank">📅 14:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665608">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONagQjOwUWsd_rd5gKS2wFnmgvp5mZK1unyWu-VJ9hKJS2GBfD_ob0tJlJRxvQjbSZOq2Je4XJ7cJAN4kSxowXozuJlCU1uKQWe0KHIiKUvVdGeasfU48TZJ4_mjNqtkYMKgLIIiVrdMHHomhWzvktrngvl7Nuz2bAZn9dGsbBNosqUmdUyiCIPpBkLmEp6dk1-jM4nrwQnXSwYFCh5tANZdR2A3sNU1fyDVVBDtPuitq4n0xdRP68rRbNZplvQ_wsa-rdsMtz7vYeKjGLxdZ3jt-OokV0EzRDrDrWe2Q73YJyjlXhDL3EBYpu3VZpmPryUmRAOZ3m5GtiTx4VbXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
با حضور متخصصان اکوسیستم نوآوری و به همت بانک مهر ایران
🔰
نخستین رویداد کیوتاک با موضوع تجارت اجتماعی برگزار می‌شود
🔸
سلسله نشست‌های کیوتاک به همت بانک قرض‌الحسنه مهر ایران آغاز شد و نخستین رویداد، روز پنجشنبه ۲۵ تیر ماه از ساعت ۹ تا ۱۵ با حضور متخصصان اکوسیستم نوآوری و بانکی برگزار می‌شود.
🔸
موضوع نشست نخست، تجارت اجتماعی و شبکه بانکی است و در این نشست راهکارهای نوین بانکی در توسعه اکوسیستم تجارت اجتماعی بررسی می‌شود.
🔸
بررسی وضعیت تجارت اجتماعی در ایران، ابزارهای پرداخت نوین در تجارت اجتماعی، تجربیات جهانی و مطالعات موردی و چالش‌های پذیرش ابزارهای پرداخت از جمله محورهای این رویداد است.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/665608" target="_blank">📅 14:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665607">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
خون شهدا با پول شسته نمی‌شود/ ایستاده‌ایم هم برای قصاص، هم برای انتقام
دکتر محسن خاکی، استاد حوزه و دانشگاه:
🔹
ایرانی شیعه‌ قدرتمند امروز خون رهبر شهید را فراموش نخواهد کرد. خون ماکان نصیری و سعید زارعی افسر ناو گروه دنا و خون رهبر قیمت ندارد.
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/665607" target="_blank">📅 14:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665606">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdtQnjoq--7nPbyZ9j42XAiwkQf1mdOr8HCmecOawe8oAXFU4UaSasTOHOACupl2tF7P00sPWYZzC_TU6ImCjg6oR14ksLmfB7tMkri82_fileHq7RcV0SQx3g9mlkxUPfqWAkL0v5fTCMLUXdU7nvsxQFjB2tjaa8ouNQMHT5WVIK0PP7Wzb5TUiQIn-QbSGljjNRiVlPcn2FOMr9Zog8_FU285EDCGqHkWLhgVSFIIh0VrfegJKo74OL4r_uk22iIKmoJI2KqgWHzGCamdvfkLX3TB9-zZiCDtHQnaWs51N8qls9dVWyKzKzQe42G1Jm6OP5Dx6K-6W9IGPzrqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
سوگواره بدرقه یار
▪️
علاقه‌مندان به بخش
عکس
سوگواره «بدرقه یار» می‌توانند پس از مطالعه آیین‌نامه، آثار خود را از طریق لینک زیر ثبت و ارسال کنند. در صورت عدم امکان ثبت از طریق سامانه، ارسال آثار به شناسه رسمی دبیرخانه نیز امکان‌پذیر است.
#بدرقه_یار
▪️
لینک ثبت آثار:
https://survey.porsline.ir/s/aU5VZuaW
▪️
شناسه دبیرخانه:
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/665606" target="_blank">📅 14:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665605">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDuvOJsjiZMa2RUtkN9h4BWHpID8zl4wkMpwUpSFcIJWTOWkb2Udm17W7iWbUiN7CiTdOy7LEShgBRFkyMUz9KnGtZP0HTmeEkcfAaO2kZEgkvaO8alohPS8UXiGXDgDG5nCP1NebBPCq0VKqPOURlflKs4fqMTrO7114qsjFUz2LapXW0xuq9k9JIaSDz3KAOoYLZBEcTyOceWfopFzeZ1Y81A6id5ecRl0rHRRC9VnOaGK3-kl6dNvBUszeutsT74LscOaENQs_uFGIEJ1Pnrk3_oU6l6B8Y-fMwCMBhi6TByN0LbJAI-G6b3Y8BWPJny_6p4u7qXH6w9t1eIMYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
واکنش بلاگر معروف کره‌ای به مراسم بدرقه رهبر شهید انقلاب
قهرمان هرگز نمی‌میرد
🔹
«داود کیم» (جیهان)، بلاگر شناخته‌ شده کره‌ای، استوری ادیورز ویژه‌ای را به مناسبت مراسم تشییع رهبر انقلاب منتشر کرد.
🔹
این چهره بین‌المللی که سال گذشته با انتشار ادیورز پربازدید «قهرمان» (HERO) در ایام عاشورا توجه جهانیان را جلب کرده بود، حالا در جریان این مراسم تاریخی، بار دیگر با اقدامی رسانه‌ای ادای احترام خود را به نمایش گذاشت.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/665605" target="_blank">📅 14:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665604">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
جزئیات تشییع پیکر رهبر شهید در نجف و کربلا
اباذری ، رایزن فرهنگی ایران در عراق:
🔹
پیکر مطهر رهبر شهید شامگاه سه‌شنبه ۱۶ تیر وارد فرودگاه نجف خواهد شد و پس از مراسم استقبال رسمی با حضور مقامات عراق، صبح چهارشنبه ۱۷ تیر از ساعت ۶ صبح در نجف (از مسیر کوفه به‌سمت میدان ثورة‌العشرین) و عصر همان‌روز از ساعت ۱۶ در کربلا (از خیابان ابومهدی المهندس به‌سمت بین‌الحرمین) تشییع می‌شود.
🔹
طواف پیکر مطهر در حرم‌های امیرالمؤمنین(ع)، امام حسین(ع) و حضرت عباس(ع) و برگزاری آیین‌های معنوی نیز پیش‌بینی‌شده است.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/665604" target="_blank">📅 14:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665603">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-text">📹
محمدمتین تنها ۱۸ ماه دارد.
خشونت، سلامتی او را گرفت و امروز برای ادامه درمان و توانبخشی، به همراهی ما نیاز دارد. مهرآفرین تاکنون در کنار او بوده، اما مسیر درمانش هنوز ادامه دارد.
❤️
پنجشنبه مهرورزی این هفته، برای درمان کودکانی است که قربانی خشونت و کودک‌آزاری شده‌اند.
🌿
نگذاریم فقر، فرصت درمانشان را هم بگیرد.
💳
6104337737614782
💳
6037707000289144
💳
6037707000426027
🔖
IR 180120000000001264298063
📞
*780*35260#
🔻
پرداخت مستقیم
Mehrafarincharity.com
🤍
عزیزانی که مایل‌اند به‌صورت مستقیم به محمدمتین کمک کنند، در واتساپ یا تلگرام به شماره زیر پیام بگذارند:
📲
+989101785282
⭐️
مهرآفرین باشیم
|
اینستاگرام
|
وب سایت
|
پرداخت آنلاین
|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/665603" target="_blank">📅 14:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665601">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iURQGwXXqTxYguNTkJX27bkB-RMTlTG6iq2Tx6-RGYRvySH5EwP0XL_xFxGZUp2gNi-PM0fdjgwp08N3QHDjvJqP31ZIELPkFViqdxi-lRpw3FHFLCdL94R9mkPs1X1E9JLvwxaDs3LDUVofMdJuwk0bUDjIvpjI049F2hwuAwk-Dq3IaW1A1JHV_OHfEW13FLQN7mPx8El7HjJLHsmOS9-tygDijHfhXXPlZIKAZGvLOyKDQAhc9YU1duujTlS9qLWt_7eyBFb4muq5PWV2rlTDdH3QNFWYvM2fCEQt_-9t3b3IcgOdm08GmZIRKwyN0nCYNMU7y7_vMUbpcz6P9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای جامع مسیرهای ورودی، پارکینگ‌ها و دسترسی به مراسم وداع در مصلای تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/665601" target="_blank">📅 14:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665600">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
استاندار تهران: ورود خودرو و موتورسیکلت تا شعاع ۱.۵ کیلومتری مصلی ممنوع است/ خارج از این رینگ، تردد خودرو آزاد است اما توقف ممنوع است
🔹
برای تردد خودروها در مبادی ورودی تهران، با توجه به اقتضائات و شرایط موجود، تصمیم‌گیری خواهد شد.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/665600" target="_blank">📅 14:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665599">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/28f1f15dd1.mp4?token=N3GbpLq9R3EbY7HcYFfcAfY_zHnKkOAiq5VdJbi-0lpdBA44MN-0L2D6PZBv9bWmmegPNx3DE5HX-IwSzWr0iEsgXcQ_Qm_L48F9H1IoPmcJRX5lWUkzsx5p4aLlO4HbMexIurgsYpBTZTx-YFFqboN8GNQbG1RDgNzMIEm0S0mpQPy4tojWMNhG3Gkg9zcgVMf9M65Ncw9cYOEBxy3lBn1x9x1TGoGs7BAKYlPc-r2hvc9RzwfeUDAGORwxrTpwhedcHdV251eG7AeTelMJ0PrVaTFWk08MfDxKU5eGbuI2wRk-vPBrUvDxI-NIlW-sbCJHiyr0dLNUxFVmhrxP4oaFGZuADQtPO1J16fz4Vhv5vzAsZGRwOvRB986R5eznIrBT69dGyaZdMKOhNuwgjG0nUm-L_iCzaJdjoDd1beTLxCAOnU4RKyNlWuNGQZ-fvaPx3NwconMjdJg6o4lW_BCWXrq14GFg3q0WNfAZP5Q8e6-PVv3fNDzEf0cjAnAYxv5jxRV_Qlacpk0-px3RxXs56qGueA63C5qe2fo5zZVHbuMAmcBvXh9YyNwv4l-3jk92mtyMHwfGGCOgZ_UUOk381BWw8p8CUwinH8hT__32REBRrGPf8nYq6HcTcvNeqDH73mkGr8qCtQ0OedaKnifPT6njnwTs8Uf2bT4_o1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/28f1f15dd1.mp4?token=N3GbpLq9R3EbY7HcYFfcAfY_zHnKkOAiq5VdJbi-0lpdBA44MN-0L2D6PZBv9bWmmegPNx3DE5HX-IwSzWr0iEsgXcQ_Qm_L48F9H1IoPmcJRX5lWUkzsx5p4aLlO4HbMexIurgsYpBTZTx-YFFqboN8GNQbG1RDgNzMIEm0S0mpQPy4tojWMNhG3Gkg9zcgVMf9M65Ncw9cYOEBxy3lBn1x9x1TGoGs7BAKYlPc-r2hvc9RzwfeUDAGORwxrTpwhedcHdV251eG7AeTelMJ0PrVaTFWk08MfDxKU5eGbuI2wRk-vPBrUvDxI-NIlW-sbCJHiyr0dLNUxFVmhrxP4oaFGZuADQtPO1J16fz4Vhv5vzAsZGRwOvRB986R5eznIrBT69dGyaZdMKOhNuwgjG0nUm-L_iCzaJdjoDd1beTLxCAOnU4RKyNlWuNGQZ-fvaPx3NwconMjdJg6o4lW_BCWXrq14GFg3q0WNfAZP5Q8e6-PVv3fNDzEf0cjAnAYxv5jxRV_Qlacpk0-px3RxXs56qGueA63C5qe2fo5zZVHbuMAmcBvXh9YyNwv4l-3jk92mtyMHwfGGCOgZ_UUOk381BWw8p8CUwinH8hT__32REBRrGPf8nYq6HcTcvNeqDH73mkGr8qCtQ0OedaKnifPT6njnwTs8Uf2bT4_o1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به ما اطلاع دادند که شهید کمال خرازی ترور بیولوژیک شده بود
صادق خرازی برادرزاده شهید کمال خرازی:
🔹
دکتر خرازی دو بار شهید شد!
🔹
من منکر تلاش‌های برادرمان آقای ظفرقندی نیستم، چند بار بالای سر شهید خرازی حاضر شد، آقای پزشکیان دستور مستقیم می‌داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/665599" target="_blank">📅 14:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665598">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyDd61n3oNWC3fYvD3_W-xUx691slzmPXm2BxO9nq5oKko8rJWEEc4A84PQp7OuSD2H13F7hUzS_scYw0r8B73vitwJ6eLmkB0wCyWUInIUEAmZdKOgXQfqg6yxoOzZDPu2fi_9-rldYjzXTm2BflvhL70zFTiiIjvzjjaGb5GxbM5KpCLalSB9iQ33QgnBK-os4ZgYOricesNILI1fL7042qiGU0M9SDnbsfwgClrzNxuEhlazI-91rkfZU48Pm734WJFONrQv2WcM-dteBkwacHN0msfkHGU1Vo0KcZKSG0pfBkEQb6BScwUkJF1QeR4USV4imNuziHBzgv_LSZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطعی برق؛ هزینه ای که مردم می‌پردازند  #برق_مردم_کجاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/665598" target="_blank">📅 14:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665597">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGWAJKVFCIW1RopgjHOWCvxhiB2eb1Hm6KO61kWzLKGSbPzTem2FNQZzUjipIhEqqZ3w8TIPalX_JLCkQQlPHBAxQaATZ9z9J4R0woKeXuxmR6lhycWpKL0iVtI3VPpYT8Sx3c1N4LfwTRXzgnlCuP6Dzq5O7BCqn_qSGvJFR9PBtP-ah6Rk3rbhtfsRxRL1rbWUrJsc_46_5rAdr3bD-E5_oM4S-KSYyCR0U3ZUN95dgy5T1COKgWJhNa8BHHQp6bOrRGYIFrTkOowL4G9GocdSK8jwN8JUbE3SiBdrQJqU_5rlNKS_YQX1soUf6HSN8493ZHSfN_PURwBfzed8xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | کمپین «جامانده»
🔹
اگر به هر دلیل امکان حضور در مراسم تشییع را ندارید و میخواهید در این مراسم حضور داشته باشید، یک فایل صوتی حداکثر ۱۵ ثانیه‌ای برای خبرفوری ارسال کنید تا یک همراهِ قلبی به نیابت از شما در مراسم شرکت کند.
🔹
در پیام صوتی، فقط نام خود، نام شهر محل سکونت و جمله‌ای کوتاه درباره همراهی و ادای احترام خود را بیان کنید.
🔹
منتخبی از پیام‌های صوتی ارسالی با عنوان «جامانده» در خبرفوری منتشر خواهد شد.
#بدرقه_یار
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/665597" target="_blank">📅 14:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665596">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAQ56V3znDLlP2yrHqn1zQCqf0AAWW8eGX9flGhWoQlwDB_m3He4ldV__y-9YTgn5F3kjt4eUYpsvA7wDp2JV_FXLKC6fnYRVPCKqerpk8jZzUqxqd864Tk2wLdC_CwB7G-7LBkjyZfwW0Xf_1KdFLag2z5aarAPIGvXYq9aUeuWn1s2HWDcw3nE4agUvxHGjjC82uexXceaFvrsZYcxNsk5SyUi2lwpTkwK1JRi-MkD21gLNM9Xl1cliEvCG1efjAn50B-OUO4VBdgGeyXKjYEPX3FZFA72qqnAA36MqGAjuxDYfOJo3YAXt2M4FZZ0z-pJDQ_RWIlMQvq2CkpDQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهترین گزینه‌ها برای یک سفر ۳ روزه در ایران
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/665596" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665595">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهفتم از فصل چهارم
🔹
در این قسمت ادامه روایت تجربه‌ نزدیک به مرگ خانم زهره ابراهیمی را که بعد از ورود به برزخ و دیدار و درک جایگاه خویشاوندان و حتی جنینی که خواهر ایشان محسوب می‌شد؛ به دلیل داشتن فرزند از خداوند بازگشت به دنیا را طلب می‌کنند و با عبور از میان اجرام آسمانی و درک زیبایی‌های بی‌نظیر آنها به جسم باز می‌گردد ولی از بازگشت پشیمان و دلگیر می‌شوند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: زهره ابراهیمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/665595" target="_blank">📅 14:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665594">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXVE49f5lmNiL2MbGzoeWt8R6myWq4g3a0zfz6DZ2A877sh5-JzCvg2xmdEPxAOKtRiiStOQBOJwVUCw0Qj_8GiwlMOgVTCDk8PZlf2aEqGrS5lg-PWwkDIYY8wP0h7EIQQcCQIATfAUrKhtwV575lJUWdeo6Ln6n8y1Lz6AwbjTokcHMuRJi9-HLRS9LPa6FUEvI0pmkBTdChcMmKjsA9eNEh3iDxxKurpAni_HQNhY82ypRk0tLdCIZ-SrxVmyRk1i3FQKxgcr6W-h2FqUkpJB1Qpm1WAg2X47Od1JRIAZffl1X-cWT0Rf6k0oV2QJ4d7V3ekaJxtShUq3XOwZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسارت ۳۰۰ میلیون دلاری به شرکت‌های دانش‌بنیان
🔹
برآورد اولیه خسارت واردشده به شرکت‌های دانش‌بنیان حدود ۳۰۰ میلیون دلار اعلام شد.
🔹
بازسازی شرکت‌های آسیب‌دیده در ۳ مرحله و با تأمین تسهیلات دولتی انجام خواهد شد.
@amarfact</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/665594" target="_blank">📅 13:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665592">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
یک منبع عالی‌رتبه به العربیة: دور بعدی مذاکرات ایران و آمریکا در ۱۸ جولای (۲۷ تیر) برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/665592" target="_blank">📅 13:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665591">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e472a6477.mp4?token=DCu-ZEaw9U3ZskN0Wp4dNa97XuRHcmH6lcHJXEP-hnx0NHvSv9FGKtnw1GkJDrBNJ3yxk0xEpK1S30BmJeHedIIAqB6MDq4weR93Af-f60VbXeykvlYqAybQBYQ9fy_QCC2c9yGAix3KXSaF-3Fky9D6KgjAUzfisbPWxwFh2Cbla9BhhS_QIeuXJwl4LA6_HE6ZHSZRqVeM9KrlSXNjP9yNw0P5nUjUBi1Ko66QhYLThXHZeomk9iau5G4sHTkeCWfniXEcB4wbF1sa1BNOirK9oEtXX9PwVfyOwwgSHMALfETqSC_ToJzJLtr-XbXO6O7hg-4RxFaKLtwSHvske41MqK0ToRPf7B7JrMTSQaaow7acNAIiyJd-ed445vashUkVVFACodZir75TWMtOjE2Iu9ZixrqZBCvDcqEtHk2wyMMxLoTD3WUPr8jGlc_narre3hsPEwC32uQG7fOhTJFl-XUQEuQGHtn2PNjj799cv5E9qCAbURZR2UpDgmWWpKPGkLzV914BYD0Ahzr8y9KHRfOkUbnUZ4peeacqoIANHtqG9EPTSVJ0Rx9khnFd9VQ7rykpyyGOhHz7-5Y6Avcbz6XBdbsevpXYn4qYZfJ1BwXifkiH1l50U7FX5kR0As9-cUH0rLyG17KqAZ1mxavT7SC3gB2vwGg4YYEelXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e472a6477.mp4?token=DCu-ZEaw9U3ZskN0Wp4dNa97XuRHcmH6lcHJXEP-hnx0NHvSv9FGKtnw1GkJDrBNJ3yxk0xEpK1S30BmJeHedIIAqB6MDq4weR93Af-f60VbXeykvlYqAybQBYQ9fy_QCC2c9yGAix3KXSaF-3Fky9D6KgjAUzfisbPWxwFh2Cbla9BhhS_QIeuXJwl4LA6_HE6ZHSZRqVeM9KrlSXNjP9yNw0P5nUjUBi1Ko66QhYLThXHZeomk9iau5G4sHTkeCWfniXEcB4wbF1sa1BNOirK9oEtXX9PwVfyOwwgSHMALfETqSC_ToJzJLtr-XbXO6O7hg-4RxFaKLtwSHvske41MqK0ToRPf7B7JrMTSQaaow7acNAIiyJd-ed445vashUkVVFACodZir75TWMtOjE2Iu9ZixrqZBCvDcqEtHk2wyMMxLoTD3WUPr8jGlc_narre3hsPEwC32uQG7fOhTJFl-XUQEuQGHtn2PNjj799cv5E9qCAbURZR2UpDgmWWpKPGkLzV914BYD0Ahzr8y9KHRfOkUbnUZ4peeacqoIANHtqG9EPTSVJ0Rx9khnFd9VQ7rykpyyGOhHz7-5Y6Avcbz6XBdbsevpXYn4qYZfJ1BwXifkiH1l50U7FX5kR0As9-cUH0rLyG17KqAZ1mxavT7SC3gB2vwGg4YYEelXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان چفیه‌ رهبری
🔹
خانمی‌ که رهبری را قبول نداشت اما حالا میزبان و خادم زائران و وداع کنندگان با رهبر شهید است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/665591" target="_blank">📅 13:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665589">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7d3be04f.mp4?token=dDU9VlEUJZis7pMhj7txvQV37kv57DH7nEqb05KB5BdtID6Mc5byr-bwEyC3Q0QOQqAS8zJAoJLqc07jeeGUCtEXPjbv1dLh8VY2T8Idr4tMGS5ME3CeZrjGy0BGXUrPYrpVoQ4lWPyLZ3unvluOMnPuDLfFOjlDFWaEqtPHQN26RfwiA4jXEjdmXj_O8zaVPdISDw3xdFyVtPKFPMNcOxgSbu_JF3U53Pr5oq6hvig6DolILxswDdJC0UAnh9copccgBRBtImz_Nxpf_o67evkU2vj6UNMuoZyMx9lCICxnjtEIJKnpjvo73LuVt9Y_9qZNQ2tcGD5dhkRqPBO0xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7d3be04f.mp4?token=dDU9VlEUJZis7pMhj7txvQV37kv57DH7nEqb05KB5BdtID6Mc5byr-bwEyC3Q0QOQqAS8zJAoJLqc07jeeGUCtEXPjbv1dLh8VY2T8Idr4tMGS5ME3CeZrjGy0BGXUrPYrpVoQ4lWPyLZ3unvluOMnPuDLfFOjlDFWaEqtPHQN26RfwiA4jXEjdmXj_O8zaVPdISDw3xdFyVtPKFPMNcOxgSbu_JF3U53Pr5oq6hvig6DolILxswDdJC0UAnh9copccgBRBtImz_Nxpf_o67evkU2vj6UNMuoZyMx9lCICxnjtEIJKnpjvo73LuVt9Y_9qZNQ2tcGD5dhkRqPBO0xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محله به محله خود را آماده میزبانی از مهمانان رهبر شهید می‌کنند
🔹
سهم ما در میزبانی از زائران و وداع کنندگان با رهبر شهید چیست؟
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/665589" target="_blank">📅 13:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665587">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyENBaQkUf5z1LROTBFPLF7UmLS9Q5qbiDl4ciQf557gEZLgv_bkv2FrzIhnjTmmwtqw9JpTsFWp7GcuJiLtY3jlDiwqdefncgyC2iYlsrUnrqeZr8kEhjosY0fwTEKYqxY3c2st6m4N_kxY_u5CxucbbzJ7nwFsVrd3Aupxp9XiB4HjI7zTyypt5mTd8xk-_jRAz4KQZYC1rsqnzj4wcT97IzkmQnEAE5_OeW5uk_jnRImttOc3xpRy47RTHr2Pmu2bFmS4VFsNatss7VFv6sVIGBzxCfGG2iOtC8NW-U78Hmsz5Jd0sD4Z3kOqLnnSsUCe8UW-hCZzCnDfQIP8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قتل دختر شایسته ایران در ۷۲ سالگی/ قاتل ریتا جبلی در ارومیه کارمند بانک است
🔹
پس از انتشار خبر قتل یک زن ۷۳ ساله در ارومیه و اعلام دستگیری قاتل از سوی پلیس، اکنون جزئیات تازه‌ای درباره هویت مقتول و انگیزه این جنایت منتشر شده است.
🔹
هرچند بخشی از این اطلاعات در صفحات غیررسمی شبکه‌های اجتماعی منتشر شده و هنوز به تأیید رسمی نرسیده است.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/665587" target="_blank">📅 13:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665586">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
برنامه‌های رسمی مراسم وداع و تشییع رهبر شهید از شنبه در تهران
استاندار تهران:
🔹
برنامه‌های رسمی مراسم وداع و تشییع رهبر شهید از روز شنبه در تهران آغاز می‌شود و پایتخت میزبان زائران از سراسر کشور خواهد بود.
🔹
مراسم اصلی در روز دوشنبه ۱۵ تیر برگزار خواهد شد. تمهیدات گسترده برای ساماندهی حضور جمعیت انجام شده است.
🔹
امنیت کامل مراسم با مشارکت نیروهای نظامی، انتظامی و امنیتی تأمین شده و زیرساخت‌های تهران تقویت شده است.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/665586" target="_blank">📅 13:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665584">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b19dd71f2.mp4?token=YKKgwMYUWrDW8S7kzmG65-rJD4dApEkavdWZqVflnpb2rmfoC9lBJjXsgYKD01v8ZwTT8M4PoqAVQej-i3bulz2-YI7sAobu4EMv9rI2pd519JhhldXyJHYT9tUJMWWU9q5h5ZpT7VL0-4oX3awuh1T4rRm2v7IrCaoZGm19k2K8EdaZ7b15XXEqbzM8q1T95pG4ojFKkp2zfgMs0yTQBF_MtzH4xi3X2wnjNn6qUJr3mIFHFSdIrH0RUIkJ5i2_0GQpjjTkScEWjp_MsVErvnIty1RymQ_UmYorZ_4IcyQAMYTnJga0nMg0EwdXOE_W5dxQXih_yhi6ZGwzULjk9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b19dd71f2.mp4?token=YKKgwMYUWrDW8S7kzmG65-rJD4dApEkavdWZqVflnpb2rmfoC9lBJjXsgYKD01v8ZwTT8M4PoqAVQej-i3bulz2-YI7sAobu4EMv9rI2pd519JhhldXyJHYT9tUJMWWU9q5h5ZpT7VL0-4oX3awuh1T4rRm2v7IrCaoZGm19k2K8EdaZ7b15XXEqbzM8q1T95pG4ojFKkp2zfgMs0yTQBF_MtzH4xi3X2wnjNn6qUJr3mIFHFSdIrH0RUIkJ5i2_0GQpjjTkScEWjp_MsVErvnIty1RymQ_UmYorZ_4IcyQAMYTnJga0nMg0EwdXOE_W5dxQXih_yhi6ZGwzULjk9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیوارهای تهران هم این روزها داغدار هستند
باید برخاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/665584" target="_blank">📅 13:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665581">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB62ds73BPlRcjZkFjYlhhFGoNqX-nKfAzdwcdzUBCpcMi1QzAWDZ9nzd5iiV3L-0VsySGDodeZDZFojmj0eFoeBETNVHn2d5frUgJqQjIXWt6G3-UwUm2bp-eOYFWVDyH1B3wFKLTC5KqtMoRiOBH8H-5j8JV5Tbt9xIfqPqekGZ4brRAE0prCRDT17f1pry9PMQogHbI28xiychUK17F0TebBMSdlo3Kv0BBJU9xu7qRFnDZj9x-2q4ghdC77MSBItxvq5eFgg1-_f9LIGXfEJM2k2fnx9k7is8fo8mSs_3Uj1J0GZWIUqnOa3e8vIQVaP6bn0f2MAViC5h98lQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر لیوان نوشابه؛ ۱۳ دقیقه از عمر شما کم می‌کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/665581" target="_blank">📅 12:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665578">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfe108375.mp4?token=jgnkLHB8Qg4ubGiCDgNvvJI15uEXKPdwlQSiS_yezqvc_J4IJLQOpAhJ_lqgwGWYObYKlqW-cMDRY6rnaXIwwsMOTKJCfEtK97B1Ao7U7wz2fzrPTTD4bvf7cKgPV0c6tkEH0bw0d7KEf4ug42DU8eIyCXazjbGzCd9BhekZljAyzNmQPqKjq7fF4QI3qmGzCZGHzhc2liVC6x-5eCuo5kfIk6bE8T_AjAwnR75-Qytmgf14YB8KQ45LltvroIoPbJ6kWS2abAKZffocinSZFpAVxGZuEIw-ZSwGY8G2RjKXM2Ke4VcIupKklvc11f1o16gp1LMiVo5muqtYuebUGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfe108375.mp4?token=jgnkLHB8Qg4ubGiCDgNvvJI15uEXKPdwlQSiS_yezqvc_J4IJLQOpAhJ_lqgwGWYObYKlqW-cMDRY6rnaXIwwsMOTKJCfEtK97B1Ao7U7wz2fzrPTTD4bvf7cKgPV0c6tkEH0bw0d7KEf4ug42DU8eIyCXazjbGzCd9BhekZljAyzNmQPqKjq7fF4QI3qmGzCZGHzhc2liVC6x-5eCuo5kfIk6bE8T_AjAwnR75-Qytmgf14YB8KQ45LltvroIoPbJ6kWS2abAKZffocinSZFpAVxGZuEIw-ZSwGY8G2RjKXM2Ke4VcIupKklvc11f1o16gp1LMiVo5muqtYuebUGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونالدو از پنجره هتل محل اقامت تیم پرتغال، طرفدارانش را غافلگیر کرد و برای آن‌ها دست تکان داد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/665578" target="_blank">📅 12:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665577">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4764cb20.mp4?token=DbeYoS81MUiYlxs1z14YLSuJJE7NJkOkFtG2C1QbZjBUMDA0VRpniIeVsKe2_lecWpFiUyBKUIGFKOXyhbV_qe-vHh5bRHyf2vEUtRa7qeJdGI8COiTZnjhdP794JgwnIRqi6TW0yGvCnLSbhMMIflBcHvhLI1CLEtVCoVhdK4GHwxNu6yHaocxLlQWS5pLdwztXv8SeD4ppANKim-3KQMsHg4JG_4LcY2gL8yjPpeookMJDAKcCGPdwAsh_VKi5eRWjhK9V8Gc5Ae2LXCLCBER0aSBMSM9_yob7Z5O_GRatOa2h1yxCYbPtdd-5Vu1pesiGQxPdfXKJkZkpN01BTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4764cb20.mp4?token=DbeYoS81MUiYlxs1z14YLSuJJE7NJkOkFtG2C1QbZjBUMDA0VRpniIeVsKe2_lecWpFiUyBKUIGFKOXyhbV_qe-vHh5bRHyf2vEUtRa7qeJdGI8COiTZnjhdP794JgwnIRqi6TW0yGvCnLSbhMMIflBcHvhLI1CLEtVCoVhdK4GHwxNu6yHaocxLlQWS5pLdwztXv8SeD4ppANKim-3KQMsHg4JG_4LcY2gL8yjPpeookMJDAKcCGPdwAsh_VKi5eRWjhK9V8Gc5Ae2LXCLCBER0aSBMSM9_yob7Z5O_GRatOa2h1yxCYbPtdd-5Vu1pesiGQxPdfXKJkZkpN01BTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دیشب جام جهانی ثابت کرد تا سوت آخر، هیچ نتیجه‌ای قطعی نیست!
▪️
قسمت یازدهم برنامه جام تایم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/665577" target="_blank">📅 12:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665575">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56b2cd5d1f.mp4?token=nmVoF7GYWQ3dtIgKuhWG-MIkT7IDLFRprqidrjW5EenRGRm5hwHRHNguN7Gql0xo5BetyaoVqrboMxX97JohgDOA3VZy-DAFJhURDmW9ZZzdvOdbm_QwyA-fy-6VtcgcyfyTMIbUMtJSIeO8OL11nHucOp9MNjx_UMh0_FfxFMRQLoz0VENPep-_50e_mo-7PhpsRBY8isT5XHkQR9FwyO0Gja4GUdNKar2xUab4DtnaSsg2GtXXMvSBAoVyzHbKwO8r9CAOzKFs7dbt8fAFJjOpLIlNbttrUVo-fbkiWM45xW0Jjbd6X3WPXCmarTTETobjXS2Zj6yfhekOyJXs7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56b2cd5d1f.mp4?token=nmVoF7GYWQ3dtIgKuhWG-MIkT7IDLFRprqidrjW5EenRGRm5hwHRHNguN7Gql0xo5BetyaoVqrboMxX97JohgDOA3VZy-DAFJhURDmW9ZZzdvOdbm_QwyA-fy-6VtcgcyfyTMIbUMtJSIeO8OL11nHucOp9MNjx_UMh0_FfxFMRQLoz0VENPep-_50e_mo-7PhpsRBY8isT5XHkQR9FwyO0Gja4GUdNKar2xUab4DtnaSsg2GtXXMvSBAoVyzHbKwO8r9CAOzKFs7dbt8fAFJjOpLIlNbttrUVo-fbkiWM45xW0Jjbd6X3WPXCmarTTETobjXS2Zj6yfhekOyJXs7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا Svalbard نروژه؛ جاییکه خورشید هیچ وقت طلوع نمی‌کنه
🌘
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/665575" target="_blank">📅 12:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665574">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fc47TjaU9JWAQOdL6OZBv1tmTo55U0nBlRLG629-RZ1dt6WoZ6mR7no0fSWyXpnRpV1V9nHGN-yn9EzIlCAok2JUiCQ3ICDFn-g2ucqarl8Sl_XXwnDE6mXyAjtmws0qj3wo-BY2irRXi4I43ynPP_Qb2jzPNjQXhQKRv39BEtIobtz5N4xh3QvzDRmjMMop_7hsfdJi-rZ4NyCtUOE73eki3et9jZ9rXbfuyz70QnXE_dE3pMt8T9BRMP3SxrMbhvPK6A5fIXUzmaCDII3hDLvnVcEQqp8IirB4-kkRSwb_koxvyKfFjZTKO4UpooRTdo3GxEfOpjA1O4L_jyccnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امباپه در صدر رقابت کفش طلای جام جهانی ۲۰۲۶
🔹
کیلیان امباپه با شش گل و دو پاس گل در صدر جدول گلزنان جام جهانی ۲۰۲۶ قرار گرفت و در رقابت برای کسب کفش طلا از لیونل مسی پیشی گرفت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/665574" target="_blank">📅 12:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/665571" target="_blank">📅 12:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665570">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsOFwYL9lBJxN_h79m24IcDiOjGm5nhnhZAlC3RxH-VZpilLp2sljbl1OIoF4Hhy8t3v5N6cOLMOMcqOdW8bCibVHR6Hsx8rPui-HobPs_14J3eytIHfwb1jSf-_4FFFlWX0BrzOFtcw-KwPyR_2GBu05Y6ayOz9zRwHZhQza49CChM4LwxeJkFy7NS3oN7geRSDI8koqYfuf5PaGTXgCorObDl1-mDtjhtxMy33H5sP2XgUV16zGOZvAClAqsC7MA4M1SMkDfI81HqqPyAim_mIWHcnjJmd-RiBnxup0AlmwbEOaXFvzHv6RTX5WD7knIP7JeA82aDOp1poYvqrdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه رسانه‌ها ذهن ما را تحت تأثیر قرار می‌دهند؟ با این مهارت، قربانی اخبار جعلی نشوید #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/665570" target="_blank">📅 12:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665567">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c23ae14f5c.mp4?token=kpXCFJpKs2pDYYZlrr4d-j-iUxULpzQwgEcDVksqYV_bl86R91tbAJ9dCallEiIrZrnn_WIRZJc66C3je0LW61623f6Bo99j6J7FRYBilcdTfvibleHMpD3AGZ5Qdfp3XTFCoX8qLL-ghYGah0V02I0ltIXACQNjCtFxrdTcpS0U_AG1wwYBolJurXu-_MjwVTbJmvkyF-7A_7g3to2DuQfXw5XMrxWAXrwXT8N09ILvnDPLallufQcYZeI9ic7__0MoERt-y-7fc8d5mDAfTMigF6kb24iWOlqhR_50w6IpDTKGbZCYjlVSlxoCmHXPYA03TTNBkKPgqPlKFNN2mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c23ae14f5c.mp4?token=kpXCFJpKs2pDYYZlrr4d-j-iUxULpzQwgEcDVksqYV_bl86R91tbAJ9dCallEiIrZrnn_WIRZJc66C3je0LW61623f6Bo99j6J7FRYBilcdTfvibleHMpD3AGZ5Qdfp3XTFCoX8qLL-ghYGah0V02I0ltIXACQNjCtFxrdTcpS0U_AG1wwYBolJurXu-_MjwVTbJmvkyF-7A_7g3to2DuQfXw5XMrxWAXrwXT8N09ILvnDPLallufQcYZeI9ic7__0MoERt-y-7fc8d5mDAfTMigF6kb24iWOlqhR_50w6IpDTKGbZCYjlVSlxoCmHXPYA03TTNBkKPgqPlKFNN2mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌شود نروید؟
🔹
۱۳، ۱۴ و ۱۵ تیرماه، آخرین دیدار مردم پایتخت با آقای شهید ایران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/665567" target="_blank">📅 11:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5d1b8f75.mp4?token=hWeLckRdtIm6kV7U59mepMqz4zo7CvxKhcrUfL851OkUwPSpvy4vrbnzI_xIldA4Banr9NVbXUwAFM4z8kEZbS2mz4L7Qt6BZWLI7dB4voiIZULKvxY6J3SXGUuO3qkhql6ZN8nyXv0XffMr7jHfQDybjQNU0qOQIG3e-37sKPkpQDNjH8LyNa-L8Kkii2UEIku6An9qFLtAvFyrj1CkIkXIWAnH9s_-QJ8CxoGZbHtN-gVpWtBlcoWnX3UDCPO0Ci2N58y9i7Md0Xtm9H7uM359v1ZtSdtjYXynPLWXFcu2audI4LM2UAtKz5Gb39oIlX7kPy0xJ3zsB4BOF9vDxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5d1b8f75.mp4?token=hWeLckRdtIm6kV7U59mepMqz4zo7CvxKhcrUfL851OkUwPSpvy4vrbnzI_xIldA4Banr9NVbXUwAFM4z8kEZbS2mz4L7Qt6BZWLI7dB4voiIZULKvxY6J3SXGUuO3qkhql6ZN8nyXv0XffMr7jHfQDybjQNU0qOQIG3e-37sKPkpQDNjH8LyNa-L8Kkii2UEIku6An9qFLtAvFyrj1CkIkXIWAnH9s_-QJ8CxoGZbHtN-gVpWtBlcoWnX3UDCPO0Ci2N58y9i7Md0Xtm9H7uM359v1ZtSdtjYXynPLWXFcu2audI4LM2UAtKz5Gb39oIlX7kPy0xJ3zsB4BOF9vDxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر درباره کولر ماشین سوال دارید، این ویدیو رو از دست ندین!
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/665566" target="_blank">📅 11:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665565">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKXcS9tdKGYrlEJI8SMmzRMk-aVV9_Pogis_Jru07UYNMczwk0PmgHAInlrS6OHYYHil1rX9TUTkwPKRF6fEAnj4lr1T38h8CjmH41So6eINiMpAOXIVT531UfXrdvO0IQmMk-NDDVbcn3K6kadg4SmU71HmwoJiMwhI-mU8JzIG69qChqQBV-VKepHmcgwoLgsHjIWfPzWS-A_uii5Ek-3M0ajPeq6hv1KujnMjF0Yxsv9farAeOslWCeyMWjZ0PhP1Y4M-o_6iTGZNJWr_vblQINB-sAb1w9PYA53ofO6iPPHFM4EAA5ogsTDCxYJhZIjokgFeIZQS1UBA8tp0tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیش‌بینی وضعیت جوی مراسم تشییع رهبر شهید در تهران، قم و مشهد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/665565" target="_blank">📅 11:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cpswb5snk_zGM7_6rbZEddzVGFMlnQLDj1CPffpCwBN7WYMWOcx1q2_1LvVxTPuqrLMTnJtq4tZQ8_FvoOtbSkkYOag9n6ETmOhB_Dkv6t_m0g6Ip2PkqcAcU0R1GKFJDmR8PcqJ2-AqqWQD90P8shb4IsrsR-Bg7213-GUJnX5XhLp18_sbLP0Wr84y6lKXIJgKqKIw1tAe6qvdm_Rir3pen30K1XkplOEMgA08Uyt7XeyTRawWjxNq9ZvrPPChP9WHgGak8wxhgO3LfMbFYRkI1drseZ5KTPNRHHFYJur8ZecpW4Bu70xYrJPDseVwnvZ4LI1SkmFM8whFznSMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز ۱۱ نوع چنگال که نمی‌دانستید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/665563" target="_blank">📅 11:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
مجموعه «چهارباغ» به فضای جدید وداع زائران در شمال مصلای تهران تبدیل شد
گودرزی, معاون خدمات شهری و محیط‌زیست شهرداری تهران:
🔹
این مجموعه که قرار بود به‌عنوان بوستانی متصل به مصلی برای نمازهای جمعه و عید فطر مورد استفاده قرار گیرد، اکنون با تلاش جهادی به فضایی برای وداع مردم با پیکر مطهر رهبر شهید انقلاب اسلامی تبدیل شده است.
🔹
با توجه به پیش‌بینی حضور گسترده مردم، مجموعه چهارباغ به گونه‌ای آماده شده که زائران بتوانند بدون ورود به صحن اصلی مصلی نیز مراسم وداع را انجام دهند.
🔹
همچنین مسیرهای دسترسی از بزرگراه شهید همت، پل روی بزرگراه شهید سلیمانی و ورودی‌های شمالی مصلی برای تسهیل تردد و کاهش ازدحام جمعیت پیش‌بینی و آماده‌سازی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/665562" target="_blank">📅 11:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f605d3aea7.mp4?token=fPf0CPVfwZW_2mGkPuarW97kBlkU2ylDduDSW6iKJywb9FzRlCeKWSmgtD58Cty-ZBfhxCxjI4cxi1RAdeRzMEaHnbGZ-UMM5a5k8GabsqP3SBJ8wc41ke1iElxxywkV-DK4TAN814A2RMn6N2CpVyDHiJXnX4JZIlajbN5Lyj0xz108rh8YhXtKUJjLxC0fdKHShbVOdnalSzVk-xGh0Dp9WLOV-hVMQMRCiebXbdd9dJrg9ws9YiUvy0TKA026pU0zV3ZI5bHK4NZTSRWUJVHHb4GmAYdcUDwuebmuK3-Qs-_FDV2XObgugylo4l425FzKkSfarVVL8znXtGfD7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f605d3aea7.mp4?token=fPf0CPVfwZW_2mGkPuarW97kBlkU2ylDduDSW6iKJywb9FzRlCeKWSmgtD58Cty-ZBfhxCxjI4cxi1RAdeRzMEaHnbGZ-UMM5a5k8GabsqP3SBJ8wc41ke1iElxxywkV-DK4TAN814A2RMn6N2CpVyDHiJXnX4JZIlajbN5Lyj0xz108rh8YhXtKUJjLxC0fdKHShbVOdnalSzVk-xGh0Dp9WLOV-hVMQMRCiebXbdd9dJrg9ws9YiUvy0TKA026pU0zV3ZI5bHK4NZTSRWUJVHHb4GmAYdcUDwuebmuK3-Qs-_FDV2XObgugylo4l425FzKkSfarVVL8znXtGfD7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱٠٠ کیلو طلا؛
جایزه ورامینی‌ها برای قتل ترامپ و نتانیاهو
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/665561" target="_blank">📅 11:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d307391130.mp4?token=BMMc4v_90j2V_F2hYQg1Bxn_rBEBfxGddYqRLXOVueXlP0Vbi58P_Ec5sn1A7woN-WrqMpZ6XbgjxAlL3XDk7Kv7p2z2I_YzPLJOVfkS1hckcT8QA3nX_16C6O3isNg1PCBoSTDGryB7ydfRyV0sMGkvpETENT0PB5e5d-50SqoYObsFZeAX1GMefGRV1oe3SVz_vw_NM1rctAnDI8cEruN7DSCgd_ZLdRGE1E1p6xuNBv1odzFo9SrD-oo2iSyVOCIbb4aJrLyd6v7_TFXKRVW7K3sqYHdOQH--TfBeGmdo9zbdyuyq-VFhfNAMeALrP4TZ2E7_1SaKam9JZLwTV4lFa9hc00JFfKWBivQzxXunhsy0WJzjHAkOU4sq4PsgLE2_aemFRKAk643e-Vnbc2-PzIzRpPuaXgQCFq5C0uQEz2aPMm1IW9l5qhRRICUnQmGiQ2DguAtG72sz1veYEdyE1ZB1GrBMrHpBJwaNJ2bF875IRQhdggQFHconc7o5MwRr4ADts9WibjY1ddAMEDhDDiYCdBcS6TvZDzoBhfieQbEfr2HBwQApc37_Wsy_AxpxvukCPuUoxve1OkNXyRNzQtesL0BslZzth5F1Gg4hBOV1ZpiQN5DIxfsny3Ypz87UOYahV7ykhlf53-Xjx_2nlj3i9dMa5JoQ2Nxo-5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d307391130.mp4?token=BMMc4v_90j2V_F2hYQg1Bxn_rBEBfxGddYqRLXOVueXlP0Vbi58P_Ec5sn1A7woN-WrqMpZ6XbgjxAlL3XDk7Kv7p2z2I_YzPLJOVfkS1hckcT8QA3nX_16C6O3isNg1PCBoSTDGryB7ydfRyV0sMGkvpETENT0PB5e5d-50SqoYObsFZeAX1GMefGRV1oe3SVz_vw_NM1rctAnDI8cEruN7DSCgd_ZLdRGE1E1p6xuNBv1odzFo9SrD-oo2iSyVOCIbb4aJrLyd6v7_TFXKRVW7K3sqYHdOQH--TfBeGmdo9zbdyuyq-VFhfNAMeALrP4TZ2E7_1SaKam9JZLwTV4lFa9hc00JFfKWBivQzxXunhsy0WJzjHAkOU4sq4PsgLE2_aemFRKAk643e-Vnbc2-PzIzRpPuaXgQCFq5C0uQEz2aPMm1IW9l5qhRRICUnQmGiQ2DguAtG72sz1veYEdyE1ZB1GrBMrHpBJwaNJ2bF875IRQhdggQFHconc7o5MwRr4ADts9WibjY1ddAMEDhDDiYCdBcS6TvZDzoBhfieQbEfr2HBwQApc37_Wsy_AxpxvukCPuUoxve1OkNXyRNzQtesL0BslZzth5F1Gg4hBOV1ZpiQN5DIxfsny3Ypz87UOYahV7ykhlf53-Xjx_2nlj3i9dMa5JoQ2Nxo-5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازرسی بدنی «لیونل مسی» توسط آمریکایی‌ها روی باند فرودگاه و خنده‌های ستاره آرژانتینی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/665560" target="_blank">📅 11:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌
♦️
مسیر نهایی تشییع و بدرقۀ رهبر شهید در مشهد اعلام شد  دبیر ستاد آیین تشییع رهبر شهید انقلاب:
🔹
طبق آخرین برنامه‌ریزی‌ها، آغاز مراسم در مشهد از میدان فرودگاه بوده و تمامی خیابان‌های اصلی شهر، محل وداع با پیکرهای پاک و مطهر خواهد بود.  #اخبار_مشهد در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/665559" target="_blank">📅 11:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665558">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpcJU30JW9TcyPaKTVXs7SGT9jtO_ajdGwp7sCjCjCuNN9lhbmmSI-YJG8E6LMkgJ-sjh06kQR7THczMiS7YB3bMp9vMRhCk8uXdlKXsI9p_N_xY_6m2AQCw6ZfWQOnCg5LT-CrrqHcIMKpQeunwkDRiK_112V_JtZkPhKl-byb2SYXLxPH46UerNHvSe5zX25wmd-pkihgmi6B3oX5vZp0N_b7dsez0JnZEHREO6CppXJ3OzYC0vArXijd1m7g6ZnRHfFenSPiOqH91zCD-vu89b2rQCk1lB7qccd4Hf6s30JVqBG-B4mNgochVrOJsb_ySWycF-Qsc7896-v9hnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردشکنی دیدار ایران و مصر در جام جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/665558" target="_blank">📅 10:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665557">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
مهلت بهره‌مندی از معافیت سه فرزندی و بیشتر تا پایان سال ۱۴۰۷ تمدید شد
فراجا:
🔹
همه مشمولان دارای سه فرزند و بیشتر که تا پایان سال ۱۴۰۷ واجد شرایط معافیت هستند می‌توانند با مراجعه به دفاتر پلیس+۱۰ ازاین معافیت بهره مند شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/665557" target="_blank">📅 10:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665555">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JblaX62A-76SkeHAB991yXlHZ7kimX9TE6YgT4kwSqbOocGDV0B2VMCaU3inIvmqDczaU7nHTUhzfgUwmc36uSAUzWPnpAESkvJHfja4ecbXNC0SUxCBdjx1mg8GqoPztMREf6M5-3FrYnMKT-Wi6fsYTd1q5cRY4T8OfCYna19LfdMkI0n_T41OPBpyrG13OTS_qhZugH4G_QGeRq2FEIeawRk6u5ziQv-sdLkXms74SMAUaoDV1oXemMerFpay8FbMCfOwZoEEagMBhk0AfR0-I0w47oYyhtyGPlWqcWhwNcFWAyeOHJgTVO0ALUApk86UL7L1ViglOdnUKqrqUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCoDsJnbe2lYEZupsiXaKUwZKx5RZBFhPikXOgmBZQLtdvWI-BwL8JnMGcXQyII63ya6A-xu14y9Mp-ii454qMAlEynw6PMgiSGnI2_TSFqk02aBL7-vobjVUnl8oip15CiOmkpf__nGm4zKOCp30Q_1KKsysUTHUBDSms5Hj-I4tB31rSdCsiPmzsbu6FaqgDUrKnqHnHii6pOm2baRkMRCU5Q1zUj2tNsDIB5Z3InmJljUc6gXyqmg30VHzinLy2o6UaQ1WDMc3Tl6dkBJq6a2XehTKMMu_7uAXaD9XDCnUnoD59xdW0RnkrZjh3YP2GDvWR0djY256QTNkjoItA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۱۹ درصد خانوارهای ایران مستأجرند
🔹
حدود ۵.۳ میلیون خانوار (نزدیک به ۱۷.۵ میلیون نفر) در کشور مستأجر هستند.
🔹
تهران (۳۱٪)، قم (۲۸٪) و البرز (۲۷٪) بیشترین و هرمزگان (۸٪)، آذربایجان شرقی (۱۰٪) و گلستان (۱۱٪) کمترین نرخ اجاره‌نشینی را دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/665555" target="_blank">📅 10:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665550">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kI6GZ5UL4cgYeS9_hjxtHjaCP1IJkz-HlGz3iHUaeB0DeVudUf9Dni4aqefvxfvxJ86h6o8EEJeAHOkI-fQDWM5J5Xc13wpWoHljeotIrgBfPw79Jx8tsXhypcbWmVHmrLNN_tmw6Z-hhwUATe15CgfcxfWbwwBF8PuxD-EzEkO-c3C35WAJC3_qO7b56PZ0EDIvIQKshKlQzX8ePspTcRwaxQ1NVDet_5r7zD-jDO1qSav0-hSQ0F8XKxrAGvxrJswa8j8OyOOD8AHIwXk2JXqXbf55jl55as4BUQNz2MzYCgReq8hEZ_EqvdnZJxwIiROkUlCYDNywtaVjzV3nEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XW-IN-0nzEWJAi45L-o6OWDN7FDbonBNPsfO3v-Is998ch4MA5hKY-1TzKqO41kyYGULodWo7wPuLL_QzpcNfTSVzn66PLKKZoP1BAJTNLgppaTW_7xksVKpQvnw07wkCBAlXD31-YygqYhS9j_3uSdJqi7j-2IH9Oe_MMds1fltPcjipzmkEflwB7-GgpzCo3lfLTFiVPWabFfJ5OvPCH2Unz4ywZ18JcFLKCWL4ikXbZ8V7xN11r0VyDvKlmPS_t9JVapWGHnUhp9Rf66JIszaXuLjy-8G0jU1tiHzb-cK6pvSPsJ2zXfM1pECr_dQJdrh3GykEiXjA8B4AqtTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dlBDT_SCWaMtZ6uHQkc8O1s2KpmKxfe-nAsWLavwsZPrLvo8kcuvgeK13D0ykDanGPbp7aka0_nNoWR3Yd5n1Vl8CWHr15mOieCKeU7dXrgYIMbAnhq3I8hIy1h8Y4qFmxniaM43ZiVu0FRb04BXHAnGPnfwZ7phak8QtLzwdEOLnHfpejPRJ_QbA1DUG3sJ1F3o1jBw37-7tSc8LAbZiAUP4EqxS0sXs_G8dPQMaSUNbXgTqc0TNjW5hhD5cTxWaRTW-Of_tVPntMxAb6mtMgvZf1s37ZsTWjEUfJdswW7M9h0B6WN09IJgzokJhulVlkdCYTKhJKNTM3tCuaiIMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2Hi5uOHTEZUYsV9H_MlD_Zknqh6JSdR2LhW0as87Nxs2mTzDbQWgsqzecAtnU08PC9JnZwSHHBmsYgwnlZ5VMwpRvTSrBEXF71UEInh8UBEHrkDAzMgN3BKVqtsGLFl6B1OPKUVUbxQCwItTtiGmS2sOfYgnZXtHNGyE9G-6MKPtD509nN7rr0HFBcHdfpBR56Ko7dO3pLI250hhTPdqg1u7etDarIokxDed2388Kl4b6hP-6X0vPSIvqwkLaNZAet7kmZjG0dDkG5v7G0g_R0yLTsLC94yOZdredW6hTu1Y-h7PCQX_DzPuyJpYsFkopFjwuS1CDcQvBo3joX_kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با دیدن این الگوها شاید دیگر سراغ خرید پیراهن ساحلی نروید
🤩
🔹
یک نکته مهم؛ اعداد الگوها برای همه یکسان نیست و باید متناسب با اندازه‌های شخصی تنظیم شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/665550" target="_blank">📅 10:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665548">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
زمان ورود اتباع افغانستانی به کشور برای شرکت در مراسم تشییع رهبر شهید
فرماندار تایباد:
🔹
طبق برنامه، ۲۴ ساعت قبل از مراسم تشییع، ورود اتباع از مرز دوغارون آغاز خواهد شد. تا این لحظه اتباع وارد کشور نشده‌اند. تاکنون برای ۲۵۰۰ نفر روادید صادر شده است
🔹
زائران افغانستانی پس از ورود، در مراسم تشییع رهبر شهید شرکت خواهند کرد و در نهایت توسط همان شرکت مسافربری به مرز دوغارون بازگشته و پس از دریافت پاسپورت‌های خود از مرز خارج خواهند شد.
#بدرقه_یار
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/665548" target="_blank">📅 10:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665547">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
بانک ملی: صدور کارت برای برخی حساب‌ها و انتقال وجه از حساب‌های فاقد کارت فعال شد
بانک ملی:
🔹
در ادامه روند پایدارسازی سامانه‌های بانکی خدماتی از جمله واریز حقوق کارکنان شرکت‌ها و سازمان‌ها، صدور کارت برای برخی حساب‌ها و انتقال وجه از حساب‌های فاقد کارت به فهرست خدمات فعال اضافه شده است.
🔹
خدمات بانکی در حوزه‌های پرداخت، انتقال وجه، خدمات شعب و بانکداری غیرحضوری به ‌صورت مرحله‌ای دوباره فعال شده و یا در حال بازگشت است و روند فعال‌سازی سایر خدمات نیز ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/665547" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665546">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhsjSHPOVqWs1ijX4VOGJPdpj64021b9zkRNBw4K1hMfMsOgO0sO44pqHKBwHaR2KMrfohD30SanrEFpIPt-mW6ijfrvp9mvkpfNPer6mWoSEArMQSe1lxJDpP3-lsn3PBZmKqZ8qhUJKmuJLwQ8onFr4eKRUCyg3DyGNm8MibsJLZjxOg6PdmLkW3_wE96fT1iPFa9DzugCp2QRf_N2T5tId4Zp5sjh_TMPgbl-UMM2Y-J6yz7PHTPUPsfmzF68ItWatDuz4B_jLCgjtHtshtzx-Hck-x1W_d61d4q3bZIsvY98M1-xCeC8kS4_-2kkkCMIXywqkEla70WiWrVUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرمول طلایی افزایش بازدید در اینستاگرام؛
زمان درست انتشار + محتوای حرفه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/665546" target="_blank">📅 10:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665545">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8eda3dad1.mp4?token=CbpH5TwxI9H6fWctsV-f1zDjfEwtwd9kySCrnQ07GxD_M79dPW8_xU5z8vrDbSQ1MzIHuxKNFCiha8S1ZE2ujzs-sQfozsyvXvdQYJfgCRpq1aTKTGJf3uV1fvTovT2MAtbssut_x9LmBMn38RInPE-H2cUGG4kd0kOitF5VD2eLL7nL3FtCKKOjHUeI3Dvx_-5AEWGbS4co4NQC6C4d3V4Z74kkGxLKXj5l5VQRtfETUWSkYvr0_2hrGdv34jOG_bBWJ_hdsN74y1qXeoECXQcGblcF2GwmSRok_nuRGY_eXbHWOXqKYjfBgK_t7b8gPScN-YbvfyKhFgMDQmE7lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8eda3dad1.mp4?token=CbpH5TwxI9H6fWctsV-f1zDjfEwtwd9kySCrnQ07GxD_M79dPW8_xU5z8vrDbSQ1MzIHuxKNFCiha8S1ZE2ujzs-sQfozsyvXvdQYJfgCRpq1aTKTGJf3uV1fvTovT2MAtbssut_x9LmBMn38RInPE-H2cUGG4kd0kOitF5VD2eLL7nL3FtCKKOjHUeI3Dvx_-5AEWGbS4co4NQC6C4d3V4Z74kkGxLKXj5l5VQRtfETUWSkYvr0_2hrGdv34jOG_bBWJ_hdsN74y1qXeoECXQcGblcF2GwmSRok_nuRGY_eXbHWOXqKYjfBgK_t7b8gPScN-YbvfyKhFgMDQmE7lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات بی‌اساس پمپئو، وزیر خارجه پیشین آمریکا؛ نباید به پایبندی ایران به تفاهم‌نامه امیدوار بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/665545" target="_blank">📅 10:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce95593786.mp4?token=GnoaaBbm7s7wIKBh6F89qjMlc3HRrZkU1Smyd0PCK2na-P3Bcqgk1cC63udPIQ2uUXP2k2XIInit4UgcLf0I_Hw_IpLpANoJZP5Xgb8SBCYWHDvs8PftU924xBAJS9hvD-SzLB5Zuzawp4PquWAojw6lnlgiWj3gQCDEe6yrRkTwsoCtsGQYqDRBbepD_Zr0I_-0ZqQ1t_iGslhnINV8e6WV1zhYSrxDqAvpoIpnSmIvefCWEUiMsYDlGt-79bASLvFjsBG9vvXwruF8nAbWBLha5N07y4kKEnQUado5kaTkLD1p1GfOT3625VN1j3k_jku_p3-lbf9_DJeyT5Ci4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce95593786.mp4?token=GnoaaBbm7s7wIKBh6F89qjMlc3HRrZkU1Smyd0PCK2na-P3Bcqgk1cC63udPIQ2uUXP2k2XIInit4UgcLf0I_Hw_IpLpANoJZP5Xgb8SBCYWHDvs8PftU924xBAJS9hvD-SzLB5Zuzawp4PquWAojw6lnlgiWj3gQCDEe6yrRkTwsoCtsGQYqDRBbepD_Zr0I_-0ZqQ1t_iGslhnINV8e6WV1zhYSrxDqAvpoIpnSmIvefCWEUiMsYDlGt-79bASLvFjsBG9vvXwruF8nAbWBLha5N07y4kKEnQUado5kaTkLD1p1GfOT3625VN1j3k_jku_p3-lbf9_DJeyT5Ci4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ۸ نشونه، چک کن ببین مغزت خسته‌ است یا نه #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/665543" target="_blank">📅 10:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665542">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8982ab33c.mp4?token=k-QGiS09TKc1b2ygJAG7xwITHNcnWDkbDU7Bi2oWrNNwak8JZ9D0U4W6JChsP4mvGHggUFQX2Ot8PtRIg7uYkSujLvBp0_CIXL5o68aLk7vRxfM2dwhRBYH5PYrAv4fZxpIuaINP375w3okwsc9b0fDCPGehRjahgTiaddZ8xIUDRmZq-KJ5SgdCOWvT16-MDZ31wZBZffFnRUKDXRhZ26iekle65PSbc-5-pNtG5XquO_La11M237SakgLVsAGRVcIZKXDPvcKLqFMV70OAuipdVVI-m0njDstvz_t7qcv_HZqsfjDz0NSKSLS_QVSy9l3p62nZi_X-kOl7Mq-0ymKmxxNz_IhOiuiPWTU9THwL4lvkZAA82hRyVS9EUhUIRx-5BgDT__o2QPx3sPym5Vp6Aq1eBCPwa7-_G9lUMjtv858yrTTESQBl0sN55jWNn3Ao-2677eO4kBEeEEWz9Gac7g2-qd2E3l5MUHio620EVJrsQqE-l25_xZ3JOXAwgBFiAa_JDazhbtLphEz4ED9pPQ7LmHH-dgK8aoeTQuzLAxRwGFDa919FGFZ-shRCWGgScApqRXG7ZDT6vwXvmd2pn7P_SAX9rXApljUvvmHHbJCaLtJxyoso_mCFyphlN8th3GLDblUOSQJCO5nYgH9jGRqMuu6DbpU3GpULmyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8982ab33c.mp4?token=k-QGiS09TKc1b2ygJAG7xwITHNcnWDkbDU7Bi2oWrNNwak8JZ9D0U4W6JChsP4mvGHggUFQX2Ot8PtRIg7uYkSujLvBp0_CIXL5o68aLk7vRxfM2dwhRBYH5PYrAv4fZxpIuaINP375w3okwsc9b0fDCPGehRjahgTiaddZ8xIUDRmZq-KJ5SgdCOWvT16-MDZ31wZBZffFnRUKDXRhZ26iekle65PSbc-5-pNtG5XquO_La11M237SakgLVsAGRVcIZKXDPvcKLqFMV70OAuipdVVI-m0njDstvz_t7qcv_HZqsfjDz0NSKSLS_QVSy9l3p62nZi_X-kOl7Mq-0ymKmxxNz_IhOiuiPWTU9THwL4lvkZAA82hRyVS9EUhUIRx-5BgDT__o2QPx3sPym5Vp6Aq1eBCPwa7-_G9lUMjtv858yrTTESQBl0sN55jWNn3Ao-2677eO4kBEeEEWz9Gac7g2-qd2E3l5MUHio620EVJrsQqE-l25_xZ3JOXAwgBFiAa_JDazhbtLphEz4ED9pPQ7LmHH-dgK8aoeTQuzLAxRwGFDa919FGFZ-shRCWGgScApqRXG7ZDT6vwXvmd2pn7P_SAX9rXApljUvvmHHbJCaLtJxyoso_mCFyphlN8th3GLDblUOSQJCO5nYgH9jGRqMuu6DbpU3GpULmyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقش ایتالیا در جنگ آمریکا علیه ایران جنجال به پا کرد
🔹
مخالفان دولت ایتالیا می‌گویند اختلاف اخیر میان ترامپ و ملونی تنها یک نمایش بوده و نخست‌وزیر ایتالیا در تمام مدت از عملیات آمریکا علیه ایران حمایت می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/665542" target="_blank">📅 09:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190a5dd598.mp4?token=dspIKAKV78zZi3xGupWf1ZrYTa4EmhcjnV0eWWPsnA3bjcWCKi9tcWC9IzLVFA55V5MN9xSpIvkYuAL9uG-oSOJiGI7pL3zHImi_IntVVdJ94LN0zZBNJQLE8lpdatcTZga7LWK0dMu8z5anXOQ3YtvZ41lSTXsxjYg3BY-2tka8a2BAozsBQ23chrpNY8W-I1giM_Rh9Se0upsoFQXxsQiy6bh391Vp4zp9L0p4tlyJdEWSsSnFcbY1DBPLqZFXbYVSANUOOLyIoXHtjxeCOPQ5MRJxxjvpMGljJHCKBeMGzgN6FBT7QDdnOQN9ylMpmUY2WcnBFlcV7oNz6lwQ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190a5dd598.mp4?token=dspIKAKV78zZi3xGupWf1ZrYTa4EmhcjnV0eWWPsnA3bjcWCKi9tcWC9IzLVFA55V5MN9xSpIvkYuAL9uG-oSOJiGI7pL3zHImi_IntVVdJ94LN0zZBNJQLE8lpdatcTZga7LWK0dMu8z5anXOQ3YtvZ41lSTXsxjYg3BY-2tka8a2BAozsBQ23chrpNY8W-I1giM_Rh9Se0upsoFQXxsQiy6bh391Vp4zp9L0p4tlyJdEWSsSnFcbY1DBPLqZFXbYVSANUOOLyIoXHtjxeCOPQ5MRJxxjvpMGljJHCKBeMGzgN6FBT7QDdnOQN9ylMpmUY2WcnBFlcV7oNz6lwQ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت آلودگی هوای شهر کرمان| پنجشنبه ۱۱ تیرماه
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/665541" target="_blank">📅 09:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665538">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgMB-uT4WkfhXcvzqHvJQs7G1RKm84mYKN7zvPf_D8J3AXeFJ-r1P3v2DzaDd-F9NZjnHajClwbz3RIe6PjOB-701a40eRBvB5ywp-g4xLsSEd9oc55potro3iwJtqUlVE7974VyxBzmJ-OLK5JiPhdetCbB6Z8y3L1nL6B0trwmJbt1FI5sTGE2hS_5KQ6rC-P83CT63ZH7XdmlRQ9b-h3c75t64aYNiLUnq2DDb_ewkCGmBwBak5Kgc0C_oSy2hfx4-kiE6SVeJEG53bz9oPXKaDe1OR4vJ_KC9bbY4QPyvnAv9YepvVMbqB-PwJuqoMsAhj9OkOlNEvvka9lJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a702236dce.mp4?token=m9Kpftq8x9xUx-qNDhr-XDuvn54ux4653M377ovOnH-CaTSAN5kRyAN97WZqmWo5N-_0XoY9uoNE_46lEjFA8sluNrkx-SD4d_JJNZNAkrDDJlpiLHjdjhLM0UdMxi4tJATsyymXum0_Bd8HjyPsQFD0aa43Ex-jr-ugcNLIVBfDlT-hsDbJb7s_Exp79RYZt-swU_gvS_KYnMc0fUmBC9L_HbgDpljhhBYwIawbtV7CXtdLafWMHb5G2BhHsfx6WrWJG29lFXoZC1S_YMa_K3M7jfG7tpe3xEUxldvQ4riTq3FTuYmIT4lcncsSQReuc-2k8CCWwp6UtiL86pQ4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a702236dce.mp4?token=m9Kpftq8x9xUx-qNDhr-XDuvn54ux4653M377ovOnH-CaTSAN5kRyAN97WZqmWo5N-_0XoY9uoNE_46lEjFA8sluNrkx-SD4d_JJNZNAkrDDJlpiLHjdjhLM0UdMxi4tJATsyymXum0_Bd8HjyPsQFD0aa43Ex-jr-ugcNLIVBfDlT-hsDbJb7s_Exp79RYZt-swU_gvS_KYnMc0fUmBC9L_HbgDpljhhBYwIawbtV7CXtdLafWMHb5G2BhHsfx6WrWJG29lFXoZC1S_YMa_K3M7jfG7tpe3xEUxldvQ4riTq3FTuYmIT4lcncsSQReuc-2k8CCWwp6UtiL86pQ4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادی متفاوت بازیکنان مکزیکی‌ با ماسک هالند
🔹
بازیکنان مکزیک پس از صعود به مرحله یک‌هشتم نهایی، با ماسک ارلینگ هالند شادی کردند؛ هالند هم با انتشار ویدیوی این لحظات در استوری، به آن واکنش نشان داد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/665538" target="_blank">📅 09:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665536">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb365f2ee.mp4?token=YL2X-Qo7gdyDaVMIiQhV1i0T9eC_bg7msxlb-GRyZdXPpVP1JZTN4lzmOE6kkk9SvSUtOPh4sTZYuw-kwlwIpbCdyjOVCxbJsKVAYw7uK-44IKhF_h_rvp-17JrLlkcsMpkt2Q5dRGzQExgsX0IJo-nBxXHBnsE_S3MrsGk3Ue7KU1If4K5HuXKamjeok4Mq71vSR-S-yeEtNanVzqzOBRW4FiRgMozlweyvGey6X5Dx7kLhwYCkd4nuiwRiesuLY65zhI_dUvz1Lf5VKQfe7X947Dmfy9L84vt-AHVaVxFmKvu83r_mvGTzq4OpSslilAiv3k2Ccx6Tbs4ogWHldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb365f2ee.mp4?token=YL2X-Qo7gdyDaVMIiQhV1i0T9eC_bg7msxlb-GRyZdXPpVP1JZTN4lzmOE6kkk9SvSUtOPh4sTZYuw-kwlwIpbCdyjOVCxbJsKVAYw7uK-44IKhF_h_rvp-17JrLlkcsMpkt2Q5dRGzQExgsX0IJo-nBxXHBnsE_S3MrsGk3Ue7KU1If4K5HuXKamjeok4Mq71vSR-S-yeEtNanVzqzOBRW4FiRgMozlweyvGey6X5Dx7kLhwYCkd4nuiwRiesuLY65zhI_dUvz1Lf5VKQfe7X947Dmfy9L84vt-AHVaVxFmKvu83r_mvGTzq4OpSslilAiv3k2Ccx6Tbs4ogWHldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسربچه شجاع بلوچ بعد از گذشت ۵ روز در دل جنگل سالم پیدا شد
🔹
محمدصدرا، کودک سه‌ ساله‌ای که پنج روز در منطقه چشمه‌گل رامیان مفقود شده بود، با تلاش نیروهای امدادی و انتظامی پیدا شد و برای بررسی وضعیت جسمانی به بیمارستان منتقل شد.
#اخبارفوری_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/665536" target="_blank">📅 09:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665535">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06be39591f.mp4?token=GxABFI5NDqgbRL9QBr5y8tdc3X0U1FES0UdiQ90pFLaDhy08t2lDHpgkY1aLl_4l4z43UIMiJFHxbXO8ZM-2-aHqvrnaFVYcR1dnTqELT34otT25XUpb5zdpjcoid4OSPVnZ5QovnSvaqipzIiEuTwMay0lg9d1TvxlPzXtzXnYH8FEelJ28_iK4OCtJovE8n4lhHKnAXLjTaT9U-MHBePqmm39SXP0RKvvSCuJGqtfcE30CWebdazc8whLBTuDq6T2txytFIA5z9coLw9lQLkrr0rk0qZaoQBGKZ-cCBoLE4CKyFigvQafHxYjgXgX60WEjo56I6bgnUvKTXmMpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06be39591f.mp4?token=GxABFI5NDqgbRL9QBr5y8tdc3X0U1FES0UdiQ90pFLaDhy08t2lDHpgkY1aLl_4l4z43UIMiJFHxbXO8ZM-2-aHqvrnaFVYcR1dnTqELT34otT25XUpb5zdpjcoid4OSPVnZ5QovnSvaqipzIiEuTwMay0lg9d1TvxlPzXtzXnYH8FEelJ28_iK4OCtJovE8n4lhHKnAXLjTaT9U-MHBePqmm39SXP0RKvvSCuJGqtfcE30CWebdazc8whLBTuDq6T2txytFIA5z9coLw9lQLkrr0rk0qZaoQBGKZ-cCBoLE4CKyFigvQafHxYjgXgX60WEjo56I6bgnUvKTXmMpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
♦️
مسیر نهایی تشییع و بدرقۀ رهبر شهید در مشهد اعلام شد  دبیر ستاد آیین تشییع رهبر شهید انقلاب:
🔹
طبق آخرین برنامه‌ریزی‌ها، آغاز مراسم در مشهد از میدان فرودگاه بوده و تمامی خیابان‌های اصلی شهر، محل وداع با پیکرهای پاک و مطهر خواهد بود.  #اخبار_مشهد در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/665535" target="_blank">📅 09:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665534">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18700f826.mp4?token=falxWTLklaikYNesSNJDpiR279jXaSF5TVeD1Sa-vMRhZwpzbQ1Etyet8HRlRTYSZgI_kIZD1nEI_7KNqe-5Qnit-zSJijjIg8ZaHG9YI0PXtwCP6emYGQKoff56WNcV8hBZEIJbD58jzPOY5MR2qENiUHlJiPOr0z5k8Cg8UsJSdccdytP0CgOEjb7OkbtiYwr53m3WYPcmmIv77UcwJ7KQRkXCIZVfHbMr3F85b0iETe7eUQj0q971ysJus91bRO0v8NNKfNRKTm-LjMN6PugOxZApL1m8t_6Zb8Df1YJQZa2dAFVG7Rf9K-WoxjdH9mY5Mw_fk6m27q-3DC1Amg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18700f826.mp4?token=falxWTLklaikYNesSNJDpiR279jXaSF5TVeD1Sa-vMRhZwpzbQ1Etyet8HRlRTYSZgI_kIZD1nEI_7KNqe-5Qnit-zSJijjIg8ZaHG9YI0PXtwCP6emYGQKoff56WNcV8hBZEIJbD58jzPOY5MR2qENiUHlJiPOr0z5k8Cg8UsJSdccdytP0CgOEjb7OkbtiYwr53m3WYPcmmIv77UcwJ7KQRkXCIZVfHbMr3F85b0iETe7eUQj0q971ysJus91bRO0v8NNKfNRKTm-LjMN6PugOxZApL1m8t_6Zb8Df1YJQZa2dAFVG7Rf9K-WoxjdH9mY5Mw_fk6m27q-3DC1Amg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این دو قرص می‌توانند در لحظات اولیه سکته حیاتی باشند
🔹
در صورت مشاهده علائم سکته، قبل از مصرف هر دارویی با اورژانس تماس بگیرید و از مصرف خودسرانه دارو خودداری کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/665534" target="_blank">📅 09:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO4-4uAMhl7RxNKO0TSSAdLhz2gWJusqRxulTkdD-2sNmynw3a-WUiacyL-ciihTZFUs13Di0oQepoE-ayukFhVogulpdTde9dKxgdJPjYf7LJCUa5D34-0s9IrUNh2MqjXVR6xRgdbVdGTCMMUQ6TCVvLqF6ESOJ8MAwdHOB3CRxJ_-wrg8wE1_rNGjHsZrewRgXbNUFZIYT5dNfq9ZPf2LP84n995hpzeVxvLFLls82XfqkkDUuDMwktdgzIOlJ98O6ngo-jB-B0_I8t9hv_UXFH1DPv-3ZaVvNPzPfT3FfgDbGsZOxmcELgi2jHyPCZbIug2-V7-GJ-NtpMhVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای عجیب ماچادو: من رئیس‌جمهور ونزوئلا خواهم شد!  رهبر اپوزیسیون ونزوئلا:
🔹
من زمانی که زمانش فرا برسد، رئیس‌جمهور خواهم شد، اما نکته مهم این است که این موضوع باید در انتخابات و توسط مردم ونزوئلا تصمیم‌گیری شود.
🔹
در آخرین انتخابات، اجازه ندادند که من نامزد…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/665533" target="_blank">📅 09:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665531">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319b62d958.mp4?token=eadBCJu4mJN74XccL8Bl3sWW9-nwarbzyjaxpfqZpjDvLRUmHysciL0atsQc7QZ0Y27iPBGej0aMhQJcmOakh3U68QH7CZhg-KjMQqKR8pLqBjEf0LEK1Yxl8Aek7uNTkhWo12xHLZcuMN3b3jKpfEIO7fqUV_Btw5djB8WBsrdk26VuJV2lihcaxIB6k--LxsBqG16J3dKUgF7oKtWp3EpXchQ3_cwDDoTTJXHJFOVtKgzLC-vS3HwdSk8NKLX6az_ziJMjFEzoXmQliH9uw0gQRe84escmwBxTiyqu1nnq4suBfZ5TH8H3fapW4wtewNAWr0Q86vFso1K_iLcB7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319b62d958.mp4?token=eadBCJu4mJN74XccL8Bl3sWW9-nwarbzyjaxpfqZpjDvLRUmHysciL0atsQc7QZ0Y27iPBGej0aMhQJcmOakh3U68QH7CZhg-KjMQqKR8pLqBjEf0LEK1Yxl8Aek7uNTkhWo12xHLZcuMN3b3jKpfEIO7fqUV_Btw5djB8WBsrdk26VuJV2lihcaxIB6k--LxsBqG16J3dKUgF7oKtWp3EpXchQ3_cwDDoTTJXHJFOVtKgzLC-vS3HwdSk8NKLX6az_ziJMjFEzoXmQliH9uw0gQRe84escmwBxTiyqu1nnq4suBfZ5TH8H3fapW4wtewNAWr0Q86vFso1K_iLcB7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش به اظهارات پزشکیان درباره اختصاص ۲۰ میلیون بشکه نفت به هوافضای سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/665531" target="_blank">📅 09:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665530">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62fbc3509c.mp4?token=lIGAjO3jukV1-rm6ZJeqZUBtkfpavujUHPBOFTox0K5SnS5JbmYQMFmzo16qfxHoBCcbYGis8VlRagdGJNRleTnbZ06DXqF08WophKe8x3Jyn5TMtX0ka4ygms9Z_do7aPoim-R18MO4H_i8s_4VdrQL-eJVIohyBSTRQBx9Aw19ebwCIa1k6hpR7DEpZYRBC8hg91xAcUxNyADp8d60DfgJ0LBsJIAUzp5mt3-JGyVHJqAiTy3ReWlWId3CxAVlz6xuX_DViVq2W-xy4zaX25glGgJ-SCvGPMakKnszQsoRPhJWwmW3F3LBDrlKW8Wwewe1Rm1eDwW_BkvL6RHyWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62fbc3509c.mp4?token=lIGAjO3jukV1-rm6ZJeqZUBtkfpavujUHPBOFTox0K5SnS5JbmYQMFmzo16qfxHoBCcbYGis8VlRagdGJNRleTnbZ06DXqF08WophKe8x3Jyn5TMtX0ka4ygms9Z_do7aPoim-R18MO4H_i8s_4VdrQL-eJVIohyBSTRQBx9Aw19ebwCIa1k6hpR7DEpZYRBC8hg91xAcUxNyADp8d60DfgJ0LBsJIAUzp5mt3-JGyVHJqAiTy3ReWlWId3CxAVlz6xuX_DViVq2W-xy4zaX25glGgJ-SCvGPMakKnszQsoRPhJWwmW3F3LBDrlKW8Wwewe1Rm1eDwW_BkvL6RHyWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترند جدید درمان افسردگی در تهران؛ بغل کردن درخت با هزینه میلیونی
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/665530" target="_blank">📅 08:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665529">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6_lNuORZmFvIKzzaeDcnVMRayI1Q6vq7yRMBjhLAdXX5HwkReZAzdf8DQibVSVrllEBCH9HEEdb3xsg-tGvZ2fNy9cg79lxdxZvnI8kykjFUzjRdD6H41z7Y5r3DmIvDtoygqPN2XZRbSVe9uh7DVCyxvvIjFRXv88idqax-eZcC_hV3nVFbTYiQOXBmrMNWE3bXTIieAgporyW7laNlaDw4_k1oJUMsEisuLH6k0bVol-BIE3lsqQ41C7I4m7MOLBSLIIgDHCY6GspVeH7hwBbhqKZyCPeOgSfQnVKNVlM4StTX4MZ3H6AVja2t-cdR3lEwYvOVAPFapbnQhKWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی پیاپی قربانی می‌گیرد؛ ۷ سرمربی تا این لحظه برکنار شدند
🇪🇨
اکوادور - سباستین بکاسسه
🇺🇾
اروگوئه - مارچلو بیلسا
🇳🇱
هلند - رونالد کومان
🇨🇿
چک - میروسلاو کوبک
🇰🇷
کره جنوبی - میونگ-بو هانگ
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند - استیو کلارک
🇹🇳
تونس - صبری لموشی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/665529" target="_blank">📅 08:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665528">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fe1b73c3.mp4?token=uP-Bq3okO1uaNhjqpOseXSvLhamY6BAb_QmHp-PjiCwp96iGzTAbzhqOtLeoYpuUHjvREg44CwepRYh4aCJY4sIUlnidWKwi3SSGMvW4xxvLy2aVu-STy5ajcoxf2AfDKVufHfL2O4Z6igCvuZvl7Pfi7gXiTWJVZj1jTL8Q1bXUcIAMTgBEO7mgG1llfjw0a0aEQZRPTD2zpwzvocavas_ENrR7hPtkH6fNCsU1wyiqPQNzLSTYptyBztLcGiI7htRgKg1SYzWS9Ycgoieob2Ks8WlW8onVRD6-hu_ebFe75SFfvdDw_oVLDTmsuW-r8bpmy_W6oTlRJHR2Z9fv7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fe1b73c3.mp4?token=uP-Bq3okO1uaNhjqpOseXSvLhamY6BAb_QmHp-PjiCwp96iGzTAbzhqOtLeoYpuUHjvREg44CwepRYh4aCJY4sIUlnidWKwi3SSGMvW4xxvLy2aVu-STy5ajcoxf2AfDKVufHfL2O4Z6igCvuZvl7Pfi7gXiTWJVZj1jTL8Q1bXUcIAMTgBEO7mgG1llfjw0a0aEQZRPTD2zpwzvocavas_ENrR7hPtkH6fNCsU1wyiqPQNzLSTYptyBztLcGiI7htRgKg1SYzWS9Ycgoieob2Ks8WlW8onVRD6-hu_ebFe75SFfvdDw_oVLDTmsuW-r8bpmy_W6oTlRJHR2Z9fv7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین موزه آجری جهان در خراسان کهن
🔹
کاروانسرای رباط شرف؛ شاهکاری از معماری ایرانی در دل جاده ابریشم
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/665528" target="_blank">📅 08:50 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
