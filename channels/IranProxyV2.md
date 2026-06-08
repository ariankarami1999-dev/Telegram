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
<img src="https://cdn4.telesco.pe/file/CpDNCGCBOys_7KCqsyvfevYCMeTzmZYcilVXWSPZd3M1a9g26nkAa4_tWvYIfw4g9QmrPtYkFhum7uTiHghA6pucmb-fLYfidogzw8wbboyv-Iu9nbAorZEqDRLLnJ8k1syoaoINIQnnA-dDkgKznvWOv4jPXuT2ulsKSkZ7U2dhbgJHvMOiihmKC4DoZgRl2leO0VmhYJ-aL5xc0gq3nzMJwJ9WVrJKQGdeFg67p-iGunITkB-zV1K8ycIZfKoIMU8I9whF7AyqghdERxDFygsVfD1KWK4Y1XpVHYOyLJaQ-6SB89tTb-OWRGca-pfmHsvM_Bvp9TAKNIite5ywXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 40K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 05:08:07</div>
<hr>

<div class="tg-post" id="msg-8945">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
آغاز حملات سپاه پاسداران به مواضع اسرائیل به گفته برخی خبرگزاری های محلی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 334 · <a href="https://t.me/IranProxyV2/8945" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8944">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EckxBoekabQisrjA4CsTi9RNMNje6MpPddmdk8qdo4bUuv1xhEaoodrvdU8EMcK0QJSWJcKILY-DiXynyCqr-ym9PjFFKX3mVvPPBmxmpqiUUMfg7fJ73pbxdsNieG9vDgiBplCcH3PRNRzoCdmm4Ksz7V6Zf-QYSkBlKYKRaf9go6OtizrU2sq0U0_6pGEclYEGqPp5ceNBUVxo9qwumx2oyC1VdxoOL2EQBAraNv0ZTpAiLzeI9k7k1q71kDyUYCb7VNnZIfqQlOIw8K7lH-52YL0s-bJrmLFKdT4AC5u3l8eFRYNOGf4t8OdlzzRlIB0np8lC6cYjWizccm8KcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به کرمانشاه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 365 · <a href="https://t.me/IranProxyV2/8944" target="_blank">📅 05:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8943">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
کانال 14 اسرائیل:
نیروی هوایی اسراییل با استفاده از موشک های بالستیک هواپایه و موشک های کروز، از طرف دریای مدیترانه به ایران حمله کرده
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 427 · <a href="https://t.me/IranProxyV2/8943" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8942">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzvJqd1FxiEsWNSPnfdmwOIBEHifuBz5Ot6An3W6p7zTSTBvbCeUw_eQ9ATwo8Ba0fl6NfX5_5qbDiN_G5mP2iqlLzDmSmZZwqSQFurDcbInALp5G6VIxEBIHMUsOZGoZj686PqrEJCm3mtY0QLIdmek2e_mVi3N2Wg5Jz9V9jXsv4LdedV7q02ACsvD0DIQPX1AulFL7uO1JIug4R6mcBjng9GbMHb_w_PncwbqxZdH7Xuy1dLvA3TPQ33uqz1dVRQRcygxZwCyOpWRzaBvaGqVwaXW3IjubL8dK2sc_pQHJdW_DiSJUiESDzthNnkGqpw4LEJOqdz2uvgUfAuXOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کرمانشاه رو هم زدن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 459 · <a href="https://t.me/IranProxyV2/8942" target="_blank">📅 05:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8941">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue_w2sx3MREPTe8iBe_c8D4akQE61tOerf71CVnAu-9KWvB2iIZQssNzkvFMEeXDLhphh_MZl2tKMkOHA-M_poYRRj_w4FSIhoZ2o6eBy5rwT39Bsn4lqy9VlgMlWBp_2dfiB1IiB8583hS0CSnoTszTNvJYFdM-SMb0L2plpgOrvsU7v6X3Fqg_B3RYkVSWEYbg852BOoL9-KN83nBnq6UOAkHV7BWSR7jqrHvrtpimkFC8N_mXapjDta3uPGmMQm458JOAm5wNEZWmP4_dltwAFMdUYq5Gm4KL69Fwo3T7DAKHBSc-jDb5dciJglyu2L8LZOK28xw0tckNcHXHaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه رسمی ارتش اسرائیل: «دقایقی پیش، نیروی هوایی اسرائیل اهداف نظامی متعلق به رژیم ایران را در مناطق مرکزی و غربی ایران هدف حمله قرار داد.»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 580 · <a href="https://t.me/IranProxyV2/8941" target="_blank">📅 05:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8940">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAvMN8Ax9HdYPjVictGwsnQzFny71XJAgY35hypMafuqMmRRcYg4VkXdfTevD0uKEmQXz7Xuo8swoDlL6A3Gxs-N3VEzTpw90sLCF7F0Q2WR35HvDg98JnNzTEKfEDK4qs_YyrHneQvs1PfB3HwHClf7eK7SHta5OiqTzNFyed7bx1bv1W7yQ8jtfUH9DITzv404sFlmK-yOSa1OVZeyruFCTppNZFOxRJllIXKtCk7oYFC_b06sUZCiB_RobPaMCw5-nxfdQcqhA6rgZO9IwJoS8q2MAjiaLOdKcv7ZU99elIdR5bKY4-R8m2PNpKTLHbeVpCnqOCNnWRnNhmx1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
صدا و سیما حمله رو تایید کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 707 · <a href="https://t.me/IranProxyV2/8940" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8939">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_Oyj5PMk85VSKeCnZ2nzY1z80W8Z-_iz36eeCIJAz43BCQnZc1LvDOmStUSWiAbqtIIhDsNGBqpPB4xxUaVyZ69lVtu3RicFohMvnenfzPLThE0Ce_i-_TGspCNGRi2ml0Q69XqNwcGAR-lunVj8ZBv86WjoR1-Bo86zwFkr5L0LbZZjE3GXnnRLikTV1rgQQSEKDH_URCH9GnGP-fBcTv3OxFndL00DTxOxoAD02mzkxuHLjuWLOqxbIvYAfhczNxrCVtPQx8mTSr3HmkNlGVTK-6HGuiw_ZVLZFkPg_gf7mE_S1CZ_mKQyAiMJOwf1UuP1oJyuOsKPbAJigWGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار تو تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 797 · <a href="https://t.me/IranProxyV2/8939" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8938">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
انفجار در ارومیه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 735 · <a href="https://t.me/IranProxyV2/8938" target="_blank">📅 04:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8937">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RT0HRjJbPP_uM-PRlEVDrxlzShbu6EvSDr0WDsFCamFkrQD5wdF25pnuNGQhjLiK_dNn7rij2Y2K_JcHeG5eNQerbXIbU8DwOBYyb34ufPmYa90ZB4vahpX85d_X2AlTUsVMbhYl8-R3rySlzFZkMtLZFQJUMZtcY2ZtePJeenZ-PDis9B5p5zNBYQoh3buenvpwqKfiWIqa_XzCiG9JXAArQfdypQeWG3qh1x-HWDB5t0QunImz1M4DAU3uwcCQk3oQuEoVVEzaqie3pRuFWFxdW-dtJGxcTK0NGFNKLfnU5EkGQJTJzD3fujAyK5fC30Io_P5DI9ZtAGWZakV5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شاهین شهر اصفهان،ساعاتی پیش
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 766 · <a href="https://t.me/IranProxyV2/8937" target="_blank">📅 04:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8936">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
کانال ۱۴ اسراییل:
جنگنده ها دارن وارد آسمون ایران میشن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/IranProxyV2/8936" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8935">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dct57ePaCDGSDXrtGt7tGWSiUjVDwr0hgFRC5pMyoZfTGS3eKaqKzrafNR477pDXj-B9dg-qgd-Z_lG8SkklGgtcfNUk49MkxCmk7xRJ6EUAW3PCHrPIV10fFbSEiL77KdRjC6NTwpujKHLS8mIej73vY9yT43d2Q4pHltAwaDMlva12lSr18B_2Xc6CazHg2RM6TxTfzuVEEdP-RJkwk6hmzNPLTLomx3wIi6anyYya_81Pn7yzlEYCnVW8hjdRNBXf633A1vgSYAlgazaX_rEa-67tXEoj0eixRbQq6_XeKrGLQyvM3AXrA1yTxRIm2VQgt63XEmczbz00QT_nCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یا خدا اصفهان رو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 767 · <a href="https://t.me/IranProxyV2/8935" target="_blank">📅 04:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8934">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYJfspj_LQWVZaZiG7KKPfaKXD1ijvLQw1rv9Tk_jCugZqu5l3U2g6M38t4siANiV4bP3PhSxJp73rWC4X5Z5pCK5qlCOG5l_akHp5T0FDmXdkOYYoQMKhV5vchjMeUr7YVvQh4qGqDna83_QQb9xBej5kqxRQjLJt4jLaNNwNXhjZsz-y0YGIjVFJbwCJvS-C_tT5jNKGZF_pTTV8zL65tJj_9sSuz1nVPUpeQUspwnQm60PsOJi9n0A-_cY43wbYDk_auhmRfYtDTUYuALwt4KFJ4GZUPmV0PZHdKfrzGD4slqbRuKMPZRmwUryHWFWiD6l5UHvoTYMXGAhPUsOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نجف آباد اصفهان هم اکنون
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/IranProxyV2/8934" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8933">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پدافندا راحت بخوابید مردم بیدارن
😂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 798 · <a href="https://t.me/IranProxyV2/8933" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8932">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">💥
شهر هایی که انفجار گزارش شده
تهران
تبریز
اصفهان
نجف آباد
شاهین شهر
کرج
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 797 · <a href="https://t.me/IranProxyV2/8932" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8931">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
همزمان تهران و هم زدننننن تبریز و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/IranProxyV2/8931" target="_blank">📅 04:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8930">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
اصفهان و زدنننننن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/IranProxyV2/8930" target="_blank">📅 04:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8929">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏
🔴
فوری-سفارت آمریکا در اردن با صدور هشدار امنیتی اعلام کرد گزارش‌هایی از ورود موشک‌ها، پهپادها یا راکت‌ها به حریم هوایی اردن منتشر شده و از شهروندان خواست فوراً در پناهگاه‌ها مستقر شده و تا اطلاع بعدی در محل امن باقی بمانند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/IranProxyV2/8929" target="_blank">📅 04:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8928">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تنها حمایتی که میتونید انجام بدین اینه که ری اکشن بزنید و فور کنید برای دوستاتون پست هارو عضو چنل بشن، ری اکشن قلب بزنید رو این پست ببینم چندنفرید
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/IranProxyV2/8928" target="_blank">📅 02:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8927">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">+1 ترابایت دیگه برای شما دوستان فور کنید برای رفقاتون
🎁
❤️
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@deadvix.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%A9%F0%9F%87%A%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@dep2g1.aswall.ir:43582?encryption=none&security=reality&type=tcp&headerType=none&flow=xtls-rprx-vision&sni=play.google.com&fp=chrome&pbk=95vLe0hBBerV1ch9WxJ9iPTi4u7V9NExNADg9-LpcwY&sid=025086f1385a838a#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@dep2g2.aswall.ir:11000?encryption=none&security=reality&type=tcp&headerType=none&sni=refersion.com&fp=chrome&pbk=YWfCdTnr4FAOMYTY2dLrMtQUokyxOGpPhYEEszPj20E#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/IranProxyV2/8927" target="_blank">📅 02:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8925">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">1 ترابایت برای شما دوستان
❤️
🎁
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@VIP-Vanguard.userid:500?encryption=none&security=reality&type=tcp&headerType=none&sni=www.chess.com&fp=chrome&pbk=OfqZPHXqiwjyZEhZtVO1kk9PLxW2ueKdaOjVX_Br2Ek&sid=ce7d30ff97b02e63#%E2%98%98%EF%B8%8F%20980.71%20GB%20%7C%2030%20Days%20Left
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@50.7.5.85:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=dehone.tunnelltwo.ir&sni=dehone.tunnelltwo.ir&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@50.7.5.85:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=deadvi.tunnelltwo.ir&sni=deadvi.tunnelltwo.ir&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@94.140.0.0:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=nlox.nextigo.app&sni=nlox.nextigo.app&fp=chrome#%F0%9F%87%B3%F0%9F%87%B1%20%D9%87%D9%84%D9%86%D8%AF%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@94.140.0.0:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=usaop.nextigo.app&sni=usaop.nextigo.app&fp=chrome#%F0%9F%87%BA%F0%9F%87%B8%20%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7%20%E2%98%81%EF%B8%8F%20
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@45.130.125.60:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=decdnmtn.gozarino.com&sni=decdnmtn.gozarino.com&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@188.114.97.6:443?encryption=none&security=tls&type=ws&headerType=none&path=%2F%3Fed%3D2048&host=decdnmtn.gozarino.com&sni=decdnmtn.gozarino.com&fp=chrome#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84%20%E2%98%81%EF%B8%8F
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@deluxi.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@devops.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%A9%F0%9F%87%AA%20%D8%A2%D9%84%D9%85%D8%A7%D9%86%20%E2%A8%B3%20%D8%A7%DB%8C%D8%B1%D8%A7%D9%86%D8%B3%D9%84
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@usaoxp.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%BA%F0%9F%87%B8%20%D8%A2%D9%85%D8%B1%DB%8C%DA%A9%D8%A7
vless://7e3503ef-2bd8-40bd-a4fc-f3a9f5e787b7@nloxv.aswall.ir:49755?encryption=none&security=reality&type=xhttp&headerType=none&path=%2FStream&host=play.google.com&mode=auto&extra=%7B%22xPaddingBytes%22%3A%22100-1000%22%7D&sni=play.google.com&fp=chrome&pbk=4y6s7HGTYuWB9jyaUIkq0fkR0R9dpCMRSNH4r2oW4nk&sid=e769cc7b3fb496e3&spx=%2F#%F0%9F%87%B3%F0%9F%87%B1%20%D9%87%D9%84%D9%86%D8%AF
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/IranProxyV2/8925" target="_blank">📅 01:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8924">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
ترامپ: اگر توافق به دلیل بندهاش فرو بپاشه، ما گزینه انجام یک حمله کماندویی به ایران رو بررسی خواهیم کرد.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/IranProxyV2/8924" target="_blank">📅 01:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8923">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
ترامپ به فایننشال تایمز :
من تصمیم‌ها رو می‌گیرم. من همه تصمیم‌ها رو می‌گیرم. نتانیاهو تصمیم‌ها رو نمی‌گیره.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/IranProxyV2/8923" target="_blank">📅 01:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8922">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇺🇸
فوری، ترامپ: نتانیاهو چاره‌ای جز پذیرفتن توافق با ایران نخواهد داشت!!!!!!!
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/IranProxyV2/8922" target="_blank">📅 01:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8921">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
رسانه‌های اسرائیلی:
ایستگاه‌های مترو در خط قرمز تمام شب باز خواهند بود و طبق دستور فرماندهی جبهه داخلی اسرائیل، به‌عنوان پناهگاه برای ساکنان مورد استفاده قرار می‌گیرن.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/IranProxyV2/8921" target="_blank">📅 01:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8920">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🎙
مراد ویسی احتمال پاسخ اسراییل بسیار بالاست.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/IranProxyV2/8920" target="_blank">📅 01:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8919">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رویترز:
به گفته یک مقام اسرائیلی، ترامپ و نتانیاهو کمتر از نیم ساعت با هم صحبت کردن.
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/IranProxyV2/8919" target="_blank">📅 01:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8918">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مرادویسی درباره حملات امشب:
اینکه سپاه میگه ۳ موج حمله انجام داده ولی فقط ۱۱ تا موشک شلیک شده نشون میده که سپاه دیگه توانایی پارسال رو نداره و تعداد موشک‌هاش در اثر دو جنگ ۱۲ و ۴۰ روزه کم شده و فقط تعداد موج‌های حمله رو بالا میبره.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/IranProxyV2/8918" target="_blank">📅 01:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8917">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⚠️
چیکار کردید که مردم بیشتر از جنگ، از قطع شدن اینترنت میترسن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/IranProxyV2/8917" target="_blank">📅 01:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8916">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک مقام جمهوری اسلامی به دراپ‌سایت:
در این مرحله، دستیابی به توافق با ترامپ واقعا امکان‌پذیر نیست.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/IranProxyV2/8916" target="_blank">📅 01:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8915">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
حرکت سوخت رسان ها در آسمان اسرائیل رصد شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/IranProxyV2/8915" target="_blank">📅 01:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8914">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تسنیم: صدایی که دقایقی پیش در تهران شنیده شد رعد و برق بود. صدای پدافند یا موضوع نظامی نیست.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/IranProxyV2/8914" target="_blank">📅 01:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8913">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8yeCot0VydxiUpGDwsw--bNe2QNF4iownrm9Nr4mthTCSFUB0FTWohIOyEaRHsLRYBotDj-L62feWFQR-LnGiEbt4CytNUT7H21voH4UwwNPL9KhM348pTdyCKo4t0bAXnoAKs14dX5yqrFbMoogAUTvrLmtYW1KmovnOYcktE3mHnex872PnbpgxqptArTDRrXYWhuuWXMERUO26wVLJXl-DTfR2g9BY5m1RcV1_JRs89sGFBRwA76nM3BNBycOXhMSDP2llu0-SeYH3A77erTf6Gk6aqdwIbhq8FBhHdSLo8CUsEZu4xJe8Jv863M-bILFhfYhxNHrj0WQeWNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پس از شلیک موشک‌ها از ایران به سمت اسرائیل، حریم هوایی در غرب ایران، عراق و سوریه بسته شده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/IranProxyV2/8913" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8912">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
یک مقام اسرائیلی به اسرائیل هیوم:
ما به حمله جمهوری اسلامی پاسخ خواهیم داد، حتی اگر الان انجام نشه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/IranProxyV2/8912" target="_blank">📅 01:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8911">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🇮🇱
منابع عبری:
نتانیاهو در تماس تلفنی به ترامپ گفت: اسرائیل به ایران حمله خواهد کرد
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/IranProxyV2/8911" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8910">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♨️
🔴
نخست‌وزیر نتانیاهو در تماس تلفنی به رئیس‌جمهور ترامپ گفت: اسرائیل به جمهوری اسلامی حمله خواهد کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/IranProxyV2/8910" target="_blank">📅 01:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8909">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
کان:
جمهوری اسلامی به اسرائیل پیام داده که حملاتش رو به پایان رسانده و اگر اسرائیل واکنش نشان نده، دیگه حمله‌ای انجام نخواهد داد
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/IranProxyV2/8909" target="_blank">📅 01:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8908">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
شبکه کان اسرائیل: رئیس ستاد کل طی ۲۴ ساعت گذشته دو تماس تلفنی با فرمانده ستاد فرماندهی مرکزی آمریکا (سنتکام) داشته.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/IranProxyV2/8908" target="_blank">📅 01:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8907">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♨️
🔴
والا نیوز به نقل از یک مقام ارشد اسرائیلی:
پاسخ مورد انتظار به ایران سخت و گسترده خواهد بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.54K · <a href="https://t.me/IranProxyV2/8907" target="_blank">📅 01:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8906">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری
جلسه نتانیاهو با سران دفاعی-امنیتی شروع شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/IranProxyV2/8906" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8905">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری-منابع عبری:
ترامپ به اسرائیل گفت اگر توافق حاصل نشه طی یک عملیات مشترک به ایران حمله خواهیم کرد!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8905" target="_blank">📅 01:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8904">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
پروازها در فرودگاه بین‌المللی خمینی تهران تا اطلاع ثانوی به حالت تعلیق دراومد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/IranProxyV2/8904" target="_blank">📅 01:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8903">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر پیشین اسرائیل:
خویشتنداری یا واکنشی نمادین، این پیام رو به دشمنان ما منتقل خواهد کرد که ریختن خون شهروندانمان بی‌هزینه‌ست؛ از این‌رو اسرائیل باید با قدرت و به‌طور موثر عمل کنه.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8903" target="_blank">📅 01:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8902">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
منابع عبری: پایان تماس ترامپ و نتانیاهو
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/IranProxyV2/8902" target="_blank">📅 01:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8901">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSbe9HHb_2BVkbc-wzuJVhNFJ0PbXIB0vqVGYzTJoE0ZIqjI8WxyxGIz2BuoKjAg67JXRNuD_K107hAd8DBM6Pid_JRvv8LaSpDiFkB6lmPKli2PVA-zVBTDIO2LJNqh6nzfqm18n5GWvkOZmDpNY79xsW1SCVdidA0QuzBsgPYwMR4vj9sA_8H7pFNXpbIMh1i71m9oZY-4kEg1-HxcVoYniF97Mu7vxo76vWrCUGyf_7kTTFra2PTuNArjYDkLCm9ir5nuvOtJMBbrpMu5Z0_kUZGMwhFiG92y_8zXKyNMiQXFT8H0R00E2KmA9Abb4rmg58N-g_w4b1vIhjBxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سفارت آمریکا در اورشلیم دستورالعمل‌هایی صادر کرده و از تمام کارکنان دولت آمریکا و اعضای خانواده‌هاشون در اسرائیل خواسته تا اطلاع ثانوی در خانه‌های خود بمانند.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/IranProxyV2/8901" target="_blank">📅 01:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8900">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
کانال ۱۵ اسرائیل:
بعد از پایان گفت‌وگوی نتانیاهو و ترامپ، نخست‌وزیر جلسه گسترده‌ای درباره موضوع ایران برگزار خواهد کرد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/IranProxyV2/8900" target="_blank">📅 01:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8898">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
حمید رسایی:
هر چه زودتر اینترنت رو قطع کنین تا دشمن نتونه به ما ضربه بزنه!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8898" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8897">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
کانال ۱۲ اسرائیل گزارش داد نتانیاهو و ترامپ در حال حاضر در حال گفت‌وگو هستن
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/IranProxyV2/8897" target="_blank">📅 00:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8896">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">صداوسیما: به هیچ نقطه از ایران تاکنون حمله‌ای صورت نگرفته
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8896" target="_blank">📅 00:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8895">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری - پروازهای فرودگاه خمینی تا اطلاع ثانوی متوقف شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/IranProxyV2/8895" target="_blank">📅 00:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8894">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEpgk9nJvCADnbgqHjHwx_iEn20iAMIyO2U0FjTf7QqTlCDsscdWEyVSBztmthhgquX5zj08vlIRzAArpHibzw_IYG7dg7f5ohJKS4ovqxoIc0iEQFEwxpi514YrnCxN-OPplylh56tCaPXmOpgWeSffO0gtUAwq6A1EyCrTX7h3y_sPJ8rb0vmnL5GSgyM7pbcD1CloTcqXzHZWlI-sLDPMH5hpum23eANYTfUAQd_G0ewYhpt-GRDV6iOhRFnA94MEvl15GjYp_fBADKZRMqRp1iBYUwIkLH34S9nEBgD-0ajTNyH24dx2Rp1A8UVij-6Uk-NTt37cj19rdhrfmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
-
تمام هواپیماهای غیرنظامی تو تهران برای پیش‌بینی حملات اسرائیل جابه‌جا شدن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8894" target="_blank">📅 00:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeBbVtM9onblrgbrANSVDIki72ZIxtL3Hc_Ic0qreWhq5e8BDInO-zfbEdzEGCqh-tx-VQVWrZueZjw5Nu6Xlfm2l7_m0Y6eras0HjL3SD-LJtGULoDax1wBaF7zM4vSNAW_eOb-OVNtH9OJOjbd2UWPz9_s9RqOL1p0mH4YK5dRSS_J_WYDQQUgqEL7MkEtj2L0QfaixfMJWAbn52rKkq3pJvlZQ5ms3a4HZyrchKQ8tai4VCYav2bIxQX2l3BlxgIKySOpWUt8fJP37YrqRi9LrigiGJSIr9LBCUG9imiunvd89qw_p5N8s5KT0onULsRmDxIArnLk7eUWIptA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
ما بهش میگیم لبنانو نزن
خو اومد زد
الان دوباره بگیم نزن دوباره میاد میزنه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/IranProxyV2/8893" target="_blank">📅 00:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری -صدای فعالیت جنگنده ها در جنوب تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8892" target="_blank">📅 00:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8890">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مثل اینکه نتانیاهو ترامپو بلاک کرده
اسراییل مجددا به لبنان حمله هوایی کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/IranProxyV2/8890" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8889">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
تسنیم:
براساس پیگیری‌ها، صدای شنیده شده در‌فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/IranProxyV2/8889" target="_blank">📅 00:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8888">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری-نزدیک سپاه عاشورا تبریز صدای انفجار اومد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/IranProxyV2/8888" target="_blank">📅 00:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37dbb2f6e4.mp4?token=WUmgICBbXZIFRZaFYWERBGQaBF80IJHuXQxfwedv8FoeYbcRrh8UhKRax6u--HPtYx5mgIowt23vEsqUHLNMVoONOnEgsclEJD68iJO9DSieccwuedm1j__7lHgfZhWNOQunRp5Rmc2YzjtuiD2nydFFlm_4kViKx1SJFdJhmYJTRj9xkQQ--pM_LFcXyDZFYpRH7ELRdPYtQkxQV-98W3HzXoCAB9mqd36qfD741N0sLvjhq4S6sSqZ4mdIZWDDogW8dF3eMoovg_33vmPN3eFjaMn8A-d_bykVEcMv2RXWwDX1h__1EsqGuGiyOER5ma58DgOSnE6Y7MK0aejF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37dbb2f6e4.mp4?token=WUmgICBbXZIFRZaFYWERBGQaBF80IJHuXQxfwedv8FoeYbcRrh8UhKRax6u--HPtYx5mgIowt23vEsqUHLNMVoONOnEgsclEJD68iJO9DSieccwuedm1j__7lHgfZhWNOQunRp5Rmc2YzjtuiD2nydFFlm_4kViKx1SJFdJhmYJTRj9xkQQ--pM_LFcXyDZFYpRH7ELRdPYtQkxQV-98W3HzXoCAB9mqd36qfD741N0sLvjhq4S6sSqZ4mdIZWDDogW8dF3eMoovg_33vmPN3eFjaMn8A-d_bykVEcMv2RXWwDX1h__1EsqGuGiyOER5ma58DgOSnE6Y7MK0aejF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری-فاکس نیوز :
با اینکه ترامپ به اسرائیل گفته پاسخ نده اما اسرائیل همین الان جلسه اضطراری تشکیل داده تا تصمیم بگیره آیا به حملات اخیر پاسخ می‌ده یا نه؛ و اگه پاسخ بده، چطور این کار رو انجام خواهد داد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8887" target="_blank">📅 00:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8886">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
یک منبع نظامی به تسنیم: موشک‌های جمهوری اسلامی آماده‌ان در صورت پاسخ اسرائیل فورا شلیک بشن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/IranProxyV2/8886" target="_blank">📅 00:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8885">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو اگه به جمهوری اسلامی حمله نکنه، باید با نخست‌وزیری خداحافظی کنه!
احتمال واکنش اسرائیل بسیار بالاست...
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8885" target="_blank">📅 00:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رادار کلودفلر اختلال شدیدی رو روی اینترنت ایران نشون میده.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/IranProxyV2/8884" target="_blank">📅 00:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8883">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
سخنگوی ارتش اسرائیل:
جمهوری اسلامی اشتباه بزرگی مرتکب شد. اسرائیل موازنه‌ای رو که تهران در پی ایجاد اونه نخواهد پذیرفت.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8883" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8882">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
کانال 14 اسرائیل: اگه نتانیاهو بخاطر حرف ترامپ به ایران حمله نکنه عملا دولتش تموم شدست چون تمامی سیاست‌مدارای اسرائیلی خواستار حمله به ایرانن
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/IranProxyV2/8882" target="_blank">📅 00:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری
فرودگاه تهران رو دارن خالی میکنن
پشت سر هم هواپیما بلند میشه
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/IranProxyV2/8881" target="_blank">📅 00:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8880">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
ارتش اسرائیل: سیکتیر، ما لبنان رو ول نمیکنیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/IranProxyV2/8880" target="_blank">📅 00:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8879">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
سخنگوی ارتش اسرائیل: رئیس ستاد کل در حال انجام ارزیابی وضعیته و سامانه‌های پدافند هوایی ما در حالت آماده‌باش قرار دارن.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/8879" target="_blank">📅 00:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8878">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
سخنگوی ارتش اسرائیل: جمهوری اسلامی اشتباه بزرگی مرتکب شد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/IranProxyV2/8878" target="_blank">📅 00:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8877">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اگه ترامپ چند دیقه دیگه اعلام کرد با همکاری سپاه به اسرائیل حمله میکنن نباید تعجب کرد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/IranProxyV2/8877" target="_blank">📅 23:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8876">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa612d6574.mp4?token=Ck3NhpSpz8PxEGhLS1pTa1PwguEljEM9j8aHYJG1C0XJ9cbiavK95MEqi6HhJi9DPt5cYbJ56T7BweXCirwzVReNj_ES2Qi3Qfv5QEsTI6n3vxX3kvnXokf1edb6ZOiWZtZMJGhHR1hLX_FQIeSFXycJnI5TKSjH4lDzsxxt0xmKgszDSLqWgf46pd--3tvmmuN9EjIguYKoeojRf_Qv2KYID7yKXacKjKvrAzSNrRXFUcKdN6X1cEe1CMEPTRtukIdLPd1qfb0nJSBefkzPPrvYGAUScqEEInEokw3_FwfdWIqTP5-nM21mjDja1e-F878QuEZ0nQUeIMIhWqKuMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa612d6574.mp4?token=Ck3NhpSpz8PxEGhLS1pTa1PwguEljEM9j8aHYJG1C0XJ9cbiavK95MEqi6HhJi9DPt5cYbJ56T7BweXCirwzVReNj_ES2Qi3Qfv5QEsTI6n3vxX3kvnXokf1edb6ZOiWZtZMJGhHR1hLX_FQIeSFXycJnI5TKSjH4lDzsxxt0xmKgszDSLqWgf46pd--3tvmmuN9EjIguYKoeojRf_Qv2KYID7yKXacKjKvrAzSNrRXFUcKdN6X1cEe1CMEPTRtukIdLPd1qfb0nJSBefkzPPrvYGAUScqEEInEokw3_FwfdWIqTP5-nM21mjDja1e-F878QuEZ0nQUeIMIhWqKuMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه برخورد یکی از موشک‌های جمهوری اسلامی به شمال اسرائیل:
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/IranProxyV2/8876" target="_blank">📅 23:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8875">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری
اسراییل: تهران آخرین شب آرام‌را سپری میکند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/IranProxyV2/8875" target="_blank">📅 23:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8874">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngVgYrKsDuMZRg6iwQH2sER7QzvqHEPyM7HPr5BHiNS8WB7773J7jVMP78iFBy4HknbhFS-Hg8bVLLS-rcDnvsU90dtziTAar7teVbrpt9xr_T6cYwp_YhgbEWN5sg3QUu3o6Ee7awQRNdZUswcWJ3XgMjIxR91DsuTIott03XyNvd27M65dsbJ4_OcJs0q9MsMAbP0QQ6_sJB6i_VlmhWzS7od5nArFQSdpib2vAlmvGolM11lvSRLF0vlXdp1fg8bLSS1GdOcv8n_O38JBBjCywZHbs3Twm7ec_f-6JhXAcM-E5PVGUFM-dbPumGWyu5x-HAGJdXxykeeX3Z4_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری-رئیس حزب اسرائیل بیتنو، نماینده کنست آویگدور لیبرمن: «تحمل کافیست، باید فوراً واکنش نشان داد و به زیرساخت‌های استراتژیک ایران ضربه زد»
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/IranProxyV2/8874" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8873">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فعالیت جنگنده‌های ارتش بر فراز آسمان تهران
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/IranProxyV2/8873" target="_blank">📅 23:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8872">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">صداوسیما: خونه نتانیاهو رو زدیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/8872" target="_blank">📅 23:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8871">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری
حساب منتسب به مجتبی خامنه‌ای : نفس رژیم لرزان صهیونیستی به شماره افتاده است.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/IranProxyV2/8871" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8870">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رویترز به نقل از یک منبع ارشد ایرانی:
تمام پایگاه‌های آمریکایی در منطقه در صورت انجام حملات از سمت اسرائیل، اهداف مشروعی برای جمهوری اسلامی خواهند بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/8870" target="_blank">📅 23:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8869">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری -ترامپ:
به نتانیاهو خواهم گفت به ایران حمله نکند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/8869" target="_blank">📅 23:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8868">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwfSnRvc3Y8SLP2FKAxPv4Snh9ebQzYq0f4hOAeA_YfvpTqG5GNlBsbknS7OiwJp47o-iwzVc2h-dJct0am0Mg2n6u197I0Dhkh7sGOqxtIXqiVa6KVP_UP98TOeocRzZTVD0Adpv9j-owksGLcx6Vr5UD1wPvyhJMrZd35pE_SSwQ6IAjPOiTPBO_VMbyDsUM5mD4gq30iwuCdgk0drwJNJ0XmRANON_kIOOuWlVL6WgqZToH5Ky5P9F8UTA4Sc7gdAA9K4AHft6jNAzSJcgYXrDjDYYV5s7aVH7tHpiegGYPgjMauXmeTGTly6dG0-unTYw-m8f-kApcv7QK_Meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
فوری / عراق نوتام اعلام کرد و حریم هواییش رو بست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/IranProxyV2/8868" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
سازمان هواپیمایی کشوری ایران:
حریم هوایی غرب کشور تا اطلاع ثانوی بسته خواهد بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/IranProxyV2/8867" target="_blank">📅 23:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♨️
🔴
سی‌ان‌ان به نقل از دو منبع اسرائیلی: ما به شلیک موشک‌های بالستیک جمهوری اسلامی با قدرت پاسخ خواهیم داد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/IranProxyV2/8866" target="_blank">📅 23:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8865">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / ترامپ: نیروهای نظامی آمریکا در حالت آماده‌باش هستند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/IranProxyV2/8865" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8864">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
یک منبع جمهوری اسلامی به رویترز:
اگر اسرائیل به حملات موشکی ما پاسخ بده، ما هم قطعا پاسخ خواهیم داد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/8864" target="_blank">📅 23:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8863">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
ترامپ به فاکس نیوز:
نصیحتی که به ایران دارم اینه: شما موشک‌هاتون رو شلیک کردید، این کافیه. به میز مذاکره برگردید و یک توافق انجام بدید.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/IranProxyV2/8863" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8862">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری
حوثی ها منتظر دستور بستن تنگه باب المندب هستیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/IranProxyV2/8862" target="_blank">📅 23:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8861">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
سپاه: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/IranProxyV2/8861" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8860">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNBiXy08kmu5hsfkYciKO8N9KgoSoVOgbKphAfmLgDHK-anFpAWOGSxJB5X4hSzlXj41-mZ8f9axmC_QVZpbxMmLnu9kj4fXxM4Dm9tBt0nbjXZ1YLjViNGe_BnkrJXq4Aga1FpBr7b4OLfuMj43WLMqB4Ond6OgOCtyxKf63RdbYwAMTGSsaMQXJm0132EYz-nriB5K42syyyIFDu5gGZ6bHsI8Iwedm8SopgqSiPxybiim1ix0_3JEXNp0yjNkl_9ufMDUpt5FAKxcK2rClkaOqnDi_6ktulFuPrymCc7ruajHkC-0YY0c1nML9cItvQmNZYrpYuoGYSOSprZOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موسوی، فرمانده نیروی هوایی سپاه:
الوعده وفا
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/8860" target="_blank">📅 23:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8859">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70b88044e.mp4?token=LV6ncq-bfGl_FLQg3zImYDFBi18FlYMODLKJYYg7nABXSygGSL-QcSjRXvkpKCV_n_zxez7vvJbu8T745nhkbB306wljNTAdcxQIaTZg5-IbLhvTEqZ_5NggRx8hfmN3uHk0I1I2avoMLKmOqMIt98LlrMVJFdJzPR7YYkrlklBhy470VSoR5ZaClTLx2rM68EOmLNaOKFIFosoF1kGbbS64flvsMUR4C22m0leq3MTJIp-cnQGfFPkCCP9Fbn6HUKF5cyFgQbQV3G7leN86V7vX-RUHKl6CN4j-KdkUOZ4U36hDQSeSJNRQFXYDy8Uo1vBIVHowDN8JA8eQbjnnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70b88044e.mp4?token=LV6ncq-bfGl_FLQg3zImYDFBi18FlYMODLKJYYg7nABXSygGSL-QcSjRXvkpKCV_n_zxez7vvJbu8T745nhkbB306wljNTAdcxQIaTZg5-IbLhvTEqZ_5NggRx8hfmN3uHk0I1I2avoMLKmOqMIt98LlrMVJFdJzPR7YYkrlklBhy470VSoR5ZaClTLx2rM68EOmLNaOKFIFosoF1kGbbS64flvsMUR4C22m0leq3MTJIp-cnQGfFPkCCP9Fbn6HUKF5cyFgQbQV3G7leN86V7vX-RUHKl6CN4j-KdkUOZ4U36hDQSeSJNRQFXYDy8Uo1vBIVHowDN8JA8eQbjnnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♨️
🔴
مشاهده موشک در آسمان تبریز، دست‌کم ۶ موشک از تبریز و ۳ موشک از ارومیه شلیک شد.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/IranProxyV2/8859" target="_blank">📅 23:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8858">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری-موج حملات موشکی از کرج
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/8858" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8857">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری
حملات جدید به ایران بزرگتر از قبل است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/IranProxyV2/8857" target="_blank">📅 23:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8856">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
نت بلاکس:
🔻
ترافیک اینترنت در ایران ۲۵درصد کاهش یافته و اختلال زیادی داره
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/IranProxyV2/8856" target="_blank">📅 23:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8855">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trdlDe2R7bY8ZP9Le3C8hZaHQuR-idgMMCfxGFGmsQd7O-xMEoBr7qwXuiyaSRJWjwroNkaVEa3z6wI-k-EwJGs29gXb8k-t29myK8pAd1i3rAVttmmo8Mjd5eY8Yi0wSMVRcpFodHfBHjh1v4Y1BqACjf_d3LsJHpPHXNtNqngjm5XV-CLsB_YYU4m0TTR4OjHt6LoTNeyw__wYn5tUBBi_JQ3Phvs8RsM2xejjtIAWlUxWR2wCfSB-axdLnNjwOGdziD0Twwi7eW6GeU3kB5O6WyXJM1Sp-xAhAG5_Ee8oB0q_KqtuiNbjca371G5MzphowJi9MMvZH1Co4SnNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
سوخت رسانها به پرواز درآمدند
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/IranProxyV2/8855" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8854">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
نت‌بلاکس: بسم الله الرحمن الرحیم.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/IranProxyV2/8854" target="_blank">📅 23:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8853">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری
منابع اسراییل: حملات سنگین به ایران نزدیک است
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/IranProxyV2/8853" target="_blank">📅 23:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8852">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری
پمپ‌بنزین های تهران مملو از خودرو شد برای خروج از شهر !!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/IranProxyV2/8852" target="_blank">📅 23:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8851">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
آکسیوس:
ترامپ در جریان تشدید تنش بین اسرائیل و جمهوری اسلامی قرار گرفته.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/IranProxyV2/8851" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8850">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95132def2a.mp4?token=nGLLlMlkNtwsK5t_Y-MiZ_8wOVv61jG4YQ_PgiD1NEnXgoENVFZdz-s4JfZT_3fYwYltQhfN9Q_9wsZpGjdok-rDcriyNDCWMajVgP-TZAVPgRRCWxXT_VXhSnD7t5WIb7_vzoLmSeJVbKIzWksBi5M6cs8App7BTQzi6S4WGOX-b4UmMy--bscky_UItNnFjyBHJ87JcUIfXgb2D8WxysVW4xhKFLeEylN6ruvmmCOOHjgfPH5m4LxRbL9-515rBcpdxIsXzFeZJbIivZoy4LY_pfRynpVC8ZqBqMbfmJdV84DY6q36gOT4TWhuf96JCzzR5Rzh902yMqRvlQ6gKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95132def2a.mp4?token=nGLLlMlkNtwsK5t_Y-MiZ_8wOVv61jG4YQ_PgiD1NEnXgoENVFZdz-s4JfZT_3fYwYltQhfN9Q_9wsZpGjdok-rDcriyNDCWMajVgP-TZAVPgRRCWxXT_VXhSnD7t5WIb7_vzoLmSeJVbKIzWksBi5M6cs8App7BTQzi6S4WGOX-b4UmMy--bscky_UItNnFjyBHJ87JcUIfXgb2D8WxysVW4xhKFLeEylN6ruvmmCOOHjgfPH5m4LxRbL9-515rBcpdxIsXzFeZJbIivZoy4LY_pfRynpVC8ZqBqMbfmJdV84DY6q36gOT4TWhuf96JCzzR5Rzh902yMqRvlQ6gKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ساعت ۲۲:۵۰ یکشنبه؛ مشاهده‌ی نور چشمک‌زن یک هواپیمای مسافربری در آسمان کرج، همزمان با شلیک موشک توسط سپاه و احتمال شروع حملات اسرائیل.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/IranProxyV2/8850" target="_blank">📅 22:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8849">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuMNcbpDeefXzpv7s8r-4ZbdotrhDJ5fxU8aboh1nWbC4ofwFvqxu3fIFxlUUXCWG7bP0oNe9fOsMNtXphiaUiBFHjfw1IxJ4bEMcjIrd0s1DqMB8mdDnyex8DYKWjqzPGNIZo85vYDgzhdf7nbIQuUt6yVJjBls3wZCt5PoyZ8oqjPglQXWCnN8Aacvjl02o3uFcxJ58KraI6CYgwnyuPXI7RBFEHdDzOT46KbdGEI9O782hao5ejqZd8-Qq5jKPgw9D0NFymU0JI96cUUsWYole2txZFzZqe_50IeQlk1yd3JhK0sOVbVPM-FjswtocrqY0GVaeYLWqRVnWLA_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
♨️
آژیرهای هشدار قرمز بی‌وقفه در شمال اسرائیل به صدا دراومد
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/IranProxyV2/8849" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8848">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
#فوری
| ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8848" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8847">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کانال 14 اسرائیل:
به زودی پاسخ بسیار گسترده در ایران خواهد آمد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/IranProxyV2/8847" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8846">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac124d380.mp4?token=FzCiNVvcAn_1U-SUf4Bs3hZPwUdXY7EQkxNCugDff6Be3dTr1mRPFRRM_yc6WXCSu98MrpJI-OJuOP7FFd5uAQbvyZP41DxSgX3XXC2AitMTan4xUVwIWPMGfQSd9pgO0WfKrzthgqJhEdaT6z4EfkkitmyCf5sFKTjidiyYHf-dSjKfooPIUpaJrSsy582px2rKCgtQpUJ2ZPY-GJ-y9knHFArQGdtWklVJNvkJsfwDDcLH5_QwkwjS8vZCBGEbkEFxJ-uJVEUE4bjUCWP8TCj2AX9Mz7Xc___ktrKeQy-37Y-_SAotmfCGa5SNgKs7cS5MpCQ3HjgJNyLS2k2JFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac124d380.mp4?token=FzCiNVvcAn_1U-SUf4Bs3hZPwUdXY7EQkxNCugDff6Be3dTr1mRPFRRM_yc6WXCSu98MrpJI-OJuOP7FFd5uAQbvyZP41DxSgX3XXC2AitMTan4xUVwIWPMGfQSd9pgO0WfKrzthgqJhEdaT6z4EfkkitmyCf5sFKTjidiyYHf-dSjKfooPIUpaJrSsy582px2rKCgtQpUJ2ZPY-GJ-y9knHFArQGdtWklVJNvkJsfwDDcLH5_QwkwjS8vZCBGEbkEFxJ-uJVEUE4bjUCWP8TCj2AX9Mz7Xc___ktrKeQy-37Y-_SAotmfCGa5SNgKs7cS5MpCQ3HjgJNyLS2k2JFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/IranProxyV2/8846" target="_blank">📅 22:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8845">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSMMPyGJKgI1wd-YuN4hip3t5AMEm1GSI_0aVkBcVtqpmkg1b714v3sgRkTPDvgBJ6XbWKKx8KqnMqytfHpTQkZXpbF_iGUYV1SQpFVWb6H6V-Vwe0QRnIcV9p9elZ1T7dJ0e_A7XudGUPFl_TI-c5GRa6i2BkZk9VgQNFavgQa0eTadYttX0x28HIkq2Woy0_2HIav9_nIBdSo69b-qCahQKWOn4HVRED9x1cfV8boXksN1qdjcKrvE-q_M029prtllu4GneaLMcD-RnVtenwlfE5CNuUp5kPFst-sXfmiVe0EWn6fiIv6Xdhh_A8fdhZ33-GkvxDal-CYayIoJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/IranProxyV2/8845" target="_blank">📅 19:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8844">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWBY6cjsFDJlangtH_7Z6U1vAshhyfAgA4xs3sB2dTNu4Di6FSeNONb3XbwfV2TZ60R3TcHtnxDf_-XhJsomr1VLhtcV4e9-JBO6V3ay6Ve3Vw8cuUxq1DUhdjTyPU10bEtb-ZOJ1fmZ93lXFrjW6XDmTuzQmN_HhVuFWPs5iAUI6-ml-9CfGdUCMMGyDGFnysog08VJT30Lfg0IleElc2UfB6B3nXyQaStpzdnTw2lDn3kay2_RvorratZkDTs87ud1HWZAKCxzZMDLYO96XpvUNvNh10om5mihaRvrV9ueQkVbFuqYIWKiM4KN2rZc2cVXEOtTD8mcOXi-upPtHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دوستانی که سرورا براشون متصله نمیشه، ۵ پورت و ۵ لوکیشن جدید اضافه کردیم، لینک سابتونو بردارین، حتما دامنه جدید رو از قسمتی که نوشته
info.russiaproxyy.shop
به این دامنه جدیدی که براتون قرار دادم
⬅️
doc.midnightfits.com
➡️
تغییر بدید و وارد ساب لینکتون بشید سرور جدید رو بردارین
🔹
نمونه ساب لینک جدید
https://doc.midnightfits.com:2096/reza/xxxxxxxxxxxxx
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/IranProxyV2/8844" target="_blank">📅 16:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8843">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جهت آپدیت حدودا تا یکساعت دیگ دسترسی به ساب غیرفعال میباشد ولی هیچ مشکلی در روند اتصالتون به کانفیگ ها نیست، خواهشا تا اطلاع رسانی بعدی ساب لینکتونو بروزرسانی نکنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/IranProxyV2/8843" target="_blank">📅 15:15 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
