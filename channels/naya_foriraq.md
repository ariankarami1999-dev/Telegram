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
<img src="https://cdn4.telesco.pe/file/CCWQH8JdQhBiELSG3Gt8eck_LSfys4AU2S6FDvPLF6mPK--70lCupGG8V5WPwPQQat7kMkR_UrhGR_AwFDixaVj-QpWdsJdXMsuip243LRcz-0_EWEQ-7iw5JwQpFdzUP9W2-EL_Lc-mVJUucRNOdWHNGm8_tlw--wn5sh6JDbIyLmbwe3ux7UrJrJ7g3i3or-D-GILtrDIMLPNCh4veEQyzX9AfY8PTOOYzrRW8jsRx6wmZob9o6I55CJs71FNu1wx55Ljcn4nUwu8s5SSgru85qusRgNxWNJOI42QdYXNxhEi3RYnPrB708v1k57E5-kYBSyrxTmnWc60FYdscIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 23:52:11</div>
<hr>

<div class="tg-post" id="msg-81473">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تحطم طائرة مدنية باكستانية فوق بحر العرب على متنها خمسة أفراد أثناء رحلة من الشارقة إلى كراتشي.</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/naya_foriraq/81473" target="_blank">📅 23:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79ae4e2f7.mp4?token=tnbg90UzlMpKh10gUwh8dh9UY2DRwriVNi_8ynmaDa-Q8cUqMlHmRYnUzbVHyvRgY2yRkLfiIZSqp7G2wi-u9Rjlz2ysmgulBLGMt_PXFWeclCj4TDrcDefSU6-9qkWSFtYP5uWb4f-HRy4SudotJ0xbApH8P8RmxXXH4eZmH1RT5QtIJbDdsziLpOf48ZRgiBJY5vyROUqaiReNdw7T1O3ebPqPOw341Rz_V81Nho9R0GIko9oRO5MaSFMzBe-BfvCCemVI0ZtR9ZkBxHazepBFfEDybUjESHqP-_YP4vLNdAQrzyxAGyt92zx-3454CMv_yNiw7t8LZtUJkaAU6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79ae4e2f7.mp4?token=tnbg90UzlMpKh10gUwh8dh9UY2DRwriVNi_8ynmaDa-Q8cUqMlHmRYnUzbVHyvRgY2yRkLfiIZSqp7G2wi-u9Rjlz2ysmgulBLGMt_PXFWeclCj4TDrcDefSU6-9qkWSFtYP5uWb4f-HRy4SudotJ0xbApH8P8RmxXXH4eZmH1RT5QtIJbDdsziLpOf48ZRgiBJY5vyROUqaiReNdw7T1O3ebPqPOw341Rz_V81Nho9R0GIko9oRO5MaSFMzBe-BfvCCemVI0ZtR9ZkBxHazepBFfEDybUjESHqP-_YP4vLNdAQrzyxAGyt92zx-3454CMv_yNiw7t8LZtUJkaAU6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لوحة الوفاء الأكبر.. النجف الأشرف تشهد رفع جدارية استثنائية للمجلس الأعلى الاسلامي العراقي بالتزامن مع انطلاق التشييع المهيب الإمام الخامنئي (قده)
#قوموا_لله</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/naya_foriraq/81472" target="_blank">📅 23:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81471">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx9XqHEIF3kO89Nnlc-AuXjp-8ZcWFuV3V989P5xP7UOGhbpg0GX5sX8MhPRqEb9wkjkk-DQ9C3rn8WTREV_lYOdtmF7RL2kxfC0MC31tmyJRXxohUY6O6xHC-DSWPd-jRZ7V5rSEh6x9aK_EV3BQ8-i6XZhyrVYIj-E8cH7zJ-68Pi-FsGjCiScnAfmdwfAkn2kyJ_fLTNiU1OG0cxt1SdYkuWe8jr_OAlCQUpCSqWgFvU11m45z4C4HeoNReL2e9QIP93URsqIPbecCSrX6Kz8bNJ8MfG5RB04Sn1-WhgeOx0C2gP66261f18SEaLaVGUuCfZK40r5zJVZ0HB18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#قوموا_لله
تتصدر ترند العراق على مواقع التواصل الاجتماعي</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/naya_foriraq/81471" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a611a3cbdd.mp4?token=hza5PEh7Fp7tQjWHjalR05IKhrNxY7xlYmiZHwGna1LvrVSA7vjemLMPGjmAuDpv5h_2jsvKtiNWpmX4sO_OU_Eyd59vTd9AhJ__lpf76A2OKVjlSMxUgN64ifESwtSkpHP0XORIhS1R1SLAIOjUT1I-jrDtiAuoHJu7OxEFJZBIIINNzf9AmAPaBRCfbGXT1HZmBt6S_QSEgOb7O2y2S5cq4_BH_gQklPaam8Qev5fsDWEwcY6FR8x0QwVuHY4A3YxlyGvG0RH1ZYqK6zuC96JSzGAAl2GtzGO69O9X0iVq6C8c-_7v0iYpsxOASorW4qeXAPaalZMNQAP8dokOEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a611a3cbdd.mp4?token=hza5PEh7Fp7tQjWHjalR05IKhrNxY7xlYmiZHwGna1LvrVSA7vjemLMPGjmAuDpv5h_2jsvKtiNWpmX4sO_OU_Eyd59vTd9AhJ__lpf76A2OKVjlSMxUgN64ifESwtSkpHP0XORIhS1R1SLAIOjUT1I-jrDtiAuoHJu7OxEFJZBIIINNzf9AmAPaBRCfbGXT1HZmBt6S_QSEgOb7O2y2S5cq4_BH_gQklPaam8Qev5fsDWEwcY6FR8x0QwVuHY4A3YxlyGvG0RH1ZYqK6zuC96JSzGAAl2GtzGO69O9X0iVq6C8c-_7v0iYpsxOASorW4qeXAPaalZMNQAP8dokOEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهافتت قلوب العراقيين لحظة وصول جثمان السيد الشهيد إلى أرض العراق.</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/naya_foriraq/81470" target="_blank">📅 23:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81469">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9675615690.mp4?token=k-43gZ1cDLWYU9QVuIdO5ctbzzdHGDU1KeGLqQVe4piE600naWoskSFLyzBJGvjC4HuWmR_pglJvZq2D4TtUXUYtPaclWmJEE_kovBHPgnvZnjqe5TaoZKwbccvyLEZyecrvOmqNeoqZeN2ExOsMFjwcUMSin8UkswTeElkf64o4-klHsnR9cQYNKNcRc6-I2AARwevjiBZgSOzBlHf2US4EOKLg2U2oPRBTDjUGHIHGQOOs4M4C7lZEuBHJ6iCWQYeu15m_3XlSKyfH7-0v7zLjOOUTZg8WUPRr4cy0M2FmX-UMsiabVzCbdnRT2S1vl4DqjZmK3Q2HPxP_rR3IwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9675615690.mp4?token=k-43gZ1cDLWYU9QVuIdO5ctbzzdHGDU1KeGLqQVe4piE600naWoskSFLyzBJGvjC4HuWmR_pglJvZq2D4TtUXUYtPaclWmJEE_kovBHPgnvZnjqe5TaoZKwbccvyLEZyecrvOmqNeoqZeN2ExOsMFjwcUMSin8UkswTeElkf64o4-klHsnR9cQYNKNcRc6-I2AARwevjiBZgSOzBlHf2US4EOKLg2U2oPRBTDjUGHIHGQOOs4M4C7lZEuBHJ6iCWQYeu15m_3XlSKyfH7-0v7zLjOOUTZg8WUPRr4cy0M2FmX-UMsiabVzCbdnRT2S1vl4DqjZmK3Q2HPxP_rR3IwIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تهافتت قلوب العراقيين لحظة وصول جثمان السيد الشهيد إلى أرض العراق.</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/naya_foriraq/81469" target="_blank">📅 23:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81468">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd55bc01e1.mp4?token=ZmXks2pFMZIdGWQLzTFeww-8mH34eGiiimAmptr3FXnPbk42PgIBWNZPScfV6MjzTfoqaW08sl9ibiRD3CSqrlfJDoSk7V08Oz_N5cMMc-9TVvIr75OfxLjynFrDiTNuc0gIb_dzyOCZpT0qkFyqh0-iESyPFgsGAz6rzu8rq_NN-qtFc2HDetF5HU6aag0R0JenUlpx-eIMeLvcPR4wO3S_EOl5Cy_tipV_aeRjFki2pqBAthvkWDY24s8kkYz-HUb1G_oYdRkIAsgN2iFFTbmIJcptSloXdzJyIoV22cRN-SqBV1EEmp7235i5TMmSxGQUqfJUKfiuXWYZD9ViIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd55bc01e1.mp4?token=ZmXks2pFMZIdGWQLzTFeww-8mH34eGiiimAmptr3FXnPbk42PgIBWNZPScfV6MjzTfoqaW08sl9ibiRD3CSqrlfJDoSk7V08Oz_N5cMMc-9TVvIr75OfxLjynFrDiTNuc0gIb_dzyOCZpT0qkFyqh0-iESyPFgsGAz6rzu8rq_NN-qtFc2HDetF5HU6aag0R0JenUlpx-eIMeLvcPR4wO3S_EOl5Cy_tipV_aeRjFki2pqBAthvkWDY24s8kkYz-HUb1G_oYdRkIAsgN2iFFTbmIJcptSloXdzJyIoV22cRN-SqBV1EEmp7235i5TMmSxGQUqfJUKfiuXWYZD9ViIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أين خامنئي أين...</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/naya_foriraq/81468" target="_blank">📅 23:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81466">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03e9cd7257.mp4?token=h32aTEyIlh1OaIKyQ1Bbpl3Jlnxdo7vuVZr_fdcWvl_yG132xN8JOUUciwx3Gc5SjJ7MihmqYUgZsJJcVoBDZsq0_5CMBcunVwv2PARdue6yfd5d5RC9B9MVh8OjuCjWhBrHVp9umsZkSC9eQobOS6wM4CWvh4Fmwd5ZUt2XW9suUV0jRcJoyqV3jho4upHmmPwODC1UOysKmgHT2q3X4DRQNCke580_u0e6tzNwNbTwiJTy4XsB7UdwDjL6D9B1cLwvIRKC9Gl14ifmQr10Lvi0yQR7eIC_NKwjsm0j-g885bmRh-dxX6f5iEtq-fm_zUx7IzTnMiEwBZU6T5MZ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03e9cd7257.mp4?token=h32aTEyIlh1OaIKyQ1Bbpl3Jlnxdo7vuVZr_fdcWvl_yG132xN8JOUUciwx3Gc5SjJ7MihmqYUgZsJJcVoBDZsq0_5CMBcunVwv2PARdue6yfd5d5RC9B9MVh8OjuCjWhBrHVp9umsZkSC9eQobOS6wM4CWvh4Fmwd5ZUt2XW9suUV0jRcJoyqV3jho4upHmmPwODC1UOysKmgHT2q3X4DRQNCke580_u0e6tzNwNbTwiJTy4XsB7UdwDjL6D9B1cLwvIRKC9Gl14ifmQr10Lvi0yQR7eIC_NKwjsm0j-g885bmRh-dxX6f5iEtq-fm_zUx7IzTnMiEwBZU6T5MZ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولى مراسم التشييع الرسمي للسيد الشهيد علي الخامنئي في مطار النجف الدولي</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/naya_foriraq/81466" target="_blank">📅 22:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/81465" target="_blank">📅 22:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">عدسة نايا لقطات حصرية عند وصول السيد الشهيد الخامنئي القائد للعراق</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/naya_foriraq/81464" target="_blank">📅 22:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65bb850197.mp4?token=DzMcu9931MEqHG2KJJxM8jZ-MY2EG4ow28ucUFHK_1v1oSCiBICeyeNHIQKcqf0BXk08-ksjT3tI1ZES27N5afzlhHeWly6jJXO9U4EFNV5GWJxD7k_YvlG3RJxNrEwaRPfanOFsoLryRe5ZTFZz1-RVBCdNbd-4yAAqt1a7S_a9IfamK06Gv4U3R9vjbm5zOijc3TyI8TiLT5UWCuu76x3kbVWfIzZBlU5L5cqFQZ0Sx9a3vru9cVbvxHoEEq7wX6tKVUONUySR0gXJ-NUY1_vKumBqMJ57rzdsgCIsOrD9eQFWL9D2_5XZykbhRTGb2lxPxOdjdCzP4poaUYHscw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65bb850197.mp4?token=DzMcu9931MEqHG2KJJxM8jZ-MY2EG4ow28ucUFHK_1v1oSCiBICeyeNHIQKcqf0BXk08-ksjT3tI1ZES27N5afzlhHeWly6jJXO9U4EFNV5GWJxD7k_YvlG3RJxNrEwaRPfanOFsoLryRe5ZTFZz1-RVBCdNbd-4yAAqt1a7S_a9IfamK06Gv4U3R9vjbm5zOijc3TyI8TiLT5UWCuu76x3kbVWfIzZBlU5L5cqFQZ0Sx9a3vru9cVbvxHoEEq7wX6tKVUONUySR0gXJ-NUY1_vKumBqMJ57rzdsgCIsOrD9eQFWL9D2_5XZykbhRTGb2lxPxOdjdCzP4poaUYHscw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انطلاق مراسم التشييع الرسمي للشيهد السيد علي الخامنئي في النجف الأشرف</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/naya_foriraq/81463" target="_blank">📅 22:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔻
انطلاق مراسم التشييع الرسمي للشيهد السيد علي الخامنئي في النجف الأشرف</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/naya_foriraq/81462" target="_blank">📅 22:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
الداخلية العراقية تعلن إصدار أمر إداري بترفيع ومنح علاوة سنوية لأكثر من 178 ألف منتسب.</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/naya_foriraq/81461" target="_blank">📅 22:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acae2a189.mp4?token=oXmIcPepJIr7P9iGdVpkrl-CKSWlXGNHOvlAHigIt3i103TsaQoAzDtWU4uXjTNzTR3VH9_9Mohx6GACCsgrWnQOyiC2K3l-rUIIMiXepIJ5m0rl2EsTllutqA8HZWm2UQLTuTYqZEq7bLiH2BOQSxJfMfGSGCb-F3oSZQf0tSM0CpbnzeRNC_EUO_6Jw_VaJWfkuiPfXJxMqLV36-PbPkr33LlnWkXLYY1RrUFd9Es_zKSh8Av-nsez8dWpRwS9OAwD6F-WCBhYRMk7SJkS16Eg3kNZrvjb1sNBzFTJ9bS60-OWJeLfxyjhhwytNN2MrlQ6rA24jbh24RiOu9-D7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acae2a189.mp4?token=oXmIcPepJIr7P9iGdVpkrl-CKSWlXGNHOvlAHigIt3i103TsaQoAzDtWU4uXjTNzTR3VH9_9Mohx6GACCsgrWnQOyiC2K3l-rUIIMiXepIJ5m0rl2EsTllutqA8HZWm2UQLTuTYqZEq7bLiH2BOQSxJfMfGSGCb-F3oSZQf0tSM0CpbnzeRNC_EUO_6Jw_VaJWfkuiPfXJxMqLV36-PbPkr33LlnWkXLYY1RrUFd9Es_zKSh8Av-nsez8dWpRwS9OAwD6F-WCBhYRMk7SJkS16Eg3kNZrvjb1sNBzFTJ9bS60-OWJeLfxyjhhwytNN2MrlQ6rA24jbh24RiOu9-D7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضع جثمان الإمام الشهيد في مطار النجف في المكان المخصص لتأدية التحية.</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/naya_foriraq/81460" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81459">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8dbce758.mp4?token=WXDWBJkDW0NKG_8t3HIrLqucEBV6aqABupXwp5basNRd0mpz-pSuyRIJSaTXFGy7kjBCPlpV_J11OANsS1Xct1Y5CmPj5c3DZWDVnHkJW817An07ooR3mojqTg6f2jLo3MwjfE15VtuF23SA9Gc6tNmws4QjRkerEvWPa5EcBD7OHSRhTlqbS6Xuep8cWCcj0RsJ0TlBn_wAtgvq-PbFOetePrJ0V-SKaim9dS-QGOOYVm2Xd7CG36FVdAWF924z50aPHi0GKvM_lAmCXjVR8x0J2KY6LS0xGJ84MboCLFp7NwBh8kulqZzVeeNvUHjOhO7b06BZzZZGexjhdUYOCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8dbce758.mp4?token=WXDWBJkDW0NKG_8t3HIrLqucEBV6aqABupXwp5basNRd0mpz-pSuyRIJSaTXFGy7kjBCPlpV_J11OANsS1Xct1Y5CmPj5c3DZWDVnHkJW817An07ooR3mojqTg6f2jLo3MwjfE15VtuF23SA9Gc6tNmws4QjRkerEvWPa5EcBD7OHSRhTlqbS6Xuep8cWCcj0RsJ0TlBn_wAtgvq-PbFOetePrJ0V-SKaim9dS-QGOOYVm2Xd7CG36FVdAWF924z50aPHi0GKvM_lAmCXjVR8x0J2KY6LS0xGJ84MboCLFp7NwBh8kulqZzVeeNvUHjOhO7b06BZzZZGexjhdUYOCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدم بالدم ناخذ ثاره
الإمام علي النجف الأشرف مباشر</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/81459" target="_blank">📅 22:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff124e6770.mp4?token=tODATYc2xC-cVKN1bKJ2AgsfKW5-COz3YIKJ1gb42ZV64JAsnPzfllwKeXawvRqhd6F-wPMj2s01XQmbYO3GkzsXs9zInSB_jq2p0OC7Vzc6gvLikJsbJWkG1zK9am8VUEaG-N1BFgR-1y4Uj-yKR6DZUHS8p6_908foX0jtD3AsDWMEYNkX5uGPfmS4bN0mQ06s4Hec4BVQJPiaaQbDiCLOnFEOqCJ5IO9j4jx_uqvcmcUQ2R42X_gjOF6H2DvzCOnubnvatFGf0_tmQfe3VrdY0CudDdlDWMwpQfq3BFioXMFKIlRWBpc1gJ-hi4ZG6XhTXDUQhjS6UYcaAZQj1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff124e6770.mp4?token=tODATYc2xC-cVKN1bKJ2AgsfKW5-COz3YIKJ1gb42ZV64JAsnPzfllwKeXawvRqhd6F-wPMj2s01XQmbYO3GkzsXs9zInSB_jq2p0OC7Vzc6gvLikJsbJWkG1zK9am8VUEaG-N1BFgR-1y4Uj-yKR6DZUHS8p6_908foX0jtD3AsDWMEYNkX5uGPfmS4bN0mQ06s4Hec4BVQJPiaaQbDiCLOnFEOqCJ5IO9j4jx_uqvcmcUQ2R42X_gjOF6H2DvzCOnubnvatFGf0_tmQfe3VrdY0CudDdlDWMwpQfq3BFioXMFKIlRWBpc1gJ-hi4ZG6XhTXDUQhjS6UYcaAZQj1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول جثمان الشهيد السيد علي الخامنئي إلى المكان المخصص في مطار النجف الدولي</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/81458" target="_blank">📅 22:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c86698fb6e.mp4?token=Gs_mK6k7AFUuA_HUiyEzsFzLvFSmR2zX_pZ6Rd6VJ83cRBiFnempiFDmmnzPs5ShC8QQeIw595myAhwBrd_nv7_ZmFr49Zal56c0wQphl2H6Z7WA1VTEavV2DeRhwGJqDapnuzzo80edgbVV9dZ6HsKOHQ_-dud9RE_CHTCVFI0uVbILTX58ecxUNl_4gAjTNIP3FzBwF9v42jTlNcqdEk1a2eiaGoJDWF7_bbNFE8lgdpEsRqOL_20Ex_j9mDbrlgXNKCj3I6Vy3V8XiXKE0EHVnbmheCHueEFV8DrIq0qcGOIWC_gvoplKozQVRgEXxX68puturznqOQRri8QToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c86698fb6e.mp4?token=Gs_mK6k7AFUuA_HUiyEzsFzLvFSmR2zX_pZ6Rd6VJ83cRBiFnempiFDmmnzPs5ShC8QQeIw595myAhwBrd_nv7_ZmFr49Zal56c0wQphl2H6Z7WA1VTEavV2DeRhwGJqDapnuzzo80edgbVV9dZ6HsKOHQ_-dud9RE_CHTCVFI0uVbILTX58ecxUNl_4gAjTNIP3FzBwF9v42jTlNcqdEk1a2eiaGoJDWF7_bbNFE8lgdpEsRqOL_20Ex_j9mDbrlgXNKCj3I6Vy3V8XiXKE0EHVnbmheCHueEFV8DrIq0qcGOIWC_gvoplKozQVRgEXxX68puturznqOQRri8QToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تشييع مهيب للسيد الشهيد في مطار النجف الأشرف</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/naya_foriraq/81457" target="_blank">📅 22:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">استقبال العراقيين للامام القائد</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/81454" target="_blank">📅 22:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FneYzblgYwM0o8CIYT2YNfGlMurcGJc7P7INujGJCZGdopdRU79sFVuAXx1rpCXPu8eCL9PeFLksxWsVbVl_anDifRhvkh4nkiIFidV93-ar3J_fDg2TFD7K9gucXMymmlesu2ucIw7cmQ5cVBVME2l6_EE17uR80NFTzCYucnJ5WxpahW-wiDEtNnqQr4nUmmgyxhtaGrdVjLPYDvvuZmrnzYrTF8PwTQLIfJ4Qfmu-GgPps1toeEAXEuzK9RuQlOHICqbnGRJfLsgj7Hp5yabcMom_-kIvZjXpZMdLwNu9F8s239cgQb68lkelKNQw8KsmA_l-rAYkQwQlAlYtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جثمان السيد الولي على أكتاف العراقيين في ارض النجف الأشرف</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/naya_foriraq/81453" target="_blank">📅 22:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c718ba0931.mp4?token=dza4SrfjbeSi5O2dv1h-mDG6v5XriNoHzW4p5yVdoZ9yI6jhYp2oFbQ5Wo3_tZa2qOtHnvqiqS9INZgqtBvld4LycKucxuhidygvnzlZKyFVU3hovcVBknp4H_E4xahrerBZDHC--XbO2-XKpjFUVpsGI4ac3Y8BXziXiGUPwBvGFq9oVwhiqzq-TB-1g2own274pPwWNBHc0F4YcLGlgD3dXDPYE-eqPjX30b0pmccRcHhJH1OFBkF7G0e-WGrN0Ip4nBfHPCE4hagTwRQ9yx99Oy1MwIJzafkRrM4xlD0iKifLFXAK85PHl7ebEd-0qdvhJPZoK4MvZh0sWdDNZhy67SKFdktmm4jqY_z4F3XlLnSlDNYmeRlA7feLZkb5tL8UJ_OEl9QxaVC_2g9dMm88Rly4gdonT1ws-j0oWqxduU3fc2pHa60BIcLtgbCuzHeC4rNiIVcLecg47h1qMp1_C2u1tx4hbDIVK_wRV0cbTwf52nnCaefToDXytR5M2JYxvZVtmcYfvdFAb0HP13JtHP4iMXtuSzNKSstMwC2HdTtr6yipgv2UXS68jBbooPbzYhnpwvdSXGvjgXwsSQEtk0nmZAvjYBpqQCXRPtI_TjsqKPD1CVWSl5OmU0FI8ozsNOOnCnBpZnD8dk0fzIGZZx2WLGoy_5V6L7gJOew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c718ba0931.mp4?token=dza4SrfjbeSi5O2dv1h-mDG6v5XriNoHzW4p5yVdoZ9yI6jhYp2oFbQ5Wo3_tZa2qOtHnvqiqS9INZgqtBvld4LycKucxuhidygvnzlZKyFVU3hovcVBknp4H_E4xahrerBZDHC--XbO2-XKpjFUVpsGI4ac3Y8BXziXiGUPwBvGFq9oVwhiqzq-TB-1g2own274pPwWNBHc0F4YcLGlgD3dXDPYE-eqPjX30b0pmccRcHhJH1OFBkF7G0e-WGrN0Ip4nBfHPCE4hagTwRQ9yx99Oy1MwIJzafkRrM4xlD0iKifLFXAK85PHl7ebEd-0qdvhJPZoK4MvZh0sWdDNZhy67SKFdktmm4jqY_z4F3XlLnSlDNYmeRlA7feLZkb5tL8UJ_OEl9QxaVC_2g9dMm88Rly4gdonT1ws-j0oWqxduU3fc2pHa60BIcLtgbCuzHeC4rNiIVcLecg47h1qMp1_C2u1tx4hbDIVK_wRV0cbTwf52nnCaefToDXytR5M2JYxvZVtmcYfvdFAb0HP13JtHP4iMXtuSzNKSstMwC2HdTtr6yipgv2UXS68jBbooPbzYhnpwvdSXGvjgXwsSQEtk0nmZAvjYBpqQCXRPtI_TjsqKPD1CVWSl5OmU0FI8ozsNOOnCnBpZnD8dk0fzIGZZx2WLGoy_5V6L7gJOew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جثمان السيد الولي على أكتاف العراقيين في ارض النجف الأشرف</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/81452" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزارة الخزانة الامريكية تلغي ترخيص تصدير النفط الخام الإيراني</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/naya_foriraq/81451" target="_blank">📅 22:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزارة الخزانة الامريكية تلغي ترخيص تصدير النفط الخام الإيراني</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/naya_foriraq/81450" target="_blank">📅 22:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabe8849b9.mp4?token=IaG4vl4WulbWWpJTpbeJY05rN2s9U2MGn3OUM3GgN1ZvgZcbzw-87PgGPjQtBFUn2s6apW7XhJOoCbWQJRtKqhPw4dybII1bhLnMLZKV8pehrki9Ftjw7ooi3J8kxo8KZoSYwpWxa21t8B-3JUFuupsGSk7DIUCyZoTux6Re7sx6elX4zRmwFVvpl8IsGQbLq2TZ641FkwZmhlDnUH6ECyHyF0-dUbgnaoXAf8vO8702XoHE1iadxUUC4X_E0j1dyuVYSuZS1930kL3B0JwG3iSRoKaINy41a9fsFxa4Ae4eR_87eVCMGHZYTiv0ttp_JEafG4nUPvDfx6lQk1SAzqlGLHB8aVe_W9f2eFYHWTmw1T_VGxNj7gucJzOSzM6QxAyI0GD8ZNLApQT9tuZNo0ePApocvkPFGzK6Tsh0Xu7ZyYKu2oM230m5UKiNna2-96M5xaywG52RMzpM8enWs8xBJWOWgvAPB67MR4cHEemvZ1zfhteB1sYcE1TjObi2sjyB8MxiuBo9epyz7sJm2c7wukJDcVd8CSDByaJEXWmR35H80WKFdoroSl7OTmzuU6Ts5ekPtBbpGQstG7sWFqoouYdaJ0_kq96yYXT-NAlXXovtFhFU4-elSKrqyNPYJ9te1Uu-q8ljUKDTn7jt0kUIq8gvUcc5Ue2UK63aPdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabe8849b9.mp4?token=IaG4vl4WulbWWpJTpbeJY05rN2s9U2MGn3OUM3GgN1ZvgZcbzw-87PgGPjQtBFUn2s6apW7XhJOoCbWQJRtKqhPw4dybII1bhLnMLZKV8pehrki9Ftjw7ooi3J8kxo8KZoSYwpWxa21t8B-3JUFuupsGSk7DIUCyZoTux6Re7sx6elX4zRmwFVvpl8IsGQbLq2TZ641FkwZmhlDnUH6ECyHyF0-dUbgnaoXAf8vO8702XoHE1iadxUUC4X_E0j1dyuVYSuZS1930kL3B0JwG3iSRoKaINy41a9fsFxa4Ae4eR_87eVCMGHZYTiv0ttp_JEafG4nUPvDfx6lQk1SAzqlGLHB8aVe_W9f2eFYHWTmw1T_VGxNj7gucJzOSzM6QxAyI0GD8ZNLApQT9tuZNo0ePApocvkPFGzK6Tsh0Xu7ZyYKu2oM230m5UKiNna2-96M5xaywG52RMzpM8enWs8xBJWOWgvAPB67MR4cHEemvZ1zfhteB1sYcE1TjObi2sjyB8MxiuBo9epyz7sJm2c7wukJDcVd8CSDByaJEXWmR35H80WKFdoroSl7OTmzuU6Ts5ekPtBbpGQstG7sWFqoouYdaJ0_kq96yYXT-NAlXXovtFhFU4-elSKrqyNPYJ9te1Uu-q8ljUKDTn7jt0kUIq8gvUcc5Ue2UK63aPdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس مجلس الوزراء العراقي وبزشكيان يستقبلان جثمان السيد القائد</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/naya_foriraq/81449" target="_blank">📅 22:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkULgLgB1nKfOlsRd-QLpGaggJK0Q4eI-mYns4MDCalChO8z2nVv0hFTPuD_aFPxg8HhxhtRIyU85BBEbseQLrck3NiRXo6_lViVWC-sOGiLjAtUMbUpP3CS_wRWPjLch0Vwn8vmdShCeURIHDdxw1NJFiwmS0p5RnvdbpTOW3Z1KrrySwbSRkWt87MKfVRrxj1iwiBW1O-X7eVzUyPrS7KvVNnP04sppOQofW9-HfmD5wMKlfqmWXAxIFE-H4OeqeFhIUdhr0mybrPbevIeDelj1nFyUiMIR5MP0uXKMEnRvLR0PQUWGN5VGmYodmxWu_hg5TSO-aTHWGrSpYID6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج النعوش من الطائرة</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/81448" target="_blank">📅 22:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d3c10c72.mp4?token=tXg4jycgziT5_0pxR0poAi_uQdyCmxhnToZLCFv4U8bHhQjQxUrpPTXm5zw4BF1AwCWH2dqrgwxt0OCofCJOnrB9XCv61K8livO5e0-Tim_aBR5WMBH2p0zgCNWzjgwhPiC0M4zqNM3NNBOxewfieqfs_G7xVMKEPGYThyj6tycmCBdnKkgqOyIpENUbNhswlVBDRhkLgBOhvVX3tZ5t730puHEtDuSk4spZPCJlPJODXms3uqfyDoy0B1a03S5PkINzKEnEyoGRBd_YhyBO6SwVnM0VPL-aqk5RJiOFPsa2PFzFG2yLyD28nqHRdPQSbzQxQb3a5RKh6J3v8bGiQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d3c10c72.mp4?token=tXg4jycgziT5_0pxR0poAi_uQdyCmxhnToZLCFv4U8bHhQjQxUrpPTXm5zw4BF1AwCWH2dqrgwxt0OCofCJOnrB9XCv61K8livO5e0-Tim_aBR5WMBH2p0zgCNWzjgwhPiC0M4zqNM3NNBOxewfieqfs_G7xVMKEPGYThyj6tycmCBdnKkgqOyIpENUbNhswlVBDRhkLgBOhvVX3tZ5t730puHEtDuSk4spZPCJlPJODXms3uqfyDoy0B1a03S5PkINzKEnEyoGRBd_YhyBO6SwVnM0VPL-aqk5RJiOFPsa2PFzFG2yLyD28nqHRdPQSbzQxQb3a5RKh6J3v8bGiQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد القائد وعائلته على أرض العراق</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/naya_foriraq/81447" target="_blank">📅 22:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">لحظات لاستقبال الامام القائد وعائلته</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/81446" target="_blank">📅 22:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">التلفزيون الرسمي الحكومي العراقي يخصص بث مباشر وتغطية خاصة للتشيع</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/naya_foriraq/81445" target="_blank">📅 22:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81444">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTJbSkMDOJvDnB-eatFQm261iqkLS_jaOtaJGNnYMrp32VitD31XxAQJEPu4qVjorspPpGC0CzylN9jPVy_JvZWPDlZgClThfoQOKfu4ImyVB8JTH9WF_Wwciwxkqe9V-a7hVGgM89GEqs97c4AGzE_FGWF7uXzTDUdAQwSR_R3kZ9DJLCRNa_dafEetonlrx4KIE6GNHM5EmHyI-rAV_BJ6O5-Zu9Wnn8iyFgALNEspod5H3hErp9OSYPJL9ml6BdI0ZLYQRxWTBCsSS4IFfW3ZMRi6_RLKVcSq9BrZtoWYGFx3qtBqMbnn9GZIoVf1AhSoDpqcTY37kYEA_ptiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد الحلبوسي رئيس البرلمان السابق يبكي ويثغب امام الطائرة</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/81444" target="_blank">📅 22:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571e5da2ac.mp4?token=TUf6Lcn6dqXa7lihY1Nl-TyF5sgQr_qfETovUckynB_4hAlQiUiJjXUTDSHxrZ1Z2dHNnDg6nAEb-q8YXGhRAf_N9MAJFUlLdaDlrKjOhazzVkebH_UR_CWAo8Np00WrPmCyo8BROzBegvx0m3vlKlaIUwi8WTNdS2VnxMYkn3sJf58gKj2y6VdFd7r5qWVtLbQF2H8EukAzxrLtZOHvlA6-87OX1qFa6aeiuLIPxWIjU_vhPuDnqknycX1k-irMXnJD7T8FfC6hb2PIzIonMKkEBS1fzGiElWs8TZ7w7ZhTK_o7C9R4thHVfXquUfszGIPCXbuMiZTHIysISa3c16f1sXnLQxF5xGBYwiQXvvNEKmwvJdaUw_cMOWBQhHWEfnLwUR9H1H59JahAU0QwODy-ilwrn_-bEXdat7a4H36fZuWdibZLLJWjVgsZP1B4Z8XWVuuprx3zOFYH122NJmRhXmSr5CL2V-vz4drGHPjEReL_9AbJeZkk_6P7DUD9T-Xg5XVS61ZWjypd9DO3CfcZh9TvpjYkSHF9KXlZYujmEE6jqCidUjV64sdzsm4Exn8an-azEU7san6ZTKI4RKBD4NL1Y1i0rUeh_uHtQtWvw2YjoG9rglGGi-feH6fPSVnMCDvk9xW2JwYubj43Rk3pgdday3DHqqX_WJ9RVnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571e5da2ac.mp4?token=TUf6Lcn6dqXa7lihY1Nl-TyF5sgQr_qfETovUckynB_4hAlQiUiJjXUTDSHxrZ1Z2dHNnDg6nAEb-q8YXGhRAf_N9MAJFUlLdaDlrKjOhazzVkebH_UR_CWAo8Np00WrPmCyo8BROzBegvx0m3vlKlaIUwi8WTNdS2VnxMYkn3sJf58gKj2y6VdFd7r5qWVtLbQF2H8EukAzxrLtZOHvlA6-87OX1qFa6aeiuLIPxWIjU_vhPuDnqknycX1k-irMXnJD7T8FfC6hb2PIzIonMKkEBS1fzGiElWs8TZ7w7ZhTK_o7C9R4thHVfXquUfszGIPCXbuMiZTHIysISa3c16f1sXnLQxF5xGBYwiQXvvNEKmwvJdaUw_cMOWBQhHWEfnLwUR9H1H59JahAU0QwODy-ilwrn_-bEXdat7a4H36fZuWdibZLLJWjVgsZP1B4Z8XWVuuprx3zOFYH122NJmRhXmSr5CL2V-vz4drGHPjEReL_9AbJeZkk_6P7DUD9T-Xg5XVS61ZWjypd9DO3CfcZh9TvpjYkSHF9KXlZYujmEE6jqCidUjV64sdzsm4Exn8an-azEU7san6ZTKI4RKBD4NL1Y1i0rUeh_uHtQtWvw2YjoG9rglGGi-feH6fPSVnMCDvk9xW2JwYubj43Rk3pgdday3DHqqX_WJ9RVnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور كبير في مطار النجف الدولي لاستقبال الجثامين</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/naya_foriraq/81443" target="_blank">📅 22:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دقائق قليلة والعراق يستقبل الجثمان الطاهر</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/81442" target="_blank">📅 22:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81441">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">أعلام العدو خلال الأربع والعشرين ساعة الماضية: أطلقت إيران خمسة صواريخ وطائرات مسيرة على ثلاث سفن في الجانب العماني من مضيق هرمز.
هل سيكون هناك رد أمريكي؟</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/naya_foriraq/81441" target="_blank">📅 22:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHQ0bNz8sFgYTxpj9Es9IUsUOxIR8674RAjAoFdZovTf7v8BIVv-AX5C2IoV3LquEuV62ZtmqvCp_1dtQhT7-drvsHYgKRHkU7Sf-BF3VrmTvSfBlyY-nRfN0y6dzJ_xQKEVC-O9dsXEF7eMO3NFEZ2sr055BHmZEu0O_Xk4Ipvkdrn2YrM0qy4ny3fc2J_fDv1kBaT8WT9H2yuttfgt053rNnh-ZWy5avwC_ZoQAqHiujUAncj7a5a2iYHDjJWbJmNEijtIi7l1NVQUcz6_k2jg-VACt66vQ_4NRPWxpZ2R8miJ1K8coyTlttrRPlc52fdicHZfVvZQOHbxYJmfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقائق قليلة والعراق يستقبل الجثمان الطاهر</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/naya_foriraq/81440" target="_blank">📅 22:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee83fb66b.mp4?token=uPoB_RTmkeESmq2_tZKpxTInpixFndBUJF1zwRxS97FoLq4Rw1OpXQ7YFLST2GpoQguWEiMxfhg6ZHnwpej0JtjZ5LSK8cZp3Xon5Y31_jQxnYZ0n2jW693VTHqSN8T0ZKZHi9HfTrGUr8bk2-DDTTQmYzLdAn2p4CEW1CQSnG5UCrNWE2K1ozlXbDB9DJTBY0pbfpax1dYThApfxp_WSIvFpCZzd1juVewndBlYKuURSWqbid-mAhj9rOB49qcvcdtkk5EpFH2xFpGcq_DG-XNOADA-rs4BFxpTfZCxFKEqjiZTRlqgL058Edd2M93xA7Jln6TEKNFX-VplI77uIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee83fb66b.mp4?token=uPoB_RTmkeESmq2_tZKpxTInpixFndBUJF1zwRxS97FoLq4Rw1OpXQ7YFLST2GpoQguWEiMxfhg6ZHnwpej0JtjZ5LSK8cZp3Xon5Y31_jQxnYZ0n2jW693VTHqSN8T0ZKZHi9HfTrGUr8bk2-DDTTQmYzLdAn2p4CEW1CQSnG5UCrNWE2K1ozlXbDB9DJTBY0pbfpax1dYThApfxp_WSIvFpCZzd1juVewndBlYKuURSWqbid-mAhj9rOB49qcvcdtkk5EpFH2xFpGcq_DG-XNOADA-rs4BFxpTfZCxFKEqjiZTRlqgL058Edd2M93xA7Jln6TEKNFX-VplI77uIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقائق قليلة والعراق يستقبل الجثمان الطاهر</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/naya_foriraq/81439" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7631b638cf.mp4?token=uqPWuFxWj5kHk-2PRmU6ia3XB5999F3jqGyf63HMGfNHf5Q7AqMO5N4UZWt3ufaG6_EoT69zn32XrSfIIyuYe8Zf1iUvxDZagKnQddTSBDLfUKtOIObmx9w1_GqoTTvpkQUaN-TPtrFRw6aZfdql8WaKhlivrNL--Ugoqt_ra8aYIkktPv8_yhTytpDGbw5xjVGFua0ILtUPLyPkpGbDHz4xuHW4FlDkqWhIZOsymkAaYz8aL84zU11rEZDtKvxwQzZuLocdRJJuqmMVbPTagZzDfBZIs0ke55OqXBCN55qpSswGuZ3M01QpT5p_NHfhrg5X2eGnexw5rQqBigPRyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7631b638cf.mp4?token=uqPWuFxWj5kHk-2PRmU6ia3XB5999F3jqGyf63HMGfNHf5Q7AqMO5N4UZWt3ufaG6_EoT69zn32XrSfIIyuYe8Zf1iUvxDZagKnQddTSBDLfUKtOIObmx9w1_GqoTTvpkQUaN-TPtrFRw6aZfdql8WaKhlivrNL--Ugoqt_ra8aYIkktPv8_yhTytpDGbw5xjVGFua0ILtUPLyPkpGbDHz4xuHW4FlDkqWhIZOsymkAaYz8aL84zU11rEZDtKvxwQzZuLocdRJJuqmMVbPTagZzDfBZIs0ke55OqXBCN55qpSswGuZ3M01QpT5p_NHfhrg5X2eGnexw5rQqBigPRyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول جثمان السيد الشهيد وأفراد عائلته الان إلى مطار النجف</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/81438" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وصول جثمان السيد الشهيد وأفراد عائلته الان إلى مطار النجف</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/81437" target="_blank">📅 21:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هبوط طائرة إيرانية الان</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/naya_foriraq/81436" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هبوط طائرة إيرانية الان</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/naya_foriraq/81435" target="_blank">📅 21:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هبوط طائرة إيرانية الان</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/81434" target="_blank">📅 21:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzC8TowSJZUEnf0mkUCUJhduQHwolQcPRxFDfseTl7us78W-44uhRaYg5CZkwD-tyYvMEAUAY4BUC75fsDngo8FKN2L2jzN4mMUxQU1RGXmMyEs94JoiMTI2c3Tp5uRgu-n_CCaLXQ-_f8BgIl7iziadUSc7z43x02Dr8TarNsYGV5LTVCLaXXZCNKgkZj-ItLD7jzS6gI6UU2z1z0oQwP-dQwE6ARzjxr90-RkuVq1olkqUEKlcNtb5pckfeQcxS5Yb4_Dh0R-fd97RZtnMxVLTLZqGvM6zpzzz5ViPDRh-fAmc7w2Y15LbnjjTjlwSnX8iXbfkAXWY3Om9ZY9ySw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">التحضيرات الأخيرة قبل استقبال جثمان الشهيد علي الخامنئي وأفراد عائلته</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/81433" target="_blank">📅 21:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مونتي كارلو لا يسمح لقاني زيارة العراق وتم ابلاغه ان ضيف غير مرغوب به
😄</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/81432" target="_blank">📅 21:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpKq-oxcQ2gOOOYfirWoa1RhWogp6Om0Ui2KYBl4HKN5s7NBJk280PitpKwWSowrf0U31cuiiROT72CyjOUpec2ELusKMDaiRBsG2Y8R6R4Deijk_ETaDHTG2ttTwUQRTxnzvNDznNlWvksDqoxqee7p9oITNo6wKKCj1CbZYEmkp584ah3kn3RLTmRcadzdEWy0SP4lak5jHymb8Tl605OABFRrWDDE1pvbIkdNE3JB2XN_IktVHEN2bXJeMWLQuT6sQsILJwcQgGrvg3ZquSD4o6hygAGtg8P4uISvB4lPrq6dhxZ7x6E5QIkhuGwhCXZtO2wPwS8nWLpbc6iZxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/81431" target="_blank">📅 21:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca633d74a1.mp4?token=HdKFDXMCeO7jsuu0L4dLTO6rPwL8srJnaJMzLowzk3Q-MeKjSInZ7COfYd-VAB0mtCW7wwQjI_Vx5ATdwBwfVXkxCGILFow3EQsyjFFqeiosVSTd7WgYttTpgmMMudsZbhycjR4OPP7wnIbo-oHF2dWzfzgqB5DxwWwV-XJWPL2qHGtxAuf_zLEEthmW7hQm3M9RqBPKPAtLSuvN_K62zER5YsbeFp1Xm11C9SdcLC0ydjF8qGCsOltscwnb1H4utYneV2Xt8cKHtxk8De3LBwp1hfgCkiKkGoIoF43rOx7MdnD2CY26dppokX6gp7hjXuOiIjLo05Ac7NwJEY0e3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca633d74a1.mp4?token=HdKFDXMCeO7jsuu0L4dLTO6rPwL8srJnaJMzLowzk3Q-MeKjSInZ7COfYd-VAB0mtCW7wwQjI_Vx5ATdwBwfVXkxCGILFow3EQsyjFFqeiosVSTd7WgYttTpgmMMudsZbhycjR4OPP7wnIbo-oHF2dWzfzgqB5DxwWwV-XJWPL2qHGtxAuf_zLEEthmW7hQm3M9RqBPKPAtLSuvN_K62zER5YsbeFp1Xm11C9SdcLC0ydjF8qGCsOltscwnb1H4utYneV2Xt8cKHtxk8De3LBwp1hfgCkiKkGoIoF43rOx7MdnD2CY26dppokX6gp7hjXuOiIjLo05Ac7NwJEY0e3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اختناق فوق مونتي كارلو   تفهم ما تفهم مشكلتك</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/naya_foriraq/81430" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قال شو؟ شخص غير مرغوب به</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/naya_foriraq/81429" target="_blank">📅 21:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8af3e7c08.mp4?token=b8WCqITSS_ieZZuU8uq-Usj1q-xIwRsYuyEgdtdIWM3KiShc5ZpDdIwHfhvCTSTDkvbt4e3qpLZQQZCCrMaaOegeESsRyATMgQIzYfHjvx5g_QGXrjw4coD2rCYyQoS_zd6BMrFjibijvjWrAWMcZb9SmVdKhjIIE-iG4V9uCTzhMejybAGJMrH0KXvwC2EMrhAkslYFOVbpPI331sG-Ydu1D_RbgG6wpgoC8_aY26VA0iWiE3gDtKtoZFnkQpXa22a7HMC0zWrbZB0avTWVWiJgFPxJl2OZ9XeUatN-0_jGgwjVl1rCpJu0baE5x_-dGrhNdxStZtC7Ic98GJGL4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8af3e7c08.mp4?token=b8WCqITSS_ieZZuU8uq-Usj1q-xIwRsYuyEgdtdIWM3KiShc5ZpDdIwHfhvCTSTDkvbt4e3qpLZQQZCCrMaaOegeESsRyATMgQIzYfHjvx5g_QGXrjw4coD2rCYyQoS_zd6BMrFjibijvjWrAWMcZb9SmVdKhjIIE-iG4V9uCTzhMejybAGJMrH0KXvwC2EMrhAkslYFOVbpPI331sG-Ydu1D_RbgG6wpgoC8_aY26VA0iWiE3gDtKtoZFnkQpXa22a7HMC0zWrbZB0avTWVWiJgFPxJl2OZ9XeUatN-0_jGgwjVl1rCpJu0baE5x_-dGrhNdxStZtC7Ic98GJGL4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محافظة النجف الأشرف تعج بالمشيعين للسيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/81427" target="_blank">📅 21:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3986d93255.mp4?token=IE4EP1p1zp9fgDvQMzCdN-sPnIp5g7DC6ZA2Kx41lOeUWCXnEYjkaw43EHON5Vt3hapxqmIBF3Ou_JDofaZGqJ0BH8AHCOm6Mzz2d9LdmfsdCIzrhn0rG0XdE4uuge6Q4GDxFvFSl39Bc24GE_6_0aGB0gp6bJa9ZrBZ6FSbDDjDS7Dxvq_Q3XxW8wPX1BdVUxUhS7uyeuUovU7cFLBmPMNLGS0lVmtlIpK5RQt1srXSXtDF4wEPxCwobI4nptgNy966AXKwHqZhnfdfbSSRdJEFurdHeP_OVCtUn3kKVF8_abyYJ7bBM_bc9Sk49_aJPaQABfYmmyrYQfsopANUyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3986d93255.mp4?token=IE4EP1p1zp9fgDvQMzCdN-sPnIp5g7DC6ZA2Kx41lOeUWCXnEYjkaw43EHON5Vt3hapxqmIBF3Ou_JDofaZGqJ0BH8AHCOm6Mzz2d9LdmfsdCIzrhn0rG0XdE4uuge6Q4GDxFvFSl39Bc24GE_6_0aGB0gp6bJa9ZrBZ6FSbDDjDS7Dxvq_Q3XxW8wPX1BdVUxUhS7uyeuUovU7cFLBmPMNLGS0lVmtlIpK5RQt1srXSXtDF4wEPxCwobI4nptgNy966AXKwHqZhnfdfbSSRdJEFurdHeP_OVCtUn3kKVF8_abyYJ7bBM_bc9Sk49_aJPaQABfYmmyrYQfsopANUyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الزيدي يستقبل بزشكيان</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/naya_foriraq/81426" target="_blank">📅 21:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnHk7CrJaaeUNnjCWsSKlWCoAaobN3he0DJ-CLXoDqb7kHoAnmcJ1VZcKB2yYfO68go_ATQHfne54YBS1w7HggUko-ch6owrTw1Lo6akXkNzoFC1kCheuj1U18pCCgOiP7ZqVME4Mu05nl7lJQOF_KjVNxtp5a5JMSSC6KiKRto066XXQgsvWrIicszFovq5Dv7AUnA60-qK1wc6g2e7RLZw3APpkaUVrBC_LlaPQo9R63v0QMYfEoc9ezbPdyz-EeIY-u3YsG0RZ0ZZjHLLfPW9DBUIvg1BiM0vZ2Xh030FvArf94hprb70qyruSEm7N_3uIcdYUkPmCu27JQs01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزيدي يستقبل بزشكيان</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/naya_foriraq/81425" target="_blank">📅 21:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">المالكي؛ الفياض؛ والمندلاوي</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/naya_foriraq/81424" target="_blank">📅 21:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3796d4c299.mp4?token=TQwubCh2ME19K-yt3p4in7PNa9tRBxFYPDQZWhOh3GUxptX32brmRUSdOKDnpvHNT2EV-klTZqlFy0kX-5pFDyOlTknpRJz1RYUveSyisK2ujLfE7YmVIJNSHxEcAyODU6oFb05TuFVlDQwxU3kv1Q19oUsVBOyTaUG-PXwr4uFrWNeMS7II5BOw1GREYLUBuMxawuk7DGTSi7L3lz5iYr1lwhBbfTC_Byq5D3_VU6Thxz0eawua1_dTuVr-mA182rTaQU-4BCXD36wA0LgCRvK7_MnmX3lAJ5uSXo2yBzWKlBib66vsU32JQzi2bGY67WubmGiGAW-ojQJIaMs48w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3796d4c299.mp4?token=TQwubCh2ME19K-yt3p4in7PNa9tRBxFYPDQZWhOh3GUxptX32brmRUSdOKDnpvHNT2EV-klTZqlFy0kX-5pFDyOlTknpRJz1RYUveSyisK2ujLfE7YmVIJNSHxEcAyODU6oFb05TuFVlDQwxU3kv1Q19oUsVBOyTaUG-PXwr4uFrWNeMS7II5BOw1GREYLUBuMxawuk7DGTSi7L3lz5iYr1lwhBbfTC_Byq5D3_VU6Thxz0eawua1_dTuVr-mA182rTaQU-4BCXD36wA0LgCRvK7_MnmX3lAJ5uSXo2yBzWKlBib66vsU32JQzi2bGY67WubmGiGAW-ojQJIaMs48w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">التحضيرات الأخيرة قبل استقبال جثمان الشهيد علي الخامنئي وأفراد عائلته</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/naya_foriraq/81423" target="_blank">📅 21:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
ذي قار تعطل الدوام الرسمي في الدوائر الحكومية يوم الخميس الموافق 9 تموز، استكمالًا لقرار تعطيل يوم الأربعاء، وذلك لإتاحة الفرصة أمام الموظفين للمشاركة في مراسم التشييع وتفويج المشيعين.</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/81421" target="_blank">📅 21:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81420">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فدای جان پاکی که جان‌فدای ما شد...
❤️
🕊️
▪️
تصاویری از وداع باشکوه و تاریخی مردم تهران با رهبر شهید انقلاب
🇮🇷
📸</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/81420" target="_blank">📅 21:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وفد الإطار التنسيقي يصل إلى مطار النجف الأشرف للمشاركة في مراسم استقبال جثمان السيد الخامنئي</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/81419" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81418">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209e13531b.mp4?token=AiD13aUOVcPdBvJbDnPmGefzLVktGO2nt0TQmxuYLqW4WKLxY9VF87KcEx33t2L-n1f1f1erk12BusASbd76PVO7ls6gcfQ0drQoeU3P7r0_Zrf6wNzoAJv3hcBBRY9IAWa8gb78d-fjhDIyDSISuRoCzsPmgiJ42ZUGR8sqfm64WrH2MRYM-JczELSbuniM_E5Jw_VK0d3ffqkmLJ22OOHIaXbqTi5OuHucnYMMHVUF7Ufszh-e0EtLmVoE_IrTxSVUoJCAqpOYEsFToZPcQ-KkNXGB7ZLSGen351VIT8yRmmwWFyC29L8QRoQU7221Uh5qbPI7EcVKdSLMTnx_tbbE1EHkZIZZqkJwN87gyc6ufEZOS5SXrjcSeQOZKo3JC2shD_EOMkk86MoyspfpjeZl602gKzDg_LYazIopWYc_yvMjEQVTGPzmVNK-G3noepLXzzCS2U5u23iDSwE_KMLA8oYEgvMVlTx0EF9G6_Gr2oFDud5RD4Bfo--HSjumkk7c2T6hBlhtvAE9_w3MaTM8Mir4KSKEs_AxcECP5jl6cJuFKWMr9Qnx4wRhwLZHNom0J43Bru1mQvw3T-nDa2FmlUbo-sCAIviWoxP_XEXFJDwZlcVvZxPRg7_VfMTwsFoa0hpb8hNArSFEHr1VXmntWTFGviThXc8KkDDVQFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209e13531b.mp4?token=AiD13aUOVcPdBvJbDnPmGefzLVktGO2nt0TQmxuYLqW4WKLxY9VF87KcEx33t2L-n1f1f1erk12BusASbd76PVO7ls6gcfQ0drQoeU3P7r0_Zrf6wNzoAJv3hcBBRY9IAWa8gb78d-fjhDIyDSISuRoCzsPmgiJ42ZUGR8sqfm64WrH2MRYM-JczELSbuniM_E5Jw_VK0d3ffqkmLJ22OOHIaXbqTi5OuHucnYMMHVUF7Ufszh-e0EtLmVoE_IrTxSVUoJCAqpOYEsFToZPcQ-KkNXGB7ZLSGen351VIT8yRmmwWFyC29L8QRoQU7221Uh5qbPI7EcVKdSLMTnx_tbbE1EHkZIZZqkJwN87gyc6ufEZOS5SXrjcSeQOZKo3JC2shD_EOMkk86MoyspfpjeZl602gKzDg_LYazIopWYc_yvMjEQVTGPzmVNK-G3noepLXzzCS2U5u23iDSwE_KMLA8oYEgvMVlTx0EF9G6_Gr2oFDud5RD4Bfo--HSjumkk7c2T6hBlhtvAE9_w3MaTM8Mir4KSKEs_AxcECP5jl6cJuFKWMr9Qnx4wRhwLZHNom0J43Bru1mQvw3T-nDa2FmlUbo-sCAIviWoxP_XEXFJDwZlcVvZxPRg7_VfMTwsFoa0hpb8hNArSFEHr1VXmntWTFGviThXc8KkDDVQFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقام الإمام علي عليه السلام قبل ساعات من بدء مراسم تشييع الإمام الشهيد السيد علي الخامنئي في النجف الأشرف.</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/81418" target="_blank">📅 21:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مقر الإمام الشهيد في مشهد: تم تحديد مكان دفن جثمان القائد الثوري في مرقد الإمام الرضا (عليه السلام).
ستعلن عائلة القائد الثوري التفاصيل الدقيقة لهذا الأمر قريبًا.</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/81417" target="_blank">📅 21:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وفد الإطار التنسيقي يصل إلى مطار النجف الأشرف للمشاركة في مراسم استقبال جثمان السيد الخامنئي</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/naya_foriraq/81416" target="_blank">📅 21:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81415">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e42cfad2.mp4?token=mOU80ANpBqAphOqZlyuT0R3V0KG5KJRBRcdeeTbf2UefEbZGRKqvSjpqrHh91KG2Uma1E_EweDOYCMwtJ0k8s4F6CU4MxPp4IgZBJrNiMVCCDYTWx5OwjVJBp6RcsGpkPydGb8GpfECs4XNmXmW3ODtnv9mudRoUuN-KOmvG45ZBMdgnR42f4-D0v6WGBpA_sHYynWTgKyF2aDK81tZ6SalSAvmF6qeJdPC4WpZON1_g8QrrTpho_02OEDDgku8exHWw3BDmpIOu7lukRCxG_4JiAKoPwBaOq9eq8ei7onOV50feGotY_DrYmeWQGMdZvQTYvQDf_gRTmGyOkPm1HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e42cfad2.mp4?token=mOU80ANpBqAphOqZlyuT0R3V0KG5KJRBRcdeeTbf2UefEbZGRKqvSjpqrHh91KG2Uma1E_EweDOYCMwtJ0k8s4F6CU4MxPp4IgZBJrNiMVCCDYTWx5OwjVJBp6RcsGpkPydGb8GpfECs4XNmXmW3ODtnv9mudRoUuN-KOmvG45ZBMdgnR42f4-D0v6WGBpA_sHYynWTgKyF2aDK81tZ6SalSAvmF6qeJdPC4WpZON1_g8QrrTpho_02OEDDgku8exHWw3BDmpIOu7lukRCxG_4JiAKoPwBaOq9eq8ei7onOV50feGotY_DrYmeWQGMdZvQTYvQDf_gRTmGyOkPm1HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حشود بشرية كثيفة تتجه إلى مطار النجف الأشرف لاستقبال جثمان السيد الشهيد وأفراد عائلته</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81415" target="_blank">📅 20:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وصول الطائرة التي تحمل جثمان الشهيد الولي وأفراد عائلته إلى مطار النجف الأشرف</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/81414" target="_blank">📅 20:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4c5c8a5b.mp4?token=XOPNPWvlufMT_reGdIwI0ei4d0TzX1b_JuwVm2cM1deGfUTGBNV3puOXDGbb2YAcfqz3dqQ06-m0d7PEMmL3ks-FyLC7rZUdUF7fQqblkqxvMhR1K_TZA9Okgebxi8g1meJ2w1ABhN6xq5aDuO86msR80th98x-heGLL3FKw-DxpGhmpMiEUOcFCwHC1gxSofHgJHJdhlQV-y7Xo2XxozRov5hXTnIlbppT_DrT7FnIeYkUt53j0GxLymcMlRvLXQ5rCA-cdvKnTZjTh3d_FaqhxMP92wooo7cdCIV54AbGRAiyKfSbzQlh0E7FvUElRRk3kgYZmSZkLy3R-m4OLEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4c5c8a5b.mp4?token=XOPNPWvlufMT_reGdIwI0ei4d0TzX1b_JuwVm2cM1deGfUTGBNV3puOXDGbb2YAcfqz3dqQ06-m0d7PEMmL3ks-FyLC7rZUdUF7fQqblkqxvMhR1K_TZA9Okgebxi8g1meJ2w1ABhN6xq5aDuO86msR80th98x-heGLL3FKw-DxpGhmpMiEUOcFCwHC1gxSofHgJHJdhlQV-y7Xo2XxozRov5hXTnIlbppT_DrT7FnIeYkUt53j0GxLymcMlRvLXQ5rCA-cdvKnTZjTh3d_FaqhxMP92wooo7cdCIV54AbGRAiyKfSbzQlh0E7FvUElRRk3kgYZmSZkLy3R-m4OLEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال الرئبس الإيراني والوفد المرافق له لدى وصوله من قبل رئيس الوزراء العراقي علي فالح الزيدي ومجموعة من كبار المسؤولين في العراق</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81413" target="_blank">📅 20:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7301e1a940.mp4?token=DVC3vJoAXRAza_XOJAVaAF6KmQKEmiG9wFxAPUjjWqPmFXs_YRdH2aUOUUxh7c3rkmjkNMjqHA9hli72nx7_kjdVFqZOaeADUtyHp_VP6DCZ-mVDpUUZtL0seQDMQrv3_IjhI0KS0KDSXC3jbE7s9nE6TjBx-rSxZ_-256MQxk8UWebOJfXI8yod4KTeDxMZrVzdPuQR0LpLlcfJVsqSq9yFTL3EZJVWOKL7cz7qA53bicdafrqK4Wfslha37ME_MPSvJL451ECB8w4XEvjRjsLxOsh-juLGiUqyqQYkqV12LL9vVyhG87uFmeRQ6jgEnSDaFSdkgDqhVTraHFaM9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7301e1a940.mp4?token=DVC3vJoAXRAza_XOJAVaAF6KmQKEmiG9wFxAPUjjWqPmFXs_YRdH2aUOUUxh7c3rkmjkNMjqHA9hli72nx7_kjdVFqZOaeADUtyHp_VP6DCZ-mVDpUUZtL0seQDMQrv3_IjhI0KS0KDSXC3jbE7s9nE6TjBx-rSxZ_-256MQxk8UWebOJfXI8yod4KTeDxMZrVzdPuQR0LpLlcfJVsqSq9yFTL3EZJVWOKL7cz7qA53bicdafrqK4Wfslha37ME_MPSvJL451ECB8w4XEvjRjsLxOsh-juLGiUqyqQYkqV12LL9vVyhG87uFmeRQ6jgEnSDaFSdkgDqhVTraHFaM9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من وصول الرئيس الإيراني مسعود بزشكيان والوفد المرافق له إلى مطار النجف الأشرف الدولي .</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/81412" target="_blank">📅 20:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6922cd15f1.mp4?token=K50Ty2s7l_FZEe7nRmJAADVAvnRcC7IeoIQrZ__of4P4TmcQQsWCW55lezihNx6KeGIXzKqkEOuGq5Ht-4bFbu7r5xoXXafDFbH_OYSUYQG2p2MTsUsotYsKMbDGoWNTGXAC9eh16DO1HKhmveyzXM1RrVHWOD0qiTb-2U5vSWVgMa68GJV1zyS_px-4N-ivXfci35fv7Q4NKybzt24qw4XuV812YUYNOJj4mD6K3RGkZA30U_d3SRSlAvi9BcO0R0EIzK2flbl2C3h0OqyAERfUsjktjz_lJWIVhlNvHGXJ8c7PlFgMa7-pr_wxIeKShu4Lgbb-1a9ruF1OPxyIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6922cd15f1.mp4?token=K50Ty2s7l_FZEe7nRmJAADVAvnRcC7IeoIQrZ__of4P4TmcQQsWCW55lezihNx6KeGIXzKqkEOuGq5Ht-4bFbu7r5xoXXafDFbH_OYSUYQG2p2MTsUsotYsKMbDGoWNTGXAC9eh16DO1HKhmveyzXM1RrVHWOD0qiTb-2U5vSWVgMa68GJV1zyS_px-4N-ivXfci35fv7Q4NKybzt24qw4XuV812YUYNOJj4mD6K3RGkZA30U_d3SRSlAvi9BcO0R0EIzK2flbl2C3h0OqyAERfUsjktjz_lJWIVhlNvHGXJ8c7PlFgMa7-pr_wxIeKShu4Lgbb-1a9ruF1OPxyIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هبوط طائرة إيرانية في مطار النجف الأشرف</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81411" target="_blank">📅 20:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هبوط طائرة إيرانية في مطار النجف الأشرف</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/naya_foriraq/81410" target="_blank">📅 20:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
القنصل العام لإيران في كربلاء:
سيُقام مراسم الاستقبال الرسمي لجثمان زعيم الثورة الشهيد الليلة في مطار النجف، بحضور رئيس جمهورية إيران ورئيس وزراء العراق وغيرهم من كبار المسؤولين في البلدين.
▫️
سيُقيم آية الله السيد محمد تقي الحكيم صلاة الجنازة على جثمان زعيم الثورة الشهيد في النجف.
▫️
ستبدأ مراسم التشييع الشعبي في النجف يوم الأربعاء ابتداءً من الساعة 6 صباحًا.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81409" target="_blank">📅 20:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">السيد الشهيد يغادر مع عائلته إلى النجف الأشرف.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81408" target="_blank">📅 20:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVGdJXVDrpN7fi8E4SlvjZTTxBQn6SpEt8_tRaPunqhBxC2Cq8QR6LxsLxv_HXBQQceNg_K_izOhIhz9MqcUX_Au6I81sjWPrAnnVfKwzykOzjoKqmI_O4b7v0PmFDm4q64gNJ2C82r8TaXjQd41jqwttlIOt9i0LjbYup-id22SD66kLqQV9TWhZ3ZBAQVazLGmuLwuKVr-MypLi0S3yDElHiW4q_J1-qvST9-KWr7c3DodOCHltJfTRAQQY8cLGowLEz1aO1Xx2wh8ddKNn9kjwD2BFFG7okUWHdmZ2f81ArlEAWaFQfyxWWlWw5Asn1enou19hvCbkL8bV_Ellw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوموا لله أيها العراقيين السيد بالطريق الينا</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81407" target="_blank">📅 20:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db192e4e0e.mp4?token=XNFX4TwswvJtHGG2xtEyiU1aGmnUBq594z_EaqbMsDi9JAJf2KC5z3o6oLiJjmos7hIWq20U_disDVivQ1uQs2rSrMqSt3LP_VYb697dFSX12qEb4ibVh3vw-HmygwqKWKTQy8GBeNIFzwl5rPCR3n0N9-1izUjsJiZhhJ15B7fRZ0NS7Ll-lSDlkUE3BCCWzoRvomQ7jYc8VHQm6NvX5V7pxSiXuNeNArIu0SgHhixX8ly98gfUOwj9Ah-rNoqaBbreoM18ZLz3i45KLfjzQOj8Oj1-oXkJfq6vVv1ObEkiXXyO4JPEut4CSh9S_zYJ4dJDdSSNDMWdkdsFqoCthA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db192e4e0e.mp4?token=XNFX4TwswvJtHGG2xtEyiU1aGmnUBq594z_EaqbMsDi9JAJf2KC5z3o6oLiJjmos7hIWq20U_disDVivQ1uQs2rSrMqSt3LP_VYb697dFSX12qEb4ibVh3vw-HmygwqKWKTQy8GBeNIFzwl5rPCR3n0N9-1izUjsJiZhhJ15B7fRZ0NS7Ll-lSDlkUE3BCCWzoRvomQ7jYc8VHQm6NvX5V7pxSiXuNeNArIu0SgHhixX8ly98gfUOwj9Ah-rNoqaBbreoM18ZLz3i45KLfjzQOj8Oj1-oXkJfq6vVv1ObEkiXXyO4JPEut4CSh9S_zYJ4dJDdSSNDMWdkdsFqoCthA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوافل المعزين من محافظة البصرة تصل إلى محافظة النجف الأشرف.</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/naya_foriraq/81406" target="_blank">📅 19:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مركز المعلومات البحرية المشترك: 3 حوادث استهدفت ناقلات غاز ونفط شرق مناطق بسلطنة عمان وشرق خورفكان بالإمارات</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/naya_foriraq/81405" target="_blank">📅 19:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81403">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a94875ecfc.mp4?token=W6BKrXxrJca3Ynh0oBB0rxgY43SXNwDWY8FnXqpOtgdHFiNNObhpFeErIQfplGhewVS7wSdSGItIO2xUOy5Hjasp2WSqFu4mHWXHKnnM8I4loy8ikj1tP7nWmkOqPuR__vxWEwsk6IfpP24gzLQwE4_s5zI4E2ymKl6PfDUdD3XHzkHVG9E7NGonZtOtPNjd0mOySAZK2izgPA_iwLqELfFzYAx1uyIdprmKtPGb2Rg0wCuGZ2kuR6VHEgI466Zn7ijRk_XeHqgzI-9lZfIXrKn1wWCIatuv3pGvGDfSutbNgHfnFedmS3VMAr6pK4I0UaFYmB-IM11je7xUjLHykA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a94875ecfc.mp4?token=W6BKrXxrJca3Ynh0oBB0rxgY43SXNwDWY8FnXqpOtgdHFiNNObhpFeErIQfplGhewVS7wSdSGItIO2xUOy5Hjasp2WSqFu4mHWXHKnnM8I4loy8ikj1tP7nWmkOqPuR__vxWEwsk6IfpP24gzLQwE4_s5zI4E2ymKl6PfDUdD3XHzkHVG9E7NGonZtOtPNjd0mOySAZK2izgPA_iwLqELfFzYAx1uyIdprmKtPGb2Rg0wCuGZ2kuR6VHEgI466Zn7ijRk_XeHqgzI-9lZfIXrKn1wWCIatuv3pGvGDfSutbNgHfnFedmS3VMAr6pK4I0UaFYmB-IM11je7xUjLHykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول رئيس الوزراء الزيدي للنجف الأشرف</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/81403" target="_blank">📅 19:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81402">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وصول رئيس الوزراء الزيدي للنجف الأشرف</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/naya_foriraq/81402" target="_blank">📅 19:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اختناق فوق مونتي كارلو   تفهم ما تفهم مشكلتك</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/naya_foriraq/81399" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">السيد الشهيد يغادر مع عائلته إلى النجف الأشرف.</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/81398" target="_blank">📅 19:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81501b3668.mp4?token=BOC8k9kG2ImL_3tS6HiBb0Ymi0QbJLozq8hFMKD3JYrZMdIDM3NitXClZsqzMhbIQ5kEOV1j0apn1JCcx091gwpnW10e1BI_S8xpbZ4c2vqstd6ZPaSkGV8v6vZy7cnA0B_vhpso5fYvDDKXndsSn9IyPW2koM_bi-P0jWt3eksHMQAlnj5DzEXmen-E_4pu5bp66vlUPvGvq_KfVLGTUiUZmkR3UukfblRxFyFRAEBFDGn_n9_vqF1rraBXWZCMx1BL4S1Mm-lf-GjNDYIUifTouSF2csBPSL0eHdAcnVYlnw5sxyc6aVxOB6Rr9ZwlHM1RFjOoPMeGLr6M2o3flw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81501b3668.mp4?token=BOC8k9kG2ImL_3tS6HiBb0Ymi0QbJLozq8hFMKD3JYrZMdIDM3NitXClZsqzMhbIQ5kEOV1j0apn1JCcx091gwpnW10e1BI_S8xpbZ4c2vqstd6ZPaSkGV8v6vZy7cnA0B_vhpso5fYvDDKXndsSn9IyPW2koM_bi-P0jWt3eksHMQAlnj5DzEXmen-E_4pu5bp66vlUPvGvq_KfVLGTUiUZmkR3UukfblRxFyFRAEBFDGn_n9_vqF1rraBXWZCMx1BL4S1Mm-lf-GjNDYIUifTouSF2csBPSL0eHdAcnVYlnw5sxyc6aVxOB6Rr9ZwlHM1RFjOoPMeGLr6M2o3flw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جحافل الحشد الشعبي الجهد الخدمي تزحف نحو التشيع في كربلاء والنجف الأشرف</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/81397" target="_blank">📅 19:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اختناق فوق مونتي كارلو
تفهم ما تفهم مشكلتك</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/81396" target="_blank">📅 19:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔻
انفجار لغم أرضي في بادية المثنى جنوب العراق ؛ مصرع شخص كحصيلة أولية</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/81395" target="_blank">📅 19:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGw_MFqbJRGMibqq86wqhG-T78NAPyiRubORnBa2hYo2dairgVxEXR3HRJAUxcJQLvIeZGpU9QBJfTdoWsVjFTKpmRte5D7wiR1Ida_-G50Xl2CQ-HZ8Q3BH5y3ob2-KVLXUVWF04F09tczwm4FUDY6NbIEKfAVxJfszsxYhAw6EBJzY3YOaVzkVqEXE0ApZrj98yTfMCxK4GKJcStj5qqs65JNTc4jc5vpcQdiHKJqGmRjB_BKNGPF3UBcUN1_GofbhUon5DLkZXZGVpsdFENyKLX_7JfE5HYqeipr6QINmOpItctyZ9br2BZqTX_foF18xFs2p5IVIMDY6h-24Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5d_zZiznxZOHnHfACjfAaMdjrfQZUwpVNRnnAAguxg922CNxObQX6vTCqnw4qgnFaZcr3sz5zV6x4G1k_5A-EB6h5vrPtRxxuxf2lAj5sCkLaEIbxz3lcFSC6FEZDQRZ2AF7SwZXOqndVT5A90tdpqN-DjtzyjJOSe5f2NSzFOPFeREtuy6f8a3d-d9tpwR0mHHJ64cYfehhqO8_jE5rC8vCKT7YKU5E5LDPWZXEwrWPTbgy6iKm8EcFl1yXHxyrpwtImLUsWARADCScBORztepHzt5bLR82PGtmiULAQgdVdLU4BXqxOq77u02C_A236UXG48LrD3gdD6Q0qBMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYjbp5ohN3-VhKDO0N7u0GblZHfAbadqTLg5AHNInHi6L2ffOyDXy6N_oFHsJT42GFIxzTBuHjRpCUDISxvtq77MgXb5IUyTuyddZ-vCN6IaKLP-oh-m6KP2kvBzK4-RlBILE_TTSEdre9KfETiqk9waGMjy4QWdEBZUmQ3rQSOOn_3J8OW6AO1WWQ12IbN7UHo8UUwYoA8RFIZ_bC_FOZ-sLuvdESh8yY3l6oBTT92QbUFjVCPfEGggTos34HMJouqv9hnYpMfI9q9SRE0i5CkZXM8miaJD7Oxn4HXbdqecF_hqyizk5usrkSTnYViwyaRES5-IHu2vBNGONby1gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0WFaBoWMmqvvpLa_z7rt2m0L75fkodoN1dyDHqXvGEsSXqjudUCWGOP0mKgAoQIvu78K3kCkowg1iUnKbPsvDPYuV7m9nAyqlE1gVOqBKI5tOrVBrLpj82Lgi6Bp2W1OaAglOhcwJRo9byveNfcEAD-MbUWqtv4WNRUy59QFE2VyfjiONi9C4vhe6X1LdVavzoZdYbC3-KJP391A3x3GA77ePIjObmlXU7zUl7H3EvfckpJzMYVH4zGqz8U2V7xQpGGJFO62P36YMjeH2_xl2_2GBSvYOR2wwE3HNV8gBC9lLcwa9G2Dfq39IWO-UuDxA_nydS23ygfb6liqUSi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tlretdsm1aGp2LvmMAkxtf4UMm671klvqxKaIAfBPBD2l3MMtMpuj-XjfutNDR7nu29mRbFhZ9vVrHzOjw0j_EhLxCpesvOkdFN-It7MTmJy_lmnmwmNTW3R9Wg3m8HcDqbYUFuVFj8I0BFEtlSiu6GbSZVtgASlNl4Tgn7WAXff5BQXMLfiEs1YtePcdiMJmzijRER3x2zmST9vHVtmTuDSdQFVq6XggoNYmjTvuqlFVMbhjlxlxL8q8qsvO520rEYr_egaDAwQ5HTcOCBL0_GvrIzbdO-p8fwSzNB8fm0hk_-CAFn1WOqj4nZS74drqPeYhbD-GEzqVcVfVh_rhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">أعلام صهيوني أوربي : شارك اربع صحفين أمريكان بتغطية جنازة الخامنئي اغلبهم مدعومين وهاربون في روسيا يحب القضاء عليهم</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/81390" target="_blank">📅 19:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b2d800e3.mp4?token=ofY2NjiNnPbyonqO3JCyX_AvxbyttdR5MJWOTEMJnAv-ITYlyov6fAMZFAeX6mSs4eIKcjuGj1MRoiPuCkEJkE62HVILJ7BRcMpB46keaENQmYrfpFxA5RH1EAwUszqg1ZRUodwQAuAOZ8O9BiXxp74PGd5_8SKN-j7QPSES62-Wddc_wNnYAG2Lisikeg1zb_uCRAdk8uPh9J_CSmO-YCpaei8AJ2geuhF4i6IuzZhD4bJvTKsxVtUfADI2n9j3OjOBuroVDyeAjOBqQw3W3Fa76n6QewAKPDt0Hd6PFn5zL7LcGrISpfhGxAxBMc3eYkeJN1xo1T6Ox5rS_tGBOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b2d800e3.mp4?token=ofY2NjiNnPbyonqO3JCyX_AvxbyttdR5MJWOTEMJnAv-ITYlyov6fAMZFAeX6mSs4eIKcjuGj1MRoiPuCkEJkE62HVILJ7BRcMpB46keaENQmYrfpFxA5RH1EAwUszqg1ZRUodwQAuAOZ8O9BiXxp74PGd5_8SKN-j7QPSES62-Wddc_wNnYAG2Lisikeg1zb_uCRAdk8uPh9J_CSmO-YCpaei8AJ2geuhF4i6IuzZhD4bJvTKsxVtUfADI2n9j3OjOBuroVDyeAjOBqQw3W3Fa76n6QewAKPDt0Hd6PFn5zL7LcGrISpfhGxAxBMc3eYkeJN1xo1T6Ox5rS_tGBOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطار النجف الأشرف خلال اللحظات الأخيرة قبول وصول جثمان الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/naya_foriraq/81389" target="_blank">📅 19:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f302a38eec.mp4?token=XbkxT1pFb6XrK4ZV74WHZeSKI9nJ0uKvvqmpGY0CT2pLZHa10UxDSvKOTd-kOrBQ86woOwSKESp5C4Gbzr5j9CKDbYIwt89vCg6OAPoePwiHw9o6G-IB-vFmcS8n_8JrUpGk7i-xYlaPvORIuGc_nz3sz9SiUNKIIwQ3iG9CL9d81PK8_uhkdxijUwk9lijqxs6AM4Bf3B43uRtIkoe0hz9jtvZKuTqWGCvzU6uYH7VQDWrQkoGEqgB9__tlaHP389HtZYeHVApfRRBLTXsm_RImWOkm9lenmaHxsvUGkZQ2V75AocDXpP_Yu1KKURBIftqsyGPHZSebRSIQC1gHmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f302a38eec.mp4?token=XbkxT1pFb6XrK4ZV74WHZeSKI9nJ0uKvvqmpGY0CT2pLZHa10UxDSvKOTd-kOrBQ86woOwSKESp5C4Gbzr5j9CKDbYIwt89vCg6OAPoePwiHw9o6G-IB-vFmcS8n_8JrUpGk7i-xYlaPvORIuGc_nz3sz9SiUNKIIwQ3iG9CL9d81PK8_uhkdxijUwk9lijqxs6AM4Bf3B43uRtIkoe0hz9jtvZKuTqWGCvzU6uYH7VQDWrQkoGEqgB9__tlaHP389HtZYeHVApfRRBLTXsm_RImWOkm9lenmaHxsvUGkZQ2V75AocDXpP_Yu1KKURBIftqsyGPHZSebRSIQC1gHmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر لقائد الثورة يغادر الى النجف الاشرف برفقة وفد ايراني رفيع المستوى يقوده الرئيس الايراني مسعود بزشكيان</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/naya_foriraq/81388" target="_blank">📅 19:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5bd2fe9d.mp4?token=kptsrcbgihL8XalhTohbVRCbIQvfPOoEheVQ458Jt2E5VOcB2qV7ZEqohh9lUMINAJVkdi-Dt5ZSx59fG2Qf3MnNn_zvx_A2k6wQnTn8PSLdD3NITTcpLOsymh8-8_KgvmlwbPbyKqAaoKyvd8BdVXB2_kqSrjD23e6FLta3oFPyPeXsx86c-ctpDXKuVyp7H8hWBlvtvrBpHtDzBNGHGav15C2kri7iTKu9gKcHsuWdh2QP40j3__zSAWFj4o30HSNKZpdyErt8wxINkI_LH3l4Sgx2Jm4CwFh44aXcFnENcHwsLQ0_l6_qHTWZ7G6m30htnuQYqPAtZqKkvkMorlPCyB0Ka7MXnUqFkLqbp20EDobFk6H9AwmkbCBYpO4O4-_aoq7zk6kUQoGPV0cIxDIeogrHUeG2h0t1blRkg6pDDO9IfQauxvItlvWHH1P4oltZIM8GnMNS5KWVx31xzk8-IJ1lvPhBCaTU9ocyng_kR4cuYeZGENk8lnHi3i3KbEOFDlwYOCFEItgkB4HvTGadNWX1fJXMhGhSn6l-7sdoi7ps6F_nJgoY2IK3WOZZIG4aIcVl9lz5-_OuEd2LhY7Hy92szALBDhsXj_j1jRogOF8-wmTgkM4ljpyLs0yTorHrepT_uzKt8hKImQLvVqTeZm0F5siOmcS0SHzKf3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5bd2fe9d.mp4?token=kptsrcbgihL8XalhTohbVRCbIQvfPOoEheVQ458Jt2E5VOcB2qV7ZEqohh9lUMINAJVkdi-Dt5ZSx59fG2Qf3MnNn_zvx_A2k6wQnTn8PSLdD3NITTcpLOsymh8-8_KgvmlwbPbyKqAaoKyvd8BdVXB2_kqSrjD23e6FLta3oFPyPeXsx86c-ctpDXKuVyp7H8hWBlvtvrBpHtDzBNGHGav15C2kri7iTKu9gKcHsuWdh2QP40j3__zSAWFj4o30HSNKZpdyErt8wxINkI_LH3l4Sgx2Jm4CwFh44aXcFnENcHwsLQ0_l6_qHTWZ7G6m30htnuQYqPAtZqKkvkMorlPCyB0Ka7MXnUqFkLqbp20EDobFk6H9AwmkbCBYpO4O4-_aoq7zk6kUQoGPV0cIxDIeogrHUeG2h0t1blRkg6pDDO9IfQauxvItlvWHH1P4oltZIM8GnMNS5KWVx31xzk8-IJ1lvPhBCaTU9ocyng_kR4cuYeZGENk8lnHi3i3KbEOFDlwYOCFEItgkB4HvTGadNWX1fJXMhGhSn6l-7sdoi7ps6F_nJgoY2IK3WOZZIG4aIcVl9lz5-_OuEd2LhY7Hy92szALBDhsXj_j1jRogOF8-wmTgkM4ljpyLs0yTorHrepT_uzKt8hKImQLvVqTeZm0F5siOmcS0SHzKf3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انتشار واسع لقطعات الحشد الشعبي استعدادًا لمراسيم تشييع الشهيد آية الله السيد علي الخامنئي في محافظة النجف الأشرف.</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/81387" target="_blank">📅 19:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5VNmBVpK6xUJ3CX8G8uoD7iiBvEcvAWE-Lx8M1wi0S5pGTP2qEbYfENxg6M--xSXLYvq6thZpl_UJvQsDeuJZx2SV1p7chzTx_F0xfg0i2h-BiyKIpYHvybYAND-hKsNRFPoHVTmVNXJMCIMjKn0YALLkpSVWQwnit8-gHRyF4dgRDuy0KpzUbJ15bUZ745_tUexQRs5fgOdwe_DF4V6pGS46zyqxq9W0uY0lQeMhNVSh5Jr2g9lLDePVTSbRFo0rzXLxCgFwQ5mWxAWT58JvJQRTFa4ouj70reyDAvJDQo58riUSmlP5u08icefjs_mWQ4-7eJTg8EJ1NnoZKC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
دوي انفجارات تهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/81386" target="_blank">📅 19:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
الحشد الشعبي يباشر بتفويج المشيعين والمعزين إلى محافظتي النجف الاشرف وكربلاء المقدسة للمشاركة في مراسم تشييع جثمان آية الله العظمى المرجع الديني السيد علي الخامنئي (قدس سره الشريف).</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/naya_foriraq/81385" target="_blank">📅 18:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هيئة عمليات التجارة البحرية البريطانية: تلقينا بلاغا عن حادثة جديدة تتعلق بناقلة نفط في مضيق هرمز</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/81384" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e78EhVB5OcRLfYUDOKI6o6G2VvOacb0O8RA0fAhw4feUSzQh6-hicfTOhotHpDHSVEXPQ-6MGR2m1SNayMuVCNu8M818r82Sco6654aEga9e-EPFSomUCScB_VJeZMkrZl78m0z6GV74ShSoFZqBd0N5K_idLmJPZ2Yplbu5IT12fMIQyJFuQQqVy-_pV14jNrNiBT6f94EJgNF4X3mBJ5MrjS1hc8yXtbTijyUO2hiNy3LIOCQ9KBY9suw6mWW903WpSSDeGxFSTyAmYNkz2bGkOJV7jnN-knmrxGrPmhx-LD8MxNV2DbHGEoJTxdYSEcu21-C9HmZ52dGlayZ4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMkSx-frD3DlaFFwkta1e2WOq2TuvgLQBRVJa5wiyKmp60ZBTUuemvbyzkLlxIHPeX8c6q8YvLE-fHPuhoDwZg06ofzIkMKFQaZn3_fucX698obecwLEmMSyMlz8rr4FmasWOJQDqQMOAfjhoGJVBw3BbcUszfoa7LExgVgpLnne4hDthdXMMYQkhLOQ4grHo7Hq_oJeFHTDvzPlNkS0LUhWbdAX-lmPKvHrUuTpv9vXsnggxuhdnMF7ExiT9jDJ0V9FyfQiI4Aq-pYWNBtKL0ojEpQYJtYRlPaFFP5Doam8SMz_KA-2ULDs__EuQgUK7BQ0D7NvkRJFr8Q0NDdV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anilszGjNVeZ-Ii478yI65VcsBVwSVx70EJ_pIoAD77CDVp0ZO_xHzYe-AxDNRxjl4P_1iky1Hbpb5qVhduB5cmRrIIiKFuKVkvvP1RlM-TR3Vl22N4jXWfM1NGMzU1AssiyjJ_k1pbL500ecNb41oJRpvxHPguvv1nFEqHVu0trKxDHE0VSnDxUwHQXmsUpPcjRZKVW2jSasF_Uiy5Ft1B2ionty6W2MErmRph2QgDPf1rXvMTgnYR_C4ptu6xo-Prc-zXXA8WiHVayKZxlTokADd0FRxecvi5PF5lG5AsNXwFKkCI-v5dEvYUCYrNFNI5jgFyMfnPOUiwkGQ5yKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
شوارع غزة تمتلأ بعبارات تصف شهيد القدس السيد على الخامنئي.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/81381" target="_blank">📅 18:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be17933fd.mp4?token=A0Hsf-cqZ7JjkLtUYCsexOA05JTJyAqRddi4dt8sjo_-_AvYbnHS67oKAK-kauCAnTCxnD59Q-ofFJ0HDQxpmc-ntxYbj0_WFDHx_2Rkil5hu23ZI9BinO2bfaQFYGzWvPiw6TonG2e9xv5Ih0gacoS82_7af99Udl972i9UTjqPER8hTIJ3r5XRp9w4DLYqSh92EOCAos-j6edTb2AoK_S2MSDqBC3r3tsqDCYTZC_FvnpzmZHb8_WIBS3EqRRpZOHkg3u-ZxlyI6xyaH3yzVAcShu-ixkjLzmWksgwyxq1rWDMla4XI0Z7xG9aQzTGqoF1MNXFG1lKmd9rObYywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be17933fd.mp4?token=A0Hsf-cqZ7JjkLtUYCsexOA05JTJyAqRddi4dt8sjo_-_AvYbnHS67oKAK-kauCAnTCxnD59Q-ofFJ0HDQxpmc-ntxYbj0_WFDHx_2Rkil5hu23ZI9BinO2bfaQFYGzWvPiw6TonG2e9xv5Ih0gacoS82_7af99Udl972i9UTjqPER8hTIJ3r5XRp9w4DLYqSh92EOCAos-j6edTb2AoK_S2MSDqBC3r3tsqDCYTZC_FvnpzmZHb8_WIBS3EqRRpZOHkg3u-ZxlyI6xyaH3yzVAcShu-ixkjLzmWksgwyxq1rWDMla4XI0Z7xG9aQzTGqoF1MNXFG1lKmd9rObYywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أهالي الناصرية يشدون رحالهم متجهين إلى محافظتي النجف وكربلاء المقدسة لتلبية النداء والمشاركة في تشييع الولي الشهيد.</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/81380" target="_blank">📅 18:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036c96ce36.mp4?token=nKAO2oaXgRrRdkizWkd2gQhPe6-a2JmYrexXx9qlXUQ2ZX1y3hbLRiYwCeJbtGeCklUB5vlECIcKcERV4rOzmqoJ8bFaLiZqEH_Tm-fVrgAMzOHXi0YfREYdwuE2OjIpPvkpIexcx-iBC3qQMDYvZrAFqd0WDMLxgwG7Va6kcjPnJZkUojCxGTFrI8xkc-XFYgokGvWxos4dWOR7r6lzu0kTRu1CwQEXWLnibsOQm_9BHghuTSiMfOvgPI4CpQWGezhxU2ddd-1tCr7oXmz8NizRlscMDMYvNf3eKITto-10MTuNvzddMU9e4sSr5YzjdbmTapSCuylZegv1jfKn4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036c96ce36.mp4?token=nKAO2oaXgRrRdkizWkd2gQhPe6-a2JmYrexXx9qlXUQ2ZX1y3hbLRiYwCeJbtGeCklUB5vlECIcKcERV4rOzmqoJ8bFaLiZqEH_Tm-fVrgAMzOHXi0YfREYdwuE2OjIpPvkpIexcx-iBC3qQMDYvZrAFqd0WDMLxgwG7Va6kcjPnJZkUojCxGTFrI8xkc-XFYgokGvWxos4dWOR7r6lzu0kTRu1CwQEXWLnibsOQm_9BHghuTSiMfOvgPI4CpQWGezhxU2ddd-1tCr7oXmz8NizRlscMDMYvNf3eKITto-10MTuNvzddMU9e4sSr5YzjdbmTapSCuylZegv1jfKn4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قوات الحشد الشعبي تنتشر على طرقات مسار التشييع لتنظيم المراسم في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/naya_foriraq/81379" target="_blank">📅 18:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
إعلام إيراني: تقديرات تشير إلى مشاركة ملايين الأشخاص في تشييع تاريخي للسيد الشهيد خامنئي في محافظتي النجف وكربلاء العراقيتين.</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/naya_foriraq/81378" target="_blank">📅 18:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bu7PpNjYdQYnud_V3EDCXLoQVzm2OxiquxiAdO6POTcw6OdvxfAEuqRZEsE1g7hmmyyln_dCRjuFgmEJjUB3HFeha2bsI__LV-YUn-NMgN8LdanOa-cFefzdK9n0OwnP4Pvxu6rZRdm__Fs8WN2qKMLtriv4NmquKTZc7DGjsar4PlUpDiw-UmY-0IRvvhe3UaYyehASyB3BLymM__RC5UbWi0y5JgwvgUBquB0cgN1fk1SkpuNUQXh252-UNWZuLF_c8qZU-QxCSvBc-N6l5b20vSkshGSG0sIRLAqOazF4_D65nLX0xIze41aRXDns3AV85UYVnAHW2HPSdDb5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Guwokqx-D31oyMkWk_zK-b4oq5Kbwx4ZMP_TrrMJkfs4QvWxlIL48fqa4e6icUhEhk6e6ClboqMcHyIb8tvU72zQ3L6drAAE8kDijNNzAwgM6yZH8eH_s5u4v4qhFtA1loC74b-dGRLbf9wqeatJMOzDg5JeZ2oT9IIFwSrXfDd94JFxvXKr5N3Tb4cypKTK1vGUhGt5pHYg623q9E5JTaaTIoMOHflMukI0u9JteZ5wl0lfhk453y6AcMkoWGsTtZzn428fwl6VQVWo03KCmHytUYGZwLJxm0TdPJToCWf_B-lxZUAPx8XcGYqJ68OdM3aZCseKYLfd_8sFHFYTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/idWjzbwPhszLLMjJQ4j2ZMzyxWJebVuQ22Saa99CvMXpWFhtxsFfY0O83-Es5LhRH5k5lWmpcARtUHfWbH5cYRfAkPEfMQraR7sMe90V--Y3DMv810YeAwLiQsiCu-DDg_h1KUxsotPYQQkHbP0wRoMG28j5v_NcrgS3041wHAkCn1EuaLStWQPuBJ7HdVEN_KnMQbbWI8b1niTmrTYFUpnzRUGu2Lb5o-yTV92yjDCOcXdBysnq_ciw0AwiC1dKi610YRW5qqKdwBmMCYMZ2Jtc60-6m0Mer9xHihdhh1CmV8Qc73E9Dy61sDq2mJy9txu2LrmXgvLiZF5HR7uG4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
قوات الحشد الشعبي تبدأ بالانتشار على طريق مطار النجف الاشرف الدولي بما يسهم في تأمين مراسم التشييع وتنظيم حركة المشاركين.</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/naya_foriraq/81375" target="_blank">📅 18:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edQryc8H1c2vCrXrYHhqeQw3d2wVp42SO9AeG7DTWuQaGQhOJ95uGIl4FHoePYTjciJzitMZC2_Bzg5tjT8USB-IgWI1VFNgJ-RK3Wnv-d48VDjv7UJOOqUtzO-5KGRfooRAgEBQeNAAkXJFS0rmfWcyj8-Bd9qRGeFhvwLnrKfhWxLmFKwon1Iyg0uxuO8x8-b5gP4UjhUXQ7U9WZYE1mnQUFDNGekrmRdh3nMby2yKERWt0CHRbMfEnKUmzmR5QAdYXbUMwSbsNjZNhdIxpNbiGZAk7l_K6trC7mV5IwwKimJGwsLCnp0Eng4F7MCB5G-GwhHNQTooyy2rGte2cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اللجنة العليا لمراسم تشييع الجثمان الطاهر للشهيد القائد السيد الخامنئي (رضوان الله عليه) تعقد مؤتمرين في النجف الاشرف وكربلاء المقدسة لوضع اللمسات الأخيرة والتنسيق النهائي لهذه المناسبة
​
عقدت اللجنة العليا المعنية بتنظيم مراسم تشييع جثمان الشهيد القائد السيد الخامنئي (رضوان الله تعالى عليه) مؤتمرين منفصلين؛ الأول في محافظة النجف الأشرف، والآخر في محافظة كربلاء المقدسة.
​ناقش خلالهما ،الدكتور إحسان العوادي، والفريق أول الركن الدكتور قيس المحمداوي، نائب قائد العمليات المشتركة
اللمسات الأخيرة الخاصة بهذه المناسبة في هاتين المحافظتين والتنسيق النهائي لها.
​وشهد الاجتماعان إيجازاً من القادة الأمنيين والجهات المعنية؛ بهدف إحكام النهايات المتعلقة بالخطط المرسومة، وتوزيع المهام والمسؤوليات بالشكل الأمثل على جميع القادة.
​وتم التأكيد على أهمية تكامل الخطط الأمنية والتنسيقية والخدمية بما يتلاءم مع مكانة العراق .
​كما جرى بحث التفاصيل المتعلقة بالتوقيتات، والمراسم، وأماكن التشييع في محافظتي النجف الأشرف وكربلاء المقدسة.
​وأكدت اللجنة من خلال جملة من التوصيات على تطبيق جميع الإجراءات والتوجيهات التنظيمية، ومسارات النعش الطاهر، وآليات توافد المعزين، بما يضمن انسيابية المراسم التي تليق بهذه المناسبة الأليمة.
٠٠٠٠٠
اللجنة الإعلامية لمراسم تشييع جثمان الشهيد المعظم السيد علي الخامنئي رضوان الله تعالى عليه.
7 تموز 2026</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/naya_foriraq/81374" target="_blank">📅 18:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏اللجنة الأولمبية الدولية تعلن إعادة روسيا إلى الألعاب الأولمبية بعد ان خرطت الوضعية واصبح التدخل السياسي في الرياضة محط سخرية لجميع العالم بسبب ترامب</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/naya_foriraq/81373" target="_blank">📅 18:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouTJHfSSabC7xxBs21inNfgnTsDMRzZNQbZ6pO579m8eztmnSYGjSrQlSYMnj2PtgzCkVHnt7JWlmUQ9ZVy4qPyolBuNa_ITK2kCYbp6_JWhdPnrbjlZpKf-vTdqKQjdkNRURMpKwsf0LE7OwAD-D_4-Gbp-ETTPClubnHEUeaEB5-XzvpXbCHIuyKE8d0Rzwf5GdJiY9IBxQ0_k_8CT6h0wjmmRzKnBa7PNMdTQyJRF7ObS_VANOhiHQbcsx_W5O1JrjQndHDlEZm41XklLvgv1YvYSXhBs3MOkZX9MrLW_nA6ngkZL4B6XrJKqdLuxrvhxaaqSVOLztokXh4l2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتفاع اسعار النفط على خلفية الاحداث في مضيق هرمز</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/naya_foriraq/81372" target="_blank">📅 18:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇾🇪
نائب رئيس الوزراء اليمني لشؤون الدفاع والأمن:
لسنا عاجزين في اليمن عن الاستمرار لـ10 سنوات أخرى في المواجهة العسكرية إنما نبحث عن إقامة الحجة، رابع المستحيلات هو أن يقبل الشعب اليمني باستمرار حالة اللاحرب واللاسلم وقد ضاق ذرعاً بهذا الوضع.</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/81371" target="_blank">📅 18:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f639792de.mp4?token=UkZm1GOt9oC7wFnOw0ihrJLobMjVut4mNG7xWSGqf83NBVNz58bBFLjfQeSbuB1yibdGFFGX2toCZbCPIB2lyWxypGhIIGYhechelyFZS69_f-rldkOYSSggB5NmIBo931COliwGg4YC_E-a9OGiA-M_Hz70D95KwhXb6cutPVzehyvmIfRwH7xhAA2JBYKGGENP5CfVmFB-fBshaI9Vof6GQi6M5Od_XYig9MJeQblyAHb9JQXDQ8hZe9rFTZxdqKuvzymwOrIxt0zOTUn88U_z0I_yd4wLucmLknMgEblU9eyiQjXezbTxx48IK8cqBIwf3a6AA4TwScHyoI9U5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f639792de.mp4?token=UkZm1GOt9oC7wFnOw0ihrJLobMjVut4mNG7xWSGqf83NBVNz58bBFLjfQeSbuB1yibdGFFGX2toCZbCPIB2lyWxypGhIIGYhechelyFZS69_f-rldkOYSSggB5NmIBo931COliwGg4YC_E-a9OGiA-M_Hz70D95KwhXb6cutPVzehyvmIfRwH7xhAA2JBYKGGENP5CfVmFB-fBshaI9Vof6GQi6M5Od_XYig9MJeQblyAHb9JQXDQ8hZe9rFTZxdqKuvzymwOrIxt0zOTUn88U_z0I_yd4wLucmLknMgEblU9eyiQjXezbTxx48IK8cqBIwf3a6AA4TwScHyoI9U5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد للنعش الذي سيتشرف بحمل جثمان القائد الشهيد للثورة الاسلامية السيد علي الحسيني الخامنئي في العراق</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/naya_foriraq/81370" target="_blank">📅 17:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81369">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هبوط طائرة ايرانية جديدة في مطار صنعاء الدولي لكسر الحصار عن المطار</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/naya_foriraq/81369" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN9wJ_Bt0nUnq5VNM8otkFeSJZWoHBLR6VeVF9FXNGaP87he5kypC_2Ts_ye1tyO4lReXAY7guHFHV9omYg38lS8o9AC1sZdAoVEz7calrAgef2jEPXW1admANEOgiblBtr2w4a5iHL15Cx-UPEgxSRgCTzZhC90PlUm9P1rAtnVKo3bnckSszECTKAGEMjU3aT9KyMjdiKr1ZskkI-KvmWaXWZWfh7mlCcmgZYE7d5NkbicodC1a89nsYL60iezlZLn6fJYYjQb9Hd1zWlD-ftYp4JLMAIftoRX4VrYDhvpuG5f5C89RXJUc9eDPYGg6oxG41slfBzc9QnqyhyVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
برنامج تشييع الإمام الشهيد السيد علي الخامنئي (قدس الله نفسه الزكية) في العراق
▪️
#قوموا_لله
#تشييع_إمام_المستضعفين</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/81368" target="_blank">📅 17:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ايران تعطل الدوام الرسمي في محافظة ايلام الحدودية مع العراق لاتاحة الفرصة للمواطنين للمشاركة في تشييع قائد الثورة الشهيد بمحافظتي كربلاء والنجف المقدستين.</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/naya_foriraq/81367" target="_blank">📅 17:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية إسماعيل بقائي:
القانون الدولي الإنساني قُتل خلال الحرب المفروضة على إيران، إذا كان الأوروبيون مدافعين حقاً عن القانون الدولي وحقوق الإنسان فما كان ينبغي لهم أن يقفوا متفرجين أمام الظلم.</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/naya_foriraq/81366" target="_blank">📅 17:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHB8fJeCJEPJrqdmeAvad_jItcQ6wHs4-mp3x_OQRHKX49bwjQcapK963HCnAMFjT8nP5LAoKEnjXeL_ZaA8BP2S50uRtxfkIuWXFd5gZv-JWGl14hTcpiWjf4tnKqdDUcIJ_HUSaj8agjSuN4pPyVAGm_JQO_dpFanPSZmFI9amnNgpICxDTgNI3SWh3IrxIv8OYgVz91jjwNvtpgx1jnNpTFU_s4Qct2e-gPxYGRSYKl4X-WxY5xJNUr_98CNa3kcCobpaatc_MGH48oZxT5YgrzO6wZMMECbgTwEKgcDPPkkNJEBr197XnLXOe2dCfG3kHONKxnzhrm_4nHkpuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في أرضِ عليٍّ… يقيمُ علمٌ، ويُشيَّعُ إليها علمٌ،
خوش امديد سيد شهيد علي جانم فداى رهبر</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/naya_foriraq/81365" target="_blank">📅 17:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HM5KLthtCCGteTlt3QpvmCRK0xzGhgY86dgHE0Dj5f4VN-xEOrimz9SB_ZZAbExEyCvJmHB8jhlzkN8V2qdksDarOZzyNFy3UnYnEgWNc-5DH2UvqMom5b8IMD2JEtahMUnNhu1c7oqczj8TVK_XyI7EqSjpsKO_oEUgIpRP43lbiF_0xvrR5ynVf-KL64iaXm1VwozcD32wsvGH8k6PPzQNJNDaAp5u7YzkLjLXE3m-W-B3qAYiDMYgrD7D2oqjq-bsegIjBnPqg-G_lTtbsOB_dT-VFLvy-GI3e1gmQ6B8SbyY_E_JRkSVYxB5YNAms6wuUDbsU4CqFd5uOyHj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFPTEvcwBQ-ZYquX3Fqkeo69iOoTHaxx7X_x-tl5BOcdlJgNXSpKIEtDapFYw_BMUUCIhF1SLvzgdfX8mHcVNo5lxcPYHLYXXN1y4mh4ffDoBASARBjxS2F95lna3WYi3nAFTTJoK7r1H8vVFn6oELKuEdVLns2Y0mn81avBEnuETNR7mp_OHVgNlckNKldF9WVikuWS1Fr1HuSwisPyxsTbA8Jj59idoGBMZRxGHOvJyISF9c6hxegsbP9BhFuLbhqCbrv1RcT3BH2V5CY5eTUIbbDsUw-vzTkJ2pfwzvECBpdjrKKRbJiL1idtodoI-YMkLbjXB6TF9kkOXeXIfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
مطار النجف الاشرف الدولي يستعد لاستقبال القائد الشهيد للثورة الاسلامية.</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/81363" target="_blank">📅 17:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">العراق يدين تفجيرات دمشق</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/naya_foriraq/81361" target="_blank">📅 17:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
هل نشهد اليوم هجومًا أمريكيًا في جنوب إيران ردًا على إطلاق ايران النار على الناقلات في مضيق هرمز؟</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/81360" target="_blank">📅 17:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81359">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حدث امني جديد في مضيق هرمز</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/naya_foriraq/81359" target="_blank">📅 17:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSp_MJ8np7_1tDZS3QGPwkYDEcSaTAeN8f85GsUr1scHECPaSBYMcKVktF5tFlOFz4zh6vR4XpEfxM8gsx_Q6dLrYZEJSd4v7YGww8hQAOHDx-HNRyJbpGdyJA3dAmtdH-fudAnfcKA2sd2j_2sV4rWE53gtEmDeiFoMAsZvB7ymgWST5q_9z13vo8LJipmB1dLyYzPkSkhL81SA4RSM6Cvf1XLnVHo86Zo5ox8_Y9VWDrB6ZYX41pmt6sm-inbl0EDydXk5Tq3eD71XyQ-A_PB1P1MJwa37bn5RSyF-ee2jWBUUYRl9zl6yZC1eZEka_FY82HVodG6liM4PmPkppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني جديد في مضيق هرمز</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/naya_foriraq/81358" target="_blank">📅 17:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
قامت سفن تابعة للبحرية التركية مؤخرًا بالاقتراب من منطقة تدريبات كانت يجريها سلاح البحر الإسرائيلي في البحر الأبيض المتوسط، مما أدى إلى تعطيل التدريب ونتيجة لهذا الاقتراب، اضطرت السفن الإسرائيلية إلى تغيير مسارها.</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/naya_foriraq/81357" target="_blank">📅 17:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قوة امنية من بغداد تحاصر مبنى بلدية ناحية نفر في محافظة الديوانية جنوبي العراق وتلقي القبض على ثلاثة موظفين فيها</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/naya_foriraq/81356" target="_blank">📅 17:19 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
