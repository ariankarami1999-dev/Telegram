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
<img src="https://cdn4.telesco.pe/file/Z29MtDzD8kuVCuJ3wbN2RoolRIKGskGCZj8Ozjv9soqkW7eQTKkPEtj3G4r5i_rhUMHNL0Quz-gB5vRP2CG3eHoLIaLgFeLAMOisJzoucDBA2Y_KQKr9vaKKYF4IrXWN9HIEn3EVBhhbKh9QJ5DzhG2fr40VNv3ghKi020_B_2Ysl0SX11ngWVn0_j8dEejfC9u5PeHj_Q2GPXx36J3nY8W5An0KLRUtuTgdtPBh4Z1i4Rs76B0uI0JpSfbKpdgQ-jB2HfX7c4iQruq03uMe3fujVmsBb8R6BOoDZnB-BY7iMyNfPXp_gEPOw58hsB-MyQKCBpRAHqTzmOBqpBQR_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 214K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 15:33:43</div>
<hr>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=pIv9bjCEaqNjU2Bv6mAd9tiWNGfh2XbasiwmrfBWBT0og7PkLLLfYy2Exq7I9DOGQFBbSFpX-GFkMArsfad-EA0tKVHAJw1-R5t-4yDeQGICHQH0yaQvihRbIPiwTcvqFxZxLfKJ8A6EDPaOixzuSVa_LB8n8JuTqpRowx0xxRYXz3nWnxms882Ms_625QfNYLuerOeyLzO37orpCwjof6UZZJCI_Yw7bc0Dto9wDx8o59IQIOSsdfP6GiJX9c3_SCyaL0MB_uCdd2kn07Slqim8uNJJY7AUvX1eq8JeKz2UTqvOYnXNTtf1XmRwetkozjX4vUA-iiZgiV1EcMQI7Ba0ePa7KuJwXpwqpjjtNEDt2zkzAeNwkEA62GYpR2PmZsI8Yq4lYgIGBH-OAPFJI9PESkt4PqBzPWLsTiAKR1Ob7M2FOq9TKMMFkJr-tO3tX7j3AIND_svuIF_ay7RwAkpFUu6LyvRu687qwyH3yf0DTGbfda1kY0E3OCZyQjbjKzneWIJZdLulNvTxBFEdlLmu2UUaOBr0MFIglaT4bBViboUiZrb2Nm4EvviPuOR2i3T45eNd83BjaVIHavcAz3bnvrYEDKeovw8X7E_TJzF-uklbtTNf06w7xxZ-RDQUYzag50qGGVdjY1kVvZ1v3bksBR7HIBTMvCfHB1ELcRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=pIv9bjCEaqNjU2Bv6mAd9tiWNGfh2XbasiwmrfBWBT0og7PkLLLfYy2Exq7I9DOGQFBbSFpX-GFkMArsfad-EA0tKVHAJw1-R5t-4yDeQGICHQH0yaQvihRbIPiwTcvqFxZxLfKJ8A6EDPaOixzuSVa_LB8n8JuTqpRowx0xxRYXz3nWnxms882Ms_625QfNYLuerOeyLzO37orpCwjof6UZZJCI_Yw7bc0Dto9wDx8o59IQIOSsdfP6GiJX9c3_SCyaL0MB_uCdd2kn07Slqim8uNJJY7AUvX1eq8JeKz2UTqvOYnXNTtf1XmRwetkozjX4vUA-iiZgiV1EcMQI7Ba0ePa7KuJwXpwqpjjtNEDt2zkzAeNwkEA62GYpR2PmZsI8Yq4lYgIGBH-OAPFJI9PESkt4PqBzPWLsTiAKR1Ob7M2FOq9TKMMFkJr-tO3tX7j3AIND_svuIF_ay7RwAkpFUu6LyvRu687qwyH3yf0DTGbfda1kY0E3OCZyQjbjKzneWIJZdLulNvTxBFEdlLmu2UUaOBr0MFIglaT4bBViboUiZrb2Nm4EvviPuOR2i3T45eNd83BjaVIHavcAz3bnvrYEDKeovw8X7E_TJzF-uklbtTNf06w7xxZ-RDQUYzag50qGGVdjY1kVvZ1v3bksBR7HIBTMvCfHB1ELcRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 520 · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s37eul_rWWdfDrZVmqFUsAh1dKNq9i0Uc_p1JU6Lk7eeTu9gZYoNLvX1AueoUDmEjfJpnWaycW9F29th1WUNxfEKeoBDFwpv6nqEfOv1K8XF8vHVNCJjl-oo0gC_Lk18b5K1rq02xPVL38jywoKLDmdIUfMwzxrycGpIPvumW-s3OjpIc4c5vyYv2-NzfazEh3tzcKPXuIsCjOiRiiqJG-s7guVS75UNAVpQM7MEnBGe-dFwLiS16hSR7JlyIXcU5GlAe9KJ8bKeDvTaaUIFF6eYRJRL419GjaWzdviQ8R6iq-E5I3BDGMVPy9PjJRemIYuifUAkXwGwc7D9IGGLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH5MCve6-VJD_NCcpwXir5hyjGZCFnRqq1l2ORZM0pnyiFrZgg-DMW8V9gRPbWQTtbsu-WBD9zFsMd2RndOnd31yse-hyQczrEHDrb-rodx1_kV-1ztOT2dl_tftsT-Lxl0PA0Ht95sJQFv2we-NmP3nUFpS8Yc-1ScD40A-R9C3imAgdTyjPiIWSNmABMU1GGQh-DOxjUTyTHSKf_FNCiLYzsyeZnihTBIyb6WAChMlr9wwazIGziQ6m05UmEH3K3CZ83wCtIEj-z6O1DHNt2Ijy53cngu3zJDni5REY77KX8wGgK44RKTK923xyjebhXxNt300fN55Hpp6I5oD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=MqEyil9GiYDpg-MAX5XVD2mGZFZ2P7LNhMgzk2yySPsnfPBP8uAjZtJrYtgUfUHwwJy8PLSVtGnWawtQ85Gm6aHXqu0kI-P4hTpy5QGjAcLrHjuLbfyonVt9q6iVdaioV9Q-KFog47FojNf4PqauaqILwh-LSrptSS8fb8PQFW0zhnhsrcYVYNJ-84SdXvg_KU5sFAuAw1K8UlQJdXER1XEnOXFyjvDUcXY9cikELBgj66Z9shFdE0pbTDsReNGo1HKaloJSe7y_yohvWWaBCxcPfvetYHfj4ZGrF23RmC-tuY9XhtYFkpOLMz3aXcKLFQrkr5dDmyRAR0dwUyabFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=MqEyil9GiYDpg-MAX5XVD2mGZFZ2P7LNhMgzk2yySPsnfPBP8uAjZtJrYtgUfUHwwJy8PLSVtGnWawtQ85Gm6aHXqu0kI-P4hTpy5QGjAcLrHjuLbfyonVt9q6iVdaioV9Q-KFog47FojNf4PqauaqILwh-LSrptSS8fb8PQFW0zhnhsrcYVYNJ-84SdXvg_KU5sFAuAw1K8UlQJdXER1XEnOXFyjvDUcXY9cikELBgj66Z9shFdE0pbTDsReNGo1HKaloJSe7y_yohvWWaBCxcPfvetYHfj4ZGrF23RmC-tuY9XhtYFkpOLMz3aXcKLFQrkr5dDmyRAR0dwUyabFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=Uo4jEnyRDn7DS2O9V_qwaQTmqmAcaEgUV8oqE_x4BbMkj7LnDRxd58bvQTbytSPuWyG7NoWaMGsVcGPFaglNFFsIm8RZiIfuw55iwNznMHdVIabAcuF89hLwA0ZFHmvsXKcytlW-Ctg3yGsQ3tROioCNc7rK_9I8XIKGArteajz19BRL2kKaEP3s2XC9KUdz0SUK6DHoDtUjEwVBuKTfaZd4MOErKQpPVvhTfZNKkYR4214NE8OMix8Wke46ajHU_DqwAeXENEI8zj-g_3n55M-dfEPwvbvhE6VW4J_-SLlh1AjJko5bQvL-CDl51ED0Wr7cIxUevIKL9LCa9ANnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=Uo4jEnyRDn7DS2O9V_qwaQTmqmAcaEgUV8oqE_x4BbMkj7LnDRxd58bvQTbytSPuWyG7NoWaMGsVcGPFaglNFFsIm8RZiIfuw55iwNznMHdVIabAcuF89hLwA0ZFHmvsXKcytlW-Ctg3yGsQ3tROioCNc7rK_9I8XIKGArteajz19BRL2kKaEP3s2XC9KUdz0SUK6DHoDtUjEwVBuKTfaZd4MOErKQpPVvhTfZNKkYR4214NE8OMix8Wke46ajHU_DqwAeXENEI8zj-g_3n55M-dfEPwvbvhE6VW4J_-SLlh1AjJko5bQvL-CDl51ED0Wr7cIxUevIKL9LCa9ANnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=uWcKFGmZyagnnRpTNBZQ7wqewQoAMv04hba5W_oXjrfS5IR5n3kOQNRti-xFy6zZsvjweKHt2im0cTTUja-7RSJSaGjHP84ppV6LTWwSgwwvG1rsUuBGvXmRAeV6o5bKkO_jdBPImmHfkiDc4DQ8nsr4LGEEImt8gP60PCz2lY2xTtdOGMhKoBXwI56DNNBWKoRr8D0GcsFpeyhxU_CbzTBe7Q1hc2i3gGIa6LhYdeStmKvMgv5BbIHLEHNSXMfpVYIKg47euPYjV8BohSu9N7qSj2kPzgdER0Ts8z8tLTVPgt4qRu-I_ru8_P7gtQ_s2hmNgyd5gNXMvwmqvSUHxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=uWcKFGmZyagnnRpTNBZQ7wqewQoAMv04hba5W_oXjrfS5IR5n3kOQNRti-xFy6zZsvjweKHt2im0cTTUja-7RSJSaGjHP84ppV6LTWwSgwwvG1rsUuBGvXmRAeV6o5bKkO_jdBPImmHfkiDc4DQ8nsr4LGEEImt8gP60PCz2lY2xTtdOGMhKoBXwI56DNNBWKoRr8D0GcsFpeyhxU_CbzTBe7Q1hc2i3gGIa6LhYdeStmKvMgv5BbIHLEHNSXMfpVYIKg47euPYjV8BohSu9N7qSj2kPzgdER0Ts8z8tLTVPgt4qRu-I_ru8_P7gtQ_s2hmNgyd5gNXMvwmqvSUHxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m880LGFQ7ETwVsVWyYdn6CwjoXnzDJYiBh_ZQQpiXTyKdHRy4LcA-IFD8J77EjiouuNXXV4xt1IJDkTWXUAP_7etjxzwrPmpGSFyS8GaqnQh2mWgpTaL-aucmXXHzbE-M1zAIxNjm4fysUYnRX8DYqZELuaa48J1Vv-_BCWuZw5bAYvoqmzLhr_x3kgACTxK_O-5zVud6vrZWNahgJr-EbclUKMJrRcB2FUEcMXvo070WpHZ6awizS7uQlv1UEFNE8iVr_ZtXorvJNf2mMAkL4KCjaHUHx8zQBn6hNruV7vd1_U4ZwOt9ktlBUBq_ky68clWo7jTKCUnhsMRsU7C7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=QbWGQoXxrJH9XmmL5laEhZK3R1BUlo22n3In9H2s0XbEKepGOKH1o7x88H3_vSjezkb7N3LKLSQLN1nU80d9y1zdcm-X-egBnKJvOfyIjWJ-0PyxikGE6mUMyWgIcjKBwwaB0tw5nFOncYrgYN1vm6--CSggGsDMrRAkZ8gVPI8859FUGPb-fS_wSZ33jUOgwIoPxJfFoYm0Xs0oKeiJqOI77k8wRx9e3qhTdM8Urqxy7QIXzGEaNFBeTEIIpB9hstNjfFdPN7rhlhABEfeEkhmGg0htvIfR27lppPyxBvodGybdxZFUdCg2HXXdiWrJUhAq4SBoWCy-sBYpFbfmeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=QbWGQoXxrJH9XmmL5laEhZK3R1BUlo22n3In9H2s0XbEKepGOKH1o7x88H3_vSjezkb7N3LKLSQLN1nU80d9y1zdcm-X-egBnKJvOfyIjWJ-0PyxikGE6mUMyWgIcjKBwwaB0tw5nFOncYrgYN1vm6--CSggGsDMrRAkZ8gVPI8859FUGPb-fS_wSZ33jUOgwIoPxJfFoYm0Xs0oKeiJqOI77k8wRx9e3qhTdM8Urqxy7QIXzGEaNFBeTEIIpB9hstNjfFdPN7rhlhABEfeEkhmGg0htvIfR27lppPyxBvodGybdxZFUdCg2HXXdiWrJUhAq4SBoWCy-sBYpFbfmeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=nbmEACrk60bARkddpqkExgCR29y10IwpdpT9ltq8Wfh_I3rqGtYuh1rOI-B8Mj-KUDrJhp_t92AzZWfCjjPL0xXAdKeCkKk63fkXL-LWC-pfTgBlryg91g8qCvKgK6-3fYo1h6ql-0MYKCxx12dDg-8uy8Lf2c5hL36DWCkttWinCIVvUIWxEe40F6FgneMcNEX_HRAzdh4e1lQBymFPnhRqBEsN2JpENIu0flLQ2IeZRcUtfxU3GTF6OCgvtF58cqW6GOru3kMOdCAoKg8QgfaCtCJHiiujeK1CeNDfTGdrydAvk6S-z73b_peC5s9o36V8turhMPfRTFQwzkxBPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=nbmEACrk60bARkddpqkExgCR29y10IwpdpT9ltq8Wfh_I3rqGtYuh1rOI-B8Mj-KUDrJhp_t92AzZWfCjjPL0xXAdKeCkKk63fkXL-LWC-pfTgBlryg91g8qCvKgK6-3fYo1h6ql-0MYKCxx12dDg-8uy8Lf2c5hL36DWCkttWinCIVvUIWxEe40F6FgneMcNEX_HRAzdh4e1lQBymFPnhRqBEsN2JpENIu0flLQ2IeZRcUtfxU3GTF6OCgvtF58cqW6GOru3kMOdCAoKg8QgfaCtCJHiiujeK1CeNDfTGdrydAvk6S-z73b_peC5s9o36V8turhMPfRTFQwzkxBPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=fdv7NrbZU3GGtLpOqz5jLp3j-73fUaxLdqWSo-oWMAGoSxCNQcR-9r_WtPiwuQrZ238Gz-1sOQVPj78KbrbCnhzwkH600UMxCb_TsKSbAr5gcVz6-qllreCT9oyBrtnXE62SdAtJvQfGJYsuq7gW4Sx305XvncF6mMDb8Nr2PvKGUteMeRG77GIWRzv5CNQ9ByQQjKB8idw2jo7HKSMoGcB-cGVkrIc9xbcVRRqUTxUia7itx5uBDff_Aw1IgPlOi0I9U0ZaLAs8Jb9YDj_9SgawIG8H-jmAYBA1poQALzZFCequ8ot7RVqrO4l0XunHIP6LO8nrkKVGMZaT6KM4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=fdv7NrbZU3GGtLpOqz5jLp3j-73fUaxLdqWSo-oWMAGoSxCNQcR-9r_WtPiwuQrZ238Gz-1sOQVPj78KbrbCnhzwkH600UMxCb_TsKSbAr5gcVz6-qllreCT9oyBrtnXE62SdAtJvQfGJYsuq7gW4Sx305XvncF6mMDb8Nr2PvKGUteMeRG77GIWRzv5CNQ9ByQQjKB8idw2jo7HKSMoGcB-cGVkrIc9xbcVRRqUTxUia7itx5uBDff_Aw1IgPlOi0I9U0ZaLAs8Jb9YDj_9SgawIG8H-jmAYBA1poQALzZFCequ8ot7RVqrO4l0XunHIP6LO8nrkKVGMZaT6KM4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=XZln5zzFH2RkUlm_kzkry2K8zj7xlwqSsPuTtaOOi_i0PcXYoI32pyyH9dNXMWMM7-cJbHsUOCjOiZ7nxV7p5DRqnpWnx0JKAKogJgtWnH-vDV4Ouzsf5X3jIWsomV2eCN3Nm2qHJFKqRF5jwqDa0JCQdN1YuxKr0MlFfS1m1SE3OKrTvHkOJhKlpgyDoJmssOD4PmZj6BOO19sdB5Su2bObLlTNXP3IWobjo8PPTaQ0OXDbjKk-T-8ueSMIoQacUzLubpE0TuOFkcneqV-rQw47XOiTtlZfedC9yPRNic5UbNGLSaFA8r-IPgS_YGC_q2Xi5l-OEzNAf_aUiuqe4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=XZln5zzFH2RkUlm_kzkry2K8zj7xlwqSsPuTtaOOi_i0PcXYoI32pyyH9dNXMWMM7-cJbHsUOCjOiZ7nxV7p5DRqnpWnx0JKAKogJgtWnH-vDV4Ouzsf5X3jIWsomV2eCN3Nm2qHJFKqRF5jwqDa0JCQdN1YuxKr0MlFfS1m1SE3OKrTvHkOJhKlpgyDoJmssOD4PmZj6BOO19sdB5Su2bObLlTNXP3IWobjo8PPTaQ0OXDbjKk-T-8ueSMIoQacUzLubpE0TuOFkcneqV-rQw47XOiTtlZfedC9yPRNic5UbNGLSaFA8r-IPgS_YGC_q2Xi5l-OEzNAf_aUiuqe4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=dbpESipbGQunWxn2s7mYqwL5KxQ-0VdAe-aSMXgvqXbFe0YOxaemL-9JN4UU2hKK0bSvL--4KX5ChgEEpJGsLNwQt0FL8R3YgS9kRkEx22gzxpmdtoou83klx1APdLzT-AIwlNhgzoGFpIKqp7MwWb83-ADpgg8UFURSEYzmwCohe_5Q0LkjZ8aec1YDI_7-ggqqh1iA3qYBItsJGMNOQxsnbU1EFjrRjCnlOdr7a5IVUcjH0tiJpMvh4LEdeMj4ha5ecwmXMvMevLH-PLg5DIgovWTJK6J35T-Wa866ou8cOJP49teXWKBReQccb3zXKQa3VYJU4BYLI54L7nPNTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=dbpESipbGQunWxn2s7mYqwL5KxQ-0VdAe-aSMXgvqXbFe0YOxaemL-9JN4UU2hKK0bSvL--4KX5ChgEEpJGsLNwQt0FL8R3YgS9kRkEx22gzxpmdtoou83klx1APdLzT-AIwlNhgzoGFpIKqp7MwWb83-ADpgg8UFURSEYzmwCohe_5Q0LkjZ8aec1YDI_7-ggqqh1iA3qYBItsJGMNOQxsnbU1EFjrRjCnlOdr7a5IVUcjH0tiJpMvh4LEdeMj4ha5ecwmXMvMevLH-PLg5DIgovWTJK6J35T-Wa866ou8cOJP49teXWKBReQccb3zXKQa3VYJU4BYLI54L7nPNTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fy1a_g45Vf9_wtm16U5e8IeK3483oQQM8OgT7xvO3k_VaJTl0HmPWgzxSURFuGe2wFv_N9t2K6g1lpp0708Pxt4-62p-rv3HRIXH5W7eiJQ_pozgU0NxVsTJPfwT5TzP_SR8xwkSwRI1ZiQK-ebovyOVaCkxlRBxU0REQjtGYmQ9hM6ttSG08Qkx05_giypbZWgHyGVmrZn5X6VtHNtMyeZF-CFwbllUVfKOp80ILofr47GnpOzbPiz4ioRV5RxotFuSXj2A3xf70jy6jdUxEkolmpVymWIZrz-T93Zv0j0l3mdM5csvc7vnwE7NXcoxlBozM73UZWOCtD3KU5VNe4FmGtvSGfz6b1wh7-v9Ho7Z_eOwhz98Cxs9VlaUBFa3rvMkX-7tobDuT7H2OH0jSu7u58CKmOTIwibJ4CqbDLk9ySfdgDReTwvkh6xE3z2CX2BAQSIf5aZOxo0gK1kmwcdRRhv_6EnePJIXVE1DL70vGME6A2gjDonbKOHUnYgFw7TNT1MzbVEQ7vGK9FPctlwYTlawJDj9Q9K2kqEKhDpAdXgDOsG2fqxDDD8NtUgZOI85xqJo_ieUpSNHJNtpOdXZbdT1O0Nfr8psy_k270iyN9KZuXW3kblKwIAqGYKeyE1VqXM173qC2gxUbil4OBTQgcY-xKFNk1AWhHW1TWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fy1a_g45Vf9_wtm16U5e8IeK3483oQQM8OgT7xvO3k_VaJTl0HmPWgzxSURFuGe2wFv_N9t2K6g1lpp0708Pxt4-62p-rv3HRIXH5W7eiJQ_pozgU0NxVsTJPfwT5TzP_SR8xwkSwRI1ZiQK-ebovyOVaCkxlRBxU0REQjtGYmQ9hM6ttSG08Qkx05_giypbZWgHyGVmrZn5X6VtHNtMyeZF-CFwbllUVfKOp80ILofr47GnpOzbPiz4ioRV5RxotFuSXj2A3xf70jy6jdUxEkolmpVymWIZrz-T93Zv0j0l3mdM5csvc7vnwE7NXcoxlBozM73UZWOCtD3KU5VNe4FmGtvSGfz6b1wh7-v9Ho7Z_eOwhz98Cxs9VlaUBFa3rvMkX-7tobDuT7H2OH0jSu7u58CKmOTIwibJ4CqbDLk9ySfdgDReTwvkh6xE3z2CX2BAQSIf5aZOxo0gK1kmwcdRRhv_6EnePJIXVE1DL70vGME6A2gjDonbKOHUnYgFw7TNT1MzbVEQ7vGK9FPctlwYTlawJDj9Q9K2kqEKhDpAdXgDOsG2fqxDDD8NtUgZOI85xqJo_ieUpSNHJNtpOdXZbdT1O0Nfr8psy_k270iyN9KZuXW3kblKwIAqGYKeyE1VqXM173qC2gxUbil4OBTQgcY-xKFNk1AWhHW1TWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmLkMlisL9Lh8vG3w12oCoM1P0OTvaKT7nSzLJQl4FjjA0gxQA0ikvaa8LsKbVPyqjSU0kwdm_TcPzcWkpf7niEtqO7NjjexK8L2p-K67wwP0OL0SXl3dBYpVtY3EID-pjcKofm07ijxV1tBmaLNNA6gEl4GAAbfxZaDo2Nio4GmcjLvV_2sCTkUaImgLp4oWcuy7gdcK2kYD8RDDX5R5vYwZEr5SrkHfbvaeg8nVXVL6t8g58v9x3XZ1v1kL9949HpL5r58Myss1vbORtJOC4vlWaT9JSoshXqT_evy5GAf3FoxVji_4eu3FkqvAfW8rcc-J-Zf5V1HWOrlI0XAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f10MIMpcOz0kGdTQbmkTzry4i1l4gRfUf8gtOELDdqeIdfZF36YTSDY9LZkyLn35Iabmq66whEmSwMgMK55z8aOnCi2dQv1F1bDNxcVTibRMkIfUx8sjfiL9NFJoCRdlMQxRVKzix4Er-OxPUEsf8cifWpb7LZeBUjjdEt8ffUVeSvZ6trFAHCqEjJBAjgNOTksf2AF-nwBmtCHT618CThl2ZQZ3tve8KM9WMd7tovCuJosfd5TOSDWV2LtZIyBOB2nn4bcDa1EsGWb16DTamj7o3ukvz7yGWPTUOM6p3puoPvOU2jeFjwC4N8InoHqKba-MUYFKw0xRiFAbgj0Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OteJF0hYRGEzUIQ9egwX3RlFqS2WK8-hIEknzis_US2kKPDCpMNNGP31P9WgUwAKhdT5oFSlr-Jk_pbP5kHnuPuuYlAtAUDxHJABLeR0nkEem9E3Sf9S5Tn6ImyqnHMJSgoyekC7SVMuV_XCyho9M2vaMjwAmk15ynYVpDUbbsX_yLZ__qRRo2mI3XyJmPjY9xEjtstM1JAO3nkuDLflgafviO2znihGK_KfUU9y7yDlmJpGrCk6zQp-lpYw5eaH95Y8U3ghLZ-LoDjmDoLDNwad43MPE70Mun1QLp7M6K76toYv7CjDF3epUzv0GV0LHIVcBFDU9on2BNXXqLbU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=HK0c4nagj3XPa-KGgzZDpgOmvlkyVl_hVLgrLI7SJKy6UP0R12QRO92HV_Stz-IJxHQuEQGrblFZ1ShjfH37chUhOH3IfUQ3L4NXep__CGENT2hwpV7zyqU6_-VEbMtYBPGmAHlVpCP85swXB-B5dhQuOpxoBITGBS8aYqed_40BbxrpPIHvakkMHidAvcK4iq3lzH7OnDpQ6RRn-6095Yu7N_dMe9MrHxjOEez2zKAA-E-qJMxp0u0GH3bqWOk9X-mhy2c9iqrsxyB6J9Q2s34awFkApKxBK92kxlWmCp6v74gY96rsdJDtn_udBCVwutKLILxIYewsfNOwlNwbNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=HK0c4nagj3XPa-KGgzZDpgOmvlkyVl_hVLgrLI7SJKy6UP0R12QRO92HV_Stz-IJxHQuEQGrblFZ1ShjfH37chUhOH3IfUQ3L4NXep__CGENT2hwpV7zyqU6_-VEbMtYBPGmAHlVpCP85swXB-B5dhQuOpxoBITGBS8aYqed_40BbxrpPIHvakkMHidAvcK4iq3lzH7OnDpQ6RRn-6095Yu7N_dMe9MrHxjOEez2zKAA-E-qJMxp0u0GH3bqWOk9X-mhy2c9iqrsxyB6J9Q2s34awFkApKxBK92kxlWmCp6v74gY96rsdJDtn_udBCVwutKLILxIYewsfNOwlNwbNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=R5x7Kg1hk-VbrCkqTUYO_dIqJbhkXUKoCGQDd1SXOAEP7rfDxSyU9qBD_SK1Ngbb2BDcis7j_cCgQUr8x6KmwARdbfOkjSU_fV7k-xSFZF59F8rUmssACO7TBL6wIR7iEHEpBMA1JZ5ob3nWS2OidR2oRDzq8DiyfqVmX27qC3T7SrrypxVqIJubV68Xg9Jse1bv_JpE9KZT-XWMN2ili8vj0MkGR9ZrSFGUnqTBw-BCdokYPVu8-dlJDVS5Ar9akhZU8oPWXE9gwBH9RkAHZzfvPwT2o9bYG5S869ACmiLF-ZyObH_z96iIHOuwA9ih4coARjGbEytAorrvWI1aUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=R5x7Kg1hk-VbrCkqTUYO_dIqJbhkXUKoCGQDd1SXOAEP7rfDxSyU9qBD_SK1Ngbb2BDcis7j_cCgQUr8x6KmwARdbfOkjSU_fV7k-xSFZF59F8rUmssACO7TBL6wIR7iEHEpBMA1JZ5ob3nWS2OidR2oRDzq8DiyfqVmX27qC3T7SrrypxVqIJubV68Xg9Jse1bv_JpE9KZT-XWMN2ili8vj0MkGR9ZrSFGUnqTBw-BCdokYPVu8-dlJDVS5Ar9akhZU8oPWXE9gwBH9RkAHZzfvPwT2o9bYG5S869ACmiLF-ZyObH_z96iIHOuwA9ih4coARjGbEytAorrvWI1aUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=DfVlD3sxJDhPTnnGc6qI63aYCxLYrMRQ5wwdUeZ4zHww6_knArVFxipVnyD99OJrFLzigg9NmKXVFtkwDdDCp-Cq-siXg8G3TZZmKRl-vb28tY1Cnagz_YNLzc2RqtjfkdlgEo7M6d9MC2DH75yowgKalgCl6mTCjGDwsu1W7eb3Sy3avVXuNUQ4cKmhzucQx-XNMwdpTih8R36c2w5mUDyya3Hi13yjP75AnI0rU1jfDHkyXbxPIQvPrBz90gAXWlsGy6a81RYyrpKFn0Bkcggr1yYL7evd_Mzyqh3oz3tng-OQ9JG6UMnpmD4m5QI94cd9Oqkzy_bzXsmH_5a5RmG2Dx0fp1QUNpKsLAWIdtkj2mbWhUTS_lYjPxsJmahHrQYNprWk1y8DT4Ir6ywVNaHnubZCOtdjuglRhIclGakrCSxEoUi8JgfmIB0-HJbRDNz5SctwfDll8lYmxdL_fZeDoezfNBfcpc-2Qdk3L-p57rvpXAl5eBTTVm5JogEOJiV3x1jMjwueV5jvvtzdFKGsn5OOJMBT63MKi-y1SgM5pCzoC8ebVTxEsE06Emv4UOb6A-VE2S-nrJ_b0IKHzheG3COIl7FQ9b5BMhfB-oybl0i5HLG3No9W9k2u78cMHjghTUe6vb8h16vKPj9f31ojEVPm8gD_8tounivNRrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=DfVlD3sxJDhPTnnGc6qI63aYCxLYrMRQ5wwdUeZ4zHww6_knArVFxipVnyD99OJrFLzigg9NmKXVFtkwDdDCp-Cq-siXg8G3TZZmKRl-vb28tY1Cnagz_YNLzc2RqtjfkdlgEo7M6d9MC2DH75yowgKalgCl6mTCjGDwsu1W7eb3Sy3avVXuNUQ4cKmhzucQx-XNMwdpTih8R36c2w5mUDyya3Hi13yjP75AnI0rU1jfDHkyXbxPIQvPrBz90gAXWlsGy6a81RYyrpKFn0Bkcggr1yYL7evd_Mzyqh3oz3tng-OQ9JG6UMnpmD4m5QI94cd9Oqkzy_bzXsmH_5a5RmG2Dx0fp1QUNpKsLAWIdtkj2mbWhUTS_lYjPxsJmahHrQYNprWk1y8DT4Ir6ywVNaHnubZCOtdjuglRhIclGakrCSxEoUi8JgfmIB0-HJbRDNz5SctwfDll8lYmxdL_fZeDoezfNBfcpc-2Qdk3L-p57rvpXAl5eBTTVm5JogEOJiV3x1jMjwueV5jvvtzdFKGsn5OOJMBT63MKi-y1SgM5pCzoC8ebVTxEsE06Emv4UOb6A-VE2S-nrJ_b0IKHzheG3COIl7FQ9b5BMhfB-oybl0i5HLG3No9W9k2u78cMHjghTUe6vb8h16vKPj9f31ojEVPm8gD_8tounivNRrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QholPqlGVaOZzWnusWlo0lwI3YAHYn0HyP36z-tE5JMMO_zX5awY5HZdUbB0NFtSbu6H6DiEoKPJHKaPMDlY539U7iq9TGVnqR7BpZnpytry3cetZU_QToaUpghq-CyAVeUGBANyN0zl16Yafx_JOhleY0UftlKVDgmbxg2ckyGkDmf3bf06reHUsvORUtnjjRymxStIlPhgnX_3rvXUuUSIXtICU8hePzQhcY6rOjtt9nYFlURS2RgGkkf9lpYwyT1uHMCJE9ZQZj9Lp-ekAVPLfGM3hVOk8FVwWubstcc_a7ZvTe0CW45sIW1y2nds5XG2ROTqRUmL2YXnJohTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=pRI4kKETA8zYizHEvbUglYguhycBpIX7E-LxavtwYIdBjDDnvf0scPA2Fy1kFI26_phvrtm8gtI5qu_QHW0fFn-sBPurtpSvxqu9oSifjncaPMQabpC0ZeUf5AId39Zny4465yFQzCe7CclZOv90t3k9UGM9SMAGrhzQU8QH2hxutthMGb1ccJA06dGMPGIgS9nbXvb5Q_TUit5BtWWBBl3htnLXTdEL7J_rvwzvaBs5x3a7OcoAP5DOEXt0gMpnenzhnUT9Wi8ems_McvoC1JdRxi0ByrdHV_b6DdikU7wQlZdL7iYqZXJ4iusfiVwSut62Fop8cogqlIa6P5tjMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=pRI4kKETA8zYizHEvbUglYguhycBpIX7E-LxavtwYIdBjDDnvf0scPA2Fy1kFI26_phvrtm8gtI5qu_QHW0fFn-sBPurtpSvxqu9oSifjncaPMQabpC0ZeUf5AId39Zny4465yFQzCe7CclZOv90t3k9UGM9SMAGrhzQU8QH2hxutthMGb1ccJA06dGMPGIgS9nbXvb5Q_TUit5BtWWBBl3htnLXTdEL7J_rvwzvaBs5x3a7OcoAP5DOEXt0gMpnenzhnUT9Wi8ems_McvoC1JdRxi0ByrdHV_b6DdikU7wQlZdL7iYqZXJ4iusfiVwSut62Fop8cogqlIa6P5tjMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=VClrxKsRR0psolAiE6Hul4svZ6ux0-YJ4v8JO2aoUZFQJK5rjDmhaFEboj2NTnF5CuQYHV_9X-F3gey1wk-Bn79Jj9CsTECEj7zcaLxsoXfiIh1Tmm7NQ2XXByWEMfqnQoM0EGTTN0s217q2FY39wSvqdgg0mDuvWX7sKUZM54uew9lGjEFWdx1UhhqYPJYrp9e3qBSaw2LeYET9Kt3Rd9K7bbcH7aYWkneOLVqcJ9oFhn04PV68Bhvs3lLU4Nx6eYhQbhoLJjJXd6hOAe86vzQmdwh0YaQtZFy-iz8T8EaqLFOH4ANaO9gW7hIZ8OLbPz6eBBvP-iI8nKMcJutO_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=VClrxKsRR0psolAiE6Hul4svZ6ux0-YJ4v8JO2aoUZFQJK5rjDmhaFEboj2NTnF5CuQYHV_9X-F3gey1wk-Bn79Jj9CsTECEj7zcaLxsoXfiIh1Tmm7NQ2XXByWEMfqnQoM0EGTTN0s217q2FY39wSvqdgg0mDuvWX7sKUZM54uew9lGjEFWdx1UhhqYPJYrp9e3qBSaw2LeYET9Kt3Rd9K7bbcH7aYWkneOLVqcJ9oFhn04PV68Bhvs3lLU4Nx6eYhQbhoLJjJXd6hOAe86vzQmdwh0YaQtZFy-iz8T8EaqLFOH4ANaO9gW7hIZ8OLbPz6eBBvP-iI8nKMcJutO_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmBJAhSiS7LWgd9AdsoasPCyMhhgv7u19VH8X_O6325j7vLNwmTp2NuuUXQRcd_cS497CXd2T5Kk5V8U29FlcR1JyRoeCnvXeh8U8Gtm9GLlVdcPGWztmIU9l1IZRshY8-WS9a_-P0dfFy63tfh6ArPXQombeSQsOEBNj84XgsHrx_vq4B_YDZ_4qinef1noKsqSlWYa_7WOI0PIxgVJxbwJ3bxLFBKk4w3b8J77jzvXm98j_GpfrezjA93JfeXP0zst9RTyVYOTxPdIpXBu0UvkH68VFfyyB9Qvh30q2_waQobQKQJVdREweZCpZAwpWUxbl_w5sDU9sgp6GRAsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=PklQcGZvz1ltJQPWyoLPeflIi3pMY_6tkKpz58cPWooFO5mODJ19QiEwEm43DRVNaTZr56yWZNEzhQgZ8___x_3PAvt-UnahmYseAchCgbsPtGv2K5wvuN1n-EEluc-G0gllXWCvHPVic6o7O6PrizqApQ2imOk19AO_7t_p7v5hfSzggKlrbwW0YjBpa_UFh86wlMbqIRWJufwL34RZmwgM4Qnc4HIdnLZzWq1hofc7UhRn3zaTwYSGyr2uOALZE1Ql6urzHTGwp2Q6D7l6wJiSfSjU9OeUxCdOhwuqorhRYCPiNeKe1xY0XFFiPGGVLxCMI5iBzCPIoq_y3zzbHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=PklQcGZvz1ltJQPWyoLPeflIi3pMY_6tkKpz58cPWooFO5mODJ19QiEwEm43DRVNaTZr56yWZNEzhQgZ8___x_3PAvt-UnahmYseAchCgbsPtGv2K5wvuN1n-EEluc-G0gllXWCvHPVic6o7O6PrizqApQ2imOk19AO_7t_p7v5hfSzggKlrbwW0YjBpa_UFh86wlMbqIRWJufwL34RZmwgM4Qnc4HIdnLZzWq1hofc7UhRn3zaTwYSGyr2uOALZE1Ql6urzHTGwp2Q6D7l6wJiSfSjU9OeUxCdOhwuqorhRYCPiNeKe1xY0XFFiPGGVLxCMI5iBzCPIoq_y3zzbHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=B2q3bV7oJkiiS2Xca8MbuXX-zs-sRJ7PlfO-ANodEEA3mRk_5pNwGQJ9ukHVZBVXtgX9Vk-J1kakKQJAx7VHi8aAPt3uBDJIDfzOTBylrpRxoZ47hAdz7lIokBCHBww0cjEztZFnCKYbr0qm66aPkUfoX3wNszHMbvblrLAO-3x2qSbRMDSa5at4aWyFS-gEIL-26Q5cbJNhIAIoWpVCZQ2Ftetk3PyL7XuduRf3FD9E-h3knRtYmKaxYKnsEHZZRuddQ7Bq1WjoEJBwJJkGNizN1Nhu4-AnWwFSZ0NFVRra2pi9kCFEixAA2tgiCcJIHax8JcPoFR6ilHVWo4ZKvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=B2q3bV7oJkiiS2Xca8MbuXX-zs-sRJ7PlfO-ANodEEA3mRk_5pNwGQJ9ukHVZBVXtgX9Vk-J1kakKQJAx7VHi8aAPt3uBDJIDfzOTBylrpRxoZ47hAdz7lIokBCHBww0cjEztZFnCKYbr0qm66aPkUfoX3wNszHMbvblrLAO-3x2qSbRMDSa5at4aWyFS-gEIL-26Q5cbJNhIAIoWpVCZQ2Ftetk3PyL7XuduRf3FD9E-h3knRtYmKaxYKnsEHZZRuddQ7Bq1WjoEJBwJJkGNizN1Nhu4-AnWwFSZ0NFVRra2pi9kCFEixAA2tgiCcJIHax8JcPoFR6ilHVWo4ZKvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=sIhiMJhf5-oOxwk2yOBaNZ5U2ervRm3qcKJkpqhivSw63wEWTFrcZYMe0gDGVO65VXsPN-gqZeYRVzkUo87yJyu8t2UFx2_kkXC9qxACFmmgZtksRWVggybGPSjUck3D7prfek6rec4JwFyQ4j8Mi_A3g5QWsVzpHHPVNdjsVHQmjIypLnMtncvkESckWUmz1ZXmks52VYIohu9Y1MU83HwpLjPCP3CRUrqHDUCGbekXQf2XhGD8hBSfwZ6GQvIXAVjIgR8Fx3ib6-XvJEi_-hy_Fy14LRwZkwltkwXO3F1MLQNWouJ17nd_qv5U5uXwY1NEr8EqJdS6DjHzSpuNyHUbMEf9pL3upWuk72XO5fsMeEkTorBh4kle4hd5hSb3H3qsEm-Ap4VDjRhki382DKU6sZI7cMyAIILGX3bqr9nBxH14ttTWcXLv8NPhtzGs5PrSS127fHbGNwX3PtQtl52fzKWNcGICSWxIXB4T0ZRjhZ_cNRpCkq6C7TcCFxSh5dE5ryvHIez6RPeL2ChP22UwlXc6z5BpalHjP29ac84SNO0ZDNn95N6FilySdTDasqxMoibhct7LJpS_Jp0dwl9Or3h7xtxLoqu_pUsuc6UQVJ-EBzPtdGGr3kjl8j29LMLUenvLRrSaspi7HroaxQLNgcmRoYHFjKj2DAXXF34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=sIhiMJhf5-oOxwk2yOBaNZ5U2ervRm3qcKJkpqhivSw63wEWTFrcZYMe0gDGVO65VXsPN-gqZeYRVzkUo87yJyu8t2UFx2_kkXC9qxACFmmgZtksRWVggybGPSjUck3D7prfek6rec4JwFyQ4j8Mi_A3g5QWsVzpHHPVNdjsVHQmjIypLnMtncvkESckWUmz1ZXmks52VYIohu9Y1MU83HwpLjPCP3CRUrqHDUCGbekXQf2XhGD8hBSfwZ6GQvIXAVjIgR8Fx3ib6-XvJEi_-hy_Fy14LRwZkwltkwXO3F1MLQNWouJ17nd_qv5U5uXwY1NEr8EqJdS6DjHzSpuNyHUbMEf9pL3upWuk72XO5fsMeEkTorBh4kle4hd5hSb3H3qsEm-Ap4VDjRhki382DKU6sZI7cMyAIILGX3bqr9nBxH14ttTWcXLv8NPhtzGs5PrSS127fHbGNwX3PtQtl52fzKWNcGICSWxIXB4T0ZRjhZ_cNRpCkq6C7TcCFxSh5dE5ryvHIez6RPeL2ChP22UwlXc6z5BpalHjP29ac84SNO0ZDNn95N6FilySdTDasqxMoibhct7LJpS_Jp0dwl9Or3h7xtxLoqu_pUsuc6UQVJ-EBzPtdGGr3kjl8j29LMLUenvLRrSaspi7HroaxQLNgcmRoYHFjKj2DAXXF34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=AAG5WmMD1Jupu5jur_hp8BgrFMzBamD2ObFAbaykm3pSb-eExv1bP5UgVJFdnub85rEFpXTlHoMz16szELCA7lZf1PtyZbbV-XSmink1v9ZjcuYeRRuJ45bzg8vJdE2n81XXB3HmvF9gF_54RKGNZtqepjGIy49K5_0WwQU5HBbt9jhCDQL_ay7undXn2-W12GV4r6GVdsrVuzFnzuJ205qwnOOzNB7XNIHLxKSrtxyjswQXZ7_dmMclHCD21JBT5ql4fRl6P-aHJVYTzqkVCK1t0rs_CkC-D7LvDcoV6Q1v8T9Aiks3u9z4TFn2OqOTkdmbGseHEHHFr22hTxh9dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=AAG5WmMD1Jupu5jur_hp8BgrFMzBamD2ObFAbaykm3pSb-eExv1bP5UgVJFdnub85rEFpXTlHoMz16szELCA7lZf1PtyZbbV-XSmink1v9ZjcuYeRRuJ45bzg8vJdE2n81XXB3HmvF9gF_54RKGNZtqepjGIy49K5_0WwQU5HBbt9jhCDQL_ay7undXn2-W12GV4r6GVdsrVuzFnzuJ205qwnOOzNB7XNIHLxKSrtxyjswQXZ7_dmMclHCD21JBT5ql4fRl6P-aHJVYTzqkVCK1t0rs_CkC-D7LvDcoV6Q1v8T9Aiks3u9z4TFn2OqOTkdmbGseHEHHFr22hTxh9dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDJsvY-k3nQIop3kZT_kC77Fat9Mw5L827i1q2iH6STE7m1C4SqKsTLKAowN3o6jE_foJ9Ur1Bcbs3BpjpGC3Du-xidc_Mx2QroNjumzy6e_TB5Ppjgs-L0O8XrZZh-MfZAn36qJk5QDxYQX1VtiGdqF_PcQe-gbz_WVst-fKsh7fxrg1fxHh5kOXtsPUSzhx4i12LMH2he5Z5nwKW4W6Xc5T6i3Ea4MDPpmAjbPMJ5Pc_JqnXKcO1ekxxgSbxmDP-GiuGy0yZaBU24Kik0bi1O63fKjtReqmvkFTQAPVmyKQK6L4xGBiBa8lqseBQuA-MSgCqLn5mVQDtCigd35SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=ofTAzW78Dd7B_jtzffhmTVq4jZBDGNzDkxJYwXzfSdvASVivAG8f55y55J9SZAbn9QDqUsAcIjnyYfIj7H5ikmGOge3hzjQuO_kyNLKU19BVlbkOY3AGP5PhDYzOYtaXjOfK0aR09WYzTVhDHTwCB-5vVWi-E-CKscv4LnOZYKj0X5GNJbfnzXrnd8lhkf9znICWcf-RJSMGGmpD9doaVHSjF4HDgQkzodlFoNY_PW0IDnaLHjt_E4wKsNpH2wiRLtQAZ_wSHGVxvEC7elSMdoGhwHN5_RDYEI1hiWs7TAjEACXBVN1GR0TJaacDHl5tZhaq6U-KNp5bxX2SMg3ayw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=ofTAzW78Dd7B_jtzffhmTVq4jZBDGNzDkxJYwXzfSdvASVivAG8f55y55J9SZAbn9QDqUsAcIjnyYfIj7H5ikmGOge3hzjQuO_kyNLKU19BVlbkOY3AGP5PhDYzOYtaXjOfK0aR09WYzTVhDHTwCB-5vVWi-E-CKscv4LnOZYKj0X5GNJbfnzXrnd8lhkf9znICWcf-RJSMGGmpD9doaVHSjF4HDgQkzodlFoNY_PW0IDnaLHjt_E4wKsNpH2wiRLtQAZ_wSHGVxvEC7elSMdoGhwHN5_RDYEI1hiWs7TAjEACXBVN1GR0TJaacDHl5tZhaq6U-KNp5bxX2SMg3ayw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=qEkiBpCl94BgqLWLK6Gqp6_5Ig76bL5vnSjDjZ74uX46ZdUIwHiy7QmZg2mVVjh_rIf57Rev5zG3WTrxzaHv-uxoIaNAuMf_L-MyMiaCgt-oGv_YOivHT-Ad2PE9PlZ7yjkCn_pHdSx1uTPNR1hbBtJeSWlycIhgQI43ZcFTaMbZ5rFKaoc2V-IWKaZ0D2ug6jRkZ1VNeH5BWyPLpde21gOOOuKzwLeaW1mGNjhqIvKpv84geph8D7YyUS-n3YLP_gvZrxDd6rISnLxpx3vAWb5yRlGd2J--0Z9bAIJ89uPkVICcdoc7SOO8bRTZY2bmBSvgISXyZEKuQgUuujWCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=qEkiBpCl94BgqLWLK6Gqp6_5Ig76bL5vnSjDjZ74uX46ZdUIwHiy7QmZg2mVVjh_rIf57Rev5zG3WTrxzaHv-uxoIaNAuMf_L-MyMiaCgt-oGv_YOivHT-Ad2PE9PlZ7yjkCn_pHdSx1uTPNR1hbBtJeSWlycIhgQI43ZcFTaMbZ5rFKaoc2V-IWKaZ0D2ug6jRkZ1VNeH5BWyPLpde21gOOOuKzwLeaW1mGNjhqIvKpv84geph8D7YyUS-n3YLP_gvZrxDd6rISnLxpx3vAWb5yRlGd2J--0Z9bAIJ89uPkVICcdoc7SOO8bRTZY2bmBSvgISXyZEKuQgUuujWCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Y-KdvmAEIMKRpnFWXdTyhWXDq8eJQhfwD5l7x31lLp6GvhWBEpYsvEzrEt3UdObQIYoJpY8CYlBiJrFLZ5GFHQasRTShbEZTrmawaWfmxBEFJRk_rHXGz3FgYTcgvDmgoAeLAkJ2a2J3_7wd3-CjmbJAj8vtKiAoRW1G_rD6MzVzQgeXUG2yJMYGs_ZwVkJ8tn0guOnk5tbtP_QKuGPTWCNsrFXds4u3k4wt4xvcqRiSOdudhgpZuk9Y54tFygjjBWQa43tIHKF9X2T1W4dwZ9TlRAQ-pceRYJXDdxLuvU6gRwcsrl2p13Hav08DUVFftX0c6j3PrYOK2Xv6gMKyTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=Y-KdvmAEIMKRpnFWXdTyhWXDq8eJQhfwD5l7x31lLp6GvhWBEpYsvEzrEt3UdObQIYoJpY8CYlBiJrFLZ5GFHQasRTShbEZTrmawaWfmxBEFJRk_rHXGz3FgYTcgvDmgoAeLAkJ2a2J3_7wd3-CjmbJAj8vtKiAoRW1G_rD6MzVzQgeXUG2yJMYGs_ZwVkJ8tn0guOnk5tbtP_QKuGPTWCNsrFXds4u3k4wt4xvcqRiSOdudhgpZuk9Y54tFygjjBWQa43tIHKF9X2T1W4dwZ9TlRAQ-pceRYJXDdxLuvU6gRwcsrl2p13Hav08DUVFftX0c6j3PrYOK2Xv6gMKyTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUI2pLxZfvnc7hB8nM_aaB3-dMtl9eO-rcagcYmBbQgkpt3s6q_ylMICSXZ2hWGzuextR4FHsiA9-BivwWkwtnEn9NOih7a5NbJW-GKWoXw_WHxAXMC3QmRH83F3irKOzvpGGI4sWQxUwxio8sdDs-_MKozsoA-PJUZ13j-Vgu08hVzXBRp1f1WzSeP623t1B0aUjNq5h3C_eE6ywsHBf5608j11VRdDPnsKpYl8IghpNlgc0_ezEPdPNCd9yil4RSeFOuNdMFd0nkkGMy_MJWk0h7Dlcmr7pmRdjv34zzIztiHR87VH8Sut6qJlQwmFTqra-fKHLodu9BX62w4fDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=dRA6LaLNvwrY-5eecBZ7klJKW8pmxgktqPpO0S0ANQ5pyW5985w0qa2Sxt9tZEkAavvnutO-rjITw3ms9ZWHPShasTi3K16nBQnF9q4jWge1XHy6RoPNHvr6baQVez6PPCEYzz-BmEIwLEyQxf1aqxal3Sjvum_EwXYdFU3CfYzORSRZHePvRScfKJoV6Q-eQU2PFjqeq4CmphEyPiDr1yQxKSqwBBhNXS8H4vEaBKD8zO5VBIc-3azwwRxJX1M3UDxpVL_r9bduB7r-GD3RVvZWcB_5lQSpCouEVjSMzF7R41Dhr3qL1i2FI_wTMPkzmF1VgIXx3Ybx5oTHbsqEUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=dRA6LaLNvwrY-5eecBZ7klJKW8pmxgktqPpO0S0ANQ5pyW5985w0qa2Sxt9tZEkAavvnutO-rjITw3ms9ZWHPShasTi3K16nBQnF9q4jWge1XHy6RoPNHvr6baQVez6PPCEYzz-BmEIwLEyQxf1aqxal3Sjvum_EwXYdFU3CfYzORSRZHePvRScfKJoV6Q-eQU2PFjqeq4CmphEyPiDr1yQxKSqwBBhNXS8H4vEaBKD8zO5VBIc-3azwwRxJX1M3UDxpVL_r9bduB7r-GD3RVvZWcB_5lQSpCouEVjSMzF7R41Dhr3qL1i2FI_wTMPkzmF1VgIXx3Ybx5oTHbsqEUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=flFonfWO_LSrl_Asgew3PG8llHzsxTWDWOw4sl_eu_TZ3jxABG7Xy4mB9FL22hwfhHQnkPwBn6jwwyKK5tv0VRsZS3B-O9SgY-ePgF1dgjvqdiMCJes7f5cgrNGnypSI5JwvjJowaJwjPeKP9OurSsN_pbbkbVmPsGtAebWmajMDPtG649NLLMaQNCEjzZdfN0Dretl-9FqXh_dl61HNCgzVC7Vel3GNgCS78gsDsD_5ZbKUbVdsD2TcJSEqa4euo7ag4roKKs6TLXKWiQ3lsahzB0l7mJCeN1krNI-GED1QG76RhIR07FRT2ohtov_3MKrn0ku3C7qPlhCjZygh4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=flFonfWO_LSrl_Asgew3PG8llHzsxTWDWOw4sl_eu_TZ3jxABG7Xy4mB9FL22hwfhHQnkPwBn6jwwyKK5tv0VRsZS3B-O9SgY-ePgF1dgjvqdiMCJes7f5cgrNGnypSI5JwvjJowaJwjPeKP9OurSsN_pbbkbVmPsGtAebWmajMDPtG649NLLMaQNCEjzZdfN0Dretl-9FqXh_dl61HNCgzVC7Vel3GNgCS78gsDsD_5ZbKUbVdsD2TcJSEqa4euo7ag4roKKs6TLXKWiQ3lsahzB0l7mJCeN1krNI-GED1QG76RhIR07FRT2ohtov_3MKrn0ku3C7qPlhCjZygh4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=eIxIE76rfNWdsujGHerI3t7MtcEyVPB2bcmygDcz2zLYciZlo55cSNqmtj50kXQBJDIZQsbAXUEZeGEOadRd3YSPizze3bkMpys_HKWlEUEenfuwDPxewk1lBtjdZ-MZjJt3SYJ3D39-I8HxWLZ2xms1KlDwoc2j8q1M0IzUked85-CLQzWBRI827qfSbYB9ZkY8t6MuXQzzSZFcc1CzLbFhPFvFH9XRfKoTw134aT2rfuizzI_SSyycRSrgpW89Ji-Q0ehkB_qNF2ULWgD11A3VAnA5_0bvWyTEfUDSP4pK2D2mlcbG7vnvKQHSD74GswY2vpIQx1xrcWs15T6kLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=eIxIE76rfNWdsujGHerI3t7MtcEyVPB2bcmygDcz2zLYciZlo55cSNqmtj50kXQBJDIZQsbAXUEZeGEOadRd3YSPizze3bkMpys_HKWlEUEenfuwDPxewk1lBtjdZ-MZjJt3SYJ3D39-I8HxWLZ2xms1KlDwoc2j8q1M0IzUked85-CLQzWBRI827qfSbYB9ZkY8t6MuXQzzSZFcc1CzLbFhPFvFH9XRfKoTw134aT2rfuizzI_SSyycRSrgpW89Ji-Q0ehkB_qNF2ULWgD11A3VAnA5_0bvWyTEfUDSP4pK2D2mlcbG7vnvKQHSD74GswY2vpIQx1xrcWs15T6kLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=ucZMvLoUY4qw_T6fCo2JrwiNZ1PJO38BCGBMW2-T1naAtkQ_habL_ZtQvoJrqyldxd4G8or7Sdf5S4HdWsh87Jyf0VSBiVzYt2ad5A4PqM8lypvamSI7B6X2b7NItSHWuSBTTckM7RWs5RebyFT_TCKNfKiFWf9Rngzl8M3DkhOAc5mu1uLPOD9L78pKscK_iEJVvlB811peWipa9uD_N5CNm8eYi4Wb_KshzQVmTvn8m3du5M8P7EZFgD5QA5qaGs6HnBxna4ScDvWvkJATD9Ue5xWrFBdcV9EHQKJHjoY-7jjx8vMHz7RG92SFwQ1vhMHzA3w5IRDkTuWu1f8TZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=ucZMvLoUY4qw_T6fCo2JrwiNZ1PJO38BCGBMW2-T1naAtkQ_habL_ZtQvoJrqyldxd4G8or7Sdf5S4HdWsh87Jyf0VSBiVzYt2ad5A4PqM8lypvamSI7B6X2b7NItSHWuSBTTckM7RWs5RebyFT_TCKNfKiFWf9Rngzl8M3DkhOAc5mu1uLPOD9L78pKscK_iEJVvlB811peWipa9uD_N5CNm8eYi4Wb_KshzQVmTvn8m3du5M8P7EZFgD5QA5qaGs6HnBxna4ScDvWvkJATD9Ue5xWrFBdcV9EHQKJHjoY-7jjx8vMHz7RG92SFwQ1vhMHzA3w5IRDkTuWu1f8TZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szKSdO2P7G3OAmUJMsiYmraAkUANxFwFlMejn9vxA0jBAAWOfbGijhxOFLeB2i9NAp0w8_ar0EqmagleYcjPT_dyV8FQpDOFGkfOKcBCb4Wxv23Wol41KlTqbR5b48eqZjfLrmWu0AEefHLRSGNWRCH5TDHQwxJuNixqpbtXK_RvtQ8GIQwP2W0L4mQPmU_aO9O95eAW0CmfrgW9nynSeURFLQ9nUaQv7rHkSO8s-D2jS-SiP0d8zUAC_QvuRENbCwqUIQipKMXu2bGBdfL7FFjJokv5cfofulJwxg5cTZzPDIC44LJN9Qf--3iHaWoqVvJLtQr573duQ4gvSeaTCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdIUwoxE0axFTLeWFXDN1S5aBWkRKRbtMr5a5xe-T2vs70oLYtr_NeSEgkPAAXVVNUc60HgzPMCxLLG9ZxKf3hXahoIC4J7_WIy4j2obm_tFvp5vVoxF73gMTVHvPJD5GyANnLVNlBDNNaUYbTpmArfJ05Iwd2W0zKKkipeDNCX2pEZp520Hx-4tE-9WzjTvH2AhxVREbwL_Ee7yUvmSBmGlJ1sT89eHeJO7j7UUH0XL9jmY8VPC5HXgOg72nvjJEwGtD5azMyVBlpisX1BPE-Pox0Fs5tL-AOcXUp3ceAgdQdSptuRs2dSQ19SROGqJZrcE04e_z1QYwER3MzkElA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6jJbwUjimdgGHiTL5jZ9sPhAaYE9aiXBG5060-uNfi_f41yJYiMKyRyiKbY8iP97I85mjnscLsmdicmCPfO1QUlm0JKs8KMOAfcjZo6iH6VWTjkw-g46wcMUAupHSYuzpmpRMu1gTlfk6VA_PK6Mv25buFcoWo5JlW5mWLyndzZsA6BCAf8m9ymsvpBe5-c-EWPClJ9ScQuTeTp42LOyoQFx8J8txiyHqLfT5YtjNqEYWVFGqIMe0ku6kZ5l8-DdDqcee57rwg8egx2Ex18dUdulLBXceWBGNxBLN1y3rajoTJCwOxcoC2X_OIrqTrXdpV-eofyEok39_sMc0_Sfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnsZ-W4i_bBSHur5Q0EAXOgGWq5qRmeSULj_nGwxN7y3-4T86ikLm8GHYlQa122-JTp-AxJ38gwTi5SwfzLzOagisbekU-h5GHh04WT5G9Fy4RRLLAKNF-OyzOrcKT9soKwJdi4BX-Yrlf7pAHZ1XTL7-CqzXkn_wR3A8ledLDHFZ9dYERiv7-QPbs3vdRBTMDzVjOYOWA1aV5vvL4r2EbfFKxKM51uClkbg8jyYXTC8Iu-O1jtYAonQy7TDkky4QVFGiYNs9YtaKUL6-8JkmSrhHwiWLiq0ruyQ7zUOlAzqLQNEiGCpBeijdO06RQgjYLzv79HSAhtV0xqYy7rO9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYf9tavwM2ronaPMBKE5VJJQwRgiQjFfnmHKD--DgcvEaSXe8Xts1RPVXI7ybIplhII7XcOCtKjHewxzzBxY5H_PqmdOstn3KlzH3u1WRvl2cMezk0QvgcBzokecgPtuIjQ_mNglB5sDJgyCkWWv3E7UiTGafosj3dZ2inuVssdN5hiUP2_S35dFeLP70FOtJW5bedmvVbWlfO8ZeL1u8d5rl7h_EGM6H7nIXJi9sglQM3jd7ikXPXOav8lvBlFASuW8zTUO_ZEIHCWIqiWtRX-BjPvpVh4eoKncW47y8tk_u12azB7iDVXYPwgHs0lk-9EfthwthLbK8Kcl8h7DcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=aTL5o4J7mJGd76SQNT2UAmjVDnhdGL10BUqWAdCikr8aniPHxUDDynV3IakQyFjzW41YBNAu2uKkDnWY9xhI5egmnfTtQDOORmOJ5Gfu5KeGc-AiGmyKdZ-qqx0KacBsO662HY-ajjLE4XH6QEcPe5mY-9BQ6PTcyxB8_79lntAzZfvrJUGkvRiLRXCRVrb6e457NpkXYKsncpulzRrF_BJFDFlM5QhlvpuY6c8iNYK8vNUkFmHwqtuFMuGt1-y-7YzV1h68ZhMunEx311ITd86-204RIxi1wddfIRwP0yRe5wywGklks1L91ZZDrPl-UXjThWytdSRekVkjRtXsXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=aTL5o4J7mJGd76SQNT2UAmjVDnhdGL10BUqWAdCikr8aniPHxUDDynV3IakQyFjzW41YBNAu2uKkDnWY9xhI5egmnfTtQDOORmOJ5Gfu5KeGc-AiGmyKdZ-qqx0KacBsO662HY-ajjLE4XH6QEcPe5mY-9BQ6PTcyxB8_79lntAzZfvrJUGkvRiLRXCRVrb6e457NpkXYKsncpulzRrF_BJFDFlM5QhlvpuY6c8iNYK8vNUkFmHwqtuFMuGt1-y-7YzV1h68ZhMunEx311ITd86-204RIxi1wddfIRwP0yRe5wywGklks1L91ZZDrPl-UXjThWytdSRekVkjRtXsXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DLDUaE19xJZNDY6q2bHbpZh3hN0aEhldJ7fhjhvUH_ousoX1Nq8pXwAXp9vOvfieaf9ZVD9rYFvSU3tcSVJKPEPBNmtx5jZh4YBCnItdDxdW1bZQPbXKy_ix0f_lkI3I8rkS4NF1dcWGxgzlQWmV_V1RImv_0sgfsYGvWjanpbd99iE9wZ6bPkOwNb17Tr0Q6c7f2C8hCBgdVrJRWUlVC4ugydCGApEg2KcOSSI2IU5bNWLbYJ9NrGDZlaEWCHlDxWJUIg5_chmibOQuFXEquCrs_YeIHWsreY3sa9d7vKzHM97m-tGAqbtR6BgURehHpJXOP8rqv8McHlQN3X0S1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IiDhTNASRROz1W4ws_v0TEA5ApbPw3GcfnWUHmQrUrqD-ewn-BizmdoC8R-hx2N-UNv9WSDJmzQlv7wA2eWHxpO-VFUPugfOqQnEg1k2jCHugqYua0qleqfY4n_KeKesrsSXvstpTtVNEi0gIU_tdHsUXsKvFfF_tCOpUVFgik8Z4IVfHdp12cEe_BzmyTi3CVEj8pVdGHDNr4uyQQ3osfbahogbp5GCJ9iV1Ud3nb8gr9DvVwEfqe7g6i5nSXNsuT52WLlL2R1XgLYqv5sD_pK7s4YhvuMRHekUa_EEVQg0MPRVLlYnLHTgfMtrzSZGNLRsKgAFip65T6lE1A41AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=dILo6zyv8_X-pIK9BgTBtMPK04ZHFFu0L9rSwEf7snFK505b6VZUEKiSKHFEjM16JbdxIdhQx1-B8tD5dOP3z8iI-X1bQWW0XAukOup9zBmfxma9px8WoUF7qD1pdS9WfXkRpXd5809J9NnQhGSwOvBZoATu6eL1Y-juelQkjU1Pyh9Z8jb-Wv5rSaLwVdhMXZp9_cxPojRQSvizYN6Kv1r1b0quXF5MnVz-17jO7qnCi0WgFuLAA5Ad5vxR2N_3E6mSiOBfAChaivOaK1VnBnmHPN7ulUKHOVPvXptiuwf2Q87fj-NIYWsdisIN7nU6nXIK_hf_CbYTsgRhZVM2HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=dILo6zyv8_X-pIK9BgTBtMPK04ZHFFu0L9rSwEf7snFK505b6VZUEKiSKHFEjM16JbdxIdhQx1-B8tD5dOP3z8iI-X1bQWW0XAukOup9zBmfxma9px8WoUF7qD1pdS9WfXkRpXd5809J9NnQhGSwOvBZoATu6eL1Y-juelQkjU1Pyh9Z8jb-Wv5rSaLwVdhMXZp9_cxPojRQSvizYN6Kv1r1b0quXF5MnVz-17jO7qnCi0WgFuLAA5Ad5vxR2N_3E6mSiOBfAChaivOaK1VnBnmHPN7ulUKHOVPvXptiuwf2Q87fj-NIYWsdisIN7nU6nXIK_hf_CbYTsgRhZVM2HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=uZ6XgN1UXkcmfUskTj8yYe30NVo1Sv1I_jI22CEu_xeKNHTgkuGV89bwI6B_804KEv3aFqEhvylJ3-DEiCIsMBTNsaBroSXKKC3dnDmmlSOD4kE9PMK0m109oB-zd1-58qANnS9DuY4zOhCcv2G8dliaGyPflpylCs6Jkj9YsA2Wco5_FVa4rSGkuVeVhVPHx1NhYTjgSjF7W3hvwt71D2RyXAFTgFHr3mXlE7JYYzYURhaO6hl8x-QjF6QcJ556yYELZXIcdcZNP4p15UWLh01AA_sVptLyvZARZ6Gw5CHomiRG-ktY3H7ZD_CW3XmqJ-cMEoBYiSMdnuAko6SJ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=uZ6XgN1UXkcmfUskTj8yYe30NVo1Sv1I_jI22CEu_xeKNHTgkuGV89bwI6B_804KEv3aFqEhvylJ3-DEiCIsMBTNsaBroSXKKC3dnDmmlSOD4kE9PMK0m109oB-zd1-58qANnS9DuY4zOhCcv2G8dliaGyPflpylCs6Jkj9YsA2Wco5_FVa4rSGkuVeVhVPHx1NhYTjgSjF7W3hvwt71D2RyXAFTgFHr3mXlE7JYYzYURhaO6hl8x-QjF6QcJ556yYELZXIcdcZNP4p15UWLh01AA_sVptLyvZARZ6Gw5CHomiRG-ktY3H7ZD_CW3XmqJ-cMEoBYiSMdnuAko6SJ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=DLj8Z07XX3v6oIjDfHrqM7sCKlzcTS-iugVsh_B7WcE1jxl7oM1hVSzJMHyqHqn9Nnx3Ry8DQFMOvIp-DXZc1aYqq98h0mGnNm_PjoGSoTzKAWkU_1dGkaUpjm9Yyc4kNFwuGdRaHbRAtbQqb1wdYvwBs4_JrgfUkox-QRuwm08v6dogmr7hP9W9z1FpXSHrGz49F7_GC9Dfclewh6N3AF6d5fcv8zGEwY5b_lwEhyAWN_QoqH3gucyAbluSDeXk95UWv3iZn3rItlZSAEco5wya6TJ6nmM73QLiWlCcqbAL_hjDysW8T8Nw8vewpyTw5E7Qu7FeR_yGJoHkQin8PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=DLj8Z07XX3v6oIjDfHrqM7sCKlzcTS-iugVsh_B7WcE1jxl7oM1hVSzJMHyqHqn9Nnx3Ry8DQFMOvIp-DXZc1aYqq98h0mGnNm_PjoGSoTzKAWkU_1dGkaUpjm9Yyc4kNFwuGdRaHbRAtbQqb1wdYvwBs4_JrgfUkox-QRuwm08v6dogmr7hP9W9z1FpXSHrGz49F7_GC9Dfclewh6N3AF6d5fcv8zGEwY5b_lwEhyAWN_QoqH3gucyAbluSDeXk95UWv3iZn3rItlZSAEco5wya6TJ6nmM73QLiWlCcqbAL_hjDysW8T8Nw8vewpyTw5E7Qu7FeR_yGJoHkQin8PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=XiYDz2BZYmsCkDDViQ2WZOm33Hp4Z-guxcAMn88p71ovnCXr8emOuvBcoEy6xKe9xsd2DztbNj0HcLXSoEh7EFNsIcmzTLyEQ7OXv6fo6oqpAwDxXQCGrR7qwZU46HMicuUsPj1esJZ5gZnb3fVwbFV2W2UB-GFqveScQE_XH94c_o3TJhq6pCkKs91YivypT1TnRYfCDvrDlV-P0CzkXf1-cncZWc45xxTrmLDLXGbn__Ff5H_jNRXe8l1G1w4Lz-uyh4Dn8o3dz6mWYbF7qKN2hFvrVwdmgCusgBdrUzcG1wN0tGaQNQLxLWgut_24wXBCxwr_YjiPfLk9ez-17Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=XiYDz2BZYmsCkDDViQ2WZOm33Hp4Z-guxcAMn88p71ovnCXr8emOuvBcoEy6xKe9xsd2DztbNj0HcLXSoEh7EFNsIcmzTLyEQ7OXv6fo6oqpAwDxXQCGrR7qwZU46HMicuUsPj1esJZ5gZnb3fVwbFV2W2UB-GFqveScQE_XH94c_o3TJhq6pCkKs91YivypT1TnRYfCDvrDlV-P0CzkXf1-cncZWc45xxTrmLDLXGbn__Ff5H_jNRXe8l1G1w4Lz-uyh4Dn8o3dz6mWYbF7qKN2hFvrVwdmgCusgBdrUzcG1wN0tGaQNQLxLWgut_24wXBCxwr_YjiPfLk9ez-17Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=oZmj1yTo32KhMq764hjvIyQrJ-6oU2k8tzZz5nUF6vtd3KQFpzFBd9ore8-CRrcDDRw60xo_pX2rKLDRPxTj_PGrfe8RHybvlaspJLboe-Q7f4YVoSkPZeoLLLkox3A_U1uVnheuUheFP__Bh-Tu2xVN9rdVlbudBp7mW2oktcpZgVDbc_Wj4mZicrHAyaxmxm3eNq92KUWytSJ7BnQm9FTazBobI9VWXcr-NnoXlcz11FsoRu2EATJlVebkWuuc6FGEPLcTjm-03EfZXhVcCGSx32_KnOkXPxdxMcOYC7TZGsDDz4VTyyC2yn1ju_lfEsI-sgRE9-G_B8iJCIG6eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=oZmj1yTo32KhMq764hjvIyQrJ-6oU2k8tzZz5nUF6vtd3KQFpzFBd9ore8-CRrcDDRw60xo_pX2rKLDRPxTj_PGrfe8RHybvlaspJLboe-Q7f4YVoSkPZeoLLLkox3A_U1uVnheuUheFP__Bh-Tu2xVN9rdVlbudBp7mW2oktcpZgVDbc_Wj4mZicrHAyaxmxm3eNq92KUWytSJ7BnQm9FTazBobI9VWXcr-NnoXlcz11FsoRu2EATJlVebkWuuc6FGEPLcTjm-03EfZXhVcCGSx32_KnOkXPxdxMcOYC7TZGsDDz4VTyyC2yn1ju_lfEsI-sgRE9-G_B8iJCIG6eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U58VapRbhxSbmjSWMfUcEcoEBIeY_eS9HXd4gI7iQi4734-wtPutr0DQoHfv7ESsXyG_lZeF_ZkjTBPzI6YqPYzY6y0bTAT84Tj9FZfsS78AGMxDISlwYwKD199Tz6Pwfkq2THY3pixhn7_ZIwI0C_UOi7qkHz6YMDqA2TPuiDRtcESErtmy8SA25UTL29GJAdDnjW313zrZozfNfOBKyvHFYq9pjXPFDK3Md4h3y5gGcyvXU8nkjYm6l5G9eUOqCzLE2OO4a7nDlHsD2USXQ2dcaqG2WYELiggylBArDmjK53xiBWX8zNC7i_YCrIMiffmJCQ5Jv338t61Z4aRcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axTDSyDYFJblcZkBRmmEhWHQE2ggO7onow8-E6VvCAV0OGqfbsGTpsas_kSmjA6GUCBQOkkWUIPukvC9PCjELDYFB7lR4F9PhuyZz9o1ToDnoJeQIW3Xpr2q7XvOxXYXU0S7WTSCYJtzWKAL5OC89FD8rE1Ht68fWbR-f_pbQR26Lkmhrg2Ww9a-fMGPp-KSYxk0XaWLNRqBe18BXOpLxnQHKsHqJagEIDFlJA7EyU83JT7wDv9yU4KkGq0fbAB7SLvqsLkngITsozJN05MXUuKH0Gw_PZaxrVtb4wAurvcG9Ba0Q4Jl04Y6875uYVRFdmz-o_EJOo-ea5SMPAn4Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Srd0rnguGiWE6NqWCsS6oDGCiJ48HUweR6LpRa5JTWh_e0t7A3wG2nqCk26V1M-jrjgWXIQc6ugx2rvxjLMT4Kd6TnQ_d8WG4NSp0HVp-vuiqZdJXI87c_fr-gFNZablvs5lXbWYTvncnkNovodh8Wcu4PdAbFT4hAqyXjhU7N9sXQXCiUpnkEB6GnN5Yvvj0ovkULZL8jJh1kK2cqJ1yfh7FS3rn8TpNFSTI4AmAiJj0oDktsxopKBAuCtdccySj7lgGAk220gXMaXf97_IhXrr1UnE9X706A8X7juM7eliFoPYwqu0hMJLzGfL_7MEwJcs8UzHFGa6_OATZtnE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=hIXC2OcGfcxod7t3Y1E0Tv-9QnyXxQozZycMYHayxC51f0bU9R-DT7IlWEOGH_vclNQS3at36yGh85WS1pmx6GlmwR9LpSz7dohZE9G8n6WgNP3zh6iooKutjmS0vM9qTNNUj51GLpeMtZrI4y4CNw7JDU3LW3EZQBlXysIffUpyrV8TrsVSg4RhDtqO1l2KBN23ZAYTFsnn03DTbIQf5wXtcxjdUuwdJsw2WfgHXhLTSR285R7BTJNTurfS15-P-WrWYNu9XUFNVXdhQ2JJ2wyS_qerMs_qV-D5dBZqhpz6zL5cmDgvub0c3aU0NRuZ706PEr0_pJOUpm4aCy_frg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=hIXC2OcGfcxod7t3Y1E0Tv-9QnyXxQozZycMYHayxC51f0bU9R-DT7IlWEOGH_vclNQS3at36yGh85WS1pmx6GlmwR9LpSz7dohZE9G8n6WgNP3zh6iooKutjmS0vM9qTNNUj51GLpeMtZrI4y4CNw7JDU3LW3EZQBlXysIffUpyrV8TrsVSg4RhDtqO1l2KBN23ZAYTFsnn03DTbIQf5wXtcxjdUuwdJsw2WfgHXhLTSR285R7BTJNTurfS15-P-WrWYNu9XUFNVXdhQ2JJ2wyS_qerMs_qV-D5dBZqhpz6zL5cmDgvub0c3aU0NRuZ706PEr0_pJOUpm4aCy_frg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mv9omOnO5FGd1qfiurQdtoSbP4PosJbyc2ZrOAo-aSp-tyo338IHv5y2D7x_yNjEEKZIgIrAMikm9GiaXZASOH2LBYKGnWB0QtGiayG3V_2JQNZ6Vu8Mz_r1DCqKSylhq1F4plyECi8CZTa8a_94oRFh01Kmy7R7fCEXLPYpgde13JEAco4vaRp6XBiOniCmZJyzbkr_43hynH6RhrAa7NXY5G4M4LaLiAo3GpjcXcy2zu0VrL1OWxxFT-3tMMUDYKhzu3r6ZSuxcFIXax0x2RxyeCh5zdTayjsgqzGJBJY1oR1NeN1S2gf4JJpFTwnbbsyqfh26OGquHgDWxiztlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=vprezPCObL5oJFaq7Hr0FBEzqvn592RAoUeo8vqQQodB-4V9U1GN0Q2SPV2N2WpB_hxgCt4YXHNbvE9tyGrZVDcisYhJPPk3sq3fdYD7Wz1vrJ7MKSfObsgYKZk4pAt2YrDClUel4YJrbdX06wkJA9tZyVvOO1OLG0NI6MlKIHm8mx8acllp6jKUQv5MW8UibkFfoedIWrKTWHPSQQ2TetZcEy0PYELRD1vZHMRw_yQndMB8l1Q6uPC45ElSU04-FVqI2E8OuurLOq4kKlIuCUi7SLjRu1bjuGnXgH4JtGG0SRZZXZRY1UKk1zJWwSzf6BF6tihrUea78Wu3AeEdKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=vprezPCObL5oJFaq7Hr0FBEzqvn592RAoUeo8vqQQodB-4V9U1GN0Q2SPV2N2WpB_hxgCt4YXHNbvE9tyGrZVDcisYhJPPk3sq3fdYD7Wz1vrJ7MKSfObsgYKZk4pAt2YrDClUel4YJrbdX06wkJA9tZyVvOO1OLG0NI6MlKIHm8mx8acllp6jKUQv5MW8UibkFfoedIWrKTWHPSQQ2TetZcEy0PYELRD1vZHMRw_yQndMB8l1Q6uPC45ElSU04-FVqI2E8OuurLOq4kKlIuCUi7SLjRu1bjuGnXgH4JtGG0SRZZXZRY1UKk1zJWwSzf6BF6tihrUea78Wu3AeEdKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=cVqE8A6CRWNZnPWQtYG0miCik32cswDTc6-LTOqFbuNf4XPYyUiuyvRbmI6VDuT8Z-TqumDdjXxGNFKeZeaiBLRQSzC_xJXPHlybT43Zr3cPJVOvoWsJwYlnYd_S1E5to--PgLNL79P9eXl3HccXMTrjHD19yen38lJ5AZ-79I0M9MTEaQeJV9XpjmlhQQDnLurLJyUdUXT6F_ry3b4NSI_0mSWP1CwVlmNwsUKBuC6l9GubiK_tTOmedEYTZGFgKwwWNIsQ3-vRJkXncjK7fP_EpsY-U1b1XUHq0XX7S6ge0c7Cj3aoZ0ZLAHqp_ZdsGlWaZ-dGvhhNPPGLeLuyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=cVqE8A6CRWNZnPWQtYG0miCik32cswDTc6-LTOqFbuNf4XPYyUiuyvRbmI6VDuT8Z-TqumDdjXxGNFKeZeaiBLRQSzC_xJXPHlybT43Zr3cPJVOvoWsJwYlnYd_S1E5to--PgLNL79P9eXl3HccXMTrjHD19yen38lJ5AZ-79I0M9MTEaQeJV9XpjmlhQQDnLurLJyUdUXT6F_ry3b4NSI_0mSWP1CwVlmNwsUKBuC6l9GubiK_tTOmedEYTZGFgKwwWNIsQ3-vRJkXncjK7fP_EpsY-U1b1XUHq0XX7S6ge0c7Cj3aoZ0ZLAHqp_ZdsGlWaZ-dGvhhNPPGLeLuyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=lhA7nrPcDxTOoEsJZoLOSDyjG0V_BavsDRsQocSVH0tUWe3Jiex_BJ5SeCEHNGBkAmLf_LXBswWdJar97MWUeE9IJvwUpuy9qSrDXFYgcdol12XIiICxAkBIJ7w-EuoU0-fJxrTK7WItaZDmqRDwzV2G2qWdmenRZBOb74QPi03IdvfDu48Gy3ktGTeaED8-PsNHHs7KmIs2knWF5CVLzJa2tBuQ2Uu5iLkPzHdcXYp5JZOrnywCn6SDTpFTeZ7TMHGUnlkZUC62ixzFOerl0jOcjy5_DXngBF1-WG4hbM90oNnvhFNbe_Sj4cMtwiIPgWMikvBJjlLC75Y4TiBrtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=lhA7nrPcDxTOoEsJZoLOSDyjG0V_BavsDRsQocSVH0tUWe3Jiex_BJ5SeCEHNGBkAmLf_LXBswWdJar97MWUeE9IJvwUpuy9qSrDXFYgcdol12XIiICxAkBIJ7w-EuoU0-fJxrTK7WItaZDmqRDwzV2G2qWdmenRZBOb74QPi03IdvfDu48Gy3ktGTeaED8-PsNHHs7KmIs2knWF5CVLzJa2tBuQ2Uu5iLkPzHdcXYp5JZOrnywCn6SDTpFTeZ7TMHGUnlkZUC62ixzFOerl0jOcjy5_DXngBF1-WG4hbM90oNnvhFNbe_Sj4cMtwiIPgWMikvBJjlLC75Y4TiBrtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=sMo_eT7BlURXZa0dGGbjtSxmTtXx8FYAIacXpYVTr5BsznbgrPHqVc4CSeUdhbdiNTEW-LuuRUoHuNbsGP6_BVwEAwlz4vzlx545Y9K9uYhgTXAp3dZBOf1H0tWrKrqd-wAAndmHQmVXX_74aW9cZtZpMFjPN7e-PNFk_acybdIXIKN4Gx_2VuPDx1iGvgyoOPa4WtSevgwbAIwyLu_re2yqmLqszYPZA4S550RU7Y8BMYULTijkZtnZdNckBZEOOGgPLuIsmmRWrfPplMgn4odO8cHpSptDiY1VZbyaarfHfZN9YN08RLeOYiHjaqusKvc5CytPBHaC2dPDNiwzeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=sMo_eT7BlURXZa0dGGbjtSxmTtXx8FYAIacXpYVTr5BsznbgrPHqVc4CSeUdhbdiNTEW-LuuRUoHuNbsGP6_BVwEAwlz4vzlx545Y9K9uYhgTXAp3dZBOf1H0tWrKrqd-wAAndmHQmVXX_74aW9cZtZpMFjPN7e-PNFk_acybdIXIKN4Gx_2VuPDx1iGvgyoOPa4WtSevgwbAIwyLu_re2yqmLqszYPZA4S550RU7Y8BMYULTijkZtnZdNckBZEOOGgPLuIsmmRWrfPplMgn4odO8cHpSptDiY1VZbyaarfHfZN9YN08RLeOYiHjaqusKvc5CytPBHaC2dPDNiwzeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=qbOxpKDZOX842vWBaGUp6bZHqBZKKXHZs5GmJEd0NdyTI-52ped03F9rJFMhxyP1wBRQ_b06MWSd7B1nWQ7XPoTjLuFf86xqnd3E9wJ9R4tmCu-_5fovq6f9EnAOIlSwRST58mH6gwrTzs3nuV_JCVPqAcUOl9Ml2Il-fSA2o2aWCgGFlSuI0XeDTnY9jlx8ZWunHR4D6oQNIq3MwJa-wkSsqi-G15nBDLGvVVniRCKMuPf6xHQDv7bRMZTg59JPaiL30dzJq1AFxbT30OAiIFF7I18uCJn79ev8alaGd_vZ-oGY6e0_VUrgHs7qyjYeXTg7qksiBA2fXoh3ZYyqug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=qbOxpKDZOX842vWBaGUp6bZHqBZKKXHZs5GmJEd0NdyTI-52ped03F9rJFMhxyP1wBRQ_b06MWSd7B1nWQ7XPoTjLuFf86xqnd3E9wJ9R4tmCu-_5fovq6f9EnAOIlSwRST58mH6gwrTzs3nuV_JCVPqAcUOl9Ml2Il-fSA2o2aWCgGFlSuI0XeDTnY9jlx8ZWunHR4D6oQNIq3MwJa-wkSsqi-G15nBDLGvVVniRCKMuPf6xHQDv7bRMZTg59JPaiL30dzJq1AFxbT30OAiIFF7I18uCJn79ev8alaGd_vZ-oGY6e0_VUrgHs7qyjYeXTg7qksiBA2fXoh3ZYyqug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkV3QpLfAov9WZp2rvQZA2II73iO2OSWEe9pLE-qxCVeJyxcK_Mvu5D6faG0xW6w-NuA2UzcK6W-M17ECNTpV-nfSSw-XNpEnPoE7HzJhfpR-P7y-JeRBvOO3JcK6nOfasJoos4S4p56nai1SV-oTxjETVCEMFbEJPWWx-1Omk8hvcnZvuQval-rUA_rQUAE7dZczJexrV0Ta6iLS1MoKD-uaDYgN7zxiMAqe-RkAIPuXuSfTN8poI6Y4wIoLD2EwTg-jCwlFUgdxCX050KdqdD4rQRlQtLXKNHzmJ3tVzgGmRcsJayDMN8xKokXRRS4jEyVGYTAJPpNLkKgvMUXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSYz4utyBnktNglsHTBh1tqX63s4kUVYWHXyI_OMMXX5yteoawHajp2Om49TeESzen_iI7nJ1L4N0iNzJ-NOraBoQzVngqUrQ4y_MsTo2bDK8UIlHR8QfwfXuJjduf6gUywvZ_G_X7gVOXqKOMXFT-lRf0COcZ-ctxwiHcD68HurdUhz4TUWM4z87YLgMKQbbnMUCeCaxk627kjFqX6twXX1wnwKUkNGWKSBZZM9bHOp6RgBcux8g80PzrOFRLJvZBHn33OXnniRGFNUBk_pZAScyK42cM3H-Hd_WIvfOthzUdwVc0bIluSlCSB2Lu1LcZiUxUw4MEOHndlRw00oLzQqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSYz4utyBnktNglsHTBh1tqX63s4kUVYWHXyI_OMMXX5yteoawHajp2Om49TeESzen_iI7nJ1L4N0iNzJ-NOraBoQzVngqUrQ4y_MsTo2bDK8UIlHR8QfwfXuJjduf6gUywvZ_G_X7gVOXqKOMXFT-lRf0COcZ-ctxwiHcD68HurdUhz4TUWM4z87YLgMKQbbnMUCeCaxk627kjFqX6twXX1wnwKUkNGWKSBZZM9bHOp6RgBcux8g80PzrOFRLJvZBHn33OXnniRGFNUBk_pZAScyK42cM3H-Hd_WIvfOthzUdwVc0bIluSlCSB2Lu1LcZiUxUw4MEOHndlRw00oLzQqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=mu0yycKRjQwXLxU23kdqoHtbqSwerb9irq_YuCSumw8D3-tG2hKlSZ_COQsnfzxdo07-15T5oVNXuwUoXpwAnpVc_M2SRYSGlaKGsGuYrztyXyupvapcz4wBIcgeCIFjuVQHImE7s8uncf6CbYKncKxBt-jG7vFMmc495P_DMBnG29wg9TrQubIgki9EWxH0WGcNV-QeX2FUZGeCOi6pLDZrC0OgVAxBqirOhoR_vE7KVyJFWWU5PW7vtnUS3HByj_8PmtOqV8XmGpuqjZMUJ1nygeKHWmSR7AW-eyuIHhqzjMKUpW-wIt38Mb_MO16wMwP5XKxZrA1ctPb25cnDpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=mu0yycKRjQwXLxU23kdqoHtbqSwerb9irq_YuCSumw8D3-tG2hKlSZ_COQsnfzxdo07-15T5oVNXuwUoXpwAnpVc_M2SRYSGlaKGsGuYrztyXyupvapcz4wBIcgeCIFjuVQHImE7s8uncf6CbYKncKxBt-jG7vFMmc495P_DMBnG29wg9TrQubIgki9EWxH0WGcNV-QeX2FUZGeCOi6pLDZrC0OgVAxBqirOhoR_vE7KVyJFWWU5PW7vtnUS3HByj_8PmtOqV8XmGpuqjZMUJ1nygeKHWmSR7AW-eyuIHhqzjMKUpW-wIt38Mb_MO16wMwP5XKxZrA1ctPb25cnDpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=LYVJveXwDtGQwsnC7xB_b0Vv2xJCzwsian9inH8epV2BpPW62fZInT0V-unvtvMyj0nBrKl6_VcWdo44R-SvBdp7aa4b0PgDI4qDTc0uomzWwsvnXgAPKyplo_GkgF4_HXhPl-St0AfKdF6L_ipzcmvbBR3utS2pscM9eAb7yjOdpwjYvo9WvbmPSZ_GVqGwshay2-bBNygtx7zx5VSnJjdwuIo9ZSByj0He-MHD-5N0x9YGacCjy5960z2SI1KHSUuMxBQtIqelaGEkeU2dJc81HY4RD8yed2IkadTy4EgYI_iERCtUnrbnilcw3sAEKZ7CYHbsPWz6w8Lfrmt1Er3V3i3uGPl_Un9sFXEx5jjxJWwGSXcOHLuOnH5YIH2IcUXSbJ1n4CVFQFflqcLwRhKLSBIUmRdfo6_TuqKT5Iji0alFva-XrkfucXROTovcQ4MISVw71kYTZaC9EvVn2fENEwfA6Vvbbo2BER6ghy13kOyGYaGPZMvgNLN8QqS4ACSLwLXFO1qfFyHStFDJfcGb9ClFzGEhwGclkDR0t5V1RGyH6cGpj-t3T2vct_an8F-wxi0OzAvWx99VKQt1k47V7_3ZYG9EPpX__CGdG1cZNzi12e1OPBgCNf2MebDoTq6xNWoyhKpe1Qac5vgo4S8Ll1vTim41COvg0cFA-WE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=LYVJveXwDtGQwsnC7xB_b0Vv2xJCzwsian9inH8epV2BpPW62fZInT0V-unvtvMyj0nBrKl6_VcWdo44R-SvBdp7aa4b0PgDI4qDTc0uomzWwsvnXgAPKyplo_GkgF4_HXhPl-St0AfKdF6L_ipzcmvbBR3utS2pscM9eAb7yjOdpwjYvo9WvbmPSZ_GVqGwshay2-bBNygtx7zx5VSnJjdwuIo9ZSByj0He-MHD-5N0x9YGacCjy5960z2SI1KHSUuMxBQtIqelaGEkeU2dJc81HY4RD8yed2IkadTy4EgYI_iERCtUnrbnilcw3sAEKZ7CYHbsPWz6w8Lfrmt1Er3V3i3uGPl_Un9sFXEx5jjxJWwGSXcOHLuOnH5YIH2IcUXSbJ1n4CVFQFflqcLwRhKLSBIUmRdfo6_TuqKT5Iji0alFva-XrkfucXROTovcQ4MISVw71kYTZaC9EvVn2fENEwfA6Vvbbo2BER6ghy13kOyGYaGPZMvgNLN8QqS4ACSLwLXFO1qfFyHStFDJfcGb9ClFzGEhwGclkDR0t5V1RGyH6cGpj-t3T2vct_an8F-wxi0OzAvWx99VKQt1k47V7_3ZYG9EPpX__CGdG1cZNzi12e1OPBgCNf2MebDoTq6xNWoyhKpe1Qac5vgo4S8Ll1vTim41COvg0cFA-WE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=uBpyyB2mv5VdbgL_GUa1-dDNWXkQCEjgqBNQRwzd0c3F3_Vw-J6mI7cCPZJmFUy32rwjWuC2brW6hkcxjmnkLMcmH6V7F7_0yE8E7l9aMLH2mQ3HN9DAO823TafoJB5nlehgZ8J3oZLwY4fUozciuB8AoAp7ZqNjMURNpNto6qYDGL98Yn5e5dmwRQ-3fuXt7Ij9ERp28HlkD_D7BaTi36VwDZi7ZkpEl5kScChq_Fm2ZIWxadsDkM0-e53NNEJBpr8bqnc_HuudCuvCctZ8-Gjw2Qd2YGVHXuMX5KR5ZbKlwh_UFOMWv437J9ZRX181tNcI1H_-bEMHUbdJeWvrRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=uBpyyB2mv5VdbgL_GUa1-dDNWXkQCEjgqBNQRwzd0c3F3_Vw-J6mI7cCPZJmFUy32rwjWuC2brW6hkcxjmnkLMcmH6V7F7_0yE8E7l9aMLH2mQ3HN9DAO823TafoJB5nlehgZ8J3oZLwY4fUozciuB8AoAp7ZqNjMURNpNto6qYDGL98Yn5e5dmwRQ-3fuXt7Ij9ERp28HlkD_D7BaTi36VwDZi7ZkpEl5kScChq_Fm2ZIWxadsDkM0-e53NNEJBpr8bqnc_HuudCuvCctZ8-Gjw2Qd2YGVHXuMX5KR5ZbKlwh_UFOMWv437J9ZRX181tNcI1H_-bEMHUbdJeWvrRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=sAw-hiyms_RpwgscXYRYVKvhwwJSRb72v40t1Qzeeoz59m-CwMJmdFISMoCoxXwUf7k4c-ry1cfZ5O02K9_3WzrdaXC1sbvs65DodOi_k1W5UyLAvvG1pJIhMPdWnBpfD4-kRvjmqQHF9f9U_v6XxkOux8a1ohrX1U6HVcYGbCGMQ_qbnqiy17R6EH4hyHWb0s1Ki-kcUtic9BOheo7bhD0X_wISmLZHsE6gFWHX8ZjPcX4odVLDcygWn4yhwigrf5B-Y7uJe3uEF5Bc1FXd3aQ6xqpTKkJxxmrpgSb5W504Bm48DwIuhHSa_sA0cQ1erAP8tgATSfcLtIUmW2cnag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=sAw-hiyms_RpwgscXYRYVKvhwwJSRb72v40t1Qzeeoz59m-CwMJmdFISMoCoxXwUf7k4c-ry1cfZ5O02K9_3WzrdaXC1sbvs65DodOi_k1W5UyLAvvG1pJIhMPdWnBpfD4-kRvjmqQHF9f9U_v6XxkOux8a1ohrX1U6HVcYGbCGMQ_qbnqiy17R6EH4hyHWb0s1Ki-kcUtic9BOheo7bhD0X_wISmLZHsE6gFWHX8ZjPcX4odVLDcygWn4yhwigrf5B-Y7uJe3uEF5Bc1FXd3aQ6xqpTKkJxxmrpgSb5W504Bm48DwIuhHSa_sA0cQ1erAP8tgATSfcLtIUmW2cnag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=a-SdH5IHFIWhRt9Z3X92Jl1WgyAe9gs46vRXKs3TM0WqZqhjCz6bVc_Zj8THc2RHXfMFYD80ksB5EyD3C_-6dn8lpnB7Nr5XKmW2ZY6gYC8DLSEDLT_RtiUN-JevTy4bPkVMddoMq3sfTC9VEp0P200YRZeEt2ak5ylHAO1lzv2GRnjz6rGvEbbVZGwy8ECPV2bafX9SYTUJcTU7xsMQXSwq3dqJEpFMgC_gX8gsBG2QAF-_lgzSwPc7NaOWVK89Edkvxs38fC6dGCZ5rO7KGuhK_M4stLsv-74XwLp4fo2csc1igSYeYB8QXEQzxR3LLFAgsm2utw-bWVkf-Zn5SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=a-SdH5IHFIWhRt9Z3X92Jl1WgyAe9gs46vRXKs3TM0WqZqhjCz6bVc_Zj8THc2RHXfMFYD80ksB5EyD3C_-6dn8lpnB7Nr5XKmW2ZY6gYC8DLSEDLT_RtiUN-JevTy4bPkVMddoMq3sfTC9VEp0P200YRZeEt2ak5ylHAO1lzv2GRnjz6rGvEbbVZGwy8ECPV2bafX9SYTUJcTU7xsMQXSwq3dqJEpFMgC_gX8gsBG2QAF-_lgzSwPc7NaOWVK89Edkvxs38fC6dGCZ5rO7KGuhK_M4stLsv-74XwLp4fo2csc1igSYeYB8QXEQzxR3LLFAgsm2utw-bWVkf-Zn5SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf53-7rdCJwtedmoe20Ncymv7OW2Zl1Xu52qlWmir_AhkrtZuKsPEMuZerCNHIk0QPzKZ4aZ_ZG90J7jTV4Hx1AHASPrNuZSPiv4h2_3-Ikp681lZSp8ZRYfQklY87Km7_NUJLklmOv-DV8t43mws5ITJxuSJJbWhpQ9u5tB9AKs57q333Temzmc0msrsfPC8KYY2uDUOcYNxUAekMGsoJVylJQMiQoWrtP6pl2_8QSaLl0N2AR_O4JE2zjC_Na-RK0uc_Xa-3fAI5u1TztxU_YLeR8_83AisRMJIZAW0_cYmwsZa9giPTqoHL0uKLQeuioy9kzBZOQBn_N-czmw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/higdUGhUPGUIgu6kHHNqmQ-dwBttrSg-LdXq1E7aKN48HfUzMVQKfrrwwOZTw7prv6oQQgIhWgldgqEwgEst884CPOVViTfVktwkk0yJy8U7NJw_wbWxuaNHLHuybypi-tW2qLcdto5Xx7ca7vaFArDNzgKP70fiB2BIMKoAfeYZC-TvSKO-YE-FWyrzfHRQhh2cq25uTgYDE10C85P9yZYLhGyGvrweADssnBiebBM7wwQHzQBwFo2kg2or08g8ry7MeCDVlieYQPYwS8uetmJmxTQNPW5Lb2UgNBl4Oj_3DbFHb7KOVYNoVmDUtATf8D6ylf3z5B_dm2cExxbnUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeB1JX7cXFd9aEUzhcxo2Twyvy8NrgVChWw58OW9dEPA6zBxLCK7xUBIWtBURzdJRSNeFHb4c0v9rvIcuThN6gH2pVEsdfBIzbiIW0SeCVrXfYrTAcdNQgdmN38U8mt0QYal2tAr_sgBrK2eUAwAaqcPEBdzAv0FOdsA7t3l5QpCi08iAp_TisOwe7vPHJThJxxfehvWmYqBkI6-IqphBEjwZu6wO8rHXUQb9CDaCN6p2XtTita2k7FR6H9pQYlkGqUdLwwVzaLLPApD88_gGVzmd0r57GV-bOPHA5iLACS7Ny9-eY8EpycDWidgJpZJgJ4c0_8smzw1-fDN0gKF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-uDGS3W_WLnMCTK7Kf5mglfVOI9RAO7bBDoQ7QTtuqgbIR9ayjLONDkKt_bM2RcOa0TT_GL72IfzN0Lplw3kMtEkhsGzzfUV7IxA9xrpbI0Nf3XUsqDca5k0kwitWKMMeW4q3tczoK4oQjAYehbvYH76iq3s5RFE9X73tZxVMft0erme-PpWO20mVzKFiuqsYbviejP5lATETAH2V7HIkgE88IWpbsFFxvmDEdh5qE-2Z0Omcl2pOM5okxFz5MFtjnWrGJkV4XnmWVi_RrTKB2BVmYpWUwJtcLr1PQBxMRjXf-pdbFmcYBfRMmgNYTEK8TGnwVdgIvW5KEeZit_dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibfXItIVeX7ji_vjul5GUoMV4EIgxqmaCozUx4v66m5jF__FLZ0b2KR_-V6P3PB5oStb69Bo1Zk0Jkvz_WtCMNf9cQScU79nb6sh84B0cV1FntjwXm6j45k_m5V-IoKaIcHB20KU4yhHftAvvNP9ix0KaJr8b_dZKlU60hNZDS5OmynkfiqV9AkGnWGNcoAXr4qy7pwCb8I73HZomkMlKqvaj_Qn5A_e9XGLjsY0H2yFfOZBHmWCDy2BuhgjLmBoPHaZgdj5EUiHUkqvUcopvbOghcwjEUdbYdhaGNH9nE4H93OYeq4_p1SGqJsXzth3XpXeRN0Ef_ZLtWg2zNRlGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJVEPOhd-kqkLh2mQYLre2-dU3QZiMhIyOceBFwXLXB0cAdJ_ahM1PEnxfoaaxySR4EUFX-9h6H6eWcC7RDh_L2jv75I2dHD5Kzp0xDd-L3TJLyXQNKugRLmfSff7B-8w-rK5dJDZB38-X6z30TqSdf6K-Pjn3HxR3uNe2a9nONch_10-GCdcaQawpbHh5jSTlpODXrgi7Kvrmn2yoTq9ZNE7WPrzfhlMw1MeVxOKgvDD8jPxS93GXs3LCA55cqwK0NPyHRVIXNy4gJvqRwn_SY1roo4ebScZZXcLoCE3BT-EgLAXkoEHj0GuqG87eumVWMxpUC_Wrd872_xzsC8tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=f_2hZ7KDW8QWX9Xqe3032M0xS2HbarbM0JQXjJnThMYfOheixQRX_THZVqfpmms9jggWkzlkGgbQ6S4n8Ii_Pc2-ErwebF4LJ3ctk8tJKCsO4GN4RTApTY3qyI0Ko8nOof3E7HdqFK47hGbIm2LOXsTdzmHYeu2mPorVSWXi4SkNUOfjCZPONKw3fFSMnCVidvTzCQyBz0IzhrU8UZAJFfzubnSZ96mv8QuOgt81hJleRDNgh975iUzoOhdss3SSkp33PaQVTlMnP0jXRhW32_8dpzbjItsqVbf3LpFJ4owIbG3qUGaCeDKI7F5sLaIDZcFEMrRpPzGZB7IFEbgtzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=f_2hZ7KDW8QWX9Xqe3032M0xS2HbarbM0JQXjJnThMYfOheixQRX_THZVqfpmms9jggWkzlkGgbQ6S4n8Ii_Pc2-ErwebF4LJ3ctk8tJKCsO4GN4RTApTY3qyI0Ko8nOof3E7HdqFK47hGbIm2LOXsTdzmHYeu2mPorVSWXi4SkNUOfjCZPONKw3fFSMnCVidvTzCQyBz0IzhrU8UZAJFfzubnSZ96mv8QuOgt81hJleRDNgh975iUzoOhdss3SSkp33PaQVTlMnP0jXRhW32_8dpzbjItsqVbf3LpFJ4owIbG3qUGaCeDKI7F5sLaIDZcFEMrRpPzGZB7IFEbgtzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=qx0r7oheLT4f5xtw89JSWeE2sYA5aEoxlfHmuY65nIuL_V03x3bYzstDAFM4paZTAnjMyUNTggSg5GsZ_yKSY5B7bRv4aGmSXCuw0xXbVVQ7XsrG17DpzxwhIQHJo271ppJE2uZI2fUd50j1eWHQyoonvlaE3jxm_R2Ox_ZguC-LleQquAhj6CVCJ7ovemd_a1il-AB5hyTGRQjH_N3nYFUpEX2Rmq9Aulgaqu1oh5zwSmiErFJuQYq9WEcNC37NaER9tflOOqaO6D_2bwWwXHGwB7Mde8ygh-B-1x81hH4mXjygCuPvtCkURZ7HmOpvcetNRTSgj4RAd19N18aFNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=qx0r7oheLT4f5xtw89JSWeE2sYA5aEoxlfHmuY65nIuL_V03x3bYzstDAFM4paZTAnjMyUNTggSg5GsZ_yKSY5B7bRv4aGmSXCuw0xXbVVQ7XsrG17DpzxwhIQHJo271ppJE2uZI2fUd50j1eWHQyoonvlaE3jxm_R2Ox_ZguC-LleQquAhj6CVCJ7ovemd_a1il-AB5hyTGRQjH_N3nYFUpEX2Rmq9Aulgaqu1oh5zwSmiErFJuQYq9WEcNC37NaER9tflOOqaO6D_2bwWwXHGwB7Mde8ygh-B-1x81hH4mXjygCuPvtCkURZ7HmOpvcetNRTSgj4RAd19N18aFNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcqFuxdKEaulf7Bb_DgOI1c7-vVUjRbstaNUZer6fwz8-zNqeAdKqPq147EUOQB6C7s3Dx1bAwj6651AW6bQTf_EkA-1NySvFUr9HDuNvMCgAo8VXLKwC9lymxDX3FmulSLqyVHB1bLn77w37weKyuK-_dfcjLaapyLqtQjm1qae8yWLjrAieRsOoe3X64KrH8lSFVQ6zOzFAuqO9X7cEUioYEr7JKRKolgMztqqkRzw_VBG6k48JrX4ArnLwkFicmEx2nEBbmnCZECh4U3EWxnwXZGqNVhkV1LYB2O8P0GQMXlNBku5ltIAKOdxNSIUFUiyOJBVRMLlzPTgo63F-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDwFDCGyjDwx-tP_hfwMx3tMzleCvXw5tbYtGiKKidfd7lt0wVlofLQtkK66CD01UqhUQ8SdA-XfdUeI9d1NPmPGmTmVhZO4Xqogq-Ku486p1CsVJY4-Wqdfa4GCMjcD95RGdkn1n55Bl13qrA8Fc0FsNDwLxAoK2-3Dw5z9a1l-lPhTL5LnQv6wOrq_JemjYPG3Euj5R1WiT-Vvitgrm3sHdFXeMQ9AXDEPKLOsyvYlrIO8TM9SyRmr1tdKUbUuT24l5fHQ2M6GZ4Oo3qIiJ3ldmSVaCVSi_GFuLhjdTwLQeGbJtA_s6tqGMGOIh0iiteGuqIb5QXCrP1ZOC_2xOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=fZ52vGHDfGTtdDOPiYVr6wvJdEtO9n0I_T7_sjdaTdM9ooBeXgMSJGoxMPx9B_gOJv4jZyezRHoJPpa5XilUTPH4FxxXU-PpNeW5JwFV10ngInF0xe6746Rtqp9dzBbzWb9rBs5PoCH0R0MJ8kCACmh7Bo_AHQsVULQkeKFOCjs5uwEoRae8fTRJejH3PaMtPtADvTeZVJJd0ty7Icu2uLSat1G6xElX0yxNLDXgnmQysjryP7ctP8J66EO-DBoxPgROXCxIXSniEPelHj6MO_1SwLR8Srye0K9YA2YcutDxaqWtkwakEoWTQaGQ_FPXKt5dlxVo3TtFuozbTcZnWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=fZ52vGHDfGTtdDOPiYVr6wvJdEtO9n0I_T7_sjdaTdM9ooBeXgMSJGoxMPx9B_gOJv4jZyezRHoJPpa5XilUTPH4FxxXU-PpNeW5JwFV10ngInF0xe6746Rtqp9dzBbzWb9rBs5PoCH0R0MJ8kCACmh7Bo_AHQsVULQkeKFOCjs5uwEoRae8fTRJejH3PaMtPtADvTeZVJJd0ty7Icu2uLSat1G6xElX0yxNLDXgnmQysjryP7ctP8J66EO-DBoxPgROXCxIXSniEPelHj6MO_1SwLR8Srye0K9YA2YcutDxaqWtkwakEoWTQaGQ_FPXKt5dlxVo3TtFuozbTcZnWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=LFpDWsrdvEHrx2tAvP9enyBZ3T3eMmTsILEPl0v_N64Y_U7K7nt-89BxSjRDgMRc7Wa8AXPXZWLKdIbkf1FaVk3XIRm7u8BLuP_6DC-nVDNk2QKIPeDC1Y6ci52fcuaj81MkFeUhfQMWjkx33XB6bMT7HeegN-krSLNl5R7rvykC9skDKOGf8zwa6XxMkYwXJ73Pq8BjMmkgpyKflNIBIaRnEMfdHNSD4o-LQVv_akG5y9u7sZm6AMgaYNKT2ROSmrxf7daEVo8GFLY3iLvwX07QaoyZfxLA8fVEu1SS0xsdV2q0t3CHLCbYEFeOHZh6scXi63DdRtKsSK6IS8GtgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=LFpDWsrdvEHrx2tAvP9enyBZ3T3eMmTsILEPl0v_N64Y_U7K7nt-89BxSjRDgMRc7Wa8AXPXZWLKdIbkf1FaVk3XIRm7u8BLuP_6DC-nVDNk2QKIPeDC1Y6ci52fcuaj81MkFeUhfQMWjkx33XB6bMT7HeegN-krSLNl5R7rvykC9skDKOGf8zwa6XxMkYwXJ73Pq8BjMmkgpyKflNIBIaRnEMfdHNSD4o-LQVv_akG5y9u7sZm6AMgaYNKT2ROSmrxf7daEVo8GFLY3iLvwX07QaoyZfxLA8fVEu1SS0xsdV2q0t3CHLCbYEFeOHZh6scXi63DdRtKsSK6IS8GtgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=jl0Ra1rS7n27BEh_ibP_yYbDP7FBj9qYbp0OJfXKTYvZNqxrrsGgZDwRfLNFYdQNvVy7vlDvjPS2oflErjaEsgLAEhAzjEW7fkr3A9pigdonFpHRFVMTtp-e_edK52M4FNhpApJ3pLWi9qYh2BNGrh4lIodB5ESnlYeOIFLMG2JLUP2CGqpzswmRdEX_OSWehVwLp5VtAI6f3btPb1TvIVaXnCBowaRxviGvIbbd_HBC712cJ2-s0HCj_zkvCmaYafDv0xL0RuIZ48LQNADAGyjRHGTYBzNeGMDXiNuy_V8i2HmH9z98fDqFGWX1ZS7D_4Gp9GhagyfW21Pt1OrzJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=jl0Ra1rS7n27BEh_ibP_yYbDP7FBj9qYbp0OJfXKTYvZNqxrrsGgZDwRfLNFYdQNvVy7vlDvjPS2oflErjaEsgLAEhAzjEW7fkr3A9pigdonFpHRFVMTtp-e_edK52M4FNhpApJ3pLWi9qYh2BNGrh4lIodB5ESnlYeOIFLMG2JLUP2CGqpzswmRdEX_OSWehVwLp5VtAI6f3btPb1TvIVaXnCBowaRxviGvIbbd_HBC712cJ2-s0HCj_zkvCmaYafDv0xL0RuIZ48LQNADAGyjRHGTYBzNeGMDXiNuy_V8i2HmH9z98fDqFGWX1ZS7D_4Gp9GhagyfW21Pt1OrzJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=rXoLwisLam2p9to-ONbYkC2OgYJayLJmgUI1RFusm2hAxRJnxP-PYZV3pZbjQzf1e30YY4OHhTiWONGTW16XKBQEsZPXxi-IxhNTiABENMID-Iu_-uSHpN9_xfrTVvLugfSUEjqlk8x3bl9hGLPggY1ldclcRlLKqm_Kzfpl1rv68AlM1jO2xRPbDr5eMFWwY1rVc4Q0RVbv4oB1KZuD-upNgPCi0nRkRVQQxY8IKtid-xFlRmFa9VK4FcZ8QV-uvTAwCifJA8iSbViaob8PbPhqaBWP2W_km3pJH0JM1w2YPlBlQ2Y6yEvi3G-VY_0zc56V6tHoULVJ0rNrtCciTU4fw2Z5w0bk41xzYVWNrz_RZAjdX5eBoEKQRR89tznVf9x9wHbmEoIf06f5qkizeI8c7tvYQ5aktKXJpqvm9nqCdWffHtpixgQNk2rt5r3wFgiikmkHt36Y8IgkPhdTMVvzZsG9Jz3MsCZdmaNdqKBSbr5lNbi4bKvIbbzVEG8xDArCneqi7LtW2cGm1anW8JBONUb1FnTK6c8cZ-KEcGmbgVpmf2Tmg27FdaaJGSI7eVU5jV5Nf3wq61DY5F0cngXxVSqeD5mjetdoDpdt2fJVWa3ST6JlUgoDsLBb4r1YEyp_fA7-IATtGtrCi8sKaQnLIIaqnu7JH86BynDA7qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=rXoLwisLam2p9to-ONbYkC2OgYJayLJmgUI1RFusm2hAxRJnxP-PYZV3pZbjQzf1e30YY4OHhTiWONGTW16XKBQEsZPXxi-IxhNTiABENMID-Iu_-uSHpN9_xfrTVvLugfSUEjqlk8x3bl9hGLPggY1ldclcRlLKqm_Kzfpl1rv68AlM1jO2xRPbDr5eMFWwY1rVc4Q0RVbv4oB1KZuD-upNgPCi0nRkRVQQxY8IKtid-xFlRmFa9VK4FcZ8QV-uvTAwCifJA8iSbViaob8PbPhqaBWP2W_km3pJH0JM1w2YPlBlQ2Y6yEvi3G-VY_0zc56V6tHoULVJ0rNrtCciTU4fw2Z5w0bk41xzYVWNrz_RZAjdX5eBoEKQRR89tznVf9x9wHbmEoIf06f5qkizeI8c7tvYQ5aktKXJpqvm9nqCdWffHtpixgQNk2rt5r3wFgiikmkHt36Y8IgkPhdTMVvzZsG9Jz3MsCZdmaNdqKBSbr5lNbi4bKvIbbzVEG8xDArCneqi7LtW2cGm1anW8JBONUb1FnTK6c8cZ-KEcGmbgVpmf2Tmg27FdaaJGSI7eVU5jV5Nf3wq61DY5F0cngXxVSqeD5mjetdoDpdt2fJVWa3ST6JlUgoDsLBb4r1YEyp_fA7-IATtGtrCi8sKaQnLIIaqnu7JH86BynDA7qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=WhIwF3XkzvGr616luNer7fUsMfXuPbvaSoneOmRAgxKlFxjtJyPdSgWY8DEJ1u49IQW4462zTQaa6HH3mBHihPu9M6c1kPbK3VbyYqqZH-9axPtAwNM66n63dMCb08jR5pDx17Jxhi_ot3CDjwiAZ79nZXwhwbf9zsnpXLafqq5Rz8wqx0JBaT47slY5qettzgVRyIxLbcKwBX8h45AvTSx_xMl416X_iN_aBPHVoH0jrCwR4XucXHkcK9vD52GCtC4yBdNpP297OKDMiNsICh5D_l8vgHFFr9dtOgol2DLrZHISl3eLd-fMd5HYSQ0vJNrqLhsN2v3IkAdKxW5h6JJuihkZY5OLofbcF0kcBNN6R8oKCJxclj-Yo3vjkXkYMqXDqtUeJZf8OP0l6uui21185PRj0nBXHeFTxjvOW7p7Shg3-l3pCixWugE9KNW46eZ3R2HnNLZWNX9WMPJ7nGZTd9Gq5mBTLccOBd5PJjF4hylDBgXsrK3g88It3i0HwEWKZokqFWwLLaUEtOg2wfOJzTFtI7_Eqvi0M8MTcFWmCPs7Dm_IkC3zEFuHOMWeAjan5xig6XxCd6wqR6ZSODdp-dsn-mCBtiPktzWRP0TejGdoB3D2cIP76hkPOl5FuBLG2tv1dRTW2cPbxy7qkK_PL2x9uIwkt-QbXckPgx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=WhIwF3XkzvGr616luNer7fUsMfXuPbvaSoneOmRAgxKlFxjtJyPdSgWY8DEJ1u49IQW4462zTQaa6HH3mBHihPu9M6c1kPbK3VbyYqqZH-9axPtAwNM66n63dMCb08jR5pDx17Jxhi_ot3CDjwiAZ79nZXwhwbf9zsnpXLafqq5Rz8wqx0JBaT47slY5qettzgVRyIxLbcKwBX8h45AvTSx_xMl416X_iN_aBPHVoH0jrCwR4XucXHkcK9vD52GCtC4yBdNpP297OKDMiNsICh5D_l8vgHFFr9dtOgol2DLrZHISl3eLd-fMd5HYSQ0vJNrqLhsN2v3IkAdKxW5h6JJuihkZY5OLofbcF0kcBNN6R8oKCJxclj-Yo3vjkXkYMqXDqtUeJZf8OP0l6uui21185PRj0nBXHeFTxjvOW7p7Shg3-l3pCixWugE9KNW46eZ3R2HnNLZWNX9WMPJ7nGZTd9Gq5mBTLccOBd5PJjF4hylDBgXsrK3g88It3i0HwEWKZokqFWwLLaUEtOg2wfOJzTFtI7_Eqvi0M8MTcFWmCPs7Dm_IkC3zEFuHOMWeAjan5xig6XxCd6wqR6ZSODdp-dsn-mCBtiPktzWRP0TejGdoB3D2cIP76hkPOl5FuBLG2tv1dRTW2cPbxy7qkK_PL2x9uIwkt-QbXckPgx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=g2RDBfKJwYrFLlooj7WzRwA8XBMuk0KYB94NtmhTOYjtchct_vqJ9O7doZV6VmPI5kx-pqVWLIAblJ4itT47vtVbf-_QN9RciS_g5CZoHM5k3uv1lHT5d0l3q1pBRNldWu5J8k2t_IzE-X6ByN57oyxZuPmko3z0_YB1u10ENGpPznUhJJ88d1gd2FUGWxhbwmOYluxFgnAO7TX6LLMxns8C_GpTHuZAK8ui7HQAdEnARTaOaP-n1Hrh32K4xKm9dJRZIjchZUDw4G_OEl1l4Mc90NUqAXXMiU63_MhgJV6cO3e0Rp5-m-zMMtGSuA9cevh3WtYTcbkyy9Q7iQiJvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=g2RDBfKJwYrFLlooj7WzRwA8XBMuk0KYB94NtmhTOYjtchct_vqJ9O7doZV6VmPI5kx-pqVWLIAblJ4itT47vtVbf-_QN9RciS_g5CZoHM5k3uv1lHT5d0l3q1pBRNldWu5J8k2t_IzE-X6ByN57oyxZuPmko3z0_YB1u10ENGpPznUhJJ88d1gd2FUGWxhbwmOYluxFgnAO7TX6LLMxns8C_GpTHuZAK8ui7HQAdEnARTaOaP-n1Hrh32K4xKm9dJRZIjchZUDw4G_OEl1l4Mc90NUqAXXMiU63_MhgJV6cO3e0Rp5-m-zMMtGSuA9cevh3WtYTcbkyy9Q7iQiJvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta7-E0Cmrrxyb6d9717W4UG7veAhhBzsiuyTliUdX89EXQIj6osRdSe0jL21jpnysf8yc6AY0Up2UA2Ot6yeV8HOcNg34ifLOeLDYjjft1WyosXJRL4koVuf9Y7BA-fmxh_fXdd3aUW953h1v2qh4EnZHkNOP8dNyJtpYyuxD4sBVDiuVzu3fBI4KqDs9hACtKLV7oXnRShm2J5RsWvJNul6iVei7ShzykZa5Rk0y8Ts8e6V6K84UrrWlzTd2yzqSwv2_wYwIrInvYfEbo8wcL6zNWa84zjUFdseV9hQZdQUh90QW5g2Q9uMMOhv6Fon9suIiPW-C1FnYnB9NfRkWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsAEGqIjSlJFMTxf7ckMirz1YXgrhba9N7y3qHRW6azb6WV1nLq87_FIXVoim_Ly2eB1EKS2j0gvx91kT90Tl6_uLMM2INPzjpw9e-TGMXOmcTNXp3jAjEhlytDoicLf8Ygs9FZG2KL6lX7Af5pcbPHeqxvxhD91yYNDbrTpanccAw-rt3wUySXQhPZg4MfGF8_IyjCTQNzS1HsfzClDwDVrtXJyHznnWnp1GITQ53PTVOjQ2xXBmdRwcX7cgAB8f2YnGFCIEqpDZlFYPc8zW1jky_zgBZwPCjaSDDx_6cZaoH3KsFAIBTHVqJusijcr5Cgnmyqb7UJc2olBe3q-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=s7nBVT6MOUKqeRVx6yc3CwsCErrjqqgpYQXFrr4eQ6WDVlL73QvelJP3SIcsc1bNS7wC-uDeUx6djbEju2ff8r48UyV_7mRZSEs4hvZOdAUm89E5VJz3jyFR54GtI1aCGCt5E8cBfhXF5y68IPsn2NfPWq4DBvRC3hxG8soBiceYU2T1-shGa5Fz6n8EFiWDV8Jq4Fg23PozilR5jXArIN0cb9XSnNzRdN-AaA0j74cz3zokJ-74sxAH3DJ-t3HYLcZMCC9ahYhFQP4B0u7ZdX7PpVYKm8fYvGNKmSxpLGuRCF9UdPI1OFCVEMnIht90YQZiUFcYczlTZvNm-zDWyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=s7nBVT6MOUKqeRVx6yc3CwsCErrjqqgpYQXFrr4eQ6WDVlL73QvelJP3SIcsc1bNS7wC-uDeUx6djbEju2ff8r48UyV_7mRZSEs4hvZOdAUm89E5VJz3jyFR54GtI1aCGCt5E8cBfhXF5y68IPsn2NfPWq4DBvRC3hxG8soBiceYU2T1-shGa5Fz6n8EFiWDV8Jq4Fg23PozilR5jXArIN0cb9XSnNzRdN-AaA0j74cz3zokJ-74sxAH3DJ-t3HYLcZMCC9ahYhFQP4B0u7ZdX7PpVYKm8fYvGNKmSxpLGuRCF9UdPI1OFCVEMnIht90YQZiUFcYczlTZvNm-zDWyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hi3MRHrZsDBQowQHsxMg-GKuKjGFxYnb2nceKU6a0w0GBMIgpoxtMdxJvnnyhJb6w9qeZY9IgMYq4Ixq5fLdsCsxxC9DpEpUjBAuLX8mVVXNPbvUjvlkxhNP69xvfJGu79lVZGk0niZsVy3pv3Y75r4APWqz1KvzkSW7mKXnh4kkG9eyCoYeEufIHyL6UjwvYwFolhTKc-vWq9wDvni7JLQnMV8-SRHQugEf9VF2QsIkm19Rw2nWrLFEkGm8gj4PLthZ2Mh3HjI5q8WBMGhdlRKNovXwxGjLaKvUpaPnEURIDwVmRj-89u89XfITJpVAlLK70hU_f-_A3HvAZjxcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKJHE7jQPaTQNFDybQTskwUqW-7h_AHB7pT5Ex13MYEEGOGxUGlcjV3AqcBCBeC2i1hQuFAE7VZo4Z17YLWh5bKzQoUI4Bs9kr2grT2bt8IF1JH7IDwp_33mnTMOoTqg173rVckqszBobk3TU3TTsr4YiTfe1oxzPgOqmEJFiLHBj1uNVh_i615NfGO0wGQv4jXZaApdhYDA6OxCfqEzPE1b9UXC6mR4Qd8ldEsPYufWQWsSUK9dPuKgVCAs6JgfAh9B4EZl2Vb8e2Y2CLlkmD-NvhX8AWoFknuDOBqdjhOpVg-yqCtZ6OpsLUihEd2ziVj41chSDldswR3_-1HB_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufAHjCVutYbGpqxrM6aB_EuXZI8i9H_Y92HnNaU1NF179ZZDd5fCpI0jvALKbjtLjDPTrIG_AhuIsVfdUd4XPjXH9wqHKKWB3LOUzLj0LkTdh6gnRsJemFacTN02eumPh5JpkPajgJZ9Q5DgAVPbVvrcWiYStpL1tDsXKKauEVZiEkFQmbji0foOlYtscP_4Q9OZ_Yf3xz8IztHDPeayh3ngtL69V_G4wnRrs2cZ6AN5qFOtje01Otpi--bXpYPPaLhQ0BbZkhICKQH6_FENAC2UD4Ei--qDGE4nun2PVtMVfIWPaITelzIDNz7-ecbI50n5_mO1tFix660rBU0Jag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSjVPD2fuvVaXRwucQsjjBYacwOwje3dpmQa-SEMQ0co1LtNWM0-rmqokMfYHtLtd1iStKzilbUZxZi80W16PnSDBkYMWJjLc2Ea0VVZFHH-Ntz78BbiO2-GYh5_oVLpuRBPiJ629_vZioi394s773TAiLmuhbNMU-VNMp1zWRgiT9uBzwFWwRL5sHaXLXIEa6pkRRJ1kbgwQcPkPVsTqComKrG9BAU6Z1EyXTZgDimJVHCwO8y5UCRzz4zmROueu7vLkR8KrFjI_DpyOeqDvWlLU1vZodBspf290gzglsWfZ-fe0MPafaNUOOOsnoXCChXrEuiXEzSDsgr9Ie9Fdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67081">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی وزارت خارجه قطر :
هیئت ایرانی از اومدن به دوحه منصرف شدن و مذاکرات لغو شد.
۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67081" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67080">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
جرد کوشنر و استیو ویتکاف، فرستادگان آمریکا، در دوحه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67080" target="_blank">📅 14:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67079">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
‏سخنگوی وزارت خارجه قطر:
هیچ نشستی در سطح عالی میان آمریکا و ایران برنامه‌ریزی نشده است
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67079" target="_blank">📅 14:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZUb9eV8_FZdUyv3IQ-m8QznYoyF-hnj0ctAE7jYW3xQbDuuhk0MFR26lQRq0zi0LzIL4KTcZIkVhaINeuETAYGISI584VAOKj6Jo_O1DBAulDbLy8FzR67Hb_cMCiH3MmTbopJXi15sT4xY8UvZo5GQkizYEGM69Loa7K3CJxOi0Ih2fq6xSrwkqrDQ6B1sv6AURmE8lvnJkiX4_MqINUYofBuhKfi55SesYk8slz3U__U4j41GYaHCM3IRh8mdb436tCQWPRZven9wxwvnayK5tillzDLyIh-TP9XIP4TiM92sSvTl6VJ5Tz8aUXOgfOXfzZaDZ22eQ8_cMi5YL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
