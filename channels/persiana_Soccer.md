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
<img src="https://cdn4.telesco.pe/file/eAMM251mj5LMAALZBfm-wmOw5is_4zCHZ1PNoWF-c-vVXgcL7FJK2TqZsp3wldmUyXvwNe9fHe667qRniCRH0Ns69WmXEz68RSt0tlg85qSFf0InW7UAs_HNIBHijI4QUZND3Ge12EGgrnzoPyRKoqyuFmQlfb4xNXwsBnO6CPi_BaWB8IIgAJ_S9amNxPRajwh746A5l1ytvsgf0CQ55t_wq5XoMAzFP1MOPWOQYjOeaKVr8H6yyImwF-60byhiYU2M2sRUECAZp0LjoaUZFYVdQNwosPnnbDja3u1yOtN3BQYxaxQfF5HAwYIJTD-RvsaXUayztZfjB5i3wn8Qig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 612K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-29043">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBfNwwWchQVLp9ccFmTh5sj-n4FNMUryzoRTEb0WMn6rm-Kmjg8auEhJdFn6-_Z_rOCpGpk3WT89-UY9511y-SAN1M7wA2faGyKa9wC6nxLfW733jAOFo_xT10opoYRqaJI9VLVsXQLjfsO9w4w54j0awC3uMD8vMamZc4B5byw44qm8DyQm4B9516_S5lpfB_UaI7MMkAEf42gpQdDP1bE9hZDSSTJWpCVpv9B_-R5UKUqfRQFOkAoEhszj_3DZN9TAWy_0ms1CD55ZkLQwphlrBOoSG90XKwkjK5KzwgcBAmIONsY6ImFxWdVzHuqqPQB4Y9Rk2LTOLQXRP_dHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نظرسازمان‌لیگ‌عوض شد؛ دیدارهای هفته هفتم لیگ برتر براساس تاریخ قبلی در روزهای 19 و 20 و 21 شهریورماه برگزار خواهد شد. پیش‌تر اعلام شده بود به‌خاطر بازی‌های آسیایی تیم امید دیدارهای این هفته رقابت های لیگ برتر به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/persiana_Soccer/29043" target="_blank">📅 16:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29042">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/29042" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29041">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep8dSMgq7bvHi4fUu_8KOfajXjY70OYKxOojRC5ObcriY4wGAbUf3jYaO-mWiDGTxd3Om_iphAc1k1vIsGcQQZwLcbzBS1iZYOy_nAZP8i48oi93fx3MPSYXL65vhb3txdRXV0_Js7NeRUnZrvV9oZxjCH0ktjcZGJErqRHSRDYsvrya2RSUhmvZDQuumkWiMY30FV0niwgE04Vd9CXrbluRtWP5-4s9JFtx-dIgZv1Gu4poOKhPym0vVqOmWcSv0I1pK32Hm2llnenQWcONKX36GW4RQdWaUWkUG3EFFRiKYN0xXpU7X2wJqOxy39o8njP6nf3FUiKJqGX7IEaz9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/persiana_Soccer/29041" target="_blank">📅 16:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29040">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyARmuUmnRPduzk82QjwF5ZuepkbW_veqmdwgJLUyqxLbt9Y0thpkqoWJd3bwN3BF_NY_NCgNE2j9FbFgeXfQcZma-MlpUS3tDhT__ExqP9IRnDMYR_tVNO4bhhrT8nsE6-7Hgkm_BHhyWG10BFdkU7pBkvXIvBmDoRsBAmRCsJoaqTwVHnRg2rNbiwitYy1HZqFj5bXfz-O2gwfJpgZ0sbQTZfXS6nxmfIfz-ZbaZEw-fuhgOdHMqevqhp90rFL9NYTAe-UkpbmjCkbATv4YgE50MryS6pGjQZloXOBfbjafMXR2cNNe_Cy8JTrsA-k59Q-yQxMY1rhxvO0IGe1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته ششم رقابت های لیگ برتر؛ بازیایه‌هفته‌بخاطربازی‌های تیم امید به تعویق میفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/29040" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29039">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iBQZ1yFiC6OrPmNpEc-27vjw6YCXH0giiN2snEl1jCQndNIQVP11IVhMSgQ066vLAxEtQnqNgVPFJp6wWv40JgJuz56mnBsv8-OEkcJhua8usUSAYSpITdDB7AAZKBcnhfvQuGEGoLlgpym5157GnIcTmLcN66sgvkHWVB4CuuzPFAjnU6F_joTPZSDyoc49UvvOOMyhO5US_75e0S5pb__7p99570Z0X_m050iQKpJ2u1bhfCDtCQh2VHpknz_EoMdgGccHJVygw1apk-G0Ce9loja5a6LA6fFsDE9bLlDem0iOKGYjtR7t6NrIDikbnQRHuKmKTUzZmYkfVtWyuXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iBQZ1yFiC6OrPmNpEc-27vjw6YCXH0giiN2snEl1jCQndNIQVP11IVhMSgQ066vLAxEtQnqNgVPFJp6wWv40JgJuz56mnBsv8-OEkcJhua8usUSAYSpITdDB7AAZKBcnhfvQuGEGoLlgpym5157GnIcTmLcN66sgvkHWVB4CuuzPFAjnU6F_joTPZSDyoc49UvvOOMyhO5US_75e0S5pb__7p99570Z0X_m050iQKpJ2u1bhfCDtCQh2VHpknz_EoMdgGccHJVygw1apk-G0Ce9loja5a6LA6fFsDE9bLlDem0iOKGYjtR7t6NrIDikbnQRHuKmKTUzZmYkfVtWyuXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نکات‌طلایی‌درباره‌قطعات‌مهم‌خودرو؛
این پست رو یجایی سیو کنید، رعایت کنید که هزینه الکی رو دستتون نشینه و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/29039" target="_blank">📅 15:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29038">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyQi5g2en-5YeMIbJupz-d8r2bqeYEenNHRQqHxowg36bzIeSqylqONBrRci9p1x5iO6XFL_U2cY4YNI1gaDYTPiLRxd117lW3qlmkbDmrbXr4jxy3hyosHN770_f7iKc_61AD7G1J5igQs3yS9vw9lf5enTDtINw8Inbw3ZKKXSTV5Odm_aOyT7ee4YHGk8p5EJwUIGeaj5m3tgU6jkd4FrApdO8PX4qqzxjDjAPtBeyF7UNCN11hgTOo-q_RTcaW2xIQYUd_c36s5obJpkiFv1mpJLt7cQ1GZO4-nKCUAk2EXYenRlhr_HxtB3nO4w7B-BMejLpzakfrKOJe6d6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس قرارداد زینب عباس‌ پور مدافع میانی جوان تیم بانوان خود را تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/29038" target="_blank">📅 15:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29036">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A_lA-Zn5sqV7IYcfwB4TdaN3Ozx7AuJ1ArcG2UkRwGHjoN4t_ZgR0nVyGp8Se8hQAEBW2AuZ2nfWqiEeL7u8uBG3WCjMVOEg2tq1oNip85BymObDsKKCKyCQCIMTVqBfsUR9--CT9MTI7OntHu8pFHf1z6egfn16DAotCq4HNL21H0HOJ9zk1AiAVuGCn2XiztCktIakkmufCiSwkXAIQ_hM-9vyaE2BMZNbXj1G8-ewhAouzIu23vQbq0CuC-Yr3c12fhq9igyXcnubcT9Fk_sNOB-VHhrSca26miLwDxIHJYEhbWpkMuk2Kz3v3htQIDpZ-EaHycCtuIZA3WJ3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7lFCTDZGn1AlS5287jxg69w5vaM2gySPSuwQ9-JIp3-JVpy41GQ8xhX7r6HzM3oWFiGxJfh3lududPyckgotr4A5lnMxLabrjzA40azcp16mLCw8B4yoxqf3dD5mZZD0ul2uY1hR3cIb32XvRrMMG9jkrWVpaVfVvIixnF9VJ-Uo6btSXeyUEdj0UnKZ7ssM84X7TmtrPANXdZS_MUNT8eQqkXr62ALUq4k17wtvh3enH2R8cRhHNwaaJzhFUaqCTOvG91t2Z6gFPBqrlvQFciVEtp6JVkgIhFqzZmthsgwTp2iv3C43MBKrpMh6Nt2waOlVDPSMYV77ccMqBHO3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/29036" target="_blank">📅 14:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29035">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ2LIn69vcffIXouL6s7DE95xdJe3hyhtgJSyGWYBjzh_ROgrbv_23FUNs-4mxx8KlIp681L9ot8YTMhRev-f891K6M5C6lJgUlA0QddO7ZptRS6xwoFqRw2jezHKNkfW9kFAvNzRg0-Sl7H6YM1uNK8QP9vyY-pVHIHi_ma9sOs6kIPajUNyiJH2uh54lypkuZ7AU3J3Kn-azxEVPCMy0nE5O-dGRQzD0Nwqw4bPx2YzoZVgtCg6bMhrjBgeo0RJeg93EUtZd9yjI4TUf7n3Wgfis5KqCfiN7Bc75fvAk0Hrf-SEH8PuXp7SuEpIHYBkSr47PAv0HLEfs5berioBu9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQ2LIn69vcffIXouL6s7DE95xdJe3hyhtgJSyGWYBjzh_ROgrbv_23FUNs-4mxx8KlIp681L9ot8YTMhRev-f891K6M5C6lJgUlA0QddO7ZptRS6xwoFqRw2jezHKNkfW9kFAvNzRg0-Sl7H6YM1uNK8QP9vyY-pVHIHi_ma9sOs6kIPajUNyiJH2uh54lypkuZ7AU3J3Kn-azxEVPCMy0nE5O-dGRQzD0Nwqw4bPx2YzoZVgtCg6bMhrjBgeo0RJeg93EUtZd9yjI4TUf7n3Wgfis5KqCfiN7Bc75fvAk0Hrf-SEH8PuXp7SuEpIHYBkSr47PAv0HLEfs5berioBu9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لبخونی‌صحنه‌جنجالی شهرآورد 107 پایتخت؛
کاپیتان تیم پرسپولیس غیر مستقیم به سامان فلاح میگه من کاری میکنم به تیم ملی دعوت نشی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/29035" target="_blank">📅 14:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29033">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCjbZIiJq4XKSdJtN9nYP_V8DxKQw0DYSyCQ_wdEZDB-BocfCnkjPuZbbcWFNolOH_FNJv0jnRCCmQAIPpeM2i3olmOrSi9KdzWrnKgZqYkvdDkIE-FXgC-qtYQmre_43ik7WmbCGP84mn1NXEcKa0apq36zAkZmKKVqrTWabWk7GrSE-MIZWg41t9m0wLDCViuNuHguuWPJiLohSFMgNw4UwWr03oMzAjgZ_GuKhdQmVMaMbjJSN2_8ZOxUk4fG5lDrq2b7r1hzmjFSIs3MT31_W387JqLSTFF14noXtpUY6CMKS3_4VhJNN8OZz6BULvxDmFZB536DDtjWblGMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_2ZACWubCK1ABG6YSO6C3kIJ6Z7UBHl9K_1zYk_fwJD0a3cAP3RE6INdyTAwHtWhEbk2tHRWQdQlSBdv25XNAqbi5Wv6cfc9hqRpGYxLlkWC5XUOmAzxWbuzez9_jSu5AN4lsJ-6o1CiognjLEg1k24x0mXjaPAS8tLTfkTSa7FysncPcpahpS6SFJAuJWLZ-TWU0ISVLWt-GAX-oPY5HmPSdOzptMu6SE-fdVFtTVmHfAhoKTVoL9Z9VoWTDYWYuic8S3OY4lcL9B4k0i2WB4qVc6yPqrWfly-u_CBJ776cQZNc7xw7aDq2oDP8OinQ07aiGu5p_7_40A_q2xkzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/29033" target="_blank">📅 13:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29032">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUw2drwT1RHECqMbQ2Or5zKiCcU9uaDetsYTkIgNF6CCPmF3dwIUEIbD5p4uZYa2ILZZlk3_rgyOofn_-G6hOv7gVEgYrLd1ljq4mxy9ahrQzuFqK040T2zs5wmrDhS3IxipjNRGE_TYxPJ58CqxuG5f33cZXlAfMAgzEykfuhxSjejEHCl5zUA0TkF5OESEwymaSovcLobaG1Pasbp7YjGp3vv0bGlMSc_dDxEp_OF6krgpYIwvegc2VX-prCD8TKPa8mOLXOij7DioAuCqWr3p9Au_jRihb9-ntKnS_NDNSz5fABZknRN0MEimFaaSkhUXH67FnvN_Pi-jwJZyJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
دیگو سیمئونه سرمربی‌‌اتلتیکو مادرید:
3 بار درآستانه گرفتن کاپ‌قهرمانی چمپیونزلیگ پیش رفتم اما هربار کریس رونالدو اونارو از من گرفت. قطعا اگه رونالدو نمیبود من الان سه قهرمانی UCL داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/29032" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29031">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=VBZchwcwitj4fYIIDJNvSF0b2NZoJs70g9r4gdLwMWZQBnTswjqEX5fKwOykd9IQbzyCtKJBhVRwQ8eK301Vis1ZJPGB-D3Go6OUHzhXja4Qze0WKWpwgruOPy0GVULqyzKFOGgF3j3veYYyElx2ZZDEUSR42kTPqn23p4j7K1HcJnl2YPLRYOr-AL_HkZbN4NRLv6UXOddCSfEAAnA3qu6E1ZLh2D4jX0GoqzpTOK38n-PGtPgJqFqzy9zvdUF5dD9XU-iKBEVBkyOfS0OCZlGL2YZqNHbviF6vvyz4rGJiXFow6cB4BAl0JykRbTYQzDSdA0gc2UWJhCPpAD-NvUCfhKjuPNLojPuNTeetAJOpxwKLhJq6_mbiXcTju8BIexLmakOhuv_PwfHzlU_io_qhcfwb0M7SiAd1VmgOjpAUcWgEcicepNGDSpUrw0JvfxH6zDammLcE0UGJqp40N7liKdRydz3luaVfEYX-V3TuBFxyh5vTpkcfrQqmU2hKmlFX7cMEUNuw8QV9TDDpVj5M165iO0SQwgFiyf0ZZgCPthdEalJx55THnjzpIQyFcZEv6pT7fOdInwUfts7k7n7XBEk6Gd53atFOGdkLI9iFWmgL9JT2OWXnRLOohiHylmlkJfrwvRenZohGSgPaHNIYCv5MSrqpwqrsvvok-wM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=VBZchwcwitj4fYIIDJNvSF0b2NZoJs70g9r4gdLwMWZQBnTswjqEX5fKwOykd9IQbzyCtKJBhVRwQ8eK301Vis1ZJPGB-D3Go6OUHzhXja4Qze0WKWpwgruOPy0GVULqyzKFOGgF3j3veYYyElx2ZZDEUSR42kTPqn23p4j7K1HcJnl2YPLRYOr-AL_HkZbN4NRLv6UXOddCSfEAAnA3qu6E1ZLh2D4jX0GoqzpTOK38n-PGtPgJqFqzy9zvdUF5dD9XU-iKBEVBkyOfS0OCZlGL2YZqNHbviF6vvyz4rGJiXFow6cB4BAl0JykRbTYQzDSdA0gc2UWJhCPpAD-NvUCfhKjuPNLojPuNTeetAJOpxwKLhJq6_mbiXcTju8BIexLmakOhuv_PwfHzlU_io_qhcfwb0M7SiAd1VmgOjpAUcWgEcicepNGDSpUrw0JvfxH6zDammLcE0UGJqp40N7liKdRydz3luaVfEYX-V3TuBFxyh5vTpkcfrQqmU2hKmlFX7cMEUNuw8QV9TDDpVj5M165iO0SQwgFiyf0ZZgCPthdEalJx55THnjzpIQyFcZEv6pT7fOdInwUfts7k7n7XBEk6Gd53atFOGdkLI9iFWmgL9JT2OWXnRLOohiHylmlkJfrwvRenZohGSgPaHNIYCv5MSrqpwqrsvvok-wM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/29031" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29030">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVvqGIyPNYXVfiOnU04ujdH0sSkNnxrwc4TAko8YL49vGLDLbn30ns8T6uLjts76CULWZ95fASCjBAZLZ_JsNIHVt6mflPh8dGCBHNQxAV2vyVX0THXcmHPIL-ggR6EDVycyB7clDTxvWzKAqnhQROxz5aFCYeJm8ZttHOum6B0O1DAzHNtPPPS0NGUA7HRqTwqsJhtY9BWF73S54mq5su5V0KiUS5q5Rh2aI1TdBJpxDRtyoUD4yJXleAOvafN1bHAp_xJ0Q6F802Vp_HaUcQVl23SNeh6wJORYkvWLRUbD97RBuwV2wPKikgxITPpsHC67VuvMaFFSnIR8bPkZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته ششم لالیگا اسپانیا
🇪🇸
رئال بتیس
🆚
رئال مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/29030" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29029">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmoHw41y142BNqCAhoVPPjvYldqtuXYlN9sg9tKsrpfM6xNV1JsKOdvHc9kpYNFkTWtT-q4dSz6JDTnTQBhKu_w3Rp-BO9mHbYQr_bGdKz78yDY_dM02vPlnKWh89wL1IByVnYktDMdcrJqIyKfRR_1RYKTqtKtvlcz_CIB1O0-lVZEyPM-BVyKI7AJ45Y65z7akAiochmbYvlMRmA20jAa2AGTewhweyrkJHq5knd_Rh33nIzubytc-9TtXXP4197mpk0Ve6cgFe7PRU5wrsK_gxqJKrVUa7fSlppSRaU-pY7jGdLLHG0q5JD1yrwwtOMA2UwWV1DENGGrTKDzMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
نشریه ESPN: احتمال اینکه لیونل مسی و لوئیز سوارز درپایان‌فصل‌جاری رقابت‌های‌لیگ MLS ازدنیای‌ فوتبال‌ خداحافظی کنند بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/29029" target="_blank">📅 13:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29027">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4wF2lm610y1IqhHx7EGxOPSp-JQXXTP-kjhV9itZa0YT3ku2eHnRJRNZAd31d-rU-S66-IzCY404EHbZ70KBOReHvMfqOKyfvYSBO1fwe88CI_KBXWOHPHcq6r7yM-YdqTm5-YanwqpjbwOVUvSUCWvS9Wzn3ZQFaG_TAVp5tfPsajn20dhtBdwsIOGN7Npa-9PPnsHNqG8yOgb763b5WBm94vFXhVA13zlnBnvHR92ZnJfS2t5sZRhGIpD0KY4qG6wtLxdmQBEsMHbErukaE0G5Kq3g7W7iu1Bq469vxmRgXx39NDeD_1HYbuLcMUoOEvSO7WTdde5i29AnA6V8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYG8SaSODOFWKM3pXOfgxoi6UF7xFoOxhT6boMbfaApzMAZZmY5BqTeybsXHLyQa6-ve4KeXdqwLgFgq_TlRaHt0bEocE6PvK660EHKTKdk4_pdd1OWg-qpMQsqn1oEgL5aXt2PuW0TL1t7n1BiYmM-KmUVuz3HIBSCW6LHVXsqvNZVWGQh2OGYc0rwy8en1Yp2QYLem93ZE1WT51MsigQZ_7iT9ysZc6HhrnqcyHrj5rQV_qYz_Z5eKiwkNfE1KmBvhZ939ZscUm3gjQU-cdpiy_CCnMKwCCQB53NYNJowbI64wD4ykFNA4RlRcEQO-gDRwa9gKh1EZtAS1bfAkDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/29027" target="_blank">📅 13:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29026">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJAEah9fswP1bysHox6BWzVIHf2F1rzTUQAO42IwJWNASNrngo2RsLAhWvHWyZHfMLB8o8E9aVOr6SAJ5w1fq2QaqzYv8RuUPXPwBh_RI6oyUI6xCipAVTbFvQVTT-N9UDFyqX7XgG237ERPtkE_PNs8iWiZGEQWvGd5QCKWeIraS-og0j4oKyo_ivbS52q69keCkecMeycI7zKogXDdeSfoE0IYq7FWv-6kxjnXEMMiAYpBsYBdwlMRESrxmA-QMHGqA6m5nFAwaAwpI_WxC5piK_embVRNcF2T0t7uNIt1_UwUG_EOd9LKqG5a3ETqDXJ8nrTqHYQyb8IsSs3fow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/29026" target="_blank">📅 12:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29025">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvSbFG-j0j5oDPLb_7qfQApLHbkH2QWDMvOQlvH1oAW4Kvt0aRmfhxit2Z7637vzcY8bL92SYrBy3yx-z1ruC-SnYyLRcWX1D6DWn_lRJ5KIxIYu4n1HtUiMn2RDttjFNI7GytHZDE05p-kjoAFJATnnqGVHAtwbBx8gZvVJMuOczxsCcWutxqmH1IW8mjNV7QJYuWWFD1q3naLUPJ0cmY1xqgoHSUFnOua3akB0RB5--eWMfq88NgrMdeT50PiEZqOhepTJ7hBijbGBtlOkNeZASNENFjz9YGY2GlGLH44CePjvO7Wt8IpNZ1C12zO9ImyNUf3LDEBs-QlejF7TOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/29025" target="_blank">📅 12:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29024">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIQfkx1ahLY1C9x0AgRbgi9pHY2GG5_6ywVGf05lqt6Z5c5PE0IYT3Q4PZ508gfj8ClG90HqjBdP3cIkjIRF_F2UCZCfzNaBjnYGt0B7P2wG_pP0uQMNH7DkR9CPJO-xuMAppDflRh5gzQ16K1mj7UyueXknWHJWutndyBpAFyzHemZG7jagkhDQxOLbVlnYEU2XQngUcrgCLZBOk-zMz3SiDpDAfbuTciDlO7jRu5odLUtjLuoIC6cGbAeW7--sv0OsgF05OmgLLzA4kCLC_ryriHoJhJUCPGIqsGmLk57p7mcvtNzmJzg-JZXGKCD3rtkUvAuuk0r7xtgAcqhrrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌نفری‌که ثابت کردند که هیچوقت برای شروع دیر نیست با حضور علی‌آقای دایی از ایران؛ اسطوره دوست داشتنی مردم ایران فوتبالش‌رو از 23 سالگی شروع کرد. ماهی رو هر وقت از آب بگیری تازست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29024" target="_blank">📅 11:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29023">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=UyEtn1-fMSd6mjc8V3bgk9ActBhiZjFPR2kgk-lu1f_hvviauZAyStwbXw02j2b427nkyiUALYSnNdwSZtzQZtzjAQ0BUFXjurZWpx2thRQvoEb6WqB9oS_peqoJODB41KWOji-v3QAmr_W-45HBmJEjIFrjkEpF-QROQFUn40EyHIzzz4QV4KP6C2ZiWhm4YJ3CUp6CG55GiTLfYAcm7OBFoawJMMPb5kjAWaRZ8frsSPaahzps6S716QkBGxA0_b7GdPYJaslt352jIsqHGFZdSw0ff5o5ifn4Ig4Rl2a5y6IfhbwFHswtw2SB2C-JSV55i8pRp8WjCnP281etew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=UyEtn1-fMSd6mjc8V3bgk9ActBhiZjFPR2kgk-lu1f_hvviauZAyStwbXw02j2b427nkyiUALYSnNdwSZtzQZtzjAQ0BUFXjurZWpx2thRQvoEb6WqB9oS_peqoJODB41KWOji-v3QAmr_W-45HBmJEjIFrjkEpF-QROQFUn40EyHIzzz4QV4KP6C2ZiWhm4YJ3CUp6CG55GiTLfYAcm7OBFoawJMMPb5kjAWaRZ8frsSPaahzps6S716QkBGxA0_b7GdPYJaslt352jIsqHGFZdSw0ff5o5ifn4Ig4Rl2a5y6IfhbwFHswtw2SB2C-JSV55i8pRp8WjCnP281etew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29023" target="_blank">📅 11:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29022">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">▶️
تمامی گل‌های هفته پنجم رقابت های لیگ برتر؛
دیدار هفته‌ششم مسابقات از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29022" target="_blank">📅 10:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29021">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0wctuF_4BLobvE3nYgFyYui8RTSB3SHGbI-XzrvkGcDpXKy2rsj0OaYTkZyLSPMLhH-n22DX3LBGYRfcW6kh0dLT2Kil39CGd-LK-b0NLUJT6x4_YB_YD4B-WGLbsZYI9qNEbbiUkrbKKvh3TmEFFqEgN37gaXb4YhK2RLKOfI_UioeeIHhCwNYdXaW_kEKsgYf3T6htSlwBYdp-WfV31FknUNfbthF-cwM_ebons4sXBJyQ33zfc9Kty0paf_MNrsLBQLiHgfm8zXonfZtIzs52JE49GtkfEmZb0tf9YkmcPDx1gKu1JKFLQCI7blmJqwAe5khRWVcnaY77cQNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های ما؛ باشگاه استقلال در نیم فصل تموم تلاشش روبکارمیبره تا رضایت نامه مهدی قایدی رو از النصربگیره و این‌بازیکن‌رو به استقلال برگردونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29021" target="_blank">📅 10:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29019">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oc_NnBwKd1xSUrbA2-e3r4IZDyu4mhZgIi755l_MyihcbUO8xFsEBSdWixnqmIJkhMsXlg6EBg3mqFMTxuD-L2KFrrQGq9YcLKKPxQbQ4N8hJZXs3-Qj1jhy7B_DvNAkAQfOcsSSeVqphHvWm1yG87Wnjcc7hNOYY67ROZsaag86WBWdVLK217_KzB6vcsRgVu_zLiM6PqnA0L_Mbq9H1bcCmzBCHoN36uw0VOVDCmBI-6OcWrUcj61-gjAhVnFZO_yNlRfgssiQZfQeE4g5_zmErUTZ8o5tM6Cz6iD8gcEx7NLxYFhDQ058SHQkGPqOubsxliH5F20HIACKlEYOmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFGtQMBGSea0mPE520BNUsr0f1D-DJiKesQbH7oeSgsKiOlhUr4RcOpPqEfKqi1-Qcf-ra88PTBUDJK718J8H0OMt3EJcOn-2x_SkmEojFushOLJPKytdbTKaKK2TzlpL8Qs_uzGgt9Kg4z2YvVRLXgO3UqyfUF-GjbTjx-4vj3x68Q1VYyjG6EJAmyyhGtg3YFYD3N8etmcI4utFR3Ao6t2ExTsQEiVbIfhKSdsRB-NWFNal_zCwdPxL66YMrKhp2ZD8g_f-XXM90oaVfHcqewXT6ChOlMyKIw3HqQIUxppXrJRq1qht750Flt4BdrhvNv8D3yZtJgdoAWGQKQTMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29019" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29018">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCsbln9JZljuriC1fvGJ5e9leZeAfE23abaJq5imW1wAr5Iu3R8PwQkF-ng3PtM_g90XwXOMbzvkSQ4QK-1ViaYsIA_qKeB29LCp8_6Yz6RSbgja016Y7pI7ybAXY6ZnXXFD8vrDeQCSXtAgtArfXroaJkI9TIStkmAadckPCPnuB7nhKrLk39puEMfOvpLohAP7yzoxv2AL1STf-a6v6Z12GFo6A3fO5xf0YeQWZY8u8QxeH_jj9hnkuWLPi-fouglHUG_BIgnxelwheuFo4_ckzVkrylKhtD3iYlkKT6BGU0UAY8B8KWgv4e3BEfXQeCsnfqytwii2DHIJWRVKiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیزری‌جدید‌وجنجالی‌ازسریال«مردسه‌هزار‌چهره» باکارگردانی مهران مدیری. مدیری درنقس عراقچی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29018" target="_blank">📅 09:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29017">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/piuOvl4xx9sgrVxhHxaXV3c0be0QzMmvEpa9QJsV8_q5RF4klPpwsv7Hz4te6JD_E514lLsR-9g4jQCTDR-FFavYN-BDWImenunefA5AJHfCEqDmy9oeHKvaH9n6m3wt0NGLSbn0CJ970ol1RteTvMtPc87Lt3KV6-ZJeghLdiJn8pzxI0XcBlCaSamHI43bizMa_Mz-BF-tluQhZbw3Y3uUBMLPU_c930GZ659RnQgSXpINSXOLbGbXSUaJ-h4KycUAnalrWvjV1SxUySf0ZolOeJEiZfeMBW7Lw5nf6XcjIEwKi3Tkz-gqHl_q9ce0Hnj4o5KAyHq_5K3UtKauxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
گابریل مارتینلی و همسرش بعدِعقد قرارداد رسمی با باشگاه الهلال عربستان؛ مارتینلی در الهلال سالانه 22 میلیون یورو دستمزد دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29017" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29016">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAANBJwmjl3ZLiOD5CnTUKZfuI5aCr0GpvOXhMRDEuFxKtS_NKKy-xFbU5rJ6I6XDcaA1qUPJelp_gyCsrfSA0Zoi408w480OTTbcHUiWkDWMaSSoBuq2HQ6-uOyVlR3abJSGEcLriFnsqejbjBf_XIHtS0B7JhnOG-WUitX8EG7hKVsiZMF8b11IJk3si8-Ptc-JKt1YBGSTFd1WsGca9FdoJ9_2weYsAavSxqTduXv0HSoo3ldfvJwtYgGqVofnK6nKhvqY-UECC-L3ZEa1q6odJsZ2YvimpDess6NrMm76t3wx6PstifKtIcWz_ls9YbYGLdF-EF34gENgTA93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار: من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29016" target="_blank">📅 09:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29015">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eta5UaH_KYObuA4g01Na9gUe0nX_Nbf097FIplVs6W3DG28fYPtBtfX5KnJZjDBXA6sUodISx4bmFyP97MwfSNU6wQJclo8_qawOnKRsCwCkMIjphtXqI0njlvJ4TZsNKclvVZ3XSQv34M9-UP7v0YPUkVzPfHSu4JOSaxIfN1n3LONmP1HxhjrBhjG0ffquoBkUOC6rCoE1_ex986BoNMNlTCKUvP5P1a2iIlCRW58LM5qpjcHCmsvyx4awlntJSkVoYyyMenl3w-_ZkdBhMg3YXN-xuEY-WQULrzcCLMTy6CXJAgeNTMK3lN3qulqBnrdBR4ZCJyGWqYO_Krdydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی دو تیم رئال مادرید
🆚
بارسلونا برای الکلاسیکو حساس دو تیم در روز سوم آبان ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29015" target="_blank">📅 09:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29013">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJhOMsRxXe5ZaKtZPFNrRzSwPfINFupFzaU1N9WjC2L4RAnqlE-Nkqe4U0Ln4NMdpXmYaUX6JOyStnnP7gTUKkMxFeREBroPsUoLmIv8nuSQdg8vRHSF-fnIVrSdQxXNpZnQh5V9-pqxsLkKG7LO9HVrV2PcMOxn5oS9otxRvpOLsbIqrliuaDPjkXzEIo5VcUYMBo2EjkzqMzhdldv3rZPw8hm35EKjHUpCfnH3ls_8eks2Snw66TtEaQMMbnqU4nGhy8N77jBQxVHcNBIW2e2-ASIzdntG-XslVZfnCVZ6UtTSjwktiMtQBTR4EeyTB09uMQ8hpHVcTF23mtyShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از دوئل‌شاگردان مورینیو و پیگرینی تاجدال‌لیورپولی‌ها باتیم تازه‌وارد پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29013" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29012">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSvSt_mEmelgeT7AQM9nq6qc_nHptmei-9z-thnakooqXF8e9jhwe8rm5MJbgi222zn3mJ4urQ52m-MWUp9my2K2vayy4wG48jo5h7uaItX0CokCMWxl7E2J2xaJ5Bl-xFBELZPJZUB-DbLJyKc3dvGRe1VkYMZhfSithIMAMRwm7GRrQo29_4fJGZJ4f4-p-hpJOKezTSgR0iwiKJWl8QLYE3QVKQWBlR6pDVORQBnSz-BCbQLjix_7DLTaZKFnT4kQvMDmuuleCi6qzeRlpq45GbGGjnlDvYSaMXlwLYgStYxzCLw2S1rnADBnetbS63_Qvvv_CmR83SreYYTe7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌ دیدارهای‌‌‌ دیروز؛
حذف یاران نیمار از جام حذفی و برد لخ‌پوزنان در حضور 64 دقیقه‌ای الهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29012" target="_blank">📅 01:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29011">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=j08A5DPmTMvSIdKjOLHe4oc5QJ_9SQHd0AoScowPEGqkGdJzOrLuZyVAid23uTQfehbuO1_UWwRKJdj3kLqYjqLhyZWu5ARpd9d4JzRZbN7IWoL_g_-10HAp4ubiSIi4kwmWxLwT5rxwnsxQ6Zr-zNMNCvjNdS1_3JC0c2ieH03-TBZLkjTxFmvDF-r8_ZrdgrBxAVWPCGsaG4gNTKXKvPSQ4YBLjXx1LsArZupn_PJLFKrG-b7R_Ezi-1QFJq6tWiHK6Vjo7VOkxbyPfk87O_Q_rDwFusuocnyjRlDSAo3Zuo3jN6HXthj1MA_ITC3Phgu7LLtl3FWwbw6YKodJXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfa115327.mp4?token=j08A5DPmTMvSIdKjOLHe4oc5QJ_9SQHd0AoScowPEGqkGdJzOrLuZyVAid23uTQfehbuO1_UWwRKJdj3kLqYjqLhyZWu5ARpd9d4JzRZbN7IWoL_g_-10HAp4ubiSIi4kwmWxLwT5rxwnsxQ6Zr-zNMNCvjNdS1_3JC0c2ieH03-TBZLkjTxFmvDF-r8_ZrdgrBxAVWPCGsaG4gNTKXKvPSQ4YBLjXx1LsArZupn_PJLFKrG-b7R_Ezi-1QFJq6tWiHK6Vjo7VOkxbyPfk87O_Q_rDwFusuocnyjRlDSAo3Zuo3jN6HXthj1MA_ITC3Phgu7LLtl3FWwbw6YKodJXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
ویدیویی جالب از آنالیز کامل و دقیق دو گل استقلال و پرسپولیس در شهرآورد 107 پایتخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29011" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29010">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJ5GoMrv__a25pJbkw-OVWPkdjL100UJR6knDRcXxR-qMNyqWkJAcbobQBC15JjGoNQS28GWE4ZT_pxTjvnszLMPVLWyDghQQ3D5cyAsldjBywPRSj8HKooMoHUKwYFjvp7XrIlUrcX5__q-zH5O2EMqzkbqqDUhlr_LemWbzNTNASBxk07h1jdDNsECgZls1tIZLfBrTC_Bg_iuYqzypS7ExdPF_LuMw4uu7OnkOTyaZ-ltlotjpscuhEB2DVe9XA2Or89bI1o0NSg8qvou46aiKutZpGoV8B_E6a_aB0HdwpnhYuJX4KlXv3jN6KRi3pQrxqar7I7ZmFMFm2AkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29010" target="_blank">📅 00:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29009">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQdJpBniN0FZ46cw--ZX8aKR92G7-gb226IKLKwJ6b0mhIeUjnamCfCHvDvcJ22o1sl8ec_GFHjCbVbfJReMRnpsFD6hZEzKtmeHkyNo6OfXF3bomXbSCBOUdFpbsUGqAtw9OYUahjGTF8QmYNfCLND5h2ZON8TvLqmHrvOoT2oZxXlgjMUZmbtR2_aZHf0YcZENpHowTVJiUcQr7Ug8EFX0ZUAgXgK0Fi-m8uTtj2k82rCTmT4jwgRxokQr_EU2XaQEX-S5GhRny5tvpI30yHRG7PvgYzaATv-KJYo6xaGPoqZnOsfPxaJNPHFXC-3bI2_VLXsNpK2jWZoiaAkHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29009" target="_blank">📅 00:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29008">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBcMnjuNWTuOBswHnFDa5medV_RtARpDVsJ3vT3a3BeEx59iBTRPJYJ3RFk-8kf4DgyymjBbSNOKaCKGmmjQdFk3AzVo5f_SITF_hTVYYowbjT0OJIA3kvUQv0gTgon9UTUV-CW8EX8hh_Pjhy3u8C1jMx_n9W-6kL4Hx9I5DxwOKJwFaKc3gxDPyg6uvT_tY7FLS4RJxw6owz5dCceIzOWgkvqipKBgeOjp3PFy7fCPdOCv7eeubzZ54900TtIItpOUxfK5Wfgk0f6FI_VQ6XZsNWufuOuM44_b0MUK-OkDpW7mXinW1taU8vdtV7NoV_f8bR7EYJ2L3gIUVSI0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
مجری‌ویژه‌برنامه‌چمپیونزلیگ شبکه TRT SPOR؛ که گفته امسال بارسا با فلیک قهرمان UCL میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29008" target="_blank">📅 23:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29007">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAASe2e0x4TeM1DfQzy6wwIwQl6gAsE4p34YhLlaRiWtnCp3M7x9NrAlgJOyMXLQUHI1cGGDXnjo37woQ0Ukj_-L9ty0kkuEqfhQSxsm82l-5DOADfzjPvIkH9rwJWRTBL3WhtbSW6ZJQJkcgo79xJWhE88-Y3uP6a2LBmM0GLl7s_AT9YgPDpBR29uc3JOG-97XIKBV4d1TUqa7QKTjXdRaBo6kS-LzBH-VxlCiLismPzE839TmML7WHS1tIK4mV7_qRvsN2pn4ixWVPHpSzNi_tPQixbOr_FSg6GqoYN40i3O4MFKnHZhIWmpyOo7vO2P1ErcA_vgiLh3QAo5xLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
بااعلام باشگاه بارسلونا برای نخستین بار در تاریخ خود به درآمدی معادل یک میلیارد یورو دست یافت. این میزان درآمد عمدتاً به دلیل افزایش درآمد حاصل از استادیوم است، باوجود اینکه تیم بارسلونا مجبور شده است تعدادی از بازی‌ها را در استادیوم یوهان کرایف و با ظرفیت کمتر برگزار کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29007" target="_blank">📅 23:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29006">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnMLQuTwr1HyG_z0pufQR1Z_0-L8dcgYvxbl3QzCXXXYV62QCzYLkkw723LvY017X4RjHydQJ7mazLsJ1dDr4o2vx8mK1FwA6Cd-41obqwDcGXJoXi19nv9j1LaibA3kMHQRqUObYmZtJOyIhEKMxI3znj4N9gJz8cjKa6iuS2NZpThsVivffEH0Yc6rHfZQfTkL6hYvWPOJdPhlKCUTfnSBFD6S_FSMU1klFWuIOmbLMFX-H1jewobDvl-pWQ1bdGKBrFERsm9oNBUH19L5H55lWPLuMhMKMTd7-hA_dGonAtuqS3Lu-bs21urmV3kLgvlZ9-DA-oVtsn0POJ9IZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29006" target="_blank">📅 23:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29005">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdtoMEyJKDKz8zGK0Ic8kYJXQ6ExirBw6g5l9ToxrSZ-Yyj6d_ECMvmr8R0YRn4YFed1kVtoNrEf3iy04o_EWW0RLuPscqxSTBL__o2vCFwTy5V_zAKFUPuCF9mRRaB56NHGjEVVOtOGtQl1Xx_dJ9rgLNbb9nyxm7Zdpvf9EqOZv6DA3absyaGMF7lvp72rYHODKDrNZ4olJLnQf9CAcKV_az-UDFozBk39JkmLI6WR0FsR_K_JwQDjLVifj3r3leX4ie6a4tUDwvB1T-UhlaWPYDTC7SQ9lNvsiD2rn6Pmvigk4aLNOA6sZs5HUR-6VBmmBqTlzIDJOWiR_r8Y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇾
👤
تیم فوتبال پافوس قبرس با هدایت ریکاردو ساپینتو امشب در بازی سوپر جام قبرس به مصاف اومونیا رفت و با برتری یک بر صفر قهرمان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29005" target="_blank">📅 22:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29004">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu1BTDXG1adSz-nYznnH1_v1GyaEnnGoCJuEDritxWBgfkbF4yK_OgxLTVqWyUh-_BuE8TfHgmbhJxBZmJRWDgkHBj4lYXiUNleQOMJsgLBlKD1hOyd2kyTmTx5xfnI9H5YYF582SvG8CZj1WTYlqW7GzhujbRonp29x5RIpzgSOYBhsFvCdwSXq-6BIhaQ1ICKyMK12XzUwcih47JR2ibcGTZQZqDxWCeiIrZTwsLV8V1jMl41HvAMey-aOBgPz93WbhZpaqmGKQvMd7yFFsrelMmKs10isl6D2k3g5YdE3eln1WsZIpX0bNo1Lg5ZmPt_AWZkh9q-Gg4R4QmnIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29004" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29002">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjEStrlKEyk8R8KOeu-Bh-vsSHGxJvURlw5nPgP_3-53BXZlgXB5xawAF4OUrC4MA9YXcCedlXImyse3PPlJQLN-olI5D_92u-YE9RLFAdZLb7Ib008WfXJWcaQTu5hGtJVBV1la7rir0qbFuma__Tjr30EHEhg17154HtppEKwzfKjE7Pzkt1l490CRScUMuxQycx5D5MIgpX9VMD8tFNVCBb9KLXIWKH1QSNAUE2oJzhTWCSch6wMMANHxS_6QAXqbGMDcNkdX2PNV8YHg4uvjih3-3bNlz4m2XRcWA-iHpN-wNtozXFpJmtQQhlS6yCZs4OfmHqJ0wBYkz47EwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOm3fwyzoMqJJQEnPB_BzVYHqupJDFg8npbbPWZuWnUSUTHkUbXEWG4Yc_QITZns5lwJvhE9CFKC7WGjxK_H0THHNXffsQZxhpHnryO5rf8OJwrEm0OA1rbYgEFlxVUAkD0WGWJNmIXydPvKxGBnKdXgiOtPQU5Ubhi1JaaSnKPrT-pgLHrDpMI8M8xDLQ9qKb6zJ7Wsh2Ma7t0dLIAJTF5IDHyze_yyWJwyPZiv25bd21wJHUe_0Ukb7hQTszjWqTlNrmz3AC3lMgsr_lcX9UNvHeLezoDjxOGHup3qD2aEweC5_WDHN_qhSeknXgt1-fnP-YS-X4OPYf8We5Y_LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29002" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29000">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuaPGjKFB4M_sw8yxnOFBHrhSLqkAX7HlDHybLZj-mVsxHUKs6_nlW4-HDhdWeYPOvI0b312SjSv__btpJTqrB8T9V08etdYuqAZdcP8zooIy-ThaOD5BOmwHq3AKZ0wVDJoFTuulfe_RX6EEbQ6ETuSWoghKS1T8sRoyAResV079oqNdExkngKxphGQfm_4vLjvWTPTo8pNigwTSwWW_YfuC9H79pSrqVqx45_W3S_ucI5r7cBxZG_fEdjsdb5VRElN3XZsv1jzQpLSxJt3ymtAIvbdPG_QzNNWtyIX8u6lc_TBuWgEVlkVVMdLuhqAE2Tpe3Xw5CirwkYFouaINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcMCu3uHB70y2L0tvn91bmvvy5-nODopTxgf-37Mz9lzngpPwlSW8zgFNpNASXFu1VsR0Yi8VxyJbNS7I82mKmDdbNfj0wtHDwKO0rJa9rp3bqgvwuVbY3bLpZz6Zq5O00S2weDL-WSTr1QfFHR1lsipcvkEEdjIsBuggSMjJkAKKPZLoOqISc1Hkh_WGtQPhNxLU8jqOHkSoizcpNFSbmjSaR8oF1_o8WB6BJ8We9Y4YNsspLmyto603Gfys75QW9vBdTJeNHz9_k3lZ5x7fDn_EXdtkZbO8w11XI6rcqfm8vp4OUQQMn79nwVPFN38j7M1OFxZhnphu1BkcyVm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه‌بدونید 3 باشگاه بنفیکا، منچستر سیتی و چلسی روی‌هم‌برای‌جذب انزو فرناندز ستاره تیم‌ملی‌آرژانتین 282 میلیون یورو هزینه کرده‌اند که خودش یه رکورد برگ ریزون و بزرگ حساب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29000" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28999">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYif14Joa5AoPIxmHzELZRv5-6pKBewleHguXpyyrWgJTp7OotqvtU97wEVsbqj3mTjp4lWh5PZpDHypToPOLd3KPjaMan79X47oGjKHHU_SmUI34p2fB-7GsslgYWLI8AQE3gi4Eyf0vSqPtZOqMcKFD9d4Ht-thbm1FwUEHlKA0KuvsHDEjmIFBwuuk_oDxRd0BvZQkjH6F67Ih6uvNZX5dt8DYd-sMu4Ty1CWlSVNZPZ1vwy8a_nf5diyQIhL6UrzHNkwUMRixUsDXBcR1hcIG-UWEiLQniqaFkXqPMQ7WZqYvVL2TqkcUoJnY17gqJOHo9feRaKzFdNu_2BTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درکمتر ازیک‌هفته‌باشگاه الهلال از گابریل مارتینلی و اولی واتکینز دو ستاره گرانقیمت و جدید خود رونمایی‌کرد. عربستانی‌ها روی هم 150 میلیون یورو برای جذب قطعی این دو نفر هزینه کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28999" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28997">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLxbWgRP4sUf-wLvGGgoaNh5k_qJgXFh7cLr8hBQnT5YPhaG8kTAtqIlrlTAdWT0n4oEPaojz_zWXzmIb9lFceAnBE5TL3i6Y9-r0kefYY6frwx8AgN45R36DPLHhLoFDiEJ8XDJE2sfMqU3q1SlvtpXlElLwMwuqA-hp8WWgqfTW6x97hhAoP0D4GiojXMVMV_BWDZRsGWetSMkUk8O2C1TUsXb4E_u8IlJgE2Cr-Zsy-WIlckXm0Eng1mMgi9zBHLWDH-JVxEOP6IWY-uFDz2EX1NDsiXn_txkGYKLrSgxO_-X3vkD28nV6POh8o_iiVOBRfd395iCOVix4q9X4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28997" target="_blank">📅 21:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28996">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma6Xh5phI4wbp8RE6CauJXqthu7ap6IzYF8O0oydeHXyDzlBl7nmxurf6RMch_olsnkawnUpt11Qxt0xh9OzaFxKwFqKQA1Am5Hm_4Yd4ZykwU7u9B5jNPeL_YBn-JNmj7yQAcchT6EsPpybqStyazqW0sueKI8kIhCDj54yfPByswJHbdH04mYTGNz-mQk7x3nWSuWljCC_JOSVhl_QXJDbEyCZoOedRwACCWmLdLU8y_JmfDf937eAAzUUwgK0Vd1NST_Lqcho6gmZPlITqUMEoupx0HPeZEOopzqD2Lp1vjlJHuebWeGuRp4nw8hfq8WlO7i9BpxM7NT1P0pwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28996" target="_blank">📅 21:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28995">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=f_D0X7VofrIn46WCjzT4Wj-d0Qw5t45v1-TITU1UZ3sL2awO5P10FhGfO3yTpLPQICiHtzbyGMrS0MWqNEGu0PhwGyTm66Vz2gAIdUETzjimxv8B0pOHDziYD5EA0mWcuZRMPnejQqAGo-GgS45JzSx11K3sKb-VGpH8P7PwEBjeaNBXXsE51G2-EyzJiWkoBGg7-btjNrEoIibY9mMbzbDsTQUHr1NoE594T9qGHLyppqCMEEylkEhrn2OTzWOOgVdvlSNm5vbwKwjLpLDP14ElsYljNwIlQt82LKSrXlNCGIMkYxPw2JKdoxrd9151u2We7sYuA2RR0P96Jdsygw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=f_D0X7VofrIn46WCjzT4Wj-d0Qw5t45v1-TITU1UZ3sL2awO5P10FhGfO3yTpLPQICiHtzbyGMrS0MWqNEGu0PhwGyTm66Vz2gAIdUETzjimxv8B0pOHDziYD5EA0mWcuZRMPnejQqAGo-GgS45JzSx11K3sKb-VGpH8P7PwEBjeaNBXXsE51G2-EyzJiWkoBGg7-btjNrEoIibY9mMbzbDsTQUHr1NoE594T9qGHLyppqCMEEylkEhrn2OTzWOOgVdvlSNm5vbwKwjLpLDP14ElsYljNwIlQt82LKSrXlNCGIMkYxPw2JKdoxrd9151u2We7sYuA2RR0P96Jdsygw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28995" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28993">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmDNqF7Pgo4bUCjBcu6ZpnAkS-uGowgXeHcEVkC0O0PZU4YzTqEeotI-hpKm0Ix6ZwNj1f8SAv804GOL28gOz-XUxAnd6Fts8ZWgR-hG0dPg-bvaeEVLyY9D47j4IDR4nWE9Jd1Hfnh2gr0S4qIKAFkzyqawFhQer_Sf3-_uUzST0ZLMRPISRj15X7IJiyrDiJhmuCa_zWMkEIVyFtihwZRTeidXF3RQsep9NXeVfeZySzwbCJ1Aka7RoMU6vivF-O9b32OJaqQNKB3H-sa6_WGEAaYRPOotbCotJblMGX-bMWDyIk5Ev55iU-i2KpwkjZ7VX2RdQskvWlqnjYlnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پوستر رسمی باشگاه الهلال برای اولی واتکینز ستاره انگلیسی جدید خود؛ قرارداد سه ساله امضا شده و سالانه 20 میلیون یورو دستمزد واتکینزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28993" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv29e3rxOdxXbGUcGMDDyGnUq5-siogELaVwPichUeHlie8u9TzTgjcIpMQTCZFCip31ppeZXmVJQmFwhcKvuDKgM7cH-cBy020TUKU956hnq7fjVmzxneorysPp0hh7d2DNuLOI-XP1kItkso0zuK4zTmJsSiKt_-ymly_7M7qGqWLMfWym8d5TQmNq8iN_hBBwxU1CLr14t8hqUBhybBVLijTf6mVEMsLkkZCyctcUtCITVWyQ8ptvzFBQXuboKAGc4ClMj3-FnJWR6I0yhG4JDbvUEAQe1-fk8x2ecjz1nI3GnwCvtpT840zZpIPuYL0rs8mPUTwTliJl0aSd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28992" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrAWnkv8lgf0mYidcS3bO2Wihovf3f0ygsBGyiZtkkpmwDioJupxagfrlTvVlnY2Ylibvk57MeIAE7hjBivATM6Uw_yZX6V1T_lTerf4MyMdjjSdHpAmc8xK3glOdhzj6GeYNIIveU5BakUCtI79jquL5WC-NRamV2c6elZ6HSascxwA9wcdnK9xph1j3R40eZSGmMChZyyKi2T2mghqWwJNIRosfcsnLHs3gAKBfj4tj41qps8ufGxb1Hr6n7fAWCXvPVjcdTnOLWlyD2KzSUDg4WH53vYs3ktVHQgulsOE4m05L021cvZsdzGQJnkei5luPs_PRNzwpIN5IeyKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌باشگاه الفاسي مراکش، کوین یامگا وینگر ۲۹ ساله فرانسوی‌سابق‌استقلال به تیم کنگ آن هانوی ویتنام منتقل‌شد! کنگ‌آن هانوی فصل گذشته قهرمان لیگ ویتنام شد و با پیروزی در دیدار پلی‌آف مجوز حضور در
لیگ نخبگان آسیا
را دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28991" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇦🇷
ادای‌احترام‌فوتبال‌آرژانتین‌به‌مسی تو دقیقه 10
🤩
بعدازخدافظی لئو مسی از بازی‌های ملی، قرار شد تو همه بازی‌ها‌ی زیرنظرفدراسیون آرژانتین، بازی‌ها تو دقیقه 10 یک‌دقیقه‌متوقف بشن تا مسی تشویق بشه. اولین بازی، دقیقه 10 ولز سارسفیلد و بوکا جونیورز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28990" target="_blank">📅 19:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfba1QgNrWAI0R2wWvYJyOndQrfmUPetV5Pq5yGmtaE5O-g3Ow-BmBZOfKD6-_0RN2Og1vyz0Mc_jx_fyLeF_S9FoQfWhNlLOP1mjf8nuKBxX90GF-xFnZ4He489VAMpG0P66yPGftAg0r6IRCrg_hnKOWf9IoWKrL1tk0Hrr-1pXOtdQ-UDxxkBmiopWgW-UKq6Ea8a9SjIEBBuqfCes5JVsuWoe7Me5FIlztReB7gCWSxNHGW0ZzmmAkmgsVzs4vW72n6z7GRImUX4mu1a_xU2yhEaHgu0PwoI4CvlqujeP-td2HZOxQTGjMedGxuNEyy-gNzGh_ZTStIAUxu_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بانوان هوادار پرسپولیس در ورزشگاه نقش جهان اصفهان در بازی روز گذشته با آبی‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28989" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=ZpjQnyhDzVOa9tj8A6NXpn_QGpqDlhEz5I8qQH8nvAfUZxgeo7uu8Bj8-tHrj6mB9a_yvmKnctSyiFFV0xPprVNZqEPG9x2xkyNlbuS2SLMAg39rjIzPkM3PeT6qX825Fl6WrOe98YXC0ICLJK-kkpF5pOLHChzB2TifUedpa25NzKI0b1gwrs_lDirxZvcHP2XcXlnhxx9xJEer6CeciGbtWpMLErGArn8rAJYMUbgN8hCU_AXqaF7oM_bANihn-21xxkPSP3uEOpAy367qpYDZrpOZYJNX85xWNPn0bsXliVGVdDFOlCr50UoXPsbIYmxzydv9oR9XkDBowYK7fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=ZpjQnyhDzVOa9tj8A6NXpn_QGpqDlhEz5I8qQH8nvAfUZxgeo7uu8Bj8-tHrj6mB9a_yvmKnctSyiFFV0xPprVNZqEPG9x2xkyNlbuS2SLMAg39rjIzPkM3PeT6qX825Fl6WrOe98YXC0ICLJK-kkpF5pOLHChzB2TifUedpa25NzKI0b1gwrs_lDirxZvcHP2XcXlnhxx9xJEer6CeciGbtWpMLErGArn8rAJYMUbgN8hCU_AXqaF7oM_bANihn-21xxkPSP3uEOpAy367qpYDZrpOZYJNX85xWNPn0bsXliVGVdDFOlCr50UoXPsbIYmxzydv9oR9XkDBowYK7fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماره 17 منچسترسیتی که سال‌ها بر تن کوین دیبروینه فوق ستاره بلژیکی سیتیزن‌ها بود به انزو فرناندز فوق ستاره آرژانتینی جدید این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28988" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28986">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQN3hOpv35G8anayZ6RV07Ur1FTVsyS9p-pcoTzfMYT2XUieBwpXU_ZkxyeQwSmxMdJDnRvGxOMOCaPMjv38jNVaSmlHtqPRea9eLVl5O_mpbk7lNVh7YEBZS4uz77FLDDtgwwD4Eqh70rglIdxks3b0UtoLgDp5_3TXRzgHwHDT9Om3WA2FUjVR4XNR6FJz41x57HCCERfiESC-1PPsZbFniZqE8Ag25bf2iW4s4ZuyDlfGf-ikxaQxm0N9NEjUO6L9zq1YW3NXZFUrCDrD7zyeIfhvfTYKMBIylg4uXq8p3i_6_pYFCR_AKxx82TQjrpdVx75hfnw3K8Zt2Vki0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=ZcCwG_5UpROHbpnzvq5nJt1LElHjsxdTQlFfPeYWgkiaWo46dlWfbL9FkO7wqSAKmki2txbw7OJB3orIUUsgFySVOZaP3wes2XlukMJDYi3tFbwKyxw6xqJ9tKXcyJ-C1WH6AaxrsQr1uGykFgDfxdI-KRC1Jkkh277GdgreemAVnLFcxdNECxo-kMH6OPmBnmnxVwRbboQJSieTxkV3CoeLlGLgGNjiG6kG1H12urSa-vn269W0ioSad52wWNKFThs5j6YfTyZ5tRzCUQje76bbLWs6jbmOxCLUpchakDF4eQonXBPLMGDgmDEMtMDO8EXEHyFsOLBwVoeCIMDo6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=ZcCwG_5UpROHbpnzvq5nJt1LElHjsxdTQlFfPeYWgkiaWo46dlWfbL9FkO7wqSAKmki2txbw7OJB3orIUUsgFySVOZaP3wes2XlukMJDYi3tFbwKyxw6xqJ9tKXcyJ-C1WH6AaxrsQr1uGykFgDfxdI-KRC1Jkkh277GdgreemAVnLFcxdNECxo-kMH6OPmBnmnxVwRbboQJSieTxkV3CoeLlGLgGNjiG6kG1H12urSa-vn269W0ioSad52wWNKFThs5j6YfTyZ5tRzCUQje76bbLWs6jbmOxCLUpchakDF4eQonXBPLMGDgmDEMtMDO8EXEHyFsOLBwVoeCIMDo6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا:
هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28986" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28985">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtOs--zym_iM8JTKfqhnGb08cMpkOyvM019F1aak8Pth3N4Lv_E3p9AMRdYcWLvQIOiCAVVfWGQGIk89xC4JEBrYGExXwF5WxrgEbKsi1MOWPeyuN0Ro6TFfyXzJM292YvzEPOSc_6A19bHw2kdsw3o1ThhPbdZxT3jwQjRBmsgE_XTtdYETls-lyzRVDjFNmyY3UAMBzXEbzjnKj9dju9YY6e1E96KRxNOF09u27fXI_aNIih09YicwzW-bCMagbungw2HDqQSwcLrYFTZZ1DAZ6TXySD8SF1h41gFRaLqm-Y7lL2LZvVLHs0zav-t_dLTO5iHgPkiDf2Rk-JfWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28985" target="_blank">📅 17:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28984">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTovn2jEsTxRMKXU2EGkBiEIB1ljwDgL80AqXlKpLY5K0XzhnsTxGCDmHk-D1Y11cMxyA2ft0FHYNvviKpJx54MtBlHPJhDAfu5O2g-qPrig3pGhRpc6rq4JQ4ccH2ZyTDkMPqbsrJqdmk6HZPdMnvj5z7K5TUsMITgxpsmThlB2x6pbCZu68qHxtmpv3rcg_sXfRb2KOCKqsZf01QtzHVil11QnZXnoGXjUA6EVTTMz1uQhFz6v87TOQvn4nR6q7s9T7geVEtVAZ5nrzQGPRjpgN4DKMB4gvi51OpHEbGs7Zyuh_DrL61sWl_11iExFVUL5EuctnCo06hH53KB0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28984" target="_blank">📅 17:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28983">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🔵
هایلایتی‌‌کامل‌از عملکرد ماهان بهشتی هافبک تهاجمی جوان ملوان بندر انزلی به زودی با عقد قرار دادی پنج ساله به استقلال تهران خواهد پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28983" target="_blank">📅 16:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28982">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmVJhnwNJs4x6MKMUB_NvR-B1GXyLZPYdT90sWWIURQ-oCIBrseUKImCJMB-yU7TE_B2pIHZNYlxM0ijcYUj8lDfHKLSq21SRACFovpnuubRi2X5bvhcpS4rLaU3YKmobm7P9MD00CZPLOi6_VQwYj1h_ary3CzRDmZn7VvzcZQgVe9VE6bcy5LPaVgrK05KxXCzuuf9A0OrRQIZY1FKesMz7z1-q8OY6Xrd7ud3U3tlp6-tAJKKPgaoFMKDHhzWFs0VlJMkJNLZQ1D6DHIv_wE0DKiSOc8vr_4OEzZjAts51l6hHO6Mm6eLCVp7TY2xAdiAHNGIZ7GoCeNii_KnSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار:
من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28982" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28981">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dE1NomYLUpF6gKLagE0rGYuUW0Vtv4_XKmfjC9DGu5ZB1bM5QSFN_ho0VG-lgILGVc7HaMBvgilVMgosjoo6Vt740YBxSkVtNjtrT-zDm-3AsjyaR3Ha2QaFlwhWvKO90OfjjE_LT7rtK4ai0-0RJw85w9EituDgazMu9OCOgtDRU6QukTzxTszgAeT9t3t57uIvkKrpEJsdkWDb5qfi4FJiN1EKspH9eGPRDfJQ3X1r3yuen9fOw_HwKDYNSgKqA9bJPOQh16ZMjld8pCOAdbQFWe0EiYLZG-R7gqw1ky5t4-MaXL1qd98-cTLcACVk9NX_aHOvsBuJDy1__1JlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل‌گرا مدافع‌ تیم‌پرسپولیس برای پنجمین هفته متوالی از لیست پرسپولیس در رقابت های این فصل خط خورد. درصورتیکه هر بازیکن خارجی 60 درصد مسابقات به میدان نرود یک سهمیه خارجی میسوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28981" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28980">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-pBC1PePtLnwlQOV54Ji1rUe_bzNS8dwxKIHtnEPwizWuLUsisTlxfRmUuRnLtF5kNBiveaqq6ibsoLlMPBDFocGirnWscS3W20syMffU6JtA4OfwNgwXDdtHcZaQeTJ88RggjNsRB3v8OprArNw6JkHfgCAHJVIuprLyDJjBSDLWwyTWGed_8x_zdvGDj1nC7pIbl98n6gD8wdsPWkNZD9GK53WgJpYpBNRQKj9rYf-HcZ_dSXdkVGZjiVstdjPl2QRyBPv6CjBa-k5U77OXw_wW8sxwe0jeVp9k8Ce2A8R4wvud6cMTzlFm2pM3YNequQUYZK9_33Nyz8cvAyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28980" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28979">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GznkpXuQEzed1PYZpr0UnCVotWLbKJZC2HfBh-uxQcbrdMkH9P3ju8YA_pBQ2g7qFk8ozRXl1pW7o37gAhPuPqRegRgVIcAj9LH-CNxpQe-f1YC6uRseAneQyCKGo88R5LmzsKDyT64iKS2tlWD9-1lj-JBf8kUnXRFQl7a74NoD9NBCC82iUCNPZSKPS5WSjlJn6Nz0NpevzrG5vlFeeSQQGINVY2xdZQ48hUaD5P5nJ4FSd6mHm5OsKniiSw1-5Pn8vGctJ4ucugtAw-PaX2NT0zhiBwjcsps9pG2N4QO5bdE3Suwyy4vuNLSaJsN0i3IqSEweUllYe0h1W2yfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پرسپولیس با تساوی یک بر یک در بازی روزگذشته برابر استقلال رکورد شکست‌ ناپذیری خود در شهراورد پایتخت را به عدد 20 بازی رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28979" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28977">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=CoE3_QCZSFJSIhxaMI91PUHJh8gxDV3Z7C4dUO1XhTFevFkdvoONeAKliXfLonKthjk9z2Ej86oIIM5XFmnERX3XtFB7NC2ld0lsVXqN9KhQPekDXd7TNV2-C20lHsWDg-ATiNWnozctKJTwplDztdkspo-YgguYpN76ox_0UG2HdgAH9B16hGVueI1DfE3sqZAtetLurCJJM1LHT4qZ3HZs8DVrHSeuztrFFXDOMnx_rS3jjprc0OYklN-8JQVTG1Shp1VzL9ynpEl1ZMIK3HefdS1FzYTKXqGCu08iilNZkUTYKsY-Wo9my6WQFuvbzz56076VqJVoPr7vQj0L8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=CoE3_QCZSFJSIhxaMI91PUHJh8gxDV3Z7C4dUO1XhTFevFkdvoONeAKliXfLonKthjk9z2Ej86oIIM5XFmnERX3XtFB7NC2ld0lsVXqN9KhQPekDXd7TNV2-C20lHsWDg-ATiNWnozctKJTwplDztdkspo-YgguYpN76ox_0UG2HdgAH9B16hGVueI1DfE3sqZAtetLurCJJM1LHT4qZ3HZs8DVrHSeuztrFFXDOMnx_rS3jjprc0OYklN-8JQVTG1Shp1VzL9ynpEl1ZMIK3HefdS1FzYTKXqGCu08iilNZkUTYKsY-Wo9my6WQFuvbzz56076VqJVoPr7vQj0L8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های علی‌آقادایی درباره تقابل روز گذشته دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28977" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28976">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=PEam4I7IgHC2MEjguArF0errZdlIoXf-8FG9WNvLXJ6EwQcx-I0LKIPQzZ0rp09IX2Uzbech5c9xumrcFLSpO51sAB-kg4Hg7rz2VC2vBfty2CA912Mq94W-Ot_fYiB4_sAh-3GK-9C9Ab25ETbIqKkd9xB9Gzi2Hmpe06C9Y3dA_tmM_6oNZakE-2JjmrlyVTC9HVkOonRKrsQCSC3MQaKQQbRsWtrlrNC4ri3HQQ_JXQeH3EsX6VleZFc4xyI9koFnJFJSApgrpn_MaS_7dlRt5Bj27j4_4_fsMbuYV7OIDgyiEvCwjp3zbpWW29SjmQVnPbf5dAf9GeE7rN02rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=PEam4I7IgHC2MEjguArF0errZdlIoXf-8FG9WNvLXJ6EwQcx-I0LKIPQzZ0rp09IX2Uzbech5c9xumrcFLSpO51sAB-kg4Hg7rz2VC2vBfty2CA912Mq94W-Ot_fYiB4_sAh-3GK-9C9Ab25ETbIqKkd9xB9Gzi2Hmpe06C9Y3dA_tmM_6oNZakE-2JjmrlyVTC9HVkOonRKrsQCSC3MQaKQQbRsWtrlrNC4ri3HQQ_JXQeH3EsX6VleZFc4xyI9koFnJFJSApgrpn_MaS_7dlRt5Bj27j4_4_fsMbuYV7OIDgyiEvCwjp3zbpWW29SjmQVnPbf5dAf9GeE7rN02rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسین ابرقویی مدافع نیمکت نشین پرسپولیس دربازی روزگذشته بااستقلال خطاب به محمد عمری: مدافع چپ تیم استقلال خسته شده دریبلش بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28976" target="_blank">📅 14:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28975">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1KB3ofLIN2IjLNXH872MkBLgVDtEL1SxA6-qfLYdMULXKHLIa-z_4t_6tGXEcsagEMuIUt8LQ3R0fMT651OUM2LENeGl4NhwnvrhDWhDHHlS59tKlLWoWSql_TRQLK1gxPtsiBMsqdj-LCXGqAhcs5fgE1G5nUwipOUvNlfmntsDh3gs3AvEIgzwvJZ_X64SOJdvH0mkBMK6My53BCMARog8iIwkaaTQnLz3Mjs3O7ohzZKArYkhAPhFpbR5QAKB7PCgrT_7AGKhnrMhE4UIJl6AscyQyAwW-owwGBhTLU95R0YUQdDTNopdavNpxpQiJQf7HJpoaAq2H-ujhorbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28975" target="_blank">📅 14:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28974">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=g7SkjO291fgEaQgIuaJQB4MMQZAeJeihHvl_sbGrclY8GHbbxjUfilFbkh9W31NYj97qSKGtM7CFiF6uxrWx-yPfHm8SQC0qg702p4Cy4zGRY-TiTtcDOhP0dSsH5lFgUcITMQXuN987nMOj__ZJziTvffkY39ENsco3ni49yPzzKsoJ6z1DdaaJD2ut2q3MdOmahLaPhyntOpi-JunkP2_yUJhT_zkNwUSs30o0l2yZILLIhDBUELmk8f3a3AYmdLXzScSYJNBSjbTD8nyCokXmUmXJWobPMzh6hH9bAngTnF1ny31IHIWsCYmSjKYclANTE4Gif7pGl28UVbyf0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=g7SkjO291fgEaQgIuaJQB4MMQZAeJeihHvl_sbGrclY8GHbbxjUfilFbkh9W31NYj97qSKGtM7CFiF6uxrWx-yPfHm8SQC0qg702p4Cy4zGRY-TiTtcDOhP0dSsH5lFgUcITMQXuN987nMOj__ZJziTvffkY39ENsco3ni49yPzzKsoJ6z1DdaaJD2ut2q3MdOmahLaPhyntOpi-JunkP2_yUJhT_zkNwUSs30o0l2yZILLIhDBUELmk8f3a3AYmdLXzScSYJNBSjbTD8nyCokXmUmXJWobPMzh6hH9bAngTnF1ny31IHIWsCYmSjKYclANTE4Gif7pGl28UVbyf0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28974" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28973">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t76ZMLKbKCuSIXysk7eSCb64k9y1YQy8VBOnsGnYLyYs0GosbY5m6PSk62P_YgPL5ig9IPfPfs3s2uTGTUHxvEqqepzcV7xrDbZlZKhcYsAumfuZ7JTywwfOmwax0CsPHjq442SwkgTX7_IVoEJPnabCGcecSVbMYPI_ALEN6kf4pFBVM5MJbAThxS8o3uu2AGbsSr9w8fYQK7UHx3uYGLrks5zrqmg3XEWf2FV1DAtgLBgyTe5ewSEwp6TC5NZvZAd62P2rCop-Ei_7JCNPrEgpwQeOq_nfW-u76-02EjUC9QgAgbH05iyBtd3v64l-W3MVoU-z0CflCqBYGh52aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28973" target="_blank">📅 14:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28972">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMASaNsgG3DsmYlPFS8u4Y1-r7sVMTdNEnUOahTNAusR13JhUh_o25mcRpcmF9zOrDC8Y0gnq-2s-efijaliy-gLoUeUB5alCDwgQGzvIGUhf-28W-WPkj4Pq34F18O_YpkFTchjSQUiWOFyuAdH8bGV5eEKEUJAGOjyipTdah1FC8sViXcljpMyMvJ2a0g3bb3LJD3YB0hMDOpW2qr4VRbc-5829CLtJxZkRZUn2ZQJKztltFCyI-URRvf-fsZ1Hcuw_r5RQCOViGB53icjlz-2TNI0NK8HzHkc6Gm_t3sN-GsZQIKYG9WyUcIjPBz5d4Id92QIPynQ1FRI66Ou_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ: رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28972" target="_blank">📅 13:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28971">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJctBUHATUkQpQHitP7MyHfsoN4OrjiCLlXrWRRBAk37vVcX3fZ-zfJP6eDTTl9Wy-bYwOGSJv_JehjoRROuRxLr5HrxTERnPZbjLOI6ZMe3nMmiEpfT6seZ0M8DxLvShCsn4g27My5xgFAN-03FiybuLgZ3Xk8bvbyFKKd8NjUbo-ferywctxOuQ0yOTj_ZPb4ccQZIznDGwd68uMcjMqIYotohicx05_uH9k6qNnybdobWW6xcb8YC-QRcsNiCzw4WTSqe5jdLagQ7ZipqC8N0P8jMdmfhhSx7I8OpAWIH5TjSY2GRdxpyse13EsS99Tl_4Powm_ljYp0cdSqdtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28971" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28970">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELHfHjP8MMzJVZl89sdJC_7DorMSoXtZylyutivTfMzEmmwB86EHhsc80EJGBamE0l4Zy04BTBDLNVqevsAQnV3-81WwYxO-GG15LhP_Nru0KkvxYjd3Qjf7xsloBluMHTy8cvC34S3vd1NK6xMbT2HoDqvMFHiQjhL0mfLF56PmrxgjZ5oFDUhVVT6iT1L60yH1AlOyGOncFVpVyR5pHg9OSkQEfN6UPYwUPJ0d_lcTaop0S_ezu4ccMFOyo3qwELHS6panktBsPixOPC3zINYItPieUaqIexX-Y0a77db3X0joV13zCIMcfsnz7IOTnLEnwjIaMHXCptBe-VEEHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28970" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28969">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=aey4nBKkheQNjAXDR4GOKvLJdtef9tVZ-yc-eYNsJzYzmmk6OmX6FXQzG0kRWGdfbDxdaWc8td4ZtDdQsRcY2zV4_1OF6JaPYXOOC3vycuaFEu-7f5si4wEwE8TnnzQtHVu6LQTV-fMm0c_0tpuhgfsQMrR3crXZOaYaymK0LaXXBvs9CK1Du612fISd_8j_olbUFuVSSTWVx0wrEf5aIqPjgnp6b1nmYQc-14AbQbngnOJbYFF4EGUD1Y9J6K8-tW8JZrtlAZSFSb1mNPfrFjqmO4uPKNxb31tigYIHnrdtY5k6Vr2km8oyP4FbV7gMPHgcn2ewVHRJ6lIH1M9yyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=aey4nBKkheQNjAXDR4GOKvLJdtef9tVZ-yc-eYNsJzYzmmk6OmX6FXQzG0kRWGdfbDxdaWc8td4ZtDdQsRcY2zV4_1OF6JaPYXOOC3vycuaFEu-7f5si4wEwE8TnnzQtHVu6LQTV-fMm0c_0tpuhgfsQMrR3crXZOaYaymK0LaXXBvs9CK1Du612fISd_8j_olbUFuVSSTWVx0wrEf5aIqPjgnp6b1nmYQc-14AbQbngnOJbYFF4EGUD1Y9J6K8-tW8JZrtlAZSFSb1mNPfrFjqmO4uPKNxb31tigYIHnrdtY5k6Vr2km8oyP4FbV7gMPHgcn2ewVHRJ6lIH1M9yyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قهرمانی ارزشمند و شیرین کیانوش رستمی وزنه بردار ایرانی که عده‌ای نذاشتن برای ایران وزنه بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28969" target="_blank">📅 12:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28968">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=DHYy7FTgZ6f--BPX1PGknAqvWw2zfYJdfu1gUFjgwYAb6v0PqJDRYXP6tuhoQ--1AVwZ1dYWk3OrPbLPUOsKFGC9T3TBHyySAmdO4PIKmD2-8r_EQ0OtqVZwUZiI0G0QgqALT3nj0hCqv5BvVvenzFYglnPnoaQL63Jei8TCrBRlpgTokhWYlWlBRwMdsikLZTrY6iBCIcynGAs8wczOxoMzY4XQhS6S1wROjTn15z2T9_YdvXLONGBrOl4CPAT1n-VxHcN2sJzMNCf10aYHckyVcWlt8gr3_L-Z6wOgclYhQ9RBeXf6nfKsKvV7NZXUt1J43ZxR2ttt-SAEzCmKTWbXWNKx4K8o8lGTEyvg3l8qtm43qVYiHtght3GASXthyBZp2wykUd8qFoC1SlEk_a4qK7glopxwxjMAHpqxn7n7MJW3IR2yv4js0gpc4gB7YWbtVWLaqZykZjbMS5wuxKu6M7uLIZ1UFSLKKKPJmpsaX-9UploGKjePmtrRG83MJ1Gb-x5qQS9nb4ZeehiFB5eyZbKV2buudqwESsKZhGL0Spksxwig2x97aHxC_HL_j7PZQyEilXnkjw0UQ9lvbnPqvTTIjq9vOIMjzt_vV-a7CUpTzqcqMX0WfXVpOsDpSR-K2zfPYIV1mMzYjYS-rJs9FXtfUXrjOlSaaK1YsBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=DHYy7FTgZ6f--BPX1PGknAqvWw2zfYJdfu1gUFjgwYAb6v0PqJDRYXP6tuhoQ--1AVwZ1dYWk3OrPbLPUOsKFGC9T3TBHyySAmdO4PIKmD2-8r_EQ0OtqVZwUZiI0G0QgqALT3nj0hCqv5BvVvenzFYglnPnoaQL63Jei8TCrBRlpgTokhWYlWlBRwMdsikLZTrY6iBCIcynGAs8wczOxoMzY4XQhS6S1wROjTn15z2T9_YdvXLONGBrOl4CPAT1n-VxHcN2sJzMNCf10aYHckyVcWlt8gr3_L-Z6wOgclYhQ9RBeXf6nfKsKvV7NZXUt1J43ZxR2ttt-SAEzCmKTWbXWNKx4K8o8lGTEyvg3l8qtm43qVYiHtght3GASXthyBZp2wykUd8qFoC1SlEk_a4qK7glopxwxjMAHpqxn7n7MJW3IR2yv4js0gpc4gB7YWbtVWLaqZykZjbMS5wuxKu6M7uLIZ1UFSLKKKPJmpsaX-9UploGKjePmtrRG83MJ1Gb-x5qQS9nb4ZeehiFB5eyZbKV2buudqwESsKZhGL0Spksxwig2x97aHxC_HL_j7PZQyEilXnkjw0UQ9lvbnPqvTTIjq9vOIMjzt_vV-a7CUpTzqcqMX0WfXVpOsDpSR-K2zfPYIV1mMzYjYS-rJs9FXtfUXrjOlSaaK1YsBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28968" target="_blank">📅 12:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28966">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSKb8CQ7UEUka3MY3KEvDPbukWG0cfTlI_C10DpneJE_aU1YLLk-u-nRd_LzV_SFpNRPV8IS1VMeqC7GnDNn5-dZi9EGCgbM4QP8a-SmES1G7E4piUndpTZFkyYJrRgsibjjRaGWoiMAnnFPKusxu7sxsmGiLUfvIpIYGSmkxsgvdrrFss1O4NGHBg5HwlOpBZJKwaZqRNX81pOj3MSumwKN0b72H6j-Z9aJT_C4HAmz2szDFWAgWlAxt50luIi_LgB9TLIEu5AciqVWBfOG08LlpDkKFa1tI7ORf8J3AnfrEQeuJCL2b5aGK9VG6xBLHBi8iyjSNZ3BrrycTDWnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28966" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28965">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQCCqUOg4qiPHPw796HxzjB9TgHvcRvlXG5ujHbYNz8RQI9nPyFja1vXjqDsZgTC3L2kc12CP2okDAm8bbcohdUMxSgYwCZcJudf2dlsz6DVs9-pLkGej0vFMaSQeiFEzeIwlOmkA-A3wyEYYpSoHx-8T5YKUFEekJXq7LYx5wc8wQTG4rbds5noCwpz-Ex5bZQGy4oiCVpw4jiPFF_3uLWdlhp9GfHcwSDyVvYut36Mbjk6CORSytbTYSsIonWBvW5wrq6zKU1K8ggDZPmKHK8QOJKbvhwMeNTofgi37kDkBgTTtsUL8P9JmzKgccoBJw4TTKGlqFpqMTJaul9jvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28965" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28963">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d582283b.mp4?token=ujBeIKczJ8D8s6UnoEsZRhmPlQFET_1DnRxLSPjTYTzPLSDwPhp9am-Hud-MRO0KcwH-WbIlrC7yeWLzMoVZCD0-vLS36CAdzan0iWcqUdUNGZAQXbWXEaiEFWezg-OMJFBAkv4Yjk-_tQIceVGKl-p1RmX8WsdApBa0RgzWk03AXOQAKVCRIAU0Vyb8IqNWKtHxcAgBflswkAcwtMY9ceBreLeCAbmRaq8e92mygSJt-4GgUAli22IZJHMAnIybFfZEE5hU97OUBCbfDtfML3jIeSDAt0XQlihRhSnqNpIg6A4ye0hFcf7uxihJB9LwxJ2J4KFo7anSLnc8L1mOQwap29GmTHCMxg1y-o5KcoYMJz2GXca0B5PnU-8Y4_x6r9JXaFS_pQ9dcCaCe4xzebgsrFLRG9391Tse4MRXzgOB1aPtLXmt_60pzzT5yFYK41J4XTciLB9RKudvJiOeN1augzNHUyue2f0brN0HlYgc54DGfWXzC7iTKFSkeAENODwJo75VpgoTidzB0o3FN0XeDr6c566GAckNE3zvHJyQCjINDaOzYU64ZogZMBbW36g6cWQgs9MTRD-sviVjldHw5yoCxvE2EfLJRm1YBMUF8uf4rhFKrDyXvDrotEoHkMBXY66eP8gWYg5ePL1JaL4GzFCI3M-zIvF9lW_OHPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d582283b.mp4?token=ujBeIKczJ8D8s6UnoEsZRhmPlQFET_1DnRxLSPjTYTzPLSDwPhp9am-Hud-MRO0KcwH-WbIlrC7yeWLzMoVZCD0-vLS36CAdzan0iWcqUdUNGZAQXbWXEaiEFWezg-OMJFBAkv4Yjk-_tQIceVGKl-p1RmX8WsdApBa0RgzWk03AXOQAKVCRIAU0Vyb8IqNWKtHxcAgBflswkAcwtMY9ceBreLeCAbmRaq8e92mygSJt-4GgUAli22IZJHMAnIybFfZEE5hU97OUBCbfDtfML3jIeSDAt0XQlihRhSnqNpIg6A4ye0hFcf7uxihJB9LwxJ2J4KFo7anSLnc8L1mOQwap29GmTHCMxg1y-o5KcoYMJz2GXca0B5PnU-8Y4_x6r9JXaFS_pQ9dcCaCe4xzebgsrFLRG9391Tse4MRXzgOB1aPtLXmt_60pzzT5yFYK41J4XTciLB9RKudvJiOeN1augzNHUyue2f0brN0HlYgc54DGfWXzC7iTKFSkeAENODwJo75VpgoTidzB0o3FN0XeDr6c566GAckNE3zvHJyQCjINDaOzYU64ZogZMBbW36g6cWQgs9MTRD-sviVjldHw5yoCxvE2EfLJRm1YBMUF8uf4rhFKrDyXvDrotEoHkMBXY66eP8gWYg5ePL1JaL4GzFCI3M-zIvF9lW_OHPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ:
رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28963" target="_blank">📅 11:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28962">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGEEUoTuSoCP-WqOVh8De1_2tC174jqWq_PeHV6pBFEP7ePL0irMyC6pqU_Jj-cmOh_RxuAAnluv8A6vyU70H7bdyW76C2VFvTwbbbtuwVWGagizIefVpjyDEG1cXit1nZISyOOyGt6CbPov6zeyhmp0q9M_qpiJv3KGvPxJtmLszxracZghkB0riYkUPMFDtQyUHyBs-xfW8JgCOMayBrcHaXvO9ruXjWkAnnqd-u_dbuPAbR8tdoylHHmGPgUnfcYVAj-GMxOWPpOMUSxhO5aKVbXkanl3yZ3mdJi2QcCVs77AdeWQKXI2JXKh0ROn-inGyNXGvs6DOVs8c05mNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم منتخب بازیکنانی که در حال حاضر بازیکن آزادند و با هیچ تیمی فعلا قرارداد امضا نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28962" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28961">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXlYtPcVAeMGAXu2huCY_s2b9lmzMpcpa6nU5IguFSRRMmyAYaL3l3iBVHYCQK2dfIh_4zEEOulUImBS_9FbARiOzvIZ4d232Ff6KXFmN_alh7K1ju9VFnodjTvpkf_CAJ8ILsU4nl8GKMpsmsr_c3Q4AuNGats0pOIKQFfroh0P2dKaQKw6z-rGFZRwP1L_UcIdaohxs4u7YnFiVAzWBb_AplWCu0TFP03HfV23B1zztDG2slXyctgDEK9w4UEwaZgFOLc29oJEUWvnH-TaWUQI6La7r56PPd3VWnj0VDdRYuMsPeT6_63VACToRMyoqd_pdT45I1On2UdzRD_WyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌برگ‌ریزون‌لپاریسین:پلیس‌یه‌فرد ۱۸ ساله رو که عضو باند آدم ربایی‌بود دستگیر کرده چون در حال نقشه کشیدن باچندنفر دیگه برای دزدیدن امباپه بودن تا اعضای بدنشو به بالاترین قیمت بفروشن:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28961" target="_blank">📅 10:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28960">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbDVTDRFoiq8DC4DzVTv6M4lSyySIOTXYuBkq138SaLttWOvqSdeUKMvmDIb4RHgSmZXdi2bE95aygIsyCuMAtjv5eidVp4Ke5UCk4CDvbV2dzPLVUmflq4JlWv-JymaoHDONYALniD48j38ke3usFrwsdFTcGlXVHgMIR9XdEIepA1clnP1aNf9zePsH9LLT3t02iWFAwSThryRGz6CEfgYdICIg3c-pDrgGv0evJDYg_2NOp5OtFdSxJXlPp9tXTatr7PwEUb3H28pt-OfXGLjuSdE8_HhPuZFal4xptLs_o4_1uDzZsg68fTSK1RcjiTUCnI5kmn-EjQg6YTUnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
👤
بااعلام‌رسمی‌ فدراسیون‌فوتبال غنا؛
قرارداد کارلوس‌کی‌روش تاپایان‌جام‌جهانی 2030 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28960" target="_blank">📅 10:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28959">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ts3YGJRyunsobsVY3603wdOIxlNCPXMwpL7UYtS1nw43T7BJBslJ60JSNMW90XH-FUKGF9CecTCDCAS84sPWmQEpC53jDsA-AKZu3oSbmAhgCFYprdRsn7qa8aM8RR75emPod7YmBJafLJs866514Fm-mANQlKLBgNz3Mxlid3aSZGD_T0DayS0jIuWoZDy11K2zePyLj_lCHxkFoTMIYXGMMocDU4nPfFyTpLZMkaypstiYzzPyZLCXKVuJRYJqODytoV6-FLz_8jVieCc-NLNzMrB4LDCko1ngXXsyg3-EFLuOWK60zya2pmW5LaIaITCJ-ircYfNoz0MkGZkhDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28959" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28958">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbwQvcEOFejJbvUDNArxUhzFPBp279Wzi2-i_twFJrG9Q-ctXTPOIvGrowa4QZDUvTAwkQWVlq7yLVIqtV5H6-AjE3qtQfp8ZKa88J5GVMo2LQMJlRx_fcEl2xpP6gkUbiUXh-tBg9neZLl_CtUw4VqXIC1qx8LbLcjGjUSyrA6yPyCk-45RV8wzuPsR0zVbZsnRLrGN8u29iiGbtACU-qgQ47T0kGtm7es2izi240eA96sSEchTElarQd8j9-HCGUb_lGfPWpVEckokENOWQNUq1rhKuqEvyygz1zrX6OY8Uot8CqhfRNKE6ZwtAP7VHyYhuVf9EJEUldaKIwEHeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
کامنت‌منیر الحدادی‌برای یاسر آسانی پس از دربی:
«به تو گفته بودم که تو دربی گل می‌زنی
.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28958" target="_blank">📅 10:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28957">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJNYnYvTD3fRe3Eml0tc2_3v9ZbDl1d5MXpHcAHsuwb5e6YwMN5wmwgb5nz1wXzODqwGdOFU2MSoXRhTX8jn_C1gVl5Yp_2E2xW9ztcXcrIgYfUQlQDSqveHCiw7zvmwjtgYCEAwNWcQ4F9smkyIBavEWf0CtVRk6XK42AFDBT3YjR46aAU8lT15Pm2RFNjFMV8zeTRpR1u0Ti-RW0VRCxOM3sb28Cnj2Uz2UeAI1MxHFIzAghHP_6U1NcSoKLpQuKLaWUdVBOduiTmFKqoO46D4S2Y5SWGVTHvii-Ow9ksuD9dkcLDlz7m2cWz8FHAerangSiNHvkhoxWF9n9I9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28957" target="_blank">📅 01:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28956">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2nsOaptQZDnOz4Ejry0w5X-DdDcApx6I1_jLvBSMWqsST43YQHN-IqAVaeca3oilAZ2ld0CN2QH9xZLY3qrvds_iQqEWTmGyeQvVQlnjHBVWbNQk16C7Z4QK4oucUHCAA_j1CLAtIF-G286kJprINh-R-BcYtfkV5H04GkCcH4ooFMSZ35-9xUoaUiMJi4oLUQf5EciXKGgLxSBSXMk_xTjHUu_940izqxHpGsD_XiqsPAMMYbDnEd5O3uwXSY6GzgzOjFkE3J6ELJxFshKH6nMojQ9nadq1SJC6244bduSa0sOKLDPGU05HkNxrhJJN0mI6hn8NppwyZzCPS_l0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28956" target="_blank">📅 01:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28954">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUcOlAVkqkZKsJbhpr-_nW-DHpD261Pb1Ka1VOr0Y9C4kO01PUtQhM_iSreqyZs03_KHaIh1SwVAe97uyJii0VIaCvZvhfbx1XpWZ2W9hmQHPifUb6tID2CGv9jXU3ZrkKpYE2cbQuSV9hEkLRhnK-JS82IltxbRqu1y4IaEhzEcwQ7Up9SvI51AE_y_TMImrugevgdHcDTObIqd7qeFzQwx12_DPCcyqvjpYiHTfHbIXYdXPkwbfbOW7carw3wPYFpd75Pqilv4IXiGWsj5hCNCqHEyMp_y-PqdGOqEwJ3GUnVSnBqpZEEp-a2fJl3pCr7YsC_Tk0rQ3i_FRZ0bJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛آخرین‌دیدارهفته پنجم لیگ و شانس صدرنشینی یاران صیادمنش در لهستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28954" target="_blank">📅 00:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28953">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiXvVlh0Wb0kOt11uKoYxj77ziFgdbjJ_ctiWMEazUeoY-jDacYPWEnxmCIbKqlZGQpSLc8d3ODrfrd8W20OquitOSR4oYc95urZ2cVxLxQzusbvAAyBHsk5Go99oQae2w4hc7cDgMHA_jSjXBG6MzHmBpteukVwukWbu47cw8u_JkSmlTkqGJMFA55rvTDC-1lImOvtjPlIksnS9YtGPx5PEj6zJMBONo9Xp5iO2OiR38zFBf2OL3OJsuWpAH6THoytzsRoUrZitGRb0MZtntozDy69PmLJ7-ONEBPrOjoF8Z2a5b_oZGVn_XYsTykZra8oCZq-ulsLW78qKsak3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌ دیروز؛
تقسیم امتیازات در دربی و صعود بی‌دردسر باواریایی‌ها درشب دبل هری کین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28953" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28951">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzXrHsWF015HejZtS7_X4kDBjZ3lVnOeKlDhGhyF8i7gRoWW5ygK4741njlPM7ggT3PjuvDjQl3W62t0PPdDdkP7IiUMJ6WPauNsQKOz4Vie-T0rjtUzFIhBKWyZqGZJSK0iKRBbrq3DwMQlB4ZKKevi3trJOOLTNy64H3qQePFv92m9T06hp5EpL8Z-NVONkhH9ncK_0uRxxiBEeWyRZ0XT0w0N2y0vQwrbcLgOA5TgUL2hKHZipjn-vWNXnPJD2aky7XGut_Ap-7SD-NimDGKew-I77Y-sWm_6EQtkMcFmAOqQPO1TmH7Me0llYbIq5nJjwJKJIKsHIbSYpidgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28951" target="_blank">📅 00:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28950">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aApW_zUOgj6vI585Crp6q4xeH-FqBDmdeppc17mINJSMi_8Rtgx4c8zPBNzEdyVrKvi2o1X17c36qXlq2rnOjKDXdvyzneENmKpcjTIaFTAHJXzlnONm0QdjWPafDqWVMDj7bWKug7c8RR1OfeDa8mcZPdZy3bSvgoPGOVI9HSvoHcMf0g9Nzd_hoj_PTl3UvfLMe-ixn1_NYU4JAYoq6kpBVK2Jnb_0e8btuI2uK4CuNJ-TtTOc-hvWbCVxJCuPx7FyVLqtQ44KtCummITAkyqD-2PjbIry4hHPtMpaCtSe-fs3x6SHRsgyyI2upM9q40WeIl-t-_kqYFURtwB2UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌براینکه محمدحسین‌صادقی وینگر 21 ساله تیم پرسپولیس ازلیست‌ سرخپوشان خط خورد. دنیل گرا مدافع‌راست‌مجارستانی نیز از لیست کنار گذاشته شد. همینجوری‌پیش‌بره یه سهمیه‌خارجی سرخپوشان برای فصل آینده رقابت های لیگ خواهد سوخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28950" target="_blank">📅 00:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28949">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=Vsp9j9t4Wu9ztVG0r6OUCwFhjlP_lc3TGMx_nMNQBHtFv5GiK8dYWDptubZQKJ4N3P1VASrRr5T_-q2evfCn6l7fdvCBoVk6FZPXKMip_4D7tCT48RSs_ltSLx_TN-PKYZHOyfRRX_vFnbfhPDCw2IZA2ddQ3rU_lJK2HA6tqMiHhipvG069KE6jZVvWJWKHfvbTS6imR6WFl5FLlTqBsdI4Xv2xhrXK_59JbC9og0gmiQl0DB-YHQl0xwzaT3nqAvHAJ_t5u5OLAgG-b1sZ0f4z_JNVjz6pzsF5UNWoiBo_HGanUE8H8jg5Ficxk4K2NP_rVofREO3xw4xbXwQrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=Vsp9j9t4Wu9ztVG0r6OUCwFhjlP_lc3TGMx_nMNQBHtFv5GiK8dYWDptubZQKJ4N3P1VASrRr5T_-q2evfCn6l7fdvCBoVk6FZPXKMip_4D7tCT48RSs_ltSLx_TN-PKYZHOyfRRX_vFnbfhPDCw2IZA2ddQ3rU_lJK2HA6tqMiHhipvG069KE6jZVvWJWKHfvbTS6imR6WFl5FLlTqBsdI4Xv2xhrXK_59JbC9og0gmiQl0DB-YHQl0xwzaT3nqAvHAJ_t5u5OLAgG-b1sZ0f4z_JNVjz6pzsF5UNWoiBo_HGanUE8H8jg5Ficxk4K2NP_rVofREO3xw4xbXwQrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری جنجالی از بازی امروز پرسپولیس و استقلال در گیرس عجیب بازیکنان دو تیم که منجر که خونریزی گردن عارف آقاسی مدافع آبی‌ها شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28949" target="_blank">📅 00:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28948">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4-9dH1tlq-Nrvs4L_J5Ru_4R-nNSx7rz22h2AzOdlcbg9ri-g0kB96FTq91Wc9e1r-dy2HIDuvdwvk-kZXO4Xw6oNXJTI4Co562LNhUmBduPXwaQQYZfL6OQT-Q3U36aypvViCYIGoy1NaOhHV-518El6KNsltgE2JFY4HANtwqrJnR_ZZhDTAzpa-we5xVqrLDoAsKNJU9QT5s6OdUeUjo52UJutr7_p5WgGXd8WJyCeQftP3ysxX898xcFeJKa9AN78QhAstScfUxTBBfApZshVHlKqAx-w6izKyhO6yvh9D61zkkvcwV38NtZdiZBQfR2GyXKtyQlQZeErdBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28948" target="_blank">📅 23:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28947">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=EmLc3KGt4R50V8Ax7amLVMyr5bPN8hmO-58VE7MRPCRzJ2zanmZGLY0K3HDI3lmEg9l0wzB75_K54fmhtpz0iz6Jcp24JmePKiys3M7FhNofAhGt0br_jyalhIuVEc4hvFUVlumgbvicOtNmq2hml_hYKCLlHBo4XQKB-pGUUUHt3jLoFvdCA-fXhYXPQt7dDgYQEvItKjt-UGG6BQJrEpmuyOJwTapUNv_gCAkUZnHR3KEtKQq7hepo8KtwXkSilIRZwy55jJQ8AD78UqrGtsQf5GowF4CPIWh7oUkT375sVgh9P2Qr8DzyLA6MydNosxLEMRsEwxT9VXTD_dqz0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=EmLc3KGt4R50V8Ax7amLVMyr5bPN8hmO-58VE7MRPCRzJ2zanmZGLY0K3HDI3lmEg9l0wzB75_K54fmhtpz0iz6Jcp24JmePKiys3M7FhNofAhGt0br_jyalhIuVEc4hvFUVlumgbvicOtNmq2hml_hYKCLlHBo4XQKB-pGUUUHt3jLoFvdCA-fXhYXPQt7dDgYQEvItKjt-UGG6BQJrEpmuyOJwTapUNv_gCAkUZnHR3KEtKQq7hepo8KtwXkSilIRZwy55jJQ8AD78UqrGtsQf5GowF4CPIWh7oUkT375sVgh9P2Qr8DzyLA6MydNosxLEMRsEwxT9VXTD_dqz0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این کل‌ کل بامزه نقی و ارسطو دو بازیگر پایتخت با عادل فردوسی‌پور در برنامه نود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28947" target="_blank">📅 23:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28946">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsk_4nVwq98a56mfFiwpVLuuiaF8h8-xb3SldFtmlwNs2lMxFT4OwIV1LxMAiukX_vTCrTBvLUE30Dv6icYPfmBSZqGH7mAY7DHo6CKZSBxRTXYCPwEHk4Q0ChITapWNDuCL9IbhPgAYTX_65dqlhv6TwHUk9GsZxKOv7mFuerpjgMdivJrHoRByZ0hgeVi0a48pRLPtp0tczsNk48JO5_mPIgOZAEDFbLT1DvQV1E6Bmo1tLgvkSEuPgfJM9yZoOe7MiOkhiDHOwFcA2bDCP9oV-o8wupRWzH6xLRO7cRakkj8eaSUxx_kUZW6AvWLfzjiUFJve1xWO4Qw_oBfCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28946" target="_blank">📅 22:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28944">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aavv871th0p71Zg0I3Ylp-TVN15LahxEnsojQJSvArtvlkar9m4j4rhch9drX1MHjKl6sbHIVvHZBturnl2NomuBNU8lU6XTsMaQV2JqdKPo1XRMtsjaW4RY8F_i6cXL6Gq-PJSQVUCXl1OIgdVigpB9ryvHPfp5PK4EaB_9_XjCz7Qk-Gc8kKnDPg_xRB9HtIQM1qMepSMy-9r_8TSEDb2cDKxcP65bvVa2R1cc8gmtUwg_QA3tGt58VHPQqfhS0NMeLG2cZ0yrvkGO_7flpxMiDqG6vMtsM3weX_uMKYxnnYDTmNqMHu2KQm4qwTjf0qoA7yqoVvLrx_pY0ShMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M3fK-A6vjgNxt_JvKpBYOvSOcNF3OmZ5KGJ-xdPF0Z48aO2dHBqNn8ULneow0dQ077vVjBzaMzi7tNkShzQKwgACNksK3moA7uiNJhRy1dyrW-fh2jGXbf-I61U-fLOgDAaJhQnAfZ8NhJuY1I6E82nNto5VmG6qxt09o4srLRdUQPMHlPaGGA6qeDEXQzEtWFYeIZyrSkZSaktvjknI6c_oBYbOZMJKdH39zT2ByvGJj1NsRwFfIJ5IBUqzmDCTZ3jx7X27LeTjsCCDVray93z9zFtThEoK2U7MRk2sPJu-DnUK6qinKSD7CG8id_Sqe_ATQ4ToNkxz8psza_hqfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28944" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28943">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtuamEHIkdZpC96jV81QkRmQZ-aV8NfghFUgPXRKJBsHj41aezE017f1tXiFtD2aq2i-K_SE_9gG6iwmi9bfTwJXK9WZbpvh8XuyDzGQDwf3gkItbNJiKOWYHzqaOBWUPVRdQsf_WxmVl5R-1LaBRa2JS9b7TtYhcVnkeTtCEqiCwb2dHqmUfoIqQGfrWBqf2FFKY4TzxpXJuiY2BTt_0-rF64uf4zmEZhoBpFphn6e7fKFsswMLViJStegt1fI3RblhVcWEe2hagNhRn_65iM7GyRHQDTOO_NIEQEHEftysjvSTM-AXnxVJcTlTRFWsOeTRZMyKXOMoA5yb-PActA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28943" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28942">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3j5uJCiRvYvcC1FmUoHB2h_ccls18hwocMkYcZeMV-ZX7pceZyaUITTfXHTHoQmBDre6PNpWwcQ6T3qJbtGce28Ud-VuXt0oKPJ6yutk2ObO_P_7qKJieDkFoh97HusFMxI55XxCfP5MfeVMtUkJKh_WC0v05unkuz65uTmFCLd9fBkDdAxe1spAZ7sajBTgwzNWCbvHS7l7n57Aa5IfwTb5uyOUZjEbMpOQ2egDAZhZQkTT1fQlGTRemH0-SiiCvmNR2U_D7vAau5m2b0PHWveosxFqi5XFw_pqnNZvql88syYcG7HkrCGJ20hItG6tFVUDo7JnD3HMGrHtxyHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی دوهفته پیش پرشیانا؛ اعلام رسمی کمیته انضباطی فدراسیون فوتبال در خصوص تبرئه شدن استقلال و یاسر آسانی در پرونده شکایت مس شهر بابک و سپاهان.
‼️
دادگاهCASهم از هرباشگاه 100 هزار دلار میگیره آخر سر هم بهشون پاسخ منفی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28942" target="_blank">📅 22:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28941">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=JM5ZRJtGlPaUV3MfYQK6Ch-VN-hCIU8ylw4obu8Mh5X1ZuMgLHG9ut8ILD9aVCzEnBip7nn3Mraa8LHHabePIv2_drAB1Z693OTDTwrGtX8n935rS94WRjCk6olARGPiMazqVSMOqKl2KRzsVOHGdkI11Uv8SaOpLkKUheaAztrjKTpWaRywKZya3lPzirOQblIzHcwZ3fxE7QpUhbSJlHEcrfCr_585VbzJA6_OMXI2VQBvE9k22yNn4QX14P0Bh0Lfz-QHnNwgEPOQiWOroMFcL15apFE7M1wAVGp_MQI5cAKYqNTzpqkeEOgBjagUp2OXRT9ZriNE91_5p08c-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=JM5ZRJtGlPaUV3MfYQK6Ch-VN-hCIU8ylw4obu8Mh5X1ZuMgLHG9ut8ILD9aVCzEnBip7nn3Mraa8LHHabePIv2_drAB1Z693OTDTwrGtX8n935rS94WRjCk6olARGPiMazqVSMOqKl2KRzsVOHGdkI11Uv8SaOpLkKUheaAztrjKTpWaRywKZya3lPzirOQblIzHcwZ3fxE7QpUhbSJlHEcrfCr_585VbzJA6_OMXI2VQBvE9k22yNn4QX14P0Bh0Lfz-QHnNwgEPOQiWOroMFcL15apFE7M1wAVGp_MQI5cAKYqNTzpqkeEOgBjagUp2OXRT9ZriNE91_5p08c-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28941" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28940">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">📹
خلاصه‌دیدار جذاب دوتیم استقلال و پرسپولیس در هفته پنجم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28940" target="_blank">📅 21:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28939">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zk1nTKchcD0EfGMCwP0B4pS1zZJfLfW6JS4d3iVahaD-iB0TRkex-zmuYoHml0DJXhaCZvFmG3SfDwSKcBiXO2LQ9xEhHETDa5Iiiwc0bn9m-VKH7e9_ZqPKIb6zgfz3LG1yNMjmcA2aimrBTtJMDKVDEboea0KwYozBJ81uC4YcVQKJ6WESAzDFGW8iCJq3rWrVayqlcm5hSOysuD1DQkD5xJPaeGD1zPnpCFFnVYK9bdNLm1XJI6VVkIlBj3uVmbO7zZD4Q1ja6e0APg-E-KY8F_AzO9cfwEqRo86tVzwEeaCX5R03oXkthmmMVwCsX3ycyfivppFfJe9pf4VmnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28939" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28938">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEWI_5lx9SV2iNYsHqMFBJNmrW-GQZOGkrceumk6Eo4oj6vjrjR2yA2awMGsjRwnKW3WD13PZ2NUtJOfgjtslb_qPn9FReAEtehexXSV29iTQGdfgNtAaHfsjECwogqRBB1I709W1o_Q8PT1M-mjUvHXD27tM20AD3HtoOw71wau3NJCdNnHBUVRBx30685mxhuL6UGVbmtUl_AHBI_yXF3liYkNnA3zzKQYFpsBuELYiQygxwESgSuaiqTo2fwOMrur-pT5Onq_FU35JR_iRmy6caxSD1wcArrHgiDZwsXfKbA4GiUNR-SSrXVPA5P2e2fgnZehjXnzA_i5ucUB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ستاره آلبانیایی بازی رو مساوی کرد؛ گل اول استقلال به‌پرسپولیس‌توسط‌یاسر آسانی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28938" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28937">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=LBS4guYd3sBszVs4tKqr4y6frnsyfVrL2wnu7Q4L_MxzfFuiCCSp-fcsJj5e5DUBjnLMId3yc9TALoKwx6lXk27kqM98OUqHe1ITj3TfwH6aL60S-FzZXNHVQUdGFZ6YthbDI7Qjk8jV3OwCmzsFKDX1R9lSOYpHPxr-D90pxEremazwByQfsQtNpgBVtgUxPbeLl_K7Pha-2M1OTBc8XkRK4aLktCFge4AqbtGsNcfJ2J8TKHwG4wuLeyNowP4VPD1kb_2ad77yoEPAi8_IVzvCRk5J5NOm8SO5gR5bapEdly-U3TFRow3DoJBai19-IqOZJQyUQTl8iS6nlWiArA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=LBS4guYd3sBszVs4tKqr4y6frnsyfVrL2wnu7Q4L_MxzfFuiCCSp-fcsJj5e5DUBjnLMId3yc9TALoKwx6lXk27kqM98OUqHe1ITj3TfwH6aL60S-FzZXNHVQUdGFZ6YthbDI7Qjk8jV3OwCmzsFKDX1R9lSOYpHPxr-D90pxEremazwByQfsQtNpgBVtgUxPbeLl_K7Pha-2M1OTBc8XkRK4aLktCFge4AqbtGsNcfJ2J8TKHwG4wuLeyNowP4VPD1kb_2ad77yoEPAi8_IVzvCRk5J5NOm8SO5gR5bapEdly-U3TFRow3DoJBai19-IqOZJQyUQTl8iS6nlWiArA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دروازه آبی‌ها بعد چهار بازی باز شد؛ گل اول پرسپولیس به استقلال توسط محبی در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28937" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28936">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=tYs8IApPojuL6tcrJe0_SBwp_zPXMltXnrjNUwEC5j1NqASAf-dibEC_mhXZtsH4q1jC-rqUbjWsnI7aHdbncPe_2Gn0DSsbvZGko1h_8LKR6oOR09Nrcu1ah3O5cFo-tGMZ9-nGnxfnH-8llGyH7Am-5pUa0wWtzaOPeY-MttPIzDgj5-iTf8gyP_P1T-KGw4n3sb7F0gHZSdnaP_uU9h4jN9bz6h_sg_luC46NTZqsi4GbuNw2nTHx9bX75aMZD7oSNKo2XiOhbnmT4d5AuelAAfiiM_mkY3I3MiXjmRkFsviNkrsgAdK2mhYIcOEzz29fJ6IT7Yj2u6HT0Exbrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=tYs8IApPojuL6tcrJe0_SBwp_zPXMltXnrjNUwEC5j1NqASAf-dibEC_mhXZtsH4q1jC-rqUbjWsnI7aHdbncPe_2Gn0DSsbvZGko1h_8LKR6oOR09Nrcu1ah3O5cFo-tGMZ9-nGnxfnH-8llGyH7Am-5pUa0wWtzaOPeY-MttPIzDgj5-iTf8gyP_P1T-KGw4n3sb7F0gHZSdnaP_uU9h4jN9bz6h_sg_luC46NTZqsi4GbuNw2nTHx9bX75aMZD7oSNKo2XiOhbnmT4d5AuelAAfiiM_mkY3I3MiXjmRkFsviNkrsgAdK2mhYIcOEzz29fJ6IT7Yj2u6HT0Exbrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28936" target="_blank">📅 20:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28935">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=YrX63rn5BSIImYoL6Suaxq6JMoUk3_gt02FXMPJnp_Sk9vvxWZKnLbpk5kXsOuJ6f9GnPZ0IPZ35QMOSZRsQnNFOdo9Dklp95E2GDgb-n2s7OzGgo7BMbxwKBYhwePCnF2xd5AY5oZkc7Pc9gA0SHscglsPdPEF-shpjWZFVZp9LuGo53m9rls6D01udcoZkCkBM8jXcleLjSZx-U1ROigR8HTjXuJTZ-9M-t9-HTQELxVIFG0PufkY_dSeJ1tlpryz46Nh5F6Rp1LTu_EIayoSTJTbYnP__V2eMFGcUtchKe-URZvHTR2XvDlUZbC44c1WzqvSi2cfJw4oX9xnLYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=YrX63rn5BSIImYoL6Suaxq6JMoUk3_gt02FXMPJnp_Sk9vvxWZKnLbpk5kXsOuJ6f9GnPZ0IPZ35QMOSZRsQnNFOdo9Dklp95E2GDgb-n2s7OzGgo7BMbxwKBYhwePCnF2xd5AY5oZkc7Pc9gA0SHscglsPdPEF-shpjWZFVZp9LuGo53m9rls6D01udcoZkCkBM8jXcleLjSZx-U1ROigR8HTjXuJTZ-9M-t9-HTQELxVIFG0PufkY_dSeJ1tlpryz46Nh5F6Rp1LTu_EIayoSTJTbYnP__V2eMFGcUtchKe-URZvHTR2XvDlUZbC44c1WzqvSi2cfJw4oX9xnLYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشید اسماعیلی هافبک تهاجمی سابق استقلال با این‌گل دیدنی‌اش در دقیقه 90+8 سه امتیاز ارزشمند رو برای ذوب‌آهنی‌ها دربازی با پیکان به ارمغان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28935" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28934">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3eYAdnsBLaX9YXLPsl12E6_ECd2lVx_Y_O_8slC0BvO2md9bFYKWUWUy1o1yEFpUtmOu9xSlZqyGJ8s2be2Ik21AUxS0XiFII_3-TWjZ3w2NevaSHq4w1oemkJ3JsTaEi3BhISlGfXCgtKIaYwYziHuG8nmupn8oLdcJ_TKB_W3kEbqNaik4LDCu0nl0jKdcUwwf-Y9ZreEyNs-jBv--GXjmJdikZL7HGIjv7_UxOHKmpT1jJcur94ww5wwwuqEho-Qn_DrC9dkvAPF-iI0gV-cZ1o_r_afb2CYvr0TrC27CNXZKsEsi0_QtMPHQPzlnmf2uncNRHkvjTB1f1v1dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28934" target="_blank">📅 20:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28933">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOuynh2glOJJVVNdEPitQzdPBrET7uK3l9bxevBdl7uv2RfJYc_0skLXQzexFeCYS0tpfLpATYyi8oQ_g1bMPvF_vvyBJnhvKbA-2-97LMz34C-oe5kYYNaOxAMIAOjFR1L8bj1qsBbY9VSERP1ZDYdY0jNukcS_t6gMJC8mVDZGpi0p3iX5FVMeCor3ZF5W74IBLbNrm_HWLLp8SEw9WXztBctGr3wzjqcX22CUvY_8_OcJk3eRgt1WcegGvoCnLDqExrmXm1p-pl2e7dtiNZl7QZSCmMI5w7hBKnoYv0sDjoWaufb1EYgqIIZMjernZ2-ZbE0quz_PbImIOaPJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/28933" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28932">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAYKbQj3g5M4AWKFtG70z1KBCP5rbMkcfvuL4XyKAaUibtPoiiebkEZ6K21FhyX80Syu-aVPBzrwUFnsPqa0j863yxRZq5L-WhTwW1EO4-FBrjHyq9FE1Zrrp6MftIV3m5W_aTnhPuOsBeDJkb9--FmqT6tpHzsZeGnVjv5YOUpQRV8elhLjcRv7fk9EgroYDwkoT_Nr3pt829abX06O2lxKMQDhe3AvOX8Ig4zDLi-32fTO3fZrqQMK19-EFgnmbCqNODuDV5g38aMAgQou3QL_qm9qznh0t4963FW-gzXk-gfQC1jx1MaKgdy8TEUob7aJFSZmEkQ5ZkB5Db1vqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28932" target="_blank">📅 19:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28931">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=s6iIsZNtQyTnoPRCbOA9FYFJB0ii6y2rW9AKGcmBhbtL4nQhawrtxa83hgNThP2USAOCrg-sp3-pbbvdiStuB3Ccf5atyFFG-UYxJhjuwcqyh8v0eeqKry5KCq4_Fnt1elSKkhugr9ddpONjKNf43cqDeUnA5S_cXMlaEaSmutSGOIjiPyjSfyYYp-KZdGxt7gtZFRnLVUIqaXuYSx4wQt7zwVAC80BETLoK59M5rodH1OrVj2cR2-ni7g-xmMXDtQ1KZPc-ovzPU6IR_D92TMWyUk3Zrw7y_c1yr9jB5tau3m39gCdnPpLHz7jfPkG3HOkjNO8c0Kg6zwBrU5R89w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=s6iIsZNtQyTnoPRCbOA9FYFJB0ii6y2rW9AKGcmBhbtL4nQhawrtxa83hgNThP2USAOCrg-sp3-pbbvdiStuB3Ccf5atyFFG-UYxJhjuwcqyh8v0eeqKry5KCq4_Fnt1elSKkhugr9ddpONjKNf43cqDeUnA5S_cXMlaEaSmutSGOIjiPyjSfyYYp-KZdGxt7gtZFRnLVUIqaXuYSx4wQt7zwVAC80BETLoK59M5rodH1OrVj2cR2-ni7g-xmMXDtQ1KZPc-ovzPU6IR_D92TMWyUk3Zrw7y_c1yr9jB5tau3m39gCdnPpLHz7jfPkG3HOkjNO8c0Kg6zwBrU5R89w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره سیروس دین محمدی از بیخوابی در شب قبل دربی و گرفتگی عضله در دقایق ابتدایی دربی. ماساژ درمانی؛ جان هرکی دوست داری ول کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28931" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28930">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMEnAmcUcPswiMfdGLPcUiwPzY6goccP-khZk1BSO86gbNdvXDRS_KzoMinkAhoLDMFvBYESbrXVshp9fCNDOkjR59YaFuNz5XNZZjx9eMYKhFTDAGjHpy4ePee8Sl740-LJ_FHNtcftTCAxHKFYoDmATixDk0lffNFL2qqHiSag33k6jsbwIfTa81vRsEkfU_YSZtizaXayhHZM71peJU4p17hkKv5iXcGkyyRK4q8NtgvI5p7cz4TyH-o_9Dqs3GnPDYrKMZDdpoLhQEpLFQLBnIsvXn4rzkopnxpVRCWwQLhJard_GnCIxbEtYylqjs0EWtnE5HildQ9e5WpUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست کامل بازیکنان اصلی و ذخیره دو تیم پرسپولیس
🆚
استقلال در هفته پنجم لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/28930" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28928">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amDSf9_FIBNBQbSUW5M9QcBOriWIk_AjNqdGNkyHIRFR9k-tFILrKAOgY8Xo5WjBlpr5Zv1BY5ksQ7nNJ85_m2csclpOtBOTf6Tj9mZSSf_D1J9lNBndrwZypcb-Qu43Jig5xcxVv-qWoGtBmpNFnIsHVrnL0np3UqmNNOrjBvjdWyqsHQ7TB2j7d7k2F_tDsPv7bQuthTqKTOV04xvYXstG92jWcOS7yjBstaWcvi6c3eCwEVtuULZ6vHb9sUdAmtyy3Wpj8ox8K9epDfZntKAKkud7EwHgQO9-QZqwyBEPkEUmNlm91ftjniQ-6qFA9Lx52K7qk3AGb0BU9vGG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28928" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28926">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J9Jqo_m6tJZ5ul-_AKELKqwqpTW6uELZZ4HYNPlFM8yz4kodhNGemkMZXW2cAo1mzFJcI-_W_QPmDigpXaNLWFzMOi2QTAnp364maCJFhSzX5oyNcqJ61AYI1LIIRkQ2O2fhqmM-l2Iz33FLOU1-AzSZe3Z5XvKiC_-7FPCFnXio2FOhW3M4C2loUjNk-MuVSczstFJlciFrvhf5wDcpWTVBXdkVhu6vcZNBsXZfxLsVybwq4bB_ajm5HNPpaU71fS9A8sVoRPx9wEVQ6pns8UtqNZjHJB1hq40WINGfmwcQuuoS4-GlAxZyUBNOjyk2z7NpSJwSWsYGFYCEnt_sTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKoMVhGmzvSaGT7oMol4Vd3EXbye5zUrF-yqTgRDmtyBu2WawQxNgebsoK4-TOIDh78D2yFN2CuEddL7rg0PBLGxnYwFiaSamh4VTzsnkDVEEK33RKRICUgeS-awqKprjfJ7HcdRptxRtsaSoF81NifOpOnvQYigwgVMs-Y7lEWHTgt7o0QD_gj_mdci8JxfnwJ10UHYZPElrOVNMk23YxLymyo1_3wqtEoswFxRFKwWF0PIB04AknIRskD3KPmrRDCDQJHNp0d5iZpe8beKgnx_9z_9Z1qJQgFu1GN4fBi3wwam3d8D7N4kkB-gsMrHA0SqAaTWPUO9gaTRJd1V-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28926" target="_blank">📅 18:28 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
