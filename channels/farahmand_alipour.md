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
<img src="https://cdn4.telesco.pe/file/sL_NSTxe-nqPzoH7vLM9GBFP3DNwJI7KoGl4yCTNWeXLwJdku6FM4oq6C4mFUT44g5zwpcBXVzytTBBE3M6kwjgAjVETGfuHgoRnlul14PjYw2gaVtO0NlIGtsIlUIt1_P0DYnnczzRJSU3SXbQQauYil9hfHRqyVrdwwuIj2P4ynnqPRLwz7tjuZZSTJKC0Vn8zh6LEH84r0r-3jCnLmNzSwa6E6ig1yOOn8q6zFq7x6spK_N0kq5AsEojU00o8MKkSmPFKhoGL1nLH7ax4QNdODgkag31qoqVqwdGpKEMNsvkFJ5sw0rYwlXOuNiiPg1-4IvEauzO0YvjBZIMJeQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 18:50:44</div>
<hr>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=X_ZO9bb6Y-QeRFRaBte_vumpN2agvo9YEGs10kO2duRGOkn-RwKHfRxCaQFAi4lADcGK4Zws9ARr4QfQ0OOHWM-QrZERZwvkS32fCmnZm4OvagX_aOs49Mx3xa5H3gyRux_yf7SZgy9CYW3JWEwgAsxc8vh56qvX_1fTrL1gpTtgp4R2F9IkMG-vMzSmTQvK4pw03ITdr_MklShGKqn6VCKmzXTpabzoeWRLlmgUPyI3Ybq9uPwsyjBORa4vQ4QBaBAqC7p2GX0RKGi50UZjgJ0-FKXz5qTbcGUwa_98S5XdmBDAX9PGw-q9YbXXpXUqqMiIJWds37vLh0xArz9eajU66FywxZmjc-mAtpOE-KfdOjFl0KfVzKpjDMAMPDAWBlgVyuwGDoBQad3DV7BGmn5lbKSZMn1kkEJyyURH4J0b803iVhZ3FkgH5-9MN1V_EjWjzNu1FHdrebXvgh1vJ0c90jk1LmtNmCT5-d6Q15GefVEnVt6XdR6e9gjvCTTzWRSRI2Gmjw4lbPCBr-lIlBsiEWOhOGZISFsWK3WnBMmHblQBjicDhZbfDrDMGDd6mymcEBvsBALYjWrOUorTc1cYGjB2miOI4TJXLSFht5rJ9MC8KjviyGRFDm3SGc5uOO8WNqzXCyL6gjv9j1Y6Sp0VEiypZJ71ksuFdBjY38o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=X_ZO9bb6Y-QeRFRaBte_vumpN2agvo9YEGs10kO2duRGOkn-RwKHfRxCaQFAi4lADcGK4Zws9ARr4QfQ0OOHWM-QrZERZwvkS32fCmnZm4OvagX_aOs49Mx3xa5H3gyRux_yf7SZgy9CYW3JWEwgAsxc8vh56qvX_1fTrL1gpTtgp4R2F9IkMG-vMzSmTQvK4pw03ITdr_MklShGKqn6VCKmzXTpabzoeWRLlmgUPyI3Ybq9uPwsyjBORa4vQ4QBaBAqC7p2GX0RKGi50UZjgJ0-FKXz5qTbcGUwa_98S5XdmBDAX9PGw-q9YbXXpXUqqMiIJWds37vLh0xArz9eajU66FywxZmjc-mAtpOE-KfdOjFl0KfVzKpjDMAMPDAWBlgVyuwGDoBQad3DV7BGmn5lbKSZMn1kkEJyyURH4J0b803iVhZ3FkgH5-9MN1V_EjWjzNu1FHdrebXvgh1vJ0c90jk1LmtNmCT5-d6Q15GefVEnVt6XdR6e9gjvCTTzWRSRI2Gmjw4lbPCBr-lIlBsiEWOhOGZISFsWK3WnBMmHblQBjicDhZbfDrDMGDd6mymcEBvsBALYjWrOUorTc1cYGjB2miOI4TJXLSFht5rJ9MC8KjviyGRFDm3SGc5uOO8WNqzXCyL6gjv9j1Y6Sp0VEiypZJ71ksuFdBjY38o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkx454vvoBkL2QCkWSqTFWzq67WIq0x80NQ5OAMjJizy9zdo-o4J1-CKcsY0AZN0sf63sIk9pv6b6WyOlAijamLUwzjcwT_wgrUxZfZzqQxT5lRSwxiesY1Oqegq1DuWX5ILLqyc6KJl7dgut9HleURDl6AEmTgaPKTCQZ1NUPzxZ2zLMy1nHOaSRXaL_yezxMLD16op68m1hF8BERYJR_M_VlKM6yjCsvxVGPdmTkEp_YxOorbiHyA39fVroBmYzzH_dBIcM4lJ2xoyapfLiQEEILG6P8I3CsxD5X3dVsbHRkw3JuQNR_Y2yA07oNl-xTHzoqHvMVD5E0O1VhUXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ucZAcftuuQgE-EApzcxILZYL2BFHKTCDuOg63yoQRc9S2qUjDSbLrYt6s4CKJhZYZAXmabm1YCHWUXae_J7QPu9tuUlAMnwa4bB-NkchtGBXxcCJc2mCM556dKi4pn8NgwoxxqYliUvctLAhuZ3BtcISAt9qhXZFvu5BRsdYJGevjHlnTV5Kc0uaUviT-jVmW-nrD2xPMgX_j59gh8CoEHJNM0TJriunvCNoJl2mDtn4BVRVWk32-kkU1IE9ZQsSeTye4nRSBysnP9u1Q3kTps3-vk4W1kpnHlplQJq8YdYFKMeSYQN4dBg92zKUGSI5vQ5UinlZ0qn1h653wpOQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ucZAcftuuQgE-EApzcxILZYL2BFHKTCDuOg63yoQRc9S2qUjDSbLrYt6s4CKJhZYZAXmabm1YCHWUXae_J7QPu9tuUlAMnwa4bB-NkchtGBXxcCJc2mCM556dKi4pn8NgwoxxqYliUvctLAhuZ3BtcISAt9qhXZFvu5BRsdYJGevjHlnTV5Kc0uaUviT-jVmW-nrD2xPMgX_j59gh8CoEHJNM0TJriunvCNoJl2mDtn4BVRVWk32-kkU1IE9ZQsSeTye4nRSBysnP9u1Q3kTps3-vk4W1kpnHlplQJq8YdYFKMeSYQN4dBg92zKUGSI5vQ5UinlZ0qn1h653wpOQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A91kuYO3TzFrjuaNItoqYRpI5zEzGD4PwHzr04UI1lm9DiEwsKTeG_6kG02R2RCwwOmP0h168EzxOmeE7cwT2zvl4eZtSvxb2-o9zZd9dFsDE9ka0FPGI63mHUAqTNWcYYv-bkcMWr4VWrqXpkzcOdZubFXk0Zd5jWChMiDZo5_Ykg9w1Lp9bkIxYfPNRwVWlSmA40B-psnGM0OVXtI3YCRTm3DXsqwoGBFhGncgp3EyLDOe8dFiX2HEoQmD4YviNHFOWsGw5hYZe5ZAYQo6jAHfvbdBigLD5TCaYbAl9ovy-nBTbuPqVXNthWX0n7G5oSPfsKz8FgleIxWnhYbbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edDV9CjvDEqt0FpOCHD_yBMDypzmgXqWDY6dm2flpjbY66GvUL4sQSAyT3XYf8jk0beJZo-zX0dyZV818M6lxpZaAVMpjaK5cSjIzTimwOMvAl6FjMhBVPDCsROKEw4lITOYG6pfAxO-n5f4IP9JkXRt3yE_UrRjUqWMRc9EgERWhoKikDsN7ErGvFJqz2EQQvYoGHtiEYo7Ffpbe6NwDDk-8Cux1Fp9OkuJtYCF8iFDqdPRjgtwoc4CgP3fc_7_16dFtsZ-Wpv8SPuEntbB2OnohSG3WS67R6Xlz6QKF74CxWkraJ9hCNDHxQE4xM9BgfVQ9H1Mf5VfHnURQI69lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGrnjk1HjFh0sQjWt1erjgerVUKmQwtCoOrtugTug8iBR0lte3ckwy_LfEktgD47Kdjagkzdmx-lmYYUCUyaTJDEFc_IBlZQxp2Ld0OXLW7o5_A-a8aYLU_IJ7RLpxzD-8EqeGHmIbHo2NaVDcfoUUGcapNMbnNUEKxy23ZrxcvHdUfwNNICL37KwYamjdsdPhHsk2frJx6EE4IfyAe84xk-NeDhA_QpKGJ7eZSDxPerT9CaZ2SLjkGnG2BNoylFVHHXplAVSrs1lC5QsAb4GWJLA1MnUAIj7TIkiuqneBD8y80PDF7UVAZ7O5ZOqY7PwO4ieUgX-z0_HurUmVhdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKZez46Xn4GI-SoA93oRq_kFbqKOx0FhD07p24HU9Yczv9sF3dSWgZP7hsZseQCXO5QKHI-cwbK4-Xhm7GCrz-xiB72zkRArw8zvULvhnW9-fVXA4OGqwPeenPm3cyBEe0sYCqmzzXU0KzjVmkmK_abxp58aZM40lN15bJlnzZlakqpsOXztFmWv8s0ClZj4fk54TycjiPxjeSoJ8Jx_i4Bn_ZRA2KFGKI-YGY5lJJ3FJCSqsc4qVJLZqIQ29vVuzZg9oxrWXawFVWqFkY_-U0KQ0Hl5I5709E_TENYb0Pbe2_NzBpuNA3fmjnYSkkS98oBJoDjtZyxNudnuj5cGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbVM70X_5_B7MbPQQs9gr8NsBiRoMGSEHdTFwlvfMy0y0W4ZStcGrD1IyTaIv3OLMU02GobSzguligzXBg2r0xyOi03HhLJISSbRW1j0XNWh-0n8UPiEqX6cj31FjiEFEHwTUkNHMvmLSEjTbERZqu_GqEpPLhKHfKDZowkYC69DMSQyyzrDtTnsWnUXGjvrOQ5nHP6_THjDyfSUc5cWeccv4Tvb4rz5LJlX73ijolFhRLbDBCYD0wyIOTz-FkwhddfyeCej9xL6NCOe4X6SyWWthLeBuZ0TKMrEBUuEXfOxfJ6F4g0APziCA9_nPaoud2nxPv5AaBM41aFnsJF63Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEgMOSHveFO1xJ4gaGdBP0WhAis7h53aEUtzooS6oZsV5BWmFapNHX5_q8raGiGFQgCNJ-t21nnuYkojlkvIDFL6fbCtNWF_oWtlr5BPhsrEamfepi-_ROQHb-BF0QdOAZKhyWnFUaLVnFIQVL54n1MFatBqWE7VosQ7LbnX7VORu9NAfcvu41FJ0YpuFsCoWRYo72zV4QkE5qgrPA57lUV_D8RmwNMmlfBocJMYeeCunRHitTslXVOLltk_7xu8jkVUepKElX3CuCnHev6ZKqdC6Hcm71Hq1jOaCqr1kSYtb52zbkcqXabLKsRR5NwJcrRgXSfxuZEYAJ1da8Hhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJVNluKjno2kvVW1LeJV789-qsdhlaDztbwc9_KE8uv3RdNNBy0BE0FcedZz7p3uj30UtywUjZJI88RQQ5ae5SQSfjUFsrzAYyErh4_lTeEj_3f_G6EVLcl9yh5Xb_ORh_ki6xB-aKgL5yLtkLrHEPtoRKyBmpDz4wRmeSG2flhTa61va8bhH90wf-UPgL7QIhLBxf-xdVgolrp4f_xOFvLtkWl7t0m-5eB92bRYMc0vAAsFoNG1GpPA3ZxpGso37cBIRsHA9cCOcormPNmPbqHKLPZZe5zDXVld72TB67F5JlGIf_5JKL6yqLDDg3LwEhJoeGw4SIvpquvm3VmCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/km_yo_hOZjETIqxDOpoRwrn9pCGcx-Q7HgBzRaHt-bwDl2ZhP-lVKmNQWBFBq3PCm-saEqpdavmVwrIBoy7hHg25VZw79oBrBCrnaqjtRL3Gxaz5SeGCOgz5Vf9ySgnNI5R93hRJEsagVnmcejm9u-QicMGhKyqWcuz-GlWNr1xxxVaMMmA0Rz4u0Hsey3AKyyDFCEui3kBHd0uQf0cp9EHzSuXhWNzfdU2CnnQEpczyN6lTgDqHzBY6zXRB56lFvUtQzuJ8H1UhFYv5cbtXlsFY2EO8EZh1so-LXpmAnL73peLRi2ouXCgsdadEraDC73UoVXA3OEVOt28Grgg7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4JTaf0vHrdOtGcnXmHTq1egQcb3xOXdf_W1gw5uAiWtzNhNR2dlQ6HG946Tm2aCi7MqeO9drxwVv10XxZ23lTKz3u4LB-pmVFIfY9Hr9asa8sS6oWjsD0q23JwS5f0Gi0hZuf4TmFxy4AizAVisGkf8_TYrHIz2ioumaKVzKmEf321pRTKIbaI0DZSsEphn0BupyYqKQB9XjtLHAklpu3ZfHiBSvCr7iLsM3UDkU5u-UJYogGBUlexjdX7BTKgOry7u5v4dgqeZEjKVn8H8fjl6z0op5q08lgNwUEI1-8DFINnDL3efqLZ5P6H1t7p2rxp419HOuOtk_bgHbt-TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zh4h0iRyK5zhTlNO47O1CQcmXb_9PkeeFOy69p9mN2_9OigEeGrjVpgHtviV5SvNDbsXIdK2JH-G5oI5LdSPHxI0J0fAZYlrDyZajhAiYO11uL0UxuNoKw0LPvs94wUIcuWDQeMNJWEtiJXYrfO6xXiMw87c2VW2yxPlbCQkKocjVZJRG7IP8LQ74h0kkPIuFi8KKqBMZOoyuKynugL6Bp0po_pOvKUyS2FRCrdrjvd34Z0BrPUjcyjA0Eivi1b3wT3ETXDTHJS6S8ygri5QjAcUxKR6rStIJQyuqS-BazXTC7tGsQJOneEb55VES5-JZSBb2YTr_ZpGRI5afZDCIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7EDUsXNbb-mM4WE-YtSwStfWjeC5Qi7pvc87MSUhJ6C0uWng80hJoFKL-WKcxw5A1prIIZa-5BVitK6db_glsTp7MxNcbHmkxHOxaStwft2Iv0jzt2cwSnqyZ3MXthaoEQ83aHmSZO74DVa6pA3eWzc88sxpsdn5oRE2EWDpBJ1VX7tTz6_sImAhGEakee6S-S_025tNdN7aUMpoYFnrhJM1FdiD_IBXZmXY3YXRRxq2_1_1uPhtTi6kbyZJT8542lYfVLvy-YepEmkwt6bFW2h0YDbNJ1Hb7H_XD1XyD8oeCRpkzWjxnls4q5NYW0r2NzTosx4cowXkrb9xD-KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IskluEaENewhTtYZiOv-0tTiWCN8z5gY5YPW3VqGAPyrbDa5HfV6ZNHS_h852oOtrJrDb7P07TNFOAvuzwxARyyHp2ch5kkD3qFhuBL-_k6OFQx1QMaIuH6PN5PkyB3L4eiwk1dE2ArLh2OdNRCEGFMO1tza7CitlOTVrdvY4gvHYmQqJwIvonra9iaWaKdYE217uVNMBz-asQ2OMmVdktWlBV3FtUlwBIASOv20qt1PaMQ1ODbrCzgUlbGi32RK6wZ-Cp6ZxFlKLOx7w9qAKR3vO8jrtH5InLYK8WccBwFtRNUj8SjU94XmJqKycrBkQ1HT14Nnda-x0HeisOmtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C15ggFdopgf9pTzFRWOymQyWTSgSNZAEsbCsy_QMcqf_DIH9A04ERL7e0NLkbicrAcPCn0k_DLTuzAhjbzFbFdqAF7EZqwPXXNVf9zRh9F-tHS4Dhywh4YNCsRYlIvaH91t-DRhPxsZreOJwcEysCn1hsTLXmlmscem7TLhuBPtHL79i2qFO07vB2wCnUjc-eLyhSiOL-egPMMSvmfXx7ktX4JtPHNRPmo-5OtX7NNAwUBRLc9mNSngJ1kBvFldwFfe437pZphruvHWDjTg42zY0QZw7LzepaddsVS_XM1BbVu91KuLMmeadSUJBc8amSx3XYQvO-J2SUy87gQamTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iF4SQPld7bXK8UA0a_6_tHSsrmH1Ez5D15HIPTK2e5aT1X5HSqfqbYppptLu0Hn1VDBz1CUvRaewA-nvcQqRUYMJneBYYl6MZDtriNbuaJIhDleDe27x7C6XbFHC54dWTYpnsWsSkle1h-pmHY4_JFX4jMcNgbo--narYXLJWxrjDVTJmmDo2ImSDLmYRsuIhCdfY-K7RqJ2PEVBA9V50YhJkQGrxiitigv-mlHCnQ5LrdJrwP4nSf553cnQBTS9o8FEwgUXNHr4GpSj6WKgaONmmbVEI9qEjl3a7Ppt8eJX3h-essUUxp6zENfVxsBh9yK8fRLN4mSnsVVk_rCMIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHixZ9HEk0YOSSsEvBZm2p9JTdzSt4SqTpMFoIRMLy43DzgU3JQ-AUhipdgpsmAg51J0Kk6WM6qTtgWLXp0-ajmKLziI6PMQ8v0rxtD3yqjyT3dMZW6kr4kKYuFUQg21mbqaO8s2LmOlU-lLxY3zGuHv_Xubjsgg8jJZF2f_Mfg-ZrkmKMaNzGS2aIwuvR61wkMh6c3ppt0Fw4pL2nsF9a9UpP4jXmkuR5upv_mNPJrD9wJXaFK00xahe7tqrbt5NOS4P9z6Dr--qczv-tFLmMFgcE2fIoK9HOCbicqGElkkiU95IOcyZFoPCn0NVvgB4Nq0EnCnDB6Dv2HXz3MWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3BG9E6ntFYzp0fk6I6R9aces_3QKEZ74UEAlPR52hPcE44sNLYwvGaB21624htSKVW2GDdlo2lNSKYK-7UepkapXRtQaeCPbZupFAJCIU8a8k-MaxUnwoXLym5pkHcHsZ8t6ePWOE5QMz6qviCanbHxHtgZjEvrGnQeIZGJp7GaWv3_34wXkrAbKB1xSc8s3TMu09KvHkz0Pji7nJe5au5q6_EVTUInp4G-6bJZZLz7YsZ_GfUt9DrBuQDxAybsve2YphPasNyDNq7EcLRLVH_PrNRxdGC4UqOZcXTM9hyydnwR2ErD6q9v-SSdBCNWjno-b1gcPPhoZcwIY8zC6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVQ9smVy2NaUeAwRDft41xcZ1TV1KsgJmcRzh74_ycJ0zV0d1cMtrYaoyp3-ccolBVPP-eDzrwDdg4kj1cAr45_cgIvuAgCNe6bMkqNOxM3C5NDrO2gyEHlBPzQ08HyB8wn4kS9xr9gam9SBsvTWDk-Wr5VQU97j9_18PeCSEnb8LadIBJLKWW-f7UBejWMDbU1ThWmLDF_qsd-97JIQdlsPZRfECfbjMi3TkxOut67VoZVlCTBYR7UZglU1nkl8GKbLLJhCnT3WSblB0VHxr3x_x8DmWyL-oIYNElzGeywluC7nmXW-epMMMhVVZijyZQuFk421beoARB3RBKnM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=LefOdZAhaSCAJIz7OccMA4MNF1cQ_Tu_bPyZ9erfyjdXPjUqyCw7vpQ8jZc969f4-cE-vToS7JVvpLmpVjQjR0Jc8OfOe6o3iPr6HsSuQPhNlJAofUU7vNDWAYYJ96M5C4GkDOShxZtpIn6WMu7J7XcRxntiDSIoOqN8URpVLPKGGZ5tZIrtVa-g_zSYGHPBe4HPsmvpRrNgjudnviCFKcm8cMRZuKC1V2wk-DZN7LAhcepzb0b9F8y10PkKNPsYWLxHCd7CN7RBMlTuEX-Pvh9mGgYdPeFQsSLrp8xb9t0BRecVhLGE7aOhya86n9DQctI4HkpPlp8OAjz0R61Z3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=LefOdZAhaSCAJIz7OccMA4MNF1cQ_Tu_bPyZ9erfyjdXPjUqyCw7vpQ8jZc969f4-cE-vToS7JVvpLmpVjQjR0Jc8OfOe6o3iPr6HsSuQPhNlJAofUU7vNDWAYYJ96M5C4GkDOShxZtpIn6WMu7J7XcRxntiDSIoOqN8URpVLPKGGZ5tZIrtVa-g_zSYGHPBe4HPsmvpRrNgjudnviCFKcm8cMRZuKC1V2wk-DZN7LAhcepzb0b9F8y10PkKNPsYWLxHCd7CN7RBMlTuEX-Pvh9mGgYdPeFQsSLrp8xb9t0BRecVhLGE7aOhya86n9DQctI4HkpPlp8OAjz0R61Z3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBUe3YRPLchOgUBhrzju4-7CdQ8sB6XTt521bnEaufa_i41Y8tNbsTI7blZnBpmdkaPj2VAKMW5kgVAPKza1GQ5aub4SZWxXyDktcg41Wh6oOhe-51OwU5mrglqRgt6gCwF5bwb_SBsK-z_4VXPn7nBfjJTuku21rtUcZ4G0mZstQAKEFJ5tZMQMGgUNye3NLTyspS1wAlfMo7ui_105i-_dTggbF9NLNub8wMRII1-8vCeBjJ1e6IoFP5unOGTQNdAy69w1b9tECJOAwLYrOdxan8Hpa2URDKx7bFXB1M0BdlCT7rJN-xCH0j7jYH_Wv4obgXtI9NsRypvb8dsL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZctC1nk5LBwVwLI5kYO-Dc9NLnFY0clM94vVoTayYNzsk4S3YG71mxo09ixeXLcuyuvEG2D4iq-CyR8LpHSRRlMjgPDke-nEguiPKmSLGpGPH3k9u2-Mlw3S78tj9VZTEBL_Zo2BkhZRGwUWtRfkSstOGTBSIgFQLwF_7ZGTyCkZFUU8aZldeVLCwNJE8VKN8-251tQGDOUJG9OukesE9Yss8tUa7dwSBVQPF2O8uq9R5y4UurXBCrK6M-e0CedrRO0P6tWww0fZk-M3KJK8ES59S0MXZMi0fUb5qp3L3iv0kpOo0AVGCbuXhePVX5xEFIapUFdnGvc3IJeBppf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmNfabDkPtm75e7PGei0LrPH9hml7sb1a2OXF7tiKZfe3zInhfSYMBQaqAYgOot7YYYbzl27k2hxa86gUEnBCUwqJ_P7XLtg2N5bqkcFvS8S3IHUEyvA5wb_aNFS3kWGAbovf_PgZ-hFZ7S7r7lGdcAbbbmBobmnpOtm3lMQN7ZsvmGL0xfDFDUMr3YZ2whISQNRsWUjxv2yDNUZkKrz-aZbdrZeQuU8tcX_oKuO4_W5hYxRes6Xw1Iqhw26QHJ6Gew9oPmwUb4mZYmJDplZ7TWD4Zp5troZk4y6FyWOlMJV4ylFyidrFHJ0LNQM1kNIao34DBpvbGV9tU-bP_05Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=QrTaD7tk-ToFKKpyNCcCsNXVcTJS4JPpfhACsw0pJa213GS1lDI1P9Y1OuhTBYVL0Qp2gd2UZxCFfIWgEdRazRhqjs2b5eVRaZo6NsktTdOWPu3VWKWUOIQ9-Nn7mGfyRA1WmXGykWiFcAByFkOonZWwjbMc0LMdvPmkuyw31NF-D-QwBmZqIojfAEAKeJasM_mdgijWj9bdxvnDwThKZyse7Zb2b6ydfm5IC1y9MLAPg5bPTpf8di8aPFs5e-eNW5-iJvmzjL-RrQjJT2ypK2qKUFgFuuVj4B1Jjff6s7R7eyIiYATXDtDVmBmlMcvBCZQ1jkwT7pLOa2kgKh-5Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=QrTaD7tk-ToFKKpyNCcCsNXVcTJS4JPpfhACsw0pJa213GS1lDI1P9Y1OuhTBYVL0Qp2gd2UZxCFfIWgEdRazRhqjs2b5eVRaZo6NsktTdOWPu3VWKWUOIQ9-Nn7mGfyRA1WmXGykWiFcAByFkOonZWwjbMc0LMdvPmkuyw31NF-D-QwBmZqIojfAEAKeJasM_mdgijWj9bdxvnDwThKZyse7Zb2b6ydfm5IC1y9MLAPg5bPTpf8di8aPFs5e-eNW5-iJvmzjL-RrQjJT2ypK2qKUFgFuuVj4B1Jjff6s7R7eyIiYATXDtDVmBmlMcvBCZQ1jkwT7pLOa2kgKh-5Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rI_qajkYxD2HI-FQWSWfgoOGVAOWxtR873d690o28HzsHubf4q9fvvX6ua4jVhyRBpqYfW6ISwvYLSwy-_WJqX_rtPQeV6rBSWiVvNIOic-PmCc8LSe16dM8gwvNpBXuqyrAO5UpZkVSpqOBlWcZl2fBAcWaVlqw-vifnYzx8D0BD2noTMy9J_-sa5go7d5EPPz9ZXzGO014Z9_I4pWnSd0GdzHh_su-15b8P177Ah08QhHu23zbw7OXoLTLuHuXdjf_8ouptQ7BNksdxs2Z3aq4T57-Wd_UPY7uz9dQ2mYdhCCsDbp3r6PrgfbQaJc7mWtl7t4x6U1GcVAjaLHLkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=oqqa6b6gMsb06Ph33W8a5-riV69kd6rgW2iLJF116FAC2KWGD2cuDK_Hzz8WS0kqzrt1aEcGZH6w2Yqozt7hQ-M9mEHLAHldE9v26sO1TL_qD0G5lnMSHB6NIHLM8_m3q_oZ72Yay9xSH8ftVUuu7I-Tj5ap6zk1Awl4sY4QQt9pBhmYJGmS_ZTWQOCYk5nU6r3gnF8Vt_ueRGMJA7L86DR4t9Lc8s9ZzqcQAxePTSxuuUhqu7dh3bYi-8iucAUpdHY7Pe40JFs5E32ka0BTxeDm52op3GvvVL0aEcL0cnfuOSPWVqKPHCRmzRauBQ3Vmo-0JWRDJjuoASka41xKOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=oqqa6b6gMsb06Ph33W8a5-riV69kd6rgW2iLJF116FAC2KWGD2cuDK_Hzz8WS0kqzrt1aEcGZH6w2Yqozt7hQ-M9mEHLAHldE9v26sO1TL_qD0G5lnMSHB6NIHLM8_m3q_oZ72Yay9xSH8ftVUuu7I-Tj5ap6zk1Awl4sY4QQt9pBhmYJGmS_ZTWQOCYk5nU6r3gnF8Vt_ueRGMJA7L86DR4t9Lc8s9ZzqcQAxePTSxuuUhqu7dh3bYi-8iucAUpdHY7Pe40JFs5E32ka0BTxeDm52op3GvvVL0aEcL0cnfuOSPWVqKPHCRmzRauBQ3Vmo-0JWRDJjuoASka41xKOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1DXEYNOUN41AfnHh82860BOf2hSJUDinXNEFUkGypYdPao8zVC86MN6eIEUUekBspmnWUZGpfC33t2EWI7nq7bmLTven8bNQc8T9n57-G8G-LQjIBeBCsqjebaFY1kb9DAyG2L2glw91BTrFII-zjKqPy2nSddO5AHH61r8DjKjabTiupB7E0AcFSK4LqdYuoHk2BXSYYiJ5QC-3yT5LM9Gzi8YMEbLdmweH04_zb3Ke-EptGtm1p1Kw5SrJR7yXbUf8UIF4BFNjB-jssuN4HCYXppNmsRlslr1Y7NgFxY2KU9K9xy4WAcsaeRneNvEBp_VsAX4gwQhy5QfWgSQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7CIgNFYXlrRSe-qRxH7_UKOHkZLYfxD8oe-6j03ewvGw53lPOSnbh4ZKkda8DT1oa1I5H3C5A2FxMCT8hBUHZqhLg-AklglVJjPbKo1pvXKVisvM0zg0Et9RR0YUNdKdGTFDG0C_bjdGlJqOIVLp2v5-gdwKQAGttOq8CUwUphdJu-f_4qHakGGMTojlPjSqz9bMpA6iwXEqTSeM6cV9IqwCYiaO61oQ8kzley7YT_AwsGLpMxygLG37eFyuHcEP09OOCpUyCZQMyLuDTivQhaJs38rgiCihV7JXIRi28FpvEpIuac1MrJljJX6M2a0HnddpxaPQUw2jsZ_dw8lKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KMQjq7VExVbUlXyq1Jm2usSX4O9Kh2BvaonuuYyd5yXtlLOvjcBB0m5rJdsw2xHFoiE1zh4QkhOAUDMcISXYXvYrVfQMJLaX8ufYgKcO_K7IjtbkehCdzPzBtVXmFSALxEZQpKSb0V9rV2xnc0hK5JdJOArFhRTbVlz_HuuZF4u8a0BJKyG-mI0A_4KiD-m7wC0aOGlMX1XD_j7-8BqrSMCmRbnCML2-Bdk0clc9nBGz_kEnrM76kHbio164PnIRofYantrzKK5MnT4xS00s0dCKRLyXam2Xk-2I-kq32BKf798U4FhbjoUeEtkQyZKfjWozHPlqv7rU1UBKxVJxjZ4eAL5WpLo9QIt4jW6Jcy2sUG6_ewqjQCLaXmOpg0CrODgftKQKWygzYwu_oX8PK3NTJfxH_sFpnMcgu3PpSmbB_6WWcP6hTf_jP8gBKL8wYJxz3xnYPRk6jvWQm7VZZgXkuyblFN-RHtKkCZ8K24UQFSH8dZ5qzfJ3eFkSOn16d6rBUU674w29jdUPpJMtMftES0pr3cbm1NPQHPkCfa2KGZeE6dbYRxiAXN2Z6e51P65o41018UnFd60JBtejbZtT3R06p5ysZiYQM1QD_6eEzrv3Ndl-egVgZ0hDpb9gWmHyROjapEiUF4u_nsRZw0ku2Wb5jVchN2rQqbIeKnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=KMQjq7VExVbUlXyq1Jm2usSX4O9Kh2BvaonuuYyd5yXtlLOvjcBB0m5rJdsw2xHFoiE1zh4QkhOAUDMcISXYXvYrVfQMJLaX8ufYgKcO_K7IjtbkehCdzPzBtVXmFSALxEZQpKSb0V9rV2xnc0hK5JdJOArFhRTbVlz_HuuZF4u8a0BJKyG-mI0A_4KiD-m7wC0aOGlMX1XD_j7-8BqrSMCmRbnCML2-Bdk0clc9nBGz_kEnrM76kHbio164PnIRofYantrzKK5MnT4xS00s0dCKRLyXam2Xk-2I-kq32BKf798U4FhbjoUeEtkQyZKfjWozHPlqv7rU1UBKxVJxjZ4eAL5WpLo9QIt4jW6Jcy2sUG6_ewqjQCLaXmOpg0CrODgftKQKWygzYwu_oX8PK3NTJfxH_sFpnMcgu3PpSmbB_6WWcP6hTf_jP8gBKL8wYJxz3xnYPRk6jvWQm7VZZgXkuyblFN-RHtKkCZ8K24UQFSH8dZ5qzfJ3eFkSOn16d6rBUU674w29jdUPpJMtMftES0pr3cbm1NPQHPkCfa2KGZeE6dbYRxiAXN2Z6e51P65o41018UnFd60JBtejbZtT3R06p5ysZiYQM1QD_6eEzrv3Ndl-egVgZ0hDpb9gWmHyROjapEiUF4u_nsRZw0ku2Wb5jVchN2rQqbIeKnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Vi8jgYoiqZi9YaBsdLhz7WuCpHebJrfQfJK_gDRW_m-GL_1hWsOMpFXG6fQMbmEot-P59maKa0fsaFuIygx_BdfRJpBb2p0csSN_ZloP4rw2KyGEn_6wcKyDjkP7k8CpCHF3Q2Ly1xGmBvce4VDUfXx_9h0s_dEENd7potSqdgqcxppj98UaR9D4y8g-gC4dNaiEfFhY24ivxibeZoqM_WRr20jYhjhNTh4SKPPfn0mH490Guw9TkNA3IiNSpkLRlLs8pZP7oX595IZS3Uphdqr654AyXqG12S58N14ub24poWJzsSG2p0Q-883lGPAJDzRtJ6kCRtx56k9HDvqa7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=Vi8jgYoiqZi9YaBsdLhz7WuCpHebJrfQfJK_gDRW_m-GL_1hWsOMpFXG6fQMbmEot-P59maKa0fsaFuIygx_BdfRJpBb2p0csSN_ZloP4rw2KyGEn_6wcKyDjkP7k8CpCHF3Q2Ly1xGmBvce4VDUfXx_9h0s_dEENd7potSqdgqcxppj98UaR9D4y8g-gC4dNaiEfFhY24ivxibeZoqM_WRr20jYhjhNTh4SKPPfn0mH490Guw9TkNA3IiNSpkLRlLs8pZP7oX595IZS3Uphdqr654AyXqG12S58N14ub24poWJzsSG2p0Q-883lGPAJDzRtJ6kCRtx56k9HDvqa7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qc9cEtrhlJRZZc8pgXHewaHEkgdORdFe-112C-jTQzo6qjRlwDSXQcUSKTU9poNUk9Q8a6P27pB4JiYPyuXMLChsyXfmNvJnqhWrewRR0-e5Qaqjq9OnYaU6zrM-i3Y-IZReJMnNe_shm8s7AGvwd_DkBg8F-dsPOkjBmrGeT-2xtass-Vxzjd5iyWJfgu3s3qQ8zHmBCFHhGoux1Vq3nTLmz_Phib7p6doaD14afAFC10TwCiKGosQocsw2986e7bmJYaYfFUwdCAHAeDbAGxp1qNWsrUTF3PHjMA5riVpsLjumQ1pmEN32A8fDUF8p4XsxGDKc0WPezXc6mrgn2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Y6dnqhJYiF8XFXUmqAapmpFJZHlcwhv8ByRftynGZkaMEz6XaF71cCrhAgulHF4F91YXENgBNX4D9GyTOriagVGynK5aF0gelUgstY51IBKipRJ_Y20_0XUQbr2xCxXXON4V82spheuWPhSlSo2vsRmKt5w7CsAlJAb24yM-PH9eskGpD4U1omqkGnwOY3lwJeBMHYtXL-KlOi4pFwN81r8oC_rWe5OT68vehXULaqkQ_PGsAKZr5thefvu0ZD0gi91Q_JEpLAAeemhY7md78-QrXBuJQ_xq4T3cHKRdJqnlp2K39Uz0u1MCaB5SejaXgVTEbiqeJbEwAz22hMno_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Y6dnqhJYiF8XFXUmqAapmpFJZHlcwhv8ByRftynGZkaMEz6XaF71cCrhAgulHF4F91YXENgBNX4D9GyTOriagVGynK5aF0gelUgstY51IBKipRJ_Y20_0XUQbr2xCxXXON4V82spheuWPhSlSo2vsRmKt5w7CsAlJAb24yM-PH9eskGpD4U1omqkGnwOY3lwJeBMHYtXL-KlOi4pFwN81r8oC_rWe5OT68vehXULaqkQ_PGsAKZr5thefvu0ZD0gi91Q_JEpLAAeemhY7md78-QrXBuJQ_xq4T3cHKRdJqnlp2K39Uz0u1MCaB5SejaXgVTEbiqeJbEwAz22hMno_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa2CjVP04I05i8bePOjx0WLhTN0T24XefeCAwZpLZtcOUwjMBPuWMwlG_47HU_GASt-e0hWuISXgGIuHlJ34fYIrhDgSbSteV6rZ5TooMy3tzqY7SLheIAitbsXUHfhpbmB9UkY0RvIUqyM0IqlThi-n2GcUDHldM_vuYHEYGeIKJwpNk1Q_DZr05jOmnzurr2aBUt4kOJnj60kIE7OLY7KnDHLjG7fodNzLB1qfDe-jv24QsGprPaT8ukQLHqp5XbztJyJaCMBgZJ1V9cZOcsgbrbeqi4_8WjZB2nYSvCrrogzmIoNk91xCUJMP9s4ick-mU9muwI5ikNWT42Jt5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpobo4IEBktz0AcpJitRi0Igp5QJyZluywHrxX_t7YQFTkq3nXPtu2E7FRQknQ0qgfiVGYDCJLHMeFYbbuCXc6d9x4s79jkB3iuiNJECuj1cl8CqYRoEBIn3lKyiXlRyTg3vu_RH-PYDXJqmB04N1H6gDgITZqdPSVSMxlccZN9JLXGSv4ELJj8lA-zJ6coQGsQYm0XGHSTUXVHrFb0mMoB6uuAjt7U-UncPMugKNPq2t53OqYE-QecivdHGN-5VGfCxYJL7yfzRDmN2TYccOvhfMrDFfZFC4Zw9wf8Z_X3LfCG-tFiUt7eX659V_45cIN4MXcSJ1TkIsdpiAj4CSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVqmaNec2w0Pzr9qlmNa3baJal2eYkcd9495RMHs2JDbW2ukTHOPd9924oJN9BujoIJDrR9-2MAIQGrQhWf2Ei-w4hY-3ChGi0CiVI1relgwdRUipZamDSC38JcH4g-hvUvawD1gzk3r4JKxcrVRm1ZcFFs1mV77n9FIRLanZf6qiSFW7m3YOAxSZgupxGwTq1hVmYvq2xbKnmnz5sFvpayOg1ufaJLEVQxs4oljcXvQyeqRtt8-wQo6VQp-jEw1Dwtm1o2VkwspqDlx7mRLL12DyNjuh4YHyJAcAnFldMAH_hVPdYWxmSPNhM0HPqDh6AIzwhODej32k-elteJJyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffkg9YMewmTJnCUT-h-FjFk-kuzBciii1cw_VeNnaV63eolkNto40uc7Wg2CafR9PF_8QTHiLGaeBmEh3cDiwheAnFNJcDfYyTVhyBsSOyf9aVgA_fABdrdROjVQbIq5e21ofdhyq6i3UsO4y3iJpePjJzJ28pDGqXY6KOJPfUtjwOgx6BJhFENiS97rROkWkgw0bJd99NqAZx-VHvem00UU6a-qa0SMLcBPnZSkObLXD9UP2fLHN1D9hjKkySHtXJ5i8yb5Qiz3EpL7RibsMHlQcJSrv4K0oLto_Rsa6O2Y_1Bum61HoD9rSoeTKR9K7fGkiaFxzIO1WGqK_oifTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvkX0jES2EvAIQcaFTk1eh1x1KDICytVx-CDKLUL9kjVQZkKG9FfW8enzNTZiTj9pG0MfASBjXcZotSZZ_HOJ2n0oBHJl1WECwvY0anA0zpfm-A2MOKlIwMeIPPSe4j53_tDu4ddsHPi-yM8zjtcBqqSov1PgYfqTgMXdOhS6kw1zJtYZXEd6nR_Qqvicw6Gi8Jrwn2_N_8Gc75NB2kk9s5LxUAX7nzIXIZRii3_2xNq0iu0OBK90_lwRv8d6OzsZJRs74yzlu0rnTqZJ9n0On7-PJS8SqMbobI3uYhO0QRGlzGJDqjJXB6PDqzSN3nmnm-PKQOEVPqKJtUMmw5QBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Rjdcz5E4bRLiJZT4USZbHr_e8eFa6D5d9HXnXo7uwM6LgQf3DEpzw9bYLVgy3IgQsBUTe_RBqnsg6cARWgnM3085LLOMZ3KLBS7bLsMaBgISj_y9tGbQC_uYqjtWSJUBrs8fkZYawnEuOP3-NaXYUOOmF-krrQkpzrQ9qSCHVD5oG9n0xyBgmhddzh02vnOfy3dS5xpH_y_-2xrfeSSU4uOsauBrRMCzFpVa3Njtmgdp-lHPFpGCTpGoracoirKYSU9xhLNhouOEknHx52IA8_ZANxtgD2OXD2XTBC-S9cFI1Q1LVPHQT4PAPfVWNqypzYzoCBLDp1_I5dmolzp_cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Rjdcz5E4bRLiJZT4USZbHr_e8eFa6D5d9HXnXo7uwM6LgQf3DEpzw9bYLVgy3IgQsBUTe_RBqnsg6cARWgnM3085LLOMZ3KLBS7bLsMaBgISj_y9tGbQC_uYqjtWSJUBrs8fkZYawnEuOP3-NaXYUOOmF-krrQkpzrQ9qSCHVD5oG9n0xyBgmhddzh02vnOfy3dS5xpH_y_-2xrfeSSU4uOsauBrRMCzFpVa3Njtmgdp-lHPFpGCTpGoracoirKYSU9xhLNhouOEknHx52IA8_ZANxtgD2OXD2XTBC-S9cFI1Q1LVPHQT4PAPfVWNqypzYzoCBLDp1_I5dmolzp_cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2TDBNQIvrbKiaV0LnqdflDP2MmLQip22v0CaOGoa3WdyEhvs3ouXv6dd14MQWJz-5mxMFyacWAclYik9LzvubRNuUPBDFVF8HLJtADYfzoxGDQ8hWPKMRaN-Ux3Mhw7XNv564MJPZFWWbTjVNHYYEiGfn4rRWMwk_QUcLiKWcFNIEO3QW7Wiq8zIzUo4ygsJJX00EBAgeWgMED9GAJJCsMGvRPcyeKj0YfIGusi375YgGhuq_ITuDuEap3DLhw4PvaT8R-pepzDt6eL559Gx9Jq5T2bzQ4ZxRpmsYQMKmDN3HZnllg-VGI5n5_qdiaeByizfCZbOWCs3NZWuzgKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZeBG7l0EYE90zWsg2FbOkjhZ9iYFxqiu-4nhk9bA1BJipos7RWCNrHnXLHuLNb91A_r5ae59rkqQH_TgkXiAfpuZgmtfdnuex85WQTtRzTCDx3qixtSjSTPU8y-1lISyhrm_Xi8NZ-j96Xm3Lf3enyuuieVXrCbrUtmqpN5R3hmZ9TNqNnuN0lNdEmHmAaP7L3eP9KMIU0sIWaupVjjqV2OrIumtwWolPXTIY_1kTVxr6H65FrQhYkgpyK93hekyvGqK9erxj7NCREDFLIzaDpqssy28VKwm3LY7tNL0x49MVSejuo4JpgHEWqk6NYdNcXYvV3AUoZJjUnOD5b30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=OovQBk04tiRlTEX6KI9NO5RK0J-fquA8QdRrN7D6SCvEYO_r9f1riqBetfIoHTTzslQYlYwdn0WzNrYOHIK8CCYjrd9wYN_e7lIGbE2kD-9_zv8k80xF6YdiFg07W8q5ZPAbeO2usm_aNJaPw0OgQyav1H5zy2TwRj3LnkUIzVJxpI4-0RBwnm90RoKmj02dH7M2HZKKwEXqDc1zFnJkyrGHMqSLMssrxF8I-iXD_e2Der0ik--FCETdi5j9aSV5ZeGmPCVKqdCfvWIX9H8psQQnSEXjPoShbalHt2gpZWTr7NAOQmGZRt2l8azPBukJD3rx2Uql_VY01yJkaGsql6Edr48GTnC8Y-tsIopbac8CklzSfIT48_wz8ezta64TAXb45GNYpaq93wph6nxaTsudhgkRNqnAzPdkQj5tde7Hi3CyWoFAfY_5yCDy3htILfgfiLwJ_O58BUWTjhd6t_lfVz-JFwy2OuruFLcto6jmp4ZwmX_Yv-GVT7_mQposqjW0Ge0dVd8qV_UTI_mdWyx91gL-cC5ITHM3H9MChLOfiiFQj6Z2RhWUqxnMYZ53c5bA3R1y4_QFgrDmOMaC34qLLEoez48z-a0xmHJGGDRNy-DExgHN94ULMzs6Yx0DdMvRdGQHxU4YMi2w-4Dmxjk_qh4gWNrLqiAKzNB149M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=OovQBk04tiRlTEX6KI9NO5RK0J-fquA8QdRrN7D6SCvEYO_r9f1riqBetfIoHTTzslQYlYwdn0WzNrYOHIK8CCYjrd9wYN_e7lIGbE2kD-9_zv8k80xF6YdiFg07W8q5ZPAbeO2usm_aNJaPw0OgQyav1H5zy2TwRj3LnkUIzVJxpI4-0RBwnm90RoKmj02dH7M2HZKKwEXqDc1zFnJkyrGHMqSLMssrxF8I-iXD_e2Der0ik--FCETdi5j9aSV5ZeGmPCVKqdCfvWIX9H8psQQnSEXjPoShbalHt2gpZWTr7NAOQmGZRt2l8azPBukJD3rx2Uql_VY01yJkaGsql6Edr48GTnC8Y-tsIopbac8CklzSfIT48_wz8ezta64TAXb45GNYpaq93wph6nxaTsudhgkRNqnAzPdkQj5tde7Hi3CyWoFAfY_5yCDy3htILfgfiLwJ_O58BUWTjhd6t_lfVz-JFwy2OuruFLcto6jmp4ZwmX_Yv-GVT7_mQposqjW0Ge0dVd8qV_UTI_mdWyx91gL-cC5ITHM3H9MChLOfiiFQj6Z2RhWUqxnMYZ53c5bA3R1y4_QFgrDmOMaC34qLLEoez48z-a0xmHJGGDRNy-DExgHN94ULMzs6Yx0DdMvRdGQHxU4YMi2w-4Dmxjk_qh4gWNrLqiAKzNB149M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=DsFmpv2iYcymh5Fl0Bqxsnx9N19Jw7h6C6H9lQynefm3jHHN0bmb5mQ9dAxIdeLS4hZ313RBIUU6dYJkDhozY01bBF5aXLiUGM_8rt2TnAF4tm581PHap3_b1S2MZoAMRyck-Ms-S00VAyaXqut-gjIGndWVhSLozKHPGhI5TXIehuku-NrYWS_QwL4isTuvIlZyMeLRhdnLg-ieZQlaz0lqfR4gdzTfy_OOSpc9Sg6I-lgv8cdtJEAfHd5EfYJEYcnHVf6qrc6KaRa7-qTZE4DP_y3U0ldKZyLFv7aP90MujTq7Ga2mGdumuADwjNIdWupHK0znNPddmNM1nHSq3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=DsFmpv2iYcymh5Fl0Bqxsnx9N19Jw7h6C6H9lQynefm3jHHN0bmb5mQ9dAxIdeLS4hZ313RBIUU6dYJkDhozY01bBF5aXLiUGM_8rt2TnAF4tm581PHap3_b1S2MZoAMRyck-Ms-S00VAyaXqut-gjIGndWVhSLozKHPGhI5TXIehuku-NrYWS_QwL4isTuvIlZyMeLRhdnLg-ieZQlaz0lqfR4gdzTfy_OOSpc9Sg6I-lgv8cdtJEAfHd5EfYJEYcnHVf6qrc6KaRa7-qTZE4DP_y3U0ldKZyLFv7aP90MujTq7Ga2mGdumuADwjNIdWupHK0znNPddmNM1nHSq3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCp_CQmwY4CfcgPU8W8mFHhR9HQXahGSVIJNy4U8hsaPcXdTNH1CJogVeCs4c3EZdi_anxPPj5HCLEzDIhZqpkAs05mSpLT4ClAZogtt4HMuQQlPY-LLm4rNL-iu8j9Xr798f-qQoJf90BUfulHOXSmA0JXX-F_LnylkoGXMYbzoon0jJ8hAhqB4EORpaBtZJB0q80jx09GK0xiJVMRX-8kGLSTpFnyf-EOfxfbTbtlMA00An_8sMwrv5qG1lAxtk1TydbO5SLJw9k6u5UHbZmMozqE1dtYkwGMS0zBa5Z_5hVYRo20XoWWdvXS1DdQqc_UfCxGMte18TE-LEAgT_hmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCp_CQmwY4CfcgPU8W8mFHhR9HQXahGSVIJNy4U8hsaPcXdTNH1CJogVeCs4c3EZdi_anxPPj5HCLEzDIhZqpkAs05mSpLT4ClAZogtt4HMuQQlPY-LLm4rNL-iu8j9Xr798f-qQoJf90BUfulHOXSmA0JXX-F_LnylkoGXMYbzoon0jJ8hAhqB4EORpaBtZJB0q80jx09GK0xiJVMRX-8kGLSTpFnyf-EOfxfbTbtlMA00An_8sMwrv5qG1lAxtk1TydbO5SLJw9k6u5UHbZmMozqE1dtYkwGMS0zBa5Z_5hVYRo20XoWWdvXS1DdQqc_UfCxGMte18TE-LEAgT_hmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMutepz0K9zg2mVmQj-R_PomJrdMvy9STTita_kGKQIusbH_34KSWcb8ryxpx3vqfwQi9MhfS-6FkmQ7f-ryVHm2itrh-JNR2cWLxbi2OORVS17mi25bz0RnG0wUVC1zQmkTGxzXOTZ12w8s474BZAQ-fG5SU58AzE_9pH-WBAohzp_0wfwVbIjprIHD7b0XiQ4NxiXhh4Gi24iRRkyL05guHCZH_7ZhPBG0VMJjD4JnQNfq3UF_iHIxUhSd4DF4axAKSubgjn45qGO3vT6Edc4JRlBX2f4Ci4SYSo8xsHGgWFGRe4UI2E-s6q51G1qfKneedtPM4rjFi_SW4fN0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC6cdreV235tdayYF9-li-xTVDUopp8iHJQf4Q4C7JaK3mexkXpkJEPCBc-U4K-ymFoOdKoFQzfZg1qjxOZaltVR5oRfav6Ed2P-Z5MpxvV_JxDjRadDKJz36rtrt-hHiknSZunulJ8OFVkqg24V7zWEt-TCEdLZNaMG7BwxFr9zl_7L592c2QSwbv-lUa0JW4ksyhh24i1qVlK1l2MJCpOoCdP4xKdPvTlg_CBDFIkHbQ0LFySbGFfl284HoSXKcq1gX5Z2XdLSPINVmCQWIcJqWt0hSG5MQtQ7lt1SbMFzczu3BZCzV9-dwD20CK0PSUV3LuOMPGsD8qC2FIJJew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scpxAOVfqlM3ncO6cgU9AOY-tuUM4hRnXfLQkrj6ymBEX0PQII3EhikQrZeDDsxFTVMURREMcj-RI5tuftRkJVU1ERiDxiXoq2tShVI5mWrVotu8HImCYsxvuVxLCYTCxNzvknN9UZbwmzF6h31opUeIq2EKj3RMAGWlJ8NgM4VfQVqqmwyQnSG76p4pCG8F7aZmUEvyK37QaiWUN8I2kR_3pB4mS_svX-mnZLhWOnCWlJq4EwR0bzG3o-MxfzTe3kQ9LdGdiEUwtLWooycMEZKUN--9wO0Bk-3tVO6-Jwu1_4crggffm2DnXWe8va4RJpmbAVvxzq69x9bHscfvRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=OMNPmIQk-tXcx529YvJNrKd7krNTFMdqsMgBdJkiQLxgpUg0_lR-I6BQHd6EhUpVXEN4YY9d5qzbA2xdrhqlxZ214pJ-kC0vyuzQMai-UYpgYfR6YtFeAw4zC6sB1YOE6QADuRwfqibB27DqookiScnv0D_y_S0OwZwhOvp_mK_45cnc9fXHYrxNvgjURIITJ0PEqbPtg0r58R3c5SDJX1C7xDr2ZIXAAsvhNN6OPiRnMd1gU5S_3Rz0neT2uBVdz3BuC6QmTnbrnboxAZ5j75xRwPMJEy57Vxkk5bqdlP7V1wb4NgGwYxGjY-fm8MFgFof1R8diSdYt2k2r0QbFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=OMNPmIQk-tXcx529YvJNrKd7krNTFMdqsMgBdJkiQLxgpUg0_lR-I6BQHd6EhUpVXEN4YY9d5qzbA2xdrhqlxZ214pJ-kC0vyuzQMai-UYpgYfR6YtFeAw4zC6sB1YOE6QADuRwfqibB27DqookiScnv0D_y_S0OwZwhOvp_mK_45cnc9fXHYrxNvgjURIITJ0PEqbPtg0r58R3c5SDJX1C7xDr2ZIXAAsvhNN6OPiRnMd1gU5S_3Rz0neT2uBVdz3BuC6QmTnbrnboxAZ5j75xRwPMJEy57Vxkk5bqdlP7V1wb4NgGwYxGjY-fm8MFgFof1R8diSdYt2k2r0QbFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrhVJ4Id3i2MRw3booPyDnCjdcOF7m5VB0r5QKi-AnpAxVsdwnqN7T9pkDXzoqRkNrTUTHLAqYOvL5nI-7Tjbx8sT-7SxvS7gOdPFU0gTdpwLu9OZAmwNcnsrUyN-h9PP8FtlWgK0fhS6-QcebWVUFm3Y576goFjrkfWRJ0A93po88IJ1Ilmpsd7nqKkqOS4MZANsZ0cbschydEOF3Ir_c-S77XJ10fMWBCBOPT5dOXMnwJMo9sx5B1Xu5Jhrvfx_FAYM_LpO0nMEWaaEqRqdI7S3eTzbHYVzBYKZP01fKcIhjXTUFHGQ1tdHhd6v8J2sQ9xk0kk-1yQ3v4_uf1lgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeN9Co1V81jjSXfQprfIvEMD8o-cW-dkABpnZexy9kely1ROs5srck9OaVjc3kIi1jajFEZrZUHQLEvmd-IfmwPLbWRM7BHhtPR8z7p3VHYC-fF_YaHpCHTIzTVDJ8LTzHvz-D6KVXGZSNoMdZPqQl3T-P9FTkrtwUZ5skdxnyjpHO4f8PdEFVWWSAos2KIFs9bRT1019CSt5-lWUnQR1vp7ok06-U6lC6lOJeU4qzq1EHMHyohW8f_cKmfY0uNfjQmktflEL_aaA49skADCHf74ivBPw6zcFrkLm0fT05vfHTIiKLFDxeT28Ty2o0gBZI2XEegVjCkI4diyb0gmCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DR79HI4Q4UJaMzbAytWEC0iFs4Q2XP43Em09UPvMSBW6Bu536QMGfXEhn1z3MvKHwK4PXPiu33qRnGFeIbkxHxTKkIoL38UsPSbJJdjzEIP3Yfu2JUwDlSXuOK48OhuCIWwaUORR_Dzypv0lDsD_t5MsCmsQiJPl7lVSvuzx-xwEn-lSKfxK_9sJOLwqFnNN7FQ1CeQS1_Kj54BF9Y7I2bll_UKjgnaOrtn-XxuLZCs_uvL2H-tcaF4cABtM3cyidsEW2WtRrf_wcEvYXx4Umj6y7NK0WWxAz4eDsRt63vHWYCjJ_k6gET4poLZ4F8bvovjSIMZRcofgylfX_HP7pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkqWwu_CizTtr9xX8KKWnBrSAz1EgAptV2ML7_4DnD-FtptD-C0gPfKNd6pvJ622cbwagH0wcRC3Gdj7cqRsPVSOgqxpk01z-LkZ_oLqcSHlZyXY9gFiMH5ERetn9n9WZ63r9ZZJTaHQykKoJzr_GUiWHZ8l1wlan3OO7HfpIWFvDiKXAjNwGjJGYQn7hlffSDozTOPWnoE-kOOxMqGTO1EqXqJj8VwNaCN_D6GDUOMAtxlrz8valltwE4_ZQzSrBL50rr34swn8tTMlYkjlCQR7t9_OqqwwRKZD1R5uCT6DtJ2iEZGV34pwKiCQdOspf8zS0oZJxI37QZWXgEw48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=MNv8mMwK_c_CcSYSOmtJyy2w9IE77RVe-OXHkKcHia3-fF0BwV0RpStqbhathyxyAKjRYCxeM-Ti2zsXVNqHzlJIm--d4UBSUTBpjNBuqN3oths5gEEByTrPgjNVgvR-7vhKrCwptdnnQF332wZ6MAeYwwt8w0zcvdByg2eJ-jcy7bXg-BZq2FNkUBMEv9b6j-Ac3gienzYWAfmykM52QhR1-ynugNXDb1kh0l3WHxwFxUt_2D1fVihJSx51fmEHTC_AEZSvKOepROQHLOuDcnKMWJcCqNGfsJqFnRZw_7G9O-gOO9KeUIGncqNl4cK-nS_pmuJHtMBvrYf0uiAz8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=MNv8mMwK_c_CcSYSOmtJyy2w9IE77RVe-OXHkKcHia3-fF0BwV0RpStqbhathyxyAKjRYCxeM-Ti2zsXVNqHzlJIm--d4UBSUTBpjNBuqN3oths5gEEByTrPgjNVgvR-7vhKrCwptdnnQF332wZ6MAeYwwt8w0zcvdByg2eJ-jcy7bXg-BZq2FNkUBMEv9b6j-Ac3gienzYWAfmykM52QhR1-ynugNXDb1kh0l3WHxwFxUt_2D1fVihJSx51fmEHTC_AEZSvKOepROQHLOuDcnKMWJcCqNGfsJqFnRZw_7G9O-gOO9KeUIGncqNl4cK-nS_pmuJHtMBvrYf0uiAz8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=HwKKytl34JlHYxK8jEWOrC2addxtSlbW1N2oE47fvaoD-iVlV2RiryJX0fN2BleCca3C0lRVSCp8V2k9jYXsjCzuJl8XmMZMl6SfZF9MuoM7Ho35jNRkkTu-4msLqgtJ6v7Lz5imGRz5JGCfwRHY3AZm93u951HxoOLT-BcMVi4gVDCCB4f0V8ljgC6XueFRgBRv4prjpyfhB9vJfHpJ4nQvfviQDi3nLwt9TKT8CELRoZMnPMouV1AHzVlLlB9z1UGmXhmcql4fijY76hFz9EtCop7vn77NfXM_4jVKY4rhK35N1iFvM0VOuEgsGUX3FPhopI_NY7gCZ4va2B7bKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=HwKKytl34JlHYxK8jEWOrC2addxtSlbW1N2oE47fvaoD-iVlV2RiryJX0fN2BleCca3C0lRVSCp8V2k9jYXsjCzuJl8XmMZMl6SfZF9MuoM7Ho35jNRkkTu-4msLqgtJ6v7Lz5imGRz5JGCfwRHY3AZm93u951HxoOLT-BcMVi4gVDCCB4f0V8ljgC6XueFRgBRv4prjpyfhB9vJfHpJ4nQvfviQDi3nLwt9TKT8CELRoZMnPMouV1AHzVlLlB9z1UGmXhmcql4fijY76hFz9EtCop7vn77NfXM_4jVKY4rhK35N1iFvM0VOuEgsGUX3FPhopI_NY7gCZ4va2B7bKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=UprPO67yGd4q9qpzssuul6lw3LgOGJXG5sLBBAPa5x2nOWYOxsARVDVJajvVMXORv_iNJ2kypqAzKCtVPxK3lqdp8G9lAYe4GA8ErNwrGZjY0yXs-NhuccLCH5AMYw9t9koGp2X0j4eTXquIceWKlsMQxcpc998JeirRFoixq3nzaICkFdr6YZxffzUs-Z8BVuV7ji7HAfYsiEKU0euVrl2CK-3SP0eZVrF4cmNcrdPEAWZA_XS024quahrXxfiPnblP-j89YC2mXTjoT6Em753BniKMDjSjA2KPaIspT9fNAd4coaE72aUN6N3TVt6gvD2VTWMpOtlu_pu5ZgFS1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=UprPO67yGd4q9qpzssuul6lw3LgOGJXG5sLBBAPa5x2nOWYOxsARVDVJajvVMXORv_iNJ2kypqAzKCtVPxK3lqdp8G9lAYe4GA8ErNwrGZjY0yXs-NhuccLCH5AMYw9t9koGp2X0j4eTXquIceWKlsMQxcpc998JeirRFoixq3nzaICkFdr6YZxffzUs-Z8BVuV7ji7HAfYsiEKU0euVrl2CK-3SP0eZVrF4cmNcrdPEAWZA_XS024quahrXxfiPnblP-j89YC2mXTjoT6Em753BniKMDjSjA2KPaIspT9fNAd4coaE72aUN6N3TVt6gvD2VTWMpOtlu_pu5ZgFS1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIJtEp7jkR5BZCY_8p4D9c-SXdSFQm5Kz7c-r4iom71sVCUnCJNAX2Dy_-KLhttLiM9J3VeHv3cQCA-dsPtArG81rAv4BaLrq0uFanXz4YOdozHYC5jAlBESRvh1b5IbHbSUpJeuo4TRPu6HPkyGLNbmdaujPbuBwV7WJaR34yU4laenBB8P_tN2VON2XTj3r70f9bJ6LUmfTF-Cfk2YpgE5VKIcjgakq9_-1T_hqtc2kGLz7tKMV1jqcyj1pUyO8K3P6EGUwg3btbeCzQfnfun9L5-2U6fYAPXuaU6Ut7D2s7iNJzQFCkh1L6nipa5R24luLC1-oSX3Y7VUIlDHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Udnj8A6iCeiDSR92w7_x5HAdpQ9gXYLhjT3xLWalcdGSMj38uGp2Fjx4FzVJTs5PQTWKX2owSadUw9meeVp8IYde2fxfwWLF1tdkhUEtzf7yqYZ0TnSYQfmee6x9m2aO8k7U6EOPnwF4Y4JmyCvuaXeIH-kaIRPMtGQmMnafuzWzu2_bRExKe7Sv82kihY4duJ_SToArVbeWNK9oXyAYhuw5HWOW55X5reiZmpPxwO-FapTwA-dgUZlWl48TZsiWy8GHFZ-H9gsSlk59e-2NiqNibzy2rIaXsvf65f4ZVL-HqwfBVPJrQDpYEgErN8Xk8BHyIlYhOvnkEktPYRikoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=Udnj8A6iCeiDSR92w7_x5HAdpQ9gXYLhjT3xLWalcdGSMj38uGp2Fjx4FzVJTs5PQTWKX2owSadUw9meeVp8IYde2fxfwWLF1tdkhUEtzf7yqYZ0TnSYQfmee6x9m2aO8k7U6EOPnwF4Y4JmyCvuaXeIH-kaIRPMtGQmMnafuzWzu2_bRExKe7Sv82kihY4duJ_SToArVbeWNK9oXyAYhuw5HWOW55X5reiZmpPxwO-FapTwA-dgUZlWl48TZsiWy8GHFZ-H9gsSlk59e-2NiqNibzy2rIaXsvf65f4ZVL-HqwfBVPJrQDpYEgErN8Xk8BHyIlYhOvnkEktPYRikoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=FH8Ntmb1kQBXvbUbzskoTPkDxl7U5hvl79agD3D-cOI1PH1wtmqELZqTyyHMkeKDB6IRWFhdRhpOVmuTENGYp-Qje2hIK_NozDCLqSxm9HWuGnYuqhheqw1H_KWHdgMjBHwT0ogIx1V4B0O-4Cpa6lgTpz7hmqG7XmRz0xEkVIu0D3zRL4_XjHWsRYWMlik3sZ9JGVy2Cp8mJwcGVK8i7oDJYzmEGUWSlG_mXxJ6b4eUlkrCqo4RBRtZHhs-hB8AeGiTic3T_QkdhHdvSOOiwBk7iaLLBKH7fsSxm9-M6Q7OKz4Ag3atxz5ksjJ-ADp4zK9ZV8KXGvIqqAmTiuIcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=FH8Ntmb1kQBXvbUbzskoTPkDxl7U5hvl79agD3D-cOI1PH1wtmqELZqTyyHMkeKDB6IRWFhdRhpOVmuTENGYp-Qje2hIK_NozDCLqSxm9HWuGnYuqhheqw1H_KWHdgMjBHwT0ogIx1V4B0O-4Cpa6lgTpz7hmqG7XmRz0xEkVIu0D3zRL4_XjHWsRYWMlik3sZ9JGVy2Cp8mJwcGVK8i7oDJYzmEGUWSlG_mXxJ6b4eUlkrCqo4RBRtZHhs-hB8AeGiTic3T_QkdhHdvSOOiwBk7iaLLBKH7fsSxm9-M6Q7OKz4Ag3atxz5ksjJ-ADp4zK9ZV8KXGvIqqAmTiuIcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=uvhM7K4edcyUByEDRE6f2WBSO33diDy1adaUUGoAxRdkou9XJWKBQ3w1g_FxxwXNA9u2IzP5B3cLetG1WhwiO3PY_BhSAMwy_YbzXQwDTThfbm2LCtAGrHuSrwvvyX3da6gmUMDdjRx-D5AqprrtcMabKYcgPeSsoNdlERpSG0FG_b-sk5xNBpRpZDieVgtIB5NOIHRSuf06yn4rVS_bGpmHHn52VRLpCs0hy7_wsFDdy_scdyn4TEut2zU3Zt5XVs7vzAA8YAfMiKv4TKXjujhp9QGzLiqUPX3lmt6Qns76ZD9ik1j3hAwRX-j7O61wNV2fIaO41Ysr0k-9a1RQPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=uvhM7K4edcyUByEDRE6f2WBSO33diDy1adaUUGoAxRdkou9XJWKBQ3w1g_FxxwXNA9u2IzP5B3cLetG1WhwiO3PY_BhSAMwy_YbzXQwDTThfbm2LCtAGrHuSrwvvyX3da6gmUMDdjRx-D5AqprrtcMabKYcgPeSsoNdlERpSG0FG_b-sk5xNBpRpZDieVgtIB5NOIHRSuf06yn4rVS_bGpmHHn52VRLpCs0hy7_wsFDdy_scdyn4TEut2zU3Zt5XVs7vzAA8YAfMiKv4TKXjujhp9QGzLiqUPX3lmt6Qns76ZD9ik1j3hAwRX-j7O61wNV2fIaO41Ysr0k-9a1RQPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=YwL4ClE5FgvhuEr3daio9fJcV8CldP9Q8togYpesj27RiBU6uBj23LoEOQBk5BkBkHkbTWvfciEFnY8Dgrdb08a8tuG2wnODh2ceSGWMgFzDnAffn2YKtdWX42E0CMD-e7qKFg6NlK-z1kFf-bCTFtfdIoUa04DJ-kh45yNUtGI15s00w16aFmh79pGxQqCXVF7KOTnEzrw1qGLVXrcLgILrHNcaJ73yPqS_6axh2MaPH9E4NQj8C4842FUO4-oa5_4zc1Kzgf5v_TG9fXn8YCJnbPH8MTnJL3Mj-RComZN-AFESu2cl6tSy7WSz75Zd_lmW2urdIVtBs1UWLtP26JfsUkGcwZWuVaWOk54NsYPUbxCLbElnRGVDWbgLIoM0_tKs7AOyRipaFVF0uphQfVfp6HmwOQort_K86rwRAWst4QBqH5amQdi7PsEaPPDRPSMDNrP_qQ7QN-NqDmDMoREQF6qBMl1_ULy3z27ajaxzRbP6XxGTbWU0Z1Yb3f3QRy01E732gESWXZOP3Q1GdcT6KZESoJy-E1RpjV-L4EUzIabW-stYhasaXF-4KwRUWU4xEeIJ_YoiOelsmJu1gzZC2pPcrya5Ptrxo52kaAwdJvv25YBdYmE1pFyE6cJD1cFJkniNLVmXdu5QL3diLN0TMJaGipm0ztd6aNkV5to" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=YwL4ClE5FgvhuEr3daio9fJcV8CldP9Q8togYpesj27RiBU6uBj23LoEOQBk5BkBkHkbTWvfciEFnY8Dgrdb08a8tuG2wnODh2ceSGWMgFzDnAffn2YKtdWX42E0CMD-e7qKFg6NlK-z1kFf-bCTFtfdIoUa04DJ-kh45yNUtGI15s00w16aFmh79pGxQqCXVF7KOTnEzrw1qGLVXrcLgILrHNcaJ73yPqS_6axh2MaPH9E4NQj8C4842FUO4-oa5_4zc1Kzgf5v_TG9fXn8YCJnbPH8MTnJL3Mj-RComZN-AFESu2cl6tSy7WSz75Zd_lmW2urdIVtBs1UWLtP26JfsUkGcwZWuVaWOk54NsYPUbxCLbElnRGVDWbgLIoM0_tKs7AOyRipaFVF0uphQfVfp6HmwOQort_K86rwRAWst4QBqH5amQdi7PsEaPPDRPSMDNrP_qQ7QN-NqDmDMoREQF6qBMl1_ULy3z27ajaxzRbP6XxGTbWU0Z1Yb3f3QRy01E732gESWXZOP3Q1GdcT6KZESoJy-E1RpjV-L4EUzIabW-stYhasaXF-4KwRUWU4xEeIJ_YoiOelsmJu1gzZC2pPcrya5Ptrxo52kaAwdJvv25YBdYmE1pFyE6cJD1cFJkniNLVmXdu5QL3diLN0TMJaGipm0ztd6aNkV5to" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=tGJyQkv9Lf_-rfNv6N62LydnTbPmYIVp3ZqqQortvFZT6Ree628ncpg1g98dYtlIuzhyNCmHVF8IcUidSMc-MU6b6-Fncv2-uux_fGEyIJcER2FeoIMzx3-TudsLjuduvKk_PLcK9vGZdYcQ1b-j92kPQp71qZTKXTJ1jVdtj6ZJH9hmeBQZhLHZw1DDf0RQRYPAgBPugHTZHvm8AyuGFmMghqt2-JIhGmpNuOj6HCjpp4jZcd5yFYw6FFFVF-yOwVq_3dBhhuWnEHr2uoqLOVgX-k2VDcNxFbr7D5CQ0u4glPhe5f21P3bvd5OhQisYeh_xLp80Y3Hhg8iQbXLBrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=tGJyQkv9Lf_-rfNv6N62LydnTbPmYIVp3ZqqQortvFZT6Ree628ncpg1g98dYtlIuzhyNCmHVF8IcUidSMc-MU6b6-Fncv2-uux_fGEyIJcER2FeoIMzx3-TudsLjuduvKk_PLcK9vGZdYcQ1b-j92kPQp71qZTKXTJ1jVdtj6ZJH9hmeBQZhLHZw1DDf0RQRYPAgBPugHTZHvm8AyuGFmMghqt2-JIhGmpNuOj6HCjpp4jZcd5yFYw6FFFVF-yOwVq_3dBhhuWnEHr2uoqLOVgX-k2VDcNxFbr7D5CQ0u4glPhe5f21P3bvd5OhQisYeh_xLp80Y3Hhg8iQbXLBrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=sazqIXGv0V_Fndl6jzemJfqXiyzCr5nOJrOW-CQfvMIpfSwUqx9LMHGoE-A9WPPMPIWZpOiY0ggsPiNQzqu6OAKnTw0jGGUEagRo9flGEfs8HQA5hYFP80MNcoJgNsi0znPZOzlVNwwEDY9PJFli_Gq1tdf8Jn4tRyfGaA1TjTfFsCyDDLT4oHL3FGry1mZ7zRNUSH2qjPWTcVcZzPMxV9QQpyhk-r4GNk-5weXJ5HmFhVseG5vgeVSs2dRYj9vG6ifoVkVFhibCLsyo2OCqNFwcd2hPgMk8EQFOByCji5PXGY0Kh7n3HL4FgEoDI0LVSAknNv6mLzW5gvEWS2kToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=sazqIXGv0V_Fndl6jzemJfqXiyzCr5nOJrOW-CQfvMIpfSwUqx9LMHGoE-A9WPPMPIWZpOiY0ggsPiNQzqu6OAKnTw0jGGUEagRo9flGEfs8HQA5hYFP80MNcoJgNsi0znPZOzlVNwwEDY9PJFli_Gq1tdf8Jn4tRyfGaA1TjTfFsCyDDLT4oHL3FGry1mZ7zRNUSH2qjPWTcVcZzPMxV9QQpyhk-r4GNk-5weXJ5HmFhVseG5vgeVSs2dRYj9vG6ifoVkVFhibCLsyo2OCqNFwcd2hPgMk8EQFOByCji5PXGY0Kh7n3HL4FgEoDI0LVSAknNv6mLzW5gvEWS2kToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoSBRoMuq06OnVyszDSvYvyuSUCFj-2JaXuYl0SfGxFth0EyM45oT7QMYOdkrzzkfQyJaEbeNE_je7xZSp9vRVDX9TYUcqhKR7yzWmsxPBx2Ucd3onCbEmwDRidEudrEIJsr4N2_MDNLHFoAsWdYntciuwNBMZsIX_oedXhHxXlua-GEFUUIasAyeHAtaxLJltdXEzSGq2qorN4BhGDwOxVfSNej0wxNhqidl0HG1nrv0yD7RVh9B_0UNsBcAFD5XL71FQW6eVINCAUHKvaNErsgxo32309ytyuPr8jLis88wERi5LtiwEsQQFKBI6taLorUOPa4Uom5Ifft6NJcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW0drloRpMfNuv66Iz8wQUgbBWJrkdyTyofiVcKS4jTTHKQhNdQYYOmS2XeNIda7g99eJpfCjfuiMBX_JqGNRKcT5LV7QbkPtPEdWpCjPHt4Dffkdtn4ZnfhYp7unf1RVQztRVyJcC_wAclWeHhI8VVaud40wrwMZxn6GekZx3Tx-IqtBTq_qqXWflhDql3e3Ac_eZJ6dVAecTJlY7D60MlDUMmCNzasU86kcHv8NUJgeqFApzEiHywn5EefK6AnlkefT6Xgg7Mtf8L0WoCijBr982LPKenbX0PTLA3UsnmeMkj4nJEtpBZGEppHRvwR_0VvDFDrjRe-kp5NtpN5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Jt9OsiMheEMjIjaEqbu3hkcJMYDgVJ-bjECBiHz4F-lCF_Kj1ICQbiXYqRNYIv2cd2DVxVOp6YPbgkbGtYEo19X9bsN6lYjqXsNFsT70cImR59TCiJyyJ3fOOvagaO8ZIVHEgIE8ZNMMg-5nojMUPy6KvPzS9OH1Qj6JQXGQx28ZtiM9aDd5SkN7v-GVXv8HJcoom7xXlaWoEfs9mpQ1tBY1Swoa5c2m_tfOOuQq0M9SLhaf4ujMGQRIxBle9cXG4v9MUqRhtWKKaVvMoyvrQ8TMH9rqNdspx8aFLSIcsFICWRESavBMFQtlEqGivr4dxyL_2WufxncE_GRkgqhy6nGjwy27Z75_DkWwtHOQwoLcOv1XLdpNk3CyXf3WWmn4b9vOgXfWptRl9myUQlcTDYhwjBusFEZ8oCEydPu983qpGgblNuEdfQ7j-9z5IFxKYZhgRwtRKOtwzZAjktkwoPUzfaACQiUDWAFf1jbU8hM9rOKpnISa1OlrSIC6xPU9kC8n7TMUkAjfFDdXYKDKTW_bxXe61s20gKOaJKVVPid12daHztVeLUPvbYxE9YHdygkfpg0da8RIn2iZY4UxcOdv4G4cYWZfo6wQ_6XGF-hHCvCR_Psumrr5qkNcafc_n17yvF3rK0TskJDIMx1Nk8VL6IjeLuLMU8M9cD6Zs18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Jt9OsiMheEMjIjaEqbu3hkcJMYDgVJ-bjECBiHz4F-lCF_Kj1ICQbiXYqRNYIv2cd2DVxVOp6YPbgkbGtYEo19X9bsN6lYjqXsNFsT70cImR59TCiJyyJ3fOOvagaO8ZIVHEgIE8ZNMMg-5nojMUPy6KvPzS9OH1Qj6JQXGQx28ZtiM9aDd5SkN7v-GVXv8HJcoom7xXlaWoEfs9mpQ1tBY1Swoa5c2m_tfOOuQq0M9SLhaf4ujMGQRIxBle9cXG4v9MUqRhtWKKaVvMoyvrQ8TMH9rqNdspx8aFLSIcsFICWRESavBMFQtlEqGivr4dxyL_2WufxncE_GRkgqhy6nGjwy27Z75_DkWwtHOQwoLcOv1XLdpNk3CyXf3WWmn4b9vOgXfWptRl9myUQlcTDYhwjBusFEZ8oCEydPu983qpGgblNuEdfQ7j-9z5IFxKYZhgRwtRKOtwzZAjktkwoPUzfaACQiUDWAFf1jbU8hM9rOKpnISa1OlrSIC6xPU9kC8n7TMUkAjfFDdXYKDKTW_bxXe61s20gKOaJKVVPid12daHztVeLUPvbYxE9YHdygkfpg0da8RIn2iZY4UxcOdv4G4cYWZfo6wQ_6XGF-hHCvCR_Psumrr5qkNcafc_n17yvF3rK0TskJDIMx1Nk8VL6IjeLuLMU8M9cD6Zs18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbFulbrW-7FR4xa7MKk93iqBjQ8yV28-aUwYeaxiifwY1nI5gexttfpR_V5imXn-LU5Oi8_kFvHxpRz7owgzWCbOcgPXsJIpi1Z5cwcy9t4YbXgio8AH02Vz_DyRG8rJvKXEOSEctiwmzD2fLbF8GaNtSsvJMEwYhu93NiU4vN3a68Ox7ueBzvHV23RjxDDRU-9VaP2OAS9UeAUBPJUsvELrKvgasX_r5FonBMJ51W_IfGnopbOjwzLxh3Sdn2puKWqwhwhxb4CGPjvyP67Em69VLjKz5PnxkyECean8IKYPnXS3e2rw-q-A7LLP4ltL_lUCvnnYzaywkMQ02Brizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi61fWBS5yJKtmHz-8uxXrBOLEHeyjnW_ZBfFN8C6B6ADlPr6EmqUrhMdRLOKbsm9nmNer0PjQHqIqAhrVDBzsyuBVaPRtAGI8eLWkH3okwL-nCOo0woziwnajlfc8JYZEL9HlNy4bEENdapaVYqjn9njkfq4oAoaE5qew3rJuIDrSrRJaPfwl_-N4gspNpa8VBxMDcXBFgs7sjhO6FfUklq7Gj1Y64JHHTpZ5uwoXTrn2GkrS1tsR2xVw22VKfmjNWYu-ATsbDKi4HZMke1sMNzu47SfBb1GAPoDg6k_Sbz8h2LLr48YpyP7LshBK8OlMAvnXDlr_4tuYQawn6-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rg99mCstt6q8SFfZMbZxqvqDziBrUVactjn2vh3GNWhASR6GcHniUELHJaVCBmGj7dDN7w1pfL-LSITauL2_stnaksrOnlLiAAuRkQkZhuYT1wIscTQXCaSyjrNhvdCyteSlWrg9B8vDki8VHWWRkYWEy2Y4oiR2vYVbo3dQ_tjImOcUUfRyj4poAJDNVM0seo8qqPaAfpGQfrb-tknUMnMKDGXKJ6-XE-DKYVJ0Le6bLUavJxRjQo2PayVO_cgsw_AIty-lE0JDnveJCmvCxLbISoeaY1-F3o4polV3EnLxgWOY5xRCfMNoDkbo5poXCEO-LDGmcN2mSS5F-X0JiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLmF6nRV781n2rz25He9HzHjPqi_AxGfAbLwnMpHDgtgaAEVeyyqLKUDGrPbbhacdZAPBSJTj-ItNl6mafgndJE4uyntVPHFsBetoR6smq9vFF6-ltvnQPkQFTH_DLHdB0CdJ58naV2RPtylb9Kf9vRNzoU6_A_Wk22rCcx6C8SksVVifiIlyXWizZiF-TAcH3eZIwHWP2B_w_l83H6ay116rF8EJHGSXaBDa-K4o8iQJXChStinlaxNiDDXguGB7kaxDIyaZaFa5P2HEcTSHWACgh0spdyMXhEoMZmfpP9D7J0EjImf6Hn-7j5JZv15iWuiPjo5yx_9uRB7YEstIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=gzP4e1iNN_qU9DTt8j3acLxKnpUMhLhJ7gbDy5N7lKLfLpQJpBrM8m2vI1m7dslmOg548kvDdkqmQE8G6W2V-z_3QMt64y25BLdzQpq_Z-FsK6ymu42AAn3eWxkonRsEqZ_AI5RFhlrQ_7CHfflanj27KDlItoHX1hEF2Qb8LhqxNdJzWTWb6OqMa-XsDaLeESBeOOzFSYqPAF1YzqKXp9QDXeZET1F4elZXvY7WzRfYvZzkrXWxxv_3eS83FPlorDAq-C2sYZUBAUFYWBVE3lUQaS9XI8kEjfWOMlUW9_5fo8KU56lVjdiHSxg4Xmr5Sd8qaYxPqyTuElRBD06wzQLpd-QBbZ-GlNb9MsZKNfWbMCkJEzX5XTbkeaF7OJnqr6z6R0x0pkYuJkfT06VsARheqQpYCK-fLgygJZ-4kz2pIigPFSjj2A-y0BSeStZr8S18w_RJRRIrXtAYXTGInIhPQbDT3-sbtW8XGpnIraU6FyJe7xYGIg0EqnyrhjKasHfft7sccrqjIYynbVdY-0ip3RXJPJouTXVmUbxPZx1_-zPqS5nhqgR6xj00PhM-unYjBcXt17SPLXmBFuBZPvjh4DgcOaiuAb-IbC9Zs4cdxz30CuPvi_cvpMoQ3-_BXe8mptiOBSIdDq4S83W9liggHiwgBe35E47mSkEWFZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=gzP4e1iNN_qU9DTt8j3acLxKnpUMhLhJ7gbDy5N7lKLfLpQJpBrM8m2vI1m7dslmOg548kvDdkqmQE8G6W2V-z_3QMt64y25BLdzQpq_Z-FsK6ymu42AAn3eWxkonRsEqZ_AI5RFhlrQ_7CHfflanj27KDlItoHX1hEF2Qb8LhqxNdJzWTWb6OqMa-XsDaLeESBeOOzFSYqPAF1YzqKXp9QDXeZET1F4elZXvY7WzRfYvZzkrXWxxv_3eS83FPlorDAq-C2sYZUBAUFYWBVE3lUQaS9XI8kEjfWOMlUW9_5fo8KU56lVjdiHSxg4Xmr5Sd8qaYxPqyTuElRBD06wzQLpd-QBbZ-GlNb9MsZKNfWbMCkJEzX5XTbkeaF7OJnqr6z6R0x0pkYuJkfT06VsARheqQpYCK-fLgygJZ-4kz2pIigPFSjj2A-y0BSeStZr8S18w_RJRRIrXtAYXTGInIhPQbDT3-sbtW8XGpnIraU6FyJe7xYGIg0EqnyrhjKasHfft7sccrqjIYynbVdY-0ip3RXJPJouTXVmUbxPZx1_-zPqS5nhqgR6xj00PhM-unYjBcXt17SPLXmBFuBZPvjh4DgcOaiuAb-IbC9Zs4cdxz30CuPvi_cvpMoQ3-_BXe8mptiOBSIdDq4S83W9liggHiwgBe35E47mSkEWFZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
