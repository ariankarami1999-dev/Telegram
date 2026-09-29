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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol7lceJ1P8XC0E7DmUvWkV_mzPEFyQmV7Z19fI5vsLr_MJw90QP1Jm_ENhf1UBmOhYike1j5X0HnNcYJ91wy7LSR439p90zVdfnfO-STYedjHSaxRNW39CUbRspLcIjHTIDiz_oWuQPDid6JSdTUjA7jFY-CLX1TSI40lxEIPzBmhq2XEZB8vyE2x72d-Tfg7k-oar-Kp5QAipB6vKruzT-mPpnAhbJDqzfYSjvPg2nwhiQ8qtSTMETCtrx_YZAncPzMDE3gKYp17fIo401rqTWpCwwTw7iUl3Nqwjj1fO9OhwSKTMXSW6uymuWh69f1z7ycIIa8vnCg2EuuAJ9yvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YE9BVZBJoWkUKTtdpCjZhRL7b9xujfoiT6ReQ7yhHUrIz58uCyQihGHa7JOl8c-ASkucBMrygvRbDGb4QkL7aNhllH0Ql-XhQYWRUyTafnwZqbkQ_rlmCoCBxRJHvK5dVOXYcGB0wH4zPhJeqoQCxPi11WHTdbh1d7FzS048vXHJ85tydxLFVu7lT3Vp9Vye81fYj_h6zEfu8GCRplqLmsVbrxwuJTrlYJXBZvdl_PM4tBHF9iGptSbPtNMEOSlGrBCWn36mfdP-Roky95TL5sCdS8hARWsm5VZMSf-8t_yK54h0BrOKjoPMec4i63ChlhKSnM3nKo-dWibmAzWO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAPSocpFObkt1MUgplWWx8XGOM5L8Y8ScDY8IMHswscFwJDgIRBKmbWnGWW7F-Ude7XCLcQr2IcovB8ty61dStubH7Xp-AmxGMZW98l5WydpnQ8vZf-jmuLQpKPpMi-7468ZEFbkISg5JmDESsC0R21xBH5jtZFGHkIhjUZ1uC4jf15gPqOXxKtdYCTphcLPx4oRIeH0VCOzdk4PJxexMEKEELbz6yXRlExNaTg4j9S0UMIZx29Mq0RmDcUrSOS72yTAOu8ej98rq9gLDfKV55-flKj3JcgnxLsvLzNjaxN2j3zuf-PptBGPetGE3kkGC93-McTD2g083clmQ6NDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO50nJEJIvYE5pMzI5IW9QDCwM9Cl3_kSFkgPuMuWUXnP9K9MLuuKbOdbKPz1wxj5efuAFWID9KvYKRXhVSNgFS_g8Nxoi6IL9EHOUyGDuUyx9ZBXDTVZnmKpC607AGPdgSrCszMnbiLmZrutqnSVuU8ZBAyUevD7ynqPBpmszTqkGRiRbGv6EkJUHR69mJpAd8xJtrNomdKke8dPx4PpYN626i1JqbvHClbPGTvo0BCR97ZrZBfJ7BEANVvKKtcR9BfUD0MLNvx6Dq2ZdS_nFqYewWN1rw9GKiPBwK_xKX0ek0paSmzLjznHXDFN-ahMr6hYDUr1zz1nQpMN4OaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4xQpLylnjD35tKHL0jOetLd6Tjl5tjEF8Fyg_IdwmNFNR83CmqNH-BVJM3JSSpbOB4bszn6LwGLBxXDW1FEfbfPCqKCqRzktoCkJFz50dDMoSjjqtT-ON4iDDOgCRJFRnNueqEnUvPntvGNjyNGtxTC0PzXhroz1BhLPEbt7TDy4wS7qNwlyLcdJP_jzVLovgmT95wm_7dLNyZIV9fTo_gt0OSVAbHe3XOglbdOnjW9lU_3lVrzYaiKhkT6jGBm-LF7Pm3GwMBrYliAgUSqgvMG4Gt_9kLzqB7oQwUCFeLIVWRMRcC7-E-mTXPb7i1mrSdNUItFxkB3NV2VFBnP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMAa19cw3HO0gru0V10RtFSTfd8QzC2tQPzLOHZn0JnU1Zy9o3WehVfMLgh-0aV6DThsgdzJTLjuH9LA0LRDzWxatVn1vPNX0z93Lax8vsJSuGGxAW_a1uB7_Kd7aHa-KP_vxUe1yEoBQWFfs_tPyQFeJKkXm6fFON9J3aZwlkc5EPxsQFnm27TgElIJwb8igVZMaID5pusagGsw423yn4s-IMlu1M2lGl4NwkJc7fhD53qOA3FB9dhZ2YMlUZJ1SGitFbhi-VxSS-87ipMK-ckko4OI_kia4FVaim6cjPRSkHvgc0bVCrFexMksCnwZlX9l3LytTvuSCkDBHQENbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=FSiBF6ksvJj1CurcTAvEVe7Xx8eEX66mUQ2GP5OHPRDKihUvr6hnENLiFBGSLaUlri8nFJJ1RF2cTT8iAaVqvqwA42mekrMbGFK7r5ZkTyPH4DPdvle2bSOSHE5YIIHH01Jmr06g6RIkdm5CCMR5AgTw8sWSjfZANmdBRkZyLT2qLfFPOzbAh6EFJ2CkyyJpbWJUiO1smizvk-RMdyeWJnerx5UYrKXwdcBxsWit9eiBxEhyNf4miaECBMj9SbFMFRc9G6_i0P9kvInpksy7ffkw27k3eJagZd5CUKUX9QSadEa2I2mw3buzMD_pBd-4fdmPvvjtX39C9rF50oIIBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=FSiBF6ksvJj1CurcTAvEVe7Xx8eEX66mUQ2GP5OHPRDKihUvr6hnENLiFBGSLaUlri8nFJJ1RF2cTT8iAaVqvqwA42mekrMbGFK7r5ZkTyPH4DPdvle2bSOSHE5YIIHH01Jmr06g6RIkdm5CCMR5AgTw8sWSjfZANmdBRkZyLT2qLfFPOzbAh6EFJ2CkyyJpbWJUiO1smizvk-RMdyeWJnerx5UYrKXwdcBxsWit9eiBxEhyNf4miaECBMj9SbFMFRc9G6_i0P9kvInpksy7ffkw27k3eJagZd5CUKUX9QSadEa2I2mw3buzMD_pBd-4fdmPvvjtX39C9rF50oIIBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjXWBP3z39zP3y0qBC7DHvTJZxDgdfzq0-SZ1WKTjtl9299W_nRepeoTNdbQia1C_lpuq9xRbXkRbdLSp4HzXqEBYHGue3JnVb90dc5EkhQakCf8-T0W225oX4VjQ8QfBLPzcsiMvknbtOFgQTSeJUtSq_PtP4HJrcsm7nHdySgwXeZKJZQP5Ih-IsqkSXFOpoXJpDQ7-L7UJotBhJwI_CTQtVKHUuSedjaXrRxvhO6RzavZMvU4LzzBLb0K2c17wrKYeA-2LD7lm8cbaBLOHZcl7NvzudjumtwjnRUZ16RN92wR685oSN4i_8o8iIaFGRJMDkIru6FYSFIYqNIJkw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsiYZOj_hgXWhNf82kojUD47WdhY9Q9eRRy5UFlCsSs8Vl5_QCcrRfSfoB19FtbXQtT8A3pjnpfF0xh-tLu6QfVQZRE5mltwNBxjH57Ns_j61fbga98BTr_f5zS8Qhy8Nvtkp1S_vSdRVq0U-ZZf4SnrF3lIiAqxXlrasVfYnFpIJNVNCEV3FHP2Ec8wuhrWWy1gHpX9ytWZ8OlzZV1i3vE46_O0oEzMtIBpPYk_3gpWp8R-1coCXmq7k6qTEnMARQ-vAHOhLZKHz8hpE0w70Pq7dIcVnLZT9P6G6nCcLlR9i9Im83zs-vG2LqdDhrjmg900qmZ0s1OV_QqjR26SbUSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsiYZOj_hgXWhNf82kojUD47WdhY9Q9eRRy5UFlCsSs8Vl5_QCcrRfSfoB19FtbXQtT8A3pjnpfF0xh-tLu6QfVQZRE5mltwNBxjH57Ns_j61fbga98BTr_f5zS8Qhy8Nvtkp1S_vSdRVq0U-ZZf4SnrF3lIiAqxXlrasVfYnFpIJNVNCEV3FHP2Ec8wuhrWWy1gHpX9ytWZ8OlzZV1i3vE46_O0oEzMtIBpPYk_3gpWp8R-1coCXmq7k6qTEnMARQ-vAHOhLZKHz8hpE0w70Pq7dIcVnLZT9P6G6nCcLlR9i9Im83zs-vG2LqdDhrjmg900qmZ0s1OV_QqjR26SbUSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=YFMV5BsgJCw5Hsk1eREWUZvzCqtKbTuazZbOXmYzgGXTgMpTOL6qcivDAWMV6T_UZHr0mY0wxdz33GTTX6seRl1n6zCEPtABms8dlJb3PZan_dzxnZT9qj9-gjfeh4AD9YTfSxnsurJVP47MRql1Bk_-ZGUb63WLgr5Mqt1epC6A5F_uBpNxfujUBzVV2MSBFmcSUkFDBy0yRMBoJVrB8srhXZp6ZKUWbb9mX0ak4WyJ-SZcq80INluFJFPDbfliEWdlvBzj3I9Lm2KHAzVA_pJ1E8lqnAHirRhwdgNAUv1-NOKtIA0qF5tKrEpUenZ0PraXF8wosdzQFLWNh5waPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=YFMV5BsgJCw5Hsk1eREWUZvzCqtKbTuazZbOXmYzgGXTgMpTOL6qcivDAWMV6T_UZHr0mY0wxdz33GTTX6seRl1n6zCEPtABms8dlJb3PZan_dzxnZT9qj9-gjfeh4AD9YTfSxnsurJVP47MRql1Bk_-ZGUb63WLgr5Mqt1epC6A5F_uBpNxfujUBzVV2MSBFmcSUkFDBy0yRMBoJVrB8srhXZp6ZKUWbb9mX0ak4WyJ-SZcq80INluFJFPDbfliEWdlvBzj3I9Lm2KHAzVA_pJ1E8lqnAHirRhwdgNAUv1-NOKtIA0qF5tKrEpUenZ0PraXF8wosdzQFLWNh5waPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmItjsWvveFcuLzQ0nOVYjQBroatgverjBzba28nqhZC090Gja0SSO3U8Aj_3mqFTM0LniQ_6i1ABrlWUb6iOeFZipXQMBDSRS2S4Ur17PpY3FSZ-wVSqwDZ9i2nqMloX51aeqRbVJQlOnYMEnatC9qHET_KQOUeqTS0aHkI2jD9jYnzKR1I3yOFqCU4q9RU2YucJc-JHVNL4S6JoglkwHqmDnN2Q5AdoFVz0z10lUkXrcoxhFOIF8xLQnA9mP5ykr2Nw-L_6wSzQv9TsTE2FrOWVn_yVRuGzoTMM59FgFtTVyPNBRCJoLqe5H4TMqOqm1YI_L5WR11nj17P_XL-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=pdWpsGJiK65SyZYUECHUOKTIqw4yqB52kRutccAkPz659kQa38sLcrp4k1v3WEf7psPgpMs74C_DzRWecMXY7p5JO7UA62z26_Ma-2eZIKGqpPyho8pY9KXFKSdrU0lRyV52bxhYUUlHz-9x3B82OsXeX810Y5MRLuY7iiw4VuxC-iV0U_tBv5POI_k2ISWvibsE4OfC6tLY06rsYj_Q4BmA-Tbfazm655hU82ntQfnBSkAUsEYFHwX4rxvmkjQfY_uLoT6641FpdRSaVUeb25yqMphnG2nkjkJc_oAQqORRcUbbfaPfpNPd_x9Yz-W7ElPnMv30Ka-4aKTrG8qEqJQiYjUcizo0mXoaNwTsYUIUEfVAO8ump3LTD1ZR2auQn3zjRYrkZGA0fPb9YP-uRffczSTf_ZEKQu_3oKTLvVss-C-iq-zm73LALCI7lDGg1iXSHwpv-5-zT9jUXqF9KaSPwlYKFGhoGh_nbTn3C7FtO7y_uV3kg62uLEQWQHl6WswVDvKx9V4_chZfzQyoOTO0cMayJPcJ4K9jzNSSU6BjqUnQqsM5brJU1qbXF7fmTx4byD_QudsqmKakvtF1rNjB0cBn5nSrXU7u3yLSf9NdtQn73WcmA7eBOBiEsMdSTyI5xb9SBdDvd5ntr1JmyaAH1x9QqcnIE2JzepGmd-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=pdWpsGJiK65SyZYUECHUOKTIqw4yqB52kRutccAkPz659kQa38sLcrp4k1v3WEf7psPgpMs74C_DzRWecMXY7p5JO7UA62z26_Ma-2eZIKGqpPyho8pY9KXFKSdrU0lRyV52bxhYUUlHz-9x3B82OsXeX810Y5MRLuY7iiw4VuxC-iV0U_tBv5POI_k2ISWvibsE4OfC6tLY06rsYj_Q4BmA-Tbfazm655hU82ntQfnBSkAUsEYFHwX4rxvmkjQfY_uLoT6641FpdRSaVUeb25yqMphnG2nkjkJc_oAQqORRcUbbfaPfpNPd_x9Yz-W7ElPnMv30Ka-4aKTrG8qEqJQiYjUcizo0mXoaNwTsYUIUEfVAO8ump3LTD1ZR2auQn3zjRYrkZGA0fPb9YP-uRffczSTf_ZEKQu_3oKTLvVss-C-iq-zm73LALCI7lDGg1iXSHwpv-5-zT9jUXqF9KaSPwlYKFGhoGh_nbTn3C7FtO7y_uV3kg62uLEQWQHl6WswVDvKx9V4_chZfzQyoOTO0cMayJPcJ4K9jzNSSU6BjqUnQqsM5brJU1qbXF7fmTx4byD_QudsqmKakvtF1rNjB0cBn5nSrXU7u3yLSf9NdtQn73WcmA7eBOBiEsMdSTyI5xb9SBdDvd5ntr1JmyaAH1x9QqcnIE2JzepGmd-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8erNngnZ9hL5Hwg2SnoAnUNrnfnTzFOQ0Y_Se321YU000pNeqG5k_L7UogDTEPZN9PK9jOoV95maZ0XaAgphv-5F6Bn79kGP_U4su4rQQ_2dg4x8dTlW4Y4u7cXTFDy7-rWXlX-ubt8bOt0lRX1ecutoRDmjMzdehdt6Uf9r-sX6EGleZ4ohYT457pqBlRRpn3JJxD3nf1TjpJhoU47dXpYYz5Q1xLFClq7AAVtmQFrvUuMVHoW381ryNoYmBBugATI0xpZ_jd9hLojppcKy5pwUb2OIfmpDY447NzklnBaGOt-gDXnw6Uyj96F31abCXdiUUSl1XlLrYCEgzSsbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=n1jwZ4PI5DUrqGWFhboD-f4nKKblyMipbMTf193oc8804hDMWrN8J-eaGsLQrlAuETcfrXoVxxcdJA6oLRtr4pDnoxrKXaz9Bgx7cXiejOIgZIopqP7kqefYRjZpobJQilinARIEYBZm-dDST2Q3u2Ye4esCO08vttsxd0k_VF-Hh8bPJeAYbuLv3MugyYmDtjE30EAGvLiWztpXi7fPB1qfVKxTUitqWjGAuxPSxj-bZjJDMz9q0agfv-g1FWJV52TmW4g24FEM-jke4X8zaUV4bf0_bocajgym5e8C9tJl76apsOK2wHrEZidGucBkLkhtlp77bnphcj5BO-yH-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=n1jwZ4PI5DUrqGWFhboD-f4nKKblyMipbMTf193oc8804hDMWrN8J-eaGsLQrlAuETcfrXoVxxcdJA6oLRtr4pDnoxrKXaz9Bgx7cXiejOIgZIopqP7kqefYRjZpobJQilinARIEYBZm-dDST2Q3u2Ye4esCO08vttsxd0k_VF-Hh8bPJeAYbuLv3MugyYmDtjE30EAGvLiWztpXi7fPB1qfVKxTUitqWjGAuxPSxj-bZjJDMz9q0agfv-g1FWJV52TmW4g24FEM-jke4X8zaUV4bf0_bocajgym5e8C9tJl76apsOK2wHrEZidGucBkLkhtlp77bnphcj5BO-yH-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a107xzyOiOcePmYfaqSMeLVOKjsQ9WlYbgN16jbm68KVx-KpAzQBUE6UwVNjF0LNLxeW3IRnGpQ-bjsjnXAJ8qJag8q7iBqZsajpUkllsOJzfv4pUSze4A9y7Ewx7LipKAqiuYt7JGgNhuWEVmdlei9fM3qJYh6nyFevTKg_mHzApLMjsJcWimVvDMHX44DwpTP9YTGucUddyozR9OY76X3k5ZABhnrPVNjGqHjWfjSJYAHtj8Dwb2Abq_B-YLP_W6qWQpJ2SIeUgw_ATaXSeFoDSC6UMcXNt1Scwh7AaUrtRNM-PJ-nCteaUDLTLEJoEMCv7JYsMXaxt04VlC9xWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC_IicoFh_cy5LHpaXySbCbng82qO8buPJJX5KO7NRnDulP8hT4ZQfobBYd2Xqc6snfTAXF47cu5niUt_IWSE0ANeWzkQfEA_ZDrsm2PPKw2q3QQEvMYokdUCXqjeyzuTR_WDVK1rzPq1A_pO7GvIDODCF1HpatVfykFqNYU7QpGkqWzL1KSW5AY6cs5RTuLnfNXLKo8sFWwef_RFsGtD8WiuvEKh_P10f8I497D-aqSPSKIxBY1E-XOxW2N0Xv61EktUKeYMELCIOJ2BIXZYaBiF9mjClu49lef461U-pZ7yhzw6y-xnlEeCVqKL_Ujs7rDCi8UDdGU51smMwZYDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQtBSchtaMLhklHlFapL7pZHHSOXsLKpaLmoG7-gBcql1iAEcpQoTib_pbJvB0tX-dq1UAkFe6dn-O57Xm7ATyc4dBjtSnQmtxUN1G34EdE-Vyr3MhvRIQcIPFc7b3B2DXilHhIHk1rSvuFozavEFDeO-4O0v3pNKm1KY-8fOJNnCoYhY15gGBvNIauyUrcpuD_z5Alz5sLs1eyIXFZhijs7_RBsRoRLfUK0g2PwqKAccaoO8PeQRAy3noLyzkoOCUmfjED1-DFpFP4tF-DmWntzuRa9MKY5aLj47pniZ94Q3z5BM-_Uojlxu8e1-gUyx1bC5me_X6ar00mT_jzV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=HT16M5rmJju9kOTIEiz13F3yzzizGONinsSXVo61w-MQaVkcXff2Z6cWQAXRhRvG0afoEZKUl6qGpBp_IjCq8K47fhuE64QGQc0PTddZapfTTERfKEoeNzc8fLFJ9yRuC1kswDb2IH8BQzWZxXcDBkPUI8qzz8jkD53LGI9sMw0Rk-WpbXBfk_jx11fkMkTeNMRe795cGjAVnFoOW3nSTFQDWEKzhxRtWDAROhHpeO2x_JQytryiuAiLq-2QACAhXlRMfQL1fR8Q-5HNhM7JS5P18Etgu4-rRMUMXZ2v9Gc6lvoQZhHwyNfjzDhCUr1wa7Vudd_MpHFm3VJB9sBIYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=HT16M5rmJju9kOTIEiz13F3yzzizGONinsSXVo61w-MQaVkcXff2Z6cWQAXRhRvG0afoEZKUl6qGpBp_IjCq8K47fhuE64QGQc0PTddZapfTTERfKEoeNzc8fLFJ9yRuC1kswDb2IH8BQzWZxXcDBkPUI8qzz8jkD53LGI9sMw0Rk-WpbXBfk_jx11fkMkTeNMRe795cGjAVnFoOW3nSTFQDWEKzhxRtWDAROhHpeO2x_JQytryiuAiLq-2QACAhXlRMfQL1fR8Q-5HNhM7JS5P18Etgu4-rRMUMXZ2v9Gc6lvoQZhHwyNfjzDhCUr1wa7Vudd_MpHFm3VJB9sBIYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpFu5KzArgwwoKRI1PhHTr8aZW90FJfTLxrAADofPfkUpeOBTHPGm0ozN8kJeecBIYn3XhjiParQL_C4kP3HUWvEZPrdrp4NHLTK63GfK44D8JIgtSQUi1LXYTaxnMo_5wwFyyun8uFqNYlZeUjr0Eato7-EzfAoqVHUaAExzJ_W4R_-LlFIWaHAAUDetrZtMoL4O8cgJodhrkfbBkVZ7Xq223fFqGaWPdp6mPF-Z0xKVIyf904p2NPe2cEL8whxxRL5Sl0hGnyl-CErxbzaXzhlZQJeGyiNn6e6ejVcDOcmWTf3y7T49lK3-ASTkEncxCSXcuw6f570KJPi3Pe69Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFDJcDPq5PE62Lz23oXjxJ07PnLrlZcqROdwP1cX89dLS8_Urn96dPRC6usIqIsGWz62hnkkzfF9iMfhmqDchO6ZgJQ7WaKLAVlHGw-Q3H_PbwQypISxwODvsKlOk5G1MkwB0wyIB_76tbInZ3Na-B0EBU_xyx5fF03B_R8y5ifoSae_2Kbz0Dlg252mAnW9uclA3CEeoUd-zz5sRMshCz-pmTUfjBsRcMz3Iz8otZrAc8e91dPv5HDLNxZveZyimafbcChYGeeh8pnudvKF3x4a_9CV0BB8fpK6QZY8SjTcAIcJvDZi1jHtaEuOMRXiXWf7FXxq5noBy2gbfw5KcpkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFDJcDPq5PE62Lz23oXjxJ07PnLrlZcqROdwP1cX89dLS8_Urn96dPRC6usIqIsGWz62hnkkzfF9iMfhmqDchO6ZgJQ7WaKLAVlHGw-Q3H_PbwQypISxwODvsKlOk5G1MkwB0wyIB_76tbInZ3Na-B0EBU_xyx5fF03B_R8y5ifoSae_2Kbz0Dlg252mAnW9uclA3CEeoUd-zz5sRMshCz-pmTUfjBsRcMz3Iz8otZrAc8e91dPv5HDLNxZveZyimafbcChYGeeh8pnudvKF3x4a_9CV0BB8fpK6QZY8SjTcAIcJvDZi1jHtaEuOMRXiXWf7FXxq5noBy2gbfw5KcpkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=DFHmQm7JbmXrgCmQDamum5DkCR5sODPVNGI3xxqysBRJYbHaF8gy25laUhyW-crRKjnc-n_SVEfaM_YnZNTPoA0iTX7Y6N7wKpADYXmPHibtmgJnp4mYhHJMTSkyjF9b7JadHy1GpWiLQIutLlB69lclLAejPnQX6ACuTgyib9m3-k422YoQY3D86Eu73Q3zd_bkr4gzjJRC8A0JkgE0EinkESb0U_UdizsNo3NRXmRa_jG0LyeB4x9OMN5geZnvULeB5jSoog0dsRT79n_9Un8Z2_IT9dN2oA42FT-NpgFuPGekt8rFMluC2Fl2UZ4Eh0Kzbdmv40JMfLh-MQu-7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=DFHmQm7JbmXrgCmQDamum5DkCR5sODPVNGI3xxqysBRJYbHaF8gy25laUhyW-crRKjnc-n_SVEfaM_YnZNTPoA0iTX7Y6N7wKpADYXmPHibtmgJnp4mYhHJMTSkyjF9b7JadHy1GpWiLQIutLlB69lclLAejPnQX6ACuTgyib9m3-k422YoQY3D86Eu73Q3zd_bkr4gzjJRC8A0JkgE0EinkESb0U_UdizsNo3NRXmRa_jG0LyeB4x9OMN5geZnvULeB5jSoog0dsRT79n_9Un8Z2_IT9dN2oA42FT-NpgFuPGekt8rFMluC2Fl2UZ4Eh0Kzbdmv40JMfLh-MQu-7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=OIWxpKCd_yPiLCCg3Gei1KznCNhbes2Na_kOpz3_0RAP21G3j1NFFA2ZLim3cpT6cVz_kzZKbvqmRj2C-_FmSo0yRmsECxpH15SOdu_jmPti0YhpMcFwRHDiAv4f4X1kz7fkVGS2WRr1-1yJvsvdcBDpKXKuUvEzQBwzFjo2rYo21rsXiy59isHWhgHJPPYKPw1_0vfbabjNhuWSvl2GUJqPi7CQgfQmgEpKJQOgN7bJA_mxkTFwN7Wd8O2aTi3ucFj1MJ_4-Pmo1nrG7go1pUZW_00-SVrDSW66EMBjsrVz9V1R1SWmYbWTaIfosGqICZ7l3j25_cdANkBpxIKuNCYPeoJoSnlNYNQzznzIgSOpqonmodc4jktDVsIQNo0y-fBeIEgD8PYV4T7eiueqEHPkCcDR4Qsp8ShGzYdZDoJVkohLmWsiACn-pagtPDKVtzBozvfyEtjFa9UOVZkPt2ZfmZhVxjfox-wvWSZT6wfXsrfNFYKo8XgHGMfAVkHxrQ7xqwbRMpQvKzrN580Noz4TU4bNKDQEv6vU0QL8zB1lf6dc7EvSlZ92HgbohMoygIDiGjRmGjFR-c1bUhQOAaiQpaYLYayYsuH5B3Jj566ua3OXSLy8pryDaAAl57NgJG0jXgsJds3BUoUmZ5bMBEYTQ0iW9hBntfOaEuQ5hFU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=OIWxpKCd_yPiLCCg3Gei1KznCNhbes2Na_kOpz3_0RAP21G3j1NFFA2ZLim3cpT6cVz_kzZKbvqmRj2C-_FmSo0yRmsECxpH15SOdu_jmPti0YhpMcFwRHDiAv4f4X1kz7fkVGS2WRr1-1yJvsvdcBDpKXKuUvEzQBwzFjo2rYo21rsXiy59isHWhgHJPPYKPw1_0vfbabjNhuWSvl2GUJqPi7CQgfQmgEpKJQOgN7bJA_mxkTFwN7Wd8O2aTi3ucFj1MJ_4-Pmo1nrG7go1pUZW_00-SVrDSW66EMBjsrVz9V1R1SWmYbWTaIfosGqICZ7l3j25_cdANkBpxIKuNCYPeoJoSnlNYNQzznzIgSOpqonmodc4jktDVsIQNo0y-fBeIEgD8PYV4T7eiueqEHPkCcDR4Qsp8ShGzYdZDoJVkohLmWsiACn-pagtPDKVtzBozvfyEtjFa9UOVZkPt2ZfmZhVxjfox-wvWSZT6wfXsrfNFYKo8XgHGMfAVkHxrQ7xqwbRMpQvKzrN580Noz4TU4bNKDQEv6vU0QL8zB1lf6dc7EvSlZ92HgbohMoygIDiGjRmGjFR-c1bUhQOAaiQpaYLYayYsuH5B3Jj566ua3OXSLy8pryDaAAl57NgJG0jXgsJds3BUoUmZ5bMBEYTQ0iW9hBntfOaEuQ5hFU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Tt4Qt3kJ0hwMG3xHyp6o-w8c2CovuwuYWELrUpKGnjg5YAg6dqalKOWmgUVF1YSW0hudjTwf2odk5A4NxAdj5PeyDoOJzTxBc2FlArAPnTmNKJaZyLQSqPpq2O7LZUfmcbuOCF_QR9flSnqSb5My1cWSE_ryqFE1HdD78kRv0mTBf2sUcIJutzGVayWhP3-LdXCFHdWQ_Owtlk0K9ji3p3nIw0EAu_omvMTQE5dXFm2xZ1Tusr2fafVKV9cCgqTImNIQhVrkwi0xMCaQFOlGElHqSHzRzKfiq2oL3JWaGaNcfUhiigtBjm0CKLF7mnm9xszWF2K8tocNTHKutrJ3CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Tt4Qt3kJ0hwMG3xHyp6o-w8c2CovuwuYWELrUpKGnjg5YAg6dqalKOWmgUVF1YSW0hudjTwf2odk5A4NxAdj5PeyDoOJzTxBc2FlArAPnTmNKJaZyLQSqPpq2O7LZUfmcbuOCF_QR9flSnqSb5My1cWSE_ryqFE1HdD78kRv0mTBf2sUcIJutzGVayWhP3-LdXCFHdWQ_Owtlk0K9ji3p3nIw0EAu_omvMTQE5dXFm2xZ1Tusr2fafVKV9cCgqTImNIQhVrkwi0xMCaQFOlGElHqSHzRzKfiq2oL3JWaGaNcfUhiigtBjm0CKLF7mnm9xszWF2K8tocNTHKutrJ3CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP0tLH67fkOJtuT0WBJeusj8z_o9BPiX2h7anpUBiyITR9pHHpRJjWgRzPr8zH-lckzhnBoBCnVfvxgW4zMzWEIAuUDDhaKaPTsMvw4jgGiwFzIOA34TXRX_WRi_TxYcT0HLy8qd1OZl_OTuO1a0fu0ZeQh7xL4jLPd8yox-1wG44KEUde5F4zzR0iwZaPnEJNIG6T_1BNFXXpCUpWrv-vabKeLZb3FDxZjZIyLqOS73CBBZRGKxEsVGNii-2nIDWa8qJtkZM94LgvJ0K2xbina4vA8-DXqXl5kfY6zAd05F4n-qB6ULPqS2EytaOnmlzfG3iq-5wM3OqlM8x4cY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=gtCZ-JKBtxXvuLiXDsPZ80VXU9SVFDfFyDawRviH4oqNInv1l2M0GLafkb2gq143x-I3J8WQf_U1vtLpnkENUCTaEI-_JCwv55Z-o9AJc8Sh66ACRuGJj1paalsE5dIuag4TiYJu9rij8ONSoSFlSyxbHL7Lip3bq5SSr78NPapT9Zo9xPF_HnT8X104CRJUX8gcQfIP3XQcx3_hzt0MWyWXi-pR1QkSASqX5t4aLaGCOkQOAHBGUsq7W5I-kOBmlZJOYMEQNnxBvDo_Cq30DFs-zkOcQjgea-aSMQtHVf5ZA6ma0LVozDawI9D8iL868BrQBgcyRIclDauwJyNLYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=gtCZ-JKBtxXvuLiXDsPZ80VXU9SVFDfFyDawRviH4oqNInv1l2M0GLafkb2gq143x-I3J8WQf_U1vtLpnkENUCTaEI-_JCwv55Z-o9AJc8Sh66ACRuGJj1paalsE5dIuag4TiYJu9rij8ONSoSFlSyxbHL7Lip3bq5SSr78NPapT9Zo9xPF_HnT8X104CRJUX8gcQfIP3XQcx3_hzt0MWyWXi-pR1QkSASqX5t4aLaGCOkQOAHBGUsq7W5I-kOBmlZJOYMEQNnxBvDo_Cq30DFs-zkOcQjgea-aSMQtHVf5ZA6ma0LVozDawI9D8iL868BrQBgcyRIclDauwJyNLYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=mBUMOHboeugIR7abutGvFUOFeNfe5JUhsyMVXgEugF9dZaArYDeSTkmrxMfQ40t8KrBRYWtuXZRaCg78za_MF40LZcWC-Cng7aigZfZFk_KbZXReg9P9nfiXGdRG7ZmMawBVkdxwV_KbA7GCKvwEn8olCSwSst6RwlRX3otH8OCeeA15w7NlHUKZE8uneWPiemuQ8QKeSaAfBLqmDgzobaiptWemrrlqa8uqYWaWfAiDdJW8SPzODKfKZ_XQRnckDDP2xA6Lj1DpPK1VF3MroB5JWjjmXbpOXw9qyrs9Ocw3Xfz3pt7QNMCzhNipfoRqbSp-1xEo5Xg9HDNgENGuiybregg1l5tWJr4Vh842s0KzWqya3KIKIskKUNYkReqdHFmQiNj_heErpANy3Mae4uyGIyjF23iqTqNdvxccJenG9WozsXXSemTQ7IbjBclvs2VjHkgzJozsZdZmaNqJ83Otp6VIiMFrPc_RXtH5isDZEjW-WWALCb7e9qNOpM41YvsSFRL0THgMgccfm3j4X7ItJzgKOJadVHT4KSO1KZWKMgVUvWcH_y2ABRN3DpjtXj5MqD1k-OVpiRuzIUqE0DlUVYojsSvq-QERX12Ht_beBW60WR7Y_PDJ7C7eaetmB871LHA87h-QCFsoAhtOYlkGgHA7fpSR4PmecTzMTDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=mBUMOHboeugIR7abutGvFUOFeNfe5JUhsyMVXgEugF9dZaArYDeSTkmrxMfQ40t8KrBRYWtuXZRaCg78za_MF40LZcWC-Cng7aigZfZFk_KbZXReg9P9nfiXGdRG7ZmMawBVkdxwV_KbA7GCKvwEn8olCSwSst6RwlRX3otH8OCeeA15w7NlHUKZE8uneWPiemuQ8QKeSaAfBLqmDgzobaiptWemrrlqa8uqYWaWfAiDdJW8SPzODKfKZ_XQRnckDDP2xA6Lj1DpPK1VF3MroB5JWjjmXbpOXw9qyrs9Ocw3Xfz3pt7QNMCzhNipfoRqbSp-1xEo5Xg9HDNgENGuiybregg1l5tWJr4Vh842s0KzWqya3KIKIskKUNYkReqdHFmQiNj_heErpANy3Mae4uyGIyjF23iqTqNdvxccJenG9WozsXXSemTQ7IbjBclvs2VjHkgzJozsZdZmaNqJ83Otp6VIiMFrPc_RXtH5isDZEjW-WWALCb7e9qNOpM41YvsSFRL0THgMgccfm3j4X7ItJzgKOJadVHT4KSO1KZWKMgVUvWcH_y2ABRN3DpjtXj5MqD1k-OVpiRuzIUqE0DlUVYojsSvq-QERX12Ht_beBW60WR7Y_PDJ7C7eaetmB871LHA87h-QCFsoAhtOYlkGgHA7fpSR4PmecTzMTDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uw8Zc7lu4I8VQ9YfFLLmobS9Wz0_6xHQRNgfGe6pzb7iyrbU0U6lIvre5aPTQU7kotKErmYVZ2Ywkdfe4HQYicIc8RCC7iLTf5c-YQdwe0uPIYSxR-1WGPbfB98xH3xEI7cBCx5P9STT7y5KmoO-SMmeiaAQyFfhuD0uc5XPyaTqF-oUNveXBGJaysJgY0lCev1vR-SXOZTVKoeihPe39I879-OFNn6JGEG7MTuNJhsGcvcAMI0SCzu4v6Hfa7E4NhxdDdlWxFjxrZbKI-a7dbX8a6Lta3djiYI4snXQjvzHPPJ7YNcRguy_GA3dbSiDjpGmD2leYhcR3aloTIqOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=qIcBxMOJvqMlRere75PsHElI_VfT1_4-rrj9GUNzFjtPT9jeH5C_Cz0_NBtqzLwbov2i-bTXwW9aYo7TYGRsaFGfOT81VTae6Jd5M3GG6NLUNrJ0MFh2CRN0BXhOzIHG3cxcVGNdZe0Zu7VXYBaV1oQ1zyoA3ldU2k6lmRHesaUUVqRAj_75Oj7-cQCmHt-rtoKsE3GH5uzB-qaGvgdRr5p6bGhZk1vkxC-CQSmoF3zM_sbSvgMVQbGlXqCuLuilb_wmLW8lGF9hIb0PjHtS6Wk6tIV9j7moMbQFWs9cF-qJbaLoH1eMHinT7PpWJEeAS_BWD7v8HNlOdtyu7M_5V0r5OqO73UX1ioc4dyWduV8LlAsQa6imjnHYgMYmR90FmZAC5jm6cOHBJqw5YYSPz6Wa7Tf75U_B4BnunMlzqYo47Qwure5zCib5T6VbmpR8W6nR7NFAkXZ-KRBmsWcXS4V7WDzhaDpozLdabCp0uhQp9Q66wE7cYj1Cc4w2NZJDktKW0R-b-2VuzFXTZtfI7QxFfUXKdmhZGPC6rVnr9xbdMUrUsK0467ZG6MaPCtL9asD9pTf1DLEosDiaxqMTT1AgnECQjcUQG8HpAeyKLdToP-2TG_VuhCoZzLJhlVSWX15Rm8m631__Odo-rBhn7Ca-Wa85dQR5yK1QAdatY5M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=qIcBxMOJvqMlRere75PsHElI_VfT1_4-rrj9GUNzFjtPT9jeH5C_Cz0_NBtqzLwbov2i-bTXwW9aYo7TYGRsaFGfOT81VTae6Jd5M3GG6NLUNrJ0MFh2CRN0BXhOzIHG3cxcVGNdZe0Zu7VXYBaV1oQ1zyoA3ldU2k6lmRHesaUUVqRAj_75Oj7-cQCmHt-rtoKsE3GH5uzB-qaGvgdRr5p6bGhZk1vkxC-CQSmoF3zM_sbSvgMVQbGlXqCuLuilb_wmLW8lGF9hIb0PjHtS6Wk6tIV9j7moMbQFWs9cF-qJbaLoH1eMHinT7PpWJEeAS_BWD7v8HNlOdtyu7M_5V0r5OqO73UX1ioc4dyWduV8LlAsQa6imjnHYgMYmR90FmZAC5jm6cOHBJqw5YYSPz6Wa7Tf75U_B4BnunMlzqYo47Qwure5zCib5T6VbmpR8W6nR7NFAkXZ-KRBmsWcXS4V7WDzhaDpozLdabCp0uhQp9Q66wE7cYj1Cc4w2NZJDktKW0R-b-2VuzFXTZtfI7QxFfUXKdmhZGPC6rVnr9xbdMUrUsK0467ZG6MaPCtL9asD9pTf1DLEosDiaxqMTT1AgnECQjcUQG8HpAeyKLdToP-2TG_VuhCoZzLJhlVSWX15Rm8m631__Odo-rBhn7Ca-Wa85dQR5yK1QAdatY5M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Sn5psM3COrmRsifH4fYedBAxOdUROuM4jYh6eyuc2V3oCuLnpp12yfg_M5GfIDEuwg2ha5aElerDc7saOI1pXlp3dl_EmkDqgrAxWwNQfTCjXXFsGKxEWG9mq_cm5VkBsCZI24amnZPmrXEBDHRzryhhQDZCHlLqEhfsc-F4jTm9VnU_s37iELkzrkYwt401bH3Q4j1ORVmGNqgLP-srZVLuqVwFymuz-znKLTbz4M64JUeFtIKwT1ichZ7iatbUVhtZhj6je5T7Av3JrXJSeS0dqzGf3tn_AbzUrXNbveTL2z7F5mN9U3M7KWBNwmSUvW510gjytJIrQU_rnuYNWkowgS9YhmQOYMB7QuNieAqF74AEiHi_XEKIwdASE_zwuyeSG_H2VFsnfqBQpSVd5EeclFsFkcOMXoqjIn_h4i8XtU4An28r3IkJSQ4USKl8igLTZguyeRCUqiIRyaGIONPUGCrPZnIhc9GFxdNPxftl77U8C6QdzmlWtVvhKHci_G8OWNhihy8l2cRioYOvIwKAmIXQFnw9TCoG16AXn4DPuI5X_ceRN80vwNHenjIJPQsKWDW-zVxerVOXF3RSloU2tY9HJzjWHBgs1tFpf9BZ-HoU_3O7TNpBKsxPGo9L7rmqR2lR03aZ2Q5kwgJcDvBpfqOFgJAms7QnUrqEPQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Sn5psM3COrmRsifH4fYedBAxOdUROuM4jYh6eyuc2V3oCuLnpp12yfg_M5GfIDEuwg2ha5aElerDc7saOI1pXlp3dl_EmkDqgrAxWwNQfTCjXXFsGKxEWG9mq_cm5VkBsCZI24amnZPmrXEBDHRzryhhQDZCHlLqEhfsc-F4jTm9VnU_s37iELkzrkYwt401bH3Q4j1ORVmGNqgLP-srZVLuqVwFymuz-znKLTbz4M64JUeFtIKwT1ichZ7iatbUVhtZhj6je5T7Av3JrXJSeS0dqzGf3tn_AbzUrXNbveTL2z7F5mN9U3M7KWBNwmSUvW510gjytJIrQU_rnuYNWkowgS9YhmQOYMB7QuNieAqF74AEiHi_XEKIwdASE_zwuyeSG_H2VFsnfqBQpSVd5EeclFsFkcOMXoqjIn_h4i8XtU4An28r3IkJSQ4USKl8igLTZguyeRCUqiIRyaGIONPUGCrPZnIhc9GFxdNPxftl77U8C6QdzmlWtVvhKHci_G8OWNhihy8l2cRioYOvIwKAmIXQFnw9TCoG16AXn4DPuI5X_ceRN80vwNHenjIJPQsKWDW-zVxerVOXF3RSloU2tY9HJzjWHBgs1tFpf9BZ-HoU_3O7TNpBKsxPGo9L7rmqR2lR03aZ2Q5kwgJcDvBpfqOFgJAms7QnUrqEPQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Mv-218dccOQUXzvSU_-M16csccBZNYAlp25cLwIC_JwcSxqJyKmEb5Jff0iRBf-uTODJ-f0XMWk5G0R8NuqqUrxMwTJ_cckagrgpYFVLYeZiCyCuwiVHsF2Gi_3LCcscmxEubDEeeKI2LeB8dW_-OLJX99DgrIwzY1OUmjKUHwTjeOqayGMfm5opG96CtF_YafYWbO9rc0CAR9fMgm2LZw9sTwmZ-L5ukmjCk_7THpyqcqkXuMGvBc7Bpq2Fs8zLK7B7IoXGrPinGPp5AsGTRkkbOGH1ZaW2zH-ywrJZLzJKWvQovfwmDb3H8M6ZTRWlFDYRse_0xeVNYIsnDx-eJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Mv-218dccOQUXzvSU_-M16csccBZNYAlp25cLwIC_JwcSxqJyKmEb5Jff0iRBf-uTODJ-f0XMWk5G0R8NuqqUrxMwTJ_cckagrgpYFVLYeZiCyCuwiVHsF2Gi_3LCcscmxEubDEeeKI2LeB8dW_-OLJX99DgrIwzY1OUmjKUHwTjeOqayGMfm5opG96CtF_YafYWbO9rc0CAR9fMgm2LZw9sTwmZ-L5ukmjCk_7THpyqcqkXuMGvBc7Bpq2Fs8zLK7B7IoXGrPinGPp5AsGTRkkbOGH1ZaW2zH-ywrJZLzJKWvQovfwmDb3H8M6ZTRWlFDYRse_0xeVNYIsnDx-eJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=tbo1SAOP7hx4e7Qcd4HdxowKvxHBoQAFgXmoNcF-XJdNciKSlYjXaGZSokV2qcGzKa5DGH60OyJsjqm1l4qxK_ZvCF5p1F02fSDjG_H8O8iGaIg1eGndYhr1i8sZdSWlmUdSxDsuDUEDu-8Ut7GghiHxORvqkDZmpqv10yCNMss9d4VFHSumfdf_PLIg-Hcajam9qICiVitG5MQfAI0rLDZIGg_3zNc4PrL82FqHx8p23nT1kdRu5z_Bo0OZGM3v1GqrSYPQxTZXutN9eyneSf6xZwR6c9snzxCHh1SmB0nTYKWQtnK9oFTlpNlvV4OZRHSRxRHxiCX6emm7AiEKdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=tbo1SAOP7hx4e7Qcd4HdxowKvxHBoQAFgXmoNcF-XJdNciKSlYjXaGZSokV2qcGzKa5DGH60OyJsjqm1l4qxK_ZvCF5p1F02fSDjG_H8O8iGaIg1eGndYhr1i8sZdSWlmUdSxDsuDUEDu-8Ut7GghiHxORvqkDZmpqv10yCNMss9d4VFHSumfdf_PLIg-Hcajam9qICiVitG5MQfAI0rLDZIGg_3zNc4PrL82FqHx8p23nT1kdRu5z_Bo0OZGM3v1GqrSYPQxTZXutN9eyneSf6xZwR6c9snzxCHh1SmB0nTYKWQtnK9oFTlpNlvV4OZRHSRxRHxiCX6emm7AiEKdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=X6qy8PDwFOnrR5g2xbPt5lCgdxdSxlctKLFcGzP1mW8_xIjWauMKfVEe_aGtmL5hZ5uWu5NOUGj2y5xQgC3ODBY_95sBHiQ_cpJDZt3dP19Dm5B9K7jfBFGUHq3by5BvMYlIl8np39H3OQc-b9Uxg3cMnGHzV1qB4R-IHvL07MyaE5nItY7jJ8Qs3LF50pXnghr0xE6h0pIEdwnSILNZXaw-PbckXvJbaWbFQmQkut2MQlpOveI0E1m28UAB0bUNi5gg-h9DY9VZvCCuwfbQOglMdG0p0ukA_wTGzkTPNQUoz8yPKXroqf50fH7AXdsmNdXprZCk9Ex_h7YLDjJTXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=X6qy8PDwFOnrR5g2xbPt5lCgdxdSxlctKLFcGzP1mW8_xIjWauMKfVEe_aGtmL5hZ5uWu5NOUGj2y5xQgC3ODBY_95sBHiQ_cpJDZt3dP19Dm5B9K7jfBFGUHq3by5BvMYlIl8np39H3OQc-b9Uxg3cMnGHzV1qB4R-IHvL07MyaE5nItY7jJ8Qs3LF50pXnghr0xE6h0pIEdwnSILNZXaw-PbckXvJbaWbFQmQkut2MQlpOveI0E1m28UAB0bUNi5gg-h9DY9VZvCCuwfbQOglMdG0p0ukA_wTGzkTPNQUoz8yPKXroqf50fH7AXdsmNdXprZCk9Ex_h7YLDjJTXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=i6P2veTtxi6F6WkBe5e2nMBUOS7eVc379R1DLKWi-h24KZRMiND3YW7zMvXzFpf4KJhbIvfCLLLkBospT56wowcvU0gIMLU5Fpj1I0-0i7vXGBWd6Y-6CQj1gwBY4gse-uAXkdRdG21iq-e78GXZgg7GKQbEFwGwbTkPb9rEm2ZnbFaL5G3Ti4f-NI1yjb52SAvDjiBp9vfDsL9LUY1r2_ueP1hsRcOj1a9TD8ot2Faoqx8MDKpUeGbdcNRDHJyMynFNfJo6--tutD3zP94vk1WpvNfYP9uuYe6iZ1tsGYAzeZi2l5jvsIK0M8s5YGSt8pDqQH7O5q9r16e59fgX4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=i6P2veTtxi6F6WkBe5e2nMBUOS7eVc379R1DLKWi-h24KZRMiND3YW7zMvXzFpf4KJhbIvfCLLLkBospT56wowcvU0gIMLU5Fpj1I0-0i7vXGBWd6Y-6CQj1gwBY4gse-uAXkdRdG21iq-e78GXZgg7GKQbEFwGwbTkPb9rEm2ZnbFaL5G3Ti4f-NI1yjb52SAvDjiBp9vfDsL9LUY1r2_ueP1hsRcOj1a9TD8ot2Faoqx8MDKpUeGbdcNRDHJyMynFNfJo6--tutD3zP94vk1WpvNfYP9uuYe6iZ1tsGYAzeZi2l5jvsIK0M8s5YGSt8pDqQH7O5q9r16e59fgX4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=K-Issp0zLyUi-v2OLqHZ_Ztn8McS3ZPNf4HxHSayFWcg5o-ivRtpy6fZMlh5SqsvYAYRF5bQYHV_ldGMU4on8QBQm2q0FYM7kWCrwgP2J4TMqJqjyxXfqJOYa0p7rmA78_fJp_2L-qGXo03whDvH2ABKaA5-3WUBxcFo18G8YEh_rn303AnqQHYTJjCQ-FqikiUdEgFxbkJ5QjX7o52_6Y8UFDSGGLJ2X5S2rFpj1bgN0_W2pkOosUPy8u8ZnKespU7734ApCUfr2vuFTGf2-XhYSJ2jbMUIRnCuebbnbzJ4dwcGowKYm3DAAPnQdnHOUTfompsWWxE5hvoCiaNrSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=K-Issp0zLyUi-v2OLqHZ_Ztn8McS3ZPNf4HxHSayFWcg5o-ivRtpy6fZMlh5SqsvYAYRF5bQYHV_ldGMU4on8QBQm2q0FYM7kWCrwgP2J4TMqJqjyxXfqJOYa0p7rmA78_fJp_2L-qGXo03whDvH2ABKaA5-3WUBxcFo18G8YEh_rn303AnqQHYTJjCQ-FqikiUdEgFxbkJ5QjX7o52_6Y8UFDSGGLJ2X5S2rFpj1bgN0_W2pkOosUPy8u8ZnKespU7734ApCUfr2vuFTGf2-XhYSJ2jbMUIRnCuebbnbzJ4dwcGowKYm3DAAPnQdnHOUTfompsWWxE5hvoCiaNrSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=gtY8eLF2qP66vZV7-2hOgJqPfRHO6Wt3yhdhQDslolBZLc07hhKAIKLaNzbMMRA_c2sd_JBpwhNjz4Q07V5uxv_tgIsDNYzhOQ0wmBih860L7KqHrUUOQcvHY1vKlOOhQRDrp3cIRddYeFLLETEF28yWnwlpF6pf-z-c8N25Nj5CJuXUUwx-66iY0l6wLnRw7RWthEweiNZXU2EMlZgGs-LzmigHiNwLA-ovyyUo7eQoYB52Uy8_l4UaptI1O57bxOk_LRXkHv_oIy0qzlf_LyVlBVwgQdQIkG9syrui9v_ltSpzf9ji5hzzOd8wB3xSlE0NgFBIuQa8BvaeKjhPrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=gtY8eLF2qP66vZV7-2hOgJqPfRHO6Wt3yhdhQDslolBZLc07hhKAIKLaNzbMMRA_c2sd_JBpwhNjz4Q07V5uxv_tgIsDNYzhOQ0wmBih860L7KqHrUUOQcvHY1vKlOOhQRDrp3cIRddYeFLLETEF28yWnwlpF6pf-z-c8N25Nj5CJuXUUwx-66iY0l6wLnRw7RWthEweiNZXU2EMlZgGs-LzmigHiNwLA-ovyyUo7eQoYB52Uy8_l4UaptI1O57bxOk_LRXkHv_oIy0qzlf_LyVlBVwgQdQIkG9syrui9v_ltSpzf9ji5hzzOd8wB3xSlE0NgFBIuQa8BvaeKjhPrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Z7wOLtJKyjFc8HtaYkU9_qgbqLQZYWdTrmvPv-9VxbbkK6JYpTDgNyIogiHKT3B2C9vwO0eVPtnWK23O1-h6S3___-jHPE-ymtHPqI8dcnBEvco170vd8lwwLLqkY59i0m-49yA4gu17auzFI8aKGPSuXZGw_wcHBXnT28ni_KhsUf8YNHPtMWvA2OAHuTUAkJ9M4S6m_TGx-FNfP7t78oBVgakCYUoBW9sCaAN95Vb4fmokJ8SWfTzkE6TYl53eqYdOV727gRbn-RMcUUQzBog525vQtX3rfF_V0TEnj3qSRNrxP4KmrVh1r-Qf_b3v83PVaNXt-eUO6qqrCyEUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Z7wOLtJKyjFc8HtaYkU9_qgbqLQZYWdTrmvPv-9VxbbkK6JYpTDgNyIogiHKT3B2C9vwO0eVPtnWK23O1-h6S3___-jHPE-ymtHPqI8dcnBEvco170vd8lwwLLqkY59i0m-49yA4gu17auzFI8aKGPSuXZGw_wcHBXnT28ni_KhsUf8YNHPtMWvA2OAHuTUAkJ9M4S6m_TGx-FNfP7t78oBVgakCYUoBW9sCaAN95Vb4fmokJ8SWfTzkE6TYl53eqYdOV727gRbn-RMcUUQzBog525vQtX3rfF_V0TEnj3qSRNrxP4KmrVh1r-Qf_b3v83PVaNXt-eUO6qqrCyEUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNf7pXBV3m9iXvPnOBlR-YV1GrzXdfJaJ0K57u15oQEkBsLus1s9qqMtwqR813ytHNxFnsuNF9fwMkFVw993Q02TXRjZMXnx_yLO1RMgym_5fs57N37K0la4LhZn0TKoMQAMpHfQ2dE_Jg5SKm80fQDsVfNqG_WKfJP-MNC6NpnMA8goEzuOqDdx8o0mi2b_ylLAQ97tSh1DgEO3DF6N_7xsF6GbsERAGKAuwaKTZS7vnvAXSzdWWwXv1JuM-GeIrjpswb_fqKoIiB7eZhHeoIC5uVaXJbiy9yguRcaZgM0w9t6IkcsrW2_9s-ki_OSy7qOSPJrN9A-Zbr8wj6eXjg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qLBJvOt17YLOmBQHv_vhW66-1nMZjX9lAxTpFpiTIRnC5uQPpv5y08CyKLwEWsYH7T9z8LS-umLoyfodfoOWA7m2awuiJnPNzxmbLxyhLI4K9inaF1Lg8OPi86nyQLX0cW6yT51pj1IGTF2iHlvm6KlNvZGF1_Rg7J-PMWV4BZp35WxrqNDxcqQ32VdBdLYXW4Yxrz4LGkuiDw2hREayNupvbjQ_TtDwXJMk1-Nw_obpRAIuX7Vww8ZOkuEUjU6_Y0gg4PicTkGT5YXrfvWh3uMMr1srilA9bHksFoI7pWzJeZ_LI-LMgRwh0ohY18wJx2MBbYf6sSLBkrfNnKFCzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qLBJvOt17YLOmBQHv_vhW66-1nMZjX9lAxTpFpiTIRnC5uQPpv5y08CyKLwEWsYH7T9z8LS-umLoyfodfoOWA7m2awuiJnPNzxmbLxyhLI4K9inaF1Lg8OPi86nyQLX0cW6yT51pj1IGTF2iHlvm6KlNvZGF1_Rg7J-PMWV4BZp35WxrqNDxcqQ32VdBdLYXW4Yxrz4LGkuiDw2hREayNupvbjQ_TtDwXJMk1-Nw_obpRAIuX7Vww8ZOkuEUjU6_Y0gg4PicTkGT5YXrfvWh3uMMr1srilA9bHksFoI7pWzJeZ_LI-LMgRwh0ohY18wJx2MBbYf6sSLBkrfNnKFCzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=ncQL9KKWe6HTXm0XAndbpbAXWLUV9cZjkTA_NGouuQ_4Ibv35d4TeHTw0wI4guCc_DEzVe43N1FrhUIRThAwFbLLdAZBN6ttgxZ2ytIqTRwGVzmj6rQOzb4gR7yQg8zD39rBM38_8It2laucI6GiG1k-yCX-7-3hP8AP_X6C0bN0O0aZq22qCl0EDTPs4El4mJXzsssbTa6QjDgwMOC1HUwjWOJakgJWghmUX-eQDecUpGOV9F5MShgU-6-n0QMKsFkSK2uxQ_226R6jWU80PmgvqJxS4220Va03nmhkkFHsqCaI6lw_YWnBy7FoAIx7ijcJo6CxMJ0TTYpbV8w53g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=ncQL9KKWe6HTXm0XAndbpbAXWLUV9cZjkTA_NGouuQ_4Ibv35d4TeHTw0wI4guCc_DEzVe43N1FrhUIRThAwFbLLdAZBN6ttgxZ2ytIqTRwGVzmj6rQOzb4gR7yQg8zD39rBM38_8It2laucI6GiG1k-yCX-7-3hP8AP_X6C0bN0O0aZq22qCl0EDTPs4El4mJXzsssbTa6QjDgwMOC1HUwjWOJakgJWghmUX-eQDecUpGOV9F5MShgU-6-n0QMKsFkSK2uxQ_226R6jWU80PmgvqJxS4220Va03nmhkkFHsqCaI6lw_YWnBy7FoAIx7ijcJo6CxMJ0TTYpbV8w53g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=tRKeNAvacygltTXNgrIS4ws6PNb_Lc79pGq-UscohnZNGoxwXtHvt-6tYoRFPnyNSTsWwy-juydQk2e9CVsG062lspELFB72awvTpgg6-ijbfhmpP9_dvmEkbfQv6vAndvzzhTdDsrjte1VvFNkjCPHUW46_FrTTtcz6kY6bY9YJvOU7R4S2798QXObzn7gDOC3tFoYsmIqH3YSOXGJdTUMfT1wIO6EIDKDQ7oKuX20Ri1F2LiEfvkK68wn_zsWMNLX0ih9Q86yjxULB35dGtm5LjC_tpOj1NSTpoHxmUQevpMq5F77bjixJ7kw2-jsrJ1DLW7fCkW6AhyfRM68XIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=tRKeNAvacygltTXNgrIS4ws6PNb_Lc79pGq-UscohnZNGoxwXtHvt-6tYoRFPnyNSTsWwy-juydQk2e9CVsG062lspELFB72awvTpgg6-ijbfhmpP9_dvmEkbfQv6vAndvzzhTdDsrjte1VvFNkjCPHUW46_FrTTtcz6kY6bY9YJvOU7R4S2798QXObzn7gDOC3tFoYsmIqH3YSOXGJdTUMfT1wIO6EIDKDQ7oKuX20Ri1F2LiEfvkK68wn_zsWMNLX0ih9Q86yjxULB35dGtm5LjC_tpOj1NSTpoHxmUQevpMq5F77bjixJ7kw2-jsrJ1DLW7fCkW6AhyfRM68XIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=rFVQkOSZ_NXHp8HMIGlJrwlJres2lNxMHyUgVKHgIPLhoEts5M0N_AsEiGtjqzB3_5qzkkqdnhD_NDlGIkmH8FvdJLZi1WDR4rGDmT6XC3bLOS0cNBOfe3Pj9Z9Koi0tpMWMlMhrz_2lnM24Ua3S4vOqF9xWO-FBF15KTvj6zKagVISqrrzQT81m-rsLR4xemqlud484Mkcv8s17JcHh19qE27NXkeZABN_36nKVznKCqCpDEDF2exnnr06z7iD7A0p9emksyxfUxvzsPD7kUCo2w8zsVsw6ERAnUb8-O_qH3hdKmT1MjqwTSrBmlczSK9SzgpHfqecuNfEnlXonuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=rFVQkOSZ_NXHp8HMIGlJrwlJres2lNxMHyUgVKHgIPLhoEts5M0N_AsEiGtjqzB3_5qzkkqdnhD_NDlGIkmH8FvdJLZi1WDR4rGDmT6XC3bLOS0cNBOfe3Pj9Z9Koi0tpMWMlMhrz_2lnM24Ua3S4vOqF9xWO-FBF15KTvj6zKagVISqrrzQT81m-rsLR4xemqlud484Mkcv8s17JcHh19qE27NXkeZABN_36nKVznKCqCpDEDF2exnnr06z7iD7A0p9emksyxfUxvzsPD7kUCo2w8zsVsw6ERAnUb8-O_qH3hdKmT1MjqwTSrBmlczSK9SzgpHfqecuNfEnlXonuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5XuB6WgY1tTz2_uaHA4SirQVX3BNntDYKWAPrXjrUb-lGN-amN2e37DdUira1nYY2NoqrImJuwtthQgn4y_xtaaRS-ZMgwh_f6AHZLzgrFC2gVVRr0R27WG0TrUFfZ1P5FRLEGwQLlgDqmZxmMaB0sMr8y2sFc6lilRmrOwL5e3WFBRlRF_x9O5bTscuVO2isBjUNSg44w6NoB_QvOo2w5qz_xhT6cxVsYuzBwZydJKRjMrY7IGU7CqVyMFtHWJHwFtkNQvG-Q_DPg_oNOiuKgYIjdnciJz-_Yy_9mhEVBaMBcysKLmd9nyfKXFtxSSpRjopSGIrbY9QZ1GrPw3zQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=dtif22ePOp6NglWpjVW86v9dJArfdBaqPgiu0yQEQHBJlDXltohdRgINT6_r0dX6jNjMhBJjCyvehwdnxCzzq_JyAhOG_a7vq8thbEd_RadoVip0lRJEpuuWkmBRag_KrmTyqg-CX4mQ1XH9RwmQM76bpFsPFHiRxYeuCXW3Qx1v1Tfx6lk8kvj6Vntj20ciDSrhF9ucwrw0niTOTA-pbdEkHPA-FWXl1jLjoztUcnh9pflNgBoq5zdkRT8oyqzern-76izgJoMzJbBSj6HGXTsy24UolZsT1tadRAYZHANMu0SVTeunZudEZm1fk2kU6MsZFvq1qvXyX0jtRkFf3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=dtif22ePOp6NglWpjVW86v9dJArfdBaqPgiu0yQEQHBJlDXltohdRgINT6_r0dX6jNjMhBJjCyvehwdnxCzzq_JyAhOG_a7vq8thbEd_RadoVip0lRJEpuuWkmBRag_KrmTyqg-CX4mQ1XH9RwmQM76bpFsPFHiRxYeuCXW3Qx1v1Tfx6lk8kvj6Vntj20ciDSrhF9ucwrw0niTOTA-pbdEkHPA-FWXl1jLjoztUcnh9pflNgBoq5zdkRT8oyqzern-76izgJoMzJbBSj6HGXTsy24UolZsT1tadRAYZHANMu0SVTeunZudEZm1fk2kU6MsZFvq1qvXyX0jtRkFf3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=MsZ1UaSzE768oRoBFuDWi-BgjNf4sk0qCwLtZlx30dim3RRNujd9UdNu0AsqqLRjt3B0f6MOdYVUav__CqNHS0e5C01_BDUsXsQitA5JsCHtDRnt5lp4NdxzRsCws-mXz_1SNRI7luZvqpKRrAxp0TzIBTlK3VKWcIJrn2wBfIoKC7V4xwE_7lXYjs153FZYNNB-ySofZRvKv0gchujXt6cEK3o3zDLyvPY4klMvVDxZ9oFckLlLqfJLVpjglkS1C6ZWek2wRC5kKFt_ZY_svkmidGmoJ8dqbmIsxw2FRYlJzjb2P8oOq_QBPJczSOw9nwJK4fbvuAHrSa2UgA0QyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=MsZ1UaSzE768oRoBFuDWi-BgjNf4sk0qCwLtZlx30dim3RRNujd9UdNu0AsqqLRjt3B0f6MOdYVUav__CqNHS0e5C01_BDUsXsQitA5JsCHtDRnt5lp4NdxzRsCws-mXz_1SNRI7luZvqpKRrAxp0TzIBTlK3VKWcIJrn2wBfIoKC7V4xwE_7lXYjs153FZYNNB-ySofZRvKv0gchujXt6cEK3o3zDLyvPY4klMvVDxZ9oFckLlLqfJLVpjglkS1C6ZWek2wRC5kKFt_ZY_svkmidGmoJ8dqbmIsxw2FRYlJzjb2P8oOq_QBPJczSOw9nwJK4fbvuAHrSa2UgA0QyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gjdj2w8K6khH1xB0T_3aeXq6XIdPsIyJb9LOC0U2elq0frhfMV7XrdUZq1geUGtmKMeXbGnmVbse6saWv3i7rS7kLg8a5OYw6173G8YvHzGV4RXHOJYWAk172_QYFZ91Fi5Sz62SWjsBF-eXcJq7PbeK09Z_wdBqO4X97ytjONfUF5fAMi6ieT_QEq3cArSFB58rWzZ-2MaSHWvs0CwDcsBZLAxyIJbUWkzqI6GpAbEgN3m2tzA4bIpwpkWGQGc8wtyXAKRZT72kAC7UTUE17-A0htCCF1IMO8pTTJH39y98a5AzEt1AHGiGxyTLfo68NwsBC2yAzTdwaoiMEd9bHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftJbIMrWJaJUKKQxtAhySBMSq3EPPa11JC_VZPed_JFAz8sl_O4tjuAUe-Ufhyw_rmNtbnRqbN1rVXdFbkORDgDaweeKUD_M8ePeAhzfDxBZE59spZLQoIFQp-yPH-qJzq9EVoskx9AvFGZHFhLRnTViPARN4RKvA2vYRUzOyI9fJtG7827hwMgECl46WyHQ7qQrlTQCb2LIpDAP9lJG3I_1VMmaW9pcAD5snml5zdnYULjw5bN_SXOcea0VrlTCDjJyrjk2bIrwfhVCNYv83itUVqz225F8VINdwHkE6jauAUUmK-bdMoQ0dX3jJtIMnyt7CC0VZhvPTTIF1IPnCA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=iCdg8e-zLo5-cccn_ml1ypOdrrwQaISZLfXzOT1knWoO9n5VJMxlC4fsQRDXAuKyJ0LmehKgnqBaT_lzcu__AzlLPoi4S3AjDZbKEbGz9Tiza_pnuS84ovWpnr-5DxN93bIKvnUNEDybtxMsOGgeO01nsE9SzshjTuHqHmvaB-avN6A6KqxJTfSehyIJh3pZVojtPQCXJcGWxvwMkR1C_6SMq6klQq2SfW9Q7AovQUfu3MXA0pIeR8mYDw25EFtrdQOU-2mWAov1ekkX_78Bfl0cwOTaDRlR7FuU8xq2Kql_j4HpJ3oqfTLEZrVzLpAaDDuYiIVClD_jYSokSofUxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=iCdg8e-zLo5-cccn_ml1ypOdrrwQaISZLfXzOT1knWoO9n5VJMxlC4fsQRDXAuKyJ0LmehKgnqBaT_lzcu__AzlLPoi4S3AjDZbKEbGz9Tiza_pnuS84ovWpnr-5DxN93bIKvnUNEDybtxMsOGgeO01nsE9SzshjTuHqHmvaB-avN6A6KqxJTfSehyIJh3pZVojtPQCXJcGWxvwMkR1C_6SMq6klQq2SfW9Q7AovQUfu3MXA0pIeR8mYDw25EFtrdQOU-2mWAov1ekkX_78Bfl0cwOTaDRlR7FuU8xq2Kql_j4HpJ3oqfTLEZrVzLpAaDDuYiIVClD_jYSokSofUxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk_4OWxLH6r_2jr0vATRLlC0wywci1Cx-fLDV5iFz4Kn7efFAtVentjG8rKV8ASqZzJwh3M4of41yC1mE2ScD4EMT0A9aTQbK4oR7rmZ1VOCmPCqXIQ3nALWLOCHEls__frxxcZO9_78xvVFy2sz0-SZ-PIHMIPyPhLbRWFD-qd7FN-3mtgIJJO4xYfuQDX58WnvIGVI-PcYkxzDsM4WeAsVQzm3mlblaqlH07HGzy3ax3HfOlLCoXoxZA2kyADtRQTSzJ1l6qptEx8Da80sxMtCmpGDLfwSl_sNNrEjhgb-EZTEbFzGElc5K_oV84XH_U6hmNU-FiOOKiK1pwJsiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DB1jw_aaYy84IwQ7zKmfS9fmIakYRNECpPe8SUi46-sBQbEGLfCvpIUUBVF9cvUODQLRiVtOI_AjjZ4a31oFWDjYJSpy-JHQkBnQmVjxh-PBBYCdZR_f5FupqvMXslYUxSZpBM8xHL254Aw39yu15EcHeNYP8g43S_zY6N4gsnMYzD5p6sNYwImLTWZ7cYF9ytN_JxhNm6CXvPIfO-w73OdGnuukXA1UYm_0UzwxnHYrnQ5hAKmLQdow8cy9RVlMQun-dlHxNk9sYjy4BSC399AhI4rgXR-KgfF4uwaYOfuJV5phEstJHpoRIF4yFn3KOhTq5I0KiSXwRcooVDDbUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpxUWsyvazQrhV4mx9bkBL_a84RucoRv9dpzZ8LdPfxJLvQ18nI8xPJRWNWbX6csWtbfF7L0aDHVCkA2CItbCLQGzGXclo4JN58e22dUrBfjdTw7Fz5DtuuN1YYpt-gooy7cWJOWcajlbOW1JdEQ5Zg_10Q6rl3ZhxqJjUvQAt5-Im36xIDhmXQFZ2P9XRwcwS9yXh95XnX_FcNp4F8Vj0E3uoLwEYzo1oZZlEAW8JGTsGPz60U-z2omHuTo4l32H1IjN2QbnqqGXVvlqmHDYYeCKJYQYY0r0HhYslo2n0g0m3aApcKD5-kUvnOnDgcQK36aANjGGYUqgZswHYupVQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rnjOUGL1rXshjOPtz7EBc1TgzteUMJCwEXQCU5bYT7PZjeeaWcvj6kkv0QOA2oMrfo5ltfuC_hfy3ObAkhIjoDKvRGPLRYOGrbiwIGhtnD5dJuUGkm_5rv3jywEhWgER2Og5JDEXjpLKktgveKwzGKp41ohmNINUpJ635-wdclHPCLToOZ-e7vQsjCa0HXvDMrKcxhVTIhRhsL1Lcck3S2q-NI3PwY1-bJoneYiN7dCl5Dwotvqa7QbL1YLs76f7T9If4JvoPAHrXA2FGgIkzm5iVexDtuCKqgo_ipKXZTSxhJfCrvTmCJyu2LZb6Cecoflg5gqXDZwChvhty1GWVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rnjOUGL1rXshjOPtz7EBc1TgzteUMJCwEXQCU5bYT7PZjeeaWcvj6kkv0QOA2oMrfo5ltfuC_hfy3ObAkhIjoDKvRGPLRYOGrbiwIGhtnD5dJuUGkm_5rv3jywEhWgER2Og5JDEXjpLKktgveKwzGKp41ohmNINUpJ635-wdclHPCLToOZ-e7vQsjCa0HXvDMrKcxhVTIhRhsL1Lcck3S2q-NI3PwY1-bJoneYiN7dCl5Dwotvqa7QbL1YLs76f7T9If4JvoPAHrXA2FGgIkzm5iVexDtuCKqgo_ipKXZTSxhJfCrvTmCJyu2LZb6Cecoflg5gqXDZwChvhty1GWVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Hu4r35K9kYNzYgZ2JhBSyvtLjSyXLTJ_rOrT9zZCk2BYiiWbyd67WWTDf-kBvP_lpwuBw-HV00N6cCMZdPh4FkRSGxMk2G3Bjyh82QeRjIKcZ5GdqolLwWcaKeGmVASGGLNO6dnVguTIG7gQDUX20sgW4C6DeGVMdbuFDJF9C7gpKdWf5_oJSRr4UxGQZ68XtWtE9H9rrjOq9c3N7ufXbQAJshOmD3gVjGrtsoerkdz2t3AWnDjGxVijwFKNFqVV0TxMvADD2TbGU8ajQL5Vg2oVR4zRJBMEmmpiHcWDc6Qc7moJBC-UstkBGdV0xbavxltU8TJ9hc4vKUqmklcDEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=Hu4r35K9kYNzYgZ2JhBSyvtLjSyXLTJ_rOrT9zZCk2BYiiWbyd67WWTDf-kBvP_lpwuBw-HV00N6cCMZdPh4FkRSGxMk2G3Bjyh82QeRjIKcZ5GdqolLwWcaKeGmVASGGLNO6dnVguTIG7gQDUX20sgW4C6DeGVMdbuFDJF9C7gpKdWf5_oJSRr4UxGQZ68XtWtE9H9rrjOq9c3N7ufXbQAJshOmD3gVjGrtsoerkdz2t3AWnDjGxVijwFKNFqVV0TxMvADD2TbGU8ajQL5Vg2oVR4zRJBMEmmpiHcWDc6Qc7moJBC-UstkBGdV0xbavxltU8TJ9hc4vKUqmklcDEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=SXVHT6Fiwkx6H5z63O9n3sC8X-izIT0oYkh8f6hhSXmCm8EuYkfJ6U_OdVmaYvAZYt1_5U5fSzwsFaE-wQKYFyNMuLRA22qcW_vE9k7-JPJIVHhGt6vBnQX47kPmjXdlXctD-NGYN8mlEp4DKOHLcx8ASFuSF0oHJlNdYvKxCJtIZE78AjouaVhSPgpDSAClPHqkIlWJ0fvAD2Bt5KKUd4P79wzhUxLGlMCJ-bOFsAQzMDb-BYyXa_S0kvROMabhD3aSjE3vGRkORzcdR-t4BU4ZOAtuNf5A8duFZmC_5060hUUfkcZF8NDAwzA5pa_8YphnK6T4d3KGGsVcCJU3jpLU2UBVtc5DuRZ9Dz_yEU-LG0dnma3v3orIJAOyD0kVc1zxcBZb42MMmtY_Ovx2MPQ0li-jtXHXjX3cdRYA2HbF1mIoarQNJ5sPeipqjELECfRpZKx89F2rLoyAaOSc4CFPvdQBpxu893arzyDZudeDUGyfokkEiADR4Gl8MFBd-FF4etOW0Um4joqvA7bFxnLW6acVoPOucAChHkgN326crRtmRFqrM0j8eTOq-9wZzTJ84MlDivYPSUpNRah3s3F1vrpLdLvJRPXuexe9MWr08cRVCV3O4fYEm0H4S6bVFOPt5_ZqftgICmzYElBhhDgrKoGiqgFcGx2TqtWDFV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=SXVHT6Fiwkx6H5z63O9n3sC8X-izIT0oYkh8f6hhSXmCm8EuYkfJ6U_OdVmaYvAZYt1_5U5fSzwsFaE-wQKYFyNMuLRA22qcW_vE9k7-JPJIVHhGt6vBnQX47kPmjXdlXctD-NGYN8mlEp4DKOHLcx8ASFuSF0oHJlNdYvKxCJtIZE78AjouaVhSPgpDSAClPHqkIlWJ0fvAD2Bt5KKUd4P79wzhUxLGlMCJ-bOFsAQzMDb-BYyXa_S0kvROMabhD3aSjE3vGRkORzcdR-t4BU4ZOAtuNf5A8duFZmC_5060hUUfkcZF8NDAwzA5pa_8YphnK6T4d3KGGsVcCJU3jpLU2UBVtc5DuRZ9Dz_yEU-LG0dnma3v3orIJAOyD0kVc1zxcBZb42MMmtY_Ovx2MPQ0li-jtXHXjX3cdRYA2HbF1mIoarQNJ5sPeipqjELECfRpZKx89F2rLoyAaOSc4CFPvdQBpxu893arzyDZudeDUGyfokkEiADR4Gl8MFBd-FF4etOW0Um4joqvA7bFxnLW6acVoPOucAChHkgN326crRtmRFqrM0j8eTOq-9wZzTJ84MlDivYPSUpNRah3s3F1vrpLdLvJRPXuexe9MWr08cRVCV3O4fYEm0H4S6bVFOPt5_ZqftgICmzYElBhhDgrKoGiqgFcGx2TqtWDFV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=J4Ze_Vt8D0MPGr6_CcwvYy5qBO2Gcd-ToTNewZUYB11IEJeJmvibu57QA1NbHvz5A-QnKTBQ1k841gGVlQmp_lyvKlPjqAA5SK0e_uNBjC7FaUvo1eZalshvxvdJQjR8tp_VmeLEQmD62hVHX4nWnnOAW3MVmUszNge8hA5FHdFvEs3sLxGwT8A_-6Zz7BOMtKyR3Bawm7Ca8U4gQ_blsyC8vImcTigsd5dsbKdsb4FBRu9hw1oTENMqY76ud0SEVInCNV4V61GcjHJU1zH672BUgCLOdBvsH5EoXIwopHQGoAHdqmITueWjXSNB0FH_Cewof5lgR3cmRJ_jwAzSwVL5AHiQvd0fBdFsexbMPUrqtaxotkLJRozcxKqgME1hjz_ElK0jSTZpKOUU0Ofa1Jv2gS_DMncF4U4RtfBUH2u9-1GKDgnzwNFyl8gJSmRSkdvzZTRuFjuHbQtj9nZIEKDdZFx4TVeNtLBHsVwMsxxainK_EgC2Dy2evsSlGnIgmS5XJpAJ_t9ZIW3hA6StQ9V93nx6kvh76801NAF7d1i2xZ0ou6EqXqh2egxz3LSolZSqeqKxwhG7LVHw5pmA3iWdN1KQso1BpGGBSCkoYtcWlj0z5hpktCPwAI5B92ph4zz6wY0SMhiWAN5fyLduwKZ79x1NJMwknQMSSGLJztc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=J4Ze_Vt8D0MPGr6_CcwvYy5qBO2Gcd-ToTNewZUYB11IEJeJmvibu57QA1NbHvz5A-QnKTBQ1k841gGVlQmp_lyvKlPjqAA5SK0e_uNBjC7FaUvo1eZalshvxvdJQjR8tp_VmeLEQmD62hVHX4nWnnOAW3MVmUszNge8hA5FHdFvEs3sLxGwT8A_-6Zz7BOMtKyR3Bawm7Ca8U4gQ_blsyC8vImcTigsd5dsbKdsb4FBRu9hw1oTENMqY76ud0SEVInCNV4V61GcjHJU1zH672BUgCLOdBvsH5EoXIwopHQGoAHdqmITueWjXSNB0FH_Cewof5lgR3cmRJ_jwAzSwVL5AHiQvd0fBdFsexbMPUrqtaxotkLJRozcxKqgME1hjz_ElK0jSTZpKOUU0Ofa1Jv2gS_DMncF4U4RtfBUH2u9-1GKDgnzwNFyl8gJSmRSkdvzZTRuFjuHbQtj9nZIEKDdZFx4TVeNtLBHsVwMsxxainK_EgC2Dy2evsSlGnIgmS5XJpAJ_t9ZIW3hA6StQ9V93nx6kvh76801NAF7d1i2xZ0ou6EqXqh2egxz3LSolZSqeqKxwhG7LVHw5pmA3iWdN1KQso1BpGGBSCkoYtcWlj0z5hpktCPwAI5B92ph4zz6wY0SMhiWAN5fyLduwKZ79x1NJMwknQMSSGLJztc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=aqygYOntH-8s0t0zFgLDb11rQgb3Dtm-MW24XcafLoK276ox_JCNJFiGF6c3mmxGSdlPZ06NrqKpHRhuWOq4fwhq5V1TzJB0j9K_DQCBCq_FEF0Faq5E0s1UT4OlB7N0CuxqXhUuO77MK10iWjPJqD0RRA9CPevPRt1UGw-NBGHn9tO4LZnGxasGH1cx9-F4u1m5knpsdBG9_miSGcapJTS_ckmygnDFkNXwGH7yJ5cY3M6IODwQ4mJQAWSLfTeDaMNnj7XbnB24KJp8JuP77ynzmYqfw92yGkMZVHHuZfy2Kfnr2Jd-CeuiE0STy1jFuyl0YGvDl9PnD4C5urn9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=aqygYOntH-8s0t0zFgLDb11rQgb3Dtm-MW24XcafLoK276ox_JCNJFiGF6c3mmxGSdlPZ06NrqKpHRhuWOq4fwhq5V1TzJB0j9K_DQCBCq_FEF0Faq5E0s1UT4OlB7N0CuxqXhUuO77MK10iWjPJqD0RRA9CPevPRt1UGw-NBGHn9tO4LZnGxasGH1cx9-F4u1m5knpsdBG9_miSGcapJTS_ckmygnDFkNXwGH7yJ5cY3M6IODwQ4mJQAWSLfTeDaMNnj7XbnB24KJp8JuP77ynzmYqfw92yGkMZVHHuZfy2Kfnr2Jd-CeuiE0STy1jFuyl0YGvDl9PnD4C5urn9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7TMSYBqBsONQtC53i1Lhi4d1q5gbebPVnNrPOyXv778nevzDX5cWw62yo-jc3-WEDEzzUqyXQTJxWbon1CWTQ1NYv2am8inZNLiOcZv9oeGkC-7tI-JFpDnxFp2kXSi8fb0HdPKud2_3eo0Lqhz4bbTbkB33gN40IjLYpxGSp15VId_2ljvkrBFn45Ghj63pa9BSZQMkHwtxQ9xeXYUbl0QkPqLSDGIZ_LmWP0VSvHxXZrPjDXoovKlV74tJjwxVDQHLKj9YzxMTswndJAmyjpLyBzSNxdfuFyYQ0cDGgJX6ZtYe2wVAOoF94NLiBiWplVKwhrM2v-NeLYXkEbQ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=jvMTRG1kXx9E-d5qjiNBqJ9Md8IewBQnhqVrIwcTLG-wldZqsur5sa8GuDjFF6H8jwF3LAF7iJkKluwUkhiOq2KMfqJNG6xm0qGeIACiQbVUfDgFeqj2tD4mLaXaisR7PdB4V1RcvxdafnWwUGBwElR1NMf214qlm9RrwYPIywqSyQQMx2TQFaSFLuTw3Bk0ceeqtnU2gxhxiY0UA0r0B-qMUrWuc7YMIPR36XI7CYNEIA_OIVXO5ZrZOFPqqst1LkeVxDQBWtyikb7xZTUjaGq-Ui9WVZQt8fPVB6GARDimzI7XXu2l1iaQwrkU90MZLaTmFxPJx0SesxOmTTCNFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=jvMTRG1kXx9E-d5qjiNBqJ9Md8IewBQnhqVrIwcTLG-wldZqsur5sa8GuDjFF6H8jwF3LAF7iJkKluwUkhiOq2KMfqJNG6xm0qGeIACiQbVUfDgFeqj2tD4mLaXaisR7PdB4V1RcvxdafnWwUGBwElR1NMf214qlm9RrwYPIywqSyQQMx2TQFaSFLuTw3Bk0ceeqtnU2gxhxiY0UA0r0B-qMUrWuc7YMIPR36XI7CYNEIA_OIVXO5ZrZOFPqqst1LkeVxDQBWtyikb7xZTUjaGq-Ui9WVZQt8fPVB6GARDimzI7XXu2l1iaQwrkU90MZLaTmFxPJx0SesxOmTTCNFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=XbRkbr8rEjALxOZ_LeS9spvOQyaA9WcOIxDarKbcPBkyPZNxxcWIbNX1W91CXUCuj_AWmDK13jzHleaDbcNKxCSWFTvIMG08kBZFAhkqER3kEuCoFs1n098jdeuW7eauK9yjClI-ONic8fZZTYsov-f8wgDTe1ErprVtnwiSQIfKrje_0K_-xhr18jT3v-PNTGCg5rdVvIM-7CXbgXma5XXo_QZO6UgJ28oTUpDz5tFP2mz2pB39n5iAPWB9DdD_rIOcnpdAG9J-do4tQX_49hQCZ4eJNhjwNuIp-kC_TXs5dJnRf-3eB_tDPbHjXl6zKETuie7jMgOM6WNn-yZlYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=XbRkbr8rEjALxOZ_LeS9spvOQyaA9WcOIxDarKbcPBkyPZNxxcWIbNX1W91CXUCuj_AWmDK13jzHleaDbcNKxCSWFTvIMG08kBZFAhkqER3kEuCoFs1n098jdeuW7eauK9yjClI-ONic8fZZTYsov-f8wgDTe1ErprVtnwiSQIfKrje_0K_-xhr18jT3v-PNTGCg5rdVvIM-7CXbgXma5XXo_QZO6UgJ28oTUpDz5tFP2mz2pB39n5iAPWB9DdD_rIOcnpdAG9J-do4tQX_49hQCZ4eJNhjwNuIp-kC_TXs5dJnRf-3eB_tDPbHjXl6zKETuie7jMgOM6WNn-yZlYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWag3MrWOvXXNvTkm2ZycB-QVnzja_aNd9ucRcnyViCD6dX6VjwnK8MCURjbFcV0nO9anBqqAGoGnblkhRiz-i8ThBbNBjriC_KJFdSwnPfNaF9NHhzzSFSXb_AkcORB-EjkOUBz9I9L0qsOpgSvY0rI0Nq6a3lNWL7E4fNlrXYynF5SmEJ-A3Dh006nhVv2bHnJcIBpfSSHFem8nQ5wLiWROanCRopD8F3Ttg6KQyuZzfeJO3mH1e1qv6ai9hVrmvWfXw2arWTn_VB8-P7LsN3Egr25Oj-VJHhCKLvK-i3Edmmm0I09eb3mY8N8y7R0AZdR3RvABXc1PtubzhkOxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayVFPZDlP2iEcrH8Zoj41acl21EqvcFCXVz1pX69k0l6VGj6hDWtoEbuvnSRXq-Du2g5pyw8vTCSQYZItxz2UV1ig0URGUnTwZV3tIq6M8iU3pVJu6bsH-VLi1bXLf2WJPgGBb18uGi5s3iKtcz6n3TCtlq4xlvbZq-NTSHpa2xSZuH_x3PxpAmOaGLb8OXKJf8ATfUyr1paTGKWybQ00wP25fhyf8eX0wBfTFc4vZEDkP7StE55Hb8w8Cu_2cdbF2V2Z1LoajGAzHnOThQC00BMAi0vLLCviSLiUYq55RZrWmsHqQbr4zFzk1P7-hCcQAdk2WTgU_0nBKw2LQHUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYFA_nOItOk496VIcSZoXo5cNpstlhqhHzWqpj7y71rlXDzqfXE9Ye2KVWhMirvq2GJMjC8PAMxxGL-FKKUXLlOT1zjceNECG8GXCwacb3DduKAtwXu3pITZipvpfGPcPfBOhIPUdUJrDPd_2OV9-6BcSk2w1ihgj3mOFbJ_X57GM8bQLO13eCqnRDdxW4vX4V_3_OZrnPrhWvODkuTyt4CXJ3-3gxCfHET-eL5P-ldijxrQWtWZFWUBqHxK4am5zl08RzEbPsyw8IL0wzd9VcrDFYd_Uz_UPSzGbrRYtfa4hZzIOaydDDXKUnotXCkKUMmwv0wOEgsh7k0n_j4stA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ba_0yrSykBUs9Du4Onfl1x6XAlEfxHWr6OYsM5d-EG_xnwxXQRtLtqLOqrZ8JXOn3FL7ySa7rnB2dOW4hX2ulMbOLzBNybrqe8koUli_LEfPKt8o26-seSa1bWIgBYezkKV9ng95sVz6ODLqfP2hxC5RTacxw6uB7xZqvIAEt23pg1kqt_m3iF-IVVDDkiKyGSfmg5YyJtrlcX5H2oP91lOJPvvocnDJ--HKGw1MESbo_74W52umXEdsgdmRXZcTtFxKDAMg8nGQN8Sw5W1Cc3SC_LHO3C0XnG7mfVntDKGlgpQ5I_YjEZvpoNZ3GIBgPipyEyAWPauDbzj0WKoudA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFaM5zWRqesk76mJ66PZpgkLvBrdHvOeKyzJxXWQzSvzzFs6SSUctaPfkNAHfv6euZQxCRDxX1nHPn9hjyaGDsjNJBNUbwQV9iSyRL9xcTw9FIzxtvZaP4hOs-AmcjKg44kGuTPzCOvMJy1f90lMnfmc6PdQiLS9XLiXpRZ8t9RHbyke2mA_vpzhH7VxBuuB4Lr4uLgLgwUFKv8F7IYo90vnXBaZslRRlX0Q8JJRCJl7eo4aa0JR-x4H-eKQI4yBIjoGD9_xAHmlpfvx_mMFX7wBqJ84a8nXaAjnVfafl_rmbsnVHiuhTHG3u1IJvAorGJ6-o8gv7f3T4GHyymmUwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SowU2NYTsS7c_XbMpvEdGLKYImJ1KWmcTJ7p1k9Gse_qTkGGXXRzBlpmGXTa01wVrJKHWzyBQmzzak3Rg9FYO4hxVyFyP9nw6D436wDVLDmb7DkComKOeM9aXuZ0NWaIWabAxTvx2JN0h1IqHgow2pSi_LHU7AlY0ziQGzoSqUZ0dAb_aQdGxFd4EPC-gIYtm9eb8OKWrBGk6Z4Mpo_Kf7NaQsIu36JIvqvLsmBK-kYB9ASP62of7p8fFBnKfCwmeKRkVMYcuXgE7HMsg7F6sg3upTYlBubzyU-hi7GZwUnPc18YVKoOyJyCFnErP9MKSsTGRzU-i-nnkF74trvblQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpQp0PtGRePtrVL8BvS6-799jpNi88LHDqXKagcoMaRCajKFxNf3mEIkb8tNh0_juL7b3d62cK0wTvqFTOlVlF7PQIHZVU1xOylrs2Zc7jNG7Hu7B0PWXAv28M4QtjFSY8sFjUnzeExK4M0YKQMBbomV3GaGSk0_3llxdwOe6U8eepxxqxiH85mFE70drvc21SsE9N7gG1Xa4w7Dz-OQOpMHRYgHHshQlJPYHFMxsccxs9mVkGSsENZy4bbUUOJKQLcWKz9jx4rS-0Dum8vGPMA5ueuQGjkIn8ZFxinzBsinSueUiHSrYQ581gMj57ewDeel164vr_zaivWFOmEzng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwQX7DGzH8gzgWB44D8GChQZ3GQnjOEGMTeipD6PoMbVsYa1PJhY5WXmtTzR1hxpIcBAo_XT3KP6bplvR8MW4NEvn9OMUnEM50qUScZ_av8GCo8Ry_JiinQoxwH29vy1XGUFo3DulnCgOvzUoT_J-Eef2w81EGnn1rzGS4zqaQYOfRM54iyOg6GNnB7CALGIUlN8ZQMOOyQ5mWBaRNZc6DhZraL4VKHfsFj3hh4YfYBV0SIvFia3Krm-ln_vjZO_hC7Oan41KZUcR9Oh8FCuTrhbiFLvcyPtMCrbyKw4DU5tOKc0-M018Sk9KlUeD5mkt0PjBzAqkkCvCyzPlXebMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SCVkfu-5zcbLuXcj9Lx8LfDlIB73Zs1N5txPdgX7Ot80p0AqXhhxVh0P9mc1126hVoyU2wz832xiPblXV43mFY2iij5BH6dPIeDqkNgzO8JZYFbfaHv-ZxqNfKCL28aQ7AgqOuhEPa2s4jznTMApCVPiDdD0R4yKY1JBaoYmSC5D1ykdYxLJIP-5VgdOetK8wGAha2Zo0FoiQSVheRSok29E8ZOB1doWIlglVx9aB6w0nRicZNoJhApdFiFDOtc-VGwtLC4giFJBLAHCqPshV9SiPTweAl_vsblVe8KWiSX0uzue9Q9LVFyjQAO_DYul4Et8idAIfXyx_De0e2ALWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fD7sPZr9YonBCbAbFHSrXnXCYhFyWi8IJLETUFw5aR6SG_h2YForEw5Q1N6EPiKvBIHqL50EQQaJHpjnpdlsEdD9zLJDuPYV8oLhGy718w-PiblCpihQS6l0vD5gpgTThfy20ODwEDjSyRbqbxwsFFGX2mayRkx3a6TO--cVpWqZN49H-VB5gLZcMIsYn-fj_TKEWX0WaJ7BkWGY3Ko9SxbGxl7vNDvRlt00VpedqydHn0v7oKDhPUl_0jG0DCZMc1j8D9v2rFCIZmb_z4AHUmPgoLxz0T5YzSRGLddFTvYGdIXrR1WFTiTnMWRotJUVxAOJLmELblrOrGURIytaLQ.jpg" alt="photo" loading="lazy"/></div>
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
