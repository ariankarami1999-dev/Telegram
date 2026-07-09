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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 22:35:41</div>
<hr>

<div class="tg-post" id="msg-79857">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">راستی امشب ایرانو آمریکا نزده، کویت زده</div>
<div class="tg-footer">👁️ 315 · <a href="https://t.me/funhiphop/79857" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79856">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نه بزارید بک بده، همون بزنید چالش کن</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/funhiphop/79856" target="_blank">📅 22:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79854">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-poll">
<h4>📊 خیلی ضعیف بود بنویسم الان دیسو یا چیپس؟</h4>
<ul>
<li>✓ چیپس</li>
<li>✓ چالش کن</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/funhiphop/79854" target="_blank">📅 22:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79853">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940935d4b2.mp4?token=sAp3PaQ9U_b1TZP3TXeAAsWO5QCPPy8XekR-MyJ4JQOXX9zWMXBeqhAwjIGk76yqmD-aQSzITgdLyT-CUApSywI9pnuh2FaoKusCHJbcQGweTDeX9MAzqZpsolruLuh2yAEIQ-PrZnaDEAgOxidTmsguCEQgWNLaExnji_O_2nhYbenu4VY636VXJXny-vEtTl9B9wSSs7H-EKXxZGsqqIFcdfCuevC6pSsFhlAILtVfE0GxqGwhKylcT_9rW3Yx_3Y9hJnPFd21llln3INGjp6LScCxPkl_QfFAGry5MdV1xhzEv93rKTU5_qJlmR8iKOsdTW3pFJxqY6VqX5pL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940935d4b2.mp4?token=sAp3PaQ9U_b1TZP3TXeAAsWO5QCPPy8XekR-MyJ4JQOXX9zWMXBeqhAwjIGk76yqmD-aQSzITgdLyT-CUApSywI9pnuh2FaoKusCHJbcQGweTDeX9MAzqZpsolruLuh2yAEIQ-PrZnaDEAgOxidTmsguCEQgWNLaExnji_O_2nhYbenu4VY636VXJXny-vEtTl9B9wSSs7H-EKXxZGsqqIFcdfCuevC6pSsFhlAILtVfE0GxqGwhKylcT_9rW3Yx_3Y9hJnPFd21llln3INGjp6LScCxPkl_QfFAGry5MdV1xhzEv93rKTU5_qJlmR8iKOsdTW3pFJxqY6VqX5pL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/funhiphop/79853" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79852">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/79852" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79851">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حالا کی قراره ویناکو بگیره
هیشکی بک نمیداد بهش هفته ای یه دیس میداد الان که هیچی دیگه</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/funhiphop/79851" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79850">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دیس بک دکی به دلو از این دیس بکش بهتر بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/funhiphop/79850" target="_blank">📅 22:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79849">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دکی به لیتو: خانومت خوشگله بزی لی تبریک
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/funhiphop/79849" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79848">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/79848" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79847">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینو نمیداد سنگین تر بود</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/79847" target="_blank">📅 21:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79846">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/79846" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79845">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRYP_LTS_0Z7ZK04PDPMCzo_pov-sqSco6LIC6z9_5BSVpcejQbSCXk_KI38jg0ZRb01gtxMCpKfinSrKn6CFRgBWVvBQ2_zFR59q0x8aJyGdR2C47cKN5Seo0o0gyBo2EuUVPCrJF2YAN5-KQez2DY55LethK0tEuNq0oIRoBt9jR7EvqC0tA4WQlk7YgfE8010f25V68GfsAor4V2o5LqFdYy3XvEPDxcnnRbPeVZE33EtCJpPaEvOwXAdVEUYuRiGBC6uLXLxplC7-7x5rnJvnlvc4Evk8tA7hoaWgC1yoWJRdUSP4mwdi7nZlSJulItZR4iApIZfemQsF5ZkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/funhiphop/79845" target="_blank">📅 21:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79843">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اف 18 سوپر هورنت اومد با یه ست تابستونی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/79843" target="_blank">📅 21:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79842">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اف 18 سوپر هورنت اومد با یه ست تابستونی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/79842" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79841">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA M i R</strong></div>
<div class="tg-text">پشمام اون داداش کوچیکه هم که میدوئه کاگانه</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/funhiphop/79841" target="_blank">📅 21:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79840">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این جنگی که دارن باهاش هایپ میکنن بیفشونو اسمش تو گیم اف ترونز "نبرد حرومزاده ها" بود  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/funhiphop/79840" target="_blank">📅 21:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79839">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این جنگی که دارن باهاش هایپ میکنن بیفشونو اسمش تو گیم اف ترونز "نبرد حرومزاده ها" بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/funhiphop/79839" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79838">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b0c8abffc.mp4?token=shsI_q3AFm4bL7h_NzfYwBthBAUcwIArCS95510NCD-Wz1VsMYMLm53OgGLOqgQ6FP7dW2bCjs2YXNonXh6GX6qV2tClmiQItWZVTieC1_F2yYB0ZTmftamGFOWZvwiuN3Y6w8QNv6R8geHru0qhyXbTkH3GN87klEsqcmHTEwQXM24oTXb1s4RQHuDVNrM1I13JeMCKYzGjDXybmCjSFDoQRsm6G_Q4dQbR_gmxpJvsP-Nm4eLL1oSn_gaMFh9PoQOR4KPuV3VJZ0NHV__bRglIGWzI14QwrucCDCsEWMfSO1J8Y2oKjcpZUntlfEZ0en2asFAIqXbfF6I1d-sTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b0c8abffc.mp4?token=shsI_q3AFm4bL7h_NzfYwBthBAUcwIArCS95510NCD-Wz1VsMYMLm53OgGLOqgQ6FP7dW2bCjs2YXNonXh6GX6qV2tClmiQItWZVTieC1_F2yYB0ZTmftamGFOWZvwiuN3Y6w8QNv6R8geHru0qhyXbTkH3GN87klEsqcmHTEwQXM24oTXb1s4RQHuDVNrM1I13JeMCKYzGjDXybmCjSFDoQRsm6G_Q4dQbR_gmxpJvsP-Nm4eLL1oSn_gaMFh9PoQOR4KPuV3VJZ0NHV__bRglIGWzI14QwrucCDCsEWMfSO1J8Y2oKjcpZUntlfEZ0en2asFAIqXbfF6I1d-sTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری جدید دکی، مایل به کاردی 4؟  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/funhiphop/79838" target="_blank">📅 21:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79837">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q67Ktj5przwZSRTzxfyX4P4zHd-ZsziE87B2MWwk-we00s-09nK7C--QJVhscSWlvuVmWC1TkUlHLS63Qh3I2tVHO4UW-S9kr62EJ01lAKlZXmW97xhVNCE2jKRKWNumQWYarMG8oCIyS-pm0p6P-fvg4NgYsGjfE7XllW-7lpFquNiNCw3sNf86ZFP62YPyLhDEligSr7MxW_VAkXkjtrxbb-gv_nVIVEUiC6uj-wPqcsb5qOmdfSbJRBdVmCjyDKl83xSD0PI3eG3WUpkFSc_KsHnUk7PwRNLDslEIvJhlUwUEdg21sYvBtWE4pF4-Fu3ZEaLBfdKljQXf6J6dDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات وعده صادق 284؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/funhiphop/79837" target="_blank">📅 20:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79836">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">امروز 18 تیر سالگرد اعتراضات سال 78 کوی دانشگاه
و ماه‌گرد قیام 18 دی ماه هست
روح تمام جاویدنامان هر دو اتفاق شاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/79836" target="_blank">📅 20:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79835">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/79835" target="_blank">📅 19:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79833">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/79833" target="_blank">📅 19:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79832">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gie7HKhFByqiYH59rktk-POrdzPk7AsQXzjM0PbARsHfdXPqO3tOE4lnsT7IR5LkZH3w9UHaaC9XkznHgUYia8a3LTyTk8YubST5Q9-dnwby9Cwn-wccarkyOs-bF7Al9pJcCWjW7UtpEK-bIns0n_oHF0NjYD5f8pC9QZyQ4C9xvrB3Qqq-QVIHMTEplg5LpHc6AiotPyWYEqFgiRCs_t77YqXUTZzjWXU9D6v5ANV_5CcWzaefn8kmwSBOP2V2XRmvR0BqVuseLsixcO3PYwOlTEzYHOG5vDrj6xGwMVIukDaYRa5F8UnuuaUurH_IiEZaENHYbpVEETtMyZDWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید دکی، مایل به کاردی 4؟
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79832" target="_blank">📅 19:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79831">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHnRKy_L8qcMBjrXnIBEFkZXdcdlxizurToZg-nO2igHFyOSJscQ1x9A_PibZKyxu7-FTXDCoQTQqHtDmwtTYPZA2GIzeEhg0BkTd589oUffsL6YqCIbd9USFyP23w_ySUkJ99zMqAHWX24IMTY8CkQ2OiBLddVQayr3nHeyw36kJNPBEp5c25oPVh_flQWfCk3t0-mPZGLJyMc_y5xGpj876AajcQrRcXJDvnuBIBPOHFktMJGO0MFptEORhivHhVC_kfmXiO4bAIL2uTXk9wTL4wtGtpOo-Lw4L1K-3bIXEI4Wik69WmNxAmlG35ev9zcAkphYp0SkyA9giQ4xHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس کامل استوری چادی هوپان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79831" target="_blank">📅 19:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79830">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLIloAn4Iemt8ln7ce-rOjVXwc1T5GlCe069qA-JrmirCp6QUM143aqTcvQwGm_60ODD2-QrGhGZQ4KjJ2ip20CKruIxA0Voy9TywJsUS9EwhfqxStNQU_NRdHkBVig-o78Dr6YUmZ0dhKvH60TZ7efxqt9qiC0IzpGFl3xR-OPUQ1wasE6DSvxLCJgDtSxfacLjbBhXpxkYv1pftXW5Y4t95clpfQp5YVzgoxzA3LLYdoypkjDhPZo4JzJRuB5xwJYHfNaNvg7PAwDEalajyOS9YUh_mEchz1T9F24LXM2eLjOMI8K1xxOMOhgu8enI51EA_O-ZqiUcsHcz9QgZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79830" target="_blank">📅 18:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79829">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggQf1TLYCkmPVSKeAxsT41cI0JSftaBEvTwr-AodFqcAZQCuytNMW1fryMzrSy4a9Eu9GpEN7xZ38iGEg3EFYmKqwQchL1TfB8Ttrsg6Yn2qHnzLlxCWm8c40cXvpQnT69N9Bedr2ED6_hfV_oE1pibGKZjDWis1742Itp97rtUtvqt7sgreSCtj7YWw5xttM0aLot9CHdtBLdNJ9SnIvpZUFpyI_742v6eGXabUvAx_W9D0rHVDTH6R68tfji5xnsD_2h7G3q6p_CnmDbYCaRljkAWQR-0wxEsf4zX_RosOz5pq7l9Qvt6lmLELumWQiZwSzaCduBeA4ArXaOGv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا
هکتور فورت رفته تو رابطه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79829" target="_blank">📅 17:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79827">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SyMjqS11usyKBAA_Rgy5553XEsEu3oMnQGsneNi1UjF0BEhN3mHB7RqGe_VGiC1bk_pMB0jTYysKolSOUy1bTZHBkCTjzXUhs2kN-6F-AVE6mXLAeT66V4kpGsqxW7dYKa8mV2GC8lqXNRM1b3s6W6Mez40rPelRQL_RG-Omr2UR1YCrdOt6EjbaFBecckDO63YQPBRRUNxptcIIsn1KsVDe9sJaugt7Rg4s4dh8zXCoXSwQVhNMXnvgf31EvUNTYixoEA40S1FVuHUUGt8sEDvZyoXoKMzj_Wqoemjp828O67xuA18yfkPrKf99j91AUArbeq9Wbr5-ZU3KvEfybA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFPGTRbqCMGdcdWdC5cEWB61_K0rnA2Ejvwhvbf3KaOm9Kmfub4wZcRCXeTqKm1eS40n25JCbK8Osn9KqFjNqFesFUUJ0MztRDHWflYW2-8N2zeI9o7jjcixiqBU_piZYBpJZadSir_0j5A91P9gOkLZMMr2F1Elm3zmXd9EzLPWHnlNZeyK6rAbTKIjrYyl2NRZOWPk1b9xldmTijoJy2XVApyAFGa9yKhYA-n22Wh41dybJ5kh5RV604Ig8xmIS7_lnC99Ln-ws1TduD95cS6-l9MTHUu_y5rP0bBN3orZ3WZje7K-svHvfuqxE_LXjvVC9JH1QoIWHKSI8D44PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط لجندا ربط این دوتا تصویر به هم رو میدونن.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79827" target="_blank">📅 17:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79826">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP7c7qsUgF0HaDULI8yV0h1sunKiLTb4VhDCC11u7WbAE3neOIBJ8bIq7JRT593xGT-DYK-_pcUCtKFN6PPYjFk6lR1DTNtRQg2yYm2TqW1_LuWtUxYRqS-9tKbTJYX1oFYup9w1uJXS9o_TT2pby598tRmKCsl63rmlJyYCvW8gbvPyu7HQYJuo8GrNgasIE6gPyY1y2P_QYLcrWxQnAK9C__AynJV5ihZ6ydDblMgCb0bzpYU-9Jo_c_Fbl0lFi1OujsL5MXqq5CjTPxnyB70QBlqq6ZbKrOpOOqOxZ-aRwbOL2_2z1_xdc89TWffZDztg5poZhOlCc2_llSm9wQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/79826" target="_blank">📅 17:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79825">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آلبوم جدید ناجی به اسم Nowhere منتشر شد.   Spotify  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79825" target="_blank">📅 16:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79824">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkENBTqOboPrGjoECBDB4IeEBugtVXcBYZw8ZpRT3b3d21id-z-o1rvxX931h7uXlWKUmkvNrvACsq2BsyuB_QaksbIg5du4_b8M1esjN6HQC2NE4iME3kOWs_uT7mpJvKDW4OvxAphSjYRKYMMv71WXy-FWMMznhx-NDckVv34wl4hTMnSzW5AQfQb7DtPqTlHMYHWIG9YQlJT6NrI93eP9sI2THL6ZromOFNgTnL1e5sG4NGcbodsGUYUE-NikrUWVY-DuK3ibPL2OAmFZkp60yxqLU2k9QtFvbaC9-9S5xrTunSLKz0kqtXbELAnZpzmmNOWB2_k5NynCryjGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ناجی به اسم Nowhere منتشر شد.
Spotify
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79824" target="_blank">📅 16:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79823">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=PxO2yMF14vF3VXPkRSpaAwzUUiivmQNb2yxNLutegqMPERt0JCcXI5xTV79Kc1nx1H9auKl6awOh5QUxrdoI2HfGyXJKUtUKtFwyLTjv0Zyxz0-Wyiw7KawvgpoNuqG0hMfnqx6PZNRqKKrnTNAnri2Uw8FYIBc53aMR3bXnaca7FrmJXZVFBYDHVaEAm351Iz2em1bkC7Y55VizNy2nMrttjLzOPAgt6skvUX-MBiYPw-NloQVipRXeXa-DpMTmEhvlrzEzVoynyf3DYcQfzEzL60W73ZfPRC4zAQIUvCLFT4p-jyxrNjziv3hdCA2RN3tcHmgVyRnRVA8UHe1sIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=PxO2yMF14vF3VXPkRSpaAwzUUiivmQNb2yxNLutegqMPERt0JCcXI5xTV79Kc1nx1H9auKl6awOh5QUxrdoI2HfGyXJKUtUKtFwyLTjv0Zyxz0-Wyiw7KawvgpoNuqG0hMfnqx6PZNRqKKrnTNAnri2Uw8FYIBc53aMR3bXnaca7FrmJXZVFBYDHVaEAm351Iz2em1bkC7Y55VizNy2nMrttjLzOPAgt6skvUX-MBiYPw-NloQVipRXeXa-DpMTmEhvlrzEzVoynyf3DYcQfzEzL60W73ZfPRC4zAQIUvCLFT4p-jyxrNjziv3hdCA2RN3tcHmgVyRnRVA8UHe1sIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواپیمای حامل تابوت توسط جنگنده Mig29-ub اسکورت شد، نکته اینجاست که این نسخه آموزشی و فاقد راداره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/79823" target="_blank">📅 16:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79822">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اموزش پرورش همچنان میگه امتحانا سر تایمشه در حالی که یه سری از حوضه های امتحانی کنار مراکز نظامی قرار گرفتن و احتمالا درگیری تا چند روز یعنی اولای امتحانات طول بکشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79822" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79821">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivz6JXIF7OAgiD0XEpEEGFYZjIHcbr8zPSh_tdeVnV8j7fUAoHisiPeOWIExq4Cz5_qiBNCevMlJiIKxiY1movtCEpmw2QlbMKlFIuiTvpzSbG2KTnQSKwtXM3FmB0AD87xn596HdVNEEIcDnLxPMUzR4XzE-ypZDIKUKu5cfqG5Pw8_ZIYJ1S5Pnpq1_6_gBO2BQeYiyQ-mqrp9hTpIXlkHvW3i0Sj3MpbHodOSMNScu5PZIEtZ9yOay54VPEaGcW6_pH5KB0UM2OTYRg9jVQaaTEZdRnUZDO61IRE_HqRk-q4syXTnNB-S-h5k6CaProyveTjzsnb2atCz2_MgTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این 3 تا هم تو حملات دیشب امریکا به خوزستان کشته شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79821" target="_blank">📅 16:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79820">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYk_9s1xfMkFDCNKJIedYN4O5K5fOrIy16sjoHyJ08ENwlGbCJQtfOiJItOeXpZVB_54hJtjqC4OF68ILhU4StAqp10jD5iW6dMwK9PlNVxGz67vnUeHmt5jGyfU1SnCYJr5D_of98Kf39-VbQEvoi4UKL9aUOAD_dJuOd9QLbxhYIp0lt3Ep7uAHNg7sm0FYJcidUiyKAVQ3fPl8War_rh33yR0o7PIXPnBULt5qX7VR2Zdehb1VCnTcyFlhSCu-VvC1Mh4LPqjFe4-pJCLSCCATMgDSfWYyj6wfG857Vv43rituALgwj2xifzjjUKOEmP1Ibdklqw2baHl6ZyP1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان دکی با موزیک ویدیو ویناک جق میزنه یعنی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79820" target="_blank">📅 16:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79819">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79819" target="_blank">📅 15:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79818">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">درحال حاضر دکی کیر ویناکم نیست</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79818" target="_blank">📅 15:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79817">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79817" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79816">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM6EtFNKCeJ21teJClAAbcEmY50FAgnvyGH2IP5TdbpEtyL5g4jJ2Sg9mbVjObqjjkAg1FRrEvQsgN2VJRuyK7cqJ58pW6ffXXvI-V3hZ_vlosRkowiEz5GRy28e-SZI2mvkCKg3p5r8ybYN2O3oGABLsc9N8IZ86iji0BuOQ_z8siAmEs5jJxc-5h2ZphGtsUT6cRWOjPq1dwwununYi-OSzBHRS4pVIpfgON9-ruXk7iPaAYKQEoPExdWNQywP6ZWIVtnskz_zp589xlDqqaX_BmQWQH1aF7Z-5BHwOxhQ7OcRxOGoY3VQgvsw8JrmCw88TP5JXtJ4on_7QZjMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "بلاد گنگ" منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79816" target="_blank">📅 15:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79815">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWeZd0TU7njAk4ZuCE77gtPYIsDf875IaBTERE_xakUFjcxkXGBYNKh69ixk7CjeKV0M38QKqkI7yR0oAQUvkmEklMherYOSqrZ8XugMZQQK0yLTPLAk7U8pd7M5NnBQhytABYSZJAM6BZdTpMjTg8txiTBuxdMrIAEBuKNjfWA5oJmmz_dCUTFX4WpovKd4BCkZyFmevqvIPmma2hQtEDHlhgrrHKyMwjgLmzaCcbJ4Y2uN9H2wnI9yhj0Xkm-v0ebOuyHEupVUXK6e-yGUGdjGEl9oAyf6wC23tIGhQrbHSYiv415Y3dIXkN543Mh--xK5aHbJmSEJ6GeJdToupw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک ویناک اومد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79815" target="_blank">📅 15:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79814">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">💥
OFFER OF THE DAY | تخفیف شگفت‌انگیز
💥
کاهش شدید قیمت‌ها به پاس همراهی شما؛ از این لحظه تمام  پلن‌ها با نرخ جدید محاسبه میشن:
💲
تعرفه جدید: فقط گیگی ۷,۰۰۰ تومان  سرورهای پرسرعت اختصاصی  پایداری فوق‌العاده بالا  مناسب اینستاگرام، یوتیوب و هوش مصنوعی و گیم…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79814" target="_blank">📅 15:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79813">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCYZhi3ynukOXqH1U7KtZPjbqlJazHRgds1zioYCdrJ8th5b1I14cfBecwFSYKB36kDSgwGs5X92GulTClQI-ESPxiUjCD63iF07faYWDT9h0K9u2usC3pi1Re5D3g5ERcmSbEq_Mac_yoBAaIkedekbXnIOabq8X65ICeRU4SO76AeYvkde2I89GdztP-qP31yxC1n8BexkoPVRnxE6freBcqD1DVVVhz7jCLbM3Z5v0xbRa_Ahd3fxCFEsN6b_4prsZxwxJgguADU5hvZm7M1oEBp-kWtsyrCSBcZTYO4wAiD2c_VdHP-AgqqlVQ3CWIBhYH48PfhZZfo20Eu6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امریکا بترس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79813" target="_blank">📅 15:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79812">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نتتون ضعیف شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79812" target="_blank">📅 15:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79810">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX7_4v7vWx3LBZdYUl-Dc65gD-N3ljuGgn-elsCCMr92V4AF3gd61cNkvL_4g_0EGZjVj5I2xdytqaJju33US8H1sSx5UJIMiQL0Yr4IN9mveVJgRzr3-V2_ijp1-dij71ou-dPaDSCfI0nBHjigH_yJIhr_44kFnflLYnX5qDvQ_J9EQfKGadwaRdol6oQEZJcEKY5wwlGNTwVWVu0wswGsDzEIcOpncM9oaWNjjQ_puf3kvQCcFNR1BUw4FquMDYwdnNG34u-iLmyTbarJS2Au-wcG7H674-U3u3yfZEXvm2UUJsGO55ue0ejvTV9L-dPn9CmFaiZccwB22FGrLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قمار باز به صورت زنده در حال تهیه گزارش از اوضاع تنگه هرمز برای صداسیماست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79810" target="_blank">📅 15:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79809">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تو گوگل سرچ کنید erling haaland بعدش چند ثانیه صبر کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79809" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79805">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شاید باورتون نشه ولی آتش بس هنوز نقض نشده</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79805" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79804">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انقدر جنگ دیدم و برام عادی شده که دیگه حتی پمپ بنزین هم نمیرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79804" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79803">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">غزه در زیر بمب ها زندست، غزه با بمب ها نخواهد مرد ولی آن روز میرسد از راه، که بیکینی باتم شخم خواهد خورد  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79803" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79802">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آغاز موج 649767667 وعده صادق 27 به سمت پایگاه های استکبار با رمز یا زینب.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79802" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJJ1185lrzb-hHUqoBJ3XaTBwaiyYDS-ijC3tEyK99VcmT1hr6Xq8q5hjFtB7UytSggQpWZG5fmMlMD4n6CTXSTOKS-7Ec8AWFd2DrZ8brhCsLL36wb7HYdrL2_LwsJIZUjyp44YHzThvJlcMrt_R5EqwskG4UQ1N9zhjI6yFGWT4-zfHlHeeTL2qrn6BMj9LhUNdn5cP5u8I5ALsvPtAiyKKmjJ4Mqlv5yV2MhZqWxX8blByJR7h8IeC3JZfR0Lxe6KF8ORxV56fahZUnFnwBIny-iCu26p0Nd0uAU0i0iGII5MPpJ2xw8tRsENFFn2ft7mMmp9xr8iSVrpG5X-Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز قراره کسایی که تو تشییع مشهد شرکت می‌کنن یه پرچم به طول ۵۰ متر رو حمل کنن که روش نوشتن We Will Kill Trump 100%  اگه باقر شاه جلوشون رو نگیره تا قبل از طلوع آفتاب فردا بمب اتم رو خوردیم خدا بخواد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79801" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgXVQ6ssY9FkdO6OVf2sJEDqiit_0M_ys2yDZTqW65wHRYtnnOmlNKRPuaRiX7v3Td9YXdszDGXHvHeZvqblVC5Rexk7LJtp9XTpCMDAoGVrU1-OzK47pjzRLdX3p39t68WBq0po8pn8J-CR2wiqEEquCE96SXEa8du0qG5KvxLiawMDOgb0M6WgviMA5wRoxuanIIF_uYWnJZiSQWFqtB6wSXBhn5TBtYyKRAdgCKZNhffK-KvoWajGidgOFq0IzHvZCZSpL2lIwuwLtLHEn2r2wa2O_EPhc6h-_j5GB4vWAHeKy62YO7zYmBe2O9KiPgzLp34D8pzCB-RD3FVLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز قراره کسایی که تو تشییع مشهد شرکت می‌کنن یه پرچم به طول ۵۰ متر رو حمل کنن که روش نوشتن We Will Kill Trump 100%
اگه باقر شاه جلوشون رو نگیره تا قبل از طلوع آفتاب فردا بمب اتم رو خوردیم خدا بخواد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79800" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بوشهرو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79799" target="_blank">📅 13:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989fd48c48.mp4?token=aLC2Ixsz1i0x46h0R8ss4qikHN0SvWof80DMMBYGDYmFjCQd5RedBr984-JUAeSuzOPeYY3k52yJ_f-2MnLzbJYn9MLUxOT5Rb68Qz-dyy8MdXTjO1DrzSvf93oGZGylBF4BeU71oKW-W0b4GZ9iixWwrr6ZmFumeZ0nqtVV6r4cHWoGABtE0cqim9X7-cfK2FExFSTgd5cNkqMNEBD7k5rkCvl9p9yrfXjR_RsQ-mL3mR6hk-wshKmqU28MACZsYE815sXDIkixexfLQcifDhFDcBlyqd0tX8FA6RzRMol5c0MnOfjuvzcRwj9b1jQriQutX9jYaV0FsmAfy1Qxqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989fd48c48.mp4?token=aLC2Ixsz1i0x46h0R8ss4qikHN0SvWof80DMMBYGDYmFjCQd5RedBr984-JUAeSuzOPeYY3k52yJ_f-2MnLzbJYn9MLUxOT5Rb68Qz-dyy8MdXTjO1DrzSvf93oGZGylBF4BeU71oKW-W0b4GZ9iixWwrr6ZmFumeZ0nqtVV6r4cHWoGABtE0cqim9X7-cfK2FExFSTgd5cNkqMNEBD7k5rkCvl9p9yrfXjR_RsQ-mL3mR6hk-wshKmqU28MACZsYE815sXDIkixexfLQcifDhFDcBlyqd0tX8FA6RzRMol5c0MnOfjuvzcRwj9b1jQriQutX9jYaV0FsmAfy1Qxqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیری مادرکسه ای حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79798" target="_blank">📅 12:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فلیک یجوری داره وینگر و مهاجم میگیره و کیرشو کرده تو دفاع فک کنم بارسا فصل بعد هر بازی ۵ تا میخوره ۶ تا میزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79797" target="_blank">📅 12:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سپاه بحرینو زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79796" target="_blank">📅 11:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79795">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ذرتارو با موشک میفرستن خطرناک نیست؟ یهو باز میشه پفیلا میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79795" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79794">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c169218f3.mp4?token=dE8jbNk4ACkECK5nAMyLDkZvDg3ZwPDuduonNJjeYRlIjfLP5Dqar2KI3n9GdIZy_J-cllHCEY0sDrvNxyne_0XD2f7A_OCRZlvYr8ztEdQxKp_-LzQs7beG-MA_YDCeLWMh7Xc3_Wmwz4ZUa_56yWs2NdTM_yAxcwZkzuUiTLIiLu3k847ciH9P2lX2HcLlPVTava-wqnKmB-fs7E8n-QxBhaqHbTOoKH1Mxu4mx90kymGEsqRiFkauUIDv9uWCUg0_XrRjr6EHGQxGEXMXKTB28EJdJM3alLxpVwb-JLymchuWh6CaJDGlhAyLfnJ2cIJpi9Jk58krEIZ9CE1sNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c169218f3.mp4?token=dE8jbNk4ACkECK5nAMyLDkZvDg3ZwPDuduonNJjeYRlIjfLP5Dqar2KI3n9GdIZy_J-cllHCEY0sDrvNxyne_0XD2f7A_OCRZlvYr8ztEdQxKp_-LzQs7beG-MA_YDCeLWMh7Xc3_Wmwz4ZUa_56yWs2NdTM_yAxcwZkzuUiTLIiLu3k847ciH9P2lX2HcLlPVTava-wqnKmB-fs7E8n-QxBhaqHbTOoKH1Mxu4mx90kymGEsqRiFkauUIDv9uWCUg0_XrRjr6EHGQxGEXMXKTB28EJdJM3alLxpVwb-JLymchuWh6CaJDGlhAyLfnJ2cIJpi9Jk58krEIZ9CE1sNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه یه دختری بود تتلو شاشیده بود روش؟ حالا اون دختره تو فصل جدید عشق ابدیه بعد با یه پسره دعواش میشه پسره برمیداره میگه حداقل نشاشیدن روم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79794" target="_blank">📅 11:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79793">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4-lsjwq7-T-eyli-7qsbEsjPHlhdEJBlWxP_OsYOA6BVzZz7hmSDYb234UbPRdqWTRi_K9gJUj5Nf68EQPRvYEJCu0ipX-iOlbp-ajMEtkpvNDFBlcSzqDifix-amZMNqSkhoJ1tl_JWncgnaVo6xw7lxp-bhnG0ITpmLTnp7iDDXwei79WZUPFBPnJ6Lk2qISfsGQTmzJplLvdDhrT1YTerz-YrLDtZ7D35dakFtNcg1qCDEkYMXWvgYPC5J_DKd0bzuEXwGO5lQHEzervRU91AlirabQv_OczuEFN3zXwAKyQsZJneq03hwgdfepRK1-d8YaezJudtTXirHMjDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79793" target="_blank">📅 11:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79792">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این خط ریلی که زدن یکی مهم ترین راهای تبادل کالا ایران روسیه بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79792" target="_blank">📅 11:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79791">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQ_aRen3fY8cMweuNzO0bje3HfVBuA4siM-N-LxNfp_KN83TYdWbxegbtU5lUZhTDEVoU9AB4gonVqQ0BY8toQpifSkmSY6UBwaqsQFncODOUIJ_Ay6S5E_1OMOMrEjIn3DSqhJwqzYKsWZMnncTweWhS0Erwn-niEll41tSmAnqs-9xt4mtLBvMDWXb9nlORwfLMNWI_mx0yY4I5-ke8Klpbw_sPzSrZKAmFbHsQ7g0cVgIk0L_bcTrhqm1HZjaX65xywNwVBnaWh1kfs_ZU98Labk0K4JKVw9RMxTZR8mWO4Mv0yOaswmaQNI9F44YLTdI3V2LM56dBhNoTSZEZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات تأیید شده آمریکا به مناطق ایران شامل: بوشهر، بندر کنگان، بندر لنگه، بندرعباس، سیریک، بندر جاسک، کنارک، چابهار، ایرانشهر، آق قلا در استان گلستان، جزیره قشم، جزیره ابوموسی و جزیره لاوان.
حملات احتمالی آمریکا: چغادک و جزیره کیش.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79791" target="_blank">📅 09:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79790">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34521567c.mp4?token=RP9bVBB5z37Rl2aYOI2H8UblQlSDe_dkXX2iO_IKf4Sph8zAZE16AU8wyxD_b0d6LtpHaKPrBAJmjxebVyJiCp8MSKwhIqhP7bSTFMGGVe3wV_-K3qyYwYxijta8QXQkzIFxprPlOQRrr5TsbXrLr-jRKqrqb-ai4IN1T6OZY5duCS86k3ZRVnIGE37TurlVi-3DPRvVQtaijXsdQmAvcHLnTeg2-f4WEPt2ZlNTnwkOZlrh-2eOwmqlzh4vz_GPABJ6hgGA2gvRg1_ejwXGL5d-TFJXhh07gg2MxGDgI5iisNOZgOFk0nVe1xFOSUfiH104tlGhdc6Xn40fm6gn8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34521567c.mp4?token=RP9bVBB5z37Rl2aYOI2H8UblQlSDe_dkXX2iO_IKf4Sph8zAZE16AU8wyxD_b0d6LtpHaKPrBAJmjxebVyJiCp8MSKwhIqhP7bSTFMGGVe3wV_-K3qyYwYxijta8QXQkzIFxprPlOQRrr5TsbXrLr-jRKqrqb-ai4IN1T6OZY5duCS86k3ZRVnIGE37TurlVi-3DPRvVQtaijXsdQmAvcHLnTeg2-f4WEPt2ZlNTnwkOZlrh-2eOwmqlzh4vz_GPABJ6hgGA2gvRg1_ejwXGL5d-TFJXhh07gg2MxGDgI5iisNOZgOFk0nVe1xFOSUfiH104tlGhdc6Xn40fm6gn8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 4
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79790" target="_blank">📅 07:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79789">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به بوشهر و چابهار مجدد حمله شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79789" target="_blank">📅 06:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79788">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آغاز موج 649767667 وعده صادق 27 به سمت پایگاه های استکبار با رمز یا زینب.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79788" target="_blank">📅 04:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79787">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آغاز موج 649767667 وعده صادق 27 به سمت پایگاه های استکبار با رمز یا زینب.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/79787" target="_blank">📅 04:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79786">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsyYDkRClX3FkVApIvYu-FVJiS0sg-UvxyfcQmZNM-e1Tonmplbfg1s38RckhN3gNKIfXBQ5m6WZEi1coYAwvDKtt4DOTeNwIIhUcS4cY1X5vAXAT7L23XT7MmVxnsiritMnotGOJ_IF3LaRqilWaPpHLOPQ-5KeenJas_E0WY2Jt476K40Eu12dNk_WAQnSXuDIeo4q6TCt1iewi5Thv7-DBEYJmo655W1jNdEyS3jm_Q051Pq3Auw09EF_tMJfxR8C71iCN-vr6bZ3PohmwQ60JcHHQ5VFREY_578N6hp1uRIHeRYq56hFzVQMZS1SE6T0wKje-gS04lVRAFnVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال رو هم دارن میزنن  گرگان و اق قلا   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/79786" target="_blank">📅 03:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79785">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شمال رو هم دارن میزنن
گرگان و اق قلا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/79785" target="_blank">📅 02:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79784">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بزن بزن تموم شد بیاید بلایسیم  https://t.me/+3BUNQoy8hp5iODE0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79784" target="_blank">📅 02:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79783">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بزن بزن تموم شد بیاید بلایسیم
https://t.me/+3BUNQoy8hp5iODE0</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79783" target="_blank">📅 02:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79782">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شاید بگید ایرانی فراموش کاره
ولی من بعد سه سال هنوز زیر پستایی که اهورا نیازی توشه کامنت"ناتکوین کی پول میشه؟ هیچوقت" میبینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79782" target="_blank">📅 02:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79781">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خب فعلا اوضاع ارومه بریم خواب خدا را به شماوند بزرگ میسپارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79781" target="_blank">📅 01:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79780">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اماده باش صدرصدی یگان های پدافندی بیکینی باتوم و کویر یهودا برای مقابله با حملات سپاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79780" target="_blank">📅 01:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79779">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/715683a4c7.mp4?token=BP0KguqtWCPiG3g_z7ly4XYhXwwaT3rZRh-quJZ2oGT4pwQAmVngQ61IG3YlMgxsuKfw-WLFEFGRHwx7OnYXKSSkTJ-yRSyJ-a0Tnsv3P6vHNg-inBr57D6G2eATYutsMZsBD29ZYSADMl0BrhMXE65V18GeepLqt9I7uQhmtTmtEfHVAGXPSgZbKZLRBb4S8auZWXdPISJ_y0771rl4jMFzWn_Y5XaIH11OkAGUW_7GDl-dRdn_FKF5x4WRUkkdURIz8wdiGRT33E9epRdULVzCwwAhOSidYISf-YgDi49OYpIWMfPxyZH3jLkbVlf_7IXathDEQZNfPkxDsodpdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/715683a4c7.mp4?token=BP0KguqtWCPiG3g_z7ly4XYhXwwaT3rZRh-quJZ2oGT4pwQAmVngQ61IG3YlMgxsuKfw-WLFEFGRHwx7OnYXKSSkTJ-yRSyJ-a0Tnsv3P6vHNg-inBr57D6G2eATYutsMZsBD29ZYSADMl0BrhMXE65V18GeepLqt9I7uQhmtTmtEfHVAGXPSgZbKZLRBb4S8auZWXdPISJ_y0771rl4jMFzWn_Y5XaIH11OkAGUW_7GDl-dRdn_FKF5x4WRUkkdURIz8wdiGRT33E9epRdULVzCwwAhOSidYISf-YgDi49OYpIWMfPxyZH3jLkbVlf_7IXathDEQZNfPkxDsodpdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/79779" target="_blank">📅 01:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79778">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یکی از تابوتا رو تو عراق دزدیدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79778" target="_blank">📅 01:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79777">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">محمد سامتینگ کارو جم کرد
ترامپ در مورد ایران: اگر این اتفاق دوباره تکرار شود، عواقب آن بسیار وخیم‌تر خواهد بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79777" target="_blank">📅 01:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79776">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به من ربطی نداره ولی این تلافیا چشم در برابر چشم نیست، داره کیرشو میکنه تو چشو چالمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79776" target="_blank">📅 01:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79775">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تبپ 110 سلمان فارسی سپاهو تو زاهدان زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79775" target="_blank">📅 01:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79774">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ بین این همه عکس، یه عکس فیک از عملیات امشبو ریپلای کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79774" target="_blank">📅 01:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79773">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رسانه های هر دو طرف خبر از یک ترور هدفمند میدهند، خبرنگار اعزامی فان هیپ هاپ به جنوب می‌گوید هدف ترور چرسی بوده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79773" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79772">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تاکنون ۱۵۰ الا ۲۰۰ حمله از جانب سنتکام به جنوب ایران انجام شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79772" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79771">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کسکشا اروم تر بزنید همشو نمیتونم پوشش بدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79771" target="_blank">📅 01:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79769">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چغادک بندر لنگه کیش زاهدان زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79769" target="_blank">📅 00:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79768">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رسانه های هر دو طرف خبر از یک ترور هدفمند میدهند، خبرنگار اعزامی فان هیپ هاپ به جنوب می‌گوید هدف ترور چرسی بوده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79768" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79767">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جاسک هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79767" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79766">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ابوموسی رو هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79766" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79765">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=GWOWiVKjt1OdPE-utfpycRIgrPviFqMvlcOqEz0ewvZAVBZTynMHZTJpthLOI4UTHadcXYb-IkwdopO3NJ4G7iUdKPZPjwZdGlqmlwnjFxXIYuyqByOo3dALwA6hsu8Z5fvYnQui-zaKrLJKqesGtG7XlOrXv6UGS5VjvNSIaLoNVUT1aycCgY5qKBFU4oJrOdDRtCQgij-3a_QjvARiAU1ggTbJLb-rRIQfLS009jSv_eb7qc76HBOBkRTTj8qmrdqDm6xtVk0EhWCwqMaqgeutD8ZCR8EqXIYDqEtLl7w6eT9Db8W87mHMlVCSfuUIsIglafNnG5QrnjGcNsBd_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=GWOWiVKjt1OdPE-utfpycRIgrPviFqMvlcOqEz0ewvZAVBZTynMHZTJpthLOI4UTHadcXYb-IkwdopO3NJ4G7iUdKPZPjwZdGlqmlwnjFxXIYuyqByOo3dALwA6hsu8Z5fvYnQui-zaKrLJKqesGtG7XlOrXv6UGS5VjvNSIaLoNVUT1aycCgY5qKBFU4oJrOdDRtCQgij-3a_QjvARiAU1ggTbJLb-rRIQfLS009jSv_eb7qc76HBOBkRTTj8qmrdqDm6xtVk0EhWCwqMaqgeutD8ZCR8EqXIYDqEtLl7w6eT9Db8W87mHMlVCSfuUIsIglafNnG5QrnjGcNsBd_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چابهار
صدا انفجارو رو داشته باش فقط
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79765" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79763">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCH7UKJ7aRuzr6rNbzFCKr4epVIbr79QyAzmpZguYxmgtXgHbPw1q9wOiMSF40rD2gQEdC6FQoGEUTt1zI2UG_CF52dEYlX0f3EloB-58a0wPv572Q839_JoZtJ0whJWeyIAaD5kUpKiLzYOyK7e3H3clkpWV6F-P7fq9lTxgdNyLRFoh90Y-TnKcCskhFIAnFxJ6TGRkQHJRiTomOB54P8_XeF9KYe6YJZC99eJuHW022XF-wWAglGGZl1KkmctZlcz-5nlwzTmJd7-VdXO3pe9N0X5q4E_Jr4JsiYsPFT6Uo4oZCsz_WxMhea8h3kZHiyub8AcRY2d36AG6cuTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه برق چابهار رو زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79763" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79760">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الان هیچکس تو دنیا اندازه دانش آموز و دانشجویی که امتحان داره دوس نداره جنگ شه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79760" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79759">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">از دیشب گسترده تر میزنن
تقریبا کل خط ساحلی جنوبو دارن میکوبن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79759" target="_blank">📅 00:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79758">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جنوبیا تاماهاک مشکوک دیدید گزارش بدید
113
114
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79758" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79757">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">از صنعت دریایی ایران دیگه کم کم داره یه خاطره میمونه، همشو زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79757" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79756">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فرداشب رسیدن تهران محمد سامتینگ حرکت کن</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79756" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79755">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بوشهر زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79755" target="_blank">📅 23:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79754">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سنتکام: کشتی زدن مام زدیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79754" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79753">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خارگ زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79753" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79752">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پادگان ارتش تو کنارکو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79752" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79751">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">به پایگاه امام علی در چابهار حمله شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79751" target="_blank">📅 23:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79750">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انقدر گفتن نمیزاریم جنوب لبنانو بزنید جنوب خودمونم گاییدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79750" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79749">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پایگاه دریایی سپاه و شناورهای تندرو مورد هدف قرار گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79749" target="_blank">📅 23:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79748">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بسته اول غلاتو انداختن رو سیریک و بندرعباس و لاوان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79748" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79747">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سلام فریب جان بندرعباسم بقیه شو خودت میدونی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79747" target="_blank">📅 23:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79746">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50093eebb7.mp4?token=W0_BZF8G0dzfXHejWAMlOZL3rhHkkVAietTbhbUavYDRPz3FhiWyN-TOTWOjqS5CS9cs2LK7OSFFhH8LWJ7qxyg0eELD_5JRQOeZQ-BrW6KUci70e1aH9fFckhkQCr4T16iD-vEysWeSb_aINs9-L0366Kx2bLb4_eqeYGEzDjS3_arwVkrhGDi3NevbK6tpD8BAF0xm3Juco_aiumfw3RSlRRbibaC36S0I7tk2CR6A_ZYj4430qDAzwQBf8apkwEAkx1mFq-mB_dcrVmwz63-sTohNS1Ry-SLy35XNKHHk0xuXe7BZgjLveogGfD5rOpZt7FQIQz-xS6q5fnYY4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50093eebb7.mp4?token=W0_BZF8G0dzfXHejWAMlOZL3rhHkkVAietTbhbUavYDRPz3FhiWyN-TOTWOjqS5CS9cs2LK7OSFFhH8LWJ7qxyg0eELD_5JRQOeZQ-BrW6KUci70e1aH9fFckhkQCr4T16iD-vEysWeSb_aINs9-L0366Kx2bLb4_eqeYGEzDjS3_arwVkrhGDi3NevbK6tpD8BAF0xm3Juco_aiumfw3RSlRRbibaC36S0I7tk2CR6A_ZYj4430qDAzwQBf8apkwEAkx1mFq-mB_dcrVmwz63-sTohNS1Ry-SLy35XNKHHk0xuXe7BZgjLveogGfD5rOpZt7FQIQz-xS6q5fnYY4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پرامپت خفن اوردم توش علی گرامی میتونه دو کلمه رپ بخونه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79746" target="_blank">📅 23:14 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
