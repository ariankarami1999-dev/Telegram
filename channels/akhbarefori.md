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
<img src="https://cdn4.telesco.pe/file/daod1d4Wue_iz8u3xmlOfT_TLsv-Qre6VeXckLwOpN14gi2VUcevQHE2_R47G82mZ79MFzpNwmwUIzybp7zh-xP7RaFK3OV3eTra56fOJYc0kgFOO_UZ5ZLIpCNZ0nuLBwgLosptUU5PjtIKZWTsMd7IbV_n99ns8wFJC48ufb0Vr-WphB_wvq1vf2pvMGRMVb0ljVfWxS946g7Qf9K4vXb64gm3tsMImvBR7OlNp0sYMsxVtWw0QyUxvblEOM2A1DBG_nv5x53yiV5MRIexSYZyOcrwpuOWfEp9IueyNOo9BKnUmEDSr5oMj0f8htTtIOzdaE-r-BYnfsXutYV24A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.58M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-698552">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC1fKG-oZEPSxAQT8zxCZa41k-4lzY4xc9iSH3TrNxHvRnCCtQ4xqNdUiDjD3q2k2wD1JB1izqOq59UEIQcIkSdPsDd3d-q4rVj-T7e54Oyrlx5femBNEflioD2uD1QuLJmDrDiD46aba9u7cA3V4NUa2yU-VhFmXHBa_plXsRICBpFCo9e4U_Jna4xDYzhoTDUuGeBy9EutfHT6VczyhmDxZJn_tIjm3KBPq09KaKPCHwg8O1HDqYHXcZDUj0BrlZ1XobWbZdflW2ysHYUeLgnaLo0y7RwjIMmo4Ul7WYKW3tVSb2Cvfnx3biZM4tgX6GOIu0QLftm7Kb7Entg_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
فقط تا پایان امروز
❤️
فشارسنج بخر، ماساژور پروانه‌ای هدیه بگیر!
یک فشارسنج کاربردی برای کنترل منظم سلامتی در خانه:
✅
نمایش فشار خون و ضربان قلب
✅
نمایشگر بزرگ و خوانا
✅
اندازه‌گیری سریع و استفاده آسان
🎁
همراه با ماساژور پروانه‌ای رایگان
⚠️
این هدیه فقط تا پایان امروز فعاله
🚚
پرداخت درب منزل
🛡
گارانتی ۳ روزه کالا
👇
مشاهده و ثبت سفارش:
https://memarket24.ir/product/fast/64800/180124/</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/akhbarefori/698552" target="_blank">📅 00:30 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698551">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دیس سنگین همتی به بسنت وزیر خزانه‌داری امریکا
ها، چی شد؟ چی شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/akhbarefori/698551" target="_blank">📅 00:30 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698549">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92a1afd435.mp4?token=SnBdsjXlZc9_-r-0MuypHa2ZVeaqK_p1sEiu54wYOdWNF3dehGxMHrehA9vyypekrRS1rOMluDCpoKPg7IoSI1YbBj5zXMgpv9OcA9qH141aO88Nx8sWoT_vOijKuLayVGpGGewVuToZakJ18SS7vMXgSl1so15H20GTKs-z-Ys8Df_Xz-m5AntoqdkaPCNCfgUfR7O2x66rEJbys2NDA3zswRoHPPibNqPySOpcseyiDE5MZaAPPJfRBYhj6_nKzEZM6CQbVOBDHYocvri5SH7zeBHGJLhu3d_xBbatQnRHt1DcSybtVIl1IoQ1LQcYEFEaHu5FPbkkG2APHub3XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92a1afd435.mp4?token=SnBdsjXlZc9_-r-0MuypHa2ZVeaqK_p1sEiu54wYOdWNF3dehGxMHrehA9vyypekrRS1rOMluDCpoKPg7IoSI1YbBj5zXMgpv9OcA9qH141aO88Nx8sWoT_vOijKuLayVGpGGewVuToZakJ18SS7vMXgSl1so15H20GTKs-z-Ys8Df_Xz-m5AntoqdkaPCNCfgUfR7O2x66rEJbys2NDA3zswRoHPPibNqPySOpcseyiDE5MZaAPPJfRBYhj6_nKzEZM6CQbVOBDHYocvri5SH7zeBHGJLhu3d_xBbatQnRHt1DcSybtVIl1IoQ1LQcYEFEaHu5FPbkkG2APHub3XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات خطرناک موتورسوار، به قیمت آسیب دیدن خودش تمام شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/698549" target="_blank">📅 00:24 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698548">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ9fgtcXWk__1kpyto4rO4WMtQYvePuQtJUpIAfp90lk5g3oQfpSvRoi1P53evT2zCKXG8eWb9g9PZOQ9RVM4oQroN73HJ1s5AEDUqp5l7wAVKZFjCUVdYrop3QxQ6bMG59a79R-m1ZfGBPo0bgnYyCB0rzzNIxsN_lOnt7vfyNg96MvJmGyBWHWF2oQuwK1GL8f6bhmfVDApZ-mns5R4ao1Vz5FtCZx10_NcZNF1_PCgOA-yJ4QKsPqOMYD-ZxwhuP6GMdIf8FXxeIK78REkIXzP_pP80zsu2wD3ns7KvnBOAw6m4tOmTLyiPE9B20MIQAjpRFlf2dXfTih9H4upw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مفسر بازارهای انرژی و ژئوپلیتیک: بعضی از اماراتی‌ها انگار اصلاً نمی‌تونن بفهمن کشوری که ۲۶ برابر کوچک‌تره، ممکنه ظرف فقط یک هفته با خاک یکسان بشه و این تازه خوش‌بینانه‌ترین حالت ماجراست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/698548" target="_blank">📅 00:14 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698547">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a891aebe.mp4?token=M6hS38xoIX7nb1JhRqKpSFLYgK00PXXvXvV0G7sW-m3tAk4Y43w4EAVDu1Q48HavvieQdnQjXMBp0ce7_0ScspyH6eojFz7Z63yzDxbBhyi7XGFwJZs3bVT79lENooRhb7FXXd5U0_nWOEvInYsS2Vgb12_t-RbkWPKj2u-6kyW9OBofi1wWwal8FuqvAiIlIOK8SVPnEj0oZiYmhUc5eOMcw1gZV5Ye2Xo3OmUlPuz3meeJ80LYE4A3BXc0r_GuCtgySa0qTEErG5mSMKAoYsGB8Bwh6bwHmgtKOMV1dTak4e3oLrVuIY48UX3U5VHXWyRJ7xQavKyI1tZGaFbtbDpwEPtdMKSA6zoKV_p--mtt5kk3jhVvr0dg8QeTV1oApJWjaafmkI3D1RF2iJ7q2u5S3GzNU8It8qPM40H7aRvjhuI22uoOv1mz1v9bdxBoW9Rv81TywUxJPVkbnpIol-dMFgQz_pBJm7GnNu7suP2MH_nVzuFWyu_jW01phqTwk54LdUjq2Jy99VTYJWl0Q6V2271f46csMhBxSduSQv47qreQ_6nOWbPE9VwrbYwS3bxqpUmO5tAXn036CnBib6aaKC2Ae9FpwdjudH-zJjMuFB3yY2D2cqjRhLFu0wvpCCvW_dNE6S7ET-u4O6i_nZZEK3Fp8XYaIwvPh9v9ofw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a891aebe.mp4?token=M6hS38xoIX7nb1JhRqKpSFLYgK00PXXvXvV0G7sW-m3tAk4Y43w4EAVDu1Q48HavvieQdnQjXMBp0ce7_0ScspyH6eojFz7Z63yzDxbBhyi7XGFwJZs3bVT79lENooRhb7FXXd5U0_nWOEvInYsS2Vgb12_t-RbkWPKj2u-6kyW9OBofi1wWwal8FuqvAiIlIOK8SVPnEj0oZiYmhUc5eOMcw1gZV5Ye2Xo3OmUlPuz3meeJ80LYE4A3BXc0r_GuCtgySa0qTEErG5mSMKAoYsGB8Bwh6bwHmgtKOMV1dTak4e3oLrVuIY48UX3U5VHXWyRJ7xQavKyI1tZGaFbtbDpwEPtdMKSA6zoKV_p--mtt5kk3jhVvr0dg8QeTV1oApJWjaafmkI3D1RF2iJ7q2u5S3GzNU8It8qPM40H7aRvjhuI22uoOv1mz1v9bdxBoW9Rv81TywUxJPVkbnpIol-dMFgQz_pBJm7GnNu7suP2MH_nVzuFWyu_jW01phqTwk54LdUjq2Jy99VTYJWl0Q6V2271f46csMhBxSduSQv47qreQ_6nOWbPE9VwrbYwS3bxqpUmO5tAXn036CnBib6aaKC2Ae9FpwdjudH-zJjMuFB3yY2D2cqjRhLFu0wvpCCvW_dNE6S7ET-u4O6i_nZZEK3Fp8XYaIwvPh9v9ofw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ترس رانندگی در خانم‌ها بیشتر است؟
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/698547" target="_blank">📅 00:08 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698546">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a516228d86.mp4?token=Ldn9xTX6e6qOXeWA3-atJXy7mpIldPz9tEfEDxNP9qhKBkUs5mS6fhaSAZFPSH8sKSoarDy8jOVqe9ZAJDxemVLkCAeP8tqhg-YCXfuwr4PVOhJbZrktc15m-TkKkDT_L_mrGaZVEWGP0EyDQ53adFdAFSW23_tYgo60F-ks_sQK10ROrWItFysixXib_EAYcf3h1hkAaBEEuhoCAcUEnT_qYMTQT9RAEOTv7dTOu5jtpcm-l7rsxChZI0sG6p6Dcl8Mx1AkvcDTWxNO4zsesgSgoc1xbOO_9fYAlYu7sT16oP5PA3DHtKSKj64e3CmEM9U1EjwCKQ2rP4V-QlMqww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a516228d86.mp4?token=Ldn9xTX6e6qOXeWA3-atJXy7mpIldPz9tEfEDxNP9qhKBkUs5mS6fhaSAZFPSH8sKSoarDy8jOVqe9ZAJDxemVLkCAeP8tqhg-YCXfuwr4PVOhJbZrktc15m-TkKkDT_L_mrGaZVEWGP0EyDQ53adFdAFSW23_tYgo60F-ks_sQK10ROrWItFysixXib_EAYcf3h1hkAaBEEuhoCAcUEnT_qYMTQT9RAEOTv7dTOu5jtpcm-l7rsxChZI0sG6p6Dcl8Mx1AkvcDTWxNO4zsesgSgoc1xbOO_9fYAlYu7sT16oP5PA3DHtKSKj64e3CmEM9U1EjwCKQ2rP4V-QlMqww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ای که آتشفشان، صاعقه را به دام انداخت!
🌋
🌩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/698546" target="_blank">📅 00:04 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698545">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSdutjf_Q6LisJODbArxUmV7zFqKaHNpZtCgSyyK3vImqnhhkliaCI9WJL7H7-8ceAxTjmUjfOz4zlJwihBojbDAK-SaZUz71Skham7BHIwXtp9CjCtV254vkeXJ28LLiDwViEresBvaZ_VHMxr_GKv3BFftyPZsiSm826O9GjhvJxMMdsTu9wwOLVN8deVsm1wScks9OjFniMNhTzroh_hmf0obDk58nnpINeCDaoItOkeQLQe3czttlNgLX4WyA07WCBzXKyHsRKdNRuZkQq-SUBm2rHajFHCbFlo4eQdLSNjdFKKAtgmMHB796zigv30aZq6Fn9-XUopERqNY6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/akhbarefori/698545" target="_blank">📅 00:00 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698544">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
سناریوهای مواجهه ایران و آمریکا در آستانه انتخابات کنگره | چرا کوه‌های اصفهان هدف جذاب‌تری از عملیات زمینی است؟
👇
khabarfoori.com/fa/tiny/news-3252254
🔹
قانون انتقال سهمیه از کارت سوخت به کارت بانکی در این ۵ استان اجرا می‌شود
👇
khabarfoori.com/fa/tiny/news-3252364
🔹
ادعای جنجالی نماینده مجلس: جنگ ظرف یک هفته تا ۱۰ روز آینده شروع می‌شود!
👇
khabarfoori.com/fa/tiny/news-3252255
🔹
بزرگترین نظام مراقبت‌های بهداشتی جهان کجاست؟
👇
khabarfoori.com/fa/tiny/news-3252405
🔹
پروازهای مشکوک اسرائیل بر فراز سوریه و عراق | آماده‌باش در آسمان منطقه | آیا اسرائیل در حال آماده‌سازی مسیر حمله به ایران است؟
👇
khabarfoori.com/fa/tiny/news-3252460
🔹
صفحه اخبار جذاب خبرفوری را اینجا بخوانید و ببینید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/698544" target="_blank">📅 23:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698543">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سپاه: حمله به کشتی‌های متخلف پاسخی به سومین نقض عهد آمریکا بود
سخنگوی سپاه پاسداران:
🔹
آمریکا ۲ بار حین مذاکرات نقض عهد و حمله کرد و بار سوم بعد از امضای تفاهم‌نامه دوباره نقض عهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/698543" target="_blank">📅 23:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698542">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd688bd194.mp4?token=bJ9rhVHqLBc7qldvFZVL49t83lXnnecwk-ZMU_OP0nM5UaX-M7uRjxGP5agby5AOm9zFrKA2pl3BtR9PTzaHFBSrs2AyRD3iMFQLN4995JQaFR4Kg4lMXbi1Pzu1K7Idzwyj3w2ww4nflnhYmVEObIoXoZntk0lVfX-Gu4g4LjJF8Zl1PF_Nwj8P4TMKqcPiqdbAm0AEjtXNotWvwFniGxSg1uTZ920AFkXc_MoPEhLIm4G6iPVl87nfYJCGNnX93iBqKiUuv-aYFp8vMqtgPC1UU84WAbKwClUiWiq05YlEYt2N7jmrzR82J6NqBIS3WNMXpc8rZZUCZWcS8FkUHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd688bd194.mp4?token=bJ9rhVHqLBc7qldvFZVL49t83lXnnecwk-ZMU_OP0nM5UaX-M7uRjxGP5agby5AOm9zFrKA2pl3BtR9PTzaHFBSrs2AyRD3iMFQLN4995JQaFR4Kg4lMXbi1Pzu1K7Idzwyj3w2ww4nflnhYmVEObIoXoZntk0lVfX-Gu4g4LjJF8Zl1PF_Nwj8P4TMKqcPiqdbAm0AEjtXNotWvwFniGxSg1uTZ920AFkXc_MoPEhLIm4G6iPVl87nfYJCGNnX93iBqKiUuv-aYFp8vMqtgPC1UU84WAbKwClUiWiq05YlEYt2N7jmrzR82J6NqBIS3WNMXpc8rZZUCZWcS8FkUHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای عجیب کریم صفایی محافظ شخصیت‌ها در مورد نقش عامل موساد در غرق شدن مرحوم رفسنجانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/698542" target="_blank">📅 23:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698541">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTK2Zbu5qR28d9GOEosLY0tnrZHe7bWY8ik3rIfH0mny3FlFiQDcQfc-UETCQKXSjmpcGCkzbM46SBuKmMrwXvQG_IROmrMtTwYMbgKq3TX7sc-ia2VA9igKkRAU2cCd0CUcoGnUMALvEq1-gqUn4MNmGeGV1PvKCdZhEcB7VgapPc1IBVW8aX2YkGrNSP-b372SR8WuHlPFWOH2S3fTL-qTE6s3j8Hd8iP1T1QqtkUSyxMiCqyCVYLpsoxXNTz5B2YMr2vGobZaY6Qa47PrUaePMC7c8yXsLsbL0ux06DNMxO1pgz3SmExug5lzj8iQsPl3nGE-ccZpmmrs0Ska6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نه دلارهای نفتی به داد بن‌سلمان رسید، نه سلاح‌های آمریکایی!
🔹
بلومبرگ از بحران بزرگ ریاض می‌گوید؛ بحرانی که به تعبیر برخی، صورت‌حساب حمایت از جنگ علیه ایران است. حالا عربستان مانده، حملات انصارالله و متحدانی که حاضر نیستند به کمکش بیایند!
به توییتر خبرفوری بپیوندید
👇
https://x.com/akhbare_fori/status/2110411955840114907?s=46</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/698541" target="_blank">📅 23:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698540">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f2576a51.mp4?token=PCS5A0a3y439n9xQhJGfHY0nHmwZ-SlYsPNE9mOG3MD5vrz3NZG_YV2g69GH9yI1PqflNqqPV6UNoUbvEel4HcDt4RgqgJqiYeXdpSfo0oRO_JNWAoit5XgCi1qb2n2CnLSNsAWqB3aTP-Ft25Zhr8WShEzSWjAQzIIwe8a0x3iAmcGBq5X6BKuLuAtjULolzU08H45quaHUckys61xRKswRJhlBe7A4QzbObuFbR_ucU-3arRtKrbpQ34OF8EW-gGkaRYLz-QNYAcWLI39iEBwpeWrJ6LMpb8tZ9dd-gnfEzZmWbHOevSPcF4lk2r3_hRWHGPL8s4XHTrc3OFSkAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f2576a51.mp4?token=PCS5A0a3y439n9xQhJGfHY0nHmwZ-SlYsPNE9mOG3MD5vrz3NZG_YV2g69GH9yI1PqflNqqPV6UNoUbvEel4HcDt4RgqgJqiYeXdpSfo0oRO_JNWAoit5XgCi1qb2n2CnLSNsAWqB3aTP-Ft25Zhr8WShEzSWjAQzIIwe8a0x3iAmcGBq5X6BKuLuAtjULolzU08H45quaHUckys61xRKswRJhlBe7A4QzbObuFbR_ucU-3arRtKrbpQ34OF8EW-gGkaRYLz-QNYAcWLI39iEBwpeWrJ6LMpb8tZ9dd-gnfEzZmWbHOevSPcF4lk2r3_hRWHGPL8s4XHTrc3OFSkAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپ رپ هوش‌مصنوعی پر بازدید از سردار محسن رضایی، سردار مجید موسوی و سرهنگ ذوالفقاری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/698540" target="_blank">📅 23:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698539">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ادعای سنتکام: ما در ۶ اکتبر یک قایق ایرانی را که در حال انجام عملیات شناسایی و هدف‌گیری علیه کشتی‌های ما در دریای عمان بود، منهدم کردیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/698539" target="_blank">📅 23:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698538">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مجری: آیا تغییر رژیم در ایران قبل از انتخابات اسرائیل، یک احتمال واقع‌بینانه است؟
🔹
نتانیاهو کودک‌کش: خیر، فکر نمی‌کنم این یک احتمال واقع‌بینانه باشد. #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/698538" target="_blank">📅 23:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698537">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UogwelS1I6r1Wf-vFPVXlBPlpy4rq_UXLDlw92A2GxFcqZ2YlrsPb0xhP_LWuGah4BYksNHnaau5-HK2Tn6rEAOdrPYdZyJ_xtqrgSGEPGsiZbN13hOfYWKxFjMPBUm3F_ZgEcyif_94WofLfn0x4INJZ8gXcaJXlGStM6v7rukBu_ykRRQs5VQWn5pmh8T4SN8P0sQNgAEbEq8JQ0-X9-_gdGYd4sAmQJispM5uhHBIb--Xgi3NKmqrOm-tvgcAYZ9qnLlTy4PYYhZUmcFbaF1qRCi0GfDvxp1DilH4k5ixPsIFwYq-P4p-fU9FqaazlbNt5HSGHDYmRK6AbYKnhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلرژی‌های پاییزی/ مکمل‌های مناسب را با علائم خودتان تطبیق دهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/698537" target="_blank">📅 23:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698536">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ca5ec198.mp4?token=rMbCvBP4xP6lALEOL60PLVN49vaSVe7WIy5Q8WoTN3MN8Np4kr_WIjMymBGvDOkEjREIZ9TC2CzTbwZduKDr3vwDV8G9T_OvEt1-MH6vTNFTYua7iYDhef2i61tToBcOCT2CMSYKjPZW-NKBnNCqeU_6ns_cyNEI2VfLt5FUgyZWfYJtNGGjvTXJJO2wyeo6Eb6LmHApDDyzjMPZrQEbKvLdV2-CzsULEPcVcxBVJV5wyM9uoemgd_U8F6lHDpGQ3jWlliub6tRawINga0jIMNQNrIQPKmHDA7VLXzes2Vi8ZMdcYi-mn6IUlZBQw4q6sP08Sf07QkfEPLkvvQ79Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ca5ec198.mp4?token=rMbCvBP4xP6lALEOL60PLVN49vaSVe7WIy5Q8WoTN3MN8Np4kr_WIjMymBGvDOkEjREIZ9TC2CzTbwZduKDr3vwDV8G9T_OvEt1-MH6vTNFTYua7iYDhef2i61tToBcOCT2CMSYKjPZW-NKBnNCqeU_6ns_cyNEI2VfLt5FUgyZWfYJtNGGjvTXJJO2wyeo6Eb6LmHApDDyzjMPZrQEbKvLdV2-CzsULEPcVcxBVJV5wyM9uoemgd_U8F6lHDpGQ3jWlliub6tRawINga0jIMNQNrIQPKmHDA7VLXzes2Vi8ZMdcYi-mn6IUlZBQw4q6sP08Sf07QkfEPLkvvQ79Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری: آیا تغییر رژیم در ایران قبل از انتخابات اسرائیل، یک احتمال واقع‌بینانه است؟
🔹
نتانیاهو کودک‌کش: خیر، فکر نمی‌کنم این یک احتمال واقع‌بینانه باشد.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/698536" target="_blank">📅 23:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698535">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce38001bd.mp4?token=CBvlwRRJZRPiAxmZa65YTgaZ7hd0VtAjyA6uMVsvw7T5Dd15I6muBo-t7Q8R68-fT7NBuEFY_EXNTfECL42v4qOMSGqQula2J08lUuzTDIu9b-aW9D-N7NPmbc8qijb5Ee6p4j7ohbtgMGlGLckCoftim4LcEs4KRFYw4-a0L2knmo5t90h8ZdEHuIugTXgskwWLWY4cuQYlvKT1ugMOrj_IAEnMk-oKvyMx0wT1DQQ3vfqEWb8qHaGcV6l0SatNOlshVZN47k-V0xcZD70d0WzAyQU2UYWrSm6YymxINpzXks2UPkpE7bmr8gafUnzGhvSgVqa_2jHtPLVwEjhtlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce38001bd.mp4?token=CBvlwRRJZRPiAxmZa65YTgaZ7hd0VtAjyA6uMVsvw7T5Dd15I6muBo-t7Q8R68-fT7NBuEFY_EXNTfECL42v4qOMSGqQula2J08lUuzTDIu9b-aW9D-N7NPmbc8qijb5Ee6p4j7ohbtgMGlGLckCoftim4LcEs4KRFYw4-a0L2knmo5t90h8ZdEHuIugTXgskwWLWY4cuQYlvKT1ugMOrj_IAEnMk-oKvyMx0wT1DQQ3vfqEWb8qHaGcV6l0SatNOlshVZN47k-V0xcZD70d0WzAyQU2UYWrSm6YymxINpzXks2UPkpE7bmr8gafUnzGhvSgVqa_2jHtPLVwEjhtlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد هوادار سپاهان اصفهان از افزایش قیمت بلیت مسابقات فوتبال: ۴۰۰ تومان می‌گذارم‌ روی این پول برنج می‌خرم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/698535" target="_blank">📅 23:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698534">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/827d520209.mp4?token=RuV3PeqzM1XTddfz7crbRW7WDiaxWVWOEfyx484C1_Yy8C60cquyCBoEoBNNQMiq1uc1v5zMdu_DmflwfpuJpDKSaT080d4OD2meSwZWUOl7LQ-QhnupLK6XavBcJEMjkDfww9jQJYPjsV0Pn_s7hCK78womMK4yHEGkFv0qtJ0NYzlr5yUXRWkVWaWqEO4AxQup57ypYMIqhnGX1mPIPtkwmBQZBBb-CS2A23B7y_GcGy3pi_Ao_eBuubIeQ9TDd_UKmZZ3NfOja_Hi3s2om7dhYYKB67f-w46ZNBSpLc8z3fUOpzxGwfx2b7YqZTo7FdEsVyt1HigEuH5XRV86TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/827d520209.mp4?token=RuV3PeqzM1XTddfz7crbRW7WDiaxWVWOEfyx484C1_Yy8C60cquyCBoEoBNNQMiq1uc1v5zMdu_DmflwfpuJpDKSaT080d4OD2meSwZWUOl7LQ-QhnupLK6XavBcJEMjkDfww9jQJYPjsV0Pn_s7hCK78womMK4yHEGkFv0qtJ0NYzlr5yUXRWkVWaWqEO4AxQup57ypYMIqhnGX1mPIPtkwmBQZBBb-CS2A23B7y_GcGy3pi_Ao_eBuubIeQ9TDd_UKmZZ3NfOja_Hi3s2om7dhYYKB67f-w46ZNBSpLc8z3fUOpzxGwfx2b7YqZTo7FdEsVyt1HigEuH5XRV86TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات مستأصلانه ترامپ جنایتکار: ما در ایران با چه کسی در حال تعامل هستیم؟ هیچ‌کس دقیقاً نمی‌داند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/698534" target="_blank">📅 23:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698533">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
جزئیات مجروحیت رهبر انقلاب از زبان رئیس اورژانس تهران  محمداسماعیل توکلی رئیس اورژانس استان تهران:
🔹
ایشان جراحت‌های سطحی در پیشانی و لب و پا داشتند؛ من هم بعدا از دوستانی که در صحنه حضور داشتند این را شنیدم.
🔹
پنجره اتاقم مشرف به پردیس حکومتی بود.با آقای…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/698533" target="_blank">📅 23:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698532">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
‏زلنسکی خطاب به ایلان ماسک: لطفا استارلینک ما را قطع نکنید. این یک اشتباه بزرگ است. این کار را نکنید/ امریکا با قطع استارلینک به ما خیانت کرده
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/698532" target="_blank">📅 23:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698531">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70055b1e6c.mp4?token=qQ4VURPCoXmDZAcwxosIqaZMROfRkjcLBRthE-ziw5MM1ORxzoxKjJxg6SAbQiYQmvsAiyIuMB3wF-FobXLGoacc1AfcZizgFDsCVY7ICALgd5AztS7y0tfYGt7YJx3mezI4mUwc3MS0P0ncInmGj27CFQby8yvvY7pUEgaLVh9lDxJcJLgZ5eX3BzkzEJmiYo-yS1Q-BV7det5uoeF8K4Y7Nu4UKIBwbf-2wg-jBYV8yR-tDKKYe0OaP27uYVFGH7n73N6DonmLZUw8tOWqGD3ddCq8kK7qa58NJG18jJQWfORxzNnP76pxtsuhi9esBlpvvD3Q_lvGky3C8sdoBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70055b1e6c.mp4?token=qQ4VURPCoXmDZAcwxosIqaZMROfRkjcLBRthE-ziw5MM1ORxzoxKjJxg6SAbQiYQmvsAiyIuMB3wF-FobXLGoacc1AfcZizgFDsCVY7ICALgd5AztS7y0tfYGt7YJx3mezI4mUwc3MS0P0ncInmGj27CFQby8yvvY7pUEgaLVh9lDxJcJLgZ5eX3BzkzEJmiYo-yS1Q-BV7det5uoeF8K4Y7Nu4UKIBwbf-2wg-jBYV8yR-tDKKYe0OaP27uYVFGH7n73N6DonmLZUw8tOWqGD3ddCq8kK7qa58NJG18jJQWfORxzNnP76pxtsuhi9esBlpvvD3Q_lvGky3C8sdoBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود آب سیلاب به داخل اتوبوس شهری در استانبول
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/698531" target="_blank">📅 23:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698530">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
در مناطق عشایری شمال خوزستان، اسنپ با اختصاص ۴ میلیارد تومان، هزینه سرویس مدرسه دانش‌آموزان دختر را تأمین کرده تا مسیر دشوار و پرهزینه، مانع تحصیل آن‌ها نشود. همچنین به هر دانش‌آموز یک تبلت برای دسترسی به آموزش آنلاین اهدا کرده است.
اقدامی در مسیر عدالت آموزشی و فراهم کردن فرصت برابر برای تحصیل دختران.
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/698530" target="_blank">📅 23:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698529">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16428ef0e7.mp4?token=gQqtLZwE62LX3Ux2R4jywR_dQQn5eqdz89d5W3bns6d41oZEQ3EtmG_knhs7IeXzpv8kWul4Kkkul6MDeE0kipGUyPYMTVWTyNm5Z9GRb9ZBFpGGrjjXn43rczhZImu43Tb4AVZppo1N5bvGRof2lf2_FxugppdVg_-WENmOrKp1QHCBGmL_sM-EKuCtOsGB7SUXAn9HTDAt11c7_Vzc5j0LHaeNoP-D6UT56JQX_nuSGwbfOgWwpqfVVH3k1cdEVcVyQvcSeF80ztAeB-0wNJKtvSPzK_UnvhILEL4M1hhuyM79ITYEMCB9GOaXJmpEZy-40oROxGJzfccf_QpoNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16428ef0e7.mp4?token=gQqtLZwE62LX3Ux2R4jywR_dQQn5eqdz89d5W3bns6d41oZEQ3EtmG_knhs7IeXzpv8kWul4Kkkul6MDeE0kipGUyPYMTVWTyNm5Z9GRb9ZBFpGGrjjXn43rczhZImu43Tb4AVZppo1N5bvGRof2lf2_FxugppdVg_-WENmOrKp1QHCBGmL_sM-EKuCtOsGB7SUXAn9HTDAt11c7_Vzc5j0LHaeNoP-D6UT56JQX_nuSGwbfOgWwpqfVVH3k1cdEVcVyQvcSeF80ztAeB-0wNJKtvSPzK_UnvhILEL4M1hhuyM79ITYEMCB9GOaXJmpEZy-40oROxGJzfccf_QpoNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نشریه i24NEWS: مقامات ارشد ایرانی در روزهای اخیر به دیپلمات‌های منطقه‌ای گفته‌اند: ما مطمئن هستیم که آمریکا حمله خواهد کرد
🔹
همان مقامات به دیپلمات‌ها گفته‌اند فضای جنگی در تهران حاکم است.
🔹
در روزهای اخیر ایران سرعت آتش‌زنی در تنگه هرمز را افزایش داده است. چندین کشتی که مورد حمله قرار گرفتند، غرق شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/698529" target="_blank">📅 23:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698528">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4684ecccaa.mp4?token=dxAP784NABkYSuK_U6w4USM5PgoRKhbW3NTG8qwERVNPkoydt0xSn0VSjnc-JSKtPeBqMVUphFZv7CWiL4hRLtZNtk4SlESeEO9f3im7SOHih7vXTwTbpWJox2vQu19vqncFnIkiKzV2TgxoN6mTtxTsUUEBfsLRprB7NQxPRZ4ckoCXK4-bTd2LwkUjY2CKeTmWXd70dnKicUfd_NAZavoR9gllabV5Td11KPzDEd0_ymMGBJHeDIYDkFwrCWrgyblKmy-aAYI46bVMliF5UPRMvHnOfUPv0Ska0UeV4AIUMJdTAlfH5AgPmkKKeKFvjbrDobfqhtLpx3ox4TG85H3mwSEQCGYaOR0zufbOkWwH85i2goR5MN6UYGQsJH4__4rRSM88AerEacW0Jp_uLFS_xyJFXMR3O-vHK_LzecemT6tskFLut7LN2M1LoN6EV6MM5ciAmrj2PTxCbnyM_qje-RvmU7UpSwk74c_vNkMfLz08ySHmb72Rmgb5nSQ7J_IsTy4xgalpFFSteP1UqTXF2F874G6nYx9g_tPFf-hRIEIvV2btBQ6Dy3WC1c5WqTmrwXrI3aCsDKAmucW8GcsuLTNQIYL6ynEZ0DLZuLTu-1fvaKk6ag8ovXVXGmd3TRsoE8P4jMDAOEZ1wkqOVrDYm0xTpYXo9cYUNwetus8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4684ecccaa.mp4?token=dxAP784NABkYSuK_U6w4USM5PgoRKhbW3NTG8qwERVNPkoydt0xSn0VSjnc-JSKtPeBqMVUphFZv7CWiL4hRLtZNtk4SlESeEO9f3im7SOHih7vXTwTbpWJox2vQu19vqncFnIkiKzV2TgxoN6mTtxTsUUEBfsLRprB7NQxPRZ4ckoCXK4-bTd2LwkUjY2CKeTmWXd70dnKicUfd_NAZavoR9gllabV5Td11KPzDEd0_ymMGBJHeDIYDkFwrCWrgyblKmy-aAYI46bVMliF5UPRMvHnOfUPv0Ska0UeV4AIUMJdTAlfH5AgPmkKKeKFvjbrDobfqhtLpx3ox4TG85H3mwSEQCGYaOR0zufbOkWwH85i2goR5MN6UYGQsJH4__4rRSM88AerEacW0Jp_uLFS_xyJFXMR3O-vHK_LzecemT6tskFLut7LN2M1LoN6EV6MM5ciAmrj2PTxCbnyM_qje-RvmU7UpSwk74c_vNkMfLz08ySHmb72Rmgb5nSQ7J_IsTy4xgalpFFSteP1UqTXF2F874G6nYx9g_tPFf-hRIEIvV2btBQ6Dy3WC1c5WqTmrwXrI3aCsDKAmucW8GcsuLTNQIYL6ynEZ0DLZuLTu-1fvaKk6ag8ovXVXGmd3TRsoE8P4jMDAOEZ1wkqOVrDYm0xTpYXo9cYUNwetus8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمپر آب بالا رفت؟/ ببینید موقع جوش آوردن ماشین چیکار کنید!
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/698528" target="_blank">📅 23:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698526">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4396addb.mp4?token=UPXwAdhLlVhiBJ9O8ISc0sLsd57c_hJColDOyiTMkYszOUQG3S6sJoBSHc_cxZyodhgjPvJgaUvYETBjiPWIZfqFqpuVct5jnAGt3i3CyVXNG12JEsdIiAOjLKGe2RPOy116prnlRGj2sqgP1MblV_4kB_6JfzBAxF6K7XtwbSvmhz_LevHrMokRuKlVZeK-UGmpnbCL-r2RxUo6g4HCupQYrgAiDIf8jS1SvSO9V3PpVlau54NIK207cRBsOY23FguZVpGD4CGHo67q5DhpQBgPLFPeC0-Z3L4OUSi_DCpT7bSwMD2ZdrXYoSKMwpWWa_iWt1CKMPlkkQS_SaG9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4396addb.mp4?token=UPXwAdhLlVhiBJ9O8ISc0sLsd57c_hJColDOyiTMkYszOUQG3S6sJoBSHc_cxZyodhgjPvJgaUvYETBjiPWIZfqFqpuVct5jnAGt3i3CyVXNG12JEsdIiAOjLKGe2RPOy116prnlRGj2sqgP1MblV_4kB_6JfzBAxF6K7XtwbSvmhz_LevHrMokRuKlVZeK-UGmpnbCL-r2RxUo6g4HCupQYrgAiDIf8jS1SvSO9V3PpVlau54NIK207cRBsOY23FguZVpGD4CGHo67q5DhpQBgPLFPeC0-Z3L4OUSi_DCpT7bSwMD2ZdrXYoSKMwpWWa_iWt1CKMPlkkQS_SaG9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نفتالی بنت: با دست خودمان به سمت فروپاشی می‌رویم
نخست‌وزیر سابق رژیم صهیونیستی:
🔹
ما در حال خودکشی هستیم و دوره دولت آینده، آخرین فرصت برای نجات اسرائیل است.
🔹
اکنون یا هیچ‌وقت! اگر نتوانیم این ساختار افراطی ضدصهیونیستی را از بین ببریم، اسرائیل را از دست خواهیم داد.
🔹
ما فرو خواهیم پاشید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/698526" target="_blank">📅 23:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698525">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
شائبه انتصاب خلاف قانون در سازمان بورس؛ شورای عالی بورس پاسخ دهد
🔹
ادعای انتخاب اعضای هیئت‌مدیره سازمان بورس توسط شورای عالی بورس بدون استعلام از وزارت اطلاعات، سازمان اطلاعات سپاه و قوه قضائیه، قانونی‌بودن این انتصاب‌ها را زیر سؤال برده است.
🔹
ماده یک «قانون نحوه انتصاب اشخاص در مشاغل حساس»، انتصاب بدون استعلام در سمت‌های مشمول را کأن‌لم‌یکن دانسته و برای مرتکبان، محرومیت از حقوق اجتماعی درجه پنج پیش‌بینی کرده است.
🔹
شورای عالی بورس باید روشن کند آیا استعلام‌های قانونی انجام شده است؟ در صورت احراز تخلف، رسیدگی مراجع نظارتی و قضایی به اعتبار انتصاب‌ها و مسئولیت تصمیم‌گیران ضروری است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/698525" target="_blank">📅 23:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698524">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOdNoGcfSZsU9pzdUHSg5yOhD-p7Ubxb7VQtnHbqTEsnaT2QdwyIbhQyyEE_z0L3bRa5plH85bzYgX7cXx2Wqj5MAg2oM8KpX4TUO_xLbip3k-R3roqdLsMs81H0oPmchYxSsyRU-q1QB_0Jjront9X9Mdz9RjBc84buuBE_c_SFQ8ypr1DIuc2YbKtfpAJI0mfleBG0qa-8G-bX3cD9uzabnBCz7fuAyN-VJr8-ClLfoMzz4iJnCfgkyKJUUfUbsitGKg4OKjCpJH6yWaV2vaNFbXlBFdJ5Hy5OfzmbDrSEtDvN0Bs2f7X-mqRbGC9XyV27XE-BbTM3zgQ2NNL0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏎
🔥
امروز بپوش، ۴ قسطی پرداخت کن!
ست سویشرت و شلوار اسپرت
BMW M-Power
رو پسندیدی؟
😎
دیگه لازم نیست برای خریدش صبر کنی؛ همین الان سفارش بده و هزینه‌ش رو قسطی پرداخت کن!
👕
سایزبندی:
فری‌سایز، مناسب L و XL
💳
پرداخت در ۴ قسط، هر قسط فقط ۴۵۲٬۲۵۰ تومان!
✨
مزایای خرید از ما:
✅
بدون نیاز به چک و ضامن
🚚
ثبت سفارش آسان و تحویل سریع
🛒
برای سفارش  همین الان بزن رو لینک
👇
https://memarket24.ir/product/brief/56226/180124?p=9</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/698524" target="_blank">📅 23:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698523">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
نوروزی، مدیرعامل سازمان هدفمندسازی یارانه‌ها: اگر بودجه کل دولت حدود ۶ هزار ۲۷۸ همت در سال جاری باشد، ۲ هزار و ۳۲۰ همت از آن مربوط به موضوعات مرتبط با یارانه‌ها است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/698523" target="_blank">📅 23:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698522">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
نوروزی، مدیرعامل سازمان هدفمندسازی یارانه‌ها: اگر بودجه کل دولت حدود ۶ هزار ۲۷۸ همت در سال جاری باشد، ۲ هزار و ۳۲۰ همت از آن مربوط به موضوعات مرتبط با یارانه‌ها است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/698522" target="_blank">📅 22:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698521">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a392deee.mp4?token=EyE5EOF6L4rSRR21OYv9LB1or__Yz-5GiNRrbWv_s-ZF-g86nZgWdDzRlgwBkSBE0TwPh_OtHmxZVxfykON3Xmw4IjF2hJZ1gI_RKO4Ip1Oa2pkv4w9LWyznig4jP9ecn1PjpFY6bc6Zr58NpRLTtDkDNhnpZg_2dNaIc5MzJeY6lr6cQmbj5Po97py6Mk6p-VOtGyH1mDKP7_sKrei_lgRmDKl68j2BQA-uASSRnQUgMbUPPxKwU0rsSn2fHAiKldxsh-ceOzQZZEaoXRcOdoDPC_AuArXJJu7hXylfFzof-xukW1oHgTnN_Lrofv0vayIEXwwp068-_J8iBkzfkHQ74Xq86dST586xY4j5KXF5RSdYQ4W1znpBaGjR3HUITEBD8V9jmdi60_Y2qsZD9hbumwxOUojPxJxWgneIK8aUAbcZTm21sDfLTiFoxJasgfa-IpnfKMvzdUhPJjbUY23odpeZPWkBs7oa6UPD6IO4Zya7MYoFnStiwtj6nCEclBTiJlWFjOLOOnCCexE7ye3NfdRhWbGo14y1N7BwErNaKdOzXGCTFiNHxCLXvaa8stvwQAW9yD5qcW12FVFywK0-5Zdp5iIyhK8-SUKzLsXXuWpXmV0mcG0L3LytQ18ls9dkCp1lnvM94_w5UWFfa_s4epuXXH7kRaIK1c9bnvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a392deee.mp4?token=EyE5EOF6L4rSRR21OYv9LB1or__Yz-5GiNRrbWv_s-ZF-g86nZgWdDzRlgwBkSBE0TwPh_OtHmxZVxfykON3Xmw4IjF2hJZ1gI_RKO4Ip1Oa2pkv4w9LWyznig4jP9ecn1PjpFY6bc6Zr58NpRLTtDkDNhnpZg_2dNaIc5MzJeY6lr6cQmbj5Po97py6Mk6p-VOtGyH1mDKP7_sKrei_lgRmDKl68j2BQA-uASSRnQUgMbUPPxKwU0rsSn2fHAiKldxsh-ceOzQZZEaoXRcOdoDPC_AuArXJJu7hXylfFzof-xukW1oHgTnN_Lrofv0vayIEXwwp068-_J8iBkzfkHQ74Xq86dST586xY4j5KXF5RSdYQ4W1znpBaGjR3HUITEBD8V9jmdi60_Y2qsZD9hbumwxOUojPxJxWgneIK8aUAbcZTm21sDfLTiFoxJasgfa-IpnfKMvzdUhPJjbUY23odpeZPWkBs7oa6UPD6IO4Zya7MYoFnStiwtj6nCEclBTiJlWFjOLOOnCCexE7ye3NfdRhWbGo14y1N7BwErNaKdOzXGCTFiNHxCLXvaa8stvwQAW9yD5qcW12FVFywK0-5Zdp5iIyhK8-SUKzLsXXuWpXmV0mcG0L3LytQ18ls9dkCp1lnvM94_w5UWFfa_s4epuXXH7kRaIK1c9bnvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک زوایه دید جالب از داخل یک کشتی سوراخ شده در خلیج فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/698521" target="_blank">📅 22:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698520">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/236e3f7a47.mp4?token=BmB7FMzDzHqbYPqF8kK4PywZMq6KuR4WzFbTcLCsPAoapqOxYlw9yEGU6ByWuKm9DcGX0ch1yc7vM__774Gi10Z0NJfn2C2Ou8UGnTHawun_OF-eS-1AYUEc8rClTmN_qz3aVOw4gYigaVSnQzz89j-h8ryhRRQ7ZPGKxcutAS7wPBRZLWdfX0cfuL08mYa_eogGf77CoGN1YwZ3VMI8MxmX7aEVaZh_7R7sOUg31akrVSewxwJEgr_2YTTI-YidikqT5NimiE0W1ETZ99EU7ck7eXvRkdNE8C8lt09-_hM-zq1EllFeNhPWlb1BX-qAz0hfYaM8iTOOUul9dayy-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/236e3f7a47.mp4?token=BmB7FMzDzHqbYPqF8kK4PywZMq6KuR4WzFbTcLCsPAoapqOxYlw9yEGU6ByWuKm9DcGX0ch1yc7vM__774Gi10Z0NJfn2C2Ou8UGnTHawun_OF-eS-1AYUEc8rClTmN_qz3aVOw4gYigaVSnQzz89j-h8ryhRRQ7ZPGKxcutAS7wPBRZLWdfX0cfuL08mYa_eogGf77CoGN1YwZ3VMI8MxmX7aEVaZh_7R7sOUg31akrVSewxwJEgr_2YTTI-YidikqT5NimiE0W1ETZ99EU7ck7eXvRkdNE8C8lt09-_hM-zq1EllFeNhPWlb1BX-qAz0hfYaM8iTOOUul9dayy-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معجزه‌ای بسیار زیبا از قرآن کریم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/698520" target="_blank">📅 22:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698519">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8f9f2ae5d.mp4?token=P-Du9xYzyIQkolFrGQZOBdbBfE-pgHKkSczpRCdPiazyRk1raHRabF0aQ5Ol54ZA8TO2aHMGmDtYjh075TaHwoPb-xq9zsd_N42OuXPctjF0WnvJgEt8xRtZlpas4bpy-ZffZXKq5RNETn2UUzt9gi2l51PhNxl32ioueJonQmOURjzlIOoHkFOil0sQU_xdBV4GxwlsXqjjGeGOgvrXbNIsjO2axB7-IaH1jpOScSSQq4M_V59eQaa3RtuY5scl71Ns4JBh8EsmZBE56m0k2dI1yEcK9u-Z8-Xu3CIcbI5dcU9vRRGRfiBnnpYTmizr8fl6nEaYQNeqAuj7NTQvzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8f9f2ae5d.mp4?token=P-Du9xYzyIQkolFrGQZOBdbBfE-pgHKkSczpRCdPiazyRk1raHRabF0aQ5Ol54ZA8TO2aHMGmDtYjh075TaHwoPb-xq9zsd_N42OuXPctjF0WnvJgEt8xRtZlpas4bpy-ZffZXKq5RNETn2UUzt9gi2l51PhNxl32ioueJonQmOURjzlIOoHkFOil0sQU_xdBV4GxwlsXqjjGeGOgvrXbNIsjO2axB7-IaH1jpOScSSQq4M_V59eQaa3RtuY5scl71Ns4JBh8EsmZBE56m0k2dI1yEcK9u-Z8-Xu3CIcbI5dcU9vRRGRfiBnnpYTmizr8fl6nEaYQNeqAuj7NTQvzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کرباسچی: این جنگ تحمیلی است و باید همه عقلا جمع شوند تا این وضعیت را پایان دهیم/ سوای نگرانی نسبت به تمامیت ارضی کشور، نگرانی نسبت به زندگی عمومی مردم داریم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/698519" target="_blank">📅 22:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698518">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34a3b81f6.mp4?token=K5B3YQXplNUjvH0mC3d5VAbpPOt1M7c_sBWzzZUrLrcWRrk1oHDc5glARRQio35O1Xs5xnh_xiNwX_XnCgI7yNQgWs3uNZAPhIT9DyJRh5XW_vcGl2E46MYIzctGJdQ9mktMzQlFjaEM4dnYbU_5CXMdElwCWL0kWRwASrNxvmnw-br2VYfqTrcMoMEYsByrjGvQJuRUB2L_7aYgqXGjSJfKqKi_8kM_EORoWpErWocgbVS2KZaiMpA9W3pkQIr7Kz8kNtQO8mMPvcDw6Jr1aIMzAwtZC1Arr2BzFmIuFKW4plMJ8M-76OHlladEBsa57Xel0IylryPfrEb3zWh1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34a3b81f6.mp4?token=K5B3YQXplNUjvH0mC3d5VAbpPOt1M7c_sBWzzZUrLrcWRrk1oHDc5glARRQio35O1Xs5xnh_xiNwX_XnCgI7yNQgWs3uNZAPhIT9DyJRh5XW_vcGl2E46MYIzctGJdQ9mktMzQlFjaEM4dnYbU_5CXMdElwCWL0kWRwASrNxvmnw-br2VYfqTrcMoMEYsByrjGvQJuRUB2L_7aYgqXGjSJfKqKi_8kM_EORoWpErWocgbVS2KZaiMpA9W3pkQIr7Kz8kNtQO8mMPvcDw6Jr1aIMzAwtZC1Arr2BzFmIuFKW4plMJ8M-76OHlladEBsa57Xel0IylryPfrEb3zWh1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
‏
زلنسکی خطاب به ایلان ماسک: لطفا استارلینک ما را قطع نکنید. این یک اشتباه بزرگ است. این کار را نکنید/ امریکا با قطع استارلینک به ما خیانت کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/698518" target="_blank">📅 22:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698517">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
اعتراف نفتالی بنت به قدرت روزافزون مقاومت فلسطین: حماس هر روز قوی‌تر می‌شود/ ارتش اسرائیل با کمبود ۲۰ هزار نیروی رزمی مواجه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/698517" target="_blank">📅 22:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698516">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سفر رئیس اف‌بی‌آی به روسیه پس‌از ۱۳ سال  رسانه آمریکایی ام‌اس‌نَو:
🔹
کش پاتل، رئیس اف‌بی‌آی، برای مذاکره به روسیه سفر کرده است؛ سفری که نخستین سفر رئیس این نهاد به روسیه از سال ۲۰۱۳ محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/698516" target="_blank">📅 22:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698514">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
نیروهای مسلح یمن تأسیسات توزیع نفت آرامکو در شمال جده عربستان را هدف قرار دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/698514" target="_blank">📅 22:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698513">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7Pd-7JA25d6WbUm4-Ea8Jo1HeJGR4LQbgmYb8rQHgvitMMr140qeR6frQ348IyiU3irZa6SYM-Zf8jGCWesEsXZNXMTnNvCDGUvJT3npxnFSfLR2kEbXuhk9-LocFxZYQvO0c_vauhuH7von4sy0ZHKHA6TF3K82Lsek-5XsZBP0Eo0IMd3smPj9Xe3hFdcVJgIxLyYzXxsv2zzHiNlW8acPoVMvnxK2b5YwWPvrl_vwFSD9INr1p0CcB2nFXlSjPo4X86uHTxbYReQ3opT76cUswkVFEJPPB3bA-7yX5bUJegdWWCOsXusTvRHRGDNx9sFIvtRP9bfoCtpXxUlZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرتیپ یحیی سریع: حملات سعودی به جزیره میون مستقیماً خطوط کشتیرانی را تهدید می‌کند. ما رژیم سعودی را مسئول کامل پیامدهای این حملات و خطرات ناشی از آن برای امنیت دریانوردی می‌دانیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/698513" target="_blank">📅 22:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698512">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AY4PQHCAxAQTC4KhptHjDSAD4KH2PKIB0ZqVVNfPuUtRiLJ8SQexW4mS-M5B2mcar77ANAiAHZsMv0-P7M5KkYIWzmXTpa56b5xi-xqQqx8I7TyceeVwkuZThXMjM2yqnnLa-O9bn2MjVlp2KPDCju4tzjboqxSdt3ezMPlEfvm75KXsaiVeRHdjwqIZpBUGHOiU9_SI3vXJPmHq_a_SUq_J7INqg9L5LfhuSAJ4ShT_Ztx2lGILdKsHvxCFzGKk6Z6uO3YJ34g-tOOvFo4IbAiKxtgsIIwDjn6lFmRFBBuUQT3kp5kroVgllCAThF2932b14jVVqr2kVIBTdepzaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس روز ناسا از مریخ و کندوی عسل زیر شفق قطبی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/698512" target="_blank">📅 22:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698511">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPUPheDlPrWs6_uuP4JHYbYKQM8Pjj4GeFahesNTRgP0DIqhmwqZojh1E_xTCi1qjXREsxUpTpLC_nBxTTH7kaW-j1gLjUZIlZ58TjR4ztIhjINT34SUIl1Sc8kj3SzRwvNPZWXGatMeuUgJCYff_2LnIm6ABvx_n7BYV0ydG20r1iTTf3qV_nN1zIUuJRqV4N0CliR51fOK6K95grXJi4hDf-x32V_RI7xZOwwxxxm6N3UHODN6XVta8MFtQ7I59EynVVHdUKZOrPa2iOVFwse4HfIVeBt2ZEtxRgiwLi71gOx93ZOjVeW7ipZnrZ-PB3nCIzxvVz9CHohPOHreTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس انجمن شرکت‌های دانش‌بنیان فاوا: سرکوب تعرفه‌ها، توسعه شبکه ارتباطی را متوقف می‌کند
🔹
فریبرز نژاددادگر، رئیس انجمن شرکت‌های دانش‌بنیان فاوا، با اشاره به افزایش هزینه‌ها و محدود شدن درآمد اپراتورها گفت شرکت‌های ارتباطی دیگر توان کافی برای توسعه و ارتقای کیفیت شبکه ندارند و بیشتر برای حفظ وضعیت موجود تلاش می‌کنند.
🔹
به گفته او، کوچک‌شدن بازار مخابرات، شرکت‌های دانش‌بنیان و پیمانکاران بخش خصوصی را با رکود و خطر ورشکستگی روبه‌رو کرده است. کاهش سفارش‌های فنی و توقف پروژه‌های توسعه‌ای، زنجیره تامین این صنعت را تحت فشار قرار داده است.
🔹
نژاددادگر با تاکید بر نقش ارتباطات در اقتصاد دیجیتال، خواستار اصلاح تعرفه‌ها شد و هشدار داد ادامه روند فعلی می‌تواند فاصله فناوری ایران با جهان را بیشتر کند؛ شکافی که جبران آن در سال‌های آینده دشوار خواهد بود./ شرق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/698511" target="_blank">📅 22:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698508">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
قالیباف: ایران قوی سبب می‌شود آمریکا بفهمد نمی‌تواند به اهداف خودش برسد
🔹
قوی شدن ایران بازدارنگی پایدار ایجاد خواهد کرد و این قدرت باید برای تمام بازیگران منطقه‌ای و جهانی به اثبات برسد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/698508" target="_blank">📅 22:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698507">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
قالیباف: دشمن به غلط احساس کرد که ما ضعیف شدیم و به ما حمله کرد؛ فهمید اشتباه کرده اما هنوز امیدهایی دارد؛ باید به بازدارندگی پایدار برسیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/698507" target="_blank">📅 22:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698506">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
قالیباف: صرف مذاکره مانع تداوم جنگ نخواهد شد همانطور که صرف جنگ هم مانع تداوم جنگ نمی‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/698506" target="_blank">📅 22:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698505">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034cd4b83a.mp4?token=ROCuE0NHPaKPa311WfVDVuxLKxmm2qdP6FaQ1xTrLvISmSmS8BnWx55LtWf16-sfqtpqk0J3EW0BIuOMPA8Y77s6-OMiZjOea46wI2GdsZOAWq0U4-ghmQUrBJb3j5a8d4WN1KNB1R4Hp-r1lHKvpjy-b79u2ZogxuGrZCBe-o3z1QVc1LkWM6REZLHBiOB7mEG13oJxCqdsZJ2a52AFrhFSfFhuHSM-RixI1lh6dCxov0CiNTrUiP0hCW41AH16LcD0ej1FTXk1T6fNuwFDvyURvPqG8LJebLuoyxvId2gWkFCGdDD_n_MYr93xcdexCnTNrhp3Sr2S94aWYHB4wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034cd4b83a.mp4?token=ROCuE0NHPaKPa311WfVDVuxLKxmm2qdP6FaQ1xTrLvISmSmS8BnWx55LtWf16-sfqtpqk0J3EW0BIuOMPA8Y77s6-OMiZjOea46wI2GdsZOAWq0U4-ghmQUrBJb3j5a8d4WN1KNB1R4Hp-r1lHKvpjy-b79u2ZogxuGrZCBe-o3z1QVc1LkWM6REZLHBiOB7mEG13oJxCqdsZJ2a52AFrhFSfFhuHSM-RixI1lh6dCxov0CiNTrUiP0hCW41AH16LcD0ej1FTXk1T6fNuwFDvyURvPqG8LJebLuoyxvId2gWkFCGdDD_n_MYr93xcdexCnTNrhp3Sr2S94aWYHB4wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: تفاهم علاوه بر بازدارندگی به نیروهای نظامی ما کمک کرد تا قوی‌تر شوند، تاب‌آوری اقتصادی آن‌ها بیشتر شود، حزب‌الله لبنان قوی‌تر شود
🔹
ما با این تفاهم فرصت و منابع کافی پیدا کردیم که مولفه‌های قدرت خودمان را قوی کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/698505" target="_blank">📅 22:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f5295cb21.mp4?token=fKEyaA0GWCD2_VHuF3YcJDQGGW4b9c6HM5JBbYCtG8CAnIdICwjnTl01iZTzA5VWDvNj8QXdxLGG0UE516hJA6LNdKf8EY9XZfZ8MpG7YGx-mqHKJpsB035Pu_QqjhdLlwofJrF6ZvIZv5xE5mCmfoOGz8-84jFFZt3krLmG9I4YjqDN70jdj2lf_lOOcFADMqlapD0M6ZYdyQ6biLDKMwCwwT17_CeZ64tSC0iUmwX7sl6BA5OGZNmn-rY5I_gXrNMJuxUshes6fJn4fxkugyLhJg2AWgCUPM2GlYiMA4Gqo5g_Uo4e5b3i4rjgHjONeOigICjCr0Ou9eGslEtTHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f5295cb21.mp4?token=fKEyaA0GWCD2_VHuF3YcJDQGGW4b9c6HM5JBbYCtG8CAnIdICwjnTl01iZTzA5VWDvNj8QXdxLGG0UE516hJA6LNdKf8EY9XZfZ8MpG7YGx-mqHKJpsB035Pu_QqjhdLlwofJrF6ZvIZv5xE5mCmfoOGz8-84jFFZt3krLmG9I4YjqDN70jdj2lf_lOOcFADMqlapD0M6ZYdyQ6biLDKMwCwwT17_CeZ64tSC0iUmwX7sl6BA5OGZNmn-rY5I_gXrNMJuxUshes6fJn4fxkugyLhJg2AWgCUPM2GlYiMA4Gqo5g_Uo4e5b3i4rjgHjONeOigICjCr0Ou9eGslEtTHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود آب سیلاب به داخل اتوبوس شهری در استانبول
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/698503" target="_blank">📅 22:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffDXcBgxmXQ_uK9Fr0QopkYGUfLTE_rKDdLAvs_yA_W9eyqwM5aOAToFsSZCwKBM1vZP8f3NBoI4gnP0ygJoCe7aBVdYUt2EOP48BKSqibHsqYDCpKbVFJwlVbamDeMsyJx9FaThHndQBV2Fq68VjgqpYafi6Ebbb9sxAulSbn0wippZN_ZoaDS6DyujPL46oRMfRLY06CQEacaPbu7wIIVuoz5J6QXtThxXZztka4MDkMCPy6rXIGjzsU3r2PvWu5r5yNaCmD0274IjKtAqYz12ei4WzGFCa4Ci497DQC3hXsK1sIfp6kgPoU236g7N42Kzd49dXWJ3jscL4Am_ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبر خوش برای تهران؛ آغاز فصلی جدید در تفریح و گردشگری شهری
🔹
اولین ساختار رسمی جامع شهری در حوزه گردشگری و تفریحی در تهران ابلاغ و مدیر آن منصوب شد.
🔹
بعد از قریب به ۵ سال بالاخره پس از پیگیری های شهرداری و شورای شهر تهران، شرکت گردشگری و‌ تفریحی میلاد تهران تاسیس و عباس حیدری به عنوان مدیرعامل آن توسط شهردار تهران منصوب شد.
مشاهده ادامه خبر:
https://www.khabarfoori.com/fa/tiny/news-3252476
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/698502" target="_blank">📅 22:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=QKrUhnTneGKYvTMaGVLa0rYvo8vM0tUjygtYl45zwMDlbwIiocW9ubpCkGucX_O8KAfE_g2Eb3cH40jZqIsOogdaTHBg3ZopYNDN41KDus4099VFHRDe7srBesY3jkjG_uBKsV3E4NtQiVJDaq9FtyHrErqv9CGe77ycELoSHednr5ks718l5zGvDmaEsN1-K2XFbWuhzokV_dTf37JlYrvHd-qZJKRp2jZbSJ2qJkqAcEtqGFOSWqH7VdCnVOKOCuFPJUpzXIk4amA8fmWZbfeCPEw3Dj4EZJB_iTEnCB49OAbj2wxkk0KpFxjabo1l-yHdY7dvLBGEvdaz86sSFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c128d83f9a.mp4?token=QKrUhnTneGKYvTMaGVLa0rYvo8vM0tUjygtYl45zwMDlbwIiocW9ubpCkGucX_O8KAfE_g2Eb3cH40jZqIsOogdaTHBg3ZopYNDN41KDus4099VFHRDe7srBesY3jkjG_uBKsV3E4NtQiVJDaq9FtyHrErqv9CGe77ycELoSHednr5ks718l5zGvDmaEsN1-K2XFbWuhzokV_dTf37JlYrvHd-qZJKRp2jZbSJ2qJkqAcEtqGFOSWqH7VdCnVOKOCuFPJUpzXIk4amA8fmWZbfeCPEw3Dj4EZJB_iTEnCB49OAbj2wxkk0KpFxjabo1l-yHdY7dvLBGEvdaz86sSFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درمان ریزش مو در کوتاهترین زمان
کشف شرکت دانش بنیان ایرانی در آنتن زنده شبکه ســـه ســیــمــا!!
😳
😳
ویدیو داخل لینک را حتما مشاهده کنید تا با تاثیرات عجیب این روش درمانی آشنا شوید
👨‍⚕
👨🏻
✨
🩺
بـیـش از ۳۰هـــزار خـانم و آقـا از این روش معجزه‌_آسا نتیجـه گرفتن
😍
روی لینک زیر کلیک کنید
😃
👇
https://www.20landing.com/214/2623
https://www.20landing.com/214/2623</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/698501" target="_blank">📅 22:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d068336a.mp4?token=vGoBepjI2VzzO5G2RE-3dxxsYdPexfzvSV3HQkYMl3LZXXnCpc4MjZf2jkLMxKRdkUbDdvV8zdNmT6w5i-zvrOYdirLwQvo9JkBbY_MEh3BUcwx48romgJd_ZQheqwgDqL04bc1qTP7OYsjYcRP2K3wWZjQqkHoutq70P2xeh0ATlxf2nuWm20HQxr7WVy5dgZv0fb2byfUEDLiTqwc-Ou3q1L7U5lQakly8S76mBGpP7oHit2TWN-1bf9T5_zyQg5ysTFrmoR6bEwpI_RCn8nrEFCxCZ_DrGVjGkUdESsS6rLZA8mOyo2QYHvfGcjQc_JsDpwGWgyOrm02JOMFXmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d068336a.mp4?token=vGoBepjI2VzzO5G2RE-3dxxsYdPexfzvSV3HQkYMl3LZXXnCpc4MjZf2jkLMxKRdkUbDdvV8zdNmT6w5i-zvrOYdirLwQvo9JkBbY_MEh3BUcwx48romgJd_ZQheqwgDqL04bc1qTP7OYsjYcRP2K3wWZjQqkHoutq70P2xeh0ATlxf2nuWm20HQxr7WVy5dgZv0fb2byfUEDLiTqwc-Ou3q1L7U5lQakly8S76mBGpP7oHit2TWN-1bf9T5_zyQg5ysTFrmoR6bEwpI_RCn8nrEFCxCZ_DrGVjGkUdESsS6rLZA8mOyo2QYHvfGcjQc_JsDpwGWgyOrm02JOMFXmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای سرپرستی و رسیدگی به فرزندان توسط رهبر انقلاب در زمان‌های معلمی همسر شهیدشان
🔹
توصیفات حدادعادل درباره عروس رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/698500" target="_blank">📅 21:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
آیا زدن سه کشتی متخلف در تنگه هرمز توسط ایران باعث نقض تفاهم‌نامه شد؟
🔹
عدم اطلاع کرباسچی از ۴۲ مورد نقض تفاهم‌نامه توسط آمریکا و نامه معاون عراقچی به سازمان ملل درخصوص نقض تفاهم توسط آمریکا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/698499" target="_blank">📅 21:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698498">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7358016f4c.mp4?token=QadeA6jAD8WO_VScmnlPBpHg5wnhWfl1b_SPVYWY3prMYqCB1gQdp9VBGI31gZGqtj_A_vTOPsLYlB1wIuMfprMYBQCv-VcBJiLJW4xlZazwg_BppTBAgj8l1l9mGyEnw81et-eki5WdAhgmBXCMK8IfEwzGt2NQtELujwQGTemy0f-DsOj2yDkfQ3c8EbGptsPD2b6mEH4fC3TL-xVtPYg12qsxjfHDktzBWFVBLpwPHh8a0mcDpdFdLtim76Tp_U--vnYU9kyXSVVwFn_g42XCwl5d8s4B15-X54p2OkEM-K6yWdTT0OWfEi8NIpaeI85yIhAAbXU6HB0Bx5yayg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7358016f4c.mp4?token=QadeA6jAD8WO_VScmnlPBpHg5wnhWfl1b_SPVYWY3prMYqCB1gQdp9VBGI31gZGqtj_A_vTOPsLYlB1wIuMfprMYBQCv-VcBJiLJW4xlZazwg_BppTBAgj8l1l9mGyEnw81et-eki5WdAhgmBXCMK8IfEwzGt2NQtELujwQGTemy0f-DsOj2yDkfQ3c8EbGptsPD2b6mEH4fC3TL-xVtPYg12qsxjfHDktzBWFVBLpwPHh8a0mcDpdFdLtim76Tp_U--vnYU9kyXSVVwFn_g42XCwl5d8s4B15-X54p2OkEM-K6yWdTT0OWfEi8NIpaeI85yIhAAbXU6HB0Bx5yayg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توجیه نتانیاهو برای شروع جنگ بعدی در منطقه: این یک نبرد تمدن در برابر وحشی‌گری است؛ ما مدافع تمدن هستیم. ما آماده‌ایم تا با وحشیان مبارزه کنیم!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/698498" target="_blank">📅 21:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df041a4fb9.mp4?token=vGrxhR2OhLxnA_B8mKfEewtoInVgD6nlEtnWZxIP9uKSIJ8njdZ5nophJ67cNVv-MsHi7c3Q7fjTwaJKarmoYErpVf56I0gYVwk6xOlkacPNGagTIPyVBjBE9nAU_OnMkJH2G2GPqHRRfs0rETO0CWOZZz3OmG5qChEqsXmR_WH7pc7Vsp5-X8F20FfsjONsc1sqZacnoCrNZsza4vdSiqnF0tZZfwsZCh1JMdgFB7tngEkA3QOf3bv0SJhXZnIWGWFENXY-4ubmdXnIYQDnHJrp910Z8pHh7_KzSqez0Kw_QbB2LOR6-DX6uHRZQrmtdXqO8Be_ui8xEz_QL5zNWaPslsv4Y9U0j5XNs6CUe8BhaLpTjk_tzqwh_tcLyDWrz-ZgDGc_Ihj874uHYMYAcajYwFeI4PaB58r6xL3nBh-Hsr9vOZn8Afg87IjLhIP0P1Kc-3jcQkHoNBU77euzIByYQ2123AhZyBGNUIAYYCwqOAAsaKWKJzOUZxLxC4_gwdMAXLNL2Y9tZCAs6XwpY74XfemE8Y2BRRyshcew76RmrXB0h-a1dZBWeoPc86zPG6UdR4KWTG_3eQ_tCqRbnPu3WbhB-JpOSWrAEHrsvNyIPB6Snw1lbImrpT-HY7Jdpwt0lYRf7c2Bx66FlB61aa5V5BJdvocER6vSbcheuGs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df041a4fb9.mp4?token=vGrxhR2OhLxnA_B8mKfEewtoInVgD6nlEtnWZxIP9uKSIJ8njdZ5nophJ67cNVv-MsHi7c3Q7fjTwaJKarmoYErpVf56I0gYVwk6xOlkacPNGagTIPyVBjBE9nAU_OnMkJH2G2GPqHRRfs0rETO0CWOZZz3OmG5qChEqsXmR_WH7pc7Vsp5-X8F20FfsjONsc1sqZacnoCrNZsza4vdSiqnF0tZZfwsZCh1JMdgFB7tngEkA3QOf3bv0SJhXZnIWGWFENXY-4ubmdXnIYQDnHJrp910Z8pHh7_KzSqez0Kw_QbB2LOR6-DX6uHRZQrmtdXqO8Be_ui8xEz_QL5zNWaPslsv4Y9U0j5XNs6CUe8BhaLpTjk_tzqwh_tcLyDWrz-ZgDGc_Ihj874uHYMYAcajYwFeI4PaB58r6xL3nBh-Hsr9vOZn8Afg87IjLhIP0P1Kc-3jcQkHoNBU77euzIByYQ2123AhZyBGNUIAYYCwqOAAsaKWKJzOUZxLxC4_gwdMAXLNL2Y9tZCAs6XwpY74XfemE8Y2BRRyshcew76RmrXB0h-a1dZBWeoPc86zPG6UdR4KWTG_3eQ_tCqRbnPu3WbhB-JpOSWrAEHrsvNyIPB6Snw1lbImrpT-HY7Jdpwt0lYRf7c2Bx66FlB61aa5V5BJdvocER6vSbcheuGs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کرباسچی: خیلی از گرفتاری‌های کشور ناشی از کم‌کاری وزارت خارجه است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/698497" target="_blank">📅 21:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698496">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtdvCE0sxUyK4nDXXDhoDuJyAzP-jzJvRkAnmmhheG2UFVaKctmgmzNLFIDTSaCyFugibp2sP8TdCPTizXMjyzVMHOn9D1nMFHcMjXJm5Z0V2mz5zHVTjfbZcNNvpzL788RVK99nrdyZ_XpayTUpfomEhIj3-DBw_EBoulzeDpIjr69Q3M9nq8pbT_MxTbH7M9a1yks8_4Y4c_itd-t-v4vD5nJrvhCiyvrosHbCgFBLoAb9xcLNQCL6W2kLx8j3qYCr0EK_2fYbliz6n_NosCJ_8U7hhji-NYl3CIrplJzZNifDC5Da-MAZQoO1_NRMIuZ9E3nkZtfCBepEYGzMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اپراتورها خواستار افزایش ۱۰۰ درصدی تعرفه‌ها شدند
🔹
در پی انتشار اخباری درباره افزایش ۴۰ درصدی تعرفه خدمات موبایل، دیجیاتو موضوع را از روابط عمومی همراه اول، ایرانسل و رایتل پیگیری کرد.
🔹
هر سه اپراتور با ابراز تعجب از رقم ۴۰ درصد اعلام کردند که درخواست آنها افزایش ۱۰۰ درصدی تعرفه‌ها بوده است.
🔹
اپراتورها می‌گویند نوسانات ارزی، تحریم‌ها، آسیب‌های ناشی از جنگ به سایت‌های ارتباطی و رشد هزینه‌های تجهیزات و نگهداری شبکه، فشار اقتصادی سنگینی به این صنعت وارد کرده است.
🔹
به گفته آنها، درآمد اپراتورها ریالی است، اما بخش مهمی از هزینه‌های توسعه شبکه وابستگی ارزی دارد؛ شرایطی که توسعه زیرساخت‌ها و ارتقای کیفیت خدمات را دشوار کرده است.
🔹
سه اپراتور تأکید کردند هرگونه اصلاح تعرفه صرفاً در چارچوب مجوزهای قانونی انجام خواهد شد و حفظ کیفیت و پایداری ارتباطات همچنان در اولویت است. / دیجیاتو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/698496" target="_blank">📅 21:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698495">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9Ol16KrELUGzYd2z-VLEl30T8rGI-x2S6UGBZkl5cx2xUiJkH4nJCanBFOcj1490-z5MXHA8MJmSTunrnr69eeMyw3ugTrIojbd_Wj5atCVk9m97twT58fr3aP-bl3ZuIC2c9ySM8H72z5WS1MjLK3aOLnLsJLXAyi8RuUy9P-KM-kpWDaF3s8nqcy3c8LUF4FfMlvvGs3RvSMfyV-t_LDvuhMSGA0lQLBZR5zNTZLju0gMvCoMSpWt374Jvexh9zAbf0po9kPCefrxxL4DUbl8n5s4bhth_FKgZrwzr-5pEtgIHzqXLzrw3KxiPcF8Jr-OXWLt6Bjn7-_Ww0HaPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: محبوبیت ترامپ در آستانه انتخابات میان‌دوره‌ای آمریکا به پایین‌ترین سطح تاریخی خود رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/698495" target="_blank">📅 21:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698494">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd_u6k8U8PhREi5RCAqpa4PDF-oVNqRz4ZCVvo3JpHeHYNZiKDnOF4E-j-5PqNnncRf1Mg0UwstJgiNwZg4qSFmFUFUzhQWN6W-hOA1c1aVRVBz6maU0SSUiMSBS_6imG-sbsA_yj0lrapsPXqXdd4_GQXMt8219rhfy25Tq3LDPGdv5vTOB4mUuWc5ILTrEVVr4dldM2yy-pBHX5oxeX7aUGFgcLXVAPjZ6R7rHYxppmRE_Ve8V5CCvFLw74fniv3uj1LZehhQZAZO9hIH94nTNmIgp-QKiVOoCxp0fRm465dmsNzq0g6dwP98RsJ236r9kedgenE_Y_PBqmuGkmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیژن مرتضوی: وطن فقط برای روزهای آرام و گل و بلبل نیست
🔹
هنر، در روزهای سخت به وطن آمدن و کنار مردم ایستادن است. جانم فدای ایران؛ جانم فدای مردم ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/698494" target="_blank">📅 21:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698493">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714fb5cb99.mp4?token=e8SwR4tk-nx6Pvjrd00IGFcSu5YZnAPeXSm1BPsg5nmpf4ThsEoPLboI3JdtGXTZ2FSv9nAfyR-r-42CVeufVtaRIJFCT9vrRqb65nF_LXFcpUQ8IiXKddbvJayF6XMoxa8ab-f92vr2bfC5WDqTXhsv-sRlesAsKWw11VANseC9AMkXHryK5hxch8wzPV9j0Pk5O2l1a7F-5kEuAarduy6jDftDytatIWJLK-ZxRSsyS3jvXoewPbelw_k_9efeYGD5m4uKYXuL218IsX-fJu6KCNgQ5r_K-4gCnBg9UTAF2ZlHUaEC3NxSCjEdwWrRQWpu80P4F6Zkph48rrXKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714fb5cb99.mp4?token=e8SwR4tk-nx6Pvjrd00IGFcSu5YZnAPeXSm1BPsg5nmpf4ThsEoPLboI3JdtGXTZ2FSv9nAfyR-r-42CVeufVtaRIJFCT9vrRqb65nF_LXFcpUQ8IiXKddbvJayF6XMoxa8ab-f92vr2bfC5WDqTXhsv-sRlesAsKWw11VANseC9AMkXHryK5hxch8wzPV9j0Pk5O2l1a7F-5kEuAarduy6jDftDytatIWJLK-ZxRSsyS3jvXoewPbelw_k_9efeYGD5m4uKYXuL218IsX-fJu6KCNgQ5r_K-4gCnBg9UTAF2ZlHUaEC3NxSCjEdwWrRQWpu80P4F6Zkph48rrXKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با استفاده از این کدها، تصویر خود را به هوش مصنوعی بدهید و خروجی‌های جذابی دریافت کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/698493" target="_blank">📅 21:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698492">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
قالیباف: تفاهم علاوه بر بازدارندگی به نیروهای نظامی ما کمک کرد تا قوی‌تر شوند، تاب‌آوری اقتصادی آن‌ها بیشتر شود، حزب‌الله لبنان قوی‌تر شود
🔹
ما با این تفاهم فرصت و منابع کافی پیدا کردیم که مولفه‌های قدرت خودمان را قوی کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/698492" target="_blank">📅 21:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698491">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24e20cf932.mp4?token=SXJOU4Yeso3CzAeRHEpJYlvoV3thgPvWjBCfxSzN7T1Sn-ewWUO1GQyNJj81imi8XBrolht0Kw6d-c9-3NHemxPKV586L-MaouRYWeiM8WqQDZwuO4OLOGzXWrFaM9qEZ8UnrPdhJcs1qPqzVbAEI3r2UX8jg-nQ-L7_LtH_fTf9qSi2moWI-Kw9XayE4svStnQBDD8dXQ4pyxafojwJCNZpdtMYDiuqjQBb43whv-Iec4qkUxx-9-hinchfX3av3amEfM6h2rVC-KPxW8X4OtxwQY15RXHSdS-KfF_z7e2co-vEaS9L1u73fYMLXwicxRkDJmbC6sSusdzXMu1hb0jDNS77Bgi7ULsV0BZj5beFTW56wBiap_TecgZLXXRuue0oMty8nmy4irW-eYGM_28lhGrMg4Duui6l53E8FGGq_e31vIjPaF8CoDMuHc4NGNpE8GYXJedWoo7kn-b-B6GqPcEtQs69xKwA9L53IrAmccwQZ_wbadkrx7YmRFnR3BLOT5O5QATGLGPkAuQAow7ft0zpj3z9gLtxeBb6bQmPBnSC1Y5KfNN8GgFMlNF0-Jgd5L16xVtoRrFkGMjkOEwCmyouqZCI9HbKDZk3ffsmwfu_6FKRyTQI3KYL9HGyfD2rU8Rq0kQ1jNaPO02GTN_cUXkwsRxKQAsK1ZVnZRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24e20cf932.mp4?token=SXJOU4Yeso3CzAeRHEpJYlvoV3thgPvWjBCfxSzN7T1Sn-ewWUO1GQyNJj81imi8XBrolht0Kw6d-c9-3NHemxPKV586L-MaouRYWeiM8WqQDZwuO4OLOGzXWrFaM9qEZ8UnrPdhJcs1qPqzVbAEI3r2UX8jg-nQ-L7_LtH_fTf9qSi2moWI-Kw9XayE4svStnQBDD8dXQ4pyxafojwJCNZpdtMYDiuqjQBb43whv-Iec4qkUxx-9-hinchfX3av3amEfM6h2rVC-KPxW8X4OtxwQY15RXHSdS-KfF_z7e2co-vEaS9L1u73fYMLXwicxRkDJmbC6sSusdzXMu1hb0jDNS77Bgi7ULsV0BZj5beFTW56wBiap_TecgZLXXRuue0oMty8nmy4irW-eYGM_28lhGrMg4Duui6l53E8FGGq_e31vIjPaF8CoDMuHc4NGNpE8GYXJedWoo7kn-b-B6GqPcEtQs69xKwA9L53IrAmccwQZ_wbadkrx7YmRFnR3BLOT5O5QATGLGPkAuQAow7ft0zpj3z9gLtxeBb6bQmPBnSC1Y5KfNN8GgFMlNF0-Jgd5L16xVtoRrFkGMjkOEwCmyouqZCI9HbKDZk3ffsmwfu_6FKRyTQI3KYL9HGyfD2rU8Rq0kQ1jNaPO02GTN_cUXkwsRxKQAsK1ZVnZRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کرباسچی: باید نگرانی های آژانس اتمی را رفع کنیم! / مجری: همین یک سال قبل رفع کرده و آنها هم تائید کردند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/698491" target="_blank">📅 21:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698490">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQny0l1d9MNNBw-O1vk-IiArB0x3s1-g7Y3B3hJVkKCKPFcU_JwVVW9NZvkqiglVm6LMAGIEuPRyCIMcuwZh1znCebRyCkmD7Kj-o9DcBalvC99lkGhEH7-noHzYj_jP_4zwBzwIG0li5aeRu7BZ90UT8Yri62TvA6oWIB7pAQ-5yzu8Pm_Zbh-9tB_ybRYhGOnfz1du-cH5AgfLDozdK805O9EtZAkgO5u9gwNn6-5nrQYWdUfK7PwapAg5pbJDF7cposNh0tXesQpGAn09MVPyWAruxxBXA-FBKVlZ-N0wsmly-ez0vPqiTPxFHUbT8Zu0SwRgp4IBZjOFNOo25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پروازهای مشکوک اسرائیل بر فراز سوریه و عراق | آماده‌باش در آسمان منطقه | آیا اسرائیل در حال آماده‌سازی مسیر حمله به ایران است؟
🔹
پروازهای مکرر جنگنده‌های اسرائیلی در حریم هوایی سوریه و عراق، در صورت تأیید گزارش‌های مربوط به این تحرکات، می‌تواند بخشی از آماده‌سازی عملیاتی برای سناریوهای نظامی احتمالی علیه ایران باشد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3252460</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/698490" target="_blank">📅 21:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698489">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c8409f67.mp4?token=fpj--uHXJsaOi0q84ia-bUMTDiwNJIkNjwlT1x39O-OyTCnQhfTC0NqvCT0bidBY4GMZW5HKmtafs6c-99CAw9eMCVnlCgiZRpYYQKo5dJlefwgUx4kXiMmm0qje_wO2pyUwYotcd_XK0rRW40p_onsdV8kTrmanArfQO-YLwCDuMJXDSDOL9969WtmX2ND_iYquthwvMaL8wGGSYrMWEcHc9ANl9rnlKM28iJZFyBpY_6mwS7sN5sqTaY50oxrbPxuhh2cyTZJR2g35ear5sYn5IcuO5gy7SKZ1vvUW_rgoEf6D-DlgYbttvEUwvELnflBeQD-xt1mOoIy3CdTccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c8409f67.mp4?token=fpj--uHXJsaOi0q84ia-bUMTDiwNJIkNjwlT1x39O-OyTCnQhfTC0NqvCT0bidBY4GMZW5HKmtafs6c-99CAw9eMCVnlCgiZRpYYQKo5dJlefwgUx4kXiMmm0qje_wO2pyUwYotcd_XK0rRW40p_onsdV8kTrmanArfQO-YLwCDuMJXDSDOL9969WtmX2ND_iYquthwvMaL8wGGSYrMWEcHc9ANl9rnlKM28iJZFyBpY_6mwS7sN5sqTaY50oxrbPxuhh2cyTZJR2g35ear5sYn5IcuO5gy7SKZ1vvUW_rgoEf6D-DlgYbttvEUwvELnflBeQD-xt1mOoIy3CdTccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد تلویحی کرباسچی به نوشیدن جام زهر  کرباسچی:
🔹
باید با یک توافقنامه و ارزیابی غیراحساسی جنگ را تمام کنیم. امام خمینی (ره) در زمان پذیرش قطعنامه فرمودند که من جام زهر را نوشیدم و با خدا معامله کردم.
🔹
اینکه شما هر شب در تلویزیون کارشناس بیاورید و بگویید…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/698489" target="_blank">📅 21:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698487">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
پیشنهاد تلویحی کرباسچی به نوشیدن جام زهر
کرباسچی:
🔹
باید با یک توافقنامه و ارزیابی غیراحساسی جنگ را تمام کنیم. امام خمینی (ره) در زمان پذیرش قطعنامه فرمودند که من جام زهر را نوشیدم و با خدا معامله کردم.
🔹
اینکه شما هر شب در تلویزیون کارشناس بیاورید و بگویید پدر آمریکا را درآورده‌ایم دردی از مردم ما دوا نمی‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/698487" target="_blank">📅 21:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698486">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk8FMLtJr1iqlgkLgE44od3O1GxpF-LtOVObH6bF-pyq1Idiu1nhJ4Q8XZHeVQie6_s1QzcOZ_tEBDDsLJy7pP5xgTztbQzS8OU83v_QZe9aASemkvzG5HbXf07u344_FcsdPNhUz9p1iJ0oBTEnphgtCeMq76OjDUFH5JxpZMfbkOrU_7bIMqCMFFt3kFQVaMmfqB6GIigetzdZ_52kfj-NZ7xXcyimVgECxLLaA8tT4jZH30JNCb-C2ZIg_eaVu_NE0L_KHrOlov7BAfPyJ5PiwVnIoDa_leFF4H2vSjR-b4GgTqurdlmXC6NpnHZFrNsn9nhFDaDXAQsOdJHIGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف در واکنش به ضرب‌الاجل‌های بی‌نتیجه وزیر خزانه‌داری آمریکا برای فروپاشی اقتصاد ایران: به وزیر خزانه‌داری آمریکا نوبل فیزیک بدهید! او با پیش‌بینی‌هایش توانسته بی‌معنی بودن مفهوم زمان را ثابت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/698486" target="_blank">📅 21:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698485">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VoHICnsmbJC4oB77xePza0NfiNUpUjflS9a7dHA67cOzPCj8oK4lahBI7dAZszg1Bhg6HlSvuqAYMBUb9IK9zDltJxbVlDQc4ixQCIEMyqhUGklpt5Xp89FqK3r4BDCYzDAeWzD1dTp6eLViweVUTY3Q2vCEx1VHNcMiCRTE1DSxHPzuJe79JL-by0MHVuy6A71ICsorzG06eRWtrQEI5n35ulBFcIjAm9CfOlIscfHozMjFXZ1i8DPI22cIYYpd5u9oJx6YfGDDvyZwrhCkj8plAGRDwNbcsOO16o7SDV59A_XXn10HCaiAiNDvHJsVqpviCexuVyi71tihlw4Jtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفر رئیس اف‌بی‌آی به روسیه پس‌از ۱۳ سال
رسانه آمریکایی ام‌اس‌نَو:
🔹
کش پاتل، رئیس اف‌بی‌آی، برای مذاکره به روسیه سفر کرده است؛ سفری که نخستین سفر رئیس این نهاد به روسیه از سال ۲۰۱۳ محسوب می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/698485" target="_blank">📅 21:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
قله تفتان؛ آتشفشان نیمه‌فعال ایران
🔹
دومین قله آتشفشانی نیمه‌فعال ایران، قله تفتان با ارتفاع ۳۹۴۱ متر است که دو شاخۀ آن، بلندتر از سایر قله‌های منطقه‌اند و از دهانه‌های آن گازهای گوگردی متصاعد می‌شود. این آتشفشان در سال‌های ۱۳۴۹ تا ۱۳۵۰ آخرین بار فوران کرده است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/698484" target="_blank">📅 21:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1U96rBst8Ow_-1LN0fnT2IuSmdSVESm5C-zAQfUiz1-5-k_i_zVHMzmBBvf4XjpuPkmk08mKLoS23sth2H3w_kJCynUq_6ZKV2W2aQQ_Uu2YosQI8II3qkvmXzfRte4BYjEa_QjhlzEoePFbx_RdaE64_RIFgXn-PLnTLbEATKGY2zpSuLMeJRV1w_iFqRnaa-lYIbK1fbMdj7mXLZ_Gg4Nbq56lES-Dj_AVyoj3i35rk-SZQFpQwn0UcgKtVfYDZEwUq7LhvSzujbeRpYy9l4jzLNG6u7txxrhqtUzNZff5u7ykYuuRhWZlt9_dMSgUh2ecKIzKW-KEQboZqquVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امکان دسترسی‌پذیری نابینایان به محتوای فیلیمو فراهم شد
🔹
در راستای تحقق اهداف مسئولیت اجتماعی و ترویج فرهنگ دسترسی‌پذیری دیجیتال نسخه اپلیکیشن و وب فیلیمو برای کاربران نابینا و کم‌بینا، به طور کامل دسترسی‌پذیر شد.
🔹
با فراهم شدن این امکان، کاربران نابینا نیز می‌توانند محتوای مورد نظر خود را از طریق پلتفرم دنبال کنند. همچنین با توسعه زیرساخت در این حوزه، بخش‌های ورود و ثبت‌نام، جست‌وجو، تماشای فیلم و سریال، دسته‌بندی محتواها، حساب کاربری و... در نسخه اپلیکیشن و وب این پلتفرم به طور کامل دسترس‌پذیرتر شد.
🔹
دسترس‌پذیری یعنی همه افراد، با هر توانایی یا شرایط جسمی، حسی و ذهنی، بتوانند تا حد امکان راحت و بدون مانع از همه ابزارها و فضاها (دیجیتال و غیردیجیتال) استفاده کنند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/698483" target="_blank">📅 21:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjFFpUcd1QZYpPWFVfBhNJjyWgaCz2hHaR5wtFl4T_rYEsnJkVO7lf78u13JCOEPyvwa9qH4YBIHB8VXun8KIhcK30-SpuihI-EsLSp6zPDzVz0DLXa_yjsNMC3bGFZxKql5DVnqm4-nGzBpwZBpamcFcMehPR6pmchUMHtLTyuUWtMLfyZrcxfqg3UqDAWesxX-3oUz3OIYnv-5EUrcU8EwyfWVdaGmBfimkn9ODEFfqX1kQeiqPsgHsGaM9d3EFZs4brvNciLeqvWAK38WLKMgABwziaK4e0yg7s6iU3ZjBYNlW2Bpbl3KETrr6-usFe5nhMXWnHCs2DM4ItwWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطوط تلفن سازمانی ۴ و ۵ رقمی نکسفون
راهکاری برای حرفه‌ای‌تر شدن ارتباط تلفنی کسب‌وکارها هستند:
🔢
شماره‌ای کوتاه و آسان برای به خاطر سپردن
📞
نمایش شماره ۴ یا ۵ رقمی سازمان در تماس‌های ورودی و خروجی
⭐
امکان انتخاب شماره دلخواه از میان شماره‌های قابل ارائه
🏷️
فرصت ویژه مهرماه برای خرید خطوط ۴ و ۵ رقمی نکسفون با تخفیف‌های ویژه
🔎
دریافت مشاوره و درخواست شماره‌ی دلخواه:
https://isp.nexfon.ir/khabarfori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/698482" target="_blank">📅 21:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d0c8a57f.mp4?token=XhNgj4xIQ-jmmpblBOu-AX1V91yW1vqZkz8a8t2WGvSPjlKTHznXr2LKo-KHtvWKebbrTdFEYek9ZabtcQu1g3jwnvG4fYXcYuCaiRxWhAJ96847ROykFKhp8jWsmOFmOveBdgD4Jm6gBvKAMuU1xuixvK7bfn3mw136LsGpnl14sx_xehVq6LsW7IMqM1BE5sOxI5ptF-0BzUrM1uimkPiO4MeFQAEjJ7nM0lJxP5j811kv9lYeoGLpawEE90rgM1mzoK_wX0LasR1TeHcEFbSi_VQ4-hCPVoD23Pe-7EkDEWLXe_xn3YZhOZc80VE2mOpkXYmcE4YXePrtvnrH_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d0c8a57f.mp4?token=XhNgj4xIQ-jmmpblBOu-AX1V91yW1vqZkz8a8t2WGvSPjlKTHznXr2LKo-KHtvWKebbrTdFEYek9ZabtcQu1g3jwnvG4fYXcYuCaiRxWhAJ96847ROykFKhp8jWsmOFmOveBdgD4Jm6gBvKAMuU1xuixvK7bfn3mw136LsGpnl14sx_xehVq6LsW7IMqM1BE5sOxI5ptF-0BzUrM1uimkPiO4MeFQAEjJ7nM0lJxP5j811kv9lYeoGLpawEE90rgM1mzoK_wX0LasR1TeHcEFbSi_VQ4-hCPVoD23Pe-7EkDEWLXe_xn3YZhOZc80VE2mOpkXYmcE4YXePrtvnrH_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سه نشانه که بیان میکنه یک نفر به شما احترام نمیذاره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/698481" target="_blank">📅 21:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698480">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
قالیباف: هم می‌جنگیم و هم مذاکره می‌کنیم
🔹
یعنی در زمان لازم با تمام توان می‌جنگیم و آمادگی خود را بالا می‌بریم، وقتی می‌گوییم هم می‌جنگیم و هم مذاکره می‌کنیم منظور این نیست که جنگ بی‌پایان انجام می‌دهیم، یا مذاکره همیشگی، بلکه منظورمان این است که جنگ می‌کنیم تا دشمن مجبور شود به خواسته‌های ملت ما تن دهد و اگر نداد، شکست را بپذیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/698480" target="_blank">📅 20:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a3ba8961.mp4?token=S-_pMzQVX9ukoYZnNs52zCoiZl8ykHrFd4SzWLudFhJ8q_xkEDclfORsx0pAv90_Kd2jEIpyOQzVlJd1FGs652B1nMTkJkfu8pHKw5votWGxXaqwkfANcO_ImRBf6_cCllW2CVy-j27jq7AbP4Kwght-1DYCadJ3LyHH4sqTnrUzNBvUODVQuhIlqPhxqZWyvGpe52JwBBFHKGrbXpyx4RzB44Kev--DrmAGc0qqsvTLaUA9uLNvsyXoxrsdeMTUdoXf3PgSjuEUhMxpE5cu22Sjb8cMMgaXVhxMIF3tRTyLrFxHiUjT0TwLPZnIamoBZs9W7fPI9dGrw0vs4kegYRIDXYIdT_NXPvysAHbPKQtuNGxV3G-VYt4UOSYyY9VOwvSNlZ9fiMXxYahMKcT5UMDLz3tAFL5uPr28s3ej02mUfnUVPU-t_RlO70sjhwwxdfOotQbSoHWzkK0ZfEgvS6dC8Ke9FWHtF4_RA3cQ64MFtPeErrVA0nOVbxCAfCP60dZCaXsUkQxjaUXwElHdcNl4Wn3n3Ce45EwxzBe7L8WXZOgRaNs2HafNhW2o2ufy-LPqMHwwYapQYtpXjZt0ifAS-GTPedlVJ4WvCdUgAYk8bKhj35v-r1JWCTSm93f3G_HlaLSPHZKQyw4NqTVmKIc7Nv2P0ZWWcsNhP9wzzXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a3ba8961.mp4?token=S-_pMzQVX9ukoYZnNs52zCoiZl8ykHrFd4SzWLudFhJ8q_xkEDclfORsx0pAv90_Kd2jEIpyOQzVlJd1FGs652B1nMTkJkfu8pHKw5votWGxXaqwkfANcO_ImRBf6_cCllW2CVy-j27jq7AbP4Kwght-1DYCadJ3LyHH4sqTnrUzNBvUODVQuhIlqPhxqZWyvGpe52JwBBFHKGrbXpyx4RzB44Kev--DrmAGc0qqsvTLaUA9uLNvsyXoxrsdeMTUdoXf3PgSjuEUhMxpE5cu22Sjb8cMMgaXVhxMIF3tRTyLrFxHiUjT0TwLPZnIamoBZs9W7fPI9dGrw0vs4kegYRIDXYIdT_NXPvysAHbPKQtuNGxV3G-VYt4UOSYyY9VOwvSNlZ9fiMXxYahMKcT5UMDLz3tAFL5uPr28s3ej02mUfnUVPU-t_RlO70sjhwwxdfOotQbSoHWzkK0ZfEgvS6dC8Ke9FWHtF4_RA3cQ64MFtPeErrVA0nOVbxCAfCP60dZCaXsUkQxjaUXwElHdcNl4Wn3n3Ce45EwxzBe7L8WXZOgRaNs2HafNhW2o2ufy-LPqMHwwYapQYtpXjZt0ifAS-GTPedlVJ4WvCdUgAYk8bKhj35v-r1JWCTSm93f3G_HlaLSPHZKQyw4NqTVmKIc7Nv2P0ZWWcsNhP9wzzXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا مطلبی: انعام فقط پول اضافه نیست؛ احترام به زحمت آدم‌هاست، و اصالتت رو از رفتارت با کسانی بشناس که برات کار می‌کنن
🔹
برای ثبت نام همایش بزرگ استاد مطلبی در مشهد از کد تخفیف BMT72 در لینک زیر استفاده کنید
👇
https://evand.com</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/698479" target="_blank">📅 20:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b81b63d6.mp4?token=g5bhV5vc2bv3owryNdzNcqnOOifzxOYHo7quN5CzZj-D6TO9kyjIT2Uuu454o9b-q3XeRTY0zOn5n38K8wQq5-h8PTLvvh9GyC_psmGVJNYo_yZS2t3szdxDY23OGcBUyhVnZVH1GOy7tbxlGnXl8JQhtQUQJuAzkwyNIhNxbnoG5Ww5IYVj_pypvqBzYt0GNJrlT3YxUJVmE9nBkfLbdR7_jgNJ-GoAjTolBF6rHYfTOgj-Pe_kMqVNFPdcJGYW32Kdkb7k4caBqTpMa6xfFFRVc3sxDIV3z3UgydAbKxb0gCm4CvycL7n82XN1BVtLWQR1yztaAnEinXwOU9yvRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b81b63d6.mp4?token=g5bhV5vc2bv3owryNdzNcqnOOifzxOYHo7quN5CzZj-D6TO9kyjIT2Uuu454o9b-q3XeRTY0zOn5n38K8wQq5-h8PTLvvh9GyC_psmGVJNYo_yZS2t3szdxDY23OGcBUyhVnZVH1GOy7tbxlGnXl8JQhtQUQJuAzkwyNIhNxbnoG5Ww5IYVj_pypvqBzYt0GNJrlT3YxUJVmE9nBkfLbdR7_jgNJ-GoAjTolBF6rHYfTOgj-Pe_kMqVNFPdcJGYW32Kdkb7k4caBqTpMa6xfFFRVc3sxDIV3z3UgydAbKxb0gCm4CvycL7n82XN1BVtLWQR1yztaAnEinXwOU9yvRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی: رئیس جمهور روسیه درخواست ترامپ را جدی نگرفته است
🔹
روسیه شب گذشته و ۲۴ ساعت بعد از اعلام آتش بس ترامپ با موشک‌های بالستیک به تأسیسات انرژی CHPP-4 در کی‌یف، پایتخت اوکراین، حمله کرد، یکی از زیرساخت‌های کلیدی تأمین انرژی این شهر.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/698478" target="_blank">📅 20:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHXCmGSS_VL3TCf808A-MYUxSZllPG2MitCWWHyNbE2ChRGfSavdunepQ-L04Afd4r7TZl2pq5FZedJSoawo4g4UXMv-4TkqCHW9ZZzJv1fWkGIMj6OlNN4BKM4xj2VgoUe7l5VYoLWHgVcAaeEKycZxK_7ebtNSnaHwmwV7iEZhRhnjEs1wtw2pr57CaR2skuCntG89o0apavf4TO-ykdmqfBsl3yBIyq0jd2TFlacNv8BFg4h1ZD8j9lZ7DIa8bD2htOurn7kD43SqKpJi3MCct_VTs8h2TIo4shNyce4-_nSgWvv-zz7w1wchtE-brcixYKnPcR0addae36frng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناخدای هرمز
🔹
در روزهای اخیر، افزایش موارد اصابت به نفتکش‌های خارجی متخلف در تنگه هرمز، معادلات موردنظر واشنگتن را با چالش جدی مواجه کرده است. برخلاف ادعاهای مقام‌های آمریکایی، تحولات میدانی نشان می‌دهد که شرایط منطقه لزوماً مطابق خواست کاخ سفید پیش نمی‌رود. تداوم تنش‌ها و اصابت‌های دقیق ایران در این گذرگاه راهبردی و عبور قیمت نفت از مرز ۱۰۵ دلار، نشانه‌ای از نگرانی بازارهای جهانی نسبت به آینده امنیت انرژی است. در چنین شرایطی، دونالد ترامپ شامگاه گذشته با لحنی تند اعلام کرد که صبر آمریکا به پایان رسیده است. اظهاراتی که می‌تواند بازتاب‌دهنده افزایش فشارهای سیاسی و اقتصادی بر واشنگتن باشد.
🔹
هشتصدوهشتادوششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/698477" target="_blank">📅 20:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IudZzyDP0EJNcPDb6-CbQgCYC2nrOJ1LdQawVru4nruYdviZB9eZZl0-C9esmE1O8Zjxryca4JjO3UYPMONKx-tmHHcTkDmR12P1b46BkDSPrf0dkLZw56IDL605aXm3AtDuNcqNUkymaHr4XkrAsMivvI8GjpYL2TR0n1dysAhuls9tuxGi-sl0EeQNl9LjZQWW6KgRzlGSioM_F6_j3kVhU06D5txCIt68m0rWricmS-ciODZQnHypdugkSwcyaBmMA2tvlwbSY2x8zwiJy7H4L4Mx5C_bTqmJnu-UbezGcGNeKUcHl28handsHbQprAGnIs9t4Wy7i-0_IapzwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰۰ ابزار کاربردی هوش مصنوعی!
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/698476" target="_blank">📅 20:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKhnhlR0X3RcxF4Efi-Dy_Eu9N9FY5pvxD-xpJu94HZiXnuJnmYod-f1pVVrILBRCNagg0ZOWMNh0Jy-uKo5V52djqvo9BIGbUK266DJaWn_HAg6KDy-Dcwj0TipdFX9Y58Dti8YyNN_OBFdXQM0vZndmRJIxVIPTa6GjTuTo79aoLOkmlVXRlLjEt0Jkm7XXfmIR5Q-_Fyj1imyfaOS-aTqaOUlMGCtPdxJqnKjrrvFWD3rl6HBFd0mUjmAAkO9R1vEezTJhR9WyymJJ4OBZpN1LP--ZC1GJcq4EGn7qQ7UE4VfGs1TIJcC7QkWTI7sTcC8w_ZqIvzZocVF7iko-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روش‌های محبوب دم آوری قهوه
☕️
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/698475" target="_blank">📅 20:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e081c75715.mp4?token=p96oweBADphvcGMA01zI4F6QPmZswbluHHSShgOa-ES2-l4dMexWCNbe2910SlNIMANJl8WvBIv6rwhdrUB0Uas6AXI_dt5kFgmHhxxljNJydpoUGOTXwXHfmJDzRb_pj847wt56zU_nhcULp30C5gyCcgP4gmLNLRp68FzI2FOt2XMWRB0Scj1ee9tmX7MXrcjUaC4V4Rx91R_AY_8XVTUr3XT5-ViN6f2iCpuxZeFelTIDx_EiDbaO1LRsf2ll-sb1-y2bxO7a0GdtGkvl8z4PZRx-IVsOhfe-YWMeEhI2r3UkvqrqiaHfV5hPCN3t_DSZdV6Vrl1ykPNRKi1pxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e081c75715.mp4?token=p96oweBADphvcGMA01zI4F6QPmZswbluHHSShgOa-ES2-l4dMexWCNbe2910SlNIMANJl8WvBIv6rwhdrUB0Uas6AXI_dt5kFgmHhxxljNJydpoUGOTXwXHfmJDzRb_pj847wt56zU_nhcULp30C5gyCcgP4gmLNLRp68FzI2FOt2XMWRB0Scj1ee9tmX7MXrcjUaC4V4Rx91R_AY_8XVTUr3XT5-ViN6f2iCpuxZeFelTIDx_EiDbaO1LRsf2ll-sb1-y2bxO7a0GdtGkvl8z4PZRx-IVsOhfe-YWMeEhI2r3UkvqrqiaHfV5hPCN3t_DSZdV6Vrl1ykPNRKi1pxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: نیرو‌های مسلح حمله دقیقی با استفاده از موشک‌های بالستیک علیه تاسیسات ارامکو در ظهران و ریاض و همچنین فرودکاه ملک خالد ریاض انجام دادند؛ تمام اهداف با دقت مورد اصابت قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/698474" target="_blank">📅 20:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698473">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">26-1 Ane Manaee (1404-02-15)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/698473" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وششم؛ بخش اول
🔹
"إِنَّ الَّذِینَ ارْتَدُّوا..."عِقاب و عِتاب الهی پس از تبیین کامل هدایت و اتمام حجت خداوند.  [01:08]
🔹
تحلیل مفهوم "تسویل نفس" و نقش نفس و شیطان در پدید آوردن تصویرهای ذهنی غلط و سناریوسازی‌های نابجا  [04:12]
🔹
خودفریبی و توجیهات ذهنی در مسیر مراقبه و محاسبه. ..اصلِ فریب، باور بی‌چون و چرای ماست به حقانیت خودمان. [16:40]
🔹
بت شکنی حضرت ابراهیم علیه‌السلام ؛ لحظه‌ی بیداری وجدانها، و نقطه عطف خودآگاهی به اینکه "ریشه ظلم‌ها در خود ماست."  [19:12]
🔹
از منظر قرآن بازگشت به خویشتن و مراقبه دائم نفس لوامه، عامل رشد و بیداری، اما در فرهنگ غربی نشان بیماریست. [26:50]
🔹
توصیه آیت‌الله شبیری زنجانی به جایگزینی اخلاق و انصاف به جای فضای تهمت‌زنی و بدگویی در حوزه‌های علمیه [37:10]
🔹
شهادت عمار یاسر در صفین، روایتی از نقش القائات و تصویرسازی‌های باطل در وارونه‌نمایی حقایق  [42:45]
🔹
انکار نفس و خودبرتربینی، ریشه همه جنگ‌ها و نزاع‌های بشری از قابیل و هابیل تا تاریخ اسلام و ادیان. [ 48:10]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/698473" target="_blank">📅 20:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698472">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDyTLRr8cEtSxDt044PibirEGlptA5DUnXqgna7ga-G79txuT-1gvIDMYQttAxOjDNa9kBT0pXIdbcnvDQW8D509MVF2MuDDwAoklcs0aJpEKwwDgfOTktF816ykQWydg2O0mcV3rg_YyoxuZjDQMB5T9JgmmhTCVLAsrOnZE5f6lp1m3Et10NP9PNtDcW_Q76bUuyfx4iO4_80dkhNuYYHtCNzQ05ZvYs2RZGQYmERjT_1i50g_BXecYbBOUH5St4uYJeFbGhrVdk2lW1bCly6nW-qm1V9X-kQGDRhpAS01wGLi1VSE5gOSi6MPzpDdICfRcIrjch430oCxeJxTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر رزمنده اسلام یاسر باقری، اهل بم که امروز در درگیری با گروهک تروریستی در منطقه کورین زاهدان به فیض شهادت نائل شد  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/698472" target="_blank">📅 20:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698471">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxy9p13rEfn95LFc7Sc4Mk-LWYSEiz3fNk-C7KgTn5jIjDQWWtqyisPdb44MuZ_m8UhP68tMYeN21qa0LmQbPRbkF5V0QDUqSU2K9ML8PczHKc0g9WBuYXofk7H85x9gJUWetzM8H3FCq3pAMXI0IJXNsWKwoUTM1cQhcKrrwq18Ae8pmJQ6TCfLKijyy8WigpNfrn8PA1CgIBkRR7Buz6Gtx7ym5BQ_bxoCRZulQew8BqicsGU-z73iTSY5yqP1-bxpeXBu9h6TwQ7HzrTBNvA2Yk94DZKOcv1Z85VqLtbKwa_1M1ZBePNM8P89VbV5ifKY-B1lpb7LSyyTvJWixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ چگونه سعی می کند از
شکست نظامی
،
پیروزی شناختی
بسازد؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/698471" target="_blank">📅 20:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698470">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb10134b1c.mp4?token=knoAOCB0Azut8ZHnve8tOw0IYE9OKMsGI8fYfiwExFryuoIgqHM_EiNMRQ8bkEQUGMjDRogimc5cD2_ulUOK5ePswipvSxjks3YC-CdwkpZPVzb0VPFXyO56k6bqWEvGRChNLVGIXZUH6nD_JXSWkd1bbKHig1PefYMc6vogVafw9nv181lseatsSRd0o4aFJWj6d4qlhPP9abV4rzt2A8MyqmvRdTP2jAoDYDABRqE4N4gRQ-oVCmWega9eBactgqHm_NKG977RjuNjmQv_pW6uS5z6KZaiC58kyNK1ii_nYhPZS-I_dQiQv0hTmjUN5nLxkmAFjKyrI8PpABGtiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb10134b1c.mp4?token=knoAOCB0Azut8ZHnve8tOw0IYE9OKMsGI8fYfiwExFryuoIgqHM_EiNMRQ8bkEQUGMjDRogimc5cD2_ulUOK5ePswipvSxjks3YC-CdwkpZPVzb0VPFXyO56k6bqWEvGRChNLVGIXZUH6nD_JXSWkd1bbKHig1PefYMc6vogVafw9nv181lseatsSRd0o4aFJWj6d4qlhPP9abV4rzt2A8MyqmvRdTP2jAoDYDABRqE4N4gRQ-oVCmWega9eBactgqHm_NKG977RjuNjmQv_pW6uS5z6KZaiC58kyNK1ii_nYhPZS-I_dQiQv0hTmjUN5nLxkmAFjKyrI8PpABGtiIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی سفیر جدید آلمان در تهران از آغاز فعالیتش در ایران؛ «از کوچه برلن تا چای با نبات»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/698470" target="_blank">📅 19:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698469">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
فرود اضطراری پرواز تهران - استانبول در تبریز
🔹
پرواز شماره ۹۷۰۰ ایران‌ایرتور با ۱۱۶ مسافر که از تهران عازم استانبول بود، به‌ دلیل نقص فنی ساعت ۱۸ امروز در فرودگاه تبریز فرود اضطراری کرد.
🔹
تمامی مسافران در سلامت کامل به سالن ترانزیت منتقل شدند و اقدامات برای رفع نقص فنی یا تأمین پرواز جایگزین درحال انجام است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/698469" target="_blank">📅 19:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698468">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
‏
سردبیر میدل ایست آی با اشاره به جنگ احتمالی بعدی: ایران اینبار همه را به جهنم می‌برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/698468" target="_blank">📅 19:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698467">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f171fea18d.mp4?token=WTEor_ULN6RrmbocrnaEIn9D-THJnPRyfHhuU-qeNhT_1h4FFwGmFVOt03yWuxb-4JbsRoiJA5CBmVvCj3vBQN8atnUtnR-3tcd9LIM_iS6LhTzZZKrfiwFFIFj9x7PW3BOD4lz8ROMqJ9TqWUVGmTkGh9LnpeJpI1YO5zYPdi9dqwAQWb-KXAvGJVAHP7DC5MPmeWr3HfDzzXJBLeXoCRPjcsEldCezElTT2YwsyAPyORDnj1gI5YeH0TOpPgn_6fLMINkA9kwt6t3KEBJ8r-R2NUORH7iphPAqvitxt0jaOuv8wNZqc4YUgovd2TNAFsm0Li6HeOpkCUusei4uiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f171fea18d.mp4?token=WTEor_ULN6RrmbocrnaEIn9D-THJnPRyfHhuU-qeNhT_1h4FFwGmFVOt03yWuxb-4JbsRoiJA5CBmVvCj3vBQN8atnUtnR-3tcd9LIM_iS6LhTzZZKrfiwFFIFj9x7PW3BOD4lz8ROMqJ9TqWUVGmTkGh9LnpeJpI1YO5zYPdi9dqwAQWb-KXAvGJVAHP7DC5MPmeWr3HfDzzXJBLeXoCRPjcsEldCezElTT2YwsyAPyORDnj1gI5YeH0TOpPgn_6fLMINkA9kwt6t3KEBJ8r-R2NUORH7iphPAqvitxt0jaOuv8wNZqc4YUgovd2TNAFsm0Li6HeOpkCUusei4uiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به آتش کشیده شدن تأسیسات سری استارلینک در بلغارستان
🔹
یک نماینده پارلمان بلغارستان از اقدام خرابکارانه دو فرد ناشناس در تخریب و به آتش کشیدن تجهیزات ماهواره‌ای مرتبط با جنگ اوکراین در نزدیکی صوفیه خبر داد.
🔹
افراد نقاب‌دار ۱۱ آنتن از مجموع ۱۷ آنتن استارلینک را در یک تأسیسات سری در نزدیکی صوفیه به آتش کشیدند. این آنتن‌های ماهواره‌ای از خطوط ارتباطی مورد استفاده در جبهه‌های جنگ اوکراین پشتیبانی می‌کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/698467" target="_blank">📅 19:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698466">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_oRg_SEWOhWm8_4LRf5K2NP2uSpiXW1kSvn-N3vc50r45LVOD3t4GN_7t_pSrS6nhkvZD2k-jntj3kuRdB-Uakh4D2Jbl2I07J5klQXBg88tyCTXg1Us1-1DAtv-VLLDAMyZdqMOI8GLJhy4Dse_gRp3GqymHa-mvSp-BQjUiIdgLfSvhkLwG6Nb8oYRMTOjFRDoIZwQbh0HVNK6ZK51Kbo0L4r7R-CKzSZTr5mZ03An20mnmWhnfZdSm8nwAeewsXsqKR9fIVMlJGFaX3E8esiTyVHEloigxLdf3nsWi348CtCfgYrjKxLMpb2dK7x8nWO0vTI7JZvKmakp6AqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلاش تمام شهرداری کرج برای روز فرهنگی ایران کوچک/ مسیری آغازگر برای احیای هویت این سرزمین
مهرداد کیانی، شهردار کرج ضمن گرامی‌داشت روز فرهنگی کرج و تبریک به اقوام گوناگون ساکن در این شهر:
🔹
امسال شهرداری کرج با همراهی اعضای شورای اسلامی و هدایت فرمانداری ویژه شهرستان، تمام ظرفیت خود را بر برگزاری باشکوه روز فرهنگی کرج متمرکز کرد.
🔹
این شهرداری اقدام به برپایی ۵۴ غرفه ارائه انواع محصولات گیاهی، صنایع دستی و... در محل محوطه تالار شهیدان نژاد فلاح کرد که اولین نمایشگاه تخصصی عرضه محصولات بومی محسوب می‌شود.
🔹
همچنین هرشب برنامه مفرح استیج با گویش کرجی میزبان شهروندان ایران کوچک بود. عصر شعر نیز در دوبخش شعر کرج و شعر با گویش کرجی به‌عنوان یک جشنواره تخصصی برگزار شد.
🔹
مجموعه این اقدامات و تکرار هدفمند آن منجر به احیای کلانشهر کرج از منظر فرهنگ و هنر خواهد شد که در عمل آغازگر مسیری برای بازشناسی فرهنگی ایران کوچک محسوب می‌شود.
🔹
روز فرهنگی امسال تجلی اراده همگانی دستگاه‌ها، ادارات و اقشار مختلف مردمی بود که توانست حول محور معرفی بیشتر ظرفیت‌ها، فرهنگ و تاریخ کرج قوت پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/698466" target="_blank">📅 19:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698465">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
سخنگوی سپاه: احتمال وقوع جنگ جدید کاملاً وجود دارد/ آماده‌ایم به هرگونه تجاوز، با قدرتی بیش از هر زمان دیگری پاسخ دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/698465" target="_blank">📅 19:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698464">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaU92x88Q4E_QllGqJ9aEKHdnx2ikKVOYfkVG_0c_S2TYljJSa1u5pxK7WLc5v2mvjsw5UtHAYgS2uz5GVN8-nnn8fvoIQLz6u2QwaLTM4kr1e69sBeG1Nbzq34AAHeIbR-cR4w9KBVXVz0Zh-6eHm3xQ6Asui9eAglHE26QMufeZohB64Msl1eXuPn5tuXv6oY-sfro1SYYP0iR8jhDVTYFBLcw7G8ko1HawuDTlL1Ao4Zcr133rME_fL_KPiy9k8Tlg0FkrspKToDYRUwV_EmECWlET4ANkZ6-PUTfiwDPsOBTS8dmb0tDnzK3ci4ApsTMFzNssP2-z6o5cB1k5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از دیدار امروز الهام علی‌اف رئیس‌جمهور آذربایجان با رئیس‌جمهور اسرائیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/698464" target="_blank">📅 19:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698463">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac361504bf.mp4?token=FRgzkmAhCEFaqQZLmwM9RooQ3kdO4OTRhDZdMnjFYTW0sGNJVV8xO7m76irBbXnBCm2GFgUoIs2l5p1bIsY7N0EqfVcn8Bzh_nqiJPQgA1w2RnxBaJessDH7AWdEoySqBl9AQe8n6wFrSI4H00x1NXsAWl8eh2auggiwjavakXozZ0JosfrVmP99sFkVeXUe5t4lCZLXH5kvclTXj8XEmUfXfwtAW6cr3Ip5xVHAj04VZ6g4TRkT2aRRXbfvVbKgFk7pYpHlGjqXoGRNdSTQqfmQLumc-Fg4VsHrEPF_535a37JLAVmVtWbz82gZFiLgHE4Nc4Pg4WUDbLGYUVegww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac361504bf.mp4?token=FRgzkmAhCEFaqQZLmwM9RooQ3kdO4OTRhDZdMnjFYTW0sGNJVV8xO7m76irBbXnBCm2GFgUoIs2l5p1bIsY7N0EqfVcn8Bzh_nqiJPQgA1w2RnxBaJessDH7AWdEoySqBl9AQe8n6wFrSI4H00x1NXsAWl8eh2auggiwjavakXozZ0JosfrVmP99sFkVeXUe5t4lCZLXH5kvclTXj8XEmUfXfwtAW6cr3Ip5xVHAj04VZ6g4TRkT2aRRXbfvVbKgFk7pYpHlGjqXoGRNdSTQqfmQLumc-Fg4VsHrEPF_535a37JLAVmVtWbz82gZFiLgHE4Nc4Pg4WUDbLGYUVegww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعید لیلاز: آمریکا پیش از جنگ به ایران پیام داد، کنترل نفت ایران
را به ما بدهید تا به شما حمله نکنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/698463" target="_blank">📅 19:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c371b5163a.mp4?token=EUWQaEzAkL8iBRu5RXDpdPEW6sQXhIYPTZR5G1xfJIDNHNQ_2l4PWbPeRE0YHjNFrgGcUZJls5ROdp5-rMGtxPV4XFI3rlv1h-taZET1YhToaaZCWmxmmXvSz5DmBX-tP52tVu6GOkUQakFGP5kFS19cVeWC7l1nzeBefE8-vBZENfwND83ePDItIELKbkeH6WMTEYAbFpm4QBNK9lhWG3Suce-jpMN7KejIdiUCmZ-fKaLxjHNrvR0-D0CAH3wbzeICSSrysfJt1reECTYP6pX-2bGsCnatbThOXfu387-ikQTi_zJjuWWgqVg26g1NL8sQFr-gGw_6kJJv_BrVC7dFJqXqOvOzRZcdCU7X_65FsrK3n_07KAhS-ntDK5faFior4mZCoQoBo6i2hkUEbvqEQ8uZp1shXCPehpaO6J74SyfO2NLT0X93R06o97TPKgGKbDXROiyOzP3ZJo1SG-qgGBiTrORXgkPyEtsixMjsPLIVEEzFtjcGnZlEMM_GymAKR7y0mIU_xONacQ09wCvTWV8_C9FJ0OCf8oU3JDUuV6InZtxEoixuATKtuwi399inILDubWhCrH4GCva9v4nQRbPX9XNNWsYq2eS6u-JwD15wZkOuAWgkdqp8jU8DqQsR6_9aCbWecL7VzcxYmbOmqrGxUldjbSo9gP0LFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c371b5163a.mp4?token=EUWQaEzAkL8iBRu5RXDpdPEW6sQXhIYPTZR5G1xfJIDNHNQ_2l4PWbPeRE0YHjNFrgGcUZJls5ROdp5-rMGtxPV4XFI3rlv1h-taZET1YhToaaZCWmxmmXvSz5DmBX-tP52tVu6GOkUQakFGP5kFS19cVeWC7l1nzeBefE8-vBZENfwND83ePDItIELKbkeH6WMTEYAbFpm4QBNK9lhWG3Suce-jpMN7KejIdiUCmZ-fKaLxjHNrvR0-D0CAH3wbzeICSSrysfJt1reECTYP6pX-2bGsCnatbThOXfu387-ikQTi_zJjuWWgqVg26g1NL8sQFr-gGw_6kJJv_BrVC7dFJqXqOvOzRZcdCU7X_65FsrK3n_07KAhS-ntDK5faFior4mZCoQoBo6i2hkUEbvqEQ8uZp1shXCPehpaO6J74SyfO2NLT0X93R06o97TPKgGKbDXROiyOzP3ZJo1SG-qgGBiTrORXgkPyEtsixMjsPLIVEEzFtjcGnZlEMM_GymAKR7y0mIU_xONacQ09wCvTWV8_C9FJ0OCf8oU3JDUuV6InZtxEoixuATKtuwi399inILDubWhCrH4GCva9v4nQRbPX9XNNWsYq2eS6u-JwD15wZkOuAWgkdqp8jU8DqQsR6_9aCbWecL7VzcxYmbOmqrGxUldjbSo9gP0LFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی آیة‌الکرسی به عنوان ضد طلسم در موزه‌ای در آلمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/698462" target="_blank">📅 19:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698461">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8513fdb997.mp4?token=chYEgqvE14z5B7tezVo8CEnWeiaJHA7DYI5GAT3ZW7w2zSDYFZrHKXatMySnSEMVB2IaivW4jTRSJkeHyxFXJOvIP4RRwfu-VZbbgfHugiz6aYhbsNqAXeXIFxYx0FUROWY4h-UStjghRMQwd4NzGCr64IIZ5cBeMGbjlK8GbQCr4e-zw1RUvayY7rY28lgdhxAoVAlZT09djScLTW8ac2FeylpYkQWebZYolSL2Dk0vXVavlwUpmkvXSWKwooXvXZ5G4DXKW4WJgWoJZjnDu7yDtGIYdANDcpJ4fUUFgnn96y2U33BCcyI5237Egk4losD5nOHWImnTlMtnNH97nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8513fdb997.mp4?token=chYEgqvE14z5B7tezVo8CEnWeiaJHA7DYI5GAT3ZW7w2zSDYFZrHKXatMySnSEMVB2IaivW4jTRSJkeHyxFXJOvIP4RRwfu-VZbbgfHugiz6aYhbsNqAXeXIFxYx0FUROWY4h-UStjghRMQwd4NzGCr64IIZ5cBeMGbjlK8GbQCr4e-zw1RUvayY7rY28lgdhxAoVAlZT09djScLTW8ac2FeylpYkQWebZYolSL2Dk0vXVavlwUpmkvXSWKwooXvXZ5G4DXKW4WJgWoJZjnDu7yDtGIYdANDcpJ4fUUFgnn96y2U33BCcyI5237Egk4losD5nOHWImnTlMtnNH97nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا هوش مصنوعی جای فعالان صنعت بیمه را خواهد گرفت؟
🔹
فناوری و هوش مصنوعی در حال ایجاد تغییر بنیادین و تحول اساسی در بخشی از فرایندهای صنعت بیمه هستند؛ تغییری که می‌تواند نقش شبکه فروش را نیز وارد مرحله‌ای تازه کند.‎
🔹
علی الیاسی در گفت‌وگو با برنامه سیمای خانواده شبکه یک، با اشاره به روندهای پیش‌روی صنعت بیمه، توضیح داد که با توسعه فناوری، بخش بیشتری از فعالیت‌های اجرایی و اداری می‌تواند به ابزارهای دیجیتال سپرده شود. در این صورت فعالان صنعت بیمه فرصت بیشتری برای تمرکز بر بخش‌هایی مانند مشاوره، ارتباط با مشتری و خلق ارزش خواهند داشت.
🔹
در این ویدئو، علی الیاسی از چشم‌انداز ازکی‌سلر برای آینده صنعت بیمه و نقش فناوری در توسعه شبکه فروش می‌گوید.
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/698461" target="_blank">📅 19:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698458">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVHV1gatxGYJz69rLvnc_JFxKKa43eqLgvPGpAONpornEqOFC6R8ApQH88FnbyeyU_s0gtcua5uUdf9FihsIMTvlsfATRc0MjdJog2Awec-i4VduQuRkSZ9soGNW-HOc4EA3JEhn9m8iy1UcixsgZ8sMbtOKfNnDZhacWLDuLae_qjrf_wthdqldyWsynGtkNcyrOV2ph8wyZyAcGyyLzAVVvLdzTZG7jdToZoo2SfO-01QQIkwwu2vjugQTyQxv1waXsKyv3fcax-5G6WUXphyl9x10ZlLE37t27XZclP2mRZBLXCmFEjMefuU9GszoYbwDPZ1z47WF8dQZEMUDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFxtf-uZMsY-jLO_K0uy6UWU1k3MWXoeu-5szI5CLAQwNc5uGALktcTpra1bUwuETHyVkN09TN9uohkQONhr_HynJ-1la9saNDDlLHa70joQIJcfRQWzD7egBqfd8aD59DkBkanYPLCiU-r-uDSkQ-8jBL0xcCMOLNK6YGUwCqUhLdo7jLXp6ovtk-tZ2diHnlJfY0koqxLcgEPfNCO_JnbkFwXLhybGUAgwo8hp6_dePLW1Hc7SvWQCbxuqPmy5VZ652QJSdR7NLyoc2qmNKjZrOkPNqwtxEoEe6Fwb8RnIgV_bf4huyHb7OkS_sTK5IsBvVMmM4af8ch074DPdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVp8JxKyJkPhpwc6qBOBGIeoadD-w0ROO_kcgOJ8OUFy-JlVNWpycBIwpyk0J-1Fs46Knj-EyaggUVaSnIO3RitMvHApAHMr12aJCRDd-eAp6o9l3xunkzI3lO8EchUiKjcgRFTlewYziUTGX_3_l0FZEpR8OzDhX-Ntehu2YfLTCUIL-SwOJAPEy6Z1QiWfO2RWSVXwOYV1gCre2USjXNqfSkcbz3aOkeTMtYf6MDK-SjwIdvY90mJ_KgIOiRKY9GVp1YDKUkvL-N3dVk-NQlM3HMXk5ODy5Qkm76H80_SbBXL93aU2Ewwez5cDDGac0JnngMiNCOuLrwpr7sDz_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روستای تیونویک؛ حدود ۷۰ نفر در آن زندگی می‌کنند و آنقدر دور افتاده است که به آن، انتهای زمین می‌گویند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/698458" target="_blank">📅 19:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698457">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOb4MlbTxG-gFCeXJb7CQDOA5LpVZ5u1uIpK9FvxRvghlki4JhuP4yYIxDDRyEncXFqPKZN4cLpVg8DQlh73Hrtu2a3zZduqua6GIiX2CYOUr5bQKRsQL7T3fxn8UlR-c9M3_Ai3lGcJSoq7lWQj8_jYqmLrh7wnMoQ0TL1tt1r9s__aYa30L-McsEDfF-nsh-tNoEpVaPeaXYKeZiaO2KlTgh_AE-48gQej-BPvi1Aui_HHEZIqxOnR_HGc1KoP2U0plhRRYViWSCO2B5xNlMoCUR5DtbGJedb7qTPT1624tYD4AKF9igLW9vAWfNSbe84_xme_-AVszA8_jc6WuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انگلیس و آرژانتین در آستانه جنگ/ قدرت نظامی بریتانیا بیشتر است یا آرژانتین؟/ آیا لندن با این سلاح کوچک غافلگیر می‌شود؟
🔹
بریتانیا در جزایر فالکلند حدود ۵۰۰ تا ۲۰۰۰ نیروی نظامی، یک اسکادران جنگنده تایفون، سیستم دفاع هوایی اسکای سابر و یک ناوچه نیروی دریایی مستقر کرده است. این نیروها برای مقابله با هرگونه تحرک محدود آرژانتین کافی به نظر می‌رسند.
مقایسه تانک‌ها، جنگنده‌ها و ناوهای لندن و بوینس‌ آیرس را در گزارش خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3252451</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/698457" target="_blank">📅 19:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698452">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVTcwz4xYX538QBINoYSArOjOHglN_oYRsn-Gtcgp5L-eikJGk8rxFFXsvDgP2rSU74oNm1qMT3OAckvw6MANIJWbIat3mPscWcQBq1PiG3b76MwQheW6oyWGXQ3x0MRjVISgvfwEWGsqUpi7nTmYUCD4XHDXt8WMJvuPCHd4soIBSK1Ac6_2UfhZr0J1TY_TXq19igvUT_GuuoFpHI-V2aVoH5sx-HFQRrMUjUP0ueaZHdrNvdzfwl0KTPIU1WqyGYWufFKQO4Na5K0Z5o2ETT2EBJcPV-_FOdZfnaSxg8CKAigZRrpfIYVM9D934HcXFTxB7LLA_VjxEx3K5U5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ygl0jvwQqwgYZxY1lq4SxM3KMpexzUwgYUpEfSZ9F7Jo7R1wWy1fvC7Z5wly1ooem6NN8_CJ1kYLfycYzsQWmYw--ZQcMDrW3or8Sgbp1bgmZGwl8MH_5kcOYGF6NLcR7paDxA0ZzXJ-Owiq7fg5YSP-TSex_3orvTi1EsFvjh6QDItyGn3FyK8EjGdDCDxe1XwtFm7Z8jNdVa9RGMGosDE6YasPmqkNVpbilinAIyphEfIN5T3UnWstYpAjmSqDSNCM20dzNk9OXwujTs0hcr_fNw0HeiEAbKQKHyCdEcf-iNoy_b4VAULppRfiyMOaj1OST7LgJyv5sd0TBDNjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knw9x6YXEtmyNIkgNJB7Zimre1e7haluk5xdGy3XDVfPXTpzpi3F13c8SBsyCXe7xKnHd7r-rHoVpXrL1hffYx6Ow5DP3-7BZ6EHLd7YyNSbtO9T6rB68KViltDBhuPX_eH3t9R779YX5lB3vO3L7PYp7QvpgDqhb0oXVEpngIDx-4jLrFswDtQYezGoievo1nG1a1bGYwC0NWcFpZlAp3Y9oReIJUhMadQYVkEvrzIqfZ9anvy24A9IYWGO2ltwuJ3uleDBKyyJySPtp3Y4ugWn-qIuNV_oo0vG7O6uIW1n_IQLCP2ZkP6jJrPjY4jN0OIpjIzIcrlith__aLR5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LH1vfoFPLdpA210LbKSnadMu6NDKI-ASukCBvvim5ORsQBqP3oPwkR5UrbSxNgUN7ai7BWQApkQCpoUjqfJ0Ggr1UjbonaGbaCacRqjJj5Ds1G5MZ-dlvD60ergBi86INwWVNB_diO8dDmJquldOC57LICVUKIgTiuKNjH8FrNCYMr6BZvDoUbG8MxPP4jXtSBrpyz6HUkltXRbkBo2hxhH_FkMqtGlKIx0OWAd2AtUaMziBU9WL9K3MiP2ru_iIx_x3QCCkaVs7kSvm5rdMvJwLkr0n_gBqZ2JuaGzV8rtG7J3Qowb8nytgx6fZ5zyGet2PLYXi0ehkId-AeS67pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا سبدهای سرمایه‌گذاری باید نقد شونده باشند؟
🔹
انتخاب سبد سرمایه‌گذاری فقط به میزان بازدهی بستگی ندارد، نقدشوندگی دارایی‌ها هم یکی از معیارهای مهم تصمیم‌گیری است.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/698452" target="_blank">📅 19:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698451">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
المیادین: ارتش یمن ارتفاعات مشرف بر شهر «تعز» را آزاد کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/698451" target="_blank">📅 19:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698450">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba056aa6e.mp4?token=JOHEYnDJS7coZDWwk8p6lajJEi4HiPOhpeAkVLc-9D7qXj2Cq4K1gjmxA7L3FkeaIYuGvCHUE_J78IiUDTTiPaP8jD3KTzKwmQlKN4k2DbX9qqZxzBGxkHqEDJqxS8vvllZIxnIrUli-g0GD3j0OAM3wGOmTSwB5YJpIS5U6C7TP_gTq3_ZTa0GJ9DDgrIbidUlWD_TafE_aN893lnmuM4hVW7mV1-FVnphegqnzGQ-uwcmgJ84quwzplNzhNh_xJZED6Oor1TSxL5k9ztPQgUefxUM_6Y8dhnWLG1rfAluAn8gpot9Z3C4LukmsFCb6zgcJerBVzsAlAQtHk5XxwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba056aa6e.mp4?token=JOHEYnDJS7coZDWwk8p6lajJEi4HiPOhpeAkVLc-9D7qXj2Cq4K1gjmxA7L3FkeaIYuGvCHUE_J78IiUDTTiPaP8jD3KTzKwmQlKN4k2DbX9qqZxzBGxkHqEDJqxS8vvllZIxnIrUli-g0GD3j0OAM3wGOmTSwB5YJpIS5U6C7TP_gTq3_ZTa0GJ9DDgrIbidUlWD_TafE_aN893lnmuM4hVW7mV1-FVnphegqnzGQ-uwcmgJ84quwzplNzhNh_xJZED6Oor1TSxL5k9ztPQgUefxUM_6Y8dhnWLG1rfAluAn8gpot9Z3C4LukmsFCb6zgcJerBVzsAlAQtHk5XxwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبدیل یک ستون ساده به المانی چشم‌نواز با کمی خلاقیت
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/698450" target="_blank">📅 18:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698449">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">همیشه یادتون باشه، ما صاحب داریم</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/698449" target="_blank">📅 18:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698448">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
نام برج میلاد تهران تغییر کرد
🔹
بر اساس حکم صادرشده از سوی علیرضا زاکانی، برج میلاد تهران به شرکت گردشگری و تفریحی میلاد تهران تغییر نام داد.
🔹
در حکم شهردار تهران، ساماندهی و توسعه گردشگری شهری، معرفی ظرفیت‌های تاریخی، فرهنگی، گردشگری و تفریحی پایتخت و احیا و بهره‌برداری بهینه از میراث فرهنگی و تاریخی، از مأموریت‌های این شرکت عنوان شده است.
🔹
همچنین عباس حیدری که پیش از این مدیرعامل برج میلاد تهران بود، بر اساس این حکم به‌عنوان مدیرعامل شرکت گردشگری و تفریحی میلاد تهران منصوب شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/698448" target="_blank">📅 18:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698447">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سازمان دریانوردی سنگاپور: دو کشتی‌ کانتینری طی دو روز گذشته هنگام عبور از تنگه هرمز، مورد اصابت پرتابه‌های ناشناس قرار گرفتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/698447" target="_blank">📅 18:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698446">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QP8LFkytJwEpaljUI2osCFzgR7MTf47ccJXwxsFuVz0w-MfSXTovJd7_NxvjaJQ7bmNl2ITP4-7b9syGtpD1ejbu492_XFwciDi_ssRGc8FZZylyp-zKWu6zmL8aUqzu8cA5JvW3Za1H86WiORGgdUVH018ON8kKRLqFSXx1NA5hbq8ZNDPKt-OkmRb5qQGaiVr8z5cZ5IS07-cYOiYCWEDFrbkupaRqnxUq0w-l2l6XczzcXfhpONOXEdyblIzpJ1Z6jahUrGATHJ_kql42Y84stwUQCFj1e4JuPWAVThrG5dvMyE5zyKYSomBa8aJGlv1srbB2gczlgc6jBJ9nog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور وزیر پیشنهادی دفاع در منزل شهید نصیرزاده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/698446" target="_blank">📅 18:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698445">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Y-oODL4pLc3TaN2FULH_76aCi0UsokC0flKy3jvJ7PQ1BdE1a6dA9WyF6o6Le8AWMAbCDIbBJDyivOqaUVeyxuNM108SD1_NP145BwGK83KOJjlR4BxDj0bcO4XK1FfG8Q-XwPsT4g6YLC6_Ucd6m6-yVHJOE_3AnCSw-5ZcOdLlj9Ue_KRBCqbQT0YL0TdXlbqzrY585hOj9RyiJZfi-ufX3BR1013aY6ljdOGIYRlDLwg3x3NZlhmxVsBokL0090_aDSmSgGEO5oGChv_cfxUma1ts-k3tB8RI6zynFxu7QJDzC_03PUK4f0g-UkyUGCw3jqUfNhSc2Zf5IIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تورم آمریکا در سپتامبر به بالاترین حد خود در سال رسید: ۳.۷ درصد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/698445" target="_blank">📅 18:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698444">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظرتان بزرگ‌ترین مانع تردد مستقل نابینایان در شهر چیست؟</h4>
<ul>
<li>✓ پیاده‌روهای نامناسب</li>
<li>✓ حمل‌ونقل عمومی</li>
<li>✓ موانع و وسایل موجود در مسیر</li>
<li>✓ بی‌توجهی شهروندان</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/698444" target="_blank">📅 18:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698443">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
عراقچی: توقف حملات رژیم صهیونیستی و پایان اشغال لبنان اولویت اصلی ماست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/698443" target="_blank">📅 18:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698436">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSNYiHdBuv8IbvBkSFGtw465EgsFPDygkbhN0cRIMe4f-bO0mivH3hL9CAYxqKba4V4S0Pv0s3l0VtbjPgNnIfJo90yEGpwNiOadn_prBRyJ1R2m8Eqf6Gr9N2_7PD2xk3PSKq-aumtkUfhZAopD58Ufa3JOKa4TS8x-7OE0yzFrvPkxmh1N3ZDGhiC-BZe3dBdqO5A5JhuZh-gvxAdrExnqqDL2orY_8eOxx7SyNPl_74bEYBm9Iq14DzUYYRLA4ZZrNpVXnleh1fjPovRX_5sKo16341HlC3wf6ohMR-gwxlViZBAEe12HtSgePdJaR3qqs9N-xLj5tun-x8NDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSm4uRmv_KG9orh-zW9kCnCMDfUXQHRkn5nZGdVBNPp3nDQAJ9giXtKq4H-n73T8HYvIhSlhdrQGQggMLvdC68LiZF-8XjaGNls7m0l-i1hPHuuY5pZJQByfFB83VdicYRj_myqMke6XbVcDTVgRhJVczFqXLsdw1r-pV9U9nnXKVihMoLANmzQN0T94cNoLdOfLy2wzDqyLj9gQBSyJw17h-dCzR8tb_7bSDqRiS1lqwPSnnRH9qp8p6jbN__058Tyeic2yQFc10xXzdsZqe6vlft-iB1t-OH1GfNLwRwNyCFlneCRCO5oTaG_iVlG8qm1n3gtQgrJTJNGJKBNVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhZchwybymKQQLCRvumqzJ64hNVBPL9YVuo2vZL-fOC0_BW7kh98VID_-hs9kqD4ElbEyxDXUBmtiMtTAf6zh_Da-rCE1ADxoRmWRFzBLGue9fA6BeIeWv-j3XQndWfZmfH963CDHFloKtjv1v5z4oQVpE4rNuHt5Gj8L47IoaDbNmFTnzvfWS5e4cncTDIBW2OHR0Dr54OWG7xTjyt5VjklzM-RYvFRyC3KVtm-MKbpMFzbN_01EHk4--XxC0xstf2K1nN99De6ffQK6pXIgNVZAsyg8hB_AZKu5PyyPnEZE5BAbGxoc-rGV3jJrQWNx5JQ7mYP6MjptKYWwFTcyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h-RoG2xHMLnbvm-t04J5MWTyiDDI90xHuNdxujM_DI7ohbsI6yRgQCCEQsHB_41pwqLGBcOUE3vOb7MTPk3Wmj50gDs5Cm-PfuGfP4jMhu4Hz4nSLS7_m0_lGiO_sMq2IKr0mkOwTH6V8kCRiS2hMJ6cH2L2eBWc1XxIi8zMVldnw9pKqmiWXxFTcJHTvgPfhUCytGs-mHow89XUM-F91TLrATVpvn_GDEJH5GfgWbknBS0_TeytVuv1HaNaE4Bw_LRpuDFAVHoj5bjT3ldC6-Ngeo1lYsuAMZnSc7DUUE4c9HfjWvGomoeHwDxSWuhFlbAA44fjtae1rDygPQV6-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1oZ6PE-7ZrHFy0xsuXag6MILk1XitRvymVJXFRAgchR1J1CEbdyuaxYkhNNuS662MjoQUlx7FCOiPm4UwcAROSvOpLQwzkdD6ptleHnJb4YD3_iHRrQO3yNdnRUniB7iZ9EzbnX_JaG7D5WEZfV4NZ4bu0cnIuQKy8NUCl-qcVwpHV2TGZpapHGveM8w4XDIrlk31v5SRbFiHuoWXTP5vEdyaGvVtrcaKSXWg4fjATFLxrx9yDTy9R_cTMI8f4NXaxIx-S-X5CmE8nZlEEAzmqvGdXZVtFjurXZduOmidwXI9Y49FZciNahCZzqQw22XwmV1WdSuNdARL5uvBkSVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmU83yOf8Po8B92yrdYbK-HWxA0sI3HjGTc895rwR9YTmnYWujOWUTxpqeRTrbVOQiw53p6-evJatv_6n3r6Z1M5yo20ji0fcQivFD9_aa9lAHtJUZR-ZkuIPIkKiOauZY6QpprfwFk5RcdmhzV0BuyHRqOnaNAVOlJIguJ8AT7ppSanHlxLqIfyOF7p6OG64zW5vW96zsxxd1nIlak46DRjwjovb6RQ0UhLfDFdEZVqYrSU4Q64SXQXWEgMLpawZhI1D5vptNGP8qd24JWUzuHzXSe6Uc8GxLwt8-x58Mo0hyBFOmSM3W63Xw_mHrtHK-dwBkooxQ1e2-YvTQRsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVKMONllGdT3Dz_xsxZQ0aTorrBNAK6NLpMrMUKjWtLrzL-WSU9XUIZhtRipHPIRAue3TT0izHgDBll-I2DBGcLG1AF0Ktv2vQBtXDtxqfz5Y6NHv1jav0kel3vXfzNwUbMj5eOxLV2mESwBEjh02ciINJN1aNJiwrxeGwJAm1SdIBIazAgqAVzAn6TmVzoMDhvrLaZkriEWCCkEBW3FG8jbN46XMNZCWyuDN_QkJMMpfEguQ8B00nA105OP7AG0tZcM1Xl0jDyoO_Q51sWEWZ2fvh3HsTEsdBoTMvbHoAGPZEDkFwCkJ5GmX_CO31AmTe1cVLWWWRFTjgCLHv7AqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرهنگ لغت آشپزی؛ معنی ۷ اصطلاح پرکاربرد که شاید ندانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/698436" target="_blank">📅 18:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698435">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
بازدید شهردار منطقه ۲۱؛ محسن امیدیان از شهر خودرو تهران
🔹
مرکز ثقل صنعت خودروی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/698435" target="_blank">📅 18:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-698434">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFAKOOR | فکور صنعت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e637c05d77.mp4?token=T-9rjmRQu5Lx7mroAUCszl3Ot0N9dvr9bWWpBuy5MzwsBjikct5VI8zD89oFPAaun_mEK0Zk0H9eAcwIxy5vNlwEJ3ush0Fj6DVP6xjipk3y4s5wgSbHpN_qhSbm6gad4peG1CMHx9NdS_4qijay4p5LMnxz8X0YtzGEgLHFOJil6CjQJEsfKGw3_VzqdlaflGtYp08FTO31h7DywNXykOGyIN9wurjwBXoaQvXln4NosLHw-nsQ7sXiByqh6akXNIymKchYi6PfhVyUu2l_LDi4mNxgSc_IdP4ojduCHuUKVn_nCY0_UzuBOaMhDMzzJfcGCNJDiDmUQt7X4aTSFhvZI67lqTlH-VjYoLxGuerJ4xOxXg8A_WGhvd8knJcKz5V8rCcIcbWc8bPOCGzsGgZWoTQUtu7G9_BWZf8yewdN9q3H6Fr4I7zJ6D9Zuojzwtjbvsrhhkq0IcdcEe1qH0AQGmQEbEcc7ojZqdog5Ct4Ba7qaV6_vLjsUAt7tXYgswl88n0zSUq9iOt4pDMazOPUOiP0iBHrVhhI88rJ96l3eH1DLkU1VSNIRuYIUQw-zpxT3n223RIcNeEavo6HRhfn-4yEt7WVcubb7SUOpqYmCXlK9pYAnvrlk32tneQEuEQZSedETlBjOWUjRSEeDpTUhy38eadGSt0__uiGKkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e637c05d77.mp4?token=T-9rjmRQu5Lx7mroAUCszl3Ot0N9dvr9bWWpBuy5MzwsBjikct5VI8zD89oFPAaun_mEK0Zk0H9eAcwIxy5vNlwEJ3ush0Fj6DVP6xjipk3y4s5wgSbHpN_qhSbm6gad4peG1CMHx9NdS_4qijay4p5LMnxz8X0YtzGEgLHFOJil6CjQJEsfKGw3_VzqdlaflGtYp08FTO31h7DywNXykOGyIN9wurjwBXoaQvXln4NosLHw-nsQ7sXiByqh6akXNIymKchYi6PfhVyUu2l_LDi4mNxgSc_IdP4ojduCHuUKVn_nCY0_UzuBOaMhDMzzJfcGCNJDiDmUQt7X4aTSFhvZI67lqTlH-VjYoLxGuerJ4xOxXg8A_WGhvd8knJcKz5V8rCcIcbWc8bPOCGzsGgZWoTQUtu7G9_BWZf8yewdN9q3H6Fr4I7zJ6D9Zuojzwtjbvsrhhkq0IcdcEe1qH0AQGmQEbEcc7ojZqdog5Ct4Ba7qaV6_vLjsUAt7tXYgswl88n0zSUq9iOt4pDMazOPUOiP0iBHrVhhI88rJ96l3eH1DLkU1VSNIRuYIUQw-zpxT3n223RIcNeEavo6HRhfn-4yEt7WVcubb7SUOpqYmCXlK9pYAnvrlk32tneQEuEQZSedETlBjOWUjRSEeDpTUhy38eadGSt0__uiGKkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت فعالان بازار سرمایه از عرضه فکور| حسین عبده تبریزی
حسین عبده تبریزی، عضو سابق شورای عالی بورس، ورود فکور صنعت به بازار سرمایه را اتفاقی مثبت ارزیابی کرد و ابراز امیدواری کرد این تجربه، مسیر حضور گسترده‌تر شرکت‌های پیمانکاری در بازار سرمایه را هموار کند.
🌐
www.fstco.com
⚙️
@fakoorsanatgroup</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/698434" target="_blank">📅 18:09 · 22 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
