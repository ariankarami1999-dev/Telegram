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
<img src="https://cdn4.telesco.pe/file/ONWm_RBiQtHKKk4qpirnmPYnSDcPFu7acWTLAJ-_JCScXByFAjIZZjfKsKSQuUAFsPhFObPTrGNIVvUVArI2ninB2Jr-CEj5ejdOCkpirJUwvTPo5TAb67guXSPSWh_-Hge2T2DQNkYAY2-pt-7alXRP0K4fgsaD-j_wS7yCYqeptJmfMh8ZlR0CaXJjgd2oWqx0tg16n-ZaH4ZnYOKegg2olLM4oQhzro4kRT_N4A0Rwkzh-rLJ-UTuFumakpUhe7Kk786Vb_4iu8xYrYF-aaGtlFwOBQe3cG6IxJNaCRbhR-Nso_ERh_P8eXLoOEX2Yxf8Z9ShZg-a0dG7E5k7Ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 313K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 09:59:19</div>
<hr>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjdltuBNpZQx4fBR_R8njC7SaMMxDZK_K_yrhgvgfQOXXIU0kzXLEQpHWq2gJQmzrJlVXUmF4AK2w-sU-mNnEq5UELiqigt-ryO0s7G37XyQefZW0WUSQCM5vH9koFaYzSLTlo5T4vtjv-yH9vdB9uSWxAEea_LcbAv51qmaDEmNWsgCmWXRx7kieeOp1SPKz1Tvh_1dg6PfFleniZ8ui58meFn8CWr5xfu9TfGiMqSG4aDFkqGpbQ1v3FJHxB287jvZB9e4CWF5iFqWg1SVIY2vRmH3Y1q3ePi1rozgdyz8_gVsZEtNd58QnmxixU0Xv428GIjfYFULoejJR8jQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqxIt4pPBl8Iv_09LBYhupd1mjKTl1RbeNHaYvjAVXTg-lUYY3_vXoSQi35ODS0pRkq8wq8Cb38nrbwWd-kbErBt8j1MH-6cXbKl1XmS5jwR-NmtnokYU3hMfdUcfxDxCK49hYQ06rpiJeZdOFHpGOXTvuCXxOrRWkhGhx8v3hmrqcFcQ_RrFBTaQdW6fBrsjtGljUrKBpyMvoqJC9YPO64DCAlOEY_5LhUmtX2SxAVW4bLd7zhQ_KEI6ijATYwnrj9YvpjRHcAcT2Ca98xxiwgZ_ptoh7OJQ-mxGRD43jcQLKLrx_E-twNi_-dtPKFVuibTMANkE6HW_Y16Von7Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=v2mJ4FFFwE5QX6cFA1mQTwdM5uvx39yJQKAfulb1zQgTfCGeVUmiuCEvDt9yZ86xH-HoONMt9PTYViRJxEMpqrwsumIOk5brblX9ny8IV3HifWH8Qfy9REt2Fp4GkYCSVzLNinj4_xhBjlqdsg7zcDmfNG22wB6EMRlVaw8qtNAolP-mwbE5hpSvsJcfA-qMGJUqxTQ9SxSsWHK7p7-ex6l_R2OC43mFQQLVI1snXKFTOHrkRT5m9AAf8jAPCZaGEIZS9vIiGShOPw8teQoHJTphav78GrxITzKlt1GbvA3JN4Qkj1p8dgnHWPNid1rmP3Alpobq99cdgVwbLu4I3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=v2mJ4FFFwE5QX6cFA1mQTwdM5uvx39yJQKAfulb1zQgTfCGeVUmiuCEvDt9yZ86xH-HoONMt9PTYViRJxEMpqrwsumIOk5brblX9ny8IV3HifWH8Qfy9REt2Fp4GkYCSVzLNinj4_xhBjlqdsg7zcDmfNG22wB6EMRlVaw8qtNAolP-mwbE5hpSvsJcfA-qMGJUqxTQ9SxSsWHK7p7-ex6l_R2OC43mFQQLVI1snXKFTOHrkRT5m9AAf8jAPCZaGEIZS9vIiGShOPw8teQoHJTphav78GrxITzKlt1GbvA3JN4Qkj1p8dgnHWPNid1rmP3Alpobq99cdgVwbLu4I3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEGhjTckE9m32F-fEE9k1C3NLh6B5WOo7h8oOdHxN9zx04umprsWnCa8K2B1fPpJdMsv1vEeKoPA2dTop0ZxAUGpUBV9l45B9ThqK66PqfiEP_uEpmYgXQ0fZ-yTN3F7lJcqr_An-5VeDyaK8P6sC74NJ07WB9X23RuRADU0sDhhU51HENhIn89NEKcnGvA34e-etCTsTi6F7mp7PWAe1Vr-yg3RJQHQEs-MkyL1ThKP5JzL2ciw2hoQho54J0_S5yxn8_a5JduAHk8p33t_RFcmWtxwWz-8oQaKTwpjR2reo69_4nK6xSpoeI99RrXKhM-zc2PcTMzPDTQdsiW2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCdE8g22sUsF908lDDCSLoK3wtFe4CGgGSp7ziQkiNaHqO9yUzTriHcbC1-Hx_DHLdkgVeJCyTuP_yf1I0O5wNoxQ7azMGC2AFxVvjcdlIkoEvPsarchjJWSA3M7bzkVi6YLUCQfqSlEe6rsKcaDJqm8S9l3gWkivpmC_cXfrvP4Mh4HnVgu3HMkArcUvZJsLYPcq705ksBrtnO5Xb7AFBiLcx73VG5yT83cmD_bCoOnLKuuRdrAwAv1U0F1_4yPSUqXLwKYzFxlmV7t_1XzwC_W18590j0RGogwHUwOyG6b_uAg5FzBZPqyJ2T9icnu075-EyDaYm_dNby8TQK4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌دو دیدار بامداد امروز جام جهانی؛ دومین پیروزی کلمبیا و صعود به مرحله حذفی؛ اولین پیروزی کروات‌ها در جام جهانی و امید به صعود بمرحله‌حذفی درگام آخر مرحله گروهی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/persiana_Soccer/24185" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7nC6p-fwKb4ZR9MB-_1J8mWdVvJ7V1aF9_aNJ8fANBU-S8AHvTRx0JsNX5lM4Lz-I6jWfv_W5wO65cTQdv_UfO9Sbsh_gEdfXIwp9uyrEXX0JVpN0ecsbOsINvQYotgCHx77tUk4nZmm0juo4HRTLq31mF_reUxIJ9XhRxbK5EcJOgYbfVqSoMWvfU6Dqdez1STQliU50SJTFobppZ2PqDCrGVZPvrQf6gKftwsRVHCg8wyQ8RLqb_UVTcr2G8z0UNtdl10O8drJ1fhnUvioGeCj7UDTUMK-WWjYc4AV51cezxDAxCZT0XtlvbLXPJQPNxfPU8CgMdjdFgAHKR8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioIQSCPXrYH-TN3l0r7vP5VCr-mVhGZXaOCXZ4p0TGRcPSPO7VLyqg5LcfBaPuCrIYDSmM_QQ-zxiXXpv9kcnCdsMYjRcfBuxpBz5H5eYEYxOAnyi-SW5_WCvhKLYoIwDaz0HjpiPJrzhqDVi8UzPaMVLUe2108m5uLz5XFfLgh9lDUcquPjzvkn6p4IgpUgeDiajQJygdG5CYg6bjLTTbdcl6LDh-EzAfndI1amIp-S0llGuNT0RV6tPzbmhcZvjBr-XSDmZPWoOu-EE9mrziuP1gWxEzTmo6R2f9nswT-duoJAu15S_V-h26HriiHCb_jC61Sh3H5lJ9FTKWy6Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/persiana_Soccer/24183" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZRuFP4VdpZhSj1f9TlDscExBlnT8_fOH8KfuG8W90ANPgcdA3oyYuMOORdLaFkkSPAWmgHSct3BYLy7WDafPLxKtjLA0_KrV9YE5FQ-uOTrUOvm2_b8W7jUT7-3Dk83pAUJs27KtFtRW8wNITF3Mhvalx7J-AFEWhYj5cAgsFrknUUUurZ8PQQ5TWDrsfGwe8lgi8dFX2D7epYIVG-h76pjuzC6hAbYScCaDnUu7JtppCOPHOH8mubNdMqI7lFBmQB6guIn6F6yG-kcDdVEtbkKi3I2ksTfiRzRQnPbja4jHUjrHu8xCc0qa6cp4fic7yQaT23z4joUxrpswc2zmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK4OrHnt4U9XhVqeM6e-pXlt0W1Ul1Cmr6cT06fsgWvvARMDW4rJtYjP5EpXofOswrkLaO8_cnQrAY4uKj2DLHWP3ilsPdv-A4ii1ZrwxP5Wlm5wTyvYbkhCTQysMOEp-de_YvWx-VJHqpPMjR8A3rex1wdCDwMx440q0M8uu-LCTe_W9oMw0DtQ9gxrkIh9-hIdPep5YnBfy4LXiYzbpryTzDcx1QqYV1pONPckAtneSORcmXzwXHnssEM0VVmbdhbYQUCEXQOE3YzUcqJFfzG813IxW8B7IZhCU-qdUxgARm9GrjRK6HUNX_ASIosfW29GJBotpvKgDqZCTK04hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhIi0YwxXbRzQ5ZVjEQ8HtQqT52L3vzEHcy80epZwUHp2CD_qeNyThv0dcVNCRsyIL-I1ns078tfxzlZ7VKEL8pNMCr5tqre-yXz3u39T0jmjwTPGPL82TNb-fD4UYEaf4ACOXkyq5-TEFsptMQ37EV1CGCirizO5Ht_2MPUryN-bzGjBVn5dCZxe6oOCG9wWt97CgT97O5C7N4RA_xnBfsBO0dEe_ZUhsVa82hdnLgIATeG1RZkZ-BCyziaveUOPFTxxhq-N5pWx-GuMwOoMIKLx98tQli52QpsrGexK8WVUUqSogO_sCO1JRCZo05FtYZWdWZ2N04LuFFZu_TU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOsoFGsby7C-SF3jX_JD46TLxRs6u5VnV_iFKatOOPWCLPlJwCNrmgig0PtWNqncMSUd914OCoXD61OtdHydERTbV0iVs7gApBHSQTTUN8mBmU5FFaXWnxPRAqdkTawVuKift4OvhjeXQ9lcxpJyQtAXtGDu2ZFpJVVAQfbJwSdYQoaDLVq0ETleM3KOAoB0olPGN6qdHIRhPa6bEUmTPcTqK-mIsc0F11qVvQe3U-RdcDFWTPOCplIW06lrVZwaByTZX4BGJN2HbjiZrzFSvuIwIgwD5Rjm4Zxg1eihJbDDRxXz3kgUxpJTuABpLQUIJPO0AP4iRlUNQYhqi9zDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaU6mvZmy78P_38ekQG-qNTB11bw6U8Npd25GE-uFzK4WJuE8ykKgU-3gkJFVUjBuZR9dVK8wAAr4vBzFwZTo5sGe7VfjnQ3TDSgFfymd3-zJwV5lmT-20VSQvqj2qpztPFVtEfZ_yZzlYgHpH2F-2GcrvcjhgTZs0ECOmyRwHDh003nvCT2l7hcfT284jLug7ey69oWxsy31Y_mWl_lvhZ_SP5r7pTKMhDCy-2lzW4kOcOwlXzTZ1a6pq6rh6PY_vAe2k86CVqujdPWE7y-8xsHae-KoQwwl1zlLBR60B91uk0tGQ5w3EuYU5pAn_TPOpCOSJXBUT5_BDZC7Dnefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=NVBDm8h4Uc5aUtAMlvWVAeE6gOL9y0PKc-8fDRRsfq_fjsdbZMaU2EX0n_TDAOPJMgy30qEyXTH5gp1Vpv4R851RvQlBcTbf_yEaTR6w3lcwuARLn5tG_IxJ9Gl_8g1UQSk54zr1mqZllCg8j8QWTaQvrTMu1t0Vm6lFV2M70IgK3K09672cv5lAYZLBlp_haRqZYFTfMtzmO4V_Y-M6U39ZMoh2X6rYvQ_Y-XoN-O9dLl9QelyKaEimxfd_pqxuKvJ1kx8stSi0s0o5EKekFcXKvfsgqJr7J4Vb4RQuTyVAdAgFhQ119yv2P4aZKi2kIZG5n67JPqNCYHURHLRe3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=NVBDm8h4Uc5aUtAMlvWVAeE6gOL9y0PKc-8fDRRsfq_fjsdbZMaU2EX0n_TDAOPJMgy30qEyXTH5gp1Vpv4R851RvQlBcTbf_yEaTR6w3lcwuARLn5tG_IxJ9Gl_8g1UQSk54zr1mqZllCg8j8QWTaQvrTMu1t0Vm6lFV2M70IgK3K09672cv5lAYZLBlp_haRqZYFTfMtzmO4V_Y-M6U39ZMoh2X6rYvQ_Y-XoN-O9dLl9QelyKaEimxfd_pqxuKvJ1kx8stSi0s0o5EKekFcXKvfsgqJr7J4Vb4RQuTyVAdAgFhQ119yv2P4aZKi2kIZG5n67JPqNCYHURHLRe3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glg8DelYFXKBAPzxb3oLWfdINmq_Ss1H2UoeDNA3M9CNLW64fR5boucyzlBnS1zL5Gq9_ptIyZIc_N6JsHm82SxF22T3sF742y-iLM0SWLQ1U459m9JWJFkvERAXvSlP96SV7cx9WYcYs0dZ9llGP5DndIbeFKVRFrFR6e5O0JmCDTZJXiykvLXx79nd6k1DFhNIyQ2AG3U6gdnspS3i7s9m8IBeI9PXtRLg1O9qSw5emIjKFyFs0SqNQTlt5j2wl1OUMyZHybyBVPgQsPkNPrjxuOPzCBex8XFcgsEe2laOMmOBF3LrU7g3bFc7l_ShvhJUaP24j_viBkSR8AsL_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24173">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdKQNMneHC6rG5P8ZONW1aB_qn7YbKtyFuxhki1o-KOpKvrSAfWPXkK9k3nOqpocKmA6NXTAAb3vodrU-Db_liA7kfANGeY8clUnp2rpUpvu1hcifnsXsHDotqjaQbkFeTg0-qY1W0VSIAnAtdjOq-Nn5tD5wHJJ9vvKZx-QxsuJwBaL6sw7OcXGrsQ1HBghnjCaMdEiOZ6bnNmv_fAEQqomIg_aFUOwt05mKJVWqKdzROVEpzWie7W4FBZkE_DVDCsKKFYoHKdIkMf6oOwQf1e8mkVzN1DoWOQvtCn99Xqec4NBgOp-Gn8GisaheefPB3iUeHXi_EhqP46VDurqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت‌آنی‌میتونی‌برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا eA2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24173" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=qU8mOqCIN9G4DbHiiEQOiPrc-ynPll-Te3G-zxctFx4gLf--KEPEB3rMXlu3_g_7i4vZ4p9UAmMxPhbeWYtLRRU096cnz63ysRYdgk4l0tCBPXfxTTD5sgFV4Ro7H_Ov3QofHj-8Gsl--f01izRyfg5WbXFZokbGCVnEN9K9FL6qcMJJXUKFqk29_LUWo0eohPNXjchnWTw0cKhjVZcUsdIXaS7Huq3bbESjSWsZ0xVLvVSwWQbNns_8NPqZLugnFtm0iin8Z95-CnfqPAy8VahJAyfGTENBaJ_lrskHmr2FNn1pf8IR1vDI89wBpQIrVX5Lh92evywn5wzuq7bgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=qU8mOqCIN9G4DbHiiEQOiPrc-ynPll-Te3G-zxctFx4gLf--KEPEB3rMXlu3_g_7i4vZ4p9UAmMxPhbeWYtLRRU096cnz63ysRYdgk4l0tCBPXfxTTD5sgFV4Ro7H_Ov3QofHj-8Gsl--f01izRyfg5WbXFZokbGCVnEN9K9FL6qcMJJXUKFqk29_LUWo0eohPNXjchnWTw0cKhjVZcUsdIXaS7Huq3bbESjSWsZ0xVLvVSwWQbNns_8NPqZLugnFtm0iin8Z95-CnfqPAy8VahJAyfGTENBaJ_lrskHmr2FNn1pf8IR1vDI89wBpQIrVX5Lh92evywn5wzuq7bgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZnzcXi4VhY_axKvqoYRO2rfQnf7fLayxJmCB05UkLqK7j48x3RGororqUIAXF5Kqq3umjwVbub3SAo3kuSf_phg0Xvg7jFj32zT8fKys3Xn60JVvz2rt1Zj9WXvoIglTkTOsqh3hIl0kMO9c_OaDsiTXJRBiV4SGm3AcvLwuISPNJb4BKtMdGBNtli4pmeAudprAf4MKXtXBflqSUnVRmrHEQ_1AYvxam9SDhk4PVuKXxjWX_ay-XpgPwV9ZkIPsH-pHLe7lz2kc5Q0Poo5Tz_sp9zj0sgDIhylyeKzAR0i106ddi97lUePfE9J610v9sQjfH_fQtfAQjP8V1IrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=MTI0eR_6nXzd3uJpbAw-ApIQ_6iTECTej3gEMe5gxhsKWI6E3hggEAtiB7Q00rucEDmrn1Um2DUaEa5jXViCRW4LC26rkIElhZOAOsrVtugBQaukP36-1XKKXejx7DT4as5e8YAw4L-G8hB3x3HAB-D0Ki6-Q7UMXtta98uB1I48WJ5TZx1jP5TtUayiDFPG65gXU8zQLEhWoOiOpKIMeYWeBwxKMIusFLLjbEJuIA1FweiBTrik0fLK5LwFJbYMIJeKl7DAupTIEFa1rlPO03KKGXNYvbLfw5BNi3jD9_0Ko77idTefbdNiXM56jMGmAUhKNGMBm7wkJDWAv6wnBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=MTI0eR_6nXzd3uJpbAw-ApIQ_6iTECTej3gEMe5gxhsKWI6E3hggEAtiB7Q00rucEDmrn1Um2DUaEa5jXViCRW4LC26rkIElhZOAOsrVtugBQaukP36-1XKKXejx7DT4as5e8YAw4L-G8hB3x3HAB-D0Ki6-Q7UMXtta98uB1I48WJ5TZx1jP5TtUayiDFPG65gXU8zQLEhWoOiOpKIMeYWeBwxKMIusFLLjbEJuIA1FweiBTrik0fLK5LwFJbYMIJeKl7DAupTIEFa1rlPO03KKGXNYvbLfw5BNi3jD9_0Ko77idTefbdNiXM56jMGmAUhKNGMBm7wkJDWAv6wnBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlMIOJlw_iShtuWZ79GtAT_N28fkQm0ROkVh92OISlfVGBSXHWZtQc-8ZzOjL20RgyRrOYDqrP3xeNOyHZC0gHpsiEDbpF5-gxF3E0V1QaH-WtMv4WjqNXExmBgjSb1_hgGx4ffQbzO_22VmknPdouRL-CfE2zNmG6luI2O8jfakT_EQVMzpA9et5BLj4a-c79IoAyyubf3vfZzj4nk6c67cRlsr3RcrVs8hz3EoPWuQq3fJKxv_uUZQJEMxC9JjEz3k0HyCFftHFQovmSooFLetAOSlduYn2zOaFE0YSbPdDQtLxUUfUbSJLOhTLAJh3tgUOJZJ0c06uAEYOErTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y11U6RkLxI9_lsLYqvEiPpmmokN4Q3TUaMc7oSCAmglU71GrvS-xTTY5y44Q6W3KhduxI2KBRimwlN8lDxRb5L74KuxYlXoZFqFQ6yH-xhjKnWR7pIVwaNr8pNK7JfRdeB8nnH5HoqvIeiApTXhIlv1UGoOtxzcJuq8UPZdA4_LqkE_cs_dBCL_HNmcW5qPUCa0E2-TSgEPLlkv8SOcieLCBnvzxaWdTSp7bNU4yDAKdz156J2NqIT_aHSshE8NKlYTiTT0Hr8sqqKLceIG26agNx7PpqneylOyz_Xp5n5NFqyvxL-W2UuF8DzBMWrW0rd9PJPpt5ViaFpTD-V0rAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=ZxAou3ppvF4Hg33_kLYCs8Gb_UFPxH4hBcjLqwko1UU_hdXg-ZqIJzk7Kg8Mf1IPmjj2Tm3VHNgExsssYmD4SEBN0TjSuK3Y714ga-0vR6nQd-g_pxkH1FFYWBQnUqOHiylrCLJ7rB8kkKmzzKbiHGQ9cWHy1krvNSSLSOu1Haw_H7trZUR4moxgdE2qt96GZUaL7OC-FQfd-Uh_ARjtQlgPoHtnOpXI5Gaf2UbB-hkG0AMQt5Nb0droy17T8NhBgB2bh7gg_DB0mwBHek0fx03dPD5sG-X9_1xNhFnBNt95bKOW4G4LzNJ2gOmdl01C7cCqSBzJOukticKu4HJOJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=ZxAou3ppvF4Hg33_kLYCs8Gb_UFPxH4hBcjLqwko1UU_hdXg-ZqIJzk7Kg8Mf1IPmjj2Tm3VHNgExsssYmD4SEBN0TjSuK3Y714ga-0vR6nQd-g_pxkH1FFYWBQnUqOHiylrCLJ7rB8kkKmzzKbiHGQ9cWHy1krvNSSLSOu1Haw_H7trZUR4moxgdE2qt96GZUaL7OC-FQfd-Uh_ARjtQlgPoHtnOpXI5Gaf2UbB-hkG0AMQt5Nb0droy17T8NhBgB2bh7gg_DB0mwBHek0fx03dPD5sG-X9_1xNhFnBNt95bKOW4G4LzNJ2gOmdl01C7cCqSBzJOukticKu4HJOJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS6__bZMZuKC-DVp2Ngh8b93p5rnHVz--dfFvmoob3lOKw3VwC076eG0BSN-TUU9OMUNA7EfIkcKDepiKcT7CVvTUs7JpXppJgvQ_EczHNDRENYEM6VwXXQch2fFnMbyLV-N02bUjWcyqWKdtTXsn5wItdM0ZKlQ1m7PzWmMiBFfdOZEPsq23DhyqWzfDEFnMU9zilDyf7G5GSX4wHn5VFoTdhlEiZm7-103qITwdX9xbV0_1dkXawWmcniEk5iKM1IGP7kWStoeq8KFXR6_mmHN1KchRTx7xwAPTLdhMsh6bBbTiKCgm2lR4AATbFfl2yMfYLlGKiaNuu6D6WCphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24164" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=jASTI8FApPvTDYxNSsgtPiJKnIQWOVzTNJ6S6f6Mk6GwkX4Biel3aO0twCVHfYnCZVdzjfVsQpwdztIqMNQ3VUMYx75x-GAQ76WnifopAwUwctDj9UgHABQIHZwvFhVJSHX-Q3M0o3D-eyEajPiVbuxKBIc-sbcne2hQVo_OHy1YY08C0jLWN9brrgHAWyP9m6wcKyEYixlqa_dTMP4lr6fTq5JhAHuJxSoaR2pCopLpKKyv278Sv8o9_LaswZ3Q45pO44cOhnaILN9bjUvxoSrkMf4jiJ9TmSaJr6zpP9eQtAlFupX8vBMQb3Kglt3bE95n5roZDCy93slS-oJLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=jASTI8FApPvTDYxNSsgtPiJKnIQWOVzTNJ6S6f6Mk6GwkX4Biel3aO0twCVHfYnCZVdzjfVsQpwdztIqMNQ3VUMYx75x-GAQ76WnifopAwUwctDj9UgHABQIHZwvFhVJSHX-Q3M0o3D-eyEajPiVbuxKBIc-sbcne2hQVo_OHy1YY08C0jLWN9brrgHAWyP9m6wcKyEYixlqa_dTMP4lr6fTq5JhAHuJxSoaR2pCopLpKKyv278Sv8o9_LaswZ3Q45pO44cOhnaILN9bjUvxoSrkMf4jiJ9TmSaJr6zpP9eQtAlFupX8vBMQb3Kglt3bE95n5roZDCy93slS-oJLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4DDaN1wdOiA-Kiu4GQv6nJ4d8OuowsIpduPgmvIpfXf7uUa8sJpf_Y0QWzBtnP2xgYZKHOUg8hmIAyF1X0SeWlbBXRCFwx1CKAX_RSDOtOZW0ifo-FhM3pdzGG_9MWCGmoDYp4COb5qfwPScUMk5_b6aqQeJ2EwfJf67nmuxg3BmVbNBtYByQclupNqx2toz9ZjWBTc-XuV5yknVcQhjlUAhGvXfTLTG6603wwdaX8adjmcdSK--YTDmWWgluBueobrGVyfosxsfmsqX5MCohSFgk2jPfCVzydkJWNGiAcphmunmvJbbmIv7YEG0FsKW8bj435H0zOjfFUCJCs6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A99sybUhim6GssUmN9vlZr7W0IitVolySeDiWP9a64tNrIJiW5q7VCZDcC7XzWPxAm93XoYjL9BJXufgDUOY7xMoh7E53K0wRnlTy4Jh6P6GFTCBbjmWii6nuhoyICLn-7yNxLWlEeBYOktFgN2XIP_tKVCx6i6AG602NHsReqdzSfkSARrTJc7EBB8B8iXZeVCRel8UWSqZJytfa-7jDesSYW17Wvab-PdbngDPBIrmbKoaRvE-P--NhIK_sb7zkxFrLsHajHvPfkot5e7uFAA1lkL8C88RnG4abxRfKbGmS3Zz2HrxsrlZU7WXlQqEH_qoI0rP-owmT1Rar6plJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODlPLlfbu99I-77VGrenFgIPBXj7xTtN5D6NZOWsyRvBUkjOofyIIH-62Lo8sF49sbxg2RKckcjWBG19rkSFpU_tpV5qJ7expwBuymbKyFuZApuiHKE_HiAu_YUE-UIXjtpjkpA-41N1Fr3WA2uUCxuSX2KD4thGQxq07bSnyOg3lLmu3GmrDYA4_KA8Kw0I6KPEbmq3EYAg9DAklVkXkUNH5V7Fk6h3He_PNxNqzyqYyx5D8In68Bu-wwZhy1DzsrQT5LsQ3YqENyfvijDTFmqzq3bcGJSR8JmgN-nhiQOzbr1rKq2wTFzQyfCzC_GlUv7Nh4UKJh_7nqe8yv6row.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOSW3sZpR8c5vvvB-S7mJ5IuhA2Q-Qhm1V4kyyC5iOnz9TsVZBX4FoiTdxbkMPFrk_A4q_pdY16wehAtvQgY8WESdbJCS-qwLcxGV1cJpv7SYqclJK-Ot1tDsnFy2oa39nbYM9HX1_h7e7zzJRzgHnzSMY7c4UsoHeeBCI_L4WEELuo9-p4x185WjpJO6-4j-qKlKWbhOppq2ePYps1yqP1_MfujelnZnsZrUWJkeZ4NCbJ4D-urwu4TkJhgstBBfyoyPxpLp1PsT2Exizsib9jnZTPOyzJB1z4M2oDxsYWxyOL1xGN2GpCZtvA32y4gkBmMec22ArRX5XRPno4bJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrMBmM8TZdUod-fW6OjKC4HweD4_9NT8jLwyFdN_IVY05Q7F0h-g2m-bPQNGJY6HFSbSSTBBECBvZ_EPUuMGLV1ewjY5F4sn-8x8OMCxr1iA8bY9e3Vw6ABDAI8yiAzPerosdLWA5XAHhGjdDKkRZyCwTJOycc_2xEPEyBDiICJMCk-MB9LQ_nigRO6knCQ0mHnDyDOEZAGGwwNulM19V7xFIh8GvP7Ef0GP_Ee-x4RAHDnHtJ6Sm7Y8omLtVpaBZJL0fmCbiu2ji8F2PZYI8nhbBrRuF3H5jQQROe0WZE6KNbG4_nmhf3MiNFmOgTE8PFpXTimOmyQF1rUKRt9ahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU_RB6FuNBiIjIPuD-1xmiJUdxeUAN2ckZdopr37RLTKzuODrZFl7yOXrQuuMZ6s-uy1-VgrMeU6EIjg4NGmk07_6khApZiVtQbXWRtXGVoMp5saGDFLlSIQ44BoFNzMOHguQNMxM9FHS8e6vL_FOFUeVAwbMd76W_RYIP65EDeew1B5H3-VwkpYw37faquIhZTeSqCIDywcFoexQKwEDxw6FTpmBDKRtHW-yuAOSZAHVjXXlTXy4_e3ScHuS-hEqZ-kfKq1MT0ybbcqwlfQOTVKJxF8_zC9gZZ6lhs9Tc4bWR5K9IHlsuxZ5c9TrBgRy1DBkKvDDczYtIxSfZoFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N46nkOH_C1UDtrTFIosF8vDGHVZoQZzb47aPpGD8VhHSoTwLrZ0DUXjlqq_l5GzSfkTkJ3frFrZ_Og1KLGpx4kyWRUaXSvWMX9C9b3ZgZU2sBb6ZHp9KU6sJEm_E35uss_qLCZxl5HB-bDTkoCEuiLsCunK23KWCv2eNJ_sQYqoFFjT5ZtnsgTE3oZuJU1nCB8eg_tIdS51qDG-r7IlhoDKlfNEgDUecSdm29vsKy6yW6_5S18AUrk8R_4g--UjJjtun1mTLC665pctXvXnqTwytYqiZgIL-8CDK4CPtGAdGFMse9qN2Hga4dXS6-dtlDqnQF2LyRlhwxJEWeuMr3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_4z4NYbFN_HxNbFAExuQPc9BiWnFt_FoSjP4ZzW71s8-n7mxPx_EFLPbgN34EEMxsEQ5cKgP8Dj4jRSn2H85Jh6dpZjkRPFp34BOWnrLJ1vjZE9_HNbMHPk8ojm6BMmviFTuDc8Kiuv9ighbKx1SMwBbLWzdTUkbrl3ntyZ7kTkp2gRNEIS0ur8eAUGbGN2v9vAAvD7Z77LrtsRUpq77--jX7hPs1joR5-TmLuDp_oqa_2pTQnZQ22gbSVhMR9DTlOzyqyuBuUAc-Eny9Lwsr9cdnSTZiPGTO4nGH-smtFlwg-VgWiLOItWbf3MeDZ44URB5FAs6RV6UoeGhV_FUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=EJoN174EfQlY6NrzirYCkE3gaY_H3SBDUXqRQg6f1hGTfJu0wydExnObwQ6fDrVdhusSEugrOd8ChDnkQtDFLQFO-J950E3ikuL6WQIRUI7y1bfnu3k3kJ-PqHiCJypQVfAb6Q6hxxEZDOiEvYpJ5XDKXXGsJ6KRiOtQlcds4Ca4OVTZ0N-OTBuXPRGXMp6e1QcOoOy2bCnErssQEaE9VyYq8VOFV2743qndEm4uXW7g4KeKiZ54dHZoYxLqSdMRhb1C5CppaBLZ2JArEcxlyM_HQoZvP97fX6DeFuUm-Hvhq28FF6auB2fuWSDmjjb_RXJOYH1M3GmqFgH3THCFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=EJoN174EfQlY6NrzirYCkE3gaY_H3SBDUXqRQg6f1hGTfJu0wydExnObwQ6fDrVdhusSEugrOd8ChDnkQtDFLQFO-J950E3ikuL6WQIRUI7y1bfnu3k3kJ-PqHiCJypQVfAb6Q6hxxEZDOiEvYpJ5XDKXXGsJ6KRiOtQlcds4Ca4OVTZ0N-OTBuXPRGXMp6e1QcOoOy2bCnErssQEaE9VyYq8VOFV2743qndEm4uXW7g4KeKiZ54dHZoYxLqSdMRhb1C5CppaBLZ2JArEcxlyM_HQoZvP97fX6DeFuUm-Hvhq28FF6auB2fuWSDmjjb_RXJOYH1M3GmqFgH3THCFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WenGE_zY5OIr2Bb-j-r7Nvle_7LFDr1xUI70BQtISooLAkH6D1L7Y6G1b6eDwlw4Dtu2rIUb6YmGUsm5cWFGrRxE_-ieeTXL8HRFEZvXyT-8cst9BoIprYUBSeRN8fHcP37T0KQZimWRxjhvnPCotEzMiW6yZlVrzJtwOio6mZHLTnsUdDtR6Qc4VIz8uo-RVOMG0EYE1zWGZp2gqVAllKHj6mba5S487L0IDTZeE6-bBRtu5W_uY3ozGRfXYi7ZNGfWIGQhl3qqwpRzJqf1qkW6yJ0ON-amK39RVIycPagQXqjoYrJt7fH04pSz_Uxpf-1hin7yB4ahNyVodVqTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=WujZv0pnrHVI9kIhomI4PDfmpc3Tebc0RE4mbX6ok72oUQn2wzVriRUuXhQwxWAAJ5WqDHK5HPtZJodgLSymZuofIrLZAPr9KnzAhp_F6gixFmt2aOvPULGwVTc8iRI0lWhwpr3EoDeLgP3jtM8u5wXUpMwsF3MhL9IwdiBmXOhqlgmrVKMRLDfwCl8YMRNNkm81BH3aNcg-wWkOCRru4kLA555KHL5Y-clCTSYd813IDuv3e-Sp8VSrTKoa3Cm8_SsO2nCK-dQROfM9xfXRTiEhKpVigznSORZpYZZQbtK1nIcZWLFs4H0EfBt3jCDIyd0IWY5kA3Uq-O9ofsKG-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=WujZv0pnrHVI9kIhomI4PDfmpc3Tebc0RE4mbX6ok72oUQn2wzVriRUuXhQwxWAAJ5WqDHK5HPtZJodgLSymZuofIrLZAPr9KnzAhp_F6gixFmt2aOvPULGwVTc8iRI0lWhwpr3EoDeLgP3jtM8u5wXUpMwsF3MhL9IwdiBmXOhqlgmrVKMRLDfwCl8YMRNNkm81BH3aNcg-wWkOCRru4kLA555KHL5Y-clCTSYd813IDuv3e-Sp8VSrTKoa3Cm8_SsO2nCK-dQROfM9xfXRTiEhKpVigznSORZpYZZQbtK1nIcZWLFs4H0EfBt3jCDIyd0IWY5kA3Uq-O9ofsKG-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=jcg-OnDPEmzrzZV1-1tkKbNE62freP1wNSKPjc-UK-2IJcU8fLH84VRTosmo10GcdrMR3ZncpBFrS-ZgrWf6z5-1-vOAwqWr1txuoePAEtYtx-tXSiy4Aupc4H3AHZpHRQI0JeSHPmwlNnsual7Z9VQJdtlaE2jSF8_u2xaUYHb1H54LymRQ48QUR8UijF2jt7Gyu4nFW5VTMlod5TwLdtOz194gez-e9M25NW9pCDPT3S-wqlim__-ElwDzezoIXY6oaXylbKTGdtVWHxZYn_ex3MxM7Y6zkA4xCUXrjTDAghR50rsW5nS7rtzVlm7MUqbd4MrkslL1Q7XDSPq0Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=jcg-OnDPEmzrzZV1-1tkKbNE62freP1wNSKPjc-UK-2IJcU8fLH84VRTosmo10GcdrMR3ZncpBFrS-ZgrWf6z5-1-vOAwqWr1txuoePAEtYtx-tXSiy4Aupc4H3AHZpHRQI0JeSHPmwlNnsual7Z9VQJdtlaE2jSF8_u2xaUYHb1H54LymRQ48QUR8UijF2jt7Gyu4nFW5VTMlod5TwLdtOz194gez-e9M25NW9pCDPT3S-wqlim__-ElwDzezoIXY6oaXylbKTGdtVWHxZYn_ex3MxM7Y6zkA4xCUXrjTDAghR50rsW5nS7rtzVlm7MUqbd4MrkslL1Q7XDSPq0Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=vApQEFfXm8rDBfjS4Fd_Xcgb6MN05a_SEesyXClCUw_03Unw3vCUmu-iGIDzNYQb00A8YOedxH3dYycna1urWs7zIFTjngaaxS2sOCg3vVGWKt_efRCbpUxEGQnGsm2bYGaAaCUmCmQ0wCCiRbPKaycJVOpMAqUWtvT7bKx7ADiF-x_8scDNTXxyJ6wAhfs6osAWT494bwlM750cxkchGb7p73SBvpDLInCg0Xx42uixoxV-xAUKNF7jOCNyOdXawAu4NtoKNOw7I5ApeIIYr1ZiPOrcuytiuP2VQx2cuMIs6jn_OCidXoG03IRV9beekFsGHL4Z0STS_xGaxgMZiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=vApQEFfXm8rDBfjS4Fd_Xcgb6MN05a_SEesyXClCUw_03Unw3vCUmu-iGIDzNYQb00A8YOedxH3dYycna1urWs7zIFTjngaaxS2sOCg3vVGWKt_efRCbpUxEGQnGsm2bYGaAaCUmCmQ0wCCiRbPKaycJVOpMAqUWtvT7bKx7ADiF-x_8scDNTXxyJ6wAhfs6osAWT494bwlM750cxkchGb7p73SBvpDLInCg0Xx42uixoxV-xAUKNF7jOCNyOdXawAu4NtoKNOw7I5ApeIIYr1ZiPOrcuytiuP2VQx2cuMIs6jn_OCidXoG03IRV9beekFsGHL4Z0STS_xGaxgMZiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24148" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMkwgIiK0sSB3hmdF8Ct26p1AxqX5rvZDSfUy5KEYE4eEGU6zrsHJYLe9e0AkJinmtgShUzxAwAWur0z8zYjjL0DlQxhgAhq-lNEwM6KujwhzPOhrIAD6P7RIqn42yk3eK0bh0WF9-mX1gJwWnX4sd69qxYPw6TDgGydYdwF4_sLI3OBzgdfeQeO9KV9EQnz13iUfOvqxC-GD8ftfycuP8aAXBnBq5k0C-75k7tK0me0HWiDYlf7rzn7Q9D2eWA5e6kEy1evbpC3tT3D_CuU6gvO9PBl3_nTrWg6nyK--YwLOsIgMd972j9-x106tK0gKm9qRTNGWr1ciQE6dPjFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1gnpopHoLiDn1V_roPcBmvwlIaqVx9INNLAtnukaGAXo7XzfX0AXCMDsLjCWt7s57_1dt5VB9fmULFzpm_qTfylENHvROITRz72eNTayUSu9i2QSZe1KTdQPjcOHaTP3Ftc3x0ZC1sHcNkzlfUa41EYj2Fznyo_EHrYTqqg0R-3kqnkzILNifkKibvleAECn66nlTQty9q1_giy60r_7tV4L6tNW8rSal4YS9Y3L5LkeRuXaMYKPTiK7YdZ3wGmuCu56Vt2SX3FhW6_b9O4tI8mgn8jtvh8JgW0XBJoXoJUhx0z8yWJtbFjRm9twlKOI39v_KPYzJVehsnK5SFSKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس دقایقی پیش نویس قرارداد رو رسما برای دراگان اسکوچیچ ارسال‌کرد تا باامضای آن اسکوچیچ باعقد قرار دادی دو ساله سرمربی سرخپوشان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24146" target="_blank">📅 20:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1TlD_CfUVgyhKB1kQoD1FA1vnYawc-vYP6Tv6_8FJExkVPDf-9GOtB8ZBvS4lZ4SLLCvAjFhSgA_AdZIXzYs8lZtl2joyuYzrCTInzuPcJb8DXBC5vWsikDTm6yvz_0MWChKzR5bCIxYf8dwlmmDyvXxAuXLK6-ynPeJYtrYmv8hkKs2qMhFa8CDQVffWlpx1_wTeoghOOmeC2_1GcZi3BEba1xLuD1uTkHHHlbGUVIyRFo8ACE-pD5bSJejMxRAYeOwqFlvsEGN7czsBRfurb6a0MRNRpVKYcbegumcu9KBdY-SpgKhuhsaMI7uIRFMz72qFHW2AGuusk08KFQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا؛ باشگاه استقلال امروز باارسال‌نامه‌ای به باشگاه شباب الاهلی امارات خواستار جذب قطعی رضا غندی پور شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/24145" target="_blank">📅 19:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qubVVEIHmROZELhtjIo6wcP86QmM8IvuEve3dEquy4jbAJYLMDTpUaxXNS84LXclnowpVL789KkxgMGB1rk8mzXIKl5FFPZ-0zdwNWlP2DxAJUx42NCH2U-5mfuvwtGwj-FctPQnF08ecldJUHoZ25TYmjypDZq9rd0OxLgQ8WAo2GkTGLDqbQFTViHyGc09kzIRsInFRkxmD7_8T7v5g3FK6KzThpaPLZ5QyVBG4o5AHKxh21iGPKuw6gYXwBUBRQGwYvQYcokFH2Zgsm4oiW2lgzdzJ1mcGDiKNwr_mkP1xAT7AkbkIuZrFHawdQKDZeUe6P8vcu05Ur018Uc5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIqNOs9MIwhVACdHqsW-b7AaKE1s8Ex6W6ARMu5LGBOT2byla42_DN6T_UCYcJNg_iP0rkFc1_4NTeRujc_2-7D0YUgpuJ6wq1QE9Wg5agn8E99yQS08-KdGxnXPzaiCQO0n-EnR5kU2ZPEMZ8FAhhsAjAEM_XI9KPYlbrQgutOW7qA11VZNsDrEVNX_bG4eKeY0OuHx431svzO3KOrm0ZqnySbk4dMUE3ZBgoKLgjSm2_yIVzjLyWC2lUZRikw419RLZXYcgerjxZYHRHr_hWrwmPPkflRJQaYsXHyV57uWH6k_ZYVBThsuWxK2cu4FOVz2N5ZHn1qlBmIaiyPiUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24143" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdXNr7qMDD5kUXxgAs3lzBM7fSZxsT2MuRmrgdn5s2jBZuG-DnzCAzQy4YFgoZ5I0YgqyGR08sT9MNC6DNTV7HyZIV-7anVSTDPtxQo-K3MzsFh_JZ2KTXPwq5KERjhiHbj31uKPRc0vAnO5qIF4Ldx-oI3G1tTxeo66xJufK0e4mDCstS8cTLQ0KmJj-wwvQ1wrsoIeg7Of_6CYxwnLWMf9czmqct9kZsqOGv6Eo9h2tu3K-5GJK0du5SW0XI9CL5rFgtyqT6p8g2xlVvg6RCOEsDJzHUlA-CcczeTXHgYx6d71IHhUS3pBy5-jWsQlZGq5ISz5cE5v7yI5_hkEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24142" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=iOT26kQAM77kNY2n57Z8KeJTjh-K3tEwRnTXmzHxrLH-vdSorzNQe7IdMku2TzfljOvIicYmLEP3LomYVaPAfje7J3IYWM_CGTIj0T3Sa3-zki001U_roVtISZJbTlL7LmT5A62udJdbJgyYDjootrcZpWRwwSQYQr_ij0xKil8GAZ6iYAoxBL5CDxrCMH-CUj_FOM0TR55jYcj28lm_KNc3MCfOwcC3E1chV8YOLC47vN_vOAZ86D3EoQO-011868vSE7MhFY5BvoIVTRVihT7ExdWFekZkTfaWHH5y8PJJgZeI6SOb-2TrlfP20L1qq4Kkm8MtBMMRa_sMKJkOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=iOT26kQAM77kNY2n57Z8KeJTjh-K3tEwRnTXmzHxrLH-vdSorzNQe7IdMku2TzfljOvIicYmLEP3LomYVaPAfje7J3IYWM_CGTIj0T3Sa3-zki001U_roVtISZJbTlL7LmT5A62udJdbJgyYDjootrcZpWRwwSQYQr_ij0xKil8GAZ6iYAoxBL5CDxrCMH-CUj_FOM0TR55jYcj28lm_KNc3MCfOwcC3E1chV8YOLC47vN_vOAZ86D3EoQO-011868vSE7MhFY5BvoIVTRVihT7ExdWFekZkTfaWHH5y8PJJgZeI6SOb-2TrlfP20L1qq4Kkm8MtBMMRa_sMKJkOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه ابوطالب حسینی به مجری شبکه افق که به مهمون‌هاش کفن‌هدیه‌میداد؛ فقط خنده پشت صحنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24140" target="_blank">📅 19:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1gqooj05Zpw7_IdOjbLgiR7hVwtG7xGtWsHzdY7cH7g6QAU0Mfqcc8MlIcDuGyrjsaO8bOtbe7kMlBKNPHMu-dZkY-9pKdDu63kGa7iYHpBjT07BsJqjpejvTaKT17JNzUXKTdJU6RHYik5_VGVqo0r8CEs5i7xGaXyqP8xron-clQrE4CS5TbMMqaRJykWRhD-I_OecJu5Dd3R82qMWJlwkqxW7M7Zjy2tECC4XQjLX_teQyixwhNwdMKuWz98sPfiQ_ni7EIW0Zp5ysprzjfSRCM1OpC8r4RpaoSnWmG_feDoSobytZxpMnk6BMkYxbYRmIbJyqkQUgc5bK2uyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24139" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxCaY1jtbg3AAoehYJ1WiEgU5ZDNGfar-8gddSeyQDsqBomBeyZ-V828HrpcC5nr5yo34jZQ4rLySUw4fbg_F6LmtoGSt8XvZE9uMfZjbv98259MlBEBm6CcNBGRH7xiaBVZNhuxV4yyJOVzggT7rTHbueSX945dgemCJiG9EzXHnJmZwUNdWW3RqlT0hOTzxorCHP4KqLrMucv1v2ySWLVKvOkRNTshM9qef6w6vfKwpzERoZJSdkclKLgOinvjDT1KLAZx7Xk6Y0DRGra-WSpm7DMPxplsAHfZ-ze6KoxDbN2FTIwgr7R6n9LHwLdLy9nv6vgMcnsATcFynFk9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
بازیکنان‌تیم‌ملی آرژانتین اینجوری از گلزنی لیونل مسی خوشحالی وذوق‌میکنه. از اونور کریس رونالدو گیر یه عده‌آدم اسکل و احمق و تازه به دوران رسیده مثل ژائو نوس افتاده. وقتی رونالدو داشت تو رئال و منچستر آقایی میکرد تو دهنت‌ بوی شیر میداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24138" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMJnEyCfv2Ef6JBb49L7uIo0LIpPnkNnpFhzkFWQqwn0Qfon36eQthe7Zex45U44TmvGFVmnOses8aXRL44Fgrv2G53TqaCr3KHzwmOEmRf3c-xVP3TUDfq2inDkuI3ggUyXP_48x6I9l_Z012_d2whqW1ZGwJ7V872NopuRLBjQotL4600AsHsbcw8so6Aqpdhj1x2jmOra9aLasw0G6O39RSAj-Q3y8tOPxuEHRKaCBHSc0VnPbTCnAU0U3kfs6h6HxsFLSdHZRaciSKETlZXiuD0N4wXhTLNqkvNXaAypZknGlMeb9dMwURXgFmpzXEYc0UYzCLKpMYOuUQ2ZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8spNeI2PBFwiIa86TdUFgxw3VTpnNxn--tQlaMgFfIdHeOK0Jj0kRDVgIzs3b75IX23F5Y4GEVpBwPj2eg300ZA4Q3Xv-jcK4MZ7O3eK1h4kd4eimRplBkT8sCZhxLbOjrtqvTZFbEeczgeMVZcR47kBZ7m7NU4SVRk55c9IYi-gL0qxc5uI1dAPCcuG08iSytciCwK532uqcMUsDDqK_bm84z1f3xphqWN7kdRrVWqr-IOTdHSPZnVd9T5dl-7x1iRTdbLLlt9pUj9_XY5R2SqvG_MYKOKAKXpVIho-jbLvt_SPTyjKv_S-HNgQeoFNuV8ggXT6U-vTnDu36A2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv0Yb2hbF3qtoR8n84Zj39Sy38Ct-UzeHXVCivWSRZ3Tk0cGAUbWeSCbD303t5hVVtCux00RqqEtOvKcwF3Eb3Xc6Ql6qglCTD7c0S2OgwYKuhwmTVL4q2ezNVAO_I5STyupTsr6VO5bzLKCach2isqIvZ0eq2mdnGCqjJZ9M0q9uB17f6WFj_8XS3rjVDQYUiT6iBpWVJvkokh7regVjqZucgNCtc7wOoBLfNKWN3WPShrwvjTuWFPRI3OIx9G7Pma4IAIG9lHXxj421XnpKXkGR-eItuKFXu3knMz0V73Obl48OaaokZScLuHxk7x0aIGXECsBPkAu7MJfY-0OgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfpj9CYPnl5bcteTVf0hO8LMoWWCwwYEOuN60DEe2ixK-M_SCCBRTDu7Qe760dPMS9njTcBNlrxrZNzmjFClUG54V1NsLveCKXDy1ssKJqRsFqrgdauKDgFIdqa9QeAfEMm9SFDhfhoPGuMdLytirUVPqFu8yqjI2SlFjDKVr0MgENyzuhqZeyWqXkVJvxeEzMlq9JXDZjqqImgMW_tA311Y_i7SW7tgPu4J_trhrwrJH7svSlO-d1MH79znhLIl9z85iZxY3ptaYn9OJU10N94_InIoJgkuToPRQhfEbvWylRnBX7Tnux0iBOXEaat2CVeT8n8fo7fmqqjSCxoS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=jZRyTMndFlE5-xAz2lSOvNMIXnhJGSiqjaf6mIR82raMUnYPb6INy2n9SVoUSJUMC7U1x4ZtoInp9TZTpmpm7tqtLg9uUUcguAPUr-MnjqNWUo-9Fjpwr4qg2PpUmK5WTXFA2TAsHSYQkU_nLmfOcvnCfCZZF9v6j2MvkZeHBsAHTXyXVqPUMjRn0S1vn3ZWYQ5uhL1XWebsoSnGtkTqNL9sf3e2SU5hOy28zTwyIhtH3NmbCAxhQ6jBIDm3jOpcRftianbQlhN_Qz383WC8AeNOS5ujNHbA_hfEACYB71SJnWhsyXIv_cGelXzlufvfynMan-tyikNC0uJmcehFUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=jZRyTMndFlE5-xAz2lSOvNMIXnhJGSiqjaf6mIR82raMUnYPb6INy2n9SVoUSJUMC7U1x4ZtoInp9TZTpmpm7tqtLg9uUUcguAPUr-MnjqNWUo-9Fjpwr4qg2PpUmK5WTXFA2TAsHSYQkU_nLmfOcvnCfCZZF9v6j2MvkZeHBsAHTXyXVqPUMjRn0S1vn3ZWYQ5uhL1XWebsoSnGtkTqNL9sf3e2SU5hOy28zTwyIhtH3NmbCAxhQ6jBIDm3jOpcRftianbQlhN_Qz383WC8AeNOS5ujNHbA_hfEACYB71SJnWhsyXIv_cGelXzlufvfynMan-tyikNC0uJmcehFUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
زلاتان‌درخصوص‌لئومسی:
من تو دو تا جام جهانی هیچ گلی نزدم ولی مسی تو دو بازی پنج گل زده! براش‌خوشحالم‌امیدوارم همینجوری‌ادامه بده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24131" target="_blank">📅 15:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og8ybzl85zviR9l7cU0h2P3jT5-XkhE-QHwJOontszTYEfu7jhG2EsTPgH28jgMvx7aITBC-FyKIYqH71ZvnmhvjwUZA_2AahlsmvhMiv3EyumJvXNhpxaQ2KaCywpwr1StARj2YPQIGqahXVIS8DLKLwW8r4N2m_rerPaR6m_ImcO-Dg9LW79syI_UzU5j55dfo83SAQmS30UyCuVibpVqQBoF8HRAezSEkOAiuDLRDSoUCYDrh_UAghkjq_paNiHTPf8eVVG5REejtlDk_NYgZ5m0nHF4cTEA5nbZpoCG3dtNLk_zrRsUjJT6d3X7lJxNMKa7SfWLKTmZsoEHTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
فرمانده روبرتو پیاتزا درتمرینات تیم‌ملی والیبال باقدرت هدف گیری 100000 از 10؛ عالیه ببیتید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24130" target="_blank">📅 14:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ-o-cOVFUPP7FwDAziOH7TgaJD_EKB78N1iwWylODakeBRpJlm0ttiHmBlPsr-rZAewufClD0frWcUgFALEn-moF_fYKSqvddToIofILFWkdlvqoXb_npd6FtAmzOivGVboQc8LgnKg4tnYgh9DbvtXi7wVZOr--BbxFI6g4nzUqlhb24Bch4RqjU4taI3Tsgunn2bui9S8HF3nSLnON9U0wBZFYfh1FEbeE0-bHWf1zm6hy-AaYRdhU-wsZ0KdqevLK2EnNlW85_HUVjjgDjazL2Z3fhfbbEGgTCp-egwJbrpdh_s56HQIGgJWLkHpJlQcTCwnPdecpgAJC-oVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24129" target="_blank">📅 14:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T10hkqn-4YaZ-GihIHgkoRO_EdBciLDnWYocCKH4ry2ExmoJAJlJTDJXGfIisns_Y21Hpm06wngn2pIpjpzBLe_3Zuc4307RBeEPIy9wZQNAt1XuCBVcQLozBKTKsVaul6hQUl-IDk40U_TgHu5K3bIZjJNs-GNcRhCxB8Kvznz7yWZohjaT0Yxu996FaHb9JdB3KbsSJ9O5CaSimwZxjIsaOWZA4_e9SlFbxWEI_MVDJl0IbV0xJJ9KtnAjuV9QQzqJjRrX5WBNeNWd4wQAOzrKdYQPZxVcJAYuJpwElO8nMsi0Vk24p24k4AIa-fuwTPPtXWX3kedMVr50zTDdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24128" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=f4uUfWN1APq4ZI7rNhaOE0FF6EZ0mQlwkJW53edGqN84m98K8Oiah3Vj4Rmpc8vOoUvZsIPBHPv8NggM6O07TNjB14b8PERwriRHhLqDLAr_zvkleGSxurPal-TxW4A8xrex3iSz62oeimaEyoSlZiqFF5wDcOFwOXJpKpyaOIl17ee4TCfhppnyr1t2n3Z7yoInWEj3QA-661U9f52PlEWEevwsIqb9M60y9ZyCrgD5TfCmFSqCEY6n6AnfKzqH8-QyqyWo5yzdesshNmfPNxG4_8IQTEZuOKoUfcqSolyAuniZH60H7WK31WOWcwqLuOOE-tcWxLutguvp-ucOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=f4uUfWN1APq4ZI7rNhaOE0FF6EZ0mQlwkJW53edGqN84m98K8Oiah3Vj4Rmpc8vOoUvZsIPBHPv8NggM6O07TNjB14b8PERwriRHhLqDLAr_zvkleGSxurPal-TxW4A8xrex3iSz62oeimaEyoSlZiqFF5wDcOFwOXJpKpyaOIl17ee4TCfhppnyr1t2n3Z7yoInWEj3QA-661U9f52PlEWEevwsIqb9M60y9ZyCrgD5TfCmFSqCEY6n6AnfKzqH8-QyqyWo5yzdesshNmfPNxG4_8IQTEZuOKoUfcqSolyAuniZH60H7WK31WOWcwqLuOOE-tcWxLutguvp-ucOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جادوگر غنایی: هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24127" target="_blank">📅 13:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coHzvgukeXWSs7trAov8AdM-wxpggOygMgru22oL1rWrKEeFCAkqcQh3VWHNJOrks5le5lmpvS8wjEZ8p_V__wwjRrENgM1kjCkCC9aMr3Z-Xn2XXzUguYL1L2F7BeIuin6tRrSLWdJ_pu28mRFuJo8aMW1TO52qehMAHhIp_qecIui1cKAgLrP2IsiyObDdN5bHGvYiJr1790xy_LBJDlS8M6ryESAQncAQkD8AVesc_LdQd1dj5IQNr8B2SfR-gaBwjqaqly2u-jYvl6Oq7IOnjckEUeyj9lhpLGlPNGlUJRbUgDf0KnR-iUrqS0PuEhi2D0Al76gEGeNBzCtEbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سه ستاره جام جهانی 2026 تا اینجای کار؛ رقابت برگ ریزون لیونل مسی 38 ساله با دو فوق ستاره جوان فوتبال جهان این بار در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24126" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMwaeA-6nwHP__PypJjTiCUCcZtz5p9Y3BxPObPLFhqgEsOg_lViGCZpqVakkF_IhpFG_wMKR-4Qo3Ly8H1sogY1UdEJ3xfHj0G9dVqSS9VmFhvDx41wf97cdUz0oP8_GBCEm0bf0qiJ-imORa87tnsQy2mFLs28KS0YtnqRz7rBJuQNV31i4r8oYzfPHjks-x7Bcl_ek3Ld_pf5LdJbdX0ebHX_fEL46xXMOQsNtHyhuo4Q1o3gXBwPt1HhMxf_YeYEA3jo7F3481uAbRc_jEUc8IT379RX3NohdA5eUWJmJ2x94aJoYBnjnMEa_pLTyDYkeE7y-FUqa9fZBjYngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از خبرنگاران در نشست خبری قبل از بازی انگلیس-غنا از کارلوس کی روش راجب باخت سنگین با ایران به انگلیس درجام جهانی 2026 پرسیده گفته اصلا یادم نمیاد. مطمئنید که من سرمربی اون تیم بودم؟ من یادم نمیاد به انگلیس باخته باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24125" target="_blank">📅 12:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5tGlhSYoDKelU-VROs7x1UY5ePIhPadqkX24Mua0xdFbj7JsKSEgCDFhAjc9UfOB6AbtFeRhDl4_3NRVFWwA_iZnh9ZiVvVU3tEuhhkUN-neQt8Q9rUA1qWx2G1lSx_DDQq5Hv0VFvf9JSR3jRS2jxnim3zK4L-ln4sQRT9mVhVlaXXeltJb90sVHSZVeqjAUoYkjNgn0hFoVIPEfDePLb8njZcVn6pRVtEBgsAk9CqWpgJFUoxlnuvZt5ZsjR1HzoimVo8JW_CrjtxjHRci7wlcdR0ZLoy4CGQ4Og8BfcE9t4bcc7DJcZz6HZAs0EGaQKXsu5LaMANIjYfYmYt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24124" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBr2UKhzu2_bwRAne38KOj4Q6qfz1z0U56taC_v5Dm_eQGfux5bBk-xY0G-nlPOxE3p5n2m-4ZssZf3MXKUZbfeE9T4DdHjRohHxEcrft6aFQNiF8209QqhAHiJ6kw-bRcg3bNoyL5gPS5XMoK3MobZEAahpQHfkPrebKzRSiWoIzM5Z6MdhSd2EvT-9YzObXMuCgelxNzGqa2-ZVEJkCQR8VGexmMWYQUL0LGpRY1SOrnv92im88hWTUwLyvoNhmYYGbUVWCHT2Y9ycbbBWGzh8x7DduFYpNvC4WiPlevSudkX12ftQGOaaIU2WXmFngz_IThFlvRnOblXHMrmNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24123" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv24FG3ax6JKkTE-Hi9W-HnlHuPY1qtL82Vrs6pKX5B_pB2jOdryaFd3HxmyJkWahdDxOv8jfUbWzZZb-hyztHngaE7WSoO12xLGRGRSHmzeOFr82oct7lc1Dt3U5tAdmxcPL8IOdLFc3iBqgwOWhMljCnfg0jH2AK6nxq_ZN96qDg5ikiLHxICHl9WLe2DIoMfD0i5HGY1V7PxmrEQIiL9G9i2T1-UTVeV0pKG9ELKFZDqAtgPSmSutJR7gvo8YNj8TzxUnviHGeDtDpikxiFEZkK_pooACLau7FtJM6REdqjGslDKdHj0366Kci2YK-jVxVY870S7kuYKxDv20qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سه گلزن برتر رقابت‌های جام جهانی 2026؛ ارلینگ‌هالند هم بانروژی‌ها داره غوغا میکنه. دو بازی چهار گل‌زده. اگه هالند درتیم بهتری حضور داشت که اسکوادش بهترمیبود و هردوره درجام‌جهانی حضور میداشت قطعا الان هالند رکورد کلوزه رو زده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24122" target="_blank">📅 11:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp-VGKfUSQvT8g5AW0A78vrPidR4t5YNj4XJ7WmXIhZ21Hu0IZn2UF6c2rCgzcCEZnjhqXF4sepJ7RQvbRo2noXThFo0yRaJmqP1QVRZgPSkNhFPL85-g6nn0bsR6CkL4zFrQNx95knZ207K_I0nm2J68Yd5dZ15xmDXrt-FUyrrND1iqOAytIwXKwvJz4Re_lM_bK5sIL0SweboqIw4JyNs83hmWOYfxQwm-C4J3JptJifSxx2gM81EETL0sS6Dqms4AiBpE308_KtvcRk12498YzHo0BB3rQopoA7eJ5W8mU4TC1yx-I3kqIh5SCk0DwNi14EWJWM0F90Pr9wMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24121" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=jLPfdgQ0qwKShaAPK_fXRGVsbj1EiDfNfzfbC_amT_j0LKPrHeyAhg2R3snFYv5R8fhNsmh-15-14UpXcBhWYkytBr5fXhr90deTnGk0G9XuL4UVqTyryXWydT9SRmyB8xl_d6ESYhPtCr82I5_OVOpvHpQKRwW-3kQHg5uQQUgMF9swHW1BITKKGl0nqBXBU5UKiADp4EYIk2naQbYvpvkxAoPLktI3oQo-6dOB-OE5IOxnblAXgbe6eVRXCtio6Gh-J42_w6fK7oZNBk6mVFvCi62wjZdj1LFhh3m56Uz32LXqEoECGm4FL2P4tuRXFnVrLTnpx952I98wmLZlZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=jLPfdgQ0qwKShaAPK_fXRGVsbj1EiDfNfzfbC_amT_j0LKPrHeyAhg2R3snFYv5R8fhNsmh-15-14UpXcBhWYkytBr5fXhr90deTnGk0G9XuL4UVqTyryXWydT9SRmyB8xl_d6ESYhPtCr82I5_OVOpvHpQKRwW-3kQHg5uQQUgMF9swHW1BITKKGl0nqBXBU5UKiADp4EYIk2naQbYvpvkxAoPLktI3oQo-6dOB-OE5IOxnblAXgbe6eVRXCtio6Gh-J42_w6fK7oZNBk6mVFvCi62wjZdj1LFhh3m56Uz32LXqEoECGm4FL2P4tuRXFnVrLTnpx952I98wmLZlZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌اونور آب واقعا عجیبن، از دخترای کشور خودمون بدترن؛بدجور روبازیکنای ایران کراش زدند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24120" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKjJM2zhb6xzIrMM0pNBM298qvVyfWDko_vupf2Y012BkeSf_yPzxRPz4K5luH2DEhjHLIVoNWrcWjV4p8aoCKIKGZhEJuUlIm9L0N7O1kG6EXVhS5DtfnRAYWGiSwp714zhwFkR89fI8KQJyQwM_ZGTHUQ5_AIPWv5Ad_U1bXdhQTnnkSybuBu13Y6YI4m5xqRQxg85_oS1lkFeF5U3gQw-ysVNn-U7wGgnTkhBsn57NTpiNSKp88IFi1CNFbC9aK61Yzw-rp0TQA9TI2zN3MrJCVV-wRlSAi3QVRRkeSmh6n8v_ZAQbU3DEBHmr03d2NfPTWUBYiaImY4dqXH70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛پرسپولیس 5 تیر بمصاف چادرملو میره و برنده اون بازی روز 9 تیر با گل‌گهر مسابقه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24118" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24117">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C29KF6CnqRh5A_yr-3xaULTj9zEh_pEzYhSWJ3Q5-hasgp6k-JM_2VIXnr8kmqYK_UkGpit9chue9exGaqR_3salka_-CkfyUT1GJDD2u-cdnzZBFRwygwy_oatH3AgdJwh4SabB1xi13wA7tFzdDyC8GOx2i8AfTVAUfybp856SWu7eWjpLfUEcustkMqbzHEK1x4dW3RZA4wOO-cs7ljoR39ZRsDLlIp0joLoGec3Vdc1EItaCuuPIbsbxpG04ZjX8V3CimXGe_D_KrXORQYk2fnm7jfOdkEQ5GaiLF0rbNI6jJjvC2whPRPFuxRaSxGFOu_Si6ILvVmcneQ4_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24117" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24116">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdhdhITzNB-YaaYKNW-qC8s6GlEW9DZ0s7UiJLBCV69Ke3xBzhIdUAgVdpUopOnzSSsrkRt12xFgOvwepW41oCP3CSXq87MuYHC92xHBy57HcxdiVkUgH8EzgqnlYE0DoVPWA27SDbjbIJ_Y-zOub2JXJ8oz-FuUJ97wLWr_mNGPtcfQKDCMvCSAtSv3DjQVRhFpZgL4qaoTB3Bq0BgLsgoru47zDrL6qcMyoWuH29zD7bbRrIdbSPYpSpjA23g7QXN1TlOZVMWkeJTmRCh_oIPUYoB53NtCqA4ga62TeOYXTkHlRTNADvgiZHIZgUPR-ldF8HOqJ6E87UzreHQMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24116" target="_blank">📅 10:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24115">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=G5P4bywyvk7aL8pNitZHFhd17Y8i0FMoKvsaU4Z7y4DnESrWCFIHchCR9h073WssiHEewX0aD2P0S1VpJkU6iMLPT_U9PnOY9Zu2IpnTA1HgTO9JHu7vMomKYUuuzGhh3Z2EkQ2YIpO4NvrwHNSXzAuttjCWMO-Jq4-ZTYdQLmWsHeecVQUrzT0knTZN8xNCDvWy08-xo_PYm9S-3eXcYsTYpG8ZtC1P5PO3daBxL89Gx-1S9LnBmQdvkVyV7q3Use5nW4Xjhtymxdx33-n5HpMWBJa7G4ZwQTz9N-3LGt_qBPu8MnErlm-2EIM6lc0ZCYnBOWOh-oNRwiMXvN_G0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=G5P4bywyvk7aL8pNitZHFhd17Y8i0FMoKvsaU4Z7y4DnESrWCFIHchCR9h073WssiHEewX0aD2P0S1VpJkU6iMLPT_U9PnOY9Zu2IpnTA1HgTO9JHu7vMomKYUuuzGhh3Z2EkQ2YIpO4NvrwHNSXzAuttjCWMO-Jq4-ZTYdQLmWsHeecVQUrzT0knTZN8xNCDvWy08-xo_PYm9S-3eXcYsTYpG8ZtC1P5PO3daBxL89Gx-1S9LnBmQdvkVyV7q3Use5nW4Xjhtymxdx33-n5HpMWBJa7G4ZwQTz9N-3LGt_qBPu8MnErlm-2EIM6lc0ZCYnBOWOh-oNRwiMXvN_G0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24115" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24113">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=KYAOQtUOtHnMUxSr-yp08AJIjZ6sdiDws8hwR3qemjsc8H9KjbLSDO-omFttWPiG9mUxMVRz878DzknG9k-ALTdN6W2QgZfpirJpIALZhvknIBgyabVnTKBhLjEK0rxUGVUT1rdcqKbEseJao5IvbGrUhaccP04NKAMU5koreit1iScve3tYKgl3JNLlWamc35NiLxJQ6GHsTr9ceq2IB7WqnwPG7SzXDlcFZF7pv3pxQ4N0lXXcXKizNnPEajebUvrtE05qLqTk1vfU6TTcEM_KckyaWyT7Qpj6eS7gN8wDsnuPCABvmzjd1t4X6Fb2JeV475-Jy5lXo10lGNvwnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=KYAOQtUOtHnMUxSr-yp08AJIjZ6sdiDws8hwR3qemjsc8H9KjbLSDO-omFttWPiG9mUxMVRz878DzknG9k-ALTdN6W2QgZfpirJpIALZhvknIBgyabVnTKBhLjEK0rxUGVUT1rdcqKbEseJao5IvbGrUhaccP04NKAMU5koreit1iScve3tYKgl3JNLlWamc35NiLxJQ6GHsTr9ceq2IB7WqnwPG7SzXDlcFZF7pv3pxQ4N0lXXcXKizNnPEajebUvrtE05qLqTk1vfU6TTcEM_KckyaWyT7Qpj6eS7gN8wDsnuPCABvmzjd1t4X6Fb2JeV475-Jy5lXo10lGNvwnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
عادل دیشب باز هم اللهیار صیادمنش مهاجم ایرانی لخ پوزنان لهستان رو به ویژه برنامه اش برای جام جهانی دعودت باز کرد هم به لهجه‌ای گیر داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24113" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24112">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjAXrGZ5ZPxiQAcwFFTobQaOwlNK5K_mXfHTMW_5kEkPZ2tBZPmi7-6tlAo5o84d_NJ3eswCqOCXDJfcZb5u3x9dgVEPDQDuuMeVFGb61NheAcZw02vsuStEywZE302uEVX8mihqdWDBxlUDYlsUCWPMP6usvcBeUvLWzrrGCxbV2IO8Oq8lOLUk0hQ6yJ9l9MfajlMMTzRi_XZXApX-mAig8K-evbynWvWEnKqdlFz9h1C9Jq9YR631OjVHoCyytT3ZUImCjj98VGNXwzovN2-aFeo4T4pohWnQQg8fiy6u6lD7zvFv6hpLJMzYzjYSqq5obSOrMaPzxhPL926b2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24112" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24111">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjsHwYMn4MSEMplaFJenoVVAq-u-Fec6KkYR8D-W_fIwpfxPF6Xx0tH3ylIXLbaWDXwBCurvi179Q6fdZRCY-mxJEzWI-5GunyAvplhyZOQOYkj6ZZxbvUlDsDHTTf8gQcglE4VwY518yf9s3luOt8J-Yyf02av1xR6B_5cBg6Flx9-8Fws13I5bwF8ZGftOFOhAvZ6zzbbFOfOwq_uW3bGsVI94cW0IFwPNrILqqMWb9-eFJqF3GbEQViLngKbys9ejC9TrNBDOM-zmVAfW_79oicf_ItdXQdIbn-Hc49VaFAhdeyMP4vxZsXZ541smt_TZr6y6c0awHxkDHfmHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24111" target="_blank">📅 09:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKi7TERYi_0CImkVJ-iYSc_fmPAF8RwRIRffB1m1OYd8k5bzNs2k8_HyLDt5b6A_0m_WOLCYO_bao1j3UKYupOij8rufH7eduo-pwrh7LTmtjnkc9VFN-QvyLRD-zaaLFh1fqMksO18MRDST42XdFGxX5HQcFb8z9sBynqcXceYD4IXc-AAIb8Y7fGmFTJFFbipLZOjnD1VUvvadIWCqIZqpzRruZRmCV98e_DPS2SM-4CndzKQUftjVyWPMkQmfGXL02WSIn3OkASxD2TcbiCbeQxE1kVdXeKHBhOh6iJnjmUu8SO6Wondr9iD8UeUiPciXPliE4xmt9xI8oWHIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌برترین‌گلزنان‌تاریح‌رقابت‌های جام جهانی بعد از هتریک لیونل مسی و دبل کیلیان امباپه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24110" target="_blank">📅 06:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24109" target="_blank">📅 06:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkJgFe9BfOusoSj7GrkHTN54pmrb_O2IWFkg2h3JRQyM9_57UMslGUjkKoKIK7Bt2rdUYi08mJpsCl_nJDcCgLR60JFxNp72kkG3aLpxZL1SjFwLdula26SBOfmecKmO6TTcL_YpK04eFXeYl7Nehpr7amZB6eX8XVPMzSuyb8zIx7AGzAYm_ugO5IuxsbuM-sK8xnfzQKssKC13DApgO1YCTxsstohAux_0vVn3rOMICl9Fi9mZOC_9TsIAhVgGpbdxJb9Trb6LWX8Q6XJgOyDl50wyoEd5LrVFjeKYMLIo-vuP1_O7GxibZ4tmEWDjqs8sg4Ezdo2O3M2HPKAPzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24108" target="_blank">📅 04:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دو تیم عراق
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24107" target="_blank">📅 04:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24105">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y80DELZ9KAqRqa0wQ8PXpywxUj_ZEPFcllUcrvgK2-jVtG2-IiuIgARJ6uc24R7HKUyc4ykT3kJocjvC8VfhQ7RLmYadLN_VP5bZfobi-7FaO4LbhggEB5Con1t0-RNoL426lDMoIIqpKlrm4PK4mw5XwujUyEdN6LJj81pE3xAvDA06eN0YfUBD6CdS5gUVfOXF9pGPEd19oCxW8ocq0HRkun6WZDxfjeq77oAqaYIkU20va2s-Jre9CGRgx7xIZPNEyB4hErSXZhHtTPnova4-GEDLRVwlEMpXnbKiyPAudQkmQV3Q0VsbdorfmKAR9ghO-2C8sRu1rM7EevvjUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رومانو: شماره 9 فصل آینده تیم بارسا به احتمال99درصد خولیان آلوارز خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24105" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24104">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuQxV3NhUZmZytVzoDG2UmmM-pveYT2DuQgnfkw1BTcEMjoVFWQNXvHgCnkRQz8i0yOlWJdeQc3d6iOctl13LRUTKucRhkBbZ0yWTkCKoIDoRUI9wPKAkiUY8BjliDIP0JGG86cgUsb23rXY1dTap09uILMr5syttWSGfX2exGY9Vu3Xg0WaOhIue8Epabhc7GshBP6ZScUXN3uI2-MR-NrFcQYGnvMwQ3s9-CW7oCPFKNgMHfSjzEVwjMmAOaosfWkQWsaRfDk1MZZWXrVfO0p07mM39K9LB9TKSXDvIGkrLUNDX3222uaNhqs6gJalkQzHUISZpsbMNn0Us4dT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیشنهاد تراکتور به مهدی هاشم‌نژاد: 3 فصل 250
🔴
پیشنهاد پرسپولیس به هاشم‌نژاد: 3 فصل 180
‼️
ستاره ملی پوش فصل گذشته تیم تراکتور بزودی تصمیم نهایی خود را برای فصل آینده خواهد گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24104" target="_blank">📅 02:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24103">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9c8uOUmHl-oN0-BQthZnN4zFJ1Kd8pf_HKzO4E8FKeXxoPm6GTge6HosluEfG0hOeNjoKE_UdkiUyl-HsxZ8mv86cUCStxQ-nejB3uLbUEfRQr_q93Ks7YwH0PqsrVsut4JdquanXW6JA4n08gGRNGJogNEK-e8dNHHfxabtY80-gMkEhnV9Gs1b1Ko6wJ9Jcen910DFi68tOkOKFJ6T-Ianv4D7yl19s8xEj7H5F7wtpqmZF73inSsbjG7LL9Wrcat9JJXAx7IVf88VQR6H37zGcZmo_5iF3dkTm9Ja0TkdY-gpdZ4Q3cexpOAdxyAWcJSvJfPVXrqMsGg7uY1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی
؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24103" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24102">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=ZkICUFzOnheAPWZxFKrweQJ8yjAFcCAoE9moyhENRNya0YQPDGTy0MlMvafrh8ty5xdgwehlOyzWGjp3qzhFKaCBgwNZwiXF9AdMTDZUkLjkAATjLKP9SW9hm2hscVbeLB0DoSb8gg2E-9Z031qKoGv64CyaMi4Qms_jty6WIw0LKmj4wV3GlwerY4bGv7TJG8EEJMFk-0tHki3VZmdce9K1AsVSf1my26oSVsy-10olxicG313IvLMNzVQuzhsKXEN18ZktURQs38QAKGxjr4Eo2rw-WoR_KoV5h0ySKnpl6pCAdCBQoVvtyjSVV05l2C7VGDgrQbSWP0I_62qnkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=ZkICUFzOnheAPWZxFKrweQJ8yjAFcCAoE9moyhENRNya0YQPDGTy0MlMvafrh8ty5xdgwehlOyzWGjp3qzhFKaCBgwNZwiXF9AdMTDZUkLjkAATjLKP9SW9hm2hscVbeLB0DoSb8gg2E-9Z031qKoGv64CyaMi4Qms_jty6WIw0LKmj4wV3GlwerY4bGv7TJG8EEJMFk-0tHki3VZmdce9K1AsVSf1my26oSVsy-10olxicG313IvLMNzVQuzhsKXEN18ZktURQs38QAKGxjr4Eo2rw-WoR_KoV5h0ySKnpl6pCAdCBQoVvtyjSVV05l2C7VGDgrQbSWP0I_62qnkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمله سنگین زلاتان ایبراهیموویچ در ویژه برنامه جام‌جهانی: من فالوور ندارم، اونا پیروان من هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24102" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24099">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKU1ZeZS2fS--Kk3msEZiHaHLGhR2QcT5fbvwVcz28upULqmZShOqAQSwR21GMfslx6eIzkIDbZAO4vHI-tStHyBMEHlsuNCoTCAxH5WTu2JZsklA9QDPiEWy9Ue4GX-K28IBTFv8Q0Li_ztWEg534t4txcw-xfmaEq3Al_IdHQMKKBfNe16upRjwuAC5_7jBhx_W-cv0MAwFGVbF91JmCr4jCFUhowi4_9WRR134jx79M95RIWg7w2cC6aqt1rKFwegEKVrRtkztOOoP_1XWVjXfJH6TkJGNQpgXKIeYztZhTD97OXm_ZSTwwKeMTuHP_Cug574g0f4FQWvvu0Cbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد: میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24099" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24097">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBS9IJqFl2U9YOSEZvHkup516xnM-Ux-x6spADzvys5XsFYecGKAex5fHIeRuP2vJo159NyJjsYT1gEeNWo0qclpmN7AyT3QtZ3nO447H0ET7irmEUKkOJcHskr41Tom3oZzu2bokXF6Ek7A0OnNgWEXYKY7vyfIc7_ZX5IEMT8Ols3w4_jvpIp9Nfu6_cLd5HdQoQqzCPeUi4dHqy3qIWRNrKruJMWJJLe_nV5p7F6Eka5XGUc4ipRo8Z6nqKsTMkQUGmGmW-tqVXpgnSNAJqbtWo3o_Jc0WycjlqjTz4mcgtdkNvBx_ElQeQoOecpQ7i_N-ilMKr6pGy1KDh2RRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اگه فردا دراگان اسکوچیچ قرارداد خود را با باشگاه پرسپولیس امضا کند بلافاصله یکی ازستاره‌های خط‌حمله تراکتور رو جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24097" target="_blank">📅 01:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=u0gl-bWuKlRMPlM2UMvrLlcFrI4zm0MZngeABjABfW9f6hu2tmxtsbOxK6FoXXcf1CTYBomdexLFehZwauGQU0p_pcNzv2P_ZJXa2VSNCavIrducmL2h20UmLjMQnJy5kRZJY_bplmfEHX-QZ-dC89RJy3-fF_buujzH6Ts65oh3OH8xxUQTc8IA2ZxOVuDN7TXBKLbrTQpygb2oEkeGsb5254VgzdJb-Po8NqeQCIOl4beYY8R9vjPRHEBekXOTqu0fYe0LNsIQF-dupVXJRMyprMRx6InuRwz8rUXfoIe0njxh3_bPxdiesPKakZr-4-yZK6m1urnFRnwvZiJ1Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=u0gl-bWuKlRMPlM2UMvrLlcFrI4zm0MZngeABjABfW9f6hu2tmxtsbOxK6FoXXcf1CTYBomdexLFehZwauGQU0p_pcNzv2P_ZJXa2VSNCavIrducmL2h20UmLjMQnJy5kRZJY_bplmfEHX-QZ-dC89RJy3-fF_buujzH6Ts65oh3OH8xxUQTc8IA2ZxOVuDN7TXBKLbrTQpygb2oEkeGsb5254VgzdJb-Po8NqeQCIOl4beYY8R9vjPRHEBekXOTqu0fYe0LNsIQF-dupVXJRMyprMRx6InuRwz8rUXfoIe0njxh3_bPxdiesPKakZr-4-yZK6m1urnFRnwvZiJ1Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#فوری
؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد:
میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه و آلوارزبسیار سرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24095" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24094">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=txEFc9RZnQxBDWxvd_svltjW1Z4OMVIC8nTwU6BIbmBtKFXwYNqXA5ijRZCGRaBKR3DMMhfzdkl1_MlIZtT5PTGiK6ek0jhMmrMnOxmdFpX22cnlcOb3boRj_K4KqOE_kYx-1P-kfTdJKErdQj8KvOeKrJFWGJy4QnqYiU7d2vbD-xo6Y7a2zJdLqDxE9Uelh5LfA5w48mDiguvkChw023E6o-9O-rUaTL1d_rY3WomD5YhM-VuHv31q0Omm-ExbqDumELpxpfkdL-_6gNlIRDjSVFJcguqS8FxBRue_r51FwLuOzlG9IcMCnovFX5qmkkshiKpeOsDSWpTUk8J2cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=txEFc9RZnQxBDWxvd_svltjW1Z4OMVIC8nTwU6BIbmBtKFXwYNqXA5ijRZCGRaBKR3DMMhfzdkl1_MlIZtT5PTGiK6ek0jhMmrMnOxmdFpX22cnlcOb3boRj_K4KqOE_kYx-1P-kfTdJKErdQj8KvOeKrJFWGJy4QnqYiU7d2vbD-xo6Y7a2zJdLqDxE9Uelh5LfA5w48mDiguvkChw023E6o-9O-rUaTL1d_rY3WomD5YhM-VuHv31q0Omm-ExbqDumELpxpfkdL-_6gNlIRDjSVFJcguqS8FxBRue_r51FwLuOzlG9IcMCnovFX5qmkkshiKpeOsDSWpTUk8J2cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
صحبت‌های لیونل‌مسی کاپیتان تیم ملی آرژانتین در پایان مسابقه امشب مقابل اتریش در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24094" target="_blank">📅 01:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24093">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9-IHgD6CPhi8XjgSNgZ6-7RcQx947NIKBo7GsUvmom8okRRBZtgTHuEFDFnAOK_x572Aq5aRLm1TVzzg0QRRc-E7o-LOgN576SQXGT6MFxez2ZMVKd840nLCOfiba3iCF2QS8enZRFoSABWWraWmegnCnV5vdmLINLdovxjf4OTSV7k1ky1Nv20fOBe_CLDf24bTLaYisrQ8ZSg8KMc0I2WlE7j-4xPtK819nqjolWH3UbjH0jEVRDVM2W4gy8IgOn-THS4QPy_QZ2fWVfZhHYqF2G_AB9Ac9wpvpg_nOHb1iQ-jhC00xNRJxvpfyvZOtsRxdbNXNTM6gbIu_JoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف یاران رونالدو مقابل ازبک‌ها تا جدال مجدد کی‌روش و انگلیس در مسابقات پایانی هفته دوم جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24093" target="_blank">📅 00:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24092">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKOwPhK300Woq3Ag2b6B4RPre-ELXeHAySPV08IILzrcplBEIVcnhsAwlPV6gS5GZS2pUAHw9LDad0CJTNpULkHwGnHhryumo3x8nwMEW95ikxk09lkVA829aG8eNhtBStGiZvp8zBLH9oTH9Q9uZT-K--B3ZvxpkY_CEkYRaFKiZBKYU6wjuWUoXrAqzYhb13Tue_HOOHkQnxFQ9mG1erLJ1uyn4pvTSR9aJHA0KeZOfYlo5WL72Rg9O_HWii-uMQcbfvL4O3yekVwhm0OVPY_5omKMU771gHyzL0EZqTZ9bgj02K2hQG3zRVG77GbpSl5kmDzUTl6iFYM82_ipoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از درخشش ادامه‌دار مسی این‌بار برابر اتریش تابرتری‌مصری‌ها با اثرگذاری صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24092" target="_blank">📅 00:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24090">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZjznWcVpuvq5s4YJDkWPEwTXyKrrQ16wdawJxxlA9w5ks8Yfu94hNwyjhQHEaiar5n1YYdaP__inSFIzNSajk4PJ899eT_DLzVajRjCry8h5UuNClY_iVd6MfykCHdNKcqJa63s7ws799GAuu_eRjGAYVRzfpUDvMDqQOhXnPz2lPpH-JMc7U4TXP2pPBFlFWDfnm-JC6WOWXQ8v1NimZNmOlbdzReSJoGQAHEb39INu9_sKVFOi8AIM9FazduD-c3DJhsfNflo_Mh-2HpDbBshcbK505sSdf6jiHx3L9UT6ZjBu37SSt0QbRrGl6q6Q18fk0K7b1Vxdv9H7-IS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بادرخواست بختیاری‌زاده سرمربی استقلال؛
عارف آقاسی مدافع28 ساله‌آبی‌ها در تیم موندنی شد و حتی به‌مدیریت باشگاه اعلام کرده در پایان پنجره قرارداد او رو به مدت سه فصل دیگر تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24090" target="_blank">📅 00:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24089">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz1jPgkV43D1oqht9NtWJJ0VWFu5z8Ayby7Ls6196-WtQdiCDLnY6fuqei5en4GtSE90_Q36QdNSUutTwsGOomTPvyEbH7DcCXHKwqi777c1yERNnI1kb4ZWQ5cvQOGW4twrj8GLunb8xeCTk1ZI2QiLWem5-anUwpYA1qrk7yr-m87vGAwSURiFj-cWLnUlhWi_HheV0VbbtyettSTs5nH9rUJ3FAqxNjWDLEgTndx1iU6JHeFz0JRrqFovZg7x2upU8jMBRosnM5WV1htxMItZ57JSnQgrZYd_dA6IXuV-j7O5ahqayYP891tswQ0TshMpdh1qagEw6wUkzQYR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تافرداشب مدیریت باشگاه پرسپولیس تکلیف سرمربی‌ فصل‌پیش‌رو خود رامشخص میکنه یا با اون دوشروط دراگان اسکوچیچ سرمربی‌سابق‌تیم تراکتور کنار میاد و او رو میاره یا با اوسمار ویرا ادامه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24089" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24087">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGkdcHN_YriDf3vNmNGBQ7kdz6n02Ef2LEY0DtAPF3Ovd1v7CwsSuQX_iHQvrBzKsO9rUf0SpwwzbBV79KF8ECp66mM6paLvo-96cDMsrVb-VEVpcaeySeKLMy6O0aNI-vCFisFTNmJmfvQk0U2HLKt3ZkZzq_KeOrwT6ehbf6eMH8HJ2JVIFI5ePUqV3ebGtLMzrMZkND2Wqfheq6endW17Gj34JJ2pLSq_gFiWf2BQv1vJbVHEfjHVXsD_9lbKanvLQ-Tf8KIFsgQUqP70T1L-AmJL63pz42kDr6Qa0I8fy732Aw3AS-_dz9OEjsBnjhu8aVMpxjl-7-nEHFjoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6on2SOWy7FQVjfi_URO36Z6b7gozVY2IYTM56icVTkCQhHbS1DZEZRCLJTThSOdnCVfLPHvQJfdMHShvQQjNcDETQ1UiSt52TDDFw_SSOEyCEyC8fji6FeMDa2FYusOkNcKRuQ7FuFzy0zJ6gCXo0RN4vuhk4Lm3XvnRvRxqrM57DHHT5tl7P6PsvvzjVfrrf6fJI8M6yt9-KvYaJumJYc3Mn5ifqi7KbK-raYkogAmV4oz3wKHRGQd54E7WYyTf0hJYaPVwy-gsJT27lYjaZaWUf0FV6hI5l2EHw8uYLHL5Vh_S8aLn7tps57Q3T9FIZwgZOuTUALTww4t779aZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
چهار تیم ملی که تا به امشب به مرحله بعد جام جهانی 2026 صعود‌کرده‌اند؛ آرژانتین امشب به لطف لئو مسی دومین پیروزی اش رو بدست اورد با شش امتیاز مقتدرانه به مرحله بعدی‌رقابتها صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24087" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24085">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7535185668.mp4?token=UORBtYiB91nRM7aJ4ZQgyw9cw2d5GUBj-B7zZGj0SlJ9n5tCzAt_MWqdlAXG0Eg7ho1gjraOIbL6KqoXFI_wMKS7FK5_UA_H9R8kVG1N_P78Mwhm7JQjGgp2raHrfg6Kicrz3U3wyt8jKvi3m7HqcbnyjozvFoQXiGBgaooiFKb72Cn2KzT6aZwWyZXG0NgizmmBW1KrtRU2N1XK3hd30fIPyKKtCYTsPC5ofHgGofacz5XBxm-bQWS05ae1dsXgv5kwoB2J5_ZVvxAhXpzWlgyO8ynFA9eFQVeFMhxy57RjmV75qKEG52eGFqZFc-4UDobP8FKZ9sJjG4T8ZViZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7535185668.mp4?token=UORBtYiB91nRM7aJ4ZQgyw9cw2d5GUBj-B7zZGj0SlJ9n5tCzAt_MWqdlAXG0Eg7ho1gjraOIbL6KqoXFI_wMKS7FK5_UA_H9R8kVG1N_P78Mwhm7JQjGgp2raHrfg6Kicrz3U3wyt8jKvi3m7HqcbnyjozvFoQXiGBgaooiFKb72Cn2KzT6aZwWyZXG0NgizmmBW1KrtRU2N1XK3hd30fIPyKKtCYTsPC5ofHgGofacz5XBxm-bQWS05ae1dsXgv5kwoB2J5_ZVvxAhXpzWlgyO8ynFA9eFQVeFMhxy57RjmV75qKEG52eGFqZFc-4UDobP8FKZ9sJjG4T8ZViZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24085" target="_blank">📅 23:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24084">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo6rT6GHVUuLsANzXKNXRx2puT_-JWg8ygGwFhV5_LSkqE5wSTwwN8kPDj23OPlh3IFlrImQDBMD4cglZimCbPbJfrMoniK0Y8mBK-oUB41KAuj59ktOwuruY1x-OovFZ9Akn_Ocx8UaLGKklYbvQn1BZeMSRL4C6nVKNkTWXvavNI8WKRCZIFDHHIybXhzB5-30mfia1LgkrwIvon7oZJzeGcFMeGHYQICkMJmNHbQ0QjPU_4PmTBf5F9kt0Xcn6XET7s3DBswhvUvr8zFcfyVkZu24fVV4OeonttHnjgT17HeDYc-n3IwmyDib4fJkdu71a-VDmo-S0QfW03-ocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24084" target="_blank">📅 23:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24083">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4YvxmA-3QDx1KQfWlIlCz-EZvcEJxD2BZYqPogvA6DFzrWg4Qa8gbJ4LY0vfQaRnlZLGfL_YVaN7w_jAx0he4SzQ2lsvV2A65e-BIvRnJG4DZqn1aIFBsZrefD0f4PxKK0mQQEzcauiLNMDMf9u-hf_vvJnZJ-RuqcwTyZOqkVh2tVdEFvy5ZeRfhMmjvpMW-hghVA_qrehKHGCbDYDcbuCgU8T5k6QOdmaRtPtxwq0EK2w4mA4sL_IPzDj53ixL9aRCoRyH33q8nUoPOHauiL-dz5j8ZlCbxZUpDPn_jcB4oWsVyxl_tjqFPzsq2GrgzmF6yLRzeKZyPxvDLFeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24083" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24082">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs3RK0cTwZHO9LBKT_9jCmJ9GkJ7xlAJgtp2S4amuEPak6r3UgVlIhVMDeSkVwdCE6noM0e-bZ14m2knVarhwkbsu8I0Z5LH1AL6auXEr9a0fbt2ewD1c9MBXVLUYVAXLnsopFeM1zp3K-_xXg-OKr9FZW4hkxN2439eFoYDFR_UOlZr6IEW2tcPfccdJk6GSEllgSwzbZmXOQz2O2ZDZA0bKSqqdfAE0x5CaWjvw9ZchOIJwNWsgxjUnMnGYaFdK8y408iZWUyvq9uIZ7Qb6GkxaEuv9lJXjsR5P0lH9mXYExPbOU7IQBlYYqGiNUuCGgcfXf0EPo8XOS9SdhISdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24082" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24080">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwLpIPXi5guH3HONx8eR-0STueXIuBKsdmCXfpFuZe7Kl0fUaTZh1MRmiL90P7YgVsDkRFoUgfrnT6RyW5gjq_3QsGSQqOgpHF6UzswwuOgBe7vTv6YDaQigvatSx3wlBDInmu-Tf7Nw4nm3gOQ3kSGy5CRtWoU6KBnterWk1Bouf5_FfizP-Fz5Y1-6zYv7x4j_R0q7A3mcHXukuRhuOYHG-Y3TDdTNAbhT8IlfZwOUs2RmDdTuroDh0R95xxzO7HxlHGBbPBfOgJlYHUh66Ep0EzwglStgR5GOAlLY3Mc5W9FVGSjwbRhC0yCOP2c7465AdRQNsU9PE-INArIx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
شروع طوفانی لئو مسی در جام جهانی 2026؛ دو بازی، پنج گل در سن 38 سالگی؛ این 18 امین گل لیونل مسی در تاریخ جام جهانی بود. آرژانتین تو این دوره جام جهانی 5 گل زده که زننده هر پنج گل این تیم توسط لیونل مسی اسطوره‌ای بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24080" target="_blank">📅 22:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24079">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a48741736.mp4?token=BDIAAxuyFTcLF1ggcNF9kHdUD5MYipPZOq3e1zD-yaLx8Xn5OhMoUq6az_lljJkowDKVD52xXRoexlkMKLws5SZky0OCsVYw-zwMJ6xyOeGSLQ7CBeRDKTPP8eObyylZZRgEh9YZp5-Rth8QlICypv7-KIKnY6P92m6I7_eynf1mSir_xcFz4svKjwQkhTe0UfJQlq8Q_m0WkjjjAx8uV4R55lTflacViDa7dCjTgNA6T8R38TzBIMCLA1QJ8s8bRJ7ysAOKIe1m6t3Qk9itVAqOi3OK-79Re9orQUUhQDbAMR_zs3Lf3dSi-GOfXKeA6JdZg28C6-dgkZNav28w0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a48741736.mp4?token=BDIAAxuyFTcLF1ggcNF9kHdUD5MYipPZOq3e1zD-yaLx8Xn5OhMoUq6az_lljJkowDKVD52xXRoexlkMKLws5SZky0OCsVYw-zwMJ6xyOeGSLQ7CBeRDKTPP8eObyylZZRgEh9YZp5-Rth8QlICypv7-KIKnY6P92m6I7_eynf1mSir_xcFz4svKjwQkhTe0UfJQlq8Q_m0WkjjjAx8uV4R55lTflacViDa7dCjTgNA6T8R38TzBIMCLA1QJ8s8bRJ7ysAOKIe1m6t3Qk9itVAqOi3OK-79Re9orQUUhQDbAMR_zs3Lf3dSi-GOfXKeA6JdZg28C6-dgkZNav28w0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24079" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24078">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=Qmhi4uhedEcRoNeBfTRdjUl4ToXMPSsidNPcT8mTOIvE0LntXqBQaW6LSZ30upOLYrGDxSWLpBfjxEoU_ZQ9WhcPsVwezchaX93UKNGbcf52WRpPHY7XK3nyednPY67TmXQ-yOz1lo1BFpgPXW8LtIPesOM5vAIhv_YKRxvgc4ctVMe73YCheU2SwP7NZqH4e17YfyGkUnVyHdpI5TCpfW2lJUFtTiH7xNtc03oMiAf1LG_8A_JAY3reeJLnoxLTSGWklUgUn5GWkstQugn1W6SzrRBWT5c3dbleNxBbKYUtkq2_MIqEbiIsnQbSXZKjo5cSHSZPLS6ym1F2h6y0qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb8a2493.mp4?token=Qmhi4uhedEcRoNeBfTRdjUl4ToXMPSsidNPcT8mTOIvE0LntXqBQaW6LSZ30upOLYrGDxSWLpBfjxEoU_ZQ9WhcPsVwezchaX93UKNGbcf52WRpPHY7XK3nyednPY67TmXQ-yOz1lo1BFpgPXW8LtIPesOM5vAIhv_YKRxvgc4ctVMe73YCheU2SwP7NZqH4e17YfyGkUnVyHdpI5TCpfW2lJUFtTiH7xNtc03oMiAf1LG_8A_JAY3reeJLnoxLTSGWklUgUn5GWkstQugn1W6SzrRBWT5c3dbleNxBbKYUtkq2_MIqEbiIsnQbSXZKjo5cSHSZPLS6ym1F2h6y0qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24078" target="_blank">📅 22:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24077">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ay-HEOt5mXPle4MGrgHGXhxQmQNS_CybuzNqPB8vvJ5mDGHXb94ZANFVOtbb-Yeh8oIqx9r1zv33MgzuNBS36Pv6XDTDDRUpDybAm_5uiiAHh_-BC00k9Fk9f_xJWEPclTqfQLlYN7cvscSZ8hmKnbHFOcAwR5z1B37zMyvR8Qy_Qh5s13wACYnzi4dM4b0d9kuYLepI-F6pcJhvRRwlEdz94oh1PxmVYJuBBTjOYNRr2d1tv8-GF9_BzNoswmK_UI6DCciC_4shbUQ88ewVqE-glaiGbNq8rICmGIQY1Uf9XhD20mV-m-Q50-JgLaGArcIoqvG2p3UovWuk0x-bRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
باشگاه استقلال: سیاست‌ما در نقل‌و‌انتقالات تابستانی جذب‌ بازیکنان جوان است. باشگاه با انتشار این‌ اطلاعیه‌ دست رد به سینه بازیکنان سن بالایی همچون محمد دانشگر و سید حسین حسینی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24077" target="_blank">📅 21:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24076">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfYTI3QKm6a_cqMO-4JcmcZ4hmoyRQ5oIP-ECiqm_MTyjIv4MYk6t36vBnAK6Nc6fAFofe2NCYc8Tzg-2x5rg_H7fXExWv9Tf5rmVo-fMocN8u53USyLDWpFjo5tP2FGxAy-2aP6HmzDtchQfJcH8IyhQjay697R8kbfImWU5wInKj9FlqHX7tUq7EHCIRa6DRONQyQk-ia_TomjN47Rno-hXZ6tzOdF-sNGAuDeOCOfKt9ENqugZ2H4rjpmmHLNXqLrojdEUwMPI8bXDvXES2ncZ4i7cCR6sNRhp0DlxRCNetSDntLEVz7Vd2tDNHlbTlGOICdPUUKozOxMusQlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24076" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=WqqWiFb-mkQLp42Z75rLoNHrkaM2iN1bSMCHu8sBmUS29WFW4NpHzwukp6zXbeZKwsUDVxfNFjHqg8StHsETP-jmktiuPl824kYDahPub2xq2o3-CneJmVx5KMrKWJrLeuEKr41KwKjELJ_h0dy8A1wxHSsE5mgleRqreeYW2YAjdvFVZ1Ltu9OK4FI6M5EiAPYVfiZBVR4CZtNA8XOxPE3gQ0EJ0Tr6IUw2ky4etr8jdYT8p5pZYTHxxQDMZ5QjQRK9iNIW_WROT8gN4XRmfUGOIhIhvDE3vS0GsYr1YGwhNUWo1qRCyRsnbNVWNxKHwzQirRjZIZKV5x21rE62wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=WqqWiFb-mkQLp42Z75rLoNHrkaM2iN1bSMCHu8sBmUS29WFW4NpHzwukp6zXbeZKwsUDVxfNFjHqg8StHsETP-jmktiuPl824kYDahPub2xq2o3-CneJmVx5KMrKWJrLeuEKr41KwKjELJ_h0dy8A1wxHSsE5mgleRqreeYW2YAjdvFVZ1Ltu9OK4FI6M5EiAPYVfiZBVR4CZtNA8XOxPE3gQ0EJ0Tr6IUw2ky4etr8jdYT8p5pZYTHxxQDMZ5QjQRK9iNIW_WROT8gN4XRmfUGOIhIhvDE3vS0GsYr1YGwhNUWo1qRCyRsnbNVWNxKHwzQirRjZIZKV5x21rE62wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24075" target="_blank">📅 21:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b9463294.mp4?token=ixOY8868WO2ByfqUUhlBoVOyRto18QODBMV6Gg6MTQh9cRs6Kts2EZwuKG3z7X8VqpwiPQ3xhzJKsoUfq0COS1biH5Bu9gETTUlAFDsRvn3kdcPrAd9_s3BB2VyyhOns2FN4YSP9Bj89ReYlpcXUYCG-r8p_i7DZbkZvlZQCbU12eu-qnKhoF5upWBTAls7FVJ3nfuighozEOwhRsDWrP8RlaOJ_2HHUAur4hfPw5Z7cEWzN0Gp9Hpv78CtaCCkrh3LwxyBheUux2sNLuKB--38zvgWCXjsZFZC3jReYugnSR22f567Dc3d4b9bJVCB7h50v-uXbREwvdDNUojrasQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b9463294.mp4?token=ixOY8868WO2ByfqUUhlBoVOyRto18QODBMV6Gg6MTQh9cRs6Kts2EZwuKG3z7X8VqpwiPQ3xhzJKsoUfq0COS1biH5Bu9gETTUlAFDsRvn3kdcPrAd9_s3BB2VyyhOns2FN4YSP9Bj89ReYlpcXUYCG-r8p_i7DZbkZvlZQCbU12eu-qnKhoF5upWBTAls7FVJ3nfuighozEOwhRsDWrP8RlaOJ_2HHUAur4hfPw5Z7cEWzN0Gp9Hpv78CtaCCkrh3LwxyBheUux2sNLuKB--38zvgWCXjsZFZC3jReYugnSR22f567Dc3d4b9bJVCB7h50v-uXbREwvdDNUojrasQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تکرارخلق‌این‌صحنه‌تاریخی‌وشاهکار امین حیایی دراخراجی‌ها در بازی شب گذشته ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24074" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP3vqg--IqYRPYDXBm6GbaP_9SuXoFHV-IM8_WsefhDm_ZwgK-EDy_E-ti_hAArjQlSAQjfse9rgLVb9uAII4FN3r5eWk7jJFMOhmlxpw68dlAPn0q9uvK97O0c3LV8dKvJ1piSYiRORfg5TI7dWG1FMcVkHFzf80EYmtotX3gJklTlWAYoZIZMYLCODK8DH_4DiDZYQXOCZusOXJ9r9DPnKZcmTlg5ZdB7AG9rHTKSbeXEiTgbZsExojePWGrPC9NUNvR50wUiVOaMqzo5CL6_oQnsH0-H8aGKuKznyOVdnNDQmPycmqUSZjqXR8UzjmNDQF8uRqlG6s608hbnXXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در دقیقه 9 بازی امشب با اتریش فرصت بثمررساندن هفدهمین گل خود در تاریخ جام جهانی رو از دست داد و پنالتی‌اش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24073" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24072">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دکتر انوشه مهمون برنامه جیمی جام اسم ابوطالب رو از قصد میگفت یونس یا چی؟
پامپ که برنامه جیمی جام رو ساخته، ترمز بریده و داره یک کیلو طلا بین مردم پخش میکنه،
هنوز سهم خودتو نگرفتی؟
این کد سهم: pump
اینم لینک :
👇
👇
👇
ثبت نام و دریافت طلا
دیگه خود دانی...
@pump_vod</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24072" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=chTHpjKdunWgrWCdQouB0-Fp8PKS8P06E0uXKRNg3BQ_7ljDstOOrN109HhaJq-WCASx4GCn6D30hx_F_sdDC7i8K7EzZUiLT0SzSMo-3XvpkE-MA-TZYZXxM9xhX5uSXQEaKlwGJwkoBIN9D6uGb-pHsoXiHP1fcupIe-7xpMXiNvxJSpMsSC7wLiddGTKdujQCZkzFIn88cQ-0wEHKiQ7BSppKaEtABa2piMxfG4w7qGNJ6hMzBugWbRgIgSGH7oJRRip6TYGBQvVAxshlv3lzsprosV8WpMMQ_mQrRAvj4n_9JoQidlBJEqHrECqExd7lp1hUdlpygJOinePswg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=chTHpjKdunWgrWCdQouB0-Fp8PKS8P06E0uXKRNg3BQ_7ljDstOOrN109HhaJq-WCASx4GCn6D30hx_F_sdDC7i8K7EzZUiLT0SzSMo-3XvpkE-MA-TZYZXxM9xhX5uSXQEaKlwGJwkoBIN9D6uGb-pHsoXiHP1fcupIe-7xpMXiNvxJSpMsSC7wLiddGTKdujQCZkzFIn88cQ-0wEHKiQ7BSppKaEtABa2piMxfG4w7qGNJ6hMzBugWbRgIgSGH7oJRRip6TYGBQvVAxshlv3lzsprosV8WpMMQ_mQrRAvj4n_9JoQidlBJEqHrECqExd7lp1hUdlpygJOinePswg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24071" target="_blank">📅 20:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0L7rz4lTUw8PCncy3GeLLkwrqWvAPBFacIQjAN9WX2gz8OzyYjgxB41PKhAB5RHRWNGEttOR3S1NEtTR5k2_uX_zq8Br3SzrVa-4n8ezjB4f4o2gWB1kE5CbdxVnGug7_pquvER5uQg0EsMurVEfX9d6iCrazRdRCOC7QsSIpGxaG68pMrJRejbpxSD0bVkDU7cb0XoGM-Xv4RbyBLUsa130rnBuS53hJelfdYPYL3kU1bKCwbwU0QOL2b9lUDuNocivUtHT5tPF64_cHwMzasZR9WJH-5Xja2ZFjErzxoLM9oEdq4YyOeYFAXkhyDlX7r0OMag35JUqK80qcjipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
اولین گل مسی تو جام جهانی: 18 سال و 11 ماه
🤩
اولین گل یامال تو جام جهانی: 18 سال و 11 ماه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24070" target="_blank">📅 20:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=U-oPqJZUlpIsi5yy1TZhBGHTkqt1lqNdLRHfVMbUrYBIKZXMn1DQ72FeTbTiaBRSmBdWg3KID_N_FB5a5cmxilFwS0iL2oP771jrbHMkICNVtDNQFOZ7_dqLWGJNzZQc1JrvqPh0JaaKLBk5L-TAX47o2bWeQD9cdV1BEwh45V3t1yxQk6YzuXgAT5vPS93O20iiK362KZGC3DsTTcQth2QSKnLxIknYuGgsj_VGAd4USkcmg3-8FoiE_fZnv0RVuPJFdJhZ87T2HGcDgzQh_pxlE2LWqZrubjJBies9Ahp3l6vOVsn8p4MdDMhPkk_Vqvin8E449p8rktgALcZckA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=U-oPqJZUlpIsi5yy1TZhBGHTkqt1lqNdLRHfVMbUrYBIKZXMn1DQ72FeTbTiaBRSmBdWg3KID_N_FB5a5cmxilFwS0iL2oP771jrbHMkICNVtDNQFOZ7_dqLWGJNzZQc1JrvqPh0JaaKLBk5L-TAX47o2bWeQD9cdV1BEwh45V3t1yxQk6YzuXgAT5vPS93O20iiK362KZGC3DsTTcQth2QSKnLxIknYuGgsj_VGAd4USkcmg3-8FoiE_fZnv0RVuPJFdJhZ87T2HGcDgzQh_pxlE2LWqZrubjJBies9Ahp3l6vOVsn8p4MdDMhPkk_Vqvin8E449p8rktgALcZckA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24069" target="_blank">📅 19:45 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
