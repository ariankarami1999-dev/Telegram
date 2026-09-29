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
<img src="https://cdn4.telesco.pe/file/j34SWsMMNKefLB3l5HeGNx17rMvueVLzFfC3CwHbpjYKBRVpMEQZ0SV2iEn923mYO0SI3SHJjTfc61byDDq7FCFOpYKtLvqIXIPWMMnwh22GF9UuRTA7Hg9VpAjrePLkoEI44JY_X5hd9HmhwR1_UuFzF3HSxRu7SPBBlbLhNUR40h2dEKow6BDIb0Ytj00yWyGDkUGsWG0KjiySDoOSzfzTTjwcA8SgLSq-OU-djthPc_28knxUg0vkpRaig8QegXP7CtPm_YEqVL6MqeHzv6Jl381fp6xDT1Sy0exyPMucpSVgG4cmbFo_uPmdgB3lwy879aivTvSubp8ZX86SFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 23:34:57</div>
<hr>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=gn9giy794hQgjaFwsYRNcScBjY_2pP7yek4F37PvFKCO3n316kgtwyeZdpMNfb_m_yjnwqtQ5pnuSlUggR85ygZTXZhosMQUtOr3Qnefk_sHEsYQgF6O0DSIKRf1C7FbWX6FKt_6J2XslrQz5haA4mr6sqhVe-pQLPLtUGsVMo9H6F0MGaX8A_PdUYCM3aLEuBgn4IkTl8JbmQ0-GoarIiRvotBZW4PYi22r6DWuiBOnD_07O9uxgdvOt7EXK73lfN4YPCMQiOTpgOD24GusUr_aWO3jbQvVwz9hOufuTZRnzNM1Hkp--wxLTcVqZDt2vClw1qEYZr4jKp4NePyD2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=gn9giy794hQgjaFwsYRNcScBjY_2pP7yek4F37PvFKCO3n316kgtwyeZdpMNfb_m_yjnwqtQ5pnuSlUggR85ygZTXZhosMQUtOr3Qnefk_sHEsYQgF6O0DSIKRf1C7FbWX6FKt_6J2XslrQz5haA4mr6sqhVe-pQLPLtUGsVMo9H6F0MGaX8A_PdUYCM3aLEuBgn4IkTl8JbmQ0-GoarIiRvotBZW4PYi22r6DWuiBOnD_07O9uxgdvOt7EXK73lfN4YPCMQiOTpgOD24GusUr_aWO3jbQvVwz9hOufuTZRnzNM1Hkp--wxLTcVqZDt2vClw1qEYZr4jKp4NePyD2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=oAMkPH_jW-HyV82SKxPnQROJzac3XSsMp2hk3zxTNimotZTJjJq9LtZbL0JryBl3Jw_mcEtLVwfeXfxMrvWh9Pl3hs7jisjg3XrW9gNIVZ3OqGg5kMKdU0zFVhrSD7c5vipEw1ID1_uzgScP7b8d7xEqOP36L8b6dBhfu4wSOSlHL-7qVTiawK2l5276smkRFRz7jkElNyXPIe_UeGctONIx_BqM0u1_PjYd6_j8fm7oEe1b05n34t0yJ4yogG_5x0yHPzwj8dEnZ3wzqzYLwzcnwsQEMsoOTDRWxmyJHlK2_kT-_oIIIrHIMMsZv8YShzBeaXy4llT7727VY3ObOlXvIxbK3zGO3ybJ9etEm2j33En6n_B-vWQoTHlXhoQNGdOgnfeprVWniPzB9uoIStFJp_mQkGgTkV0K1qZm-lImrWfSM6mfBfQkVRXetXvL7a5BptfQjcpqr9t_iOagdWi3id3Z81y6qZL6euy9Kdd-vfC8xJP4NB5z_mqBoKnswdppZIzTmgSucvRpyuNVmkSrnVe_2ng3J93C-0PBkyLcgvgSj2OWVsUCYQPniT61j2QF5LXOowxY7Ik_rUt20G5f_qZXtX5ZljUfHSU_gnqjnU1xlRutOPz8iu9mzU1apogbZplkiYuXazAtvslA-QZxhtuBHxUpAzwv60zmOGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=oAMkPH_jW-HyV82SKxPnQROJzac3XSsMp2hk3zxTNimotZTJjJq9LtZbL0JryBl3Jw_mcEtLVwfeXfxMrvWh9Pl3hs7jisjg3XrW9gNIVZ3OqGg5kMKdU0zFVhrSD7c5vipEw1ID1_uzgScP7b8d7xEqOP36L8b6dBhfu4wSOSlHL-7qVTiawK2l5276smkRFRz7jkElNyXPIe_UeGctONIx_BqM0u1_PjYd6_j8fm7oEe1b05n34t0yJ4yogG_5x0yHPzwj8dEnZ3wzqzYLwzcnwsQEMsoOTDRWxmyJHlK2_kT-_oIIIrHIMMsZv8YShzBeaXy4llT7727VY3ObOlXvIxbK3zGO3ybJ9etEm2j33En6n_B-vWQoTHlXhoQNGdOgnfeprVWniPzB9uoIStFJp_mQkGgTkV0K1qZm-lImrWfSM6mfBfQkVRXetXvL7a5BptfQjcpqr9t_iOagdWi3id3Z81y6qZL6euy9Kdd-vfC8xJP4NB5z_mqBoKnswdppZIzTmgSucvRpyuNVmkSrnVe_2ng3J93C-0PBkyLcgvgSj2OWVsUCYQPniT61j2QF5LXOowxY7Ik_rUt20G5f_qZXtX5ZljUfHSU_gnqjnU1xlRutOPz8iu9mzU1apogbZplkiYuXazAtvslA-QZxhtuBHxUpAzwv60zmOGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol7lceJ1P8XC0E7DmUvWkV_mzPEFyQmV7Z19fI5vsLr_MJw90QP1Jm_ENhf1UBmOhYike1j5X0HnNcYJ91wy7LSR439p90zVdfnfO-STYedjHSaxRNW39CUbRspLcIjHTIDiz_oWuQPDid6JSdTUjA7jFY-CLX1TSI40lxEIPzBmhq2XEZB8vyE2x72d-Tfg7k-oar-Kp5QAipB6vKruzT-mPpnAhbJDqzfYSjvPg2nwhiQ8qtSTMETCtrx_YZAncPzMDE3gKYp17fIo401rqTWpCwwTw7iUl3Nqwjj1fO9OhwSKTMXSW6uymuWh69f1z7ycIIa8vnCg2EuuAJ9yvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J1INunVeN6G1YbQfez-eOjlUDrtGlNUauozvFT4gHj_qnxXG-1QVbwYE65xVhdlPKLGMt-ATXEljmmRaOqroWbYUQJVV6DtWG28AWsskh6inLnQmD2oQBVH-mCN-phE9i6kZE7dABDqtIXQaYoRRRuqfaIBaWKMvEaI2jCHR852-aZbypgNd2Bt0uIR7Lo5qXNK9ygk3opk8qDYI_mDqYUWxPoAlFqRyeRCnDqZJ44coYUDp2FkYuWBEYX2xODDM1lLvsAl6WDP1yradsHBYh8Ov79WX0I1qU-A8hDcA7v-Isemm81G5OCoQj7A1w-elFm-xAeEV6f2Z7deAX51TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vvg3wwGVC5pZc08MKzC584WNFCMZULVySx5sXlVU7_oMW5345pTzpIZzhIIMmTlAwfgGMiDZ-ZLl9LJQspSRk6QnFJEmf433gMkA6aVd8mbvXyQ-CHUrnC5oB2iukQmmSXUS9kZ7PEQ2nO15eR3RXyBrtxMSpwZZgDLKK8SK-FKucekxTU6qYuMeL9puf66--YpKH0Ksbd_iIjjHOTMfc7FSJzbAGC0pS7NIM3PkqWnYCpMLsAmtGkrZCbWIy2AP-d0dOpNaF9J7k2FxWolMZCoI8Q-t_rUN3lsPYCCcnFxP5bUkWSqQl_wN1I1zK93eqtLnWLLAO-Z6VJd8d8pyog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=oCj3sd4rBXHz2OVBZxSMLYvixlwjFNnUjEufYs4TAUWmLLh_IdMxZR5nE7BgvXQq4sAm93AByBs0F5H3oVqdQ196w5FU9GsQAs1GxYUoS6UsSJCWc4z6cKg2DmlLYoZRy-YTehSchztfSlqKk0HRxu4yGJMEk87-LE4vcSTcDUe4_ZUy0R_ZnRNEqQf_-NWNdJqliB_VDQKPAvI3gZT2QBdgINqb4HAzFL0SVK-8amtA0U054SnTVpYHNvEBYmyrQLtLXV_8jtQQ1BX3pSaGUvblHSzf0tQ2hbozGCk_fOrTDcnbiRjIzcFGvv6N2swKcbyRMKVWOQYy2ZEyGpkepg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=oCj3sd4rBXHz2OVBZxSMLYvixlwjFNnUjEufYs4TAUWmLLh_IdMxZR5nE7BgvXQq4sAm93AByBs0F5H3oVqdQ196w5FU9GsQAs1GxYUoS6UsSJCWc4z6cKg2DmlLYoZRy-YTehSchztfSlqKk0HRxu4yGJMEk87-LE4vcSTcDUe4_ZUy0R_ZnRNEqQf_-NWNdJqliB_VDQKPAvI3gZT2QBdgINqb4HAzFL0SVK-8amtA0U054SnTVpYHNvEBYmyrQLtLXV_8jtQQ1BX3pSaGUvblHSzf0tQ2hbozGCk_fOrTDcnbiRjIzcFGvv6N2swKcbyRMKVWOQYy2ZEyGpkepg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=tiE3CWri2WlvI5Gvs0AyD6IykgYpzab9qxR_CqlddtN-GftEKHCjVO5chl3gOfcKVVb4U-4pGPm-ipNDuGFFzrQgB0FKvMzFaNl7gpvizXb9lfXJgt5e9a5J18z4rp5uEtS0n_Ey_nF244_LV86ftx7M7n_02fAmaobc2HWyfC1L4nQ5a_nTYj6bB6MCwCdz7UcHkEr7PNuChmDOJl7iCovY4bNmWeSKiUdB50_SzDeIF5gR8-wD6cct3SYF4GPn9r3esRFzKeaNaKBEBLCp009qZHNJ3sjZYK43NCO6gvZmDtE4n0eDPntxTMKxPL_5v7mKEOvThTjgYTSt1qbzmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=tiE3CWri2WlvI5Gvs0AyD6IykgYpzab9qxR_CqlddtN-GftEKHCjVO5chl3gOfcKVVb4U-4pGPm-ipNDuGFFzrQgB0FKvMzFaNl7gpvizXb9lfXJgt5e9a5J18z4rp5uEtS0n_Ey_nF244_LV86ftx7M7n_02fAmaobc2HWyfC1L4nQ5a_nTYj6bB6MCwCdz7UcHkEr7PNuChmDOJl7iCovY4bNmWeSKiUdB50_SzDeIF5gR8-wD6cct3SYF4GPn9r3esRFzKeaNaKBEBLCp009qZHNJ3sjZYK43NCO6gvZmDtE4n0eDPntxTMKxPL_5v7mKEOvThTjgYTSt1qbzmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YE9BVZBJoWkUKTtdpCjZhRL7b9xujfoiT6ReQ7yhHUrIz58uCyQihGHa7JOl8c-ASkucBMrygvRbDGb4QkL7aNhllH0Ql-XhQYWRUyTafnwZqbkQ_rlmCoCBxRJHvK5dVOXYcGB0wH4zPhJeqoQCxPi11WHTdbh1d7FzS048vXHJ85tydxLFVu7lT3Vp9Vye81fYj_h6zEfu8GCRplqLmsVbrxwuJTrlYJXBZvdl_PM4tBHF9iGptSbPtNMEOSlGrBCWn36mfdP-Roky95TL5sCdS8hARWsm5VZMSf-8t_yK54h0BrOKjoPMec4i63ChlhKSnM3nKo-dWibmAzWO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=c_FnaA0DjY0IDTPCYLdiJ3A3XJMGp0SZQ8fxrN5lKLHBCVyHxrYDxvohQF37fP7xFqvS7wywLxxXsyw1vQlynnWOZlld0HrSFJactoN7-0Sfo_BBQEg2O6HfFSmu-XCCeopISSSskMZJJ_4iPpwKsYMOybrmHU0pwc0pSkGw_C0nF1XvmIbKI9Bsklke6bQIeFeExDVncmz2oBa8OSJJyBQKqYa8arqpWop79QB_Yio-xfqfj3BUuiyAJUb60WIxKQUfoabBKRyR5srDY9yLxEhaW6x1G-1KQKbsM0lC1p3V1WPQGasyQdTlrXjzgOhi-19kOzp-SwV3p96VF7RySg55UWZL7AzAB6i51PhyeP8Us16iAf9Vbtf4MmeahHEf3LyCYh9i4l_16xd3pflAajFzDwJw7k8A7tg9GOle7JC9RUVHH-51N4FyDKTryZtKdKbig0zyUohXUYKUViffAuxG18aTk5HQq8ivjZ9zeM2tSKJqQurkTRM3qSFMvvyYcnrd5ZCDZqNFG2qD_ttb6ZLUDbrNrxbG24nKWK7Zya3FTCQM1PEhTAgnF3tf4B3UPI-7fksHtl2JItquiLEGb4KfmZRbNcKMvWctG4OYOl3S7ZJGmu37e3RTRfRpUZdEV6K5OlibFxO9r6j3lqsQ8Jb9wB6awrbIBLU0Ux8Vf3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=c_FnaA0DjY0IDTPCYLdiJ3A3XJMGp0SZQ8fxrN5lKLHBCVyHxrYDxvohQF37fP7xFqvS7wywLxxXsyw1vQlynnWOZlld0HrSFJactoN7-0Sfo_BBQEg2O6HfFSmu-XCCeopISSSskMZJJ_4iPpwKsYMOybrmHU0pwc0pSkGw_C0nF1XvmIbKI9Bsklke6bQIeFeExDVncmz2oBa8OSJJyBQKqYa8arqpWop79QB_Yio-xfqfj3BUuiyAJUb60WIxKQUfoabBKRyR5srDY9yLxEhaW6x1G-1KQKbsM0lC1p3V1WPQGasyQdTlrXjzgOhi-19kOzp-SwV3p96VF7RySg55UWZL7AzAB6i51PhyeP8Us16iAf9Vbtf4MmeahHEf3LyCYh9i4l_16xd3pflAajFzDwJw7k8A7tg9GOle7JC9RUVHH-51N4FyDKTryZtKdKbig0zyUohXUYKUViffAuxG18aTk5HQq8ivjZ9zeM2tSKJqQurkTRM3qSFMvvyYcnrd5ZCDZqNFG2qD_ttb6ZLUDbrNrxbG24nKWK7Zya3FTCQM1PEhTAgnF3tf4B3UPI-7fksHtl2JItquiLEGb4KfmZRbNcKMvWctG4OYOl3S7ZJGmu37e3RTRfRpUZdEV6K5OlibFxO9r6j3lqsQ8Jb9wB6awrbIBLU0Ux8Vf3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=ma2uJKp6PZcxlrViC-II5dg_ezDlYczUUdxypC-Uh4BnV8pFY08BxZZiXOjiTaYpjPDf7YCnae8qK0xg85DlU4LWdtk0Jgjy0ISfuccKQx69eKUjyah2vvngWk6eJzuI3seroZ9CRGnBVQHqXWOxH0qXhMOKGrF2jphQ-hPGVWAv56Q7xG1UBrTt83phZx0CrXC7uaXjSA88FF7fjClBUfw3-7JmZ78GDPhPTvkMgh0ngPypa-yuHIJX0t2UcB1ym1RXRPPHtw556YPwrniaRbbaG7uEKwQNOgIawQHqGC3LDl7FtQFXzjsURhDMO6wUsvu1Ny7zsS52XbN22-QDRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=ma2uJKp6PZcxlrViC-II5dg_ezDlYczUUdxypC-Uh4BnV8pFY08BxZZiXOjiTaYpjPDf7YCnae8qK0xg85DlU4LWdtk0Jgjy0ISfuccKQx69eKUjyah2vvngWk6eJzuI3seroZ9CRGnBVQHqXWOxH0qXhMOKGrF2jphQ-hPGVWAv56Q7xG1UBrTt83phZx0CrXC7uaXjSA88FF7fjClBUfw3-7JmZ78GDPhPTvkMgh0ngPypa-yuHIJX0t2UcB1ym1RXRPPHtw556YPwrniaRbbaG7uEKwQNOgIawQHqGC3LDl7FtQFXzjsURhDMO6wUsvu1Ny7zsS52XbN22-QDRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAPSocpFObkt1MUgplWWx8XGOM5L8Y8ScDY8IMHswscFwJDgIRBKmbWnGWW7F-Ude7XCLcQr2IcovB8ty61dStubH7Xp-AmxGMZW98l5WydpnQ8vZf-jmuLQpKPpMi-7468ZEFbkISg5JmDESsC0R21xBH5jtZFGHkIhjUZ1uC4jf15gPqOXxKtdYCTphcLPx4oRIeH0VCOzdk4PJxexMEKEELbz6yXRlExNaTg4j9S0UMIZx29Mq0RmDcUrSOS72yTAOu8ej98rq9gLDfKV55-flKj3JcgnxLsvLzNjaxN2j3zuf-PptBGPetGE3kkGC93-McTD2g083clmQ6NDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=inYnV8pSmbgoBnBe5UgCgCPACLo7URtVlPUBnLN41SxC_yVJzmcUenItn9rsIzGryyKyCDWZfI1XRjqh4BfngyV_DH-zg2ioYIAwF7IH-DEW2UuGkCHtcpnVJb-Enf8Z_8VWHkwI8RWtJUGSkgsy6zpmk5wq_sYZDmIWBoWz2a_Ktfye-R6PyqD9tFPGBYXhQBlrUuVMyz416v1zzyneL5stMmsxSZcCuEkL1dQVNV9GBXwk5srcEB5KvHt5S_PjJmYEtJQN9Xv4KE3uS56o2fIrwhgzWyyl-5H0gRs9CwpaBX_KGCjP3nctKwhkUriPuMbDKZ1P-TsQu7MvgtbLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=inYnV8pSmbgoBnBe5UgCgCPACLo7URtVlPUBnLN41SxC_yVJzmcUenItn9rsIzGryyKyCDWZfI1XRjqh4BfngyV_DH-zg2ioYIAwF7IH-DEW2UuGkCHtcpnVJb-Enf8Z_8VWHkwI8RWtJUGSkgsy6zpmk5wq_sYZDmIWBoWz2a_Ktfye-R6PyqD9tFPGBYXhQBlrUuVMyz416v1zzyneL5stMmsxSZcCuEkL1dQVNV9GBXwk5srcEB5KvHt5S_PjJmYEtJQN9Xv4KE3uS56o2fIrwhgzWyyl-5H0gRs9CwpaBX_KGCjP3nctKwhkUriPuMbDKZ1P-TsQu7MvgtbLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO50nJEJIvYE5pMzI5IW9QDCwM9Cl3_kSFkgPuMuWUXnP9K9MLuuKbOdbKPz1wxj5efuAFWID9KvYKRXhVSNgFS_g8Nxoi6IL9EHOUyGDuUyx9ZBXDTVZnmKpC607AGPdgSrCszMnbiLmZrutqnSVuU8ZBAyUevD7ynqPBpmszTqkGRiRbGv6EkJUHR69mJpAd8xJtrNomdKke8dPx4PpYN626i1JqbvHClbPGTvo0BCR97ZrZBfJ7BEANVvKKtcR9BfUD0MLNvx6Dq2ZdS_nFqYewWN1rw9GKiPBwK_xKX0ek0paSmzLjznHXDFN-ahMr6hYDUr1zz1nQpMN4OaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9JWt4qyrbzargX3iSypoAEKj_IIckLCLqJp6vupF3H9SlC0F0zIo0zVL0WgZF7cJGQj7dtCnqS2-znaZyd35TnKyYO_9QxGhgmx8u4z_4ezCpJqi5zJeLfONeN9AzHDHa-FejJs3LQLjnTWRcbOw1uGm6sBXtBGdLwf2YduF0H0MqzFh4IHdzVYOHVy8HVbF5hfI3BirFADk1eeRThuOV3pflQxRaJJLQYqr6Cl7tMDGlCL5ouUNLHgP_ZSNdgCO_PjO42dcFh7iuePaWNYEp2Qt7-PjVDOtdzD5DCiBNPGWcKNodvF0nqa6DHx08qNjL9scgbn3shm-8dGUMyeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=Jioa_x_mGmISXAsKiXN9_5mZagR_2tv4yhVlHBqfEa--X-i3W3N0ffk9S9YQbipXEkQj5FOwP4J_9eWRXa6PuRJdmdw91zMV44Cb-BeYkQ7b9O4LD7Lr00emePl7lghK-fPFnLKTNfEpnJZ-j3HTlzKNc5a-yPalkVlrJg6a_iIy-O8oPGph-0vMJ3LmnoqblKA0AWb82p0Iz0Z12to-JrGg68UtUPiCOdFND7-_JjzKhcZnd1W0v8laLAgXoeoSNnhnXI6PR8mlWyrPp25iwqpb9l7sI0r6aQTyYLDnJc11YywdSW7LtpgPVXfl5G5eqZW2I52zVOLKrOICrUDTHKDTcVAIhcJoRgpLhHuMa9s3gJ3Zi30rzZaLannbTg7GsErUvgYYPkDpYUdipN8WMjA8PhKDRU6WbxJ0UdZRaWAn4JLQO4qoMdivVRSf4voUPnLcIr7CYmUof3ClF5SYmqNctokwWnVFXaBRE0kgToM4hKo8T8-_8t2CsSRV2iUgm3X-uy6ij2Hql5X-bEp_WeoO1_tGj3rBQSGGluHLnOwZxqFvWzWwD7tV0D8IRD5kVF-UHKVgMbtHABMxyY2J-PtgZxHElobZl1TP2HLUGFllol53wsaM3gSHgV-4IPV0fdEx8ylighVWhN_JDax6s5MGxiDc9VGhrTvNZNL_2tc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=Jioa_x_mGmISXAsKiXN9_5mZagR_2tv4yhVlHBqfEa--X-i3W3N0ffk9S9YQbipXEkQj5FOwP4J_9eWRXa6PuRJdmdw91zMV44Cb-BeYkQ7b9O4LD7Lr00emePl7lghK-fPFnLKTNfEpnJZ-j3HTlzKNc5a-yPalkVlrJg6a_iIy-O8oPGph-0vMJ3LmnoqblKA0AWb82p0Iz0Z12to-JrGg68UtUPiCOdFND7-_JjzKhcZnd1W0v8laLAgXoeoSNnhnXI6PR8mlWyrPp25iwqpb9l7sI0r6aQTyYLDnJc11YywdSW7LtpgPVXfl5G5eqZW2I52zVOLKrOICrUDTHKDTcVAIhcJoRgpLhHuMa9s3gJ3Zi30rzZaLannbTg7GsErUvgYYPkDpYUdipN8WMjA8PhKDRU6WbxJ0UdZRaWAn4JLQO4qoMdivVRSf4voUPnLcIr7CYmUof3ClF5SYmqNctokwWnVFXaBRE0kgToM4hKo8T8-_8t2CsSRV2iUgm3X-uy6ij2Hql5X-bEp_WeoO1_tGj3rBQSGGluHLnOwZxqFvWzWwD7tV0D8IRD5kVF-UHKVgMbtHABMxyY2J-PtgZxHElobZl1TP2HLUGFllol53wsaM3gSHgV-4IPV0fdEx8ylighVWhN_JDax6s5MGxiDc9VGhrTvNZNL_2tc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxC2mpdAok1zvNECl5tm6Jq0U7K9NKoktP7VZKWe21DJIfC_5gciGMu-YpLpOyQC6wLLBBILtvBRF6I9ZmEOY3ChQLkUz3_Ypv601OVy7bxQy_Z3k-I8ejdjOvadaAmT4ipPXfF5RKyZ7ZiVcbDeBf_y0RZxL0juljYwDjgNeQxRTj0ShvejKZ1c0wtp13kMsKNI1VJSxrHMB2Dj5kV-x76WKRIoSqSdhEhKy7Fs89f7MB4_f8yDiSfUrObRUPd6I40h2lEXKyoG7S1hxfIQIVyyrcGVtSpcn4n6_uzwvgtSIqSM8sVV6itMwTO_eo7855onK_e6PE_qyT0bOupysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMAa19cw3HO0gru0V10RtFSTfd8QzC2tQPzLOHZn0JnU1Zy9o3WehVfMLgh-0aV6DThsgdzJTLjuH9LA0LRDzWxatVn1vPNX0z93Lax8vsJSuGGxAW_a1uB7_Kd7aHa-KP_vxUe1yEoBQWFfs_tPyQFeJKkXm6fFON9J3aZwlkc5EPxsQFnm27TgElIJwb8igVZMaID5pusagGsw423yn4s-IMlu1M2lGl4NwkJc7fhD53qOA3FB9dhZ2YMlUZJ1SGitFbhi-VxSS-87ipMK-ckko4OI_kia4FVaim6cjPRSkHvgc0bVCrFexMksCnwZlX9l3LytTvuSCkDBHQENbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=Lp0LNQSt56ZfHx7eh_W2jFJmdYOQCmwF1WzCM8V62vfnqsFY5uc4WMfPsYSB-63t-1zadwmqwb0Wquf_wHk6sr5kOi_PM1O0x1YzyMfQOwQQ59iTaUf1bGgVNk1wSCrB2h_AE-DaGLxt0rD5V9JHk5qOTaUpTOK3FqF8LxwJuG8aaARTrXXhnAP77gaXHucNG_CsPWY3kjUOcXc5HudXPJdsfSbO4BSubr2BYx5RElHtnKyFuMoYVuAhQyoV-g6LFH0hGjIUL7yTCmIk-huHAILsmc0u2nzSOEXmbtAfEgjvT-2b2WQuY702H5Qn7wg4w03J0zYiK6OHuRzAnXZ5QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=Lp0LNQSt56ZfHx7eh_W2jFJmdYOQCmwF1WzCM8V62vfnqsFY5uc4WMfPsYSB-63t-1zadwmqwb0Wquf_wHk6sr5kOi_PM1O0x1YzyMfQOwQQ59iTaUf1bGgVNk1wSCrB2h_AE-DaGLxt0rD5V9JHk5qOTaUpTOK3FqF8LxwJuG8aaARTrXXhnAP77gaXHucNG_CsPWY3kjUOcXc5HudXPJdsfSbO4BSubr2BYx5RElHtnKyFuMoYVuAhQyoV-g6LFH0hGjIUL7yTCmIk-huHAILsmc0u2nzSOEXmbtAfEgjvT-2b2WQuY702H5Qn7wg4w03J0zYiK6OHuRzAnXZ5QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=rCHwxL-iiDqoa0aWLl8PfGuR4zQBH-e0yWH5N_3Yp0V38XfqeYty2jlg5tZFSZ6Pv8YyRcW2DmDRah627jiwp0iRngaJKU02BlDByu_ZxQWSk_vw4Ty1LrliBn6ZEOlkPLqRRw7qN7lXlT0pLYA9eGKugN5I3aADVKVGh6TjzKxcwDDdZt-FYXiYxoC8qKhA36rQEG43Hb7FiZpE-HulIcUfrhbxiM-QpDI7B_kq3B8LkUt1KwqMA7lLalFfa-E03PytNVAEftIWvBWQ90vRBLsPhTElCJ5maGpyQrodljmL4Suors0BNnG8ynS-aSdNwW75iLoN8ZBFCmzCcZUz1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=rCHwxL-iiDqoa0aWLl8PfGuR4zQBH-e0yWH5N_3Yp0V38XfqeYty2jlg5tZFSZ6Pv8YyRcW2DmDRah627jiwp0iRngaJKU02BlDByu_ZxQWSk_vw4Ty1LrliBn6ZEOlkPLqRRw7qN7lXlT0pLYA9eGKugN5I3aADVKVGh6TjzKxcwDDdZt-FYXiYxoC8qKhA36rQEG43Hb7FiZpE-HulIcUfrhbxiM-QpDI7B_kq3B8LkUt1KwqMA7lLalFfa-E03PytNVAEftIWvBWQ90vRBLsPhTElCJ5maGpyQrodljmL4Suors0BNnG8ynS-aSdNwW75iLoN8ZBFCmzCcZUz1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=A-vOoxkRk_3u-p_ei_cl5qc82V5jac7cVrA5CZst9GBQkZbUmPKwC0dcAEa9hbLzgeKBuZ5bc4FO0mdoC5UyJNjHjjwUVarat8IgS-waMMzSCScS3KYlEnL018mn2KJ9DzVJScCz-wwBpBU7QGU47XMSq_eeATi3bNTbYtGMqn_3tMDhCK7Zn7Dn2PEtm8TFpeJSYLav8zh1AM42tel99jWMeYau-dEFOEAdGt9f_HFYKLThDZ4sVmiOKODMV0VeNvouN5FdoBdfyTpYBPyh1TEKp0jt7Jtyy-blDYb_awwu_IQyL838hbnVsi5YTy359NOf040HGGJmziavPbUQSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=A-vOoxkRk_3u-p_ei_cl5qc82V5jac7cVrA5CZst9GBQkZbUmPKwC0dcAEa9hbLzgeKBuZ5bc4FO0mdoC5UyJNjHjjwUVarat8IgS-waMMzSCScS3KYlEnL018mn2KJ9DzVJScCz-wwBpBU7QGU47XMSq_eeATi3bNTbYtGMqn_3tMDhCK7Zn7Dn2PEtm8TFpeJSYLav8zh1AM42tel99jWMeYau-dEFOEAdGt9f_HFYKLThDZ4sVmiOKODMV0VeNvouN5FdoBdfyTpYBPyh1TEKp0jt7Jtyy-blDYb_awwu_IQyL838hbnVsi5YTy359NOf040HGGJmziavPbUQSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqYlZ7kse59shatz6pJ5p28cBAAWHaBBtxH3HIbLoCx5NktspD7KgZoTN9n9Ae-TcyJPNHWivgNgdBDOngxV-9TnB_A7KfbRhHl4gBWQ7jiZLb_eeQGf2wPLLVvLhE1gvudCXeI2sQPwZg7mgjOZpIww_SxDeV14UG40FiduKfP3WXBKEVb1nw_IDXZ7S0hMnXtqAiSEhkMkurwXkv2B_uHDgX4yoOcrhGhHT1Y0N-BlPp2WxAO_nLuK-MOrgyAZ2wbAsNf0H-RzuI0gZ46V2lpdqsZDs5hHk4cbUIpN0Oeqf46srtM4CvG_gspjWv4aHm1rLjTq41YR7gTJAjk_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8C3a1ObXuHMB0s7IagpmSS0XWtBHQ9_vj91xDPtrerxkRIi_1nJiIEn0gjFMCaW9G_l3MWUNEWx8L8_Hpqv-WdEv6w_lAX9zED1bLOKUutnp_ySAcKg3Om62T4Jva7FY3aor8zoppjpCv54wY3POXCPIAo9eUeLGq1Y17NGcHzu3SHeD8f5XW8Utr5wXx-jhEzazzJKL1fd9B4AuFABa5gODunl_gMQDZ6A8u5k2LOAo1rej0yD89PHl7agjZbMDwopWGFQdSh32inlHobmSFx1IX_dLNLn7FrO5iQ0YSwElNPgyYQbq7WOuucoYxGG18-ADT74OZLrlqkFdTeo1HZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8C3a1ObXuHMB0s7IagpmSS0XWtBHQ9_vj91xDPtrerxkRIi_1nJiIEn0gjFMCaW9G_l3MWUNEWx8L8_Hpqv-WdEv6w_lAX9zED1bLOKUutnp_ySAcKg3Om62T4Jva7FY3aor8zoppjpCv54wY3POXCPIAo9eUeLGq1Y17NGcHzu3SHeD8f5XW8Utr5wXx-jhEzazzJKL1fd9B4AuFABa5gODunl_gMQDZ6A8u5k2LOAo1rej0yD89PHl7agjZbMDwopWGFQdSh32inlHobmSFx1IX_dLNLn7FrO5iQ0YSwElNPgyYQbq7WOuucoYxGG18-ADT74OZLrlqkFdTeo1HZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=s4S0rqAiwSXrSofLw7WKSLnScV1cC1pOd39OFtqlOr67eCL77VtXdBtu0SpbOrJprkB3J6GgyM8RpzPtJ_R4MyuQs7wKlgdjhyaQpxD3iFRe_XRmccsYpnWjDW1URpWdIEK55o6yz50H02aIDBrDTaiMDMYq3Atq_CKgvt8Cshkp6E1_laPwrDtCOHb70XzrAJ75cwPGTipYH21lkBnBArfGDBbtgZjJYxN7WRLIYnXoEkr7JSVLwWoWGwlbBtIbtKmf-YAvbuAogLILbJv2mNgp4GCM_Gq34wpWl4YoNupT7OeFIfUwqtv-s9sSeyAx287KiOGGBCBlbmFf6pUMdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=s4S0rqAiwSXrSofLw7WKSLnScV1cC1pOd39OFtqlOr67eCL77VtXdBtu0SpbOrJprkB3J6GgyM8RpzPtJ_R4MyuQs7wKlgdjhyaQpxD3iFRe_XRmccsYpnWjDW1URpWdIEK55o6yz50H02aIDBrDTaiMDMYq3Atq_CKgvt8Cshkp6E1_laPwrDtCOHb70XzrAJ75cwPGTipYH21lkBnBArfGDBbtgZjJYxN7WRLIYnXoEkr7JSVLwWoWGwlbBtIbtKmf-YAvbuAogLILbJv2mNgp4GCM_Gq34wpWl4YoNupT7OeFIfUwqtv-s9sSeyAx287KiOGGBCBlbmFf6pUMdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOoqzcIK4l7D0wAYXiTqKUz0-PSsEniMiSunlpmw1eroo_6uwSUJ3etiXypMGwY9Ccflud94nK3FJpj691AdInDayD-c217GgVm5rKjo5HMWlu6aIuwIWTkFTypHOt2GQMtVhTI16kRVL2radQVcW5eCaJDQhhXsYeOWMB-YOgqusYrREY4a9Tr5JiGQKpKFGua6-7ifcW8WGc0e5OQQ58U6EL7p2rKYZ9rTRUIY0CthBAMgylGgfZga938iEjacSDDH7i6TYzH2mbLt310IJKnk9H_8ENtTFY1P_z2_5vXU96HuJSfod1qdm9xjZJZsUaxKnofljHr4NQ_uWdZtJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Rs8F5zFmM4pzJSyRGS0o1HuVkAaYvu1TBf98CpYU6aE7tyct7oSitGphug2GMwLWgRppcbvs1iXXn1XtgvMjCbl9S90QQ2fjo53IMSE-tfQusfE6iQaVQbXw0Vt9qj0d2CqAfAOu0EQC8pTgl8DMdnnsF-wWl6DGb3e5tvaoFRR3PeDrS-PDVQz6W395U6NmsvRngyLVOrMuEloRoibxLTGcJ4UgH7yKxl1Thsw5wbS2rPIUotJGP2l--zdYptgfF66sfeqKiT0655-bxpDgxb4KLQMan_tVWYSb44dFznwY5IRddox3viX3FZnFfz-zE629MsEcfz1C_freCGmB5HyLZezq0I3RZ-AvtoXLxeS8jg8zStRBKKefHozA7DcP9KcTMJB8ULMa0gMP0oupGukKMLilKBdpmQq-3JPJ-8IwBaC9krw1eMcpgV3qHCw0TliB4dyQ_bpO0T8snGrz2eHweGiyeip0X2yiWEv81AnsN0KZ9QZrM7MZUSFwol9L3KUI0k1nSjv2cSySzdaBoLYfFU5SmkdPqydWFDTNJDGtH-8aBzpjXVQw7W5IqOVwoolKUfSsB_0dEjGABjIWCoSdRGl8Sw5jX4GTlERMKUDOdIE0azdQZoEmza6KJmiTixgHCQMRO3XDPYX4E7yD1YIHxsrBmF1Dn0oNXYHnCyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Rs8F5zFmM4pzJSyRGS0o1HuVkAaYvu1TBf98CpYU6aE7tyct7oSitGphug2GMwLWgRppcbvs1iXXn1XtgvMjCbl9S90QQ2fjo53IMSE-tfQusfE6iQaVQbXw0Vt9qj0d2CqAfAOu0EQC8pTgl8DMdnnsF-wWl6DGb3e5tvaoFRR3PeDrS-PDVQz6W395U6NmsvRngyLVOrMuEloRoibxLTGcJ4UgH7yKxl1Thsw5wbS2rPIUotJGP2l--zdYptgfF66sfeqKiT0655-bxpDgxb4KLQMan_tVWYSb44dFznwY5IRddox3viX3FZnFfz-zE629MsEcfz1C_freCGmB5HyLZezq0I3RZ-AvtoXLxeS8jg8zStRBKKefHozA7DcP9KcTMJB8ULMa0gMP0oupGukKMLilKBdpmQq-3JPJ-8IwBaC9krw1eMcpgV3qHCw0TliB4dyQ_bpO0T8snGrz2eHweGiyeip0X2yiWEv81AnsN0KZ9QZrM7MZUSFwol9L3KUI0k1nSjv2cSySzdaBoLYfFU5SmkdPqydWFDTNJDGtH-8aBzpjXVQw7W5IqOVwoolKUfSsB_0dEjGABjIWCoSdRGl8Sw5jX4GTlERMKUDOdIE0azdQZoEmza6KJmiTixgHCQMRO3XDPYX4E7yD1YIHxsrBmF1Dn0oNXYHnCyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-cK_Iz_4exP79zZEATkE1Smp3goO7qHs7mTo1W-gyh7itJx0gpmWbMqmyyDZ6EK9mIv5RMoQ5P_7sja2GeOpWi8Lb0Y4wfpgfcqzm-4h34PeTc3RZ5V01lamOOrytAanMUtBbYchY8DeLjtnpPl1SpKYTcNU0kaG6n0JsPh7Vo2McsIVxvMv56lyiGtxn6BE8k2ni5eDjoHfgDGKX-I6gBAcp8iLvZn9npRWe7BI9RQs6Gb2RDI5gw9-VPLdgSoUPdj67Kys92AcBGq6ad_9OOIfpe99lP_Q2fct3qJXjo9qonxg_6n6oExZEb6YXWhsfvJKKm7X67Xgra_jlYMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=bLkdmNPSfgwIxz36NaE2ZT3puyYg4kTXVmuGM8VDf2jdUM5V00nVI8JyaHO6Nwop8ZAQ-iktrOjQb_W9R3TFVF1-iroU8JOhJ7NLH2yfy9nVE5iyIXtRC8ZgH1HRN7ssayO5orjgksdXc7UZdoKac7n2BfA7f91LzvrG5gZwdelsWQkAp_fU_xnxFK_H5bIW3TTs5azTl4FtuwgwFTOJIWSCgHbhdGQGBE_YliDdXXfnzi2e-KQE0jlcE0q7LmJlIxFHjMMtnDzY-3o0nSClUIJrHNxUdohdhrpAUnH6U9Zc9dz_iNBGv3ndt8cSNmeCCvYFZP1ajjTh8Tdh0cm9GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=bLkdmNPSfgwIxz36NaE2ZT3puyYg4kTXVmuGM8VDf2jdUM5V00nVI8JyaHO6Nwop8ZAQ-iktrOjQb_W9R3TFVF1-iroU8JOhJ7NLH2yfy9nVE5iyIXtRC8ZgH1HRN7ssayO5orjgksdXc7UZdoKac7n2BfA7f91LzvrG5gZwdelsWQkAp_fU_xnxFK_H5bIW3TTs5azTl4FtuwgwFTOJIWSCgHbhdGQGBE_YliDdXXfnzi2e-KQE0jlcE0q7LmJlIxFHjMMtnDzY-3o0nSClUIJrHNxUdohdhrpAUnH6U9Zc9dz_iNBGv3ndt8cSNmeCCvYFZP1ajjTh8Tdh0cm9GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlBNQ2-fB5gxsxWCmrtm5ilE7eSyMdXdv1G-esL--QEgDIexYNNAX3uQulfCfLvvKoYVRJ0yFbXZXMDN943prnIsEUvHuxL7xowd00mDiNjQ88BaMUorDp05FzQFrh9Yo1w439MaFHe7zfapqJ3kPgE8C1svkxxjJ9bKRuuT2S-6kcMRJGDGGG6UpVE22SqMIJx91vfPuDza2MyNU-B4pzJ1BscFXJqgNsqhBB2MmTt7JcVS-rOvfdhwV-NxLHSXNFNekNuDUhp318kiNAYq5_-WKqKgYuU0tScsNNGjnR1_4ugBkzXQ32ITIZuq0MBhZGPlh4VLylkRDEyk35ds5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cler070MlcVi979Jf8lpDLmlvXnjeqGzcL6e0szsPS_Bkv2Z3lNukrNX5lQe5Qc66rrcm-hRaczdXOtumsWOkghH7eBedDkvZFranXgEonsSjKjwlXvSGHlFU-n67I6RVgdw4vwmetuqiguc6AYs0AzooyCg-KQFAd-vYpt4T1kY9VwLkr6oXgKrJx72W1VLI3cuuwH0DLHgMAD1NPIPFXv8ifkPvzsr-5oopDTedYTaG8wk8z-z7wQ13NOQ7xyZ-hYpHV2WKIcQ_jQ3gYSBuR6tPD8Ce8B2qR7xjFVFujGdDSmYDIuk2gj3UFWXCIrJm_Oi4IqqRVcUL280m56xiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjOabubA95MCkX7bqCo3z8KIDyGNFJCpydORzaBXP15KF-fWu6CxLk3YoC6FSJu0JiUCEKVMfGSKL-hr_BFOPVnG0An4pIlntjgB9BCBbArWnsQ8Ic93o3njROqsHAx_tGNpEYwcmZ5gO8CReHnP5a2cAEw8Ea2gFQ24Kk5TZT3ur85mrUuBs9lfn1_-3yjSnoWCEb3HxalqbCVgccw99wjgJ9r8V6EK-lZRuqYHXi2Ht6hdX9xGRRSm0WNoZOpFor0t7sJdIBX6sLOjvqpZZADAwi5TUMYHncDNif02sV-aYSJDetATpdXIQlscZy2qBbo6yjdE0qz3agJYOl1u2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Fq3x2JePiCJhWg2ceoyFjirfhmhIfJ2EcBjy6COiTyBgUzlV6QWn9T0CJtUiXaWBe8Fg6HUYhdaBxEfltK2Df2bWoLORa5irlmm3kyBEc_nzi-LBH7pTc9M68g67u_bpvFAqWTcYzvszH5jsEMg07ClfFYor3N81x-IiVmKfekZWxlaig7iZN_wEGK8ps20rqpBbXGgz12Dsv0m72dgYNlg7hHs0VtVK94R_VigVgyr69jVId462KRg3EDO_VnJPt0NXXInsa_hYlrTX1ocJtR4obhAQeJFvb_DH8wE5KfWshYGDf-1xZEjZmVqnXUI4BOtJYRgfE1tpgQWzx38k7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Fq3x2JePiCJhWg2ceoyFjirfhmhIfJ2EcBjy6COiTyBgUzlV6QWn9T0CJtUiXaWBe8Fg6HUYhdaBxEfltK2Df2bWoLORa5irlmm3kyBEc_nzi-LBH7pTc9M68g67u_bpvFAqWTcYzvszH5jsEMg07ClfFYor3N81x-IiVmKfekZWxlaig7iZN_wEGK8ps20rqpBbXGgz12Dsv0m72dgYNlg7hHs0VtVK94R_VigVgyr69jVId462KRg3EDO_VnJPt0NXXInsa_hYlrTX1ocJtR4obhAQeJFvb_DH8wE5KfWshYGDf-1xZEjZmVqnXUI4BOtJYRgfE1tpgQWzx38k7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAsq9Vgi7-KKzdEoXTkn27trEkUAk-FDXpBIX8ZGp3QlK9ygiXTq_kb1UL-HNDcnoJsl-xaZWWiJEXzRSMPNoO_FhrtUY0OM71syCUWkoYfrzYtqNUysSkLw0L_r6nTM6HsmDMygTV9ldGnly9-zrI5caSqjrFYWqJNuo4cZquurB3N8dJv_vJdLAVBdB6MZTtPCnWLqsV82TpiLLVTXxsx3YMDJmLCd8z0NKoj-ttR9y1Xn9Kt-3B4CtHgLGjexbdtTfVt5TXuXvLr0cxseeau2uxcn0n2fG3UCJJ3QqekOi0Q2sKTCEoStUgaJnLwEX1FcNoiANPLlEGUW6BI-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2edLB2zP0lQUhRGxLrooLsAg8VuHy6j8u3qhOZstwBigKRaHMdXCWScuaPFyuzvmIWMAHR2EeIwhLEkfm42xcV8HVLLIRY7XFqv-fon3Dim9agJYYqFlC7MdjGbNd3aLJsWPMa_RFKiSMZV0kMjGHDZ2mmC-UVElQ4PHLJFp7dC6NGEPkTsVYqRO_CKJsxdMixVPQ-rQKitGS0cJRiLa9GTcdI_w8uF4lFqVGBYeeMy3WdywrB8n-f1fc17WDKDlHV_IwANedrQcikG4LzLuHF94hca72a_gWf2zQBo1mlD2C1iAoR9eAIjpuFvLmMEIdvnhI5GeGXbrDKRcR2AN_0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu2edLB2zP0lQUhRGxLrooLsAg8VuHy6j8u3qhOZstwBigKRaHMdXCWScuaPFyuzvmIWMAHR2EeIwhLEkfm42xcV8HVLLIRY7XFqv-fon3Dim9agJYYqFlC7MdjGbNd3aLJsWPMa_RFKiSMZV0kMjGHDZ2mmC-UVElQ4PHLJFp7dC6NGEPkTsVYqRO_CKJsxdMixVPQ-rQKitGS0cJRiLa9GTcdI_w8uF4lFqVGBYeeMy3WdywrB8n-f1fc17WDKDlHV_IwANedrQcikG4LzLuHF94hca72a_gWf2zQBo1mlD2C1iAoR9eAIjpuFvLmMEIdvnhI5GeGXbrDKRcR2AN_0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=g9jfaOLvEc1UujE5OEg8y8Fv92qgjtfyMfeSuL2enw9AQaT55osiFLBXQ1suUXbvHNoNsqtbueiLI4CG_LMHPnm2h369KmzbALySm0_ApW9MbpThUQVp9B_cpctvi4AvY7a-Jzq9U0KZPJySKWck1ePVtuRysvELSnGA2ZRXM4rrXS40rJiOv27LS4MZ1UU2jMKVREokiAfC9_XAZvegjcjWJfGHaelCUNn2fLhLLV5aIjdPUsC35ynh4oa4KhWMY4Wn_C3Gm9izIAkr8MZYhz_AyFDBkjnHTOd3ojG4KFRHUGJwfOoUvpkoa26N65TxjNURv7dbGmfSR_rWm3e4eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=g9jfaOLvEc1UujE5OEg8y8Fv92qgjtfyMfeSuL2enw9AQaT55osiFLBXQ1suUXbvHNoNsqtbueiLI4CG_LMHPnm2h369KmzbALySm0_ApW9MbpThUQVp9B_cpctvi4AvY7a-Jzq9U0KZPJySKWck1ePVtuRysvELSnGA2ZRXM4rrXS40rJiOv27LS4MZ1UU2jMKVREokiAfC9_XAZvegjcjWJfGHaelCUNn2fLhLLV5aIjdPUsC35ynh4oa4KhWMY4Wn_C3Gm9izIAkr8MZYhz_AyFDBkjnHTOd3ojG4KFRHUGJwfOoUvpkoa26N65TxjNURv7dbGmfSR_rWm3e4eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=eZMDgka90Za5JDmsokMQ5xZW5Quj0SStcTJytPP0D5EICfZmkYuGjr-VRzyAG1FTnmNr30X6oV3t_Px1086F0DJjFIIHRE2c4lXsODTXq8niqnZqAocjr-ZSJEWzMF5okE1MD0LXXagv1jrJgn3dGxgPZyutMWwENexnX0c1EV8G4ZMnSDtHOrQFA10SfG3jtB2F9shH5a2mhKUTL0y3S6pppwSs75OcO0rjAgyRbjTkx7uBQm2Bm3U3NjTXsWrTCkSoLk-7LqtL4ysziEQIDWqXmjlTkHCHCTrgo52jXsfeBIoR-TEBU52n2-ZkQNbjKAev2Wq4_5ZVS2zYbNpU75Q4o8UHgd86R454ou_YRg6GHCfG2b_k9DmKQELAVDtV1E-6dicAjmZBseulZWpLZ_dgua1V4I7ryPWuIMeeT7TYEsuVTynenOf-mqD_Mg4G7XFlUGXtrJWYDpRSYxwtmaSK5Myz753_1xMaCXLlVtC3UtmpZ7phf2lnfeFGvw4yg254bOL8awuW3Cx-lC1EXmwJOQwbbXZuCtuTqCVy-bhe8unizt8Eyo6nz4gvdQF9NE4SiZgO6uXXRlEg9-Wf0C04GC-Ud5crr866fNG-CiDoVjBJLlPfSVO_MzHMFFFcv1w8DRTixFIf5OgDCDlMJy1ZQ_OInRG60Z6DPRKPiO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=eZMDgka90Za5JDmsokMQ5xZW5Quj0SStcTJytPP0D5EICfZmkYuGjr-VRzyAG1FTnmNr30X6oV3t_Px1086F0DJjFIIHRE2c4lXsODTXq8niqnZqAocjr-ZSJEWzMF5okE1MD0LXXagv1jrJgn3dGxgPZyutMWwENexnX0c1EV8G4ZMnSDtHOrQFA10SfG3jtB2F9shH5a2mhKUTL0y3S6pppwSs75OcO0rjAgyRbjTkx7uBQm2Bm3U3NjTXsWrTCkSoLk-7LqtL4ysziEQIDWqXmjlTkHCHCTrgo52jXsfeBIoR-TEBU52n2-ZkQNbjKAev2Wq4_5ZVS2zYbNpU75Q4o8UHgd86R454ou_YRg6GHCfG2b_k9DmKQELAVDtV1E-6dicAjmZBseulZWpLZ_dgua1V4I7ryPWuIMeeT7TYEsuVTynenOf-mqD_Mg4G7XFlUGXtrJWYDpRSYxwtmaSK5Myz753_1xMaCXLlVtC3UtmpZ7phf2lnfeFGvw4yg254bOL8awuW3Cx-lC1EXmwJOQwbbXZuCtuTqCVy-bhe8unizt8Eyo6nz4gvdQF9NE4SiZgO6uXXRlEg9-Wf0C04GC-Ud5crr866fNG-CiDoVjBJLlPfSVO_MzHMFFFcv1w8DRTixFIf5OgDCDlMJy1ZQ_OInRG60Z6DPRKPiO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=EdLl6xjDR_ou-B92TPVbjAtZfaADB4-WR-_i5ze-9MSYwiXG7A-6NgwgSYhwPVtGMXpyD1wbkmmngaZuqcv3xS6RgbV7ZOH6EjamAEEA5fV1vIMtWVB5-jv8xRiKqun6yjj6-5Mn3dpXWMkOZKsrysUc9sT3qQ_hOZrJuKyeqlesbWQHObWgME5xBw0DwWxxFUfDC6-eVV4H_iGfybAqWuF7jze4ve0OVEmt5QGduyaWZmhLUIHP8nb6HINl7r14-vBaSOtP9xTSIM1YKgpY_GcFfP8XNJpP73elkTeicqIqU4HWZVicViev7BZfiCkiLlPxrddFQa4ydY7ptQ0f8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=EdLl6xjDR_ou-B92TPVbjAtZfaADB4-WR-_i5ze-9MSYwiXG7A-6NgwgSYhwPVtGMXpyD1wbkmmngaZuqcv3xS6RgbV7ZOH6EjamAEEA5fV1vIMtWVB5-jv8xRiKqun6yjj6-5Mn3dpXWMkOZKsrysUc9sT3qQ_hOZrJuKyeqlesbWQHObWgME5xBw0DwWxxFUfDC6-eVV4H_iGfybAqWuF7jze4ve0OVEmt5QGduyaWZmhLUIHP8nb6HINl7r14-vBaSOtP9xTSIM1YKgpY_GcFfP8XNJpP73elkTeicqIqU4HWZVicViev7BZfiCkiLlPxrddFQa4ydY7ptQ0f8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pICVvWO-HXv1Okml39Q9ohqgtPuCCAgj_sG2A7fuF0jmzDxpel9O2QVdoStWWAW2pJYWNyAEL93906onHY1wddCVtQhn6Jbo8YyL14ePwzHQJ1cPvETTf-bJBqmkD8f03dZCeSnerHa0138SwBLOz87yLCBGgjhvsAtsTOjE4UaSmQu8YfTY7rEz4hm6uRWsmqK9uu7E8Wym0o1IYw6X6YgSm7VfC8jkZcwLVYCudCqbYx0NfKmNcUzrk9CsmtYNHQOpFidIfNPd1ycFdXJ9fIuWkTbdNLXopcWki1tBzExqnTgd3t0pld4MlQ7xmzdlM0ufx_l3J0mqpDNlwMNDrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=m8jDr0GRhl2lkCMZDfn6CivebzHtwhTxoHpXU0_MI2F5YpF531vNGzKrAZfkFZgOBP5IESiDzzAOcMwfzTfU5vxM41xu5KF1BNkDCOSgnaY-PdPqI4MzXZsxi9eAZPhr0c4qDrVGevYCywB57lU4LczCAFJO2co0plw7jOUeeeTjUkeeIcb18Qh_mcW-vtpjpHQopvwOxHEI0m0olylnDbVB5jl9bHM3r2uqOx5Kmn-0EyDH1s6AmQ-8lOfnxAoygITKN52l1Zrwe19ze6yzru2Sysmm9pvSpbEZYKO5Sw4aZ5dhlNPvlZo273dS0ZwvEjWXn35rMTxjhzlSFMDveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=m8jDr0GRhl2lkCMZDfn6CivebzHtwhTxoHpXU0_MI2F5YpF531vNGzKrAZfkFZgOBP5IESiDzzAOcMwfzTfU5vxM41xu5KF1BNkDCOSgnaY-PdPqI4MzXZsxi9eAZPhr0c4qDrVGevYCywB57lU4LczCAFJO2co0plw7jOUeeeTjUkeeIcb18Qh_mcW-vtpjpHQopvwOxHEI0m0olylnDbVB5jl9bHM3r2uqOx5Kmn-0EyDH1s6AmQ-8lOfnxAoygITKN52l1Zrwe19ze6yzru2Sysmm9pvSpbEZYKO5Sw4aZ5dhlNPvlZo273dS0ZwvEjWXn35rMTxjhzlSFMDveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=dzPfF6aIUCNeEKw-e8RMQvNTbgKg6pGWmqWKNwA3OnPHOrkndS1jW79v_onDMwqUJdjsg2gjEx-EKb2k3nydYuL3959nIAaNWqaZ_a3ehf2RONkNoPJ1Rv47zA7xqa8K4tKYfRmms_0HFtt7uPbVdCjcthkR8zTpBpy-V3WObTclbJe36teXSIydxQmIKpeHJjIsPs-N5N8_57pmCqCl0qjyQgS_oXPhYDxT1MfzzlLu0P-8JObhCezz0-TSMf7LQN9r_kM2LJwukTueUhiMkUqHOZXWayjEJSA3XOsYNmdEqBrNT8lkPLzupwhyd0wxI3_8uAmLhyUhS6ioKe5LawkYrASwRU3ETsWXpy5TaUzqYHDybqdmQR-Vj_0UvOwS6WF6KS0u-pFwvUYUFHcHWUCMea3EgfJq2v9BpFPGcGzbIABx7StgoT9t2gwHun9MDEfvIHDOmF8atqPdIgLjIH7MJ1fFRKkBeApgRy-AbE632q0AFRJpacwxdm6A7Qh6MK8xQumGgLMHH-3wl86GLCObNP7cFXl8gxGJ26NSrWvZzXw7JBWMzlhN_HSlkKhDJaTX-9LXP48jwUVYLALx01_vLFo5L3Y7aQ5Qo-wZxmaRuWi4kKUNUekMcQgmvQE-LHkg6jVvjcmErqewjrQCH76gFEKUwJKFr2NFWN5OpwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=dzPfF6aIUCNeEKw-e8RMQvNTbgKg6pGWmqWKNwA3OnPHOrkndS1jW79v_onDMwqUJdjsg2gjEx-EKb2k3nydYuL3959nIAaNWqaZ_a3ehf2RONkNoPJ1Rv47zA7xqa8K4tKYfRmms_0HFtt7uPbVdCjcthkR8zTpBpy-V3WObTclbJe36teXSIydxQmIKpeHJjIsPs-N5N8_57pmCqCl0qjyQgS_oXPhYDxT1MfzzlLu0P-8JObhCezz0-TSMf7LQN9r_kM2LJwukTueUhiMkUqHOZXWayjEJSA3XOsYNmdEqBrNT8lkPLzupwhyd0wxI3_8uAmLhyUhS6ioKe5LawkYrASwRU3ETsWXpy5TaUzqYHDybqdmQR-Vj_0UvOwS6WF6KS0u-pFwvUYUFHcHWUCMea3EgfJq2v9BpFPGcGzbIABx7StgoT9t2gwHun9MDEfvIHDOmF8atqPdIgLjIH7MJ1fFRKkBeApgRy-AbE632q0AFRJpacwxdm6A7Qh6MK8xQumGgLMHH-3wl86GLCObNP7cFXl8gxGJ26NSrWvZzXw7JBWMzlhN_HSlkKhDJaTX-9LXP48jwUVYLALx01_vLFo5L3Y7aQ5Qo-wZxmaRuWi4kKUNUekMcQgmvQE-LHkg6jVvjcmErqewjrQCH76gFEKUwJKFr2NFWN5OpwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qduOWI-5y_2Ycma8lx4bddY0DMfOJp4vMrtE6OfeHFdgTEkhF9HDzFVbg8K_H5diKEvy_nct_zJO9MIgVlpk6aOu8lgWoy47Uw1Y3OXEXZC1CX2I13zvboPEQt3sykNjpM97vmR11YFXDL5N3Pndek2iuxzMxCOVEA4vCJ2J522ShSAJYn95DbPTP6TXAUqVCq5-t1mQwm6B5O1cwOOPLTv0O4MkK2-_0Ty5fJsjuN3rn-F0vv_NDIyJvALoZA6lkESDVPeowfxvtJLkxop8tZ3MlSfddRoytzP-v3tRAbJ517WO6967MGkoPhhXxiuk5UJIK-MHu4mUREAi1O-Ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=TruOh9XOinriAnWkNFKuLh09JB-GLtw4ysfMtlxIl0v5ekzBPUnkW2oMEhvi3tgZMTC66yqgVUyMz1nUFMJMjLdw-WYCOgnpvQEW3gtXOXRaWuT6KTmgf7_Wx6lm0ZgELzoptDq51irz4R3FYYB7pqx3E2sK4qWg2Hki1V7CBmb2-Yz1QXgs5S-iLBs6LXR8pZXXO322P2sqnMa5Pfo_D97xsyBCD4w_9z4p4A7Zps-IeINbxq9rHt3P7az-cX-HIXWSOvnvr80LQapHwnK9Ww_QWdJi0n_lK2iWL3779rBrxGmD1HGaATcN24xJJ9kZFBmECWVgXPG4hBBrW79k8HfRVDxL0AWPLwYJ9WjlkcbH-0xZnLE2BOKTm1dEevRAvO6wgutwfBLQrHL6UbSUqDsnvEhpm2CsFcCtr-fDr14PXcNQBGXpq52El5sIAqr6nR93h4SzoukyT8lXTjCFJJzRSa-DeJxVV34VF2poQNXiPLeac2Nf9bVvizTLAfmoB_rY0MK8agCVaAmDuM5qpVw1T06_nAslhQ8FeS9uH3GZq1QA0_w2eXyCE2Ma0jDXpaT8IvesFa45LwJ9ZeJ5sB_bU6pA31O8TWAv0PY34G5BCvy1Z1lZDo6VSfevGWKdkTqh6y9Sk48MyypWjWkDjWmqa-s1A953OwcIqcFS_2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=TruOh9XOinriAnWkNFKuLh09JB-GLtw4ysfMtlxIl0v5ekzBPUnkW2oMEhvi3tgZMTC66yqgVUyMz1nUFMJMjLdw-WYCOgnpvQEW3gtXOXRaWuT6KTmgf7_Wx6lm0ZgELzoptDq51irz4R3FYYB7pqx3E2sK4qWg2Hki1V7CBmb2-Yz1QXgs5S-iLBs6LXR8pZXXO322P2sqnMa5Pfo_D97xsyBCD4w_9z4p4A7Zps-IeINbxq9rHt3P7az-cX-HIXWSOvnvr80LQapHwnK9Ww_QWdJi0n_lK2iWL3779rBrxGmD1HGaATcN24xJJ9kZFBmECWVgXPG4hBBrW79k8HfRVDxL0AWPLwYJ9WjlkcbH-0xZnLE2BOKTm1dEevRAvO6wgutwfBLQrHL6UbSUqDsnvEhpm2CsFcCtr-fDr14PXcNQBGXpq52El5sIAqr6nR93h4SzoukyT8lXTjCFJJzRSa-DeJxVV34VF2poQNXiPLeac2Nf9bVvizTLAfmoB_rY0MK8agCVaAmDuM5qpVw1T06_nAslhQ8FeS9uH3GZq1QA0_w2eXyCE2Ma0jDXpaT8IvesFa45LwJ9ZeJ5sB_bU6pA31O8TWAv0PY34G5BCvy1Z1lZDo6VSfevGWKdkTqh6y9Sk48MyypWjWkDjWmqa-s1A953OwcIqcFS_2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=IgfcUDun-mBmd60dJ-691qHgM8LEt45oysFveBtMOrfhslATTOa3AqPod5gKMOHC3nJGdMeiMwMYjGdUU39pcmxDGXWIQxRKg0o7Yfg2TkJKZ0kLvcduN4nCroagAUOz8tT9IQciQZdghcolwpS5QeZeoJlTBhuX6Y30kok-GtCckSTECKABU01sFGFI3Uo7z-jg3QC_vSiLvqhUSAJ6Y88HJMlZ3exkkqnpQBVv-MKCUzduUgpsGpoD6fV3SsLCq8CS2y4geGdBAQKjfFb0dVHbS68ZoktjY7g0odx5BsJRpKqvUU8PckNdx8vVUDt0k6MeGVCOTF74DkE4q-UjvJif6m1gKVY-Rymy3IlqO_HgfaqjhoN2GFGhESI63_PWnqZgIM4bqCzDiZRD-3jHLcfa-tj_lHiISNk9RkMnYbylxPRYLcA_W_a6LVg9Ejxk4wUNQhWR-8McnrMM-Wgpjt--5q8xL6RLZXrgY-YK-eggdMIPzeBgddc9JQt4sA8Ybf4_OD8XuyicGXHkh2dvrALuDWupVz7knB-_qPaGBwh7SfUFYBmfMiNbbg2qeal3KcWXfaXivpvX1OIAfQ5rLNO2FXn4BFZGlQIdSK-cjwLOJ34LZ-eNFmewTfiSdzCYK5ruKxOh-uls0c0X2AnCOPqFsmgvL6u2RKv4klkZUcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=IgfcUDun-mBmd60dJ-691qHgM8LEt45oysFveBtMOrfhslATTOa3AqPod5gKMOHC3nJGdMeiMwMYjGdUU39pcmxDGXWIQxRKg0o7Yfg2TkJKZ0kLvcduN4nCroagAUOz8tT9IQciQZdghcolwpS5QeZeoJlTBhuX6Y30kok-GtCckSTECKABU01sFGFI3Uo7z-jg3QC_vSiLvqhUSAJ6Y88HJMlZ3exkkqnpQBVv-MKCUzduUgpsGpoD6fV3SsLCq8CS2y4geGdBAQKjfFb0dVHbS68ZoktjY7g0odx5BsJRpKqvUU8PckNdx8vVUDt0k6MeGVCOTF74DkE4q-UjvJif6m1gKVY-Rymy3IlqO_HgfaqjhoN2GFGhESI63_PWnqZgIM4bqCzDiZRD-3jHLcfa-tj_lHiISNk9RkMnYbylxPRYLcA_W_a6LVg9Ejxk4wUNQhWR-8McnrMM-Wgpjt--5q8xL6RLZXrgY-YK-eggdMIPzeBgddc9JQt4sA8Ybf4_OD8XuyicGXHkh2dvrALuDWupVz7knB-_qPaGBwh7SfUFYBmfMiNbbg2qeal3KcWXfaXivpvX1OIAfQ5rLNO2FXn4BFZGlQIdSK-cjwLOJ34LZ-eNFmewTfiSdzCYK5ruKxOh-uls0c0X2AnCOPqFsmgvL6u2RKv4klkZUcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=lPYCvztR21fy4mJaDpYc4qmFsPt2OMXXIXrYgAVVGqZ3FnsSZmPU52UflXwVRY-sKOdHJuFHrar7z44d0QM_p_hZYsieb_Lni-uSomYffqkQj81vz5xFLHCMopbSxkEzAPqsjl8MtlMe_IXDfpWeaKbpv3PiifubHcjtRpDmYk9ylX8OxNQxbgAkI9s1TnwWqsl6WJAWo4CKHZqt-_9SxN81dEkejQ9siTMU0f6WKovKye2theipZUxLXAYn5wU1WbH94wKowpulREz0ZPObA97ucAwjgmA9-VdJ7mfeBkrlwM0itvHvgrk-137EDa1DS9PEg6CnGd3ds-i0PLDUwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=lPYCvztR21fy4mJaDpYc4qmFsPt2OMXXIXrYgAVVGqZ3FnsSZmPU52UflXwVRY-sKOdHJuFHrar7z44d0QM_p_hZYsieb_Lni-uSomYffqkQj81vz5xFLHCMopbSxkEzAPqsjl8MtlMe_IXDfpWeaKbpv3PiifubHcjtRpDmYk9ylX8OxNQxbgAkI9s1TnwWqsl6WJAWo4CKHZqt-_9SxN81dEkejQ9siTMU0f6WKovKye2theipZUxLXAYn5wU1WbH94wKowpulREz0ZPObA97ucAwjgmA9-VdJ7mfeBkrlwM0itvHvgrk-137EDa1DS9PEg6CnGd3ds-i0PLDUwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ujBu2nUsrYj81swu8lClnIs5GtiM7Qx2s6FBHTOilPShziOLZe5W86cth__RKZFq-EMMBoqselMzy213cwFKswcz6DKC-EW4wS1Uq3MqpxbeJTMhPklvq2xyq2WQucXK5P0pXxcqpUpgjji_iq2daw3i8e5lPMbK7S9Y27Osg5qGi4RVQtFAukWkkE-iiHn-rA_tVRf7Aw9wNh00Ruf8e5mbSQygX96VNqW_N9-WIHVtbMdkNpqSMPcnHw3ReGHnLCOn5BHSWbQavoC3J2ru1M-NgQ2RIZGzMkYuZPbDG6ESKFjqxgjHfXNCQQTQDYS7KFtXDomLhyDJrFi4Zx6ZCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ujBu2nUsrYj81swu8lClnIs5GtiM7Qx2s6FBHTOilPShziOLZe5W86cth__RKZFq-EMMBoqselMzy213cwFKswcz6DKC-EW4wS1Uq3MqpxbeJTMhPklvq2xyq2WQucXK5P0pXxcqpUpgjji_iq2daw3i8e5lPMbK7S9Y27Osg5qGi4RVQtFAukWkkE-iiHn-rA_tVRf7Aw9wNh00Ruf8e5mbSQygX96VNqW_N9-WIHVtbMdkNpqSMPcnHw3ReGHnLCOn5BHSWbQavoC3J2ru1M-NgQ2RIZGzMkYuZPbDG6ESKFjqxgjHfXNCQQTQDYS7KFtXDomLhyDJrFi4Zx6ZCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=aAPd-ypLuzIjdguQKgSwqFUXMS9QmDQi603PK4IIq2FxLueMm0Jihx2DuegAeCqAiF6B8xTMsqk_0G3hRlyLrsvFEJyDstvzk2z8DUWoj3b-chfhEls_PG4Lg-yapuwDm0vZbNxNcgM2TV4TSxoxsz5Heliyp-2aA4gSbZbo96d5Q72Wz3ooos0gSu7SgKWebHsJtBwtqKzHKYgmhDNcUXAXlBfbBT5DyhCqy3VHiCiVKNSdTu9XHzBwoVZW9VQDH3uY5_72qxZfb0hEAPvrEx5VCxHBcYVCbkrl0orZF2TAWuO9iQwT9vRIV5ihFJomroapdE1r2W_x6wNdVAoUmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=aAPd-ypLuzIjdguQKgSwqFUXMS9QmDQi603PK4IIq2FxLueMm0Jihx2DuegAeCqAiF6B8xTMsqk_0G3hRlyLrsvFEJyDstvzk2z8DUWoj3b-chfhEls_PG4Lg-yapuwDm0vZbNxNcgM2TV4TSxoxsz5Heliyp-2aA4gSbZbo96d5Q72Wz3ooos0gSu7SgKWebHsJtBwtqKzHKYgmhDNcUXAXlBfbBT5DyhCqy3VHiCiVKNSdTu9XHzBwoVZW9VQDH3uY5_72qxZfb0hEAPvrEx5VCxHBcYVCbkrl0orZF2TAWuO9iQwT9vRIV5ihFJomroapdE1r2W_x6wNdVAoUmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=a5ct8jQ4fpeyNR_v3HNtyKQG45XY6MTjcE6JLR4RBzX6fNqO7rJrvKG1NSn3nI923obIvczqS6OIYHgSj3ZOhntG3RmZWASNO-f7Kbut-Yf1RHLeQFxesmhncEopqx372Lw0Po5MpugAwPdZnzkmAeVzXAooTGUVVRUdaBfwe-eFoSG7Uin53GqQ4qwFbe6w2ukglc3zwfxBwqN9hwBSU0JG50XqSrPKpPu2ScnxTwFI2ealXHd-mrbBrh4UMwzZzCXzyKceLK1WqL1_OwZbI3QmIElJ0lJL74JbkHKm7pITNjo43F1U2ek_h61s8kU-iezEVWwn_OXD4iXH0z2RmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=a5ct8jQ4fpeyNR_v3HNtyKQG45XY6MTjcE6JLR4RBzX6fNqO7rJrvKG1NSn3nI923obIvczqS6OIYHgSj3ZOhntG3RmZWASNO-f7Kbut-Yf1RHLeQFxesmhncEopqx372Lw0Po5MpugAwPdZnzkmAeVzXAooTGUVVRUdaBfwe-eFoSG7Uin53GqQ4qwFbe6w2ukglc3zwfxBwqN9hwBSU0JG50XqSrPKpPu2ScnxTwFI2ealXHd-mrbBrh4UMwzZzCXzyKceLK1WqL1_OwZbI3QmIElJ0lJL74JbkHKm7pITNjo43F1U2ek_h61s8kU-iezEVWwn_OXD4iXH0z2RmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=rRFISmwuww6HIH9CjqMx1j0m_ySTDVl7JtxOYxL1VlRzBLBpLsoijxOKj5Q8T8VfvHhlcEDItTZsn1UDu6Y5JRXy6N2a_fe5LB0z5UWs9AzBzB9geJE3xvd_LRyjHW9wcHF05clQ0WBfP8Bs6YkwjsFhh_eyGXOa-iwmfr7mLQZ3xUda9Wcvgh0fF6Jt8Lz68WohxlqBbEJuupuLD0zglJDdPT-ZTM79mMIE6HoSM3d51kIMqy4yDYZk9uBNedreQlE948DQbkbmLgcQvu1TrmZ5uG9DSrlyGbJ6q7JWWxP5yR3hV06ihDrBfUpIyxqndYwmf01TCBwShcTtZ-6DVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=rRFISmwuww6HIH9CjqMx1j0m_ySTDVl7JtxOYxL1VlRzBLBpLsoijxOKj5Q8T8VfvHhlcEDItTZsn1UDu6Y5JRXy6N2a_fe5LB0z5UWs9AzBzB9geJE3xvd_LRyjHW9wcHF05clQ0WBfP8Bs6YkwjsFhh_eyGXOa-iwmfr7mLQZ3xUda9Wcvgh0fF6Jt8Lz68WohxlqBbEJuupuLD0zglJDdPT-ZTM79mMIE6HoSM3d51kIMqy4yDYZk9uBNedreQlE948DQbkbmLgcQvu1TrmZ5uG9DSrlyGbJ6q7JWWxP5yR3hV06ihDrBfUpIyxqndYwmf01TCBwShcTtZ-6DVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=LQHvrMyncJdj2VE5IOx8VWRXLjPWnt-_ph673hpLlnuH8Lo1jy_3DwHBJQR-pMxeykBtDG-JIfEomlRkJQdJoYAgWRwLjE_USLN_vY1FKoPg2psLyvCSCBa9pi9vUeBNCcylkvblMkoj2QYoHrMCoCWZpOt2kuYlKlzbEVOfEIhJKej324NgV0vho4B0s7gqAv77hP0pePZde4IQ-JAVNMy7AzHXzJjLAeaKyuRFjIdySRSXisYqa4NPjyuBYR_aMVDGhEBWKXSX1r9YQA-_J1C_vc6OAzvKfkgd58O4SoqfL3DAj6KZDg3wXBR9NaqmfSJ1WuvUBt7aEshg8jgYYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=LQHvrMyncJdj2VE5IOx8VWRXLjPWnt-_ph673hpLlnuH8Lo1jy_3DwHBJQR-pMxeykBtDG-JIfEomlRkJQdJoYAgWRwLjE_USLN_vY1FKoPg2psLyvCSCBa9pi9vUeBNCcylkvblMkoj2QYoHrMCoCWZpOt2kuYlKlzbEVOfEIhJKej324NgV0vho4B0s7gqAv77hP0pePZde4IQ-JAVNMy7AzHXzJjLAeaKyuRFjIdySRSXisYqa4NPjyuBYR_aMVDGhEBWKXSX1r9YQA-_J1C_vc6OAzvKfkgd58O4SoqfL3DAj6KZDg3wXBR9NaqmfSJ1WuvUBt7aEshg8jgYYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=lpIdvFIoNeXTZhdwsZ4JUEWiqSuDlwdGjiuWAee-Qb4cYw0j4J723RM-IbKX7zutpsUNz8lBbLnEELLhQwDpdKIjzK2f-NZo2dAoNpd5sJjShX_R0-2qj3dnqJ2YNhsXpaCN3BBhrj8v4O4Mij9QjUwHn1-MIUVXotgTL1Ru9Oe8GQIw4Q-3B7bAV2A9EPHg3sW3i4m6KP73EGPIBk__UMPzGpiZ_NrJpf8i9l5ZjIdtpcKS3lAn6Am-H_xtoYdPlwPwvf6RMjj_P2n_T9Yo--nj9yI9VEIXUAektQeXaaUL3JCQtu5fG1OI5BiEkOxKRgK2lbl3icJ70S2eNAXB_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=lpIdvFIoNeXTZhdwsZ4JUEWiqSuDlwdGjiuWAee-Qb4cYw0j4J723RM-IbKX7zutpsUNz8lBbLnEELLhQwDpdKIjzK2f-NZo2dAoNpd5sJjShX_R0-2qj3dnqJ2YNhsXpaCN3BBhrj8v4O4Mij9QjUwHn1-MIUVXotgTL1Ru9Oe8GQIw4Q-3B7bAV2A9EPHg3sW3i4m6KP73EGPIBk__UMPzGpiZ_NrJpf8i9l5ZjIdtpcKS3lAn6Am-H_xtoYdPlwPwvf6RMjj_P2n_T9Yo--nj9yI9VEIXUAektQeXaaUL3JCQtu5fG1OI5BiEkOxKRgK2lbl3icJ70S2eNAXB_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzXvyUuj3SnwJVk39GNAJ9AVftlN9-NA630epm6EQj4jPiF1aM4kc6Ll2uxAf8pAWK4OrFOICNYR9uOR2m0762yCrsfDrn6M96-XGTY7WTmKjjhID0yxGw__BbK2qkZIXRRi9YpY7_3_DfqfY5tluqkHFNpbXYLpRrCJz0WvIZa4-GrUIuh157qQd_41M81J2lbvxBMj3Bd1Q1bdGqnYnHsVRb0Qmn7vh93bqwZH6Jcy1yB9KxfD8Mf-26U1NjOjCcJIaKX0Z8dwRLTkMmX_GJZFistplLls3-kEt4hFXuZhUEyKp1A32UNFRttKpAPAzy3DTYmNDwMPmIYmr5gShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Oj6YtTRQIRAJOblyoRJNx0L6PTCynYqXWwvBshs_5Kf-s0MEjsVJfBMV3oAn0hcHAdX8V7lxGCycYpD45nkdIiKkzDRp3aRwVj3b5HxAvB-imwyFSJK-GJIO9ETS_k-091cMX6GthbhYceAep6AMTx1aObUmH4zQWl1pUVr6uzShpwSIvNaroZBfWJ9RxWW_xh6uPFpedYMDdyC8QT_aPHr0geoQopGNaJMoi6eeoAPcL9h54j6lUBSITeqwBj7e2V9Mt0tLsvZjpn4TS1XibKXVI7PcsbjCWq2bXgNpqCLcQZylDaIzb3PnbFCfb83l-mJ83s-TzzQUihLzKFAk3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Oj6YtTRQIRAJOblyoRJNx0L6PTCynYqXWwvBshs_5Kf-s0MEjsVJfBMV3oAn0hcHAdX8V7lxGCycYpD45nkdIiKkzDRp3aRwVj3b5HxAvB-imwyFSJK-GJIO9ETS_k-091cMX6GthbhYceAep6AMTx1aObUmH4zQWl1pUVr6uzShpwSIvNaroZBfWJ9RxWW_xh6uPFpedYMDdyC8QT_aPHr0geoQopGNaJMoi6eeoAPcL9h54j6lUBSITeqwBj7e2V9Mt0tLsvZjpn4TS1XibKXVI7PcsbjCWq2bXgNpqCLcQZylDaIzb3PnbFCfb83l-mJ83s-TzzQUihLzKFAk3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=D4eMmcO2XTEQJ8c6XjTchA0s2VJ59_9u1f5rdMvLC_aDlul_MOAS8Jyyuu-f_9AHKSdesVWZ8DcRN8I71MGjYttaRPH6qTmr7A1J8YGI7Q5z5BujY4Twki-3G3ISXg1vgBjegoZ8InGosyRT2J2ilWJVkvyVM7FLU7NWbONGu7HIVxR9qxsXxpjGE4n-np4QCANEfFB_qROigfRKhhYMUhkZHetXB46QTZkBUVLV2NV87RtvtqI_gzlVvh30bxpRTwkEzPMeNvTxhnB0IWF5nHbkLZNtRQutt6QK8Y7n7hP-u-Rq5olXas4LenKmvYfZsPVRMWN7tacecyuY1uhAZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=D4eMmcO2XTEQJ8c6XjTchA0s2VJ59_9u1f5rdMvLC_aDlul_MOAS8Jyyuu-f_9AHKSdesVWZ8DcRN8I71MGjYttaRPH6qTmr7A1J8YGI7Q5z5BujY4Twki-3G3ISXg1vgBjegoZ8InGosyRT2J2ilWJVkvyVM7FLU7NWbONGu7HIVxR9qxsXxpjGE4n-np4QCANEfFB_qROigfRKhhYMUhkZHetXB46QTZkBUVLV2NV87RtvtqI_gzlVvh30bxpRTwkEzPMeNvTxhnB0IWF5nHbkLZNtRQutt6QK8Y7n7hP-u-Rq5olXas4LenKmvYfZsPVRMWN7tacecyuY1uhAZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=ZxrfkkkduKSsDuTAFGhwpFk59cxtSazIk8yiLl9WFh2bNvemV4Kb98jDnA8oUSACI5vh59TBOAuJkz3Bk25z7Ln74ml1Pw1XMzC4sz5O2fJS_UvljL4H8lBkh5geg-8VDLPvqJL47v3iheZnK5yz8kzQV1c2PLB4UtLQbwCYSXvYNuJO5_BMhRUdXYY5L7bckF-on1nzYlc74-B7_I4nu4x17qbGBj273kSSpX1L2Q-rgoa7AzRdM880fXq3PiCIo3bDF_IwFniArM1EwHYwjyRKIDRDDmuM5btRwxaKrhuFyJRp9WxFxzA6fndVxZwcfUdiT857Qv3j7KaflQbALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=ZxrfkkkduKSsDuTAFGhwpFk59cxtSazIk8yiLl9WFh2bNvemV4Kb98jDnA8oUSACI5vh59TBOAuJkz3Bk25z7Ln74ml1Pw1XMzC4sz5O2fJS_UvljL4H8lBkh5geg-8VDLPvqJL47v3iheZnK5yz8kzQV1c2PLB4UtLQbwCYSXvYNuJO5_BMhRUdXYY5L7bckF-on1nzYlc74-B7_I4nu4x17qbGBj273kSSpX1L2Q-rgoa7AzRdM880fXq3PiCIo3bDF_IwFniArM1EwHYwjyRKIDRDDmuM5btRwxaKrhuFyJRp9WxFxzA6fndVxZwcfUdiT857Qv3j7KaflQbALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Najp2Fo2bAALT8DTnAQwbrbzmunsh1-6gsWN1A-7TlwJqlqA9vbfuAJjomlvmaaWAbG_aEFKrnLHx_D8nrodKx8nHyi-yNQo0E39UgxHodtG2p-XgrIyxe-9hX7AUxMerMKeeEvhlBpzRCKg-ukTbThPIX9UkbUa4pM3m1ydesctruOom0gYiXhfO7Ii1TSolMTnHfaonpF8s1f6wKbW7SYmMAPHxGtr7q6fxV5ZqcZvKeye5VmJanMwNTUVH79l5AYUsvGhLKUKEccpmF6FzkZI4F9K_Swv0ZGXwOPaNV__X_1P5kSR8dWxxvWOqaMF5ujPtHpkN_s0iuy8nhy5EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Najp2Fo2bAALT8DTnAQwbrbzmunsh1-6gsWN1A-7TlwJqlqA9vbfuAJjomlvmaaWAbG_aEFKrnLHx_D8nrodKx8nHyi-yNQo0E39UgxHodtG2p-XgrIyxe-9hX7AUxMerMKeeEvhlBpzRCKg-ukTbThPIX9UkbUa4pM3m1ydesctruOom0gYiXhfO7Ii1TSolMTnHfaonpF8s1f6wKbW7SYmMAPHxGtr7q6fxV5ZqcZvKeye5VmJanMwNTUVH79l5AYUsvGhLKUKEccpmF6FzkZI4F9K_Swv0ZGXwOPaNV__X_1P5kSR8dWxxvWOqaMF5ujPtHpkN_s0iuy8nhy5EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crtatb_4oEa43ZsgjBtRvF11PK6vcY-5-f4c8-fpe6uBtAXfGuBXeFfqJV5pG3ZOAtWaB7e8eIeo755Eu1rxpDAAeReAiWqCK-F2fgGvI4mQbQd-1K6epSdiNAqXkJl8-2mHvycIY5_4LUaBRMjG9TJPWv5sVo2mUQymR5eqaR4K4AtJzgUxWinSQhKRSHx4yadqTjNJSwIvx1QoxStw6MEwKXapSVe4DsN2JfOt8O0GAbOyeDUrLAfQl1k2f3xZDsgI4f4-wTCJM5B5T1AFL0-rcxj6c2BbNpYcjHLBf027DSXrHTaL7KV5MsH-9vb7cav6fy4C6KKOk0kjjafSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=WrNeNzfu3ASPWi4KqDbaMbvnyJP5ZbGUtqOwgHcJAydJS7_8cAWWPqnW7GT53vw-249j4dKsXUQqX8l7wSDOW7taLP3AU_3oCSVQuJjSYbMUMnLZFZKKKQrhknfJjmoqHkj_umn6UVZyGomLLRGWkTrv5azVLWLwgsJrkrxFF_JEFbPLQhfRoxzXao-burHDJJ8tS1sT3OnaCd6GNo4ufi8LXmk5kcdFfUR_3Sog-gG5Yie3E4hQlyeNoQXWUzkrsQB5nOoSlBAobChCI8FFvVkIn-Y4LQdPmrvxBnzGM_o3_0nyWly4P99LzqO0sHub5fjCMVApwD8lbPhj7JOtRTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=WrNeNzfu3ASPWi4KqDbaMbvnyJP5ZbGUtqOwgHcJAydJS7_8cAWWPqnW7GT53vw-249j4dKsXUQqX8l7wSDOW7taLP3AU_3oCSVQuJjSYbMUMnLZFZKKKQrhknfJjmoqHkj_umn6UVZyGomLLRGWkTrv5azVLWLwgsJrkrxFF_JEFbPLQhfRoxzXao-burHDJJ8tS1sT3OnaCd6GNo4ufi8LXmk5kcdFfUR_3Sog-gG5Yie3E4hQlyeNoQXWUzkrsQB5nOoSlBAobChCI8FFvVkIn-Y4LQdPmrvxBnzGM_o3_0nyWly4P99LzqO0sHub5fjCMVApwD8lbPhj7JOtRTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=lBQEMdgCvkAIVAsqOxWyScVwM425_O-cRM4COj1y4jZ42Nd_YEpy86Gb7D6DHEsE1f-hqEtiWbdjpLlh8DXmW0y5pxdlxSC4c8oekJfEL6zN7Rxc71Tto720kIaWe7s1xZXLmxwzWkLkfOYq9e_9bbr8DiYFKFZQMsJWAj5qjG7VeCRDCB45HJ7q9T5toEkoLTB4A5eXmA3Y2poO1rQ3T5DCZBQ41TdEoFyuDBdvzA-admcZLYpv8qwpr9YRPO3sNnpYBAVmNDLnI4v3q82mk98e80T1NzRKu79mcCXHY-RWS_jB4fs2I9Y1uPIMIj3EdQ7ceyVFYWrUbc36QepKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=lBQEMdgCvkAIVAsqOxWyScVwM425_O-cRM4COj1y4jZ42Nd_YEpy86Gb7D6DHEsE1f-hqEtiWbdjpLlh8DXmW0y5pxdlxSC4c8oekJfEL6zN7Rxc71Tto720kIaWe7s1xZXLmxwzWkLkfOYq9e_9bbr8DiYFKFZQMsJWAj5qjG7VeCRDCB45HJ7q9T5toEkoLTB4A5eXmA3Y2poO1rQ3T5DCZBQ41TdEoFyuDBdvzA-admcZLYpv8qwpr9YRPO3sNnpYBAVmNDLnI4v3q82mk98e80T1NzRKu79mcCXHY-RWS_jB4fs2I9Y1uPIMIj3EdQ7ceyVFYWrUbc36QepKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9NLuRg7l_fgVgvgRgBjAroQ6zArDiXiGvUOTHDGXJzIfjvdrYpfN6_WJIboVQajZZtq5Cus6r1Tye6IiPnTbkZojAsL3Z-WgL2_s0eUJxcY3iUuX0yL_5YPrQIpkuiybO5XlhGoCHgh5rDjJCHzWN-fYkYBGN3XApJ_7k3Fbl73Sfz3e6A0DDDpHxTkcqfshtvIKAQZhU1ol62xwWoU9rt8bgQYH3-YIc8tWeYxuvo5PVNmTSRwBukFHHPBBLh_JDKTgkQTet4Y0ZC3UGhZaDv55uHB-dg7bYLjOl_T236Rwh-rVGnrWeAjDdP-a83YWqR39hRRrQs50fnt7bgIPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzt-z-MDYD72x8JdrIcCspH9VqDInPYRL9D-SOaYMYpGGIADdlu97ntd9Rkt0m9OAWCEAcCHC3h2F-RNc4iBJzpiQMnjaBKWs3vq9NAMaOYA2U4w3gzPXchNAc8rnEGyZplYl_lQvJEhQUp4Xyciv232nmK0RHSSz9FSqjS0ERqrRcRhmgidYVVDhY8Q6FSuoOSHeYAPABlNho0s0QsM0Y_Ydd9E30KNunS7nZaYuUuOG61W7wxEzsOwgVbHStBCrd8mAMQwc5Ssewp6jAdSq3PaAgTEjzzFeCinJ4_r8LQQFTLPICOww_VgkdDGaJcnilHKlnn2WT83fxvpROsSbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Hn-9xAyzmGZlf0bSmo55EhkOXU6fIJ8Ef3PnYkWrUrEZSjn3K5Vh9t6maZm9UxJGyRNlskl8tysZkWc9DJ4J0oXE6TViVtvQr6TUxbI5FImQEFLI_tqxZyodfRmEQeGGwyRjG2F7XapZTo5_TthDJyaL-SP4fI-BIRcKcC5_DBqhnTkd-2abm0raEEJEqrIcNQNJ2iBPad711NwIjKgegRmapfMhkWDxAHABrwDBrxbZ9IHtE32hlMfuwkhozz7FIVcg00utsbDVjsQzobWSUuZUwh1MEywwEQHIgGVjaUwwD-wIME1hQHINQvBWnaoHfA6b73kU8VGIX9niWKlcHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Hn-9xAyzmGZlf0bSmo55EhkOXU6fIJ8Ef3PnYkWrUrEZSjn3K5Vh9t6maZm9UxJGyRNlskl8tysZkWc9DJ4J0oXE6TViVtvQr6TUxbI5FImQEFLI_tqxZyodfRmEQeGGwyRjG2F7XapZTo5_TthDJyaL-SP4fI-BIRcKcC5_DBqhnTkd-2abm0raEEJEqrIcNQNJ2iBPad711NwIjKgegRmapfMhkWDxAHABrwDBrxbZ9IHtE32hlMfuwkhozz7FIVcg00utsbDVjsQzobWSUuZUwh1MEywwEQHIgGVjaUwwD-wIME1hQHINQvBWnaoHfA6b73kU8VGIX9niWKlcHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ9Ly1KfLDbynq6bUWghC6g3onq-er8_rHhc3ClcPwqQFOGeRDc-pNAxNrPN2kvZ9VyXuMwVOKdpd2KCYQs-AWiLFQR_FVF1-pxU5LQDXtdCkJIWJJQXIS_l93MgjOOiO-sO-XAwyfO_NMeiTOfyEH-dl_14mjI7i_tBzfwYMWXif_dcuOrB7gAxF2QbO3vAL7ytInQ_ECuI81I-HZ-9COEWTYLC56LnMxURzE07Y4n4fbgfpXbExHOessqQSHRaCWf_LyYeSbp9mxpFzCrD_cKfBFXQQnPTvmGDPNKgBdFZuii6mF7nim3Lo_c-F3umPB14nU2iCM4ASgpX2zqJ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRC5_I37xUD2yfZMBMdJGS7vlQTKCpPtj0bCLfFAxpTXYi7TfU6YwViauwk18Z2g5ooKqQwjpxWS7g0tZMlNF4vTHSTnCv6YkQnWStI0kcqUigND7nQkNgXIrX0f64rYRu7ZVS6wj50ks6sABG8yPScXTm6J1YyuyLJP0tVDxtU_TPyTTUL-Ono6tSu6vWIkQ_jExlP3UGA5oECpH0epAW3n8IFHJMKOR214KETV1SWwbKmDiboWwMJ-MpCxz74l-FyOik4q_r6ylGaLdC1LVXYQbmvyvPtCEZbR3qsgxNoUpUH0SFNGTVTLH-_NHuUA_bGWuP2isCCKTlwwRycRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bV4LbeYYFgE5wWOJOLyx_vNUGfgPzgKFNdd0zwos30VjFoHPBaa1jPAoZkHSK8TR2MNaejU5TPEMVnx5sdh5XnAazQacROeV7kDra-U5a1KEc2T4q2lmROIJqgTlkptXJClUbcSqevXHHZ_jo_43gqld5yxIJxhBDl5n6wuFTQfWTX86iM8YOM-pcXyJYQF1ks2ikG3PdjBzPjGnY2ujSATc-S0-u3ClX8R7Jx2KfY7nLc4CR_T7k86nF19tjsu8Zk8WHrefUKwZWfzNjsz_H8DTplbZHOgDhVAmdaAyIl_CpySRMGzGziW_L2Qw1elbnfyKJu6I968ihwH8es2y_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=DpuJNCKJeJOBWcyMjwB-o9iFRj0gHaRRTTh3ha8O_mftDPYpBno44J_suaknB0Y2WlC2Zuw647qd39dxji6F1WHSDko5LAF-N0KSoRedjhqrULy0rp0lf1N0sauw0QvI7fWtbzWmIBqpuaPj2Ltbm2okxZJTKIOLBWriZcFcGRZk4B2Fv5WsVURXcLs4a66k4OcnzZ5YE3SZaJ7zCMVrHJyX9CYBLRXNTyEO4XymROWQRV0FSUpKrFQjXyM5pCAGELZSQQJQUNXhFMtzzoGCDFhnmGOSle13LJviaj5Rsko9mWkqD0CZp8jUjESSGjrsmehaJu2m7pqE6MJdjwSe6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=DpuJNCKJeJOBWcyMjwB-o9iFRj0gHaRRTTh3ha8O_mftDPYpBno44J_suaknB0Y2WlC2Zuw647qd39dxji6F1WHSDko5LAF-N0KSoRedjhqrULy0rp0lf1N0sauw0QvI7fWtbzWmIBqpuaPj2Ltbm2okxZJTKIOLBWriZcFcGRZk4B2Fv5WsVURXcLs4a66k4OcnzZ5YE3SZaJ7zCMVrHJyX9CYBLRXNTyEO4XymROWQRV0FSUpKrFQjXyM5pCAGELZSQQJQUNXhFMtzzoGCDFhnmGOSle13LJviaj5Rsko9mWkqD0CZp8jUjESSGjrsmehaJu2m7pqE6MJdjwSe6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=UKrUqUB8DTRZBTLizMR3X0lr4en3yBYUPwzojv14qdqqvhCpxT9sP9RojurnprpnA47YXqnU6qqHAL2mbOxaMRKPbd0ZEkHrQIqGd271YUMKUVGIz4pUQ4DeM_5zzet2XJmLSqVFNKIVba7-oWIqmkkfKRNY0niSy2pCRKJ7varFyIrqixXYdcGPgR1_oX6GhYdT-MoWRpL2wV9JskQqdYZV_eEMC8EXGYKSme3q_ojw5UJZyjECecCItEpYE2Bwm2t3GvcVr21ksoyAh6W8tQwfA7ELs0VdiGwiHHclJMBfO8RkADWAjqLLGuToBnPt5sTtkFbHa_IIl8uOOhm6qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=UKrUqUB8DTRZBTLizMR3X0lr4en3yBYUPwzojv14qdqqvhCpxT9sP9RojurnprpnA47YXqnU6qqHAL2mbOxaMRKPbd0ZEkHrQIqGd271YUMKUVGIz4pUQ4DeM_5zzet2XJmLSqVFNKIVba7-oWIqmkkfKRNY0niSy2pCRKJ7varFyIrqixXYdcGPgR1_oX6GhYdT-MoWRpL2wV9JskQqdYZV_eEMC8EXGYKSme3q_ojw5UJZyjECecCItEpYE2Bwm2t3GvcVr21ksoyAh6W8tQwfA7ELs0VdiGwiHHclJMBfO8RkADWAjqLLGuToBnPt5sTtkFbHa_IIl8uOOhm6qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Sbne61g4awETnNRlPj3Di-1VHYIgSndo8YzrDGgVT_1ix7XDbNr6rZOIudqH-Rb65v7x60TdrkOo7GNr-mTZO7sVyCETZ6GV2yjH7msodkiPEcWgxCtJa3MqNW-7Wel4wP9xLRd7IVXNMdpdmnqLL4w76zMxKjbWnTSGZnUps3xUuN8eV4oInxnobm-44I1warFDT5whFWNNDNzf-QnoxEeQkDrHT0iySEq_3BoXm2W0Id2ZhJcTNTUy5AO_VGMDVmQPx7ZzgQ0xbpw7dflbjEIwqdqEqV_KQlOOfy9rNHPOyGhZXx1NfH1JrnRGkY3BI9zafpjcDfEkWJnYHZNdCRqtpN-IznLfRMhD_22lMESrqWsJ7m07DgapymDgYwFFiYDuNRhdSqlhIWhJ9bCYwiHcm7xP4Fra7pnxbNhhsCQAU4N_nlqyZd_ljuk4OnN6qkaTuLLifTA5ZPfIIb0CDwnSykZGSQ1I4rKY7nUYEdIGctbTx_pD3HarNkh4QW841r4HrN9zsOdxIy0PJqDuCIW0MdCeAoLQ-CFQzZ1PPyzFpNdmwl9ocomoquburSsfbcIa3usC58F8eCCJOM1nP1LGw5SCMfISk7d44GiJ8EXVnyM0d37tGHe5y13SL-rxenxty_ianq_APtdGLSg8DCtR4gzw3V3Bd4ZNJw5cWMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Sbne61g4awETnNRlPj3Di-1VHYIgSndo8YzrDGgVT_1ix7XDbNr6rZOIudqH-Rb65v7x60TdrkOo7GNr-mTZO7sVyCETZ6GV2yjH7msodkiPEcWgxCtJa3MqNW-7Wel4wP9xLRd7IVXNMdpdmnqLL4w76zMxKjbWnTSGZnUps3xUuN8eV4oInxnobm-44I1warFDT5whFWNNDNzf-QnoxEeQkDrHT0iySEq_3BoXm2W0Id2ZhJcTNTUy5AO_VGMDVmQPx7ZzgQ0xbpw7dflbjEIwqdqEqV_KQlOOfy9rNHPOyGhZXx1NfH1JrnRGkY3BI9zafpjcDfEkWJnYHZNdCRqtpN-IznLfRMhD_22lMESrqWsJ7m07DgapymDgYwFFiYDuNRhdSqlhIWhJ9bCYwiHcm7xP4Fra7pnxbNhhsCQAU4N_nlqyZd_ljuk4OnN6qkaTuLLifTA5ZPfIIb0CDwnSykZGSQ1I4rKY7nUYEdIGctbTx_pD3HarNkh4QW841r4HrN9zsOdxIy0PJqDuCIW0MdCeAoLQ-CFQzZ1PPyzFpNdmwl9ocomoquburSsfbcIa3usC58F8eCCJOM1nP1LGw5SCMfISk7d44GiJ8EXVnyM0d37tGHe5y13SL-rxenxty_ianq_APtdGLSg8DCtR4gzw3V3Bd4ZNJw5cWMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=UBV4lf0X8tUrIVFkzkb7uY6R9XWH8ynnSAqpEgbylC6_uiaZKqvEMmz3siHxmPGqdoWy5lyBOLfNcWyyRYBV1qDQyprXwxHnqLI9rNy2ZRKoNLe8unAhYYca-JjKQg9sF1xKNKypM5UzoclZ0tfi2ZNnDjpgFK5ZEcv1XD4S2Yh7fw3zUgEiB0SAG4o49KEuhO43ch4KOqEg7P7byITSZm5jNB_9cU1oyj9DOH-HsmT0MER2DBhdumOXV9N2eDaaloR7jroWiGuf64aLUAdcu3VxDxphcyNMjDXMO8c5nJL1cyTnSWDC1Q3KTDwRBaor3N0qBjoj1Rk_bds7ai1Dp7AZW_m5LHqd2mEWoAV6Y9AWUzevL-W6Mj4iLQdUvh10NOKo4fsDut7IArHbEr4Wnv7dkMukuW09X3SpRc7ofY6tkOfq-1Qc1_1WBAquVcjw7uMyiD7MDs17JQEk7pcPmD7PkH-R1MQP62Bqrb67zUpUlFGmJKLxbWHvx70bjyRpX3t8CfnimW047J4dF8jbm1d0c2RZe1vaj40eO8d5Il4drrXL-yMSJxlB62uD12UKDsugkre_JWtu4glC9mD3yAEBFjPL8N0SJZLDWzgPYaG9cWbgdIkV0sz6JVj7uRxVOi3SoWe6eSO12t6Pq_rntTNalNBO8ayhbnsDzSuaQaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=UBV4lf0X8tUrIVFkzkb7uY6R9XWH8ynnSAqpEgbylC6_uiaZKqvEMmz3siHxmPGqdoWy5lyBOLfNcWyyRYBV1qDQyprXwxHnqLI9rNy2ZRKoNLe8unAhYYca-JjKQg9sF1xKNKypM5UzoclZ0tfi2ZNnDjpgFK5ZEcv1XD4S2Yh7fw3zUgEiB0SAG4o49KEuhO43ch4KOqEg7P7byITSZm5jNB_9cU1oyj9DOH-HsmT0MER2DBhdumOXV9N2eDaaloR7jroWiGuf64aLUAdcu3VxDxphcyNMjDXMO8c5nJL1cyTnSWDC1Q3KTDwRBaor3N0qBjoj1Rk_bds7ai1Dp7AZW_m5LHqd2mEWoAV6Y9AWUzevL-W6Mj4iLQdUvh10NOKo4fsDut7IArHbEr4Wnv7dkMukuW09X3SpRc7ofY6tkOfq-1Qc1_1WBAquVcjw7uMyiD7MDs17JQEk7pcPmD7PkH-R1MQP62Bqrb67zUpUlFGmJKLxbWHvx70bjyRpX3t8CfnimW047J4dF8jbm1d0c2RZe1vaj40eO8d5Il4drrXL-yMSJxlB62uD12UKDsugkre_JWtu4glC9mD3yAEBFjPL8N0SJZLDWzgPYaG9cWbgdIkV0sz6JVj7uRxVOi3SoWe6eSO12t6Pq_rntTNalNBO8ayhbnsDzSuaQaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=hYt904pUs67evlvyn7BJBdLV9D-Y4RFT9rYnifcK5USs7JTIDNfKp05Yw89ao9K9PnCkIz7upE9RmBeH0Ek91frcmFpR19onKvrnPb0lug8hLO5e3FoT3aoukj49u084U2bGooIopXmqicoRm3tIZ6dxXoVlncvAen8DO-nrjrTZAhstgQ69MMDD6j_V1o853nuM6k4SFOLxEJf-6J_OfXpLpxymkNqFlfmDP_BQcKuSrZlne5zLm5JaLpXjtk3sUKfslqSDIT1DHQLZRmqa5nEFbC_2Sm9eOp6S98gZNNDQPNGujkNPXJBp3K10uPdj0yvyR_gRMheqCj5iiM7yVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=hYt904pUs67evlvyn7BJBdLV9D-Y4RFT9rYnifcK5USs7JTIDNfKp05Yw89ao9K9PnCkIz7upE9RmBeH0Ek91frcmFpR19onKvrnPb0lug8hLO5e3FoT3aoukj49u084U2bGooIopXmqicoRm3tIZ6dxXoVlncvAen8DO-nrjrTZAhstgQ69MMDD6j_V1o853nuM6k4SFOLxEJf-6J_OfXpLpxymkNqFlfmDP_BQcKuSrZlne5zLm5JaLpXjtk3sUKfslqSDIT1DHQLZRmqa5nEFbC_2Sm9eOp6S98gZNNDQPNGujkNPXJBp3K10uPdj0yvyR_gRMheqCj5iiM7yVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayasLU4hPP14E7DmBLdBFJYvuhuUfiWBqmyc9xih40czeAKwNRTwocZrVoy0iog9nW9JCQTNO_NZ0e3vgCxeB-9fGa6pC9i4y5Jk5n6ZPCEeHgYD_CzFS8s7KQZKbhqU4ocunGenN5NFZbZL8aXrvqLWzk_nj8xHlT9EaE6WPk4-FK7-a-tmqD81n2nFNRzVczrR9anWI8-3YpJrzqn4cjFYq08o-r-mO0vAXgqLIwUavSoL42MFuDhk6QHxbYiDIPOSH7vQcswF3uKNyP1it-8FYIr7le_4sIr2SWXeIWDDyJa-G8lBgT9QDYaMq-IxT2J12ChNOJzEEXj41gkJ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=O5naSLpaE9mtNZwnozm4tymRtKvs6g0LmWc2NuTwv4_Js4PTPEDiSzaOcLCpGFTydlhAlad4jeQm4tI_YbAwoHI1UrRo9IZ04zNqrJKo6xZWxEsyCUXX0sY-qtzyKcddWNtWnW83yewSZLHq8V4uP7WQWHr6zUnJENIjmSNPTeggHiirI-z68B7WnX-yB1GqRRXilm4HxUpk4aExyV4YLCBDihG_avyWTE51OMlZCwwPQht_zonME5mBtw58oRsNA8-ofF6XQ0P98rex8oRVm9isIEkugLxjfc08JNjEpXH5XhyJVDSXa7-JzROcC3UUu-xVQC1gFwqHt0M9Cy6hZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=O5naSLpaE9mtNZwnozm4tymRtKvs6g0LmWc2NuTwv4_Js4PTPEDiSzaOcLCpGFTydlhAlad4jeQm4tI_YbAwoHI1UrRo9IZ04zNqrJKo6xZWxEsyCUXX0sY-qtzyKcddWNtWnW83yewSZLHq8V4uP7WQWHr6zUnJENIjmSNPTeggHiirI-z68B7WnX-yB1GqRRXilm4HxUpk4aExyV4YLCBDihG_avyWTE51OMlZCwwPQht_zonME5mBtw58oRsNA8-ofF6XQ0P98rex8oRVm9isIEkugLxjfc08JNjEpXH5XhyJVDSXa7-JzROcC3UUu-xVQC1gFwqHt0M9Cy6hZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=PCrantrXYnq9K4GUjn9_m6DcQfiaHil5o1iXcKtfW_G6eilByK7nyLrapiimXBrtAsaheGAVHfp7Yf72AFywEkL5uzhpWVy8lxUI6rcWFBfY2kBPvA5SDcFOvBP7cqv9suwZ-ZFG2k6n2Fc8FqKdSlabEm1KonVDtfaIIfIhl24Hvi_xu552wnhw3VoFxzTBqOyH-SqQ82DCOjvVVY5T_bwjPfgKETzSPd9yZSIgS3GO8Ram_oK90v9d-6FS_MqIKWRYX1tUuT-7EdJfgJRd58MAD-uvInQeExUy03WXOASMk6BhjmSv0JcTRIFcToXWtrcKfCEqw75VxbCusVRAXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=PCrantrXYnq9K4GUjn9_m6DcQfiaHil5o1iXcKtfW_G6eilByK7nyLrapiimXBrtAsaheGAVHfp7Yf72AFywEkL5uzhpWVy8lxUI6rcWFBfY2kBPvA5SDcFOvBP7cqv9suwZ-ZFG2k6n2Fc8FqKdSlabEm1KonVDtfaIIfIhl24Hvi_xu552wnhw3VoFxzTBqOyH-SqQ82DCOjvVVY5T_bwjPfgKETzSPd9yZSIgS3GO8Ram_oK90v9d-6FS_MqIKWRYX1tUuT-7EdJfgJRd58MAD-uvInQeExUy03WXOASMk6BhjmSv0JcTRIFcToXWtrcKfCEqw75VxbCusVRAXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0jmUDti1jw9Fe9O3hoxuWgTgBqEFsL_-IamG62_MVAUIBqsIiTGf_-R5EdT5OfwVvmBNn6LuUxQw2vv-YqSqUFlYJrwKlUnd0l27Db7mj-26c8jWbrKxHtLDo3PloPMm_au6VFAicY6Uqir9zaLZBTpdkMxosI80LT3Yb2PNdYQ1mhOFmSiuU903T346iQEuW7_ezY-M3wWm2dcfACQGRqrgKOq4a0pAHg4nPfa6Tl6J9Xt2JlBY0o4YTgJkw1QYBQaN8IKiOHaHTd6s-zxG7-d5b9G_iSW0PdQN_3Slx-Vpfj5rqw-4j_66t5regFbdhbGoNz_30-UZxjUWCCU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTMpOLt5W2XhYV6_7vCld_CxCZStTchzWnKoOQFgzjWQvYbEvfhXlDOKFIrBbNjShH1Dwya9tNH_rNmhfRSof5G-_bOR7O0t0LgNKc3O7jwHVOsW-v3tEA4QxD5iDsLcjaXwdBv21r2GG-4UMrBoy2yLkaYB2vnQAXZZTPjS9jpKdxet_olPwxmv51RFY6h3cRMYg21FWkIz6dnTU7oVtcsQdD6bK6hEvla15lbIY7wXvPmWxXL3b01T9enAR_xi7StLVv-BA9INQ6j3B_1GtIQggxxG6K1n-tuueqdv1hHDDucn4TRyRVpaXzcxXTiWC1yKUPYqtV3Gdf1dc6L1nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UthdNr4OO-MKjJQplIQtoq22X28bDDa3UQbCqycTvZIuShxz3oDrgfngp5XBPNXTdgAR-DUjuvDbR97cli6nbm7WWFd4G-OxK-ZsiU1ADLdpa7XVqh1T4F6c27YS8XMGd_O-uAoNq3KCgh1aJFuoOY4VCg0obmTMjByZMLTg741CgYC6Oks9s_mL9QtBRj61o24ieMJYbYiMZrkxLY5xlTRDWWx4ce7eyQmy5BZQV54T24EzrGUgVOGSPKtxo5gj4Po_q7-TzKGMFjhiSY0Lve4gSI_Sxiv5ibjkKSLYBYH04zn6tOBbkwWE44lbnfjtWiWR2Z33EOothhh7pjfU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QW4MbT2M57kiYKYeVCTzsPcoMQZGsIXadwBQpRHne8NphcKuDG8Z9kL8SExFCdexn4Lb2Q6qr-SE1WBLHhXuHYA8L1MC3xNcvS_SHqpvTvp_59_N4Arvdek7OHMts0Mc7-fX1LzBHAsNI8L2sDwDIDMf0krRqCxeKyUP-bOLA37gaAE8vNWeOND7mv5yuibld4ipYQv9ZhCSWWeEONm7aNFhAl47RJnCdc8B3hayl2kzS4TbhlrSKPcKRaCk7uHwNrZ7n406hQsmoINBK7d-0CXwhHUOr45Hkfo1XgPNaFaG10iMzJhmkLVxHOB7GqGf9YUQpeEje7goX2b73EiKVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzmKO5ymgn4Rt6RRhfHX8uiV4oVpymfy_bznlqLlwRioMdcJmoxSJ1NQHgsPGIEJY3XykxdIUyh_6jI6q-m1T1s93lTCGFwzyp96s4aBxCNeFEYc2MSujGwxi6JoV6yGct_Ys7s6andLQQkk15mcOP9YDUvN_1qdiIaqFyfklPtWfTUjmNB45Y9_01_ljR4ovcAywBXn3XwFa7M-khP7V7S5HC-hXplIuZARGq5MxQCIM0gOQFSAt8leGHUr2PTSz8Q-LawACgCi7vRCmjWy3mBst2bEqOeQ059ZJxYbgHKRJ0bEV4mzGucPX6axsHuyqEAGfYkWbnqhQc3fXIEKNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIUVe2hSwfFabB2RKFQlxCdnQ9ytbddgvLFDKXvH3vqWhQ75N5U0x5_plwkZq47BT8nP5Ka5eNO1Oi5DcJPOaAIAo63aRDB39e-kIhxR5yOgrdDt9l4OksV4YIRDRLCZ2B1jqmAERf_ECzuoYLWukUN_Pg--GqkmelAK72iP8jw28Bp9ehBhz8Uh6ltZlElk4HyUc54E7rZCyPOqAeCnCevlKek9OuaY12_p6d2mlAVFoIjR-5RILr_dfsTdsKAxH6YwKhjXJpucS18KchT5G6_7kugfAr2OeN27MtNF9cxVkwf2G2f-xEjJyDGe1cu_bhzua04vRdv_VEHQdJWPYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdmLJPVatroDjAp65FC8rlhO15IK1XA4j_laeL8V7DrqYhnz1a9wgoGvO9VpBKuvAO-f-l-gwYtLd1zBNY3AMUGbOOYcI-RL7XaOa5nIDGt2gftc4KkyYXSMiRg3cP4ohS9y5PCN8_wTP8XWp4NfC7EuxDni11QqUFb9tfd6pxM4YchT4LJERrZmN0XOV-mRGlX1gDDF4VYQHyRF3JeBWT7KJMEtN36QBBE_zOxR9qfp06rspFrAA_0Eno8x6NqAntWPzFaQmAjMB34MuLP7dSu417kIZ5KcuO8jiwJ2GDvoyY04UyTz0yYdE4GGRVFk206g-42G2tt0Q5DMtk_9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOrGv9TVidIez6Su00h1qCBN_C48Q8DJflj-zt3_jHWtg8MK5kh-wKcw-H8Xpe3L37c9Mf3EyVLmLhA-f9fjW9Nq4xNMAcgHokD9VsbzWYbQIJKzxjRhza_H8Lp1-RzCFJvJklosVXMBw6u_qc0BXBOjxQmqGJK9d-GLfYqfVyTDpY6wbEC1LgKi1s9jFRaumyb5YhSPiEwsmQezqsETh5rZZkQNKL1tdb3FjMr9s8xrpVYn9EE_g44AuT4tpELJjDgZtqu7YR5V5R4a4vAqbsQR3jlQX8IV49I13jBFDur03I8bFh-MsTBfKz6AAFZfTiP270ir5po5Z2E8Qe2RBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKhrnT0aEYpeMuEIzRs73ac3uHNXzzfdawtG4d69ZL4rR9kFjm-BqLeP7jpbSr8MgEp8Es7E4FeFxwZtUFjtd73C9B4Ib5hdI3HCH6wWvvb66VdmefTyir9Ed7Yxk4DCqFocYZjZOa_FPgbzeee7WDt2nn3Ljrg04KUZD6ivlq1Kd-keiI3W6EpaTORqXgLKg6lVWIpskncb82qNKNeronxySQ_d99mIkBbO4UQh4oF7KhZYZXGo0YeSAEdsdPGjG0eAS0UG8BvcHLSc6QorGgTDGLh21NKgVoearyX7fKggmWI3XpjU_y5HDyyHPnmdxW5nM3eLPbdS9aONuxF0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPBbgHgdRtJo6Q2YO9N7X2XI2gaZACi4R24AdsezKpDzIPpMSuA8PZ27MulIC-1Woh76UCuHE0Hhn_qijk2yRafa9m-o_MwXZ4tskT9DZWEQT4Yyt0cg-oO9qot-9HaUo78nO5JUHhD5w8lM4RvfbYzGKm83C5a3Iise6ciREaePc1m3zmHqfLYTP-o67Qrv1kcBiLP7ClO0IQYlIahn21G8PfigIF9cOUaCtnWjjM2nI4fvqVrcgTOhU2G72mYHJJGEMmA61ZACWf-lpYXCSSGqG3Pl89KqMQX4E3aBdQwXozjaafQfgU4TH6GCUXFdr0MQJrQ78l1Spfr7E-9LLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
