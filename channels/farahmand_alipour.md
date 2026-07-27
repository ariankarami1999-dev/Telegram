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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 15:42:25</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkx454vvoBkL2QCkWSqTFWzq67WIq0x80NQ5OAMjJizy9zdo-o4J1-CKcsY0AZN0sf63sIk9pv6b6WyOlAijamLUwzjcwT_wgrUxZfZzqQxT5lRSwxiesY1Oqegq1DuWX5ILLqyc6KJl7dgut9HleURDl6AEmTgaPKTCQZ1NUPzxZ2zLMy1nHOaSRXaL_yezxMLD16op68m1hF8BERYJR_M_VlKM6yjCsvxVGPdmTkEp_YxOorbiHyA39fVroBmYzzH_dBIcM4lJ2xoyapfLiQEEILG6P8I3CsxD5X3dVsbHRkw3JuQNR_Y2yA07oNl-xTHzoqHvMVD5E0O1VhUXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A91kuYO3TzFrjuaNItoqYRpI5zEzGD4PwHzr04UI1lm9DiEwsKTeG_6kG02R2RCwwOmP0h168EzxOmeE7cwT2zvl4eZtSvxb2-o9zZd9dFsDE9ka0FPGI63mHUAqTNWcYYv-bkcMWr4VWrqXpkzcOdZubFXk0Zd5jWChMiDZo5_Ykg9w1Lp9bkIxYfPNRwVWlSmA40B-psnGM0OVXtI3YCRTm3DXsqwoGBFhGncgp3EyLDOe8dFiX2HEoQmD4YviNHFOWsGw5hYZe5ZAYQo6jAHfvbdBigLD5TCaYbAl9ovy-nBTbuPqVXNthWX0n7G5oSPfsKz8FgleIxWnhYbbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edDV9CjvDEqt0FpOCHD_yBMDypzmgXqWDY6dm2flpjbY66GvUL4sQSAyT3XYf8jk0beJZo-zX0dyZV818M6lxpZaAVMpjaK5cSjIzTimwOMvAl6FjMhBVPDCsROKEw4lITOYG6pfAxO-n5f4IP9JkXRt3yE_UrRjUqWMRc9EgERWhoKikDsN7ErGvFJqz2EQQvYoGHtiEYo7Ffpbe6NwDDk-8Cux1Fp9OkuJtYCF8iFDqdPRjgtwoc4CgP3fc_7_16dFtsZ-Wpv8SPuEntbB2OnohSG3WS67R6Xlz6QKF74CxWkraJ9hCNDHxQE4xM9BgfVQ9H1Mf5VfHnURQI69lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEgMOSHveFO1xJ4gaGdBP0WhAis7h53aEUtzooS6oZsV5BWmFapNHX5_q8raGiGFQgCNJ-t21nnuYkojlkvIDFL6fbCtNWF_oWtlr5BPhsrEamfepi-_ROQHb-BF0QdOAZKhyWnFUaLVnFIQVL54n1MFatBqWE7VosQ7LbnX7VORu9NAfcvu41FJ0YpuFsCoWRYo72zV4QkE5qgrPA57lUV_D8RmwNMmlfBocJMYeeCunRHitTslXVOLltk_7xu8jkVUepKElX3CuCnHev6ZKqdC6Hcm71Hq1jOaCqr1kSYtb52zbkcqXabLKsRR5NwJcrRgXSfxuZEYAJ1da8Hhqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVHNyHPeagSnxkwEfmIrKKeiocZOMLHac-Ampa5iYk4oKWnbnUQ5mmDpj43K9ZZi4ScMe-SFPpbMZp1b374940tv8hyRarAZClhCYlCNkGyTcpRQds0j95atYiMfifXFOZGGgkLPwwPfCRVRR0k1WTNcrkBJMJgZ6qvZk6wpv8qiVbtOlxQqaTASMiclI7q0gZK8jMWIL2hhoGbNqhuD_Jfle6Y9VBm_9GALlygBHfOXYwj9mjO04vM28hgbpjJbAiRy3v1y4AFppInFPv60GbmuRu8QnFNqagehXpjfvLfF9y6oQ41jn-rk4p8tS8jLs4_knXKQ7Fkm41mt_U8Nxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vU03JBBIUrINr83zJT82G-VOKqE8hOi6VDow9Vk_JrqmtdlDqAZ4VWG2z6kPYKYWnTvcu1ghQYhN8YxdE3WNEs-puYUx85kYY4Gj7TJ1HIHBl-Z1qC3StQRjFiHbT7CppiHHAE4v1oZPOpZUMXOfdcUN1h9ilzqqgRBd5aJhbmIOAabbejFL_KnA94YSUmqaZULOPgbThc7gMMVMBuJCRXVs-BoDbGEmpCSNmoXpnK2UBLLuvWLwEo0C_AmejZoVeeOOmnT1FrgCm600e-Zya7Q1SPA1SiH57ooZqksGRi7Mt7Z4_If_Z6p7vDT3ipcJFoN3pXnyeMra1mG0EJK7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIXQbGNLxLnVKuqgG_olUbtDfWKIe4i1CMFN-9REoQ74SecXHNiPbykmXKjV-rE8gP_1bR7R9csPePaZCN7D4kvI-1sy4JdM-GFXDZ4z_uwuJwlzWkmSShHHLlUUtIcPfmSu-lGjFsn8tEZ2-zPNDXd1kWSJ-ga7le62RlNBiLGhOO-z7en9cNVYawWc5ENGd5NEQLhDZfDurZsGJvYFWSIEQlYOszZug7ZgBVVJKDRttjNdIeDOB2xhtCZ2QMBp3Af9xfxsbFzscbLiFsqu54CiBEDdiJiERwiw9HICKUXxEoUx3_73j6DyyvCUEg-IMr24L4m8W_v_E9DNowgsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TSMhPzbQwUS0KYuCD-gNrTThnyyXV0x08TwIPrH_oxqUkG5Uy-8FtjEvMzABjb3Fjmaooc0-y-n44f0zxRxhnLne3M18XF4Z6c-ChqVXUSkT31o2-nK_1gJWz7_axDGs6GfYlTHMT0NCJzb02hllvFc77FeyYm5aINrYFW0ztZ1UxLPp8HcaE1b3ugvymt5GJCgWmyrfGFHpKaAXJHppvzihvTbMRr4wGX-jyjjMVQV5EQa2nYbdxSN131-sVutPgv18tH7vxrMN2QJ33d7i0kirNIatpcUjruVPEu1E4MYlBIR8ex5hxak8OjBBcsw-55LqZC4bzh5d_HJn7mnaCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VojIowQcX8guJd7i2frkhBWqipoTnZxKsH5IJGgMb2VCvQS7nSnqSigmnOOrup2AE_jvI-vMpELv2b3n8HjOoobQzeCHuw02S64d8riO2cU5a7Q8s_WCQW8Lm9zMXgSjnFHbHky7S5uSlobmstyckWAqGxUXF2jYD4M8hI9h5hjuwf6E83ZBf6IPU_Xx4yd5DRa-aT1mumzm_eM8QsNwtr51Wn6FnIXBgFBr71YwYY9hchjePRhOgq-M7gZKqCYpkk6jqcIJxZJbT42f3VUeFYna1gVqBdIbNnzcghk_mX6jnnq1XKzojia2vtBVCCszNJhC0BW3eTQ6PCVpRRUKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=r9aJM86pgksz6t2oi3Z17ituWdKvzHEji8qSDt3RoD6pVv2EEL1Qu7C9hZ8QbkqV6KCW5rJQ2gXSbOPMWKpXZAouUr-dW-PwjdmS0Ybd57nyX-c7EBVu3VnYQD96araKVWLZSDgQvWqN7HmEd7vx7pdcdDbxP4_bPiJGO7R4psvMnMM5poDbrvMNfTIDSG55FAphPyzK_V27R1bVDqXjZA9bBto_rdah_RVj7Q2d9CgHkj6EuHIqz1nHxZtA6qpv0IJfWmJWEQIaWm0KNKjIMXeeg33aO9_0hRrlwUur1z3wUfbGhSmZ8EaedbFkXq3di1tfvqnOTnXqecsbkEJ0vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=r9aJM86pgksz6t2oi3Z17ituWdKvzHEji8qSDt3RoD6pVv2EEL1Qu7C9hZ8QbkqV6KCW5rJQ2gXSbOPMWKpXZAouUr-dW-PwjdmS0Ybd57nyX-c7EBVu3VnYQD96araKVWLZSDgQvWqN7HmEd7vx7pdcdDbxP4_bPiJGO7R4psvMnMM5poDbrvMNfTIDSG55FAphPyzK_V27R1bVDqXjZA9bBto_rdah_RVj7Q2d9CgHkj6EuHIqz1nHxZtA6qpv0IJfWmJWEQIaWm0KNKjIMXeeg33aO9_0hRrlwUur1z3wUfbGhSmZ8EaedbFkXq3di1tfvqnOTnXqecsbkEJ0vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOlVqhes1RmyP1YHjxG_M2KShMiMd6HBQLz_6R3KwLLB_V01xV72V3MyM9R1LKT0G8UHmVFgJ16TAgg3il3uo7Do7SAm1QtaE7kNzPMpcjW86jMMczn9PCA92O3kvlkXmsY2WUSPjRL5qcmS2zoU7QEaf6x_77tBNTTAP5UJ-Jrrkuml5KU6U7fvrAHJCkp-0ZQGuNG3EYtrAykuWy7bBTO-pP5YPcNAg_TYJg-aR42mWmH249dmHQFpjwFbmwyRtHYTND00GV-atsw_iSpTA6nxOBNvI44oCoPj6IZ80ZBoQQCNx1a363niyKMqyQRZ1pr9RXkzkMAOV9x3Tl324w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjPmisvZ8F5KJA8QaOyh2I1rgyI0CmVfBX822ZMT1OnE13sxtIaZ4aUX4x0tuBETnTabGrEwLBCWBF-S6LgfBNaRAxISjPKqfWtIIcNDoL_7__DB3K5_3-6Nx-dlmIrXq8H90d7z3Ho_veTqC2Hw2Q95yF5_iD54rNNevS0jCLMjJwLCotiEtZBl_n34hZrjzQNk12Iw7btdQI9v8n9rczz4JVCVPwwNbuISV6NsqcrR1wPKHnL95p_gDFtLoaD7BAXLT6C_q3T2NNAgLq-4BBBUHA5U58ZRM2-WDXS-NBIgx364UerDeQq4OkWecZxUeYjJxkDqpCyOFqY0E8EjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFhH4-y12EbCs4h4B-qEIT1gSqekL9ZNgOtBExzoMHANHAjnOj-86IGQvr11xaCI38TquNxuBwMMYorkvSnCyPsaOBXwemqD7JOyuUmwZHkT3_bm61-EmHqmpll5uJmQay8_gLFc3rSQYZZFMwJzMwDCQBTNzVlvG6G900ZYP6pTAjQVhEVZcDobpC2nZ6R_lCzWnq-h7owidw2J69Pf3RERFl2EGLbdqUUuMWVIzMwzJ8mYQwvAaoZGqytCv1vwAqFwq1hiPGC1ZyV1Cmed2YglYBBO1_5mq9n3yoi3SNoCuWmk3ifsFZNQQ3hy_8rMR882P3MCCu84XVRA0rW3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=BtazV50UrEitadDWSFI7-p1lO6wLlpbYlDWMG4o6j-_F4hXHUJYO_yiWSBj8MngLqiGLrqLpKBtzt6i1tXJA-AQwiHQacIIxb-SYWZ0sF0_fdz7Zsh8dB4-9TPY1drzGA_kUPoUcpCNfqSsFTscCZpMtXWdcpCSIvga-u1JV-MxF6d1ScpcZxkd358kOuGo7u0yTP_fflqPls7HN4FThiooIGu78XzMFyLHEi16EBU5nyXc8zSCm8lqyQQAsYMdbxEWl98Sazws2uLls1G6mLFF8cXoBww04vrqoVRpSMuXmL9TsWBhu9JXhEwKiUHlng5EVUdzdKfe9sUYe2thu-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=BtazV50UrEitadDWSFI7-p1lO6wLlpbYlDWMG4o6j-_F4hXHUJYO_yiWSBj8MngLqiGLrqLpKBtzt6i1tXJA-AQwiHQacIIxb-SYWZ0sF0_fdz7Zsh8dB4-9TPY1drzGA_kUPoUcpCNfqSsFTscCZpMtXWdcpCSIvga-u1JV-MxF6d1ScpcZxkd358kOuGo7u0yTP_fflqPls7HN4FThiooIGu78XzMFyLHEi16EBU5nyXc8zSCm8lqyQQAsYMdbxEWl98Sazws2uLls1G6mLFF8cXoBww04vrqoVRpSMuXmL9TsWBhu9JXhEwKiUHlng5EVUdzdKfe9sUYe2thu-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_ORfInSW73bI_FdZuBAegWu3O6VQscY5lKYZn8Nw7rgh5vh43T_QeRBkp4wEDOuyDdaz_yjUFGDOByhkMi_Eba74neZ9ElRb35rRb21-oQVAOGysMiqy-aaERuaqPUJNe1ujvvnz-RUPxzbspDCzgd3KuP1Jf4e0ZVItmSNvHSxfa5Toipic0m1k-wahkdmv_LVqdCR0zGRmKt_qGj-7f88J5J6IOwRVv-Yau8_8dj_zfiAugIBvLoDPbk504X-NB3e45mCjEtnVU0tRmtNXd8dmySEWyczkb6wgreMTANE2rtZc2hHdnOqol7bjEXNW5e61L4HLg3d_7JqQ6X8ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=vtsyZrxDaDfZXcIlIn1LA070KBMlI-eDXL0cJu51vJjNTHlZVh_WFmBg-q00bjtv1VvLQvag9HRhOs4odRBato2HubXXvUhM0mVPqXH-eDqPrAcdoOiacAZU6Z13hRUFOI26Km5jF7xqGYhWRUN4_KdCDvAUZPkSCgtAfSQMIg-kUsgKXBqVHaz9b9cC2KocMg8udkp2w1HrdwaCrkTfD7SZULs8a6q6sAdcxAB_y7JXZxprv58j0RTxlZl34ucjBPu8dvYGsmEYEeut3QQ2Ppb039W9I0yw6cq1rw8R5IZH1MiXBYRBHAqImK-UnLKse6kZHYdJEEAoh0a2kbqn6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=vtsyZrxDaDfZXcIlIn1LA070KBMlI-eDXL0cJu51vJjNTHlZVh_WFmBg-q00bjtv1VvLQvag9HRhOs4odRBato2HubXXvUhM0mVPqXH-eDqPrAcdoOiacAZU6Z13hRUFOI26Km5jF7xqGYhWRUN4_KdCDvAUZPkSCgtAfSQMIg-kUsgKXBqVHaz9b9cC2KocMg8udkp2w1HrdwaCrkTfD7SZULs8a6q6sAdcxAB_y7JXZxprv58j0RTxlZl34ucjBPu8dvYGsmEYEeut3QQ2Ppb039W9I0yw6cq1rw8R5IZH1MiXBYRBHAqImK-UnLKse6kZHYdJEEAoh0a2kbqn6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7OoyWd2p5PxX7EwwTlwKv_Hz4E3M4_iwz00bhJMs3X3B7ENwb1SrIuQEhRQuFH5Jp72-HonA0jrTokCFVIgGV6_LYfb6o-k4xvUqsYyu-XPs1XiP8be9yLP86bj_H3OghDjO3SzqiIed9mY6xza7VLmQAMh91hmacwwRzAMd0GME4knJSbsxdQXyb8WDSdfGDU2oOaV_9XwoY21Mdf3Qre9ITFiZRI54AslvvlTw2yav31UIfPOm2D_XLNirTScsEIq71Xo4Koxt_Fa1rO-HNyFCfUXbzv_ex6wF38Pq384nbHJc6NkSDMwfmdTlUDivI54YVp1itS_nzVzYUR5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mj6utzsJSSdmoGc50ZhnOkxc4WerU9jg6Y0FZck_VAGAuzihrHdwyHTxjYhZTtzzutx1VzfOPwGZoXlIqKWhr1-JaOX3VMVLKfLU6f_w8o0Nef8SsjR_7ar6Q1EBc6U5F8vgSr6rHpwhq_jr2NnCC4MuoekERdF3YMTPRC0w5QxTOxKJuveLZZnAMRkugtTykpq0QT9k_WPxQZXfuGbn-VY50wwLCwbIxSAmQf4OGXXijudXM8GGrE448Ab7lTz1hKywaWgz1vzvupZg4a0heDCSpEPSKTzNE5XxPeFbnlseBKS_7RUZTvLpgZmW6-Cgpp2S2kOnFPLC3nn3WedhOg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=CcQQoodlOiraYmAia3wtHQ0dBeNJgA3zIJv_pbwkZ_ZzqhFGrCdselOKMaOURgVYxzShxI3JAjMFUJLEhG_-DdH-IeOOW_oq1WGXbPOiB5jBIWukmXnGA1gnquryNKCPjLaz7s6XbnVLkjjMaEjp0-S61NL66ZMbDAZ3-3WG7RNRhoXX2xERHQWvw58dcCBKB_WifSDxQWDAbgOjtVtYGViXZIIpjZmdfCkqoHy97PpN8GMCXV06UHrSFu4YWUh6o8C3fKb1BXM63C9kyV1scaFyM6zZRv1KmmVHNMrGcVpefVK1ae6tymnPZ_vh-xdNGYrmPLik8ZNgUjoqBTBN3ZpQUQWDmtS6waSM0RRLqZ-JW6ZvTFMRyTvi34tPCnKa2u9XkyTU5x43SgAzJ_NJdqzIYGSueqzaP04NnLz5aqM1L8w_tozuRuXKThgG9OHrXeSR0XP07dCAoKuwpJoD9bDkd4rGSZwRXVd8dTpPZf4QRfHLbsi3IyV6SL3WGR8WEuBpbnsbQfI0rYW5WAElqT8RBOLWW7l7iFv6B3XI0gOq7L_F7ykPWtJBTEMCpJKt_ER8C27obhG9HjyFl7b423qp3VXl5qvZqSthH1nfiv5D3wPay-yEqd_XEUDED44xx51VuFRnaOhcr68F9RAyMrSWCOJgFWVplPAORKCtPvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=CcQQoodlOiraYmAia3wtHQ0dBeNJgA3zIJv_pbwkZ_ZzqhFGrCdselOKMaOURgVYxzShxI3JAjMFUJLEhG_-DdH-IeOOW_oq1WGXbPOiB5jBIWukmXnGA1gnquryNKCPjLaz7s6XbnVLkjjMaEjp0-S61NL66ZMbDAZ3-3WG7RNRhoXX2xERHQWvw58dcCBKB_WifSDxQWDAbgOjtVtYGViXZIIpjZmdfCkqoHy97PpN8GMCXV06UHrSFu4YWUh6o8C3fKb1BXM63C9kyV1scaFyM6zZRv1KmmVHNMrGcVpefVK1ae6tymnPZ_vh-xdNGYrmPLik8ZNgUjoqBTBN3ZpQUQWDmtS6waSM0RRLqZ-JW6ZvTFMRyTvi34tPCnKa2u9XkyTU5x43SgAzJ_NJdqzIYGSueqzaP04NnLz5aqM1L8w_tozuRuXKThgG9OHrXeSR0XP07dCAoKuwpJoD9bDkd4rGSZwRXVd8dTpPZf4QRfHLbsi3IyV6SL3WGR8WEuBpbnsbQfI0rYW5WAElqT8RBOLWW7l7iFv6B3XI0gOq7L_F7ykPWtJBTEMCpJKt_ER8C27obhG9HjyFl7b423qp3VXl5qvZqSthH1nfiv5D3wPay-yEqd_XEUDED44xx51VuFRnaOhcr68F9RAyMrSWCOJgFWVplPAORKCtPvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=PLC9VUak2Udl3pmiEVUxRf-vvZzA5K6ZcURde5EJ60EQvYAYnGEXnhOToGZBYZfzAJIC4nmsu39ZxYMxlNZnIm2HDrUgq3h3VNqelnvvOO8dwMKMEMwrlTBxTlSlxM_ONRSUEOafnVmd7lJ4DRjNCXsqk_s-HkpyvAofQRjXQoQyEWusw2Rfb8mhjJZ0OXoG1-0r2e5IEVmfrf_Dy3q_G9U-WMm7TVgzn4OVwudMYDbfLJK2VE7xIbZQIHTLJZ6gnG6ei9nj9yWZ0jMhs9mCFx3h9TGAFgeL5a1eWTyLjDW4hJw6-dndY3Y785FqerZIyKgVenLwQkGhWEqMgtdL8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=PLC9VUak2Udl3pmiEVUxRf-vvZzA5K6ZcURde5EJ60EQvYAYnGEXnhOToGZBYZfzAJIC4nmsu39ZxYMxlNZnIm2HDrUgq3h3VNqelnvvOO8dwMKMEMwrlTBxTlSlxM_ONRSUEOafnVmd7lJ4DRjNCXsqk_s-HkpyvAofQRjXQoQyEWusw2Rfb8mhjJZ0OXoG1-0r2e5IEVmfrf_Dy3q_G9U-WMm7TVgzn4OVwudMYDbfLJK2VE7xIbZQIHTLJZ6gnG6ei9nj9yWZ0jMhs9mCFx3h9TGAFgeL5a1eWTyLjDW4hJw6-dndY3Y785FqerZIyKgVenLwQkGhWEqMgtdL8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4RnDlEZ7DIxmhsinGy4_n_MWp4xBuiZPWQCxt3ryJZJBNhzGtaWKh-j9RgponpAgHutrXQHQgMFRyzN4xjGP5hH5UJ-bY16hotpUrLw9RnHF5guPY5vN3CSra0ut9-ETX4RzSuD6eh0uSekYqqbsnkPj2tlMMzeEQGcn84SrkVXX9hJHghb3Yqe-doYudcE8c1lrLR-lrgqC6i-P3hjcAn51jTqS1P_ErP94zvLtgHmMgZQqbdMTT0ITUcUuZEq3JlLpIMqEibduGckSeNfNaypn9w4yIr9w-Cixm9mPruvewJMYqoI2i464qAIEFhqpxGF56V4r8X7kG0yIjaqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=H0r0l8VosQ20IEPNZMCHYifUlkxmXEqdQXrgygdV3d6sdxb9h0TH6soKbgOigA-m-xrAX3U6xfyu6ExLiNrbFO34B6YAKJ_YMx7bJYpMf4RYsQpi4vECiJ_IZNQN92P5RkX63l04KU6kOrUZGrUVsN7ENdG5_dLxyUzK2fdQ_xVuRo7vKaSViA2RzNhAl60U3Dxw_fsyt4o6vc7ActddrSiW4s8vkAOW5VrIw6mh27gH5QRItIdEZTLAooryFgbj5IlnUj2Y-LLi2wNqrAqigm_htN8NkYbvQ4LqHpIOOhZEmb45tP3OCSt-XgJFuCjnR_PiaHgWF_dfFq2DbtzgrjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=H0r0l8VosQ20IEPNZMCHYifUlkxmXEqdQXrgygdV3d6sdxb9h0TH6soKbgOigA-m-xrAX3U6xfyu6ExLiNrbFO34B6YAKJ_YMx7bJYpMf4RYsQpi4vECiJ_IZNQN92P5RkX63l04KU6kOrUZGrUVsN7ENdG5_dLxyUzK2fdQ_xVuRo7vKaSViA2RzNhAl60U3Dxw_fsyt4o6vc7ActddrSiW4s8vkAOW5VrIw6mh27gH5QRItIdEZTLAooryFgbj5IlnUj2Y-LLi2wNqrAqigm_htN8NkYbvQ4LqHpIOOhZEmb45tP3OCSt-XgJFuCjnR_PiaHgWF_dfFq2DbtzgrjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTWQjQHt132Y1S9rshodGhyNjrCQKzd_kJTx0VmXMNjcH7C39fqBRlw6jIjgNKvRywzSKZ-saj8OhH5V5Gu_aVLzt-DXiYlQyzvfNinwkyIgtnEl8TdoZ-duzUeD6cdGPz40wDHPOXuBFzBeXXNmFPDUObK2ueeaI5Uf95RwEyOwQL806BMSk-I4MhfFdLOxVMeUgPjM7tTba71qhqVZR0isIK0lmsCQSrF3peLr7i3PaSR0Q5_GhMufEoCNgw_nQiGamc8MhLnLUM3Y25tg4ZBX5lTU_g5mR4YENT3W1Bb09W2CoFL-YWZSR98De4oQfIKYGV2B1AsfgSgJ-6t9lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZkFocN94-9sxdijNrqGCAoNZ74A1tXTmyIKjA6XU0FweWdh3Xv4FcZPpsqTM_unGItaWGyqeSOr0Hi6lhj-M-TCjM9eSS93JiOl2Ow6hIYBWjL7CroD4m5PdKSiy6IbTzJIwpG_5bbI6j_rV9U0YYGL1RYG8Dy1bL1DIfVPnBMtfKdqLcjspgpMdwpj3nJpNtr2L-SsPFxs2HYoenXxosyOfFO2OWEYxPy3a5ZAKeid4jcHHnAg8jBKZ6FlBKjodgdEBwDhNePoFLm4T2vf4Lgnho7b_bEKCxLL1-Cdd1_dSpY4raXpUjnkUOLc6sMYKln2NfGpPfKzjU2xvbHPiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPHAVG-AhBM3fh83hH8yfMH_tCfEtVmCJ1uM9cDxi7WwLOqoVa1z-wg9-3b8B0Z7yN_UDxmoiO5-e2p_6yQlUEIslY2ZvbzInVeHXtc_ayqmHGAZAW05z4PAWvFeSoIE4UeGLwrt6rWBvGa62MyYCB_t6bauqQnjIqZQ7VnNcaNKEeAXSKhe7u8E5UVPosv_hXHvb1DkkUgIBjHA1dBrIf86wOQ0uDsf_yu9bnxIdS3iKXEel2hWcODLqmKDgzw9C_5A2Z6Wd66Tl93lfsq0vZjNKf8jZQ2huAeBDnvXPqqYVgZV2ZrJJJlQfyZ-hBmb9S5RyOa74xU8JNIw_8b9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRmblZD0Bfz44wHGUK4kk3A363Rr_07vvCq7E46gSmMxY4qVNWItTbFxU5TvgSvo11CP01PRKzIIEO4FCPQYoe-E7YxcNltj66LAg5i26C8GohoupxQiLQPiIevFyuxTdW2BIwSI3jteOa4G_83IjX8oeP_Lf4Sc5Jb8FEvy6FY8-AUAhJU2hVwKRTA92VODX-YsvezVF1qwgs7JO7P6gCczjxgAj7kkJSM1HGqCImA4WaxIrrKr7qiaX93ogw2dCGyiEjnnonThQADArYYxcL2QekXYI6lYYSQ9xKLV6oS1yqbF3_fPzyyYnKpbcOGnUhVfH0HT8MGXAtqPZsW1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVaDZOb-3nxDLzApQxlpz6VbSjUYkwyjJUnk5UvqfPaijuvAvYz05kPyWUZYruWjpeW0-vZOtUOiO-xOquyyv_4Vn_shYmb-d-t7q4jgzkeLHR0Bd96NCqlmFW86NDMkjTNinFqNcTzXRfXaIq0V57SkMFQteC0rZ7og779uPlI8v6Ns6Y3Oo4IVct9Q1VMT2eBbrmeuG-UB3eK09L_Lxp6J72TKUhFtyISSQOkXHFJcyNMGm8aUrqpzSll0Rne6yGejAsM_g9pC61csTDdnWFYz2BSpYzNBII16lgqZ3kavoiG42WXjnuDHcK4aAWGPJIAcI3SOG-R0WC-Ii1tCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Q3DXnpuXk1hMlprnpPoZZ7S_XF0n7BVdxqj0WLlIt9O2wNezMFKyAIfeZORqLfMP3PBd0AQ45GUqXW3IOvNP6tpE5Y0EO7oJqmpX2-YLz6QGTixyZZiOt7OUnpUDFXNzMFO4TxIjYAX8J00u0hwwMfOplpqZe58Tuj4K0XuN_1c5ZGLa_AUqAL6tky3wdbgHheqZZUIlkXaOmR8VnL0NqSzLBA-PNIwht10NcfG6fgHzGVwvrbOETvwKxAWtKIYmQXjKYxVzz_1EUAyDqVO5lMnBVjhZENO-B2hYiUiq4_gq3y-nh13klGVrx45TTRmzbo3HXZKMBLE95S_UCL-DGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=Q3DXnpuXk1hMlprnpPoZZ7S_XF0n7BVdxqj0WLlIt9O2wNezMFKyAIfeZORqLfMP3PBd0AQ45GUqXW3IOvNP6tpE5Y0EO7oJqmpX2-YLz6QGTixyZZiOt7OUnpUDFXNzMFO4TxIjYAX8J00u0hwwMfOplpqZe58Tuj4K0XuN_1c5ZGLa_AUqAL6tky3wdbgHheqZZUIlkXaOmR8VnL0NqSzLBA-PNIwht10NcfG6fgHzGVwvrbOETvwKxAWtKIYmQXjKYxVzz_1EUAyDqVO5lMnBVjhZENO-B2hYiUiq4_gq3y-nh13klGVrx45TTRmzbo3HXZKMBLE95S_UCL-DGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Imeiu_lBMb7bmXv4VAacftLoRGUS9TGRZB9T7bg6EWCGVVMt4F2Knoj-aTyId0zfEI_9zUpdElQZoEhxcrvHdpEYe2iPTCrKNsNxbqC5v8pEOaMv4CzeaB2FaqQ7aX1fi0qSvFzqnX8_o_EWnJFIzoRrW1Gu1VjcyjEBxNKEwSdbjU7U6nQnDOsFPKsRPQhXSlM6bD_5Q5eZORdR3Vt4WsdvLjMyiaXIDgUo7TFPK-Xk6mn6NRmrOWbW15ObrsmQ9BMjTHg0Il8WtYFkNHq_ZzM73Yzb9NygdB8ole3nOD4ZWCLW-qtrWGlPO0DZyQ55AZ3crOT7HhBKQ8oIbIP4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCSltetpxHBsySZ-Yk6xWWaPpOoS83XTIca4gfSHN1vFJoEq0-XHsVPAzrL1ezGBt0jliJW_r2J6SawoaNJWYwtRz5cXQV-OpssCVJt9VZ-km8ndSxEXKZ-f3HeCZBnJioUBK_AU240o2x9tqSsjosRUlwIqEkctVf9Zqro-nTt4FZYIjkzMg6ZCRH51FxyWvXujMOOiijdHWHYT4S4bU0rHvm8asUUIFv-MGpOLXgJb7DHqw-0HBJhm0IQ-OR1ofJPmFkRZva5Ogg9jA1Z8VYKSmJtnCbxebk8GXwjSGACCUvtZuqqLgHSaog8M5b5fxr-WtyOq9g6bBsnHiSW7JQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=L7EImM2qr86Eoop0Z9AfCar0mppPrRGAO2YJxljhYlcD9RR9m74IZot_UqCeRgtlRmNnwwAcVV6qKQkTG5WG2-LUB4EVJ5W8CwnNO2eiG0DWwcuT9kyU0462N64JkGSm-qVtMdeKpCefp2PTW1PR2qFMHTMmVdZE57ipkjSErHpMULDqMG8Hu7tRndSq1EZZRw6yyOZfMU9dFGmQTp4Nz6XLVP6EZOg-PK3e0PZzh_rM2AWl8jqsLGK5DfzxU433vi6GYdD8p5eKYLwvpZfGpOy1QY3ic1htrqXU_y5XnTlXx1mhB7_NDmgcuG8FtA-fE6aPtjtgIMWfkNcQMDlfF21uwQaSGuFZxNMs4Wmgjzgpg_8ZYPted1XeSByiyKL8hEV57_vzUNM5S9VFsAhAv2FgzEU4CpHm3wrWHBrkUAN5rTuV666FhpKJU70VukIaciOp9_X-6onKWfXFhO9Z2Y3Cy12rfinPYKVc-Uyq3C8YhTqhwxzJ1rVVqIj0OT1YOzwSknILw985xiN8rqIWNEX8JzDC1x9Q3-_4jRSlsZ9kGFx3caeu92C6f13Nqt68xuG3Rsmed4_s5akf262VARA-h7Cgs9UCKAtnJB-38vdgtcGkLbAzRgKFhbPgJvg2bjzJBLaE9DhBwLxBfLqRK1JOBIs8ScUTk-hxOP1-ST4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=L7EImM2qr86Eoop0Z9AfCar0mppPrRGAO2YJxljhYlcD9RR9m74IZot_UqCeRgtlRmNnwwAcVV6qKQkTG5WG2-LUB4EVJ5W8CwnNO2eiG0DWwcuT9kyU0462N64JkGSm-qVtMdeKpCefp2PTW1PR2qFMHTMmVdZE57ipkjSErHpMULDqMG8Hu7tRndSq1EZZRw6yyOZfMU9dFGmQTp4Nz6XLVP6EZOg-PK3e0PZzh_rM2AWl8jqsLGK5DfzxU433vi6GYdD8p5eKYLwvpZfGpOy1QY3ic1htrqXU_y5XnTlXx1mhB7_NDmgcuG8FtA-fE6aPtjtgIMWfkNcQMDlfF21uwQaSGuFZxNMs4Wmgjzgpg_8ZYPted1XeSByiyKL8hEV57_vzUNM5S9VFsAhAv2FgzEU4CpHm3wrWHBrkUAN5rTuV666FhpKJU70VukIaciOp9_X-6onKWfXFhO9Z2Y3Cy12rfinPYKVc-Uyq3C8YhTqhwxzJ1rVVqIj0OT1YOzwSknILw985xiN8rqIWNEX8JzDC1x9Q3-_4jRSlsZ9kGFx3caeu92C6f13Nqt68xuG3Rsmed4_s5akf262VARA-h7Cgs9UCKAtnJB-38vdgtcGkLbAzRgKFhbPgJvg2bjzJBLaE9DhBwLxBfLqRK1JOBIs8ScUTk-hxOP1-ST4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=VxLUhCd2lWMsQJOmqaqDdDfM1Sm9J9cFQmN3u_2oXUZYlULbzTDb-kVvthQ6zJdFgbSoM0Dt6wXNvx_MBbc9e1RL5dcTvXMizzjpniPSoPFqA0t3pOyVhXukIyDVLN1FTwxvbiIaGFTt8jlBBfJEr5VfiXAPOFsrAzqe1vNLt2zzDTt0irWPWQuKaeMAGk7X3tphVzCoPbFkN5TVJawN9eJugSXupcpQp0krTIRdzCZuG1w9AIc2XbzRABHvjfAMADhvmMn9ypL-5ZnQ-CUL5V8O4Cl-bKwR2nR52b4Pjj4LfijvbCcfvpRbHV8kJ2dsPTv-flsj3Ne2XOWZl05Nrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=VxLUhCd2lWMsQJOmqaqDdDfM1Sm9J9cFQmN3u_2oXUZYlULbzTDb-kVvthQ6zJdFgbSoM0Dt6wXNvx_MBbc9e1RL5dcTvXMizzjpniPSoPFqA0t3pOyVhXukIyDVLN1FTwxvbiIaGFTt8jlBBfJEr5VfiXAPOFsrAzqe1vNLt2zzDTt0irWPWQuKaeMAGk7X3tphVzCoPbFkN5TVJawN9eJugSXupcpQp0krTIRdzCZuG1w9AIc2XbzRABHvjfAMADhvmMn9ypL-5ZnQ-CUL5V8O4Cl-bKwR2nR52b4Pjj4LfijvbCcfvpRbHV8kJ2dsPTv-flsj3Ne2XOWZl05Nrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIpzdrA9Ekz6johBW1RPS-rKIa_6JEnExvZ4KdFCHK-RBuiB3rAFSUdgWE16Be5-uBtxfrj6iz4C6Fzp4i75eXHO_UTULgzItJBKmddF-9scuTNkA0wGxkjyOSpOcU5oE0ATFXMDbc2fzdzud5IxFKBypw5RR2iFyFY-mATqDeRmI_fbvRSRDeyTrvLmAtIyVY7JcwscW3N41wMBzF3W694Wf69XFdPyc5jTtD2GrU9uwTnfzM1hrdg7iOFN3v_LiqY2xZTAhbK9NDssQzo3oQPWlp4YXwHdo1ExxRQR2VnkUgeyvQWldah50d7O_77vE2rbQj7-Mkwe4Rl3O6HvE5Nk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=t-iLWePhESkLrxXqQiPfcAYeNYsh5QE8zXxwBYWtfApjSzcCSRHwjbHFZhRQVtwykJ7Ml0RMB4yvUkSH8WxNIORokDv4kdC29P0b-cGh_gwigY6geCIZsAHYZ06zy-vdHPlIppept9yUW2FnPvipDTmeY5mGn8oVTolfilTlxEhsE5cZB-zFST-8zDuj7U5aCztK3Vl0RuQ3TofNYjUPXKIPLw6E3kKA7GMtuZ55a8jyXS8yamkoNvk2n5EsqA0Ihs0cETXyla0T6SLuR2BzLpFrHsOS65mX84nvgzpkDz3a00OltxyqGkB5380U3ps4PZftv_2q_PXwtAvr_D7JIpzdrA9Ekz6johBW1RPS-rKIa_6JEnExvZ4KdFCHK-RBuiB3rAFSUdgWE16Be5-uBtxfrj6iz4C6Fzp4i75eXHO_UTULgzItJBKmddF-9scuTNkA0wGxkjyOSpOcU5oE0ATFXMDbc2fzdzud5IxFKBypw5RR2iFyFY-mATqDeRmI_fbvRSRDeyTrvLmAtIyVY7JcwscW3N41wMBzF3W694Wf69XFdPyc5jTtD2GrU9uwTnfzM1hrdg7iOFN3v_LiqY2xZTAhbK9NDssQzo3oQPWlp4YXwHdo1ExxRQR2VnkUgeyvQWldah50d7O_77vE2rbQj7-Mkwe4Rl3O6HvE5Nk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drOGls2P0MC99hvM0C6FFBw6yH03UwiaQuhI9ipheBXc5HmyDWzG1kH7c0rBKfToa60YxbZBBHe_rn8bya-iP18VqIFumQstqQNLBfVcn1Bi96dMSKo9c4k0PIXow7yrlOaur8dJYsOxIfnUjmD_iqUUbtAoVJR_aj_fM--60D2b-yx9jdQpYczH98X8-h4X75b2sYYJBwtbOEgdVYDJC0Klh_V4Dq4xgHZ2Lp3-8juZrksN0s-eZJWXIEoWeRTgWzT1LzWDB3JwpRuxkuPcELaPsKpd1ANi1JQcBLT8G7cWmSWQM64RrIB4wq3s-y2pbHNwmtrI57UVRKMUoEp9Gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCyPle8JGEIpZ_7VHIHjBdHFU8hM96tLtRRUo2FKdO2PE5wTYcI9JknV65rZoi3HWrnSpFZ2TpZMKL3_EzCb76an2u441iFWXWBA7egmCvO8OKsGAM5Pj5IRJK6gqnXg05gD9e5SXj-gjWvQNdFCT3JELUlI4mviiiSrGymYkJqa0OqABHQPpQ5Wqyy9CjdIXdog-hIfC8Z-dHJuy866uZ6x3bcefWRGYws-rWDnZepKaV4Iasjbgv2P029cgJapKxNNdhnmCfLVMORlbZ_pzQGfH_6K5cwX74FnCyUzZANHVHAmIZ86lg8_Lq-hqGVOJcAd2zKxVNWHzxeZh3xvrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nk35ThR5tDmlZi4jG2MZadIJaTUpOlplUH4QLRopHrDzcvKRbrrn_Z7aW0CV8eczXgpOb7Nh18_J6gHoSjzzag7vz5qiHihQ0GF0Kz1Dz0hT_uM3K5Wgo1pjAZIHnz4D2UybzKSlMSVkxBNObpznhYVAG9N_8aCdblP2Sr5Ems0i8KnBDMe8xuW7usPNUQncOcCwvgcPMV3ku_TuaQei3Yj-AZzBQNI-UohBGcM8nX36sHJaZ9rB1Kq3M5z6Zrb6p7qBFkLt-HZiVy3pbABjoZ_Y8d_RvQOTJnczvYvsTfGyKq9pvL5RWYGRCo4hZMUU--OmwbfoADgaxpK1DW7oEw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=k3rou416fUlVZGbx1Evfg3cxPlmx5tdTzyO_m1MEwFP74CaoSu-HuRu-jhuYLQv3ii4LBm2qNrBxOlkHiYcAuotbF4AcTMs_rWbrPY-FkqsWJJ9VWG6Oqdqmjdlo_dKN-_wuYACZcmUCaOOEr8cOIxzHgc7nHaLg0Umg6eC3mFe9_cewFKnDEB4yCpDa1xE9IqCuyVVft86SWz9n2Sm400FDYlgjKA1a0fsodCFgrsU6pdPEn6mBwZAAEclB1CZsJiTQAJ9h-UFHVIPl9XXfroecSdTHoc_8HPFDdZuQgHY3BtxnMqRWSOeGBCvSbU5dQgAbC5WJQhUVuIHJriRogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=k3rou416fUlVZGbx1Evfg3cxPlmx5tdTzyO_m1MEwFP74CaoSu-HuRu-jhuYLQv3ii4LBm2qNrBxOlkHiYcAuotbF4AcTMs_rWbrPY-FkqsWJJ9VWG6Oqdqmjdlo_dKN-_wuYACZcmUCaOOEr8cOIxzHgc7nHaLg0Umg6eC3mFe9_cewFKnDEB4yCpDa1xE9IqCuyVVft86SWz9n2Sm400FDYlgjKA1a0fsodCFgrsU6pdPEn6mBwZAAEclB1CZsJiTQAJ9h-UFHVIPl9XXfroecSdTHoc_8HPFDdZuQgHY3BtxnMqRWSOeGBCvSbU5dQgAbC5WJQhUVuIHJriRogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWNVp5d98T0bnULY81v2wQ1F00kQdu2W25AGof9pFXkcSCLvT-V_PCcny59Fepx8fPuhTJ-Zw8xk_ynXmmtguQ0Ir01yTHy3X78UVd1XrYoIqQ7mSlF7r-euNQ2PhYbSn7W11o4GZbinq8gp9qhaYzGf6xZaNEIqcYMTxiKHhyYOt9QWkCkU-DR2cVSnPCOO6m-qms9Q1LlUg_ksQCnwTTKQF2Qj_h71sX0xbEdjJIllXQTijbXaTyAXBjzLLK-VYCX3cqSBvmhTRaOagEgBvLvXQ_rbN8AzqSVPjkQqzq9HIwWFqBo0dR48Xdub3T44WFXCau0631msij-pbUOMGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A4UDIVpofmheHGurYBt7KV1zWZiZ0qZ7IipVHLbMVL-XV7AM-rBBazKC8v6Q9Ma0OpOdsH13aeXswcWIJxKLFALlQk0f51-LQsGf-5oabo4O0IE9U2AYoyB0ltb9Lf7z79lBCvLaRuTu7DAORAwr92WnaNZg8eub1xselJFSzUv0m-TuiH64TJne_AWduOJOYPDfIXEhVHKKJp04PDjxOhUgjZdrggyMBBNOjbMEP5QgdkX9Z-2og1sIenQApOnyOjcZAM0pPQPGWS9sSdYSZEADokrakTbj9HzUAIKPVS9z7in7DDYRxH839S7eZMPaeLBIuIkBbayw54r9GIWOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PInG6IAxT8_iENLsGwVe45TCBBDo8-gyjjVbaPQ8fdOVEESzhWN58bZq13bq8HmMw3fqfp6rPG-zW5XAuExahAbQTSL-O1ve_kBxPiOdeUqob6msvfeUgsYTG0FQE3b3ibGZSlj4LRQt4fOphQEWb49Ln_7djuYa66ojaVkuaf1BM-yxlESMNUhYFM2T5sWTovSUuZVYnJkB26ZbhS9wS4HVTThj4eHvJXDtbJWZDe4S5iFfFZPJvimZxJUvMitye0m2GOpuRcIyoMHgkYMkryWwF_48dXpfa9ZdPQL1HFOmsZ2k8N7_kFBhBZb9_BgxTOT_78myXcvjytJGkFCJwQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7uj_7722NotCosP5atfSn6ubivmtqYEZcLwXAW65_EUpvSjwPTv3h-fG8Av9eAyyf3LNgB4tYdSBttTtH3PMK5CtTmN3tpIGk8XuIMDjyeykA4fqEjh3C03Qi6IrTXE3phUhkm44Kn4uW1lnQsvvNqDzapbBghn01_js5dXnubtK34h_vhfwW09U6uGogLpcVAoy-b__jQhkJfhw-f7ugI1IcLLBT41nv3-kGy1nZj15HiI1E5ec6THr2TAY_GlRDf_Cfu-LsA4r_fTCM2Qk7k7ej6Lxwfo0cSs9VK5tRR1AGvxYklizKX4jhOsQTIizzLWVT8E179YnSAofAJ94w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=RWCAmHp--sDPou0AwRca9CVlC6-EaigV1nLM3AV3GzrGHDDE7TbkGE7g24towsCD_nZt4edE0jbbDdN5kxkscO5iI5svDEMPwjG2W4_859n1Vftwi7ZEmd_bFaYYoiSdtLUWFuTG9eo7Y8xmXdQ7JOrExX2KoStssihvkUeNgNbcVmP1iY72-Tj7mEv05S4K2mz4pxRKxW82O0Vv5Q3x8da_P_gJB1Iw3xzfD_HUPHxr-MDow4LCYBJzfgC6t5LgQpYfSdYwuMWo37kaxzkTtf4Veda83WrNfNfcP__ZFHOopywEPWC-WbSGZ-1fDvGF4VxPkTHjkjMI6Ovgwixym4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=RWCAmHp--sDPou0AwRca9CVlC6-EaigV1nLM3AV3GzrGHDDE7TbkGE7g24towsCD_nZt4edE0jbbDdN5kxkscO5iI5svDEMPwjG2W4_859n1Vftwi7ZEmd_bFaYYoiSdtLUWFuTG9eo7Y8xmXdQ7JOrExX2KoStssihvkUeNgNbcVmP1iY72-Tj7mEv05S4K2mz4pxRKxW82O0Vv5Q3x8da_P_gJB1Iw3xzfD_HUPHxr-MDow4LCYBJzfgC6t5LgQpYfSdYwuMWo37kaxzkTtf4Veda83WrNfNfcP__ZFHOopywEPWC-WbSGZ-1fDvGF4VxPkTHjkjMI6Ovgwixym4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=gzmQnqzWzTBmG_4wSWhMOFjKIfhwkoLZ6Lr5yEUzb17g3-Un_LgnIuDdq3NhDvab2SngRX1YL7ixsMyHqdBDRMPTlFBV1bgzxM-wtwWrNuWvPxGDBGRG5uWAbY7Qgnhk__ST-BTWQmc1Vcnu-6Mwl8EegJh8tir-6gErbUq5aIlsX7722VM__a074iEoI0-5YVQ6aUFUZQCAxNz8jov4Kiimx_p2MAIktLxKzPoIwgVs_8ZiXeBkub_gU5liUCBi3L6iaLQDwQjKaVvJzpwJNaIw4GbGquFxSzWmV4uKHrZAz5KrY-tchGawf5PuOp21vfdfx6er_24WEuK8k_viHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=gzmQnqzWzTBmG_4wSWhMOFjKIfhwkoLZ6Lr5yEUzb17g3-Un_LgnIuDdq3NhDvab2SngRX1YL7ixsMyHqdBDRMPTlFBV1bgzxM-wtwWrNuWvPxGDBGRG5uWAbY7Qgnhk__ST-BTWQmc1Vcnu-6Mwl8EegJh8tir-6gErbUq5aIlsX7722VM__a074iEoI0-5YVQ6aUFUZQCAxNz8jov4Kiimx_p2MAIktLxKzPoIwgVs_8ZiXeBkub_gU5liUCBi3L6iaLQDwQjKaVvJzpwJNaIw4GbGquFxSzWmV4uKHrZAz5KrY-tchGawf5PuOp21vfdfx6er_24WEuK8k_viHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=anC0WXHYVwu5L8jiHXPkbJzBDJ2KoMRzaXJkqcOtru6VuTsKsLMv806BpBcg5lieNdhmH-153lIuyRjLr5Dk4kBwMZl9Bi0GQQsL4ebEqkPeo8ZUvJCKQ1Fb3FjSEDAsOQbZmZ6URi9qfmrwuHjrrMEEVwodh-WKa47We-wDKsVaFX5MtK17TB-TCC6zCsbBBQ8QQDS2xp15yPDMxvJD74eSQuNBon_NQaTTQiX597VGJX05TKrxOhEWGJB-tgcZFrM5iir1mg88drlyryipv_-hnVPC4uxjPhbLMK6lPliMyf4ARffj5zH4ipDl2J3PfNFT7rySnfFzKdysLey3_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=anC0WXHYVwu5L8jiHXPkbJzBDJ2KoMRzaXJkqcOtru6VuTsKsLMv806BpBcg5lieNdhmH-153lIuyRjLr5Dk4kBwMZl9Bi0GQQsL4ebEqkPeo8ZUvJCKQ1Fb3FjSEDAsOQbZmZ6URi9qfmrwuHjrrMEEVwodh-WKa47We-wDKsVaFX5MtK17TB-TCC6zCsbBBQ8QQDS2xp15yPDMxvJD74eSQuNBon_NQaTTQiX597VGJX05TKrxOhEWGJB-tgcZFrM5iir1mg88drlyryipv_-hnVPC4uxjPhbLMK6lPliMyf4ARffj5zH4ipDl2J3PfNFT7rySnfFzKdysLey3_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1eiwxEBrVuoAtS2kJc50kNBXoj9rq9AAJAADOIG6XTj98wEPqfRFnTTTNZLZ-7Jlr2lKlVdz3BKhUGXX-UlwRraRUPVankr8BV34dfu3ZKvWhO9R0bOwZb_qCNP02A7hpniMpDpQyFLPU_3iHv5O33jkg7JTLdDbIbvzViJhteb8xlc8YwINSjLtc4mFsCBQyXvExF2GRBmPgnVWWZO2TzILJanG364NHoagJwD4t-428NMuTVz9ObZp-tj-iwegihq1As66H_ZFpLFrIOTg4A-eClZlRm1JctJo2KRrg4W7BwCtG1j9D2wVeC-Rib4o-bW0iCBzOb6hWiF3mD99A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=NKjbzYfX56hPTR6Z0iP58Bsto_L56Iovo4ChpDprBRIzcBdrze6j8cefzJ0J186u_MALav4SxhlY_oJt65VbAc7IYeGkHQ8GRowD5Kzi91n1iyINqYSl9V8da3wHMQnoCmEVsb-0j1ONxHY1ePpkBkuh_JGINBnN8guTYmDug2_rD-nCjT5BJg4M9eUUCIYGLK97mi1B5kXCLO1IHDhp4VZWGw8iEPKCkWpTs5RGlugiU1vjwSy6up3N7vlAXMNTzwuur5Y4S0zh3vvKVIXDo7GDyE27ltq4oCwugZ5QFUahiyynFhw6X3WHKSfcjvMG6j_pVMPmWHG9SN3fI7d8wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=NKjbzYfX56hPTR6Z0iP58Bsto_L56Iovo4ChpDprBRIzcBdrze6j8cefzJ0J186u_MALav4SxhlY_oJt65VbAc7IYeGkHQ8GRowD5Kzi91n1iyINqYSl9V8da3wHMQnoCmEVsb-0j1ONxHY1ePpkBkuh_JGINBnN8guTYmDug2_rD-nCjT5BJg4M9eUUCIYGLK97mi1B5kXCLO1IHDhp4VZWGw8iEPKCkWpTs5RGlugiU1vjwSy6up3N7vlAXMNTzwuur5Y4S0zh3vvKVIXDo7GDyE27ltq4oCwugZ5QFUahiyynFhw6X3WHKSfcjvMG6j_pVMPmWHG9SN3fI7d8wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=dXGKkCxaoJ549AlMxtedU_85CecwfTpwp5ksHI5I9jGIRi67m_tw2gcAe-dXmo28sGNdCNBRRe5F2MDw_oB0VCn4jVUDp-wqyCPiMNs_79ZyEp8oMYSzs45XrMfIVzzo1sF_C2-3gE3HVeVVlM4g959JIa6BsoLadqCnUzyxppmNLEWa2EYCIkXZGSWQ9HONMcYq2SYg1oz7-1cBE4KOCp76y9WqpiTyQbD7l6GPDCntKoy_zaQzWAaG-ySV4YAOBMSGHVHQPLi4UaFBIQU7g6E5pgGMoOVDpngiOcCGmUKa-HKFDkxGEnXrgbrbXPfkt-tVGnm1bOBQEtdoqPp1uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=dXGKkCxaoJ549AlMxtedU_85CecwfTpwp5ksHI5I9jGIRi67m_tw2gcAe-dXmo28sGNdCNBRRe5F2MDw_oB0VCn4jVUDp-wqyCPiMNs_79ZyEp8oMYSzs45XrMfIVzzo1sF_C2-3gE3HVeVVlM4g959JIa6BsoLadqCnUzyxppmNLEWa2EYCIkXZGSWQ9HONMcYq2SYg1oz7-1cBE4KOCp76y9WqpiTyQbD7l6GPDCntKoy_zaQzWAaG-ySV4YAOBMSGHVHQPLi4UaFBIQU7g6E5pgGMoOVDpngiOcCGmUKa-HKFDkxGEnXrgbrbXPfkt-tVGnm1bOBQEtdoqPp1uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=n8jdVGBaAKzGmcEDfbTCWMvWf-4npOEVrFh30LmzUpFKdeV7KFyZqXUzG5belAWyHjY7Ss5tmmue-0zWEWkeoctisu4pljKnWqBEjycfGvXh3DjyrAF5lGqOneBpeyTBK5_QnCWJJqcNkJFLlpHlLne4EMfN_01OcugnKDdSAgVVhPkxLeW_qjzYLJVM8nj97t8EfmxE38qd0cFLTX5KlXzGRBh0P3Kesxc61RDBRn7f_Ns9rziHzCiSiuObhYVQl0TSuEHswk5cYDTSeOHSmn772jkAWGDXE8oTDCqU_cYQrV8V0No3RVUkxu3wt_a7qYFhusaVQo6fPwLg2xb79A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=n8jdVGBaAKzGmcEDfbTCWMvWf-4npOEVrFh30LmzUpFKdeV7KFyZqXUzG5belAWyHjY7Ss5tmmue-0zWEWkeoctisu4pljKnWqBEjycfGvXh3DjyrAF5lGqOneBpeyTBK5_QnCWJJqcNkJFLlpHlLne4EMfN_01OcugnKDdSAgVVhPkxLeW_qjzYLJVM8nj97t8EfmxE38qd0cFLTX5KlXzGRBh0P3Kesxc61RDBRn7f_Ns9rziHzCiSiuObhYVQl0TSuEHswk5cYDTSeOHSmn772jkAWGDXE8oTDCqU_cYQrV8V0No3RVUkxu3wt_a7qYFhusaVQo6fPwLg2xb79A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=JWTnH-PSfYZVsBIJ4vkmOsjXI_K5s7PH6XVSSyiT7zsyM8B8b6WCTNXf-MIyJ3ME27LN1s1JXIqVs0ywcNNBcVYRRnlIS8MLRHoHfY71G4b51y2OkFFomq8z8RWhwV8KKCgGGS6rxjYiFxswoNxYEcMkCnOAEVML64Wey2GVTxetUTOdj_7bSW0wF__THn2TbsPJxnHeaPhdFd5ouATE9mRw4T9rvLukPmWx8IwwdvWwYhBz0-uOHm6sbkyxq85yqPzN0GkY7BfTxuxn-e3QSqBOPvnDrAmylw47VBYKgjW7xfl0KKEaXPdEX-LZVUEWaHEtXBbFOO7sP_hEiF72blUW5C327ZatrHQxsAK2WLtjDMLfh_0d5dp9bxyMEAIAgicA3nHfCcd0FrSLQfzVaWFckuVRQ2Dfz3eb4sd_dmUb-kxfiUdwO8pn2cnQ-05Ayj0A0hG1SJI7xyPwYWQjimXwV1kfxGt7plMQq1r3mZQPjgepJEDKHFCGWKfKJY0cZBZdeTJfL2r86rPH3hsVz09sb2HsVYLFC_sUejNp3CylSPzcth5MRvukSdBgs5eGRrvSahkB6XVaFlMFmk6iAdSehqec2JimZnV5hOiJN29so2vc5clGuIuOtfIt2sUpUMbXU-UCHSHVARwBJUlrSxsQqQ3EdH_dkNQKe5GdREg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=JWTnH-PSfYZVsBIJ4vkmOsjXI_K5s7PH6XVSSyiT7zsyM8B8b6WCTNXf-MIyJ3ME27LN1s1JXIqVs0ywcNNBcVYRRnlIS8MLRHoHfY71G4b51y2OkFFomq8z8RWhwV8KKCgGGS6rxjYiFxswoNxYEcMkCnOAEVML64Wey2GVTxetUTOdj_7bSW0wF__THn2TbsPJxnHeaPhdFd5ouATE9mRw4T9rvLukPmWx8IwwdvWwYhBz0-uOHm6sbkyxq85yqPzN0GkY7BfTxuxn-e3QSqBOPvnDrAmylw47VBYKgjW7xfl0KKEaXPdEX-LZVUEWaHEtXBbFOO7sP_hEiF72blUW5C327ZatrHQxsAK2WLtjDMLfh_0d5dp9bxyMEAIAgicA3nHfCcd0FrSLQfzVaWFckuVRQ2Dfz3eb4sd_dmUb-kxfiUdwO8pn2cnQ-05Ayj0A0hG1SJI7xyPwYWQjimXwV1kfxGt7plMQq1r3mZQPjgepJEDKHFCGWKfKJY0cZBZdeTJfL2r86rPH3hsVz09sb2HsVYLFC_sUejNp3CylSPzcth5MRvukSdBgs5eGRrvSahkB6XVaFlMFmk6iAdSehqec2JimZnV5hOiJN29so2vc5clGuIuOtfIt2sUpUMbXU-UCHSHVARwBJUlrSxsQqQ3EdH_dkNQKe5GdREg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=lf92uQXJwMoJie98NpxiVCR1Bcz38XzMm8KVD_-8WfdtJFutNVw3tEQTeqQOaIXqyddlAypSDbFWYxo_6b1FEMy4s_QZtwm2dNG6sYiiW0jkEwUQQnyxgsRctSUBWyOEY6PSJVYnoiJh0B1p7cb-u1Fx6sfsj9xkaHYJ1c-ORojMjf5QU0GXuhPJzqVoJEIef7sZ7q_HxOxqAZd76lQ6HqixjTfjxce4S_ZUUI5ZR0AbypZ0nxG6nCJWStuklLvDYFBCGpd_ms2HYF2vS2ZTBckTmcpTaVTz4MgYWVyOxF2FqlqC3OTInMZM1IARthDiCDfyYsObQeX8gyBEjSGH3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=lf92uQXJwMoJie98NpxiVCR1Bcz38XzMm8KVD_-8WfdtJFutNVw3tEQTeqQOaIXqyddlAypSDbFWYxo_6b1FEMy4s_QZtwm2dNG6sYiiW0jkEwUQQnyxgsRctSUBWyOEY6PSJVYnoiJh0B1p7cb-u1Fx6sfsj9xkaHYJ1c-ORojMjf5QU0GXuhPJzqVoJEIef7sZ7q_HxOxqAZd76lQ6HqixjTfjxce4S_ZUUI5ZR0AbypZ0nxG6nCJWStuklLvDYFBCGpd_ms2HYF2vS2ZTBckTmcpTaVTz4MgYWVyOxF2FqlqC3OTInMZM1IARthDiCDfyYsObQeX8gyBEjSGH3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=U4--LFK4Dls3nwQqBppzFz23gJmSGjbe6cBUOQGLSSLTllD_N-nJKrIPtzbVCpJ0GSFjTBxuqqrqgIbV9HPNfWIpMjqub95i0WXW2NObfcI6W5J01f9BFcD0eBnRkOPEt6pmf1NWbze59BsaTXUm9XnsVlfEOfgrnwA5Nj-ClpUDz01dWmmhBFi1UhU2pzbpBgSi6ff5DPdQDTCpvDExtBafnfUHFnoK0cfNCuBIRQs0o9mqd5zI--iZ2hiOgm_8dAnTdWqyXbgH6Ra_h4e9NgFOizUP7C6WCemg1MI7MqZN983v7rcia8zYuH5oKgBSB7iiaPVh5FScHQEd_iI9hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=U4--LFK4Dls3nwQqBppzFz23gJmSGjbe6cBUOQGLSSLTllD_N-nJKrIPtzbVCpJ0GSFjTBxuqqrqgIbV9HPNfWIpMjqub95i0WXW2NObfcI6W5J01f9BFcD0eBnRkOPEt6pmf1NWbze59BsaTXUm9XnsVlfEOfgrnwA5Nj-ClpUDz01dWmmhBFi1UhU2pzbpBgSi6ff5DPdQDTCpvDExtBafnfUHFnoK0cfNCuBIRQs0o9mqd5zI--iZ2hiOgm_8dAnTdWqyXbgH6Ra_h4e9NgFOizUP7C6WCemg1MI7MqZN983v7rcia8zYuH5oKgBSB7iiaPVh5FScHQEd_iI9hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMJbCz1maZ_aCJS0_3ypDEpccTow4sqGBby2tomuQ0EmRAZFlZoZ4egU5eP9Sd8pcLEDPJftpebMMbrunChattCiPWF0lBxa6P5gwJlI3ijHHxjyr0EeGW3MCF6gtXJ0AsNAL1msbWHMsAQ_xlRW6b1F6GXo9nDGA3qRn1Y0EqxSkuFd5SGKYAMDWc68sBJP6zEW12CbN4aIzuZiBq-sUIVulsci64iCbRtvnfBY5_dHa-H7UD8Gbpu6V5hj9nP2Za189E7MJosf8B3n20gPjHbS-IYQf_MarYnlZYK__HxysFnAkCiX0BT9-PmQszc0DFA6u9p1JcqSyvJrGx-cBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jn4vV-fNvJ12S2ALaQ6huwTlyTOZHLPxjxtvD7IbFlHBzqEGZlTgdWb_OJwOlsGYwHVFcVHPgRyxUBjQ6zJ_pVO9Qd5jjb-y9SsMKqrWHuTjng67jfo87son1xsIKri-oSPX6vzjSvASlKvsSrZmGlIf9pcGbl_waAFvn8wSmPt0mqzkiDcOTKFqyyB8kq3COqEnCPeeoQvFOfT1C2aDoyS_c3AO1IGv9RyIrbHaSGiPk2sg-CpNv7Rq8nm-QwlbgQA2U098TmtcwFA98Oy8GUO54gQzXaC7vG_Z8eNrvAuaTXYY4X6Aeh5SDKYWJ3xnQg3Y6idTDvb0D2klHfXnSg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=WaS7lRCjmF0ZxATMUtzlrYXUdPx6AEl78JuqI2CW-x4CKzPk2H0NjWUPHXp2nbjsMt2zak9ee8OHNsIi0qfZSajpfnDK0PNLvEAQ8VSQbv0WuB9r55XIOPAiWhGAZImDjCwTkhP6aoZNy8L1iqeUWllw1hpxbOfAYrd6LzaXfJ8ScfmYD3cXQhb0q0Ib56B3twkHDcSuK6yGUPN_r4_lvyrxfFfC60S5j59NFkd5ZpK6dg7ARey5UbSgTYvZSvdAjc7U6K29K0zFgtpSX-iLYg9l3Z2oHxnrDJOR88hXj7Ksc6WzGJFzDqWY6liEmmSh3oo98YLmCYHqDoPBFm3TIaegJlL8L_tQI8kuU9qG43NSqQ4S_uhjboJODl0LE5mcowCgeGNRcMJJ1fZLktprYJzjcDt9MjFaEyXkeoCr2a5DFtXk4SzFRJuw-loVKCxgpMJMxKGvzBHT3SU8NXGYD2i4NtWNgo8p4BDPwLQP5YIYJCII7DlRl2O5qcFLsZjWRl6t_B5HVhKANXCdMxtlDUgHXKGBBdI0U6nWy4TlxjIX5htxC7g3CXfjgIQxnhk3CQyvQptJVTP1w72yvK8CtQPQCSXJg1UkOtqxCrWJQvZlzyC91GAWHOpFOW2tf8TKJazFTzyFHIv9yqpiusa3r5ewqJuOclErfXmQw1OmsN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=WaS7lRCjmF0ZxATMUtzlrYXUdPx6AEl78JuqI2CW-x4CKzPk2H0NjWUPHXp2nbjsMt2zak9ee8OHNsIi0qfZSajpfnDK0PNLvEAQ8VSQbv0WuB9r55XIOPAiWhGAZImDjCwTkhP6aoZNy8L1iqeUWllw1hpxbOfAYrd6LzaXfJ8ScfmYD3cXQhb0q0Ib56B3twkHDcSuK6yGUPN_r4_lvyrxfFfC60S5j59NFkd5ZpK6dg7ARey5UbSgTYvZSvdAjc7U6K29K0zFgtpSX-iLYg9l3Z2oHxnrDJOR88hXj7Ksc6WzGJFzDqWY6liEmmSh3oo98YLmCYHqDoPBFm3TIaegJlL8L_tQI8kuU9qG43NSqQ4S_uhjboJODl0LE5mcowCgeGNRcMJJ1fZLktprYJzjcDt9MjFaEyXkeoCr2a5DFtXk4SzFRJuw-loVKCxgpMJMxKGvzBHT3SU8NXGYD2i4NtWNgo8p4BDPwLQP5YIYJCII7DlRl2O5qcFLsZjWRl6t_B5HVhKANXCdMxtlDUgHXKGBBdI0U6nWy4TlxjIX5htxC7g3CXfjgIQxnhk3CQyvQptJVTP1w72yvK8CtQPQCSXJg1UkOtqxCrWJQvZlzyC91GAWHOpFOW2tf8TKJazFTzyFHIv9yqpiusa3r5ewqJuOclErfXmQw1OmsN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkcFVN6KmEaUbt714QU-FncLm9_cijXKm2CJQUO4QkBT3sPTIl0mauBiWhODRFP1qaYjvookcBvB4Lxep7WdITN-Zy67ZZAolmlOXUJpIxi5xhLz49EF9An6xOydofYnBtfGgXxEQX6BB-CWEUIeEpsxzrlzyaKDti1MhsiomZCi4SxhPKxf66ORlTcnki1qe3GW5R2dImHnn8vZhis2SS9Cql_sGQOHRXDIyikw2oxGVrmiWZsrp0xW8mGxFOYV6J6dxbQlsXelAKNVD9CvAadHJcohNN17YQj4hKMrk9yTVfgoOX2cJt2WloiPMK89SwS_FYoPjSu48jGI0iROpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXKsU8hcbmpvEsGadj8uXvDHDB_9qRyexo28_riFcyQ5pxr_12mXxR4WUrLRBj734BbysHOaMU5NfT8dcVLhG5h25hwLbQ4Kg7WINL-KUo7jlGiiruhevtN1TaIvbykCVWeFD24gCnS-yDoniWTHKaZulZxyGh6BJ0TLPvRNlHhrlCb0Nr5xMCbWTJgpD1Zw2ISJC9-VOJM9zw4p0hQo0OMAtJhIJ_2ABDSzplAV3qdAmgKquwwCIcz-LNH2szx8R-JqiXSeneQ4fgimXcPWce-EUkLGsGe-Lf85GjHTZJOTk-olAsOgj-CmQT4SNszsAsFf9WbiPLNv0WeAfSRbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVAPMNMSVe89IgFgiRrC1bLN1emlFwQx33R5QO8Xaf7uXwrBctBz_b1aWARJRUTddvd_fRPvP-qEX_ROEWhTHMIuoQxGVZFaOsvHaCsalB-N5iIFkRrRym9xkMVo045PoNcEkGsq7Gp-hxUvvzW-Dz37CVH5KJeCuuhPs9gENZ9SQwDxOec9Gu0YY35BW4sP3gnIciI8KO0OLTbBhMthPSvweoodxm11qTMCDi6OmqEqNTpvKwtMUbaxu_fn31WzqQLFSOFIVmcjsyViKuhsaQzsaSOWDCFiUD6sZJh13nPcpWe-HF-3KOm_yOeaoNb4OMJWq616vD0G0nJlgXm7eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCtAwQtsAQolbJgs4J5Q69Ns-JEe91w9iiB8dNsnm5gC7AdFMIYzvmkWptD1q1r5eqW5E6we6HSUs8E1EoIJEApNZ17bveDwaTHQqtsjPjWj73kBuXlH9_1HDJQaXxsBiQkoet1l--3obY196xvS9tIex7WMMnivf00qhnaeQgMvKT1LHDHximAosteBNDwbw_uADk4t3jzfT6opdt61h0rVaXN4MQV-BK5aLdehT5M5EI0CC1NjFd9EiakuG1r-gnixYdT1-0lLYE5zmWuIk3MR_pYjQ2HfxE7iuldy40jC55Q4eWej7MOT89wDnGI2VHeLzhwTfM39QHCy2uZRKg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=LDas7w8Grl3ayJ7xP9yfsV0-uTo20EtBR76a6W-ekdrgD92ubXFL7YrFTn_qk8wN7dt7mbYA_bb_Jw-Lqt--Myx7gKf8NOxPos1E1G5oPulZrs5FVs8mwY3J-4CrjzjwrkDiHTUyp0e3Jwo3ddrN5NS0twN9p-teRY3eyxVjhdv93Km8xfeZvQM5-QO5w-Frmfg3I2PN1hsawFGROqf9ZdLQToDBfhbidFoqcrWem7unvvQTmKZS9mAqXgIf3l5i1EHC1356zae-LxbRYWI5JEtbIPVNl85gcfrsq2JxOyvNLukdMjZ3T24HWC1M7XGgUZL9memEq8IQfKZKMFS6X2CHaMlqKcHtVI27q7Qsy7KexZQXLB38EalLbREavhNtT-Y9fRhwF-6axdTrCrPTwOpjkxQDjNEUQRIjO5iJG2SuROTUr54qU49C1dQVuxP-HU1OB1kTCEbVR4FgUKQ6wu_2DGLTjd28MCEkFRdKqPGt6Ela-AwjUdC31qStx_qIcgibD3ZbznM40nJETODLqOWPFkJymiaQuDNEgSQsd639cenz4_rn8i45-tzi90wH3WYflPURIYfmgAWt5FsICtR3i8VQW6mq1tKph8yEnp27efCxqdxggysq9I660lv_jpIG-FINGy6Tnvtckednna4cpIl3On67JEDU_iqW1As" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=LDas7w8Grl3ayJ7xP9yfsV0-uTo20EtBR76a6W-ekdrgD92ubXFL7YrFTn_qk8wN7dt7mbYA_bb_Jw-Lqt--Myx7gKf8NOxPos1E1G5oPulZrs5FVs8mwY3J-4CrjzjwrkDiHTUyp0e3Jwo3ddrN5NS0twN9p-teRY3eyxVjhdv93Km8xfeZvQM5-QO5w-Frmfg3I2PN1hsawFGROqf9ZdLQToDBfhbidFoqcrWem7unvvQTmKZS9mAqXgIf3l5i1EHC1356zae-LxbRYWI5JEtbIPVNl85gcfrsq2JxOyvNLukdMjZ3T24HWC1M7XGgUZL9memEq8IQfKZKMFS6X2CHaMlqKcHtVI27q7Qsy7KexZQXLB38EalLbREavhNtT-Y9fRhwF-6axdTrCrPTwOpjkxQDjNEUQRIjO5iJG2SuROTUr54qU49C1dQVuxP-HU1OB1kTCEbVR4FgUKQ6wu_2DGLTjd28MCEkFRdKqPGt6Ela-AwjUdC31qStx_qIcgibD3ZbznM40nJETODLqOWPFkJymiaQuDNEgSQsd639cenz4_rn8i45-tzi90wH3WYflPURIYfmgAWt5FsICtR3i8VQW6mq1tKph8yEnp27efCxqdxggysq9I660lv_jpIG-FINGy6Tnvtckednna4cpIl3On67JEDU_iqW1As" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Skd7ItDGoJwDW552MJcww3S4meDH8CJBZP1wUmvlVQG2YsUgQzc7QNbw2UPWSS7K66Xzi7A8NjOUD2rXNKHOeIQfVzV8Cp-SGxHBFJaYLYKz5Om0othj2CKiIWnf7q_vxUKY9ggLh2eaf0JFUkbCtrmTK0XqnuzAc3U0JaX7FcZMC9f2-WXEeTEqfqKsTnLboHWMhG0-tAqGQV1gfVKx3CuVl_cehPMr8MEgUEdR2ZbqMIGhscPvKoXlvrjS74pqUIiFHF1iDUcG5fmreogzlvXBJSggD4b8Rl9A-mcdM293wFh9OBt2RUXCp_gnEJvvXLeguhJsIMBnKrD6J-bzdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=Skd7ItDGoJwDW552MJcww3S4meDH8CJBZP1wUmvlVQG2YsUgQzc7QNbw2UPWSS7K66Xzi7A8NjOUD2rXNKHOeIQfVzV8Cp-SGxHBFJaYLYKz5Om0othj2CKiIWnf7q_vxUKY9ggLh2eaf0JFUkbCtrmTK0XqnuzAc3U0JaX7FcZMC9f2-WXEeTEqfqKsTnLboHWMhG0-tAqGQV1gfVKx3CuVl_cehPMr8MEgUEdR2ZbqMIGhscPvKoXlvrjS74pqUIiFHF1iDUcG5fmreogzlvXBJSggD4b8Rl9A-mcdM293wFh9OBt2RUXCp_gnEJvvXLeguhJsIMBnKrD6J-bzdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
