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
<img src="https://cdn4.telesco.pe/file/VhX5BUOlv3ZtcGgtiB_Ja58wSLX2xQzC_Y_h8BHimUyim00q8aR9ZHR6ht65msNdgeX5t42-XxhYlzjOc43WRRqtNsOEetU8kn4jWL6MVm2C_KlinlHTlwgNkAqqJzA9iX8dza_hdbvBwRtWISSzQX1dL6uVSyhod3EV4rLrTuk6TvjgJLF29Sp7OB8c9Q2UmKjHUAp05VTPpzwdrUoaGo_B3HJXM0nGdAY5gZovQPPni8U5MzbTk8MhHys_FvVmQetcHWqB1AxqCavYgwdZvlVc_z2m--FnKzmvupiFUGnjV0iCw4m86PxCvZXvyiAv4W3kmbjndgo4jhMQwof73A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 06:39:04</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdmttvCvkjPut4MmtPjCdR6VkrrVjppZZMJGMajbNBT-4TmeKLH09QcInaI0pFOnFPzqKKKIY9WhcLW4isTMkCwYrVn1U00IvwK4ZCNOOahZvkBVbe2II8grqEtohtVAIbA_RJtx96d1_AiCnY9PJC14amv-a-gV_iFIPn3g_su1eXuLgUt5JVpLtK8mDGbBvxBAQR1Eumbzf4VPKw1q-vqPYeyU0rSMT9Lponr_PEQZ1JLFNvqgw0vWmGQSwTjJJqBQ1h4D0etORADB3KfXRUbUEY67VfGKVhnU_cbCTTLWeiZg9osnSsBNe07Wkp0Eun72bRPNti4uL8vjxUQt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YE9BVZBJoWkUKTtdpCjZhRL7b9xujfoiT6ReQ7yhHUrIz58uCyQihGHa7JOl8c-ASkucBMrygvRbDGb4QkL7aNhllH0Ql-XhQYWRUyTafnwZqbkQ_rlmCoCBxRJHvK5dVOXYcGB0wH4zPhJeqoQCxPi11WHTdbh1d7FzS048vXHJ85tydxLFVu7lT3Vp9Vye81fYj_h6zEfu8GCRplqLmsVbrxwuJTrlYJXBZvdl_PM4tBHF9iGptSbPtNMEOSlGrBCWn36mfdP-Roky95TL5sCdS8hARWsm5VZMSf-8t_yK54h0BrOKjoPMec4i63ChlhKSnM3nKo-dWibmAzWO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAPSocpFObkt1MUgplWWx8XGOM5L8Y8ScDY8IMHswscFwJDgIRBKmbWnGWW7F-Ude7XCLcQr2IcovB8ty61dStubH7Xp-AmxGMZW98l5WydpnQ8vZf-jmuLQpKPpMi-7468ZEFbkISg5JmDESsC0R21xBH5jtZFGHkIhjUZ1uC4jf15gPqOXxKtdYCTphcLPx4oRIeH0VCOzdk4PJxexMEKEELbz6yXRlExNaTg4j9S0UMIZx29Mq0RmDcUrSOS72yTAOu8ej98rq9gLDfKV55-flKj3JcgnxLsvLzNjaxN2j3zuf-PptBGPetGE3kkGC93-McTD2g083clmQ6NDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO50nJEJIvYE5pMzI5IW9QDCwM9Cl3_kSFkgPuMuWUXnP9K9MLuuKbOdbKPz1wxj5efuAFWID9KvYKRXhVSNgFS_g8Nxoi6IL9EHOUyGDuUyx9ZBXDTVZnmKpC607AGPdgSrCszMnbiLmZrutqnSVuU8ZBAyUevD7ynqPBpmszTqkGRiRbGv6EkJUHR69mJpAd8xJtrNomdKke8dPx4PpYN626i1JqbvHClbPGTvo0BCR97ZrZBfJ7BEANVvKKtcR9BfUD0MLNvx6Dq2ZdS_nFqYewWN1rw9GKiPBwK_xKX0ek0paSmzLjznHXDFN-ahMr6hYDUr1zz1nQpMN4OaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxC2mpdAok1zvNECl5tm6Jq0U7K9NKoktP7VZKWe21DJIfC_5gciGMu-YpLpOyQC6wLLBBILtvBRF6I9ZmEOY3ChQLkUz3_Ypv601OVy7bxQy_Z3k-I8ejdjOvadaAmT4ipPXfF5RKyZ7ZiVcbDeBf_y0RZxL0juljYwDjgNeQxRTj0ShvejKZ1c0wtp13kMsKNI1VJSxrHMB2Dj5kV-x76WKRIoSqSdhEhKy7Fs89f7MB4_f8yDiSfUrObRUPd6I40h2lEXKyoG7S1hxfIQIVyyrcGVtSpcn4n6_uzwvgtSIqSM8sVV6itMwTO_eo7855onK_e6PE_qyT0bOupysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMAa19cw3HO0gru0V10RtFSTfd8QzC2tQPzLOHZn0JnU1Zy9o3WehVfMLgh-0aV6DThsgdzJTLjuH9LA0LRDzWxatVn1vPNX0z93Lax8vsJSuGGxAW_a1uB7_Kd7aHa-KP_vxUe1yEoBQWFfs_tPyQFeJKkXm6fFON9J3aZwlkc5EPxsQFnm27TgElIJwb8igVZMaID5pusagGsw423yn4s-IMlu1M2lGl4NwkJc7fhD53qOA3FB9dhZ2YMlUZJ1SGitFbhi-VxSS-87ipMK-ckko4OI_kia4FVaim6cjPRSkHvgc0bVCrFexMksCnwZlX9l3LytTvuSCkDBHQENbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=lvxI1oLSETAHG0Qi8Cp5i9ckAPZzS2xeqAK3QetbFV3Q4aSKjzg45eK0dMBuSW2Ajp96x4w7mXY0OpRlaye7JldCgdHuUXv0y5xTOutofOFR416hxy7cHb6j6uC8SQBOwvuirP3gDAFUPMhrlVpa3B3YOTuNXkKMpKwf23kaTJoLtQzLXMhK3hOvZsYGGKrYwmSPLMhYOpppQHqSpfyoU3OA4lo_AeqXMc_dzuFe7dBDxaHBqZtaEL70ApLBJJqwEm_yfSonDWPb6_GSL0HWrKC253d2nc_yVq2UnrMipHVHdrRUZAjK4P8EUszgDZUFWpWzV_RAdA8y8T-5lfHdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=lvxI1oLSETAHG0Qi8Cp5i9ckAPZzS2xeqAK3QetbFV3Q4aSKjzg45eK0dMBuSW2Ajp96x4w7mXY0OpRlaye7JldCgdHuUXv0y5xTOutofOFR416hxy7cHb6j6uC8SQBOwvuirP3gDAFUPMhrlVpa3B3YOTuNXkKMpKwf23kaTJoLtQzLXMhK3hOvZsYGGKrYwmSPLMhYOpppQHqSpfyoU3OA4lo_AeqXMc_dzuFe7dBDxaHBqZtaEL70ApLBJJqwEm_yfSonDWPb6_GSL0HWrKC253d2nc_yVq2UnrMipHVHdrRUZAjK4P8EUszgDZUFWpWzV_RAdA8y8T-5lfHdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USc0zLUwqppRPepIOiNYgyV-t4iZCIGb2meDrlaLLgmby7N2gxUL1FpCZ7RE1HeYtD5kRYCHMsf1lNPesPjpwjEk8UE3uJzEFtw6EGQ7yOHhE4Kz7Oc0ImJXweUe7XxH6I4FyBPRUYLMqbm85OBQYuD7Q-Rmvhxs__tU2rz03Q7MlNaZYTbLD8atZlOE0-fByWjteH9XV4J7EPxk-8A7FVyW7nbsHobaDLE2h_EQpENaSA2DQqZhADqHgIcc3uW0OViOi5quWfYqjnxpV6f0VYiHKnUMAc1zCDq8lvlSD-Cus85G5FzvLM17q_7dAKYu9Ah3Tsr2CcxfaL1Jof0chw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KFGi1wIBfEHMnuQAsRSYor78myEotXP4MWmtWCEzhd6XBMNz1ElyA_zBpzOmtAiU1zSZVDBFXUIPIv8l45erOzmPSk_9A-w8jZgEU4XhREtG9zHdEZSexfqP2Efg8Kj2N9d-HjHuAjijLKYtFk0NLGUGvXI6Akpy4iY6x2LjDL_aqBNctyi6Jl-BS9B0aXv0IUoktW6GeZq05QbYmeMiFNb-FENyCfT_OgDrdZ9b_lryl2kKvoJiocpWjifb3ScpC7Epq1VCWdymFGhcPDLDjjcMaNR567mVppqWjvhNtiDAeGAinPOmUSGvIuvxMbE2Wv3r3F5lTvYcKlnVz67eSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8KFGi1wIBfEHMnuQAsRSYor78myEotXP4MWmtWCEzhd6XBMNz1ElyA_zBpzOmtAiU1zSZVDBFXUIPIv8l45erOzmPSk_9A-w8jZgEU4XhREtG9zHdEZSexfqP2Efg8Kj2N9d-HjHuAjijLKYtFk0NLGUGvXI6Akpy4iY6x2LjDL_aqBNctyi6Jl-BS9B0aXv0IUoktW6GeZq05QbYmeMiFNb-FENyCfT_OgDrdZ9b_lryl2kKvoJiocpWjifb3ScpC7Epq1VCWdymFGhcPDLDjjcMaNR567mVppqWjvhNtiDAeGAinPOmUSGvIuvxMbE2Wv3r3F5lTvYcKlnVz67eSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=J7A2nZgQs-GPkEg_Rvp0cpYo24eoOvNBPDhoeJ6pomeSei3dxd27GG8-Bk6McpLv2EvEbCjXLJfPwR-BHRelAtP4tSRZZy7lruUZ_y9u9ZP19sD5ReUpYFyIZTKZu98JBwseu7nHOnl5td_ANqrL-l5GL4vJOavqyXJ0-pTVrGbtSl_M-7tUpM23QsjI64Z2c54uFcEXzkWmf5Nf33iYbQIaWN3EZUgL0jXLN5acVdz02Yqet0DNO40171cdVY2341-XWqGy3_ofUI4tz7QnNgZaHn6jTg8npp8TJ1qJRLtWyszZMpHf7Pr0FW3BjBD_7Rt2K951z6yXRDav4ewbzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=J7A2nZgQs-GPkEg_Rvp0cpYo24eoOvNBPDhoeJ6pomeSei3dxd27GG8-Bk6McpLv2EvEbCjXLJfPwR-BHRelAtP4tSRZZy7lruUZ_y9u9ZP19sD5ReUpYFyIZTKZu98JBwseu7nHOnl5td_ANqrL-l5GL4vJOavqyXJ0-pTVrGbtSl_M-7tUpM23QsjI64Z2c54uFcEXzkWmf5Nf33iYbQIaWN3EZUgL0jXLN5acVdz02Yqet0DNO40171cdVY2341-XWqGy3_ofUI4tz7QnNgZaHn6jTg8npp8TJ1qJRLtWyszZMpHf7Pr0FW3BjBD_7Rt2K951z6yXRDav4ewbzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjhAfStsurab97NlebiC4Ev8YNi31U1JIs6pkr5pn0ECyjWDn2A7nuqIxEr8meH1VK2iAl6cG3EZuZJESZ_qZQPntO63r4e-EtVd2pt_cNFFr5M0yx3lnNhFwmSV8KWsNpWJ3JwJpmBgE2QL_Pd-HEGlVXWslLQMJoPnJScBVUJ0zyTI92IjAHkvjzGZL7yY3uwaWYM7JDbTT0xXr7QnB8I3tYgzeEmjpy3IqMFGrm3XczWKXeZKhre5haPfRMfke2FdxVLM-UrH7KX5marMj0YwGbP4W7YXRbqLedhHxW1uFDdtAQ5a2wOJQRIifovYfX06V-e_inDsh964J7ofdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=pDX7HQOZQrLSNPnoQ6tX7299JVuROBboV-OR-gX6DAovOiKwUMwu-poSzr6Dae-zbRnbfaWOWJFIJMdHotA8w5WS4CYYMjbKzVi91pnA6iQCb1QLcdJHAudVRWsFDvcn8ZdqsPzuiyg-d1Ege7LGwQdHpWhxgUYEjG2NSfUiSWy3qu1pV6cEpslxwSws5MwGNJu4i_z_cBd0Kasxe60Cb_A8HTdPvuXDvllFqy9eB34loOgTroNpOEVA6J2I3C6Fvz3wjGpnAcNSMA7eM5PmlpSjF_fkJMZr7nuSZh_0AU_bPIdk_tOlJex3_TLnbPLiQLaGKpo7uxGtWwqrqjuOTSylUqCf4W3RuqDr_v5bpXK0ITbmIuFfuBsiWnMzfVj6wByJmGUphQ0mzqFT0g1EBlkLaWLoSy9VahLWXYetWkK7cCrcIUFhyK3s98GtXSqCJT2E4f9MNjRotOp-aJ4K7rTkCGRk17OTWmJF3-KAsg7kH8R_zD1MfrtFNO4crnCvt8nX3Jb5DWwxRU23DlcuhIxuq03ycXcUNL39N9kmEQkT5b4UlcsJPFG7MYMU-XcZEBsn2C5om32K8v_0WOo1tZIm6FQM56C1QMgsiZSNM-4kumeQ3Ut7aqnEXWuQzyt30AjgBGS7SDWkVXySgQoNn8MhAtvpgK8BGSsoA85a4K4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=pDX7HQOZQrLSNPnoQ6tX7299JVuROBboV-OR-gX6DAovOiKwUMwu-poSzr6Dae-zbRnbfaWOWJFIJMdHotA8w5WS4CYYMjbKzVi91pnA6iQCb1QLcdJHAudVRWsFDvcn8ZdqsPzuiyg-d1Ege7LGwQdHpWhxgUYEjG2NSfUiSWy3qu1pV6cEpslxwSws5MwGNJu4i_z_cBd0Kasxe60Cb_A8HTdPvuXDvllFqy9eB34loOgTroNpOEVA6J2I3C6Fvz3wjGpnAcNSMA7eM5PmlpSjF_fkJMZr7nuSZh_0AU_bPIdk_tOlJex3_TLnbPLiQLaGKpo7uxGtWwqrqjuOTSylUqCf4W3RuqDr_v5bpXK0ITbmIuFfuBsiWnMzfVj6wByJmGUphQ0mzqFT0g1EBlkLaWLoSy9VahLWXYetWkK7cCrcIUFhyK3s98GtXSqCJT2E4f9MNjRotOp-aJ4K7rTkCGRk17OTWmJF3-KAsg7kH8R_zD1MfrtFNO4crnCvt8nX3Jb5DWwxRU23DlcuhIxuq03ycXcUNL39N9kmEQkT5b4UlcsJPFG7MYMU-XcZEBsn2C5om32K8v_0WOo1tZIm6FQM56C1QMgsiZSNM-4kumeQ3Ut7aqnEXWuQzyt30AjgBGS7SDWkVXySgQoNn8MhAtvpgK8BGSsoA85a4K4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltfXB9VQzglIlPtDOmjyByAiG3BycSlxGIaZBzP79uuZgCJAP1pGCNQrhudKf7y-IvttPLemv-tlPG-HMiZEAqy8my9Ptht1XEHRgIJEXpeuIDi19vf0-h6yZSzBdsjOrfhGV0z9yQEQf4u-H9yrbisYoAT9WoC-GXdgTpyrj1bClrRg6_YAgM6SLP36fcOZbYhZDaxbzcEFp8WuTtjceJadFhlqBTlnxkqP1Xae1ZjPU4_blijLA-hQJU1kbhl2s34OOOPDR6PCNk6F0G9y1jrP4_zzPAnR0EBoFe2YjmsBeH3MvAqnN3HQcJPT8vQwFkAClz09zgEee26HO9Q3BQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=OEhDc9oiPkt6BpkSBM3nyNulQylQsDkpwDYWU8YyjlhkNo5rSB9Yh_UVMNK_BBXwGmAjnHMiR6x0gE6rwqAk_yYqI6PYFtT6V2-yTtLCNDY8_d9pg0pCKcCMchoaTKooE6vOrY7pGYfxy7_JDkJj2Z6DXaGelTzPQqZUMWKK1okcMqEWxXzv8KXdgGGiOBTKfEiwK4wnVmdXWYIhA9olW1QmZmw8tVqUQHgC94OVrsulUvoewzIe95H7P5xgVoLJEbQNFO4g1r7rU3EsR97_Ky45_I61Xjx6AumUWTem1dQMoNReVMUQlJMOn0A9OhCpzc_Cf5ZuV5C_Zz9D8O3X4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=OEhDc9oiPkt6BpkSBM3nyNulQylQsDkpwDYWU8YyjlhkNo5rSB9Yh_UVMNK_BBXwGmAjnHMiR6x0gE6rwqAk_yYqI6PYFtT6V2-yTtLCNDY8_d9pg0pCKcCMchoaTKooE6vOrY7pGYfxy7_JDkJj2Z6DXaGelTzPQqZUMWKK1okcMqEWxXzv8KXdgGGiOBTKfEiwK4wnVmdXWYIhA9olW1QmZmw8tVqUQHgC94OVrsulUvoewzIe95H7P5xgVoLJEbQNFO4g1r7rU3EsR97_Ky45_I61Xjx6AumUWTem1dQMoNReVMUQlJMOn0A9OhCpzc_Cf5ZuV5C_Zz9D8O3X4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWZRAkhGJMCePggn1rky2rESuUJ-pA_B10ZI0eqTfa4W6HNkJuy9G5y0ly6p7AwMyntJlMIDitwaPdydPffEE8J-rVmLOe3QF27j24xbLPj7vnfN3cpT5p_lYcedEfRataM_BrKW9dKQj9hPsruZMgjCsYPUU4YHvETYcGXFGBM5_ZLVjvymLtqsztThoNE3eyfwnL_bZahq8jZ7li1x0GxZbU47FwgMyeBMmJSh4oI8TTCnRyisR94JBsgJQarqQlzamnEDl6AkZ2TzI61HXrCMgwKcqOzHAalCuP9k-4N0-ADYva-5aNnqk-hBe5JpMIto60tfcJJI_MHi62vgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjw7u2WEagWXfxn5CqmZ6ErdJ3lBw0JDxBOcqCKHzeC7Rv-2ld4GxKbi0uyZ_EjQvwDhF6Bg_QRm9_ITSZzttU3hgZHpnOlkyViDn2c4hc1wWvDJtw5REuY2wI_ro3lY6PyTmoxuumbWyk6YLEkcNLoDtCmdUhn9dZTy3L1x0uaE1La7MSXlbGR2KmqWZDWlGS0rX-gpeexP1cS6M4-jQJhLOLdAj4h8QczP7fFYl4JuGDgsbHXwZUPodCUM0K0jtcXA-mkdGyllE_AM644Qm4N6MHOD7lazb2b2ePetMPoQIbMtFlQOghqBhwMhOGgND0qbcimiusC-reu4jwBpjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkidljK4jRT6mJPPV7Kg4rNq8NAWhkSTgv5vXOqKkOpVz4zdSzft55ZUzjKfIrN9dLncHBaGUI9Waz7WyYUPxoUAtynhnujxoiiv800-UHY44rw9tzNpU2cgFJ2YmqGJxVKZcERZcTvvYy7zWGsjK0iVvoB3nlosYUKjGT7eBxccu164zhj6DzQQUVBX_wVDRgIiid3ENM2IDW5Njl3BaJPmwmQDDpFQaKfujCM37PlqQGJlEGGM5aGtchouO3Kbn3t5XRWOpgVsAiWoCarnj5HCAZDXZ3fCt12vsfw6eLFEAmMiBYLb-G3dpUovMV5Gel3lkU2T9N2wSW2aYUDkTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=t83orQnpx4wkAHpc2vrPfS7Q_IXO2-zeuhcQDsGDoBAedcMWpO1cli_sw77EB2v5G4XoIZiGbTzQJg_0Z9246kIRPr44WFu-di1d_6xZiDdyqgO2ui6_qFJCGwqruIba4UpTrngHVPf67HXQA8TLLS5hpVdXE2FbUhldIAjpC5Lk1v-gRZB89WMuRxNnQEmRBP2U_fH-dhJcBa7zAbK5ZRMnU1mY-_insbHrFfY7YKuAYmKXxmqygJ1yzP49CNosobZUdoEezaaiMdRskHtitPWYoM7zWLav9IvTiiht7c69HTmY8NtKwfKJQIeSN2Dj6ZVWvKJOZNLMbI2w2gy4fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=t83orQnpx4wkAHpc2vrPfS7Q_IXO2-zeuhcQDsGDoBAedcMWpO1cli_sw77EB2v5G4XoIZiGbTzQJg_0Z9246kIRPr44WFu-di1d_6xZiDdyqgO2ui6_qFJCGwqruIba4UpTrngHVPf67HXQA8TLLS5hpVdXE2FbUhldIAjpC5Lk1v-gRZB89WMuRxNnQEmRBP2U_fH-dhJcBa7zAbK5ZRMnU1mY-_insbHrFfY7YKuAYmKXxmqygJ1yzP49CNosobZUdoEezaaiMdRskHtitPWYoM7zWLav9IvTiiht7c69HTmY8NtKwfKJQIeSN2Dj6ZVWvKJOZNLMbI2w2gy4fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLBG3prU5jpmRlyLnvA6EQGDo3o5kuB7D6p_a6OdEmRAi3a7DkLlugORStRpNt0UGv5pVcEreqexqaVCDFlkw-oEz7Z8Jj-z1ZYqtZVHka6PfZ3qDbXSv1YVY2hAipL9S98RnLg-jyQ6hczixBNVspwTMDUsX82ik1XdI-cLw8yxoUkVfOnlilI9KKmCorNJd2DCN8u2j7ppCbBuWy_tHx4Up1IBq42IQaWuB4c3jz4BIEKsnL3oH0-2TUzrFkP_p4T_cfjAtcLRKn2GLrEJOQOPYjUo9dzasG6XfeoKPLAu0Zy7bl8iGuNFcsvKkqHiQwkmALRaMQKnCCEnTnPxaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu7TQNiMPYQ-JFNA7wlpANr6OfMclzjYfHE4ZSlKtwvB8f2yaGhznm14DrHTyhO8H6HS1cyZrgx_DkZWW5oVM2AxmRp0hZcKDWvkoh4RVL2_PVWQ-9PIKpu9VSye0hMJKxMmSO97jiX4lgcGxsb16yucDszzXN8FUo3X9nhdQ7p6qpn2QTNNsVjJlJ2Ie2l2nJVHXboaj9mOkT4_BuAfjUGz__F6QCAhfAgTWp4GTu283rq0LWMcChfz0mdrEgYuVoZ7Tcwb8qbqhnoa86z3FP88AmW52yyNh2wpquv4BeKzHJGSA9S7Jy_RkjvjWLOkQdmH_bw17evFZVcSOCLv47Gs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu7TQNiMPYQ-JFNA7wlpANr6OfMclzjYfHE4ZSlKtwvB8f2yaGhznm14DrHTyhO8H6HS1cyZrgx_DkZWW5oVM2AxmRp0hZcKDWvkoh4RVL2_PVWQ-9PIKpu9VSye0hMJKxMmSO97jiX4lgcGxsb16yucDszzXN8FUo3X9nhdQ7p6qpn2QTNNsVjJlJ2Ie2l2nJVHXboaj9mOkT4_BuAfjUGz__F6QCAhfAgTWp4GTu283rq0LWMcChfz0mdrEgYuVoZ7Tcwb8qbqhnoa86z3FP88AmW52yyNh2wpquv4BeKzHJGSA9S7Jy_RkjvjWLOkQdmH_bw17evFZVcSOCLv47Gs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=W4e6iqmBZXoRKbGRzjhP0CCfF2e7BrsJoOBUJtoJM4qEB10Si27Tk1c_ltX4QECNhJwNfOiEmqxtGJ6cqY9HBrsjpkvisKum-aDzv5hfyvXr5YoHH-kRySajVUIVpjFtGQ2SFk0XFY7H3YjzCutjdoM7gCvM9z5byKg1SPuPJonFqR2gw8_hVAhU6dGHVofGrxwIHo82b5CNJAGEmb0JEFc7-qb68bEtldspmuxpMoww1bhC3SthAXpyfzy_HqP6NzqlTvuZZcEfU1D9TkvNf5AzMoZ316DNuY5iFcS2VkzUKz9KzztD30-Q185xV3-fH1S0qdPRXgMZD5H2LYS5sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=W4e6iqmBZXoRKbGRzjhP0CCfF2e7BrsJoOBUJtoJM4qEB10Si27Tk1c_ltX4QECNhJwNfOiEmqxtGJ6cqY9HBrsjpkvisKum-aDzv5hfyvXr5YoHH-kRySajVUIVpjFtGQ2SFk0XFY7H3YjzCutjdoM7gCvM9z5byKg1SPuPJonFqR2gw8_hVAhU6dGHVofGrxwIHo82b5CNJAGEmb0JEFc7-qb68bEtldspmuxpMoww1bhC3SthAXpyfzy_HqP6NzqlTvuZZcEfU1D9TkvNf5AzMoZ316DNuY5iFcS2VkzUKz9KzztD30-Q185xV3-fH1S0qdPRXgMZD5H2LYS5sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=ZXjP0nR5Aa4E-4pH-tb5GApVD5AlbvZUDzr49KVzO7YICz1JwixpQf8y5Gryh31av09f1lgH-UT3x5EJ3IVpCmE8bKy4eLDWubY7H5Rxwg25rOxBBQR3jBRX8O9ItQ6suy9kY-NeWP3eyBTuakLHvWBS268BNUyn81tiFQvF-SibRVLHfgLBcSDz0FpcLDDzGxFTwGqB_K3_YGwFW1YwatpJoibqDe2B5zmBzfBRo_4f-zx6292Kz28EXMPw6SpSUf2qGafUG8wVJ2bIIb-NOuXcWVUb2Rc_mTKClufChClQihfxVxYqJei2hIpVLwg05MZKYNtZKBI83SZkrtv1aIT_gJOpXVS7nbhWyQOwAsT_FbUHQulw-DyQLcCfNEeBvEaqfqaZuXS1sooiuPaHuM7xA8w5lSxXyI25n_0HbYvFh6gC_vRDK-NPV3E9fdZq_AtpVe4TzjAVIgDGrswbPbMdPqBMx5Sw596nuMvtcX_KyHw9KjLSmyHB0wkxz9lD-uPgIid_XfApaL74RhI4ydD4_ev6eGTR1MZ4blVciQr4sEnLv3PUjL5G5kF0lo7YnCqDAn1iMtJXtsDjpjQ5YzRMyIMXyVm7v8O0bh6v5tMlmnl9zGgArsjLjraP3aaee-Gt0GrUD5hIPwvYABJY789b5FxjtC9j_18h3J1rgrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=ZXjP0nR5Aa4E-4pH-tb5GApVD5AlbvZUDzr49KVzO7YICz1JwixpQf8y5Gryh31av09f1lgH-UT3x5EJ3IVpCmE8bKy4eLDWubY7H5Rxwg25rOxBBQR3jBRX8O9ItQ6suy9kY-NeWP3eyBTuakLHvWBS268BNUyn81tiFQvF-SibRVLHfgLBcSDz0FpcLDDzGxFTwGqB_K3_YGwFW1YwatpJoibqDe2B5zmBzfBRo_4f-zx6292Kz28EXMPw6SpSUf2qGafUG8wVJ2bIIb-NOuXcWVUb2Rc_mTKClufChClQihfxVxYqJei2hIpVLwg05MZKYNtZKBI83SZkrtv1aIT_gJOpXVS7nbhWyQOwAsT_FbUHQulw-DyQLcCfNEeBvEaqfqaZuXS1sooiuPaHuM7xA8w5lSxXyI25n_0HbYvFh6gC_vRDK-NPV3E9fdZq_AtpVe4TzjAVIgDGrswbPbMdPqBMx5Sw596nuMvtcX_KyHw9KjLSmyHB0wkxz9lD-uPgIid_XfApaL74RhI4ydD4_ev6eGTR1MZ4blVciQr4sEnLv3PUjL5G5kF0lo7YnCqDAn1iMtJXtsDjpjQ5YzRMyIMXyVm7v8O0bh6v5tMlmnl9zGgArsjLjraP3aaee-Gt0GrUD5hIPwvYABJY789b5FxjtC9j_18h3J1rgrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=iahdmr4hRyz_XEDm2DhblCvmNGTnC2o5uFZJ0ZzdFS-1MzVZNZVWV7IjANTvI2WgkVsY_aoJz-p3qV2sPOncMOsjrizerKbMXNqwnzF3yR1QZlDz-tbvY9WWMk4DUPvdSNfmxJnVDmJTOjzy_pNoWiOROEVL9C1KeWdmgOIXfgNA83ZTsqSeGhK6i9qg5HPzMdyv--cqtggxa3m8VhwMBQxBhupWsh8ZcG34sc569kogE4B4OY8RNkwsPDvUX5JvyQG_NvdtaCoG2EuNPAmJ9pnc3b4uKwniSJ3cijOHlyV78R46C0_PQqln2JI5fGogMq5pT79WGR9ZIrzjKDGpwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=iahdmr4hRyz_XEDm2DhblCvmNGTnC2o5uFZJ0ZzdFS-1MzVZNZVWV7IjANTvI2WgkVsY_aoJz-p3qV2sPOncMOsjrizerKbMXNqwnzF3yR1QZlDz-tbvY9WWMk4DUPvdSNfmxJnVDmJTOjzy_pNoWiOROEVL9C1KeWdmgOIXfgNA83ZTsqSeGhK6i9qg5HPzMdyv--cqtggxa3m8VhwMBQxBhupWsh8ZcG34sc569kogE4B4OY8RNkwsPDvUX5JvyQG_NvdtaCoG2EuNPAmJ9pnc3b4uKwniSJ3cijOHlyV78R46C0_PQqln2JI5fGogMq5pT79WGR9ZIrzjKDGpwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCkI4RCbulzUlFPGNdDL4b7n3cl5tzTF52Bdt8RvN1-SZWuJModSXr12hiCAIUIQdQBd-veIN_g1sT9ruTxf8e7ZQkOrTazfEuCxrRb9kkCQRs7Bz5eNc_EPQSwKubPkipIukywZMLdAPmMtpLxM84HtEYy_XkqeHRVO2VylZifvsfyRVy20JkGqhbfrXFPMxBTPnZaXjfSo-8c3-UArwZwB2Xm4nRXiXQmpTiOxG4F1ks5J9clMVHw-mTcJaCjMdZDhuJ3EJdx2Ga55pNu1ADMMFf4cLT1bYLh9Vu5an6CmuN-yBSrz1bhMkBZTK7KXNqZ4rAQSXnZEALWgD0Vffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=kBtGMzmOC90eY8EdAClxRAjjOP-oJIMS2Fs4v23Qb4XZc-Ijkmf2jLFEGzMXR4FQFMbIyFdqIOKRl5PPfdwORVIlql0kVlr4GcMo3CrtmmyH3aJ_kOyC_3Iv4BSutj9CI6MJRss2o-2p28ceuofUHOG3E_flhN9QGJXRxn9BosQnhrkf2JZSxtWfQ54Q5iF57TQ52OMdU1GOSlS8Ufw-9fD38QN7REEvf6dSL4PQyRK9uCkXBUo4zQsd2fC2e13cnbY-GgK5qu_HAlItiuZ02FUWZz0Aznb9dV2ccSSlsBnGM5BisVhrupW22RDqtXRjzFTmdJOgwW_wwNt-dJZUUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=kBtGMzmOC90eY8EdAClxRAjjOP-oJIMS2Fs4v23Qb4XZc-Ijkmf2jLFEGzMXR4FQFMbIyFdqIOKRl5PPfdwORVIlql0kVlr4GcMo3CrtmmyH3aJ_kOyC_3Iv4BSutj9CI6MJRss2o-2p28ceuofUHOG3E_flhN9QGJXRxn9BosQnhrkf2JZSxtWfQ54Q5iF57TQ52OMdU1GOSlS8Ufw-9fD38QN7REEvf6dSL4PQyRK9uCkXBUo4zQsd2fC2e13cnbY-GgK5qu_HAlItiuZ02FUWZz0Aznb9dV2ccSSlsBnGM5BisVhrupW22RDqtXRjzFTmdJOgwW_wwNt-dJZUUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=VYHMeNILM5VhPmEb4T-EEir6wKyCizeYP2LYTfMfl6cwSMKXng5HmbfQPvcfHHpdHSMwIgJJTr2Fh8GI4xUoKX2cejW-STH15XRzjqWI7koPiDEtST3aD6_fHqStfDi-3iD30POHHalA41qCfeBte2a1yZ2_2V77QUPcFC4tyh7_zGfy0NWjq4IMZvWHkU3_JNCdLQzO4NU0GTLhQPaKYdBgfitEv5J0EoKxHLsRL7ug8ouPLCahh5ya5TXhv-pGmUbpSIhTcgIt_pssYwZDKMHQDxQH6fJpqAWAFCzLPM8Cv1u_loKvq5e6gCh99LuEjEyAMYP__rEs7CO9RIUz_ETICANGO32XSmY26S5TPRY420zwIhdF4Hd8fmA7SFmBF_8jalMsuONhLFwaxTIxyJ2X8QOjFNumUzMc2yMgs4AOw1kthlYgbGAUxstUN4QTg5Fr6_VSDc-WOwF8w2DXsBXohBW8sUtg7jgInpT5-0Q_FU_dfiDMonYPmZRJsIwTl9YWsu2FXgOVpHuFfRCjtINszdmvNnfcv9tDP1fV0jKBt-qW8D9PKMJhsenx7jP5w-whFpkClmcHVsDSjJxFUQazV0f_9-NR5o7zDQZGL7oo75QNJfe0-zbo8HtFjqHst1Q5Rm8IgJbVCa_eCI_RImLJiTzXnMeb05zRyG2IMJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=VYHMeNILM5VhPmEb4T-EEir6wKyCizeYP2LYTfMfl6cwSMKXng5HmbfQPvcfHHpdHSMwIgJJTr2Fh8GI4xUoKX2cejW-STH15XRzjqWI7koPiDEtST3aD6_fHqStfDi-3iD30POHHalA41qCfeBte2a1yZ2_2V77QUPcFC4tyh7_zGfy0NWjq4IMZvWHkU3_JNCdLQzO4NU0GTLhQPaKYdBgfitEv5J0EoKxHLsRL7ug8ouPLCahh5ya5TXhv-pGmUbpSIhTcgIt_pssYwZDKMHQDxQH6fJpqAWAFCzLPM8Cv1u_loKvq5e6gCh99LuEjEyAMYP__rEs7CO9RIUz_ETICANGO32XSmY26S5TPRY420zwIhdF4Hd8fmA7SFmBF_8jalMsuONhLFwaxTIxyJ2X8QOjFNumUzMc2yMgs4AOw1kthlYgbGAUxstUN4QTg5Fr6_VSDc-WOwF8w2DXsBXohBW8sUtg7jgInpT5-0Q_FU_dfiDMonYPmZRJsIwTl9YWsu2FXgOVpHuFfRCjtINszdmvNnfcv9tDP1fV0jKBt-qW8D9PKMJhsenx7jP5w-whFpkClmcHVsDSjJxFUQazV0f_9-NR5o7zDQZGL7oo75QNJfe0-zbo8HtFjqHst1Q5Rm8IgJbVCa_eCI_RImLJiTzXnMeb05zRyG2IMJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V47hmA6FY0W0-ft1eWlzbtZcv6XSC5A0xa6xmYHmPkTrRmuZLA6KheheDHMbzyAdg2lNWR6U0dplkaOI0uJ1jfTA1FNsn3LYjo-caIGQvoAX8Ae7Xby6beaJZjHYW60lOPgolukqt4hoEQ0SfexleTjy5YYXkOT0SbN28QvczJnEpCw-YMksbkbV83ysNBwJ9OBjLLZhzpHcRl4IEC7N1M_tOjox_LYZ3QisXr9GoHpKLMYWB80-gf7w2TOtCIDQijTX487rOwIpH5JJpe_X-oA0tb33Or1vNhDVcWCV9SRhb0mC2fmJOr1rEE4fw6EFpLcU8BFu_ugYbz6AAEEKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=dGp5YALQQXdjicQO0GJjnQXjbGxzO_cMHEILcSgGKH7DOR6D4SkRxynsSZbaGK2I1BLSPFv8Hk3GrBOT_3FczauwouPU2AO1StCVO7sxnn1ALWcgxkBFAE9zOjebQU7EiC61uqmtmbIJB38jTusAIaykWpsvJwKRXoFVaJGJFHwuKW0oa4hQhZfPne8UbYJrzhLYohkZP2nMoq3AbeNk0Xfc0nCT7EpfZAK3j9g4HvyiqCO2gBcLD2gXWZ9pbHEj7CWcFKWxyGKBTr_I1gLWfZunrbk7JuT0JkebScCC4MB_Dd1kzeGRzgwgU1wBgPWIqLWeO94UIMlaN2AAYbpPWb_NLkVKIQWOqAGcO6MC42sUzYHh3Y_CJbPpx4BSLuXES3zvYX-oAETjDFI5kbmbj2kEaINw7as-ADzainMF78rt-1ReJkcaYrOwXov9QGUqrx8uGYM9ncX17BUJgIDWDbDDdFsLkx2u8Clz5fa8tgdJ99WAVym2MQGNhYM7WKb5lKVfwxi5TDYqt5HKt6vKVAOWA-ajb92MQkv82jMCiBm62bq-pyCZxOnnN-2E6dW2z9GctwPvqNp7e4y49PXfNeoZCT8FdfqLSk-FyqJQ8Ch58BWLxJJ6Z9PVdwPsN4bKD5OC8LGAIYAaeHuWtK4AE_y8yhC7J4-hj8w8aTrR3l0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=dGp5YALQQXdjicQO0GJjnQXjbGxzO_cMHEILcSgGKH7DOR6D4SkRxynsSZbaGK2I1BLSPFv8Hk3GrBOT_3FczauwouPU2AO1StCVO7sxnn1ALWcgxkBFAE9zOjebQU7EiC61uqmtmbIJB38jTusAIaykWpsvJwKRXoFVaJGJFHwuKW0oa4hQhZfPne8UbYJrzhLYohkZP2nMoq3AbeNk0Xfc0nCT7EpfZAK3j9g4HvyiqCO2gBcLD2gXWZ9pbHEj7CWcFKWxyGKBTr_I1gLWfZunrbk7JuT0JkebScCC4MB_Dd1kzeGRzgwgU1wBgPWIqLWeO94UIMlaN2AAYbpPWb_NLkVKIQWOqAGcO6MC42sUzYHh3Y_CJbPpx4BSLuXES3zvYX-oAETjDFI5kbmbj2kEaINw7as-ADzainMF78rt-1ReJkcaYrOwXov9QGUqrx8uGYM9ncX17BUJgIDWDbDDdFsLkx2u8Clz5fa8tgdJ99WAVym2MQGNhYM7WKb5lKVfwxi5TDYqt5HKt6vKVAOWA-ajb92MQkv82jMCiBm62bq-pyCZxOnnN-2E6dW2z9GctwPvqNp7e4y49PXfNeoZCT8FdfqLSk-FyqJQ8Ch58BWLxJJ6Z9PVdwPsN4bKD5OC8LGAIYAaeHuWtK4AE_y8yhC7J4-hj8w8aTrR3l0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=VgytjJ07RJEZHSileX-sPWHNKT0PBk6GU4UrbF1z1gSh9sjtjCvemJK7EMXhgACnOxAy3ohz5uuKAwJMqcD-h0Y643uiGZYGf1AyaHRqL0U8ZmoT9Q5K7OJUm5JwrChOwKEud3eeLyAp4JHaiH19tJh-KvC766GxK1IF4oLXqcrk9k1s7Sqzmz3T0Y6vYBo3bKzXJSxDziRmPpem_-IWaRJJG3LR6qAret0EWFWfXmN29b8AUnj6PL2TePiN77L7AE8n_oPBMTVMEgNEuPeRhdo0lGzo25lmu0C3XmX0ngqatYPndQQ3nK1PPzO9nvw1jrrrukoOEgmKlrzzWsQuL6veGdaea-cOH7nuS9tVRm1DDN4XPzPxtDoM4BtpEbLLH7N6MXFnb9PYuHiUIEd8ASIZ6L6MuLh2OA-zdlIr88YPth65FSaoNFrN0WJ4pyivKMGyQc59AyEUl2WzG1lPrkB00B0BrW1BwW3Y34aFsNVkKK3toB4V7YKfKwRXEVYvcSqGZHeREt_hY9N9SbOo8U4wuxlx08TT9e9J4bgCKakg7plheWQ8W0sM9kCjsUanyFLX3_C8VH1W_zjT5tEpuL87knZdeP3CN_mApFnXpT1rzu1PUhkavXbOlr0MZt9DlYFqDV1hQLYmrNcS02ya4TTasjWuzMemFmp-4nKyvdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=VgytjJ07RJEZHSileX-sPWHNKT0PBk6GU4UrbF1z1gSh9sjtjCvemJK7EMXhgACnOxAy3ohz5uuKAwJMqcD-h0Y643uiGZYGf1AyaHRqL0U8ZmoT9Q5K7OJUm5JwrChOwKEud3eeLyAp4JHaiH19tJh-KvC766GxK1IF4oLXqcrk9k1s7Sqzmz3T0Y6vYBo3bKzXJSxDziRmPpem_-IWaRJJG3LR6qAret0EWFWfXmN29b8AUnj6PL2TePiN77L7AE8n_oPBMTVMEgNEuPeRhdo0lGzo25lmu0C3XmX0ngqatYPndQQ3nK1PPzO9nvw1jrrrukoOEgmKlrzzWsQuL6veGdaea-cOH7nuS9tVRm1DDN4XPzPxtDoM4BtpEbLLH7N6MXFnb9PYuHiUIEd8ASIZ6L6MuLh2OA-zdlIr88YPth65FSaoNFrN0WJ4pyivKMGyQc59AyEUl2WzG1lPrkB00B0BrW1BwW3Y34aFsNVkKK3toB4V7YKfKwRXEVYvcSqGZHeREt_hY9N9SbOo8U4wuxlx08TT9e9J4bgCKakg7plheWQ8W0sM9kCjsUanyFLX3_C8VH1W_zjT5tEpuL87knZdeP3CN_mApFnXpT1rzu1PUhkavXbOlr0MZt9DlYFqDV1hQLYmrNcS02ya4TTasjWuzMemFmp-4nKyvdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ZwCn7UoObRdKur6vcT8HfkOUq9x6Wv2sN_8JsJZF-SnJOwPq1ZkdcvOdppUiBAO9T7Fx8WQrCw3OtNtWHN49tUhJfp3UmvEVF7ii9pl8xpEeFS0NZg8Q9c85H51m8JtAy71ps8cl833BmOMZHCm7QGioUsW6SzE1i1t5UsnsTZ81jmxL_EfQQsHOquK3kEz0g0VO6MMEO-QqQZlTKCierYJRXV__hNSH3Oz0oGaEGrCkjbxG-VgUsCDgFcU0MmySlBT8EKHt_Vu6nFPY9LavppJ00Z7QIx0ZCo6WdI3PkfkKiZG7MroRO_hgJxh5hCPSzJBVz68nfCJK22zVCtfkMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ZwCn7UoObRdKur6vcT8HfkOUq9x6Wv2sN_8JsJZF-SnJOwPq1ZkdcvOdppUiBAO9T7Fx8WQrCw3OtNtWHN49tUhJfp3UmvEVF7ii9pl8xpEeFS0NZg8Q9c85H51m8JtAy71ps8cl833BmOMZHCm7QGioUsW6SzE1i1t5UsnsTZ81jmxL_EfQQsHOquK3kEz0g0VO6MMEO-QqQZlTKCierYJRXV__hNSH3Oz0oGaEGrCkjbxG-VgUsCDgFcU0MmySlBT8EKHt_Vu6nFPY9LavppJ00Z7QIx0ZCo6WdI3PkfkKiZG7MroRO_hgJxh5hCPSzJBVz68nfCJK22zVCtfkMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=kqJeHD6SmD8YNzMqSaw1gDk1I_hyoEK1X9GQdZAutpBMsRXSdKn3prmYbKLiIm4ZyL9RPXIvrOWCTwvzAht8ZV3QZxOYvOymwrRwn-lIHHJGJN64j6mzqxJv6bjgnVnfLbnCSho79S0LlP0nBRBc1d1LiOEHmjkYxFo1ViPelMlgM-nvwFP45GvqZjWYVrA_lV76F8EK_x4ZXEN_bC69rBJ_S70DAD7iTNhtd46ruN2Z2nQwbt2tn9UvZhAGDgwD2On5DmaAKPR7iiJe176XObFldFD2_XVukxglyQA8W4Ljm9Wn_2-Akojun7hNNzvl_NveBDf7ob81FngnfJit5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=kqJeHD6SmD8YNzMqSaw1gDk1I_hyoEK1X9GQdZAutpBMsRXSdKn3prmYbKLiIm4ZyL9RPXIvrOWCTwvzAht8ZV3QZxOYvOymwrRwn-lIHHJGJN64j6mzqxJv6bjgnVnfLbnCSho79S0LlP0nBRBc1d1LiOEHmjkYxFo1ViPelMlgM-nvwFP45GvqZjWYVrA_lV76F8EK_x4ZXEN_bC69rBJ_S70DAD7iTNhtd46ruN2Z2nQwbt2tn9UvZhAGDgwD2On5DmaAKPR7iiJe176XObFldFD2_XVukxglyQA8W4Ljm9Wn_2-Akojun7hNNzvl_NveBDf7ob81FngnfJit5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=bNQ4_Zz3BpXj98ZXZYgtJgBLVEQn-VD-SEVP_XIzcGP5qKZ1Go1t3pBXjpgKSolsspuOGNp85td7gUGZO3tCO9E5sduAfHpUvx_J3msC0rHyfEIX7PGadp1K6WXQpKtniwa0_ghUrSjYYOk9plBqu89rc9_YTUdsvsXqaqngM6KYcg8qeyNZICk1d1RyjrYDRT-qGt8W3JNSPc9jAosxe7qlR-qjBpry02oJnfZbVOLMVTU1aVrd2blsiqS_JtuIFE3HvyOHW97EcytJQniw6HIYwbNzbBSGvCjpbCYM8zEfJ3gAwYrq4-KcjkhHwOoLdmcBRZ8mgMo5KzWeXPD4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=bNQ4_Zz3BpXj98ZXZYgtJgBLVEQn-VD-SEVP_XIzcGP5qKZ1Go1t3pBXjpgKSolsspuOGNp85td7gUGZO3tCO9E5sduAfHpUvx_J3msC0rHyfEIX7PGadp1K6WXQpKtniwa0_ghUrSjYYOk9plBqu89rc9_YTUdsvsXqaqngM6KYcg8qeyNZICk1d1RyjrYDRT-qGt8W3JNSPc9jAosxe7qlR-qjBpry02oJnfZbVOLMVTU1aVrd2blsiqS_JtuIFE3HvyOHW97EcytJQniw6HIYwbNzbBSGvCjpbCYM8zEfJ3gAwYrq4-KcjkhHwOoLdmcBRZ8mgMo5KzWeXPD4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=eyThI6-ev_BnXt9T2a06G7oIDbvOqLqnWA8P08B0Bhu9N6UE8Q02TI0nJ0-vN8BMI4ultA5lt6YcgBfelG9elCjycHjudjvtqvsT7XlNGHwczjOA5tvTPDm1q-KU_VDqGdgzS_7p8m-O2TLdy25fz51lVzLAvrEdkGbGwazC9ckI6txoxPYJ-5fwdjj7h-7eTz8fVMAO1W93E-KAwwYnfmA5Mc30mbAk5MdD3jEH7ncdI4eVCf9TBPkXdQc8PF-bGPk9lnLokc0Rx5IGYtFNrCOdCKxUaNCns72oqyEKNtLYoN6kqqblPiyyESC5YawDZbF76YgCMbnLLy7UalOPbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=eyThI6-ev_BnXt9T2a06G7oIDbvOqLqnWA8P08B0Bhu9N6UE8Q02TI0nJ0-vN8BMI4ultA5lt6YcgBfelG9elCjycHjudjvtqvsT7XlNGHwczjOA5tvTPDm1q-KU_VDqGdgzS_7p8m-O2TLdy25fz51lVzLAvrEdkGbGwazC9ckI6txoxPYJ-5fwdjj7h-7eTz8fVMAO1W93E-KAwwYnfmA5Mc30mbAk5MdD3jEH7ncdI4eVCf9TBPkXdQc8PF-bGPk9lnLokc0Rx5IGYtFNrCOdCKxUaNCns72oqyEKNtLYoN6kqqblPiyyESC5YawDZbF76YgCMbnLLy7UalOPbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=byBEeAcTnQaj6ElkxDMrmtl3Mui4rRPNBf3VP5ZIVe5TtmA_TDmTdjsdlaf1pMnSMUExVHkRm-HLozKvTtbHkqY2AuZHpMcQczQVVIMiapTZYeq_EmbwJWrfShWSQgHzohSHZ9cSF7-0g7ah1gf9h9r6gM5ASQjuav1lr7JuVDB1apb8sd30ufLcTOOwbl3fKBbaT7a5yGjDnOZObqWEIBjQTeUr0zmOrDb54qyEE0fzW0i8W1blJLuBkMjZFwN-GyoKbVuu4t87T1MytgEwpNgC742iHW-_j-xMYzT-Mz1KeqM-ZoVKnS5C5UJdKarig8YMMtrQpsbgxRjwK1b-nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=byBEeAcTnQaj6ElkxDMrmtl3Mui4rRPNBf3VP5ZIVe5TtmA_TDmTdjsdlaf1pMnSMUExVHkRm-HLozKvTtbHkqY2AuZHpMcQczQVVIMiapTZYeq_EmbwJWrfShWSQgHzohSHZ9cSF7-0g7ah1gf9h9r6gM5ASQjuav1lr7JuVDB1apb8sd30ufLcTOOwbl3fKBbaT7a5yGjDnOZObqWEIBjQTeUr0zmOrDb54qyEE0fzW0i8W1blJLuBkMjZFwN-GyoKbVuu4t87T1MytgEwpNgC742iHW-_j-xMYzT-Mz1KeqM-ZoVKnS5C5UJdKarig8YMMtrQpsbgxRjwK1b-nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=aHzHVXrsvkaSvjdJFZ3nFHkwIbvTqKAZBQvBNR1X6Ss5-mPH-wKLn9-_9X_q3YsKjijaj1G2EKueNM8lqyv2iVVXsVHFQTgyg93bp4P14kwmYmL41tiBeYCAf3sjlanyp46dkdvL0hftz0rUjLHEy7MSMzK4mbCSMRHzwuT4_vpHqKSeajmZBfMCzl9iIeZIoZ2l6xtLb_en_MSyGMno7EW7-zWuL36d5HfePPl2JI7i_LHF8Or-2AM_SU3OU-x4ZNfon9xNF3rScKEXckl18YcDSIE-YeTPZPEsDUm4z6LfnqEtWl8f1QWbWMc6-8eQQydESmwDeWdKCzrCmn6-4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=aHzHVXrsvkaSvjdJFZ3nFHkwIbvTqKAZBQvBNR1X6Ss5-mPH-wKLn9-_9X_q3YsKjijaj1G2EKueNM8lqyv2iVVXsVHFQTgyg93bp4P14kwmYmL41tiBeYCAf3sjlanyp46dkdvL0hftz0rUjLHEy7MSMzK4mbCSMRHzwuT4_vpHqKSeajmZBfMCzl9iIeZIoZ2l6xtLb_en_MSyGMno7EW7-zWuL36d5HfePPl2JI7i_LHF8Or-2AM_SU3OU-x4ZNfon9xNF3rScKEXckl18YcDSIE-YeTPZPEsDUm4z6LfnqEtWl8f1QWbWMc6-8eQQydESmwDeWdKCzrCmn6-4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=jeKcMzd7nYCqgUbylIdw6pxz4QiNHDaDEKY9YE4wgu9JjMtjS3G8R7PQLwrhufBaeR1nPqt-cGvn2FLWlv10mrmPJi__ZY7GzyfQe-VuBMegBY4qAL1GXSaoSVbDcxDOtA4rtHRIwpVqhzVejEcPRkYUFhrzI4l-LWUPe9TTk_EHk8Kjr9zTdD6eQJ3RlUxOQoVDPRQbR2tHb60lY_gwO-IRRQs32iDg2JCJBIC1XPEpwqxKc5fo47lF16LKFU03WGWHC6eP1wXK5uX_vfzJuj22ye0TxbwWLnCRcFYBGStfjKuvqS_-Q-HYksF5sjnBwuHxo3a4TPCnZGD8MNuhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=jeKcMzd7nYCqgUbylIdw6pxz4QiNHDaDEKY9YE4wgu9JjMtjS3G8R7PQLwrhufBaeR1nPqt-cGvn2FLWlv10mrmPJi__ZY7GzyfQe-VuBMegBY4qAL1GXSaoSVbDcxDOtA4rtHRIwpVqhzVejEcPRkYUFhrzI4l-LWUPe9TTk_EHk8Kjr9zTdD6eQJ3RlUxOQoVDPRQbR2tHb60lY_gwO-IRRQs32iDg2JCJBIC1XPEpwqxKc5fo47lF16LKFU03WGWHC6eP1wXK5uX_vfzJuj22ye0TxbwWLnCRcFYBGStfjKuvqS_-Q-HYksF5sjnBwuHxo3a4TPCnZGD8MNuhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqud4cgMqwWXXtIEeWevHZf0cqyWh0Y5Tsc6xFVroDiQeMwfLJCVz4PAZlraUAmtk-GpcsPTqZsxp-V6CEPrAQnR4ulPfSe7CtPBAWRAGgaaKEzCmvKmmB4nIk9rkVsaAm15hE2elreLz0hyUs4IdZa0mDPVVqUSRU-Ax_HIvfET7Lww2gh-TjsGnZzKT22tZZq2Rq0LdlJHMAYoaNfvOQT1qoTSxzNsFhoX5FaSo1zhrqQ31eP0zASl3no_G8IxvjCsRckoe_dXBH2hHUFaq0Hgo4rhJWQBo_8AHGhTZXvGpaYUTbT1nuDtjKMclBwAmqmOsCILuI4KgCCCTpJYXw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=fpXAAv0HIWxytEIKGOLCXLpNafVWBBLYCFoQijYKpUzqkoGQHCd_meo88nJ0Gb8qMRMFFtqUjUtAbxRah1cCbfdESwc6mVwpjj_VIY_C6GXe5Ois6sp_aBfgYSGUQuLR0tkdzsBUXGjN_rXJCcCkyBeh-nLlB37s5-YOz2uF0fKIodcZfAQm0YlLmIa1iRtum9XLtGJrE4AVZIJmPssU8o0M51k01hZsMZJd1ZbavAb4bI5ynLRHBDfjNlIJ5zLquaBWWt2AxU-eYWz5dCDtofrOMFKp5nrShvpe7opQWbAjs6_OItm0QbjOtnkaAUqTf4R-aHPp_GzehdqB2lKkOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=fpXAAv0HIWxytEIKGOLCXLpNafVWBBLYCFoQijYKpUzqkoGQHCd_meo88nJ0Gb8qMRMFFtqUjUtAbxRah1cCbfdESwc6mVwpjj_VIY_C6GXe5Ois6sp_aBfgYSGUQuLR0tkdzsBUXGjN_rXJCcCkyBeh-nLlB37s5-YOz2uF0fKIodcZfAQm0YlLmIa1iRtum9XLtGJrE4AVZIJmPssU8o0M51k01hZsMZJd1ZbavAb4bI5ynLRHBDfjNlIJ5zLquaBWWt2AxU-eYWz5dCDtofrOMFKp5nrShvpe7opQWbAjs6_OItm0QbjOtnkaAUqTf4R-aHPp_GzehdqB2lKkOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=W5aio1J7ozaDsCQYruC_1oewkPa88iY2kcQTqM1n6tZwZQ5Cs2ReMCd0mWMiqadJ3OW2wpc2KKu1XNYOZc7Qlbm2V5z7AC3bKYNv0CbUTT73g_VgZ3pLeeGlNR4p4_QlKaofk0FO_vvBsVLcQ9J3_aX050_VaJbZE1qfxrpg7MzXApnjy4KWKzJo16qfftenrScgGnGj-F3HegUcmDvZ42KJ89iFIqIiBvy6nR3weJMyhDQURqZvAgvNAX8rSfiMJ0S6xLguC2hWVymXVvc5YYLeu-wAB8jRkexsRc3AWPgzl8-BFI4aoDkoaTBzLAf1T7hlmcdiMORqQ6xPDG3mvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=W5aio1J7ozaDsCQYruC_1oewkPa88iY2kcQTqM1n6tZwZQ5Cs2ReMCd0mWMiqadJ3OW2wpc2KKu1XNYOZc7Qlbm2V5z7AC3bKYNv0CbUTT73g_VgZ3pLeeGlNR4p4_QlKaofk0FO_vvBsVLcQ9J3_aX050_VaJbZE1qfxrpg7MzXApnjy4KWKzJo16qfftenrScgGnGj-F3HegUcmDvZ42KJ89iFIqIiBvy6nR3weJMyhDQURqZvAgvNAX8rSfiMJ0S6xLguC2hWVymXVvc5YYLeu-wAB8jRkexsRc3AWPgzl8-BFI4aoDkoaTBzLAf1T7hlmcdiMORqQ6xPDG3mvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=gpyYGwrynejejfsvBiZgry4si4WPgvCVVnilInyM-ZK9s_yZLZdZWfDjThjvS_X0e9Da-eF1qpx534ZHsKxWVmQ4OEdQKl-Q9rkRwj3q-twAilWUjt0jRAp63uKxPSLhzBs3l0wGS1rzhbCBxbjbqb5HoAggyoGdrTtfZ9rjeHAAkmDyYBcfPkoZxvX41O44uHEZcdTGwnb9o24PZQYxn0PcU67o1kFt3GtV1pgesBEHk6gtjEicTQhLgiMxvqIvMuT8npQNS3FsY1LcmMFFEkuUjbbL7nyYqjfNTrdceDqAS0DI6AKw9DRTDgwI9Qx2h5qgE9YI5dxqrIOTdUYuCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=gpyYGwrynejejfsvBiZgry4si4WPgvCVVnilInyM-ZK9s_yZLZdZWfDjThjvS_X0e9Da-eF1qpx534ZHsKxWVmQ4OEdQKl-Q9rkRwj3q-twAilWUjt0jRAp63uKxPSLhzBs3l0wGS1rzhbCBxbjbqb5HoAggyoGdrTtfZ9rjeHAAkmDyYBcfPkoZxvX41O44uHEZcdTGwnb9o24PZQYxn0PcU67o1kFt3GtV1pgesBEHk6gtjEicTQhLgiMxvqIvMuT8npQNS3FsY1LcmMFFEkuUjbbL7nyYqjfNTrdceDqAS0DI6AKw9DRTDgwI9Qx2h5qgE9YI5dxqrIOTdUYuCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=qpwgh1UTk4GvdJjowWU-pQR44biQxyXWyYAeJjfdQ0a4o_54ZD6Yjtl54zIQ6NbecVKmwX6_Y31Vo7AZBZYoAOTWyfJGhChEvjAznyj23DEnvZdRbEpJ6_MMbn1HWY7tmLWcYb8ghYGSKxZaPDti4caBFMZsFC0urdQcN5Da3ZBIPak0di3HxA9H9mEEAt88wD-MvGsdoCNz0r4dpugWleojZyiMKTDZEdwcjQ3-oewkRbM4rxzaiNIzf4EaVBwei0ZZjR4wf7dIgeH8aSRqHE9Ya13IEgYZdiZ8yNLM05njm9JOW3kXmmu1NsktHDdUl0NM7ZPXfztMTZmXmHnuKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=qpwgh1UTk4GvdJjowWU-pQR44biQxyXWyYAeJjfdQ0a4o_54ZD6Yjtl54zIQ6NbecVKmwX6_Y31Vo7AZBZYoAOTWyfJGhChEvjAznyj23DEnvZdRbEpJ6_MMbn1HWY7tmLWcYb8ghYGSKxZaPDti4caBFMZsFC0urdQcN5Da3ZBIPak0di3HxA9H9mEEAt88wD-MvGsdoCNz0r4dpugWleojZyiMKTDZEdwcjQ3-oewkRbM4rxzaiNIzf4EaVBwei0ZZjR4wf7dIgeH8aSRqHE9Ya13IEgYZdiZ8yNLM05njm9JOW3kXmmu1NsktHDdUl0NM7ZPXfztMTZmXmHnuKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnP3lFc-9_4VQG-eMt-PjeeHrtpMIrKZ-YJ69G6A5OI7GIYzTKsmxXL_ghEXIpvk6kQ0CVhWJBr02BapJtQcHD4ArhDl44PjpnlymsrsgX-l1tKYlUi9GCZXsAetRIyvnhzpA8ykcrTUhgUVI3Bpfj0KfZ2ghd664UY9WPwT-q2VVOtTGsdqKonvyG-OTtOv4clZh_oBNUawhVRmouaoCay9dMrlQnlwHVIr0ChnHc9Txo7S9JAnrPS4xzbjFIIdhQzReXn1Il-6hXZQB8jcRp16XlU-ePN4PG8JAybhpR4ZxCFDk6KhrZZotOpYq9IBezdp81BvVKQbPpxmGpFp9w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=W20nLG5rh8v9K61hC5lNIfa1bH_VJfI_vVsVoGXihTZXhSlbxmBCdBYhEBNU9AepUSFSfSVfbfaeLa4So59Q41ma5u8jzz82a7fAUHc11jkGTAWd5bD04kAwwvntj8tf26tUykTGTi4cshuQNb4b8uQVbkPb7qjy4nzpUOMwezy2T5YMSeDw-2AXQhQRv8G_sGRrLZr2op2yrvpTxIx-zV-gXqmUxx4eFfalaDNsnXW_njeTKaAR40-r8Sz2tL30oR6VmO96vz8ZF_VxB3p2cPClJA7lL5QwOvHrjpe6Ju8C6W9NwoW1UxgD9CrkyRQNUCt0a_m7VsWVLVt4kzzoBDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=W20nLG5rh8v9K61hC5lNIfa1bH_VJfI_vVsVoGXihTZXhSlbxmBCdBYhEBNU9AepUSFSfSVfbfaeLa4So59Q41ma5u8jzz82a7fAUHc11jkGTAWd5bD04kAwwvntj8tf26tUykTGTi4cshuQNb4b8uQVbkPb7qjy4nzpUOMwezy2T5YMSeDw-2AXQhQRv8G_sGRrLZr2op2yrvpTxIx-zV-gXqmUxx4eFfalaDNsnXW_njeTKaAR40-r8Sz2tL30oR6VmO96vz8ZF_VxB3p2cPClJA7lL5QwOvHrjpe6Ju8C6W9NwoW1UxgD9CrkyRQNUCt0a_m7VsWVLVt4kzzoBDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=qORg5gUHAZM5zoG7AQeHzaWstXlxpI52auCm8zES-HgYznwrsmcrvQ87nMrwOM0AgLjn-BcA7_D1vuv_q1Os52heZ6OH7EMmtfi-hDHWhtzAQ_t38SwfCx-tHW1_5sU0ByEMVwnfMfh18vyHrDFLkfigzaBmBcHdjp21agHRR4nOv1ORCljYoPY1knFHgQHFxk8afMcCGk8fXexOVL74li4GPrwA1MNdnYpPcaqUF_LVWZ2cscKX2tBHf7AzGW-fsX5KyoZvC1PCshtpkStO24YT1FIVrx-nlPAowC7j4zOi7XacHbILCCLdU32AW0a_StcMI-9RPjFwjJvx8BHXvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=qORg5gUHAZM5zoG7AQeHzaWstXlxpI52auCm8zES-HgYznwrsmcrvQ87nMrwOM0AgLjn-BcA7_D1vuv_q1Os52heZ6OH7EMmtfi-hDHWhtzAQ_t38SwfCx-tHW1_5sU0ByEMVwnfMfh18vyHrDFLkfigzaBmBcHdjp21agHRR4nOv1ORCljYoPY1knFHgQHFxk8afMcCGk8fXexOVL74li4GPrwA1MNdnYpPcaqUF_LVWZ2cscKX2tBHf7AzGW-fsX5KyoZvC1PCshtpkStO24YT1FIVrx-nlPAowC7j4zOi7XacHbILCCLdU32AW0a_StcMI-9RPjFwjJvx8BHXvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3nBpWitRIwrH3eQzjuTUa6jifQTX5buf-KAWIzUshV2_k_sNP_mRdg2C6-hYICkFeO4tSxm3kXv8dIxLEqQ-OBJkBHVD8qEotXHHaNwATvoLCBkGt2kipDmUqByVVwJtyxOzjHncJtDFzncz3FuuUZES6HE9-Ptd3YyNhKo6xDyIQyk8-nsTujry1K8mhyrxxavXYMnI1mx-lL3cObZNUL53DVnGPfJLdQf4Zx6bfNWioSEaWJjcC2vD-SOEd9SeIwhVkZsz8BQVjfDA62WKFzVnb7R6E_uoLpWYyJ7Z57eaBGKJhtkSRxOCayiKV4b7t2MOzNn6JDTNdjtJVy5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WM--TpitVnQNZmI3rue7O2qH7j0dgbX-5lVNYLuY1NTfckys-4k80Ghubok9c0PnsxIG6wFK9Hk_crD1QVh7bhXSGhSROOC0MitRS_jWcfW6zV8g_go6zGwOiukrIdki9sO09TXcBgN7n1-06p8lWGSnVoWtDk8cx2ejbjFjtWgEXv2FjJ7rqjpjF_oVuBXxzv_bclanWd91NiyrjoC7oJZsBArcX3Ll1z6wDd0zQaZMips88SxBBEbsdaEtONtA8WXibmAQ_OE5eKQoGy8sfhrfqK2YdZvrY3Zq9QCjLA7FYDCN6nX1zugO2rAXfokebBFPNyEEBYpGak_U4l_R5g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=DdAe0ExjOu0Ux4aNk7mDUpEVrueheugP43xv_bE1IwTKFDT3qs7-r2LZpM71II2MQ5Obx4Go8odGd85CSUBaAk8WRUlScOCRGDK_sC5d9fuGB76b00zX6f_tLh0C3WDg5VeQLXNT1BTvr_q90XFMJv8fQ13BhQz5rF2UgZwle0yBeydBPI6O2PtLnXTxXUlEQdeqdj6Pd-w1x53o9sI2PAENxz0aG99YX0bBDxKT2Ojsw02b_wKLJTOG9EEboDMVcVg3nxVCgvKl6O322vVUUCKB8_IysfFL8OSquOpRCcauLyH8F-hFkt_QPJiQC4TRLNDx6G7FNh-vLc1Ybct0mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=DdAe0ExjOu0Ux4aNk7mDUpEVrueheugP43xv_bE1IwTKFDT3qs7-r2LZpM71II2MQ5Obx4Go8odGd85CSUBaAk8WRUlScOCRGDK_sC5d9fuGB76b00zX6f_tLh0C3WDg5VeQLXNT1BTvr_q90XFMJv8fQ13BhQz5rF2UgZwle0yBeydBPI6O2PtLnXTxXUlEQdeqdj6Pd-w1x53o9sI2PAENxz0aG99YX0bBDxKT2Ojsw02b_wKLJTOG9EEboDMVcVg3nxVCgvKl6O322vVUUCKB8_IysfFL8OSquOpRCcauLyH8F-hFkt_QPJiQC4TRLNDx6G7FNh-vLc1Ybct0mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svg3MpyD8BpJog-J06Tb-wHXBWNpsjIGhY3j7Isti3jwOtRlRgbLFBV8JpbXA-KL7KFfkPSS78bey6XzfX16kDkOpklcIkv-KAN7APtZ3twY6LiswY__8z4E1bK7DMRwyfMtM6BiaboIgRUtYI3nyil3xLoXuCFBLUqhRhATeFnwE2T_XY9knpAax8-LwWI5yCOf8DkNK2M07e-06-kBUaiofcdH6H-R2ut2dTmBRfO39B4w6tk1a2yH7q3Zzcq_N8QknRo5TXTx8JEsHPOM3iyrsU8Ly9HJh2BPCk9-TQHcUgLvOg3mRG7azPTH2gKg8YSO9-R5hGk-1E38Tx4sqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1gvsAExu8kVSFsUXPUpyKNByxLVoCWjYVRLkSCqSMH9HyxJCNZCmBSiHvtNJ9Wf7Tl0e8Ps8ZtzDPtP6LPOgHZV27BQcH3qvav9uV7KRAR-5X9GMVZzzryz2ACJiN5n4JINpz3mWPycZO2Hw-EqC5Fpa5anLK6MyQ_r61pDToKdctJcpqFqu_2mRkdzknUsKVhQFY-9e0QNLveMsQHZ-Evz00qDi8Z16BwY-_D3jC1Q4fijNzRKesPRNbOGNneNEKIXKAuK2hVJcLu9bhG0y8FwIAGlEMeQ1ggQN56KpzEKiJKhJu2hELLOAMFcgsjd3lvTKJnrtiRCHvJ4LnOjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5jVJfIJkfV-zQRJrcQVXxGccyh2xR1bGYIV38QdQ_GdcGBNQs9vQNAOWSeuNvfrP9uRcZb-cNWwy8jXb-CymaF4zKWoFk9u0p04ewLdN7fZTw-ndFSL11GJ9bFEbA9Ap7Fmwd0hhLmS8HEDTzZBa5aruvYRDVZAKvRW2viurQxLOXjHYpLJ91gekB-aHDwWKj9vkeKsY6UbUjLyicaESpTsEfitiD5TFR8KZTFBrAwv2dSfEJyOAvM_GoCpVgX3_2vR7QorLHr-isFhOiJuqC3OqJ0g-RPDXogaI7SGnZoYOzm8M9FNDDGtd-n3cm482PwDBozE5riLUf4wyurbhQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=EdIC--8AI8WI9QK7q-YHUAVr15ULS4PX512BQdw0jEBSCSAHnj38Mok8pVPD-1jo2lwIlxl4ygtk4V39m5TRLFTB3UuRcJn8Uee2s_z5Hy_dvg-hAmu7cuIwDejeyFS6fteLZKexKxBnEFun7hpBKuhrq0b7yPSH1QCx88FriX84izR4C2D1TKvPg2i4VDa2Yuz5EmHW-N9MEam8ocl1dto0hsPTRQvbUoh8A8voMYawguRHjCGM7vhGf8Bxj_6xbH2AR0uZoRZgjnxV-0ZNSdwZj5dxF0ZD0JZMfRCVcJQcV6bAMCRACdkWJi_gjDmmn7gLVTg6CDqU1MZxjoqKkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=EdIC--8AI8WI9QK7q-YHUAVr15ULS4PX512BQdw0jEBSCSAHnj38Mok8pVPD-1jo2lwIlxl4ygtk4V39m5TRLFTB3UuRcJn8Uee2s_z5Hy_dvg-hAmu7cuIwDejeyFS6fteLZKexKxBnEFun7hpBKuhrq0b7yPSH1QCx88FriX84izR4C2D1TKvPg2i4VDa2Yuz5EmHW-N9MEam8ocl1dto0hsPTRQvbUoh8A8voMYawguRHjCGM7vhGf8Bxj_6xbH2AR0uZoRZgjnxV-0ZNSdwZj5dxF0ZD0JZMfRCVcJQcV6bAMCRACdkWJi_gjDmmn7gLVTg6CDqU1MZxjoqKkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=TJbG1imgoKkG2BDvkpsyjXb-NHPcfKGrzsvmY_OM2q8CAxcTadHUdcZRLWgaqscJkphCmXBlqpHMhJkSCw-fvafknZfVLD3Lqr5M3newIeM7Z4oER2pHvzdKswJLN74My9h90LR37A5hiMt3-akrD15_0bmgAB3UtXt7TpCTcZEIXQHdKjIOfqVMzUdQPPT48kOoQg49Lqw-1vqAljnM8VAqeNuNmes6_YzpixUA7_vc0GXSiGDTMrq0iurlTkNlHFnuGOdciOEBslx_wVNpzRsYUCkCnASH1AkQlmXu72aCJxN7pyTsII4RmqHSsHySGWrGXWxxBzroa_gjX7g2jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=TJbG1imgoKkG2BDvkpsyjXb-NHPcfKGrzsvmY_OM2q8CAxcTadHUdcZRLWgaqscJkphCmXBlqpHMhJkSCw-fvafknZfVLD3Lqr5M3newIeM7Z4oER2pHvzdKswJLN74My9h90LR37A5hiMt3-akrD15_0bmgAB3UtXt7TpCTcZEIXQHdKjIOfqVMzUdQPPT48kOoQg49Lqw-1vqAljnM8VAqeNuNmes6_YzpixUA7_vc0GXSiGDTMrq0iurlTkNlHFnuGOdciOEBslx_wVNpzRsYUCkCnASH1AkQlmXu72aCJxN7pyTsII4RmqHSsHySGWrGXWxxBzroa_gjX7g2jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=OJFdIKMfwyPuTXFI3lGaFyv6Tz9uaKA9a3_ynYrbI8c-mekPzLCe3OX6kDD1weCs5KSJvm1FtL3Nh3YhgICf3lrfCD43hzcc2WP2BVTPtoOYkwXrmtSe11UhxrD_E0gGQbpZ9WCXghj6MhnafO5CLWv8KwOR_bHux71FaweBjNpzxnJ9-5wDfotH-jxMVvP2-1PWASVm-SeP7mCyyzp0JPK6GR-nS022nIrbGHTaJla7YtldcZQjl3vPWM5N-yqu_MxfkoIKRUy4_aCWVwMhy6yXjWrsAGt_ul7ud9Wu5Io8bBg14GvHrEGXFTyG7bqRj63kjEGRnskAtLBqlws88lXM0SKeBDePq43a4d62tZq9LO39bY5jLpV_cWun8PwuvdQfCQxjA725bBLCJKEfpkWq-40ixhsH5FnuabfkwpmRjA7nnh2qyCbrVPPQLE7WrZOaC4G_cfOEZxQY288-Mm_j8tW_qlEpbsvTL_JcfbketapYF9IoNQLtlS7wSpzNUj_fRpJ3yKDpo-hfineyYD2U6xrtjXBUrTtVeB9N1vJiS09f_FuOMcXtWWMGw03hO2VFSAmFBWO20Ua3tjLYr4TVZ-98UxXU3pIY-OmRueg4gCJ19qi-ajJchWqA1EIN4sfMycn8WLUt0hcXG7RErpx_6Bj8PW21RC3bD263xNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=OJFdIKMfwyPuTXFI3lGaFyv6Tz9uaKA9a3_ynYrbI8c-mekPzLCe3OX6kDD1weCs5KSJvm1FtL3Nh3YhgICf3lrfCD43hzcc2WP2BVTPtoOYkwXrmtSe11UhxrD_E0gGQbpZ9WCXghj6MhnafO5CLWv8KwOR_bHux71FaweBjNpzxnJ9-5wDfotH-jxMVvP2-1PWASVm-SeP7mCyyzp0JPK6GR-nS022nIrbGHTaJla7YtldcZQjl3vPWM5N-yqu_MxfkoIKRUy4_aCWVwMhy6yXjWrsAGt_ul7ud9Wu5Io8bBg14GvHrEGXFTyG7bqRj63kjEGRnskAtLBqlws88lXM0SKeBDePq43a4d62tZq9LO39bY5jLpV_cWun8PwuvdQfCQxjA725bBLCJKEfpkWq-40ixhsH5FnuabfkwpmRjA7nnh2qyCbrVPPQLE7WrZOaC4G_cfOEZxQY288-Mm_j8tW_qlEpbsvTL_JcfbketapYF9IoNQLtlS7wSpzNUj_fRpJ3yKDpo-hfineyYD2U6xrtjXBUrTtVeB9N1vJiS09f_FuOMcXtWWMGw03hO2VFSAmFBWO20Ua3tjLYr4TVZ-98UxXU3pIY-OmRueg4gCJ19qi-ajJchWqA1EIN4sfMycn8WLUt0hcXG7RErpx_6Bj8PW21RC3bD263xNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=q1D6besArYyaEawgtQDFrqK1zhYmVFZ9OHeRpTISsmvcfcxqNJTZjWz_ixpGtXVRdn4AbYnDUqdsTaOIkFiMsI5GqDulgEVWEzB2ALCFIjiQTJ4ulp0U_gLJNYoWJZgaoxOl3QTRLWUVJlsv3YTthAmDkyHcbGyGKix-GnFZ1SUZaip7MVirYJdoRndpIVmv0n7kW62IidLFu0IbB_nQOctgVphgoxmHkikxUCHC-kekC3ubWCgpFbp08ZV8cYM1mflbn4CgkEfC9d-t-grTMXdr9FEyBFag4ATo35vrLMDvDPoi-Yj3uUqAS0KqieacC7e28twznKmZjB_8-bFSSo28QY0wWGM5K2qFJUFOPJOSG5le0_DXnH0TXTW_dYJt7RZsgBeZp47zk-HvGuJTFMx-XBMs2_yc1G1BBXHjIBQQBFFeCXaxrW4ZUywnqA6JNlD32Y86ciy9mJTd-QJlRXh3B73waTihQSJzsHR8kG1R--n8NBIaeenEiZ0u6a_ePk2sAZzExjVqBJSj-sB8Dwyuefl67wZssLQAlxewWmM__q68pe_aF2mhY3gANMsRAR45gsVgaQIHsXSYer8IFeZPI2xlYtLmtQKy-ttg_fvGY9fVRLIkgf-GOMM5T0rU_ePjX1KSD2KVv1eaF3_2yt6ravU1NodCtD7RMDG2W0Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=q1D6besArYyaEawgtQDFrqK1zhYmVFZ9OHeRpTISsmvcfcxqNJTZjWz_ixpGtXVRdn4AbYnDUqdsTaOIkFiMsI5GqDulgEVWEzB2ALCFIjiQTJ4ulp0U_gLJNYoWJZgaoxOl3QTRLWUVJlsv3YTthAmDkyHcbGyGKix-GnFZ1SUZaip7MVirYJdoRndpIVmv0n7kW62IidLFu0IbB_nQOctgVphgoxmHkikxUCHC-kekC3ubWCgpFbp08ZV8cYM1mflbn4CgkEfC9d-t-grTMXdr9FEyBFag4ATo35vrLMDvDPoi-Yj3uUqAS0KqieacC7e28twznKmZjB_8-bFSSo28QY0wWGM5K2qFJUFOPJOSG5le0_DXnH0TXTW_dYJt7RZsgBeZp47zk-HvGuJTFMx-XBMs2_yc1G1BBXHjIBQQBFFeCXaxrW4ZUywnqA6JNlD32Y86ciy9mJTd-QJlRXh3B73waTihQSJzsHR8kG1R--n8NBIaeenEiZ0u6a_ePk2sAZzExjVqBJSj-sB8Dwyuefl67wZssLQAlxewWmM__q68pe_aF2mhY3gANMsRAR45gsVgaQIHsXSYer8IFeZPI2xlYtLmtQKy-ttg_fvGY9fVRLIkgf-GOMM5T0rU_ePjX1KSD2KVv1eaF3_2yt6ravU1NodCtD7RMDG2W0Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=Occbxzso6DGZ9RG8XRSLRs6kRLut3KAXOw4M65Zur8OR0uKpulHKdUcUjmuK8zlhJp8EccBO4-MuoKtEAlmAEsdj5nxftVH9hhxVJSeV6BFUuwDvRV1z0z-vvTTeqAcF2VNjcq8WuSqbhC-e99COjXPhKQsAhbPCrv7v2SQk9TCTWrB1nTYGyjXL5q0zmCq1TpR17FmIom6WEAMVPCW1ZiJeh2NGy1pH8k-DkfJhdZ7jVxYtxwz6gveGsDR4YW-49sVDIsQTbXbw_-E0TOH97FMim1pMjWCGXPWAmMEBu7ghZaffjh7n38HUEqkzK2mX-XEwHhXTPhg8fkLdh_QVrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=Occbxzso6DGZ9RG8XRSLRs6kRLut3KAXOw4M65Zur8OR0uKpulHKdUcUjmuK8zlhJp8EccBO4-MuoKtEAlmAEsdj5nxftVH9hhxVJSeV6BFUuwDvRV1z0z-vvTTeqAcF2VNjcq8WuSqbhC-e99COjXPhKQsAhbPCrv7v2SQk9TCTWrB1nTYGyjXL5q0zmCq1TpR17FmIom6WEAMVPCW1ZiJeh2NGy1pH8k-DkfJhdZ7jVxYtxwz6gveGsDR4YW-49sVDIsQTbXbw_-E0TOH97FMim1pMjWCGXPWAmMEBu7ghZaffjh7n38HUEqkzK2mX-XEwHhXTPhg8fkLdh_QVrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtjj2E-4_-23xSPHR5-HFN_NoHvQmmUydtNFn_dPyuvOL1IRzvOwsdTozjObMQUfbHNnjlac45FOJCiXLe2o2u9XvM1VHQ2gp0x8QPWOfI6M17KtkNwcijIIzSKQC74gXlMDIw1JDZQa46NDa9wWHHikH2VLqykGW2unoKnpJy3S_jZO40SgNKy0kdtN-WkRuvh933TUseosCUFwa15Cqg_1clYHXX40WJgRv1ic1mr6gPCPqlnkHoKwxI_epovS4nRPPX9X6rPgJFuqrn7eEKOoSnlrJlM--ntf7ETMlyQTU4F4YfLb0s1RyamNqHpEtWGglPZYKCnQ-erlDGdj6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=huXvZo8TFk61UN2cjSFEcxrlVunz7tu2Mm04ARevgjDUdCs3wSbVZpHWIJZ1h2fGz2bZlNhWpihKq0d-zohOyAURHK_mRN3e8Q_UkOAHLraO3uYyZYKqNSpKHeluHojlJdxzUHwe-TmUtjojtI1HppatGiYQ3OdkefTJd3UTESPl_h7RLs7uu8G5FgMK--NX21xxVd4exn1UH4vljdycrfUDEJt0ep3lYtO0HAC9GVme2cGFkhOXXMn0ZbbHGWM13U2wOnxXMIDyISORdLujJ7TkpqffqdDUuh5gNK_GX7isEPfLmqXQdIkguuLrBJFESRAVt1vpFakMH33VGh_Q8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=huXvZo8TFk61UN2cjSFEcxrlVunz7tu2Mm04ARevgjDUdCs3wSbVZpHWIJZ1h2fGz2bZlNhWpihKq0d-zohOyAURHK_mRN3e8Q_UkOAHLraO3uYyZYKqNSpKHeluHojlJdxzUHwe-TmUtjojtI1HppatGiYQ3OdkefTJd3UTESPl_h7RLs7uu8G5FgMK--NX21xxVd4exn1UH4vljdycrfUDEJt0ep3lYtO0HAC9GVme2cGFkhOXXMn0ZbbHGWM13U2wOnxXMIDyISORdLujJ7TkpqffqdDUuh5gNK_GX7isEPfLmqXQdIkguuLrBJFESRAVt1vpFakMH33VGh_Q8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=PG7H_CTaKHKxBqWKNI09UZ2hryZBLYGczeHA-Cqt9HM7LO_2WBi1Gb5UrWZvV0WkKVLw3OXmH78-xLjK_9eLC1YxU_WZq9hhhZgUnc6OSVyzVZzy-Egq04_AC-bDZ8no1i-rSDdDahp7fZCQQx2Q6THhQ13vCen5UrzcLN1mDJiHNNOAW85K9xAywNi_v5luGB4tx4KrLrJ3KILr2QafGe2Cea1R2anRLmF9JhrfaX1NrKeMbQmtYWd1H5zg1grfXrdQOo_lUqNy7QH5JsyAADlYy9_zjYEFW32OFFvJ2F7oa4ZIor_jMDLbLwGgB_xMBe1FxY6RaK-3N6HR9v8FXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=PG7H_CTaKHKxBqWKNI09UZ2hryZBLYGczeHA-Cqt9HM7LO_2WBi1Gb5UrWZvV0WkKVLw3OXmH78-xLjK_9eLC1YxU_WZq9hhhZgUnc6OSVyzVZzy-Egq04_AC-bDZ8no1i-rSDdDahp7fZCQQx2Q6THhQ13vCen5UrzcLN1mDJiHNNOAW85K9xAywNi_v5luGB4tx4KrLrJ3KILr2QafGe2Cea1R2anRLmF9JhrfaX1NrKeMbQmtYWd1H5zg1grfXrdQOo_lUqNy7QH5JsyAADlYy9_zjYEFW32OFFvJ2F7oa4ZIor_jMDLbLwGgB_xMBe1FxY6RaK-3N6HR9v8FXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX3TY2Upw6piivInthgEE0roOAMG8Eu4gX93xbxE9LpmOL87CHw5OzbJH6x2Yk_-nwNtqpCk-d5Aa2PDb34lBPinIGo8V0hsDwnZ2h3y5b4j3sDL0B-S0QKOOKqzUeXRqpeipq_SlYQsietVlUWekBC3h_Tmp8XQjGhnBiX63KX0cYz01QK5x3gBU6tlNCs_pM8qzSJJ7r9Xpr8eGzdjcOPA7McEGdVV7JSAWo5BoFXP3XytL6UP8ug9Mi4vtwSSqDc7IiC7VyYjkt_m7IiGyejGYmGe-PQMrSDnSteywGnHX6DawxSJ6TR6i_tVNMSN443_qvIXW_XfhsvaARu1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DV_otaj4NLyJ208_xDSIVvLiMjP2ODj5Nn_U3AFXMOQADXa93qkmFZilgrU9aYqSM2ClWrUaOvq1SrJLNxJJXa77zu2rXcDetmtxpXm-rjlahfAylyyupkR0zKYcIPQUbUNUy2mI9LSNwhLH9rn5dW5hOurLt71jEdpEoLfMhLloNAOXAeSt2bq4q_NRz7QGgLCSMDeNO2o1HwWQpMDMAx-0Zl-jRgtkMweRYBoywAUMVaaKa0PdBad7I1Ft8xpO2GoUcB7n39zsyPn5ovCWVhg3wV-xiAiBdaV76oOex-8bXeeouLlFSjmpLP8hHteeWZ6BNbyLEoHc0kp1-JRoHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vjbsb667H3-iBrytgtSu_usziNlyb20p3UbPy8LL7ErD4WMe6wFcnoUXZEJ3ouTkYZzkC0n85UCfmi1GemYkzFa_dZ8lNZtyUTnqEgOhSJRK9lPG7gwuizn7G-kXT6gLjtim8RFD_TowvlC3lmQ6ElohJPLDKtFa89meAanAnRDejr7TwlAU2dxM-pcc_yaBn2VRGGnb8kChFQAOkRChs3VW4twmJstMgHOpSREB1XLfHPY_lzsI7rLuGV6_ho_McYim9Dqte3oICE5Hw53Ztz34Js0HfDPI_75x6x7o94DQfe1HwqJeIPYW06mNcSJSsjzaD7hvXpYxipV2Zq3PZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8Uep0A5DWT478-6YZE4ol_5RZYBuWG37jpz3I0-wbX1a4AA48iID60PvHT7azGz9EBwH51ZUcF4VWrdDweMhDKM93QvyPb_an_oNEyyb2_5BF-pMP9mB6FCcevBbZymzjXWIJnybIurWOnx65cxbddd0in5j-WgIXjuegYjcklXLt-JqMqriaDJFe7NOkUp6pj9b0fPvtU9R2EGco_lpLIXQxP-O4GM36lHOHWGDQM-2icAk6Sz7B3M5DHE7Kp93EmXopB6Q-TFO3QDrL-aw7rBIy8XVQimLlLN8Io5K7Sb2ekxJiabeITi1WdxD0Ib3oF-Jbrw0i52hPN2mTqQQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlttH8Zn8h6sFuBi4K0BUi9Lj9AwfdojKQ9DZxci03Y3WrQ8dsnx53Ljf97jhLa4cWZl-9gCS4GTXr-z3IfXwr2b3-5zZ9jXEdjd2jhjlony-V26Eg35dTExHuzX11mJBK4IiaRCFaUT16ntnTqOdCJJyZ_VCnvrVt5ZYOw0Y-TAB-KEv_jiXrhaleaeTAIFTqq5V59QhmNb1MkbmOtw2_rqFW3uVeiT3-nDwFfYUL8zVtr2ysBomTodmO749mCKgSI8T8wqw1ldJKIUi8FGe1QWgVHSqe1fGzXr5uHg-A_Uyk_psYh4p0CmTN1DWQNeklXJzqm7RriFNDYKMVrgNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSy3nzfkgzI4zJgjqxzq2X25ZLGNzqDwISoE6CKMffwAluApnJH8Ctw8SRg5hTAwvLacQWMB3BCobagNl9Z3_P_93YLGUfrkDLV02zhxkkdzlGr-ZEbydahjztZ20eNhQuQkM5Ue7etFtwha0GgwIMY9sxHrX68mfUxz0FcJE5xsToZ4l0YThTCBiH1-t15oM-cu3wtokcRn6OMNPlPkTOEIAViUaau0aBosSZMkfrmeqTRor9zoCaNHrA9OxZndexby3rnNwdQGEv6gzAbFAxonMpDZnfU_q3xtGzhsPS8gTUbCZYMVF81nNeIPLK11l035hX32Oi9MObXJJ3qgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzlC0cnAvxVRVQhttCD4bM1MGBmdgLbqyzY3kqDJSf1Sy9kBwfVUWT48Gnjyz3ZADwVPgEH-ZpliXdrmbWjvO7YhBRrABVR08qtiuLY_kzadQ0SuTz9sr7tiG1DO9HJnTBYyDnzQbo6iBXmCZx_7ctOt7WRaMQ_28RMJqWT24sCOeBzxgfyAjFwGGsUalYwV8sGevHtiHL8wfv8BqfOCkHAcMmj_69JlT-oY6S63Q-eohCa3j17Tn-6bFYYIDqsNmwPr2QlpzOquIR6SEjRxvLxyuzCYvyLVyMTFCgyddlJIS3T-MJS1bxmhIQACPeo26w_TXVLf1WAxWacNIq9Mmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYIIiwUKRrkU89ZmGKNiTHZUFi8-IvfBwq1Ao66kuX1U_ADoHwBGcVzCObWJiS2a20JTRKzqYYCGwtABUADnvNzVukdNyMPe12E5g65Qtt00vJhfLSpo2JFopJ-4olaX6gkTxvQizBLas-GOWtq8cMzbOg9cVj8fQiQ_ZgK-vKrash-fy82WdP8tSD2g0wUZXAjq5gvvvY66OQmYlzP9CN44D78LRsotM0xxCYQYSoBKu2YyxWqKZ8xWVCHkHDQpcC16Y-vrwD3yYoeiTV6_vv9LsMEHa3JavArchg-mDNHiCIGqwakVz1cfIwNhgBJFsLtU6BgzsAu5AlPyfTZhIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoMdlvEsg79Z6cKFUnuuLiwvVMYeS4osNIFSIa-wETh1uU8I0esSX5Ow9cXkrGOUmxUqarpdF3smkqddSr4xXYfO9hbnGzIK8SHBaeUdi9dIq0mdS-HpavQLG003ghnj3DAbAt7iBjeX4Hj7mOgX8sBEVdAKOZh_dHsjOWK1crbsT1VXbcJpIvJ3H1dLXSui1PcyBP5qhje-dMOgbsHqVFzgr8-_G4pZy6kFXaDOlvKVTYOVAFNgkRIy4p_B7bZuPoTerSD4YKmdIvMga2u_gLHPnMGCbMQNGAYyHAXLzzzLySOaKLu_mD1zgfwgvdcbNk6fYNcMSuqZWVGaMVBoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OT6N0tcGsTGtMvORmzXz9rixRUmOi6QUSFWQy17elAQ-oqL4F--B-OLLFnUeE12GwDskbwKUqNUUZH6HTqEE0iJWfKVLmICoLrw2FvWMvG78bmgMm3cXFEdXNnHh0vo8SMNkMQMoRARMDRIAdBwEPG2OJKobfrSbXOH53zykTDrPP-9GtfASBt1Q8LGzZeJYUCd4vgkXIXE_WTMafB-Ot4pEjjSkG4N3n4BUMb1uv5qEqAz_57E2wbOQyVZmnzC7mzWHgp__hg8FXpPbj2lzEbulA72tonZ8lheJNBOr41roJ0m46cXuRvc9yvjzVRpEx7h_vA4IWGIEgYQPp1TCGw.jpg" alt="photo" loading="lazy"/></div>
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
