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
<img src="https://cdn4.telesco.pe/file/C6txvn9JkJnSBQm7zw2oyDdriv7RnqhI4NJJF7OctIE5w0hLwzjNSnM4-vGp-g2_cn-K5YX2cG-pSb_3H6g6BUx0jjtAM904zGX_V9b2zljUqEnkvbriRP8lPd3-oHja_iGeS_FUX51j1UYSbTLUjV5_lIvIs08DfcAej4btwslyj6QiJv8JYnIZmc-WPAN2quJ78aFwo2dLFof2cM9aLE8A0EPIxnPNAJGHzLAqk9cM5NIJgqO3GJM340h86q1f4jc_L0vzJ9-6Z5WRj3krroZ8wBYOaeB5k7qYZPmfaVva224aGUNbkbNcIFF26ZMVQ5S59wG7NouV33HGZGzxAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 07:59:57</div>
<hr>

<div class="tg-post" id="msg-447819">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7e992159.mp4?token=l76dbfhjUL5cCeNvWWlxVryZzfNY4CZXOghFXt1iOyFQQy9nqp00xrY7HHBHrkpDn47UQ4oPEicRnXcUD6pEqDVigGTO6WCM39HR-9HJOjXv8dvR51tHQrb_GAy5SW7rudpJZyI4GZJgitxpeHypTQAEnL7I9E6WSipDQhwSEV5k7asRrdLpm7AwkjphBrQyYX0LOuM40sTY6POweJdsb_k3g9LyiE7vEIitKGFFIB_thxqn3wN0zsyXUdqigfZc8X_ttk7DndAY9MDhbeaDWHJinFIyzA-jOXce1U0R5BjhmWeaL15F5sGOCgkt9kPGLkecxJ_lG9NMjJLzLD_WBnlerx0gLHIiNa8Usga4w0B4GSvlWuNmGwIHe-mPFCD24d92cYrXhBWNwd5KiC03k0vr9XdnYkWU9u3ldGe1UiHiSpxs52w-zTnqbpCB1kYhaiyG-ZpzlGDCu12CNID5RNjAYG1kiTLKo6kr_6s4TABz4SVcX8B6jOxtLuncwDQTyo883jVSS8q3EBEbAJYJzWAdtVWTfdA2tuRelslwh0uvx8V5cxwO6FmdWySSrRvTM8gPwPXU08G0-03PHm0R6ZIzf0GnPAwuQR-0vrZN0nsxmQr6vhrqduiz7DJlJIF6lQ6rchq0B4OWuP2_VXasfqVxfr7M9f-JkqXT48IzYx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7e992159.mp4?token=l76dbfhjUL5cCeNvWWlxVryZzfNY4CZXOghFXt1iOyFQQy9nqp00xrY7HHBHrkpDn47UQ4oPEicRnXcUD6pEqDVigGTO6WCM39HR-9HJOjXv8dvR51tHQrb_GAy5SW7rudpJZyI4GZJgitxpeHypTQAEnL7I9E6WSipDQhwSEV5k7asRrdLpm7AwkjphBrQyYX0LOuM40sTY6POweJdsb_k3g9LyiE7vEIitKGFFIB_thxqn3wN0zsyXUdqigfZc8X_ttk7DndAY9MDhbeaDWHJinFIyzA-jOXce1U0R5BjhmWeaL15F5sGOCgkt9kPGLkecxJ_lG9NMjJLzLD_WBnlerx0gLHIiNa8Usga4w0B4GSvlWuNmGwIHe-mPFCD24d92cYrXhBWNwd5KiC03k0vr9XdnYkWU9u3ldGe1UiHiSpxs52w-zTnqbpCB1kYhaiyG-ZpzlGDCu12CNID5RNjAYG1kiTLKo6kr_6s4TABz4SVcX8B6jOxtLuncwDQTyo883jVSS8q3EBEbAJYJzWAdtVWTfdA2tuRelslwh0uvx8V5cxwO6FmdWySSrRvTM8gPwPXU08G0-03PHm0R6ZIzf0GnPAwuQR-0vrZN0nsxmQr6vhrqduiz7DJlJIF6lQ6rchq0B4OWuP2_VXasfqVxfr7M9f-JkqXT48IzYx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مردم در مسجد جمکران و وداع با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 27 · <a href="https://t.me/farsna/447819" target="_blank">📅 08:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447818">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🎥
حضور جمعیت بی‌پایان عاشقان رهبر شهید انقلاب در خیابان‌های اطراف مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/447818" target="_blank">📅 07:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447812">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHrlKU6IZBZrPZiQyWmFwqMYha1ZF_ilS7UhtqNFlrm6J6KojX4kKYXbq9YfCPx4XKUkJ0VNKqiZ2TgUS50Ol2rcA4bvf9HN390tKLtEeDUlQEq4FBy4hBHhydeNkHl68eTx4jSV-WMqbdufhgAM4byiteiWwrPxusyF-Y9NZqTwJKRFjI9WUS9aWyesuiIEInxa7mDwfavO5-TtN-v7xLeaCCOEF85nWKHuk0Gnrb21msITlmR9oUM2YMU6ATiBzmmiA7QtbmvZFeszZRnFEGE3j8gi-Cae77wn82RLB04VeGCb53ohTp6wTnHLYWpEincrnGlVihX3U75osE2YTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgfT7CZivwVKHa91bM0x69G2jb_96X-0llXhynvP66apFnSDSyEaJtCCVBPilOK_Sr6Frvh3O2lIUKUqGGOmjfE3hIUArPeByYR2xBA6ECsTIPSsqwIDLZZg4yYy4bJxR4f58Pymbt16BW-dBB_n5pvzGXIOlvm0Z28hDuW4LKxdFMfEEnCsdfK9y61s0tn0vDX8MJ8EF7cqSJ4RbtkYav13gFn6V3f8y103ypDhEY8XesY120WiU89moevZxTq-CewFyO7m5AnEKXWYbQjDKRnZ2k_Kfq_auGLjGYa6DFOyC3gAiiIKmlubOKYKFNuCiPCC6jmGhVcelODWN0JYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7cWfaM48W0sNmSfNpTN4pbZlgsZaCzx1cqtfMXAJnz342mAK2o5RQI-QgOQ5WYG6zWomdD8nV7ZtdUygEMTYzAXrEff-ndB5YDrLW_gav-g55wTKuHSR9O_sJFK_0ZYu_UWrjlKZ11hqB6v6k0h9pDgwQuu25g6RsAhG0TAdgumAH7oYnOGVOazjKSpd68EBPoa27-Qb6gg_JxPU82r2vAozlA37hL8XvFMrnPP5k7zINjj3QyHEXL0FyXPRUxGamgzHUfiV4xwy-HUXNauQbYvw2XyAdrVxOtQo1ydn5i4RC3wltJmVmNqTfoB4s6Z476y98-jzqNeQmgwrt1Ewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZdB8E7D5-gs35Y_rDz1555SninCW7tho8gyxiVdC0kxeqSpfZTLl4E0Cp8hCM4egB9Eo-8P1IJ6_5lOKUxzuyuS_FsZYxhIkw8FSGsZdUj5a8uH3mBgY07DyPDfPPEpmysBaEvNEGScL0uy4ih79D2o_MazCJMy2eyKII9Jls9GRGam8hqYwG4EirJ0X6uGu24NWe_r2LjpOR2HppKL_04sNOGbBARwBT0lBF9gsv2mCrTtl4VK0aKltuYrDz1-m80nzYcMuCrROewk7vVZZMfFdb_kvchOyxCqp5-zIUllNc3FwdIs4ZDEWEPKrY97tvd3MrPabaaEqwkH8zxnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANUigSwW_mkfzvI1xaAwzpQMHDeV2u1PC3IH9jgNBBYK3Jyw7RLELsmZA6zT7bT5UunHqJ8AidF_fjI-SYqQrN4ejIjMP0TjfumJHXN-2yVmuitRiMQHUkjOZEm9xFycoHA0nso9g5xF8dXgv3fV6HkWLJl8Tr9sHqwB_TMSYZNaBRq-T_VdwqCAVJgwOrXrAid3ggH8HtR75eDh6Rylm4cslbpHf3yXA9VjFcFzzoFmofFmDV-_fb-hy-NQUIljoEwlTeEgD16P4sb9X5aj8bIcJTkxlDgcP_iK-PdSXmuMLn-XcWJ5NAmzYT-UHc5k7BAcJvcU5e9AlCUOFBDEWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7eVhWVGEh8kvykGQXrClkkhQizy58MsPM5TZuorm7xGcS0Joa88ylsN19uMD_yYZGBofUDJMQb62xR0r4MIF__RH8ugELiNy7uoACdg0KfZZuq9X0X13lGjGcm772a5TMM9dStooKgNoQL4H8Mt_DV-mmpzlgcqepREPD6bokpejxxHjo1F7q_LzZH-Lm7QFztE4NnslTNXOoEPZdyDN6luDrZn550gsNNEXVe0UuoTHHKZFcFYenVPNAi0YaFVqBQ6bo-mHbwTGfF8dNAEaY_2F4Y75qCtpD7Im7DB9rXXIsC-kR5MjCBUL6th5-2FQD4MtIbJQPSRZES3X7KMdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماز آخرین زیارت
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/farsna/447812" target="_blank">📅 07:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447811">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8-eSqXSBtmq82Fgyxro3nN7l_qoNPv3WWirXmcgeR_zTu8qJ7CyHiVwXzdOwHilSWA9l5lZp1fjoWNI_Px2C0Jw1bb6ot0g9Xn67DZsYKgWghNRtKy_DYzsk46wwNrQ3MmAyZHVMWfUCFc-T9YcPoypAGarh6Vva-HLIsNviynzZurosfOBQZ7BUs15HWCPrFx49rQKLn5Tqcr2ULChEpLaVkQCgxYLTNABF2wxudOOW-la9TYU_Uyl1e8QRKVwTmlOzGvJwnsiXfNsY9tu3RXCFSXP6-F7N9UaUjFQGHTCihxxY4An9dP6x8sMDzoFsrB00_FmCYt-VmE6IXcyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از حضور خیل عظیم مردم عزادار در مسجد جمکران، برای اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان
@Farsna</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/447811" target="_blank">📅 07:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447810">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19f3357f2.mp4?token=j3zABBIuBrMPjIrJlixIrltvSbnpEVmDQmq5wXzpV3tjlUnCKjPzehT30wfI6X3dMCMa01vGOOrQkkbSKfdl_PXYxyUNosDkCkxxbNZ5zEyCbU25Rlk1tStLHwgWy4UWVV454ax_FfGNV3D6YEfDDWM4csXe2r5nadz9-hFDbkbhacuFYOJ8fEUyAUW_zSbilGTh-dmHgdnN4Fx6LPJ7XZk_iMenn6fgmYGPGUW85w_jhR_URtx3hmryU466wTQm6WyRF1iExt6L4wdt-39u8rpZN4dmYaMtGI9iUNf2Jmyneh4ad8sNWlfa1iNMrJMzFA2IrYiWx7tokTskS-Zpnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19f3357f2.mp4?token=j3zABBIuBrMPjIrJlixIrltvSbnpEVmDQmq5wXzpV3tjlUnCKjPzehT30wfI6X3dMCMa01vGOOrQkkbSKfdl_PXYxyUNosDkCkxxbNZ5zEyCbU25Rlk1tStLHwgWy4UWVV454ax_FfGNV3D6YEfDDWM4csXe2r5nadz9-hFDbkbhacuFYOJ8fEUyAUW_zSbilGTh-dmHgdnN4Fx6LPJ7XZk_iMenn6fgmYGPGUW85w_jhR_URtx3hmryU466wTQm6WyRF1iExt6L4wdt-39u8rpZN4dmYaMtGI9iUNf2Jmyneh4ad8sNWlfa1iNMrJMzFA2IrYiWx7tokTskS-Zpnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش بی‌پایان مردم برای وداع با رهبر شهیدشان در قم
@Farsna</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/farsna/447810" target="_blank">📅 07:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447809">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6340788de5.mp4?token=pwWnOuDlmhMSPL1tehyeyQoxV8W3WX-vIoJBLNELhmA0YBiKWS5_LyeExu_-61XodkjuAiOS-eGeRmADmiRWdGpK4AGDT9rhrM_4LkxgdFYZkpHE93Y6AbY6Yh46OGrIjVtPChD_GTZHp-aIyTv6IW4L6qlV4QtE1o7m6VIOKq5zlEG0CaVTLT2xdbjLgUukzNYMzBNgCO8qtreqlIWPLuvtx7N4moKc5OD_3BCX_kDVX4RbUTOPWjX35kKvb_eE_m9SVbTOY7fWWcaefDLPwIm2Yd0SxqL2leo2wZqy5UN5qXHCLMkZk1YloARH3ejkD7UtE74ta7JHo4bZ1VYRfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6340788de5.mp4?token=pwWnOuDlmhMSPL1tehyeyQoxV8W3WX-vIoJBLNELhmA0YBiKWS5_LyeExu_-61XodkjuAiOS-eGeRmADmiRWdGpK4AGDT9rhrM_4LkxgdFYZkpHE93Y6AbY6Yh46OGrIjVtPChD_GTZHp-aIyTv6IW4L6qlV4QtE1o7m6VIOKq5zlEG0CaVTLT2xdbjLgUukzNYMzBNgCO8qtreqlIWPLuvtx7N4moKc5OD_3BCX_kDVX4RbUTOPWjX35kKvb_eE_m9SVbTOY7fWWcaefDLPwIm2Yd0SxqL2leo2wZqy5UN5qXHCLMkZk1YloARH3ejkD7UtE74ta7JHo4bZ1VYRfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم تشییع رهبر شهید انقلاب از بلوار پیامبر اعظم(ص) قم به‌سمت حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/farsna/447809" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SykI8EZPoTn-74wjN5n5VvzuUQzFVSotXdkqAUWc5sDrqz_y459oHXol-geT7N_x1Dw4y0Y_HE9VwlLD01ionoNzc772zA9FKkTxgpt4zwo0du_hJYgL3p-iFwgkHSOhGDztJ8Xg1PqkuqjWiZOnnNpmXB5_7T83EJSqQz389yhw8zEP-QI7masXWEQh8XtVVIcwHaZusxHNtPxWoTqHSm_v-gOhrecYoBkjcRVRbpHH62fJeAEo14RYSSl7Oknqn9WWG4L_Jtrs8LWae7lWRHMTiQ663zioS8x85NxQRTseUxVzEeZvB794cfApsW76vHqwwHnw1bn7JihG1gSU6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qvh-ttZAoxUmkez3Z2SXVDKsgTSXwBOV2FPS97fOir_koKO8Pz45pbsTaOHs9PMQ_bUk70myXJwtvJO4ODbL2EuL9fTtsb3wEnvxfa27chdqkOuXNbAMZbyyal3flt3aM8fda7gKDEvQssCzlslBSylThIVMTahyolqDgBsHBNlA289-WP1U0Y4L_d72izHaJyZWJpM5RqQ7OpPnGyoP-9nPl_K2VKKcgdOdSpFgTQ5Zjl9zhfpx0f5PYxk79_a8c9t8WVnkcWFBv6R__gPeOTKNvCQu3rKi0waEnG9llLDruYl0Z6cEM1xEAyE5xhvFgfJSkdrm5BJxiWHORAxYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HSpNBjLYSPoGYqfjsKSf9pl3sf8sf9nWgKmC-TM8bfHP_jYULDe59ATgt_YdXPPbxtg5qI1nbl8bMBwCmIGU-wK9RHzvUFDGTiywFvmj9RQ6gwgf6Ys3iSzyaZeu1nlUl63FsOtaajJIts2b4OBwWKnzlTvhG0MhI3eScAq1ewHqS5unse4snLssgZfgayU7nRyHqRL2UVyORI-0maL4wynr_Q661EsdhOSnX2cmEEvqIEZxHdoXjGCwW-Z0oDH45sH9gkySZJSllxiqCa3QhvQSuyf55QRYMNLgFEg0NFRhg3Y98tO5h_9p9rIBIcTS1BhderZkB7plBOwwCie8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B7gc2XQ4mm-vbaZs5p9Z1yAa29IFDyPEujak0FSRV3nI0Vve0ImPiIrVNE0zRUH2z7TxWXZgVLgXi9HFOV_cNDgoSUFqfVQ2vl98vZcirRJ9J_3f2gACRuLVAraSBu7HuIGKuHKreA8rWzcU3CGuAevR75igBn827QKBp3TM-h7ymKDnECPTRuBoh1wnsHbjlplrRjJX3nKPdGS8DPQIKEAKhBCZdg0_pC7d5S1qRP-BM3J1PFg4UB5XRz3S2e8-8VUA5cZsNQKJBtkR8SwOkHZQcNSx8-KzNbpT_qLd7koq4Yz8gvCHFu3Y7QdHLoFcfBI6UkO9LzD5oCQWwQwX4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P50nrgkVVGKVPqjPw-bvXnJBid4eaZukePlQPaEcVV5tRuO03ddauz8nfCNzHT1xODH3_RnOq3B64ZdOwbDuIwGfkdWTSId6DdLFnTbZKPp6TL-NanmpbQzP4zmiVztZ_TU1K0zU3VCo9cxPTMzhvi4C8ZRvJoG9mSzc4cjEAd2CflU9VzC3pRDhKW65qDgxei5oCq5TQmOfZXUaCzfPI5wsRlKCM8y_KaQA3e0h0ShFVLlwLQ6XJ95ngQCf9BOTehvVa6EK_ckURXMpkVRLAi9VvjskiZo7HcXi907QzYnJA1nwMbsv2JwokwHYdswWYN3T6WmDJnvSxzHTTPggVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BiT8f4Q0Ewk1ihCFB0nAunWGkpBGJvnDY1wot0ypqgArS_MXbm68_ixtGPtPZPweLVBmwlK7trD1-Bz6MiSdwDI35Pw0LILkFNMxhojPGMvP72o0kPzJXUwPMUS6M2SyoOH75bDOvqOI1HrAA4xVd3_ytgHVIS8yB3IiZ1asf5kXyMa8GUb1LvCGU7D4saxP7vsPIXhoTVjiLZSAo0Ad3DkYGcOH-eR2bK7Xghcv5V092zGHEhpBe_btkUUik9QXxknBovVibJdSN3npZCk7hOGEM1I3-iGHoa1LkGWmj4alOKMuND-nVX8Ed415LU4CVwOcukXTTsOpJ0aKeEmTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtFxuQVaiZpuey_gwEo0A5M0ap7DgCiWVwJdXWEapJERttkHJKRoMjsyPxusk2KmeX0J0XNwiUwKqEXSQJaXICsl9WbjwyujdZNc1b-4kH8-22dxXaUZR4UVnjTNkVWNPZwqNWv94o1JlLmZNxNlds2R0lvIwS8xOTiUgbGjGdUDQXeUhZgjonwYr5IP3ATWdN68lNmdafzGUJJK3TAIjCsa-pw2hM6E7AIYzpsIWGsLaK3gXXef9M6RRpiJzpgrZluradDlwjrMvmOZxG7FdiAvskXkU9XrW00lFFfg8_M_5j6SuaFy8GaXBoz18vFafQo8YNqebyDui8VAT_ewaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/focqv9SIWwUYDjaQgAnCiWXRdiZNKvUvtw0A6jO7Tl6DrCnRaWlXlDQ29G2PI9QFkQY7dY67dS0tKPAK2N7i-uODnq3CVFinnSEV_-TYjL2S6S8gEvDcxjZshOJZrp0JjiJJliMxHTuJJLIewaerRwYdf_sx0fsChrEMrHhHFptK9ZCidV1bA5YAjgW0WIvBI3hsldSsFdtiQJJDWkTWVKnQn-fitTCYxIPIXIwMxaa5YgvOwfX1xLVRkhNtuTpwjy5pVUjPyzp8NuPIa1w4rFm5MEvsLLPvluLe_KpdcpYtrdU1jwIvv2WHEX5hbrpE90hx1eyXEKJv3VSGFYkBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFgl1-H3AN4htTW2xCQ-Orwc7vrOlLgcMx2Hdg6zDKhwl8i35hAE9MDW_Xl37NejV37hXNQrjpFP8BvAd9i4BarHqDiHC0i81IXah3GkeSobwrLtgf_SnOlHpu3nVbPFEfq0HeOQF3Yfw-ac5zqARNASPsMaXeyJdySAuTTnAVwi9hiTOCwr3RieiMDRwOH8cKZr9ihVv4FETOW0dbuH8hU-mTKwxKdYoHXVppT5Ygs8NPjLNDLaTRxQp3pZGLyDmyDLOS4YQj88_GiMsUmTqv_Nw5y-VHYJoSeQWX13fENogqY61dRpV9Poi3bgbp_fXFGFrM3Zs4H0bRl5EXnGAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCn73dKVqD5RoT41VxorqvnGe5QxacvrSSQJcBOue7HXoj0zdR3sa1LsH88xomTU5h6iAGJ5xdqkrw52_zucv3uWzahRDHUfOL6KMNnDlWZG4wguwKd2VRAxqJ-rOkUv3fa28QdKo8nke-WnvyWxrGPzT2GQL7MKt-jG-zXReBf0jT5930XcewWr9N6swOaVNNCkGdf3i7Feh5KhBk16J3dOzUye_JQhmF0B-zFbP7tZBJ642FD0F42jE3jqcXO4ldNAuFjclE7U6spY9NLBdPL9emO_aXURkjjUXh-0fAw1Et6r_GSadswzwBd6NRReTBrNHdRy4F2hjqZbUXrmXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خیل جمعیت عزادار امام شهید در بزرگراه پیامبر اعظم(ص) قم
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/farsna/447799" target="_blank">📅 06:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983268db8b.mp4?token=JYf9YQuz4BPck8issbdP8NZaIYfcvocLzfMKEMOq0hE-3EkG6_JA-CvvtuYuh6UUaqWutc-0rBIiLIY_8cAxegaL5P1iO0ERaB8WZ_Nm2fpli51M7iH-8feKLCOobFcsrMh6NikmppV4c7NJx06NELQT5fE-YCu9ldO6d6tF1ovJWOVCdaw3YFGrULXpnZj7XgA_uqOVcqln52cdhrF-YL3qq3lsqDH46BXWEkhK-QyYCNmdJ9LHRj0IqB6lmv0IzlOTZahzphLkCxokH9Iv456mecdhrl8rmqhYAS0xYHSdo5Kd5rbh00MB2mUu9nYznMmt5f9zG1X_d67-KR3QGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983268db8b.mp4?token=JYf9YQuz4BPck8issbdP8NZaIYfcvocLzfMKEMOq0hE-3EkG6_JA-CvvtuYuh6UUaqWutc-0rBIiLIY_8cAxegaL5P1iO0ERaB8WZ_Nm2fpli51M7iH-8feKLCOobFcsrMh6NikmppV4c7NJx06NELQT5fE-YCu9ldO6d6tF1ovJWOVCdaw3YFGrULXpnZj7XgA_uqOVcqln52cdhrF-YL3qq3lsqDH46BXWEkhK-QyYCNmdJ9LHRj0IqB6lmv0IzlOTZahzphLkCxokH9Iv456mecdhrl8rmqhYAS0xYHSdo5Kd5rbh00MB2mUu9nYznMmt5f9zG1X_d67-KR3QGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از شکوه و عظمت حضور مردم در تشییع پیکر رهبر شهید انقلاب در قم  @Farsna</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/farsna/447798" target="_blank">📅 06:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cef9405f6.mp4?token=LHQjg2tgAWzLAzyZdBj9iqaJlxzvHURDRThGC1K44TgZvypzV8k4fQTV5fxORkIXoQYpIczfivm6sK5eDAZVVsvw-t2NjbdFutXWEM9IFbBzR5E7Dd72eH7iID6ald8wWxI_9IyzugtYFiPouIOdH0NIv8n-ovkwS2Oha9YZaiNTttiy8jYkzvfcZ0lnYDVDkdCxTJ6Yyr619yAmrGjJYN6BQT0JUBNMgf8ehF8PpBaf15n36RXfIV-uoLdqvKi3Nf8mqzjh8zth_QLpGowalMyatV-GKIo5fkOgC5bv4woQ4vJfKLiWnGloKOjPJucDZE8onWUaX-Wn1J3H40lMVSYD8kE8ehkRkccc4-4MDzxqVAif80KOkOcLAlCzieLldrosBbZRVZ1g6883XkrrmOkiWC6N80RB9vfa9uZ4vmW-erKyU4X0NJBLp21NA2_ZtSImLcgR12yMcFcYeu9njutvjJ0VZDRK89QaboI8C6guKIpjmfEPXxmX9QpsFxJVUjaB3cFRHJU5WPZixz37Go7uFoiXdrQ4VdETrKbNZliP4GunHEbed9UaR9HzuTkA0Bgr0k3BzfFjeQ-eKsTQqp7t8RMuFomQJmljtB7fkGoz4_esUXOknP5ZEjfFqzjkc-TyWCis2oCMMRAeUt_L4Q5MkfohAOl80f64iOVUKp4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cef9405f6.mp4?token=LHQjg2tgAWzLAzyZdBj9iqaJlxzvHURDRThGC1K44TgZvypzV8k4fQTV5fxORkIXoQYpIczfivm6sK5eDAZVVsvw-t2NjbdFutXWEM9IFbBzR5E7Dd72eH7iID6ald8wWxI_9IyzugtYFiPouIOdH0NIv8n-ovkwS2Oha9YZaiNTttiy8jYkzvfcZ0lnYDVDkdCxTJ6Yyr619yAmrGjJYN6BQT0JUBNMgf8ehF8PpBaf15n36RXfIV-uoLdqvKi3Nf8mqzjh8zth_QLpGowalMyatV-GKIo5fkOgC5bv4woQ4vJfKLiWnGloKOjPJucDZE8onWUaX-Wn1J3H40lMVSYD8kE8ehkRkccc4-4MDzxqVAif80KOkOcLAlCzieLldrosBbZRVZ1g6883XkrrmOkiWC6N80RB9vfa9uZ4vmW-erKyU4X0NJBLp21NA2_ZtSImLcgR12yMcFcYeu9njutvjJ0VZDRK89QaboI8C6guKIpjmfEPXxmX9QpsFxJVUjaB3cFRHJU5WPZixz37Go7uFoiXdrQ4VdETrKbNZliP4GunHEbed9UaR9HzuTkA0Bgr0k3BzfFjeQ-eKsTQqp7t8RMuFomQJmljtB7fkGoz4_esUXOknP5ZEjfFqzjkc-TyWCis2oCMMRAeUt_L4Q5MkfohAOl80f64iOVUKp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از شکوه و عظمت حضور مردم در تشییع پیکر رهبر شهید انقلاب در قم
@Farsna</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/447797" target="_blank">📅 06:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59d9c0fdb.mp4?token=uEHLOKBj8SOYKYfZ_BPWaxIEMiuW2fANLL6hqvChKKaEKRf9BBiU33rUa4qX5KfnUyav3gfpY9uGBi6NPutgPpV-HJZsi2KHPi6Pxo2R9jaeOwbNlAOreqw0jSj8Hqkc2blb1ndYqMHuW10NtsBKnGNMjNPj41HTYnm7gwtKHVFEX8C127jn6-lln1CTOZZQQDpL_W3eoUjX79SOpaB6PFpTyZPbhqOWo24x3DXrXAZq3AIxwdGPr6mibrsSqBOeEAHsW2kRMJlzRiFMDOxFviG7bXwi_UAUzA65ieg3nq3V4teBaet0xHWpN_1SMlVjlzVervMmi3MfbCwaTnhFMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59d9c0fdb.mp4?token=uEHLOKBj8SOYKYfZ_BPWaxIEMiuW2fANLL6hqvChKKaEKRf9BBiU33rUa4qX5KfnUyav3gfpY9uGBi6NPutgPpV-HJZsi2KHPi6Pxo2R9jaeOwbNlAOreqw0jSj8Hqkc2blb1ndYqMHuW10NtsBKnGNMjNPj41HTYnm7gwtKHVFEX8C127jn6-lln1CTOZZQQDpL_W3eoUjX79SOpaB6PFpTyZPbhqOWo24x3DXrXAZq3AIxwdGPr6mibrsSqBOeEAHsW2kRMJlzRiFMDOxFviG7bXwi_UAUzA65ieg3nq3V4teBaet0xHWpN_1SMlVjlzVervMmi3MfbCwaTnhFMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیکر مطهر رهبر شهید انقلاب اسلامی در جایگاه وداع با مردم در مسجد مقدس جمکران قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/farsna/447796" target="_blank">📅 06:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447794">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43be92ab9.mp4?token=Eb5uxTWCeWO4J29hEBEUTup06weFaO5x4Fqm9FwmVuEVxv-wyuvfpX9FRg2a3Hm0Ni0eWdaHrgY8MSxs03gkLTlmkmpjZF4D1XBBedE9Iqo_o6xkZS2klGr8R3uPuxvO2JEAiWGgULSwKF3DoMvs87EK-nwIflTNMJ_cKNGsJS0qt7_VNvdw1sAAVMXC6iNOPrtwVDIfxXpiNolJaYB7wcvGBy9syqNmgKy5-3xOyP9Idq88m12MEvqNQE1VZhLEIssLphzJJvHTpMssG91m1tWZntaE2ZPwu5LZTTiWSxmlc-kcwrcWqjFPIqELsvZ1xUYy5L1jM8IVoX5BJWTBYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43be92ab9.mp4?token=Eb5uxTWCeWO4J29hEBEUTup06weFaO5x4Fqm9FwmVuEVxv-wyuvfpX9FRg2a3Hm0Ni0eWdaHrgY8MSxs03gkLTlmkmpjZF4D1XBBedE9Iqo_o6xkZS2klGr8R3uPuxvO2JEAiWGgULSwKF3DoMvs87EK-nwIflTNMJ_cKNGsJS0qt7_VNvdw1sAAVMXC6iNOPrtwVDIfxXpiNolJaYB7wcvGBy9syqNmgKy5-3xOyP9Idq88m12MEvqNQE1VZhLEIssLphzJJvHTpMssG91m1tWZntaE2ZPwu5LZTTiWSxmlc-kcwrcWqjFPIqELsvZ1xUYy5L1jM8IVoX5BJWTBYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بانگ الله‌اکبر زنان شهیدپرور در بدرقۀ آقای شهید ایران در جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/447794" target="_blank">📅 06:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447793">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b585c6d4ad.mp4?token=b3BLAKFjxulIzSgGmIrPk-GH238kBH7itdCVeLjnBqAPYNTBYV47dxKFEUZGVzRKNbNc1d1C3z_mnoXaV7lr6tIJMyha-EusTLHDEiKbDwaxZJ9JCYxo1UWwUwSFgs5PyhcPtJEjH_HdcyOMMt00pcx4IAU4CBvOzoOuwma2Q48yMUOGLH0WxbiJLOGroa5gYlTdpB3p4Qgc4SJKAtMHTi1Mc4N7w952RrxVSf8fLZ8cpnlmutWCsLYpYkoJlJCI5JQIjtNbdxPOF0aM4ITc4zO3dxRBDflRw8KtlTThUfpLy-iAxH5c1hfpXXCV-SxRR5c0Ze3jjAsGJZHd7jzzuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b585c6d4ad.mp4?token=b3BLAKFjxulIzSgGmIrPk-GH238kBH7itdCVeLjnBqAPYNTBYV47dxKFEUZGVzRKNbNc1d1C3z_mnoXaV7lr6tIJMyha-EusTLHDEiKbDwaxZJ9JCYxo1UWwUwSFgs5PyhcPtJEjH_HdcyOMMt00pcx4IAU4CBvOzoOuwma2Q48yMUOGLH0WxbiJLOGroa5gYlTdpB3p4Qgc4SJKAtMHTi1Mc4N7w952RrxVSf8fLZ8cpnlmutWCsLYpYkoJlJCI5JQIjtNbdxPOF0aM4ITc4zO3dxRBDflRw8KtlTThUfpLy-iAxH5c1hfpXXCV-SxRR5c0Ze3jjAsGJZHd7jzzuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشییع پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان بر روی دستان مردم عزادار در مسجد مقدس جمکران
@Farana</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/farsna/447793" target="_blank">📅 06:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447792">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb7089e92.mp4?token=jrHSdKq0-NyiD54fLggdvRA9M80MSo-Oe_ulc_k-JyjXT4fIjRLGxA-kkLqUrSzIMYzjKogVM8cHydloqMIsKo8t-LsIm9TE_Ctb3zgEc5QupK4jYMpQ0dV7g-IUuFIZ7MsapEbwnvBnihKylJLrskFKmh_zQ6RmvmQiRmUDNZtylKHb7ptn18mOZOJ06_oZ9QJjjoJvEUaCL4GxGSO4xwUtMMlD_57EHWk23n46KbxhAkI2bvuKsuJzBKS5yGa5Egvs6EXIoMwxCxtjNWvKUgWqdrPwgZMHsMP_FZd4mdGu7ySn1Ilp9evWEhzl_2fY7--lkYk_QyhJroeZEpF_GR-IwAD-0sZXp3zWNtauKmXMZFSr3JsfBynunnpy7cHg1VymxRjqQkR8DsBeYD3phSmMb0eAthU4dnYsZEdRFxXouJkQlHf71oDqlDJfq5vtfrNEJf78aSS1lahir1WObKWiETnZPbar8FIDuTzU_BPNIM8juDKe7M0W-1Xgza_YFtAaeMm3VjrtNx2a9sR36RuahBquSoVCZE74_6Ne7fKMznoEwNzkLrAVc4oVXceSPEIi12AkFAgnTrmhJquvd92xE6NgH-XPccZHPU0XsEZCCWAVCq8JImsZaG18lZROw-MKQKTZ5dxukwIAZYtQgGgvdWBL9_sqBWzJUATwxU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb7089e92.mp4?token=jrHSdKq0-NyiD54fLggdvRA9M80MSo-Oe_ulc_k-JyjXT4fIjRLGxA-kkLqUrSzIMYzjKogVM8cHydloqMIsKo8t-LsIm9TE_Ctb3zgEc5QupK4jYMpQ0dV7g-IUuFIZ7MsapEbwnvBnihKylJLrskFKmh_zQ6RmvmQiRmUDNZtylKHb7ptn18mOZOJ06_oZ9QJjjoJvEUaCL4GxGSO4xwUtMMlD_57EHWk23n46KbxhAkI2bvuKsuJzBKS5yGa5Egvs6EXIoMwxCxtjNWvKUgWqdrPwgZMHsMP_FZd4mdGu7ySn1Ilp9evWEhzl_2fY7--lkYk_QyhJroeZEpF_GR-IwAD-0sZXp3zWNtauKmXMZFSr3JsfBynunnpy7cHg1VymxRjqQkR8DsBeYD3phSmMb0eAthU4dnYsZEdRFxXouJkQlHf71oDqlDJfq5vtfrNEJf78aSS1lahir1WObKWiETnZPbar8FIDuTzU_BPNIM8juDKe7M0W-1Xgza_YFtAaeMm3VjrtNx2a9sR36RuahBquSoVCZE74_6Ne7fKMznoEwNzkLrAVc4oVXceSPEIi12AkFAgnTrmhJquvd92xE6NgH-XPccZHPU0XsEZCCWAVCq8JImsZaG18lZROw-MKQKTZ5dxukwIAZYtQgGgvdWBL9_sqBWzJUATwxU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغض آیت‌الله جوادی آملی هنگام اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/447792" target="_blank">📅 06:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447791">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8c37f805.mp4?token=BSdKKoqptb9cj8kuBplZwouAUeOalPs77lEbH_XeobYAIWLuKiGE8RalpxK-NcoNJkLcBvWFJvMJIvoaoag_mosOcd6coq4KG8T_yO0NfpYTNoRW0SSbPoFSp4Lnts0Dy-FXES__gA2uL7S_znLCXIqiVJeiTuNV6aZlipdJOZw1vZVUl0LhBzedAc0NqxUHI3zZSldwLAKZvL8xLT5Y0BdAmDnWw3kaMdMPdNgCCiHWxxa5s7Pz--z6cK2N_4ehn0DyUhso_O0CRxSQQjPEObOLO7tGB-sJKTXzigL3zE2jR-GWTXWkE37Q2iHZTQz3LWWkVjad7KKEehLWsQwjyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8c37f805.mp4?token=BSdKKoqptb9cj8kuBplZwouAUeOalPs77lEbH_XeobYAIWLuKiGE8RalpxK-NcoNJkLcBvWFJvMJIvoaoag_mosOcd6coq4KG8T_yO0NfpYTNoRW0SSbPoFSp4Lnts0Dy-FXES__gA2uL7S_znLCXIqiVJeiTuNV6aZlipdJOZw1vZVUl0LhBzedAc0NqxUHI3zZSldwLAKZvL8xLT5Y0BdAmDnWw3kaMdMPdNgCCiHWxxa5s7Pz--z6cK2N_4ehn0DyUhso_O0CRxSQQjPEObOLO7tGB-sJKTXzigL3zE2jR-GWTXWkE37Q2iHZTQz3LWWkVjad7KKEehLWsQwjyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
طنین انداز شدن صدای آقای شهید ایران در مسجد جمکران و گریه‌های بی امان مردم عزادار
@rahbari_plus</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/447791" target="_blank">📅 06:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447790">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5340ada419.mp4?token=EDEs52QUfK6Alpd-dygLRYJvmyJnoKKhFdi_HCZqvasm3sFJUyvs6K_qW_7P7IXrK4SPY_b59LwDE39KmoOHpQ2igwdiCDYl57iPe81T4LjpydfkMSy9VRwhEITIbYbElroAPA2NJNdjWmUMI2Ylim8mhnDesh8r_lhmffoKDdqu1vGwQRQ2rB_XxNoMsyvPOamYifatx9admboiOim38uCf-x4rh4GReun-VxIlt285mH7PFYV6p1j9X7XBcHAVSrlq5L1rRLUrFy_QPgxGWuNNTvvJt-ibZCWAenQZhRL7bZ5KCJGlnfpuW7uMWAcjBRb5tJgrhhbFjLpPu9b_Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5340ada419.mp4?token=EDEs52QUfK6Alpd-dygLRYJvmyJnoKKhFdi_HCZqvasm3sFJUyvs6K_qW_7P7IXrK4SPY_b59LwDE39KmoOHpQ2igwdiCDYl57iPe81T4LjpydfkMSy9VRwhEITIbYbElroAPA2NJNdjWmUMI2Ylim8mhnDesh8r_lhmffoKDdqu1vGwQRQ2rB_XxNoMsyvPOamYifatx9admboiOim38uCf-x4rh4GReun-VxIlt285mH7PFYV6p1j9X7XBcHAVSrlq5L1rRLUrFy_QPgxGWuNNTvvJt-ibZCWAenQZhRL7bZ5KCJGlnfpuW7uMWAcjBRb5tJgrhhbFjLpPu9b_Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز اقامه نماز بر پیکرهای مطهر شهدای خانوادۀ رهبر شهید انقلاب در مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/447790" target="_blank">📅 06:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447789">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎥
آغاز اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان توسط آیت‌الله جوادی آملی در مسجد مقدس جمکران  @Farsna</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/447789" target="_blank">📅 06:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447788">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d90e12057.mp4?token=FAdIOYo2ckZDY8DR8pDlwp-if1YWxiKl2mSaUPN8Nk1Sh9m8kA8hEZO9Yfp3Z_SyVRrOexbNG15aqscZB3kIXatB2W2tQDLZ-GcVHIjPOFf85guM6q2RqeroikBJMTxf6z_Ov0eK7bO6t9_sV51Rr9UsyECloJL2IzoI1AbqcpRUH_LB1G2yMZ7Y6bNzzSYQxwRSRle94er217d8-rWAXI4OG_S_xx9HklQLySwR95h4zwXKnXZMemMmxF6EV-7mnlJZd-S8HyMYtNzUAnyMY8de1XPp64b5_ufU6JMHi7aQYnapprwTLyliFbszhzOWNNFr540SUP4dnHdQjwDBZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d90e12057.mp4?token=FAdIOYo2ckZDY8DR8pDlwp-if1YWxiKl2mSaUPN8Nk1Sh9m8kA8hEZO9Yfp3Z_SyVRrOexbNG15aqscZB3kIXatB2W2tQDLZ-GcVHIjPOFf85guM6q2RqeroikBJMTxf6z_Ov0eK7bO6t9_sV51Rr9UsyECloJL2IzoI1AbqcpRUH_LB1G2yMZ7Y6bNzzSYQxwRSRle94er217d8-rWAXI4OG_S_xx9HklQLySwR95h4zwXKnXZMemMmxF6EV-7mnlJZd-S8HyMYtNzUAnyMY8de1XPp64b5_ufU6JMHi7aQYnapprwTLyliFbszhzOWNNFr540SUP4dnHdQjwDBZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان توسط آیت‌الله جوادی آملی در مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/447788" target="_blank">📅 06:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447787">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23086ebf39.mp4?token=kOfqVkO8IcCHrKhCaY3ktSodBBhJCvf9t8Gsa-IHcvxy3lmt0F0rn5Z0bS5q7RIJa3BFFwL74j_UL0cetOWNn04S8AfafawHYdeFL8uATUxKN4HWyDmvfRP7gJsChbSQiqX-eGswabQI4Q9C8KDOmwvJJNg-L1ZMlB2fkp4efYRdtC-_vqhgIToiOV5Gp9ZltvZTpM1ZQSAoUvY2bBOIjbO4rnt9yHEgTBb_IiB1P9yyHix0MuLMDBFxFvJBG1LXUzFZaBkRmW3soo-tfEtkK7r4i2QTARSlnhy4AWYi1jz6wgDlnKyOas5vl8at5yQVfO3Dl9ahk1mAClplkdYmzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23086ebf39.mp4?token=kOfqVkO8IcCHrKhCaY3ktSodBBhJCvf9t8Gsa-IHcvxy3lmt0F0rn5Z0bS5q7RIJa3BFFwL74j_UL0cetOWNn04S8AfafawHYdeFL8uATUxKN4HWyDmvfRP7gJsChbSQiqX-eGswabQI4Q9C8KDOmwvJJNg-L1ZMlB2fkp4efYRdtC-_vqhgIToiOV5Gp9ZltvZTpM1ZQSAoUvY2bBOIjbO4rnt9yHEgTBb_IiB1P9yyHix0MuLMDBFxFvJBG1LXUzFZaBkRmW3soo-tfEtkK7r4i2QTARSlnhy4AWYi1jz6wgDlnKyOas5vl8at5yQVfO3Dl9ahk1mAClplkdYmzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتقال پیکر مطهر رهبر شهید انقلاب و شهدای خانوادۀ ایشان به جایگاه اقامۀ نماز در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/farsna/447787" target="_blank">📅 06:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447786">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7de8818c62.mp4?token=RFInRdd7rkt-P0uPPnwDUTjHzEpqKjc2fQ2EE6-7rICVKl9BQ2ZymdghQad2JmYBS1jevbAm7VYks8Pb4KckSAUT6AKSGWBA7wM_qoFa797LQSmol2UL10U9w_N8F3Yca006EX6bb6tN1AjZCq-h_ILWijAbwPxMt9eRlmAUf593y5PPYKYelI6BZ33W9F_v_qncY0m1rzTNZgL5OZknzrvWXFI4ts09KCRZn8meCPL7WRxNEd2Rf8ZmA1xhz3ykmaIQHsmCGInWWCviDplYIRocK_xtCOhE2nykfOabLN85mPU8xVuz9oUNlQwlIFAIzBsg-cYtw6hOwqfUFTDRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7de8818c62.mp4?token=RFInRdd7rkt-P0uPPnwDUTjHzEpqKjc2fQ2EE6-7rICVKl9BQ2ZymdghQad2JmYBS1jevbAm7VYks8Pb4KckSAUT6AKSGWBA7wM_qoFa797LQSmol2UL10U9w_N8F3Yca006EX6bb6tN1AjZCq-h_ILWijAbwPxMt9eRlmAUf593y5PPYKYelI6BZ33W9F_v_qncY0m1rzTNZgL5OZknzrvWXFI4ts09KCRZn8meCPL7WRxNEd2Rf8ZmA1xhz3ykmaIQHsmCGInWWCviDplYIRocK_xtCOhE2nykfOabLN85mPU8xVuz9oUNlQwlIFAIzBsg-cYtw6hOwqfUFTDRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت فاتحه توسط آیت‌الله جوادی آملی بر پیکر امام شهید و خانوادۀ شهیدشان
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/447786" target="_blank">📅 05:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447785">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87d0189ed.mp4?token=B6fBPysre92nrnE-Hs6VHIPD5rSwLuuViwFl3yo31O45Dgc2P4QOyM5ixKMWwttL-76ir0vcSeUrsKXP-H5Y04v1FrGecdDWZFD8-lKmVFXfSF2lgNyEzoCPAxZQ5GLQse00TxvpHlBlC_FBnvTyiVIODPuJgxhYlgbda6WTzecEDTxPwpM6TcSanFH9zJm8ejwTD8VZQye7e1H1-y1RoBX25IKKomEM8KwxcLtr6uNPJ5eViRbpn1-r7YPyrI0rr8vKjEr5ErF0tfAjHRNiTso8cilJs-35MGg_r8VbgA4ZnX_ohDiXWvu7qzq83h_xgGeyMlc5DiTPC2f2cDSYfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87d0189ed.mp4?token=B6fBPysre92nrnE-Hs6VHIPD5rSwLuuViwFl3yo31O45Dgc2P4QOyM5ixKMWwttL-76ir0vcSeUrsKXP-H5Y04v1FrGecdDWZFD8-lKmVFXfSF2lgNyEzoCPAxZQ5GLQse00TxvpHlBlC_FBnvTyiVIODPuJgxhYlgbda6WTzecEDTxPwpM6TcSanFH9zJm8ejwTD8VZQye7e1H1-y1RoBX25IKKomEM8KwxcLtr6uNPJ5eViRbpn1-r7YPyrI0rr8vKjEr5ErF0tfAjHRNiTso8cilJs-35MGg_r8VbgA4ZnX_ohDiXWvu7qzq83h_xgGeyMlc5DiTPC2f2cDSYfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع حجت‌الاسلام محمدی گلپایگانی داماد رهبر شهید انقلاب و پدر زهرای ۱۴ ماهه، با دخترش در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/447785" target="_blank">📅 05:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8907b298ac.mp4?token=VekDSk6j1GvkPc2V_JvgffTy1dV5TXWvT_whVVJ4aCd2-SqlT56260LcaCoY_sW0yE0k3mn7QwpUvCq3_aSI4uchWky6OKoY9MmMcHJ0bmgWO7HdOOWOaSadEE1-SFQkB_-2u6iZL8Kl_pVJnpmLhRDvab3vYWI9yik0ui3JcLrXCDp3rUBwrBb__-SLKb6TEQlUm4xUyLXeA-YO5h2XGLDe8Tt-lV3BinhUkvS911jMkxUjdfGFhBjkSjjeypgU0u1nTIiu-5YXMVK74UgbULCyTOLRevsTbQK_iuzJOcM84D0822Qd8oqvC6zol6JfW0iozsNBaxYfeHF4i-9mhjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8907b298ac.mp4?token=VekDSk6j1GvkPc2V_JvgffTy1dV5TXWvT_whVVJ4aCd2-SqlT56260LcaCoY_sW0yE0k3mn7QwpUvCq3_aSI4uchWky6OKoY9MmMcHJ0bmgWO7HdOOWOaSadEE1-SFQkB_-2u6iZL8Kl_pVJnpmLhRDvab3vYWI9yik0ui3JcLrXCDp3rUBwrBb__-SLKb6TEQlUm4xUyLXeA-YO5h2XGLDe8Tt-lV3BinhUkvS911jMkxUjdfGFhBjkSjjeypgU0u1nTIiu-5YXMVK74UgbULCyTOLRevsTbQK_iuzJOcM84D0822Qd8oqvC6zol6JfW0iozsNBaxYfeHF4i-9mhjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر آقای شهید ایران به مسجد مقدس جمکران @Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/447784" target="_blank">📅 05:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHRG9TFm_Q_VyVQqAehqhMFSd9ugMSv28MhGxLSncgvutpWTGL4plsZL9qZvY7_kpLGPgDP60rd-wBENxcIAvTwFQ_Y53jC397TJeSQpFbkSsD_tLwSGNzkTNL8_vhBxUVsNlghVPV5cuKTrogXlfNZ05iHWjRzlc9hw--OLho613Xuk_8mp8tNqd8mhhydxqb5v1bveYo__N8w-F26OhmGsVtxv_wwUfE6AEeEjusi-Nm_Br3Vzf1146IRGve4ptxAtDYJ_Aa32IC4auEjs1njnlbHt4LJlcuCy50uRa6klowKqQ3obdBzwdnjZzp4Q_rKSbuksaIVxRKQefSMsPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخالت ترامپ هم مانع شکست آمریکا نشد
حالا جام‌جهانی بدون میزبانان پیش می‌رود؛ بلژیک با تحقیر آمریکا به دور بعد رفت
⚽️
بلژیک ۴ - ۱ آمریکا
@Sportfars</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/447783" target="_blank">📅 05:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c706552831.mp4?token=kv-uvC5_xD1aFI_nyfbq6hZqxx04LaASTbzD-si-l8tyEfCUh5HMOnyKF1alKDzr2gj9edP1RZaXMzxAzl0AgG_m77dn1Osfm-NxMSCVQDJa_ADHrTCzwYTRLS4uHj3Wt8FEMs2_61Y7Ea0IQCmA8DGv7KiKDB0X6SazcJEffFlKDp8DCsz33wgR-OZrVmwqaymb5NAE2K24ph8WTjYZMzJoM6_4L4LZXBBR9T67vllNjQ6Xi18xnv-M5fmH33eZD38CgYyXH5UH-BZbGGy3Gep3Li7jfuoUiYoGqYJ_JmGyDe1O4JTKOK8XbqkJARMN6dQ4vWnY6WJ9YbgMqJjUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c706552831.mp4?token=kv-uvC5_xD1aFI_nyfbq6hZqxx04LaASTbzD-si-l8tyEfCUh5HMOnyKF1alKDzr2gj9edP1RZaXMzxAzl0AgG_m77dn1Osfm-NxMSCVQDJa_ADHrTCzwYTRLS4uHj3Wt8FEMs2_61Y7Ea0IQCmA8DGv7KiKDB0X6SazcJEffFlKDp8DCsz33wgR-OZrVmwqaymb5NAE2K24ph8WTjYZMzJoM6_4L4LZXBBR9T67vllNjQ6Xi18xnv-M5fmH33eZD38CgYyXH5UH-BZbGGy3Gep3Li7jfuoUiYoGqYJ_JmGyDe1O4JTKOK8XbqkJARMN6dQ4vWnY6WJ9YbgMqJjUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود پیکر مطهر آقای شهید ایران به مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/farsna/447782" target="_blank">📅 05:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447781">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da69444ad.mp4?token=e7cYA-S7DoNrkdF2-T_Y4D8TSD2xyD3NgABCbZv0oIw7zrTikdoFPSIKovdI8Qg9yIm8vD6kL77VCmALjkYP4eWNfTJ2mKTmPWrpdxm5Tbv0Sl9pY8nGUzhiJj1djbd_8EAWHaZTtvDB1xO78OXHGBEG9XJXgIibS1Fr2QpIcqgiPMBVU2QzPa-b7tsEOY7Qz8OpJ7hhGti3uxYwAVo969BY2IjLoOMKmspG8q6L3r-PfhylHaktW9FgUdAz9CEj3K0HwK2i8hqXzSLrPKVR74FIpjXWP6dWBXs9wjQoStFAZ8qgbJeD3jG5j4KtzYaLzdb1tpDx5l0ngNjVWEkR7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da69444ad.mp4?token=e7cYA-S7DoNrkdF2-T_Y4D8TSD2xyD3NgABCbZv0oIw7zrTikdoFPSIKovdI8Qg9yIm8vD6kL77VCmALjkYP4eWNfTJ2mKTmPWrpdxm5Tbv0Sl9pY8nGUzhiJj1djbd_8EAWHaZTtvDB1xO78OXHGBEG9XJXgIibS1Fr2QpIcqgiPMBVU2QzPa-b7tsEOY7Qz8OpJ7hhGti3uxYwAVo969BY2IjLoOMKmspG8q6L3r-PfhylHaktW9FgUdAz9CEj3K0HwK2i8hqXzSLrPKVR74FIpjXWP6dWBXs9wjQoStFAZ8qgbJeD3jG5j4KtzYaLzdb1tpDx5l0ngNjVWEkR7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیت‌الله جوادی آملی بر پیکر رهبر شهید نماز می‌خواند
🔹
کمیته اطلاع‌رسانی ستاد تشییع رهبر شهید انقلاب در قم: نماز بر پیکر مطهر رهبر شهید انقلاب در شهر قم، توسط آیت‌الله جوادی ‌آملی اقامه خواهد شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/447781" target="_blank">📅 05:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266863d78c.mp4?token=J3W5_7uh97VTmD1NK7wffCavM5oX7KNN7fJJKDH8h1JtBc5Ah-SrVKU76YbZsBvS4xKtphrb8EQosdBT8rcSZcnp-PVdsWH06IghLWeoTSPuEOhDI_umYHT9Akzx0JkajeDsh5cx8V0s1BZ1fN1yLFWQk4OZRLMuDbthrW-SnrOEGM6yLvNbQmFiXxr-VLMu1l8goYewRbF_s42ER27KGbYvgj0_Bp7T2wDgIABao4xaMwR3saqc8ZbtDiahO0VsgOkdF4ST6fwDLJowtkDotFC_YZQjgdH_1cMKFEHA81lmrYFihDyPqXvpJjCHfOyRk5b4PlVH8R6wvbPIVeYN-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266863d78c.mp4?token=J3W5_7uh97VTmD1NK7wffCavM5oX7KNN7fJJKDH8h1JtBc5Ah-SrVKU76YbZsBvS4xKtphrb8EQosdBT8rcSZcnp-PVdsWH06IghLWeoTSPuEOhDI_umYHT9Akzx0JkajeDsh5cx8V0s1BZ1fN1yLFWQk4OZRLMuDbthrW-SnrOEGM6yLvNbQmFiXxr-VLMu1l8goYewRbF_s42ER27KGbYvgj0_Bp7T2wDgIABao4xaMwR3saqc8ZbtDiahO0VsgOkdF4ST6fwDLJowtkDotFC_YZQjgdH_1cMKFEHA81lmrYFihDyPqXvpJjCHfOyRk5b4PlVH8R6wvbPIVeYN-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از حضور خیل عظیم عزاداران در مسجد مقدس جمکران و خیابان‌های اطراف
@Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/447780" target="_blank">📅 05:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9a17b8ed.mp4?token=mHWMDagCEGnMLVbOWL2hfgUWVIAFcO-OZQ6_la1uhHFrGybmgPiY2sq75SFwljQ7t0BPcX5ieBpQ0ziGUXfO3pXLqIB8RvXLmw4A6s74QIu-eEcOFaVZmZv9UCkC_kN1LiHEPDVUNd4k8IjV7ZQDziTee5k8xQWRHf65zqBCfAASXhDWwOLhcp4rxeJUrTxtCl4uzWMVws45B2Yg7YGpVk66YZerFmbKkcq1OVxIbEK1uwdBx1zkcL2tQcgZ0DkkT9oqpF4fzBexTHjuOsr2LxzbKjqcSB8be0Ab1MAIsFvfruNrRC9RyE14p3xWPLjrz57Iwuut-7nuVYeA1k2B0iTLyeH5bjMAC_8kc4xewdeU1VsLglkIHO7kjThq94C18AM-7gdR64nWStR81lZnuSzrwOCFkP3y0BGGS1wXIM8WIloI7ZJRnFqtxzjcWvHLuFNKJ31_K-5qaIapizQCuC322Z4ZciCnggt8YqQPazLJpT_6IP-S7Ju8EqG-luDzEoByPEHzgp6HjB4IO7Uz6pSGv_J28k0nOwm40_RqNcji328fL1Y77JV8tmHVcsdDwkrFb2NvhU0f-Mz1vWEqlzRld-Ltm0n66z-qFS4PEwen8aSgV0ZlGNyz_QKYOEMvjQeVuaagxJaYzkn59Rd96pG2Q7s9JIYjw3P75geewUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9a17b8ed.mp4?token=mHWMDagCEGnMLVbOWL2hfgUWVIAFcO-OZQ6_la1uhHFrGybmgPiY2sq75SFwljQ7t0BPcX5ieBpQ0ziGUXfO3pXLqIB8RvXLmw4A6s74QIu-eEcOFaVZmZv9UCkC_kN1LiHEPDVUNd4k8IjV7ZQDziTee5k8xQWRHf65zqBCfAASXhDWwOLhcp4rxeJUrTxtCl4uzWMVws45B2Yg7YGpVk66YZerFmbKkcq1OVxIbEK1uwdBx1zkcL2tQcgZ0DkkT9oqpF4fzBexTHjuOsr2LxzbKjqcSB8be0Ab1MAIsFvfruNrRC9RyE14p3xWPLjrz57Iwuut-7nuVYeA1k2B0iTLyeH5bjMAC_8kc4xewdeU1VsLglkIHO7kjThq94C18AM-7gdR64nWStR81lZnuSzrwOCFkP3y0BGGS1wXIM8WIloI7ZJRnFqtxzjcWvHLuFNKJ31_K-5qaIapizQCuC322Z4ZciCnggt8YqQPazLJpT_6IP-S7Ju8EqG-luDzEoByPEHzgp6HjB4IO7Uz6pSGv_J28k0nOwm40_RqNcji328fL1Y77JV8tmHVcsdDwkrFb2NvhU0f-Mz1vWEqlzRld-Ltm0n66z-qFS4PEwen8aSgV0ZlGNyz_QKYOEMvjQeVuaagxJaYzkn59Rd96pG2Q7s9JIYjw3P75geewUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقی‌ها در قم پرچم خون‌خواهی رهبر شهید را بلند کردند
@Farsna
Link</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/447779" target="_blank">📅 05:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f137e1068.mp4?token=lnsygPlTCxwesnYCqFJNMZ25h8RHEFEm2ygmr5hII6LSZ1AySIRTTaEtmnLekkvEf1jv_GNgj2ralLfpn4TkLgppGCZT4hihn0Ae9CrGdvXLxIsndPKv55MBLhSG6b860ZYjCSLuwRWHZYx-RiQyFb7IrRt55U0q3Ix3aNsVUnKNXvf9DOMeHx3kUG4ncI48tVw1vyxT01WTwK4c15tcXYV0KTQpn3gQ3cHH-CAUJLcyfvtWi1bFruIB3SZcYnl99_AtoaOzi5D9MVSZqHnVb6PtyImUhdPB8V9cIhfUY-CCypdSTOsknNmsjihNlQqBoCs8Aixcjwo4Aqtyy7AefA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f137e1068.mp4?token=lnsygPlTCxwesnYCqFJNMZ25h8RHEFEm2ygmr5hII6LSZ1AySIRTTaEtmnLekkvEf1jv_GNgj2ralLfpn4TkLgppGCZT4hihn0Ae9CrGdvXLxIsndPKv55MBLhSG6b860ZYjCSLuwRWHZYx-RiQyFb7IrRt55U0q3Ix3aNsVUnKNXvf9DOMeHx3kUG4ncI48tVw1vyxT01WTwK4c15tcXYV0KTQpn3gQ3cHH-CAUJLcyfvtWi1bFruIB3SZcYnl99_AtoaOzi5D9MVSZqHnVb6PtyImUhdPB8V9cIhfUY-CCypdSTOsknNmsjihNlQqBoCs8Aixcjwo4Aqtyy7AefA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ما از لرستان آمدیم، برای بیعت آمدیم
◾️
مردم هم‌چنان درحال ورود به مسجد مقدس جمکران هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/447778" target="_blank">📅 05:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1013a01b5a.mp4?token=AMc74iB2ICc740Wd-orpOGObk3b52MNKVqvQpGzVh-GP3R4PHwQgTberykHNSLd4QpyWh_nNKzQCcdrGikbO-7AM3HbqqlbTM6tYt-qQCRS2PvO3WOncey_0KSYZwmOxxBumI2ss1YUhonQjSmXX7uTUJGEbb-N_brZA9kWx-fRmeunwnmMKqjBUFLk7GkltdqsV2a_Y26QsB_7q0x0cde7isJFUfZX7XrKdqEZo5Y2oFtYSVttXoBk7nvjfPtOKu4wxrdVhoNStLHJjlpjE7xC7I2N4R4AJWUWDHigkmJCLUM9h1R6-G7eITc-S8sA2rFbNmjn5vf18Iy5AvvH2mGkYSngO8Iq2TEgFCdxOSm6FlYaBqXpLcpT6ocz2ym1bbmxxY4q_7iyrs7WZYGts96ObFxL_XOFqZmYCTbxDEk6uGzKOYgPZm9Lulaz3jExi6uMu7jxGOUFmVFBgTwPPAwjEOX3kYeld-6eCzRA6R9Qx7EaBLsMa40fQlsGwkIR9pdUKDC02C8m1Fy-7D70nPuIFuuR8aGMQxlfEEp1dWDifixnzHIjecZvIRE5zua98UsaoURdCuidT2cpMMND5HhmFyqfAWtaSSKao5_1x_YtDCr_EOErzE-87mrzGXjf715e6foLOF-GiPnN-mpMnqBE2nODv0GjRO8X0BYyQZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1013a01b5a.mp4?token=AMc74iB2ICc740Wd-orpOGObk3b52MNKVqvQpGzVh-GP3R4PHwQgTberykHNSLd4QpyWh_nNKzQCcdrGikbO-7AM3HbqqlbTM6tYt-qQCRS2PvO3WOncey_0KSYZwmOxxBumI2ss1YUhonQjSmXX7uTUJGEbb-N_brZA9kWx-fRmeunwnmMKqjBUFLk7GkltdqsV2a_Y26QsB_7q0x0cde7isJFUfZX7XrKdqEZo5Y2oFtYSVttXoBk7nvjfPtOKu4wxrdVhoNStLHJjlpjE7xC7I2N4R4AJWUWDHigkmJCLUM9h1R6-G7eITc-S8sA2rFbNmjn5vf18Iy5AvvH2mGkYSngO8Iq2TEgFCdxOSm6FlYaBqXpLcpT6ocz2ym1bbmxxY4q_7iyrs7WZYGts96ObFxL_XOFqZmYCTbxDEk6uGzKOYgPZm9Lulaz3jExi6uMu7jxGOUFmVFBgTwPPAwjEOX3kYeld-6eCzRA6R9Qx7EaBLsMa40fQlsGwkIR9pdUKDC02C8m1Fy-7D70nPuIFuuR8aGMQxlfEEp1dWDifixnzHIjecZvIRE5zua98UsaoURdCuidT2cpMMND5HhmFyqfAWtaSSKao5_1x_YtDCr_EOErzE-87mrzGXjf715e6foLOF-GiPnN-mpMnqBE2nODv0GjRO8X0BYyQZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازخوانی مداحی «باید برخاست» در مسجد مقدس جمکران و اهتزاز پرچم‌های سرخ انتقام یالثارات الحسین(ع)
@Farsna</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/farsna/447777" target="_blank">📅 04:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4cae73280.mp4?token=E3WDEzsvi-s4mrq0s3rVnEYrwjn_oZ6mTVK_zStkck51QpTkzSsfnDKXXs1OwEOtPw67lEfld5vaeFxqk2ldFzhZMKtJBI6IPm55RmRfYQqElhdL_I_AMtAxWHTKXubelLwGykb2pLCU24EiAHYNQxyoWU32vc3_jU9gDJfPVezMVett6GDYpzoNskphupa5BpDV5fGT5nbJjsBlflThxJA7BPWnGQlKIxazspBjpuUKBoGX9KnV6CTR3jvBUz9MOSdJ-Y9FL8-dK6FUsbPglFZXHb8wDw8HC6SWEbOuuBGLi9cG8vBBoOBgxWJUCrgvwwluJutVdwe6Tlb88-zETA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4cae73280.mp4?token=E3WDEzsvi-s4mrq0s3rVnEYrwjn_oZ6mTVK_zStkck51QpTkzSsfnDKXXs1OwEOtPw67lEfld5vaeFxqk2ldFzhZMKtJBI6IPm55RmRfYQqElhdL_I_AMtAxWHTKXubelLwGykb2pLCU24EiAHYNQxyoWU32vc3_jU9gDJfPVezMVett6GDYpzoNskphupa5BpDV5fGT5nbJjsBlflThxJA7BPWnGQlKIxazspBjpuUKBoGX9KnV6CTR3jvBUz9MOSdJ-Y9FL8-dK6FUsbPglFZXHb8wDw8HC6SWEbOuuBGLi9cG8vBBoOBgxWJUCrgvwwluJutVdwe6Tlb88-zETA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم، پایتخت موکب‌های خارجی عاشق رهبر شهید انقلاب شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/447776" target="_blank">📅 04:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447775">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وقوع حادثه برای یک نفتکش نزدیک عمان
🔹
سازمان عملیات دریایی انگلیس از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در آب‌های شمال عمان خبر داد.
🔹
این نفتکش در حدود ۱۵ کیلومتری شرق شهرک «لیمه» مورد اصابت یک پرتابۀ نامشخص قرار گرفته و دچار آتش‌سوزی شده…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/447775" target="_blank">📅 04:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaclkoNy63701Dqu6iv4hH0ez0i2qRD-irlFS0SHTe_GTVssQKiV6puBCl5k9LOjz77wDdxiAJP8H8yD_55qNBRHqAvdTlp1yD0_rNiJ4AGM65f4P9IDwG0IIw0kIvqVPUu5rXYs9SqQX4AjtFRtgDrMRUaUBNohyvz12uQUk1w_9O-DWGv7SsUyTSPdyCnNLfVAizBm6wvKPvGIXirqg57u_Fop1zYtJQ6Qxj4oh-nH4nBm2uC6Eh9HSQkkiPws--Eb2VostuUVT31csL3X7-b_zBa4RaQU53X_m6vmcf3nDZayUo0neONLhYdkUBy3Lk1W4s1N180a8M7OGRbfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حضور فرزند شهید سیدحسن نصرالله در مراسم وداع با پیکر مطهر رهبر شهید انقلاب در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/447774" target="_blank">📅 04:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447773">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef58706c7.mp4?token=AQ59TJ0HJMugA-hSmaB23NlgatH4rWZYhOZUTHPu-6ralcyt3Ue9gZadhT_upAJkXkBboDYn4jCqSC2LiDXZLsMUUyHTF9qgUTuiI4XUg5EhXLfL49kTMKHH7AU3UIMkmLRmWDIZw6c6ZEXVBTlWzcU5Wb8Gxhkvig8nuIljhwun-hjFxa_AOCmEnIHeUA2RnTBxZ2BWgAq0t5H0AE6IIy1tYmZFEr-GMdEVceO9VvHlBCpTwimoRcUCkXgQZs0E9zfUNfbNJDzWDTaN5exwt24HW0ii2R7JPQRmfMlna0qmC0TLz9PcWRcQ7h9hnp5x09nEtufQQSfM4MuPIc21PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef58706c7.mp4?token=AQ59TJ0HJMugA-hSmaB23NlgatH4rWZYhOZUTHPu-6ralcyt3Ue9gZadhT_upAJkXkBboDYn4jCqSC2LiDXZLsMUUyHTF9qgUTuiI4XUg5EhXLfL49kTMKHH7AU3UIMkmLRmWDIZw6c6ZEXVBTlWzcU5Wb8Gxhkvig8nuIljhwun-hjFxa_AOCmEnIHeUA2RnTBxZ2BWgAq0t5H0AE6IIy1tYmZFEr-GMdEVceO9VvHlBCpTwimoRcUCkXgQZs0E9zfUNfbNJDzWDTaN5exwt24HW0ii2R7JPQRmfMlna0qmC0TLz9PcWRcQ7h9hnp5x09nEtufQQSfM4MuPIc21PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد مرگ بر آمریکای عزاداران امام شهید در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/447773" target="_blank">📅 04:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07b7f4c40.mp4?token=enMqnlH5pi7CqwfeLWKAY2nEDBy3aS9Tb3zHW7NyYtUvcssiq9b9ilm_iJeTEPcYZk2ZZGYI_w7lPzZxKJqlENSx2uqyH4fZBtqM5TQxfwJrKr8Cf7-yx1CwxCg3yjN4NkRLD9xRYu23E6h2wVxUHGLMoGN5DVGwc9Ix8mzqrIeSr2nGRAkOHY75b6kqZKFnEGAxEzKd3OYzSlDaO5oA1y6SC19TL0NCnidNsxANH9ecy-E4ccFUK8f4Cz0cBmbOn8K7PQ9RwLF1m3x9zsi_XXD-f009KqmPoQS_rKo4xqdEt5YbXOR8R5i3ekfflHhKL3SFyCiUcB3P0WOCnrwzKw_-bNn4f_Z51HfBY6AwMJPOf1IpP3zWVizvqvYLs1DLa6F650OqfmfK5RbNE_9brPEfqp-RnL7RdN8SXH87HyN1rtEkoXUzW6WZn4o-X98mep4EComRptDJvUuTuyX88zmEkJzuzXgiu8VYg2nHODc4jDJQ0Ap-1dqugNzRAyaSlOckL6oOS02bHyrSApzuEGhCnG1jBiFVfcTWrpRr8fraLPGpjtatiBkDpU3obI6QO4QmVLDjtqfl7Soc-Vd8N22LT7bBk1h8K6XxvWPzvmPaYG3J5G9OTT-9FQxIS3rO_rBx06TJf2zl-SBfIdDlltzQSJR67vBibp2KlEzt9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07b7f4c40.mp4?token=enMqnlH5pi7CqwfeLWKAY2nEDBy3aS9Tb3zHW7NyYtUvcssiq9b9ilm_iJeTEPcYZk2ZZGYI_w7lPzZxKJqlENSx2uqyH4fZBtqM5TQxfwJrKr8Cf7-yx1CwxCg3yjN4NkRLD9xRYu23E6h2wVxUHGLMoGN5DVGwc9Ix8mzqrIeSr2nGRAkOHY75b6kqZKFnEGAxEzKd3OYzSlDaO5oA1y6SC19TL0NCnidNsxANH9ecy-E4ccFUK8f4Cz0cBmbOn8K7PQ9RwLF1m3x9zsi_XXD-f009KqmPoQS_rKo4xqdEt5YbXOR8R5i3ekfflHhKL3SFyCiUcB3P0WOCnrwzKw_-bNn4f_Z51HfBY6AwMJPOf1IpP3zWVizvqvYLs1DLa6F650OqfmfK5RbNE_9brPEfqp-RnL7RdN8SXH87HyN1rtEkoXUzW6WZn4o-X98mep4EComRptDJvUuTuyX88zmEkJzuzXgiu8VYg2nHODc4jDJQ0Ap-1dqugNzRAyaSlOckL6oOS02bHyrSApzuEGhCnG1jBiFVfcTWrpRr8fraLPGpjtatiBkDpU3obI6QO4QmVLDjtqfl7Soc-Vd8N22LT7bBk1h8K6XxvWPzvmPaYG3J5G9OTT-9FQxIS3rO_rBx06TJf2zl-SBfIdDlltzQSJR67vBibp2KlEzt9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بغض دختر لبنانی وقتی از رهبر شهید حرف می‌زند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/farsna/447772" target="_blank">📅 04:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6719732a.mp4?token=p2tR-TsaoE8hQFids-H3w6sunY5aDX9cO1hWnR-Ar8_MJ_bcPGFyI1Xpjg_DboD7vK2nrEjs5HJsudhoDAIUKP6SiLJ9h4nEX3dL2hJ5aPsGxgvZHiIFfHz-7A7fk5gXGjO1QQ2SUyj_jQ6Y_6l26m97mVYX-G-ZXVKH9QvKsdl4URV2Ws_dGGZSHmsHRXWhTj9RTLe9dlIUTzE6C3UfjfBmCS4VuVvjIkA-mLxuWXYWbbMe06axxs6xyW6Hpeq14Dyg-FgLdEyv4m-BmCnIEpjoiFnxcVui3hn1IwjQeRWESRa0AJ5m_qL-MyVNUZXxEn_unJ6fFcmJr5YQQEPGqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6719732a.mp4?token=p2tR-TsaoE8hQFids-H3w6sunY5aDX9cO1hWnR-Ar8_MJ_bcPGFyI1Xpjg_DboD7vK2nrEjs5HJsudhoDAIUKP6SiLJ9h4nEX3dL2hJ5aPsGxgvZHiIFfHz-7A7fk5gXGjO1QQ2SUyj_jQ6Y_6l26m97mVYX-G-ZXVKH9QvKsdl4URV2Ws_dGGZSHmsHRXWhTj9RTLe9dlIUTzE6C3UfjfBmCS4VuVvjIkA-mLxuWXYWbbMe06axxs6xyW6Hpeq14Dyg-FgLdEyv4m-BmCnIEpjoiFnxcVui3hn1IwjQeRWESRa0AJ5m_qL-MyVNUZXxEn_unJ6fFcmJr5YQQEPGqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تمام خیابان‌های قم به سمت جمکران مملو از جمعیت است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/447771" target="_blank">📅 04:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6dd50ce2.mp4?token=muEJSmFltckutShxvJAm7PQHchaZvKK5Em_fJTnuAN0SsYFyQY6EIwKLYMxHfLK6hS3esJLQISV-XxS8goIEgfhL1tD6hPb0trDjRq26eS8OCFjLV-KYHmP1CkzA-AtYM3Azld-cqutYijjzXqG-ZScHwWQko8FS1pg-m2n0-na9JI4k4c6sdl7AOm87MjhLM3caLwdNBKMHLHnMw6GgQkjsCsQW1Kono6F3PGbdYEOzFZ6LoXW1OqFcgzStJytMgEbIuHKo8e70DbWqiPeax5LghpMmgubGiOnXA2jcnBH7aaRncijRQP3Qr3hEDFLEl7_Khgpk45FeE-VuJWd8jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6dd50ce2.mp4?token=muEJSmFltckutShxvJAm7PQHchaZvKK5Em_fJTnuAN0SsYFyQY6EIwKLYMxHfLK6hS3esJLQISV-XxS8goIEgfhL1tD6hPb0trDjRq26eS8OCFjLV-KYHmP1CkzA-AtYM3Azld-cqutYijjzXqG-ZScHwWQko8FS1pg-m2n0-na9JI4k4c6sdl7AOm87MjhLM3caLwdNBKMHLHnMw6GgQkjsCsQW1Kono6F3PGbdYEOzFZ6LoXW1OqFcgzStJytMgEbIuHKo8e70DbWqiPeax5LghpMmgubGiOnXA2jcnBH7aaRncijRQP3Qr3hEDFLEl7_Khgpk45FeE-VuJWd8jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداران امام شهید همچنان در حال ورود به جمکران‌اند  @Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/447770" target="_blank">📅 03:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74704832ef.mp4?token=Lniq_i3hLPGIsU1yV9mXkefbrS7S3o7wXYWmRCqbCeJ8SXrsu_equzAagXi0t0SDnB6VfOxkRk39m7J7v5ZTaCZ_QDNDTxO6F0ntA6C4IQ3eqC5jRfaV5mOWZpo25HdvMbMEzkl_29NoPBictFEA6l1p2QX_G7FjJw2nXcSC70e5JL6mV9ByIlMXGlgFo7Vy6L0J9YbPEfOkmatnq14T9d7_WCF_eFG6hiC_5r3yBYCTt-OvNTuGl8VqI6CUkn45rwIcP1hXqGV1A32qLbe2KbpqAhHOAz5SWJkFCPykYUASBRTx6RsMVAm2D-kcZLi8TLDJGKFpIdDCXFpsvWV8tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74704832ef.mp4?token=Lniq_i3hLPGIsU1yV9mXkefbrS7S3o7wXYWmRCqbCeJ8SXrsu_equzAagXi0t0SDnB6VfOxkRk39m7J7v5ZTaCZ_QDNDTxO6F0ntA6C4IQ3eqC5jRfaV5mOWZpo25HdvMbMEzkl_29NoPBictFEA6l1p2QX_G7FjJw2nXcSC70e5JL6mV9ByIlMXGlgFo7Vy6L0J9YbPEfOkmatnq14T9d7_WCF_eFG6hiC_5r3yBYCTt-OvNTuGl8VqI6CUkn45rwIcP1hXqGV1A32qLbe2KbpqAhHOAz5SWJkFCPykYUASBRTx6RsMVAm2D-kcZLi8TLDJGKFpIdDCXFpsvWV8tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترکیه‌ای‌ها در قم فریاد خون‌خواهی سردادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/447769" target="_blank">📅 03:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaf812dde3.mp4?token=J85PrINIFbizFS2x0XSDETr3P-f5J0W4oNO3IGmFpXsHOk-DQm6BLovVdZSlAArvMpWYybLeMR8ZgeV3et5951ghntK9fGxP1EhW8A30Su5UJ_Tb40w6RG0ISsOgSlOUb9chYQ3DRGMyQi0EDOM3ur7Ut0JNPeWdmqwISM1inUN9TCoqtOQH8iKSYVZqbK8dFLY2phvS8k3Nbj9E__UQQFninqfQa4zeQo8xdqZu8l5xcrO385h2ddiM2Ak7jcRI1aNqRMM0nvK_21QtfmI6mBEnSCimDav8WkZK2TYe5qb3hTaf-LoEUuP1TrUEukHn2XRy4YPXEI1MIGDcuGr5m4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaf812dde3.mp4?token=J85PrINIFbizFS2x0XSDETr3P-f5J0W4oNO3IGmFpXsHOk-DQm6BLovVdZSlAArvMpWYybLeMR8ZgeV3et5951ghntK9fGxP1EhW8A30Su5UJ_Tb40w6RG0ISsOgSlOUb9chYQ3DRGMyQi0EDOM3ur7Ut0JNPeWdmqwISM1inUN9TCoqtOQH8iKSYVZqbK8dFLY2phvS8k3Nbj9E__UQQFninqfQa4zeQo8xdqZu8l5xcrO385h2ddiM2Ak7jcRI1aNqRMM0nvK_21QtfmI6mBEnSCimDav8WkZK2TYe5qb3hTaf-LoEUuP1TrUEukHn2XRy4YPXEI1MIGDcuGr5m4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاج حسین یکتا: وداع با پیکر رهبر شهید، آغاز مسئولیتی بزرگ برای انقلابی‌هاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/447768" target="_blank">📅 03:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0c2622f9.mp4?token=krVlI330chWo5x7QR-tCOLPoXyvxLpNWyf7A5NZCV_oD1JzcYdlQ15z9yEDKZtzkR0QyG5P_0GxGIG2NNsKEWjGkucMZ-6aAdW2DqKk7QydZzhIVGt8HV8CsU1CjnkmzSXZ3XYA3g2b1avDP-0zi_Dan_gniG6FvpUiONAX3s96ZwRSUrf-VYgpWXMkb2cvVlqo4cK0NkBf0iX_yTlfIZmVJih9lhrT7DWMxvLMnefucGCSjLjXtbvBaOw3jkz787H3QJ3CWNXx4oBHdIieXDgZBDEHsYZ77uTLdkYyGLGXbNaogSSjRX-k29aoutyhftbRv9iT2uFGisUp8-2VoAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0c2622f9.mp4?token=krVlI330chWo5x7QR-tCOLPoXyvxLpNWyf7A5NZCV_oD1JzcYdlQ15z9yEDKZtzkR0QyG5P_0GxGIG2NNsKEWjGkucMZ-6aAdW2DqKk7QydZzhIVGt8HV8CsU1CjnkmzSXZ3XYA3g2b1avDP-0zi_Dan_gniG6FvpUiONAX3s96ZwRSUrf-VYgpWXMkb2cvVlqo4cK0NkBf0iX_yTlfIZmVJih9lhrT7DWMxvLMnefucGCSjLjXtbvBaOw3jkz787H3QJ3CWNXx4oBHdIieXDgZBDEHsYZ77uTLdkYyGLGXbNaogSSjRX-k29aoutyhftbRv9iT2uFGisUp8-2VoAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وَلَا تَحْسَبَنَّ الَّذِينَ قُتِلُوا فِي سَبِيلِ اللَّهِ أَمْوَاتًا بَلْ أَحْيَاءٌ عِنْدَ رَبِّهِمْ يُرْزَقُونَ
◾️
ساعاتی پیش از مراسم اقامه نماز بر پیکر مطهر رهبر شهید انقلاب در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/447767" target="_blank">📅 03:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d5020c7f.mp4?token=TFQY42ZpF-SkMSeCtiMURNYYYiloUYvZ0YLiLVXx2EfU6HlfIy_AusxdQdQrsbfCXCoukxM-uDN2Bn3ZjL3_xJnpoAmLYraC79yMGl7B7WF5E0pCRW8fNL6F9_mDnXYJkm0G1kS_cIBLwpH3CSKFoPwW8SlcW41VaQPmk0JGRk6_69AmwK6f3xlFkEIitCFxciXZsOWxnt9Ath6EEjFPC0bFf3kzGErejSbZPyAoC5Kl5Q55N3_q13rsNG5QPZNdsHN1PJdUqSfHk2s4ge30XHhqK_PmUAn_nlcHR9L_NqRrsx4ccoBXAba76fmRcPtE02GKj5Og2VlwhKLC4guvCSz7dCAd8pzta_r_HJdxz8zEk7Go6lL_CP8nsxUGlGsFa0tB5YtKUAZ2q2kE5Fz3lSq3-0luJH5HsY4ymkICOjTQBlxPondTxs_9piAK79jJ3ldSDyiGsDl6lQbZNPqLsSocE-SdwiqwTkvqy1n0Cmebx0g6iTE9Lh9Ts5EjthUjyIO6dVgI0hQKwpsLlZLbxE6z9Iupq7DtE8zxClQYmxp3DWn6TooYkriVxdENWlXMS4HM22IxrW0WtXJ2n1knb6TlWgeV3Nc_96gvF4iLrgKX_mUSO_3WRcV-KvXIe3BZMJK9Ru4L0oHNEnrcn0yrT0y5vLNpfZlubmcv8tyqKOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d5020c7f.mp4?token=TFQY42ZpF-SkMSeCtiMURNYYYiloUYvZ0YLiLVXx2EfU6HlfIy_AusxdQdQrsbfCXCoukxM-uDN2Bn3ZjL3_xJnpoAmLYraC79yMGl7B7WF5E0pCRW8fNL6F9_mDnXYJkm0G1kS_cIBLwpH3CSKFoPwW8SlcW41VaQPmk0JGRk6_69AmwK6f3xlFkEIitCFxciXZsOWxnt9Ath6EEjFPC0bFf3kzGErejSbZPyAoC5Kl5Q55N3_q13rsNG5QPZNdsHN1PJdUqSfHk2s4ge30XHhqK_PmUAn_nlcHR9L_NqRrsx4ccoBXAba76fmRcPtE02GKj5Og2VlwhKLC4guvCSz7dCAd8pzta_r_HJdxz8zEk7Go6lL_CP8nsxUGlGsFa0tB5YtKUAZ2q2kE5Fz3lSq3-0luJH5HsY4ymkICOjTQBlxPondTxs_9piAK79jJ3ldSDyiGsDl6lQbZNPqLsSocE-SdwiqwTkvqy1n0Cmebx0g6iTE9Lh9Ts5EjthUjyIO6dVgI0hQKwpsLlZLbxE6z9Iupq7DtE8zxClQYmxp3DWn6TooYkriVxdENWlXMS4HM22IxrW0WtXJ2n1knb6TlWgeV3Nc_96gvF4iLrgKX_mUSO_3WRcV-KvXIe3BZMJK9Ru4L0oHNEnrcn0yrT0y5vLNpfZlubmcv8tyqKOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظات ملکوتی اذان صبح در مسجد مقدس جمکران، ساعاتی پیش از اقامۀ نماز بر پیکر مطهر آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/447766" target="_blank">📅 03:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447765">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04737890b6.mp4?token=GFa96Nvfe3CMd4Lic2lN0EQKfqT2roLQrLDD9qvrAjtQpzn3KEh2UknIio1K6E8wzMFJ1Yjx3FEJ9_yf0R-KUCnTzL5zeklJPRizXxn-0AdSyt5EP9nqmqqZOXR7FuOU1cHcrJ9QpLgUZXa0yU2YIOUHN6_sTwNZYsU70Ph_SyEZysmTGTeEtlXxP7bw5nX8V_npGgzYcO_JQPcfGKwvGjt08EqmUHzHQtEVPyzOHonn5FBEsCjSmT8fhFdfRwF_fKK9UKhShZqGlZgTBgn5RuGwtJqQvT618_z1QTlU8JZ7g3QZtqtPm9A183mIRu4Tk6kqY_4fVMIMNUqrIVhwCIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04737890b6.mp4?token=GFa96Nvfe3CMd4Lic2lN0EQKfqT2roLQrLDD9qvrAjtQpzn3KEh2UknIio1K6E8wzMFJ1Yjx3FEJ9_yf0R-KUCnTzL5zeklJPRizXxn-0AdSyt5EP9nqmqqZOXR7FuOU1cHcrJ9QpLgUZXa0yU2YIOUHN6_sTwNZYsU70Ph_SyEZysmTGTeEtlXxP7bw5nX8V_npGgzYcO_JQPcfGKwvGjt08EqmUHzHQtEVPyzOHonn5FBEsCjSmT8fhFdfRwF_fKK9UKhShZqGlZgTBgn5RuGwtJqQvT618_z1QTlU8JZ7g3QZtqtPm9A183mIRu4Tk6kqY_4fVMIMNUqrIVhwCIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائران هندوستانی در مسیر جمکران برای تشییع امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/447765" target="_blank">📅 03:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447764">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_DtaI1kqViYMK1dPSEO_lGRPvNjYzqHYrauVW5fi_BzW44dE26CEuDUOsKGEqTka4uH0YvjCy5L-lR4u8hbOcFDtIrVL7DlM4pt2TedCnlsdVvqLkXN_s8C-ikRxEtT7LbgsJGw4QGdANAQ3I12t3RDQY_smYIxHXVNOD6GGVfg94eABWrREvZYCArKlI5rKarR3bLomq3ztNktuWrEjtK7qiFF6ruzR_cKsEGyorcNsnC_VcvPtZf2ixGhPzR-oZhwbtb4qGUIX-wqSqWu3rXImMwTplQMJgf8rMbnySsf9geoqygBEd4Zc_TVMfdVjXsNS6dinMz16CvbP8CX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقوع حادثه برای یک نفتکش نزدیک عمان
🔹
سازمان عملیات دریایی انگلیس از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در آب‌های شمال عمان خبر داد.
🔹
این نفتکش در حدود ۱۵ کیلومتری شرق شهرک «لیمه» مورد اصابت یک پرتابۀ نامشخص قرار گرفته و دچار آتش‌سوزی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/447764" target="_blank">📅 03:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447763">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773824177a.mp4?token=ZF_R7sl237lkFReJdkoY5yM7ea6sJuokm2Wr9JyuHIHb9Dx1adD7bWaOx6ZHovVZDmHpeCv1_FLnbkbJkkSZCWNW-j9UK290RgbGKCNSNyMLSdAZSv-QIdmMmEF3odSdLeVC3h-GgDCtl-usDKJ6SOqRm5rex0AqzWCOL3ZxyQx-oGJlPAjNWqED9Yo-2pn6MLEB5c1Oqcs0y754PU8XqkclywdUrLISA43cLoglgjz-NQ-24UA-2de8CYF9-SHCJ6S9wPC50Bzy0wQZSbgELRGgGg1gPS1B8TMqzL6xY8WfmrhXlAjF8qzqVGXmXDbDZvLY3rwwEjjkPStlnoWp5GuPOFEV9kEfWGBb1jnrO9SK1W2kmWrOEgXdOd0nspt7hntjFkGb39uq_2GA_K8JxvK0lGj7zOx3oLvYdmdQGiyCTZKnRJFLbHNum3mnFQMLm-nfIcimLM1EVhhfLdMkTQkMPUWzWoiSIrkI1nNHSw7iRgTPXUoFgmGA9s9H1x2WUjpwlpReHo_65gUbDkZRa47IEKEbDHj5LBkRwtbVXO9RiqdHlMUiqwkmC2y3w9fIXEjytA0UYBedtHT0vO4Wai7fqHID0Vj9e_s-bM125uuC39w8niQKOhzwMwh66nHSxyqo3hlBh79jWKpSHO94AuoaXyt2MTRXVXvcozu9d4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773824177a.mp4?token=ZF_R7sl237lkFReJdkoY5yM7ea6sJuokm2Wr9JyuHIHb9Dx1adD7bWaOx6ZHovVZDmHpeCv1_FLnbkbJkkSZCWNW-j9UK290RgbGKCNSNyMLSdAZSv-QIdmMmEF3odSdLeVC3h-GgDCtl-usDKJ6SOqRm5rex0AqzWCOL3ZxyQx-oGJlPAjNWqED9Yo-2pn6MLEB5c1Oqcs0y754PU8XqkclywdUrLISA43cLoglgjz-NQ-24UA-2de8CYF9-SHCJ6S9wPC50Bzy0wQZSbgELRGgGg1gPS1B8TMqzL6xY8WfmrhXlAjF8qzqVGXmXDbDZvLY3rwwEjjkPStlnoWp5GuPOFEV9kEfWGBb1jnrO9SK1W2kmWrOEgXdOd0nspt7hntjFkGb39uq_2GA_K8JxvK0lGj7zOx3oLvYdmdQGiyCTZKnRJFLbHNum3mnFQMLm-nfIcimLM1EVhhfLdMkTQkMPUWzWoiSIrkI1nNHSw7iRgTPXUoFgmGA9s9H1x2WUjpwlpReHo_65gUbDkZRa47IEKEbDHj5LBkRwtbVXO9RiqdHlMUiqwkmC2y3w9fIXEjytA0UYBedtHT0vO4Wai7fqHID0Vj9e_s-bM125uuC39w8niQKOhzwMwh66nHSxyqo3hlBh79jWKpSHO94AuoaXyt2MTRXVXvcozu9d4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگواری بانوان جاماندۀ دزفولی برای آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/447763" target="_blank">📅 03:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447762">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a66b0e84.mp4?token=giGRLswdvV7wx7fzcENNQO_xlQiKZljXzLo4Pu8qo-d4g_RxBnLNBEHqdBh1-0KkDKYsNFTe7QBjho_rafb9e6UKfvgkXhEtf_k8rPcLN1ptr6PT8W8bSGz1PPp5LVre2PyZZEn5l0yb5qt092pYysUx_CbpF08y3NIt0kri8mrVsOMxBJOK1975QQEoNgF39angOQJSvMhsNFPd1vUupuVZPJNWiXuJPY5BbJSaK3yVl7HpDxLziRH7rdAJ0qykvz9KuCNhw7ATiLBroJdCBWKNhzTAQ6Ehs02E7bvb1N0TuRnIzhXAPakObqVyRdZpWxIHwrOEAQ833GYWXOJycw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a66b0e84.mp4?token=giGRLswdvV7wx7fzcENNQO_xlQiKZljXzLo4Pu8qo-d4g_RxBnLNBEHqdBh1-0KkDKYsNFTe7QBjho_rafb9e6UKfvgkXhEtf_k8rPcLN1ptr6PT8W8bSGz1PPp5LVre2PyZZEn5l0yb5qt092pYysUx_CbpF08y3NIt0kri8mrVsOMxBJOK1975QQEoNgF39angOQJSvMhsNFPd1vUupuVZPJNWiXuJPY5BbJSaK3yVl7HpDxLziRH7rdAJ0qykvz9KuCNhw7ATiLBroJdCBWKNhzTAQ6Ehs02E7bvb1N0TuRnIzhXAPakObqVyRdZpWxIHwrOEAQ833GYWXOJycw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداران امام شهید همچنان در حال ورود به جمکران‌اند
@Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/447762" target="_blank">📅 02:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447761">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef9060ba02.mp4?token=qL_Rzfudm5v-by5DB0nc3zwjleYaP7f8KKYiyh4H90FKaUbuUfcGSFgxhCFwG9Oini6YhY0PUagJmZgqguCq_EZw1774IONv4gR9b70E6KQDUctrBtzOhfq1VnDXgAFyDp7bcAAltXxyWZe-jY-w0meZ2bLCkNIAWGbZxJ-Tberg-Uz0W4avQ9W3cwFB8z5YQghftqrXel4GuiwHo4VomOXqYYaFTKkebX9RjD_swW4y04jkFNoAFh5fL5WmYsahebflEvP1gtU5wG7qKpYuManr23VRzKjwfpFKWQmbT22A57Mlz0KBwY22en95F2jxmd1ZKwszJOlpZxIdRqDJMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef9060ba02.mp4?token=qL_Rzfudm5v-by5DB0nc3zwjleYaP7f8KKYiyh4H90FKaUbuUfcGSFgxhCFwG9Oini6YhY0PUagJmZgqguCq_EZw1774IONv4gR9b70E6KQDUctrBtzOhfq1VnDXgAFyDp7bcAAltXxyWZe-jY-w0meZ2bLCkNIAWGbZxJ-Tberg-Uz0W4avQ9W3cwFB8z5YQghftqrXel4GuiwHo4VomOXqYYaFTKkebX9RjD_swW4y04jkFNoAFh5fL5WmYsahebflEvP1gtU5wG7qKpYuManr23VRzKjwfpFKWQmbT22A57Mlz0KBwY22en95F2jxmd1ZKwszJOlpZxIdRqDJMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماهنگ «محراب جمکران»
🔹
لحظاتی از حضور رهبر شهید انقلاب در مسجد مقدس جمکران
@Farsna</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/farsna/447761" target="_blank">📅 02:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447760">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/795c89354d.mp4?token=NCPzxSLzClud3GsoUuyJ-YHm5RaZf7xo_VMXnWXnWPzWLrSoofd1U7pS2wVyDvZV9ntNkQlY6KulpmVh3kKsqtFn06mFXZSXa0ozRtZk1snq7wnxxkFRIrt-DGiD1j43wRPmfTcWk0_TrrlIz3h-goZ0sYBOd9LiPTaAOhRR6D7EDG_VjBdWP2OTWyEcZVwV8PafHWEIH_wq1tFTeqo1yc3Mu2gIlm1CQmI0e79kwGc-AHnu0ygWyqLnie7kpLTe8FzkMQOdBcHvN9ctu9qxeOiH9sBC2ImI4gAQnkkPfgiJrrqmyQI0niHLparsTAWZ-LXfies018SQS3O4RB5aAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/795c89354d.mp4?token=NCPzxSLzClud3GsoUuyJ-YHm5RaZf7xo_VMXnWXnWPzWLrSoofd1U7pS2wVyDvZV9ntNkQlY6KulpmVh3kKsqtFn06mFXZSXa0ozRtZk1snq7wnxxkFRIrt-DGiD1j43wRPmfTcWk0_TrrlIz3h-goZ0sYBOd9LiPTaAOhRR6D7EDG_VjBdWP2OTWyEcZVwV8PafHWEIH_wq1tFTeqo1yc3Mu2gIlm1CQmI0e79kwGc-AHnu0ygWyqLnie7kpLTe8FzkMQOdBcHvN9ctu9qxeOiH9sBC2ImI4gAQnkkPfgiJrrqmyQI0niHLparsTAWZ-LXfies018SQS3O4RB5aAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیل عظیم عزاداران امام شهید در مسجد جمکران، ساعاتی پیش از شروع مراسم
@Farsna</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/447760" target="_blank">📅 02:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0690d9ce.mp4?token=erudLzww1Pgsd6tdI8y01SyoWEK8M2Jr99cR4y60L1fuZnIH9UEaCh2s34F6ZadfkNVbx4TvElkM8lu4uidyUPgBIZ1WziZwZ2f9zjzE0BZx_zioneh9dOkRWY-iBz3tZK72nnwgspA6YVriVX6WCIsnAg-w9jgW6ry4aH2tdS9YT6SSnOnWsS5R4Fv5jQmLU_KXzMUsKiSfBxcoAcFT4azcT0eZHWE2WaN7YmwDl3J4IB8dZuXRU5onbkHSCU1TXPQguNrQHOk3Wjccy7QXVW1VSwkZN6CIksEUaf-IklchuQ8yLbwmobymHT4YLw3G01vlnUXTx3nP97cjOQy9Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0690d9ce.mp4?token=erudLzww1Pgsd6tdI8y01SyoWEK8M2Jr99cR4y60L1fuZnIH9UEaCh2s34F6ZadfkNVbx4TvElkM8lu4uidyUPgBIZ1WziZwZ2f9zjzE0BZx_zioneh9dOkRWY-iBz3tZK72nnwgspA6YVriVX6WCIsnAg-w9jgW6ry4aH2tdS9YT6SSnOnWsS5R4Fv5jQmLU_KXzMUsKiSfBxcoAcFT4azcT0eZHWE2WaN7YmwDl3J4IB8dZuXRU5onbkHSCU1TXPQguNrQHOk3Wjccy7QXVW1VSwkZN6CIksEUaf-IklchuQ8yLbwmobymHT4YLw3G01vlnUXTx3nP97cjOQy9Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوگواری زائران حرم امام‌رضا(ع) برای آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/447759" target="_blank">📅 02:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikuBquKy13veX30hmoCs9qusJBle72PsOj6ijFGfqvGhliw-rAdo-xHXWZlRMinoDzcprsVeOwZN776nEWrFdHVcPUMnm5fPM50joHemAOuXMwcyTSC2N1e0jwrKeuVUf8oelCL9IFam1vHG0fcd209jOz5iK9v8nHOCSU44nU38eXCcbziybEjV6tcliD1IrpHIqiIJVYylgKDaugjF0XMlOoD9ROSEraSU_lvmPwsD2TMBLAhaN9EmCPjyuBjOtrB6Q5LRxFTXvT3DzgytNvYbV7aKspkV_yfxwhkSbIlnBBe7DDcChpxVLKftxBqXLAsQ3GfVf2yhRf-p1P6aVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">التماس رئیس‌جمهور لبنان به ترامپ برای خارج کردن اسرائیل از این کشور
🔹
رئیس جمهور لبنان شامگاه دیشب ملتمسانه از آمریکا خواست که برای خارج شدن نظامیان صهیونیست از جنوب لبنان، به تل‌آویو فشار بیاورد.
🔹
جوزف عون، که تسلیم‌شدن به آمریکا و اسرائیل را به مقاومت در برابر اشغالگری ترجیح داده، گفت:‌ ادامۀ اشغال، مشروعیت دولت لبنان را تضعیف می‌کند، مانع استقرار نیروهای مسلح [لبنان] در امتداد مرز جنوبی می‌شود و اجرای توافق‌نامۀ امضا شده در واشنگتن را زیر سوال می‌برد.
🔸
پیش از این، دولت عون با
ارائۀ امتیازات بسیار بزرگ به صهیونیست‌ها
ذیل پیوست محرمانۀ توافق بیروت-تل‌آویو موافقت کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/447758" target="_blank">📅 02:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qArV90BOczv1u-TOFJam6lslv7Ry84d-vRb0b3YCeDHZ6Osi7YuMKiXUmCqQIYQ9i1ULsrDegultl_yM8OhbHuT8Aa9pDwUgoQkGwy-75tf_0Klke81NlJWKqHpyQI-L9c9uLRfdCDFVDSHrbb62GtElzYB5B7M34yBkrd1i3bBHn81wZwEmT21eBHz9YEH5qlR_dPuVP7aZa56-S5Nu2tlk6zegg4Zy7y34wbIT2CHy65jB0635E3qLsCrMZkEDQpAmqbQcwY6GMjpy1F-p9LNCCI3CwwzX5BKNZVUCoJM0UTC7VsZfo90BIp9b2NJSxSYg79L2HA6hIeoP_Wp3pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو: این آخرین جام‌جهانی من بود
🎙
کریستیانو رونالدو:
‏
🗣️
من ناراحت هستم، اما تمام تلاشم را کردم. این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ ادامه دهم.
🗣️
پرتغال قبل از من هیچ‌جامی نبرده بود اما حضور من باعث کسب سه جام ملی شد.
🗣️
نمی‌توانم تایید کنم که این آخرین بازی من با تیم ملی است یا خیر. تحت تأثیر لحظه یا احساسات تصمیم نمی‌گیرم.
@Sportfars</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/447757" target="_blank">📅 02:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb0e831d3.mp4?token=kPaT_ESC7Mc2x46jCIzRMcXdV6YFafngz0LS7iBBDbZuPvuKUb_4nkXJmqNG0KA8Ac3-SBJBvB0c_a3_XGdbEMcsEkdiVV46YHZw7Su7W1ACGbLU0BKMKGgZvQ-9t7MHh-UYiKo3kRDhnQcEwpyAEPK8VqxEHg-hbDS9nzzaZgKDPjxcUrFv4aXYXQtQ4jcGSCPpqSa17ZBoC8cLdS9D9ZG0NBquV3jJX4sy52VzWU39Lz_EUB8utgvrbzbA7ZjUEXBf5TgRYNDN9zckVtL13fKuR0SPoZucPEhs1QTN4lXERYCrkMG17nHH_tg4FBHDZD-rV1PPZMhlYEQTd_lPug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb0e831d3.mp4?token=kPaT_ESC7Mc2x46jCIzRMcXdV6YFafngz0LS7iBBDbZuPvuKUb_4nkXJmqNG0KA8Ac3-SBJBvB0c_a3_XGdbEMcsEkdiVV46YHZw7Su7W1ACGbLU0BKMKGgZvQ-9t7MHh-UYiKo3kRDhnQcEwpyAEPK8VqxEHg-hbDS9nzzaZgKDPjxcUrFv4aXYXQtQ4jcGSCPpqSa17ZBoC8cLdS9D9ZG0NBquV3jJX4sy52VzWU39Lz_EUB8utgvrbzbA7ZjUEXBf5TgRYNDN9zckVtL13fKuR0SPoZucPEhs1QTN4lXERYCrkMG17nHH_tg4FBHDZD-rV1PPZMhlYEQTd_lPug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ممنونم اگر نروی، میمیرم اگر بروی...
◾️
گلباران پیکر مطهر امام مجاهد شهید توسط مردم عزادار در خیابان آزادی تهران
@Farsna</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/447756" target="_blank">📅 02:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba1c4bcc.mp4?token=vxsP9nGRW591MH1qHXggBFVcuC3NM8y6TGYfyUgtc7CEr-RR_sJC8gIDxs_vlSx-kGdwofwG3apMOsXpZlwxxTT4JKEdUAnsOPGMDYcFMaG_6pR-t888v6dxR9cwGDDQP-64P_zsNBGLyvYV9xrz_t7_Q0bEzR1lxFPALCV82QSezsDNZajvQzyst5jjEx4pNEe_rGVzZINfDSgM5boDq24ZiaBOZpg1A7gSsK4qe5z1EvebG0VJYhvpsO5ghD6-ulq9N-aclWJRw2-kaBKSbxL7C7Jy2EsQ7v79B2BOPel5-faX2F-ZqfmB5RyNGxURJTT9ojHdV7DT2XiAA9OJWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba1c4bcc.mp4?token=vxsP9nGRW591MH1qHXggBFVcuC3NM8y6TGYfyUgtc7CEr-RR_sJC8gIDxs_vlSx-kGdwofwG3apMOsXpZlwxxTT4JKEdUAnsOPGMDYcFMaG_6pR-t888v6dxR9cwGDDQP-64P_zsNBGLyvYV9xrz_t7_Q0bEzR1lxFPALCV82QSezsDNZajvQzyst5jjEx4pNEe_rGVzZINfDSgM5boDq24ZiaBOZpg1A7gSsK4qe5z1EvebG0VJYhvpsO5ghD6-ulq9N-aclWJRw2-kaBKSbxL7C7Jy2EsQ7v79B2BOPel5-faX2F-ZqfmB5RyNGxURJTT9ojHdV7DT2XiAA9OJWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بامدادی حرم حضرت معصومه(س)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/447755" target="_blank">📅 01:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b606cf8c9e.mp4?token=kZTplAIBJMRXSSZ30K-C48o27wXFYFYNlrIbPqcDh586OYXVmSEW5E1V0TSb1cydkRORUKb4InjfGDVopVeyQ-5n9Yyzp9p2lB1Dly3Hf1noBTU9C647GTpJDoA4UOv-rEJ_pezbuDdt81bGKjrtDBcdBGa_6CvMPCpr83Yu94uni62jVvmjJjYVfNYc3Es5KSRBa1_k47YUu7gD2TcPj5gv_Zf4ytkjlemwRUXahRrxbToHGes8aODtFKVN7qMO-m887JivIennb3R4QnEGFLXfM7m6JxkzTWZ3p4xuZdBdKozoxNSE0hX2gKdavDDFj-ctfVefQhtJjjfnZQZq8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b606cf8c9e.mp4?token=kZTplAIBJMRXSSZ30K-C48o27wXFYFYNlrIbPqcDh586OYXVmSEW5E1V0TSb1cydkRORUKb4InjfGDVopVeyQ-5n9Yyzp9p2lB1Dly3Hf1noBTU9C647GTpJDoA4UOv-rEJ_pezbuDdt81bGKjrtDBcdBGa_6CvMPCpr83Yu94uni62jVvmjJjYVfNYc3Es5KSRBa1_k47YUu7gD2TcPj5gv_Zf4ytkjlemwRUXahRrxbToHGes8aODtFKVN7qMO-m887JivIennb3R4QnEGFLXfM7m6JxkzTWZ3p4xuZdBdKozoxNSE0hX2gKdavDDFj-ctfVefQhtJjjfnZQZq8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زبان، از گفتن حرف دل قاصر بود...
◾️
هر کس، تکه‌ای از دلتنگی‌اش را با گچ بر دیوار سپرد؛ شاید نوشته‌ها، آنچه را اشک‌ها نتوانستند بگویند، روایت کنند. نماهایی از این روایت‌های دلنوشته در مصلای امام خمینی(ره) را ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/447754" target="_blank">📅 01:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OduDiyp_L5jZJF720nfVH-T7TCY6AQox9qYCysJRDtR5Gfg1TlAH33tXxMJ0F9RfG9EyhIdh4GR1kESmGmTE4ZPwJiQtR9rWFEOCEg7IKpFmLaiU5K1V9HPmEYwRM_j0S0nusfYq_FBA0tKTf71bHy3cYMvykLF-fObSCM96F9voBnou6VMMWDMVZwg8Rm6KNE9ne4FD0AT3fzN8OuBV7rGfzR6mbOP5Y9UqqXxBpu2Y5Ngt8NdGSXoF4u7fFLBx_nEBhkPANIjte_ZIk_INuLWKurhRq4QGOww7ylDHEhdBqQu2JTrpZ4vv8kggT9p1hheq8nkHREPn-efKRKjxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نمودار مراحل حذفی جام‌جهانی پس از صعود اسپانیا
@Sportfars</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/447753" target="_blank">📅 01:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de640b817.mp4?token=hxqIR9eqNaec6NurzNAawjKWrvWahlSQpzzwfvuQdHaezhFGyjwAOUQ_ODJHjghLZMhYKcarNLhpPazEO_oJBbf57XU1Nk-VJJPln1T5g8bJSbR4IJA9ryFyKnjsb9pIEalcIPrxoPNcH7sBSqBUnWhUykUdjxTaBn-kdOgPyXTF5qyzL8d0EjTVTkM74wxmE-1oZU_gTin6GP9nRkh2Hj972_oXwh2ep8Ctz9Hpj1ib-JVEJYkKdLtsIoj1EkikWCJKBRG7ZNYJdApZ3lRY5vpUYAvrt9OP06wS152Yi5jIs-gxPuH0C_2b1nH4RH8jdide6khcb4CIQbBGxBG5Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de640b817.mp4?token=hxqIR9eqNaec6NurzNAawjKWrvWahlSQpzzwfvuQdHaezhFGyjwAOUQ_ODJHjghLZMhYKcarNLhpPazEO_oJBbf57XU1Nk-VJJPln1T5g8bJSbR4IJA9ryFyKnjsb9pIEalcIPrxoPNcH7sBSqBUnWhUykUdjxTaBn-kdOgPyXTF5qyzL8d0EjTVTkM74wxmE-1oZU_gTin6GP9nRkh2Hj972_oXwh2ep8Ctz9Hpj1ib-JVEJYkKdLtsIoj1EkikWCJKBRG7ZNYJdApZ3lRY5vpUYAvrt9OP06wS152Yi5jIs-gxPuH0C_2b1nH4RH8jdide6khcb4CIQbBGxBG5Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم | لحظاتی قبل حرم حضرت معصومه(س) و شعار مردم با فریاد ای پسر فاطمه منتظر تو هستیم  @rahbari_plus</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/447752" target="_blank">📅 01:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jE9d3aYsnoOBwazn3E3ROahwqCKx_32tqfWfKcVJCF3C2_8egQY42TaQlmiHRnIInFe6ERGPZ9xxucGrzL4AoV6eL3nIBRhzoobNUnUijfvtGD-Hi83WkeZYD2sEyBeoZtdde3G3ENrybL_qcxmDZC-2tycOu9-6q0Vm9xn-P6vknPa1D5UmhcSyc3MT9KGiMwtksafVDmKG7XbxR49Fgpy2AESI5rXGJCv8wI0R13yr8BxnRzBFCcrWBsf_cynrD79rsjd-SN0N9tt6WWo5n-S3sk0i64VDzQFtnWzmf6-9jUxjK2nD4g86WJADmZXNJ00sqM2uVLQ2Umm9FN93tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
استانداری کربلا با عنوان
خیر مقدم به اولین زائر اربعین امسال
به پیشواز تشییع رهبر شهید انقلاب رفت.
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/447751" target="_blank">📅 01:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447750">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4598f64be3.mp4?token=eOV_qoBGKCDkAv2QNNg3Fd3tlkX4Jial2Uoq-DHLZngqini6EXZeyqP1ceOrbmpjHOTu56HsqT6J3ry7XLka79hvsoFq_AGlGFjXzBPggMjggLwYYQVGcs_M4lLW1Kt1YVZYCxZK3IZfxjOF8Fhvrym9rcDQ0PuqO6g_fYSmFwjQUzy7sQC9PQEyzGMDHX-J9DNOpXAibbbk5o5e1617YYqwa5hCqXIhN3XzCMRuipM1qVMQ3pSJt_lh15YEagY7MBXrHHk9IZRQA-MwQfFAgnGT4XOe0GZLB7ZeBxMtmGnnXrJdUqwF5iQNG6elc6xeMxJoPJPmFQiDJd7vZ1PX0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4598f64be3.mp4?token=eOV_qoBGKCDkAv2QNNg3Fd3tlkX4Jial2Uoq-DHLZngqini6EXZeyqP1ceOrbmpjHOTu56HsqT6J3ry7XLka79hvsoFq_AGlGFjXzBPggMjggLwYYQVGcs_M4lLW1Kt1YVZYCxZK3IZfxjOF8Fhvrym9rcDQ0PuqO6g_fYSmFwjQUzy7sQC9PQEyzGMDHX-J9DNOpXAibbbk5o5e1617YYqwa5hCqXIhN3XzCMRuipM1qVMQ3pSJt_lh15YEagY7MBXrHHk9IZRQA-MwQfFAgnGT4XOe0GZLB7ZeBxMtmGnnXrJdUqwF5iQNG6elc6xeMxJoPJPmFQiDJd7vZ1PX0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مسجد مقدس جمکران ساعاتی قبل از آغاز مراسم نماز و تشییع قائد شهید امت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/447750" target="_blank">📅 01:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edec66bb71.mp4?token=UGxQDHEd6jA5b4OiLwsEm59QsidRg_wtCgZY9_QHGiGcR8X63nzjKwcOO-I9j_QOWOjfSDC9eEXUGsZk8hZjyccpA02C0nhI775G455iKRvYe6dKGrRI0k2dksJIizDDA1ErXtB74DtAKgHm7rjUOyu2UtNP1YaRsZI-IGeRe2-pMxTa-bpixc_4X7yKIGO8rOdYYhP3p-hw2WBZzdexLk54qhg85nWMoLo53qqiMkxR5_mKMm1BivTNkYOWww1F26qMZ5yFcGEN1tv6ZHxGRLOBLfukWkQGrElHPsePyxwBlhw6g-cgZkAfEUWxL-dVptihYZ5vz7Ew7-qcngdtRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edec66bb71.mp4?token=UGxQDHEd6jA5b4OiLwsEm59QsidRg_wtCgZY9_QHGiGcR8X63nzjKwcOO-I9j_QOWOjfSDC9eEXUGsZk8hZjyccpA02C0nhI775G455iKRvYe6dKGrRI0k2dksJIizDDA1ErXtB74DtAKgHm7rjUOyu2UtNP1YaRsZI-IGeRe2-pMxTa-bpixc_4X7yKIGO8rOdYYhP3p-hw2WBZzdexLk54qhg85nWMoLo53qqiMkxR5_mKMm1BivTNkYOWww1F26qMZ5yFcGEN1tv6ZHxGRLOBLfukWkQGrElHPsePyxwBlhw6g-cgZkAfEUWxL-dVptihYZ5vz7Ew7-qcngdtRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج جهانی دلدادگان رهبر شهید در مسجد مقدس جمکران هر لحظه پرشمارتر می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/447749" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d73e666c.mp4?token=PtUqmKE5pgB5dLeWRv_X8vXUARjsICUsOTHm2UmlKMMSbeeacYxExtJDM4duIvL22FsKCdZwlKdv4SBpl3aMTd0N0frWVElZQCAdx3LQmL0BYxt5o7zuD73aIIyDOgDEhu_EZ77rsrMBrYmIxY6Fdra5uIHJ3kJPAsNy6idhWXumuzhXAzbYFmlJ64fQCJUlzljMbkILsMmovt2OpOjfrD3R8gnPFFyHVXvXHu_RVBmSFjHYWGHobV6oyfjhOzBRNed_HeqJNabGtQaW-rx31bIDJuZA_dBgUdu8Azs_vFRasoH4Vn-DRVNeWQuFE-Lcjmm2-DHNbglu8d7SeNLPmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d73e666c.mp4?token=PtUqmKE5pgB5dLeWRv_X8vXUARjsICUsOTHm2UmlKMMSbeeacYxExtJDM4duIvL22FsKCdZwlKdv4SBpl3aMTd0N0frWVElZQCAdx3LQmL0BYxt5o7zuD73aIIyDOgDEhu_EZ77rsrMBrYmIxY6Fdra5uIHJ3kJPAsNy6idhWXumuzhXAzbYFmlJ64fQCJUlzljMbkILsMmovt2OpOjfrD3R8gnPFFyHVXvXHu_RVBmSFjHYWGHobV6oyfjhOzBRNed_HeqJNabGtQaW-rx31bIDJuZA_dBgUdu8Azs_vFRasoH4Vn-DRVNeWQuFE-Lcjmm2-DHNbglu8d7SeNLPmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
لحظاتی قبل حرم حضرت معصومه(س) و شعار مردم با فریاد ای پسر فاطمه منتظر تو هستیم
@rahbari_plus</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/447748" target="_blank">📅 01:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705f58c0f6.mp4?token=Uh06a_9ZlPU-J3X0GzVYyzT9YGxR-UDuhQBv_Amya1OZ5bAYZIEQf9D3_fydgVq9ksxgFRuXhnFsRs2GCOpL6i2LNBD_E65wn1whonBcWzXa8J-6uz69cY44WT__10JFGU3qsSud2djsC6cCHAuW3j2XuhU0Yh4XM2L6StVjem_U2HtviiyyFAt0z-dQVJ6yqsQHWzHbGbliOX4t4S7RU2RfMdTkKaawsi9WQ6NCi6oIegVYvrO8bQLqJVo8oiUUNuHyA6sL4JwU4xU6hvBYEzBCag8Zj1T8opssUkmuOq119axjnrPTljYvqPs-jVp6X6whYHWahMLQdAEaUUTyVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705f58c0f6.mp4?token=Uh06a_9ZlPU-J3X0GzVYyzT9YGxR-UDuhQBv_Amya1OZ5bAYZIEQf9D3_fydgVq9ksxgFRuXhnFsRs2GCOpL6i2LNBD_E65wn1whonBcWzXa8J-6uz69cY44WT__10JFGU3qsSud2djsC6cCHAuW3j2XuhU0Yh4XM2L6StVjem_U2HtviiyyFAt0z-dQVJ6yqsQHWzHbGbliOX4t4S7RU2RfMdTkKaawsi9WQ6NCi6oIegVYvrO8bQLqJVo8oiUUNuHyA6sL4JwU4xU6hvBYEzBCag8Zj1T8opssUkmuOq119axjnrPTljYvqPs-jVp6X6whYHWahMLQdAEaUUTyVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از حضور مردم در مسجد جمکران، ساعاتی پیش از آغاز مراسم تشییع امام شهید  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/447747" target="_blank">📅 01:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2346d154fd.mp4?token=vZVsEABVce51RI9pqyqDIujijVN2T_RKVQ3W9GwWl_CWa8ghRSOgbsplzvUvqXqkS0gH-4jU0d_N-QdoeDR6SdJy-nKpyuzxhhQ5tAskjLz1QE83nm6SbgT3ICOAEIVPx7Un6MBp2IDP32e2qtpO2EKvtKFAA_aPoVKGxkDM5YhLvhBZ9PlfpKWsnA1D6GGDn4vs2gkbJwH4rwIHsDP7oVN0afMQLco5FOuqwuDrx_FlkcYB5hwBUf30z1RNH7YaNdMmvVvSVs8Wi4a4O4eYPzqgf0oVltk1f2quwvZq0k1alWeXPThtwfz27S_QPBVLpLkAqolV9A_BJtm3Sxo7QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2346d154fd.mp4?token=vZVsEABVce51RI9pqyqDIujijVN2T_RKVQ3W9GwWl_CWa8ghRSOgbsplzvUvqXqkS0gH-4jU0d_N-QdoeDR6SdJy-nKpyuzxhhQ5tAskjLz1QE83nm6SbgT3ICOAEIVPx7Un6MBp2IDP32e2qtpO2EKvtKFAA_aPoVKGxkDM5YhLvhBZ9PlfpKWsnA1D6GGDn4vs2gkbJwH4rwIHsDP7oVN0afMQLco5FOuqwuDrx_FlkcYB5hwBUf30z1RNH7YaNdMmvVvSVs8Wi4a4O4eYPzqgf0oVltk1f2quwvZq0k1alWeXPThtwfz27S_QPBVLpLkAqolV9A_BJtm3Sxo7QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ساعاتی پیش از آغاز مراسم اقامۀ نماز بر پیکر مطهر رهبر شهید، سیل مردم روانه سمت مسجد مقدس جمکران است.
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/447744" target="_blank">📅 01:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de20f9d08a.mp4?token=vFPtP2iPBhaWGjmvpx_k7fKuM5sSgU0ko9W2HjFMCAL3F081EXuhk9ksufy0Oq_bgONCIaLQznyynNWh5TZRMqUOAUQFm0g3MzwBXSFbN20nqwlLiyS7XgzrvjGKMJu_YJ1oneP_peyk2TOHsk-xGYd87GBaFtoduiB7pIGo48Soz4es0T22NLIcJOkj1I9KKpRcz2S9EbGjCj7_FtJq1GHRTA64X4QpSd-YktMvekqfLcQsGO5jou24Ci7lle9RUdZCo6oe0UabFv56GyBjY8FaI9lRG0V_79ghC0ICjYL4q18qjUz2kwHlZdaRNfkN_FDBOjeag9sYFnV4glxQiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de20f9d08a.mp4?token=vFPtP2iPBhaWGjmvpx_k7fKuM5sSgU0ko9W2HjFMCAL3F081EXuhk9ksufy0Oq_bgONCIaLQznyynNWh5TZRMqUOAUQFm0g3MzwBXSFbN20nqwlLiyS7XgzrvjGKMJu_YJ1oneP_peyk2TOHsk-xGYd87GBaFtoduiB7pIGo48Soz4es0T22NLIcJOkj1I9KKpRcz2S9EbGjCj7_FtJq1GHRTA64X4QpSd-YktMvekqfLcQsGO5jou24Ci7lle9RUdZCo6oe0UabFv56GyBjY8FaI9lRG0V_79ghC0ICjYL4q18qjUz2kwHlZdaRNfkN_FDBOjeag9sYFnV4glxQiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از حضور مردم در مسجد جمکران، ساعاتی پیش از آغاز مراسم تشییع امام شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/447743" target="_blank">📅 01:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be6e3ce38.mp4?token=omm6Tsn6Iy3Gcb65GePBKCdPFIoJGVLgiNPkoKRGuzjxCepiec_nF9K10CVhyaSoHx7ncW3_qADvCpQXP6fOZTxqhPAPDpwEJ0ya_ZU4_ODS902BB5qOm3VJjywA4-PAawDvdKezMSbJC9V-f_evKtZSOmi5xQ7w_m8mImOK2-Jz9MsNJByL8WAK8TStMX-Rv9is26VC1LMFKGzl2sqWabRztlw43Zmbc66GdXfF4q_QVc1GMX01i3k8X2ldmvfZ1adK6ippcdVez0HWPKP2L6StzgdY5RJ_Wrl32vRTHcuqXD1CyNHLmgtmZnjIUVKZQZmZS-36pz1KRmS_qPUfuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be6e3ce38.mp4?token=omm6Tsn6Iy3Gcb65GePBKCdPFIoJGVLgiNPkoKRGuzjxCepiec_nF9K10CVhyaSoHx7ncW3_qADvCpQXP6fOZTxqhPAPDpwEJ0ya_ZU4_ODS902BB5qOm3VJjywA4-PAawDvdKezMSbJC9V-f_evKtZSOmi5xQ7w_m8mImOK2-Jz9MsNJByL8WAK8TStMX-Rv9is26VC1LMFKGzl2sqWabRztlw43Zmbc66GdXfF4q_QVc1GMX01i3k8X2ldmvfZ1adK6ippcdVez0HWPKP2L6StzgdY5RJ_Wrl32vRTHcuqXD1CyNHLmgtmZnjIUVKZQZmZS-36pz1KRmS_qPUfuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت در مسیر منتهی به مسجد جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/447742" target="_blank">📅 01:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p48h0SsklRIKGxE19JOUR56caC0RxQs3acnewoJcGs5JU_imHo-2YMbt8VkKXwK8supk6IEGjObhprsN62GreDNbhu8x4qI-MUfDqoVYgS2WiH2KHsZ8-xHqSB1ln-hWKRJwQqteuINRD8ahAwlzJrAsLMBSFgNzFeA5UOMMm9ftfzEmGL9Cy0pH8ZSnlWtFBKBw1wb26PEZcniTLwZ1_TB8DRakZnTS2oLzPEkb0YV2bZqSjlJUsi-1C3AnVgAP-5E_p49xfyoQLBRLMX8wEj2S8854Y4YSnsYTwhf9liRUXv_7HCoZS0bTfjEg5rKm_hvot39CV659gubTy9B-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WcXZPDm7Ozfv9HWkXdgKOGVAT3eRBc345Oyl3P4onxLELlvlUgZa9FSbwjbJdgHl-f58R5n9paI7Jqd8-P6_cogkLcwZR254PJD-6HgyAlpRo31aqz2K2Jf7LKwppTooz8r2C5xwCsNjRl55SPlRfVkKcI07xFgEcAle_tKkxIhFXhqxbaXQ0DZzwR2oOeKNgS_rP00D_FfjCKGjDsvTc7NTd2bR9tl966L1o6ywzmzuSX1S3Ts6HjFmBHF1VsLT7Hcm_6qf5c3uVVqbv79ixfMHfFe41KflYBR6E71TNyWIBEQ6DbYVuWv2NnUpXhZmDOf7BnWN3K93gtbn-wdMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pfAABwvLl5DbbfsjiBRlWb_Uh-pBg2ZlpLxI0sarR_T7x7yujMZZLAoQQnkAkBNdNxSBcZqwoO0Jk5BwNGQySa668fQJHjHkxuiPpOXVz0jF8nxiMvBaj-VFznztA8j3SajeoQw_Q69CUweUPKYhOxlv0AteHuHm-mCJisFnXnm4xKQYMYROFYOq_9pRHX_ZVqZyJ6ZtwfGGnGcXRgUKTlnoEAkHOSggc7u9d6iQbT3kwZu90EnCM9IrJTa6HYUYiuO0U7hlXFLkgD6DsnwU2qG8LoJm8xNOQPh0ViE7MlJkprLPggBXYuuxOMMFE4_V9exXed5H70jsTH9hQ2YXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NulEDn0jEfZUuz7tbYRdbKuehp2lq_KXN5Mfvn_T2ClaO0bIrBpOYniv_TM33ZMlvFCT28l3ATQUCTS4FHN9oXICm-ldxOeeecL3tdYHJgNS9sMds91Yk1OUww4QKcBeEoIcwq8BiwkScilOS9copt8HEGsI5Iy4P4Mvtb5671pAL27DoAeB1Jm9oWPqZBKQoOpCUJfH_7pQmmfHQAoxv3xQBS34wjLn69dpF7xizL8lm773YLuPZpkaPmR9ZFgPqOhTBmviigQBHnAc5tKUauzOXJV2U4Cx7oeCMov937tNZ1d4DxLwYebOK7L8QNQ2xKBG9fnhvtWbExyygAGWmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۱۶ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/447738" target="_blank">📅 01:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447728">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GwUuBY3ddvD0wcaBCpNojNyycup3384OaZoOtSt3NLyu7O0vXigVQ-QpgN9UW3z07O0X9HNOimQ7mvoJjeHHUa6gPWuUKekYPESKjCnzaYP5R7y5srFxBfkpMDzTD9iKb1zKCdrmclGD9a3nkrAWW3iNSPpFVrtCA4sjg9thND1Vbg2lAbbmSyq-TDZSTGNs88TD8JCvzqzoid8wvQUkfs9x5kdMB0gYQpNmUOhjhxx73UEoxJYixmQ7_-q6vYdDsl6_Xd6GdZVntkjWPC1Z0bLMS4qg-ZQMj6hrI0OQqgSkjxSCzoGOgprEMxKgIrQH7RYceeGhn58fpt5T1qqHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vS606CWzhtUCb_48Qgj9enIcl-MZtcagkkEkZiQQ21bH_pwLMUpQuGvgDCcH8Ktk01lDIfK60eHiY8pG4sNA5MYeJagJJscOcGt7-Q-iJaumwUa0R_x6Hkd1T3nLbeoHygzUsz8WknebNDe0eJyJ9bP7EhG66cn2jrNjrpcz-74CnACoYHkztD0cx7DPqqkajwfot3Rcw2ETiEDUwf1k2928P_6PePIpUGrG3Fs__qwZ9O_lyggDhZzeSw_Oa47Eoc9FkR73mBjGJ_vCGP72vPImv86LIhbwfDsqQX94_nmJuGc99IF3V49iZsP5dHXUSfCPsx44d5lTSaAO-RkR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-vcZWDTZ4IE6SBWyaCIwMCnCum-0qTG2veZ5wkAiVVHlAp3B_G2YtAWPGxdzQ5SKt_eZ536DHlsbt_8WDOIHdZd_xU3F6CqQzxWVBjrtNsrdRBURUZY6ZwUet_Y2aH38Np5gyV7wnF5G7wHM8VzX9nlSqzDJI_owvGrZ_vB8wmJtDplc3j44QhW0jCTGJRUs9-yHhG0t_Wpb8ZXQ1VjzZcfx_BCoNBJwRhXhDw_VyZClIQ_lxk-O2sx8dMDKqYMm05lAgHN_Ogv96pVWHpNXNfl_PlI0xbjUO_l2xbfAcYwbIE8jb7qaBvfDJItjGCfN2Wu_ZVxKRW7Z2HjVI_jCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lQ7bvTI2EmF57X3ZtbYy589YmPhGokyJO3Ty-aM-DIxF6OAe31bWSd0lr-AAbxqRtw9vsfVlereSrznRzqIKIrSOKuOszT-DL3Umitey0sb8drcxHlITrMLriqAhT6KWqCVntysa-L3J7RBh5sqSsGL_FKb7zDSNAueeKf6TePm_ESBd3fjx9HY2RG7gFZOr6AUdZyl3jfnayCgbyvQRXSIIyUyi840bPGoyOv3vRa7xKhCie5fZpytqu4691wS9IsGMMNXxEyRgUpphYLOBvG04q81NClqDtCTXelhFobtyiSLwUXAJyVtP2v_fXGk53i1OtVJ2WKp4g_c_fRBZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoxzLU9mwIPzlvaPvmi_vAynq-7FWm20sYMK9Rexr1QbvCmvkRNR661baKnrE_rVsmCzJQo_I9NqAoxseUcTfDqI7P1RnkiEbwgDL4pi4fxvH0uSjBctOPcDyZz66BYunFxza2X9HquiQ4b7UD_zXLprzpaNW_zUuzkuSNo1MHXJm0DuJJC1kzxjYwPQrwvr_ukByAbXVUyczqyi6_QsEWqnOb_q7pofGaA6kx9AK6gKNVkKrZd55G0S6vPHEk5qT3-Tkslwebnp-Wfajbo2htVJFU5RGqmwteMCzLGX2LBGMTPG5CX32k8Je7XIQyIMqSO_sk_q2LY-WouHyM00XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kx9oEIYdF9KJPBlZVDUdImkyrF0X1K9c3ZCBBWPJvP6A8oUsOzfVV949jSubteSDVbW-xIbLjetDdVQF9bhYqNwoeVKl9uD91-eX2MZ0efXuZjD5qZopz2Zltg70mF_AHleuo6ObRk0_xsavCxf0mUWZJYHd98uHYwpdTZAPiLi7G-TkjssSYM4wGtPqG65deZUAeQb-0oIyXv-ttBBOXH1OpK7fz2SBzbzwDZOvwvbgSQ9Iv9rQzMJc3l20kiDYgIy2OXQE05tZb75iVra-HY_rhWDFOGuHVGWm0_PwNALjlHwEBRT1kH8ZuyF7dwHFq-wIuAjBI71F_CIzzn9-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QOv4cZ1zIAn3KN9YPp-_G_CM56jDdPdpiYRy9jv_siFX5qE1PNztoLae_RP7iqoRBH8qy-kZpNuWZlMsGNi23E-hd9gmm89p-y_FxrMp3QaYYY500V1hmryCYu6fEODlydnKXpDIdYY57LjVU5Zv7n5jlFSVgAOiZ1dvi9W8OC4_ZkrQvqT0kfrD5VwEkGbMrrCuOnwLFNKf6EfC7m1dD36fvvWYyUWkDrLV0UUq-yrqFab5jQ0iRUr1uvZR_maxjK28JNAhhDx8RoOHOaEC0wWZdkuOWtTsvITzWInnvJaJhXCIgo43Z0mtRk8t568fxsa7cXJSQ1lUgtg_Zbz4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwa4Vvpq8Ti4HtpVYcxmUHJQMy9HJ1svUmfbwjdRPXANiIJ-KBeKz4cUvaFfrUKOaQ7OykWzE_mf3qeopmEPVNd6i3h9ghBlCOvqOBxk4Eql9mI1zPaTHuCU-KD5Zk26rkgX4XsA0g6ilSQG_X3y1zi7p1OX6Fje-i3bckfXNOMjlEbkaHGFGhV5jsXMrxSDlXiBpeITdQ3fIqm2waPoMqjBmp8vMg9IqDfs1l_81ViJNUy1k9LONrur03TFHt1BvIbN00EyjF7CRoIYoDhCCyNaFcRiBqcwJJeqxVmiUt6in8iZXZAuRE9aOEkGgT-TUUAb19Rtb42l2O2Q3WgpUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icdUn6-Z0R-w2irvAew4f6p846X7TvEVz0uzGjvS3xEpkoUEGVeCvTradKGP2wubbOL2hEXo95tTxqUIuknzCetpCm9K3pDsqlwz0cJw_oQ2n8jyrzIo2ULNwqsBpGqfbXjHzoGzbjzPZzEsOZx4jMQwUNV0PjGfL9d3RcmsR1l-UeTUBmmUo4E59YpK-AZanQ39o-gx7qWs2U1uvdVWPm-ou4dHZtDiO8RYKOtotgBD-9FEuA-57Ttx47pfEvth80kqWGXv3GXs0vQrN6kiT5TbsdQbX5s99ycVNDXSPFLjg_ZLUiwX0an4ye_xJ75AGOlQ-hmT_2ojYZU-CYTC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnde7_VrF_fjt02MkJfHmYZSPm4msfZpOdtlSY0RIuhZhfcN-MELo7aS7GY10SX1H0-ciUCSdctXl6PTANhYB-SEmoc92REdbRfz8LwSSdyRxhqO1RTu2vG6H7Ew3CvxWs1BX1cC3Ao5JoccaKRBJmuevay5O1L1divStma1kPoXKDY7QFkVndaMUJjuot9qpaLBXZW4XxFTBXLTQIpB5GOOiB7CfsoOW_2hWNdbfQWp1QwxZf7DQDezy3vkYOWb6Cm4k59daZTX0pwGZ41LgXrLSZ3uP5SozFJMcLAiIfySqzczm_AQ8SuLMks-CT1S8o8JaNbwcHvHD0S3j9zMbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/farsna/447728" target="_blank">📅 01:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447727">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdRdy7UAylsgedBtJFchDKj0w0yRButWQK711DNs4VJQ1SSqjDH-kk29lp1omIAjnV9GZr898MrrBjmntZho4Bfj1oYnYYflWFLRRo6yAZJNJWMeEcJd_RRt_Tz2OtjgxiXyBYR-EtpNA0LsLo_TkcttAv3L2y5bKoi_uWcT2Nt5MwVCzDjw2WcvqNTIJM-_DnzZzDkMG8YF2mgc6oXOjWG5VTcizEXrHrCFNPclx4GyLF_XJTCKyjHDlYbfGzGXYohRVQxQKLK1woCbtAlkWXI_j-lOR8o1adJwL3-8HFpNeUagilcc-0YuEBa_NLNMl_dPrt3PuTyyzo5mHwv7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام تشکر و قدردانی مسئول ستاد وداع، نماز و تشییع پیکر مطهر رهبر شهید در تهران از مردم ایران
🔹
سردار حسن حسن‌زاده، مسئول ستاد وداع، نماز و تشییع پیکر مطهر رهبر شهید در تهران در پیامی ضمن تشکر از خلق حماسه مردم در بدرقه آقای شهید ایران، نوشت: جلوه‌های اندوه، خشم، حماسه و خونخواهی مردم ایران در روزهای ۱۳، ۱۴ و ۱۵ تیر ماه در تاریخ جهان اسلام ماندگار شد.
🔹
قدردانی از این وفاداری و ولایت مداری ملت عزیز و بزرگ را وظیفه خود می‌دانم گرچه پاداش این حماسه‌سازی تنها نگاه و عنایات حضرت حجت بن الحسن عجل الله تعالی فرجه الشریف است که صاحب اصلی این عزا هستند.
🔹
اینجانب به نمایندگی از همه دست‌اندرکاران و تصمیم گیران برگزاری این مراسم از همکاری و مشارکت مردم در برگزاری این ابر رویداد تاریخ معاصر ایران که نقطه عطف گام دوم انقلاب و شکست توطئه‌های دشمن است تشکر کرده و از صبوری و تحمل آنها در قبال اقداماتی که صرفاً به دلیل اولویت قرار دادن سلامت و امنیت زائرین بوده، قدردانی می‌کنم.
🔹
همچنین از همه دست‌اندرکاران و عوامل اجرایی و خادمان این مراسم عظیم که ابعاد بی‌نظیر اجرایی آن در آینده به ساحت ملت عرضه خواهد شد تشکر می‌کنم.
🔹
برگزاری چهار مراسم مستقل استثنایی از جمله میزبانی از هیئت‌های سران جهان، مراسم وداع و نماز تاریخی در مصلی بزرگ تهران و تشییع بی‌بدیل پیکر مطهر آقای شهید ایران و خانواده ایشان، جز با تلاش‌های شبانه روزی همه مردم و مسئولان میسر نبود.
🔹
امید است همۀ ما مشمول توجهات و عنایات ذوات مقدسه حضرات معصومین(ع) و شفاعت امام شهيدمان قرار بگیریم.
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/447727" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447726">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a074d8b52.mp4?token=ndZzYg2ulpnApJ7Rd0M13LWJC2ylj5CbVIfsWzItVSaE-Ga65s-mLUzl8aSSGhSzpBTiJz_meW4eo4hDyYrDG0P2r6EgwjTlldwjDvVjQOJhPmrlPiifiR8lYdhaf9IjLGsVEkd66jcqvREi7iiOaIEaWMvmMaVtKADIqf9YCOP6bBz9_4zF8x0D9ueCRtCw0oMaULGcGx4wvzEBt_rEbzlIJBTzt2bjBDFicZHYDc1SZozYuAoOS63GFYmwTckh5uEmJtJHfdxCMbZH4O0ByKjpoIsHC8t4Yz9W4oSPTvcHpejaCGMwU2e9fOuclsQTBt2SsNM1PGqv3UP45h7Bhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a074d8b52.mp4?token=ndZzYg2ulpnApJ7Rd0M13LWJC2ylj5CbVIfsWzItVSaE-Ga65s-mLUzl8aSSGhSzpBTiJz_meW4eo4hDyYrDG0P2r6EgwjTlldwjDvVjQOJhPmrlPiifiR8lYdhaf9IjLGsVEkd66jcqvREi7iiOaIEaWMvmMaVtKADIqf9YCOP6bBz9_4zF8x0D9ueCRtCw0oMaULGcGx4wvzEBt_rEbzlIJBTzt2bjBDFicZHYDc1SZozYuAoOS63GFYmwTckh5uEmJtJHfdxCMbZH4O0ByKjpoIsHC8t4Yz9W4oSPTvcHpejaCGMwU2e9fOuclsQTBt2SsNM1PGqv3UP45h7Bhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمای هوایی از مسجد مقدس جمکران، ساعاتی پیش از مراسم اقامۀ نماز بر پیکر مطهر رهبر شهید انقلاب و خانوادۀ شهیدشان
@Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/447726" target="_blank">📅 00:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447725">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxEUe8kpWR3akSeZjMr4LWPTvZGjaNSeAO_Efpt0QF7Fa3lCiPjNKrv2nzdo2jbI7Q5owFm6hwZLtmx9RRElx6YCnDqH6_Et9xOqnDdXOift_4sd6RDWO699EDmqfDCS-UfuV2iGevPPVfwbM851K0iJxK31V8uaDTBsDqrJJZjwXO61qb04tk4PHDPZvD4djBvIVIN9j4ltUnoLvKWKi1xq96HjCbCvHbkXoFuOMhCoMH4scFCXY4YSAOsNHOhr4Fii5pxG0G9bweoZZwpY-36MeM5q15ty3kiSvF2-bFV2N6K7ipfHIQ7pChJTwVH_IxnnEarcNIbQ653QI0mrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: لفاظی‌های وزیر خارجۀ آلمان علیه ایران، فرار رو به جلو و تلاش برای وارونه نشان‌دادن واقعیت‌ها است
🔹
سخنگوی وزارت خارجه: لفاظی‌های وزیر خارجۀ آلمان راجع به تنگۀ هرمز شرم‌آور است و از حیث وارونه‌نشان دادن ماجرا و بازی با کلمات، شخصیت «مفیستوفلس» نمایشنامۀ فاوست گوته را در ذهن تداعی می‌کند.
🔹
آلمان باید به‌طور کامل به‌خاطر همدستی‌اش در تجاوز نظامی علیه ایران پاسخگو باشد و غرامت مترتب بر اقدامات غیرقانونی و مجرمانه‌اش را بپردازد.
🔹
این نوع دست پیش‌گرفتن‌ها نمی‌تواند رژیم حاکم بر برلین را از مسئولیتش به‌خاطر مشارکت در یک جنگ غیرقانونی و جنایات جنگی ارتکابی علیه ایرانیان، مبرا کند.
🔸
وزیر خارجۀ آلمان روز گذشته در ادعایی گفته بود جمهوری اسلامی ایران باید هزینۀ پاکسازی مین‌ها در تنگۀ هرمز را تقبل کند!
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/447725" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447724">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e31d74c9f.mp4?token=NPieSdHPRt4QK7AAM4ymUjt1Ffb5A8W8YMLYwkdKgGt_IMdeGGme--fDFLQbjWNW1caj3SiBi37Z6cu4omRDxLjKkVaKvhjA7dGA7wpfzO0BFQ4AvSl2Ek_eNiJCO25YT2EPSKvEkiz8hiEoF-Qtuf6aMuA9lv89_LtgB_BXikQWsPcAlgQJA0YmT5jZj9awU4ASziJfdTiUUbunI8KTzYoNqe5AFvXTQUhdBdgXIYlfoKE2nEH7G_gaf1xuXJIj59OryhmMl0EuoDX8jwXN14GSVGWu6NtGh7SsUiYf9OqS99Ptg-l-VKyFsMRerMabAqOX7p8O6i6ddEts38RUxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e31d74c9f.mp4?token=NPieSdHPRt4QK7AAM4ymUjt1Ffb5A8W8YMLYwkdKgGt_IMdeGGme--fDFLQbjWNW1caj3SiBi37Z6cu4omRDxLjKkVaKvhjA7dGA7wpfzO0BFQ4AvSl2Ek_eNiJCO25YT2EPSKvEkiz8hiEoF-Qtuf6aMuA9lv89_LtgB_BXikQWsPcAlgQJA0YmT5jZj9awU4ASziJfdTiUUbunI8KTzYoNqe5AFvXTQUhdBdgXIYlfoKE2nEH7G_gaf1xuXJIj59OryhmMl0EuoDX8jwXN14GSVGWu6NtGh7SsUiYf9OqS99Ptg-l-VKyFsMRerMabAqOX7p8O6i6ddEts38RUxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این خانه میزبان شماست
◾️
طریق‌المهدی آمادۀ میزبانی از زائران و عزاداران امام شهید است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/447724" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447723">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d88011533.mp4?token=Qkkxm8rveFwyn7HsHwsQwOij3QGK8E_ufDhdPo9mzrTmAXU4b2HlRRLmIaAh75ZpnW7aBPiK8A7lL6BPvOy5c2qsS58l648ATmYY9GD735-Os8ifA-A_B4_EsGku-wseVxnSGUbM8g82cRZtYR-AqmaOghcLTrfVx0vspV8nHH3Skh7_aMJ3ZYTnxNeuAkrakxzWY5wK45_XmCJb3QXeek3UpGK4qZtaKHLDHrik2Vg7PPK6XWkqtxT3Hg28J1pz9jxKGapdiSM4P71Psm-_kgHd3svu_N7zOSLnHUl4CK9djTmxk0atV9ZBWY_GLdjNAe_AZ_VjqyuaV2Hz437jTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d88011533.mp4?token=Qkkxm8rveFwyn7HsHwsQwOij3QGK8E_ufDhdPo9mzrTmAXU4b2HlRRLmIaAh75ZpnW7aBPiK8A7lL6BPvOy5c2qsS58l648ATmYY9GD735-Os8ifA-A_B4_EsGku-wseVxnSGUbM8g82cRZtYR-AqmaOghcLTrfVx0vspV8nHH3Skh7_aMJ3ZYTnxNeuAkrakxzWY5wK45_XmCJb3QXeek3UpGK4qZtaKHLDHrik2Vg7PPK6XWkqtxT3Hg28J1pz9jxKGapdiSM4P71Psm-_kgHd3svu_N7zOSLnHUl4CK9djTmxk0atV9ZBWY_GLdjNAe_AZ_VjqyuaV2Hz437jTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌های سرخ انتقام یالثارات الحسین(ع) در مسجد مقدس جمکران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/447723" target="_blank">📅 00:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447722">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pednNIMIeH_oJy0Fpn4EYORAOyErhMWCR-ibGjj49ZLKzlvhmdnGXESD_i6DlF3OA3q0uHfeQHFEKQbsA9THlDflYqtBWEcXkFl23KU_nEazGPgBWcSBq2bO9NQAEH4W49osdw0RHSmGYDypV4ajtu5q9NvAE5WrB45z0kBx8Yp_7uxST0mvP2ZNRapS69dynzCigv-vYN_P-Ntt7kh2R0VeudaiEO6U57BXOGp5wzLxnyGFohDK07QFKCJ3mlDaYuKwbRmpTTOOfJ86kWIsHpFyL7xWC16pvXRshcB7mZIG-cE-Dd03bTpqEPnKX4q4FNx1kY9M8n3D83M8rcxDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکانس آخر رونالدو غم‌انگیز تمام شد
پایان رویای جام‌جهانی برای CR7
مرینو از نیمکت آمد و دقیقۀ ۹۰ گل‌ زد
⚽️
پرتغال ۰ - ۱ اسپانیا
@Sportfars</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/447722" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447721">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8180ac8e2.mp4?token=o_DMb37GPgqNogObrjhmgxWrWmaPj9Y8YK7edlNcVmkZDDAocPU6yf602bG8LHAhDBXdDmDoA4O6a6J90l3qY7TPHfYILnvMTmy2Kb0SznN6TJTX97yOrM-BvinhdkO6j5zyF95e2Z4PSPdpaA4BCEmn8O9bG4Mpejzhj-lk2_IBX8YiY9-i9ur8WE-TgTPvVsWXh7dnFgefxuIENnEqGqhq_YuVsy8zJSM6doeAzeJpJpbhswQZNR6Kedi-WU1DcuXs81-5us56EFo_xFnCFnKsccD1yqbqwSIJZJNS21Z27nDN7-sTLMcRqQbWa3pwLL_N70dDLi4wk6qd5Myh8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8180ac8e2.mp4?token=o_DMb37GPgqNogObrjhmgxWrWmaPj9Y8YK7edlNcVmkZDDAocPU6yf602bG8LHAhDBXdDmDoA4O6a6J90l3qY7TPHfYILnvMTmy2Kb0SznN6TJTX97yOrM-BvinhdkO6j5zyF95e2Z4PSPdpaA4BCEmn8O9bG4Mpejzhj-lk2_IBX8YiY9-i9ur8WE-TgTPvVsWXh7dnFgefxuIENnEqGqhq_YuVsy8zJSM6doeAzeJpJpbhswQZNR6Kedi-WU1DcuXs81-5us56EFo_xFnCFnKsccD1yqbqwSIJZJNS21Z27nDN7-sTLMcRqQbWa3pwLL_N70dDLi4wk6qd5Myh8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسجد مقدس جمکران در آستانۀ تکمیل ظرفیت
🔹
خیل عاشقان رهبر شهید انقلاب خود را برای شرکت در مراسم تشییع به مسجد جمکران رساندند و علی‌رغم اینکه هنوز ساعت‌ها تا شروع مراسم تشییع باقی مانده، صحن این مکان مقدس مملو از جمعیت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/447721" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447720">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2015a46b7e.mp4?token=G6rTIvUTekO3j1U8ZsIs-umHLkUiDZxBVdo37emXJ50UOCVOj__5yVTcqlWUhrf7wEPFMGAuYY0Pr15uMRUc4qnVtD-1sLwiVFM-tALrZMFisYMDmmMsJrN2Hs2CVF9oTIKdu4UxDbtLRY6dfXzxMOnsIYXVY9SUWcJnRJ1aVCf7m1wyvS9aXEv208oAjqE8zpTWfSqYvVxP8pzUHrPzXIsR8kfyLG-7q37MqBY1DYm4l6Unre9cgJlZ8H3fOtyw8ou8y2zGVPXaDGmjMOeN53DgJMvLFAxEcQN_t06be8bn2vxswANsOfqfz7vh6EHxzI9-YcsjXxjmyeSZD_d_pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2015a46b7e.mp4?token=G6rTIvUTekO3j1U8ZsIs-umHLkUiDZxBVdo37emXJ50UOCVOj__5yVTcqlWUhrf7wEPFMGAuYY0Pr15uMRUc4qnVtD-1sLwiVFM-tALrZMFisYMDmmMsJrN2Hs2CVF9oTIKdu4UxDbtLRY6dfXzxMOnsIYXVY9SUWcJnRJ1aVCf7m1wyvS9aXEv208oAjqE8zpTWfSqYvVxP8pzUHrPzXIsR8kfyLG-7q37MqBY1DYm4l6Unre9cgJlZ8H3fOtyw8ou8y2zGVPXaDGmjMOeN53DgJMvLFAxEcQN_t06be8bn2vxswANsOfqfz7vh6EHxzI9-YcsjXxjmyeSZD_d_pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب انتظار در جمکران
◾️
هنوز ساعت‌ها تا آغاز مراسم تشییع آقای شهید باقی مانده است؛ اما شب در مسجد جمکران رنگ دیگری دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/447720" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447719">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76860b664.mp4?token=R86EmahZdQ88lTtDFeq3M96qDmH64PHXjanm5a8S1yjRn7Ut9ixAIowXDfb5dpqrkKXEjBJ6mGZNmMYj3Xwt9jFmYIOKDVNANQRz5RC7CIeVRuPmOf_Su7flMeKQEWENIVlMx8Kco7aEn5Pj-s14C1kNQh8PVBMql3qqPBVjS5ZFROib3QXzAbcN_pC_0hNq76Ty05NGhIuxDEGhBPzUxVxOleA4tGWpsvoZcHQoNQCZU6dsi4PrzAznqbOVAJqQoVt7EyEghA4TvmYYbAmuHJ7O-m6nk9c-2UV94Iib_63xeXWTICZpLHDmhPm7z4jZpXeULjzBILQhFm3Puoec5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76860b664.mp4?token=R86EmahZdQ88lTtDFeq3M96qDmH64PHXjanm5a8S1yjRn7Ut9ixAIowXDfb5dpqrkKXEjBJ6mGZNmMYj3Xwt9jFmYIOKDVNANQRz5RC7CIeVRuPmOf_Su7flMeKQEWENIVlMx8Kco7aEn5Pj-s14C1kNQh8PVBMql3qqPBVjS5ZFROib3QXzAbcN_pC_0hNq76Ty05NGhIuxDEGhBPzUxVxOleA4tGWpsvoZcHQoNQCZU6dsi4PrzAznqbOVAJqQoVt7EyEghA4TvmYYbAmuHJ7O-m6nk9c-2UV94Iib_63xeXWTICZpLHDmhPm7z4jZpXeULjzBILQhFm3Puoec5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
حضور عاشقان امام مجاهد شهید در مسجد جمکران، ساعاتی پیش از مراسم اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان
#باید_برخاست
@rahbari_plus</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/447719" target="_blank">📅 00:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447709">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwnxHlYxq_H-gJpBKbQw7tkeGeqoijIODxI6zQs7IFcD3AEkww3VxOtV-fzOnyb2p10fc1K57iOqypkEillt9oakc-DGv5Jpb2VJ4PW0RhRibNuMiCr_CvtJKSaFpfoHBIfFm9rJUzUGAlYCdlyr7wbQqgaCMvNj7aWAxgeKIi50RJga6b78cjSgM-YvmDWcS0swfJ0Qyx36ZbBvTD98vTJ5LhEHwQxOq0VeQh8tpdmHO3hM73JymQElC1vV79PJt_HmwRFEJ-dSxDwNqSv5xo4VOHuySdabFrtDMciDY93Ymy6-XKU30oKbwN4gjJvA5hlF0pK_DLOeLdfGZn-QWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l98NzqQq1pN5XQeE7PMSICDHxbdDMS1WyaLZ7WmGjTWeErbsPjotH9orZd1wgedaNoxXVICPX-CXmHffucrDqjY5K0s_fk2yy21d8-r7PepDva4-pG3Mze976LMd8t8AyA8K_L7yUl8r0q3wqKst4jPcX4o1FO3jb_cvEAxsMZnG3emCoQ9XNcwTfTXTA6SkMcB7p8b5xGwTQegp_9utRWYVf3A2EjQcsGJSyh-ZH7fAp5vPcFetEYIEAvKd49_EgH_nvvhMhfCnw5HMV633-j_EZeqqYI1crHZG07Vf3jcqhuDa9LXG77MXAcVYl4_c9H7vj6WbY0IJmzIKI34AMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atpnZsUY6U9S6dxGaG5kICQkhPlR5jh7KsSWV9BR9GSDVvZ3kjvN0AGSUvdX_kfmXUQKoNObQ3tjnLo_aXHKwjWYh9TXFOddTP0l62NVydz-hN-QpPKUoW_CrWKI6ikd5gpdABuooq7KvwYRvb9nnBxK8d-GuutBgdoAV5aYkDhrToF3dxNF1z3lRdpNMIhIenoAeHZOFZeY_plRwytFrVbM8A-dNWbHSsaeXN0Ahv23VJogZV5y21wzU6WmbDiVucDhWt3jA8WnbnsnOmjvNK8EDPfDjqh3DAO_ShYAJ_hswGyHgFuk37CoFxYIGUleiVP6TKetG9dRxzZAbNFZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOXHHKRhlk0aVq7ryPnt2CdZGxxFpbfDa0uenJPH_fHFkNk_E-oExDiXMsqaVdKCnKuUt6hfIvHdwb8fomT8ycglya-JVQhkkeX_emWnBzisZGVAcjcTc_VaJ7XjF8ryHoVWl4DjM-lwT2tgmNTiPQYZd98EMpwDW3y86HZsCYOUgWDLgg91ZykufO1RVbs9rDhWsLaFFZ9Dzdvea8qRtdBNhSqqgxSLwHQkBZcZrbrQbWBr9RBwBkTrJyt3d_Fj6gOrLPvgRJ1PXdgG7ZQ2owMZlhrDz3kWk7Mh7Cq6xWUHERYVholI6aZDdwCWRX8J5OcfmxTQaUVlG5cVnjFgkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHa31FneFzJLd1ZJYlqn04huBBRF0EYwjwcZ3mV-BRjQQA8tMLT20htlQsttZyi2xAB1j1TQGpdHfnZ-5x4WU70mfIeYY5dF4IE7SMVJNylkaCSv2_MPo1Ehx5RkByVOKiMnSQwAeDqErN8TWC2E8Kl6nYdzLZD2j7_SCsYaZlMJ6fg1RUTmk-4mbNCqeT-Oh2qLXQmo4HdMC9z3pTta6XWr5N_bS4-1le6ElE0zg6lQya73E_OGTxryvLG9ziX1w2RkTDw9wXaJLW_4LYZqhzrKLUtcCtBCvvM5VZczFADbhN1NSgILBGy37N0R6tU9RlO3xcWcnEpWChAmd85CTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MSONQvr7zYsg3s3354r6MQV6C8PZgOHjhRKBuL_N617Jxp9fK7X2JXQGCFSG8ZUQQYAuP7k2wo1a5aI68GFt6fwgI0ZFw11bQW1KWpYynjTf9aEDwnfyDI6PXPhEVYpEVBspLfNCouR5cWnbLZyWUnCFlz469ZhIUvudha3oXSb5xikV87aZYnW4qVSJAy1oPZkNpt7HEirsJODK1khdNEIt-_Q3Sl9zEJyf5_mrN6gpNFp9u2d2Fz4lHkOesUh0MfNLC6kwrIzGEWVfiGW5MamCV8-MqFCHI-3eNru_j_OKLv48A3mR4y5vat4jDmTkIBiEwhmJKAUSJWgizsVLmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqpcyO6pqlfLXEKKIGoda7c1xRF_AW0qRHCzZ0886aAtcrzuuEp3zrCNPHFajCpycopsZmget1rWSkbr7hktEPnGxI1jlQN8RJ2k1WmqQYiSUvbvfSaQx1Y_YUcl3C5LXdpFcgTdHOmo72yGdUo9_UawqChRkTzVn02I3HHHP6PC-bmVzrlF4HRetJycD8aFk_ysKF0aLsOSbDYvoQt_h4ADapXyXbWzmBCy5QM11hUdK9zMg2IdTlHV9PBw2vQUBkCWTsgjWvgxG5avMNLKrsEUE2S_sdNHqu9YS2u_uGPMHRImjoG5kyjE2epV2NoFOnHKpLZIm-bY9xsyrZJHXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHXYEf10jE09WabHfBoC4OaktEzrLqVQSIan6L1jGUzgvWtPpqevgh5jXI4yVw1-HeJOmLI2mfkRv3Mnu0oLM3vZGvYVc3Wd0vdYI-PEDNwaiX1_vwHVWIvkGDN64jveVLLoDNp0L1DMMinvU0dcLIsN-YHAK9duaV-i7lPQ7xku9nqJnqhMmbPhUA2odbFL0o1tyvPW1M4cMEn5shAZizY3hNymoaE9Xsame2UrO4H5Q6wZ_gaIcgxgwmgMdv57lzj8Bwd8k8mHUSQRtw2B9PyvRpGEAD3FZHg-Nk6G26YxM5TvxRyWRohx7x_ob-B0SOwA2w9VzMtBZuXiGz8DCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/deitNNG_zGcjb396_rkTaE9-ivMyeBI_Fh9OnFM0VQ3aNALSkmG-I9_4Rujfz8ybE8zxwdY23s5TmgkHahnz1_Co-3sCS5ji4KAsHtGV0Hn0ksQhqUAD8Sda86fp4tvf1BFjlGCa1kONb__F5Ua3cx73TpFUnMEqG7H3OnRDSNIIRVOu-65oMC6AANZodOmE5LnClmopncJgCShLPLm6m1zTntS3Xo5TdY4gl668LUB6UP0FPjFTVIopqjyiFL_u-tF1ell9oSKMH5k63Rcm_HZiv4i_Ut6TnTn_LyuWft-TrDWf2SsszSI6HRBBLWuAs4rKlsIPvDFRbQO-ZGYXrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vrSpwjN2m4b01vmXLdq0nf2I24tYD7r1qbhoSjPntWjSdrM7gTRmvsQfXQbFx_Wy-3aEc26c6p4t0BSh4sC37ABergeVleKNKNIBG0aWeQOgO5wi3Hgkp2Qklq0nv8Eawb3sbX5hk2ftgxdia4PuuTYEcEFl2wyW-zMaiRN5jbBSu6pXF7ql_Qa7xTH18czTpPaBXagITPQcMljeef4ULFJxw8jLGLXErlGqTbsE6WaSiN8GQgY6MgXA7A_eRDdtOfhqUe8raOXd0T8yzb9VC6l6dwEnvZsPMQxrJc8hyElUeZqAa8_dohijXv2Rx9O8p782zZyTO9xRykFea8mUUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای اربعینی مواکب قم، در شب میزبانی از عزاداران امام شهید
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/447709" target="_blank">📅 00:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447708">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc10d9e65.mp4?token=vCrGLplFBMoHdmji_A6EEtzlf5f7UzV_RPcctdT8jUvtCO4gPaqphx8meo1XMGKb9yvi3wIo6Wh29g2rVLBoe0tGWtjqUmTjEHW-7O37W3VSvz2xdwdsODWSsp-HPpUKj8NRzwoZlFA85UeRtd4LnBELQoIFhPWdUGZz3ZmravP3nqhqEQfNvmfy61EED9_z-91Lakzpc0Ouos-ydHNj0SaJvHNocz8maT6xtegymAoy-QmwiQdJiUnVpPwFuwicKdI_jqorMUHhWJh9ZBO7jDMK4Uyo5oMm0mmFkwVtsB7r9vnNRxQ6Uw1U5LUtoy5KBuURkl8i4lkVuVSKLfnDfW69ZaCKh-XAJhkyf60Tttsg3lYdpXY1WtU6UwiRxE9Zm1JX3r-HeLauRMqp2Cbfj8E86hyeGA_I5L-ts1qAZH3yHNnFqk4a9kCVpK7tuRwllzqK-hiH3RhKw7ZIioj5pr2iy24QQ6_v0v37dG-m-DZUPqksJxy3gqS6dNovbzx9-6ABACRytW_NfOD6ZuU2TsGSw6_c_5WRHT8csNUeYN4klPor9GXdK0BDVT9aYXtXYiV4rXFmSPpppNBoMoQi7YnUUHygEvV7Ix18O_TSccllHd_lDKfcMfw3h4VXr2g8JMa7tKLnMEnzTKEs7g92ubGJhm5Gddp397_L7UbgTAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc10d9e65.mp4?token=vCrGLplFBMoHdmji_A6EEtzlf5f7UzV_RPcctdT8jUvtCO4gPaqphx8meo1XMGKb9yvi3wIo6Wh29g2rVLBoe0tGWtjqUmTjEHW-7O37W3VSvz2xdwdsODWSsp-HPpUKj8NRzwoZlFA85UeRtd4LnBELQoIFhPWdUGZz3ZmravP3nqhqEQfNvmfy61EED9_z-91Lakzpc0Ouos-ydHNj0SaJvHNocz8maT6xtegymAoy-QmwiQdJiUnVpPwFuwicKdI_jqorMUHhWJh9ZBO7jDMK4Uyo5oMm0mmFkwVtsB7r9vnNRxQ6Uw1U5LUtoy5KBuURkl8i4lkVuVSKLfnDfW69ZaCKh-XAJhkyf60Tttsg3lYdpXY1WtU6UwiRxE9Zm1JX3r-HeLauRMqp2Cbfj8E86hyeGA_I5L-ts1qAZH3yHNnFqk4a9kCVpK7tuRwllzqK-hiH3RhKw7ZIioj5pr2iy24QQ6_v0v37dG-m-DZUPqksJxy3gqS6dNovbzx9-6ABACRytW_NfOD6ZuU2TsGSw6_c_5WRHT8csNUeYN4klPor9GXdK0BDVT9aYXtXYiV4rXFmSPpppNBoMoQi7YnUUHygEvV7Ix18O_TSccllHd_lDKfcMfw3h4VXr2g8JMa7tKLnMEnzTKEs7g92ubGJhm5Gddp397_L7UbgTAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعای شهید؛ آمین شهدا
🔸
در این فیلم شهیدان آیت‌الله العظمی سیدعلی خامنه‌ای، قاسم سلیمانی، محمد باقری، سیدعبدالرحیم موسوی، حسین سلامی، محمدرضا زاهدی، محمد پاکپور، عزیز نصیرزاده، علیرضا تنگسیری و مجید خادمی حضور دارند.
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/447708" target="_blank">📅 00:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447707">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EScmgDJRgKFLXPuUOD9H8Nh4822PsZI0w-Q1O8zKsOUUGAooBKn7IRjeHjjq3MV1lMZt-h9b0P56C9JPXwHwSdLSBtrgqjile2zy1zeONrBaHmUp8iZRIyuVOeQKw8_9JJK0g2Nlu_DIIkhCdC2DJn0xLznZ0cR2Mv-zzx8_D8vJJzCwOcO3ewpKgYZkuY4tu-tp5msg_QVh9lKjFLzzVNKrYoqsFiMPKUaSGYwDB7z5mFj1HEP3sQG-ZPIH8VWgf7sRqtW2b3SgYkFSosxDGEkAQEHekq_gIeNtrSAK-q4KaiPWFN0x3meNxoqvLQG-u3Je7KFufeGpYoebQy59pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
| سه‌شنبه ۱۶ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/447707" target="_blank">📅 00:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447706">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hte9q_CfKaECUwgF6Sh5CaYuAvtWZXAoCjRE_nQDfb4Yp7G8PStsXC-Xo9IYxdQQWOE6FWJB__rLJg646sz1PTiyhSLDuH_pNyHRPyeC2EK-wcDQOeQpeDhodDw9xF0o1EZfowu8PsA0duxf6PqhI2sXEWVaYWHlZgwlCq_uTvJcc2RySxcNDkhTqpFEwZdwh7XKk_wH4DUkniKHdtAR96FqmJ_8f4z2KEFJ5dDg57JYliAqlD9GmAoY7xZVWmdjx2MoV1kL5NogLp0kMP4kWPICq0JyNCE3-4vHAiilCZ2cM-XEWkoUp90N_wZn8LF0MejzK3fOv0ovBMCiSRpgkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نماینده رهبر انقلاب در شورای دفاع:خون رهبر شهید علت بعثت مردم شد
🔹
امروز، آقای شهید ایران خود به میدان آمد و با خون خویش حجت را بر همگان تمام کرد و مسئولیتی سنگین‌تر از گذشته بر دوش همه ما نهاد.
🔹
جوشش خون او، علت بعثت مردمی شد که امروز یک‌صدا فریاد زدند: «هیهات مِنّا الذلّه».
🔹
رهبرا، ما تا آخرین نفس بر عهد خود ایستاده‌ایم و هم‌نوا با شما میخوانیم؛ «سِلْمٌ لِمَنْ سَالَمَكُمْ وَحَرْبٌ لِمَنْ حَارَبَكُمْ»
@Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/447706" target="_blank">📅 23:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447705">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907de65e2e.mp4?token=NNpEsqe-p5dBhh86cWQ5TakMISP_0Z43fJj-x3q5N5xhMrUmLaeNz6fmclIUe2uQfMZ67hSUFtY2ITqtnubic6Lrv3LrwFcHtrhet6WKS5dCpsP4msH0tGLJB8ZE4dW-gr9g8BWEYWs0W8xooRfnw3HIBoYz7OGYSBPCIfvs9jRqruJ_-uXLgKVOFjqKaWzBaKfKLZsLbK8G4lOJmw3eVoYIjLqgJASq-srTqV5Un5qUaj_ebSmd7OSFNbOqWT_ufn9yKquXup3TyX-ENvNjc0M-HPuXpmlaRcVTmApdBrS8OtuojijQ1gGVkS0xGCuLU0moesMWoPxJIBAoMqkc_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907de65e2e.mp4?token=NNpEsqe-p5dBhh86cWQ5TakMISP_0Z43fJj-x3q5N5xhMrUmLaeNz6fmclIUe2uQfMZ67hSUFtY2ITqtnubic6Lrv3LrwFcHtrhet6WKS5dCpsP4msH0tGLJB8ZE4dW-gr9g8BWEYWs0W8xooRfnw3HIBoYz7OGYSBPCIfvs9jRqruJ_-uXLgKVOFjqKaWzBaKfKLZsLbK8G4lOJmw3eVoYIjLqgJASq-srTqV5Un5qUaj_ebSmd7OSFNbOqWT_ufn9yKquXup3TyX-ENvNjc0M-HPuXpmlaRcVTmApdBrS8OtuojijQ1gGVkS0xGCuLU0moesMWoPxJIBAoMqkc_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیگر در امان نیستی؛ حتی در خواب‌هایت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/447705" target="_blank">📅 23:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447704">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b07596c0a.mp4?token=MyyDIJ50uQVRzDY5ZcOL8ws2EGQNdhQUgdeBfw2FNwRvFnlU3Vx38QXhh-KDfiL_3XQZyTCora2URVcJ5p1qA-8-xZQ-gqOKpkqzQcNmDr8M8VycBWa4JhjxRq8a4jVbD4toxq0E9o325E0gPpIMY0Lows8jtHcTTbVU3PFzVqzixB2hX4C5gG3yM1_UG51vSceJci1BkZWZa-umSfQZOVj06pHEfjQ2rITT7yVYZtky7REcVAn-NaXPPgJsRiAO0SfgVHiWvSycmOIDGM72LVynB8iCC0lkEYRN0zRVnEWZWxXVKa1JcWjWmDSXw1j5Iemr0txO2JJUhNz668sGkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b07596c0a.mp4?token=MyyDIJ50uQVRzDY5ZcOL8ws2EGQNdhQUgdeBfw2FNwRvFnlU3Vx38QXhh-KDfiL_3XQZyTCora2URVcJ5p1qA-8-xZQ-gqOKpkqzQcNmDr8M8VycBWa4JhjxRq8a4jVbD4toxq0E9o325E0gPpIMY0Lows8jtHcTTbVU3PFzVqzixB2hX4C5gG3yM1_UG51vSceJci1BkZWZa-umSfQZOVj06pHEfjQ2rITT7yVYZtky7REcVAn-NaXPPgJsRiAO0SfgVHiWvSycmOIDGM72LVynB8iCC0lkEYRN0zRVnEWZWxXVKa1JcWjWmDSXw1j5Iemr0txO2JJUhNz668sGkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به این میگن فراخوان
🔹
شعار جالب کودک انقلابی در مراسم تشییع رهبر شهید در تهران.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/447704" target="_blank">📅 23:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447703">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDgzB6oD3F7xxDGsXRToVg-zlKdm5jBi8YCgSac0Jp3LQBndOwD1QQ5ysW4pLjHO2DuK4x-PQt_ILzHtiOsSazBBYnOZBSmytCu2KFb2L6gAfAF2kl5TEH7gOSCGaMibb8p86dVLaUBM9Ov3mT-67cwS4t43_kIeJ67CZpSkv3EwcScnIxMQYr4cYiIynaXKoyCP-4QDK5c4adrsZT6Gvh__T1s2hLctIf9SfARI2lGi5iH0WD0akpLbrg-C3-Oi9D1W4dbBH5p-llqBmxgHvD7lHrY0QGZwMeLKGeAn0dnF_1ZUbmAs119oviMMC75mt1a4Cjrg4j-_B-wsIlzhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکای‌نیوز: تشییع امروز خارق‌العاده بود
🔹
سردبیر بین‌الملل اسکای نیوز که برای پوشش مراسم بدرقه پیکر رهبر شهید ایران، به تهران آمده بود این مراسم را با عبارت «خارق‌العاده» توصیف کرده.
🔹
او دراین‌باره گفته: مراسم تشییع امروز نشان می‌دهد جنگ ترامپ علیه ایران بی‌فایده بوده و ترور او نتیجه معکوس داشته و حمایت عمومی را تقویت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447703" target="_blank">📅 23:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447702">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daf5179a07.mp4?token=JajdW5AX1JtAd1nFuOKi7lBit2g5X0GRgFeHvSLzRN-g89El5Snp2l2DQCbdxFPG5TW8PloyoifMRv2ajtwaelZXzBi2NQ7iI6o01cRzEezaDMvQzI21Xi3Ik1RaCOpuYO0DdFfFIFU_3XjAFRdr8s97alfruZQXmCfI36j32Rb7DGbw_4nat1vI63vydEk5DoHodNP5xp2RgxZwLFXoavmCGSSIXynz_UuT2von6D8QUWen6BgiTQV5srGxI0H-gv_Ch55QDB8JTPkUjvVBBnwjndJKNEfTQljW5SvgKZ2vBrj1csDMMbwpGm27VK6YfBacizpxsx4ROTQda_qbaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daf5179a07.mp4?token=JajdW5AX1JtAd1nFuOKi7lBit2g5X0GRgFeHvSLzRN-g89El5Snp2l2DQCbdxFPG5TW8PloyoifMRv2ajtwaelZXzBi2NQ7iI6o01cRzEezaDMvQzI21Xi3Ik1RaCOpuYO0DdFfFIFU_3XjAFRdr8s97alfruZQXmCfI36j32Rb7DGbw_4nat1vI63vydEk5DoHodNP5xp2RgxZwLFXoavmCGSSIXynz_UuT2von6D8QUWen6BgiTQV5srGxI0H-gv_Ch55QDB8JTPkUjvVBBnwjndJKNEfTQljW5SvgKZ2vBrj1csDMMbwpGm27VK6YfBacizpxsx4ROTQda_qbaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال و هوای جمکران چند ساعت قبل از شروع تشییع رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/447702" target="_blank">📅 23:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447701">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be5112c1c.mp4?token=Lmeg696LZ5ejBt1CYb-jZF5VI0wtdL4cWtolIsKdv1f11tEV81cydnrgVAqfEPpavpMiI9WI_-ZTSdGAQVLyWmUq2AxxZT6IP328c0t8yT7JbXK1s-RRG-s0G7aCNw8nQvbHRRTlwuSg5i6t0y4-Hcl8EeF_ue_58rfbIIuTkhPNgOzT5n3Jtwka-eRqhZ9CfZGpY4qIXtSPFmwQGs3U-Peb3fg8FC6TqWfdMZPTN2l0xhJeU1lfAVO6ql_mHaTHgLb4szUCLa8v3XjEl9MjCt0sqi0tAZw001a6agavujZOWp1Ic-1TxOLz711zwoXXf04RlInW4CpgcnZb8Enr3F8dlpe70qA6uhA2WY3hZ2t8fXa2tjfinpKwhL_su13AQpQQ7OLVxX6EWCGh8Q_iEGLCYP0iessSZ10GiFkVDLS30xZVxkRgjCi3C32DEdek3qNsmqtUPgjH9Zs8qaVirXO7jxz3WSnxag8oZU5zkv8HIPUlESxjmQSnDmja_XQ_q6bRhqFnsEkS9i4wVsU93ebiRXOs-K2256lFUosOFg44GNM8z65_9BYDgAWZE8dnVPVeHSP1EStL4aezn54dBgiSLoTV8CabBCdWO8yV1FAlEOCkOSVxVnQ-BrOLMAJDVLCOpMgZBLIVUod_VD0nlP3Rw0nFNllLvGh3ieZel3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be5112c1c.mp4?token=Lmeg696LZ5ejBt1CYb-jZF5VI0wtdL4cWtolIsKdv1f11tEV81cydnrgVAqfEPpavpMiI9WI_-ZTSdGAQVLyWmUq2AxxZT6IP328c0t8yT7JbXK1s-RRG-s0G7aCNw8nQvbHRRTlwuSg5i6t0y4-Hcl8EeF_ue_58rfbIIuTkhPNgOzT5n3Jtwka-eRqhZ9CfZGpY4qIXtSPFmwQGs3U-Peb3fg8FC6TqWfdMZPTN2l0xhJeU1lfAVO6ql_mHaTHgLb4szUCLa8v3XjEl9MjCt0sqi0tAZw001a6agavujZOWp1Ic-1TxOLz711zwoXXf04RlInW4CpgcnZb8Enr3F8dlpe70qA6uhA2WY3hZ2t8fXa2tjfinpKwhL_su13AQpQQ7OLVxX6EWCGh8Q_iEGLCYP0iessSZ10GiFkVDLS30xZVxkRgjCi3C32DEdek3qNsmqtUPgjH9Zs8qaVirXO7jxz3WSnxag8oZU5zkv8HIPUlESxjmQSnDmja_XQ_q6bRhqFnsEkS9i4wVsU93ebiRXOs-K2256lFUosOFg44GNM8z65_9BYDgAWZE8dnVPVeHSP1EStL4aezn54dBgiSLoTV8CabBCdWO8yV1FAlEOCkOSVxVnQ-BrOLMAJDVLCOpMgZBLIVUod_VD0nlP3Rw0nFNllLvGh3ieZel3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی گرگانی‌ها در شب ۱۲۸  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/447701" target="_blank">📅 23:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447700">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0073f2bda.mp4?token=niTUoOLR90U6NeagL0K0ag0DH49QrHo1EQIupcFuebjsm4NRyZ6LsxS1sf6iCRCAvbxtYFawLVrq7yipXm9Kq3gWhqPlis1R1VpLi63mMTiQJwjHtefrCoE7Ue8I_nf261hml_BET6TeujbJkoYEc5bDH5WGLFuROCxr14D21cKFZHq82xBA_waSzUwo_qMBeE5GI15KZleW32cRQys29e0rz4EZpm1eQ89uLmCVWkBwyZUXMwfG9VUFptJwuMA_9-qdlQ3u3ChfITfBSzzL3X1x5gEkCqHwUVP9M0KshBWONcSvzKCmsKr-Ll__pdwHHsW14iHWZ_hE19Ci0O2qPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0073f2bda.mp4?token=niTUoOLR90U6NeagL0K0ag0DH49QrHo1EQIupcFuebjsm4NRyZ6LsxS1sf6iCRCAvbxtYFawLVrq7yipXm9Kq3gWhqPlis1R1VpLi63mMTiQJwjHtefrCoE7Ue8I_nf261hml_BET6TeujbJkoYEc5bDH5WGLFuROCxr14D21cKFZHq82xBA_waSzUwo_qMBeE5GI15KZleW32cRQys29e0rz4EZpm1eQ89uLmCVWkBwyZUXMwfG9VUFptJwuMA_9-qdlQ3u3ChfITfBSzzL3X1x5gEkCqHwUVP9M0KshBWONcSvzKCmsKr-Ll__pdwHHsW14iHWZ_hE19Ci0O2qPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاشقان امام شهید در جمکران منتظر آخرین دیدار
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447700" target="_blank">📅 23:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447699">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd89a66e7.mp4?token=g0G60xMtDfrp4tpHJU7vfaS-UMzL_uG8vWD5wOxUOMhMKDpE4wZsKuTkrLeF7XyYGmFR3iE6Mtn9L_eJRFJY_MgjjEzpCmMNfNNkNsmf6UpTBq7AEPzKT6CdcdiNWzNcPK34qEmEP6cHi313wt9USzrKUKWhi74w63kf5vZNkEIHY_Oq4pILxL64Z87NJyO4NcoADrrW9Zk8gKZCWthEtLPGbiLuGBSmw1yoXpAnCV_dtq8jPGLbqHMNSG58LAHtsHIYrdVUY1IOGazhRKace8HDeqYWSKnR2hdPIa2AlQrdubcxrcKkqtAE5aub3WBHPENHNYb-JHfMhZK0orkmOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd89a66e7.mp4?token=g0G60xMtDfrp4tpHJU7vfaS-UMzL_uG8vWD5wOxUOMhMKDpE4wZsKuTkrLeF7XyYGmFR3iE6Mtn9L_eJRFJY_MgjjEzpCmMNfNNkNsmf6UpTBq7AEPzKT6CdcdiNWzNcPK34qEmEP6cHi313wt9USzrKUKWhi74w63kf5vZNkEIHY_Oq4pILxL64Z87NJyO4NcoADrrW9Zk8gKZCWthEtLPGbiLuGBSmw1yoXpAnCV_dtq8jPGLbqHMNSG58LAHtsHIYrdVUY1IOGazhRKace8HDeqYWSKnR2hdPIa2AlQrdubcxrcKkqtAE5aub3WBHPENHNYb-JHfMhZK0orkmOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد خون‌خواهی گرگانی‌ها در شب ۱۲۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/447699" target="_blank">📅 22:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447697">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa2cdpJbCE20sVeQec7PRqnICK0kEF1Jwz0JfndU8Zsc265-Y9jQPamtnZrLPb3dQOpzphECi6VY0m91z20YnW-tJWcwC7DQngzONcosF8U0tVm24wXjXItEw438y_INO9LhygMPM4mrr9Rcd2xKlL3aglNThkvmnJePOh6CVe0OCbD7Vs7bR0Xcn8carXD5iQmwSlTxfNxOnnaBzU7ZgFr8d2xm1EN8gLP4eHuE87LSG6csQAWLdivVOBc1B3j371SqQPUMOxj4R-Gv-m4ZCGv8DhELt2UGhIRQB1iRS1ka2UjU6KLB-W6HUhszfcVD25aDHmIFN_ygCCV2rhxntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی در پاسخ به ترامپ: با مردم ایران با احترام صحبت کن، وگرنه با زبان دیگری پاسخ می‌دهیم
🔹
ذوالقدر: به رئیس‌جمهور متوهم امریکا که امروز ۹۱ میلیون ایرانی را تهدید کرده است می‌گویم:
🔹
پیش از این تو به‌عنوان رئیس یک کشور بی‌ریشه با تاریخ ۲۵۰ ساله با ادبیات مشابه از محو تمدن چند هزار ساله ایران سخن گفته بودی و نتیجه برایتان جز شکست و استیصال و درخواست مذاکره و آتش‌بس نبود! ایرانی با زبان تهدید بیگانه است.
🔹
پس با مردم ایران با احترام صحبت کن، وگرنه با زبان دیگری به شما پاسخ خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447697" target="_blank">📅 22:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447696">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd48407210.mp4?token=JVNkxWBweSG_NLbqG-OQUzU8EiETIpPvt5gsidY9qSHC39XQX5FUNn_bhNE-9dEIASGRHCYmxYTtb4eYCzxmJMy9FT-84Y5Df4BSYbmRjsYC8pvaxplZB6cVDqFL0ihRwDWw51RBgd0_mq1rEhy6T39VbIq9csNq9kyBUVpjblMvRuZ4I3F8zrR3pgYAE43bzCV_st8dCo9I3v4lWC-HxHm8Bj1_rwtdhj5qp_IS4suKsRuDpytcIHejvPdbWXCfrUHJrqqx2sXq-YuzIKE43lIi4kyhey-Oax-ua4rLGHZMROwv9sVKUsm_D_eZ5R2iy2a9FJo4a5JEnB9RFrEXGX7HRmufIUk95UBcsPWyHv0rpYxSLgOLXk05LnmGYdGka_PugtoGVmJE5u1USv74G9UeE-PSv-9IbDMrUl3YzNpOfId_pg0m7QNErUGbXDcMbRypwM8uQ3JYJrRd9TWM38ck1nTCuAQVBszttQEzqm7XmoFLy3tDRzZuj2jo9hlOesz2J6ir-gcNkrsXCmoRKkTbfTBYQm56-yqFN_Re3gzxJP3sx4dpIdE_oumInxPPRmDssuCdwsYPWwtTJhM9wIwMozT6ttjDjKGHFZNEQUnWaV6KQK_boovaLdrR1wgSIstnKUrx1n2_1ncG0vM364A3ikcSaOLVNiiHj3rXd2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd48407210.mp4?token=JVNkxWBweSG_NLbqG-OQUzU8EiETIpPvt5gsidY9qSHC39XQX5FUNn_bhNE-9dEIASGRHCYmxYTtb4eYCzxmJMy9FT-84Y5Df4BSYbmRjsYC8pvaxplZB6cVDqFL0ihRwDWw51RBgd0_mq1rEhy6T39VbIq9csNq9kyBUVpjblMvRuZ4I3F8zrR3pgYAE43bzCV_st8dCo9I3v4lWC-HxHm8Bj1_rwtdhj5qp_IS4suKsRuDpytcIHejvPdbWXCfrUHJrqqx2sXq-YuzIKE43lIi4kyhey-Oax-ua4rLGHZMROwv9sVKUsm_D_eZ5R2iy2a9FJo4a5JEnB9RFrEXGX7HRmufIUk95UBcsPWyHv0rpYxSLgOLXk05LnmGYdGka_PugtoGVmJE5u1USv74G9UeE-PSv-9IbDMrUl3YzNpOfId_pg0m7QNErUGbXDcMbRypwM8uQ3JYJrRd9TWM38ck1nTCuAQVBszttQEzqm7XmoFLy3tDRzZuj2jo9hlOesz2J6ir-gcNkrsXCmoRKkTbfTBYQm56-yqFN_Re3gzxJP3sx4dpIdE_oumInxPPRmDssuCdwsYPWwtTJhM9wIwMozT6ttjDjKGHFZNEQUnWaV6KQK_boovaLdrR1wgSIstnKUrx1n2_1ncG0vM364A3ikcSaOLVNiiHj3rXd2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خودروی حمل پیکرهای مطهر شهدا در مسیر آزادراه تهران - قم
@TehranFarsnews</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/447696" target="_blank">📅 22:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447694">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">لرستان هم فردا تعطیل شد
🔹
استانداری لرستان: تمامی ادارات باهدف تسهیل در تردد زائران آیین وداع با قائد شهید امت فردا تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/447694" target="_blank">📅 22:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447693">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUhqflrPWks6sOnpJ8kqiW_4p7ToAPN1TX7ab7YscLSEHYvG6XUHypZfngjOC9vgBjvq13ok-Iw9vvbQCeMt7ockPxeD9YAUsEgKRSY5c0Xm5YeGD_lQ0yPtYOqHlDzqcMzMHZtUmPlrIxgdHybtcVJCPX99xMlUFZV_4Wr7rhIjcG9biKekV4bi0w5JcAicIn60nwHV-c3mXXFU3gNy0M8v3R3U8N83Mdyl3EGYYpMnaw-cHDkBhWugopoL36LAyjJqVZRhony5cCgx_6MnsbVX6wBZAEfHkHVn-C0AuvgeYIblrD88DbV6grK43a0SsizqwSIFWmFH4YnOzWzeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محسن رضایی: ‏ملت بزرگ ایران، پس از ۵ دهه، امروز نیز با همان صلابت و ایمان روزهای آغازین انقلاب، شعارهای کوبنده‌ی خود را علیه آمریکای جنایتکار و اسرائیل غاصب سر می‌دهند.
🔹
این شعارها که با خونخواهی رهبر شهید توأم شده، به خشمی مقدس و اتحادی پولادین علیه دشمنان این مرز و بوم تبدیل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447693" target="_blank">📅 22:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447692">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سخنگوی ستاد تشییع رهبر شهید: نماز بر پیکر قائد شهید در جمکران، بعد از نماز صبح و به امامت آیت‌الله جوادی‌آملی اقامه خواهد شد
🔹
بعد اقامه نماز، پیکر رهبر شهید انقلاب در بلوار پیامبر اعظم به سمت حرم حضرت معصومه(س) تشییع می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/447692" target="_blank">📅 22:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447691">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
تهران، آخرین سلام را گفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447691" target="_blank">📅 22:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447690">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a509ce5c59.mp4?token=qBoo-YpS8gASO9_CWGzmUAzszXHi8wD24Oo2GflQK6bpICYVV0RNH3HB0BovFMSxhC0d-iQNqYOod1oGeSaP5XSYAHYS-YEMncDcq3OPjtxL4orEyN24kO--fZqmT-g4w9MKf3vaS5MyGCapBLvyqYvYpgbKr-Vj-PRHjM2gjM-TkfsFOOMVlIv9uVE7mA7BMEgzh3MV9B5eEqTW7-H3-w6AHbPRA4HUzSQtel7sufefIKAwwz7QUppFw1ZgQPTgxOwPCulgrJczPPoMD3dI38fyU5-Y0tGFiK7SJvnkgTNLXkJ0HIIOPKKBFitbM9oWW_oVqEl4KkGlQPeYtYnZKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a509ce5c59.mp4?token=qBoo-YpS8gASO9_CWGzmUAzszXHi8wD24Oo2GflQK6bpICYVV0RNH3HB0BovFMSxhC0d-iQNqYOod1oGeSaP5XSYAHYS-YEMncDcq3OPjtxL4orEyN24kO--fZqmT-g4w9MKf3vaS5MyGCapBLvyqYvYpgbKr-Vj-PRHjM2gjM-TkfsFOOMVlIv9uVE7mA7BMEgzh3MV9B5eEqTW7-H3-w6AHbPRA4HUzSQtel7sufefIKAwwz7QUppFw1ZgQPTgxOwPCulgrJczPPoMD3dI38fyU5-Y0tGFiK7SJvnkgTNLXkJ0HIIOPKKBFitbM9oWW_oVqEl4KkGlQPeYtYnZKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایانی بر انتظار ۱۶ سالۀ مردم قم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/447690" target="_blank">📅 22:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447689">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN8k-VOg-TTeVzJXMpxjn5qtuqna23w--CdoyLdDn3LGReCFWr4NwkGGvljNy6fn5jtgM4ns1NrMwSDe7v2lN3IeuvKXMIN8iNFIzBuLH1dTJfWx8PxeTFySL8SsfGVuHquJ33FKicA2ochi2AkSaiRQb1lTjFr5N6x_3619nfPCHZgDhPfGkjLRYS-kPq9KOuvXPaHXn7oGj8pfzLk6TBvS1YWtArf1dG1INW1ORjPlhAst5eekkqQ4mWidjmoENK0ig_OY9AFJFSXBONTOQXMhQjCLEmEawoG-DQWplxsxDJAmiyAEHSMTTIBp9kj6xJ347pYVYtIxRgnia0X6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای حضورنداشتن سیدحسن خمینی در نماز رهبر شهید
🔹
انصاری، سرپرست آستان امام خمینی: سیدحسن خمینی بدون تشریفات متعارف در مصلی برای وداع با رهبر شهید حاضر شده بود.
🔹
اما دربارۀ نماز بر پیکر رهبر شهید، ایشان به سمت مصلی حرکت کرده بودند اما به دلیل توقف خودروها در مسیر، امکان حضور در صف ویژه نماز فراهم نشد.
🔹
او همچنین امروز به همراه خانواده در مراسم تشییع حضور داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/447689" target="_blank">📅 22:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447688">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phBmj4cm48LYGsW7heJNgPL6jh11MY3PiD8IkL3-NoJA8WPVmDPMUD_wypIKwHbACgsBUe6L6LUYoGreebWTgh9jouL0Ei8hLF7WJ88gvCh__9LdsNNXFCl27HErhdjwEP6rc0atGbtLzfodGW8eoerWsNDIS1yOq2UuMZRPy2Hb77ahQ3IGkzAOqsuFQB303hzGoJqtme5-4yxgGJ_gsNX4h9HTBWXalHe4LqoVAnMbXA0gckd5bt2k17-D4tt_Tu7uJb2cppBzThyAgTd9qXhv5G-zLdws_JVM2GrU26lz9p2qVsFdywVUz1xQh62m1uLVa5EZB08KsombzUDTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: قاتلان قائد شهید امت به سزای عمل‌شان خواهند رسید
🔹
رئیس مجلس در پیامی به‌مناسبت تشییع تاریخی رهبر شهید انقلاب نوشت:
بسم‌الله‌الرحمن‌الرحیم
ملت شریف و قدرشناس ایران!
🔹
داغ جانکاه فقدان رهبر شهیدمان و آخرین روز حضور جسم مبارک و مجروح او در پایتخت ام‌القرای جهان اسلام با تجلی وجه دیگری از بعثت شما در این مقطع حساس و سرنوشت‌ساز به حماسه و شعور تبدیل  شد و حرکت به‌سمت پیروزی قطعی ایران اسلامی و جهان اسلام را شتابی دوچندان بخشید.
🔹
مردمی که ۴۷ سال پیشران و پشتیبان انقلاب شان بوده‌اند، در ۴ ماه گذشته هرشب با ندای مرگ بر امریکا و مرگ بر اسرائیل نفرت و انزجار خود را از قاتلان امام شهیدمان فریاد زدند و «انتقام» را خواستار شدند.
🔹
تحقق وعده الهی قطعی است و متجاوزان به خاک ایران اسلامی و قاتلان شهدای این سرزمین به ویژه قائد امت، به سزای اعمال شان خواهند رسید و گام نهایی انتقام از مستکبران با آزادی قدس شریف عینیت می‌یابد.
🔹
ملت مبعوث شده، رهبرشان را بدرقه کردند و همچون ۴ ماه گذشته دست بیعت به سمت ولی فقیه حکیم مان حضرت آیت الله سید مجتبی حسینی خامنه‌ای دراز کردند.
🔹
باید قدردان این مردم بود که در مسیر نورانی امام و شهدا ذره‌ای عقب‌نشینی نکردند.
🔹
دنیا امروز فهمید انقلاب اسلامی و جمهوری اسلامی ایران، پاینده و جاودان است و با پشتوانه‌ی این مردم، بن‌بست و شکستی وجود ندارد.
🔹
این ملت، از مکتب حسین علیه‌السلام و تربیت‌یافتۀ امامین انقلاب اند که در ۳۷ سال دوران زعامت رهبر شهید انقلاب، نه تنها روحیه جهاد و مبارزه را حفظ کرده اند؛ بلکه ساختارمند و محکم در برابر زورگویان دنیا ایستاده‌اند.
🔹
قدر شما را باید دانست و از هیچ تلاشی برای احقاق حقوق تان کوتاهی نکرد. چه در پای لانچر و دفاع از کشور، چه در عرصه دیپلماسی و مذاکره به عنوان بخشی از مبارزه‌ی تمدنی و اصولی با سلطه‌گران و چه در عرصه خدمت به شما برای گشایش امور معیشتی و اقتصادی.
🔹
امید است توجه به توصیه های اکید رهبر شهید و رهبر معظم انقلاب در کار بی‌وقفه و موثر برای مردم، با همت مسئولین محقق شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/447688" target="_blank">📅 21:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447687">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تمامی ادارات یزد برای تسهیل حضور مردم در مراسم تشییع پیکر رهبر شهید تعطیل شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/447687" target="_blank">📅 21:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447686">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ادارات بوشهر فردا تعطیل شد
🔹
استاندار بوشهر: به منظور تسهیل در تردد و بازگشت زائرین رهبر شهید، ادارات استان بوشهر به‌جز دستگاه‌های خدمات‌رسان و امدادی و بانک‌ها روز سه‌شنبه ۱۶ تیرماه تعطیل است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/447686" target="_blank">📅 21:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447676">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZmF04z4AA__fdCuLzj-0Y1GE75Bp6GCABMf4cSMOTbKsddznhh8OpV3HYSt4TV6tbV_Htb2LdW6P9r0fSZ0LDnvEXCRWLFvAHXgFJQx1HLvSiHwDd5XyGb8jyYJ-8m0fYVhhG9Gaea25qNfCDRGD2NJKbzNbZ3OSydUW2bgfrecFUneETKERalmvonekgoUOtRIQbeO23ssdj70skNvqVsUkm3AcgJ54tKSXs10eMt1pL8mkgwMMxViUvUU5-dYw2NFizdMM4o6sm0Gcbuh1kiNL8dEHFq4aSosW5kk43vRA-E5jRXocU7nLogzg_SM9TP4oAQerfIDJZyFVyrKkZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXo70wkP9Xopxig8JXkl-_H2PGZqqXnrH18wfqEIBXSb3aE9srwxAMI9udZOkU93-TKZb-u0h_nyR_K7kX6oE4hf0wbvfITvf1fkafKUthI921qnDUEFzb4zzGbTV-0IWoudHaLlQqTyOp_Bgmhw4ulfyQI20I_ms9hjjAaPEobisILDXluNJGZ72jSKcOzgu8POdvuuQFDUzjOc5m7ceiwyROHVR0WF9X9eWDzYlvlF8856GCx1mKE6Bed9L4JlgG4YkWH41_bW-tgYD4jbHzvtgTKlSjA7OtEAK_PMJmL8OiARmxjiYyR19Jgrei_ijwbISSQrGPJ5k8ww8GgkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJVftn60MazDwRVjDb3IgNvHVgObeoYbTE71amZihbE77931VCM8kTTEHHCoA3hSP1N8-7nyd0kszXKatEOJc1-BdBdH4crBGldY7AL5xoJAj63mGSdIO_HgbfCvvtiIv2QqIuv5wcJ6IfXWoYaGCh1LfPG3h7s9vKzIw86L0xap1MZ-kkPtdPxJ66J1wFRrNUEUWkW0OK-K7L8nKSmcq-34tAKJBQhkpDYYYIRG7OC04WsgHSX3pkp2TQacMegSsFjEpHaVqd9uliLLaBx4LRVs1SqIkn3f4El045DiQl9rpvpn91f3QppLoB2-vXlxezKpiFNp7FNAy_FA_BjLjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hS_ga9BjnPPjoXDiRrVLNzsVDAjMqhGtcaKS4mNdPwcvIwVVW98wFYE6i1hrGZGYASK8NDVqttXEC6ILrseqge7NlWm84b5n8K4WE4OA3Yt0ul889hicLrNz8WxPthdZhoFS6cbAdNj3SRS3ycxI_1gCfumoGTjpb65PBYl9G_KA1E2zD7pwvsOBjz_jPxXVfPk7SgXckCNq5VpAY6FzzcQrfMLR4Pa1MgBNls7R7cj6j25NoNIwWVJQCP8IgICkVuiIzr0B029YJXZOd7-TzGaOIyKXGnUJuT7lo140rwE759Xvz1OSyottwRZmK6a6NoiZQMurAP3XwJ3jnXgU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dDR6hhsZMMAZEIU_8xqLnlWpf7QwaN3geWI0FZtAdq12uaX5aoBR38byyyUqBM06WLQ4Rcn8yOwUDmQf3kfWDTE9vXS69eP_m8f4HHGKNyjt3e941z48186TbHhqvexL1WixpX6QoiYIpSoeGmg4OL_G71cDFTzk7cjqcRztRLWiWU0LL4Vb1ju8s2DyMzSS4u5aLHq3wZL8o0fy0msElC5pz52ppC7jWLs1ApqDGBcs37NuQHT9DEMHB31VgKKEdDg16cMttefyWdD3l3SAI98Q9k0nnH-ioX1W-RQvZDlUEcfZ1gMOz0dvp1VUgOcABx0ABgTijJaFHQexni4vIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EbyN9Q7JiZ0CgUpHgSL3MizJSG6YRJztBYriWgACuMVLlbVhALQdsfjhj96zIIPgJCN5Whawcvqp_UhoG6OBSIuCaQGxm71TBvINP30yLF3x4VRo75wjf4PaiVvFUIJJjyVZAupNbirotsOd-9wqEhp00ejZ-lJSRfe6FQibXlAuNPMfGKYmWCQ2Sc-mFvllv7sjpczeZcF4zG2Kz8VfUJDShE4N9l9N5dhkwyN6Vdvx1Jlw6HVdNkfQBsAieChp-PY_glWiBR-Qp3i93xIEhYmx3oQA42S5y0PQ9L74kXNhJDN8822v9ZHgdYEjG823Jd5Lvx3J57IceyvWwfQQOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unT1TV_ilEIYGaYIA1-RhBVgRQceGA9yOsdtLQIKLUS7EQkVE5KkbFZXD5OSMeuSOSaojcb4fiijm7yoJwX76iITQU-2NdH-1W9pGCKReLVQF5sFpLdBrMTb7DPR04Gc_jl_vkDU9HUUj5Za7U4AYvUHwJ9Dg-lbsjWXYwLI9-M3RAqUcOoqsO--zKc0iPK8GmnMyn49Aw8t-xZv6mESt-IqlaaFYfelLRs3xWTda_16wdLtLNDUPRLQF6fDNzBidIXB1gQvI2RODF0l0Sz3pBBs-Rl-Ji785BH_qcY33a_zzjPivzzVCbffvc_ApRzmmidSjjh-2EuswIOPDQBBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IOkxUFk_MrjEvpulassqKRK_IN5fhwQJcsKrOI4YSYL--YrkdnCv_p05ejpTs_4BkzwuVWwROFhfJXyCq8EN26QuB6btfr-TrzvTOWew_12ibcbqAjFejsQgbUn8TJXxEbhaE_CIhjsCB4E15Za1HAjk60pY0C8UtGBYMI219mH3VPa0wEDnbU3OXqZo8IcAxT31Ts-2TfCJOrwScZn8N4MeAUqTT7Zz4nsXFFwY_Tl-3KoXVWQY8jVT9_BT0jOssZccODmqpiXKB0iirv02emJoPFMs6pqNYq37ZyV8rLkcSNDp5uWxZGpgDtY6pYQdX-lmrYiMfw4DajCig9fMmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0MM-F9mA3sUyhZSnm2_o-IIOQSfdtHhSq_txz73K5budy1Uqf0Qo4mNJcF_HBMZT0NYhZ6W5RCWJfZ7MDyi99nQoLJVNSemDtrP6X_8J1GOCRvmW7wBIsH1T_1YgPacMasLf_sBAB1hD6Kdc1hC1qrdEuh5oolsZg61QjxwCTWw_kVpPLLUfpxLrh0FsVwOJgHk3M1yyoTWlxXLGJPzazwIFMsdMil-F0h6KTAh_vJIeVDBQCYSz2SKsnIv4nZh_9koHMM3qJc9bWlMgSuVIWWxlIro3hwCCpiehkP16WCDIZvd98IgaQF-MQyZ-0nsrKz72RKQuY-U67RWI8lC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6z3wOmt1bn10BPPvYApjZ1idQ-NliVcl3S6swCSMmURwKNinl6aWdu0Q_d2gLi5y435OsHV9jJkD7wk3A8BJrkjrDzme2xxve2ZCKT_QY3qiJfRSUFdZefMN928FA-m28Ldr_tPfnnk5OU1Y8KsQgzplBUChDRL5F7maSzY2-hwMbjdfVjmHdWdvmC0_Ik6j9WyxjBkkSG3A0TQuIiBzwpebJi-SDzfH6VWchAfvDFNhKKB3yhN7uYCR-BtOTwKcFXOlq6UwT8oA6lMflxPCB8oq3c0Z1dU8_GpddKgt1fP4DNycvalj_aidSrt6mBFkliflAudYBcPiOzDU9vcqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
حضور مدیر عامل محترم بانک شهر در موکب خدمت رسانی بانک در مسیر تشییع پیکر رهبر شهید انقلاب اسلامی</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447676" target="_blank">📅 21:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447675">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/447675" target="_blank">📅 21:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447674">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKbHp58W-qdzS3r9Fvkgr40RuRtOM_C0r598bjqiXQvJBwSyql1Zr-z2lb3P0k8zIe71AnUUafuWSzf79wdLfTF97zjExkHF8wscbhFEWN70D1RgNavQYvVwof2FD6uJsLhnHCS5C9rqLrpUwJ9o06Vl7uNtAgCewYsjA_KiK24wzbZOKqZaxF5bpj4dJ01QBhdJRV_utgNLBmp825086UQeDaV9PYotI6k5Ie5PqSeWMyY30H3-eKi5ntljWYcCGjEFZIOVPmJqLEs0LVXdbaP3MmQUPzm6VtNIxhS5iVGmrZJhdOVhnIb5Wg_2LIwUQN3SQNHoSs98mx4ZJ_LXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس فیفا: ترامپ دربارۀ کارت قرمز بازیکن آمریکا با من تماس گرفته بود
🔸
فیفا روز گذشته اعلام کرد محرومیت ناشی از کارت قرمز فلورین بالوگان، ستارۀ تیم ملی فوتبال آمریکا را بخشیده تا این بازیکن مشکلی برای دیدار یانکی‌ها مقابل بلژیک نداشته باشد.
🔸
بخشیده‌شدن این کارت قرمز با شکایت فدراسیون فوتبال بلژیک و اعتراض افرادی چون توخل، سرمربی انگلیس و یورگن کلوپ مواجه شد.
🔹
ترامپ امروز تصحیح کرد که دربارۀ این موضوع با فیفا تماس گرفته زیرا بالوگان را ستارۀ مهمی برای تیمش می‌دانسته است.
🔹
در ادامه اینفانتینو هم تایید کرد که ترامپ دربارۀ این موضوع با او تماس گرفته اما مدعی شد این تصمیم را مطابق با آئین‌نامۀ فیفا اتخاذ کرده.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/447674" target="_blank">📅 21:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447673">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv5thzjrrqW4Cdy55TLrmy92seALbROJi-1FdapXzFTDKgENRBq5nFY8FW21uxZXv1jkDQt-FMvZ0CrvaeLY_MW1kwNP8HDgKZr-T34A7Y0t6e-gBiPgHHbocowzJWKZufiR7VwF7LG_AkE_4Ni2GTZPelY3DmEGxT6NIVodc091n9jL_UFxMJKWjycrOe9kYrykzEp_3ynS9VvbONTX4umklqmRxNaaXHmSi35P4Ipiy-gTEFwHChVsla9H6ZrHiiG5mK3Kqe9OKut4FLzK_VIAlFGRFUtch0xriMSmchkzkrylPzKS3ksp1VwfGFOm1TWYrzcqOE_zqI9FOWpkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بدان امید به تشییع آمدیم که صبح روز ظهور برگردید
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/447673" target="_blank">📅 21:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447672">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_Gcaj6fsie9wTVrZG3fZRWjZjwL2BDKN8D0ITJQ7zrazvfczhOexKCuHhKPioou0jKTbLhu9lGQvJdv62_gYorUAu5vzYMl3R78uipSEG-pNAqnUw87uqNvdfR2MQyNJdMw4wtWA3hq06lpBxZP9oXVm78ijJHQb7HkcyyzNxWy8bvu3ugo1ObE8ozfxz64CMoVfhmipWFiLyqUdJ2Vw8hFqHIeepuzsPM5SkWisL3yJqObcfa_sdZ-Dw5oLwrfm9tHk4F-jZn_WVggcJqmDJDatpLq-G9UhmhfDJh2pTudsaeCq3Df_1sjMuaogHsEOI7fks2dSxNjeIGSKuc6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
رسانه‌های جهان مات عشق و علاقۀ ایرانی‌ها به رهبر شهید خود
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/447672" target="_blank">📅 21:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-447671">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a9851feaf.mp4?token=pmP6abOl9d1_qSwXk-Lw2zc-bm0ggLmc6yEeXtFmrVtmzZsGzPQT9SaL7SomFQZZW2Gf7FYBpRA40AkjAklGJ1iV8iehPbJzs6IygiVcPWbICHx7elfpPYg5JxLPzbEWoPEWZ5NLOhaFzNVe0hd1Bi7DKaxWoe3FIF35fwBs9VR6cddaUGUFe-ZeMXdz48TsPFqgWLWp1meZ-OLrdFeeh-y3FKtM2n1brL-A-tbS9KtNwWHo1XCMkZ0_e_EGBys7y7570cGm-llbxDJ2BbbIzJmo9KE4ABO8O91uVsWQ7U1wAn9CNTxCRlSGsjnT3zOq--26SIRrE-jjMCCLvUJ7UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a9851feaf.mp4?token=pmP6abOl9d1_qSwXk-Lw2zc-bm0ggLmc6yEeXtFmrVtmzZsGzPQT9SaL7SomFQZZW2Gf7FYBpRA40AkjAklGJ1iV8iehPbJzs6IygiVcPWbICHx7elfpPYg5JxLPzbEWoPEWZ5NLOhaFzNVe0hd1Bi7DKaxWoe3FIF35fwBs9VR6cddaUGUFe-ZeMXdz48TsPFqgWLWp1meZ-OLrdFeeh-y3FKtM2n1brL-A-tbS9KtNwWHo1XCMkZ0_e_EGBys7y7570cGm-llbxDJ2BbbIzJmo9KE4ABO8O91uVsWQ7U1wAn9CNTxCRlSGsjnT3zOq--26SIRrE-jjMCCLvUJ7UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قم آمادهٔ آخرین وداع با آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/447671" target="_blank">📅 21:16 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
