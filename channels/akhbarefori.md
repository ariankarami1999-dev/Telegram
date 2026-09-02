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
<img src="https://cdn4.telesco.pe/file/Mw51jRYg7_Ij66wchzLCKonqFMuLWzUkOdp-j4ijMrD036jxt2pzysbAu654XKR9DMQ18o815_P5LxpMeXcKv7ztWNoEItPF22WWUKQpD2Ob76yAIg0Xlkalwhqu7s-DstTr8BKhsc0OK3bJ76vzTL8HoXhCDlSpHMBB9Q2q3fg7y8Ey02OLY2jj4FTzDy8lL3pYreompPHv7zfmTgZSe5ExdAC7YgwHsxQnB2l9aXDKctbVBfCThOE7IRUT6OhDdS6URNysPwkuaPTatNxazQr1ulD1BkzZ_CTFiBTnpg9R2r2RDTGnh-tpeWTkNCu2zFht3PzYXs7nhe0E8hAx9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 23:03:40</div>
<hr>

<div class="tg-post" id="msg-686743">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_taL9XLkqffKA5WAgA0Zrvd1fYQxt3agUKriihY-RiRaqYyDszPMXy9ZeXsXuDPnk2AkkRr_nNpu0vI1NdZ-06ZEPyfv0ZA8g6n9F1OkHxcV0352ZIGUKNsMsQYcSUDiMK1sm7AH-ynJmnLXtcwNXyaoTeFRlrbnacc4ffGlDQbSP8N_7dwPpka7_Q_VIITiD23hhMhxWbNR9NXFHitBQfj4vtCyh067PRKrsssu63hYGGkdueH9EU9b7XjHzdk89Uf-y-rmIM6eTVdYKOdI7vAiGIJczN1Yyn9YoaBpp_nnvZu6ZRbcgkewxk1DxgOi3fB8LYUmFVn-BmWRiFz6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف پروازها از فرودگاه نجف به ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/686743" target="_blank">📅 23:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686742">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/686742" target="_blank">📅 23:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b182ff65f.mp4?token=I2Mg-CzRWJ6rcen84PqmZm6TgvuXDce5Xu1HB61UQYOHWqvB3ySmivNXlAB2JDSITSYCaWwlMycb_rHB4SnbR2u35JwPl56FzMmNCYFACzgrIlXBYsP6Aky9X8-RCNA6A4zCvA-LXB6Y2CjyUkFkHo2Ams4Aisg7fdmUKhwRal7wSHTJn_ivTRL8jZhN8lsDUHJlWsh8ig6gi2yaBDcJ80gycDpc8BHMUymYhCyesb_ijcWa4ZnScftAQasXaDx7DnKZtFyRIMTDe-lb0QX7DSBBqNkRXlNIJpicq9_J5ODPucFpjyUrY2jHpKhyi5uFFeM2kpk6wq38V-3bbZQ5UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b182ff65f.mp4?token=I2Mg-CzRWJ6rcen84PqmZm6TgvuXDce5Xu1HB61UQYOHWqvB3ySmivNXlAB2JDSITSYCaWwlMycb_rHB4SnbR2u35JwPl56FzMmNCYFACzgrIlXBYsP6Aky9X8-RCNA6A4zCvA-LXB6Y2CjyUkFkHo2Ams4Aisg7fdmUKhwRal7wSHTJn_ivTRL8jZhN8lsDUHJlWsh8ig6gi2yaBDcJ80gycDpc8BHMUymYhCyesb_ijcWa4ZnScftAQasXaDx7DnKZtFyRIMTDe-lb0QX7DSBBqNkRXlNIJpicq9_J5ODPucFpjyUrY2jHpKhyi5uFFeM2kpk6wq38V-3bbZQ5UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: اگر شما می‌خواهید در ایران قیام کنند، آیا سازمان سیا را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟  ترامپ شیطان زرد:
🔹
من نمی‌خواهم این را بگویم. گفتن این حرف مناسب نیست. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/686740" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686739">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eb8ba8b4c.mp4?token=gM4tltGiUs9VjSsh9jK8b6bz7JMgrcQqpSnHg8rma8AqMFOJFjaFbVdihz6gV0UJ0t9whHRTLhEQjNyg2d9l0vY-vIb-ACebv5q48S02v0J_KTShWy_H8tlt6dbGWoKlH9wLvf1etKgFF8jtbaGHNzvSGb6igHhTWEPBJgiuXAMVJKB5ob_URtcONLAyFrHAk0DfWJPYTE-Nk5aguv85Ol2Ht59WRKNKlEDm4P2ON3paBTPw0VN_R0e7L1JpGZMWXrh44qd6CcWDmxJBxpJ2FGmEXJU2GJ74KBWV-uBkfvhPmxqn4EVHW9wPqipPr7iV25OVhxRfCLL4qK8FDIKLmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eb8ba8b4c.mp4?token=gM4tltGiUs9VjSsh9jK8b6bz7JMgrcQqpSnHg8rma8AqMFOJFjaFbVdihz6gV0UJ0t9whHRTLhEQjNyg2d9l0vY-vIb-ACebv5q48S02v0J_KTShWy_H8tlt6dbGWoKlH9wLvf1etKgFF8jtbaGHNzvSGb6igHhTWEPBJgiuXAMVJKB5ob_URtcONLAyFrHAk0DfWJPYTE-Nk5aguv85Ol2Ht59WRKNKlEDm4P2ON3paBTPw0VN_R0e7L1JpGZMWXrh44qd6CcWDmxJBxpJ2FGmEXJU2GJ74KBWV-uBkfvhPmxqn4EVHW9wPqipPr7iV25OVhxRfCLL4qK8FDIKLmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: اگر شما می‌خواهید در ایران قیام کنند، آیا سازمان سیا را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
ترامپ شیطان زرد:
🔹
من نمی‌خواهم این را بگویم. گفتن این حرف مناسب نیست.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/686739" target="_blank">📅 22:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686738">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
مای‌دات، حامی مالکیت محتوا با استفاده از بلاک‌چین
🔹
در مراسم رونمایی از شبکه اجتماعی مای‌دات، بابک زنجانی با اشاره به اهمیت توجه به مالکیت تولیدکنندگان محتوا گفت: در حال حاضر اتفاقی که در رسانه رخ می‌دهد این است که محتوای تولیدشده توسط یک خبرنگار یا رسانه ممکن است توسط رسانه‌های دیگر بازنشر شود، بدون اینکه مالکیت و ارزش اقتصادی محتوای اولیه برای تولیدکننده آن حفظ شود.
🔹
او با اشاره به تجربه انتشار خبر دستگیری صدام حسین یادآوری کرد: زمانی که صدام حسین در عراق پیدا شد، نخستین خبر در یک خبرگزاری ایرانی منتشر شد؛ اما رسانه‌های دیگر آن خبر را دریافت و منتشر کردند و ارزش اقتصادی خبر برای ایران محقق نشد.
🔹
زنجانی ادامه داد: ما معتقدیم باید رسانه‌ای ایجاد شود که مالکیت ارزش محتوای تولیدشده در آن مشخص باشد. بر همین اساس، زیرساختی مبتنی بر بلاک‌چین طراحی شده تا مالکیت پست‌های منتشرشده به نام تولیدکننده آن ثبت شود.
🔹
مشروح این خبر را در سایت خبرفوری بخوانید:
https://www.khabarfoori.com/fa/tiny/news-3242267
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/686738" target="_blank">📅 22:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهای بانک | Hibank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd0f51f783.mp4?token=TbebQAmye8kPi1b1CUog0gXBTU4VxNudPmSH33vjXNAA9P_t6HFx8RDBbuSfARE0PvwFToi1doMWqOGelcYvwBeHCElR_u_dYwHEn-W_8u33Yhuo9-Wz_H-mwrNfV6TzIz0ISj3OBgGr7W-DXDYvL2rFizzezU8BzDhoWEpCMOkFZW0ypBy8xRa1j9lTAraDl-Zlk0bUPB3nVdzWyAk_STkXwhFQC54_5LsZxpqgs6wgpvp-8-U0hkaG86e7XU1DOaqKyTFBEAsBQbH3D8hos3oI5zlQpZA7g7xuaB-BIZ-BkcgHHCJXaLwxcrka4YorrOTsuygmhnS9TG25QX2A2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd0f51f783.mp4?token=TbebQAmye8kPi1b1CUog0gXBTU4VxNudPmSH33vjXNAA9P_t6HFx8RDBbuSfARE0PvwFToi1doMWqOGelcYvwBeHCElR_u_dYwHEn-W_8u33Yhuo9-Wz_H-mwrNfV6TzIz0ISj3OBgGr7W-DXDYvL2rFizzezU8BzDhoWEpCMOkFZW0ypBy8xRa1j9lTAraDl-Zlk0bUPB3nVdzWyAk_STkXwhFQC54_5LsZxpqgs6wgpvp-8-U0hkaG86e7XU1DOaqKyTFBEAsBQbH3D8hos3oI5zlQpZA7g7xuaB-BIZ-BkcgHHCJXaLwxcrka4YorrOTsuygmhnS9TG25QX2A2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
می‌دونستی با خدمت جدید Hibank می‌تونی زودتر از موعد حقوق بگیری؟
⭕️
کارمندانی که حقوقشون به حساب
بانک کارآفرین
واریز میشه، میتونن در طول ماه بخشی از حقوقشون رو از Hibank به صورت
مساعده
دریافت کنن.
@Hibank_ir</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/686737" target="_blank">📅 22:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCPmIXMWdcddwmw7eE1wiAJqLIw6Jngm04KXgmDz84J8IMm5V_8z7xAyypSFJUdu5Lopcel4pxaRm35uNN7ia3EfyXUj9MyMfSm6FizS2LIiShv1SipVbXXOwYojxdDpgjLGhpK8SMDN4mMkIl7KdPWEsmUNBk4O-jFuQ6gcyAzmJdRdM74UUwpAtnRmCn-XikfpQbJBitW3WjBv4XIFFy79FeEdsv_B_Z-kRuUE0kHwl9Y-X-a_2SgMWLalpWk62gR_dQm_ctAAr1YMtlTqV6CXjdQGgu-p-CPXaugzh-sjx31344HArtzW_kyz9bdHVJSHQ8TlzjzUaHjQC-cAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر پس از پایان روز دوم از هفته پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/686736" target="_blank">📅 22:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686735">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf977dab9e.mp4?token=HRF6AWQlYvhM53JATIrLSnPEUPLnfVg2h5q-_8EEg8n6G-yF1tNavwMRQ92vdeM81gbSurRPfvJcYBx76UdJVy1dXDwJDoOUqZLnh_P0KBUnBCjP863B0dwus5NaUsjyVQATo4NYyyauzLEPY-4rHSpy0Sab--G4JiZb7V07_P7BVhk0az_BHSx83CjaRZxYxpLGDjFj5CTzHF_X9LdRS4i_UpuJz-A6VfqsI-tfuv2h5SMWMxZ-0OUHBMWXNN0bKwL1OqrvpO5wAyUEXbsMSi-dI2cF_0_TGTr3hBOfIiFKK6IvKORqcCqWUB-J8ijmqoeNnDqSD9LKEuF5vA6Y-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf977dab9e.mp4?token=HRF6AWQlYvhM53JATIrLSnPEUPLnfVg2h5q-_8EEg8n6G-yF1tNavwMRQ92vdeM81gbSurRPfvJcYBx76UdJVy1dXDwJDoOUqZLnh_P0KBUnBCjP863B0dwus5NaUsjyVQATo4NYyyauzLEPY-4rHSpy0Sab--G4JiZb7V07_P7BVhk0az_BHSx83CjaRZxYxpLGDjFj5CTzHF_X9LdRS4i_UpuJz-A6VfqsI-tfuv2h5SMWMxZ-0OUHBMWXNN0bKwL1OqrvpO5wAyUEXbsMSi-dI2cF_0_TGTr3hBOfIiFKK6IvKORqcCqWUB-J8ijmqoeNnDqSD9LKEuF5vA6Y-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همزن برقی؛ از درون چه شکلیه؟
#موشکافی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/686735" target="_blank">📅 22:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686734">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ee037820.mp4?token=qojuv0kKGun9zavsBUwJeX3UgCvrgoBIZj2GXHDCgnD48LCKsCqiJbfxbl8Qif2hSMcbMw5RDHthFndkGBkyd4x3mLBorHttj2-n_lUgJ6B_iB0bz6gzNYKeez52rWOJyXjA362whmcqKKsDiOA7h0POCZuxvsWS585IYUZZHoMdgeA5V-nUQRsoFXegCIBvBN-ZO-heqWBDqvIj9joGRhysntNbCEUtDTeM_HuA-K8-Q5gSST17s7HYTwz7iPaLx87wQWWeuUROLABO1tWq_ew6RZVJq7GljugMdCExE0q4-Pt1p86ZsJlUO6CSKc3iknmBqHzizP3VzBdmUW0zLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ee037820.mp4?token=qojuv0kKGun9zavsBUwJeX3UgCvrgoBIZj2GXHDCgnD48LCKsCqiJbfxbl8Qif2hSMcbMw5RDHthFndkGBkyd4x3mLBorHttj2-n_lUgJ6B_iB0bz6gzNYKeez52rWOJyXjA362whmcqKKsDiOA7h0POCZuxvsWS585IYUZZHoMdgeA5V-nUQRsoFXegCIBvBN-ZO-heqWBDqvIj9joGRhysntNbCEUtDTeM_HuA-K8-Q5gSST17s7HYTwz7iPaLx87wQWWeuUROLABO1tWq_ew6RZVJq7GljugMdCExE0q4-Pt1p86ZsJlUO6CSKc3iknmBqHzizP3VzBdmUW0zLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت خبرنگار ارشد بی‌بی‌سی از حملات موشکی شب گذشته ایران در پاسخ به جنایت آمریکا؛ یکی از بزرگ‌ترین حملات منسجم ایران در یک شب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/686734" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686733">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNfMtcgZvqF_XUVaBvhvBHYB_40l1SLJ7CprDvrY9cGov-IjKmfl9iTBdB6MkPqR6gKfirN_pt6Hg9GYZon_EGGwIlGhdp0YRbZFnVWY_F6arlW7U2K6XyhtMXZ9IFCPYJXqHS2SxKTIJBb7_xWi3ZppDhWzrrOk0t_oqSeYGqaZQdgifLM_3JMsjmMCxIg8SKJk8R7kG4V9BJKGRMiBM6h-y5b1-kfQ-hW74B4CeYMazzuIqtMruRKFRR3qJNAgSAnn_TdWrEQR7cce-vW_6jPBy3wGyD19f-xPs376pb2iikNX1mWaTaxAA1yU88nH3XW01R8ZjYexTS9k1qy3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرخه‌ای تکراری از راهبردهای شکست‌خورده ترامپ در ایران
رضا نصری، حقوقدان بین‌الملل:
🔹
تغییر رژیم شکست خورد.
🔹
جنگ را امتحان کن.
🔹
جنگ شکست خورد.
🔹
تحریم‌ها را امتحان کن.
🔹
تحریم‌ها شکست خوردند.
🔹
حملات را امتحان کن.
🔹
حملات شکست خوردند.
🔹
دوباره تغییر رژیم را امتحان کن.
🔹
سیاست ترامپ در قبال ایران، چرخه‌ای تکراری از راهبردهای شکست‌خورده است که هر بار با عنوان یک راهبرد جدید ارائه می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/686733" target="_blank">📅 22:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686732">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4dbee3ba.mp4?token=CY1C2hAd8k_fNUX91gx6FNA1iTnjq6O20dxX5Lipm8IvmNqcUTG-bs85AqneTJzEClL17c83KjkqSNZ-KLc_Y04dsprh8ocR-k58w4MKCH4fYUr2APZ3QpC7pr4a-6zOYY15uFrKU1tCWJOvwwTjQYfdNZ60_x4JeUqVwphjai8SYB-5oxV2NPZesdVzRH9Fv9CnOBiErP0Ed0rySvVe3VZNk0oBXma_OY4BDxMb27b_mfvt_gXnkiSt5FoTKPxOurgByEp9QCXnpfSgpQs3aGuaVr_1io6JBBaO6_uoaiQpXq4RFf38-MCu5Um3_KiIKlfiLkhbWwAPlXM6oICkVYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4dbee3ba.mp4?token=CY1C2hAd8k_fNUX91gx6FNA1iTnjq6O20dxX5Lipm8IvmNqcUTG-bs85AqneTJzEClL17c83KjkqSNZ-KLc_Y04dsprh8ocR-k58w4MKCH4fYUr2APZ3QpC7pr4a-6zOYY15uFrKU1tCWJOvwwTjQYfdNZ60_x4JeUqVwphjai8SYB-5oxV2NPZesdVzRH9Fv9CnOBiErP0Ed0rySvVe3VZNk0oBXma_OY4BDxMb27b_mfvt_gXnkiSt5FoTKPxOurgByEp9QCXnpfSgpQs3aGuaVr_1io6JBBaO6_uoaiQpXq4RFf38-MCu5Um3_KiIKlfiLkhbWwAPlXM6oICkVYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ در ۳۸۰۰ متری اقیانوس
🔹
زیردریایی تایتان در مسیر بازدید از لاشه تایتانیک، در عمق حدود ۳۸۰۰ متری اقیانوس اطلس دچار فروپاشی آنی شد. فشار عظیم آب باعث شد بدنه در کسری از ثانیه درهم بشکند و جان ۵ سرنشین را بگیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/686732" target="_blank">📅 22:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686731">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
آثار یک موشک کروز هواپایه AGM-84H SLAM-ER متعلق به ایالات متحده که در حمله به مراسم عروسی در منطقه کوهستک استفاده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/686731" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686730">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه نرم‌افزاری دانش‌بنیان پارت مشهد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36728760a3.mp4?token=EqR4-2dQ-gStpSul8cywgq2DJDNkQM7ZaHHxmNyrIXPfS6AlrDMxhOoUdU87qLECo8zOU0YcVN2SjeOVkzaLagIzOCscp7TXgiVHlBuS5iUcAlP-33JemFkqIs3i5XDr1NRBw-SWKrfx8_y8JEATfnAaZzDJgUpkA9DB9a_WgwP3oDs3KD17czJ_rEFCvJm7Yw5TTSZTODIfrJNd_vJg6UttRJk9ULtT0SAJW1xiklvyjQ1zLW4uD7rAPLpyeQ3H5hOzXHNx1J_wX1kHUWUzlUpTzS5RScOIPmQQZpEiuFvQOtRKNS7zbJaJS3rFNKWQxaX1YkmXhokWuXxVO6iQZ5Rdv5WTW78SWiZvDRjFGD7Nm-iX6XP-sRmE58r9bp-NmyuXCEnRBgkeMjBbfav2sKPm4ejzZ-Inn7UcIWGPY00xObGvVwNoe07C_B1Lof5_nR6ifbzukuIMo7YMHm8qzTIcBcDtkldQ9p2pDrwQqvdxzdOZoFuuV04Hw0e_9DVniFfkQOw4J3gz3jYzi_bYSfsxXLEu8JIrDEBwHjdMRLA1nlJVm1uaV437T_L-2vry2AjqN7dF63R-22RQqOuIFDSRAeuA1yndtvRXUwQVZeedJD30ynNntKNr-FVSCl_FOEVGS_QXPAQAs1shoUWM73bpd1EQVutKryAgIMZOqts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36728760a3.mp4?token=EqR4-2dQ-gStpSul8cywgq2DJDNkQM7ZaHHxmNyrIXPfS6AlrDMxhOoUdU87qLECo8zOU0YcVN2SjeOVkzaLagIzOCscp7TXgiVHlBuS5iUcAlP-33JemFkqIs3i5XDr1NRBw-SWKrfx8_y8JEATfnAaZzDJgUpkA9DB9a_WgwP3oDs3KD17czJ_rEFCvJm7Yw5TTSZTODIfrJNd_vJg6UttRJk9ULtT0SAJW1xiklvyjQ1zLW4uD7rAPLpyeQ3H5hOzXHNx1J_wX1kHUWUzlUpTzS5RScOIPmQQZpEiuFvQOtRKNS7zbJaJS3rFNKWQxaX1YkmXhokWuXxVO6iQZ5Rdv5WTW78SWiZvDRjFGD7Nm-iX6XP-sRmE58r9bp-NmyuXCEnRBgkeMjBbfav2sKPm4ejzZ-Inn7UcIWGPY00xObGvVwNoe07C_B1Lof5_nR6ifbzukuIMo7YMHm8qzTIcBcDtkldQ9p2pDrwQqvdxzdOZoFuuV04Hw0e_9DVniFfkQOw4J3gz3jYzi_bYSfsxXLEu8JIrDEBwHjdMRLA1nlJVm1uaV437T_L-2vry2AjqN7dF63R-22RQqOuIFDSRAeuA1yndtvRXUwQVZeedJD30ynNntKNr-FVSCl_FOEVGS_QXPAQAs1shoUWM73bpd1EQVutKryAgIMZOqts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎒
ثبت‌نام ششمین دوره آموزش تخصصی Back-End کالج پارت شروع شد
🔶
دنیای توسعه داره تغییر می‌کنه؛ ابزارها عوض می‌شن، هوش مصنوعی بیشتر کد می‌نویسه و نقش توسعه‌دهنده بیشتر به «هدایت کردن» نزدیک می‌شه. اما برای هدایت کردن، باید ابتدا خوب بفهمی.
🔷
"بک‌پک ۶"
درباره‌ی چیزهاییه که یک توسعه‌دهنده باید توی کوله‌اش داشته باشه؛ مفاهیم و اصولی از
Back-End
که برای رفتن به آینده، هنوز هم بهشون نیاز داریم.
🔷
"بک‌پک"
بازگشت به گذشته نیست؛ توشه‌ایه که باید با خودت برداری تا بتونی به آینده بری.
💗
اطلاعات بیشتر و ثبت‌نام:
🎒
Register
🎓
کالج پارت؛ در مسیر واقعیت
🔹
🔹
🔹
❤️‍🔥
website
🆔
instagram
🆔
linkedin
🆔
telegram
💬
bale</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/686730" target="_blank">📅 22:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686729">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چرا محک به الکامپ آمده است؟
💊
موسسه خیریه محک امسال به نمایشگاه الکامپ آمده تا از اهمیت فناوری برای ارتباط بهتر با حامیانش بگوید.
دکتر احمدیان، مدیرعامل محک، درباره مسیر تحول دیجیتال این موسسه و نقش اپلیکیشن محک در ساده‌تر شدن مشارکت و همراهی مردم با کودکان مبتلا به سرطان کشور می‌گوید.
روایت حضور محک در بیست‌ونهمین نمایشگاه الکامپ را اینجا ببینید!
لینک نصب اپلیکیشن</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/686729" target="_blank">📅 22:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686728">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khhR5BzVuEGlMTH8GP7zDUMrcBwQzFOViA7Bt4H6G37X2TF3t7ug0bKJ3ZXMpgxHh6VKuIVFfCg2dTD5iglFvP-Grf2nADfWHQvz-GUIF6pgdGE4nEvW2AYTFYma-VYUOxvizPFMl5oJTxRxmdWvWu5gqEf2tYxXBKPms6YV_kdF4qRm6X_GMdD4i7tFFAdhLKUnu5u8DkoNl2wINqidU8vLuE1cPhFaJqyJnqzU_dTnk0YTpBHUi8EKjl8zqNzYr4Mcct0qZdcuJfaXZ80oYGbxCHmTQZ5o2u6A5ZN7EGlkc2M8nT_k2N_axgv46pKE7V-XCrDsdB5Jb0gQvfWgMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دلار ۲۲۰ هزار تومان؛ زنگ خطر معیشت در تله ارزی | چرا ترمیم فوری دستمزدها دیگر یک «انتخاب» نیست؟
🔹
عبور تاریخی نرخ ارز از مرزهای پیشین و پرواز دلار در کانال‌های نجومی، این بار نه صرفا یک شوک روانی به بازارها، بلکه ضربه‌ای مهلک و مستقیم به سفره اقشاری وارد کرده است که سهمی در تعیین سیاست‌های کلان پولی ندارند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3242226</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/686728" target="_blank">📅 22:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686727">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم درباره ایران: دیشب خیلی بیشتر از رادارهای آن‌ها را منهدم کردیم
🔹
حمله دیشب بسیار سنگین بود و ما آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
🔹
ما کنترل تنگه هرمز را در دست داریم، آن‌ها تلاش می‌کردند موشکی بسازند که مین‌های دریایی را پرتاب کند. چه کسی چنین کاری می‌کند؟ من هرگز چنین چیزی نشنیده بودم، اما آن‌ها داشتند همین کار را انجام می‌دادند.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/686727" target="_blank">📅 22:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686725">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9ouju8xA6rGr2ufeXui0PwppbzvW9xkcbkzQL6cbOvnps2kCxjONyxA-i69_AuiZuHdl3JRmDWs-ikIxhGV9p5isB1wNyRpMLcTbmQ4pdLZkGR9lVwyTEx7E-Ve2Tnm22KyUeFu0_7IYXH_jxbQ6PIHBU30Nl5c2UZi5i1Ui2_w8j6Q4LzwZzyBX7d6Ev0C3RNRqW7hnoPyF73JOQCopv_rNlL9xXVEsWARkXPAi3Qx8YNBPK5r-GItjGLJC1tHoZmtHzymoxp-Iom9VyzOJNp-ZhS48EeAdUKqHyVo2M6_k1M3yalzeu_cpVO9YQ0wWQX5mYUgA0MtOAZYiEPCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAW1lf4sfzKZVVdSuUOBwXLsiOCGgBO8uJgkDn_8g98jG3jUN_dGV4DFETxezRr0z9Egzut-RzHvNWPvUN2cT2fNdOwZXz2lNGEUdxLEj4zDu1KtfbrSTignTjX4ZJS4A302MoF3B283VEjYk4KRpTUkewF8tl27zB1XOtPjbRjNFufYfr0yCvJ6GD2LZdvIM41JbG1_S7K4c2sfi2FO90vh2O3X_N_57bBwmg9_EQp8uHmLvYtHTM_ZB-xlHEaZYbvU6X8adKeH7hUMzI-af3pH9ZEPuVjP69CIxcjq-xO11fe0Tg8Sc4AZ1WXZ4chJadMJylAAtmAGD4FuheXYzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فهرست شناورهای متخلف در سایت «نهاد مدیریت آبراه خلیج فارس» به‌روز‌رسانی شده است
متن کامل پیام پی‌جی‌اس‌ای:
🔹
فهرست شناورهای متخلف در سایت به روز‌رسانی شده است. برخی از این موارد با اطلاعات داوطلبانه مردم به دست آمده است که پی‌جی‌اس‌ای مراتب قدردانی خود را بابت این همکاری اعلام می‌دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/686725" target="_blank">📅 22:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686724">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0ZGnj3_Dv4QLypMiUZKYzUnk769mA648ttZefZm582GkHh_zh0rZoBr17R5SfnUqbSK1t7OQQ8EOgGJ1hE7nIhNzEALVAqF4o5xSCZVYlX3sn3ib77dkJgwovQz69E80AOK8e4rTqhHYXa0LSkT9sF6XnkxHKKCG7NqXD84rasy1URjEeM7RMN-XEoLGh8ncLpR3eKugQxfaaBo9cV1E2xwtNHYMnNotboAfhm9nHb9iIllTrWixmizkBreDJrvmjKr_GoVk-Zcax7jG9DDWaCuDOp85dzI1__9EvA6rb_lTQhxT62ZkDF1Ib-s8KEFEHNepcOPbH2pOQgpQCsNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبر، کلید عبور از سختی‌هاست؛ کسی که طاقت و شکیبایی ندارد، در برابر مشکلات زودتر از پا می‌افتد
🔹
امام علی(ع) در نهج‌البلاغه می‌فرماید: «کسی که شکیبایی ندهد، بی‌تابی او را هلاک گرداند.» صبر به انسان توان می‌دهد تا در سخت‌ترین لحظه‌ها استوار بماند و تسلیم بی‌تابی…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/686724" target="_blank">📅 22:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686723">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-text">🎬
جشنواره ۷۵ ساعته آغاز شد!
🕒
✨
۷۵ سال تجربه؛ اعتماد و همراهی
✨
💠
هم‌اکنون وارد جشنواره بزرگ نئوبانک سپینو به مناسبت هفتاد و پنجمین سال آغاز فعالیت بانک صادرات ایران شوید:
🕰
۷۵ ساعت هیجان،
🎁
۷۵ جایزه ۷۵ میلیون تومانی!
❓
چگونه شانس خود را افزایش دهیم؟
🔴
دعوت از دوستان به سپینو
🔵
انجام تراکنش‌های روزمره با اپلیکیشن
🔴
افزایش مانده حساب و دریافت امتیاز بیشتر
🔹
خدمات نوین بانکی، در هر زمان و هر مکان؛
📲
«همه جا با سپینو»
⬅️
همین حالا با دریافت سپینو، وارد جشنواره شوید:
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#سپینو
#جشنواره
#نئو_بانک
#بانک_صادرات
#بانک_صادرات_ایران
#خدمات_نوین_بانکی</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/686723" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686722">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
توسعه خدمات دیجیتال بانک شهر در الکامپ ۲۹؛ از سرویس کهربا تا هوشمندسازی حمل‌ونقل
🔹
حسام حبیب‌الله، معاون فناوری اطلاعات بانک شهر در گفتگو با خبرفوری از سه دستاورد کلیدی این بانک در نمایشگاه الکامپ ۲۹ پرده برداشت.
🔹
وی عملیاتی شدن سرویس کهربا را که امکان پرداخت‌های مبتنی بر NFC را بدون نیاز به حضور فیزیکی کارت فراهم می‌کند، از جمله اقدامات مهم این بانک برشمرد.
🔹
او همچنین از راه‌اندازی نئوبانک ردبانک با ارائه خدمات نوین در حوزه مدیریت دارایی و امضای تفاهمنامه‌ای با هلدینگ گرین وب و پلتفرم مانا جهت هوشمندسازی پرداخت‌های حمل‌ونقل عمومی خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/686722" target="_blank">📅 21:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686721">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnvgkUj7nrXnxwZIt86HBvAenlCENifFgQ6Y52otUpu_Jv7VqAiWufQPWTSasY3HKIGOX1u4F6j_3Uhchl2RhW28XLqYt0bnUOjyfQ264OJllwenopAZopChINC4B7Bq2aQOuiRpYtx0MpIFUAitCQJE8xnvavxRsXYbl2hdhHvUG6fjfJi6GndIo0ZZD3lxZU3mFLavYaIr7h7xlMX23fskinlXLJcw1P8O2_skUuTAC3t11g1rmarniJBEZHG_tH188XKOpRutxgthiPxUltyuAzWbCNhRR5GsST1N8KaioB57VawQPalMxKGbybgKymhQDuEaEcL-GAP80-wb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف گنجینه نقره در حیاط یک خانه
🔹
یک شهروند دانمارکی زمانی که در حیاط خلوت خود مشغول حفاری برای ساخت یک تراس بود، گنجی معادل ۱۸٫۵ کیلوگرم نقره‌ هزار ساله را که در زمین دفن شده بود، کشف کرد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/686721" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686720">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f5cb7d72.mp4?token=vHHgdXoFAOgM8gU2MmFR-7cNKs4rgCOV6zMsRl5PzdLs1PJ9RvEX3du3rbKz3SrYuINDXHCzK0mYxAI1CRAuJnifzAKPlO_kF1Z90oRQ_5L3WNrD92AJysTBAjcjy3631ex4QG5PnjX3CcY8GESbiA0-vQMfHwIpTsr2jofOl4HcPhbDSD30yrJqSGINn8GGJ_gatOgp3yRj_GMSxsrQS-oF9KOzAi9f0gJHW_fAB-J3F5-yE8rNmpxnyqALlYPB8HgNx8UiD9vmaqYU0khs-FOub-ca6LtHMTtXkQUPpsb-NPrRMgRjqb9fjtVfoKPtG03uB_b2CbxVpUE1iBGgHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f5cb7d72.mp4?token=vHHgdXoFAOgM8gU2MmFR-7cNKs4rgCOV6zMsRl5PzdLs1PJ9RvEX3du3rbKz3SrYuINDXHCzK0mYxAI1CRAuJnifzAKPlO_kF1Z90oRQ_5L3WNrD92AJysTBAjcjy3631ex4QG5PnjX3CcY8GESbiA0-vQMfHwIpTsr2jofOl4HcPhbDSD30yrJqSGINn8GGJ_gatOgp3yRj_GMSxsrQS-oF9KOzAi9f0gJHW_fAB-J3F5-yE8rNmpxnyqALlYPB8HgNx8UiD9vmaqYU0khs-FOub-ca6LtHMTtXkQUPpsb-NPrRMgRjqb9fjtVfoKPtG03uB_b2CbxVpUE1iBGgHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیالوگ جدید محمد نوری: همه ما جایزالخطا نیستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/686720" target="_blank">📅 21:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686719">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
قالیباف: در منطقه جنوب غرب آسیا تحولات بزرگی در جریان است که این تحولات حاکی از تغییر و تحول جدی در نظم منطقه‌ای است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/686719" target="_blank">📅 21:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686718">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
رونمایی از پروژه‌های جدید دات‌وان
🔹
بابک زنجانی، رئیس گروه ارزش‌آفرینی دات‌وان از رونمایی چند پروژه جدید در دات‌وان خبر داد و گفت: در حوزه تاکسی‌ها توضیح خواهیم داد که چرا تاکسی‌های دات‌وان برای کشور اهمیت دارند. همچنین درباره رسانه، اپراتور جدید، طلای دات و سایر پروژه‌های این مجموعه توضیحاتی ارائه خواهد شد.
🔹
او درباره حوزه پست و لجستیک نیز گفت: تا سال آینده تحولاتی در این بخش ایجاد خواهد شد و «پستکس» می‌تواند در شرایطی که ایران با محدودیت‌هایی در حوزه پست بین‌المللی مواجه است، نقش مؤثری در عرصه بین‌المللی و داخل کشور داشته باشد.
🔹
مشروح این خبر را در سایت خبرفوری بخوانید:
https://www.khabarfoori.com/fa/tiny/news-3242267
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/686718" target="_blank">📅 21:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686717">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای آژانس اتمی درباره راستی‌‌آزمایی در تأسیسات ایران
🔹
آژانس بین‌المللی انرژی اتمی اعلام کرد از ماه فوریه تاکنون، به‌جز نیروگاه بوشهر، هیچ فعالیت راستی‌آزمایی در تأسیسات اعلام‌شده ایران انجام نداده است.
🔹
آژانس همچنین اعلام کرد از ژوئن ۲۰۲۵، توانایی خود…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/686717" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686716">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/279257d0dd.mp4?token=bXd9odKiaSVVScJYyl9XH5PeBCl53JDJPIndH3UeHXAgA7BxPrl1b_CGYdo82pWyEzuxjzZxeaQSJW_aLPak8MQc5DXExqn_Ra5jrvFqmrg87P6KcTJDxR-ieZP6onqZKFccLmURXz18wNZGzqHD1Bllw0hDOU5exQJrFa8SxcRDPVTdg6nM2QCf1z7gKKmYx0zn-ZiLdjG_8LChOoI9ArumB2LI6S3S5azuNm3TkvRsNSQD1sX5gRlqXnxIkFCcPvQEL2LsZSSwhL3pYQv1C1MIatdyQ471Jmg8bdCB2F6vQLlfZCSry-8fflp25BgShYtuoNbsjy0Gzg6iz_q2oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/279257d0dd.mp4?token=bXd9odKiaSVVScJYyl9XH5PeBCl53JDJPIndH3UeHXAgA7BxPrl1b_CGYdo82pWyEzuxjzZxeaQSJW_aLPak8MQc5DXExqn_Ra5jrvFqmrg87P6KcTJDxR-ieZP6onqZKFccLmURXz18wNZGzqHD1Bllw0hDOU5exQJrFa8SxcRDPVTdg6nM2QCf1z7gKKmYx0zn-ZiLdjG_8LChOoI9ArumB2LI6S3S5azuNm3TkvRsNSQD1sX5gRlqXnxIkFCcPvQEL2LsZSSwhL3pYQv1C1MIatdyQ471Jmg8bdCB2F6vQLlfZCSry-8fflp25BgShYtuoNbsjy0Gzg6iz_q2oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از تقلید صدای موتور تا شهرت جهانی!
🔹
یک پسر ۱۷ ساله سوئدی در سال ۱۹۹۷ صدای موتور دوزمانه را با دهانش تقلید کرد؛ صدایی که سال‌ها بعد به «Crazy Frog» تبدیل شد و دنیا را گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/686716" target="_blank">📅 21:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686715">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHosfWbcVwULJFOyW5ey4_LBX-qJ3U2c5fddKbh5YL4ClukcHCQmWnn4Y5sDPgDjlLm90usFi1ud5nyrSmMgVe5f8GaCxFUxG3UK5sI1OIK2PqxwItfMee5-AwsBbwkZPpVOwnQdjsV5NvCGx9tvqIzVSpvp-HQxRMu63Xz9W90wDeh4h4YHusz-Jb5xjyg0edtBLMNov-HNmbIE9RUKVyRTO7PpbCaAY7LJvfOjbZ_adBXGfKBmOZ60FxCTacK_VMXOwj_fNM5JUK36pm3DQ397iJ1Dj1XKMNK7NWwssnta4RsqTOXVqDK5VkBwL58yuBCPfetMXZBXqJ61QYMHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دربی مساوی شد
🔹
استقلال ۱ - ۱ پرسپولیس
🔹
گل‌های این بازی را محمدمهدی محبی و یاسر آسانی به ثمر رساندند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/686715" target="_blank">📅 21:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686714">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ya3QTi3YjXWod5kjTLQNZ7HvgPYbpX34q98DEO-KVuC_OdXjYuDDp_17h9ueA7qXz_zKjy4XWp6JyEMmQCRdeQSgs8Ssgm0Vt4QMglGk318oGRa0eSUU4fNfhS-bvAsdq-mzfCdibtteFu4Fy22RnSfEGbhwwFQYgV5ZukBxmufwwTr0fxWgzPkgbHtk2rULUONkp4e-T8pY6_o8Uj9INLT99OGooSuTupOR8XtHoyL5ZMxbimLH85YUFODmx9DFLggJ4i8E410sGcHL0AzL0uDO1B4jvjY42BO2_7tiuS7AJVK1-M9RFzZ-50kGoBV6XwM6jWiBh7hBN016KJKYRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از هر ۸ بزرگسال آمریکایی، یک نفر GLP-1 مصرف می‌کند
آمپول‌های لاغری شاید هنوز روشی تازه و حتی نگران‌کننده به نظر برسند؛ اما این درمان‌ در جهان بیشتر از چیزی که تصور می‌کنیم رایج است.
براساس یک نظرسنجی در نوامبر ۲۰۲۵،
۱۲٪ از بزرگسالان آمریکا
یکی از داروهای موسوم به GLP-1 را مصرف می‌کنند و
۱۸٪
هم حداقل یکبار از این داروها استفاده کرده‌اند.
این آمار نشان می‌دهد آمپول لاغری که تا چند سال قبل برای بسیاری ناشناخته بود، حالا به بخشی جدی از مسیر درمان
چاقی، دیابت و بعضی بیماری‌های مزمن
تبدیل شده‌.
از ترکیبات شناخته‌شده این حوزه
تیرزپاتاید
است که در جهان با
مونجارو
و در ایران با نام
زیکورپا(داروسازی دکتر عبیدی)
در دسترس است.
رواج استفاده از این دارو به این معنا نیست که برای همه مناسب‌ است؛ و مصرف آن باید براساس شرایط جسمی و
با تجویز و نظارت پزشک
انجام شود.
منبع:
نظرسنجی KFF، نوامبر ۲۰۲۵</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/686714" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686713">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ادعای آژانس اتمی درباره راستی‌‌آزمایی در تأسیسات ایران
🔹
آژانس بین‌المللی انرژی اتمی اعلام کرد از ماه فوریه تاکنون، به‌جز نیروگاه بوشهر، هیچ فعالیت راستی‌آزمایی در تأسیسات اعلام‌شده ایران انجام نداده است.
🔹
آژانس همچنین اعلام کرد از ژوئن ۲۰۲۵، توانایی خود برای ردیابی ذخایر اعلام‌شده مواد هسته‌ای در تأسیساتی که هدف بمباران قرار گرفته‌اند، از دست داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/686713" target="_blank">📅 21:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686712">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8262727fec.mp4?token=piFwbVqfzJ3ftHwgT-NTJMFZqbw7A7eOcoP1eBKUUYtkTaSZ7tRjN35bolGwZ-lKa0Ix8CSNk1F7PWxrwnJ7XYCN2qhaJN6UJrznXmrs2Y9mTl5xMbUyecr8BQqjb6MAtQzeFl277UjPIpTQiiDwDYxC2ghl0YIajGtPLg70kT6vsyiv_OSZ31nNLMTUdD5w8afEnNZ1tbt2TtcgyNP65eP6wgg3EbzEtyFVA6ls23PC6TDinqMuU1hlBdkh_Wu-7m5OsjrUJbPz8RX0bR79TLl2nSwGvoffZDApCl2SnCVFwjyKhqMePfUYb8PL2xKeLFZBklmhUDGm5lge88x1IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8262727fec.mp4?token=piFwbVqfzJ3ftHwgT-NTJMFZqbw7A7eOcoP1eBKUUYtkTaSZ7tRjN35bolGwZ-lKa0Ix8CSNk1F7PWxrwnJ7XYCN2qhaJN6UJrznXmrs2Y9mTl5xMbUyecr8BQqjb6MAtQzeFl277UjPIpTQiiDwDYxC2ghl0YIajGtPLg70kT6vsyiv_OSZ31nNLMTUdD5w8afEnNZ1tbt2TtcgyNP65eP6wgg3EbzEtyFVA6ls23PC6TDinqMuU1hlBdkh_Wu-7m5OsjrUJbPz8RX0bR79TLl2nSwGvoffZDApCl2SnCVFwjyKhqMePfUYb8PL2xKeLFZBklmhUDGm5lge88x1IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه‌‌ای که بازیکنان پرسپولیس اعتقاد به پنالتی داشتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/686712" target="_blank">📅 21:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686711">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
انفجارهای کنترل‌شده از ۱۲ تا ۱۶ شهریور در بوشهر
فرماندار بوشهر:
🔹
عملیات انهدام مهمات عمل‌ نکرده متعلق به حملات جنایتکارانه آمریکایی - صهیونی در تاریخ ۱۲ شهریورماه الی ۱۶ شهریورماه از ساعت ۸ صبح الی ۱۲ ظهر در حوالی پایگاه دریایی بوشهر انجام می‌شود.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/686711" target="_blank">📅 21:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686710">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8628a80e70.mp4?token=smYDA3y2b9CW5pNkNbV6V7g_m1EFEouZ0gtjpjAXbIyDfNz6e3fXGDkMHoTQimWp_kCDhvANzA4oq1Sl_-CV0oXVdvjlisQ6rG9zOCy5gPDQN9QPAL88rNMpjgdWlL_3bCjhxZuygv_5mOthpJLbxY0lLDhUk1lEZFF-FlKdiyaoF_xi6E2y2KXMNJaKhFWeQ0Z1aVTsfQZKeSp5uQTAXJQUJn4e2nItBmCxj2PDcBo_O6tkOhbk-lfPzXIttYQPgT8Uc51cUAlbjr0-IvcvlAkZFEKmvEhsqtLCTlIIeTte3ZIEwOIkYGEqDc-ETv2i5lK85EEyTFjUnazcqHxDcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8628a80e70.mp4?token=smYDA3y2b9CW5pNkNbV6V7g_m1EFEouZ0gtjpjAXbIyDfNz6e3fXGDkMHoTQimWp_kCDhvANzA4oq1Sl_-CV0oXVdvjlisQ6rG9zOCy5gPDQN9QPAL88rNMpjgdWlL_3bCjhxZuygv_5mOthpJLbxY0lLDhUk1lEZFF-FlKdiyaoF_xi6E2y2KXMNJaKhFWeQ0Z1aVTsfQZKeSp5uQTAXJQUJn4e2nItBmCxj2PDcBo_O6tkOhbk-lfPzXIttYQPgT8Uc51cUAlbjr0-IvcvlAkZFEKmvEhsqtLCTlIIeTte3ZIEwOIkYGEqDc-ETv2i5lK85EEyTFjUnazcqHxDcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرعباسی مانع گل شدن ضربه زاویه بسته عمری شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/686710" target="_blank">📅 21:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686709">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53b27efc0.mp4?token=b0RgxCDRyctJNWWaUCZ9BjfvMD83TZGn6aE2bV8aT0mU6DnQDADzI28txobstx140lrYwGgw2_WQt1EDSRzGMTvD3WFNMy7UoAkPNXf9z6ahNI5iE8AIEx4TGd29FsLIxPr_Jw-BxRsmyOl5oqjJkpWeUq7i7MvPbTgA0z6W0u8-ukfjfpIa72AwqlZJTMT9IanEfyt4Tw7rKyOz4s61pgVt8gzEL0QV9WBm-JwMzZ0SNeG1JgrTTyiyLHIaOgwJZ7VCNuDBzClktz2h4fRmWd_Tox-_YO8PP22tjdaA-t_U8KnDx3A-HxF1j54ssxyuSoScnc5MTuYpCAJg8_Q-ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53b27efc0.mp4?token=b0RgxCDRyctJNWWaUCZ9BjfvMD83TZGn6aE2bV8aT0mU6DnQDADzI28txobstx140lrYwGgw2_WQt1EDSRzGMTvD3WFNMy7UoAkPNXf9z6ahNI5iE8AIEx4TGd29FsLIxPr_Jw-BxRsmyOl5oqjJkpWeUq7i7MvPbTgA0z6W0u8-ukfjfpIa72AwqlZJTMT9IanEfyt4Tw7rKyOz4s61pgVt8gzEL0QV9WBm-JwMzZ0SNeG1JgrTTyiyLHIaOgwJZ7VCNuDBzClktz2h4fRmWd_Tox-_YO8PP22tjdaA-t_U8KnDx3A-HxF1j54ssxyuSoScnc5MTuYpCAJg8_Q-ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرماندار مشهد: علت تصادف بلوار وکیل آباد ترافیکی بوده است  فرماندار مشهد ضمن ابراز همدردی عمیق با خانواده جان باختگان تصادف رانندگی شب گذشته در بولوار وکیل آباد این شهر:
🔹
طبق بررسی های انجام شده حادثه شب گذشته صرفا ترافیکی بوده و هیچ علت ضد امنیتی در وقوع…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/686709" target="_blank">📅 21:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686708">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e915a6a216.mp4?token=t03qE2YBM_cGCIY8ftRTRXWI2NrNxnfZRQS1X49fHwzfGWdNnTfyANsezJ_Hf4vrmWm-GZ37LIOkcwJFehV9z0IUiKPFGxQuyLp680OYttd-MN0Ttgp5zg4ZiiTKYTpyrZbQZIVKWD70JgjUJ8OUhjzaPi211qbbnOtLoixC5eQH05NeUAP6EwkzmZsesJFCUzeiGQFrTQa5WF3ohtPDWAnJKFm3369znbxqBUy_0_A663rPhnQtmHUrBRWxCzL4DXMqbBsmevQoe9Dn9ffsb493Cr1k6QBAuJmfXHdsI2-Y9YTaZiYfYwkFJl8Yq6VO8aXvZ3WplfuSj_CodnxIsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e915a6a216.mp4?token=t03qE2YBM_cGCIY8ftRTRXWI2NrNxnfZRQS1X49fHwzfGWdNnTfyANsezJ_Hf4vrmWm-GZ37LIOkcwJFehV9z0IUiKPFGxQuyLp680OYttd-MN0Ttgp5zg4ZiiTKYTpyrZbQZIVKWD70JgjUJ8OUhjzaPi211qbbnOtLoixC5eQH05NeUAP6EwkzmZsesJFCUzeiGQFrTQa5WF3ohtPDWAnJKFm3369znbxqBUy_0_A663rPhnQtmHUrBRWxCzL4DXMqbBsmevQoe9Dn9ffsb493Cr1k6QBAuJmfXHdsI2-Y9YTaZiYfYwkFJl8Yq6VO8aXvZ3WplfuSj_CodnxIsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت تکنیکی محمدمهدی محبی بی‌ثمر ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/686708" target="_blank">📅 21:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686707">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhiJyY3FRJYvXhY8Txt4bz9TJpy_Zc7dsiNY-xsBEf4BNiTD2QpE9isC7DkUpTMU5Ty09e7wkhpSND3iC1gF8glYdahgLSnCQj7nATscplHvq0yRRg99ZlH8HpA2csMH1CjUuPR71wpfoHdrC0Zx3XGrTDox9NdcC00MmuCcFJ_cbgNw9ob0HxmCUK05F4LQxALOmvaM58tTZAJhVZzscEewlyLMG4Rb6hBH-ZuyI0lOpyIbnAB5XzLYYMtbnYEXWiEfxXzw7uLYdPjJcBJK0DzT7iuLFd1IpZVv86QF1hBQOE89g24hx_dF5ALPpJ0prGPTQ6AivOnndsCqX1dpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سلفی همسر عراقچی، دختر پزشکیان و فاطمه مهاجرانی| امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/686707" target="_blank">📅 21:10 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686706">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9590a8577f.mp4?token=mI7HPLWrl-6K0zsePYh2Py1Gdi7Ws0ss__pPxvnEwf0V0ukjEHe7GTk7jWp_5_2AkfCMRvaImnEOpQq2Q6ySNl0R9Q29HJuQq6mKGPpotn74gmbS0CMKkLk-A31C1kI8qlgBUeNaBJVvtjDSzST3VX6NZVwRsW_HOJ9HEuCIJqAAcPBJ-FOCrWZKJzPnBG-ZHXHxemMkWF3Uncob9310i1VY8OtxlS7xxsPQ3VeI7NLl260w16Cl6kbawtmwa89aIicFx7aExYw81xNgMDFhRrYXMOFAqlyMRtqqv-0kdzguVOiHZhIuWO77p-Zak3tm7eZEzluCwvFB0nvNnlCmWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9590a8577f.mp4?token=mI7HPLWrl-6K0zsePYh2Py1Gdi7Ws0ss__pPxvnEwf0V0ukjEHe7GTk7jWp_5_2AkfCMRvaImnEOpQq2Q6ySNl0R9Q29HJuQq6mKGPpotn74gmbS0CMKkLk-A31C1kI8qlgBUeNaBJVvtjDSzST3VX6NZVwRsW_HOJ9HEuCIJqAAcPBJ-FOCrWZKJzPnBG-ZHXHxemMkWF3Uncob9310i1VY8OtxlS7xxsPQ3VeI7NLl260w16Cl6kbawtmwa89aIicFx7aExYw81xNgMDFhRrYXMOFAqlyMRtqqv-0kdzguVOiHZhIuWO77p-Zak3tm7eZEzluCwvFB0nvNnlCmWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موقعیت خطرناک گلزنی یاسر آسانی روی دروازه پرسپولیس در دقیقه ۷۲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/686706" target="_blank">📅 21:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686705">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b314d9ba45.mp4?token=cBr1DOzPm_7eJKo4XcDDrwTglL3x9edoSStyyFSzCEL_7U0Fb9z_6c0PvxMZePV7iM4HK2fhNM36Mv_uPjQcYkahQZIoPu2yCMc60fFFwPkf0a7zy5lKKCKRnRTh0jAHS2W76pvUK1GDc2V0APsJUxpwdjw3ylAvfCafHs0igbg41qHghQabAkOFKBLyj0sNYd6ItEHmeDQcMebDlxgQz_nsobEVvz_arZ8mAuEIR7Wt-BTYhjAaM7Ay1Cqzf9csmmh3_p5vHyQPjQJfh8Hovnad1A9kj9sGlUL1Uw6Hs_f_DNDAN14bapHsHjU_JpwNuMJIS1IMKgf0TjMLG_rgA1873UhMuMfdw22DYmLW4gKaNLU9rqHqpCAXDnj7S6ZmTLtpl49cY0QFlZKfbb_Xr0I7arRhk9cTaKdZXBcSW0QNeEGJJ2i9be8FdnwXPtqTZ3Spx_ZlBa6ykytDPmexLHKQyjaJ9iJv7EFqkHyWNqIQjyNKLXCaqxBT1EL-XMu50YAlfc1RVK_XqVt8IUZJKoMSXNGwdczKjMtSLbqi3k2LC5tJpf1vhCuUkmIN9ZcA401jon7g0LSNpoGgZJw2N3fL23I1xQwgOysVsidlM23YZ2_EsW12ujrV4PbCHgyyjERi_R2TxceIefRSu46XQnhMWN77szVqtHTRE5WYG-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b314d9ba45.mp4?token=cBr1DOzPm_7eJKo4XcDDrwTglL3x9edoSStyyFSzCEL_7U0Fb9z_6c0PvxMZePV7iM4HK2fhNM36Mv_uPjQcYkahQZIoPu2yCMc60fFFwPkf0a7zy5lKKCKRnRTh0jAHS2W76pvUK1GDc2V0APsJUxpwdjw3ylAvfCafHs0igbg41qHghQabAkOFKBLyj0sNYd6ItEHmeDQcMebDlxgQz_nsobEVvz_arZ8mAuEIR7Wt-BTYhjAaM7Ay1Cqzf9csmmh3_p5vHyQPjQJfh8Hovnad1A9kj9sGlUL1Uw6Hs_f_DNDAN14bapHsHjU_JpwNuMJIS1IMKgf0TjMLG_rgA1873UhMuMfdw22DYmLW4gKaNLU9rqHqpCAXDnj7S6ZmTLtpl49cY0QFlZKfbb_Xr0I7arRhk9cTaKdZXBcSW0QNeEGJJ2i9be8FdnwXPtqTZ3Spx_ZlBa6ykytDPmexLHKQyjaJ9iJv7EFqkHyWNqIQjyNKLXCaqxBT1EL-XMu50YAlfc1RVK_XqVt8IUZJKoMSXNGwdczKjMtSLbqi3k2LC5tJpf1vhCuUkmIN9ZcA401jon7g0LSNpoGgZJw2N3fL23I1xQwgOysVsidlM23YZ2_EsW12ujrV4PbCHgyyjERi_R2TxceIefRSu46XQnhMWN77szVqtHTRE5WYG-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمول کانون ایران ‌نوین برای تسخیر ذهن مخاطب
🔹
محمدرضا هاشمیان مدیر خلاقیت کانون ایران نوین از جسارت در خط‌شکنی تبلیغات و مهندسی کمپین‌های میلیونی می‌گوید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/686705" target="_blank">📅 21:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686704">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLrD8YGU7FBgmfzIF2g0FnwOXSyyUcLwk3X3l8G9cTq75BmxKhq3W-TxEXdNS-lF_atjbYN-4bR32t3bJxijJptkhnhUP4A6ZuM_X-PEEWi0Ujk0P3NWsQiFL7AnAY-X3RCN5silaDFNSfayg85BCof7qOuRYYx4ChAoDcrkOmVWxGJBTQo_vy8t_OkGC907a-zXmJCZi7lHBiqt7OeT6VuAjjSOQBKhBoXO8o9k3p-wkJwvxSXwtx75uX2-MkxN_hGGw473ObNvi2I3vUyIjrbutmnYO4PmG6wPxmwIB75RoxQhBInQlIK_Mh8Eyblclc8Ejm9equvfz6CElRwsjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در دنیای هوش‌مصنوعی GEO چه کاربردی داره؟ #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/686704" target="_blank">📅 21:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686703">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
ادعای روبیو: یادداشت تفاهم اسلام‌آباد منقضی شده است
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/686703" target="_blank">📅 21:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e7f3537d.mp4?token=I9YgpgDDDSho4EnyPFbQGjrG1DvqVdRbJTv2jArOT5JOirKuuHMXNlSVjfuLuRfKdPkDVpB7-aE7N1-57rzlVcwf3JosBUqbxUgJEFgHYfE7upL89IHz2fag9Rtha0FV7yiDGaebDB2hNstndvPP9d4LBHA1Gpc35pNVahPaAHpNOAQXCAAMEN5c5g8dd4-3KZ8e3pkg_F4vmLH4U8oxbt_mFCMCFd3S-t9Mrr-gHjgulzOnqDRNCUZFlifWjXxMCiNsivD12lhNVgnIWJPlNRVKGdufWGwtrl14Uj9m1JohlB9bewtsnlQajg4_nCzINduJedoUpdNe3SnD3Z1ljQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e7f3537d.mp4?token=I9YgpgDDDSho4EnyPFbQGjrG1DvqVdRbJTv2jArOT5JOirKuuHMXNlSVjfuLuRfKdPkDVpB7-aE7N1-57rzlVcwf3JosBUqbxUgJEFgHYfE7upL89IHz2fag9Rtha0FV7yiDGaebDB2hNstndvPP9d4LBHA1Gpc35pNVahPaAHpNOAQXCAAMEN5c5g8dd4-3KZ8e3pkg_F4vmLH4U8oxbt_mFCMCFd3S-t9Mrr-gHjgulzOnqDRNCUZFlifWjXxMCiNsivD12lhNVgnIWJPlNRVKGdufWGwtrl14Uj9m1JohlB9bewtsnlQajg4_nCzINduJedoUpdNe3SnD3Z1ljQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربه کاشته آسانی در اختیار نیازمند قرار گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/686701" target="_blank">📅 21:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686700">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904e741dbe.mp4?token=WgYjUD9dYLdNxvY2s3wdJsgmmULhe-gRQGeQe1qd_DO6JawEY7KuFvgablpzCwrwSUDaZ5FSwc8Y-Czpv2zE-c03j1wkdw45UWRgdNCTn_jErsAsM15VAu6SkdRIo5Z4oNlY_aCQKTYKbyXrL3qa0HHCbQGGxmdLpSPsz26Djs9nMLqeHitUmpOJdpoRuS5LYP3vMIYi-EAIlnp7bEHpHVALDTXdjS-Mrr1dPAF8ll6ipKvqIAOqF2JGs7ngVZJ4ejFeUykgXoP6YXZ-VuwV5J4hn3bpoRLVDRgdKiIKRXwEKby0adqABSTIJGTTeEmVpbfw6HQl5GcpBpJH8yNtVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904e741dbe.mp4?token=WgYjUD9dYLdNxvY2s3wdJsgmmULhe-gRQGeQe1qd_DO6JawEY7KuFvgablpzCwrwSUDaZ5FSwc8Y-Czpv2zE-c03j1wkdw45UWRgdNCTn_jErsAsM15VAu6SkdRIo5Z4oNlY_aCQKTYKbyXrL3qa0HHCbQGGxmdLpSPsz26Djs9nMLqeHitUmpOJdpoRuS5LYP3vMIYi-EAIlnp7bEHpHVALDTXdjS-Mrr1dPAF8ll6ipKvqIAOqF2JGs7ngVZJ4ejFeUykgXoP6YXZ-VuwV5J4hn3bpoRLVDRgdKiIKRXwEKby0adqABSTIJGTTeEmVpbfw6HQl5GcpBpJH8yNtVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صادق خرازی: رهبر شهید فرمودند اختلاف من با آقای خاتمی در سیاست خارجی ۲ تا ۳  درصد است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/686700" target="_blank">📅 21:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686699">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIX1-I3R5R_0wTRsm2zDaS6gj4TXrQF9SC9rsVm_9ZdRO4Xob4QsZfJ4ZK1MRJo8Hhkq3yn_nWLwluY0k0q_L4W1x8x21Zis9hwutY_T7tO0o6lgU__bf3jlYxIHEjWW033F6wNsqGcgRlOO_hJLytV2k_KXukHduC664y8Qp6IH91hVgAPbWzqTnE2vA25uDP6U-6vXRKHLI0b7W77yah_8POzyvBVwhairVu3Wj2HKW_JnYzfwsKOBTdnZwuXuhcZOsLWeYLTaCiaOJZ9ZDZeWMa517bEkPI1sdpWexuhfSJulYtcL5qQpRguWag40klAcxJVvxrWhzn3TYhJACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جراحت شدید عارف آقاسی در درگیری با کنعانی‌زادگان
🔹
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/686699" target="_blank">📅 21:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4024730870.mp4?token=E2cdpfalfrxIIvfeVXxrqwfrbN_rjy1j9roVc4Z2TWFX0NTOpNAJGpgSVOnMOL7UHwGCUaZiqqU2iWDrbZK1pAXI-GaGVdOJm839gLTPYGU3gHsy2vBt5E6ShKQYnTiihj3pDc2Ishcy3K6wuSC_BMb-UGhkR5KLKgps4iHcT3OgbQdHxmbV2SuhZq5CIF56wj2ghBHhIbXPxvXX9XtA1Nyy8XBOYQpKgjomhrXgKwdvRx1_Z3d4ErTVWFCuT0YnRJ16l2oRHCukeu2L5XkVj5S1Gs7X90twSkuSDV9jAPrKKqzvRaXkDREljcDk-ujCmxIVl7zGGPXvSLbq_aZydQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4024730870.mp4?token=E2cdpfalfrxIIvfeVXxrqwfrbN_rjy1j9roVc4Z2TWFX0NTOpNAJGpgSVOnMOL7UHwGCUaZiqqU2iWDrbZK1pAXI-GaGVdOJm839gLTPYGU3gHsy2vBt5E6ShKQYnTiihj3pDc2Ishcy3K6wuSC_BMb-UGhkR5KLKgps4iHcT3OgbQdHxmbV2SuhZq5CIF56wj2ghBHhIbXPxvXX9XtA1Nyy8XBOYQpKgjomhrXgKwdvRx1_Z3d4ErTVWFCuT0YnRJ16l2oRHCukeu2L5XkVj5S1Gs7X90twSkuSDV9jAPrKKqzvRaXkDREljcDk-ujCmxIVl7zGGPXvSLbq_aZydQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوشحالی بازیکنان استقلال پس از به ثمر رسیدن گل تساوی برابر پرسپولیس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/686698" target="_blank">📅 20:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686697">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40dc1081b3.mp4?token=hjYSHeEzmHXhzGDZTNUPwue8D6DLBvrLThXn_HKD5Uu-CYn9QFVAEuPM4IWNEbYUEsCEnhN5AjofVYdkCi3fjZEAsq5LXKxcaVoFGPrhhRcybaz8AgRuOKQZhwSbUKqXFxXumPKdnv9DRojrE0lOI2xcyCpq30GeO7P1fNd_G-xSHnIbxLqjzVw1qXAgfwOxF4FqY3GDk7En6ZNeGKcGRCi_yYfFcXSFKx2N5Ly1bKZStjwSfdVM8yVqaFX-h0eP2mV5MmE4yD7qRIxayjkQ1wmzZioL-v79UbIBaRynOVn-EmvzMZuW2rrQiFQYPuF9dj3vDJssyBH5mKCM6NXz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40dc1081b3.mp4?token=hjYSHeEzmHXhzGDZTNUPwue8D6DLBvrLThXn_HKD5Uu-CYn9QFVAEuPM4IWNEbYUEsCEnhN5AjofVYdkCi3fjZEAsq5LXKxcaVoFGPrhhRcybaz8AgRuOKQZhwSbUKqXFxXumPKdnv9DRojrE0lOI2xcyCpq30GeO7P1fNd_G-xSHnIbxLqjzVw1qXAgfwOxF4FqY3GDk7En6ZNeGKcGRCi_yYfFcXSFKx2N5Ly1bKZStjwSfdVM8yVqaFX-h0eP2mV5MmE4yD7qRIxayjkQ1wmzZioL-v79UbIBaRynOVn-EmvzMZuW2rrQiFQYPuF9dj3vDJssyBH5mKCM6NXz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به پرسپولیس توسط یاسر آسانی در دقیقه ۶۰
🔹
استقلال ۱ - ۱ پرسپولیس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/686697" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686694">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنمابان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUu_tsdh1MWUKSZ32tP-RKilP67ewfjuEk9q3MdxEiv3hmjrUA1lbf5kNGEH8pKu19o-6lwn2Iv5-uRB2LDPDDXzz43NHzViXZv4ltO7jUk2BzrJjMtgJjbzdRByYQ_igv00J7nCyG_PTqbyZJkLCLByYvsF-5xffAKutjHBRNbmT2nUuSdBro1seIDLdPY6rlqkWBaZvHUu8g1dVj_OCH3w1-qUmVbTz3BwzIKsUz3VWYlA0Jw63oGbx0ow1HtfJ75S7P5Z8AoqSVlUsHscmXSrD48HmJlwJykNIeulCK4MM4ZW8R3bfZ_CEQ-Lt8AEwYAQuriYzDZxM8QtkgvV2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دام تازه با وعده «اینترنت آزاد» در اینستاگرام
کلمه وصل را کامنت کن تا راهکار اتصال ابدی به اینترنت آزاد برای تو دایرکت شود. چنین جمله‌ای برای بسیاری از کاربران وسوسه‌کننده است. به‌ویژه در روزهایی که نگرانی درباره دسترسی به اینترنت و اخبار مربوط به جنگ، به یکی از دغدغه‌های جدی مردم تبدیل شده است. اما پشت برخی از این وعده‌های جذاب، چیزی جز یک شیوه قدیمی کلاهبرداری با ظاهری تازه نیست.
در روزهای اخیر پست‌هایی در اینستاگرام منتشر شده که با استفاده از اخبار جعلی و حتی نسبت دادن ادعاهایی به وزیران یا مسئولان کشور، کاربران را تشویق می‌کنند برای دریافت «راهکار اتصال به اینترنت» وارد لینک ربات‌های تلگرامی یا صفحات مشکوک شوند.
این روش البته تازه نیست. کلاهبرداران بارها با سوءاستفاده از موضوعات داغ روز و ایجاد حس اضطرار یا کنجکاوی، کاربران را به کلیک روی لینک‌های ناشناس ترغیب کرده‌اند. تفاوت این بار، استفاده از نگرانی عمومی درباره اینترنت و شرایط روز کشور به‌عنوان طعمه است.
در چنین شرایطی، مهم‌ترین راه پیشگیری، خودداری از ورود به لینک‌های ناشناس و اعتماد نکردن به ربات‌ها و صفحاتی است که وعده‌های غیرعادی می‌دهند. پلیس فتا نیز بارها درباره لینک‌های جعلی هشدار داده و تأکید کرده است که انتشار و بازنشر شایعات و اخبار کذب در فضای مجازی می‌تواند پیگرد قضایی داشته باشد. / نمابان
📱
@namabantv
📱
namabantv
📱
namaban.com</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/686694" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686693">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67db30b4bb.mp4?token=LeA7sLgDvqt5rerSIjXjQ8Dw6Iw2wwLA0Lf6ptAmzW8EYZP7g1MQCZbCUR-HUd054tZSVOKJKs188-waTA5sS5Qhj02OvEE-iAr_lhqXqZJu_2-Zv2FW3egeDK0Rc7V8CXq5qwczivO7LaFnfp8ihwbLwqMCMzE03Y2hmLPNXeswIO1BwgkslpwKsi1IzSHrK7dSA5FEXb1o5O7lIlrw9z5wcxqjs-en2NxFDBsnfY5FvwF99T4psGOo2b58iCigQoxa5-aqw-6JG02TH-3h6OjJ3fG_RMmyyTCJsMcbaMwqnoW3TVowr6J1XMRwm2GrnhHxIr10t00wICbvxsW8Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67db30b4bb.mp4?token=LeA7sLgDvqt5rerSIjXjQ8Dw6Iw2wwLA0Lf6ptAmzW8EYZP7g1MQCZbCUR-HUd054tZSVOKJKs188-waTA5sS5Qhj02OvEE-iAr_lhqXqZJu_2-Zv2FW3egeDK0Rc7V8CXq5qwczivO7LaFnfp8ihwbLwqMCMzE03Y2hmLPNXeswIO1BwgkslpwKsi1IzSHrK7dSA5FEXb1o5O7lIlrw9z5wcxqjs-en2NxFDBsnfY5FvwF99T4psGOo2b58iCigQoxa5-aqw-6JG02TH-3h6OjJ3fG_RMmyyTCJsMcbaMwqnoW3TVowr6J1XMRwm2GrnhHxIr10t00wICbvxsW8Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
شادی بازیکنان پرسپولیس پس از به ثمر رسیدن گل اول به استقلال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/686693" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686690">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fd3464eb.mp4?token=aiK7bAG_8FiO6ZrwU-NlqTqglfROnOgRcZfbpxUxb3gFHkMxqFqQFPLutTvhjprvYFSu6_TzUbHIohtclR6Z_MAq_Vo4PTc-NEHBHzC7cIiuGSUlxLRagROimGzZjJj6hL1sJCg3051DgUTPybnKnYanCHeK3e9Rpg5sqoWvNahGUD1fHLc6_sO9SzwCgASWEDqHU0RRX9mIMiHtFmeuYZSyuINkKICpxAEaQVSsdD95jh-T1ez0zGLNS5DSk8d3MWax_pTghbbuKDQBs5PIFRZlfUwBV7Kz4DrgC7jLYfLyVbBfP1UOP0FV1UUMCX1dtALk3nUigBpO8_JTDO_Mdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fd3464eb.mp4?token=aiK7bAG_8FiO6ZrwU-NlqTqglfROnOgRcZfbpxUxb3gFHkMxqFqQFPLutTvhjprvYFSu6_TzUbHIohtclR6Z_MAq_Vo4PTc-NEHBHzC7cIiuGSUlxLRagROimGzZjJj6hL1sJCg3051DgUTPybnKnYanCHeK3e9Rpg5sqoWvNahGUD1fHLc6_sO9SzwCgASWEDqHU0RRX9mIMiHtFmeuYZSyuINkKICpxAEaQVSsdD95jh-T1ez0zGLNS5DSk8d3MWax_pTghbbuKDQBs5PIFRZlfUwBV7Kz4DrgC7jLYfLyVbBfP1UOP0FV1UUMCX1dtALk3nUigBpO8_JTDO_Mdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول بازی برای پرسپولیسی‌ها در دقیقه ۵۰
🔹
استقلال ۰ - ۱ پرسپولیس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/686690" target="_blank">📅 20:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686689">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای نتانیاهو: ما می‌توانیم در هر لحظه به ایران حمله کنیم
🔹
نخست وزیر رژیم صهیونیستی در گفت و گو با شبکه ۱۵ اسرائیل ادعا کرد: ایران را تسلیم خواهیم کرد و این رژیم سرنگون خواهد شد و تمامی نهادهای ما برای تحقق این هدف تلاش می‌کنند.
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/686689" target="_blank">📅 20:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686688">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssgyEdl0H0k5M7nSoNrHLHxiwVRTTZz4XfOhp95bLLelIGMqGwOqAl-J0TPYnxPTthDTebksgcFOG4Ra103ttySLM9meqmOy2DwSQHw-_OOwQLgJFHUrzOdxYWkDz9rx3_w-KnEN5AWePxo5A7B2ipJyXa6S-9ivtyYddHK5j7kSfGf0IJoqQIYuBWtQ3r9n3VDEOOxg73CqZIh_cwJ-j23cJEerIerlejh5gRlBK_dBh7q0yZ_61a6TxqzakWAEqhp00L8z3yHnCjRf899iEfoTAe8EfK_dFxL2OF1Uo3uKbEjvuCm3C7lIQaFotk84a7IydzuptpnVpXYpXbvUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از کودک آسیب دیده در بمباران آمریکایی در سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686688" target="_blank">📅 20:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686687">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dfe005e97.mp4?token=feAEascx3MquQmM89bQcXSiQrRQAlIEB23RgEl9JJiTZ6BSQFWTrMsu5xSpHRHP8fwd-LLE5_pajJNZXT68Yhjl5jzqZ505Y2K92N4AR3rpSJEQHLp3_wLyRNMqid1gwdw_Z6oOeeI5axZXWnag3ydALPmH9glPf1udw5DnfRFCS5gWkFdz2A2CXq4NVzuDmqJrC-nbmDhmBPE9pkf8ESIHksYmXxqdU1tI2Hvs3goPLOFfMzSOeLPDtwE7R58IUS-lD6uMI-lIU90d5KhJ3Uqs_IYxcfyV-wU5HsrwOCSHYTj9p39SjXTVlcuspTSlrnDiCCoGeT7mhrhfHY4kUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dfe005e97.mp4?token=feAEascx3MquQmM89bQcXSiQrRQAlIEB23RgEl9JJiTZ6BSQFWTrMsu5xSpHRHP8fwd-LLE5_pajJNZXT68Yhjl5jzqZ505Y2K92N4AR3rpSJEQHLp3_wLyRNMqid1gwdw_Z6oOeeI5axZXWnag3ydALPmH9glPf1udw5DnfRFCS5gWkFdz2A2CXq4NVzuDmqJrC-nbmDhmBPE9pkf8ESIHksYmXxqdU1tI2Hvs3goPLOFfMzSOeLPDtwE7R58IUS-lD6uMI-lIU90d5KhJ3Uqs_IYxcfyV-wU5HsrwOCSHYTj9p39SjXTVlcuspTSlrnDiCCoGeT7mhrhfHY4kUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روبیو در دنیای خیالی خود تنگه هرمز را مین زدایی کرد:تنگه هرمز باز است
وزیر خارجه آمریکا:
🔹
ایران کنترل تنگه‌ها را از دست داده و تعداد زیادی مین در این مناطق کار گذاشته بود.
🔹
توانستیم این مین‌ها را با موفقیت نابود کنیم و به همین دلیل مسیرهای کشتیرانی اکنون بازتر و گسترده‌تر شده‌اند.
🔹
با این حال، آن‌ها همچنان به سمت اهداف مختلف شلیک می‌کنند و به کشتی‌ها نیز حمله می‌کنند.
🔹
تنگه‌ها همچنان باز خواهند ماند و تحت کنترل ایران قرار نخواهند گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/686687" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686686">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4dm6HnVa8w1KmYlb2QUW1Ai1aJXWlKd9vXzRPgCvB3ccTkxCkFteIs4YyWb527OM0omSgMIQ52N0F6T5lLfqu59JejKQxBwHx3eg0-Rmc2qqOJFwJPBhN1j9ESvryDLJBnlN9epRTL4zapBCo9iN0hMuJD0ImEI3TlMj3JuAWYBye-B7MBMzgGoMMVLg2rClNfgLYz-dqY5vPVGecw-Oz6IdLrq5thIaOnTChuEM3I3kXk9_gOxN_X_rU3FxbaVnRyWgHKded6dXpbjdJgrupCuDEUyJwyR8_84X2d-QpCxDWijngxzSO6dHcvul5b50mgfMoAfQ3AmByjX65AvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرانه تولید زباله الکترونیکی در جهان
🔹
بررسی آمارهای اتحادیه بین‌المللی مخابرات (ITU) نشان می‌دهد میانگین جهانی تولید زباله الکترونیکی ۷.۸ کیلوگرم به ازای هر نفر در سال است.
🔹
کشورهای مانند نروژ با ۲۶.۸، بریتانیا با ۲۴.۴ و سوئیس با ۲۳.۴ کیلوگرم بیشترین سرانه تولید پسماند الکترونیکی را ثبت کرده‌اند.
🔹
ایران با سرانه ۹.۳ کیلوگرم بالاتر از میانگین جهانی قرار دارد و این شاخص برای کشورهایی مانند هند ۲.۹ و افغانستان ۰.۸ کیلوگرم در پایین‌ترین سطح ثبت شده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686686" target="_blank">📅 20:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686685">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc154cab0.mp4?token=LJLmvDglYYY41SkNnop1d7w864HhHm-jwNow-RY_Z8FNKACAp8E_a8slDVtdBMHNOxnx2s_msG7seS3HhOxMWcS7CtF2ria0uLil4ucjqpakQ3WdvThBXvN9NocZyUDAuo4GiDZLwg2T6xZjMw6sXVIUyTAohaz0ONR5O-1yHku4SFDGxpATMoJZRVQ5Z6c6XV8JxhohmqepK02w7BTKqgHJvxd3msiO4h0OD-L7CiHhOTqyr_hn63v0DwdvKEVtOBaAPP-LeB8w_mmvsalKjB3s69hNmUKlfB1kZZI1HDQZP39zg97VHeAxcTrctQZc0HmEzcnzkQfyrEYxRdZLoYu6PkAUL0fyUaXE5ZyIwF6hLvWwFoB3O92U2cAMEgKPvnvjCgqDPGJx_xllfNF1EAn3n4MmyG5zHucjdsu7drLilM4qqPVVg-zlopf13Y8nmEg_ZNkn20Z7nmdpps5Cbim_plCeeLe_ReAGShZp0kGkNUd01Sz_P1egAnEk_Lbu6kqoHI8chdRkuR0cZzLMoqiDhsQ3pODwLwlS8O8piS-kZVrYU7TzB3TcCl_D-ovOdACUnX7L5eiMgHIBM1gVsTt0rEiO-k018nLp9k4PG12mNmqMKAA1_e7p1ef0U55h6JZFk1OBBhMouUv9aP51K3yx56AKON7ULwa5PMMZpKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc154cab0.mp4?token=LJLmvDglYYY41SkNnop1d7w864HhHm-jwNow-RY_Z8FNKACAp8E_a8slDVtdBMHNOxnx2s_msG7seS3HhOxMWcS7CtF2ria0uLil4ucjqpakQ3WdvThBXvN9NocZyUDAuo4GiDZLwg2T6xZjMw6sXVIUyTAohaz0ONR5O-1yHku4SFDGxpATMoJZRVQ5Z6c6XV8JxhohmqepK02w7BTKqgHJvxd3msiO4h0OD-L7CiHhOTqyr_hn63v0DwdvKEVtOBaAPP-LeB8w_mmvsalKjB3s69hNmUKlfB1kZZI1HDQZP39zg97VHeAxcTrctQZc0HmEzcnzkQfyrEYxRdZLoYu6PkAUL0fyUaXE5ZyIwF6hLvWwFoB3O92U2cAMEgKPvnvjCgqDPGJx_xllfNF1EAn3n4MmyG5zHucjdsu7drLilM4qqPVVg-zlopf13Y8nmEg_ZNkn20Z7nmdpps5Cbim_plCeeLe_ReAGShZp0kGkNUd01Sz_P1egAnEk_Lbu6kqoHI8chdRkuR0cZzLMoqiDhsQ3pODwLwlS8O8piS-kZVrYU7TzB3TcCl_D-ovOdACUnX7L5eiMgHIBM1gVsTt0rEiO-k018nLp9k4PG12mNmqMKAA1_e7p1ef0U55h6JZFk1OBBhMouUv9aP51K3yx56AKON7ULwa5PMMZpKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناو آبراهام لینکلن در پاتایا پهلو می‌گیرد
🔹
ناو هواپیمابر یواس‌اس آبراهام لینکلن با ۵ هزار ملوان و تفنگدار دریایی که بیش از ۲۰۰ روز را در دریا سپری کرده‌اند، روز چهارشنبه در پاتایای تایلند پهلو می‌گیرد. مقامات محلی ضمن تشدید برخورد با روسپی‌گری، برای جلوگیری…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686685" target="_blank">📅 20:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686682">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-HpZftrVrbYpL2kKkByydh7r0vqm6yOqekgH6DgL0TLT8yh-d9wPxh9Yjo0BWHv5BSCcBG1J-DYMnpjMq9XrQkGQgsepnLke3iV8dV_eXc06u33HO9Az9471Bbl8kycf5SVZhek1ShseuypErH7qTs6p0PHzzA50G1RPLpIcaN--y9_dVVMsW6JKHZAYu2w9wj2QLYt658ZfT8xUVlhZPcU7jyoxl3syvLJkLmdDffxapTgAWOxYiJbp2wj_ISMBd9GyJzQATnjMmSKyeRyN8W5XgwXU0p6D5BvQbB5Cct68r1W2pmgF3cIEIvAjZd0jz4YaJQI9FLzSNanwBxBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q79hM3uU-EPCelDR_k1xkP74VJACNVVLZWtFJ6Amuzqw8NSsJV05jSqz9smJhsxRrzHnA1G9sYNHNNjyQswr7vUpNlubFeLa0TQFaLoNlB_U7s42z0RMc8DaOxCecUrzDIQqIicdTnv42GGTjOm1dJ_8pmYx-SGKsV3rGN9tEOiiXMi-Nqz4GXa_6yl2ABRGmgcbiRI8lm39zlbcqVbD3ugsgzKzJhFToDo_DgOeBlqeusyHIW6t6pbw8VkZZUxnzq8X4k9WK8CfhyNao457IvqDHWEnxwTDhiwCkUrIKX9eLrrV-uFvJ5mLHZ5wick5E6zR9ubPbFCIfIKRrVtmVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nvccgM2nooyNJMn6wR9FRnxXMMbTcsr9F3Uwpnh-L3Rz7bPG8MKFfUkrRLFbP4UH6EIeD4-VPaeb7Oe3XwlOwDgqKXbeXjB3PjcuQyY2sPqh6yw7cWfNZKyToHshpSxWlrGdI-gWYdEjpXcxNlUN5Ndk-WkkC1viqyxIp3eaiBEk6YhuNGuhvUWpSWb8wV-QOAnCxuZH6jXuU1WzOy2i9uCRchcANjNzQfnj6bPmSQT2DkdM6RzVPLGsMowLrZVCQQMGIFqhcpXiZqbWbe7UcHaB9IBs-1JJzisIE__orAbJ8W61IHIaFm5gHaLoX_eISVfJAUAwVfRMhsyW_pO5RA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آثار یک موشک کروز هواپایه AGM-84H SLAM-ER متعلق به ایالات متحده که در حمله به مراسم عروسی در منطقه کوهستک استفاده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/686682" target="_blank">📅 20:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686681">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_4QgqV-kXVb3EbAnvee0FtG_eancYS2ez1KKPeUN9_qilre4eyyvATFUKCUbUKOPMslkLkd_MvWkNMGebN2edWzSrhH_hKnJjSdwalmYoc0Lx4ckcogdKTD15o0vHuSQF_uPxKot7UZKHl7dVcZGVJDJle-0gzPDdhR_iIpz5Y4lmYD2e-jccNVyGZaBwLsBMDDk3xBA_Jx_DirBVsqtyVZ9NIaQjEsMowtUXc_EHvHUGks87zh1SuMlcr17ufeujqVzAOTiy1w5r8Ab3PjG0MHhRPtCIi8lvVAZ4MjL3M0YVzertP7QXJ7rFVWBxkjRRf_L-UjXAxrLZcKEoE_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توسعه مشارکت راهبردی ایرانسل و بهزیستی با پویش «همه حاضر»
🔹
مدیرعامل ایرانسل در آیین افتتاح پویش «همه حاضر» بیان کرد: چتر کشف استعداد، باید در دورترین روستاها و نقاط عشایری کشور گسترده شود.
🔹
ایرانسل، در ادامه همکاری‌های راهبردی با سازمان بهزیستی کشور و با هدف حمایت از عدالت آموزشی و فراهم‌سازی فرصت برابر تحصیل، به عنوان تنها حامی، در پویش ملی «همه حاضر» مشارکت کرد.
🔹
آیین افتتاح این پویش، ۱۱ شهریور، با حضور معاون وزیر و رئیس سازمان بهزیستی کشور و معاونان وی، مدیرعامل و جمعی از مدیران ایرانسل، مدیران سازمان‌های مردم‌نهاد، خبرنگاران و جمعی از دانش‌آموزان نخبه تحت پوشش بهزیستی، در ساختمان مرکزی سازمان بهزیستی کشور برگزار شد.
🔹
رئیس سازمان بهزیستی کشور با اشاره به همکاری‌های مشترک با ایرانسل، از جمله اجرای طرح «دانستان» و غربالگری سلامت روان، ابراز امیدواری کرد پویش «همه حاضر» با حضور ایرانسل، منجر به افزایش مشارکت مردم در حمایت از دانش‌آموزان تحت پوشش بهزیستی شود.
🔹
پویش «همه حاضر» تا ۱۵ مهر برگزار می‌شود و مشارکت در آن از طریق کد *123# امکان‌پذیر است.
👈
جزئیات بیشتر
📷
مشاهده گزارش تصویری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/686681" target="_blank">📅 20:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromعلیرضا زادبر</strong></div>
<div class="tg-text">اینکه ترامپ دعوتنامه آشوب خیابانی می‌دهد از سر ابتکار عمل نیست. او به مکمل خیابان نیاز دارد. او به راه انداختن جنگ شهری در ایران محتاج است.
محاصره دریایی، محدودیت در واردات کالا اساسی و تهدید یک ملت تاریخی به انتخاب دوگانه تسلیم یا گرسنگی کشیدن، جدال در رهایی از تنگه هرمز، همه و همه بدون به خیابان کشاندن مردم ایران برای ترامپ هیج است.
مردم از امشب خیابان را بیش از شش ماه قبل تسخیر می‌کنند تا این "خلاصه اشرار عالم" ادب شود.
#علیرضا_زادبر</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/686680" target="_blank">📅 20:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686679">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fe8455fc.mp4?token=sUvWAV2cREmqwlS_JVPtAWtkFRk7i0ac_-6pSPih9IuxrUWk9MvMlypCQnJJCdje7TLGRf6tQ4UqFOSpu6wl9nWmAb0hsMsTz_XlpWKwdy_gbdfe8QjXuT0bI490D9xo338UYlE0kg8nHaq7qjKmX_gKlqKmk9sqSqEygH_2eswqFy9QV2UBi6Iv39ZhYZuOFtHDCHCS-Aj8n662DgRMkkKJhDHgX6FtviiyD7cZSj-Gl9fqmypW2x2WfcN5gIkp8ZP0muxLBRx9GuiZDfNvyjSRr3PCzWELw4rQKewx_Ch2QbpxlUYc_HsqQuu63dMm6e8VkBi8lCAXyZs5AKaVtYQQUvV3-Q5OTYXAPE5dGYk1rdSp0bPqpQCZZK7ROjD69vtPs76e5kB5R-5sNr9Di22cTpgmUcEo8C21EipxFeM6Rf6HfdHyCZ3RF_kpCYATwG2Kp5wwwVJ6EdyeCK7GeoWtrM1ogYv_y59CT8H8AoPsceO0khaGeiGoHktNAzjMl21GI6n8O65QSd_m4cDwLCdJdU0vueiKD9m1AWk8mrktQ02BLZJIj-OF83Fjx7kbbfjS4fnEBvcFDIRzuVG_ZS4NXTZe_q37TU4JopjmryjPH6NKKRYY-7AaWVfMW4kzBsws89YEXx-sU5Sby8H38fRn2mYtGRDpKfMOh3sNMKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fe8455fc.mp4?token=sUvWAV2cREmqwlS_JVPtAWtkFRk7i0ac_-6pSPih9IuxrUWk9MvMlypCQnJJCdje7TLGRf6tQ4UqFOSpu6wl9nWmAb0hsMsTz_XlpWKwdy_gbdfe8QjXuT0bI490D9xo338UYlE0kg8nHaq7qjKmX_gKlqKmk9sqSqEygH_2eswqFy9QV2UBi6Iv39ZhYZuOFtHDCHCS-Aj8n662DgRMkkKJhDHgX6FtviiyD7cZSj-Gl9fqmypW2x2WfcN5gIkp8ZP0muxLBRx9GuiZDfNvyjSRr3PCzWELw4rQKewx_Ch2QbpxlUYc_HsqQuu63dMm6e8VkBi8lCAXyZs5AKaVtYQQUvV3-Q5OTYXAPE5dGYk1rdSp0bPqpQCZZK7ROjD69vtPs76e5kB5R-5sNr9Di22cTpgmUcEo8C21EipxFeM6Rf6HfdHyCZ3RF_kpCYATwG2Kp5wwwVJ6EdyeCK7GeoWtrM1ogYv_y59CT8H8AoPsceO0khaGeiGoHktNAzjMl21GI6n8O65QSd_m4cDwLCdJdU0vueiKD9m1AWk8mrktQ02BLZJIj-OF83Fjx7kbbfjS4fnEBvcFDIRzuVG_ZS4NXTZe_q37TU4JopjmryjPH6NKKRYY-7AaWVfMW4kzBsws89YEXx-sU5Sby8H38fRn2mYtGRDpKfMOh3sNMKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار سازمان ملل درباره آب شدن جهان!
امینه محمد، معاون دبیرکل سازمان ملل:
🔹
رهبران اقتصادهای برتر جهان باید روی یک جزیره مرجانی اقیانوس آرام بایستند تا واقعیت افزایش سطح دریا را ببینند. افزایش سطح دریاها در اقیانوس آرام روی دیگر این داستان است و گرمایش منجر به آب شدن سریع یخ‌ها در جهان شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/686679" target="_blank">📅 20:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686678">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6730a56a0e.mp4?token=P1_ScNeyef3_4LZ5My-xzwN0Hw70-T3AO46sUPBAqkLBGvpPBKyd811cdGZKeE3e-J1A3QfnUn6LgN6FWiG9TF186tll-zQufOSg3YwAUIIkKFd_oA9EQ1ChqpM_IXb0HkF95HO-vz1sayRznd3NKGI3iR42IRZ_SyNW5wsrehyj7CEt5ZotP_UH78mO-jnh0o6lB3CeQQVTUEGuIQ9crfMsu4p4f3smQtj-emmC8j36DggdtpZd4KnSKaEhYNMB_MzynhYlceQF71_5F7SrF-AJs9hIW35D6-RGutFbWwKBI97rqrkHKdH-hPeY38_eHOiafT1tztBVbqnbL1syXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6730a56a0e.mp4?token=P1_ScNeyef3_4LZ5My-xzwN0Hw70-T3AO46sUPBAqkLBGvpPBKyd811cdGZKeE3e-J1A3QfnUn6LgN6FWiG9TF186tll-zQufOSg3YwAUIIkKFd_oA9EQ1ChqpM_IXb0HkF95HO-vz1sayRznd3NKGI3iR42IRZ_SyNW5wsrehyj7CEt5ZotP_UH78mO-jnh0o6lB3CeQQVTUEGuIQ9crfMsu4p4f3smQtj-emmC8j36DggdtpZd4KnSKaEhYNMB_MzynhYlceQF71_5F7SrF-AJs9hIW35D6-RGutFbWwKBI97rqrkHKdH-hPeY38_eHOiafT1tztBVbqnbL1syXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی یه نکته‌ کوچیک، کلی دردسر رو کم می‌کنه!
👀
این چندتا ترفند رو یه‌جا داشته باش  #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/686678" target="_blank">📅 20:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686677">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
وزیر بهداشت: در حملات شب گذشته به استان‌های مختلف کشور ۱۸ تن شهید و ۱۰۸ تن از هموطنانمان مجروح شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/686677" target="_blank">📅 19:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686676">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkspnN2SLL6wLCKnY7hRo1WHKK7bsFugQjQId5TIyMgaI_K7fl_OM8dC7HOY9KVDSz_vzEhoud4wqWjtnwV346LIIuu2hxouu75EjWu5AG4XeWGdVUOcBvffJNEXhN96sH28uQVaHNHNHd3lFW85TSuiimOd7DVu3jvXz4kxUuHpzLsTBx_5uGv5Z6eVsxFm14FreWXPPT2-PUmFgYLaGcbYQ66FlvDBA-x5SC2rBaGYfZhLASdjoFbkuIG4Yo94ag2U2BfqCEo7Ss-SZoE0WkIoXZprO6GJvOV_AY_ANXsuwor-k5w4E4FlM05hQ8pVbWj-aWHBZRyKiw-OyrBnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همراه اول بازیگر اول بازار ارتباطات هوشمند کشور
🔹
بازار ارتباطات ماشین ‌به‌ ماشین به یکی از بخش‌های رو به رشد اکوسیستم ارتباطی کشور تبدیل شده است. این بازار از کنتورهای هوشمند و کارت‌خوان‌ها تا سامانه‌های ردیابی خودرو و تجهیزات صنعتی را دربر می‌گیرد.
🔹
به گزارش اقتصاد آنلاین، تازه‌ترین آمار فصلنامه بهار ۱۴۰۵ سازمان تنظیم مقررات و ارتباطات رادیویی نشان می‌دهد همراه اول با سهم ۷۱.۵۱ درصدی، جایگاه نخست این بازار را در اختیار دارد.
🔹
در این بازار، ایرانسل با سهم ۲۸.۲۹ درصدی در رتبه دوم قرار دارد و سهم رایتل نیز ۰.۲ درصد اعلام شده است./ اقتصادآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/686676" target="_blank">📅 19:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686675">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f262048d3f.mp4?token=RvLxaEA85GYdjKsPcukW17u217IMGh04inVh-_s4SI-VJeOHBzAb-8cggEPlvIgtLe8ENmeqYFAtC3o4A4DyZ3CaBIa_rXPPyZ3w4YNe762HbLDDLb9sbYv3r9YVeVBG_swIEVNZC0z27Zk-mDwwetyhyDuIuBEyLy79v9Ohmvs_A00nzuGrPi-AXPLD-neTxz5lbbQ1tZS3bjioM_UOJcdk4-A4KPE_V7B5e_H5dnQULwGBUqWVp5fbLWF3_c-nSCfONN6ASBX08jIWJXoRU-9Gu_f7DFttyV6dyJwT7Ip95UwbzbPodalnvWbXlPa9SH0ELCGSgnOnG7-MAUeuFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f262048d3f.mp4?token=RvLxaEA85GYdjKsPcukW17u217IMGh04inVh-_s4SI-VJeOHBzAb-8cggEPlvIgtLe8ENmeqYFAtC3o4A4DyZ3CaBIa_rXPPyZ3w4YNe762HbLDDLb9sbYv3r9YVeVBG_swIEVNZC0z27Zk-mDwwetyhyDuIuBEyLy79v9Ohmvs_A00nzuGrPi-AXPLD-neTxz5lbbQ1tZS3bjioM_UOJcdk4-A4KPE_V7B5e_H5dnQULwGBUqWVp5fbLWF3_c-nSCfONN6ASBX08jIWJXoRU-9Gu_f7DFttyV6dyJwT7Ip95UwbzbPodalnvWbXlPa9SH0ELCGSgnOnG7-MAUeuFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلاب سهمگین در تگزاس آمریکا خیابان‌ها و منازل را غرق کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/686675" target="_blank">📅 19:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686674">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e9fee4971.mp4?token=fD9IOC--ZIrS-A8UwuYHN0varonJ3txC_C7EOgOAnrFBlX9gXW7lm0Osj4x64kao1Mx_7xEPJicLUbs37TG0DgPXEqP2MidcKhTgfdUv-L4Rig8o1yyJowV6Cq4kZxBRBuTkxvsV8mp9yDcQluFJc_Xa_3FWyerhpohWG2pKzbRZimYKQOfncH1SD8oN2CsyWd-qTiLhT0mE-RxNpDH2whxAqQBWZ-NYnAdHQ62w_ydUWK_JEmIxnIIoQgdM-CQ047ZnuZw6Me1PLDtUFwp7TbCZAbZepGWfn_gNyD4juGwrIJjtEwHLgLZv3ZIVzdPLIe4HCSBA--wCOZo7Dzz_2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e9fee4971.mp4?token=fD9IOC--ZIrS-A8UwuYHN0varonJ3txC_C7EOgOAnrFBlX9gXW7lm0Osj4x64kao1Mx_7xEPJicLUbs37TG0DgPXEqP2MidcKhTgfdUv-L4Rig8o1yyJowV6Cq4kZxBRBuTkxvsV8mp9yDcQluFJc_Xa_3FWyerhpohWG2pKzbRZimYKQOfncH1SD8oN2CsyWd-qTiLhT0mE-RxNpDH2whxAqQBWZ-NYnAdHQ62w_ydUWK_JEmIxnIIoQgdM-CQ047ZnuZw6Me1PLDtUFwp7TbCZAbZepGWfn_gNyD4juGwrIJjtEwHLgLZv3ZIVzdPLIe4HCSBA--wCOZo7Dzz_2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از دقیقه یک بطری انداختن شروع شد
🔹
طرفداران استقلال هنگام کرنر زدن بیفوما شروع به پرتاب بطری کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/686674" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686673">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/686673" target="_blank">📅 19:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686663">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaNL5keODMjwVN-PnWxOjtYoaTShcpS0ImV5rcv1O6fKNPJHR9lJVqijRZFQoltAjva57J_Okuob65d2jGuFgiPXvSzU09y7DenveeJ5PCo88Ir9jTkHiNSYu5mw1LP_GpoK8mNHR4hgu_kJu1SDx-UxgBPdsTogrBvga9qR5p02UMVmOgRjkblUBlomrAWDxaWNVJY4yYW-ilLfOjU7zeiv_D1_hyqL1OCkTUy0xsQ2gZT6nAQt10I1-Su2FIe2nXKwLqzuG9VvMfJZSEniseYZQrHuHOwVeW_lxTVS7HlE_Cd-z60u1k6h9ppeYUq3ROqpE6hw8OusjhqSKQTJ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIvn2fDsna-BnI8O7pg3swxNHyYcJsjyIE1zPNzzL73FqnocWLpwsxBgMSWN1uFIlNS34g8ym20-NmLmCP6YRNj-DeajequJlNOctAnXUZ_4-igGrJpgXJFUGQ_VwfCx_PztXBaNK1MhJAtSzsPu2W8QpKXKjnpZ75JjWbdKJ7pg7hEWltzPWBIs7PkxY2HLZSaTuhvfBC8sDFY7Is6C0Jo4CSBHt5yxSYdO4-Qbh38tvZEwwas7teCeRhbe1fj7DmX-IwUMlofj2AaGMYhyGVcHRB5Zop1W-F5_uoVKPfgK6gyI5idA4I0IsCVRJmeR635YEpJsct4smTRRbkOxxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkYQ0ISjsY6_yqjpeL2VNiEyZgyDC0FcrOpx5vQXL4IElys5WFG2dzEHxzo1ZwyHNukgubeM7LiCFptp9t2l2IQztzYy_1qPKcKgAfidtw-XPqiOmscEUeQiCbBuzxVhtHNr-02dE_wKeqlEU92RisQxwj1aFpVx_j0RHy6JhV7VNKnS6K8TwpyIB6DPIlvhUMbJsXzLXcDPz5GM0v8gwFXFgfF5koe6g5uFvkf5U55FrL6PrUsIrTIB7Kw1bIOdZhmkNVnvjNit6GfVTzsxdhs30aOGeE900u-aHTodkQDJEYuGLWET3tu8Elb_QuG7XqxF-JiNHYdbb4zmLx1b9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hwNYYXVrYdexTqx6w50ytQYSu2DD-Tx-lxaHcrXdwJ-h43v1BQfXeM8aFhhMgO3K0PxkcfIiWepyCZ3vcuk42jYmycxz6vWhyg0Rjby4DsG4aQnd-V-SrAKrIx_JSOnVnr4d44LNhwlULhVgRRyNyc3qmrhaCMZsw21Cls-Lzp4MJK9J6jV0ipL59cOvoOP5MTUAcpWustEK-bHosnsmuZfWF4WLYUisU98aphtDGeQAB1Xc_VOFNqjObpktfZ957VynTcaeJPKZ27qGMaPmN6J55M0-neehPgCc9A8DOUwVGBTBWYPP6qCVo3MBeUCIPeFYhj6jjX5bGmaH3uxGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HwQbhgvniKmkYqotzGhduMjOGaeZXFyULwd2gTE6q19ATRnWfZnKvqGjjgVN7ZhE5kbvBCWtcHvtCeL0LG1JvfrgFvXchWdqyCyakn6JMCyQyhDfMEYwE_F3EFGcHoz2bjCeIVMA9_20nRMB3mHNnG8ExbJg2jHsDjpMOiDDCzOBl7H_Jrts1hkEMg7NYYzW_--s0phejlHZxRGxOu6gFyn4RKL4Ea7EYmefuPPvp4r3OdyueiXU6aqc6uWOXhrqXrst41MpDsdma4NpzYPdcfYbIQ3sK3CQIG03Kb2uoLkE2-TgLU6fFWN0OYhnOLobglCkczmbH-4oTcxhqziu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QASivp7yqGm90UYEtOQg911Lndu4p7oz-srufjWQeipPwc3DqHmLjWfVoiD8gu6zerRC6dJiAtESPfVGVEt5_9Ub1OmnVJdUPAo2P0wS3aryZYgZ88D82qqsOQHm2xXyb4yMfyrN01ZyHp3-9g_Wwn7U3JdX7OPJY1SFHx-_UPvmqbtfsQhm_SNVMJU1StmYrgFApJ6bvk7qcuFlhUGUWC-NK2rL5TFxpInG0RBKeF3GSlzUj_oNwFcsX2Cqscpj26ERZsrCkMOgGa7v3i69Om11fcnA10OQ01mGldV3p8RPcqzS21ruGuXMcaJl_9ygBTgcO64pJZsZ9kPNGce8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dG0UCxocBVoqdsXGjzKkb7gf5P1Oj5RGXaEs_cWo2s-KyWDKd2a6A3Zfc4LS8ZMS_Bc8Yq2-PxlzMJu5fnxNyNYp6ikNIm_2FkSUPSgGVg3c1-bW4yCJ_V_P5484TfBJV_eP8CGs2qPUovyvvCOpuJSxzyiWJDPL9r8mNbbOp3VKCetZei_HrDaII9QsCWlPMOx7XLbTmnL_DrTRsHtoevaQDcIG2TrUvs6jofRT0zbyETPX_RItnRAaP4C-SmmVH2rT1_ZQ7F46IKDj63x4DEfH9I9914m3OF7j2ofNhHShNY_XeShEcLXcDNjeni2cRL9jsyhD0b0wNSC5G_W5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPr98t0PhE4okUDkMXRaNbTXITDFhZqIqDMm7Sa5yjgRbeI1DjpjzOh7iYO94jt9JlE_Bs7l3iNtwFlsct74-7KzboCPC3jF696BoJNGCwIOqikUf9tNtIaNRVMQ1bmamIeKge2h4LgnTZzaR_ZB_EFl9aUFGHvcJOvRD9ZEY5P_dohGtSLwo9IDezXP1cnkcuEZYgFFIvoGNAoJfASnHArebHccTIQvL_BUUuLoxprOHc0Mlup7TV8BoUikGBTv731IcduFLtjfqL3WQ6V76lF_jwv-0NxRr2MjlFHu-3eRer5KwhXPyMAY6wzOGd2uPix6jao5a59i0obSXNQhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrElHxjzV5XGUQxlhyBGY5viVcvcL6VEOCQVw58VOZoqo8opkhGbePETLYFZw_Lh3CgMLiPC1zFm3CID5RTePS9kDqjNr-PFjb-m6sxNPx-6pEmIHOPujQwvxmVYSYRw2z2Byglg1VpGekQaceTcwyv2z2VMW6bLSlXnE80oN2KTLzZORWn9E5p4xiTDCuS75V7KKo-5lCtYYnyRJJB6Q7lVCCSRMMAPA3Cs7RKquNJq6a85efzL6fkE0BrlxO3gbPIXVORDMWeIg939INJEZ46CGra5Z_hW09pvnJXGH4Yy-cAlVHrWXpQgKj1g5RfrZAiM3nptPLH_QCN1lNljNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKZZH-ODwVhthjVAXGAUsuDN-CwT4YpSwdnJ8gSny5a4BwGw-NsBLvGSPjfn9Izu9oinxNzVprxrSIKrE8XN8NgTYu00Caz5-YEOW7QT60ZdyJX_rhbJGF3D9WMzkMYKefzDIlB0w9-WfGRSVluVooQVotsMtbebOJbeCxJGQYmA0L54gJ3Ny0PEOUsY_O6La1KPLjpFHnGdqaVFveBAFoS4bLu8BG1bgijBMPSSzY6o98uzYFHO_zHfELcRq5Ndv-lJ6JnP94SJ3hNo4SsINJ6QRzf8HInyKSfm7Es5_Bodob8uvPk_gev0p37oU_XtjIjY9gxHcF4P-w2YsRl7iQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
بازدید مدیرعامل بانک صادرات ایران از نمایشگاه الکامپ/ رونمایی از محصولات نوآورانه توسط افشین خانی
🔹
مدیرعامل بانک صادرات ایران با حضور در ۳۸ امین نمایشگاه بین‌المللی الکامپ به بررسی آخرین دستاوردهای حوزه تجارت الکترونیک و فناوری‌های هوشمند پرداخت و از ۲ محصول نوآورانه این بانک نیز رونمایی کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#الکامپ
#اخبار_سایت
#بانکداری_هوشمند
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/686663" target="_blank">📅 19:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686662">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xvlfv5VMsyKfJHBKaFZe6KiobAmsmBAlC-1hxoMtePgn1ag0CgNkVg37dUvaYYhbJdlWcFgllLywBCpYuexA3Ek8pypSb6Xl9CTX8smLhLpge9YzwS5MdISmQhFXGeMrN7vRbvbS9udVNSXSoOat1wPcvpQAM9z5DKarkZYznHc_EoOSsSgJUNDrXF0Mjp5lkv_yOfztZ0X2hFs2GR-gnOgtWT91bSgwL4GKjNIH-ijyznnVY0_R6P-unJXrPHrQ1S38qaoEjRJ3RUjwaRu0VZke09GQjp7q7oOhZmiiAxxtkK691Ix4xYJXJm4pG3295QBrue3BAi0EgGL7hMSIbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۱ نشانه‌ای که متخصصان می‌گویند نباید نادیده بگیرید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/686662" target="_blank">📅 19:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686661">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP0DTlKm0eR380VycBg7oIpX2NBo8Udn4quRBGJgmwUeNZFbmY1tkgYgJLCRde7CzFQeto6z4ovijgnXXjQOJkcIhrywjgS7dmVQgGBOi1pnnMiPFKzxyu7oAfR9H6Qxfm4jCB-Ui6YckG41BkCKH-LBx-Dbia9oVucW_Smh9cS3K09hqMEgEqOJDjcSs1RoDphHHoJMhkDDo7g_NFJ99DcTQYU0TeePf0j-QjeVhGA6TXMB_ocYlL-Gtv24z6cyBEEBAIwbgLDEx1savDT-jakpVT75i3YndvBvOiK5RKzJuLZDVnALCp8aig1DZLDc88y38zvhWPxMKO2grxU49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محصولات ایران خودرو باز هم گران شد
🔹
هنوز ۳ ماه از افزایش قیمت محصولات ایران خودرو نگذشته که قیمت مصرف‌کننده محصولات این شرکت باز هم افزایش یافت.
🔹
خودروهایی که از تاریخ ۲۲ اردیبهشت ۱۴۰۵ به بعد پذیرش شده‌اند، گران می‌شوند و ایران‌خودرو می‌گوید بدون پرداخت مابه‌التفاوت، فاکتور و تخصیص پلاک برای مشتریان انجام نمی‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/686661" target="_blank">📅 19:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686660">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32586f319.mp4?token=UunHrSe-pyzGvqAZW-SSWBtCHwH6WWNiZfwWFR3ihFuakcqIL1y-PJ9jyKKDC2H7dhR2gTAO6w8UaCUz0_zm22Rm66zPqUa2Ezq-1SxzIjVUd632emDgRe2KI6NhXamdZP2cSlcq5pRKZ3SVTy2jzze8SCGTCxtPEvsIc3matQnfmzZ0fo1dXk5iPkLTCxm88p0re1GdGOaB3ms-UkhIImnzyUnxxfUjWUGgxAMqboqgyi8pMA2bXHa-kmAcHJSaQz1AVrxcR-zT6LcOmgb_1gErpfKQk6GQO26IllPtvFGx0myDQdrEpGSQmio0YYUpEBFm9LhAeCV8EcAWWAe9uKZQGa_sVxfYzTdxWuZaI3-V4xZ_czEzc0HT7QkuVcZBd2OWHfGi05z7KKYk7mCMzKGOWdNwqao8lpS6UCMFZyZAUehmzI2MKnNGogUjszv-6Lgs7O96VqqqqFVpfmvpBwG3H9Mw4aUOClmYBtF5rLDm1vwIzW9qZ67QQXFdJ4r-u4l5FvZuj2bXNo2q61onbOX6zK-931NvU20Hx_A_dXDUwHBkXMFZgjmPWY2dJSisYFmypvEM4B-uFUfpknXV3fi8nvR1PxpwSYqbdiRlgMKWBFqpDvsWYr714EdEZZDOUdTJG6KUomrVX22-Nf5RMZbXTfO_G2nEKyL02TjGt-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32586f319.mp4?token=UunHrSe-pyzGvqAZW-SSWBtCHwH6WWNiZfwWFR3ihFuakcqIL1y-PJ9jyKKDC2H7dhR2gTAO6w8UaCUz0_zm22Rm66zPqUa2Ezq-1SxzIjVUd632emDgRe2KI6NhXamdZP2cSlcq5pRKZ3SVTy2jzze8SCGTCxtPEvsIc3matQnfmzZ0fo1dXk5iPkLTCxm88p0re1GdGOaB3ms-UkhIImnzyUnxxfUjWUGgxAMqboqgyi8pMA2bXHa-kmAcHJSaQz1AVrxcR-zT6LcOmgb_1gErpfKQk6GQO26IllPtvFGx0myDQdrEpGSQmio0YYUpEBFm9LhAeCV8EcAWWAe9uKZQGa_sVxfYzTdxWuZaI3-V4xZ_czEzc0HT7QkuVcZBd2OWHfGi05z7KKYk7mCMzKGOWdNwqao8lpS6UCMFZyZAUehmzI2MKnNGogUjszv-6Lgs7O96VqqqqFVpfmvpBwG3H9Mw4aUOClmYBtF5rLDm1vwIzW9qZ67QQXFdJ4r-u4l5FvZuj2bXNo2q61onbOX6zK-931NvU20Hx_A_dXDUwHBkXMFZgjmPWY2dJSisYFmypvEM4B-uFUfpknXV3fi8nvR1PxpwSYqbdiRlgMKWBFqpDvsWYr714EdEZZDOUdTJG6KUomrVX22-Nf5RMZbXTfO_G2nEKyL02TjGt-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیحات نائب رئیس مجلس درباره نامه دبیر وقت شعام درخصوص ابلاغ قانون حجاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/686660" target="_blank">📅 19:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686659">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a5a3e74f.mp4?token=NhPjjDtEz-kIDFqRwPFszKfKfz7VbkukAmCztyiVVcNHEABZbWSn3q1EOmP5ShpJPZDG-n207riuGUjYKDTs_a1QCyD3veUEMuJ6huhes7za65Dzz8xr46cyNP8DkC4_j3vI9RXk-FdeklgKRUtMvDcA3iHig_J_rjvNDNC5njphnWsUD920xWjg-HmnGxyT8AQhPCMpYmkeJ4ghKF3axKQCRx75fotmrXnWVNdHrU7KzWmCnDFfY7xKXkwIgMuDJHA9ayc4oFPopksQRPLeBYue5aKHIcRwivig3amUOGokomamqk8omzVvaYQvT6zvlMpKwYW91uPJllMMmPjdvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a5a3e74f.mp4?token=NhPjjDtEz-kIDFqRwPFszKfKfz7VbkukAmCztyiVVcNHEABZbWSn3q1EOmP5ShpJPZDG-n207riuGUjYKDTs_a1QCyD3veUEMuJ6huhes7za65Dzz8xr46cyNP8DkC4_j3vI9RXk-FdeklgKRUtMvDcA3iHig_J_rjvNDNC5njphnWsUD920xWjg-HmnGxyT8AQhPCMpYmkeJ4ghKF3axKQCRx75fotmrXnWVNdHrU7KzWmCnDFfY7xKXkwIgMuDJHA9ayc4oFPopksQRPLeBYue5aKHIcRwivig3amUOGokomamqk8omzVvaYQvT6zvlMpKwYW91uPJllMMmPjdvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک: رژیم صهیونیستی حملات خود به جنوب لبنان و منطقه علی‌الطاهر را با شدت بالا ادامه می‌دهد
🔹
از بمب‌های ممنوعه فسفری تا انفجارهای مهندسی‌شده در روستاهای جنوب رودخانه لیتانی.
🔹
هدف دشمن، اشغال منطقه علی‌الطاهر و ایجاد منطقه‌ای ایزوله با از بین بردن امکان زندگی در این مناطق است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/686659" target="_blank">📅 19:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686657">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کرونا صعودی شد
قباد مرادی، رئیس مرکز بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
بر اساس داده‌های نظام دیده‌بانی عفونت‌های تنفسی کشور طی هفته اخیر موارد مثبت کووید-۱۹ افزایش یافته و ۸.۳ درصد از افراد دارای علائم عفونت‌های تنفسی، به کووید-۱۹ مبتلا بوده‌اند.
🔹
همچنین ۵.۵ درصد از این افراد از نظر آنفلوانزا مثبت گزارش شده‌اند که هر دو میزان، در مقایسه با هفته‌های گذشته افزایش داشته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/686657" target="_blank">📅 19:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686656">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5338e0f8d0.mp4?token=rPYyM7qSWSB7BBmQyZo12g2ZSnboZ-k4yyhSCJAiJuSCRYxVwBP2MvMpCUr6vilVg-UUPOr_FUNh8txM_DRzIdHzFxZb7Npua5vWCTGzqzyinlYb6E31yPHSI7jPMDabcf9F7PDmfLhKoIyKCAC7-eRBgdhsHQszH5ewEb8ugh2wyUp-MGDQ5r7IZttaXrpGqS5KAIyYf5Be9Y1TI3BKa6UiS20bJzC7xAnYYVAUw2OtXlvNYFZz7p-cMm4FsKYJD4-WKoopHvoB7uLy-GW92utJLIkfriGLkHcnr7wwgKJo-x41lDoVyaDG9oEUYRUtdiJuZsc0mNBmkZK_7Q1lnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5338e0f8d0.mp4?token=rPYyM7qSWSB7BBmQyZo12g2ZSnboZ-k4yyhSCJAiJuSCRYxVwBP2MvMpCUr6vilVg-UUPOr_FUNh8txM_DRzIdHzFxZb7Npua5vWCTGzqzyinlYb6E31yPHSI7jPMDabcf9F7PDmfLhKoIyKCAC7-eRBgdhsHQszH5ewEb8ugh2wyUp-MGDQ5r7IZttaXrpGqS5KAIyYf5Be9Y1TI3BKa6UiS20bJzC7xAnYYVAUw2OtXlvNYFZz7p-cMm4FsKYJD4-WKoopHvoB7uLy-GW92utJLIkfriGLkHcnr7wwgKJo-x41lDoVyaDG9oEUYRUtdiJuZsc0mNBmkZK_7Q1lnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش عالی هوشمند روی ریل فناوری؛ تفاهم وزارت علوم و سازمان فناوری اطلاعات در الکامپ
وزارت علوم و سازمان فناوری اطلاعات در الکامپ ۲۹ برای
توسعه خدمات و
زیرساخت‌های هوشمند و الکترونیکی آموزش عالی
تفاهم کردند؛ همکاری‌ای که قرار است زمینه اجرای پروژه‌های عملیاتی و توسعه زیرساخت‌های فناوری آموزشی کشور را فراهم کند.
📍
سالن ۲۷ | پاویون دولت هوشمند</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/686656" target="_blank">📅 19:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686655">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سرمایه‌گذاری ۱ میلیارد دلاری دات‌وان!
🔹
رئیس و استراتژیست ارشد گروه ارزش‌آفرینی دات‌وان: طی ۱۵ ماه گذشته ۲۷ شرکت در این مجموعه ایجاد شده و تمرکز اصلی دات‌وان بر آماده‌سازی زیرساخت‌هایی است که بتواند زمینه فعالیت و رشد کسب‌وکارهای جدید را فراهم کند.
🔹
بابک زنجانی افزود: طی ماه گذشته نزدیک به یک میلیارد دلار سرمایه‌گذاری در مجموعه دات‌وان انجام شده و این مجموعه معتقد است باید به‌طور جدی روی لجستیک، فناوری و رسانه کار شود؛ چراکه این حوزه‌ها می‌توانند به حل بخشی از مشکلات کشور کمک کنند.
🔹
مشروح این خبر را در سایت خبرفوری بخوانید:
https://www.khabarfoori.com/fa/tiny/news-3242267</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686655" target="_blank">📅 19:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686654">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxSvQp3-XVg8qem8_hyiuUVxJS17P32Oyp2BV2lQ6UcIp_HhUJbo4zFFyioIB5YgPYvHKYX5FpH5tdjFry5UcQjdArzX1rUaDSjDHqGhAu7NT_yfI-UrafkjGf1A8rVfN1DZwRC4FU_envS21Vnw1w-OOS8ggmW1xPwJSx1gm2De7Av8IBvHp5Gbl8TFZ4APUpwub2y7xdCqYmvRZJRNVdIDKv-ayYFru0dA3NPQS99zPZ2rZsvZRuxr8rYabfgCZ2PBPbPpcRab5AneL2Gwy2jOP3jLoH9xNVpuk172XirvIb7FdffQdVXkB5y73NBcGM8YYcUlgJSUME4hH07zTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم: حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به تنگه ترامپ تغییر دهیم؟؟؟ مثل خود آمریکا، «داغ‌تر» از همیشه خواهد شد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/686654" target="_blank">📅 19:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686651">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قوه قضاییه: صدور حکم اعدام برای احسان خدادادی کذب است.
🔹
زمان ثبت‌نام آزمون وکالت از ۳۰ شهریور تا ۵ مهر ماه و تاریخ برگزاری آزمون، روز جمعه ۲۰ آذرماه ۱۴۰۵ خواهد بود.
🔹
آموزش و پرورش: معوقات فرهنگیان بازنشسته پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686651" target="_blank">📅 19:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686648">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4d3da04bc.mp4?token=B5CTTSRWa4-PLVSe-_k4TEhUWs47t3sjE-Xi0QcLIUGmcY3Ba-xSyggcSrWfhkqJEFzLeK6bdPpMbihjfqS4qk-h2geMmfvrtNiTDwMNjcuemgvJCuV4A_1COF_sONftTfaLdi_vB0_ZOm0_5ZkYbNtmg5FiPY9V994yZ9ZJXgfu8_su6H2a5cihlnz7RwNbjnROpNJlb38sgePks2J2HoFKd4leg9o-9m16o1aUIE-vEZFuOsxsD57pESYQBroa-oE6jArowwztm_IHGYRg9jVJIAa_wDdIdvUHqu-YECJMiPOTTIqxkkRxD3sOqtGlgIXNqajp5zJvS8vS33SFgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4d3da04bc.mp4?token=B5CTTSRWa4-PLVSe-_k4TEhUWs47t3sjE-Xi0QcLIUGmcY3Ba-xSyggcSrWfhkqJEFzLeK6bdPpMbihjfqS4qk-h2geMmfvrtNiTDwMNjcuemgvJCuV4A_1COF_sONftTfaLdi_vB0_ZOm0_5ZkYbNtmg5FiPY9V994yZ9ZJXgfu8_su6H2a5cihlnz7RwNbjnROpNJlb38sgePks2J2HoFKd4leg9o-9m16o1aUIE-vEZFuOsxsD57pESYQBroa-oE6jArowwztm_IHGYRg9jVJIAa_wDdIdvUHqu-YECJMiPOTTIqxkkRxD3sOqtGlgIXNqajp5zJvS8vS33SFgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهوره‌ای از اصابت‌ها در پایگاه پنجم دریایی آمریکا در بحرین
🔹
صفحه اوسینت Egypt's Intel Observer تصاویری از اصابت پهپادهای انتحاری ایران در پایگاه پنجم دریایی آمریکا منتشر کرد.
🔹
این صفحه در تحلیل این تصاویر نوشت: آثار سوختگی تازه‌ای در یک انبار واقع در داخل این پایگاه، در مختصات ۲۶ درجه و ۱۲ دقیقه و ۳۴.۳۸ ثانیه شمالی و ۵۰ درجه و ۳۷ دقیقه و ۳.۹۱ ثانیه شرقی مشاهده می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686648" target="_blank">📅 18:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686647">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/835d4c8879.mp4?token=eH_WzgAo0JqYLeLRCbe-pba-yfYYRZIDXCXfOyjYMci6EyQmUpKs-3sQXdclf6jVvn2hkkzhA3bPD6YLMvgNfzfGh44qdzxQj045qJhiTa8GhytTCpKnzg9HXco1LWRam0ABMFWMuw7oQrp2_A8MnYO1jqHfYiTshr_2N7c77hVi4pO1qfxPrJ3Cj2wedN6r2d_jr7CfLc0lwpRiMi7b7rkLagh2a2YzI5UgdPx49E6-G_kZGlv9SlwpgAIUG8WmN0xaVF2XZXLNWxjfyq7HKFurgh29LuqvG_xcgojUyZxofEbo6SkuNYJxM7JCnAIemb41uRL0tlQ585jpwStVbBQFYHiSy0XK6qUku-319ingSDcjuQ7lTlFWM4P4busOO1O7AzR_PrZ6iDDGImDgGldy_pydTj97z4_T_vZnutFop7pZHoqnPOPrMC09So0YVVOcxJ8YC-CVJCB-Ugrt7enjxjOmMh-T3yDv_7Y1yk6qU58FSr3SHMd_byLftGWo7YwPdua6JEP_QjUTkXgvkrMbbZUbL3NsISChSBdUDJvqRM68HCoXLS1Xh-Oi7LrtnGgzX8WVbGucdHNfsa-R89OFiLQ-Zc_tDaXT5TokkLfEgnzGCB0THxbGOQ0g2QQx6CPiY9Wt4d3scxSjyN_f-Z_5vgqTgHNBFzxk5ioFhrw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/835d4c8879.mp4?token=eH_WzgAo0JqYLeLRCbe-pba-yfYYRZIDXCXfOyjYMci6EyQmUpKs-3sQXdclf6jVvn2hkkzhA3bPD6YLMvgNfzfGh44qdzxQj045qJhiTa8GhytTCpKnzg9HXco1LWRam0ABMFWMuw7oQrp2_A8MnYO1jqHfYiTshr_2N7c77hVi4pO1qfxPrJ3Cj2wedN6r2d_jr7CfLc0lwpRiMi7b7rkLagh2a2YzI5UgdPx49E6-G_kZGlv9SlwpgAIUG8WmN0xaVF2XZXLNWxjfyq7HKFurgh29LuqvG_xcgojUyZxofEbo6SkuNYJxM7JCnAIemb41uRL0tlQ585jpwStVbBQFYHiSy0XK6qUku-319ingSDcjuQ7lTlFWM4P4busOO1O7AzR_PrZ6iDDGImDgGldy_pydTj97z4_T_vZnutFop7pZHoqnPOPrMC09So0YVVOcxJ8YC-CVJCB-Ugrt7enjxjOmMh-T3yDv_7Y1yk6qU58FSr3SHMd_byLftGWo7YwPdua6JEP_QjUTkXgvkrMbbZUbL3NsISChSBdUDJvqRM68HCoXLS1Xh-Oi7LrtnGgzX8WVbGucdHNfsa-R89OFiLQ-Zc_tDaXT5TokkLfEgnzGCB0THxbGOQ0g2QQx6CPiY9Wt4d3scxSjyN_f-Z_5vgqTgHNBFzxk5ioFhrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری رییس کمیسیون اقتصادی مجلس از فعالیت پشت پرده تراستی‌ها/ رسیدگی به پرونده ۲.۵ میلیارد یورویی
🔹
سید شمس‌الدین حسینی رییس کمیسیون اقتصادی مجلس در نطقی جنجالی، پرده از فعالیت تراستی‌ها و میزان نفوذ آنها در اقتصاد کشور برداشت.
🔹
این سخنان بعد از اطلاعیه وزارت نفت که مدعی شده بود صحبت در مورد تراستی‌ها، بازی در زمین دشمن است؛ مهر تاییدی است بر فساد گسترده در فرایند فروش در وزارت نفت و فعالیت مشکوک تراستی‌ها.
🔹
به تازگی دادگستری تهران اعلام کرد ۶۶ پرونده تراستی با ارزش تقریبی ۲.۵ میلیارد یورو در دست رسیدگی قرار دارد و برای ۴۳ پرونده قرار نهایی صادر شده و ۲۳ پرونده نیز پس از صدور کیفرخواست به دادگاه ارسال شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/686647" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686646">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b9e676a56.mp4?token=kjoCtv5UhOz8mfo1ZpTpvUc9gykR9Z91RpkGN036S8Lvzs3QtH-To80r1xMC6DFs0N0_9vkxsbBisW2ZfsxD-ENyB0J7_Ui8WVK66idzmxvMDoCoe4fnfE7BuDURyQoxYZ7DoWnbmJNTAMJe7bqZfOrP3IDT7rO3q2SSkdTZDi3FkTCNbDxzCXa1K7RL3pVn9BcEhVqioi8eOP8LX3IEia36BR1AmLHQgHmy8a8ijkUTWMu6Z8aiMqBlnaLGg-QzmpIC4ca7zfP41NsJ1SrSSqpzECl4wx9BGarqXONH4yKdM2Kz0_O7K9HDgHTVfK_wDncwI70Li9Xa4OmzCb_2-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b9e676a56.mp4?token=kjoCtv5UhOz8mfo1ZpTpvUc9gykR9Z91RpkGN036S8Lvzs3QtH-To80r1xMC6DFs0N0_9vkxsbBisW2ZfsxD-ENyB0J7_Ui8WVK66idzmxvMDoCoe4fnfE7BuDURyQoxYZ7DoWnbmJNTAMJe7bqZfOrP3IDT7rO3q2SSkdTZDi3FkTCNbDxzCXa1K7RL3pVn9BcEhVqioi8eOP8LX3IEia36BR1AmLHQgHmy8a8ijkUTWMu6Z8aiMqBlnaLGg-QzmpIC4ca7zfP41NsJ1SrSSqpzECl4wx9BGarqXONH4yKdM2Kz0_O7K9HDgHTVfK_wDncwI70Li9Xa4OmzCb_2-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان یار؛ رقابتی فراتر از یک مسابقه
❗️
اینجا قرار نیست فقط تماشاچی باشی
🔥
اگر فکر می‌کنی برای این چالش آماده‌ای،
میدان یار منتظر توست!
✌️
قراره وارد میدان بشی، رقابت کنی و توانایی‌هات رو به نمایش بذاری.
🔸
تیراندازی و مهارت
🔸
کمک‌های اولیه و امداد و نجات
🔸
تولید محتوای رسانه‌ای
🔸
پیاده سازی ایده های کسب و کار
لینک ورود به کانال پیام‌رسان تلگرام:
https://t.me/meydan_yar
لینک ورود به کانال پیام‌رسان بله:
https://ble.ir/meydan_yar
لینک ورود به کانال پیام‌رسان ایتا:
https://eitaa.com/meydaan_yar
صفحه ما در اینستاگرام :
https://www.instagram.com/meydan_yar</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/686646" target="_blank">📅 18:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686645">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FETVkDcZZjU5PI68cd1e7albPg6tsaSI_FBQjkMeZiAW8pyGhHjAPDotFNeq3ryamIsKW7IvjmAEti7979-eXe1Ppot0H-oc7AqpPdFhiRdFN9WjiUZdL8rFd08_YylJtyjp7QlDsC2WFsc9xcEpvskoLDmB2-KqEDNDQHHXBNOksBDH5kn3Pgp8n4V2VgVtXr7LnJkpI7-45fF2U-J9iUwpg-CS0MI61to-q1xaHNv8we163YVdCEHUxnpf1PJBezTir7jsUeDhPFNt6hOpUlGdyjJp4ZV893TznR0ft8GoRbUrpygJxVD176GsMsfquwlwVr6Ce-ncOSmaGAFPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشکش شیطان
🔹
آمریکا در ادامه‌ی جنایت‌های پی در پی خود، شب گذشته، یک مراسم عروسی در کوهستکِ هرمزگان را، با دقیق‌ترین سلاح نیروی دریایی خود، مورد هدف قرار داد. دست کم در این حمله فاجعه‌بار، پنج شهید از جمله یک کودک خردسال و ۵۰ نفر مجروح شدند. این جنایت، همچون باقی جنایت‌های شیطان بزرگ، در تاریخ ننگین و خونین آمریکا، ماندگار خواهد شد.
🔹
هشتصدوپنجاهم شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/686645" target="_blank">📅 18:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686642">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M5KGoOlW1ycrY0DzpGelMjTKjXMFpkmyzD5wMQlSyQ2qiPgF50A8vByuFxdQn8fZkcofnGVhpBqHR4OYJpJp_vX10XBJss2ItCoKBrZ3HH6qq9OvD3cHv-CAdEjb_aV-BybvpylcmnSBh__zjENa9ak_Xd0IgfT-R-HLsDw1PMog5kkE9HrFc04dHPWT-WvFsaAtzb6sHrpoir4skKtQasHcy79s_CfC9RjTi3y9-RByj-5_l2PfKovue9Yw4rdanxjWokCCZPcQxa0LlSyFUtRzKxgSlteRc2-a_4uif1cHPjqU33DEWyL4P-h7w8sxq9auvERWCv6B1hXeFkQrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqb-IRTsbOb8E5ZmhlsczfGBRHOAARcspFu8_QDwdl8yISyR7oKV3UwjKSjJ_AtczrC7Cj879ukYMLpGXJE8FvPui7erl8_gdwc9pYdaVJeL_XbcuzGuGHxQZe2zxhve_tFG6M4jlDDi9pueiUXy3uRGwfytv6xbX13KoYlIzBCaP8hGFWVdhzdIfC8bPw23_PuZSs0kQf-pp4wCcwiwlCg9KsjsCaKX10_kQFM_TRUM4raTE_Khr-OvsKvGe_UvaJ23p17lvK_pCPNxWeT9hbC_CMypAHFkAfWtSJj6lwlLJJKGy60osMuPuahgOgFfyGN9ZGjNJW9lJKG9hI38fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترکیب استقلال و پرسپولیس
در دربی ۱٠۷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/686642" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686637">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDpp4IiOQRmt6sas6xgy0tdUmEnzYDjZ4jQGxDVaHmJjbrhDHOuxyvLlEaMdGol4yg_ujJjjvnprbXxqFyjSg8s7s7psDKODcLNxWbxwt6-CIF-6MgcClQx_FxcnHmsfozfwXL2gsUA8eTv0KQRWh5tMt3ddyJl8rBr8TsNeoOmvIr9calaNH9fUcmFrX0wLzAOnRzm30lLdJBENGSUqDlpk8dYgUIkKyvocuwnHrnvF97kZpO5Jq1g29SNXeuaeHsbjYus8nq8el3EErtEvhmqWP7A7wV2sXydCqqt0E3jep-hsVZ5x11Omtw74f-5AiG3EmJ-iDJsyg_IkHZhKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاریخ امتحانات نهایی شهریور اعلام شد
وزارت آموزش وپرورش:
🔹
دانش آموزانی که در آزمون‌های نهایی تیر و مرداد از یک یا چند درس نمره نگرفته اند، آماده باشند.
🔹
امتحانات نهایی شهریور از ۱۴ تا ۲۵ شهریور برگزار می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/686637" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686636">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b7363f91.mp4?token=W2t-0Qs0CunmsQJ-DkUKcVPxPoapt68N6x_-gdzMMkkDR9cjLnKqA1QG7vQj_TL-BhhC1PoaIGaHlqfFpNQ5q098eJrsx3MOD0lbC4WQyp5-_GJhlPld3gC8hslqMcwFEXTm27PfFUfUQl14VJvFnhujvFAIbNyzYt6gNs22K6vbnlnjdrffDFUUn74YD2QZljheK48DMpfv-OChXHRk9-ZiEFJYhAfLo5vbdPV3m5LAqx917alsBOlU3ZsAXCP7jIy9gMbshhuhkD_HxDrQsU4Ak4y8KOwx-Q8XrXduQ2a0dpnjq9IMnJYGPVAL_8cFvfc2eflJmI9yewtSWODswA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b7363f91.mp4?token=W2t-0Qs0CunmsQJ-DkUKcVPxPoapt68N6x_-gdzMMkkDR9cjLnKqA1QG7vQj_TL-BhhC1PoaIGaHlqfFpNQ5q098eJrsx3MOD0lbC4WQyp5-_GJhlPld3gC8hslqMcwFEXTm27PfFUfUQl14VJvFnhujvFAIbNyzYt6gNs22K6vbnlnjdrffDFUUn74YD2QZljheK48DMpfv-OChXHRk9-ZiEFJYhAfLo5vbdPV3m5LAqx917alsBOlU3ZsAXCP7jIy9gMbshhuhkD_HxDrQsU4Ak4y8KOwx-Q8XrXduQ2a0dpnjq9IMnJYGPVAL_8cFvfc2eflJmI9yewtSWODswA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسنت یاوه‌گویی‌های مضحک ترامپ را تکرار کرد: ما ساختار قدرت در ایران را تغییر دادیم!
وزیر خزانه‌داری آمریکا:
🔹
ما دقیقاً تغییر رژیم نداشتیم، اما ساختار قدرت را تغییر دادیم. نفرات رده اول را حذف کردیم و بعد سراغ رده دوم رفتیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/686636" target="_blank">📅 18:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686631">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUn1NxcBPIikEa1yn5oq9bgG_zPhz37JhQX18WVe6yh-3CmkvrlrNSzY1zbDx6inp0cP7F5xZrNiCExEs66E2oDzQGBJrRrrgxH1gY8_N-jRgjd7lOz-MdgtV6zPbNCGgkv5VYG5ZYAhwR8M4uAdyvSJkBUTtnSNFH1-6BmO4Fg0RqFlXEmNoPsdrt8sXDdeUVSfhwHxRc6jZyINv7QTvsDyuvoe2weAJ3rukOaPjuaFTe2N8SxzDOqAaGosiSU522K1gNAQCgH1aRMqlDo3UdAh0-lPL5fsLPJ7IfcjMCdgW8A12xCH5e24CALqyGLbqE5_IlUSrvaPBsI9Csokug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYJvOPihev5bhOCYN2KkyqiFUJzdMiUoaKodR9r_3J2kcQvwTKORdF4eutmRCbVtB8FP72CvuovpxOGKJx5EV-eE4Io3Cy7vIMLepHrzF6gP_c1AWzQZT7xak2LJ4k8uFCYzOi7d6BcQndg0vTo6TorrwRF6729rXmkR21Zqk0oat8tJ3ONaF8HZFH9FLeMDzE_UhkM9117zjebEXrv46iPsMZ_4Twbpl9WO5Vlmm2mGBpvnuUblT3ePCdTz8VrHTaqTa8yzRVrTgBaLEuPGaensohcmB5nE3CH8G3Nhp-qO1Ms93Jvmy8EYdJkL3-WweQVaLLV06S_4FCxfgcTmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWtiebnN1mAfu3gqXO6DFFynN0Hd5dXj17nwU7IePRIuPv4rNnJx80cRlgBaYr-XYcjCDg2CyjwTRvPXnbmoSVRxpX2mAlSSkB2hdBn9KdMvnfCpnv1Sb4KQ8S7YhWdZEhxscymeAhYLCR3L57uZYxc4w2VKjXyjFN470hQ9xLX77xCBAuyT5QbaAb8uwAtEkeMibeiNv-6_cVg2nQV8qSfB1Xf4HIzDp8zUYJBNN6paGR6FxBNAfBW5JFfr5gWKgz5WdORpZMFAB2GIp9n4HJlY-imVQPsXaFsBKjbh2ceIif69IuxFrccfnABXaVabyYd-FuA2i1DrDlOu1adEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQa1IaLycrEj7mUcMe5fgmgiVTqSt3b8t07mbvqc6-DtPuiXtJA97WFYT_X6KcCNOIrYOa43OZK3TQUdXMvLz4NwcOeStotODGsRrSKV6KLqatnZ08mF_9C4IxlAeYc8yDqRsTXK_SQ-q1TxuTt_rDg7fWNRHJ4DyfS-EE9VsoN-CmQozc3PgWNIsytnPPfC5GGKx5FyfgFzy8QudXIlnSNcjEXxDywcQf8Xze3P78AvQzkpoaLXGiGeAXe9hxQz64FbvY-v4OtqUmtdY4Pm_WDh4UWIGtpb4BtoPsxpNtBFL4A9fg987eZTGNgarFjsJKRlHisaqejXP5ENkxTkVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovGx3-sdzrW1yw1K0bBkM-jCws-fuaoSNtGpgjwlibmfXQqQb_jEInAwMWSOLo9x2N265zqdtDXX7rLakXAsqTG1MLDNvphMbXHRJha7GuowiclAqI9UKmHYqg9C0-tDLyBIZXdGcndPVPDq3XJz0-BCoHoxh7k0NX7jMeq2TDb1E9UfIBPtjv57gSSzJAwo_4qc1iMV2akDWyCmQdDhym5SdOdJFl7h2GB3O_tQQEQBLDNFZGpL0pZ_ZFn_Wnnrq-O0zwSOZepkjyAuRLoyb6RgcsXE77EJtdf8LHMKkHqWv3NsWOTJqvfSXIDwPohXpdjboyVPhoaLreQo6WVykA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استفاده از این قیدها در بین جملات انگلیسی تا حد زیادی می‌تونه سطح زبان انگلیسی شما رو بالاتر ببره #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/686631" target="_blank">📅 18:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686630">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: می‌خواهیم فشار اقتصادی کافی را برای وادار کردن تهران به بازگشت به میز مذاکرات ایجاد کنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/686630" target="_blank">📅 17:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686627">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aUxgW-MktLHVHqSwg7kn6w6oNIgkuyjR9Cd9DHv3jBUQaXUeOijHkk4ISMusg_bx8orORP18wlsehBkAca-COF5QdNG1BWL4SDTYh1VtFxRnKJqlYTL4PpdlmEWa-aavxlbPl08LmX9rk8kThCimEkFkbW3DT6e0vhBQmHa6S9ywR_IwkSMRDttmsSzviryYJNPvkHFdjKGblEqa35RNufdLpkqoPKQEJXliysW5mBjB73w3HlSw6xW88UW8os4Zksg-C95mbYSTOVT6Ycq3D4UyvuIkkSzsG7HNhLJrT2e5OBzjNlQiphbY3Y9IiSjU8DWzzk2ybseSo8KjDoJpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCubbQpK5F2yDXF-eS-pDw9wj_awNheF1FnTu8uK7cnNaMZ0jJR33CTROTqZhOOA0FLqpaN7a_zF-3pKxWIHzjpHReVg41MKuzKFQujWLipDeL1yAfHtW9sKLQ9WX6l_emIhXVCcuEEfK7lX_cZbc4WzzspLB3uQdCrdyNKJxEm6-r4GkEIS7iGzOLGI6sETdIbn1kI9w0eGnOKmJXhpAW4WEElsSKVdckITvufHREZM7ZLCHXrX-zkWE124c7HxgN2Fd5RgTfR5pyvOGGxDujgUxX63RE6c2l9DxsTyfNELEP5DYcZMqVjdwDXl-a8zOUucV87eAZPKmYmzR9FzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvcKZyCr9IsPNiCc6FopAEVUsgfnO1uYxHmwShMpJtpzfXkf6sKsC7nLpDIdpxewPj8m7Wf2YvXYSLwDJdGqTsqW8iq_RDBa6T_UNeuUOgmpiuJY73uE7Y3NQOIKCVljzIa1rQqJ5skG1JSG4xCXpLsdrVKO_nYP-xP6ycs2TXEsw2sPlIerAe-burQeMrllf1L_IKqRz1UtlwDhdip60QjGASS5PCLyfB6K5pzqaA8f7CBb1Z157d1vb40jTvJObvD4NYx0Y98gsedimhLnaQXuL-CemjUFTO75Oc8CfTOvTcVmDB9sMpLb6SaTx2TqRtZ6Vyhzg4unR4H7_VavKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرماندار مشهد: علت تصادف بلوار وکیل آباد ترافیکی بوده است  فرماندار مشهد ضمن ابراز همدردی عمیق با خانواده جان باختگان تصادف رانندگی شب گذشته در بولوار وکیل آباد این شهر:
🔹
طبق بررسی های انجام شده حادثه شب گذشته صرفا ترافیکی بوده و هیچ علت ضد امنیتی در وقوع…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/686627" target="_blank">📅 17:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686626">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39663bda8.mp4?token=htATF1BfRN2PueuNZ2ZauLEUGMWHPXsxX8E9N08__-JWvR6GFIHJMNZXU6pmzvV4J1j09ArLcO4tNQDzvAhz46Ovvw__UPa251GJ2Nd19oSomubLXvsIu9liUyw9eGCHMEzm4a6RP6_aemwyiFIKG9unua5KcFCEqBJ5DA87ZTQG-Zz8W6xFnDorYRSoHUVt0nvh-KbZvPn-GjeBgwfYyV1s7F-eUIzFeFj-oVvz4LgcHLJUUNotEKo7h_VWyRx8GSfpBUZZkwfdeks_nqJR6yFQoeoXbhveublix1gxGWCjfd7Iu56HRxW-psMwlvUZnxeoBK_O8uQVIDkdZupUj4ImunFIcyp-U_kFtrFcdIa_qtMtbLFqjLwgfYfhhQlcAtFxntTilX3u-81h-RxeG3ticvul4RHUncqmbRrSlT0Ew9EYRwsuWBR_u0ycBlumpI5GqJTICydg3ml_w357ylmeoHx6bMFa6a1AYeuJqjMLpqa1Hwace0SbEXOA0DBeYLYFK07LeCEyRxKnNb9AjnKn8bccFL4T8d5qjiPYx_A4v_PqBf_0d8JfxnvyUtSE7JW6m386V8LDkMwpvDByGkE7SByFmWcHu8SrXXRkZLLKF8bPpT6syuIlPzXyN803TxiWAKNy_KQycOm3o7z_QVCnGJJnOZW3ofdCRk_Hk-k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39663bda8.mp4?token=htATF1BfRN2PueuNZ2ZauLEUGMWHPXsxX8E9N08__-JWvR6GFIHJMNZXU6pmzvV4J1j09ArLcO4tNQDzvAhz46Ovvw__UPa251GJ2Nd19oSomubLXvsIu9liUyw9eGCHMEzm4a6RP6_aemwyiFIKG9unua5KcFCEqBJ5DA87ZTQG-Zz8W6xFnDorYRSoHUVt0nvh-KbZvPn-GjeBgwfYyV1s7F-eUIzFeFj-oVvz4LgcHLJUUNotEKo7h_VWyRx8GSfpBUZZkwfdeks_nqJR6yFQoeoXbhveublix1gxGWCjfd7Iu56HRxW-psMwlvUZnxeoBK_O8uQVIDkdZupUj4ImunFIcyp-U_kFtrFcdIa_qtMtbLFqjLwgfYfhhQlcAtFxntTilX3u-81h-RxeG3ticvul4RHUncqmbRrSlT0Ew9EYRwsuWBR_u0ycBlumpI5GqJTICydg3ml_w357ylmeoHx6bMFa6a1AYeuJqjMLpqa1Hwace0SbEXOA0DBeYLYFK07LeCEyRxKnNb9AjnKn8bccFL4T8d5qjiPYx_A4v_PqBf_0d8JfxnvyUtSE7JW6m386V8LDkMwpvDByGkE7SByFmWcHu8SrXXRkZLLKF8bPpT6syuIlPzXyN803TxiWAKNy_KQycOm3o7z_QVCnGJJnOZW3ofdCRk_Hk-k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لایحه نفوذ علیه کسانی است که سازوکار مملکت را علیه مردم خراب می‌کنند
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگوی
اختصاصی با خبرفوری:
🔹
اگر دولت خودش اقدام به دادن یک لایحه نکند، مجلس خودش وارد می شود مانند امروز که طرحی دوفوریتی در خصوص عوارض گمرکی در بحث شهرداری ها و دهیاری ها مصوب شد.
🔹
دهیاری‌ها و شهرداری سهمی از بودجه دارند که در حال حاضر معطل هستند و دولت باید زودتر در این حوزه اقدام می کرد.
🔹
همچنین در خصوص سهمیه قیر، اقدامات عمرانی معطل تخصیص قیر هستند که چون دولت اقدام نکرد، مجلس وارد شد. در بحث نفوذ نیز وضعیت به همین گونه بود و ما خلا قانونی داریم.
🔹
در خصوص لایحه نفوذ این گونه نیست که آحاد جامعه درگیر شوند؛ نه هدف مجلس چنین است و نه عقلانی است.
🔹
خطابم به مردمی که نگرانی دارند این است که عزیزانی که تخلفی ندارند نباید نگران باشند. این قانون برای کسانی است که سازوکار مملکت را علیه مردم خراب می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/686626" target="_blank">📅 17:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686625">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj5sOta6b7EBPRSCYYb3lXU1Q8Blh9XX6v0uMMxglcvnKCND7DzOeCCfa0wAHkHs5sTRHEVGUtFCC3zIsgzyb9Fh0NUO9UZImQ5KAEMWqA2io3ImHJ2jmHB8bpVm9o12GrOvZiJhlRTkKW9OIwrkkVOn3jPEoFy1Qk-ET02f9aO_Xd0B4-fEalAGNvHcsNjCqK9dmQUw86HaIk6TkAF9G0nmxGQXsQbk_MGPdviFx1s1FhVL_CsOz-guDDbq7i0bcaxA0O-dTk7Yj_YWz0OvQMomDXxG0uxVgiPx-t4sKihcSynVFeNXpHaimtBv-qzDHw7r-94Llpc1pSrMLkjjgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سکهٔ ترامپ وارد بازار شد
🔹
فروش سکهٔ یک‌ دلاری دونالد ترامپ امروز چهارشنبه شروع خواهد شد؛ عرضهٔ سکهٔ ترامپ در حالی انجام شده که استفاده از تصویر رئیس‌جمهوران زنده روی پول آمریکا سابقه بسیار محدودی دارد.
🔹
در سال ۱۹۲۶ نیز تصویر رئیس‌جمهور وقت آمریکا کالوین کولیج در قالب یک سکه یادبود نیم‌ دلاری استفاده شده بود. این سکه از ترکیب مس، روی، منگنز و نیکل ساخته شده و ارزش اسمی آن یک دلار است. ضرابخانه فیلادلفیا مسئول ضرب این سکه بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/686625" target="_blank">📅 17:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686624">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
برخی منابع خبری از وقوع یک حادثه امنیتی برای یک کشتی در نزدیکی تنگه هرمز خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/686624" target="_blank">📅 17:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686623">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23b5feae79.mp4?token=BqacwVdCM0dNbIdi4pF7snLRbkseWLd4eNA5lLbxxB3dffHzsmjMSIvZttNQlTppnn8yPAHUd6gofKc2EGLIYxAgpIYkFJGqLuZqGnLzDfM_UbBhns93TUQ778b7cx-6xn2e-LCOV17pNnFkjZnZVif7kp648RY4U5HdSJpahOt89pppb8JpkO7pHCS5rwxkXCaZRpAs95VVKdDUzXLnH3pZ6llX8EZWPQaWirSyvFjgdapNkp8_hdAIyLIu-8L8N_BJz3wY1F_KPgyICRQIlsIoepNHSJdE7isiYbb3Rewa4U-9fzQ12dwoSqO5WMn86JVpvjoKGjeM6xvi3AO28Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23b5feae79.mp4?token=BqacwVdCM0dNbIdi4pF7snLRbkseWLd4eNA5lLbxxB3dffHzsmjMSIvZttNQlTppnn8yPAHUd6gofKc2EGLIYxAgpIYkFJGqLuZqGnLzDfM_UbBhns93TUQ778b7cx-6xn2e-LCOV17pNnFkjZnZVif7kp648RY4U5HdSJpahOt89pppb8JpkO7pHCS5rwxkXCaZRpAs95VVKdDUzXLnH3pZ6llX8EZWPQaWirSyvFjgdapNkp8_hdAIyLIu-8L8N_BJz3wY1F_KPgyICRQIlsIoepNHSJdE7isiYbb3Rewa4U-9fzQ12dwoSqO5WMn86JVpvjoKGjeM6xvi3AO28Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری ؛ پیش‌بینی دربی
🔹
در آستانه دربی ، مخاطبان با ارسال پیام‌های صوتی پیش‌بینی خود از نتیجه بازی استقلال و پرسپولیس را با ما به اشتراک گذاشتند.
🔸
الوفوری را دنبال کنید
👇
#دربی
@Alo_fori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/686623" target="_blank">📅 17:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686622">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارشی متفاوت از قلب بازار موبایل
میان رده هایی که پرچمدار شدند. تب و تاب این روزهای بازار موبایل. کدام مدل ها بیشتر می فروشند‌؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/686622" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686621">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlu6mP_OSQQLYcAWcrxvhbGioq_6oVziz6rI6SgI_rex62jBMHhu-lXPlET0orxBCaqdOB5NkDThbpTx2xYH3zlwOXqgrrcxCpuCFE8sS0dOaCpMUapqYMgJ5WM1Cm0BPemkoePepuBDVewrRVmF1pJBLnQ8xIpvPeHeIq2JOtOptkClyNjfaZ_-fmlTnZ-NpnkbqsIfys9HoUxVNd4VVAEh16jyyU1aOxY0oXPzI99RihSITfGjDRtyI-dUnYN1sqo89Yy3X3lA2JTMXAz1WBiPPvohT9Ir-tPH8Ivje3Hs1gHyx-DyxR896nxcXiw_kBEqSLi-9NuUpSzm39L_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقایی: ادعای سنتکام در حاشا کردن حمله به جشن عروسی در سیریک، دروغی وقیحانه است
سخنگوی وزارت امور خارجه:
🔹
«تیم هاوکینز» سخنگوی سنتکام، در انکار جنایت سیریک مدعی است که آمریکا غیرنظامیان را هدف قرار نمی‌دهد.
🔹
ظاهراً او سوابق رسمی ارتش آمریکا را فراموش کرده است: کاکارک در سال ۲۰۰۲، مُکرَدیب در سال ۲۰۰۴، دِه‌بالا و وِچ‌بَغتو در سال ۲۰۰۸؛ حملات مستند آمریکا در افغانستان و عراق که به کشته‌شدن تعداد زیادی از غیرنظامیان، از جمله زنان و کودکان، انجامید.
🔹
ظاهراً او چیز دیگری را هم فراموش کرده است: حتی سریال Homeland، محصول آمریکا، در فصل چهارم حمله یک پهپاد آمریکایی به یک مراسم عروسی در پاکستان را به تصویر کشید؛ حمله‌ای که حدود ۴۰ غیرنظامی را کشت.
🔹
واقعیت آن‌قدر هولناک است که حتی پروپاگاندای آمریکا هم ادعایی را که هاوکینز امروز مطرح می‌کند، مطرح نکرده است. سیریک داستان نیست. غیرنظامیان واقعی‌اند. قربانیان نیز واقعی‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/686621" target="_blank">📅 17:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686620">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27bd7a197a.mp4?token=uLWoWe9mjC_II7bKvHKk2Rv3aVV1i49V3cE5cpCgvQ0S8MZ85P3WMWr4fvaf-NXsnOKpdaj4hk4LpLOeVAmX81GznKWU2ABWOOxXmdkiSRs_HapULRmTkSwXg5LCho5YyrwzZRKcrQBWwE9Cg25eIHXJbyovSzReErGeH6pmV_KQlcXrMqd7tLhcy9pQc7nzXAi7EzlnPDqFZRkjSIWgUNbktso3RmnS4akd_sulstzEkvD4AhEIH-drLPJ7ir-QrklGkQFJQH9XSms3PtsGx9IZpgD3ZGV77NHX6fb-ajvz4mz_XqMCXwRE65fnTNXOXVwAvwtQ3awVKMw-m0UmTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27bd7a197a.mp4?token=uLWoWe9mjC_II7bKvHKk2Rv3aVV1i49V3cE5cpCgvQ0S8MZ85P3WMWr4fvaf-NXsnOKpdaj4hk4LpLOeVAmX81GznKWU2ABWOOxXmdkiSRs_HapULRmTkSwXg5LCho5YyrwzZRKcrQBWwE9Cg25eIHXJbyovSzReErGeH6pmV_KQlcXrMqd7tLhcy9pQc7nzXAi7EzlnPDqFZRkjSIWgUNbktso3RmnS4akd_sulstzEkvD4AhEIH-drLPJ7ir-QrklGkQFJQH9XSms3PtsGx9IZpgD3ZGV77NHX6fb-ajvz4mz_XqMCXwRE65fnTNXOXVwAvwtQ3awVKMw-m0UmTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی یک متخصص ژاپنی برای کمردرد وایرال شد؛ ادعای کاهش درد توسط کاربران!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/686620" target="_blank">📅 17:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686619">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd22734b47.mp4?token=s7m07pz9dL21cQ1VMr4yS9VCv-3oH53fqUJz0Gfpb7zmWfZcoL21Y8gQ8xoPUM3DHDEjzooXFg_86R3rXZDVA5xhU3-6oCLFqMD0rCX7aVQboWEanH97EHbFxT3jZ2ZvEzfyPN99KdBPAhSGX40a4NL1Nvr6gTzaVGDw7IwNERxtQDem7tTfKttE6jydWx5aQbPJxNTDIDE_qHGT4zkBYA9GYztbY6XpRN2tNXeYj4uHsyGUeoUVykaxpqz6vHmIhpiwtecaYgTt-l08peZwWuRqqCI4ZCfvoXM77TXEIj4hSqQDaqnnD09ot4Bvp4Hzj3mBEskLHJDrppUffBxZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd22734b47.mp4?token=s7m07pz9dL21cQ1VMr4yS9VCv-3oH53fqUJz0Gfpb7zmWfZcoL21Y8gQ8xoPUM3DHDEjzooXFg_86R3rXZDVA5xhU3-6oCLFqMD0rCX7aVQboWEanH97EHbFxT3jZ2ZvEzfyPN99KdBPAhSGX40a4NL1Nvr6gTzaVGDw7IwNERxtQDem7tTfKttE6jydWx5aQbPJxNTDIDE_qHGT4zkBYA9GYztbY6XpRN2tNXeYj4uHsyGUeoUVykaxpqz6vHmIhpiwtecaYgTt-l08peZwWuRqqCI4ZCfvoXM77TXEIj4hSqQDaqnnD09ot4Bvp4Hzj3mBEskLHJDrppUffBxZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگۀ هرمز همچنان بسته است و کشتی‌های مختلف هدف قرار می‌گیرند
🔹
گزارش خبرنگار شبکه سه از جزیره لارک؛ جزیره‌ای که هدف حمله نیروهای متجاوز آمریکایی قرار گرفت و در پی آن تعدادی از نیروهای نیروی دریایی سپاه پاسداران شهید و زخمی شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/686619" target="_blank">📅 17:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686617">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI9zs-0apWDJHtjULxcxOv-rFNvqWWiRgqrrOE09opiJ6vjYn1mw5dPILAAtjb9-oFfhiaVJujWmVB2xC5-1cz1KVVBQEirdVACJe9Blt39fqxgCFgi7NP6gvOIhxr9dMYv6abZj8p1K9LKFdxh3GXfUGB-pJkZ6In3g15_aVPRuxV8AtLdV-wZQiMzSeZH0KlyGTla9CFGDwePAmDbUw5m4cCjS9ltYC_zrxUSswdI-Wf46XW-lMBFu3ufKEH_Mu51ToAgOzFIPUCuJNJ6JakjhQNWfB9h8zSbCDYxVsk_xzrkrHB0w1jSWHQHV5BdU-4jxDlXTP4sLoIv-Dlp7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ موشکی و پهپادی ایران به حمله وحشیانه آمریکا
🔹
نیروهای نظامی ایران در پاسخ به حمله شب گذشته آمریکا، مواضع و پایگاه‌های آمریکا در پنج کشور منطقه هدف قرار گرفتند.
🔹
مخازن سوخت و کنسولگری آمریکا در اربیل عراق، کمپ تیتین (ساحل عقبه) و آشیانه پهپادهای دوربرد پایگاه پرنس حسن در اردن از جمله این اهداف بودند.
🔹
سامانه‌های راداری و محل استقرار نیروها در پایگاه‌های الظفره و المنهاد در امارات، تأسیسات راداری و مراكز تجمع در پایگاه شیخ عیسی بحرین نیز بخش دیگری از پاسخ ایران بودند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/686617" target="_blank">📅 17:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686616">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جانشین فرمانده کل سپاه: تمدن برآمده از ارزش‌های انقلاب اسلامی هیمنه نظامی آمریکا را درهم شکست
🔹
مدیرعامل شرکت ملی نفت ایران: ایران صدرنشین کشف گاز جهان شد
🔹
جرج کلونی، ستاره سینمای جهان: دولت ترامپ توسط کم صلاحیت‌ترین افراد اداره می‌شود
🔹
چین و مصر: جنگ آمریکا و ایران، دیپلماتیک پایان یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/686616" target="_blank">📅 16:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686615">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای نتانیاهو: از نوار غزه عقب‌نشینی نخواهیم کرد. در حال حاضر بر ۶۰ درصد از مساحت آن کنترل داریم؛ قلمرو تحت کنترل خود را گسترش خواهیم داد
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/686615" target="_blank">📅 16:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686614">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
شهادت یکی از نیروهای راهسازی در جهرم بر اثر حمله پهپادی دشمن آمریکایی
🔹
بامداد امروز، یکی از کارکنان بخش راهسازی قرارگاه سازندگی خاتم‌الانبیا در شهرستان جهرم، بر اثر اصابت ترکش ناشی از حمله پهپاد شناسایی-رزمی دشمن آمریکایی ، به شهادت رسید.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/686614" target="_blank">📅 16:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686613">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/196b45b251.mp4?token=KZm4_O1S_G91yS-dX0O4kO6dfkaid2YKr2kV-ZIB9duSe4_hCsfmsyq4uarN1aTjCqNtymI4sdVcoWpWUGse95p2_fkHM8SzTqEvoDWKI2a0PSLd2XAkY0BgA166GCrxeY5O4ZwRWz4R4_ilFHQGJQ48r2UOLUDMxvdpoY6ltSQRFPi_stoM4sJ-b3IrI6rq9q7EFrxGnY03XfBo5tD8I9ll3NBubgI5F-vXlE9FV218QdlKEoBDF6FQBJItyo8GSIs64pKH8CeOx8Our0YAinHrjXMb-5Bit4obd7-cfBtygVJHJksxYjKDQxLS8EyQgYSeuTySchGf39MoZuFCp7O2FTKIvgglZuAPrYDru52Vur-spUjiclymi6EkspT1TiqClz127jl9-P8HZiCNM_qmxOC49m6vOA-jyeU4hS3vEo8wgERVmzPW6LiwiXliti2lTNEr2IKhyFiU8tDJkcwmnJ-z5MZsvBUktwFZ6CuTNBnQk8zMCHz0n2cQmJoumjAS-yZugYK7IC_R9Odr3SfN8nXbWqdg2hhEvtx3moLl4Purwhv4lZ8eP7S7Mz9AhsA0o1DdscPbptL4ulqdy912RnJxLtGT6aSMh0C6VgBSH8flNV2A7ewKWs9pxkuv_ZfUgVf7FdEMbCo81XZoNSaopEPDYWhsJIVa324g0WU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/196b45b251.mp4?token=KZm4_O1S_G91yS-dX0O4kO6dfkaid2YKr2kV-ZIB9duSe4_hCsfmsyq4uarN1aTjCqNtymI4sdVcoWpWUGse95p2_fkHM8SzTqEvoDWKI2a0PSLd2XAkY0BgA166GCrxeY5O4ZwRWz4R4_ilFHQGJQ48r2UOLUDMxvdpoY6ltSQRFPi_stoM4sJ-b3IrI6rq9q7EFrxGnY03XfBo5tD8I9ll3NBubgI5F-vXlE9FV218QdlKEoBDF6FQBJItyo8GSIs64pKH8CeOx8Our0YAinHrjXMb-5Bit4obd7-cfBtygVJHJksxYjKDQxLS8EyQgYSeuTySchGf39MoZuFCp7O2FTKIvgglZuAPrYDru52Vur-spUjiclymi6EkspT1TiqClz127jl9-P8HZiCNM_qmxOC49m6vOA-jyeU4hS3vEo8wgERVmzPW6LiwiXliti2lTNEr2IKhyFiU8tDJkcwmnJ-z5MZsvBUktwFZ6CuTNBnQk8zMCHz0n2cQmJoumjAS-yZugYK7IC_R9Odr3SfN8nXbWqdg2hhEvtx3moLl4Purwhv4lZ8eP7S7Mz9AhsA0o1DdscPbptL4ulqdy912RnJxLtGT6aSMh0C6VgBSH8flNV2A7ewKWs9pxkuv_ZfUgVf7FdEMbCo81XZoNSaopEPDYWhsJIVa324g0WU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم اخبار را از کجا دنبال می‌کنند؟
🔹
پاسخ‌های جالب بازدیدکنندگان بیست‌ونهمین نمایشگاه الکامپ به پرسش خبرنگار خبرفوری درباره شیوه دنبال‌ کردن اخبار.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/686613" target="_blank">📅 16:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686612">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYsZsD8_Gvz9vtd4ABjLU-Y9fRgOFXWqFh3AqEEU2U3uRjj1R4CkmZF-WXhjn2EIBHPLeyCqVTSJAGJ_5S-fhG-Wh2Nm7w8uQxl8lPNoJXK8nRvi-vy3m1c2AfMZAWJ2b5I3Dsf1aVKOgY58p9XPhNDb51mCFGv8Ge-Ve0Z9t49GtwcnGr3nX9UDwbnKDIN3Wme7Z7DyAgPHDcHZo9JA2cOWSv7KXFhRBJ52hoq7iJrPUZUcMGdE80zZftgX4XorMbr8zxaddVKKPl_3q3wqNMhdHwhp-KtLyPR5IsRUg9egUiz5phumzlLZ3l-T1IjNFd4Cg91e4yzq6LMrXxQ_Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دکتر شایان: «بنگاه‌سازی» را از «بنگاه‌داری» تفکیک کنیم/ بانک تخصصی باید طراح تأمین مالی پروژه‌های بزرگ باشد
🔹
نقش بانک‌های تخصصی در ایجاد و توسعه پروژه‌های بزرگ، با ضوابط شفاف و نظارت مؤثر، می‌تواند در قالب «بنگاه‌سازی» و ایجاد ظرفیت‌های جدید تولیدی و زیرساختی تعریف شود.
🔹
بانک باید از تأمین‌کننده صرف منابع به «طراح و راهبر تأمین مالی» پروژه‌های بزرگ و پیشران تبدیل شود و در کنار منابع خود، از ظرفیت بازار سرمایه، صندوق‌ها و ابزارهای نوین مالی بهره گیرد.
🔹
اجرای پروژه‌های بزرگ تنها به تأمین منابع محدود نیست و به شناخت صنعت، طراحی ساختار مالی، ارزیابی اقتصادی، مدیریت ریسک و نظارت تخصصی نیاز دارد.
🔹
اصلاح نظام بانکی نیز باید هم‌زمان با اصلاح ترازنامه و ارتقای کفایت سرمایه، بر مدیریت ریسک، حکمرانی شرکتی و بازطراحی مدل کسب‌وکار بانک‌ها متمرکز شود.
🔹
بانک دولتی با مدل کسب‌وکار سنتی نمی‌تواند مأموریت توسعه‌ای جدید را دنبال کند؛ نقش بانک تخصصی باید از تأمین مالی صرف به ظرفیت‌سازی برای تولید و توسعه گسترش یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/686612" target="_blank">📅 16:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686611">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
کاخ
کرملین: در جریان مذاکرات رئیس‌جمهور ایران با پوتین، هیچ درخواستی از سوی رئیس‌جمهور ایران برای میانجیگری با واشنگتن دریافت نکردیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/686611" target="_blank">📅 16:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686610">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHeWs2b91FI-kSYB0tOXWcx5JEQsRHzu7xIMteYvPlPOPtYw8-o3UItshYRhBOVOsdau2RLGymVa1-WlrC8Tg9IETUaPur5rSb_Md1xO8wvsrTa6aqpKnYKRSXgxG4bENrauxAfIQVwE1TYfSkw7_M7JzwkU5wx961ojX9RcH8zzx_R-4QO8XBPA_ehuUCSAWrewvMAzumIgNfyxlJFsxjWmOKVmERFsxcYCODqehRSTWz-jlfUAaIIeInuE4xopxhPemx5bRtCdd-rvQtMpGvxxQoJll4lDrAF4P9kk-tbFdH88VT-i-oSkYZn-ONukysQtgjl4IHBvt5TCODASFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری پردیس احمدیه در واکنش به جنایت آمریکا علیه سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/686610" target="_blank">📅 16:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686609">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-poll">
<h4>📊 🔸به نظر شما کدام تیم برنده دربی امروز میشه⁉️</h4>
<ul>
<li>✓ استقلال💙</li>
<li>✓ پرسپولیس❤️</li>
<li>✓ مساوی</li>
</ul>
</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/686609" target="_blank">📅 16:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-686608">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
سرمایه‌گذاران طلا چگونه به نرخ دلار جهت می‌دهند؟
🔹
سرمایه‌گذاران بازار طلا برای محاسبه سود و زیان، علاوه بر قیمت اونس جهانی، نرخ دلار غیررسمی را هم در نظر می‌گیرند. به همین دلیل، زمانی که انتظار رشد اونس یا دلار وجود دارد، تقاضا برای خرید افزایش پیدا می‌کند و در شرایط معکوس، معامله‌گران به دنبال کاهش زیان خود هستند.
🔹
در حالی که قیمت اونس جهانی خارج از کنترل معامله‌گران داخلی است، نرخ دلار غیررسمی می‌تواند تحت تأثیر رفتار جمعی بازار قرار بگیرد. فعالیت معامله‌گران در گروه‌ها و شبکه‌های اجتماعی و افزایش تقاضا برای ارز می‌تواند به رشد نرخ دلار دامن بزند؛ نرخی که خود به عاملی برای تصمیم‌گیری بیشتر سرمایه‌گذاران طلا تبدیل می‌شود.
🔹
از این منظر، بخشی از نوسانات بازار ارز را می‌توان در کنار عوامل اقتصادی و محدودیت‌های ارزی، ناشی از رفتارهای سفته‌بازانه و تلاش معامله‌گران طلا برای جبران زیان یا حفظ سود دانست.
🔹
این امر توضیح‌دهنده خوبی برای افزایش نرخ ارز غیررسمی در ده روز گذشته است و البته نباید این نکته را از نظر دور داریم که انتظارات ناشی از کاهش منابع ارزی به دلیل سخت شدن تحریمها نیز بر تحولات نرخ ارز اثرگذار بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/686608" target="_blank">📅 16:30 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
