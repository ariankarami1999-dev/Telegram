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
<img src="https://cdn4.telesco.pe/file/r6I4cdydSYO42GBGHRdQjjk7g1N8eAAqamNc-aGQSkFTe-1oAQ_nGMDQDCu9eXyGWiw04m5qGww-yBCcOwNjDsjCDLxmKDDL7eAWtj3q2fG2saNl0W5y6lziIfCnJJ03b6rG6jqImFdDLPzML_oUpH-JPLJHh268aAyHjfz8EWVgKFW12jfhdxr6OlMxhFiJhVKyzxdDUjR2ojH1QMMmjyOOtM3nZK2XUY7Zr48Sd78EilbQNZkC270__tXFqdhTXAufFQYrYtl3QgHYVWgUK9omHi8bO0UTtt7fIga1WdBbH-UC-qp0Q36oWdvTuXyHl00T8nl3VjZ6A_0fod38WQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 173K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 17:54:52</div>
<hr>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miRA47l1wWbczRPUquI-zCnK1mQwugzW732wHJKDaXt0bmvQYMjCdL5HzcbjLXgc6rSap87JTSKD6d6XcaZV32TQfXSqGYzVdI-glSWLyzeF-a3PSPcYBZWAq_hPVK8WbtbFv1-3u92bS1_hy7KDB0fvtsr5Rq1mZYjxLZg0Bd7ssy5czbLrdCWhKAJX97kVL99K41FdWCAJi-xO07PdbugasY20EG6Un0MgYgFk7zJzJlztexZlfKL3RF7H7pL1rMjqjsupOyBO5Vr_S4NxXH47Gi0IUt9MKnD_ztSwvD71Z3B7uZol2u4PxzZpl3mNZtDb1sKsTwwtwxtn9yGvXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=QEyF4kLAVgiv6yAezq7ZZCHpikZifGtSG6TFw7r34U3pQFBcEdgTlbXbInOF5UwTkBLzbsqjHebCkGmOEZDC0_r1cpA_HOMqBiUegc4udMal45_cCUeLKcs1uS-Bfe6sP0Clgoowd8IAp2zlYvw9JOq0d4TtUfX41n_WqRcH0OfHD7d4CB6qnmzJnrstNhz5BYTAeHl_49CDMu9kepSW3r_DBY3kuS7hiDYy0hAwZVVf2rmRbcf85-uclNvdRmA8mBijuDpPXdGoFZJE7ekpxkBSCN335IYe-NUaKU95ue5JFs96X26n649SSBW61M9PQ1OW_Hi4L4bkhXvyOMIh8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=QEyF4kLAVgiv6yAezq7ZZCHpikZifGtSG6TFw7r34U3pQFBcEdgTlbXbInOF5UwTkBLzbsqjHebCkGmOEZDC0_r1cpA_HOMqBiUegc4udMal45_cCUeLKcs1uS-Bfe6sP0Clgoowd8IAp2zlYvw9JOq0d4TtUfX41n_WqRcH0OfHD7d4CB6qnmzJnrstNhz5BYTAeHl_49CDMu9kepSW3r_DBY3kuS7hiDYy0hAwZVVf2rmRbcf85-uclNvdRmA8mBijuDpPXdGoFZJE7ekpxkBSCN335IYe-NUaKU95ue5JFs96X26n649SSBW61M9PQ1OW_Hi4L4bkhXvyOMIh8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxBc5c8LFD-ePtu9Tfi2cevbXyupuo3B44WRIGrYAi6jfdmEABzbk1uc326a30sSn3JQZ0OnBA93YzAWJVld31_3J3XUCMrTSZhZ5qURObM1y3VYuLOX8Ej7s4SrmosPUSuUqsD0qa1-FPB-IpDRgn84dhHY5hKio2wx4xv2ht7_FmUqax5d29J5IhQCEHr4ISRSwJTM_k7LMczGUHnOqvJSS8vtvHCuu8iMWbkPIFWKL2Uyqx1D3VM2W9NkVAo4PadSPo0B9IIJCV1EfMoKl21csTebnMmeVA7u-mWSOs_ocpfuJqilJBNQh56B3-Iu8d9zsRKx9EnJ8dgN7jBSzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIJNc8a048mD7p3humb_joYe2xRn5h92uD5UPLEeLuGBajCABYhLrhW0l9Cej9kZ0E7xsj_eM3nJ7McJ7eSUbWMcuz1gyHZk2bvCsk8Yqg3Qb3JvqknANOBHUYqzABo1hLUFyCEeBUQbAs04fvhO8V0pFKkFHFn5jCOrGLcUYIHDqbVOyoBQ9_rETtHzGQrcyAANq--aX88bGS6uWmvfoXRg5Wue2aiV9k1-NNeIidjVt5FDvKzDcdyInNNJFVDSPq6YNf4qxi0NnY4CwcBhRRPPvfpztBl_rGvBkwfV9T7nJhelI52PH4hiB0Ev2iY3IbhId4VQbt9G75wbVSE4QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppw1-dwa8BnUPI8hu0Fp0MjfOMYrAGaqp2EahWKPJSuSV1g2_TwRjmwOIOIwq0mjvbIcuaOuNWT6VjyZ95sMrFSgafquxCzkaMHb7yZbqHsO1oeajRWLWGCQ_cgBOg7v6nPOvJRp0hiWemN3kkYY00wgnifSi-F1L_MK24KBNSyrKuu2LcJqDjEMmVUQ_UEd55UnpSl191l1RlsEFUOtflXBV6GTllIndjqCFtHIP5vIjDgu_Aqj425Zvn24XprKtRNuONwqZFvUM1ORQEgIOpoQdN0ctb99E1oZPTQD5S-Cx-ckuOF8niKAfFk9Q04tWEO2U8xhx3JpUhhZXoq7SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWqmfCdKwWGPZWTR8AuUo6i8m_F4x7yMcT79_eGVpw4cgABoAPDTBHcUNi22wRp63kvtxjRqPlTZemcux0NO1SLcEEkZGF5zlazM0vNl_wkSyGP-s6XLUEJQK6Oq4yxPjsxvZIWhH6vgjfB1pNzXBwgkWqx0eYbYLq4571T96BJ6RV4PKSrNFBFTIiWVhHBp7rpRjnNXwQVftGaOTiuJlLvg9olu_YzdwCQGsHtUMSYZFjxySw9__KG5nGwVAR5QSnmYqAOZbuAxCW8MFzZMiWq3nSigbxzecdCd9BIdN2FAaCxErMH8g2p-GJDGTnhFxfhjEp6v_KkVv4TjjCHRhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGTjOfanlhHfVtJDPcJbTAvDy6bL4IUZC_P_WQpFqZJ6XGdOl3pkiBASliqCCX-w7csuO5uBc4xcVABttdux8ddRmm1ccFMRpu7JVUc4QEUmXrKLKi7-ea73AN4CfDM_38VVeefLJhQY6lROdnQNeo7zqNNcFLUhffFCUPueA3qJOAqN9ManCyZDTlEqecBplCH6umEQKZhRFaOaKyARqRRVqdtUBd5ZXJycZK5Bh8nmiN3ddB673wtEAGnpL0g28hjh8EtDQI9VcTPxXPbD6s-pCy8fd1AsNiChFzN__-RfkeN1wH4XH608cXa0SpYOvOIGJZ1uhe7C_AwMIc_1JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrIN9ZVK9AwokoLxOyBMLsuDwkB9BeIrA-hbDUilNSDCIMa7GC8oFgZj-PaIfaAqibGtTVB0PRL5iR5rqbw50iEPpgnFDt_S0d9mgdk-7ZDkoe-n8HaRJBayGIXduobCFLZ9MkVRLpjLj59H8fe20WE2ydgWc_WIHCZS3GoSFk9tl0HKk67Kh7MqDyG_wFMWDtrmAYmjFTnNWuOEbKmtkqVZdJaphWKhP2Fg3caA9vPYjSwrGArbvkDMVEoYl937xTm8whsrYVDsJ3nIuIB81h9t57jOKVUm1ItA1XpjlbZl1ORnnW1tlvTl3IjAmjKCkBPQOwnv_dOt7HgoHjgMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWDdlnckZnX6Sljw1MstpowOBiQjtI6_SXr7hSjxNiBdjDg-boKASjFISokP9gNmhVWahOgCkqLyuik3jhHKqK3FH3viStJoNGbfnUr1F5wVs64O79X_Epgnn0zMpGXP0-84cu1dpaKNgpKSbPDLgyfntcDdVf7GUa2DTFQAtG8QHnKqbvpT0k17y7aQszNOL3cgtS4lF5ZVBq0eICcfXMs1D_MV5d1Py9x78tjT5JidThhOoFDZHgyhjmP0ZndcidpjdJitdpaMWO27ZrZpSzRfXb9v6SC6F3e85y8yQawqAckUtmRG6gh4GGoRsT4YJ_7R5lkoWQn_LF0hf2aK2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXLOSTyaBMtT9-1Q0zT48AezUCAIo5vrFGzAp3QL8NtmDubo3m5UvNNbbZuLcomedxIo1VWpKVp-4tR4iZ70YFvIf-MDHwP_9wSuwMBqPT0_xw-7Nn1TQeYwppr2JWF2xgdyQIZ8iOIyrtlA9DlzGRDKXuqFPmRjMugwwliy2kQBLmFPY5ngAV4ZtdmrNe9bbV0W6nfvxp0feN_momQfBeklOgTXJbzc1pBf_hLR_zG-M_PDEVGGH82Z5ZPkjlvrfWDuZo1enZyXBLggsF5ydAmCqWeKOY9aw9BYO7dcwSoAcsXrPN6BwM5gz44CnRqNM6Ps-Wd8dNHmDSSgPQBoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL_i4RD707ElmgVTadn0fbhnWe_bkY64SHQjg0vQf0tfcSz_3-F-otgAEh76iEYcBNwRhhmie20WPjEjssiWr3m6dADmO6DfDSrm7bUjPc4QFPOL67QafVpy_4aWVWJrWgbGdaraWXXP6VhMyJe-Un9_YpTVTMTlSl5nOJB08gQUGaLU-WkZkDZP_UCK-p_ha-NSxBRlbhs0nFDqbmdkwvHId6-48uOGcG7JCr8I93Svix5CUnaTdoihuDgtLN0D7c1RAlzUhKCN2f9hymFXCeDnCvvj16HV1e5OfHApZIxJqK3RU9hgxOyiHZuk5viDbMUrQ8JjMe1X-29uxHPZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Smo9NPTqdIn6mNWvYP3hcOiqwges19Mu6nHImGYoAma9JmHxyS7_6it-7kaFEx_SpoozGmzQ1b0bpOt2vT36oJtuj6Po5ftS8vuCRqYNo4Cawro6W4GB_Ghu2LSpl2JVbJMUpiWURErmKUcNZlfGLWtXB5wvyZB4MHQ3W4xNNMTU9QIJFFRfcZ-EM6MivlxB6m9DJJxBTR4Yt2AvwkAG3tb3VkTi1d4yEYodFd5HWRWvAPkfAIIP0eec2VSTERHmHjmgUEMnXh1nObgqR66ihH3limiuIHK6wbBat4tZ_Th5O8A8CIsstmKW2Zi7lfCTuErgKbgXTqVxkxgbpeHw8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=Smo9NPTqdIn6mNWvYP3hcOiqwges19Mu6nHImGYoAma9JmHxyS7_6it-7kaFEx_SpoozGmzQ1b0bpOt2vT36oJtuj6Po5ftS8vuCRqYNo4Cawro6W4GB_Ghu2LSpl2JVbJMUpiWURErmKUcNZlfGLWtXB5wvyZB4MHQ3W4xNNMTU9QIJFFRfcZ-EM6MivlxB6m9DJJxBTR4Yt2AvwkAG3tb3VkTi1d4yEYodFd5HWRWvAPkfAIIP0eec2VSTERHmHjmgUEMnXh1nObgqR66ihH3limiuIHK6wbBat4tZ_Th5O8A8CIsstmKW2Zi7lfCTuErgKbgXTqVxkxgbpeHw8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDzbx0c89qMr9t80BXhPAXIKN5fgA5NWKsR_rBA1bgkKh_7gCNxJB_8-9FQ19sd4VHBpIx0HHq3PiXl0MO905txC8IvXgqCfyFZWIWBIU2rsEp_SvTCvT9YkcpUdJ9vN6RUYFi_7CdNK7GXt03iI1H05uX6Vc44J3FEn1k232muAbcjSvEJxws0D-UB7R7dRYD6hluBzsIlr0hy6WAp9YjBUVBU6oHD2xOdVrmNGLb5Gbj-VKHGe340oBGUCcBcn06eHS_m0p4fcDuI0Ycjkv7eW0URQgAKw9-1WRAp4A5fN_d8UXEF3v7uBKGYMUaM0WAOXtCyiCNV-ctatSP7k-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ag9p55ZH6lgn0KqcMoXyibAKQ5FWZ8HOK9B6kfHnATY4k1Phxete2HxwCxRCJETfL0hI9rQY51xuU2Egy0EO3Qb5XtHbUAoiQiOXIguiCqyMJ4xluEOlOmMmq6SmeeeqL3Xh4fMhgnxmK34h7ZQOXCIMx-6e5rpzIERueC_oB5LZI8YYI0oSGgYMx2uU7LKF2COCUfYYzoTO_QXkzKc6IF3wjeJmnNQWJeSsoQEin0LXcjU7Q6Qn4NZLoqB3arl8vkyBMXfXO3KtOTVxWmN6XmYKrUlFMs4ScWr3bEkDUsxKOgchdIteSuQwgl6xvwDjkcjoUreGdDBKVC6sGIVP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjfpbMmFsbNcAhSwclbNMYnPz8Q5rGW6S7lR-93ULQb_JA7qQmUkj_xQ9CtrMhclTKsHb0PiECf2DbPg6UfgkM69AkEdzai8oC1c2yhc9_q8lGK-zgv4eB8F8yg-ZKUNZ4LZ1-K_dZeZuBWq5Il20--KDNGJ0sBdPCoXsa5oHDkb-S7bnxVc-DbL-paY1WYiU4-phrN7q3r1EX6jlfJ-IZWuZ58YoVkbi9e5X64BpeP58PUALo99UWfMRJCFJAScJfqb5RhPMLVgHlHfpuiMxEmdQ4QJjp1SJ49DBzZYuoPT1maApAnQmc-pTFBl2aIrorI94Jgr1iB5E5PaayJlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWp4bqY8rXhKjuFFyB7IS0rN6FI6WqrBa2RTXd9946_yOS9w4Q24Bi5Ccic5WFrCxc7YTx98rsBIZa95M0Sw7N3VcV1j3srX8KlWb6GEafz-_oyoxvd0ez7-jpV9Necxcpc_KqAmWkvGJ3HiDa3mIA5PqZgVHzVYgRxvm4WNEgpHKRhbdGCVCeFgeBnMEG-j3XuflwQmzEzsSt7LFYENHGdkT4U-Ih0TZZYE49Yw0soYCr196VzZbse8HE-Aiz8dT_eGp-xZ-QPBxa7s4BXVRcfp0iK-7ldo7Dd7nRjoMMBUxJWwb4e6fZ_2H6FYkRmYBYNR81B6G5onJJafJUWAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=JHlMRwMMaGMQ1TsMq1fJSsC8e6VqhKFLmXwPkkruRSruz38NGnpFeFvyFGtBj8Ne8QWG1GDC-LW_lf2wKNQv9Gf5tF9OM4p_EU3VhIvbm2n_nsuZQuv_8KqUDCvAq2kKUbviV3_lnE8e_Kan0wCr13daa4Y-I5BD2jyFTLwX1u8JAYFV9gxOMB1tMxHJ5RL6K9uJ3U5gKxbgESJcX9U8kAFfz_8JsYFaxvSMZ8Ow5RPEe8DtyWwve3Is-ms_iRRL1rLMecJDjfbMhNQoYAtw6ox2D2RlsJbRgiQRu65p2lbvc5Fgp9_CL-kB3BlyD4IeVxVVqiEt06WyOHyBvK3zxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=JHlMRwMMaGMQ1TsMq1fJSsC8e6VqhKFLmXwPkkruRSruz38NGnpFeFvyFGtBj8Ne8QWG1GDC-LW_lf2wKNQv9Gf5tF9OM4p_EU3VhIvbm2n_nsuZQuv_8KqUDCvAq2kKUbviV3_lnE8e_Kan0wCr13daa4Y-I5BD2jyFTLwX1u8JAYFV9gxOMB1tMxHJ5RL6K9uJ3U5gKxbgESJcX9U8kAFfz_8JsYFaxvSMZ8Ow5RPEe8DtyWwve3Is-ms_iRRL1rLMecJDjfbMhNQoYAtw6ox2D2RlsJbRgiQRu65p2lbvc5Fgp9_CL-kB3BlyD4IeVxVVqiEt06WyOHyBvK3zxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22869">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🌐
اسپانسر رسمی لالیگای اسپانیا
😀
مورد تایید سازمان Gambling Judge
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22869" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGqjepSpcevt_l0Pb2OOWHxk301yJLdkv1YBXNhVhqX6Nu2_-Cn_CwPaSXobn9n8LvlToyzcJjen9XiBE3zxpAb-3U_e5BGGqh7VV0oMjxk4Bup2oQCN_Joite3n4W3ZJgaeyWbO5yrRDK3L8pWcMHgj9s2oC4SceVejqjeib752SfDDPQDJqcsrOSWm0Se4Ov3Rqi0HZCbjWZYApQqYZ1U5DUCjUVZhvgCyeclSaGvynH4-pQC3t8zGKGm0F95uO8n1MksPg4C198TV1EsCWUkaQ-gS7MpeFjQEaAli7xlLzNG2zTSYfA5O4LsKb9ek7OHnCVkiBz5R6yJCJi8SuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwqvX3O5Zzx4_YhUUyCf5yWhNQX7R_6jiZJng0KzKkz111bovYG9yh6JbaRPx8JRir5FT5uxiqBWxlV5G8d2wPqT2IWADK8bkPBC2zam9Qd5fUy2Fm4Q0aeWbO5mPmXlUasUpXktBuPKuucWlnDZpKwFr6TJAu3TO9hMtNeJEeT7nxADC_ipLylZh_Jw9VMKTMz9USG7S2s7g_2YGsfWmC4J6xF-PWUneGi7zLmdlehYfr3Kssvvnm3M2lciXB7bLoYW1KE8zPYQylXz6CZZGTIv7SYHd_nqbQxvh_89RYZhbCnA3LBfL3ifCcy2nR6sEHaHflvmxXE_jGC_94UnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=n9dvuL9oLxi3xHWgiqutKrESKOo5EqHHGOZvbo2H-axSf6ZC20LUMKLfaEScF5-8VhUmVrPAiiQbLxPbyTc-_MKp_rjLnasPT5DGUQogM7Ft2BNCj-OKZ9VYuDDi6KXp1xZ7uOP8BIQTuGMrYoU7WJncXHzoJPaf9UFR6sO0Zwtotgy5fGgRgiuLKj_67geVOe-9zcmHnSEseVpmA06JcwI3jP_rP2_ca5ZNLTzQndugdy-Zd8w8mKS9B5mSQjRmh93NMRXkRnyjyFe9TPA24WF8pcgCmvEYMRM1pHZnXUL0V9tuFJJRvhbpiCSN9Fe4jyY5SS-TXFVMSkGXbhwJEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=n9dvuL9oLxi3xHWgiqutKrESKOo5EqHHGOZvbo2H-axSf6ZC20LUMKLfaEScF5-8VhUmVrPAiiQbLxPbyTc-_MKp_rjLnasPT5DGUQogM7Ft2BNCj-OKZ9VYuDDi6KXp1xZ7uOP8BIQTuGMrYoU7WJncXHzoJPaf9UFR6sO0Zwtotgy5fGgRgiuLKj_67geVOe-9zcmHnSEseVpmA06JcwI3jP_rP2_ca5ZNLTzQndugdy-Zd8w8mKS9B5mSQjRmh93NMRXkRnyjyFe9TPA24WF8pcgCmvEYMRM1pHZnXUL0V9tuFJJRvhbpiCSN9Fe4jyY5SS-TXFVMSkGXbhwJEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=W7f26tCz4eflC814D26QbWrvtGEjd1zRmG-y_ktee3RJRDOX6OQYUFAAqzuzOXjwDLjawq3IB7XMjc8wswzeIetuAawBb3PZ15Uvs10GO3_7EHD0SM_n0O8izYnobDrTCa7OT7QkZVm8yhIq3ZxshQPkEOSt1rwFgAhklSTSGJZga9jOlH47TdAJgpD_3NgmAdBk8ZlHtbHOGMcVOuwcxVdzOftFw0HVHs7qBxvS8YN0bF_BMAPNjHbqKWZ4aOJroqNFjWnrGN8T2sV2qpgN93WvdtIsHmo9Jlx84NdOwP1i42E6cN8eAYFqD2e8yYsrG4lG6mnWwjJLGbYp2lne7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=W7f26tCz4eflC814D26QbWrvtGEjd1zRmG-y_ktee3RJRDOX6OQYUFAAqzuzOXjwDLjawq3IB7XMjc8wswzeIetuAawBb3PZ15Uvs10GO3_7EHD0SM_n0O8izYnobDrTCa7OT7QkZVm8yhIq3ZxshQPkEOSt1rwFgAhklSTSGJZga9jOlH47TdAJgpD_3NgmAdBk8ZlHtbHOGMcVOuwcxVdzOftFw0HVHs7qBxvS8YN0bF_BMAPNjHbqKWZ4aOJroqNFjWnrGN8T2sV2qpgN93WvdtIsHmo9Jlx84NdOwP1i42E6cN8eAYFqD2e8yYsrG4lG6mnWwjJLGbYp2lne7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3KD3Dn_nYakEInwEvZLxrZ4thmZWAezRinF0o0mHT5vzyMRG4C4v2W-_ojTmpy0G4lHrZWUYFjkKV6yMvPELXlacJ7I96OJfug-levGz2znzZ6jCCXRynCCsRjBJ7E6ZnwDp1IrrjxZnzzM9lGj3Z6dlOMiRv30IGnhcBWQ_FspMyZz-xTOIk-WZw4nd4VmYpG4Ln-QMI3GtyZyy4N8vDS-YXrlHfGbTtU-6ZreJWFjnkO8xujkHYgcuOSTfDmCox2SsHHOr3s4IUv-om_fp_yUU2oZ-c0LHc0Ew0JM6q3BPdIXElI96mc829geLBzgzfU7gNP4iUJKAfcudrP4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=lqHmpen5w4EqNJF_nnBRjvB48a8h2KGVSPVEiqY1dMgrpUymKMB7vGfhoxo2wIlXw_8V7EKzl2FH4LkG6wjmWl1WhPKPC8Ljy6yObEM3Xx8X7CezsQpjG365rN8hIE5AoAY-cLOCJ3jcB14IQqf-aMBkEtVToFtkc_ozwIwMprW8oaQDOjQ2yTZRU8kkph1MrKX-fw_zteWozLRPxtdhMxbGPojQIytFXnTYOWpmsSavhCzNQVUiezLYgmNZLgdnCaSQHTjapdJ8q0yAHJvUw2eSCu1YIJIeuYHOGXynt3N-KE9gxKyutRsXrnAsKqS16f8AVRTk0Q3vjcmjhThMhaKT4_Zrmku0umCwKNdcfuGLPa0Sm1OCV3gOiw76oieTjra4GqdIncSftxeijc3ae6oe3PvfF5T8SARH98v9ejMg6G1K9-o5_TLP6kgseC72glevnoGeruwB5ummjlMOqrf1PkTWbKqnR2eCdGBo5r96mGt_xgYu_GzBRmi90ReZ9HaGWKFPQXEVzjbRAfF1tVz75pkZCbD5ZTjlWPu5eqiKKqq41UxcsBSggD4EgF-N0OX3XNwQFLmq3IiMT_EW82xEiB31ZbifPGsbBO9HblADeNNu2RCmsPEqswWCh-T9QUvnjkclEJNq24oXyip4XTXXLfDMkzcQzQ1lPKfMNRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=lqHmpen5w4EqNJF_nnBRjvB48a8h2KGVSPVEiqY1dMgrpUymKMB7vGfhoxo2wIlXw_8V7EKzl2FH4LkG6wjmWl1WhPKPC8Ljy6yObEM3Xx8X7CezsQpjG365rN8hIE5AoAY-cLOCJ3jcB14IQqf-aMBkEtVToFtkc_ozwIwMprW8oaQDOjQ2yTZRU8kkph1MrKX-fw_zteWozLRPxtdhMxbGPojQIytFXnTYOWpmsSavhCzNQVUiezLYgmNZLgdnCaSQHTjapdJ8q0yAHJvUw2eSCu1YIJIeuYHOGXynt3N-KE9gxKyutRsXrnAsKqS16f8AVRTk0Q3vjcmjhThMhaKT4_Zrmku0umCwKNdcfuGLPa0Sm1OCV3gOiw76oieTjra4GqdIncSftxeijc3ae6oe3PvfF5T8SARH98v9ejMg6G1K9-o5_TLP6kgseC72glevnoGeruwB5ummjlMOqrf1PkTWbKqnR2eCdGBo5r96mGt_xgYu_GzBRmi90ReZ9HaGWKFPQXEVzjbRAfF1tVz75pkZCbD5ZTjlWPu5eqiKKqq41UxcsBSggD4EgF-N0OX3XNwQFLmq3IiMT_EW82xEiB31ZbifPGsbBO9HblADeNNu2RCmsPEqswWCh-T9QUvnjkclEJNq24oXyip4XTXXLfDMkzcQzQ1lPKfMNRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvWXUl9u7LKfSNid6Bfjp5C7w3AWyWhgy2KEp6jHLwrjgEhPg3uQnFNlL_MkkPFPJ73cs00hiUoW5iNhTw8Mee4fuylwgmC8KsVSH-uptuH0-qxZiqBXuh0yfHIMbKEEI2HyKa7yheQU_k01CD46a1kxCCeAnszkIKIcpmdg1MQP6U6kgEcpBEfPVgx9X7H-brlqi6SDX9TAkwl5p6er5mBFy5xiPE_IOcjlMMlbrqJbdSdfKcy95SgN68dsgBQ2qvvsdIXh-UgWaYI_kG0frwum1D3CXsdzniNFgbwQ7VVasHrtPYMG-fnAjrVrLhBL5OPJTp7nkk3Qo2VkKkCcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVj1Ro3fze3ZaRcQN9DHdnCXjjOhk_kUq0xupB1Fw-ESCAITZ_AincdHV7kZtBWLiWKSoaokNcOm7T_y7bMMLErhw84tCYNOOuslww7941btqN19yePUHDR37QNrYmKUMWVZ0C76iUXdaTFgGRhS8r45pS-WwiFnHtBfcvCqv8sSRoCGkyI_nkRpVzNrylxCS6TCN8rQbcKg7iimGhBbN_tyWfmdYcFaFcWYL26Kap_mexCt0prskaKcXZADn0WDO0YZdd2DDC7mSUvKP_P96beVsZn_BUXN176qmBtsAEHmrwfSLAGJNgODWqq8qt5sec7UIa03lTlkQNsD1ckm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxbe76dDtgfdWKJq-5pDYWZoZro1OowoMZOO-0U7idsmRDolVYgDU5TXI3XjJjJp2svl0GopClCulqWuguC9NYmvuBEje7lLEcUzrCFbXtK5jH_fBtzRifnQxRXvwguvCWFXjiEWzu9epTQWadPA4QHhYjqSBt4dUVWVMZYcX4vcLw0Vq-OGttT71ecn_UMjTD8Q5tE9M8DCz989fXcnNb1tFlpvChu-ZWGjGSVQkR5dfPOAcMzOP0j9-GK-uIXaP6R1wN06sJ23wbUI_mKFrlc978KSFG9NRR4C8jHf9fw4H2m9PWGwJXAD7LVRCZr4TxlAaSDwh2e3xFQD-iP9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0I7b2C8DzHbpBmo92lZJZJAJU9tFWBurYZwFtnz4AVdOfo6Tj_JKay3YxIURHoz5tIQF_SRpNdPI0LGGpHnbBbI2ho5AJTfx7r9rz7JjQ_iM8kF4yeqt8T9s30nfp9bX9Cs9cLWwK2JQLTUo_Pg7N6K8gKHq_Iqizaoxs6cE_lnnd18zC46gTnZGEEn-g96EK3YNDBdks0wA9oOM9ke3cHORcCV3pgtC3DUPuhPQuvlSRg55iNsgLVXRc4AO7P5qPLVVuhy-31r4FHI9y-IJ7wQuPJXW52ZEvmYSDTN5y6HpqxrsONfThKR79ZnQoYLiS52yNx8bnpVef4Xyedauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grxtckkKbczK_Vyiu-Cq3hkLPJ_7gfu-E_RAaMAiglfX0I5lLxM3M9wu1-EyB-52mTS83xnlKt0QDFFbHlSipYa9IXyu365oosy8Xf_-XH9vvJJtl2K9gV3aFgOwji0xQTrnmQqNs6qvDf4ct-5Czoq39UyDYAWQ3822rfsOOWkJGQoT1w7il2K0_ZWNUpZDkRc40HehrthEX4eIeRCVKmDRXzm6xxEDwGFAQV27uPCVzEWTFdPOn3RwJ_DkPALuVOKOZGZpHEe1lbI0ZWN74XvKCfb0t6Yp7LMPGnm_Gc1u5C0eqp3qJ5LROiHgglT5g40Xqfx4bHS6dEE-4xTJbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqwoczyQp0iqmK5wNCWxPod5zT8u4BnxJbvpF9YaZAVIsSqsx-7bMSFc9fGA0g_jViB2D667fjtHbFDFO_kX0y369IsLtx1Wulxmfz2llxpwVfmXuu2zc-tWM_BxGT2DFXHq6jC37lAfqAvFPrPURIJ_jxMgjv8DfRteDpQFF_qlSVh6p_GxySuj-bvT9d-emBYBCsDIzSOl4HGobouQU7h_PAG_QqFrHa0_KjWcDphvLBHR0J7znBpthhj03yJ1MT5UN0lRZ9Ptq530Weia6GopJprn7K-Y3Q3OZHk4wlaKuao5SqpLkATvRb6n1Iim7EZdGlR3InKpjBAJpMuFOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moXOZdWmGZua0El7pokyHMObL71dk96GLOZBKDGW-84RRnWuFSVsf2xD7J4Pagmi6T41Ra80caIH5-pxxsNzhnigDMRnDr8RtqLBKW1X0FIl1GlGKwHY3ntxPqmH8qR1AYd_zXKzNNAc_WEuMZ0TK49La61Hyuo7xmR09C4h-OOQTfvIO8haZMQOXxQ9wGVzgIzhqvODVWQfPJ6xoP48PaJueKy3z5f3fzf3COPcLPGnhETne6qeswZRitSs8dAAScKxhy3TMkAkqoPF6Uss5h4yXMvSliGBdpTh9a7oK7CBbSzHMLdpbRi5Z3BVWFQP2v4tevEiScmHQItC0pzwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=BKdIxgA5xJM4Z6hiiOhPEYn6hTdfNyDKSWXoLWRlshdzm5HhmtRmBUx5IZI2lcHJywveT_anURyRWHQAUCuEb_YItCgfzEhkwW1WgUmE7cQF-9j90YPHU1EP5cCJaZsgew2wFyL90lddyAp0h-dnx9tgGkooa9XVQiN6r5yxuoohauC8leIIVEpJyc0cCUHgfriDUrzvQyJneFkH_xDvo7CympEQe5_sd1CDy_M9wFc420srAaaQR9SNX3vsD9X0dzX3uPj7FY34mu7sbgmMwiwlmQFl4e1KugBNaVRfUX68QMS7fiZx7CWtl-pHIKJfGw2dLkjiev8otKCCQh1GYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=BKdIxgA5xJM4Z6hiiOhPEYn6hTdfNyDKSWXoLWRlshdzm5HhmtRmBUx5IZI2lcHJywveT_anURyRWHQAUCuEb_YItCgfzEhkwW1WgUmE7cQF-9j90YPHU1EP5cCJaZsgew2wFyL90lddyAp0h-dnx9tgGkooa9XVQiN6r5yxuoohauC8leIIVEpJyc0cCUHgfriDUrzvQyJneFkH_xDvo7CympEQe5_sd1CDy_M9wFc420srAaaQR9SNX3vsD9X0dzX3uPj7FY34mu7sbgmMwiwlmQFl4e1KugBNaVRfUX68QMS7fiZx7CWtl-pHIKJfGw2dLkjiev8otKCCQh1GYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYSxX4nUlH4JvAKib2UZ0r3PXf2ajZmmCPG_GUZk_2BOOdnIpvb4835WnJcM5q-y1OzjQVlQ5CSWpkWJtULUwn9Xscmn-2RGOWz_BYRERfVH8F1zNFt6ofhHPZCW669Fwdwuk2TaO5JW1e_Z4ohqu_8sc7ZpWrfGqP5CRvnBcK5eVnpG6E0HQNh3DPaKIb5hr9I5XiDo3y-sYvcOb1dai_hk2dubO0n-XEFMFJQuukvkO6HiXc08JAuEkn-Pvopz-fWRNDfpS5wiXeQgw21LfEwS8t7OkQpf5nTapC3gMqo2RLE_DEb_W9GgWfnGdL6ASfhJ_88F5nT07XtZVCXevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvWVNW0hsa-xoJoWrzWz2ofsQW4utU7oUtY6PnNVpkkD5um73BAgurpWhL7IIW2TKgLEen9TSf2xaQRr71bqQJfYFmBY3iWwIXYN1OYvEle2LcWtSpJsbz5O6Q6yE5icmiX60qz4Gt-oUhsNYkmbP1rC0a9t7z7Wqkm_3_1kcA46kuTA2nczCyoK3H-nN2U_M-z_ffPMYx1s0KrmFPLlNH9xg09jycN6uluOV2PbxUCRkUeSynn4GEfq1Z83tyqxj5w_3B3-xgD04ShRkzgxYjVZzEcVtG8f0Vf7m7UnTRg_5AhZfYEs9kMshNwlu0bw5lmziIel4OA5IXa1WY7vaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=nrctwEdoF1iNq670drOZ9L1YMie2qih-ZH6lhHr5TwVZguTwhIV9ajhMAwM8RxFBNUxBcK4Du2hMbjdn_31iHRLCH0oX5UyubZauUW2dS5pVTtpYBgNaiTJkZoWERhhxFdAHoiMtG4Wr1PNLLUJnK8j7kz7jjcAvvb1kNy6MGrBo1t4VDx9bhbJugdEtXGnOlnQdgKDcfCBrmkCS6wCg5gjb7jvRktaAwCs3dGNNVUR-w4sKB14u_d2HvUPRmJxWuWZCA0PZBzyk7__RfjRfoBX-gmSjpkJ5uOofKql8cQnuSojQOuX-oUtAixMpauT2TmQxxLA_ZzDJ9AAYqXCNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=nrctwEdoF1iNq670drOZ9L1YMie2qih-ZH6lhHr5TwVZguTwhIV9ajhMAwM8RxFBNUxBcK4Du2hMbjdn_31iHRLCH0oX5UyubZauUW2dS5pVTtpYBgNaiTJkZoWERhhxFdAHoiMtG4Wr1PNLLUJnK8j7kz7jjcAvvb1kNy6MGrBo1t4VDx9bhbJugdEtXGnOlnQdgKDcfCBrmkCS6wCg5gjb7jvRktaAwCs3dGNNVUR-w4sKB14u_d2HvUPRmJxWuWZCA0PZBzyk7__RfjRfoBX-gmSjpkJ5uOofKql8cQnuSojQOuX-oUtAixMpauT2TmQxxLA_ZzDJ9AAYqXCNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=MmMOApNFmmw7Yfq7X5coCatUcjcCbA2Fvm8SsM3ogI51SAO6KKzi7VI5MBGar0m6ixvj2-IyM39znGZ0-k_QOZNWbkN_QV1oZNL3X7KBwnLcGlEzF4jd0zA76oOcTPf4rxjL2ouNlPEPeMMS0xcrXrIC9WV1TXzTgEN6vsPC8hQ3Z6vgwFAcRIGBZSkjGr25N2CXD1NK3uOQm-lQEB6k7gLUiBQe5o9I5SWQxRJxIce-7Zh2h47zWn56nQkXYNTLbIZTgRFEghr93376S0D0UHb2VCV78DBzyr-8hbw97TnGq1KQ4MxNrQcpcIOWPlAtPratUY76apDhx586f-cgXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=MmMOApNFmmw7Yfq7X5coCatUcjcCbA2Fvm8SsM3ogI51SAO6KKzi7VI5MBGar0m6ixvj2-IyM39znGZ0-k_QOZNWbkN_QV1oZNL3X7KBwnLcGlEzF4jd0zA76oOcTPf4rxjL2ouNlPEPeMMS0xcrXrIC9WV1TXzTgEN6vsPC8hQ3Z6vgwFAcRIGBZSkjGr25N2CXD1NK3uOQm-lQEB6k7gLUiBQe5o9I5SWQxRJxIce-7Zh2h47zWn56nQkXYNTLbIZTgRFEghr93376S0D0UHb2VCV78DBzyr-8hbw97TnGq1KQ4MxNrQcpcIOWPlAtPratUY76apDhx586f-cgXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtRGVTCm9ikfXxsX-nEz24lpe77p3xU8pXKPLMKaR_JJTSq51anmVc5en0wnFxh3dVEm4HGG2fACh2m_iGKFTd_DB2oU92TRzhl_7ZwU0r6GU71JTcgO3cO825yiIb8BMugMsnaW4gFHKI1cxPkNv24nL56Ac1nC8zbL2BdezZI62C5Q01wZrlKsXMw5aG8ExcIOvBZaUCUbmx7FkjnbN5gnE7OKF5dLmYMLjDAACTxjMbxe24ALgBcEzt2bck2wl_ySnwWx1JzuXQWm_YSvxRGV7ZCzaimn3nzsFsidhbmxha1nyYRcQuSaqS6j_5jNuefAeh6xfNvEK0dqW_5ceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=UBZ0kzERDQoF35Ms07Jk0d7KYB1r6Xjby7Yg5_LfIZGYHkeWrmDNciN3J8jBkr-9dLnGw-ZrlI0jTzw_WHIrNvuQ4yHYI91DC9jBA_WrytT4woAFqvdWNBM3SfjgZEXmSmmHjL_npak6D8arCqbuUEFJe5rNiVH49O36lS5RNoIDDjJdHLBS1OKRG9ocg6qxIjDhCBaiDZYSk01aRcNFZmU7kXM1tOTW2n-hxEKpmAhW2daKhDug1MCEFyYJ886hKKq_2XifX3Iir9ei4eNlFBcAkFvx8iqGLFsyMthxvs9c7BASG-L-s6Ifp72Qhfj5LL4MQErMXGjhYRZWKh545Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=UBZ0kzERDQoF35Ms07Jk0d7KYB1r6Xjby7Yg5_LfIZGYHkeWrmDNciN3J8jBkr-9dLnGw-ZrlI0jTzw_WHIrNvuQ4yHYI91DC9jBA_WrytT4woAFqvdWNBM3SfjgZEXmSmmHjL_npak6D8arCqbuUEFJe5rNiVH49O36lS5RNoIDDjJdHLBS1OKRG9ocg6qxIjDhCBaiDZYSk01aRcNFZmU7kXM1tOTW2n-hxEKpmAhW2daKhDug1MCEFyYJ886hKKq_2XifX3Iir9ei4eNlFBcAkFvx8iqGLFsyMthxvs9c7BASG-L-s6Ifp72Qhfj5LL4MQErMXGjhYRZWKh545Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=FmgGoZnoOlbCTyE1Kzou1Uj16PwXZoTnK-lK0mPHM57ZYrX6C50mjqhbOEcT0MpO6uwsyu4ErcwQdqMCAoHV-1zhBvG0OLfQSMFuy6udFMm2hYo9yHUn8Iy6R4MjiSjX7S4P6GfEf-Kg-XKv7RuM4bFk8UmygwgEqrPqSB4oo1svx4qoFISEy-i9EyB_LAV8nVlTfSSsgw8NBseN1JY-BCMRE83wrDbGvq7WOsmg3mYorrn_jNpYehhOHhVPAda1rW9CFAlawy5YXf2zRMfD-vqASb7EKefl3ZkkOg30KsurDh3guYwu3QqUTS5RtoBGk8vugdr_euPsvgDGrLf5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=FmgGoZnoOlbCTyE1Kzou1Uj16PwXZoTnK-lK0mPHM57ZYrX6C50mjqhbOEcT0MpO6uwsyu4ErcwQdqMCAoHV-1zhBvG0OLfQSMFuy6udFMm2hYo9yHUn8Iy6R4MjiSjX7S4P6GfEf-Kg-XKv7RuM4bFk8UmygwgEqrPqSB4oo1svx4qoFISEy-i9EyB_LAV8nVlTfSSsgw8NBseN1JY-BCMRE83wrDbGvq7WOsmg3mYorrn_jNpYehhOHhVPAda1rW9CFAlawy5YXf2zRMfD-vqASb7EKefl3ZkkOg30KsurDh3guYwu3QqUTS5RtoBGk8vugdr_euPsvgDGrLf5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=Ql4635pEHyz6BLNTaIVwxVEQa7sAzMXobeIYF6nUgq7sWHq2AZV_fKyQdpLp7I7mHKmjPzj7xsrlF4i9CbGy8PNjfO8WXKSz-eQ0v4mjwcE46G9V8WQidGh1doPXyDhd6REjU9PF2WS9ccz6ZZ62-TlHW1sntiZT6_q0gDWCQ2-931bB9BnHsOvR2b8o7X5OLFmK8qRyTYUNnswIly9eXGCs3K8Hrb0xrlFx8Fwo6G2wjN2tSFoWCCOG-vkCX9x-TZkBGTfAdw06sUbl_OEjupNDu8IzkY0j4ZvbXMlfYH1FNd3w2eji-brbb1BC0cLkGs49fVY-4MialWWH4QPdxDHuVknyqDHEyyKUVvbu8qWfferYFWeIo7zGuREgt9thk35Fk_UJzV7Y9ZHaYibUqPiaOVZCfimFq_wiEwLzHZYPD_WqjP27vvavx05gg5alp-59uYWxUqpZ_T7UrAGsKGvC4pz9YBAOQp2wPwjz5iIKJvlKS0Xx-nm__DePDmpIIdt96xdgBVwgq5KY_EiNf-YP1KkdssUBlLowcaY_ahy-E878esaW8BgXHUieuA4hSihSIqWNtJAAUIEDflquJ-MesGVHts1h7Q1XuQNlqK_Em0xnxYJSKcncmpuSXgdhwhdz2ptdvqBjsOCff0FbUCZN7DoR36ZaBG6YvZh3Pys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=Ql4635pEHyz6BLNTaIVwxVEQa7sAzMXobeIYF6nUgq7sWHq2AZV_fKyQdpLp7I7mHKmjPzj7xsrlF4i9CbGy8PNjfO8WXKSz-eQ0v4mjwcE46G9V8WQidGh1doPXyDhd6REjU9PF2WS9ccz6ZZ62-TlHW1sntiZT6_q0gDWCQ2-931bB9BnHsOvR2b8o7X5OLFmK8qRyTYUNnswIly9eXGCs3K8Hrb0xrlFx8Fwo6G2wjN2tSFoWCCOG-vkCX9x-TZkBGTfAdw06sUbl_OEjupNDu8IzkY0j4ZvbXMlfYH1FNd3w2eji-brbb1BC0cLkGs49fVY-4MialWWH4QPdxDHuVknyqDHEyyKUVvbu8qWfferYFWeIo7zGuREgt9thk35Fk_UJzV7Y9ZHaYibUqPiaOVZCfimFq_wiEwLzHZYPD_WqjP27vvavx05gg5alp-59uYWxUqpZ_T7UrAGsKGvC4pz9YBAOQp2wPwjz5iIKJvlKS0Xx-nm__DePDmpIIdt96xdgBVwgq5KY_EiNf-YP1KkdssUBlLowcaY_ahy-E878esaW8BgXHUieuA4hSihSIqWNtJAAUIEDflquJ-MesGVHts1h7Q1XuQNlqK_Em0xnxYJSKcncmpuSXgdhwhdz2ptdvqBjsOCff0FbUCZN7DoR36ZaBG6YvZh3Pys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPlbdUYLAIHcaXfl4j9JzsjPw1hG4kTPvFL7k-eAIKoPR6BlBOlNCZ0P10n3OzdwV7ty6Se3T6LFKCK5EFnao3MLKCrtvH-xJLHMAAlODYI0dn3yX2QhfXNXUD8JURUrPCWNOcKbmZAZGjcUP6M0AyMdl4GUU6M6vuPcjdtUPQayyJRCWknTqDgpgyBfUS7AuYGRM7b19XR8JjVPXwEhaadaM7PcZtaYH_4uDiFS5gd_9t3QsJscurfHk_Us22U6sblHY-lLcO39sg9raMpP2A5r36HJMUmIVRJL1gVd3Fu0hbVTxnU4KNwYZbylRBCZN63Ru4KKgD8RZxRBQpYC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKO2vLfs79Bt8PtjWZmqwjxv0OfnyELmgTAMxXonW7ejLYxQxSnDcBcvtCkWQ3lD7PPvSxFMwyoRlq8M2YwspIzmEdvu8XseeT3eZ2GvSAMw_QWFZA1JdDZMYOmAv1ZmWKbXgD5Jlf5kkwYJJBv7zP5Se22K6wqXzBWEp_jFVgNxcMkOorv2ta-2E_YtnYGUX-giEONsq12RrwQ2db0LGL3eJOjhzf66FWDsYOA-heEesKPuXLY93hL-eVLrDsuiFDaU4U_IYEdtkHefarrZ77zyyWXuZv45WRZIQJ-vgCpDBsVSu20Bmusk6D3E0UQsyD4xo0maF_rlUlnMCUMNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=cohh0BNoX33uNGql1c_V-07LwS5eFAYaPpxVK41M3vqkxMg3HX-6Bj-trpO5ae26ctxxw36N3kwAQZ05UdKUj5bf8LnqvD1ya5dB2xL7vEPZGc_-OiGT88BUi2g2BEzOvjAIHF2ysIOezUnu11-CXwYOkEDSj08mmObTMop7KPtdxup17LJ87s6ezNGq9wxCDCHZqjk0dD-no6b1q-_slIzJtIqARkgbteQxqTyWo9IOhjGM4GaqGTaQc7qwM2MxFDXxOXpbMdMGuGgOlNxz-6hwj6T9ij122Lg13kavMQHUMWFP4tL0z2TuxyfAo_RRsr2n16GZMDFRQext0271nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=cohh0BNoX33uNGql1c_V-07LwS5eFAYaPpxVK41M3vqkxMg3HX-6Bj-trpO5ae26ctxxw36N3kwAQZ05UdKUj5bf8LnqvD1ya5dB2xL7vEPZGc_-OiGT88BUi2g2BEzOvjAIHF2ysIOezUnu11-CXwYOkEDSj08mmObTMop7KPtdxup17LJ87s6ezNGq9wxCDCHZqjk0dD-no6b1q-_slIzJtIqARkgbteQxqTyWo9IOhjGM4GaqGTaQc7qwM2MxFDXxOXpbMdMGuGgOlNxz-6hwj6T9ij122Lg13kavMQHUMWFP4tL0z2TuxyfAo_RRsr2n16GZMDFRQext0271nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwGpcjRHBJh9Bv0ixdIEdViROoC91PWzLr3b_-KsrhEOa0vHRc1TLNw3haiYZdpRy1T-ljZaq4KT5NHWC-eV6c4XvcpWn3LTgrbpola5AUHVOYAFrKATOGaHJBh8_S-_D-tWvF3IHsM6OTxSYpjUXjUGWYZ3KRBlRM2ayct2en28qQMi8w6ZmAceGP9j0321iy5mBUb8oepKeeaeIjamWWbQFUqLGGwOm-SMevW-WZ0uhUM6Qaw2lT8sDH7_o85oOi03KCaG1MENot-VzI9X-WZ1qTPQPCv1rv0mYIcKjvc891LguVLzyyN2oP8bni7WO9ms7A4MO6pJmqap3fFLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCOuo2hyZuyYn1apO6gP6jIYnNgQip531euHzJTBYigsl2QdXo40ZI-8gqS77kesAie7RO7FkIZiSlsmaoTUe2IK7hKKuvgN8IufS__XUPJqFXyI1_VVzK-_nLRCO3kATel7pdXrS0OSJDWvxE8Zl1d6MB2Fh0frhcVLuXy2NKWJQg_3rvHvMbTIBxEzplIbh_7K0Go3bcNx-xsKcjqQ3h9yyLTaInFRygzgSWtWYcMRRVc0Fe9LM8IG4sNdSgMJtMO6Uc7tjN97IqiWJVsC1CH-v5E47_3H7weis557SGZ_2mUuXPb0FABXfx8FqGMrZpKHELUSPFTCdgNWmJE51A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6OHaUfNtgYjsEuiUh0bmncRHxry8MbLofoxtV8qtlFTrNjxh1Z1ARIMUeW7RRIC-9t_wugldmvHVSQlxqZSXPtOu-_6rCbz7saFXyJ_8LjSW3Q8-TiZgiUTXJYnF_bAYJy4YHUs2XaTtwciX-C-_UBxcnfjOShZXHLU4guLd1wPkEnjp4rFJe5Ih4KjSLRyH373C3c9daaGdjc__a3P39JXg3YrjYLeqpNWjMnfXPIXH_0Ns7FnefJuhTEv_evxhpdkOV5Wwk3m9BnMvz9mq2cGigrcTpKy2zvqP3CSI_U0Gd8kux1DcqLbJyU7ubSMLwKhXtBw6W0UbpSGi5m1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=lXy2L3loknbHITh4TxeFzwLbNNzmMom8C-TCG0bViq3uUD9eIx3ksXjaJTvRvRMc-odjmC7ymIZbgmZbxjjus2PLUe-CM4YPn-LgY8lHen5MfRdMbUYFOeMyEnDtXok0LCXfEUqPXKOzPV9Ql5F1gbzxn_SkR0Sq8QB4yKsE3zmdrcPK8rVJtjfuiRjXdQhh_wbQPCb_GicwDPg12U2BYSEn4bpwn8-rpQ4gwDfeyp7x-yEd9rqF4w6F8Ly5CwPCWBIW66vDtlQ6RMxU2yH3kIdkAZdQmVsMHtcFhBoVPP3DEfBVnDVhLFMt_na8S_ughnM9iH3859ymBctZYTB6Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=lXy2L3loknbHITh4TxeFzwLbNNzmMom8C-TCG0bViq3uUD9eIx3ksXjaJTvRvRMc-odjmC7ymIZbgmZbxjjus2PLUe-CM4YPn-LgY8lHen5MfRdMbUYFOeMyEnDtXok0LCXfEUqPXKOzPV9Ql5F1gbzxn_SkR0Sq8QB4yKsE3zmdrcPK8rVJtjfuiRjXdQhh_wbQPCb_GicwDPg12U2BYSEn4bpwn8-rpQ4gwDfeyp7x-yEd9rqF4w6F8Ly5CwPCWBIW66vDtlQ6RMxU2yH3kIdkAZdQmVsMHtcFhBoVPP3DEfBVnDVhLFMt_na8S_ughnM9iH3859ymBctZYTB6Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kfsq4-2nWnu9EeaGLcoZs3x63qNTA8emg-jQBOhwtiT3b8V7XwHEoj5woNr9kDHZ-H9D0cOY3nAw-eFmftFFpFNvI5oiXyuY9VDqGaT9zbOhhGIReczuZkA70ywJ52CkPpcvcuwqSH1rKhTilv7CD1Pfi_r1o9ngTUcRMFpLVNKtR9USpyNNHZIR1_mpy1oMU2C2UDDlinYqVw8ZyXZnAbXBh4l1Y32ukBh4FriIU1DlQ82JFPwX67kmTO7jdocWEdn7xybXktBseA7DuD0BCK0gAiQRMTnmW5tygX0VtHjCNaUtlKPbkPoYhLaFlgKEK0ApZHLVarNe0ggb7YrkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijoAa2n8dEFS2RLO7ClDU_n-ozNwtNhM6f4L1BYpey50RqkbztEmdiPGbt00sk4FELiJsD9WL5IJ8Mn2ijxXVTFZ6-ysdjIU8ckDY5f59dsy-l3ZmQ5NdMC6ppV96delNrZIiqCmkIW4l9xBcQm8X2JHyCzzhS6jMcytuLrWS3f7OacpcAxhuvCrmhViynqjZOzw2Oxg_SdpUsmSQ69N4ZEqQCRmcHdENzw-fO_JWYuPqwq1IvPxOy2_REvVz9lsstoJMr15z7ff2f_GxdaKjUEhswE_APDPMCpbd-WIZXjcfcDrqK-V-1DiyyO_F4jINXdAVodXTPzNj1XXAmDjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu2pL5yTT8D15W8WZLTEk8GLs6TsR-UTofPSW1_byNjBbux_ZlBjhwSzehHasK4htfg93YWuX8ZoH5Adk7IA04CsjnN2lpl-aeBDiyXgD00fJycoCcMcRUT1p2V3hsfnWaK5m1Ag-8GZz8WVxuPMVZqimfhnyQl_SwuUmml1S_HafQ7DlIji-E9b-Gi49T0_0PQ5jCHTHM5F19V68VE4YaTJI4Qqu8NF-uI4F_EQlpi1kR1oKej40a5r0UrmqReD3VvCubCNT3HE6l32HmnHn73ohcT2CiUIz6ynK1vRO72CLUFnQli7TBxEK0JubVY2VmsmTCKPt85diALLBNi2Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qApt4gKvyYQ9QqB-EuMIU0KdfuHC-64Yn86ljwa2tm9KZPu2QJTXrV_w3_EZhVgzR-F9Zj_St8-g7a84JQq81HzABqVS7m6Ntt5AW2O-EKk0sA1KM4crB7g9m0fHM6_SIOM9OWzH7UG4BPHcUvKJlSh7hJdzvl7ClGFXS0RD9--hQJ5nCzFC6GvicM7Hka331EMGp1g8-41NkquXuiSn09bzJJOTST16BTPAQ2yUAjqQOXt_cDaeGmd0r1RJXCp7aLEgsAOGEhxrlpU_p7E4CYG-gsgk8WgL_AWGKlcNaFohFC_X5iNhkXM-RcUVv8lK7324sm7VyV5-8IMGtOiirg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3h2NpYWUoW0C7KZoCHQ-b_l4KqEDzEUivbRvVglKZ3jRAPQ48Ln8KjOm276p6kkj8AV64WIRb_J6z4iImTgJv7KP-XrsnPFptF58pBvg6c-O_lHNqZQkHAOAUKzhgcbRO2sqHvDGE9-WUREAO56yL5WC57eJfLMTxpTcZS80JlgZfOn_5EIQf5GPlVX2OGZeMgisDFsv7ec8PSHMTbk2dZ6dgJJTN8KQtv_TkTkr8OyIo4fnbIWR72MWuF5GP3eCZRzF0Jo6UT6CrLE5RZiYPvK_n1GNRpMRJ7HVUiN30SowH864zoFLQrmEbotKeR8aZ7HNQivgMY4G5o0yzmvFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=RwZhaQtvUerdtFG2vkXfFwEXRzNfw7vXWyXjwLLlEFr9rgVzA18p2cBpSo-BCXPZo1IjQIf23HbmHXziayFsjQTT2ZahhUM2JZSD2DLwLx7vOL0-Kz9xvFlZJYM--JVXxaH9WdQvRdicBIWPKIgJhiMYbW9S8Gqo249LOeaeAxhIMGa18tQnZU8rS2uO5e3pVTWn3FBfp_b2YtAO0HoRhBVVBhba1XPPmYpSlgDoMqRlJ873EtmglgxOtzc0Dk2jFuPoislkhg94-jEkt_-YdB9G_WbaBSc6R5BvbGQ3aI4qGJSyukp79lW_-PslvahNxCybyOKViD6C2kUfZSQb-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=RwZhaQtvUerdtFG2vkXfFwEXRzNfw7vXWyXjwLLlEFr9rgVzA18p2cBpSo-BCXPZo1IjQIf23HbmHXziayFsjQTT2ZahhUM2JZSD2DLwLx7vOL0-Kz9xvFlZJYM--JVXxaH9WdQvRdicBIWPKIgJhiMYbW9S8Gqo249LOeaeAxhIMGa18tQnZU8rS2uO5e3pVTWn3FBfp_b2YtAO0HoRhBVVBhba1XPPmYpSlgDoMqRlJ873EtmglgxOtzc0Dk2jFuPoislkhg94-jEkt_-YdB9G_WbaBSc6R5BvbGQ3aI4qGJSyukp79lW_-PslvahNxCybyOKViD6C2kUfZSQb-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jggo_muuCW6rwgU6JLynWYOS9RJQh0PARYZkmJZNaz3DOZTNv-anEwu_6Z_Y16YPBq-URbU-Fg4VJ3TmD1DZ3a2b4GnKPGjtpNWqK3B2qQLB2I2funyIx7l_sFVrwGCjpqbpltWMLQwTjT0aiC225BZV74L3cwK56M7yOPtVgyuoXmdwx2DlpKZL7esxySMf1_XfWxHrzL94zEj6th6i_ciRHe5xSZEWWxQoRunXCX4rzMJ9hM2pObZzHeusEwv6TjeOayRUFgnbbjCfs0iiN1xCUzN6eJKcL36Wf5Ysh5W7wtaYJSowveXZ_RvklwRcwEF0u0PTgOOhvgh15mNJGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsUcRejEOgnmQTwMU_KMw3YPstYyIFLURF4wXp29yYbD43PjTuWQz18IzArXkLeQyzW0gkBL5kl1Scp7gg7VrhHHgzf0n9abGjxMRqhA_4GPzQkcQE8k-dMVVmEoC9oi64s2RzSCW8Kavmq0R8KLoImDdzqw_wUkCectTsamiDZqCDIvhxbjNw9TUU6Ohs2DJlo_mqC5srBTgimnDdmE4reUF1XHR-QIbKFgxMrgdO3EA9qcXrm1Vza3dMgvRVJlsYp2YWcepzjxUJ7-dNzI8VZBoPR2LnJmTOxDQ4uyDAWWcI3L_9ebQ8YXREM32OMA4D4CDLzcwpPKU1-oof2DOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=gzlu-SFeUu3V7WM-xSLoStkW7T_b5Kf1Jwyf5Hj-ITbvk-pHdJhakecx1n_OtQDq2U-M0FOepEVIjkHImja1nnO6--uLxp-qw1YYx2ZNNRvgbW0PD5aQXkgp5ROon2Rj9lk09MiZJcGTzpymW3BjJuKMjU1JmGzs5vV6vn-ppgnXpQv0YOB9bjPLauJKd2lp3A4x4RYNaptEP1y1lXIkp4PLeYTKRStYiyyFGL72c45KfS8DkkYGQgd_ExA3HugoX2sQIRnrpHV56vLCgs0tQWvG-KSYJ9JlAC6aHfDdHWYtUvj0U92tsvHWS1IweWIm0ZSGSlrRalQrZ2Fj7t_m4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=gzlu-SFeUu3V7WM-xSLoStkW7T_b5Kf1Jwyf5Hj-ITbvk-pHdJhakecx1n_OtQDq2U-M0FOepEVIjkHImja1nnO6--uLxp-qw1YYx2ZNNRvgbW0PD5aQXkgp5ROon2Rj9lk09MiZJcGTzpymW3BjJuKMjU1JmGzs5vV6vn-ppgnXpQv0YOB9bjPLauJKd2lp3A4x4RYNaptEP1y1lXIkp4PLeYTKRStYiyyFGL72c45KfS8DkkYGQgd_ExA3HugoX2sQIRnrpHV56vLCgs0tQWvG-KSYJ9JlAC6aHfDdHWYtUvj0U92tsvHWS1IweWIm0ZSGSlrRalQrZ2Fj7t_m4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMpjyzgFhp3ZuC-IRZgPJC2ZF5nRs4Wc6517pPQZCX_DXfoQHQJJobDsg0JaifMgW1z80aIgpQJXeep556WbTvFHdZWGXdOt-CYzf5_RyM5iXq2UfYuy14TuAr4YM51Ys53g41XllWcUsQoaLXsr1VulMy42Cu_wMBow7IOjc_kienCvGxsnVWhq5UakLyy0JkSp-0WYGQSJyfpNBBG1JLrbsj7CP2Dbi5O3qCACqx0N1Uyurun-dXrb1O7ZmrQB1YCMXaymzZvOw7cyrSZRZaTkQa12Pyvs0tWjaOhSzHSWvISCF6EvyEVmeQMJC4aaE5AMRjkWZwcHB5X81k3boA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ho23gJdtjJMYtauUGMHmnesFRp1ljHrB3JMhADox-DldBDldADqrreLSRd7U1lTvO5pN_SiSwcgs4fyrFAPpFYA8tUfOsGS6A6jYM9qt9mIYnlEzJul6ucBYE6jGshxU4QgG88ZTM_5v8vaOoKiA-CExnC_-q9SNre80cXlmDb8Mp3pgrVJHMJTYIMex_CP0YLYAverbH7TWnNU7m_O76lXwCJir_RXmFkUMnEVO6kH_Zt1mtwJxorBsXPJctLg7OWJ6ksLJIeIir0i7ECnzLE9heZyLMPhaCAY_hKhqTctbYR87v78txHvzqTFDkpTLztqSFGylBDNO5Xf2hXCf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDpagNefEWUEte3sLBrxcNopVTaSyikC3ohYBVTvFhRNjznLVndm5NjhG4IDDnZmKFi1eY-gnqosqJoCZZC5iS5K-Il_T6gwW75WftPpe2Y8OVXoVndZnWkEr3erQHlq18yBtrIN0kkk4syJsEOO9B2QrJGoEDf3GiDyxkvIlqahe-USwMlYqIObPI3t4O8_Y5B2mMn8Syt3V6FhjhuZN6QH0BugKPxq7yNyow1shJduiWWyljgn5HADp_qPQF6NkF05wSTa01KUygwdnfzHhoQ81ZtzloqoBHGVXJjKSqemnWFICSIyk7Ao1SCS6bzPSSwjMGNOZgRgL9tlXztMRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTDLKi_iV3OvCr1aqKjYkC69Wh1HlwLINIv-XsOEoH1e9RrYkUMVYnROTSXhIzgxKaUCHB-30hLy10AD0UnpTWa5lKm3EV8YqV6RlJo-_POt1CNMLjvbjMTEddXlBKRcUtzsBesh4cD9jrAptOb_pJymQ59q_wzJ6tRoQUquv3juTs9-SFXhiAjao3hXXLpuTKGiZ-OtT77Ex9NWrAjkjIQoxsj7hMUHhZuqTQXMD6FTarg6ripq3JZZobyr3iW25z7ExbxbZ2DaW0eG16u9u4ZfVyIDUgHD9GFwOTpPvx9ggDImuYJ0LfLDhXDnELU-nh25UKI6LmIeKn42euhoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVBYbO84eztQU1fILE3xf6TGnxcfoOHzp5kJ-7WydYvr3mzL-I1inQnjWey8xVlVewMiANEcIDaxASznHtX4relZn9vXl9L6P3HceFTKIYhqTjOVlEVX7aeYF6FXilXoORvhcUitkJHIOu-ZB8tjdSF4H4Bi5ECRGzLBaXAc7jgUAL2n0dAt_k0vrqa1Z8Nwx-WUhKVv1YicAhvqGrLtfdEr8vNFgzNk_uw2Q231MpbG3UGFGaByS4cNI9Nq5PU-F47bHygsNBRaOLCom-BgAx8TbXnIGxH5aapLkXQG409J52I2zssmaP6OziBGR--xNAwNMrQAy_QrLIDVcC4mKnik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVBYbO84eztQU1fILE3xf6TGnxcfoOHzp5kJ-7WydYvr3mzL-I1inQnjWey8xVlVewMiANEcIDaxASznHtX4relZn9vXl9L6P3HceFTKIYhqTjOVlEVX7aeYF6FXilXoORvhcUitkJHIOu-ZB8tjdSF4H4Bi5ECRGzLBaXAc7jgUAL2n0dAt_k0vrqa1Z8Nwx-WUhKVv1YicAhvqGrLtfdEr8vNFgzNk_uw2Q231MpbG3UGFGaByS4cNI9Nq5PU-F47bHygsNBRaOLCom-BgAx8TbXnIGxH5aapLkXQG409J52I2zssmaP6OziBGR--xNAwNMrQAy_QrLIDVcC4mKnik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhIeYU_WIsW7PdXoMx_1UUXI-VrgLA_xTnFp3V3-wBV4MgTqpdUc64cF8roezaJM8bltn9VcuaA_OXbXWNEQfdOlvMyZfOiAAiPqcnLmokq2I_i2tL_6HBE4zNs-70DDCrJhgBH2_SMbawExIJxS6Hdpantzk5iwRb04aaKonMIAvx1lXNpQUXmdpEzoysI5EPMO1w8b96-JUvm536cRGCMpT26QmahQp5QGBtucUCK2JZOP9kJbHABpjO4Vln7mq8vP36Axvoe7e9yt6vgXdY7Spoq4PIZ5ckZjwfpr4fqIuZhx_08_WX7dA4yK6liOfRk0SNvnBqfPxNV6Y45oGQdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhIeYU_WIsW7PdXoMx_1UUXI-VrgLA_xTnFp3V3-wBV4MgTqpdUc64cF8roezaJM8bltn9VcuaA_OXbXWNEQfdOlvMyZfOiAAiPqcnLmokq2I_i2tL_6HBE4zNs-70DDCrJhgBH2_SMbawExIJxS6Hdpantzk5iwRb04aaKonMIAvx1lXNpQUXmdpEzoysI5EPMO1w8b96-JUvm536cRGCMpT26QmahQp5QGBtucUCK2JZOP9kJbHABpjO4Vln7mq8vP36Axvoe7e9yt6vgXdY7Spoq4PIZ5ckZjwfpr4fqIuZhx_08_WX7dA4yK6liOfRk0SNvnBqfPxNV6Y45oGQdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVZkryuI02jSFRf-ppIWNuXUr_6OEzD_wxR2kcW4xr4ZydR1T11mRNKJIPem4uAfjl__6AVYMnLilXIhELxb6qFbHspyITm4NflCRiWx3s93qviJuDZZ9HvnvbjznrDCC8uUJ-AXdyz3GY9SM0jZRSuPsFQcQty65bServnRvYvWu_YeGfn68KjndqSO46gBrq1u1ZG3rcoojXb5zgvQw0b3bP57ALjlE5mXvVUoPE6_H9x1tNF22f4cSs-g5pppQKKduaiWSDgJrfTmu0Huem-o8qY-HWvPyvDaHnJxNTzKsS7kzC2HBtjLwnoy2UDJtrYjGcOQeRWrZAu-WeltjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqTOXISd5z2XYgd85LeOSZQiHHhEvLKPFLb7voSrkhDG5Wl8y0cspFxj-hwrXMKbFW9d69VNr3XkNqjPHGCQsBY4iuTmooPhFNM3TXBrwFAFc_MR25CVzGfEdtWXj7rQJNWkzI0U4y-YFTVGhrtLOaDcsuOjQLhRD4pNJCy-1vY0AF8rw5WG88JLPHmdbKfuMON2lpjAL5exNdwwAiWuu4kSL4rRhVGG9Z4MPO2u2qbZSJg06j254PsAIZ10SYmFn9Z5BsPDTKpHYsfpN6wxGtRCyFjIWB-KWQCBuQcDZVQCs9S7sGjlG_FSqEIGH1dWmF2P-05Rhk0u9ZwnD83gimd0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqTOXISd5z2XYgd85LeOSZQiHHhEvLKPFLb7voSrkhDG5Wl8y0cspFxj-hwrXMKbFW9d69VNr3XkNqjPHGCQsBY4iuTmooPhFNM3TXBrwFAFc_MR25CVzGfEdtWXj7rQJNWkzI0U4y-YFTVGhrtLOaDcsuOjQLhRD4pNJCy-1vY0AF8rw5WG88JLPHmdbKfuMON2lpjAL5exNdwwAiWuu4kSL4rRhVGG9Z4MPO2u2qbZSJg06j254PsAIZ10SYmFn9Z5BsPDTKpHYsfpN6wxGtRCyFjIWB-KWQCBuQcDZVQCs9S7sGjlG_FSqEIGH1dWmF2P-05Rhk0u9ZwnD83gimd0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s85bdhxGEdHtbG95fVRQWXyoc3Pk_TjKiODPXOPPE3e_NsYhri3UFRoWxzhBmhoJ-J0I82h3GNlcIDCXzM1wNoThjg7GiIGo-hCcw2pIeyJFvbbemZzyqyUBAX6092zBf6hlwvQXZRsW4kaGNtAp3gFH1wBqHyhn4RV6uxRHt-eApz1Ha0i3KuFc2RWrBE_GstOnmfTW5C8BL3EAlyNNSMAqmZgRJo8aXqSqIPjOVqE8sGfQrpOzi9ca3fvkOm0xwuNqqMfAj0Sx9DUxkl-jlEDprvr_QxqPkUlOg8qkJOSYMph5N-ntPIHwMUdf5k45kJIOu7a5Y5AyPVSHGvXBxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=TY9m-DVkS2w99Vm-_Jp78YIcMP6vj3SLA_3lQz5y5SohR-b6_cGEQVz6fwsuS4k_Sz2UZcBb8q9d8pPJFRewYDYGHbWQTQsGh26P34adf62bJ9BjFnb8OM2putr4CNyyFqK8T0Z26if2qaRpC4vPsf8RwCqcSksNynUKwcTu5_2BA3QNFmmfsMWGevUAote5mkFF_JO5iPpOKGCIvUhb5-GzXFA8mgZAD6a3S-oaCp7mPsGUDujqqsWvhXVa4_VaZRuueO076FqJaSSagqvF76Gv2jqyCt77_8fCdlmFRaEPnIFK5GTBOd-xOuOy9Q0EP3T9w2vsOyBsguIUzsqsW7iZFXFmyzUI7s2yV8mfFQICwve3HSugD4jJSQTjzdiBZVbNvvg1KNZgP0Y8VpsYcR-P4bwxvyxb-DRzHW9p7LyWMFD-3C75pmc8Pg_rQqR2DORU8nAL50FpzRl1-5nb8jCdPKlVBu6Wjh_MXep0WheIaN_mz16UEXWhWtijWti-muk0y0zybtU2mrq8sYNwHDwHu4vNwwHATc3gZKsrOxB99v9DXy7oATwSyDJWjJg8Z75ioYl8N4UBjcLOkXklHBxvyJPlg7gYQznVwZKvKAXK3oVZZnKEtwi1xPUp7WjxvV-ociYn1nXuhG6JARrzzHyBDgzKqAr0ssbxRQw609M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=TY9m-DVkS2w99Vm-_Jp78YIcMP6vj3SLA_3lQz5y5SohR-b6_cGEQVz6fwsuS4k_Sz2UZcBb8q9d8pPJFRewYDYGHbWQTQsGh26P34adf62bJ9BjFnb8OM2putr4CNyyFqK8T0Z26if2qaRpC4vPsf8RwCqcSksNynUKwcTu5_2BA3QNFmmfsMWGevUAote5mkFF_JO5iPpOKGCIvUhb5-GzXFA8mgZAD6a3S-oaCp7mPsGUDujqqsWvhXVa4_VaZRuueO076FqJaSSagqvF76Gv2jqyCt77_8fCdlmFRaEPnIFK5GTBOd-xOuOy9Q0EP3T9w2vsOyBsguIUzsqsW7iZFXFmyzUI7s2yV8mfFQICwve3HSugD4jJSQTjzdiBZVbNvvg1KNZgP0Y8VpsYcR-P4bwxvyxb-DRzHW9p7LyWMFD-3C75pmc8Pg_rQqR2DORU8nAL50FpzRl1-5nb8jCdPKlVBu6Wjh_MXep0WheIaN_mz16UEXWhWtijWti-muk0y0zybtU2mrq8sYNwHDwHu4vNwwHATc3gZKsrOxB99v9DXy7oATwSyDJWjJg8Z75ioYl8N4UBjcLOkXklHBxvyJPlg7gYQznVwZKvKAXK3oVZZnKEtwi1xPUp7WjxvV-ociYn1nXuhG6JARrzzHyBDgzKqAr0ssbxRQw609M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZRcCy2yYBU73F6ixqZEldHoRoRf8e7LPC6PSrnucMgR5KD-FVMdhQGlE4z50OoeML2VC1PVLVeDcEBZSdaZvFkgLopByUOiHmaR31wBdSvpewjjamXV8YAt4I5fe2Q7sLZqBBy36FxabOclhLo3YmgejuzcMPam5BCQTRKpw0keoD2dG6G-cfrzhyufdWKBpuPt9Ilss4yU321gM5SOCTvo_PE8TC1vwO__hIiqc860iH3UIU4foxxNei4ZgpEOJ--IqZouaeYCaZWnhhinfpesiQLIeVpKjZPLY2BFG2w1gPMcjhD4DpSCrkvOnGz7M-e4zNzlPoWwAYGmEO8xEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLnzByPYcNua9c056M40Nhykhm4dRj-Qtc3h9A2vGZrQg8eCTdGCc12tuVOidlHhrlRJ9h5DRFxBbuzZ0vmISBRnx2T6vrvIZXadrKeYT21m_wdfx8MYkplxfSIXVr88ZPwITaLxGGvZC8KBdeCw9yRSJT2Lzp8iOOjseOi_Xj2Gp-6K01cS-1tFIDPrQvgdvgEwjEHCyRmmuXmdKxpFMjHD49syIPpS6IOSxsLiFf76bksK_8WTsx8gzapPxtHcAbaBA_t43dd1h2aR38WgXBFiDNNMXaokyVOq_UZ-kbFP00GE4tI5DVI5Ll7TxfrEOPFKHQ8ZYJz787GlgV7EVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjXjQMzupAnBCE7dc94K3uZdipegw8GyUsDP_SWQiUIVXhhlDNKfy-IBJ7TLg6X78gTgT6nMkekSPJxJQ_BqYEN42TCPi4tML9zBCZeMwhOJI_HUoOsqMVUpzei0yzUzi4bNd1bqrnFjUuMVVBWv3huQpQ8hlIWQ8InTfsRCrPZi7v_Ubm0runphE84CYpkCIEAQFHp6hoDS7VwceFv4o2uL3xQoOYeQWOZezQwQISKdGcOag4hWv9jIhoUH2Rm2F9E-JF9MgmRaU9y_rWb5ufflaxRAvkOXn2rV7o9lBzChIfofQ1i6tqwws_VCVAFTOPn4d9Sw8MavZNYM9znWGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUDk8c3jemFpaj1mn-zCwmkiDMQelNapmzj_YbMlckYBo-5tVrzAc1OF09-nDuVUEzu8XZeg9s2i931eetUup4Krt91yj309hfzzvSU6i2E0Av8JBUqhBKNC8VNjnnVUnZQfbV5fbvQSHh59m9CSMgBrlmgsBgs8CfBYbUxJ-Rgrp4mTHpkPSzUMfOamIicVXtfvIFsCJN9ykpiYsipTOs-buMq8E6W5mVp2GnQojojNOupqGE7jS0iQqKL9g-bXRHQ8FqUPKUMnFTTOUKMelvTuFCO0-il2wDyc9GWNOedLgRutglvMGTrpDnXdl8tuymwyll6yOMWJDzePrjjolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAm4vHjybRo8Kldeu-8Z31yxk5tPfe1tW2daZ72QWdOzUZEfcDn1kIb4UoM5QzZCYjusvhlcw-s5n-sV86sEpKSg7J1fHJ9MrnMCWmivW-HqHqCwUMWenLe69CxXwB9yeMNGD17Hc-ZyVBaZZ336HQHENUhsu4QPx-7V3qjfwWyhEEXL6A59RDd5W5VmmbJ9A1o_vVTvrf2MjMfVAp0PBDf7p70uKZii50Be6ZuS31NUyPto7qPVrN2ChCS9LtRraOJComTYOEj_d59oUPwjoa1rqQ1n_q9LmFcq6Fjj1bY0ewS36Xre-XsG2enmK_qfLE9clsHpLdY_XLnIhRuMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-0R3i8M6827jhYzUqlzR7aAtkV0j4Rq-H35eYSAwIO6XLGH2x6lpocXJqJb2jNm9w69Y_4WfFdorFHIN63MUaNIMnbyiityNuWfB7d-DDiw-AQXa-I1zkup0UCrAMTcFzdwgzjqJRVFRLeyfZ1BUrmeeK1WFbOzVbWEsk0SV4iSYRRmzy6ql6TUFRYLrACDV-7WgMQmzYtnbvrgywJ4PbSy7tvz-nKr8OxT1fXu3P-0-RzKya0IqTNQr5O913xHUkI1ESFzaWha8ayzR0zdjopJXKCnojkhFWAKb8WFy-OTIk1jmrN-Mq7ihQIkqBKmBR_UrtAp2PR7GQtktxaJoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6cwRiyrhd0ZWjGizq1l-lFWQJcj0YPm8FFDkM7o1s6iKYepKUix6xRXK6qAuHYdjSki9ay-qDswFpWv0VgrAXCXWqiFk5Gcd8IOB_1GJfMq09LWW8m4IUM8bAgaZayIUYuyJ0BqwT6ZW-ff3pkDHe1fgLv5whOmpv7kySJdHXlRsw1tPFtdcUnbDpvVkXLCHJ8OHtdHumylwTaLyHUejegM_E735HYNWWrWYvgrVvCuqYJQzQyeK_2EhZJ0I2hDb3b5W_pwcIYjmY6e3p7Y3gTUhU7XkMhF1Z4jPY8skkAMGYKPPu8SxuFi9UMRK99y1Ttbrsri9ICPMSu0aVLoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7GmgF6qDr5cVkJhlKWZuy7HubpnNzBhmdDB3G1A_YZBNDUCSpBaxJSx1mG8c3vAkiHaCUrPHNGg-gli15iVoLgvGpX-iqqY48M6EuVB_h75dOca8A0-Kp4yPUqmUgbVNfbHtMV4V7dk_FVod4H3KPGZA_EfyqoIPJKegWN782Li7gzlLV2JdP6QoIINGd8Pzo1EY9QXx77Z8aS5WY5_OBPJBrMiW3IQ8TRVFE9A0hbHvPZk9kma2UVszRL3i5tWuY6VFIb6RHeaTEo1BPWNSuFE89NGydttiYcKmnqDxhP6W6mEYMls-yJBvnqg5VC-W5EjSQ8mVrIGDqnaMC7rsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gyq2Upc_cxccoM-YsLJ_cGctNbqZGoDmxVj1SHgfMK5bL833tdXbCLJ6KtOafE2OswgW9Kd9NzM2f-JzXS45R-1wnl6yelZkJJTf0SVnyEHKIragtffi7Y6f5zM12rn831EFeoVzWteTRhbZCEhcdYM-PAMhxbU-AJtIxY_qihdtZxpF_lswc3xCcQy7UHiOOgGxAYY22Qti66xC-dEFRIKIZsYu9zcHxpSgXJ09nwD5-9Ok6eptKWlc1t7CjJnmKZvytWzFzV8CxYcC5Y6lbXCb5yE7gyGY9qNwKHkrrwmEO63qlgcKkm4QTJqgIYU24ZZFBWG3nU0WFpryIRDhnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuuoW84Cy5gs6Atb3PUDUVKgEXD4USzWMHeh2lhorTLnufL1winh2BTcI6wyZCpHbPsp_22WV1gAZu5d5g2wvIcldJgnw3yJELGGSJpju1rnLnMhsIp-_5iAY-pe0O02Ke5I9LliR-iohyAYnirYy-FBMaRGyiVLWjXePjmIheCv3YKRSVmaf-mj7evxtKwtbfFnijjryvxaMPB6wKDZ66AKjZ_cK_QIQjMeQBrMUM4CBJbsXxNmbKgclYkZpK2gLIIgJmfqGaGc8z01tkw6ZGT3cSmyKhP_NKnRy8aOj0TMu-nv8yjg75oNE6fBEiO8x7CKTkfFSeNtQ_3Cjcv3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6NhpLNEJQqZ20PSyE_H-nUvxDgMIfp4b1O5axZEMWOBTjmlNQ2KkOvDyZT00as9uHnlz4zc_NfDhZjNOewr2mi49ZGVDbM0flCaBgjYTl3g5VrwAATjq5cMdlFWsPxHB3FHnTXhQzaUnibq-KsOQCWddSP0KLxfco3a-m9f6hq4HjTtXPPEz6dIwCTiCWPixf51GrVXKtUSx4Uzi6tX4_ViHgeTBXT8JzkKyILlnAdJ4-2rSmtTRXUTZZYGqrtOXEmSFMVeVWMS_94W3tsUKX-v37TUIyXht9GE7N2xCTvq1a9hcBojKwbUYlS0VSw6rlJ5qqk6PAN4xSWyxiTX2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_738z4V00RFsEN-ceOj_Ym2TgmOuNj7mfLi1KaJkbivJIgWQFggxXj7pjLocNPSSuCuCEHUjmwHf5zL6_KSSb2j1PhxvLvoW79Z6f9SbvxlFvk7sEse5m0BLANz1k8s6eIwT3rh6mnr_OXJLdhab_qsTndxbfZff2bstReQNe1FnaqWJ0Lh6SY2J8qDqHaPLZPLlFpkBRpQCpaxRFIB9OvPQz-wCmowWxeBsc3F5Xn9u8mfOz4X3Wufm0xg7T7N_LTWubWCwRR_ErNMiaaChejS573RedqR6itV05roU237vce33MiYxbFEigKrBuwLnVjCIFQlQi_h1X74lgbffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=tw6SL7LypTojkDZ5LlnTJTlRidwoESBeGM1bptzCuA8J14FLaObN0V3E0_GSnCMVJKKb1qtEtLN5n31QGrzJAHr39MdYN9MDXaS2Q0u3nFh-7oL3Cz-nqWhv4fup3jru2E85KqYW15GK3nhxGNn1jCbE_cFx3yTuNkArhlfytHhWSqVuqkZkqW57MMgZOcLV_5q6loSCVDMLO50pX895atIlC7jPWl3BAIY7rxU87Z1Ie97FJLX2Fvcr6KcQo0MLIVJroIT632fSbOzXGQnisEPTeJo8UTn969t0uPD7EVOwUw95LTESKB7gxm_u6bGpifqfidKuacjelGUkV6ESDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=tw6SL7LypTojkDZ5LlnTJTlRidwoESBeGM1bptzCuA8J14FLaObN0V3E0_GSnCMVJKKb1qtEtLN5n31QGrzJAHr39MdYN9MDXaS2Q0u3nFh-7oL3Cz-nqWhv4fup3jru2E85KqYW15GK3nhxGNn1jCbE_cFx3yTuNkArhlfytHhWSqVuqkZkqW57MMgZOcLV_5q6loSCVDMLO50pX895atIlC7jPWl3BAIY7rxU87Z1Ie97FJLX2Fvcr6KcQo0MLIVJroIT632fSbOzXGQnisEPTeJo8UTn969t0uPD7EVOwUw95LTESKB7gxm_u6bGpifqfidKuacjelGUkV6ESDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcmhI0KeklGI9XRIX0j1cQbtPMNPCMYtUW9gOfGqNsDDMOS1chVLpMIaswzRvFL-wwzBhcU_Nc_oxRlO261YjIqw_Go7fKWSJy6hkU75E6kjp9DMtAmgWIOB_sF-gObiAVKX7L5E4niyJHzgi6LavwInCSYoOD-961kWb2m5HJpHKbUUBr8jcqewkM74zCLFxyMjdouaCnGRvcZevdoLC9r1rEvklxhJ1hfusunVIC_1MxVHJvBW6-kpR3OLpodbsXei8B70d6Xr2KXiG5nL150YxbcVMcNJvIkskf3YMTujcBUZ8O4DWmR5tQDX4zJEAM7FkAC_o_8YnJ9R6j-1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=CL0a0lYWM2duwWcEgm6YF3YLZ-6xlXpiTF8nE2CfzA57vvCG8GOWxia2tV7UGZ3mact4ueSvvKDId4F3m5pP_S176q7lGQK7gSASmo-b0iDYAVD4_w21IoJCiGupncbuYFTcRwYtuBs_-uKUJl_ybkp4RYw328APLhPHEtrT82arYbpNiAbxw5gsFMW7GaVDzf_KSDXckq0G8vhey80RyVjSW-Of-QMwTQBBBjjNRyzQFuzlmzoXbbkrfF401SZqA1-aczhDHU99ZSc8MW3QKtWoIjAT1_qgM2oQEPY_3WbTtkH0JoEMiVxBMj1aF8ZGmKcuM7CNRuM5Rhg_g5ch2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=CL0a0lYWM2duwWcEgm6YF3YLZ-6xlXpiTF8nE2CfzA57vvCG8GOWxia2tV7UGZ3mact4ueSvvKDId4F3m5pP_S176q7lGQK7gSASmo-b0iDYAVD4_w21IoJCiGupncbuYFTcRwYtuBs_-uKUJl_ybkp4RYw328APLhPHEtrT82arYbpNiAbxw5gsFMW7GaVDzf_KSDXckq0G8vhey80RyVjSW-Of-QMwTQBBBjjNRyzQFuzlmzoXbbkrfF401SZqA1-aczhDHU99ZSc8MW3QKtWoIjAT1_qgM2oQEPY_3WbTtkH0JoEMiVxBMj1aF8ZGmKcuM7CNRuM5Rhg_g5ch2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMJxM-iXTHGvevrXLPwFSEim0yyeWC8TJQ0cj_yH4wVc5p9yrSa2Uq13mmJlnd1gWCI2XGwY25wy1MvfqecHxWJXMxYbQLSUl_Zxst2ddHsSdjcnBLl4NmWN1HpCht9pwUcZYYLriWuEFQi8wTF6nHPuexZDTVof1mznmPhXW9VpQyADV5Wv9tJg7PWKqKxaz0bd3p3MXj5eHbNrdUk1nuEM6JG4NsLhSot-rKbeaIQbEeYg11rkHyxf6RlHzgCZvAH9VO3ZjwZdOVtPR5kglkkaZybFMptkhPPVRe7e--2YZTpiqfZcJVzglSijtUGShdcehmzWPMueWfiK8qJEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idp8iQoruNxBGLdIxEY0lD_B4tO8UcSSd92T_KzAJwp6oRgQTMU32RAQwcLrHysyHEa7zkV3CqQ7AecSeRWDGEKbnjAuu20-CHAsIl_KoYkWnFO0z10jrXtyZTiYk3VOlkuLiOFnxyzId9qBVzuOK7ncwy3eiRg78d8zNA3IRIi7NA7NNEGemmqSS5fwiIXTesnZNTF_vV26tihkC0tGzcEA-z619GLjwRBeLJeZUgd2SjCnYKKAffJ4F2HkVAVdPgn51oPra8zTvMD8dEfucX0cn1Z1bDb-naHy-qQ1E-i4a5iJ9HySwYf5IdqrBt7ZRA_L9K6Zo_nFLO9BFEEo7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpNg0PkLhsd93psNMSZtSojFXwpwaDc2k9_pTI294DKTA1_ea1uvBpaYViia4ZuizRm_nlpU5t1LBXOi2sxNoL4woYOQSBt-uhyqaNz4CqxPsOZyfm6oU1055kUWoXMJ8BXiaWuCUI7lArYvGCnhz7HXe0t4dqzngoASdCpzCgFvQBX-83xvHB9rzxmFVYUYxH5Qi6GEZ6GlLchdLv13POKggJzJF4WaF5gMVpUCt3BaqfFAOH52Ugyu1OCc2UvPV_94p6h7GRZSUyU2bitvjJ1H0KI1KYY_8-4cK_4ARuQz-gVvj9CgM6xSVJYVga3ljYzs0DG6L4e-MwSaKWJQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAdXfvl0pgsbWdtKbpL5xxJCSLG8K6VzmeQxCiaPOe8OrR-XJIlzgWB_dhHhxt-bmy187F-xI1A2lC81HWF1PFGeHJIUHV0a_Kf4S5dYX5zH2xIBy-CENHNt68htIEQ12qz0ZIu3dL6g7E8BJebp6OcrNLnkQrX_MnFwZk1dnNP-CXeoI-1DQduavYNEEO4CWeawsD1JjD6-F0nPviExMaP0_X8vWQg4X8OYtiadSEj6-pKDUHhxH9RGieXFO-cbkVSi_TrUZ1n8Ucyu01LcxCS5K_2YbXwGGlrPwCBpvowuJ1b9Up87kibxgTsh6ZE7xH0xuZo1LcNc-tJtVmGEeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2Xoe230fuqji4KrVJEBWTqER1kvWX_02lVkzHdZI9f_M9IeUMu8T39-VgZO__yVX4vTS-Jbm-BV5SncpUKKFrZBbnh5r7yNbrLoqpUEEcpK7HD_an8z5lJxOd63fQJB_B6h14APjNdga0eao8Zpu-kampLMKy9QCXZTgvq1tEPS1NKLWxKVZrTOA7HoiteClp12RwTE4S7pAWp-0sVcNPq9iHf3vmEpBcmX8BC4caeK2J5xXkX64KEk7cjBvFDAbPliOTAKp1Wrm6unQLDimdIEqlZniRNQSWhfiSdIkux8s2mBRBMbOJ1m9ouu2vTcWk_ZS0_om24vV91XdGBvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvMZnBoJRSh77SiVb2zOHbQMSf_jRd1F6fbhaWyV0e2ODoNY-STLqQ-uwDS1ejGx_-_AHGCRVtV9XMVFqGC6Gy00DwP22k_H5zDMrSWc9Rqde1SJDWw6kqLSTaYwR_PEaLzlSuBU8O06w-HMkvZjgtFCYAj-g6caMY6ARh0wqRW39GQYF-RG4x9lhwdvZuErMmc99ZG9x7wWCuDFBo_sOQgaj5v_QvPfA8IyXKU6Ls3eASsVnLDf0TyU16rd7DiL6NlEBh7ztwebGpB1PBjYGG12_zUzArfiALZBCbXb_Gqa_YPnDtq9lGw0mEGjmfa6GSKsdzVSzKEwo0MMHc1iHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_ISY0jiOo76p6bx9RzW6vclmI65fOqmD7_nPgBCfFe7gz5QEukLvd3TgoUAfKhd8FoKTDrzf-o14oAuPQLEdtlwDnGtwLglGEybpn-mUQMpTmtyPQVUj2AG2qW3PC_LvdF3xcPRVFDFGdYaqrFuXFroWy4dPZflRz7HddmcQbMh2jjp6BcHG_ZVA3kQWM9FN1PDufOXyCQombc_5vPWCbfQGQBa_77YGfjeZc52Z2fYNsic9kvRLOgtn1hKOvbbLzrDziwZ1A8e64ZtQsT-5TFC6yeq3cBAlOQ3upnIhpLU2zmPNKx8hfD_2abHhorvujjm7WcCjmDlhftRJI_TF9WVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_ISY0jiOo76p6bx9RzW6vclmI65fOqmD7_nPgBCfFe7gz5QEukLvd3TgoUAfKhd8FoKTDrzf-o14oAuPQLEdtlwDnGtwLglGEybpn-mUQMpTmtyPQVUj2AG2qW3PC_LvdF3xcPRVFDFGdYaqrFuXFroWy4dPZflRz7HddmcQbMh2jjp6BcHG_ZVA3kQWM9FN1PDufOXyCQombc_5vPWCbfQGQBa_77YGfjeZc52Z2fYNsic9kvRLOgtn1hKOvbbLzrDziwZ1A8e64ZtQsT-5TFC6yeq3cBAlOQ3upnIhpLU2zmPNKx8hfD_2abHhorvujjm7WcCjmDlhftRJI_TF9WVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=g5Xdditz5wuUbRi9KMsB7oS8P1YI0OPUlLWaEFUqTXwfLO1ph3GjCq3JdBVS70iSnYBVWn72ZLUI-QqPzGCxtvnprEM7uWpD0_Rk-so5WdDlVqK9WCrHQRNPqMKxIPHLGMlsCBp8jMHy99kzlOIEz4yHArV0zXMdhsIguMA8q9H7FIegLgdAQVx6IHmzm00uLDh6czO0FyyO9mkoEoXa2bN2m74CZB7dfS725p0ArJTVkam7zWxMysN5TL4D380o954exrxhxOwOmh2O4dqvCO1QCFDLTBr9--68IzqJQnUKKYKNKB9pL7MXCjCzCy0ZQkP5qIfgtn1huLvoBoMbKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=g5Xdditz5wuUbRi9KMsB7oS8P1YI0OPUlLWaEFUqTXwfLO1ph3GjCq3JdBVS70iSnYBVWn72ZLUI-QqPzGCxtvnprEM7uWpD0_Rk-so5WdDlVqK9WCrHQRNPqMKxIPHLGMlsCBp8jMHy99kzlOIEz4yHArV0zXMdhsIguMA8q9H7FIegLgdAQVx6IHmzm00uLDh6czO0FyyO9mkoEoXa2bN2m74CZB7dfS725p0ArJTVkam7zWxMysN5TL4D380o954exrxhxOwOmh2O4dqvCO1QCFDLTBr9--68IzqJQnUKKYKNKB9pL7MXCjCzCy0ZQkP5qIfgtn1huLvoBoMbKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqLRcdCIHNR9i3sgMLFdkErYwwEHqRT3ilDgv6YHqWBf5uaxC9Ufq99m5UIzFcUxl595DF_kTydV7zTFJ6NyBVetYsVntsSDW8upKgMCYQmgq_0-J31tCKWrnbDkDSGB4QKaBmvfdM6XDCB1usEvJcsp1wfoSZAHeMflWIkXW7y7tBFncJiWpsUBaYWUIQZXB5kz4YUWwe8Y-7XrGoHVOC-cCnHAnKPB9vm7oESypNWRzTuHkLydxKGNtKnN20T7lWfwzJz72MbtNfW5uqpNh30OagSPKibQY6C8Zgw0JWPds9xH96MMWaAvNk-I55mzQNLHO_TMuu7cCrPOm2NFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhmtYuvxFKKP7x1eShnC6idrv7fyNb6G0THGwewzrucF4s1Ezy9ml-7hfLF8QYOfal4dT48wO1HtfPUfUwBhpQObGwXelTQ1RFocvFTfp5vMxqJiBQQLn49rHIQGEIN_-MyBioG_B7WvP3wF5h7iE6cQn8d2lkJuVurPGzvaFgwszs8b3jXE1K49acKmRAJMESTWJErQyp3wV8lNnXuTgt_FfXoqIHzrMKofPHmwFYrm_OjRHDRHyBY2XeaC72QXvcNRRxfIuUy9VXOWT9q92PiwFpQPzMVdQKegfMFfpoUTob0E-Kh01DddG4xOEW_RKUbGRaCFQyBsGd1NNB-Ohg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhuGrMyfY_df8uD84NH5cAZ9SCXF2h3yFmK0B4dMZh-oV0y8-0Ifksaeec3CEljdwdlhAUqQtmL2cFSFBEh0LYmXGrtQz99uGPbCMl4sInDaVWhQLe-IRRDyFDkHotYo19zKC_VhY85tWgKKoIuiFbFJpiRoEFgJttryl_YGZb0H4zjUgCu_nsXbrCesFMBm-139GZpPcdb1BfpWhTrW9EoILKc3cxcWgWAVfodX-GjK7q01XqoENb_CufptS6rC0OQhPJm0rlQPIxNzIh-7aUEspr5BjDJgqh6sLFOaNd1dzsgdY6Q8EyzyQ0NnnH0VrmJmYjxTdKHvRauNHdHCtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ellkstdj_jGES-urKT9s8775sJCGwZ2Q2bOl5zGeuDlPwkQUXBOVoio4c878Erzw18pLLPxwBaDRUA3yScw0_kySKOjeN4E803d6fEm7T9M-vXaCeLsO_WTVmvNtn7Z93Mjwf3C2rGfXPvgE7y8OZD-PYE7Q-F427CInNsKtLpz0xRpOKypYnKG3Ef6vOBiDkqz5DLSpOyF6pbzVoolk0P7MvAK2UD3pllgbCX4TQGUjKliHJ9Z5O2Q9RfEtHkR6KIAWC4NkjbXQ8alYdPNXr0tNhnXn9bcOQiQpacj-ToF3WWyjB33eOyZDJsF10HFfqhcK7AXoIeBR0namhO8-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSo0kHQ2tqOe4BpTa9Z8yQuieGMZ2FHH6d6-mcP3ne6x_A8IVgECcCLy3t0Ihr-BPSlkDDO6m6JkwGtBUSb4IIDIZcq8kbtXHaPeeggaTAZXBsxjHq62HZD60Dxkk4MalYJVzhsXQzxKmSlQyPY5DAAXmK30HIRB759CVKzsHf4zDrTRcuxo5PfDUWRh5Es7tuRp_97a07JupOXRf5C_NRpLS55jLhy4ByvK7MDaAGirkafU-npCpw92dLlWAqDOxXOW8TLwzM1bgUR0rlbfrWX-Dm4dETygSoKs0Nqi2hhr91VG0bFYuFAEvuel8Dqm_6RSleIW9wxgOgSc-L2vvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p01JIRZwcXwduzrftBHM_0cxSmpKoJhrCCcR1Lw4_VcZsiqoVrgWW7C1gHPwBEOsax8lflcZc8WpuFw28HDTrp68JA-kS-bfg5NMb-AXJBJsP3T5gNp5lDeib0PLll_0RQkoCJ2FztkoY5cGy0FrvuwQmpstMDl7c3pzdvzmkVwSM1TAenuAgZGurB9m33Zndo9sD1bqwAppW2OsrXBF_EVIjAtd6VwNjnYJVuukJbAOMu7HTmbls6OLTKppt-bywWWgx6UhmHMFaJflDLX-t8HCLVKDznEoJ8jwNeyBoyem8sRhnnGtb1Mtl9QZpmTKcFng2juNWnCevLrdIFmemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTHV0VdkJ3gLgSEV01I-E_6D1WFSL2BfTRXKn2USdZkofOkTdoccRrDUmLTuzek3g6TseJwFNS4g_sy_KnfzDju4CGHaswsQCqhSEs2yLk0Cf4_YggRzBHYY_McMNMa7nEU0-8DEYYQscL6DOThX5nQ6PYelHg6pXBxBUABIbUOxyLEw8jYplmaFJWhvJf8GShsXjlccubPd-ifPSQmuhFbtEsMsNzQcwjEMttytmxCRjTefJlN3J1K5_48jyaL87os29GD0hT69AnU1-mtwO0C6fg9Swk3gcm_Y7JheQQX46ozZoK8Kv_Kpf6iaB4hWBn4d4V-U9s64LDOp2mGgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxV8Xi9acbeW3AHV-B7DSqaunD3jl4Uk0baBI0Za40E8WAxsUvzIrOd5fTXO_VYtuCHRVXyzNdoCWvh8kmmkWblUX-XuDa0tqf-zPnIye871Xw2TjuLZ33iH5NEe8SZhK4BMruAdOzIJhSNM4tixCA_43YojD5gqgKgP6xmB2X4rFwT_hrAvVkBeAZU9SC2alL4wQOFMesRWHMPsqcZeql4RBLu1GLDv2OsK-yZb6NJe424wBDZrZve7h-3Ud8ttjtf8WBLirx13wYT-n5BRcYdLrW9h9z-kWtJV-Z8b707TQTNkqq64eQTYQt8m4ljgFkZriqg6nsaIPdMhouReEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgfPawXrgVZdi0upjmatC8DJPImAmthL8BVJjXGchUac7tEgN2JIFxzlGSDpJoxASC_9e7EDWLsLeHgsCs216YFNcASKQwn6MLJygMQoeq_CYH-b5zb8Nxoy1hArWkgkfa-yDmKLXg8-ffkI_px16aM8BC67Zq5uTpP8tS4LwZ-KFoRuJQEH3zIEV7Wawbt10eu4AYfLvQKTRxD6e0hxdCusiPCvf73guGWAkRKXri5je4NvY5jwL_NO8f3fh1YQ0k54Q4rh7ti7jU3FmfwudGFj8I53zgpX3M4TAqpSw9pBJiqcBb0rVw58rS46mg4dvulIXEUKz6THljUMM2_h_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q43leqVcFGQDwNL5QopOThB5hw1CKcNw0OtmG2ZwlpdlTdqS-stt7an92_D3e5DA-ZVgi73NzLzCmV0Wiag3Dw-qakSvvO6GylHZ81zImatjkzNvbnTYWA8jgBvBGtwxCSVK5YmWyeIl0wRe8FmEbKBmY_N4SepEWszaxdYbZTZ9WywWqBA8J9Cra3tDYyTZ1w-IFYpTZCOo-jcjfkKNjUhxZZ9Co3gl9fVdFwCxR3iqNtp0p4z4o2tDUhboJtU3PZm6g2lBlPxTjvc9x0TPW1mqoGUDAQYt8rTtvoV4kbLp7fscQehI247os9upm9hAqbijGTR3GValRZF0h4eiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=R1_2Z8L0mbZHYFVwimyrPKOR8x0BLVkT-zl8dRCeciXmTNxVuJsuzbzH5ADaa-TllLcsXMXjC7SJWWDmhHgdjlZTcYCKpKbUKcyNRo7DPtcSGfxt5o3sJvXCVcZVUfFCMiicUW5KFHsYdIXYTcwQw13Jcoaiel6kvrtYQFrsarcKxX7zzKKau71kqJpU163-OhZGt6nPLYGLvFnVLlISiYUcr3wzaHMQENERZOiL9Tw5R_ScxDL4zzQ9vuqDBAK_twYBxUmbrBzB666aaMfNFDJe1XsCNTMDUffyLBwWFSiAJ_WcUUdl1sAte-yhdKdeoRC4u-jiMqZREcUcdf3Q0Hv8rayOMMGNVqoQQZ997U6FMwE6guVimuakCwFSsza8WG7JjpDwD-jlCpUPnpUFEkidbFaFq_YXD05r4-V61xvR_xWfHF_Y7EtLxy5Nuapg2Rd4c52zQurZURjWOlBz_xozYrplkTCqQxBnhXddX_uPy0r7977Y5IrwNqB_AnMCkDYzff2u2EsPKQG8w1eOHpZ34T5cjUiBu0d-KoYdGCnBISt5UXg0fAYZq4yb0UZERhhXnPMylQoRlZyqsucUhMIjVBuW0t-oCvhZelQXltyqsemMAp_60NQRfKrkh_k639bZ7OoyINTUT-HAQWKT3qCr7MU4g4ewSY_cxDendiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=R1_2Z8L0mbZHYFVwimyrPKOR8x0BLVkT-zl8dRCeciXmTNxVuJsuzbzH5ADaa-TllLcsXMXjC7SJWWDmhHgdjlZTcYCKpKbUKcyNRo7DPtcSGfxt5o3sJvXCVcZVUfFCMiicUW5KFHsYdIXYTcwQw13Jcoaiel6kvrtYQFrsarcKxX7zzKKau71kqJpU163-OhZGt6nPLYGLvFnVLlISiYUcr3wzaHMQENERZOiL9Tw5R_ScxDL4zzQ9vuqDBAK_twYBxUmbrBzB666aaMfNFDJe1XsCNTMDUffyLBwWFSiAJ_WcUUdl1sAte-yhdKdeoRC4u-jiMqZREcUcdf3Q0Hv8rayOMMGNVqoQQZ997U6FMwE6guVimuakCwFSsza8WG7JjpDwD-jlCpUPnpUFEkidbFaFq_YXD05r4-V61xvR_xWfHF_Y7EtLxy5Nuapg2Rd4c52zQurZURjWOlBz_xozYrplkTCqQxBnhXddX_uPy0r7977Y5IrwNqB_AnMCkDYzff2u2EsPKQG8w1eOHpZ34T5cjUiBu0d-KoYdGCnBISt5UXg0fAYZq4yb0UZERhhXnPMylQoRlZyqsucUhMIjVBuW0t-oCvhZelQXltyqsemMAp_60NQRfKrkh_k639bZ7OoyINTUT-HAQWKT3qCr7MU4g4ewSY_cxDendiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKmx0epJcdF_09TiDVlAlzLR6kr0_RDF6mdyTYvyRIuL00ZQzMB0jOtPbK7Fexehlwpnb2vq5oMyv187PI6khegYQsWtRrk8T5d2y9qK9oALNazkZcCJyCx1c-rcgPqegFXqjwkRkb4vx7ex3X8zlNwPMaDKZU3k44ksnUCLEeqtoCiqLgznwvYDGB8aZnELRO4lY0kq2zXN08hpjaG33Nm9rbITwXvAces1QrceMoZNfEmHMMc5xBP7snc-EB3DdDUIIs5lDULnLklPvAUczf7XeDx0N6rv6bzVip3qb4oc7VcQ0OzVj6vugMEYUMZpnMBb8biOYyyhOprKTV0CwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=AfdktKlNDXQ3fj62RAzSKM_jQV9aJ0KciQ4IeBgOkQTm1qVyTMF9haCIBLSZCHq_edrsk3LJN6_APhkQzQyb4ccOocToDtNnPO9HvbhXEYm9lyPBjMDgQzgr8Vnu2PrzJqvYJ0KhrmjQWQKLK5T26We3anR5aIe3pqMRU_CWgRMzroMh5hVP79IuRo6ewxVnCfuSHGIVSQ1DZEjJ4Z0donlNqHwEd8T-U67UAnyguqYWpGwc-wyKbKL7GRCvQQNyn6r6bta9uojARf0ttnknvENFlafBdnCIZ8ygpTrTm-Srp0Kt5x7yef7fnJ0hR7xKjKlopHSXPXVUmE9o7vDdOb3osgDUYuW8OueNeulUaIXikMMS9BhsT-drdEcPZb0WvJaJ3APKjbGBN0gGAPZiLAF97r7jRuS-Sl-FDjnfWOtAk4jqhvN2zL1cmzcp8kC4Y0TVE5i4D2zrDUvEh0bw8PFFw6amSKqF94H_EGQUizxSn7KKbdvIer-mdxrlMnErJro7XD6bsRHBhQ1uSrjMKe9tRtfRQmULyE--qoVv-Cbd0sD0oJneIiu3lHj7FdyzBwNMDb-64I0A530Ih8W5WCBtgikKlHSEObDv0GlyIsK5oS5nVZweq0t2assb8jT-v9JN41-mFfQa9Q-6STFLBW4jZueTFCGHtpwgJdf_hGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=AfdktKlNDXQ3fj62RAzSKM_jQV9aJ0KciQ4IeBgOkQTm1qVyTMF9haCIBLSZCHq_edrsk3LJN6_APhkQzQyb4ccOocToDtNnPO9HvbhXEYm9lyPBjMDgQzgr8Vnu2PrzJqvYJ0KhrmjQWQKLK5T26We3anR5aIe3pqMRU_CWgRMzroMh5hVP79IuRo6ewxVnCfuSHGIVSQ1DZEjJ4Z0donlNqHwEd8T-U67UAnyguqYWpGwc-wyKbKL7GRCvQQNyn6r6bta9uojARf0ttnknvENFlafBdnCIZ8ygpTrTm-Srp0Kt5x7yef7fnJ0hR7xKjKlopHSXPXVUmE9o7vDdOb3osgDUYuW8OueNeulUaIXikMMS9BhsT-drdEcPZb0WvJaJ3APKjbGBN0gGAPZiLAF97r7jRuS-Sl-FDjnfWOtAk4jqhvN2zL1cmzcp8kC4Y0TVE5i4D2zrDUvEh0bw8PFFw6amSKqF94H_EGQUizxSn7KKbdvIer-mdxrlMnErJro7XD6bsRHBhQ1uSrjMKe9tRtfRQmULyE--qoVv-Cbd0sD0oJneIiu3lHj7FdyzBwNMDb-64I0A530Ih8W5WCBtgikKlHSEObDv0GlyIsK5oS5nVZweq0t2assb8jT-v9JN41-mFfQa9Q-6STFLBW4jZueTFCGHtpwgJdf_hGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
