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
<img src="https://cdn4.telesco.pe/file/IiwktjHCndONpWMQmVILs3yArRzo5kcY5jRWi9tZXtuIiWKdvPtwsbbjHhpz1yNQ9TfdvH_zGZlT1-kECSoX2mHVQJkFbfVsA-QgiNQCKbJovCWiqCzhnU682-710FkBaLeItKLj6Q-eKd0-cDART6ryllTXGBkauIJQqsxytB5G8ak2XVfT_MsQ4_o_07SBmyYsIVO4HwwOf0tFHg9jIq9FVZ7vPuGrV4gZwwrv1P7DkRSQGim36w55DBiW1aS0hvBJI8mj0bmPSppEhRUneW7ao1uyQHWaRyHkDRnXSu7GK8_4zDtsqullixtph6BMbSJKCDiS0WaoATp4Shxbow.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 175K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-68007">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33092f28c9.mp4?token=Y8ZCTCqwL8sx-zRKQhdE2djVjI_J5KD03svcxuP1Jm3ZOEPjGfWEe5a39QcD9s_18KTIPTsdhiVBcT6TJk49eFtqO0tEZyED-nFPuijyu3N3B-hj_arNDv54yEdryRpGu72tUhLMQIUr4ykxi3z2ojfJ7RPPlBNTsyRWbqgR2xEnRWARm3J7pfHX-z2oyjxRr4hYmxj6FbLQGzug1rkvPUeWyc0hl6aigpXwyJbeqgJkVc4Glpa6najzXksmhHeJtJjxQ6OyPgazMAh-xEot19_-TaBnNkU9vvP1637YroAINchDo9OJthLfDdNE44-Pcszp2thhVJ-46v0R5J2gD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33092f28c9.mp4?token=Y8ZCTCqwL8sx-zRKQhdE2djVjI_J5KD03svcxuP1Jm3ZOEPjGfWEe5a39QcD9s_18KTIPTsdhiVBcT6TJk49eFtqO0tEZyED-nFPuijyu3N3B-hj_arNDv54yEdryRpGu72tUhLMQIUr4ykxi3z2ojfJ7RPPlBNTsyRWbqgR2xEnRWARm3J7pfHX-z2oyjxRr4hYmxj6FbLQGzug1rkvPUeWyc0hl6aigpXwyJbeqgJkVc4Glpa6najzXksmhHeJtJjxQ6OyPgazMAh-xEot19_-TaBnNkU9vvP1637YroAINchDo9OJthLfDdNE44-Pcszp2thhVJ-46v0R5J2gD4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی اقتدار و وطن‌پرستی محمدرضا شاه پهلوی و قدرت ایران، جهان غرب را به واکنش واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/news_hut/68007" target="_blank">📅 20:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68006">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93097e540.mp4?token=kga5G73xmb7sp7wiEgraPw9g3irv1hkvp3y1t0vW4yw3NfDzjFgEDkIHQMy5L6_axAGRmxyE4hPnzJsAR5gckrCKZt7NVipulUEW16fTU0CKIHty3ZfHE3NLmdNC6TmTVC3gObDX8T7yNmYtasfPDbh8CxqQjRiX_x2LgrRS9UZ0OoWSqHk3Osy20NOWbtDGRL8khvdl38HPE9CzpF0lNA7kaMAWBJCNQk1bV_Hu7dWFcLKgAp2F7Lua7AGiF_d5M8jh-2PxZa_CyTeNk-PDiAnXj5qMGMP0f3PsQB9Ca1kX_6wHq2QRbndmzK1kj2q_GIRnrOnLc0z4Ws8jBxI_SW6Heo3gfORPa9Qq4C_C5YzsB_CDYOzb9A0Gbub8zy7OeLP9_LxGy3xU5WhWveOWTP4Jc2u4RGIY4yUA_cmsODD5Qnoi1oLpdJ98YpGLgQ0HTClELJyed7xoMvAuS2C77v2gUrHfgTb8gyYPgeCckyzG_GcTZu099OCM45RKmyCznBwxLdfqy6WSFRBadDQ1SA-HgVSeKPI0F35IN_pAiowtMGZDwN7M0cIQiaaixJ3Zqz14_nxUxWo0mSyPdzSivCtmFXsxf0tBFNyvB0zH92zL_jU0UM4_dXc2lv0NJCNkyHwJo553JjuAcLRsHvgek5ReqHF2F2ONISXn-zEO2RY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93097e540.mp4?token=kga5G73xmb7sp7wiEgraPw9g3irv1hkvp3y1t0vW4yw3NfDzjFgEDkIHQMy5L6_axAGRmxyE4hPnzJsAR5gckrCKZt7NVipulUEW16fTU0CKIHty3ZfHE3NLmdNC6TmTVC3gObDX8T7yNmYtasfPDbh8CxqQjRiX_x2LgrRS9UZ0OoWSqHk3Osy20NOWbtDGRL8khvdl38HPE9CzpF0lNA7kaMAWBJCNQk1bV_Hu7dWFcLKgAp2F7Lua7AGiF_d5M8jh-2PxZa_CyTeNk-PDiAnXj5qMGMP0f3PsQB9Ca1kX_6wHq2QRbndmzK1kj2q_GIRnrOnLc0z4Ws8jBxI_SW6Heo3gfORPa9Qq4C_C5YzsB_CDYOzb9A0Gbub8zy7OeLP9_LxGy3xU5WhWveOWTP4Jc2u4RGIY4yUA_cmsODD5Qnoi1oLpdJ98YpGLgQ0HTClELJyed7xoMvAuS2C77v2gUrHfgTb8gyYPgeCckyzG_GcTZu099OCM45RKmyCznBwxLdfqy6WSFRBadDQ1SA-HgVSeKPI0F35IN_pAiowtMGZDwN7M0cIQiaaixJ3Zqz14_nxUxWo0mSyPdzSivCtmFXsxf0tBFNyvB0zH92zL_jU0UM4_dXc2lv0NJCNkyHwJo553JjuAcLRsHvgek5ReqHF2F2ONISXn-zEO2RY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه از هیجان پایین جنگ ایران و آمریکا خسته شدین؛
پیشنهاد میکنم این شوخی معمولی پسرونه بچه‌های بلوچ رو تا آخر ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/news_hut/68006" target="_blank">📅 19:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68005">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e510433ba3.mp4?token=qWK3BvzE1fcN45xgU590fJdwSkQlgK4tTCf4_zeswMqoQ7dF-bnlVQzQKoWO1C83rTInI4j1NElcP1uchZV2p8PMmSUrG6g2BokbvRKQJf8WcwW-H1NvSWu9gBQy_IhD8pO28UxXSjy_L7gVAZe1v85F6Ilrs00v76D4JQvhpPRpKpzby7vgyq9asK8mPlCVBtKA6dWZNCD3UDG7zvxzZqS075rPn-YeM-QQL5jzvIF79Hba6802fskvojY6HZ1esNycyOR2YR_4eE2mAzfubp6_x-nsOPbzL02iFxuVsStYE2s5SYmzmxPKV199Ffnb_amBNYSO6Bvl7rF3buo2LUF78NSftg300JehK7fGMrRFGY4ewal4QuXKqE6Oa8FIPywOOKWkYSzCyZK97rhgQHaYwfZ30qnFVe45tujZZ9_s5sjROpC5YJf2nWKCqhbxkQuEIfpEaPmXSd-jQWfBfiSVkk-JWGQlTz28o7y3lGMFuH5UrXOryYe1fdzcjqMHIsJMo8gne3fvR2msSRDovMXukuXdXWiD3G8kptoU6PoMiwmdAusnM0lvgmezGLunv1QSTFHGz5jcYrQmJm1ObLaGFVqn5Dhf9T5ZS-o-J4O_gV-IJirsTOIZPGOxGxpsMkP9cS81pJTVDhcWQrmQZeL2nWiClTRhk44rAumCIRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e510433ba3.mp4?token=qWK3BvzE1fcN45xgU590fJdwSkQlgK4tTCf4_zeswMqoQ7dF-bnlVQzQKoWO1C83rTInI4j1NElcP1uchZV2p8PMmSUrG6g2BokbvRKQJf8WcwW-H1NvSWu9gBQy_IhD8pO28UxXSjy_L7gVAZe1v85F6Ilrs00v76D4JQvhpPRpKpzby7vgyq9asK8mPlCVBtKA6dWZNCD3UDG7zvxzZqS075rPn-YeM-QQL5jzvIF79Hba6802fskvojY6HZ1esNycyOR2YR_4eE2mAzfubp6_x-nsOPbzL02iFxuVsStYE2s5SYmzmxPKV199Ffnb_amBNYSO6Bvl7rF3buo2LUF78NSftg300JehK7fGMrRFGY4ewal4QuXKqE6Oa8FIPywOOKWkYSzCyZK97rhgQHaYwfZ30qnFVe45tujZZ9_s5sjROpC5YJf2nWKCqhbxkQuEIfpEaPmXSd-jQWfBfiSVkk-JWGQlTz28o7y3lGMFuH5UrXOryYe1fdzcjqMHIsJMo8gne3fvR2msSRDovMXukuXdXWiD3G8kptoU6PoMiwmdAusnM0lvgmezGLunv1QSTFHGz5jcYrQmJm1ObLaGFVqn5Dhf9T5ZS-o-J4O_gV-IJirsTOIZPGOxGxpsMkP9cS81pJTVDhcWQrmQZeL2nWiClTRhk44rAumCIRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری ۸سال پیش روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/68005" target="_blank">📅 19:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68004">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97484f7b84.mp4?token=WZyTkOD6tzYOaoOvwYGX-QkmqzxuiefZSdD_6aUTHbYW2je20JhkfPw6GEDmS4peLSjpRi4IeKlg8pdcfhEWHSR8b6HBSjUOPIesJW8GzlbKA_bn3_gBRxgQ1KGOPsICwAXUH0_oBLxh34baGTXgwOyN0_Ad4rLb0Qc4KWKHpjYdCwqYCVxLpHJC5xAlIyGI9l1sOK2b57b9UPPFbppmPe_bxuLRlFeecyD2QWy7DBdTkkKPSEm40T-FIgs_a9RyfaZ2JbUXy7ovvu2x8u-13jM_gwSS5Isp1iVDPpF-h4LnlbFU_QyH9Y3KpvodGREc0aK8bmS4jMLxk5ej2qcn_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97484f7b84.mp4?token=WZyTkOD6tzYOaoOvwYGX-QkmqzxuiefZSdD_6aUTHbYW2je20JhkfPw6GEDmS4peLSjpRi4IeKlg8pdcfhEWHSR8b6HBSjUOPIesJW8GzlbKA_bn3_gBRxgQ1KGOPsICwAXUH0_oBLxh34baGTXgwOyN0_Ad4rLb0Qc4KWKHpjYdCwqYCVxLpHJC5xAlIyGI9l1sOK2b57b9UPPFbppmPe_bxuLRlFeecyD2QWy7DBdTkkKPSEm40T-FIgs_a9RyfaZ2JbUXy7ovvu2x8u-13jM_gwSS5Isp1iVDPpF-h4LnlbFU_QyH9Y3KpvodGREc0aK8bmS4jMLxk5ej2qcn_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💪
سنتکام: برای اولین بار با استفاده از شهپاد (شناور هدایت‌پذیر از راه دور) یک تأسیسات دریایی ایران در بندرعباس را هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/68004" target="_blank">📅 18:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68003">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooJrt0MMd5i9_m6WeSlwbnZaepVIrQ5nVpvAStu1EkDYmJdb-hdlijYvy5Z9iIzHlqNK2MoYp0tqsfoK9TOMYajcKPEMgU88ESWPeCD6_Egu3HIUG9e3j1r6Tyw2h_MzBpx_vo43m0lSOq2QonhIzL3EBOFeOrSZ3LRp11i2Jd3kbPldfUQ6qeGE_HrHSmfv6Ap4tG5VKJ7i4WB6y77MR7FctgB0WzNYMK-m2lTOdP86j0x3Ui0fExFG3Q1PZ5OHrYx5yRmmO9HUjbTwEEJ3F_grzcJLI0aWY4rm69MnwGQ-EfY87RAiWPMzpcOjVxrenKb8bzFFn-z9-vvuFrG8mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ تروث سوشال:
تنگه هرمز باز است و با حضور یا بدون حضور ایران، باز خواهد ماند.
ما «محاصره ایران» را دوباره اعمال می‌کنیم؛ نامی که بدین دلیل انتخاب شده است که این اقدام صرفاً مانع از ورود یا خروج کشتی‌ها یا مشتریان ایران می‌شود.
سایر کشورها از دسترسی عادلانه و آزاد به این تنگه برخوردار خواهند بود. ایالات متحده از این پس به عنوان «حافظ تنگه هرمز» شناخته خواهد شد؛
اما در همین راستا و بر اساس اصل انصاف، بابت تمامی هزینه‌های لازم برای تأمین ایمنی و امنیت این منطقه بسیار پرالتهاب جهان، معادل ۲۰ درصد از ارزش کل محموله‌های ارسالی را به عنوان هزینه دریافت خواهد کرد.
فرایند و سازوکار اجرایی این طرح بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/68003" target="_blank">📅 17:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68002">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ترامپ دستور داد محاصره دریایی علیه ایران دوباره اعمال شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/68002" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68001">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a2b70f10.mp4?token=LrgU2S2uepTv8mhD0Jd-2qbX5RAo_fc9M8l25zDoadwBfx509CZSnlezxsu-2UmvtevOANBIlOTsw3BOsin5gsCG8-RGQuF6lN3Wd-QEDdMYwYJ6SMdOn2emBlCnS0w39f7HuPqMsJcxdlElQ1_N3sVgYCUdFFwOm6TsuVnCbhzO_nbOs-xV5O3SyjtIAIEyMbD-ABAeH8qYVHrdYZhnYz6-Zl-trke2b8oA9fJwmZM7eCP_Y7J2iLqZCvNruqJf_e_M6ECudQk6lpVvz9T9LTUx9SDTNCnw8e6CMxyjbpVjfM8OSDsPUVEehGJEfOPZYMQu5BAHWco6dY9GdTRJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a2b70f10.mp4?token=LrgU2S2uepTv8mhD0Jd-2qbX5RAo_fc9M8l25zDoadwBfx509CZSnlezxsu-2UmvtevOANBIlOTsw3BOsin5gsCG8-RGQuF6lN3Wd-QEDdMYwYJ6SMdOn2emBlCnS0w39f7HuPqMsJcxdlElQ1_N3sVgYCUdFFwOm6TsuVnCbhzO_nbOs-xV5O3SyjtIAIEyMbD-ABAeH8qYVHrdYZhnYz6-Zl-trke2b8oA9fJwmZM7eCP_Y7J2iLqZCvNruqJf_e_M6ECudQk6lpVvz9T9LTUx9SDTNCnw8e6CMxyjbpVjfM8OSDsPUVEehGJEfOPZYMQu5BAHWco6dY9GdTRJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
من سلیمانی را کشتم. سلیمانی یکی از آدم‌های واقعاً، واقعاً بد در تمام این قضایا بود. اما در کاری که می‌کرد مهارت داشت.
او ژنرال بسیار باهوشی بود. من فکر می‌کنم کشتن سلیمانی یکی از بزرگ‌ترین کارها بود.
من فکر می‌کنم اگر من با بمب‌افکن‌های B-2 حمله نکرده بودم، آن‌ها الآن سلاح هسته‌ای داشتند و در حال حاضر خاورمیانه، به شکل فعلی‌اش، دیگر وجود نداشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/68001" target="_blank">📅 17:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67999">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d51dbf16e.mp4?token=hFGW5ph4xn2NMIZ4rmiOVKDSgjsZGkDTmtxSzuTxLqvUVnht8Jsu82l0n7vJKjOEJzm7057KyQ_qwCfvKLt-abWJO2vIW1o4gFbFczgC8fVuI8tuLyAkK3UsinzpBXSc9xWw8bR0XJqTijm1ZH0CG_AQIv4y9VV458MhU1MLtZOkJax1NibhR9nVt28sW04c8Xfw5ioi4nMrQA3U-FirOoZxfjB3ryRcBuHSyWrQdhegPCSNjiHlS2GqH6eS3ZCgIZglw9m6ectay3PnCLxtPM4oEigvWVOLCoj47OdZruQ6V9N5VyEeb6h5LROeomqmDwRyjqiEXLxTAvxUnwcAXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d51dbf16e.mp4?token=hFGW5ph4xn2NMIZ4rmiOVKDSgjsZGkDTmtxSzuTxLqvUVnht8Jsu82l0n7vJKjOEJzm7057KyQ_qwCfvKLt-abWJO2vIW1o4gFbFczgC8fVuI8tuLyAkK3UsinzpBXSc9xWw8bR0XJqTijm1ZH0CG_AQIv4y9VV458MhU1MLtZOkJax1NibhR9nVt28sW04c8Xfw5ioi4nMrQA3U-FirOoZxfjB3ryRcBuHSyWrQdhegPCSNjiHlS2GqH6eS3ZCgIZglw9m6ectay3PnCLxtPM4oEigvWVOLCoj47OdZruQ6V9N5VyEeb6h5LROeomqmDwRyjqiEXLxTAvxUnwcAXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها هیچ‌چیز ندارند. هیچ نیروی دریایی ندارند، هیچ نیروی هوایی ندارند، همه‌چیز از بین رفته است. پدافند ضد هوایی‌شان نابود شده است.
رهبران‌شان همگی کشته شده‌اند. بهترین رهبران‌شان کشته شده‌اند. آن‌ها از بین رفته‌اند. خمینی کشته شده است، پسرش هم ۹۰ درصد کارش تمام است.
آن‌وقت نیویورک تایمز مقاله‌ای می‌نویسد که وضعیت آن‌ها امروز بهتر شده است... آن‌ها تورم ۳۵۰ درصدی دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67999" target="_blank">📅 17:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67998">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebd104df8.mp4?token=p5wZs0zZQ8jdFDJBjyr1mX0YziJqvQ87wBgsVZBK2fQxYAaH27CJAihtXV45Rvt6d-tt56cswMilykO1GrGqxdyOvMtlvkB5dVrU1vjq0kdYr_6BC0jveuL9Itl7j_ZLdpaAgJ4mh7bGNq22jD7eSHbokZfQcvTI8jPhSj6tbe5FbwYA79OyzLFsxXqmLGJsO0wmarTbOR5jlNTRm7l14iPqBMTi5dZpouyd2Rf0xzsEm6Eb9QffCTUkx-Huch5uaP-FYQe6v9f8KfwDRjT6sRDPdDWlEmVAfYpurdVm6YWY2VTkk9zZBixtPRzKDOln52uf4vhGhUJW3_O4_ZOq7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebd104df8.mp4?token=p5wZs0zZQ8jdFDJBjyr1mX0YziJqvQ87wBgsVZBK2fQxYAaH27CJAihtXV45Rvt6d-tt56cswMilykO1GrGqxdyOvMtlvkB5dVrU1vjq0kdYr_6BC0jveuL9Itl7j_ZLdpaAgJ4mh7bGNq22jD7eSHbokZfQcvTI8jPhSj6tbe5FbwYA79OyzLFsxXqmLGJsO0wmarTbOR5jlNTRm7l14iPqBMTi5dZpouyd2Rf0xzsEm6Eb9QffCTUkx-Huch5uaP-FYQe6v9f8KfwDRjT6sRDPdDWlEmVAfYpurdVm6YWY2VTkk9zZBixtPRzKDOln52uf4vhGhUJW3_O4_ZOq7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ایالات متحده شب گذشته ضربات سنگینی به تجهیزات آن‌ها وارد کرده و ممکن است کنترل دائمی عملیات‌های امنیتی در خاورمیانه را بر عهده بگیرد.
«بیشتر تجهیزاتشان از بین رفته است. ما دیشب ضربات بسیار سختی به سامانه‌های ضدهوایی آن‌ها وارد کردیم.
«هر بار که پهپادی می‌فرستند، ضربه سختی به آن‌ها می‌زنیم
.
«اما ما توافقی داشتیم... و آن‌ها آن را نقض کردند. آن‌ها همیشه توافق را زیر پا می‌گذارند.
بنابراین ما هم ضربات سختی به آن‌ها وارد خواهیم کرد، کنترل تنگه را حفظ می‌کنیم و احتمالاً خودمان اداره امور را در دست می‌گیریم
.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67998" target="_blank">📅 17:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67997">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060cc64d0d.mp4?token=tWNf8LBDIfTsy7nYotGM9xutzXZgCZdydQCAZEKA5LcFTAJpiotcnHsGHNXvX28RzT78TIsdqI4guVwc8syWIzjSWhlEuw8SZX4M14K6a-UfT2QC5E5uj82t9rAQJrLl56eU5EMsBisn7TcuBi0Jc98aPK8WcrNYd0U3acG88s7G84-ZBp28CUlHysJ0gbS14c7dChRu77_tC14bduNQZv5YTViO6Ohk0pOFXuWLavfCWqutQmut78fFQU0mZ3aXXJXVYlUtWItZYPwbdWIyhrflq8-Cre_TVHls9hPQf80EtZD--5Tyc8wOKHmU6RpA_zt4JZpfu5AdD09yPrV8IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060cc64d0d.mp4?token=tWNf8LBDIfTsy7nYotGM9xutzXZgCZdydQCAZEKA5LcFTAJpiotcnHsGHNXvX28RzT78TIsdqI4guVwc8syWIzjSWhlEuw8SZX4M14K6a-UfT2QC5E5uj82t9rAQJrLl56eU5EMsBisn7TcuBi0Jc98aPK8WcrNYd0U3acG88s7G84-ZBp28CUlHysJ0gbS14c7dChRu77_tC14bduNQZv5YTViO6Ohk0pOFXuWLavfCWqutQmut78fFQU0mZ3aXXJXVYlUtWItZYPwbdWIyhrflq8-Cre_TVHls9hPQf80EtZD--5Tyc8wOKHmU6RpA_zt4JZpfu5AdD09yPrV8IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
🇬🇧
دولت بریتانیا رسما سپاه پاسداران انقلاب اسلامی(IRGC) رو در فهرست سازمان‌های تروریستی قرار داد.
در حال حاضر، ایالات متحده، اتحادیه اروپا، بریتانیا، کانادا و استرالیا سپاه پاسداران را به عنوان سازمان تروریستی ثبت کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67997" target="_blank">📅 17:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67996">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4923d848c0.mp4?token=G1Xe-VyJGFbPffAg7TOumyhPMYXxO3JI5zbs1Ruwb1a6VTPoBuhhQfG5Pzjquqk3JgimQAuxrcxgGLfoaUseoo0tZDsAb92LEXC6ZtpV6EBiiasd6isnIWnuyJwA_wEx-j8x_1VkZJhYceM-zgMwWCsA7GJzZgNRaHUVnSsC3y2AHc74yzOU1cU9X5ExeLHjaXiCi8XxOtMldPgtkv8IJA2g5L9ZcZiah-y63J4aBBSyGlZfK81P5sLNG8tfvGvtazSwozYxbyN_WKRI_-yDQAijC2PFuCHulnLz7__RPtWJa0SFG5Y-xiqjTwC-gUcxgx_l6nlvdgcIHdddJDAimg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4923d848c0.mp4?token=G1Xe-VyJGFbPffAg7TOumyhPMYXxO3JI5zbs1Ruwb1a6VTPoBuhhQfG5Pzjquqk3JgimQAuxrcxgGLfoaUseoo0tZDsAb92LEXC6ZtpV6EBiiasd6isnIWnuyJwA_wEx-j8x_1VkZJhYceM-zgMwWCsA7GJzZgNRaHUVnSsC3y2AHc74yzOU1cU9X5ExeLHjaXiCi8XxOtMldPgtkv8IJA2g5L9ZcZiah-y63J4aBBSyGlZfK81P5sLNG8tfvGvtazSwozYxbyN_WKRI_-yDQAijC2PFuCHulnLz7__RPtWJa0SFG5Y-xiqjTwC-gUcxgx_l6nlvdgcIHdddJDAimg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند
:
اونجا وقت برا دوش گرفتن هم بهمون نمیدادن.
از بس بهمون سخت گذشت که تعداد زیادی از بچه ها شورتشون اونجا موند.
مثلا من خودم شورتم جا مونده آمریکا.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67996" target="_blank">📅 17:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67995">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b88bf07.mp4?token=Yzuy-74qYP957UiM7OqRxXnO19rdYFfODMZMFXJv3na7nlpnlQ7JjT57c8zbXCb-VGG4F6DO2icqnj1Bv7UAFAfM5YFGptPf8jXW8eB8-VVJOFPqOM1NVY7zUyY61cYrJPHP8uv6LOhtA_6cxBW-hNIPNDC6hKgPJBeJZ6L-eeVIL0nZ4JVheUmYFjYk5iOQq5t6Wn85MJKTcjPUeNI4VAD8EN3SSMLuSXCeBGl_hN_w6CqW13Jfu6oths9bAWggh0R6gEhNhq98mvCLeNFqQUxdniLLYc0Ndbt0GyMtDjROXI36O7P-212KGOvFm_nnATvSXX_tQts8OmtYdt4kKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b88bf07.mp4?token=Yzuy-74qYP957UiM7OqRxXnO19rdYFfODMZMFXJv3na7nlpnlQ7JjT57c8zbXCb-VGG4F6DO2icqnj1Bv7UAFAfM5YFGptPf8jXW8eB8-VVJOFPqOM1NVY7zUyY61cYrJPHP8uv6LOhtA_6cxBW-hNIPNDC6hKgPJBeJZ6L-eeVIL0nZ4JVheUmYFjYk5iOQq5t6Wn85MJKTcjPUeNI4VAD8EN3SSMLuSXCeBGl_hN_w6CqW13Jfu6oths9bAWggh0R6gEhNhq98mvCLeNFqQUxdniLLYc0Ndbt0GyMtDjROXI36O7P-212KGOvFm_nnATvSXX_tQts8OmtYdt4kKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه ویدیو ای از حملات موشکی بامداد امروز به پایگاه های آمریکا در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67995" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67994">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8627adc5f4.mp4?token=GeS4Dt_rEdKzJsAnARbKOZg79rlFazfpA53Cds_asgmd8h0-HeNEitejQUMRieHc5o9sHLtBwEGsmHr1OzMKlqjAYECwX1ABETjUz9DTIoMptHe86mu-Htjf52KUjgayWRg5V4-UuOSfZaNoOksKNQemojX4nTXqHA7pOpvTS1MxGra53DdNFttlh2KTNFbvLHigItvksg1yGUt7nSzM6tPrNmJFUZtRqGnQzwddYNPPYDj4tjNJtROvzGTm_c_TdUfauYtvc2vimoPv33SK8a_TBmntVmaYUxVluUTIwaeGjCRI1UFexRSAejopDAoT5iwX1PEDvVmcMrrVzmuqvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8627adc5f4.mp4?token=GeS4Dt_rEdKzJsAnARbKOZg79rlFazfpA53Cds_asgmd8h0-HeNEitejQUMRieHc5o9sHLtBwEGsmHr1OzMKlqjAYECwX1ABETjUz9DTIoMptHe86mu-Htjf52KUjgayWRg5V4-UuOSfZaNoOksKNQemojX4nTXqHA7pOpvTS1MxGra53DdNFttlh2KTNFbvLHigItvksg1yGUt7nSzM6tPrNmJFUZtRqGnQzwddYNPPYDj4tjNJtROvzGTm_c_TdUfauYtvc2vimoPv33SK8a_TBmntVmaYUxVluUTIwaeGjCRI1UFexRSAejopDAoT5iwX1PEDvVmcMrrVzmuqvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لیندسی گراهام، دوست وفادار ملت آزادی‌خواه ایران
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67994" target="_blank">📅 15:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67993">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a38d8e8e.mp4?token=K_mg-Bfw2HGFYq6Zu4jgonQqrtPCWLku633aTV37lpfTLev_1jcHISUNHamkeCKv1MOujl-wiX6O9PwnInEv7z-ftmVFegPqMkfotKv2Gl2ifAz6bg0GA_FzvjaqoWT8-GUYWxQlOmAR4qssI6O0qMsWBz5EU5Aj_t_88S2ype7krXRi7dUpDGz1indSlVYej2Alv2x8YvAocDaaL6Qjshza3lNNrpZXSxNh6cFsoh4vzTzGXPDfZw2azwQ8Yk_WtT6dBKNqLichD45CNbKOS5HSjQIl4q82z4agBMl6MKr5vK9LeVr_ZyytquA9mVahRZ3vQ2N1rx9I0pZo_SSkHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a38d8e8e.mp4?token=K_mg-Bfw2HGFYq6Zu4jgonQqrtPCWLku633aTV37lpfTLev_1jcHISUNHamkeCKv1MOujl-wiX6O9PwnInEv7z-ftmVFegPqMkfotKv2Gl2ifAz6bg0GA_FzvjaqoWT8-GUYWxQlOmAR4qssI6O0qMsWBz5EU5Aj_t_88S2ype7krXRi7dUpDGz1indSlVYej2Alv2x8YvAocDaaL6Qjshza3lNNrpZXSxNh6cFsoh4vzTzGXPDfZw2azwQ8Yk_WtT6dBKNqLichD45CNbKOS5HSjQIl4q82z4agBMl6MKr5vK9LeVr_ZyytquA9mVahRZ3vQ2N1rx9I0pZo_SSkHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇺🇸
سنتکام ویدیو‌ ای از حملات دیشب ارتش آمریکا به اهداف نظامی جمهوری اسلامی منتشر کرد.
در این عملیات سامانه‌های پدافندی، رادارهای ساحلی، توان موشکی و پهپادی و شناورهای نظامی هدف قرار گرفتند
.
همچنین برای نخستین بار از پهپادهای انتحاری دریایی استفاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67993" target="_blank">📅 14:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67992">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3c5be180.mp4?token=a5bPe4AhiUI2yvLBIdZFxBo5twJX_px6H4lbQipzwkzU0gWB_zi7mqcrnVgLDbk29wvV5SVrHw0zXt43tu7nz-iDEkuQwqJmLFs2FP4ZKuB8w2wg7JN5S4uQozNo_pVG-yhYUUjI7I0v5t2U_-H6WB6bai3_oPq3wsv8b6OIyWm4rmqtnda6I4Cf36AhcW-WnJODZUopWOuyER-UkfYOetPwlKWkUVN75v4mY1rTTeddtIGdmVnvbWqCKKAKaBW67WtDtK34Lnb59LXd1qZ1Naa32d2KslsRgWl0By28oMKlrVt5vLcSOR3OF-VbpYmoBWu2vdgzlsiPi1oFIc-DkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3c5be180.mp4?token=a5bPe4AhiUI2yvLBIdZFxBo5twJX_px6H4lbQipzwkzU0gWB_zi7mqcrnVgLDbk29wvV5SVrHw0zXt43tu7nz-iDEkuQwqJmLFs2FP4ZKuB8w2wg7JN5S4uQozNo_pVG-yhYUUjI7I0v5t2U_-H6WB6bai3_oPq3wsv8b6OIyWm4rmqtnda6I4Cf36AhcW-WnJODZUopWOuyER-UkfYOetPwlKWkUVN75v4mY1rTTeddtIGdmVnvbWqCKKAKaBW67WtDtK34Lnb59LXd1qZ1Naa32d2KslsRgWl0By28oMKlrVt5vLcSOR3OF-VbpYmoBWu2vdgzlsiPi1oFIc-DkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تازه‌ترین ویدئو از حمله هوایی به فرودگاه صنعا
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67992" target="_blank">📅 14:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67991">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbYr0IKYL8l-zp0C9RSDh8ZELAE0N_eAdDFkMSoz711-okHflwgTdzk7ViJuOvNqlPNJdRkzrJDen-VdAoGh7yeIFYXcvRB-d4-rPKuEbHTRr_Kn0IshdgVWVJeWrX9-3TF9AkfFvCDsLewLKiFuDSGN1DuXgYdQf7DqR3F2ygVjuCYefCm_KCEhcMmXj4-LnEvCQKpkyu27HXLgFg2Bh2J0b3L20A_skI1DF3ARuSLr7PGdmKErFcwEJkje2S1L8qAXaya1aa8PXv57u0bbozrIVLg7cO4OMqNmINCnz7tDqT11fNdeaq-9Fg9jpijWu9vB5KtMjvGtQ6f40mybDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
هواپیما جمهوری اسلامی داشت میرفت سمت فرودگاه صنعا، این فرودگاه بلافاصله توسط جنگنده های عربستانی بمباران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67991" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67990">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsuLfZ12zNeQhTpgMU_OGRsAvW8sNGaZ7OtYBb7YfNWAlNNMzkRSMMBq024J8TFpJ8Mpnm_rUTsXGZR3Ru1jF54axGnvNoOIokgkL8eCs9r2HZw-ChKu9GnnAQ8EHfQlJ9z23oiiSHaHY9hb9UOMGgUpKE09XD8q9SDjKIP1PjNHL0eDon0gMxw6CF8Ijw7Zdpvjj7FanUN_AUS0va0v68NpYm_T7fi4HfO3VFkuUWPthpKH7p0SzjeimrAY_hmrDE4Q1p752urlFmQDj8aeToaFqAhoyLtiTLa1qJm_SMFTcL-xd5MCidHv5dD1qMF4ZPa5S5oshSSCTjXMo0d8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی، خواننده وآهنگساز ایرانی، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
جاستین بیبر، شکیرا، مدونا و گروه بی‌تی‌اس در این اجرا حضور خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67990" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67989">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gui1c7A-sQqyB81MPbEncYkeeG23LYJSwZ0avX06LMC49XVA8SGDglFSVLJLO4D3iyQ4HCqwnWi6uoMfjr7uJu8wpmIm1wuo84U_Z_MncUNoKGMsDnngnyIBLWPwI2whM1rzKmza6HIOd3akqzUfpYexv1F_QAeU9nm9r3FkswN2u3fp4fyGV1hJ67TvYMy1dz90tRez86vWRXMgRZdf-4Y09M-zxtJU1fadlF2azTGDIE9J_4odr_8IHKqaDTArsMrAq3ccDLYGoPQM8aBMVU6KyGv5O54e3FXC_GnDkeiQEb9yqTjZ05S9gPFrZXoIlXFJ0UHdQFscOz6pSpwntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های داخلی وابسته حکومت این لیست ترور رو منتشر کردن و نوشتن لیندزی گراهام اولیش بود تا نفر آخر بی‌خیال نمی‌شیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67989" target="_blank">📅 13:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67988">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
تنگه هرمز دعوا شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67988" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67987">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7891d1b9.mp4?token=MxHBDEqVNSGDNIMyXdltAt-A_oERz96Te3cfw65FGxZjQkz6-by62V2Vjdwhe62y4EZWBfR_PSBgBA3JPUDBixuQdjy0o0FdqUO105VcbvaIVgNHONlb9TFKkGIqS_LySv7kMpgtsDgBbJTK46j7qmpOv-yp9HsErlMPdNLZNX01Shn58dgSthRAuaYEw8ccc5tVRjBmxwyPJRyvfr6TyzNFFkkxPBXcQKkHFDr0_HOEumEzqyxS1bMZKVeZNnxC_wfcGWyQm6aDqE9pFEINV28DCYAgD0bt9IF-h_rTHdBX2Vy_fmc8n88A-I4nDQvRyCnROxnENPGBRiRzCgjlCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7891d1b9.mp4?token=MxHBDEqVNSGDNIMyXdltAt-A_oERz96Te3cfw65FGxZjQkz6-by62V2Vjdwhe62y4EZWBfR_PSBgBA3JPUDBixuQdjy0o0FdqUO105VcbvaIVgNHONlb9TFKkGIqS_LySv7kMpgtsDgBbJTK46j7qmpOv-yp9HsErlMPdNLZNX01Shn58dgSthRAuaYEw8ccc5tVRjBmxwyPJRyvfr6TyzNFFkkxPBXcQKkHFDr0_HOEumEzqyxS1bMZKVeZNnxC_wfcGWyQm6aDqE9pFEINV28DCYAgD0bt9IF-h_rTHdBX2Vy_fmc8n88A-I4nDQvRyCnROxnENPGBRiRzCgjlCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:با درخواست گروسی برای بازدید از تاسیسات هسته‌ای موافقت میکنید؟
🔴
بقایی:خیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67987" target="_blank">📅 12:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67986">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67986" target="_blank">📅 12:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67985">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=GUAexAA7iMNVwRp2I3RZDLcDMPq_jm3N0hSF7qoCKGbADcLiYzNt9G7fb05U_NxC5K2-7ne1HwMTBXtl5ZoV2INJGN9LFiKaYyp6YPZj7ci9l1JuiItLOXmDPHgIWr1TqtCIoOU3lpRkopIHNraCOXKI-tOFNUywDpqt3W3Wn94ojatUuhr-HSsELZGMRvKBf5sPYGcItR3vBWGT1BxolbJhKkRKSMmEdrKE0okYaYDI_GphKv7DStN9Zg3jABVJ_Cs1qF8seKrDlRoHGPXbyIS8_vdmETfNfvFo2xMruFj_7D_eq012Rv99XDKl4mpscZa224QV_JlkVzu1V_f7Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=GUAexAA7iMNVwRp2I3RZDLcDMPq_jm3N0hSF7qoCKGbADcLiYzNt9G7fb05U_NxC5K2-7ne1HwMTBXtl5ZoV2INJGN9LFiKaYyp6YPZj7ci9l1JuiItLOXmDPHgIWr1TqtCIoOU3lpRkopIHNraCOXKI-tOFNUywDpqt3W3Wn94ojatUuhr-HSsELZGMRvKBf5sPYGcItR3vBWGT1BxolbJhKkRKSMmEdrKE0okYaYDI_GphKv7DStN9Zg3jABVJ_Cs1qF8seKrDlRoHGPXbyIS8_vdmETfNfvFo2xMruFj_7D_eq012Rv99XDKl4mpscZa224QV_JlkVzu1V_f7Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
ایالات متحده مسئولیت مستقیم تحولات اخیر در تنگه هرمز را بر عهده دارد. آمریکایی‌ها از همان روز نخست زیر قول خود زدند؛ آن‌ها تلاش می‌کنند مسیر امنِ هماهنگ‌شده با ایران را دور بزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67985" target="_blank">📅 12:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67984">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ae996e.mp4?token=ZSZrnnmNjZzDC-cMCeLRHISwqtbzxfHf5JtryzwOkKNumMHio1-ZPrfjSpoaf332JdVn1k0GSZyH7NTAHzea0tkNl6yEArY12qmtc1mJqinNq1IrcV-TubIMnsVCh-S5AMqUb4hzkkIi6B11EdlOX3E9Yn8fg7-y26xQB7RYs99kydTIbab98nGSdumRzxF551zkkcMz01_xHVLZMz4GznoCGN14hu9PisMUqgW0ghf5UrvPsnq1RP9LMRzZnpkL3WlnsRAYUOfgGHgiFzK9Hu0Zpsl3pROcMo5HKVR-XEeXJlB_UQEdPD0Nc6xnpLJUcVUIGI1U9bGfcdUM35UgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ae996e.mp4?token=ZSZrnnmNjZzDC-cMCeLRHISwqtbzxfHf5JtryzwOkKNumMHio1-ZPrfjSpoaf332JdVn1k0GSZyH7NTAHzea0tkNl6yEArY12qmtc1mJqinNq1IrcV-TubIMnsVCh-S5AMqUb4hzkkIi6B11EdlOX3E9Yn8fg7-y26xQB7RYs99kydTIbab98nGSdumRzxF551zkkcMz01_xHVLZMz4GznoCGN14hu9PisMUqgW0ghf5UrvPsnq1RP9LMRzZnpkL3WlnsRAYUOfgGHgiFzK9Hu0Zpsl3pROcMo5HKVR-XEeXJlB_UQEdPD0Nc6xnpLJUcVUIGI1U9bGfcdUM35UgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
پیگیری عدالت برای رهبر شهید، یک اصل جدی و مطالبه‌ای همگانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67984" target="_blank">📅 12:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67983">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=cNOtLSSLN2dQ7qbi3_qWcVqUpZlkc_04oUTG-D_UKkc7du7_57HJiwGrC0SxBXHlMNS9x9oJUiHDuvDUnFwX5D9KI0Y2i5Tg_DwF4H2DkQXsd4U9lpZLXY6Y4PhrfTzm4c0P835K9ZeOQzQLzzY9r1euEbfW4KkX-aLHOt4OnUqZa0omr4MEH7KcskTmsCffTTiBXnFRVVP-ZsjVshpGbeZZjnFDQqCT0k_Rae0i18DoI9UHq41-onTJM3SQ2He5yc5VaMA80pGucmzf2-yDt_oJ4Ab4PJUwp00O4UkC33ELoG4hBCA4mVA7zIidmLAXI7RKXwUMUG9tjyQ6v289Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=cNOtLSSLN2dQ7qbi3_qWcVqUpZlkc_04oUTG-D_UKkc7du7_57HJiwGrC0SxBXHlMNS9x9oJUiHDuvDUnFwX5D9KI0Y2i5Tg_DwF4H2DkQXsd4U9lpZLXY6Y4PhrfTzm4c0P835K9ZeOQzQLzzY9r1euEbfW4KkX-aLHOt4OnUqZa0omr4MEH7KcskTmsCffTTiBXnFRVVP-ZsjVshpGbeZZjnFDQqCT0k_Rae0i18DoI9UHq41-onTJM3SQ2He5yc5VaMA80pGucmzf2-yDt_oJ4Ab4PJUwp00O4UkC33ELoG4hBCA4mVA7zIidmLAXI7RKXwUMUG9tjyQ6v289Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای آمریکایی با استفاده از مهمات سنگرشکن، یک تأسیسات موشکی زیرزمینی در پایگاه چهارم شکاری تاکتیکی ایران در نزدیکی دزفول را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67983" target="_blank">📅 11:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67982">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L44TAiIx4tkWbciUhdwDK_1KLX3fw3pyPk1iGrm2JBQoO5Dal4At4dHFEvtl3J1Nax5O-QRiCiUgEKZeiFuSyBD-769EA1V3XLXo0W--XmmMOiTv9fEMoB88YaapmJqF3lGcC9FCawDPdXYg28lVUE_FmdAIfeXx5lEeQDEyvdERTA-KWLfwA7ttX2kace6VlrVNkC2nahFR7kdPGyGWdOi1FM-pVmU_ysw_qGBbOCNG-rv-CHDdtQP6Bngl7skYB5BbO09y0XX5dupv-Yr-5NxllG-dQuEtmyOZv04Tc6S2iy4h0O3QDrMYiQdusaEU4udCRPgzfINsQin1z4FDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ در تروث سوشال تصویری از لیندسی گراهام منتشر کرده با کلاه معروف:
Make Iran Great Again
ایران را دوباره با عظمت کن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67982" target="_blank">📅 11:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67980">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxJEnzy5-yglCQ8h8BBTM8K8esS4_wx5WOnNx0VqQM3jW0pbIYA85PdKTgOHJ8fu8Dx8K15QLOqEipyg1bGDfvczBFxXUo2mo0Sk0RWrsZ3zJ8vRHXGRnVplwCoXc_qENzcNID7ErJsIad-K8R9AoSrMYk7-nOi2luouC40Es-wtsxdF4g1BghJwOnQmFnZTdQpWqigygY7zCFJzuUSWjvSdjl7Qz_BJFFhGVLxAsKXMmoV5oHHmR6QlVGQL1PeVobM293upD2S7UIE5rmozBGEN4wXITXKdzQC8CRqAr4y1Gdgn4_EmEjpj9iv7Xu_FoszlRpadGvbXYvoDTanB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnvUIDR0Qf-YKD6wiV9319BpYJ_FEV2vHy845f0nX7p_7Ng7XY9ZPRwTu8EiLbtzLrtg5pPo8AE-xQKS7CeA4YuAbFaSmDjU0UWUy3KOsSN9U6FT1R-dZIGg1dZYsjNSVKIdDWzaiCCdFkt4sPT_hXH9s8Lt1gL4ZWw3lf1r6p5XwSofyBX21U90A1Tk_y5vbRrFaB9rl8_8MutZp6WjuWcFZlJlkhiVfHRQmzhK8WieDrUe4PFGwNbepy0N7P7H_9GNb6GZj7t2aF8B9_7LHj5zoBRAA_Xp0uv-c9Hgl5mFkZ_q--6t7wr1q87tWyQhjXn4iMD0_Kj9JXl77t4OEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
انهدام پهپاد انتحاری لوکاس آمریکایی توسط پدافند رژیم در بندرعباس.
آمریکا در بامداد امروز برخی مواضع نظامی جمهوری اسلامی را با پهپاد لوکاس هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67980" target="_blank">📅 10:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67979">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddd337574.mp4?token=gEhOzwsU_49Wm1QtSclTtHGpQ4LBbuQFIpNKM0kD-jDoeYO68TXwMhgmtABH6WNL6FyajmaS0tHjpQPzmShoUyM925ejrIny8s9X8JC9v82Z4UI0xHtzHR0riCTHDXP-IOtJJJ8u6SzYR6f8DBUtBeORpI6tKP128JgVAJs8gd7SCfpgaTtE_aIrXO4XWZvDyjI9Z_oYIfRewjz3zTnd7HIhbd9AK-b33pvxh50k3T4rgeP8FF1Phhdp-8fa0gqfGtXBAPFB_wafwJCBWtll5DXSKLRtxN0YpKhb6KgjvzWIzyFcg5J7X_g8OmjzNRC2_-SrQ5gaXJ5QrWjVMzM2FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddd337574.mp4?token=gEhOzwsU_49Wm1QtSclTtHGpQ4LBbuQFIpNKM0kD-jDoeYO68TXwMhgmtABH6WNL6FyajmaS0tHjpQPzmShoUyM925ejrIny8s9X8JC9v82Z4UI0xHtzHR0riCTHDXP-IOtJJJ8u6SzYR6f8DBUtBeORpI6tKP128JgVAJs8gd7SCfpgaTtE_aIrXO4XWZvDyjI9Z_oYIfRewjz3zTnd7HIhbd9AK-b33pvxh50k3T4rgeP8FF1Phhdp-8fa0gqfGtXBAPFB_wafwJCBWtll5DXSKLRtxN0YpKhb6KgjvzWIzyFcg5J7X_g8OmjzNRC2_-SrQ5gaXJ5QrWjVMzM2FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید شاه
👑
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67979" target="_blank">📅 10:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67978">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5afa19317.mp4?token=ptTvVMcu1MNaZ7cGnABlX6RPkaXbnysKC1aZ22Q5MDqyjfP-4h2OgPF8JxF5Gtc4qSuGD7VjXFtS_I0YyoAIUQcZVoevgdHBP2nZozQnxq2flQ0WZXKx63RNnK4U2QAZB48g_v8OFXig5g81SPMqw8vuxqxPjGfq45aTo4T3dZZ2xbvb8RPP4UwKakMmpGun5F7R9bMOA0V38XLrd1dSvytnoj8YccD-3Znyy4ga_ToQUBhrD4lPDGp_e8swgodfzhoG2g8OCrN-S4A0Hon-OkfY6tL39iJwXuXTb118CjnZNCTFKjz95OuKJyLXW2G-barebq772kFv5dr2i0vXtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5afa19317.mp4?token=ptTvVMcu1MNaZ7cGnABlX6RPkaXbnysKC1aZ22Q5MDqyjfP-4h2OgPF8JxF5Gtc4qSuGD7VjXFtS_I0YyoAIUQcZVoevgdHBP2nZozQnxq2flQ0WZXKx63RNnK4U2QAZB48g_v8OFXig5g81SPMqw8vuxqxPjGfq45aTo4T3dZZ2xbvb8RPP4UwKakMmpGun5F7R9bMOA0V38XLrd1dSvytnoj8YccD-3Znyy4ga_ToQUBhrD4lPDGp_e8swgodfzhoG2g8OCrN-S4A0Hon-OkfY6tL39iJwXuXTb118CjnZNCTFKjz95OuKJyLXW2G-barebq772kFv5dr2i0vXtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستتو اینجوری کن
🫴🏻
لباتو لوله
😢
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67978" target="_blank">📅 09:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67977">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b2083eb1.mp4?token=EZ1joQPmkCTyx1hHv73CR5--19Dkddn5QLMc7trpMESV9S7TN-UWQdRTpgWZhXE9s4_HGLTAHHV5lJht0kE2qMB4uNAEFy2kMnH5HIy4MrC5hNYyga8H4ITkB33RfStVNIqWTy7MRNEQeXIahyYOs0RDt_en1M_quNNPfvY5CeGssfbYScHUPWQK2SWV1kxiY8H-x0jT49TKORJSsY7HGWMnri0HyweAE1_7WNqA4eZhstwErGWUWSbnUbIFBvTTBUVi0WXoY9v9S63xsRj2PAVGU30f5Sn0VoVR0qQkf7Hj12H_WHAXLTgrSXFHOTYqVtVD3RT5mxdLan5NyPOy9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b2083eb1.mp4?token=EZ1joQPmkCTyx1hHv73CR5--19Dkddn5QLMc7trpMESV9S7TN-UWQdRTpgWZhXE9s4_HGLTAHHV5lJht0kE2qMB4uNAEFy2kMnH5HIy4MrC5hNYyga8H4ITkB33RfStVNIqWTy7MRNEQeXIahyYOs0RDt_en1M_quNNPfvY5CeGssfbYScHUPWQK2SWV1kxiY8H-x0jT49TKORJSsY7HGWMnri0HyweAE1_7WNqA4eZhstwErGWUWSbnUbIFBvTTBUVi0WXoY9v9S63xsRj2PAVGU30f5Sn0VoVR0qQkf7Hj12H_WHAXLTgrSXFHOTYqVtVD3RT5mxdLan5NyPOy9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پهپادهای شاهد سپاه درحال حرکت به سوی پایگاه‌های آمریکایی در حوزه خلیج‌فارس
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67977" target="_blank">📅 08:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67976">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش‌ها از آغاز موج جدید حملات سپاه به پایگاه‌های آمریکایی در کشورهای عربی  @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67976" target="_blank">📅 08:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67975">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش‌ها از آغاز موج جدید حملات سپاه به پایگاه‌های آمریکایی در کشورهای عربی
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67975" target="_blank">📅 08:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67974">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👌🏼
تنها
#سایت
با بونوس های واقعی
😮
به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
✅
نصب اپلیکیشن بدون فیلتر
🚫</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67974" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67973">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCunL8YRMKH5B13HM0FBSMARKq8n9gSmjNHlQi_cw-LZ6gSDL8QeA19KgPrUckgxcRQnsu27pfCZJJ1TUailVKPWibb0K06NMn6DOF33LoiB9t528vywAV3P64MUd4IlL4_gzI-t1VAgVfCLJlWnjqbo3IIymVf9Fswf3wUjo7szrv5YlSdcm61RQPi-0uLZ4dInzLr9euDIYQMKxM3PD3h4x0079WnIxuRZIwSp9taZS-4j6mHjVOcg0vDcS-MWtldXPqF2-nni29CAo3XBlJj3v2NRMPGjJQ3-KU_ZAwsWN4snzlOyrpz6XyBm2eLAWWSH2orDY24DhJTeOP9z9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هر
1,000,000
شارژ مساوی با 1,200,000 شارژ در سایت بدون قیدو شرط
💖
💵
هر بار حسابتو شارژ کنی
0️⃣
2️⃣
🅰️
شارژ اضافی میگیری بدون محدودیت
🔴
اگر هم باخت بدی همون لحظه
0️⃣
2️⃣
درصد  مبلغ باخت به حسابت برمیگرده.
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a22
@betinjabet</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67973" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67972">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1a4493a9.mov?token=V9cdKmeYoFG-2U5-CLQkmbh0IHvvNBZTF1aWpXomGYoV4_nh9qGQN8lkAs_4dFBxjHT2aOuNI3GsmzZpUgPH4hVygpY93HQ3Iivw67Pus-yAohEgtzxWsPQ6WCO8Me4Li6XRlbWRxfPTUf54DIy6tATTL-78YGSoPyiP6YiVvW1daqyuGamnX8Kjh1vof0fqYvkcM9YQWw4-W1dvKZq2wIW0TzVRnWn-WVI-TUCLRUS-OboA3gHeOx-7m6WHFnmoA8KVJZ_E7aGl8tni_5lf0HDuQyltl7vDxwQ_PoXvJ7VSsZcI66MC1wC0QqI-YTvCvGnQHZCFpf5BN7L_9MF3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1a4493a9.mov?token=V9cdKmeYoFG-2U5-CLQkmbh0IHvvNBZTF1aWpXomGYoV4_nh9qGQN8lkAs_4dFBxjHT2aOuNI3GsmzZpUgPH4hVygpY93HQ3Iivw67Pus-yAohEgtzxWsPQ6WCO8Me4Li6XRlbWRxfPTUf54DIy6tATTL-78YGSoPyiP6YiVvW1daqyuGamnX8Kjh1vof0fqYvkcM9YQWw4-W1dvKZq2wIW0TzVRnWn-WVI-TUCLRUS-OboA3gHeOx-7m6WHFnmoA8KVJZ_E7aGl8tni_5lf0HDuQyltl7vDxwQ_PoXvJ7VSsZcI66MC1wC0QqI-YTvCvGnQHZCFpf5BN7L_9MF3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتسب به اهواز بعد از حملات ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67972" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67971">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
نیویورک تایمز:
مقام آمریکایی گفت که انتظار دارد موج بزرگ‌تری از حملات آمریکا علیه اهداف نظامی ایران در یکشنبه شب (به‌وقت آمریکا) نسبت به حملات اوایل همان روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67971" target="_blank">📅 02:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67970">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فارس:
دقایقی پیش چهار نقطه در شهرستان‌های امیدیه و ماهشهر مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67970" target="_blank">📅 02:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67969">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
دزفول رو چندین بار سنگین زدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67969" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67968">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67968" target="_blank">📅 02:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67967">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=N3Cxc0V0F3mt9GQLgvOXqd6LAD-syNKC7ixac0m4AgQPmhLs4LUG_q1SmRzEw9T00Qtc9eu3cEY7bsJPlZeZmJs-P6kDjtZC3AiKFQdVrqnBccmzytYN6B4U1BccFbKPacNlRDJOxzU_gNfscyK8fq_2G5WKjVjomQooU9pI8Wg45AZmBFLmu-iMwI0Ujp2oe28LGqebOhpMhr8d4WIXbTs4tJsd7o6iThyqsjU0lgueDoWCoiZLXeF-EX-To-10muVpTic4S08AdnBShTGdf6D-cMbW2scernKaJWwo9h2bKTPKDN8H79M_b_O38UWIiF5HaZusGMisB6dKJUspLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=N3Cxc0V0F3mt9GQLgvOXqd6LAD-syNKC7ixac0m4AgQPmhLs4LUG_q1SmRzEw9T00Qtc9eu3cEY7bsJPlZeZmJs-P6kDjtZC3AiKFQdVrqnBccmzytYN6B4U1BccFbKPacNlRDJOxzU_gNfscyK8fq_2G5WKjVjomQooU9pI8Wg45AZmBFLmu-iMwI0Ujp2oe28LGqebOhpMhr8d4WIXbTs4tJsd7o6iThyqsjU0lgueDoWCoiZLXeF-EX-To-10muVpTic4S08AdnBShTGdf6D-cMbW2scernKaJWwo9h2bKTPKDN8H79M_b_O38UWIiF5HaZusGMisB6dKJUspLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال شدن پدافند در کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67967" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67966">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=VC-FLQtwUNvjfEWO6fC8Xvw1ZJ7TUPwYgoqsGGxn9W9zGqw7LFgvZV0kUS6ozYQKeKsjDtYm2NUTVeVeTOky8JZRoIKO9EmXvz2QYoT5NxqViofR8jOY_uwF8AdngBobFzYumBrFhzIpVETURKQG1LLRgou67Ea4ZgpMNZCMqDuhrgEB3Z0tX4Y2nVX1CeG8zZ06BUMowEEG-MxWOPl09VoW4K-bJT26RavAfYHEDhguV8RYRx24Fg_z-xHqoYi4vM40nEoDthxCKgXIIQVGT0RV-8zpCIsjXhuiRqvC40gaFAIPMbqp-J3PWekoTIZXbnsE96ltN3uwiEoKNXysng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=VC-FLQtwUNvjfEWO6fC8Xvw1ZJ7TUPwYgoqsGGxn9W9zGqw7LFgvZV0kUS6ozYQKeKsjDtYm2NUTVeVeTOky8JZRoIKO9EmXvz2QYoT5NxqViofR8jOY_uwF8AdngBobFzYumBrFhzIpVETURKQG1LLRgou67Ea4ZgpMNZCMqDuhrgEB3Z0tX4Y2nVX1CeG8zZ06BUMowEEG-MxWOPl09VoW4K-bJT26RavAfYHEDhguV8RYRx24Fg_z-xHqoYi4vM40nEoDthxCKgXIIQVGT0RV-8zpCIsjXhuiRqvC40gaFAIPMbqp-J3PWekoTIZXbnsE96ltN3uwiEoKNXysng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویری که ظاهراً پرتاب ATACMS با استفاده از HIMARS در کویت به سمت ایران را نشان می دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67966" target="_blank">📅 02:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67965">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
حیاتی معاون استاندار خوزستان:
در ساعت یک و ۴۰ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه نقاطی در شهرستان های بهبهان و دزفول مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67965" target="_blank">📅 02:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67964">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
مسئولی در استان خوزستان ایران:
دو نقطه در اطراف شهر اهواز مورد حمله با موشک‌هایی قرار گرفت که توسط دشمن آمریکایی شلیک شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67964" target="_blank">📅 01:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67963">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
مهر:
معاون استاندار مرکزی در گفتگو با مهر حمله دشمن به مناطقی خارج از شهر خنداب را تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67963" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67962">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=JHlIguoFDbWxSp1UbLWQfPYuxvgZY-DPVPi0wLG4SPwk9fB4koV-0eUvKfv9giPxtFrRQ7362O765WsGbt4OHQbAKR_xoBQUlgzhj5ZcZNvMM6QIFkVQSVTPLZgnNjUy9ZohyO4wAZsDbMVkyIppZGpNkFKEl-H1lqSne1Iss_2kk4EcKWIaGni4yq9j6saTR9eReh24kA3z_Tjvleg_L1NgtfGnuXVDoJiiSTqfAFON56AYArerSDjY4Vp-SqDpOto0jlTodHxg6KjBGc5PotP2oa4SmI3E_PFJZbA0QhQ6NEZ8UKccoICzBTbUfcoYIPy6OKgnomG8sVeiKXYp4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=JHlIguoFDbWxSp1UbLWQfPYuxvgZY-DPVPi0wLG4SPwk9fB4koV-0eUvKfv9giPxtFrRQ7362O765WsGbt4OHQbAKR_xoBQUlgzhj5ZcZNvMM6QIFkVQSVTPLZgnNjUy9ZohyO4wAZsDbMVkyIppZGpNkFKEl-H1lqSne1Iss_2kk4EcKWIaGni4yq9j6saTR9eReh24kA3z_Tjvleg_L1NgtfGnuXVDoJiiSTqfAFON56AYArerSDjY4Vp-SqDpOto0jlTodHxg6KjBGc5PotP2oa4SmI3E_PFJZbA0QhQ6NEZ8UKccoICzBTbUfcoYIPy6OKgnomG8sVeiKXYp4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67962" target="_blank">📅 01:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67961">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=psyte_ZEQG1dUpI2yzHayOf3Md2R36o-dAvNVBJvu1zG6kPbrWMAU8qXpx-CnpTGIevtRmRk_UZlgKCu0orQ7qhXtxhHceBJOYPBrlCYurVpZZ6lK3k8Rhmkl3gwOMAxwk6nXkfC1Cbmp6aWRPvvv0AK_piqZpXT20PkYOG6h0YvuhBG3HeWLQPTCEE-np3iqV65Uu9QHvSJywDlqm-lmosGtmpuOHuBus7t-Rf-Hc3n4R2krpA20iz474-MEqIBwQBcZxp-tkpvM4qUDHtgs1s5BuHashdDwTofGMXOdpYqA9fUnwLv0VncfgvoVUZ8XNBeNSop1II-i9kVJkGnQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=psyte_ZEQG1dUpI2yzHayOf3Md2R36o-dAvNVBJvu1zG6kPbrWMAU8qXpx-CnpTGIevtRmRk_UZlgKCu0orQ7qhXtxhHceBJOYPBrlCYurVpZZ6lK3k8Rhmkl3gwOMAxwk6nXkfC1Cbmp6aWRPvvv0AK_piqZpXT20PkYOG6h0YvuhBG3HeWLQPTCEE-np3iqV65Uu9QHvSJywDlqm-lmosGtmpuOHuBus7t-Rf-Hc3n4R2krpA20iz474-MEqIBwQBcZxp-tkpvM4qUDHtgs1s5BuHashdDwTofGMXOdpYqA9fUnwLv0VncfgvoVUZ8XNBeNSop1II-i9kVJkGnQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منبع عراقی:
موشک‌های آمریکایی از کویت پرتاب شده و وارد فضای عراق می‌شوند، به سمت ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67961" target="_blank">📅 01:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67960">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuZMRyplaBlHWivdoLyO9UgtvCKxWnTHTCBMPYKq6qxhFlTWOtrkjgzyf_N4WJ66grEFA1n1mNVBkwI33UsWd5gjVJhk41WTUxg88YPqEUktaEvp7ITVcLHx5kTfnqUoXu83snvhWAl9w-K3dTFeEMyOxLwH_r55W3jwovZGpHQ11cOpJkaLTXmmGkht6OtH9A_0opDNyro-lX_zxQe-HeM4es5j13znbbSU7wHOLo2tNwVWzxPxtzY6V0QSMVrlLZCYHG-uXm8jYHU4fWqjN1ZWaguTijqBpiOZOIjDcFE-KttJVq1MHiTy-4FNheRkqGQjk1KAYmq_UVrQ3EwWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
ناخدا دوم تیم هاوکینز، سخنگوی سنت‌کام، به من می‌گوید: «در یک ساعت گذشته، نیروهای سپاه پاسداران به سوی شناورهای تجاری در حال عبور از تنگه هرمز شلیک کردند. هواپیماهای آمریکایی تاکنون موفق شده‌اند یک موشک کروز و یک پهپاد تهاجمی انتحاری ایرانی را رهگیری کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67960" target="_blank">📅 01:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67959">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
اهواز رو دارن شدید میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67959" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67958">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
گزارش های از وقوع چندین انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67958" target="_blank">📅 01:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67956">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYwa0rkETnGB7SVAe6NgHE1KfIbVZkpZNH7utITsYEsY_NpuJA_jMM9vm4JFLfn7jmEmTtnVeTyCn_1fyPKBS4nqUav5TE5P4XmKYE-fX4YVcUMz3Zkak8N9O4s_0fVT7Zhd94UpXOFhghzdN4gybzPRJpdLwjoQD_7JRwfU1MpFMEu9Bi68a-jVPICsKjN5cHcP-tiGRUm4_PTKJqySu5aoAStVDfvgqRLeWDyEoczaooedGvCSVac9-XoxhR2I2B8nj2nXnZB5AjlY6pusmS2FnME3O-XNBhDqOr2_6EmglhvF1E52kUOuZjLygA2KD8y1hHOURY5Q0Yj-sUWq7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=bTZdK74JJ5D3CtZIL1bNyzTmjLoOlJhNK0Hse7l1gUVVA3QeXVnGIxznNJddEF_wHdqerm3HpoHm9PrEkXkSYTBQyT9ey1qYF7FKjRqnr3qGan8O_2cy6DBMP17EdoPA2ZV5We4dEAVd0-BCwCxWgAvkTJ6sEBOXQqfVHYlYQOxW7G7aGgWNvSDuxBftY6P_QrrSEBbz17CT7x7DEI9LYzAu8K9LI08wGHBMN9krYgJh5nAOHWm8MFoGcLYk7ASGBXVGbdsZrlHgGxrZND3HCH1VCaJD6fuuYusuPc2b0iVTIy6S2W33WE73EY7vtGTf6YuMZgYIIbBptlsyrQsnag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=bTZdK74JJ5D3CtZIL1bNyzTmjLoOlJhNK0Hse7l1gUVVA3QeXVnGIxznNJddEF_wHdqerm3HpoHm9PrEkXkSYTBQyT9ey1qYF7FKjRqnr3qGan8O_2cy6DBMP17EdoPA2ZV5We4dEAVd0-BCwCxWgAvkTJ6sEBOXQqfVHYlYQOxW7G7aGgWNvSDuxBftY6P_QrrSEBbz17CT7x7DEI9LYzAu8K9LI08wGHBMN9krYgJh5nAOHWm8MFoGcLYk7ASGBXVGbdsZrlHgGxrZND3HCH1VCaJD6fuuYusuPc2b0iVTIy6S2W33WE73EY7vtGTf6YuMZgYIIbBptlsyrQsnag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویر مربوط به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67956" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67955">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBeHrAd🇦🇷</strong></div>
<div class="tg-text">توالت + دکل = برنامه طوفانی پیتِ پرس زن</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67955" target="_blank">📅 01:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67954">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :  @News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67954" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67953">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
گزارش ها از انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67953" target="_blank">📅 01:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67952">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEDHuLuaX4zuTYAcMTacsRe2OcxYuufArRG84ojWCwdDZ5kzhJ7LOXHC8atxQqcsdKIPihsUbyPkW12ntX_Zrt4kDlEoOkQJkYgGA_SWKomVaH2CyPG2Xfrx285bdu3-RR-OQ6wfPZ8rKd86I44v_jt6Y8kEIUcvmK2xTRqRFgxdqmB8sCodteNwTU-xmpdMbKkozql6PFG0u2MQ-9lib1FsmkjxzLLbbPVo4LWycdNA_2H7dFD1s6KOP0ZVz9vr1kbCuyoZNMMZ2iElbVs2ZmaqLOCkuJNXI1uycDfVNjpt3NFJzpmAZkAcxybAoHHZdufxRKQ7uPSQI699b1OsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
9 سوخت‌رسان آمریکا در حال حاضر در حال پرواز در آسمان خلیج فارس هستند
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67952" target="_blank">📅 01:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67951">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnD7k9wy-296Rh28rZeozhwgNpYIhJXWExpM3tP0wa3sseH1whXXWxTUjA8_NlOSxf1luTBKNDk2lAd1aJSFWkQJ8D-iTjfy5rOikM9Mn2KyKz3ICvtJEUUcbmByUg8J2rAXGb89BIwKAOobmPQHbLipGcwKq9MJHmUzeUH_mDvVm_u75gYjuCD27yhZys_C_69q52Qs42XHhnk0m0HvEVD-iH36A-5R0W5GThieGbKuOuXeKkvkFgF4Xh-Zsm5Go8Lx82k20SYslF8eCFW_iAgUiFzbc24GVXSMXnHEtPLaxNsmNPTeOHn_Z-CuZ34eloDQnCFE6Hz0lafF2ZbT0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویر منتسب به انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67951" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67950">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmxsPFX3UJ5VBuzJrGvo2GGwhPpgO5_uMIbXXYNcdiXOpLBAk6SBiKaSfNbrgBUV-4H34o_w-6SQPObYiPyJ4XF59oiNPCf5g2g_nwj6VNjsUW37hI225OPDKFDYi2Gjbx-1sqYqA8R6SNEi7lcushH08TlqnuSuJwX7nf5q-TsM6PtMxRnCCK2hgo8CiL5UPKalf85ZLqFkZGPhX88yePY64AN-pir686-nIEg73_T4Nbcc6QNNye8UgSCdhDMw5XeDf81Ydtpj_jMshRip_EMkGFxBqRmyoeMSWYQXPflBBvoMLhQQnh2TTBuPTPIl8RozMXXogzI8lbH9e6OPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر من زود تموم می‌شه، چون:  صرفا حملات جنوب کشور هستند دلیل حمله هم حملات سپاه به کشتی هاست و این یه حمله ی انتقامیه، مثل چیزایی که دیده بودیم قبلا   یعنی در واقع حملات، کنشی نیستند و واکنشی‌اند  #hjAly‌ @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67950" target="_blank">📅 00:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67949">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
❌
دو انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67949" target="_blank">📅 00:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67948">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67948" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67947">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlOfkV-LbqGwWWNqlTg0pAOal6DEG9VcqBLM5v2O0nskEihx0xJpHXtNNH1jSLlTdakj3r2zYfzYF8P8XMWPRmPN4PWm3Ybd1YCBVK4_CcLCxLqGlUx5bPOc-eGCpftZvW3soLQKcPSFszWX6HfQ5iST5QJl-VAvggEX_qtV4sEYNNKML1QppACnzbxKQ03L1KukWaEFXrhu5KrdBG-d3ZKY25VnaC60iP3WGP2GnQOUT9hlJ5hO_80jW24ROae9SktB6bksPZUZpS383XdQQZSud5GkyDFXe289KmzFPixLWSV_ugwa8uvfd1m9B52TIwngClsU64hLa4acI5lArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
ساعت 5 بعد از ظهر امروز، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به توانایی خود در حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند.
فرمانده کل قوا دستور داده است تا به نیروهای ایرانی پاسخگو باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67947" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67946">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCQJsXjjAoWjJTgZN2mwY7RDt5yF9g0Bk--pfHw3-c55k0VfjehHzYJuxlWfseKJscvr_sQ-I92QnigMlQ64_ioo11GsjlLRVMqpFoF4YuEIJmBIbwiXwWcryS8T0tFUgHv5Vxkx320s1cfDmYjVgrZu9UIxjQKqkA0Kn6hrefDepFmCRzjTEqTf3DIlI_JhU0PAyrHWUax70QvX6GFoAbhveReJfQZE90hANW1_zUCi_IfQYFHzxs9fcPLJOb5hpA1q1byAIoRo9OhS9-wwNxJjQ4MesijfzsWMpi2kGfpz4J3lFa3qQ7h1OtILHAFNKhYMqYIZdNwqkKtm5fSTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67946" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67945">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇮🇷
ممد سامتینگ:
اگه نمیتونی جنوب لبنان رو امن کنی،
پس جنوب ایران رو ناامن کن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67945" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67944">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67944" target="_blank">📅 00:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67943">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
❌
گزارش های اولیه از انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67943" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67942">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67942" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67941">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به خط ساحلی جنوب کشور آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67941" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67940">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
پنج انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67940" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67939">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
❌
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67939" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67938">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار شدید در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67938" target="_blank">📅 00:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67937">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
خب مثل اینکه شروع شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67937" target="_blank">📅 00:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67936">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=YD08pvYmuDGJCA288MKJBXfzQy6l9RS5qdkRQXiWjN1RJTn1zIX-SFWCDQ0XjFcX23MSVxSaB7KeHv50SvJKW-WWjrZ9z2S0hlOrgLgYA055s2SRpVoRSMmsDKTRH_xcQ6XlgnGo389Ktvz0bxRj09FyV4a4EDZ6cO_7mGSWBG9IelDWEIEv3P0s3lU2GWZoH_wdjqSbFiZDN6KSo3Gznx2zNffBLU1tvrwLkLrou8ruq-uiJhY1CyYeZhjVhEwxgmJnwq-3ObdgzZ1GMpZBIkQ80ANlqoLtzzBz_jfSUS7kaVWa95kKXMQSlx8dNI3UtAr22tRMnqteSTKsgGZTCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=YD08pvYmuDGJCA288MKJBXfzQy6l9RS5qdkRQXiWjN1RJTn1zIX-SFWCDQ0XjFcX23MSVxSaB7KeHv50SvJKW-WWjrZ9z2S0hlOrgLgYA055s2SRpVoRSMmsDKTRH_xcQ6XlgnGo389Ktvz0bxRj09FyV4a4EDZ6cO_7mGSWBG9IelDWEIEv3P0s3lU2GWZoH_wdjqSbFiZDN6KSo3Gznx2zNffBLU1tvrwLkLrou8ruq-uiJhY1CyYeZhjVhEwxgmJnwq-3ObdgzZ1GMpZBIkQ80ANlqoLtzzBz_jfSUS7kaVWa95kKXMQSlx8dNI3UtAr22tRMnqteSTKsgGZTCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Rip
🫡
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67936" target="_blank">📅 00:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67935">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZenSBv-B7nQtsEbjVGc1XcJuebyYffCpitnX0VrueRGTk8BwDHTg9jaqw3xIBoVyPMaf3_dXc0B9XGKvqBVb_QTcdoNmMqi8PdHlQMFKc37kECTkiOgksNbDxoXzqt7x-uFIjl1ElVwrIAcyIaKlzHejkoN9aX2QUWLa0iPCQWlwrWEux8e_XUMLlM7rSbJs4QHxKQbhEEgKtNk85pI_77W8Z8WC4wJfXbE93PNy_qGOTfS5pq_MD5DgSK-ElTeRXMiUW7PKDPdDpU4AWoClg4_NkI7eK4wDoPW4ROJR-cyImdyYNeyiTGrH081U-JgDv1KROIpnMcCDnHUPKj3sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
❌
ادعا: دستگاه تبلیغاتی ایران امروز مدعی شد که سه تن از نیروهای نظامی آمریکا در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✔️
واقعیت: هیچ‌گونه گزارشی مبنی بر کشته یا زخمی شدن نیروهای نظامی آمریکا در منطقه وجود ندارد و وضعیت تمامی پرسنل مشخص و ایمن است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67935" target="_blank">📅 00:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67934">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=LOhceFyBpAeTYnIIPpNeJZKrvvbU5Pjk70pI1FRDf3LctDkNFRq2u0VGBRHUZAj3uqut8-b9la7T54KJ3S9g0aAoifxc9aJWirWfmNyBkh2h3DzGVN1jNibF0l5WhIbBr9aBvnWn7d3H6U0PK29aGV_68HAEKRSfHYJrVe6J1KLEn52FreA3ozMAbzjzhkHIXJCT--afQvWqrF2BUtbhDHYQjSijEXrnMteB_S5Y0azpzEepGc7E_Y8MxrDdDYLsyM4JRT68PbX1KilC_5ag-qnR7BWK8EkIkLlmNKCk6-LlH5zULjWSMeO6vT7eKjQHnk3dTnDG2juv_YOsYYPsNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=LOhceFyBpAeTYnIIPpNeJZKrvvbU5Pjk70pI1FRDf3LctDkNFRq2u0VGBRHUZAj3uqut8-b9la7T54KJ3S9g0aAoifxc9aJWirWfmNyBkh2h3DzGVN1jNibF0l5WhIbBr9aBvnWn7d3H6U0PK29aGV_68HAEKRSfHYJrVe6J1KLEn52FreA3ozMAbzjzhkHIXJCT--afQvWqrF2BUtbhDHYQjSijEXrnMteB_S5Y0azpzEepGc7E_Y8MxrDdDYLsyM4JRT68PbX1KilC_5ag-qnR7BWK8EkIkLlmNKCk6-LlH5zULjWSMeO6vT7eKjQHnk3dTnDG2juv_YOsYYPsNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
سخنان قدیمی زنده‌یاد مانوک خدابخشیان در مورد لیندزی گراهام:
گراهام کسیه که به کنفرانس های محرمانه بیلدربرگ می‌ره
کسی که می‌ره چنین کنفرانسی یعنی از پشت پرده باخبره ولی اجازه نداره چیزی بگه
بخاطر همین لیندزی با هشتگ Make Iran Great Again می‌خواد به مردم ایران نشونه بفرسته
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67934" target="_blank">📅 00:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67933">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfK69EXhAmVS8GanZumyplRDo_ga5vDpv0UB_Ise70mkibvYNKU1goWAOu5blBgQ18QbH5Gf1AFgdKd62Xo3YrtSOIxifFMZEz2XuvSV5Wgsmmmvbt2fvzvOPBcUrWNFUqfZtZLtOTABEUehaNjayaLsPLOXOELacDcTJEjqJ9Trk9jZOB0HLl1uOC4bxh3Mcl7503MrHe4zZmYZjZ8m9uwYRt63Z4pGtelLHGKp5k2FNSOlDmmO50dKzuCElMyET_kpC8UtIcqmVIPAXRMJxGevjWv3OS5ExWalaxF3X2olVOFZGZ0NejEqEzdGnxk_z-3RP6xKyurEryDjrXD3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال   @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67933" target="_blank">📅 23:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67931">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e345P40hoB5Lqc1JVig6wgqLzV1wWBfbYtZMX8EjK_01xARjIJMwJUvxYCP9ooSLqncvYkexob8n1lzn67mnhfB0WeplgmSkvCXza2gcWKI-LbYWk5P5SzRKuOAXmXGy0VzlJqSA-aOZkpXQkdkLOflDYnvhelZ0hk1RRQTQyyeqOq3PykySw14tD9s96PJQ9mWsFi6vua3SrGCaug443gg7CcLnsLVM75N1tIU4rMu7rzUcB1t3mwgSrQHiHLX1m7j8AWVQkIEb4CgQaU2DbK3ew0wTnkHZFndQybCvs6r-4lRjmMtb6-tLUD6yOR-DCTVgamCkp5CuZAj-QnFctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIwdYO_kgAmIO7Gf9m9ylrrzMC_dOJlp3msJXsak57wpZc-9g2AmTPD5g6985o9mKnrF2J07YHEqzZhLaAGQA1PSeusQ_yeFKes66WT98FsKvM8Xax1L7P4Ab7KxnAwIgScUnfocE-xH3p96nL9eVdlMaW6w5kA8g5qlQKU8KL_jojepGh9nB2r-Q5AAKe1UkSdOGSICzReqbn19jjQYqctJanZsFacVkvrzKUyn0OT-jtuYjB7sB6Fa9DLHhbjF1acjRUExlx81L6HqtzzyOvm16H7rOOe13KKyTC4UpUmayte_r8eGaEXmTo9zOkMF7FdnNlG9f9lK773HRHW01Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67931" target="_blank">📅 23:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67929">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mp9LHRMx3IMgNvWDJf8Pr9m3OLtThPqVZxqSpvst68ekKcWYN0q8vGSLGJb12AM50izaBKvCxLe79AitlLZqxTe1_HixAnF4Myjs_-hg3hc-Sx4k9399o1Ry6YN3dFHdsLYTH8peQMnQCu9ARsEQ_sqswCoB8NV-jBwEwPh43gZSa5jWstqnmrrdUAjgs7mYu89KsNZrV0YxKWOUdjiCn4M1fxJGUp9mf_Qgr2gi_ULdgKlwl0sP_E3odSmS9BH2zQm2qYS0I_Y3JpbQbujgQrAxq_MlM172KmA-8bVaMAgENlqIGYXwcnAU5MSpYI4fChQ7lllArCOSHPc6Hul3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwvAhY6yCMcueNcUgklhtB7GgHj-q0bsUBuPe21SOxz_F4pYbG-V73YIlyH7eRAlBYCxg43qkbrs1i3F8HclnMqt1eP-tCzEoTOYwGhGPlj1fnFZqwzBdAH5IdxfKAQiPY3b7T8HL5tBvmyYuLex9lptnfEkadPaC2sFTs4T2FoiFrfPPD2DaO6oaYDoCXCRq4B1kMo5rmNpI-Y_x9VT1pKk6IgLnbEh5G2jKwpENQyfW5byKendY32FU9y_RPJgr2MLnPe5akCEHF13FRr51NkKs3LyR0L5SXPsmZ7K5ZAPP6Z6YMdTWxDOlDDUQIsAj4lexucvlm2lI2im72PfoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
🇷🇺
لومر، خبرنگار جمهوری‌خواه: ممکنه ایران و روسیه لیندزی گراهام رو کشته باشند، باید تحقیقات صورت بگیره
همچنین FBI هم وارد تحقیقات شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67929" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67928">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=gksahmuV2dNDsYL6A1jNN_9bFRbkHreicWrsnj4O0LGsp2mQcU0yJE7rTiObqv1J4aZWMkUvjRCItjHwLN-aoOYXBWFox7H5lOb-Tq-FBDBUr6pAoJCsl9DH24mXAT-TQfq_m9eVQEIv7dUG2QDZ5X3xuXmZ-VzqTGr7-EVWJQjCP0DwmDxOhD1HnHEw7kI7rdrxhvzMlhwDT2Xbl1BiIBcas6bl5P0H6LP2ySAcj5s5VDnw876yD_f4Frh_8FyZEmSrSkoT2Qq9L1EriAtjefzssFZ5Q5ISi7j1NuFF5ZQhts8OznZlVcMjLKLXGfwHq01qDkz6PL6w5mncwtACsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=gksahmuV2dNDsYL6A1jNN_9bFRbkHreicWrsnj4O0LGsp2mQcU0yJE7rTiObqv1J4aZWMkUvjRCItjHwLN-aoOYXBWFox7H5lOb-Tq-FBDBUr6pAoJCsl9DH24mXAT-TQfq_m9eVQEIv7dUG2QDZ5X3xuXmZ-VzqTGr7-EVWJQjCP0DwmDxOhD1HnHEw7kI7rdrxhvzMlhwDT2Xbl1BiIBcas6bl5P0H6LP2ySAcj5s5VDnw876yD_f4Frh_8FyZEmSrSkoT2Qq9L1EriAtjefzssFZ5Q5ISi7j1NuFF5ZQhts8OznZlVcMjLKLXGfwHq01qDkz6PL6w5mncwtACsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خرگوش نر به تازگی جفتش مُرده بود و میخواستن وفاداریش رو نشون بدن که اتفاقای جالبی رقم خورد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67928" target="_blank">📅 22:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67927">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CR42zJvNWn_fW3p7tM8hm3nwU_btoYA1YhhVWvuA_jX1kRbTP-OI6s8ISlqpqnKf9kfwt-1syYOzGqye4bMR3WOkIB9jn6QxWC5TgVCcUevhRELhHJXKgYl0KQlh54Z4od7kKYyluMdS84Z1E1bpV9t0e0QL1S-UaUiVmOWn1WoIk8FwAEJXqmbCFoD5RiHk3dMyHPWuKXbJGtuKM-m_hVIM53AybrdQfYJZb469yJSwSGRQ-lwb7gIjBh4bElENGa5NetkH83gfa9YFfh2eYuWQcIzDGOEiGLgQfFFYmDRRpUYe773ykayjDTNKTbN4Zfq9nrXOYAXMbCUsNFgP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه های عربی وابسته به حکومت؛به تمامی شهروندان و مقیمان کویت، بحرین و امارات متحده عربی:
با توجه به وابستگی حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای پرتاب موشک‌های زمین به هوا به سمت ایران، از شما درخواست می‌کنیم که نهایت احتیاط را به عمل آورید.
در صورتی که هرگونه سیستم یا سکوی موشکی را در اطراف محل سکونت خود مشاهده کردید، لطفاً در اسرع وقت منطقه را تخلیه کنید و از نزدیک شدن به پایگاه‌ها و تاسیسات نظامی آمریکایی نیز خودداری کنید و از تردد یا عبور در اطراف آنها اجتناب نمایید.
از تمامی شهروندان و مقیمان درخواست می‌شود که این مناطق را فوراً تخلیه کرده و به مکان‌های امن دور شوند، بدون هیچ گونه تأخیر، به منظور حفظ جان و سلامتی خود.
پیش از این، هشدارهای واضح و مکرری را به حاکمان شما در مورد خطرات دخالت در این مسیر و درگیر کردن مردمشان در یک قمار بزرگ با سرنوشتشان، ارائه کرده‌ایم.
با این حال، آنها تصمیم گرفتند که در مسیر وابستگی کورکورانه پیش بروند و تصمیمی بگیرند که بازتاب اراده مردمشان نباشد، بلکه از خارج از مرزهایشان بر آنها تحمیل شود، در غیاب هرگونه حاکمیت واقعی.
بنابراین، آنها مسئولیت کامل تمامی عواقب ناشی از این مسیر را بر عهده می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67927" target="_blank">📅 22:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67926">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACt6J_CvgpbLIrLbqoALQvkCXBF2KCknK1brx9KcaL3Se22CRWpkEj7idQxYfijjaKSiI3ONQ8Tf2rCSRH8h0g-bQq-Q7rLeiAjueAn6m_8HHRJPzygwuZB-p2tAk9rewHn0x_hwxqFZm5XGE1O-3LkySF7nIL7AzLN5RspX1i3NIYjR8IGlau7GMQja5I64dPrSKWEoxI-yTjIpsJrmLLsBmZiCsoXiyQJlX_i1CmXrutfZXm3A-xqq1VIDmhOe5z3cQXBRO1m-cZ5vyEkvdwXWSneGQUCjx-kXTutadnsTJA6gnWZxnAnYlFViqVUYty4oNJdBuH-LIM4E5nOpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آکسیوس:
اندکی پس از تماس تلفنی با پرزیدنت ترامپ در شامگاه شنبه، سناتور فقید لیندزی گراهام در گفت‌وگو با فردی دیگر از وخامت حال خود خبر داد، اما گفت تصمیم دارد مراجعه به پزشک را تا صبح یکشنبه و پس از حضور برنامه‌ریزی‌شده‌اش در برنامه «Meet the Press» شبکه ان‌بی‌سی به تعویق بیندازد.
وقتی به او توصیه شد فوراً تحت مراقبت پزشکی قرار گیرد، گراهام با شوخی پاسخ داد: «الان نمی‌توانم بمیرم.
هنوز باید تحریم‌های روسیه را پیش ببرم، تکلیف رژیم جمهوری اسلامی را روشن کنم و روند عادی‌سازی روابط اسرائیل و عربستان را به سرانجام برسانم.»
سناتور فقید لیندزی گراهام تنها چند ساعت پس از این گفت‌وگو درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67926" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67925">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=d2qZAaLXxrk9Qo98KXQqjstvald6f0VyGd4bbj_5-m2q9aJEkbUWkaP9jl4t1McLEiIM3O5YX8UHJJn65r0ROe9lwwL8IpMjQTFztldWc2Op0zyPrKUOft9THjYYRJu63wUUZ-JZJEwcFW57FOCmmhBTOSbw1NVFyIeaRESiDV0ng3R5_g_ji_MfHjorjei4RgHXXa6EN9Ze2ciJ9XRdywFSlu1VWjXb3HoVzfXXGUQjVVax22eDiLZ8HCPYKPe1XQsPokJgZ2RgGd1I9XzdDti49B5e4ugiOvhFn-1eiOd3ZizR8-8oWfk5grVc0tcri2_Rn_9dmKVc_K2fd2dr4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=d2qZAaLXxrk9Qo98KXQqjstvald6f0VyGd4bbj_5-m2q9aJEkbUWkaP9jl4t1McLEiIM3O5YX8UHJJn65r0ROe9lwwL8IpMjQTFztldWc2Op0zyPrKUOft9THjYYRJu63wUUZ-JZJEwcFW57FOCmmhBTOSbw1NVFyIeaRESiDV0ng3R5_g_ji_MfHjorjei4RgHXXa6EN9Ze2ciJ9XRdywFSlu1VWjXb3HoVzfXXGUQjVVax22eDiLZ8HCPYKPe1XQsPokJgZ2RgGd1I9XzdDti49B5e4ugiOvhFn-1eiOd3ZizR8-8oWfk5grVc0tcri2_Rn_9dmKVc_K2fd2dr4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کانال 15 عبری:
ارتش اسرائیل با همکاری همتای آمریکایی خود، در حال تمرین سناریوهای مشارکت در حملات علیه ایران است.
ارتش در حالت آماده‌باش دفاعی برای مقابله با سناریوهای مختلف قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67925" target="_blank">📅 20:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67924">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
👎
خبر بالا فیکه و ترامپ با هیچ رسانه‌ای چنین حرفی رو نزده
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67924" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67923">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
❌
وزارت دفاع کویت:
۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت.
‌همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67923" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67922">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSlxtmk9mVNRpaneBRWnVJZky0KpAyXfjy5oMIOxKk4pgA5bRr7z9DrOod5M9cxNxWUiXO3rm99WwvxuKD0v7rtapHDHw9OMUtfkUKOaBw5rIo_58Bduh79vbRDdv0BX9PbN-4UyCLWg-Yp-cuDLmyZELSkaqKbo_RJdyE7SLVql4_izftO-rIs-0u4G89c0s5S1VO2wR0jdv5tMRnYuB4Ml7DOeqTzWXVIoXhNq1X02lm6DihhNlsGltBtwye4N7I5oEk-DE4xGNz-Qqn3_2A9qcXlEtcUMrm_t6y3KFtkeZpTpvVXYPcgI6KdjVJ7HChDJoAL3TdEULcgclhbzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
ارتش ایالات متحده چند حمله را علیه سامانه‌های موشکی و پدافند هوایی، و همچنین قایق‌های کوچک متعلق به سپاه پاسداران انقلاب اسلامی در چند نقطه در نزدیکی تنگه هرمز انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67922" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67921">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
فارس:
خبرهایی درباره کشته شدن 3 نظامی آمریکا در حملات موشکی به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67921" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67920">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
منابع خبری آمریکایی:
یک حادثه امنیتی بسیار جدی در یک پایگاه نظامی آمریکایی در کویت، پس از حمله ایران، رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67920" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67919">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
منابع امنیتی به نیویورک تایمز:
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67919" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67918">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vm4830n-k-WhLfEUeRF-NGiFtUVvTw6DdHVYmNwnqsrtOvKXXGTmFvvMwlcXQxlgVgDYpy6Es-UIOHW_tmronU-Fsd5nL__oANlonT88Qc2oKiVDXFKype-Trd74uHDJf2xitPl30Fddl6SAdjS4sCUFdmhcg4owp1asfB39Q0zN6x6NmPfCZNrR7mDjknS4GdC4AEVBwLk9BAP4X8jLLneIKWoQjfmu6o3WXJxaou82eC5hE9bfG6TFCEzNqhJJqPAPQsQLx_uwg14dFwEb-byQ3YDWZn4ZGHwVq-lXfvBGxvXn47XcYqruYh8xud2OWTyyEUcX1kAg0Y6-6TriJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قشم همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67918" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=Yp0KqBnvDVW8Aok4oiwIs9qvKQ4VtONy7D1GVpPUqGBefa276RFvnkzqQYrVaF8vHwLFSY8hi6h-7B8-E1ydfp31jcCfPV7BzUoC6c8AbUOTEwpwlBO1YUFe-0sf1rORcFwuPU3xi1-HeDf4IZAqU_Doc7iEUw8VR6K__9K0VdVgTrtxisfyskEzLNsvwzHtjP_hlAHz8u2dyUDgeGA8F09Lyit8FHV_S1Bu0PIzzjdqadv4x51FyAKETW9XVqgjLMRMON-g6Ts4RzVhXPiSt__dSxRg0jqBEB_HRRe32ZrdnoZKfxAMnGo_eFnYnbBWOyEbs3GkC3mF5IU5zQK8yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=Yp0KqBnvDVW8Aok4oiwIs9qvKQ4VtONy7D1GVpPUqGBefa276RFvnkzqQYrVaF8vHwLFSY8hi6h-7B8-E1ydfp31jcCfPV7BzUoC6c8AbUOTEwpwlBO1YUFe-0sf1rORcFwuPU3xi1-HeDf4IZAqU_Doc7iEUw8VR6K__9K0VdVgTrtxisfyskEzLNsvwzHtjP_hlAHz8u2dyUDgeGA8F09Lyit8FHV_S1Bu0PIzzjdqadv4x51FyAKETW9XVqgjLMRMON-g6Ts4RzVhXPiSt__dSxRg0jqBEB_HRRe32ZrdnoZKfxAMnGo_eFnYnbBWOyEbs3GkC3mF5IU5zQK8yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67916" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇮🇷
نایا:
نیروی قدس سپاه پاسداران انقلاب اسلامی، کشتی‌ها و شناورهای آمریکایی را که در منطقه "کیلومتر ۲۰" در تنگه هرمز فعالیت دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67915" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67914">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67914" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67913">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVqyDUrnxQibhDMOto7F5Dc_Su-dOrvK-MO1aCYXeGFaDbQtgoiSYSFokbiCIs4g77qzJHDgBbqr5FdYoJv3XHZbPpREWAmZNlI2D3_Z1aCqD-lnJ1DsDzezvOAJtSD3IM8FmnzSPh4CW7bDM8GI6N6nlW2JCc9DLaTQOsibM2EVCqrAwdkj21lQm7MDdKLKFf6HPk3pAchb-tQ2VuQUbzKs0DdOq3p0-MGN4gd9_MBHNAmdAh_LAR3lVbZnnI1oDyuOffRpy6xH3LLvMkL2er3FacpFSjny8q1xfXmT23Kz2HMPifx_FQhQUrjdwti2mM99yNiGPjLotXib3voQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تروری که روزنامه همشهری منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67913" target="_blank">📅 19:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=inKJ0w9Efx6hbDIFCuLEm-kMDKZp_3vtiIrJAM8W3AfA_2Add8ZUPnYjjxtNNjPsdwIlK14s__LWvW4_jGM0LWmyJI-QoHhifzwE58iAnDXyYKRsdU2ClCUTXLDwJmVGEKrOBkDdiJtMyY-GNF1lwsrgLI2r3KJGV316mzbf8rDFXYR0nzBggOrqBQ74QV65mdWlG-Y7W-n115oDb-PYAyKBhQTNKttat4c6wAQ1ZYFvA6S8MZRICSlfTSNI9ub4JkAUmeuAKnlgOIIHQw-8X7qZXSmRSfduAHgw_j-QnfVmHguqlED5uEHDFLQWt46VcGHNR_LXYIXU_2S-_qwm-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=inKJ0w9Efx6hbDIFCuLEm-kMDKZp_3vtiIrJAM8W3AfA_2Add8ZUPnYjjxtNNjPsdwIlK14s__LWvW4_jGM0LWmyJI-QoHhifzwE58iAnDXyYKRsdU2ClCUTXLDwJmVGEKrOBkDdiJtMyY-GNF1lwsrgLI2r3KJGV316mzbf8rDFXYR0nzBggOrqBQ74QV65mdWlG-Y7W-n115oDb-PYAyKBhQTNKttat4c6wAQ1ZYFvA6S8MZRICSlfTSNI9ub4JkAUmeuAKnlgOIIHQw-8X7qZXSmRSfduAHgw_j-QnfVmHguqlED5uEHDFLQWt46VcGHNR_LXYIXU_2S-_qwm-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
دقایقی قبل از فوت سناتور لیندسی گراهام با او صحبت کردم و "او به جز خستگی حال خوبی داشت"
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67912" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=a8CxukBJLQRUyaSwFvhWNN4trKO_ytiwkG93yzbRq14XQnnzGOfVZUaC0qQ1b_yAMY2FzQUOlJuAO44ZRPYbh4IUg0xpSHH0YIkf_MH09QTSxfPjTdc0vmrDDF2vrSTLks78iy6CRAB-7BOAHi2fdr22sNuZL17_VIMzh1o_OJxmkVmJiVCqKP0rxElCmAyHPKhUL9_NemgYHS2yiwKy1LeQOxYi5I35mNpMD4nPHZWdEIp-lJNwGsHYjG7z6qlRKtDdjo7WELSExl-qGBaNQvtxBEgAxQz9pMdtcwllGZUTj5SUYltlZ17KGmlSLkjm2-5jaW7PssPCFsdOtljqHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=a8CxukBJLQRUyaSwFvhWNN4trKO_ytiwkG93yzbRq14XQnnzGOfVZUaC0qQ1b_yAMY2FzQUOlJuAO44ZRPYbh4IUg0xpSHH0YIkf_MH09QTSxfPjTdc0vmrDDF2vrSTLks78iy6CRAB-7BOAHi2fdr22sNuZL17_VIMzh1o_OJxmkVmJiVCqKP0rxElCmAyHPKhUL9_NemgYHS2yiwKy1LeQOxYi5I35mNpMD4nPHZWdEIp-lJNwGsHYjG7z6qlRKtDdjo7WELSExl-qGBaNQvtxBEgAxQz9pMdtcwllGZUTj5SUYltlZ17KGmlSLkjm2-5jaW7PssPCFsdOtljqHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کویت کمی قبل
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxzoOBjalrT73BpzcF_UqCcvl86B3UAC9I9TOco64egdpAnysLSu4_yzEIw11lOJLMyP6pyt7kN6K0fFeEP5_6mN6e4q9pYu_iUGfjmoCGKrnU6SW_RrBBHgey94eVW6UkcuGVdpWdIiLNQY6ht68fXhEWx3y_VkkCsDTYKq032p-hysY2axIXMqOheHhu_iHNTDmRLpC8mb2nIZuf-0O84tTwxiBYWGObVEVNn8lZuaR_NPchdC5UNkUbNiYJKHjXwMeoTYpC1t1QQV7FY2pj78UE-xNT8FwyhHcD6poW9A8Cxd6ONzg6fQdWKvt843Ca91KxFVOvU5Pp4cZnhfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=QKyDV3gNpR8FIE40-LopZu9m16M8dn9ARnZqgSYh5e-WIbzJI0u3C4OkMSFH2PK4g5qzhoMxubYSxlO-CSPqwPaB4UNC4StXLqv7izKyGxcXbmYEL1YNjjexTxEKZDKoETte7rZ8Fkmw7LzkgLPS7xhzXc0f8NedcXBVcMayVj4aGZ1Gkky2VP5esuc4-83pPTkcmULtISEtJe6Pnx3C8iuZzZ0cQvQQ1U0YqdutY9be3ldVSIdwdbXvs8JLO8VZDlbd2FfxfMsov_75O7uKO6Vj03Qpwosu_hnbkCoXJOxsJnOzT-eu5yXMXyn_VDHbe9QCUwNlXKb2QusSeYq3EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=QKyDV3gNpR8FIE40-LopZu9m16M8dn9ARnZqgSYh5e-WIbzJI0u3C4OkMSFH2PK4g5qzhoMxubYSxlO-CSPqwPaB4UNC4StXLqv7izKyGxcXbmYEL1YNjjexTxEKZDKoETte7rZ8Fkmw7LzkgLPS7xhzXc0f8NedcXBVcMayVj4aGZ1Gkky2VP5esuc4-83pPTkcmULtISEtJe6Pnx3C8iuZzZ0cQvQQ1U0YqdutY9be3ldVSIdwdbXvs8JLO8VZDlbd2FfxfMsov_75O7uKO6Vj03Qpwosu_hnbkCoXJOxsJnOzT-eu5yXMXyn_VDHbe9QCUwNlXKb2QusSeYq3EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پرزیدنت ترامپ:
ما آخرین جلسه را با آنها داشتیم، آنها دیروز با یک توافق موافقت کردند، یک توافق عالی برای ما. نه هسته ای، نه این، نه آن، نه هیچ چیز. آنها همه چیز را رها کردند.
و بعد از آن اتاق را ترک کردند. و سپس در عرض یک ساعت یک پهپاد و یک کشتی را به آب انداختند.
گفتم شما افراد مریض هستید. شما افرادی مریض هستید
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67908" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67907">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILHu4N51XThxTl8sk5CQjvraYoO7wFrh-Lkq_Bc0jgaNKnO6Glcc_gYqgikn8sPKzf9tOO3y_Iu2uosN88jBrgrQ4whOZD9ik3KMK407VfkPd2KWinnUV0AZbfv7bjT2R2KHCI9K8himvyRK_lpA16dIDMHk_Nvyy-pTQ6-d3xetjadkAP6V7Bl8AQEAJRCAa3iAv-qwt3IqFTA7unJ8f_5UN7k98DLOG_CDaXnlK0nf3HWKsmQW4-A4dMxyX8VicDO_YH1HduVzim9oiD2eeKxMLGqo2WyMvm-VfPNm5bu6kBbq5BR-zupABfl8FVXpnQ68eZ-FKidIOxTHntOtNAhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=bkRrmFUrsEOYGYcHuE27V7mu_XKvi6St7TiJzMFGeFQPAMXjQWHdwSFA67KIb_AMfUuTXQpJlFElgnPzBXB-Yf1Tm6ZjwBezPM1YgXoomjummNOHkMHhSNARWHQQ8_fKD6C0gxx9HOLa8sEk8uDhMHHDugdGYvOiL_MzxXoD1d0aSULBv7qC-wta-znXli5mZq9N3zphS1VTVUR8OnLgQak66W_AbK2XOuqFBXmywB5l4I8XIams4fKhGEOLNuwu7-3QUmzdGEvhreXsILy6xwfG1_QOgVqMkGlq6XOLOt17vewLjzRmGw8r3sV60qNVcP2J2IpA0Vj4V5N2M8LILHu4N51XThxTl8sk5CQjvraYoO7wFrh-Lkq_Bc0jgaNKnO6Glcc_gYqgikn8sPKzf9tOO3y_Iu2uosN88jBrgrQ4whOZD9ik3KMK407VfkPd2KWinnUV0AZbfv7bjT2R2KHCI9K8himvyRK_lpA16dIDMHk_Nvyy-pTQ6-d3xetjadkAP6V7Bl8AQEAJRCAa3iAv-qwt3IqFTA7unJ8f_5UN7k98DLOG_CDaXnlK0nf3HWKsmQW4-A4dMxyX8VicDO_YH1HduVzim9oiD2eeKxMLGqo2WyMvm-VfPNm5bu6kBbq5BR-zupABfl8FVXpnQ68eZ-FKidIOxTHntOtNAhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
و شما بدیهی است که یک شبه دور جدیدی از حملات را آغاز کردید. ایران یک شبه گفت تنگه هرمز بسته است.
سنتکام امروز صبح بیرون آمد و گفت تنگه هرمز باز است. کدام است، آقای رئیس جمهور، و چگونه می خواهید پاسخ دهید؟»
🔴
ترامپ:
"این باز است، و من نمی خواهم در مورد آن صحبت کنم زیرا می خواهم زندگی لیندسی گراهام را گرامی بدارم، بنابراین نمی خواهم در مورد آن صحبت کنم. قبل از تماس به شما گفتم.
آره بازه ما دیشب آنها را بمباران کردیم. آنها افراد بسیار بسیار شرور و بیمار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67907" target="_blank">📅 18:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67906">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=QVn357dV5UMrKNTAv27lPpC_A9WTv11spR5CvIU8a_xQSFmGhgMlpmeI4x9qL0o-olpuXGWsXDpfHo0PVANGcESbqbODuzdgUOivZiuTY5ZESJew8hSKWqxbyTTqeHDFLtf91rO0Oj09PxDkP1XY10O5H-okeybDLO1LlW7WUm9MhJAsobZ057-1FNT19JSv0xf4cJNR9iXeXR4aV8llg3z6lookfeBAUdcJ-v848_StZ-2-boRkyozv4ccSup7yUqPoidbungCyZAjITM6GG7_wBGPe2Xui3AIvUH6cT0R-94ABOasKhQAdw88eSO-P1KNxuXlANdGwDkEb0B_WRUMw11tbPg3eAlW9Gb056n-luw3PBdUUC0xsSkl52pNxsTSjQKeVK3cKu3aXRFBvX-elFvb9FQ-lK-LEsMr49dncDgEHnzzI9xXBGp9iylfUWQVkfVydJsM2VPrya6PjGj2nOrjUpcisuWoff6wnZwX5C5jZ-lYd4wcyoMWkp_DTTDN5G82uaK0-6MC9AZGH_blUcHx7nauEexlVTXxWRmAFUmtSezoKZxyLmumDT_HZAjwjSsZyr22jb7Fml0AHYkiY7B0odzU3xxk6UnojhdKok0Ml9lEzrw4E3ugso5IwD2aDnox_ZLgcYyhn20SqEeoReRAEwDOwcvH2AbXUzuE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=QVn357dV5UMrKNTAv27lPpC_A9WTv11spR5CvIU8a_xQSFmGhgMlpmeI4x9qL0o-olpuXGWsXDpfHo0PVANGcESbqbODuzdgUOivZiuTY5ZESJew8hSKWqxbyTTqeHDFLtf91rO0Oj09PxDkP1XY10O5H-okeybDLO1LlW7WUm9MhJAsobZ057-1FNT19JSv0xf4cJNR9iXeXR4aV8llg3z6lookfeBAUdcJ-v848_StZ-2-boRkyozv4ccSup7yUqPoidbungCyZAjITM6GG7_wBGPe2Xui3AIvUH6cT0R-94ABOasKhQAdw88eSO-P1KNxuXlANdGwDkEb0B_WRUMw11tbPg3eAlW9Gb056n-luw3PBdUUC0xsSkl52pNxsTSjQKeVK3cKu3aXRFBvX-elFvb9FQ-lK-LEsMr49dncDgEHnzzI9xXBGp9iylfUWQVkfVydJsM2VPrya6PjGj2nOrjUpcisuWoff6wnZwX5C5jZ-lYd4wcyoMWkp_DTTDN5G82uaK0-6MC9AZGH_blUcHx7nauEexlVTXxWRmAFUmtSezoKZxyLmumDT_HZAjwjSsZyr22jb7Fml0AHYkiY7B0odzU3xxk6UnojhdKok0Ml9lEzrw4E3ugso5IwD2aDnox_ZLgcYyhn20SqEeoReRAEwDOwcvH2AbXUzuE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67904">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=EcAk_RPYFdhswR2OZYb3E7dglYrnPTdLHtHbFB8k-ywT3C35uDKVuESNubY0UIJw4oT_HGkKiO58NQtvYl6IipJ5C_B0sqLd0BgPdTfByz7b9IIDjpc7ppbGw0y7bC6ji1LxKdoUYDwHdYCn_EJHoVKMKWgJSUSwLRYV_nFy0e5GmKv_6pdQUbS-Kiqh9xoby32ZixGC0NFRaZXns82jO7aDqzn0SRnj2uROzIPz3gJtNmfgUVck9C5rQf6aNJkCwxy5eTsOdrKmURM_JBxtnIbH6aq99QyI65uRDXJIXeNhf1L-5RpetCqwbUrYByahs6M8SQ-RTToMCt2ddc1iDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b2f989ab.mp4?token=EcAk_RPYFdhswR2OZYb3E7dglYrnPTdLHtHbFB8k-ywT3C35uDKVuESNubY0UIJw4oT_HGkKiO58NQtvYl6IipJ5C_B0sqLd0BgPdTfByz7b9IIDjpc7ppbGw0y7bC6ji1LxKdoUYDwHdYCn_EJHoVKMKWgJSUSwLRYV_nFy0e5GmKv_6pdQUbS-Kiqh9xoby32ZixGC0NFRaZXns82jO7aDqzn0SRnj2uROzIPz3gJtNmfgUVck9C5rQf6aNJkCwxy5eTsOdrKmURM_JBxtnIbH6aq99QyI65uRDXJIXeNhf1L-5RpetCqwbUrYByahs6M8SQ-RTToMCt2ddc1iDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن سرباز بر اثر انفجار اشتباهی در تمرین پدافند هوایی روسیه(نزدیک بود همرزمش رو هم بگا بده)
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67904" target="_blank">📅 16:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67903">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCYTnjsla5geHr-1AEY1IuF7uhoCnUwfMb2j2rd_mfly7vRafOt5M70Ag-CUjWrZKLlX7kO9RoUIqfyWTvLaBXHTtLcBN-E9YKTbzNo_zvtlt0-t-7xOcPy-H1_Bf94Ui2A0DGZQqam5kP8tjv5sGU8MTmCAghtEa7RjpnJAPpvb6ZRd3pnQo7ii737SRnQC4e0adKMVeO81o3aArz91Dvo7VNX5RKJkc5hDETDcEcGg8nMf--Zx2MtVyMjEjTP1fm2QPNyGdTyBmiqzbx7OseKVYr6EJtC0aNpDM0HBAw3dNMjqbt5eQLAe2e1jx2YZDuoBb7esA1nPx0Pn2XNbCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
تنگه هرمز برای تمامی کشتی‌هایی که قصد عبور قانونی از این آبراه بین‌المللی را دارند، باز است. نیروهای آمریکایی در این منطقه مستقر هستند و آماده‌اند تا از آزادی تردد دریایی اطمینان حاصل کنند، علی‌رغم اقدامات تهاجمی، آزار و اذیت، تهدیدها و اظهارات غیرمنطقی ایران. ایران کنترل این تنگه را بر عهده ندارد. ترددها به روال عادی خود ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67903" target="_blank">📅 16:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67901">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5jXiukWAGI4-e38_lKXJjIT9h5nL60sxwMXU0cYxFdY50gnasqTcTkJGpG-kAPVLkB-01LThW_9kxZo1itscMKHGQ3LZNMMQIblcQZq6VlTgMB038wbqyyTYaSbsg52XF8wp0hW6cJzs0EWwlyu_NdOHXZtxf93mykMizlLMHZsshFWZJAEsSZsHoh-lGiOtuJ422fLmnI_cafZ94qQfBlgCvOHMoTaVgr9c_cyLdxZHA2F3wixZCk5KDOnG5yuGoUnFykNtnZ7NL6oHc7kW3DjwyqoROo5XBtySNouZs2JarBK2S6k0EOTfIWTnE0rtobe0c1axmYJ31b10kLHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=LKZCdX9TVtv_I7CBaRnZl8aTOsxbWqY3Ns386R8RwARw6SGehsFeDsCnlucB-Mf-5Z0-Pna-SAKTLI9iXNm2TY-PpmRthZ9oSWvF-pVJKCbPJmF2Clw0ErOHkQXzYleuI4_a2MkH9-orHqwm8Faxwxmfd_Ik3x42Ge6fQu1UAMJrg6uQSlSQL0NUD9-bPTzdDwsu_i4KFjU4PPSmCXDIVN3ojGh54qgFp2eZ_plaF0WmbTOxMdVhRHPFS72JTg4A1T449qW681K2f7y95QNcr-PhqFQ6Q4fNrQNPgh5QLXtkOgKSAI9rj213YANIeprdV9rkoROiLNnt3Hq8SVn1ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa15fb6f3.mp4?token=LKZCdX9TVtv_I7CBaRnZl8aTOsxbWqY3Ns386R8RwARw6SGehsFeDsCnlucB-Mf-5Z0-Pna-SAKTLI9iXNm2TY-PpmRthZ9oSWvF-pVJKCbPJmF2Clw0ErOHkQXzYleuI4_a2MkH9-orHqwm8Faxwxmfd_Ik3x42Ge6fQu1UAMJrg6uQSlSQL0NUD9-bPTzdDwsu_i4KFjU4PPSmCXDIVN3ojGh54qgFp2eZ_plaF0WmbTOxMdVhRHPFS72JTg4A1T449qW681K2f7y95QNcr-PhqFQ6Q4fNrQNPgh5QLXtkOgKSAI9rj213YANIeprdV9rkoROiLNnt3Hq8SVn1ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از اینکه صداسیما رسما مرگ لیندزی گراهام رو تبریک گفت
فیلم تبریکش بشدت در رسانه های جهانی وایرال شده و گویا برخی دنبال ربط دادن مرگش به جمهوری اسلامی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67901" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
