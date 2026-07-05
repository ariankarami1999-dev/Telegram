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
<img src="https://cdn4.telesco.pe/file/Mc9KBt3uUFjBj7OblSlHJSBVtcsquzDO8NIehmIP4XNSfYSW74sB4OQQ9vFFm7d39C1oaeixtLiUBpH7mxBNk704wbzbZNje2ajnO_xekYLdCA2G2qwcb2pgw8gQ9NNkeD1tQwE-9CZLnHzu18qeogCzc8C9TyFbMrbxsBBR83RtrJtDxDCxZwtgPkTVJR-PUB05B3Yh26FlwqVMMMqfOuzESJ_cfmJVqQDJbxZ4gtYbpkOjPCI-Zpz2PJvigT9mXPLO8VtJm_Dv6xy2oWP7e36OJ_Mg1UN5WFE0PX0TosUYLqRQLeiHJ_d5H1MM_RAVpsysoM1wvh0g7phFiegx7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 204K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-67352">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=tuArcdsdB7t7gTc-O2AD9A9lzfZjwvlqZr_zwHmsb1xLw71nBwdn4gNHQnNayHXfORlk8C9eKzAEJ8bcuGOhlEiKDoRaHltAJLYqFvfe1JMZRkJg9jhmgOUeBAkZfuSB_ejNQ9b7ZQtBAOWfzvcwTtpTmO0XGIrSJeKIHZtMlrFhjgi1JuuSbvjQ_Wei95AswwXvlkng63qZCgzqsqoOsIOlzS_FlYPRjBJD4JLZRQf9nTzsMzP9qSovJkKJW9XVV8U68kEyBBHlBHRSpz_cwthyYvGb2NwvNTR55uPMl9W86UwZgO-JI6dChdYJzds4bh8DiG0WEVS2XCZdZgWZJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc47a54d3f.mp4?token=tuArcdsdB7t7gTc-O2AD9A9lzfZjwvlqZr_zwHmsb1xLw71nBwdn4gNHQnNayHXfORlk8C9eKzAEJ8bcuGOhlEiKDoRaHltAJLYqFvfe1JMZRkJg9jhmgOUeBAkZfuSB_ejNQ9b7ZQtBAOWfzvcwTtpTmO0XGIrSJeKIHZtMlrFhjgi1JuuSbvjQ_Wei95AswwXvlkng63qZCgzqsqoOsIOlzS_FlYPRjBJD4JLZRQf9nTzsMzP9qSovJkKJW9XVV8U68kEyBBHlBHRSpz_cwthyYvGb2NwvNTR55uPMl9W86UwZgO-JI6dChdYJzds4bh8DiG0WEVS2XCZdZgWZJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمزه صفوی :
یکی از گرون‌ترین سیستم‌های حفاظت در بین رهبران جهان مربوط به علی خامنه‌ای بود، اما نتونستیم اونو حفاظت و پنهان کنیم و از دستش دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/news_hut/67352" target="_blank">📅 21:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67351">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
ترامپ:  از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!  @News_Hut</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/news_hut/67351" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67350">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obf9JaJGHQ4m9bN2JAeDjK1Eo9P_86JBQn7MlAcYpcRYtdoBwNovuKRIX4dk3GYI72fIlglaMxSaqYIgNo0AjzT2Qnkzcm9Hc6AOzfFefITtKTpN6pOMQ9aXep4b5_Y8QvLV6ADQJG5ZylgKaYfnixn8y5BZJiB13TwXBCxCDIsLot2SqPerV24118IlHnpWFkHqzQzjbtZ3Lq6EfSe_ACUoUpP665FiLDI4yRUCwBYJqIZ_RPDQ2Z68NZw_WxNxdPiySYwSpEThgX7siPR4W4sS8IkF0Y_LvPYvIAjEtxCsO9coXl6oxy0pgDETcIU92oODTj9cq0UaTAIZmkrgYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
از فیفا برای انجام کار درست و جبران یک بی‌عدالتی بزرگ سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/news_hut/67350" target="_blank">📅 21:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67349">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Ooh3yFt3X3f_7PcEZTRxbzNHfUILqxAJsAYpDG3QabT37qhKupFb8tYCqF5qMP9IcLtsayHbOfHDzZ9OYM92vVDSTXClv8-VpGBD2-RSdN3FoJ8j4i-UDrygmRD_qRHbYO7PSerNftSbsL0U3nz6oKz4VedfHahcEOCgZHuSsjbC7qGVyg86kFGwuiEklaVlu5t5ihr-PC3HppXqjNr-GVjVNeA5Thu6t1gmbYqrFTcdKgJAcx7awopHVOtzldgwb6iwi80a9Xt4ytE2ElbIA37k3MThIKsKWjGGE6BD25YJzMINpZ942CIrqtXB3vWQVJFM6h6nHxDTpFYT8eGOXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d12e972bb.mp4?token=Ooh3yFt3X3f_7PcEZTRxbzNHfUILqxAJsAYpDG3QabT37qhKupFb8tYCqF5qMP9IcLtsayHbOfHDzZ9OYM92vVDSTXClv8-VpGBD2-RSdN3FoJ8j4i-UDrygmRD_qRHbYO7PSerNftSbsL0U3nz6oKz4VedfHahcEOCgZHuSsjbC7qGVyg86kFGwuiEklaVlu5t5ihr-PC3HppXqjNr-GVjVNeA5Thu6t1gmbYqrFTcdKgJAcx7awopHVOtzldgwb6iwi80a9Xt4ytE2ElbIA37k3MThIKsKWjGGE6BD25YJzMINpZ942CIrqtXB3vWQVJFM6h6nHxDTpFYT8eGOXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد مخبر مشاور علی خامنه‌ای:
قاتلان امام شهید به مرگ طبیعی نخواهند مرد و نظام آنها را به قتل خواهد رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/news_hut/67349" target="_blank">📅 20:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=e9QNADRIU7DvGH08h80HsGcb85GAmeoEz9Z7feq08wY6qyvgCKQCOV0j3I0PaiXfQJ4pcMGed0cXicLo0mmG_-Vo3MAgvhBS_FPaOGx0wsnovHINPTcoq20ZB1-Rnpr3BaLZNEsqQ197aZGVkTgDzo9VYs9W_R4-XqYxGzVDCtIbWKQA4kN2pq4Q2IXPaJivXaSIElUW-iYupXWc6uj41GEK3Koli20jz-6pLH3AEa4oc0ceDyDg3FmLrXpGqywDjcvhus6lQIc5uvkqGLYRGU97WzW-W72o_Ho931cVyxQuSOHXdLfrYyux0b2SqPME_e_skR4OMj6I9kimLBCuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5503b743a2.mp4?token=e9QNADRIU7DvGH08h80HsGcb85GAmeoEz9Z7feq08wY6qyvgCKQCOV0j3I0PaiXfQJ4pcMGed0cXicLo0mmG_-Vo3MAgvhBS_FPaOGx0wsnovHINPTcoq20ZB1-Rnpr3BaLZNEsqQ197aZGVkTgDzo9VYs9W_R4-XqYxGzVDCtIbWKQA4kN2pq4Q2IXPaJivXaSIElUW-iYupXWc6uj41GEK3Koli20jz-6pLH3AEa4oc0ceDyDg3FmLrXpGqywDjcvhus6lQIc5uvkqGLYRGU97WzW-W72o_Ho931cVyxQuSOHXdLfrYyux0b2SqPME_e_skR4OMj6I9kimLBCuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
قول میدم راه امام شهید رو ادامه بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ET0K2pTvdh2_72WDOvTMmVIQGr4NKss1hbEDBygUEnd7fwWOcbY16NE3-B-uLbvnp5UMno9nDK7zbckoaZSVRaAj3kb5KXAbwcqh3enbf26VhBqw1VUHjKoebq5sf0QT37Gp5O23e1fWcVBrY6aR74SHwPtoqx0xVCfay94FGNClqRjgor0lRACom3N-y44mDn0y8CqBNk_MZqD4ptRgUfSVXhyEUtx06q3BtlyWS-OnjHzizG-zHqdr5DgImhQ8AyxjkIVTRZJV10j1zv32-Z8ZQWzZB5oWeoDdiXYZ5l8ypMsu2zVUZkAJHv1LnI6rI6AJT7-xKe8IC7XLl2wu1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5djCapQrqonqHvkxK29FL85i-gIXhM_oate_qaOnlakFBsyYkE4Pr011yKxUdxGV3wKv7YUlue-3AN_Jq_tPdr9Mh1IWf810dCl8fmOSYBJxuFCtuxBt7_yvoO3dF_hK-Rhj5komyD-MrpXeFBRi4qkT5pW2pD_nDTDIBC6CNd3CntziyOZDBQ9mazCQ2rYefdWL2xlrX-KU-1jBVOZicvqlfus_dkGeKqVNfBhAulA7ejOqM3A8_kGTuM3btglAGKu97QfNDDN6BS0E_ch0pWHJVAMedBkEPGGOI-FJU1zHDw9bAXbfxLfDqZ5okanLb5eTxNpPX0Jj5atrkAPmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a975887416.mp4?token=T_rJ3vF-o89IUehsLlyxRQzuMsyASEeG_kTW6g1La28N8B141AI4lSLQ-xtL4EjpQSzxcukHu-MuXe4qkLFdF-p3-dJ_MhMJlHRLo_Pzz494M-r52vzJ0Dps7rrwZK21A51HpV5nAKTsUhg5KVONyHVMXjiwjNJxyxUmyvt5PZk93G7b1yU69Hrf5Ss-QYl5bdcSuIxHpu0J93ixEjwNBupbZPwPw6Yh7gdlYC4hTWvhY3iNnq7Fu5wmPW4Hx9Hxb0WZy6xSDwsieI_c4MW0jAr5K38D58vdygj5X44WqYH8E9Pb_VKNmYm3zHIKiz5eQ5SypKvRFfuf5zqlAue_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a975887416.mp4?token=T_rJ3vF-o89IUehsLlyxRQzuMsyASEeG_kTW6g1La28N8B141AI4lSLQ-xtL4EjpQSzxcukHu-MuXe4qkLFdF-p3-dJ_MhMJlHRLo_Pzz494M-r52vzJ0Dps7rrwZK21A51HpV5nAKTsUhg5KVONyHVMXjiwjNJxyxUmyvt5PZk93G7b1yU69Hrf5Ss-QYl5bdcSuIxHpu0J93ixEjwNBupbZPwPw6Yh7gdlYC4hTWvhY3iNnq7Fu5wmPW4Hx9Hxb0WZy6xSDwsieI_c4MW0jAr5K38D58vdygj5X44WqYH8E9Pb_VKNmYm3zHIKiz5eQ5SypKvRFfuf5zqlAue_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
حملات ارتش اسرائیل به نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=ZvZzqP_qndQYQZ6p6zftKV7rRx-0FdVSvVygTCFkuGZcc38Z0i9LM6mdJiRjbbw5t3oVFtuwDZMscXSXJCpCKF1XVFgrnc4JMctWg5poQZ-pGTYv0GikZ8a0LXWJ8MRsaWtYMt3dQ_evG1y-wzCA33s9f1cTrUkAuQYtG9P05GaDa6J_h1416RKFrZw-K2f6twMEtspRf3b2N2RIcryHoekcMg2bl_WuXlI9MdnICDGC0mJm_9tu_0Vp-kXQKZ69BxUIIef2IznhwiUHjZzVacpwi_1KX6dy7G1bvsvypENAyQHhMyfvtCoWli_o28mdmwO4CHsxzg5HX2ljlVJoyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4c05c580.mp4?token=ZvZzqP_qndQYQZ6p6zftKV7rRx-0FdVSvVygTCFkuGZcc38Z0i9LM6mdJiRjbbw5t3oVFtuwDZMscXSXJCpCKF1XVFgrnc4JMctWg5poQZ-pGTYv0GikZ8a0LXWJ8MRsaWtYMt3dQ_evG1y-wzCA33s9f1cTrUkAuQYtG9P05GaDa6J_h1416RKFrZw-K2f6twMEtspRf3b2N2RIcryHoekcMg2bl_WuXlI9MdnICDGC0mJm_9tu_0Vp-kXQKZ69BxUIIef2IznhwiUHjZzVacpwi_1KX6dy7G1bvsvypENAyQHhMyfvtCoWli_o28mdmwO4CHsxzg5HX2ljlVJoyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما در وضعیت دائمی جنگ نیستیم.
من خودم، به همراه رئیس‌جمهور ترامپ، چهار توافق صلح را به پیش بردیم.
تنها مسیحیان لبنان نیستند که از ما درخواست حفاظت می‌کنند.
دروزی‌ها هستند، مسلمانان هستند، مسلمانان سنی هستند و حتی تعدادی از مسلمانان شیعه نیز همین‌طور.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=ftuHmp5nW1_Bt2d4Dap_15e0sS0SlUM6cUuCry3STtbOvFCcFVLg8sB7K5LCy21XPi2jox4BpkbrSGaYIHOxqylUVn9CAgisELy9TDTeuZ-ejcooj8xbM0aFT6EwN_xzgFzgtgTNGMi1g7qlTJsirHqZgSCw3bdWF9byWVg8o0lLkNuuHCmYbcilBx1vO5QmyXr6ycp8Q5ZsugRaiShUdS7eY8bEuPqWk1XwaDi3yHc-9apcxlQmY7oq4FaBFnm5DVqkvqIce75w2-5BpLw5erj8ulwaiklXoI6kR_qORAWflm-O26WNhbQuDUT0OOTm4pz4RWjj54j0NXBhks4Rdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4244b191.mp4?token=ftuHmp5nW1_Bt2d4Dap_15e0sS0SlUM6cUuCry3STtbOvFCcFVLg8sB7K5LCy21XPi2jox4BpkbrSGaYIHOxqylUVn9CAgisELy9TDTeuZ-ejcooj8xbM0aFT6EwN_xzgFzgtgTNGMi1g7qlTJsirHqZgSCw3bdWF9byWVg8o0lLkNuuHCmYbcilBx1vO5QmyXr6ycp8Q5ZsugRaiShUdS7eY8bEuPqWk1XwaDi3yHc-9apcxlQmY7oq4FaBFnm5DVqkvqIce75w2-5BpLw5erj8ulwaiklXoI6kR_qORAWflm-O26WNhbQuDUT0OOTm4pz4RWjj54j0NXBhks4Rdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
روستاهای مسیحی در لبنان...
برخی از آن‌ها در واقع درخواست الحاق به اسرائیل را داده‌اند زیرا ما آن‌ها را در برابر حزب‌الله محافظت می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=pDs6a4dY4DEyir4Io_mPH2c_yGuHZfAC7xcNym4HOs9ToJwTI-kV8z-o6ApCj-eOtcUmHqHzOeGtXfAdfCE97AheIEa9j8mAhecAo6AcQiEgpRwCPyUmUj7BftrPf4-YCxasM_g0iweZVYe_BYiE-IYjhHp_q_WWq9xwniNfX0lfi5CsiVxsT3ukM69etjUXDCybO1564KhGR6xaNeGlzLQNKsDdhpfYSjR1LdTZXk4mODe2o3HNiy86LY1k6-JS6fFrDmh7b81v1_0KR2wUqeylOjzLfkJQdlgDS2dGmGl5_eCvjNKNUtZUB5Wj_Hdst5FmVHULgOH4zNxWzRjPFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd048f948.mp4?token=pDs6a4dY4DEyir4Io_mPH2c_yGuHZfAC7xcNym4HOs9ToJwTI-kV8z-o6ApCj-eOtcUmHqHzOeGtXfAdfCE97AheIEa9j8mAhecAo6AcQiEgpRwCPyUmUj7BftrPf4-YCxasM_g0iweZVYe_BYiE-IYjhHp_q_WWq9xwniNfX0lfi5CsiVxsT3ukM69etjUXDCybO1564KhGR6xaNeGlzLQNKsDdhpfYSjR1LdTZXk4mODe2o3HNiy86LY1k6-JS6fFrDmh7b81v1_0KR2wUqeylOjzLfkJQdlgDS2dGmGl5_eCvjNKNUtZUB5Wj_Hdst5FmVHULgOH4zNxWzRjPFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار تسنیم : نظرتون درباره رهبری مجتبی چیه؟
🔴
زن عرزشی : چی بگم؟! نمی‌دونم ما که همه منتظر بودیم مجتبی حداقل برای تشییع جنازه پدرش بیاد و حضوری باهامون صحبت کنه، ولی بازم نیومد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c05464482.mp4?token=vAfiQEeIBlH_OnUDVy7DMjeA83Dg8ipxo07cuHp7Ja2e0_DFv0cIMiNBTdTDeFHAjqq8VFgbmW68CNl1KXuQiXUj7b49SJUSmUTzpCgwBK-KSYAKx2GHKGLM-vsmiguFDz3TJt213br9eCwriwcwgUFMthBzyHJQDe95qEsIOFNhpXF7K8zTSkmmUcReWxA2vxx5N5lPx_s66JZqNzv6pLACWH1DLlJR4Iz3R0fCsrnNtw9-N6Sv-mpcPdeKYMriyKm7oev3ThGnoOJAoMAIToobUznCyhsQ_iDtWOFx7kXf0keK7FFYWdZHHY1be3tNE_G5Ixxz57JhSn69ePfZiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c05464482.mp4?token=vAfiQEeIBlH_OnUDVy7DMjeA83Dg8ipxo07cuHp7Ja2e0_DFv0cIMiNBTdTDeFHAjqq8VFgbmW68CNl1KXuQiXUj7b49SJUSmUTzpCgwBK-KSYAKx2GHKGLM-vsmiguFDz3TJt213br9eCwriwcwgUFMthBzyHJQDe95qEsIOFNhpXF7K8zTSkmmUcReWxA2vxx5N5lPx_s66JZqNzv6pLACWH1DLlJR4Iz3R0fCsrnNtw9-N6Sv-mpcPdeKYMriyKm7oev3ThGnoOJAoMAIToobUznCyhsQ_iDtWOFx7kXf0keK7FFYWdZHHY1be3tNE_G5Ixxz57JhSn69ePfZiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زینب سلیمانی:
شهادت آقا برای ما سنگین‌تر از شهادت حاج قاسم بود
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWfMuvNit0HsvO3Pxtlz12OvOMhduVo_V-I0vSVKlcTTMKxcjE04ifcggWR8TPpbnHnUCb2o3vtoPMQAuO90ppvBd-N78OKINmhGriabBW6YWkrJ3MSaY5qyVV4eMBohz_aj5lupTZd4CeNyvkOPKVyqC1f09R19eUIwEq1Rg1mm0ZHxBTKeu536PtvKgsI9fxt1N_GDvt6Hm7iOzt97rl0hDfrgiLrHOjK95KZ29GzP-vQNzgJgvaWih2WYAOSlrcIQyxD2t2SPykyJhFQp5mlXxLtyMQAY7MLDMIb1FfsZjj5wE7jCwemf05xlpfKjR0AHU6YbU0Z_3FEXDoitmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دفتر شاهزاده رضا پهلوی:
🔴
‏تلویزیون بی‌بی‌سی فارسی در صفحات رسمی خود، با انتشار بخش‌هایی تقطیع‌شده از گفت‌وگوی شاهزاده رضا پهلوی، تصویری نادرست و گمراه‌کننده از اظهارات ایشان ارائه کرده است. تیتر و متن این پست، با اتکا به نقل‌قول‌هایی ناقص که پیش‌تر نیز توسط رسانه‌ها و حساب‌های وابسته به جمهوری اسلامی برای تحریف سخنان ایشان بازنشر شده بود، به‌گونه‌ای تنظیم شده که به مخاطب این برداشت نادرست را القا می‌کند که شاهزاده رضا پهلوی آغاز جنگ یا تصمیم به حمله را به سفر خود به اسرائیل نسبت داده‌اند. برداشتی که هیچ نسبتی با محتوای کامل گفت‌وگو ندارد.
🔴
آنچه شاهزاده رضا پهلوی تصریح کرده‌اند، این است که سفر ایشان به اسرائیل، در کنار تلاش‌های گسترده میلیون‌ها ایرانی، به روشن‌تر شدن این واقعیت برای افکار عمومی جهان کمک کرد که مردم ایران دشمن جهان آزاد نیستند، و از این رو دنیا در برخورد با جمهوری اسلامی باید حساب مردم ایران را از این رژیم جدا کند. اینکه مسئول اصلی بحران، جنگ و بی‌ثباتی در ایران و منطقه، جمهوری اسلامی است. ایشان همچنین بارها تأکید کرده‌اند که هدفشان پیروزی مبارزه ملت ایران با کمترین هزینه انسانی ممکن است. چنان‌که در همین گفت‌وگو نیز تصریح کردند: «تمام هدف من این است که این مبارزه با کمترین تلفات جانی به نتیجه برسد… هر انسانی که جانش را از دست بدهد برای من واقعاً دردناک است.»
🔴
این‌گونه رفتارهای غیرحرفه‌ای و تحریف‌های آشکار از سوی بی‌بی‌سی فارسی در حالی صورت می‌گیرد که چندی پیش، مدیرعامل کل بنگاه رسانه‌ای بی‌بی‌سی و رئیس بخش خبر این سازمان به دلیل رسواییِ دستکاری، جرح‌وتعدیل و ادیت مغرضانه سخنان و مصاحبه‌ها ناچار به استعفا شدند. از رسانه‌ای که هزینه آن از مالیات شهروندان بریتانیایی تأمین می‌شود و با وجود ادعای راستی‌آزمایی، به دلیل نقض مکرر استانداردهای بی‌طرفی با بحران جدی اعتبار مواجه است، انتظار می‌رود فوراً نسبت به اصلاح این گزارش مغرضانه اقدام کرده و سخنان شاهزاده رضا پهلوی را به طور دقیق و امانت‌دارانه منعکس نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=XdIzk5SV8_HLdXs_eXSFNvnkYzFclTUcr3ZzKJ9GtkmJplea-yP8nFsSKbrh3b7Ds8wy1qPS-FRyE7HFte9JcIcBRpMU9B3cx-AsFCu8kPKoIVxZZ55I6dm4ARud0gqneYarMXn20fyFjmuZzthd8k69eU0mjkzJ3m0ZFSjKZ-iKk-bOtBpX1uGKfrbykTbgQ_cfrJaFqKuZEanS2Uv9xbFUUKYYAMJd76EU1eNvJmQGL1B7tV-vBGuW6XJXp4TWAoQgEr6vxvEilaNmk4BL4GVuViMJRG2GsIpiTwgChuyllCiYXa8OevJPvOU6AjXBDj5SFtZlBaWHG_zuYLJHCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7e9ec8c8.mp4?token=XdIzk5SV8_HLdXs_eXSFNvnkYzFclTUcr3ZzKJ9GtkmJplea-yP8nFsSKbrh3b7Ds8wy1qPS-FRyE7HFte9JcIcBRpMU9B3cx-AsFCu8kPKoIVxZZ55I6dm4ARud0gqneYarMXn20fyFjmuZzthd8k69eU0mjkzJ3m0ZFSjKZ-iKk-bOtBpX1uGKfrbykTbgQ_cfrJaFqKuZEanS2Uv9xbFUUKYYAMJd76EU1eNvJmQGL1B7tV-vBGuW6XJXp4TWAoQgEr6vxvEilaNmk4BL4GVuViMJRG2GsIpiTwgChuyllCiYXa8OevJPvOU6AjXBDj5SFtZlBaWHG_zuYLJHCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین آتش بازی تاریخ آمریکا در واشنگتن دی سی به مناسبت ۴ جولای روز استقلال آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm-J8mdXqDkBr_GYo_c2Dx4iJTRUUb5_JNg3BRFsh5-XoE5FFhzQ78pZ5OFEwayM-fx0qbqo0VSWFp0hQpEFhkrbx-KfjAeHdNjLAvqqt6_U-5qXAEh5FvYOSLJlh9NyncoUscHZZvN-5wBx_-8oW3LDWAspJMQQjc8I9xXgKdbh68vJa36n-k_RMVg99DBYyn9Q_QBDK4gA5Vq4XBqJ5T6A8LK989zJtdl8ZxkCtqIveLdquG--URu5HD3BpesH6_SM4P6x3XkfdH1WEyb0nKSDgj4IcpodW9RYWK93lLuj-t2iHa6BZpQhAWkweoq5LD7C5tvZqRXP-TFCo_Rnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=RZt5QIytLvpuG6rnPW9RDU69EnrDsQqVNlZH1j5iWYElfWhCzJ3JNzNwKBD5D5jvPLViL0Mw5BSI5dopAL3zifFnguIy2uuQZlHZ-iYHKz2jQSSilgxTcZe9MpT_l4-WbWT1z6FzNX-bXWdhXe66IOYiY1r9zUAn9GEncAFDu5p6LjTCfQHUwNVfHokTwhBkLdGx_I7Yt2SSM66QWtpebHfYOINi2jNB7zmnAAJ0ocVtuQho2Y7HPx6hIlw4AbRj2VIFBBGjqDA7ABtOxYjZDj1i8OPiTlEQ1Xu1FpQWQAdJkhO3kq1kaejiuVChqaJ-rTsx8LkHhl-CZ3QYliPBfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e644784ac.mp4?token=RZt5QIytLvpuG6rnPW9RDU69EnrDsQqVNlZH1j5iWYElfWhCzJ3JNzNwKBD5D5jvPLViL0Mw5BSI5dopAL3zifFnguIy2uuQZlHZ-iYHKz2jQSSilgxTcZe9MpT_l4-WbWT1z6FzNX-bXWdhXe66IOYiY1r9zUAn9GEncAFDu5p6LjTCfQHUwNVfHokTwhBkLdGx_I7Yt2SSM66QWtpebHfYOINi2jNB7zmnAAJ0ocVtuQho2Y7HPx6hIlw4AbRj2VIFBBGjqDA7ABtOxYjZDj1i8OPiTlEQ1Xu1FpQWQAdJkhO3kq1kaejiuVChqaJ-rTsx8LkHhl-CZ3QYliPBfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اگه اهل دعواهای خیابونی هستی، این ویدیو از استاد طِقه زنی رو تا آخر ببین تا به امید خدا پیروز میدان نبرد بشی؛
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67335" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imlaBmP8K5B94CcNALz1qLnopgVMnNhhP7CefwNXd94_raM1gkJcnzf6LgvOF748VqwOlXi5y8Jw763_f6lYIdzviBzrZvm5554MuY7HgC87d_x9hi-BMyq_k7SMaqrPdZ-dTLs_mAEnl1sqdc50tn2OBfvsfJCtEwRW_nlKrugNpLlaWjpoLpOZZvqpE8VFx77zgXx5FN2IJSJRJw_RfwyCgJ170w-gF8mTYLA3FF02GWvwNunJuTQ9-nB9IgrnUw5jg4QnmMJJA8mepfg-SAZD2dcKIXcQPFfrMULSdAsSMZYhf7yMoVl1xpSdKwKyFkM0cANdEIyQbPinoVq24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrSdbI3MRsl2wWIugJq0dRVlAXQW8fAYiacjo_jnWO6_FucEzIjs8MkV8551FR_d4Hd3OkESIoQbbKKLjn419RDZ9SuICgqOqKG4MGorkjaSR8Dsruh4cyQVO_PBhj7wO8QSvCQ92QwD3PqMl8ZjF5je40z5XzbIYunAWrfEQTmGDGO2wGfa5dS9tfOHQLeTlRMtpumS64yMM0QiVUs9w4dGmspgFHBIdIHkQFYLN31uoVSU_FszKWqe6ROh6hYTaaPN3AFrm5U37Eult-N5zNfhOkYnwE1lGSZyWhez4Pw5ziLQC0e9wphdPCOmCSn95D9o3onSODCAp4TpLrtYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgj0lbBM6XPEAKI75v5spsMaQIKN7JrXbzbrrSuDavPKpWCaaVZ_z8Z6l1KP_u0cpwZz6ETcTxBPIzMF3lcOi_7_IrhSrx7yH7VAJFVdSHVGvmfHsLoOs8tB8d3kpHUk1_W6SBUn5a_w2ScfN-QK4dKqMvr3N6KDsFqTLlTcVsxeQ3ewCx5hyVehKeyn4OHmGjhkUxYgT2_0cPu1_j0Y5txLLRk3pwzKiOG5j7N3WNptbhziuxIu0R70s4TivpuzCs3hKOsOOr5HGYp-YjPDWDC67vsLPvjtqzYoV2MXTnPmodBiBjEpAeuuMDLvcGb7nMtu1esq_y8kwiqvkZn7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm3wpwJ5qVzehFZpCrX61LV87mMqTgWMiN6NFVDshzyEfedzYp__FxZsKIvCUIceTn8mquCih7uqOq5qKP1vCYoGEu5EkR4w8SHKDc-PbPF5TPy-UeZ-vWHAs1fxOGLuusegCaP2sxdxmpCdZZoUuqHCW8hbbXppv0zQQxQ44weoGkZHRETjSJDq13MUb5UdmsVusra_JwGO4NDp5bORBbi8AIn6U2FbDmPTvNmSVAsWU3o7gXIEpzBs_ohEkHYGUavrehI4qOTZyRnm0_COYI6KAXlrpBQvvh8bL9pqVTs_QS_o5CUPPbt3sH_bcVImKBfImlpP2l1nmUWrtqkV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=rJAF-Laj9TZRlWWpFAD6lhTCQYGPWoRdJNa__hANYu72MdJn_32rGJ2goHHMcCiN51MUno1h-SgFuUJyXXgMj5TcxUqy19aQLwIRxr8_jC6h5w0dmXKKoKbM23QHeJEM9SMupx3fczgGZQtjjmepzWWgFoYDZL0gSdrfSEM8ari-qU4dxZ08w-IZaSuQWgWbJnw67TlH3LGThyHsiki5Rl-izsh0CtKvBYnsKTl0hwJliVH3QoBnFXR-tdNyRM8nE0or4KGBQr7pB0rQF0Ad_oB5xZSckh3WtyNbluyJYXQ_QjGLeuGo9adK_UJApcrw17AYBP40pImix4n9XgSruQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=rJAF-Laj9TZRlWWpFAD6lhTCQYGPWoRdJNa__hANYu72MdJn_32rGJ2goHHMcCiN51MUno1h-SgFuUJyXXgMj5TcxUqy19aQLwIRxr8_jC6h5w0dmXKKoKbM23QHeJEM9SMupx3fczgGZQtjjmepzWWgFoYDZL0gSdrfSEM8ari-qU4dxZ08w-IZaSuQWgWbJnw67TlH3LGThyHsiki5Rl-izsh0CtKvBYnsKTl0hwJliVH3QoBnFXR-tdNyRM8nE0or4KGBQr7pB0rQF0Ad_oB5xZSckh3WtyNbluyJYXQ_QjGLeuGo9adK_UJApcrw17AYBP40pImix4n9XgSruQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=rfcz84OVHs4SoZYKu8flPj6t0Q9tPJgn87Zyw_wH7xohP_IlK197XECIZtZ_5pqxSZ_FinwkWGV-RsOev_PlA_CMxm1OuIfrvnKsbwhpD6NGDt5Nxx7cFn5GqkWufksL9sJ4LU8_dcb1nnMrf0TB9uQXdxNoTREpo3_ECc7vT_BUAC6j6saacrdyNlW3Zw2NykVEB7dqCX3LTKS_v8cTYyhtppM5ufJDYqz8MK2bg2kRiHRrrwa8vhr8DZUbSuadoPLGnkcyoWz4-_691XYkq0TqMwCIzYAPpkKVmOKuTkIm_r37-D-4t7BJlPVcUq2khZ0jHA3-noFqRm2aYAmjag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be756a04.mp4?token=rfcz84OVHs4SoZYKu8flPj6t0Q9tPJgn87Zyw_wH7xohP_IlK197XECIZtZ_5pqxSZ_FinwkWGV-RsOev_PlA_CMxm1OuIfrvnKsbwhpD6NGDt5Nxx7cFn5GqkWufksL9sJ4LU8_dcb1nnMrf0TB9uQXdxNoTREpo3_ECc7vT_BUAC6j6saacrdyNlW3Zw2NykVEB7dqCX3LTKS_v8cTYyhtppM5ufJDYqz8MK2bg2kRiHRrrwa8vhr8DZUbSuadoPLGnkcyoWz4-_691XYkq0TqMwCIzYAPpkKVmOKuTkIm_r37-D-4t7BJlPVcUq2khZ0jHA3-noFqRm2aYAmjag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمهوری اسلامی پس از ۴۷ سال در مهم‌ترین رژه‌ی خود حتی به‌اندازه‌ی بند پوتین‌های ارتش شاهنشاهی هم نظم نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac4BNJdKFqVIJe_cfPKqTKvb_EVAOEg66WXMcbywQo9D5t05-Mmx_p2g-ODN1agpc9qk3-E7xBq7rMkF9dFerR13KLGullf06zN2_iJD35ANN7mQQvMbxK8iXpu2eG952_SipvwMhUIyWfr_6AWX0TvMfxieCU6qz8TXf_FFa24tIuzt7atsz87ois5SZ9RCQNaLJFOorJPD58A6w9RD5aBMWosRENSXpT3B-jrPFtwA7tusnklUEG2EEUl9byazNkeIxfyv8_jxx_FcW7kRnzoSiML_T4XA3v-MUQVRCBAqa0VkZHUaWqJwy7Et5anU43ECpU2ykIjWKCb4j7ngTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcMx5yLa1xYvZeTVsGvQhvt1HAgp7dN2g0mcZFkR0uBJ0L2Yq_cOZqj3qokmSekbp5qNervO3E7hJbikaPmWQ_-CAv5gjdtrHwy9SOi0I3nTI5RwJ765xqFTGpucSEwcvetN3jAPqyoz4EVtbBYzjElHkquSRHWT1gYyHFufkXJt_QpbwFb9J7YEqJGXbyfrk9Vj3sGB_wyvTfzJn1eqJV_K_VoSbpm78i7ZUduccoeBVuUR-0qPDqQt1HoYXkbWkJ-sTAsVf3v4B1NdrnOwQ4FIfs84krE0j2UirqX5c3ReDTLGvClGi-gURFIvhq1pvsUx0v-Aj_AIBw1UJoulYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=BC53Rui0MT_KcmpSXEfzR1oxLypfqESXk9-IF0SPjyvoZwbEMsexsmwPLzq8ITRdupRpGyhV5l1pHbDmuC_D_nVP29LrvXkansLzM0tIvpCvFwbzeiL5Sbw78f51pslUlbW5SX0X2AWMqcQSmitX8OlFQFYk-0HCR-WuIHAIBIQng7vlG2Ohk0RyYNnDqVipxFeJVHLTGRjcshpvf4Uh2pqvcIv6s4BCLs-1HFFrtG2Z7gIG2Ev3KRcMVDYvk5X_v2N_RoWefJybk0bBF8nEAk-bHAA7hw1Scwz2dROuEraNKASy_Vjm7Jn-_2fPsFGKsIrPETO1AQbdmwsawy3PLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=BC53Rui0MT_KcmpSXEfzR1oxLypfqESXk9-IF0SPjyvoZwbEMsexsmwPLzq8ITRdupRpGyhV5l1pHbDmuC_D_nVP29LrvXkansLzM0tIvpCvFwbzeiL5Sbw78f51pslUlbW5SX0X2AWMqcQSmitX8OlFQFYk-0HCR-WuIHAIBIQng7vlG2Ohk0RyYNnDqVipxFeJVHLTGRjcshpvf4Uh2pqvcIv6s4BCLs-1HFFrtG2Z7gIG2Ev3KRcMVDYvk5X_v2N_RoWefJybk0bBF8nEAk-bHAA7hw1Scwz2dROuEraNKASy_Vjm7Jn-_2fPsFGKsIrPETO1AQbdmwsawy3PLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=LLLTBSTq-Mngs-nTOlfxsDwOORa6Hl7N6Z9Lb4wekJpBk6-__0pXtcBhmlZs3s1jdaLC4s-atVEoC8U-LOtm21uNl7kSQJ3FQ9M730og9wCLl3U3o1VHcNen2ZrKP-O4WhZ9-lfy_DNZ614jU7behYNI4-G-XqzqgHJp0v8jJirfNtsWa0pd43bGftl1zfEnMd9XAEmgxxXlU7prNoZIE4rkAYqsFDxdhXis_xmFP3Kdh8XRIawVf0_9TAaARshenx0B6SpWLFwYtr1UhLL8n3a2ycvpWda_GYicCMfXQFRgs2v9BjwcNphCc32VFd6G-SxSoUwUthfM5f2gbudN5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=LLLTBSTq-Mngs-nTOlfxsDwOORa6Hl7N6Z9Lb4wekJpBk6-__0pXtcBhmlZs3s1jdaLC4s-atVEoC8U-LOtm21uNl7kSQJ3FQ9M730og9wCLl3U3o1VHcNen2ZrKP-O4WhZ9-lfy_DNZ614jU7behYNI4-G-XqzqgHJp0v8jJirfNtsWa0pd43bGftl1zfEnMd9XAEmgxxXlU7prNoZIE4rkAYqsFDxdhXis_xmFP3Kdh8XRIawVf0_9TAaARshenx0B6SpWLFwYtr1UhLL8n3a2ycvpWda_GYicCMfXQFRgs2v9BjwcNphCc32VFd6G-SxSoUwUthfM5f2gbudN5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=ma0O_z55Ngsj8lTZTmsmVD-xNAMwYGzoCY2p3uVuCOVtWzl2mpy2V9fExax8z8JEPmTLczGyhqwD62o_Ph9g8rP3bNUD6mlVd6oYS1RnF0W5JO_g1WrsyMMn4jDoIhPl9HQzyywU4lMZDum3rM44vUq9VFqmucSFiEI4eAUX3xWW74epVHxCNoGhW3uztXSgwJRLlBgk5RHSzvu7e-488_eoIlCp8klLRIZxvfQS-_puYThlP_mD2WDahuyMQaaX67TBAgwU1pUQLMhzoyqxP0KzKMxpUUM8gQ_0rqWgLO3kQJdzXx1guYuamVWPLJuAAgWtx86mTmoooBhFLWg4hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=ma0O_z55Ngsj8lTZTmsmVD-xNAMwYGzoCY2p3uVuCOVtWzl2mpy2V9fExax8z8JEPmTLczGyhqwD62o_Ph9g8rP3bNUD6mlVd6oYS1RnF0W5JO_g1WrsyMMn4jDoIhPl9HQzyywU4lMZDum3rM44vUq9VFqmucSFiEI4eAUX3xWW74epVHxCNoGhW3uztXSgwJRLlBgk5RHSzvu7e-488_eoIlCp8klLRIZxvfQS-_puYThlP_mD2WDahuyMQaaX67TBAgwU1pUQLMhzoyqxP0KzKMxpUUM8gQ_0rqWgLO3kQJdzXx1guYuamVWPLJuAAgWtx86mTmoooBhFLWg4hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=cuSDC5fFmdhVJVSvrT8QzB2zHw_pRC7f5vb1JFm9-4fC969a07SYMDmf5R7tmE9PVydF8YnoFXpo3NF3HeGqCpJgMiohjTZdR6qD-ZKLbDnVGd0Hhq0H5B494G1GQlJnX7luBMae2tyO0cCI47SKaijJ3u-JYjoIaH4BKV5HUpB0_PlROSF_uGSvGVQvv6gg-23C1H47rtVDhC9pDIJo9yPEk8LB6KNna81BSFI1SpQY0V0-Gpxi4dNEYS8AROjpzxdkBI27xD9x28yFxy86WwHQh5DT63p2-e1FX-nhHSenrmvh8koEWQrAK-v1Hcz6AjG2TEXFvlXapKGEgKIvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=cuSDC5fFmdhVJVSvrT8QzB2zHw_pRC7f5vb1JFm9-4fC969a07SYMDmf5R7tmE9PVydF8YnoFXpo3NF3HeGqCpJgMiohjTZdR6qD-ZKLbDnVGd0Hhq0H5B494G1GQlJnX7luBMae2tyO0cCI47SKaijJ3u-JYjoIaH4BKV5HUpB0_PlROSF_uGSvGVQvv6gg-23C1H47rtVDhC9pDIJo9yPEk8LB6KNna81BSFI1SpQY0V0-Gpxi4dNEYS8AROjpzxdkBI27xD9x28yFxy86WwHQh5DT63p2-e1FX-nhHSenrmvh8koEWQrAK-v1Hcz6AjG2TEXFvlXapKGEgKIvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=sNnE5Ak1MQjff_7gISjjUBr04jiuSF_nRDO7DkqxSrvKtr3fbnzmm2U1QgBYS7fW-SPYYOBiuls9yQf1RRT6OnZhhpkmcwIQGfutb8eoiqPQQV5529223-a-xoUxRI8G21GOCj8_LT4WHjyILRDfeu6K1SeDSrK5odTJxhKlHSYzq8hYlUjXgDHkOdOiMooDN-h7j5vqMyo1MzbpBsTQ2yWteMqFo3YxtXxtEmF-uuanNIh00kggDFuLh4KVR0Y9BP5D6EYkMii4Tlhj5_lBa7pM3rcQcZJ6PLkCwcemq0glIbRGDQsO2gLwKRqnNu9BiNEautJx5NGS3GznMGbmvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=sNnE5Ak1MQjff_7gISjjUBr04jiuSF_nRDO7DkqxSrvKtr3fbnzmm2U1QgBYS7fW-SPYYOBiuls9yQf1RRT6OnZhhpkmcwIQGfutb8eoiqPQQV5529223-a-xoUxRI8G21GOCj8_LT4WHjyILRDfeu6K1SeDSrK5odTJxhKlHSYzq8hYlUjXgDHkOdOiMooDN-h7j5vqMyo1MzbpBsTQ2yWteMqFo3YxtXxtEmF-uuanNIh00kggDFuLh4KVR0Y9BP5D6EYkMii4Tlhj5_lBa7pM3rcQcZJ6PLkCwcemq0glIbRGDQsO2gLwKRqnNu9BiNEautJx5NGS3GznMGbmvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=KyANLv6MmHrLnv_kB0cCnC5qlMI4IUSPkv2kKoYnWzkGnJcbvKiPS4HzBp7jYgA-p27km-VwAba4JAgLTQERdzFMBZJ-oWQDgCdyS8KRMkcbCbjNtpM0lqQehN368U9RiXxlz00z2L_vEvNniVFWgHb_CWec5-T3nXFgSBNFvzKA_jrYC9zhYiSPPzfC7j5sOlsvGjsHZlnl8ZlU4KUZwZSkZzfN2eg5-SLi4qfY56vnH2ga3chdaR9A08bTavdNcyQnwE5Zq1QKcTVc1Rm6jtyg3t-0E8usdqGzPjGc6Sxzoquuk2_2rdPGOQhJu4SZwSos7fyfhKdmha-_-ZLu8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=KyANLv6MmHrLnv_kB0cCnC5qlMI4IUSPkv2kKoYnWzkGnJcbvKiPS4HzBp7jYgA-p27km-VwAba4JAgLTQERdzFMBZJ-oWQDgCdyS8KRMkcbCbjNtpM0lqQehN368U9RiXxlz00z2L_vEvNniVFWgHb_CWec5-T3nXFgSBNFvzKA_jrYC9zhYiSPPzfC7j5sOlsvGjsHZlnl8ZlU4KUZwZSkZzfN2eg5-SLi4qfY56vnH2ga3chdaR9A08bTavdNcyQnwE5Zq1QKcTVc1Rm6jtyg3t-0E8usdqGzPjGc6Sxzoquuk2_2rdPGOQhJu4SZwSos7fyfhKdmha-_-ZLu8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJKKjAZPMdnfKhz2__gcVjCP81-6WOnDym_9JiH9qUqPy7ySkRgJ450GDHxHEJvbR2d2fTf1iBZ_IlJsoXsaG8LAtYF66Rm66iXWXDQe1735iR7Js37SUmKSKK5IeGufHbt_yIsVjG4hXKqNi0jLU23vYB008YBsWupyX5erA6NPCSZiDhac-1HYgDTIIkJXEkUWDHlNdCctDeYRNY0c_iiHt3-dQbBz9F41_HioXYuinFCwJCFeoSotuEIulVeU50CAyz2ogpbME2HNsXc23L4jQbDmfWmhYldLoOhiNydhPRZ29gw1BbtWU36hEh_YWfQCjW90YHGK6gTarL9yXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fDq1ieLc3NozN5I-57PCNRAJeQlZ5d1uGjE_M5CnV8iFbc2l_Rvn58c38vL50aAfX80wsrb0WO4lYuH0EnUyyvSBBdwQEnni--hALfnms02MXEVbWyT_F_EeP3rJsPP2VLtQGf14IX2Fbjuk19Jdu22oDoGk5xwdUP_Qsq-U18mAXPMjnuW-uO6fElvTFSzYGVgdK8oAGn_fmoEwcK7KooH_nuxqocgTz51mA_mLUsNrKMoO3KvOicLvsGKtVTP0At1orLGm31kpOHhHePqOwpyqg_KbmF4VM8nVlJwOE2ZlFApzVI_uMjmSfj04Z2ZAqKQXuqQix2PFVzdGyaV_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrRsjTOag08CwXsGtT0ulVWxdQS2SB-CQziOK6TiuEHghzWTuN5wD6kvdFKg-YhdlO3Ujy9RK4IGyO2zPKQfCwYA_KRmK_Iyg8p-M4HXiaMebkEQb5rgouvwCQr6hu6WzhToJd37VHLi--igWfWG-W-T-KTT4Q2waOXhSgX42jHk-Dn8TYbqoD5yZMQv9gmMO_zSaIO2ituoof4313HCgdTlaDALPtMV86qF5ZI3yqKum9S7pfHvrsvUQ1pm9LQ4g7lExC-lHpWpCCcBmqxoaIaXKD-VmH81e0OOfDlNYxEXP7_burBFiE-KXZKFf2ONtTEVtZUCuXq7QesdwxCZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=Ywc9ezL6eJJfQmw2eUusz5uQ3TUiUQubEdIGLwBQxjjm5jRVk8KhLPxXh9Eiq7mel_AQjrkSicrN5wFYcizeu1hFvIV8qwM8EYJXWzpEIGJaANrGlT7T_x5QXLEj43aSmEd9D66DGFyX5ivJeF_0UjXmsbBE-Tmy-XTaKhvhKV6t5XMawaxyeS5qxSYKXsBRrrdajJTCfYBHzd_0FAuIhh_LEvSZWX99BRcJD7xisHELv3-fuL2Yi-_7-LboYwxNTOgP5pJqTfp4KzwcU0b3BMUtEmcCMocKb8W5sQ3Q0onlNV3BV51k6yi-wmFQS-wdw1NndJddoD1EvwtfeqdQyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79806b6dec.mp4?token=Ywc9ezL6eJJfQmw2eUusz5uQ3TUiUQubEdIGLwBQxjjm5jRVk8KhLPxXh9Eiq7mel_AQjrkSicrN5wFYcizeu1hFvIV8qwM8EYJXWzpEIGJaANrGlT7T_x5QXLEj43aSmEd9D66DGFyX5ivJeF_0UjXmsbBE-Tmy-XTaKhvhKV6t5XMawaxyeS5qxSYKXsBRrrdajJTCfYBHzd_0FAuIhh_LEvSZWX99BRcJD7xisHELv3-fuL2Yi-_7-LboYwxNTOgP5pJqTfp4KzwcU0b3BMUtEmcCMocKb8W5sQ3Q0onlNV3BV51k6yi-wmFQS-wdw1NndJddoD1EvwtfeqdQyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمعیت هموطنانمون در تجمع چند ماه پیش تورنتو رو ببینید و با جمعیتی که در مراسم تشییع جنازه علی خامنه‌ای اومدن مقایسه کنید
🔴
فرقش میدونید چیه؟ ۸۰ درصد جمعیت در مراسم خامنه ای اصلا ایرانی نیستند. کلی لبنانی عراقی یمنی و فاطمیون افغانی گرسنه رو با پول و... آوردن بازهم نتونستن مصلی رو پر کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBmHBZEDtk6vawUGHKOj5OK_4y26ViC98_XWZFOCOdZ9oRU-FJaxrXByNzazfuW2DePuPgKYqzqsoEsTmcvXqVj5Gy95VLBvqZ4cAg83VqpqEK7jh1ti9OebcgwGzh8HrPFyR3KaOHb_xtJF6cEGdCiiMWUQK8RLE1oN8q3eyPhirzl-B54OXQJ_ZtB3m28BWucv_XFRQdtdvuv7MVTmyeLtnXvrbuj1c6FTiEusRmqwN73aLZveVTFUCqW-2CpbP95zrGnGkWvrvJwxs49KLbjWeXfjE-G9hY53FwYdkZxzTjFwpICvQed0tQTWtSyEGfVRI09OtBzEi9tGimbw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=HlniYYJgnbkgIIF8nsjNzQKGDxwqYqreJln-BYmb1BpIgyG2EZ7oREcDcZ61tUyLwb6HIbLml4j4r1Z3NcP0tWd16lO5eqUmoag-xrfVhI6LemywtdYjUsxAUtokl5_71u5aovmMAMqKb-NxjUzMaOIEbyDi7HityPbOdOdVhT8wTRLsktVFR1ULp91qgyo_b1ThpGjCiJJ5N5gzOn1qwMBfN_IzzLrzrt6Oi4-8B3e6UPOVoCedysDU_P-h5iivCvN4m2AIbsC6KyncUskbugC8iBucK0goEacmr8Z3uqSWZ_coZQPdwGKULG3cNkqtahvxSLAWUIALc1fEC1FWsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=HlniYYJgnbkgIIF8nsjNzQKGDxwqYqreJln-BYmb1BpIgyG2EZ7oREcDcZ61tUyLwb6HIbLml4j4r1Z3NcP0tWd16lO5eqUmoag-xrfVhI6LemywtdYjUsxAUtokl5_71u5aovmMAMqKb-NxjUzMaOIEbyDi7HityPbOdOdVhT8wTRLsktVFR1ULp91qgyo_b1ThpGjCiJJ5N5gzOn1qwMBfN_IzzLrzrt6Oi4-8B3e6UPOVoCedysDU_P-h5iivCvN4m2AIbsC6KyncUskbugC8iBucK0goEacmr8Z3uqSWZ_coZQPdwGKULG3cNkqtahvxSLAWUIALc1fEC1FWsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGJWzWfEGRFtNojIce4DhmOVyuNlWZM3gYTbl_BpehFwyDU0lqpgIu-76TG3u9WGdhtKJcBH_w3W2sc4JwEuaGEvIQKV7ek3ZfSMidKO4LZG8Gk_xPsUQEgh3VF6HfVwwYA_4n5h3kEDY4_o9KOynrl9wrWJqlxVBxmoPKc7ibbCOLl5AnyffAYk8qblQWTXzxVRUqBYNEaDXGhy0pFzC4ApzB4dzqorSunb7Cu48GClbDE22cI4BS5NsqwirmGQkHJQ_zviKUSNg4SNWooTi0sNJe3qhqBWfnnjd3w-C3FfJsjICm__b9UIIlEKUhHSLOw8V5eNN9Cr1akhU58ZqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67309" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67308">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=TblJHQUXDYXDbDRlkpwkcPAKWJ7WsKTLDUOcU76jGimvdfXs_bqWb_i_caT3zkSTpK5ldfEmOiSk-23THyAqF2YW2ttiOjzyZqg3Sh8pMx5cMIEwnwdYqMjmJcO7QRMOE0BNQWyWimEclHQdmNLI_HBQ_YysRlPfibU7iAIFvUdLkB0_VsiC1UTyQDS-pY_vdYEg7VH9I_0Y-vWK6pN0phDorLCCKdzmYhS1I2PDGKOVc9x5asAilf929QCurDLXmGmiJrUHQttZLHlW3zlC9NtrM9GPuMoxIc_W57U2UoWXVIoEs-rT8m0886W-LcT8pWgZ9Os5rW7_reBA6iZxCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=TblJHQUXDYXDbDRlkpwkcPAKWJ7WsKTLDUOcU76jGimvdfXs_bqWb_i_caT3zkSTpK5ldfEmOiSk-23THyAqF2YW2ttiOjzyZqg3Sh8pMx5cMIEwnwdYqMjmJcO7QRMOE0BNQWyWimEclHQdmNLI_HBQ_YysRlPfibU7iAIFvUdLkB0_VsiC1UTyQDS-pY_vdYEg7VH9I_0Y-vWK6pN0phDorLCCKdzmYhS1I2PDGKOVc9x5asAilf929QCurDLXmGmiJrUHQttZLHlW3zlC9NtrM9GPuMoxIc_W57U2UoWXVIoEs-rT8m0886W-LcT8pWgZ9Os5rW7_reBA6iZxCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌هایی لو رفته از ابویسانی، معاون وزیر اموزش پرورش حین گفت‌وگو با دانش‌اموزان معترض ؛
دانش آموز:
نه اجازه میدین تشییع رهبرمون شرکت کنیم ، نه اجازه می‌دین پیاده‌روی اربعین شرکت کنیم، چه کار مهمی الان دارین؟
+ ابویسانی :
اربعین بخوره کمرتون!
دانش آموز:
ما می‌خوایم تشییع آقا رو شرکت کنیم.
ابویسانی:
برو بابا تشییع تشییع..
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaWa5P5yz7WIT9awWW8sCl15M0BZ1QK0AXhRTd-rhEgsi4FsiIGvPSS_5mn4sxe4pWwMpJyFEysU5YIA83voCj34hVwum8i0n3QYz1EkfCnmgWSr7K7SpDUG78DRTrI6YYETCWM4yOPSCpzSTEX2MXYM3KXs4amAlP6pzSbEJ9Ws8-eHx5EuxbVZVHuS-pV2mv7Q1SFDMfcznMKwc5gmpaVTw1EmZcZekfKTiO2KZZFAMhRHYi8fwORm1gvefmU7MQ8gA-334QrFtcPBF7x7Lff5H68bFIPBJul3u4Qm8OJ_kYuyynXxeKgG3k4GLdYYhWp660M4ucVWo418mXrgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=Zp_ohKaYCXU7fGx6SrPSbb9kxByn71vPIS220ZfH-4Onp5spji6GhRKCttDr1oWV4HlEcAUu_B_L4biBjiAjc4amsjOSzagSw64xXboa6fCNs6__AQ2CaCn6uIPZAAnjcQ9APBycBPzKpOwzMQN7PzucHJ3k0gHi5hK2OcfT3lqsExxH-YisvxuvTa9GVfgsHvaifOUjcsV4txFHrzDeE26jF_lDmL3Tz9Gt9yFLGFzmAivkaq-LnfbIklPDs4jfoLU5NDed5hB9nRnCfqOi3pGtGib-Y02DbP2b28K7Ufk8f-CgBOeTSr-7r6_5jAMA4wTcR9p75_ZdODiQUfnAfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=Zp_ohKaYCXU7fGx6SrPSbb9kxByn71vPIS220ZfH-4Onp5spji6GhRKCttDr1oWV4HlEcAUu_B_L4biBjiAjc4amsjOSzagSw64xXboa6fCNs6__AQ2CaCn6uIPZAAnjcQ9APBycBPzKpOwzMQN7PzucHJ3k0gHi5hK2OcfT3lqsExxH-YisvxuvTa9GVfgsHvaifOUjcsV4txFHrzDeE26jF_lDmL3Tz9Gt9yFLGFzmAivkaq-LnfbIklPDs4jfoLU5NDed5hB9nRnCfqOi3pGtGib-Y02DbP2b28K7Ufk8f-CgBOeTSr-7r6_5jAMA4wTcR9p75_ZdODiQUfnAfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=kilY-5eiCUXCKOCnXLui7_3fEYeS4azFpfRQRcAXX7914e5wptgYLPnFlP7LN9iRJR1wbm1MsLuuPkJRo6TnsQSKwflZzVlo44k67xoGyTrPyNb1Mq4LZ2Wajxq5TFk7WTStkY3t3h8jhrG00W5VCzkDP8awvsm8Ok6d0A8cWPsUPjxmzF7RDqyGtYGX8v7FzqDQaQywFbDhrQpLkjqD6SyH3u1vNW36XIM2rFSo2kn_YgNE7dC7nuWhyQRgJpqSWm8Pa2a3Rxf22uwEyvOi3Momu4xGFsJ9fRq2pqPqUJe9ghaNooFBo2pegHLRHpeqbyPHQepRpR8xgi9ba5HUxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af68b2c3a9.mp4?token=kilY-5eiCUXCKOCnXLui7_3fEYeS4azFpfRQRcAXX7914e5wptgYLPnFlP7LN9iRJR1wbm1MsLuuPkJRo6TnsQSKwflZzVlo44k67xoGyTrPyNb1Mq4LZ2Wajxq5TFk7WTStkY3t3h8jhrG00W5VCzkDP8awvsm8Ok6d0A8cWPsUPjxmzF7RDqyGtYGX8v7FzqDQaQywFbDhrQpLkjqD6SyH3u1vNW36XIM2rFSo2kn_YgNE7dC7nuWhyQRgJpqSWm8Pa2a3Rxf22uwEyvOi3Momu4xGFsJ9fRq2pqPqUJe9ghaNooFBo2pegHLRHpeqbyPHQepRpR8xgi9ba5HUxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم خاکسپاری رضاشاه بزرگ در تهران، زمانی که جمعیت تهران فقط ۹۰۰ هزار نفر بود و بیش از ۲۰۰ هزار نفر در مراسم شرکت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHeGj41NNLtAKCV0Rl6HlXXUdiFIltTUQ8e72EgTp0ptuZ3GccNVcU1xQNirxCHDZTnOwJdOfSU8hemf1ZRLwgXbe_8e9her2O567EjlyqYkz78_02DMnNgOP8KcLCgIdvn_s2c5APnyRKBvoBdaJNgwcG6nW3CVvC0Uw9-n14_Y9vdMFR2Djc4HVcx8sjDbpWdRwwwH2J1gbJRrq5HN4SbIw3QXrqIh5idstNaJm_ZCuHWAstjbkQzqIY6fkGLwt2g55hva5S21y_aT-58YvWPhEpmFP3I4ca6SW83uFnqN98SLdw-RwqomMd9PHb9_kJF8PmZb9i-PRTZIPo8HRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxmsshQ6yQpWtugMrbdiP1QPKkuBYbghoWKtACk58JwMSo2tQjPPttnPamL8a-b1tJFGhT463X26s5KQcoofomTRuSEH8CWCZSCtzP2THl-bqvd-bxPwIv77l-Uh1dN_zjDVWSpp0VeKHH7IQVsThA9hk3UG-k8boSttv5mq1VOyEsU9gj_qdCquiPyjIpWitr8aXJCeSSj5teJ1NnEXbg_gKE2VK1gCVwgJeOuY-zzyYEYb090q2fn-La2VwxwTQ8rXbVihprC3IIU0GUYHLDYcyogRXG2nCfP8vparZRbH2XBL9zs5CdngyK_yuUyjzUYX4RprIdTPa1DNoiB_4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZAwNoYuIekupob6a_cUav3XDYteQdlECaUFf44rshBgvO4rXlv2bjwdK9A2I72q4LUE8MglAdm-VDaZKyxjwbfmKeZbJSYzXkrH4PqhZwi5v7Ox0hdBSvjY1Oo-qhkPic91WtNCRbUKoMGRNEaMvVCd1xJNNy8P6_bXXrqs5tAfpFBpTfCSNCbLql39LyvviEz3JSVI8upbFUwGQ1N7iIqV2HnW0uDqbe9s81LjhyzaL28au-PrxqNfDDOO9px729RC8LLmf8zut4Lp1BmtvuaxhHP3tWdKesS-muOVp80wsgVaqqTfILSuIKvl41MqCJcdhrpXdHu3fRAdatRxfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=iD5o-aeddTctEghWUJQximSNUC-ZMJhgimJPlzfichPITlG1qL75KIBqhrbWEMB81usWKASBWeDczPhVcF1cxfZivBG7oV3b-htTEtpjKKEkqsFUqXdVJjtyWD8uFNabjEQ6hgFNktrQ3Jm_04OVqtKd6vCJRxtnOzTs_pn8UnJwVu3X-1iECQBTfWqK6YMs2d1Mg3A-DmgkPJL4eEEC4sgbM9Ff0ghXAl-QWhA2jiS0ed3r89ywd6kQ7MTYImSK0uW7GA0f3hGjfHw5j0PVnyzxxjdP8I7MPWusjCTshhOHf76MZ7jMjedAerxQe-Ens5i0awMlAJnsiq6isQwCeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=iD5o-aeddTctEghWUJQximSNUC-ZMJhgimJPlzfichPITlG1qL75KIBqhrbWEMB81usWKASBWeDczPhVcF1cxfZivBG7oV3b-htTEtpjKKEkqsFUqXdVJjtyWD8uFNabjEQ6hgFNktrQ3Jm_04OVqtKd6vCJRxtnOzTs_pn8UnJwVu3X-1iECQBTfWqK6YMs2d1Mg3A-DmgkPJL4eEEC4sgbM9Ff0ghXAl-QWhA2jiS0ed3r89ywd6kQ7MTYImSK0uW7GA0f3hGjfHw5j0PVnyzxxjdP8I7MPWusjCTshhOHf76MZ7jMjedAerxQe-Ens5i0awMlAJnsiq6isQwCeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=jabqgLV8mJ8j-Ax0VEUqJCwXZYRyKqxiz0u1Lpn6d8zKN8fsPoqFITSn3_tNI7aVOT9FADEKnB15gH2ylSyZK51-FkOgGQbLjDz-L4xfkvwEnPqEIFAsb7nqFHyKuzB1J8NnhgkwrU543Al2HMtZ_PXfIMaKprZK_OL5sItEkD6BycMGfoP78T8AOWNHjS0rM4MVDJnP4EvZO2YfFIWrB3X_ua3bFFuaMYG0yE0cqqnNXv2f0OrPNovUoyeQSVwt0NH_NMqc6z31VlZ8cmGdF_REB26WU4E555zfNP_fvplrm67sPOU0vg7Q7Z86t6Bjo-UEYYddGHNeYE9AjCBOwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=jabqgLV8mJ8j-Ax0VEUqJCwXZYRyKqxiz0u1Lpn6d8zKN8fsPoqFITSn3_tNI7aVOT9FADEKnB15gH2ylSyZK51-FkOgGQbLjDz-L4xfkvwEnPqEIFAsb7nqFHyKuzB1J8NnhgkwrU543Al2HMtZ_PXfIMaKprZK_OL5sItEkD6BycMGfoP78T8AOWNHjS0rM4MVDJnP4EvZO2YfFIWrB3X_ua3bFFuaMYG0yE0cqqnNXv2f0OrPNovUoyeQSVwt0NH_NMqc6z31VlZ8cmGdF_REB26WU4E555zfNP_fvplrm67sPOU0vg7Q7Z86t6Bjo-UEYYddGHNeYE9AjCBOwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyVUxyk7TrgrSEAYOADH2xk8yTjcwFnIWTQsvQrANFDtfEajn_4j4Cs7YTywK_P4SK1_AQsQXzrjBif6YkKheLqSaxWvbXbe0Hisuc17HhHnoN1vwaVtlgYX0lIH85ILmsM2f4yRu032-LClFH37lA-mylAFbVZTIDYDz_iVelKRaRkZEvWMBcuHWbkpcjhbDM0jLWyV1PkWjhC8OfOaIkBF74lUV-QxT2e_nwJ0aq1XuBhc7E4a980tdWHuwh6CacUAfZGUGszLRWynsBwhlw8COV2KZf4CsbJIh_dhIbHUwNim7pNGzGYMQjo0oW6fRIjFsrDewzepBrU5ORTVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POp7qJqFJyndRRFYDebR4Hl1PNrH2hBraUK_3atICcLzK5shrr9lZhITkPTup4DuQrjmqlO7ht4ZZSmUSAxPZGPApOaAfsS-9OPx1hraiDz8EZihR71iMYOoO41Ci7LwnGIqoFn6PoaNm_pmnLH5FaFN0fmCusWb0MOC83DTusDcWCncQbpYNe-v90v4b-0maeMyg1qXCr1Kx-xe7u306B4MYKEYmcEf05JUJeC9DnvexdEzZYjTsZ0o3mzqYV_2cDemRGKZvL66klivhUFY09bcn86Pe24p4fnJ99VXJqmTsVgX3CT7VttwXoB0yZ7LSiAXSNlW4nQHg6bXZYMKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXOPmzt67hNdgjEaN3a_XZ0aNmpyTjy0HwjJXZ3mvfRlqGlBMmrsrmTNA4y0q1GBrql5SSgdfGPkDbWYqOPv4K_o3q-SLKvxUi8WfYiWTmHWcjJDoSnyd0sy3hx7tauVH-ksZY0NAzAXOCxUkPHQbHFdh3uqt_HCKkGVEdV3CTjoJT8T85HHzX47zDVqsAAm9YMvN1UdcwO6YAj0hHg0Qn63nG6sLiawpRrkT1gFL3tICYBGk_MyFKjchwn7HBr0_Hk8eOkpNnqK9cmKyt77FSlt_SxiA45eEpe5rEgFLHzlX21OJ8SwRi4QU2vc7JM0BNBeDjIMupcovtCJsDJ37Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=mUeboy1sIiOfI66frXHtz7FNXQXIV3pAFSQQ1TnVeiR0qRB-WYH1Jc_zVKROs4mgrmUrBKXzvyKn0mKl-Ma-dnSAIsbPL55dzRpxyGrj9WHU4geJeJChMgNxy06d4T9nBIlm5KJW70bBwBC8UWLUo4BZnVDKqR58u-XblExHUaGAxkML1Z9kY7XFumWqUhG4-K5D6N3fN67hD-xzOcf_aj9gLE6E_Ruv-gpvbG0DOUpo3OIrdiHQ5Mzt30ixdTQkjLAFCpLkW7kwB57s47pjQBw795HSQyLnOqq36Qv1PLCOzB76-ja3HHrtUomeVxLIDqbCB3IE89EJKNS0ZK3B2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=mUeboy1sIiOfI66frXHtz7FNXQXIV3pAFSQQ1TnVeiR0qRB-WYH1Jc_zVKROs4mgrmUrBKXzvyKn0mKl-Ma-dnSAIsbPL55dzRpxyGrj9WHU4geJeJChMgNxy06d4T9nBIlm5KJW70bBwBC8UWLUo4BZnVDKqR58u-XblExHUaGAxkML1Z9kY7XFumWqUhG4-K5D6N3fN67hD-xzOcf_aj9gLE6E_Ruv-gpvbG0DOUpo3OIrdiHQ5Mzt30ixdTQkjLAFCpLkW7kwB57s47pjQBw795HSQyLnOqq36Qv1PLCOzB76-ja3HHrtUomeVxLIDqbCB3IE89EJKNS0ZK3B2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=sQU0l8ct4xBlsGHF2IV9VJItkC-UGjGb8zr5l15gFtjur9K1JOmEFYExQ9fZ_nM_OZZP1YW7D14mJHnHENpE5MFYocGZXXGeoKVbK2S2xWatOR7X9NhSL8NTZdhZrzh4k7jVp5qLXcTUoQR_n_0fxJjsFQ63uMV8ISscZuoK103_MxPckYKltJOXmVimKpTLueeCq0FvfIFP37LcysB-4pt6F2mkOilHZSXr0FckdOOcdiMjz8r3q53_BWVJI_Fd21uVVIec4S5nJlNAxKbDmDONWGTBWwD2Pq4VUjC7ZdC5NECiJ1ghgXisgs-gK0k63i4bicLuHjPyXC2urTueUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=sQU0l8ct4xBlsGHF2IV9VJItkC-UGjGb8zr5l15gFtjur9K1JOmEFYExQ9fZ_nM_OZZP1YW7D14mJHnHENpE5MFYocGZXXGeoKVbK2S2xWatOR7X9NhSL8NTZdhZrzh4k7jVp5qLXcTUoQR_n_0fxJjsFQ63uMV8ISscZuoK103_MxPckYKltJOXmVimKpTLueeCq0FvfIFP37LcysB-4pt6F2mkOilHZSXr0FckdOOcdiMjz8r3q53_BWVJI_Fd21uVVIec4S5nJlNAxKbDmDONWGTBWwD2Pq4VUjC7ZdC5NECiJ1ghgXisgs-gK0k63i4bicLuHjPyXC2urTueUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر : مراجع تقلیدی که‌ قراره نمازِ علی خامنه‌ای رو بخونن که همچنان خبری از مجتبی خامنه‌ای نیست!
تهران : سبحانی
قم : عبدالله جوادی آملی
مشهد : نوری همدانی
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67291" target="_blank">📅 19:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67290">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=F3rFYhildPl5ciGvDQvIMrAlM_hfY0scePcOXvGemp1gpDY8uKLEd8uGtH6Vg_Qq5mQvHRU9TMJBH-SbcdJhlcuHVBpu_JdPpjGEJr0mRewn1632-HohKfDlVs8MjqTEq9GQHeLt-RKF7CpONw8hvIS0YsFUNC1h7OYeVHFtqsRWX4SsPKRJM8XC80wfBJO_fy8xJ5Kr7du5RUQpgO45OP1Xt-VahJkhVajEpz3a_ArX6XD4rF3uFUu4LdB2pkb5nQAYz0DD3VtqRtRzKEdwqXMVdl-6ckPUNhz47M2J9WhzLfdBo-e2LGk9IopX1QLgbYEgHHK9LjHwE0WSAmcW8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=F3rFYhildPl5ciGvDQvIMrAlM_hfY0scePcOXvGemp1gpDY8uKLEd8uGtH6Vg_Qq5mQvHRU9TMJBH-SbcdJhlcuHVBpu_JdPpjGEJr0mRewn1632-HohKfDlVs8MjqTEq9GQHeLt-RKF7CpONw8hvIS0YsFUNC1h7OYeVHFtqsRWX4SsPKRJM8XC80wfBJO_fy8xJ5Kr7du5RUQpgO45OP1Xt-VahJkhVajEpz3a_ArX6XD4rF3uFUu4LdB2pkb5nQAYz0DD3VtqRtRzKEdwqXMVdl-6ckPUNhz47M2J9WhzLfdBo-e2LGk9IopX1QLgbYEgHHK9LjHwE0WSAmcW8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGtEQqwo_MYfhsWUQcLc6eYCaXC9uExYZ5uXVjYR_Bc-cUKHOXfHPd8arFT42RmcvEvjPpl4gydP3mHC_bA8MZJgskoc9ziXeAEbQSQn9Kudnp596B6hq-_VGR5m8PX3kp1FJrx_6A24gAKoXh-BuZGnFJ1WpXnE0He9Q1-TW5IFYiHuKDiB57sOAZ_Qd5Eo6owIr6PQFLFMYdTJu8t5UTuHlNHzrbpOzpv_pU8CqX_Qyi7JS2VqRPuZUmRUqEOYBb7_YBesZkhfvFG-v_KVZ_6qcNg4njDeZFD7jm92rMPdGKASnjulRXd1f7H01uFrohaW9hwIV9NJsP0e7CTITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
🔴
خطاب به نمایندگان خارجی حاضر در تهران برای سوگواری علی خامنه‌ای، دیکتاتور فقید ایران: ایران در سوگ او نیست.
🔴
ایران سوگوار بیش از ۴۰ هزار فرزند خود است که در روزهای ۸ و ۹ ژانویه به دست خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به خاک و خون کشیده شدند.
🔴
رژیم مبالغ هنگفتی از ثروت مردم ایران را صرف برپایی این نمایش تبلیغاتی می‌کند، حال آنکه حتی یک رهبر دموکراتیک نیز در آن حضور نیافت.
🔴
آنچه امروز می‌بینید، ملتی نیست که در سوگ حاکم خود نشسته باشد؛
🔴
بلکه ملتی است سرشار از خشم برحق، و همین خشم و دلیریِ قهرمانانه، بساطِ باقی‌مانده‌ی این رژیم جنایتکار را درهم خواهد پیچید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67289" target="_blank">📅 17:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67288">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=KuzHN9FLR3xCOdwSz1UPytzO0Erf2s-nnJUb5um0divcWi6F_StT_muKuGVycqxGxGv6n2MGFfyMlMmEyzi0Bag-uIL5t6A8iKplG4A1ywqkW5C7CtosJ1eGezUrX4IqB3DIMVsFKLUjLEhqj758VfDEFpjtacJFkcWb5FBLbzjVzuSa4zjWcMx7gHJX074xR0ONRkkZR1obZjjCOWYZC2lDkqQqOT3Z0cR_Rezh_76mt84g5aB6Tn8h-dWELxYlmKz6m4mG2KPQDxr1T_OTGpDXfspYkQLQWXeOJx7hrVOEc94H226TWQ_U9IEPZeH17fDW0aA8BU5a9tTB4VTT7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=KuzHN9FLR3xCOdwSz1UPytzO0Erf2s-nnJUb5um0divcWi6F_StT_muKuGVycqxGxGv6n2MGFfyMlMmEyzi0Bag-uIL5t6A8iKplG4A1ywqkW5C7CtosJ1eGezUrX4IqB3DIMVsFKLUjLEhqj758VfDEFpjtacJFkcWb5FBLbzjVzuSa4zjWcMx7gHJX074xR0ONRkkZR1obZjjCOWYZC2lDkqQqOT3Z0cR_Rezh_76mt84g5aB6Tn8h-dWELxYlmKz6m4mG2KPQDxr1T_OTGpDXfspYkQLQWXeOJx7hrVOEc94H226TWQ_U9IEPZeH17fDW0aA8BU5a9tTB4VTT7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
ادعای نیویورک تایمز به نقل از ۴ مقام ایرانی:
پزشکیان به مجتبی اطلاع داده بود که در صورت عدم توافق، از سمت خود استعفا خواهد داد.
نامه‌ای از رئیس بانک مرکزی ایران باعث شد مجتبی با یادداشت تفاهم موافقت کند.
پزشکیان، قبل از امضای توافق، به مجتبی خامنه‌ای اطلاع داد که محاصره دریایی، ایران را فلج خواهد کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67287" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67286">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=ZA2oEF7oKQpvPRTPQ_Tsa5qM0kkEjwcr-ghmAYAe8cUMINt7vIhd7uCKf9vTuKtYiRy8TtkUJ5rMo4xCnGWWAda7RTSQo_wAICx9yS4hTPlHTOhJ0hKOnfPjGsD-bU6vZbiLyONF-xMc0y93IzkqrZg65UgHrNVNADTAaCkIhwLICKOEhb2Tgtgek14USAs-Znzsnawynyv7otrwdB7f56Q8G8L7GaWawJB6Rb0mmHID1meKqCEwTe8pFtjjtvHlocMWRr2PAX_X9B7rg_x_SGUMgY3SqXype76uSHsY1SBaP5JjiO_8QFvYEW-owMtGDaDjPXDgFHDNKOiRXDPdIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=ZA2oEF7oKQpvPRTPQ_Tsa5qM0kkEjwcr-ghmAYAe8cUMINt7vIhd7uCKf9vTuKtYiRy8TtkUJ5rMo4xCnGWWAda7RTSQo_wAICx9yS4hTPlHTOhJ0hKOnfPjGsD-bU6vZbiLyONF-xMc0y93IzkqrZg65UgHrNVNADTAaCkIhwLICKOEhb2Tgtgek14USAs-Znzsnawynyv7otrwdB7f56Q8G8L7GaWawJB6Rb0mmHID1meKqCEwTe8pFtjjtvHlocMWRr2PAX_X9B7rg_x_SGUMgY3SqXype76uSHsY1SBaP5JjiO_8QFvYEW-owMtGDaDjPXDgFHDNKOiRXDPdIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=lWHGQgRltwrVvevKMMgsYNsdK9eg7L0xzEYYcbDzaJ7MWCXoktgK1Hc3VvaHuYfnHLFZfbcCh_iNOf3-8E58O2aSe441VibBpOwm1ao_S6gnHgPkoiYQ21s7Iw52uQqf4VAzHiLvdMT4G9kUhoS5UwHO6OEschj6NMIIjsMLWpt2T5E1wopKGajgN5WIkkXmMy4fUXfVtJTIU9nQ3K8G_bHRSEsszGsk0e1S_bflH6lmybHOiBGBkMPurNIFcEGP4BQal7lvZi2kJBrpp_ZGujf4XbfuPbYbDoImbS_-237_7hMyUkV_lKA7TKak03K_LWgfn6tF56NcKYNgoLNE-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=lWHGQgRltwrVvevKMMgsYNsdK9eg7L0xzEYYcbDzaJ7MWCXoktgK1Hc3VvaHuYfnHLFZfbcCh_iNOf3-8E58O2aSe441VibBpOwm1ao_S6gnHgPkoiYQ21s7Iw52uQqf4VAzHiLvdMT4G9kUhoS5UwHO6OEschj6NMIIjsMLWpt2T5E1wopKGajgN5WIkkXmMy4fUXfVtJTIU9nQ3K8G_bHRSEsszGsk0e1S_bflH6lmybHOiBGBkMPurNIFcEGP4BQal7lvZi2kJBrpp_ZGujf4XbfuPbYbDoImbS_-237_7hMyUkV_lKA7TKak03K_LWgfn6tF56NcKYNgoLNE-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
ویدیوی این بسیجی که در مراسم تشییع علی خامنه‌ای وایرال شد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67285" target="_blank">📅 16:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67284">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67284" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67283">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67283" target="_blank">📅 16:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67282">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNLthOHfVCzo2hcXWSDQnL6ch4G5LS_9lCJ_lfNLIUu6bsXL0JZaXjpV_KTXVCI2fjOvWvYkmhkQvLTX3NqYT5ZZUEOPLKZ820OKGeZnNb-M5uCca2MsdjETcKvpcvJo34T6hwj9_DRUZDGjKX7vskXOETNrfO94gVl9eBWeWpsFQkQxZgB0umlaQDWFBAIfXufh0PptS7Ph0FCHWUqwqUuALxHsEBMENDEZ1kGImThgIg2HJDKMJJbwA4NcXD2nfSLAoMUz8g17OL2Yz6kGn-ZmorVfdlX6yyGwtRmFYJLgZMkmPHgGcx6oRH1h1yrnOr-OYOQO_genPiKAHF1Bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXLf-kt58wr6mP8ZJ3O3JAPzNOE5kUh8cp9LtN3xdlDpYv6lM1zOT3zM-h8NYgt1ph9Dw1MVTJf59k_NQHTSIiFJyxdzUm4gqz6HOTkj9cj5xTZ3djDt8NdjDgvNHf9Jvp067O3kTY2q3LxsWpkL1snxEUpYDW4EyngULsGv2-fvH31jgx2cODAUTXMBvvPL6YW7eoaO9MjBzqCHiBcMx5h65zSQ3sAEdyXJHclAROOCT68GlL4Y4d2cj4rvkdkZY_Umq48REiw6CSyvMAtjwJ5ubWscI6nWB9fa-IqaKdDkpoxN3Tw7jnVT5DyekA_cNeh1aqbgRLFN_2MXioT0Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیویورک تایمز به نقل از منابع آگاه:
🔴
مجتبی خامنه‌ای به مقام‌ها گفته است می‌خواهد در مراسم تدفین پدرش در حرم امام هشتم شیعیان در مشهد، که برای ۱۸ تیر برنامه‌ریزی شده، شرکت کند و نماز میت را بخواند.
🔴
مقام‌های امنیتی تاکنون با حضور مجتبی خامنه‌ای در این مراسم مخالفت کرده‌اند، زیرا نگران هستند اسرائیل از این مراسم برای کشتن او یا ردیابی محل اختفایش استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67280" target="_blank">📅 15:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67277">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-B1fVUva3jVcFL_Q9-GkVtWyjKYcNfCx6u9tY45PIsmHyETHhM-YDnPf6IAGq53YS293Y1vcohCYsFtcoUljap6d2fp5VJ5DnP37XhXOVWiwipah61COcmX05Esa7YUK9rG0K2HyXoSestbwut4MkGnwg2eAhd7Mh5jjgBv1kEeLs2wZfp8mXBaYeIRjvAfc-VikC391xay4gMk81x6eK2Ct5oMtL0E9dHHOHGpJhGCuddipTUQGKYMThtP3oKvVDwiTfBVtuIG16Zr_J7tK3-CJSRIx2HWOsadCGRf07_INBBCsrYq27kJGiXtaY6kMlxiLtL3MlenJVvJFUq3Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0aeCxqXsg2sdTCRurgkHJeu3kih9IgUNluQAmsnioGmV6jwtqhPKDaUThRoX8V4qiK2j77Sga4SqWvm2StAfa-ADfAHCK5y7RLB85O3uWBlvdG8J1kWHsuAyeVEgQkjdZ9ZhfqgUSLSctabKaYCCi0swkjfx32mjgzgo5Zj7wUJLg6lEnAv4maIzzSj0AmzFaTF5bC0ceclyqMLYaz5Bsqha-HyHLZnA2UMqlnvi_ZNbkoav8NAxdozlqjFGoJJTFUwoNb-fCkC00yotQ54lT3zgUPG8eiWwahXnuJfyqCfZjfUkJ7DtxQMY0rR3iUMDJ2DN2wftOjSCUMdZjLJZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=BnfrCbFdyRq_gSvD2XZ_7XqNtPvpfaDqL47a7Aj2H4lMIlW2j1lgbUzDoRxXf0e-WwJBe7Ch7IjMTye8OKHyZAaULvMokFp9NjDPP2F1zr8emZstfOOHUKFnRiR0OeI05-Q4kCAMSZ8WQpdC1YZgSrykRr4yvRKYNEHbot3x_3jZFIk0EC913o42zGguz6Uo_opBMt6ffJKKOlCGecy1Ej7CvB3G1rDXQpeJ1cOesu4_BjdadL-i82Ptf7z-_biBCFeydiTDATsvM97dOmMRiYdd8Uj2foqvQ_PNTbPSWPRZseFeksaElrFjR-PP_rLDxUxWQYXcm7Q51sDJt2mDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=BnfrCbFdyRq_gSvD2XZ_7XqNtPvpfaDqL47a7Aj2H4lMIlW2j1lgbUzDoRxXf0e-WwJBe7Ch7IjMTye8OKHyZAaULvMokFp9NjDPP2F1zr8emZstfOOHUKFnRiR0OeI05-Q4kCAMSZ8WQpdC1YZgSrykRr4yvRKYNEHbot3x_3jZFIk0EC913o42zGguz6Uo_opBMt6ffJKKOlCGecy1Ej7CvB3G1rDXQpeJ1cOesu4_BjdadL-i82Ptf7z-_biBCFeydiTDATsvM97dOmMRiYdd8Uj2foqvQ_PNTbPSWPRZseFeksaElrFjR-PP_rLDxUxWQYXcm7Q51sDJt2mDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLwW_lwNxgqAqBkCWmpeV45v86jrpnZ_12epvlhsTfpSZTwchvRKGlhKEWd1WIv8NJvyn5DZqA-EKYTzm93fBmt9pb0ZPxDJIshkpWetUhWMshIIzzwJ1krb0z32iFXSLM69pBTumJxVG0HWIfYxeqx1WaTkl4nFaa7YG4ega4kW1umGaeVGKOloZiwZtVS9J7Er2lTfiEjLA4D2fSHcIhoOPav-5D3K1Ihw63a5pbZJxKvPtVvvGBn6OgvUtcnhCByRyr7I8AmpadkJtLo9MMQB8qB8FTgzgaj0RdIY-t_sm5YEbkF6jqcxGfwchzXS5itM4Fq6ILiVR6bhkms4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدودوف معاون رئیس شورای امنیت روسیه:
🔴
ج ا به‌جای سلاح هسته‌ای، به سلاح دیگری دست یافته که دست‌کمی از سلاح هسته‌ای ندارد: تنگه هرمز.
🔴
بحث‌ها اکنون بر سر این است که در آینده، درباره نحوه کارکرد و وضعیت این تنگه چه توافق‌هایی حاصل خواهد شد.
🔴
مقام‌های ایرانی همچنین یک «سلاح ترمونوکلئار» دیگر هم در اختیار دارند: تنگه باب‌المندب.
🔴
اگر این گذرگاه بسته شود، همه محموله‌های نفتی و سایر مسیرهای حمل‌ونقل عملاً قفل خواهند شد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO_2obfWOwErrUEEfs8x4WD2x3R_08u2kxGXmYSJANq7DY5YfvuO-aIobOeM6ICGnYr-5_Wls4c30XcV8grByCwc5fhoREOxLmA3AzLrczMnhpiRQz0il5ZP5QhTGQ0BMdUaJV1wSvWyNUbj3wGHgmh-M6spb3WF0fBdltaglKtqzYYRt4Bh5b1JKD5GIbVVR-NdcCJRV0BMQXcdXvGX5v54MHPlmkPqFZX2E-jDhFYBQHyD0Fgi32JlNBDwh1m-QzGXs-Bqd6tOVD3TsrilM2RdqCLC4OHGXbXw0EhG7hb22sFJEnGdsDCHkWb5JO9q9ggUH4QRngrLFv5eMPmFcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0tdsasPnn23yR7G0tzNb3fseW9qkpweVY7N5ZXikycXpVUhdMY4bbZWcszgBZ_kIVLjHzL1khm01W9mMB7mEpNZo8BYzyZihdYUuRFqtqAVOsa30KVWA4vhBYcD7v2HwG9N8bQKXV33-AiySGvKK02RvFs_lw8h73r5HwfBpnPQTaMHWLjlkJtsDYzWHGkqx1yaKH86JEV9ugsurRoqFJYrW_j0JS4_YgnSt9DHm6InyWqAPB_8erfHtqN2g_mtVf52umsV-nhtSlzElAQHTfaPHyT6KUBhL2x8qGJc--xLTc4V-ej_SOpb3E4N-CgM-0OA8jwQkPCGDh4rM-rTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=q6IuPG0vkhI4jp1m_8CZiosAipeaYsukHhupwbWYdV-E6SL1YgNjHDPPAWu4fvsQdrT4EOrdmiAaU_nLvEM01eZP2q3bxKVQHci2YMamHr0WPYyaW5iUxumLDqCx-DAuyt54WCD7MItaOtwlT13ZtM4wVs_ntHdnAXmCa3IRwqAuusU_lA_0zjsGvvEw1E7fA7CVvSrHsH2XqPHAP40P3Mn6Qbg3EiT8EonncRpmgfIDWbaC52c8ra4HE-TR177GYWI782V3l9JlNa0SKSt_I5wwAHUrWXF6ACJgK6YOPi_CWnTr3KeUOShzd61F1wgnxhujpXDdShhurn4U7WfenQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=q6IuPG0vkhI4jp1m_8CZiosAipeaYsukHhupwbWYdV-E6SL1YgNjHDPPAWu4fvsQdrT4EOrdmiAaU_nLvEM01eZP2q3bxKVQHci2YMamHr0WPYyaW5iUxumLDqCx-DAuyt54WCD7MItaOtwlT13ZtM4wVs_ntHdnAXmCa3IRwqAuusU_lA_0zjsGvvEw1E7fA7CVvSrHsH2XqPHAP40P3Mn6Qbg3EiT8EonncRpmgfIDWbaC52c8ra4HE-TR177GYWI782V3l9JlNa0SKSt_I5wwAHUrWXF6ACJgK6YOPi_CWnTr3KeUOShzd61F1wgnxhujpXDdShhurn4U7WfenQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glMvTInTEXxj6ChRtPkq6Rtd2dPsodeMXpNQIgpKD6wTLRoBG2LHcC4hm55ArzHaMcH05XhuQAj9W50GydgUQBru7WH6VI9D5xLG5sVsrUgqLWmmRlldTB0I8ERXBVijPnB3d14lBBZngzImEJMKTvOyvNM69CVT2hy17s6-uloSUOKQ4MmY6o7lkRcnFAK8Qkupu6KMcAnbO-KDZzXlWHJPGmRdwjIoOWZdPrDJ70IUn4iO5JJmLubTtw9FPgCsAEcTelj-ip6AtlUflduwXlalJOjL5436J1v2G9Jo3swvA1mb1uv2zvhDnce10Eqv2OyDMINuJrwc22cp-dXJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=HPOzyGzuEoXEtYrDaQYWas_XGIce5ibFTnPSFySmmWXhJkxQWFguI3p1xZ2HbkwKHzqJsIvSz4PmDSAJGXGfq3GY_4qc-eFJhHE7hbqjDaPgohWR4UMJWnG5o2XdwGKGmTZXZqorqIYv7Z7q_9xrCxUar2v6BfxioQz8FE8CW9qXRSq-MkEYWUrbyCZSLOtfATuTuVxCxu6o5JN-FAI2y9Xk-vnDAHWTUiAB_OmuN903FXco5DoRx6q2MMu8LHICHF5fGkYxCJ6ECaDPpK4iRsjbavYtErsQY3MpiNyPfgTb0k6w5-CdEDr2SSF3ZrSoYMLyM9Er8nK_mB0QkThw3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=HPOzyGzuEoXEtYrDaQYWas_XGIce5ibFTnPSFySmmWXhJkxQWFguI3p1xZ2HbkwKHzqJsIvSz4PmDSAJGXGfq3GY_4qc-eFJhHE7hbqjDaPgohWR4UMJWnG5o2XdwGKGmTZXZqorqIYv7Z7q_9xrCxUar2v6BfxioQz8FE8CW9qXRSq-MkEYWUrbyCZSLOtfATuTuVxCxu6o5JN-FAI2y9Xk-vnDAHWTUiAB_OmuN903FXco5DoRx6q2MMu8LHICHF5fGkYxCJ6ECaDPpK4iRsjbavYtErsQY3MpiNyPfgTb0k6w5-CdEDr2SSF3ZrSoYMLyM9Er8nK_mB0QkThw3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=oqQIDYs1da2EyJXLg4yyYhsqMu2k5gEOK_hpfNtcxnzLoh_LDRYsxdd2JXlCWVRb6v40WqMUJDL0NR7WK5Ix7bTPwW-JwVZwMjWh-Thwp9RmaOFIyOctz2AAtjAl84avHcvdrQrP0t-14cYio04qubsNJA5VyqN2fk_Jn98pT7JoeeavVtftt_FMRy6KTL9cKBZxQKz76fz1tfiCNoqG4E2Cq5b9Z9exwZ7WDKgQVMPILuCfLYBbhGSqcUGBFnAi4XpjPqnUSDUjD9_OC_u1PKI6AIDlNy1TN_OMzkHc3LVDlEPIETyICSXJ8CxCT8yacxRaEhBbB7kPjKoQUUj3lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=oqQIDYs1da2EyJXLg4yyYhsqMu2k5gEOK_hpfNtcxnzLoh_LDRYsxdd2JXlCWVRb6v40WqMUJDL0NR7WK5Ix7bTPwW-JwVZwMjWh-Thwp9RmaOFIyOctz2AAtjAl84avHcvdrQrP0t-14cYio04qubsNJA5VyqN2fk_Jn98pT7JoeeavVtftt_FMRy6KTL9cKBZxQKz76fz1tfiCNoqG4E2Cq5b9Z9exwZ7WDKgQVMPILuCfLYBbhGSqcUGBFnAi4XpjPqnUSDUjD9_OC_u1PKI6AIDlNy1TN_OMzkHc3LVDlEPIETyICSXJ8CxCT8yacxRaEhBbB7kPjKoQUUj3lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=I0itN1OO74VMmf02GD-3xHndZE0CrXq3RRDxtAwiQaDoU446gJ3Mctx_upOOjzWJU9et9U3Tur81Q6BduI0LRKZQ6xV2T970U1hDeTSKqV_SbxdrOmgSLkcyjz2f6Oad5Oa5oaBJVDTpLaUXvJaRrIlmRSchYs21nCNJgIlchUjXar0sTudp-YJUaPd2OY9Qv8x1xFRoRZTJ1d3v5sZ-vQ291FbR_x1sU4sz3cxJebEGsl3TWtS2uxP_81ip5VcnPuEk661ywnjWRymu0MsMCPE8SBtpBoulQ9gLb4kx1IO0EAPd0_piCyMyCfTzZQgqZ2RVVvFSipTrkLofqLt71w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=I0itN1OO74VMmf02GD-3xHndZE0CrXq3RRDxtAwiQaDoU446gJ3Mctx_upOOjzWJU9et9U3Tur81Q6BduI0LRKZQ6xV2T970U1hDeTSKqV_SbxdrOmgSLkcyjz2f6Oad5Oa5oaBJVDTpLaUXvJaRrIlmRSchYs21nCNJgIlchUjXar0sTudp-YJUaPd2OY9Qv8x1xFRoRZTJ1d3v5sZ-vQ291FbR_x1sU4sz3cxJebEGsl3TWtS2uxP_81ip5VcnPuEk661ywnjWRymu0MsMCPE8SBtpBoulQ9gLb4kx1IO0EAPd0_piCyMyCfTzZQgqZ2RVVvFSipTrkLofqLt71w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=M_uGslk-p-6mgfQEbl10To6s3EXDc6R8Qyi-wL0u4m3Q8HnjAWr5HNsO8MebWSDcuWnimUvMPwIZ_MoTujLJd1EkxEIgwdMn92vJIM63LfXHq9hPqZdLYEWdMT06zuLw5-oBoUX1_G8xhmYY16Bk-TnXJJiI_XqsHMbKb5APeBhz-EAqOSD8HFVg-M8NknMpJf49qPiRA0aE1cvKRXAO9e-1SuugaDFmzwJJtfQj6lbj3HOagAFsi9NazVHwMF_uWiGuhDQfjn3r2_bYJ_aK4T9zjKjpUF0BuUZTae_0vBl2jcqnrLC-gdAcLNsKNeHLRbssazS9Oa9fA-kmeA__sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=M_uGslk-p-6mgfQEbl10To6s3EXDc6R8Qyi-wL0u4m3Q8HnjAWr5HNsO8MebWSDcuWnimUvMPwIZ_MoTujLJd1EkxEIgwdMn92vJIM63LfXHq9hPqZdLYEWdMT06zuLw5-oBoUX1_G8xhmYY16Bk-TnXJJiI_XqsHMbKb5APeBhz-EAqOSD8HFVg-M8NknMpJf49qPiRA0aE1cvKRXAO9e-1SuugaDFmzwJJtfQj6lbj3HOagAFsi9NazVHwMF_uWiGuhDQfjn3r2_bYJ_aK4T9zjKjpUF0BuUZTae_0vBl2jcqnrLC-gdAcLNsKNeHLRbssazS9Oa9fA-kmeA__sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=IPS5e7_fVCOjPsuhz5jrHzSjlEC-_BGer1GCt7ZvjGmkBF_ufdEEkhbhZxpW_DRCdZtwXmCuZuvYpbucIGwfq6kjfZYiFoU0zk2Ww_DNT-H2-KQeLMccje70s8CdPscxNQgZhDoXhy1_aebw0GC03X3RJomooAiFTphYJYPoV8NiPJkrj13clP7lEd9wAKORHTUAc5Q_1rXZ2Mwnw23xM9zB0AOyyTNd2vNetmet-0qMGRdv5icjTqOMC2TkUMQbe1Tx8738lPM7edKYbEUY0PE1RN_e6dSsvhDQJDsYpFgHSM3So_Hq6NzN2NHqL-tdwa0DD6LarCUTUfAsEcpu2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=IPS5e7_fVCOjPsuhz5jrHzSjlEC-_BGer1GCt7ZvjGmkBF_ufdEEkhbhZxpW_DRCdZtwXmCuZuvYpbucIGwfq6kjfZYiFoU0zk2Ww_DNT-H2-KQeLMccje70s8CdPscxNQgZhDoXhy1_aebw0GC03X3RJomooAiFTphYJYPoV8NiPJkrj13clP7lEd9wAKORHTUAc5Q_1rXZ2Mwnw23xM9zB0AOyyTNd2vNetmet-0qMGRdv5icjTqOMC2TkUMQbe1Tx8738lPM7edKYbEUY0PE1RN_e6dSsvhDQJDsYpFgHSM3So_Hq6NzN2NHqL-tdwa0DD6LarCUTUfAsEcpu2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=PvvPqbz9hnAu8ow_Aq0qUpu64-5LsiWvjwFYzUKC_c2mRu9rsfp3p2FItceKwGOJ2qItm6adrMVHHX6sTgzQl83lDcJGmvPpcX4TwgGFupdiweuX8mXdwYb4TPdaCtxN7cDM7kumXP3RUIQE924_hw0GJbevHK1GJSMbEM_E6Pu9h_o4yG1oTm6mrT5EOii7A_HOaup37xbepoXttqvm_kCezGg6csOvDvbwXI13Zm0X0tJPS5avVnvKUrYPEZM3f2B6FrljQ3OOUDR6fdUoQfRL_kLXd25JbiB4h-LjXr5HvMgyHe1_StoXIFJ4RxysalgtUeFAK4ZkDj-mVJB65g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=PvvPqbz9hnAu8ow_Aq0qUpu64-5LsiWvjwFYzUKC_c2mRu9rsfp3p2FItceKwGOJ2qItm6adrMVHHX6sTgzQl83lDcJGmvPpcX4TwgGFupdiweuX8mXdwYb4TPdaCtxN7cDM7kumXP3RUIQE924_hw0GJbevHK1GJSMbEM_E6Pu9h_o4yG1oTm6mrT5EOii7A_HOaup37xbepoXttqvm_kCezGg6csOvDvbwXI13Zm0X0tJPS5avVnvKUrYPEZM3f2B6FrljQ3OOUDR6fdUoQfRL_kLXd25JbiB4h-LjXr5HvMgyHe1_StoXIFJ4RxysalgtUeFAK4ZkDj-mVJB65g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=rWzmJmf89XIZyePKbim0eITjGQ0dD665idmUbQ0zj_NVS8xsfA4QFQPzzGDQdaKZW6QwZVVBXIFXtw0rs-IWYrUNDNznCPJsIO-bPutcv1c8T37J3uNFRUprXwoPbotTtM73fOpyjL1FBgFbP5Pc9IdLOCFq6H-v9mnmqrLxhs0XWXXWtGClouIfMl4T1eH8M07uzl9aMYVa0pP11SaiJDoot85dRbni1wLRa9dN3hXMuxdD1Qi-gIPJ-CvUc4TNx2m_h7PI1VmCUP1p7Y-IaXA9R01F1TC3JRtiokdZNod6YRvhiZJu_qF0OkPodJ3Eg6pTMFF5JviP26m3QOx16A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=rWzmJmf89XIZyePKbim0eITjGQ0dD665idmUbQ0zj_NVS8xsfA4QFQPzzGDQdaKZW6QwZVVBXIFXtw0rs-IWYrUNDNznCPJsIO-bPutcv1c8T37J3uNFRUprXwoPbotTtM73fOpyjL1FBgFbP5Pc9IdLOCFq6H-v9mnmqrLxhs0XWXXWtGClouIfMl4T1eH8M07uzl9aMYVa0pP11SaiJDoot85dRbni1wLRa9dN3hXMuxdD1Qi-gIPJ-CvUc4TNx2m_h7PI1VmCUP1p7Y-IaXA9R01F1TC3JRtiokdZNod6YRvhiZJu_qF0OkPodJ3Eg6pTMFF5JviP26m3QOx16A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NiU0lajpB-yEx2D0TFzGlHya4DKi8UzyvCq4AYH9WbK3hzpJ3XiBOo4u4GFIPLhbVWeeBdv4nfzlKdCNTPXXfuZGKbN2FsM_A-fO3zNkbUPBdtanX4vX7hNuC3GuwGGdOVGSWAUcUBhIVOtGJQe28vQcTjdtNFcP3HIhUC9pLgrN9shok6XbRVQlVigDLBk9UhS_7QcV8lcMVCZb75ObJSTcg90Xn1JeR3-0_TdcQP4HMIRul_TDYanINBCrXZr2lR_MPRuK9iHZEUclpv3TO6pipo-BnbKMVrrwXeUK00Cs-jw8MRFRwUgg7bUqhMJ_U7clf9uSugQZvJa5crsm9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
🔥
🔴
میدونی هوش مصنوعی ترند دنیاست و اینده ی اقتصاده ولی بلد نیستی ازش استفاده کنی و درامدزایی کنی؟
هوش مصنوعی TimeTrade این مشکلو حل کرده
✅
هرکسی با هرمقدار علمو دانشی میتونه ازین هوش مصنوعی استفاده کنه و با سیستم auto trade به صورت لایو و روزانه درامد داشته باشه
🔥
👇
https://t.me/+hcwmoHXpF6k5Y2Q0</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iUxuRmaI9XckJThk7LLrJfEtjzDZrVtDqI63nOhhQEf18mVFijpoCr7k66zmyFjMkkQiEkqgantoDvTOT-g4e8h1WwPMIwbfwyjy_eeEbAtZdVYXWof7JnB8gQ576MrMiVmJbKmCLCzcaX8Sixh3Isy_HsFohmcnFdpatnJUg9ojROL_2nyHEUEmp-4l_w9IwGKfuovVCpjmGk4In4bew9lsiK6se61R1x2joRfovrdTtx3_48-mSIl8Bqk48a9oVf4by6AiuXjE8HXn7rIiUiOgbdzLpne8sB97W74U1bmJfM5UITHmca6rlLnAGidoI1KFng4lUcoCuUvlBMOLAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=JXzvmdW2lFe3Z24VhzXLjCihHoq4K1w8v3pfrgbiT8Wv_-HbheVCHqd4WNg8to9FW1F79w1qNWbt9n4ArHYM4Iy7pyUhewB3GL7niVVqg-UMVgXgAEj3rE6VZmu8GXmxjsST6tp4ZbGuKNAyWOLIqc89i3njETvbDjYWb5LMs4rG-AZ9akYvWcp_8Q33O_AGrYw_cvWC_eS8q7ftAkb4haMi52oBNQK7r5XjghxQz1m3BTxrfGOzuQ8Vxn9fYzrZEC-O_5RhmAqnc1RGzuHShZWsYXHaGOOmttL3jEHcSDDbW3-__4JM2z4ZaAT2Dhy03PM6jO58vfoTs1fS8a5opIpofC3Ncs09D6LckSs8bgB3N8u-ZyWsx9dAuGv23vKJ-8lvBBPs9Lgkv-x5Hw1gcfjA36_ZuRlAWKAakUwFNhE2StoJl9GrPIOF6Vl_OGRyEj42-K1eRmPaaYvEFxsQEDoZEGIbKrl5U8zSmPm35NVnfavdVO3mrWJSJmM_j-MxjCKKvLcqmt0u-4M3pjHozND583o6dDVr0o61M-RLK6iZTFF9nEc31bQYcQZwmFWq67G4BwZ_M6EB8d74aihSoyHvyKIVvm6eErS7e5_xmgfq81OfuwBG6SU0xenhngDnsrzfkYjHtoEr2u61iWxyr_L-gu5czfzRJ3NbJQa-278" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=JXzvmdW2lFe3Z24VhzXLjCihHoq4K1w8v3pfrgbiT8Wv_-HbheVCHqd4WNg8to9FW1F79w1qNWbt9n4ArHYM4Iy7pyUhewB3GL7niVVqg-UMVgXgAEj3rE6VZmu8GXmxjsST6tp4ZbGuKNAyWOLIqc89i3njETvbDjYWb5LMs4rG-AZ9akYvWcp_8Q33O_AGrYw_cvWC_eS8q7ftAkb4haMi52oBNQK7r5XjghxQz1m3BTxrfGOzuQ8Vxn9fYzrZEC-O_5RhmAqnc1RGzuHShZWsYXHaGOOmttL3jEHcSDDbW3-__4JM2z4ZaAT2Dhy03PM6jO58vfoTs1fS8a5opIpofC3Ncs09D6LckSs8bgB3N8u-ZyWsx9dAuGv23vKJ-8lvBBPs9Lgkv-x5Hw1gcfjA36_ZuRlAWKAakUwFNhE2StoJl9GrPIOF6Vl_OGRyEj42-K1eRmPaaYvEFxsQEDoZEGIbKrl5U8zSmPm35NVnfavdVO3mrWJSJmM_j-MxjCKKvLcqmt0u-4M3pjHozND583o6dDVr0o61M-RLK6iZTFF9nEc31bQYcQZwmFWq67G4BwZ_M6EB8d74aihSoyHvyKIVvm6eErS7e5_xmgfq81OfuwBG6SU0xenhngDnsrzfkYjHtoEr2u61iWxyr_L-gu5czfzRJ3NbJQa-278" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=VwmRKsO94Kur4UxI3rq3xrac-V2A3s4aNAsIt4yPVAGdGtn55q-StXD0c6TVCteAm8wpg2tjfSQjSsAyLpDXiYPpA-PQhYW4A3vYUKmxc72-dyCrhT0eFYwyxjvIfp3MtKwNQnC2DWAJmGkC8RJb8PExHmOCOPCuYBjz_YuVuOcBRFXTUbLG4nOXLqVlTpAh8brJrifsSKRQtSVYwbm_3zjDp3s51XYjG0K71_vyHDOUDnpA_5d-dhAMQdRyXZlZYkr9TV2UgvRG5jo8k8WUyJYq1romZgJ62iE983i_D4wjKUBmIDLBGkBOlbw6kzCcjbf0So56vT3JUEwq9xt8Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=VwmRKsO94Kur4UxI3rq3xrac-V2A3s4aNAsIt4yPVAGdGtn55q-StXD0c6TVCteAm8wpg2tjfSQjSsAyLpDXiYPpA-PQhYW4A3vYUKmxc72-dyCrhT0eFYwyxjvIfp3MtKwNQnC2DWAJmGkC8RJb8PExHmOCOPCuYBjz_YuVuOcBRFXTUbLG4nOXLqVlTpAh8brJrifsSKRQtSVYwbm_3zjDp3s51XYjG0K71_vyHDOUDnpA_5d-dhAMQdRyXZlZYkr9TV2UgvRG5jo8k8WUyJYq1romZgJ62iE983i_D4wjKUBmIDLBGkBOlbw6kzCcjbf0So56vT3JUEwq9xt8Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=fXWvivQKVmDKLgjCb_4vfvEWL-_bcFoa9CdFG58zQ4cIwYCv3qwEIcPvMP1emAMWJa3It4n7wmeWF9-PBBwN8SJE-LqlCfyQHabmFb3R2AyRX9WLexOodw7WR9L7VSgHlr4wUhQncvNPALSP5yzxnbADkGlT3_GNMYwzieKWcDAVk1SRtmSM-jxAxeMi6TEEdUEzWSY9ijvJ-jaS9W2kLGAfmv3sbt62TWY7LTfgYbzdXa3OXIUvFJCWpF4s1tv75cOlHtfFzz3MpO8KedzlfP7q6w7tf--Vq-uFuubR-Kx3un96lDoDV_DRuf6oSy4JBz2PK2PdbH7EnzyaGSPQxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=fXWvivQKVmDKLgjCb_4vfvEWL-_bcFoa9CdFG58zQ4cIwYCv3qwEIcPvMP1emAMWJa3It4n7wmeWF9-PBBwN8SJE-LqlCfyQHabmFb3R2AyRX9WLexOodw7WR9L7VSgHlr4wUhQncvNPALSP5yzxnbADkGlT3_GNMYwzieKWcDAVk1SRtmSM-jxAxeMi6TEEdUEzWSY9ijvJ-jaS9W2kLGAfmv3sbt62TWY7LTfgYbzdXa3OXIUvFJCWpF4s1tv75cOlHtfFzz3MpO8KedzlfP7q6w7tf--Vq-uFuubR-Kx3un96lDoDV_DRuf6oSy4JBz2PK2PdbH7EnzyaGSPQxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=O3Onud_wIedw2FWM4bepP4ExkCVFy8lLX2UkmsrZDlACcMZLz8dwcLbaPTVpCtHTcJ8fAvPrZIfIM1Xi81o1aWhtFdl-thn0cXac_zS8ADqmoeqC3TaZKFgnLwxgAh9AssmvAi9cJLvJCePzZ_vbXvbx-wSQQmpuNW-L8aQ1sL1hyrpB4LDk19DttbqR-33R0wV0774YWWiJkljpCOURbtyoQ_6x8vMPVMB7lJw-Pmg5fjre0XWxKnUIUw5UNWHP87syLXrJUrW5dWRFCCQPhdJdKzei2bswLosLfOb3g9g8nhj0t1FAb9x6ZFNQhTREc9cdO_9jSWWiwqmKZnCOZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=O3Onud_wIedw2FWM4bepP4ExkCVFy8lLX2UkmsrZDlACcMZLz8dwcLbaPTVpCtHTcJ8fAvPrZIfIM1Xi81o1aWhtFdl-thn0cXac_zS8ADqmoeqC3TaZKFgnLwxgAh9AssmvAi9cJLvJCePzZ_vbXvbx-wSQQmpuNW-L8aQ1sL1hyrpB4LDk19DttbqR-33R0wV0774YWWiJkljpCOURbtyoQ_6x8vMPVMB7lJw-Pmg5fjre0XWxKnUIUw5UNWHP87syLXrJUrW5dWRFCCQPhdJdKzei2bswLosLfOb3g9g8nhj0t1FAb9x6ZFNQhTREc9cdO_9jSWWiwqmKZnCOZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=IX8tRCLDcTC0oNor5aK15XyCAfiRXvtpguj-4vdJeTAtGtKOXBJXzO0Qk8pFJBjF9akMr1SyDQFajy35VX93T9fShoNGuAD7nRmFy90mONojL5UhvllWieF6w1PiyOzAoiOZbfBX2oY2YGDGa7U6fP2sEF6W4v95So3lRactQQ1dqOtEdYjSztQHMrDsM_sKElUv0NZhlNhkpI2Nrldsj0snU-qti9OabwzSXdVDkk5YV0p9rJbXLkAPMyzfHjU01YwV6_PGdh8It_BjagHBtar8AI6A8_evW_SRHhFm3G8gmaauPDBQy1grB-6yNlfLswJh1Cs4yRDLBU-_VD8Yug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=IX8tRCLDcTC0oNor5aK15XyCAfiRXvtpguj-4vdJeTAtGtKOXBJXzO0Qk8pFJBjF9akMr1SyDQFajy35VX93T9fShoNGuAD7nRmFy90mONojL5UhvllWieF6w1PiyOzAoiOZbfBX2oY2YGDGa7U6fP2sEF6W4v95So3lRactQQ1dqOtEdYjSztQHMrDsM_sKElUv0NZhlNhkpI2Nrldsj0snU-qti9OabwzSXdVDkk5YV0p9rJbXLkAPMyzfHjU01YwV6_PGdh8It_BjagHBtar8AI6A8_evW_SRHhFm3G8gmaauPDBQy1grB-6yNlfLswJh1Cs4yRDLBU-_VD8Yug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo4fRvI8NNv9gSnPlfxIUAKjCJTiu8O0wWb-6KeoJEoUrjwAgS9HKKGpxfmjoW5h1JZDOpe10mPOWJDMHbOjs5A-JXC0l3_riFERdhe473Ul3pDk-QBhVALnizcgWRJFofrNKkFpp0LU_QvGsOt9oFUA-whFATYevrIj0RIdN0nkg8pZJeOi54KhckJrGpUBSKbRYhSjmOdHlFqZkOOmQOeOqo4SeH1lOPoo445bMPA6l91Q6-xSBk-n-pOjBhO-mQ_sY0rNaBrHweDVSskamMvbqSvxC16w63i2SnlnMClyCgYHFU4Qpko42KQf-MGVXUOU8wM2WPTiixUGnSyVbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCBXYtS7gPwFjbnGkso1wI5RzZIorQtK1aJc8G8qiQGN9g_Z94ofUQ9O3XTG_EoTocHrqKGCSY0gCVCKxBqrPGUuUAFOkPflOUvSXfc0YAoHw0Y0qf9b_OLcw1DhhuJ4-p8hYM0u5v5we6OW8keQGm-z1VIPC8n8zossV-vqYWWYoJQXPcY-suUtOVpCDctBNmpk4N-w0h9CIf4i9PXW93yFqXyOMEPZUDRlRLzwab-TltapNomPtBXRr-jenzPNeiavb6LeqQ_wf2ffJ-vxMAX25Z9PCDXkz8FgTxs1WGMj9SyZlu0osuhKKmS88ioKYlQe6WUrBG3SuSdRxaAvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpRUztdcJqmuPXWY6pX1W-E2pB5fUR28xZsPdNsOSDKhTOXJUsyQ67qWeNWhzfIGdOhTLyozPbBvwqNYda6Om5ij-BFg_DsNuulg9BukymdnUCfDb1kreawnNWTppFG7pFsy73sTmmVlxC8c8nd-eJVIknOEbauG8j3vcLiqQhTCKfnkjlOjMviq5wqcsO5bV4qZdSmUFUcNKND1Jr8AiI9XC5XzPw39qeQLn1F9dOlk5qOCqXz5Ab0ownFGkApaUm-ZV5zM360mSjdxwTyD5r3lS3_LrLEAdaJ6bqUwbrcjY9oYmECAD7VEi75EXQjiDtSd98R2Re_WpmCnb_c9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ugn5sVzKADGsbVGWDtCEHDrIOPUnoNHiguSX5AQoeXp_pgGXEooyushn5ZgKR8opsSUokIN4Mi_i0bXFYDlPqfoRfolzLFUuHA-Uo9e6tPEeOpsgnABaYDLd1hKNRHlnMKA6zzCJWdj-b87gCSEejag_k5da-JgS1j-6MHnh1Oiv7IfxOo4k4XCgcapkt9LB-2thETzP92UIYsYzPnBtz6LmwCiDL97j_ZPmxTIW2ESKufMwGi3PuU27k8_Indj-l3HUp9288MEZ5070YE-7Ve-n8xBCBuAiNFFHf3fCc3viADWE3x47cKVjvghc4fPZ1SwPrSV7YvorlCiCfcogFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN3Zve7UV2FnGEYr0CAiyLYwiHAVskzmf2GSE5HkELe1Dm6BhTMz1xA5zjUDuwxKrf81JKoyUTxVJtEIep3KgXMg4wlCmYhbhL1IX48M4Uc6u9sCgadhqjTv-x8azHLoYvrVxlpOFvt0H8-ClccPKQHKHPX22OnKlw0emzDX4Lj9VdkVyiE2YQjkTnX6RJQGjFAUh8bjoTylkP7M9_T1lqn8RFOcOr0qDrkg-37aSybLD1PCgdcxPurgTttykP5QIEEK6myJ4EoKXTS21mlg8N941b0_yqKL82kYCxZzG5nQD4ehoFcBnfqmosb_diCvOYkPEXAaffkMGHFBYzIWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDrjZZj9gSRPL_3-VmYN0vdmv6d-8sjHvZZwkpt1ZzeB--9oZs_YdMWl62dU1LlyPFNbXlkjshoUzSTqk-Q55__gwkGuWV0oCwcJK2Lahi_ZNMVR-wns0ZBBqZ2oJhyXPtC36tf_69mngQueNqmxuui67aQtKOKlvoLXI3A5-d6WmMdBp-ymnvSHjCPNgEXTRBQOnWaXG3XWdSGKR-gd9k3qAEBsa85CgU5lCPHpali6TS2vbTEf1MOaOfRUZNaRh_697gWaUbBvlTZLx55jOaVsRV_HAtunbcl2i6zbIwycNZFw78o9VbpIu1sdPwe57wqo4R9LzZRxNxDiZao-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=ZnGMnPm1iRvoAmhsbSuwOgOJAZA-QKdEJGUG4cIp4DsjN3cS4-qKGlH_BgG1_dMRMd-DF4h0WAx0gHQDrF_64B9wKxgV8KBt99eChjliEoSDitH2tYz_UUiXTYZpH9uv6ZuwmbKaBo7S1zuuojvSlbLcjhrlz0IAV7VopWAYfqdTLmFMKyD5kadkESxXAWF6ewV68KUX2cVD87xCPaenRouprHUR3NcdQEQXDcgwzvOYzE_Qpuy6a9mxBkHrCh49gViH3W6DRg86ZRPi7rvQ4StWtEx-HZ7KmiIdH7rklo81giR89ivoOoU3NCkx5kZLUoAbj6KoBg9znnzMU47mtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=ZnGMnPm1iRvoAmhsbSuwOgOJAZA-QKdEJGUG4cIp4DsjN3cS4-qKGlH_BgG1_dMRMd-DF4h0WAx0gHQDrF_64B9wKxgV8KBt99eChjliEoSDitH2tYz_UUiXTYZpH9uv6ZuwmbKaBo7S1zuuojvSlbLcjhrlz0IAV7VopWAYfqdTLmFMKyD5kadkESxXAWF6ewV68KUX2cVD87xCPaenRouprHUR3NcdQEQXDcgwzvOYzE_Qpuy6a9mxBkHrCh49gViH3W6DRg86ZRPi7rvQ4StWtEx-HZ7KmiIdH7rklo81giR89ivoOoU3NCkx5kZLUoAbj6KoBg9znnzMU47mtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LCcLO1yBFD2SsfzeezxmE--tuaKKSwpMpcgQUNIQEJU-FjvYx5FmUSa2MccL5bXQLIjdVhN9ZKRM54OJ0AO3HitBluyXAQ4YbREmc7j5toXrbcLhjPqQmo4f_YoBOQJZ_BAtHrK9RBN-SLRO7IPDyCbqP_6s9KsEwbEfAqyBy-PidGBuKzIMWQwWAB_YfxGMDNKn0O60CRFqnRe0B2keGprweNWkKeg8Lhlrf_Ji3bASRtr6kFQznWwwVG4FPezBGQq48Zv9AcdpTBLXPo7dgysTsG-_-c-EcThDzIbrJWEWa5SMHMbXre8lJM-wnNw9NUUrYbdEuniTq5k1krQqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=RdwUwYcCwSq1jT7ZSRs_TKNCppGHt7Xyp0H34t1MkFBVBWUUkqT0pF9YGZw0aQD1kP03mobHV7MAtXyLurL6GySBOeZlRVfqnLZsri_OuV_Thd9AQuKawTI1GHbh-gD6LGkFP7OTHQYaPUaojEqBPHQdJJX7TLX6EIgOJ_Jj_MOtoOuPSQkJ45Jc3WnQljO8nCbIzMv3VdUby9a9-3m-lFxLzSVQF0b7N9BFoJvbPnKwSTLPoLP-JDIBtfx36ngUTEL6cWuzVfpdCpP9TFRE3B-ikAk8dKVMCgWpC2BjyyGojHYzs4-qTB5e-1IinHoy0nmkv2vE4WGeYkC9IM4m0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=RdwUwYcCwSq1jT7ZSRs_TKNCppGHt7Xyp0H34t1MkFBVBWUUkqT0pF9YGZw0aQD1kP03mobHV7MAtXyLurL6GySBOeZlRVfqnLZsri_OuV_Thd9AQuKawTI1GHbh-gD6LGkFP7OTHQYaPUaojEqBPHQdJJX7TLX6EIgOJ_Jj_MOtoOuPSQkJ45Jc3WnQljO8nCbIzMv3VdUby9a9-3m-lFxLzSVQF0b7N9BFoJvbPnKwSTLPoLP-JDIBtfx36ngUTEL6cWuzVfpdCpP9TFRE3B-ikAk8dKVMCgWpC2BjyyGojHYzs4-qTB5e-1IinHoy0nmkv2vE4WGeYkC9IM4m0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=K9fVi9mVL-yuVFt6zjmZUJ0I72jlw8pPlPq17385f7lO2EM9R-3Akv8nKhhJwV7WbDjE_m_1zwlaEfpSp09DG7rkkbXBgv2t1WU-43T1Zc7z0aUbAbLQXyE3b3MqGZKEPQcF7BZK_Z4DxaXN2xsUnc1ZDNg3MhogQ8cYO6EpFnx21KjD3bl5Ka3HdoLs1i9QryEwFKfUIKPLR-t5nnyneoyniHtfJF0aRsOnznwY3DzrvSVMey8cI9yV9ZxbnIXLn3iG8pBakdCh1j3wt_e5ymoeTK7gzbfnZeFu7vOj2VHzUzH51qgb-xIsnoMdFGoaIb4kx-wDZru_v1Fi8Q6hYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=K9fVi9mVL-yuVFt6zjmZUJ0I72jlw8pPlPq17385f7lO2EM9R-3Akv8nKhhJwV7WbDjE_m_1zwlaEfpSp09DG7rkkbXBgv2t1WU-43T1Zc7z0aUbAbLQXyE3b3MqGZKEPQcF7BZK_Z4DxaXN2xsUnc1ZDNg3MhogQ8cYO6EpFnx21KjD3bl5Ka3HdoLs1i9QryEwFKfUIKPLR-t5nnyneoyniHtfJF0aRsOnznwY3DzrvSVMey8cI9yV9ZxbnIXLn3iG8pBakdCh1j3wt_e5ymoeTK7gzbfnZeFu7vOj2VHzUzH51qgb-xIsnoMdFGoaIb4kx-wDZru_v1Fi8Q6hYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
