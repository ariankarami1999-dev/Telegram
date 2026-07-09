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
<img src="https://cdn4.telesco.pe/file/gz-wUecz-Djl4uYFk3oxa3PaMSdIIgJA0ryb5QO0Mug0yDQ_Z9Qd8F9ik0JxsqC3qBwvbUBFisfAjFrjklRi5mY1TgNpa-_EYH6HqOIHiBfYHF72xKZSzE4fwHncgjkSVEvpkVB-oZOs3oqObd5-stGn6rkMXmHmMVRZCPUdZNO95rkiPqDvPUAbjR9pwV16xLctuhJ4N940ZhKR0lyHdEOHmTPIpQWeM64-VTpi6KjZpPOoTSi_kUBeiWzOfbULadWmcJqn3ijL41zZoRLFLar4q2bVDME0emfMQhQG8BECYKAIj8uNjNIlUXHWFPs1M3x9lAjJnA3uRaKqPZTC1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 198K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 00:30:37</div>
<hr>

<div class="tg-post" id="msg-79865">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">محمد سامتینگ رفته برا تشیع جنازه تو حرم امام رضا، چند نفر ریختن تو سن بزننش که مامورا باهاشون درگیر شدن، صدا سیما هم چند دقیقه پخش زندشو قطع کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/79865" target="_blank">📅 00:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79864">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مراکش عملا زورش نمیرسه طبیعی هم هست ولی فوتباله و هزار و یک اتفاق غیر منتظره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/funhiphop/79864" target="_blank">📅 00:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79863">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یاسین بونو
🔥
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/79863" target="_blank">📅 23:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79862">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تعداد حضورم تو جنگا داره از امام علی هم بیشتر میشه کیرم تو خاورمیانه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/79862" target="_blank">📅 23:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79861">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/79861" target="_blank">📅 23:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79860">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ریدم حاجی فیروز کریمی تو شبکه جم چیکار داره میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/funhiphop/79860" target="_blank">📅 23:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79859">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دکی سه دقیقه دیس دادی به ویناک یه کلوم توش نگفتی نمیخوام پولتو بدم کشیدمش بالا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/funhiphop/79859" target="_blank">📅 23:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79857">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">راستی امشب ایرانو آمریکا نزده، کویت زده</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/79857" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940935d4b2.mp4?token=sAp3PaQ9U_b1TZP3TXeAAsWO5QCPPy8XekR-MyJ4JQOXX9zWMXBeqhAwjIGk76yqmD-aQSzITgdLyT-CUApSywI9pnuh2FaoKusCHJbcQGweTDeX9MAzqZpsolruLuh2yAEIQ-PrZnaDEAgOxidTmsguCEQgWNLaExnji_O_2nhYbenu4VY636VXJXny-vEtTl9B9wSSs7H-EKXxZGsqqIFcdfCuevC6pSsFhlAILtVfE0GxqGwhKylcT_9rW3Yx_3Y9hJnPFd21llln3INGjp6LScCxPkl_QfFAGry5MdV1xhzEv93rKTU5_qJlmR8iKOsdTW3pFJxqY6VqX5pL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940935d4b2.mp4?token=sAp3PaQ9U_b1TZP3TXeAAsWO5QCPPy8XekR-MyJ4JQOXX9zWMXBeqhAwjIGk76yqmD-aQSzITgdLyT-CUApSywI9pnuh2FaoKusCHJbcQGweTDeX9MAzqZpsolruLuh2yAEIQ-PrZnaDEAgOxidTmsguCEQgWNLaExnji_O_2nhYbenu4VY636VXJXny-vEtTl9B9wSSs7H-EKXxZGsqqIFcdfCuevC6pSsFhlAILtVfE0GxqGwhKylcT_9rW3Yx_3Y9hJnPFd21llln3INGjp6LScCxPkl_QfFAGry5MdV1xhzEv93rKTU5_qJlmR8iKOsdTW3pFJxqY6VqX5pL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79853" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/funhiphop/79852" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79851">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حالا کی قراره ویناکو بگیره
هیشکی بک نمیداد بهش هفته ای یه دیس میداد الان که هیچی دیگه</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79851" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79850">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دیس بک دکی به دلو از این دیس بکش بهتر بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79850" target="_blank">📅 22:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79849">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دکی به لیتو: خانومت خوشگله بزی لی تبریک
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/79849" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79848">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79848" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79847">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینو نمیداد سنگین تر بود</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/79847" target="_blank">📅 21:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79846">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79846" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79845">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRYP_LTS_0Z7ZK04PDPMCzo_pov-sqSco6LIC6z9_5BSVpcejQbSCXk_KI38jg0ZRb01gtxMCpKfinSrKn6CFRgBWVvBQ2_zFR59q0x8aJyGdR2C47cKN5Seo0o0gyBo2EuUVPCrJF2YAN5-KQez2DY55LethK0tEuNq0oIRoBt9jR7EvqC0tA4WQlk7YgfE8010f25V68GfsAor4V2o5LqFdYy3XvEPDxcnnRbPeVZE33EtCJpPaEvOwXAdVEUYuRiGBC6uLXLxplC7-7x5rnJvnlvc4Evk8tA7hoaWgC1yoWJRdUSP4mwdi7nZlSJulItZR4iApIZfemQsF5ZkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/79845" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79843">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اف 18 سوپر هورنت اومد با یه ست تابستونی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/funhiphop/79843" target="_blank">📅 21:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79842">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اف 18 سوپر هورنت اومد با یه ست تابستونی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/79842" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79841">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA M i R</strong></div>
<div class="tg-text">پشمام اون داداش کوچیکه هم که میدوئه کاگانه</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79841" target="_blank">📅 21:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79840">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این جنگی که دارن باهاش هایپ میکنن بیفشونو اسمش تو گیم اف ترونز "نبرد حرومزاده ها" بود  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79840" target="_blank">📅 21:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79839">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این جنگی که دارن باهاش هایپ میکنن بیفشونو اسمش تو گیم اف ترونز "نبرد حرومزاده ها" بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/79839" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0c8abffc.mp4?token=shsI_q3AFm4bL7h_NzfYwBthBAUcwIArCS95510NCD-Wz1VsMYMLm53OgGLOqgQ6FP7dW2bCjs2YXNonXh6GX6qV2tClmiQItWZVTieC1_F2yYB0ZTmftamGFOWZvwiuN3Y6w8QNv6R8geHru0qhyXbTkH3GN87klEsqcmHTEwQXM24oTXb1s4RQHuDVNrM1I13JeMCKYzGjDXybmCjSFDoQRsm6G_Q4dQbR_gmxpJvsP-Nm4eLL1oSn_gaMFh9PoQOR4KPuV3VJZ0NHV__bRglIGWzI14QwrucCDCsEWMfSO1J8Y2oKjcpZUntlfEZ0en2asFAIqXbfF6I1d-sTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0c8abffc.mp4?token=shsI_q3AFm4bL7h_NzfYwBthBAUcwIArCS95510NCD-Wz1VsMYMLm53OgGLOqgQ6FP7dW2bCjs2YXNonXh6GX6qV2tClmiQItWZVTieC1_F2yYB0ZTmftamGFOWZvwiuN3Y6w8QNv6R8geHru0qhyXbTkH3GN87klEsqcmHTEwQXM24oTXb1s4RQHuDVNrM1I13JeMCKYzGjDXybmCjSFDoQRsm6G_Q4dQbR_gmxpJvsP-Nm4eLL1oSn_gaMFh9PoQOR4KPuV3VJZ0NHV__bRglIGWzI14QwrucCDCsEWMfSO1J8Y2oKjcpZUntlfEZ0en2asFAIqXbfF6I1d-sTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری جدید دکی، مایل به کاردی 4؟  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/79838" target="_blank">📅 21:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79837">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q67Ktj5przwZSRTzxfyX4P4zHd-ZsziE87B2MWwk-we00s-09nK7C--QJVhscSWlvuVmWC1TkUlHLS63Qh3I2tVHO4UW-S9kr62EJ01lAKlZXmW97xhVNCE2jKRKWNumQWYarMG8oCIyS-pm0p6P-fvg4NgYsGjfE7XllW-7lpFquNiNCw3sNf86ZFP62YPyLhDEligSr7MxW_VAkXkjtrxbb-gv_nVIVEUiC6uj-wPqcsb5qOmdfSbJRBdVmCjyDKl83xSD0PI3eG3WUpkFSc_KsHnUk7PwRNLDslEIvJhlUwUEdg21sYvBtWE4pF4-Fu3ZEaLBfdKljQXf6J6dDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات وعده صادق 284؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79837" target="_blank">📅 20:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">امروز 18 تیر سالگرد اعتراضات سال 78 کوی دانشگاه
و ماه‌گرد قیام 18 دی ماه هست
روح تمام جاویدنامان هر دو اتفاق شاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79836" target="_blank">📅 20:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43dd96db2.mp4?token=NtDe6g2EdCbXHR7sK7gb2YdXEvb42nu_b8lbvzsAbTXUZpbsb25_5rBx7-k8u25r9IbSgsc4PSdtTHRFqA3XWAEuYPhOaHDF60fQanobMJZqwNRHuNaqu13f_YS7k8u-vM4q5SBVmAaxfvmyloUdbixuoQpPb_l-zKeKFyVBJ1zarB4X73VbQvbdbcKl0486_V4WgAe-puQCUWx7SqeHH8xQxUC_HexJc6wGPspP8HC6lPk0CTJQSlqD-P-Nfy5ZWoKAPdnWKn5zvdi6W-6QiIWVXbAvw03-6l2PyJA7LJvoCj3weOgeFl_aOwAfTm3nTIVnwptN2IwtlaudFprZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43dd96db2.mp4?token=NtDe6g2EdCbXHR7sK7gb2YdXEvb42nu_b8lbvzsAbTXUZpbsb25_5rBx7-k8u25r9IbSgsc4PSdtTHRFqA3XWAEuYPhOaHDF60fQanobMJZqwNRHuNaqu13f_YS7k8u-vM4q5SBVmAaxfvmyloUdbixuoQpPb_l-zKeKFyVBJ1zarB4X73VbQvbdbcKl0486_V4WgAe-puQCUWx7SqeHH8xQxUC_HexJc6wGPspP8HC6lPk0CTJQSlqD-P-Nfy5ZWoKAPdnWKn5zvdi6W-6QiIWVXbAvw03-6l2PyJA7LJvoCj3weOgeFl_aOwAfTm3nTIVnwptN2IwtlaudFprZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانیا با ai هم طنز تولید میکنن
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79835" target="_blank">📅 19:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79833">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0-T04O_8-JGn8CrEWy9YFAKwSvVQCDb4aPCHfd44l2Eiv9t3ptIBB1MEwjSAToOKL9Wt5-4HGdjv3Y17xPlE3di-trtDtWLxkN9k9acPK4aFSpE0wGzjLpC8he4ww4MLs8U9v2WAuZjTVRbe5xrFDGkYcdMTpU-kkFHGPj4f08ccDRlh1yu84YdxZsigL3GEwUJ81AXYNH_xodumOOmkxSOUcaGNL7xoiyyOsAreoJA01M8-0QFcLJJJpGbevtk8WgORjXpfWTkLh4gEEHYJanNlNPwQLl8LEk1cncfA_-GXopRo3QRSzThKZCgjjI7IDSgTRofn5aQm3k2no_4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
با Legovpn وصل بمون، همیشه و همه‌جا
✅
سرعت بی‌نظیر برای استریم و گیم
✅
لوکیشن‌های متنوع از سراسر دنیا
✅
قیمت‌هایی که نمی‌تونی رد کنی
✅
پشتیبانی ۲۴ ساعته، ۷ روز هفته
✅
کشبک ۱۰٪ روی هر خرید
🤑
کافیگت رو بگیر، دنیا مال توئه
🌍
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79833" target="_blank">📅 19:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79832">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmEDgHyw5HalNUml6Px-GvMnrUqCZOqnDPV-Roia4MIQMojEdl7A5anTxSK1iTl-C5Cw4Dg6p9wd6LG0ga6gdvKczU_BMxDw-tsT_acWSqh3Y_ttB_59Jfb2XP8Gmlr2dqXY1bWiCP-mU07-xMQ-SL-gIfCk95Y5yLbu0K-ieWkMQozPJgyjZ1WghxdtsTpgqxDXDVZ4GLiyJvhpp2x8IdLixcyypnEoiXGgFHakcnGouUYiBS8SJTrK-RJVuw6WvNRzoQoKOKOj9w2fjjRcl3MSSvlWH55YOWVGHTpda8ILwcqRR2vpdCQGTiQNlwdM_I_Cupmynyvc8sWCpS1ZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید دکی، مایل به کاردی 4؟
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/79832" target="_blank">📅 19:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Esl34l2aL82fbiHbV4PzdjPq_aKweKGscQPiHAcWc5qtcSmtoE9yrfa8CKr1DR0zvhHUX1ZHI7MJpWEbSVZ8A_oxqMJxV-JFv8mCWi9Pv_T-ShnAS30JbVKqp-0B_yrUGZHsXmFh8zm8CFmFZoFUnD6_RBjoxMStSsBtKa8TzetthS3Hj749d8paMPcU6UeksSt2BW4gdwjr7Xe7mE3fHXiG4lw3zD0rA0UL6tvfxedOsNBusdxMMuaeu7JnRn5zkFL755Z5KQ2Ow9QXBsW9GX50MXi2f0K8sKeE6ZqQR7zjEidiBwsGzKHskKE8Z6O1pkiYR4Itmg0rWbSGS04OqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس کامل استوری چادی هوپان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79831" target="_blank">📅 19:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sua4DwztJwRVgn8Iu5jzgmayji6K6FJDxS1nexJa3_Ml7gc5M_qdVuys-ceV5HBS5vCcFr-xglr3npb8aYhOvcqZQHXU-x_ul_SeFzC7MJoU6Y8iYeY3y5xKFrz40_hZKO358tFja5Nzx2G4cEQAh6Z6XUWHcvSsL_bt73xxX_RU91cAHkGQzpI_TUVCX0u3fn7YqJ3w2ZKk3musFWlXLc1k42tYdpvV_FgPOuHYtsW3_iVL6nKG3BGeCrEZ-DHeoeo3azTBDH44wkQypyY_t9r5KaJrw2lEUGoMjB4URhLf09K7U2SvZ2vHJLugELp1cssUibQep0ub1YcurfCUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79830" target="_blank">📅 18:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utpYDiXDhuk5xTwMwL6b6NvYzAN76VxFrrvAOJZpU3yi9Payqae4eOc1Mryh4GWUyE6Y9cCVkyqaji5p0oT1JjvYe3hAGj7kWOMTM6UmI3pir6kzh7O0FzZKSOGfQJcYYoKtIcQVJMAwyg5VAGFmeBYHrFvCIDUnAat0_7UfA31M1Gxo8zFWbKf2Or-gci8GDWDhl7calUm-aBR-f-oqYidtuy60dQcuPIA1zYvpp6qfpjg6ztQCmh7Ig5ZRgByKLloHIdxXyodjUsTMv3rTPIcITNu7LnNI3ti1xJJNQcS2QTeqWdokdPeCrKRHQDexY_oVpo1hIUhlZ7lSWM97qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا
هکتور فورت رفته تو رابطه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79829" target="_blank">📅 17:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79827">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzeLHxquObmPcoJzQFyLCNkDgLgLR9KyTDqfsaDENK1ab2e2Ze5PRjZTZSyu1E01upnzIuImunyu7eW2hTdt__sHko4-fxihUu6xIPH_VEAjrnKYi1vx9CK5LKwrZRWd767Lqq4YMdzV2aujAz-Fs-fhOcKPNjxV7_gDtVXCTjeTcFvay9shhcbDyzDi9EPzxRLELpdOIDiwr7S8Ss562qlvQLrjNKgTueILzaWyZsJ1Be4qHiQVV6FiYC6ssqBaDqaEzxFMgJWjoVBZCZux_C9HyeQPvw82ewH-dINf7AW37nIok9IXFIV8Jd7Cb-S4zE-HT2r_6mjIu3EkFWYmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqUbn7nPIXHkhnyVfW7-4cd09Eqf7O21_4EjPUSKd5rv0e6kjgT4J0mfI7XWCr7nGTnlXWJuJEY6l-HwvdV-_wrpIQTyHCA17dJKjF4hJPUJbjM2nK9beKg-VJeRBaM2ZRu9UxxfAldZ_fmU9yZcMRHBEIeMUhzPEkMXvI_R-0JwnNA1NTq60traoKq45ChgveY0VhxGDQA7iL9agg6uNmsTtakLwy9lfzj48eGH2l2kQTtuRz7PO_hsN_8SvQchRhychiFvVDZpTNeYOBUaZ120Rjb_19FZ-nhqjojPjqG6ib0yOTGnT5ugWgZiUQ8ZJbiAYVc6aubFa3aIsedbnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط لجندا ربط این دوتا تصویر به هم رو میدونن.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79827" target="_blank">📅 17:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79826">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK5KjMez7nKlcAlwv15R4eW4Z9RhUZhX-KnjYpGt6h6jOblv3cTqzgW3tu7XtUVHWcWFj3Iq0QSB_v647qivoHNemwmXA6jhxyW1DlbgkgUfRbsLEg-pVV5kU-Y_w1LYzwlRHvPd6ghpTBPcB33gg7XI-ORrVp7lkBfkuO4seb15tRURNBCBu42IyLfK2x_B0XlInk2gOpFirg8JtYsqwNNkIrcYXvDv86zYqB8iyV-wGBywdkNU0jQMMzFPjMy91apVv-cb96py4pYhNNCvGfx8X0I491Gr-YCPZePgTbDzeBwPRbm80ziHZdQL0Ios1uZYDnJCD3FS4V7sJHkxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
دو هدیه ویژه جام جهانی ۲۰۲۶ (مرحله یک‌چهارم نهایی)
🏆
⚽️
روزانه با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های مرحله یک‌چهارم نهایی جام جهانی ۲۰۲۶، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد در هر روز از رقابت‌ها ۱۰۰ درصد مبلغ پیش‌بینی را تا سقف ۵۰ میلیون ریال به عنوان اعتبار پیش‌بینی رایگان ورزشی و در صورت موفق شدن پیش‌بینی ۳۰ چرخش رایگان ماشین اسلات به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/FWC4
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r18
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79826" target="_blank">📅 17:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79825">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آلبوم جدید ناجی به اسم Nowhere منتشر شد.   Spotify  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79825" target="_blank">📅 16:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79824">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca2C5RnOuZg-54d_u9XELsQEaItmnEK83uYBuxYBzhCQk7462EahgoIPfrlBgkx-IBzqvpKytMKNuPI5Sz089vpufzFSWjilfiQe957Bry2Q9McQ2fQxk36WF6gOEhBMrHpSgTlSCZx-6xlxUcZ_izqHRHjoo8-qJ3FxllpCJPNqJQAwiHmZbYh7uO_iHFvo6FOmb8kwvp7olZfxMtGElNeAJyPrv8BgRtDbenhSXO0-Ez7hvefpbJLfFuLpLAEyekSwm9eYfeuDcVLqnjXF8A5KY5FwHXUhqwdgG66mcgxXopJ9bEabABZoD1a-dmvfFNGPrtpKzUrdI_2z_EJp_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ناجی به اسم Nowhere منتشر شد.
Spotify
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79824" target="_blank">📅 16:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79823">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=KCrlCmiHQjLq1PtA4fSXKcyeBzMSYWoSYbBTZqP26-eThuMAdlvjLl5Pq8KiCx2FfqIDxXQdsU_W5z1C3l6n2IhGciMiOQFDgTILzWf6Eq10oAFlubrVc6Ktr-apkY5pTtTv1butlRe8nLqTcbUw0xCZisGwnGg6QvsXnALltuN8uO8AnvDB95pAvvwnZJjHBByI0YTKU1tuy_urs31S6Q6jvIFDwymMTbnILShLp4O3JmxN5QonuxsYVQI0fj3-o2zJ88CwkHiE_UsffOSzb4SKmWf2jTNEzoaKbKJOR7whvmtoUUrTaBKkkatAm4R3JdGGKM1lc3Kdlush8Rt8cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=KCrlCmiHQjLq1PtA4fSXKcyeBzMSYWoSYbBTZqP26-eThuMAdlvjLl5Pq8KiCx2FfqIDxXQdsU_W5z1C3l6n2IhGciMiOQFDgTILzWf6Eq10oAFlubrVc6Ktr-apkY5pTtTv1butlRe8nLqTcbUw0xCZisGwnGg6QvsXnALltuN8uO8AnvDB95pAvvwnZJjHBByI0YTKU1tuy_urs31S6Q6jvIFDwymMTbnILShLp4O3JmxN5QonuxsYVQI0fj3-o2zJ88CwkHiE_UsffOSzb4SKmWf2jTNEzoaKbKJOR7whvmtoUUrTaBKkkatAm4R3JdGGKM1lc3Kdlush8Rt8cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواپیمای حامل تابوت توسط جنگنده Mig29-ub اسکورت شد، نکته اینجاست که این نسخه آموزشی و فاقد راداره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79823" target="_blank">📅 16:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79822">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اموزش پرورش همچنان میگه امتحانا سر تایمشه در حالی که یه سری از حوضه های امتحانی کنار مراکز نظامی قرار گرفتن و احتمالا درگیری تا چند روز یعنی اولای امتحانات طول بکشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79822" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79821">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJgybNF9OLsXjZ59hg5aufSdJsg_xD93y87x1iRSnJGak7afmxN0Mc5ck-WkhffCIgR63PB_AS6zBZzpu2R76LaDWS46FbsHXGJ6IPVrnPlHElddcQnhQp0K3wn7JtbyoZHOhRjnou687hiipAOZYqpdQZGDEObnDdiNpSr6PTRz_6gS3uKFQt8glMzVpF5WONwopHlZtciEnJoTOfECIG1C6BzQY-ecJOdnCIjvAWzHe9cMt73B8ZoMtFd1mPdsG6vkq1rB2c5j-Crq-Kp4MxoRBrmSbITuosznUKIHMcoxHgaFR7DJgd6nyT1yp9K0wrt0UQG44QatQC1diWJhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این 3 تا هم تو حملات دیشب امریکا به خوزستان کشته شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79821" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79820">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYk_9s1xfMkFDCNKJIedYN4O5K5fOrIy16sjoHyJ08ENwlGbCJQtfOiJItOeXpZVB_54hJtjqC4OF68ILhU4StAqp10jD5iW6dMwK9PlNVxGz67vnUeHmt5jGyfU1SnCYJr5D_of98Kf39-VbQEvoi4UKL9aUOAD_dJuOd9QLbxhYIp0lt3Ep7uAHNg7sm0FYJcidUiyKAVQ3fPl8War_rh33yR0o7PIXPnBULt5qX7VR2Zdehb1VCnTcyFlhSCu-VvC1Mh4LPqjFe4-pJCLSCCATMgDSfWYyj6wfG857Vv43rituALgwj2xifzjjUKOEmP1Ibdklqw2baHl6ZyP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان دکی با موزیک ویدیو ویناک جق میزنه یعنی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79820" target="_blank">📅 16:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79819">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79819" target="_blank">📅 15:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79818">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">درحال حاضر دکی کیر ویناکم نیست</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79818" target="_blank">📅 15:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79817">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79817" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79816">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmZ-xts0mkE125ksndDCQSs2UK6WV_5XhDKIwSRGrzNk8hQMVKiu18UQ27xbHT9xYuXHugy1CkUGtwFh9JgkukOdTVTylcn8ZFA_bvk_lXiDdJRiUT_50J5PN2F7biPEyID_GC5G_8-od4pDytQshde03YOUmzuxSKJfZVyEm8dk4wO5pd63UWqgdOzxVcb8D4ZgyzKP78EZmSHyAJSjsdZRG49G2j6-Vm_Nfobsf6PpkkITRPwCKkdnzZamnI0OwR6NHnHGTpDsHAGilsEx1MqRqesuutad3ZzerZuPbglR8DshChdLXEY_I9k-Yo49v9CjFtJ_yzOssXOI7pqPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79816" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79815">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWQzW8_97_BcJtLdA27sAFo7ZlRQL8TEBF1_StbsnOxH4B-Qxmi363NWLxXaiarbhd-Z5CtCu1wS2zkcyRr108gP52vDSjjBBP2Qvz-3ngcxVDtnReQxf5zJre-Si9KE5bO5eiLjwd49LGum_PlYTa5VKhlynBuv0eXZ5yEpEX2bFrIDBodjR7vLd1WuQtiZBrU6L5C9Lp0zNLgGvq_8TQvBt-CSKBgGgGBcVcwoSa0NNtIdOa1DP0uvD9zswB9AzLU6ySIDckcCbDd8sLB1873ULNX3IPoz_LEtXszjYkNN_oM-yZSQXMNl4wbvrt56r0dKbakWNIemsrQfEvHMFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک ویناک اومد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79815" target="_blank">📅 15:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79814">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">💥
OFFER OF THE DAY | تخفیف شگفت‌انگیز
💥
کاهش شدید قیمت‌ها به پاس همراهی شما؛ از این لحظه تمام  پلن‌ها با نرخ جدید محاسبه میشن:
💲
تعرفه جدید: فقط گیگی ۷,۰۰۰ تومان  سرورهای پرسرعت اختصاصی  پایداری فوق‌العاده بالا  مناسب اینستاگرام، یوتیوب و هوش مصنوعی و گیم…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79814" target="_blank">📅 15:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79813">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp-YrVVPoNaS_W3BYNNUMfms1k4YoY9tMl8Hsf026qeHsmcf1XlB5olnoybwam_pyuEHQM14mb8KIfBuvfqFxD9gFdF9x0T5s2-p8hBk7F2XJyaSfOtZ4ayoI5Jdp5HKaX1uiRVutXhIXtYG6KD4PmoL20bnakf74MSjhWGR63aeWcB68qt5D5Q9Fcpexq16KnMoLTCAdh6upqyQ_6edVF281QjGGr8hdp_tPQN92u4RuTY6z-d1qbK6cj46Mez4SJWIE7Tl2e9uPSl6RAZacd66ur8hjOsYaKKJ_VAwkImtY6C2M8KNKL_1SSyAS5uHesy_dm8Qa9CtNEWa8PXcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امریکا بترس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79813" target="_blank">📅 15:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79812">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتتون ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79812" target="_blank">📅 15:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79810">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEPE1AVIUoZmghVA567HsUZb3AUAilQ74mdxxmOCCb9L6oNzwtk_08o-O6Vv7YWLCFUb_ppCYjG6Bx3A4-XVj9xJHyMWR2BsgeyulABFqQX0DDBouxu4_nDoFd7BPjHhiA3pkPyWZzxjU2vKWFUrptmk7ys8gCcFdgIdVRhzqnNRJ2klPk99WYwbVuARlwLfkBo1vE3PlfPbZijJJbmq4s60SoOIOMS1Y533affrc3_iTuwzY3bvwCWv6Rcwt_7mpzS4N1K9_bVIDLr7C3ig2_OJET_3BSM7GRK-PMXIU_dg20AiVL9HVchodFja-rMYAJ100eBHBk2_PaBLcOVMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قمار باز به صورت زنده در حال تهیه گزارش از اوضاع تنگه هرمز برای صداسیماست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79810" target="_blank">📅 15:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79809">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تو گوگل سرچ کنید erling haaland بعدش چند ثانیه صبر کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79809" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79805">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شاید باورتون نشه ولی آتش بس هنوز نقض نشده</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79805" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79804">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انقدر جنگ دیدم و برام عادی شده که دیگه حتی پمپ بنزین هم نمیرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79804" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79803">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">غزه در زیر بمب ها زندست، غزه با بمب ها نخواهد مرد ولی آن روز میرسد از راه، که بیکینی باتم شخم خواهد خورد  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79803" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آغاز موج 649767667 وعده صادق 27 به سمت پایگاه های استکبار با رمز یا زینب.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79802" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79801">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oss3BzkW2mlwmuKnOiAqofcN-JSKADX0M65grvKY3JQZOjaGzDaUa1pzF3GAexhDAHb2B3UmQAN9lj4ERsDDWOE0ta0RvSEEnpugVkrVcuKPN-3wBxMjzd8N1AHNHpcTQFfk8adoVLLzxe5mfJ1ZdFC31ldvOH-S4pMJsqNUya1-kFnCrNMl4mljg2HwbCsYELL5CJuYAE3gmSnfLgILI2QpkyRf3WYfUruVuFVWYZpC3engWzfgHQ3YRkuCbnCdmgHlqLKHwvQumdsbxyO8Mk0RDqjYZmK1_X7ROu2pSRb0atnXFuA-_kJLXnOZGeD2LkTjYFGv-p1TmysHUK5cTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز قراره کسایی که تو تشییع مشهد شرکت می‌کنن یه پرچم به طول ۵۰ متر رو حمل کنن که روش نوشتن We Will Kill Trump 100%  اگه باقر شاه جلوشون رو نگیره تا قبل از طلوع آفتاب فردا بمب اتم رو خوردیم خدا بخواد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79801" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6hyRQ_7zs3yEvnC9NBzJX6ngytblW9ABmeWBkRlm6Vb4ZnxtHjHiVcJrcNhlAKsGG2OYjuiSZVp4Qca5qwMnRU4gghchms0MNsTyQKAKWvinQp4MOnta9umHcdRvxokiNTEoZ_zs-Jf70ObXCbb0OAL7gCo7Q-oltMZGC0usOXt5ELKOBd6cN0qgBIL9gqwRuMzAIs9iYAn6NI60NIXzuL5nxGN4OIh1HuaQJStORegb5RUJGkItzwMCWwav1i6n2b2Jtu41oAZBEnW729ADafcLzvLm_9vZOAuZuMHVYKNB3J09MltOETgG9fOdTXSF1xZi9Fi-uVnIuvKjz1MQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز قراره کسایی که تو تشییع مشهد شرکت می‌کنن یه پرچم به طول ۵۰ متر رو حمل کنن که روش نوشتن We Will Kill Trump 100%
اگه باقر شاه جلوشون رو نگیره تا قبل از طلوع آفتاب فردا بمب اتم رو خوردیم خدا بخواد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79800" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بوشهرو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79799" target="_blank">📅 13:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989fd48c48.mp4?token=MheHIj6i9qABlq80FRH8fUYPVjRKWJm8THIBmLFu16HJuuns8O-hVN6HEz_WJYOk5owi3WHsApfkRVASVnu7pgGWkk7IdD0u9uZdxVKp6dbWfyaOLg9S8Zdg7Aziri-pN95L0jXy5WVQgpP0NKG3htM0XkyeoA1u7_YGUvLUx9Hvehn7x4HFtpqYb4nBymwa6vn6qLHZy-hhBC-RtavJH6144d69eN5djGuR4nMWPS5ULg6mf3Ne2_QX5XZqne9dJCZYmW_004SaYF2aqp9jSRoE3T-LKS4v5vvgX2T4l5OHyjzrKFnBs0NsD5Jnb2PgblXuxzCLD80M1H4s2QcY3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989fd48c48.mp4?token=MheHIj6i9qABlq80FRH8fUYPVjRKWJm8THIBmLFu16HJuuns8O-hVN6HEz_WJYOk5owi3WHsApfkRVASVnu7pgGWkk7IdD0u9uZdxVKp6dbWfyaOLg9S8Zdg7Aziri-pN95L0jXy5WVQgpP0NKG3htM0XkyeoA1u7_YGUvLUx9Hvehn7x4HFtpqYb4nBymwa6vn6qLHZy-hhBC-RtavJH6144d69eN5djGuR4nMWPS5ULg6mf3Ne2_QX5XZqne9dJCZYmW_004SaYF2aqp9jSRoE3T-LKS4v5vvgX2T4l5OHyjzrKFnBs0NsD5Jnb2PgblXuxzCLD80M1H4s2QcY3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیری مادرکسه ای حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79798" target="_blank">📅 12:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فلیک یجوری داره وینگر و مهاجم میگیره و کیرشو کرده تو دفاع فک کنم بارسا فصل بعد هر بازی ۵ تا میخوره ۶ تا میزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79797" target="_blank">📅 12:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سپاه بحرینو زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79796" target="_blank">📅 11:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ذرتارو با موشک میفرستن خطرناک نیست؟ یهو باز میشه پفیلا میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79795" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c169218f3.mp4?token=ixY_EqVjA6lTSzn7QgVlvhHEbEcd210pLDdf6ShTXtAqGSQkjALOLEKuL2kpm0BkP7Cjm4J8q39WYDAMScj1gbpk_79b8Xn4YJA32zVBNthkDOnqYbwQB_LhlmgkiBJzRmO1v6K7Gq451hwQuhySkS1-_cS0DT06uA4X7GIM4JNV6V0RHJcGcayUXGVLBbHtkXPS3frachbckI5Z1Xgf6-AxdSP4CYCuBwiCiXW03aR1Nsj9rfMtVda2Loh6zk27MFmcH4wbfvhn6ZReI7NZV4WAH9x9xHNCZM9_TTQIRLleCu3HPz2l7F7QYDF2JzJ8XA17M-iIO0uqihUlJ6GpVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c169218f3.mp4?token=ixY_EqVjA6lTSzn7QgVlvhHEbEcd210pLDdf6ShTXtAqGSQkjALOLEKuL2kpm0BkP7Cjm4J8q39WYDAMScj1gbpk_79b8Xn4YJA32zVBNthkDOnqYbwQB_LhlmgkiBJzRmO1v6K7Gq451hwQuhySkS1-_cS0DT06uA4X7GIM4JNV6V0RHJcGcayUXGVLBbHtkXPS3frachbckI5Z1Xgf6-AxdSP4CYCuBwiCiXW03aR1Nsj9rfMtVda2Loh6zk27MFmcH4wbfvhn6ZReI7NZV4WAH9x9xHNCZM9_TTQIRLleCu3HPz2l7F7QYDF2JzJ8XA17M-iIO0uqihUlJ6GpVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه یه دختری بود تتلو شاشیده بود روش؟ حالا اون دختره تو فصل جدید عشق ابدیه بعد با یه پسره دعواش میشه پسره برمیداره میگه حداقل نشاشیدن روم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79794" target="_blank">📅 11:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGaFcgu0Nx4vyHw8t_yPZPsrywEUU5dB3hK58dy4ZltzxLBKCjoSCqI4csH_AXOZjK1EZP_y8oFoO-mgqTVksNySJS78m2MSYiDYFmuzzCxy-sodxscLQGIwCehMfe96uNlY2pgjpeZhYp3w506p2MBF3CaGgpXNVUy9WwIvMMSoyrDme0NOy037B3E9ApQoRZJ5UE9KJkQ2ySnXluUMFsM7hskuyoSLo0Ap5Zh0fwZxJ32FCkeKzr18O30yS0t7w_IDPdQkmZAU7H4saGmCYVWgxzuqkIRVWs_8KvSharLGWDdNo0OF-0oYq1bE-w2ZFKmcrD8OfhQcu-gYoxP9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
دو هدیه ویژه جام جهانی ۲۰۲۶ (مرحله یک‌چهارم نهایی)
🏆
⚽️
روزانه با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های مرحله یک‌چهارم نهایی جام جهانی ۲۰۲۶، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد در هر روز از رقابت‌ها ۱۰۰ درصد مبلغ پیش‌بینی را تا سقف ۵۰ میلیون ریال به عنوان اعتبار پیش‌بینی رایگان ورزشی و در صورت موفق شدن پیش‌بینی ۳۰ چرخش رایگان ماشین اسلات به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/FWC4
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r18
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79793" target="_blank">📅 11:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79792">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این خط ریلی که زدن یکی مهم ترین راهای تبادل کالا ایران روسیه بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79792" target="_blank">📅 11:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79791">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJBYGyWx1oVaFRJ-7aAxMy1iV4fr_0kWb16thIxsnDVIJqKUu_7KnMB2Iudx4or2qO_R69ltcTkKVEqejLSWezpZ9eK2_EPQ_Onn198E2x6V9j0yqC3U7DLwCYNnwFaWlb6Qa7pWPctd2bBuSzKTe6lGE_o1WZK308O0hVqpjXm3rGfgDi2-1t3YofvCvNMAU-OzNCA6xaO2fwZmzKN4DZtCg80Pfi8-You4j2_25pWbrzoIcRjfdKewcirxZavdAP_EL93ArGM-59r7SLo-r69xH7dVqYvROELgpHYJ8hgtjJjTUx0GuIyKhP-pQaywc3pbq7eUNid500FOHNztuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات تأیید شده آمریکا به مناطق ایران شامل: بوشهر، بندر کنگان، بندر لنگه، بندرعباس، سیریک، بندر جاسک، کنارک، چابهار، ایرانشهر، آق قلا در استان گلستان، جزیره قشم، جزیره ابوموسی و جزیره لاوان.
حملات احتمالی آمریکا: چغادک و جزیره کیش.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79791" target="_blank">📅 09:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79790">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34521567c.mp4?token=LrgO54W-WlAi3LoiCXrNqyzQF229DqL2iRH_jli83uVohkBSXBfNMhxi91PcESScPuhj-r7kkxOb6EEV2h5wgLd39X7xJRFY8vJYvGOYmJ3My16PunT3q7hcEDg9CJhhxZhGme7IhFnRv8UmD-qIo5pD69TrvTqNjLsPxED5_mfT7IU3GJMa96OFOvwRbPHh6AZSDvFjw21qgRjpA_6ZbO467Lj1AnDrTdIfldCSLqbKHKRbS2tB1s0Bj2XrQLuPQs0wcr_dz4clCsyBGcAT4-whqrzMISmMzrSm93eg0Vn9JOhVkFAms-RICy3fFo4HSn6ZhOy1SWcPImLbch4dWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34521567c.mp4?token=LrgO54W-WlAi3LoiCXrNqyzQF229DqL2iRH_jli83uVohkBSXBfNMhxi91PcESScPuhj-r7kkxOb6EEV2h5wgLd39X7xJRFY8vJYvGOYmJ3My16PunT3q7hcEDg9CJhhxZhGme7IhFnRv8UmD-qIo5pD69TrvTqNjLsPxED5_mfT7IU3GJMa96OFOvwRbPHh6AZSDvFjw21qgRjpA_6ZbO467Lj1AnDrTdIfldCSLqbKHKRbS2tB1s0Bj2XrQLuPQs0wcr_dz4clCsyBGcAT4-whqrzMISmMzrSm93eg0Vn9JOhVkFAms-RICy3fFo4HSn6ZhOy1SWcPImLbch4dWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 4
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79790" target="_blank">📅 07:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79789">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به بوشهر و چابهار مجدد حمله شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79789" target="_blank">📅 06:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79788">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آغاز موج 649767667 وعده صادق 27 به سمت پایگاه های استکبار با رمز یا زینب.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79788" target="_blank">📅 04:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79787">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آغاز موج 649767667 وعده صادق 27 به سمت پایگاه های استکبار با رمز یا زینب.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79787" target="_blank">📅 04:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79786">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cbv6YHnlXmsB_BiOTSaFPnSgJXREXwTVoMuBxvQ86IiG0jAnzDPGyrYyOMxLkdT0bM0tnt26jSjHHfhWGVqdyrtiwPTSmzlI9jnyJ8eNMN2AcWNTZEuy1xwqQ2LLLqC2wDvKW6iIRxkv-x6rOcYEv9uourWyRqk1aFneTf4gcjOAyyPL9BviIAh4gVZ5tZ2fJQYXJaqHLQMEYcdteff9UNYVU1sDQYCpYBYleRPaCTYawPMzP4dvJiaTtg-tRVDKCQIMXWw6IA6ytEl51ZykGYK8nXi_eKz3RDM-ZevedehCWGi9STCiBaIsPvuK0IdHZqWZtDo4bB4wHVZtZaicXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال رو هم دارن میزنن  گرگان و اق قلا   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/79786" target="_blank">📅 03:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79785">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شمال رو هم دارن میزنن
گرگان و اق قلا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/79785" target="_blank">📅 02:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79784">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بزن بزن تموم شد بیاید بلایسیم  https://t.me/+3BUNQoy8hp5iODE0</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79784" target="_blank">📅 02:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79783">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بزن بزن تموم شد بیاید بلایسیم
https://t.me/+3BUNQoy8hp5iODE0</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79783" target="_blank">📅 02:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79782">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شاید بگید ایرانی فراموش کاره
ولی من بعد سه سال هنوز زیر پستایی که اهورا نیازی توشه کامنت"ناتکوین کی پول میشه؟ هیچوقت" میبینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/79782" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79781">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">خب فعلا اوضاع ارومه بریم خواب خدا را به شماوند بزرگ میسپارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79781" target="_blank">📅 01:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79780">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اماده باش صدرصدی یگان های پدافندی بیکینی باتوم و کویر یهودا برای مقابله با حملات سپاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79780" target="_blank">📅 01:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79779">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/715683a4c7.mp4?token=XcIgTK3ed7orlKlQP0pMlcKaC74otF5JcYZUS7G-kZoSJvOajni-YbGMH2tM7hcNrqc0K1z4QbseoQam73VOwc8qjNCbLHP7Rx2Tj-bZ8mLRgfvaGmlP2Elf4g24qcRhuU0FdWgfCKXXXfw_8mJXvqIyB2nb45yE0v4_DgFZs6Ii-SvIUj_wSf6i1MlrZZcGZXBUd9UOghlUwoew2UfvtPcZspr3SMrzinpu-m77AHdGcpjGfQKACUUukQiTKdzRP0NnH_Kf_Lx4mqbXqEhTkdzR0MLSPtGNAh7LeQkjNCa8ijoICmvGZ-8pYR2_c1cBnM8s-JEizD4X3TIjG_zCKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/715683a4c7.mp4?token=XcIgTK3ed7orlKlQP0pMlcKaC74otF5JcYZUS7G-kZoSJvOajni-YbGMH2tM7hcNrqc0K1z4QbseoQam73VOwc8qjNCbLHP7Rx2Tj-bZ8mLRgfvaGmlP2Elf4g24qcRhuU0FdWgfCKXXXfw_8mJXvqIyB2nb45yE0v4_DgFZs6Ii-SvIUj_wSf6i1MlrZZcGZXBUd9UOghlUwoew2UfvtPcZspr3SMrzinpu-m77AHdGcpjGfQKACUUukQiTKdzRP0NnH_Kf_Lx4mqbXqEhTkdzR0MLSPtGNAh7LeQkjNCa8ijoICmvGZ-8pYR2_c1cBnM8s-JEizD4X3TIjG_zCKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/79779" target="_blank">📅 01:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79778">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یکی از تابوتا رو تو عراق دزدیدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79778" target="_blank">📅 01:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79777">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">محمد سامتینگ کارو جم کرد
ترامپ در مورد ایران: اگر این اتفاق دوباره تکرار شود، عواقب آن بسیار وخیم‌تر خواهد بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79777" target="_blank">📅 01:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79776">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">به من ربطی نداره ولی این تلافیا چشم در برابر چشم نیست، داره کیرشو میکنه تو چشو چالمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79776" target="_blank">📅 01:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79775">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تبپ 110 سلمان فارسی سپاهو تو زاهدان زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79775" target="_blank">📅 01:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79774">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ بین این همه عکس، یه عکس فیک از عملیات امشبو ریپلای کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79774" target="_blank">📅 01:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79773">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رسانه های هر دو طرف خبر از یک ترور هدفمند میدهند، خبرنگار اعزامی فان هیپ هاپ به جنوب می‌گوید هدف ترور چرسی بوده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79773" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79772">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تاکنون ۱۵۰ الا ۲۰۰ حمله از جانب سنتکام به جنوب ایران انجام شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79772" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79771">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کسکشا اروم تر بزنید همشو نمیتونم پوشش بدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79771" target="_blank">📅 01:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79769">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">چغادک بندر لنگه کیش زاهدان زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79769" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79768">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رسانه های هر دو طرف خبر از یک ترور هدفمند میدهند، خبرنگار اعزامی فان هیپ هاپ به جنوب می‌گوید هدف ترور چرسی بوده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79768" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79767">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جاسک هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79767" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79766">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ابوموسی رو هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79766" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79765">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=OHOquQzDZkpYLUwmwOU_1XHnoe8rXkYloSEfzU6qVdyscWkc3CiO7inQUfhwt9qiSQAx2meLkzhNy8-93H1L8rk7HhZDzTwh4ku3tiG9KBfQzZNk9P8W28HNy230QdXwJ_AZMfmX_23Pkrcs9TmmEXorTen0Y48x6V_ZT_UcM7e721kO2JrQreuFZcOkaJWqct1tqLE4-AqZ7IonHlCkDVVWfeLWhcWR-lXjRkSg7T9cmXfHegO7cH3jb1kbQugI5q6GVwiNenopkRFjtwbzu_mlIlVKrD9FxvASSFiPbZmbM1LybsNt5ksbj1iKMBwxR5dOcg8PSndQse4A_G0XbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=OHOquQzDZkpYLUwmwOU_1XHnoe8rXkYloSEfzU6qVdyscWkc3CiO7inQUfhwt9qiSQAx2meLkzhNy8-93H1L8rk7HhZDzTwh4ku3tiG9KBfQzZNk9P8W28HNy230QdXwJ_AZMfmX_23Pkrcs9TmmEXorTen0Y48x6V_ZT_UcM7e721kO2JrQreuFZcOkaJWqct1tqLE4-AqZ7IonHlCkDVVWfeLWhcWR-lXjRkSg7T9cmXfHegO7cH3jb1kbQugI5q6GVwiNenopkRFjtwbzu_mlIlVKrD9FxvASSFiPbZmbM1LybsNt5ksbj1iKMBwxR5dOcg8PSndQse4A_G0XbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چابهار
صدا انفجارو رو داشته باش فقط
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79765" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79763">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPGG3NjlErqJvWL3PdF79s3mPz2pBeeT_iAEq7fzghw-_V_LuFv-LBYrBytytSebAXJTrEURY7UH2cZoeiSS5TjW7tg-Q-A1CqgPxxRPA33bYG7N7yvFmVziYiy_WV424sdUnQUEqqXtd21_5gmSPjR7Ef3Xhj_fXUpDblbhIBClGFBhJS5KoP8DqwG-mbpbc_56oQm8nGYx1cTwfw1bFlFU27aN3e0x4l9BC18FKTu4bB8sKIm170hsKpphocPWAd4JNNkx1f6yRkcs4ivHSiXysQtmaf9F4dtM3X3ITXHUCx792of86aLdtAHqNpoqbblqdt4bPx_K7qBqsHYOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه برق چابهار رو زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79763" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79760">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الان هیچکس تو دنیا اندازه دانش آموز و دانشجویی که امتحان داره دوس نداره جنگ شه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79760" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79759">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">از دیشب گسترده تر میزنن
تقریبا کل خط ساحلی جنوبو دارن میکوبن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79759" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79758">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جنوبیا تاماهاک مشکوک دیدید گزارش بدید
113
114
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79758" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79757">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">از صنعت دریایی ایران دیگه کم کم داره یه خاطره میمونه، همشو زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79757" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79756">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فرداشب رسیدن تهران محمد سامتینگ حرکت کن</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79756" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79755">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بوشهر زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79755" target="_blank">📅 23:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79754">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سنتکام: کشتی زدن مام زدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79754" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79753">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خارگ زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79753" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79752">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پادگان ارتش تو کنارکو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79752" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79751">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">به پایگاه امام علی در چابهار حمله شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79751" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
