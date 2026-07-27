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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 12:21:40</div>
<hr>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkx454vvoBkL2QCkWSqTFWzq67WIq0x80NQ5OAMjJizy9zdo-o4J1-CKcsY0AZN0sf63sIk9pv6b6WyOlAijamLUwzjcwT_wgrUxZfZzqQxT5lRSwxiesY1Oqegq1DuWX5ILLqyc6KJl7dgut9HleURDl6AEmTgaPKTCQZ1NUPzxZ2zLMy1nHOaSRXaL_yezxMLD16op68m1hF8BERYJR_M_VlKM6yjCsvxVGPdmTkEp_YxOorbiHyA39fVroBmYzzH_dBIcM4lJ2xoyapfLiQEEILG6P8I3CsxD5X3dVsbHRkw3JuQNR_Y2yA07oNl-xTHzoqHvMVD5E0O1VhUXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ucZAcftuuQgE-EApzcxILZYL2BFHKTCDuOg63yoQRc9S2qUjDSbLrYt6s4CKJhZYZAXmabm1YCHWUXae_J7QPu9tuUlAMnwa4bB-NkchtGBXxcCJc2mCM556dKi4pn8NgwoxxqYliUvctLAhuZ3BtcISAt9qhXZFvu5BRsdYJGevjHlnTV5Kc0uaUviT-jVmW-nrD2xPMgX_j59gh8CoEHJNM0TJriunvCNoJl2mDtn4BVRVWk32-kkU1IE9ZQsSeTye4nRSBysnP9u1Q3kTps3-vk4W1kpnHlplQJq8YdYFKMeSYQN4dBg92zKUGSI5vQ5UinlZ0qn1h653wpOQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=ucZAcftuuQgE-EApzcxILZYL2BFHKTCDuOg63yoQRc9S2qUjDSbLrYt6s4CKJhZYZAXmabm1YCHWUXae_J7QPu9tuUlAMnwa4bB-NkchtGBXxcCJc2mCM556dKi4pn8NgwoxxqYliUvctLAhuZ3BtcISAt9qhXZFvu5BRsdYJGevjHlnTV5Kc0uaUviT-jVmW-nrD2xPMgX_j59gh8CoEHJNM0TJriunvCNoJl2mDtn4BVRVWk32-kkU1IE9ZQsSeTye4nRSBysnP9u1Q3kTps3-vk4W1kpnHlplQJq8YdYFKMeSYQN4dBg92zKUGSI5vQ5UinlZ0qn1h653wpOQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A91kuYO3TzFrjuaNItoqYRpI5zEzGD4PwHzr04UI1lm9DiEwsKTeG_6kG02R2RCwwOmP0h168EzxOmeE7cwT2zvl4eZtSvxb2-o9zZd9dFsDE9ka0FPGI63mHUAqTNWcYYv-bkcMWr4VWrqXpkzcOdZubFXk0Zd5jWChMiDZo5_Ykg9w1Lp9bkIxYfPNRwVWlSmA40B-psnGM0OVXtI3YCRTm3DXsqwoGBFhGncgp3EyLDOe8dFiX2HEoQmD4YviNHFOWsGw5hYZe5ZAYQo6jAHfvbdBigLD5TCaYbAl9ovy-nBTbuPqVXNthWX0n7G5oSPfsKz8FgleIxWnhYbbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edDV9CjvDEqt0FpOCHD_yBMDypzmgXqWDY6dm2flpjbY66GvUL4sQSAyT3XYf8jk0beJZo-zX0dyZV818M6lxpZaAVMpjaK5cSjIzTimwOMvAl6FjMhBVPDCsROKEw4lITOYG6pfAxO-n5f4IP9JkXRt3yE_UrRjUqWMRc9EgERWhoKikDsN7ErGvFJqz2EQQvYoGHtiEYo7Ffpbe6NwDDk-8Cux1Fp9OkuJtYCF8iFDqdPRjgtwoc4CgP3fc_7_16dFtsZ-Wpv8SPuEntbB2OnohSG3WS67R6Xlz6QKF74CxWkraJ9hCNDHxQE4xM9BgfVQ9H1Mf5VfHnURQI69lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGrnjk1HjFh0sQjWt1erjgerVUKmQwtCoOrtugTug8iBR0lte3ckwy_LfEktgD47Kdjagkzdmx-lmYYUCUyaTJDEFc_IBlZQxp2Ld0OXLW7o5_A-a8aYLU_IJ7RLpxzD-8EqeGHmIbHo2NaVDcfoUUGcapNMbnNUEKxy23ZrxcvHdUfwNNICL37KwYamjdsdPhHsk2frJx6EE4IfyAe84xk-NeDhA_QpKGJ7eZSDxPerT9CaZ2SLjkGnG2BNoylFVHHXplAVSrs1lC5QsAb4GWJLA1MnUAIj7TIkiuqneBD8y80PDF7UVAZ7O5ZOqY7PwO4ieUgX-z0_HurUmVhdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BKZez46Xn4GI-SoA93oRq_kFbqKOx0FhD07p24HU9Yczv9sF3dSWgZP7hsZseQCXO5QKHI-cwbK4-Xhm7GCrz-xiB72zkRArw8zvULvhnW9-fVXA4OGqwPeenPm3cyBEe0sYCqmzzXU0KzjVmkmK_abxp58aZM40lN15bJlnzZlakqpsOXztFmWv8s0ClZj4fk54TycjiPxjeSoJ8Jx_i4Bn_ZRA2KFGKI-YGY5lJJ3FJCSqsc4qVJLZqIQ29vVuzZg9oxrWXawFVWqFkY_-U0KQ0Hl5I5709E_TENYb0Pbe2_NzBpuNA3fmjnYSkkS98oBJoDjtZyxNudnuj5cGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IbVM70X_5_B7MbPQQs9gr8NsBiRoMGSEHdTFwlvfMy0y0W4ZStcGrD1IyTaIv3OLMU02GobSzguligzXBg2r0xyOi03HhLJISSbRW1j0XNWh-0n8UPiEqX6cj31FjiEFEHwTUkNHMvmLSEjTbERZqu_GqEpPLhKHfKDZowkYC69DMSQyyzrDtTnsWnUXGjvrOQ5nHP6_THjDyfSUc5cWeccv4Tvb4rz5LJlX73ijolFhRLbDBCYD0wyIOTz-FkwhddfyeCej9xL6NCOe4X6SyWWthLeBuZ0TKMrEBUuEXfOxfJ6F4g0APziCA9_nPaoud2nxPv5AaBM41aFnsJF63Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEgMOSHveFO1xJ4gaGdBP0WhAis7h53aEUtzooS6oZsV5BWmFapNHX5_q8raGiGFQgCNJ-t21nnuYkojlkvIDFL6fbCtNWF_oWtlr5BPhsrEamfepi-_ROQHb-BF0QdOAZKhyWnFUaLVnFIQVL54n1MFatBqWE7VosQ7LbnX7VORu9NAfcvu41FJ0YpuFsCoWRYo72zV4QkE5qgrPA57lUV_D8RmwNMmlfBocJMYeeCunRHitTslXVOLltk_7xu8jkVUepKElX3CuCnHev6ZKqdC6Hcm71Hq1jOaCqr1kSYtb52zbkcqXabLKsRR5NwJcrRgXSfxuZEYAJ1da8Hhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJVNluKjno2kvVW1LeJV789-qsdhlaDztbwc9_KE8uv3RdNNBy0BE0FcedZz7p3uj30UtywUjZJI88RQQ5ae5SQSfjUFsrzAYyErh4_lTeEj_3f_G6EVLcl9yh5Xb_ORh_ki6xB-aKgL5yLtkLrHEPtoRKyBmpDz4wRmeSG2flhTa61va8bhH90wf-UPgL7QIhLBxf-xdVgolrp4f_xOFvLtkWl7t0m-5eB92bRYMc0vAAsFoNG1GpPA3ZxpGso37cBIRsHA9cCOcormPNmPbqHKLPZZe5zDXVld72TB67F5JlGIf_5JKL6yqLDDg3LwEhJoeGw4SIvpquvm3VmCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/km_yo_hOZjETIqxDOpoRwrn9pCGcx-Q7HgBzRaHt-bwDl2ZhP-lVKmNQWBFBq3PCm-saEqpdavmVwrIBoy7hHg25VZw79oBrBCrnaqjtRL3Gxaz5SeGCOgz5Vf9ySgnNI5R93hRJEsagVnmcejm9u-QicMGhKyqWcuz-GlWNr1xxxVaMMmA0Rz4u0Hsey3AKyyDFCEui3kBHd0uQf0cp9EHzSuXhWNzfdU2CnnQEpczyN6lTgDqHzBY6zXRB56lFvUtQzuJ8H1UhFYv5cbtXlsFY2EO8EZh1so-LXpmAnL73peLRi2ouXCgsdadEraDC73UoVXA3OEVOt28Grgg7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4JTaf0vHrdOtGcnXmHTq1egQcb3xOXdf_W1gw5uAiWtzNhNR2dlQ6HG946Tm2aCi7MqeO9drxwVv10XxZ23lTKz3u4LB-pmVFIfY9Hr9asa8sS6oWjsD0q23JwS5f0Gi0hZuf4TmFxy4AizAVisGkf8_TYrHIz2ioumaKVzKmEf321pRTKIbaI0DZSsEphn0BupyYqKQB9XjtLHAklpu3ZfHiBSvCr7iLsM3UDkU5u-UJYogGBUlexjdX7BTKgOry7u5v4dgqeZEjKVn8H8fjl6z0op5q08lgNwUEI1-8DFINnDL3efqLZ5P6H1t7p2rxp419HOuOtk_bgHbt-TvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zh4h0iRyK5zhTlNO47O1CQcmXb_9PkeeFOy69p9mN2_9OigEeGrjVpgHtviV5SvNDbsXIdK2JH-G5oI5LdSPHxI0J0fAZYlrDyZajhAiYO11uL0UxuNoKw0LPvs94wUIcuWDQeMNJWEtiJXYrfO6xXiMw87c2VW2yxPlbCQkKocjVZJRG7IP8LQ74h0kkPIuFi8KKqBMZOoyuKynugL6Bp0po_pOvKUyS2FRCrdrjvd34Z0BrPUjcyjA0Eivi1b3wT3ETXDTHJS6S8ygri5QjAcUxKR6rStIJQyuqS-BazXTC7tGsQJOneEb55VES5-JZSBb2YTr_ZpGRI5afZDCIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVHNyHPeagSnxkwEfmIrKKeiocZOMLHac-Ampa5iYk4oKWnbnUQ5mmDpj43K9ZZi4ScMe-SFPpbMZp1b374940tv8hyRarAZClhCYlCNkGyTcpRQds0j95atYiMfifXFOZGGgkLPwwPfCRVRR0k1WTNcrkBJMJgZ6qvZk6wpv8qiVbtOlxQqaTASMiclI7q0gZK8jMWIL2hhoGbNqhuD_Jfle6Y9VBm_9GALlygBHfOXYwj9mjO04vM28hgbpjJbAiRy3v1y4AFppInFPv60GbmuRu8QnFNqagehXpjfvLfF9y6oQ41jn-rk4p8tS8jLs4_knXKQ7Fkm41mt_U8Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU03JBBIUrINr83zJT82G-VOKqE8hOi6VDow9Vk_JrqmtdlDqAZ4VWG2z6kPYKYWnTvcu1ghQYhN8YxdE3WNEs-puYUx85kYY4Gj7TJ1HIHBl-Z1qC3StQRjFiHbT7CppiHHAE4v1oZPOpZUMXOfdcUN1h9ilzqqgRBd5aJhbmIOAabbejFL_KnA94YSUmqaZULOPgbThc7gMMVMBuJCRXVs-BoDbGEmpCSNmoXpnK2UBLLuvWLwEo0C_AmejZoVeeOOmnT1FrgCm600e-Zya7Q1SPA1SiH57ooZqksGRi7Mt7Z4_If_Z6p7vDT3ipcJFoN3pXnyeMra1mG0EJK7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pC6g7mZJ1gx_nFJ42ryQIP4txktMyeeh3lCwGqdFB3zWm2nbYN_JTkzaosGloSqYqGY91roPGLIk20FFNCm-J4zcIfWmj4oK2H4KEALrrNo3XcYRbQ6EonxqwyD47NRbiekl2ryEGB7cm_5WqXM_l7z49yHxjWfjOh2aa_7Ry0j0fCFxvnZ_zIVFdXTacgD73kHGXmRP8HjhKSf7_x4yUYGCvzKkDlKIDrk0t5oY-4gN_Cuo5Ng0NCT2SApwYmI0LMDxF4EwrRIQOTo01me7cFV6fMS_JIuVP3gLq-risKNuWC0YlnqOeLGqj_py_nw8soyG_qAAPpSBaL8upR1lJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gthSSNCKc3BcDNXZc2TqfATKIMfv9Zbsxum1xhGx3d68FeT-zW9VBhJVLRvlwnl8ZB2QvPHhlPjd2gm5rpL34hYEpAti5T-VnSqXN4OyoBiPvcNR3N7H0UUgAWFRy2plhgnpOadu-Kk5mlsLXyplyN6CHIJ902fbeIS-Orlb2Z_yO89fwETCtlFXsHI_qvH5y43TCrrTHe-WHjEcdxJ01hV5at1mvyqSHdWgzCIoNY8YoYs4xcXcFzW5TS8lUkSEerdk5DQEuDd5fSONbqkxNoueLo0yL45LhN77ebRlUZaRF6We-S0tklji5-ZM6RfrJ4V7EvSLwYdOZszXcYzolA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpTESoK2_tYaLOiq_JjLOZ7iQVr1QkE3OiR1wyqrUIiZ_uXf5nPlx7uj8DtFv8WeFGUMfFdTSnxW_33U_A0XqkweA0ejKs83Xy39HinoAu_tsu2_ZM_ov1uW0TtBbhYhLK_DuVEm3o5y6J8Or8IjVZokFrACz7wYMDt04pkBx35L5Qf_0bDvyj53qD9o3eXcvv_GYv2uYpHVXEEiciOuDsJfnsXVGuscrF76fb0-ioxfo8BikfiDWePdWXVpBQ_oWM3nOCdopwPO2kUB9mdOfKjMN8hkjigHrVjl0_e5sV5NiGDRDlV5m7OBUEo-ZvpJH9wWInttuuDyFbUsrzWPog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=e_oiYOgDCCDI9SlfSwBtKfvY8s2UsJIV4JMq5YyQpVMznpNMSFGNaWL19jtvXW9eNa8px35bTTuzvK-ltFRidI-JwEVwNslm5M01IZFsCp1sUyp_rpA9SjE2cC44uF9IqHlAiEeoohUsIbm7uUW1Qw7zpsCYJdKQnz55LKhEigCYO9I7xt3UM3Cj_CczJ2pjsoILsuf40y4zj-E06oC4FAJhE2glhNXK83iDrUdNLVdg_cQPXZI0MeKssZd0DnKsHW9Iyg1xLQe-r0_VutTOhM2VrkiNUm_QgGkOrmdYSFLIO6la_Tmy_5Jlj2Br7tkpgAvc7cguHO1G8_lHNsQG_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=e_oiYOgDCCDI9SlfSwBtKfvY8s2UsJIV4JMq5YyQpVMznpNMSFGNaWL19jtvXW9eNa8px35bTTuzvK-ltFRidI-JwEVwNslm5M01IZFsCp1sUyp_rpA9SjE2cC44uF9IqHlAiEeoohUsIbm7uUW1Qw7zpsCYJdKQnz55LKhEigCYO9I7xt3UM3Cj_CczJ2pjsoILsuf40y4zj-E06oC4FAJhE2glhNXK83iDrUdNLVdg_cQPXZI0MeKssZd0DnKsHW9Iyg1xLQe-r0_VutTOhM2VrkiNUm_QgGkOrmdYSFLIO6la_Tmy_5Jlj2Br7tkpgAvc7cguHO1G8_lHNsQG_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v23xyCQPodGoN7ILDj2oXMItE0jXZvliw56oLEyIv7RkEhZlw7sfVJTOmj7LGguTuMOok6priJMX2-oSe1VwgNf7Gn_OPFywseY_Kqwy1RnYCg-EDWqnBZb9YpLK5ZF-0HOshdMKRH1flTYMHF_kFUzu-Rz02Zb7P-5kSKys1vs4Gt2YFF43dPWYVvvYJjkWqEtogBUSENwnYYEDEWxVZZm6eBWshXDbxRz306kuUVU6yEG4LuO68z4knCiicltxA9qJCuvEr_s3Cc_C-D6HShD29NRhWOuUv1Apbs9-rBJcQBdIaN2nv1EnvIM0fAZfQRlM8nB5pY-R16ImBQBtSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMMLYRvRhJEO5Uy84ognzbYInFYa_7mx_JHWsC1oZmo5lMFbXk9OPlr3yeAh66oUUiXDup2yU1kKU3TQvspKf-7RFGF9dDfelGFlWe0wC17GfPy9FrUHHo9zmeONHARZKfJ-TIdTZcY2Fe9JpR3eNXgAgrkx09Y93t-21oAZwxFQD4-3KUV8fbmOih_Hos99zKD5Lq0jKsxtx42E50PMYGgJEWSvA6s3vQLqdSouMpN_8LiGgMy-ta_0414xL_gaqrgAWd7DYWUvrK8xBBOqGmaJ3ioNyG1qWZEM4bkSUgg_2XG3C6Rw_UoYTlEjBH96sowe4au23Wrr8LIE-w_jsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJOXI_rrtkYdEHbPqmTRDEqMVhoMx9qZZdQfrs9auOHogtbFzCXtfRMCrGvJGR7qg_jhWFOIAMzhMUTcomGyppWzRc2f7IEK9IGluk50VOwyCGWuW0I3fEKuZVjkneTaE6qbLhRqZD6EaP37tkMjOVJwTge0bH-8sNOOi4_vQiro75wl_irpZCJzjDPekEJha8xI8ffhRkOtcA8fogiGlyl6rzBlCAI4Jjn5RK92UhUbEu8g2WsdPuznzVGmjLJslrdpYVZX6oSUtRNLfWexoOX5nmfvteug1h3mh4PIOFprSaeBaxL9PVI5GHRMpH8hpoFQE8ueHc7EJfP0suMjtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=W8OPOKIYRgba9j3cvG3-qijs8APW7dRSA_Gov232u-QGrdSHKAVyayK-2H5UL_tO6kzVnakeHkxsW9t13bhHgLXlDdVeOr8kMDNYBiuLjkB6MdbfjYAFgduAgurptp0tmTosyU4LC0vd1YqfatZIBhyy6dZHrA-XrZskuL2FxGkIooKOORQsXrXTq-oSTewK3i1FK1_pQZpmcuCmhMmPade-w4C3c2VtoWkDrFu_pqiMI8O1_Pzz-JCD3lFLnPgFmOvAhyNyP1E7oME0-B1wedCsFtwdN53pWTeZcp2XQvyRSCwusSxvgS8BfkhrWBbnNSrx-CbMgJtn6LeD37Ybmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=W8OPOKIYRgba9j3cvG3-qijs8APW7dRSA_Gov232u-QGrdSHKAVyayK-2H5UL_tO6kzVnakeHkxsW9t13bhHgLXlDdVeOr8kMDNYBiuLjkB6MdbfjYAFgduAgurptp0tmTosyU4LC0vd1YqfatZIBhyy6dZHrA-XrZskuL2FxGkIooKOORQsXrXTq-oSTewK3i1FK1_pQZpmcuCmhMmPade-w4C3c2VtoWkDrFu_pqiMI8O1_Pzz-JCD3lFLnPgFmOvAhyNyP1E7oME0-B1wedCsFtwdN53pWTeZcp2XQvyRSCwusSxvgS8BfkhrWBbnNSrx-CbMgJtn6LeD37Ybmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mm2gGjAX-RMJVfjZlqpER0Py6E-ePUryJFLSdBA6HDpGDk2_PhtPLZ-P6IX6JHGcw1XgqMla-YwpMd0CK_t7FGXTsFzfcVTAxpMNpuq0aGw4cjviL_pCEgu8BN93EleugRCqhdNYonmD3EvN6_AyN4QLyOVrk-KHumMfsMg7ceNQ1KKQ_zIqIuYDAuIQCQpI6HZKKzwzXfSiG74OcwfvZ3rK68v1CF2KQgeG1CERCCiHrh8rUXSgh_gyvn0K69ahD2QZUiuIds47AsuVlU6CJ_W-d3VUcYeJtuQqRzaFlUVi-rqGnq7h-xKyrV4KWIy7oxdoKYbNOiiOLRYH_KAOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=NzxEkJM_kcMwQmo-6722AVcYc4vk9Y0o9u9dkrbiUE4Lpdux2vszVyY4ab2NvtB6pi1R3saSQYkz3sXOwMPgnkL0ihPFEERwSniiEelf_af44MZFlZR4_1iApcsJOj5Wx3Cpk6QPtnP0ie7f0ozZ3wEv4DDtignvBd_kxoYb-Qq6V7Mz6FqS4FqBSzJBx6TtAOXv9G09ADJe3RnUgRiyIiKzcisH7rrnh_AUR3fFMol41SKPAd90sq7wfqCCdNYT9FQCjYS6SxgRgZ-EKfp2y138u-Y1nzVDFF--Dqjl4JyI3qD_4pn6sS60Rw2XzM0jo3ViMv0kHFswvl942CXkLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=NzxEkJM_kcMwQmo-6722AVcYc4vk9Y0o9u9dkrbiUE4Lpdux2vszVyY4ab2NvtB6pi1R3saSQYkz3sXOwMPgnkL0ihPFEERwSniiEelf_af44MZFlZR4_1iApcsJOj5Wx3Cpk6QPtnP0ie7f0ozZ3wEv4DDtignvBd_kxoYb-Qq6V7Mz6FqS4FqBSzJBx6TtAOXv9G09ADJe3RnUgRiyIiKzcisH7rrnh_AUR3fFMol41SKPAd90sq7wfqCCdNYT9FQCjYS6SxgRgZ-EKfp2y138u-Y1nzVDFF--Dqjl4JyI3qD_4pn6sS60Rw2XzM0jo3ViMv0kHFswvl942CXkLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAdIDnWTyV7oxtbRXLJM8pr6ltqs4eKQVfraXf7qYMFgzRA7iV6-VlRwtH96HVcadYTZXpL8Fmq1YAOI1hnaE_dCqDxPPn39ThbSBgpD6GO4iPSPdsvqiRzzcxeKP05yJfnoF8S_bTN0LlV_cKDxV9k7srLFevVLQrZYF2nUQ5S-3ZuEWX4gHDb_wkd7kgDipi64UrBBqCK8iM8Xh6nlzPNIrqSV670Uh__O8I4OxNIWgMp9Kf1T8ghfydTD__DD5Ya6Q7rj6RGwOAp-hfVbq--unqaEfNhfJ40Fg3ODU3Q-IgvLbalugVplKM4cpp-Ewc2I_QJSlCotokl0TNLc3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WecsECtiBH-_ctL9Et3z3GG-gOFQjdcbYECTPMFftlkQwp0bzLVhAGlTNG9SKe2J2ldtYZd25WdMgnDjHOhO4gwtmUUeJ4Uxz_znWlrxaov5dA-sRooxvDM7fbFOTowK1K650WRl25jTioqcBr85qhqdsstI0K2Pkcjdy1fGrRaDY1CtV5fMSD0hd6bYWwbHTYDlCPJG3S46bHMBT1aE0cdcnz94laBMIKXDqssG_YwsXkG_Fwoe0e5uyGgxR-PNNn-jREE-3lUypi8_SkjI6fvRc5Vb78cIv6fY3liCyt4S9HpDga0co-Ctw6gfXvExs4uhbBtJuhVnZAFEbhLwaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=apqo-cMTv8BL9CW4XNfLMMaxmtF6_TTPpdy9FmtYB7ajA6nEXhVuJHfb8LghKagZAjsF7Jv_qnNxdk0HOMSVO1BlX7Tdd59GcU828lxXUfqzea0PK0NjJPsHu6FHQk5c5N9zc939ySMZJ3vOgM_V2Wmui3Yjus6SazEs3gQhg5F88XgmxiEJ9ZKolXfAWQCbOi8mE_oNoOdMnz2tk1IYj9PBjzy2DJwI53UoTZdL0-QXvdUI0NimCqCwdUsDKg1gkKR7D4tUHdlmBaGQofVVBYrbYL90FmP6BG_tpgZ3VVyjeyeIAXzvX8nimeXdCTxJmG4-j1PvGAQ6Vhg84ZGwgw8s8AhD4kVuT5m99k8qUxdJNJHqu1bMbskS_Td1Md5J77_vfkXVGi9NRGMUdbg5k_i_KvsxZyWGIG_-TewDfddBN5ag4j5cbuRmmZ5Q51U5aecLFTfCGnbuBn4IJn1n8wkUobZGFVD7_K5nhNQoX5QZ7vK7kAGZfmVFh7LFVXWwmg1zJZ2egJcts6oubCUUhwbNbJZah5o37YJl3qz3oFCLCGtVEOWLyV-Kd3JFTfEBRf2ELHiuodj-hrJL_IeTwgt-5MYXlxs4mmkRaFJvOTJpsNG570OB4h76MfMzkuUkQVKUH17hLPq5-lEEI7y80_SOfib7Onr-xO8EXpVotic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=apqo-cMTv8BL9CW4XNfLMMaxmtF6_TTPpdy9FmtYB7ajA6nEXhVuJHfb8LghKagZAjsF7Jv_qnNxdk0HOMSVO1BlX7Tdd59GcU828lxXUfqzea0PK0NjJPsHu6FHQk5c5N9zc939ySMZJ3vOgM_V2Wmui3Yjus6SazEs3gQhg5F88XgmxiEJ9ZKolXfAWQCbOi8mE_oNoOdMnz2tk1IYj9PBjzy2DJwI53UoTZdL0-QXvdUI0NimCqCwdUsDKg1gkKR7D4tUHdlmBaGQofVVBYrbYL90FmP6BG_tpgZ3VVyjeyeIAXzvX8nimeXdCTxJmG4-j1PvGAQ6Vhg84ZGwgw8s8AhD4kVuT5m99k8qUxdJNJHqu1bMbskS_Td1Md5J77_vfkXVGi9NRGMUdbg5k_i_KvsxZyWGIG_-TewDfddBN5ag4j5cbuRmmZ5Q51U5aecLFTfCGnbuBn4IJn1n8wkUobZGFVD7_K5nhNQoX5QZ7vK7kAGZfmVFh7LFVXWwmg1zJZ2egJcts6oubCUUhwbNbJZah5o37YJl3qz3oFCLCGtVEOWLyV-Kd3JFTfEBRf2ELHiuodj-hrJL_IeTwgt-5MYXlxs4mmkRaFJvOTJpsNG570OB4h76MfMzkuUkQVKUH17hLPq5-lEEI7y80_SOfib7Onr-xO8EXpVotic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=cN9mLzNMrr5wHYdHD39v0HZUBh-D6D6Iag0lEQjLUAGe3fFY9vlDMLjinQg9-rzLr4g1VXyCIAfFkhPuS_OWwuOoTWPLyvkvu40ReK_-pgeldbzf3VDqhRrofRjASolivYjeFqs11TQqkyd-D4aesF3bzJhUrPyhtcXVYpns8nlfDZBdJqlI1FY0_hom8OkMm2n2R6PHm-hHuEL8oPCq1cYX7SHcebQ7eueZD84CViFJ5UctPp_2Uo6uk_2lQLuTkf3q82h7huqduFKl0i1pu2CmkE-bqhrGX1mC5VxvQtlnyFZIX3dy4LE8r2_-gEb3mLVchawOgm6pB1h0ecIO0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=cN9mLzNMrr5wHYdHD39v0HZUBh-D6D6Iag0lEQjLUAGe3fFY9vlDMLjinQg9-rzLr4g1VXyCIAfFkhPuS_OWwuOoTWPLyvkvu40ReK_-pgeldbzf3VDqhRrofRjASolivYjeFqs11TQqkyd-D4aesF3bzJhUrPyhtcXVYpns8nlfDZBdJqlI1FY0_hom8OkMm2n2R6PHm-hHuEL8oPCq1cYX7SHcebQ7eueZD84CViFJ5UctPp_2Uo6uk_2lQLuTkf3q82h7huqduFKl0i1pu2CmkE-bqhrGX1mC5VxvQtlnyFZIX3dy4LE8r2_-gEb3mLVchawOgm6pB1h0ecIO0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_K9cgliu44UqsMWyFqbZaQwnZ5OOYmgB0IPa6qmi1PwEeAmelZft6A_kUL6McjB0cHn6cFeZt_qHzHYms9X7s6iW2zTJtI73_Mqx2HBsytOvBhJj9Wzit9DU1nMIsGP_ks5wXKOc7ELn360SsTDPnIvjs6VXfg61Ojk3Vz0vaieiJmMbols6yrLv4wtvRq3vqwo4kSe9hFNTRbUCoHODGucpoRbZqV7zjgoRsA6RRe9t5agKhWN_Havw_YBzo_wMsGiji5ghzZXg5QBa6SjyrQfE3txo6bwyLOj4Xy3N6xK6O4J1yp-srb0PCpFzzjeAk0vPr5n53S30VrdOxmv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Ea8VpF_MUFA0Jrqotovfrm3PejHHJzYqfEJbauYm4KIk3TlagDeTnIbtr6kKceanyV-3pk_gmlQwknTEZS0EMw5vxXl4lDvzgWQP7AvAUW17km3lr4CkHyeMIw9QRURWca6pS_fqKVh53HYvYRZI6PH2cRnLdo4npyM3qrKaz7sOOjS27DKVd7avzje8rEJbTJDIGw0P9_YpN9crVjZEseWoyoz_uUylWl1rhKH2bCx_FB4Fs6Tltw7OhFeaPX5d7YqywCr8a8gFmoaqOnNEO9Rh7gr6Vw_RVQzd9wb1JivXATRqBmnkLeXjQtn1PLBzsc-BSzVoyr92hMU-_lZiMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=Ea8VpF_MUFA0Jrqotovfrm3PejHHJzYqfEJbauYm4KIk3TlagDeTnIbtr6kKceanyV-3pk_gmlQwknTEZS0EMw5vxXl4lDvzgWQP7AvAUW17km3lr4CkHyeMIw9QRURWca6pS_fqKVh53HYvYRZI6PH2cRnLdo4npyM3qrKaz7sOOjS27DKVd7avzje8rEJbTJDIGw0P9_YpN9crVjZEseWoyoz_uUylWl1rhKH2bCx_FB4Fs6Tltw7OhFeaPX5d7YqywCr8a8gFmoaqOnNEO9Rh7gr6Vw_RVQzd9wb1JivXATRqBmnkLeXjQtn1PLBzsc-BSzVoyr92hMU-_lZiMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqZpCv7mzer5KG2nn8QZNLKX1MQIb6_Xon9tU7hVHDaAbAAMURrgR0tIayy_UPXu0k7pQk3zvrtH2XspY8HnjNNfGcoTosX4EhQGXJ7AliPtPY9tDbO_Riugzvx1Zwcgl0CuABthdS9w_uErm_LKdVs1XNi-DiFqtea_6KLf2qPVCVrZzaFIPE80-_TZ4zjMPhms7Uw3oHYEc9nD4F1ArrjkkeodYefllaC6Vaqmhhu9_X6R2g7ZC6aXUKiazl8EhEoTfrb5Cb71lF5kikCwxHhic7CVYAdy73cKXGVvBQ0LNfPCUDqJiMp4f1tVTauvYyosjnKu-7X26lx-0prZfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwnICZagLbIcUAML0oZX4PovPD4dKZ2-A2zLKQh_ivYyexZfJn429scFplfy-4TOgZzc5Yy1Y9x351CJOcIIXmoPUCSaH9Ba17mApe7oKnz7pEJauC5hCSg1SUYZOICRtYFJejhOJD4uDaKIQlMBdECG-JIHY7lL2Ur7Wq4tXsB6MMrjb20Xh-DiJ_sR648ttyhszg7dCJuxYlhEnk5dvNBKXN5gsveH73Q3Mp7PAwfI0hTxLgur6OnYS0B8tjTA2HqQDTYuIj4OaWq424gLJ1YDrULqmgi4RRAdPev93I-RnRwiCn_ULLEv3Ur4Cztnh2v03gCSkhIiN_ZeO_dcbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfLU7qKkJNQFtoV7tNEiLczKfRMT4fakwibqGRXrRKBZzkTOK9-GvPj4LP6ORW_vyqzD2SF6njVQaRANSCZLcYNr9FHiS-RNaKqQNTenL0H0YEHjo6ctbvnSXqegCbmt0cvvt6rFF4QJqEKwdB7ykDmleIpB-Ov7ZMdhhnsDuFcl7RFoIKPuGX7iEnt6hyBqOsvO0l1tpsm3Y53CKt2HNFWAiut5AsrX-k-dtpGAdoJ5Ul-ZekCKLrmDTFJMymPtmo8qBlULzcE3zob7V_561s8aeWpv11jhGpf0R3Hco0hLQZcJCw0GODdLtcZ1y168JFl6IZMGcQlE9Q1ZHQHMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XT5AQYT8z5AoPLSaIbcMT2HdKUrTKMziJg9EUvHpdnfgAk3v28RquLHB2jyY-aOHuW6lmaGniylLNZfh76uv01GdCSAErKBrMI1UdhXziHoOvdojMsi9mr9YvByDU-jytFyEx9A6viTno1D1WrLDSbDxkvoWcgyHc1oEZH4EO3B0n8e5d0eX4k7J65v71YE8L7aSgGQUwaOoleNcPkCLce0KDR1_dynlwRMvtwaLS3iYRDLxFSBMeSKMEUx7I4dJPQrV_25c7-Pf6cceruZxf6hQdyC_Zj92a90l0qG-tVzVuKztDkc4GmoxRGNIfw21T3gcBVeuzzMGLJgiLbQbjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buuAWyQJLhHqeGLvqsZqBZtLlz0QpilzmON1DzG8Ttp00alwVcpv8-IMATFA_wGxmZrzUUc6nEUR51bUl_Fgf7NOXXrJhF4H-Ks7c2WiEIo0Ef6-d7f6OSxm1nSbqEq5nOBl8ZjnnJiZIPZLQ4Mkn29nO1CzEKE8YvM6BujBsPIZFovmuMQ8u2fSeXmPxYXgktv5YN6GSZU_iw5rp6eWUn973gXTE8dyaWRX8b1cLmS9bCu2iYSq6ho_mRSrvGaOiL0O_HCkxzJ16-yDuP3nQ14PYM2hI9ZZG3Z0jxMY-ySH6tu8h-iDpNoP-p828SdCEbLYYmOmQD5bAW4LQ2POdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Yqa0YHlSyJmj-ufEsnTd1x4oRDfFA4J2x6BRYZjJSX_PZWTruiiceNd9OOunhn8clFhreplfniAi3W51Lw2ycosI4Xs1f_iexthJCv8bemdLzQUBz8rPOAjtiCSnRChc7_eVX_oszOZomGx6NBqFn3RLa6CirlFP92x1cffJtydl_0QxYLoaOuJPTNgzsLrGbsNQ4ClNz6iAuwLwmMd3mMdjj7EKNJrv0jO2vPB4l8tHK29tYy3T1_2TBNd0zlKKCXrmh4gE8uIIbTu-wlSrm5KFrFkiQrFI2tKsWzFw-xM3EckTb9LE9VLDjc8tjptTadhi_WBqqNuXlUHladItMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Yqa0YHlSyJmj-ufEsnTd1x4oRDfFA4J2x6BRYZjJSX_PZWTruiiceNd9OOunhn8clFhreplfniAi3W51Lw2ycosI4Xs1f_iexthJCv8bemdLzQUBz8rPOAjtiCSnRChc7_eVX_oszOZomGx6NBqFn3RLa6CirlFP92x1cffJtydl_0QxYLoaOuJPTNgzsLrGbsNQ4ClNz6iAuwLwmMd3mMdjj7EKNJrv0jO2vPB4l8tHK29tYy3T1_2TBNd0zlKKCXrmh4gE8uIIbTu-wlSrm5KFrFkiQrFI2tKsWzFw-xM3EckTb9LE9VLDjc8tjptTadhi_WBqqNuXlUHladItMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLhY-E7Az3XfoWtjxaKWzTMuZxfEoIMO2RGBShbvClRw6LDm6YWUsvw_wbQP_aue0YiRV9YsMPwzYdEOcrQx3J5rpHLYqwy8x39bIewibrwzP-rhXVCYNNB6ZKqQ6AYERzgTD0EPpV9BifzN7_SYrxCPLuIOPGjxIvxf5v9oe88klHZuR4NfyKoK0k0BeLnsgTk7umJazEQ4H2CjDAVnVlOUUu-ghb4U_uJQMjtMgdn8h8TvcmpZT_N2tuN-QpbmOlFCrXnhwC9eWDgs-FjpHzEWXB4XsaGf0hPQaTUERgn8TlY2ET2zV8Sp8hFhv0SeNh6ZrHXtwHgGKF24QGdgaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH2A9qBWfxXiBmM9g5-mZalRTT1AgqYWPTMfuMg55_LG8__wsGRIqjbDpUl9PGVfuOx_0qIgwX2q6PEZxD2LB7Dztmcx1oI-XXWwgGIuYG5rQXZhdLWxa7YX5-JFf3LyP5itcw-HXEPtaTNtuCH-QzQxn1Q3mMl5u4sbAnUWNNx6rW-_8_3goZp-sVf0b67R9H-8tnlTNrI7HN7gDiGL3hAjW6N1tNpmmBMi9QPAnnU7UJ4w4nWYEAEFFV835mhGKkNqzf6g04Yp0cy6IK0h-NYvVlNotFdZFDdyKYOWl0Piad4SZN7lEZF9KFx-24HPFyZSX34j8_QkdJue-hyaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=ryge5MYkIMB0JAkDbLjp7z1bul36MbGZnPGEkpocbibbOlDLPnUtBaHqZMMASLaXPNDasW0ctAC_PPPLoETPWqe3VznNP4xUSHJASCPoFyZVFSjAqf9wACvLWSmUgcb_rHs0QQefsCFyqbzzL3qg4rWoOjEQnTcvIzDLJWx6eR0kxof9s9lhMWegYxItetWXz0KpI7XgoaU_uXCstLU2s5DIln8JPADp-hon4Qi0O9yYA1Y9diP4hJ65BdEkavq-IRdQ4O6O40GiFYfhZow5NIyfwxJcLKl62vLpT6LiahS95rILGubLc8-WHXFZ-c-oOZRlwaeOhF0_e3RPlRIGSJlBPL0GzPzxg0ZIEduTgo5tDCsGJaBtqw7N7wmDfRSeAMxJRvVXoKqkBDK1LSOe3sx_iHQwmMMSwo43P1T2U82sdsVm_89SSk20M7sIUIkNC7o-RamSYzJzr2sMSOkqEe7niaJYmIs1E0jiv92P7ZKsFFji6U3jM0o2rMdENF2Ssguo6b2GtXe7-o8K4CULlNvrar0TDVupmRKMa_jlmIrcsuo3zYsqu5sDgWdW3MoaHS5KebZ8fJopRudsjFT_F0OnysdNMdBZm55i4M2j6CFTmkRAxuQvUoIw4yhTVjffHs5ikGGjIVYtjsx4-YtxQoKxvnWJcMwWs7cqtO5jIx4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=ryge5MYkIMB0JAkDbLjp7z1bul36MbGZnPGEkpocbibbOlDLPnUtBaHqZMMASLaXPNDasW0ctAC_PPPLoETPWqe3VznNP4xUSHJASCPoFyZVFSjAqf9wACvLWSmUgcb_rHs0QQefsCFyqbzzL3qg4rWoOjEQnTcvIzDLJWx6eR0kxof9s9lhMWegYxItetWXz0KpI7XgoaU_uXCstLU2s5DIln8JPADp-hon4Qi0O9yYA1Y9diP4hJ65BdEkavq-IRdQ4O6O40GiFYfhZow5NIyfwxJcLKl62vLpT6LiahS95rILGubLc8-WHXFZ-c-oOZRlwaeOhF0_e3RPlRIGSJlBPL0GzPzxg0ZIEduTgo5tDCsGJaBtqw7N7wmDfRSeAMxJRvVXoKqkBDK1LSOe3sx_iHQwmMMSwo43P1T2U82sdsVm_89SSk20M7sIUIkNC7o-RamSYzJzr2sMSOkqEe7niaJYmIs1E0jiv92P7ZKsFFji6U3jM0o2rMdENF2Ssguo6b2GtXe7-o8K4CULlNvrar0TDVupmRKMa_jlmIrcsuo3zYsqu5sDgWdW3MoaHS5KebZ8fJopRudsjFT_F0OnysdNMdBZm55i4M2j6CFTmkRAxuQvUoIw4yhTVjffHs5ikGGjIVYtjsx4-YtxQoKxvnWJcMwWs7cqtO5jIx4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=Rwb1P69kH_5El_8YPlrifK6jOh5hBQbc34nNigTLxAIdFXzyusl43E-x_myxMNbYK8NjnjqZIDnBO86v5_XqJBLBggJzsYh6tzHT3smO23kyKwnttZXz-XNZxc-vFDiqNFWVgWGYrplEj6SvjkcrxtdRy5Z9eblA9X-jI8J_UZXi0036ojiOFwLfqxrFxKGrLadje4tvDxQBZvk-QsbRFL-C5Y0MYdFNR-MmrkNlZbGEtm2doq57aKwwbE0bmXbKvo8JBWptCtR5RlseJDMkeNBiQV5V4NDfJI1b-uEqiGCvL4Tgzka2ByyBdrKtr8VlQCLKOoEO_EUszhO9ALo9bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=Rwb1P69kH_5El_8YPlrifK6jOh5hBQbc34nNigTLxAIdFXzyusl43E-x_myxMNbYK8NjnjqZIDnBO86v5_XqJBLBggJzsYh6tzHT3smO23kyKwnttZXz-XNZxc-vFDiqNFWVgWGYrplEj6SvjkcrxtdRy5Z9eblA9X-jI8J_UZXi0036ojiOFwLfqxrFxKGrLadje4tvDxQBZvk-QsbRFL-C5Y0MYdFNR-MmrkNlZbGEtm2doq57aKwwbE0bmXbKvo8JBWptCtR5RlseJDMkeNBiQV5V4NDfJI1b-uEqiGCvL4Tgzka2ByyBdrKtr8VlQCLKOoEO_EUszhO9ALo9bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIrhK7v9v8B_aANbGKgTRbKO_Y2SUGf39vaKUhuhWYsljLmwE1vwk2s3gYbNYWrDGM7BNoMm_EiP7wSDkPGNoAV5KUQQrCl81KcZf2zeHanVXlK-eQSRvgZgBPwLV7zgmxSUrnGeTWpkRDGMFBMLADsDwy-lqNmJPO6CXD-y-KuyBsl_9qt9CfRCGVl2SRb4gOw6j0y567rUDpP6qhi5yhMijl450XXIx20o5BfV7jjINFkGN4hHiE3n25cEKhlTWgQNQOpLIbPhWcag_pINSKaGKyYjjSVIbOuE5l7ifufP7OQo3NAnvuoTbp1NLViq1-T74kRzS31EIVgCYKyOd4YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIrhK7v9v8B_aANbGKgTRbKO_Y2SUGf39vaKUhuhWYsljLmwE1vwk2s3gYbNYWrDGM7BNoMm_EiP7wSDkPGNoAV5KUQQrCl81KcZf2zeHanVXlK-eQSRvgZgBPwLV7zgmxSUrnGeTWpkRDGMFBMLADsDwy-lqNmJPO6CXD-y-KuyBsl_9qt9CfRCGVl2SRb4gOw6j0y567rUDpP6qhi5yhMijl450XXIx20o5BfV7jjINFkGN4hHiE3n25cEKhlTWgQNQOpLIbPhWcag_pINSKaGKyYjjSVIbOuE5l7ifufP7OQo3NAnvuoTbp1NLViq1-T74kRzS31EIVgCYKyOd4YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GH6OjCyUO_D_ly4qgSmsrqZ3HjbE2usNbA0MyKdB4UD6mNdhV6zd-Byo3P8356S44amPr77Y1D7xAv6zWn4jomzvz1KT-dUlCH8pOjPAPlofzVY8yaY7J6G-aLXK3vnoPOc_zfWFk2k3bx-569QY5afPNn98u06fSuW4GeBU2JLnS0H8gfBnLEGaIKPuMybZH9FQ0XrRet7fuOF_8bwBkOBVZsHAhJcgRXo7lBQGOuvmv1CDDRldgy3K9TT73KUzBh9msQ-ZJrBkijWkDVoY52n-8I8yDjn7ddODkqqhsUICN8gRHhEehBlakr1B6EAF5oFX4VNbJnOwL0rpdRpl-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKhSujq_6TyCWU-Z2f3Fmmj1j0xXVmms5QvKoY1El2X2zP_k-4zjK0EZfKFC0REDPCgcr1M290NOjwAXFHsXNbQFhrPfwktYYfT84FuF8ECFvP-UHrjmghjIdw9qNDxGpT2M6DnyBP0eKWV_LFoiMX1e3SQsAnaTV5Dbor8wGA8mLDoAcFomcoYjZsrlGVYnkItKF3bp_PjX51cqI48p-dSYe61pj8rT87sRJMd8-EQUysG-hQ4oG960UhcB_ZHVKS23HKQYS0cOZ9QMfHSiOIYkPhyfdyTaSmp7gCFqBqpkCcTMAjIgnXeCGe-rVxyKfwqEd3B32R3d3vK73yxsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUTSUzNMHb5hDPEqSeoX28eCZb6CHy6HoKUi_OuOpfoo1s3wHZUI9nhyekJ4hbLHVyFWlXUWCweiyT7pZuf-VEKGuYOonuPqJvrffn1XV3Z2U9JrtTuu5wiRitjInA4UZyYhZ9soCdEq2-DV342i-_O1ybYR6i7hXQi5Z9Gj09VbfSAJdi__ypgzzgodAb5ltm65VjjxkE2kBjjsmgaBVFvuviO3mdMHBdsETkOkZzSuD4M24dejif09z_gG0Ejen8pAlW_lWnyqCmH_0huvJporzL-PwgNzjzA7WtuFj91ns8vwrwr1nw0Zrkfbkel2XdvB4s85VD1AHGGX0nchsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=IGMKGhALuXkpKPYZ3pY0KY_JUbqNsNuqI5-VdbMwT3heZIXma60NrCidhkrMGogeSBkjArqLJZTMYuOK5rXRXcKeyBFeGKd0MwHZQOA_w4v1i4n33R1Vo6-qmik8lXzq1sHgwAu4x0SbuUS2fRUV3p8yBbebL5xYmkfGsFwEB4fpAfBGvlHYLV5A1AC_CQAVVFkpSUtim4soCoFpv0PWsU72F3qA_Obal05lbZZzcSbuBW1GU-Q-Wx8M6hp8AZM8-WTrv6peL70mEwlRmOOOEbce2H8rGzWrhbnMD09jcRIZQh0Rc555HA0nw_ZRUnTDgeEdmcVTde4OF-jPm13Tww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=IGMKGhALuXkpKPYZ3pY0KY_JUbqNsNuqI5-VdbMwT3heZIXma60NrCidhkrMGogeSBkjArqLJZTMYuOK5rXRXcKeyBFeGKd0MwHZQOA_w4v1i4n33R1Vo6-qmik8lXzq1sHgwAu4x0SbuUS2fRUV3p8yBbebL5xYmkfGsFwEB4fpAfBGvlHYLV5A1AC_CQAVVFkpSUtim4soCoFpv0PWsU72F3qA_Obal05lbZZzcSbuBW1GU-Q-Wx8M6hp8AZM8-WTrv6peL70mEwlRmOOOEbce2H8rGzWrhbnMD09jcRIZQh0Rc555HA0nw_ZRUnTDgeEdmcVTde4OF-jPm13Tww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETezR5BmOp9eNAM8ITEn3TwYMym1NmFYXM9jnds_mB9DxdAV94EJ_y3wJPcoXSegtxRAUXIVQzorEg_zbXXaeq6VDVVuWJf_y2jI099bFSLJxhT5gq0eHlyPUL1ubPkDBte1C-MDE3FYi4E11oJsR8tbQFWoxkc8KOXxWzhJ5GuMDHTAEcpWvVZy36iNKT4J8joG_4F-hetf-9tlZN2tn6-ffxGpodzKKvNoxxmEPumar7Mg8nGBvb-T8YD5C19WGMBr00bnWQTC572Jed94_Ag0verJ1b_I99LkgqFHu9RpoEW-00tpJnIxGm_iosKNBcpJnLiUHdT_7dKgYwnEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRrKuvskTD0ZR0YX2Q9Drv7UwrFeELzlKLMhaYvutNnvwQYIQ4E4YX-i6kmjkk2FNlXV-VVaynf7Pm5AePhjg3nocupStGlMidIvUfk-KWT9uch33DwT-UJTcpcSKhrmlOXhYSZvM8sGWULqevK9YINGeZMY2ero-3G5kiCNfYxWiRZyLQBj90foob_2F7BCyKPX3O7q0rp5bwOMdlbpGcpm-RrL173QDWDk0XIrDwqc7wjTCH3M6P2TYVg1z4urIbmwvcZEanofkmhbSf-66MTzlodJ-Q0jD-9Aha3q4l4ktCaAMBlzBe2oVhJGyeudhK7JbgoBle2mE1p2I27Khw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFRtUu2naLu5jo6etxS1pRbK4xSZKzam-PRh5foP2B7lmb5AN4hF6PH_wGWJx9McgTp_cTqHVks1QHtxiWeN2VaqoGxCOPFkda1ir20cJtxFs7qgxuXzE1ljGNj8ADcGZdB9fw1g91uOkQMgiI1wN7P50xtRxDL2eITjzxoD1hGptVrE5JhBue0VOUFhRjaTrLnqCgv8sYEzyFJ0WyIyE2FCRWQ72VCuZ-1aJDXDkBIkEF8jbXJ8h7REBPHkR9OawQbDDQnYgC157VQ7trObyWIGp9EjL-DZDIvm38NxJoAiHJQ87QQUrQ07nwwPG-HBXHKyi2k0pqvrpiVbXxl5dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdR21Psh_kdxwIX3q5tOtbEiRRYIJF7gOfa9ugjPLARDQNUd-OAiunzJo1x3FhTIAosuyjlyn5AeSORZsAWZmahPIm0F4yU460Bfxk6M_ge8UW5dI8_GUJJt5N0J9-YCab1R33GJ9cVVh2-rcxykd6JD5JAXWJHwlcaaU64BDSEKYyeEWQphAHeCn-iOXDy-swaRHSNv_DeZ56AE5VRYI3DbwzPvbY6fsqeCoEgSSF6g-b-qrMOqss4p26x1x_rOVdgmBBwSPndocOt8qReREpVsVVp_pypYn6awHka1Ze-VAeHiAh9nGISyx3fS_2ZXzpi15g-anr6MOBnwhwQEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=BCh3aUrJn5D8U2M0PKY-6ZNgqm1IWcd9XP8LyK6YDVmNNqUAWbu0LXhvFf0D3rmSBCxv5Va7i5_xOcRXF1U7eri94nfaE_bGKMTr196LCxT-BxVXyuFo7-AcIiw8fV8PNIQIyMeGmGaXfMX67MKHNA3L9LdDLbCPwinf6P5w05ntC37VACbZBdRB-tXoYNEhWmJFWVki4qsFI2Bwo28xOw81NPmtwZC_5rlJQ3OHOx1mIuVwkgDSQxPhuenpRq_FY1yNUhqCIvXG0eC6oOIdUzINanXyAZtpzQBsPM0QOPX9ja8glQK_8lm4uJHWyUmZ2C7ci5ojErlYo10qlTzjN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=BCh3aUrJn5D8U2M0PKY-6ZNgqm1IWcd9XP8LyK6YDVmNNqUAWbu0LXhvFf0D3rmSBCxv5Va7i5_xOcRXF1U7eri94nfaE_bGKMTr196LCxT-BxVXyuFo7-AcIiw8fV8PNIQIyMeGmGaXfMX67MKHNA3L9LdDLbCPwinf6P5w05ntC37VACbZBdRB-tXoYNEhWmJFWVki4qsFI2Bwo28xOw81NPmtwZC_5rlJQ3OHOx1mIuVwkgDSQxPhuenpRq_FY1yNUhqCIvXG0eC6oOIdUzINanXyAZtpzQBsPM0QOPX9ja8glQK_8lm4uJHWyUmZ2C7ci5ojErlYo10qlTzjN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=XXoVLzWL52v5l-gdMTPalhPZZq0uHMXXmxCPmX0Gxjg9gMUrKq6OPHOMIAp3dy11EsDPfxf5ffaFo0M8d8VLHSlki1-EyVXNV3ZVmTNhFAOyAP-VkpndoofXwCMXaq0_gYWsm-9aapuBvxX1Yu9OQmLeGrDhmq2s-ru9HViv3bxqxGJe9aXPEPC4wy29d_TH7uP79DbfScRs7ERBMykRNip2q81T4TyGaaWxFTeM2LAN4hc639ODe4L2EXQxbNzseh3zZ2rgncn_ylI53qVomY_td8bh00RgE2kxZDYy6s-VmZhUZ_JndbuBiUVmIPdrmb7YUfJ1gBkkv9hZNZrLHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=XXoVLzWL52v5l-gdMTPalhPZZq0uHMXXmxCPmX0Gxjg9gMUrKq6OPHOMIAp3dy11EsDPfxf5ffaFo0M8d8VLHSlki1-EyVXNV3ZVmTNhFAOyAP-VkpndoofXwCMXaq0_gYWsm-9aapuBvxX1Yu9OQmLeGrDhmq2s-ru9HViv3bxqxGJe9aXPEPC4wy29d_TH7uP79DbfScRs7ERBMykRNip2q81T4TyGaaWxFTeM2LAN4hc639ODe4L2EXQxbNzseh3zZ2rgncn_ylI53qVomY_td8bh00RgE2kxZDYy6s-VmZhUZ_JndbuBiUVmIPdrmb7YUfJ1gBkkv9hZNZrLHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=JypPhJtszNXYUqGkXF7UOtYCq8qxLVrPp7q31NjEWwDBOfxzM_YXKm7UrMc5uYzeLINqr6MfQ6XUrULmLQqx4Un2gJXT44i_P-8Xy_BU93DyB2tdg84dLCoM1i2-mLGTP64KvO2Yk99rqCB1xS6RunF16q8OjHSfczoJ7kVeC59uaopv-Uy857FDcHlATqSD8i-z7V8_gb-NRbMIyV-OpnjGS266RmBNOzQNAOKWupAI5Asl4SyF4czJxUHsLJtja60fx6Kf7YHTkdmlba8KbGpso1B-0dLzTMiu22n7keHvwYx0Rg1JIbYSN5xHzVQjHug7fh1Ila4OrUwKIKp9DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=JypPhJtszNXYUqGkXF7UOtYCq8qxLVrPp7q31NjEWwDBOfxzM_YXKm7UrMc5uYzeLINqr6MfQ6XUrULmLQqx4Un2gJXT44i_P-8Xy_BU93DyB2tdg84dLCoM1i2-mLGTP64KvO2Yk99rqCB1xS6RunF16q8OjHSfczoJ7kVeC59uaopv-Uy857FDcHlATqSD8i-z7V8_gb-NRbMIyV-OpnjGS266RmBNOzQNAOKWupAI5Asl4SyF4czJxUHsLJtja60fx6Kf7YHTkdmlba8KbGpso1B-0dLzTMiu22n7keHvwYx0Rg1JIbYSN5xHzVQjHug7fh1Ila4OrUwKIKp9DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPllGFP8sREjw7ad2d1burESg7kz52h10oTVTYTxgPaNbxkJq32-qb2WkgOEiwjxm2SU1YseN_-SI4DdoekLta5wxs4nHD1BN5KDgMf5iJNxKNtx3tKlZmXRQAAO9GWwNXlkK8jqISdqZEx9mn4pb7liIU5GX5Nm8R4e3OitDtoLNaKwa-vyViZtC8bnowxsluGN-0_CRf3T8ST3u66bw4Q_A5SCRTWVQPcQvZSNdePBU0f4_hsnYFLikf-T0BHrwvtUStmFVOZJHGbh-WRk1BphyDHsAaleZifBFgU-LKOKsDhwHuEs5sri4a8HrjYOCKfjn6Aukf-mA8kc0KdKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=PTKcvfCKor-M3_qP3lBlJvG61IWu5XiW0UENdznhb5YZ7rIRmvNomiLYjehHamwa9q19YwyKMXvVPo6nwQKgkwESxc6sGRGUnwnZKZdZeRh8IXqNYx8w3nX_yKW2TValDZ7TP3eF8B1l_wqHs65kz7vV6XfC1QywHcytI3htR8EpeHN9nqhQEXxhjehOZI3vriojCDxGG6MCZrFEcbiqJpx7Mw8raQy5ZyUg_TSGhUBHYZcDcXrfjwEOvKiP32v9BrTOn6lVly36dH84sucffYN2Oe0BDpE-P017QoI4Lb4KUAMkHoQEOxDNrKUpj9AQZyhT_Njr4Xj_OBUfS9MOdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=PTKcvfCKor-M3_qP3lBlJvG61IWu5XiW0UENdznhb5YZ7rIRmvNomiLYjehHamwa9q19YwyKMXvVPo6nwQKgkwESxc6sGRGUnwnZKZdZeRh8IXqNYx8w3nX_yKW2TValDZ7TP3eF8B1l_wqHs65kz7vV6XfC1QywHcytI3htR8EpeHN9nqhQEXxhjehOZI3vriojCDxGG6MCZrFEcbiqJpx7Mw8raQy5ZyUg_TSGhUBHYZcDcXrfjwEOvKiP32v9BrTOn6lVly36dH84sucffYN2Oe0BDpE-P017QoI4Lb4KUAMkHoQEOxDNrKUpj9AQZyhT_Njr4Xj_OBUfS9MOdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=UBjig-x-pSbxof40tt0g13oMNtWRnMz2YzYk5UuuB7ARsQZW7KHKAxHctod9X7yrtDvwBDq2Zxe2fhzE14Wq1muih08HYz3cDn6VILih4QZZkn_0d09dq9PFCMLqkSVapQ3bIpnHYlrM4zMn6ZC5CtDJ7SHw68ezrOX_3ZsztYZ7h3bepsSd5m3hftC3_ONpeB1mXORUEcPau-mA0dLh51SI7m7Uxf8CVSyOSsCImS5ewz9Ewvp-1Y65kBcGSQuBWClKxNsPAPMhtAdaQ0olqiwY9e5Dzx33MPdFGfnICl3OWtsLIwA307PbexkJsOeBgeFKx3tUy_Ct-lYTYnq2oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=UBjig-x-pSbxof40tt0g13oMNtWRnMz2YzYk5UuuB7ARsQZW7KHKAxHctod9X7yrtDvwBDq2Zxe2fhzE14Wq1muih08HYz3cDn6VILih4QZZkn_0d09dq9PFCMLqkSVapQ3bIpnHYlrM4zMn6ZC5CtDJ7SHw68ezrOX_3ZsztYZ7h3bepsSd5m3hftC3_ONpeB1mXORUEcPau-mA0dLh51SI7m7Uxf8CVSyOSsCImS5ewz9Ewvp-1Y65kBcGSQuBWClKxNsPAPMhtAdaQ0olqiwY9e5Dzx33MPdFGfnICl3OWtsLIwA307PbexkJsOeBgeFKx3tUy_Ct-lYTYnq2oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=MT2zwKsrOY-LpopiFWiiOJPNLSsLGNTXGWRYBDmWCkmlGeEIh0fCIZ6fqvm-c9cEAlPfL__1QhnytAIR16seXDdNbEvc-dhPh9ONc46MqVheDMABXm8VpQ2uJy9V-DkF2gNS-KX27lz08Sig6aemvHg3yqSdlYlwnGEOLiQdlR3UlNhHzR-URtTs27YM0XuGM4AHog7yC7Nm5y3aaO00R0vE8jWrKhGo92sKbejKV-QMiSVqNjhaDYwt9i-6kDxcIjx6mXr6vldbzPAftLmUWT7UpL5M6d5dyna9p7PlzKEUNqJ5I2Z512JfoUvSzWMdKQ5IwlDhrTrJUrZqHYozaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=MT2zwKsrOY-LpopiFWiiOJPNLSsLGNTXGWRYBDmWCkmlGeEIh0fCIZ6fqvm-c9cEAlPfL__1QhnytAIR16seXDdNbEvc-dhPh9ONc46MqVheDMABXm8VpQ2uJy9V-DkF2gNS-KX27lz08Sig6aemvHg3yqSdlYlwnGEOLiQdlR3UlNhHzR-URtTs27YM0XuGM4AHog7yC7Nm5y3aaO00R0vE8jWrKhGo92sKbejKV-QMiSVqNjhaDYwt9i-6kDxcIjx6mXr6vldbzPAftLmUWT7UpL5M6d5dyna9p7PlzKEUNqJ5I2Z512JfoUvSzWMdKQ5IwlDhrTrJUrZqHYozaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=SBYYcXL6ZCrf4hnxamhZl-kzW5Szs5GONzo3n4KSMUE28xF6xEnSwg_0N9UhGwWeUKaEAkPJcA_KW76YsQfHZqorb1NJogHykhhSn5zQaJPF-Wv1nKBFIjaRs24Po2yaWdPFE82E9M-UpLI8xbaRYw37QKdt_W_qOChRVjhD31euf-qv3VC16QhsqmmdkWuqcTjr0QIhwItedyool-xjbZ4asXOD1-vzX31t4dwWl6UOqhg_hbZZCrYmnj8nQFEA1FarTtwCKyAgGbS6gTV_xUbyQz9zZc-5hSjsKimUUYLUE49MTb7BI171kaB0OI1nbvsZODNrsO-Lj30h8dJKGI1gOLlqeljFA5mS-1xko1nNeiB4Vty2V5q80o4Y_-Uf7hF63p2MOovH-fcGzK6e3t7vFTGXh22C59V4j58lZimOEb1ynvndXl7BhTmouq0QK7wZBa05jo52BL7q6onOQHCx21RYKGcoCWB5hLyAkAc---QSRbUQOxR4C7_nL0oto6Ezx7hIZufKWfPHb23xTCDChYyH1yjzeItAmhruQeEdOqAX4-Ax-vVgLJFTa-Stpma3s0uVx88KfHOMkK4GnlIxmmMrkXGs8LkeNngiY1YrgY51Tc6XQMSWW4GWKC44i5PWlPQ8sc2xsCSIf3JRk35faFEUIDBPO4DSJLu-sng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=SBYYcXL6ZCrf4hnxamhZl-kzW5Szs5GONzo3n4KSMUE28xF6xEnSwg_0N9UhGwWeUKaEAkPJcA_KW76YsQfHZqorb1NJogHykhhSn5zQaJPF-Wv1nKBFIjaRs24Po2yaWdPFE82E9M-UpLI8xbaRYw37QKdt_W_qOChRVjhD31euf-qv3VC16QhsqmmdkWuqcTjr0QIhwItedyool-xjbZ4asXOD1-vzX31t4dwWl6UOqhg_hbZZCrYmnj8nQFEA1FarTtwCKyAgGbS6gTV_xUbyQz9zZc-5hSjsKimUUYLUE49MTb7BI171kaB0OI1nbvsZODNrsO-Lj30h8dJKGI1gOLlqeljFA5mS-1xko1nNeiB4Vty2V5q80o4Y_-Uf7hF63p2MOovH-fcGzK6e3t7vFTGXh22C59V4j58lZimOEb1ynvndXl7BhTmouq0QK7wZBa05jo52BL7q6onOQHCx21RYKGcoCWB5hLyAkAc---QSRbUQOxR4C7_nL0oto6Ezx7hIZufKWfPHb23xTCDChYyH1yjzeItAmhruQeEdOqAX4-Ax-vVgLJFTa-Stpma3s0uVx88KfHOMkK4GnlIxmmMrkXGs8LkeNngiY1YrgY51Tc6XQMSWW4GWKC44i5PWlPQ8sc2xsCSIf3JRk35faFEUIDBPO4DSJLu-sng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=eM_9Blv1rF4N2qDv7RhSuQlyArZuRrRBHvQjZu838JcDbE3czC4ofYPe6okM_ANpRArjxF0Z36yIicRy2yEnSgpp_nqSBeVD6X-sEMRnoXI1mmzMXD3ciPxYnePvdo6TgUI7K2M1gxvBkgRSoTAWqhKMJgp6NJawU9Eq8Wqy5UMoMs6XrAyJX3pAEMNF6GG5ZYPP1eo5smAv3MreETN4BHLHLLDWcKwYle9_4KIO7OyxiFqIBuM-5x9kC8DjQqWq_7-MHuMEk-9FYpGiGlPTmcMcCyzc6xMbnEd19WqqGwFu_XKECISYaCiqZJErm_6wvdkNB7XjanBeQlP5IZ4EbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=eM_9Blv1rF4N2qDv7RhSuQlyArZuRrRBHvQjZu838JcDbE3czC4ofYPe6okM_ANpRArjxF0Z36yIicRy2yEnSgpp_nqSBeVD6X-sEMRnoXI1mmzMXD3ciPxYnePvdo6TgUI7K2M1gxvBkgRSoTAWqhKMJgp6NJawU9Eq8Wqy5UMoMs6XrAyJX3pAEMNF6GG5ZYPP1eo5smAv3MreETN4BHLHLLDWcKwYle9_4KIO7OyxiFqIBuM-5x9kC8DjQqWq_7-MHuMEk-9FYpGiGlPTmcMcCyzc6xMbnEd19WqqGwFu_XKECISYaCiqZJErm_6wvdkNB7XjanBeQlP5IZ4EbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=fN8OYA01WExAjriA5PWJZFfrnYSeTZ-gthvqJURwtZ4peW_5DvKxVHZR-61dGSa6wQCShvE7vuHL72IUPtPPnj5_Uu5b4jJNLjD_cVxDOZ3z1qUrIA93PbqBFtIGvar2bS9qSNorcU9i1mr6hpOezKuBYq_THR9BoGLDWHiYaQveDc6EEOpUeCTat7-GjIp1d9uHfpAt6_JZKkmGvZ2qiXT0E71ZxD376iBENY5qRpRIVUZGe5M0SSbwKwxUlUSERWavF8Us1PaItkcUwghQRKKuAVLXV_uTn7z1fiVADHHfJqOenUZnl0_OB-OscK6sQlL01SNb-lNo5Kc9KFA_bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=fN8OYA01WExAjriA5PWJZFfrnYSeTZ-gthvqJURwtZ4peW_5DvKxVHZR-61dGSa6wQCShvE7vuHL72IUPtPPnj5_Uu5b4jJNLjD_cVxDOZ3z1qUrIA93PbqBFtIGvar2bS9qSNorcU9i1mr6hpOezKuBYq_THR9BoGLDWHiYaQveDc6EEOpUeCTat7-GjIp1d9uHfpAt6_JZKkmGvZ2qiXT0E71ZxD376iBENY5qRpRIVUZGe5M0SSbwKwxUlUSERWavF8Us1PaItkcUwghQRKKuAVLXV_uTn7z1fiVADHHfJqOenUZnl0_OB-OscK6sQlL01SNb-lNo5Kc9KFA_bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qrd452XsbATIMRbKTPYCNkLrdNeyMlyc4vSo7ei3hicHO2KqHFNTBrhMuR8ZhqOoffz2YH1Myuh8eOVjRxNIpEghVOYq4d4jANKYWM3gAPnZ6PF_Vj7owGQwB7zzn0h11HvM0DsY6nQB_LH0sIYKCDNcuMlQwGr_95-xYDHHBtGwuwiTryQ5qy4DYPDle-4BN2G8FP_gO5B9yEEv9dBkuetzUvopD6FkYkrTh18i0Ghhm8w_nkGCsBRX666aUb4zDtEPdFYKv6RB3m_k-l1mXtJYy5KPoIfmk8cgjrm_PAs286_AtB83XDniMygQKqzxxUfo0LnjnJTKiiTdKog5DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3UOSCtgnGc60YEM7siLHAb75sKuc4UFbUeD64M0NKdOBwKRklfYS2GFYBTXrx4UxTiHOVymCCg3-cDt5ctL0-ydujEEw8M3j680LGaOvGgAqnj5uFTmSGpE0vjynTkDsNzZuAAJKc1TDUwhEIqZjDmpJcooX5NXsVNRpTMZ1amNM9_3sc2rBnCZeL6qFyn7tX4A_SiCAebqCuza8QnWyE_cqrpUZOSamuKvO9P4rZflCn4whUDypTCxupZnQM4lQPmaqLug1hXs1FPqbEYASgdQTkycLVfF8yt-uNP3pMzhp2o0B4vfwZJWiO1B1dqX3dQHE8bjmVdeKRXW9Ala_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=qROwDZd6cbnmzrqz4b-9a9skw5bCPegFX31031KTR50cyVwk860njSTenLa38IXimqTxCA3-q6aZAsy3eMTth8CcYwYQE0i-S26owdRDxqL3vcr6IGKGXBnb0aDte55ZZmLf-cSsP1wYtGdHuyIj23_y1LmNTs81PHFUGlO-X5E4Yw4M6HXt0e19XnHZe1olfR-zaipSDrS8i8GfM1nzd6lGblV0EEMdvSfA0MGJzM5FeOpJaQ40jo3yLFmnpJnejQk9VEXpvIcfKJ9hGhaAiFCaylZDQuB2_iFKUo_TVuk5BqJ-9cJmvmb8glzNBsdK_zYeCsN5S1uv168eQ_bu4HEGmereOWgt8tNuVZXi8Zs3Rj6sbQ1cKTbYvvldxbl9nIxsgyHwUQNWXy_0nGTgKCAHZJ4jpUA5EIFxP_IiBRa0QbXdKfxb_53G7vQGR7Q4KfIhOTnMFq5-SSViuubsp5ZIBd78Gq9S5dkPruG4MwRwJ_YEbNYS92ka_12-gj8XX6Sdi0jAfLsfX6sov5QvWozqE7HA6QRLl_XTykUt4_CX1t007diwLv75VCzhJ6ymLMOPhEnYlvsIL_epSXujYGoFCOrplFDqYGy8SLTShfOtt2DU2vBhd2rvwFzFaSDQ8rJQIHXFAUfq8rh_02P4D288-ncNV5ZURU7lxsfAavU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=qROwDZd6cbnmzrqz4b-9a9skw5bCPegFX31031KTR50cyVwk860njSTenLa38IXimqTxCA3-q6aZAsy3eMTth8CcYwYQE0i-S26owdRDxqL3vcr6IGKGXBnb0aDte55ZZmLf-cSsP1wYtGdHuyIj23_y1LmNTs81PHFUGlO-X5E4Yw4M6HXt0e19XnHZe1olfR-zaipSDrS8i8GfM1nzd6lGblV0EEMdvSfA0MGJzM5FeOpJaQ40jo3yLFmnpJnejQk9VEXpvIcfKJ9hGhaAiFCaylZDQuB2_iFKUo_TVuk5BqJ-9cJmvmb8glzNBsdK_zYeCsN5S1uv168eQ_bu4HEGmereOWgt8tNuVZXi8Zs3Rj6sbQ1cKTbYvvldxbl9nIxsgyHwUQNWXy_0nGTgKCAHZJ4jpUA5EIFxP_IiBRa0QbXdKfxb_53G7vQGR7Q4KfIhOTnMFq5-SSViuubsp5ZIBd78Gq9S5dkPruG4MwRwJ_YEbNYS92ka_12-gj8XX6Sdi0jAfLsfX6sov5QvWozqE7HA6QRLl_XTykUt4_CX1t007diwLv75VCzhJ6ymLMOPhEnYlvsIL_epSXujYGoFCOrplFDqYGy8SLTShfOtt2DU2vBhd2rvwFzFaSDQ8rJQIHXFAUfq8rh_02P4D288-ncNV5ZURU7lxsfAavU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyxySHCOB6Hd2MGI_vcLLHe2D7sdP6_nJy3Pt_zD7eLfw0oDUjDqOx3-UG2S7tkuxr9JwFHE-2F8NbYnZfm5v308z6BuBpij0O0lqDVKDifnAnKXF7IxYYIq_-XJVCTzLLy-DA4sMS5rYgLp0cF022AvX5L8yHYO4zi8UI-VOmLl9XBD7mrIBYOKFOoV6CI1X10li1X4Emco0ucIuG_rtVHDc2d_BREHk2slDIwqQixmTjDE_6d8qquRf9ZHUDZH6Fa-KLGl9ZxzqNrIqTPJeDJo-Xb2GcCNcEFA0fz478yRIoPZiMXN0Vh0QFpzlMjhq6d_F4hZ6__zsIQdfgqLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WE65Dd2kLLy3RYv-Mx9hh7XA9eO4ZL-cWCPMgb1EUWKy-_CXP7labKxlCk1ksBgdF8U5Cw0DE5DoXji79S6u2WembHvlabLeSu_250cElxQWQQksdmt1FEHrwi7APRW4UmjdZEfRAsvZLYtqFNEJ2hxSU0kQqaHM42JlgSTm8Jzyg0Vle7_lgESgFkpxqi6kiixTyCHGFCz8J_y6_opEUmpGKuulol8gTTPXjuX-ppwQVAPbGJtLeDTXXj-loePUTbMdgsg0Wgv4PU6zQI403jG4S9iN-hlf46CfceuvEVPB-k2mCfZ-S6Hku5BZY1HWHcElD9ohHLrwQBYeJzuZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K95sAfl3NbOzfCCTrfWCxHRvLJA9dH9vGwazOh8-Bm2WKL6SbFWLv6K9ASi0XmzbxyKqNEt50gl6R624-WLu0X9FRcuMWiX_1PwHQXFpP1u0hIk7u-zLGb9LP_gaoAh9nIqzXdkmCSRsGjlLodQnMMX-HOKXcbqgv8TagtyLXyEW5NgRt4mk0y-2AGpUbuUokhTPFWjCzodP8UsoGmuz2LFGxpeOb2fgmwszmA-F_L7w6fdnL157SXD-P6xhIK-Wuw1Y74hgDCXIF80pWij5Ze7v45nedqDDz4vKf5y9fGyo7_JvJi7XSiU5MHyXLDGSMZi7_4GSHWOXZBGt-QNXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB9JBC04Z89z_ITmFr_Z01WgC-SEnvUlGf1S8zadRyM4UEsSp_Mzu8ksu5d__gF33AmALWNDC77en1p-OUKaAo0h5dcYnT1aP2liSu_hbdH1AtsYYZoQAQcRhUsxerSLT00I6Hks3YQPPoCfznHgqx5D_W5DnjGHZfmj43-V8A5LbVwQMmcpUbysxQpDy1hKg8q2Sbp7lKtZcEDc2cbz9uxH9d4pgrWtbxRTtpicyjTJP5rO1DyhGEFWZAWq_rn8e8qek7xiZ1sz9OjOEiWY99jNMzw1xtM92QKhLpY2s-JPyx74g9O_tYYzBRKoRmbz8ssnxPu-oUe_E3r51hlTGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=pcfhZmiPlrNCtoi2sWaWvpSsp2jCDUWQgHa9-7IdveFc_GhcLEYKkWPSzZ_ClrWW7r2zH3aSPXtNtrGVpNdoaXHhFTpuYtRfsj1ltwiN8eACYjtmiJCiFb751L5kjE1_mgLta4VhHz28lJf2uHf-gA87V57ZO2pFzrWcSFeWAthgZh5oYueE8ZuYNBgqpt4x64bbJtfzuEJZ_ktHRWzKUozDXzf5CXxleRAtCNQkBEseQt-qoOaCMwHx60J8RjEfC9BRv8WrqwDkB1bVgHijPwMZIA9z3eADWNhu42jkM_v7qPuvY5ekcPot8vX6QNJ3K7E3CS_MtXEMbNNDBUMUbofCiXGveWfjp_ky40RJ8NmXZSy7m7M45hwCxMBWJ_YtMDXrQMcPqHZ3RDKwaoqtmmfW15kHwtEwWdoH-tyc2HBVuKysTcPWLMemvOztBEXP0IGOTarbg6T3B-CSwL6gSmJclbPLxwcTHeTe4-oF8ptMlxGhOESJg_zQAEQmM-5m9MQH-7gFgOXh5iG5rzaP_mq_LjwuO6gN8gkr5BcBIQLWo5RjELYwdNbz0TH9AA4o86FhLvoE3lHL3h8DpWxqUWe5wyxTeiR6Wgi013moR0JXAI1KUVAC3-QPI3j3MPVkFVxU1ndm7nZJrxcQY-eHY33rVHufBxS13cFVSOR3OOs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=pcfhZmiPlrNCtoi2sWaWvpSsp2jCDUWQgHa9-7IdveFc_GhcLEYKkWPSzZ_ClrWW7r2zH3aSPXtNtrGVpNdoaXHhFTpuYtRfsj1ltwiN8eACYjtmiJCiFb751L5kjE1_mgLta4VhHz28lJf2uHf-gA87V57ZO2pFzrWcSFeWAthgZh5oYueE8ZuYNBgqpt4x64bbJtfzuEJZ_ktHRWzKUozDXzf5CXxleRAtCNQkBEseQt-qoOaCMwHx60J8RjEfC9BRv8WrqwDkB1bVgHijPwMZIA9z3eADWNhu42jkM_v7qPuvY5ekcPot8vX6QNJ3K7E3CS_MtXEMbNNDBUMUbofCiXGveWfjp_ky40RJ8NmXZSy7m7M45hwCxMBWJ_YtMDXrQMcPqHZ3RDKwaoqtmmfW15kHwtEwWdoH-tyc2HBVuKysTcPWLMemvOztBEXP0IGOTarbg6T3B-CSwL6gSmJclbPLxwcTHeTe4-oF8ptMlxGhOESJg_zQAEQmM-5m9MQH-7gFgOXh5iG5rzaP_mq_LjwuO6gN8gkr5BcBIQLWo5RjELYwdNbz0TH9AA4o86FhLvoE3lHL3h8DpWxqUWe5wyxTeiR6Wgi013moR0JXAI1KUVAC3-QPI3j3MPVkFVxU1ndm7nZJrxcQY-eHY33rVHufBxS13cFVSOR3OOs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=CguLTpifq3Kst56FYAEy8kAvAXxF0NON5OpzHbaDKwQZyL4q0iUyqGgovVomOyP-uPeL8du-ll662KF0kvBHZa81r6Pi9-UquIBjx0x3WLxggQQR3MPMMw4n_Fjr4gkYgn-SmrRbt8BFKDRvxaFWoLvarxRsfaguNL0oPD6thXX9l5-rmV4vrGKfBmhYrSMCE8nzVCLM-DMA3jphUu0HtcY73Bn4ASGKUTrVaRuKIg6mxVDO1HW-tw6gJj2CflBPvyMy0z0oo5ZaFT7J-9QshDEpSDKdALARHAQdanp_pK7Gwclz_YjEKLR7lfth-nE6Al5qWQ3y8HsV6QHktdTaTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=CguLTpifq3Kst56FYAEy8kAvAXxF0NON5OpzHbaDKwQZyL4q0iUyqGgovVomOyP-uPeL8du-ll662KF0kvBHZa81r6Pi9-UquIBjx0x3WLxggQQR3MPMMw4n_Fjr4gkYgn-SmrRbt8BFKDRvxaFWoLvarxRsfaguNL0oPD6thXX9l5-rmV4vrGKfBmhYrSMCE8nzVCLM-DMA3jphUu0HtcY73Bn4ASGKUTrVaRuKIg6mxVDO1HW-tw6gJj2CflBPvyMy0z0oo5ZaFT7J-9QshDEpSDKdALARHAQdanp_pK7Gwclz_YjEKLR7lfth-nE6Al5qWQ3y8HsV6QHktdTaTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
