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
<img src="https://cdn4.telesco.pe/file/oQEi69z3ULo_fds4nRrRbpvuByIXQ9rDRbpu3m2Oe4BKb5g_7rPCjDN6aaql_y2uuOcF_8dJvI-HxezUzicOda-sPsU-C8Il3XbwWDyQ5GszK99uWSSYg_TKr_N5exytDJ85NwISRTNqAqcRIz2CWRcR_GFNSDAfmezR3JP3CHVWUHRtXWyUl5z3uKxFSQ4-LuDcHk0ZG-MfmV5ghglWRyxbFCXgrBrIIiWUCKMZcUkniYYn8-_JyM7qncouf-qj9WVfdi0vhA3blkGu16wgpfXleqi9gNUIm4gycOGL3HCX2N6FtplN0aEtu6HTPxRRDwLOpKWDJy_tip8tycqoaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 209K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 14:00:23</div>
<hr>

<div class="tg-post" id="msg-67274">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBQAoWe53VRAs_nSCpUpveb7Z4tZegMKXHRKAJZ9An1ycGqgpfFS3W3xWFoRibr9cRPHHJ3r7jDmTojekZqpBJompfBka0F5BQXOnXgGIJMjw-QKKQVdeKo1AK1vuqm0d3rfzBaiVEYm66Tc0WiGe9gIymF01ST4hRVnozErrdRwiNlWZU5o0kWSM2CC7aQ7RsQZHnS7ghB3ex0v_k8B6BDJj0XQs5NOge-dYCdZ-in1hlRmNzQIVtFNmyZHfejaHgLttQLbwY2P6h1W4_J0uW_dtfWQib7l-YJmlV1VMGMH3fe4dGB3TaudrywSyMULCLfWojOSjX9D5-GOTEvQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برافراشتن پرچم «ترامپ را بکشید» در مراسم وداع با جسد علی خامنه‌ای:
@News_Hut</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/news_hut/67274" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67273">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=cNzTaMO0Tu0tJQ7HfzpZG31OqzEEKXpIho1Qa6SyG5nuXPJ7aInzwuAhh3Tjf6ThItStYx1liPdzqlRydx0sAN3N-bY2_3BLrVFZvRpcCUvsVipopjZ-WmW_bYwBdDCioel88KIvDPoZv-VxpV-mPGR7PdM14MOJz7ibjuB0MQeoDf7iRd6wSH8MhyiHNnacgoYvo4GyD9SSPUDsPigH4weranspoMR_w6Wy7FF_wI33Z691hIQZ6SKbMutse6r1AwxVDBmxosy770g88iGwXay3acOz_dH16o-l_LGYfQQdxROPv_X6s-TA6mwPFuUBZwnphQjzQo0NCZEN0Y37GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2883f7592b.mp4?token=cNzTaMO0Tu0tJQ7HfzpZG31OqzEEKXpIho1Qa6SyG5nuXPJ7aInzwuAhh3Tjf6ThItStYx1liPdzqlRydx0sAN3N-bY2_3BLrVFZvRpcCUvsVipopjZ-WmW_bYwBdDCioel88KIvDPoZv-VxpV-mPGR7PdM14MOJz7ibjuB0MQeoDf7iRd6wSH8MhyiHNnacgoYvo4GyD9SSPUDsPigH4weranspoMR_w6Wy7FF_wI33Z691hIQZ6SKbMutse6r1AwxVDBmxosy770g88iGwXay3acOz_dH16o-l_LGYfQQdxROPv_X6s-TA6mwPFuUBZwnphQjzQo0NCZEN0Y37GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش نکیر و منکر بعد از ۱۲۰ روز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/news_hut/67273" target="_blank">📅 13:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67272">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN1iX3Dj1ejxYuAiEbe7JJwfvrugjvL6IbsGjau7PNlnxoLO1TJiW5jzNcJGZOwbg4dVkb_RMiNf2w_hfWEa6BnVw6HJy8t878wC3-wTwaYtokbYDpS2wEhoxQFram6c4Dp-Y9RXXrev5IUDmVN2GOzKLFGMO9RMppcLQCHgDdkTnMRK3wjzcIYbm6srCQg_4_IbpSSimFo_sghDfmY652B-YhrF84QXy8ElaWmki0O2xTqXYHpXYrvJTo9Wfnv6PGl8zLOdQ2NBcEYYqj6VAG6sczHIaoDPfO_eJGAp-PTWOMD8CWoCJJfCvhJYjawDFujik7kqLd4QvwqmAfzckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
التماس رسانه حکومتی در ایتا برای حضور در مراسم ؛ جمعیت کم است...
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/67272" target="_blank">📅 12:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67271">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=LOs0diW-0H25y81hP3OSLAVqWAsLZ6HW7rGvtHmgwJoL-sCPzp6KkJZ7g4e0nfiYEbJUetmkGgjKn6fKx9x9hgosvyIerYQ9vnefqflPppKc0wKz1cfltL4UWHbT6TYLat74B1a1KzHx-__55y0vU_SBfzVqfNq5-0UpbeoE483_XhBfKdmMqDuNb2tWwcLQHsUdDkVNWN3NVqMwctzCmdurxATfRz6Pb4CHICgcid_fu0ZVpYOHbkHw7hnj8CKb-rMc14f4lIyrkZmWz4QXEvLfAeyp0lVpRG6DeF2r-H41a1IlWI98-Cc3F9XkBg7PL13z_8lna5kfeB5HOlx0Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc8da4a29b.mp4?token=LOs0diW-0H25y81hP3OSLAVqWAsLZ6HW7rGvtHmgwJoL-sCPzp6KkJZ7g4e0nfiYEbJUetmkGgjKn6fKx9x9hgosvyIerYQ9vnefqflPppKc0wKz1cfltL4UWHbT6TYLat74B1a1KzHx-__55y0vU_SBfzVqfNq5-0UpbeoE483_XhBfKdmMqDuNb2tWwcLQHsUdDkVNWN3NVqMwctzCmdurxATfRz6Pb4CHICgcid_fu0ZVpYOHbkHw7hnj8CKb-rMc14f4lIyrkZmWz4QXEvLfAeyp0lVpRG6DeF2r-H41a1IlWI98-Cc3F9XkBg7PL13z_8lna5kfeB5HOlx0Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
ویدیو ای
از بمباران بیت رهبری9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67271" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67270">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=ILCZeFxAI4s_F2-rS32UHeR1rgN43SDGMIHwQW3mHFLoeA9KETtDMl8nei-mi7IlqACZm3FFV8QYrq7AIOW61tHy0XI_oNfzk-hm9TNU1r4si-r4N9NFOoGtoCkNLRPXjKXjmzAqdGEoGEfBYFEz-OFvEuF9biw1wsUq9tYPtDC1yhD5lKCU049Zrx7lkOTcrr86Jlo5RlaB0516MXLMNvNkAB28bh1T1DD0pBLemHft8-SboNQOWiWR5ScCB4TVd8Eiy1wu7WrmahNmUBJ03o42YHlcm2WA5t-i88rQzZoi_lG1fsIQMkQL-iguwKMADBv6ixxaesiYa896BGcWFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccea9f87ad.mp4?token=ILCZeFxAI4s_F2-rS32UHeR1rgN43SDGMIHwQW3mHFLoeA9KETtDMl8nei-mi7IlqACZm3FFV8QYrq7AIOW61tHy0XI_oNfzk-hm9TNU1r4si-r4N9NFOoGtoCkNLRPXjKXjmzAqdGEoGEfBYFEz-OFvEuF9biw1wsUq9tYPtDC1yhD5lKCU049Zrx7lkOTcrr86Jlo5RlaB0516MXLMNvNkAB28bh1T1DD0pBLemHft8-SboNQOWiWR5ScCB4TVd8Eiy1wu7WrmahNmUBJ03o42YHlcm2WA5t-i88rQzZoi_lG1fsIQMkQL-iguwKMADBv6ixxaesiYa896BGcWFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار مرگ بر آمریکا در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67270" target="_blank">📅 11:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67268">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=cqcuHo-bCFQm5DV_oAW7uZI--MpP5ujfmBx5P-Pmc11b8As5drQjngRYyyD-tEOhrXePLowJn4tT5UypUzAbYWb1KjH_BAVYrSkm-6fGxHd_XlNm2j1h4M5rDOJaxR9cZQcKrzcoINc1zC-xy9kvkSxZjznxNzEoOlTqeDQ9DbrtKsOAozRSHDA4Y3bE1kpMI_m4NsmSYtSKDPjoxuZtgc8cndpFXoYdz0dJj70DlHJyYmN70u4aqWsB5sz0ADUqEr5Tc9Wbx1stW4z9l6GrrOUZo125LROZrqgxOYnj_09uAj_X-0B1RGpCq1ry2Rmgd2qQosOGlG1aeQtIanrY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d436c597.mp4?token=cqcuHo-bCFQm5DV_oAW7uZI--MpP5ujfmBx5P-Pmc11b8As5drQjngRYyyD-tEOhrXePLowJn4tT5UypUzAbYWb1KjH_BAVYrSkm-6fGxHd_XlNm2j1h4M5rDOJaxR9cZQcKrzcoINc1zC-xy9kvkSxZjznxNzEoOlTqeDQ9DbrtKsOAozRSHDA4Y3bE1kpMI_m4NsmSYtSKDPjoxuZtgc8cndpFXoYdz0dJj70DlHJyYmN70u4aqWsB5sz0ADUqEr5Tc9Wbx1stW4z9l6GrrOUZo125LROZrqgxOYnj_09uAj_X-0B1RGpCq1ry2Rmgd2qQosOGlG1aeQtIanrY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از پرواز جنگنده‌های اسرائیلی بر فراز بیروت در مراسم تشییع جنازه حسن نصرالله دبیر کل حزب‌الله لبنان بین سالهای1992تا2024!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67268" target="_blank">📅 11:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67267">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=prSH689w1qAoPCbcQ7rKAFcWlq6UYBjUIJPdW5xGB_3opKQb5ud2IE_S6ciOQw5VwWAj4NnyEzYXAkoU9tc1C_qZfHxeIfOxnmYQGNUHKM_vZNjWAfvocPXBPcGZrm6U6eFQy1ykTnKMafV9FrifGzY-d5k-VBuD7eA9P0C8MVXcuHHExwR9-LKQ5hW7J2wKTOOaK9b0O4GhQgJYN41Mysp-BmSzkx0XKt4A1InWfVBnXztg5vMwFHI0siaOZQwROrCOzIzc0tJ7IG9h-FYHFFVng9703kiyKSIS7gIi1H1VpZ1ljqxYexC4YZMtqlji27YL9_IK0cTp3c_0xtnXcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64adeed1d2.mp4?token=prSH689w1qAoPCbcQ7rKAFcWlq6UYBjUIJPdW5xGB_3opKQb5ud2IE_S6ciOQw5VwWAj4NnyEzYXAkoU9tc1C_qZfHxeIfOxnmYQGNUHKM_vZNjWAfvocPXBPcGZrm6U6eFQy1ykTnKMafV9FrifGzY-d5k-VBuD7eA9P0C8MVXcuHHExwR9-LKQ5hW7J2wKTOOaK9b0O4GhQgJYN41Mysp-BmSzkx0XKt4A1InWfVBnXztg5vMwFHI0siaOZQwROrCOzIzc0tJ7IG9h-FYHFFVng9703kiyKSIS7gIi1H1VpZ1ljqxYexC4YZMtqlji27YL9_IK0cTp3c_0xtnXcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مایک والتز نماینده ایالات متحده خطاب به نماینده جمهوری اسلامی در شورای امنیت سازمان ملل :
🔴
اینجا تهران نیست که بخواهید همه را خفه کنید ، اینجا آمریکا است ، اینجا سازمان ملل است. این اسناد حملات شما به مناطق مسکونی بحرین است که دروغ نمی‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67267" target="_blank">📅 10:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67266">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=JSZII4__NY8RAFKgS-AB_KDMpyQt9sGPV0WiBxGwqM3kHd0qyOsLQOWyUn8oUsk8bY75JyYaT9e-y-ttpKxWiIGvHndeUFFXd1D-sutrmp4edNr3Ai26KCEl4Cf11qL1ptcxjuVVSHcZ6-E-0QrA_V4dZGU5_niihcaWMGEzpg7pVfvbgA0pgB5J1AWWcEYE9LuNE8k4Ns9P7aDMtaCHyhLnHNpUf34KYPCLSJ-uy9Hc98hEbH3bJtwDePMc12NDZlcgIsnFTWn0N86IDXSbiJmgdXMk4chFl2skvVHF3O-f7nECx4rXU1--un6ckAdRr3khppI9Hoj-144nauk_MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b206a5500f.mp4?token=JSZII4__NY8RAFKgS-AB_KDMpyQt9sGPV0WiBxGwqM3kHd0qyOsLQOWyUn8oUsk8bY75JyYaT9e-y-ttpKxWiIGvHndeUFFXd1D-sutrmp4edNr3Ai26KCEl4Cf11qL1ptcxjuVVSHcZ6-E-0QrA_V4dZGU5_niihcaWMGEzpg7pVfvbgA0pgB5J1AWWcEYE9LuNE8k4Ns9P7aDMtaCHyhLnHNpUf34KYPCLSJ-uy9Hc98hEbH3bJtwDePMc12NDZlcgIsnFTWn0N86IDXSbiJmgdXMk4chFl2skvVHF3O-f7nECx4rXU1--un6ckAdRr3khppI9Hoj-144nauk_MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
وقتی تو ایران میخوای پیشرفت کنی
واکنش آخوندا:
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67266" target="_blank">📅 10:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67265">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=WjjzbwHbiwacnGkyDuxvm_H6ZvOYSHSoiu_fUEW5M58xmym_WLkzTgYOqsEK8pplJl9DV-z_V4YqrnI7HPdvuzFLzUps7G0zpPjSOVdD3WnC9-KnuARY2TTVSXBxYxYWcQnNx6MqLa_xJPB9MuNyaKzpw-aKkklx0X1R73sQuZmcOWSq78_uxdkXHxpmrMxESToBucJHfrwklP7rrJTABgdXWgRfcHjYsfoos6YB_MBQmeSJ1P5Etdz_tp2No140v30CmGUsgxJ498b8rxN4sM1sOuFnubSdF-YbYqFnv6qTF_u15jhuNPeO3Dogd_M29FOyRcPtOSPAFd0GYghlHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b88ddeb40.mp4?token=WjjzbwHbiwacnGkyDuxvm_H6ZvOYSHSoiu_fUEW5M58xmym_WLkzTgYOqsEK8pplJl9DV-z_V4YqrnI7HPdvuzFLzUps7G0zpPjSOVdD3WnC9-KnuARY2TTVSXBxYxYWcQnNx6MqLa_xJPB9MuNyaKzpw-aKkklx0X1R73sQuZmcOWSq78_uxdkXHxpmrMxESToBucJHfrwklP7rrJTABgdXWgRfcHjYsfoos6YB_MBQmeSJ1P5Etdz_tp2No140v30CmGUsgxJ498b8rxN4sM1sOuFnubSdF-YbYqFnv6qTF_u15jhuNPeO3Dogd_M29FOyRcPtOSPAFd0GYghlHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ما ایران را حسابی درهم کوبیدیم. آن‌ها برای توافق لحظه‌شماری می‌کنند؛ به‌شدت خواهان توافق هستند. ما به خاطر یک مراسم خاکسپاری، یک هفته به آن‌ها مهلت دادیم، چون آدم‌های خوبی هستیم. واقعیت همین است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67265" target="_blank">📅 09:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67264">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=oPKeDi6eYW5Rzc5T6KWMs0lX3ZxuX3xDkHwdwNiCIXJ02Zor35BG9EtJp8EBHMjfktlTMH4NsVcZ0_MQ8ja5V-6fO2M0-qmPP-6m1RgvQwOMvKpoCtTvc0u3Lv8Pc8yVxS_UmN-XxCpwUnmuPgAOHKEgWfpdyBvhFoyXCC7nK2pfH8didl2eoj_Q0lDQ0YCp2_FRuIJOSLI_g616SCAGWzlEFlLvuPpNJGiLZCeeyPo12sRzFcVuGHB-Gi3rTSGfw5RSJAIQM6lbY8_dbdA6jnHHjMrojP0n2SiGgF4m_uvdeqsjtXMeLqF1LwCNjA3IqpqMwLPaZ4jvt1j5hfhj1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8124f389.mp4?token=oPKeDi6eYW5Rzc5T6KWMs0lX3ZxuX3xDkHwdwNiCIXJ02Zor35BG9EtJp8EBHMjfktlTMH4NsVcZ0_MQ8ja5V-6fO2M0-qmPP-6m1RgvQwOMvKpoCtTvc0u3Lv8Pc8yVxS_UmN-XxCpwUnmuPgAOHKEgWfpdyBvhFoyXCC7nK2pfH8didl2eoj_Q0lDQ0YCp2_FRuIJOSLI_g616SCAGWzlEFlLvuPpNJGiLZCeeyPo12sRzFcVuGHB-Gi3rTSGfw5RSJAIQM6lbY8_dbdA6jnHHjMrojP0n2SiGgF4m_uvdeqsjtXMeLqF1LwCNjA3IqpqMwLPaZ4jvt1j5hfhj1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان:
آمریکا یکی از داکترین هاش برای به زانو درآوردن کشور مقابل اینه که هزینه ملیشون رو بالا میبره مانند شوروی که همینجور کمرش رو شکوند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67264" target="_blank">📅 09:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67263">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⏸
مستند کامل و 46دقیقه ای شبکه 14 اسرائیل به نام از «چشمان جاسوسی در تهران»:
این مستند جنجالی دیشب از شبکه 14 اسرائیل پخش شد.این نسخه زیر نویس فارسی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67263" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67262">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/W6fZjvEJcMp9D7TXH-tqS5phNCktm5a13S5gpF4f0i2gb9Hm6kd1SGeBU5zxHq5R5HVjK_n9Bp-H1KLmrN6hg5S1GmVDcSH48p-sZO38s0I64tzE7gvbhR321pR7_tYYWVj2m2IulNTJpxZAexVl-PpiMQwZh1KiPHVwhvozy57_Fc416SPstg9KCzecxh67TiVIHVcuhuTDCvev0Zb6r2xryYZCpXXudSiPmosXfT1hEderm8RsFCzcZlVxg4lrHSi2hfZ9KgNs4L0sTh3Ei9RDaN-AfQ3YZ3pUe5zwvC4aQSfuGT3XjcVUx5-yn85WdUidK8Mb6PpcseDtPydyYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67262" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67261">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet @Vision_Bet @Vision_Bet @Vision_Bet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67261" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67260">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/koWgyGceZ52C6NM7MhhG5QXd1u1I0fORsv2ArZPGMpsU_uS_7mHDF_qmpG6G36NQ3N_E7wKAiPlExhIsbJL6W4NJXrOVCouy4PpuR0_4bgmFtGLIzMUMhFQQtqRtEcvU27Fzp9cbdZIAhqovJCg91XsRdTLhhTo88U_S9GtdtpneKwK7LK1ACxK8F9cIoFFU6FuKoqqZ2L2_4Ww3tlNffeotey4hIh43mZOFvS5eKXZmVtjI9X6x6yG7fkJOqsBiMvnwAyz0AD_NeUPW0CdV9dU6B1zVa2G4pA5DnYw98f6IM_XA9HBchH476u04WiM639W_7zL9nvdUW3StNufWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67260" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67259">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
سخنگوی ارتش اسرائیل:
اسرائیل آماده است به صورت مستقل با جمهوری اسلامی وارد نبرد تمام عیار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67259" target="_blank">📅 00:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67258">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=QM-mNUjBZX337UkozIQLyBalZy2XSxDyqORPCzCyByVCYWoxv1yinY_F2_ovNPf7Rt88YE3k24uRR9NcSY3n-0qorR5o4yxVh1zl_SzRBY1bZYGPTqt0p5AZ2s1dFmXx0gDs6wyZk3zfw_FrIf7GDud6J65h7CCy0LeCNsADwoX_LM35sLflJUAs80A-FSnEzR4DzWeJt1r2vnB2ojdGhlXww99F5YpjqeGM_FJkCEE0sZ1MafdqvzUSr8tuZjbR65zdCrCXAjYglBA4NL2WWrp0CfR8ifY47n_cb58W3A9x1XPawgyK_iNi18OyN3qsZjLEkAhZ3XeImvG_VdlHdkw4tUz9odLpLEHDgGxeNyNWFz3vN9HlWyzBGzIiY3O7st8Dk4MBpTY7CisHE6TpcgAfTYPFBH7mK6QDKu8dsYC2MA1yfdu6Xd7N8TcAImq6zxZAhnQbJ0rQwCabH5XTQLfJ3IuKMOPgB0ixh7hOpICfxIeLmtaad1gjns0cijiB4DNgF8-_yd2224uQdVXvcfPhgy81ne9OJc_9LP6hNKHwewhquWs7DI-grZz-vs7u3_9WqVw8k9Y8DeSXxELouzef5xYb0CJMt2vSeFfW3jKSHOZsI6iJVnmmXb1MJ0W3qZ0hdUd-mMs6PqQOmNpuOP8c8cUlkedKfqAQFeVsfqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b72ac39d.mp4?token=QM-mNUjBZX337UkozIQLyBalZy2XSxDyqORPCzCyByVCYWoxv1yinY_F2_ovNPf7Rt88YE3k24uRR9NcSY3n-0qorR5o4yxVh1zl_SzRBY1bZYGPTqt0p5AZ2s1dFmXx0gDs6wyZk3zfw_FrIf7GDud6J65h7CCy0LeCNsADwoX_LM35sLflJUAs80A-FSnEzR4DzWeJt1r2vnB2ojdGhlXww99F5YpjqeGM_FJkCEE0sZ1MafdqvzUSr8tuZjbR65zdCrCXAjYglBA4NL2WWrp0CfR8ifY47n_cb58W3A9x1XPawgyK_iNi18OyN3qsZjLEkAhZ3XeImvG_VdlHdkw4tUz9odLpLEHDgGxeNyNWFz3vN9HlWyzBGzIiY3O7st8Dk4MBpTY7CisHE6TpcgAfTYPFBH7mK6QDKu8dsYC2MA1yfdu6Xd7N8TcAImq6zxZAhnQbJ0rQwCabH5XTQLfJ3IuKMOPgB0ixh7hOpICfxIeLmtaad1gjns0cijiB4DNgF8-_yd2224uQdVXvcfPhgy81ne9OJc_9LP6hNKHwewhquWs7DI-grZz-vs7u3_9WqVw8k9Y8DeSXxELouzef5xYb0CJMt2vSeFfW3jKSHOZsI6iJVnmmXb1MJ0W3qZ0hdUd-mMs6PqQOmNpuOP8c8cUlkedKfqAQFeVsfqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هواپیماهای اف-۵ و بمب‌افکن‌های بی-۲ بر فراز نمایشگاه بزرگ ایالتی آمریکا در حال پرواز هستند و جمعیت از پایین نظاره‌گر آنها هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67258" target="_blank">📅 00:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67257">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=XK5DaQ0aDwJIHO7WOy6ntksN-kSNknvXCD3Tzw1sYdStSFMsynaOx2o_xhUJGNt5Tu-Kf0p_eAmlTgVY2e3JquNvsfFzk3r_kgT5QJtLxKvnw4QLxrfmxnsef9aOzTyWU06V5L-mXdrqRg00R5v3C-9PmIYM8iiW4iLjfpJCZkmRju1SEYStBkf5GxSkPJciMzZjcC17t6eyLVK7GrUhFOQ_2HtFG4kwYtjBoqB2uy9dwuTRr-NJGTMtS4FxKpF4wnajC90iyXmcwHKl3iFtFSFO9CyHXDIF_SswdtOPpM4JwohoHVjWkTowfT1u1jTl1YAsqzlW4kSh312XHFIMtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd926d6f8c.mp4?token=XK5DaQ0aDwJIHO7WOy6ntksN-kSNknvXCD3Tzw1sYdStSFMsynaOx2o_xhUJGNt5Tu-Kf0p_eAmlTgVY2e3JquNvsfFzk3r_kgT5QJtLxKvnw4QLxrfmxnsef9aOzTyWU06V5L-mXdrqRg00R5v3C-9PmIYM8iiW4iLjfpJCZkmRju1SEYStBkf5GxSkPJciMzZjcC17t6eyLVK7GrUhFOQ_2HtFG4kwYtjBoqB2uy9dwuTRr-NJGTMtS4FxKpF4wnajC90iyXmcwHKl3iFtFSFO9CyHXDIF_SswdtOPpM4JwohoHVjWkTowfT1u1jTl1YAsqzlW4kSh312XHFIMtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با هر ثانیه این ویدیو سوپرایز میشید
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67257" target="_blank">📅 23:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67256">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=oMVEJEW1CItvAJX1FfZfwP2q40yLZCfk1HRlq9Yv9mE3_Ddbjxt2I5SQn_iAkzCDKGQGTOYWLOQYntBOH5--t22Pz3U1lJRT91scnI-neY-81YfRtsEuSoj7NJIv0H3t49ig2PK-8KFlMDLymvMYCkGZbjbYocAwEEigSzdkoqwzuwEX0lsJrF5TCqO7CycjaNQ9PlBWvvYXfd_VYJvPHQwu6jpwcTmMncIVJ--JAt5blY-92w6B93mSyFoG0kkx_jMI_yjRPRJXKCgyZkC0cMA7rG8AK1HPEOkb79ROaaVKjTNd5uek-_4HDU1hck7KpcENTv9vrIWk-xMRm5WZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e000f4f43c.mp4?token=oMVEJEW1CItvAJX1FfZfwP2q40yLZCfk1HRlq9Yv9mE3_Ddbjxt2I5SQn_iAkzCDKGQGTOYWLOQYntBOH5--t22Pz3U1lJRT91scnI-neY-81YfRtsEuSoj7NJIv0H3t49ig2PK-8KFlMDLymvMYCkGZbjbYocAwEEigSzdkoqwzuwEX0lsJrF5TCqO7CycjaNQ9PlBWvvYXfd_VYJvPHQwu6jpwcTmMncIVJ--JAt5blY-92w6B93mSyFoG0kkx_jMI_yjRPRJXKCgyZkC0cMA7rG8AK1HPEOkb79ROaaVKjTNd5uek-_4HDU1hck7KpcENTv9vrIWk-xMRm5WZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عزاداری مجری آیت‌الله بی‌بی‌سی از سران حاضر تو مراسم تشییع خامنه‌ای بهتر بود
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67256" target="_blank">📅 23:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67255">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=jlix6Nrb35jPb9gOdWZPIUG-1CN7_YS_IJOiH2nhX_vjKskT66ozPwWzw_tL3cCoExbi4mmBNatZWfySu_-97bULRNP6kJ_pVCxVGxveNT4GO6dza5v7nie1xI_B7JFQBYRAR_OZNipXjWUO1DMMy-abWJDKUxzcHZKIdWZ2JL392pT5bgJUWuEiwjVsVfN3kZBUkO8lQ7cLnC2zNd7fYWFVgJU7XhT3Gmyuuw1XSdbebUb5gDhSnjtrrFsk6RoSb-tC6U_DarBfeh4OhVvgJIKaQ89cRnPEhPTH5vj177cuwalhII2-DyY_2etJwAQR5xFfUekEZciJGFDdRb5AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1191e0b9a.mp4?token=jlix6Nrb35jPb9gOdWZPIUG-1CN7_YS_IJOiH2nhX_vjKskT66ozPwWzw_tL3cCoExbi4mmBNatZWfySu_-97bULRNP6kJ_pVCxVGxveNT4GO6dza5v7nie1xI_B7JFQBYRAR_OZNipXjWUO1DMMy-abWJDKUxzcHZKIdWZ2JL392pT5bgJUWuEiwjVsVfN3kZBUkO8lQ7cLnC2zNd7fYWFVgJU7XhT3Gmyuuw1XSdbebUb5gDhSnjtrrFsk6RoSb-tC6U_DarBfeh4OhVvgJIKaQ89cRnPEhPTH5vj177cuwalhII2-DyY_2etJwAQR5xFfUekEZciJGFDdRb5AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر شلیک موشک‌های بالستیک آمریکا از کویت به سوی مواضع رژیم جمهوری
اسلامی
منتشر شد
ویدئوهای منتشرشده نشان می‌دهد نیروهای آمریکایی مستقر در کویت، موشک‌های دقیق ATACMS و PrSM را از سامانه‌های پرتابگر M142 HIMARS به سمت اهدافی در خاک تحت کنترل رژیم جمهوری اسلامی شلیک می‌کنند
.
بر اساس توضیحات منتشرشده، این تصاویر مربوط به ۲۸ فوریه ۲۰۲۶ است و بخشی از عملیات نظامی آمریکا علیه زیرساخت‌ها و مواضع رژیم جمهوری اسلامی را به نمایش می‌گذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67255" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67254">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3720a35424.mp4?token=evHV3ucnTx0LTRXG5JpWWkADx4mkXXtzqUpVmezeNF8il08gng11Qd2MNVs0_W2b16L8LBcdi8cGwUAIzAYvldXDp-RAjhjJbja5jEGzvrKEoRzhhwdVloVrE3BFK877EhtWTCcwoNs9XAt0HL_qgKJ_i_s3gIbQ_YzK_prWXr1agog0my42yj_NInBkRw7jap-_IBs6RaNKvGnWONxmNUW9eUerwZG95TY8XKkv1C0Q1J5HF6JRitK7IPG8LDW_cPIcKarVrLydScqFbocwzZ4tvzAeYGXV2ARiUusbMQ4U2xgaH4jgxdz2tfAdv1_15NIBxDX3j6j5oDTkXTV1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3720a35424.mp4?token=evHV3ucnTx0LTRXG5JpWWkADx4mkXXtzqUpVmezeNF8il08gng11Qd2MNVs0_W2b16L8LBcdi8cGwUAIzAYvldXDp-RAjhjJbja5jEGzvrKEoRzhhwdVloVrE3BFK877EhtWTCcwoNs9XAt0HL_qgKJ_i_s3gIbQ_YzK_prWXr1agog0my42yj_NInBkRw7jap-_IBs6RaNKvGnWONxmNUW9eUerwZG95TY8XKkv1C0Q1J5HF6JRitK7IPG8LDW_cPIcKarVrLydScqFbocwzZ4tvzAeYGXV2ARiUusbMQ4U2xgaH4jgxdz2tfAdv1_15NIBxDX3j6j5oDTkXTV1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ورود خودروی حامل‌ جنازه علی خامنه‌ای به‌مصلی تهران
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67254" target="_blank">📅 22:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67253">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3ENSkopgj3JXfFSeEOYbqo2eruKq5Edd6uXeXvu_pj1G3br8DcKRbTZ0tHhq0y0l0eW2H6P0LG3qUbxg99ag38C9Ksb7_MCB9om1jESbEyB_fTJNx28yKneO9ckwN5X3MV5T0ad5Jmc8QJqwRNSTC8ZK7X5B1bbx9MqESLbAkDISRA-7Tju_8v_nyQoQF5YVNViGsEKVj0joFJRSwfA_yJBsyGzKIFUSghqZPXSDAIAo7K--WXXVc9Cq2No9X0oySGYziZix4OU4T9Y8rIMdn6PBOIF0PSWxe5oFtEVs99hoKOtZHhSBpjCEm_6XPQ9xkilXiVmnvywHGzq2dmXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سید مجید نقطه زن فرمانده هوافضای سپاه هم بالاخره از سوراخ اومد بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67253" target="_blank">📅 21:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67252">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyrM_b_XCOK2IvpO_UtxfdYuZzUjU1NJ_umw4cgwCNdN4dWfVU-0bjUSVNBw-e67Bp1p-tvcgPD2F9Sa03oobo-UQBRdl2shbP2YzvXVsVZjrxu2y8kL-sNiRD5V77BI5G20bhbjyY-ZoRT2ZgTGtFXJTVG-bHtZi-oe8SBUcl47LJOn4_ZWx_ns0MwF6LUraCLp2wwmNixH3TcEMcBiAOxLnadAuF_wki-7GEvc6qGOX3hryjnc5hyykwMM3nyWlvjO9SR8wsGEPvMUnRceOzwA3ZcuALb7kl_6PCb1glI-8s87VG4Q5pNrcu9OzktZ07SlLwJ1s33Ia1OkIm1y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ: ۵۸ میلیون بشکه نفت و میعانات رژیم روی آب مانده است.
حدود ۵۸ میلیون بشکه نفت و میعانات متعلق به رژیم تروریستی جمهوری اسلامی روی آب انباشته شده و نزدیک به ۹۰ درصد این محموله‌ها هنوز مشتری یا مقصد نهایی مشخصی ندارند.
بر اساس این گزارش، با وجود تعلیق ۶۰ روزه بخشی از تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خرید نفت از رژیم جمهوری اسلامی محدود مانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67252" target="_blank">📅 21:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67251">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWhVfeSQS0-k8zhwufwtMKdG94WBlV8zZ8n5rCJqOpMvSWNItbr8NhQPrVGjXmOyzJ43wrOGztWkkHey02-u4Ozty4WoxkGiSuiVnVOvLl-SzZsK2sKL74_oG52gfx17PMiV_YY4M27pnLV-vO90iimkCu4Jh18J_Furfs7iMTHp7Cs3cWDyszi6y_s6mSLiegv-ehFjEBRDALCaT-xPKqWGD-X6INgc5Px4uPERfcrTfor5tZdZEUV-Dk83Lw4hUK1Iye9c2rBrrMxQm7EDzqnVO01qtyMKBcASw8amTgXWKem1uXFh2Bq3rYn4XgasIKWoq73nn85eKMcaFkQ99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
نگاه معنادار عراقچی به قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67251" target="_blank">📅 20:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67250">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfb7i3vKjbMXa19xtT2ohmM62JvwU5v_xC57UlCYTptHJgGVGcIECy1v55bNxPILnZWuLIyGwTuQt_TyjvH4e24PfmWeDgYka0uw3RsRg2xhIO0H1PMK6r4dSW10ZbVJsRslyQEqJ94S8BBl3UBnXgP15DOXAb8C-YnxvoxvmL21qNJheOqbq7XmcAm5vXOt0GuCRjw7RzjVHU6xbj6aLQcUWIbSRAZ3LsKK-4jsEnHRN0NtQpMOP-TWs7xO3SLdmiWtTDenYbYRXHJnJL3EU68sD32g6qLZROghnrCL1cX3KFt-mDYk06I1giUqGyXs3ewRKENxCyXHS4WisPtAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید (آکسیوس):
رئیس‌جمهور ترامپ امروز با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفتگو کرد. دفتر نخست‌وزیر اسرائیل اعلام کرد که آن‌ها توافق کردند به‌زودی در ایالات متحده با یکدیگر دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67250" target="_blank">📅 20:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67249">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUavKjwEezKvp8yxDjk9f3K-ucBsScwQlwnXUmmtxzWc3_tsBb9QqmtVZipj8kY5hE3R1Dwb1S7o98X4Wmou_kfZsMIHdoNaPhURpBZmNBdNY23l3kaN4WhEbDetNkZsLehKmqQnyFNQEQSGLsXTvIAKHn_B9pLEWYedjCRYdXNT6NJQSbbSdDbjli0wDagNU0WQNXH2ytn-J69JjotIawSW-_ytk_OMzFvwpko06yKyAbcD_-L5-pXMORwfqFEWNLTB2h_zdgUz_RFEFd90y7wTf7cMqQWlYq58cYU1AeE-3MxNCBWuWI1BdfjS2o0WOoQFDUqRMYnv7kwXh7m44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
😆
‏سی تی اسکن از دندون عقلم:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67249" target="_blank">📅 19:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67248">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHJ72TPPAe7iW-fBNt1czBEUDqk7nH-AIBEPZtyRNh80PKTGV5QA611QNuBKqCMJ_vZmyrKbFm5gW5RwKdBOoUNBIjOqjizL23Fn0s8lR3-cVADN2M-tMLo-iummAMWOhqvd9DeCg-aoDtPKvAl2hEhbtjNhD6cGsAI5m17Ke5FmP_00xzBRULN45IebrOSPEg7n1P0MGkBXY_v0eM5vo8aRF6EbDT0SCnJVDSMXc03MFOKWYsN8nVI0FVLvtP0pYxhvULsYfCKj3TgjsOX_A8mrrZh8_GwerUOBVlicuVAb1DC4UGp7BjvPQ4-63kSMfRq-q6uxzYbX9ECkiYDM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دفتر نخست‌وزیر اسرائیل؛
گزارش نیویورک تایمز را که حاکی از آن بود مقامات آمریکایی معتقد بودند اسرائیل در حال توطئه‌ای برای ترور مذاکره‌کنندگان ایرانی در جریان مذاکرات با آمریکایی‌ها در بهار امسال بوده‌اند، رد کرد و آن را «یک تحریف کامل از واقعیت» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67248" target="_blank">📅 19:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67247">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=ZFRoDF9nIEP2u5c-IYosKxYHvuI1J-jkqxgimXQI1pGjSlym4IpkXvrxVubiaNOsy716_sUWJfjCekaKGuauJc4weVbRobCae5MrqypXBNdn06zKG0r7FIgnh6fT2oNXXQi_y7YE4suVcpRVwwdpmy8Vwluy57TmLCaXSUDYLOlXz5PuLzGoKLshwyQUTpQ9A4l_3WmT_ErJztp1mqLEJsM-eD5_0WW82DNGDg3BsfMda3wuwzF-wnHCm1g7Cs9x8lJdY_57LAFUFmcxVW-ys6p1lB7h4FxH7huqgbPioi1XHXDY4HlNCw2T-JxbtA1rgbQFZWzWgU1WjtXEEDO1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bc1c344f.mp4?token=ZFRoDF9nIEP2u5c-IYosKxYHvuI1J-jkqxgimXQI1pGjSlym4IpkXvrxVubiaNOsy716_sUWJfjCekaKGuauJc4weVbRobCae5MrqypXBNdn06zKG0r7FIgnh6fT2oNXXQi_y7YE4suVcpRVwwdpmy8Vwluy57TmLCaXSUDYLOlXz5PuLzGoKLshwyQUTpQ9A4l_3WmT_ErJztp1mqLEJsM-eD5_0WW82DNGDg3BsfMda3wuwzF-wnHCm1g7Cs9x8lJdY_57LAFUFmcxVW-ys6p1lB7h4FxH7huqgbPioi1XHXDY4HlNCw2T-JxbtA1rgbQFZWzWgU1WjtXEEDO1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بمباران بیت رهبری 9 اسفند 1404
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67247" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67246">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YjzF9HVK8ZbOHP137q9dubClR7M3XkXPCkf4XJ0ZzzxNbxpFux-Y3e7ZATMpcQaePG8lHmUpjAMe65pVHtm8XBQNAIFJB8_x5y-HMEZgbLkttEgPBE41eFMdG_EDUn9fGPCbxknHVz2jHe7efHy0dj3opG4bOGLM4Mwm4K1z4POZXVJIWSPwjEcVa9fue-vAenptxDwmkFPGDah0e7CwKXoTvZOhExhkpGLhxPeqCdubwLM6RhGW6L2T4SgacHu7weZgk-rHgcrx_5555IgHf4t8gjirYF9MZWLtemLh4z6iBumB-LBh5UKMe032-MIDzAnN_MJY0TY_3icxzJqP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67246" target="_blank">📅 19:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67245">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=c880j0fwUUQlNe4Kfy3G-Ydn_JJeCiQr09WL0PT9QmlulSFEB_1dcEMqNYg1jeRjSm1oZK6q_EDrhtH7V9NnEaqenbrF9-_M-cukRq3Yopr5TXK6jAvOUjj3nWu7Y6AH53MQZc14t5Kk-9a8HRqWu1e3NFKdRG8Y-yzl-8_EbsKcrw9k2YLec9COtO_XvGpbLnnDlunYEHVb6JDq0DsPSRJwzAwU8S-Wkx0pdD7Xys5ZQE3Dx3txPd75jhQma76CP0afskir4pRjUQEZgAiaeuYgDAsMRg6PvHr6CGqgrTLjKFhGuMhXGuZog79op8yd4LxlpLjrTd9GbJkBFg3YKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1099f5d95b.mp4?token=c880j0fwUUQlNe4Kfy3G-Ydn_JJeCiQr09WL0PT9QmlulSFEB_1dcEMqNYg1jeRjSm1oZK6q_EDrhtH7V9NnEaqenbrF9-_M-cukRq3Yopr5TXK6jAvOUjj3nWu7Y6AH53MQZc14t5Kk-9a8HRqWu1e3NFKdRG8Y-yzl-8_EbsKcrw9k2YLec9COtO_XvGpbLnnDlunYEHVb6JDq0DsPSRJwzAwU8S-Wkx0pdD7Xys5ZQE3Dx3txPd75jhQma76CP0afskir4pRjUQEZgAiaeuYgDAsMRg6PvHr6CGqgrTLjKFhGuMhXGuZog79op8yd4LxlpLjrTd9GbJkBFg3YKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بغض و گریه های تمام نشدنی قالیباف در مراسم وداع با علی خامنه ای:
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67245" target="_blank">📅 19:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67244">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=n9W0VdK0aKH5tpBQoOod4vcXXTpAgbJ4VhFjDI4MaGipCSqoexQ5CgVemzXnZYPogOOV8jYF9xP7bAsOg3euAZ64IdXfZTXqm7a-MRBYeqTLjFHudXqn7jfbhOTDwwKhE7KsvLCHPHfiIXE9hbLIvZmMWfiSxOPCevhlUBL7GiJZlPtsMBHSUKAikgNwXh1bYpFW0KvohnvI3N1cH8aEYhFrrMAtJFa-kNYfTir5D13168A0oyTpdUv0mD8XAYTGlO2IZZQxZnfzycdLAtd0DBmt22uPwTzX1G7gbhGw_Zv-0cpR0LhA63CBYtmL6P68g2zVwD2iS37r5Gi5SuZe7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff481eda8.mp4?token=n9W0VdK0aKH5tpBQoOod4vcXXTpAgbJ4VhFjDI4MaGipCSqoexQ5CgVemzXnZYPogOOV8jYF9xP7bAsOg3euAZ64IdXfZTXqm7a-MRBYeqTLjFHudXqn7jfbhOTDwwKhE7KsvLCHPHfiIXE9hbLIvZmMWfiSxOPCevhlUBL7GiJZlPtsMBHSUKAikgNwXh1bYpFW0KvohnvI3N1cH8aEYhFrrMAtJFa-kNYfTir5D13168A0oyTpdUv0mD8XAYTGlO2IZZQxZnfzycdLAtd0DBmt22uPwTzX1G7gbhGw_Zv-0cpR0LhA63CBYtmL6P68g2zVwD2iS37r5Gi5SuZe7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد سردِ حدادعادل ( پدرزن مجتبی خامنه‌ای ) با عراقچی و قالیباف
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67244" target="_blank">📅 18:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67243">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=RvoatEUvhF4BFYQZXcGD6nOP9cgo9fglvwrQEN9bMzwSqyMlL-w26HiL_z5XSd1T2fDKxKbgnDD6j6vArRk_eYNMqKs2zaXY07PsjOlpls4-In4q8HPT0cQ8WGB1jTpXTLoG0jFbBp6ZveQl-WSUItnqT5_eGM4SIrN7CdvIF8Nq9x9YS2pA1o9NHwntJHbNoaxQ6H4BHb-JV2LAfSrO-ChDZIpTSKTCCJnsWc6EpzDEsD6DrBPH0OUfNOOSQ4QaSngLtkiIt5teNtVqCk3hFMHTmYFpTaEgkreEIrbUMgA-xaZTmC0hysjJ4ZIwwU380eSER4RfMbsTGVhL0N5Czg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d67ab774.mp4?token=RvoatEUvhF4BFYQZXcGD6nOP9cgo9fglvwrQEN9bMzwSqyMlL-w26HiL_z5XSd1T2fDKxKbgnDD6j6vArRk_eYNMqKs2zaXY07PsjOlpls4-In4q8HPT0cQ8WGB1jTpXTLoG0jFbBp6ZveQl-WSUItnqT5_eGM4SIrN7CdvIF8Nq9x9YS2pA1o9NHwntJHbNoaxQ6H4BHb-JV2LAfSrO-ChDZIpTSKTCCJnsWc6EpzDEsD6DrBPH0OUfNOOSQ4QaSngLtkiIt5teNtVqCk3hFMHTmYFpTaEgkreEIrbUMgA-xaZTmC0hysjJ4ZIwwU380eSER4RfMbsTGVhL0N5Czg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی قدیمی مربوط به انتخابات ۸۴
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67243" target="_blank">📅 18:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67242">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tx2eRCTIr9uMunLHKizc6XYcVAMMOGe1GHYmgIRaVMmLZg7KPfikcW81nxcTGRtsABOiJ5-h8Bip0BsS693PQvaK1_B1pduEjPu-7MDh3P_1qomfkfkYL8_bzvxOysZqiaffSkoOst5x-zi0LtojWVchjIPLDn3j1iRqocMu9GDjo68JA5nbXN4L89oik1DE07iOI0gYq40W35yWTNazsDX8sdjS6H8r391cVCLSeGsn-DcB_vqbNqKBzjFlBPS8BrgO4UH84T_DYOztpfFTHu2TPp0dC0HjWFd3YCcYs7wmTdYiSuNmgwmBkXlDLpzd4qsDUprvy79LV4IFA4Wqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهره خوشحال پزشکیان در استقبال از مقامات کشورها
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67242" target="_blank">📅 17:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67241">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=mbRhuqC8pwKhdRr-p5VchtPf7ev1RYCfFx0U5O9z8R5bmk3sG4NvdwWdFxorHBWpqoQlfMku-iofdnhzWyc8nUHTHAGnPOER91rkE1BpntFMYLARGQYiRgtZnNAaTD9QvwzkzXEIQQd73kzrR9SQJn3YPE8D-gPeqvye9QCTAF6acpuiNvK2_sPmbIQnzW7hHosZsb38lI33AQWbDtXZCNeKUbLXu4G4uyda_8nU0Q1FNA4IxjxgDYouWHEEd777MH22ld41MGi3TV0h3Su0MdNn8v2AGDK7-uQyu7MyP3yDFW2-BsYx_C3Tmv8bvmgNIWGoIslQR3MAcEN_8FTpdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4864316f1d.mp4?token=mbRhuqC8pwKhdRr-p5VchtPf7ev1RYCfFx0U5O9z8R5bmk3sG4NvdwWdFxorHBWpqoQlfMku-iofdnhzWyc8nUHTHAGnPOER91rkE1BpntFMYLARGQYiRgtZnNAaTD9QvwzkzXEIQQd73kzrR9SQJn3YPE8D-gPeqvye9QCTAF6acpuiNvK2_sPmbIQnzW7hHosZsb38lI33AQWbDtXZCNeKUbLXu4G4uyda_8nU0Q1FNA4IxjxgDYouWHEEd777MH22ld41MGi3TV0h3Su0MdNn8v2AGDK7-uQyu7MyP3yDFW2-BsYx_C3Tmv8bvmgNIWGoIslQR3MAcEN_8FTpdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان در تلاش برای جاری شدن قطره ای اشک از چشمانش
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67241" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67240">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=APqrW6Wx3zZycKzhnKXacG5QeKwrsGLl1fuXp3JTlIkbfm3WnzgIU8AOsruId6qlzUGtbZaz4ZmHhRv96XB5AVJunBBrEfnjnhWRh7nej-JNbb3UQGE_nLjTHSkWBtXVsA3MBj1muH_3OP5so__k9vQ9NiUEvHm_sMB0guwtew7_RkdwrMtvASieOvMYJOQFzWYHEONanVfQGDnCOjdETQDg_2QpejEt3_ySibjC3-47_swuz5-WkdPXbtC43VObRiSlhVIBjMjqJlOE_09RRiqD646URwXNN0bzv9crghOmoA4XZxHhGwfl6ixBjWpoGK1JGpfs6RRaS7MfGMh4Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597b986b2a.mp4?token=APqrW6Wx3zZycKzhnKXacG5QeKwrsGLl1fuXp3JTlIkbfm3WnzgIU8AOsruId6qlzUGtbZaz4ZmHhRv96XB5AVJunBBrEfnjnhWRh7nej-JNbb3UQGE_nLjTHSkWBtXVsA3MBj1muH_3OP5so__k9vQ9NiUEvHm_sMB0guwtew7_RkdwrMtvASieOvMYJOQFzWYHEONanVfQGDnCOjdETQDg_2QpejEt3_ySibjC3-47_swuz5-WkdPXbtC43VObRiSlhVIBjMjqJlOE_09RRiqD646URwXNN0bzv9crghOmoA4XZxHhGwfl6ixBjWpoGK1JGpfs6RRaS7MfGMh4Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در یک سو مردمی که در زباله‌‌ها باید دنبال غذا بگردند و در سوی دیگر «تامین ۱۲ هزار تن کالای اساسی برای تشییع قاتل فرزندان ایران زمین و عامل شماره یک تمامی مصیبتهای مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67240" target="_blank">📅 16:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67238">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=ZCassu6tEjxLEqDpLC_5YV9djAAivKeva8SXj7dmxjqv0U7fnjnRlmN3Vcs7jfpS9aKz32gXfqG8Zah33qq-3nuU_wDC1S2WUcr22W3iOtqCvYm-w18YVcgJRIycaqzQMDByUviRvtpCaxPPX2KMLU3xwPXgHrbPgshGL87CxiUmDTLZoyvE3lh0Gfq02inWGDOB8pElsbegV6wAWT2rNFlYiU68DpyQTkEJSkZzxtoHfZ6F6n7zp-uIX1lytR4xJO4FgmUhDHosWmu8nObeQmQotM97hvuMzjbQyV0srqDpTp_xOtAwTASJ1rO5bM5NT8uandTl6-1EeFy72_3ZIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b4f0f3e3e.mp4?token=ZCassu6tEjxLEqDpLC_5YV9djAAivKeva8SXj7dmxjqv0U7fnjnRlmN3Vcs7jfpS9aKz32gXfqG8Zah33qq-3nuU_wDC1S2WUcr22W3iOtqCvYm-w18YVcgJRIycaqzQMDByUviRvtpCaxPPX2KMLU3xwPXgHrbPgshGL87CxiUmDTLZoyvE3lh0Gfq02inWGDOB8pElsbegV6wAWT2rNFlYiU68DpyQTkEJSkZzxtoHfZ6F6n7zp-uIX1lytR4xJO4FgmUhDHosWmu8nObeQmQotM97hvuMzjbQyV0srqDpTp_xOtAwTASJ1rO5bM5NT8uandTl6-1EeFy72_3ZIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:‏در واکنش به آسیب واردشده به نیروهای ارتش اسرائیل و در پی نقض توافق آتش بس: حدود ۱۰ زیرساخت سازمان تروریستی حزب‌الله در جنوب لبنان هدف حمله قرار گرفت
🔴
در حمله‌ای دیگر برای رفع تهدید: نیروهای لشکر ۹۱ یک کامیون مورد استفاده حزب‌الله برای انتقال تسلیحات را هدف قرار دادند
🔴
در حملات دقیق نیروی هوایی با هدایت لشکر ۹۱، روز گذشته (پنج‌شنبه) حدود ۱۰ زیرساخت متعلق به سازمان تروریستی حزب‌الله در مناطق بنت جبیل، بیت یاحون، کونین و براشیت در جنوب لبنان هدف حمله قرار گرفت. زیرساخت‌های هدف قرارگرفته توسط این سازمان برای پیشبرد طرح‌های تروریستی علیه نیروهای ارتش اسرائیل که در منطقه امنیتی فعالیت می‌کنند، مورد استفاده قرار می‌گرفتند.
🔴
این حملات در واکنش به آسیب واردشده به نیروهای ما در منطقه امنیتی توسط سازمان تروریستی حزب‌الله و در پی نقض مجدد توافق آتش بس انجام شد.
🔴
همچنین بامداد امروز (جمعه)، نیروهای لشکر ۹۱ یک گروه از تروریست‌های وابسته به سازمان تروریستی حزب‌الله را که در نزدیکی منطقه امنیتی در جنوب لبنان، در حال انتقال تسلیحات با استفاده از یک کامیون بودند، شناسایی کردند. بلافاصله پس از شناسایی، نیروی هوایی برای رفع تهدید علیه نیروهای ما، این کامیون را هدف حمله قرار داد.
🔴
در پی این حمله، انفجارهای ثانویه شناسایی شد که نشان‌دهنده وجود تسلیحات در داخل کامیون بود.
🔴
ارتش اسرائیل به فعالیت برای رفع هرگونه تهدید علیه نیروهای خود و شهروندان اسرائیل ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67238" target="_blank">📅 16:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67237">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPgQyClc35lgT35oGQRkmHJhBlYHIV_7SnIbB8v-Rks3t60lIhfkBtydqBDFnsDEKzm-4T6DYzomnO3SBGQdED-hBZ06HGknKsey_eS7t9EbQ8_MlXUheKtQI1sgt-U8IsyRQjf2BoZ_-jO7ymmbBk_I586Torck3dkgd5aVX3Hff_ucn_uFgAHxMcqRTSqnUNCAUWR4YgbjA9CEcBFGKduU5y6pKAuXjvpbsqhJoo9IPJuYJmiK0UUQKMLE5d6aE91AUGEA6GxBnle0gacd3QL4cz_BQAcdXyFaUdcO36Ynzifajf3fLZ77FYKgrRiuKi5aPeXM-CgSVLI3lsKwpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پنج فروند بوئینگ ۷۷۷ سعودی سابق علیرغم تحریم‌ها به ماهان ایر تحویل داده شد:
پنج فروند هواپیمای پهن‌پیکر بوئینگ ۷۷۷-۲۶۸ER دست دوم از خطوط هوایی عربستان سعودی به ماهان ایر ایران تحویل داده شده است که دو فروند از آنها در فرودگاه مهرآباد تهران تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67237" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67235">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6HC0bO302-9ou4e_Tr5-lRUF1jV9JeFth2xB4vMx1I3KYWWNPrQFeHw_pzCUom_yojtfVdH-Ln-aLxFe5USuFHWsmHUuOrdhwNvCn_QLPrPejofsMXcS5pw1mlXWHERZzZa9E_tsNFzNf0jmFRidth0WPPNyK7FxykXI0271CDvq4Wblko4c0O2CpvZzg5c5uwiUawc-CEsaWU8-RIfd93AuqOQ5lIYJ9bAsMBrRdUNkYy6sl4oOyWivQv2g2LGLMVFYewAXwyMVxMVDKpF05lJsd_qoxhzZGGV0MLIKUzqvmo04WoNYeP-i3Kw2Ph_e7dlQTOdY70mJYcbevbTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=QL1F05kN5uS0EJvUQz_ncu4j2QbcrLoXw2QAnHq0qmTq7sbYlv49YJebDQjCnX_gleaXkAvdU6wAf0Ysm-m6y6IBJ5qBZD8JyZbsxHAlquNUSocQmcDByFgGQ6WHfj3wQoGdCQV-Edvf0ERcZzHDmWzRMh9foT-qO7LsXuAuwCR0q-uFLOEfgZPIElFnLcNCtOf5etjCYAyrq0traWZGqal_Fo3es8Nud4yAZ3uKU_Qefhk2r0Wtxd7xACi3y8bEfZtLtxUyZnW21fgQGeH-RkrGstrZyRJ-T4KTrzN2oAgxFGtguELEO743MkOWjGgv4mc7FOqt8-Fmkbxy6MqYyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e169f3d67d.mp4?token=QL1F05kN5uS0EJvUQz_ncu4j2QbcrLoXw2QAnHq0qmTq7sbYlv49YJebDQjCnX_gleaXkAvdU6wAf0Ysm-m6y6IBJ5qBZD8JyZbsxHAlquNUSocQmcDByFgGQ6WHfj3wQoGdCQV-Edvf0ERcZzHDmWzRMh9foT-qO7LsXuAuwCR0q-uFLOEfgZPIElFnLcNCtOf5etjCYAyrq0traWZGqal_Fo3es8Nud4yAZ3uKU_Qefhk2r0Wtxd7xACi3y8bEfZtLtxUyZnW21fgQGeH-RkrGstrZyRJ-T4KTrzN2oAgxFGtguELEO743MkOWjGgv4mc7FOqt8-Fmkbxy6MqYyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بر اساس گزارش‌های اولیه، جنگنده های عربستان بر فراز صنعا، پایتخت تحت کنترل حوثی ها، به پرواز درآمده و مواضع این گروه در نقاطی از یمن هدف بمباران قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67235" target="_blank">📅 14:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67234">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FQMR4Jibc9MyQ6jWmrbcm9AGfzNPXUGOaCyUKSAeoY6N88Be2LhjCitmsA_eF__wZYdwlQj2TdcQyswNp3qjgzbHdXwOoa1y0ZmGbFJdAEdbd1g7mH1WPb0FNVTUi-USc7E6JzV_pZCX25iLGf8qrDMOs-WV_TGSXzBspk-2EJwhO6xx4ylCNB5TekAONJifhJM_Mze1irwWFipDAK0srbhKTemBAlpoxHXHCeWKU6QfuZ84jyL_OoEOVzqoKqnHFco1MyEQCAU6hZpavFuHOWqHSN6d4wD_JrmOInaDlqDH1kGIHOIXyx5lCsRAFXZfIZnGr-1_hWaM7tX5MBWBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این عکس از تفاوت تابوت محمدرضا شاه پهلوی و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای شکل و ظاهر عربی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67234" target="_blank">📅 14:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67233">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=E1cs5r3KzwCL9E9c46J0vGXl6ewShjVy21DDcNTYhrF0XvwWHyDLll5XgOdvexTPKay65JEKggwD3UveEypHgydz3QXp6VQhcD58btWi3DBa1ILjjrEnaQJpAQSoSfPyi4B0wDcpgkj6BHQFhWVufLDflgYkmvRAXICTTV_ahIaYn-o6PJYedSlCqf6IzB8yShV_9_22abmqIz9riVWl4DW1J2mB_LhY4FqE8Gr5iileMgOAa66zacwLQ2k-47oSlX-q9-9vqP6QD4AZAcpEO72YetpBJZFQwVYfqWSv-lmgnAbe0S5dyNW2f-LWGbu4h5323paz0EpqEz_pfvXUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4654e8258.mp4?token=E1cs5r3KzwCL9E9c46J0vGXl6ewShjVy21DDcNTYhrF0XvwWHyDLll5XgOdvexTPKay65JEKggwD3UveEypHgydz3QXp6VQhcD58btWi3DBa1ILjjrEnaQJpAQSoSfPyi4B0wDcpgkj6BHQFhWVufLDflgYkmvRAXICTTV_ahIaYn-o6PJYedSlCqf6IzB8yShV_9_22abmqIz9riVWl4DW1J2mB_LhY4FqE8Gr5iileMgOAa66zacwLQ2k-47oSlX-q9-9vqP6QD4AZAcpEO72YetpBJZFQwVYfqWSv-lmgnAbe0S5dyNW2f-LWGbu4h5323paz0EpqEz_pfvXUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
حضور فرماندهان ارشد نیروهای مسلح جمهوری اسلامی در مراسم وداع با جنازه علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67233" target="_blank">📅 14:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67231">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_U4_FU-G05CQBr-bHGOy19gjmcSVvy6N_nX5EFUUVdpufQsHDXdBaEqngcTgfA_oi7JyJTnDfjkjEEx_Jtii0G8KpssO4vRfWMJSx2P4_Pi7Nb90ifG1cBcO2MmRhx79vVqdt9C-ffDCvdx_ljmQM9R-pdv4AmxrbOyM9ujZ-_hI6QcbuuSDONA-Gw2mOMSmwRXk9AWaVVhwsR7oZP-jc_R4gUGv_mW_8KQD7gkzifOkV_8p7aWWY-PA0RwuY9YjQnCFLyBcZKkvad22x2YRNRPDQ49ngTK_sMjNKDAjfqstPyp9-JclwYtj5OzF4YgnvcvD2tjEquWJDkspGSyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=DAFZycUKAI0IPOKSqRZVthsbR1pcg0IoAxq2PN1i7OAXdXOFivI0-Go5eHJL-UbMVx-H05ck9ihUGAHq2Tj4cdCAEcvs8sq-GkVl70DzJpuYZQWMhVP8GfhncqfxJICy-Iox2sQR3_-tbpj9Z84Mn23L7qdjauPl1hBdLG-MIpkQIdlMyUXTgGj9gLUGFPqfUGlOI9RyiB0L2sNJz3S5-jVl8oFr0b9n_GyOwTjUM7eHFnXQT2SrZcP1E345pLaeekK3ZEVM9txm74xW3qjNESxe8e_blyCOD5iFBRrbMfYhaHi2Es-nbFGR02Bl9w3BVQofJjc--5ek1RNWOQn3dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1483e21a1f.mp4?token=DAFZycUKAI0IPOKSqRZVthsbR1pcg0IoAxq2PN1i7OAXdXOFivI0-Go5eHJL-UbMVx-H05ck9ihUGAHq2Tj4cdCAEcvs8sq-GkVl70DzJpuYZQWMhVP8GfhncqfxJICy-Iox2sQR3_-tbpj9Z84Mn23L7qdjauPl1hBdLG-MIpkQIdlMyUXTgGj9gLUGFPqfUGlOI9RyiB0L2sNJz3S5-jVl8oFr0b9n_GyOwTjUM7eHFnXQT2SrZcP1E345pLaeekK3ZEVM9txm74xW3qjNESxe8e_blyCOD5iFBRrbMfYhaHi2Es-nbFGR02Bl9w3BVQofJjc--5ek1RNWOQn3dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس حوزه انرژی: تنگه هرمز از مسیر عمانی، اتوبان شد!
این فیلم از موسسه کپلر را ببینید،
چقدر تلخ است، کشتی‌ها و نفتکش‌ها در تعداد بالا از مسیر عمانی از تنگه هرمز عبور کرده و همچنان می‌کنند.
با این روند، به زودی ترامپ بابت تامین امنیت کشتی‌ها از مسیر عمانی، عوارض هم می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67231" target="_blank">📅 13:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67229">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fa301248.mp4?token=OHOys_PxTcf9nLTBzzu1hipET3wfGsK0qNxGoA5N0PPdxUiIsvfpGco0Fy7A1EMKRLYtqUa_g_B1heH6qYnODHQ4OBSb2kuxqVHUQmYYIgif3TerWQTRCeXk_ciGOibAdcu3P3T34NmioYXdBaQ8qCqBwkygppEZWQwrpzlbBaskPqvn_hM78BAlgSV2Ru8Cz919xoAT3UapmqXfoCxFZaEQUawx-NQV6sQKossXNrQS5HEVnOLfC6R_xKz9qgX_BkC_7QK99XxjnBVK_qGeqgDxmVa-OieHAqVqu0kDeq22QjoaPmhZ5ql-K-0_CkoFrXLS9bpqo49VHb2ngPN8GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fa301248.mp4?token=OHOys_PxTcf9nLTBzzu1hipET3wfGsK0qNxGoA5N0PPdxUiIsvfpGco0Fy7A1EMKRLYtqUa_g_B1heH6qYnODHQ4OBSb2kuxqVHUQmYYIgif3TerWQTRCeXk_ciGOibAdcu3P3T34NmioYXdBaQ8qCqBwkygppEZWQwrpzlbBaskPqvn_hM78BAlgSV2Ru8Cz919xoAT3UapmqXfoCxFZaEQUawx-NQV6sQKossXNrQS5HEVnOLfC6R_xKz9qgX_BkC_7QK99XxjnBVK_qGeqgDxmVa-OieHAqVqu0kDeq22QjoaPmhZ5ql-K-0_CkoFrXLS9bpqo49VHb2ngPN8GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پالایشگاه کلیدی لوک‌اویل در روسیه هدف حمله اوکراین قرار گرفت!
این تاسیسات سالانه حدود ۱۷ میلیون تن نفت خام را فرآوری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67229" target="_blank">📅 12:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67228">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7KSdHsxxIZIqFCyVfa6lYlcbwyOOgWfsTnpuihZY00Ixxpt0FjU1ZBMDZrkgYpdksfS5oesS1_K1FH7lOO_f69o9d91f8-hKAyKjjOWSACbJngdJpJZKCsvTASImc4jIQbuGzPpZrBBDi2y3flw4G4I4BXZXojdHgKlS1gNMlejmydV1JA0RWdGw-JNMnx0aVpvPay6vzqXXLhlVkBtkUKlZwQITpjXZ4D0Gf9j6SKv35uXxF79ehS0uTP5WrzGcXFbdmu5knT5SCiZK42jY9WqTA9ec1CFSNWNxhbuF5n_HQtrTLwdVfwH5CNgfu8-uJ1uqqHJ0qZ_oQQFflbGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
همان‌طور که ترامپ درباره درخواست ایرانی‌ها برای برگزاری جلسه در دوحه دروغ گفت، دیشب نیز دوباره دروغ گفت؛ این بار درباره حمله به تأسیسات راداری ایران. نه جلسه‌ای در دوحه برگزار شد و نه حمله‌ای به ایران صورت گرفت. هرگونه حمله‌ای از این دست، با پاسخی کوبنده مواجه می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67228" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67227">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppthnRbkpu6vrgrRJDn3hL2DQdAyM2oTmHsvdq4p_G9AhZejQKrF2xcdTh9iXZWKn5VAZLRdhWzLuj4n3Z_ql0hg2xd6J7Fhas96KZJRgwCaMfl1PHvCyVEqMlHTA9LeRa8CxWhu_jIdqm809bVs-MGU2lpa-KAH4OlLomW9nrp0H48wmaleb3Adf0V5N5AJv1JnGiSSKXf5Q8qAyhhVpNVvdRcKFayNWE3rvkia92Z8nTCXCtNmKXcVMv-kL73h0UGSfmuFiyM58hEFwG6At8z14PjOMl9prP-Xvq2AXlEoiWa92L9ifKJGLoVDwj_XDTJ1cDzP53J-jB_EYTqzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67227" target="_blank">📅 12:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67226">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3hJXc-biWGo1n4mz-jo-YSsflwzdvKqziOACx0yEHVzvdeK6_57QqrpaQvdM3B1fe0bpV1UD50rt3PnQFgVlV3x8XA1aGmKrEozWtNkjZEoFe-IzeaEgVkQgwon4WXd5OC28f88IhMZvrhgtyxBg-EUkfzUu_Xo7i7mBjBavabdS_VrQ7T-0HPD0O5VaYHtZ8hbfckzJiQxbI-IWWDw0IG_tL88sR0p02MzfFo_tV_IiCEE8bpOIPXjsDqbvSzBF0JOi4LPfUtXb4VWMWAaiZ8EjOUqXtoxBkGISoCkWTeUCFrtjpTfANK_ds7O9HYFPRe8VPT-AIfjBRJR2ugwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید محمدجواد ظریف:
ایران، پس از دو قرن تجربه تلخ ناامنی و آسیب‌پذیری، با هدایت رهبر شهید به مرحله‌ای رسید که در گزاره «دوران بزن در رو تمام شده است
🤣
🤣
» متبلور است. این تغییر پس از دو سده، احساس خودباوری و اعتماد به توان داخلی را برای ایران و ایرانی به ارمغان آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67226" target="_blank">📅 12:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10282a802.mp4?token=a2qdOJJmLJxxqprVd32k_MQA2Mjw99e2KODVMLdufqEPxPQeUuuiOA233sU2GL3UeA5vkcDhws3LiTN2puicphS6Zv_dm6byfZ2ZtfRHF3nOel-B_t9vBnb9kITEhIynP8wiwTXQAi2HYWiV2Ty_cmrmULuzb5U1iEhZbkto84CpE15OjXRq6OXAoRI6PZ3yejhgvmT5cjGFKfI5qBZqRWzB9F6I6JPJDh5Z31z_KBcO_92lLEOWDSAkXcZSoWfFzhzVcL3GCamwd2zDUq5gMisEHEnyWoFHmC0YWUT64zRporskU0XT7nH65-0DUSdQakUpHFJR-ZFQxNKdik-eWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10282a802.mp4?token=a2qdOJJmLJxxqprVd32k_MQA2Mjw99e2KODVMLdufqEPxPQeUuuiOA233sU2GL3UeA5vkcDhws3LiTN2puicphS6Zv_dm6byfZ2ZtfRHF3nOel-B_t9vBnb9kITEhIynP8wiwTXQAi2HYWiV2Ty_cmrmULuzb5U1iEhZbkto84CpE15OjXRq6OXAoRI6PZ3yejhgvmT5cjGFKfI5qBZqRWzB9F6I6JPJDh5Z31z_KBcO_92lLEOWDSAkXcZSoWfFzhzVcL3GCamwd2zDUq5gMisEHEnyWoFHmC0YWUT64zRporskU0XT7nH65-0DUSdQakUpHFJR-ZFQxNKdik-eWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده‌ رضا پهلوی درباره اسلام:
🔴
من نه با اسلام دشمنی دارم و نه با هیچ باور دینی دیگری. ایمان، امری شخصی و محترم است و هر ایرانی باید آزاد باشد که دین خود را انتخاب کند، تغییر دهد یا هیچ دینی نداشته باشد.
🔴
مشکل ایران، اسلام به‌عنوان یک باور مذهبی نیست؛ مشکل، حکومتی است که دین را به ابزار قدرت، سرکوب و فساد تبدیل کرده است.
🔴
همان‌گونه که هیچ دینی نباید بر حکومت مسلط باشد، حکومت نیز نباید در باورهای مردم دخالت کند.
🔴
ایران آینده، کشوری خواهد بود که در آن مسلمان، مسیحی، یهودی، بهایی، زرتشتی و افراد بی‌دین، همگی از حقوق برابر برخوردار باشند.
🔴
معیار شهروندی، اعتقاد مذهبی افراد نخواهد بود، بلکه پایبندی به قانون، آزادی و کرامت انسانی خواهد بود.
🔴
اصل جدایی دین از حکومت، آزادی عقیده و برابری شهروندان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67225" target="_blank">📅 11:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67224">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226825be38.mp4?token=YGw5yvcolkzwp0uFVOwCJ7DDz5i5PPSWrhR8TXjyU2jYq0PCP8-kLLLjateNXRwkPzhcqbG9FZnyhmkP1pOj1XMHZvOc7XE2_WXJxojrFp5I1bXkABLRZGhNUweLdauHqbZhIoXTp3A_kUUQ21dP9Aeqxq0zy5woebT_M70L_PiYN7SSUWSbFp30yTguV60RlpIOrqNEMA5Zlgo5Y9rPaREMhPSff2A3axOjXXGpS3HKKyaJvtDP6F3ArKcDMan927HPYkURaqk5AANMRuJ2zMUBCYg9GZ505g76REZ04tVOP9FlAmi2nk6pkHg0NnGvEjvNZGtZ9na6QN--7Wl3Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226825be38.mp4?token=YGw5yvcolkzwp0uFVOwCJ7DDz5i5PPSWrhR8TXjyU2jYq0PCP8-kLLLjateNXRwkPzhcqbG9FZnyhmkP1pOj1XMHZvOc7XE2_WXJxojrFp5I1bXkABLRZGhNUweLdauHqbZhIoXTp3A_kUUQ21dP9Aeqxq0zy5woebT_M70L_PiYN7SSUWSbFp30yTguV60RlpIOrqNEMA5Zlgo5Y9rPaREMhPSff2A3axOjXXGpS3HKKyaJvtDP6F3ArKcDMan927HPYkURaqk5AANMRuJ2zMUBCYg9GZ505g76REZ04tVOP9FlAmi2nk6pkHg0NnGvEjvNZGtZ9na6QN--7Wl3Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نریمانی مداح حکومتی:
منطقه شیعه نشین جنوب لبنان ۱۱هزار خونه صاف شده، آقایان چرا نمی زنید زیر میز مذاکره!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67224" target="_blank">📅 10:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67223">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUQG0iV7z1ezgjnX872TeUykXPNlvNPGqC5jVyjwp7xFYfZcbtcOJCY5T_dm9J8te2Tp_ZaRfwm9vMszaiiH13mevBAz3U0wpMJPgmBJvDO41pSK7e5qb0ZcADdnR8Stz2e-Ptg8-MpBInhsPBVI31yxzHhKfUYtMb_eWNv0TRc6o5ue12u4Qw0JoUikpQlI7puVUyISQHzH0e62COaRE3mLTM8TRZi-EG1uqZ3mRfDQKjLo0-92JuaDLnqTQHlw4Ff6xv0NjA_apIfLPW8ODpWh-0OUV2NC5RZT3v8Kq8-bZ1mDmL_QKyEApVrOaGC8zVSz8CQJoDFZt13zNWR2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه بانو الکسیس پورن استار معروف اعلام کرده با مردای همه کشورا غیر 2 کشور رابطه جنسی داشته، ایران و غنا
برای اینکه کلکسیون خودشو کامل کنه، گفته فرم پر کنین و درخواست بدین تا یه نفرو انتخاب کنم.
از غنا 2700 نفر و از ایران بیش از 1 میلیون نفر درخواست دادن! جوون ترین ایرانی یه دهه نودی 10 ساله و پیرترین یه پیرمرد 78 ساله بوده
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67223" target="_blank">📅 10:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67222">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55805ed771.mp4?token=Q50VkDuonlPZD5W0MylGgTUdlYGzmE4ze9J0j40fAO32hafXPmRhYOEtLYSbTfiW_xtYhF7yqXn8FMSyixjAd9GrB63sOU0DTQ26FOrKwlwuK1G_KvPs5ego-h3-QJ-3bXBv73M2wLisu5KMXtXaNEL8RcU2VJvynAiLGYwGVsPuN0kEhXTjzYLYpcs4hM_MQZ7Cdw3Lp08-kkuwj1NVTtBuCay1BAJk4rxCej4RjRUUhmzTRLr40u53zT2XgVPjc56V9P9UJL9G44YgJXcq-5hlayz2UoGCcOVc8oilafQEUBDvguXcPwdkyX4tCS_1UhYKC5U9xD5r-YI2oR5FrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55805ed771.mp4?token=Q50VkDuonlPZD5W0MylGgTUdlYGzmE4ze9J0j40fAO32hafXPmRhYOEtLYSbTfiW_xtYhF7yqXn8FMSyixjAd9GrB63sOU0DTQ26FOrKwlwuK1G_KvPs5ego-h3-QJ-3bXBv73M2wLisu5KMXtXaNEL8RcU2VJvynAiLGYwGVsPuN0kEhXTjzYLYpcs4hM_MQZ7Cdw3Lp08-kkuwj1NVTtBuCay1BAJk4rxCej4RjRUUhmzTRLr40u53zT2XgVPjc56V9P9UJL9G44YgJXcq-5hlayz2UoGCcOVc8oilafQEUBDvguXcPwdkyX4tCS_1UhYKC5U9xD5r-YI2oR5FrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پروفسور جیانگ:
آمریکا احتمالاً بین آذر تا اسفند یا حتی زودتر حمله زمینی به ایران را آغاز خواهد کرد و امضای تفاهم‌نامه فعلی تنها برای خرید زمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67222" target="_blank">📅 10:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szP7KYIhIDiYtjiqufMjkAivna6QazWx2PIWNWHCPSt3xC3Hc6j_4-EkxL33rd-I39ZYDfB1Uymu0affU7TGKbHYjYyP3cEcQsClDb5MDqosj4bnUhIVTFiFBDy9IAb7sVTtq7cMaEEJR2udM5ySwEZ91PrHKsfVZ5dEWseCWMkRl5ua58Fp8nJllR1vVovQbF-1PUcMo_OODWis1-A4CtFSuZcp-8xTj0sCT5GPdBUtRY6AaAyqPjp_8-dmtyYAgl8e7VbCW9UILhg2n0jbQa_eU9E75KRhohzJT8iNMTNNk-AOEMc0gDGI-vx4T4vV7Qxv2pPJ7_RBO5zCzfJBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین فاصله زمان مرگ تا زمان دفن رهبران جهان، مربوط به الیزابت دوم بود با ۱۱ روز فاصله که سیدعلی خامنه‌ای با ۱۳۲ روز فاصله با قدرت این رکورد رو شکست و نام خودش رو در تاریخ جاودانه کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67221" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=fdJYcVi6liJ4Q3hybqsc0-D-vY5aE6TXE-NsP0N5r4lxI3g_efszPdwaDU2fPuJnPm3to-OoQ4P7FC4CRdat0MSZLCrdufGSe9ZWT1xrWnRN4U4DA0SdHcdy-H5ptezdbkSID8xwDJkCWhI3Ib0nSmgfsc8ji5DiyVdkq3hpxzkAR97wz5u2tUb5yeVbBK8wEFeWLqVGfBLVVQz7aYv1EmNsrqtoSwRmJYjvxqah0lKLu5_bLTqgb1qn93qF20FAG1vSp9zp7dwhMtMoOwOM_X_tpyY1g5zvQ2KFIg5EawIIZwJ1V1GIO5dVxYulkI5roFBxcsQgVHD7ccONCV2-JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f82b0159b8.mp4?token=fdJYcVi6liJ4Q3hybqsc0-D-vY5aE6TXE-NsP0N5r4lxI3g_efszPdwaDU2fPuJnPm3to-OoQ4P7FC4CRdat0MSZLCrdufGSe9ZWT1xrWnRN4U4DA0SdHcdy-H5ptezdbkSID8xwDJkCWhI3Ib0nSmgfsc8ji5DiyVdkq3hpxzkAR97wz5u2tUb5yeVbBK8wEFeWLqVGfBLVVQz7aYv1EmNsrqtoSwRmJYjvxqah0lKLu5_bLTqgb1qn93qF20FAG1vSp9zp7dwhMtMoOwOM_X_tpyY1g5zvQ2KFIg5EawIIZwJ1V1GIO5dVxYulkI5roFBxcsQgVHD7ccONCV2-JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان
:
من به عنوان مسئول دولت نمی توانم ببینم مردم مشکل دارند و بگویم همه چیز خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67220" target="_blank">📅 09:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67219">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67219" target="_blank">📅 02:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67218">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFuck Bet(cheGuevara)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XY3F0GI-aW94i27Sl1_KUH1mthVZ4GC1FmKiiC61mt-_eDLmw-O0fK6dftrbQv44ig0BuWGkeo5hTj86ynBuutHnrftL_Ugq6T_NZ9-THa0ejYWUPoWJ4ALL30Tap-QLX6JVDt5Q1S5E9hzfKGmBZghO40fQ2YJQXzfPqtmZQ2LVdmZgRh6CcVtsnGQGGuJ-ewY_R_2Y7sieMi-YBta9xbZDg5iGz9KL8Hy6Hwg42itEzdYTe8g7zY4zMyPgFh2vL5Mx0gymlmCch_KbiFSUSG0LFaXZN3k46ALM4GkumUmk1HdVnFZygL2yMhBdj5FYsXyR-znUrJrGYAMKlZpZ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
کنداکتور فرم های امروز
💸
مبلغ در نظر گرفته شده ثابت 100 دلارز
🔥
سود کلی 1,287$</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67218" target="_blank">📅 02:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67217">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=bmBjKj0oMUQUWCt8hKJnR7lLTj9ry1TuBiyLDpZMyEJ8KmQyDKf5Dh20H_hYdjRbhKbP0NvxLRs6RzJvW0gADZRvWaZWAo_1cHtQqSx9zPNjQCe8SLCuM4jyhc75MB7Ja0EYQcIyvil3TFZBf7xWFIHesALKTrEUx_P2g3zS0F2rcbonuD7g8WgoOZpcIZNaXIR_B8rYoQ4KJPXOWy8njr0FAZMcpAb1A1eAIoZzG9PqHJaDWY9J4wPPcTrkE4-NPRhmj8kLVMgC88bZb9ySorWwjJ-ZILNDFq4Z7IVZg78wLq2WSH7L8JUBp8idzpTve35LM3opC2sUw7evRvQKvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a8c8202f.mp4?token=bmBjKj0oMUQUWCt8hKJnR7lLTj9ry1TuBiyLDpZMyEJ8KmQyDKf5Dh20H_hYdjRbhKbP0NvxLRs6RzJvW0gADZRvWaZWAo_1cHtQqSx9zPNjQCe8SLCuM4jyhc75MB7Ja0EYQcIyvil3TFZBf7xWFIHesALKTrEUx_P2g3zS0F2rcbonuD7g8WgoOZpcIZNaXIR_B8rYoQ4KJPXOWy8njr0FAZMcpAb1A1eAIoZzG9PqHJaDWY9J4wPPcTrkE4-NPRhmj8kLVMgC88bZb9ySorWwjJ-ZILNDFq4Z7IVZg78wLq2WSH7L8JUBp8idzpTve35LM3opC2sUw7evRvQKvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«آن‌ها تورم ۳۰۰ درصدی دارند. هیچ درآمدی ندارند؛ بنابراین ما بخشی از آن پول را برمی‌داریم... و اگر به آن جایگاهی که باید برسیم، دست یابیم، تأمین [مواد غذایی] را منحصراً به کشاورزان آمریکایی می‌سپاریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67217" target="_blank">📅 01:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67216">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=KVuqI8f8OYolDBds8xe9c8-f75Zj8-DwA74r2vvvoQ3q_A9QgrGkStC_UZl4Q9UaKI5k2HruSKytc-9hzaoLT623zFSaXn7JvrNrBXBEkBst2jPDa29OoncTo3mnTsxU2QZIyhparAMyPjPK4Essb-r1RulQBAfW7jJ5k80r1NNw72Cz_pbtOiLurYxmlEh5HoYpCDijpFeQn-RU7vaku5JOzrE40PNLjVIl7MiwbupY2yHhWD-_2OhHv03vo9FML1U3YrhB-9S44Qye7X8ISWHorsYajrmJ6lJy2NbVFc1ef50FvXvRoEOFG-Pn1A3_gHHoJh7CIrdjeTQWIW8tBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ff4f4224.mp4?token=KVuqI8f8OYolDBds8xe9c8-f75Zj8-DwA74r2vvvoQ3q_A9QgrGkStC_UZl4Q9UaKI5k2HruSKytc-9hzaoLT623zFSaXn7JvrNrBXBEkBst2jPDa29OoncTo3mnTsxU2QZIyhparAMyPjPK4Essb-r1RulQBAfW7jJ5k80r1NNw72Cz_pbtOiLurYxmlEh5HoYpCDijpFeQn-RU7vaku5JOzrE40PNLjVIl7MiwbupY2yHhWD-_2OhHv03vo9FML1U3YrhB-9S44Qye7X8ISWHorsYajrmJ6lJy2NbVFc1ef50FvXvRoEOFG-Pn1A3_gHHoJh7CIrdjeTQWIW8tBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما رادار ایران را منهدم کردیم. آن‌ها هیچ راداری نداشتند؛ هنوز هم ندارند. همین چند شب پیش دوباره آن را منهدم کردیم. آن‌ها یک سیستم راداری جدید و خوب داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67216" target="_blank">📅 01:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67215">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82798a9488.mp4?token=QaKOTOI4nAbjShV6NwT34o7F2v0vrozw9XzU98qE59c9q9FOHpMUMC-uWFTTH1bebHzubJq7eK6VmZ3H8LUVIhN-HV1A8_Uk-JXaf-t_UVE7VmK2z-wDFXubqVbhcjSxWVVYXHerSoOSAmAXhO2dZ_JNuYRayjwZtvm3h3afB0T8j4SLeZTQT3R6v9v9CM0ex_NMArPMh4YzmuROa-ssnZQeyDmo3pazd5oZT8v-iClPLAuvwd1I3zi6NNpDDUMdHJoUqZEhXuseyPSsDrNYncEAzfJLBQ5UsRI5ILMf-zN7V5MfI1LpxTo0dB5jg2OJxNdyjYQHlbBL1eSKLuSkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82798a9488.mp4?token=QaKOTOI4nAbjShV6NwT34o7F2v0vrozw9XzU98qE59c9q9FOHpMUMC-uWFTTH1bebHzubJq7eK6VmZ3H8LUVIhN-HV1A8_Uk-JXaf-t_UVE7VmK2z-wDFXubqVbhcjSxWVVYXHerSoOSAmAXhO2dZ_JNuYRayjwZtvm3h3afB0T8j4SLeZTQT3R6v9v9CM0ex_NMArPMh4YzmuROa-ssnZQeyDmo3pazd5oZT8v-iClPLAuvwd1I3zi6NNpDDUMdHJoUqZEhXuseyPSsDrNYncEAzfJLBQ5UsRI5ILMf-zN7V5MfI1LpxTo0dB5jg2OJxNdyjYQHlbBL1eSKLuSkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آن‌ها را به طور کامل از نظر نظامی شکست دادیم. آن‌ها هنوز تعدادی موشک دارند. ما می‌توانیم آن‌ها را نیز نابود کنیم.
به نظر من، آن‌ها تقریباً به تمام خواسته‌های ما تن داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67215" target="_blank">📅 01:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0Dw-wKVO4AnYEwewJ3MSvZc56QQ3L7KCu30FqRz6lyGmTVwnPVGW2JHPOCpjVfY6ci_Y2x2RfkB6PFGw8aoqPUHlzeRIcFrePcqthndxBv5i4o52UpbmFChTIAS8ot6uygNi8Nn7MVnsXbYaAnoP9pNJkqP6LxjGQ8v4gjcG5xWHy4jSXMWVetOalA-kaHNsGKrlcoDkQd2IxiihD1PnenuoF96cQO55dhXOPU_mqGnT4nEygaGRkH4DBDrGzsrNgX3wBopOoJ269TnZ1Y0_n5MxPbbS3Y9zFWkCMQlZZRwLIeWUOWtKGnvJNcQaJsKalRRirWjNJg7fETiIeHm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZMtNU2hwlGuxyoj-ABPMq7zVrxaoBgSTNrLe0GVZTbrt59b9CSxZ7HJWSNI9VPxIHy9pTWPmYg3q2q4Qq3E_irZDvjrp2f3yG2jSteqHcm9Vu6utPDYTXM9oTpbWi9e0yUvXHn4MFYbDVEN-5_Z3d4ZHovJ9E5VWRBkqQ8heTx14RJ7AH_yNpcuSOTTRW0kamNiVWVz1oYnB32-Hw6T_S24yCCHtMVX0okMhX_fgXrwTdGgyptonA4oxkjhdlD_EheKDwUhnqX8xaVRzwePdIU03B33Bh8VMbT0Kj0FnT2DGcY3vETRLyEKQ3q8O1Va7A6har5xj8uC7XMtmnudKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ton4iR9a8UKItafoKM6GjEChOLLEKVArMU--7_Gsqj6aSR_o4bNBVSyRxFMPqBPDeIhPQ-4T-RzSsjUZ3u4adVkIRCaEa_emLsHsbpFrCDzLrjPuW0Gq0E43krEDxe0WqrESiUjOuaQ3u-VvTl9m5RlClEVqK5EDB_WM3836tQOsjZ9St6ekaqfrAEweIQbndhYVVYsD1f-OqemrYGSNjB1IV0io4RpbRJl_gDpSXhvJCZbnc1iAnmoMuqZXK9xzf4-1LOE_n6nTjfX5CSWIcIbQX5LlaAB8jHpP_SEG1SIdbhp1nMhYz5D7nPMJRlcAO9EucJ66X9UH_2Po_zNXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=V4_pPlQu2GzN-nvfqbttY2Fpc5SXf42f9M1q3N6v0CJfYwEeEgfQwv_olRdg5NLV-0NNmg84e9n6DWVsg4szp6H2dWLmDu5l5SnPp4ortJljSFGrPEHLsmVPWyv8UCYboHZo4A4XwfgO1z6uOC3EdeQFaGCLHvKJwRsGY0YBJH6zjW8W6OnPJHC-qBhHPVcVAT7LGYO8SpCA1YilGUDW7gfE4r59UJCOx2tEdfoqtv0I_73zZH-iATLr0M9vnk3PHSeWfx7Hx3edpFIy845bOEORhL93N1ckYBiRkzSnau7Fu5vCOjhcyhjdhf9OY-mpHZZ8_rJjpd9qDQ-hObEe2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=V4_pPlQu2GzN-nvfqbttY2Fpc5SXf42f9M1q3N6v0CJfYwEeEgfQwv_olRdg5NLV-0NNmg84e9n6DWVsg4szp6H2dWLmDu5l5SnPp4ortJljSFGrPEHLsmVPWyv8UCYboHZo4A4XwfgO1z6uOC3EdeQFaGCLHvKJwRsGY0YBJH6zjW8W6OnPJHC-qBhHPVcVAT7LGYO8SpCA1YilGUDW7gfE4r59UJCOx2tEdfoqtv0I_73zZH-iATLr0M9vnk3PHSeWfx7Hx3edpFIy845bOEORhL93N1ckYBiRkzSnau7Fu5vCOjhcyhjdhf9OY-mpHZZ8_rJjpd9qDQ-hObEe2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z6iIlz9SN4wGMYNfnZZpc1GObEpZScCXS4O3nppllmJDqmcheNA0tBP1NfFHMQVKUJfFJ0BvBtYI4PzzwbvNHCrJYKDKgLDt6EADJD6G1fMFPEcAph9m1Kgm6acUAwjoiYxjkIzFHY1GKxUYx1zMNzf8lfYbm3gPyCwbS01ioG6qWK4cpRUD-qF5jkMpFgkHcY_QPyJks16q-uxPfc71KJzwuIIK87vroikz_qU64PtadkyMzTFdoj2UIalp5j85-39l_7WbZoZGhQKBZUJfzkIJmfbhO0xX9dtSILvSA2VXzYBMmRKzcjNL5afeSlNO16tG4OPz-TIBarLQJ2IsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=GJX-3LB1_c5eHAEHXWJnYSzF6hKmFfyuDmXu20U1M-oXT98GIhrnQ1K4KATE5Qe0DvNUNGnJOuHnYNlOvkdnWMZPOk1z4rRiH00qN2zZY_eeK8Aksno1QZWpO673odqn6mdl6gAvH0NMSE_kIwR7JEE7XfU_UOV_uqEhs17OIR2MK0SDR7nZ-yEAEhvwsbhvQNuzRxgyTRzMC-v5HhlnQwql1fgIOR0MY-yJpqAOA899QKfffogE73LHcEUN8W5dWTcLQ6A5fnA-MKDKxjvgKkDw8mdXqLWgKHXejGfhzQSD8CvoDIwYRLBx05XqohO_cUhPHBPDqmT0_rFy7tlvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=GJX-3LB1_c5eHAEHXWJnYSzF6hKmFfyuDmXu20U1M-oXT98GIhrnQ1K4KATE5Qe0DvNUNGnJOuHnYNlOvkdnWMZPOk1z4rRiH00qN2zZY_eeK8Aksno1QZWpO673odqn6mdl6gAvH0NMSE_kIwR7JEE7XfU_UOV_uqEhs17OIR2MK0SDR7nZ-yEAEhvwsbhvQNuzRxgyTRzMC-v5HhlnQwql1fgIOR0MY-yJpqAOA899QKfffogE73LHcEUN8W5dWTcLQ6A5fnA-MKDKxjvgKkDw8mdXqLWgKHXejGfhzQSD8CvoDIwYRLBx05XqohO_cUhPHBPDqmT0_rFy7tlvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-dznyK3EuVesXqYCrFcoCqnIMdMdsj4TGNbH-xf4gMHW4kLj26hg6luT9HADDkhQvg__VcStjMJpnTFKT8htYP54p0GNKFdPF3OxvvBz6GCUCwj-prAUbf5o8mhNZdDnuO_JWQoxXztbAJxiI5uRKoFvksP8RVABMVCrPriZHmijUm5ggFwV4WpYG2HIzr39gCq4vVZI7oK3DmrkHlViH1IwmsF4BdGGPSd64bhn83rpw9qHIy7x3p8Ei93ZW1i3nXuI9ozQjXj7QibueOfXKg-0EZeUUDxS1lhHKnj6BJcrLh7pC9cMFOMssSjM5lqoMcR032fKdPZ6XGX5uSetg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=rGrCWW6mRurHvu2UAKFD1DlWIa3xoxKkIvC07YxvChacbZQme3YCOmCg9rWd3h755KwhrWTXWPncASJ9-jAhNkB1jfvtF3RJ3S9q0pWrqwxCgTqJJiJK0zlb-CE8D9ZEaSGo-RxtEanUU0O-JN1TzGo8oekb-kqV9t9LYyHDTI7nEoQ96dm4F4pIbUauX4ZxKdIkgpCh8SypTfjDpPRohJYQgNsJF1ZfSNPHTckq8zkZaJ0_mHeXR3UX_XCmPjEBA3MBugb8fHwNubhaa3_WDB-RPW69p_FQtzmCukNuCVXKep-9IKLHj-a_lcChak3Ap17X49YW3zYmPO9z7ywhrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=rGrCWW6mRurHvu2UAKFD1DlWIa3xoxKkIvC07YxvChacbZQme3YCOmCg9rWd3h755KwhrWTXWPncASJ9-jAhNkB1jfvtF3RJ3S9q0pWrqwxCgTqJJiJK0zlb-CE8D9ZEaSGo-RxtEanUU0O-JN1TzGo8oekb-kqV9t9LYyHDTI7nEoQ96dm4F4pIbUauX4ZxKdIkgpCh8SypTfjDpPRohJYQgNsJF1ZfSNPHTckq8zkZaJ0_mHeXR3UX_XCmPjEBA3MBugb8fHwNubhaa3_WDB-RPW69p_FQtzmCukNuCVXKep-9IKLHj-a_lcChak3Ap17X49YW3zYmPO9z7ywhrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-ozqWiyWzgkbq6QXq57qGGCC3o4BqBZL8vKrXRRYw_-6lKIu6MgejYBVdEpaABgRoR0smm499vQtcrmbBaoVsKxVgVpUGkBy_Uv-CPcIqyLrjxoAIhlUvSIL9AIoxT3550FfQdq2BWtbXX_b_EG_QTItRw9aV2y8LamNTDK3Rw1Pfny1PqZXjHWo3hSer_2a-LHwiXuHIjIH0Utjl-oD2yjM1V5AU3lCNSr2TUbFHnPFBuZg0G9mBGHb1r7yaI4ZWL-wq5dE0KPaUTsGGVu_TbQv9tYDbUAV_MVEt33rNulbzeNiPtHaGaWvvxa4veGmxj255NbanBiI3At-uQS5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijiQT-mYMX5khAu9aMxJwg6AmgppCqANU7L5n2A4QanhiHn6XFLNRo1tnR6ttzVGiE9vSoG6AqLHNioG1proJVlE0IAa64GMFZ6feAGGCDJHT1VgPTPNAjgq9XkGjDAU2SFVkW1ohkqQc2-iIIzYA-GoeN2l-iTClzsTj6azfNz6R-ArwmN4L3ngHJE1vbBsAG29GSeUP2xOsInZ3Idg5dbcD-bTdLYGwCTVY45O6Yj2UFPeSodHpPj5sMYgUa7ddoj3ijtfQ07Lf8gKf0xS1Glzy993IIQdBTtOhhQq6Ud8BMWNVvpmBnVX9y93LDOzptpW7pBQPIslIyq72XZpcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seWUuOe5RIAiDYj4L2BK8ZrBEbzcnUnXRylLlaAeKd3QA0bsSEcSkuuruK9UfPV4QeSeTAtyE3hGF-6IWMnSNXDBGS5-M6uFVMxyjPoT9uVuCPjneuRp1JmK8ygea9a8Zs4yMjADYlGm5d6kfhhoajrlsBnbm6Has7WOoYNTP4FTzVAkMRCofiwnPdS7qsAzYVjbEzD6Xd7-zT_tAoVe5GlnFmx4YvSYkbu2btybMgtSJpVBJK25gJs9W4v-rdj3paELY3huAvE6Jqvdg3sO0i0nQGe2U48MosFy0pIDZY1D3lSJKcJcXPUJAoinCsNLrab_joIxz7JhOYonLKkX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL6iOyQ4X68pDHLNMNFChVdAJL72r3HdxYBP54k-k4oY7B3ouF-Vq7b1GKCcA2IQNVGBhyNEFBYENHV5-oVUBw24iHwFEepp57T93PcyNv40mI79OSPuTHyhgA4sKPhwir3Sz9g6d57jh73oanBBEecNixbdlegcTeVC7uqOv69RkUrSx7bz-ugQr5cbmP9nevzbuOSO5wXXJzQJGTifm_2pNPSZaaZF62-FoQjcoqLRQS1aeaK7LCeJdyfDbQKNErpCBLPYjdLe73Rrn1U0iOwICUkb9qF-J6VypW9beureTIRInvPFkmnp8veOwMg3Z8gqzASblynQKOeQRwAw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX-C0CXRXQTzCqR32nBH-RSVVnrxOoPDbto7FnSi0qfR_yspCucpXGsizCd1OU81Az9bt_-ESFQ7FvVXjfZb6J5vapEJmEFKX1PiAwwwxD1PFmsbBWDilvxNWVsi5pNh1q20RKlqVxC83ms-3dJ3rkL8mYYKhITqZPReF6kMCIZN0k7Yzsd_DpNUHxjopOw_fh4MXn4_ESO-a7iSBjyVVkwQVTiRPf0vTIexrthpc8AX1EBufQKcy9ZF5DnOpHlh-Zpk8kP116whPofGu4JW4P9KJ6wS7XZbbeSLl-eqRzudnnyA-IhGHmKV4eAVVrhEfHBAtLt_D6D4Wy1Nazm7Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=UWs-6an9WWH9ZSCODo8IQ4DFhtNNYOHFJ-F8yG8oBpmbVBcGCs3lUPIIFpPVt8hO6IExL0w7Up8rKBAlgu3oQH9wJQcP5r-vYIxyWW_xq7abjtqWEe0zNV_yO6ALSKB31qh99NcMSPyrwv58LyTIAKfu7_HdL5oXaxMheWv_OkF7SQ070Szrjj2vmwi-I03t7DcNvwVJo0Zt6gh2ZjmI77f3XS1nRSPwo1liEswcWHViKMYBJ5i1aFRNSRzCRi4QWw285FiXQuS7hrhl21ctdYDqBKTl869llDsBbt9lXY5zRjlsvCAKE9OUf3gBbjDfLcVFmNGmyUs-3Wb59wVMug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=UWs-6an9WWH9ZSCODo8IQ4DFhtNNYOHFJ-F8yG8oBpmbVBcGCs3lUPIIFpPVt8hO6IExL0w7Up8rKBAlgu3oQH9wJQcP5r-vYIxyWW_xq7abjtqWEe0zNV_yO6ALSKB31qh99NcMSPyrwv58LyTIAKfu7_HdL5oXaxMheWv_OkF7SQ070Szrjj2vmwi-I03t7DcNvwVJo0Zt6gh2ZjmI77f3XS1nRSPwo1liEswcWHViKMYBJ5i1aFRNSRzCRi4QWw285FiXQuS7hrhl21ctdYDqBKTl869llDsBbt9lXY5zRjlsvCAKE9OUf3gBbjDfLcVFmNGmyUs-3Wb59wVMug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=rbXk0O05s_5K1J9Iey_mQtEmzGK3h_dL7ea_UWC5-aaOFT0OtRMaBFkGP_RRcI2BhKESofORw03HrjQ3LSGykTz8WrlkIHDPfrFteHuMRdslNZ8qP-WrahVkwglBSq6LUTDeHfgrc-xVAF3iWY25ZDSRohFZ1ZtfCmCtJgGk_09WAZWvnkcBk6XZWRrjvLiEO20Wlid7WOaSYKZKICEI_k0g9qM96LBzHP1I8JjYuCA5AEKM8SCaffj4xuxWj5yfUi8iNSnrnHb9Ilkfs1-XZNxabhJAqW3-STmkNyKQb_tJ2NiagmwIUCf_ENYD162hbxVPHnCfLCpJoMdW9MsQ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=rbXk0O05s_5K1J9Iey_mQtEmzGK3h_dL7ea_UWC5-aaOFT0OtRMaBFkGP_RRcI2BhKESofORw03HrjQ3LSGykTz8WrlkIHDPfrFteHuMRdslNZ8qP-WrahVkwglBSq6LUTDeHfgrc-xVAF3iWY25ZDSRohFZ1ZtfCmCtJgGk_09WAZWvnkcBk6XZWRrjvLiEO20Wlid7WOaSYKZKICEI_k0g9qM96LBzHP1I8JjYuCA5AEKM8SCaffj4xuxWj5yfUi8iNSnrnHb9Ilkfs1-XZNxabhJAqW3-STmkNyKQb_tJ2NiagmwIUCf_ENYD162hbxVPHnCfLCpJoMdW9MsQ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=hKGBmeSBBA5cjTREOJwwi9QSTKQjWUbcVvjxuzQ-8Ds6uRpQQxk4Tbw1Xt1lX0Y0HFLb5Tu19TsjXlbPBZURTWAW-O3zTWOqM79E2DLeqdGKLYVwqzZJ3D599ANHtKElqBzSoMAIaZghHbEkPDlKCvv5v2BxZx1nLDQS3_ArFwiYq4qbBu_0vAgkqP1XnSa-EkNP5gYiee8zCr1LbdDDOBS-ceCimUVokS5TVyD3s0Y7gZXJ_JEvkhqOK3Zll7CjO5XLp_zFb8yLqL1M30TlRGwXy4GZcYNghOhc5BgUVVyV71-jqkGPkR46fVcuAPEUKbIiA5iXWdAbWdeB1ckcRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=hKGBmeSBBA5cjTREOJwwi9QSTKQjWUbcVvjxuzQ-8Ds6uRpQQxk4Tbw1Xt1lX0Y0HFLb5Tu19TsjXlbPBZURTWAW-O3zTWOqM79E2DLeqdGKLYVwqzZJ3D599ANHtKElqBzSoMAIaZghHbEkPDlKCvv5v2BxZx1nLDQS3_ArFwiYq4qbBu_0vAgkqP1XnSa-EkNP5gYiee8zCr1LbdDDOBS-ceCimUVokS5TVyD3s0Y7gZXJ_JEvkhqOK3Zll7CjO5XLp_zFb8yLqL1M30TlRGwXy4GZcYNghOhc5BgUVVyV71-jqkGPkR46fVcuAPEUKbIiA5iXWdAbWdeB1ckcRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQPucac84-TxV3yrKuSWGnuo3WgVTod4VlvizW6Co9q5xYZ0-bl2Z6Uf9SzaiW-DXVXkT7ayh3eEj-S0bq3CL6hIRepgeIgERGpVdcuYi3QST2eKXjecVuw2ZY1CpcETqOHZzHsp8wANf2jPYrLJM25yJgBaFi237vTnAfr_gSpy-Rl6zy5fj6JPmW_JERiRNnmCqjx1AZAyHz_uRCROgzJaqNEvrrCBe4Y0IaM9X30oH4E3UqVvcRBVbeyAA6wm6XIUn0RsiU4UUvQK53QePyCTDEI3ZD_J2egfmDw-bqQloIIbeffobjdoip3XMqWP5rDF0nK5SVs3SWwHWbdK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UcAqepefHrKzgWk7TKwdXb5lu5Vmd646YaoX-9rxH7GFtQYG3vM--a0b4ZI4zhgb2Egai1iwuPyHarA5vUUociOtD8wPVOjEETaXDemeIeLIO4eZPKmJMx10vtNWN-a-IatQZW2j-Gx3b4LfS51EUrAcfGQ39lvCJqqXAyZJ1zjxux4mJvGl3qJabUg8vQJee6AuUNfA0qfQvGYfqosl5tFs4i70nj-aZNUHrRuePQKkDQAI-WZG1hgh0KLStCqPs0SREy4aXLiJFg-hoos_4iRsMETJ1kA5fMMAgzQWRMS8EPAEP5Z6qdytjdhsWqJM2bSNECw7FMo2vhdJBkp6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEtuD1cB2w5UZvIMBL_BuEq4kj8YMqbbawLa05oiRJRiWrVTCIFdsDzRupo4X_qTNmTQGYUJK6noHMn4Who83daNcHLGxrpG5sX4UpMH4mRpyjYVfH-EF7T-F1uirPgtMq_Mvds4uDCXuoSNLSQ3ODrhMH44b7BQ3dN8rWcLjXma7_pnRvlaOD-qNC_g4IKE6N2khPShnyGddOLTxz01U8UVklaoRgO4X372HpyP0TeJ7mvC2cbS3h094ijk7CYB1vBQAo-2cMu1aHztSl1AFf0z1x3ARBgduHpP9XfR4aPhsxgi343-DDwbnR7R5gRx94dilMnf7UatLXKTEwy8ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=FkfYjnIoT6PjUbccpt5yWBjgRUYI4H-9GlnCJVRRxKK1apFOnLO1mfKcWo1qObRj7_f9m_dkxDDjhp3krmgXU_kSeZkM53FCV4n_OKbtSp9DBfzwnresLVDGFrzqcHUyYDFKgDUJ22i-78xlfU4rrFs9US1awawdk7AsAUakFSygSgbG-fCDjF56fse8YLFbF_f1VT5Z4meEX0fHEcrBuFfC6wqRfc71Iga4s3jYQkugwlxQl_bcJVx54ZitlFVMHMFNwrcHooMkV0ItLk6SHXaVs64XICvigtdk4lhpjO7PfBM31UhAlVz1bpljvjngscfY1llNNxGEci58nKzNGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=FkfYjnIoT6PjUbccpt5yWBjgRUYI4H-9GlnCJVRRxKK1apFOnLO1mfKcWo1qObRj7_f9m_dkxDDjhp3krmgXU_kSeZkM53FCV4n_OKbtSp9DBfzwnresLVDGFrzqcHUyYDFKgDUJ22i-78xlfU4rrFs9US1awawdk7AsAUakFSygSgbG-fCDjF56fse8YLFbF_f1VT5Z4meEX0fHEcrBuFfC6wqRfc71Iga4s3jYQkugwlxQl_bcJVx54ZitlFVMHMFNwrcHooMkV0ItLk6SHXaVs64XICvigtdk4lhpjO7PfBM31UhAlVz1bpljvjngscfY1llNNxGEci58nKzNGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=C2YRQDBDoOfm20zoZO_-KsnjBsLTBwIlYoIhNdjcsPjada7kW-2l7-4apNdkJMHOZXwvmpk0XfqmVNrqr_WCOvD9_NPGd1kBDXLZmoNuo_FRIr2M8CzL4VkU3GSJ1c4musMlTrDwF6i4dF-ReWOEoHIwzxz8UoSHOu2ei2VIvMFj1lZcYUR28DCbXbZMGx9Qqg1ET_AfHcyUHexVL8-lqyP5wWZdgvovUKry5NvI1udKpnmBmNjptjLf4O1x_aDCvj4w55-otxI3dsD35X2eaPF8vgK_YP6hqd0FKP3yf4wjEsT5NjaqxtnmIzQ61ABC8vhBuc4cL0xisyg5hcYc1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=C2YRQDBDoOfm20zoZO_-KsnjBsLTBwIlYoIhNdjcsPjada7kW-2l7-4apNdkJMHOZXwvmpk0XfqmVNrqr_WCOvD9_NPGd1kBDXLZmoNuo_FRIr2M8CzL4VkU3GSJ1c4musMlTrDwF6i4dF-ReWOEoHIwzxz8UoSHOu2ei2VIvMFj1lZcYUR28DCbXbZMGx9Qqg1ET_AfHcyUHexVL8-lqyP5wWZdgvovUKry5NvI1udKpnmBmNjptjLf4O1x_aDCvj4w55-otxI3dsD35X2eaPF8vgK_YP6hqd0FKP3yf4wjEsT5NjaqxtnmIzQ61ABC8vhBuc4cL0xisyg5hcYc1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Gb1MLz8aphoxt6w2tksdJV1MlWx73D8xw0tCcL1VmMEw41WLuBXudBHv0KKVjLjbl1MKq4GWQnhItfPl-unq_cW7x9q3EVmxYTgz--4Pkf1LCmPbMPOxubvwslaeqv40o8O6oBkj4uiUSUTwcjgN6Kb1mz46U7AgW8VjF8Cq4Pn_b2c2K9YQUVfx1ABd9bWIZApfjDE7XW0S7sRZi-Dj64jckpu6vt4NBAXFhNt6e1iAfMBqvFovnWyqHdDfzuc_rk1vjYcQD8GX32HZGoi0HYCW23h_G5I-aHiEkewfQUiVnKG9g1Ki6VosRRU7NghayOJzGCVR-AnAZWq7ViR4Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Gb1MLz8aphoxt6w2tksdJV1MlWx73D8xw0tCcL1VmMEw41WLuBXudBHv0KKVjLjbl1MKq4GWQnhItfPl-unq_cW7x9q3EVmxYTgz--4Pkf1LCmPbMPOxubvwslaeqv40o8O6oBkj4uiUSUTwcjgN6Kb1mz46U7AgW8VjF8Cq4Pn_b2c2K9YQUVfx1ABd9bWIZApfjDE7XW0S7sRZi-Dj64jckpu6vt4NBAXFhNt6e1iAfMBqvFovnWyqHdDfzuc_rk1vjYcQD8GX32HZGoi0HYCW23h_G5I-aHiEkewfQUiVnKG9g1Ki6VosRRU7NghayOJzGCVR-AnAZWq7ViR4Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=E4g28vFWbyebK9zjgiDg6N7KUXqD-_AuiP7mZx9cGqcof97N-t4sKWE8XloZkbyBWhdXBwLVeGJ6ONhZaSJCAJcesHF_eTyg5vslGc1GlKmaVKofZWXf_LTlnx56dVagMBdNzVv-JOp9hQYCHS62Oy3kWbEBbCWSgtg6dLXlafPimq2s95Av5TfsJFq1GhR817TCvkmSTeEJW7IVCR2OdhEPvzSZE4mst304ghiXKOKwK8W-M_P6KkzLogcI33tKrZG4YATiSK8iU9rbgWc_orGIb7XWrZ85jdxmVgEQmzVDYW2dA__A7AyFTh3aF1QYgose7LtN1NXEJlvWERWkznQ9PMMtwEDQh7RHAXn7zh3Ixk2nNjpUZOMPe-uWNDn_Wydx-cSTNf9dzRRUGUcsGnJPyScpXOgfLo1uXJkZfXIBOL7oDvne0OV8b0tDLeM_TeLIsuxV-vYPiOqMqiW3HsM2wj_ugrRDyDh_yM7DVPNg-bY76qmzQEB0KSdEB9OMbUXL4B8Cgm5HsQq_8-ioTTtlaCtKcyTgN9KK5W0CYa_aWrBY-Z1QaM4T6KCvdgE6UWia0xi9rTPVKq9dlpKfdKBPeAGtS8xbNYht7yKtfjberRDw1yUYzgnJ6syHGHYf5zVrccOG2Yup60bEuPlwiSNvQRkeR2b9Dv8xf_8esno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=E4g28vFWbyebK9zjgiDg6N7KUXqD-_AuiP7mZx9cGqcof97N-t4sKWE8XloZkbyBWhdXBwLVeGJ6ONhZaSJCAJcesHF_eTyg5vslGc1GlKmaVKofZWXf_LTlnx56dVagMBdNzVv-JOp9hQYCHS62Oy3kWbEBbCWSgtg6dLXlafPimq2s95Av5TfsJFq1GhR817TCvkmSTeEJW7IVCR2OdhEPvzSZE4mst304ghiXKOKwK8W-M_P6KkzLogcI33tKrZG4YATiSK8iU9rbgWc_orGIb7XWrZ85jdxmVgEQmzVDYW2dA__A7AyFTh3aF1QYgose7LtN1NXEJlvWERWkznQ9PMMtwEDQh7RHAXn7zh3Ixk2nNjpUZOMPe-uWNDn_Wydx-cSTNf9dzRRUGUcsGnJPyScpXOgfLo1uXJkZfXIBOL7oDvne0OV8b0tDLeM_TeLIsuxV-vYPiOqMqiW3HsM2wj_ugrRDyDh_yM7DVPNg-bY76qmzQEB0KSdEB9OMbUXL4B8Cgm5HsQq_8-ioTTtlaCtKcyTgN9KK5W0CYa_aWrBY-Z1QaM4T6KCvdgE6UWia0xi9rTPVKq9dlpKfdKBPeAGtS8xbNYht7yKtfjberRDw1yUYzgnJ6syHGHYf5zVrccOG2Yup60bEuPlwiSNvQRkeR2b9Dv8xf_8esno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=u4oBO8-abqn1T3pm_43nvSad1C7uqgjjzKTyEp1YFciR_68g6tmrNKQMBwyF-wu3iKtAJciyCfDyBRj0YczGGShqsbZ5X5wo8jn3U5rDg48GUGOgLiR0B8d8c3m8PcKLXPz0xzS4LQOSBYAgFDjM2eh24ugQLiH-o6K47eNipZWWFhxOS_dkbec5OsWxBytdubcy91GdquB385nhAsJNBh3bvMMm5-mNFSpKeVBA-htSOiCeYmfNv6A-_LHmtKmKxl8m1P1yWljvpvmWuiLNxblh8N1YTg-SM4OM1_-5MLZwbRcT-uSdCvY-cQ38zPBejWU9w4pIi3ZxDv_IiMoXHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=u4oBO8-abqn1T3pm_43nvSad1C7uqgjjzKTyEp1YFciR_68g6tmrNKQMBwyF-wu3iKtAJciyCfDyBRj0YczGGShqsbZ5X5wo8jn3U5rDg48GUGOgLiR0B8d8c3m8PcKLXPz0xzS4LQOSBYAgFDjM2eh24ugQLiH-o6K47eNipZWWFhxOS_dkbec5OsWxBytdubcy91GdquB385nhAsJNBh3bvMMm5-mNFSpKeVBA-htSOiCeYmfNv6A-_LHmtKmKxl8m1P1yWljvpvmWuiLNxblh8N1YTg-SM4OM1_-5MLZwbRcT-uSdCvY-cQ38zPBejWU9w4pIi3ZxDv_IiMoXHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XvfDGE4Xc0DlG8WTOXCGjR8GFpCz6mboJ6h6_hlEbI6AKV8uvWH-e820ibwjjENxQMeG8Jd4LK4-8VNmQZT93ZoyTTEHqAm8N4K2D9_oBHNTw_mxa05ggHKCiD2GV8pTunWbgwwsfYqa3YKPw25ElUOzp0bU4iB2TGzEybdnUXXHa5EUvdH9O40SCJ7eABsOhYX7ZjLsPpzXl81D2WmHrdZZejDhPa1lFPHiKzj7--M72mVnlDCNWe-5yZjdDIZLd9aI3U9Frr7RTEU8PeuChuAdypUJt8k_wiMNzJNYelEfcrZwiABvZy1of0cxwnZj8V-_HMXjO3jBoBIRmY1U0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XvfDGE4Xc0DlG8WTOXCGjR8GFpCz6mboJ6h6_hlEbI6AKV8uvWH-e820ibwjjENxQMeG8Jd4LK4-8VNmQZT93ZoyTTEHqAm8N4K2D9_oBHNTw_mxa05ggHKCiD2GV8pTunWbgwwsfYqa3YKPw25ElUOzp0bU4iB2TGzEybdnUXXHa5EUvdH9O40SCJ7eABsOhYX7ZjLsPpzXl81D2WmHrdZZejDhPa1lFPHiKzj7--M72mVnlDCNWe-5yZjdDIZLd9aI3U9Frr7RTEU8PeuChuAdypUJt8k_wiMNzJNYelEfcrZwiABvZy1of0cxwnZj8V-_HMXjO3jBoBIRmY1U0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-w1GrAC3v47vODycqVFKHPDIHNFrGw3jG2Ti3bGJSPOIIxKbxrNP_qSfKAomkOqEJ81iUKhxXJw-oygdGZhfmiV0OAv-QZIn-MnLdKCxRzr67xRlo2S2lZbcEsMtjuG1n1Bk40e2dziCMbubrHUk4pcggM8OA7w7SCB-p_iuQ2Wget_LiCUDi_r3PJ4Uau2JMIknEtftd6YVaCtbFZWeRQXCC2luVOHIvMKCpBTq5RlG1N1ntlbabOpvRiHgTJVlBaQlInbSO2RcrHxvCdz1F4pobQjHWB-iKaAE2iDFrDTFf_svhkBNJu0CPMfwhMHNWHerZTaPcPThofqJU5lNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vT8WR_Js2Y-T7VGqdHjLfj1UUq8poKFTka_pxPZgWA-i4Ygel7bPryw25F3rWoPanDTEAvE61EUHH-9YTxesBiooDwPCirSW78IUyeazf3xJet7NjQRNtmOlNhhq9jsZLNREJvb1GM_FW3VEH0ngWPFlO8iucMou01LInliXx5fAcvM2U64Z49zwOmls-istiMMM5jXUVoKhOzTFUODEZlBI3SP-WYDIBCYZDd2FSvkRe7rfRBOZFvT-sJpzsvpaBdom03eRn9-3QzF0wUueCGd4ES29ylNZxRr0mbazbbORGIXNjG0ift7023OzmuLOhTszFIMha7910YBXMTmaMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=BPD5VRWfRvVO4QSLmYsYgeBZRFOhmu5n4_sEhgb7gDf6KZsFVpTp7NSAoaONQn6sqUNefdjhc5-BxC2v0-Bcm_mXjwn988Zch6dTmJy-0-ziHlSGNcIg8O64ffGcQ0n2cCn_A1XijliUr8FOME80YVksffjxWO9FlG_hKzXGi4QGngU-XwmA66ZO-zoNpm5tK1bYxKkR343gGf2FNfrGNzhi5Vc3-rcHn_hzsY4SHvzG8bdePCRDYNT8ZH2mkclJP7cfRW29sEH-6mssNFK6MlCcQ_BamN6aaeHGzqTNUyUhFUi5ISrX2IMgqLNVw4rQV4i9hChX8PBFTiQpDCMDdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=BPD5VRWfRvVO4QSLmYsYgeBZRFOhmu5n4_sEhgb7gDf6KZsFVpTp7NSAoaONQn6sqUNefdjhc5-BxC2v0-Bcm_mXjwn988Zch6dTmJy-0-ziHlSGNcIg8O64ffGcQ0n2cCn_A1XijliUr8FOME80YVksffjxWO9FlG_hKzXGi4QGngU-XwmA66ZO-zoNpm5tK1bYxKkR343gGf2FNfrGNzhi5Vc3-rcHn_hzsY4SHvzG8bdePCRDYNT8ZH2mkclJP7cfRW29sEH-6mssNFK6MlCcQ_BamN6aaeHGzqTNUyUhFUi5ISrX2IMgqLNVw4rQV4i9hChX8PBFTiQpDCMDdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=QqLONe7-rAddD9OzN3Q1mNltK1n1tRgiFFcrvloWu228NmSQ6U5iEEfFPC8GSzceLs9-O1PrXHWuzNbjBS2KpmacAMBivzIwbBfSvHcgG3TTmDARniS8X9sYmN3zav-XxOMxSy_Inmnjeoh4ZzkWdl161a-1UPydUZIZIjuY5qRiO-eapUfTqx_2TzGrxQzFD7tPDDpGA8s4ilixREPEFg_8W2GpPqb3lJw0x88r1wDy8SyHvoup8DNqSBe14bVDD00U0qPluDiiRHxhI1avcGLYIjfwvsYXbGgw-n0sEXatw3d6GqI4M5cWmdsjUayuajE6-2d-c389VCBmBlKyfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=QqLONe7-rAddD9OzN3Q1mNltK1n1tRgiFFcrvloWu228NmSQ6U5iEEfFPC8GSzceLs9-O1PrXHWuzNbjBS2KpmacAMBivzIwbBfSvHcgG3TTmDARniS8X9sYmN3zav-XxOMxSy_Inmnjeoh4ZzkWdl161a-1UPydUZIZIjuY5qRiO-eapUfTqx_2TzGrxQzFD7tPDDpGA8s4ilixREPEFg_8W2GpPqb3lJw0x88r1wDy8SyHvoup8DNqSBe14bVDD00U0qPluDiiRHxhI1avcGLYIjfwvsYXbGgw-n0sEXatw3d6GqI4M5cWmdsjUayuajE6-2d-c389VCBmBlKyfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=XGwsCbqCp19iqKlOrxRYbzU5YIfdZojtAVCHh0aZfDaqS2zYtMsF4LKJS99Ru00uQLrHt8CrBtlUDRVLq9KGb3qL0WdfZwezOhW_olJ31y7iWykAjXIsrytPaPIAHJcmm-ub1ttLn9kkN0y9nLwy50kVJZUSgu1qpq3ADjn_2sf9debo57JkwBrEySmfUjH-aCZQrv7k8Letx8AknBQ8YaxUsHlXEPH7qAsQ0zFjjHbewE9I9PK2V1f1Uv4LJZeLq9E85Jw9Dq2KVBlJotvc7v2nd3TqJjFgRgU8gvivkM-y8-itkD1vosQmKYaEzM-v6exeSJOAVVkumJIZCMpIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=XGwsCbqCp19iqKlOrxRYbzU5YIfdZojtAVCHh0aZfDaqS2zYtMsF4LKJS99Ru00uQLrHt8CrBtlUDRVLq9KGb3qL0WdfZwezOhW_olJ31y7iWykAjXIsrytPaPIAHJcmm-ub1ttLn9kkN0y9nLwy50kVJZUSgu1qpq3ADjn_2sf9debo57JkwBrEySmfUjH-aCZQrv7k8Letx8AknBQ8YaxUsHlXEPH7qAsQ0zFjjHbewE9I9PK2V1f1Uv4LJZeLq9E85Jw9Dq2KVBlJotvc7v2nd3TqJjFgRgU8gvivkM-y8-itkD1vosQmKYaEzM-v6exeSJOAVVkumJIZCMpIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvWISy_vaGy_gJiLLBFQo-6wtxAvk8wemoSsHwJq4T_FJyJwUT5bYG4F9BXglNQrgbFqdE5rB7DrSLLURXJsQPzC2ScMFwg8VRhoepMIX5ZJLuqo5yO74dSdJJcDopppAZHVcVgInrhCh48Pwc-LUVN6ChdhcznRxjdsa3wd10eYR-ZdMChybfx_AlsKLPT_RauPzCZSAUPdri3IXq6ReE23QL6sKl7KS4e4m3vNaOoKFhT7waMr4jQDwiXGe9zHM1ziJXLW3_qnWkDX4EvTL_9-GTjrhPSaD2w8FinYk4kxIqJtUmzOSpdjCRcZuU3vOn5aWZH_Ea5BIP2XJNU5VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=hCuHO1rDGPzx1LVU5-eTb4nRIzGN5U-Jl4szdLAfaIVOEzS6uBMbk1JNo5PlDCo-i7zr4TldMTfjjyg0-HQJqkjVQ4-qvpwWcYPg0Lisihz4xZN9aez6FRp43EAvE0gn3C0FocG1sTDCBJvI2VlbFGSRCF7D4S2yuJSszDyuBX0_ptzvYPFoxliTgspnJhl7faN8vz0Gcuvzh7qO9WVjOcb_FL1YthxC4y1aZwO9CNg-i5FvYR5qP7QfwN6EJ9Xidz_25KTcDTzt39UxcucB7HFKmotuGDKDyAZdCW8jQlLLEv7_EZezRT6Ab8YvrAoaKLtwqTiAi6dbtQT294kOGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=hCuHO1rDGPzx1LVU5-eTb4nRIzGN5U-Jl4szdLAfaIVOEzS6uBMbk1JNo5PlDCo-i7zr4TldMTfjjyg0-HQJqkjVQ4-qvpwWcYPg0Lisihz4xZN9aez6FRp43EAvE0gn3C0FocG1sTDCBJvI2VlbFGSRCF7D4S2yuJSszDyuBX0_ptzvYPFoxliTgspnJhl7faN8vz0Gcuvzh7qO9WVjOcb_FL1YthxC4y1aZwO9CNg-i5FvYR5qP7QfwN6EJ9Xidz_25KTcDTzt39UxcucB7HFKmotuGDKDyAZdCW8jQlLLEv7_EZezRT6Ab8YvrAoaKLtwqTiAi6dbtQT294kOGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=NQbskziXFo7ZCfWvLGH_PI97XhudIj_f5_1sAXF5L1SyuoQ_mNHLXoPTZ1dFE3UwJ3uK01sX3uu14ovN8tzc1m0CKX_VKkQypD4kvwGlFSdc-qI4z7sXWipUU6vq1pZjVdisd1a9I1e6qMdlH0a4H3_25SXFkrTq0VgojiYZAzlHaFC4MA2R4v75Hy_tfqcMGA7srE_bospLaOL4uDK7ZPgkdyP_XUtdPd2A1_eO2b8avGx_pXRDykguj8fqhuuYGyhRlcOipxv3APBMqEa63OqCD_xoFsMF4PBrS_rmzudioBVdFrmpAK0oZbq1BbroXCnCqTxUJs2rvRD0E8s4wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=NQbskziXFo7ZCfWvLGH_PI97XhudIj_f5_1sAXF5L1SyuoQ_mNHLXoPTZ1dFE3UwJ3uK01sX3uu14ovN8tzc1m0CKX_VKkQypD4kvwGlFSdc-qI4z7sXWipUU6vq1pZjVdisd1a9I1e6qMdlH0a4H3_25SXFkrTq0VgojiYZAzlHaFC4MA2R4v75Hy_tfqcMGA7srE_bospLaOL4uDK7ZPgkdyP_XUtdPd2A1_eO2b8avGx_pXRDykguj8fqhuuYGyhRlcOipxv3APBMqEa63OqCD_xoFsMF4PBrS_rmzudioBVdFrmpAK0oZbq1BbroXCnCqTxUJs2rvRD0E8s4wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=DRYUNxj0IAWxed_m0rNKRNcpow-hZE9xm2clxxBdMAMrvYrfULNJoLXPjY-ZrD1mr-m0ylhaCAqyjD63syo87otXVqevDSxJtQaVQua4VktZ27fMb0FoQEyDadxToYIvvvSDf4wyHYuCc5n_AUUhI4AvyMLg6TfftxDfgXecn5b2Go34cxMC87dsLc7cC9c46hdF1t7fo1JXG57Hrt4UztGFp10fNuEhypW7tkt_vkFAY9Ro47YddEzPeCbO8OnVPiChwkb-uA7qBIISdQE-_G_GsSw0sb1moSRub_OrdHpNFTgpQiD85U0Ed-AbKSIvWFz7pvN-1sA4d96F5e6Yvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=DRYUNxj0IAWxed_m0rNKRNcpow-hZE9xm2clxxBdMAMrvYrfULNJoLXPjY-ZrD1mr-m0ylhaCAqyjD63syo87otXVqevDSxJtQaVQua4VktZ27fMb0FoQEyDadxToYIvvvSDf4wyHYuCc5n_AUUhI4AvyMLg6TfftxDfgXecn5b2Go34cxMC87dsLc7cC9c46hdF1t7fo1JXG57Hrt4UztGFp10fNuEhypW7tkt_vkFAY9Ro47YddEzPeCbO8OnVPiChwkb-uA7qBIISdQE-_G_GsSw0sb1moSRub_OrdHpNFTgpQiD85U0Ed-AbKSIvWFz7pvN-1sA4d96F5e6Yvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=OxIHXcVz245csP9d3MfgZesn9QtkhlA9WibJbtkp0Z7GRQeN4fWspUGGYlnIYdAm2yFZhrC33QgPIJB6HKWa355ucTcZGGOD72c9YvBeNUSf_8QOTdivvYEEb7qVbHwhmUlfr_RRxxSYh5tkvzGGKdn7DvFA3EcqIHekj8Z-cdhua5P0kFyOyXK-DzL2973UZtujZixYvolECZl1y_RHjaTU8PUdgHaO_efuiVe-8kmAF1hFJ9hYKKyBv6_AVQv-QuSJrZHiyr0BoKzDJxAiamp780X07O9cx0zGiWUyEffKZu47jryu7UavahrCQVNW_Yp8HXsG2UXbd0-Iv2Inrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=OxIHXcVz245csP9d3MfgZesn9QtkhlA9WibJbtkp0Z7GRQeN4fWspUGGYlnIYdAm2yFZhrC33QgPIJB6HKWa355ucTcZGGOD72c9YvBeNUSf_8QOTdivvYEEb7qVbHwhmUlfr_RRxxSYh5tkvzGGKdn7DvFA3EcqIHekj8Z-cdhua5P0kFyOyXK-DzL2973UZtujZixYvolECZl1y_RHjaTU8PUdgHaO_efuiVe-8kmAF1hFJ9hYKKyBv6_AVQv-QuSJrZHiyr0BoKzDJxAiamp780X07O9cx0zGiWUyEffKZu47jryu7UavahrCQVNW_Yp8HXsG2UXbd0-Iv2Inrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=odlZbhmF-BmJ8_ntvS5wH7oLVdUyPkUYBVLcaXLVKIRlQBOJ9_XOjqpCSWE2fb5-j95zZh6Lh1dF0c7Q9hYfYDRMezn91iILhlrZxc56B56Wpma1fszltyHd6scWv3_FHj9K0wf_RcrPK0Ay1u2Mnm05fKc7L8eN9Eyoh4mzQYKPuNgLwtoWbbpN25MxFQPWTBSmwgxzpuNM3DV90KiZHCB5Qfpw13UpTcxYBlxrgFLdugR2X_I0Dp8zfMPWnjdmXLNMRZkPKntc_Jgxg_XE1q_-qtnXZm6Re8RHWaSfn7tMjUrgQ_A__pMbYfexGuKS-Vny9lHQJA_WvbPEe4SLog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=odlZbhmF-BmJ8_ntvS5wH7oLVdUyPkUYBVLcaXLVKIRlQBOJ9_XOjqpCSWE2fb5-j95zZh6Lh1dF0c7Q9hYfYDRMezn91iILhlrZxc56B56Wpma1fszltyHd6scWv3_FHj9K0wf_RcrPK0Ay1u2Mnm05fKc7L8eN9Eyoh4mzQYKPuNgLwtoWbbpN25MxFQPWTBSmwgxzpuNM3DV90KiZHCB5Qfpw13UpTcxYBlxrgFLdugR2X_I0Dp8zfMPWnjdmXLNMRZkPKntc_Jgxg_XE1q_-qtnXZm6Re8RHWaSfn7tMjUrgQ_A__pMbYfexGuKS-Vny9lHQJA_WvbPEe4SLog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=sRNqF5hV4b6Elr1D4uJ2IynpEH07B1oeHeBomf_v3V0qb1qPbukUJ0mHlSbHStx9Gp5JnXr7XFwT808l6cd5OLykUlvd_SaouLmodTPOO3UoRGt5KDSYr3ClnszZKxtESyBjhlMKojyHId8X_QO1n-iJzXNoE3ow4mIxiNwPQb7qxIYwaniLBlztmRDbVcZWkmTup2Ym3OWMEu5pWhBTWcH6Mc50Ihgk4tntF-koYIuhOD9k6tYialNblmE9CDm-trzHeTuPlUJkRRNcmqtOerSV1mgZs7zTu8-3Q9opNnkopuTpde3xUnAwcvfcVsosZPe-llFr1Sq0pFvnbciLcJWCZCY1eraLiuWDtxWx1qiJpEG63TYVu8XFMLCAZjleyWzQiC-ZeiXcvKiVJs_QC2SyMDZ0298miNuIYs9NlYS1WYqOJqIiDZzsTN2_CdDXHK64-2UFv83qE8uffylpinNXtRZ9PcuezEUe4WMVEdttdWH0QfzmtXATOHSmB1v7uMGWzeIO316SmWmkicpc0upjZij2J3PBmgj37cvIc9vuUQC1z07RFa4mioZSAx_9ruqzGdrJUxiDehp7nRe4nhUNsm56Gv2OwO8LFYVC52KGulARAvuyXnGbETafh1KMPfHeYQX2d6-Bv5QKovUrKIUPgDaLNeVWS3avMM7ViRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=sRNqF5hV4b6Elr1D4uJ2IynpEH07B1oeHeBomf_v3V0qb1qPbukUJ0mHlSbHStx9Gp5JnXr7XFwT808l6cd5OLykUlvd_SaouLmodTPOO3UoRGt5KDSYr3ClnszZKxtESyBjhlMKojyHId8X_QO1n-iJzXNoE3ow4mIxiNwPQb7qxIYwaniLBlztmRDbVcZWkmTup2Ym3OWMEu5pWhBTWcH6Mc50Ihgk4tntF-koYIuhOD9k6tYialNblmE9CDm-trzHeTuPlUJkRRNcmqtOerSV1mgZs7zTu8-3Q9opNnkopuTpde3xUnAwcvfcVsosZPe-llFr1Sq0pFvnbciLcJWCZCY1eraLiuWDtxWx1qiJpEG63TYVu8XFMLCAZjleyWzQiC-ZeiXcvKiVJs_QC2SyMDZ0298miNuIYs9NlYS1WYqOJqIiDZzsTN2_CdDXHK64-2UFv83qE8uffylpinNXtRZ9PcuezEUe4WMVEdttdWH0QfzmtXATOHSmB1v7uMGWzeIO316SmWmkicpc0upjZij2J3PBmgj37cvIc9vuUQC1z07RFa4mioZSAx_9ruqzGdrJUxiDehp7nRe4nhUNsm56Gv2OwO8LFYVC52KGulARAvuyXnGbETafh1KMPfHeYQX2d6-Bv5QKovUrKIUPgDaLNeVWS3avMM7ViRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjiEa7DGo-x8xcVxjYYqpaFpgNXpZKltR9v0MLw_hqmc8evlNBLiM7Vf5rtxycGzV4t2a7v0mfhOEOhE8hFK9VMwpsvRTYBgTj8yYtGvA-OKkokypx15W5le31SMVYqsuI1JOp6UuUwNIvSCipKY-Jaf1vXPZNWMEMaAxHe03Eld1VyxZWHtokvyk0IyUtRc67ZP5nFPyohb3SnOyFGg2w2C1U5fpsyZ49m8LLlg_v2VBeJbp-ej4TEiL3XL64IDFmhV9cwbIBqh53SNskoHi-cC4lzX14rN_phsXMAuf3onQSLrpCQTOlH-q2U4EOJ1_QizCSM_JgHlPOLS712__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HSiZG4Wd8uEdbbbsHh0G2O9W-FDX07e7K5VfYT5vpsDhSoZQ0Z47jZ7DMS18CROaTyuiWm2I8Uf-J5HuVaZ__RkJRsocpnWDBFckm5XHV1RqzT1wpYDj8bWqdCUSEfloL-B3tOJ801e6Y_ucZv3v7BANwiAu8ZwxnkZnIJGsSuwCuu8WTrnvC6FrC4j9q1o5kD8b4Roz58C6xdUMeqkZFLkW2xlH2KJCAQSNpQyHY12AXKh4i0k6gY_Un42x1BUJ-Js1Rhx3O397gRaJmSaW0dunArt3mc__XuyeuRc4DuheR_Rm4GMy_7rGIi1kUIhMESxEwLrz2CFxUHYBkPCKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm3HHQl5unNSvAuq35LEhTUqBW65snAHrJDg-ggt5MB2HHMp2UPZCnlKXSzWlr_n53hivelghUt6mjnn1uZHCL2azZ3zU6FJuU-Qhop2ZWNle_GLjb9-uxslBv9HZHrcuk08osxyTV7jI70FGptjuFo-UnSDnS3oxuCYCZsLjW1mcOup9Rzz1L6fNJBQDmciMg53rMCLCpUZ9IEotIyfaOzmc94P0cOZ1dmuegEMKgXtlq0aa5amXh8AV_RiM3pL7GbUM1XyUIk1vJZsUsSq-jiGOtJnVIf1X5mareVRS57-mmb5hNbPFc-04OEqJbT9ZrlyLx__IwhdAgyCCQoSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=FQdn453PAKvvx2LoLdDOMdLXVqGPy2Unw-9zEl40iKwYuqzP8USDPUrhIQDW3i2LGbyr1sbHcZRDC7clJfnkGxwHEULT1HnI2WGQDINwp4-TcCWL8zqmmL_gyvSGTeh2cKR3dWVEhGFXEkl0cuJFoouZeE82KZ3M17s6xmCRSFzQPsasDBl4e5L1kCx6MLfx_IAUWgd8OAp2irF_bFCiws5D8u-MhVCSnPHOwcKxvOwDNjMxj1uuUg6CZhWiaC5Ip30kdigDYtcnsYH0NYMNaa6PQbX76ViY0WXQTGTG1v5uOXhLHPtKNcntOWizNRPW_aNj400QVjdSXMycXo420g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=FQdn453PAKvvx2LoLdDOMdLXVqGPy2Unw-9zEl40iKwYuqzP8USDPUrhIQDW3i2LGbyr1sbHcZRDC7clJfnkGxwHEULT1HnI2WGQDINwp4-TcCWL8zqmmL_gyvSGTeh2cKR3dWVEhGFXEkl0cuJFoouZeE82KZ3M17s6xmCRSFzQPsasDBl4e5L1kCx6MLfx_IAUWgd8OAp2irF_bFCiws5D8u-MhVCSnPHOwcKxvOwDNjMxj1uuUg6CZhWiaC5Ip30kdigDYtcnsYH0NYMNaa6PQbX76ViY0WXQTGTG1v5uOXhLHPtKNcntOWizNRPW_aNj400QVjdSXMycXo420g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=bwTAoRfS-Sausbr8rMjXo5ZbMNt0mjKMVZkk9PbGXgyJo7p1Ejkkqr1-g8lcJjaPgr8qJs6LctaCAK-1dC0-E4rAFpSKZS9Gl3GBnzo_Vr4D-QE9yEdyizU6tLc4FvzX4y0_VP24FSmq84e_UJYJf0-orA7obxDjgVICNKQBSLMMV7TvJW7rQl53pSFsWfOB_iRTol9Fi_aw_tE9zC5r52bJnhu4NU5mN_nU0k4tatI3Z2dNgo4uQvTsQ9c_APWqfVQNbOLqM-vBabM-OaMpC3_NRqvc4sbN8E-XDGS2M65t89uvKGVq_wF_DvdCKRaq-1qj6rG9moFXGCgNUQt1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=bwTAoRfS-Sausbr8rMjXo5ZbMNt0mjKMVZkk9PbGXgyJo7p1Ejkkqr1-g8lcJjaPgr8qJs6LctaCAK-1dC0-E4rAFpSKZS9Gl3GBnzo_Vr4D-QE9yEdyizU6tLc4FvzX4y0_VP24FSmq84e_UJYJf0-orA7obxDjgVICNKQBSLMMV7TvJW7rQl53pSFsWfOB_iRTol9Fi_aw_tE9zC5r52bJnhu4NU5mN_nU0k4tatI3Z2dNgo4uQvTsQ9c_APWqfVQNbOLqM-vBabM-OaMpC3_NRqvc4sbN8E-XDGS2M65t89uvKGVq_wF_DvdCKRaq-1qj6rG9moFXGCgNUQt1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=pplMLqv9cEh5M9BE6USEBUlsZKmoI3ZphO15B5yjageDF6EeRy15zvYxa3Thu4VM82ffKnM4Kzk8VHFFCoVMq2o4VuY97xivncctv9h_axOGOv_xRO6_O5W9otOV1DnSsBxpSyMOLHS0MkITLggw_8ILfUXqCu4NhiUrk6pkVWUVb1VmGgvU21HNvWFVlXBQvmO2JflUr8SzCITII2FAeVx-hMQn9Qu-xYF9sKGhK2zums2kumD-5u1XCAbWDCQQOXYpJXUtf5gn0g_JPPqedQuwcXTUoya9M2DUjzxCJ8OjahTdgJPLKkZa0SoycO5-RotC-6-MXi29s8rIJtupFxqAVixMuHfYulmaw9LpjCD3FkBdTzxqXYghX2YgEBvP0Al5X1BwntLIeICBWuv4FdqlWOyvQ6mLEJON-kyw7BNvIdQ0hAFIVjGFS48xZNi_uPvOM7Hwg6APcWSmAaGlmv6ds2EDfFM_R4lxNI4l0NcYjNIxjJ8C4CIBsdikdy36kXsrj3RrccYe6VKij3TgCp14HRmC0jkAfSzH8xerb77D7XslSlRMscaaA6qWFPrV1uv2NR-T-x_LyrfIHneZejTXLo4OJ3wT6MoFRgBopYwjeN4IP-4QUDHvXyamSCfAHMoQBcIEOfrGxzj7rVfLM5BE2jNHgA9kKmX48MBHBL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=pplMLqv9cEh5M9BE6USEBUlsZKmoI3ZphO15B5yjageDF6EeRy15zvYxa3Thu4VM82ffKnM4Kzk8VHFFCoVMq2o4VuY97xivncctv9h_axOGOv_xRO6_O5W9otOV1DnSsBxpSyMOLHS0MkITLggw_8ILfUXqCu4NhiUrk6pkVWUVb1VmGgvU21HNvWFVlXBQvmO2JflUr8SzCITII2FAeVx-hMQn9Qu-xYF9sKGhK2zums2kumD-5u1XCAbWDCQQOXYpJXUtf5gn0g_JPPqedQuwcXTUoya9M2DUjzxCJ8OjahTdgJPLKkZa0SoycO5-RotC-6-MXi29s8rIJtupFxqAVixMuHfYulmaw9LpjCD3FkBdTzxqXYghX2YgEBvP0Al5X1BwntLIeICBWuv4FdqlWOyvQ6mLEJON-kyw7BNvIdQ0hAFIVjGFS48xZNi_uPvOM7Hwg6APcWSmAaGlmv6ds2EDfFM_R4lxNI4l0NcYjNIxjJ8C4CIBsdikdy36kXsrj3RrccYe6VKij3TgCp14HRmC0jkAfSzH8xerb77D7XslSlRMscaaA6qWFPrV1uv2NR-T-x_LyrfIHneZejTXLo4OJ3wT6MoFRgBopYwjeN4IP-4QUDHvXyamSCfAHMoQBcIEOfrGxzj7rVfLM5BE2jNHgA9kKmX48MBHBL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
