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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 20:45:13</div>
<hr>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkx454vvoBkL2QCkWSqTFWzq67WIq0x80NQ5OAMjJizy9zdo-o4J1-CKcsY0AZN0sf63sIk9pv6b6WyOlAijamLUwzjcwT_wgrUxZfZzqQxT5lRSwxiesY1Oqegq1DuWX5ILLqyc6KJl7dgut9HleURDl6AEmTgaPKTCQZ1NUPzxZ2zLMy1nHOaSRXaL_yezxMLD16op68m1hF8BERYJR_M_VlKM6yjCsvxVGPdmTkEp_YxOorbiHyA39fVroBmYzzH_dBIcM4lJ2xoyapfLiQEEILG6P8I3CsxD5X3dVsbHRkw3JuQNR_Y2yA07oNl-xTHzoqHvMVD5E0O1VhUXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A91kuYO3TzFrjuaNItoqYRpI5zEzGD4PwHzr04UI1lm9DiEwsKTeG_6kG02R2RCwwOmP0h168EzxOmeE7cwT2zvl4eZtSvxb2-o9zZd9dFsDE9ka0FPGI63mHUAqTNWcYYv-bkcMWr4VWrqXpkzcOdZubFXk0Zd5jWChMiDZo5_Ykg9w1Lp9bkIxYfPNRwVWlSmA40B-psnGM0OVXtI3YCRTm3DXsqwoGBFhGncgp3EyLDOe8dFiX2HEoQmD4YviNHFOWsGw5hYZe5ZAYQo6jAHfvbdBigLD5TCaYbAl9ovy-nBTbuPqVXNthWX0n7G5oSPfsKz8FgleIxWnhYbbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edDV9CjvDEqt0FpOCHD_yBMDypzmgXqWDY6dm2flpjbY66GvUL4sQSAyT3XYf8jk0beJZo-zX0dyZV818M6lxpZaAVMpjaK5cSjIzTimwOMvAl6FjMhBVPDCsROKEw4lITOYG6pfAxO-n5f4IP9JkXRt3yE_UrRjUqWMRc9EgERWhoKikDsN7ErGvFJqz2EQQvYoGHtiEYo7Ffpbe6NwDDk-8Cux1Fp9OkuJtYCF8iFDqdPRjgtwoc4CgP3fc_7_16dFtsZ-Wpv8SPuEntbB2OnohSG3WS67R6Xlz6QKF74CxWkraJ9hCNDHxQE4xM9BgfVQ9H1Mf5VfHnURQI69lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEgMOSHveFO1xJ4gaGdBP0WhAis7h53aEUtzooS6oZsV5BWmFapNHX5_q8raGiGFQgCNJ-t21nnuYkojlkvIDFL6fbCtNWF_oWtlr5BPhsrEamfepi-_ROQHb-BF0QdOAZKhyWnFUaLVnFIQVL54n1MFatBqWE7VosQ7LbnX7VORu9NAfcvu41FJ0YpuFsCoWRYo72zV4QkE5qgrPA57lUV_D8RmwNMmlfBocJMYeeCunRHitTslXVOLltk_7xu8jkVUepKElX3CuCnHev6ZKqdC6Hcm71Hq1jOaCqr1kSYtb52zbkcqXabLKsRR5NwJcrRgXSfxuZEYAJ1da8Hhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYumfGHS-Y_3QGZ85L7Gu14AFl3hTRwMGwG53LLZwtBhQ-KgUbe3Pcp5P5WJyX2bz2jI8tPDq0LKKu6Gg8e12JkVYQeQPjXjQgcBJrypWby7nZPgTbtZK1Jf1iFJigHkhzlO6wxm_T7zg6RhmWtWEVqZaLpY3cW5hQ91LpvGVgwE419eX9y2BjqhD1waB1vwloEflQx80aFNFRfuslbumWePQTrhZbljUt-QpEmnCMhzvduM8nyVbVZLKjQXnlzny2gpEiVdEkrpkH2p8DI1b3jva9lE0DN4AlGLVsC1Jydw7-ibX6aGSLTbsYfUvRPTsykITrGQhqCoojetdxYR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JuvsaBXI1A_3WIhkX9tk1nKyzrG8czM2cnKr4qOd4z_y_sY4JDzpoFciPB8Bs7uTIWAdJd802D3FYQroiNOWiG3nSeVXQ5RMh_qXCgKPD7WBC8rbctR_ZGoVfXdgJe-rT6_jr5a4ylCC34lknA6ap1oIDfLoGKK7VIAw2yfAMfYpPnb1aFbnry1tXU3q5C04Rg06RBJLUOmNqyGirZ7DB4vYtq5PrVBoQtXPJ_y6styLucR8cHdOmKquWWEXt5wO-1pOIN8jC6gZF9KtO2R8zxXXYIClhOhQ5tmawd67-abnySHcHLUT3WSaFZv2soqTYd_DnMlcxiw6jBhscKQLuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZuXqOBFP_2-inFI6Z40FNeb6XZ47ozNM6kM9h7ILIhTrImu4Ig3OwLeJbEQEPE-qsfOY3lkoXWEkAXns037w8kkAJil9SVrmAlIuwq8XsYxMTkbgVdR6i2DWRmEk_hfHgE-OH1ihjfss52LGKRwe8mtILh5g6LDEwr_yy8fdcdpnVHkrcXKKtFN_yQumoqe4x96HfsvkhzntKmi6aI-xG7SYVQ501IDAthzI9VFqtaV-ILSyvRy31ubZ7rAGqje73PPpYif0ORX3qwR8ZUAr4B01lP02UYSMwbMn06n21UOfFbRRhbPPUlCMd31v8PUptQFtTzh5lXpDOJUwoWN3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KIwj-Sszbv2i91Ymftnyr06d4YbmVopDexWkPYmSA5aPHqfOZBZ8AldLyBihiWJBqHzJCJXBHVxR0rD-urn21QHw5uJ7v_tvxaF2Bt4FOpG5577HqtTgVKT-Dma8ITNmvUIXzvQSd8TIr_6FXq_MkHg1qJgO0WftIxQpnYjvrG7EecusyNj3Uulm-vKYEtCUYuNYJBbeSWhr9ntCA6ArNCIPWCcoHFQhIgsuzqfOeMVtG0JdcAMOsZ7fy-BYCayu7FR2OgdHF5SmpdeYJqrruPlhYCx7YagOjDWsCT0XSCzQzHwqsYcvJzJoOLwSUrnxsJtAVG1fvtC4lGj0DSWIhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7EDUsXNbb-mM4WE-YtSwStfWjeC5Qi7pvc87MSUhJ6C0uWng80hJoFKL-WKcxw5A1prIIZa-5BVitK6db_glsTp7MxNcbHmkxHOxaStwft2Iv0jzt2cwSnqyZ3MXthaoEQ83aHmSZO74DVa6pA3eWzc88sxpsdn5oRE2EWDpBJ1VX7tTz6_sImAhGEakee6S-S_025tNdN7aUMpoYFnrhJM1FdiD_IBXZmXY3YXRRxq2_1_1uPhtTi6kbyZJT8542lYfVLvy-YepEmkwt6bFW2h0YDbNJ1Hb7H_XD1XyD8oeCRpkzWjxnls4q5NYW0r2NzTosx4cowXkrb9xD-KRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IskluEaENewhTtYZiOv-0tTiWCN8z5gY5YPW3VqGAPyrbDa5HfV6ZNHS_h852oOtrJrDb7P07TNFOAvuzwxARyyHp2ch5kkD3qFhuBL-_k6OFQx1QMaIuH6PN5PkyB3L4eiwk1dE2ArLh2OdNRCEGFMO1tza7CitlOTVrdvY4gvHYmQqJwIvonra9iaWaKdYE217uVNMBz-asQ2OMmVdktWlBV3FtUlwBIASOv20qt1PaMQ1ODbrCzgUlbGi32RK6wZ-Cp6ZxFlKLOx7w9qAKR3vO8jrtH5InLYK8WccBwFtRNUj8SjU94XmJqKycrBkQ1HT14Nnda-x0HeisOmtbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4WWlBDb9thHJOZ5rWxxAv5kVzhiUHylLLkgG40CFirbzXye2Kb1X9V20QK00aeTRjzLzPPo7Yy2qPkg_NyA_zbZAgE3mj34xN-5pJRKf16NErXIHR7YvmOKwTm-FDlQRQd3gmYZVho9Yl9AeDEa7aXiiZHddLyEqEJpljYq497-mpmF3TBPIBQ9DqWobA1bSyYPO71jvkY5FxcdqVsD0eYOqMIGohcrNOVmqrmbQ-PRGvIhbirKcS9UFuArjIeBWryqel6aCCT5007UcNvhu1CizsNrmW60-w1MD6_JzUxFxBw7LHne-KAR-EXbs5ijoUpiCWVMyW6JR2IBVyZZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wvvz9qBjjstLQ1zSKB262C-I0D2m6ojaT8TOtQpsGJBghETjHzYTV0oskHNMMCGzeliNn3UqxPNN2PNnor8MTur3GNoGjHACuP5xyL7q0k4IoviTVN0T1r59q0mMqgS_tCw908A9L-9GotBCTrQsLhwJK2ZUP8mo8x_rDoV4fhjG12FsfK2Kx6vKHivcsds8rfGj7scmR3Ceb4-erydd8PTSl0Ja9ncaZKUDly8ecg9nzkBbG-8iGbPSSE9Vdo8rqIi_-iffPfQeppkGvAr1F4IlkLOBfPGsjAZ-zyn6psCsVN-giqZ2KRrSvVqzaROGCYNhzby9_tSqA6IZqhdPFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdyvlvYDUpxMbjzXRYuLlBiZL08GylT1waCIeLqC6xdRhaeC6raZHtq7dlWiwJFddhKctWMn-bSkfJjbeCxeMYdXHJ-GTdDVRR8uqdOWAi2_0Z74JHJfCsJRhS3gG2UUsTL3E_ROAOQ6HmVesIGoSlfOZ4jZKgJHccctFOkilggv8rI4iYlNVnDUtHUUceFSLGGp4bRf9rwp-v5ZyN2f7i8A35RqeFqBpTGMiRu76C9elVevsFP296y679vDLd6_IMaPFeVjGPZuEYMdDRlPa72waOfCxbu8Wnk7enRIjBvNIOfn7v2ZZB_6XaDpT_qrVNXrrHUbVG9TP5SiN09tDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=rJl89xyoEuE98qVBYa0G4SBTmv3hiMDhFsm0scb4wDEiXorGW36_DOZjcHs2VcKUgK23YRO4Eym59NIwUAmOlVDqQBM1j8bUnuqkrE8n_c_rDtv9220ip8aSaaUtNvmNqhppRIvPMs-1ESwEEmdC-bUiG-pO-8u6bl2oYPvw5LuzWmuVd2ru-9BU-FYW3qfieFXvK6n2DSKDqJljapbbbAWI94S3PuJm0ltTiYPdr2yvZF5yuDY_VsIn8PS8H0sL9kXeP4gKSaY9YOWiSIKOOnLkaJMTGi7CesLgqgDZuEwFZZs8Oq-zIWnN0FlGw9qJjeEZkf7q69Bca-QJWuCotg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=rJl89xyoEuE98qVBYa0G4SBTmv3hiMDhFsm0scb4wDEiXorGW36_DOZjcHs2VcKUgK23YRO4Eym59NIwUAmOlVDqQBM1j8bUnuqkrE8n_c_rDtv9220ip8aSaaUtNvmNqhppRIvPMs-1ESwEEmdC-bUiG-pO-8u6bl2oYPvw5LuzWmuVd2ru-9BU-FYW3qfieFXvK6n2DSKDqJljapbbbAWI94S3PuJm0ltTiYPdr2yvZF5yuDY_VsIn8PS8H0sL9kXeP4gKSaY9YOWiSIKOOnLkaJMTGi7CesLgqgDZuEwFZZs8Oq-zIWnN0FlGw9qJjeEZkf7q69Bca-QJWuCotg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ip2NawMwbvMYrX9cUPixXCFNJnVf-KWY1kiaNmknoO_qFT6FUGENjIiWjnysrRMVqPFG0-6b8YV_G_jRpIlSpb5aXqED8QpWUbj8KJ_B9-7k2iEmd7GE0IkGjERlJj4597cH1dB4kPeQZVFO0JKZnXPJ-xfyeyXzN0Xa8hw5HzKWD1gLFSgMfc99iZFdB6uwdq2WUV-DJiZEnUOb_YJBijhwlq9MCZ7yzwTQ7GmtmWO-QgfHZq2XesL2DHiZrr0JsWpOutn3Emm5MDLibNcASS1cJSInLPF7xe_gRz5u_4k-tUauRT4Z-73fIibJSPJjdIxij7fvpUOPWfgbdl6Obw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAkqwGhVgWDd67doVo-rfNRaEzjMUV_JXdFG74qJ6NGzRNwSTuwJMlb9nOEVQFp8WyVuFnX8Nwgrg1F0TbX9wXqrgtTfTOAXIy3RexpQhdPGNVt3fbb4JddzjtS8xqeAM7u3sDMcfxuWrUJO4y2QBCNaQ7xK3Dp_w_xgPz-Ux0xolbgRS42nuAcqvJx9dp3YoSHrw2r7JF73LQNz09-QethmXY3lhQzCnxtcKp2IRb3k6l153-GdnLB3mS0lSEvJYdYMqdxiUSyDVwNg1r2X9NkTgHnK_OErsnQfiyDy-k9xr78XbFHn2zxo8kC2-a7O9eygpTVmT0m4TLXwQmoVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6DFDY4DnEXw2ENI9M5kcVRlIAZl0HmA7NbtZ6V7_toGxYtrREpQFBp5HCiPulUn-HXk-DWEJS2vUzfK3-dQNWivbIdtCAnZVQ-Px5RmjEigZfayc9AWavTgDKs6B_odjhCc-hnfia60x3vb8E0o5Lrub_NN_xB9Mz2euRPygdK30kn0UZjMaRKa9QR8j6yFRyQQb-ml61waTFinlZa6J1ERfjgFgoL0kpk0gYqrd0-n9Ezg9rRGDkhRQirG6753MZB2Ssh-zq9cEI38aVf-Q6cFBEjgnurDPSddCILWEZoKCahk-IbZWrJv6pOf_SnfW4eY6DcxfnsvlK90pCFbAQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=cHYGgfw2NKY0j9qwGLhQ9H54BhuSOma-VLFkbSltGaEq_7urhpyxwdPPgzBGvxfUj0ClrVTxVD5CqOaQc_CFM7IndSK25MddklllzlAcfXd_Yc2MipUNJs61kVRHzWB7ql-dFZQINfPBJQq0WsuB5wcp4OKsm-txzHCkUoLaHUUHbzdG0Yr_C0WmgEFgcK87AjYk4hGX4jQ3B7KjG7uMSTi1_ibP8klM-zGNchbH9-uTrM6GcpaHxNDe9CViEBD7N1Xs8eavz6qs91GHoZeXr3TlupiPG0mX0um7J3mN_uNf13sm3fh2kBusjdTdxAdDseUdJ2oapvSdy17IyzxuAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=cHYGgfw2NKY0j9qwGLhQ9H54BhuSOma-VLFkbSltGaEq_7urhpyxwdPPgzBGvxfUj0ClrVTxVD5CqOaQc_CFM7IndSK25MddklllzlAcfXd_Yc2MipUNJs61kVRHzWB7ql-dFZQINfPBJQq0WsuB5wcp4OKsm-txzHCkUoLaHUUHbzdG0Yr_C0WmgEFgcK87AjYk4hGX4jQ3B7KjG7uMSTi1_ibP8klM-zGNchbH9-uTrM6GcpaHxNDe9CViEBD7N1Xs8eavz6qs91GHoZeXr3TlupiPG0mX0um7J3mN_uNf13sm3fh2kBusjdTdxAdDseUdJ2oapvSdy17IyzxuAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXRfOVxdKfF318xCnHU6FG8mDvyNZh6HuYs39hSihdXygbtIOirhzirpFUMXHfARyQAbuc2VRkPnOPWF5JAcCSBgHMauP1Fo9fztHRAF8GNpAjiMht-SHYaU9OYD8lL5QnXxSeuqjIfnkXYp9cfWC3mCE6vrMZvk9bYdKpahPcJHMbiH6nbqReGfPJMaytRv_bpbGgR867ROjdupFV461iBkoi38OGTN20JAGiC1v8sxQiEv3pj7Fh28pvT6UloRKjp89LO_4gGhiTWH1fZsQRtLH5hTABS2EViNqHI-BtavEboY5QqG5pSFO5xgUo_10tmqY3LG6g-7MVxWd2s4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=O7Vrb4pWm1LD8_IiarRNBwDXi0jSfinY-hbKJRmuyjpl9jgMW9hb6ltSPgskXmqYV3erFcU0I34L5GFyufe5fDrE2SUH64OBwDKrkA_pBVe1X6wAPhl-R22NSgeU1t-Hr2YwtSKNpe90JqfcRKF05cYeHBU2Lq44y9tWl1eqHztUC286wp_2mFSQNoFSnb1qJYFqIwkempRdBHKCmBwewX2drNZ7RNgEDcd1nNG3tmkmMxDS5hOyfUTHT9SYu0AUykAnSQc089Y1tWCSkLBMoGbJGY12mIB2TFIKu2jvior25t9xZiZB-OapPKmGKV7gHdg6s5TV4xvyBk0EDwj1Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=O7Vrb4pWm1LD8_IiarRNBwDXi0jSfinY-hbKJRmuyjpl9jgMW9hb6ltSPgskXmqYV3erFcU0I34L5GFyufe5fDrE2SUH64OBwDKrkA_pBVe1X6wAPhl-R22NSgeU1t-Hr2YwtSKNpe90JqfcRKF05cYeHBU2Lq44y9tWl1eqHztUC286wp_2mFSQNoFSnb1qJYFqIwkempRdBHKCmBwewX2drNZ7RNgEDcd1nNG3tmkmMxDS5hOyfUTHT9SYu0AUykAnSQc089Y1tWCSkLBMoGbJGY12mIB2TFIKu2jvior25t9xZiZB-OapPKmGKV7gHdg6s5TV4xvyBk0EDwj1Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvaeB138K-DCSNC9IbNt05wUYOKWkdXRpqmgyBv-Pa-VjKt8sMAUOJjuxtj8zW1FwqkfZxbTGzmJmVqKq7DQK1SyhoRnzxbwFBB1VTW-eKWjowVtMWR5N7yo2OU_NAvIqZCrRFwOLwtoaW_c0XO-KanQrvne2Lf-UqaiZakW_fUOOz-nPSGMlQyr5wqVPBiZMepiv817eXlSEvd4JwyQrYx5mvgkx9bGYSHPwGlznbnbs1mfh2mUhUsZV-8ifyZTckGevarOOAGqorL5Jnpiw7tKQQFqCbJEG1Atq45-e6a9B96mTRtBeVzeF8J5B32oSfhqOfjZZUoIicBHqSCrZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5sYuF79UwO-zZ30dL7ln_NzFxpGBIhtuHnD3NeRDLONyibxQkdfTrnPSMkZ7_70mqe1wz3bGRNBG0FlaC72K6SFdblaffyy1GT6ATIAOkePG0lZKtr5cyWMWqsuFmXqrtsA3V2zbjumo3P_BRHGvnWTkgBYKuxqRN39-kbO0v7GPZdSsNZ-M0JK1HXESBIOoT8Mir2PJLjDVLP3q8hINzZrhHh5PHcNtMOdhUDUDwSwWGUV5qkOLjocj7cyMsl8xiTswZ6bRhOqx7PRBg6Fxt2Za17HaeLKBWK0Il-iD0pxuDhrJbf15FoZD-TSQcbyYu44qvEMuFzkynfcL9W1CA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=LwoMmLW25Lod08OYSG2lj_TVfqz_AHn1ikgIiSWs9LXBs8dsKxdETmj2iHQOwAZRo--3zcUPiNsUiE3s8J6umwGV6b28rq0Rd3sS5cMm53MW8lDb8Jw7BvEyp-br0ol-ZP5rrJgsd2NP4GhsivMcho8eVyIeHBKejbVeyVlACxTFSxFKg1qKnV8wE02vCXGsKhRO-VN7THEUHMkYz9yfOOh4ARl52Eycao9LF8qs_rA4sNCnNrO6z-6H9rzcdUqwVwekWnqmdwChUOV8E6P_085fgnPvYI0WxtiPXrCnSl96KFd9Ak2GQzlLLDegOoCQcw9qFOjLdyI7h1ZaVSgwp2NOdLAgEzsemRGEQ15MiO87btV1A95ESuLRBr7UxWtk9Wi8S8pGYRcUP45Fc43_Us86sfg7b-FzceZ_r3HQ6KSAFcw2K7b7XZWxeCpdalf6CI-Js85DKXuvrLhcNBRHUZHAtzqu0H6cYxHZPmDsoY73yOD-MZem-1-peDxzsRFY9jhrSYGpZj2kMTLm2HDSypijt_TRmijdTFWJMJoTfIGPvpdxohZZBAHbpXiXUEmQ4bo11zeXrMvBEAv-NRAw5EmrW6rDlKOxctfWRHO8cHL-NlApG-Dx8e446tPfbapW2Y5hUoCqvzKUBPpX1lvdzPHASEy98WFyuScLrLj9vnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=LwoMmLW25Lod08OYSG2lj_TVfqz_AHn1ikgIiSWs9LXBs8dsKxdETmj2iHQOwAZRo--3zcUPiNsUiE3s8J6umwGV6b28rq0Rd3sS5cMm53MW8lDb8Jw7BvEyp-br0ol-ZP5rrJgsd2NP4GhsivMcho8eVyIeHBKejbVeyVlACxTFSxFKg1qKnV8wE02vCXGsKhRO-VN7THEUHMkYz9yfOOh4ARl52Eycao9LF8qs_rA4sNCnNrO6z-6H9rzcdUqwVwekWnqmdwChUOV8E6P_085fgnPvYI0WxtiPXrCnSl96KFd9Ak2GQzlLLDegOoCQcw9qFOjLdyI7h1ZaVSgwp2NOdLAgEzsemRGEQ15MiO87btV1A95ESuLRBr7UxWtk9Wi8S8pGYRcUP45Fc43_Us86sfg7b-FzceZ_r3HQ6KSAFcw2K7b7XZWxeCpdalf6CI-Js85DKXuvrLhcNBRHUZHAtzqu0H6cYxHZPmDsoY73yOD-MZem-1-peDxzsRFY9jhrSYGpZj2kMTLm2HDSypijt_TRmijdTFWJMJoTfIGPvpdxohZZBAHbpXiXUEmQ4bo11zeXrMvBEAv-NRAw5EmrW6rDlKOxctfWRHO8cHL-NlApG-Dx8e446tPfbapW2Y5hUoCqvzKUBPpX1lvdzPHASEy98WFyuScLrLj9vnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=NUbt8lAi_EMVNMzgXzfhbPgJcuDzE1Yx8fVrKOrSx9bnwomuLz0WM0LqcqDFZRSe0M_TUE1SlWwXxe2OxJTskwp7O91MwPk_NIZzPYtmmMQPyXZ4W7JJpAQC538XTWv9u2fQY2bC90dRlPbscFIhuo24PoD89EDjTzEDOmim1wCmkXnyfzUKZG1patQhPfyr05zdj0Q6MW9DL6_FzXP9TqrIl5lQKQPuyBglE1xzVzlZCEtLinSJ9CNo0pzYnU9W-6j77S2Owtn-cg61ccPxji0kFRVvND83deFeHKZfKohA7OxQRbCFcHTZ6hf29oP8VtbMxIjHmKzocBRNKBruWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=NUbt8lAi_EMVNMzgXzfhbPgJcuDzE1Yx8fVrKOrSx9bnwomuLz0WM0LqcqDFZRSe0M_TUE1SlWwXxe2OxJTskwp7O91MwPk_NIZzPYtmmMQPyXZ4W7JJpAQC538XTWv9u2fQY2bC90dRlPbscFIhuo24PoD89EDjTzEDOmim1wCmkXnyfzUKZG1patQhPfyr05zdj0Q6MW9DL6_FzXP9TqrIl5lQKQPuyBglE1xzVzlZCEtLinSJ9CNo0pzYnU9W-6j77S2Owtn-cg61ccPxji0kFRVvND83deFeHKZfKohA7OxQRbCFcHTZ6hf29oP8VtbMxIjHmKzocBRNKBruWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku0oNXgsRQB7XIny8Axa2rhA9n-Qto0AsVq2QHhNEZwKPgKaG256nHd_53nf2CGn3eJ3oHUH-hR2-jX1MsxLksRybKWggLkLR5hjMM-SAYD_wLDC-P6CWtudFI2Fwkh95sOrgcGa9jdL5WHFjTLC7llM6V8Mmeh2HIy5THyFhk02lV9UPUu2zN5hannlNJhknQ8ZwasUBjhXvYV3yfUX8ofpfMSjZJjyD7IQiO2AIiedgzbBGeNk1bFc9TdtFJI1q8P7eU028hts_eU9KjDFtZ6rhTM3YItb6d7Ba1Eja7PUI0A1hXl1iJ7TjYsc11oLG1KRvfTrnC432T7EJPxnog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=BirpiVSXz2HicoWwLNuk_ivZyX5gleHY-z6y3i_qCST7QS8LKFF8UNyHmdN6Sor6mpqREKIiIjfyWe4N8FYMO4lBmMeqC_SmpspicMjx8Fp0JIPuJNRO9h5sJ0oV4NVbeeWqUAsjHIg5g-PJqRTGhWLfuvYZx1zMKKmQ5U4HOSyCsi6VA3F7l2NX8LpEZMaqP78FBI8aJhUoaKtTxkXhaS_KOtfIMtKk27Q7o23oBL7YAIB79xMGhvEGzF4YGzu4YNF3vtKPZ07skmFcr8YS3_uHDqaO-b14gR14CJmLGJImehwQVYa7YwQMoRK37dYuvlmIlIxIMBDcm6tHFtNhZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=BirpiVSXz2HicoWwLNuk_ivZyX5gleHY-z6y3i_qCST7QS8LKFF8UNyHmdN6Sor6mpqREKIiIjfyWe4N8FYMO4lBmMeqC_SmpspicMjx8Fp0JIPuJNRO9h5sJ0oV4NVbeeWqUAsjHIg5g-PJqRTGhWLfuvYZx1zMKKmQ5U4HOSyCsi6VA3F7l2NX8LpEZMaqP78FBI8aJhUoaKtTxkXhaS_KOtfIMtKk27Q7o23oBL7YAIB79xMGhvEGzF4YGzu4YNF3vtKPZ07skmFcr8YS3_uHDqaO-b14gR14CJmLGJImehwQVYa7YwQMoRK37dYuvlmIlIxIMBDcm6tHFtNhZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJgv28wApGAwus6-Bjk7aZ6SBBNsDBDomb831bIwhpq-XVtEMob--1Bmhe4wDlR_rwigFVCsuVui0QCutrZm1KcHXRQTbp1jNOudflpbK9FdFRxtr5Wi7x8YY-HMzfn1wD4KMjGBSj64rzJb75O1OisAY_JFtIo6OIkzEN5tmFL2CAiUoZKttMUAnVAsyr3TQVSElCV9_MdcEFynkkaO-oOZE9Kvm_z2kWATlusVAoLN2aAVuFg6gGy3P-yvl_bqVHwKyOXeXmNeTLMz9mBS-I2T_7vWupbqxnTKEOpBMjyt_Fy_K7ZB7nDOiLT5ZxjrhlYEYXVyitMugQa0obGfEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orxcqDJLFNyFmMnXED_wHi1bUpe7damJNs2anTG-p6UEzD0SFxlUbTnPSeFN0ICn7RICOn6qk-lqoVJPb9H-4xPN46hceD4iTGJk62H8FLULw01F7zNALhcixfbrfFknB5zix1kvQzwIL6FSkG_UIVFM2RLeqnXmdozRNjz1f_X8NGGUNL5DlDPr-zmdDIDr0aX3My1-zvvaQyZr94ctiqMtQCahVBn0yIoB0Xg9c1hZQ4IRRKNIsPysBXRO5H3qGTyzHvCFA0oqr4P1vvHaydfy1ytzHQ5xGfrFiWI1Iz_x7DEa33jvKDCAHKzMtzW_nlWRHUhWJk_vNOL7GZ6AjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGT82-OOxzUNQLBerg-dewGIxHu0lJoM9YxMfQ7WujuQyM1Y4kOjOg20Sv1rQ4UtMlFuWrG-LRw5a8SKxcDifeCQc1V26OfltixK4sWdrMdpWZ-6H1x6eLE2EBmD5_C43_aH4S4RW8N0m-P5Dhk_OWPHJDguJ17LUV3v43OlzYen9r0SceP3PyHdnzE7n1ZVSUKXaDcEKvk3WPhQUy7QcKj0aNppFW-0Fder7tqzqLYg3pRhJ9HWywfCWQ0uEcO0BMvzlGLF0z1_6qDhUYLbkHyff_3XeRfiv2z1nxwf1fqf7Ax0vjMuloJREvIGrwUG5gA4ytd3ciCLaLFlfV2Nkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6PTjci8Gv3pu4NWo32rMKadATNJFXDynY--bFnlGN3siVzYR42iKhS5Gk_bqoqdZDYQbtPkrwRA7VrPzt37Sai6IFw6WdT_l8Ub-8hDfINCfjjMyhGid7O6ao2h5vqnKkX-50UykGIx4A7juqTIfLfdWTMmjyzfHmfudH235YPT7hmtnna_q1_wwPoV-8Jy6U1ojHc7ywS6bmfRdHaGY6FnI-g1b4HCAmxH5OdYuD7Z9GoOomDsipeu-VYMMKGzpeBPtDxGyuRnzy01-jDp8K4W6r-mJI4r7mIsFPFhNbFKdlt-54UKOIXY3C-Dv3z9DRhJQ_RiusU88hv0Saji8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=v9c9PUZnMIPxDvcpRNTJkh4d-6W9vkx0QNZQMST5N8ZSJ2AmmLzpV11cMX8autKhYSa3DflIrKLmUh71QXprS0VniWpAf1ocgeF735-hZYkXzKezjz1bZ5FnbJHl6uYM8-OL9-g0Lmi2dA9PQ01vewiwQ6zEIWWnM74qF3YMJaC88fYbGcdiyq89BW9Oa6T8dtZuxNHouNYD4Po3cYXbn0Hr_VmQfCDaDbH-S-ptVFOEmWjZcTQ0niyPnwk5ox2YuPmxMl9ArkQc1M6IGrSd6dlrtOmVWLr_x8H6oFkTTUSIsYAO91s-pOPHYaBubBCq_g3lvRVNwgLQ4RfW116bKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=v9c9PUZnMIPxDvcpRNTJkh4d-6W9vkx0QNZQMST5N8ZSJ2AmmLzpV11cMX8autKhYSa3DflIrKLmUh71QXprS0VniWpAf1ocgeF735-hZYkXzKezjz1bZ5FnbJHl6uYM8-OL9-g0Lmi2dA9PQ01vewiwQ6zEIWWnM74qF3YMJaC88fYbGcdiyq89BW9Oa6T8dtZuxNHouNYD4Po3cYXbn0Hr_VmQfCDaDbH-S-ptVFOEmWjZcTQ0niyPnwk5ox2YuPmxMl9ArkQc1M6IGrSd6dlrtOmVWLr_x8H6oFkTTUSIsYAO91s-pOPHYaBubBCq_g3lvRVNwgLQ4RfW116bKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0Vx7bvMAzCF0Yxb5j-h7749IEYdTtrzUVt2rmOJCGu0YflNIHoBfQBbSXM7hxYuRkw9b8pdjogY7nLmz0Zq-FYcb_SxKaYNK0BWhJq434ce9YenSWTC3e6i8WqqRaSf954MA-6jlN4F2GlCFxUxsKPZUSuYmsSOhxKs7dakWQiNRTiWaliF0H7jV9IVV409d_vO0jtyGwIaz4nNyR9KcRxRMflQfOeyE9NrPGNvb2wQQO_49r-aaHxyesy-0gT9PuTjzx0rS-ExqPcbuUDLuajxRQmEraIW1vXLiNM_pKeD6011VkYvk8ts29ce97vrgAqyvPV85ZG6W9rWCBdFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_aUuXWHHJ4reCpod6e7tQ9cHCPdMm34u1y5pUwqDM1lfST3vy6QIBldaTyGFR7mTNIioiHT7CLeKo19AoXaHhLUgrXqa12NwhbNE-T2XEMIOZ-cRiZHBYIiyH18Bi8JGtAHJPDOlWWaOVcO46r9yYHwld5xzrzgMM9GVxmONdXlHE_bqMgvMCnNJIeRZIUEVWZ47xl-gKW4-zzw6xg2D00dFZyXGPSizPbqwyn1gLxWecsQ_uZw-NljxHf81oVWt8NlNF0SDpP5ELWYNanBy9YN8KaqnSNXnOKc0seoVyiGfT2WF9Vfwmk4hhtibbF72VmN5yl2ioK0s78PEszKfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Mhm6LsXAccLNCN8bhnmU03SAbGvdEpGL7ju3mIgolHao8FVRDr5Ia_sMWnFkye0wao6y28KnsfqFZ5om-ZtdyWE1E44R5wcOR5SBh4PcMN5_snNTeDeywXMRavjzyoT6Ztdy0GLQarsA0eh43HahFfmG8lADyOWJKGCCcBG7TT1EgcFWybJO_JI1Uo0AwZBXAklNudC6K9oZuGeeRm_w5J4eqz0nKIiAXcFWH64ZXHvftznza6WK7fW72hDhKWa5pORszgZjPoqe2pwOJGmBTIuxMtmExa3tzeQpj1pytWGRZn-oKGTKdoPp4qDrAmuTTvRF6XZREXZOZohvO7ivZ7FCBN5RbNg2qFxzHBgbORVxMHOUz8uPM-sJBGRx6kd3D_Ytqi5R4SZ6UuJtBgfjwPly7zxqEt24Dg9ZH4dI5XJtPvj0Ko7Qv5fCVhYvIVRsEcAmzIBfZFLb5mFcTbCSBrcyYgpVYs0Hg0RFEofK4SwRcADTYuhe2ZleRHDOhv7Mew8mdx1AwVatjRpzL_GVCpBW3n00nTTWOEGcfXEYZmxcojQGpJzM_YcFa5c4CGnG8VYx1AloodiWnw7_367V_Skn7ypCsYBSncthxMyJyzfk-bpni2a8Ugip2db83Vg9uRwwtffH3VhAYBiGVnlHtAl8Jcmq0drpHUq-ou7yhVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Mhm6LsXAccLNCN8bhnmU03SAbGvdEpGL7ju3mIgolHao8FVRDr5Ia_sMWnFkye0wao6y28KnsfqFZ5om-ZtdyWE1E44R5wcOR5SBh4PcMN5_snNTeDeywXMRavjzyoT6Ztdy0GLQarsA0eh43HahFfmG8lADyOWJKGCCcBG7TT1EgcFWybJO_JI1Uo0AwZBXAklNudC6K9oZuGeeRm_w5J4eqz0nKIiAXcFWH64ZXHvftznza6WK7fW72hDhKWa5pORszgZjPoqe2pwOJGmBTIuxMtmExa3tzeQpj1pytWGRZn-oKGTKdoPp4qDrAmuTTvRF6XZREXZOZohvO7ivZ7FCBN5RbNg2qFxzHBgbORVxMHOUz8uPM-sJBGRx6kd3D_Ytqi5R4SZ6UuJtBgfjwPly7zxqEt24Dg9ZH4dI5XJtPvj0Ko7Qv5fCVhYvIVRsEcAmzIBfZFLb5mFcTbCSBrcyYgpVYs0Hg0RFEofK4SwRcADTYuhe2ZleRHDOhv7Mew8mdx1AwVatjRpzL_GVCpBW3n00nTTWOEGcfXEYZmxcojQGpJzM_YcFa5c4CGnG8VYx1AloodiWnw7_367V_Skn7ypCsYBSncthxMyJyzfk-bpni2a8Ugip2db83Vg9uRwwtffH3VhAYBiGVnlHtAl8Jcmq0drpHUq-ou7yhVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=D0grqG2qBleffF07qzKiJtwlxLtQFbUe3O5NDJXUKeY33AF-ZWfW38DfDbKr1KWc6bal_tkKQp4WOgG0Pxru_UsQ7jLrZUncCV6EZKnTm_5OWb2jYX5TTXjxVI6_XIiRMtOEYovcFfNmyRKWTuXG7o_4eWaujibH49Iuhh9_TSsCF503ew2ZGHynFQFxf12ZtjXX2bHLIuwqkNBRhFKruLiww8We7YS8KzGQzLEZI4R-K6ZJFClD-4_jW8lxRpdz410dAoZQLvhPiU76Qm_52pinR_2LRXEAyfd8J-ieEul_pBAsXGMRSJBr-Bh1MD0NKexnVJ_Q6PUsNTeyhZ0IAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=D0grqG2qBleffF07qzKiJtwlxLtQFbUe3O5NDJXUKeY33AF-ZWfW38DfDbKr1KWc6bal_tkKQp4WOgG0Pxru_UsQ7jLrZUncCV6EZKnTm_5OWb2jYX5TTXjxVI6_XIiRMtOEYovcFfNmyRKWTuXG7o_4eWaujibH49Iuhh9_TSsCF503ew2ZGHynFQFxf12ZtjXX2bHLIuwqkNBRhFKruLiww8We7YS8KzGQzLEZI4R-K6ZJFClD-4_jW8lxRpdz410dAoZQLvhPiU76Qm_52pinR_2LRXEAyfd8J-ieEul_pBAsXGMRSJBr-Bh1MD0NKexnVJ_Q6PUsNTeyhZ0IAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F25XL9iYLPiA3KylybLH_EtVEStO5gc3QG62kXmwhOkh6LDzqDyP0uBgRi1kA4JbUear5J_z6nkSmAhJiWsWQ0-q2oFzr6ueapKKju0-uosebtujxAWp9aBBUREIfPtRCSscPtMZ4dasztJghyVVS5OYKFh6spSp_C9hm9Io30sBQLEI5Xxel4sc_xFjxxn2T03YL5JX2dlwLXFG7R9xoxlrhT1OSyNzPv64IaiwxYSAeW7XjTr2OmKPamXBwfwoW6aj4WmuUiiaYHkUA8L03qR1dLz6Xm77BckDOUVAaLmlCHY1IDQAw_Kh8SnVn2-hb0enMuBbFiG2TiKXV2BeuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdQSrM6PiX3A53AJ--jhCMcaQo4GHdAZFbkKOZEOjaWbbypxcOx-rdLcD3umgS-JLknowC51HkbuZn01iPu5CdKC7mL8Lgos2VT_taIxqlKHnLI5N2bdIh8UFZ171825unS0gzm77Ai6WitsyxV-4BbFphSzWr0VyYcbTuqvfUjiTxNG7dX-ZekzWCqoYASwqCCTmYKwXStfzblDL_FLJIxo0N9F405yGIxI_1rpyU-I0Rq02Nzs8vawA5WHLNmqZ9OyZwltnz4vg4_MVp7wYLHxw-YbGFZtcryW5Y_KXlvEOL0-_4-mAsbV6y2uhq-9qIVX7BAIzkFXQnrb5Jl8LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYpDYCZKg6dnmX97PTThDWA76l9J0DpWzKDlNdvxWnnUHtcZjP5t203tmiMjjSYneCtCbugL_ZOhRdGZCgJyaLClukKNsqpozghQvAhST8spciicen_FQ1O3h97BvbAG-RKfsOLnCe2qTJ7wVvIByeEHJLKXnEaCcKf90c5rN8LXqXJq43QU-Ewvy4Dnh1Ow431e8nfEXCmlr1tEFwf4h4bDYfccpuEDkNKMBw8lelOyCpCZy3XLMOEVzGh7RGesL5-tqq4qU0t7cI_PP2jADLYKQCBoMfwiGnUE0G-8u6sn8oCHrT-gzPXKjZeHQXefLRrIId2QVwTYw0q9kovmtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=mYquOR8kh30mqSt_5fD6WIdRi7l6YHmtuKqcQBV8BiNd6cj1g8_8ifY18cQoenu9BtEjoC6ykYyz66WYWv5rUT2NfWF4ltkMi67cZfoIEyWhScA-6T_YNN2ODrKxEWp-MbKhmyBLKmozmPR02CLQoqC9wDBdaXOzjFzsUkNgMuncEF4KMcnMEKbS1w_K7YohFww8nrIdtubN7lUjq37TRdiw50COZvVAjGKi4O9_fwqPtPCKR2wLmAr3UgZDamOsLWtnuF6xnqnOApnzBFlTUiOs1mTKV4wX1hI4Vcom-71Usk3luiYBMqBipnqSWT1snZVBCRlr6iv1gS9aeEuC4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=mYquOR8kh30mqSt_5fD6WIdRi7l6YHmtuKqcQBV8BiNd6cj1g8_8ifY18cQoenu9BtEjoC6ykYyz66WYWv5rUT2NfWF4ltkMi67cZfoIEyWhScA-6T_YNN2ODrKxEWp-MbKhmyBLKmozmPR02CLQoqC9wDBdaXOzjFzsUkNgMuncEF4KMcnMEKbS1w_K7YohFww8nrIdtubN7lUjq37TRdiw50COZvVAjGKi4O9_fwqPtPCKR2wLmAr3UgZDamOsLWtnuF6xnqnOApnzBFlTUiOs1mTKV4wX1hI4Vcom-71Usk3luiYBMqBipnqSWT1snZVBCRlr6iv1gS9aeEuC4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9_PKBvrJxRqsNv6-5XLsDrCSPf02OMBUb_thKkbE1GXFPmkdvrvHiFYLscsebKHwatE3-RvaPHNHb21ZbOdlgJG1xgdMgDKv5cKji0mHjUA3WJy7ycceLnEBMxIfSK0OGHYW8MW7nmb_flVMYUWfap8oWNPi8H-np4IFRq7ccg-0515tFjx8iBmNpjKJk_Xiy_ctlmfwhqMJ-wohDjVV7zla5adWGB6k4KGbk1GiQ4HzScysv8TUsLjahdsMOqRXhIjxxO1vepeiP2zdD82anCdBKMknc_E0AsykPLq3V1c8MwIjNRnImghq7DPnPblFfVE_I69Hhu93YN76j4QFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gg7VRrJd_15oJPBOO6baLbt7WH22AC3BL6dVpVfuQUQ-PMRLw5mI4_KsuFWYD_-Y6oN7TY3srJ1DOS_Wadtqh0Z90fqa0axSlY4mfgVvB9NBv9RVhpAsr3qROERsSDpf7eUe6hkMpCqUuQZoh7FAQXj_Ey0uIAagj_eAQRDk8ZodPWUFMPpgPx6NRUehtL2u2KpuzycM0B6UUz5b6e6cOoJosBurXJvLE-agsBaMBTc7Q0pPvozwHkuttztIQlBSfJnMLIs2uSt0Sw6bpAuIUt28NvGT2vmDmjJA3_OzRr9jqoTGOlOUrXqre8ua6IV3lHD0hXVQ2zbpb6nYYz7gCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIEF6zii2x6W-kGc4KZjRx0B1TC07_8khoZW6oYwcwCXSobDLCHJiqpX3MGBgU2IBThTT_nWPYa72B-ENJK3iS1H-WNbML4DlCyVKcRZgTvcXlgS3MC0xSd2ob1c5PidMoTpwGE02hOGJ2Yr3q1l8QHHXbz9GgjV0t_0DEmP3HwOhjD2XGc2vgY8q_5hLdtpE_V2DQyBR2vce58kraNhUoXeotN4xlZT2tPhhtlY-wzrtiiO093X6-YScppABS2LqUcIYIUWx5mqhgT4S7EO9UYsSsnTlwuIK456XBhwZ9hqvnKsw7Rka7gDaFss2SBbGLqkCB-0W_ptAggfU89zrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgl0k7Th-uGqlQjGDkPqavdExE0cUlmEYbjv92ol19KgQEdPvVQwZYANgRmLYbf-nANDX4yHTEM_QSKMW8A8oVXSNYlK3LPZ5SZ1CzapA4qUtAQn1k5BmsVw50CjLlXYbRBr9Ac3Jjxv4OArcH3xDid__VaxlSvWYriAhqAAorFypXGIuFmMbA0HOgWiqN7D4v6CbnQcInPr5IRMYSQSqZxIBWOH6VOCAiPtmZidzoiRNo1Kamgnw-qe9Ufz6I-MCmQvoSB1cwluahsaaOV6ZJnVATn227c3AU_FaYoLNN0S72TK39Xw661jdLv5c7mIVEhFr5TOw4s4qTKR_Z0gDg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=jp51Xt9k-6r6o6zFhRWN8WiYcPNJsrGetclvT0U7X2jcb0Pkk_R1SA47dY4hra9Ix4XX6_-6XU4llg6a4UYoHsc5mzJObIncUejx3vlg2gDhbYqh-zVlKmtfZMfJ5ShN7TKqsiF2G1btDe9KrRPlomcw9H7mNH4ivt6sfwKzI4RmAEUc9B5o1RWbjWNYAnHr2GxmvnZITVlmHr6e9bhcIH03FL_5z4tFtcLX5d-RjJ2ZKXTMKpXWAWi4noUYXWRylq1lzql5rxzWpjNYIlsJV4EYIq-wVAGAf33_G1wzfRLy1Vs26T8GrN5dyuz-JPYhWBN8NDJkgglOEXe-EbodWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=jp51Xt9k-6r6o6zFhRWN8WiYcPNJsrGetclvT0U7X2jcb0Pkk_R1SA47dY4hra9Ix4XX6_-6XU4llg6a4UYoHsc5mzJObIncUejx3vlg2gDhbYqh-zVlKmtfZMfJ5ShN7TKqsiF2G1btDe9KrRPlomcw9H7mNH4ivt6sfwKzI4RmAEUc9B5o1RWbjWNYAnHr2GxmvnZITVlmHr6e9bhcIH03FL_5z4tFtcLX5d-RjJ2ZKXTMKpXWAWi4noUYXWRylq1lzql5rxzWpjNYIlsJV4EYIq-wVAGAf33_G1wzfRLy1Vs26T8GrN5dyuz-JPYhWBN8NDJkgglOEXe-EbodWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=aiOuA76nYPdRJoyxR02R10C4LQxK6lMH-hDrCSkSqjb4nnM4rDsQrmZ0lko6t1ATx8wYqUlwSqVZ3ePIodDm9RONnvDwJnfpOtMpTfjXOaklDWcke3q2NyD83lifWkHrA9IkbfyESCj2aMqAujWQRQ91JcKHAi9ZVBp4AqulimmB9_8Pa-a6cEuITReWGAS7B3t3N9WGYTjJd7XYZavnC3EKA0p-Cl-aJ5XOQRNbNK2PrP0vHmYTrrRszoJ1UK1yrU2KAE17U1mPCWg_fPmfLy3svzMCTUlWr5jJnmyg37QJ-NImq8ZEVaakgclpjYN9v28JFf87eLRYnL5lrD172A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=aiOuA76nYPdRJoyxR02R10C4LQxK6lMH-hDrCSkSqjb4nnM4rDsQrmZ0lko6t1ATx8wYqUlwSqVZ3ePIodDm9RONnvDwJnfpOtMpTfjXOaklDWcke3q2NyD83lifWkHrA9IkbfyESCj2aMqAujWQRQ91JcKHAi9ZVBp4AqulimmB9_8Pa-a6cEuITReWGAS7B3t3N9WGYTjJd7XYZavnC3EKA0p-Cl-aJ5XOQRNbNK2PrP0vHmYTrrRszoJ1UK1yrU2KAE17U1mPCWg_fPmfLy3svzMCTUlWr5jJnmyg37QJ-NImq8ZEVaakgclpjYN9v28JFf87eLRYnL5lrD172A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=VcHJZUsOLi-gm43r1UYxzb3L0L8VlJGEFWxLeMYpD_hLNdFd2SpvAr4tPJgI3v8cauIU6m-bW4Y8A5tfNT-6eavTyqbQJFfs1UQ8FFfgjDvizuje9jkagEnXJjBavUzM_u3F28KgGBUuli5IDQoKRxCwgRle8bcSP5p7kZPXLJTLkkao02SxfW8iWR0C3ybZJlKdBswO31e-wGITgwe3MXc3QakKEqr3EH0YMc6qrRslXyPmdQ4vI0Svt2n5A5NHGRtqNeHtmZD04OM3xer8M80W1UZeyO3K7ySuQ8DLJU4xjWjltg9lDTmd-Vh_TMGbCSh1gYF60zwyfTDhwJWY2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=VcHJZUsOLi-gm43r1UYxzb3L0L8VlJGEFWxLeMYpD_hLNdFd2SpvAr4tPJgI3v8cauIU6m-bW4Y8A5tfNT-6eavTyqbQJFfs1UQ8FFfgjDvizuje9jkagEnXJjBavUzM_u3F28KgGBUuli5IDQoKRxCwgRle8bcSP5p7kZPXLJTLkkao02SxfW8iWR0C3ybZJlKdBswO31e-wGITgwe3MXc3QakKEqr3EH0YMc6qrRslXyPmdQ4vI0Svt2n5A5NHGRtqNeHtmZD04OM3xer8M80W1UZeyO3K7ySuQ8DLJU4xjWjltg9lDTmd-Vh_TMGbCSh1gYF60zwyfTDhwJWY2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=h4hijq4IWh55TFPC-44KApybKNtLctdFP3xjzkw2zgohYZ1F4DTDmx15WMtk7BeXuwc3PQZt_X9io_Vm-BZaPBf-Bo3JHfZFa1l7bqJ6UluaLN7ywgjBsMRZiNR-SJZJiDEG_CgIBtEtQbYoZbW_PA1jvRFQ-xin9Jex5rXqu0xOVJ5eA9OVwY66QflhWoOkqtaFmbT6lCzqmtV4lEgGgvfkRzttD5t5V_cd-JXSOQ1xaXvLvcQwf1uaafleH837EwQhv-vI-_8qk3F9GOiC54n0WlM0MD-7SERTFV-JOEyzgiM9QF4eVl-W5WXZNmlBQY9dFZMCoafGfEod1dQ53A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=h4hijq4IWh55TFPC-44KApybKNtLctdFP3xjzkw2zgohYZ1F4DTDmx15WMtk7BeXuwc3PQZt_X9io_Vm-BZaPBf-Bo3JHfZFa1l7bqJ6UluaLN7ywgjBsMRZiNR-SJZJiDEG_CgIBtEtQbYoZbW_PA1jvRFQ-xin9Jex5rXqu0xOVJ5eA9OVwY66QflhWoOkqtaFmbT6lCzqmtV4lEgGgvfkRzttD5t5V_cd-JXSOQ1xaXvLvcQwf1uaafleH837EwQhv-vI-_8qk3F9GOiC54n0WlM0MD-7SERTFV-JOEyzgiM9QF4eVl-W5WXZNmlBQY9dFZMCoafGfEod1dQ53A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=qxpGcngj8isWKH3CUq2Ha83zKpTwuv-StzM-AaF00u3zQnRkigH16Vgqc_KX0wRIGs1QzeyDyPcszX19GinP6_aTKaNFEqcJUuw9fV7yGoZtAb6QwdrWvjq6lgIgo3JyCnSc3tl1Hm2f-5_3P3lnpfJjjcuuhXkZHeU4bNEcGdUtwD70hSADj91iuIJBF0dkJFFCMofd_YlkUWN-Gdss5gSlazHGH9a1G-aMEuuKMGWfttDjnBdQRXvi63WDyXjI8o-rZP1pc-XaKz8coESuScCGJBap1qi1QaUAOqTRUlj00RQmUYlVxlnVFxahoNWNGMTavbGHZ11N5E2er3sKNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=qxpGcngj8isWKH3CUq2Ha83zKpTwuv-StzM-AaF00u3zQnRkigH16Vgqc_KX0wRIGs1QzeyDyPcszX19GinP6_aTKaNFEqcJUuw9fV7yGoZtAb6QwdrWvjq6lgIgo3JyCnSc3tl1Hm2f-5_3P3lnpfJjjcuuhXkZHeU4bNEcGdUtwD70hSADj91iuIJBF0dkJFFCMofd_YlkUWN-Gdss5gSlazHGH9a1G-aMEuuKMGWfttDjnBdQRXvi63WDyXjI8o-rZP1pc-XaKz8coESuScCGJBap1qi1QaUAOqTRUlj00RQmUYlVxlnVFxahoNWNGMTavbGHZ11N5E2er3sKNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=BfmVdKIQTvF2ssl-GUb9rh22xtmsJCCP2XvvUOgZFuVMv7qFeXpB2T-m95S1JrAUU2KKes3P648Dkel0Ypu8nqhymdALwJ58Y2_0xigxHcaEz_O6wMxb_vm1fHfXd6Rcl9G_mQoHzXFEQFA24bwcOGVwaYJscpbU_dz3CxDLhkwIIqRsnflKDKQ3PNlbXJaS9jJRfkWFbY2xt5-RxZYx1nSwxUuYLPdoQ-2Ub0EgvBsl00ZcRSTYFrthVFBp2vnJwT1e44vwiIg49IE54UmYRHEvhUFhJzOpPkZwZZg90pGiDc6eEsHqOVs73GyGO-5OPKieSZt6W_pdVo9-jXHxlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=BfmVdKIQTvF2ssl-GUb9rh22xtmsJCCP2XvvUOgZFuVMv7qFeXpB2T-m95S1JrAUU2KKes3P648Dkel0Ypu8nqhymdALwJ58Y2_0xigxHcaEz_O6wMxb_vm1fHfXd6Rcl9G_mQoHzXFEQFA24bwcOGVwaYJscpbU_dz3CxDLhkwIIqRsnflKDKQ3PNlbXJaS9jJRfkWFbY2xt5-RxZYx1nSwxUuYLPdoQ-2Ub0EgvBsl00ZcRSTYFrthVFBp2vnJwT1e44vwiIg49IE54UmYRHEvhUFhJzOpPkZwZZg90pGiDc6eEsHqOVs73GyGO-5OPKieSZt6W_pdVo9-jXHxlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=m_oOdMipRnVR4y27aOgHdqicVp6Z_UGTFp_Hid4pSnnqcub08AiDvLJkH6-p4spTmp51gRtRZ_bVvGpBMl-rPcgiKCCyDhlFiprgpmmngmIY3_Jm18kvqlMA1dj8podu-FZWyNzuMEWlzDjl3kspKTzlSJ0Sc70magLTxn6-8z6EkqTnWwK84H2hz9jSNeiWG7EigddA5AwrArISAt9TOfW1IshL38EGQoYcKFLixtXg4vDd3TK09hid5vNmr-n-wJy2jjcEa9NDz8e0Vhky0kBUpR4WzXUIcdYwzAD0VMZYLf95hjslzUP3slQQ8eTTUiIMzuzgVpZ4YOhZsbmy0Q_aSkAuPv-U2bkqPjj5zyuMdvNMFv0vLcVTpfPANwXYSxWx6QpTkhiUAJiQV-OltJOle-Feg5ZhBVDATUGIeKZNd9Fm0nabdPbJOaM2pRY5uNZR3DVpM0a2Y9y89FZCr-wv4q31QNYcC09Hb5IJYQZD9t5-RlRui4tr5Ly9I9S61KfZb5yWbmXwZVHKl5ZqYj_u301gVHIq3jbgOrJc0Uvu3ssA30CLJIaTSJGOvRtYO8z6gAbI97PgsXSUDCkZJPe_kz25v3p04SUl3uMTXHj-mmtI-oQXgMi4-IYfTqyx6aElEezUfhJmUjwLigz6BJottOBgn8VhwVH8UV_UR-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=m_oOdMipRnVR4y27aOgHdqicVp6Z_UGTFp_Hid4pSnnqcub08AiDvLJkH6-p4spTmp51gRtRZ_bVvGpBMl-rPcgiKCCyDhlFiprgpmmngmIY3_Jm18kvqlMA1dj8podu-FZWyNzuMEWlzDjl3kspKTzlSJ0Sc70magLTxn6-8z6EkqTnWwK84H2hz9jSNeiWG7EigddA5AwrArISAt9TOfW1IshL38EGQoYcKFLixtXg4vDd3TK09hid5vNmr-n-wJy2jjcEa9NDz8e0Vhky0kBUpR4WzXUIcdYwzAD0VMZYLf95hjslzUP3slQQ8eTTUiIMzuzgVpZ4YOhZsbmy0Q_aSkAuPv-U2bkqPjj5zyuMdvNMFv0vLcVTpfPANwXYSxWx6QpTkhiUAJiQV-OltJOle-Feg5ZhBVDATUGIeKZNd9Fm0nabdPbJOaM2pRY5uNZR3DVpM0a2Y9y89FZCr-wv4q31QNYcC09Hb5IJYQZD9t5-RlRui4tr5Ly9I9S61KfZb5yWbmXwZVHKl5ZqYj_u301gVHIq3jbgOrJc0Uvu3ssA30CLJIaTSJGOvRtYO8z6gAbI97PgsXSUDCkZJPe_kz25v3p04SUl3uMTXHj-mmtI-oQXgMi4-IYfTqyx6aElEezUfhJmUjwLigz6BJottOBgn8VhwVH8UV_UR-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=XIleB6Rdl64NQU6aTsov8iC1paGWvxI6A-_BkhpKsMkxZXvU6uQbTh7ox8JVt8Uvy-jFUmnoFE0bZCEOhcMncR978JCRmk44gk4z88sjDIzQyio_QoibiKOkH0A-YGTh5qjPCxQMokWd-MXLE0D-aoAQd_K1U8miDxbATvRh3bK9MdYrwLlk3_nC2yC9HPCeAba-5ZtSCOtqohlEUE6I9bwckmoONA2az-oQVaDe-jk1C1qNtQ0Yd-Opp1clOy1IQHZjTKqkhQ4xZyjGuO9dr0N8YlOB6vps8CpjfIkgl4xQjdnrzkDPAaHXQLrsAPPsDFwreAj9NwwNiuegOM96OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=XIleB6Rdl64NQU6aTsov8iC1paGWvxI6A-_BkhpKsMkxZXvU6uQbTh7ox8JVt8Uvy-jFUmnoFE0bZCEOhcMncR978JCRmk44gk4z88sjDIzQyio_QoibiKOkH0A-YGTh5qjPCxQMokWd-MXLE0D-aoAQd_K1U8miDxbATvRh3bK9MdYrwLlk3_nC2yC9HPCeAba-5ZtSCOtqohlEUE6I9bwckmoONA2az-oQVaDe-jk1C1qNtQ0Yd-Opp1clOy1IQHZjTKqkhQ4xZyjGuO9dr0N8YlOB6vps8CpjfIkgl4xQjdnrzkDPAaHXQLrsAPPsDFwreAj9NwwNiuegOM96OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqSy8TEIwjkpUfR9-DxLvT5RNs9w5ukmnGqLFGH0HZZN9vJQmHwaa25sQ9ATdY2wz-0zzNJm82k-RxBOZ7pFjrKN-T3kUQM8kk5FW9ChyCqLBhwBDV07_isEOOW-yBH3Zqa0HyAQC6aCyCwwo8JChPJNrVS0kLutDSDh_GTsoa-v9DZGnGsZiZ_NKQh5UCsobC2bBc7VPs2xB960Ef5uZ0CW0XHAN5LODTfi9OayEygB6qobIvt5F4LZfdsRaDTFPe2OpyYEXNH_5yhc7dvVR5rNS0BttFexu5MEY1r7LXxBKn_ZyP7YUilEUGiy80sqqjE5F1YIEohWSrY84rbmEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnlXT7WxizqbJJHn5Xl43A6ZXJHJxLOhfLSfMijEz-_wOzI05etQlkWNxaOFzwy5UlS3bkuIn0zvnyRJPupRLV3F7hMXUPw4IRz7WFhBQlOJPPQdKao8mAFS1f0NUEea7zj7yKWuMsh5XeequpGqRqs9B861Qf9eexEOm-ksdVSw-elPV8l7fyc4rHRMfbafnGXw2QSgjp5DZg9xdrfy4CqAv1BCLdyOMUy4Ax1iZD_pTaclNl5C5fAPn4WpXdxhEPsKze1eR9QgclF0ilmHRwMlDWNO27roKBp_toi4tM9kmpn6QHKwj9vgos4plUqk4Qr5heCQbmS2MMz7q0GzDQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=CI1J7_7JMIQx09kiVUctTsKLSM9F-iMb96fPZe1GzqqsYp6e0DOS4jIkUeAU2f3Q5w7gXLnr3T1gNWRqY0cZobtTRwV9Ad4IVwNLxqswwSxXxpjtPflSPqu8qB6h_qMpI7Jq3lKbT1thNdRD0YW3MIVAhcu52eIRool3oXkm0OwNC5QeBy5Ti6lMs4gyTKzYhyg1vkP7hEh-e3BL6Q-_lYwuRWp8hI9QZ9yT4PDL_twKmgIFpLx2Ckb3pQXgEE1WeOgX4CzdnZljJ_4o97nc2zoO75Wr7FTLX6C6Qd4qAwgQanqg9STMGG_XFLbFd1qScWGRVTdVRuCMYeZA9bRFlg2-2wihDLhbukBaBgkck62Li8lH3ddSig2q1fW2LsQ1FSBEl58Z0akBDYV_cU2nI0OgVYzcMf9_o57NE-mvINPkCG92GgT_9iD5bw1PQefYLefOGzxohEdQdF971tvZwxCSDFw5IrsK7tCEeLtCZhhQiTDhaZ1Rhrv4Gjdc2-K8gEJ91ftiwMiTt6g9T_x_eEA2womO-IhU-uZ2iJNE2WpG6np6bZktusj27jBaOp4VuOxzjgdTOLxAVFBgqs5fTbggukhRpcA6m4YjIIVu7giggK0JaMoYorcaBEHLNoaRjUnhT88RhbzjWPGdOkutnDga-ueShqhf6UKBtADn2VY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=CI1J7_7JMIQx09kiVUctTsKLSM9F-iMb96fPZe1GzqqsYp6e0DOS4jIkUeAU2f3Q5w7gXLnr3T1gNWRqY0cZobtTRwV9Ad4IVwNLxqswwSxXxpjtPflSPqu8qB6h_qMpI7Jq3lKbT1thNdRD0YW3MIVAhcu52eIRool3oXkm0OwNC5QeBy5Ti6lMs4gyTKzYhyg1vkP7hEh-e3BL6Q-_lYwuRWp8hI9QZ9yT4PDL_twKmgIFpLx2Ckb3pQXgEE1WeOgX4CzdnZljJ_4o97nc2zoO75Wr7FTLX6C6Qd4qAwgQanqg9STMGG_XFLbFd1qScWGRVTdVRuCMYeZA9bRFlg2-2wihDLhbukBaBgkck62Li8lH3ddSig2q1fW2LsQ1FSBEl58Z0akBDYV_cU2nI0OgVYzcMf9_o57NE-mvINPkCG92GgT_9iD5bw1PQefYLefOGzxohEdQdF971tvZwxCSDFw5IrsK7tCEeLtCZhhQiTDhaZ1Rhrv4Gjdc2-K8gEJ91ftiwMiTt6g9T_x_eEA2womO-IhU-uZ2iJNE2WpG6np6bZktusj27jBaOp4VuOxzjgdTOLxAVFBgqs5fTbggukhRpcA6m4YjIIVu7giggK0JaMoYorcaBEHLNoaRjUnhT88RhbzjWPGdOkutnDga-ueShqhf6UKBtADn2VY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1jW8RzWAR_2Onc4WCUBO9JGu2s_Nk4tTfW4b3ASiKLd9Be1otqSO3PdjXk7Ug6PMCiHwyTOiGIPSYsSWo15E3NYpt2cdd9dil5_UiZ_zogeHL7v9DqSixV8T6TrPTpfroHOSSYrgH11v7CPEpulRk9Efx1XRIYUrU3Er95gO8H-rDEQN8f-tOsWFr7unoURY6G8pLdBYGsXhtUpPBUOjahlpb2o6CjS0R10go_-8N47183TlyJDt9IPNCnzN32CnUAz1OXKVx6SZ_oWZTDNHjzHqA-hNV879ewiv8LjYyrH03Gp7t8XFhIm7MDtxN2HVSzYAaoVbbitPJ6fMLWcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLeLnI_f6IvvxXa09ryrY6EFfr06grapsj5E8gar_uD0E_3q-YQLoAu6GukBZef1QdMO3Ale950GSyHKd02xspBiW8MGoJr5GY1Fg5xbs1a7k7-QsY8S6SJSq1pB4mksWu51eZVRlLPn0q8SmYrpYbJwGBwB3VGQ66LY1sLJ8NwPgmW6MviDRrjCBmn_zpl4Wz-yYX1tSyFKu959kf04tYUTQUosq05-QDnu59Zf19q4M3KXPLaHMwxoJdY5TXmkobC_kfiwhQTpjfB9vOKaz702mEoj9j5stgNjuMd6Cctuo316hP74ODwFcy9c0_6qTb08GM-Q_2Dh81183snwjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omlXekVFxZUY7ffactJZqqW0Ie33QpIyB24dxVJLKH-u3MbX2oOXdg36l9jgcQTkWCozMo5qeNGrhxjP1_2WWFvYSAHuzQc6RUoZ87demQdKmoxdVxd-SuSH5GLOfonissgehg5EzdcjEGpiH_Tob_85TOKPVeXjJ_rY17opBKnn2Olp1sP4B8pIQARDDcxkPqMvi4A4RrS03FVrLOcH-o7DBeDwYPc0g10RlfwmSKmWQKVS2EaQey9HDXvz5IAeW42Cboikvjh6Eu5gNtFWswuNONDz9Lv-qerbsbgvSacURbdcdrejjJjgy1I9EtiEo5-reJ6pVOvPocItZfL5pQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=rHIynQEZvHTqgHToDS_2aLb5_qeAzNnZZaoD7QihP0HKHI6XfAYDpZWZoH8ujo9r0s3OlLz9_fEs4HNRLbWFqatiYfDzk6IZBGH0_GwGNXzq3Fb9nbCWjKXQ2qNxFEdwDqgrBN6vSzy3HjX8a5qjaRXGehPtCPMSgUzC-r-qlfdE_W7Nn7IqZF_sqMXGG7qbtp-PpgPSXI7AmRSC5ps57vMA-dE2R8vlARgmxvkgCLYwIKZ0PEqsoeZ8kQgIbvxC0ueCJH8MQD_4YIdPUt-pmnLp6Zzte1b7rNq18CLyLpcYgGhuIwadSIpPG6qOrkIUKMMFclkE8ybnDOsxDFng2xM-rich5FYxMm5Gx4CH973fd7uHTYUbBID5Som_zSSt-Zu3F2m7t3-KLQ9ZEAdCeGncD1RHrrt1HmTG8F4iSU7gpT4oiNhm0WooJoEoBgXB9Ju3cWglDI-olN4aTdilOYRaumDcpsoxUZoQSxChUOvAWSlNS-bKGM-GVChzl7ZwMY_6eAVyeVm2kGmDhSaL-5LnHlrMMfH26L20LdC7FkFD6W5E3dtMaKjNuglhbhh6eVKPezo1tRN9AW5nxub9h4598K73mFp-soezsJt0clhNcz5nIueAn3vBePfs-7ROsJXGntdyUxefPXI1t6mQeCzNusjRrTFkdzT0-9f1exc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=rHIynQEZvHTqgHToDS_2aLb5_qeAzNnZZaoD7QihP0HKHI6XfAYDpZWZoH8ujo9r0s3OlLz9_fEs4HNRLbWFqatiYfDzk6IZBGH0_GwGNXzq3Fb9nbCWjKXQ2qNxFEdwDqgrBN6vSzy3HjX8a5qjaRXGehPtCPMSgUzC-r-qlfdE_W7Nn7IqZF_sqMXGG7qbtp-PpgPSXI7AmRSC5ps57vMA-dE2R8vlARgmxvkgCLYwIKZ0PEqsoeZ8kQgIbvxC0ueCJH8MQD_4YIdPUt-pmnLp6Zzte1b7rNq18CLyLpcYgGhuIwadSIpPG6qOrkIUKMMFclkE8ybnDOsxDFng2xM-rich5FYxMm5Gx4CH973fd7uHTYUbBID5Som_zSSt-Zu3F2m7t3-KLQ9ZEAdCeGncD1RHrrt1HmTG8F4iSU7gpT4oiNhm0WooJoEoBgXB9Ju3cWglDI-olN4aTdilOYRaumDcpsoxUZoQSxChUOvAWSlNS-bKGM-GVChzl7ZwMY_6eAVyeVm2kGmDhSaL-5LnHlrMMfH26L20LdC7FkFD6W5E3dtMaKjNuglhbhh6eVKPezo1tRN9AW5nxub9h4598K73mFp-soezsJt0clhNcz5nIueAn3vBePfs-7ROsJXGntdyUxefPXI1t6mQeCzNusjRrTFkdzT0-9f1exc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
