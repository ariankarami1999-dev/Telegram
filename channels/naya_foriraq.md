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
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 05:08:07</div>
<hr>

<div class="tg-post" id="msg-77530">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الاصوات التي تسمع في سماء المدن العراقية نتيجة عملية إطلاق صواريخ نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/77530" target="_blank">📅 05:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77529">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb9bdd584.mp4?token=nzy0caePmOwGqjvX5Y2-90FZahRV2hd-yy6g5v1kfldNkYL7fjHvN3ifbF3m9XhXv0lP_V4ZOHHyIe3K5bU8m5PeKAQFJUuU4ZdJ6NPn9c9BIuFvzRMGkbGSZP-5UmbbfxFuUvr5HWU0mwZq7nRyWwkhQ2r_LKak5SCb92SGgrLN3xu9lylwnT_zOflvRPS1oU1L3XuwgtOXCa-aJKGc24n_aVOvkdUaTKjbeuhpxZER1PdM0UbfKyiZxDIR49xe8-kPhRTGCow3mLnjAvBD9ARaCuToCqYnEkSBdO-F8NMG6xaoEGuwX5oAGKvG402spEWxeCFu3arJplDZrUPtQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb9bdd584.mp4?token=nzy0caePmOwGqjvX5Y2-90FZahRV2hd-yy6g5v1kfldNkYL7fjHvN3ifbF3m9XhXv0lP_V4ZOHHyIe3K5bU8m5PeKAQFJUuU4ZdJ6NPn9c9BIuFvzRMGkbGSZP-5UmbbfxFuUvr5HWU0mwZq7nRyWwkhQ2r_LKak5SCb92SGgrLN3xu9lylwnT_zOflvRPS1oU1L3XuwgtOXCa-aJKGc24n_aVOvkdUaTKjbeuhpxZER1PdM0UbfKyiZxDIR49xe8-kPhRTGCow3mLnjAvBD9ARaCuToCqYnEkSBdO-F8NMG6xaoEGuwX5oAGKvG402spEWxeCFu3arJplDZrUPtQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة لانفجار في اصفهان</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/naya_foriraq/77529" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77528">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حتى الان سمع دوي انفجارين في طهران وانفجار في تبريز وانفجار اخر في اصفهان.</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/naya_foriraq/77528" target="_blank">📅 05:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77527">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">طيران حربي في اجواء العاصمة بيروت</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/naya_foriraq/77527" target="_blank">📅 05:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77526">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eaecfeaef.mp4?token=HX-9KbjdZzY5fkbd7HxWAydnzp3grSB0GkaQ-53Hs-vDcNhye_BY4Jlps63imPBGcWbPZZlG5h2I7pMxnFqEqFPmiH9qPrxJLyArmc9nDGBVbm0ljLPaqFhGBHxLeuZpGpMwK7P3-1O4B3PPctJHndyNKHx56UUvqDUabRstek1DtNpF10Nwog15VglrOfgSFeWtVmZnsSxnirSkIh7KG_sGskqPuMGckEjvg7L8ycgHxhljI1zB0AelhwBJsY7qsn9BDOglcetUxC7t9XBnGwGt_uRCPWcuZrOOMZks282-_GViLH9OvPJ-An93RQbKVrEv8EJVipVKhoECs1WEkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eaecfeaef.mp4?token=HX-9KbjdZzY5fkbd7HxWAydnzp3grSB0GkaQ-53Hs-vDcNhye_BY4Jlps63imPBGcWbPZZlG5h2I7pMxnFqEqFPmiH9qPrxJLyArmc9nDGBVbm0ljLPaqFhGBHxLeuZpGpMwK7P3-1O4B3PPctJHndyNKHx56UUvqDUabRstek1DtNpF10Nwog15VglrOfgSFeWtVmZnsSxnirSkIh7KG_sGskqPuMGckEjvg7L8ycgHxhljI1zB0AelhwBJsY7qsn9BDOglcetUxC7t9XBnGwGt_uRCPWcuZrOOMZks282-_GViLH9OvPJ-An93RQbKVrEv8EJVipVKhoECs1WEkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
ان عادت العقرب عدنا لها
#شاركها</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/naya_foriraq/77526" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77525">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حتى الان سمع دوي انفجارين في طهران وانفجار في تبريز وانفجار اخر في اصفهان.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/naya_foriraq/77525" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77524">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏القناة 14العبرية: مقاتلات إسرائيلية تشن غارات في إيران</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/naya_foriraq/77524" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77523">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الاصوات التي تسمع في سماء المدن العراقية نتيجة عملية إطلاق صواريخ نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/naya_foriraq/77523" target="_blank">📅 04:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77522">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌟
الاجسام الغريبة المتطايرة في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/naya_foriraq/77522" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77521">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f6debd1d.mp4?token=HT6wPlwetoWL8PQ4ppeMWpCoPEboVPF4Nyy7RhTIJQYRIxzVAJTZ5-navZC0k5Wtj0oPNBEvbCihaHr6FxCfcZ6vjcni6bUDXp9_MT1KQ8kEsV2yoLQB1j0-CZaeaur8mdXvNMNlFU3a82yH2tbbHiMVVujuqlepToQafe0qNE39t4TVh0rMO-KYvj_mIqnoEmqQUwDY86izSC2EBNm7Hk0BtbwJmKhTkGdpR9HEUvbHfd_JrP7b6Q-GrcgjHZkS4piYvCMHy95B3VMaBb7VOxnU_nBJeXvdRUa-loXtEZxpu7asbyYe_QvMsuwsfl9qoxaWuh8-KhROqhJrJsbF3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f6debd1d.mp4?token=HT6wPlwetoWL8PQ4ppeMWpCoPEboVPF4Nyy7RhTIJQYRIxzVAJTZ5-navZC0k5Wtj0oPNBEvbCihaHr6FxCfcZ6vjcni6bUDXp9_MT1KQ8kEsV2yoLQB1j0-CZaeaur8mdXvNMNlFU3a82yH2tbbHiMVVujuqlepToQafe0qNE39t4TVh0rMO-KYvj_mIqnoEmqQUwDY86izSC2EBNm7Hk0BtbwJmKhTkGdpR9HEUvbHfd_JrP7b6Q-GrcgjHZkS4piYvCMHy95B3VMaBb7VOxnU_nBJeXvdRUa-loXtEZxpu7asbyYe_QvMsuwsfl9qoxaWuh8-KhROqhJrJsbF3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
اجسام غريبة في سماء العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/naya_foriraq/77521" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77520">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mm9sVn0iOvJd83wK-f6x7WCdsqHOCf7qafEdcllUBK8EQRInqIiDwBCRMcyBFIJYr9q2JUN7JbdNteBJ6kUd7eL4ygHyd4hVgDwHdPss8WCDNpSxCUgdlxd_R2khZfUVlTTeTwBETn9XnBSHH2BsjW4dqU9rpFL6_Ayrtgc_XwlExpZc57SOxDlIAp-DzL6O1gh4XbZA6nB460-ul2K0pX5YFQ_cHgHlVRMkr5D_yQuGwya8ZnVQCdWe9MjUD8lByf_KTCYzxxxWK4-tnG6fqtlcIn_JaAmJDtClJdnzhQWN-I4plvYBQCFgPwWxz1XmjTUSCqPFJMlVGJpxNzrf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار في اصفهان وارتفاع اعمدة الدخان</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/77520" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77519">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات متتالية في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/naya_foriraq/77519" target="_blank">📅 04:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77518">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🌟
سماع دوي انفجار قوي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/naya_foriraq/77518" target="_blank">📅 04:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77517">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">أنباء عن دوي انفجار في طهران</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/naya_foriraq/77517" target="_blank">📅 04:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77516">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2ba7451f0.mp4?token=bi2ZQyQidCX0NNEEaXWm-j8y2qCqvuuQ00m9KDQAIDfeX8k3j3gG9VexTSg6NgXhhfadhm84wnJcM92uSxkUn_A3j6qdT0RbZKefqjArnezjM-5broB_8QxtRQZ2d1eH8Je8IOUfN4IINFtHBsU8UUY0rHwmiSmucq6bp0gmMc6aTRpqAHeFm2mEQQ6Suv4et6cHtpsiBHnfgZQ5zjZpBtUUbPTZv8S7tB2Ruq945E75QgO3zeNCT6jqRMzEjtFyafKPt6uBs9Fg4on8U2lpMAImGtlU7CBoTnfQ5vnEkPosaR6BfFyLkoBhyn4IQpNYlFgMUe2hmasdpNB2BX_I-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2ba7451f0.mp4?token=bi2ZQyQidCX0NNEEaXWm-j8y2qCqvuuQ00m9KDQAIDfeX8k3j3gG9VexTSg6NgXhhfadhm84wnJcM92uSxkUn_A3j6qdT0RbZKefqjArnezjM-5broB_8QxtRQZ2d1eH8Je8IOUfN4IINFtHBsU8UUY0rHwmiSmucq6bp0gmMc6aTRpqAHeFm2mEQQ6Suv4et6cHtpsiBHnfgZQ5zjZpBtUUbPTZv8S7tB2Ruq945E75QgO3zeNCT6jqRMzEjtFyafKPt6uBs9Fg4on8U2lpMAImGtlU7CBoTnfQ5vnEkPosaR6BfFyLkoBhyn4IQpNYlFgMUe2hmasdpNB2BX_I-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجار جديد في بغداد</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/naya_foriraq/77516" target="_blank">📅 04:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77515">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb41d32833.mp4?token=AEMa1ch8quqAVVpJHv7bLmVwjv_EDULaLnhvEAJsTbXNVLk1aB0ydTquUa2tCsogdWqhxw1P_sozmRUGHjCljBOkreFmHFLsTvYvvF9lM80J_Qm_xvlAEBJlS3LDRUg1A4odWBbOGdke_zXkFGIl9Mp-cpdUwM6Vi1uAZtZZlj8_xVhE7gIoCP4JAjW0tD13sseZF9k6Mpdl7Ch8m-2f8KxEiIwCr9MfoC4t5xwAKENcEpTBEX15gtCOlN2Z77_shSUDqehSDWXWHXIyQkkwXYY8O2ry4oFgCvu4zOHld9DJiYzJcmnkl3bw64ORBFYuK0k6yZVpXWBmqiVA_13H-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb41d32833.mp4?token=AEMa1ch8quqAVVpJHv7bLmVwjv_EDULaLnhvEAJsTbXNVLk1aB0ydTquUa2tCsogdWqhxw1P_sozmRUGHjCljBOkreFmHFLsTvYvvF9lM80J_Qm_xvlAEBJlS3LDRUg1A4odWBbOGdke_zXkFGIl9Mp-cpdUwM6Vi1uAZtZZlj8_xVhE7gIoCP4JAjW0tD13sseZF9k6Mpdl7Ch8m-2f8KxEiIwCr9MfoC4t5xwAKENcEpTBEX15gtCOlN2Z77_shSUDqehSDWXWHXIyQkkwXYY8O2ry4oFgCvu4zOHld9DJiYzJcmnkl3bw64ORBFYuK0k6yZVpXWBmqiVA_13H-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ في سماء العاصمة بيروت</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/77515" target="_blank">📅 04:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77514">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
سماع دوي انفجار قوي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/naya_foriraq/77514" target="_blank">📅 04:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77513">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">أنباء عن دوي انفجار في طهران</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/naya_foriraq/77513" target="_blank">📅 04:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77511">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🌟
سماع دوي انفجار قوي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/77511" target="_blank">📅 04:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77510">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3632f7ab53.mp4?token=HV-2WWX9A9YPcAKEiEOfa8WeVQX0NX3IGKW8bmifObK_BaYNGoYLfE0g5POJzq9egnfsmbqf7LDIQL4usCmXfQJmAIiwTa5phWp8nw-wtTHmPR6aZWRAqraJlQgDA0Y8vU35hGE_en1eCLTeTb64__oSmEseWuYhnddreMOvP4RbbwpgVPogEq8AkNEZOGxnq8LsMFvBF3Bx8XYFriDe3d0Wcqbed7RR4YFlEpyR_D-6z2ftgfLaxJLqKGL8i-sJs75wDFyD3TUcsEkRl9Pffg1NyfWWn3uWPTCpR0vfy2OYCNNjbmXFLbZpDeTRjXhgeiMA2bwRroVCPd1TyxFLmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3632f7ab53.mp4?token=HV-2WWX9A9YPcAKEiEOfa8WeVQX0NX3IGKW8bmifObK_BaYNGoYLfE0g5POJzq9egnfsmbqf7LDIQL4usCmXfQJmAIiwTa5phWp8nw-wtTHmPR6aZWRAqraJlQgDA0Y8vU35hGE_en1eCLTeTb64__oSmEseWuYhnddreMOvP4RbbwpgVPogEq8AkNEZOGxnq8LsMFvBF3Bx8XYFriDe3d0Wcqbed7RR4YFlEpyR_D-6z2ftgfLaxJLqKGL8i-sJs75wDFyD3TUcsEkRl9Pffg1NyfWWn3uWPTCpR0vfy2OYCNNjbmXFLbZpDeTRjXhgeiMA2bwRroVCPd1TyxFLmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
سماع دوي انفجار قوي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/77510" target="_blank">📅 04:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77509">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دوي انفجار في مدينة تبريز الإيرانية</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/naya_foriraq/77509" target="_blank">📅 04:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77508">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
سماع دوي انفجار قوي في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/naya_foriraq/77508" target="_blank">📅 04:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77507">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🌟
اعلام العدو
: تقرير يفيد بأن حزب الله يستعد لإطلاق كثيف باتجاه إسرائيل.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/77507" target="_blank">📅 04:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77506">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
‏
الخارجية الأميركية:
أنباء عن صواريخ أومسيرات أوقذائف في المجال الجوي الأردني.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/77506" target="_blank">📅 03:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77505">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اكسيوس: لا أعتقد بوجد شيء وشيك فيما يتعلق بضربة إسرائيلية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/77505" target="_blank">📅 03:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77504">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
اعلام العدو: ‏
مسؤول أمريكي يتحدث عن المحادثات بين ترامب ونتنياهو: طلب ترامب عدم الرد على الهجوم الصاروخي والانتظار بضعة أيام لإجراء المفاوضات، وقد وافق نتنياهو "نوعاً ما" -.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/77504" target="_blank">📅 02:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77503">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اكسيوس: يُنكر المسؤولون الأمريكيون إعطاء "ضوء أخضر" لإسرائيل لشن هجوم على بيروت. وقال أحد المسؤولين: "لم يكن لنا أي دور في هذا الأمر".</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/77503" target="_blank">📅 02:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77502">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⭐️
توثيق يظهر إنفجار في سماء محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77502" target="_blank">📅 02:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77501">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
اعلام العدو:
نقطة مثيرة للاهتمام: كبار أعضاء الحزب الجمهوري - بما في ذلك ليندسي غراهام المتشدد تجاه إيران - لم يغردوا.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/77501" target="_blank">📅 02:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77500">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
🏴‍☠️
‏مسؤول أميركي: نتنياهو وافق "بشكل ما" على تأجيل الرد على هجوم إيران.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77500" target="_blank">📅 02:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77499">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf76df37a.mp4?token=VZ_1yYiLbNxzdysQ94QA0d2OFKF0RWeRC1McYPvbGAYsqPhHOZI50FeU9l3fo0-C2pAKNa6tqECzjQt6jDI0HRXokivmn0dfHm-RorFJe2s0nBPllrdOazqbOaZw68FRUYfVMEjgrKfQRzNtlWX7kmSCG0-HHngCKLq678KyItCovh7LBhYDaov0ZzaPaQss53zIimZajHCzOX3G11AwdTmij1mHFahb4DwAYLL4wRRbMLXulnoA70YJ__ujSTplcyDrruuUKbP_hoMgGClZ3MwG1JaDHT1SmTmrFLCLXj5EZybS4Lr_OoQTLt_ucE8KnZfXEcmCgVJZ0cFU1e7FpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf76df37a.mp4?token=VZ_1yYiLbNxzdysQ94QA0d2OFKF0RWeRC1McYPvbGAYsqPhHOZI50FeU9l3fo0-C2pAKNa6tqECzjQt6jDI0HRXokivmn0dfHm-RorFJe2s0nBPllrdOazqbOaZw68FRUYfVMEjgrKfQRzNtlWX7kmSCG0-HHngCKLq678KyItCovh7LBhYDaov0ZzaPaQss53zIimZajHCzOX3G11AwdTmij1mHFahb4DwAYLL4wRRbMLXulnoA70YJ__ujSTplcyDrruuUKbP_hoMgGClZ3MwG1JaDHT1SmTmrFLCLXj5EZybS4Lr_OoQTLt_ucE8KnZfXEcmCgVJZ0cFU1e7FpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الحشود الغفيرة في ساحة الثورة بالعاصمة الإيرانية طهران تطالب "السيد مجيد الموسوي" بقصف تل أبيب.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/77499" target="_blank">📅 02:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77498">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
🏴‍☠️
‏
مسؤول أميركي:
نتنياهو وافق "بشكل ما" على تأجيل الرد على هجوم إيران.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/77498" target="_blank">📅 02:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77497">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏴‍☠️
وزارة الصحة الصهيونية
توجّه المستشفيات برفع الجاهزية والعمل وفق تعليمات الطوارئ، مع تعزيز الكوادر والاستعداد لإخلاء المرضى عند الحاجة.ى.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/77497" target="_blank">📅 02:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77496">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🌟
‏
وزير الخارجية العراقي:
الفصائل المسلحة مطالبة بتسليم الصواريخ الباليستية والمسيّرات.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/77496" target="_blank">📅 02:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77495">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌟
‏ترامب: الضربات الإيرانية لم تغير هدفنا في إتمام المحادثات الأمريكية الإيرانية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/77495" target="_blank">📅 01:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77494">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
‏ترامب: لن يكون أمام نتنياهو "خيار" سوى قبول الاتفاق مع إيران.  أنا الذي أتخذ القرارات، أتخذ كل القرارات، نتنياهو لا يتخذ القرارات.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/77494" target="_blank">📅 01:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77493">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
‏
ترامب:
لن يكون أمام نتنياهو "خيار" سوى قبول الاتفاق مع إيران.
أنا الذي أتخذ القرارات، أتخذ كل القرارات، نتنياهو لا يتخذ القرارات.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/77493" target="_blank">📅 01:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77492">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
ستبقى محطات المترو في الخط الأحمر مفتوحة طوال الليل وستستخدم كَملاجئ للمستوطنين.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/77492" target="_blank">📅 01:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77491">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9f90571f.mp4?token=d5Xl3rjOpBdGeEl6AkGZTiy4wlmVBx6Ze7l4b283gjWoNxgvJzRvZR1NEx8h9JV42r31UXZnFEUVjOGVxasrmdwDcZXmzzTv75YU105SghBQnYlPoLL5WLfdGLkpPhT3uCZM6719aFc8otCbIKQIbMl3jnmxVJENOt-ux-s__Wn5VYDJfRzGMA-dE1ldLG3Vtm1AlYs5MTJ1tfuFnZEtu8mmME31e86hFf6zQwqc27NEsuCINZOa504mzX6tgnRdsmGYqMByFJxO9gJLL83hiPr6e6Z3UqucNUAUn7JUuaKjz9ZcLOIJ5s7xD5UOAuO5op_DVKkRbak2TzUhq-0a-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9f90571f.mp4?token=d5Xl3rjOpBdGeEl6AkGZTiy4wlmVBx6Ze7l4b283gjWoNxgvJzRvZR1NEx8h9JV42r31UXZnFEUVjOGVxasrmdwDcZXmzzTv75YU105SghBQnYlPoLL5WLfdGLkpPhT3uCZM6719aFc8otCbIKQIbMl3jnmxVJENOt-ux-s__Wn5VYDJfRzGMA-dE1ldLG3Vtm1AlYs5MTJ1tfuFnZEtu8mmME31e86hFf6zQwqc27NEsuCINZOa504mzX6tgnRdsmGYqMByFJxO9gJLL83hiPr6e6Z3UqucNUAUn7JUuaKjz9ZcLOIJ5s7xD5UOAuO5op_DVKkRbak2TzUhq-0a-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
الإعلام الإيراني:
عملية نقل الطائرات المدنية من مطار مهرآباد في العاصمة طهران إلى مكان أخر.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/77491" target="_blank">📅 01:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77490">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترمب لنيويورك بوست: الأمور تسير بشكل جيد وأي تصعيد إضافي لن يؤدي إلا إلى عرقلة المفاوضات</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77490" target="_blank">📅 01:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77489">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5ee21503.mp4?token=Ja3CGWz8SpIz9hoC9uPQoXWvl_evdwXAPpQh8ClLz_jIMYBW0V5iSB1bWqGr3WZymD_hejHdYXSPFw8beO6o-Cq6dHBHkVvforEHPNcOFnN7bCfRxdrud3Thj7Cu_cQ5EX2nqQZXJxO8IksubxUjZXsZaTwuTootsWiUdd-r6ExDQsoa4Zk0qo5PM2ENNrlZW2g3I6l6Me4g3vUO87_gJdhKv-cAhOQETYpBGM60P0MiSmWyeJD2TN3fWBktg7mBFM1Mmp06ZTyhkZIjxsUGuL26TapWeAzywwC_dWxALQCk6dngXKtEZoBOIpurjfd5X0K3DolEfktoKMS36KQl-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5ee21503.mp4?token=Ja3CGWz8SpIz9hoC9uPQoXWvl_evdwXAPpQh8ClLz_jIMYBW0V5iSB1bWqGr3WZymD_hejHdYXSPFw8beO6o-Cq6dHBHkVvforEHPNcOFnN7bCfRxdrud3Thj7Cu_cQ5EX2nqQZXJxO8IksubxUjZXsZaTwuTootsWiUdd-r6ExDQsoa4Zk0qo5PM2ENNrlZW2g3I6l6Me4g3vUO87_gJdhKv-cAhOQETYpBGM60P0MiSmWyeJD2TN3fWBktg7mBFM1Mmp06ZTyhkZIjxsUGuL26TapWeAzywwC_dWxALQCk6dngXKtEZoBOIpurjfd5X0K3DolEfktoKMS36KQl-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
انفجارات متتالية في سماء محافظة السليمانية شمال العراق</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/77489" target="_blank">📅 01:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77488">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترمب لنيويورك بوست: الأمور تسير بشكل جيد وأي تصعيد إضافي لن يؤدي إلا إلى عرقلة المفاوضات</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/77488" target="_blank">📅 01:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77487">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
دول العالم تتوسل بايران
وزير الخارجية البريطاني كوبر:
يجب على إيران إظهار ضبط النفس وخفض التصعيد فوراً.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/77487" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77486">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY-Qr7PQRRUhkXXdeGqlhkG3uO1F1stQiYY5tetkwu05JJwCDVzw7-jzGa_xvaWTcymJkwzsQho_qnug_oL54-nTDHlX5LytHA4VChfT5gQe27vcN07meYdje_2l_qoFu_NsGWgCw9izEhltEElUj0xHVj9ZtDil_hnVTr4DfjszINz28-JYzvsBZ0mNBMkLHjgThyVL-IGJxzbOAu8bdldbJbvEe6ecmVaLx7M8RA35zT6-WazKytTtn3hI2EtxzDycRwYYOXiiLijGCQL_xZ9sylq6urIWXqIJ4o4tKljwgWqkyWhFBhCHUiQ48MBIr2-yz141ZoCwlnpHPFVx_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية إسماعيل بقائي.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/77486" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77485">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
الاعلام الايراني:
هزة ارضية في محافظة هرمزجان المطلة على الخليج الفارسي بدرجة ٣.٦.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/77485" target="_blank">📅 01:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a5a66d4c9.mp4?token=G_KhABNJHIvJVtt2HHqjkqS9a98l-OWGNovkwTxkHyiExkipUlugqk08cvhICYg8uLbf7tvvbMCgiafvZABcXVwNmB3qiGmYfesgXBa1TONaO--eAGR_AceXUsXyxw0ofs0T3SEWlUYy4i3wbVEcB_p4KFz_W9_Qh5Vt2NLAmi1EKgrmQBglXpJeS-j2YT_qkAxsiV2CW2dZXWnHOG1LPDeqboufvZPraz_u5Lx8gkWuSutfexdZkKE9D6sG7O4Ktd-GNQWgrlzrVZDO2BlIxZNtWHUL7wDx7WADVWByH1nanIRpVgwbb_WlQiKnkuMUPjGrtMSMux938rr70Ppdcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a5a66d4c9.mp4?token=G_KhABNJHIvJVtt2HHqjkqS9a98l-OWGNovkwTxkHyiExkipUlugqk08cvhICYg8uLbf7tvvbMCgiafvZABcXVwNmB3qiGmYfesgXBa1TONaO--eAGR_AceXUsXyxw0ofs0T3SEWlUYy4i3wbVEcB_p4KFz_W9_Qh5Vt2NLAmi1EKgrmQBglXpJeS-j2YT_qkAxsiV2CW2dZXWnHOG1LPDeqboufvZPraz_u5Lx8gkWuSutfexdZkKE9D6sG7O4Ktd-GNQWgrlzrVZDO2BlIxZNtWHUL7wDx7WADVWByH1nanIRpVgwbb_WlQiKnkuMUPjGrtMSMux938rr70Ppdcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
إحتفالات في شوارع العاصمة الإيرانية طهران بعد الهجوم الصاروخي المبارك على الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77483" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">إعلام العدو : وزارة النقل: "اعتبارًا من الغد، سيكون حجم النشاط في خطوط الحافلات 75% من النشاط العادي، وفقًا لتقييم الوضع وتوجيهات قيادة الجبهة الداخلية. في هذه المرحلة، تعمل سكك الحديد الإسرائيلية، والقطار الخفيف في القدس، والقطار الخفيف في منطقة غوش دان كالمعتاد، بينما لا يعمل التلفريك في حيفا حتى إشعار آخر"</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/77482" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
🌟
انتهت المكالمة بين نتنياهو وترامب بانتضار التفاصيل.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/77481" target="_blank">📅 01:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77480">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🌟
اعلام العدو:
إيران تعود إلى مبدأ وحدة الساحات".</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/77480" target="_blank">📅 01:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77479">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامب: كل من إسرائيل وإيران نالتا نصيبها من الضربات والمنطقة ليست بحاجة لضربات أخرى.  الاتفاق سيكون جيدا ولا أريد أن ينهار بسبب التصعيد الحالي بين إسرائيل وإيران.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/77479" target="_blank">📅 00:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77478">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامب: كل من إسرائيل وإيران نالتا نصيبها من الضربات والمنطقة ليست بحاجة لضربات أخرى.
الاتفاق سيكون جيدا ولا أريد أن ينهار بسبب التصعيد الحالي بين إسرائيل وإيران.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/77478" target="_blank">📅 00:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77477">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47043baffe.mp4?token=gWaRBbNvpvZVnpd6f9I3z2uZsUNRdpzR7yTMtAtw08faGzkh8FJXVkV2h7DA84NQ_kHAWETK2x3IeDB2w7aZ6nz86uc-bNyusRWbOtrOFdDbzylyuIGTN_r_uBZNKcdtBsBS2zjfNU2BjwlQ9V5cD4sGDUSP6gBHU-ulrHX78DpjeZke59pN4FzysDKJBs4669eHUYBHY7t65Fp0Oi8-CktHd3Q0UcsZQAHcV3G1klGDvRVXF_R1F3t_YTMz3c6SloLGdVWZctjGIB4NK_Xw84MwT3Ff9sVDYoguZRvR92vGDWxCMJ4_NsvcTUXVVQfwVVCi-a43wGrO1SZ8_KzGEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47043baffe.mp4?token=gWaRBbNvpvZVnpd6f9I3z2uZsUNRdpzR7yTMtAtw08faGzkh8FJXVkV2h7DA84NQ_kHAWETK2x3IeDB2w7aZ6nz86uc-bNyusRWbOtrOFdDbzylyuIGTN_r_uBZNKcdtBsBS2zjfNU2BjwlQ9V5cD4sGDUSP6gBHU-ulrHX78DpjeZke59pN4FzysDKJBs4669eHUYBHY7t65Fp0Oi8-CktHd3Q0UcsZQAHcV3G1klGDvRVXF_R1F3t_YTMz3c6SloLGdVWZctjGIB4NK_Xw84MwT3Ff9sVDYoguZRvR92vGDWxCMJ4_NsvcTUXVVQfwVVCi-a43wGrO1SZ8_KzGEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات جديدة في منطقة طاسلوجة بمحافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/77477" target="_blank">📅 00:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77476">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سماع دوي انفجار في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/77476" target="_blank">📅 00:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77475">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سماع دوي انفجار في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/77475" target="_blank">📅 00:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77474">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🌟
🌟
انتهت المكالمة بين نتنياهو وترامب بانتضار التفاصيل.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/77474" target="_blank">📅 00:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCx6Q_7HmWzv9BUMQYaCs58JyHVip5BvJwgSa1Bo0ax42kGPzCcbGP3P3NdbD2gDgaXCL8JWIg0dWFV6MN45D6cRo_XJZ75xucupqrdU895R4SUyfa_KJuSP3BlU9acUvmmhOa73Z8HcDSpcvg62UMW2k4HLW5IxISbP58V31nWoYtW20ebQnRUZ035-XbiFclR1PFwStA40YXEmjgy-e9mCU1BFnoWeHBlujvZ2fBqbHDQJBtVSYLvSkOr0VGWt5YJrrmLqeEO_-W4a55czE0luFXinStRNkm1LPepMAD2RJXb1vP1dqINcfwVFK-PZ5gVxp00FJP9dz_PqQl8V2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بيان وزارة الخارجية الايرانية:
بسم الله الرحمن الرحيم
‏فمن يهاجمك، هاجمه بالمقابل
‏بيان وزارة الخارجية بشأن الضربات الدفاعية الإيرانية ضد أهداف الكيان الصهيوني
‏في أعقاب الانتهاكات المتكررة لوقف إطلاق النار المؤرخ في 8 أبريل وتكرار الأعمال العدوانية من قبل الكيان الصهيوني ضد لبنان والجمهورية الإسلامية الإيرانية، بما في ذلك التواطؤ مع الجيش الأمريكي الإرهابي في الهجمات الأخيرة التي استمرت أسبوعين على السفن الإيرانية وأهداف في المناطق الجنوبية من البلاد، فضلاً عن التواطؤ مع النظام الأمريكي في القرصنة البحرية ضد الشعب الإيراني، قامت القوات المسلحة للجمهورية الإسلامية الإيرانية مساء يوم الأحد 7 يونيو 2026، في إطار الحق الأصيل في الدفاع المشروع وفقاً للمادة 51 من ميثاق الأمم المتحدة، بضرب عدة أهداف عسكرية في الأراضي الفلسطينية المحتلة الشمالية.
‏تؤكد الجمهورية الإسلامية الإيرانية، معربة عن عزم الشعب الإيراني الجاد على الدفاع بحزم عن أمنه ومصالحه الوطنية أينما رأت ذلك ضرورياً، أن وقف إطلاق النار في لبنان كان جزءاً لا يتجزأ من تفاهم وقف إطلاق النار المؤرخ في 8 أبريل 2026، وأن حكومة الولايات المتحدة تتحمل المسؤولية المباشرة عن انتهاكات وقف إطلاق النار من قبل الكيان الصهيوني وما ترتب عليها من عواقب، فضلاً عن أي تصعيد للتوترات في المنطقة.
‏تحذر الجمهورية الإسلامية الإيرانية من أن أي مغامرة خبيثة من جانب النظام الصهيوني ضد لبنان أو الجمهورية الإسلامية الإيرانية ستواجه رداً ساحقاً وشاملاً من القوات المسلحة الإيرانية الباسلة.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/77473" target="_blank">📅 00:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇮🇷
تعليق رحلات مطار الإمام الخميني بالعاصمة طهران حتى إشعار آخر.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/77472" target="_blank">📅 00:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77470">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">إعلام العدو : إغلاق المعابر إلى قطاع غزة بعد هجمات صاروخية من إيران على إسرائيل .</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/77470" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77467">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2261df5242.mp4?token=QYQ_qcekkoZnD0eo9TtmsUdhFNH7Qdh7oIoC0DL0mafE4RFp4ltKBvkfSwWhuJP4kX4sCw3BCVBMNjOXfoDxj-ab2Gkq44NboInebwpPLhmX7peFVAwA_kJNRGfBZ5TlLfF2N0EoREB6aahDgVjsl1E10M7NlYchvnFsSjEdLrcZHXheP289MQ5jmp300fAYq4JA9r46HjvK8lHXQLafwf2lfvl7HYncQ6zUhutLBUD8DE2Rcl65jHbxYDorQIfjcIxpdBa1bhUgcqUMToAVm_GpC6mFk6SupaAzMyi0pf9-zUsHBILgoSfRzWGxWYKkJU7OvGSWBvEPqg9gFfJvFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2261df5242.mp4?token=QYQ_qcekkoZnD0eo9TtmsUdhFNH7Qdh7oIoC0DL0mafE4RFp4ltKBvkfSwWhuJP4kX4sCw3BCVBMNjOXfoDxj-ab2Gkq44NboInebwpPLhmX7peFVAwA_kJNRGfBZ5TlLfF2N0EoREB6aahDgVjsl1E10M7NlYchvnFsSjEdLrcZHXheP289MQ5jmp300fAYq4JA9r46HjvK8lHXQLafwf2lfvl7HYncQ6zUhutLBUD8DE2Rcl65jHbxYDorQIfjcIxpdBa1bhUgcqUMToAVm_GpC6mFk6SupaAzMyi0pf9-zUsHBILgoSfRzWGxWYKkJU7OvGSWBvEPqg9gFfJvFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
لحظة إطلاق الصواريخ الإيرانية باتجاه الأراضي الفلسطينية المحتلة.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/77467" target="_blank">📅 00:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77466">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmkyqwY6zXiSgGWcOVpLWT35PmJjDeGCT1q6-jyCQbvLmTbSEkzFvrHyY53MyBwaBtAMNaI_YNkCEH6Y-PMdNhyXl5CikQ3BL3aIazNB7JtA2J1RyDNs2DfIN-1lTHb0a8wkDXjgaqwsMbFvt2EUrnDP98Q96rL2jYwtkQ6RWX8WbeNB3ej3ZcqPW7UAUz5W1ZBVJvrv1h-x4OtnSvyDYDezhj0S8ijbd-ymWm60tyhovBbQ3z3pZeLgg1aGh31n_JXwDpVGiAIbZvIVR9fFwVaIPaG0_5ioEQSmI-Mw04OqXKL_pSZOjiO_nQ9pDQM-DIQqz2oHDkNgG5AC9AEykA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
أصدرت السفارة الأمريكية في القدس توجيهات لجميع موظفي الحكومة الأمريكية وأفراد أسرهم في " إسرائيل " بالبقاء في منازلهم حتى إشعار آخر.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/77466" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77465">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b40b17597d.mp4?token=vtIB3bXP4G4TSHN22YiUUetMb20FCDG1WIdC1NHygdC3oCDquP8vMHsgOAl2ExhWSa_rturRGqUC0mkFO0ZlJJMaaSU6lqvDUeRPXWoI_ALNc9knL_teb6lGRKWKZpl3moxroN3UY0z7q4wIowgV-2jLm0ogI2mnUjKoHlrXFBDmx7lQjkk7mWESBgIo_8m6iy7XUv-ppoYRLxlLjyCFVKbWBeaZyfjX2gLUDPCwNLY1upLVvK4k96P9Q-CxEjNkcAyPw7q42DAWZohgr6mntf1pKV1CLBicEPQnU00S-Y64vsDIkQ744nc_DMtYxRNi7jshFvkMfW7LIP2nS5hagA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b40b17597d.mp4?token=vtIB3bXP4G4TSHN22YiUUetMb20FCDG1WIdC1NHygdC3oCDquP8vMHsgOAl2ExhWSa_rturRGqUC0mkFO0ZlJJMaaSU6lqvDUeRPXWoI_ALNc9knL_teb6lGRKWKZpl3moxroN3UY0z7q4wIowgV-2jLm0ogI2mnUjKoHlrXFBDmx7lQjkk7mWESBgIo_8m6iy7XUv-ppoYRLxlLjyCFVKbWBeaZyfjX2gLUDPCwNLY1upLVvK4k96P9Q-CxEjNkcAyPw7q42DAWZohgr6mntf1pKV1CLBicEPQnU00S-Y64vsDIkQ744nc_DMtYxRNi7jshFvkMfW7LIP2nS5hagA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇮🇷
رفع الأعلام الإيرانية في مدينة بعلبك اللبنانية
😆
يا حرام طيب ارفعوا صور عون</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/77465" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77464">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">إعلام إيراني: تفعيل تدريبي للدفاعات الجوية في سماء غرب العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/77464" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77463">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">على الأرجح الطائرة التي سقطت هي MQ1 او CH5 في صحراء كربلاء !!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/77463" target="_blank">📅 00:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77462">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بقايا الطائرة في صحراء كربلاء؛  هي من طراز MQ 1 أمريكية</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/77462" target="_blank">📅 00:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77461">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/77461" target="_blank">📅 00:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77460">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfoOJHqFy-ZQauXqdkOW2CDm_xPyLFt2IK1rAtMS3colmoUBvuhm7g_ERiT6pmUxcXLG5q0AHiWLsXeIkzkNhSEdHbWn0nkwgEfFNRW53aK9na1t8LHauoydovgd_KjXCSOOIICIFrMWcGlxoA7Ul8yBZPyAL3cbap1uElsdSS7u1oN6IrYsQMWfx1-9qReGipWt9a2NHAEvjWC7CQKmav3neN4msU2HQVwcWYfjAzCRnguOoCvypIimu3JWVV_hv7xwWWrXPb0IHibyUBDxdPirk6uJNEjrgNg9piAaRwKlvB4Id4LpJmtbKhyLflxtKmnsYJKBbpTWTysV3mRz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">على الأرجح الطائرة التي سقطت هي MQ1 او CH5 في صحراء كربلاء !!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/77460" target="_blank">📅 00:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77459">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJbj3inSydOiqQyYiCoUWyc4bx9TsHBx-wiqc9PAJmLgE0oujRGGv7pUBoSuYlziS5IZMeT80IgCZ6-wnmSitg6ilKu1qfbxn--zrkRkrDFCpymG65YajHpN_9u8r8yubNoZUz_iKdvSV9Pu3ZYPDDYfo4-2Ar9WcLo5bDGtmQr7XKflYVVSvInzst7_ykN9svf_lij_A9YRybWqToySQiZ4GPLntq6N0q80v73u7xtokAs27thHp-rTEgWH1X4QqcX3gsQPwM3Rrgi-jNWWQchBNHIT_V0sr_L1gURU_5qCvU7JyQssx6-B4UqPD0K-ymbOMLSY-C2wokjjbxOJsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الملكية الأردنية رحلاتنا مستمرة عدا للعراق وسوريا ولبنان</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/77459" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77458">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
مصدر عسكري إيراني:
صواريخ إيرانية جاهزة للإطلاق الفوري في حال رد إسرائيلي.
إن كمية مناسبة من الصواريخ الإيرانية جاهزة الآن للإطلاق الفوري على قائمة أوسع من الأهداف في الأراضي المحتلة في حال رد الكيان الصهيوني على إيران. إذا ردت إسرائيل، فستكون الجولة القادمة من إطلاق النار الإيراني أكثر كثافة. إيران مستعدة لخوض معركة واسعة النطاق إذا رد الصهاينة، وعلى الصهاينة أن يأخذوا هذا التحذير على محمل الجد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/77458" target="_blank">📅 00:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77457">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQokBPcRkb17McX3FXs5AsWNEMZaerNZpWnEAKe22WtDrQXJyfbleRlgMcp2OWpZmxjDmmgRhnCRzcstVr-OO87b0E43349Z62h21Ex2KIM5NiVA1jaZpc9CTtPjcexkKcQYN99T2_m-4rQRMDlCLUC65yvWEO6NCKyHSDnh_vIXOb5XiaLWVp5BF4GKSC4q8ZSXY9ilSdjyS9aypCASXnBrLXgTyCIFkWCZq9-1a1AV2lKAKJrn3LXmcdZrh-5gJX8lPiHeT4bMLQr6QedclxM4qUbl3zzEIzE-vNxgaVN5HXN8iXBTYedp7WhzrieHQB_pVSc1NMhx9oeqor427A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دايما حدكن
🇱🇧
🇮🇷</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/77457" target="_blank">📅 00:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77456">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/77456" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">😆
تسريب من مكالمة ترامب ونتن ياهو</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/77456" target="_blank">📅 00:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77455">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">الخطوط الجوية العراقية: تعليق جميع رحلاتنا المجدولة القادمة والمغادرة خلال مدة سريان قرار الغلق وسيتم إشعار المسافرين بأي تحديثات لإعادة استئناف الرحلات</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/77455" target="_blank">📅 00:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77454">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سقوط جسم مجهول في محافظة كربلاء</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/77454" target="_blank">📅 00:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77453">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سماع دوي انفجارات في تبريز</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/77453" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77452">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سقوط جسم مجهول في محافظة كربلاء</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/77452" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77451">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0004c676b.mp4?token=fravbDkL_mpYqz4OTiK8Ej-QSYjORaMfHrmRgZMShER_kKiI0cbNgMB4jdWi2HHeT_vwZPOcXhf31POCbuCoWc_ilFaprC9mbmXjWJ5oein0hrwrQrN2OGn89jQXz1KHnETPxNx56zeEkibmosDHLrVCcdruVjP4yO9vVbUeSvfqJOTOtP-sxeOEOSSKnOOZwkHNO7AL3LggFI6PsiMDjkTqKTX6FDuHgm7PeYUfItpQ5qNybCS2qgDBDAAfUHKcL6BQ1JBBv87DTJ5QM0g95Hkggzbth-GVwIshjorQCgFduIr0DSg6CBUohKyJvmik2B8ZJPPAWW_vXM7dM5Jz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0004c676b.mp4?token=fravbDkL_mpYqz4OTiK8Ej-QSYjORaMfHrmRgZMShER_kKiI0cbNgMB4jdWi2HHeT_vwZPOcXhf31POCbuCoWc_ilFaprC9mbmXjWJ5oein0hrwrQrN2OGn89jQXz1KHnETPxNx56zeEkibmosDHLrVCcdruVjP4yO9vVbUeSvfqJOTOtP-sxeOEOSSKnOOZwkHNO7AL3LggFI6PsiMDjkTqKTX6FDuHgm7PeYUfItpQ5qNybCS2qgDBDAAfUHKcL6BQ1JBBv87DTJ5QM0g95Hkggzbth-GVwIshjorQCgFduIr0DSg6CBUohKyJvmik2B8ZJPPAWW_vXM7dM5Jz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجزاء من صاروخ ايراني في محافظة درعا السورية</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/77451" target="_blank">📅 00:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77450">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cadd5da828.mp4?token=ePtE8sQKlKaI2qwQy5OnE23TMkB8W6J8gXi8sAwPreUmZl1Ul94kAk0oWvCtwj0dbt-DGbEaAPEi_mXLaVGQuv-ZbAD9boN722Owef3PMOtLaFd3UbN5ABFSoGk5rfIA6-mrCsKRxIh-aJva1EFdktiLt6fGy5I9Ax2fD5DSzlq-2WTc4GnsnJQIfSczqT8K-0Gt2eoCOhgZgEIb2laUjtIGD19IZig9buJ4NkQTnbkuoMZXzupoVW7Bw8mjrVbpyaMHgWdTgS1BTtLM2epVe1TtGaOBAppSp1JCBzVIthAzYQTx0i1z7UcwePKIhRhAH_yvdk-U9auh-TJXZNQvTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cadd5da828.mp4?token=ePtE8sQKlKaI2qwQy5OnE23TMkB8W6J8gXi8sAwPreUmZl1Ul94kAk0oWvCtwj0dbt-DGbEaAPEi_mXLaVGQuv-ZbAD9boN722Owef3PMOtLaFd3UbN5ABFSoGk5rfIA6-mrCsKRxIh-aJva1EFdktiLt6fGy5I9Ax2fD5DSzlq-2WTc4GnsnJQIfSczqT8K-0Gt2eoCOhgZgEIb2laUjtIGD19IZig9buJ4NkQTnbkuoMZXzupoVW7Bw8mjrVbpyaMHgWdTgS1BTtLM2epVe1TtGaOBAppSp1JCBzVIthAzYQTx0i1z7UcwePKIhRhAH_yvdk-U9auh-TJXZNQvTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه عبور موشک از آسمان ايران و فریاد شعار «وما رميت إذ رميت».</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/77450" target="_blank">📅 00:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgYpN4b3Shq_ojlMjKU0R9l-RUDs8fxZxH2PytCEmCKptYSB8pj-BCfpNmviDHJeJSk4bSI3nx32aUGxNiYLx3HcWvThDuBa9h4WU9oYn_gZEFUbtkLC_FI2x8owD15OEYDuziioZGyGo0QqdNmzqyBegi5fJCGTVSlpOW5D20RinkqOGXBnUr_HNhfAjolUp3OAiSxAL6d4vF2O9Tmo6NU9qtdk3VOgcaqazzrK4YyE-wzPsfXsddZl5qA7118lYFa5Malb6NXje_Vfk3aZZuRpMzmHfJf7CjOcOKg1CPVb1lF3sxDZZ-7LjNPz4N7rb4JCw5F3z3LcLQp449FJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
المعاون العسكري للمقاومة الإسلامية حركة النجباء مغرداً</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/77449" target="_blank">📅 00:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">إعلام العدو : من المتوقع أن يتحدث نتنياهو مع ترامب خلال الدقائق القادمة.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/77448" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">أجرى وزير الخارجية الإيراني اتصالات هاتفية مع نظرائه البريطانيين والأتراك ورئيس أركان الجيش الباكستاني لمناقشة التطورات الإقليمية في أعقاب رد إيران على انتهاكات إسرائيل لوقف إطلاق النار في لبنان.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/naya_foriraq/77447" target="_blank">📅 00:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">القوات الامنية في العراق تعلن إنذار جديد قرب مقتربات المنطقة الخضراء ومطار بغداد</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/naya_foriraq/77446" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وزير الخارجية الإيراني: أجريت اتصالين هاتفيين منفصلين مع نظيري التركي وقائد الجيش الباكستاني</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/naya_foriraq/77445" target="_blank">📅 23:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77444">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سماع دوي انفجارات في تبريز</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/naya_foriraq/77444" target="_blank">📅 23:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77443">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71e274350.mp4?token=MuMSDY225z-Wl8S92xtm-OePp-7Rcy4b7jPZsL1v_A42sDDbd5V_NEe6ULJfY4MnBvK6gY1fmJVeRRdehDDoSnI3AkRuB1iMzh0vQctmR-2litKJQbAYA4TwkigcF8EA6QRER9zDshrv9LgqZjvrC628EuO2FZa9vYS-eC_s2bTdUezzqFXghe0NtThfM29L1EzYCdLoSZLXTZnaNQYRj27UpPThdnLtzf4UTGTaJRVCFu3a0lwZbOwDp0jcOF0j3DcPX5e_N21HDdSyLC12CO2QWj_pVD_RbkJkpKIr-H_WUOaLB34uJb7iV5b_WzBZtMNxBdSB-4_lz3Jm68As9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71e274350.mp4?token=MuMSDY225z-Wl8S92xtm-OePp-7Rcy4b7jPZsL1v_A42sDDbd5V_NEe6ULJfY4MnBvK6gY1fmJVeRRdehDDoSnI3AkRuB1iMzh0vQctmR-2litKJQbAYA4TwkigcF8EA6QRER9zDshrv9LgqZjvrC628EuO2FZa9vYS-eC_s2bTdUezzqFXghe0NtThfM29L1EzYCdLoSZLXTZnaNQYRj27UpPThdnLtzf4UTGTaJRVCFu3a0lwZbOwDp0jcOF0j3DcPX5e_N21HDdSyLC12CO2QWj_pVD_RbkJkpKIr-H_WUOaLB34uJb7iV5b_WzBZtMNxBdSB-4_lz3Jm68As9oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد توضح سقوط بقايا صاروخ في صحراء كربلاء الامر الذي روجته بعض المنصات الموالية للولايات المتحدة والكيان والخليج على انه سقوط طائرة مسافرين في الصحراء</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/naya_foriraq/77443" target="_blank">📅 23:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77442">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZHhHu-5-iMc0nOIG9pp86AlSJH12bC-Y831xVLM1fG1iyaruBpbZj4IA5jIx0lIhmz93jAh1yfUsfUOS7h_o9aFlym9VIMNnhrf1KVWZCdZ_HKhx67podbXfA6wCwJZb5F5zsbc5vvoAzFkPgkAgvNHndnJM3ocIR4P0adWVNWIRfEoutGSeAwF-bfxKDsB7pgfBclBObsljTw4SlfVKEappBkeMDgyZbmecGfLOmGttGzI_jREDE3bi9XoUNrOR7GeSafT4SWi4weKr7mP6_Uk6kavR8kUXNxuF9c_Ai8kX_K5gtj3mUB3wXpXkVLYY4yDLMSrWnq2koZjdl22JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عنوان الليلة ..</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/77442" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77441">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/naya_foriraq/77441" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77440">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سوريا تغلق مطار دمشق</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/77440" target="_blank">📅 23:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77439">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">إعلام العدو : في "إسرائيل"، تم اتخاذ القرار: سيبقى المجال الجوي مفتوحاً وستستمر الرحلات الجوية كالمعتاد في هذه المرحلة.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/77439" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77438">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0005d30c3.mp4?token=KkN8rVirh04RM_tUP49EEwiOoqwlfm0bZ4pRjiBhEzTJ2L2R-YmpssPtHPr2bSZWWgoa5VTPPysWy7i3rZ2c2kKfGmFi2ZS852yogabv672VXVsVLCznnVNCfxgdV1YjOTHph-2zjJvfS2cValrcq3wz5JD8M6-ZKl61JSeTOdm6L_wJhkTL8OKqWSJ6Dzys2LHlEGWeFG4g1xE72DiXcnMOeT6-ShKAtNASyMbUAcW075wIRBCNdR6c5FjjUOiYrETYM9MYlEOS1uyws4I8DpQkzGQ68nBu5TBMAOqtBiHOktP0sUC5aMS9kmZxwP-nTdFLRkmDpnJxRmEzgG_1wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0005d30c3.mp4?token=KkN8rVirh04RM_tUP49EEwiOoqwlfm0bZ4pRjiBhEzTJ2L2R-YmpssPtHPr2bSZWWgoa5VTPPysWy7i3rZ2c2kKfGmFi2ZS852yogabv672VXVsVLCznnVNCfxgdV1YjOTHph-2zjJvfS2cValrcq3wz5JD8M6-ZKl61JSeTOdm6L_wJhkTL8OKqWSJ6Dzys2LHlEGWeFG4g1xE72DiXcnMOeT6-ShKAtNASyMbUAcW075wIRBCNdR6c5FjjUOiYrETYM9MYlEOS1uyws4I8DpQkzGQ68nBu5TBMAOqtBiHOktP0sUC5aMS9kmZxwP-nTdFLRkmDpnJxRmEzgG_1wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد توضح سقوط بقايا صاروخ في صحراء كربلاء الامر الذي روجته بعض المنصات الموالية للولايات المتحدة والكيان والخليج على انه سقوط طائرة مسافرين في الصحراء</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/naya_foriraq/77438" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77437">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قال مصدر إيراني رفيع المستوى لوكالة رويترز إن جميع القواعد الأمريكية في المنطقة ستعتبر أهدافاً مشروعة إذا هاجمت إسرائيل إيران.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/77437" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">المتحدث باسم المقر المركزي لخاتم الأنبياء: يجب على الجيش الصهيوني وقف هجماته على جنوب لبنان وضواحيها.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/naya_foriraq/77436" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77435">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">إعلام العدو : تستعد وزارة الصحة لنقل جميع المستشفيات إلى مناطق محمية ومجمعات تحت الأرض.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/naya_foriraq/77435" target="_blank">📅 23:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77434">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏ترامب: سأتصل بـ(نتنياهو) وأقول له بألا يرد على إيران.
‏ قريبون من الاتفاق مع إيران ولا أريد التشويش الآن على المفاوضات</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/naya_foriraq/77434" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77433">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بنكين ريكاني رئيس سلطة الطيران المدني العراقي :  لا صحة لاي انباء تتحدث عن سقوط طائرة مدنية في العراق .</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/naya_foriraq/77433" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامب لـ"فوكس نيوز": لست سعيدا بالضربة الإسرائيلية لبيروت اليوم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/naya_foriraq/77432" target="_blank">📅 23:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh_IB67TA4WKPydER6N69emdT4IGH_5b0ncgqpOYYBFKuDzhpWLUWo_hA4Wj3bFO5pLWXk4YwWxuvgVW7cDsa7R4hR99EjTpYEws5ERViwEV_tt_DS31mgoAykcmVqapAwputX-CyEZBNv7yJcrDki6IQVuKqAbh30oEdwm86Bd4_SfgTi-GcGULGNK7k_kilOYBXrY4yHw0nbCpcbBWGXlhxcmgsA67TaQSqv7mMJ3EwMRqY--i8LyyjqrBT1hQaYrkWajc6EuyD9pK4z2f3POyvq2B3IoTGiD-apnzN_t_eZNO2kNKAEASQ0zkL9iu1N_BPMQKKsY_8y6S8qfRcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب قائد الثورة الإسلامية ينشر: أنفاس النظام الصهيوني المهتز باتت معدودة.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/naya_foriraq/77431" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77430">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">إعلام العدو : اصابة موكدة لامرأة نتيجة الصواريخ الإيرانية التي دكت سماء شمال فلسطين المحتلة …</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/naya_foriraq/77430" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سلطة الطيران المدني في العراق: إغلاق الأجواء العراقية لمدة 72 ساعة</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/77429" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812f395cfe.mp4?token=qJ6Zs1OBNoU5FW_dLZR6O7BRQoeVcG8oHweqZjhwfQEtTmKGmHTdWz44bUm53iVZTHjN223MKUsiwV3BfSzjYRPJDMpRFz9wNnaUR5G4XMtIlfgF_wZ8YhYjSXfTcNpOv-cST7F_59I1WbMrmoWl_4vONu42M56fbbnTn8SDeUYVGd4Sw-PRuBYtGjrHXn6yTBJjkBK49wTD5AB2fsQ48jrGFOEnsq3GMZbtSoaQpDFhQCK6h6QxpQSzybVnAxC0e65D0EEA55IBKJ4vIGpHE2oVrRQeXhPn-3iI1w1wIpRa7PdGeGD3fp3dseq0qAqNPUmd8GDB_ksmzdUL81xg8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812f395cfe.mp4?token=qJ6Zs1OBNoU5FW_dLZR6O7BRQoeVcG8oHweqZjhwfQEtTmKGmHTdWz44bUm53iVZTHjN223MKUsiwV3BfSzjYRPJDMpRFz9wNnaUR5G4XMtIlfgF_wZ8YhYjSXfTcNpOv-cST7F_59I1WbMrmoWl_4vONu42M56fbbnTn8SDeUYVGd4Sw-PRuBYtGjrHXn6yTBJjkBK49wTD5AB2fsQ48jrGFOEnsq3GMZbtSoaQpDFhQCK6h6QxpQSzybVnAxC0e65D0EEA55IBKJ4vIGpHE2oVrRQeXhPn-3iI1w1wIpRa7PdGeGD3fp3dseq0qAqNPUmd8GDB_ksmzdUL81xg8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر   اصابة مباشرة في شمال فلسطين المحتلة</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/naya_foriraq/77428" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77427">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/77427" target="_blank">📅 23:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77426">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHZYDHA4nM8JWqYlaeBRku-zIyj6pyulSJTrr-aR9fv8rJJgUbiBDJQEeGcOrEKAnVusfAjUn-HIVpyDj14xHVm5W0G6owDQS8U39gF5neSThMk5mcQ2SjxBLpgWTUFO8lTPjMcxnnxxQfbrPZPJG7J-lI1YXCgwV9FomwcTInLGfv0nejQLTX0vfpXgm56TH_KEzyJN0VG1GmEcY4S4yHCIUNNohawYP1EAffBtNwa3lzp8ztUHC1MPkEAKP1tJNLiBxATMEUzxM-VJwhIEWXIDeHobgYC-Yh3Ys_Z21EI75CTV4lkmgqNm2cthA-zwgfd0cI0teYhPQGE4Jyan7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف تام لحركة الطيران المدني في سماء العراق وايران …</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/naya_foriraq/77426" target="_blank">📅 23:31 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
