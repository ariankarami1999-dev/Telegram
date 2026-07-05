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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 20:27:24</div>
<hr>

<div class="tg-post" id="msg-67348">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/news_hut/67348" target="_blank">📅 20:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67345">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/news_hut/67345" target="_blank">📅 19:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67344">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/news_hut/67344" target="_blank">📅 19:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67343">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/news_hut/67343" target="_blank">📅 19:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67341">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/67341" target="_blank">📅 18:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67340">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/67340" target="_blank">📅 18:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67339">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67339" target="_blank">📅 17:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67338">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67338" target="_blank">📅 17:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67337">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm-J8mdXqDkBr_GYo_c2Dx4iJTRUUb5_JNg3BRFsh5-XoE5FFhzQ78pZ5OFEwayM-fx0qbqo0VSWFp0hQpEFhkrbx-KfjAeHdNjLAvqqt6_U-5qXAEh5FvYOSLJlh9NyncoUscHZZvN-5wBx_-8oW3LDWAspJMQQjc8I9xXgKdbh68vJa36n-k_RMVg99DBYyn9Q_QBDK4gA5Vq4XBqJ5T6A8LK989zJtdl8ZxkCtqIveLdquG--URu5HD3BpesH6_SM4P6x3XkfdH1WEyb0nKSDgj4IcpodW9RYWK93lLuj-t2iHa6BZpQhAWkweoq5LD7C5tvZqRXP-TFCo_Rnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67337" target="_blank">📅 16:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67336">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/67336" target="_blank">📅 16:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67335">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67335" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67334">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67334" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67333">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imlaBmP8K5B94CcNALz1qLnopgVMnNhhP7CefwNXd94_raM1gkJcnzf6LgvOF748VqwOlXi5y8Jw763_f6lYIdzviBzrZvm5554MuY7HgC87d_x9hi-BMyq_k7SMaqrPdZ-dTLs_mAEnl1sqdc50tn2OBfvsfJCtEwRW_nlKrugNpLlaWjpoLpOZZvqpE8VFx77zgXx5FN2IJSJRJw_RfwyCgJ170w-gF8mTYLA3FF02GWvwNunJuTQ9-nB9IgrnUw5jg4QnmMJJA8mepfg-SAZD2dcKIXcQPFfrMULSdAsSMZYhf7yMoVl1xpSdKwKyFkM0cANdEIyQbPinoVq24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا کامیون حمل جنازه علی خامنه‌ای مبلغ2,298,000 هزار تومان خلافی داره
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67333" target="_blank">📅 16:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67332">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrSdbI3MRsl2wWIugJq0dRVlAXQW8fAYiacjo_jnWO6_FucEzIjs8MkV8551FR_d4Hd3OkESIoQbbKKLjn419RDZ9SuICgqOqKG4MGorkjaSR8Dsruh4cyQVO_PBhj7wO8QSvCQ92QwD3PqMl8ZjF5je40z5XzbIYunAWrfEQTmGDGO2wGfa5dS9tfOHQLeTlRMtpumS64yMM0QiVUs9w4dGmspgFHBIdIHkQFYLN31uoVSU_FszKWqe6ROh6hYTaaPN3AFrm5U37Eult-N5zNfhOkYnwE1lGSZyWhez4Pw5ziLQC0e9wphdPCOmCSn95D9o3onSODCAp4TpLrtYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمد اکرمی‌نیا سخنگوی ارتش:
«هرگونه اشتباهی از سوی دشمن، با پاسخ قاطع نیروهای مسلح ایران مواجه خواهد شد. ما بارها اعلام کرده‌ایم که از فرصت آتش‌بس برای ارتقای توانمندی‌های رزمی خود بهره می‌بریم. ما حتی یک لحظه را هم هدر نمی‌دهیم و تمرکز خود را از این مأموریت برنمی‌داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67332" target="_blank">📅 15:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67331">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو در جلسه دولت:
شنیدم در رسانه‌ها گفته شده که رئیس‌جمهور ترامپ خواسته علیه تونل‌های تروریستی در لبنان اقدامی انجام نشود. این یک افسانه و خبر جعلی است.
او حتی یک کلمه هم در این باره به من نگفت و من هم از او چیزی نپرسیدم. ما بر اساس ملاحظات و تصمیمات خودمان عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67331" target="_blank">📅 15:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67330">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgj0lbBM6XPEAKI75v5spsMaQIKN7JrXbzbrrSuDavPKpWCaaVZ_z8Z6l1KP_u0cpwZz6ETcTxBPIzMF3lcOi_7_IrhSrx7yH7VAJFVdSHVGvmfHsLoOs8tB8d3kpHUk1_W6SBUn5a_w2ScfN-QK4dKqMvr3N6KDsFqTLlTcVsxeQ3ewCx5hyVehKeyn4OHmGjhkUxYgT2_0cPu1_j0Y5txLLRk3pwzKiOG5j7N3WNptbhziuxIu0R70s4TivpuzCs3hKOsOOr5HGYp-YjPDWDC67vsLPvjtqzYoV2MXTnPmodBiBjEpAeuuMDLvcGb7nMtu1esq_y8kwiqvkZn7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویر ترامپ در مراسم وداع با جنازه علی خامنه‌ای که روش نوشته شده:
خواهیم دید چه می شود
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67330" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67329">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm3wpwJ5qVzehFZpCrX61LV87mMqTgWMiN6NFVDshzyEfedzYp__FxZsKIvCUIceTn8mquCih7uqOq5qKP1vCYoGEu5EkR4w8SHKDc-PbPF5TPy-UeZ-vWHAs1fxOGLuusegCaP2sxdxmpCdZZoUuqHCW8hbbXppv0zQQxQ44weoGkZHRETjSJDq13MUb5UdmsVusra_JwGO4NDp5bORBbi8AIn6U2FbDmPTvNmSVAsWU3o7gXIEpzBs_ohEkHYGUavrehI4qOTZyRnm0_COYI6KAXlrpBQvvh8bL9pqVTs_QS_o5CUPPbt3sH_bcVImKBfImlpP2l1nmUWrtqkV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسرائیل به فارسی:
بهرام که گور میگرفتی همه عمر
دیدی که چگونه گور بهرام گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67329" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67328">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=kdzTbY9D2BdJPZObPGwo_Zl6To6pCxvAx0M2QizX7SPFDO0qBB2-lMirO6kUScLDnmzD-Jn4BfAdGBNeUkSByp8ebSSjiitFxS1COfVRapepxwZzP8aW01Xdb5wt58KmdXrUdnV1TQrEj1bhOuwpzZcTwoL0LlZ-7fgFDKmG3sv78Lsid-xyXM9nrsgrghyeKPDGZqPfAk43ufKzTgqgETkSFCku0OGm7g5OJHKULsllXz1bHyTYNC29_ra6e9nVDRvLMHzKGsLcgXLFOy4E42Ljt8bbX1OsHYXxvcUsPtF73GLU4s7v_fwO2gtIzo4Oxki1A4G2JfbfAD5xvaxk3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8ead8806.mp4?token=kdzTbY9D2BdJPZObPGwo_Zl6To6pCxvAx0M2QizX7SPFDO0qBB2-lMirO6kUScLDnmzD-Jn4BfAdGBNeUkSByp8ebSSjiitFxS1COfVRapepxwZzP8aW01Xdb5wt58KmdXrUdnV1TQrEj1bhOuwpzZcTwoL0LlZ-7fgFDKmG3sv78Lsid-xyXM9nrsgrghyeKPDGZqPfAk43ufKzTgqgETkSFCku0OGm7g5OJHKULsllXz1bHyTYNC29_ra6e9nVDRvLMHzKGsLcgXLFOy4E42Ljt8bbX1OsHYXxvcUsPtF73GLU4s7v_fwO2gtIzo4Oxki1A4G2JfbfAD5xvaxk3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این بزرگوار که قبلا گفته بود بخاطر یه تیکه نون به سگ دادم اومده داره ترامپو تهدید میکنه میگه بیا کوت عبدالله ببین چیکارت میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67328" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67327">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
❌
دیوید کیس مشاور و سخنگوی پیشین نخست‌وزیر اسرائیل:
تنها دلیلی که ما امروز تشییع جنازه خامنه‌ای را بمباران نکردیم آن است که 10 هزار مأمور موساد در میان آنان داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67327" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67326">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67326" target="_blank">📅 12:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67325">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac4BNJdKFqVIJe_cfPKqTKvb_EVAOEg66WXMcbywQo9D5t05-Mmx_p2g-ODN1agpc9qk3-E7xBq7rMkF9dFerR13KLGullf06zN2_iJD35ANN7mQQvMbxK8iXpu2eG952_SipvwMhUIyWfr_6AWX0TvMfxieCU6qz8TXf_FFa24tIuzt7atsz87ois5SZ9RCQNaLJFOorJPD58A6w9RD5aBMWosRENSXpT3B-jrPFtwA7tusnklUEG2EEUl9byazNkeIxfyv8_jxx_FcW7kRnzoSiML_T4XA3v-MUQVRCBAqa0VkZHUaWqJwy7Et5anU43ECpU2ykIjWKCb4j7ngTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هرمزلتر:
🔴
نیروی دریایی سپاه با استفاده از قایق‌های تندرو، کریدور مورد حمایت آمریکا در تنگه هرمز را به طور کامل متوقف کرده و در نیم روز هیچ شناوری از این مسیر عبور نکرده
🔴
سپاه صبح امروز از طریق بی‌سیم به تمامی کشتی‌ ها هشدار داد و همزمان قایق‌های گشتی نیروهای ویژه را برای اعمال کنترل ایران بر تنگه هرمز مستقر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67325" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67323">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaB0osKUzDmp6z3ij2h6F5IuJc_2UnA_E4GzGrpS17rA478rtwXPUFHwDSAXWxaliA5OoE0KWo3ob2b4wtndC1O8w6KgBVcOVb9FQI7V1LCAu6WD0bX1J_6h5v4YOyVLHc254w9_r3XQJOOIirdcW81ZkELLtNd-KG4UbbhY0Fqnbu78oov8ZcDTUckpx1yZn-i6CTWBVEtnqh3DVS5bZwGrx94r-3G7ln9ok4Vl0t6H0z9CQmjs_yHNBGoLSsUnfXOx37FraI4V1LYG4aGlWwgu3eLPyOS4s1FeP5roMc4okXDGfrnsLe2BWB2WJFL0Ilfjq1MaEyd1cYYmS7GB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=PnlSlFQR-48f5XCqZvlHzS3KnmZ60LBSAFYh96fq5xkDKbDNoNLTY3SNw6zq8um0ThL8IUcDJ6I0XUHPqBbhhGCL8X5tqgxEk3_fVIft59owZYph7y77zY-qvAlhnhoBBTbVHYCbnz9zH5fSIQNqjXZtGtJOMcQR_ohTW-IYvcqGzKcSuYAeTgUrbExhgHuw5l2OIK5EgcJmq9rAii-RikJbOlWDUjd4O2dcVj9EyhPmlVDLATQg_JRGYKmNqz-WBXBQRbhx1Du2ffik7Lox5WcjgI1r2oJx8OrehCX-8nT9ZMk6ch_9o-7jvT2BuGmjWuB2mctN2WglTX1hJiGQHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f22dc07ca.mp4?token=PnlSlFQR-48f5XCqZvlHzS3KnmZ60LBSAFYh96fq5xkDKbDNoNLTY3SNw6zq8um0ThL8IUcDJ6I0XUHPqBbhhGCL8X5tqgxEk3_fVIft59owZYph7y77zY-qvAlhnhoBBTbVHYCbnz9zH5fSIQNqjXZtGtJOMcQR_ohTW-IYvcqGzKcSuYAeTgUrbExhgHuw5l2OIK5EgcJmq9rAii-RikJbOlWDUjd4O2dcVj9EyhPmlVDLATQg_JRGYKmNqz-WBXBQRbhx1Du2ffik7Lox5WcjgI1r2oJx8OrehCX-8nT9ZMk6ch_9o-7jvT2BuGmjWuB2mctN2WglTX1hJiGQHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بعد از چهار ماه همچنان عامل این جنایت و قاتل فرزندان ایران چال نشده و اجازه چال کردنش رو از قاتلش گرفتن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67323" target="_blank">📅 11:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67322">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=LjpxoXQpGdrLbuPc76Q-bVVz3NX4mh04wj6NDO33-UF_gvL_A6OXxJKuhOLt4E_UfbjCtg3WdSIeMywzIzG12jBc0f-ff9GlkXYCf4zS6fWbuXK6QI-3nqIwYSA-cU3AlygIs6tKFlIkktSnPpA-k-kSxCzBYwJ7Z5TwVROGwwzE8ojqM6mSlnSYnpKQtRJBI3u_2Fuf5UnLKfwcZNGClehxN7U8Jf3FBwcKt2XVZuMNUPddEunTLX4ncN92K0ZJOBhZpA3ysJ_wlsIzB9MzAlBNc2vgG-oguNGlDImk4OVyWgAyicK8l1CXc9RmDL_zJgEjPlJFWW7Lgfzo83eGAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5f6d58549.mp4?token=LjpxoXQpGdrLbuPc76Q-bVVz3NX4mh04wj6NDO33-UF_gvL_A6OXxJKuhOLt4E_UfbjCtg3WdSIeMywzIzG12jBc0f-ff9GlkXYCf4zS6fWbuXK6QI-3nqIwYSA-cU3AlygIs6tKFlIkktSnPpA-k-kSxCzBYwJ7Z5TwVROGwwzE8ojqM6mSlnSYnpKQtRJBI3u_2Fuf5UnLKfwcZNGClehxN7U8Jf3FBwcKt2XVZuMNUPddEunTLX4ncN92K0ZJOBhZpA3ysJ_wlsIzB9MzAlBNc2vgG-oguNGlDImk4OVyWgAyicK8l1CXc9RmDL_zJgEjPlJFWW7Lgfzo83eGAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رسولی  مداح بیت رهبری میگه برای خون‌خواهی اومدیم؛
شما هنوز خونخواهی سلیمانی و... رو نگرفتید بعد میخواید اینو بگیرید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67322" target="_blank">📅 11:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67321">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=qzjfrR74N8kUHThDdwDs3mutU0HLll60A-iRTQpeoNtEQFopPnYWr7DoEXtyJbgu-mN2xvsG0__G4_7zTHHOUqQ-6xMgg3KQ7__LZ85o3qJnh4zF5hdNx0VZGF1XPgmkCrgifT7F0btsN4JYRJad3N8F36aY8g6xvSBelKvOscRLaQKTTr_W4qhyulMhAR8bnpb6bmtyQjK0s_mXGPbcpM7ee_97nf2JqU_TXuJTw9HW_f_SdxUt0wmMInAu3SRGWpnGkrtw2pDrX6xSsvza_3Wmp4_I_t_TLdCbRTeO_wCarWy8i6sVfPssqhPpj0Dwgve4D2Qi8jdwSdnD86n4wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5807c7f54.mp4?token=qzjfrR74N8kUHThDdwDs3mutU0HLll60A-iRTQpeoNtEQFopPnYWr7DoEXtyJbgu-mN2xvsG0__G4_7zTHHOUqQ-6xMgg3KQ7__LZ85o3qJnh4zF5hdNx0VZGF1XPgmkCrgifT7F0btsN4JYRJad3N8F36aY8g6xvSBelKvOscRLaQKTTr_W4qhyulMhAR8bnpb6bmtyQjK0s_mXGPbcpM7ee_97nf2JqU_TXuJTw9HW_f_SdxUt0wmMInAu3SRGWpnGkrtw2pDrX6xSsvza_3Wmp4_I_t_TLdCbRTeO_wCarWy8i6sVfPssqhPpj0Dwgve4D2Qi8jdwSdnD86n4wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف یه 20-30 سالی هست درحال گریه کردنه
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67321" target="_blank">📅 10:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67320">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=l386xyC_fozaBtfIp6X07mxH80rnFVF545fmzsICpGJEmhAbH81XloOi-mVg5VTZWlyO6ONIjqkyWul_awtaSQTdEwKeuFSQyiYlpdPsX9vt5TIVExlbcaOjoq8ptPlUTyGOElhwSFBL5DCONWf_JcNQph1O1WgHrH2fhugGt8vNUifrNFwREhA-LClySY3Cxqx_miQZb2ZtVKD9bHgs-HJbH7i8FgT-LxkAWPExcoO0RsM9uCbvReMe21kZ40nZelWq_yP7hFI-9PtK08wHBk9f4UcLaiSvPysgMDC2Vnmde8cAJbRDO6Y4qQvYg6dAaxHEi1xvt7yK2V0XMgdh4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/810ada8a67.mp4?token=l386xyC_fozaBtfIp6X07mxH80rnFVF545fmzsICpGJEmhAbH81XloOi-mVg5VTZWlyO6ONIjqkyWul_awtaSQTdEwKeuFSQyiYlpdPsX9vt5TIVExlbcaOjoq8ptPlUTyGOElhwSFBL5DCONWf_JcNQph1O1WgHrH2fhugGt8vNUifrNFwREhA-LClySY3Cxqx_miQZb2ZtVKD9bHgs-HJbH7i8FgT-LxkAWPExcoO0RsM9uCbvReMe21kZ40nZelWq_yP7hFI-9PtK08wHBk9f4UcLaiSvPysgMDC2Vnmde8cAJbRDO6Y4qQvYg6dAaxHEi1xvt7yK2V0XMgdh4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان مراسم افتتاحیه مسابقات «فولسوم پرو رودئو» در ایالت کالیفرنیای آمریکا، یک چترباز پس از آنکه پرچم همراهش به درختی گیر کرد، تعادل خود را از دست داد و به شکل خطرناکی روی یک چادر سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67320" target="_blank">📅 10:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67319">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=ZU8HtOswhTN1IPsrpVpH3ea0Pf41sm85uoSJacmJApIPN47h2iJwqXjEOImor0MDbvOmxFrTlrl73wcGFND0lm9AU9EWRDahrFXKuppV0jmpZKDjZs1f_6Ch5WZcJLXgvdfhy0e0QcjHpCbr3Yt3IJS6q8V9K3bfV9KYSNWGJMrp2x2UvqEMYQUELr7wL_Fz8pO6F2CLsNkFafmK3losLGDCNZpMe3JkPuRotFnXAefciPq2d4pcI9e-jBmY18P4HNxUHBDNuQ7-0WTCSjm_uJOvC37lupp26aMvettLfDW87TBryUAHCazuVXgeZX_0OJHnLF-3ZZDe2wjSCelMqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ca0cec0e0.mp4?token=ZU8HtOswhTN1IPsrpVpH3ea0Pf41sm85uoSJacmJApIPN47h2iJwqXjEOImor0MDbvOmxFrTlrl73wcGFND0lm9AU9EWRDahrFXKuppV0jmpZKDjZs1f_6Ch5WZcJLXgvdfhy0e0QcjHpCbr3Yt3IJS6q8V9K3bfV9KYSNWGJMrp2x2UvqEMYQUELr7wL_Fz8pO6F2CLsNkFafmK3losLGDCNZpMe3JkPuRotFnXAefciPq2d4pcI9e-jBmY18P4HNxUHBDNuQ7-0WTCSjm_uJOvC37lupp26aMvettLfDW87TBryUAHCazuVXgeZX_0OJHnLF-3ZZDe2wjSCelMqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین حضور عمومی مصطفی، میثم و مسعود، سه پسر علی خامنه‌ای، در مراسم تشییع او در مصلای تهران.
مجتبی خامنه‌ای، جانشین علی خامنه‌ای، اما همچنان در انظار عمومی ظاهر نشده و در این مراسم غایب بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67319" target="_blank">📅 09:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67318">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=hN1Hqon8DbV9eofxzEtAiPV6Cs3agA8dNv6IMRuNRZDf_nSru7jm8R4_FlY24n0jA6p1Gu5vc5G6cXCwwnTt6C06YiCO6uJRnbyjRJiKizIsH2NA-0cuXt17b06GVrCi1_r0gxrbjeKhXRexiFyBVepHfVlWwnzO0PBx0wH5itr3XsgUqkXlqSZe1mrC6mSqIFSHsnn0cim6ZYOP_oQBlzL6_qgg-0BiJIjEk8tmN1rmkMjTeDn7oNXduWq85SPz9AHOBBbF6HX_dP7QIDufl4xUJorhGJABE83cuKJBuLvajELwAfnNR6qps6Tfs2KOICUO9m6Gnxmet7D_KTgPwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6157bafc.mp4?token=hN1Hqon8DbV9eofxzEtAiPV6Cs3agA8dNv6IMRuNRZDf_nSru7jm8R4_FlY24n0jA6p1Gu5vc5G6cXCwwnTt6C06YiCO6uJRnbyjRJiKizIsH2NA-0cuXt17b06GVrCi1_r0gxrbjeKhXRexiFyBVepHfVlWwnzO0PBx0wH5itr3XsgUqkXlqSZe1mrC6mSqIFSHsnn0cim6ZYOP_oQBlzL6_qgg-0BiJIjEk8tmN1rmkMjTeDn7oNXduWq85SPz9AHOBBbF6HX_dP7QIDufl4xUJorhGJABE83cuKJBuLvajELwAfnNR6qps6Tfs2KOICUO9m6Gnxmet7D_KTgPwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زاکانی و برخی از مسئولین تو حاشیه مراسم رفتن چلوکباب خوردن، عرزشیا هم اون بیرون زیر آفتاب، صف وایسادن تا تخم مرغ آب پز بخورن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67318" target="_blank">📅 09:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67317">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJKKjAZPMdnfKhz2__gcVjCP81-6WOnDym_9JiH9qUqPy7ySkRgJ450GDHxHEJvbR2d2fTf1iBZ_IlJsoXsaG8LAtYF66Rm66iXWXDQe1735iR7Js37SUmKSKK5IeGufHbt_yIsVjG4hXKqNi0jLU23vYB008YBsWupyX5erA6NPCSZiDhac-1HYgDTIIkJXEkUWDHlNdCctDeYRNY0c_iiHt3-dQbBz9F41_HioXYuinFCwJCFeoSotuEIulVeU50CAyz2ogpbME2HNsXc23L4jQbDmfWmhYldLoOhiNydhPRZ29gw1BbtWU36hEh_YWfQCjW90YHGK6gTarL9yXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
8فروند جنگنده A-10 Warthog در پایگاه هوایی موفق سلطی اردن مستقر شده‌اند.
🔴
این جنگنده ها برای پشتیبانی عملیات زمینی استفاده میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67317" target="_blank">📅 09:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67316">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67316" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67315">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WDfdGlSNMHmQDgPBEqpVQv-xAdkK9YR2mI6PfTwTAyJYLXu4_jHl4q7rUGmBToRT_Qsizvn-OwFloz0Ywp_RCT2651rEhJZhfaV2xFYE5njbfyeEuzXU1sRwvhHcbkmUhxCCbRmtjy-X_266iqY7T0h7rfusFGASq0_cQXAMVHJp_Wjj8Q6usDXRRBi1yhkJgSe-2HYx4_pXCyivfOuI2naDDWvOa4shwpW5zluBH_PnHDQyEPxFHdINppQ0CdqBJZZ0to0UAag7NfkfDUhA1VU8LHYGBXPc5M212K6yr7BiGvucsjKXk2L4HML9Nis0gxH7dIqyDpnrqRGKa4HjBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet
@FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67315" target="_blank">📅 02:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67314">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFqfwYEnYJns9kB63zx0WRm_-ZkGOwHi2VVRSAT4fiJhYK1tD-Dagb6iLc2aNA6kPQa9ONPgH5GEtWUBZOcGDhF6H5zHA81WigGEWLB4ACAFmBz0_mjHTZnFzH_Z9fF6m9Zp_gi3o2tsJlNRJQ6PHSF1yDxHYHkN1pTXCq32vATOJdN-bEFWdhd5SMqH5U2soSXNtxUxf4xEwOPoANk3tofV8_sAZjdMyv8ix8V4Sng5KPTNovA8vniWGq3pSjqDSazUw5-WfVZAMOHBKkg2hi6FZ0jEIE9ObxKBzJ4XUOQlPurdxPeOZEuOisd-dosiaWSk3aOmEixA2TirozNEzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
ولادیمیر پوتین، رئیس‌جمهور روسیه، با دونالد ترامپ تماس گرفت و دویست و پنجاهمین سالگرد استقلال ایالات متحده را به او تبریک گفت. کرملین اعلام کرد که این گفتگو یک ساعت و نیم به طول انجامید. پوتین از ترامپ برای سفر به روسیه دعوت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67314" target="_blank">📅 02:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67313">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67313" target="_blank">📅 01:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67312">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBmHBZEDtk6vawUGHKOj5OK_4y26ViC98_XWZFOCOdZ9oRU-FJaxrXByNzazfuW2DePuPgKYqzqsoEsTmcvXqVj5Gy95VLBvqZ4cAg83VqpqEK7jh1ti9OebcgwGzh8HrPFyR3KaOHb_xtJF6cEGdCiiMWUQK8RLE1oN8q3eyPhirzl-B54OXQJ_ZtB3m28BWucv_XFRQdtdvuv7MVTmyeLtnXvrbuj1c6FTiEusRmqwN73aLZveVTFUCqW-2CpbP95zrGnGkWvrvJwxs49KLbjWeXfjE-G9hY53FwYdkZxzTjFwpICvQed0tQTWtSyEGfVRI09OtBzEi9tGimbw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نیروهای ارتش اسرائیل در حال عملیات در منطقه حداتا در جنوب لبنان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67312" target="_blank">📅 00:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67311">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=rVL-7N6zoFXWPyYl1oQjwx3nFS2FBlLlXq6v1MtXc5XQm4dhcMxrzpW0NINBi9QOBhxkK6ykFuy2fIxaie9F6uwUeXOHNfOqbvowYPn5QuL8CoJqdJyDx7LdmUOD9ewc4TmHagJUJn8F9BYuHxOvJTJVzPjKfE57eslOUgQqfG1zcNarHsVviL_2TDREdRwue4TJKHdsIf8HXMVH3DRB_DBofCGDyHiWfZwwjvjWSuXVC-wAUAMqe44YyPzAWTsUFOhBzSJ82VJMY0xggI0R2m1dXxo0zf_4r76Ainz5JOOSxEfE3SWQV09RXjAiA9LyWTiqN7NVKWJiV-26wJfHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5be218b45.mp4?token=rVL-7N6zoFXWPyYl1oQjwx3nFS2FBlLlXq6v1MtXc5XQm4dhcMxrzpW0NINBi9QOBhxkK6ykFuy2fIxaie9F6uwUeXOHNfOqbvowYPn5QuL8CoJqdJyDx7LdmUOD9ewc4TmHagJUJn8F9BYuHxOvJTJVzPjKfE57eslOUgQqfG1zcNarHsVviL_2TDREdRwue4TJKHdsIf8HXMVH3DRB_DBofCGDyHiWfZwwjvjWSuXVC-wAUAMqe44YyPzAWTsUFOhBzSJ82VJMY0xggI0R2m1dXxo0zf_4r76Ainz5JOOSxEfE3SWQV09RXjAiA9LyWTiqN7NVKWJiV-26wJfHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی خامنه‌ای،‌ 3 بهمن 1403:
ده‌ها متوهم به درک واصل شده‌اند. من به شما عرض می‌کنم به فضل الهی این تجربه تکرار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67311" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67310">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67310" target="_blank">📅 00:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67309">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hl8Z-5FdHJB_hkxGrK7UffjhJVT0sXI4y5m68KycCspYSIGvaj4AJkPaM_a3xRnNdRbfLy_hv9uHrNZqq1NQ7h61on3-4hpKpa8ga6FBl8Hf2SaswGa0jzRME8TDlYmgOcXSvvvWrqkLveR9jWzUaSou1-IOlU0YRCOgRjz-LdjAXwfwhI7E_LFsvwAIK783yCuqWqLOvoeai_M_er_OPpaMaZ13RkhF_8qpe0uzu4OCbMtImabRRSTg9U_FUoBFozwQZ2NegHv0MrrWOZTxlclmS--lFywPBQ3Lee85UIF8_MrNCmfYES7rLYiKcRStlHfy6oUpgqdlX-JONrJOeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=N58GYgCAaSE4Vgb1zkPfwCoQ-05pMihXQOc5_MYN_u8LzhJeRhXJbVXCkLYAhCHc7NuKK0QUjeuHyWRSeEz6WeUTYwcpr9EyOLiSUrrXMSd8uPhAumRWIGPUdyLT3dKi7nu95-SlU3r3SvG7Ap0UhKxMfibFTCLeU_rQXbkLKUdVxqfMzWDbvodv_FcD7pq3GeUdbkzUikcJWQ5joL5_lHE7_5macRaa-RPWTWqpSmTG8ktASu3cZJaPUxpG1QsDz-gQieyDjrJo8t82HWspuy4lXTrcWyzAGUDBswpDrZHb_aNmGjk0pBH0hhTuhvKimrf6Q1qMXGm-KNLCgXGpOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842bb5b4aa.mp4?token=N58GYgCAaSE4Vgb1zkPfwCoQ-05pMihXQOc5_MYN_u8LzhJeRhXJbVXCkLYAhCHc7NuKK0QUjeuHyWRSeEz6WeUTYwcpr9EyOLiSUrrXMSd8uPhAumRWIGPUdyLT3dKi7nu95-SlU3r3SvG7Ap0UhKxMfibFTCLeU_rQXbkLKUdVxqfMzWDbvodv_FcD7pq3GeUdbkzUikcJWQ5joL5_lHE7_5macRaa-RPWTWqpSmTG8ktASu3cZJaPUxpG1QsDz-gQieyDjrJo8t82HWspuy4lXTrcWyzAGUDBswpDrZHb_aNmGjk0pBH0hhTuhvKimrf6Q1qMXGm-KNLCgXGpOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67308" target="_blank">📅 00:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67306">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4aopl4KWXxkN19FFlRCgRMKg2fWoX9VL-Lwc0fHv-M7c5O4qPqmth7kRP2mQNl5nBRhsJ8IHcSJTFlEZ1hvOMc2bzO-8AwAsvwfKRmW1SFEH72iWS8dvu4-R_CA5aeorvHDdDIto-ZYWuE-EES0yXB0N9ztDetdSHvBSC95ZT6c7XCfP-HZA7sScbpJ-MYiIg2tpVxFaCe7QxI9_W4prbUFNfqPnTp-iw6_mxOXLZBxqU12ga_3LDDD-ud61o82OOUcTdDTjDDX9nzGA4s55xz48Tk6-Z623LU3Xg2m1r8o31EAo37f2y7n5eB5OodK5ng92LN5JO_0b8eElr89Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=TCt2HlngNV04t1vpfI7r_EENOe0FtteVTOlGDysMW7so7OCASokKwP5B0wRLbA6mCc8mPiqYk_iAIe0stwzR41IpZwa-2a2i_DIMBWDWJ5EzGMslhRUqMDsAtReRGfiAv7Bq7MjP5FNUDAuC_bU--t4BjaILlNacRqQ1UI4dUidBNss-2QMOIJKLDrJeRDro5VKaXXF4AWFvmhppIxFuxESFQ8FYOXIrZmYuHDLo1z0dGihRxGW5l7xkd917Cxj2SRZLFdu7mp406M5JLFlSQBHhq9Euv0-R25u92m-pPWHp3OhDxejxeZ7wHvRzgLsTiFT6eYnRlagtX3l2BgOSJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ffa7579f.mp4?token=TCt2HlngNV04t1vpfI7r_EENOe0FtteVTOlGDysMW7so7OCASokKwP5B0wRLbA6mCc8mPiqYk_iAIe0stwzR41IpZwa-2a2i_DIMBWDWJ5EzGMslhRUqMDsAtReRGfiAv7Bq7MjP5FNUDAuC_bU--t4BjaILlNacRqQ1UI4dUidBNss-2QMOIJKLDrJeRDro5VKaXXF4AWFvmhppIxFuxESFQ8FYOXIrZmYuHDLo1z0dGihRxGW5l7xkd917Cxj2SRZLFdu7mp406M5JLFlSQBHhq9Euv0-R25u92m-pPWHp3OhDxejxeZ7wHvRzgLsTiFT6eYnRlagtX3l2BgOSJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از مزدوران نیجریه‌ای حالا یک فاطی کماندو از بوسنی و هرزگوین ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67306" target="_blank">📅 23:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67305">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67305" target="_blank">📅 23:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67303">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-aCEjOQM1v4J52UEHSVxzjRUk7HVQTQuOaobWE2KB1H8sMZXUPhBlE6MI6MXgvQpIy4BFYSs5MuFMQqmsx2ANH9QCtWkLbP1hEx6nimSp8XL4HxF-PQvpat2t7g_uoMDXphmLlMZC5t98GfjUD6TZdlDEtPPF8kQYZoofIe8GD9Rpdfk--Pt6bgsQ8GfXeL2ohC3JXWlTaMKY1ujQ_oUd-e4Ig5Bl3kicfnz6vmSjVKeN1KvoaKec9qecCJorO52B1MIHCN7Mt0v0QzG2BiIO98ToRakb75AbutUG8Gka7TdRM1aKM9CCkPVkU4GW_Ss9tfrJWgbl_QMrWifR7bFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UxmsshQ6yQpWtugMrbdiP1QPKkuBYbghoWKtACk58JwMSo2tQjPPttnPamL8a-b1tJFGhT463X26s5KQcoofomTRuSEH8CWCZSCtzP2THl-bqvd-bxPwIv77l-Uh1dN_zjDVWSpp0VeKHH7IQVsThA9hk3UG-k8boSttv5mq1VOyEsU9gj_qdCquiPyjIpWitr8aXJCeSSj5teJ1NnEXbg_gKE2VK1gCVwgJeOuY-zzyYEYb090q2fn-La2VwxwTQ8rXbVihprC3IIU0GUYHLDYcyogRXG2nCfP8vparZRbH2XBL9zs5CdngyK_yuUyjzUYX4RprIdTPa1DNoiB_4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زمین گرده...
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67303" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67302">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6ZumzaO1OvPIaHAijP_KRZ757dDm4Db2ZRGbUFAi7TSnprKKanqVWK47Ol_aAKIQTKoGa9GiXNh1Woj1tlXlHV0pRdk-MLRBvk02hyb-plEos735WrsdMhUEiSEra1G5QXfp2RQsj4yW8zyZX6ti_Yn830JLAgGX0vpPQLAWBy4xcePdHi5uIAry5Dzl25m6-17KB1fCDTkqaQUVivr_H2Sk0942m8uIb5szk1Tnv8XMrWOM1K3x0YTJBPfHImFTTWXq4d2-qqb8REcsnKWFzoUnJYms1Y9DDXOYWA90abiAL_c7FhAu31BwuueYrfLNPGbJEyLY3J3JM2m-QU-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
دو مقام آمریکایی به من گفتند که مسیر جنوبی در تنگه هرمز همچنان فعال است.
یک مقام آمریکایی مدعی شد که اکثر کشتی‌ها با سامانه شناسایی الکترونیکی خاموش تردد می‌کنند تا توسط پلتفرم‌های اطلاعاتیِ «منبع‌باز» (Open-source) رصد نشوند.
این مقام تأیید کرد که ایرانی‌ها تلاش می‌کنند از طریق رادیو VHF برای کشتی‌ها ایجاد ارعاب کنند.
مقام دوم آمریکایی اظهار داشت که سرعت تردد در مسیر جنوبی طی روزهای اخیر افزایش یافته است (حدود ۵۰ کشتی عبور کرده‌اند) و این مسیر همچنان باز است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67302" target="_blank">📅 23:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67301">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=i1YTZfcEOWl44FC27FvaqQ1txNsXfmZ1sb9iKTAZmTNNdZMDjPXjIQbOje24UcntseeZkAjqmoiUyMWsaUW9iN7PDjIOX9N_kN7Z4IT4AVDO9mvS4wAS7Ql5X3X2xYidS5Yj4RSeLjeRLojOtnCqZGi1MQ65ZNMiTOewgkcFUtW_l2h8wRaeciguZpOnwRSi_yUu2EE5-9VdIWXcngOSyK-5o0BoXe9uARZBexSf7cvaDdcwXTZggcswEMEuXWTuQPTL7f7tCmo34ccuqbC98EWNUJaUnsC4Vqq84Y2IKSyqgGXKujRc0gNPQHpo3wGq57erU9LuKHcsXSZOAwoL0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0711bc2f95.mp4?token=i1YTZfcEOWl44FC27FvaqQ1txNsXfmZ1sb9iKTAZmTNNdZMDjPXjIQbOje24UcntseeZkAjqmoiUyMWsaUW9iN7PDjIOX9N_kN7Z4IT4AVDO9mvS4wAS7Ql5X3X2xYidS5Yj4RSeLjeRLojOtnCqZGi1MQ65ZNMiTOewgkcFUtW_l2h8wRaeciguZpOnwRSi_yUu2EE5-9VdIWXcngOSyK-5o0BoXe9uARZBexSf7cvaDdcwXTZggcswEMEuXWTuQPTL7f7tCmo34ccuqbC98EWNUJaUnsC4Vqq84Y2IKSyqgGXKujRc0gNPQHpo3wGq57erU9LuKHcsXSZOAwoL0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم اروپا با دمای نهایت ۳۶ درجه
🆚
مردم خاورمیانه با دمای حداقل ۵۰ درجه
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67301" target="_blank">📅 22:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67300">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=BU86jMeRiafV4t-Ir3YqZ9MQiR9F0slgt8zu3t0CFhciIspVKNhlT_tBN43g5G9XlHlpkky2KODBtgJyNkCnRdn5nn4L_u_DoTxNgo5Lg7OLA6GQSSFcMGx4rAojTQGOlBa5mDZ2txSdWtueRbLq4GFh16ZtRJJgLJlAYn8l-T_XwoFlFuSRwZlFgKn1NyAOX5ek0sC_OAVQl-brAGuiJ1WBkKth6nSY6NmAq_jH1LfiiGEuePn4MAdorXtQDMTmPPIxHFD06Y2ena_TOeX_5tNfc3aA_OiskivHVUDCFwQCQdGKaUcBe6kHDrtpZDjn7oxCyk1WLQXFmRw5Cd2a5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda932d9d3.mp4?token=BU86jMeRiafV4t-Ir3YqZ9MQiR9F0slgt8zu3t0CFhciIspVKNhlT_tBN43g5G9XlHlpkky2KODBtgJyNkCnRdn5nn4L_u_DoTxNgo5Lg7OLA6GQSSFcMGx4rAojTQGOlBa5mDZ2txSdWtueRbLq4GFh16ZtRJJgLJlAYn8l-T_XwoFlFuSRwZlFgKn1NyAOX5ek0sC_OAVQl-brAGuiJ1WBkKth6nSY6NmAq_jH1LfiiGEuePn4MAdorXtQDMTmPPIxHFD06Y2ena_TOeX_5tNfc3aA_OiskivHVUDCFwQCQdGKaUcBe6kHDrtpZDjn7oxCyk1WLQXFmRw5Cd2a5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیام نتانیاهو به آمریکا به مناسبت دویست و پنجاهمین سالگرد استقلال:
🔴
«۲۵۰ سال آزادی. ۲۵۰ سال دفاع از آزادی.» او این مناسبت را به عملیات «انتبه» در ۵۰ سال پیش (که در آن برادرش «یونی» حین نجات گروگان‌ها جان باخت) پیوند داد و اظهار داشت که آمریکا و اسرائیل در ارزش‌ها، سرنوشت و مبارزه با مستبدانی که شعار «مرگ بر آمریکا» و «مرگ بر اسرائیل» سر می‌دهند، اشتراک دارند. یادآوریِ یک اتحاد مستحکم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67300" target="_blank">📅 22:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlzQ99_YeQldfTV5A82gkZkk3SME86cEtEPxFVst7e7FD5eNarA9sEyLdFp4gOye4LXbOKRVbI_ZKvNGoFF8SjCFZz5qppNOvD5qmNCWlr6B982tz30RPX4VLSj863gLeGEG5N4IYL8wmGkwMRhGOH7pabxohBnbp4LhMltYRsm1XQMCc5HyVSJ1dG5Iry7GfLamzGsVXFj-wQ0AWc_XTtZEHTlzLLED6JQyPc7ViO5w2TlsNAJlzUHQm4UZKJLUhr7XXB4eq7mmkBjyHi3bG2yOBtwNvyvaJAt0faZ26EanBFgb7Czp7RC2MUYeM20MMURKqu4vNs8_JIulCAegmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
دور بعدی مذاکرات ایالات متحده آمریکا و ایران در تاریخ 11 ژوئیه (21 تیر) به میزبانی پاکستان در اسلام آباد برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67299" target="_blank">📅 21:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCi1xwTenltwBAutcC1QguWhRKPlYeY1h2_DstoSGJYiHkvcyeQ4AA_YViFi8yUoPWcXw8nADhif55eDJVpA3-PjV2n7XhDPQD5ji4YbOsmhQCupgqClkqSPsludaM_cKH-SU9YqOFytjdDwi-BLNJeP7zWg5bTVTDeduI-OPA3LWC4BFgKJxRujV6k9V2eX8kSLSw1BJXaVs0O5sU0FWKIxV18fIllc_QGMe9vi5Urg9vxK8yxA6afHGWYABz-9JOM_qkunnBvdt2jHv7AD76MZHA3lQ16re7to9bEFCWtDx6EaV28bNasvXVeWWPQM_-B_UDiAt6zqy7hhxA6Ftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ:
فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67298" target="_blank">📅 21:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iy3__90fk_rQA97LPMonC0SMKJQrcBVhU5n8DxdtVzuvyRRham4-JWRdiz5b7oIGoeqvb0JRJqQk9Ckad9s5sKAVdY6eKaFollNt2Xqy_4eBtI1HbbvPqcb9LDkqjiqzgE6kct31lJUHYrJtw9xwLQPvBW77mp_lq625kfIsOBCwlHlfzZq0T6GjS2VmjQesWKOqYmL81Na3ybK-K5M9UcB7EV7jqZeDPZQEP-b0J8HURwL-C2XIwBtbdj-OL_srBN6I46nRrhhYAKi1YK5bPXn3ut_KIYyEn_Y-kuwoEebsBx_6cFvvSCRZPU7mnHsyvtAlLegLYrm3Hr4j5AuJNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ به آکسیوس:
نتانیاهو میداند رئیس کیست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67297" target="_blank">📅 20:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
نتانیاهو درخواست ملاقات در کاخ سفید کرده است و این ملاقات ممکن است همین هفته آینده رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67296" target="_blank">📅 20:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به اکسیوس:
از دیدن ایرانی‌هایی که در مراسم خاکسپاری خامنه‌ای گریه می‌کردند، شگفت‌زده شدم. من فکر می‌کردم مردم از او متنفر بودند.فکر می‌کنم آن اشک‌ها مصنوعی بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67295" target="_blank">📅 20:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ به آکسیوس:
«همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67294" target="_blank">📅 20:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/589cc62912.mp4?token=A-DjuCXQI6GbPLJLIlg0wefVPVEDQjJbP-5hvVHcHUVB-JNh9NNtb8WHKBDnIEmlfz_vHjmPzNajBN-VNG8kcvvQA71CGNCzgfR5hQbEzU-vCdTBoYxT2ABlDc27td3OfpjjcwUpavyyK-7NPYkqPQhi4WISvRQo3dXxJ40T6-L7iNAxdBNmIYV2EV62gY-cazxOhrqLeoeqxk8jvhZp6s5v_TEHAOCb5ASPJYCLQwa1_PXC9kBpj9aAJmQxH8wpjp8eIOWnmUd1Y7vdYzKPetetJghnQZG45Axiw9lygDhYgW7zd70dp3rAhMzufp8mJZkUupf120v148HFA9SV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/589cc62912.mp4?token=A-DjuCXQI6GbPLJLIlg0wefVPVEDQjJbP-5hvVHcHUVB-JNh9NNtb8WHKBDnIEmlfz_vHjmPzNajBN-VNG8kcvvQA71CGNCzgfR5hQbEzU-vCdTBoYxT2ABlDc27td3OfpjjcwUpavyyK-7NPYkqPQhi4WISvRQo3dXxJ40T6-L7iNAxdBNmIYV2EV62gY-cazxOhrqLeoeqxk8jvhZp6s5v_TEHAOCb5ASPJYCLQwa1_PXC9kBpj9aAJmQxH8wpjp8eIOWnmUd1Y7vdYzKPetetJghnQZG45Axiw9lygDhYgW7zd70dp3rAhMzufp8mJZkUupf120v148HFA9SV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
۲۸ دسامبر ۲۰۱۱؛ مراسم تشییع جنازه کیم جونگ ایل، رهبر کره شمالی؛ مراسمی که تصاویرش به یکی از عجیب‌ترین صحنه‌های تاریخ معاصر تبدیل شد.
وقتی این تصاویر را می‌بینیم، شاید اولین واکنشمان تعجب از شدت گریه و شیون مردم باشد. اما واقعیت احتمالاً پیچیده‌تر از چیزی است که در چند ثانیه ویدئو دیده می‌شود. در کره شمالی، مردم دهه‌هاست در یکی از بسته‌ترین نظام‌های جهان زندگی می‌کنند. از کودکی به آن‌ها آموزش داده می‌شود که رهبر، شخصیتی فراتر از یک سیاستمدار است و باید بی‌چون‌وچرا به او وفادار بود.
از سوی دیگر، در چنین حکومت‌هایی، ابراز احساسات در مراسم‌های رسمی همیشه یک انتخاب شخصی نیست. بسیاری از تحلیلگران معتقدند که آنچه در این تصاویر می‌بینیم، ترکیبی از باور واقعی، سال‌ها تبلیغات حکومتی، فشار اجتماعی، ترس از حکومت و گاهی هم منافع شخصی است.
شاید مهم‌ترین درس این تصاویر این باشد که وقتی دسترسی مردم به اطلاعات آزاد محدود شود و فقط یک روایت سال‌ها تکرار شود، همان روایت می‌تواند واقعیت ذهن بسیاری از افراد را شکل دهد.
تاریخ بارها نشان داده که پرستش شخصیت، فقط به یک کشور محدود نیست؛ هر جامعه‌ای که آزادی بیان، نقد و گردش آزاد اطلاعات را از دست بدهد، ممکن است در همان مسیر قدم بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67293" target="_blank">📅 20:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/648e669177.mp4?token=P8EmO8Sr7uRtjjJ4-2yWpDmBsNUMiwqWyNgOulBnhFntJGyEIDwe3m7qpkGdP-DILhJXqv4DiyfQXGf88UO34y07RlBKK7FRnDtgNRhrpp1oX-NA_VQ1q1Ge3S8LfVD92ULLHrhD926hmLuidSGuxLXQQEttl-OACmui83GapWtV0VIIb45MrEdkHiWa87eLJQe6TRtilU1Ev_LvI370JTvd3-SK1c_Ad2x4BZ6RDoBbmD2xqV87L2DwUMcsDqTptqDXJX3Yr_nacv_qcvwruNfFbS25Gkt4yNnZSJXUBp7Oy9CtHIkXXTGDawI5KTUQ8LtCEDcsbOj4jz1oc3-S6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/648e669177.mp4?token=P8EmO8Sr7uRtjjJ4-2yWpDmBsNUMiwqWyNgOulBnhFntJGyEIDwe3m7qpkGdP-DILhJXqv4DiyfQXGf88UO34y07RlBKK7FRnDtgNRhrpp1oX-NA_VQ1q1Ge3S8LfVD92ULLHrhD926hmLuidSGuxLXQQEttl-OACmui83GapWtV0VIIb45MrEdkHiWa87eLJQe6TRtilU1Ev_LvI370JTvd3-SK1c_Ad2x4BZ6RDoBbmD2xqV87L2DwUMcsDqTptqDXJX3Yr_nacv_qcvwruNfFbS25Gkt4yNnZSJXUBp7Oy9CtHIkXXTGDawI5KTUQ8LtCEDcsbOj4jz1oc3-S6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
▶️
داده‌های تارنمای ردیابی پرواز «فلایت رادار ۲۴» (Flightradar24) نشان می‌دهد که یک خلبان آمریکایی در آستانه چهارم ژوئیه، روز استقلال ایالات متحده، با طراحی مسیر پرواز خود بر فراز ایالت اوهایو، عبارت «USA 250th» را در کنار نقشه جغرافیایی آمریکا ترسیم کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67292" target="_blank">📅 20:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67291">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=bjL2LHiMTLrZLRq7Uh9ToaE5YjRh2Z1B6HYUblqp8SWts7ofoQVfdEL7AoV5DpZOBtCaFxYoa99AnUPdniwJaQUVWAkxayIbrNXOW4kzZJLVyeTqNRAnSzvhJ2FyHigkdRoQzKcAXS0TXskQ9y24CZcP7OoFPEREi2OxPv3PmNJ-ylFddAX-VGnVjWlGYq5WTSKXKVRhdfQ5lvQykOTIJWRtGHAs-4v7qe1tbL2d6wOTVDCUDeJct9Zr7_Ddyaz2PtQWAzdSLEDoc9FNJafLNxVWFQtpzHiG1CkfUQ6A-QkcVScvL6wyNIkhDJ5f-p5YRaoHjk9jHd6jloqp2Y59_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc795d411.mp4?token=bjL2LHiMTLrZLRq7Uh9ToaE5YjRh2Z1B6HYUblqp8SWts7ofoQVfdEL7AoV5DpZOBtCaFxYoa99AnUPdniwJaQUVWAkxayIbrNXOW4kzZJLVyeTqNRAnSzvhJ2FyHigkdRoQzKcAXS0TXskQ9y24CZcP7OoFPEREi2OxPv3PmNJ-ylFddAX-VGnVjWlGYq5WTSKXKVRhdfQ5lvQykOTIJWRtGHAs-4v7qe1tbL2d6wOTVDCUDeJct9Zr7_Ddyaz2PtQWAzdSLEDoc9FNJafLNxVWFQtpzHiG1CkfUQ6A-QkcVScvL6wyNIkhDJ5f-p5YRaoHjk9jHd6jloqp2Y59_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
یحیی رحیم صفوی:
بین ایران و اسراییل جنگ موجودیتی است یکی باید بماند
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67290" target="_blank">📅 18:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI96dlJ0WWYE-uqB33TWoZhs7GSPi6YnZEE9Ia49mQ4H44bHmPqsO5SR6LoioyZKS8xWYtSOpzY-kPQzrFl6lI99OpN26_wAy_RZikgf3hgCHRYwMNKsFAqCcmsvJ_dTW1NdzsgRlebjqZsy3VWIRWY8wa9gLfDBoKcMzSopXfQFhiTg80sZAVMC39Yz9l3wepok8QkRW4tIq7YHhpsLSGs0frJHAcl53Jb6VvhMaXoFPW8rHYJY9N-n8AQrjm3UDr1MEyalLbnl5tKQvkXChCWq_rx_wRusdmxLTUIGh4Ciy5HeGLh5KOLVXilbw2eQkqp0mYwGtMvcCbJizw_mkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=GSWpTRoXxms-jRaHl6QN_hKsMaFaInF3-uLSTZfVnnoRSCdfpnEdxEVwG7KRx0puwi5BOHobW9Qb6wbt08Qz69-qLddgnG6aXmw40ZSsaJbIvo8KXLyj2kzkCAl4N-htljAGp5Zv1AnLh7gSESpeTtx1Czw4aA03Jaluhi73hcVQjGDYTAoBn1PbxRYx6KkwVlvnbbNJ_mFeHhiXUwPOH2OSbZiDZvt5Ysphjw-7vITuXz7-1pbwgZqU9xqNSAjuWoF_5ZHR1KIfiLToDdUMEqTFOJZtRyP8m-DfvgYauLuPITEWnlvEbV-AYSxyiY84jInovIO71Hto0sLbyqjkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20335e95a0.mp4?token=GSWpTRoXxms-jRaHl6QN_hKsMaFaInF3-uLSTZfVnnoRSCdfpnEdxEVwG7KRx0puwi5BOHobW9Qb6wbt08Qz69-qLddgnG6aXmw40ZSsaJbIvo8KXLyj2kzkCAl4N-htljAGp5Zv1AnLh7gSESpeTtx1Czw4aA03Jaluhi73hcVQjGDYTAoBn1PbxRYx6KkwVlvnbbNJ_mFeHhiXUwPOH2OSbZiDZvt5Ysphjw-7vITuXz7-1pbwgZqU9xqNSAjuWoF_5ZHR1KIfiLToDdUMEqTFOJZtRyP8m-DfvgYauLuPITEWnlvEbV-AYSxyiY84jInovIO71Hto0sLbyqjkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
روایتی تصویری از شاهنشاه آریامهر محمدرضا شاه پهلوی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67288" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67287">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=NxBaOI5SsvKdwdTyITFsaCDN_9cMWrNFutdmwXXWSAV_tJlxYRnFSUs4Z7KgmUp189tbDH_dagtZopE2-S8oWdVy9VNYdJXrdwJrTNWyNaKJ4Boohk6To_Gg7NVAqAKH8K6VvoKVgbURyaQCHkMlN16i-CU6DAFr6pUx6bNOFFb7H2hp25uaGtEJBB-qbee0F5tbuPu92ME2E_qLLMG762RFGIbVCs6o9GttqiNgXDl9GGACVtRysRv6aRmG5E6uUXeQNNIn6eM_HkVxkhqGRuOO5qhEbSAtO82isAgZ-6j3ifMPCjmgNTglnvsq4zHQcqePZ_wezlkX-lzB_UzlRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90b7a34aa.mp4?token=NxBaOI5SsvKdwdTyITFsaCDN_9cMWrNFutdmwXXWSAV_tJlxYRnFSUs4Z7KgmUp189tbDH_dagtZopE2-S8oWdVy9VNYdJXrdwJrTNWyNaKJ4Boohk6To_Gg7NVAqAKH8K6VvoKVgbURyaQCHkMlN16i-CU6DAFr6pUx6bNOFFb7H2hp25uaGtEJBB-qbee0F5tbuPu92ME2E_qLLMG762RFGIbVCs6o9GttqiNgXDl9GGACVtRysRv6aRmG5E6uUXeQNNIn6eM_HkVxkhqGRuOO5qhEbSAtO82isAgZ-6j3ifMPCjmgNTglnvsq4zHQcqePZ_wezlkX-lzB_UzlRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب در تجمع شبانه علیه قالیباف و آمریکا
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67286" target="_blank">📅 16:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67285">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=YeF9JWdwDVs_lFxXuZsNCRhIgxUOV566S_o3IHmiD5OXjHasIlR8lDK-Xqpx3om4NGQgGtzYp1H-8Y4wRZSRq0XZQK4sxBQCoFXY0WKmmrPdrtRF7Kzf234ZDHYacFddgO63jgv7FYPGGgLJXEUHd6LbQ6rX5UD0wHiW7b5hYUpPwGM13GfyJUKCstSTh6oRYqVvOAZ8WIdnA04l7G4vFaiJcRNlk_HZd4zMgzz9V6UV_NgYIWGZ_cFWNMxIlFIk6FWWaJz9jg1EKpdjfjY8PCatS2dIlRxQ4OTABAmXyFzqcrmDNo3bSkBP-U6xsNy4-ydAV3ZHHBBuZVthxmx5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441130dd0d.mp4?token=YeF9JWdwDVs_lFxXuZsNCRhIgxUOV566S_o3IHmiD5OXjHasIlR8lDK-Xqpx3om4NGQgGtzYp1H-8Y4wRZSRq0XZQK4sxBQCoFXY0WKmmrPdrtRF7Kzf234ZDHYacFddgO63jgv7FYPGGgLJXEUHd6LbQ6rX5UD0wHiW7b5hYUpPwGM13GfyJUKCstSTh6oRYqVvOAZ8WIdnA04l7G4vFaiJcRNlk_HZd4zMgzz9V6UV_NgYIWGZ_cFWNMxIlFIk6FWWaJz9jg1EKpdjfjY8PCatS2dIlRxQ4OTABAmXyFzqcrmDNo3bSkBP-U6xsNy4-ydAV3ZHHBBuZVthxmx5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3Brh2eBfMaQm7If5SrCK4V9uoLczD6BNKwD3rD_CT_pFxEWhU9cWAv9VEh50Umiz6cqCECvI5CSOTGcTNyj20tCD7jhFChnbzBfAv5yk4_IkZLQjYYrTXqt7YlejsLoo6YCAtvge5VtRMc2f8tnqkcM9eq6sftd846UM7x8ZcJsxcBrqWKE3Lds-ISLRn_Cc-cNtAnjQEbd3uQnNR-Sxfk9cOdmW4-Uig83dZrupuBbIyuY7GvIxaj3NrkkQtfR9Yg5rKwI1-dAFiSkT52FcIw4zXpB1FZ2z8rMBhpsXh1-mGmgrcaTXlg5ei4a8fqRZC_5N8CQ9j6rubTQMbc-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی عظمایی فرمانده جدید نیرو دریایی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67282" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67281">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
با تصمیم هیئت دولت، کل کشور فردا تعطیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67281" target="_blank">📅 16:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67280">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vap01okg8__5__6TGCW_ruEP-a150Uj5nN-OzPamosRmwyIgPuOfsV2K5H4lfRD6TN3HzvFfJdAEARHZCs-JX7wjnEZNg6dj-5djAjfn0AZaShCchK7gVF1gtaAq4kTp9CgiJJiUM9KLNQCzmnitLsUCKTKlrcFphMZasM1sIt5G8XqsYPsGU7YtO0uQd7LaMOT6bhBeiSA31SjgqVMnxTysNeHn5jUK6ibniFQjsI4oqpVQPelBzgSCc_-p8rqr3OFJR79wHb_d_I3U4wQbQuGuM4QV9iSyYtdI9A_kvgL4kfvDzNbZmSjX2mvu7FgfZ_FVeLx6eJxwGGC6WaAKzA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5HQmcgn7w0ejOaG6huu38ImxWz9SbLAETXjX3VvUTmfbMFxnbGytwr4CmE4yiRFTglRXXvHARO8BV8ONsKM79Sf_RocLUEP1nV4h6OTw-SWlN-fHiQ8PP0kF2UaWOwW9Yi5nTJwEe8IEbRAaDm3lvBjA1vbodeyuuQ_YH-ZHCCss1438JudSllCFoYsRMEzGE8nA4o4jivjJlYDgMmIYEL2-G47Xl0vytSCUKejmpw4lVXK6VQazxnPZeWlc7aHUea0JdwxcSs-oBwMc2QLDr1vQSvMwg80SmMEErdakZ4q72oNqH24VGkSpOEh7WEg7zksG7-2uGzf82fqRi4okw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWzzrfOLkhEsRFM8zpZ-kIt2Y7be7BlijobMR4Nfvl347SBHOfn2_qWt7D5GurCZmNpOuJe1E0Ie6ZkguJXaNgUz2qprUtLA5n1SLkAo4NTLxZJrKfEZ93vY6kNEdqLKr8v3RQtUvazMILEHGbbAOYnb-XgVCIPrACtPCMHzHhGcBkLmpZP9puh3d2KevBwh8-gC5oGBE2MCbKvXVZiWbSvnYeEPiPQ_vIsT0pojubj1nKaxAdAGaqXNxYD_RySW9dhuxfJRrGzo0Gu52WjKmzmeqTnHwMdHjImvIpWT8Q6oXGMvT8W-a3naFnZEjz6bxGac_gpHfiK_SdTkrhpFCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=vxVIsXTOZ2cAVPwh-GZj6RMy0hoFsfPnCvh57wjsbErm5HbWtm4hStyjZXurh5mr9cVdBfUAbY9Oqz_5bjRIdv8UkpCfnayFam566NVoY4psE3Jco251DWiQIeSwLI37Ic7E-QzYPtwdlRsLLZUZOYbc45YaK7QXwbsKDGqiZh2tB3FPomyAFSTURqf8A_Xcw0VLroXg3Nqw2WN0blhdvYRVk9y0AeAZlt1jL_CsrzxTpSDreMxSUjWeu57BxP3zUQ4S9uQ_lgESS-q3Yuo7Z3irX9LS1ObVzym8BNnKJMwaAobA54xzXBgnRIzrKaGYbGVGltBv5F0Wg3rN7T_2PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502fac7d76.mp4?token=vxVIsXTOZ2cAVPwh-GZj6RMy0hoFsfPnCvh57wjsbErm5HbWtm4hStyjZXurh5mr9cVdBfUAbY9Oqz_5bjRIdv8UkpCfnayFam566NVoY4psE3Jco251DWiQIeSwLI37Ic7E-QzYPtwdlRsLLZUZOYbc45YaK7QXwbsKDGqiZh2tB3FPomyAFSTURqf8A_Xcw0VLroXg3Nqw2WN0blhdvYRVk9y0AeAZlt1jL_CsrzxTpSDreMxSUjWeu57BxP3zUQ4S9uQ_lgESS-q3Yuo7Z3irX9LS1ObVzym8BNnKJMwaAobA54xzXBgnRIzrKaGYbGVGltBv5F0Wg3rN7T_2PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب، برخورد یک صاعقه با برج وان ورلد ترید سنتر در نیویورک
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67277" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMHSIMwhjsgNcw0muUoiP-W6wKmmZIbB5nfQoNebDg9iTD8nNhQorS_XwREr-5aDVHHYPsSlfrbAcYp4Qu-A8F7h6djOI9jgP5rwaRJYzB9VzA4q-BEFJ_HXIBBObZiEayUbCSyejjry1to5oi1xXlGO9CKDe_YukMkByDfwXf2EstUlxm878LvO1oNbIZx70W6-giTh37f20Vyty68x2txBP52U8RXBgJpJg6OqgFtoCrUqnRDvrK6tRJgYZrPeSGVtJv37vT_LJJ2rdfey-5k8kWYR62YPr8WQH6UxjYenKWUa4ZvUSPdBVoqWvepay_U8gmDJxwZx-fcXuNxw-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67276" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCSsx14LqIJ9pG_CnJRKiV_T_EK5nKcr_UNasve6jZdgqIbZxqjQE33A5RaaMWsY6fnKkCLS4i4-iPEfS156SiuVaHFPrrWeN6klSbF6NKLeaVdeoJGluWvzcvKpOdPmoxbhAbWBN0WetcyGZJG6kGBc8areBVD7FeUGf61VR0K74YBlObJTI815ITtS3BOaUuBa4yikbFUGJn1WeM0h8ozTL4SV_CCIh6n16-CyL8CXqZL5fRZuePvAj1LfR0zlWx-016Aiv3Uf-Q5oOMLg6n1CpmRNvy9BEpAMr41S_BGX9Rz_gLHEvy6DIorEZHtfVIqwWQnLpJ1xo8oqBE5cXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمال مجازی‌شدن مدارس و دانشگاه‌ها در سال جاری!
🔴
میزان کسری گاز به حدود ۶۳۰ میلیون مترمکعب رسیده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67275" target="_blank">📅 14:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DksWcaoffP1Pr8yNBtLZeP82y--_6uDg4mO1QsKi0lortPkWpB4o-9JbH6CZOVGrmMF_348IevkFFTTa9KYrsOeYMp7lF-8xQXDzYGhQ1X277Y7_gf-aCmW47hkVyCwBgRkhBxZ0qKxxPd7mA57ONewDG1PYvj-P65cJKRQ6VgYHjGQMIHekmN0OE6N4pgxQXhkPuLFeZ1_NfJEK83u12-GEjwvd9Hw2d-8lkHX0u4BReicgEk7389dSrNzgCiUSgKgjvtQc0pzCTkbJMYHmZCyxB0GWd_U1JONdQ1MEYWFve4goGmImX9CssYVtdtmXk15TJ9d48hl85qcgTDs-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=OsG3ibwuJzQ_Sbfwyhj3bKRVBD1UGXQzkiXkimECr82KEwGQ-XkxG1W58c7R9vOf6UsrbvcpXKxwwUkKtDRTReMMAMtG2iGAzRDDw0hR2ycJGqU9JzjvKaZuTnl7YgDjzR2-eCqXwOGCxSGPnt8cK8_SGZe5vsfvEfb8FVx34MhyeN76f2ET-WsLsEwaSPsyxQcfEpFCWQNufiwjGUqxM2A7DTx1hwhF-T2UgDj3IHyRuLdlok61A_eyiv2Sco2kRcpEGTyrVpxX_-glFvg4sks9GDA-IVt6w2kLofnC0Ha3IdgsP-djITsJAroMcSzGlSN4s_lCwzh0qKwa4iM22w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=OsG3ibwuJzQ_Sbfwyhj3bKRVBD1UGXQzkiXkimECr82KEwGQ-XkxG1W58c7R9vOf6UsrbvcpXKxwwUkKtDRTReMMAMtG2iGAzRDDw0hR2ycJGqU9JzjvKaZuTnl7YgDjzR2-eCqXwOGCxSGPnt8cK8_SGZe5vsfvEfb8FVx34MhyeN76f2ET-WsLsEwaSPsyxQcfEpFCWQNufiwjGUqxM2A7DTx1hwhF-T2UgDj3IHyRuLdlok61A_eyiv2Sco2kRcpEGTyrVpxX_-glFvg4sks9GDA-IVt6w2kLofnC0Ha3IdgsP-djITsJAroMcSzGlSN4s_lCwzh0qKwa4iM22w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzqDkHNwWl12rRnTaU75A0MerivNfSA1iAuogrUZzH2kSW8c0uG5nfIEr288nPzqRT1JuEa0Dk1zEByQS4Kna8ZjbbRibf0lzgJJS4ZquLFiPmrgEVD4AxbRAHA_eI2oK_fXGCMFxTvHLRs-fOMkyqLH3LAlHNADEgdZS6boi4pU4iwBCfXzuvoBsB8nscBcJAQ8wGzmOdQ2FGM--ncjYb1pliuytpKiVIM8yqlnKRFvnqHg1ruHpAvV6PtAAz9h3H7kcKn8Chv6WILoslnt5jzwi3UchD37wATWidzbIqqbhglNFQoyWmRBP_85MM0LT-_8uM-eYmlDQIr7vfS5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=kxVsyog_2j_Pn6o-93Q75s4wzh4HrVkmwL7FXY3lyGXniGwEtYjmoDNmGJ8NWNbg3NPS9Zbft4-HI8EPD_ZdyKr57DGbLHJvP_EY21F5wcQ0-_HPIKeYzSma_B3KmD23luskwxUS32hilv_0N_OCApXJbT45c_JB8B3w1uK8KPcnA5Vzoivj85ul0nnp5AwLyrZ6DEDnKFxz_naMafe2l5_IuDGwiaw06FKhmjwnIJJZOWF_SOBU_NC249Y-DGgTXxzjwYJh9x69Nyw84FB1qIRPhniOAIZekIZ6gC02LSZ18tvdfDX2Q7ovF-UEvNrJx3ig4pQHlQ4KjxERZLmBHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=kxVsyog_2j_Pn6o-93Q75s4wzh4HrVkmwL7FXY3lyGXniGwEtYjmoDNmGJ8NWNbg3NPS9Zbft4-HI8EPD_ZdyKr57DGbLHJvP_EY21F5wcQ0-_HPIKeYzSma_B3KmD23luskwxUS32hilv_0N_OCApXJbT45c_JB8B3w1uK8KPcnA5Vzoivj85ul0nnp5AwLyrZ6DEDnKFxz_naMafe2l5_IuDGwiaw06FKhmjwnIJJZOWF_SOBU_NC249Y-DGgTXxzjwYJh9x69Nyw84FB1qIRPhniOAIZekIZ6gC02LSZ18tvdfDX2Q7ovF-UEvNrJx3ig4pQHlQ4KjxERZLmBHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=JFtGgAMvRaPUjHL27iLEdyAfcMSPH13LThXoZLUg-vBmnjyEkbnL4y-tKljKff64CpUXR3Z2y3u6EiFuPrF8cdL8h8y2f1S6-3iNjrAgp4Ep9rkWBdryCsPPA82hVVhSdEXWRl_L-odBFGbPztcDlTKuXYv4f1JCUdBZNf3aCHei-FYnS72RObcYTwcLyvvaXbyGPg3uemAyIpvK_qeHDczJ29oMRRh3f39gJvTn_vrcRWYnYa5YObM4SGL-MXfirdpLk1o02FCklYp5RlZB8sKbYGGg3JzF2IrqrCVPGRa6zhSY9rcLd9A1d5ImwIlyU76j1lIPp1DkZezZ6jwznA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=JFtGgAMvRaPUjHL27iLEdyAfcMSPH13LThXoZLUg-vBmnjyEkbnL4y-tKljKff64CpUXR3Z2y3u6EiFuPrF8cdL8h8y2f1S6-3iNjrAgp4Ep9rkWBdryCsPPA82hVVhSdEXWRl_L-odBFGbPztcDlTKuXYv4f1JCUdBZNf3aCHei-FYnS72RObcYTwcLyvvaXbyGPg3uemAyIpvK_qeHDczJ29oMRRh3f39gJvTn_vrcRWYnYa5YObM4SGL-MXfirdpLk1o02FCklYp5RlZB8sKbYGGg3JzF2IrqrCVPGRa6zhSY9rcLd9A1d5ImwIlyU76j1lIPp1DkZezZ6jwznA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=anq4S8OXI95RYL7H9ZXfaal746jxtrHAcm501S8DXxnu2rG7rTfZwkl_xrHfoe8ZSMTwi_0eUYSn5DNp14EFZJ9vNclzfUH4sDRqxxQ_459c-FpYSg5cPm2dmxeSYMVBbRjW5HmGVwSqY7_1th9RjOPqxpRhSo9H1vvbwuFpV6LQmDLhPJ8bMLxEy5F4UV_9FGVTMLxjNxr2EH3BLjXnm5LJdYhwWuJbe0ItnP8LhHjE48y2aLOUGCa2pKqGg7zdeJxO9m4DV4WU0UpzxmTpz4WjFIrbYhd3JB6GFYcEcrjbFpoTjrFEunzldAuFKcCQNPAyKCpgJvjV1HdcQ_BP2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=anq4S8OXI95RYL7H9ZXfaal746jxtrHAcm501S8DXxnu2rG7rTfZwkl_xrHfoe8ZSMTwi_0eUYSn5DNp14EFZJ9vNclzfUH4sDRqxxQ_459c-FpYSg5cPm2dmxeSYMVBbRjW5HmGVwSqY7_1th9RjOPqxpRhSo9H1vvbwuFpV6LQmDLhPJ8bMLxEy5F4UV_9FGVTMLxjNxr2EH3BLjXnm5LJdYhwWuJbe0ItnP8LhHjE48y2aLOUGCa2pKqGg7zdeJxO9m4DV4WU0UpzxmTpz4WjFIrbYhd3JB6GFYcEcrjbFpoTjrFEunzldAuFKcCQNPAyKCpgJvjV1HdcQ_BP2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=l-2YBOjej8LCY_OzCXhn1hsx88StJjI79g4xPXaDCYi8BnckWVoB8YUPUo4rvij8gSNyi5BgahZ3oQfB27WT9X-TIOycAv9yhBDCueeUl0R5sP81AmNpfxVEA5Elt3mXDBjuqXTcFmihH8XATWsCjp6R8ZYLPAPm6C0-fXKifyt3ZgRM_OWQPDJPWtzZeP4oBLpFAJ7rElKsxXROHOYtMsmwDBv_HwGBH6fi9390cDbUpqb-ZlbFflgmnX91TvyHXWY9i0AFI-SbGvt17hyPbuKnYDPbhDPGyHotwJEpWi1TRuXe_iYjNp7DCYPvw8HiXbo_DLc3jMDjivqq8Y3pDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=l-2YBOjej8LCY_OzCXhn1hsx88StJjI79g4xPXaDCYi8BnckWVoB8YUPUo4rvij8gSNyi5BgahZ3oQfB27WT9X-TIOycAv9yhBDCueeUl0R5sP81AmNpfxVEA5Elt3mXDBjuqXTcFmihH8XATWsCjp6R8ZYLPAPm6C0-fXKifyt3ZgRM_OWQPDJPWtzZeP4oBLpFAJ7rElKsxXROHOYtMsmwDBv_HwGBH6fi9390cDbUpqb-ZlbFflgmnX91TvyHXWY9i0AFI-SbGvt17hyPbuKnYDPbhDPGyHotwJEpWi1TRuXe_iYjNp7DCYPvw8HiXbo_DLc3jMDjivqq8Y3pDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=NFCpJIVF9lht4pl9SSUSOt5Wq1BMdMXqQYWSpi52iNd2UelDnhD57JF_uNgV18ozU51TZpojbYlQ33wrHY47XjAoYe2wEAx7P8_yGXJVag2TwxWM5BevNVpeLXC3UkpWBDzXMvN1NKZP4XsTFGmLuaYePzZ1z4wOaWgFm-nqe5rnRNcE0WrvnIgNratzO6beW2OovdNsXLaaQ7fjofzP2p0RBHdYdng6X7DQxWAUe97ibQGw8ldgaqCXuKB2fjeX1YwSVZ392kTHQ_ubtiq6nKh5mBC9StHDFu1JS1yUwf8gIv_7_9J26yDEgZZVhIHraLEKckrNeOrbjYSl8kMy6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=NFCpJIVF9lht4pl9SSUSOt5Wq1BMdMXqQYWSpi52iNd2UelDnhD57JF_uNgV18ozU51TZpojbYlQ33wrHY47XjAoYe2wEAx7P8_yGXJVag2TwxWM5BevNVpeLXC3UkpWBDzXMvN1NKZP4XsTFGmLuaYePzZ1z4wOaWgFm-nqe5rnRNcE0WrvnIgNratzO6beW2OovdNsXLaaQ7fjofzP2p0RBHdYdng6X7DQxWAUe97ibQGw8ldgaqCXuKB2fjeX1YwSVZ392kTHQ_ubtiq6nKh5mBC9StHDFu1JS1yUwf8gIv_7_9J26yDEgZZVhIHraLEKckrNeOrbjYSl8kMy6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=Y2iDPcoRkVPK6YC70hBsEZT9NOUoDebrwSjCbgWdXzIXY9OvmCXPvQGOSdfbfIXLpkvZ8EOFf-GQEPGC1PeZKsEyCdZye0021eKC1CnJ0YFA60jdR3y2jMh-glJ6BVoeo5r2oq3s5SV6kv4wAa_2Xa4NswsfVWeVWHzBNQUhatCuJPo5oowu0czuBg95-SoOmn6dT_cop9Z3FbiJVmAc0PbdZcPeR-e7qOXy2mWp5DXnI1NgIY7IokU6XToLeGMumtytO2ymFcnT9y9oRefkfJ7JinmVgxOVVZfcKyRcnhYgwJZfSwjm6yu2SgQrg88ogpRGZJGqJCaUF7uNqkxNhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=Y2iDPcoRkVPK6YC70hBsEZT9NOUoDebrwSjCbgWdXzIXY9OvmCXPvQGOSdfbfIXLpkvZ8EOFf-GQEPGC1PeZKsEyCdZye0021eKC1CnJ0YFA60jdR3y2jMh-glJ6BVoeo5r2oq3s5SV6kv4wAa_2Xa4NswsfVWeVWHzBNQUhatCuJPo5oowu0czuBg95-SoOmn6dT_cop9Z3FbiJVmAc0PbdZcPeR-e7qOXy2mWp5DXnI1NgIY7IokU6XToLeGMumtytO2ymFcnT9y9oRefkfJ7JinmVgxOVVZfcKyRcnhYgwJZfSwjm6yu2SgQrg88ogpRGZJGqJCaUF7uNqkxNhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=tInrOY8iwEvArxeI6-_UmDciQ3r4LNrE8H3NZR321e7NUFlFDJGvduMONqIXtTwYq4EYr1Zeq5jaoHZl29wBIyjwV0CnnYteheAgIWO1HoB5nT1anpIaFkRDLgl_MZbCui3S4Ilv0_5hwl8KhA649vOObx3_-RAL2kcDjWnD1IKFJPHGDZIb2D7G9ljFq9A2ZT4CsAQv8bmuUjNl3KH8lP7SzoDB3Pym3m05WdO7-qxSwVNEiTu_HjOcpW3aZgScgxHaUG8VCLFLAb68hKWw5t0mC7qbxf1wZk9ghs3dIyUcyl5kQWpMTojsHzyBKDhkhj2xZJlai7ZOCpuWbIJihA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=tInrOY8iwEvArxeI6-_UmDciQ3r4LNrE8H3NZR321e7NUFlFDJGvduMONqIXtTwYq4EYr1Zeq5jaoHZl29wBIyjwV0CnnYteheAgIWO1HoB5nT1anpIaFkRDLgl_MZbCui3S4Ilv0_5hwl8KhA649vOObx3_-RAL2kcDjWnD1IKFJPHGDZIb2D7G9ljFq9A2ZT4CsAQv8bmuUjNl3KH8lP7SzoDB3Pym3m05WdO7-qxSwVNEiTu_HjOcpW3aZgScgxHaUG8VCLFLAb68hKWw5t0mC7qbxf1wZk9ghs3dIyUcyl5kQWpMTojsHzyBKDhkhj2xZJlai7ZOCpuWbIJihA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Nc9gaRys2CcA3ESwouoMaNmcMjuKlkcyGLhH1CmCX1SPBdHZc1c0OjuFPtz8tRwnz3RJwUiiTfS-3nIE--3jEwL_VoHdUpBVm7f9w2OQbyjEKBKI-RZ1cKf_6PO-Tr2CS-HXkilNjNdAShlD4Exg7_Fb4JgHf1tS34b77EMMT1eunpMxCg2iLQjm9X6BPpBG2FWjXwEmUXi5EuA6zRadCmiYGZm_CEhKlZm7ARsqVBjGtVenzCdGxXKm6EoZDeq6MIA6oOvf0uQiYdeophwyUnrpZ4tQU1IeNCdBkcpB_f2vkPRWWjYHUdh7gcfdRlvOgQIFSrlANXq0YCd-IkxGLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LBkMOxRbVW2rlwStpy61yK61jbhmgIs7joARN0onZG4CXWyxEor-obBaOSQzVTWyesIANo7qhl9iRbYnp0EMiuk9s85Tt63nbxbCVdUvtbySDGKWhpibpEaNzNVJiCGH-kVum9eBWpC_wOxn-JkFC0GjBcTQoWG24g_VBLE8DPWLrjdWo622eqs3kMBcqlrr0KHiwfG3XiFa_pPWO49CchLI0IUuIFVOZx2YQksA_Lz37VycdGJUiKsWeoVUTrO6b9ALALXk9v-oinxz24rzhW-4Rl9gKv8G4j8Ci8yPTDXoNQbxHrOCV6pvdmA1MCC9wkqIZ6xUelbd_3XbNzxHrA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=DV_X4B5LmFqgvwj52uU_P_omX-ooE_mQA-U60q5P0HUVQXMA_2zxQkoIXYRe5n1cyvxDR6bUzhBWzetMR0fa39u0biKLkF8f2GyxnVnFpvNBFyvP1nD6W3N3HJOibB_20qLrYp7-6mERTQPH2zSzy-qfjCYbD5LjKQiR81u-VBxB_fpVhWHcHCljoulnsbWsPo6Q6ugourRfJYl6_IauzuwDu7E50gvTNcG8mbkOFTTG5Ui0jKTYAU-zCmXEhOC9yF9k5gncVMdwrWkm6sdTaGEdncLSD62az6t5tYTCtfS4HYLpTC_crbVYg8BlPlXirjbmo1imdMmb-8U9Hs3ce3xyUCAavZCnz8BlggkaTBaTYk5YQxbq5VJyIbxdIwIq8FycDn4y7ELGdlA39ul4sIy9cx-7vcABcnTBle117lK1418t7JrvqnSTjEIejb2X7GGe77iKDGXf2ttnI1iytzoRXZ8Qzo8T-NXuzsfnuNbVI5ns8D5NXSUCVhvXKj7xiuqmKILCQtpzVHqE6LjMRRZ9BxaC3qKMqdv0aNQSCj1Cq3cjTbTc0_E5cz4Nd7OtwgX8hpm_JlFB_-O84VV4skx6Db0aLTCLscq8wuemqL4pJwX96veWHt4gY9kaE1OhWZn95PXGBn1Q3Iy4KIfksq_LnByVLQEj4ebzqFg6fOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=DV_X4B5LmFqgvwj52uU_P_omX-ooE_mQA-U60q5P0HUVQXMA_2zxQkoIXYRe5n1cyvxDR6bUzhBWzetMR0fa39u0biKLkF8f2GyxnVnFpvNBFyvP1nD6W3N3HJOibB_20qLrYp7-6mERTQPH2zSzy-qfjCYbD5LjKQiR81u-VBxB_fpVhWHcHCljoulnsbWsPo6Q6ugourRfJYl6_IauzuwDu7E50gvTNcG8mbkOFTTG5Ui0jKTYAU-zCmXEhOC9yF9k5gncVMdwrWkm6sdTaGEdncLSD62az6t5tYTCtfS4HYLpTC_crbVYg8BlPlXirjbmo1imdMmb-8U9Hs3ce3xyUCAavZCnz8BlggkaTBaTYk5YQxbq5VJyIbxdIwIq8FycDn4y7ELGdlA39ul4sIy9cx-7vcABcnTBle117lK1418t7JrvqnSTjEIejb2X7GGe77iKDGXf2ttnI1iytzoRXZ8Qzo8T-NXuzsfnuNbVI5ns8D5NXSUCVhvXKj7xiuqmKILCQtpzVHqE6LjMRRZ9BxaC3qKMqdv0aNQSCj1Cq3cjTbTc0_E5cz4Nd7OtwgX8hpm_JlFB_-O84VV4skx6Db0aLTCLscq8wuemqL4pJwX96veWHt4gY9kaE1OhWZn95PXGBn1Q3Iy4KIfksq_LnByVLQEj4ebzqFg6fOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=bUJR3OnMmDK89MTG8T6p5i4TuMJeq_D3bbItzlv70m0hmEAZhrTK6_66sF3YtASDkcEJHvDeMIQKcGNb0sMOOn5qRVFXO68Nk61-LYwlp3_VcfiJ_S_O1vHwidvP7EkA-OV-s7QKXq8Utv_NX-sgVFoESvNkJiHEWHTIlOYo911WleGu7S68Lgc_u4mAnomKpZw6Ki6kxEMjGcMpGh2N7CugHy-AZkVDDXY2I3vofN-s1Bn6qQh4Tgff-Yd7NDNmaSq6td9L5gCGzRz0VxURxYco6OFeXXrydws0uLTTO5nvH_RcfwFcs2OKa_VP1Phpn_p8l3oFyRs8g5VvUezK-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=bUJR3OnMmDK89MTG8T6p5i4TuMJeq_D3bbItzlv70m0hmEAZhrTK6_66sF3YtASDkcEJHvDeMIQKcGNb0sMOOn5qRVFXO68Nk61-LYwlp3_VcfiJ_S_O1vHwidvP7EkA-OV-s7QKXq8Utv_NX-sgVFoESvNkJiHEWHTIlOYo911WleGu7S68Lgc_u4mAnomKpZw6Ki6kxEMjGcMpGh2N7CugHy-AZkVDDXY2I3vofN-s1Bn6qQh4Tgff-Yd7NDNmaSq6td9L5gCGzRz0VxURxYco6OFeXXrydws0uLTTO5nvH_RcfwFcs2OKa_VP1Phpn_p8l3oFyRs8g5VvUezK-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=rdGU8OLWV5WCls15Su8Il0lymJPFPwvlWzBgtOYJyZJXWiSlCnjI6v_S44A9S7ft57Xr5mXObcXHbi5852nB35VCajtFNSIxzQ1pWq88MCZ92XZLULCj6dogenChHn6lq2pzpyESEz1FUfZu9mcm09rBTuyaygA-WE182J1gM1aftJiz4IPXq_lb4PZ3GsGWTvv1QkprKiK_jowl2Rhd3jpIvV_BgD8Vhcop7MH_t_igwOYlpnuskY3WLTSCZMr0MSk7NxZQkCdwrwZJHO26rV1IxtteEaq3SQPQXeKSxShdMdlplG0SvDbLew9KQ2GWxsrJAG0EOYZNs6TMH1DGng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=rdGU8OLWV5WCls15Su8Il0lymJPFPwvlWzBgtOYJyZJXWiSlCnjI6v_S44A9S7ft57Xr5mXObcXHbi5852nB35VCajtFNSIxzQ1pWq88MCZ92XZLULCj6dogenChHn6lq2pzpyESEz1FUfZu9mcm09rBTuyaygA-WE182J1gM1aftJiz4IPXq_lb4PZ3GsGWTvv1QkprKiK_jowl2Rhd3jpIvV_BgD8Vhcop7MH_t_igwOYlpnuskY3WLTSCZMr0MSk7NxZQkCdwrwZJHO26rV1IxtteEaq3SQPQXeKSxShdMdlplG0SvDbLew9KQ2GWxsrJAG0EOYZNs6TMH1DGng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=d3VKkAvl7qcfuj32ZExGqDWR7J_efEbMggovk7AbZSLNPj9OT8PwVDRbT8uNiVxrRG1ZfG7dhBAdbqayyg-Z5VTPMYbw7Ev8xuo2PTqVEoPSlYupO9lxdqrbQYnEp1QFYO2wh1g9vkjR1ySIWHhDCc1PJapWP4FgnBDJcXR4-BhGyoJuICL0PvhFAL--0QVJZD4hzKBt84SGuP7DWole3XYuvmb_a9TcLsfyc8vzjKVFfMBpReNRoOKJ5jHDmPz9APH_5-778GdgiWDyMF12juNWfU4K1T51KSLdoDd5n2daxh_45BgpEdfJWql0wIUWgGWO7yU_nAoddnlZo76pfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=d3VKkAvl7qcfuj32ZExGqDWR7J_efEbMggovk7AbZSLNPj9OT8PwVDRbT8uNiVxrRG1ZfG7dhBAdbqayyg-Z5VTPMYbw7Ev8xuo2PTqVEoPSlYupO9lxdqrbQYnEp1QFYO2wh1g9vkjR1ySIWHhDCc1PJapWP4FgnBDJcXR4-BhGyoJuICL0PvhFAL--0QVJZD4hzKBt84SGuP7DWole3XYuvmb_a9TcLsfyc8vzjKVFfMBpReNRoOKJ5jHDmPz9APH_5-778GdgiWDyMF12juNWfU4K1T51KSLdoDd5n2daxh_45BgpEdfJWql0wIUWgGWO7yU_nAoddnlZo76pfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=oh11E1EnsLQfQazp5uDA2g-m9B2j1RzNz0QRYwvgjgQW3nf5BYdiR0e-QRL9-cCSkgbxbwq6K72I0xO8ERDT2QBu2NyJf8NL5MWJrntK6lQVSZBP54f8_fF2TOivYxIBl2GJ0i19faqqUjUhIOhg177OC5EinVvYSEUxuoG_c9bZN6MGaBBiReNjkqSOn80uR5KSS-l4qsHsRe8dRgxzarb1hT0AmbWlDJAq6bEvkPtrGSD3GlKfdpllMfk17p4FyVu14S2qI7LJ9WJpSy4BYYHQOz00Dcd_IrC6aGAREjNVqVrhj7ST6R_uLjXr6KP7WtCxrpjeTef22DzAMKZUZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=oh11E1EnsLQfQazp5uDA2g-m9B2j1RzNz0QRYwvgjgQW3nf5BYdiR0e-QRL9-cCSkgbxbwq6K72I0xO8ERDT2QBu2NyJf8NL5MWJrntK6lQVSZBP54f8_fF2TOivYxIBl2GJ0i19faqqUjUhIOhg177OC5EinVvYSEUxuoG_c9bZN6MGaBBiReNjkqSOn80uR5KSS-l4qsHsRe8dRgxzarb1hT0AmbWlDJAq6bEvkPtrGSD3GlKfdpllMfk17p4FyVu14S2qI7LJ9WJpSy4BYYHQOz00Dcd_IrC6aGAREjNVqVrhj7ST6R_uLjXr6KP7WtCxrpjeTef22DzAMKZUZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK5hdiXRwVQmofiRSlPOVA5xCRWKtBmca4iD9RNJV89ZUhch895xpGuLIEazeRdwW9bdOYPiVfG_qUt1Yd98y6XdDvGerADBfe2LvWhn4AUvhEmTUxb91sYlVGZ_zeVRVS_zxjoSBb-zwCi78lNg6T2vdymJaelHSYCx-TFstclOS9bxXWGBA_DCrx9kKMY4ajtXJY_4ZlSeFSpEUNhTDvAGBC5Br4CwrINf2kkqDy83Iu0KPPchqXqt7rxTd6hPkm7f3ua9gkcKryYy6WkYmN8Gf1TXai-O9FTRZiEjHO0obDzfUHCakuA5bW_22ePMUYjp5y5uTCcwf5PtJARQoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohtNDPEpQMZrvw7M_XSRRibDzquu7otWhdgadCkZumiG_nMMxEUGkM1UkPUyK56pc-C7R5_-h9bMOqfUdyAYfWY0scHcIJi6QMAwOJkn0mCDue8Tirs0-1mjmC8-3vsoObXNHtp_e8_P8B2iacIwj26dZH9ibGi9S90zDlW8vUzUNi_B2mk3eIlzPcygWc6rddd_tldwQcB1V15DcJL5QIzwHJBSdZX1_UChrSuSdPwWOZk4jbias1MMPKohib_VoVFuDqRuSjfF1LjGHpXFazyZ3ZsWFf68j9BxnIBNpjDtGi5HIcQXFjKq89AcdBHLeqt6LTbr5RSIfohw0Oqmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJCsypr1MZJiLvDNDw1l0EocpVRFecTk6f82ZdfJwc7_0wl7ALIFRHTzP407w3cq6SaNDBgIfXS_0tEFLW5VhNlR-KJou8accY4k2zH8uMr_jQ-ZZDEi4MDgbk95N4xFUV9Y4wV_OUGfqOCp4aHH2_mGVKAE4w_np4p7gf4NpBI3a80vVcLSnUGmKw7CxI8Nsus8pMavS5w_PZcONSEWR59kLbHKibGIL9tWBFF1NGiFOJWMGDTkPm2lx0iX5QAa03GXMAtcskChJHFXwuYOev9uXt6zr75zYfYRsRHT4KrSMKZ57rSN07ir4ccpB5K36Z3K9WbnL2kx1wqXv5Qd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOHuN_Wd3p4gM9Jcocaafst44dRbrfSSaBawHbDynNqejQ2HpckeCgNnImkWAVhqnldqmbCNffzAovKc4tMsKw4UHT4Fg_E6HBSkLt2zigGjdPinDiAMjY6TXuZEq_Dg4UU7EMGY2pqglGAB-fLJTWuwmqXg9ph-O5ijYetvHy2Z5yAjI2TDM57CsFx95eGBdKKXy93vcgPlw8bN_WZGeI_zTVzqbeg2SsaBCVxXl_nkjaYFwdoHyO7OizfecY7mGvjWFv-tbE6XEi2qzDryCSt2owf17C8-ba8NAMJm5JxxLlooe4kZIUyOmbzYWRFuvac6j0nBC6ambQXL4I_O_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erTxTAvgBcn607n6z8DimPa5TK2qwAYGLjYijmKpcl8kVmqcKpfvJ20VmxA2SBJ8-BaEdDmTdj9q-Unm012j2Dn9naPp-2fEsZZs493yMAtUaOmqTtAXoE5mZOYr5arCp4m9LiogBZxl0h-x1FmKQRQu0ONw2-dltd7nxFhGn_b8Ti6Nt0t2qxPgWG7GcgMn6KBQqCnvgomunMFdHOTO2vTh25KOUhkARuP0_fkW9WzIKmmqJOYc7fR9tGFdyFO_sdPvFwcuR99ChtanE-k7bc5eQihETqv-vhZx4EmBKhj3Tn06o1kaVVz9EbeLD1_U4TqWnGkT0LD_DVPxJVBmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj8LaM8_UvAb5FvCBub8JEJhjMriS86lonNx3SlZEGf2mSoH7eHR2566yVdMyXsH6JqEc2nYSHaM9dgPFJ1imhthKyc_gU21k55dtUSATqaEdU84hAr4eVOaTFom7F8QJI7ptUmZtbgvfz-rfnM5_Z9qqqMqLtn1byVwVcISK9HnD7WgIg1A3kZWAzDAdVY1Jr81jNysbvzfF__sj434TnE5nEsbbF-L05aHZUAGLx7oFPElqes8Y3X_if2kA5p02vPV_n-SdW4oo76EhXrx-kCC1kxBU8aUlrzIJZBhdyqfShUezzZf-Si8HzGF5VAkPO_cySAhgDiTrpsbaBXfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=SDkRaVVkcOEDhS9zUK8vsbmDrtY9cYnRwvVJlHlbn9ImoZTkRb0IR8DIFKYrpSFidSCK6FmHzukxhxpvWOXkAiTxHPrSwZcP__o3453AKXqqAuhswqtoYzGCYNPNhKff4zeKQjg05vTPglqmIbn-Hlw5mwAxcKZ5UJdNhlhoM4W7HuEHejN6sW08vusg1DQ9EtaFt1M23BkEcC4Q6PI2mjiiYMv5bV1Sj8yXdf5-tvWOBQF_pfh02IX8KsroJh42kTlFkUo6EkY14yAd4ie9VoT8ncRzEJ7S-iKl50X9XcaAkeFNb6nha26b69BqzRiRC2KcGf2veoWHKKkSV0IpQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=SDkRaVVkcOEDhS9zUK8vsbmDrtY9cYnRwvVJlHlbn9ImoZTkRb0IR8DIFKYrpSFidSCK6FmHzukxhxpvWOXkAiTxHPrSwZcP__o3453AKXqqAuhswqtoYzGCYNPNhKff4zeKQjg05vTPglqmIbn-Hlw5mwAxcKZ5UJdNhlhoM4W7HuEHejN6sW08vusg1DQ9EtaFt1M23BkEcC4Q6PI2mjiiYMv5bV1Sj8yXdf5-tvWOBQF_pfh02IX8KsroJh42kTlFkUo6EkY14yAd4ie9VoT8ncRzEJ7S-iKl50X9XcaAkeFNb6nha26b69BqzRiRC2KcGf2veoWHKKkSV0IpQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/m4Fz_PqxL06GNM8jUGVNH0lsh9qqrNDmXWOcVMScUl4g0aJsv6GN8I2-Dn_C3Mm7ZsBfHaIuU8DhGWB_nJ6HWG240GsFp29_Ho-pRfhCiWR_a0YbYRP_qAqWEg8h5Wdn0RQWxY_6ThVTFs2utXFyLDjZ45LoQYfC4wy6-p0CpSBYCjMpVeszIULYa8BmV1dGi2PitMzmkM-bNaRWYbkRF2NC-PMyCJYkcqLhKcYJ0t3agaXVyp8VtPwoL7g3AegnNu7HZOmK7rmqdrs9aZJl3TUDFfeaLzMq9jLSEkphgFUWL7duWwBZtb-yQBdibHQhPT6MhnUNS6U53u4g099AmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=REBMlvbXsxk2MvKfEjZ1tnW2pzdFF2p2jJYcHa9siRZmC63tmYJ5k6oBA_NzB0l8TlxJy0YQd9jcV3WC1Pz3Igw0cEsXVVJ28Vg1fxEpfrMCr52gnNRpryx5BwFMJNhDn2vsdK3dhdEmA37xIgOYDb7sAFOs4x7_KIqnGPCKFQF6tYff2314MGRiNCDLKz3jeq9P7WJjLSYWNMtzId2vKz4QNEbGarmOgPTGCoVUyhlrm_w_gLGEPBfhyz8mTPfCbKbnmyVcM9mQCALxCwF6nVQKwM08i-kBSenDP-KNsoA2Wj4_w9L-T22KCbok-ysFwhPw3qVuar89-6WWF63xkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=REBMlvbXsxk2MvKfEjZ1tnW2pzdFF2p2jJYcHa9siRZmC63tmYJ5k6oBA_NzB0l8TlxJy0YQd9jcV3WC1Pz3Igw0cEsXVVJ28Vg1fxEpfrMCr52gnNRpryx5BwFMJNhDn2vsdK3dhdEmA37xIgOYDb7sAFOs4x7_KIqnGPCKFQF6tYff2314MGRiNCDLKz3jeq9P7WJjLSYWNMtzId2vKz4QNEbGarmOgPTGCoVUyhlrm_w_gLGEPBfhyz8mTPfCbKbnmyVcM9mQCALxCwF6nVQKwM08i-kBSenDP-KNsoA2Wj4_w9L-T22KCbok-ysFwhPw3qVuar89-6WWF63xkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=ndPThLSZkX1TEM3aGfzY-2dZJiKfJ7yi4hikCQQeCiksNgUqPj7QYJPOpgfNaCZhFTtYWPT2Ul9XUsuHxXU7Lqv23AMAT1LBbfEw9V4X3gCmlyygwZNSsSb00fJtBwBk7VvtUvZD0QrGIdicEqfP_CehALZH5OigSucw-4PDiNMox4NurijWVS2b1blf1OMwz646_XWCqLhfLQNEx0pNmqmAJSQg_kTcN7YWQg-rsfOkA36FHjN2uFb0Vv-sKXqK0BWghuKySkPs3oZw1TdqRi4aktTcrO55eyydWgN1DlJMsuzFZGSU672xQwq4PCr_M_7F3OlQN0EEmXT98mSxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=ndPThLSZkX1TEM3aGfzY-2dZJiKfJ7yi4hikCQQeCiksNgUqPj7QYJPOpgfNaCZhFTtYWPT2Ul9XUsuHxXU7Lqv23AMAT1LBbfEw9V4X3gCmlyygwZNSsSb00fJtBwBk7VvtUvZD0QrGIdicEqfP_CehALZH5OigSucw-4PDiNMox4NurijWVS2b1blf1OMwz646_XWCqLhfLQNEx0pNmqmAJSQg_kTcN7YWQg-rsfOkA36FHjN2uFb0Vv-sKXqK0BWghuKySkPs3oZw1TdqRi4aktTcrO55eyydWgN1DlJMsuzFZGSU672xQwq4PCr_M_7F3OlQN0EEmXT98mSxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=JtUqglV3ESwEy92RwYvGVksWqp0KQ4VujRz5jfH0PPr0b13Muum2rCep7VZeWWaiZamvVlBokaups12Z9XAoV5rZmtq01DKjPPsPrp00BE69Tfk33nndkk6A68d0w-fD-heKQyQpFxuPc7D0Xb5gnpaHKauhqwlPeYZ28nwkc-GHr7M-1givrBeUhOhnRpxdS-T0Q6B4PeT2yxfJZj2p4-7dQCv8tkX_cCDeGcLxqdp9pxOwC-PJTkcI9FC7PZ51JoVoeqqq6ohs0Iod7BbgIWiVWPxoRjgR8hYI5ZP8pWc0_gKIW_hYkbYkMvkpKPGPQnWOwk-9S4lUcMnW4J_b3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=JtUqglV3ESwEy92RwYvGVksWqp0KQ4VujRz5jfH0PPr0b13Muum2rCep7VZeWWaiZamvVlBokaups12Z9XAoV5rZmtq01DKjPPsPrp00BE69Tfk33nndkk6A68d0w-fD-heKQyQpFxuPc7D0Xb5gnpaHKauhqwlPeYZ28nwkc-GHr7M-1givrBeUhOhnRpxdS-T0Q6B4PeT2yxfJZj2p4-7dQCv8tkX_cCDeGcLxqdp9pxOwC-PJTkcI9FC7PZ51JoVoeqqq6ohs0Iod7BbgIWiVWPxoRjgR8hYI5ZP8pWc0_gKIW_hYkbYkMvkpKPGPQnWOwk-9S4lUcMnW4J_b3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJY-SnWGx42L2FROn9FgrI4xzKJtZ8FbApnqUN41aBu-3JmYc0GYsfISiLIbu6ZYJchJyzvU8NaiWJQcSjB3-2kCBcLySZGha10jmFgW7zA6A9zJoMkIcbUnQWYrrPqqzju6KYgJvl0KQMnfKNn0F41cghR3cIXh4LQpQrSE6sanDHwLOKwV3D96mKNYA8vqf5EWKnqkORFAF_LEKflQS1C1VCdA_rg0E6DRVIKT2PSO7ImdI166odmAjm_TsAEFnswiH_18CyevS9xBNJmZ78HiFzG0xLHOCzcCG0Lse3a5wmFTj4QDaZGZZXq5wEail_dBvFj-vEkzvHRzuWcABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=OXnQgPikl_7My7m7r3WVpjalqXfeOHxZgrLVQkbJRDwfkGtNKN0GBoN5zzU-dX-4EEnhlrE3zcnsL-QQRyBEsaKNVucOvrPimH3ZEza2TiLq9N9O4XSOvil63YWic0pdn7fGq5x1lKMa5LUbQMnvDrT3CJUzY3yGB_lR-G-lDyXdlzgUGEeIKE31Dd3khpuZij5txWSQsaSQQUgusgShrgUrV6MPxbIGlqwJygEI_4hel1X9bM78od051FrK3MSKMofWBR_MPFtsvD5RQCg1i21KfL1RFy2Q0U1vgEav0_bWPih1ccyHDUvW2J0IZiFwdEoWWbc1jCBijgzlAaEStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=OXnQgPikl_7My7m7r3WVpjalqXfeOHxZgrLVQkbJRDwfkGtNKN0GBoN5zzU-dX-4EEnhlrE3zcnsL-QQRyBEsaKNVucOvrPimH3ZEza2TiLq9N9O4XSOvil63YWic0pdn7fGq5x1lKMa5LUbQMnvDrT3CJUzY3yGB_lR-G-lDyXdlzgUGEeIKE31Dd3khpuZij5txWSQsaSQQUgusgShrgUrV6MPxbIGlqwJygEI_4hel1X9bM78od051FrK3MSKMofWBR_MPFtsvD5RQCg1i21KfL1RFy2Q0U1vgEav0_bWPih1ccyHDUvW2J0IZiFwdEoWWbc1jCBijgzlAaEStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=CagOaKisNM6E_mAGRHKhxxSUnLhPMO4HLMpo9bSMZVxN3rC7jmV4fef5l7XyFp3S9kYEGr8ygXgsRHm07Xh0BnEoDL7OU26EGvwHrKkylBEPkwABffKLlq8ejLgoks2B0qjA4VkCud2eV4nqhScq16kbtjz3cglzkk8AYlCCosGQ-yEqJCzP2Eo8EoCsOLt6DV9HnHiPbHZY60WR3ruXLrC6uqYji4iQi5FL0WFzp9k_ynElOOMiEvFWXh47VjxOPvXB8np6tT7YyKjUP7_UvwentXQJwLJijPTmnCVyt_uYodRwsy5uxR-UaUXCam1r9NnySr5gvpRzw2Pg540bzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=CagOaKisNM6E_mAGRHKhxxSUnLhPMO4HLMpo9bSMZVxN3rC7jmV4fef5l7XyFp3S9kYEGr8ygXgsRHm07Xh0BnEoDL7OU26EGvwHrKkylBEPkwABffKLlq8ejLgoks2B0qjA4VkCud2eV4nqhScq16kbtjz3cglzkk8AYlCCosGQ-yEqJCzP2Eo8EoCsOLt6DV9HnHiPbHZY60WR3ruXLrC6uqYji4iQi5FL0WFzp9k_ynElOOMiEvFWXh47VjxOPvXB8np6tT7YyKjUP7_UvwentXQJwLJijPTmnCVyt_uYodRwsy5uxR-UaUXCam1r9NnySr5gvpRzw2Pg540bzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
