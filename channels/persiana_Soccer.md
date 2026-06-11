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
<img src="https://cdn4.telesco.pe/file/dPqY9QQV9S6tjg_RMDBo9DPYTJrlqg3NYmoPyCE5hS9oQVslh8vk8g3_5JUa_N9b3D7FtlyQyQfQJQWsx1vpNPXGwRy-9C62-5VQMhplOaH53wgLj238jH7In7t1FjIuc8Sdjj_gMGGt-NNTjfCiLI6p6t9aLyjFjiaWGnv04jTAWUDHrKnyZtJ_qnwihftul86ReJ-xejRCCj_6yH1MaJBN8NIg4DRX4OvDoQHTTKPGdunrIcPHNzpKIqZo9v-B5v0q2oyvxwoNb8SCtOcbHP_u3ViRShh6VNqvq3qm4T-zVe5pgXXXKajEt9rZwiVfu7xLp13gyXfMp9wx18a6Cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 195K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 00:43:33</div>
<hr>

<div class="tg-post" id="msg-23222">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwT_cVvPmUoaEBKfmMDE4NYUNgC8Zu_EgLCHP_h8hyzaUEV_srLwaHwU7415kihpqTfTZHENq35iroE0ccZjhbaN3t1bF8oBIIZZvnewa5mHKV3IP0M7a--cw4NX4dwCc8_aAQR7hRMKgZpETGOyUvUepszIH-Ta5_PWeRwSCGJ-2RE5GHoT9p6Jc1F161bG-kCe0vL6EIGBKdXkn_ljuk_jDHpN5U9jFm-O7bKcJMMtYDIF8MF2bAu7bmElOlQr7XzsPx66n9e0cD649YZW0ySa6UWJ00uLpr5w_PvWMlffjVWJIEY2eNN1TSuhBa84_DLRdwLNAZw6rtBjYx-2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9AXIHalUyQwXdGw14RhtYvDDFAxrKsGruJDiORgz46UUcbWGLFCsKBxpAA_k4m78VUeL2Bz6nOHij8KWz2hi1SNKO8Gzgi0qrYVYYooFpJqzv4gJRBA-bS7fcL7EabOh_GBmdWzhzb2bUB337dz1J3P8g3S0Z_cqQKUwN7v5sXA_ByEk41GgdaJ5-hnLn_wjo1fZT2Agy4i3McP3CAZW3IJo1Vs9ZCCSWnvautD_8XB7BMTtFN_99LYOEiEAWp1J06qsRbOd1654QG8UalOz6nTqQlfzweeOnCM55U_Z_VTjXyfagP2fB-NbzQRqywBXTf9-qWC4pNkoXfnI8hHKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/persiana_Soccer/23222" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23221">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_ajVbf1_Ngn_CjWf1ePAHIKivBzSq2vWcEauuGbOtSm4T-zlPcSvIwQpEacFsFGJ0XrV0e4QXRpGVb5QBC1p31x0rD0eaPZDMMoLxs9OP5iqW6yVEyUrGWxzCJ2AVwhLClAN6evgVz1WW-w-qYgdDWqzcOyDQemTsCNHUXcpGUw-zgaY7BUPwuGeFfVtxQjUNaIInKvgLs12UDERkFkAEG5UITwPyqM9ncedyfZhqXfC-kPqzmYx5Df6kCFfdOZqpL6IbyxyNk1ZhUUcdd_QH4RuKrhzvzKwBN0op_FbI9BPlV6t9aztR1f4lykjRDOLhxlttPfaakYfTtwN3X6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حیف‌از این‌رالی‌دیدنی‌بازی‌بامداد ایران
🆚
برزیل؛ شاگردان روبرتو پیاتزا در نخستین گام لیگ ملت های والیبال بازی رو سه بر یک به برزیل واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/23221" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23220">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq8SMvAs2t0WPBAO4neunU1e9Lbyr1Q9v3HpB0V_nXimH-bB7u0b_pUdw4_TcF8GjuHsEKND48e91eq12_EnRQuBZ9-x-z7tmdsmNoifEeCGqsEQTXNWpE7oDO-zr9qC_9G_tT756eZL4lM5U-dQh9XN4rcuz4RwS4i-lJZ09JMDUi4EzdPIAFBqWQk9C_pDAO08uqprCUHE5169OZuIeagY-X-UlfVe9gbuLpVUhCz4hemlnJF0GET6-rh6g7w42bEU_s9ZVFljEPfV9R8mILudFHm5HPEMMqVMmwQl7RPbSJ59Rakc4YD6b4kv6ow3esCdM4ykh-qPsnLHjLbWKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مربی‌بدنسازباشگاه پرسپولیس ساعتی‌قبل به تهران رسید و از فردا در تمرینات سرخ پوشان شرکت خواهدکرد. اوسمار ویرا و کادرفنی‌اش نیز احتمال زیاد پنجشنبه وارد تهران خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/23220" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23219">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDm-Wz5Nr7wjlrztBQSxE86D2hfifyvwrTak0Uql2Bh160GeXGG9i1UetRxu2H_vVyG7V6d7IvU6jNZ-lKc1Sv4YGc9RtoCyA7-78uXx4FDuPSnba_NzNiGfdYhV-1m_BVUZRoBpthB9bt7L-_FfY3evteE4WW8cB9lbVmbihuM33G4KOWEeJPETociUBIS5Q4lJB6lLcqxww7PSBUM8keJenB4KVqzPDM4EGcMj3BZF2ujyIeQJN1O88qg2i6iXl3tki3cx9a-EpwsjYVZac-xtNPg3EEj6d3rOO1PR6WBK4aRJ0WFD5uTu6OPSPj0lUHE6cdPi5lsKoMdscZ8zdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/23219" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23218">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw4MjlnmPVC3UrCKAqJOPfUzEJGsWdHq3vlK7AoMp_uZRR1fzfx-r0zoqgJC2bkS2MgGGU7g0jBSTRGg2vnUUu7rPRvCq1037h-ACp7JlLxn7LoUS44jewN9BHAy4KWpEhFd6AWxlZyKqNDpWtuS-ukbh5-IAYz_NWIFCEKMUYEuDsJLVCuslZK73u7fsQkhY-5gI-gGHasNFKfgV3p8V4ZURyR5s_1FAvIVz8MQx9RzcWmOn795wm4G6ns_tWaOsW_dpHJp-pZKT6Bw-19cM1MOvb0di4_WXJyuY_QtHeuJHDMbCQH8nGf9Mlp24w9cRY1P4uQj0DppSFxgOrxdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/23218" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23216">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehNjU7-X1CmQAQr6scOwQzMvFVOMoQHs7-nRgrKbD6pgj5dVODS5xUybiR9vCdN6GvOs3Ooj4pvmM91GqbpFs2mq6nxgmhkIloqt1I57qGdBs5M6rTaTYyj8Z7KJ7332fKzvJ1LNdDqtRel9fNvlTsJnHhYrWVw8Y0FZDpfTvfY1-EJcXZgd2XC5ZiIUswZs1_GahOLb6_PXmDWse7gZahLQ1Qq1CXSIhuVi7OL96OGZL9E1sRZeoJFVnsMItdeglceQlt-qKbz5Q8AE57v2YRmuCWppMUNyr93HAywIFAgSez-PQGxvoXxqR0cEh8FcUnah_n1qaAoKr5J3PTujrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODZzKTfxpNjhJ9K8tkkLlHjtEBrjXkfecETwRN3MJux3OAIUFZYOTuqeqQtGELlASZY2cMYdzdSGFlNlx8WnVvzGxtMSH9KssGOWU5Onf_BOTeRtY8X9TvcNMIyELskJi1XbKhjgxBH-71f9HTzQQVex8sDnM2-8gspEGmBD67BbPVSBLx_qAXnrmNr0qtVMdO8DZ-sAELoKAthvkNopM0w3n2iSQL5iFo7sFhj6szjAQ-c1sRxV4vYTaLcynmzbgBd3DLq9_hG8sQaL7WvYpIcJCTxxV0PUq8x_658kbImLxrtZpOzniRk9xHYo4PIc5j28wzwseXr1C6EEkS0oqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/23216" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDFWYSzd8c3LCDiVLc8Gnofil7g8vaMwJEceKguBPlN4sF78WuSVeug8yMFsNFQrTlCOBMubJlFEDwvI58Rzkbu2Sv8_PfaBNk-b_0xK2mP3CTDAm2mJeVHG364RZNhugk0UgHI-pTGkvNoYrB9bJak8SBRW1hsHc9h6NIMWkCoAtMBkOevzez4LbawHv5n_hL96Rutv5nkJDUCIF7V8JWGpvyd8TL6JbVEKGZGeTxG0fLM_rm4EfcW8qMBs7Ra_O34zOjL0REwH3Q-EhrZZlfzrC8XFBajXbFpLxAryWKNkEruO4eV9i7iUBtQdFWLuEahWQRTQSgO-MDHfXW7Uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
#فوری؛‌ خوزه‌فلیکس‌دیاز: برناردو سیلوا ستاره 31 ساله تیم ملی پرتغال برای عقد قراردادی 3 ساله با تیم رئال مادرید با پرز به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/23215" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=Yixy0jLn_FGV7PuvBnlq1TvA5szmcGi4GJgpWZ9P2-vJD-qhWbsCvUdtv6kATMba0zWwyvfAnTCG9NUUFik9Z-wRjdAeXk0iYX51oiKShymwnwt69MZCa9tgeSV4hyIuJ9ZeMSw5jJASQ5gYMSMUIqW04vUCTC5nNcEC49rjrjy40jmWO7DySR7H_XxnHDqKU0No-CgXs9w4l12d3AREmlhTZ3YgPA9dV0G0zlbYH2A1-jCHuVXS0oxcI_VNPq91K9ZtQRt-9tS1Nk8uB9uLNu3oI5XPkKQcK-ish7W5mKKyUGwjL_UyHIZot4JznpOdseiVdno94wxg9lVillIThA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=Yixy0jLn_FGV7PuvBnlq1TvA5szmcGi4GJgpWZ9P2-vJD-qhWbsCvUdtv6kATMba0zWwyvfAnTCG9NUUFik9Z-wRjdAeXk0iYX51oiKShymwnwt69MZCa9tgeSV4hyIuJ9ZeMSw5jJASQ5gYMSMUIqW04vUCTC5nNcEC49rjrjy40jmWO7DySR7H_XxnHDqKU0No-CgXs9w4l12d3AREmlhTZ3YgPA9dV0G0zlbYH2A1-jCHuVXS0oxcI_VNPq91K9ZtQRt-9tS1Nk8uB9uLNu3oI5XPkKQcK-ish7W5mKKyUGwjL_UyHIZot4JznpOdseiVdno94wxg9lVillIThA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد نکونام در برنامه زنده خطاب به عادل: پائولو دیبالا لامصب چقدر خوشکلهه این پسر
🗿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/23214" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/23213" target="_blank">📅 21:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L42VW5EeJ5_hdZ7Y6KAhT2cJc01aMKwjn2A_5_jRIbcnaNuDSpzoFcUnDprOoNzLDqkDFmxtSm2fJvLn5_llfM2lg5tb2xU6NKhM9hJAaqNZPoDRgCoYlEx_zEqD-cpj_nI_0sN-3oGcxt-n07tiQ915EGIy-68tliTeP2DxAN8znrwVgL-iEfGFZ9eBGfYU33fv-S3Fa6KOuxnAnUlCnPAK0HfbjA8ErGpCft9Ce-axSSSoAhcq94KvOGpbf91eBsp5CPPib_4hve8YOzrTA_R5-TIp8bn0fjZdfJXCfYbtd_UEXTjV3nWXSQ7xhA6fCIEIM3UgGhtjNX0d-GDFVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇷
صحبت‌های جالب پائولو دیبالا ستاره تیم ملی آرژانتین در گفتگو با عادل؛ برگای جواد نکونام و کاوه رضایی از این مهمون برنامه عادل ریخت قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/23212" target="_blank">📅 21:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23211">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTusUy8DzuqVvANVkzZ71uEUjBigTeZTiIio1CoNDW8cRt3OqWFM1b7Dj10xSZS94oRXS4t7_6ylDojoX7ce7NhIsz4r3uKVvD0EWKouO_kx_r9RLw-vv18OiPQzKKGd07xTWMeKwZpWWG5Rgcx65lXJ750iju6ptGJPKuDBiXwspypY2HWkW7oQaitdAFVVzoHFfGNCdrwanDk7jbVyj80-fVrHjM5n3a6woLcZ1kU9sd4hmDvMyTRzIsFiVFlMwwMaoKSYRGzqLJj9ZNozNlzjV9rYZ6D0XUxRSXk9TRtYzgtmoFpH3lh9UHyOUAJfiDDBRBZyT451JaL_97eujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ باشگاه رئال‌مادرید تا ساعات آینده خبر عقد قرارداد سه ساله با ژوزه مورینیو رو منتشر خواهد کرد و رسما اعلام خواهدکرد که این سرمربی پرتغالی بار دیگر به جمع کهکشانی ها پیوسته است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/23211" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23210">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9Vq_XEWrvs8Piu-YGfeuH5wUXW7qau_aTs4LkIModGPzxw7ECvWuO78STMBjkYLhT3EFD5KQUZxyHPScVTrGhgaxsFsqVhZnqNmHUdBtk_6xqkqDBAIlUkXQDprGShl4bB6ATgWySLv3SOvXTQ64Jfv8ejMggcIbm7gjbnprKF-_LSCxzjB6jux7YOm4RUNcc_aD15psXReC0-jbPDX9OknmHeNqjzYhy8vVhXjcpFef5z8TTDFfKg09c3G-yJ_4E6ER2JJx9gQlzE73--MCOltbCiJAzVkdlkkeLnAztw7tebb_e0I__miWO-f8G-GEb9szHznOy_lCfYZ1J_mtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/23210" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23209">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=KHvsjYfxqQiKP34sEUQEezR6ZGyVYKlKFEBhh47Vu7YTS7gR-Cz4fi7zsgA62CP8H8qWNozK88jlEB0kQ-ebttIAEheiTXGpamfUR1nsz55kZ_V2cC2XSpIvAlXtpni3Vs6CUNXowR595ahJAARV87b1cOmwng9hTFRs7j-86Awty1mNB2p6Ow9F3b4ylhYASp_6rjUzxO95r7IXvJEwwJUoE3XicsHwBSMiwk3xpHP_v0JEQwZ0-ZmtpAi29kB8z4K4NALuIakrDCyAAIStiaQJj2ebwTEBwmpJ2ANlNeqtZDaBIO_3l8bwLFPxYjV9AM-JRwc1wC2Qk9X4-nIj4kjS9n_NYigB996mN8t3XBXbxEt9KCoG8hiqwipAisGk47Kj5v-AsqPbUC_VZTZ58XhAn8Qh9jU2rhS3toRFay662w-JEM1ydxpnUa0PP-mQNtNAJfwbnhD4B_4WdoTWMXUrRQoHfPEqQzeaNXrzlcY2t6vLboAVlaxxMOToJ537W_LCw5tpDFogJrO8UYeCO3XXRB6wM6f7QZJIqs9fsq7h2joGldClzO3d5K1NemsxxDzityTNVK7jH65O8ha3BJoH1cGQeZhGrzwWaPeRyfY4eklO6kXpNG4DdkjOLaFhmgnVnfDtRZnkg5rOJTutEI3ECV3YrbHkxlePDM1Jw40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=KHvsjYfxqQiKP34sEUQEezR6ZGyVYKlKFEBhh47Vu7YTS7gR-Cz4fi7zsgA62CP8H8qWNozK88jlEB0kQ-ebttIAEheiTXGpamfUR1nsz55kZ_V2cC2XSpIvAlXtpni3Vs6CUNXowR595ahJAARV87b1cOmwng9hTFRs7j-86Awty1mNB2p6Ow9F3b4ylhYASp_6rjUzxO95r7IXvJEwwJUoE3XicsHwBSMiwk3xpHP_v0JEQwZ0-ZmtpAi29kB8z4K4NALuIakrDCyAAIStiaQJj2ebwTEBwmpJ2ANlNeqtZDaBIO_3l8bwLFPxYjV9AM-JRwc1wC2Qk9X4-nIj4kjS9n_NYigB996mN8t3XBXbxEt9KCoG8hiqwipAisGk47Kj5v-AsqPbUC_VZTZ58XhAn8Qh9jU2rhS3toRFay662w-JEM1ydxpnUa0PP-mQNtNAJfwbnhD4B_4WdoTWMXUrRQoHfPEqQzeaNXrzlcY2t6vLboAVlaxxMOToJ537W_LCw5tpDFogJrO8UYeCO3XXRB6wM6f7QZJIqs9fsq7h2joGldClzO3d5K1NemsxxDzityTNVK7jH65O8ha3BJoH1cGQeZhGrzwWaPeRyfY4eklO6kXpNG4DdkjOLaFhmgnVnfDtRZnkg5rOJTutEI3ECV3YrbHkxlePDM1Jw40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/23209" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23208">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709c123d60.mp4?token=i8VuX0GLO3PAlDBkOFfYdKCMWpQoYpeUsCo8u6Tod6xBeR55LJS9hBpjJ6Cbs7uUADkyINxCA_N9rEJobkVilLGBHSKFFfncsJmkx8n3R8hJIBZ2-eltKVrajpOm9PJz3ZmWCwCviK7tFQQUwsJQFJ6rzAJDDb2uNYFIfMhNWQUKCGOVP5c1p5xtiErhu7JvdNSJFIJ5qzPkXg-YAf22kHlAQSuAKZRYqUM7BANdY1L-n3LqGiEfkYnbFKVFeSn1OYTd-Rf9pKhca3CrAwJalNJT0xrb-CR9ZMERWwH4hi7WOGJ2KOH27KMzNz3hV1ZRY_7ML3YuVJtfOqZ96pu-dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709c123d60.mp4?token=i8VuX0GLO3PAlDBkOFfYdKCMWpQoYpeUsCo8u6Tod6xBeR55LJS9hBpjJ6Cbs7uUADkyINxCA_N9rEJobkVilLGBHSKFFfncsJmkx8n3R8hJIBZ2-eltKVrajpOm9PJz3ZmWCwCviK7tFQQUwsJQFJ6rzAJDDb2uNYFIfMhNWQUKCGOVP5c1p5xtiErhu7JvdNSJFIJ5qzPkXg-YAf22kHlAQSuAKZRYqUM7BANdY1L-n3LqGiEfkYnbFKVFeSn1OYTd-Rf9pKhca3CrAwJalNJT0xrb-CR9ZMERWwH4hi7WOGJ2KOH27KMzNz3hV1ZRY_7ML3YuVJtfOqZ96pu-dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور تو ویژه برنامه امشب پائولو دیبالا ستاره سابق‌تیم‌ملی آرژانتین و سابق یوونتوس رو بالا اورده و داره باهاش حرف میزنه؛ صداوسیما هم داره با خداداد عزیزی حرفای کارشناسانه میزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/23208" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23207">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPBHq0HBuJiGLdlBNTXYjfvX9muQuVV9x2jEhsCyZsf4QMv82rhE3TkvAm0G70BDZh_QFuMJT_abAdD0_NZ-i_WvLkopIyyUFvYnAwoAC_miTKpuvMOZpgZWIxpLL6xCMOpAxkUUx88J4NFz7zgLD3Jl0lrifsCsOkX7ipkPfEMhzMY-VgaTSZimdYqWnIsV2wzkFG48QxjdRJSAKvlGv3ISc2Y_645VAh7fWXWIZrX0auPIxwj61HXFLg93azagWmlaS7243y9QCRKuqqCf3Ib7VVaf5UAx1WZDWyp_KnIkJbagP-R7KaFiQ-7eJsOOu0JHc4EQRZcRlcLJUgHqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
گروه همفکری شرط بندی | Tips Group
⚽️
دنبال پیش‌بینی‌های بهتر و تصمیم‌های منطقی‌تر هستی؟
📊
تو
Tips Group
خبری از سیگنال‌فروشی و وعده‌های غیرواقعی نیست! اینجا اعضا با هم مسابقات رو تحلیل می‌کنن، آمار بررسی می‌کنن و ایده‌هاشون رو به اشتراک می‌ذارن.
✅
همفکری روی بازی‌های روز
✅
بررسی آمار و فرم تیم‌ها
✅
تبادل نظر بین اعضای فعال
✅
پیدا کردن ارزش در ضرایب
✅
محیط دوستانه و حرفه‌ای
🔥
اگر به شرط‌بندی ورزشی علاقه داری و دوست داری قبل از هر انتخاب نظر بقیه رو هم بدونی، به جمع ما ملحق شو.
⏬
@Bet_talking
⏬
Download betting apps</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/23207" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23206">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXQYH367n-FB8ZB-FSOPex96yrjlX__EdwesqOptg1QWNGOwxHT5EHnbPxnBqfh7nULOYri5yr_Ur6qm3nzkMDktDSTA72iTi41opyrMtYJDITTsZosRQ9m7AbNyFjzzq_w4tx5zyZeM6WrEDu3exO7GzRIvANWbyzxTuSVWULTHlovm3YDYudewxSKOPhWpKuIPDCPl4UPoi6737_RV8-hbptNWBKNoNb_5VDTu9T4i_JNNX-9wWpWPzLQG1G79GsxYE2x9KO1ApdCwKzjQ0M4dEy7Rlc4LsJVWvmQyVYUt-PnRPV7Luezi5dtolbQ6fEySKsQrLvm9HSSiZGBgNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/23206" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23205">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB6jyR4eIuWmpmTVUjytqF5IFeJykCmPo8WHgyERfKGHFETjIsaq4hXr3q-6g-xlH0mSV6XQsJaDX9OroCF0CijvOGljNXQUI6v-dTMYTctvzrxVWtMrpmnL7W2DmKTMm-h3wwF-pa7gjLac6BsrgOXO8xtexHQhSMmBKgGTdkgV2G68zEr4dNSBUY-c5H7c6ZehD8rHHDCDLtn6N0GExcd02_VtZnSEo5SBkpVwpHs709w8ifaoQhSB5Okeg4rZkUUYRVzo2qNd_GCEc22OyW_XmA2hVS_4Y6ol9ol0NWjBwoQWlE8hC5FXL5uHudVLgtvG2FrGSpL_mbEmabcocQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو: باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23205" target="_blank">📅 21:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23204">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBC9wMqR5ic2Lzvz0mATe1ELFe6XZMhCWYbPJJae-dP3Nyar5vpSgbdVX_j0k61LUN8CuWNSe4JIbyTC7PxuHpSDCatxKdBSH3WvDODC4gcy3FYMvYwswrHHKLHuA6CyAFkCmfpmy62Xs-dksbTtvZskailrcsZPWIMl-GgAme3M79Iw7y7tkE-sUFCJ6fAPg3XedYilZ2m-v8OKwMykCmyd3edwYAWqYzELLU7G3mwwnyPN11NQ9r3eerTrAFcVpPYmiknnve5moNPWZuY99r73KzgBqZLZskqPXfhgWNMFoCsbDBOKYDa32SvYy_Gn8LZD_1Hou_w-7kMXPb3aXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/23204" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23203">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePQ5kYzkhcAjsb5wo43q0BhglCVQI5rLfkmDOyK5eDUiFWRZzJJqnkCBdVHgeHg-F2im6SbHNG5GaExPxyQth48yua-fxq7Mp_NB_mYNlReB6LM6ZeV9rhlH_Eqd-6HKBUKNGpoMHzkV_rIwk9wi1fP6_mNYZW9uZHBgM2c9trHjBhpjhomL36FaS_lW2gyscJnFfyYn_WYLbkPljB6EJHXWsOmOYPD5W0LIZLmB03vF5hZLu_k09fhtxH5ZGPdB8dgdGFuWXHk8VfJV0OI67sr1ht1n_5kvPtc5UAOEA6DO2TuFNTP_NRY3mbZCQpdMxgYz01x_VCLz3kiJGWomFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23203" target="_blank">📅 20:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23202">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWZuN9Ev_SASnpfPkYoJ0N3IkP9mmSUmVqzV_CqbbNqdapgDfxPKHEElPHN3tyH235enG-hLQ6yyQJizNi69sXRpQ6jOUoor1lVw4cvLo2cwn8J1CgmjUTTvneHStf7J8fGP-HhBwmAKvhsbCQ260hwebWcZPYqpN0oWyxIxvfZxJCsvO8t7f0eEkvzVDPCq7HyP4FhVkrlc28o7QxmYrQz1Uc7fR_B7CGZgKOlo527LUg1efvJNlv48uhvJci_ty2yZ0rV9EzpSFXSuBph8sf-rGi2CYZK__sWp07O1psTSc0XWsPLQur3K05TD7DpNrtWIE71Jc_cmKgZOfdAdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/23202" target="_blank">📅 20:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23201">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8BFp6AOtqg05-uYrj_O3FpV2HrlWXPWNsNOHukSelMMDO6MnCMS4q3YpLZDhLfPlY08tNsB2MX6_oraooeGizwhS_UwOSNCpHk7sccNVvBpICckhwUSot3kNeTSetfPRqtPZ5UTRpoQ0JXbN2uv8D2RWDGCOyxgnnVLM3CthaSM3qPxcSLmU69C96_bNUHs7LoypH2bEQZUp73T6BzPaA94tMwSHCliN7C397en0U8NGcfpxKkRnmhRD-Te9vBGq1TP1gQMcoQWf5m6Alyl9jAzbBauJ0bRZAk6KRWEWqsYLZqVF23pvrwVRha5u2PwIEvX5GVw-RuBwTwa9xCAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو:
باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/23201" target="_blank">📅 20:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23200">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2P3XPQejSKOPhba5gRnvnAHQUKaFCAwJJxN8jAThzsz1U8SHu_5BJgbWNeFvGHv1Ou1mgOBbz6_EiKdxuPX1QQkpB8bG9uUcPKzaM8N8KnlLZ_bkqyOS2LNA-yV3bAZZSGsuweuTiNBNvCkT6JSp9RYJGSvcW7BYvUVaviWwn-O_VCjAuSbfz6H1FwXbbBzNGdir9Tu16Kx5P5j3qVL1XfEZHSBKIM_b2pCNXf-Q2jB43BGnqMCi2OjBBwJ4GqQh01bZyGfpPubZ18pOf0lR9rsW7vhUZkQHPxadQ0dFlqzsfEHv-zXBF1Gg-OYAbG1cOJPH_3ASzsh3wgbFqxpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقا از طریق‌کانالای‌بالامیتونید مراسم افتتاحیه جام جهانی رو بدون سانسور ببینید. خودمونم سعی میکنیم در پایان مراسم ویدیو کاملش رو در کانال قراربدیم برای دوستانیکه نتونستن مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23200" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23199">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaZyNY7WEQzkBwrMi1fHDAYd9adFiM9Tk9mS2SLpzo3mmJyIYc_NXE8eUXUcFZbL9Q66Oq8TSvcIh0By65ugdSAjt569fDRxOolJZUUoJEni5w-JlM7c3UtxP832Hs8PIVV3Djhu8q1lvvZ7g9yYeHjhaI7yrB6X_UYXyabUoONsSCozD-hhcpv9_iE03a6yhkBv2KYpsxZSqBGN0oRL6r_7Y5bUlSCsPP-ScOfkX_ckeYSfBufB15Mk7BSPeZwuj0wrc740BWXGwwffddRfHHWe9WD6lRGqETNuldoX_hGcsjpN_tivu5iCg72fZgn4Ixphe1VKMKqRW01k8_pIxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان: بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23199" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23198">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flpcspEXHEd6n0rPcI4RwCVV-kwsH8A7nZrEDsPrYywvJ5wAAU9SMU6mI6XgYw7KVTQGlPzLOusOB923_LYrLqDBqHiEhAH7uTSl2Vwmat0I4cAxQUGw4r5ryFTB6ZggT1jSS5E6fkORbZ1GY2qHpbeiJWpSh8pr9zSN3kOopyGOiCOnFok1AmcXj1iGGkabQIBNj_pV94m181NSWmAM1ovhTJKIb33cRNKQ5ECp5Xw7Twwqv9tpOEU6m_1ocNni08WU3WROLDl1SY_pD9d6GNQ-bfvC1027LkdF5mldIOy3MCBRAEhRfc815YvsaXOQO2jk0NMb49dnajIjndUAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23198" target="_blank">📅 19:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23197">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSwFppBjponuuwkzzXJ_7-rF1X6dYJmkLeQqXIPuKllacymlTOOFv_sUlxLVsAYui5cJ5AVZQMk0xsum7dIDsItWQNuFNqKa2ua45mduR0cl6WnNr8uvDUBTyzMExodgF5hqdMYCbusl2LXeMKqOv09Sz8jUfwRv7y-e8-pau3PV_LIq4ZcqBxGBMjDJ4b79dWvJSwtUc7_vm8n7hVnlGwcYp7MAfAAEWmVpBSKNzWPoJ-cCNgqWCJYQT9rJX7MfMJHR83aOCWS5-ijmoEO87dOIdem6VccL5nhS-k9qrmvEwCG4b0Luyy5WI45nHOtFAilKel9a6rJe7wxOvAK-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/23197" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23196">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDO4YTQ3xrFLqNnGxMe6VhjjbTnlubj1SeccuXWaoGHgKNhEW33LRlPl7XhsZrodQ6WgXYZ4gIrZHuUAP4JMj07adAfMoQBYYgAb7XurHcVUBlShm9hEqOkt4WIpBiZ2OAG3OOrpBdAWy6Yntv3Mx6ypYhT5JAM7dIO_cquA4lWiAYD6GrRjda-323jttnOhMyaQTvmh9SESmLI_y0HgMIe2yCnXkfSorw0VUREdi3Il5VJhmu3misL3E65GRyi81kb3gx8kRAoARzHGgyFBJOABy9acio1r9fNWImvdwbFgRB49mSGKTt9SfuCYV8DAGiaEElyrW7GPDJ68R0uFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌افتتاحیه‌رقابت‌های جام جهانی ۲۰۲۶
🔴
برنامه افتتاحیه در مکزیک
؛ پنج‌شنبه ۲۱ خرداد پیش از بازی مکزیک و آفریقای جنوبی؛ ساعت ۲۰:۳۰: آغاز مراسم افتتاحیه؛ساعت ۲۱:۴۰: گرم‌کردن تیم‌ها؛ ساعت۲۲:۳۰:آغاز بازی مکزیک-آفریقای جنوبی شکیرا، برنا، آلخاندرو فرناندز، بلیندا، دنی اوشن، جی بالوین.
🔴
برنامه‌افتتاحیه‌درکانادا
؛جمعه ۲۲ خرداد؛ پیش از بازی کانادا-بوسنی؛ساعت۲۱:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۲۲:۳۰:آغازبازی کانادا-بوسنی؛ آلنيس موریست، آلسیا کارا، الیانا، جسی ریز، مایکل بوبله، نورا فتحی، سانجوی، وگدریم و ویلیام پرینس
🔴
برنامه‌روزافتتاحیه‌در‌آمریکا؛بامدادشنبه۲۳ خرداد؛ پیش از بازی آمریکا-پاراگوئه؛ساعت ۳:۰۰: آغاز مراسم افتتاحیه؛ ساعت ۴:۳۰: آغاز دیدار آمریکا و پاراگوئه؛ کیتی پری، فیوچر، آنیتا، لیسا، رما و تایلا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/23196" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23195">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukftnOZ6gYHnYLZPkZSsfFi6HUnRV8nUqRz7gVfrjICaFx7z4yCsLRHZk04bYCjuCfx0fnNAxQqoWIPB_3TupqSrjlmeLDQVOW_d2DTKePV2Wa2sEcalRAT3dOb8UIu_jGwI5revV6XtospgT4pvMYBr5sYrq_D8ZFDk6a_WD-SbOO80-Mr4ZM9cQy3ESzwU1Mo8jht8tSJxZ76SbNSNjKbT-h0C9FqDu6RTQ38UsfLBk-2J16d0pbxJO_kx6-d8UOO3STDubfruaPImZkJED1PUXbx3TnQyKV-lTdCn7PFhhywCNs7seirdurntKf-p8TLar10JBlvFxj96iXqj_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg21
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/23195" target="_blank">📅 19:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23194">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsiJ9xRdnn9GtpW_au47JJvEE_qee5ZDgbdJn8FJyVlrd7JhRI0H_xLmb4zaVRzTRiQvrgex9sli_EFBOV1e43rXIEbLPkPhFMhvyCcnMjva_GON074Rct26yGDz3nF1aFychcYEZ-tdiaBwgWds6w3xdqoYP_EQUG3Q_21UGyKd0AhoI1bIMGfQu1PdUUrwqcEVqmKzmSVot2pHjdjNcnmikiYAhjG6TJQvle8JMbILwy8QVK30PAP7DfOSJcF9KYnCGdCWa5mBf1_HM4k5gmRJynjTtl-P3jAkEg3FsWckfZF5MsxjUIgqDf6BXmqYYUteeL6ryvsSgturzA3v6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23194" target="_blank">📅 19:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23193">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGuBDWsI4JklrlX63fZ9-spj0v9b4uUCDYM_MHy4T2qZu24ypL2Hatktbd88dcqFR-yvdVKm8cfsiWWqAhOvpfXHs5YtWsRFCFomTJePsRWHENBg6G0-jF_meuSLBYBems9GFVBucZe5hNo5EoL1UpN9qORo6m2b9C8XW5gvRDT0ybVMZ_dpJyCgSZvne3n1fhTKeCUG7V20bzPYK6MNLvr3308Dm005sl8BLxz2yEA9xmQm1b8MjKjqCAQ9DSPGugcDt8ex5n0raFdAaB7Q4oRcnCQgzeZ1VjQRLmYuxqjPZxpDNg1XGibTvK59XRkSccs-L8-4pCRnkKm6xcfyHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/23193" target="_blank">📅 18:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23192">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=CPs3jJEQK2HOaouuGjhgLyfqf9tjeKJTVo7trX6AJu_qzzupGXtGS2f_C_69ax4wOW1IeXF9oEn0AOVp6zHxxgsTTYGG0n3RFak8G84Vv2dcmILyKhGIOwvSmGtAKl4vvcuJTX4kbezaIyytt8AV4uqvfFaH-y4mfQYnKQy_8ur-4cKnwd6OCfw17z3eYCZQls7y24K9Y8QkOmgXjwOtd9d5vs2ueOmFw4QSd1vyOeOvVTfVMdpwyV4FnS9HOq_-FAaqTzF7m0zjwBDFL6ysqirN_lLryl7dEGMQWd9seAp5OJBkBsKbRVsvKm9w3Z8m-y4v_XPMgjXmC8ccKCe70mOOvQ32pGwKa8_CcJdJTlHlGIUBaxOOFQ_yRu6kPGyjrpbssA4D_kLtTSWASP_y6XAQFo55arDYyAjp_yhZ7amcay76_DxNJ8WXLgMdGeWtSCfAMhnVDDBIAUKy0QIdyWOG1CnZ1tHZnoGB226UKNqHykYU0TE9eTT4S_yFH86h4KwPJxf36YymM5n7fBGSDv-J8S9mvMBGFSk8LI3ENUYYx062ClrQuqeUUuz8aqsCqEjUlsnzTEWHjqQTkTI8Z9-s9wlJ0JdInWponoIC-8Gxg7y0mNDSUDI9jxmHZw4V9rmuzHHOJbYikjLKqUdSFRaMHVMmR0j4PgxMIAavWDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=CPs3jJEQK2HOaouuGjhgLyfqf9tjeKJTVo7trX6AJu_qzzupGXtGS2f_C_69ax4wOW1IeXF9oEn0AOVp6zHxxgsTTYGG0n3RFak8G84Vv2dcmILyKhGIOwvSmGtAKl4vvcuJTX4kbezaIyytt8AV4uqvfFaH-y4mfQYnKQy_8ur-4cKnwd6OCfw17z3eYCZQls7y24K9Y8QkOmgXjwOtd9d5vs2ueOmFw4QSd1vyOeOvVTfVMdpwyV4FnS9HOq_-FAaqTzF7m0zjwBDFL6ysqirN_lLryl7dEGMQWd9seAp5OJBkBsKbRVsvKm9w3Z8m-y4v_XPMgjXmC8ccKCe70mOOvQ32pGwKa8_CcJdJTlHlGIUBaxOOFQ_yRu6kPGyjrpbssA4D_kLtTSWASP_y6XAQFo55arDYyAjp_yhZ7amcay76_DxNJ8WXLgMdGeWtSCfAMhnVDDBIAUKy0QIdyWOG1CnZ1tHZnoGB226UKNqHykYU0TE9eTT4S_yFH86h4KwPJxf36YymM5n7fBGSDv-J8S9mvMBGFSk8LI3ENUYYx062ClrQuqeUUuz8aqsCqEjUlsnzTEWHjqQTkTI8Z9-s9wlJ0JdInWponoIC-8Gxg7y0mNDSUDI9jxmHZw4V9rmuzHHOJbYikjLKqUdSFRaMHVMmR0j4PgxMIAavWDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23192" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23191">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTySVwZfIey8ZUE2OBeeEYPqkoN6deazvKEYUw7KtOtSwzzi4H4exUhFzcQlCQHRLj3Od96XvQwksiemzQ8DcE9E5i1TR1KIaL67vJRdKOSP3--1onEATf6ah70zaIJAjgX7Mg3EU3TvXkPhy5hElVLkoyp40gY6RKynbXxAr6fXZ_wj2j1ISTGE8nn8WbDbyD0NLTY9j0q34a4oHhSkaVvsGvOmAWMr6d422hXXnSx1o8mpu33leglElilDL98N1tQp3nw87gA9WldChfIemRcfCvue2107DtrenWABCNFzkgJ9cxsZxLTSPuanRISU9WuLj8q6G9eYxAye4TW09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23191" target="_blank">📅 17:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23190">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT6BOn1xr5pO70aBamuqz8gh4kaYwgI8fHVN-IC3orevRZRPzboeYF-pEc0NpGIIslFwSPR8IZVctqROiWpzYiJYHhVbXHRBTXjZTlMs6a_uCp_TMwI3ZBCnpoCs8W8JIbV40BwAiW41hsl469NIJarRbWx_6DShaMLRp3U85iaiLE6dMNDJvrIq9U-HlNWczsbnvGfly6R9n16CWUwA1wtAo9FElfnzHhfayx38ZZsfK7nSvzAKDbBzS46bLw_EGmwwaS9-1girPTHrNrRkTsTXsIW1fhQ1OsbYhwEmYj78AmtnoY6gIO7zp_gbedDyT8fk4_UWUsmKAJx1w_PQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23190" target="_blank">📅 17:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23189">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_3M2vUg0hvtybZ3WEumhcJCWOem_haVxPOFthAhvxS2lwJj6tt5M5WdcpUlfpD7GSJloTvo1bc259fyhWefFcgHS2HE3woipHFMdOqKE_xeD2l8JdQ0Oq7bFEEWwDtDWI7QeSeFm7zA36faS2JLmXzu4QuOy0ipO2lXWsmdAIJsmhSmOPFje6ofo9SZP-ZWhDHu3Ue1J4LUUhcGskq2ZRu0tkDQOaKfJ8Pw9finQHsDKx2P1JNi-BGfSGk3gGRGkx1F-9zWOLRxwmaV6YTkJGBoQ_-Mw0-3I3HywtsazZ8Jwx5OgQZARURwcJeHRdwRVaZBcJV3rzL47Kq6yIGIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیستی‌از اموال‌برخی از افراد معروف کشورمون که درماه‌های اخیر توسط قوه قضائیه مصادره شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23189" target="_blank">📅 17:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23188">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV0fHxocDBSCnLpUQRRCB5vDs4bJn5bAMyeJ1jMKg-d8Q2PoYPOeGYKUT4P0e511ubsL61AMLFe2dwXZOtcrn4gvAp9PosKTuKTl9NsanxHZQZQy3BpkzHXt3FpVW1hT2UusLjR_mKwaZSc4b2Kjee3vaaPMh1v40XJlghpymfH00CZ6mUge6R5Rgl5737gkkqr7sBNq6jjGWA1q95dcm4MANp8Uiu_aRMuXR18jHfKBBTYhLj8CyA1ZeX39I4HaRtWnJZ_mWIrQXvrGHC7v7zIH2tA_UE5zKxtqC1VLBjaVf73mXl44nUACvrmnC4L2r8SFwz3voejkpf_uIDcsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23188" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23187">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyZt8ReuktX6a6bcwS0Jl4LARjtb1NHweMx9aCqDccHiInlnqYsmC2JK7GltSHQcxm66xQAJ5JjFd0hX2SyhWsJWnDrgJFMWei9i93LbAe6LJDjpa0r1Lhquayv47BpJi5BlBc85YmK1XgIt7eEZFzqZiTSJyt2YgUgQPejv4uzMU-a9k6YrXqcjZPFD3KPtylA7SA7Gt4P1wpfe18BtNqwRU1PnkO8qGwiS11MbmC9OAo7zXG4_iv6mgP1kMJ8lMpVaERMH1nskAHcnRoZ0Z98iW61YQlJcjg5PEL_UjGcgH8nP8dR7C4NGruLkCtT1DWaLefVy_s3Q-xibSsGcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23187" target="_blank">📅 16:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23186">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG4o0UwptNahOBlCDLu9EFQyd4OSEMcWx7QS1dCo7H5elusQUeKlMwkhJwjK-oOAjHEj4Yzz1MZTD38iKF0W14-0lV7tcw8dXPPf29fAms52gte6geD4uU7wBa5IRP0S1cMjL4ynju4J8RLT_fnxI8FgVhUK_4RqbN1gboBWz_4cxyqeqncxo5gaeigl-LEM2uTWaNR23bOFzvqQjjeI9wVJDIsppBH2vpGawrr6pxrY06FvLDObYKfaSCfvpcFakwaTc2EOXqA3CTRHbUZ_em4CJNM02-lIDROjvd4b42esXq4zIIw-b88aRbCTW8FHWLCjQUYaA0MRFNKdM3edUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌مرحله‌گروهی رقابت‌های جام جهانی 2026 در یک نگاه؛ این پست رو که کامل و جامعه هست ذخیره کن و برای دوستات هم بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23186" target="_blank">📅 16:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23183">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvezFDGDUwFE8J3YPbsgpZw3hvna881FPRgRYYagTGonH9zvPhsZH50zHe18NwBS2JUG2fqQosbaccDgsmn5gUOP36GtBFcZYeFj8M1-IVes_sP5rnX5eh66DQhkU1ZIOjkxc5AHbJ_e76S-eDHGfetB0AZx80WZhN_gFuVNuR_AIVrZt1SuZHm_gQYfNZ_pi04T72IRxeeYUS92cpoXVZXEpjkWi3A4l9CF1-84eMuGZxce1cTRaY3w1fIewB08jXaDQklXE_GP8oCgv1T5h7hBlNiUUXH6N9c84gXSMKJ9wpQJpA6JcdviOeG3RI-ORru-BTDerl9exDn1uoU7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=MdUsYZJIaQ85iX2zp8FQZQj9pgzpmesQlGm-gT7Fx3V5wRLKKnbiJywxnOLah0ufpD4WGpbv75LRWgALGJzqTcs0uW_oMmw6NHZ5ZjUg5wiVG_knrlMi8pQNBl9CYoy7qkWNnn9557NBCV-AvD558uZMpAZI4uso96Ef3uJImv4FWE7cii3nzUyaGdxOvloiWElDY8xkahd_NLO2E0ivyEVD_tFvb97s-QKBwQRW0R-BLuSSigHJPEDn9y0LSUbfX7ULqAoiP0hDNGs9QE0ZHpakQU1UICD8riu1WlDz_LMhMzFlHlFesrOf96iTh9-R4LFt0UN6qE4dT4bdlC00Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=MdUsYZJIaQ85iX2zp8FQZQj9pgzpmesQlGm-gT7Fx3V5wRLKKnbiJywxnOLah0ufpD4WGpbv75LRWgALGJzqTcs0uW_oMmw6NHZ5ZjUg5wiVG_knrlMi8pQNBl9CYoy7qkWNnn9557NBCV-AvD558uZMpAZI4uso96Ef3uJImv4FWE7cii3nzUyaGdxOvloiWElDY8xkahd_NLO2E0ivyEVD_tFvb97s-QKBwQRW0R-BLuSSigHJPEDn9y0LSUbfX7ULqAoiP0hDNGs9QE0ZHpakQU1UICD8riu1WlDz_LMhMzFlHlFesrOf96iTh9-R4LFt0UN6qE4dT4bdlC00Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23183" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23182">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs2x9_rq81HYLTc3dmG05ec880sHJhbp9tlNo_vMEYhq59OGkyLRKZD2is1zXnU08Sya94AsQYhjIH4-wZeCrVlQnl21TaFYXerlDwZmx0JNBp_oR56LccgkDKV9oOf5tjaRlAnm9z86Xsob016K64bO1wssYeYfk2u-UHqEcpgMw-AbeXGIOdhtt2x6Una6-PLee7apJaexapoUFPGDsxZmlbi7I8mkbZGLBlr8gMFSD7_q7tvor4zJBWndRTFFc9ysru_PzBfBAW0QykPRGqLO0e-6MqGK0vgcT1rF2X5U3GsUZ-AoBmlozJF87jpy6k9OKQ4D5ve_6e-hzYByng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه بندی تیم‌های ملی حاضر در رقابت‌های جام جهانی 2026؛ یاران لیونل مسی در رتبه اول جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23182" target="_blank">📅 15:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23181">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWX8dBCyB-o8l61SRRy6zTrl9aCWWdair4c4dE9vslIZOW2jPbweBdo1ZGW4iB9iacoIcongjJ76X6vDFZmg98kEem_c0wM_DUl_CMQyOf_SsDLIbkQRwuKAObkUwz06ne_KJa9P24dUPPvYJTsjCOR81oIn4VGWWWwtVq5BaqR7JLSW6IryVigybddge0Fjd3xat4cBFQ2oPFt1K42T2WPgKcV7gtG4do7Krw6gE6zAD1m5FrpHRx_5S0Xd-5GJM4iwzeWHcrC_NNxLo6nw1DK1gVnM1RUEqKyzpoFHHSgzPzBNU5oSYBTcbe5Gl-lLM2C41924gdbhvSqGqlGcqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23181" target="_blank">📅 15:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23180">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=FQwOOAllXYB05rcOZaNAQZXjLAAnEq3dX2Xx6ezISxyOcjqXzfx8RhzsMEEh6o7m2E7sLEkWW8j3Cn3eEkgSUoWY5mlTZcyySpjwzhYakWCem2Sde_0UVm0MBnADsWrm25xzkY8oGzAor3Z3SfK47BKLAqZBjac4q0ExWn_QnK8nKdnVJZ0zQoDQKRX-0ikHDYUjamsgmNFQqekiNwSHcTHuDKZP8lZF9OUKMb_HRsQcIMPqurJ2siCLM5iiVTJjqB6D5hisuO-fBP8abr4VkJku_4lLM3T1c3qN63_ZKwWDR6MNOrHvF1VVgudfh2hlLreMbJAXqHb_vBetcFccxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=FQwOOAllXYB05rcOZaNAQZXjLAAnEq3dX2Xx6ezISxyOcjqXzfx8RhzsMEEh6o7m2E7sLEkWW8j3Cn3eEkgSUoWY5mlTZcyySpjwzhYakWCem2Sde_0UVm0MBnADsWrm25xzkY8oGzAor3Z3SfK47BKLAqZBjac4q0ExWn_QnK8nKdnVJZ0zQoDQKRX-0ikHDYUjamsgmNFQqekiNwSHcTHuDKZP8lZF9OUKMb_HRsQcIMPqurJ2siCLM5iiVTJjqB6D5hisuO-fBP8abr4VkJku_4lLM3T1c3qN63_ZKwWDR6MNOrHvF1VVgudfh2hlLreMbJAXqHb_vBetcFccxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
جوادخیابانی:
سردارجان تو الان تیم ملی نیستی ولی هستی، بعضیا وقتی نیستن نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستند.
👤
سردارآزمون:
آقاجواد حقیقتش اصالتا ترکمنمی هستم فهمیدن اینجور مسائل یه مقدار برام سخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23180" target="_blank">📅 15:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23179">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=k02C-y28CulMeFD9A0-XkKuiN-lfHarewDS2rlJKmd7qA01s7uRI58nA3hldNLWSMYLGpl71oqxSTwbz3HCPUZJNp5Ol0ujFQRSpJmGxiKpLmkNdJZIDCRj6CxZVSX7AenVKAAMBFBWIkhKYIToJccJFdnCVgUiV2BuXVcsWX8XqcWEjqW8MR8epEq4NEfQlBWvRlvY-ZQVdTG4UXfwec-990y-GDSlQRdXl_EaefVhp-EfkgVCnjmf1WL2Dg7HJ2uXgHbub_oMfBwn5T3HbgIVDt1ZUUFlHYlsfhkXqCBSQes2P0tcY1Ce1rZgiJGrvLM99rh_uoR2mH3ArCZnopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=k02C-y28CulMeFD9A0-XkKuiN-lfHarewDS2rlJKmd7qA01s7uRI58nA3hldNLWSMYLGpl71oqxSTwbz3HCPUZJNp5Ol0ujFQRSpJmGxiKpLmkNdJZIDCRj6CxZVSX7AenVKAAMBFBWIkhKYIToJccJFdnCVgUiV2BuXVcsWX8XqcWEjqW8MR8epEq4NEfQlBWvRlvY-ZQVdTG4UXfwec-990y-GDSlQRdXl_EaefVhp-EfkgVCnjmf1WL2Dg7HJ2uXgHbub_oMfBwn5T3HbgIVDt1ZUUFlHYlsfhkXqCBSQes2P0tcY1Ce1rZgiJGrvLM99rh_uoR2mH3ArCZnopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#تقویم
؛
خیلی‌جالب‌شد؛
دقیقا 16 سال پیش در چنین روزی؛ آفریقای‌جنوبی‌میزبان جام جهانی 2010 دربازی افتتاحیه به مصاف مکزیک رفت که با این گل دیدنی اون‌بازی رو برد.حالا بعداز 16 سال امشب این دوتیم دوباره افتتاحیه جام جهانی رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23179" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23178">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4PTcxzqtKBEFSjfpweXXEk9nQ1Wlj_tT9DBgmzHs9vccCqPU3Ztlgj3Fdiwv7QlLIpA9YgXLNFpq63b3hKCYIkPNVbNXkTszDyBKVa-H0UE9sehXDQW0hZSrlYahARgwPGz_Yizwm8ydw6u4LdP_SEwhopPNIyZiNr3vYnR4LCi9gP_Vg7AzVZbp0Q6ltAQ1KLGj81ROHw1FJbn6yb4GObL10WLKLnQD_kNJUjOLTnItmNmErGyvWCP7mB-cgU1eSlLmQdxk58lGo87Hzgh7MxkgJvHowOdQarLYI2QwsX-435WQUi2R5Q60zbv5abzKLE0peoUMLua0Cs-7c1R-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23178" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23177">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcQke7jTHwkRkNrkuefXrQsX5twN2zEld2vUHWMKz86pEXd50ZBCQMKKAU0GWATexojGCTWa7wCHr2U_QSguImSUpNvT9hRTUWTl5cnVh2MKkwJj2MN5sBZdkyJLpCrujQ9GnV9jfrL1MHjUqHQ-OB5OfxpwKifsJgGawDy8eShiGySJmX70DnLSFOj_ipWG0yxVm4VP_Ax8pOnXt_OTCDh_MR8NjAFpMTb33oCeoWQhk44oW7mo39WF1dR2xU51Z0w6CvEqTYPb6ZVMOICL53WOeiX5rWgwerIuVYaKbtf8JBwZ6-6xFbQ5jIY9ZF7vz7_-Ew817ZmMisGD9m_uZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا از باشگاه استقلال؛ علی تاجرنیا برای تمدید قرارداد محمدحسین اسلامی بمدت 3فصل‌دیگر با ایجنت او به توافق کامل رسیده و این بازیکن 25 ساله به زودی با حضور در باشگاه استقلال قراردادش رو رسما تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/23177" target="_blank">📅 14:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23176">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=f9uEN4CJ-3FzBaCAQOHHOOg9LbWUuy_v5oTRt-ytL2ID8kEQVtfdT32oZ8oxKvdEnNWVhqI2M8U_vh1UQ7RzQOP6FpBznJ7g2ysAhHI537WRRFeE-Nu4RRcdxWSG44CLTPQ_xL6_sAmaolUec_z-9SacNHTPNGAUbu9fCyV9MOqwjHIH0pP-qrbBgrApWu-nOF5AWf6s-cmQGDzO2XPFYtzR3R9S6lA4LgG_K3_mTpkvb2c-DWLRRQx-g087E9OBI7xjHmDRNKa5YK-8I9IB-qqPeSwIF9GNG44tOfVxg90sFRghBB27K3cpDV1bI4odBAvhbZnm-WlO0qa7Ud26RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=f9uEN4CJ-3FzBaCAQOHHOOg9LbWUuy_v5oTRt-ytL2ID8kEQVtfdT32oZ8oxKvdEnNWVhqI2M8U_vh1UQ7RzQOP6FpBznJ7g2ysAhHI537WRRFeE-Nu4RRcdxWSG44CLTPQ_xL6_sAmaolUec_z-9SacNHTPNGAUbu9fCyV9MOqwjHIH0pP-qrbBgrApWu-nOF5AWf6s-cmQGDzO2XPFYtzR3R9S6lA4LgG_K3_mTpkvb2c-DWLRRQx-g087E9OBI7xjHmDRNKa5YK-8I9IB-qqPeSwIF9GNG44tOfVxg90sFRghBB27K3cpDV1bI4odBAvhbZnm-WlO0qa7Ud26RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 تااز بهترین‌پاس‌‌گل‌های دیدنی در تاریخ رقابت های باشگاهی؛ کدومشون رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23176" target="_blank">📅 13:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23175">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T893ID1fPActj8WnOa1wxe6qN0nvKwHNpzUznIpflx4X6SOyXF3CHKoHcnKlPDKQo133mTHYxPpzg7_r_3k6n5mAMpOnV9ox7CRY_oMN9hhctu7p1eLr-FZnTw4onMpHQnKYgnJKkUvB_KheZDag2ZXp1M1fEfM2GROwQ2iuOTy7v7dDbvHk03ySh0PTA7tEB9qiMga8taTwAppSRO3OY7C2cNATR9eSOTcHJDkNqV-S_E4X-xUtNThpquGrnbet2aGk0zU8f12A7DyS5O5oTLQCE_bpnFiEw-4WfCgY0ghiUHhWE2hYLwN9nOG7bmG-lB7Dh8LxjbUr-BVwFkFc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
🔴
#اختصاصی_پرشیانا #فوری؛برای اولین بار اعلام میکنیم که اگه شرایط کشور برای فصل بعد مساعد شود نظمی گریپشی فوق‌ستاره‌البانبایی روبین کازان به لیگ‌برتر خواهد امد. هر سه باشگاه استقلال، پرسپولیس و تراکتور بدنبال‌جذب این بازیکن هستند. باایجنت ایرانی نزدیک به…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23175" target="_blank">📅 12:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23174">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFxPi3Nv9tbs1NzXuhBPdXGEWjx75XKBFGB70TLuCQ-GxGRkwMkeBghuItEpKMAlT1F4Z6oO-09LzhIzXlTtC8bjKYxj-0IKPo94hOS-7lVb5yNGnXnLKjcbRHdzKoWCextpCheeT-nMC5eIMJNlOVbigGW02yKaWIZ7cA-qNg-DRaMKkzaC_bwZfj48FbmxRUfbK5sUuevp7wFcQ8fZXutZhJ_iDeisYHXJFzwv6dGc_xTIcImykGjeD_ydPEbR1Z8GWm5xebhDeX41FXnsTF5cCX2ns_U7DNnoNc7KNnmP4ci2dVSxlfgzr-TSB0E87gpSHABgMH6d-FHIHND85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23174" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd68pBAsP3pzs13YAEEP75IlH2l4ofV4BCupzEtelR7wf5Nt6eTNQ8EtN9vWdeyiKCiFxJb0iA2Wbm-0P2CRImoqISuqhn5GItT0TsS4VArc82x7ONinekWLG1zkcgyvtYirFfI-SKFanHr-Qqmvbq-QvHXi0TbGtDS8D_SdIN8FmkkAnmPks1_rU5KhFqMmgLz-bdIbb_PAkLsQf-bFduggssdYQdGTgNxaiMVvz88YKSXQJFdJJjNytJvcnYTdpSvCqRQOUhYrwk_LnHA1dJ8kAyZwco_EO-ZkWZharV4UIFq2siLk8djOpZ9t7te6lEpe--vRxwePp6ZMgDE-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده شش ستاره فوتبال اروپا در فصلی که گذشت؛ جای ستاره‌گرجی در WC خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23173" target="_blank">📅 12:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=CFBxAuWWjGTCFcr4AOqRPWlFCRRPI22b-gTfzUd5a3sw1bqc14UgHCjH7rXZMLTl4iiAI004dn30oN06Z9IEwmSNcBD3Yf-eRtKwn_vsiMvic_Ptv_Xk8ThYZ8qbKw9m9RZIfoN1PK7J5TDCMWbGoBN7VsoygjLH4S5SL4OJG_cjy3hTkFBlS_B-SmHOq293WIUAkXbcj1JaUoBeo3CqYUMxJsUjIjLpUBtKLCFNzxQCqlq_kSdjAXy7uq-TD1S3PqAcwhIXzijYABUetd7NOCquFeW5Aq2BcoyZmeJjMb3cC7oo6CthQCVcOOs0AmxLpAHu_MYOF_O-XlHYUnEm5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=CFBxAuWWjGTCFcr4AOqRPWlFCRRPI22b-gTfzUd5a3sw1bqc14UgHCjH7rXZMLTl4iiAI004dn30oN06Z9IEwmSNcBD3Yf-eRtKwn_vsiMvic_Ptv_Xk8ThYZ8qbKw9m9RZIfoN1PK7J5TDCMWbGoBN7VsoygjLH4S5SL4OJG_cjy3hTkFBlS_B-SmHOq293WIUAkXbcj1JaUoBeo3CqYUMxJsUjIjLpUBtKLCFNzxQCqlq_kSdjAXy7uq-TD1S3PqAcwhIXzijYABUetd7NOCquFeW5Aq2BcoyZmeJjMb3cC7oo6CthQCVcOOs0AmxLpAHu_MYOF_O-XlHYUnEm5Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ نوستالژی‌وخاطره‌انگیز از اوج هماهنگی فوق العاده لیونل مسی و اندرس اینیستا در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23172" target="_blank">📅 11:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3wR1HaYjw2tdmJxtio1CYmcp6g9EZvwRSwPG25JeTnsDjMoLoMPcnVBg1eBAgtNTU5VX34C6Nfqi3mav4fZa64ihP_lkuW_hFpP4thFpgbGtxvuw8LDZ-QIIZ6IFlxRuHFI9ALwab7nuWtQZjU4GFIVNaeB3R9u2Pojzw58ISI4_YnAe3GfjJyorjgue4BN5WL_WMiCgngSpi_APVbs1piWJ4kQujUpziMVB8SewEyHKg6wg5l7n_4EB19JxIGCgfLUetakRQpuPwfq-IaRc73TeTBM2PgVuR7G-yD6XeUZm0qZu7J_vAMtLLTQpBrjItAGEfT14zHq_715etgDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23171" target="_blank">📅 11:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23169">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwZZgTN8KtLfZvNfwpYfh709f9-0XtxDf0S1s5Ma2yxwi9y2AoKjSi2XUZDyv0upAC0wXjNSFQfKqo_3uaLAD29JfAybyn_PnFYj0OwicrBZ1WQQv2w2jnKuprL6VZCGqhUx9XG5-xbjaiE_HDSKUnve7VstgxnzxJeP91p2m7DMKAeRPgkHXcOkMB9Vt6rHlK7j9g9TW094R76yMDlCFhGXHx8VJugXAqVogMVvMUj0tqpE95V4lFp_TyvQEivMf1CtWwUZibbQSW3Q6sC30Z7zkYf0WdP5kbN74xdHM_R2e4aqo6G3mHKGleuGmWMIB3bIYeyxBA4KnsnSujbAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZCCXE7u7K6ey3-SpetuBxfkLCp0DhM62NlYIs1LH3Tj2RPddRTqtkg2MieygBc_P4Nbmn7SxR-z64WF0qcv8Ah01dAqO6gI-ozZVfxZq8YkKejfVxo0M_wBG1t6spOV1nTmjLKxEiHJw_XZq8sX-fgUgFLTNbOXJmdo7gkplsCwoEh_BmHj4MtdlXboXJWWAp1JqdKIFadGOZwfHp4oPtZW14iW70Rnq95peqIFF-JHQhQMmai24IW_UBOkwwi4L5OesAfaPRiWrsHgmXX-ue4-_oPAnD55aUCDXf1X5hoMzq2vUPb_bT5h4IWYs68uekHYZd0SM5bdgPbU5lRe8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک تموم بازی‌هارو سعی میکنیم پیدا کنیم بزاریم. اپ آپارات اسپرت هم که چندروزپیش تو کانال گذاشتیم دانلود کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23169" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23168">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RURlI03MOKNnZNhB2MJVYRxVNMi4JIB75csk2mGUgnG74ECVP_fvoHoTvf734nLuiYnbbdUHuc8V5oN_bPj2vIAWiTyUhR6sxGGEGC7v2HLAgfz8CTervxFMV02rRcSEAAHupdpZwiLqiQs4lE7MvyPXLcbu13ijEvkArFbo0W4oSqDy7Nksz7jHz-bnr2m2uNxu9F4lLvXL3rbYAoi4_LAuoccIj5gRoMJqhXuFZmip65UFnDo_9cTE9bN_KMmqgqzjR0jlmDFUQzBh_ESsuv3ERYa9q6Iiesm6ICIQ3oDgHCoHwDtd1O2IuqnUacvvTI39thpskVEM2A5UUvXjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛شهریار مغانلو مهاجم‌ملی‌پوش‌باشگاه اتحاد کلبا نیز از دو باشگاه تراکتور تبریز و پرسپولیس آفر هایی دریافت‌کرده و درپایان رقابت های جام جهانی پاسخ نهایی خود را به پیشنهادات خود خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23168" target="_blank">📅 10:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23167">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=CgjuC5MquAwtW9HG4YjPi1jLp2BJzKn7JEpLtTiDGvUMKaQWPnmwm9fasjCFGtl_Gg0neCMPF5mNT1au0WSPb1afhEnHPo9UaUDEka-UtIF1wGsCcfJOcAFZwM8J_bJ8l3Ce1BOI5iIRKjKB3OjYQu26I6GueeFib1ZoCU-g9kbkVlnRUtRvzm-jY7gW94gFckBjkp0kcqI0nWLkbEFin1JjMJmqEWkdiLndt4EpzaVQNJcFoJ7tiAgRYXUdUk8oXaPgg2vBlBMe3aUaeIoJ9GEBFvTJZ9Uy6hC_qwN3gRcKmNPKoNNTbkt_eKHNdS338e9_Jp1pgPVnQiJJFRGsZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=CgjuC5MquAwtW9HG4YjPi1jLp2BJzKn7JEpLtTiDGvUMKaQWPnmwm9fasjCFGtl_Gg0neCMPF5mNT1au0WSPb1afhEnHPo9UaUDEka-UtIF1wGsCcfJOcAFZwM8J_bJ8l3Ce1BOI5iIRKjKB3OjYQu26I6GueeFib1ZoCU-g9kbkVlnRUtRvzm-jY7gW94gFckBjkp0kcqI0nWLkbEFin1JjMJmqEWkdiLndt4EpzaVQNJcFoJ7tiAgRYXUdUk8oXaPgg2vBlBMe3aUaeIoJ9GEBFvTJZ9Uy6hC_qwN3gRcKmNPKoNNTbkt_eKHNdS338e9_Jp1pgPVnQiJJFRGsZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23167" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23166">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ru_S6O6q-4jMjk89_UEi57BvmYgqhekljeRNBZuieVm7HL1j8VGZeItTdtetwHUlxXNndSp8cvG_NdfR6KqUvoobypjaroCbjM4wmcxIdip4DSg0TE_jkiVT1Aicqjz0PW0QHlIHpT9ykdevV-0RAFFRCeA049N8cyWKVowIRgi-n4c3nVKbABsO2wpDS_4eDavC1jdpaLPgPVi9LQldgFmQXx-4MwLTJ-OaI5BW15yNSZ6Ooz56DCgMGgZxoZZxQyZZMBM6KrDgiwknYM-72o5Cx-ags5tu8c5jWSWWXIWkqMOWP7PDprJiwqj8j4IrPyAoh7kVjdW91Ef5cJl7mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23166" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23165">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEpPUhgaSQ41PFfIG3GcarmlJb4pRjJSErEo8vC5P6SKaZFs4Fe5O3HpEcY3RFZ2FxxcjcDzabDAgAPAixcc8hCs3rkqXBT8DyaQYfe0rFkhhnpODs2zo9DJsa4caScut0y1xo0YbGFSTXNVYVKyr3EItOgrINS_uAngCa6ULQD28-HU4FnI1qpDMAGGcPFk1e5uWhUBnPO6Dy-ZpH4S3V_u4eCMaoyQXe5xn5ZpbJbpyeHhwxjuy_z1suNoIMTq7oDSiO7TLBOXyOc-s0y2ycA5nI2ortcCPcZAtmH76z7lM9Qa1uYn0gOuoj5F5GWeh9T2cm0S0AWMDQTD5vrMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er21
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23165" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23164">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e065f47574.mp4?token=VnodEqh5epSeFjC1AG2-ABKE-kaQO9VbLk70EtzW6cWRzTj1NeZ_6Nuwtd_Cjc85cB06kcbzV94OUA-FKgspq-DUBbUNDX6Z0IrOfd0BYr4fC7yh3PG5NDEkjGGMXYGtB9SePjBSyHGCmqdjdO3Y_Kg4qWgtMZO7l6ataJSOZcLLS2hlttk7U8EUYW26O-jJtKs33PjvI1D567D3ujwTwgzqQrR8_b5teqyx5Nh1w7iVCj8ATYKb06Dua9oqYo0EIe6D0tGBGg0AGlHPy8IloyMBjgNKL8CJ3vjgk-1OJ3Mb7xpecStAjK23t1XPzkxi5XeKXxTlmxDUmAZtNjRauZjUhxHK8UVoJtD7q-_5M7zUXzS5gTvjtsal8xBFuvzvGJcB_dxpXmrAMVCY0Ma3PWJT1Y00KfaiqV8CyDCGoiwoL2X4NS5YIryzHSxk9o6U_ydMnwHyYH9F7goIeU4uGBpdRifm2fRFmgjs4lrjFixxl_MEBrndpYaN9y56hP5EocVRh-YIICGvmXcN-FG96ihRoKi3sJ6a_uZQTcBHCcpTSi01SHHvrNWBJOEGvnbrfuB6SkQqwopeQuoJO2l53vrzZPmHo6w4Fn1WmWelO6YRbJgZY6VpzSLAG9q0sTUr66hPTJlTb0XIiP4rM8zsjrUlxmBomUC5OflcFYpVUV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e065f47574.mp4?token=VnodEqh5epSeFjC1AG2-ABKE-kaQO9VbLk70EtzW6cWRzTj1NeZ_6Nuwtd_Cjc85cB06kcbzV94OUA-FKgspq-DUBbUNDX6Z0IrOfd0BYr4fC7yh3PG5NDEkjGGMXYGtB9SePjBSyHGCmqdjdO3Y_Kg4qWgtMZO7l6ataJSOZcLLS2hlttk7U8EUYW26O-jJtKs33PjvI1D567D3ujwTwgzqQrR8_b5teqyx5Nh1w7iVCj8ATYKb06Dua9oqYo0EIe6D0tGBGg0AGlHPy8IloyMBjgNKL8CJ3vjgk-1OJ3Mb7xpecStAjK23t1XPzkxi5XeKXxTlmxDUmAZtNjRauZjUhxHK8UVoJtD7q-_5M7zUXzS5gTvjtsal8xBFuvzvGJcB_dxpXmrAMVCY0Ma3PWJT1Y00KfaiqV8CyDCGoiwoL2X4NS5YIryzHSxk9o6U_ydMnwHyYH9F7goIeU4uGBpdRifm2fRFmgjs4lrjFixxl_MEBrndpYaN9y56hP5EocVRh-YIICGvmXcN-FG96ihRoKi3sJ6a_uZQTcBHCcpTSi01SHHvrNWBJOEGvnbrfuB6SkQqwopeQuoJO2l53vrzZPmHo6w4Fn1WmWelO6YRbJgZY6VpzSLAG9q0sTUr66hPTJlTb0XIiP4rM8zsjrUlxmBomUC5OflcFYpVUV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجموعه‌ای از بهترین آهنگ‌های ادوار جام‌ جهانی از سال 1998 تا 2022؛ کدومشو دوست داشتید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23164" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23163">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJEiBj2yF-RejoDEih52D4SFwnjPdAFEx7qbXMmuPQaqU1uFSYS3BVC7JH2TwcrfzlMSU1dUVAY8ui2BfI6MgBEJoMbygkWtxqn4hc0rW0336IAbMv2AEwsgOsHIt8VKguyky4Q-EFxbsRadlq267j0VLUS6G-m2FeJkWpNrGqQfOIGh1xyWeoRbl1XTAcDnZHSOv6RPsIhK-QY9CxKj2D4YpWeZ7XCXlFBDJPNhcV5-YgOxi5cMfg4bq1-Dhzbbdho6x0dT48g20IUgilCLR9RRzIlXOzcPo3imEWjmHDGxeS82S-lUD2IPtA_gutOsJyG8_DBGg7WDFfvJHt5mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23163" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23162">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX_FykYT2c7ggN673H-mXYpF_Kq1kfWnA_9FmAkViWAJbhRP1r-ienkA3HZIyJtcYzqJhsq-_7KjMVRhQla2myLSDGwpDOASIAiNy7xDwi6OrKVhd91-qdUh2dnVGHvIAmp_s65PWYe19JJRXNmFU5FXFY3W6LFfBjz-9R-vHQVJVgeQHQFoS7m58xSfqXjS8xBCDyyGfefHw-TjoXnvWRw-3qAvJNnki3k_lRE3KysK0i9kbWV3iAoAMb5qAPe8B003VJlOLoAjGcTaGyqyoDb7bin1NCAPw-8oLYjKX5Se_3CZ6X0kqABmTy2GunjqX-_f1viodksDALEJXv2l6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/23162" target="_blank">📅 09:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23161">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=vACs3qcIvUPbDiWYJTVutHyx4YfqXa6e1TSW0AkAb8dlMa-TXjgxabE7T1XTxyNiJSuhe-QJ4wWiEMbjqyXu5EpRuHpXrLe-DfOshpKr7R4oPiSpBC5WIi-cJfYB6hPJrzDx9lIi2_apeoR0RspLJXlJf2QuZ63yhQqwiPEzBtGtMfUb57yyEHxrMX04_cUK6fi-JDAVNNmYrEcOqM8EtoWe6ZDO_sNssIIGDnJtGAWHR0D0G1qX9AtkHX7QnyhWHv6sAWMjHba_k5SoJjlA_yVi7GmSQT9pN86L7B1rz8a_yXaeSsZpOChpRiuZE3w4oF44OT5XdSd6HxSMk6Dqag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=vACs3qcIvUPbDiWYJTVutHyx4YfqXa6e1TSW0AkAb8dlMa-TXjgxabE7T1XTxyNiJSuhe-QJ4wWiEMbjqyXu5EpRuHpXrLe-DfOshpKr7R4oPiSpBC5WIi-cJfYB6hPJrzDx9lIi2_apeoR0RspLJXlJf2QuZ63yhQqwiPEzBtGtMfUb57yyEHxrMX04_cUK6fi-JDAVNNmYrEcOqM8EtoWe6ZDO_sNssIIGDnJtGAWHR0D0G1qX9AtkHX7QnyhWHv6sAWMjHba_k5SoJjlA_yVi7GmSQT9pN86L7B1rz8a_yXaeSsZpOChpRiuZE3w4oF44OT5XdSd6HxSMk6Dqag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇺🇾
جالبه بدونید
؛ مینا بونینو، مجری سرشناس آرژانتینی، تنهااز‌طریق‌چت‌اینستاگرام با فده والورده ستاره رئال مادرید در ارتباط بود و قصد صمیمی‌ تر شدن نداشت؛ اما شنیدن یک پیام صوتی از فده همه‌ چیز را تغییر داد و او در جا عاشق لحن والورده شد.
‼️
درادامه مینا دراقدامی‌جنون‌آمیز و ریسکی شغل موفقش درتلویزیون را رهاکرد و بایک بلیط یک‌طرفه راهی مادریدشد تابرای‌اولین بار او را از نزدیک ببیند؛ تصمیمی بزرگ که‌سرآغاز یکی از وفادارترین و پایدار ترین زوج‌های حال حاضر دنیای فوتبال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23161" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23160">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=vH9p062v5k_Yzroo7B7uB52Q7lFvfHpl1zqvPAUUzvhKVDhE1i2em6NIPlM3-vsF6aRxVCEJlSpxCxyLg5SKPeRIWDSX4MTs53PTPYIMMiXMIof9YLdn90Rb4WCsfkd1ohYM7X4p7X2VySHZgZpn4CPRIJRLSewlhUMK7aldexZsoXovhY2cX-IZjl_wpFgBM0kQoTSNQG9Ub_v1mKIqkTRcmD1T1QhmjAmjKeHVdfzvf_6Lt_psvaNtpQl_IehWSH6NNppEqGgHrvKCfV7HHElxBwDW_Zpzokl9fuYvwGPXUPV01cIc0Y6InR8Y0a7omQVtLVEBZpDUgLOxnh-TgqbxUIfe40jYNVp6fkiukQYFGWyr7ZNSLSyusDsP54lW4A_LMWFiOwsK6dX9U4LvrZ6ZjXCgOjugq18Z_f0cVd-FwlXRJVkGNtb1LhASLz3v0nGXknxMnY3rwcfXSs9cidk6DvW1NAbo5Lyqu5qVOFTh85ZtcxCj3KOeTE5BmYKlBn7ESVI0giwlJNWU3LjAEJndI_9V9M8JTEbzcorrfTIObngdlilLhYzzLVlymbGatT_5eMFj5uWUiXef_VBfYmeXAmJBb0P5GEaeTMxP5ZYHrLLL4eQdpae_x1VQKfJRrOV5W9cwWV6Fapaq99ND73i1HR6qXylqd9nngsoFXX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=vH9p062v5k_Yzroo7B7uB52Q7lFvfHpl1zqvPAUUzvhKVDhE1i2em6NIPlM3-vsF6aRxVCEJlSpxCxyLg5SKPeRIWDSX4MTs53PTPYIMMiXMIof9YLdn90Rb4WCsfkd1ohYM7X4p7X2VySHZgZpn4CPRIJRLSewlhUMK7aldexZsoXovhY2cX-IZjl_wpFgBM0kQoTSNQG9Ub_v1mKIqkTRcmD1T1QhmjAmjKeHVdfzvf_6Lt_psvaNtpQl_IehWSH6NNppEqGgHrvKCfV7HHElxBwDW_Zpzokl9fuYvwGPXUPV01cIc0Y6InR8Y0a7omQVtLVEBZpDUgLOxnh-TgqbxUIfe40jYNVp6fkiukQYFGWyr7ZNSLSyusDsP54lW4A_LMWFiOwsK6dX9U4LvrZ6ZjXCgOjugq18Z_f0cVd-FwlXRJVkGNtb1LhASLz3v0nGXknxMnY3rwcfXSs9cidk6DvW1NAbo5Lyqu5qVOFTh85ZtcxCj3KOeTE5BmYKlBn7ESVI0giwlJNWU3LjAEJndI_9V9M8JTEbzcorrfTIObngdlilLhYzzLVlymbGatT_5eMFj5uWUiXef_VBfYmeXAmJBb0P5GEaeTMxP5ZYHrLLL4eQdpae_x1VQKfJRrOV5W9cwWV6Fapaq99ND73i1HR6qXylqd9nngsoFXX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاگردان‌جوان‌روبرتوپیاتزا درحالیکه ست اول رو مقابل تیم پرقدرت‌برزیل فوق العاده شروع کردند اما درنهایت 25 بر 21 این ست رو واگذار کردند. پیاتزا درتیم امسال پوست اندازی بسیار زیادی انجام داده و بازیکنان جوان زیادی رو به تیمش اورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23160" target="_blank">📅 07:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23159">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=BANYjtVDurvCfGScO0lp4nqJ7skrD2CoFK2Q9MKWBQOk12L_mMqVlivEpD62GWBopNuQdsYQMawle4oLSzo1u8sJ1bYkMFUZXN0PTZowifDh8X6DQM9iZBfzQU-aoW0PH8ZIdCDVyQf-nOfzXAp1t-bfpiRij8BdfU2Lfjh8EOQDK9txMAtF5Ptqe6yH0C8cBHsCdL5rO0waesoB7NFnVZNoeJ0lUWFq7LZ6_SQVMWGmVaN0bjHathHcnYelVvvaZ5u5r8B6mStDtmh7I5Tyrya-7DG_JEzEUYDpP5Ik-tT2h5upFUdmRMNSeTSDb1uT73F8ZyJfbyY2Vci45M6V0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=BANYjtVDurvCfGScO0lp4nqJ7skrD2CoFK2Q9MKWBQOk12L_mMqVlivEpD62GWBopNuQdsYQMawle4oLSzo1u8sJ1bYkMFUZXN0PTZowifDh8X6DQM9iZBfzQU-aoW0PH8ZIdCDVyQf-nOfzXAp1t-bfpiRij8BdfU2Lfjh8EOQDK9txMAtF5Ptqe6yH0C8cBHsCdL5rO0waesoB7NFnVZNoeJ0lUWFq7LZ6_SQVMWGmVaN0bjHathHcnYelVvvaZ5u5r8B6mStDtmh7I5Tyrya-7DG_JEzEUYDpP5Ik-tT2h5upFUdmRMNSeTSDb1uT73F8ZyJfbyY2Vci45M6V0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏐
برنامه کامل مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23159" target="_blank">📅 03:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23157">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6E0MosCULtM2pj5yfvF21fl8EVxG1qBqwtdbgtDx7ufBr0UTkXxCG4HAC0YkCCy1UW0IpdIcyWFwVSwu0QGoI-3xQ8cuxwyYFGPj4byZFydxk4391Oyp_Lqq1xljVmY8KbcQ22A47nf_BpwkAlaBN_FTLBerietCvaHhb14WTwiYHzcx3TYhMADu3rY7ncWeSswuyrpCWQVzLzHqTSfYyBW1Ls-xn-Mj-ynVLyb2OtxBrwj2t7K9Rfv7cM_Tn4honMr2E-ipPNjRFldvceJI0uPJW0wgPAvtlAwThgBI5qVbNbVElANkbRhjKyNccl7XVUvFNumyqFzQME4v34WlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23157" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23156">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmxamZC8dngOPC5KovQmyto8Z36csxtTzeBMKT75-9NzuEmH_3DxxFXDhebXED5SnJFl1qUQwDl1mjci4OK1sTmwqwKU31LLzQLRYdLH2U5BFAHCq2D-6Yuiz_lIKz5CPh9Xk3fHi4voH7LooAv6wY81uhgyuBnWrNZA0paZMDOE4bIIVkBLQHf47MioHPA0RQMg9h3nqtpQAQrXz2Odq5ZYMlimWcsVWc0rzSBmPPMsAiAXtGkU597EWHXjm_ITuQjPGCYX2jOZ2MEdF_YWWWs-ElwnNEN12CvnqdT0QD-jeOkLcZY9QnL4bqJbHjr_osK_Z1_7CfO7QnqltOWeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
برتری‌آرژانتین‌وپرتغال برابر ایسلند و نیجریه‌پیش‌ازشروع‌جام‌؛ انگلیس هم تاپایان نیمه اول با تک گل رایس از کاستاریکا پیش افتاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23156" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23155">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyrhDk8NwdShgmMf8tpzB2qmW75yVo6a4D9pEY4xNNXIkNYzVzlyfabsQNH0CS7OgQGmmBY_V_3jDlL5PjOWC1xDuEIRF6K3O55dq_amXblEvLd_rRZllVqNYXUJVTRgdedXviYPuKIoHcJW3oLNQc0Y1oQp3C46QjXNX2IpurX3Blg6UWMERUgpbKypowbNRQto8jNgYT8vwA6mqitx2Ach7TXURVirW-o0IX0vdW50pFzOIN4UkkRmcV8cc-9TatLUnNl4K0lJd0M5KDGlATjbNONwwwX45u1H6cf6mxDIhtze42_5W77gEz1sRJ96-bgBKxPoqKxl0sHHmfkGeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
— سنتکام آغاز حملات علیه ایران را که از ۲۰ دقیقه پیش آغاز شده است، اعلام کرد.</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23155" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23154">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">▶️
هایلایتی‌ جدید و کامل از عملکرد نظمی‌ گریپشی فوق ستاره تیم‌ملی آلبانی که مدنظر سه باشگاه بزرگ پرسپولیس، استقلال و تراکتور قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23154" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23153">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrvjZ66boz306jMvRPQ2UJTkgNoqa5uYFk-ezVw8HUe7GzCrOORNB7mA1_JEqIsVN1qe56_Vm-x2TmBw3EiUiKAhaszgPzr3PHsjquW-nvmGRffyhaPlW4YLutCt9ImDSGWLV9WMWxX-oC6dchHkhO8aV4FQQYAKga4dLaf0vnAolaBXbC_1bLvwh17DtviU4wggvCGoOPyhDDZmg_1u8paXcLe_C2PsGhXaIaOKg0U884qdiPR02SLdgD3KIxWOWSEl31uOkVZV0dj8XpK-f0WfSKYuCDCEAWbbpXXPROsIjzyPQ_MIWAXAphgRWqVbXlGdmto_O6IbGkppHo7aRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23153" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23152">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=lcSQ8U0R1bPEp9f2N6r--AG9dKKJRd3vGgT7BKZIl4_FSj44R1NdrkSNn_0mNZQI1MAtrsOuEHk4PpmyD6sdyjxnCmNzDRvLLcPyBd-scXJFPvj6_lNp431pCm7HqFeRgYClIdBweYtZfGRgdvPNICXoqmG9vk6wK5pMsFW-zdSj7fMQpqA_CfGUGXR6Ypv_eIWVuT6frk4vfFLFkHf17KqvO07IXQFjYZNAci3EMZuoguDrzmZTdaWQtrHQxG0b9Xydi05u1YhtDDuwepKUjyhWHlQmP8u1MXyVlfWEnhYmN1bBvQ1nmnLWHlzjrlpmvoLxFPEi0fDYU7Dwsa8Viw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=lcSQ8U0R1bPEp9f2N6r--AG9dKKJRd3vGgT7BKZIl4_FSj44R1NdrkSNn_0mNZQI1MAtrsOuEHk4PpmyD6sdyjxnCmNzDRvLLcPyBd-scXJFPvj6_lNp431pCm7HqFeRgYClIdBweYtZfGRgdvPNICXoqmG9vk6wK5pMsFW-zdSj7fMQpqA_CfGUGXR6Ypv_eIWVuT6frk4vfFLFkHf17KqvO07IXQFjYZNAci3EMZuoguDrzmZTdaWQtrHQxG0b9Xydi05u1YhtDDuwepKUjyhWHlQmP8u1MXyVlfWEnhYmN1bBvQ1nmnLWHlzjrlpmvoLxFPEi0fDYU7Dwsa8Viw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23152" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23150">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdrkxr3Rh624Qwzu6AZOe1w0lF_9ZeHwdY399_FnH6NEQqRZsXqtkPIEOAyhwkbJzJceJQi8x3Vf59ipCcJZEKBEBx8UuYikY-w3PFaz58i1CY3seEAyI_WNI637gK6W-PAqostvRF7yAMO8YbPEzUWnUBlJuwGZz0DtLG_OG1exsil4q4SjiALae1g7NQFAx1cqaUGxwK2o1rn_HoYDbRF9sWCE3gEGghuRsyLAgziL5H3wARtiHlPLQR-H91w_Jt_YZAP-PYokN4RCVf7nCuNZg2xCa9uGARNBlzd0ui2FsPoRGdIxr06mZTC90irVL0nhcnF_SPBbQ--DAJ3-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23150" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23148">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2WmhyzDH_-TMOdJo4fiR_V2HO30fgkC4UaO-sBCRgjJ7-VNGwDZ87S2odauhUjzXDlQrCVk91Qvzol6GCCwm9Gq9TWlqcJMJ2qOH3htucHOins1BmdPTjRl17JM2YtiDw0gc66m-mDdLqOMR66lKRoQuAH-YI5bE_X7CdTE48TBmHQdCPxTH0do73eZAVQgm8SnDdWC1dA2PDat_daCYSFjW36BFDBVCyUzKJxvlqY9tMC2m2W2fnb7E5U15guUc0Rd1I6a8N1tbQEdxx_Rfmjiz1IRCqNhoUWhBM-iSmGVFXMqdSV6sUykQnmkSpG5VJjNlSbAolU8s4JEB8Rusg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23148" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23147">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=diKkPm8eco--qKnpb3KN-S7EISAch6d_k4pHBwEcSqsKjBZc3-Rua05CaVjnJYZCEewvB75on1rOt4iayiQnED-Ty3Im7Z3vtsM-4jCu2I921YDEAG1sHs28u3aak_ZXLfbyyauHKpbcRbiYiHJfE8-ztcb7Oq4Y-amlkKoRLxyTxqSbtS6WcrJKN9oafaG2c-Muuz0Sp3iXY2mbK-0LZi6pqYt0B7_VuQBDBE2EtX72s5bbfjLzMZZv6J_3uwiqQcLpYuqubHwKNYSsokba0vsmj4JbCMkJlUPH1u0TAWEm-hRT6Xvg_jQ8euPHhiWy1VWyTN32lM-GvGAhnwZMwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=diKkPm8eco--qKnpb3KN-S7EISAch6d_k4pHBwEcSqsKjBZc3-Rua05CaVjnJYZCEewvB75on1rOt4iayiQnED-Ty3Im7Z3vtsM-4jCu2I921YDEAG1sHs28u3aak_ZXLfbyyauHKpbcRbiYiHJfE8-ztcb7Oq4Y-amlkKoRLxyTxqSbtS6WcrJKN9oafaG2c-Muuz0Sp3iXY2mbK-0LZi6pqYt0B7_VuQBDBE2EtX72s5bbfjLzMZZv6J_3uwiqQcLpYuqubHwKNYSsokba0vsmj4JbCMkJlUPH1u0TAWEm-hRT6Xvg_jQ8euPHhiWy1VWyTN32lM-GvGAhnwZMwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
از پیت‌هگست وزیرجنگ‌آمریکا:
سنتکام امشب درگیره چون پرزیدنت ترامپ گفت ما امشب ایران را بسختی خواهیم زد و این کار را می‌کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23147" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23146">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzI_egD_bAMPB1PvZY57qeNYVooqgjal1BiNBUxaY_BSRBO9nxQwWTrZ-5gagGx4c1h9GZxHc8KVemsDeIuzXxBkUnR0F_kcjQ0zJBsk8gG7HGjJGy_pOXxuyW8i1zVQx8qJJbXTVlNHiw_OsEHaIS3KuWAuztNRcTTOOAqBE3curzcaELWLZB9QxDLs0gMD_zV6cYVYVnt9f2Z7ZsfjAncbGSm4r9kbTf4X7Z7luE1YBWRv_Y1V_QgmDx9dsLB_0d96kRUT04Uv4kzRomMTT6Xk8TvzwbI9IMEIdBNgYu-kitARgmoB1h3svmTwj6pCXOYHRSBkYorzCmXYB1YeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23146" target="_blank">📅 00:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23145">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCk-M7DPRPaXbjObyOyr1nmmmxghsJkQaXNTG6_cg77P69ePDo6OwHc5NGs6ce4eMXIYS2w9q5Nr21JZ3dtIi4S8SDRfHuo-qhd76JjKxEk8lj8iUbIfncj2it5zIcimW6zTawwnvdoV2_AXSB2DjvvLF9743anEf8R_pRjrKSxaZbPHz65ULlNLh4OKdDFxxCNz8M913_GOJI0ne72eX3HUoxe43MAt_Ezn1WePM0PjxOTk8zOcRWP7Minz43MIbJI15lsKgst5iEjzxDKpvJN1QWC3NNCMUTjdicYmm90eF8kC57Kc0-UwITmY_ESBXRupULVyLQvXgpOH4W7yGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23145" target="_blank">📅 23:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQyt-ztGDu39QprR24ni8i4TqToz6ddwBUfRyN638KW-fJ7nHkQa2bIG5WPKh0Gi4XFrD5ye-r3ngPWdjYaFh0BAialqu-vldF1VB8LiyDmd-QPC6-rQzUyShBqfi9I6J2MDsF3fB8iXvSmCBMEdccImWiXQCMX6PKmThAGCYfZ5_3mOX2jTmz8pC2TVxNdE8B5jTAOGvRsV3TzLp5deySHq_XdOY4O3g9fJB-OMxC-Iozm7_W3tuB8wb6GNFB9Xo7BFv06uJpRtPkl0Z0WfBBX2Ao83xPDA5l9q6R1IXQx78J5kFMhFl4EsGDSZiLTTmRpVlsc5ZtAhXVwJxMzXwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23144" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23143">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyMAt6RCd881GghUFPGSLlxqajVUxazzdrokbvKK1hjXdjKQGR-BVNqQUYqZEvBXZFBf1ACl8LJcQNxg4dUwH2l7zzIurbmWjIFXHebRWc3ef9N7RgK9THAvMk3xW7WOnrKIyKZXziQF_2aD_5P066c2P32RFksSk_5qdMeAOun2ue8Avo5wv1dGbSmNM6mAKboQuBZ4JaSDeMRRQ7w6sf3U9L9Zhlz0MsG69p4VzYmC767QSJgUcstI66if0vEax9ZHbmJeM1Wd91fHAvdQsNYeXeOMUUzbJZloxbA8KPYQheACpNIANpv98TPUWbwKTtMefAkfz9fTJvTXU5NykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23143" target="_blank">📅 23:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23142">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHAyjmU_FUcP1SXDYQABKr8wjh9Q4IG5wtytkUwAL7h_h_OJpodZOpdsoGmKI_DIYQkPbLEz0T0geRllvmfNAOUEgaPwtn6SpufNZAweFFptVkUjb7xNdqd7t0n_rOkHG1dR2HD3_p4aXW7H_jxIWNmHV_Xz4YGxkj3iij31j06d_3_ajYuoB40-eTzQOVCWRz_Ta7zbFR7-ANe2uguFlCdTbBUhqpiRqrejry-Ttd4QnPQ1chZoL_xpHZDfHO6Y7iswj488JtB60picXDh0_sEgKzM3cZZ7ElsBhu1gLVpIwzaU6wy8e78yjnB5cgB5h4sKl7OF7v-3yzMjwAiRlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23142" target="_blank">📅 23:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23141">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLyjjuhwS0Au1mmb72DueErZuUANqVercQNTSgxHfDCJb5iSoT6RtBRuNEyDbqjmjHVN9TcFXT4VkAbKm1gZsoz_0tyOzMX3AVKormZXzvMGbzATnrsZ9SQEapAO5lwLxuVCFe8AHFOUieEBqNTEgIjbVNP-GNb48r_j3vipF2_iQwlmVmsKJ3D6slekAXfSyG-x9LFlNYtUomCv-fODqNDd0I42uQuhX_0nefr9jo_ExYTNRoGqVs-bMnUrRlT3dgm1-jLPqGY2BFLXzjjyySQNTpDkUyEL84wAHZbUV4KAOtusAjek--iyTRaqCQ15aASJA-2JOB312GpzcC_nsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ متاسفانه اموال و حساب‌های بانکی و خط موبایل وریا غفوری توقیف و مصادره گردید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23141" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23140">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=Hu0HK1LganYJEOH52s0GFy5frOeCXYOdy4XoXSeaNV36Q7ZegCmo1ongp9gXn6d0ssWY5qiwg4Y-CkVMbIS4dcc2TNMAyqPH2f8D_le8d4zoT3mxVWkojImp3RCL8ICrk1_N685Tzk601af22XBYeg4W1vFwSJPvgBNue87dB5VSPKos4jaQKP-ww4677L0kSfnMDnoaGxq3uCzKmUjy_B0RQbb3fv4OgkmWwt5IyRThgAmxkwfXBqnPrko7sSu3gslTy7s2PiARze7586t0iJoLa1JXtjAB4UPlNs47L1g9Cqis4d4eWE18pemH4XiVOaiPAEkyqXeSZoKpwIj40iH8WR0fPPW76HF-LMXsLzmJnsCvPSuu-SCOJsGVU7IpaA52axj1dLansl0A-PjJXi6nOg9tlARv3j03xcjcAxnyexeBrF6Jgg5wglUsGMHBabmdZo8ewEkeAVxQ4OXQQJectnE5MDPxhZDtzuue0f1aPemTfTgy0MtPGT3g1bbPglagITIb53zyEpONoR_aED9fkFmiAVPe-sjnEw82DM0AaYEAmDmYekIg5bJgJ_jI_g19LebxB8Fq5I9-q_bMQKSfxoeD6MKLsr9SHDrnp5heOadUG5POTaDIj8prPYZP7NskUAySdradWzBmPV34JYZDZ4eomBbEALlFyWPU0X8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=Hu0HK1LganYJEOH52s0GFy5frOeCXYOdy4XoXSeaNV36Q7ZegCmo1ongp9gXn6d0ssWY5qiwg4Y-CkVMbIS4dcc2TNMAyqPH2f8D_le8d4zoT3mxVWkojImp3RCL8ICrk1_N685Tzk601af22XBYeg4W1vFwSJPvgBNue87dB5VSPKos4jaQKP-ww4677L0kSfnMDnoaGxq3uCzKmUjy_B0RQbb3fv4OgkmWwt5IyRThgAmxkwfXBqnPrko7sSu3gslTy7s2PiARze7586t0iJoLa1JXtjAB4UPlNs47L1g9Cqis4d4eWE18pemH4XiVOaiPAEkyqXeSZoKpwIj40iH8WR0fPPW76HF-LMXsLzmJnsCvPSuu-SCOJsGVU7IpaA52axj1dLansl0A-PjJXi6nOg9tlARv3j03xcjcAxnyexeBrF6Jgg5wglUsGMHBabmdZo8ewEkeAVxQ4OXQQJectnE5MDPxhZDtzuue0f1aPemTfTgy0MtPGT3g1bbPglagITIb53zyEpONoR_aED9fkFmiAVPe-sjnEw82DM0AaYEAmDmYekIg5bJgJ_jI_g19LebxB8Fq5I9-q_bMQKSfxoeD6MKLsr9SHDrnp5heOadUG5POTaDIj8prPYZP7NskUAySdradWzBmPV34JYZDZ4eomBbEALlFyWPU0X8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23140" target="_blank">📅 22:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23139">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba85793af.mp4?token=nWf3dnn0tHNxfte_vrYyS5J571SqmaYSsAJNR8L2EvHEOmzHFu4-ZDWWXoX8F5a9UZDPrcES5Q9QYR-fljnSkqDLUEa1JXCRaFC1bYOyfl8f9mLkz2tp1RyUmHQNjixRrKSdFCRZO51v_-xUoyr2LY1eIERZ_NuS7FesrW5Lg_SEsgSPOV0SHlV5Nu3-2y_jX-VBySwJ649EecUT34n7yZnheD57ITPJ1w3Fh7nQNQ32_vVnK08QazPPObmlmfLUPNBkyx5rBRBjaWskx-Wn1KXtCgOIfLq_O1tG1dVZcql-zecNJnDUkFROW5KG21quYsf0s0j0OruAN2So2KZLvl85a8qv5wBSHJxMhLl7c-qZ5mI-OWWcAydPIt3uJsivZVhJYg5eOmr_wFF0rDPSweVPUn_10ZkttGNYrGNBLe_v4mfQhXexANsaYnIo4YuzJBPgSBqURQ-T9xZ14iAvb1WRZwzYRBunerjHY9kM1GKjH9edmZ0KUnluMax0jT8p3bmJgPwHP_V-CyKwkfBkosCbT-RPtcJ17fho6U1hEhnyKNcxR_fgtX8umNfpJYEDUQd4RmMCBwWSGcEE894TjZbzv7oMymlTzIldrbiohKmd2QUSXxYq5bzbM6790tFX_x-o6OFOqA0srHEhthBJX8xacmiMaTAlVz-0ApF-RtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba85793af.mp4?token=nWf3dnn0tHNxfte_vrYyS5J571SqmaYSsAJNR8L2EvHEOmzHFu4-ZDWWXoX8F5a9UZDPrcES5Q9QYR-fljnSkqDLUEa1JXCRaFC1bYOyfl8f9mLkz2tp1RyUmHQNjixRrKSdFCRZO51v_-xUoyr2LY1eIERZ_NuS7FesrW5Lg_SEsgSPOV0SHlV5Nu3-2y_jX-VBySwJ649EecUT34n7yZnheD57ITPJ1w3Fh7nQNQ32_vVnK08QazPPObmlmfLUPNBkyx5rBRBjaWskx-Wn1KXtCgOIfLq_O1tG1dVZcql-zecNJnDUkFROW5KG21quYsf0s0j0OruAN2So2KZLvl85a8qv5wBSHJxMhLl7c-qZ5mI-OWWcAydPIt3uJsivZVhJYg5eOmr_wFF0rDPSweVPUn_10ZkttGNYrGNBLe_v4mfQhXexANsaYnIo4YuzJBPgSBqURQ-T9xZ14iAvb1WRZwzYRBunerjHY9kM1GKjH9edmZ0KUnluMax0jT8p3bmJgPwHP_V-CyKwkfBkosCbT-RPtcJ17fho6U1hEhnyKNcxR_fgtX8umNfpJYEDUQd4RmMCBwWSGcEE894TjZbzv7oMymlTzIldrbiohKmd2QUSXxYq5bzbM6790tFX_x-o6OFOqA0srHEhthBJX8xacmiMaTAlVz-0ApF-RtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23139" target="_blank">📅 22:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23138">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4xz3wxTiAUVVTKG3elEiWzT3BthLBGsAxHhC87GXmgSVFnjtdHLge7_TicKw3LRqCIEmHkCY1zKcvXLa0_fws1dywXZTXyW05ijXnkxN9s7iP-pHHfBtGroUloxrWluvHiMZTQPEpN9ANcw3rlZ8jQLI_wYw2_NmhszT6WRBs75XmAsmQ9TUwt1a22xi-k7o0BBzb_AovIJ24XOnOm1e_6FTssN4QosTs-rmiMP-ajHrWBxuGYpYPQ__qBxWFaUhFtZ3fvc72D1Fjafx1MUh8skvWqqJO1WpgO7ZDnwULnCC6EBr5xGDwtj-nqU4gsilZXyCoGBmAfxnB4h4OlZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ دیگر مجری ویژه مسابقات جام جهانی شبکه TRT SPOR؛ از هرجانگاه‌میکنید بکنید فقط از صداوسیما باحضوراون‌دومجری عنتر نبینید. از شبکه های خارجی‌ببینید از هر نظر واقعا فوق العاده هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23138" target="_blank">📅 22:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23137">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTpb5P1_ku0aid587_NsrDt5OTQecOt1B1iRM5YsP7aXgxBlvueLAHN07mMObIcWeMzFKz3b5r7sREwJSQIN5i3NzPeOYAnKEcKhzH3a7VuBURiXrcCr3ZH-4X6YwrUNf3Kzqye_rDLbwzpYqedCyq0Y4lE9UEP5w2lL6u1k4FkCA8dwEIGaNnnhu4cLDf5pOb5v7OGKpdsHkI0J7U0D4NHijTL-2BginIET6ODeinJ0RAnXmPfk1SQRtTIybHsZMMxdje1ZV03qYIKM7EHfz63HPsr7BO8SCHN0Srd4-u5jlkxza8x6419WVqrSQYxeNSMtUUQ-nqMzOhpDcTb4HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23137" target="_blank">📅 21:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-ZpfOUkuR-B1iDNyYNi_lVVHyEPuVVkPo0FZw2YpdfbKnYTzW4HtrjUQyVKNctDmeLzIKP6TikF03tJNhsCkgbOFAyBrYlTEC1ZmIOVPC8rFEnuXvHIvXKU3c_Z6DpnSNvcJp6FDbQ8x9-bV3dZlapDBmmEw6tZfs7sAq-EkZO0-G9MB9NlvFCkzHod6_4nj2dmfnfSHe6XBHjVjvdaXzvhUvC4VNBUejOOJR02ueJGTC0LJj_81lj9Wa-m_sDTVFPCkWYny1_CvvCFCptOMDVw0jupq9wdZM5VVXah0mGX7bZLzrAsgTFUAWtV4Hy-U3pQquJ50j1M6nsRD0typA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌اشتباه درطراحی نیست؛
پرچم لهستان روی پیراهن هائیتی؛درسال ۱۸۰۲ ناپلئون سربازان لهستانی رابرای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه‌ استقلال این کشور جنگیدند. پس‌از استقلال هائیتی در ۱۸۰۴ ژان ژاک‌دسالین به لهستانی‌ها تابعیت اعطا کرد. اکنون و بیش‌از ۲۰۰ سال بعد هائیتی با قرار دادن پرچم‌لهستان‌روی‌پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23136" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CX3plO9TbcYplKuJ61fiIoyBFtdaKXPVU4R5xg4oz8phaK8huQiHjvSa_RvcRUPilWAeGNhCVZruYWhvgom7kaufLw8SfqfJ401RlfkDKGP-eqD-zDIB72hpWa6TvbkbBaebopXTOHIyjGweh2oRcTytS5dvnrlCNg68NVk_TDFX9GcEC2Ye11O7gaBvqgezGFSxa57oN2Vr98ZHhskjj2vHnYKOXq5gRppbbRPv-viUtuqoA81vdv4bXRCr1gAdzrsncb2cCR_sTCinPkP552K7ZGoUnllMjsb-p28g8rede3HpAxa6AEXdL8lBkjuFXMoNG5E6VNRR8G8yi3i1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23135" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syTRULR6GKKePTeNK_GqZdxaIsU3hnRnCUy42X5YG0J0YDRS-hHeLf4BGLLViG2rgD6_nAiGr6j7U_ceUtJR-w4-HO20YvcbqIJRVygrClKFhjU818u9qyVRaQw8y6vGVC9AHjD27wMh5-r-QaHCxamEr-L_1YDDOmKmDG1B9zGKU8jlzKAZU4kVl8kHP3gMUyxOtUe5bRdOP_L5J1odSv7xnb273r14enNNm4i9CW0Sno_Ap39hKKw2XuFjekaZ0KH8o_pdzBeWSJZWQdtzzpHZIa8BKc-J3c351_581MMC-ZwCqaTKGYys4QrU_w-yd2tncknrzQYCp-eWh2mbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23134" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnugAJu2vxw4wPwQUIWhfDCBjzhrV4cwoJ4cIE929IjV7kKM3WHmEadWYVYzgkmUt9Bz8g7pcZEKF9aqqXg9c3zY9mvcAlJVWhfHlhDEhLDavhyknL8WgheNEM8g6p7aIxGsXxneUKn62uyI95Mz16YfncjcxUi4Ug-62xD65HmbHKfrAjiA_F1SaOCogkQG5mAAjlaGPshhboeWCNtzaryNbjWnUs0dEtJxELTrNBp-BmKK9y79ylrOs92Io4qTgFGkR6uAzz5d53ZiHnHrmV0cVCmVWnwTzf-3j1SkadWX-TZJ46pwRRsvc-TLAAX899OMIKKfA5QmGCxj3ma7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23133" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/agusT9MF3pP27vVV3XRJVFDWdKHqfyL6fyzmk-NE0aqBj2x4M8CLxNiRtnXuqnNLjTysM6OuNxEAVuIxIZaLGPMiIi9b1LTQxgu4KOYk1yNiiiCdOeYVpfRFFeEBYbnMtbV8Ysx1VOEgH8lD8QTwimYQnrfqmuHn121p_fpNzLwW5uIeq2bZgNRHZ-4crwZuCE_ASpEPvl-1kTCJZL0bWscLxkQhC4ZKg1if6KZgRjG8J-EicOQhWkR2hPKaRUsoIgyCXnykwfJ3aM_vZxxDhPTocFk1jGeYurK4r7F_DjCASZwlX-v02t7jNgnlOJV7BtCvWAaVbVaMtCuhKIwTcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v72RDIA8HgJFFpQ7glKMmaO0cqYwEirXbNnSfuRuAr2vwIxWmS3RsBXjnf8cIlXYFCMBPNf63i3KQeN-rSSXivgFS7141XmLl1owp2tUJeHoRVGj1_4nPQKYhcI3Mg7X6_VgNDpHWop6_IvmrS7g_pYlsx_mSqMFUL0naZjPFHOkIudbCpBlalin8a5nb_pg9bX21b9wqZTvz-ZJQnt5kGR8xxzJ_zBukr-Ziz_fVYHg9vTVxvYsJRJVxGF1tStLJNtP7LtYQ-XV_ZD06TNSm7iQyLo8Y-oaIk6ZAKu9ClHHrvO3n_X2ij4eyOKtrfIU2eW-mCA1ROXPSou2t8IS_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرخوش: تولد و بقای پنج توله یوزپلنگ در پناهگاه میاندشت‌. ‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت خراسان شمالی، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23131" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=uEc7hBQ0_vrL9XSMsG_jmocRAaoQPpo4UJ-xXYRYq1Cy-KCr22PoDZNEwU6CyNpL5Nh-ZXWMir7QkzGCoFeF8O5SmTAc69q6L91lQosaIGlxQVYuwWUpGrXpEvi7gqqArhKqfo0BkczeJjGBObMpFQE1EuZ1YjU2RpR_NEOrgxNkUtV_37NdQLUY0SN9pP4XCoqf1I7EWphNJmtmWv_BLn6Y9vDgdlNRcAvu0c-D6_fo652sUtseyAe8ZgvDJtr4NKR5fdbAUa0XdHUZ6IluhqBxRsA9OvBobFnp7DYJkhRBo9DTDrRubT58IyskwhnponQEYFkCjC8dx4j-a3bxbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=uEc7hBQ0_vrL9XSMsG_jmocRAaoQPpo4UJ-xXYRYq1Cy-KCr22PoDZNEwU6CyNpL5Nh-ZXWMir7QkzGCoFeF8O5SmTAc69q6L91lQosaIGlxQVYuwWUpGrXpEvi7gqqArhKqfo0BkczeJjGBObMpFQE1EuZ1YjU2RpR_NEOrgxNkUtV_37NdQLUY0SN9pP4XCoqf1I7EWphNJmtmWv_BLn6Y9vDgdlNRcAvu0c-D6_fo652sUtseyAe8ZgvDJtr4NKR5fdbAUa0XdHUZ6IluhqBxRsA9OvBobFnp7DYJkhRBo9DTDrRubT58IyskwhnponQEYFkCjC8dx4j-a3bxbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇷
حس و حالی که از آهنگ‌های تیم قلعه‌نویی و بازیکنان منتبخش و تیم ملی آرژانتین میگیرم:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23130" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXNrmrmkHlgCvw_LnbFNx6jY-5TIBqBAU5Lf_BtDvdMykcbKOew6C7J3D3tItrHF4zX7DTabh_48qVyHHLyrGsnMR5RTNh-p8XWVNPxxOV6tOECQkQU6Tm3CfxJptptyA8OdHBSjifWQp5FPWgTapJkP-bnTAGOLnHsI-vLPH7aaec373KPsOb7OhM4-aarM5rOF3Br0My_zvogr4UUZgb6HUZ6_NZUPBK8yTMHpPA_dO8rScCwC6AMe5UZZIcVuaOMrl1-7-MTldkaHAJJg7ea07DuiRYga5PhmPc7cwX_W9VK7p7IVW3NQ8_XJVx1pJ8BoYtEOi2hHkfTC9j8_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23128" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23127">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1xHiXK3Di5bZjZtuEC-KNEjjSN_KXtLqugO2xuOOoMkW1DlhyR32UYBpu3EbSG3k3FhQXRhp9OgT5FowlxZE2NU65vcHAJCWk8d2xTcZFHZ9Uf3hOWnW3fbnCwraIsETOntYlY6xUKYv4bJ4FXpyFNDKmDuUnRoJn8M4CXyoFUVsyWU9Dx05I480Ej_zeqbWQmVrgx4arJIC_KUGTWAzOWYZIExD7TIR88qKp18XzmfiR48YWgIjqC9zOPpTIXGuv9uu_9I87DURJ7SI-SE2iTFuduRmV1vFCcVRX8bK3dfwB_GuUw3NyL777RVrwUSYMcV8HrRCIIThQzpu3gCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23127" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23126">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-o3yjueO3maIJVe278ArQArJuLEh6PnPpHN5g10ahPGuTT0hCT3VO8NVj48Zt4nSP1oYA7rOCHu1YhbumRHs8NnTq--vDXXc6ew3O85mFOT8hu6Zm4N6kgy_HqYprd2uIzGBsc_ctqmwhfa4h7_RpEgNC5hsY_WI_QmFucJJfObzM2t4xdpueGf1LGdiV1sVEdgBd_37qzCI7n0KG_xrvKsqSQHu090sKBlp0eFfL0-ECVxXUyItdcz7LBikH8Mik1vnbiuDUijtGhsVqUg-CqErSvbRRoTEvH2CwmmKhCE6I5JF9bOrOzKaImmChlmXlUHavOFvAsjvKag-vyBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23126" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boWcPFx-OMb2TnPF7z3SCoY_qBIx3j4NqimA8VcBR9ZeKsEhxL1HDSqEbQRBh6TAnACEY9s7x4GCae3ix4IbbocKQ0fiRGke44TsacLr-nYHZRCt3NL8H91ve66rKmcRXB-dFnE7B2PHE3VWbN2fU-oBO3IlEx6m9w_rrOLKUciAgpIJrNTuF4ODdB4feH4cQoh4POiIWIGCDP7W5Zbzh9g8nyMiMfFg2aD2QN1C7AkLDViKSk9FYxlIwpCqpk3ZtKYp2K4qMiHlkOHrAY2AjaLuhlET8lUOUcvM78GoexcEmDGfWbOowH49rF3hbe2r3JGMfom8VrWLksMVZ3p9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M2EyUlkryw1-G0kp_xc7fW11oTDHc4u7qg0o4zDfPKqgJ1JIKkTmbQsP14FViQKEq8bLGpTFHMwCehyBEq53WE15C9dsBVFVbWmnfwDaG8ffn-37xLL5fET5le_nBvrCmXhy5Qut8jrOBjkSZuIP2XSTZW8lbb4ewMWaObmFpAaGWmYxloCoyQ2GvdyPOe6LJpDVkQ3gQUIB4WRt2OLUbHrRrulqp4PETNSU6NwS5Vit4myiSfllxOwqRqKvLWOpw8jQQF09QDXjl4GWnpQ7raf9PzguufoW4HinUdKZZokfGgYAtqzKXDTBIlz-mAFc6X98tEGlfsJ9BIKg6F6t0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23124" target="_blank">📅 16:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbwQktl8Qrj_ciMeQ14fL-6_1x-PaZPwYab8bHbSZdS5VPym0r1cdHbvFQ-3CP5Y-ZLI2ioj-uUP1NCazABzHbgkSaIn_Br8JDIrhlec2dCEZN5i3vxDQNsSWuk_HNivYBRfeopy6VMISJ11aoQqrDj9bW_e9D-YjjsXeZeypM2_EaIoB4zmMKlzqhUUIyFT5D4tHHOA3NFvpq1oJHQe4wJUF5pkPT_0KXLkW3i_E1ZFIqWfYBaVo6YQpOr3cQCqcFXDw3mB742J3CjtTpBgIWd_bx6c71dyl31GOQ1zdepKY9mJpiNG_V5rDdqNLwX5oc3_ykKzq_X02EFHBJNCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23123" target="_blank">📅 16:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میراث‌ترسناک‌ضدحمله‌های منچستر که بعد از یه توپ‌گیری آغاز میشه بامربیگری کریک پس از سال‌ها که توسط سر الکس فرگوسن اجرا میشد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23122" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9maete-v4bcm77CuJFDPGzynFZKC_c-sSl13OllBJEdKWlSjtAvooBRryaSyFEddRyU6DfQmIOUw1ZozD5DoeWABuin9yWTcw3dH_ScLnA0BHb3kLTVwUWkszk_p7nWwBDzeSLGI1DwOcjdTY2fU7KZnqMfrIklz_fTy3dC7NTeCJ1jaBFqlQ8TFuKpHHRXFwhxHSg5jnEHtfQnUyxOglwVftCm2XBVmsKMrpIUe0d-5CbIq_9wOhEdZiJxrZcdPMya_R8LAVl73FxKcWxGttYQXd684a-0OROQBi538RrQjknvlClif0HHy6HBVOaLQEtWUPbedxESF_V9fAD62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KVnkeptMUpahgJ1LTWqEAfZq7EAnCseS-TfZq9rkGiRibTkH1213ZNauZht25WADOm3iMqee6JwdpuLysJKjccu_0Nw2tSW_X7narOOG9TLCk8QnEglZBAaoTaoGwk9UYWYbDR4PIgOeax-VPT8DrgJJ2Iu5nb-kmje-PUKTL6pOzYtlAD4GOcGWldSjkm6mIlVOow04FajFG2Enc2q9VcT_lsWNgmUIoySre-hWAngJNn_E0TIF3BiEG3-LW8xszYtQePOan7WCJ1hspbCWa387Q6vRBJ-yJLnGteDGtp-TVa7jdemjt497GmCVw69mF815l0uoGBpJfP1Rs3zjZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23120" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubvpqh6zsBAGnP9OnHnkZw-2JmwKhBmhSnJvv9FLFYJBo704-wqx-1b7rz4xfikL6dn-F2dTF0L5KiifU5giMjPrTGuv4gTPmpqqc14V_XO_RQxKuuXi3A9qykfa4dOlNm1kpk53zx8mBviaKCKoGdHAF3INAtY3TN3bmnb2i65uPccTWb586shyWfAEC03qJXuL7aEmagSadeA-lpZktRIVoF9OjQVLEaQBjbLmlTMPam3EQqZ_UxgatkTfITtu6k_S_g6JYA2o6TWD6W8cdbBqyABUjqpz7qFeGUwf4lCZ5sK42vZlpVLS_gN_2VjexCeQZoEQ_mzp8I4cYZWlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23119" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WoQGIYU3ATUjOFQCDXJMTkiS4aFS4-C0BVtuidgTuam_1NuXarn4q53-iGFY-JIdb1AM-mqECNDOtxe1KVOj_uVm-Z9jhogBWtiBzl1xFNtveie6HZ8ssmCA5UTTdPMmuUCZW73eAQQTGxOxndP6sNrI88iKpgeJwc5bGcuTUhlR9yd63w-6iEwwxtI25MvL30i0SN6t1iSVcNo_H7st8J_O74j6ybVFzdRfMZc726ARR2jm8KuBWidNMHWDP5zfG9wYeQc5oHO5fJAyDLp1KQ2-i_bGGyUgyQXgnN6QGG3muEmwT8qCOGPY_3NqJXUaaiZVyzZJUYpQWMeUD6ib2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
شهربرلین‌آلمان تازگی‌ها یه مکان برای شنا زده که خانوم‌ها در اون مکان حق پوشیدن سوتین ندارند! همونطوری که مردا سینه هاشون پیداست خانوما هم مجبورند بدون سوتین وارد اونجا بشن و شنا کنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23118" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PI6k7eeznbHBvvE9AIp6dLFx66CxEhqfImvvput6k9uw07HgU_jumX-OFK-dGC8SGCsvi1hJ2UEgktO-soaHrOqDH0dEQCjJOREx3cWTkXss2ryaAU7XTtH3uCs84BEQthm_sqbcU0PilcLxcakvxEXV4KElk2NJ__-bTnU5JpLDE6CC-_jOPko7zk6XaZO2yDj7oc_cBWHx0chTaNCyfbLxVlgaYTHCFyoVGbhit846aUXvWX4qj9K0FTTIY4TSQAGoPWfYzyrEGZOgjBMbz9_XZ9tiA883-UhNLdVgcjwmEzPWXehxPekNpZi0RLE84El7odfapj62yH3m08Aybw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23117" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgWidYT2-2mVvTt4-3mUhwvUxHP3GYrsltQar21P59Ea2mQW9XlKNWys9CrCzNJzwzgoMvT6q8CdAftDkFUDnh2ibdQndcixadpy2HgPJmIZrq1TVBEaYIpK3p1Iw96xNdYrEJPH3rwR0w79RsKngkJ35CQn914vc_Yz2paNNxQmP5BNOcjpjkYrTpLcJ7TB6pDZ8JlNwYuVqUtJqrKMQUdwrhD7JeaJwNM60zfmeEvJdy-LAZo1pCzhN5a7Ydy66dHQr4jJfJ1pi--Um-6AlDoxlxXqUF3fbWnStsCULas_KcAdOEUHK2HI66OlGi2ctVj0faNFv_4E1PrOPwripQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23116" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEnogE05gufS6cBubVlTDwyzyGYE7oRdRfW3e-lUiuAlFdT-CZPXe2FtDUvGGh_jNGIBkJ2vGlvcdZg2e9r_s1HBWVX8GDOgOCE0_Qgc-4yBIZ7DfXhVe3wWrRYX0VHr_O3Cjre-6Acw_Ww_iy93-ocw3vpCXxxjk-UMMycX29snYtOrmDg18MfLscKNu9YVeu1I_F1SrYpGIVMzhfoiqayXDX2zG5p24Nl84P5IjtzlM4XZAmeETnikG6ZCuddzDEOs7JM4XVdVPvFkSw47WpCuis4oPdIdp17cfCsxUQ1MCyOfApRKewwZvLgy3tavjtzKFDrAKYsp6YE1jorsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23115" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-P6MybL7OMzzPbinfPaXOnux0l0VrIqel0cueKdQkpt9Dfz-z4kBmkDqyR-shlTRpgyGaYx3kqAgtkATQ7H1QQghCmr4Px8nRrOckSXS088Cablwc2pB-3omAxZEMXpXUn77MzKVYS6ndKuQsgBAly0AizDW3MOR4SbW6Z1tb0BY3ahcS6ZFMrbD2dbmeJhhRFSXG_ZorvMOBGtMemBs31mQAMNc4gaNbCvrFF9ihx-0C-WYnWtOQKsQfKxxkofM0FjVlSCKqmtAczcIw1-Gvt5QOuAAwWhEzvUWb_guyF_dXx5C2O9OkezZpo14stheFpcZD9glRJQs4CyAg_X8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23114" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=tvuGTrWuefDYKAhk0J-hOymboixGVCujoU8vSPyamq-KppORnajskrWEeQaIukITaXqUJrKt-VpxWeC_qDp4TK7s7g88TZuymTqoAv3I6xCB5DUViDg12CvzxtqsgCUZEEkxILuub9uZPnAyb8zi_bKYVpk7C01RvEPxA2OxSFeU-iJTNJy1Mfo1M6JJl_SRnglpVRP9ivqu852hI3s2Vd2l00O7lDZAT4v1bXmXz4JylsBFaK4Kkom-bilfpT2WsvBnRzFon243tzxXcP1CVU5GrV7a6dxHY_ibh40XULit1dmsz8woH4MdMEefODrD3wA3jndI_fO9Hl4TB3WSsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=tvuGTrWuefDYKAhk0J-hOymboixGVCujoU8vSPyamq-KppORnajskrWEeQaIukITaXqUJrKt-VpxWeC_qDp4TK7s7g88TZuymTqoAv3I6xCB5DUViDg12CvzxtqsgCUZEEkxILuub9uZPnAyb8zi_bKYVpk7C01RvEPxA2OxSFeU-iJTNJy1Mfo1M6JJl_SRnglpVRP9ivqu852hI3s2Vd2l00O7lDZAT4v1bXmXz4JylsBFaK4Kkom-bilfpT2WsvBnRzFon243tzxXcP1CVU5GrV7a6dxHY_ibh40XULit1dmsz8woH4MdMEefODrD3wA3jndI_fO9Hl4TB3WSsjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اسپید یوتیوبر معروف رفته‌سرتمرین تیم برزیل؛ بهش میگن شوت بزن اگ گلش نکردی باید شنا بری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23113" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwIo4QlubPR4StS33o0j4zUO7JrIbV8jhLCbLOuaRIyPYvlD-zN_zb80qi37xx7vUHPhyr3lyWWa1QozOJyG1bvtwsN0RMui-JYNFGegw_oDH82CTp1RuBCaVMiIPUQScXdtJPVODe4crcU75ViH1L9UI553iODDlZdRIkNOnpAnKkvdFmwHWd0ALf4E-DrlpvO8yvrwPaTqphrAkJG8TJWylcbhW-plj6Ht2eFTJrZgYR1ZKX01K3oOT94io7b8vIlLzSECDXzb46ttf4Ig99hZ7SdWTQ1OlgRsvVmsK198Mr3LIo1EJI9lGPsf2l8NZWFdE4Gxbd4GhBRFLd54fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23112" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
