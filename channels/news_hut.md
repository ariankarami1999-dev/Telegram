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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 21:56:29</div>
<hr>

<div class="tg-post" id="msg-68010">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyn4CWMzoLweTYeCqFZgoSoy058HJzTztUfae3wKV1_Q_OQufV1PFaEU8BMx1Wk3toaY7M3LBoqq-HiWEbl-DqzhbEORZ0C1d7Wnrfhv0-vA3rPQUhSUsY_jt2_Njt-fOUtR9Thtulv5dW2WaSp7RrUS6fakoDHbbK6AO5AZXE9p-SqmptoO6Yrs76y6T90fGPiVK9jHD08h-ql5lgCZyDWHNPSODmmrulB5wfzqUbnz9X1VOSlpFBIldBvbWlhTQnHucj9ReG2zWXsa6rUScOUHBnp_-2LJVw4yq6S5T7nD5MlJNCk9JlwyGN2UOAsjxTlNHeDNdsO3Jput0qplug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛ایالات متحده اعلام کرده است که از ساعت ۲۰:۰۰ به وقت گرینویچ(۲۳:۳۰ به وقت ایران) در روز ۱۴ ژوئیه، محاصره دریایی تمامی بنادر و آب‌های ساحلی ایران را به اجرا خواهد گذاشت و تمامی کشتی‌ها — صرف‌نظر از پرچم کشورشان — مشمول این اقدام خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/news_hut/68010" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68009">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzTgbH9vnn-0oM6URZVMZezPqeV8j7OZqrjzaPTFhu4rr11FIa4MPXDecOaIvkyNHn0_Zqh9Jy5Cwth5tW8qxGhEsXluq0ImBMeswR7S-V8BWIzGhoL_qgHWR0Iz23VK0_mwmNI6-iC9QqWKpWHHIMmDcS5_3OXnGFXlD1MvX-UgZrBhV2y8xm3R95kSm603vEpF6q9QwqjGNX4MyTw7hfKOZEj7E5_8gg4ka6cHeleLpXjEBk-WVl0e8c-dPpS9-YqXB5w4GAoEzuDHoCM8adQwKxzRlSW10X8Xye5TP4UhelBZwDhk6xPpjvqL1hCjrX2x__UFLkj6K5IXkIQTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/news_hut/68009" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68008">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
هواپیما جمهوری اسلامی داشت میرفت سمت فرودگاه صنعا، این فرودگاه بلافاصله توسط جنگنده های عربستانی بمباران شد.  @News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/68008" target="_blank">📅 21:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68007">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/68007" target="_blank">📅 20:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68006">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/68006" target="_blank">📅 19:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68005">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/68005" target="_blank">📅 19:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68004">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68004" target="_blank">📅 18:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68003">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/68003" target="_blank">📅 17:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68002">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ترامپ دستور داد محاصره دریایی علیه ایران دوباره اعمال شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68002" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68001">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/68001" target="_blank">📅 17:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67999">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67999" target="_blank">📅 17:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67998">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67998" target="_blank">📅 17:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67997">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67997" target="_blank">📅 17:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67996">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67996" target="_blank">📅 17:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67995">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67995" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67994">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67994" target="_blank">📅 15:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67993">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67993" target="_blank">📅 14:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67992">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67992" target="_blank">📅 14:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67991">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbYr0IKYL8l-zp0C9RSDh8ZELAE0N_eAdDFkMSoz711-okHflwgTdzk7ViJuOvNqlPNJdRkzrJDen-VdAoGh7yeIFYXcvRB-d4-rPKuEbHTRr_Kn0IshdgVWVJeWrX9-3TF9AkfFvCDsLewLKiFuDSGN1DuXgYdQf7DqR3F2ygVjuCYefCm_KCEhcMmXj4-LnEvCQKpkyu27HXLgFg2Bh2J0b3L20A_skI1DF3ARuSLr7PGdmKErFcwEJkje2S1L8qAXaya1aa8PXv57u0bbozrIVLg7cO4OMqNmINCnz7tDqT11fNdeaq-9Fg9jpijWu9vB5KtMjvGtQ6f40mybDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
هواپیما جمهوری اسلامی داشت میرفت سمت فرودگاه صنعا، این فرودگاه بلافاصله توسط جنگنده های عربستانی بمباران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67991" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67990">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsuLfZ12zNeQhTpgMU_OGRsAvW8sNGaZ7OtYBb7YfNWAlNNMzkRSMMBq024J8TFpJ8Mpnm_rUTsXGZR3Ru1jF54axGnvNoOIokgkL8eCs9r2HZw-ChKu9GnnAQ8EHfQlJ9z23oiiSHaHY9hb9UOMGgUpKE09XD8q9SDjKIP1PjNHL0eDon0gMxw6CF8Ijw7Zdpvjj7FanUN_AUS0va0v68NpYm_T7fi4HfO3VFkuUWPthpKH7p0SzjeimrAY_hmrDE4Q1p752urlFmQDj8aeToaFqAhoyLtiTLa1qJm_SMFTcL-xd5MCidHv5dD1qMF4ZPa5S5oshSSCTjXMo0d8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی، خواننده وآهنگساز ایرانی، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
جاستین بیبر، شکیرا، مدونا و گروه بی‌تی‌اس در این اجرا حضور خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67990" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67989">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gui1c7A-sQqyB81MPbEncYkeeG23LYJSwZ0avX06LMC49XVA8SGDglFSVLJLO4D3iyQ4HCqwnWi6uoMfjr7uJu8wpmIm1wuo84U_Z_MncUNoKGMsDnngnyIBLWPwI2whM1rzKmza6HIOd3akqzUfpYexv1F_QAeU9nm9r3FkswN2u3fp4fyGV1hJ67TvYMy1dz90tRez86vWRXMgRZdf-4Y09M-zxtJU1fadlF2azTGDIE9J_4odr_8IHKqaDTArsMrAq3ccDLYGoPQM8aBMVU6KyGv5O54e3FXC_GnDkeiQEb9yqTjZ05S9gPFrZXoIlXFJ0UHdQFscOz6pSpwntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های داخلی وابسته حکومت این لیست ترور رو منتشر کردن و نوشتن لیندزی گراهام اولیش بود تا نفر آخر بی‌خیال نمی‌شیم
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67989" target="_blank">📅 13:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67988">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
تنگه هرمز دعوا شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67988" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67987">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67987" target="_blank">📅 12:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67986">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67986" target="_blank">📅 12:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67985">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=smgDQ9xPq_6mR4NZBYW3Jgi4AxmE_if-I7g0od5TF8dYjtz__lTGflsf2hkT0nguu3YD2vE-1of9jwQg2xlWGtu2JCIIyTKUjCj8_qF-4KqPd2ci3Gz4x7Edwts_vq05TYKiOlhygpeVN3dAzYHEE5h3iyLun0DZJHYOKRa6n_ANrbuR_MBI2z88eUUkft543I1C_ZEuHXDkLBQbTzai8Z4FECvVLZCjM8PT5EY3G4vTsgSxdqlUKok5gfFSJl9obozRh3pJ_EQyWTnWT9KIccniCCWDa3uh3AhyR4S--3Gj9LfSP0XRL6c4ojHi9h3tFVe-uSwOqx_H_tV8YGfuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=smgDQ9xPq_6mR4NZBYW3Jgi4AxmE_if-I7g0od5TF8dYjtz__lTGflsf2hkT0nguu3YD2vE-1of9jwQg2xlWGtu2JCIIyTKUjCj8_qF-4KqPd2ci3Gz4x7Edwts_vq05TYKiOlhygpeVN3dAzYHEE5h3iyLun0DZJHYOKRa6n_ANrbuR_MBI2z88eUUkft543I1C_ZEuHXDkLBQbTzai8Z4FECvVLZCjM8PT5EY3G4vTsgSxdqlUKok5gfFSJl9obozRh3pJ_EQyWTnWT9KIccniCCWDa3uh3AhyR4S--3Gj9LfSP0XRL6c4ojHi9h3tFVe-uSwOqx_H_tV8YGfuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
ایالات متحده مسئولیت مستقیم تحولات اخیر در تنگه هرمز را بر عهده دارد. آمریکایی‌ها از همان روز نخست زیر قول خود زدند؛ آن‌ها تلاش می‌کنند مسیر امنِ هماهنگ‌شده با ایران را دور بزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67985" target="_blank">📅 12:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67984">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67984" target="_blank">📅 12:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67983">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67983" target="_blank">📅 11:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67982">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L44TAiIx4tkWbciUhdwDK_1KLX3fw3pyPk1iGrm2JBQoO5Dal4At4dHFEvtl3J1Nax5O-QRiCiUgEKZeiFuSyBD-769EA1V3XLXo0W--XmmMOiTv9fEMoB88YaapmJqF3lGcC9FCawDPdXYg28lVUE_FmdAIfeXx5lEeQDEyvdERTA-KWLfwA7ttX2kace6VlrVNkC2nahFR7kdPGyGWdOi1FM-pVmU_ysw_qGBbOCNG-rv-CHDdtQP6Bngl7skYB5BbO09y0XX5dupv-Yr-5NxllG-dQuEtmyOZv04Tc6S2iy4h0O3QDrMYiQdusaEU4udCRPgzfINsQin1z4FDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ در تروث سوشال تصویری از لیندسی گراهام منتشر کرده با کلاه معروف:
Make Iran Great Again
ایران را دوباره با عظمت کن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67982" target="_blank">📅 11:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67980">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFHuKS_CxUEh3hOY2K_aZXGsdsX6vPcnZ7S32vWTAygrprRAZZPVlErKz7y0c9tccmyvBLZWzwuwSQQeMq_01B5DEt8IlriXt9jm31C_5bK0LE6VhIFPtWCV3f_3USDvCut0PPZ60x0M552WDvP7IHzInM3H92MQKK_EZCY9lnWVTDFMBkzwTxGBMDSxNVDHh7R7BL-IJvOpdvXaHDtHDnoUKuiawwGoM9G38FXD_yoyaUgYSDeONT0m6C5oeTqaAPr28_8tkAStglyA9isx4RUJoRuH-ZHuhj8NVaJYKCdxvNS3vydmcdUvGnzBvzGyc7JSjH213hRMzuFrdjkwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZAq7CagHnYLzVho8_yfqBA_lji4dFgrXb5AXCZwT_i0hGI4bVswV5bE-qyoR9L9MoVhFYaED8wJRiRwnfacmcV8_syNAvVrxNbSHZqvsOz8ZqMsG_T2yy3NeUqwliSV2pqxKsu8Qd-DZ1xz33ObzI2f6GV9pM9RwtIdFda8TCXPyl3QXtTQF9l38uURtRMuJ58lh2WEW-o43UFEwdFO5I6geVEVM5xkeeIe5Zo7I1tlEnM-Wss_dtlCWuwhuFKIFjpJ7tHXzB-YETRCTtHHgL-EsGz3ANQDu6j76JRhUE1oCz88Tf5P7FaE-JPElHPAWIiTFBYWVPOivTja3R30W6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
انهدام پهپاد انتحاری لوکاس آمریکایی توسط پدافند رژیم در بندرعباس.
آمریکا در بامداد امروز برخی مواضع نظامی جمهوری اسلامی را با پهپاد لوکاس هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67980" target="_blank">📅 10:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67979">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67979" target="_blank">📅 10:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67978">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67978" target="_blank">📅 09:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67977">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b2083eb1.mp4?token=MIxlqMk3A2rT2y05yzV3OA_PRDIKgfPnU1wT_Fls2Gs18sgMhUYlktMJsv_z5YBDOgu8m79LTEMeEIKp148BjEttdEQuFQbinjtyxKCFsOi-u6AXtrZmsLwJ3FI92rQFpyPDzLC9A7FRAwvAosrGOtgi54brIK42U_axOrviHaba43gLgPAdzU7yoyUICYB2MKxt16opgkqwfjExeXBiUDLqyynyBlTln2OLhqlftZDaglf90Axc4o57hq1Ddam0X9If3c4IgZhM-hPXWqSGc0WL-DBBHTyboxCTXDS5C3ln6pFCV7sKqCFj_012qXhNuvDVqDWR9oUAzAvM__DxXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b2083eb1.mp4?token=MIxlqMk3A2rT2y05yzV3OA_PRDIKgfPnU1wT_Fls2Gs18sgMhUYlktMJsv_z5YBDOgu8m79LTEMeEIKp148BjEttdEQuFQbinjtyxKCFsOi-u6AXtrZmsLwJ3FI92rQFpyPDzLC9A7FRAwvAosrGOtgi54brIK42U_axOrviHaba43gLgPAdzU7yoyUICYB2MKxt16opgkqwfjExeXBiUDLqyynyBlTln2OLhqlftZDaglf90Axc4o57hq1Ddam0X9If3c4IgZhM-hPXWqSGc0WL-DBBHTyboxCTXDS5C3ln6pFCV7sKqCFj_012qXhNuvDVqDWR9oUAzAvM__DxXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پهپادهای شاهد سپاه درحال حرکت به سوی پایگاه‌های آمریکایی در حوزه خلیج‌فارس
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67977" target="_blank">📅 08:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67976">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش‌ها از آغاز موج جدید حملات سپاه به پایگاه‌های آمریکایی در کشورهای عربی  @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67976" target="_blank">📅 08:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67975">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش‌ها از آغاز موج جدید حملات سپاه به پایگاه‌های آمریکایی در کشورهای عربی
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67975" target="_blank">📅 08:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67974">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/67974" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67973">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFkj3JhxATCsNXfNxIYg2ykr47OJ2CkPEzVenF_H2TPTECPAkH3zaf8ZR5EVxsBHMFeqifGaN5AxoZxHH8nA1OIBLpDMDvCsft6AmpTpP3xaTEeS8a0CH1HlAjcBCQ3j3Sqfala6INGa_gdOLRaTKDILy97nmSC4yXbMAT5ZO07bRNcMP3LT40q8_e3qWqmu9evdlJFM5gU6HW7xpS7AswYD-3J0ZWyh8VJbWoUgLwAGI2bumiZ6gLN1qHrKkseqabXeFpp_evBIxdNF2HkZs8acymGnBJY-6FR4kzYAhcK0ASf5W2X_m4wRl3inicY-WVsbSy9WX7atlFOiZmzr5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67973" target="_blank">📅 03:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67972">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67972" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67971">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
نیویورک تایمز:
مقام آمریکایی گفت که انتظار دارد موج بزرگ‌تری از حملات آمریکا علیه اهداف نظامی ایران در یکشنبه شب (به‌وقت آمریکا) نسبت به حملات اوایل همان روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67971" target="_blank">📅 02:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67970">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فارس:
دقایقی پیش چهار نقطه در شهرستان‌های امیدیه و ماهشهر مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67970" target="_blank">📅 02:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67969">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
دزفول رو چندین بار سنگین زدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67969" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67968">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67968" target="_blank">📅 02:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67967">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=vJP-2N_fnidagG822GoC5CYOmdoVffEtPqWxEFUqh5FyUrtn1aaxSQYKzp2X9Als7lAh1D7MtTo9dVednxGOj2WYRMTY41wjD-XFLT-Xfq1t-1t2ooHSppb5lH_dCkPCsGGV4nrXkAMVW-yijbOkwD-gmcrFIBKSyv-V7NcVANpxXIA_BYrDajDa8-LfwrRPB1ko-8hYMRYvD68AMoHaN1R8InQ1g2tNQo70zeECVfysq_HggNRlom8E1cBcVfR2uJBK47n8KGdPByfp2oaII4HsZ5KD9q8icbA9m0NxDVfyq_1xlKcAk0ehvC-gfk9ghBrU0Qe-TdNy-KOkOmZ5WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88de9c653.mp4?token=vJP-2N_fnidagG822GoC5CYOmdoVffEtPqWxEFUqh5FyUrtn1aaxSQYKzp2X9Als7lAh1D7MtTo9dVednxGOj2WYRMTY41wjD-XFLT-Xfq1t-1t2ooHSppb5lH_dCkPCsGGV4nrXkAMVW-yijbOkwD-gmcrFIBKSyv-V7NcVANpxXIA_BYrDajDa8-LfwrRPB1ko-8hYMRYvD68AMoHaN1R8InQ1g2tNQo70zeECVfysq_HggNRlom8E1cBcVfR2uJBK47n8KGdPByfp2oaII4HsZ5KD9q8icbA9m0NxDVfyq_1xlKcAk0ehvC-gfk9ghBrU0Qe-TdNy-KOkOmZ5WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال شدن پدافند در کرمانشاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67967" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67966">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=K4UN6D92xf4HabrmRk1rcjBDEjmSDMggPYLJe-3nmnSVWuYSDoiC6jNnO669GN-QBCwTDxXg5YVJ8CQyvn7azDHIhNLlxVI8bzEGu9uEdX9o9xzcJFp60mpsGABoNvXU82oIkLvlakhbeOAp5K-q1Ewpk8arkFPV1gq7Acc6uBsAslhRsFYU02eMKx2yThY-P0e_wEqct6p6sxgyT_LbpgHReq2iJIo2Wsm1uvpG9vhbXiOLKmMCbpik42ZGE7MWiAA4ha0T9pUVW9l7Rh8j2a3wRZZlZ_WE79lWD5NI_jitPGNzmEQYo460cvWnoUydBju8yS3_ombstdmmwEYnBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a15f1b4.mp4?token=K4UN6D92xf4HabrmRk1rcjBDEjmSDMggPYLJe-3nmnSVWuYSDoiC6jNnO669GN-QBCwTDxXg5YVJ8CQyvn7azDHIhNLlxVI8bzEGu9uEdX9o9xzcJFp60mpsGABoNvXU82oIkLvlakhbeOAp5K-q1Ewpk8arkFPV1gq7Acc6uBsAslhRsFYU02eMKx2yThY-P0e_wEqct6p6sxgyT_LbpgHReq2iJIo2Wsm1uvpG9vhbXiOLKmMCbpik42ZGE7MWiAA4ha0T9pUVW9l7Rh8j2a3wRZZlZ_WE79lWD5NI_jitPGNzmEQYo460cvWnoUydBju8yS3_ombstdmmwEYnBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویری که ظاهراً پرتاب ATACMS با استفاده از HIMARS در کویت به سمت ایران را نشان می دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67966" target="_blank">📅 02:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67965">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
حیاتی معاون استاندار خوزستان:
در ساعت یک و ۴۰ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه نقاطی در شهرستان های بهبهان و دزفول مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67965" target="_blank">📅 02:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67964">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
مسئولی در استان خوزستان ایران:
دو نقطه در اطراف شهر اهواز مورد حمله با موشک‌هایی قرار گرفت که توسط دشمن آمریکایی شلیک شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67964" target="_blank">📅 01:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67963">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
مهر:
معاون استاندار مرکزی در گفتگو با مهر حمله دشمن به مناطقی خارج از شهر خنداب را تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67963" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67962">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=lEtxPc2xPRfhb9YNt9VIAzwx70h3BdPRXaFDNcujwRkO2F3EWjOBPMeYIq6foJKO2j2jp8Mpay0xsnG01z09k3-eDSKEcoWWMX_R7kpSWEMtAmHx0cs3vhDGQ0K3T94pL5emR0gqZ7g1PJGWuHLZrHrSpH5ksJIbjzfSMMcblDdjIPABf9Nslr7pVEmKsN5Z7vLwR7yUPgmjaPTfTxSVNlJyNspODECuA23R-APvm6IxcczmEIxq2Po6LcctVw8GWyzCd-TyVsYalX3bWVC4HHByi6VQO5oFeuPCaX7KOG7vcTfjHernWDqdUvZaMtHqplQjXwtmd1GV1BLcnNqcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=lEtxPc2xPRfhb9YNt9VIAzwx70h3BdPRXaFDNcujwRkO2F3EWjOBPMeYIq6foJKO2j2jp8Mpay0xsnG01z09k3-eDSKEcoWWMX_R7kpSWEMtAmHx0cs3vhDGQ0K3T94pL5emR0gqZ7g1PJGWuHLZrHrSpH5ksJIbjzfSMMcblDdjIPABf9Nslr7pVEmKsN5Z7vLwR7yUPgmjaPTfTxSVNlJyNspODECuA23R-APvm6IxcczmEIxq2Po6LcctVw8GWyzCd-TyVsYalX3bWVC4HHByi6VQO5oFeuPCaX7KOG7vcTfjHernWDqdUvZaMtHqplQjXwtmd1GV1BLcnNqcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67962" target="_blank">📅 01:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67961">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=ls5ie52i0_0IPyKJkWORhB0C1FlUWuxNZO22cpiYWfyfKdsRNOJMGdNO0DOfoOexvOxlwySH6D7XvCzZYqe-hjb5deXn1hpBENqOoJ0GfTBWOuwrCsTFMGMA9MiA_E_QvOIZiXti5tfdRrUJEAvPKgPVNCmLN9tEREr_Mp1_nuW7cASgkSFu6SvtCM5pkOOMd8J5UEiyIT909X6rrKAEGC-xIli5m13q_Z0sVJiZmM8A2sEjCzWGSQwCCZOBEL80rdgLfUXCL5vT1t34icDbMdAePsxXo3yhQxQukpEnhV-SMSW4dP6ihjhnHKAcat6gX5hrI8vxip_TX5DehOp5ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d6d7e5a4.mp4?token=ls5ie52i0_0IPyKJkWORhB0C1FlUWuxNZO22cpiYWfyfKdsRNOJMGdNO0DOfoOexvOxlwySH6D7XvCzZYqe-hjb5deXn1hpBENqOoJ0GfTBWOuwrCsTFMGMA9MiA_E_QvOIZiXti5tfdRrUJEAvPKgPVNCmLN9tEREr_Mp1_nuW7cASgkSFu6SvtCM5pkOOMd8J5UEiyIT909X6rrKAEGC-xIli5m13q_Z0sVJiZmM8A2sEjCzWGSQwCCZOBEL80rdgLfUXCL5vT1t34icDbMdAePsxXo3yhQxQukpEnhV-SMSW4dP6ihjhnHKAcat6gX5hrI8vxip_TX5DehOp5ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منبع عراقی:
موشک‌های آمریکایی از کویت پرتاب شده و وارد فضای عراق می‌شوند، به سمت ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67961" target="_blank">📅 01:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67960">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYmDTHRZZkopDMbtQQyxuuw4EtyCZFSPGTlaUEZ7A88scdthSTYGFPpKv5pdHKId9KxU06wYFBB5Bbir8YurhFs9aJKNENKafE4aaJEwCSTPrfIh0s3bSR8fiaV54W7Je4WqQAH6qDgci4BpehYJQ2TWqLgfyR-mHRuQNruF-HZKZ-lbSzQy8S0aDo1dFFYu1RGEIMnYg_oV2YsVCQY26K3vrb_wU7n-QzMlYzGpEwdJc5ZHGQgrB3gR2jJA4OH2NQxM0WSvknF7SgzXIhaRfsLYepQ0w_hDouy5vEJQFOYHcShpyo2G4prKqvEeoRNWnrdd698qpYTzafV9O53L3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
ناخدا دوم تیم هاوکینز، سخنگوی سنت‌کام، به من می‌گوید: «در یک ساعت گذشته، نیروهای سپاه پاسداران به سوی شناورهای تجاری در حال عبور از تنگه هرمز شلیک کردند. هواپیماهای آمریکایی تاکنون موفق شده‌اند یک موشک کروز و یک پهپاد تهاجمی انتحاری ایرانی را رهگیری کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67960" target="_blank">📅 01:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67959">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
اهواز رو دارن شدید میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67959" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67958">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
گزارش های از وقوع چندین انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67958" target="_blank">📅 01:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67956">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi3uvZDXRBdtphJ2p3heRsL2QnGIkCnW3F_j_Z6ei3pInS5ASWDHQb5kPgUSbW335TFizDD7_RWhVjISCQdLwCI6875E_oRub8Z4G-MNcRFh-D8jteTzVMZ2PWtH84ZiK_g14MItQRJuY__16F9likw4KP5OZVW0PYwls9dJ9xNsoCoJ_0zexZtf_a1FqBrRUqUVCWlHdUHSleJv4NFwGvMePdaWgEpoJ8NfFDnjVq1vH2JsUgvLhAvnyiwmfjXRp7N5YolD3enjDe622pFBNwg1pdUgAZ2DQMguuOGi03Gr6g5CAfTGIcd3U69L5PV-eyHuzKhPA2_4SpaUy-2r1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=WBplD9HA_36mCDPTEIVwl7BobF32wb7YcAe_InRhQC7JTQCI6akWbIj_GM4N0lPz70ljKPmBl0AJBWmg90iVOeAW1MV6aUffy_1qyNXGC9fqjOifB2W49ZyB3FE2vIurcz95sTGbU0IZQxhh8eu3Qpge2wOD0ZotjEcSQImvyM7tMZcE700gObDbUKyzBGi2E9jIkeAhOQNm11JbOQJc1xQA5gKXTpqzfRe8zjEPmBYGgeUdqz4qPzDRhElygrMWQk7lQRirEdOuXv1WiX5k_vzLaeuZY3y1dKxR9uf2iAnDYhLd8PK7rb1g8CrXJAfyIlW4xay69I8bwhuuXMJn_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=WBplD9HA_36mCDPTEIVwl7BobF32wb7YcAe_InRhQC7JTQCI6akWbIj_GM4N0lPz70ljKPmBl0AJBWmg90iVOeAW1MV6aUffy_1qyNXGC9fqjOifB2W49ZyB3FE2vIurcz95sTGbU0IZQxhh8eu3Qpge2wOD0ZotjEcSQImvyM7tMZcE700gObDbUKyzBGi2E9jIkeAhOQNm11JbOQJc1xQA5gKXTpqzfRe8zjEPmBYGgeUdqz4qPzDRhElygrMWQk7lQRirEdOuXv1WiX5k_vzLaeuZY3y1dKxR9uf2iAnDYhLd8PK7rb1g8CrXJAfyIlW4xay69I8bwhuuXMJn_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تصاویر مربوط به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67956" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67955">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBeHrAd🇦🇷</strong></div>
<div class="tg-text">توالت + دکل = برنامه طوفانی پیتِ پرس زن</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67955" target="_blank">📅 01:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67954">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
دکل مخابراتی سیریک که هفته ای یه بار مورد حمله آمریکا قرار میگیره :  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67954" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67953">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
گزارش ها از انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67953" target="_blank">📅 01:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67952">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo-VKUFwDpar1FNpIpAMUnYJHXB1XDPOTUv7Nj3Hf0xJdxmBEqpqWGN6HWo8FjSJ8JVqjZu-r43tu4nfhWRBFBdhtKRhXV4GOnaU5ZnjYtnqTZ3MokYrmOvJP8UpxF7imFZybQusaDAoKx9dWRcV-ap4h3d5QYyLtdb2Y9Jzo2G9dz5lt0ycm2CsDBMKqmI0PnQE9iUgTpYzYy9I_edpqo9VURfUq6lBycC_UPcpDg5WPjjipaMtvo6yHmUd4_x90PXUxZ-RFc4ulmRzHsf8TVkGht4jzGLLdod2XqK5p47TBO_GuZujqlt2OgPo32fz9xv2K16ElbhqMBE0FaIutQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
9 سوخت‌رسان آمریکا در حال حاضر در حال پرواز در آسمان خلیج فارس هستند
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67952" target="_blank">📅 01:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67951">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWXa6q1g63sv210FBF-q6BSElv6DY5XdK6jOfeBrM3lW0Rc8yTJ2kAsuT87y0DbvSa67L3XyFoW1OVDq1tyfkGERbNg-LyObwJr-O1FoFqzFSMjITCxfZ9CC8HQ-QEb-4AiB24s2VRuXHJ-gq3j9DXyJRcX7DPgffXptoKfrdTZ7ki-Mx5YcdDnemt6eUE4M_1J2SDGbng4NFRyYKbb2DXk5WNHeYkWEnQMIJUjzU4Su6Y53yRHzvfuwepcjb3uQsjsRfkgYJXJb0yAvcrb0v8bE4FyYlq9rPpsZm-VAqOr9ASP5dobcn5wOZo2P9fJvbXBiN398NbOEc-6IcrpXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویر منتسب به انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67951" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67950">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga2d07X60IxOhoD5yGcJea16CIcK03PNr0mJ-7p6DDDzTSj4ygnCsOiIQ7KuJU_ud8O14TiDbpQRn4xmwiWhLBa5BicCXlmovPhoA9we5pDRTSX-H0NcvFR_Mtwiw8MqvNvekHyEtJHf6YfQw46atEu2P78bc_OGVqq_Ac9g1YOy7bHyNFBKPHTogn71qH9RZZw_GfGAJWShJTW7DCJofpk4ArMwqHzjXJoFiox8BTqYjVRJ9fySkqvhlNtM3kESih84S-kYxBGHpYJtAGQKl1NwCe717C_YGtydfQLJRjlroPwcRdkHO0SAVwt7kKtdfrFMaso0nBeaH9paMrgEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر من زود تموم می‌شه، چون:  صرفا حملات جنوب کشور هستند دلیل حمله هم حملات سپاه به کشتی هاست و این یه حمله ی انتقامیه، مثل چیزایی که دیده بودیم قبلا   یعنی در واقع حملات، کنشی نیستند و واکنشی‌اند  #hjAly‌ @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67950" target="_blank">📅 00:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67949">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
❌
دو انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67949" target="_blank">📅 00:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67948" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67947">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9jlJp39M6tmSFDBcx3e6mTcgcK136lC2VJfsKBzvNdPR2a9e2hon2qxiAWs96QCulAriiTG5uXATk4Rv7ZHlZxRk9tedZcVFZKnBpWUXVNnXiQSA-SQwPhKnu_ASiaqPzJm-79701CFAv_TpolYPsAZj00BbEKGgH2gQwAi_x0twkqLkng7Kmo9u6QEA9812kHEOI2c9gMXM_xj7P0E2PbztnPmQahXe8Bk7NVM-QBgrvbl0rdQ2EgpGEHJMLM3K_kzmED_KLC8lVxxQkalqNHatLgkMGS6rXwe0qPKDASJBTJ5-v9fU19221aBpwDCFz1fsYKHxJsnAQuwrpdIcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
ساعت 5 بعد از ظهر امروز، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به توانایی خود در حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند.
فرمانده کل قوا دستور داده است تا به نیروهای ایرانی پاسخگو باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67947" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67946">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSMKbovCm6as1fX_77oXjlzewVK4ppW3tBah3bxnfj8g98GFOSG2ImwESBKqsFXCfWLZik24AMO3VV1sIPx6OxznQhn_RJCqAjtI1WqPbGQ8kbLB3T4uqTRPNGiSMqdgWkPnIhd-mC5TSju9uDea46cfyXOtR_AFGl7VJNumt1ysSvkkdiiRKshJ0751dIEm7BVP9oMEeRSwkNHSVAQ6qacpKKFN7KMuMbof0doC-_YGLRcI47EnK-IBp1bBqLiCi0M-hE1EAhOiisDyW8xjpw10bn0lhmlvaubm-tQNY7qUyK8Q7QojLSrQtNJ1buly_NBeVZMrYYclYOWtgQ3hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67946" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67945">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇮🇷
ممد سامتینگ:
اگه نمیتونی جنوب لبنان رو امن کنی،
پس جنوب ایران رو ناامن کن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67945" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67944">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">Ah Shit Here We Go Again
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67944" target="_blank">📅 00:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67943">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
❌
گزارش های اولیه از انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67943" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67942">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
بندرعباس رو شدید دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67942" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67941">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به خط ساحلی جنوب کشور آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67941" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67940">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
پنج انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67940" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67939">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
❌
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67939" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67938">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
صدای چندین انفجار شدید در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67938" target="_blank">📅 00:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67937">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
خب مثل اینکه شروع شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67937" target="_blank">📅 00:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67936">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=u5H94EF4w9My4RsNCy6xb9i-Vg5uUaGy20Q0EUWJgBerMv2uUCBwtkifWU5Qpzz8b-1ieOe9ngAJmSZQbePDQr0aCJ2b_SwpJmlz-2SL1aLQ5sdczaIVovv4HAuO9-U_YYb_H42DNksD26bbtygfBhrmC8EqfKLbS0oX_JqpGUY-eEA00OlaSSNI6jAPegXA7_o8bUZQ38oPHneQpdhRWgRmqbM7Io5dYIieToXo9MkyBP38gD59xoxo4JvCp7J7nsmSXvywAScqpX1rhBfyEKh_gavPd1wNuFrEaPGeWUNlYmSRN6aDvJWm5gYJquagNGHgcv2t5bkzOuNBK2POJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce49929e0.mp4?token=u5H94EF4w9My4RsNCy6xb9i-Vg5uUaGy20Q0EUWJgBerMv2uUCBwtkifWU5Qpzz8b-1ieOe9ngAJmSZQbePDQr0aCJ2b_SwpJmlz-2SL1aLQ5sdczaIVovv4HAuO9-U_YYb_H42DNksD26bbtygfBhrmC8EqfKLbS0oX_JqpGUY-eEA00OlaSSNI6jAPegXA7_o8bUZQ38oPHneQpdhRWgRmqbM7Io5dYIieToXo9MkyBP38gD59xoxo4JvCp7J7nsmSXvywAScqpX1rhBfyEKh_gavPd1wNuFrEaPGeWUNlYmSRN6aDvJWm5gYJquagNGHgcv2t5bkzOuNBK2POJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Rip
🫡
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67936" target="_blank">📅 00:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67935">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwYYeEJCAWiJjOq3GcN4gq4luf43ANZdaS5G4sLSefadRKSTjdynQxMdMeOx1FyRjW_IW0Q5SJd9FneIW2X06GY2DXQhipP2a2gyq8PB5Oe0p3AGVOIs7qNo3U9X59I392fo1tpAVP0xyLSGjPfZ15b8UJ0b9YvepQvlwWw6aIhWzdge2RugRnxvGmGmdUddw4lNvTEm88iBoe9PZH7LnVfb5fbU4OPeaKTYZwdwVf2D3jKNnh2MEtohYMHzRWCvlfN9stRob0KCoN_MR7CjtK3oD2AHz5K50_4C7EjaY3rPDn0G50GVdZvrShDw5tGaE0rb9EKG2pvS5AhdUZhnbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
❌
ادعا: دستگاه تبلیغاتی ایران امروز مدعی شد که سه تن از نیروهای نظامی آمریکا در کویت بر اثر حملات ایران کشته شده‌اند. این ادعا نادرست است.
✔️
واقعیت: هیچ‌گونه گزارشی مبنی بر کشته یا زخمی شدن نیروهای نظامی آمریکا در منطقه وجود ندارد و وضعیت تمامی پرسنل مشخص و ایمن است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67935" target="_blank">📅 00:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67934">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=RGUxBLbJuhJQ11JfrXU32s4HB6b8gKN4mPEpNyOQKqDtwN3E3EyWbBUwwuB7qVY7E23eNnFo81I0cVtz5J8W3-Z4pxoHO7cOOKCecpbehMpNcAGDMhAEA5DIFphZuy0XZi0X0mdtnC-VRck2noLKyASPNdpwhXK-1nHU9d_yVWgTQhdGDMNDDMxCDvPV9yEaptZjjtNu75KuB5Qr2MI4qNExsEilc8HWxLNMENxJnogYRMYjQKNcllZkKvssk9qzgQqXt3apP1gj1UHaa8m40kCNqMuSbrOQrmJJyFfj-D4PoWxo0z5qITXABSmHCf_aENTdgU8wAuti4GXONnCd0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96a5b8a48.mp4?token=RGUxBLbJuhJQ11JfrXU32s4HB6b8gKN4mPEpNyOQKqDtwN3E3EyWbBUwwuB7qVY7E23eNnFo81I0cVtz5J8W3-Z4pxoHO7cOOKCecpbehMpNcAGDMhAEA5DIFphZuy0XZi0X0mdtnC-VRck2noLKyASPNdpwhXK-1nHU9d_yVWgTQhdGDMNDDMxCDvPV9yEaptZjjtNu75KuB5Qr2MI4qNExsEilc8HWxLNMENxJnogYRMYjQKNcllZkKvssk9qzgQqXt3apP1gj1UHaa8m40kCNqMuSbrOQrmJJyFfj-D4PoWxo0z5qITXABSmHCf_aENTdgU8wAuti4GXONnCd0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
‼️
سخنان قدیمی زنده‌یاد مانوک خدابخشیان در مورد لیندزی گراهام:
گراهام کسیه که به کنفرانس های محرمانه بیلدربرگ می‌ره
کسی که می‌ره چنین کنفرانسی یعنی از پشت پرده باخبره ولی اجازه نداره چیزی بگه
بخاطر همین لیندزی با هشتگ Make Iran Great Again می‌خواد به مردم ایران نشونه بفرسته
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67934" target="_blank">📅 00:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67933">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFKS4soZ1rEDdPfaJ0SYDs4meicbj5E_a44vaejJDcWqs510GyYHUAYvMXl1Mi8BebxOCdVBvsUh3MzfiMssDS9ma4UR170vjAk5qfF-jqAQaRdh6JVhmrRR4NIldtHXtQhjrPQT6S8s1NaiptaVpaydQz7QH7v5RWKt1P2GuxMxex-AJS1tQZI4TkzVoUyhFpoVVGfPVGFXVgyPITzMMX04T06qQi8CtlvWmIjvJIot-WqCvksKtl2R0E_XIIKcG4zK0jXVXsZYSW8Ute14X0wru9BBcb9TCZeW1ejI_qW4XZZUQFJWY7-A6rJiVZXBCp8hLcfGTJMtlruwbIPNxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال   @News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67933" target="_blank">📅 23:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67931">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tPsOk_Gv66QKN8tT1LzdfOQZaU0GUnAz9jG4tR_0eELu6q4d9OhGIeH9euOXGh_V5y83QsaD8wRUTPuiRtTnico8JfQQANtYeVwDktGmTX-LNE7bLu0oDFpuXWniJSRnM_pCgUMLd2sOZb5XkbUGti3iY-oZP6G22-O1KkdyygzW-HT7riRsB5zqC7hZWvqMyiN4HxOQ8EwYqVZ537A6hiF5UrqidkFCMEOTlKZX-wqqtiLQhhotk49_EHVNK04bM4WyAWA5kru6g0Ab2gImVGH_8MAc8hu95D1tS5HdLewXocvxt1SpLFZqSe2EBNE64M-N1iUgG5cF_xENIa1aSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gu9ljAhnfSXjXApCsFXXpO6t0zFCakWwTIZwj72bd3jmV2KBjt9w2Rs1udnd2kgGvZYtGNWNFrKL7PUK7XRJcb01fxtItyUUrziaIoVUu39-TwAuzhAs9XvjSK1fVLwKeOA0Qle_lLqRhX75AdNiitsHSErW-l_SynSRu7MdIX1hAP7mcFYoV3OhAC2NmcADQApTxzfYrUjHXANxJBG-B8N6R9O62V5RHdVqXSIexOFVlW4sKFP7MQhvJdNR1zY9gbIib-XIFPhhE7da73ecm8SIBAbevYendVis0jVvhY9QNFYnI9P_5zXvYi91suviFf-DZPk1RqPQpbl228UNtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67931" target="_blank">📅 23:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67929">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XC15fzkFCvMhw4bvk5qzuyFDQBVVLt-qgBed5DiOEAeVUjK8BlG9qpGQYDVP36SBuNZIuZZEQwVQbiuPOiJKooONnIzSIAV0vzQEpGoHOuhdrBS3KDe9dJwqo9BPh_D3l6SxoPZHr65H9TxSHBMjCYBF2nLkFE6nWEvsh5pplRVOXIdmpxw124pNBQy0pNeOGsFOtCcFlDGS8DYuEUs5RNRdct3m1NQyMUEo4wlGL2jiaUXpHmTBPoJWjVUCm45IKHuDwk80XzDQyI1_eU7vhdK938Qcjfryk68GDh5hNVyN5PDSsvwsL8JPzwNaj-uke_gvnR8J4H4hZeckSbNSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peHzBXJ-eOC84oZajqmIN0mIdvfCOSI-21j2M3zv_Envpa-YCSAD1_OZAYcqJ_veHdAhe3Gcf6XRR_g408MNR4-UdNCE_t-7TsWN0C5LdXMASerlgDKzWPSCvbm_w9NplUzoNCL3B0_3xMeiEuEqqns6H8gRUj4WqvAg630AUMm2L93gUbv0JOd2lg-GjbLXO8qrxA0aeKvXbhsEJ4NV-i2nn3DPQPcMdPKZZIrXPNI_cLzrd-w-HK0KkJyfMDtCU5Nh7eBHeiGntCXSj-bhiGh9ss4FbOOwhJFSky0ncy05SJFV2V8buVPV_OTBXT4ZKkdUjrKpmEP39opbFDM85g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
🇷🇺
لومر، خبرنگار جمهوری‌خواه: ممکنه ایران و روسیه لیندزی گراهام رو کشته باشند، باید تحقیقات صورت بگیره
همچنین FBI هم وارد تحقیقات شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67929" target="_blank">📅 23:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67928">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=B4SPqNzf9QLdhhsmSnBbBaL-aVhCt5ZFaXzJXLBmXKI1cfE2-14E0kjXahpAT0JFrqv7KNWhIqlWnAF9p5QEUD94ui9Yan9RrjLe1u3oHOu0F2X6YoW-Wc7shnxZpvXUZm150RFVV5nMdm3yR-ekY36q5dAxcBu6kh-Pkn6YqSmW3dsvbbGHw7aVyUEPthV-8dWdS9srX_X35kSxZAhWTeitZWlVI6GYF-wuYseGl6PxpOmpyPGTLPPMM3JmXytD9n4uGe59XD1Yswx4ovPv-OJLqptFqk2UZZ27zBi-CZ8jS50kX5LH2aXGaTuILZhipjUNxmCCtdy1fz5RvVyaug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7a73bd81e.mp4?token=B4SPqNzf9QLdhhsmSnBbBaL-aVhCt5ZFaXzJXLBmXKI1cfE2-14E0kjXahpAT0JFrqv7KNWhIqlWnAF9p5QEUD94ui9Yan9RrjLe1u3oHOu0F2X6YoW-Wc7shnxZpvXUZm150RFVV5nMdm3yR-ekY36q5dAxcBu6kh-Pkn6YqSmW3dsvbbGHw7aVyUEPthV-8dWdS9srX_X35kSxZAhWTeitZWlVI6GYF-wuYseGl6PxpOmpyPGTLPPMM3JmXytD9n4uGe59XD1Yswx4ovPv-OJLqptFqk2UZZ27zBi-CZ8jS50kX5LH2aXGaTuILZhipjUNxmCCtdy1fz5RvVyaug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خرگوش نر به تازگی جفتش مُرده بود و میخواستن وفاداریش رو نشون بدن که اتفاقای جالبی رقم خورد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67928" target="_blank">📅 22:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZbMUUC8mXnQ84n1sirDludJVDlRzIJdNpMKfhUDDnEu2dyNOIMs_pFb0LbC5wwOzz53UWC2ykrUlMGjmGHr2Rb4sjgRIZaFkWwCeUpL1rgHWve24t6iUYa1iiLwDKgucbFfC5IdOtiroIda9DrL-CWqNZbRXsLwEz52AzrCGsKJ4ajJC5nPyxnVt1BS_A4taPfsEOlTTGpOlMN73y0d_bpH9ZeDcYGfjU7EMqbo2zKnbSOLu3n9xaW8IHKJjyDNAyMTdWSvMsUdxhYNszDHBRooN_Zx1CYggsqxon3aw7JWQlTGRxENfYnrV2LmQshXUooJHSljGThOOVe4mum9_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه های عربی وابسته به حکومت؛به تمامی شهروندان و مقیمان کویت، بحرین و امارات متحده عربی:
با توجه به وابستگی حاکمان شما و استفاده از برخی مناطق مسکونی در کشورهای مذکور برای پرتاب موشک‌های زمین به هوا به سمت ایران، از شما درخواست می‌کنیم که نهایت احتیاط را به عمل آورید.
در صورتی که هرگونه سیستم یا سکوی موشکی را در اطراف محل سکونت خود مشاهده کردید، لطفاً در اسرع وقت منطقه را تخلیه کنید و از نزدیک شدن به پایگاه‌ها و تاسیسات نظامی آمریکایی نیز خودداری کنید و از تردد یا عبور در اطراف آنها اجتناب نمایید.
از تمامی شهروندان و مقیمان درخواست می‌شود که این مناطق را فوراً تخلیه کرده و به مکان‌های امن دور شوند، بدون هیچ گونه تأخیر، به منظور حفظ جان و سلامتی خود.
پیش از این، هشدارهای واضح و مکرری را به حاکمان شما در مورد خطرات دخالت در این مسیر و درگیر کردن مردمشان در یک قمار بزرگ با سرنوشتشان، ارائه کرده‌ایم.
با این حال، آنها تصمیم گرفتند که در مسیر وابستگی کورکورانه پیش بروند و تصمیمی بگیرند که بازتاب اراده مردمشان نباشد، بلکه از خارج از مرزهایشان بر آنها تحمیل شود، در غیاب هرگونه حاکمیت واقعی.
بنابراین، آنها مسئولیت کامل تمامی عواقب ناشی از این مسیر را بر عهده می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67927" target="_blank">📅 22:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67926">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_7PyQHUINwZmshRfKIUaN0565gYVyNPe1e5mYlURSByBAmrdqAoIN6XXkZ8gS-k1Ehds4o15wH2uCiHGI0KN6y4FTHxTQ3P_xCOfzYYkDTBJukd80N1-9KEErAvEj-MA7Fbmu2NnND3AWy2W647njXqqR2T4W3D1hBD9ehGZymbU0ghSiuxowJqPMkqJzjeWlb8s9ldeuasM0M4qw9WVdVa1ky4Tx-AiaButKnntE588TwBhuelqrV5qJSw4aXKROejbpq6rkqDC-y1KXezc4-eEuaO8nIzzabfXAVcxAHsEuPmZh0k6Us-wo7Mf4sG9D3Qu74oIgLjLNsRCOsutA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آکسیوس:
اندکی پس از تماس تلفنی با پرزیدنت ترامپ در شامگاه شنبه، سناتور فقید لیندزی گراهام در گفت‌وگو با فردی دیگر از وخامت حال خود خبر داد، اما گفت تصمیم دارد مراجعه به پزشک را تا صبح یکشنبه و پس از حضور برنامه‌ریزی‌شده‌اش در برنامه «Meet the Press» شبکه ان‌بی‌سی به تعویق بیندازد.
وقتی به او توصیه شد فوراً تحت مراقبت پزشکی قرار گیرد، گراهام با شوخی پاسخ داد: «الان نمی‌توانم بمیرم.
هنوز باید تحریم‌های روسیه را پیش ببرم، تکلیف رژیم جمهوری اسلامی را روشن کنم و روند عادی‌سازی روابط اسرائیل و عربستان را به سرانجام برسانم.»
سناتور فقید لیندزی گراهام تنها چند ساعت پس از این گفت‌وگو درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67926" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67925">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=aEzO7U9-KppynMuYMB8-swd4o_nPed2I9zedeZoJqhkj4t6VMRuELHM6n6UnyzQqvEs2jPWwyitfmSx0suCUXYXHr8gR23qvnwgKKBll4uEU0SsfW4W5yPvM16LpzFmUxnTGy5SbblmSUubHJ6Rnk3ZdhO4M-EEfTStV2iur5xaOxMtcH7HZIzsJa5XO0sJ1W4YYyzEsIDRuxqUEw2pdapHlnS8j2MhgQgJGRkJBVLRebBTtut-f3X0xO8b5spqN4xxib4nm0nFmt68RiM5nHXp31VOPAR5OTomh8luK8M1e6vsSdyLcDHnPt-i3feUBs-8QYjBXZGhujhxsEJw67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b34de9065.mp4?token=aEzO7U9-KppynMuYMB8-swd4o_nPed2I9zedeZoJqhkj4t6VMRuELHM6n6UnyzQqvEs2jPWwyitfmSx0suCUXYXHr8gR23qvnwgKKBll4uEU0SsfW4W5yPvM16LpzFmUxnTGy5SbblmSUubHJ6Rnk3ZdhO4M-EEfTStV2iur5xaOxMtcH7HZIzsJa5XO0sJ1W4YYyzEsIDRuxqUEw2pdapHlnS8j2MhgQgJGRkJBVLRebBTtut-f3X0xO8b5spqN4xxib4nm0nFmt68RiM5nHXp31VOPAR5OTomh8luK8M1e6vsSdyLcDHnPt-i3feUBs-8QYjBXZGhujhxsEJw67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کانال 15 عبری:
ارتش اسرائیل با همکاری همتای آمریکایی خود، در حال تمرین سناریوهای مشارکت در حملات علیه ایران است.
ارتش در حالت آماده‌باش دفاعی برای مقابله با سناریوهای مختلف قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67925" target="_blank">📅 20:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67924">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: امشب به طرز ویران کننده ای به ایران ضربه می‌زنیم
👎
خبر بالا فیکه و ترامپ با هیچ رسانه‌ای چنین حرفی رو نزده
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67924" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67923">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
❌
وزارت دفاع کویت:
۳ پایگاه مرزی زمینی کویت هدف حمله قرار گرفت.
‌همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت هدف حملهٔ یک پهپاد قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67923" target="_blank">📅 20:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67922">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ts9RW5-w9kcxx-Ca8ZlgC5GK5snECCpQJGG20QMLiliEZCNIC_c2rSeP8nz1eFYo9n71qaj2XjXbEflN4Z5YeKiAmBhdAPT7hIX8BXrPMuCzemTas9nUl6JaDPgwS6simzi7uFBlQPYHiEIL0YMlTn22oSjWamRKVJm4DMfmyTgmZHmhRIkO-q30_hzR_-qIZUmhrPaPgIsZ9c6mbMMGVMHbZe4shLm8pzJOQu9oBcTLRJQ20cKUi3wA1o5rtVKf6G0GW1Be5pfW7itNvB-7xZAxiT2DcWagqoLcj7nOZs2NT1ejFobeODkjY__kmrwEabA3Sf4anFQ9ZzvkuYGf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
ارتش ایالات متحده چند حمله را علیه سامانه‌های موشکی و پدافند هوایی، و همچنین قایق‌های کوچک متعلق به سپاه پاسداران انقلاب اسلامی در چند نقطه در نزدیکی تنگه هرمز انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67922" target="_blank">📅 20:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67921">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
فارس:
خبرهایی درباره کشته شدن 3 نظامی آمریکا در حملات موشکی به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67921" target="_blank">📅 20:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67920">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
منابع خبری آمریکایی:
یک حادثه امنیتی بسیار جدی در یک پایگاه نظامی آمریکایی در کویت، پس از حمله ایران، رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/67920" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67919">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
منابع امنیتی به نیویورک تایمز:
ارتش ایالات متحده، مجروحان جدی را در پی حملات اخیر ایران، به بیمارستان پایگاه رامشتاین در اروپا منتقل کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67919" target="_blank">📅 20:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67918">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQzyegflpBVLz8WAVyUhJa-E6QhTrhSLVNfUMXF2aqO3rT24L9tBbGlf8uoZTFXlP6uCS-ZlO2q9sJpTkm00sPZ0mVpZL8INwIjMzxO_tmxIk41sg2b8Qc3YnH79c8PSD8jYG66UtnMy9cxi2oHSz7hIIDYIlyLNgNGdjm3bcXXSINZ-wT-u41H3tTPm5Tt_xK3GpmCH_NvZ8CCdqdXA63jWhVBd6BXjPqk6m3U9O6xSvcS-kMZDqR_w-WMrz6AYeMZwJ0V5C7PD2Yk0YZZ-SIySXRJY2Ua6rVAMz3kHvjVix-r0tOF_OlpBBKvXb5nVfxHrNa554t0_8XNNzjBBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قشم همین الان
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67918" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67916">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=LrK15aNCAlYZ9eCe5oxyZrCaK-xQ06HEI_A4oYoJtg10o7J8V2Mo2xXJRgpr_sB-ldOtNXwmdrbmkE2EJMOAjUygHuXePNZL3DNjf3uyHEgTQTUz8KK6nubnqsDaN69qFlC6uwsLSG4qzP3yh7fA-MvxBTuLcIJ6fIXqff3i3qOvwFqnmPYocrE5zjoZeCVclXREv4G4rtqrL3sTVtz3oI18oktyp5bQSMAKKLDit_37rrGvhWvrlEQD_Kl-tOe1lDEAQbqsIbkLTe0mUWVy86liLqTIC0NZ5CBKEA05XefIRIiBW73c8z3JUirk1OpANUQF32M79NcBfo8DJMVy2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c182d343.mp4?token=LrK15aNCAlYZ9eCe5oxyZrCaK-xQ06HEI_A4oYoJtg10o7J8V2Mo2xXJRgpr_sB-ldOtNXwmdrbmkE2EJMOAjUygHuXePNZL3DNjf3uyHEgTQTUz8KK6nubnqsDaN69qFlC6uwsLSG4qzP3yh7fA-MvxBTuLcIJ6fIXqff3i3qOvwFqnmPYocrE5zjoZeCVclXREv4G4rtqrL3sTVtz3oI18oktyp5bQSMAKKLDit_37rrGvhWvrlEQD_Kl-tOe1lDEAQbqsIbkLTe0mUWVy86liLqTIC0NZ5CBKEA05XefIRIiBW73c8z3JUirk1OpANUQF32M79NcBfo8DJMVy2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به قشم
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67916" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67915">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🇮🇷
نایا:
نیروی قدس سپاه پاسداران انقلاب اسلامی، کشتی‌ها و شناورهای آمریکایی را که در منطقه "کیلومتر ۲۰" در تنگه هرمز فعالیت دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67915" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67914">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67914" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67913">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmDzmNruHGkkQF5Se7lqi-0EvJiRFDn6hlzIHUmCuNRl6wFoaqV9VBbNgB5G-rWMbLH7bVXGdAjQ6eakh4TW0nNo2Dgm4CDhfoXpFBm407YUMF02_IZ9fc0LJRSkyYiRZYRZ-5k1kOtC9e6qN0MuLhzlWxEmD87o9X2H6os8M2hjLK16MrHPdIqSfOZXHtc4f3_9lRoxPzOaIhzpqx048jfKJOqdudvQp7lv52IVqtLyItF-Q7eMLikUwBOT6IqxDK2IOTt4J-vr0eLiGZosiEfrm85ax35EyGQhzXrsCcAuLJcBAl_1qo2-hgedOASQgPZldJGMYNOt920J79SxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تروری که روزنامه همشهری منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67913" target="_blank">📅 19:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67912">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=meb-eUF-jp35mEPJszyon61ztKavrqs_41bEq7oxMxW3hLLJoR8Jj7ax0WLeFo-izu7MpYWB0rvld-jrvU3XwvfqG2YEcF5husdtgYMvvFwyte__Dyzk8DmoKPHg9T6MtPCTtIUWxGfV_LjxqfYo42D1Jj-138w55oaTfNeA6dJBMX-oGLCOyM2A5Z4G7kdqogacU8hezbFdH_3zdMg343_4Nx1dSuPP9zADKLFt7E_hZelCm2DPX39o1uSAGh8DV7EIAx8w4btgpzRgnxYiQ7Kbn0a3eSkPETBKcPUERDHbT2j-IlaTfpVpLlrPOtC_hc25zKxfhio3Sh0otts5iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491f5ab181.mp4?token=meb-eUF-jp35mEPJszyon61ztKavrqs_41bEq7oxMxW3hLLJoR8Jj7ax0WLeFo-izu7MpYWB0rvld-jrvU3XwvfqG2YEcF5husdtgYMvvFwyte__Dyzk8DmoKPHg9T6MtPCTtIUWxGfV_LjxqfYo42D1Jj-138w55oaTfNeA6dJBMX-oGLCOyM2A5Z4G7kdqogacU8hezbFdH_3zdMg343_4Nx1dSuPP9zADKLFt7E_hZelCm2DPX39o1uSAGh8DV7EIAx8w4btgpzRgnxYiQ7Kbn0a3eSkPETBKcPUERDHbT2j-IlaTfpVpLlrPOtC_hc25zKxfhio3Sh0otts5iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
دقایقی قبل از فوت سناتور لیندسی گراهام با او صحبت کردم و "او به جز خستگی حال خوبی داشت"
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67912" target="_blank">📅 19:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67911">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
حمله موشکی ایران به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت.
گفته می‌شود این یگان در حمله دیشب به جنوب ایران حضور گسترده داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67911" target="_blank">📅 18:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67910">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=DJ98zl8An_ModWao-iGMvD182bEoGcwLT5kEd4E7-v43NKDmfxnUmrqpGi0WtoAQ-PaJBqel03gs2aFsFz49_nhwjPh9CVKDYk5rOjcEk-qiHMbFTGoxjHFGaMhSR7RCklyLl_QJ1X61fS72sbSk360cpxcg4FjEmO9bznROqGXKgZnIyoG3evG0AJsaWJVxNwU640J-b8MnEwGSKcWwOnciHf-dVyAiQSnoa62i8UQehkhFrc0TA8sdUrwNH39KR9kpmTJAwjnw6WBgONAUrp16okpOLxdgD6CPLo0eZ8XJRDuUfqwM0Gw9sonPCLyJjaVFkkqxqKjLLOeOEhokxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb024df7a1.mp4?token=DJ98zl8An_ModWao-iGMvD182bEoGcwLT5kEd4E7-v43NKDmfxnUmrqpGi0WtoAQ-PaJBqel03gs2aFsFz49_nhwjPh9CVKDYk5rOjcEk-qiHMbFTGoxjHFGaMhSR7RCklyLl_QJ1X61fS72sbSk360cpxcg4FjEmO9bznROqGXKgZnIyoG3evG0AJsaWJVxNwU640J-b8MnEwGSKcWwOnciHf-dVyAiQSnoa62i8UQehkhFrc0TA8sdUrwNH39KR9kpmTJAwjnw6WBgONAUrp16okpOLxdgD6CPLo0eZ8XJRDuUfqwM0Gw9sonPCLyJjaVFkkqxqKjLLOeOEhokxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کویت کمی قبل
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67910" target="_blank">📅 18:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67909">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLFSwWIOYpEzD-Rpc-cZsLsduYerFPBblaAn7TxfcKm7kWKnaiANwCSJdjhQAjQfrbcD3j3lq08q-RNlQILIOIra81pNKFjya3RybtwXq3QT1ZG7mv8ziEAQ8VX_TJyeh5nhsPKaJlliy-EVj_j4vFdxDKWovtOHZOrG_Z8pUuFpxkpt-bWEecsy1afHyGMeJqNKszqzYwv4CYGTrAld1wwPoSpZwUuW9LqoYqmCuEf8zgYXx05ZZTTHeaHXo3NxtHYqGYAKK3wPQHNefKXq7D6LeoYVBkq8DgjX5xCYSvEToVpFPVIK8c6QyubAbAy_snmBiGov-L-bTmlrUPaVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
دو انفجار در کویت و برخواستن ستون دود
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67909" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67908">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=YF3xt-MfV8I9UW5PBaoai70fWtOJIpA3NFygK9uBTYfDg531qK-GSTlSbataYdHfbEaJdcnxU41EcFtarMAgstOFyf0vepO6v6PtfLL18DSk3Rzb1c-d5mDu7AEd13jibZi60iQBAp4OlkadskzD9j5-cqR64xAR8XN0q-of66HEYY-JEPjhtjRHJpas_kyQLXUCJVYOj6j24zBDta_BR24jjWVg2YiuKGIBgWwupgbGrhVvFLYr9xVDk12M8WH8XB5VZ-4It2imUuSjP_2JV_4XsI0vm70NLDBuGV8jFUihQVskfA5gRrTIbpg3qOaDKgFlFugL4UMZh_MYigftVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09b038fd4d.mp4?token=YF3xt-MfV8I9UW5PBaoai70fWtOJIpA3NFygK9uBTYfDg531qK-GSTlSbataYdHfbEaJdcnxU41EcFtarMAgstOFyf0vepO6v6PtfLL18DSk3Rzb1c-d5mDu7AEd13jibZi60iQBAp4OlkadskzD9j5-cqR64xAR8XN0q-of66HEYY-JEPjhtjRHJpas_kyQLXUCJVYOj6j24zBDta_BR24jjWVg2YiuKGIBgWwupgbGrhVvFLYr9xVDk12M8WH8XB5VZ-4It2imUuSjP_2JV_4XsI0vm70NLDBuGV8jFUihQVskfA5gRrTIbpg3qOaDKgFlFugL4UMZh_MYigftVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=aTmhO8OV44k21hW1bfjXTvqaQ5uV83lq04S2VEzpyC2YMp-L9eRsPkWKSq5R0bmIxqPhG_KyplSVWwz38vfvSBm5SRTve3_wdcr7Horj5gqQUlQVOYlhiirOfQ4JGewppKBwTluEwC3uJM7GQCwxf4UllU_nEyDy9lfmOj22WcDYDfwZtItzYURtfIECBuf1oReeg8QnGz78AV5rqUCL9MWT_rS1ej9k2AYBNlQHuPcnHEsXlca02MtMIdVr-duYG-adn_FPyDHWEtMUjijX_XB0fV3qOGaQ3abnrvSjlDMVDIAr8oUFPiUIUTd-25YNDAbQ0Noo6UBn60dQRwg_ygfxpzbzU6hc89-qz2CZilzMSIozHtdf6DtbaI-_aDAau2KSHs72uwT89uRFSNR6mpN6e89OqCDbFnL12h2ZvkR29PLilWgrQEkaTy1CL3wc-9b3SwZHNJsRREN8onR7MyP6f3iETE5EIDmlIa1rv5S8oRzUf6feJ7RXrZSxdVrt-M68Kkeg2n8P3yho7f_hHqZPB37UmO1W1WlkpPrZajlOGO3ti_FdDiG9tUVTiy6zobCLydPH9j4JWZrOv-Nz_mca5mmoiOpiyamAixQxe4GsZIlcZhddaadUeshGuQGYePuJ0FB9u-Dvc6ol0w4g_EP3PVxbmPeaktIwfEjOURE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/550c5fbdb2.mp4?token=aTmhO8OV44k21hW1bfjXTvqaQ5uV83lq04S2VEzpyC2YMp-L9eRsPkWKSq5R0bmIxqPhG_KyplSVWwz38vfvSBm5SRTve3_wdcr7Horj5gqQUlQVOYlhiirOfQ4JGewppKBwTluEwC3uJM7GQCwxf4UllU_nEyDy9lfmOj22WcDYDfwZtItzYURtfIECBuf1oReeg8QnGz78AV5rqUCL9MWT_rS1ej9k2AYBNlQHuPcnHEsXlca02MtMIdVr-duYG-adn_FPyDHWEtMUjijX_XB0fV3qOGaQ3abnrvSjlDMVDIAr8oUFPiUIUTd-25YNDAbQ0Noo6UBn60dQRwg_ygfxpzbzU6hc89-qz2CZilzMSIozHtdf6DtbaI-_aDAau2KSHs72uwT89uRFSNR6mpN6e89OqCDbFnL12h2ZvkR29PLilWgrQEkaTy1CL3wc-9b3SwZHNJsRREN8onR7MyP6f3iETE5EIDmlIa1rv5S8oRzUf6feJ7RXrZSxdVrt-M68Kkeg2n8P3yho7f_hHqZPB37UmO1W1WlkpPrZajlOGO3ti_FdDiG9tUVTiy6zobCLydPH9j4JWZrOv-Nz_mca5mmoiOpiyamAixQxe4GsZIlcZhddaadUeshGuQGYePuJ0FB9u-Dvc6ol0w4g_EP3PVxbmPeaktIwfEjOURE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
یک فایل پنج‌ساعته از مکالمات بی‌سیم نیروهای سرکوب‌گر در اصفهان به ایران اینترنشنال رسیده که نشان می‌دهد نیروی انتظامی با مجوز استفاده از سلاح جنگی، در ۱۸ و ۱۹ دی‌ماه با کلاشنیکف و وینچستر به معترضان شلیک کردند.
دقایقی از مکالمات نیروهای انتظامی در بی‌سیم را در این ویدیو بشنوید.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67906" target="_blank">📅 18:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67905">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=KPmZ559qD1sclqVXUMo4wyBNEEp4oK0n8J0Sn459s9Fkjyf5vdk8ARzVezWNLs_2hNbw5KD47hUSM4ii6vuQ2HqdIPnc12hqcCMKZKsLKOxLU1Z0lRaDFb-pPQDYQdhEzYc6HEdljn7CbePD9LFdwtNEmHfTnDkmehRXOibddy46MFO9tHdCgNgy9pH5C8nlmVldcDZz_pH6Lchh_yqgLjLLkpSzMkd6IaYX91pFSGa-wVPksjwlPrGhLmfnMBCYacV8hTEXrB-Jx9kLmIqYorpFGEZW2khMLcqclagnfB-W6nnBrFlhk64H-i-Mndnh0UYlwSC7C2Jzfd8j0P20Y4BdW4VtKeYX7mT61Gtr8jJ_TMU4fCxWCjVugxLTD26c_WXMF7508AxcNEsFixk1VyOnmPNyFOK81Si9py-nPJ4XMoWwcmnm7ozBvmTLD3gTZV437X65_3f0_BMGDsZaVHAq3lth8nHwu6L3A5mKN1HLRIBBA9I_bmRCXnOsjfpT_899BXSXqdzRQdbsT3XudBZ4yyQRBl0XDIQXDLnkvnGA1u7pvNisFfRm8aBRopkQQXZHzk6ze6MqqmscPKDa02_FL2P2lJd01Top4-RdBtobDRya798OEqcdxFQcalaE6Qd0gie904Rn7nNB5X2yKcT4IVTrP7Gwi_PVntzBF6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f43409a1c.mp4?token=KPmZ559qD1sclqVXUMo4wyBNEEp4oK0n8J0Sn459s9Fkjyf5vdk8ARzVezWNLs_2hNbw5KD47hUSM4ii6vuQ2HqdIPnc12hqcCMKZKsLKOxLU1Z0lRaDFb-pPQDYQdhEzYc6HEdljn7CbePD9LFdwtNEmHfTnDkmehRXOibddy46MFO9tHdCgNgy9pH5C8nlmVldcDZz_pH6Lchh_yqgLjLLkpSzMkd6IaYX91pFSGa-wVPksjwlPrGhLmfnMBCYacV8hTEXrB-Jx9kLmIqYorpFGEZW2khMLcqclagnfB-W6nnBrFlhk64H-i-Mndnh0UYlwSC7C2Jzfd8j0P20Y4BdW4VtKeYX7mT61Gtr8jJ_TMU4fCxWCjVugxLTD26c_WXMF7508AxcNEsFixk1VyOnmPNyFOK81Si9py-nPJ4XMoWwcmnm7ozBvmTLD3gTZV437X65_3f0_BMGDsZaVHAq3lth8nHwu6L3A5mKN1HLRIBBA9I_bmRCXnOsjfpT_899BXSXqdzRQdbsT3XudBZ4yyQRBl0XDIQXDLnkvnGA1u7pvNisFfRm8aBRopkQQXZHzk6ze6MqqmscPKDa02_FL2P2lJd01Top4-RdBtobDRya798OEqcdxFQcalaE6Qd0gie904Rn7nNB5X2yKcT4IVTrP7Gwi_PVntzBF6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از  فعالیت موشک‌های رهگیر پاتریوت بر علیه موشک‌های ایرانی در پایگاه موفق السلطی اردن از دید سرباز آمریکایی طی درگیری‌های روز‌های اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67905" target="_blank">📅 17:15 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
