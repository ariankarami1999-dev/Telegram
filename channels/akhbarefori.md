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
<img src="https://cdn4.telesco.pe/file/PDgrB4vGEfeYGq1eUfOS8P1nw22r5D6RAEDR2s8FAEq9ltpQtIvnFbdb4gZ3wDVVpmMn8WUjo503Z9TxtGJPd8YIJmZbN6X66I9LydBfwHSupY1KPXsx6ElPCyvndMtseNlgAga4hxgVjxMOfY3XDrR-X4mxM0PHbTvvb-0kjq_mKalwX9OTIcOo3TSmN55d4mqdtNyEbo0ZCEVbRb_e2nchR2ojI6_Kz1bn3SlXSdnENHL7j3k8F1r40Vqu6wYKbF8b0H9CTvw_pkdNwsBSRyKj0A9p0XCiv4pFq1hgb1P1lZ2QT8f0ZOV2qI1FhVE-8pHZaL0gRsq-25VBscbgbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 00:57:43</div>
<hr>

<div class="tg-post" id="msg-671606">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494055b9e4.mp4?token=jj2s6ehbyLS4w1yZhdjqhvNB5MnzOYJValvJUrLjCKfvGQlM79gAOydzxz6Ik_YL53jQ0MkuLCBCXIQDiHLkbWyNyWl66R-MiZUJM2zJiFo2jAaR0ff0aRTRrPs-znuqhlWdFq9LIjlzzzHesJP-gxmqZZHi_Hvn76SRj58GoqBdeWr_ndq5yticlYx8WviTwRao-K0PgGtiryeO866qiNzzbFs7XiFRsGAztDU0csXXhba6tHvoub5s5PaFXldOKSZ6sFNzrYZt-HKBmDqrdmtxZQ90p0xkg1U4pORhi3mQ9cH8LS_i24XnWxpQZKyf2DwxK7xn5miwckYJqRTTJIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494055b9e4.mp4?token=jj2s6ehbyLS4w1yZhdjqhvNB5MnzOYJValvJUrLjCKfvGQlM79gAOydzxz6Ik_YL53jQ0MkuLCBCXIQDiHLkbWyNyWl66R-MiZUJM2zJiFo2jAaR0ff0aRTRrPs-znuqhlWdFq9LIjlzzzHesJP-gxmqZZHi_Hvn76SRj58GoqBdeWr_ndq5yticlYx8WviTwRao-K0PgGtiryeO866qiNzzbFs7XiFRsGAztDU0csXXhba6tHvoub5s5PaFXldOKSZ6sFNzrYZt-HKBmDqrdmtxZQ90p0xkg1U4pORhi3mQ9cH8LS_i24XnWxpQZKyf2DwxK7xn5miwckYJqRTTJIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بیمارستان شهید بقایی اهواز پس از حملۀ آمریکا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/671606" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671605">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b35b61078.mp4?token=gGxNRp_b80agWkv2oloM9uL-bWU7U8i6gexRs5l3yMCqJd_su1CjcacFYnQEMy3OwPxPqhR2njjnUneH5CKERkYEmpNCuMf_uyJBMbLeXoeElc4E7a1qie59PS3ueptuvhteT97ahC8fVtcD_v2E3AxJR3-4JTWSOdhuzlLHGDyK-Vbq7Q6yCYwbPSysIqQF8sA119mB846h-2OIdVc7QUi1QKLJ6o05oWTZll_doZIn0eWws5SbU6eMDuYrX2wFVCGxXIr5eS88_OvtnO2TtO2xgxYl9r_yFBNCSjLF5Mtf4IffCNmpIWDSys25OpdKdtDqmBSf_aiI-bjuPX1NjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b35b61078.mp4?token=gGxNRp_b80agWkv2oloM9uL-bWU7U8i6gexRs5l3yMCqJd_su1CjcacFYnQEMy3OwPxPqhR2njjnUneH5CKERkYEmpNCuMf_uyJBMbLeXoeElc4E7a1qie59PS3ueptuvhteT97ahC8fVtcD_v2E3AxJR3-4JTWSOdhuzlLHGDyK-Vbq7Q6yCYwbPSysIqQF8sA119mB846h-2OIdVc7QUi1QKLJ6o05oWTZll_doZIn0eWws5SbU6eMDuYrX2wFVCGxXIr5eS88_OvtnO2TtO2xgxYl9r_yFBNCSjLF5Mtf4IffCNmpIWDSys25OpdKdtDqmBSf_aiI-bjuPX1NjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشارکت کویت در جنگ تحمیلی آمریکا علیه ایران
🔹
رسانه‌های عراقی با انتشار تصاویری،‌ گزارش دادند که کویت با پرتاب موشک از خاک خود به سمت خاک ایران، در جنگ آمریکا علیه جمهوری اسلامی مشارکت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/671605" target="_blank">📅 00:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671604">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
امتحانات دانش‌آموزان بوشهری لغو شد  مدیرکل آموزش و پرورش استان بوشهر:
🔹
با تصمیم ستاد عالی آزمون‌های وزارت آموزش و پرورش امتحانات نهایی روزهای ۲۵ و ۲۷ تیرماه، در این استان لغو شد.  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/akhbarefori/671604" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671603">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4886136147.mp4?token=Hds2xJ8t6LMSslMM13_NX2P48VszR2e37Xdt4w8R4IFTyAnHGtNRcuF9O3lSJEhKBXYIdpXKh6hWUkSe_QjBCPebGgRbuOJIoaFzJqudsFkrPtpdUWSuv_hLH-u9GstDWUIpXz0vbeNoDMIAJfFyG888H4A9ICT-vhY4XQ8XkXIue3OzZ2HWtRZGV-Y1JIp7UgZgSilkPAMhQmLcHcZBosNjZHnDdWYI2-brhJdkCcPTJUDLObwAfXToY8y23GrmkVs8EjlrDBwRoP7BD2-jq0EPBHj3SQ37BL_TNjhToQssxc3ngbn2J6dxigIV3Nh4Wu3vppUpwujJKk-Spbw0KjaH8alJQTSdJmWq0vNgeiaBAMeLM1RFdRYTDmAfseIGVm0_ekF7XcJyOMZcUWSfGNndaiaKAeFuLZKbanpQnXdD3yIOycuO3T18MY2ikDXb1aB9RnbwVrX9LP4LiJVLAn2OcOzbI1Ao69EENzrCS0vkCh5d5Cm0lnMvQm0XBPKBPne7ixPN4SlPqGPnVENFVYttvaqUc5oGXktC8POijvDlehjDlDNo2cf12igl4wQQqwRP-wm--hW7_oYbKeJg6SvnMf5ZZtrY-uAimnu_I2cIMZjky5nrK2_uwxqzkXL3EEmGzwSqb0z1o8dD8wZDtN-BVpwL0aEwqrAorOLUXzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4886136147.mp4?token=Hds2xJ8t6LMSslMM13_NX2P48VszR2e37Xdt4w8R4IFTyAnHGtNRcuF9O3lSJEhKBXYIdpXKh6hWUkSe_QjBCPebGgRbuOJIoaFzJqudsFkrPtpdUWSuv_hLH-u9GstDWUIpXz0vbeNoDMIAJfFyG888H4A9ICT-vhY4XQ8XkXIue3OzZ2HWtRZGV-Y1JIp7UgZgSilkPAMhQmLcHcZBosNjZHnDdWYI2-brhJdkCcPTJUDLObwAfXToY8y23GrmkVs8EjlrDBwRoP7BD2-jq0EPBHj3SQ37BL_TNjhToQssxc3ngbn2J6dxigIV3Nh4Wu3vppUpwujJKk-Spbw0KjaH8alJQTSdJmWq0vNgeiaBAMeLM1RFdRYTDmAfseIGVm0_ekF7XcJyOMZcUWSfGNndaiaKAeFuLZKbanpQnXdD3yIOycuO3T18MY2ikDXb1aB9RnbwVrX9LP4LiJVLAn2OcOzbI1Ao69EENzrCS0vkCh5d5Cm0lnMvQm0XBPKBPne7ixPN4SlPqGPnVENFVYttvaqUc5oGXktC8POijvDlehjDlDNo2cf12igl4wQQqwRP-wm--hW7_oYbKeJg6SvnMf5ZZtrY-uAimnu_I2cIMZjky5nrK2_uwxqzkXL3EEmGzwSqb0z1o8dD8wZDtN-BVpwL0aEwqrAorOLUXzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهانت سناتور آمریکایی به نخست‌وزیر عراق
🔹
در حالیکه سفر نخست وزیر عراق به آمریکا با انتقادات زیادی در محافل عراقی مواجه شده است، «تیم بورشیت»، از اعضای جمهوری‌خواه کنگره، درباره الزیدی اظهار داشت: من همین چند لحظه پیش وقتم را صرف گوش دادن به سخنان نخست‌وزیر عراق کردم، اما او درباره هیچ چیزی نگفت، وقتم را هدر کردم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/671603" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671602">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
آمریکا مدعی حمله به یک نفتکش در مسیر بنادر ایران شد
نهاد تروریستی ستاد فرماندهی مرکزی آمریکا (سنتکام):
🔹
ما امروز یک نفتکش خالی را که قصد داشت به سمت یک بندر ایرانی در خلیج فارس حرکت کند، از کار انداختیم.
🔹
این کشتی هشدارهای متعدد را نادیده گرفت در حالی که تلاش می‌کرد محاصره آمریکا علیه ایران را نقض کند،  در ادامه یک هواپیمای آمریکایی با شلیک موشک به دودکش کشتی، آن را از کار انداخت و از حرکت آن به سمت ایران جلوگیری کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/671602" target="_blank">📅 00:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671601">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlO7XpWHcMdQklQO1Du84m6rfXFd7W5-0yPLJEsmzl_IYXpSFo8z2q-JFDJvUIpUZ60Kuck_dPmYb6vvcC4Ugl3azskVuirXYx-aLaMHSvG0Zt0NCWLi7rLv-ek3DA-HAxGEhN8YHTec7Banb-Ki15QqOLDzzcT5eZB-wL2ZertIhf0cP4NUglK8a0TgOb-rmVrDj8QxjFjP39NKRHF3caA_n4yz_WxIiPS4q5yfTdqBbO1zSmJVPvD6HQnwu_m4P6uUFBBwYxIpd5xp66EY0M3UOjbZ4b_VJcH6nCjHTpJ916DOeOWAU7q3IPJxfsZTN4nTRnAqsCqc2SiWkjs0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل دوم آرژانتین به انگلیس
▪️
آرژانتین ۲_۱ انگلیس
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671601" target="_blank">📅 00:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671600">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UErmjY9srQjHGxRLf61zziBhjxGI63HV4IfG8Pf3dZ9PG61RUsCqO04xG-nS3-OB0xszkCBDvo6zdUNWEhGyfze741dsMdmNyPjU9NHibH4mUaxuELI8q5rAOzxiUtnoYcn2T56G_mBLcI8lsVDP1cTfqGU9uI7OE5zbtEGD1UZF3UddAVPVIYnXL5FWztctw7U2s9joNEckkpUbKRTLiiijXq0TEzOvtOWZz7saQ9TdGisyPOBSdBONuzrP4KP_ioY3yMruWrzn4qgnzndK4d-r_HvWE2zOl5x3RCuQqwshpEfvYBoEzzhYDWEragP1yqgcd_lLWuv1SBJFef47tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کشتی اماراتی دیگر از جنوب تنگۀ هرمز برگشت خورد
🔹
تصاویر ماهواره‌ای نشان می‌دهد که یک کشتی اماراتی ناگهان مسیر خود را از مسیر جنوبی تنگۀ هرمز تغییر داده و برگشته است
🔹
شب‌های گذشته دو کشتی اماراتی هدف حملۀ موشک‌های ایران قرار گرفتند که این هدف‌گیری به توقف صادرات نفت بندر فجیرۀ امارات منجر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671600" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671599">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a1ced86b.mp4?token=jsciiv2hoWLGscddrt65eXxy01Zxw40zII-unxv5WXGgml04oo8pCnxT4Qfwe84o1qyQ1Sh-HUMHOLUPEbzOD_GNdMNXJqE_MEterHjZkdPM3OYT75_Azj_WdVeUn5qJZaWxPLAXj4Kfutn_R7Fwi5_thSifBz6v1EKOjvh3tNnDre4R2h2uwR1W1R1DVBs2QQ_tghR12o-LchX16JlWYsFC6cC82J5BXQiF5XQEhlCvFbOlgd1Y4AhpN0j1BgApceXtBTfbQk6meQkMTuD68O_woF4WI3cFhs4OI22gR5YSylZUvDbO7GgH2aRl3IP0GYrQ7g-KxLQ4OHCHXAJ3_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a1ced86b.mp4?token=jsciiv2hoWLGscddrt65eXxy01Zxw40zII-unxv5WXGgml04oo8pCnxT4Qfwe84o1qyQ1Sh-HUMHOLUPEbzOD_GNdMNXJqE_MEterHjZkdPM3OYT75_Azj_WdVeUn5qJZaWxPLAXj4Kfutn_R7Fwi5_thSifBz6v1EKOjvh3tNnDre4R2h2uwR1W1R1DVBs2QQ_tghR12o-LchX16JlWYsFC6cC82J5BXQiF5XQEhlCvFbOlgd1Y4AhpN0j1BgApceXtBTfbQk6meQkMTuD68O_woF4WI3cFhs4OI22gR5YSylZUvDbO7GgH2aRl3IP0GYrQ7g-KxLQ4OHCHXAJ3_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل دوم آرژانتین به انگلیس
▪️
آرژانتین ۲_۱ انگلیس
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671599" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671598">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b282391b4a.mp4?token=ROZRc9aVuV2J3gNiGRNctWIr7AV4XEJ36s-jS_p_vUO-chy-4wfujRFKyYW99fAw9YNg9CVZW4XIpzi8cWHmw1YinA08hjMEQQD6AtGgWOwg3rTI2XuDj0SFWD6oQLjPYeD2fg5Bb-mwHXVGnNpg_wl4ofu833sOzEl298ASuOdWYGhuBHRCwdCppoawM55n1UNGWoJ4IYPzCHZG0MsPfRYfbiBqMebs6arF9puNEe_p44SVvDfo0v0NZ_VIPdEQQzc3EUeMQUeCUnuIDyP-tuKALxRrI-DDTjrv3ZRNKSsg1Q8FOt4vHJRJ_YwmKkRyCgcMyzutwH9G2a1wj-z3qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b282391b4a.mp4?token=ROZRc9aVuV2J3gNiGRNctWIr7AV4XEJ36s-jS_p_vUO-chy-4wfujRFKyYW99fAw9YNg9CVZW4XIpzi8cWHmw1YinA08hjMEQQD6AtGgWOwg3rTI2XuDj0SFWD6oQLjPYeD2fg5Bb-mwHXVGnNpg_wl4ofu833sOzEl298ASuOdWYGhuBHRCwdCppoawM55n1UNGWoJ4IYPzCHZG0MsPfRYfbiBqMebs6arF9puNEe_p44SVvDfo0v0NZ_VIPdEQQzc3EUeMQUeCUnuIDyP-tuKALxRrI-DDTjrv3ZRNKSsg1Q8FOt4vHJRJ_YwmKkRyCgcMyzutwH9G2a1wj-z3qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قانونگذار آمریکایی: کسی به ترامپ اعتماد ندارد
سث مولتون، نماینده کنگره آمریکا:
🔹
کسی به ترامپ اعتماد ندارد، نه فقط ایرانی‌ها، بلکه هر کس دیگری که طرف درگیری است.
🔹
منظورم این است که ترامپ می‌گوید که صحبت کردن با ایرانی‌ها اتلاف وقت است، اما به نظر من، بیشتر جهان فکر می‌کند که صحبت کردن با او اتلاف وقت است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671598" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671597">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رویترز: کشتی‌ها حاضر نیستند به کمک آمریکا از تنگه هرمز عبور کنند
🔹
هفت منبع در حوزه امنیت دریانوردی و صنعت کشتیرانی گفتند که شرکت‌های کشتیرانی پس از موج جدید درگیری‌ها که نگرانی‌های ایمنی را برانگیخته، از استفاده طرح ارتش آمریکا برای عبور از تنگه هرمز خودداری می‌کنند.
🔹
به گزارش رویترز، از زمان آغاز تجاوز نظامی علیه ایران و بسته شدن تنگه، کشتی‌ها مجبور به استفاده یکی از دو مسیر نزدیک به سواحل ایران یا عمان هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671597" target="_blank">📅 00:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671596">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس درباره ایران: ما قرار نیست فقط بمباران کنیم، بمباران کنیم و باز هم بمباران کنیم
🔹
ما تلاش خواهیم کرد از نیروی نظامی‌مان به‌عنوان یکی از ابزارهای متعددی که در اختیار داریم برای حل این مشکل استفاده کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/671596" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671595">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812957343a.mp4?token=NpoDgtcZ7Q-RXeZJDvNKp8PFGST-yIhiCtrz2E-wnGGmAcRaF0X7P48pKOGmxl3Wf9cFAT1IfBSA2saeszuco2TzNIu73l46RojJaRD45xlbCMNlhtmFyQnacIqy2eeAyUIayLR7V0-J-wrDMJio84GnNRZZzh5Mh8OEfY_-PQ27R5H14IiOkix6gJMIXjNawm2nTElDfOeeI2nabetjelJ1SXRf59HJY3vecaahV72S4HQOCgCGoXY6kS7S5ESYRmp8wO_XrDNajIGHh8vxwWDyfnxhi4yaWHG-0wxjS_i9vNRePLVIieLxawr76JYj-qiD7FA3GawsRvbuJVDCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812957343a.mp4?token=NpoDgtcZ7Q-RXeZJDvNKp8PFGST-yIhiCtrz2E-wnGGmAcRaF0X7P48pKOGmxl3Wf9cFAT1IfBSA2saeszuco2TzNIu73l46RojJaRD45xlbCMNlhtmFyQnacIqy2eeAyUIayLR7V0-J-wrDMJio84GnNRZZzh5Mh8OEfY_-PQ27R5H14IiOkix6gJMIXjNawm2nTElDfOeeI2nabetjelJ1SXRf59HJY3vecaahV72S4HQOCgCGoXY6kS7S5ESYRmp8wO_XrDNajIGHh8vxwWDyfnxhi4yaWHG-0wxjS_i9vNRePLVIieLxawr76JYj-qiD7FA3GawsRvbuJVDCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل تساوی آرژانتین به انگلیس
▪️
آرژانتین ۱_۱ انگلیس
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671595" target="_blank">📅 00:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671594">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYPHROXRg77QaDlZVROa0TdZzT51_gIBQLzlWXtVssTi2xBo4aipIH5-VNwr7RLB9btWKixM4v_6-cCkyqL0swzHjzz2j_AUYh63WSCsSATQHmcmQwclImEGZ2pXv_xydQkGsoWMmUOW9C3l7aY474wKvscwCve2_b11gRr7GYzAkQrN3OTgKGUWsYgWwSBuv9vOCqnhJjK80C-dAbtZhMmkOwzmK4iR8ANSC9eOqGjVhNjvLYJDovS9cY4lLbHyONxIlk7e39mPhV9tvBJQS-xgNMoSaUlZ3zM2yHdW7Ch0ZoNjCP0bKM6yQvhX2tWxiCb3MoC7ZFZ8dX6fkwwgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/671594" target="_blank">📅 00:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671593">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تکذیب حمله هوایی به بوشهر
فرماندار بوشهر:
🔹
تا این لحظه هیچ‌گونه صدا یا حادثه انفجاری در سطح شهر بوشهر گزارش نشده و اخبار منتشرشده در شبکه‌های اجتماعی کاملاً بی‌اساس است.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671593" target="_blank">📅 00:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671591">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
استانداری خوزستان: پس از تهاجم دشمن تروریستی آمریکا به شهر اهواز خساراتی به منازل مسکونی اطراف وارد شده و شیشه برخی منازل شکسته شده است
🔹
تاکنون این حملات تلفات جانی در پی نداشته است./مهر  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/671591" target="_blank">📅 00:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671590">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
تعلیق همه پروازهای فرودگاه اربیل تا اطلاع ثانوی
🔹
فرودگاه اربیل اعلام کرد تمامی پروازهای ورودی و خروجی این فرودگاه تا اطلاع ثانوی به حالت تعلیق درآمده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671590" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671589">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOp_PNU31hqyEgZ6ekdMEL_-K3cBOafHaGoAnSVbcltXR0aYnQMS9rCVvDf0veTYTb8wlFoN07lNdOnRDnSNapPbg9G_zshkFMgXQDjrFEKAr5c55xOy0didbDRHP23vLkBaSsZqu-qiPuWq9BnWqx6WHTC4Iu_zxyBbSJK7B0o-u5SH_m8wEVdG5Ly6QU3IQByNamUFsmCDRbOsA2Zc5lacsBtNOKE77G8c516lv1eyFt_-2UwWSIjMORbmp8Z8uLiLmFeWcxMg2r_8v53bj95lB7oBb5YfNJdxnGca4yxtRowQApgh4Ob6pgiH7QQ-xnZ3XKxhzruuNdaKBS8BFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/671589" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671588">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a7fdcdce.mp4?token=kZVAQkIR269IhkSRypU8IzNPtTgsiPMWZqlalHRVy0yGC_byLQcHhKnWm0K8doW_-UT9mroAeD75x1zfSwuNx2_EWl5Fh7Ahdxbkik5sgCshkVP2XqXnTqTQCsns8fYb3nCcQ73_Kb1QPYi24F4noP5jOHijrJzXuKZz1oXzZrn8HLJqaau8vnmGzIFqXZRpqrNGln-hkv5va3PQggNaeDGmvxidNqBrWzBUyWNt0LxkxW6XPOFdDNyJ2cJcgMjpUQJksRCekd7VoprNpE13hLXZR07q4w7ulDX7LxjDV03tdYPczCtfO11Pvs4uctIcnPnCWVPxOTnbEyw_Ny4KGkr9FjVpvzkXLWsbBKWEfYeYL7psKtDSk-bTtt6Xm6svFLUm5fEmPt2kt_VW19mIFymhghJt8ktyPef4h_Ub_HJIelqDlrzICLJ0gm6NderkkiOWljGwyNlhPEih7O3ZGlmRFEDsEzpP2f63i4I0KZxTWhjZdyYTmCi1zCRgNLADrBShiNypRhHyCbLmYFqakNqD5Nb1am7PUUAIJ9-KV9xRQ88eFfH2wF-Chp40nOl5ihSbFUcAyBfXbPt2VZfUBUtg6YK_osvv4RYKOHgnxNMYM5clf7HSYZbTSQ3kSaJHBCgxWFNQgrkAIJ2_FOXrXRUmcscedYrYD26Eb6XcKA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a7fdcdce.mp4?token=kZVAQkIR269IhkSRypU8IzNPtTgsiPMWZqlalHRVy0yGC_byLQcHhKnWm0K8doW_-UT9mroAeD75x1zfSwuNx2_EWl5Fh7Ahdxbkik5sgCshkVP2XqXnTqTQCsns8fYb3nCcQ73_Kb1QPYi24F4noP5jOHijrJzXuKZz1oXzZrn8HLJqaau8vnmGzIFqXZRpqrNGln-hkv5va3PQggNaeDGmvxidNqBrWzBUyWNt0LxkxW6XPOFdDNyJ2cJcgMjpUQJksRCekd7VoprNpE13hLXZR07q4w7ulDX7LxjDV03tdYPczCtfO11Pvs4uctIcnPnCWVPxOTnbEyw_Ny4KGkr9FjVpvzkXLWsbBKWEfYeYL7psKtDSk-bTtt6Xm6svFLUm5fEmPt2kt_VW19mIFymhghJt8ktyPef4h_Ub_HJIelqDlrzICLJ0gm6NderkkiOWljGwyNlhPEih7O3ZGlmRFEDsEzpP2f63i4I0KZxTWhjZdyYTmCi1zCRgNLADrBShiNypRhHyCbLmYFqakNqD5Nb1am7PUUAIJ9-KV9xRQ88eFfH2wF-Chp40nOl5ihSbFUcAyBfXbPt2VZfUBUtg6YK_osvv4RYKOHgnxNMYM5clf7HSYZbTSQ3kSaJHBCgxWFNQgrkAIJ2_FOXrXRUmcscedYrYD26Eb6XcKA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزادی‌خواهان جهان چطور و در چه محل‌هایی می‌توانند ترامپ را قصاص کنند؟
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/671588" target="_blank">📅 23:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671587">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
استانداری خوزستان: پس از تهاجم دشمن تروریستی آمریکا به شهر اهواز خساراتی به منازل مسکونی اطراف وارد شده و شیشه برخی منازل شکسته شده است
🔹
تاکنون این حملات تلفات جانی در پی نداشته است./مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/671587" target="_blank">📅 23:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671586">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is7_jcs9qBlH0ygUkucuLV3maCVOqmYMi9e-xmbnEFXrc_l5WvEm8i2vrVFmvPLzd9FuMVf_h9Nzm9vEseRFCw-YFal87-zyZ9TnyyV31RJiV-TnrrSKSm5P-EQGCHtiOQ3Obc0AE64PP6xDTEv8mXU-bSJ7U0Vj5TQuFOQBSH_vO1x4I-duNzUrsruxTQUFGcs7uydPEAYrE7FhB-Q5Ez5LCkMnEYEArhG7oJxxYLOj-f8JG5JsNGzCUmGoecXFTypHhqq5K4uRjlaJllAy3PoG96poZwfVV_Pqou7v34U6Z5LcOgSPG-wEFLsp1tkmYSLeI7Mzh0uKu4MeVgX_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان خدمت
🔹
هفت سرباز نیروی زمینی ارتش، در حمله موشکی به پادگان بمپور ایرانشهر به شهادت رسیدند. این حمله که محل استقرار سربازان را هدف قرار داد، شماری از نیروها را نیز مجروح کرد و بار دیگر داغ جنگ را بر دل خانواده‌های ایرانی نشاند. نیروی زمینی ارتش ضمن محکوم کردن این اقدام، اعلام کرد پاسخ این تجاوز در زمان و مکان مناسب داده خواهد شد.
🔹
هشتصدودهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/671586" target="_blank">📅 23:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671585">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a931a74fee.mp4?token=RQZGMbDVNrA5DpIgVV6LsBNIL6iJfd0H94I19B06HHneSm9BMO5HZtc1gv27TWqpnI-XervYD3dkt71epoVmqG9suhXh_niOAFsmCBYMk8uqR14-EFnVYK3mKqlZiry3M3ch1TizQAJ7ttSSLtHiETBSgmzIIQH2Y-31PtZEuUmtd-374B0lpQHcvpwxahA3inrpcWJhkLk6SEjez_dogr4m8DoZJ0NGuczcWko7y2wY2vJbGgohOzIb6Y3bYqbJ2KdXZJP4ZcEYw9apkiHLhycxmcaaR-p7lPZtN9jmjDTtChla3A-tNW4dxSHy_aOubUNjAQ15Ec2R6QYdsW51Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a931a74fee.mp4?token=RQZGMbDVNrA5DpIgVV6LsBNIL6iJfd0H94I19B06HHneSm9BMO5HZtc1gv27TWqpnI-XervYD3dkt71epoVmqG9suhXh_niOAFsmCBYMk8uqR14-EFnVYK3mKqlZiry3M3ch1TizQAJ7ttSSLtHiETBSgmzIIQH2Y-31PtZEuUmtd-374B0lpQHcvpwxahA3inrpcWJhkLk6SEjez_dogr4m8DoZJ0NGuczcWko7y2wY2vJbGgohOzIb6Y3bYqbJ2KdXZJP4ZcEYw9apkiHLhycxmcaaR-p7lPZtN9jmjDTtChla3A-tNW4dxSHy_aOubUNjAQ15Ec2R6QYdsW51Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد آرزوهای خودش را تکرار کرد
رئیس‌جمهور آمریکا:
🔹
ایران به‌زودی شکست می‌خورد؛ آن‌ها خیلی زود شکست خواهند خورد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/671585" target="_blank">📅 23:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671584">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
مالک شریعتی، نماینده مجلس: یارانه بنزین باید به فرد تعلق بگیرد، نه به خودرو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/671584" target="_blank">📅 23:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671583">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e842e1cbcd.mp4?token=pZqrjTWzjd_D6xfsJw-rNhJw4QuaexPzQLh7htC1AlvyIjigRj5Sv70R1mwesy5ksUR4lCvtg2EwosTMvrO5R58o6BcvsykFtuoVfpBkErE-m5R8aDySgePxQMozXMVdAmU32ssYhZQCqLTfIidbmtk4BQOBQ2IH0r42ywg_5OaI6h7pXuaGaNxWBytqnfX3PdYvnC3_7l93fhGloygDUOHexkuEUWuJ3y6ehq9s_F4Q4HH7tk-CM1-QpOa5vYRvBwkse2GR9DM7-qPC4yxae_kBWCcaCcaKacAzDra6vcbLjsJuN5JnpFQrp-nZeSWqxV3hlf_QjftjvJBYhOnmjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e842e1cbcd.mp4?token=pZqrjTWzjd_D6xfsJw-rNhJw4QuaexPzQLh7htC1AlvyIjigRj5Sv70R1mwesy5ksUR4lCvtg2EwosTMvrO5R58o6BcvsykFtuoVfpBkErE-m5R8aDySgePxQMozXMVdAmU32ssYhZQCqLTfIidbmtk4BQOBQ2IH0r42ywg_5OaI6h7pXuaGaNxWBytqnfX3PdYvnC3_7l93fhGloygDUOHexkuEUWuJ3y6ehq9s_F4Q4HH7tk-CM1-QpOa5vYRvBwkse2GR9DM7-qPC4yxae_kBWCcaCcaKacAzDra6vcbLjsJuN5JnpFQrp-nZeSWqxV3hlf_QjftjvJBYhOnmjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل اول انگلیس به آرژانتین توسط گوردون
▪️
آرژانتین ۰ - ۱ انگلیس
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/671583" target="_blank">📅 23:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671582">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
خطوط هوایی، پروازهای خود را به غرب آسیا در پی تشدید تنش آمریکا و ایران لغو کردند
الجزیره انگلیسی:
🔹
شرکت‌های هواپیمایی یونان، کانادا، ایرفرانس و کی ال ام پروازهای برنامه‌ریزی شده خود به دبی، تل آویو و سایر مقاصد در منطقه را متوقف کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/671582" target="_blank">📅 23:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671581">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
شدیدترین حملات به اهواز
🔹
امشب اهواز شدیدترین حملات را از زمان آغاز موج جدید حملات ارتش تروریستی آمریکا، شاهد است./ جماران
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/671581" target="_blank">📅 23:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671580">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
امتحانات دانش‌آموزان بوشهری لغو شد
مدیرکل آموزش و پرورش استان بوشهر:
🔹
با تصمیم ستاد عالی آزمون‌های وزارت آموزش و پرورش امتحانات نهایی روزهای ۲۵ و ۲۷ تیرماه، در این استان لغو شد.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/671580" target="_blank">📅 23:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671579">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=q4Vr2LE0bekR9Eqt3bf3Dh08RjXxhXcFYPyT6tyXy9sgWlhTnI56Ml-Hv4zMN8G6GZdY9tzjuJMwkrSRHWK1aF-ChqMgGTgZA2TOV54ObbczliG7a5k9AgBv5LCInTKGlcQbsUtv5-9E2I8FNMWxkYELfhhtvlQQ82K2qOsXMupW2CUkTu1MMjBJla7r5yVg6Z34C5kwHZvM1K_yrcZq3qzhS3cMMSOTPwsfDRwp600QL6BvIr3ppvQguG9DpZ6exOczrK2IotZaJlFJA06Lb406X02rzaLYnxs02hvbDmhbQ4xy7uXMZ2hMll1zA34AgaJY3GD2vlfEdy19Kx0hhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=q4Vr2LE0bekR9Eqt3bf3Dh08RjXxhXcFYPyT6tyXy9sgWlhTnI56Ml-Hv4zMN8G6GZdY9tzjuJMwkrSRHWK1aF-ChqMgGTgZA2TOV54ObbczliG7a5k9AgBv5LCInTKGlcQbsUtv5-9E2I8FNMWxkYELfhhtvlQQ82K2qOsXMupW2CUkTu1MMjBJla7r5yVg6Z34C5kwHZvM1K_yrcZq3qzhS3cMMSOTPwsfDRwp600QL6BvIr3ppvQguG9DpZ6exOczrK2IotZaJlFJA06Lb406X02rzaLYnxs02hvbDmhbQ4xy7uXMZ2hMll1zA34AgaJY3GD2vlfEdy19Kx0hhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماسی از ایرانی‌ها برای ملاقات دریافت کردم
🔹
خبرنگار:
شما به این نتیجه رسیدید که نمی‌توانید با سپاه پاسداران مذاکره کنید، آیا این به این معنی است که ممکن است آنها را مانند داعش از بین ببرید؟
🔹
ترامپ:
بله. همینطور است. درست زمانی که داشتم به اینجا می‌آمدم، تماسی دریافت کردیم و آنها (ایرانی‌ها) می‌خواهند ملاقات کنند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671579" target="_blank">📅 23:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671578">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
وال استریت ژورنال به نقل از مقامات آمریکایی: گزینه‌ها شامل تشدید حملات و اعزام نیروهای زمینی برای تصرف جزایر ایرانی نزدیک تنگه هرمز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/671578" target="_blank">📅 23:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671577">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
امروز کدام شهرهای ایران هدف حملات آمریکا قرار گرفت؟
👇
khabarfoori.com/fa/tiny/news-3230586
🔹
در ترکیه چه گذشت؟ | جلسه محرمانه ای که باعث شد ترامپ به فکر "جنگ بزرگ" با ایران بیفتد
👇
khabarfoori.com/fa/tiny/news-3230677
🔹
آکسیوس فاش کرد؛ ترامپ در اتاق وضعیت برای حمله گسترده‌تر به ایران چه تصمیمی گرفت؟
👇
khabarfoori.com/fa/tiny/news-3230476
🔹
ترامپ دوباره تهدید کرد: پل‌ها و نیروگاه‌ها را می‌زنیم!
👇
khabarfoori.com/fa/tiny/news-3230437
🔹
طلا و سکه امروز چقدر گران شد؟
👇
khabarfoori.com/fa/tiny/news-3230577
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/671577" target="_blank">📅 23:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671576">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
وال استریت ژورنال به نقل از مقامات آمریکایی: گزینه‌ها شامل تشدید حملات و اعزام نیروهای زمینی برای تصرف جزایر ایرانی نزدیک تنگه هرمز است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/671576" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671575">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
استانداری هرمزگان:  در حملات جدید آمریکا به حوالی بندرعباس هیچ مصدوم غیر نظامی یا خسارت به زیر ساخت‌های مسکونی و تجاری  گزارش نشده است
🔹
هم‌اکنون تیم‌های عملیاتی نیروهای مسلح در مناطق مورد حمله حضور داشته و اوضاع را تحت کنترل دارند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/671575" target="_blank">📅 23:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671574">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ-8S_1SIF7FymyzDBUhspp3vq6tjh2US48hwZ5eCk4Vn6JF9PDeJIsgUFSuPX4LLhEbJ_i-1xfbPTybZzhQVaUWcAGXd6KZAQYmpOCgfzbXVJPT10kvggVzeASrz7EfxtL5rsJmP_4PuJE9tOctsBmr854tS-D0fAPSF0Y5ULXfMMdj7O5AetHW-5pXqj28RWdDfAFlnN2nOIsPoBB89q9tRBQX2GrCckX1to7qg0VgUBbdBIg8VDaRU0nNeTR_WowYOx9Fi0UX_rT8qFJg4Hq3mpwvWvCZrdw4P2ZyY_9q3bAQy41jHRqwTmdmL5xMwBHxoWS0uK5R37JTKz-_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران در میان ۴۰ شهر جهان با بیشترین آلودگی نوری شبانه
🔹
توکیو، نیویورک و سئول در صدر شهرهای دارای بیشترین آلودگی نوری جهان قرار دارند و تهران با امتیاز ۷۵.۲، رتبه ۳۸ را به خود اختصاص داده است.
🔹
آلودگی نوری تهران از شهرهایی مانند ریاض، دوحه، زوریخ، ونکوور بیشتر است.
🔹
آلودگی نوری علاوه بر پنهان کردن آسمان شب، چرخه خواب انسان و زیست بسیاری از گونه‌های جانوری را نیز تحت تأثیر قرار می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/671574" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671573">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
شنیده شدن صدای دو انفجار در کنارک
🔹
از کنارک گزارش داد که دقایقی پیش صدای دو انفجار در مناطقی از این شهرستان شنیده شد.
🔹
براساس این گزارش، هنوز محل انفجارها مشخص نیست و صدای پرواز جنگنده‌های آمریکایی شنیده می‌شود.
🔹
طبق اعلام مسئولان منطقه صدای انفجارها از مناطق بیرونی شهر شنیده شده و اکنون شهر در امنیت و آرامش کامل قرار دارد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671573" target="_blank">📅 23:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671572">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
موسسه اچ اف آی ریسرچ: فعالیت بندر فجیره در امارات عملا متوقف شده است
🔹
با وجود دو ناو هواپیمابر آمریکایی و پوشش هوایی سنگین آمریکا ، بندر فجیره در امارات عملا عملیات خود را متوقف کرده است.
🔹
با توقف فعالیت این بندر، حدود ۶ میلیون بشکه در روز از بازار حذف شده است.
🔹
این بندر اکنون «تقریباً مرده» است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671572" target="_blank">📅 23:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671571">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hda3pRGPjBlwb8zekvS73PVOTqYURAPjaW-hXNN4TCRO3Z2EP1BDV21TSvixaKUmhM5bzoQ6qfQy4Colh7Ujj423yjH0btyl6iF-kGNQiRagra6QaG8RlZ4Z584VC3d6Uy2NCwF1ZVeqhsX0tjoybnYE_5NPMTkg2NOhFgrilRO56EVoTvgtCzGkgesJ3tbGHvH11c_B7QT9ie0HcSy3ho9QvONdPs1yGR3eHT8ogxYC8tfkPMgShXxxfyKJhXNHjtAQxOFzlgHKHSm9D1Ke4qEKL31TGEharjfSfOcD1zHmJXOeVmDU-iN_5EqkcZpkzIB9nhSLxhUaAYWvudnKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهاجرانی: داغ بمپور، داغ همه ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671571" target="_blank">📅 23:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671570">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4wVCMwvRNPrC-Lo9lMEgw4ciAsvwiIJ1IAqxT4OtW_hx5LYKaJQlyKLMhKSThHX2uvtVWYK2d1UBA2zCvE9-iY2_FUKnbW4fMl-Kphvc0hnYV8kLhsxI1I_Qi_gw7ak5kaSatZ21uwejTdVV3ypK6Y9DGVLqlJvImnv55u0-B16mskiLMvX3nVrI53kdnlU-8dyTUE0EqJOMdQPa-g8m4JYy48H1rpmlOjH95rELE3jNKgki-tAmAHxVoqZY6bNja-vJ4EhO9P0wYkH-zSNWvitvpxIRQ1tpROFG5n5fck7AtDvop66KH13l3waqVWFARycj03B_N_5IpwHOjInnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصول مومن بودن از منظر امام علی (ع)
🔹
امام علی (ع) در پاسخی حکیمانه، ایمان را نه فقط باوری قلبی، بلکه ساختاری شانزده‌گانه بر پایه‌ی چهار ستون اصلی (صبر، یقین، عدل و جهاد) و زیرشاخه‌های عملی آن‌ها تعریف می‌کند. این رویکردِ جامع، ایمان را از مرز اعتقاد فراتر…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671570" target="_blank">📅 23:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671569">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
آژیرهای هشدار در بحرین به صدا درآمد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/671569" target="_blank">📅 23:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671568">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار دیگری در اهواز خبر داد
🔹
منشا صدای اخیر هنوز مشخص نیست.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/671568" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671567">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYhUEtCLDMMcUK3DlScF1PPouqMAbLCIcpF0bKPheEt-H-ysLFvqwJQ4DYv5jfOqqC0WxwujNjMCrgi8WfNde1_pg-dxbRxoPGBr6loI0zGIdiciWbPCV3ls4YuySiQT1qohorkbr2MjEWoQpJ6RXwdAknDtlB3kZeLheWmLmd4s6GGgnEoliXpKGnVdxNA3TAQoEsObtVW9gXqGMXcosd6pVYuoGwSqdBJVMo6FvxIrqYPErl4vxdxrOEqkDYQefZ4um2_PUXi0XsRCcHZIZZ2DUSjpTkrHWFaI6lo0We5anv2dZVc2-ZEkcE4jpG43ewk10nrTGdGSv5o8piGhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ترکیه چه گذشت؟/ جلسه محرمانه‌ای که باعث شد ترامپ به فکر "جنگ بزرگ" با ایران بیفتد
🔹
به نظر می‌رسد یک جلسه محرمانه و مرموز باعث شد ایران و آمریکا وارد جنگ با هم شوند و درگیری ها دوباره اوج بگیرد و تفاهم نیز به سرعت از بین برود. این جلسه مرموز مربوط می شود به جلسه مخفی ترامپ با سران ناتو در ترکیه.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3230677</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671567" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671566">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
انفجارها به بحرین رسید
🔹
منایع عربی از شنیده‌شدن صدای انفجار از حوالی پایگاه آمریکایی شیخ  عیسی در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/671566" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671565">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
انفجارها به بحرین رسید
🔹
منایع عربی از شنیده‌شدن صدای انفجار از حوالی پایگاه آمریکایی شیخ  عیسی در بحرین خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671565" target="_blank">📅 23:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671564">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
صدای انفجار در راسک شنیده شد
🔹
دقایقی قبل صدای انفجار در شهرستان راسک استان سیستان و بلوچستان شنیده شد./مهر
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671564" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671563">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af223d3da.mp4?token=BTYgWg8or-7NHyUI7PYV8ClIlBNbCX-yDyYt5w1qiU9ZxboQ2eADJafNA1e1D2sFQXcQ1LvmJIsWwBi3woUpNAfDd1xSao1vBD1yg-yGfaCf1Yis2Ss1spEk6zQQ-g23Dzo_SszJIslvwUsPniGED9upK-nI914RuE0DYeEcBw9S9ptISDtP8xbs_81kel3q64SvqwO-K_NxhxSFeRlqhE5PhG2iMLctM9fhFzRJq0iOGKt8K0spttSHoaGRhEPvbxs5n9FkvDkY9NcYY6HDnX-tpemkVgQJFHero2nflQ_SbdJx01earqj5LotMc_gBETSukbcJ_Y9nlLtTITMkYUQbod7j_DtOe7e-diuRe5TBMtO2LY1ibMGFmjifwVvvjFgfiOER3NCCUin2_V9nglba5Hq7vaKyUJMXz3ahSflScj_nl8pULHl8D_swCrpE29KYspe_8mR-HgKS8rovL_WUI3vdGacJE7Ax8ik96RvvYQO0P3oXQSPJmqmF2-TTMhLLaB4wtcsSyv9OZDvgIrKjJdXj4b-dMJjRE23bYsJ5puqWfph9g4ATSdo_fW2Dlcq-Hzev-09ePzicSWK4krbBNilP1n-kgjtJfykVJ1fbOiuauwAYFNHrpLA1GeG309rxN3QdaaBNChgd42WJw91Aar1n94fuFIbPH93xXVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af223d3da.mp4?token=BTYgWg8or-7NHyUI7PYV8ClIlBNbCX-yDyYt5w1qiU9ZxboQ2eADJafNA1e1D2sFQXcQ1LvmJIsWwBi3woUpNAfDd1xSao1vBD1yg-yGfaCf1Yis2Ss1spEk6zQQ-g23Dzo_SszJIslvwUsPniGED9upK-nI914RuE0DYeEcBw9S9ptISDtP8xbs_81kel3q64SvqwO-K_NxhxSFeRlqhE5PhG2iMLctM9fhFzRJq0iOGKt8K0spttSHoaGRhEPvbxs5n9FkvDkY9NcYY6HDnX-tpemkVgQJFHero2nflQ_SbdJx01earqj5LotMc_gBETSukbcJ_Y9nlLtTITMkYUQbod7j_DtOe7e-diuRe5TBMtO2LY1ibMGFmjifwVvvjFgfiOER3NCCUin2_V9nglba5Hq7vaKyUJMXz3ahSflScj_nl8pULHl8D_swCrpE29KYspe_8mR-HgKS8rovL_WUI3vdGacJE7Ax8ik96RvvYQO0P3oXQSPJmqmF2-TTMhLLaB4wtcsSyv9OZDvgIrKjJdXj4b-dMJjRE23bYsJ5puqWfph9g4ATSdo_fW2Dlcq-Hzev-09ePzicSWK4krbBNilP1n-kgjtJfykVJ1fbOiuauwAYFNHrpLA1GeG309rxN3QdaaBNChgd42WJw91Aar1n94fuFIbPH93xXVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکرار و تاکید انتقام در پیام‌های رهبر معظم انقلاب
حجه‌الاسلام قمی، رئیس سازمان تبلیغات اسلامی:
🔹
رهبر انقلاب در اولین پیام، پیام شهادت دکتر لاریجانی و پیام به مناسب چهلم شهادت امام شهید، به انتقام و خونخواهی تاکید کردند/ این یعنی انتقام حتمی و قطعی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671563" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671562">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان
🔹
هم‌اکنون صدای پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان شنیده می‌شود.
🔹
مردم منطقه صدای اصابت ۳ موشک و انفجار را مناطقی از شهر چابهار شنیدند اما هنوز محل دقیق این انفجارها مشخص نیست.
🔹
مسئولان امنیتی و انتظامی گفتند که تیم های عملیاتی به محل های انفجار اعزام شده‌اند و به زودی اطلاعات دقیق به مردم اعلام خواهد شد./تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/671562" target="_blank">📅 23:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671561">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای انفجارهایی در بندرعباس  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671561" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671560">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
۴ نقطه در اطراف شهر اهواز مورد تهاجم دشمن آمریکایی قرار گرفت
معاون استاندار خوزستان:
🔹
دقایقی پیش ۴ نقطه در اطراف  شهر اهواز توسط دشمن آمریکایی مورد تهاجم قرار گرفت.
🔹
تاکنون این حملات تلفات جانی در پی نداشته است. /مهر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671560" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671559">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
پاداش میلیاردی برای سرمربی تیم ملی
🔹
مهدی تاج، رئیس فدراسیون فوتبال، مبلغ ۱۴۰ میلیارد تومان از پاداش ۳۵۰ میلیاردی اهدایی از سوی رئیس‌جمهور را به امیر قلعه‌نویی اختصاص داد. همچنین تیم ملی ایران برای حضور در جام جهانی، حدود ۱۰ میلیون دلار نیز از فیفا دریافت خواهد کرد. در همین زمینه، یکی از روزنامه‌ها با تیتر پاداش برای هیچ به این اقدام واکنش نشان داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671559" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671558">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40564f6cd.mp4?token=FW1FvLbbg6vAb66JK2HITP_ol9H4nHhVjg9ILk66ux4lMQj8rGx8yeLTPEbBMd_aFYTvO7sWL8EP-Tw8CSexH44iBfoqIZ7XCiBehqBpLBQPc5FNla32UF5OgZnhNwAl82eC44a3isVfzRPq6dvzR4bpUIc8wiftI_QiM6RAPECVDwcNFYQqAf9FEFzf_CwC7lOT-10lvvU7VtC9PhqkH3vFYt6K9cOJ3dChk-2PyTlF7rSJvf9R4MwxFWmXAQnKiGqJE8acM3d12urjYnQV8eW7Y7dFP3voHM3199Zhmfj4G2mLmhVgUNbfV54fMZdfddYk5kyoLmU2cgV2JzrEPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40564f6cd.mp4?token=FW1FvLbbg6vAb66JK2HITP_ol9H4nHhVjg9ILk66ux4lMQj8rGx8yeLTPEbBMd_aFYTvO7sWL8EP-Tw8CSexH44iBfoqIZ7XCiBehqBpLBQPc5FNla32UF5OgZnhNwAl82eC44a3isVfzRPq6dvzR4bpUIc8wiftI_QiM6RAPECVDwcNFYQqAf9FEFzf_CwC7lOT-10lvvU7VtC9PhqkH3vFYt6K9cOJ3dChk-2PyTlF7rSJvf9R4MwxFWmXAQnKiGqJE8acM3d12urjYnQV8eW7Y7dFP3voHM3199Zhmfj4G2mLmhVgUNbfV54fMZdfddYk5kyoLmU2cgV2JzrEPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به ترور شدن توسط ایران فکر نمی‌کنم
خبرنگار
:
🔹
تهدیدهایی علیه جان شما از سوی ایران وجود داشته است... آیا از ظاهر شدن در چنین موقعیت‌هایی احساس امنیت می‌کنید؟
🔹
ترامپ:
من حتی به آن فکر هم نمی‌کنم، چون اگر فکر کنم، خیلی مؤثر نخواهم بود.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671558" target="_blank">📅 23:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671557">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
مهر: شنیده شدن صدای انفجارهایی در بندرعباس
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/671557" target="_blank">📅 23:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671556">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91ae1b4fe0.mp4?token=dE1cI5Tzr43-bE9tzl1sxGDG_8RjDy0gK0YtBKKIItHB8PbpJCZF87-H9tmwQI7lxq4MmDNPDIRtfXhtYFtir8w2MxxautnmImoM5b93fycPVOCTQ561e_RlB2bniMxnSL0A-hIZgdvHyAWZGKrJPre4UmZOxr5FnHqo2DOW_0OjLgncNvSJf7kwGp5gVxgjhRCJ5kEDVCmqLLFDIAXz3bUlU8dQ3WJKPejkVktf9xve1rT-z8Bez3rih_6lZrSs2tUqZST_Hb4H8q8TIiyD6xN9GE9zFF67hXNkAohL0axTOpy8uXu1zXOjmaohzeIxYBd4BAG04BfYYFsH3M7hlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91ae1b4fe0.mp4?token=dE1cI5Tzr43-bE9tzl1sxGDG_8RjDy0gK0YtBKKIItHB8PbpJCZF87-H9tmwQI7lxq4MmDNPDIRtfXhtYFtir8w2MxxautnmImoM5b93fycPVOCTQ561e_RlB2bniMxnSL0A-hIZgdvHyAWZGKrJPre4UmZOxr5FnHqo2DOW_0OjLgncNvSJf7kwGp5gVxgjhRCJ5kEDVCmqLLFDIAXz3bUlU8dQ3WJKPejkVktf9xve1rT-z8Bez3rih_6lZrSs2tUqZST_Hb4H8q8TIiyD6xN9GE9zFF67hXNkAohL0axTOpy8uXu1zXOjmaohzeIxYBd4BAG04BfYYFsH3M7hlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایرانی‌ها می‌خواهند توافق کنند
شیطان زرد:
🔹
آنها آدم‌های بدی هستند اما می‌خواهند توافق کنند
🔹
می‌توانم به شما بگویم که آنها می‌خواهند توافق کنند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671556" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671555">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de1acb88a.mp4?token=dcLUYs4-0rVSE6j8_38x2NYq_7yE04aysTK_BKW0j0hBQjcf_Hgq9bfamxkHlwSIpumo2Ds9GW6tIZeSICqONvffQQAMXAFA7qhZv8JDReD73exCcysx2oeYwaK0v-7Cu2VMIm-dUPUaOxc6drAhXR60PXGLzxwvATH0EzuQyppkqHo460nQ47fXwLWVi9Y51s2czQhKnCLTZUfHFe8L6SKcFok65hCnJg59R4iiowWDTprwTJDJkFd15w37dS_5S8r_GrZDBH3ZXz4RBHjUoCOuNqz-iF4ucC30eUDZoPf50YaL_0Wk0u9FZJ_pGhHREqzjkuLiw4FxEl5kO-UPOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de1acb88a.mp4?token=dcLUYs4-0rVSE6j8_38x2NYq_7yE04aysTK_BKW0j0hBQjcf_Hgq9bfamxkHlwSIpumo2Ds9GW6tIZeSICqONvffQQAMXAFA7qhZv8JDReD73exCcysx2oeYwaK0v-7Cu2VMIm-dUPUaOxc6drAhXR60PXGLzxwvATH0EzuQyppkqHo460nQ47fXwLWVi9Y51s2czQhKnCLTZUfHFe8L6SKcFok65hCnJg59R4iiowWDTprwTJDJkFd15w37dS_5S8r_GrZDBH3ZXz4RBHjUoCOuNqz-iF4ucC30eUDZoPf50YaL_0Wk0u9FZJ_pGhHREqzjkuLiw4FxEl5kO-UPOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ایرانی مقیم خارج از کشور: ایرانیان مقیم خارج جنگ‌طلب نیستند، ما نمی‌خواهیم کشورمان بمب بخورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671555" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671554">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psyIWUT8GHuZ9TD7QUJpfYX3QI0dSCH2G2XvSqIB6ACRM34s5pDm8japkslBKDtmFWdmDd-LTsKN4339VN8SlebELrjQCCvrKpLAyyDHzsO7nvTg_7FDuEn2WN3unxOQfwaDkQAI6t2ifmU6dhKJ14kQe-pQwFEucYMwuaelhzQfcRWvcNOJTpxi2TeTg_bxqVJe82XuTUwU8nLIUtBioZ098qF02YCqDFYjgCLgjmiffm0ueTQcIw7vKPXWotNsSQokLARKjtNLMZnf1dFJ436kqVbKmltymmDSvMsrbuLL1iKa_Avc9fYJRsw18wgvL8PMzLwTWyg69gEqc3wJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای بوئینگ‌های مرموزی که در مسیرهای جنگی پرواز می‌کنند
🔹
تحقیقات رویترز نشان می‌دهد شرکت‌هایی تحت کنترل یک کهنه‌سرباز نیروهای ویژه ارتش آمریکا، چند فروند هواپیمای قدیمی بوئینگ را در مسیرهایی به کار گرفته‌اند که به شبکه‌های تأمین نیروهای واکنش سریع سودان مرتبط بوده است؛ گروه شبه‌نظامی‌ای که به ارتکاب جنایات گسترده، از جمله اتهام نسل‌کشی در دارفور، متهم شده است.
در خبرفوری بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3230659</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671554" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671553">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر اتحادیه املاک تهران: برخلاف گفته دولت، اجاره‌بها ۳۰ تا ۵۰ درصد افزایش پیدا کرده است
سعید لطفی، دبیر و عضو هیئت رئیسه اتحادیه املاک تهران در
#گفتگو
با خبرفوری:
🔹
اجاره‌بها تابعی از قیمت تمام شده مسکن است، با توجه به اینکه افزایش قیمت مسکن  داشتیم، قطعا اجاره‌بها هم نسبت به سال گذشته افزایش پیدا می‌کند.
🔹
برخلاف گفته دولت مبنی بر اینکه نسبت به پارسال فقط ۲۵ درصد افزایش اجاره‌بها مجاز است، به‌طور میانگین بین ۳۰ تا ۵۰ درصد افزایش قیمت در اجاره‌بها اتفاق افتاده که این موضوع با توافق میان مالک و مستأجر انجام می‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671553" target="_blank">📅 22:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671552">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
صدای چندین انفجار شدید در اهواز شنیده شد/ جماران  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671552" target="_blank">📅 22:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671551">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZkvHG0tv1xTAs138gOCgFQDM-8kdYLO9F8hk3KUUp4wmGrOoEVGnAVTQ56mKx9mM8rRTqnB3jiKQl5t-XpaxrFn6h9kHsre1xkprlef6VuCgffjaJWKE4L05tUr4MJij_xptWAhDpUzF1A1H5B_NWEokHoTW6ltVXPIDK12M3SMojAjH6iOkkVzYOzTtvzM5kZr_kIXw1fpZ_ZGRuPQWm4R_hUIxaMgYhOCEi7V8cNkUPmLQUV_j3HR955xjYO0zVZcakfM03HnefAvjDM76KbJXxRZshrS1uUikdzsNqZ8xdQMESEOtlHm2u1I2o1eLFH7967kXsQn38kNbJgqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام دقایقی قبل از آغاز مجدد تجاوز نظامی به خاک ایران خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671551" target="_blank">📅 22:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671550">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
منابع عربی: از دقایقی پیش صدای چند انفجار در کویت شنیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671550" target="_blank">📅 22:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671549">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
صدای سه انفجار در چابهار شنیده شد/مهر
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671549" target="_blank">📅 22:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671548">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
آمریکا از شهروندانش خواست به ایران و افغانستان سفر نکنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671548" target="_blank">📅 22:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671547">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
صدای چندین انفجار شدید در اهواز شنیده شد/ جماران
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671547" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671546">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c8e99b02.mp4?token=JlIO2-nSfSjmLJp2fMBXpTkjFlUvuuNn4tzFWtJRh9IfmSMUtga6_PaAuNGyzsba9KAEHOEQ1mNdDmhu_9UX0lFl-qVNFSjWtBsFI-KGhViArXzQHUzYz_WuPGnxlxz9FUw92pakQ0MNo6CWlXPLhf5eohcASVlC8BRaJsjIVlHEKRLb7i3dPSFhXz0fDLBOVAvt_iemCUhrO5wprxT2eJfbH3-MdjOyZKdVbASfKs5CT-11CsO1eX_FGBPEebHcrJdjDnAXQKGilyIp629N9eS30-RwXe9MT3RVVhO0SmBlrxA3Mud6bTT-VByx71UEyDyTitSk04zQkaiJ0_nb2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c8e99b02.mp4?token=JlIO2-nSfSjmLJp2fMBXpTkjFlUvuuNn4tzFWtJRh9IfmSMUtga6_PaAuNGyzsba9KAEHOEQ1mNdDmhu_9UX0lFl-qVNFSjWtBsFI-KGhViArXzQHUzYz_WuPGnxlxz9FUw92pakQ0MNo6CWlXPLhf5eohcASVlC8BRaJsjIVlHEKRLb7i3dPSFhXz0fDLBOVAvt_iemCUhrO5wprxT2eJfbH3-MdjOyZKdVbASfKs5CT-11CsO1eX_FGBPEebHcrJdjDnAXQKGilyIp629N9eS30-RwXe9MT3RVVhO0SmBlrxA3Mud6bTT-VByx71UEyDyTitSk04zQkaiJ0_nb2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیامبر از انتقام مسلمانان نمی‌گذشت
محمدحسن رجبی‌دوانی، پژوهشگر تاریخ اسلام:
🔹
اگر عباس عموی پیامبر به ابوسفیان نمی‌گفت قبل از دستیابی پیغمبر توبه کند و اسلام بیاورد، پیامبر به محض دستیابی به او به انتقام مسلمانان او را می‌کشت.
🔹
همان‌طور که بقیه را دنبال کرد و گفت اگر به پرده خانه کعبه آویزان شده بودند آن‌ها را بکشید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671546" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671545">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
بازگشت وزیر امور خارجه به تهران
🔹
عراقچی که بعد از ظهر امروز چهارشنبه برای ابراز تسلیت به دولت قطر به مناسبت درگذشت امیر سابق این کشور، به دوحه سفر کرده بود، بعد از دیدار با شیخ تمیم بن حمد آل ثانی امیر قطر و شرکت در مراسم مزبور، شامگاه چهارشنبه به تهران بازگشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671545" target="_blank">📅 22:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671544">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
از کسانی که مذاکره با ایران را رد می‌کنند، راهکار جایگزین می‌خواهم  ونس، معاون رئیس‌جمهور آمریکا:
🔹
نیروی نظامی یک ابزار است، اما دیپلماسی ابزار دیگری است. من از آمریکایی‌هایی که می‌گویند نمی‌توان با ایرانی‌ها مذاکره کرد، ناامید شده‌ام. پس پیشنهاد شما برای…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671544" target="_blank">📅 22:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671542">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1833a97fe.mp4?token=PGQ0paRx_rhQcBMv-9Y9D3_QuDzVz_-V47iOR1kwvfMk6KGUHJy7WHWfApblStjwvMrlAaXK77AFpKwLWtqnAbs1Ew69qsqMquDqTi_3v-6DuvJWkraVck817soozfs1VLkMCA2oT21yXxnzHc9--qJFenblnGI162UrI6GyFWtTzt4vZzC4X4dQAuE6XQlUkqLWxIhWvIivno6xyyNeEaEk1xweikLdZ9NSbcEwZewK56nKdQp7TfFNej9SdC6Cp_vb8W5_V_e9ImaJ3rODi8xGDBzjmhT7hqLE6ANg2qYj_ccsT4xqTVMrB4R6EMBH28fziOAw3Vzpo8GxTmp7ZFXBMsWdEz8bZdEJvsg_Mn7YAHqgxFJsOwJFKT0PxEyJvkazbmznBOdyAlzehvK6ZGz9LbI_87PIMlDvvGxIBioJVgjLTwTljAXQ-DS4seRMTcW4g5WgoPMYTrYK1VxtKkdKkq8EPLUMZ82XOl5Jbcep4d3aS848eUsQ1yR42yrl_DquZQOzqmlE-rSxxuxb7-VpSZgjtbHy8_gIEkMzs5QhKAxdyVG5Nt2T5-RI0UC6b9CDo2FGVgdbon7s_WkQ-S6D-RPhLVXjUTo59ofCuJkTJEXmFMdS2z6bY8QzbdneUC1w7ymqa3P_xHE7r4uUpjeUeKJHj5g8wYQkBw5M-0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1833a97fe.mp4?token=PGQ0paRx_rhQcBMv-9Y9D3_QuDzVz_-V47iOR1kwvfMk6KGUHJy7WHWfApblStjwvMrlAaXK77AFpKwLWtqnAbs1Ew69qsqMquDqTi_3v-6DuvJWkraVck817soozfs1VLkMCA2oT21yXxnzHc9--qJFenblnGI162UrI6GyFWtTzt4vZzC4X4dQAuE6XQlUkqLWxIhWvIivno6xyyNeEaEk1xweikLdZ9NSbcEwZewK56nKdQp7TfFNej9SdC6Cp_vb8W5_V_e9ImaJ3rODi8xGDBzjmhT7hqLE6ANg2qYj_ccsT4xqTVMrB4R6EMBH28fziOAw3Vzpo8GxTmp7ZFXBMsWdEz8bZdEJvsg_Mn7YAHqgxFJsOwJFKT0PxEyJvkazbmznBOdyAlzehvK6ZGz9LbI_87PIMlDvvGxIBioJVgjLTwTljAXQ-DS4seRMTcW4g5WgoPMYTrYK1VxtKkdKkq8EPLUMZ82XOl5Jbcep4d3aS848eUsQ1yR42yrl_DquZQOzqmlE-rSxxuxb7-VpSZgjtbHy8_gIEkMzs5QhKAxdyVG5Nt2T5-RI0UC6b9CDo2FGVgdbon7s_WkQ-S6D-RPhLVXjUTo59ofCuJkTJEXmFMdS2z6bY8QzbdneUC1w7ymqa3P_xHE7r4uUpjeUeKJHj5g8wYQkBw5M-0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امنیتی‌ترین فیلم سینمای ایران رفع توقیف شد
🔹
آغاز اکران فیلم سینمایی «لباس شخصی» در سینماها
🔹
فیلم سینمایی «لباس شخصی» به کارگردانی امیرعباس ربیعی و تهیه کنندگی حبیب والی‌نژاد
🔹
#لباس_شخصی
روایتی از پیچیده‌ترین پرونده امنیتی بعد از انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671542" target="_blank">📅 22:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671541">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای ترامپ: سوریه در تعامل با حزب الله دقیق‌تر از اسرائیل عمل خواهد کرد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671541" target="_blank">📅 22:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671540">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
تیم مذاکره‌ کننده ایرانی به اسنادی دست یافته است که نشان می‌دهد افرادی نزدیک به دونالد ترامپ، از جمله استیو ویتکاف و جرد کوشنر، با بهره‌ گیری از اخبار محرمانه حول مذاکرات و جنگ، بازارهای مالی را تحت تأثیر قرار داده و سودی بالغ بر ۹ میلیارد دلار کسب کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671540" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671539">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
صدای انفجارها بار دیگر در سلیمانیه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671539" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671538">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14afdc3e6d.mp4?token=p3ljGY466YhZHOjaxjUbBeYqdw23yQUXii_zrjjsf9RBVXdjt3Lwr9UpqbOroeHPlwHHF9bzFJk80FgD8EzCtU8fpmR6_hyS_3zMKsH2POeAwIPF6YavHHgXcBGTsPYmmW44oWbsSbtAjSbAqg_3EwCNESKA1oh_7od_oBKqBV2Pnd7f4zIxaoVF9ZfCNOsN2eave-Dkc6LS8t_KJb0N2DeAIoPvCfVGTZDUw-IgTifoCKAukepOBp2MT95TcFYpynHlqkkp7XvIo5GuEPUhhV396XloZbwn6wPIi3OaexiAWp0ZiR9mLpHieumPx99D-KMdc3Jwq4kkvKvGLmyFLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14afdc3e6d.mp4?token=p3ljGY466YhZHOjaxjUbBeYqdw23yQUXii_zrjjsf9RBVXdjt3Lwr9UpqbOroeHPlwHHF9bzFJk80FgD8EzCtU8fpmR6_hyS_3zMKsH2POeAwIPF6YavHHgXcBGTsPYmmW44oWbsSbtAjSbAqg_3EwCNESKA1oh_7od_oBKqBV2Pnd7f4zIxaoVF9ZfCNOsN2eave-Dkc6LS8t_KJb0N2DeAIoPvCfVGTZDUw-IgTifoCKAukepOBp2MT95TcFYpynHlqkkp7XvIo5GuEPUhhV396XloZbwn6wPIi3OaexiAWp0ZiR9mLpHieumPx99D-KMdc3Jwq4kkvKvGLmyFLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از کسانی که مذاکره با ایران را رد می‌کنند، راهکار جایگزین می‌خواهم
ونس، معاون رئیس‌جمهور آمریکا:
🔹
نیروی نظامی یک ابزار است، اما دیپلماسی ابزار دیگری است. من از آمریکایی‌هایی که می‌گویند نمی‌توان با ایرانی‌ها مذاکره کرد، ناامید شده‌ام. پس پیشنهاد شما برای اینکه مردم را از تیراندازی به کشتی‌ها در تنگهٔ هرمز بازداریم، چیست؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671538" target="_blank">📅 22:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671537">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
مخالفت AFC با درخواست فدراسیون فوتبال ایران
،
گل گهر نماینده ایران در آسیا شد
🔹
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671537" target="_blank">📅 22:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671536">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90873cbacb.mp4?token=SdL6-okPRE7o6F3n7RtUGMqrEWnTRpwZTOivq2bXxwmQh5O6Quykcjf-RQmjwIufIg4fuCi5tjFwyTs7MvOesXrcXNrGnwyv3hhV0_MEpTKO8Vhq73PSRgiaUbvwCBzBRxO0diUMhcopHb9s_RSU6an6NlMyxFvHV9-qL1ITJJvrum6SPjPATV19lQQxuPeJqHsG77u9NMlDOy3BpwBR-2Mnm4ne6MxqF4iR1aM-l1kTnhEpDxr2WkzLX4JokBq-nUbKrTgbYKgx1zGnBK5yUgPui59_TUFI9vtvy_MqxXoW5t9Rgk0Gli0eBzsHtEpdaErI8xsyxrEHAQUJPuSLZZfxAM3nYHTxMYlpeW5DzVum6rlTB1JOuA9PFw6eekO-ti7ABPDJW5hC60D2KIHELl6WyxC7EoTMhGjY_mhZEWkHsA1fEmCo1gK2dycxIkkp8kmPv9Ol8NXwnifm91yZr_r_u2J1vyo9fnnxywsjKl1DsW0D56QliR8HaP-5KzNiVaa14aaFEaWpEo-pSOWBDDRC8UXTDOUeu-oBPr4J-LNKoMpAHlqBHNn6F339t6Sjrk23TtTzokhC5_TtT2jPaEIOTDA67-Ir8G3oFHCSaoFEQ_wufxEYkXkbWNHWTANzm4581RK-yTgReJRjCo7rbyw2O_h7CjZjW7mw1LlDZSY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90873cbacb.mp4?token=SdL6-okPRE7o6F3n7RtUGMqrEWnTRpwZTOivq2bXxwmQh5O6Quykcjf-RQmjwIufIg4fuCi5tjFwyTs7MvOesXrcXNrGnwyv3hhV0_MEpTKO8Vhq73PSRgiaUbvwCBzBRxO0diUMhcopHb9s_RSU6an6NlMyxFvHV9-qL1ITJJvrum6SPjPATV19lQQxuPeJqHsG77u9NMlDOy3BpwBR-2Mnm4ne6MxqF4iR1aM-l1kTnhEpDxr2WkzLX4JokBq-nUbKrTgbYKgx1zGnBK5yUgPui59_TUFI9vtvy_MqxXoW5t9Rgk0Gli0eBzsHtEpdaErI8xsyxrEHAQUJPuSLZZfxAM3nYHTxMYlpeW5DzVum6rlTB1JOuA9PFw6eekO-ti7ABPDJW5hC60D2KIHELl6WyxC7EoTMhGjY_mhZEWkHsA1fEmCo1gK2dycxIkkp8kmPv9Ol8NXwnifm91yZr_r_u2J1vyo9fnnxywsjKl1DsW0D56QliR8HaP-5KzNiVaa14aaFEaWpEo-pSOWBDDRC8UXTDOUeu-oBPr4J-LNKoMpAHlqBHNn6F339t6Sjrk23TtTzokhC5_TtT2jPaEIOTDA67-Ir8G3oFHCSaoFEQ_wufxEYkXkbWNHWTANzm4581RK-yTgReJRjCo7rbyw2O_h7CjZjW7mw1LlDZSY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر روبرتو پیاتزا درباره کت‌وشلوار پوشاک زاگرس:
«کت‌وشلوار خیلی عالی و کاملا مشابه استایل ایتالیایی است»
«زاگرس؛ تلفیق شخصی‌دوزی صنعتی و دقت در اجرا برای ارائه‌ی محصولی با استاندارد بین‌المللی»
📌
مشاهده در اینستاگرام:
https://zgrs.ir/zi
🌐
وب‌سایت:
www.zagrospoosh.com
📞
02143064000 (داخلی 330)</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671536" target="_blank">📅 22:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671535">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
احضار سفیر انگلیس در تهران به وزارت امور خارجه
🔹
در پی اقدام ناموجه دولت انگلیس در قرار دادن نام سپاه پاسداران انقلاب اسلامی در ذیل قانون مقابله با تهدیدات دولتی، هوگو شورتر، سفیر انگلیس در تهران، امروز چهارشنبه توسط علیرضا یوسفی دستیار وزیر و مدیرکل اروپای غربی وزارت امور خارجه، به وزارت امور خارجه احضار و مراتب اعتراض شدید جمهوری اسلامی ایران نسبت به این اقدام خصمانه به وی ابلاغ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/671535" target="_blank">📅 22:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671534">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b8c2d1a0.mp4?token=A5pQFETtnT3ZFTyC0kKB0YdPx5aqce2KXpyccnfceHyrsPzwXa2p4IObEsfRcvU780n7N5o4V8WsLsbrQq_xe4onnNPrvz-cqJqaPPH2mq1FcOQ3paFOsBka2jFi6AUXDXw7pIqQn_OMy-1SbDSgyPPRYYfP-mBhL9Hj3aHd1c9GuggasjsCFMGHlYZjOjtSWhWBKR_imp01ni2vJD2iY7LlFz-S_XXXDzOCeB6fB1TVvIe-bSddAYzCUWM9TyHlyjQjalOYg9fVM5L-UhrKU0QycBkCXnGsfgb2s3ox8o0WKqm7c_HEPfHxSUj4wq3UIqbgmTb1RUd4wP0plY94qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b8c2d1a0.mp4?token=A5pQFETtnT3ZFTyC0kKB0YdPx5aqce2KXpyccnfceHyrsPzwXa2p4IObEsfRcvU780n7N5o4V8WsLsbrQq_xe4onnNPrvz-cqJqaPPH2mq1FcOQ3paFOsBka2jFi6AUXDXw7pIqQn_OMy-1SbDSgyPPRYYfP-mBhL9Hj3aHd1c9GuggasjsCFMGHlYZjOjtSWhWBKR_imp01ni2vJD2iY7LlFz-S_XXXDzOCeB6fB1TVvIe-bSddAYzCUWM9TyHlyjQjalOYg9fVM5L-UhrKU0QycBkCXnGsfgb2s3ox8o0WKqm7c_HEPfHxSUj4wq3UIqbgmTb1RUd4wP0plY94qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوه قضاییه با قاتلان شهید عجمیان و شهید آرمان چه کرد؟
🔹
دکتر محمدحسن رجبی‌دوانی، پژوهشگر تاریخ اسلام در محفل الهیات انتقام از نرمش قوه قضاییه در مقابل مفسدان داخلی گفت؛ افرادی که باید به قصاص و مجازات می‌رسیدند تا در نهایت بتوان خونخواهی و انتقام از امام امت و شهدا را در خارج از مرزها پیگیری کرد؛ اما خیلی از آن‌ها به سزای اعمال خود نرسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/671534" target="_blank">📅 22:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671533">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e727526ccb.mp4?token=hb-uxtZOChNVsf2Ix9UfhgxyZDPxZovc4wTHcDgmEaNuh9WEDa6kUZVBK4Jp8vqYVBKXQi0u1x8kFpMXKwTT9NvaBK-NpyAhVeASdRtvVYNv0fm0ku1VLth-yW7Jgh6T43gM_T5v2KrLvxI4XereRrfhGiG0_DK-qxP_SP724jwuRAvxwFRAL3n-jhuLnqYNLmMs6OavPYxBg23A5HNtIoM__ir-VKNXsPo8bZn90Ro_rGEnAB3E8AqzS2rTBxfVCdHmOUrO7j0fX5z3VXpJNm5GFbu1cuxDTFf0H_kVfjxS0hg-AICtOxCBr3abITcz2bk7QDvzl9cRfEU0CswRXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e727526ccb.mp4?token=hb-uxtZOChNVsf2Ix9UfhgxyZDPxZovc4wTHcDgmEaNuh9WEDa6kUZVBK4Jp8vqYVBKXQi0u1x8kFpMXKwTT9NvaBK-NpyAhVeASdRtvVYNv0fm0ku1VLth-yW7Jgh6T43gM_T5v2KrLvxI4XereRrfhGiG0_DK-qxP_SP724jwuRAvxwFRAL3n-jhuLnqYNLmMs6OavPYxBg23A5HNtIoM__ir-VKNXsPo8bZn90Ro_rGEnAB3E8AqzS2rTBxfVCdHmOUrO7j0fX5z3VXpJNm5GFbu1cuxDTFf0H_kVfjxS0hg-AICtOxCBr3abITcz2bk7QDvzl9cRfEU0CswRXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای انفجارها بار دیگر در سلیمانیه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/671533" target="_blank">📅 22:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671532">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سی‌بی‌اس: مقامات دفاعی ایالات متحده در حال بررسی طرح‌های اضطراری برای اقدام نظامی احتمالی علیه کوبا، از جمله یک حملهٔ هوابرد، هستند، هرچند که هنوز هیچ تصمیمی گرفته نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/671532" target="_blank">📅 22:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671531">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
پروژه آشوب با تصاویر قدیمی؛ ادعای تجمع در پاساژ چارسو تهران تکذیب شد
🔹
عصر امروز، چهارشنبه ۲۴ تیرماه، تصاویری با ادعای اعتراض مردم در پاساژهای چهارسو و علاءالدین تهران از سوی برخی اکانت‌های ضد انقلاب در شبکه‌های اجتماعی منتشر شد. شماری از کاربران در شبکه اجتماعی ایکس نیز با انتشار مطالب مشابه، این ویدئوها را بازنشر و تأیید کردند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671531" target="_blank">📅 22:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671530">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfe604fc8.mp4?token=XDtWNztVGBmnZMYLVY8uqECSYf52OzNxsPuRPsnJN0jWsRRhw7vaqw31M3HUJzLiuAS-c-gTPh_HW_arPPf-P1pBd78GpeBUDc7tb_HUuYaWLMOCHyAUyeWJxhrIaRKXA3K_UrS9I2jun_0b2B0y21h7i1g-NEHcLr2_083rtqJUGaOM3KG62LbEJje6OuRqXyqL2V5jzuf2wU9YlZdhJ6ch5M_3tumV4xaAD1oGPvwYDJVOqFXMXQK6-1UgBqNULO7dm2myzVa2LKgnHTr_9lVzVMVQGRTGwMcp3MdNuBTZxMIHvrLlBgMNRI17NyaIJfjHEJ6JX0vbMgcDTum-WLq-P1EiiEzkzJar-JtHOe1CzgJAEYP1KIuYLxLLW984k9qioPRHJoNB62Imlu5_NWKeBvULxkL4tZv9UEJ0PoDo_bqN2V67AufWF2Hf7vl2LMj1MNuckvRxxlX9g6kGy8j21KumZlwna1Zc1y0PWJAbwu-gZDScDG5EsyXzgQQ_A6wFr_6OwLuFAoc2p_bLYVGOHq7RfwCX7gCZqOx-Qz2xYb5EP8DT0j6nVkdgUn_25f47z4mSQQt5GQVQU6D3aNJ92FvXGnLIYKFoa10JPeGQDGfTpghdE9-9A6TSB2Bmqlbp42VlSdj6-f63xHGz6_qkHyuCETlAN0FH642Ggxo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfe604fc8.mp4?token=XDtWNztVGBmnZMYLVY8uqECSYf52OzNxsPuRPsnJN0jWsRRhw7vaqw31M3HUJzLiuAS-c-gTPh_HW_arPPf-P1pBd78GpeBUDc7tb_HUuYaWLMOCHyAUyeWJxhrIaRKXA3K_UrS9I2jun_0b2B0y21h7i1g-NEHcLr2_083rtqJUGaOM3KG62LbEJje6OuRqXyqL2V5jzuf2wU9YlZdhJ6ch5M_3tumV4xaAD1oGPvwYDJVOqFXMXQK6-1UgBqNULO7dm2myzVa2LKgnHTr_9lVzVMVQGRTGwMcp3MdNuBTZxMIHvrLlBgMNRI17NyaIJfjHEJ6JX0vbMgcDTum-WLq-P1EiiEzkzJar-JtHOe1CzgJAEYP1KIuYLxLLW984k9qioPRHJoNB62Imlu5_NWKeBvULxkL4tZv9UEJ0PoDo_bqN2V67AufWF2Hf7vl2LMj1MNuckvRxxlX9g6kGy8j21KumZlwna1Zc1y0PWJAbwu-gZDScDG5EsyXzgQQ_A6wFr_6OwLuFAoc2p_bLYVGOHq7RfwCX7gCZqOx-Qz2xYb5EP8DT0j6nVkdgUn_25f47z4mSQQt5GQVQU6D3aNJ92FvXGnLIYKFoa10JPeGQDGfTpghdE9-9A6TSB2Bmqlbp42VlSdj6-f63xHGz6_qkHyuCETlAN0FH642Ggxo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک تغییر: اولین بار که رهبر شهید را از نزدیک دیدم، فقط مات و مبهوت نگاهش مانده بودم/ آن‌قدر آرامش و نورانیت چهره‌اش برایم عجیب بود که دیگر هیچ‌چیز اطرافم را نمی‌دیدم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/671530" target="_blank">📅 22:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671529">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
فعال شدن پدافند هوایی کنسولگری آمریکا در اربیل
🔹
شبکه المیادین از فعال شدن سامانه پدافند هوایی در کنسولگری آمریکا در اربیل خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/671529" target="_blank">📅 22:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671528">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4312fee5c5.mp4?token=qHq0QzC9MJn4KWXA9voahx_AezpRhw1YEpKmecpav4cSCm9Bs3X6qhMlGkgdhgzS2qgygZ1HHXbYb1obKDoa-6qMsaBoBEGzFCploWh7mJdrbPPPkK2hax_3JS9PZfLLcuQxZDKpRrBvb9qgi6PSb8UKddFFcyR75klXDLOk9PkSXeWtV07NUL-Q_4_8DLYQ7ufuqhvwGRLeN90-NMQbxjTHuIniv0vboL2P6uaFPW6_wnvL5sw9Lo2OxbGwtArxEeJvB-Mz2OaUY-rTioEE_VAAP2WH9LR22KkfH1iRxGkQFIXv6GzO5lqRlzlPiqxo9AoZPM00jGH7Jao9OGQoGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4312fee5c5.mp4?token=qHq0QzC9MJn4KWXA9voahx_AezpRhw1YEpKmecpav4cSCm9Bs3X6qhMlGkgdhgzS2qgygZ1HHXbYb1obKDoa-6qMsaBoBEGzFCploWh7mJdrbPPPkK2hax_3JS9PZfLLcuQxZDKpRrBvb9qgi6PSb8UKddFFcyR75klXDLOk9PkSXeWtV07NUL-Q_4_8DLYQ7ufuqhvwGRLeN90-NMQbxjTHuIniv0vboL2P6uaFPW6_wnvL5sw9Lo2OxbGwtArxEeJvB-Mz2OaUY-rTioEE_VAAP2WH9LR22KkfH1iRxGkQFIXv6GzO5lqRlzlPiqxo9AoZPM00jGH7Jao9OGQoGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عامل اصلی آتش‌زنی فرمانداری و کلانتری شهرستان دهاقان به دار مجازات آویخته شد
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671528" target="_blank">📅 22:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671518">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTf8_8qxH-JvCUXreaAqhlZg_76JSwAmIVr4qFEXSeMSex7bvDqiwGzAaxl0feF48xiIIgLQA-jvxnWpbxy1v5d00QT2EtmncFmCnozoDML73MclSJgPFwQTbrBeGjoMsIVMnNLMFEBkOPQ17exK2EeUmNv8mXMft7umpNxSC1Sr1-DZbc8uzoGAccmHW3Sps9V56IQcOn_PxJ_45RX3MjJhnxdovBJ6klxxT6a6sBHnmz2FMlhtVJz1q8Hu4wmwvPtSDUjb_JDBrjqyp2QFxDncLML8aMdjEH7i8PZC_E8OnLLXZcn13_gsnDRvzdulwHEjvJyKka4n92bGjkSw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O_xrWNfcOtxwznTC_BYlIWwWNoQnccaUntU9A_5JmQfalE47qf8W6HoNtq_ysTEHsmJhVz5GK2pL-4XKzQRQqEHM_0bg7OjT-y4xYKw2xi-dtlMo3jenNdNTYXycmAh_iygSk1aFlxyyiQm0GBD9Vm63fUrjDZuVdaKFgBXa_ypxD_sbZK9yTMxS88OtHBKuMjjb_qKxljvkThA_th9gH4hQ2-6CkCaUwzvt7ehqODMANcxbRT2wB-b24ta2nT8iH4qqnii4WFTlvv0D2jA8ECnNCspmoB1FuHQvhpV475H_m8HkQvxuqsKsi3HQ9lmjXsTTM3CR0d4NdkwCu9XNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eH0XBfV_0VRLsS1J1ChcC5eelRp77EJMPokvNWVpZTa81r0cskulhzIQyqiB-9dfSsEQj80CbKiFe_r47oGRAj9B9DfkMmuS8SAF7QTu1HBA3xoi3mm8o8uRy7FcIYARR6nWF2JCq7s2kVDU3KSnWvdjxLVRq-9YmnQhl_zV_TqWKwlhOp2-9eulrsAAIWjHcunRAgBUCQls6LGIiIVXA3QBz2U_uBABvKik2E7MJTavwJO777DvW3ZLFw4iH3bXGr8QhLJhN48wyUSyUvbFVr2gVews8ZE8BirmTdnMA3-PASry5nI052VvYz9psLnc5wmKA6UvMbfMmeoK7gQxEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqA_yfx4t9SKgS0KLQriB5bD8jTnpBkL5XNoRq78UUJj3d8AY2FAzc5z9dtiAtYmwwWAfcG05mu-mn9u_vkGp5Uh8JV6koUpBaiznmXcmuc6KHbLcQWE2QIoL_6vvKAfKeyxbCEjl0B50zjuXKIxuvhGX1HilLDAwzSh0LNJa7v-wobvY3_tHJIbFUS9KMYDGlBAA99kX41iRu4PyFLzxrmqYYMLTYb8-HYfnIs1ShhCeH730IBUg1Ppeskl8Wnq7HW2E95EF5Rt_GUe-A_D_bGMHV33-eVwouAByQUchRdshKhPaZaBfxlf4gXg9pSxKezu-CFGJGgU2BWowTGUzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vwe3F5HlLwtX8xPJlGESGZ6Ltou6Jth8IFCUpAq5aHxy_dKw8TKWGQmQTa57e63ugwoEiEjCg2WhkO6nbODi56YL6x98WJMWfqqBgeWHNRtz-aAqiO9jOWb-Ws7OwXyCuTYFHf4zPVFCZYWlxh8sZXikQxPJZqnt7agAoyAUGPaYdwcguXQlY3PFPl9L6p-b1Q_FpozxQ17aEm3KNw7VyYu3q2NtAqKa2if6ZMlYbF5Qyznu7xfEgstExCtwNEVz1M7I8wZUcI4VJhccrZbl2DNL65QEodFAuSY8XaOFnHgbwlF9hLAHLC5BbdgIpD6RKv54CT6MDcnesxeFGRQdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vz6TRtA7f03aRqb1bAgVih42-APMTaRsjLCrJaDNxCXaHOT28OstNMv7u_iR3dHb0_lTRwm-_UF3PDaAIIt8ptGPxXlnmhtQ1OlnE6oY37nEzZfmb562zplU6x-0Hwh7DKpiwuNnj4nCycxFehVmYPyLPFbj-4uSfT0lObCKIAmyUCmxZNNFn0jT3bC4C0uzdmsqImoUgR32QPTGrMYUH5UnorbifiRJCeJlqdWhpynBYYpe-DfZQGUfxHPpLb2s9Q_N2pwjIJ1GlXYGiEa_UhNWKxsPB3osVSpMNT0RY-RXxd0g-D6WCSgG1PTbE1dat-MlNTsiqDnNMGhnvE3FnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jmbOcJXdhBeIQGAxSbgw1F4_p738MDvBrAIU7nmTecSSJ0UhUlxaIujOOZsuPUUZ-j5dHhyjfn_CAP-npRr7yUa2rr3qhMTK76JbuBAqpLBfxz99nRTup-G-XBx77k9CvlCpSmenuSe0ir-JNF4FlqRtRbSGnTBbIxHKpq89jecCe0iQgLRMCeMDJyv7CVsCemhwZoBnkmEI2l-YHyBOrcfYwImOm_YgaeA4ZthSWYzQ5XOV4sYm-TeGQoiPjVUM5Ufio3w4OpvPxA1OCaFjFbqKyRCnzvmgj9jq6s5Ya_Fz4kPMG1-BnVamhqcD-uDqzLihQg871cYXa6buyrnWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3TFxuu2O7VV0x7cyQN7MCz99D_vD4uLzAzkcqPLBSGIraDXn6Wy-bQPuZcHw94Ce9Ms7vFdtyc20c2t6QChU60z-sckZpUWGvjrjPkd1YI_LLgws5XLED2vjvrd73NQUxLtcNKhxcl2RvfN75a6kf7gdx_VbirFRko_9-OmI2DOqyOlNXhxZWwPpjrFHYTabZvvpIjKFDc_p8sYQwcwh2QbzN3309BTEf25u5D6j3sMC0WRYIkVwyhWbaVgykSFe4Q0P_v7Nrlk8xgrPwcjS507OHkHLQls6Gz9OpWs5STN3Mb_I0RHoCyijPOf3AeBWDo1MH2CQwyUGETUUGtbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hqvp3vRaSflKCUokDsKgG3Uy-0R8u9ixqutmpUJkhCb8maPZ5BfkKhxhPq2660gmkXe66xVmviyZvfaKz4_vAKT31cnfeCKOin95BcgWRxxZADZEfAgPFj4py7P5OeUGM2lAkPSmez9MhpxAnorZnckhUPuiUwDtj4F8ZOgqs-zBQ3zybWAwF74vGDS_cQ4F9SXAgjOaWHIHmlMsxfarKmVQJyOvObtso3B1zRr_1pltgL45uFaWielSMCqkaBKZlbWlrK7zQ7fANNXn1MUJJBzq9n07ejYIzwIbFPNPKYwu9b6475o0irwzaGI7IDEANjSDT_efky89EPF7G1haGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfqLt15qgXvwqit1zOg0gasl2EylADyPREbJJTDS0B0j-T0_cx4uzMIu5EHnFz7u4fUt1jkef0fUASt8LwytNEAPg4qPMRPiRTbP3ftmFoReU8Hs_ufR0_a3WpjQB8pFhlMoqDSkaQAGM3ScQhmHIwqF5N_sgkeXotGO2rTgjRAuL34RIhc8kEaArW8ZPnBNYJ4QE9Ybi4FHMZBJILLMLxNX6C0jKQp0KaOGbhiPsPrwulPJDRLmCkf_RR3vNhsBRlnsfOEJXLe_iarFALmzg6sBZh4nXOa5lpRHdsWMWx_aEUh4IeEl-C5N1h5aDX1Jk5NQLOnAmK2h0zw2J3QpRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت مخاطبان خبرفوری از قطعی برق در ساعاتی غیر از زمان‌بندی اعلام‌شده
🔸
اگر شما هم چنین تجربه‌ای داشته‌اید، از طریق الوفوری با ما در میان بگذارید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/671518" target="_blank">📅 22:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671517">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
معرفی فیلم: کتاب قانون
🔹
ژانر: درام، کمدی، عاشقانه
🔹
امتیاز (IMDb): ۷.۰/۱۰
🔹
خلاصه: زنی لبنانی که پس از آشنایی با اسلام، با مردی ایرانی ازدواج می‌کند و به ایران می‌آید؛ اما آنچه در رفتار برخی مدعیان دینداری می‌بیند با آموزه‌های دینی که به آن ایمان آورده…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671517" target="_blank">📅 22:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671516">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شیطان زرد درباره ایران: من از تعیین ضرب‌الاجل خوشم نمی‌آید
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671516" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671515">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e6e5618c.mp4?token=Yrn9NhTujHN1GxPmW55yJ6Knjh_YK6m5GQXptP-h8R3BM4ljO7Jg7IQlNuzx0L-mKPaONalr7SiYwoRhEhIi2O4VGfzO7ZGsICEnSDzu1QaaqQ3Kh_AW16lk1xnWzK-IFDC8bQlphJ0qWbLa6xxu47CXQ3U7MMxziyJzDmcRUgOZLSyLrrGjr8mFcAK1uL5tpvyQ29fmfiV56igQ2OkM97rDmHqJ6TX4rN0NCOJjKQhffCLPEWH9RFZ75oC-yAz9DLfuYPz84Mo12zRHaRp02n4OvGl5zIU9LXOjGLcYz-dIXjeUSnri_w-79ssP5M8p_8qx5FWn8a0SK9cTxDIWZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e6e5618c.mp4?token=Yrn9NhTujHN1GxPmW55yJ6Knjh_YK6m5GQXptP-h8R3BM4ljO7Jg7IQlNuzx0L-mKPaONalr7SiYwoRhEhIi2O4VGfzO7ZGsICEnSDzu1QaaqQ3Kh_AW16lk1xnWzK-IFDC8bQlphJ0qWbLa6xxu47CXQ3U7MMxziyJzDmcRUgOZLSyLrrGjr8mFcAK1uL5tpvyQ29fmfiV56igQ2OkM97rDmHqJ6TX4rN0NCOJjKQhffCLPEWH9RFZ75oC-yAz9DLfuYPz84Mo12zRHaRp02n4OvGl5zIU9LXOjGLcYz-dIXjeUSnri_w-79ssP5M8p_8qx5FWn8a0SK9cTxDIWZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی نظامی یکی از ابزارهای حل مسئله است، نه راه‌حلی نامحدود
ادعای جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔹
کاری که رئیس‌جمهور بسیار بسیار ماهرانه انجام داده، این است که گفته ما در این شرایط زمانی از نیروی نظامی استفاده خواهیم کرد که به چیزی که سعی داریم به آن برسیم، مرتبط باشد...
🔹
اما ما قرار نیست کاری را بدون پایان و به طور نامحدود انجام دهیم... ما سعی خواهیم کرد از نیروی نظامی خود به عنوان یکی از ابزارهای متعددی که برای حل مسئله در اختیار داریم، استفاده کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/671515" target="_blank">📅 22:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671514">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b3fa6a0e.mp4?token=h1BpGNNwDSHpyA623jkwQ3jS4TBE8styypKVHO0uQyD6_QNjvMrEfBVRYKX0lWmqitErBXG1FyYxtYPDYu-_nAECkDG5XjDJjvZ5pHaBuz6l4LF-Hlue7BKGk3nUFBfUbUZ6yEmrhSAdr2cpS65buJSr2J4hOeVTXLmOzz30NXlmSyfprfbkGNFfI3hGRkavnj89J5f9S1Ov7zMqIsYfg-i3xvMv_qpGbG5xydo_KI7nh6SNYaUhcHY67lPnkf0Dx3rGEdBjXrn4Nz02VOZS_PiJ6F_k1RtzTUHX_iFRhSOGMliQIcz1N9I25JUxuYCeQBXVMPTdR7zkYNHHovBRBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b3fa6a0e.mp4?token=h1BpGNNwDSHpyA623jkwQ3jS4TBE8styypKVHO0uQyD6_QNjvMrEfBVRYKX0lWmqitErBXG1FyYxtYPDYu-_nAECkDG5XjDJjvZ5pHaBuz6l4LF-Hlue7BKGk3nUFBfUbUZ6yEmrhSAdr2cpS65buJSr2J4hOeVTXLmOzz30NXlmSyfprfbkGNFfI3hGRkavnj89J5f9S1Ov7zMqIsYfg-i3xvMv_qpGbG5xydo_KI7nh6SNYaUhcHY67lPnkf0Dx3rGEdBjXrn4Nz02VOZS_PiJ6F_k1RtzTUHX_iFRhSOGMliQIcz1N9I25JUxuYCeQBXVMPTdR7zkYNHHovBRBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مأموریت من تحقق اهداف رئیس‌جمهور در قبال ایران است
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔹
این همه حرف‌های بی‌ربط و مزخرف وجود دارد، در حالی که کاری که من واقعاً سعی می‌کنم انجام دهم، تحقق آن چیزی است که رئیس‌جمهور به من گفت تا به آن برسم، که همان حل و فصل این مسئله به گونه‌ای است که به اهدافمان برسیم. ایران سلاح هسته‌ای نداشته باشد؛ جریان آزاد نفت و گاز را داشته باشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/671514" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671513">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09524fedc4.mp4?token=I64ZfFYpTzE2822bvhyNAFekVYqdtF-cnqke_J_Qt41cu89Fy3U7Br5M2q-hmt8-6uAHpkkaNEDo7DGHuloloBgg0RwoE5kEZi-5-rWDIzMl4iAl3YQhLZAzKk4PRldkhKyPPSlk7KjAq5--wLNuORNJwWS8kt7kJSWhAPPA4LBz2Utlr9kmuJvQES0VI1IccigNj4wB9x59DWSnTAeYEZp9cEVM-yPjGRoGY9Z54VVuyEPv6Lxb1h22QaLv_92cyo2ceOj0w6Teed2s-c4awFwgjZW-jyq5dEEWebRON4XDchC3ApgMZzRbTWZHXqGAAj9_cTygNfUbHYOEUmZ3Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09524fedc4.mp4?token=I64ZfFYpTzE2822bvhyNAFekVYqdtF-cnqke_J_Qt41cu89Fy3U7Br5M2q-hmt8-6uAHpkkaNEDo7DGHuloloBgg0RwoE5kEZi-5-rWDIzMl4iAl3YQhLZAzKk4PRldkhKyPPSlk7KjAq5--wLNuORNJwWS8kt7kJSWhAPPA4LBz2Utlr9kmuJvQES0VI1IccigNj4wB9x59DWSnTAeYEZp9cEVM-yPjGRoGY9Z54VVuyEPv6Lxb1h22QaLv_92cyo2ceOj0w6Teed2s-c4awFwgjZW-jyq5dEEWebRON4XDchC3ApgMZzRbTWZHXqGAAj9_cTygNfUbHYOEUmZ3Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در انتقام دیگر هیچ خط‌ قرمزی مطرح نیست
🔹
گفتار مهم استاد رحیم‌پور ازغدی، عضو شورای عالی انقلاب فرهنگی  درباره از بین رفتن خط‌ قرمز‌های انتقام درباره انتقام امام شهید امت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/671513" target="_blank">📅 21:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671512">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ونس درباره مذاکرات با ایران: نیروی نظامی یک ابزار است، اما دیپلماسی هم یک ابزار دیگر است
🔹
از آمریکایی‌هایی که می‌گویند نمی‌شود با ایرانی‌ها مذاکره کرد کلافه می‌شوم. پس راه‌حل شما چیست برای اینکه افراد دست از شلیک به کشتی‌ها در تنگه هرمز بردارند؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/671512" target="_blank">📅 21:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671511">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ونس: ما برای تغییر نظام ایران، نیروی زمینی اعزام نخواهیم کرد
🔹
معاون رئیس دولت تروریستی آمریکا که به توان نظامیان ایران اشراف دارد، گفت که این کشوور قصد ندارد نیروی زمینی برای تغییر نظام ایران اعزام کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671511" target="_blank">📅 21:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671510">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
اعمال محدودیت مصرف آب در فرانسه در بحبوحه گرمای بی‌سابقه
🔹
وزیر گذار بوم‌شناختی فرانسه مونیک باربو روز چهارشنبه گفت که این کشور با وضعیت خشکسالی «استثنایی» و «بسیار نگران‌کننده‌ای» روبروست و تعداد بی‌سابقه‌ای از مناطق تحت تأثیر محدودیت‌های آبی قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671510" target="_blank">📅 21:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671509">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
تصاویری که می‌بینید انفجار موشک نیست!
🔹
در شرایطی که برخی استان‌های جنوبی کشور درگیر جنگ با دشمن آمریکایی است در همان حوالی، معدن باریت آبترش رفسنجان با انجام عملیات آتشباری مشغول توسعه عملیات معدنی و افزایش تولید می‌باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/671509" target="_blank">📅 21:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671508">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
فعال شدن پدافند هوایی کنسولگری آمریکا در اربیل
🔹
شبکه المیادین از فعال شدن سامانه پدافند هوایی در کنسولگری آمریکا در اربیل خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/671508" target="_blank">📅 21:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671506">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0868a52354.mp4?token=DTu1e-IyXmvE3nL9PYNCbbM2d2FrEcGytOjJ2KabwB2YN3osohd1GG1wn9Hj-kbdQ33UUNFKIDm4riLg_n-0zotepzBmWzeE2z0NkhYGwZn_OKHHY6uh8aAvMeiLWjaslqvCZh7uZ-Ymh5DtjotItROD3to7VXw24nPI5X2NoszC873JsoCURw6rC-64CnxultpAOyNXZ-jXBAUwXPI7dIuEKqBRzxZrq7WGywSJscLk1e4wSSWWxfCLOHblFPKgsdFBg41sfvZU8u1huRHzJaIxDwehhu3DJYe8MP8p9-UdvGsU9nhUTtRkJy_3k3rhUMnvuZt_dxAHre3tbWR8zLrckKE-WaEBNKoMBHdyhhGh1VINdZSmioasCGCOOExxQAzvR8y9rQZ012uOtRH9ZbD9OvPmHzRo0LJUUqXbYd0prSUPuRJPreBGONEp6MR8C9ov_LrAWW9kjnn0N1CkFH7GESBWcO2farv_GXNdoYNb7auHPJp71YPOnMogLdyNm60nZw9OYgJEhIDo_ISdtFz9OhuRp7Zxpv9nyEPX4XofS4OafyA8Qnb6h6SKoEuCF9LCimILDfXcOKbBLtcHEK3Y9XNB_MFDNcvz8PrHohijNkyxQ28RrWavHza0AYw-pOXkW6MBMHmitBXjkhDK5cAJRKnWYnag2kIU1GzuXUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0868a52354.mp4?token=DTu1e-IyXmvE3nL9PYNCbbM2d2FrEcGytOjJ2KabwB2YN3osohd1GG1wn9Hj-kbdQ33UUNFKIDm4riLg_n-0zotepzBmWzeE2z0NkhYGwZn_OKHHY6uh8aAvMeiLWjaslqvCZh7uZ-Ymh5DtjotItROD3to7VXw24nPI5X2NoszC873JsoCURw6rC-64CnxultpAOyNXZ-jXBAUwXPI7dIuEKqBRzxZrq7WGywSJscLk1e4wSSWWxfCLOHblFPKgsdFBg41sfvZU8u1huRHzJaIxDwehhu3DJYe8MP8p9-UdvGsU9nhUTtRkJy_3k3rhUMnvuZt_dxAHre3tbWR8zLrckKE-WaEBNKoMBHdyhhGh1VINdZSmioasCGCOOExxQAzvR8y9rQZ012uOtRH9ZbD9OvPmHzRo0LJUUqXbYd0prSUPuRJPreBGONEp6MR8C9ov_LrAWW9kjnn0N1CkFH7GESBWcO2farv_GXNdoYNb7auHPJp71YPOnMogLdyNm60nZw9OYgJEhIDo_ISdtFz9OhuRp7Zxpv9nyEPX4XofS4OafyA8Qnb6h6SKoEuCF9LCimILDfXcOKbBLtcHEK3Y9XNB_MFDNcvz8PrHohijNkyxQ28RrWavHza0AYw-pOXkW6MBMHmitBXjkhDK5cAJRKnWYnag2kIU1GzuXUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی هوایی روسیه ۳ کشتی باری اوکراین و ۴ قایق بدون سرنشین اوکراینی را به این شکل هدف قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/671506" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671504">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050eacefc3.mp4?token=ULclwugKovY2EY7Yv1GUAY3ftneGp5ZbxVC2XNn8hatBUmiZfJiXeHbUaSy1JpimNkJEOoCblpJIyT51AYiIP0veASoRF_sp2u2Qk2uDWqVfDyAqAZ2-oicDxh-dezPAfUpXzXeJCGAciBwG8P92tPLNo392owukUk6bAvT7MmtYrfazvIHWBrwSCw7B9VD9hOlJjwtE9efVFlGV-fSryhR9-pO7EHpsrNtcHvlP0cFz7MafWWJ08XVn7PeI6Cl7a6Z4xlkZODDv2uwA-bvhpZ7Qfz5KPhCKcyXv7nVJG8NZkom84ieffC1JVM94F8lraqEbWXXV5_hjaz7IHgo7Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050eacefc3.mp4?token=ULclwugKovY2EY7Yv1GUAY3ftneGp5ZbxVC2XNn8hatBUmiZfJiXeHbUaSy1JpimNkJEOoCblpJIyT51AYiIP0veASoRF_sp2u2Qk2uDWqVfDyAqAZ2-oicDxh-dezPAfUpXzXeJCGAciBwG8P92tPLNo392owukUk6bAvT7MmtYrfazvIHWBrwSCw7B9VD9hOlJjwtE9efVFlGV-fSryhR9-pO7EHpsrNtcHvlP0cFz7MafWWJ08XVn7PeI6Cl7a6Z4xlkZODDv2uwA-bvhpZ7Qfz5KPhCKcyXv7nVJG8NZkom84ieffC1JVM94F8lraqEbWXXV5_hjaz7IHgo7Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله موشکی به مقر تروریست‌های ضد ایرانی در اربیل
🔹
رسانه‌های عراقی از حمله موشکی به مقر گروه‌های کُرد ضد ایرانی در اربیل خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/671504" target="_blank">📅 21:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671503">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد «لوکاس» در بندرعباس
روابط عمومی سپاه امام‌سجاد:
🔹
امروز یک فروند پهپاد «لوکاس» دشمن متجاوز، توسط سامانه‌ نوین پدافند هوایی سپاه امام سجاد تحت شبکه یکپارچه پدافندی کشور در بندرعباس، ساقط شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/671503" target="_blank">📅 21:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671502">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
تداوم حملات توپخانه‌ای و هوایی رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری از تداوم حملات هوایی و توپخانه‌ای رژیم صهیونیستی به مناطقی از جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/671502" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671501">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b4786a59.mp4?token=LW8kGWtWY7e9MQHEawQzAjQhTgWEuZUAp4kXSWxyUSHSaCNPz9rDWvYkTnU3_Bdnqe4KYVwNCM4YM8r_TibO9Oxx036VLILymeankX3Qh9AoxHT9uxU-UVyzHRL14VBfLIOjy8dWbVl1DjH-CiNkaqetgcRPc9Xbf4Y6s9JjNzG3NGcv7bU4gmuhT04puLxK3x3U4vNCKQfwxGb1SdY-ruV5zc050RSPLAaNaNb4Z8HMCBMNYMcq0dpiJ9ju0Of2JLh2QE2cRzn_WmC9kLW7TJn1_J2XwOXazTyojBbsVmj_jdebnhPWmxcogOVUSIzh6bpx-UsGjCSyNbhz3EiyRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b4786a59.mp4?token=LW8kGWtWY7e9MQHEawQzAjQhTgWEuZUAp4kXSWxyUSHSaCNPz9rDWvYkTnU3_Bdnqe4KYVwNCM4YM8r_TibO9Oxx036VLILymeankX3Qh9AoxHT9uxU-UVyzHRL14VBfLIOjy8dWbVl1DjH-CiNkaqetgcRPc9Xbf4Y6s9JjNzG3NGcv7bU4gmuhT04puLxK3x3U4vNCKQfwxGb1SdY-ruV5zc050RSPLAaNaNb4Z8HMCBMNYMcq0dpiJ9ju0Of2JLh2QE2cRzn_WmC9kLW7TJn1_J2XwOXazTyojBbsVmj_jdebnhPWmxcogOVUSIzh6bpx-UsGjCSyNbhz3EiyRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقام امام شهید، یک مأموریت الهی است
حجه الاسلام محمد قمی، رئیس سازمان تبلیغات اسلامی:
🔹
در پیام رهبر معظم انقلاب واژه‌ای بود که انتقام و خونخواهی را از یک سنت جاری الهی فراتر برد و آن را به «مأموریت الهی» تعبیر کرد
🔹
برای اجرای «مأموریت الهی» همه باید آماده باشند، تلاش کنند و برنامه ریزی داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/671501" target="_blank">📅 21:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671500">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهای مهیب در اربیل
🔹
منابع رسانه‌ای از شنیده شدن مجدد صدای انفجارهای مهیب در اربیل واقع در شمال عراق خبر دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/671500" target="_blank">📅 21:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671499">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ونس: ما برای تغییر نظام ایران، نیروی زمینی اعزام نخواهیم کرد
🔹
معاون رئیس دولت تروریستی آمریکا که به توان نظامیان ایران اشراف دارد، گفت که این کشوور قصد ندارد نیروی زمینی برای تغییر نظام ایران اعزام کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671499" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671498">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDF1PtQ-FJG1DDIpberz15WZchVQAdljVFBbm-p7nkPMiv1qO4_eKlbVaUdp1aakD6IoiXtD7WNzM-U6Rmvpl8F1Gva54ked1HauiUo3y1TFVAVPOvxp7q6PnPYqTgconryodZ5bimiGpO4jyTsCLnMEK3Tgs8ww972m_AzlHG_g8t1x6hX8mUicqYC3k5kM1_xOL91bdqY2w4s6V8GkCNGKOxLN4vwoqcQRVDXQmhHLVOyIBSa7g4nb91oHjNA3sgXdTneXRpfNxnCptF72gdjh4WMLMxUck8jsM0NBUumNiHgBGdpYBYUE3ofYlMuStSRwJ9qFznnmLJbRYfhbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ایران یک جان به‌هم‌ پیوسته است
🔹
ایران را نه با خط‌کش جغرافیا می‌توان برید و نه با واژه‌ها می‌توان تکه‌تکه کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/671498" target="_blank">📅 21:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671497">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
قالیباف: مردم جنوب کشورم، شما عزیز جان ایران هستید، جان ما هزار بار فدای شما
🔹
به مردم جنوب کشورم که این روزها در خط مقدم جبهه قرار دارند، می‌گویم که از ابتدای جوانی دوشادوش شما خواهران و برادران عزیزم اسلحه به دوش گرفتم و جنگیدم، شما عزیز جان ایران هستید،…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671497" target="_blank">📅 21:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671496">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
قالیباف: بنده هم در میدان دفاعی و هم در مقابل طراحی دشمن در جنگ رسانه‌ای بودم، بعد از آن هم با علم به تمامی مشکلات و تخریب‌ها در سنگر دیپلماسی حضور پیدا کردم و هیچ‌گاه از زیر بار مسئولیت شانه خالی نکرده‌ام
🔹
هدفم اعتلای ایران عزیزتر از جان، تحت هدایت‌های…</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/671496" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671495">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
قالیباف: حمایت و اعتماد شما به سربازان عرصه دفاعی، دیپلماسی و خدمت، دست آنان را مقابل دشمن برتر می‌کند
🔹
مطمئن باشید آن‌ها جان خود را ضمانت امنیت شما و منافع ملی ایران گذاشته‌اند و با تدابیر رهبر معظم انقلاب و مسیری که طراحی شده، نتیجه این اعتماد و حمایت…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671495" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671494">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
قالیباف: برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/671494" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
