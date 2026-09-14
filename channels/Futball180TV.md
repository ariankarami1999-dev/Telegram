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
<img src="https://cdn5.telesco.pe/file/vfKDy4JEPy8xOQ8t3VzYRK-qkZiUSIY_IWyNpqFGyyXfT0vTuEZFVloZD9JU6NCGBtAHyM0DO-2t0CNZMGaJZByzN8n1_Mjx09JuRGe5CpHOfsk2yxePHtSPkR9CJBW77nmUduE59ppeu4odSvxUQHmzqSvSQd8MhngKq7piaNyEEGg_4gv8X4Y_blA1l33FmIIyfqmh-VwUyD_xAWa0JQi6r3vn7UgRkBFSUyv8N2g3O5l_AvXzlxOo-h7YXaRkCQvNiQotJ0N0QFTB44xcKdO9zPyeJb9vd_NPCjsvLtTOlOlUa56JNQXddJTEol14rCAeUvnHZu6P6bGfp8ukXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 414K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 11:50:28</div>
<hr>

<div class="tg-post" id="msg-106422">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYIxSsW4XsxAjNrML9H9ZmoMa3Ts4iFC82heSdTyZ-i5M5S0gA99CT1tSLXlvq98utH_Y8zttaizQjdYArwwTTfQ61D2nOjw9w7WZv8q3e8BrllrxgkXvG0OdxjvilNDDYhw7tzSmt_oNVSSPpOhjEQR9-pVJoxri9nMoo5zlhTL1sHpRa86Fc4lmXXmg6EgOuHVS2OfrPDC0e5F86Lh9lUhfhzHWrdoYZkyb08p1f_pFlFjdey9N2LhgpRrIv7hgtwsHrF3I_Ol60QbPB-TLSWN93zh8Xr7SIPVZ0basO0AUqA1e_otuAv42rky9IWFImKZx_cVPqBXYUJhvBX75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🟣
پوستر باشگاه استقلال ایران برای بازی با السد قطر با تصویری از حردانی و چشمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/Futball180TV/106422" target="_blank">📅 11:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106421">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285c0d29ad.mp4?token=l6acPDY_J5HB9XFyWZ6Y1eBdUM0xu_UYOV9YezsxbkavIDylarJqSOq5S43jIozdQSf--0HJJWcJX_nRbUCN9YkmEnTlgH1eiwhtE9Snd-yjMbtpUkq9pweEJnqHEsZykThwvW5rrfHgri7TBmhgzv2CQvb69hBkcEtWjbTYgNU67umF-ZGy2ZmgRRaovsdU5gv3FGjUnIwNzV-UZMaPm8s4Ey5h2l3jakCuXKK47vwhXmoDy3f98rYzszfZFVJx6GcuNj3q-riznbSIl50IqxQQIUJWB8G1qRqfWrusnXpYWX6sYe_u9_RRdFPYumLMIUvwl43Fa5ijcj6Z0oHKeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285c0d29ad.mp4?token=l6acPDY_J5HB9XFyWZ6Y1eBdUM0xu_UYOV9YezsxbkavIDylarJqSOq5S43jIozdQSf--0HJJWcJX_nRbUCN9YkmEnTlgH1eiwhtE9Snd-yjMbtpUkq9pweEJnqHEsZykThwvW5rrfHgri7TBmhgzv2CQvb69hBkcEtWjbTYgNU67umF-ZGy2ZmgRRaovsdU5gv3FGjUnIwNzV-UZMaPm8s4Ey5h2l3jakCuXKK47vwhXmoDy3f98rYzszfZFVJx6GcuNj3q-riznbSIl50IqxQQIUJWB8G1qRqfWrusnXpYWX6sYe_u9_RRdFPYumLMIUvwl43Fa5ijcj6Z0oHKeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
هاشم بیک‌زاده: بعد از بردن کره‌جنوبی در سئول؛ سطل آب یخ را روی سر کیروش ریختم. هیچکس جرأت نداشت اینکار را بکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/Futball180TV/106421" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106420">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErOy621D0WnsVJZMSTUD-lY0Jdn4Snz9Wzz_tzCzJeGqHpnAt4ZS2b9pcRpdHdN6YtC_qODOU7W06Dkamo-4ScCEDu1jP8IPBaj0k0RGo2RbvX8TA3H0axFTaxmf9S-N2h-lIFlD8vwpf0MpCH0FtApIwe81KCLVkAYliPKlMNd2mXS5nkQ6QzfK_TW_yM6G4KgU7-_TuWOZPE0hN8AXKVglaMSIXVnD64fwPpC_XWfGBTtNgqJNururDMWl0EC3wnd3W6920oQB-_x58Qrr-FjHQu3VQJrIrb4J9ktEfGxbvz6psRUVflcOySqHeV0FSnrQjuTXXqYZ2FExBsgNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/Futball180TV/106420" target="_blank">📅 10:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106419">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbf719687.mp4?token=nD5pkqfLaoZvZOdKVJuxM8NLKNJsIw1Pi0CGaP9PjcYq21krJf8IKZhzzVefyt2gNCUFA1wXWfxC3tiKyg_l8qvlPikngdPLQgjCn1lR4BGZms02Az9Y6P4fZJBSFl8p4y2DstuHfk4InnyleXGSBG6X-ulF5ALqNIaMxSZj0u6cCSqTqhuSmEPNq6WnSdFBlqHrPsIKMSnC7hwfFok_b7TpeX_Xii1JlLxS6S8-ikcwSyzXrkdIHfK2-lmPdZBuHGuN1kbp3LeOxqMZpaPQLKuxvswGf1MQAzLgsUQsRWbGVfSfxcc3xhuNXKiKHIki_H43JKBOWVVrL2usBujxMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbf719687.mp4?token=nD5pkqfLaoZvZOdKVJuxM8NLKNJsIw1Pi0CGaP9PjcYq21krJf8IKZhzzVefyt2gNCUFA1wXWfxC3tiKyg_l8qvlPikngdPLQgjCn1lR4BGZms02Az9Y6P4fZJBSFl8p4y2DstuHfk4InnyleXGSBG6X-ulF5ALqNIaMxSZj0u6cCSqTqhuSmEPNq6WnSdFBlqHrPsIKMSnC7hwfFok_b7TpeX_Xii1JlLxS6S8-ikcwSyzXrkdIHfK2-lmPdZBuHGuN1kbp3LeOxqMZpaPQLKuxvswGf1MQAzLgsUQsRWbGVfSfxcc3xhuNXKiKHIki_H43JKBOWVVrL2usBujxMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
🏆
بالاخره امباپه فاتح توپ‌طلا میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/106419" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106413">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfaC698X-ha5sQhLWHfM7Iod4DPlA1KpB7dvFSaxEncxbO8GruazwE-S_zPnPybY2VCx4sJC_JCyaOKq1pX9pdn4fAbt15wG-sj6N4wK2fTLOnF2Jq1zdwuyu9G9Ti9ME2TI59WztQ6PJ_r_gQ7OXXF212TNQqF6uMe0IOiNIeLB03W_Y6dNt3XquqxU2fXwdZQQQ-8WBrXrzVNKIA4nQXbE5rNjwWT743JYBnsTpn7BqCXWLi2mZfglvrUbO7KGGcDWN5I7pLHmy5sTyt9bxfSmqox_vzaTcDiXGKrRdOpIy8cz8O_C52fu6K4Kwgm29jUHi9M03mvNAsq8xDNafQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BS-PfoWFcAppVsF7f1IPk1hWIkeLdUM7pn2S_AoacwaKIKf1k94sf9VaS2Twl-43w2HVQljWB3zdFpvdD1_TRKfRHzy0ELDJOm5LkTN50Rrj6YQAsoY_0tXjA6HHrVWzGzXbRSD0JJeXdxxljJzlgfkj38oYM4x3qeqxRTMahwKOgTUSsCX9dX4syCFu1Yf_2NqqsUBBgezuyNrcHVzRvSlw-ZjckUqpZcmC04jSMVgnFgBqNIk6fYuYYWrn7kRZCXGnNf5TW_RL-JU4VxBUPJ4o3rMavIu0y-hNdAfLgq5V20c-euK1svPntwiuFFLTSh5s2WbT9VrUI6iTLqSWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_zRck-ozRjhCJtT1xFwB1WyGOwUFFZDpgBeQds3cHb4TjNjBNDETwgxvmnHRTlkOChRQnl0QNRNR5RR6zEYy_BTzQ1PRi3fMBZy8ffKu-zcrI09C_gjhrl2mooJn4g6Y3pgQGaf8s2EEhlHgEYBuNtVRccJZXJEGD8JALfi08AqXI8lnYTIsleEm_hvi7jKVNp0ZYJbDJyxwFRuxeZutOcWkzxhqpwX3YDOdH-6bbr0zXloIwS5bSm1mXkruy9zuQncZOpuoT6wguLtoUZjnQ1fRVETALnEEk2mFv_AQnnN7u4ykn_WDiqbGx1E9S1kg96fOmDlesmVmBt0ywPdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKkgGqr9-M7ffQ-mElJjLcP9csMu0TIXQe5UaFxyHmC8DGFQ223n9gRq11GoJNYEhrkWXvswjvWN-hbq6T-NMmrU8lhO-OO4OUCtjGVHx1HCIdbu9_VSzl9u8TBrORl2YQHHxYthF4JMBnzq8d8P0jDjeGW-fWpbm8ShMt_OzJmneWPkTTwOygzbkSC0oX6f4MFKNTWe7XPncfLDM1aFn4_7-J7YXrrhRK5FiNOgZWhLIuhUgpVyxhn3ARTPSRz73zhXCuBM9565pZUXWLhPzMI4r0ObKG_2EsdTdEGDt7BzQ-6HP20M3L3SiIKH_aMEVIkbiepWL7VLeOPuFWTrYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GpxmpTF526twEuvpLQI87mzLbt8UnnPRtqNg6gCx-S_tbRqyhmT__BXyQrraMboDOuwnj5mZ1kA2-DV4S9Dhlfkwg3cs1b4DbVOdVk9xw4zbAYpexg8BCI29o0WTN-YlzHys4An-d1bUNpYC9oxhoLIfOw-aDyCPeXkzn61sS9-NdydXVAPYYfEoaJvcIxJL7fp-B6DG-iY0FPlt9hdsF4a0jcdwZVkSUBZZFvgS6MNMO0L1Tygbd06w5dP21OIco6AYV7KQzevu4sVlE666J_k2QQrJKNRDtD93ClPT0Q2gR6UdIA0Ond4CeSks9Ik1dCVwfGXeJvXTLlubD5Y4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3acf7nKeXpJxkhG4p4ngmB9ErV8dC70Nnci6wlXx6esFdL_tlmUzLSW7mHZMibIiE1qAWEF_IPR4Max0qaXZROTusGX4HYUjjMwKOE4nDuXtUe5Q2CxF6nnHbiWyc3AC7rlsjZGvaqpTG-zFeBDTvA5imNIpMa1yQZzFvUsW1qCcIQuN_qiGU6viYsaIdh5p8v1PW3y6YbH-4TOptwLUFvnTE7yrXM9CsxXPdbjW9tfLiWtQzCjhc63g8qJtZ5e30CA88wqCPk1Xx9O9yHJiZtptwzmD20ED0OdUjxDICIE4cON2yzyLzh1nAQpeoIrgZgovmzedAOxM2NNYPXXLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👀
بعد میگن پول تاثیر زیادی نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/106413" target="_blank">📅 10:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106412">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dcc7c68b4.mp4?token=LGpd-J4J8psFkcfz9Gq8IhDhwXcC6DZEw7ccFDjaoQfdJEYItJiawXPMpC9vCzeVPEk54ylKLsN6d0NehSnsfkDV6qXTu7pYn4QZD8UKnImxktAM-VVJmLJ_knpTaqpnilyoy8pIIXarCVXcs4mGPlHn3SGpKsXeWzz7-T-cCGm99141Due1o56sHeKq9xl6BYNm1WAxEwFPxuOPwjge8v-IieIdb9o0fhh3mJ5SeRxLM5kkqgKIyNg_7qO8ku_WbrigLVaHqG9tEu9CaVkwcXkran2KmFSUyZCftE5leMqLxay0fpIAW7p1uvqshhjv-zYzZbq8T6Q2cLN8DZdoz509OR2PrRoKvMVXrJzpZ5r7rPwI5FzNfPU77JqDGuFqdnt6o3tapQjBc8WUvPMwjYy2oYj58gdYnhJE_Bzv6oiUOYhxDnK40DsQylA6Az_RY9CRlswz6HquLY1owQEn-B_0WAvAkUi0WVf09PiJs_TqGxpLbw2KhcbirHac7nPCdIYCjtJj3vVt828DpqykKs_6fRl4sQ6uerYdTp8kr-0fyiPD_pK7NHHbapPsjLp0-85vIRdXhbPkes06UspDGbCePsbGpOFJbeBPzSLrdjkWqeYWRjrpUYjIT3anwBsl9hS8i_64Rlw3VXTkt9HWIBAzMW1M1pR-KDiVpR2bB60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dcc7c68b4.mp4?token=LGpd-J4J8psFkcfz9Gq8IhDhwXcC6DZEw7ccFDjaoQfdJEYItJiawXPMpC9vCzeVPEk54ylKLsN6d0NehSnsfkDV6qXTu7pYn4QZD8UKnImxktAM-VVJmLJ_knpTaqpnilyoy8pIIXarCVXcs4mGPlHn3SGpKsXeWzz7-T-cCGm99141Due1o56sHeKq9xl6BYNm1WAxEwFPxuOPwjge8v-IieIdb9o0fhh3mJ5SeRxLM5kkqgKIyNg_7qO8ku_WbrigLVaHqG9tEu9CaVkwcXkran2KmFSUyZCftE5leMqLxay0fpIAW7p1uvqshhjv-zYzZbq8T6Q2cLN8DZdoz509OR2PrRoKvMVXrJzpZ5r7rPwI5FzNfPU77JqDGuFqdnt6o3tapQjBc8WUvPMwjYy2oYj58gdYnhJE_Bzv6oiUOYhxDnK40DsQylA6Az_RY9CRlswz6HquLY1owQEn-B_0WAvAkUi0WVf09PiJs_TqGxpLbw2KhcbirHac7nPCdIYCjtJj3vVt828DpqykKs_6fRl4sQ6uerYdTp8kr-0fyiPD_pK7NHHbapPsjLp0-85vIRdXhbPkes06UspDGbCePsbGpOFJbeBPzSLrdjkWqeYWRjrpUYjIT3anwBsl9hS8i_64Rlw3VXTkt9HWIBAzMW1M1pR-KDiVpR2bB60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
وقتی هادی‌چوپان میگه هانی‌رامبد رزومه نداره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/Futball180TV/106412" target="_blank">📅 09:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106411">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5d091739.mp4?token=lJlK6SQQYbTnOD0tVgB-UW4DypvQt8AoOaKbF_h-MTLsXnP2QzfrgIIDvviTNzADYkpVcSatBb8wl9AbGBh7E93ZB2Ftzbt1z1KDMd3DYZnGhvE3eCNtFSFy1vcOJPwRSLPuQ4w4dZ1vRO0vB-cEKEmBbF7AQ4hcBjnSQMzdaiO9WxehtAKYYUx2e5KPIH-2ZZluejqcK4DKyyx8qUiaZ9MV0NdnnKg5jOKTO-gxNY8P2lUoLKqa_-22C9UUauIEkFVVMfb9P3vgYjydXWxemkBBfT1BK2ZWvlV48bHYCCz7Wef9vCEXP3Wm0FsYsMnCacJIdUFzxBhbawmg7tEguw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5d091739.mp4?token=lJlK6SQQYbTnOD0tVgB-UW4DypvQt8AoOaKbF_h-MTLsXnP2QzfrgIIDvviTNzADYkpVcSatBb8wl9AbGBh7E93ZB2Ftzbt1z1KDMd3DYZnGhvE3eCNtFSFy1vcOJPwRSLPuQ4w4dZ1vRO0vB-cEKEmBbF7AQ4hcBjnSQMzdaiO9WxehtAKYYUx2e5KPIH-2ZZluejqcK4DKyyx8qUiaZ9MV0NdnnKg5jOKTO-gxNY8P2lUoLKqa_-22C9UUauIEkFVVMfb9P3vgYjydXWxemkBBfT1BK2ZWvlV48bHYCCz7Wef9vCEXP3Wm0FsYsMnCacJIdUFzxBhbawmg7tEguw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هالند: خیلی دوست و رفیق صمیمی طرفدار منچستریونایتد دارم و قبل از بازی کلی برام کری خوندن، حالا باید یکم واسشون کری بخونم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/Futball180TV/106411" target="_blank">📅 09:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106410">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
🎙
حاشیه عجیب مصاحبه خبرنگاران با اسطوره علی‌دایی درباره صنعت خودرو ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/106410" target="_blank">📅 09:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106409">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514af894b9.mp4?token=bNzEfznpJi5Ks8WPvJOy3P4BYr2gFNaVAiQHqhOJ1-9Oe5uuoIXlAxVvtRITNIEVsyRN2pT2xdcfyzteevr5mh4j9HjrS25-fsx4UaEsLCuANuOJTq5cKQppG2TDucuQnG-Ql1BOjltepw6pui6hbSb3jGBYuWo6oVqGvz7uWnlvFP1lXLXqqc_ctc32DwaC-7N6W3sk4yf7LMGX06XOiMYLSDwgeZW2S5oInhK88pwKxfuvmQ_scB7Aq1HBvaUwR3RGxJD6YmBPwLYJx-nZhCG14JeYYZaXG8nPbHwC580uJQ28sfM869AqlGSvLC07BXG5bMK3bYIXZpOa9xrsWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514af894b9.mp4?token=bNzEfznpJi5Ks8WPvJOy3P4BYr2gFNaVAiQHqhOJ1-9Oe5uuoIXlAxVvtRITNIEVsyRN2pT2xdcfyzteevr5mh4j9HjrS25-fsx4UaEsLCuANuOJTq5cKQppG2TDucuQnG-Ql1BOjltepw6pui6hbSb3jGBYuWo6oVqGvz7uWnlvFP1lXLXqqc_ctc32DwaC-7N6W3sk4yf7LMGX06XOiMYLSDwgeZW2S5oInhK88pwKxfuvmQ_scB7Aq1HBvaUwR3RGxJD6YmBPwLYJx-nZhCG14JeYYZaXG8nPbHwC580uJQ28sfM869AqlGSvLC07BXG5bMK3bYIXZpOa9xrsWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نتایج ترسناک بارسا همچنان ادامه داره. 100% پیروزی تا اینجای فصل!
👀
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106409" target="_blank">📅 08:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106408">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
جزئیات تازه از نجات دو خلبان F-15E آمریکا پس از سقوط در ایران
🔸
برنامه «۶۰ دقیقه» تصاویری تازه و از طبقه‌بندی خارج‌شده منتشر کرده که عملیات نجات دو خدمه جنگنده F-15E آمریکا با نام‌های رمزی «آلفا» و «براوو» را پس از سرنگونی هواپیمایشان بر فراز ایران نشان می‌دهد.
🔸
این دو نفر با فاصله حدود ۵ کیلومتری از یکدیگر در مناطق کوهستانی جنوب اصفهان فرود آمدند. «آلفا» پس از ۸ ساعت، در عملیاتی با مشارکت ۲۱ فروند هواپیمای آمریکایی نجات یافت.
🔸
«براوو» نزدیک به دو روز در خاک ایران باقی ماند و با وجود شکستگی کمر و جراحات ناشی از فرود سخت، خود را از یک مسیر کوهستانی تا ارتفاع حدود ۲۱۰۰ متر عبور داد تا سرانجام نیروهای امدادی آمریکا به او رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106408" target="_blank">📅 07:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106407">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106407" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106407" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106406">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGOEI3IWGbvTkAq39tAI_iBS3RExHU-Nn_wY8kQu3sYcXgGvjAHYL3ytWyCAvrKmJna5A1rDWadLa_RkXJHxfzl3FNmab7POPtItP9bz1OEcuaY3yi9FHGKspOxL8mprlpVVkAHPrLlzHxuTtltBCdJCy0fPjYrXxKojst9Nl5QFcABcF_yaxEf5YKROQh6Tn9Qj3xyvwFTyBdJiiG6g3nh0Ov3RVEEVjGtQMCu5tXsmiTvbjPfID9XZbLHJoEjmFYBZ1SloogCxDcv26YklSVxPJ70nBLetM1tB4Sr5sqMZji3OzJ2P84ECQkWdDlm32U4DRTt5gIwbHPE0okV7Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106406" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106405">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106405" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106404">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔻
🔥
🏆
لامین‌یامال: من و امباپه بهترین بازیکنان دنیا هستیم و توپ‌طلا باید به بهترین‌ها داده بشه. بنظرم فصل‌گذشته عملکرد من گویای همه‌چیز برای انتخاب شدن است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106404" target="_blank">📅 01:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106403">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj4wY0eMFqorPcqPqkyKmvaDmvBwlwUmmOlazintdSlyWdls-RLohbsIleWqJWliPtgXL6_NvOBgv6nEpct3nWOyQIl6W3O3OPJLE9N7058wZSZ29NyzfOHJsv9tK-QNjlMef_d5UlLLto0rbZDmvoh0fyPLhGTdTnvsKKGkzkQrknnHMLQSTSsTV9ztrO9PMDRthVOMAh0NM-pzg9XCx3I82nxbOcNf5x9xpoFSAo1lmnsZWwltVjP1T_vnHhFYVNLkqfKs3oKy3QuKTvsHALNvuS82AtyUP-WfL6KJ-V8duTvC0-aJHqaGc7iCOUjQZBiGySkt2cgT7V6LBBbxFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
بالا گرفتن جنگ توپ‌طلا؛ لامین یامال: «فکر می‌کنم امسال به خاطر چیزهایی که به دست آوردم، شایسته توپ طلا هستم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106403" target="_blank">📅 01:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106402">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poBmRSgoCX1g7nKDMRkua5OYDUHv_ihuA6nywmH7Jpzaad_Kjec_zJoO-lwmQvIXpTwHJJf-SYIakSsTHRCGAcnw1toBRWYra3GdszwN6mKLC1Jg-dgElME-hUtMdGMnKGUAdwjEPR_fKSsW-HCka-Egzjx-0MKaPCon1Hr6olR6la_wLrE5eYPx-J5DsK-HwL-J3lHP5NkhgLsF7xG1UeCOTtMJJxP6luCMPm_TP1sghiTKoJlqwZZ3hQR5qk_R-xNDwNZ6wqAXYA3jHAn1vdyZ3PWEYG1vdqd_LxV45P37xBfMfqu76Mi4znoKRnk68Co5N4JNJY8jwyd2yvjtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
بالا گرفتن جنگ توپ‌طلا؛ لامین یامال: «فکر می‌کنم امسال به خاطر چیزهایی که به دست آوردم، شایسته توپ طلا هستم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106402" target="_blank">📅 01:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106401">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhXNST936FC-fg6llheVdOHzIpJDTr2J8YDZ0dKkkxnY5M2eI8yB9KhUBr2VLKDbWuiMUdXC1nY2nJtSdY8FHDHsnDx83JmS6IDMmeAwrGk6SW30Ntw9TZqONs3qAUUv7wiOGuumKn9rKN0M2vvXZ0-rtpQs5TMPOV01DnempyaYIrD6RR08vjDCJxhyLpyFDTejAAk7dRfnHVEEP_Rvrt8Jw_rN3VEwfi2MZOdDCKSF-OmXjH04Hf4_HOX6IOJ1XMWwEGeMRutAh5cNCN-PDdQYihJwsj-lemNShgnDvoE1c1Kb1zq2iyonuDh5LhpEXsCMgEgP0iDPP0knp9zJ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🧕
بیانیه کمیته داوری انگلیس: "داوران تصمیم گرفتند که هالند در آفساید نبوده و همچنین تشخیص دادند که انزو فرناندز به توپ دست نزده و دخالتی آشکار نداشته است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106401" target="_blank">📅 00:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106400">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8675062324.mp4?token=hA-QPFnSAfVEwsvmQ0r2P1ss9lv--5ijgKB0swV3mWSIvdO93iXwL_XWbd-9bJGi3MZH9xaWiIBWDceeMWUamg8u3bU7408SM4P4ATPMuGk8y6C6_pq2QEma3snGbY3eavTafJ_lFIT5xuWEU6u4cKPQxUqe6kodRWGaDrAQi4o76gzChfB5HlRmmPIk4FDcvEqLSZIXISvT6jszhoBOIdP33zmnV2FRkf19eD2P1Sg6kAz47aRl8pnD_RFf1VR5DgjXDDbwSxnT2q27gCC-Ku0WrHzjm8VsM6XPjlMM6wgAfA8aEx4bdgQ-TpF8N9o-GLc_53pNa-g3BM0AwzwVDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8675062324.mp4?token=hA-QPFnSAfVEwsvmQ0r2P1ss9lv--5ijgKB0swV3mWSIvdO93iXwL_XWbd-9bJGi3MZH9xaWiIBWDceeMWUamg8u3bU7408SM4P4ATPMuGk8y6C6_pq2QEma3snGbY3eavTafJ_lFIT5xuWEU6u4cKPQxUqe6kodRWGaDrAQi4o76gzChfB5HlRmmPIk4FDcvEqLSZIXISvT6jszhoBOIdP33zmnV2FRkf19eD2P1Sg6kAz47aRl8pnD_RFf1VR5DgjXDDbwSxnT2q27gCC-Ku0WrHzjm8VsM6XPjlMM6wgAfA8aEx4bdgQ-TpF8N9o-GLc_53pNa-g3BM0AwzwVDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇫🇷
🇫🇷
پاری‌سن‌ژرمن با تک‌گل‌ فران‌تورس امشب مقابل برست برنده شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106400" target="_blank">📅 00:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106399">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THyI6hXSHUslNQwQUzDEkMxsjJdnmuR9TKiYm5_Sugw0fJjCNCydf2bYxii5NavT9JLT40_AgkOH11gFkt8eIqVmtemIfYs7f9shjdrmnMZwuNVIwCJwHiju7wbJRw4fFaezuPTFIL8wIvjD09rtC5l-Wze4tcEu8ThWrQCAsnW4N6-t0jA_9xSz25qEsxDeATb2OyKMRi9yVX8H-Sjolw6rdFmUh49-2AQEAt_wrZM8KC6kyMm7x2pR7ya3KXN9QEfIkPvVjBW1fsrde9kBzQnAp5TpHVKqdfV1lGFdrzJgXpIcfQ98k9Jm0BKw96QbAqaBUn8PX8gtTdvJIwmDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
افشاگری پشم‌ریزون نشریه سان:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
شین دافی، بازیکن سابق برایتون، برای یه تماس تصویری پنج ساعته از نصف‌شب تا حدود ۷ صبح، به کلی بلیک، مدل انلی فنز، ۱۱۰۰ پوند داده. بلیک گفته دافی توی این پنج ساعت بهش گفته چطوری لباس بپوشه و لباس زیرهاش چه رنگی باشن. بلیک حدس می‌زنه که دافی می‌خواسته اون شبیه اکسش لباس بپوشه و مثل اون بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106399" target="_blank">📅 00:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106398">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxqBjWbGToUgCYBXK3vcymMEGXQcyiGBqBsbqKEtRYulYJD73AT8ryJLz6jVOZFUzzooJ_vsj_EdbgYFEhc7hMiIZvfWNIOb1ala05-4kUvFCV5K9v-gDIFlSkWYwpiDGgbtl6C-kptwgp5ANx0eWSSZl_zm9vNI98SSauQhaYkzGYJW-giC-8V7ONqGdU7qpYvDTdTJTLKElCLI3t-UxtivXFBqFFqbWs1DJ0g0Gv3BTJTGz5hKnX47UttG7_lZ38R6Dh8UII02RClU2sRbixRLeDvxBCbvfAKxNbcjR0Ac53KWiil73279Yhk0yneazzFIWe_klAbhMq9DWMfuLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
محمدخدابنده‌لو رفیق صمیمی اورونوف
:
🔻
چند روز پیش از اورونوف راجب شایعات جدا شدنش از پرسپولیس و رفتنش به یک تیم دیگه از ایران پرسیدم که با پوزخند بهم گفت که در لیگ‌برتر ایران فقط انتخابش به احترام ۴۰ میلیون هوادار پرسپولیسه و در صورت جدایی در آینده دور، مقصدی خارج از کشور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106398" target="_blank">📅 23:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106397">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcBC1Jk0-MvLq-k3P8oI_hLQnzsJb7iPWHRABemxR_M2pet2L32LmT_GpyAqbH2M8HmONnIJp46Ay4VEouybJgT0VXnC-db-6iNMRrcuPIkMwAvMhOlr8uAgS2q3PIMa4TIP43qsqeOtdPsipHYJtItwVXwGRjSQPHcetGq9WzYhCNd7Ff4o1TFgbx5MZ3vJPYGPM8spzQfOEAqbM3iryVpHvezdmr9oeEY8EDiKPQz1xlhylr3kKASziWnUwaYyK7bB9e6nPcrlG8XFthGp2SSN4YvvsOvXEQcxGnl9lRFcUj8YyCYMcmS_zcBxy7dmy-EAH79eG4Cht4RS_gLkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
یحیی‌گل‌محمدی در ادامه روند فوق ضعیف در لیگ‌عراق، مقابل حریفش شکست خورد تا زمزمه اخراج این سرمربی پرافتخار از تیم دهوک هر لحظه به واقعیت نزدیک شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106397" target="_blank">📅 23:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106396">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4S-EIz2IKcZLgjz68tgJWQ1YIhzzehPOgzMBZEdT3b_mC8kAmt4KplUTdF2gPDtcXhnwwulSzTJ3qIVl8-TOah3JzcI1amHH2WmvofnV4of6itML40Bm1FLTcR0pHoCtP84lDeS20dFWX1BADtokGjXlBO1DmSHFT9uuvUvhwcTVXv3ZM9dSf6a2la2cDtpiUAbCji1h03hsRI3mLw0u93S1Pt8P1tsd2zfql-x4GPay04p2uAbF8M6p0e4RbEUHX6mp9dslT6G7guipEBLEXv1DmmzXvFPlV6hOXyGbh-yj_12Ozh9eVqN38oMopQYyYD7pCtzew0MFlb8gSwo3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👤
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106396" target="_blank">📅 23:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106395">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
📹
آرشیو وار: گل ارلینگ‌هالند آفساید بود و نباید از سوی وار تایید میشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106395" target="_blank">📅 22:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106394">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66e5d4924.mp4?token=N9rbX1Svp7tC-yYBxKIfuNec8dASW_HamGXpboIR3U89GXq_8_DJnX7h9UMNv9bDKtNBNW9zXEiU2CF5j5YkcVzFbS4vkfAVSC6F7yxbcm2gWmf5ZwC1hOrqDXr5j-xzOaqzpwdjIV5ZNjKdacYbqFu909WHZl-DKYNFqu9glnTrn585Efa0Kd39bm3XgUHZZ8VIrod-dUNsdZ9Fvykw3-k8yke3ZdKRr4sEj50_54vOIBqh48G89X00INZrXpnNTdjq2avOufgUp0RKHovbiyQkifAwvFeB0k8RF-j04pkFFrT1ZBE7IHxgbwoSjfqvhPLQ7NjvUuuSDySCjGSqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66e5d4924.mp4?token=N9rbX1Svp7tC-yYBxKIfuNec8dASW_HamGXpboIR3U89GXq_8_DJnX7h9UMNv9bDKtNBNW9zXEiU2CF5j5YkcVzFbS4vkfAVSC6F7yxbcm2gWmf5ZwC1hOrqDXr5j-xzOaqzpwdjIV5ZNjKdacYbqFu909WHZl-DKYNFqu9glnTrn585Efa0Kd39bm3XgUHZZ8VIrod-dUNsdZ9Fvykw3-k8yke3ZdKRr4sEj50_54vOIBqh48G89X00INZrXpnNTdjq2avOufgUp0RKHovbiyQkifAwvFeB0k8RF-j04pkFFrT1ZBE7IHxgbwoSjfqvhPLQ7NjvUuuSDySCjGSqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
بازگشا: با احترام به وحید هاشمیان، تعداد مصاحبه‌های او از تعداد دفعاتی که روی نیمکت پرسپولیس نشسته است بیشتر شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/106394" target="_blank">📅 22:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106393">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44897a1039.mp4?token=Zv2edYXlDyo6XgEKc8kPFDB3_uLVsZpM22gIZfnxoIbTs8hjow1XPfe40vJJEnxxDk141oOcCW7vz9CKOvE45OFuaiLK1A1w9WVcGZnY-tTKSSlVoQDDdEHDtYQ2wWxvSQisoRI_WasqqQsR_FoG0eNSK7zgxPdWgd3fEumlDgiG8ggV74zIF2tx4OAnNczzZrh-H-WdwSJhwIGn-SoWUc-bEgO2YS0-TgYe0sSYemt7kU53Cd_W_gK7Priu34oepeQUdBhkUC4pnFFZgOBnfeDRMkd41njmxmUXT60aj_yfsHTY411YQbjEahLli_4pWF8kkJATVACw0tnVQFKHJ08Z2LTKmQACJxRu4hpnCgk00SkpVk6Dk2-xl5TFk-TsqDYgw0d0SbviH8FkJWWUTzNANU36JzhiKAC9ITB2gLWxsvTi75oC7Wvwd-55pY55pYkgIxoWe-CG_pnGVvnoavqVtwaDIcAwwMigOiHAD7ImWQw1yjhvMNXHhnYwwal4TAMEszrM8uuV6YtvXqmiVPVHvjGtnbUzFxDYFssxDLqGiTjX0LE9Jatjc0VVRugC7WctU3c5heutTYey4-o36QkED-QcuwJ82D2qzEfzBiSl1bkmTwjJxWgPbZOsnyC2-nUNacWNUNxkjkJXzqGyP-DTm4Myud_Esuy1YXsKgKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44897a1039.mp4?token=Zv2edYXlDyo6XgEKc8kPFDB3_uLVsZpM22gIZfnxoIbTs8hjow1XPfe40vJJEnxxDk141oOcCW7vz9CKOvE45OFuaiLK1A1w9WVcGZnY-tTKSSlVoQDDdEHDtYQ2wWxvSQisoRI_WasqqQsR_FoG0eNSK7zgxPdWgd3fEumlDgiG8ggV74zIF2tx4OAnNczzZrh-H-WdwSJhwIGn-SoWUc-bEgO2YS0-TgYe0sSYemt7kU53Cd_W_gK7Priu34oepeQUdBhkUC4pnFFZgOBnfeDRMkd41njmxmUXT60aj_yfsHTY411YQbjEahLli_4pWF8kkJATVACw0tnVQFKHJ08Z2LTKmQACJxRu4hpnCgk00SkpVk6Dk2-xl5TFk-TsqDYgw0d0SbviH8FkJWWUTzNANU36JzhiKAC9ITB2gLWxsvTi75oC7Wvwd-55pY55pYkgIxoWe-CG_pnGVvnoavqVtwaDIcAwwMigOiHAD7ImWQw1yjhvMNXHhnYwwal4TAMEszrM8uuV6YtvXqmiVPVHvjGtnbUzFxDYFssxDLqGiTjX0LE9Jatjc0VVRugC7WctU3c5heutTYey4-o36QkED-QcuwJ82D2qzEfzBiSl1bkmTwjJxWgPbZOsnyC2-nUNacWNUNxkjkJXzqGyP-DTm4Myud_Esuy1YXsKgKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
بازیکنان رئال‌مادرید در گاراژ مرسدس بنز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/106393" target="_blank">📅 21:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106392">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1IGb7xf7MkHEC70MmJ5MJLJJIr5Qrmy3FNlazU8nwc468W_4vhlrmemvh5mOzUDi29D-mnRxVhYXerrYynfAYxS4v_pqf1bhJ3pdzB0KGekNKJPyW_GeiQuEyJA5XGQkQr5ichxATKpcigKHxy6DNqZds3yV5SCVWxzLN5FEPWUy0RSgLQ5GIsPmcFp1CPVi_cBRLGsFfy-Ij1QDvFGDJeKwnLxQ_P6p8XS2i05efmIEZHfi0ytcdmkBrdUWMzz4pcol2Qz0wEaDDoQx1_ssdwjiwSsfvZwzmNrDkLYXA-42OwdNo_D6BIhex9pxqeuds_mFXoRN1i0htIJW5lwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب اتلتیکومادرید مقابل سوسیه‌داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106392" target="_blank">📅 21:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106391">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkxLwMG4U2wCeunBlIoDCF6NBAGSRogXqLzlK5d3XtA0r2PJcIHV205QImLbHs9zuFWsR9v6uyhAJrgme8WaEctxZFvw-YaubILIGbn1ZLEoz2XFhMFcXVaZ7KGC21kC5uOuT43Cw8TAKA_Y6kr6MCQdaAhqQz6vpN3gKC_hWvhVs002w0sWm3FrTs5fn8bdvcRjFSRlylxJUIbnr3wnhtST8-6wgVy6p_fyhg-Olm_xTTt7ORJrGWu_06f1OnoFVZ-orN1XFrHA4_MFYmad1-mB-DghhNSA8qASGeiHHvSzDwJW7XAxFWXG-x3vVVQqj2GT58aGR-hOjueZHuN_Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
🔥
ارلینگ‌هالند بهترین گلزن پریمیرلیگ با ۴ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106391" target="_blank">📅 21:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106389">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1dxyokBq-Uwu-UaiNU3Xpn5AxS5n04oXcYoB0SKmoHateNMlAClkzxG0-wBCZy6rdT3q2sGF3WreJgSnZUyxG9CLf3qyfcXM2eqvQytuX_wd0SD-im-SBF2JbMfoIInL45o5Mij3OjwGBmKqZ_XVgwOb3K5HrlMXM9APYc2t9gv7V1eSAKTWGtjXpq2PITsMNYBQt2Fu6dwLU-lXWxQ9Dyua9vlw0wFtEPV2R5CRqmuyNKPUJzDzeWbhzEqMKyEumE6ZSgnaHJ64efX9GQ79kfM0KqGUEfLjvaxZ5vV1821EGAmUwqBiSwOQQfprfJCKNBGxO3RXuRQzmIiZkXd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGEq7ok70LfoUK7utCusLxuF_SblP5cAow3lRV6ZQIz--rni1mrWjbIVO-X7MG41tIyZj4cTxzoF6sbd6g0pIEalKByrtkyuT4BqUnJ6z2lvQR46OTEjJcj3TGOYNJZF85UIgOtIf7SlNcVxVjFyhE9YBCHeIehzh7Iykf9KBV18S9fggPb69ggs_vqivI5hLrS8qIXa-yUugGyf6mI-l7o3KP5GYmxJqGaEAFkTt9UMKP0PIDx0XDCq2nS_zNBLAJp6yqEnaGSFZqwCGgLsPsJF6uF-zd2kExw9qd-JHW3rPiyZ9BNexRR0lOE3vwPDX4qcJCQoL9bRdEMA5D9jVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی ده نفره به یونایتد
⚽️
هالنددددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106389" target="_blank">📅 20:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05e9e2f327.mp4?token=SuY9a34uAKEGygHSv2HtzS0cfdcZyLq5gE-YCnxQGJruT-k0Vb2nQ-FaTE9GvuYHxQ3h9L1fcJkvZrYcABQ8WiRBZ_OLWgV9Igh_ZVue7JWNXzJ5XpJ_nd9eiiiizPAF4vyRjbHx9qCy7bTILXYpiKOfYIwseS7k1thgi7J-sjwPf6OBg-1huVJ8Qf7j61s4saUs-Rr6W-yO4WVi6rdw7EWy1hPpwLXXoIVumerzugkT6ohAyN-q1Ye6UNUPxr2h6szMrDcMeWNUTgFVViCZPsaE5tmMhfukEOp3ktM0EolJM4XiFtYsRLrd6aSs_8hChzfJfDDnfNywqdpw1qt7Xx9O7p0yvVMxruu8hMA315b_YeyJTbQXyZ4qinuONBK43K9bLNcKkF9tJecwKZ69tokyxK6hFLakt89oK_XR1KPeqYL5hZEzmX19LjbTp356xBq8Q327Bd5Z7JfDrCMhiQmHzHxsdbZbygrG-C-Zh_yi2Uui7Fk8T11lJgDRrljALjruXDSTnrT34Wt9O9UOf6-q5pN28W6sJxlR_Y94ret7f28v1wSxp5MYLVbO4yEwipE1Sk436Vx-Pguku6ZPhn4IqmDff5_tsW7nwk9J-9XkU_l0gvqgo9UE4xSr0uX5mcN0RbsFWtUb-iMy09RJnjwlsvtx6NW8XHQeEaJiCso" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05e9e2f327.mp4?token=SuY9a34uAKEGygHSv2HtzS0cfdcZyLq5gE-YCnxQGJruT-k0Vb2nQ-FaTE9GvuYHxQ3h9L1fcJkvZrYcABQ8WiRBZ_OLWgV9Igh_ZVue7JWNXzJ5XpJ_nd9eiiiizPAF4vyRjbHx9qCy7bTILXYpiKOfYIwseS7k1thgi7J-sjwPf6OBg-1huVJ8Qf7j61s4saUs-Rr6W-yO4WVi6rdw7EWy1hPpwLXXoIVumerzugkT6ohAyN-q1Ye6UNUPxr2h6szMrDcMeWNUTgFVViCZPsaE5tmMhfukEOp3ktM0EolJM4XiFtYsRLrd6aSs_8hChzfJfDDnfNywqdpw1qt7Xx9O7p0yvVMxruu8hMA315b_YeyJTbQXyZ4qinuONBK43K9bLNcKkF9tJecwKZ69tokyxK6hFLakt89oK_XR1KPeqYL5hZEzmX19LjbTp356xBq8Q327Bd5Z7JfDrCMhiQmHzHxsdbZbygrG-C-Zh_yi2Uui7Fk8T11lJgDRrljALjruXDSTnrT34Wt9O9UOf6-q5pN28W6sJxlR_Y94ret7f28v1wSxp5MYLVbO4yEwipE1Sk436Vx-Pguku6ZPhn4IqmDff5_tsW7nwk9J-9XkU_l0gvqgo9UE4xSr0uX5mcN0RbsFWtUb-iMy09RJnjwlsvtx6NW8XHQeEaJiCso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول منچسترسیتی ده نفره به یونایتد
⚽️
هالنددددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106388" target="_blank">📅 20:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106387">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBzX7PRKR61RM84IXQbgLoVowcWefXA-eAt5wSfGJqGS4HtV3szZs-a7vVXSEMOrLKQH3MdBKQIAdICgOTlLHqCXfUbrsl1IcBp3rYOC1eICg2Nj-Tajb7tfeI__auAPWtxXaAtgHLo_EIfNTeGMUUQwK_msilQLkA8VKlHfKc4hHv4qWcpUjBU0U4uH1rhDAtsMzYng-YtQksiH7-hNlXpZomcQ4yAkTAHu-ZUZkd8omf2ngHYlpETSFwKgUsaHlc_A_hyMfM2SzGahUariwP37DiniPOu6_htoE1TG1ymPBS0BJ8sMOomg-8fgRbbo2kKj3RX729Srv6EZR7VxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
پایان بازی با برتری چهار بر دو بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106387" target="_blank">📅 19:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106386">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بارسا چهارمی رو زد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106386" target="_blank">📅 19:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106385">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ژاوی اسپارت قبل تعویض شدنش ریددددد</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106385" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106384">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بارسااااا خورددددد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106384" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106383">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گلگلگگلگغگغ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106383" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106382">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/868a077e6a.mp4?token=DyqpO5rdhkPR6p1imRjbT5iTbqV_ykHhZ4cIiuvM9c615aXVaWCza2cjKaJg-MPmDSHYA7jPlRiBLDxhcrjt2JjDEzl6iL-a-8cm8sJfkZAospQUKYi2Een5bNLPXXb3l7CtrV9qdUzaRC4SNhNRTyrCFr_VnOR3JCjROVg0O5tcjyHqcfaXeVVW-P1s-DzFJZhltN5G8vM2KdloL5zwB-KSbckg3WBThucdD4qdTlpE0a1gsmbvgwOOniNxA63iSWH4TwUbTa1zwpaCTJg1rYV0bOQKIu5JK_RGQNhkoTLZAzPY7NzrnZcWlkYKUIDrRgHOyZdUE0Mxi8LlkG4lsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/868a077e6a.mp4?token=DyqpO5rdhkPR6p1imRjbT5iTbqV_ykHhZ4cIiuvM9c615aXVaWCza2cjKaJg-MPmDSHYA7jPlRiBLDxhcrjt2JjDEzl6iL-a-8cm8sJfkZAospQUKYi2Een5bNLPXXb3l7CtrV9qdUzaRC4SNhNRTyrCFr_VnOR3JCjROVg0O5tcjyHqcfaXeVVW-P1s-DzFJZhltN5G8vM2KdloL5zwB-KSbckg3WBThucdD4qdTlpE0a1gsmbvgwOOniNxA63iSWH4TwUbTa1zwpaCTJg1rYV0bOQKIu5JK_RGQNhkoTLZAzPY7NzrnZcWlkYKUIDrRgHOyZdUE0Mxi8LlkG4lsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
صحنه اخراج مستقیم فیل‌فودن مقابل یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106382" target="_blank">📅 19:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILSbm3ZehFUQ3xNJJpSdCN4f7igfW82FXVtTlweVSzxH3DzMx1DrKDtvDZjlCIxEwX-oESacrkGJkpR4_sRF4oHKu8_OaSo_vq9ys26JVoIataxQOj9j1JaS4ejQ0WObDqrUuhHRmgVEjKO8XiSVEy0InEogPme20SQQw-YlbBkYIYyDeHXpm4XLmSBWQJWm7WNZU9R3gwlDiAYRIsk1sxTyR_HHVR6dhtqTqY1n0ggJqOwsdTt8KwBVmLIzuosWoM-4qYznFAIAHGWjBekewJrQTqL-Z41JqEs3rgeODT90smhl73uc7xXNTwgK1f6ohXNDo66Veagk7t2-dLYqrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🇶🇦
لباس استقلال و السد در بازی فرداشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106381" target="_blank">📅 19:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106380">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8f3bfffa8e.mp4?token=Q3dRQbVLbKaS6INwmzm5_2D4uyXQ8r39SxQwTzymE-L7dV5Yr-RcQ7AmZ_7HJNSspTOOpEcohOkS4Izc0RhySnpcMfmkEwtod_zqcVJ22JlRlraUSZIF5ahyQiQXshqiJ28gtZJ68Uwfp5WKAfRMzzjLnscQYydYxKMb1rdzpr_wvCn7Ca2-SbkojOUIdjdoUMBS1B1fPWgMUtMn27uNHxTbRcFXYJqgc2p70KdD3K65pmRq0fBfkTeR1qqHDkAZNwW_Qx1CCwRjYM_aJlQM8Q3PrId7FQfFfDoI_sioSCyD10WIxdij0e3sKQsflfInXCx-aqsvuwKol8dNMZ2erDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8f3bfffa8e.mp4?token=Q3dRQbVLbKaS6INwmzm5_2D4uyXQ8r39SxQwTzymE-L7dV5Yr-RcQ7AmZ_7HJNSspTOOpEcohOkS4Izc0RhySnpcMfmkEwtod_zqcVJ22JlRlraUSZIF5ahyQiQXshqiJ28gtZJ68Uwfp5WKAfRMzzjLnscQYydYxKMb1rdzpr_wvCn7Ca2-SbkojOUIdjdoUMBS1B1fPWgMUtMn27uNHxTbRcFXYJqgc2p70KdD3K65pmRq0fBfkTeR1qqHDkAZNwW_Qx1CCwRjYM_aJlQM8Q3PrId7FQfFfDoI_sioSCyD10WIxdij0e3sKQsflfInXCx-aqsvuwKol8dNMZ2erDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل لامین‌یامال و گل سوم بارسا به لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106380" target="_blank">📅 19:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106379">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">لامین‌یامال دبللللللل کرددددد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106379" target="_blank">📅 19:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106378">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگلگلگاگاگ زددددد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106378" target="_blank">📅 19:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106377">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پنالتی برای بارسااااا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106377" target="_blank">📅 18:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106376">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
‼️
⚠️
🇮🇷
صحبت های تند رسول برگی عضو شورای شهر تبریز درباره اشتباهات داوری به ضرر تراکتور: روزی که مهدی‌تاج برود می‌گوییم شاه رفت! چون کاری که فدراسیون نشین ها علیه ترکا میکنن شاه هم همچین غلطی نکرده بود
!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106376" target="_blank">📅 18:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106375">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gufzmMNjA8gC7hp-6qerpn1EsajG2wziE4wryVG1K2A1g4WnPpXxyZ-RZZT5YIoY2nZxhWJC4nm867XQeU3PRav0Pgl9uaFw0U0k5gtbKueshkmrdeu-o2AfFfmGHASwQYNSjxC8_dwpfm7x8MKqP_SkSMsh_bfYJXnn9MNTGh7BZ72Te7vg7psMY6ECEuqeMigdnIAz_WMU2eV8Aoq-HfKH_sD1mfMI_3ftxAoP-XTpoFPsWTw3yzueG7vhn_AjfZpsrMZavdC2lnM6eachbEtmYXxP08uCbWd4jszDzmc85wvt8aCVBFkluEYk6HBdoRj-lsPGE4H8hL2h1wW0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
⚠️
بختیاری نویسنده و کارشناس اقتصادی: چند سال قبل من رو به سمینار دعوت میکردم تا اقتصاد رو با انیمیشن به رئیسی یاد بدم؛ گفتند ۳ دقیقه بیشتر نشه چون ذهنش می‌پره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106375" target="_blank">📅 18:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106374">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxk6eNjZJyfw4VUkww2sCnBycF45jrjwWw6yGD6OufD3RaJGF1tQr0i1zNqT9J0xN-goPlR6U4a6s1Sxbcv83_YAPfnRvQWiFK_QQjsJXxRqJsto2dc9O-VuBfQ2nOToolRDrCcZ0GdcRmspSAL5esX_qkArHya1Vo5nRdWOy_ctWYrAe-Q_g3waSpxY2faSFQ2T92ddQC0XmaiKM6vh3o1aHn5qQV-PRwPWF_zq4P1nzFmk3E9BGPDVM5g7BEZ82lEUFrUMPlSXaMeB6W-PN2qDt35g6584k3vMmApbz4wseqrfPgDvxqR3HylYN3tZw1SEvqE1O8oM_AKzipmPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
لامین یامال در 4 بازی اخیر بارسلونا:
⚽️
⚽️
مقابل رایو وایکانو
⚽️
⚽️
مقابل والنسیا
⚽️
🅰️
🅰️
مقابل فاینورد
⚽️
مقابل لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106374" target="_blank">📅 18:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106373">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs5VMhFk7wbb-OiA2zd6QF3eutFkqARhxERV9v7Gdtbj849Za1gZmFoz1SMCWmorrwOmIVz2LaWdrwQ-cET0CL2ffjPSMX0OxxM0YRqOPMzb-ofZvYwEYBF4q_iI9cHlmXAklwhJI87y0J25mp-SE6oOT4Yj5SJsFFWlYYiiZi3FgZXPjPwKchIyhiNU0IN9kXmxDj-_L5yikti3XLcQufv3Hj9UUhIwdUbyA4dTlCRP41hptjO2vmv8GygjbKFNNZ2dWBGiWf-lax7yzKU-4qax-WwSRlR5wfI0BcLsJELc3Bg_ufVjukuazbkIYd1yixFSfZRR52FMOt1u8pPFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس در دیداری تدارکاتی با ۴ گل تیم شهید قندی یزد را شکست داد
⚽️
مهدی تیکدری (۲۷)، یاسین سلمانی (۵۹ پنالتی)، ابوالفضل زارعی (۷۰) و مجید عیدی (۸۵)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106373" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106372">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106372" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106371">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSYI4QqFgn-WMFjM291DREHbBMY5h8KB6o-JQ7uWU6gngw5r1TxdgB2StEMGgSGLDsiwyRlPzFVGicGRaWn6kPaIbsJ_3yaaMMifcl3ZDFkF27FU84W4G4wR62sTpWMRAlO2XvJ1P_B9n7uKgHAPZp4RCXWQwOmFu8TQg49xBJBqtSrD65UBcvhmpXHleEyjjOLe__8Qd59NQgevE-n-oTMsAk5Di6wTz2Og9oY-H7ewkiy15GN2zSBkrH3rbImb62m6Mp1g88LABxLQ-vofP-zCmnuzhSKRrxveIqWY5Z5dse6bnAmEkrJN34qBWxEOTr5ToVJqmaLrRW-pqWbz9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106371" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106370">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رافینیا دبل پاس‌گل
😐
🔥
😐
🔥
😐
🔥</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106370" target="_blank">📅 18:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106369">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">لامین‌یامال زدددددد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106369" target="_blank">📅 18:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106368">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگلگگلگلگلگل دوممممممم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106368" target="_blank">📅 18:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106367">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2SFBqdnM-ga0pBM2mmLT9Rk9d2Z5-UwulUmA7LyGc6f4zkiF3XFt_aNBSuUMww-vSzZCkKi4fABGvQHRgt1sSPkup1nur8PUQNrm8HMb8_7lFO7FoPBvJgXtpcyuhKzCm_0s3yq2AiV4hWJI9SBmrYyQ-8GXilJz8W972oSSCercuztRcm7roHNBimze3YDdO9Ry3yXHQLQTJrg3euzhW5JldgfauI4RXRy0kN-oCvHYIosRKvNSrepvB0TsmMRblVg7OnOIwd4plj_eftbF4dSgiZgTkbPnjRt8eYIT3M01bYlRuGcnv86qDhqqG4WL9dJK5Byi2VVzNHCxGE4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
ترکیب بایرن‌مقابل الورسبرگ
/ ساعت 19:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106367" target="_blank">📅 18:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106366">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d40cb71cac.mp4?token=hcWX2aEyurIu2T7t4E80u9bO_HCMXb2nXGgilPZpWw_mGcwTehYL36qJAYyUVhP63FP92OMfVPZLCVsxtrYzr_avgiVIMZfCDIFGc_OuxQAu3FONEmV9q4zaX8s8SF85I_a-KuhzhPXq-V9NnEbPC9DjxU5wOeBu9c6KuAC1iDdJ_h4wm33_HOHUP12GtKPw8p6vk9A_FxzhXnFiEodYWRbkMoEHz4k1Cui8pn3abjsFUnZ0nopQTXXmwDFSpiWuGqINVy4rPHlNpX_f5Ihp2Ga8pzzTOKae-Tql27wrydBiwRjLBgjv2eykbt2xB5wgYoOH_e_wrglN4Ml5ValYl3mJP0MBiT09V2-53uhwb6mo_DBRw7dUTGq44cSv89UCmNWvllX2a4iPUTpMr9ja63aO41czllDlFAJ0POWKg9DXCPTd8PO-gMnBBajKafUkpRB-uyXj686vpsnCDeA-nzad8UJaAkR1aaa1TXRugdONM-LYBGlgOQnmUUwYA28Y9h47a2PiwxH4GdDIkNotsAE_zHEpvu3pOtv4enEPwsOcf1vvaMIvB0p3FGsKwRzQjOMZaeXrjQlpziSO3ngA5K2w36S9No-SskoSewgi-yee2-za7lkYRQlwAvMbmCfTt9s6USIjSKDxwMZQdbb27bjcLPGwpOBCvYtPYEw2j8M" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d40cb71cac.mp4?token=hcWX2aEyurIu2T7t4E80u9bO_HCMXb2nXGgilPZpWw_mGcwTehYL36qJAYyUVhP63FP92OMfVPZLCVsxtrYzr_avgiVIMZfCDIFGc_OuxQAu3FONEmV9q4zaX8s8SF85I_a-KuhzhPXq-V9NnEbPC9DjxU5wOeBu9c6KuAC1iDdJ_h4wm33_HOHUP12GtKPw8p6vk9A_FxzhXnFiEodYWRbkMoEHz4k1Cui8pn3abjsFUnZ0nopQTXXmwDFSpiWuGqINVy4rPHlNpX_f5Ihp2Ga8pzzTOKae-Tql27wrydBiwRjLBgjv2eykbt2xB5wgYoOH_e_wrglN4Ml5ValYl3mJP0MBiT09V2-53uhwb6mo_DBRw7dUTGq44cSv89UCmNWvllX2a4iPUTpMr9ja63aO41czllDlFAJ0POWKg9DXCPTd8PO-gMnBBajKafUkpRB-uyXj686vpsnCDeA-nzad8UJaAkR1aaa1TXRugdONM-LYBGlgOQnmUUwYA28Y9h47a2PiwxH4GdDIkNotsAE_zHEpvu3pOtv4enEPwsOcf1vvaMIvB0p3FGsKwRzQjOMZaeXrjQlpziSO3ngA5K2w36S9No-SskoSewgi-yee2-za7lkYRQlwAvMbmCfTt9s6USIjSKDxwMZQdbb27bjcLPGwpOBCvYtPYEw2j8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول‌بارسلونا به لوانته توسط ژاوی اسپارت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106366" target="_blank">📅 17:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106365">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دقیقه ۵ ژاوی اسپارت زدددددد
😐
🔥</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106365" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106364">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بارسا دوباره اوایل بازی گل زد
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106364" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106363">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106363" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106361">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1J0x3uhnioGpP7MvSe-nDlXvFOcRaedcw4PHVm9f_im9lNxaRuGHFmziqNd9d_kxXFYmwwFdBy0HlEO9N2ak0cv-Gch54CW50xOObXhkQnuNHTrt7XKtLuk69WxIqxoKY-qiXHWeQNNraWi9cey49im8IDPmZlMi1Lw31CyfOK8TUoSpguiHUCtzDFad0LnAPBSeRJg9Zz5QVpWAxUElSAewMq45m7F2mfqltFmEYisPO0Z_Qy7HOmE8EfrtrrrK52N3e0SfukZQMxAUe8IUIYBedhC4tKmlchTIkXkkk4fnW3jKegzReMu6JP-QCdvtbER2-IfIbcY4RExeDDTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6NWmMC7Zm4QLoa36VWDE-Me0w2KCrDBCcXdVp9IdcBCrk3pUfyJS9ebMygXV4H5qzqFtQhYYXI52b-xaGDVIJAN88rwr8PVjm_eLEhLIM4_9-kQjGO4_hASNr92VWXT4i2icmVaEbQVZrO29c9nq_M01GW6VKtKtaLXdKUeABj8PJmsDmuttO8VAilBT8IS3lfnu1WLCs9MTeF9pdXn7oWnUhXBPtO4V1h7FucKX0YCp9aNS-JbruID9kp4h0derMs7kSd9rR3gc1ZUY7MtJgECR0TJePifp20_EmlgA898yu2vwoDrGqpUjQgpggEuTpHZDbZXQ8U4YyjKgs6zRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ ترکیب دو تیم منچستریونایتد و سیتی
⏰
ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106361" target="_blank">📅 17:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106360">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a36fb349d.mp4?token=e43gAeNake8x7MQzFv1ya9kTbID1VjwVdxCgGbYC0dQOeUI52y3MfglNFUnJRI9fx5JTOEJQzE_TWeLExCZhcJpMN-38ir-uGyT2qQBJMGs5-v5Vpr_Qie34I8A3HnCo4W9OtW5yi3yZEn6aog_lpoMYFSZUdf2Js_zVC4ZO19GaLG2S3NbyM8JoQXSjuIv1BWvQrZYNR1gBmHmRq-xaN1qSzLtnQ8n31-wgdwSj7ObUbLCJhgs_sUKDGyJ6CMasCoktpa8-VwxIL-pxczL67XRHmr7aUcmA-x9R0-6QwHPkl1t07s9DumRpO3ysEF43n3CJrs2EoFmWdcGIESITPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a36fb349d.mp4?token=e43gAeNake8x7MQzFv1ya9kTbID1VjwVdxCgGbYC0dQOeUI52y3MfglNFUnJRI9fx5JTOEJQzE_TWeLExCZhcJpMN-38ir-uGyT2qQBJMGs5-v5Vpr_Qie34I8A3HnCo4W9OtW5yi3yZEn6aog_lpoMYFSZUdf2Js_zVC4ZO19GaLG2S3NbyM8JoQXSjuIv1BWvQrZYNR1gBmHmRq-xaN1qSzLtnQ8n31-wgdwSj7ObUbLCJhgs_sUKDGyJ6CMasCoktpa8-VwxIL-pxczL67XRHmr7aUcmA-x9R0-6QwHPkl1t07s9DumRpO3ysEF43n3CJrs2EoFmWdcGIESITPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⭕️
⭕️
رادان: بیرانوند شامل قانون سرباز قهرمان نمی شود
دروازه بان تراکتور از اول مهر سرباز است و باید یکی از تیم های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106360" target="_blank">📅 17:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106359">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgH97YZwlbbycskZEnn0eo1TGYJkoozicQIoDZMJLiowiEq0LxS0bua371WPsXElFl2Lt4IVwuWkFc0lK-45d7Zmsq-4lEPc2clL6wcADi7Ehjh3rImI6aHMXSOsvheS-WqMKji9NdRUIhbRnJ9PvjW25c_ELnE69GterJ78AyAlMX6MDKIiEWL8ccFUe-gLeOm54JZP1k3e1_Akt3wklag3w5ko_kJCKTaQvI1kZ4U8GTNnxwkK3QoCoPPC99xGYqfT7gLBTaCP0FKu4jmG5-FuWHbQEqxi67gJvcnVUY_dAq3QlkQ4aaN_LxZBuyhEVKZ5KVGoz-ZyApXcmH3tnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه گلزنی ستاره‌های جدید بارسا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106359" target="_blank">📅 17:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106358">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rnw_KVCZCrxIRkkKEky1d79Li7YLuLDHIuXHM8C0n_UevOYfGlpjw0VxtRVBAK7KeacTJ-p3nm6iz_tubttEqE9fPKZvl8A6r4EniG5DndY-NICGzwn5nKmVBQlL4kDKsTy7gpXLg6xuku-Eu4W_TlAjShQQeV1GaDKvIveZTz_zQUZ0ekHyrKsNWt4ZOM3FzZYvoSkKS2vjra1UpouSdY4WCHi6wxu91_Hht4wLEQtZlkpw3sByAKQHQZXr3SomNIVvvLd50OPJkt91Q2pVisrlenKZygYVn-Wfakvuy3tLRxi5eoMVCuJ6Z_gFkXzfYI5h0kIUIsfphOl_G1w4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇪🇸
شماتیک‌ترکیب بارسلونا مقابل لوانته
⏰
ساعت ۱۷:۴۵ شبکه‌سه سیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106358" target="_blank">📅 16:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d01737ee.mp4?token=svz3-ksTjfQjtlAA2MC1S1nYwtRgOjuQCzkeiovQAnVIcnIIY_mk8Gegr0mCbbJf_mI_iynrsBgWpUWO9kUyh8DlW16JnmyMlKDdnip-CzqhRpOcoT6U839zWrrzSQeJpG5dFuaU5n_ODcRZM-YMGJVGwvct79XAa4kpwgMOm_3AfJIBAmQthkKvsBqMBxWRxGXqcL1cgQUVcivVR7NjJ6Eifg7afIJAF22Nl4YPbtwR5d_7PTOfli6pkQAz8VwvaCiZL_aZXtBXnwNP5dPtjF9RsvhZ9N9PiQZxNP9u5Xe4AEAqtp56MsDlIp362iDkusX3o4R6moBHj2WJ1fcT_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d01737ee.mp4?token=svz3-ksTjfQjtlAA2MC1S1nYwtRgOjuQCzkeiovQAnVIcnIIY_mk8Gegr0mCbbJf_mI_iynrsBgWpUWO9kUyh8DlW16JnmyMlKDdnip-CzqhRpOcoT6U839zWrrzSQeJpG5dFuaU5n_ODcRZM-YMGJVGwvct79XAa4kpwgMOm_3AfJIBAmQthkKvsBqMBxWRxGXqcL1cgQUVcivVR7NjJ6Eifg7afIJAF22Nl4YPbtwR5d_7PTOfli6pkQAz8VwvaCiZL_aZXtBXnwNP5dPtjF9RsvhZ9N9PiQZxNP9u5Xe4AEAqtp56MsDlIp362iDkusX3o4R6moBHj2WJ1fcT_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🟣
با وجود محرومیت در لیگ‌برتر، خداداد عزیزی به درخواست زنوزی قرار است در بازی‌های آسیایی سرپرست تراکتور بماند و کنار زمین مشغول چانه‌زنی با داوران باشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106357" target="_blank">📅 16:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4IUQ32WmMzit5JjvdUzjgsJ3zLR217rm-4EzqGaL7CdDwB3YyeQa47HmNBLAGIBee2qZ3RrtkVFwQT1YM2a1oZK7v2eCcYFhdfaE4zHl24N3kZmDCvfw396aYHRE-me2-JYEDVYSL1GPHqwSBs52qamq8jzN6IPTfDizO4E1LlTsMYX4SflfzgTfwSIh2IuFGk0inYUkCJcBplNW3ScTMIjZ03Jg45UwVVDhYVzOsaVMcG_2moYTaGKQwXgewdrA7OZqG8yb0iQrO6CRdWMbFymyy7TcoY9_5VqJYbLJ-VBZWwqx9ggjmveLw13MyLURrMqyHSGpW4z7Vl6xPw5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇶🇦
السد قطر پس از هجوم هواداران پرسپولیس کامنت‌های پیجش رو بست تا درباره یاسر‌آسانی مطلبی کامنت نشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106356" target="_blank">📅 15:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmL_mR8cy8s4Q-zrYh4iNNGT-h3OniKkHD4ZjKEramEjga6JSaxofJCmv3Ow6CB8PgdbrUS6NTouzdW2W-XZx5YD6gwULrGqHoYooZUJO1h9Y0nX3F23gfqIUQzC8PVYPq4rKlRj3pMcuBwGwLjscGVojZ_qocA2cueHzgDWprMwzmQ0fdpv6nhxwM8odlvCWaKzlfB4ZgNk7Q-IJGOVSe787eDqbNaX_ZWty6zDegsvANYiddMuXGcs7xtm04IMoKnuqSs0699vdx2PrHX0A3d5yihOXuGuOS9O5aESPD-vub-k1RQbtfFf18lKEJ2S_CKBymcp-HGIj_ht3Ku_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق معمول ده بازی گذشته، مقابل والیبال ژاپن شکست خوردیم و سهمیه مستقیم المپیک به این کشور رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106355" target="_blank">📅 15:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری داماد سابق علی‌پروین بعد از 22 سال؛ آرش فرزین: رهبری فرد و باندش، سرمربی پرسپولیس را کله پا کردند!
بیست و دو سال از روزی که آرش فرزین حرف های راینر زوبل آلمانی را ناقص ترجمه کرد، میگذرد و یعد از این همه مدت، حالا داماد سابق پروین، پشت پرده آن روز را افشا می کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106354" target="_blank">📅 15:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1b2c19a26.mp4?token=s9lqk6eb4_-_Xz_LdXqOxy_jCizZaxHw8EtRw9Uq9BLDHYncsaLN2NFt_RBE8NSbQZySsHM4i3OKo8mVvYz91rUrNaWc95tPcOP4-rMhbtm2RLuYFCGfCnCGM_7OWJgPFuDMsgQZivNVE4UAcOekVk0BINpdDUwyAu_PlE2llft76_FTWkNJui-x2zHG6GAnS6aqyePJ1EShMMdxJe7CB19Wbh2TsrI4ig_e4d00MkPL5efX_cKxPHw5P-OwSsw8Ei39_Z10p6kaSgCsWj0YflWRl_wV_qPt9SmZ5hIUkTV6_YIgkytAAPm-6VIwDAMc28Dj6TlZvdNv0OypuCMTAaSbA7iovVV5gwk_YWkrF6XTDPe6yII27ODSMhRH7SwTl8xE5fC2J8iy98HHFoD63wiyc7BuxQRC-cu24W6_QWIqLn1rz68JCP_-vwgS6ZRYs9yfmWYxq513qGVn6pYjnJY8jxYGTiOIenAC3WQNSHFW7lE1JQfD68Uf23Df-jPwe5vOOytiHQQpyJAvZCaNkU1Io_9Mlm1RfiLsSbqRG6-TDg97lB2n5pm5j_kvmkG50jf0YKGL0GcG7KYDsMI9ZQ2Q_aVQUkXhegKEnmfo_JxFmUe2EXqsVzA56dY1uQwp1ouxUyt-1yflKmfReDic5MIi7YdGlbR64CfuGtAIzzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1b2c19a26.mp4?token=s9lqk6eb4_-_Xz_LdXqOxy_jCizZaxHw8EtRw9Uq9BLDHYncsaLN2NFt_RBE8NSbQZySsHM4i3OKo8mVvYz91rUrNaWc95tPcOP4-rMhbtm2RLuYFCGfCnCGM_7OWJgPFuDMsgQZivNVE4UAcOekVk0BINpdDUwyAu_PlE2llft76_FTWkNJui-x2zHG6GAnS6aqyePJ1EShMMdxJe7CB19Wbh2TsrI4ig_e4d00MkPL5efX_cKxPHw5P-OwSsw8Ei39_Z10p6kaSgCsWj0YflWRl_wV_qPt9SmZ5hIUkTV6_YIgkytAAPm-6VIwDAMc28Dj6TlZvdNv0OypuCMTAaSbA7iovVV5gwk_YWkrF6XTDPe6yII27ODSMhRH7SwTl8xE5fC2J8iy98HHFoD63wiyc7BuxQRC-cu24W6_QWIqLn1rz68JCP_-vwgS6ZRYs9yfmWYxq513qGVn6pYjnJY8jxYGTiOIenAC3WQNSHFW7lE1JQfD68Uf23Df-jPwe5vOOytiHQQpyJAvZCaNkU1Io_9Mlm1RfiLsSbqRG6-TDg97lB2n5pm5j_kvmkG50jf0YKGL0GcG7KYDsMI9ZQ2Q_aVQUkXhegKEnmfo_JxFmUe2EXqsVzA56dY1uQwp1ouxUyt-1yflKmfReDic5MIi7YdGlbR64CfuGtAIzzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
ویدیو وایرال‌شده از آغوش گرم دو بانوی ایرانی در جشنواره ونیز ایتالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106353" target="_blank">📅 15:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ecf94960.mp4?token=eokE0MDvY8sDhbkJgSo6yI1lmOj5F3y4xrIsR6a1PTue13jlYPz9ngmIVW8wzJPwwT9CqZC83jE2m30aNUG5muDBzkHk_dL1e-eMz-Ofpxf5YBH4aSfhaOV2iuk7JczJcOBwsL_BvGzV1_2cKbeYRDb1uq2nO_4kh4RFt_14LGaHgw0vpn0Ka_qewy7HIpQIAgL3y1BvZAXccYJQsulpwrZlr1yLPI7yFbEHBEsHlq3pY1Twnxyp3ZCKWq8YnFt2W-YKbrlIiykF8NMApDEK5_ZvzVFVxMl53pMoeMvpEv5DEaZDGc9jH8tDOh02nfnVhfjvLU4GOtXiEzXO1ONhtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ecf94960.mp4?token=eokE0MDvY8sDhbkJgSo6yI1lmOj5F3y4xrIsR6a1PTue13jlYPz9ngmIVW8wzJPwwT9CqZC83jE2m30aNUG5muDBzkHk_dL1e-eMz-Ofpxf5YBH4aSfhaOV2iuk7JczJcOBwsL_BvGzV1_2cKbeYRDb1uq2nO_4kh4RFt_14LGaHgw0vpn0Ka_qewy7HIpQIAgL3y1BvZAXccYJQsulpwrZlr1yLPI7yFbEHBEsHlq3pY1Twnxyp3ZCKWq8YnFt2W-YKbrlIiykF8NMApDEK5_ZvzVFVxMl53pMoeMvpEv5DEaZDGc9jH8tDOh02nfnVhfjvLU4GOtXiEzXO1ONhtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبت‌های شنیدنی سعید دقیقی درباره تفاوت سبک بازی اوستون اورونوف و تیوی‌بیفوما دو بازیکن پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106352" target="_blank">📅 14:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJGrm3gns9s1jJfdnkoe1v6zpgZO1W9Bfa8MjfFxqZNpEpUPOI4SDla2T3_b3K-ogzbtKee4c2rsl5D7ISnBdoAHwPjNTuvuVaHM0jPFstdUWKlPsSzGDRFucwDKhN2hw0_ciIrySAJuC-2PcN35f18vZ-RxHfFZ2rNet46oGFrWUK_LEp17HN6sz0TpsCS6sTth8hEt3CFuUs8ld9HxLLJ4ry3qnSAZKMbRcXvwwY99hI82urDSHZTQpPf9a7MYEOosObEkPRj_TRV8riK6-ZVWqsV2m__Q8PO9Y2osp2Uz669_4--ocA7gyRR8yh8LAiO3NPjXJkmH5PzpFGH_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
هوادارای التعاون دیشب برای اینکه برن روی مخ روبن نوس، بازیکن الهلال، اسم دیوگو ژوتا رو که دوست نزدیک نوس هم بود فریاد می‌زدن.
✔️
👏
نوس هم بعد از بازی درباره این کار مزخرف هوادارای التعاون فقط گفت «امیدوارم حداقل بعدش نرن نماز بخونن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106351" target="_blank">📅 14:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2eae5e40.mp4?token=bYB1Txquel5ZMZyb2s2nCX8hKcrIIMay3Qmk0VHPDqbN-u-wdJ2sFGvNGI6GkkpBIDIdOfEwdzBxV73pJuKg3r3jIvwRwKmEFQwQjkdfqnNaQ12aWjV9PRQf_1JHm9_NSZFOdptL6NPUryWrDNAy12AIVzqXREFpnyXc429LYjtTPKsaJ_cIwbHPp84GEs1CnyWWGt01tTodG0JJN1I8Z-ylNfZW6pDwbWcD_YLe0xbJ3qlR7kK-1Hd2NK7u_2e_ntuo9z8kqJMDNFp0KUo5JR3NgBeotnZo0Pk0-ePdn9yr8n1kE8BkALN7GNyELlTi0LKa3MTHe8P56UHgWjRgBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2eae5e40.mp4?token=bYB1Txquel5ZMZyb2s2nCX8hKcrIIMay3Qmk0VHPDqbN-u-wdJ2sFGvNGI6GkkpBIDIdOfEwdzBxV73pJuKg3r3jIvwRwKmEFQwQjkdfqnNaQ12aWjV9PRQf_1JHm9_NSZFOdptL6NPUryWrDNAy12AIVzqXREFpnyXc429LYjtTPKsaJ_cIwbHPp84GEs1CnyWWGt01tTodG0JJN1I8Z-ylNfZW6pDwbWcD_YLe0xbJ3qlR7kK-1Hd2NK7u_2e_ntuo9z8kqJMDNFp0KUo5JR3NgBeotnZo0Pk0-ePdn9yr8n1kE8BkALN7GNyELlTi0LKa3MTHe8P56UHgWjRgBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدشانسی‌های لیونل‌مسی برای اینترمیامی در بازی بامداد امروز تیمش مقابل نشویل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106350" target="_blank">📅 14:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6ed3f485.mp4?token=aNzxpAYsRGkm8UOXztkVLXERumTdCTT7KpNZD2ZJ1rXHk377nHjayEoRUraBjajhLXap5OvYlY4eRR7h3d4RtEULbMfXLqmrD6zwsR3KxVG5DxhagT13_8iRPGXwIVUbd1Hd3n6uBfw-J2lRpZsRt0ObXMkn0OQskDiNw794Lw0CAaVtEXhms4E50M3TTI8V6ahhzv1YpHu5o3yzoIGM-zXJLfZpgQwqDKkmNCemLu1wc1dFwzPRd7y1h95EpZzc5EBZKrNqf29RCCUmyYyHLiWFNi7Q7uHZUvpU7qiG6yweM4PH98Eudb8TDDIRSO3dof9vywJ81Baeh49KJkX7loWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6ed3f485.mp4?token=aNzxpAYsRGkm8UOXztkVLXERumTdCTT7KpNZD2ZJ1rXHk377nHjayEoRUraBjajhLXap5OvYlY4eRR7h3d4RtEULbMfXLqmrD6zwsR3KxVG5DxhagT13_8iRPGXwIVUbd1Hd3n6uBfw-J2lRpZsRt0ObXMkn0OQskDiNw794Lw0CAaVtEXhms4E50M3TTI8V6ahhzv1YpHu5o3yzoIGM-zXJLfZpgQwqDKkmNCemLu1wc1dFwzPRd7y1h95EpZzc5EBZKrNqf29RCCUmyYyHLiWFNi7Q7uHZUvpU7qiG6yweM4PH98Eudb8TDDIRSO3dof9vywJ81Baeh49KJkX7loWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یک‌شهر و دو تیم برجسته؛ به دربی جذاب شهر منچستر خوش‌آمدید؛ امشب ساعت ۱۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106349" target="_blank">📅 13:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106347">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cY6sYR1WU2MXbghl6Qo-2X-3JqybrMlE3a3PvUqKVaOw8DJYgQDD-9IayYANw8AsnyPvy1f1qh3VAHOkUgmzYS-4VFMT_JFtEfipZwwvQyzae0L3kYyepRteJHV8Ocoy0zfVoXgzs8ohRS4ij4RHtcvPzocPcM143F7P-Oz3-U1ZWkCChMn7xNp-7PjpnnttV_NFfeb-TVqrjz70phGjmkfo7ux92tkVZae_gWLHEVBwKROy3V43mxUgYemTjISS1Xwd44G5fGu67UbiapUhFMLb3ZD5Sv4aLNq30gFgWZAUD39wRlPWkO9CqyJwa6-zhioOhH-rAJhV2g6EcPuGyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qqn6Tts0RyMeR-PKWuTt2RJSfeegebNBLT58YQhCICSrObmP8wb71WKklM5XAVuReAz8OSdd2U14IW_3iPsCwir-KXPdHyr9s-MQE__hVL_aPV3P7BG1QgjtRUKFgI-UgtocMz6xFPMQrJfh5MIVMJZ2zIJpJIvbH2yvu5UikYZ-IhTFFfl-rBRxywlg1TyxsJEycKCCsQLvdMleOdc5NY4u0Q7Nx88jXOx6Dm-3_5fx4Zj4p3fD0nMeu0Cl3IBnUNqu5mNFf7_4zId09RPsF6dWCANCnR-MmjjQN1k4BJ78x61Le1bh1QKJPXBXKUEsFE6eti9hQcUsjErsYPsqSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
بر اساس اسناد منتشرشده، فرشید میرشکرایی، مشاور عالی و منصوب جدید تاجرنیا، پیش‌تر در پرونده‌ای شخصی با موضوع «خیانت در امانت» به یک سال حبس تعزیری محکوم شده است.
حالا این سؤال مطرح است که چرا پیش از سپردن مسئولیت و منابع مالی باشگاه استقلال، استعلام‌های لازم درباره سوابق افراد انجام نشده است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106347" target="_blank">📅 13:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106346">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJLnA5aEKDQeVmTE5xVx2Z0QaRNW83hIZVm9vV6Apd1MlqD7qB2wf2Cn7LvddhHJhUJbU6PQAnhDCcM4Aksy6OWM16BqNUL9dPqKT050L-9BsZEQXRk6z6-8GDGISt-WoXWdxfMGE3oxypBlIJABu40EZ_HsXs4N1zuFbwR2lxX1IjTa9Z0wBCrK95bSyYIyOvuOlxkrQY6grlfacCWtYWk_6BnXtmzPFJlsIiX5gCItUku6Tcxj_-5oA4agn-3lmKsfKia-uUmgus7pbfX92nZcuo4yUWrtaSu6hpUzfVpZUbCAYR9KE1-zn10y2rNNNaH0ERQrHil2s8Ay-YasNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
فینال قهرمانی آسیا 2026؛
🏐
🇮🇷
ترکیب تیم ملی والیبال ایران مقابل ژاپن
؛ ساعت 14:00
🔥
قهرمان این مسابقه سهمیه المپیک میگیره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106346" target="_blank">📅 13:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106345">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddad7e35de.mp4?token=XUuQzSiqsDMlUV1dABYi3ZB62m6vRuQ62bQXXSzllQtUgtyuVekki0Z-8w3XmY-Ws6I6CTwLCHZOhMIjzeyKxdNAoWUeHeZ7dRuCkE4-I1pkTE0YecTYXfOpOx8LhCqIMeMTsXusHLpT3hkc_kAm9rOOr3dnUcjYDr9mPkKkUR2DfMTKB-l5pn30xEBtFiA5d4QdoIueS4yC2DBRD7Xt6i6B4phmJPlQz7Nega5PspV3rOdikCx7retguIh5fKRPi09KHYSlQUQq2jaTDGmwDc-o1D-qwl6kwk4UKUuc7X4RWbd85BL-1vwFr4Jmi7NkpKjlU_SDqm0TbU8V08u-qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddad7e35de.mp4?token=XUuQzSiqsDMlUV1dABYi3ZB62m6vRuQ62bQXXSzllQtUgtyuVekki0Z-8w3XmY-Ws6I6CTwLCHZOhMIjzeyKxdNAoWUeHeZ7dRuCkE4-I1pkTE0YecTYXfOpOx8LhCqIMeMTsXusHLpT3hkc_kAm9rOOr3dnUcjYDr9mPkKkUR2DfMTKB-l5pn30xEBtFiA5d4QdoIueS4yC2DBRD7Xt6i6B4phmJPlQz7Nega5PspV3rOdikCx7retguIh5fKRPi09KHYSlQUQq2jaTDGmwDc-o1D-qwl6kwk4UKUuc7X4RWbd85BL-1vwFr4Jmi7NkpKjlU_SDqm0TbU8V08u-qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
دلجویی آیسان‌اسلامی از هانی‌رامبد پس از مصاحبه اخیر هادی‌چوپان علیه این مربی برجسته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106345" target="_blank">📅 13:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106344">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0dd00f3a7.mp4?token=Z2onH3RWCs2Q4L3YjPjFAxo1NFRgXKxxmbdncrokW55CMS_oZr-cIEJSt8IOJCXCKsYfuo7C7hKI6YI7oLMv4r6WDBqz-_iF6zuGYY4N5rH9OqvREHUsECaYR5L8MPeL1DfYSS0AUlF-JleoZkYCswruhbF4Emh9goL-AApiBRRmSDLCtkQlL_19CeiA33hTy3t9wR-ZS4oy06NAYWpZgdDdt3dXnQpo2TFvGRiLYB3XJQTDKlzYtRRc1qX-Pt1GDyA0bKW4jOUu1vxX6cjNbTWFXjKFDKeIGnwgquaKFq1Jfg8sJ1ofwFawbfcnD0bLabGG96yEuoAewFYcSg_lGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0dd00f3a7.mp4?token=Z2onH3RWCs2Q4L3YjPjFAxo1NFRgXKxxmbdncrokW55CMS_oZr-cIEJSt8IOJCXCKsYfuo7C7hKI6YI7oLMv4r6WDBqz-_iF6zuGYY4N5rH9OqvREHUsECaYR5L8MPeL1DfYSS0AUlF-JleoZkYCswruhbF4Emh9goL-AApiBRRmSDLCtkQlL_19CeiA33hTy3t9wR-ZS4oy06NAYWpZgdDdt3dXnQpo2TFvGRiLYB3XJQTDKlzYtRRc1qX-Pt1GDyA0bKW4jOUu1vxX6cjNbTWFXjKFDKeIGnwgquaKFq1Jfg8sJ1ofwFawbfcnD0bLabGG96yEuoAewFYcSg_lGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
برخورد ناخواسته علی‌حاجی‌پور بازیکن تیم‌ملی والیبال و یک هوادار ژاپنی در حاشیه مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106344" target="_blank">📅 13:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106343">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUVLMX-pmu-unzU2oE1JsA-9x1K5jg9oyKqhZboKKIA39gGLPq8Ofe1PJx1eiZMtlKg_85Bou_0ObzR4jQGQnrZBykMyEKN6olrdWWxJ2HJa2J4rrmpZ6oO2O29xaQyJ9hr6ZSRE66d-AAfLBn_nphDNkkUg67d0q84Oyq4QkjaAHFfm6Ns8hk6Lc74_spZK9wXv9CTZ8XnevGCPq8qerSDjYz8Rb-bOcedAa7zUaTiTr0yDfa0wuEl-H8Rdc0Kln8rCZjDd8VsmeDz8FjkwjeCKuOnSVBrsBa2aUpHj3V0Sm7LP_XnbzphF358kS0U9Jno9GOonwe3jcyYWuq3xPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
‏
📊
نتایج دربی منچستر در طول تاریخ:
‏
🏴󠁧󠁢󠁥󠁮󠁧󠁿
81 برد برای منچستر یونایتد
‏
🤝
54 تساوی.
‏
🏴󠁧󠁢󠁥󠁮󠁧󠁿
63 برد برای منچستر سیتی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106343" target="_blank">📅 12:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106342">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siCCvRBTJz27HNH9lutmEXgSD3WKz0tdF9tnlHJNBQ2oCI9_Ec5VDeJfIqGld1JrJvNUUZETIfjDt2saXznjn7PclM4yVa-Hlik2rkGTR2LFY9L50md3WYn1vyc6y-XCUc182B4uNv-yNpzZ0NHESrvt_3acPiuNe7T0EPFQrPNpKfT9e5OlYAa-0Htx3FoZvgJfJmZXsbqSvvufcb3aAeIbMdafMQI6GJdGb1XXf2vJsK4-8hknVd7AQKny8kNLRW_zE-LoY071-BgWTHd1NuMkBjGyS8gjiJ9GlCCywi42aiMpMT2slnW4rKKXjKnZs58wypvfKEs8buXVJk4Z8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آمار یاسر‌آسانی در رقابت‌های آسیایی:
🟣
آمار آسانی با گوانگجو در لیگ نخبگان:
🏟
۱۰ بازی
⚽️
۹ گل
🅰️
۱ پاس‌گل
🔵
آمار آسانی با استقلال در لیگ قهرمانان آسیا ۲:
🏟
۸ بازی
⚽️
۴ گل
🅰️
۱ پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106342" target="_blank">📅 12:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106341">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCKjolIDAYe5aXKnTbeq5hsPhx02Y8nWRLrAUeo06MzkqN45KU2DUENSGSfNtNnkp7dpj6m9wXoc4L1TEjv7unq7vEpSazaCozHAH_UTO6UfEqG278Pd_2t8jPhck2FFS69LUOY4VSjNQbbqqViwZQl70iDTxif0JPpbj12_IYnxQ3pdm-bMDgcssuTvJt16bwcIq2-sC6ZJ6f0CtZXPgh8vtY2lBGhYorpm8luMoCDXR-Tx2ibdC6eJxZ5S2XZA7qn6K2oMGyrT7cTZ5A3W_Hz5K1BX1ykJvcAtleWyYfpxVQBWIkvKWZSTFTPZ9e5GqG-tNSOC4vAKwRQCpxKRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇪🇸
خولیان‌آلوارز از لیست اتلتیکومادرید برای بازی با رئال سوسیه‌داد خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106341" target="_blank">📅 12:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106340">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2faf6374.mp4?token=GQQh_LoABYb_jYcnV3HahezB-4AlXvV_3hc3bc9Fw7ENP519WJdViYDkRZLhs1-ns889ihLb1dhhMVaPSao3KLvfMxPuRLvA8_29Y7tnSjGtO7f4lPrP_Y9-iGOuD-HIIR74Jm392NgVKkCCK5iU8XaonotB3_8C4_TYYrTc_5XjgSqP4tkVbygH0kuk8A-K787yuVWajrDkhR5uQKdZKb8haXOxgxRSN0dBgSyaq7q-ttr3gKNIU-zvK-CuVm7jeWkC-DEy8qiVIu4QlL9xJSUPmiOnLs62M06AqNW4plY-r6syJKsgKaddUCDwZThu6Qz2vb8VR9JTKamiJS36rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2faf6374.mp4?token=GQQh_LoABYb_jYcnV3HahezB-4AlXvV_3hc3bc9Fw7ENP519WJdViYDkRZLhs1-ns889ihLb1dhhMVaPSao3KLvfMxPuRLvA8_29Y7tnSjGtO7f4lPrP_Y9-iGOuD-HIIR74Jm392NgVKkCCK5iU8XaonotB3_8C4_TYYrTc_5XjgSqP4tkVbygH0kuk8A-K787yuVWajrDkhR5uQKdZKb8haXOxgxRSN0dBgSyaq7q-ttr3gKNIU-zvK-CuVm7jeWkC-DEy8qiVIu4QlL9xJSUPmiOnLs62M06AqNW4plY-r6syJKsgKaddUCDwZThu6Qz2vb8VR9JTKamiJS36rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کاش دوباره برمیگشتیم به این‌ایام شیرین...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106340" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106339">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106339" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106339" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106338">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cfqb1jXZGXTPgji9_oJN8OgqphbKtcgXUbEk0b_daGhuwTV1hpUor32-ssiLN35UOGKkmN062ztpNXuctz4RR6k8padvgiE5aA907WJ7JI3UyIH3-wHCE4Nx6yUMGONlETPIG9-d96Ssh8VjgOhJxP71CVIzKUCTq9AGzCpIK76qi-PSa4j2_lHy44gYuKLQ-2TNU0leuO5mGCAKIE38cv2H3wLz_tMuGqq7FAZ_kzqvt4lN1Fw1iAWQnHhydQogkDtzPFD_UQgb35SVp2rkWsl0g-U6CbrQNw6VTwoDJTUx7KbtNFZTOxy7PXii6gJo5tloKjBTD_rirxgzKSKdUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد بزرگ منچستر در راه است!
نبرد هیجان انگیز
⚽️
منچستریونایتد
🆚
منچسترسیتی
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ دربی اخیر منچستر:
⚽️
منچستریونایتد: ۲ برد، ۲ تساوی، ۱ شکست و ۵ گل زده
⚽️
منچسترسیتی: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106338" target="_blank">📅 11:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106336">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsrzUDCaY35Ncw8ZUWugLGQQPUUJNfW4zwTvLr5EjR4G-mvlbkKUajhP73TowYkCWMmqBgp3TAIUHO-l81G6YuGExuy1XBTNX9MDYPiMus_ptwuEwTWsv3Uj8RoMG6cJXM7bKTAJRQO10ReR4vFXLIS_zCCu8aHInosYLqGYlgBQH4kQyFacfQ0fqGD5wG-mr0qqUAvw6GTcK3kxT8-UvwmPxnQIJtuc1IqjDKVqTqMuoAg0Cr83-13rOoflTyhA7BkJMnipNlyn3hh8QFePMiU5j5tEIsR_KFYaZSLxAgEmZw2e7YwzG2KVc9-YVVsyiJ4lHevk8lhZwFGkTV1cEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇮🇷
پوستر باشگاه استقلال برای بازی با السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106336" target="_blank">📅 11:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106334">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe38a96709.mp4?token=Vao9zdpvblP-u7k0SFi5g8hlz49B44HswsJa2RyRtInBORqT_glLl_HY2D1lQbj0_zQnzxVt5TFtooOgd5_EEUxfipP52fyOJtXaKFRoBruqCH57NDSXTcE1qiXC4BvFp8T0whP8FXsCm3vZ2SvpfAy2iBX062vTl_z-RkH8OyB9VYrd7qCJCOUMH38ANN5DOBZsQXkKgbk9J6h1sJ9scig-8do8vRTG8NRspK25ORPu6KexHL2QJKqnGlf9OhjVCLoss6wuCj3cTSUOMfkxSRn2SBZhkyAZRnklIaDFZ6Uy2o_8To-OiN4gP27RGootxu1JF24O_VdhC2hH088LxES-ONI0bHffm3tUcqnM-HT7a_quJn97ACqB52XtPGDfzvimNXByxTZNeFBkdlD5NQpeAIKo7d6M-BRV5w5CMkegBgphUKA5ErVpdDPNrqzw9lPn6LDKo5YIrxCFtVki5r2Q9RV8xsphAJSl0OAyrc1CFUfJRwFT22__ob2D52WFVhMEY1pan4SazU-U4UzLGPTt7n_B40eKPzH3E_BcUz40WSb8t9Hli0DSS2mKiSl4paRk3fwX5AroeU2Pd5YuRFttRa-gk9iCQBRC-dga8QjkSaQ-6HH0IRWcLuRksDgqlKXjlhdfVhbnDOswhi1Whfb4QSsGlehaIxPchjZMazw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe38a96709.mp4?token=Vao9zdpvblP-u7k0SFi5g8hlz49B44HswsJa2RyRtInBORqT_glLl_HY2D1lQbj0_zQnzxVt5TFtooOgd5_EEUxfipP52fyOJtXaKFRoBruqCH57NDSXTcE1qiXC4BvFp8T0whP8FXsCm3vZ2SvpfAy2iBX062vTl_z-RkH8OyB9VYrd7qCJCOUMH38ANN5DOBZsQXkKgbk9J6h1sJ9scig-8do8vRTG8NRspK25ORPu6KexHL2QJKqnGlf9OhjVCLoss6wuCj3cTSUOMfkxSRn2SBZhkyAZRnklIaDFZ6Uy2o_8To-OiN4gP27RGootxu1JF24O_VdhC2hH088LxES-ONI0bHffm3tUcqnM-HT7a_quJn97ACqB52XtPGDfzvimNXByxTZNeFBkdlD5NQpeAIKo7d6M-BRV5w5CMkegBgphUKA5ErVpdDPNrqzw9lPn6LDKo5YIrxCFtVki5r2Q9RV8xsphAJSl0OAyrc1CFUfJRwFT22__ob2D52WFVhMEY1pan4SazU-U4UzLGPTt7n_B40eKPzH3E_BcUz40WSb8t9Hli0DSS2mKiSl4paRk3fwX5AroeU2Pd5YuRFttRa-gk9iCQBRC-dga8QjkSaQ-6HH0IRWcLuRksDgqlKXjlhdfVhbnDOswhi1Whfb4QSsGlehaIxPchjZMazw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
هوادارای التعاون دیشب برای اینکه برن روی مخ روبن نوس، بازیکن الهلال، اسم دیوگو ژوتا رو که دوست نزدیک نوس هم بود فریاد می‌زدن.
✔️
👏
نوس هم بعد از بازی درباره این کار مزخرف هوادارای التعاون فقط گفت «امیدوارم حداقل بعدش نرن نماز بخونن.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106334" target="_blank">📅 11:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933458c59b.mp4?token=JhOEPJqpHrUkPfg3BKmRB5JXjeUBGgNkL39VrpH5rVu2meyVIHUfcDaqtIfDKoTjOXMll9g8FRgh_fhT7XP_nD-BpNbtVwWk2bjvnfFsNAfwWNx5JWtqRUc0NI2_eFJX0AJRDql4fMbxsYfwuCryh6gPmItuGTLWxzDvRjWPzO4HQipmHnmxW1wML8P-mzqSt3hAiFeZgUl_sI4I77_bKzGd4Drx_O-LTcnm_fZ0Dx3J2M48bdjarL-c1FM3aWL1v9zv_5lZbKhWNJWDJNxoRvzttEuWH5kMX6TXd2jwLjcvF3aGbQLWdPBvJjr36cPMEDz50_kZFhpFG3EWWbL-xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933458c59b.mp4?token=JhOEPJqpHrUkPfg3BKmRB5JXjeUBGgNkL39VrpH5rVu2meyVIHUfcDaqtIfDKoTjOXMll9g8FRgh_fhT7XP_nD-BpNbtVwWk2bjvnfFsNAfwWNx5JWtqRUc0NI2_eFJX0AJRDql4fMbxsYfwuCryh6gPmItuGTLWxzDvRjWPzO4HQipmHnmxW1wML8P-mzqSt3hAiFeZgUl_sI4I77_bKzGd4Drx_O-LTcnm_fZ0Dx3J2M48bdjarL-c1FM3aWL1v9zv_5lZbKhWNJWDJNxoRvzttEuWH5kMX6TXd2jwLjcvF3aGbQLWdPBvJjr36cPMEDz50_kZFhpFG3EWWbL-xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر به پوچی رسیده و انگار دیگه هیچی قرار نیست خوشحالش کنه.
‼️
⚠️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106332" target="_blank">📅 11:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJmehAsALFUgufKrjPXS8dzG2ODHY1uryxBABtm-Ojt5hSK8884kmZ4sILDaIPrLWrM0ebKoGP21_X-W7sfjLnURuhaBRGZ-2aWV3VzTGkSgB3MuY8L5lDoYClKrozTLWRMY9MT0oUdhPyrGoC6_nkVN76Y0q-km-8fhKbJBDVVa_TDe9fKLh-ZGULfaLVJDFPB6W-ckH0ipYBEL4Rr8IX7iNLA7G3y8usoF105lYOlvfuhFrX-Fb4O3jX1yXtO8OL-oI-ssjXjclro_5p1NH85aF7GSDGDrfN0CpZVufGs5g3dM6ybsGQ4XdEX0yIeeYvmYX5T1Bs6QG6BS7d5QdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
‼️
جدول بهترین گلزنان لیگ‌MLS
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106331" target="_blank">📅 10:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106330">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a30251b5d.mp4?token=AEyckByiax1aPdFSOjaL_6sAPWpX1bE-ODUUOcoVlL18LBWFp1eW-XuRPAzBMey5XciNZ5rm1Xt1Zh-lmLbeKipcKKeG0N5yFYt_cc8M10d4JJayCaYgHE_yXRoXngjU0XtgbGEda_mJ5jBKunbN5TW9szQgEUumZznbScz8p1huqxG6amO8TdDrKTVJsIfIJ__L5_nwVo9a4LcW1Dolb_9rxyQ2xJejLPaza9ZpQ47Ysf5_6-tmlIWv3F24qE0KH3kcOAPYLIziGd7bYqLAYgzyNGyh6HfBr6H4yCgdqx2tB-ALq4aSGGiI0wU0j8kWSRhh56q86zMg-QxLEaWcjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a30251b5d.mp4?token=AEyckByiax1aPdFSOjaL_6sAPWpX1bE-ODUUOcoVlL18LBWFp1eW-XuRPAzBMey5XciNZ5rm1Xt1Zh-lmLbeKipcKKeG0N5yFYt_cc8M10d4JJayCaYgHE_yXRoXngjU0XtgbGEda_mJ5jBKunbN5TW9szQgEUumZznbScz8p1huqxG6amO8TdDrKTVJsIfIJ__L5_nwVo9a4LcW1Dolb_9rxyQ2xJejLPaza9ZpQ47Ysf5_6-tmlIWv3F24qE0KH3kcOAPYLIziGd7bYqLAYgzyNGyh6HfBr6H4yCgdqx2tB-ALq4aSGGiI0wU0j8kWSRhh56q86zMg-QxLEaWcjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کودکی‌هممون در یک‌قاب
👍
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106330" target="_blank">📅 10:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a4aea1dc.mp4?token=YvXCYNhRaA8oH_4T8vhWAMJstyWRDaxvMC6b6bPf5wPyDAas0vkkHK1JD7xtCgn4zKeCc2qS8COYffe8uS3HH9yD639h9zRikLl97Ld7bSNHGBdhS2veaiSTj4XX6sOuBKBQqLSgImDTbNGU1M5ADo-tJfUR_kZft4z1ckf2gr1nmPhH7lqFJ0hU3YAQZRE6-EYhvjHUW3sG-lRm4UUnsVhKMV_TN3p5UFbhq-zWVOdrD9iKdUg-2nt_8tglQHFHrXUmW4yF3NiwaapCH7lChPENi76HS3CTiQuA8LXJwK1lSwGr_ssAAVEIk7lo-8j-EMf3JYSRa9hK9bUSH3Kowg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a4aea1dc.mp4?token=YvXCYNhRaA8oH_4T8vhWAMJstyWRDaxvMC6b6bPf5wPyDAas0vkkHK1JD7xtCgn4zKeCc2qS8COYffe8uS3HH9yD639h9zRikLl97Ld7bSNHGBdhS2veaiSTj4XX6sOuBKBQqLSgImDTbNGU1M5ADo-tJfUR_kZft4z1ckf2gr1nmPhH7lqFJ0hU3YAQZRE6-EYhvjHUW3sG-lRm4UUnsVhKMV_TN3p5UFbhq-zWVOdrD9iKdUg-2nt_8tglQHFHrXUmW4yF3NiwaapCH7lChPENi76HS3CTiQuA8LXJwK1lSwGr_ssAAVEIk7lo-8j-EMf3JYSRa9hK9bUSH3Kowg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عاشقانه‌های مسعود شصتچی و خانومش در مرد سه‌هزار چهره؛ عجب شاهکاری ساختن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106329" target="_blank">📅 09:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106328">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3cjEJR8Y3Mgl8KBql_VJYp3rAplfQh6-IkVvNLJcfqGgOcisODQFSSlQWBlvOi3jqoJEH9CbbazYPe4eSOURRuePZ7iJKN02MFNk1IotNsKoPW37Vc5iFafEd5qtHLP1aHwB8_Muy6FarjA1g9tPTDT23GG9Okks9x-LDTfRnVd9leQdNK3QNsKfuV1IZm0rFn-gpRGDVuD3u8llND4ol0srQn_FghV0YTC6iUivQtuNr649KVHTFSBlOy_FLng0mGwRcPxx-1zfvtQog1l3kjK9IlNXNw62A9J9gLIXLhcKBvrM4vy6O75jtCkMmG5b_I_KsjzKwuiUOwsR1FYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مقایسه آمار برجسته ترین گزینه‌های معرفی شده در بین نامزدهای توپ‌طلا در سال ۲۰۲۶
🇩🇪
هر‌کین 73 گل و 8 پاس‌گل
🟣
لیونل‌مسی 45گل و 30 پاس‌گل
🇪🇸
کیلیان امباپه 58 گل و 13 پاس‌گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ارلینگ‌هالند 58 گل و 11 پاس‌گل
🇩🇪
لوئیز دیاز 30 گل و 23 پاس‌گل
🇩🇪
مایکل‌اولیسه 27گل و 35 پاس‌گل
🇮🇹
لائوتارو مارتینز 30 گل و 10 پاس‌گل
🇪🇸
لامین‌یامال 25 گل و 20 پاس‌گل
🇫🇷
عثمان‌دمبله 26 گل و 14 پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106328" target="_blank">📅 09:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106327">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0452f0d7e.mp4?token=CYPZ4LVp-WrP-4_AYy40yM1fkKXJaRAxxxP4c6JaLTk7hK61pJ9WvR9384deHwB2gIhAKnUSq4dQurhwY5Gr8Kat47bVQjmn6TKpVH3s8Hl2fw3kUL7Zm_5wBK7uGLtOEoFknC96rc-BPlEw2QAP2w-LeXvHez-GaDT2WgKSvhB4RALPMq5IKeJC6IVwygVaNzPd1l-BdNLv5-YbWR1xzhNtqL5e_xf1sTjF04Lbu22J76qDWqfRwqxYTlTdcKKmELD0hO5FWyqsC_s8buzWWmO0b5CXgCoXAoT0b43ZXHT_cECZKXxuSF7FrD7xJFhFPz9lvzXKVwx2XIBDV0v9uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0452f0d7e.mp4?token=CYPZ4LVp-WrP-4_AYy40yM1fkKXJaRAxxxP4c6JaLTk7hK61pJ9WvR9384deHwB2gIhAKnUSq4dQurhwY5Gr8Kat47bVQjmn6TKpVH3s8Hl2fw3kUL7Zm_5wBK7uGLtOEoFknC96rc-BPlEw2QAP2w-LeXvHez-GaDT2WgKSvhB4RALPMq5IKeJC6IVwygVaNzPd1l-BdNLv5-YbWR1xzhNtqL5e_xf1sTjF04Lbu22J76qDWqfRwqxYTlTdcKKmELD0hO5FWyqsC_s8buzWWmO0b5CXgCoXAoT0b43ZXHT_cECZKXxuSF7FrD7xJFhFPz9lvzXKVwx2XIBDV0v9uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ال‌نینو دوست‌داشتنی چه هیولایی شده
🥊
🏋️‍♂️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106327" target="_blank">📅 09:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106326">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fY7ZHSP9rE5SFtMIdZOZH_w88I__maw0aBxfY3BKhfsp_dYjUyL0ovzW_-xHwbIVNOw_A5qm1JKh2RMwMfnxLCbLwixbD5GtiMuE5tXLHj_-NC-vK2ZEsXJwH3y7sXagkabQHXGL620sLU_zA9BokW42ZgaweTuFASy2KCjIinyWq7mOABu-ZCv7TC-qCJMOTXVZh3mQJOqEGvklarxIAT5f_7-DxUapq5zLFSq1WXDd8nfZwG61QskIaMkv8O9quk1E1C0ZLmeoBoKMYGEAzN8SKtBhdrTALFvM2JNo9-Ag73xVrLkKhaVitq7JvVkSwKKEtyeC7kuOqzusXw6E8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇶🇦
رافا موخیکا بهترین مهاجم السد قطر و آقای‌گل فصل قبل رقابت‌های لیگ‌نخبگان آسیا با ۸ گل زده، بدلیل مصدومیت از فهرست تیمش برای بازی با استقلال خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106326" target="_blank">📅 08:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106325">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde925455e.mp4?token=FU-BKU0OJiKrpgg6FJ1UoCPORrLUBPin3G6JjU_VaVyYnZtrdW8uOHUSuocUItsmVw-qxn_pKw1J7zG2w5qFroaUhMlUeP-AvHAOoGTXCN0YpasY00m_iHdmpBXGfCePO2kQlihTAH6FQZ8s32Dtni6UppytcJe-qh5R9P2ktfKRiF1EjCb8dRAMPudjGq3-WQ2zKpyLlcSOX0vXK7y4uM6JJ1SMgcaAAVyNjpvwlipr5cUCaeczJvh9vlPumpWouYxPJ5hHm08Fv2-pqQkQNaYxt4i4kzPoKJ94NJaPpovtzSs705nK19wVlV9E3eAhiAXS5d6Bmil1vwOO8jC8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde925455e.mp4?token=FU-BKU0OJiKrpgg6FJ1UoCPORrLUBPin3G6JjU_VaVyYnZtrdW8uOHUSuocUItsmVw-qxn_pKw1J7zG2w5qFroaUhMlUeP-AvHAOoGTXCN0YpasY00m_iHdmpBXGfCePO2kQlihTAH6FQZ8s32Dtni6UppytcJe-qh5R9P2ktfKRiF1EjCb8dRAMPudjGq3-WQ2zKpyLlcSOX0vXK7y4uM6JJ1SMgcaAAVyNjpvwlipr5cUCaeczJvh9vlPumpWouYxPJ5hHm08Fv2-pqQkQNaYxt4i4kzPoKJ94NJaPpovtzSs705nK19wVlV9E3eAhiAXS5d6Bmil1vwOO8jC8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
صحبت‌های شنیدنی لاله‌مرزبان پس از دریافت یک جایزه در جشنواره فیلم ‌ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106325" target="_blank">📅 08:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4G_J_1BdiDZ8CzdeWuvRSVs-c_T0sqAjU-84GeuF1Q2j2Kt8FIMxgaeTygFuNasDRNe_jXerNeWGvmnoWKhdtyBJmoi_DngEUpi-5rQwgI_iG7wINXMfvYCMDHc2KwJEX8TYMOIhOjdtrCHhW6WUq3FcE4zzNKbS9mr3bAVfG5sfMywmKGY_mJ1a0yVum0EMBDMsBLblGj74F-Ad6jg_IUAeeCvwsKWETBdz4HqvXcJtAPiG6_tCfQWNwjPk4t3nl5N8Mgmi8AVBlbz9C-NxTEHWvFTBNp0Fppasn3Ql2_kZnv7X19Re4rDjh8ZZEAoDsuKhQKrvcSrUPUnRGkqLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ آرسنال همچنان درحال یکه‌تازی؛ ساندرلند هم مقابل تیم آرتتا زانو زد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
😀
-
😏
ساندرلند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106321" target="_blank">📅 00:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106320">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulaTKEHGs9bzTCR3DSk9Po5nMFC4zgldDAvJXSSFNHtDwWGLiO-zV0ZRNWQQEqcq7DkMxh7hR0oEK0Xk6foVaIb1qJk2oiBd9iJRm0GQNqaJ_mATRs00HEXwLnU24Ldl_0vs_4dFr4xnEz0D3Zh4mbGTzAE9VU3nROC4GaHpt2aAnYmPUyMIRmOD_Xq-p9tn6awwwnpIgK8ACBunQ03nS2ghCNEL6W1bAbeJsa0QFD_Ku56kvz5kAq5ix3_QIq8tH-2bbVfaeHbwQIlRIIdIiXlb9gQOn8cF9qkN7TSwaGMZcyZzVvTCt0zajiunIHY2vtmehHS4do-ZlzLfDkjh_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
کیلیان امباپه با رئال‌مادرید در تمامی مسابقات:
🔺
۱۰۹ بازی؛ ۹۳ گل و ۱۲ پاس‌گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106320" target="_blank">📅 00:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106319">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrqmTOTuhUEsZ2hUpCPcGwzjAAkN9TzmshyklRlkzSf3TeQr4Y3Txx2OnhILFv4U3G5YeH90r-z-YGgNKfpp3qGpOv_V6I88XdC3KuGBESeO4pqjE7CgU0Ky17yiDCFt2eN8k6toJLokx1gx7ZhdU343AzR9KcKuVLwT5Nym8R15HFI9d4kEkh-QkUCD0e-7f5qeaiPYXlZZZ91B9L1yvfSKOb5deSaM-m9qRdk769Vwr6UNQns0vMOE6ga-aC7987VssjIWIyjUAUbEXAgPvJxl52DJO737EHUphj9XxhIGFXohfyBalfcRhezADcRxYDxvLpfmpRmI_inj_n0NlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
گلگلگگلگلگلگلگگلگل برنده واقعی توپ‌طلا</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106319" target="_blank">📅 00:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106318">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OigbBVliHj394JRigDLufje1-dGZPjhnbbFayfZn7pW19-cOMei1ZpA84x7maiirazRylSQfxzKHVFjnH9njgc6dLUA1WkmRE7SCTAd5cUMMIpL8PEsClcgODJ-SBVEOnVnLU6SPyqGMITSG8f9VTzUCR-sIK9Eg1XUTPpK-WYTMFLt6MDUl3IhQYgwbrlUPp9QTSLVFCsRDPXTwMQhvzpbctB2CWewJz0K1OI6RK8cFTqlDJ0bEH4rXsuolVDbJk7cQFoifQJw8SJOGnRXIQB4hJc1TC9xk_QEE15s6hcC_buh4mvIcxPvGO1b_pCo_0aqJgQmG0Cmq4ewbPC0v7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌چهارم پریمیرلیگ؛ آرسنال همچنان درحال یکه‌تازی؛ ساندرلند هم مقابل تیم آرتتا زانو زد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
😀
-
😏
ساندرلند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106318" target="_blank">📅 00:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106317">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f6e034671.mp4?token=cnSVJB7pKMhtS1I7B96EW4y3dBcAZBOYZ7pDaGJB2kduAnLa8BCwWbwYWqAOth7Sr4luyW_c32qPfhoRBYaPeYzfGM99r2et6rSfUPumFJGx3S_nFyvM3LPbbqiFCRblhOoPfI_yjmPhqCBbGWKzQCaXY0HAqDOjlivz9iMgZQHjsZOsekyZcogwQgG9wtO2rQBXRNlcozFkECqkEq7Cj74RIzFfiu6BLIDT_HBdsxfFOrs5joj_rrzDAptMLoPcGcV4dGE-tKkJ1F5xznCtRxNpWqVWmApuXQysyiPgSi87wLMF1GuBUBJVjzXNa5unkgGSEE-fP56ty7U_yN2HHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f6e034671.mp4?token=cnSVJB7pKMhtS1I7B96EW4y3dBcAZBOYZ7pDaGJB2kduAnLa8BCwWbwYWqAOth7Sr4luyW_c32qPfhoRBYaPeYzfGM99r2et6rSfUPumFJGx3S_nFyvM3LPbbqiFCRblhOoPfI_yjmPhqCBbGWKzQCaXY0HAqDOjlivz9iMgZQHjsZOsekyZcogwQgG9wtO2rQBXRNlcozFkECqkEq7Cj74RIzFfiu6BLIDT_HBdsxfFOrs5joj_rrzDAptMLoPcGcV4dGE-tKkJ1F5xznCtRxNpWqVWmApuXQysyiPgSi87wLMF1GuBUBJVjzXNa5unkgGSEE-fP56ty7U_yN2HHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گلگلگگلگلگلگلگگلگل برنده واقعی توپ‌طلا</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106317" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106316">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اونور آرسنال دومی رو زددددد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106316" target="_blank">📅 00:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106315">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">برنده واقعی توپ‌طلا دبل کرددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106315" target="_blank">📅 00:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106314">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رئال چهارمی رو زدددددد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106314" target="_blank">📅 00:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyERGH4xaHIvwGwgAuXFw8eQrCKfoOY_yXTnuBK1ceub5kZzE-DUV_ycGX0H5k7_UwtzV-LawguHFMsgFkqoAgx3DXEA9Eo0idTWDMdfO_FWgGqd5nKnJBGYE-zEVegkYg_t2EgYp8qx1EOBXYZtP0U2jnZFoJQsc7xJtOW6lkC9k7fWi3tlqef723RaVWpqXaFazrw58akvRaRGblAQyXDvQsdp41J1QxpLJAoR7ZsDDoMcurEnrr57RkcK2LuEb2B0Dm6r5S1XMhn9kPiWGCVoDpvgPXMBc3-cLnBCBWuYLgBK78G0GkPIhNL5v8nwQWgwPNg-TIpLIHs8NnqYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
استقلالی خبر جدید براتون اومد؛ مارسلو بروزوویچ از النصر به السد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106313" target="_blank">📅 00:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU8ZeOwSYwfMdlp4cgFlpYpdxaW1d4r61-WxLVsVoRTxR8iiAVASrbIDxZT8nxxx4fw89cGxK2Vqct-EINlXz0zHk3XSpTYGx6nUT8eFeZpxZ1oUH0bUrE6zN519oVRL-FlYIRTlmVuwJZIpw6-qe3bHrip3d4QD-Mo09xlBGSgXL9Vc399lTGBI7HOosxf3ZMFkbY3h1XpW9h0MGxcSjXok-LmeGlcniGZTMF0btBtl6Izzt4Oy_70ZzD6fkz6gLxRtuGMKpDWFs1zrSMIc_B7zU9anRb1AfqFgv6lnu3tRruRoAD8RuiaPvkkNPmiuqHkhMWURbJRVqd4wLThV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صالح‌حردانی چه دلبری از سهراب میکنه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106312" target="_blank">📅 23:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d53729e95b.mp4?token=vFFPV8nF0Pta5H4isWPTljfxyuO2Vm9636_M5lT060_sPusINl1NW75W-P6zEHXPe4Ri_nSYz1kQemcEu6YU6mM6a8XkWjIGbRBwpPJ33Tl8_ARKsbhf09pUvlnzG4-ISXQS8jncYlEVMRYgDo0qVONdFMOL1up8fG-q61U7KRw1vShXZbTCuOxSWXOD_K6WrsMj0seVrXzd2nsdu9Sl_phe25kTqlLTfyB6Wv4BCxNbOJBj-rNwdTPcAFLE8rJddQjyJi11v-4IMnauRDN6Lx45XmJg2hmFJFQ0q7sKOU6FPndsjdqnNPLmwYNz-3XIqyUuu6VQoaS56jsQWkfh5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d53729e95b.mp4?token=vFFPV8nF0Pta5H4isWPTljfxyuO2Vm9636_M5lT060_sPusINl1NW75W-P6zEHXPe4Ri_nSYz1kQemcEu6YU6mM6a8XkWjIGbRBwpPJ33Tl8_ARKsbhf09pUvlnzG4-ISXQS8jncYlEVMRYgDo0qVONdFMOL1up8fG-q61U7KRw1vShXZbTCuOxSWXOD_K6WrsMj0seVrXzd2nsdu9Sl_phe25kTqlLTfyB6Wv4BCxNbOJBj-rNwdTPcAFLE8rJddQjyJi11v-4IMnauRDN6Lx45XmJg2hmFJFQ0q7sKOU6FPndsjdqnNPLmwYNz-3XIqyUuu6VQoaS56jsQWkfh5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل اول رایووایکانو به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106311" target="_blank">📅 23:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/152a6c453c.mp4?token=d5ENmii5Cu7dJ-f4F1QuZpV7ktDJEZrR6CeCvDhtuqiNKbcVy63J59v6P7KTTJvtHzdhc7-6aBlGJBeejjK3IxVvj5CtFDevLRf27l6im_bDsgWqyDUx25sBlLX0puDVvgp3CIQOe1Ga_2Pnitq7hOd5SNwNheMkhWZRK83Wdvf7_3cj3pMZHOEsS03spuONyeaaJHY0JAonm7Fk3QgnjnL2q9j0Iu5ExvwkQZgc-PXBC89tOoQS15p6aYCH9LskHU6ydrKxP2ratszgFc6UFyyzeNXCR8K2yVZXFo6a_F_-LFNFV1-ODXhY9zr6k03loTucUoUEuWEWFfEziz4M24i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/152a6c453c.mp4?token=d5ENmii5Cu7dJ-f4F1QuZpV7ktDJEZrR6CeCvDhtuqiNKbcVy63J59v6P7KTTJvtHzdhc7-6aBlGJBeejjK3IxVvj5CtFDevLRf27l6im_bDsgWqyDUx25sBlLX0puDVvgp3CIQOe1Ga_2Pnitq7hOd5SNwNheMkhWZRK83Wdvf7_3cj3pMZHOEsS03spuONyeaaJHY0JAonm7Fk3QgnjnL2q9j0Iu5ExvwkQZgc-PXBC89tOoQS15p6aYCH9LskHU6ydrKxP2ratszgFc6UFyyzeNXCR8K2yVZXFo6a_F_-LFNFV1-ODXhY9zr6k03loTucUoUEuWEWFfEziz4M24i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم رئال‌مادرید توسط جود بِلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106310" target="_blank">📅 23:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106308">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بلینگهام هم سومیو زد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106308" target="_blank">📅 23:09 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
