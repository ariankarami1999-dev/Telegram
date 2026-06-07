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
<img src="https://cdn4.telesco.pe/file/mYPFNtUJSKMzDgyWg0Af8qSkYhCQmoszHErjlWIggJhRd2gkSGP4m-4AwxaMRPZBkVOgpwDnZ3IF5yzJFlZ0mRg_11icQNFrf5QuFAbm0EgJUCKIePBNVUlnxaUdWnoUq-PHEZYI8Lwqz3N9OYGuPyNIDZQ2zJNHz_uk7A3AuiSSETnzCImGS-8oY8hZPfmeCBEkJM-DiktS9L2an9Uf54ZZom08USeiuvpIgHaSgmMbkMp-GUnYA-XcLzy_3mgpVZ8s2z2TjSrjmcxuD3kkcJNwJn2j5OTlMrCmF9f3xuSWusGk8OCIi6fwtGYZvXY1clL6q7N3OUJZuebdQSsLTg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 254K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 00:13:13</div>
<hr>

<div class="tg-post" id="msg-77450">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cadd5da828.mp4?token=ePtE8sQKlKaI2qwQy5OnE23TMkB8W6J8gXi8sAwPreUmZl1Ul94kAk0oWvCtwj0dbt-DGbEaAPEi_mXLaVGQuv-ZbAD9boN722Owef3PMOtLaFd3UbN5ABFSoGk5rfIA6-mrCsKRxIh-aJva1EFdktiLt6fGy5I9Ax2fD5DSzlq-2WTc4GnsnJQIfSczqT8K-0Gt2eoCOhgZgEIb2laUjtIGD19IZig9buJ4NkQTnbkuoMZXzupoVW7Bw8mjrVbpyaMHgWdTgS1BTtLM2epVe1TtGaOBAppSp1JCBzVIthAzYQTx0i1z7UcwePKIhRhAH_yvdk-U9auh-TJXZNQvTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cadd5da828.mp4?token=ePtE8sQKlKaI2qwQy5OnE23TMkB8W6J8gXi8sAwPreUmZl1Ul94kAk0oWvCtwj0dbt-DGbEaAPEi_mXLaVGQuv-ZbAD9boN722Owef3PMOtLaFd3UbN5ABFSoGk5rfIA6-mrCsKRxIh-aJva1EFdktiLt6fGy5I9Ax2fD5DSzlq-2WTc4GnsnJQIfSczqT8K-0Gt2eoCOhgZgEIb2laUjtIGD19IZig9buJ4NkQTnbkuoMZXzupoVW7Bw8mjrVbpyaMHgWdTgS1BTtLM2epVe1TtGaOBAppSp1JCBzVIthAzYQTx0i1z7UcwePKIhRhAH_yvdk-U9auh-TJXZNQvTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه عبور موشک از آسمان ايران و فریاد شعار «وما رميت إذ رميت».</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/naya_foriraq/77450" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgYpN4b3Shq_ojlMjKU0R9l-RUDs8fxZxH2PytCEmCKptYSB8pj-BCfpNmviDHJeJSk4bSI3nx32aUGxNiYLx3HcWvThDuBa9h4WU9oYn_gZEFUbtkLC_FI2x8owD15OEYDuziioZGyGo0QqdNmzqyBegi5fJCGTVSlpOW5D20RinkqOGXBnUr_HNhfAjolUp3OAiSxAL6d4vF2O9Tmo6NU9qtdk3VOgcaqazzrK4YyE-wzPsfXsddZl5qA7118lYFa5Malb6NXje_Vfk3aZZuRpMzmHfJf7CjOcOKg1CPVb1lF3sxDZZ-7LjNPz4N7rb4JCw5F3z3LcLQp449FJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
المعاون العسكري للمقاومة الإسلامية حركة النجباء مغرداً</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/naya_foriraq/77449" target="_blank">📅 00:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">إعلام العدو : من المتوقع أن يتحدث نتنياهو مع ترامب خلال الدقائق القادمة.</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/naya_foriraq/77448" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">أجرى وزير الخارجية الإيراني اتصالات هاتفية مع نظرائه البريطانيين والأتراك ورئيس أركان الجيش الباكستاني لمناقشة التطورات الإقليمية في أعقاب رد إيران على انتهاكات إسرائيل لوقف إطلاق النار في لبنان.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77447" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77446">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">القوات الامنية في العراق تعلن إنذار جديد قرب مقتربات المنطقة الخضراء ومطار بغداد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/77446" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77445">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزير الخارجية الإيراني: أجريت اتصالين هاتفيين منفصلين مع نظيري التركي وقائد الجيش الباكستاني</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77445" target="_blank">📅 23:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77444">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سماع دوي انفجارات في تبريز</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/77444" target="_blank">📅 23:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77443">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71e274350.mp4?token=MuMSDY225z-Wl8S92xtm-OePp-7Rcy4b7jPZsL1v_A42sDDbd5V_NEe6ULJfY4MnBvK6gY1fmJVeRRdehDDoSnI3AkRuB1iMzh0vQctmR-2litKJQbAYA4TwkigcF8EA6QRER9zDshrv9LgqZjvrC628EuO2FZa9vYS-eC_s2bTdUezzqFXghe0NtThfM29L1EzYCdLoSZLXTZnaNQYRj27UpPThdnLtzf4UTGTaJRVCFu3a0lwZbOwDp0jcOF0j3DcPX5e_N21HDdSyLC12CO2QWj_pVD_RbkJkpKIr-H_WUOaLB34uJb7iV5b_WzBZtMNxBdSB-4_lz3Jm68As9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71e274350.mp4?token=MuMSDY225z-Wl8S92xtm-OePp-7Rcy4b7jPZsL1v_A42sDDbd5V_NEe6ULJfY4MnBvK6gY1fmJVeRRdehDDoSnI3AkRuB1iMzh0vQctmR-2litKJQbAYA4TwkigcF8EA6QRER9zDshrv9LgqZjvrC628EuO2FZa9vYS-eC_s2bTdUezzqFXghe0NtThfM29L1EzYCdLoSZLXTZnaNQYRj27UpPThdnLtzf4UTGTaJRVCFu3a0lwZbOwDp0jcOF0j3DcPX5e_N21HDdSyLC12CO2QWj_pVD_RbkJkpKIr-H_WUOaLB34uJb7iV5b_WzBZtMNxBdSB-4_lz3Jm68As9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد توضح سقوط بقايا صاروخ في صحراء كربلاء الامر الذي روجته بعض المنصات الموالية للولايات المتحدة والكيان والخليج على انه سقوط طائرة مسافرين في الصحراء</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/77443" target="_blank">📅 23:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77442">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZHhHu-5-iMc0nOIG9pp86AlSJH12bC-Y831xVLM1fG1iyaruBpbZj4IA5jIx0lIhmz93jAh1yfUsfUOS7h_o9aFlym9VIMNnhrf1KVWZCdZ_HKhx67podbXfA6wCwJZb5F5zsbc5vvoAzFkPgkAgvNHndnJM3ocIR4P0adWVNWIRfEoutGSeAwF-bfxKDsB7pgfBclBObsljTw4SlfVKEappBkeMDgyZbmecGfLOmGttGzI_jREDE3bi9XoUNrOR7GeSafT4SWi4weKr7mP6_Uk6kavR8kUXNxuF9c_Ai8kX_K5gtj3mUB3wXpXkVLYY4yDLMSrWnq2koZjdl22JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عنوان الليلة ..</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/77442" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77441">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6feea26b5.mp4?token=kqrJlr4eOvyG0Rz1TQ_B-tPHHVpUg8Qa7LN9pJrrNVJDxghKmQog2F74usSdD8mwkyUEpT_Ot-XXN2Jy7Gsl_NlkCqy0ZmgsG5Kr-qKTPWClgWOSQ5-DgHpl0lThEA7SnYzwECB2Ehqy3avkoI-mxW7GTt10KzYbFeehsd7zOQD7BAfiwqv_2RUWuJJx0oxY4wQ-cNgaiam-hjXa_iJE93cyvuidzQG2uem68gRU0nxCaUnsb6t4BZFNloFTPae5RV6A_YcEYb7F0pSQ8FJoarwtc9luhd1VgwOPT2ezlTVlf_dESzsQBa-IoEv5a1mKUkcmi3-fHlhmrvU5rJAD7HN8S_sRsyEj9BSiPKm7nxrmA8lGD3THo56x-7iO8YvmqJzMy7YHdGfFutxKxFIfFM5L-kIpbvgxNCruTEMtmaAgzX3Qeo_kwBIsBUcWv0qDLJsLTO21rAQw__5IljZl57SJt7LmDV0MfbC4czGup1pQ-0FOxfO37N5wPQv7v3uGgKUNQf9OAvTxlKxhlSLbkvclDSOWx2lb0gVN_x_hozcNtDxDlnlJfMutyVZ2Ry8Oxkunkz053KJcJzfs51XMR3vEdXVmYXhxLLZuuciqVE-FZ8FdQFr-WV2R5MILKCpxGQzBRPrB_lvkcHra2qifdXBmaQEJz8X02ek5vXeO0wY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6feea26b5.mp4?token=kqrJlr4eOvyG0Rz1TQ_B-tPHHVpUg8Qa7LN9pJrrNVJDxghKmQog2F74usSdD8mwkyUEpT_Ot-XXN2Jy7Gsl_NlkCqy0ZmgsG5Kr-qKTPWClgWOSQ5-DgHpl0lThEA7SnYzwECB2Ehqy3avkoI-mxW7GTt10KzYbFeehsd7zOQD7BAfiwqv_2RUWuJJx0oxY4wQ-cNgaiam-hjXa_iJE93cyvuidzQG2uem68gRU0nxCaUnsb6t4BZFNloFTPae5RV6A_YcEYb7F0pSQ8FJoarwtc9luhd1VgwOPT2ezlTVlf_dESzsQBa-IoEv5a1mKUkcmi3-fHlhmrvU5rJAD7HN8S_sRsyEj9BSiPKm7nxrmA8lGD3THo56x-7iO8YvmqJzMy7YHdGfFutxKxFIfFM5L-kIpbvgxNCruTEMtmaAgzX3Qeo_kwBIsBUcWv0qDLJsLTO21rAQw__5IljZl57SJt7LmDV0MfbC4czGup1pQ-0FOxfO37N5wPQv7v3uGgKUNQf9OAvTxlKxhlSLbkvclDSOWx2lb0gVN_x_hozcNtDxDlnlJfMutyVZ2Ry8Oxkunkz053KJcJzfs51XMR3vEdXVmYXhxLLZuuciqVE-FZ8FdQFr-WV2R5MILKCpxGQzBRPrB_lvkcHra2qifdXBmaQEJz8X02ek5vXeO0wY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
لحظة إطلاق الصواريخ الإيرانية باتجاه الأراضي الفلسطينية المحتلة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77441" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77440">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سوريا تغلق مطار دمشق</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77440" target="_blank">📅 23:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77439">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">إعلام العدو : في "إسرائيل"، تم اتخاذ القرار: سيبقى المجال الجوي مفتوحاً وستستمر الرحلات الجوية كالمعتاد في هذه المرحلة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77439" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77438">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0005d30c3.mp4?token=KkN8rVirh04RM_tUP49EEwiOoqwlfm0bZ4pRjiBhEzTJ2L2R-YmpssPtHPr2bSZWWgoa5VTPPysWy7i3rZ2c2kKfGmFi2ZS852yogabv672VXVsVLCznnVNCfxgdV1YjOTHph-2zjJvfS2cValrcq3wz5JD8M6-ZKl61JSeTOdm6L_wJhkTL8OKqWSJ6Dzys2LHlEGWeFG4g1xE72DiXcnMOeT6-ShKAtNASyMbUAcW075wIRBCNdR6c5FjjUOiYrETYM9MYlEOS1uyws4I8DpQkzGQ68nBu5TBMAOqtBiHOktP0sUC5aMS9kmZxwP-nTdFLRkmDpnJxRmEzgG_1wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0005d30c3.mp4?token=KkN8rVirh04RM_tUP49EEwiOoqwlfm0bZ4pRjiBhEzTJ2L2R-YmpssPtHPr2bSZWWgoa5VTPPysWy7i3rZ2c2kKfGmFi2ZS852yogabv672VXVsVLCznnVNCfxgdV1YjOTHph-2zjJvfS2cValrcq3wz5JD8M6-ZKl61JSeTOdm6L_wJhkTL8OKqWSJ6Dzys2LHlEGWeFG4g1xE72DiXcnMOeT6-ShKAtNASyMbUAcW075wIRBCNdR6c5FjjUOiYrETYM9MYlEOS1uyws4I8DpQkzGQ68nBu5TBMAOqtBiHOktP0sUC5aMS9kmZxwP-nTdFLRkmDpnJxRmEzgG_1wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد توضح سقوط بقايا صاروخ في صحراء كربلاء الامر الذي روجته بعض المنصات الموالية للولايات المتحدة والكيان والخليج على انه سقوط طائرة مسافرين في الصحراء</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77438" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77437">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قال مصدر إيراني رفيع المستوى لوكالة رويترز إن جميع القواعد الأمريكية في المنطقة ستعتبر أهدافاً مشروعة إذا هاجمت إسرائيل إيران.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77437" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77436">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">المتحدث باسم المقر المركزي لخاتم الأنبياء: يجب على الجيش الصهيوني وقف هجماته على جنوب لبنان وضواحيها.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77436" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77435">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">إعلام العدو : تستعد وزارة الصحة لنقل جميع المستشفيات إلى مناطق محمية ومجمعات تحت الأرض.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/77435" target="_blank">📅 23:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77434">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏ترامب: سأتصل بـ(نتنياهو) وأقول له بألا يرد على إيران.
‏ قريبون من الاتفاق مع إيران ولا أريد التشويش الآن على المفاوضات</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77434" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77433">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بنكين ريكاني رئيس سلطة الطيران المدني العراقي :  لا صحة لاي انباء تتحدث عن سقوط طائرة مدنية في العراق .</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/77433" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامب لـ"فوكس نيوز": لست سعيدا بالضربة الإسرائيلية لبيروت اليوم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77432" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh_IB67TA4WKPydER6N69emdT4IGH_5b0ncgqpOYYBFKuDzhpWLUWo_hA4Wj3bFO5pLWXk4YwWxuvgVW7cDsa7R4hR99EjTpYEws5ERViwEV_tt_DS31mgoAykcmVqapAwputX-CyEZBNv7yJcrDki6IQVuKqAbh30oEdwm86Bd4_SfgTi-GcGULGNK7k_kilOYBXrY4yHw0nbCpcbBWGXlhxcmgsA67TaQSqv7mMJ3EwMRqY--i8LyyjqrBT1hQaYrkWajc6EuyD9pK4z2f3POyvq2B3IoTGiD-apnzN_t_eZNO2kNKAEASQ0zkL9iu1N_BPMQKKsY_8y6S8qfRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب قائد الثورة الإسلامية ينشر: أنفاس النظام الصهيوني المهتز باتت معدودة.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/77431" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77430">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">إعلام العدو : اصابة موكدة لامرأة نتيجة الصواريخ الإيرانية التي دكت سماء شمال فلسطين المحتلة …</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/77430" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سلطة الطيران المدني في العراق: إغلاق الأجواء العراقية لمدة 72 ساعة</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77429" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812f395cfe.mp4?token=qJ6Zs1OBNoU5FW_dLZR6O7BRQoeVcG8oHweqZjhwfQEtTmKGmHTdWz44bUm53iVZTHjN223MKUsiwV3BfSzjYRPJDMpRFz9wNnaUR5G4XMtIlfgF_wZ8YhYjSXfTcNpOv-cST7F_59I1WbMrmoWl_4vONu42M56fbbnTn8SDeUYVGd4Sw-PRuBYtGjrHXn6yTBJjkBK49wTD5AB2fsQ48jrGFOEnsq3GMZbtSoaQpDFhQCK6h6QxpQSzybVnAxC0e65D0EEA55IBKJ4vIGpHE2oVrRQeXhPn-3iI1w1wIpRa7PdGeGD3fp3dseq0qAqNPUmd8GDB_ksmzdUL81xg8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812f395cfe.mp4?token=qJ6Zs1OBNoU5FW_dLZR6O7BRQoeVcG8oHweqZjhwfQEtTmKGmHTdWz44bUm53iVZTHjN223MKUsiwV3BfSzjYRPJDMpRFz9wNnaUR5G4XMtIlfgF_wZ8YhYjSXfTcNpOv-cST7F_59I1WbMrmoWl_4vONu42M56fbbnTn8SDeUYVGd4Sw-PRuBYtGjrHXn6yTBJjkBK49wTD5AB2fsQ48jrGFOEnsq3GMZbtSoaQpDFhQCK6h6QxpQSzybVnAxC0e65D0EEA55IBKJ4vIGpHE2oVrRQeXhPn-3iI1w1wIpRa7PdGeGD3fp3dseq0qAqNPUmd8GDB_ksmzdUL81xg8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر   اصابة مباشرة في شمال فلسطين المحتلة</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/77428" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77427">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77427" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77426">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHZYDHA4nM8JWqYlaeBRku-zIyj6pyulSJTrr-aR9fv8rJJgUbiBDJQEeGcOrEKAnVusfAjUn-HIVpyDj14xHVm5W0G6owDQS8U39gF5neSThMk5mcQ2SjxBLpgWTUFO8lTPjMcxnnxxQfbrPZPJG7J-lI1YXCgwV9FomwcTInLGfv0nejQLTX0vfpXgm56TH_KEzyJN0VG1GmEcY4S4yHCIUNNohawYP1EAffBtNwa3lzp8ztUHC1MPkEAKP1tJNLiBxATMEUzxM-VJwhIEWXIDeHobgYC-Yh3Ys_Z21EI75CTV4lkmgqNm2cthA-zwgfd0cI0teYhPQGE4Jyan7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف تام لحركة الطيران المدني في سماء العراق وايران …</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77426" target="_blank">📅 23:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">إغلاق المجال الجوي في غربي إيران</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77425" target="_blank">📅 23:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نقلا عن إعلام عراقي تابع للسعودية يزعم: سقوط طائرة مسافرين في صحراء كربلاء.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/77424" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77422">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8030552fb4.mp4?token=MXD5MHZgjIRJsIyKSHdqW2wJa90KvcK5EvLS6lMARLCiZZzxEELE1rVvrtuS1upykvvMvYs0G7pgFGKD2W-XCJN27-cte-7ohRQO3Ej1bj0mI7zrfXLym7xWu3xfJ8REVOODsvWk_MbxDtnCvn9gq5bbpRfJCQWSC7gY-Zyxg-kI9mFeAcDjFuMj-0D_757pjkUAFw0aORHOGn2qk1wZPjDGdYnOnbij7h-_NJ_rCy5iYfZ2VNAYXM-UKgpHxoA4DKexas8WeT1eAv9_qWHxGVvgfNVSFxFmKPYfRxi8jAduvsYMkIVibLbotbluetmb4vUpazOiT9-ZZgfMF_nVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8030552fb4.mp4?token=MXD5MHZgjIRJsIyKSHdqW2wJa90KvcK5EvLS6lMARLCiZZzxEELE1rVvrtuS1upykvvMvYs0G7pgFGKD2W-XCJN27-cte-7ohRQO3Ej1bj0mI7zrfXLym7xWu3xfJ8REVOODsvWk_MbxDtnCvn9gq5bbpRfJCQWSC7gY-Zyxg-kI9mFeAcDjFuMj-0D_757pjkUAFw0aORHOGn2qk1wZPjDGdYnOnbij7h-_NJ_rCy5iYfZ2VNAYXM-UKgpHxoA4DKexas8WeT1eAv9_qWHxGVvgfNVSFxFmKPYfRxi8jAduvsYMkIVibLbotbluetmb4vUpazOiT9-ZZgfMF_nVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">التكبيرات ترافق الصواريخ الإيرانية عنده إطلاقها نحو الأهداف الصهيونية في فلسطين المحتلة.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77422" target="_blank">📅 23:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77420">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-text">من الضاحية الجنوبية
إلى معسكرات الأمريكان في المنطقة
والخليج خصوصاً انتم تحت نيران
سرايا أولياء الدم.
سنكون في الميدان</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77420" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77419">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc5908dfb.mp4?token=JkI2gv2MsFeIpflgpQUj_QPl6HxcU4FNIhnarwoTGkma2A4Xl6aPW5dt3D_iwMGqi-4y5b1GG17gSo4BT81j7TDR3baftiYFKBC3q9R1C77-R4Za1F1e7BaWYEejHofKN4PlXgLPTq3pxCTsb2IzFOxWAb6HQwmm4_dCozQzUDYCv3koe0WNdAjQqvf6xG0BjYGby_UUzSNi9JuZrTm4lgJCBCo6AX0kY7zNshy-B1-cpgEICuOcAl5QfnPd3SIZws_aXXezRKp0efnhfeJ07QVK_WRNcrdjUjcrcLpJBumB4vRhchPZhPrzUskOop6Vp5x7h89HwmVsQV35t15Uhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc5908dfb.mp4?token=JkI2gv2MsFeIpflgpQUj_QPl6HxcU4FNIhnarwoTGkma2A4Xl6aPW5dt3D_iwMGqi-4y5b1GG17gSo4BT81j7TDR3baftiYFKBC3q9R1C77-R4Za1F1e7BaWYEejHofKN4PlXgLPTq3pxCTsb2IzFOxWAb6HQwmm4_dCozQzUDYCv3koe0WNdAjQqvf6xG0BjYGby_UUzSNi9JuZrTm4lgJCBCo6AX0kY7zNshy-B1-cpgEICuOcAl5QfnPd3SIZws_aXXezRKp0efnhfeJ07QVK_WRNcrdjUjcrcLpJBumB4vRhchPZhPrzUskOop6Vp5x7h89HwmVsQV35t15Uhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق في الشمال المحتل جراء الإصابات المباشرة للصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/77419" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77418">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWr0OzYnEvjkFvWoYKwqUKdmD2_nf2_oLr79Q3Mstp1n0CMYOVDsmsiEctC36SxC6lUfl54Ft6T8qkpWtKl--ZlvaZugSzQ9rzCJ1-8N7gH9tAP8ALz0zRdGXW_5TYpkWL4saEy-g8a4Ov_0hZEHRTZirYmjptf7cYwxPIYCXfje9qFjTCPX59vUUYMuxi_iGTefLapXmeecVUaHHhXC_RmPQis29i56F-NpvS55C5wlSzz_ZKo4I9WkOMnKK_XTOcOCRE-WZ7on6YatqBFaZI6qjiuH-CxgAVbNVQqbxhCNT6GO9hf0oC90hhwJT9U-CRu3RRTYU9G3KIeFtq41Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Come in ground baby , its World Cup</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77418" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77417">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامب : عودوا إلى طاولة المفاوضات وعقدوا صفقة يا ايران</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/77417" target="_blank">📅 23:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77416">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامب يتوسل ايران : كفى</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/77416" target="_blank">📅 23:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77415">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامب لـ Fox News: نصيحتي لإيران هي: لقد أطلقتم صواريخكم، وهذا كافٍ.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/77415" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77414">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">لواء الجولان في حركة النجباء العراقية  يوجّه بإطلاق للنار بدون توقف نحو الأهداف الأمريكية والصهيونية في المنطقة إذا تدخلت امريكا بجانب اسرائيل …</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/77414" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77413">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قاعدة رامات ديفيد الجوية استُهدفت بصواريخ باليستية
أعلنت العلاقات العامة للحرس الثوري:
بسم الله قاصم الجبارين
﴿قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ﴾
ردًا على الجرائم الواسعة التي ارتكبها الكيان الصهيوني الغاصب في جنوب لبنان، وما رافقها من قتل وتهجير واسع لأهالي صور والنبطية ومناطق أخرى، بما فيها الضاحية الجنوبية لبيروت، استهدفت صواريخ القوة الجوفضائية التابعة للحرس الثوري قاعدة رامات ديفيد الجوية، التي انطلقت منها هذه الاعتداءات.
لقد كان قبولنا بوقف إطلاق النار في 19 فروردين مشروطًا بوقف إطلاق النار في جميع الجبهات، إلا أن الولايات المتحدة والكيان الصهيوني، كما جرت العادة، لم يلتزما بتعهداتهما، فواصلا الاعتداءات والجرائم في لبنان، كما كررا الاعتداء على السواحل والسفن الإيرانية في مضيق هرمز وبحر عمان والمحيط الهندي، في انتهاك واضح لوقف إطلاق النار.
إن عملية الليلة كانت بمثابة إنذار، وفي حال تكرار الاعتداءات ستكون الردود أوسع نطاقًا، وستشمل جميع الأهداف الأميركية والصهيونية في المنطقة.
﴿وَمَا النَّصْرُ إِلَّا مِنْ عِندِ اللَّهِ الْعَزِيزِ الْحَكِيمِ﴾</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/77413" target="_blank">📅 23:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77412">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6821faae8b.mp4?token=iLzmLCe6xgXu_8HetkElXgv1ngw-1zFPp6HLaCPKrKgn0RTb6OUVYyWR5zaCEFZQsPY1lnvI6G1gF7vgOUWJ-MLZepU1qA7wQbHYm7rV_2DIwXrCsMCKohvuyqe7CTi6iSfL-9Ug9XMtb_463XLO-oZ3M6pGWeB2U6iluqhF_ShClmeYIx5EyNX8p7ujL33IdRMKwYDkTlcu-aQpU1xAXZpcUzmywOIzMS3MLc7yQmbpbZbWHgfq1NX4xPIDk6BIV_CWnyqs9oz1bgu0cwRgdlAaU4fwgSxEGY6pvhqK0FwJ-mmd8j5DF6a7PD-C95ixg6-u8vz-07R39vj74Qn0hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6821faae8b.mp4?token=iLzmLCe6xgXu_8HetkElXgv1ngw-1zFPp6HLaCPKrKgn0RTb6OUVYyWR5zaCEFZQsPY1lnvI6G1gF7vgOUWJ-MLZepU1qA7wQbHYm7rV_2DIwXrCsMCKohvuyqe7CTi6iSfL-9Ug9XMtb_463XLO-oZ3M6pGWeB2U6iluqhF_ShClmeYIx5EyNX8p7ujL33IdRMKwYDkTlcu-aQpU1xAXZpcUzmywOIzMS3MLc7yQmbpbZbWHgfq1NX4xPIDk6BIV_CWnyqs9oz1bgu0cwRgdlAaU4fwgSxEGY6pvhqK0FwJ-mmd8j5DF6a7PD-C95ixg6-u8vz-07R39vj74Qn0hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77412" target="_blank">📅 23:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77411">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">أنصار الله الأوفياء يلغون كافة الاجازات ويأمرون الكادر الجهادي بالإتحاق الفوري ..</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77411" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77410">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d01a1c2bc.mp4?token=XZsIojlKnL1ORfrxBbT1Eyc_X0XT0XJKiU1eb-WrfEq5RWpUrEp0uGsVRxGHN23SAw0wZgeCazI1z8LLFeMDFy23mmScZ70KTnQ1zhmg6YoWb-qIDSbXWLMBBZrtMt8sBDOv_W8Q1jE8WEzbHT1xxnuYW6ZKCiz8Ha1Iz-qnzbTbPWnBOwuHa_cjiyW9DCe-YcWZYsJPsBYlpk4GgyKn_Gi3MIzBM0u84e_ORV91v0StmMR6hZMwwOPCOl2M_x5eKAyQg19kTHGPV_t1cXe1Xsg7DFavIWQG9il-Ln7IrgfRqIEcRQsppueNO48ylswNEbmcCbddxiMa0ByTqA4P2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d01a1c2bc.mp4?token=XZsIojlKnL1ORfrxBbT1Eyc_X0XT0XJKiU1eb-WrfEq5RWpUrEp0uGsVRxGHN23SAw0wZgeCazI1z8LLFeMDFy23mmScZ70KTnQ1zhmg6YoWb-qIDSbXWLMBBZrtMt8sBDOv_W8Q1jE8WEzbHT1xxnuYW6ZKCiz8Ha1Iz-qnzbTbPWnBOwuHa_cjiyW9DCe-YcWZYsJPsBYlpk4GgyKn_Gi3MIzBM0u84e_ORV91v0StmMR6hZMwwOPCOl2M_x5eKAyQg19kTHGPV_t1cXe1Xsg7DFavIWQG9il-Ln7IrgfRqIEcRQsppueNO48ylswNEbmcCbddxiMa0ByTqA4P2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77410" target="_blank">📅 23:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77408">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">كتائب حزب الله: إذا تدخلت أمريكا في هذا الاشتباك سنستهدف قواعدها ومصالحها في العراق والمنطقة</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77408" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77407">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌الحرس الثوري الإيراني: استهداف قاعدة رامات ديفيد الجوية بصواريخ باليستية.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77407" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77406">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الله اكبر
اصابة مباشرة في شمال فلسطين المحتلة</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77406" target="_blank">📅 23:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77405">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a51f0607.mp4?token=UApPSe_Z55p2IY5Up_9eki57g7VINlgi4DadE2ZncleOlFnxJZ0S-4mJP7Jvh8PQ3Nu9zGmv0iEwmAnrg5VsKh1Mz6Vhc93InEk6sggugyBqNgIiAmqXnN1ENyM8U22D3NYNZpwX3GMG-FrcB5AN66UpCEPkWQboDG8nJxJIfI-gmzazl4_XTgqxl-3xmPPBYvbUaXrrz2lOpci322qsljj9I8H6Ru5qPevbU6thbeyTfHz4ERGG0ExXtqkarbt3uoN_SKHi7HdQMwaQ3RQIMaQ-JX-55y0XZfj8uz1QInzRTCKm1mBLXvZ42nzL-aTWjNMPaTBIcBy3wCP8wvFbHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a51f0607.mp4?token=UApPSe_Z55p2IY5Up_9eki57g7VINlgi4DadE2ZncleOlFnxJZ0S-4mJP7Jvh8PQ3Nu9zGmv0iEwmAnrg5VsKh1Mz6Vhc93InEk6sggugyBqNgIiAmqXnN1ENyM8U22D3NYNZpwX3GMG-FrcB5AN66UpCEPkWQboDG8nJxJIfI-gmzazl4_XTgqxl-3xmPPBYvbUaXrrz2lOpci322qsljj9I8H6Ru5qPevbU6thbeyTfHz4ERGG0ExXtqkarbt3uoN_SKHi7HdQMwaQ3RQIMaQ-JX-55y0XZfj8uz1QInzRTCKm1mBLXvZ42nzL-aTWjNMPaTBIcBy3wCP8wvFbHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویری از آسمان عراق.. بزن که خوب میزنی</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/77405" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77404">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">كتائب سيد الشهداء تعلن النفير العام باتجاه قواعد غرب اسيا</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77404" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77403">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2gJvGJ9klRvEH_qF80OlHePxIHErxpx_MaDKcF_nPJnKiT0oe2NMGyEEm189Xj0RcUB1-GttE4Dx9SCxkXjhk-wijcJCOCGICgGHsK1YGf7Kb4Kz9NUGDHdWNmyBb1I8dsr5FE2PIiQzsltYIdwBn0mqJ-iApUBvRzpbOy5hPdvjfDKFjHDbHE1DZenXw5Z3fkuY4jcXgB5xP4I3Z2MZfA_FFTKwQZ4DN814dZuKZog24SZ4hAGvfP6f7vAPMVUnH9XWRfEqO5nIjVYuLlqsKzLhyM7J6az09ej3DqcNAR7php5W_AFqMf21Bwog2MMQlXUzNXgIeY7efjfyXy00A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/aboalaa_alwalae/status/2063707145346986169?s=46</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77403" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77402">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHd8s-37zRoSCbEbjw-zAwjxg8oE8znxOb9TIpIBoQjOX0VC2I0uoc6tkt4e3gSLKpk0ongoJKuRgVr3EIlbB1LbMms5JJrQOoyEJjPFw6CPoiOhBKvqWOQRN71DDAzhxrwPzOO8fYAsNtU4XGSsXyOVmn3ek_95DwFqrCfiieg-IxcykAF4U40A1tBsGg-4QmKFRXmwEUO211Uur-st3wrMtP6ByUwZzL5zsRgm6GcKBnRuPYXyRB-3FMJgsSO2DhKzClZFrd00spJmKzz7XAkSVZYTrEyjhnv9054-ZlwQuMtkgeMH6Gv1OrM9wz-sZUY-DHGq6nEJwUezkBau4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من سماء العراق.. عبور موشک های ایران از آسمان عراق</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/77402" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77401">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a3fc885d.mp4?token=LANd1-Sn4J04yRKtA4a7Ji0SqEMW4uhaWx7WJJ007d4mJArbSy8rUwTehoLB4Av_AQ0PtZzpKrkvtXfzlmK-cocrN_1lz1X0luF7oe-Kfb7hiZ4RGIeO4bfs_eI3F_TpjkSZgtKKo3QQaeQYcigNonpZ53P3oH_lnm6roTZJM0lhzuWJsLnhPeUZI94A70pzKa-MijU0tnVDr_jL2Isk7nWRe_rKBBBTM55anJrU_3E5vlgGbLcAolm5VI3V2ijXayx8BoTyigcNHmRRYc1N-Lpzk40q-d0yHge_87PWk5MgIJFYZfSxjs8B2VCa2oX5HH0m-WX8V-HCOdf6mrDSYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a3fc885d.mp4?token=LANd1-Sn4J04yRKtA4a7Ji0SqEMW4uhaWx7WJJ007d4mJArbSy8rUwTehoLB4Av_AQ0PtZzpKrkvtXfzlmK-cocrN_1lz1X0luF7oe-Kfb7hiZ4RGIeO4bfs_eI3F_TpjkSZgtKKo3QQaeQYcigNonpZ53P3oH_lnm6roTZJM0lhzuWJsLnhPeUZI94A70pzKa-MijU0tnVDr_jL2Isk7nWRe_rKBBBTM55anJrU_3E5vlgGbLcAolm5VI3V2ijXayx8BoTyigcNHmRRYc1N-Lpzk40q-d0yHge_87PWk5MgIJFYZfSxjs8B2VCa2oX5HH0m-WX8V-HCOdf6mrDSYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من سماء العراق.. عبور موشک های ایران از آسمان عراق</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77401" target="_blank">📅 23:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77400">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انفجارات تهز سماء عمان الأردن الان</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77400" target="_blank">📅 23:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77399">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPB2LtcbMtQo-jQZcCr5UY1YpNIMLI6V_QHi3PwMbWdp7FZeGeEKOi78KEBYCxvqp77OlFwm_HJrykLEacpkwifSHnSqevHfqFdEUBitZ0IG8s0R5YQTw6n8Z_2fYNdepmfab8ddcyiIgKCnYckI0_Dr4Sc0tTQdMAl3xNwI6xZlZ6qYkk8_4uJcHVazFL0_ff1J57YuSVrdsWW0iiEB9JU5BSk8sXqxcvEmiT8JrbxzIb_KM89FZLB3gOQ4MAFRu9ClEpAqLj7SqJgp_5Xz3fbif_spLyCdzOE-SysDoZXzdNLV-0EKegX6MC2vm8_pHFbNWEZCYj4jBIrN6NCHeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو: بغض النظر عن النتائج، إيران أثبتت أنها تنفّذ تهديداتها بعد قصف "إسرائيل" لبيروت</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77399" target="_blank">📅 23:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77398">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtBRMtIIldNWXCWfh3lyHUTyJjT2VIIQKtipEB0wNHykT5YHBy_4W0JzVrib2K9z7-0oWaq2Qz_QThr5AputZhpYvesMRsChyfSpcw3n3IBlv77p_zoNPrLCDuLVf7faZ84DEHDWi7ZpmuX4wKpThODbTkogMeqCOvp9-hZtekhzeY6pJ4MJtBBs_nCmByuybcf1CXU8n8LC9j7h8gRH_slhH6NhUrwhxJ8EGMcmAPmVYG5fq7Hu7x-jY_EcI60pUPeHyuROgMmrYsWyF8fxsGuiPPhK0cebo47640JyOiw7n5mDeNXit8jkEcFzlZ85E_XxYxx-KR5I7OAaPjz-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو : رفع مستوى التأهب الأمني ​​لجميع أجنحة القوات الجوية الأمريكية العاملة في الأردن والإمارات العربية المتحدة وقطر والكويت. وأُرسلت إشعارات إلى الجناح الجوي الاستكشافي 379 في قاعدة العديد حوالي الساعة الرابعة مساءً بالتوقيت المحلي، لتجهيز الطيارين لاحتمال تجدد إطلاق الصواريخ.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77398" target="_blank">📅 23:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77397">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64bd60b95.mp4?token=WW3Uxci2Hu8gTeCXrfJB_26qc4teQXpTtSlGKao-M7arBEaITCK_VZuGMMEAQZ0X4kMVZEPKloIxi1iioVYlP6TnU7EUcHezvnctbi62ozbIggrc4b_ZuwFYsiyjEK0EZWGgI8ezFN_fmDAhVn5SY7DstMkzguZRDRn-7WZHcojxUMpR3_wqCcVV6ibvUkBZd5JMCPdEkYGCMpmMUyn-bd1XGxtuncfASyL5lkoW9DrwLiTJjGMhue16YyHrwUGebxPl1iX2_igxyqZLYfOGhafcMztH9SJXPXoRlhRQxKgZC7-IJWhIe09rqw0RZVrlhqPY5_ZXloQD4UdT-mzlrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64bd60b95.mp4?token=WW3Uxci2Hu8gTeCXrfJB_26qc4teQXpTtSlGKao-M7arBEaITCK_VZuGMMEAQZ0X4kMVZEPKloIxi1iioVYlP6TnU7EUcHezvnctbi62ozbIggrc4b_ZuwFYsiyjEK0EZWGgI8ezFN_fmDAhVn5SY7DstMkzguZRDRn-7WZHcojxUMpR3_wqCcVV6ibvUkBZd5JMCPdEkYGCMpmMUyn-bd1XGxtuncfASyL5lkoW9DrwLiTJjGMhue16YyHrwUGebxPl1iX2_igxyqZLYfOGhafcMztH9SJXPXoRlhRQxKgZC7-IJWhIe09rqw0RZVrlhqPY5_ZXloQD4UdT-mzlrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية في العفولة</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77397" target="_blank">📅 23:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77396">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الله اكبر
رشقة اخرى نحو الكيان الان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77396" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">إن لم أقف حيثُ جيش الموت يزدحمُ
فلا مشت بِيَ في طُرقِ العلا قدمُ
لا بدَّ أن أتداوى بالقنا فلقد
صبرتُ حتَّى فؤادي كلّه ألم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77395" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مصدر لنايا
خمسة فصائل عراقية بجانب أنصار الله في اليمن تستعد لاغلاق مضيق باب المندب …</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77394" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77393">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">إعلام العدو: بغض النظر عن النتائج، إيران أثبتت أنها تنفّذ تهديداتها بعد قصف "إسرائيل" لبيروت</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77393" target="_blank">📅 23:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77391">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe2282152.mp4?token=Svq000v3I9SzGzVJWhkSnu8oi_vUpA65b25cbbbz5dJomEk6W4BdJ39RGUEbrAi0BbgTJ7acdPy68heCIrlWpxsjlXOAnEawEZ18iRhbIESaAYx4p0pH1Gg_Z3GgjV9hHoUT8tFrBi_lg32q0M2jaXaGfkKuvyozq6G81HpVCdoWI4fcKbmXSy9S_FmX-9BMMMvbVMChZmLafF6TJr9vmcjjPhZcwRs-Epz64XU85riDlwTcL9T17R57zeSeuiwqpM651NcCPipK_XdVea6iQmg6kcPIreXQcaJsG8Oq7YoqaFXP0F9U6TLHkUrC58vfiduZx5Em39mhWROfLvRWmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe2282152.mp4?token=Svq000v3I9SzGzVJWhkSnu8oi_vUpA65b25cbbbz5dJomEk6W4BdJ39RGUEbrAi0BbgTJ7acdPy68heCIrlWpxsjlXOAnEawEZ18iRhbIESaAYx4p0pH1Gg_Z3GgjV9hHoUT8tFrBi_lg32q0M2jaXaGfkKuvyozq6G81HpVCdoWI4fcKbmXSy9S_FmX-9BMMMvbVMChZmLafF6TJr9vmcjjPhZcwRs-Epz64XU85riDlwTcL9T17R57zeSeuiwqpM651NcCPipK_XdVea6iQmg6kcPIreXQcaJsG8Oq7YoqaFXP0F9U6TLHkUrC58vfiduZx5Em39mhWROfLvRWmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابة مباشرة بصواريخ إيرانية في الكيان المحتل</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77391" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مصدر لنايا
الحرس الثوري سوف يضرب كل مصادر الطاقة في المنطقة إذا تم استهداف اي مصدر طاقة ايراني .</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77390" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314693a962.mp4?token=KQUKsAgrfephpVIyrNsdnY3gROdgL25nRWveYGxrsgz04iudBOp49zSm4onu1GaJy92wVH4k0IhiKooJg11qIlTGlTApkbjC8XEaZPYrteLXlHT4pJqHtHWop3mDdJBlMekvfpKLojrdLmcUz3UFGnVW0TfpALgyVXnd2BrA5xEv-fpAaXYZauk_vkdB3U2-4O0tJYodYI0cZPA7NRN41lxMzZAd52e_5SZ7TCMau5l_6rk6L0o5Lvrlh1OMYw7OuR5-1NdbYtiTRbFXQrv_DNv8l8ruSy9jmh3K9waMJmSyLHggMZ5IhTfxYCqzvjsrCnUJm3cOGogMz4qkf8F4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314693a962.mp4?token=KQUKsAgrfephpVIyrNsdnY3gROdgL25nRWveYGxrsgz04iudBOp49zSm4onu1GaJy92wVH4k0IhiKooJg11qIlTGlTApkbjC8XEaZPYrteLXlHT4pJqHtHWop3mDdJBlMekvfpKLojrdLmcUz3UFGnVW0TfpALgyVXnd2BrA5xEv-fpAaXYZauk_vkdB3U2-4O0tJYodYI0cZPA7NRN41lxMzZAd52e_5SZ7TCMau5l_6rk6L0o5Lvrlh1OMYw7OuR5-1NdbYtiTRbFXQrv_DNv8l8ruSy9jmh3K9waMJmSyLHggMZ5IhTfxYCqzvjsrCnUJm3cOGogMz4qkf8F4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابة مباشرة بصواريخ إيرانية في الكيان المحتل</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/77389" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77388">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a9ed1f308.mp4?token=IKfpo1yzfP46bQLTh0q6aaIJn4I0q9dxH7ZeS_Hs_nOhLjyvMSWuO3M071hiC9DRRrNhP55C1r0v9E69HM5GUJuzQeWNS_rjajP6r3w4s3M_5AaVRPSx98egDs7knz0mMeltzxVVoXBZ6muwi1kxR7ZsfXwsj2d2HLFETdNQaWg5VHO7cUNHEA6HRLfDOkFPc0Zl8-z-5cDxnUW2SNwfhTtvS-W30uo9MX4rMOJ2RNgnkdKzCxlWeps0gMEcYnGwWV5c7dpN4AGTf9tSaPbe6wYxqh7b87qbDH0EshcnlGhs-HTJLo0uUbkn1-3RybGE6Bo6MpDFC4cO_FbThdCKHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a9ed1f308.mp4?token=IKfpo1yzfP46bQLTh0q6aaIJn4I0q9dxH7ZeS_Hs_nOhLjyvMSWuO3M071hiC9DRRrNhP55C1r0v9E69HM5GUJuzQeWNS_rjajP6r3w4s3M_5AaVRPSx98egDs7knz0mMeltzxVVoXBZ6muwi1kxR7ZsfXwsj2d2HLFETdNQaWg5VHO7cUNHEA6HRLfDOkFPc0Zl8-z-5cDxnUW2SNwfhTtvS-W30uo9MX4rMOJ2RNgnkdKzCxlWeps0gMEcYnGwWV5c7dpN4AGTf9tSaPbe6wYxqh7b87qbDH0EshcnlGhs-HTJLo0uUbkn1-3RybGE6Bo6MpDFC4cO_FbThdCKHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ ايران نحو الكيان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77388" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77387">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ياعلي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77387" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77386">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ياعلي</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/77386" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77385">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad80048ddb.mp4?token=iJDGIfQaq9l_xjfgIxR_7Ofx_byQggjfMUGx2GE3f5lj1jDpQM279djV5CQKZ6X67EhJgPwFOUyJdcV-V1qCr6O_ZPE4gv5IzskRNIg4zjz1G3khoeMCyZALd4lVPcJeiXBhmqRUh3lUGu9nqbUbf-coOAcXCY9wsIbB40fS-u2VcPQlchUJl5SYsxClhZV4Q7m7DWMAhxU9fqHsuCTHnHK_p8hcjhv_sQB4NCqjzIJocdDz2L4ChL2XZ_PRSkeKkOkCS9fRnEYqRn_pTnr0k5FQTWBq0lwHCp0OR-YSBPx4t0OxI1eIZTJFr9pNWbUxeim97iOhHcFdKf8VpsfXGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad80048ddb.mp4?token=iJDGIfQaq9l_xjfgIxR_7Ofx_byQggjfMUGx2GE3f5lj1jDpQM279djV5CQKZ6X67EhJgPwFOUyJdcV-V1qCr6O_ZPE4gv5IzskRNIg4zjz1G3khoeMCyZALd4lVPcJeiXBhmqRUh3lUGu9nqbUbf-coOAcXCY9wsIbB40fS-u2VcPQlchUJl5SYsxClhZV4Q7m7DWMAhxU9fqHsuCTHnHK_p8hcjhv_sQB4NCqjzIJocdDz2L4ChL2XZ_PRSkeKkOkCS9fRnEYqRn_pTnr0k5FQTWBq0lwHCp0OR-YSBPx4t0OxI1eIZTJFr9pNWbUxeim97iOhHcFdKf8VpsfXGoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ ايران في سماء الكيان المحتل</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77385" target="_blank">📅 22:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77384">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea95dba377.mp4?token=oCjZ-hPs9EZ4vH9wb3R0Bf6f0DGBa-72MlmK1t1MjbmoSN3eHFgMs_VCb_6LVufhfi-_f9ExJjV3rSq1ix7aXy9EjF8Aj3Btb4j2Jn3_ZtidZIFiQ5iXY1MwmIvvUm5AGJuxES4_-F2tKNS8gSL-VhebJR81H5VqdHvm6PyiVp7wi6MDqCTYw3Gy4Boay--bluXRSRzKRwM0o-GFaaYtK9DKrt5CUnsg2joRor7xVrOjsiCntQyW_tIYRKSPL61sxbVdORzeitnxLOK5gzHSDmaM0g4gzRa2SyHYjpmolIaTz_9fb9sC28ga8fkvozYvzsEgRWS2XohNRQ-lVwzA-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea95dba377.mp4?token=oCjZ-hPs9EZ4vH9wb3R0Bf6f0DGBa-72MlmK1t1MjbmoSN3eHFgMs_VCb_6LVufhfi-_f9ExJjV3rSq1ix7aXy9EjF8Aj3Btb4j2Jn3_ZtidZIFiQ5iXY1MwmIvvUm5AGJuxES4_-F2tKNS8gSL-VhebJR81H5VqdHvm6PyiVp7wi6MDqCTYw3Gy4Boay--bluXRSRzKRwM0o-GFaaYtK9DKrt5CUnsg2joRor7xVrOjsiCntQyW_tIYRKSPL61sxbVdORzeitnxLOK5gzHSDmaM0g4gzRa2SyHYjpmolIaTz_9fb9sC28ga8fkvozYvzsEgRWS2XohNRQ-lVwzA-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من سماء لبنان السيد حسن</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77384" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77382">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8ab904de.mp4?token=rgPyZ6I-Xjs06ZBxJ_ZnUg_83FLcLxwY4JWhdEMw9B_8eu8-p8t-46SZJaTeQzMHPYVSlKTNygAax2UnrFdnzFsqnG1eCVCB8c0PLxUXMzHKFCdrIQusiTOvq9m09cpcKFaNRLnnATP8kTQgvaNFVqfM_e0-l_9Spbdwt85OTs6FUTGmE42X4I8nsrXMdKdDymJfu_iNNMM-y_YrW5-LKF36w7sQDSpXMYL2Q8Rvw5Nlj_4jQ-0MJzn65GbS_oMDWElFGMd4xDreFcBEPqMLuGVOotn9B9NZtwAj8F2KT4DdO0Mga3VU643DBjknhay7L8uO_fqwmR39ijDSjSRZQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8ab904de.mp4?token=rgPyZ6I-Xjs06ZBxJ_ZnUg_83FLcLxwY4JWhdEMw9B_8eu8-p8t-46SZJaTeQzMHPYVSlKTNygAax2UnrFdnzFsqnG1eCVCB8c0PLxUXMzHKFCdrIQusiTOvq9m09cpcKFaNRLnnATP8kTQgvaNFVqfM_e0-l_9Spbdwt85OTs6FUTGmE42X4I8nsrXMdKdDymJfu_iNNMM-y_YrW5-LKF36w7sQDSpXMYL2Q8Rvw5Nlj_4jQ-0MJzn65GbS_oMDWElFGMd4xDreFcBEPqMLuGVOotn9B9NZtwAj8F2KT4DdO0Mga3VU643DBjknhay7L8uO_fqwmR39ijDSjSRZQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ الايراني يصول في سماء الكيان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77382" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77380">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792ce38aa5.mp4?token=UfV2R_B3ZMVpgbuOtbYJu4CeB8ccgqz0Wmb-P8EnurHPp1xPjPmjUX6K1Gwt0Ta_Zlxv_mJlEb4IVlUpSiWrDmxwcq-j4_RnXf-il8jPUzLEnLxdvB88bMvjPdSQ9X_MXFG6m7AviN5cMzBwo9B1rEGMXlU6LWgUWIRCQpRimv0b7AxhK044yLqRQ8p-Nb56a8bhdHMlpYdHdegkzvOYjKor237opgBjUD6-PpZ0GLO5SQV3Li6XRMRo96TbZBStPbkFEAcT4_PuGYmYUd-LPjk__wB8nG7FTYPdlVEktt1uFj-wo31ozodaKaeF0DqqQDeZliDf54saiKngcyTzO3NFlge4i-s8OgUxv21ztHCYCJV7ReLOuwOtnLnzASvIbfD2Wlk7ZqpQUVuwP3riWKAT65S1XuiRmd3M0BXzmLO1uWdaTh7hdSxOlyQA6sZ_KmFzEiwMij7DH-yEEsqyNLJZ-UHKzpkRy8YA_ve9V9Iu74yxV1vHXs-bhhIG3rLhIzqoqoofmowMrRChpq-3KNfl44R_0Lln-_WhYMNhZ62qlhRIWn3Si_adv1X4bAt-OokivG8BIgD5BQktbqTO19Y_IzB9u18fTjQlXaGT2Fb7kjs1i5JvekQy9eGhk3lNLUXiKmaXUxPegqe-2vTga6kAsQk4LF9AR9RdkRc09cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792ce38aa5.mp4?token=UfV2R_B3ZMVpgbuOtbYJu4CeB8ccgqz0Wmb-P8EnurHPp1xPjPmjUX6K1Gwt0Ta_Zlxv_mJlEb4IVlUpSiWrDmxwcq-j4_RnXf-il8jPUzLEnLxdvB88bMvjPdSQ9X_MXFG6m7AviN5cMzBwo9B1rEGMXlU6LWgUWIRCQpRimv0b7AxhK044yLqRQ8p-Nb56a8bhdHMlpYdHdegkzvOYjKor237opgBjUD6-PpZ0GLO5SQV3Li6XRMRo96TbZBStPbkFEAcT4_PuGYmYUd-LPjk__wB8nG7FTYPdlVEktt1uFj-wo31ozodaKaeF0DqqQDeZliDf54saiKngcyTzO3NFlge4i-s8OgUxv21ztHCYCJV7ReLOuwOtnLnzASvIbfD2Wlk7ZqpQUVuwP3riWKAT65S1XuiRmd3M0BXzmLO1uWdaTh7hdSxOlyQA6sZ_KmFzEiwMij7DH-yEEsqyNLJZ-UHKzpkRy8YA_ve9V9Iu74yxV1vHXs-bhhIG3rLhIzqoqoofmowMrRChpq-3KNfl44R_0Lln-_WhYMNhZ62qlhRIWn3Si_adv1X4bAt-OokivG8BIgD5BQktbqTO19Y_IzB9u18fTjQlXaGT2Fb7kjs1i5JvekQy9eGhk3lNLUXiKmaXUxPegqe-2vTga6kAsQk4LF9AR9RdkRc09cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صاروخ الايراني يصول في سماء الكيان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77380" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77379">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رشقات جديدة تنطلق</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77379" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77378">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رشقات جديدة تنطلق</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77378" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77377">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07eecfd8f8.mp4?token=sTR6FVSrz4_1pV_MTlWM9f8MP0eo29BjhYiiTbqCLQLVcrF6fiAF1ElTSuL_L18cl0lphB7qSu7TswqqPGECqkRDLvZqxnsTwm20UUMRmxttn-NxoZW7_2Jb_HTbGtE5dAHUxjPIyksxIpWQ2ffOH9bdcu59zuWMKfAlxXWy-Ib_Yus_5GTGRba-2d9oBWdJX-hiLMwzJIGOuj0Zo2dWhJJGOKtX7jp-iwieimxp0k2f2vRk-D1Qb_GXQ0lm-t94MirxoAj6RTe5ffGddaij47iNkTIcungPJ5yzn41d6XgCYvzBpEyLNRr7bunYgoqUlVfaxxpwmMhbtgYa_qLpmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07eecfd8f8.mp4?token=sTR6FVSrz4_1pV_MTlWM9f8MP0eo29BjhYiiTbqCLQLVcrF6fiAF1ElTSuL_L18cl0lphB7qSu7TswqqPGECqkRDLvZqxnsTwm20UUMRmxttn-NxoZW7_2Jb_HTbGtE5dAHUxjPIyksxIpWQ2ffOH9bdcu59zuWMKfAlxXWy-Ib_Yus_5GTGRba-2d9oBWdJX-hiLMwzJIGOuj0Zo2dWhJJGOKtX7jp-iwieimxp0k2f2vRk-D1Qb_GXQ0lm-t94MirxoAj6RTe5ffGddaij47iNkTIcungPJ5yzn41d6XgCYvzBpEyLNRr7bunYgoqUlVfaxxpwmMhbtgYa_qLpmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77377" target="_blank">📅 22:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77376">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77376" target="_blank">📅 22:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77375">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/273a979480.mp4?token=KGybSOt_6Kx2y3d8g1s1-1UK1t5YP90BYnxnyZN9PTXE4ulJ5Va7egXyPfMLP0Vc6FaZfHNfMVPUCp61y_aspRfRjL2HCIvexnmJD8Hne1KeMeI5KCBWjIxq40dN58BZ8-gPXqqkAW7FrXSYAgygKcVyFCvAQ6uwuOJq9ke4HzraoJIzpb5e1T_6xDM7ZPkGtt0mZ7AsKQth896QPfMyTlLBenGMpiI9Qx-5YB6ZdtS2ApsGhFhHTxTt-EWha-ZtCN1F6hD_KImMH9Y3Tq8oND9JDI0uxYkYOWAPc0oLUuyzHRWuKCfGTwA5kc9Lm6CgZ3mNnVsgu1y8pBKCCT6mXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/273a979480.mp4?token=KGybSOt_6Kx2y3d8g1s1-1UK1t5YP90BYnxnyZN9PTXE4ulJ5Va7egXyPfMLP0Vc6FaZfHNfMVPUCp61y_aspRfRjL2HCIvexnmJD8Hne1KeMeI5KCBWjIxq40dN58BZ8-gPXqqkAW7FrXSYAgygKcVyFCvAQ6uwuOJq9ke4HzraoJIzpb5e1T_6xDM7ZPkGtt0mZ7AsKQth896QPfMyTlLBenGMpiI9Qx-5YB6ZdtS2ApsGhFhHTxTt-EWha-ZtCN1F6hD_KImMH9Y3Tq8oND9JDI0uxYkYOWAPc0oLUuyzHRWuKCfGTwA5kc9Lm6CgZ3mNnVsgu1y8pBKCCT6mXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في ارجاء حيفا وطبريا بالكيان الصهيوني</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/77375" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77374">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوي انفجارات في دمشق</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77374" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77373">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مقر خاتم الانبياء:
إن الكيان الصهيوني المعتدي، عبر انتهاكه المتكرر لوقف إطلاق النار، يزيد يوما بعد يوم من أعماله الشريرة ضد شعب لبنان المظلوم بضوء أخضر ودعم من أمريكا المجرمة وصمت المحافل الدولية، ويرتكب جرائم حرب باستخدام الأسلحة المحرمة بما في ذلك القنابل الفسفورية.
على الرغم من التحذيرات السابقة، فإن الكيان الصهيوني القاتل للأطفال قد تخطى جميع الخطوط الحمراء، واستهدف ضاحية بيروت.
لقد حذرنا سابقاً بأنه في حال توسيع نطاق الاستهداف في الضاحية الجنوبية لبيروت ، فإننا سنهاجم أهدافاً في الأراضي المحتلة.
يجب على الجيش الصهيوني أن يوقف هجماته على جنوب لبنان والضاحية، وفي حال توسيع هجماته على تلك المنطقة أو الرد على الهجوم الإيراني، فإنه سيواجه ضربات ساحقة ، وستبدأ هجمات تدميرية ضد الكيان وحماته.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77373" target="_blank">📅 22:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77372">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/151681d00a.mp4?token=p-l0DVJvWj2_-bdh8wPt8YfBrIwuLd0TRS9X7YhxL_L3xp6dIgudmrqiwyzOdDiBqJYchcHbaQ98wMm0rHVgiyK-aUFRodH-nP61Pzs2KPIMABMGUGjSCNV6Xj3buIrGWMALM-4P1TvkQXIThjzQQUmNGydZ2mCyTwB5UEg5qykgidYY-peDCFF3-NKIlTsYn-AD2UDL9BikvGxatx2xUgpwhOV5f2kEzZtHoEDVfrEggCNNz_BSou9Q7yy8bxz9ma19nOL1ALR7u0BVeBZuj5SzTnuhSlVHxkU82-g3ry9JCqeDap6Jk3MmqvSQGPLEi4SD7IwwBp1HkX_yczkAR46DKmvrC3mtAhsgpcy9LQ0h3pJgdEIY5UgcxxkehgdYjqfm7JzzvBIIOjVQiTEoxYs4k-YStZirR1TIW3pkuek48Ov1aiCdmiD993l06Fg9OAeTJ9coNIIETriP-C41l7j6MzKegBNXAs9-9VALYqVK5gp9NIVFzqgUerNcNJkZDqWFnYli1uYa0kHHNWZmEGaQiIlMyJrl8yX1Ln5Gi1ief-i-pfNMlVbYbFvJIvCnNIKdAbkeddMyYZlfgP9oK-dtTQ6am0jFnZhxAoznXbCx8KSXuZllJ6peVMSY9U9l3eMQA8W7RhpVor7MmY4Hg8DUmIoUb0qoZ95boEd6gXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/151681d00a.mp4?token=p-l0DVJvWj2_-bdh8wPt8YfBrIwuLd0TRS9X7YhxL_L3xp6dIgudmrqiwyzOdDiBqJYchcHbaQ98wMm0rHVgiyK-aUFRodH-nP61Pzs2KPIMABMGUGjSCNV6Xj3buIrGWMALM-4P1TvkQXIThjzQQUmNGydZ2mCyTwB5UEg5qykgidYY-peDCFF3-NKIlTsYn-AD2UDL9BikvGxatx2xUgpwhOV5f2kEzZtHoEDVfrEggCNNz_BSou9Q7yy8bxz9ma19nOL1ALR7u0BVeBZuj5SzTnuhSlVHxkU82-g3ry9JCqeDap6Jk3MmqvSQGPLEi4SD7IwwBp1HkX_yczkAR46DKmvrC3mtAhsgpcy9LQ0h3pJgdEIY5UgcxxkehgdYjqfm7JzzvBIIOjVQiTEoxYs4k-YStZirR1TIW3pkuek48Ov1aiCdmiD993l06Fg9OAeTJ9coNIIETriP-C41l7j6MzKegBNXAs9-9VALYqVK5gp9NIVFzqgUerNcNJkZDqWFnYli1uYa0kHHNWZmEGaQiIlMyJrl8yX1Ln5Gi1ief-i-pfNMlVbYbFvJIvCnNIKdAbkeddMyYZlfgP9oK-dtTQ6am0jFnZhxAoznXbCx8KSXuZllJ6peVMSY9U9l3eMQA8W7RhpVor7MmY4Hg8DUmIoUb0qoZ95boEd6gXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الرشقة الصاروخية الثانية وصلت الى حيفا ومحيطها</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77372" target="_blank">📅 22:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77371">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رشقة ثانية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77371" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77370">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96358e50ce.mp4?token=rw7lIQA1Fz3mSniXP7SvzXnWY5BdMYcj1v2qPhN_Fvujg-IbaGNIRvEC22BmJTjG33sCDBs_q1jeUR3gFc1lVvIECkL5QlZhAr2RCNL5donGuYxGrrOi6kul_lu6FXuVwrr7-eHtR9JDNqZR6kLMpYnSAvWxVpz7-zjLIdWQhW0ZdrJYcgSyr2uhoVZp0jrgNkjySkzyzrFTvAjRXLC4ncDzorNzzBlGoXWpmJhqsF0y_-NEYaCIdUOvwfSLzj6FLyNvJ27y7WZaezxtSqPq4Q8yR8L7VxLpp9HvfXM9Mqsaw1468Vrobwx5qOJhPsyy85bgV7_XtlOmhPwpHLp65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96358e50ce.mp4?token=rw7lIQA1Fz3mSniXP7SvzXnWY5BdMYcj1v2qPhN_Fvujg-IbaGNIRvEC22BmJTjG33sCDBs_q1jeUR3gFc1lVvIECkL5QlZhAr2RCNL5donGuYxGrrOi6kul_lu6FXuVwrr7-eHtR9JDNqZR6kLMpYnSAvWxVpz7-zjLIdWQhW0ZdrJYcgSyr2uhoVZp0jrgNkjySkzyzrFTvAjRXLC4ncDzorNzzBlGoXWpmJhqsF0y_-NEYaCIdUOvwfSLzj6FLyNvJ27y7WZaezxtSqPq4Q8yR8L7VxLpp9HvfXM9Mqsaw1468Vrobwx5qOJhPsyy85bgV7_XtlOmhPwpHLp65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تدك حيفا وطبريا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77370" target="_blank">📅 22:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Otxv0a-OkpXgt5v1IS5E13_bH__FmNLOJ-eZfxVW-gGR9-zlTdYwNMXddC65lyC8yDHkC5AYDn7l4YbzSNfx7LIy_AMK07UNCixgERoNsuQ7LxwmIMCGruLg8d51lsjX36xC0ko6cHMC2KO5A35oFrAFdPWbHBOO6OyGlAPl27zJoiSOqDjNO7CougKeAdBIpuHa2sNIGF5MUMm-_2RFFoZjAtb4hIFvHgdN2eB5ZMO5P7VfAXkES9_mL80wGZCdxG9eCYqWmqYXDQ8al1EaEzDFgB-lRcctBqJxcsA8mKY-0eMnqxfRHAxswZwkBchGslJzAIYz3MmAsoMj4LuhYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي ينشر</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77369" target="_blank">📅 22:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بن غفير: يجب أن تحترق طهران الليلة</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77368" target="_blank">📅 22:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3220853f05.mp4?token=HapGkqxeMgqWx6mx_p8intVasF8Py6v7nSSTalO1yHZFFmAzuf47OD02DbdqalMi_GijtsvUu72fNqM0MYBAyuFhyrzHTSRiMBL1aEu_XtHeu6396-PcZzRQIY7UeXY6zHI7eHVtWew6PCoqOo6H5I8tQB5Ig9GbEVXVHSmSzzWNWFSud6aE_7-LgMUkBDHgEWlGOxl084bIOp4W5dWRNWXb0OLAiMEhpN8zcSNeV0VbG3DohdTaw0wQItVHUP4YnQ9yFRKgNIBhfdoAE_ZT7YhX4ewcWf3PCyMDGcBgtADK3TbwiVEWRlMs13AzAdJkya44KleHMBiV4VDNlhPm9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3220853f05.mp4?token=HapGkqxeMgqWx6mx_p8intVasF8Py6v7nSSTalO1yHZFFmAzuf47OD02DbdqalMi_GijtsvUu72fNqM0MYBAyuFhyrzHTSRiMBL1aEu_XtHeu6396-PcZzRQIY7UeXY6zHI7eHVtWew6PCoqOo6H5I8tQB5Ig9GbEVXVHSmSzzWNWFSud6aE_7-LgMUkBDHgEWlGOxl084bIOp4W5dWRNWXb0OLAiMEhpN8zcSNeV0VbG3DohdTaw0wQItVHUP4YnQ9yFRKgNIBhfdoAE_ZT7YhX4ewcWf3PCyMDGcBgtADK3TbwiVEWRlMs13AzAdJkya44KleHMBiV4VDNlhPm9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تدك حيفا وطبريا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77367" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77366" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77365" target="_blank">📅 22:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d881d2cf18.mp4?token=KKtNwpDztV4hzVv_2NnTEcBAoFG0BUszsxnSTy6wn5PvkpwwlYI1kHG9xx2JW5f6Ge2eCxhLOGSYCqn0t1NZYX4N03dytp2uG8qf2gxsXotl2Qih3lDrnUbUohZSLNNRP8NLr3bXGNjExK7k8eZZF--TbtzXR7jdjQTijb7Y-Pr1kVHSlF3vzKAcE6AwCDutCiBxhLgnrwGCc8pBZZI6aYE_4_q6SxIdrSznztxP_KcvicH4VNj5-Cu5ba0kjy4nxZ8ir_JpZgilf0wZ0fNtuKVra_yefL6ye3iLgn0lWTfEgX2tnqlMvM9FYv0ks90LPi2lS3dsCmMpre-LHgkjPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d881d2cf18.mp4?token=KKtNwpDztV4hzVv_2NnTEcBAoFG0BUszsxnSTy6wn5PvkpwwlYI1kHG9xx2JW5f6Ge2eCxhLOGSYCqn0t1NZYX4N03dytp2uG8qf2gxsXotl2Qih3lDrnUbUohZSLNNRP8NLr3bXGNjExK7k8eZZF--TbtzXR7jdjQTijb7Y-Pr1kVHSlF3vzKAcE6AwCDutCiBxhLgnrwGCc8pBZZI6aYE_4_q6SxIdrSznztxP_KcvicH4VNj5-Cu5ba0kjy4nxZ8ir_JpZgilf0wZ0fNtuKVra_yefL6ye3iLgn0lWTfEgX2tnqlMvM9FYv0ks90LPi2lS3dsCmMpre-LHgkjPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من ايران تنطلق الصواريخ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/77364" target="_blank">📅 22:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77363">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8f604a0b.mp4?token=g0545kWHZuJ78yShbtdKflx47zCZJ-LU_Rhglr38Q4eFoov7Qhn2se2Se7kd5ZAJShSAv_8vXM3rXzYTJ6oVbr_EFK4fsaV3mBrWncexmU2jLl2GKH-GbXDvKkkM2cot1TxT3OopQr-6HUOHg_UdVHNQ0gOvM9KhlpFWRlS2l0CvDSYoPryvdU_p7uT4ThqegTu36D9ylS12YYWCfiwH5JcS1qGnCgcnlazlPhIjGZ1jQGcKAopdR7G616HRKRUSZA_yrCHoTidFJB7addklGRBfDRY2EsiMGWuPLLHtvKYygQ-8eBMtl9_ig5mdCtXutzzqRN22AZS3s6mTy7__jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8f604a0b.mp4?token=g0545kWHZuJ78yShbtdKflx47zCZJ-LU_Rhglr38Q4eFoov7Qhn2se2Se7kd5ZAJShSAv_8vXM3rXzYTJ6oVbr_EFK4fsaV3mBrWncexmU2jLl2GKH-GbXDvKkkM2cot1TxT3OopQr-6HUOHg_UdVHNQ0gOvM9KhlpFWRlS2l0CvDSYoPryvdU_p7uT4ThqegTu36D9ylS12YYWCfiwH5JcS1qGnCgcnlazlPhIjGZ1jQGcKAopdR7G616HRKRUSZA_yrCHoTidFJB7addklGRBfDRY2EsiMGWuPLLHtvKYygQ-8eBMtl9_ig5mdCtXutzzqRN22AZS3s6mTy7__jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثناء توجه الصواريخ الايرانية صوب هدفها في الكيان المحتل</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77363" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77362">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20a6b80f4.mp4?token=XmH6o2fcTi9LeBpP2lc8TplLC1JkcEh-Jr8heUYuzRKEPFQKkjj3vJlFWGRAGuH7tWut7LQnKC2afQEm97rPcSXgyljFSTS3v22OjamTIVUFMJ-Dy3pIz5Nc43cf_qd_p2dn0qaiPVQjQrgH3bYFgWbw2hzA6IfYtKQ6iz0OVxX8FRY_jCSOtCEB4OwWbJw8mL04ZXu7aCPejUvyc7xqTQ1o7-AGM735YisOrwXTRBDC2B16LmxnSpE7OGjd_gI9vE3aV-ypzMlMStTswPUPbRP0eQuFiO919o0gdtfCUaR4m9pfE6hhDJwPmUo4rvAVzGvnVzRuLsA8XDvT6DQNiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20a6b80f4.mp4?token=XmH6o2fcTi9LeBpP2lc8TplLC1JkcEh-Jr8heUYuzRKEPFQKkjj3vJlFWGRAGuH7tWut7LQnKC2afQEm97rPcSXgyljFSTS3v22OjamTIVUFMJ-Dy3pIz5Nc43cf_qd_p2dn0qaiPVQjQrgH3bYFgWbw2hzA6IfYtKQ6iz0OVxX8FRY_jCSOtCEB4OwWbJw8mL04ZXu7aCPejUvyc7xqTQ1o7-AGM735YisOrwXTRBDC2B16LmxnSpE7OGjd_gI9vE3aV-ypzMlMStTswPUPbRP0eQuFiO919o0gdtfCUaR4m9pfE6hhDJwPmUo4rvAVzGvnVzRuLsA8XDvT6DQNiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حيفا المحتلة تحترق سمائها واراضيها بفعل الصواريخ الايرانية</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/77362" target="_blank">📅 22:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77361">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94bbe50a85.mp4?token=I86-PeFs-E9KY7wPEgNm_Zzj_6UJGYqbhYVR3zq4AIQymgn3XasLe_H-4FoJpDEixT0qRZt8Z5U2aLDKwnBF-82415g576_AlkNUHYZxZONJ7z4IegunWyUhLV324GxwrbZqtKT6I2b4m31Fims_rV6lpuMp7AI6uAseGA3TXGE5QoJ8FcBXapXkDrEJGWV5n4UUSinakaRCBeOubYE6sJEY1Ph0QaGgZTk7xhvmJ1VpFaB_8F9hMbtGnbqXvzcvhM47jQVRrP4VYYsRk-vlG11JdnsL4kv4NJoYofil9QwNJBfbUqwzxsoYN_8k7UVht1R-Fc0ceXaGP2rDB5Cxsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94bbe50a85.mp4?token=I86-PeFs-E9KY7wPEgNm_Zzj_6UJGYqbhYVR3zq4AIQymgn3XasLe_H-4FoJpDEixT0qRZt8Z5U2aLDKwnBF-82415g576_AlkNUHYZxZONJ7z4IegunWyUhLV324GxwrbZqtKT6I2b4m31Fims_rV6lpuMp7AI6uAseGA3TXGE5QoJ8FcBXapXkDrEJGWV5n4UUSinakaRCBeOubYE6sJEY1Ph0QaGgZTk7xhvmJ1VpFaB_8F9hMbtGnbqXvzcvhM47jQVRrP4VYYsRk-vlG11JdnsL4kv4NJoYofil9QwNJBfbUqwzxsoYN_8k7UVht1R-Fc0ceXaGP2rDB5Cxsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حيفا المحتلة تحترق سمائها واراضيها بفعل الصواريخ الايرانية</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77361" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77360">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea107d1d0.mp4?token=Bv3yAFhvdRgLr-ulEHUjV0rP0gCExdP_gJfNGDRI7PrThOL9v260D7mTAnshfLdVodst-IwKX8HBwyV8XbA5D8nNuhTEbhsYthXPAqQTRVgdzYW7SK8E73m9Sa80Y9ZPbdYW3y0wm2j94n7H8Ag3Qa5a62ex--VwS9i2_ITt-5YDrl4M-27x5SS1U-6M27W-nS8Z-t-9rcN51Xok_O7JEaLaRRC4wCLrQYQGMROmF3GdQcoFbGjsbDAZAm7elYDbYWhsJpZ_5Wq6AzaZSOKKhrK2Rwgw2rd32EQ18aYXt1n2n5s2c4jf0e55bpeqt0cKwe3na_O1exgRn9P-O-q6IDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea107d1d0.mp4?token=Bv3yAFhvdRgLr-ulEHUjV0rP0gCExdP_gJfNGDRI7PrThOL9v260D7mTAnshfLdVodst-IwKX8HBwyV8XbA5D8nNuhTEbhsYthXPAqQTRVgdzYW7SK8E73m9Sa80Y9ZPbdYW3y0wm2j94n7H8Ag3Qa5a62ex--VwS9i2_ITt-5YDrl4M-27x5SS1U-6M27W-nS8Z-t-9rcN51Xok_O7JEaLaRRC4wCLrQYQGMROmF3GdQcoFbGjsbDAZAm7elYDbYWhsJpZ_5Wq6AzaZSOKKhrK2Rwgw2rd32EQ18aYXt1n2n5s2c4jf0e55bpeqt0cKwe3na_O1exgRn9P-O-q6IDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من ايران تنطلق الصواريخ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77360" target="_blank">📅 22:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77359">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bcd63ee3e.mp4?token=UPlBjIZl1TOdSRHvUNbax28BrgIl_LJ51K07Ef0KTjb37PKbAC3MrT0u4d1ORBMiXLIQyLj__KCAdI8jjYtS6wLY9dz71riH1Of9rYW3kJi9yr8OHb7cw0DOMLg6_EBTqn60aLiPJV8xg5EW0qCNshzGFZSTHSR_CBu8y_Tmv1cfU_4BvjA78WVvBPocOj9sLqH48qfW-tOscvkJu-Q0U9f-oSHGHN6znc8xABrgqxvxETOWdSxsEzqfZlNJkGcZazGcWV6eWgn8uG9aTP3ZEpKoiYQrCYjvIjAmsE_xD4wPdpVTxeNYUIdOtB0U1kG13Ui54kj3NdzNyxMrk8MTrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bcd63ee3e.mp4?token=UPlBjIZl1TOdSRHvUNbax28BrgIl_LJ51K07Ef0KTjb37PKbAC3MrT0u4d1ORBMiXLIQyLj__KCAdI8jjYtS6wLY9dz71riH1Of9rYW3kJi9yr8OHb7cw0DOMLg6_EBTqn60aLiPJV8xg5EW0qCNshzGFZSTHSR_CBu8y_Tmv1cfU_4BvjA78WVvBPocOj9sLqH48qfW-tOscvkJu-Q0U9f-oSHGHN6znc8xABrgqxvxETOWdSxsEzqfZlNJkGcZazGcWV6eWgn8uG9aTP3ZEpKoiYQrCYjvIjAmsE_xD4wPdpVTxeNYUIdOtB0U1kG13Ui54kj3NdzNyxMrk8MTrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/77359" target="_blank">📅 22:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77358">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/870ec0c7c0.mp4?token=abelGEYQ-gmIp-eO96welJB148YCOdRvscNUNy6I1z81GtpKsFK2oQWLEP8f65EFt0sqYnYWfbEf_0IiRQ4-8dINUoFaxgmBUQgx96SFpaXfwkO1tyKA26PKmXfmC5gLZbgq3gRss4C9FXriTyIEFRNrXi9VbhNz22Wtzj3QyuBMiwOVjpvVH9jD2qoLBzMPGBMBaafYLelFlVMNVYoyl80TNXoB4OxiiD6NWTk9fP_M3Ww-rbyxLuwMgW9HH99HZ53E3XxbVUa2RgrZmxxuUtjm4xePjEtwW5mGWynS1E9uo_BZPkLU615GR-Lw01HaHICoAXoGi6fmDbC5ze4cJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/870ec0c7c0.mp4?token=abelGEYQ-gmIp-eO96welJB148YCOdRvscNUNy6I1z81GtpKsFK2oQWLEP8f65EFt0sqYnYWfbEf_0IiRQ4-8dINUoFaxgmBUQgx96SFpaXfwkO1tyKA26PKmXfmC5gLZbgq3gRss4C9FXriTyIEFRNrXi9VbhNz22Wtzj3QyuBMiwOVjpvVH9jD2qoLBzMPGBMBaafYLelFlVMNVYoyl80TNXoB4OxiiD6NWTk9fP_M3Ww-rbyxLuwMgW9HH99HZ53E3XxbVUa2RgrZmxxuUtjm4xePjEtwW5mGWynS1E9uo_BZPkLU615GR-Lw01HaHICoAXoGi6fmDbC5ze4cJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  صافرات الرعب لاتتوقف</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/77358" target="_blank">📅 22:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77357">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله أكبر  طبريا ومحيطها تحت مرمى الصواريخ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/77357" target="_blank">📅 22:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77356">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حيفا ومحيطها تدك بصواريخ إيران الإسلامية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/77356" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77355">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وصلت الصواريخ الإيرانية الى الكيان المحتل</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/77355" target="_blank">📅 22:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77354">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وصلت الصواريخ الإيرانية الى الكيان المحتل</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/77354" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
مستشار قائد الثورة الإسلامية "محمد مخبر": بقصف لبنان بحضور الوسيط الإيراني، أشعل العدو طاولة المفاوضات للمرة الثالثة، مُعلناً انتهاكاته المتكررة لوقف إطلاق النار في جميع المناطق. إننا نخاطب المنتهكين بلغة القوة؛ فمحور المقاومة كيانٌ موحد، وسيدفعون ثمناً…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/77353" target="_blank">📅 22:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77352">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صواريخ تنطلق من إيران نحو الكيان</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77352" target="_blank">📅 22:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77351">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رشقة</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77351" target="_blank">📅 22:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77350">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/77350" target="_blank">📅 22:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77349">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رشقة</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/77349" target="_blank">📅 22:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77348">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الخارجية الإيرانية: مستعدون لجميع السيناريوهات</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/77348" target="_blank">📅 22:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77347">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏴‍☠️
جيش الإحتلال الإسرائيلي:
في أعقاب هجوم جيش الدفاع الإسرائيلي في بيروت وبعد تقييم الوضع، يستعد جيش الدفاع الإسرائيلي لإطلاق نار باتجاه أراضي دولة إسرائيل في الساعات القادمة. قام جيش الدفاع الإسرائيلي بتعزيز مكونات الدفاع وهو في حالة استعداد ويقظة لمجموعة متنوعة من السيناريوهات في الدفاع والهجوم.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/77347" target="_blank">📅 22:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77346">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgdNp4N0V58DYWFNHwTiNjqToQJ6eg7TS_vDpzAjoI8JxYrfRJA4ajDKWphst3sloV7sHbNCY3h4no2ZTYmf3usnbE2KTzUoqFwi15SMt-OE7edXQgjWAo4_lU19GBzb4AYQvk-GCah8wCrSmYoy2eUp2luy7yxfFiVsxvfN1rnccZ6lKm0aGokGhV453si9KtVBRiNzl01TgG8KaxjBhZ9rzkOW8URENq09fj4BdVK4I2nuncMVoX4ZB9-6JH6-4qm7Kiitd1RHgIEBtcAEFxvROVa2hOPrWcSE9_iSNGQnAnLhOyOtyFUNfXsPBxwxHoM-P8e0GSNTZ4m7xBgaQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
إلغاء التعليم غداً في كافة الأراضي المحتلة بسبب التهديدات من إيران.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77346" target="_blank">📅 22:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77345">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vK7387i4wUYCKnY95LnKGQLv42nUikG5oFU7wkzicfdn1yAFcf2fGI8Wv-KEBl7o7HjIbeWUu9mqmOs-iy5juwYg8BZ3Owt_b5fxwKUjiM9ue2R867XMlkFY0p-S2Cau8xBZSJsVv4gwFTFgHqVrzyW6DtEtb-ZVZHs4HLubvpKSntwMjE67xr94IiqoW6jYO2frHIxmf50YZwC3dp7G0KdywlYYFrmIvImBXM18SuhVjUkN-MaKRSvHBe0pnqEZOl8Rg4eRtQpc1-dCgaC2XbwsYmH17-rCRzokFKSIqyM2ACNwVJNHX3Mhe2d3sGdwEcoTHOrLQsgne0gzu5PUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
عدد من الطيران المدني يتجنب إستخدام المجال الجوي الإيراني في هذه اللحظات.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/77345" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
