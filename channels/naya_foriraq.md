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
<img src="https://cdn4.telesco.pe/file/hHN-KtnS6JNJw2NUUrZ-gGJkC4e1i0Lmz9pRJ2gFWdOLek1_ZHF0fb2dBgzcs0tbm0pynx0KA8eua1W_7LmRQFSN1NIHwWzCqkdaCh2f16ryn-3BoNfbuS9gxK6B74zY9-yPDjTh4YWARBm0VqE8bkGiJvLjO3mPmz0a4Cg63Ys8gA-FdZP5KHi01Uk2q08J4kR4gOSKa7OTB4TZ9Eq3ZyQUNK-3OZpsOs9BfZDtx1Wk-70hU9pQoYVRvuoZdTcWYmoW7z9_HAJulV49y0HiRzzSjv36EDf84S2fQP8NG_xF0u3pUraZwG4k96RpLGjz3lC9ReFI2HhbmioUCc_WXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 20:21:39</div>
<hr>

<div class="tg-post" id="msg-84460">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏
الأمم المتحدة:
تهديدات انصار الله باستهداف الملاحة البحرية قد تؤدي لتصعيد إقليمي أكبر.</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/naya_foriraq/84460" target="_blank">📅 20:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84459">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
مصدر أمني لنايا  تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/naya_foriraq/84459" target="_blank">📅 20:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84458">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP1RyQvC15ICrs0IoI6sZnFFzr-6rCoA6Ypf8UAIDhddJUS_UhCb-PF-DY4PtQXx8nHnU3OUg3p9nx7L5BsWMYK-CqSA-HZNIUTwL9Zod89snQYId9rYAnBvtt88kB3sLQlBjxgWQ8Ei0Fu1Dv1IryHONtAJUaV2dS2s2pxMYGSOxsQgI3DbjItFjD326I6vaUbIqHmjgGf_TEqzLGCPDTaX4kMpMddUypbjRloHf9u4QGSNf6ZsMR1kmUGgzf584g5ag3vqxY7U8DRwyIxNVrtvXmOyWI1_j4EnMI3pV8Ryt51PxIefldA_NIndNpD58eWUBlxDvh0gXF6rQ5Ky_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كون العوز يفشل
ترامب كلما قتلت ايران جندي امريكا سوف يزداد دفعها الثمن .</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/naya_foriraq/84458" target="_blank">📅 20:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84457">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/994d799481.mp4?token=pHDqdcBNdlglpirU5-pHnlyGEabzKQd2qTxY69YgOmq-LXPH3889D-8aMABnkNgR2JA2DR6zQlaewpb2WMWPGRY9S2JraQEFuyPUMuGOePv9NbJNFV9RKexCMtlPb0nWbyOAhvEYm6Jg2ebB2bflD7884dsqYyZBNcitLjeJwBpEiF5_K7xmvvty4XXTMsp_wawKU3LHXK1BK6TxpJMev20ktPiT6jx8gJu_nOFP34w52MtBNkA4FdYwyBtzoXiftpzjUwk4XLdbozmmzi1Jrwv4N87RPFS_RkCBZVt_-8qDw_Kf0WvF-UqKrC60Py6kwObXXk9SzpCHTd0xjt_JXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/994d799481.mp4?token=pHDqdcBNdlglpirU5-pHnlyGEabzKQd2qTxY69YgOmq-LXPH3889D-8aMABnkNgR2JA2DR6zQlaewpb2WMWPGRY9S2JraQEFuyPUMuGOePv9NbJNFV9RKexCMtlPb0nWbyOAhvEYm6Jg2ebB2bflD7884dsqYyZBNcitLjeJwBpEiF5_K7xmvvty4XXTMsp_wawKU3LHXK1BK6TxpJMev20ktPiT6jx8gJu_nOFP34w52MtBNkA4FdYwyBtzoXiftpzjUwk4XLdbozmmzi1Jrwv4N87RPFS_RkCBZVt_-8qDw_Kf0WvF-UqKrC60Py6kwObXXk9SzpCHTd0xjt_JXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر أمني لنايا  تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/naya_foriraq/84457" target="_blank">📅 20:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84456">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
مصدر أمني لنايا
تحشدات عسكرية إيرانية برية بالقرب من الحدود مع الكويت ، يرجح ان تقوم القوات المسلحة الإيرانية بالساعات المقبلة عملية برية أمنية باتجاه الكويت.</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/naya_foriraq/84456" target="_blank">📅 20:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84455">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IatWxGBkmFGKjcQ3fX0jvGtBh4e2aDG5R-uZQtD7zTO5EQQVw10852SUMvJkFdKriMrLMArvthf9nDe8p8nJsqjB_psfkeSoIMskLkRK6iJBChluYUdHRH37QSiy4S6teNUiw_iDrNr8SpEjgSUD5uy0p8TOUchsvXvggkXrPA5SM4KDj8U1G37fFud6CQ0IbhNODJIOe4OS3kenbVgc0-ZpEylC3iEdr675QYe0avCIyJMDIV9hPCJLon9HQ584wrKHunik1Mdifk2QmjMNwmJI7Gawbkm327BIFUYG4MQenO7Uo0puaDxH7JkDR1C7k8mhIB7onopr6WAKEKKspQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
هيئة البحرية:
بلاغ عن واقعة على بعد 17 ميلا بحريا شرق دبا في الإمارت</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/naya_foriraq/84455" target="_blank">📅 20:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84454">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veGh7O8jN7_eUiqiGrLVg1BWi35FTaOl53wNQIHuj1NlXpsaYpDSUdBqS41Y2gN8IDJDEFIxt3frGCr9zVY3uhAyYK4kGf9ihklBvX5SevNgi-i7qzMegqjPJF8Y-tDwhzzMh0kqFFNg2HIL1b9hdgM70uuAjHpCWJAyLMEjTkMAJz1qwg7BWhHvdp33y5yb_imJsLBZRaOzhytFJtodoUZe-FWi7l8Jmys0uNhEGoghVPKBywDXKIck6pwAPBkuUiMNVVnA6_ZzUxSZ0X4A-QCmZvogsbJ1imhSzpJbXIfxPHjPPpR2KG78sWa6o3HrjAXtwX4_gtJqDpgwx1D0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏القيادة المركزية الاميركية: قُتل جنديان أمريكيان في الأردن أثناء تصدي القيادة المركزية الأمريكية والقوات الشريكة لهجمات إيرانية بالصواريخ الباليستية والطائرات المسيّرة. كما لا يزال جندي آخر في عداد المفقودين.  ‏تم إجلاء أربعة عسكريين أمريكيين طبياً إلى…</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/84454" target="_blank">📅 19:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84453">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3cc01cd85.mp4?token=Nn4o2Df4aooaBpg23CNYGP0qQmdNPhOYFP9T-AaPMmpij_uvjM3CjAFCnXbEQlopC-URsaUA311C7cwtDMDhRCGMGsORbeoxsj0mGbwIsRxJqy42B81D-RG6MWqe77-ldSnJjggYa6JBS5zAnfSJsVohIjseytO0QijgZQP29gEXKGa15UHIlRCDvx-UAEBRGTI3_tLs4yRltR7brdEK3CLSplkMu84OTps4nhC25H9HUfNrH-xc8A_iaViJNs1ao-IuhKaPOOwddGewQbC98pU5PxgBAXhLoXWftGYMYdc8ML98UJcxhe2OY2C4uQZT7MSRF0U8shvzBEKj7dg8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3cc01cd85.mp4?token=Nn4o2Df4aooaBpg23CNYGP0qQmdNPhOYFP9T-AaPMmpij_uvjM3CjAFCnXbEQlopC-URsaUA311C7cwtDMDhRCGMGsORbeoxsj0mGbwIsRxJqy42B81D-RG6MWqe77-ldSnJjggYa6JBS5zAnfSJsVohIjseytO0QijgZQP29gEXKGa15UHIlRCDvx-UAEBRGTI3_tLs4yRltR7brdEK3CLSplkMu84OTps4nhC25H9HUfNrH-xc8A_iaViJNs1ao-IuhKaPOOwddGewQbC98pU5PxgBAXhLoXWftGYMYdc8ML98UJcxhe2OY2C4uQZT7MSRF0U8shvzBEKj7dg8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صواريخ فتاح ١١٠ البالستية يتبختر في سماء خليج فارس</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/84453" target="_blank">📅 19:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84452">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1bbZxmrS1WZRduLt8TQVdazzqnUBWSP7rL3vuj8ITtvk9OSQIKxoWoBmZN0eLgPdEfOiY7vXMDZxuaSLG4_L-foNJCDlRvQYM6uK_cKXC9siA0oQDeiSxWoUyNVpwNgDL13bnO9-EaIs19lePZ5FnSu5OjZ1t71HC3gb2VA5vqZ6WvUzS1tzWsMHO7GAL0VrmNZxb6Iah3ICAICSZOk8ryPMWVP7HsBr5BPoXigSkEDOC6keRnjKEl_4EsWbYC9sFjTE7MycO4jc-J3wRnCWfgYljLBe8Z5ratDXAbwNzOHnxbtxJGcZVfneC55n8c-mO49lQ2ZPCGcpUod0X1T4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجة صاروخية إيرانية اتجاه القواعد الأميركية في غرب اسيا</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/84452" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84451">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/84451" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">واحد معطب السرفة و واحد معطب الهمر
#شاركها</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/84451" target="_blank">📅 19:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84450">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a526d078.mp4?token=g9RmrZSZzMN5km6LhAExW8ojAmhiAxoKEUW3DEcPHSq0Y8LiLSE-COAIGHwFjCJ5EwmvHawvMX67EBS877A_oujLGkmbfv3cUaj3UlSIJ9JqDwXKHvv6ogK6AcjxIkE9LISTU1ZqCoh1puD6F4rmzmJqRR2Qmjd3qRKK7lRafe_E-gc8wqGIic50zvbt-z4rtBrsVfpeUMK0lu3vu1bGR6bkOW8JLAe3O2HVYnANtnD4HYCNp7SOQX62iNqdJwnClqChMqFbwNHWMKYkiSkBvLbV-LTDSDvb5G-NZTmlp3HCY41GtcHuCwyvArciPsXqfuLOhdhHcu_RvezPjmkbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a526d078.mp4?token=g9RmrZSZzMN5km6LhAExW8ojAmhiAxoKEUW3DEcPHSq0Y8LiLSE-COAIGHwFjCJ5EwmvHawvMX67EBS877A_oujLGkmbfv3cUaj3UlSIJ9JqDwXKHvv6ogK6AcjxIkE9LISTU1ZqCoh1puD6F4rmzmJqRR2Qmjd3qRKK7lRafe_E-gc8wqGIic50zvbt-z4rtBrsVfpeUMK0lu3vu1bGR6bkOW8JLAe3O2HVYnANtnD4HYCNp7SOQX62iNqdJwnClqChMqFbwNHWMKYkiSkBvLbV-LTDSDvb5G-NZTmlp3HCY41GtcHuCwyvArciPsXqfuLOhdhHcu_RvezPjmkbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية إيرانية اتجاه القواعد الأميركية في غرب اسيا</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/84450" target="_blank">📅 19:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84449">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رشقة صاروخية من ايران باتجاه البحرين الان</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/84449" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84448">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتيجة الهجمات الإيرانية ؛ شركة شيفرون الأمريكية تعلن إيقاف إنتاج النفط في منصة بترونيوس.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/84448" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84447">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/84447" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84446">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/84446" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/naya_foriraq/84446" target="_blank">📅 18:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84445">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3d0d6c4d.mp4?token=sg4aQLmqWlPzoXr43DqVfJWB4eq9wO_aGB-Alf-lXorYaoOUwuncUCGV-GvADQaBkS8Rj_Fdk-WXBmaPJ5CFt96kBoh1A5UIZyLbW2HyL4MRfc6PTLC9y_gwS-UEF1n2VlzPTDLihiwefmO9j2NZVOQzEKqaGLScbuabDxHmrf4cb2MtjeBSmzMnndqI0lDGh0WHQHvAfYa6cdLWXGCjidgt4F4ZrsUG3G6UdFEiVoJNhkNQUDOvNBMuE4JdO1p3DZ7ytsGF7HZubeIx_SF8UaoIEaOn9JCkzVv51Pvjdk31u9ge_zAvJNSxYyBzwDRo6HgXcd9Wk9OdnUgLTBZPIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3d0d6c4d.mp4?token=sg4aQLmqWlPzoXr43DqVfJWB4eq9wO_aGB-Alf-lXorYaoOUwuncUCGV-GvADQaBkS8Rj_Fdk-WXBmaPJ5CFt96kBoh1A5UIZyLbW2HyL4MRfc6PTLC9y_gwS-UEF1n2VlzPTDLihiwefmO9j2NZVOQzEKqaGLScbuabDxHmrf4cb2MtjeBSmzMnndqI0lDGh0WHQHvAfYa6cdLWXGCjidgt4F4ZrsUG3G6UdFEiVoJNhkNQUDOvNBMuE4JdO1p3DZ7ytsGF7HZubeIx_SF8UaoIEaOn9JCkzVv51Pvjdk31u9ge_zAvJNSxYyBzwDRo6HgXcd9Wk9OdnUgLTBZPIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
أنصار الله في اليمن تتصل الآن بالسفن المتجهة إلى السعودية عبر راديو VHF، وتطلب منها العودة في إطار سعيها لفرض الحصار المعلن، وتحذر من إمكانية اتخاذ إجراء عسكري في حال تجاهل أوامرها.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/84445" target="_blank">📅 18:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84444">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇷
🔵
أفاد وزير الخارجية الفرنسي بارو أن اثنين من مسؤولي السفارة تعرضا لترهيب خطير من قبل أجهزة الأمن الإيرانية يوم الأحد.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/84444" target="_blank">📅 18:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84443">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0y7K4K0S_2hxFmUDHNQFYhzpPv8kAhEt9HqIky38sFJTTCdCXmamQ39Vn7tn7-CZkvMhobl6fjnIZ-BVS7Ka8iSWVaJCxPA-2owBx-2YEEZejoOxcKdPgEo7w1bWcn4NZak6vkddFGNSxmxZOWBp5H5zRkpgRjyqn7elEeAwJz4jKU9b_haEr6eJjHHxO5h_p_GHQsRzPmMTGoRx8QFM9FqxRcpOYgm2S3fKSfVUv_adh5bz9Qbc-gT177Na0CZ0R1PeWCyYY42QnMu6jccFzBi6d-Ea-VsUKzW-XMfCUKb4h2L6-DDMwLMTep3obWvHlxNe3eN-beojh4AtAnrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇭
استمرار الانفجارات في قاعدة اسطول الخامس بالبحرين</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/84443" target="_blank">📅 18:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84442">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2AA6ergXaNZGbyB4x1W4nEYeP8PRVvdbJLrAYMtTr3k5ceAEJzPQnZg6ueL5Fa9ATB_slEoGNe_t6Fcja6kUffY9BHqR1hOLaPGlBcaqc3z7Njj8bIOuhgt9KnXTpwaRv5uMBM7NarHk3pfe8xLgJAnvpibxDNpBGF6jvAHn_UTxkPD2qe65b5pwfxT7aBdvcCBY0uuQCbNQWqp5PAabdq9q8Q8Mu3Urx202vr1N8qGaHHbTLuoK31jBByLjTX2Sz6c5NwGhrDJEp2HIJK06Z2nvD7DwZwz7F6_CeU-2Z4qSibCxRGNCnUov1OEOj4P67rKauXqAGHbJ5ryLr4gYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
🔻
This could happen when you choice wrong president that he work for Israel not for America
Tyler James Feehan another solider in US army who die in Jorden due to IRGC missiles before 2 days</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/84442" target="_blank">📅 18:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84441">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/252853cc5a.mp4?token=PmZ1RRxhrtOXkRl00HAuQ7Up_8DQmndZ54cT0jekzTWn6sC1OeqBxqvc_J1GZ9h5HhgfTSst5gAQs0mkviy_NBAirC_rN3RE3muU1NatMNFw-Bz5uMX0JYw3p43B8opABCxzEILrqzla3o89etVKLZxAfjo_P1yhASgkHbxd-eIYUpNr9uG3x-rlB5lLSojLnkIjBS1fHotzcrCx5_QuPc7rDKF86K7b-nHyQ75av-Y84MRQjTfi92JCCC64NPcy-1I-vlE55moew5S_xD9Oj9ihc7j6TAXYP_rfHpq0RsMz3lkCiT5BqPmjUGenSEAqt-kyo6mdASrlycJb7VcE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/252853cc5a.mp4?token=PmZ1RRxhrtOXkRl00HAuQ7Up_8DQmndZ54cT0jekzTWn6sC1OeqBxqvc_J1GZ9h5HhgfTSst5gAQs0mkviy_NBAirC_rN3RE3muU1NatMNFw-Bz5uMX0JYw3p43B8opABCxzEILrqzla3o89etVKLZxAfjo_P1yhASgkHbxd-eIYUpNr9uG3x-rlB5lLSojLnkIjBS1fHotzcrCx5_QuPc7rDKF86K7b-nHyQ75av-Y84MRQjTfi92JCCC64NPcy-1I-vlE55moew5S_xD9Oj9ihc7j6TAXYP_rfHpq0RsMz3lkCiT5BqPmjUGenSEAqt-kyo6mdASrlycJb7VcE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد بالأقمار الصناعية تُظهر تدمير أربع حضائر بشكل كامل جراء استهدافها بطائرة مسيّرة من طراز شاهد 136 في قاعدة موفق السلطي بالأردن.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/84441" target="_blank">📅 18:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84440">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5aec97ad.mp4?token=HJ_KVnftmdB2xnJl4CXs1cyAfu3wOeYX8iImJQA0zXVsQN3XG7nO6gjqR7ZU8LzN5kgwpRJLVaRbhVDTbzNrx9e3kDSLt6kYnSgT41qFrOk8dsBm9RqPPgz_uYneCrR2Vaq9j9BEFP-cqL0qiyZ7PytmRnnoIe_FuohW4q9tN4s1hEGrF_u4YhNBB0DlbzRg68vKiQim9sbMaoGEkrLDLE944IxHuKMPkCIpYqq-9-fv-qiT2tYWFz1F7AjAVjoRo9us8KYMJfcgNugPs-aCxW7VwaicduzdMoSuguO0mEDXh_rHDmEbxm-10aF-v7WB9LkVGHIMmQ2boRnDzFy4KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5aec97ad.mp4?token=HJ_KVnftmdB2xnJl4CXs1cyAfu3wOeYX8iImJQA0zXVsQN3XG7nO6gjqR7ZU8LzN5kgwpRJLVaRbhVDTbzNrx9e3kDSLt6kYnSgT41qFrOk8dsBm9RqPPgz_uYneCrR2Vaq9j9BEFP-cqL0qiyZ7PytmRnnoIe_FuohW4q9tN4s1hEGrF_u4YhNBB0DlbzRg68vKiQim9sbMaoGEkrLDLE944IxHuKMPkCIpYqq-9-fv-qiT2tYWFz1F7AjAVjoRo9us8KYMJfcgNugPs-aCxW7VwaicduzdMoSuguO0mEDXh_rHDmEbxm-10aF-v7WB9LkVGHIMmQ2boRnDzFy4KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
الانفجارات مستمرة في قاعدة الاسطول الخامس الاميركي بدولة البحرين.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/84440" target="_blank">📅 18:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84438">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7ed8l_z4Y6YdFXvrS6aDZuiouxrxmhdI1cG7llz8ZIaUOBv7xsxqm4V-kBuICmqIttPBHjrIkHfifpo98OV7iGrrVSadb3ykn1Uxw4i00K_Ru6Gzjgdskxfq90cmQ1-MGAkEwv03aUlfDoRYgGz4OzumVF77lnR-bxPGBs4t6OlNwxZpGMJvSEgpP_FMDgCjp42ibrorf3OSF-TKzu7-LdMLkbKT92M2SJquWAPlhsvMGhmhnEgSZHGacRxfixoCmROLEt0kOBZ5G83cFCx6INBoCIO17VDyQfMj52OBRgC-cticuKzoB6qN4992Bb7BvpZX73KTOm0y9plblRkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qq4ynD_4Cr3xnuo0pRDwugTIVFmuCSKEj26LuL5UC3cmmRa6FmmQq-py9uHitWnpQF1haXSmxC1I6yaC7oZk-PX0xc6JhdpUCH-kxgM8EbH-vxd9eqbLtnsTSiGnG1tIeRNzHwW4M3Ttai5FfibKifpP9UbgA_8KiEdN3TMQP8LAeqOyO7x-Mbw5TyokDSSa2uAqiQO_2bjOtx-kyUGuVI9VTw6HjM00BvMW1AoLURB7wmJSqOdGCP1Ct9YVUkBYynrGG7RW15YE04D-Uw3_4QmgBAnyRsjaWzUqf37uY9UUZtj0so88DJ1AozcUaZLBGOZrwhK-qK6VJW3TEP1fBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇭
استمرار اطلاق الدفاعات الجوية تجاه الصواريخ الايرانية في البحرين</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/84438" target="_blank">📅 18:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84436">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d83612b8.mp4?token=WOC5_OHtkG1NMXjQjyVRRhZ6XPIfmo_weKcMaMuLK6irqR5BeBBgmV_O2OghMEe06pIBlay2hLafATfDJWeK4ivfleMSX3g10idl8t1BYTjZBFF7pnxpYip_SbAltObBw2Kr8Qf7VNh09af_anY-fqdOt5CaN5Zh5bEiNu0i8Ni0CyjnW7gZbSwUTcsbL4C8bZucq7b9wq3FAavrfYbHPw30Nr-F3dRXVn2sjWNyZkFl8ivZSpFSuBmvzVf81TGMChVNFp228b76nE-gj3o4i1O3KMciG9-XGE4x2cvRBwqJOWUkXTtlGOwI7QEpif8SBKUXp1UexP5LSOVI5GsSRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d83612b8.mp4?token=WOC5_OHtkG1NMXjQjyVRRhZ6XPIfmo_weKcMaMuLK6irqR5BeBBgmV_O2OghMEe06pIBlay2hLafATfDJWeK4ivfleMSX3g10idl8t1BYTjZBFF7pnxpYip_SbAltObBw2Kr8Qf7VNh09af_anY-fqdOt5CaN5Zh5bEiNu0i8Ni0CyjnW7gZbSwUTcsbL4C8bZucq7b9wq3FAavrfYbHPw30Nr-F3dRXVn2sjWNyZkFl8ivZSpFSuBmvzVf81TGMChVNFp228b76nE-gj3o4i1O3KMciG9-XGE4x2cvRBwqJOWUkXTtlGOwI7QEpif8SBKUXp1UexP5LSOVI5GsSRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
معارك جوية بين صواريخ الايرانية وصواريخ الدفاعات الجوية الاميركية في البحرين</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/84436" target="_blank">📅 18:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84435">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT_7i6iZEtKKncdJHzTx4KHZAdg9AP5POnYw1hkhqF9Vx_5IB5eqk2sIKmu70FgDj1tvjUeOaYnFrzpGC5rE8boGANtHPlCeESagGNC9ISmSLLU0XkxiEYDeuH4RV5OzFqESXpkVnWEpNaIsdx1T-5zw1XATxsMjdg7QT8xB91y1rBTtn4ShjQ9-m30NZ0552Op3a0vRJknZEffr33NiYEl9X16Vaj4CY1z5sHS9L0zI75uSv4LwD7lI9cMdID_ZN8SuNG0UjrYalq2QD2KkIke7MD9CCInd50wBHZI1Efa6XLZ1kDHujXmhkASt_6RR7n9DQFYaggxWe3edX9ekOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل منظومة الباتريوت الامريكية في مقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/84435" target="_blank">📅 18:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84434">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">📰
‏
أكسيوس:
انسحاب الجيش الإسرائيلي من "المناطق التجريبية" في جنوب لبنان سيبدأ غدا الثلاثاء.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/84434" target="_blank">📅 18:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84433">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/84433" target="_blank">📅 18:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84432">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/84432" target="_blank">📅 18:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84431">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/84431" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84429">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vS9jT1pn0Ikrz3NCnY6flALx7SH6oeySRjlXsknkd-Cd_vEkdDVVAO-usj7OuaCLPEix3K_m0PSqBpGqxUV9ijyuvj6XjNYWSOQ95nYsXcEKUndZw-ImK12qpKBNIX50Ib2iAotCV1E7EFb_bIhhEkBing1YCt2j07UGDZCRTS8dD9F6CXciv46iC7xBqfbutzvzkIWbdBDZ9qhU0y4Tb_3AT784ymhr3zVNptL2Rk2IqkCu5W-ZbVomDlr3aYFcyGEaG3Z_3GsE3Cm8pCJ-1LHA1mzDSlNcoYGWgIpk4tODHkLtZhvheNx90CIf8ZnBYFlGEAZNNwJDaQQUpvJN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpRr1vRo3VXMgkzhhRzODYy774gTRwp-N5MjATi70sO2h7iMy4wfUGMWyRufX_htbF5CKGSak-cQeDvX6kOaYzE2zFN1eivy1wA1DjyT4KGfN5DIZSpo0E_NbDZAIaFpUVbK7eCaoOUfTBWeP33Aa1y2mYBWI09CUerfgjSgWTncKElA86bzVsuoF-pYRCvxrShJQDMRnsZRGCoFAX6krlLsXS4urwNA5Ls_sDbgRIE7UlB_JZRSBTbyvs68ep4_4uiygG7GS1_-objg4v4aYllHaDXZl5iWWFg5JPomxxovl5fbW-9UNdzBOFiyZkXfLyvY5qcQjCNujR9VeEK_qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عدوان امريكي على مدينة شيراز الايرانية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/84429" target="_blank">📅 17:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84428">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">استهداف سفينة شحن يونانية قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/84428" target="_blank">📅 17:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84427">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/84427" target="_blank">📅 17:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84426">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a2342666.mp4?token=PuA2Eo5ZRYuajMZwHBE9OLhaMAE5ma_6TUckmJfKSzl-rDy7e87CY7pw2LYhklqU3pfeVFzPCjgfRJ-bfAU6P3t9d4V_L53GhNWcgwzaVmUx93fUNHQndj9QHRGSyRh2nKKM2wWPJXbaLp5N8RwHni7gx-FgMn5c5WSWOm1A67eGynoCdPDhxb7dcioY8Czh0ltEYNYVqVeG-wVJNl_vH22nQ-xv_k8pm8QwG0iVqTk2ztThFPoBstE3OYjLEJNP-TIV6Rcu8vwKF8kv0Fkbvf6hp920vlK4xRF8PDTJ8ENR9CkgDB7b4nwCnuiLMIxCRFqZgdqaRAd8zlte7Dwqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a2342666.mp4?token=PuA2Eo5ZRYuajMZwHBE9OLhaMAE5ma_6TUckmJfKSzl-rDy7e87CY7pw2LYhklqU3pfeVFzPCjgfRJ-bfAU6P3t9d4V_L53GhNWcgwzaVmUx93fUNHQndj9QHRGSyRh2nKKM2wWPJXbaLp5N8RwHni7gx-FgMn5c5WSWOm1A67eGynoCdPDhxb7dcioY8Czh0ltEYNYVqVeG-wVJNl_vH22nQ-xv_k8pm8QwG0iVqTk2ztThFPoBstE3OYjLEJNP-TIV6Rcu8vwKF8kv0Fkbvf6hp920vlK4xRF8PDTJ8ENR9CkgDB7b4nwCnuiLMIxCRFqZgdqaRAd8zlte7Dwqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي صافرات الإنذار في الكويت
يا عيال الكويت تعورت</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/84426" target="_blank">📅 17:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84425">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اخلاء مبنى فيدرال بلازا في نيويورك وفرض طوق امني في الشوارع المحيطة له</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/84425" target="_blank">📅 17:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84424">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجارات واشتباكات عنيفة تسمع في محيط مبنى فيدرال بلازا في نيويورك</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/84424" target="_blank">📅 17:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84423">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجار واشتباكات في نيويورك</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/84423" target="_blank">📅 17:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84422">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجار واشتباكات في نيويورك</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84422" target="_blank">📅 17:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84421">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ony4bQRrMQ9sDckurjB3_9LyA3fzPnAzL8tSuW9R4Uavz4eYj8HT8eqN_P__Dc5VQNqcbnDNGeVRw4kdKxzaw6QKHGl12601TEvrAUiipqhPQfQiaqyy8bKExoEkH1R7lg1BA9_BYfOdIBZXDScDR-GnkIszwBEDLr0_wECxrMQHu2j381fVs_6xjyvKZ3z80iUvNseMSXiH1fcoaFle96NIc6_BWDVr46hCJM9yASbi-Nh82h_YLNFoFagmcdEJrmfyXrdgPwuZyLWDOR-QbJe26pnl6oJqBTv0i4Q2AmrmQY-F5VuEH67js-6E2uy1jeH-YpxezQZ1YlAb6ZhmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناقلة تحترق في مضيق هرمز نتيجة هجوم إيراني</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/84421" target="_blank">📅 17:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84420">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee7f1624c9.mp4?token=PitKn5R8W8oVIOIUhANFPbueMKZUx5sJkSIfOb1mVEG9INF-gN8te-xhNIFISU7CFFQGIVlhuqHK8dAZn9lzGswUELo3dsZ6UfeLj9fjedWE_MVwWoidGo4pnXgj2_dq6WvOWpfdISV2bZi_zyKwI-tfxAJqVKWQ1ocr9fXUeCrjyFLslFdOfLHF9DYMtKMLDKv6-K0fy4UBcl1FeJ4O5rY06QJIFurZvUwqQdPGc8WHvYjAUmPPj4mVYO-gFaPUIppeFHHYiWjDW1-JH1Uy8UX7KmzxDyvUwkLLWUCVttf3fnxmRM1I0J3W-SNkOGotQxky3j6hI9h44miaOhUjJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee7f1624c9.mp4?token=PitKn5R8W8oVIOIUhANFPbueMKZUx5sJkSIfOb1mVEG9INF-gN8te-xhNIFISU7CFFQGIVlhuqHK8dAZn9lzGswUELo3dsZ6UfeLj9fjedWE_MVwWoidGo4pnXgj2_dq6WvOWpfdISV2bZi_zyKwI-tfxAJqVKWQ1ocr9fXUeCrjyFLslFdOfLHF9DYMtKMLDKv6-K0fy4UBcl1FeJ4O5rY06QJIFurZvUwqQdPGc8WHvYjAUmPPj4mVYO-gFaPUIppeFHHYiWjDW1-JH1Uy8UX7KmzxDyvUwkLLWUCVttf3fnxmRM1I0J3W-SNkOGotQxky3j6hI9h44miaOhUjJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الكويت الان تعورت</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/84420" target="_blank">📅 17:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84419">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3c866de13.mp4?token=aI6llKH0ZpPIp-UoG8dRVaYYlstJSIwyo3TYdCewUrXZr2FgGF888m1XXLwn2-punFhPQ2OyO8yCwuAESzyZcXUOrJ69OQsZ49I2sy0UszWyedpME_yQifXYQG2v17u27eborlqidLJqgGQEQTPU4-zadS1QCW9yz8kLR60vAHkhKekY5TEyL2bT9XgtTh8XA7Eq_VxseGcQCiLfvNdRkyxIGJh5fwrIFkGrZNgRfcuv-ILdrfvrPuo4vGLeWbsBb3dVM--WVSO_BVChN3T-UU2cnaHwJGi7fSMcYFXqaTx1bQbVRMI3kR56cdje3VC2Fa846ocjZl5c8Kf46XQMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3c866de13.mp4?token=aI6llKH0ZpPIp-UoG8dRVaYYlstJSIwyo3TYdCewUrXZr2FgGF888m1XXLwn2-punFhPQ2OyO8yCwuAESzyZcXUOrJ69OQsZ49I2sy0UszWyedpME_yQifXYQG2v17u27eborlqidLJqgGQEQTPU4-zadS1QCW9yz8kLR60vAHkhKekY5TEyL2bT9XgtTh8XA7Eq_VxseGcQCiLfvNdRkyxIGJh5fwrIFkGrZNgRfcuv-ILdrfvrPuo4vGLeWbsBb3dVM--WVSO_BVChN3T-UU2cnaHwJGi7fSMcYFXqaTx1bQbVRMI3kR56cdje3VC2Fa846ocjZl5c8Kf46XQMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناقلة تحترق في مضيق هرمز نتيجة هجوم إيراني</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/84419" target="_blank">📅 17:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84418">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">" اخ عليج يالكويت تعورت يالكويت "   مواطنة كويتية تتحدث عن ألم و حزن في قلب كل كويتي بسبب القصف الإيراني القققاشم … مراقبون اكدوا ان لو لا وفاة المرحومة الفنانة ذات الأصول العراقية حياة الفهد لكان شاهدنا مسلسل رمضاني يتحدث عن كيف هرب جاسم بالوانيت نتيجة القصف…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84418" target="_blank">📅 17:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84417">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هجوم صاروخي ومسير مركب</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/84417" target="_blank">📅 17:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84416">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84416" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84415">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84415" target="_blank">📅 17:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84414">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/84414" target="_blank">📅 17:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84413">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe1ed9d731.mp4?token=ldUm_qdvTV_faJEbZljhmgvOg-EjdjtRHPqd5tHe5sLduK1xlwTRLxp2JVqmWjMrUsOuxfSbub4z94ErvltdEM_fninq1XV_aoEelfkMX3Md1aQ_TMQcLnvgQpuYiNln1OJobsU-Knv0xJ7cMZM7tUiINR8ba3tsrQPSO-z8eCith4KpVSbG1azXAyr4jYf75kRl_2lOtbyGSzO9O_2bOWu8Z7vNtZnhhr76VGUW1w-mqMxxR1AQe-VDR3pelQ-8xs4aahFWDrvpHPS4kd3A8l9rQFbeIKe4vZ57Y3Kl3mKNBANj9bqKvohZ0YlCh8sUAuTy3M5aGuYc4AgtYkpJ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe1ed9d731.mp4?token=ldUm_qdvTV_faJEbZljhmgvOg-EjdjtRHPqd5tHe5sLduK1xlwTRLxp2JVqmWjMrUsOuxfSbub4z94ErvltdEM_fninq1XV_aoEelfkMX3Md1aQ_TMQcLnvgQpuYiNln1OJobsU-Knv0xJ7cMZM7tUiINR8ba3tsrQPSO-z8eCith4KpVSbG1azXAyr4jYf75kRl_2lOtbyGSzO9O_2bOWu8Z7vNtZnhhr76VGUW1w-mqMxxR1AQe-VDR3pelQ-8xs4aahFWDrvpHPS4kd3A8l9rQFbeIKe4vZ57Y3Kl3mKNBANj9bqKvohZ0YlCh8sUAuTy3M5aGuYc4AgtYkpJ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حرس الثورة الاسلامية:
إن الشعب الإيراني الإسلامي المنتفض وصانع الملاحم، بالاعتماد على الله تعالى، وبالاستناد إلى الدعم الواعي من حضوركم أيها الشعب البصير في الساحة، قامت القوة البحرية التابعة للحرس، عبر هجوم متزامن في الموجة الـ23 من عملية «نصر 2»، وعلى ثلاث مراحل، وبالرمز المبارك «يا رقية (ع)»، بتوجيه ضربات قاسية إلى القوات الأمريكية الإرهابية في المنطقة.
المرحلة الأولى: الهجوم على مستودعات حفظ وصيانة الطائرات المسيّرة التابعة للوحدات الأمريكية المتمركزة في مطار الصخير في البحرين، ما أدى إلى تدميرها.
المرحلة الثانية: الهجوم على مستودعات تجهيز الزوارق من طراز TF59 في ميناء سلمان بالبحرين، ما أدى إلى تدميرها وإلحاق أضرار جسيمة بالزوارق.
المرحلة الثالثة: إحراق مستودعات تمركز ودعم وتجهيز قوات الكوماندوس البحرية الخاصة في قاعدة عريفجان في الكويت، وتدميرها بالكامل.
إن الهجمات الساحقة التي ينفذها مقاتلو الإسلام، باستخدام أعداد كبيرة من الصواريخ والطائرات المسيّرة، في إطار الرد بالمثل والرد على اعتداءات الجيش الأمريكي قاتل الأطفال، مستمرة.
إن رئيس الولايات المتحدة غير الحكيم، الذي اعترف مرارًا بجهله وقلة إدراكه بأوضاع العالم، والذي يقول إنه، من دون معرفة عمق ارتباط إمامنا الشهيد بـشعوب العالم، ومن دون إدراك حب وتعلق الشعب الإيراني وشعوب الدول الأخرى به، قام باغتياله، وكذلك قوله إنه أشعل الحرب في هذه المنطقة وهو يجهل أهمية مضيق هرمز في اقتصاد العالم، قد كشف مرة أخرى الليلة الماضية عن عدم حكمته وجهله، وصرّح بأن عددًا قليلًا من الصواريخ والطائرات المسيّرة بقي لدى إيران وأنها أوشكت على النفاد.
ليعلم رئيس الولايات المتحدة القاتل أنه إذا استمرت هذه الحرب لعدة سنوات، فبإذن الله تعالى ستستمر صواريخنا وطائراتنا المسيّرة في الهطول على رؤوس المجرمين الأمريكيين حتى اليوم الأخير منها.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/84413" target="_blank">📅 16:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84412">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84412" target="_blank">📅 16:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84411">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84411" target="_blank">📅 16:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84409">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3VGYnQWENbYY9637yw9qdhiqgda029aY-TEo1bKfdnoObzQBzKmOGESU8xKmXpoO5jDGBZbJxFPsx5MAdtr05IrsIgmdn4tvNaaZa-HNtUDxK1llxCoI35dR_nzEC9oOuALMsKYHirdoJn5gSaOC7KkwCYCqmwTnIbOPvdoCdODfKqMyjk9rw1AZPccBHuLQBaCHf3Qx_weGNfNypo69vb8SFIKrCEmULSunENffr-3E4EXd2SDkZkRr2VnutIyZaullsmiHJ3nAowl6cHI4W6i9v9nguo0nKCYknxIrERAaAQhO5VPVA7tIcCoA1sK8gf52k3bxdYpq7Mpuecm3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uIhTWJ9kM4NuU5EfNVbz0IoXKh-nVqdtIGRGx0DtKs339tGy2zaU08e2XPw2W1ITDr5yEwGNaULyIumTTGZB7WEm-Z_C5Bx2Wrl2nIw6mCmELkNrnT9hIAVPumPeetdapzXFVuR_vrZa4qXlqQcX0vyBLtd2wKVCEo8G7eNf3rqH2dBfEWQeQY51js972L2zduXlVmAg-SHLCkWhgueMBSeowqnjNa7bhJ1g5xDbgTXYPFu7Z3Jr5ay7txBPAzkJZWjB7xM5VNP1BoKLi5uwDfFVAxSeQlIhlob0psZwd2gN0UP0a2vyunNUfZ5y0oJWLw-wkQMhuQWBxMl7qen4cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇯🇴
🇮🇷
🔻
That’s what I voted for. The Middle East isn’t safe. U.S. troops should return home. Isabella Gonzales, a U.S. Army soldier, was killed by IRGC shelling in Jordan.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84409" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84408">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
مشاهد لإطلاق صواريخ تعمل بالوقود الصلب، من طراز خيبر شاكان، وفاتح 110، وذو الفقار، وصواريخ عماد التي تعمل بالوقود السائل، في عمليات هجومية دقيقة وتكتيكية ضد مواقع أمريكية في المنطقة، ضمن الموجتين 21 و22؛ عملية نصر 2</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84408" target="_blank">📅 15:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84407">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇾🇪
بيان للقوات المسلحة اليمنية:  بسم الله الرحمن الرحيم  قال تعالى: { وَلَمَنِ ٱنتَصَرَ بَعۡدَ ظُلۡمِهِۦ فَأُو۟لَـٰۤىِٕكَ مَا عَلَیۡهِم مِّن سَبِیلٍ } صدق الله العظيم  يواصِلُ العدوُّ السعوديُّ المجرمُ حصارَه الظالمَ والغاشمَ على شعبِنا العزيزِ لما يقاربُ اثنيْ…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/84407" target="_blank">📅 15:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84406">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇾🇪
بيان للقوات المسلحة اليمنية:
بسم الله الرحمن الرحيم
قال تعالى: { وَلَمَنِ ٱنتَصَرَ بَعۡدَ ظُلۡمِهِۦ فَأُو۟لَـٰۤىِٕكَ مَا عَلَیۡهِم مِّن سَبِیلٍ } صدق الله العظيم
يواصِلُ العدوُّ السعوديُّ المجرمُ حصارَه الظالمَ والغاشمَ على شعبِنا العزيزِ لما يقاربُ اثنيْ عشرَ عاماً من نهبٍ للثرواتِ وحصارٍ شاملٍ على الموانئِ والمطاراتِ براً وبحراً وجواً بما فاقمَ معاناةَ شعبِنا العزيزِ حتى وصلَ الحالُ إلى مستوىً لا يطاقُ بدونِ أيِّ حقٍّ أو مبررٍ له في ذلك وهذا ما لا يمكنُ القبولُ به أوِ السكوتُ عليه لأنه لا يستندُ إلى حقٍّ أو مسوغٍ قانونيٍّ أو إنسانيٍّ وليس له أيُّ مشروعيةٍ فهو حصارٌ باطلٌ وعدوانيٌّ ونتائجُه كارثيةٌ في معاناةِ شعبِنا اليمنيِّ العزيزِ مع ابتدائِه أيضاً بالعدوانِ على بلدِنا باستهدافهِ مطارَ صنعاءَ الدوليِّ في عدوانٍ ظالمٍ وغادرٍ فلا يمكنُ لشعبِنا أن يعاني من الحصارِ الظالمِ ويُعتدى عليه دونَ أن يكونَ له موقف، فشعبُنا العظيمُ هو شعبٌ مؤمنٌ مجاهدٌ، شعبُ الإيمانِ والحكمةِ وصاحبُ قضيةٍ عادلةٍ وله الحقُّ الكاملُ في مواجهةِ هذا الحصارِ والعدوانِ الظالمِ بكلِّ الوسائلِ المتاحةِ.
وعليه.. وتلبيةً لنداءاتِ شعبِنا العزيزِ المجاهدِ في الخروجِ المليونيِّ العظيمِ في جمعةِ التحذيرِ والنفيرِ وما سبقَها من تجمعاتٍ ووقفاتٍ قبليةٍ كبيرةٍ فأنَّ القواتِ المسلحةَ اليمنيةَ تؤكدُ على الآتي:
أولاً: تعلنُ القواتُ المسلحةُ اليمنيةُ حظرَ الملاحةِ البحريةِ على العدوِّ السعوديِّ المجرمِ وفقَ معادلةِ 'الحصارُ بالحصارِ' وسيدخلُ حيزَ التنفيذِ من لحظةِ إعلانِ هذا البيان.
ثانياً: نؤكدُ على حقِّ شعبِنا العظيمِ في مواجهةِ الحصارَ بالحصارِ والتصعيدَ الشاملَ بالتصعيدِ الشاملِ وتثبيتِ هذه المعادلة.
ثالثاً: تؤكدُ القواتُ المسلحةُ اليمنيةُ جهوزيتَها الكاملةَ لكافةِ الخياراتِ وأنَّ أيَّ حماقةٍ يُقدمُ عليها العدوُّ السعوديُّ الأرعنُ من خلالِ التصعيدِ الشاملِ فسنواجهُه بتصعيدٍ شاملٍ وقاسٍ بإذنِ اللهِ وقوته.
رابعاً: ندعو أبناءَ شعبِنا العظيمِ لمواصلةِ التعبئةِ العامةِ والنفيرِ العامِّ والاستعدادِ التامِّ لكلِّ السيناريوهاتِ والتطوراتِ والإسنادِ للجبهاتِ بالمقاتلين.
خامساً: نوجهُ التحيةَ بإعزازٍ وإجلالٍ لأبناءِ شعبِنا اليمنيِّ العظيمِ الذي خرجَ في مليونيةِ التحذيرِ والنفيرِ بشكلٍ لا مثيلَ له ونؤكدُ له أننا لن نالوَ جهداً في استردادِ حقوقهِ المنهوبةِ وإنهاءِ الحصارِ الظالمِ عنه مهما كانتِ النتائجُ والتداعياتُ مستعينين في ذلك باللهِ ومتوكلينَ عليه.
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 6 صفر 1448هـ
الموافقُ 20 يوليو 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84406" target="_blank">📅 15:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84402">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8TewnQZLGSUkgvbyH1IOY1Av2ACHdfsDYvh702es6W8_hq60O2dDFEUGWfroBDXJYDs96yeE1IESjyEqxKG-c9PaTBceebNpcZa2z6vN9EwXmrE4Fm6CIxdpmrG8Me_HBgjo-Y_qKHNRPxj4nPLAkSiZktPZxlWZbQzj7b9xJBioK6PE0zcTOqP_a5OHM-48BcEdngXfZZAM95owFBMVQHo1RN_0BwbzmLxbktgBrDqH1gYWwZ1YjaRgSRhAghyER79m2zn00qH-Km3t5miiK914oeqx6gIVO8182gzZKlLna2pjFRSjd2c4HYYqtO6VPSycGQUaL9YGzHU3O3nlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjxCbwNNSLRX8fud1TfDySB860rvklEKH4jc_KqclRw4pi51yjYfdLyV-1oFqg7xJwLwWWe6UlkG8u0veIVU6ahC7NPoLvidzs3CVPm5q8ef0qhrvodd47kCXsKm_sarDWKn90uhEoONLV8CG60F90nv3PqjamMziFMGrI4jMUgbKHYN9ElahRi2l9w3IF1aMJbMVyAGW1Pg2QscCdlOlZYwJGWzBpE8B1LJd3Uprs6_PJi4yYrOWPu5JB_UYCo8yFZh799H1MYjmfogklU4cUJ-7IKfjyp8GBWqHmw7kJLoiIg7WVsq96SKM3Z8jKXJZfIQOZ7JLLPACn5dCIoaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9dcnL5mh71orMhnwvJxcZKWf51GtmsWFzGJuFZ4hUMVvgHNc3ItP01HNXJobhGZ-A8zxvp280SqIwOc3ly1NFZRNtz66DJeUqd-b1-J5MyDJB92l8t1qoVqRmoklYtlPlnXN5RZUk_qfKAjKQnwWzG6agzwy95P9v1R1QC90QNrO-H5AhKpuUbjoe1ZFj1DbWUHkdHuR3o3cLxwB3Lz0tRNmQmbxZSvyRBj-J08u33BcBzdr4UjWv9MynWYbVdpSBCDeb7ASqRzev_XQjgrXeDHLQ9zwuuZ7MOgwlBZsWA8IJ1-_gtjcjs_plQ3f81v1Z1AhJkUKB-MKGQaB98iSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNpMLu09-1mwodJxvKHtZ4YWRWgXd4beYQK9FfcFW_olReWQmxMZu7KsyBUl92qf8M8ldUOLce79pzMNlLOnCfG4Tpvf_naVPDBoWVFofpRiFUmBloyYmYS9JqCOpjm9Zz6v3t3aK9jZoshqJvQyVGmGRlIpW9TF-T-WR1CcCC6PCAS4kq63e_NmAjUPgyb5W_SIrchHgicWqW1YqpVCZwMgRRqm1c0GExqGUmAWXTUu4cNwH9zgO0N7FpLf4Tr66skZv_t1z-mV0toYAf9JGEnxdZOSctvt1DMrvf1IlO5bEEhYPovImEYs8iOBaqrHMWa85Dpts-_lz5jYb_MjHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الوقف السني العراقي يقيم احتفالية في مقام الشيخ عبد القادر الكيلاني الاحتفالية بسبب فشل الانقلاب على اردوغان في تركيا علما ان الاحتفالية حضرها السفير التركي وعدد من أعضاء مجلس النواب العراقي ..</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84402" target="_blank">📅 15:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84401">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الوقف السني العراقي يقيم احتفالية في مقام الشيخ عبد القادر الكيلاني الاحتفالية بسبب فشل الانقلاب على اردوغان في تركيا علما ان الاحتفالية حضرها السفير التركي وعدد من أعضاء مجلس النواب العراقي ..</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84401" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84400">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN9stcygTg9MQqGSEuNAuRfq7FU9T9ThfWXztQ3p6kC6APUNEoCYiT70W85yHybI2J76HrcnT5fDEbWpyWDCIrStqiEzrgvjY_qfGNFxAorz8iVqxivSuSfabWDbNgiD-DkZXYIGEE-M9Z2s9BiGwdABUwDeH-geGHqC8lNDf-a9L21DTyCnyuamSNFzGRrx_fyjLGUrLw0YPDtkTR2nvSmsICWaclw9rGctVUixQIvvutvCj2K6c-A1JOv3mWOhsRMVkdZ1hsB_kKltPFKs94mco5LRbPeka3-ZI5pbZsWVL12vDFMWzjyIK0SgM-YWq5wmjcWFZ_cU94SvUbKZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
‏يُواصل الأمريكيون جلب معدات عسكرية جديدة إلى المنطقة، ويدّعون رغبتهم في وقف الحرب. لقد اعتمدوا على معلوماتنا الاستخباراتية، التي لا تتجاوز مستوى ذكائهم المتواضع. ‏لقد وصلنا إلى مرحلة التخطيط لهذه الألعاب الأمريكية، وقد استعددنا وفقًا لذلك. يجب أن تؤكد الأفعال هذه الادعاءات، لا أن تناقضها.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84400" target="_blank">📅 14:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84399">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOglC_wtJVeMXuxxGvxlgGP4k8eNhVkknqOOyOXPrWgC6veVu1rQLG2K7ijCkf24tjcatdcKFkqoOkaKEUD-9HV-Sd8FLZUK15rELwyXMxocaiBeke1Rr_zcAI6L0keW6Pp15eD5UKt1oLn4Mns7hDmtxGvRV8h4nG6vo6mkD1xbHpMPydwbPl2-2JRn4yoDhuuS5X3V3mBUgf_sZgl0-sLByoSAMrPElTOUQvSFLONhX2sR3TBuaNqUuvsGSDGNcogDj8CZpBM1pZMxDioKsBnY6dfRfPp8lI0r_n6U71lfeE5ffBObCPzot3g8nW4L3Dj4nj4p8r5FEg70gCt42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
بيان:
‏تعلن حركة المقاومة الإسلامية حماس عن انتخاب الأخ المجاهد خليل الحية رئيساً للمكتب السياسي للحركة خلفاً للقائد الشهيد يحيى السنوار.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84399" target="_blank">📅 14:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84398">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏الطيران المدني البحريني: عدوان إيران استهدف أجهزة الملاحة الجوية المدنية للبلاد بمسيرات</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/84398" target="_blank">📅 14:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84397">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سقوط طائرة مسيرة امريكية من طراز لوكاس بالقرب من رأس البيشة في منطقة الفاو الجنوبي في محافظة البصرة جنوبي العراق من دون ان تنفجر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84397" target="_blank">📅 14:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84396">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">باكستان وقطر يقدمان مقترح مشترك لحث الولايات المتحدة وإيران على العودة إلى موقف ما قبل 9 يوليو/تموز "كخطوة أولى" لاستئناف المحادثات</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84396" target="_blank">📅 14:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84395">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huSg0qr-5YJTRaSqhzC653tD6RHSmvFN4vFRGXA0I_avxUV797vcECXw2ekJs3mwlgAxhfzj562uCWJDXDvj6yPBC-8SvSacxlDJyAIgQNsFRpLHariS7n6dHRDpFk_hr5ElTfWC6Xdh0lupsfi-bhdw7EtCZVZ92bWszyiNeBLQHEmfkuvMtDiXq_qfKCp16QWlJmMaruClb-1sJepRqNvc7L8YVUrEQp9fATL4J2USlcGnwDJav8dnQSRpaYnnkd7NO6NmEH0hj340T5tC-8YtyR9LT9rKCjzAnrExa8azZ9dbxUaS0FCI7dFIRNLG35-_NZyEwZmEl95Z6o3flA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
جيش العدو الامريكي يكشف عن هوية اثنين من قتلاه خلال الهجوم الايراني على قاعدة موفق السلطي الجوية في الأردن:
- الملازم أول تايلر جيمس فيهان
- الجندية إيزابيلا غونزاليس</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/84395" target="_blank">📅 14:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84394">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇨🇳
وزارة الخارجية الصينية:
اليابان تحاول إحياء قوتها العسكرية والسعي للحصول على أسلحة نووية، إذا سعت اليابان إلى تعديل "المبادئ الثلاثة غير النووية" فإن ذلك سيقوض النظام الدولي الذي تأسس بعد الحرب العالمية، وينتهك التزامها بالسلام، وسوف تدفع في النهاية ثمنًا باهظًا.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/84394" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84393">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇰🇼
الجزيرة القطرية:
الكويت تدرس خفض نسبة الدوام الحضوري في مقار العمل؛ لتخفيف الضغط على شبكة الكهرباء والتعامل مع التحديات المرتبطة باستهداف محطات توليد الطاقة</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84393" target="_blank">📅 13:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84392">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
🇾🇪
إسماعيل بقائي، المتحدث باسم وزارة الخارجية الايرانية:
في رأينا لا وجود لما يُسمى "حظر جوي" على اليمن ونعتبر ان مبدأ فرض العقوبات على أي دولة مبدأً قاسياً.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/84392" target="_blank">📅 13:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84391">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
مصدر أردني لنايا: وقوع عدة إصابات في صفوف القوات الأمريكية نتيجة الهجوم الصاروخي الإيراني الذي طال قاعدة موفق السلطي بالأردن.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/84391" target="_blank">📅 12:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84390">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📰
نيويورك تايمز:
البنتاغون يخفي عشرات الإصابات بين أفراد الجيش الأمريكي في الحرب الإيرانية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84390" target="_blank">📅 12:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84389">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f9ad4d954.mp4?token=quNPZA3g4cEbwI64pbvvbRz5V13eRB6UG6YNNtqkY8U-FbxioSl_31uaoPd6cOYroXwCAX0W587xnBUlZA7B4Ye5pNQk6UayytM1QuEjSSDqAMbgw0Qsa9JWITWKp9cFz6Fh9Nls0Y0Ncpn7Uhcb0bICfv5Si-5wa8I3qVHrxPDowLm4AGWlS9Vlqqo0GqveRHny-D5GhtZX2Z1-Cj6jN5lBYiHb4GQYRBSE3bKtp0MLcYbXnu2Q-vsb8mOasy515Saab8WoT_Wrgiq1jh7vwGDiN0D7UnMXEBTqt_fDVKjnhcwt1NeNZyurzEeDaPKeYBrZDIhpsOvfvA3jMyDxhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f9ad4d954.mp4?token=quNPZA3g4cEbwI64pbvvbRz5V13eRB6UG6YNNtqkY8U-FbxioSl_31uaoPd6cOYroXwCAX0W587xnBUlZA7B4Ye5pNQk6UayytM1QuEjSSDqAMbgw0Qsa9JWITWKp9cFz6Fh9Nls0Y0Ncpn7Uhcb0bICfv5Si-5wa8I3qVHrxPDowLm4AGWlS9Vlqqo0GqveRHny-D5GhtZX2Z1-Cj6jN5lBYiHb4GQYRBSE3bKtp0MLcYbXnu2Q-vsb8mOasy515Saab8WoT_Wrgiq1jh7vwGDiN0D7UnMXEBTqt_fDVKjnhcwt1NeNZyurzEeDaPKeYBrZDIhpsOvfvA3jMyDxhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
ترامب يتحدث عن بيدرو سانشيز: ‏تحدثت مع إسبانيا وهنأتهم على امتلاكهم فريقاً رائعاً. ‏لا توجد بيني وبينه أي توترات.
ولا توجد بيني وبين أي شخص أي توترات.
😄</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/84389" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84388">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2bscMp8Dqr4I0L4IkK_RZNC3XRc52JPAI64ZRE0Cr2uGqS179qqyOv66zpMBpZY2lqzAm103s7QVYDNrqv0dH-zPd21Fkyxsr9daAdgBwF9PPE7yWdqve_60evXHiCvJCK2pgNcJOlQYTxLlUGKhqB1vTLUaualWIQZ23p8ZbnnthGgLGLcNupSbh3yyRURd3f8hNbDRa-nIvaVX68E9VjgqJU80gHMUeXdcpQt59dHNCImtUjXmN-4YbsOwCIFO0hDeNa1eQ80hAy-zKtjLDpxXC1G5rYmEna2M0JhB2bvO6NIBafsOqqJtucP90loi0h0oyfUU--J-J7q8xPtnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوارع طهران حاليا</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/84388" target="_blank">📅 11:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84387">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">#ترفيهي
القيادة العامة لقوة دفاع البحرين: إيران تواصل نهجها العدائي الممنهج عبر اعتداءاتها الآثمة التي تستهدف المدنيين في مملكة البحرين.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/84387" target="_blank">📅 11:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84386">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
🇵🇰
وزير الداخلية الإيراني يصل باكستان اليوم حاملا رسالة خاصة من بزشكيان تتعلق بملف المفاوضات</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/84386" target="_blank">📅 11:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84385">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79a89642f.mp4?token=Kif_UDOTHDz1yaDMuldSrIJAivL1oBp9hI0Tt_cVjQxw0RIblnUuS1iWnW3qn0H8UoXB2ave7FARyNoFHXZkrBhHfseXztSgZ6aBEWt6nephgOzmvHoiFWOmlQpjfZWuG2fMJxT7PY39c735ziEfFU1OqlTXtcgtxek0nRJlNbokkT6HMTx7Fs4IJ3nAYLj0Ugrk9g38eXYhAcwmMFy9bxh_xl-cnvpHwJ6qTlyi4v6KbXhkf6MZu2nQmpVEr0yZgmCd4DGZkApDbKgsqYAd7FExuQgivcR54mKjvXdKociG3Nt4o3kR8s6xDxlGstmBmCG5XxVHuSZZeo1wkMRDGylNEOsjSrwSFRUsMctkO5f3HqFmdMNQ0KQJBWr0a7EuU9a-V39o1j9UdXiTeOi-Imeh7lttKbrovx8PR7-r20iiYwMc-uMUw8RYFgwkbgs-54XvcLO7J6bdSNzVR8L1Ttl4bp1u0P-3Rl946P7FZOR1FIJbQFenoE0T8YSeJ22dRrP_W2aqtiKVSJSVL-MJji2J8eEOMugEr1_l-LEIljfshiYTqSrc23HrM17ApuY1rasVbZLBg3oKpTPniNoU9Nuf2jS2BzhbC1j5dPTqRcgDvulCKRekac5p93p9nbPEeHpHoj4piEvFAIC6YuQm6vpTdlIr9ML9HbBOBv3ckBo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79a89642f.mp4?token=Kif_UDOTHDz1yaDMuldSrIJAivL1oBp9hI0Tt_cVjQxw0RIblnUuS1iWnW3qn0H8UoXB2ave7FARyNoFHXZkrBhHfseXztSgZ6aBEWt6nephgOzmvHoiFWOmlQpjfZWuG2fMJxT7PY39c735ziEfFU1OqlTXtcgtxek0nRJlNbokkT6HMTx7Fs4IJ3nAYLj0Ugrk9g38eXYhAcwmMFy9bxh_xl-cnvpHwJ6qTlyi4v6KbXhkf6MZu2nQmpVEr0yZgmCd4DGZkApDbKgsqYAd7FExuQgivcR54mKjvXdKociG3Nt4o3kR8s6xDxlGstmBmCG5XxVHuSZZeo1wkMRDGylNEOsjSrwSFRUsMctkO5f3HqFmdMNQ0KQJBWr0a7EuU9a-V39o1j9UdXiTeOi-Imeh7lttKbrovx8PR7-r20iiYwMc-uMUw8RYFgwkbgs-54XvcLO7J6bdSNzVR8L1Ttl4bp1u0P-3Rl946P7FZOR1FIJbQFenoE0T8YSeJ22dRrP_W2aqtiKVSJSVL-MJji2J8eEOMugEr1_l-LEIljfshiYTqSrc23HrM17ApuY1rasVbZLBg3oKpTPniNoU9Nuf2jS2BzhbC1j5dPTqRcgDvulCKRekac5p93p9nbPEeHpHoj4piEvFAIC6YuQm6vpTdlIr9ML9HbBOBv3ckBo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشاهد لاحتراق منطقة واسعة في معسكر للمعارضة الإرهابية حيث تم تدمير مبنى بشكل كامل في السليمانية شمال العراق</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/84385" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84384">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
نائب قائد القوات البرية في الحرس الثوري: سنقضي على أي توغل بري أمريكي في أراضينا فور وقوعه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/84384" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84383">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sb3lK8sY64ZZQ2roE6PHlDrSfcTZj0E8siy3q3CFwBfCVlva-6ThR6weGJgtqFiZaAFHkdi90jk2azAD8yX4fzilPknDY13TzHvqqMfs3aY8qquxXvCaEyahGMi8lLYA4wjDuqQs2ThiHIIF0-YSfn1TEogRa7JkekYJICTxyHToCbYmUcbs9sCxT882X5-9eI_NXqKzuLrEvcmhL3LI9iMDI5QQ2EwUf3A2Hr35ZkqJjvvKFlBBeH1sWKZLG9A2fa19WcyvY_6PKHuN2qJlNZlZcz-8kyfFJYck8XbtY1jF7x0R3GWFtC7-Kgcrk5KP4QpHT5pwyif9Y8hWlXbAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
طيران الجيش العراقي يقصف (6) مضافات لإرهابي داعـSh في منطقة (وادي زغيتون) ضمن قاطع قيادة عمليات كركوك.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/84383" target="_blank">📅 10:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84382">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
حدث بحري في عمان</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/84382" target="_blank">📅 10:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84381">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔻
حدث بحري في عمان</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/84381" target="_blank">📅 10:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84380">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تجدد الانفجارات العنيفة في البحرين</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84380" target="_blank">📅 09:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84379">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">على مايبدو البحرين تعيش اصعب لحظات حياتها</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84379" target="_blank">📅 09:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84378">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">على مايبدو البحرين تعيش اصعب لحظات حياتها</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/84378" target="_blank">📅 09:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84377">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/84377" target="_blank">📅 09:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84376">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
إعلام إيراني: سماع دوي انفجار في مدينة أصفهان</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84376" target="_blank">📅 09:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔻
🇧🇭
المشاهد الآن من البحرين
🔻
تُظهر صور أقمار صناعية أضرار على محطة فرعية للكهرباء في البحرين حيث يُستخدم الموقع كمركز قيادة وسيطرة (C2) عسكري أمريكي ومركز بيانات للذكاء الاصطناعي إثر الهجوم الإيراني.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/84375" target="_blank">📅 09:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84374" target="_blank">📅 09:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84373">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84373" target="_blank">📅 09:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84372">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇱
🇺🇸
مسؤولين صهاينة: التقديرات في إسرائيل أن واشنطن قد تطلب إدخال عشرات الطائرات الإضافية للتزود بالوقود إلى إسرائيل</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84372" target="_blank">📅 09:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84371">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc91471066.mp4?token=VsbIRbswG0piI27IorFm4K6kMB2pmH1CrKlEKvRD6GNQbfLcaaxqe2i1LbHdMt0ldDfgeT6VUHc_0VzYVhXiaiz3XiPWT9m2r_6FalLAIUsoWtDmsvWoFO_x0X18iWD5bcMcoDccVaKGIKRHoTfBYb509rWXDgNX07pIZwA5ZXGln15uJWXMglWmc5n4HMobs7ItWFINirwyMNJk40qaUpCWbNfjqTlKvDLWGhZ8eRbZRB5OvKbaof5VJRJr1tey8en5y_uvR3yJ8zS5I1q5k0Eu5R5cn6E1p6WEXUhG9S93euv-bO1KpMjpln3aCcYTzihfA-lnTm89m6-cr3x9WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc91471066.mp4?token=VsbIRbswG0piI27IorFm4K6kMB2pmH1CrKlEKvRD6GNQbfLcaaxqe2i1LbHdMt0ldDfgeT6VUHc_0VzYVhXiaiz3XiPWT9m2r_6FalLAIUsoWtDmsvWoFO_x0X18iWD5bcMcoDccVaKGIKRHoTfBYb509rWXDgNX07pIZwA5ZXGln15uJWXMglWmc5n4HMobs7ItWFINirwyMNJk40qaUpCWbNfjqTlKvDLWGhZ8eRbZRB5OvKbaof5VJRJr1tey8en5y_uvR3yJ8zS5I1q5k0Eu5R5cn6E1p6WEXUhG9S93euv-bO1KpMjpln3aCcYTzihfA-lnTm89m6-cr3x9WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"
اخ عليج يالكويت تعورت يالكويت "
مواطنة كويتية تتحدث عن ألم و حزن في قلب كل كويتي بسبب القصف الإيراني القققاشم … مراقبون اكدوا ان لو لا وفاة المرحومة الفنانة ذات الأصول العراقية حياة الفهد لكان شاهدنا مسلسل رمضاني يتحدث عن كيف هرب جاسم بالوانيت نتيجة القصف القاشم !</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/84371" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84370">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOiqhDQjIUKqRT2ZK6AHq5H-ckU8y0RYTHEnvu0T2IwkIhgAU1hyjh8mmwv0rb4tg9EQ0HpNfh1H_wN3Od7d_oVh2Txmzf0-u2ww0XaJrXcuCeQxXySI5ebHuEpCQMAy3Evi60v-yfcSePvvMLvLsVxHOQlxawtXTzxD2-q5-TFxnTsjdT8B4JCTS4PgAUra0CC5MlZ-Q85yCxk0DI3uSDJg-muFNzcHpknxIgIUuyniijeYpDmm014ItHiQcOQyIshaQIyAB7jMj6em33hIBJVniFJiawW13DmD1fWYCpyCpnobzng4VBL8FKlQBvYgj7xOCi-Ec7eXITErwWZewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط مباشر في المنامة وتصاعد أعمدة الدخان من مكان الاستهداف</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84370" target="_blank">📅 09:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84369">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات متتالية تهز البحرين</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84369" target="_blank">📅 09:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84368">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">البحرين تحت الصواريخ الإيرانية من جديد</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/84368" target="_blank">📅 09:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84367">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84367" target="_blank">📅 09:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84366">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84366" target="_blank">📅 09:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84365">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجارات تهز البحرين مجددا</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84365" target="_blank">📅 09:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84364">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84364" target="_blank">📅 08:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84363">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50429d07bd.mp4?token=mC3eu0jdojq9P3Ye7RKCHqLTVwj3w1vE2Xy1Je6SCrBWIQTIN70HgbewyuPmbu2Dv_3Q575rdH3iNKRdXm07RauwnO8obsWIax6AhQ2U1Q-d8DEROi-CXfgk1uR0NN2fzoOIO4gL-R9DG9NW9v5REmSstAF33ndksdePoAr-mlTdbx2fnkWGPn4Br6il_S82NaeXLRtYoAEkInWs_ukW2J3OqRjExy3ku5fO0jo7GN8uKTGHOkyPss0UdApSPiXYsQRah-5BE8ak-z6ObdEZTng8VSaU4SPSLWDtvlOejM-YWYDMcZ6DSLKBIUEpB69mw1Q7Wm9-DJ_Ux5E8gAemTIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50429d07bd.mp4?token=mC3eu0jdojq9P3Ye7RKCHqLTVwj3w1vE2Xy1Je6SCrBWIQTIN70HgbewyuPmbu2Dv_3Q575rdH3iNKRdXm07RauwnO8obsWIax6AhQ2U1Q-d8DEROi-CXfgk1uR0NN2fzoOIO4gL-R9DG9NW9v5REmSstAF33ndksdePoAr-mlTdbx2fnkWGPn4Br6il_S82NaeXLRtYoAEkInWs_ukW2J3OqRjExy3ku5fO0jo7GN8uKTGHOkyPss0UdApSPiXYsQRah-5BE8ak-z6ObdEZTng8VSaU4SPSLWDtvlOejM-YWYDMcZ6DSLKBIUEpB69mw1Q7Wm9-DJ_Ux5E8gAemTIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇴
لقطات من الأقمار الصناعية تظهر ضربة مباشرة على مبنى في قاعدة موفق السلطي الجوية بالأردن حيث وقد دُمر المبنى إضافة إلى تضرر عدة مركبات مجاورة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84363" target="_blank">📅 08:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84362">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇷🇺
🇺🇦
انفجارات ضخمة جداً تهز جنوبي أوكرانيا جراء قصف روسي مكثف.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84362" target="_blank">📅 08:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84361">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات عنيفة تهز المنامة</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84361" target="_blank">📅 08:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84360">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0727eab181.mp4?token=TBvlc8mXpeyNcPLNuMAUdv4LPOrR6IxHaDLdyMxUBmBXmaLbXX5WLWIM2yI_1s_kfbZ_pb4UsWelQkGG8IXPZ053iRlmA0ugS41TzAEMx6-VK1FZqSkFCMgmY_6fn4KQtmPEmrWGWo1yKZKMj-oN96mvxoHKkKi4x2o3du4kXZkzzj6wUiblFgllUWh0qyixY6NpiRnYC5_97WWgkaF9pf56Cuz12fNZfX6jfuGrhmLmC1TVO28GWB-ZB1MNmrcoXlPHjkBR9P0q75qauLirPnHNP__j3_2NptZUNOfhKbNuk5jFA0b_rEsAejgtbMFGK2W-hTv_61NABtHGhGEnrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0727eab181.mp4?token=TBvlc8mXpeyNcPLNuMAUdv4LPOrR6IxHaDLdyMxUBmBXmaLbXX5WLWIM2yI_1s_kfbZ_pb4UsWelQkGG8IXPZ053iRlmA0ugS41TzAEMx6-VK1FZqSkFCMgmY_6fn4KQtmPEmrWGWo1yKZKMj-oN96mvxoHKkKi4x2o3du4kXZkzzj6wUiblFgllUWh0qyixY6NpiRnYC5_97WWgkaF9pf56Cuz12fNZfX6jfuGrhmLmC1TVO28GWB-ZB1MNmrcoXlPHjkBR9P0q75qauLirPnHNP__j3_2NptZUNOfhKbNuk5jFA0b_rEsAejgtbMFGK2W-hTv_61NABtHGhGEnrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇰🇼
لاول مرة
الكويت بدأت باستخدام المولدات الكهربائية المتنقلة للمناطق السكنية بسبب العجز التام لمنظومة الكهرباء على خلفية القصف الإيراني المستمر .</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/84360" target="_blank">📅 08:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84359">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">منظومة الباتريوت تفشل بالتصدي للصواريخ الإيرانية في سماء المنامة عاصمة البحرين</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84359" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84358">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84358" target="_blank">📅 08:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84357">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84357" target="_blank">📅 08:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84356">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">إصابة مباشرة في مقر دعم البحرين</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84356" target="_blank">📅 08:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84355">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات قرب مقر دعم البحرية في البحرين.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84355" target="_blank">📅 08:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84354">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84354" target="_blank">📅 08:02 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
