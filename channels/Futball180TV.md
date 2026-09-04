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
<img src="https://cdn5.telesco.pe/file/o3U_RGU4cBMrjTx_VOKfs3bxtOVel8LeXrM1e7Yu3-x6Bgxjd84Fe-vPWfoqjD2p-HP2ylGY0XLePBVnc6htGsD2Cp26QHgOf5VqC17MIVF2LSRu3eqi4AOlFJow5du3lf2tTxCqZqdeNv9Pk8lCLn4X-kxZK5Sv1JRwXVcC9nbcE1algj1tnXwvmBS2dxt4h6Css1haMhopy-6p66Ioc5X8kDj9EECIB_5gDDGaY4H77xSPRwDgt3VXOoE7-SNWWhsvIO1tFcyeLAKmZKC2TwwbDTJcx055uUcBP7evxw8a01tIeHJEy_8ySLXuccahGREk1WS05Jn171NgXQ7BjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 428K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 12:42:35</div>
<hr>

<div class="tg-post" id="msg-105485">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=LL9zAJme216Kum9rCCsZZ5PLP8HEmYuXtok5WZkoe2fTzMp0EGa_NQeHp0ISOkDRVGcGE6VE6Q8bwfzm4mxRQInXnVeTVs0PaD0VJuA35zcUj6w3KAqMUcdN1GZtffyhMLy__lVXfMOFs4UnmFgziTpcLTkbuXDaQjrWTRYoI8jzAdoUz92zinKSfEIWt7XkIEDLi0BMCnysgwlGcpTkiH_-FPsJRV5FyHYVoMJ4H3hAxfh_IhWW3pC70vSqN-V-8ufljx1SOCJZ_L5Jd_8ePUaL9Tnk4xykvs_fA_FJ-3qrfquAQM5FFj-gYjI6W-wbh5ClG1wF-uzUFxaPrTUR6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=LL9zAJme216Kum9rCCsZZ5PLP8HEmYuXtok5WZkoe2fTzMp0EGa_NQeHp0ISOkDRVGcGE6VE6Q8bwfzm4mxRQInXnVeTVs0PaD0VJuA35zcUj6w3KAqMUcdN1GZtffyhMLy__lVXfMOFs4UnmFgziTpcLTkbuXDaQjrWTRYoI8jzAdoUz92zinKSfEIWt7XkIEDLi0BMCnysgwlGcpTkiH_-FPsJRV5FyHYVoMJ4H3hAxfh_IhWW3pC70vSqN-V-8ufljx1SOCJZ_L5Jd_8ePUaL9Tnk4xykvs_fA_FJ-3qrfquAQM5FFj-gYjI6W-wbh5ClG1wF-uzUFxaPrTUR6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
اتفاق عجیب؛ نیمه دوم بازی شمس آذر و تراکتور ۱۶ دقیقه وقت تلف شده داشت اما داور دو دقیقه اعلام کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/105485" target="_blank">📅 12:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105484">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjfZv_2lVVSZvCjb8hiRMduQGRafq0KEwbqYKXZLlGyE132F0JlSp5LGVXxQMF76ZKgOWdIss9k4uZWQq5UPJ8IHJpOwNBjvz-ov_Zw8ZjMwQ7jjsNwnsoDx4xMJr98cU_z2DaCEAIPkTinZfco5E-x3HAKsa8ZXGC_lcwK0_KOtlfxvHI2bsXn6rrP-cJC_WvySVpOu1wsCq1nqGYhdbr7e6qvqPFCVCeCqO9mpNUIyTQR8lK32B45klAXd_axK6C6wueC-gvXLNTxPDhcGws5Y0QoDMDAuLrnWNwr6AniQM2JagnJNkYXzgz4qC0boj6s6APLECiBWaXDiyKRRxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
نگاهی‌بهترین‌گلزنان فعال در دنیای‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/105484" target="_blank">📅 11:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👍
▶️
اجرای ترانه حماسی ‌"ای‌ایران" توسط اسطوره معین در کنسرت چند هزار نفری خودش در ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/Futball180TV/105483" target="_blank">📅 11:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105482">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPEepEj0gkV0AmsDNW47diCY1H-MRNi4byn4JV3Sf2WTTV0AASzZ6DCZ6NI4UNY9WNv1jY4VZ9YEkcKsqZzF1fwRZJrARHooxpPslgi8fkl43brqMmufxd2JdVrRAahPf6Ebck8384vD3g7l7JRdbOE07O0yUDL7LVDZfqcHfZt4Tqqbwcu3F0srB-QEl156J44AaaszP1lkX7NUdkAL7BAzxea1lWQrlp9ORF58kVmyHJcFxwQcNvcWlI6m_fgWFkWJEC9mOXXkiJk849tS0UiXZaXFD3uqM9HkQP5qyxNSaL-O_JDv1al5YxdtBgLNEF_ZBWQoHPepaUCSFT6w5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو دربارهٔ بازنشستگی لیونل مسی از تیم ملی:
صحبت کردن دربارهٔ مسی مسئلهٔ پیچیده‌ایه. چیز زیادی برای گفتن نیست. هیچ کلمه‌ای نمی‌تونه کیفیت او رو به‌ عنوان بازیکن توصیف کنه. او با ۳۸ یا ۳۹ سال وارد این جام جهانی شد و دقیقا همون‌طور بود که همه دیدیم.
او یکی از اون بازیکن‌هاییه که دلتنگ‌شون خواهی شد. مجبور خواهیم شد برای لذت بردن از این سال‌های آخرش بعضی بازی‌های MLS رو تماشا کنیم کاری که شخصاً زیاد خوشم نمیاد ازش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/Futball180TV/105482" target="_blank">📅 11:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105479">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2EY2N2Ez4hPsTjCaBJnWtxvUSLZzgGkOTiepUfi9QBBOHo-NPCc_7X40pj9JdsJVUeqpOUWFvqGU5-drGlX05yFGa0DglkpaV9Zgysh2bTo27lFrSJSXohnBrPRl2fWdYWcSIq30duIWwSpLpNnQIQ3ZyJflvmGQKwwpjAVopEKGc51TPQXXgoox4geyRBmkEevU_NqFV5pUiQKhki_mZQZ3MIgXrHiaHihAtddIy9rgUSBPZ4RoYl-kBucsi2Uz7jBxf-cVKcKBAwTHKuOzxR1wCIN7kpLSwZfhBcBzqnkqcgfOC3t8p57PDsFOG76WgqYFtQNECeROGGouHSqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htpm7fWm7mKF0Kanh01Q08VId8HnGbeWmi6SvMQmikKTpHv8JpdB0v-ALksC3WP7W4rBn7ik0H4W2K02ZDG_4_ip2dkn2iLbuz1e95pKnpcjL9A0p8NI6HMyirAfIiVTZNkwzg0wdcpXjxKF3DrALyFkIyLRcYsFjhSJE8fsJ3K5mu-9LsIjxiE1XtPosWYVQPivsTcTSOfmWBUzJC4ZN1SY9UpHN4GqsoVBfso8QB8ZizlGsQmJsmukRkgfkf35Chc8YuB4fu7kcubxNv6cvptSJKITr5JPiI8Jf1PGjpX-U4LvLmvDfXbd9ut0jmSdANvoYUbWiexHpJXXebJGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCXf0n2anAqLxVFE2ldlSPytaBw5H_IJuzJ0cyJPUdKe7N5BmuN7KDWrVFfBtow2yQrmhuDViNECnlklhyBfEvrbyaSEPidQQ2mSouGccPjtpU5OLUjqDoFxlj157hgaEIyRTw28k5Uxj6vn3CdOymCQzy1-Z9QKSmDzyNB47q5qeSerGClmz-o6TPASCN5DnjvfSFchuM4ZB9d0jReCOvTO1oX4IMtOqAZNbOxEwM7xf51BJJSUljoceLB2He1E_EvEAKqC0DKZeOy9b1eZZJjkhGLlLTnkuxQJpK02Yt8JJnbTa1N1Gu8UAbrtrqSQ6yHRUjxbKryt91OQrtIcdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکاس جذاب در حاشیه دربی
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/105479" target="_blank">📅 10:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105478">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👍
💥
عایشه‌گل دیشب رفته کنسرت معین و از لذت بی‌نهایت صدای اسطوره ایران بهره‌مند شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/105478" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105477">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb75d47bec.mp4?token=hw_4LlxmO_K31mcJ6BQEWmXtEzyuIc1WqOJvFPBaUJYm5_G6GKIrnSCRU_XKIcAqHyC6JcfC4kyBEHe1HoV3AQ4C724b1__r7jylUPQVdNgL_shIUBlGYlQgYpz2XzICF8qmX8tZdqvzRxVeXr37u7UBMSIQJ9ZDXEBE8wJ_F4BaFDLCuD6mLz_Tr2CFn2JXVQm5ub0qEjHILvuVogiZ-nwS2yJqFKFtdXOYCPu1ULwhAp1EskGxoEXNU_jSRVlEuW3lltDXKq1_QKE5qEguJZTZrTxLP3aOXt46YziOdlWvRbdJZvo8M1oatqolxxhyofTXL--tKiybUdjO8lzyVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb75d47bec.mp4?token=hw_4LlxmO_K31mcJ6BQEWmXtEzyuIc1WqOJvFPBaUJYm5_G6GKIrnSCRU_XKIcAqHyC6JcfC4kyBEHe1HoV3AQ4C724b1__r7jylUPQVdNgL_shIUBlGYlQgYpz2XzICF8qmX8tZdqvzRxVeXr37u7UBMSIQJ9ZDXEBE8wJ_F4BaFDLCuD6mLz_Tr2CFn2JXVQm5ub0qEjHILvuVogiZ-nwS2yJqFKFtdXOYCPu1ULwhAp1EskGxoEXNU_jSRVlEuW3lltDXKq1_QKE5qEguJZTZrTxLP3aOXt46YziOdlWvRbdJZvo8M1oatqolxxhyofTXL--tKiybUdjO8lzyVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خولیان آلوارز در اتلتیکومادرید موندنی شد.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105477" target="_blank">📅 09:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105476">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0670f6d10.mp4?token=NGGFFqv5gSiGjqR3vAThp5VugoAik9vaKrNFH9NECeb27l9N7MeWwD48VrRZZh_34ScO8YicGPRKczqXJe9CBcoOnPNEVX9nMQbI3hiZBfoW95r-rToBIviqWc7_KYisejDWQP7zb6PSsMzh6X56hAEpgJYpTFBBpJ91IRxVGiqlfqwEvQcZXyfDwJfM2MNIs0_0VOByNuDP_o3YZbAX1kEm-BVu5gEjy7-g1SFJcATvcDQ7Mi7degXCxio5AOMwSVxI-JfVDysUJ2Md37qrD8YnLTsmTkNz4KAGxIT_UawBieDbyRnrbhKbW7vGHu66dmCS2YJOEr7zOWtUrfM45iYWkMNpUKL4E3Zq0JIJ1wTbjNuoSUFeN9lAQSmLllcQjDvIzSsM8zmwLBI9L5dMiw6vdm3qETpiX3E0Bfj7BY0KUQqyCw4oSQxWHiCZIQ3q-OYmIBD40JefeG8IaOPHV8l3Y6fxaYyrZ7TX45wwK0zalpnv1ZhpHqPMDk_xUC843iKC-PC_ZhWctMMHFp0LJORJW3FCII7EsJpISjf_FmpXa1fyryvGAFX_45MCp7imusQLy9mwbnVOkOh9qeYpWATwYB6L6WeeQu50gU_U8m3MlF35m1WnBtB3WfyGrsgZz4_BtVAk1SAemRUN6sCis_dPyapdpPx4lvrJG4Ls1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0670f6d10.mp4?token=NGGFFqv5gSiGjqR3vAThp5VugoAik9vaKrNFH9NECeb27l9N7MeWwD48VrRZZh_34ScO8YicGPRKczqXJe9CBcoOnPNEVX9nMQbI3hiZBfoW95r-rToBIviqWc7_KYisejDWQP7zb6PSsMzh6X56hAEpgJYpTFBBpJ91IRxVGiqlfqwEvQcZXyfDwJfM2MNIs0_0VOByNuDP_o3YZbAX1kEm-BVu5gEjy7-g1SFJcATvcDQ7Mi7degXCxio5AOMwSVxI-JfVDysUJ2Md37qrD8YnLTsmTkNz4KAGxIT_UawBieDbyRnrbhKbW7vGHu66dmCS2YJOEr7zOWtUrfM45iYWkMNpUKL4E3Zq0JIJ1wTbjNuoSUFeN9lAQSmLllcQjDvIzSsM8zmwLBI9L5dMiw6vdm3qETpiX3E0Bfj7BY0KUQqyCw4oSQxWHiCZIQ3q-OYmIBD40JefeG8IaOPHV8l3Y6fxaYyrZ7TX45wwK0zalpnv1ZhpHqPMDk_xUC843iKC-PC_ZhWctMMHFp0LJORJW3FCII7EsJpISjf_FmpXa1fyryvGAFX_45MCp7imusQLy9mwbnVOkOh9qeYpWATwYB6L6WeeQu50gU_U8m3MlF35m1WnBtB3WfyGrsgZz4_BtVAk1SAemRUN6sCis_dPyapdpPx4lvrJG4Ls1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
یادآوری تلخ‌ترین خاطره مشترک وریا و سیدجلال؛ خط خوردن از تیم ملی برای جام جهانی ۲۰۱۸؛ از خداحافظی زورکی کیروش برای سیدجلال تا غافلگیری وریا از خط خوردنش از تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105476" target="_blank">📅 09:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtG2f-G0nqFT2Q9AAbws032oSTd3-VAqaUxQ0ET1cF809zpRB0IQg0Nk9Surg_h0ZdPZf0cnAeYgDtPKv85MEHMW4fGD5HkGeBb2HcrBENs-v-yWxxYEc1VK2-d8rp8zuFdKPnbdRorzxtxORtA8MJVIT6zUNtJ_HX5yo_p8Yct48OaQKXFxtxEiQJLZYZVaowl-CQUHE7XbnT0jPNcpqCkwJrzIuLC5it0C6i9pE54PtFeHne_whGgva5BW9keuV9U5w4L9ydL8RYI3lQUMRtiFmfke9ONLkXD2DNVVDN659g1yykLj-39UZ1OHWLm15Q0Dxgq8h0mKDrplkCo-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وریا غفوری عزیز و همسرش
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/105474" target="_blank">📅 09:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105473">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084453a784.mp4?token=OQfcvDj8paVQdrwWmDCXaAO_vswJVYBMotJ6FSNK3Y6FDz0QOll1RxUhDGsKHISdSHn5LGcHrrTDTk2vZjKRlQ8l4giUbdnMLS2qRPe3qz7OJ6iGU7EB-oGvZDpidn9PatleJGpEoWeHR9F0q56w50TejzTRDO3PocJXekzb50Ry68BrNa96Pzc3QKVCxX7-X-9iHx42GHhj6lrsVbBqRZNckqWDEunJ221RV8DhpkqxgOD4mr8ykLVSwhyNOismhkmfU_zCukMr5HqG58Ks7oRUsJKzoGpgsTXvxJumtemLq_oVxGFbCocW8CrkPjzezv44eK9KEEMeTkVoJy4S5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084453a784.mp4?token=OQfcvDj8paVQdrwWmDCXaAO_vswJVYBMotJ6FSNK3Y6FDz0QOll1RxUhDGsKHISdSHn5LGcHrrTDTk2vZjKRlQ8l4giUbdnMLS2qRPe3qz7OJ6iGU7EB-oGvZDpidn9PatleJGpEoWeHR9F0q56w50TejzTRDO3PocJXekzb50Ry68BrNa96Pzc3QKVCxX7-X-9iHx42GHhj6lrsVbBqRZNckqWDEunJ221RV8DhpkqxgOD4mr8ykLVSwhyNOismhkmfU_zCukMr5HqG58Ks7oRUsJKzoGpgsTXvxJumtemLq_oVxGFbCocW8CrkPjzezv44eK9KEEMeTkVoJy4S5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
⚠️
اوج قدرت صداوسیما مردمی در تمسخر و تحقیر رئیس جمهور بزرگترین کشور دنیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105473" target="_blank">📅 08:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105472">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105472" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105472" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105471">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQsK48TWshORhKCWUX8yZB5RQUPxOvLF0kNIyjXLIoMhNtY2ZBQRXPB2pKm9sblZVhnLNbH_L_hcMttgGcKxqCjeiVeC5kxkPvfrnBXbOErc8tEUJ_GHuus5rsyaP_7GDc0FLhNKcRFfh674bsrrM8pEalJe2rvXdOmVsku_4pWHMbIpsSqn1cpWh8ScPaTRUhpL6T558P12ZLKPht4nPUccBokfefwOLpFpjqJqDJ8vmNsZJqrsiG_4M9KDHRc8QZyTX08Qnznzj5sF9Y51VDU1m39kIVdXWXEdq72GUiaCA9yMmdlM2cYWNLc5tqIEcbjYWKotoz0Ir49GXMkDYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105471" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105470">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105470" target="_blank">📅 01:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105469">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a64bed0c.mp4?token=ZRVYt9fWPTJ_1wtX0i0xWfckJFP2j0RJkaXCYftItZAhAZOg230WjTwwhy_G53KyeBpJMfc1btnrXep8j6Tiwm2nKZ9BuuWGZFDiMmbyTy7VLxrooCeSKGzxJ2M789N1RU4IxSwQ1CIhway77NLoLaD4iZvuxl6b1VRIz8uM8ET-ApkEftqwVCllQEMXUcps49to_ygquID6LNpZs4nGAJXw87wmPpZr8uRlrcZe6Ssbarya052OMOo8mbdMtEd1ATDqBhTFS1Wy2FEp4n0BEcBC1CIhlL7qhrmjYE8hz09lyL2gHbjE5vr-8gF5IO02qAevISE2axa3V5RRltT1PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a64bed0c.mp4?token=ZRVYt9fWPTJ_1wtX0i0xWfckJFP2j0RJkaXCYftItZAhAZOg230WjTwwhy_G53KyeBpJMfc1btnrXep8j6Tiwm2nKZ9BuuWGZFDiMmbyTy7VLxrooCeSKGzxJ2M789N1RU4IxSwQ1CIhway77NLoLaD4iZvuxl6b1VRIz8uM8ET-ApkEftqwVCllQEMXUcps49to_ygquID6LNpZs4nGAJXw87wmPpZr8uRlrcZe6Ssbarya052OMOo8mbdMtEd1ATDqBhTFS1Wy2FEp4n0BEcBC1CIhlL7qhrmjYE8hz09lyL2gHbjE5vr-8gF5IO02qAevISE2axa3V5RRltT1PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
واکنش‌ها به صحنه جنجالی دربی:
🇮🇷
بیژن‌طاهری سرپرست استقلال: کنعانی قشنگ انگشت خودشو فرو کرده و کشیده!
❌
میثاقی: بنظرم باید طول درمان بگیره!
🇮🇷
محسن‌خلیلی: صحنه خیلی قشنگیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105469" target="_blank">📅 01:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105468">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=vjge9kEUfT9KtfdFN-gZGAqNLg9ILTea5WsfZXeoc1ie95MflDxR2v-HsUt2dhTr6kKCdUMJvU7nzXAEbD8mUj88pTRl3wVZyUrewcT7_uZr-zSSo11irqNtsx_sbqolRotGsoSPlUEzI1R1LBMSQg3ImSHTPWBCP3mmp2hKW9vWtPcqneaZHCI39V4KAPu4IboXhjsZyO98DIQdURSwiLuyVBWuxlOkwFb0zimZ9etDfP4-FEMymW8ZaH5koDGTRDaSGxYeIczZIf_fyg_sKp2TeQK1hceCTC7Cj7Kaa1wCTfhw4JzqTTJU7dxX1EeN1aFQD0BEV2ExNdw8lu8Tfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cfe803aa.mp4?token=vjge9kEUfT9KtfdFN-gZGAqNLg9ILTea5WsfZXeoc1ie95MflDxR2v-HsUt2dhTr6kKCdUMJvU7nzXAEbD8mUj88pTRl3wVZyUrewcT7_uZr-zSSo11irqNtsx_sbqolRotGsoSPlUEzI1R1LBMSQg3ImSHTPWBCP3mmp2hKW9vWtPcqneaZHCI39V4KAPu4IboXhjsZyO98DIQdURSwiLuyVBWuxlOkwFb0zimZ9etDfP4-FEMymW8ZaH5koDGTRDaSGxYeIczZIf_fyg_sKp2TeQK1hceCTC7Cj7Kaa1wCTfhw4JzqTTJU7dxX1EeN1aFQD0BEV2ExNdw8lu8Tfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
تصویری از ناخن‌ بلند کنعانی زادگان در صحنه درگیری با آقاسی که در برنامه فوتبال برتر نشان داده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105468" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105467">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e73b0c80d.mp4?token=hedfKV9w5p8sDGxhWl5qVBusM7s3BqEoB886j58NbERW84PwGPZewSOmVF7Anwp3XbwbD0tpjkY8zL1A3vPc1vuoH0-VEogrP2nkuoEAgLeXPlOEeZ2dy6DLjp2Vz9LlHQmBbkbJWORsu4sTmT5IqIuo2WX2GCaRlvE-m8HBCEcd0BAm6bfnYQxIOYiQa5afpuBgUr1Ii8HNqEO4F9c0n3tVfXfMMaW4GPADVjQa_9Yki5anLHu3JBoIImfgIijSjx4BLOFL4h2pLjSdo3x67wsXHFApPVLTwUVljmwRkVUBqEfglfRJyN8wDam6EQIu0UFZT8CuTM-e2hY1VbjCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e73b0c80d.mp4?token=hedfKV9w5p8sDGxhWl5qVBusM7s3BqEoB886j58NbERW84PwGPZewSOmVF7Anwp3XbwbD0tpjkY8zL1A3vPc1vuoH0-VEogrP2nkuoEAgLeXPlOEeZ2dy6DLjp2Vz9LlHQmBbkbJWORsu4sTmT5IqIuo2WX2GCaRlvE-m8HBCEcd0BAm6bfnYQxIOYiQa5afpuBgUr1Ii8HNqEO4F9c0n3tVfXfMMaW4GPADVjQa_9Yki5anLHu3JBoIImfgIijSjx4BLOFL4h2pLjSdo3x67wsXHFApPVLTwUVljmwRkVUBqEfglfRJyN8wDam6EQIu0UFZT8CuTM-e2hY1VbjCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
📹
🇮🇷
🇮🇷
🟨
نظر اتاق VAR در دیدار دربی درباره صحنه درگیری کنعانی زادگان و آقاسی نظرش بر کارت زرد بوده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105467" target="_blank">📅 00:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105466">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2b5d1c797.mp4?token=e1iekfPaOz8oMIDv1xWuJUtcPw6IeUBGPgiKAJ5Glb4_idUlrgAx_qTXc8tS2xtAbKZHrFFkgkF8i3OmlU6tnn4pjFZ0j11P56EUxI3n1T9PUjz4gOKWGEH3JLdMidTua85k2yFSQRhQHt2Cwh0Vc7VGDaXoNRIPtYPxs41GvE0QJlU_I6H824J3x77FGN8WPUEjaFEQRjeVIykxk_paVdO---xXX5zgoiv6tfUG44IE03cCCPRQhvmbzNz8M8dHz1vKmV1Fu5sd0C-xtbS7FgxZ2IeBaFAGtDt3Uch0tD67QVJ7_-eFPQuOoXKfiXSb-67wT-dIi06ltpGQeoDdPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2b5d1c797.mp4?token=e1iekfPaOz8oMIDv1xWuJUtcPw6IeUBGPgiKAJ5Glb4_idUlrgAx_qTXc8tS2xtAbKZHrFFkgkF8i3OmlU6tnn4pjFZ0j11P56EUxI3n1T9PUjz4gOKWGEH3JLdMidTua85k2yFSQRhQHt2Cwh0Vc7VGDaXoNRIPtYPxs41GvE0QJlU_I6H824J3x77FGN8WPUEjaFEQRjeVIykxk_paVdO---xXX5zgoiv6tfUG44IE03cCCPRQhvmbzNz8M8dHz1vKmV1Fu5sd0C-xtbS7FgxZ2IeBaFAGtDt3Uch0tD67QVJ7_-eFPQuOoXKfiXSb-67wT-dIi06ltpGQeoDdPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
بیژن طاهری سرپرست استقلال: آدان دیگر به استقلال بر نمی گردد باشگاه هم پولش را می دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105466" target="_blank">📅 00:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105465">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b23d335e1c.mp4?token=ZfiELP4RiyKOnXBmcf0fclVs_XCFFc0Ah5Nv_HD4svIim6beAvhB6BJebn-UEeyNYU5OCcXgOGlQSk_GEun6UZPPT1C5STuiup7IvtZIWGixb_7WE9Ic_r97WtpPGoiJhfy-YYW6DtcAQeRTSqsRLCaxPExJsso6WUsL7xGpIo0Gou2Tqu-JB_bjehYkT4kdt_gt5F5_KBh6DCpgoaSBHGRwngE44Wk9L7fXtYIiYmeGe1V94czcAJJAggq0q7OYWT1qOOCEqL_HXrRsASaasw54E7MfzjMlSWt5g1a03-SwaezT_psBXQme_jPBp_qxXIJpALB_IqxwVyhoOg5rVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b23d335e1c.mp4?token=ZfiELP4RiyKOnXBmcf0fclVs_XCFFc0Ah5Nv_HD4svIim6beAvhB6BJebn-UEeyNYU5OCcXgOGlQSk_GEun6UZPPT1C5STuiup7IvtZIWGixb_7WE9Ic_r97WtpPGoiJhfy-YYW6DtcAQeRTSqsRLCaxPExJsso6WUsL7xGpIo0Gou2Tqu-JB_bjehYkT4kdt_gt5F5_KBh6DCpgoaSBHGRwngE44Wk9L7fXtYIiYmeGe1V94czcAJJAggq0q7OYWT1qOOCEqL_HXrRsASaasw54E7MfzjMlSWt5g1a03-SwaezT_psBXQme_jPBp_qxXIJpALB_IqxwVyhoOg5rVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
محسن خلیلی مدیر پرسپولیس: برای دربی 5 بازیکن جدید در پرسپولیس بازی کردند اما استقلال تیم پارسالش در دربی به میدان رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105465" target="_blank">📅 00:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105464">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12003f9a0f.mp4?token=Gq3uj1WYkq7N397RjbeOQ8kwIVlu28XTsriM-Zy0usLoz4ST5i8OIJK3JRymrhAKlWY09V9azJ891EWQc7dcQqvvU9iYV1EIfXfojXu1RoAz3F89MZJNcypIO5VED-135EsDmC1bcKq4j-shO2bxVVP5L6ffd5vhGQ2xIwdbCODSCRDO3w2N42leP2Qwsz8KPOOFrZgmKvt2ymsx-uSRz25PYjSD76awAyq01lFVARSfZOeLJ4n-XPhya104NgpvJemzTPzZQZmPEd-j67bhq5wn-n5R_p82_ju3EG9IgrTGuWhHbNg-1Q50-Ht2evh7c63ZZSUsh_viv4TdVgnhdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12003f9a0f.mp4?token=Gq3uj1WYkq7N397RjbeOQ8kwIVlu28XTsriM-Zy0usLoz4ST5i8OIJK3JRymrhAKlWY09V9azJ891EWQc7dcQqvvU9iYV1EIfXfojXu1RoAz3F89MZJNcypIO5VED-135EsDmC1bcKq4j-shO2bxVVP5L6ffd5vhGQ2xIwdbCODSCRDO3w2N42leP2Qwsz8KPOOFrZgmKvt2ymsx-uSRz25PYjSD76awAyq01lFVARSfZOeLJ4n-XPhya104NgpvJemzTPzZQZmPEd-j67bhq5wn-n5R_p82_ju3EG9IgrTGuWhHbNg-1Q50-Ht2evh7c63ZZSUsh_viv4TdVgnhdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
محسن خلیلی مدیر پرسپولیس: من شاهد هستم که تارتار واقعا دارد در پرسپولیس زحمت می کشد اما یک سری هجمه ها روی این مربی وجود دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105464" target="_blank">📅 00:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105463">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b35cee8f1.mp4?token=Ympgz0wB_FrETUiu76-LiStXl9m5864_5A-dy0oidkbxzOFY0wTjQnWwWkYQqtfwbSluuRQaqsfP1VTpCgd8257Z_B3VlBz1nmO0S9HoWYpqv98laSIbaGthEpfS06lMqVlWJEDv6yjpX7aSDUdOZnFAACIBlzn_j382nKB3U2mlIyqlNXIB0nfebbA-gnKDXaYHjZq6WA_BC3AXhM4KJDKZPXGlso-T8E5bPuZl-Qz3wfpDM5Pu6jE-TggwjqW1CubAw0YZ0BWbTM5OXr929XFYdIWieBeRohEvfKvt5ZWIetwL6pFiRsj-UllljgDpB2vPGHi7iOjwotN1q0z6RF7O-EWrUCvRCoSIDfCUmuXFai-hRNLbXDRCIsLy_J9FgMkBixhhi3xU34STze9wtLDsallqi4OZKrLDtSEQDOLbFkgTOMCLFRzxb_izZq7HO0WtWrMs84LKDF--aOz6Lrhgy_FwZEJjAlQXaYe0uCPJmhkVoqPlRxfbONZtv4JvBUNjQEVLCPHqI8JOjppcuSz3YXfJW94VYzTwK7x6PoGys_ZJUCeeOq9D2og73CbV69UI8pxl6dyRZZGMXcBjKg3BNL6ewyUUtYTtZtrolKLA6ygwJ5LjG2unDHyhE3eo6ngoYjWUYGWnr83hGyOINVtVAfFw2zvRINkwkRJhj1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b35cee8f1.mp4?token=Ympgz0wB_FrETUiu76-LiStXl9m5864_5A-dy0oidkbxzOFY0wTjQnWwWkYQqtfwbSluuRQaqsfP1VTpCgd8257Z_B3VlBz1nmO0S9HoWYpqv98laSIbaGthEpfS06lMqVlWJEDv6yjpX7aSDUdOZnFAACIBlzn_j382nKB3U2mlIyqlNXIB0nfebbA-gnKDXaYHjZq6WA_BC3AXhM4KJDKZPXGlso-T8E5bPuZl-Qz3wfpDM5Pu6jE-TggwjqW1CubAw0YZ0BWbTM5OXr929XFYdIWieBeRohEvfKvt5ZWIetwL6pFiRsj-UllljgDpB2vPGHi7iOjwotN1q0z6RF7O-EWrUCvRCoSIDfCUmuXFai-hRNLbXDRCIsLy_J9FgMkBixhhi3xU34STze9wtLDsallqi4OZKrLDtSEQDOLbFkgTOMCLFRzxb_izZq7HO0WtWrMs84LKDF--aOz6Lrhgy_FwZEJjAlQXaYe0uCPJmhkVoqPlRxfbONZtv4JvBUNjQEVLCPHqI8JOjppcuSz3YXfJW94VYzTwK7x6PoGys_ZJUCeeOq9D2og73CbV69UI8pxl6dyRZZGMXcBjKg3BNL6ewyUUtYTtZtrolKLA6ygwJ5LjG2unDHyhE3eo6ngoYjWUYGWnr83hGyOINVtVAfFw2zvRINkwkRJhj1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
🇮🇷
نظر محسن خلیلی و بیژن طاهری درباره برگزاری دربی در اصفهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105463" target="_blank">📅 23:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105462">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/125703b27b.mp4?token=hFRWnq7hUvYoWshLXk1Iy1nTx0yDuOTKesC0agIhBmunaBidJyVKaqB7MEGmZ8MsoeiM12_aekR47o1WqB0sGdoETGTZ4rd8n0Rgr3HSLxupwEdVVIPHuv7cmWqfUsB8nWEhJh1Cm19SDKyNs3_pjGuPrlPEpFn57HKLbaGXTbnDYMZvcObJIrCkvFWoY8xHgSbs9wEeoqzJDyGtjrXCmeFLjg1sdOFYQKVshk6vSyUMpJ_9lMMnw7Vzj2iztyUOkAyPse-0ASTy6qOvK6wJmgyKbeIO7SaapE0CxM6AsFi7nWzcyDa09OzZ2behtau_WoLClOf6UiyPEcQkmxAp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/125703b27b.mp4?token=hFRWnq7hUvYoWshLXk1Iy1nTx0yDuOTKesC0agIhBmunaBidJyVKaqB7MEGmZ8MsoeiM12_aekR47o1WqB0sGdoETGTZ4rd8n0Rgr3HSLxupwEdVVIPHuv7cmWqfUsB8nWEhJh1Cm19SDKyNs3_pjGuPrlPEpFn57HKLbaGXTbnDYMZvcObJIrCkvFWoY8xHgSbs9wEeoqzJDyGtjrXCmeFLjg1sdOFYQKVshk6vSyUMpJ_9lMMnw7Vzj2iztyUOkAyPse-0ASTy6qOvK6wJmgyKbeIO7SaapE0CxM6AsFi7nWzcyDa09OzZ2behtau_WoLClOf6UiyPEcQkmxAp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇶🇦
رسمی؛ السیو رومانیولی از لاتزیو به السد قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105462" target="_blank">📅 23:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105461">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92fff150f.mp4?token=LVMm8crJTARiHzyz1AW1lz2Bk0Dbkik8Qcd6zzIuUwEU7KCx-joWPqx7_V8SFCAak0xl39n09fvFEgA68uPWsp633BTR62y13Sp6a0-c0n6yFQ2tLkQjTUzeAB2jIIgoZ8GsWyID9LXED9CEEKouT5i3ig04Nm2y_cTJUDofDaIyXA-Y3rwcq2teAAvU5UpTkcUlp-sVf6vL9Zk-5dom3yyq-R0ootrdcLWizXOJZMZRAgW2M8huR3x1bLoWIo-wUlNFao3W6wpVxq_GZY8Ga2Ox4ebRMMqwGVJCcBtJTyGYZBbezX0oAl2ITCv_D7KbPKwAQ2wY7v7SppopNlIzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92fff150f.mp4?token=LVMm8crJTARiHzyz1AW1lz2Bk0Dbkik8Qcd6zzIuUwEU7KCx-joWPqx7_V8SFCAak0xl39n09fvFEgA68uPWsp633BTR62y13Sp6a0-c0n6yFQ2tLkQjTUzeAB2jIIgoZ8GsWyID9LXED9CEEKouT5i3ig04Nm2y_cTJUDofDaIyXA-Y3rwcq2teAAvU5UpTkcUlp-sVf6vL9Zk-5dom3yyq-R0ootrdcLWizXOJZMZRAgW2M8huR3x1bLoWIo-wUlNFao3W6wpVxq_GZY8Ga2Ox4ebRMMqwGVJCcBtJTyGYZBbezX0oAl2ITCv_D7KbPKwAQ2wY7v7SppopNlIzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
گابریل‌ژسوس بعد از حضور در تمرینات فلیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105461" target="_blank">📅 22:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105460">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbghjJ2P1FhtCdHAGh3g2zTq_oPT2SHGNVI2jXTSqAH4yqNhZtJovjaeQiI4mvhtYfnFriME36UyT9yuXmhGhXM7sOCMaOK4QoeL-MpCRs1FJO8LfJgiiqB_ra4XInMBCdpDyiMddwkrHNiEsKjd-8_qDgfIHLhISzNWt96Fmx38fa5ayg25PoWQ-LbHAz6R-lncahuyRjZEkzA4jLLkjxl8Ce05ehwJnKuxgRiR_MAdrM_JYIJzl0TRzemBHH5XvkqtqX6pamuFHKlI7asrOxFwyJCZ2Cvlv7eNIFJZBFZSENk1bsNTa_qjPMlA4htUd-FVmrRoX3N8QLO_4eNJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید حضوری با اسنپ‌پی، یه خرید معمولی نیست؛ شانس بردن BMW داره!
😎
🚗
با اسنپ‌پی می‌تونی از بیش از ۲۰ هزار فروشگاه حضوری خرید کنی و هزینه‌اش رو ۴ قسطه و بدون سود و کارمزد پرداخت کنی.
🎉
🥳
همه‌اش همین نیست؛
۵ هفته، ۵ برنده، ۵ جایزه در هر هفته هم در انتظارته:
🏆
۵ گرم طلا
📱
گوشی Galaxy S25FE
📱
گوشی iPhone 17
💻
لپ‌تاپ MacBook Air M4
🎮
کنسول PS5
این شهریور، حضوری خرید کن و شانس بردنت رو بیشتر کن:
👇
👇
👇
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105460" target="_blank">📅 22:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105459">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c856b1122.mp4?token=dRehqhEoN1jVkSQ0ylVzs7VcoUUItxZU588Wm6vBnws44OoUl8AeFLWVqp7S7WE20MLactMBy87ycSKx91qpZQxNvpEtbcBj9TqRKODpxU6Y6uXN3Kpw4E3A8yRjLo16M3we8QB9qeGOMAid-iJlXqwQ40xngwX_JUpA_mQP8nb-qjo_WScMEFmCC-OoEZXP-nHGQ_r5w0v6MBImO57bOJ12lyoEuMoPBwnUWcyh6fDMIqWRwERGw3JDCfC2RuodvXipweyOqUNNjELSYrSNfyhLn96Eqz9gasrIfN_0wkIn-7VTvxRan6AInJZ4-BoXEh2QAUcCf5YeZQkEdUTXpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c856b1122.mp4?token=dRehqhEoN1jVkSQ0ylVzs7VcoUUItxZU588Wm6vBnws44OoUl8AeFLWVqp7S7WE20MLactMBy87ycSKx91qpZQxNvpEtbcBj9TqRKODpxU6Y6uXN3Kpw4E3A8yRjLo16M3we8QB9qeGOMAid-iJlXqwQ40xngwX_JUpA_mQP8nb-qjo_WScMEFmCC-OoEZXP-nHGQ_r5w0v6MBImO57bOJ12lyoEuMoPBwnUWcyh6fDMIqWRwERGw3JDCfC2RuodvXipweyOqUNNjELSYrSNfyhLn96Eqz9gasrIfN_0wkIn-7VTvxRan6AInJZ4-BoXEh2QAUcCf5YeZQkEdUTXpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
بابک‌زنجانی از دزدان قهار مملکت: پیشنهاد ۲۰۰۰ میلیاردی خرید سایپا رو دادم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105459" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105458">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn4Op6ziUyAaZQ65ELMC9Ml904ZlxFRs1MULZ2_SqaMOg1jSoDqNqki3Dr5aPpUH6iW_ywBknSldh8G5zSXA4XFUUBob1WiQJEa4KrXi37k0Q6ae2UA9TyPr9QMAA_7VEjaXeeQqUuBp4GA9rjA8h95reoniO8Hyp6DDIPlPHPqqU-UUfvKCKPPX9Rga5FUXNQAlbXOMmmXsMxi8kcDaaq_EgI1_azLVpIU5_JuNrhkEF__UkRayPxtnlpeU4fzb-wJeYdkawEQXAxzwn049QnhAxESPt3IuaMr_BtFi3KMITQzgWDivNZcqafxc5lhum49q2JF6zStiD9wFMrquaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
💸
درآمد باشگاه بارسلونا برای اولین بار در تاریخ، از یک میلیارد یورو فراتر رفت.
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105458" target="_blank">📅 21:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105457">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/666c84fc7d.mp4?token=cnrjbKZmdONQFpk2TpffN6AQdNjkcAoCYVrEdK_iG4GM0SNntVcLgafLbK68TAwOm4By4B8ecB_JXmzKJ-TzgeWgvmknhLhVIqz3n0VFFi0W87iBTjZnK-LDlKG8IdKRnuIhnTv3CxAKY5OZQ6cTpLlxUINoHWGVs4WUpwWNiaIYAhgR_s7hjUpDwJNI4X_3pZtf1g4dPp39KhJIIpaPVtokKEukNYSc7eZ30GmYT-SH1D67er0rXf2To7bJ6YPP736jS1cYxvT_TU8O_q8sVRZKv_ZHmrCbNwn1CTFTP7euiTzVEyQ1NkQoCVagYNaDrHJfxFXy-SCUNBrZzWi_fYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/666c84fc7d.mp4?token=cnrjbKZmdONQFpk2TpffN6AQdNjkcAoCYVrEdK_iG4GM0SNntVcLgafLbK68TAwOm4By4B8ecB_JXmzKJ-TzgeWgvmknhLhVIqz3n0VFFi0W87iBTjZnK-LDlKG8IdKRnuIhnTv3CxAKY5OZQ6cTpLlxUINoHWGVs4WUpwWNiaIYAhgR_s7hjUpDwJNI4X_3pZtf1g4dPp39KhJIIpaPVtokKEukNYSc7eZ30GmYT-SH1D67er0rXf2To7bJ6YPP736jS1cYxvT_TU8O_q8sVRZKv_ZHmrCbNwn1CTFTP7euiTzVEyQ1NkQoCVagYNaDrHJfxFXy-SCUNBrZzWi_fYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
چنتا سوپرگل زده شده روی کار‌تیمی تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105457" target="_blank">📅 21:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105456">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
⚠️
دعوای خیابونی تو شیراز که یه دختر به ماشین پسرا زده بعد میخواسته در بره و ادامه داستان...
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105456" target="_blank">📅 20:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105455">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f597aa331.mp4?token=i9xmHxozlAZqh2ZptRSL2Q9spKGKsoGmcuLmzIbRnbpBvmM-7yD_-kutPiPA0HQJFVroVrOcSm0DECadOy8rdFLbaNnJ2updwdt01Ttr74dgWaTyhAtEShr1osV4j-j55qnuYf0gg0Z9QmUR8AWBhiSaGXYLhfH5BW3LjwkxkBAK3kQywl7n13Smo5abD3PCX2mKHyoScGW1HIvKOfbSTJJtSV4gfmwNq0jsw-ULcODR05VVPCx7ie8bY8xOXLZbr3RDOKarn0lXPE_AYZXBMdEg-iJOv_k6l1AhYdhoSKSPEEBGPQCUZsVmkcDBQzRDnWH3zfWSF5QxvygSQCqgl1IIrAU3c-baGlEP76CVpUnrbOxrNNIKa5ViS2_9cgw_xG-n9YN4CKuWTVsL1NC8SBtdIFJfD0vTvm4TuSZonqPKe9JTa8Lmjlnoio5brxm6xELRILwQGUbELlRmlYVd-Fu-VT-5ctzm-5-XQCUof2rPyvpSMb2z1GvCN7ZxdfY1rDFY0XhP0ubY9YJd0o0YHpKX9GoMu-XZhJiyjo6wrgTawDOEvJpiKO2AORXe-0flDsViGk6_wTZI8pmjG_kXzE7YgUs5KL0kDvEjtMIhf9o1lSfjh4JkoUAHPGMZTM-en5dF9bCdFg2moIhbQ7uvcnRfV98quIbq3scTeaWdNgo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f597aa331.mp4?token=i9xmHxozlAZqh2ZptRSL2Q9spKGKsoGmcuLmzIbRnbpBvmM-7yD_-kutPiPA0HQJFVroVrOcSm0DECadOy8rdFLbaNnJ2updwdt01Ttr74dgWaTyhAtEShr1osV4j-j55qnuYf0gg0Z9QmUR8AWBhiSaGXYLhfH5BW3LjwkxkBAK3kQywl7n13Smo5abD3PCX2mKHyoScGW1HIvKOfbSTJJtSV4gfmwNq0jsw-ULcODR05VVPCx7ie8bY8xOXLZbr3RDOKarn0lXPE_AYZXBMdEg-iJOv_k6l1AhYdhoSKSPEEBGPQCUZsVmkcDBQzRDnWH3zfWSF5QxvygSQCqgl1IIrAU3c-baGlEP76CVpUnrbOxrNNIKa5ViS2_9cgw_xG-n9YN4CKuWTVsL1NC8SBtdIFJfD0vTvm4TuSZonqPKe9JTa8Lmjlnoio5brxm6xELRILwQGUbELlRmlYVd-Fu-VT-5ctzm-5-XQCUof2rPyvpSMb2z1GvCN7ZxdfY1rDFY0XhP0ubY9YJd0o0YHpKX9GoMu-XZhJiyjo6wrgTawDOEvJpiKO2AORXe-0flDsViGk6_wTZI8pmjG_kXzE7YgUs5KL0kDvEjtMIhf9o1lSfjh4JkoUAHPGMZTM-en5dF9bCdFg2moIhbQ7uvcnRfV98quIbq3scTeaWdNgo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
یه‌گل‌بخودی جدید در پریمیرلیگ ایران در بازی فجر سپاسی و مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105455" target="_blank">📅 20:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105454">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKNSAgewS1SkTyGdCjQHfoXNHjnnz9bRtiCF4Y1jRY9yJt9-fTuApdRjHj7VuhCFbDPeJ4j6N1MEMLd3lGqsizSOsIkU_RW3Lrb1btVUaqJqrTbDpsaQRCyUXLSpNGlNDnnQ62zNNJ5b3fDEGuZiA5NOt5sv5VnbW5Z9IJaBTYuk66bPZEOI6iXjO8cKy9CMSy3PTQB1jYthlYrDR0Tw-a8d2eWRM9xjkS5xli487kb7f1A7hqme0KUeVibQS6UQF54XqWhJtyltEim1DwbOc_mR-m5lBA2osHHqPscGZ_5O-_fIEmenBe-7qLfzBHBWjV-mklWHfsd6Y-zFZrmkFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مارکوس یورنته پس از قهرمانی با اسپانیا در جام‌جهانی از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105454" target="_blank">📅 20:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105453">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESPlj93YTS_si3U_B2xc6E79htAmChtWMMjtR8uDjq4QNzD8qoFZ7kqPGyAaui3D9u7TZ7Wbdgtmp_OUd6DGs3XnAdkWB7D9ojlHsT1b74YHphmJFDQ5gbhzKWalfsTVbZ_W4mJhVsati1lDSwbxtTIMezPjGVhZ_zE0QZ9HreX1GHhJlMNVyNNFkwhZPh6lYuGu1PgQITFA1b6l8DUQw8Jh5svRa3irQTUtTYvuY6UW6yfKRNF-aNEb65qhBVA3_5vMmpY1-2AaUxbBliPde-gYDA-58xIbuI4KZVBMnPikBWgpFrkh1fFAqN_Cn8TUoohe1hfxFPi3SG1lXYaNng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇸🇦
رسمی؛ گابریل مارتینلی وینگر برزیلی آرسنال با قراردادی 4 ساله به الهلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105453" target="_blank">📅 20:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105452">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCJwUjNA0oGeYmCOMIg9K84fnLMESNcnsiag8UMhFSIBF-IL6YiYrKFVxqMPSCON-akc7KeujSixsRQc1XkJxU2cg4nv7ULaGIeSiRtEvtcDxQy4J29napbqlyq5wE3euZ7ZZWUYl3rX7KEomeHcJJP8QnLZg5LNQb1t709ZWQicPFw9gW14N4TPsQ7m9JPjiuO47Dg90iDH8pGQmmGOPVZosDr2uImWCKP8_Lb2IeIfK3zNA40CE8uqDu6MDygtadq5aE9u0UKEOhmFX7fVjhU2Aa4T1_fW7fR0q0o87i5cylQJ6Av9QHlCjzjpDXNIABtAUQF8xokR-Kd_RRAsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✍️
کوین یامگا، ستاره سابق استقلال و نساجی با جدایی از تیم الفاسی مراکش به کونگ آن هو چی مین ویتنام پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105452" target="_blank">📅 19:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105451">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8qvLQLkrHU9qeAk0CE1RGeyoHyGzC8rfjesAjvSalW8wqYMCk5D8tQkCjBUTk922jRVJ5AVwxKEQ_s0ZXOWeUbeyDM6uaPMFKOsWtXRi7HrxNrJhAPQlDsMy8zW6GQPSyvQ0GTTE8t95qHq9vTabRnrlYJi3JznVcuR6fRkDX4jZL9qggzrR0FKRIiN4XC0SP8MkZy2_jxlXZB-jZrSaDz2ridP0xCFDmwniXqEvYEDNEDlA_SBX2ILopdevcVc4iTri9RwSM0f-d4fSp4SkucJxNB0dYOOMESpsB1s29a0cNONC8l6v7s6zRmUDzugT6CBVKXQTzyKfZs0BRlIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
گرانترین نقل‌وانتقالات تاریخ فوتبال
🇫🇷
نیمار از بارسا به پاریس—  222 میلیون یورو
🇫🇷
امباپه از موناکو به پاریس — 180 میلیون یورو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انزو از چلسی به سیتی— 145 میلیون یورو
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک از نیوکاسل به لیورپول - 145 میلیون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105451" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105450">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAZAfxso1Hr74Zl3M8CsCBPyMSKfg2OfuABDBYztQUpcn-pmPUXIZWE24xer5I8djoaLzCgCsiShYgeUgGyJ-e-gcgzFr03eZuj8KMtJ5BEn5nNlAwZswsuB3xrS0XVFebKLC3MjDRPjpsq0Y8xPumMASVqr9H1IS62A4b0Fy-1cJJdSwuadR61vazXoLUcbv7hcZpUPpgA-5GS3lFtchv9caDtb1WbpSDdmQoyzmJ5aT-q1poz0J8C5CL0STZq0gaxlpnTGyjPYfKsomZ8wKs1WwMv-tL_Kwi9CKfDxPUAyWBatGFdFZXdgJeYhRqhR-6PBUJERWaqh5VWm6ZWk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسلامی می‌تونست تو این صحنه گل برتری استقلال رو بزنه ولی یهو از نوسان قیمت دلار سردرد گرفت.
📱
«ℳ𝒪ℋ𝒢»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105450" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105449">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egHEsKxRZh6ek3hzTP3Wyr5JZRita-bWmrdIuCEGhxyASFmI7-KWkWbfhXO9WAvTigYYsxMP7rOLg4G-8_v5PtvMqWIEKRNmjFc5iG3rLKV-vVjL-0IuOsL9RFkbY3TqBNZsnGGxsTov-U4pjBAMX_zy_H62Xufsd47DlltFcisTy-DqlsopURP7GjFX9baUlKxsVwBGbKswLRq_smXRpw6U884c6PyKo_jerfVps-YkwrD1Q-cYPH9jgfmWs50M6Qi5j1xtwQUXhjCxlOT9hXiBtghblqOTO0MprGHH4NlEbARjV4mudaqpDFEJ_LRrL0VZS7ZPQQByWQJR5y4fdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد خط‌حمله بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105449" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105448">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYT2O3pdXFNcuKVS0YKnWxsOUNMUd4wDvS1CYotLvYU9no8_QT3lYvDxoKOQsEZrH50mNddoJIs28Ox3O63BSt1uyvVZA9qc93wTwVdvNRbZNLZPqlYYnYTECZaUrkyXVXYZobKojtotzojWBN65YRdTS4AgCjtIIw6Jwf-2ESrwthitf1ksNvZMgocbryx0VXARwn8mZAlvFifUtIx8Adobp9EdhKWvFil_zkK4YxTk7Am8E3qC9OaMo2Lwto2ejrDBna4w9GfeAUt88RH4HzBLY9sPJcpRKtmc_xqosNMbQWQMnhSx3ORHR5jMYC94OUqShF-ZMIN7wY-xbZ003Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
آسنسیو مدافع رئال‌مادرید از اتهام پخش کردن تصاویر لختی یک دختر ۱۹ ساله اسپانیا تبرئه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105448" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105447">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r49RZuwrCKGGquZQLBV2RCwBWcDxjDnomGXP9FpnjPiYNKnmihYiAZcRXwNKIR4DXEcAF-wS6sIxXq3JiWsxnUApGRj4rlO_5180uqy2aPyJt_e7WJ6ClELvqE0Ob40fOoSv5fMi0DN1ZSEK_KDsj9DZcVucXSaPM26BCgzmWI2GfuqoEluPmzVizoUXiiNXiKI2aXQ_T_MAquW6nklq8NE0CaFPritl1DiasgtvQpPJ2PhjSyQRID8zM6dFhLngnnqSHDntpm9UDrPLgyL24BHq5tnmnaWVxcxuPQXsk9IWQ514RlblmBA7aZNIcNijQqgodn54TehIiYY19Vb_9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
😳
ترکیب منتخب ماه آگوست بارسلونا چیز ببخشید لالیگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105447" target="_blank">📅 18:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105446">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d07bdd0548.mp4?token=CNjjxnxFQEgeDPln4Ua103M-Eeihr80wnigvYFugihjcsTZ8uOFLI9fPQr_tcngRCmP8WsI9GHh1aCiUlyTlfOu2Bcm2Ty8Gyoh26oCznuL0vnXCtUuwoAZ2J7okPMd1OjciHsaRPQaLPtKoiRmM_mrb95vcYA96CufbATIcwtpZDAY7Wq3AINhIHDWeiywi9uOA2cL9jj0SlSTXubvjeE8rxIiAIGzyOUC6AlyMlEa5xE-UliFSWiTj9qKM6f637vGE9iFEfRIJnISW2NkuZBH--cAzT6kUn2ThLg5ssEUAhhd4YtlTlumrm3l9effGc-xN5WsLdUQTwGIPypOUnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d07bdd0548.mp4?token=CNjjxnxFQEgeDPln4Ua103M-Eeihr80wnigvYFugihjcsTZ8uOFLI9fPQr_tcngRCmP8WsI9GHh1aCiUlyTlfOu2Bcm2Ty8Gyoh26oCznuL0vnXCtUuwoAZ2J7okPMd1OjciHsaRPQaLPtKoiRmM_mrb95vcYA96CufbATIcwtpZDAY7Wq3AINhIHDWeiywi9uOA2cL9jj0SlSTXubvjeE8rxIiAIGzyOUC6AlyMlEa5xE-UliFSWiTj9qKM6f637vGE9iFEfRIJnISW2NkuZBH--cAzT6kUn2ThLg5ssEUAhhd4YtlTlumrm3l9effGc-xN5WsLdUQTwGIPypOUnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
آمریکا برای اینکه به پرسنل ناو هواپیمابر آبراهام لینکلن یه حالی بده، برای تعطیلات فرستادشون تایلند. از طرفی تایلند هم به پرسنل ناو آمریکا اعلام کرده که خدمات جنسی زیادی در پاتایا دریافت نکنند تا فساد اخلاقی در بین زنان این کشور گسترش پیدا نکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105446" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105445" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105445" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foorSyP-BboWcpSgkmi0r9djy0q6U_8fqvf0jid5zqUOZuypunmgVT5x9GfKgsqRdF3iu_bArq9Tv0ZdvazXO9MAcY8jNDdX-XqTVoHG2fCG0k0UU3GifNo7Z2ApnPWce0nh1jQ6l7Cy5ixtDxztSFFr3C1weKqYHhvOuWAss4AArU00rHQ8K2D8qt8TRJfCAVyblz11GZBUKaYe048H7RRQ5azpX1LyxVobwpSjcq7lc-E-AFcUJyGym_o121p8sE3h0TJt2vCPlx57Ki4gq6VfIOy4zECZqNhEGIvBnbo5Q3ESmVbhy6mSAUPhUPc7fan4QdaewOxN5xLkBEMogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105444" target="_blank">📅 18:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105438">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWDbbPMDMROjolBQb2Ig0WycATQf98eITJFlNkJ2QoqMLQR9V4XOY4l1trJsH9qY7E6Wlu8HkOf5dIaGN-2FyMcSIUwXFvR3TB1Y-YDHsIWAQwkGZ-xSVyAOgYP_739w5sFFHkUxlKA1Fcan56peMGV_arqLXHJxlyHUBcPtN0-68ZDaaVU1ou801OB1VvDmhIp7MzErJHbY4txcH2AfkcJMiXyc8WLrSt4pqjvReUgUywTBep8KxbQwsfnq8wKPaABOzXYKQKCY2XWqE6LfmGWYGCAf5yW3C7UeiZM8eLqXMj1SfTSwPu8eSh9wsXah7o9UU3dWWzDPWdtrkB0JtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2vpsah8LU1DTtro_unmqujr08E__oF_DvLm5-R6k2OeF-vPGwx1JbH18f14ybO4oGeWUatQagDjJwpujF3cus_0pB0gdGz42dgsVNbjzxy7X-kWUKq_RvBAF24gChdpC14ywkRLmTho5nyOWtbIU3HDENmwx-CDspGP-1fljE0rpsLjqb3jqyB1HD7d4DkI5IKhBTxKq7qsH9tF3R1W-hvDP17ftk24oxfWlLjcb9tJcsW98iLTkXKDvoh_AdFmqi72OtfK09OmT1maVTcqOIr-M5w5Kj0JPwwgDHU9RIA44ZuZy_jPVf7ovj4kMFBibnAU2NnlX96X26-CkTfKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cSYxGpCjoPgG6_MJb_He6nGC-dCjmRPw_PtrrDOw5ajQ3olOaSpN7tRPtx8JbVmz2kczLRxCxA38VKZKQGkv5uyNjEYHbTbHxACOCNTi_xNLkEksWae2Y473JnFsWpLEv3F0pvIeP-WMJGijNBSKW1uD9zTVzgpVxoFcB5i991y3eofUpHOeICNfJsMYH-cVEurn9tKKxIgeBRUD6ALntU-27a-eNC0NTPZPLAP6kIf9pcyx8mUFih9zNc5M5BQqfk7jXH3IF34PMjk60mlS6fSiYepxFt_TEb9CeAa46oEK_lmaoyZZf4KdIIq1KbOa3DDjjNIss9B5I-U48O3lJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVF_qVl6IfNnrtpe1aY7AQZ_srhWmZCQOcQMbDuQdRmtoC6MIvxR-KivoX-Z9uWmz8d4_gf19f6vMFWZ5odDR2nZYGiJ6Hp5toRYuXjv2TD7y7FRuEZydvTGPdF8MbHIHXosd9mQ08kVcXiwafSp04mW0gofmyET6Ou5suIEdrJTCtsNIL5X-hApAJlUnr9yZhqDaM4h80LSd8UTl4gGdIHDyI4LjEUR5N9ZWO83lvgUoMY6CGs7g15VXEyjk0JrWFbDMOadtsZAXCIIg2PnJZ7q4_-xhqN1HqLtwDdf13gOlL_1XcuNC17s86bjeXs7hSWzhWRatjJYxz-FH0Mcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIWDyVY2l7tDoQ1M1YRVOnieHTTwN7KLnxmPS2ha4Z-oxGMZgQEg770CnG6g7hQF2v5MhLQ2Uuv3ZuesflT8LoBOJkFYMA7fAaIIecugeNU5XpzGIXovKPnv-kbMyNfF239NgaIUR7baeGYHh1NiUWwif8ASGXS1tIbTwdSXSZQKHtD3lZbHdhe0DWHtWRZRQTyfU6VR8gce8PdJG6A3AP8-q03t7VV54mzBJfRTAWbwRnLx82PqFKPx7y9g9rSQMdFDkmDqOt8nv8SGSOvg5CsUDmn_4cyz7y8KDm_Bj_TlG_tlUia3P9Djz7eVmQb1lTGZYgZCiDqvLOFSnre87Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
هوادار بانو استقلال در دربی نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105438" target="_blank">📅 17:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105437">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3894ae1ef2.mp4?token=kWxrODHZDPyHjKT4I3u1GmRo5IodfPb4JhVuulZMqzN0_t5NrjFkk4C6LJz2eIKOhcPQBf1PHTlffUfLcsuXatkoIMYWcFoW3in7DILEAPRRjWjRrNdOQwB4vN7TQUvYORwpHTA4c3yE3YWVLKbGWEggXmrxBVosHqDQyG-LaO_-pkrrjrcncqXoB11AmGGnH2y0PI7skQEYHhOjQAxqa2j8JMVVWbWrwo2ft8a2d0UnlpnOQbONUNxjFXenCkdIq-kjqvUMbiabqICvFWKrNcWPvzzRLbTEQH7rxew3xhXepUX6p2ng77roL8-A7CQBRHEskx2SzSpPxh9kPpNcCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3894ae1ef2.mp4?token=kWxrODHZDPyHjKT4I3u1GmRo5IodfPb4JhVuulZMqzN0_t5NrjFkk4C6LJz2eIKOhcPQBf1PHTlffUfLcsuXatkoIMYWcFoW3in7DILEAPRRjWjRrNdOQwB4vN7TQUvYORwpHTA4c3yE3YWVLKbGWEggXmrxBVosHqDQyG-LaO_-pkrrjrcncqXoB11AmGGnH2y0PI7skQEYHhOjQAxqa2j8JMVVWbWrwo2ft8a2d0UnlpnOQbONUNxjFXenCkdIq-kjqvUMbiabqICvFWKrNcWPvzzRLbTEQH7rxew3xhXepUX6p2ng77roL8-A7CQBRHEskx2SzSpPxh9kPpNcCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تلفظ نام سرمربیان ۲۰ تیم پریمیرلیگ که ویدیو بامزه و جالبی هست
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105437" target="_blank">📅 17:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105436">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4ef259e8.mp4?token=V0QoYx8f3CGU4wn9NGOmBBS2mRBf3IzGgRBYYJfH1gNObBt27VlX0avRgc4RuqlHSJfYcKcnoE2d2wpOB9R6J4g5Y78CQRRprmE7CcSYQy0Xag8kbXocBSxC3ye2gCQirqIaMkZH5EVTnVHV5EKMukCFmySmWpVd7DjXCVIm65zqBO5pZhfmtnnG5wEfq5LvaZc4eEOQpfoRYkBvQMpYzlK5xhF2mgQA8N_7n-HrnrJmejW076eqGlrv14LixpRKt73EemwUSyeJgBx2YuV2jx7AfQa8vy-_AdWQRI5p70O6R0wIZJ_HbOE4nihYihv19mrw06TpJthZ92YeIJmGUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4ef259e8.mp4?token=V0QoYx8f3CGU4wn9NGOmBBS2mRBf3IzGgRBYYJfH1gNObBt27VlX0avRgc4RuqlHSJfYcKcnoE2d2wpOB9R6J4g5Y78CQRRprmE7CcSYQy0Xag8kbXocBSxC3ye2gCQirqIaMkZH5EVTnVHV5EKMukCFmySmWpVd7DjXCVIm65zqBO5pZhfmtnnG5wEfq5LvaZc4eEOQpfoRYkBvQMpYzlK5xhF2mgQA8N_7n-HrnrJmejW076eqGlrv14LixpRKt73EemwUSyeJgBx2YuV2jx7AfQa8vy-_AdWQRI5p70O6R0wIZJ_HbOE4nihYihv19mrw06TpJthZ92YeIJmGUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇹
سازوکار نقل‌وانتقالات در باشگاه کومو، از زبان میروان سوراسو، رئیس باشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105436" target="_blank">📅 16:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105435">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f719399999.mp4?token=JLNi5fNFZkqHZlqbSbUXgKEQRLXUxmUqCQGErC_jiG1GiTGcv6-EKuGiFc6AOlnGb_w7k3t1cQfylBSHvFZig_gljw9IN1U1F7aXJV6uFjvlRlVM-gDKvfyWShlgz1s5epH6ObRHPJhqFf3u55RYYSbkaB4ANMN-79OWP_ubijYLwG1m8LeKi7cha8i70Ji1PZxCPYXtpY81X-SYWCd05aMXvsdetRo0ArcFrFmPowkKq6-s5a_Ck2c-I7zlUJZy7zJfRnfFDpYmXlfKED9U3E16Sb1pnbWh8lxIbXE130nqdjyUMMtZ3zKnDd59WqCUp6867gyTD6ldMj6dl7U3RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f719399999.mp4?token=JLNi5fNFZkqHZlqbSbUXgKEQRLXUxmUqCQGErC_jiG1GiTGcv6-EKuGiFc6AOlnGb_w7k3t1cQfylBSHvFZig_gljw9IN1U1F7aXJV6uFjvlRlVM-gDKvfyWShlgz1s5epH6ObRHPJhqFf3u55RYYSbkaB4ANMN-79OWP_ubijYLwG1m8LeKi7cha8i70Ji1PZxCPYXtpY81X-SYWCd05aMXvsdetRo0ArcFrFmPowkKq6-s5a_Ck2c-I7zlUJZy7zJfRnfFDpYmXlfKED9U3E16Sb1pnbWh8lxIbXE130nqdjyUMMtZ3zKnDd59WqCUp6867gyTD6ldMj6dl7U3RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
امیرحسین صادقی خطاب به فشنگچی: کم‌کاری کردید باختید بعد می‌گویید استقلالی‌ها دوپینگ کرده بودند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105435" target="_blank">📅 16:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105434">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/855a5a9849.mp4?token=N957HKdD4ZCD2jAAdkrZTABFW2GkOL1tORGtxWM4sY6M4sdrSydFYHYlNDJVMHIEIvMI4thV6QTyS_NDtdvRDQ6Rhv8JuZSLpEjZbukWYIkR0-9s3PIrtPppeLgKoq8_Fe-a01ju9YAU7oZhS9QLtnZ8lDInvNQkqe6MEPu-5Tj4KQ3GI8x4XvjHvTxLGhWsJ4vX3IaSthSWgDrSvdsi7jTs7XZUMM9RIKmxrlXkLaG2ffOqHA-ohVVPLxdPZKj5vPrK6YDcI5VVpd7EdK0u3ubifw10QNG1WdbegeWGNBl3Fjjq7C_Pl48YFkk_CfY-K8iIefx6n52o_YHS3QoDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/855a5a9849.mp4?token=N957HKdD4ZCD2jAAdkrZTABFW2GkOL1tORGtxWM4sY6M4sdrSydFYHYlNDJVMHIEIvMI4thV6QTyS_NDtdvRDQ6Rhv8JuZSLpEjZbukWYIkR0-9s3PIrtPppeLgKoq8_Fe-a01ju9YAU7oZhS9QLtnZ8lDInvNQkqe6MEPu-5Tj4KQ3GI8x4XvjHvTxLGhWsJ4vX3IaSthSWgDrSvdsi7jTs7XZUMM9RIKmxrlXkLaG2ffOqHA-ohVVPLxdPZKj5vPrK6YDcI5VVpd7EdK0u3ubifw10QNG1WdbegeWGNBl3Fjjq7C_Pl48YFkk_CfY-K8iIefx6n52o_YHS3QoDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
روایت وریا غفوری از گلی که آخرین برد استقلال در داربی‌ها را رقم زده: مسخره‌ام کردند، به خودم قول دادم گل بزنم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105434" target="_blank">📅 16:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105433">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d62c5ae06.mp4?token=k73NqxL1GPXj5tJtI_6gFraCOXYRHAmXqXheFJittOURIEdrmAxXam1xugHSv7ArcZL4D9Gv2A_Tts6Z8dQSwk1SQKy2rbMmqMpja9DmEC_A5NNVYYwwluhsAbSGFYOJDw4vwWe8WgB_XjnL3VaJPMChjrPqJCPU7a7kAv7qy-C5R2LrORjo8UiFySg4TKOxUGOpw9d5HYvMpOfN29pdeaV-TDMyQFJ9ceEYQU8Oww98FBB1P5X-fH6qAuWL_BAXRzwwCxK0vgBRT9kjAmU769iUmR2OmAZzA18QNkQRQisRnZc46k4g0H44nyAbxw6g4Q-RiNQN35CrB13Arro7EE0gvsu8dOSmBInmhS_TsCR_90Fwm9CZ18UuM3g_opVX2g1eXldDOZgSeRvWlf5VMkuM4Kor65ckW3awBngzwIuekwrnOxOB0nzwaCJcgl_fdagfoLMl6GN8Xi54yMyhBXlmoEdBY0sDvFiDVOMIIBl5A3Ox6i72d54RduPs6DGkJf8Y-XDYe3thvBdGqYbYtvc4eAR86DAdW0qQFjy3QsNlkBKNWc7R_FcTmk3POGrq1uKxgAvJaaLKxbyJkAJUHAE3NmYYhRutOiNnlRcNp8Tsb9c-_kjLNGxES-L02GYP6qjPxZ57GBC-0yt4Y2HxbAM4yLRJSYv50Go757c-9S8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d62c5ae06.mp4?token=k73NqxL1GPXj5tJtI_6gFraCOXYRHAmXqXheFJittOURIEdrmAxXam1xugHSv7ArcZL4D9Gv2A_Tts6Z8dQSwk1SQKy2rbMmqMpja9DmEC_A5NNVYYwwluhsAbSGFYOJDw4vwWe8WgB_XjnL3VaJPMChjrPqJCPU7a7kAv7qy-C5R2LrORjo8UiFySg4TKOxUGOpw9d5HYvMpOfN29pdeaV-TDMyQFJ9ceEYQU8Oww98FBB1P5X-fH6qAuWL_BAXRzwwCxK0vgBRT9kjAmU769iUmR2OmAZzA18QNkQRQisRnZc46k4g0H44nyAbxw6g4Q-RiNQN35CrB13Arro7EE0gvsu8dOSmBInmhS_TsCR_90Fwm9CZ18UuM3g_opVX2g1eXldDOZgSeRvWlf5VMkuM4Kor65ckW3awBngzwIuekwrnOxOB0nzwaCJcgl_fdagfoLMl6GN8Xi54yMyhBXlmoEdBY0sDvFiDVOMIIBl5A3Ox6i72d54RduPs6DGkJf8Y-XDYe3thvBdGqYbYtvc4eAR86DAdW0qQFjy3QsNlkBKNWc7R_FcTmk3POGrq1uKxgAvJaaLKxbyJkAJUHAE3NmYYhRutOiNnlRcNp8Tsb9c-_kjLNGxES-L02GYP6qjPxZ57GBC-0yt4Y2HxbAM4yLRJSYv50Go757c-9S8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🥇
رضا قیطاسی پرچمدار ایران در بازی های جهانی عشایری به مدال طلای مس رستلینگ (چوب کشی) دست یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105433" target="_blank">📅 15:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105432">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a16cd1aa.mp4?token=Kp_LhPZiS8e-kxVhRP4KcpVF2iExUNhPnvGapwLxuFU0hA9wdkfn66IXx18WB_ZDHXaI_USPnZV2_0Xg6UxvzNxg2kBuXQaL1nuiL_Y1QXOK2hG6BCVxfleg5IN9p5C-4TrF23i_maaKRXZ-af-GTogJWB74XxbuSAWOtqRWRgMfUMPQEk-9ioCnhiKF12_frwB4y7az1i9Cy07ug0TiQY5jGwdSz1S9Ywyyi0fBztkEPeJ8-d5UVQiXGAnqJzsl_heL0cMNT2yPxmjNVtFIFcO9y2ASjn1a2mve1j5bi6UkDTNu_AY0_gk813NRNXErNQROLpZr4x1ga7ZDm5Rh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a16cd1aa.mp4?token=Kp_LhPZiS8e-kxVhRP4KcpVF2iExUNhPnvGapwLxuFU0hA9wdkfn66IXx18WB_ZDHXaI_USPnZV2_0Xg6UxvzNxg2kBuXQaL1nuiL_Y1QXOK2hG6BCVxfleg5IN9p5C-4TrF23i_maaKRXZ-af-GTogJWB74XxbuSAWOtqRWRgMfUMPQEk-9ioCnhiKF12_frwB4y7az1i9Cy07ug0TiQY5jGwdSz1S9Ywyyi0fBztkEPeJ8-d5UVQiXGAnqJzsl_heL0cMNT2yPxmjNVtFIFcO9y2ASjn1a2mve1j5bi6UkDTNu_AY0_gk813NRNXErNQROLpZr4x1ga7ZDm5Rh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
اسپویلِ بازی بارسا-اتلتیکو در این فصل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105432" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105430">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqxghsRhAqzg11zetyzXO5x65CBLpZmftxHCV8qmXlwtP9KgUQfc4gEd8zW3mkQLKGEEUz7gov19-t6CfkO2WiCfBYHS7PMX6dN8X-cdNXLxTpiGSJK0J1efkrf51txwZVi_CPi0P_dfkrL6IcyM6PGpDJINscdhwblLRvFBMSrZuYVvk5WafU8o5RjQZP4s--yi57Qt163VVF_wdfdgFiXg95dNEWrBjkDHytpVb--7IF1W7SugkoDb-AoBv36n-EiK3-HXaW0z_XvGcAOMgZVFEg5m1dZGLmAJOTBPGfqlUVej4Vb2sHsHzLmngyvFKKXf_d4oG9VomtkN6kmmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLK2TPrvgLJtw88qFvN1CW_0g1YJyIx61U9YBQkmL_5DeilHeGImMnDJNyAlPPyhWpHIX8ioOkkX3RpNR9oH-gnNM6bNrD_4ppNYLizq2nXw-MAQBx3QPNzN_DMvD3bl86ZFcVEO7iWhDeXXzH-qVMgc4QzsOGFgTYr9imFzYkCt-fMzRCx55pYLe79hLmz7oZSPL6Jiai6ZDgxtQGBo0vmwQYJdByxWRgqf7kwHMnH5rcIh2rkJWUPUnocyYjLYFmQPAO_1LYrj9AavkGkNXy_0cq1IQo8wNIN1SoZ9qiZ-kfbP9lE7_eQDUsn_jF62NIUtUMgAPuPFc1jQoYIWEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
عیش‌ونوش لامین‌یامال و‌ زیدش در پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105430" target="_blank">📅 14:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105429">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8bq9U4-5bb8P2xwJzS8xNL4KIOlo01T_0jrXqyLvM72cBu7veAK__Punp4O1KmB8D_EDc-IA5-IZqpSop7RXeY7j2iTR0jDAA0C727fKhVI20VMgsciQZpZQr-xndhWqbtBVnEQu3DCvqJeuOe6MXh1QkYgninU1TixaVSOHpjnGSu81_tE7-0t5VfvMRPZ3tIQZ2gOfDmDBElMfnDCVrpA2keFxDAvwmehu3im428B1PWqLbm1uqyCpcFyQ9Hf0jEpK7tqLeOqmF7EJzMGguRa2LZs6eGXq-D0IeOEcehbpotJfLLD0i4DZ-1N9mzgDtZGs4Hh-OMD6bnUwIoznw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105429" target="_blank">📅 13:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105427">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaD8mcN9gspIRACdpReZeoLF3K3y6lyz3uSwoypkepdWE0YW6-9X2LdO2DPjKjmTxfG8Goq5kSjAo3krwawE0jW0jaISACxyyeu9X_fkU60Jq_u7nzYSjWC1Ml8rWKF1cksS8e_BQvnB-Mkd2pvkShBEIQzZlV9OEgnMCDeGAfBnXwrDTeduchgSbzPAxHGVaxdSBuO2x5nWfAPWZW3SdQeJxU33si7i6uRuaiRsm12-RT4FwQedNwOueeka9pBXNvU_iF3ZUTrokGUXLjzWJCuSFQvv6cBQb8jeO-w174EaRNoQ83CG1mOJBuyc-J1UBH6P-s2ONithmgGC3bTsPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنعانی‌زادگان کاپیتان پرسپولیس از صحنه مشکوک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105427" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105426">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEarT5ndKuF-Ja0RQkzDbiaILNmM6oKort0Dg8aX53yG6hbBITgVwlrYzCXu02ZGu0CKu6a9Dh4XBPyxgVfui3k5woS5paGIv2mK-8o00GfLnQm-7SQEHnxZ38QphpWALShAxS1icFF94UQak4TTwE_sXckWNtDxBbegfQEabinvsW-f4-hxZu3PrfYLgB7FL8Vzno4X355Y2MwnYViD82lm3qhqDsy9t2AvQdtPQb0XB8hgrPJq42c3iSOWDTdckEAFc7BloxCIZVu7E05mHD2HrpWQL5hFdXYnlNPVnCdkr5WicHs-znwhXGWsmJxhQLqL8yL_QrLaFWRa9TaGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!  باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105426" target="_blank">📅 13:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105425">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05e1941b9.mp4?token=sGqJePBiuuXQdy5WStRy8Gt447FPFhvdvLe_-5OcqY_Xx_ikiSBKo-PaeqIcdNNBTshN1la-6FUvgRLGhMfa3wJwMsHZ2S4XgYbXXLaqqQu5cfZODTI0unNHAq6EiJVr1Ztt1qaQSnlZsDukDOFC7T-Htb4B7Ew6-66LesFtIeRdYL2UWrzECkzYbrM1XHKzFxA4JHLG5IIg3Qc4v-DpIl6YPJAtaAO4f5SpPRVAjTl8zVAnKFkgumxKxPYIrgPwY6_HST8tn3cmcNieYgx-ZguTbLSc8SH0kWSBLGKOUEqCgLFK9ezmoFWIAuGe6xQwebazDvu8Jmxt821bksoMLScPwPKMZr13AFDo39VWpvzMxNfJ8nGYkujSx3ZsRAjoi4DJ0rBRx58L1TX5zH-w6j5MYMNfhEXQc4wIcgVXFXSvq_lokZLB6ygcMblvQdSQWb4MW63-ygWhbci209exWAsnedEP-zX7CjzDlF8zDGXwLciEgf12BiiCdG8oOFqWQIzn_qt2ocIHIS3zWCV2yYjhfyfRF9b1PZUP5A9b7LgNUw66MPWqCpItYbkznP_PkmZ1eJg6UrSZ4EvbLsK42IE9vQ0fIzpMudilSX5NhfD9xu1vSxElqCNtTnf6G3wsyBSHopmTAWAQAedOsREKCOgASwqYQEcRFEzbxFF1C6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05e1941b9.mp4?token=sGqJePBiuuXQdy5WStRy8Gt447FPFhvdvLe_-5OcqY_Xx_ikiSBKo-PaeqIcdNNBTshN1la-6FUvgRLGhMfa3wJwMsHZ2S4XgYbXXLaqqQu5cfZODTI0unNHAq6EiJVr1Ztt1qaQSnlZsDukDOFC7T-Htb4B7Ew6-66LesFtIeRdYL2UWrzECkzYbrM1XHKzFxA4JHLG5IIg3Qc4v-DpIl6YPJAtaAO4f5SpPRVAjTl8zVAnKFkgumxKxPYIrgPwY6_HST8tn3cmcNieYgx-ZguTbLSc8SH0kWSBLGKOUEqCgLFK9ezmoFWIAuGe6xQwebazDvu8Jmxt821bksoMLScPwPKMZr13AFDo39VWpvzMxNfJ8nGYkujSx3ZsRAjoi4DJ0rBRx58L1TX5zH-w6j5MYMNfhEXQc4wIcgVXFXSvq_lokZLB6ygcMblvQdSQWb4MW63-ygWhbci209exWAsnedEP-zX7CjzDlF8zDGXwLciEgf12BiiCdG8oOFqWQIzn_qt2ocIHIS3zWCV2yYjhfyfRF9b1PZUP5A9b7LgNUw66MPWqCpItYbkznP_PkmZ1eJg6UrSZ4EvbLsK42IE9vQ0fIzpMudilSX5NhfD9xu1vSxElqCNtTnf6G3wsyBSHopmTAWAQAedOsREKCOgASwqYQEcRFEzbxFF1C6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🇮🇷
🇮🇷
تمامی موقعیت‌های خطرناک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105425" target="_blank">📅 13:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105424">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNU5hYcXB-ow636iE1DXbdM42dz7pCsmkHc4TiOmXKPRsr_B2wuPkWZN_nWXOfxScHs0MERKJBAgIW3611ZiUF2tTFL3KKIiL3bfl501fXkI591isFhw2BZbYjPlSpJ-yYRFBhGt4oxwE_bPQaE1I_b0UwUiBg7x1J5DeRbcOoXrmVEZGHdCdwR4B5Tg7XVS3N2oFTOeeK4u3Lip-FGT4jAc4g9F75ace9hdEpRD1w8wB5jjvosupAB4omKJHA06oUhyuOj0_WROCoKgRKRP_vTgjNKcPq8CLqf_GhFmL07PYi9cANFSf7gtdmOBzvNoPHWHuEfvnH5FazG3bvnQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105424" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105423">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105423" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105423" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105422">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkSRVir4A2f0VmWdRfQLwvHBEC29xPBZJMDq4ZmGZT4y7HJxg3bUqjZiN92bXy2GCPl3NiyHyKKuA7B2oETsDZeU6Xy-Wtxk9ArYq_AXkVzDoHBD_3LTWn70W8krSG_pl86W53FCFOMxyuUS9Oy_HtkhLr8yRUTD1Vv7rff-ikPRtzPn67jrjo5U1xKmWrdZUI08L5OrhGKON9JOd7xCPJ-_j6vxUCvJkLjFofQDG2KQmBHQeZfkysB1YRjhiR8bA2Ony0nEWw8TGLOxCHxQp_dEBsDcigIMzN70JN93opRuhci2dhvsmwXzKJAyzLb04ZD4U7292v_F1M0GU9G2FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105422" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105421">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857b23b6b5.mp4?token=ucLbjrfakyh0uY1xSScOdhv77jN-PmcIjYqdkrVQzp9FkHti2NAYqbfNRAxvR996Gi9yzCL2l-7HBb8q6krMajWbfJpiH9xHPKZm2qbTfC20hbHOUbaLSzslq4thbao93rauOKEeGQpXvKb5Kaltboe8UKw5GL7Gm5axOsJEvXlIiE7B2ZjAv0PAlutjPDJfxOApHFKVRafTqfaOaNNXqHGXoSXRL81OpFbASbDkaV4A9YT8Kw7OJj-_SEqEu40aUtlB83HGmKRCUeymEGVOZQTJDu_y1AjeY0obCmRg648YbZMD16_3gZ3-zULhRTXUvoh8cG4Hfma8df9hm-4w-wSd3RxUMFLGVekh4_vMi66865_fq8NN9kyn0wH7DJ4UTLAklIB9U1FhA3WJVeZ-lV43XBBxYHiGEiDNz9s87-o35G4P_GvcYonmsKnw-cv_4mIuFiPcgMz7OuKBUYe5k5S2xMsTB7GbjdnzaMQVBxxuYr2HWL589GkLkCqL1Z-hsUA5Nc0fFTYYb18G_MgeVPK0UDhdLnU6eToUAMfD7SYd1-8uzSwPl6mQwDs9OZkn1yDeSCbhgCY7PcFhnhFJNzBmniOYuF6lRTRg6pFywSoxKO5--V1hm_uvJsEQ4JR6F6aO4rURd0D8dRFYPny9LkjsQ6rOSBw6fFFDUv-zXVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857b23b6b5.mp4?token=ucLbjrfakyh0uY1xSScOdhv77jN-PmcIjYqdkrVQzp9FkHti2NAYqbfNRAxvR996Gi9yzCL2l-7HBb8q6krMajWbfJpiH9xHPKZm2qbTfC20hbHOUbaLSzslq4thbao93rauOKEeGQpXvKb5Kaltboe8UKw5GL7Gm5axOsJEvXlIiE7B2ZjAv0PAlutjPDJfxOApHFKVRafTqfaOaNNXqHGXoSXRL81OpFbASbDkaV4A9YT8Kw7OJj-_SEqEu40aUtlB83HGmKRCUeymEGVOZQTJDu_y1AjeY0obCmRg648YbZMD16_3gZ3-zULhRTXUvoh8cG4Hfma8df9hm-4w-wSd3RxUMFLGVekh4_vMi66865_fq8NN9kyn0wH7DJ4UTLAklIB9U1FhA3WJVeZ-lV43XBBxYHiGEiDNz9s87-o35G4P_GvcYonmsKnw-cv_4mIuFiPcgMz7OuKBUYe5k5S2xMsTB7GbjdnzaMQVBxxuYr2HWL589GkLkCqL1Z-hsUA5Nc0fFTYYb18G_MgeVPK0UDhdLnU6eToUAMfD7SYd1-8uzSwPl6mQwDs9OZkn1yDeSCbhgCY7PcFhnhFJNzBmniOYuF6lRTRg6pFywSoxKO5--V1hm_uvJsEQ4JR6F6aO4rURd0D8dRFYPny9LkjsQ6rOSBw6fFFDUv-zXVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
افشاگری همسر رشید‌مظاهری از شرایط این گلر شریف سابق استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105421" target="_blank">📅 12:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105420">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZE3hjDUnx6_dvZdVyaMLJm3X0eKodqmAMxEs5b2WuAD6wiJt2vCgzesJULWlGiuW4mQ3AF_hPPfOO8N0C8S2HHp--CvzsTNbAsN8t-FWzcSgDBKbN7mWiJjJ-ydQj37iCQVocQDa5hoUgMGJbE97NOFYdX_se3eQu70Ksn4UdBPUwIR3P3XGX1UBzu64OTdKrq0M59cAXLNqgq00rJ9mwpjjLYrQC9X67BUO7adgg5v_K5otc-NYXXIW8gzwQzUI54wxwaOHDNJUuB_T6LZ8MIprurQYP9bMKs62CCtoN7iUt80bopEiJkhJAWAeIqJQO0R1SkAqQx2-0RkWw2ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
✅
🇮🇷
پست اینستاگرامی مهدی تارتار سرمربی تیم فوتبال پرسپولیس پس از داربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105420" target="_blank">📅 12:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105419">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSQm6bEzzlVu1CNEzBZ84pQqbaeG8ScyUGTj4XdCB0JPd7z-A_iGveDb2nKSxWThXGPu9IpxIU1LztfXvRHe9zAAqnZ4kdtMQ7Sj_ZgbvZts1v0FDnABAnnspR1bKRUjwSCXIcQfgE5gZHYj_z3Y4WM5sIBEblB1fBIlUlINN2ivRGltLF1LAR8JhzzSsegtrz78zjnwlCOH3qscp2rWv4FpI6JMf7SzBcWyFv-8FYErlmduGHQH0auGlisovviSvCAqiZ3lsMQZEUfTAtm-TRBXQHeWcOr3lSj-EbQPWWHdqpP2ldQWy0P3nkQXTMx2QXvHmTXA92eEkx83qFhwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
اعتراض تند مدیررسانه‌ای باشگاه استقلال به عدم اخراج حسین‌کنعانی‌زادگان در دو صحنه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105419" target="_blank">📅 12:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105418">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
📹
🇮🇷
🇮🇷
نظر مارک کلاتنبرگ درباره صحنه جنجالی بازی دیشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105418" target="_blank">📅 12:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105417">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYD-oQlVqaV8x4ugevwR3kWbimSgLTNESu5AOJGScrOZMeczgiWaL9WgNUlTd1kNnisRtyZ2t98k_bLHJtZgc-Y3Bw030yOwJ-SAr9OCzxQ2OJA1QV2SUUYZkrmgJwKK8wCxnYEctGLBT8sW34pS1Js9X0dM-I2cpt7CpcWR5MmhTYn4AEFBTdvV10Csv9yRpHj5ySL1VlU9NyddlOBujv9_lECEmvVhAMc-IZ3CpxuAU9iL06r7lmWQYDbUV9FXyPCP0sUpvVqRTtb0Wh6icvg-Hh-Ejzzamkb80GKUXroCj2ahyKasTFXiJFjBFF6TnqaFjYjDKoN_uqGO6pTVcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
محمود خردبین اسطوره پرسپولیس و دخترانش درحال تماشای بازی دیروز دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105417" target="_blank">📅 11:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105416">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4fbd0e6c.mp4?token=qpLCmhD-I7eJbet44Pt2AF8Xfe9NCnZ8kT3w6w2s3Et8wQqBDDqwhJMu-k-xfBveIUIG6GyREhdyeB-Q1ASGslwgxhmXiiCMbo5axxfdem4XJ1qsXT4yZg2J5zuC6aUX69jjECkZRoRFhfxCu-5j3gnZTSmOnq6dXZIo5PoT8HdMDXg_IbhxUdX1hclGPmlkear6iAn_3LnXcmzTVYLEsAn01wDH2OoXiJG63q8crR47YtSLu3mlA76qyMjME3kI7VxRzHv443bg0okTyQktgTROpiUezOP-gscq73hJ8oHRy-69_uK1KRYsZ2uZutS1H4ucIC7yEVpZQZGoMCapSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4fbd0e6c.mp4?token=qpLCmhD-I7eJbet44Pt2AF8Xfe9NCnZ8kT3w6w2s3Et8wQqBDDqwhJMu-k-xfBveIUIG6GyREhdyeB-Q1ASGslwgxhmXiiCMbo5axxfdem4XJ1qsXT4yZg2J5zuC6aUX69jjECkZRoRFhfxCu-5j3gnZTSmOnq6dXZIo5PoT8HdMDXg_IbhxUdX1hclGPmlkear6iAn_3LnXcmzTVYLEsAn01wDH2OoXiJG63q8crR47YtSLu3mlA76qyMjME3kI7VxRzHv443bg0okTyQktgTROpiUezOP-gscq73hJ8oHRy-69_uK1KRYsZ2uZutS1H4ucIC7yEVpZQZGoMCapSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
داوود رفعتی: بنظرم داور دربی کوپال‌ناظمی بود اما چون تلویزیون رسمی پرسپولیس یک شب قبل از اعلام این داور رو معرفی کرد،‌ فدراسیون تصمیم به تغییر گرفت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105416" target="_blank">📅 11:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105415">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40e7ca6dd.mp4?token=HsU3y0RZ982xLVwFmOheoo8J2cFGRKJRIX8qDTaSCcmgtF7nykxpbz1Bp4P4eEzMhA_-AbmXNWfd7fw0XfmF4c28gubzuVG_9NG-z37cW6N5N6LQ7OR9fF198dnkrE4_3SLjpSJmH7JlfVCO-IWYYu6CrkTjw8oARL-nfbacobWEOfhCqL1hAj_t7asp22P3ST4igviF906mniOUulBp3n9NE5JVnbWMo8_e_aj6ZdyZSahebHlMuPzlGDseyRU4ZaS-94DPds__0a2AfFknorL2Pt9o5tR8v0_pCdHzgCb8p_RfN8RBnv3BonyF7GdPtuLMBdzCLE9yO-GLM9Q2Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40e7ca6dd.mp4?token=HsU3y0RZ982xLVwFmOheoo8J2cFGRKJRIX8qDTaSCcmgtF7nykxpbz1Bp4P4eEzMhA_-AbmXNWfd7fw0XfmF4c28gubzuVG_9NG-z37cW6N5N6LQ7OR9fF198dnkrE4_3SLjpSJmH7JlfVCO-IWYYu6CrkTjw8oARL-nfbacobWEOfhCqL1hAj_t7asp22P3ST4igviF906mniOUulBp3n9NE5JVnbWMo8_e_aj6ZdyZSahebHlMuPzlGDseyRU4ZaS-94DPds__0a2AfFknorL2Pt9o5tR8v0_pCdHzgCb8p_RfN8RBnv3BonyF7GdPtuLMBdzCLE9yO-GLM9Q2Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
هواداران اسنابروک حریف دیشب بایرن یه طرح قبل بازی زدن شبیه ترن‌هوایی که خیلی پشم ریزون و جالب بود. تیمشون هم در نهایت از جام‌حذفی کنار رفت
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105415" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da46dad11a.mp4?token=gC5rCDGEoHBENO0duaK0orZH_dRTBVWKodITyc0BTuxGcWdEUPQ5Jh9AAbUKhIhUXxdadMhbuovTb007KYDukS_3kLLGwUmpcb4XhEwZ04He1_zgDy50CcbJTuYrNfP9I33lKv-cMlW8ah2G6OvhqoaSU63l1tl7zodA6Tby65IgAHa4xtlBTdjC_uMK3xt4Q6u-YVMFxO5SftZnN6NpFaUDhvniSwNHcTyY0wNUFBBfASHBXyiHeyK76nayX05wbpjqpif_Xwip8se-5Mr_1ytN2Op-9fDDJLjIe1_yorjDzR3OUHT84k7SpQtAE9fCZ31beU6_GNle2VFrski5_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da46dad11a.mp4?token=gC5rCDGEoHBENO0duaK0orZH_dRTBVWKodITyc0BTuxGcWdEUPQ5Jh9AAbUKhIhUXxdadMhbuovTb007KYDukS_3kLLGwUmpcb4XhEwZ04He1_zgDy50CcbJTuYrNfP9I33lKv-cMlW8ah2G6OvhqoaSU63l1tl7zodA6Tby65IgAHa4xtlBTdjC_uMK3xt4Q6u-YVMFxO5SftZnN6NpFaUDhvniSwNHcTyY0wNUFBBfASHBXyiHeyK76nayX05wbpjqpif_Xwip8se-5Mr_1ytN2Op-9fDDJLjIe1_yorjDzR3OUHT84k7SpQtAE9fCZ31beU6_GNle2VFrski5_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی شدید ایگور سرگیف از تارتار بابت  تعویض شدنش در بازی مقابل استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105414" target="_blank">📅 10:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFRE4ZxsWk8o5n1WpW2JuZNyXYnya8aoiTbQmWuSpEj8ouTaTRMwDF_-469UykrTfRxzjeIlWIVTrwjnm7MtTkcv2-sTaoouS-kY94OWho3T5hemTo1K5cau1bwdBCq8Yu-J_93fw7HogEEgc2z21b_-n4i3azSG5G7ltEiM9_tiMpGB6jmcr4V8qtjH6jCLvjGHBCARSKV3aoyulYjt2ZKvRyydA22EVhi5jMxWtgVPlh8pG-gHNcpDEwRKk_jFEpQopvTu14_Pn3ASqdJ7J9Z2npuh4emTEFiLCDQz7knNQVkWgAoYpYIEtxvndeeT1mr3agqrHkRBizOAIUJLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
✅
قرارداد کارلوس کی‌روش با تیم‌ملی غنا پس از درخشش در جام‌جهانی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105413" target="_blank">📅 10:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105412">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jY5VL-EyeB3y-hatdZQAUyVdjpOTgGzh-Ie1ptt9X0FlVACS_9hSCl4BB-gozWBYeZxtGppS0XWOmwhi2kLTRB2hBiWuo4IqAbR-CgMfvuNSsTXHQadcxVNllgZTrqyhmA6TQWfSfl_ocNMi9KGHHOk9PFSZW4dMkyqDVsOaxUEpsWqGg4_Pjw6I2i2C1PkR4RtV3mYvgAmFdWHThsrIgGbaVLOkjVhP1PRj9A8FuyIzfqPVrmr1C_oQWhbWIjJYGBo-62EJ9ZTmU5JcBj1G5lkJbKOEd3Y7s8cfUBvwQt88ci4M3DyilqzYifeTXoSIYCKqMQkBzdWh1GXotSqxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنعانی‌زادگان کاپیتان پرسپولیس از صحنه مشکوک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/105412" target="_blank">📅 10:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4193fef239.mp4?token=cVm7Fz_XrI6t162JghhTwfNWW3ekOVWoy42n8wq0PI5jsgQbFQJTJXuf32OBYDrMVDlVaPTcolxg0Aw08whoW-Xmq6ZArApozOq4T26Mepl54yrEBGjo16fm6WqZQNbXJtqF51MYJL5XVr1s2iMs31MIXq-wkAIR93YmtxkqAtwXjlfB1vLjYUg1sT5IHxBSjtoxSAiuQaIHv9iKI_T44mZgqqoP1s2z4b7qNxCRP7t8FUafcmYsvof4ECVQyFGtMTCe_7g5gLfKn4ImlVW2n1Zf9o__ThtFQDIsZrP4xlpPD6FpeKlcib-bCBkX3JrLFw0aRr2zVksn1ioQG3NK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4193fef239.mp4?token=cVm7Fz_XrI6t162JghhTwfNWW3ekOVWoy42n8wq0PI5jsgQbFQJTJXuf32OBYDrMVDlVaPTcolxg0Aw08whoW-Xmq6ZArApozOq4T26Mepl54yrEBGjo16fm6WqZQNbXJtqF51MYJL5XVr1s2iMs31MIXq-wkAIR93YmtxkqAtwXjlfB1vLjYUg1sT5IHxBSjtoxSAiuQaIHv9iKI_T44mZgqqoP1s2z4b7qNxCRP7t8FUafcmYsvof4ECVQyFGtMTCe_7g5gLfKn4ImlVW2n1Zf9o__ThtFQDIsZrP4xlpPD6FpeKlcib-bCBkX3JrLFw0aRr2zVksn1ioQG3NK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/105411" target="_blank">📅 09:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92a23e71a.mp4?token=VzUrtpHiifboseSWtEmC5yI7zGVBq0hToZvi_0MciMKWAsQ9OxCuJY7y2xN6dN2qBZpdRq4hbHjexKUsEsTi64pMJv7O-I-5HJm5cgV30aJ8M0meA0AKScHkXunDJu4iLbzIctpeVwgu2sgcwuQZyQkPxIOg9VM3OeHbvbDZn7CLY_QA4VUKDegkMYFmXOxaMS9su9tMz3wuTYIdgF3CycjeiGnt1wa4DyBQCuYKa9KK58Qh2YHGR8WU7Iyd7xusOeSgue89WhN7tFtl0A7llJyKDW_HpVpIg9j9Qin4ZvG-DESYInYn4fqo36pA68HLPt8UCrpLi_WHDNcCQOmDTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92a23e71a.mp4?token=VzUrtpHiifboseSWtEmC5yI7zGVBq0hToZvi_0MciMKWAsQ9OxCuJY7y2xN6dN2qBZpdRq4hbHjexKUsEsTi64pMJv7O-I-5HJm5cgV30aJ8M0meA0AKScHkXunDJu4iLbzIctpeVwgu2sgcwuQZyQkPxIOg9VM3OeHbvbDZn7CLY_QA4VUKDegkMYFmXOxaMS9su9tMz3wuTYIdgF3CycjeiGnt1wa4DyBQCuYKa9KK58Qh2YHGR8WU7Iyd7xusOeSgue89WhN7tFtl0A7llJyKDW_HpVpIg9j9Qin4ZvG-DESYInYn4fqo36pA68HLPt8UCrpLi_WHDNcCQOmDTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
🇮🇷
🇮🇷
توصیف‌‌جالب عادل فردوسی‌پور از دربی جذاب و تماشایی پس از سال‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/105410" target="_blank">📅 09:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff9c433cb.mp4?token=UpqaGblbTTcw9e2Ox5byf9Dji_2iZ_Z6QPSSwWzu1N4KF02U2n2aPvnNMQ8j8JHMZ9Uivgqms1d0fv8jNw2yZtLWSaybZ52TOIlQlzwcyL03aJnPhvPbpM-sbUGmI1TmitEy9IBacwKokR3AVTUOkjGmJHgt7EDjDudMy_d-GCRaFLV3D6xQXNtgLdSnW7MJvtWTHARXzzY3Nb5b4YcrbmoqQkheMa-UTcBMIuRYvycKXnmEkHx28bEPepIRJ7lB63Srwclt8CXp_g8xC_cJn07Lra4UkXfYp6V2u61OvaYX8kMYybtgKBP62N0AUucjfaHb2simHvnusvGgKeeYvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff9c433cb.mp4?token=UpqaGblbTTcw9e2Ox5byf9Dji_2iZ_Z6QPSSwWzu1N4KF02U2n2aPvnNMQ8j8JHMZ9Uivgqms1d0fv8jNw2yZtLWSaybZ52TOIlQlzwcyL03aJnPhvPbpM-sbUGmI1TmitEy9IBacwKokR3AVTUOkjGmJHgt7EDjDudMy_d-GCRaFLV3D6xQXNtgLdSnW7MJvtWTHARXzzY3Nb5b4YcrbmoqQkheMa-UTcBMIuRYvycKXnmEkHx28bEPepIRJ7lB63Srwclt8CXp_g8xC_cJn07Lra4UkXfYp6V2u61OvaYX8kMYybtgKBP62N0AUucjfaHb2simHvnusvGgKeeYvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📹
🇮🇷
🇮🇷
نظر مارک کلاتنبرگ درباره صحنه جنجالی بازی دیشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/105409" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105408">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603e84d100.mp4?token=GzNpHN2MKwTmSY1_w_qqv0hrxROZLrLeWrSUfKwEs7MXF-v6uiXemXYDkIGcAsAP-MG9aZKJBKlBiLOYnjTcB0SOkepDsIeOpERLyguNwaeX9UrCpJp5e2Cdn33lEoCaxfBnPL9m41lyN-SXC2JGXEJFQb_SGSE77vlzYCdsqaH1bLl4ald57j1qxiEkPXDm_glmnhKBA4CSYnFnWUySoZoWTtDhTAqN-52NgjkdueHllY7UXxjwgNjS9sLo57gigYuMjv8UzXUjOgruNUkw_o-3po4i0uzi5FKFexBghZg9j6XFM3WSpN7-kk2KtWm4DjxKUpM6pkwaLqS0IgTCww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603e84d100.mp4?token=GzNpHN2MKwTmSY1_w_qqv0hrxROZLrLeWrSUfKwEs7MXF-v6uiXemXYDkIGcAsAP-MG9aZKJBKlBiLOYnjTcB0SOkepDsIeOpERLyguNwaeX9UrCpJp5e2Cdn33lEoCaxfBnPL9m41lyN-SXC2JGXEJFQb_SGSE77vlzYCdsqaH1bLl4ald57j1qxiEkPXDm_glmnhKBA4CSYnFnWUySoZoWTtDhTAqN-52NgjkdueHllY7UXxjwgNjS9sLo57gigYuMjv8UzXUjOgruNUkw_o-3po4i0uzi5FKFexBghZg9j6XFM3WSpN7-kk2KtWm4DjxKUpM6pkwaLqS0IgTCww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
👍
وریا غفوری: یاسر‌آسانی جدا از فوتبال خوبش یک انسان شریف هست و در ایام حضورش در ایران برای یک فرد کم‌بضاعت خونه خریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/105408" target="_blank">📅 08:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=cg1v1GMbUvtiDW-E5p9gum0Z0gaPjqN0Tzk6b3PAZZMRchzALcvSJP-smHJrlW9O5rfY5LORgfDvrJeD0aqBDswHWKIwtPhx7z5P75M-fdec_biXd6xry-Fa7FmDwDu1Q7sh_v2AlQysvMkqb3MRzRnbFItbMyJQ_z0bL5LIrhCb-qICLDmv7WefepljouVhGOg6d4qKvimIV4OKedWb6_hkz6oNaghngxW8i2gvINw694ku665EXd0YOWCPI3XMbQn52dvRgCa5x-HHOz7ghMrubLNuLPejfbBtgoAPJ9uIincb_gzwplR2US0U_ivwUJjtqy0uBP3Ru_qS7CtBJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=cg1v1GMbUvtiDW-E5p9gum0Z0gaPjqN0Tzk6b3PAZZMRchzALcvSJP-smHJrlW9O5rfY5LORgfDvrJeD0aqBDswHWKIwtPhx7z5P75M-fdec_biXd6xry-Fa7FmDwDu1Q7sh_v2AlQysvMkqb3MRzRnbFItbMyJQ_z0bL5LIrhCb-qICLDmv7WefepljouVhGOg6d4qKvimIV4OKedWb6_hkz6oNaghngxW8i2gvINw694ku665EXd0YOWCPI3XMbQn52dvRgCa5x-HHOz7ghMrubLNuLPejfbBtgoAPJ9uIincb_gzwplR2US0U_ivwUJjtqy0uBP3Ru_qS7CtBJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/105404" target="_blank">📅 00:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105403">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pvl2WsACVE7IdiYz_s56wjj6z_jmty4OsUg3XvcRp1Gt_FHZEyGMcs-h5kRJbngXs4sCELYptHeCmURZJIjvSV8bld6-u_HIpZselM4_vGESW80yB4Mrh-I2b4U2Rxm235uso6L4L7g27wQTsCu_tk3uFw_IL6wXd226hGBYJX1XPYL9gQX5n6YhJe_8X5_imG4LgSNfOQxqN0wEkfYhR6myBVr4mcUFBHzPSK48VYmT3NW16J0HDcdSL3OJZ3NKyXRwVDwgE_1H5n4xrMWvLVngB0z08RDbJBZVZbv3EXfBY3Z8pEF5OaLZpvaO3LuTmkpv9hVe30MDZpH7SrSgZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👍
فدراسیون فوتبال آرژانتین برنامه‌ریزی کرده که همه بازی‌های هفته آینده مسابقات مردان و زنان توی دقیقه ۱۰ برای یک دقیقه متوقف بشه تا تماشاچی‌ها و بازیکنا لیونل مسی رو تشویق کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/105403" target="_blank">📅 00:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105402">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e447de2235.mp4?token=HF4lQOb4rbiI0P4HmPnU5TVGTmS23o-ANq39DDWucKm9DlMUfxO8f21XmqxaD2R7TIazTG70xeY1_WYdu4DhSjzH9qmQr7F0OgjlfFp11pLGOlvB49xzgWGxzGRZlzcCxdnLrxkUwNSgYAh_UCz8VqCHtJyUNWgO5iUMYo_xMS6GCvaN9Tz_C-GKW4WAs19HIRtsWeYMaptgXB5bDhvG3fS9d0w77ATWaqQMlKpWyRRXrme3Z10b0Db4ZRHZJzaLR_aA65slYn07dGF9fDN2aUd4Bfe8Tsexgyc1Qw0NVlaD4xk0VQS_hFYXcowj0juM_oKAZcbl9LK3kcJjXEYnMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e447de2235.mp4?token=HF4lQOb4rbiI0P4HmPnU5TVGTmS23o-ANq39DDWucKm9DlMUfxO8f21XmqxaD2R7TIazTG70xeY1_WYdu4DhSjzH9qmQr7F0OgjlfFp11pLGOlvB49xzgWGxzGRZlzcCxdnLrxkUwNSgYAh_UCz8VqCHtJyUNWgO5iUMYo_xMS6GCvaN9Tz_C-GKW4WAs19HIRtsWeYMaptgXB5bDhvG3fS9d0w77ATWaqQMlKpWyRRXrme3Z10b0Db4ZRHZJzaLR_aA65slYn07dGF9fDN2aUd4Bfe8Tsexgyc1Qw0NVlaD4xk0VQS_hFYXcowj0juM_oKAZcbl9LK3kcJjXEYnMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
🇮🇷
تارتار: ارونوف؟ هیچکس از پرسپولیس بزرگتر نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/105402" target="_blank">📅 23:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105401">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
‼️
🇮🇷
❤️
کنعانی زادگان: از اول بازی استقلالی‌ها موز و سنگ به سمت ما پرتاب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/105401" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105400">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=SD6RBgTwERAX0Z-9G8IvUcC68qImSFwNk78GUtwRYtB6qCSgMItDvtlxU-nbSuJ8lr0-75o4SX7yhs8Uahcxos9ll9tnJRjrzYFcVcCF-diKeCZ2rWSVB4EeHDXwBH5yYcN6bPwvzH5aGcpSKfze660cPt5DBb-r4n9Pm2gHfSbPj_exiqM3zodJH0gsJjiXrSlg4BTQY7g5FkicsfXNR_xa7EzxiGOPhPxyseW_KvIF9KTk78Tlgvi6XXhC9Tb5tsJLnsMvdstXwm7HzwvwjO8jUOv9UxiiCgorxOVKq-pknrHucZRAyGJngXKWHb6ZRv7rM2Up7oAShfaVf76eKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=SD6RBgTwERAX0Z-9G8IvUcC68qImSFwNk78GUtwRYtB6qCSgMItDvtlxU-nbSuJ8lr0-75o4SX7yhs8Uahcxos9ll9tnJRjrzYFcVcCF-diKeCZ2rWSVB4EeHDXwBH5yYcN6bPwvzH5aGcpSKfze660cPt5DBb-r4n9Pm2gHfSbPj_exiqM3zodJH0gsJjiXrSlg4BTQY7g5FkicsfXNR_xa7EzxiGOPhPxyseW_KvIF9KTk78Tlgvi6XXhC9Tb5tsJLnsMvdstXwm7HzwvwjO8jUOv9UxiiCgorxOVKq-pknrHucZRAyGJngXKWHb6ZRv7rM2Up7oAShfaVf76eKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
📹
مارک‌کلاتنبرگ در لایو برنامه عادل فردوسی‌پور: موعود بنیادی‌فر باید حسین کنعانی‌زادگان را اخراج می‌کرد و این تنها اشتباه فاحش داور بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/105400" target="_blank">📅 22:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105399">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=kT--o-gLQ_Kz0rEbjHsVZ-BWYqnIB-4EHIYXiESYV4LQPtC6XZKQo-7mU_WneQS-f23B4ZJTgqhSWeuI613ZaL9tBJuXUtu5udNKi-pvwDU8LYI6U3FjfnRDYpw1QrfewovslzQarmB0zHyMGX1adlQsWpcj1n6fDgyr39qWlMZ6HZtYVf0kLt-BoTKrBoeQbpqAVNRhmgutTNmV4joCW5DMZxNoyJB4ugLeawwtrEJfGfIkODalhbxNJremIKtXcyd656kXjyleTsEWROLY6L6FWQn8s7wuXqpaEENjl_KkspumKG0L-Z_Ylmwm5LOqMRY7VT1_je_EDVhtTQkcAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=kT--o-gLQ_Kz0rEbjHsVZ-BWYqnIB-4EHIYXiESYV4LQPtC6XZKQo-7mU_WneQS-f23B4ZJTgqhSWeuI613ZaL9tBJuXUtu5udNKi-pvwDU8LYI6U3FjfnRDYpw1QrfewovslzQarmB0zHyMGX1adlQsWpcj1n6fDgyr39qWlMZ6HZtYVf0kLt-BoTKrBoeQbpqAVNRhmgutTNmV4joCW5DMZxNoyJB4ugLeawwtrEJfGfIkODalhbxNJremIKtXcyd656kXjyleTsEWROLY6L6FWQn8s7wuXqpaEENjl_KkspumKG0L-Z_Ylmwm5LOqMRY7VT1_je_EDVhtTQkcAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
💙
سهراب بختیاری زاده: فکر می‌کنم اگر آقا مهدی (تارتار) بازی را دوباره ببیند، نظرش عوض می‌شود.
🔵
اوت دستی یکی از راهکارهای ضربه زدن به حریف است ولی ما جزو تیم‌هایی هستیم که بازیکنی نداریم بتواند اوت دستی به آن صورت در باکس حریف بیندازد.
🔵
من بازیکنانم را تحسین می‌کنم چون دو بازی را در مدت زمانی کوتاهی انجام دادند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/105399" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105398">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=c8i41I8oUhHTt5CdO8IYI7BfLmWiinvb1f9HB9qFSJz57ednTb-_TlXcFqY-AppBJiMw3uwZlRDiOKCuhst0RSHxuzcEu1WThLvFSyNNDpOkfneBrQ8m3R0ulVbcPp3uIOe7XzmKLH1TuR3lkHpuElsAYnHSeDjuIZszE4JPPDTGLUBh4QvNjcqHILkHg1Su0KVLjFX40STFuESTioV0yMSuzIK9Ayvp6M1LyiH3RxXK8fUTbmXWgS0StGWC7VenCRUD9hGgdZm_XHzG7cD6s7f3tZNpKF7ZZ394nJWULBetqrDALwGWWrkAJmwQE8-5XWjOW03Ks_L1rHETIBxNkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=c8i41I8oUhHTt5CdO8IYI7BfLmWiinvb1f9HB9qFSJz57ednTb-_TlXcFqY-AppBJiMw3uwZlRDiOKCuhst0RSHxuzcEu1WThLvFSyNNDpOkfneBrQ8m3R0ulVbcPp3uIOe7XzmKLH1TuR3lkHpuElsAYnHSeDjuIZszE4JPPDTGLUBh4QvNjcqHILkHg1Su0KVLjFX40STFuESTioV0yMSuzIK9Ayvp6M1LyiH3RxXK8fUTbmXWgS0StGWC7VenCRUD9hGgdZm_XHzG7cD6s7f3tZNpKF7ZZ394nJWULBetqrDALwGWWrkAJmwQE8-5XWjOW03Ks_L1rHETIBxNkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری زاده: کسانی که بازی را دیدند، از این بازی لذت بردند و از دربی‌هایی بود که حاشیه به آن شکل نداشت.
🔵
در نیمه دوم ما تغییراتی دادیم، به دلیل اینکه در نیمه اول نظم بازی را در میانه زمین به حریف داده بودیم و این موضوع را رفع کردیم.
🔵
روی یک غافلگیری گل خوردیم ولی برگشتیم و این نکته مهمی است. می‌شد گل‌های دیگری هم بزنیم.
🔵
هیچوقت درباره داوری قضاوت نکرده‌ام ولی دو هفته است که اتفاقاتی رخ می‌دهد. در بازی با فولاد دو کارت زرد اشتباه به ما دادند و امروز هم فکر می‌کنم صحنه اسلامی، پنالتی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/105398" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105397">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1qXW94HTezN4qlggpqm6ipqVjm_OOHQciYpVAGilBwmvTBxIUjrwKsBsY9T9tNROVdiWDTUm7tiZg5FXQzmlRWx3tmEGm9Vg368CyaqKi88I0EXySup06LjyorY-TRCmb3aOIDGHiCGJbvDfSRaQ2kKCZBO-fGVDDZouG25kXVcTiJHAV8Ild8w4PiKOP0W66_fW5zyOV_kJwfjRFkSQWcqhYp8CijDrvmBhmQ2Z0lxPhyHf2uBf_l3Qg53DoflXI1mng0Rnz4R-ps4MEQQzpga7Pm04sDJKqF2z9ngkdFdNIX1rNtikgPAaCqiXT0CPF34KB_7y-C0BuY3zTrTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/105397" target="_blank">📅 22:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105396">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDN8ZtvhL_cfde3kjZm5An8yduDtK3jTF1ZEERiUTIs40jvc0DeHEUprq0u1qjFz22jSw3XRe9saEa-rs0cF-NM0_FiKoBr6V6ZiCwLVMR-Q9SePAlPD3rZM2ItkzQbBrwBxJ64ydxZ8IN1uXvC6cHxK99EwXKD9NToVMjvUOuOV1HXTK1QzNckQ5w9fgisd0cEcJlsiWcCQqYzCykvRSJhoIblsOy2AF1UzLU8Uqi_WQRKQghbn7_jImGo46AMcmVaJUPvMkE8YQTDJl4Y6wvkKfXAa6DuXrV_J5yFE9S-zPVxhiA-qPsAWryMKaKGi62gVuSDDHOu--PiuTrLWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/105396" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105395">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
‼️
⚠️
لحظه حمله کنعانی‌زادگان به عارف آقاسی که منجر به خونریزی گلوی مدافع استقلال شد و داور هم این صحنه را ندید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/105395" target="_blank">📅 22:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105394">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=J69g_potxa74eZYFXx8NruFQySVIwYMZJjLvw72Z5ArFEpEOPMGDn1qbT8SvSb1mIChaRUUzbcI0J32NoWwW1ebnKhSMB-1h-p2Xi_rsjltPPRj7y1ycyC_vziBfa9QTQPSFuI9AKPNPsH-pKKcwUbvpciNYfCuBfiZtxAavs6pCoaTi1tnTzj148_i16mkcRkzwwkfMqEWEAwwbomPQ6cr7_1PMxroezFTuxcY2kh3ZqST9vRJyu7Bt3-uvKi7T1s8KzNf7XhPzbu3Z3anUHYc280SjZPu6X3IqVrddjKPfxiYjTh3RmvZg0bjU99rOUPq9XioRXGXm56lA2w8kfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=J69g_potxa74eZYFXx8NruFQySVIwYMZJjLvw72Z5ArFEpEOPMGDn1qbT8SvSb1mIChaRUUzbcI0J32NoWwW1ebnKhSMB-1h-p2Xi_rsjltPPRj7y1ycyC_vziBfa9QTQPSFuI9AKPNPsH-pKKcwUbvpciNYfCuBfiZtxAavs6pCoaTi1tnTzj148_i16mkcRkzwwkfMqEWEAwwbomPQ6cr7_1PMxroezFTuxcY2kh3ZqST9vRJyu7Bt3-uvKi7T1s8KzNf7XhPzbu3Z3anUHYc280SjZPu6X3IqVrddjKPfxiYjTh3RmvZg0bjU99rOUPq9XioRXGXm56lA2w8kfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
❤️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/105394" target="_blank">📅 22:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105393">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
ترامپ: برای آغاز یک حمله ویرانگر دیگر به ایران آماده‌ایم که مدت کوتاهی خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/105393" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105392">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bamKowMVMQn-gcIv8pG8zx4jUyXf3pqRWoDVC3GQ5waO20s1pBUTdcHvoo91evG23oo2I7Cv_shGWwmHhkpH96pYLHzNHM-sxOLCoK6Vv00UigbUegQYJdnlMEfoM4gJB8OEeWlNnopS84RIUs8xMdlX62nTVayrHetluk-r8n-Q21kG7GutzN2JbGSUH4A_w1-fixFl6mI9HV4extJarlgYTMRy_DmPGm6iZTXwJoqQE59iElnpgBq9p9MlXDT3PpD2iRQoQmry2mOABXV0D8qvlowimmGljZNJgmKea0vtE3wN6GXcg4Q5e7GsVAVoYUwiNp8hgxU7mXzqrjKUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/105392" target="_blank">📅 22:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105391">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63becc7280.mp4?token=GvcmYupcn1SqIKAIn4UPrmsx5yjBe0aCchsg3rlSD9ozaHAVtjEaxJra2hBGkXZd2bQDSIcOKlRldHhIi8XDNYXJqxVXbmmpZE10_ZDU27vYSoq1BqVFvDSAIqVonepsMde8m6zf7E-2zOVnth99aJIPpVxzh7oMsEoGNzWacfx5Zr1m_4vxbNUxTwcGa-KgUz9Ob96cZSgJ7tnMnzWgIqmvUB2b17r7Ss2lJ23vPhywXmzk0NEC1uGuLEQ-wVSjCDcVPkaH1xqZsUnRVDcsdva738--gXzIsTQOJUn6KN-fWJKR39raneW1ujF4iVM41MfEsRVgixk1HKZZ2G7EtQvr6z0CECr-hupE8zfplR7r7m_siAAxwkP9BZ1xLBKTqAOoiZObsK4k_K_SgMivDUp-biVBhvr1Y7kvmyt1CYwc15MbtnRdP1s6zX4wlK4n1rO7Dm4e8dCLHnXplW3-p7HdtFPyCq1kXWu3h--91_mOEtQjsBwkuESAAIsJN9Pn_3p8gUKS74jZSerRrrFuQR7eNAxzM0gwrRouE_H9R85SsCvP_7Z3B9Fh09NwK4pmuxUs6nI8F7A7Vlgo7MHy70hq6aWK3Qlipq01FSOU9eg8iXyt4eyf1R0rjFSuLPHi0s0JAqGVS_QKfFH4UnxKjIZoCflstbsZNQBvVLo-fWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63becc7280.mp4?token=GvcmYupcn1SqIKAIn4UPrmsx5yjBe0aCchsg3rlSD9ozaHAVtjEaxJra2hBGkXZd2bQDSIcOKlRldHhIi8XDNYXJqxVXbmmpZE10_ZDU27vYSoq1BqVFvDSAIqVonepsMde8m6zf7E-2zOVnth99aJIPpVxzh7oMsEoGNzWacfx5Zr1m_4vxbNUxTwcGa-KgUz9Ob96cZSgJ7tnMnzWgIqmvUB2b17r7Ss2lJ23vPhywXmzk0NEC1uGuLEQ-wVSjCDcVPkaH1xqZsUnRVDcsdva738--gXzIsTQOJUn6KN-fWJKR39raneW1ujF4iVM41MfEsRVgixk1HKZZ2G7EtQvr6z0CECr-hupE8zfplR7r7m_siAAxwkP9BZ1xLBKTqAOoiZObsK4k_K_SgMivDUp-biVBhvr1Y7kvmyt1CYwc15MbtnRdP1s6zX4wlK4n1rO7Dm4e8dCLHnXplW3-p7HdtFPyCq1kXWu3h--91_mOEtQjsBwkuESAAIsJN9Pn_3p8gUKS74jZSerRrrFuQR7eNAxzM0gwrRouE_H9R85SsCvP_7Z3B9Fh09NwK4pmuxUs6nI8F7A7Vlgo7MHy70hq6aWK3Qlipq01FSOU9eg8iXyt4eyf1R0rjFSuLPHi0s0JAqGVS_QKfFH4UnxKjIZoCflstbsZNQBvVLo-fWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
📊
آنالیز گل پرسپولیس به استقلال در دربی که عدم یارگیری آبی‌پوشان مشهود است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/105391" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا: موقعیت های استقلال بیشتر بود و حق ما برد بود/ یکی از جذاب ترین دربی‌های چند سال اخیر را شاهد بود
سهراب تیم بسیار خوبی را جمع کرده است/ من به این تیم امیدوارم
داوری بازی؟ مهم این بود تماشاگران بازی خوبی دیدند و باید 3 امتیاز را می گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/105390" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105389">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKoOcj-AGbSmtVQB83hQuneIsISZOEQgtgS70-udxX03viy5BWtFHwgF-z7rL472bE-Iw2PTUDCTytFzgi5Cb0F3nLaZVYPZ3z-nxJRQ-O5lXkNWZYGtWEqkkIx-eDfXfsReAE_I2Qy5mRUu_RnMlviP2-Zz6iTHEuQgIksZO8hMK6Qwe_wEfAfvfobQqtYkH6mSoGF2oNaUCF54CkgHbHmM2X2ykziYZrQib-2CBu0E0ECfLLpT_pc8q4g61g6c73HyzmSbEEpsL8HpKG3PM1-oFHtH8qGEgtMxOYETa2yNjtaH_Yw6VewymPWqEyJ6bDFE0jpovoVjwILye35M0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آمار بازی استقلال - پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/105389" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!
باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج بازی‌های مربوطه ۳ بر صفر اعلام شود.
حالا باید دید سازمان لیگ با این شکایت جنجالی چه برخوردی خواهد کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/105388" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
خلاصه بازی استقلال یک پرسپولیس یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/105387" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105385">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRa0XgUC4G4QXx0YtSgwpJW_kn9f3Dot9kAiW9dRHBbpEwVYmN4bN6APyNemWLilhaPUIICfD53XC1OMYQpvn8fuDMGKbAGRjtt2dSH97--qGiVk5JEzw4Q2n7oBjpD-oRYNwar5Gt1Kxu53PxYhPzK6vC9wgxf1i5PIRkUEuUFsSx4MejsS0aNt_TFLZxGsY1Xpqb1TQJ6p2P91NThzIgjYuBTJqDFGBH7uz6tlotgbOLyektuI88vsLdTCRazUMYqcrlnfNiQsIdxbaYz1zAN2w2qnn8DKwuQRaWARz17B8Q2UZGa5l9JRe4DS-jL4U2CB3Xibgzgj_qFDsvgO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
جدول لیگ‌برتر پس از پایان بازی‌ دربی! پرسپولیس در دومین بازی بزرگ خودش هم با رقبای مستقیمش موفق به برتری نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/105385" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105384">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geNXkqzPOYVYAvb38Ph69ycHdt0wnO-ql-c0nItFGa38GdiWUnoRmEEozZaU7zHUYtJRZzHlPxUYCdWkLYmIob1y40tjue1MItRMl__yEH6OfO7htXxpAr7OPZ5hqaeEq-SooFCP30DRLVxnPXmVVQ35LNL9YFiHYfJ_u75SKWp7ULEjAi38AXVd2dfS9LPcxrTEpJkkuI6Qh7gxXKLchEFlG76bY3QfW6sNsxBUOQXXT0I1nvcuUtyA3MiKyJGyuLaJL3T7t9fLsqsvVjXd3fmK6cpGMJ8zK9TPUCAW9-TVUw9X88OwPNW63jCsRYg2c0Z59ha0G7LQVFQ3EqecCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌پنجم لیگ‌برتر فوتبال؛ ۹۰ دقیقه هیجانی و تماشایی در اصفهان بدون برنده؛ هواداران از دیدن بازی تارتتا و گواردیولا لذت بردند!
🇮🇷
پرسپولیس
😃
-
😃
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105384" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105383">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuZn5ORev9FfEUhG7y5FE2YtFGpPB9sVKcJdRhgPCFcL_7yASspsSUbrj166Q0V82SDXlgOMWpWSDBH9OtlF39JwYwS0RYyxD-yX_vnJxOeau0C0yoZQ9E3QLQg-kC77IZD7-txI72IdRzllAe2f6HBIc3Ki-htS5tL7dw4PfY0lnpPP--xDspLBvAwbskUvuGxoENxYF2cep4ItP8penKNPWOwNnmPck-rret91hNKhrEnlV7stoanspzGUhardq-veSUOm0l1g_QCQuwi8Drm-upwrpjeKabmhklm_4FnBzTL2kLLpk3YBozSvX4_yPK2_QNB1IVCUREkUA7xyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌پنجم لیگ‌برتر فوتبال؛ ۹۰ دقیقه هیجانی و تماشایی در اصفهان بدون برنده؛ هواداران از دیدن بازی تارتتا و گواردیولا لذت بردند!
🇮🇷
پرسپولیس
😃
-
😃
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/105383" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105382">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b714d173a5.mp4?token=XrJdxnG5i5MMQsTl8GVtmRLyRLzniMXoo4ppTKeTwqxLvt9v7CP0HzvRALj_G8LUYS6FT0bKN2zfc5QdgNRK3TL2QP5WZvkvkygVLQ3sYhaSzmX3m2HErT6RFY448yUAYivqzHvOOswCJaePcDK_iayn4vPGtqmNhv6Bq9MEdsK3ltwJLyuwUeVHf3iOFxr_563tsH0tAT65P2x2CoJ_H9To5lwykBoiyer54ZA9XkeSKKy8mN6bkGzzla_xgFb5pwRg9IBDWUxNDW8B2Jh_kU_ezD9Pm0Bl_2WlZNwTyx1xTHtpUfl110ryutkFpDGF-Sw1sRjlb72shIY_4ncPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b714d173a5.mp4?token=XrJdxnG5i5MMQsTl8GVtmRLyRLzniMXoo4ppTKeTwqxLvt9v7CP0HzvRALj_G8LUYS6FT0bKN2zfc5QdgNRK3TL2QP5WZvkvkygVLQ3sYhaSzmX3m2HErT6RFY448yUAYivqzHvOOswCJaePcDK_iayn4vPGtqmNhv6Bq9MEdsK3ltwJLyuwUeVHf3iOFxr_563tsH0tAT65P2x2CoJ_H9To5lwykBoiyer54ZA9XkeSKKy8mN6bkGzzla_xgFb5pwRg9IBDWUxNDW8B2Jh_kU_ezD9Pm0Bl_2WlZNwTyx1xTHtpUfl110ryutkFpDGF-Sw1sRjlb72shIY_4ncPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
صحنه ای که بازیکنان پرسپولیس اعتقاد به هند داشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105382" target="_blank">📅 21:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d553ea91ff.mp4?token=KHSJzIpkK9HHYi_viH5vQTEwTLa6EYobVgFipbB08fRnunfzEbH6OcU9MhUBK2Wn3JOgzWQMBNM6QqozY3x2_mCXqeWhCJ51J6yHBHsnl_yeahfpO_VWOkFNWwE0qwQMt9yVxUQvh5QKQgJ9XOOtlbsQBA-C87akCdP9UCXAqEeMUzj1twMtbYpcmXpRNPd1dR5XfhkdOpm0b2EegOLLFiV20hnfxRzUwnXjSJbUB3_r_m1ioxJoum3mOvzCpu6lruyvn4BXlyljruSbudSNT2mmh2rLefLUeTmgYWQomXP65foUgWASFnfMgtX5Jqhzy9QTh3Skp11zyAxKDpX6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d553ea91ff.mp4?token=KHSJzIpkK9HHYi_viH5vQTEwTLa6EYobVgFipbB08fRnunfzEbH6OcU9MhUBK2Wn3JOgzWQMBNM6QqozY3x2_mCXqeWhCJ51J6yHBHsnl_yeahfpO_VWOkFNWwE0qwQMt9yVxUQvh5QKQgJ9XOOtlbsQBA-C87akCdP9UCXAqEeMUzj1twMtbYpcmXpRNPd1dR5XfhkdOpm0b2EegOLLFiV20hnfxRzUwnXjSJbUB3_r_m1ioxJoum3mOvzCpu6lruyvn4BXlyljruSbudSNT2mmh2rLefLUeTmgYWQomXP65foUgWASFnfMgtX5Jqhzy9QTh3Skp11zyAxKDpX6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوت علیپور خطرناک به بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105381" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105380">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcBWAHBOVo2-QomORQivWiYpf2oiuNI_xSyoqofsjOVj19_ErO3jYWP7O3eP46fkRPrcy97RHv_4X-TmXpJz-hRBHwwwCCrRSXDk5q3JN9GBgcHgg_n17GHmIHj9ISTDWBcMwpRI1FQVNFNwmposU9OxMQJ3s2Nz0uf7oSfO7mvthV14c4Buc6FbKT28neaFCYn_lVjxac-g00OSdNKQcIpcgF3RtDZZdjWPSXzk0XdVtC9REFEi29BCQStPwuklSLgEOVkUcl4_d-eMFvj3ZiRgWvZQCRw2ABHUdTs_LpxUT2SH0xB-jsb57LlO-sgTfFNXm5yJ789j7PTprcHP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/105380" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105379">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3436b36eb0.mp4?token=bY4Fx-OMQBNt12FR6IzXqpRX4hR1aRFNMxk6BIlA7TDHVORjPr7-f7oOKwXO-qpUNtCk01PLTU0tPio7nudlR4jgpAhMmpnlbIuHwicAiCjDFOcUZOCE42QOp8xfb-7FxFt__7exUwofDY0FeM-FvRHkdRDhm_zQF_O3D-jXFjbh2bOCt7GkFugIIGjN82sejweA0c3hcwlJxAbx_QWg9W7lmAM0ZEEVt0DiqLqWIWytNwwdRXpIvQ4ZsBTq5BiUPMCdU21IV58J_1bkKzeAgXu5BRLiEfdHtkV8HYzTrxhpxg26ORl2ear4eU0HCgsFmTzXBwjCOHNrv0Ti_DL2sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3436b36eb0.mp4?token=bY4Fx-OMQBNt12FR6IzXqpRX4hR1aRFNMxk6BIlA7TDHVORjPr7-f7oOKwXO-qpUNtCk01PLTU0tPio7nudlR4jgpAhMmpnlbIuHwicAiCjDFOcUZOCE42QOp8xfb-7FxFt__7exUwofDY0FeM-FvRHkdRDhm_zQF_O3D-jXFjbh2bOCt7GkFugIIGjN82sejweA0c3hcwlJxAbx_QWg9W7lmAM0ZEEVt0DiqLqWIWytNwwdRXpIvQ4ZsBTq5BiUPMCdU21IV58J_1bkKzeAgXu5BRLiEfdHtkV8HYzTrxhpxg26ORl2ear4eU0HCgsFmTzXBwjCOHNrv0Ti_DL2sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول استقلال به پرسپولیس توسط آسانی(60)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105379" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105378">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آسانییییییی</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105378" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105377">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یاسرررررررر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105377" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105376">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">استقلال مساویووووو زددد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105376" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105375">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گلگلگگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105375" target="_blank">📅 20:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105374">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=hBA2Gzc7MPjczwijYqzwY0HF43kMhjThEL9t6vq9LC1YtDBsJLKLUNAcGqP-lITGQl-b35-Vy5A7Iir24yhZovbJsPGZmh5pO7DmZGXQ_Ba_-G8WBvQraGvZpXZ75_P7z9-y0f2JFvhJ6iYv50-MXRfmHOfLlIKe6MK3y3PbanERAJE8Lzsjgk_YDZTt77FpnTAXxjrXmBV2UcCWUa6EisX0VfSk0EtFXT6U5YoqvCSxl8K3_a_EaGEchAqlBImycdhdCTETgCgA3i7B1aumrP49dg0WHnGh0sLjzcqDv8_SEr3BGJgef1NJ3aEhvYDFjokgXjeY9-CjvrGXsep9fk0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=hBA2Gzc7MPjczwijYqzwY0HF43kMhjThEL9t6vq9LC1YtDBsJLKLUNAcGqP-lITGQl-b35-Vy5A7Iir24yhZovbJsPGZmh5pO7DmZGXQ_Ba_-G8WBvQraGvZpXZ75_P7z9-y0f2JFvhJ6iYv50-MXRfmHOfLlIKe6MK3y3PbanERAJE8Lzsjgk_YDZTt77FpnTAXxjrXmBV2UcCWUa6EisX0VfSk0EtFXT6U5YoqvCSxl8K3_a_EaGEchAqlBImycdhdCTETgCgA3i7B1aumrP49dg0WHnGh0sLjzcqDv8_SEr3BGJgef1NJ3aEhvYDFjokgXjeY9-CjvrGXsep9fk0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ضربه خطرناک آسانی به تیرک برخورد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/105374" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105373">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c2230f3b.mp4?token=VyqrDGWceSTuWKpD47kLp6VYn8Aq5KhuWmQj1IEpNsYyjiwv_8k4npf6Oc-Mikqq7ecHfKgp-Hbge3siXPf38Abpb_8g4Qo2sW8hUJQutaJztBBPjGZ2w85bxqpQCHmuAR_234ojHN9TnBqpicp00PyKjT1qrX5G3TNBB7Nze6OKneV2GOfd9OEik_KdFJiwDOqbQ2gMhbHQX4hjBJhQr1jfsyUuVaLKTKOFtWJYmHTZJreAj8g2_e3SfslOPb6S5OWy7CkSle3zfc4i0_w5Dg6Z0cWb7oVf3vCucYxnkXjq34HQURrQP0fqUpICg2SYOqEN7YbDkYc9ZALuSWps2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c2230f3b.mp4?token=VyqrDGWceSTuWKpD47kLp6VYn8Aq5KhuWmQj1IEpNsYyjiwv_8k4npf6Oc-Mikqq7ecHfKgp-Hbge3siXPf38Abpb_8g4Qo2sW8hUJQutaJztBBPjGZ2w85bxqpQCHmuAR_234ojHN9TnBqpicp00PyKjT1qrX5G3TNBB7Nze6OKneV2GOfd9OEik_KdFJiwDOqbQ2gMhbHQX4hjBJhQr1jfsyUuVaLKTKOFtWJYmHTZJreAj8g2_e3SfslOPb6S5OWy7CkSle3zfc4i0_w5Dg6Z0cWb7oVf3vCucYxnkXjq34HQURrQP0fqUpICg2SYOqEN7YbDkYc9ZALuSWps2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول پرسپولیس به استقلال توسط محمدمهدی محبی 50
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105373" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105372">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پرسپولیس زدددذذذذدذدد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105372" target="_blank">📅 20:42 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
