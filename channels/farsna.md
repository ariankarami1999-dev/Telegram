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
<img src="https://cdn4.telesco.pe/file/ouquaWHB3DBYjZAOPjNOk-eGU45xnRTuqpdNHtRoPeu-4L4BcLctl8Gbw7MQBj9cHX8Ua5aCa9JrqHQFUIPOsXZD7ncSouyUhi2HbtgDUt9HMH6ad_RSwVqnIj2kT-AOkMvkMo9oO_SKr9ZmaSKyw_elSW_AIYwzzJFeCTiPSPxSyf7Mt1cB_4kspi3kPf4ry75ejHCmJYnGuW5Q8Pv8DaU8eUf1Nwc_W3cGxsHh7NEEyJl-2qLooy_nDTXBDzL3jXODjaNEWXBWAvkgnpxuHieX_9CVbeSRqG-VOEMQ6NvYynPYA6zc0zNEmv0Xf86TU0SsYk5DSKvaqyIJ2XQnUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 18:20:19</div>
<hr>

<div class="tg-post" id="msg-455520">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VjsTeauU4LOp2artPma5txyKQuQ4Pici7jTKVO6LfOfdIETMo81mga9KNEhbSZAl-Sx2_Mbw8VkO3Vdk05WGoP6JdS6G-1Db714sAFPL880Nq7nV5bEJ12AmonKstnfWWdp7kv3LG_IHlAs6cBmCawDeTSXZd5AyvS4dMxeqYanFZUqAoCJDU1S-ATeXUEdq8Q6Ko8bgfp0EUj7JPMzeo_wAfoCQuFxgc0CMN5d-OjXEMDN8xw-iWYBQl156t6xfaE6A1nBHux1D2e6D6OUd7IDSmMMPFmXGc9ce45jp1o-E8bMurXzfqFBIRwOUPmNkR2VxnN68alEWoXUkHGl6ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAdzvkWI0Kh8Dy8K6vnTqwmCPc2pihbVaVBIsSojxEkFEC79o41eUjxv2WNr6wNG9_tjkrFN-nD2Y6CDjvOh-iatTK-flxte7cyNZT8MDHW0qkVMKeZegh3xQqU0p_SIkpBD9VH9he0rc8IfxnxrvqNGMWgMMjPpMHUGefBx_1wuhAh1tuAuMwuUF0PugFt9z802KOjQjBbpTFOVrX97U2-V6gGKQlvq1vKwXJn3vbGm7AZh7ZJ-qhHBa3XjS-6P1gpwc75iD1AOhbft6ogY-gvCyyohXHK86bpLFmyPh5O_W26dXeAVOJCPtRkJ44LPfv7S0U5LealYujp8hhdDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTKA_XnDwQ43wk3MOcvQW1AwauJqdihaZ5VCKgFyifse4hrkznKHsyn5Lp5g6eZ9T_lYsi90jbJQU5GqCTktxq1t0nU4QUQ9Gfywyd7hmENGIIVCZFcydeF3dR-aihoWtNQG6SVQgxX0qPTFs9ZJPyljt9zDrMwou3UUsY2ByYK2QzikO49ZNb5ygAxt5xzGMVQYgPkN3MOxiSBBnajq3dJCTvSYhnGI152iuUSZY2-K_p5YMZKYL6EMdE3rZUvm1jdtEyRAIS46uaFDuZ6bBMpvtRQJTPmIHzhY9xgyQ-e8mhl0UysJbkvsJoJGpA3xl7Pl7khFOGhpU3nc7PC3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fk-2yPG3LgSWChg49peMuQ_F5OKCLiAjiR1Az3ezM0bbqfiXfvP1BVoL7EDpg0zkaL6gDM6AmucbezuiXm6wsCk0sexy9eL2hnDKjnSNzW7pIjtOY4g9sHweo_Owg0sSdVJgPQeiuq4oOh4eBR_5lHTuQeo3nQ_z4gnu5X5sDtyiLor1nmACJVEBWUfQUly73j-04A9jumAQuH_OW4fo4J2ZQo35PGNgszAsG2js3nE81kWK6TnpGiza9LG6shdVX-vwPWfhajyiLy2nk2n87y4yTre5H2_uRv12ehxfq4acXyvdMoc5zmJ-X9SbcTdvmemlCnBOyd5wVgG2m9OBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJGlK2OZpMONkXrA9z0GIb7QI0GZmOVz1BUyKRrg85F2Z6C6bzRB_JZ93kZ1az3dSYUTD8p1lNy-4KiyBZSl427IZDycsvlnq0Kcu9DOR1XD3PyU7cIjAs2YuoljKqryqTDLWBZP9TQ2mKgT2AMdY8yOkNbL6fZG-Y3-3jnvZyPAysxxTw1o8E2RAXbU_F26JGq_TKEps---EjtHyWkx4btHqRm_DyEjLee5A-UQB8rr76XpH06XGAI7alu5HTEZVnT9VjEXpf9aEVV4IM3xUO-ymaZbyESGe6Cvlk1ntE08kblx3YSc3Oyxmoqz69cG73ap1dh3Mh0oZqho06tydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cg-OduErap5xCKTNqHr0BHtflNCj-BmJZcJmqvH9gH9A5AalWFTfq0NNpQv3TcboyOOJL2OIG9zBefIipScRk0alrwMMdedTQLTrT8PBY0rlNaqn5JK-Rmp5xc-fu_zqmA2S7KjXZ7dP-V8WjQM8gsw2keHs8IovPM-zMpEr78hLuoYu3gn0Z2RZVAzmle_dI9FqtXfLxc637yvFx1_kYUzurTWEB24ayKXCmKzXQmtegA9B1wFWMH_IChslv2piyFJebhbK2tgjFcPeBPDQZ6ko4rGdzRWj878DpUGrvulYYGt8a4aQGHZDR3fMIRATZX0MFrm1EZ9yw7oTkfZrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UeW9MjsvE9iuGtviiRv3Sf-iCzN7FlFx0WuyU18zieuCvki8Grr2LV0zaEtQcmGjR5dDog9D7xZo58z7XLGmzZnRXaILlhCLUMvCFpvQZ2P_cpO5JWeGO1tnFitu-XguBcijhm190bboQjZiMUVU82g12dBxg7H7Y7v2gpH6rC8IzfmExadkvJJUTAGDbp9dFRnBaYL6ScrCtQ65vR3H_3sMeYv_Jg7uG5hycecXq7l0lzdclRQyJTbO3lCCmmXliJ3STsoPLq6RnKCjfkVYaT_iSU2ENCDMMuTQAQ1W3RQ7wJXnChS1vsNbTQr1chmkY6LFiLFf2AI5vTWVpFACTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تفاهم‌نامهٔ همکاری بین وزارت بهداشت و وزارت خارجه برای بازسازی زیرساخت‌های آسیب‌دیده در جنگ، امروز به‌امضا رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 710 · <a href="https://t.me/farsna/455520" target="_blank">📅 18:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455519">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDBzSX09JllCtfCeWtmIKpkomZjX_N-HEPzEnLfpNurWTAVN1pw9P0Etrd9rCvUORk9UPvmeIvjRyfJdE9osbxhk08VbXIUHZiR7qOm7XSZ6V-LRinRV0Lv_WZE9FA-d5dCBVOTSAw8TzwR-ujYrEbku3X_aaJZvWhfu4EEfRbzeM8dmSBhudWNhJ9Kbqxl1j_HEHTRnnbUGERqP4d5SIejZzyTHj65a0xF4RBf4WEo-u9G7MYgEvA0aVa8QNeAv8uqkfj-vSeOSpX-829jbCVabUp9riEQKs86pt70UOe_l7KXGUPZRAaiwkQd8cWcsp4M1vY3GC1i5RLhEVSlFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر انقلاب از سرلشکر عبداللهی، رئیس جدید ستادکل نیروهای مسلح چه مطالباتی دارند؟
🔸
ارتقای توانمندی و آمادگی‌های همه‌جانبه و روزآمد دفاعی-امنیتی نیروهای مسلح و بسیج مردمی
🔸
فراهم‌سازی امکان پاسخگویی به‌موقع، انقلابی و مؤثر به هر سطح و نوع از تهدیدات متعارف و…</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/farsna/455519" target="_blank">📅 18:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBiUEmgOq6tXDHVXJBLeOY2Y7Sdf3XsKFAAl8LQHjMfb_y7bIcmHghGWR6-k6BZdHc-xWCHTPYPlYzpGa2CjSY96PS-tLeQP_FsGbp1jRGhz3As0nd8xJm8GnFtDhTADVfWKqEaEYo4Oo8Kx_C7rdRqmeYt2gRYRLU58iTvwXm0Nb7RI1Ywl2yx_PfZW02bS2GJKJSVJeb47gbTO-DKfr7YVTjciaWLGO_pG_xg9Tzsu0BVRlVEOkScHnmAd8MCwZySciGaG7su7c1bqFVvbtmqe13yq9BKHW5cKfIcD3W5ftVbVTd0RflMO8u6BeWNjsUYde_iU_n6EJcyW9Z0IjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrWi_IWTlwedBz6UbIcAp5YqXAXL-jm6cCCYWDH14eJOzoq1YaJGFr71cJJURSTuqJFlFZhep173vMjPOe0Jdz9kjFDn1usRaXRT3i4fPayo0A_9OKgoiQzaj9fwyMMZDtzekOSKivPgZpi8q8b28DOK8_fBxUcAHfmOfRIcnYbLeHW9xGG-L2SU9GLfAJYmIdrSH3gSEQQEf5WfdHCCqItb2_TMYs4XcVl5HDpRhPvFPtf1jZhOCk0Zns6l89tRpmzBgmfbcYNxBQR_ZLLVB7DoQtvTteGbSislzzMG0AKzhgMCOnaQKOd60M3nNsxS_37j5g0IdnhV_kUddTFoYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر کشور پاکستان با عراقچی دیدار کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/farsna/455517" target="_blank">📅 17:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455516">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdf3c21c13.mp4?token=lI_9EkdMK6XJt7lXobMDPFr89sOXWc6HawNIMb8I6hu1HH_TD79ZDJg7EFgnhWI2eMK0uFXA7uOaCXlXDm-bMGGoSqWbQgkFcWSbya0Z1dWA4xNvYqk0uqoFU-PHSZPEPgz9DOgl9d2RWZspvfTOTuAYnQTPHQyAUhGPAFVktQWpvY3If40JYIqVKW88PLPjGYKIzxcBydAzGvphjiVxkUe3KASkSacvkh7J6SxmQME27RLk_4zxSbBPA0ZbHXuwgTUq5lnXjnZqAkSL5jFOo2YV_x1ux5zrc_zJOXrqSXbvF37SKNfT3uGsOBhbx6vUGW6p_BW5SEfhlIxxK-eaxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdf3c21c13.mp4?token=lI_9EkdMK6XJt7lXobMDPFr89sOXWc6HawNIMb8I6hu1HH_TD79ZDJg7EFgnhWI2eMK0uFXA7uOaCXlXDm-bMGGoSqWbQgkFcWSbya0Z1dWA4xNvYqk0uqoFU-PHSZPEPgz9DOgl9d2RWZspvfTOTuAYnQTPHQyAUhGPAFVktQWpvY3If40JYIqVKW88PLPjGYKIzxcBydAzGvphjiVxkUe3KASkSacvkh7J6SxmQME27RLk_4zxSbBPA0ZbHXuwgTUq5lnXjnZqAkSL5jFOo2YV_x1ux5zrc_zJOXrqSXbvF37SKNfT3uGsOBhbx6vUGW6p_BW5SEfhlIxxK-eaxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بر اثر زلزلۀ ۷.۴ ریشتری غرب کلمبیا، تاکنون دست‌کم ۱۳۲ نفر جان باخته و ۵۷۰ نفر مجروح شده‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/455516" target="_blank">📅 17:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455515">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdxz60hAXMNBybkbkMaQMWIEOoeydVc4r5ICO6CZVFTjmU1TeRJXXQW90FSeWFALoYwuVteV1MfXM97M0Pp28US4lTsQV4TcvuGyuNQdh46QgPfLgBL5NbBKIMp8VrZVnfvKHSsVm9seFCwyvfWgthtnhHQW4s-0938ucS5yWEeMSZKt94lCg_KeU8jgXv6Sx6N3PqQuM3DljMbjWbS8qnU75UDUz9yVm-dxiopLaXsU-OYUqvl7Ft6-OPCmHi3cmZ_vGtEeEn3TDNFAX2IIuUZGNqhOuLjd9o9hmgpRg4lVRXb58DWg7o278f7JLTEpVwDYqzu5OCdBz8oU2gODxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان برای دیدار با همتای ایرانی خود امروز وارد تهران خواهد شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/455515" target="_blank">📅 16:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455514">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQ3IJT-_zXy6ee847MiVHTR6tc2cjRTgMv2_hDgRi2a6zlzvfQvWzoALrsbDn86ZRUeLw0IC2SPtUmtx-FwCFfDJ8PTtAp8M6n8u_VSciMrK_lkYcTh6ooRYewdL0ojlJMrdd3pRFQ3gJ36uzgKVV24ufP3Tw2vsUBk2TiALqwgQE_P6iNXPmjBZx1GZKdZoTcTLjCxjByyXurQO4Ap0wVjdp87HxMLQctd3xNYWuAUjh3DElRtExiqPdi2hjlLKe3xpLqndczzaaEH71E_R5bZopFfk1a2Ms7t1_TBV4m2bsnTXOo56BOLuZ5Zw58Rc6XcCJDPrFmEb2sgIMUySsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌ بانک مرکزی برای شرکت در اجلاس بریکس عازم هند شد
@Farsna</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/455514" target="_blank">📅 16:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455513">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY3ahZghFS463bmCNbhu8EzR7z9HzTsykxg2WxzPizcuHqCTZvsu-1thHCBePuYOZi2NbeDAY8yslcG5xPYx2LXv9LCx0fXhge0uNI9ngkhEVqr5XKA0B7zpkfdzdDZ4Qz5IrhDsYVp63Gd6PaxZZwN4AZIw6WziuOWjFhWxgpxVzc0BGEsf8PqfdLzp-ARz-cDZr3ipNVpOEjrDviyMtB0DcnoE2GC-f3h7x2H-LvE0yEPaCqNdpHQzi4jJLlUzUPN1d6Qc09dGIzh6crTfJSWKkEmikiou_JfBxTnvgw2K_rErhK1pmapMXtuid76fjAXEsxiGcPMsU3zY_34ERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار ابن‌الرضا: زیر بار حرف زور نمی‌رویم
🔹
سرپرست وزارت دفاع در گفت‌وگوی تلفنی با وزیر دفاع مالزی: ایران همواره خواهان برقراری صلح و ثبات در منطقه بوده، اما این صلح نباید به معنای پذیرش خواسته‌های نامشروع و تحمیل ارادهٔ طرف مقابل باشد.
🔹
ملت ایران اجازه نخواهد داد دستاوردهای این مقاومت افتخارآمیز با فشار و حرف زور نادیده گرفته شود.
🔹
فتنهٔ اصلی در منطقه و جهان اسلام، رژیم صهیونیستی است و تداوم جنایات و تجاوزات این رژیم یکی از عوامل اصلی بی‌ثباتی و ناامنی در منطقه به شمار می‌رود.
🔹
وزیر دفاع مالزی هم در این گفت‌وگو گفت: مالزی در کنار ایران برای کمک به برقراری صلح و امنیت جهانی قرار دارد و بر توسعهٔ همکاری میان ۲ کشور تأکید می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/455513" target="_blank">📅 16:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455512">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTuG8wkMYCMfBnff9gAczd6fA_l9Cch4ZA47g5Eq17hiyPEwdXRQz8iGXJPVnZjsYSwK_PsyrHw19SDt7oPI47UaKygOQhRFEX6835ZH5DWgqiFD8WLllqNyy0JU7ok5ehjfxHpd8ABoXrLEA-Py9XQIe2yU_Ri921EIImNUEM2rrl3zLq_gMLOZzQuW5eKfKt6rg92HiLTKcHyNmhd38hLFOq2hXpzMFBa4iFIk0I-_gQvH2Vv_3kDeztIyZBCyIcw7BZsGsxtQ3KwUZfeCnbS7kdUGcYflqinRkXNlRjDfQFxJ_XICzvnDJa4DZSdM97cdRn6TsWnMpM8OKB7H1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان برای دیدار با همتای ایرانی خود امروز وارد تهران خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/455512" target="_blank">📅 16:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455511">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-n6tXyaPC8IxiKmYhfZgPlYuNfuGWBGFE22p-0YGLWaLXMDBIwfm5pXRJwiG-6pzjBFj71ZcEUz7rxruCONzw3Aec-k3f_LhT-G70SE8QAs1hrijV9BtxrAjqzSjl3AjigeWu2PLwPXebzeyM_gNCnAZXKIsy3osnDBLi6jn_Tc6Z_yYWg6M4DiUv_rjRt7ZDR36dOELt9VqxLVQ9FEc_0H-vSoqCmghS-7D2yewRrbyNcQ-4ke5KJN9hRg9bcjvmcWkGHIH4iA6Jrj_O8T72Bt3n7hnbjsLRRsqIuCLBHCoJXaP_TiJTPgK7zcJ73iWkLy7FNX0xth60qYajPZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر کار: نقص اطلاعات فراجا، کالابرگ برخی افراد را قطع کرد
🔹
پیگیری خبرنگار فارس از وزارت رفاه نشان می‌دهد کالابرگ برخی افراد حاضر در کشور به‌‌دلیل ثبت‌نشدن اطلاعات ورود در سامانه فراجا متوقف شده و وزارت رفاه پیگیر اصلاح این اطلاعات است.
🔹
معاون وزیر رفاه گفت:‌ افرادی که صرفاً به عراق سفر کرده‌اند و پس‌از آن به کشور بازگشته‌اند و به کشور دیگری سفر نکرده‌اند، اطلاعات لازم از سوی فراجا ارائه می‌شود تا از فهرست افراد مشکوک به اقامت خارج از کشور خارج شوند و کالابرگ آنها مجدداً برقرار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/455511" target="_blank">📅 16:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455510">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
محسن رضایی دبیر شورای‌عالی امنیت ملی شد
🔹
معاون ارتباطات دفتر رئیس جمهور: با حکم رئیس‌جمهور، محسن رضایی به‌عنوان دبیر شورای عالی امنیت ملی منصوب شد. @Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/455510" target="_blank">📅 16:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455509">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw6HjbiNHK6xFw_4lfZqOSxhtNvy46FKiTkbLzL1w4OBPJFO2neqgl5DJs-eymsRsfYEAF4aOkyPTAo6Dwe0jRsOkVK4DELXlsggk9q36m6tAypJcivephOCC37hhhYlTZ4aN3lIw5xx08e507O_Xv1MZhPAuPfS39ZWaGu-qHBF7GeODiCxU4klq2L837eohLuGF_xpWu5BGa38TvgDrXyoucDWP29FsqGHjJ9L92Cij8IMKNp0dvX7qf60N4pzza8CWCLB2-EFVw_9ch6ewO7RPOJanCdZ5o6gB6ANCcU57XE2hHc63vmPp3rK75FMPOoz_StG2yquakH3gkfY-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار بوشهر برکنار شد
🔹
اعضای شورای شهر بوشهر با رأی به استیضاح شهردار، به فعالیت حسین حیدری در شهرداری پایان دادند. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/455509" target="_blank">📅 15:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455508">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🖼
پزشکیان در پیام‌های جداگانه انتصاب رئیس و جانشین ستادکل نیروهای مسلح، فرمانده و جانشین فرمانده کل سپاه، فرمانده نیروی دریایی سپاه و رئیس سازمان بسیج را  تبریک گفت.  @Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/455508" target="_blank">📅 15:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455507">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMKgqUy7SRwy5Fs2j0EnMSxbyaCUIxFMqhqwpi-LAGH4MiGwLaqQcgtR2pjNIk_IjiSI0awWNQ6WDZFEFINUKVW3SHnsL0JbaAVHppcuNcyCEwvtHjgE6pku9lnZS5f2kY_B-ncpFLwTx2BggUwPaB3pMNcE39xpUMBxJ9cF55tHUrW6bkQ1pHVaXcPluJFyAoYZMPxOfWEOqUPbjlnNO1C8d57D_rEArsRF1efNBHmOZyACumjUnWuqnFrrZw4GVK109Flyz3jYq0x8YifPTMvY1LWV6CKDXA9wKbPXBAKkswHE6dasoTgdx1B9dFL3vflZF42vO9d7uEwhRTNhyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاود روی متن‌هایش ردپای نامرئی می‌گذارد
🔹
آنتروپیک با افزودن یک واترمارک نامرئی به متن‌های تولیدشده با کلاود، راه تازه‌ای برای شناسایی محتوای هوش مصنوعی ایجاد کرده است؛ نشانه‌ای که در ظاهر متن دیده نمی‌شود و هنگام خواندن یا ویرایش آن، تفاوتی با یک نوشته عادی ندارد.
🔹
نکته مهم این است که این واترمارک هنگام کپی‌کردن متن نیز همراه آن باقی می‌ماند و به این ترتیب همواره قابل تشخیص خواهد بود که آن متن توسط هوش‌مصنوعی نوشته شده است.
🔹
مدل‌های کلاود که از ۲ اوت(۱۱مرداد) عرضه شده‌اند، از ابتدا به واترمارک نامرئی مجهزند و آنتروپیک در حال اضافه‌کردن این قابلیت به مدل‌های قدیمی‌تر است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/farsna/455507" target="_blank">📅 15:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455505">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9bUE2P4jdVh-sSPQ4G0P1z_KvXzVn0-KdykhHFyCOEFqUlHfNJDpp3WNoTSpBTSblqnS7GldGVfYuBR2N43SQuPGkqtWHUId66YktgpVLl5yMX1D2eyJu4EP8_Wj-whNrwZOfIoRlMMkmq39K5pxKPMH-mWHDEKApvEBJfIUQHIV0X6hDpKPmT6afdc1N9I8UpYXk_1JyjcSvi97okz0qJTG0htLYAnusaP1vit_aAPSibV8eAbAwN9E1UmZ3cjd6xbaOb1tGMZADYGjX6DWaiHQWUcbHA-5KM3B0bX8lrLchFRWkKhbfrUz-U1VN1wAW_EpeUR38uJflEQsOwJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
حملهٔ موشکی به یک کشتی سعودی دیگر در باب‌المندب
🔹
منابع خبری گزارش دادند، یک کشتی تجاری دیگر متعلق به عربستان امروز در تنگهٔ باب‌المندب هدف حملهٔ موشکی قرار گرفتند.
🔸
این برای نخستین‌بار است که ۲ کشتی در فاصلهٔ زمانی تنها ۲ ساعت از یکدیگر در دریای سرخ…</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/farsna/455505" target="_blank">📅 15:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455504">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd10ae97a.mp4?token=tVXmgWm5OHkYHcY_SUvyeWr5oeN7u5Pod34Cqe9ic0i0WNmu3n5RB_jkgDyjBq01Wu3uXiDsFgFKTI1TBuVLodHuedag0Atdxux42XvjfdhfFofgqOik-GCKdOfksk0U2aQ2pbh3UiHCG63U6Yp__3MZEDxal4_5hgZrEdbaktUDa0Qn3zrZCbx_f-JUcXwehNBvrrIPkDXA1_QLi3VjtR05nPtVNsUnyQUB1apWmPkWi-MMRI7KYNnMBnF8ejDT0gRf5RtUMnNJdHs08C7Cjd-LBiRF14j5RAlqCx6vUHJ7LYZoRSwHNg6xRcySiZMbKcF9n-0-5kyZ4Hz849i1wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd10ae97a.mp4?token=tVXmgWm5OHkYHcY_SUvyeWr5oeN7u5Pod34Cqe9ic0i0WNmu3n5RB_jkgDyjBq01Wu3uXiDsFgFKTI1TBuVLodHuedag0Atdxux42XvjfdhfFofgqOik-GCKdOfksk0U2aQ2pbh3UiHCG63U6Yp__3MZEDxal4_5hgZrEdbaktUDa0Qn3zrZCbx_f-JUcXwehNBvrrIPkDXA1_QLi3VjtR05nPtVNsUnyQUB1apWmPkWi-MMRI7KYNnMBnF8ejDT0gRf5RtUMnNJdHs08C7Cjd-LBiRF14j5RAlqCx6vUHJ7LYZoRSwHNg6xRcySiZMbKcF9n-0-5kyZ4Hz849i1wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا محسن رضایی مسئول امنیت ملی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/455504" target="_blank">📅 15:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455503">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJHP3b2OpqOHDQdGxA5FihThXR6kiWacUFkluwRohHV2JpXbQbvLhhhBVYipPbtJeOPoXVazefqWbDMX9k7Zc4p9LKOM5Uw6gZyTcBzDAENEquJRTWWgcpbcdy3VBQp0HBTHH0t93gpTwZyRURC4FaV3EUyiCbZicB7EMJ12PlIezSmJr7dpnU8FQKWeweTx8uKW23oweOHKVrxysoUHheGQ1w8dVQeaM0LbLet1NnvWPFzhxDMpDTS5DbTCYp_ssEjF5Hcdidwu3maTrmFxTprho9pmji9nBr6iQMWNjOTLz6peX3MVfkKHeuopPIiqs9hz-LzZ63Fg9UIqJ-H7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم: کنکور سراسری در زمان مقرر برگزار می‌شود
🔹
برای برگزاری آزمون، هماهنگی‌های لازم از تأمین برق حوزه‌های امتحانی تا هماهنگی‌های امنیتی، با دستگاه‌های مختلف انجام شده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/455503" target="_blank">📅 15:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455502">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ba1afedb.mp4?token=voMW-UTlmHuY2htXSkkHYligYcg7Y1e-7VLPhHnyrbXhMCm2S94XkKIFpQpbwftdrP2Z1paYi_ulJ-c02ezmLLQPJppILes7KlBfjeeWhNi8T5EbX280gNdG21nS7cHCCnaFgVb99w8mmzkJtY_Pl4T5DF54_DQaullI60MNtoeejOKcX4rlpWlI15lFyny157_NvgjZKDeaXYpIZZfVwAMpJQok-dlaEn-FwSZFzBfsoh1o6sO3uy9xdnu15ZWR7a2O2Bu-nfaJVOyvrAQ0kRHFVZGmXuLgG8jBvuaE_EbeWMP-NOXOpdk_F17LvK5bsrVe5mOZpFa9_wMdiQ6SNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ba1afedb.mp4?token=voMW-UTlmHuY2htXSkkHYligYcg7Y1e-7VLPhHnyrbXhMCm2S94XkKIFpQpbwftdrP2Z1paYi_ulJ-c02ezmLLQPJppILes7KlBfjeeWhNi8T5EbX280gNdG21nS7cHCCnaFgVb99w8mmzkJtY_Pl4T5DF54_DQaullI60MNtoeejOKcX4rlpWlI15lFyny157_NvgjZKDeaXYpIZZfVwAMpJQok-dlaEn-FwSZFzBfsoh1o6sO3uy9xdnu15ZWR7a2O2Bu-nfaJVOyvrAQ0kRHFVZGmXuLgG8jBvuaE_EbeWMP-NOXOpdk_F17LvK5bsrVe5mOZpFa9_wMdiQ6SNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فروشگاه‌هایی که قیمت‌های قدیمی را از روی اجناس پاک می‌کنند و با قیمت جدید به مردم می‌فروشند
🔹
رئیس تعزیرات تهران: با فروشگاه‌های زنجیره‌ای که اجناس را با قیمتی بالاتر از قیمت درج‌شده بفروشند به‌شدت برخورد می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/455502" target="_blank">📅 15:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455501">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a33540e9c.mp4?token=BOxz7BVSxtCImBG0zcG3bsP8JhxQ_LFnsjACt8_FOI906mVuwgxCZ5-Mu9AnwgNb92OnYqjHT0V06PA3C97gvsGibOdNpC6pMl6-fSzZj15gnB9voj2UsIw2U6Etai0f6aTq7YIDA1n64jBfitDOlJuZlFIhuHANoyeW4pPe1qaWDkujn_YdRLFdB7U9xCiG8c6eQ8lgh4prXU3AWpNd7xI62ePHuAKYPUebxp1voM-gNz_-UyECb1CK-gyd0hSZpcRHTRMfrpBZP6UqcBmLcf0AwdsFEoIqo5UM362axoR6NcosybjGxCaR5odzFI2Jt-IrUC4dqNZdcj68Fobj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a33540e9c.mp4?token=BOxz7BVSxtCImBG0zcG3bsP8JhxQ_LFnsjACt8_FOI906mVuwgxCZ5-Mu9AnwgNb92OnYqjHT0V06PA3C97gvsGibOdNpC6pMl6-fSzZj15gnB9voj2UsIw2U6Etai0f6aTq7YIDA1n64jBfitDOlJuZlFIhuHANoyeW4pPe1qaWDkujn_YdRLFdB7U9xCiG8c6eQ8lgh4prXU3AWpNd7xI62ePHuAKYPUebxp1voM-gNz_-UyECb1CK-gyd0hSZpcRHTRMfrpBZP6UqcBmLcf0AwdsFEoIqo5UM362axoR6NcosybjGxCaR5odzFI2Jt-IrUC4dqNZdcj68Fobj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارنامۀ ترامپ بعد از بسته‌شدن تنگۀ هرمز
🔹
بنابر اعلام وزارت انرژی آمریکا ذخایر نفت استراتژیک آمریکا در این هفته ۶.۱ ملیون بشکه کاهش یافته و به کمترین مقدار در ۴۰ سال گذشته رسیده است.
🔹
همزمان قیمت نفت برنت نیز با افزایش مجدد، در آستانۀ ۹۰ دلاری شدن قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/455501" target="_blank">📅 15:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455500">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxGzqx22pesDlhZv1-xXv5YT3203Pn16c3LFj7ojqoVrPTXY_KT5N6YFg9QXOmOUz7SKhTQ4Sk_G8YDDQ-maWor8RynZVonYpBF1GTSNrIV-MVV0IJyfAXJoRjCXVA3K4-ZsXswp8ALgbyeC1DVhVwJ7aXDat3VLHZAgBmuN4gAENqtJMNdsTKDKYJufVz4icBSxJ8CXbm2uM9UCldRXD1LTY6rZ7a1sYdMRwgXyQWi9itxG5JZJHliLTWhKbUoKuFli2uxUhw-AC1XmCw7VxO1dQpeBI6NeOxySent7gZWcD3Ef-INpSx4QwZ48fNlfUrJzB7BOPWwHKBgD0zdPhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
واکنش رسانه‌های مختلف جهان به انتصابات جدید رهبر معظم انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/455500" target="_blank">📅 15:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455499">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be9d724b0.mp4?token=Bajl0hQUcZovTlsy5T0fX_9OKBkUVHKdFW1STrhuzTGhuWpClXKipHgLL2Pa2Pr97n6jjQ_J3I7745YuNd7awkh2Et3sRpU5GkoS5oinDqo5X1cinhooEFJFZp8SD1HXiPSgewAC3opaBiTclrMPTLQYEGW8l12dkTKK8ssft_k12vUtG1piIVKZPt7p1sTAlpfVWRSK72Tij4MzaWbjlsGh3n14rSa5q8KA4eEMFCR5nZND-oS-xJRpVECH3UOQfsVsNk3ywd0EE0XUthfpK1vzTI4mcfeFnBXJ0cp3Dm9odm-oU1OWR8owqQ-gdrXEL9A5JtUN5MhdtKz_oNsFTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be9d724b0.mp4?token=Bajl0hQUcZovTlsy5T0fX_9OKBkUVHKdFW1STrhuzTGhuWpClXKipHgLL2Pa2Pr97n6jjQ_J3I7745YuNd7awkh2Et3sRpU5GkoS5oinDqo5X1cinhooEFJFZp8SD1HXiPSgewAC3opaBiTclrMPTLQYEGW8l12dkTKK8ssft_k12vUtG1piIVKZPt7p1sTAlpfVWRSK72Tij4MzaWbjlsGh3n14rSa5q8KA4eEMFCR5nZND-oS-xJRpVECH3UOQfsVsNk3ywd0EE0XUthfpK1vzTI4mcfeFnBXJ0cp3Dm9odm-oU1OWR8owqQ-gdrXEL9A5JtUN5MhdtKz_oNsFTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران میدان‌دار جنگ
🔹
نیویورک‌تایمز: جنگ ۶ ماهۀ دولت ترامپ علیه ایران، بیش از آنکه به پیروزیِ راهبردی منجر شود، در مسیر یک شکست راهبردی قرار گرفته و این وضع، جایگاه نظامی و سیاسیِ واشنگتن را با تردیدهای جدی روبه‌رو کرده.
@Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/455499" target="_blank">📅 14:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455498">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd3c187fd.mp4?token=HKFR8pxUXm-fk14evtwmnrzx_U-MsY3RXI_cJ3OM_tHPh0hGI-pVyVGhwVt8Lh7JKHWlpiDkio8DBPLmiHS83ogJ5jfq566jab6xWQYNEDfv4OoPmWyBi5ddVBfzPSBW6AFE4353nUvYH6esocXERfsDkipy8hq_UjjqbrCbcPMrillQwlT3zQERGlyuUCIaUtM5WIxQ__aZtxRveac7n3aXUAn5uy0vkTSm1XguPusKsHgYXEwBI7JQaVqCrl0FwlnqmPnrd8A00W3l6AiGjYrihmFAkelqqflQBYL9BMddLAWd2COzbCOBruxn8paFG0kr4IqPmEd-68I2I__rhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd3c187fd.mp4?token=HKFR8pxUXm-fk14evtwmnrzx_U-MsY3RXI_cJ3OM_tHPh0hGI-pVyVGhwVt8Lh7JKHWlpiDkio8DBPLmiHS83ogJ5jfq566jab6xWQYNEDfv4OoPmWyBi5ddVBfzPSBW6AFE4353nUvYH6esocXERfsDkipy8hq_UjjqbrCbcPMrillQwlT3zQERGlyuUCIaUtM5WIxQ__aZtxRveac7n3aXUAn5uy0vkTSm1XguPusKsHgYXEwBI7JQaVqCrl0FwlnqmPnrd8A00W3l6AiGjYrihmFAkelqqflQBYL9BMddLAWd2COzbCOBruxn8paFG0kr4IqPmEd-68I2I__rhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رهبر انقلاب ۶ فرمانده عالی‌رتبه را منصوب کردند
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های ۶ تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند.
🔹
براساس این احکام، سردار سرلشکر…</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/455498" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455497">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a20cc9106.mp4?token=joR7joULzP4UmTKFMeHtoY9tpGFmnZH7yOKDemdvlN9zCvvCLRpMUUPOS6US6S7zbII5HAesMrphTadM6-wcLPnwRprMvb1nzNgVNq77JadKuspUQAQZo5RBEQ4FH-hdgdZ0c0mWowiLXGBT_EvoayDRj__g2pnnKXa9Qd5KD44wughvrV05zq_quQqhQ60UeSxCmlvsy334Oi9AG2F7sIefxUKbTEPaYRQFil7eS6vG_xeQkVWc7p0xh6ngk32TsUYF9u35-p5sTV8JiGh3F7QrkdhXfxuFVBnMjS9ouU_t241iA5IsGuf77dnPzS_GlECElzfYS1vChc3xUfbL5L6pqkBNikfTo2LfO3zxm4PljWiPPBz0rPoxj3wV9PmP82b41CH8Yq2-ZOTBztrtnFaTlUMsid07gMAxZJVPKW7RXL56aP7MVNBYHpw5S9SDP8J7xINrx_9QQ7-7-s2AqbeZ5MD_Bvijx9I34jp44Q4NmKYepzGNoBXWuXBZxOPxylnXBGTdHTxDeWJCmS9jo4NUK_etQJct2ufXjYNGEGpPXOF7DwuEVR4R77A8iQoATv51fJD418B8cWrAVJOMpvGY80ohULy8ggDbJxIjBWHVWbbbJ7WxiI5EFPTCF_BpCybhjc2FG0s6bzhp0MvtO2wEcQ_il_X69oLftjzjObI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a20cc9106.mp4?token=joR7joULzP4UmTKFMeHtoY9tpGFmnZH7yOKDemdvlN9zCvvCLRpMUUPOS6US6S7zbII5HAesMrphTadM6-wcLPnwRprMvb1nzNgVNq77JadKuspUQAQZo5RBEQ4FH-hdgdZ0c0mWowiLXGBT_EvoayDRj__g2pnnKXa9Qd5KD44wughvrV05zq_quQqhQ60UeSxCmlvsy334Oi9AG2F7sIefxUKbTEPaYRQFil7eS6vG_xeQkVWc7p0xh6ngk32TsUYF9u35-p5sTV8JiGh3F7QrkdhXfxuFVBnMjS9ouU_t241iA5IsGuf77dnPzS_GlECElzfYS1vChc3xUfbL5L6pqkBNikfTo2LfO3zxm4PljWiPPBz0rPoxj3wV9PmP82b41CH8Yq2-ZOTBztrtnFaTlUMsid07gMAxZJVPKW7RXL56aP7MVNBYHpw5S9SDP8J7xINrx_9QQ7-7-s2AqbeZ5MD_Bvijx9I34jp44Q4NmKYepzGNoBXWuXBZxOPxylnXBGTdHTxDeWJCmS9jo4NUK_etQJct2ufXjYNGEGpPXOF7DwuEVR4R77A8iQoATv51fJD418B8cWrAVJOMpvGY80ohULy8ggDbJxIjBWHVWbbbJ7WxiI5EFPTCF_BpCybhjc2FG0s6bzhp0MvtO2wEcQ_il_X69oLftjzjObI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باران تابستانی به کلاته‌رودبار سمنان طراوت بخشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/455497" target="_blank">📅 14:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455496">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_dA22amHhMiEfSl8yDLiXJFg03vCiZY95xVTYc1p66c_6YZs1ifBtnwHu9U6T0R2Vt5Ihun6MvcrHx6cC_pVz2O_pWj2ra4uGNlajQo9Z8_l_AhEnFVywXCTsdYnBhuTCTbNpw2GbrLyHk1tr7tZ3fvNqN_tugyl-z59AipCw3mfNozrLliJ6XbEB0Mxz87VQJLixs3KuRqDlk1O0OzOcAai-yeE36OEFGKWoxhL1PWhTCVYFN4xFgNJT9G1129azqveCH9kWiuFe2MKxNYkoHmfYTo5movlcuUDL0dBJwGBD0OCo8ty3WRfC9I5rk3wd_dj2oTB7-O9P53vuBS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فولاد مبارکه پیشتاز در تولید فولادهای پیشرفته
شرکت فولاد مبارکه با توسعه سبد محصولات خود، گام بلندی در مسیر تولید فولادهای پیشرفته و با ارزش افزوده بالا برداشته است.
بر اساس اینفوگرافیک منتشرشده، تولید فولادهای خاص در این مجموعه با هدف تأمین نیاز صنایع راهبردی از جمله خودروسازی، زیرساخت‌ها و صنعت نفت و گاز دنبال می‌شود؛ رویکردی که ضمن کاهش وابستگی به تأمین خارجی، به توسعه زنجیره تأمین و افزایش تاب‌آوری صنایع کشور کمک می‌کند.
این مسیر، بخشی از تحول فولاد مبارکه از تولید محصولات عمومی به سمت فولادهای پیشرفته و تخصصی است.
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/455496" target="_blank">📅 14:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455494">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUIswNHD4N9vREJ793pw0YLUfU8ERaQlzOJS0J272-pkOWP2R2pJgA5djzjvt-NLsUX1lRxBwN6bRI2jjSAcwFi93lw7biPdcHvpqJxvumUEl3wASjUKIE4NQ9L31sCW6XBqNHkTrYxXWvRSWG6OYifGkXwwWddHaiE_14zPjnPf8_if42cQCoZD8jMz1Bs5WwPynJSqEiKKVFJzpX4fu5y1YL-y3cmtKDfN3m2ivca4svKkQ0aRevCM1wqEOqtaFRA1iIw3PGXcYZm-WJBZMnv9Tn27GxAtBVw6jXuBvq0PCezxE-uhDFjejM5PNnZLYtPyIXSKjpOf1TvCPJBJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-ouzFdYqn9Y4LyZ1-mN7Zf5VOgTZbOU5hlAOzW42pHULk9dNb6tWk94UAJqrmM1cEAJvA0ejZItg1PJ_FSHRPgh3Sf6fbbHDPuwZx9HFdBcIXMt4k57fyNrJ44ep6bWN1kkGv8cLBghKBmXCuVvgLWL-decloY9vQ6JihUh51o_7_7DIVDdv0cF2jCM4hlQp9ZcmkN3LYjq05pNuiwjaNWVRo3grAupENVdz5aHkFe3dp_jySlWqkfzYOcKSkqWU8-8_wKgRxaSmvYxUDy0FP-qMYM_-Xh4zKjZdOT8S9Na1nlSjTffXeSvixdeyCwz4ejEWNeSfM0ybB8tmcyAJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
مدیرعامل مس ایران:
🔰
هماهنگی راهبردی شرکت ملی مس و صندوق بازنشستگی ضروری است
🔻
نشست مشترک مدیرعامل و رئیس هیئت‌مدیره مؤسسه صندوق بازنشستگی مس با مدیران عامل شرکت‌های تابعه، با هدف ابلاغ سیاست‌های کلان، تبیین الزامات حکمرانی شرکتی و تقویت هم‌افزایی راهبردی برگزار شد.
🔹
در این نشست که با حضور برخط دکتر سیدمصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، همراه بود، بر لزوم هم‌راستایی میان مؤسسه صندوق بازنشستگی مس، شرکت ملی صنایع مس ایران و شرکت‌های تابعه و همچنین ارتقای نظام‌های پایش عملکرد، شفافیت و انضباط مالی تأکید شد.
🔹
دکتر فیض با تشریح سیاست‌های شرکت ملی مس در حوزه‌های نظارتی و عملیاتی، هماهنگی استراتژیک میان مؤسسه صندوق بازنشستگی و شرکت ملی مس را ضروری و اجتناب‌ناپذیر دانست و شرکت‌های تابعه صندوق را بازوان اجرایی شرکت ملی مس و مجتمع‌های تولیدی عنوان کرد.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6Sw
@mespress_ir</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/455494" target="_blank">📅 14:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455493">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/455493" target="_blank">📅 14:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455492">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5brPlq3w9k9fVuNjbEqqPsjbK1AdO4gmqUS2SDArUtDkkdno5rECHYIlQWqmlxbqHMPK8GkyRIGf8m75VG-fxajuiZeqhjkLylloLEraawiC-c0e3CYyi0lvoU-u1ZZH8bXeE9ts0bL_N0EoNcDJ1lYm2Us-E6kdBVJfdvpB5m8mibFW3J5rV5ft7ORAfu2taRmO4_gpddLN3S2RCLsMWRko5xKnhE3-FzBuUf1k84SuY5kleZOlyI5AmVMVCJnM9P3S9h1Tx0U1WRqkC0ZN1OcPufhWqbFbWqbLmeCD2tIaM5nwKVx3Ku6nRu2__Ni-YRsD0KZvFKLKggI7uE-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۳ ریشتر در عمق ۸ کیلومتری زمین، تازه‌آباد کرمانشاه را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/455492" target="_blank">📅 14:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455491">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c314f67236.mp4?token=Kf60hw7Zb8qnQshp0iy6VDw7bksUM0xFQAnh0zmY0-u1Kp6WYbrCneDAOo6qTO4OjUCi3hBGWkK-8XwvT3w_4_ngUUrjwpHAj90flgIgEAumlz__8mUtZZUYOQCSAZh5_0SXAbzVa1p_ECGfVxZUxVL-ZJqr3_EEFswHUr6862ARX44GZMvmHpr-bH15bjJLXJnt_W8b3i9rxUW8lwv124KuT4cPWTt0xvE41ch1w8RXSJpWzmVDTAQ4Gn_Edd8n7fuU0KhhQSUovGRTpSzcR42rBzAx28liYQmo7WEohoBdd_zsCRjouPFOQR4wsqiYRgyDuwVflixXLWA-7a5QoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c314f67236.mp4?token=Kf60hw7Zb8qnQshp0iy6VDw7bksUM0xFQAnh0zmY0-u1Kp6WYbrCneDAOo6qTO4OjUCi3hBGWkK-8XwvT3w_4_ngUUrjwpHAj90flgIgEAumlz__8mUtZZUYOQCSAZh5_0SXAbzVa1p_ECGfVxZUxVL-ZJqr3_EEFswHUr6862ARX44GZMvmHpr-bH15bjJLXJnt_W8b3i9rxUW8lwv124KuT4cPWTt0xvE41ch1w8RXSJpWzmVDTAQ4Gn_Edd8n7fuU0KhhQSUovGRTpSzcR42rBzAx28liYQmo7WEohoBdd_zsCRjouPFOQR4wsqiYRgyDuwVflixXLWA-7a5QoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگ‌ترین پالایشگاه روسیه که در ۶۵۰۰ کیلومتری مرز اوکراین قرار دارد، در آتش سوخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/455491" target="_blank">📅 14:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455490">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612dd85d5a.mp4?token=I2F_xOWwMOnBLOIR4CiJZdmqxrSaqZmdVLMd8sJq2BldPwSJ506dCLECFAw17d15xv_jZndsdM2cgRRamrI8uelFWey-GQJ6Rrb-AZ0EMy4fr7oQphNdYG3nHtP8SoSFpwh_Gn_p9Oo8QjSAEXSAA1ppXqa5xEGS8xd5lJc6YFNwxOQH_yyWi7XgCRn43oxGZFDOndZlbmYHCHjzGn3DcPdxaB9rvxK9-dQz79Wq9e_-_EosWkVGmUTLYkX363kT2NnGTcXpRysTL8CBcnY8356xa9nIRlcHgiXOkYVdCGotzBFCtsbiW7G5s1Mwf7AJUJ5gN6dLuajvIStREy1H1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612dd85d5a.mp4?token=I2F_xOWwMOnBLOIR4CiJZdmqxrSaqZmdVLMd8sJq2BldPwSJ506dCLECFAw17d15xv_jZndsdM2cgRRamrI8uelFWey-GQJ6Rrb-AZ0EMy4fr7oQphNdYG3nHtP8SoSFpwh_Gn_p9Oo8QjSAEXSAA1ppXqa5xEGS8xd5lJc6YFNwxOQH_yyWi7XgCRn43oxGZFDOndZlbmYHCHjzGn3DcPdxaB9rvxK9-dQz79Wq9e_-_EosWkVGmUTLYkX363kT2NnGTcXpRysTL8CBcnY8356xa9nIRlcHgiXOkYVdCGotzBFCtsbiW7G5s1Mwf7AJUJ5gN6dLuajvIStREy1H1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندهٔ ولی‌فقیه در بنیاد شهید و امور ایثارگران: در جنگ ۴۰ روزه ۴ جنین به‌شهادت رسیدند
.
@Farsna</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farsna/455490" target="_blank">📅 14:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455485">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منابع غیررسمی از حمله به یک کشتی عربستان در باب‌‌المندب خبر دادند
🔹
شبکه «الجمهوریه» یمن و برخی منابع عربی از هدف‌قرارگرفتن یک کشتی عربستان در نزدیکی باب‌المندب خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/farsna/455485" target="_blank">📅 13:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455484">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjhvbJVjmz9KBo2ZQ53RrzpG00qdcm35isj6IPq8rm9LhoN3zeYSBefUb5M2IVdqEdLkyAxyjmmOPUDbzq1f4CU8cMIw3nnFvXfrjG7wKo69ZtPNc1eCwLfwoqUcmtsHYBte33U9Qe8k4KM40gPiD0CdXzvqiEcbUDUfPvbEyCjzx4eybRla9LtxYIYUGian8j8nLB2GiBSOEFVIr04EefSAm08vGgz91wdTCvj5_FXlQ7qK6OQybh0KW7HDcl5dCZbQei1fANNONPSBhB87aaF_1gIyk4BUzoV68gjYg2uo270gPwbpmBHYWIhF8PhJSFjY9OHkOdA3xiA5Tj3Vjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: معیشت مردم باید دغدغۀ اصلی نظام باشد
🔹
با مدیرانی که برای افراد فاقد صلاحیت کارت بازرگانی صادر می‌کنند، طبق قوانین برخورد شود.
🔹
بهره‌مندی از ظرفیت محله‌محوری و مسجدمحوری الزامی برای راستی‌آزمایی و ارزیابی وضعیت درآمدی و اقتصادی خانوارهاست.
@Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/455484" target="_blank">📅 13:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455483">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پیام تبریک رئیس ستادکل نیروهای مسلح درپی انتصاب فرمانده کل سپاه  برادر ارجمند سردار سرلشکر پاسدار احمد وحیدی؛ سلام علیکم
🔹
حسن اعتماد فرماندهی معظم کل قوا در اعطای درجۀ سرلشکری و انتصاب جناب‌عالی به‌سمت فرمانده کل سپاه پاسداران انقلاب اسلامی که بیانگر لیاقت،…</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/455483" target="_blank">📅 13:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455481">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQhXcltNsSkzg24RO1SpkrZfpYX81Q1M9aKmpyJtdzd1494gSwe-NfwqTI_BjhlbACj0mixTmMn4t_tDaRWs8Hnu46dtD9nFdiq8BXqL5ZWGYbEZzF_ShAlFuyGtcFEZRk6sx3DONLLY8lzkkS9T1kUDO19QfP9Cn3fdu6nMCwUAHg_nIWRbuCVw5_m7w9MVqxArRX3SHU8Dyzls4trKqDVVVi-S65bW9SmE-hEI5pgIBdgJ_tiCSoTmCkX9Ye3K0951_9SPD9qVvYPb2QoOCJZbyTsq57qQIqKyAIFEJy7VxNyYkbd3GeyHKF1B3VUMGXb9NnTutBabB9iUrUywNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پیام فرمانده کل سپاه در پی انتصاب محسن رضایی به دبیری و نمایندگی رهبر انقلاب در شورای‌عالی امنیت ملی
🔹
برادر ارجمند آقای محسن رضایی انتصاب شایسته و حکیمانه جناب‌عالی به‌سمت نماینده رهبر معظم انقلاب در شورای‌عالی امنیت ملی و دبیری این شورا را صمیمانه تبریک…</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/455481" target="_blank">📅 13:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455480">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCrafj32ImOHb03bYNWygqbaSEzC4Wr42Hyb5-P1MtMKoRkY9UyCSIBEy1zaCrMgBeLz7sWJOca-rfgOgVH8VwiYtfPh_RYqDbJS7NLSpPKwbEfW3ge5-2Po1ydahnXozGM7CpeDaLRJ3_gRaRBm8t3mX0FG7sTEY9sJf1QHhi1Ad3WLMtKC_iH71nhYtLJXMavGE9l3lO92KLC4WEmVljteGBsJIxOAy_9pquUCLrmZuxT5qClmWKkHanizbgxixxMLW6Zrns5n0DBWNC-o3SNYB4Lc8WNjJG0-4_JJLcP9gb5WocWYQ2rui8DQRqj5x9DT5aPE9grCOuBYa4geng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وقوع حادثه برای یک نفتکش در دریای عمان
🔹
سازمان عملیات تجارت دریایی انگلیس از وقوع یک حادثه بین یک نفتکش و نیروهای نظامی در دریای عمان و در نزدیکی بندر «گوادر» پاکستان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/455480" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455478">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ec778b72.mp4?token=mKH4AXFC9qXlKVy9fT6Ze-JNPuUsFJ7TgWSi3qOnJVbx9Rn0kHcEhESHr6UKjOtTyjBLJFXZ5mTh2eDYZycV_VawX9S6viYqCIy4V5stCEyiYk6ytnxsW5sNS99KnthCvB4YCYeVlvc60q975UUPBDULuVATanm0M2gVsCdpKrB9Tk4ULMIEO5KFd1FZvTpcVlz0qPH0qusGYJrugme74edh9L2642kNLv8wfuRJxi1T2QMJNCKoywHsqKH2sL00P-DGV4aN5TMups8U8vM9L8WgKdwCIlC_GDkDvEfoB7FX7tK3cfGvty7Vd_TJ8bkEMae9pKbStCCfeIX2JhR1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ec778b72.mp4?token=mKH4AXFC9qXlKVy9fT6Ze-JNPuUsFJ7TgWSi3qOnJVbx9Rn0kHcEhESHr6UKjOtTyjBLJFXZ5mTh2eDYZycV_VawX9S6viYqCIy4V5stCEyiYk6ytnxsW5sNS99KnthCvB4YCYeVlvc60q975UUPBDULuVATanm0M2gVsCdpKrB9Tk4ULMIEO5KFd1FZvTpcVlz0qPH0qusGYJrugme74edh9L2642kNLv8wfuRJxi1T2QMJNCKoywHsqKH2sL00P-DGV4aN5TMups8U8vM9L8WgKdwCIlC_GDkDvEfoB7FX7tK3cfGvty7Vd_TJ8bkEMae9pKbStCCfeIX2JhR1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمین گلف ترامپ پادگان شد؛ تدابیر دفاعی بی‌سابقه از ترس ایران
🔹
نگرانی سرویس مخفی آمریکا از حملات پهپادی و موشکی ایران باعث شده این سازمان برای حفاظت از جان رئیس جمهور آمریکا در زمین گلف ترامپ نیز سامانه‌های پدافندی مستقر کند.
🔹
به گزارش پایگاه خبری «وار زون»، در تصاویر منتشرشده از حضور ترامپ در زمین گلف بد‌مینستر، سامانه پدافند هوایی Avenger ارتش آمریکا در پس‌زمینه دیده می‌شود. در یکی از تصاویر، ترامپ در حال بازی گلف است و یک سامانه Avenger در پشت سیم‌های خاردار کنسرتینا مستقر شده است. در تصاویر دیگری نیز یک دستگاه Avenger و رادار پدافندی AN/MPQ-64 Sentinel مشاهده می‌شود.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/455478" target="_blank">📅 13:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455477">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXNH8oyDzdKbEE3OCyU1WBv5pbDtHnyzs1F6ey-cjo46LBaTy8TnKfek3gGWTxOunNHNOwGxUxlyKv0eFGgtbFJjgzS2OEl41a8KYl6yJQer2LHxLgggQNaW9kcoO8A0xfDa17n90drvUlBK3DEksr5d3ysVKZwijchNaK9wf4-Zq0RN0ZHyI_otgR96a7sEKseF6lTPQJbDfmiQKUVHkSZwZtwFaTHtI9CIxGxIoxiie9aN_2M5PSVBqjUEOktjB9J3IHB6UO-BX7g0oMyJq3LQepKrbEHtJhH1WMWw3jSVhXPOYjeUEX6swknbI4tc56JJSJTBFvVMmu16a3oiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی ملکی، قوی‌ترین مرد سابق ایران برای ۴ سال رئیس فدراسیون بدنسازی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/455477" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455476">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/443634235b.mp4?token=mttvVIPOjG-6EfAzRb6bjoVJFqx4ZDIcOqWgM-DjlqzkDu_iKshzbvYLeU2ayP6SuAqDm4Mgl171sizII8sStP8_nrt934AfVF1mn5wEudC17JgXJXdP_UWm56k4_3ariP7_kaMozqzYpBFs__gt0obSRBBVe2J3uNkKdr3lBzSxusaf5RRlVrxpZVZDY3sSv0uJTvwK5FKC32mji96XAnHRPeRVAAPPO1NhCiSiiQSthLp1cA1clA0mjvIKGKnwrXahyuHmAfxEFOtgDBINwBS357JxJLPVKdbr23hqwvPWv8ocRpRbc95GDZctebqQdKMUuIi7AtGnF-Kv0GTk1DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/443634235b.mp4?token=mttvVIPOjG-6EfAzRb6bjoVJFqx4ZDIcOqWgM-DjlqzkDu_iKshzbvYLeU2ayP6SuAqDm4Mgl171sizII8sStP8_nrt934AfVF1mn5wEudC17JgXJXdP_UWm56k4_3ariP7_kaMozqzYpBFs__gt0obSRBBVe2J3uNkKdr3lBzSxusaf5RRlVrxpZVZDY3sSv0uJTvwK5FKC32mji96XAnHRPeRVAAPPO1NhCiSiiQSthLp1cA1clA0mjvIKGKnwrXahyuHmAfxEFOtgDBINwBS357JxJLPVKdbr23hqwvPWv8ocRpRbc95GDZctebqQdKMUuIi7AtGnF-Kv0GTk1DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پورابراهیمی: قرارگاه خاتم‌الانبیا باید در حوزۀ اقتصاد تشکیل شود
🔹
رئیس کمیسیون اقتصادی دبیرخانه مجمع تشخیص: رهبر شهید فرموده بودند «جنگ ما با وزارت خزانه‌داری آمریکا است» و امروز نیز محاصرۀ دریایی را می‌توان مصداق این جنگ اقتصادی دانست.
🔹
در شرایط فعلی، مقابله با فشارهای اقتصادی و تحریم‌ها نیازمند هماهنگی و تقسیم‌کار مشخص میان دستگاه‌های اقتصادی کشور است.
🔹
همان‌طور که در جنگ نظامی میان سپاه، ارتش و سایر نیروها تقسیم‌کار شده و قرارگاه مرکزی خاتم‌الانبیا تشکیل شده، در حوزۀ اقتصادی نیز باید چنین ساختاری برای هماهنگی و مقابله با جنگ اقتصادی ایجاد شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/455476" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455475">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTwzPV74ljCspebEMNB2geo8zTp7jC9NZRb1enpTG2_cKRDXFyBKDJkchMhl4oEWDG_hCG_6lAl5-AiKbOirN4Ichrh-V_akfuxldMZeADmwpROI7KvIeg500x6xXdhJAz1Kuw5bQ4fLgQGJaL9Rjkimvu0wAq0MoRd0yL_n6rnEAXJX-ceOwb8elr8XFB-ps7tkrLlznor2OMp9K8ijpUuS4ebIngM1k7fWS3JVODHw7SHOMoeiPE0opOCPe8Z5OlBgOZR2IbX6foZibBq1weJGPyY2K1yD07ezaVpdL8w6ii_rCOswh8j-_Z6LQnxJTevxQURntXgm4LU3CaogWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرتیپ پاسدار احمد وحیدی</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/455475" target="_blank">📅 12:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455474">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqxT81UQ3rKEQPwl1qhBFwiUga7PANtIayHTw7YvD85zE6f-DZEt1LeptwoVXLhExwpsZ3YynMD4kX7jSbENH8IrSFPV53lwWTalyc5_DKNoSIaOAlQyXGvwQq65HNM5IqneRHH0_w2MA4x2v0Ac2guJOhp7aidoIq1cjoWcfKvOVX6-pUIGwPi9bkCzDoqv0fAKrE4iqwDx33WprA_-ezStKNtnjajeQHhOk6tdMKSvrdOF1JcNbe6F0SGNcF0yypvrg7XUj-bLMWRk6DuAWEt-sP8X_PDEMyaMG9gZbVwkSwBAk-KEO3_BVcVu5D-ag63UC7A0j7yP_ia0rd5wZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلیت تهران-مشهد پرواز کرد!
🔹
همزمان با موج سفر زائران به مشهد، قیمت بلیت پرواز‌های تهران-مشهد از بازۀ ۱۰ میلیون در کلاس اکونومی شروع می‌شود و به بالای ۱۹ میلیون تومان در کلاس بیزینس ادامه دارد.
🔹
این افزایش در شرایطی رخ داده که سازمان هواپیمایی هنوز واکنش رسمی به آن نشان نداده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/455474" target="_blank">📅 12:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455473">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699cf9fe4e.mp4?token=qEFZwN1k-l1i6hHGAUpWaUzBhz-otALHY-Qh0wOYdaIwKv80aVdKVUebbTnY3bN0dak7-Ih0XyKn7g-LHknKfbUOFsUgvJeUtCw-JRB8UZ56nZ4mPUM-kwoCd-viqjOQbg46u6Huvb0xr3yPVDYwFC5qw7mP0IK22STtx7VTDzBj8Rtkex_F_lO4xYRkNimabeNGI00CHmgs7XQukDmPlSFkJADNIKmBPulo3mXgixeRekm1FVMq0D1VdLW654rf4KvhabpyVM6FDPpFXkl2cPB5CyRmHZvv1_Wmo_tLZUkRqJioWFTHOy4qNIEiQDdTaKT8nx5j_YLfAx1uSbbpqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699cf9fe4e.mp4?token=qEFZwN1k-l1i6hHGAUpWaUzBhz-otALHY-Qh0wOYdaIwKv80aVdKVUebbTnY3bN0dak7-Ih0XyKn7g-LHknKfbUOFsUgvJeUtCw-JRB8UZ56nZ4mPUM-kwoCd-viqjOQbg46u6Huvb0xr3yPVDYwFC5qw7mP0IK22STtx7VTDzBj8Rtkex_F_lO4xYRkNimabeNGI00CHmgs7XQukDmPlSFkJADNIKmBPulo3mXgixeRekm1FVMq0D1VdLW654rf4KvhabpyVM6FDPpFXkl2cPB5CyRmHZvv1_Wmo_tLZUkRqJioWFTHOy4qNIEiQDdTaKT8nx5j_YLfAx1uSbbpqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی امام رضا(ع) ضامن شد
🔹
مراسم آزادی ۴۳۷ زندانی جرایم مالی در حرم مطهر رضوی برگزار شد. این طرح با دستور تولیت آستان و با مشارکت خیرین به ثمر نشست تا ۴۳۷ زندانی به آغوش خانواده‌هایشان بازگردند.
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/455473" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455472">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7107Rn_5Boq4Qo5kd05AGnyz5orP1ay8BeNDibYkjcJjNL7_QSr5_3jqYzVzcsdzLIq1h7xd1IXIEDkOq8-WaemjEiIUs03Y9athFEQpzVm2TKcvs8lrl7Hmw-9Zz1QIkM9FVraVWey-47P8YrpEh56gRTOpE0WLoQ9Gkj-0rahjim8F8D435r-NjjhLyJUbslmeeekh69XmddDksO9ZY2yIvrX8DON2FCfFLS-ol1CKkzmwUP4QKlkt6OTJwo9UDBvhyF7ahHP_aoi2r6ccUGnW8HXn0HPvOoUWnwY3Hvv4x1VY7JYo7znJr6HH6_4-2LsDrCh5vUQQwttTEzvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاگردان پیاتزا حریفان خود را شناختند
🏐
مسابقات والیبال قهرمانی آسیا ۲۰۲۶ (انتخابی المپیک) قرعه‌کشی شد و تیم ملی ایران با چین، هند و نیوزیلند هم‌گروه شد.
🏐
تیم ایران ۲۹ مرداد با ۱۴ بازیکن راهی اردوی تدارکاتی روسیه خواهد شد تا پس از برگزاری اردوی ۱۰ روزه، برای حضور در رقابت‌های قهرمانی مردان آسیا عازم ژاپن شود.
@Sportfars</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/455472" target="_blank">📅 12:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455471">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCRUYqh8jiPByc-1SCFjxjM8laiFE_Yuwny6B88Ilf-rTqe8n6LbXWlQ7m8M4JRQFZXFAq-drIq8-PvB8TG48DUDhw96oFPHcqJYAP2V0lIfCPRyg5J_LUA55vnVOJok3yaa2-Hu5bcJ3kThezxOegcwkTOcuEv8QoagQdAJpHMAL573RzU363blL8FBdz07WYuxsrlRMUKR_Lrkr6xdqRL8ITdd6zuxD1jmjbMEUgw27sHOHn-_bQXkSDdutydr9Fbb-E7urxG6PWE-qBy2fINXme29nTx_tLdiIZTRCVPv-sgF3ug5HU6QMo7tNtVRvePJ7v8qNUPGBzeu7B9d1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: تحویل بشار اسد ممکن نیست
🔹
سفیر روسیه در بغداد: تحویل اسد به هیچ نهاد خارجی در دستورکار نیست. او نیز تاکنون هیچ‌یک از شروط پناهندگی اعطاشده را نقض نکرده است.
🔹
یکی از شروط این است که به اسد اجازۀ هیچ‌گونه فعالیت رسانه‌ای یا سیاسی در مسکو داده نمی‌شود.…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/455471" target="_blank">📅 12:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455470">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzIPI3MB6P9HzfRmHytKP52FF6pIuHMVvOnz7G4gsyaCrPwJ9Ru_yDTDuz-6XWDF5RWkeSf4tqpyNz0cLyO2HUEzzTz4bReBBXsd2XPKPUs7S1B2WVYpf4jv1J5CeT3L_wTMirEl5DduCiZeflr7zjV31-e6uRcoeZlwIBfEwDEXKvJDt2wBsOVgE4QLxOk6Bxrm85JvwwR2AK6yOgPxQbWwnNDnpcGxP2B-oakTknAQD-yYwAR8kOj1tGjHr-aRIi46tWG_ht4UwRJKxG3-nt3fSUo-jrqyBO2NtaNqx6deidogJqd_fUlTep4A6XEwoxRxAraQh9HzkdBV6RXcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس با رکورد جدید هفته را تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۸۲ هزار واحدی به ۵ میلیون و ۷۳۷ هزار واحد رسید و رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/455470" target="_blank">📅 12:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455469">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgpGjdDLbo6nI9FbjHJ_LiC_vkfUqivmav93BTzKwCRWvqQXGx43dHNSr8n2ZaLGKF2KH-Eqq0thFdFztphlJrapcqmUtxaadymqk0wHtk3eZkiVkhLfkR68d1htubqS1Pxv3DlemShJtJe0WaRdfD40YibxKqR200vSryLbUkjJHuoWp8uBFkiIkCggBa9JEQTvIyT4KzzGoFDKNa7olZuwOmhl0maIr1UOgc5yI1nA-3hte0A0L0ErgF_dK6JBixNoaCadsRXn5Kd0SP1nDYfEh4cojM1Pe4cJQZzoLNWI38l1Z5dwkBMADsyJTgFj8GMkY6HXkoWqnUQ_egbmTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانداری خراسان‌رضوی: ورود ۶ میلیون زائر به مشهد در ایام دههٔ آخر ماه صفر پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/455469" target="_blank">📅 12:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455468">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فرمانداری سیریک: انفجار کنترل‌شدهٔ مهمات امروز در بندرکوهستک انجام خواهد شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/455468" target="_blank">📅 12:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455467">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73ce01548.mp4?token=rzDw9_zLD1RO8LyoRmRVTE1rkPvllUgG_-zcgcrQCJ2rTCmJZra2gN9vS3qHRd1HN_0xVnqSWirCaQwCIxS9gSMTvQwBqmr50XMvPePIadnhv-fiOv7wOHyPLxXgCgGZD-zbFkqvS9g-YjZDHP7xTzHLKS6I9BClgIz1S81n51IaR9Z9gHXx4rWXsqxQWBROsxO0dIjhjLC7pGkmu8pv2aWz3zSP8McJEgfTPN_qkCnapAmAPUna4naeBSyAmIydTvgZxxWUWdEsuLFB__26sMt521CXi22YB7Um3jiHb87J4-TGJm2UwqxKqykyHDotpUvo_dekSaObB3StwVvTSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73ce01548.mp4?token=rzDw9_zLD1RO8LyoRmRVTE1rkPvllUgG_-zcgcrQCJ2rTCmJZra2gN9vS3qHRd1HN_0xVnqSWirCaQwCIxS9gSMTvQwBqmr50XMvPePIadnhv-fiOv7wOHyPLxXgCgGZD-zbFkqvS9g-YjZDHP7xTzHLKS6I9BClgIz1S81n51IaR9Z9gHXx4rWXsqxQWBROsxO0dIjhjLC7pGkmu8pv2aWz3zSP8McJEgfTPN_qkCnapAmAPUna4naeBSyAmIydTvgZxxWUWdEsuLFB__26sMt521CXi22YB7Um3jiHb87J4-TGJm2UwqxKqykyHDotpUvo_dekSaObB3StwVvTSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: تا جایی که ممکن است اموال، مدارک و وسایل مردم را کمتر نگهداری کنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/455467" target="_blank">📅 12:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455466">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4dZJrfzzcvODopQ-FiC8g_RHsUFfYBwlF6g87DKsRHYwY56pfaiO_nhNeWBVUrhGGgu04JjjHxGDneK8Y8j3QOIRVKqYyPPec_8H3cmKEb6cYkFZqU0wXd5d9m3vj6B1ElMlSwQRBU98Vf2-0KKHnDXKKFuV5LPGSGNMepdcb99OdOdM9CI_i9MMa1dR6hStIEJfE5UaQr8uvhrR1f61nOPqFSokCuW0XFFc2VxBT3Imu-uPfu6FIJ2LzbopTCJPtvzx3jMp8jmCoU2PCJZ33s_0PWdTD9DbLJjwLLor0a5tlirGpkJZ6yJAQRBSRB3ttzyUval00MTQuaxL3lqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس اوراسیا: پیامدهای کنوانسیون دریای کاسپین از واگذاری بحرین هم زیان‌بارتر است
🔹
برهان حشمتی: در کنوانسیون رژیم حقوقی دریای کاسپین، فرمول ۱۵ مایل آب‌های سرزمینی و ۱۰ مایل منطقۀ انحصاری ماهیگیری پیش‌بینی شده؛ یعنی در مجموع ۲۵ مایل. این محدوده به‌هیچ‌عنوان…</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/455466" target="_blank">📅 12:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455465">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frZsWl3u7UIqWF06IwpjqjxLEMWFRuFGJQ8QeEY7pqp3fVVUL_GEqluqV1LP4VJvSVgrLLarM0cuPljfVumhBnb8vhdUtMdW8xNJhWXW0rFZ8zTQoDn6dB2Nz4iagrvz25vmh0GDep7lIpZ_OjWaY9oh2Q4NazIS3YRv5GlS0V610wfmxB4fGOLIiqBHqNtZrk5hcXqd_EI_3Mu2BizAoQ_OQbvXkv7eCgnCxMSnar7U0Ie8WzHfnG3AYlTM2Vdzeylj73n4OgQhmSeVdF4nNALnIMv8uLyIxJl_IU5-EGxzbleFxSzL4QGh2yimHXL3YXlVVNnIMgwu-M615--g6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ قالیباف به پزشکیان دربارۀ ارائه لایحۀ اصلاح قانون بودجۀ به مجلس
🔹
تاجگردون، رئیس کمیسیون برنامه و بودجه:  رئیس‌مجلس در این نامه از رئیس‌جمهور درخواست کرده‌اند که لایحۀ اصلاح قانون را با قید فوریت تقدیم مجلس کند تا هم دولت خلاف قانون عمل نکند و هم مجلس بتواند با توجه به شرایط جنگی و اتفاقاتی که در جنگ حاصل شد، قوانین را متناسب با این شرایط اصلاح کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/455465" target="_blank">📅 12:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455464">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDoX-d1ADCE_XU1FJY9tG8czq63ccFtnM9fF7D0ANbDBpjbNTZnuAZyfU8ZW4b2Wdgu2Hd0omG7vG81sxs_lyydZPTcyBrwRjXWkjMmK7cdU_zh4JD8jhGBODqubLs2tOSK-cImP3xZHnOe8xE3v3u6T7W7LNuLCmwVUErsjcVH0sIU76F5pMWCBs5QFtPmmW145czDMMpap4e6-z1TSPTuV7Mv4IH-F0cca5gdD1J0iRRDLFRSZGb9U5yVQHZyMf9F4ISxhThcBZSca14C_OrFJQExUjoRohGxgIed7VYn7XQlW2I78-e-PCPLkDIk8kB3Ok1qwASIsSMr75opqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین تصویر ماهواره‌ای از وضعیت دریاچه ارومیه
🔹
جدیدترین تصویر ماهواره‌ای از وضعیت دریاچه ارومیه توسط ماهواره کوپرنیک و مقایسه آن با مدت زمان مشابه سال گذشته، خبر از بازگشت امیدها برای احیای این نگین آبی دارد.
🔸
میزان بارندگی سال آبی جاری در حوضۀ آبریز دریاچه…</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/455464" target="_blank">📅 11:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455463">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51a74e04ca.mp4?token=K0de8FkFg1ytkYuvw7Kc5GINrtAEODjh8USiXT-9xgN_Xkjk1RsxVv-X6hBi26MzYhzC7cbvn5_7wK0iV4tIxX3Lp_gcw1NCZ6wqK3v9NgREBYuBak4DZO_noMO49bemMPTEgNiHNFHwYT-9PuoQUZ4jq-u02sEMwuWBIm9Tkqd9hbN7y3jNjtYYKHPeBbyORzqRGyW1706LKjWMZuwP2PuROf5ySp5YINtsR8VZcn3weNvpVPFg78NpXPuT5HaCGgYCGR4L2vrIDlAczWKlNlVo29Rtxfzxnhgh9Fl7F9Rxi9kI1bupebSx3oI7lP7OuQTlM6PmzkBhWx1z0uKW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51a74e04ca.mp4?token=K0de8FkFg1ytkYuvw7Kc5GINrtAEODjh8USiXT-9xgN_Xkjk1RsxVv-X6hBi26MzYhzC7cbvn5_7wK0iV4tIxX3Lp_gcw1NCZ6wqK3v9NgREBYuBak4DZO_noMO49bemMPTEgNiHNFHwYT-9PuoQUZ4jq-u02sEMwuWBIm9Tkqd9hbN7y3jNjtYYKHPeBbyORzqRGyW1706LKjWMZuwP2PuROf5ySp5YINtsR8VZcn3weNvpVPFg78NpXPuT5HaCGgYCGR4L2vrIDlAczWKlNlVo29Rtxfzxnhgh9Fl7F9Rxi9kI1bupebSx3oI7lP7OuQTlM6PmzkBhWx1z0uKW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«دان خوابالو»؛ هشتگی برای ترامپ
🔹
روز گذشته دونالد ترامپ، رئیس جمهور ۷۹ ساله آمریکا، میزبان یک رویداد رسمی در دفتر بیضی شکل کاخ سفید با موضوع سلامت مادران بود. در طول این مراسم که با حضور مقاماتی چون رابرت اف کندی جونیور (وزیر بهداشت) برگزار میشد، ویدیوها…</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/455463" target="_blank">📅 11:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455462">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/692ecf877c.mp4?token=ocMaEZGjAaDLG8cDuUaIrJ5miDD2cXPnY62i4h0urNQa9M3ICihclV44goUIgyZSk_5pGhGhfuNRZG7cFinDazXMm2vo9YijYaD_OnCx3asoY7BIkI-dRNP6MtfIVYDe1dUy1jZdzPfapWTNFqzW1wJOLGevoMoff56SLnpzMUmJAJX4xRrxnO6AgAMjdss4gQJdjCDYYptiI3pKby_LxG4KpiFm3BV61pBCcwMiMSMwHSlMDI2W0DGOFDYt3jG8ovvuzggiyEQyEPw3CWoUOEsJdeNRu4323UWgmkNbsar-O9wo8N0hOrTJ4mBmqd1NeL6ebXrRjI9fllceXOmyqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/692ecf877c.mp4?token=ocMaEZGjAaDLG8cDuUaIrJ5miDD2cXPnY62i4h0urNQa9M3ICihclV44goUIgyZSk_5pGhGhfuNRZG7cFinDazXMm2vo9YijYaD_OnCx3asoY7BIkI-dRNP6MtfIVYDe1dUy1jZdzPfapWTNFqzW1wJOLGevoMoff56SLnpzMUmJAJX4xRrxnO6AgAMjdss4gQJdjCDYYptiI3pKby_LxG4KpiFm3BV61pBCcwMiMSMwHSlMDI2W0DGOFDYt3jG8ovvuzggiyEQyEPw3CWoUOEsJdeNRu4323UWgmkNbsar-O9wo8N0hOrTJ4mBmqd1NeL6ebXrRjI9fllceXOmyqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رهبر انقلاب ۶ فرمانده عالی‌رتبه را منصوب کردند
🔹
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های ۶ تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند.
🔹
براساس این احکام، سردار سرلشکر…</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/455462" target="_blank">📅 11:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455461">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9001b587af.mp4?token=mOyKRoWx6mnhi_MDJEqiwlIkoxadOrSnWnNs1Y8afcvCZR2WoVGkjQsvZ_K7NP-dTdEbpxn-gTDCx9GzyKxnJpcTmGHFF4K2uVrbFIRDWBJXdnlhozUqXO2eLmkAM4amFTXmtFSr4t5MR8pgFJiKEn0uLofSuKZkV6Dhp5aFeiP6PitNhCBCxoEh5n81sCjfs78i9J-mrOnEOSgDqTX0THREH65IKWXD_Cea-BepHW_vKl-siA8Or9seAu_BkeI_A8dGNvIR0UXYYWFVs96Ajz6wzGsQ7PG6wMxtypsg7xwyoSYWRtYDIusbiiUBZBsmq0x6xeuaUe495u2A2WLp3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9001b587af.mp4?token=mOyKRoWx6mnhi_MDJEqiwlIkoxadOrSnWnNs1Y8afcvCZR2WoVGkjQsvZ_K7NP-dTdEbpxn-gTDCx9GzyKxnJpcTmGHFF4K2uVrbFIRDWBJXdnlhozUqXO2eLmkAM4amFTXmtFSr4t5MR8pgFJiKEn0uLofSuKZkV6Dhp5aFeiP6PitNhCBCxoEh5n81sCjfs78i9J-mrOnEOSgDqTX0THREH65IKWXD_Cea-BepHW_vKl-siA8Or9seAu_BkeI_A8dGNvIR0UXYYWFVs96Ajz6wzGsQ7PG6wMxtypsg7xwyoSYWRtYDIusbiiUBZBsmq0x6xeuaUe495u2A2WLp3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: جنگ‌های ۱۲ روزه و ۴۰ روزه صحنه‌های بی‌نظیری از جان‌فشانی مردم داشت
🔹
نیروهای مسلح ما هم توانستند بزرگترین ارتش ظاهری دنیا را شکست بدهند و عاجز کنند. جمهوری اسلامی ایران نشان داد که یک قدرت سرسخت و شکست‌ناپذیر است.
🔹
مقامات خارجی بارها به من گفتند…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/455461" target="_blank">📅 11:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455460">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a4478836b.mp4?token=hsJf5CpM3bjsVh8IBU_G8smAK5ldT_zoTXQumWzYF48R3y4I3Lay-hc79E-HV98SZ8Q62U3n3KkJ1TGUCVOTS6UJV791QbUQThOXPMhv-1hvJOIl45Qnulj4Yk2yXIdiPGVk-30xxpeGE-Njrfno9oYv0XxE6Tftr4E0ne2AG1ctwiapx9EcV1FjQ2rPmzUYjnah6cIw5HX1EwX6Are-y1O1g3RQfgSBHaGzvFA_hT3rMimpFRKmK4b8OIWBL-_6OblW8nT-szzrBnfpqiGT75DegziRCnSzEAZ6VSAkcS_ZIU7TGlziUQHxcF0Rt-1-K2EFXH-ZO6nwEe0uKweGBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a4478836b.mp4?token=hsJf5CpM3bjsVh8IBU_G8smAK5ldT_zoTXQumWzYF48R3y4I3Lay-hc79E-HV98SZ8Q62U3n3KkJ1TGUCVOTS6UJV791QbUQThOXPMhv-1hvJOIl45Qnulj4Yk2yXIdiPGVk-30xxpeGE-Njrfno9oYv0XxE6Tftr4E0ne2AG1ctwiapx9EcV1FjQ2rPmzUYjnah6cIw5HX1EwX6Are-y1O1g3RQfgSBHaGzvFA_hT3rMimpFRKmK4b8OIWBL-_6OblW8nT-szzrBnfpqiGT75DegziRCnSzEAZ6VSAkcS_ZIU7TGlziUQHxcF0Rt-1-K2EFXH-ZO6nwEe0uKweGBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامهٔ همکاری بین وزارت بهداشت و وزارت خارجه برای بازسازی زیرساخت‌های آسیب‌دیده در جنگ، امروز به‌امضا رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/455460" target="_blank">📅 11:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455459">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef60d75d8f.mp4?token=Wa7aZ9ATjNDc1bIe5NnHOjhbFCo_peF3I-fr-vSogohnrbMoagV9N1aG0bjFqg6nj58R2s_wq3b6N_UIAMBuSHSxhl0REU9TXcPj3MDpSVlGpp1z3bAFqjez1wImFs3qnxwkoMfIYf8KZDrqR4llfjv2yw7wcjKo76v0B9FNcfs5n0aZCEEi1QAol9JqZ1AkuABGBAOAuzITcENvZMnc8kctqD0gvmh8qI_9ANgQRcZpK-nAnqikpSv4bhpMEtW3N0F_pHWgqYry0w2CxSyVbVVASpbg1hiDfm8GjQcTy4d2wnWTJyKpojieRookD1ods5lDdj40QupFVZk_NbDsvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef60d75d8f.mp4?token=Wa7aZ9ATjNDc1bIe5NnHOjhbFCo_peF3I-fr-vSogohnrbMoagV9N1aG0bjFqg6nj58R2s_wq3b6N_UIAMBuSHSxhl0REU9TXcPj3MDpSVlGpp1z3bAFqjez1wImFs3qnxwkoMfIYf8KZDrqR4llfjv2yw7wcjKo76v0B9FNcfs5n0aZCEEi1QAol9JqZ1AkuABGBAOAuzITcENvZMnc8kctqD0gvmh8qI_9ANgQRcZpK-nAnqikpSv4bhpMEtW3N0F_pHWgqYry0w2CxSyVbVVASpbg1hiDfm8GjQcTy4d2wnWTJyKpojieRookD1ods5lDdj40QupFVZk_NbDsvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: سال تحصیلی آینده حتماً حضوری است  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/455459" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455458">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6rlKGJ7zXgtCD0iI4AI__9KQcfTOWsNLJ5HEBJaxUAVL_fI-77H4mhidC0Oc4c0UpRZQyqDUIm4vhrRxC7RkyVEbgp0klJbRYSW3DScTqqq1yDVeH0EEF9B2fPxwxCR-f8hYuA0E7iaa0orQLnTmbN1vCrR4o6yhxLVslSJsms6wOW7eIbXz-YvaUQ4MWjaTUC6JCwdIpI08-kXSw0lO6vIx4fZwm3UJyOqoxbGYFMpQCfjzHQEFuyJzgqCfFOHA4yKoGHsR2pEQa-7QthJIFVvAH6_nhfv_ED6U-Kc_Jw034sMMyvl9AAmtsD-JeGTx8HIujeNEsU4VIezcFFtZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم‌نامهٔ همکاری بین وزارت بهداشت و وزارت خارجه برای بازسازی زیرساخت‌های آسیب‌دیده در جنگ، امروز به‌امضا رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/455458" target="_blank">📅 10:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455457">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/455457" target="_blank">📅 10:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455456">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m58nxusrlc5UGmUs9oOyHWmr5gVXASbkB-senwrNOwwgrC6Ly_tDnfa0tds_1WgC7pXidVD1jAosCuOzTQ1alk5tkIf2fntNgJHhuzHNS7YYwZT1DmhBs1Iucw6Gjj1yRtw0iDYl9cizPh06knFqMPeBaMIY5FuUKNthxSBr3HJHwQ5csQclfxyChSf5-dyuapC5ffnSo_wmBd_mjep5TaoL1Iwy9Lj07vKCfOD8zlmlREY3ANdogHZcXNMFe2kGJH9yLSmDzdBmSPV75cft7s7eP9lr4Yh87gQk3vshEc_Z2cyq4BlGEFvHbjFQfhivevmX2ajBNVFiN-WsMts8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیال‌بافی ترامپ: تنگۀ هرمز باز و در کنترل آمریکا است
🔹
رئیس جمهور آمریکا شامگاه دوشنبه با ادعای اینکه تنگۀ هرمز را به‌صورت کامل از مین‌های آبی پاکسازی کرده‌اند، گفت که ایران اما هنوز می‌تواند مشکل ایجاد کند.
🔹
ترامپ در پاسخ به سوالات خبرنگاران در دفتر کار…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/455456" target="_blank">📅 10:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455455">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">منابع غیررسمی از حمله به یک کشتی عربستان در باب‌‌المندب خبر دادند
🔹
شبکه «الجمهوریه» یمن و برخی منابع عربی از هدف‌قرارگرفتن یک کشتی عربستان در نزدیکی باب‌المندب خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/455455" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455454">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مسیر شمال به جنوب کندوان مسدود شد
🔹
پلیس‌راه مازندران: از ساعت ۹ مسیر شمال به جنوب کندوان مسدود شده و از ساعت ۱۱ از پل زنگوله به‌سمت شمال یک‌طرفه‌ خواهد شد.
🔹
همچنین در روز جمعه از ساعت ۱۰ در آزادراه تهران-شمال محدودیت تردد به‌سمت چالوس، ساعت ۱۱ از ابتدای پل زنگوله به‌سمت چالوس و از ساعت ۱۲ از مرزن‌آباد به‌سمت تهران مسیر شمال به جنوب یک‌طرفه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/455454" target="_blank">📅 10:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455453">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302f3b2287.mp4?token=LKCU54HFJETVmO8eEi89qgm54165XodJHCvq8lYE9OU-I_huDBbGN7VpnSp0CzPrWRC_mRix_WcZJ0VUvQtZUJln0hZ_wuMcSZtt89kE6oWa85zY6uSjRmfXxn8add4mbjO0aeILEhmSckY0L1jHBYGwhVtK-JKznw6iaWxu0C0UqXN7jGSJL20lUzPSJbgHU-adUBVa0PmT09Xl2HYVD-YUGuHni8-ZlaT55paYBz0W6ICBF3CFTUhVb7UEaDq6ZMNUc-O80EgJhA9dUpG3pirSCl5yVx54kkdI6d0HMavZtpR1B5eub9JTBHx7c8huEAjcj9xDvtxH5gZOos3k4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302f3b2287.mp4?token=LKCU54HFJETVmO8eEi89qgm54165XodJHCvq8lYE9OU-I_huDBbGN7VpnSp0CzPrWRC_mRix_WcZJ0VUvQtZUJln0hZ_wuMcSZtt89kE6oWa85zY6uSjRmfXxn8add4mbjO0aeILEhmSckY0L1jHBYGwhVtK-JKznw6iaWxu0C0UqXN7jGSJL20lUzPSJbgHU-adUBVa0PmT09Xl2HYVD-YUGuHni8-ZlaT55paYBz0W6ICBF3CFTUhVb7UEaDq6ZMNUc-O80EgJhA9dUpG3pirSCl5yVx54kkdI6d0HMavZtpR1B5eub9JTBHx7c8huEAjcj9xDvtxH5gZOos3k4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروگان‌گیری در خیابان ولیعصر تهران با حضور پلیس ناکام ماند
🔹
پلیس تهران: صبح امروز در پی اعلام یک مورد گروگان‌گیری در خیابان ولیعصر، بالاتر از پارک ساعی، با حضور مأموران به آزادی گروگان منجر شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/455453" target="_blank">📅 10:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455452">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbb-ys07oHLfkFj4CvzUkgr6rpkZ33f8tm888SYIyg5YbngLgGUZlidRQQ5JurW469U8YHQE4OqlHOny-2MQAlYu3jWDE8feiBM3AWNudpKun2AinuKUd0wHgzk0vjCSdS0br46kSG0kdLRvR0EpYFRKsxHFIN7WY30sQFsfN8kmi2iZ9wR6WUYqh3njsB_nBC3q9hnP7QTnbPut3kMdqA38UCzP7dgX2Tnp0FcOXgJm6LGyOVeoj6miesLBPjrUsR7dx4Ewaof1Y9oCIFZg6tWZFBhOh-pknLTaMgxMD2SdpCGPJvlciga9Gqf2otyq2fHITn2kkE7WsRF5zpe7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروگان‌گیری در خیابان ولیعصر تهران با حضور پلیس ناکام ماند
🔹
پلیس تهران: صبح امروز در پی اعلام یک مورد گروگان‌گیری در خیابان ولیعصر، بالاتر از پارک ساعی، با حضور مأموران به آزادی گروگان منجر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/455452" target="_blank">📅 09:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455445">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rqzgc-OSzCpjc6wxUa5NRq4VolwnMHYLGg_enKoiv6o9rRbxWpYT1WhHNPeg0RUFBjFOWrE54DQ2vzoBksTbYQB16nx7Ygzt3qOkuch3sQtW1nJPY28nww8il14I9R2UckgQsjX7D0N--isfNcK9zWBgPhrexyojnTolMeRx6OvzfB3j1kAarQ9dKKYX0VWa1llYr8IwMwr9mnDe1hECbdzrBYSzGZGXdD5pbinNJsgP107j1DnEwViRxILif_STrzPYKs4w0Ekua5sElFth3cCSTjdYt_w_8gGFKxzIfG_PUHd7EF2UKw1FYvgSvhHRRumjBjC52-A2x9uQYpU8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lhn2JdaDZI1mvBc2Y1vjpNBP0pYV2Tp-di8wqbtdIXrNHaQsLzM8wjK3sJoAgVC9ZJkMsbuuktfzg8xapTzIY5A3xgJMKVDSmZ8m8Bv7oHAy_83gZl2Oopm5ZbLFTLE0i-5nO0CUop7wWfytKTYWP8GYK39eKLatKAJTGH4A-2evM5xpbp2i-MEzgrUMCtYZq_wKP4WgVhw2FnrPAJelW1ry4WhV0SGv5kEnjh7ird7mes4NcW7ESnUGvSD66c5rxqH_o42YRC_z6XbVE1I9DCSH73hm6HZaHVT9PBCImaLDGh2foLmcg6Ru8oklDLkTvdXDt0kXFShgHCgnWruZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7fnSBgmOLG0yJAA29-UNO6XU5XZHm9sa3kWiGKgRhO8rkiGa2e-nouRwWGihqFLFv_zLEN6QnjJKLlNv5Mm-u9KxQvzpW3PlQNoPmED5yzs7fxuJlv8owk7T77F10XR1w_ZCPJL4tnBiN5Ps33Dw2beCg98tZYBfcjA2IRKo-I_eowhQO-orMliKnNa5RNQWRLYCHi58-Jfitfqf_NxIhouu6dqPNgaTPdn-Q5hLiFq87ZqEYl_1pgilVrWEtYFTqGY8tSD5-QiNuMtrC5FDNjQ8fDZXg79KNgObf0Asn7lPPI0WaRFsa8eWcfhvAZ0caLNse1aFqIzREOerOyqQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFtpwvhpOpa-T4fxTDIw3TUkQrQRdw560aL4g6Wf2HoWUymXTk5TQ0TO0o8iBAYN6udIFrKbMah9q2NilHochni1JerKzV9Vj0VHs9ATSbljGHK3vwkpuG_fWveUreCWt8LKDv-JBKFuFc9hrlmN-Py3p1u8NWx8jGhYzDEpbjI1tcqKH3n5qrWDnK9IZBOW9YrArwi8ahn3iFmfQWSqztWlG35fkopWzP3KtNVb0Tts3IppdJo7sO9JzIEj9XQG6bmycaMOIqe1iXA2t6uQxCJS172wNnmQHlKTR5GKa4i7HCor5o42r-Wh157a2a6e-HpGZHSAAIx39LNpgvPTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCqxiJV-vGbbtRNSvzEf5lBJF2PW7nyXZyFQJ3mpebdh8icpEZH7wNuMls5TauIfkoCqsPWGvr3iBvXqEtdcNYUhQ6OMCZWMaIQLuaZC6efDeOecB6hlUa5lDwbg5w8yxCMPmvrA9RkT3zDsCK8ijfDq6UNmPpmcHwu6GJuABeYm1WiPyFfyNsTULOG7Vj0W4l2VMh9uMYiOoDF2MLlh-hg5F2pdpUDLdU5-vatGkdWdX7ehTTca9JZrNIEMLC0UjG-6uebGeBR_GM7OWAGuSy1ZVDFnkl_Rj7zLK_OTulHocYjsFvfacPwpq3oWIbVuBF22iPQzVQ84fb5RBt4Naw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICHRlqD6r1RBZ1RyJ2ShApOWmZQT-x9an_6T7GlsItOMZ-YUo3TUeMVAyIkdQCHhiHn03FAQkdfrWRNQIar-s5Z8vw_eIllAmkdPNdzPPLImz5R1UdkzRI8CISH2-eylEWwvEADEcIcNHRRkwfMR-y_KAN1q8xrvsZ0e3tQ6l-NBvuG-mCVL1hyG4aoRczkrR8Cc738gl_5YqDCdDhLuU_byi0YOKf622RGzAE6PiQKzcmnwX0WmRbOmx6vqyA6F7IiSfxN923YW_YTTcE5BZGJnc_Txsh7QmbtORLjp-xtF8WaJlzPpG4Gh5DDr-UT0gkV3YRJy4pjOkpVy3618LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VniQZwWctvqXbmuFsSviApbYnVxZpH6aa96_3aRkMhM-rXpFzHuuMcPoFPWEEJTSD1qMkSGmYNYPORxyay8iPA8VBJhhj8YYiQXK-uZQKF0mNmOQ1Tk82Kcc1nz5S41ZXNAaya9oI3wxGWncEEiZ1QAENGwAmItCpO18U5Bv62ZKNxXk1lsE2fi5FX6YF9Lqw3NCVC74V0Zg0ZRFAh_ugLhASU9ylWJ1EqUdOFb4gjs9RrmxWSf1CD-91NiFOrWmFcF6TuT7GjLSfO9g3pFbzVQbHNwLMnFD81A6_TDaEqCGmU5iLM57wJWDaMyzmNlWfNUYqaabqWjEjvTQQaPfFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جاده‌های مشهدالرضا، میزبان هزاران زائر پیاده
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/455445" target="_blank">📅 09:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455444">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb0nCqRuybtCs2kiGB1rMgHY0iUc8-_q111BKEMMW5fVRr36ktdyRyPd4hst-tTUVJyoMhRIvQ8XotXEnXBV8YAdNt4ZIMHlYwpkUCWZqr8_--dubRwYIrVBkliucLKqMpKMoFk2ZZH3Qno-HSkcfyUgpqo_rQ5qWp1fE5580sW58QmizJ9RFMzTHixrEsDPv7BUvWFh9G3VSJKP76KHj86M8U9Y71naBRxYqH86ajEtodfEGupKNU8PNCWq6ZAV0RNJ0bPDaaSTpdOYZeugHxr-K0MlkB7h3kULNx3IaAKTjK2cU3SzXW93qJW0YDjIkpBL2cvvsP-YVWQRu-bSDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سرنوشت‌ساز برای طرح بنزینی سقاب
🔹
طرح سازمان بهینه‌سازی برای اصلاح نظام قیمتی انرژی شامل بنزین، گازوئیل و سایر حامل‌های انرژی ساعت ۹ صبح امروز در کمیسیون اقتصادی دولت مطرح می‌شود.
🔸
پیش‌تر رئیس سازمان بهینه‌سازی گفته بود که دولت قصد گران کردن بنزین را ندارد.
🔹
طبق این طرح سهمیه مشخصی از انرژی به هر فرد اختصاص یافته و هر نفر باید مازاد نیاز خود را در بازار و به قیمت کشف شده آزاد خریداری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/455444" target="_blank">📅 08:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455443">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1760a6e3cc.mp4?token=e5YOuSSI9cJegvZG762IfJaUgzliQV4JfE194DSHipYb99nZK_cg8jHdTjD_i3zsVY8CmlhrXK6HS8mHPazFwdAJ5PCmrqMZyW0RjPsh62RYPQA1yMGVSm0_wV5oUHQOfpdL1IkfR5TH-5X05owSHJzzHN3VGmMPN2iFA_Bia7NN5LpbficJycFSnuNDRCN3vF3h3sHYaDikJMBtCUgMbcNh8UulV50r97B3sXSRVQFZ8RblpWXuX6R6fFIXzghDIcdPy93yCG8OE8HyrVDpTv81A3IGzJ1K-1_13JAQ3CVtsDZsPiopVhAOP3QrfQvjc3pJM4bVof7_K6rXItaAeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1760a6e3cc.mp4?token=e5YOuSSI9cJegvZG762IfJaUgzliQV4JfE194DSHipYb99nZK_cg8jHdTjD_i3zsVY8CmlhrXK6HS8mHPazFwdAJ5PCmrqMZyW0RjPsh62RYPQA1yMGVSm0_wV5oUHQOfpdL1IkfR5TH-5X05owSHJzzHN3VGmMPN2iFA_Bia7NN5LpbficJycFSnuNDRCN3vF3h3sHYaDikJMBtCUgMbcNh8UulV50r97B3sXSRVQFZ8RblpWXuX6R6fFIXzghDIcdPy93yCG8OE8HyrVDpTv81A3IGzJ1K-1_13JAQ3CVtsDZsPiopVhAOP3QrfQvjc3pJM4bVof7_K6rXItaAeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اوج‌گیری اسلام‌هراسی در انگلیس
🔹
بنیاد مسلمانان بریتانیا: هر ۵ روز یک مسجد در بریتانیا هدف حملات فیزیکی، تخریبی و آتش‌زدن قرار می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455443" target="_blank">📅 08:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455442">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616dbe674e.mp4?token=JewBQCcY8eJkjWCk5naEH8iIak8wzxiwOO5H7czuoWrtfvWN4s9n1mI72dUt5nyPiO45H_tOeWc6J4S310jac-UBm2sh0n7M23OOH4Qa80G5OLRuUgRSMml7EovI7aZTiEBDd_WL2Dokj3LAOuvFztG1t9abU1ryXvHiqY1_l_e8ZWFp6VGaSoAyfOCmOk33SXcKKVhBSerdULPpxs6cLDBB4hZSRT68vJi61v2h0S3Gv2GYv8zp8KyH7Y1pZ4pnEYjqglU8Zq9VPoiKglswECP43aNhRZ4rsn2FBLg2UdhEYPwhhPpLlOwq2qEhE7ZpIEdUijMNNp6CqQufwOVuSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616dbe674e.mp4?token=JewBQCcY8eJkjWCk5naEH8iIak8wzxiwOO5H7czuoWrtfvWN4s9n1mI72dUt5nyPiO45H_tOeWc6J4S310jac-UBm2sh0n7M23OOH4Qa80G5OLRuUgRSMml7EovI7aZTiEBDd_WL2Dokj3LAOuvFztG1t9abU1ryXvHiqY1_l_e8ZWFp6VGaSoAyfOCmOk33SXcKKVhBSerdULPpxs6cLDBB4hZSRT68vJi61v2h0S3Gv2GYv8zp8KyH7Y1pZ4pnEYjqglU8Zq9VPoiKglswECP43aNhRZ4rsn2FBLg2UdhEYPwhhPpLlOwq2qEhE7ZpIEdUijMNNp6CqQufwOVuSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضاییان: تا چندروز بعد از بازی با مصر از خواب می‌پریدم فکر می‌کردم صعود کردیم.  @Sportfars</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455442" target="_blank">📅 08:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455441">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qE5mZ5YnB08KvK4qHna9f9eKsIylWe6CzP5iYEgoy1fKC3FW5JOOPRZReJqYRzacRVZmjuEscXcU7orTu3PKcQIgUE0SzeSn-6h2P1448az4VLbhBv5pME1AbTgXozqXQOlR0i7UCPcGfOAIjIaO2rO4Th33rrjpI0_DDzovN3wDe-13kq61HmX7CcJGRAxVbj1HXsPLSKuHGlWOBQtuSaI-C8ba7T3XSk07jFvoNqChRsSQJNjbIr-CEDh1B-IKj61WTRgHrERIO2DLcm8LIxjxjYOIi35_EA4QYUIiJ7N9umugdvXOg6w_nq3hALdTlutnXLGSgabjTM3VcpYtww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیدر معروف ترکیه‌ای، قاچاقچی از آب درآمد
🔹
پلیس ترکیه شب گذشته از دستگیری صباح‌الدین شیرین، لیدر معروف اولتراهای گالاتاسرای خبر داد. صباح الدین معروف‌ترین لیدر سوپر لیگ ترکیه به شمار می‌آید.
🔹
حالا منابع ترکیه‌ای خبر می‌دهند که پلیس هنگام تفتیش خانۀ این لیدر ٧٠٠ هزار یورو پول نقد به همراه طلا و جواهرات به ارزش ٣٠٠ هزار یورو کشف و ضبط کرده است.
🔹
همچنین پلیس ترکیه یک قبضه سلاح گرم بدون مجوز از خانه این لیدر متهم به فعالیت در بازار سیاه بلیت‌فروشی، قاچاق مواد مخدر و تبانی کشف کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/455441" target="_blank">📅 07:42 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455440">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هوای تهران ناسالم شد
🔹
بر اساس اعلام شرکت کنترل کیفیت هوای تهران، شاخص کیفیت هوای امروز پایتخت روی عدد ۱۱۳ و در وضعیت ناسالم برای گروه‌های حساس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/455440" target="_blank">📅 07:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455436">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WNNLKKGmjMY4tItR52JZKrLZQXH9ZUujZppG5r75WTaY3K9KbTgpTXxHGENHCM_sLhu2X3nNMdqnrJW-iUh6X0avRdRoHyti6Y9q5S-cVk02GdbDGXYOwpbF02e8BxJAifh393B4NH3qGuXrQ2SjjYrd2H81WHhCfz6TeLCGBCAOLYRsbwhBktUnGH_5XpkgYqZgX7XDIoo5VOhN_ewvplplbZ_7WtNHPUq0RBO7QUw9sxMRmUVRyLHJxxMoXkwagg2yOpy8Ha_JRL5lZru2mhmtFroqQ2ffNTYMOVaYkiK4xJ0brUb_RC1VVq5xkcIw4njyu0gVDW_cBk8y4EtobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EI5HQpH4hsfDX5D6t3iyZRpO0sq8wGRjr8fX-0O0l6nlqZsfd48vcoJT7h03yuQbI5_LbjHvUfl0zviqmqV8wDtcCVBsaR9qEHgTNIcn7tQqNVcrx05yarK_v0FBk3Y5BfMBwjpwmnVGpoLSdUnz1wNnksDYIqgftJgfTdPFkPQNVULprRin_oY-_9ocfIOGMU7gnAKcw9o22BxqMfcMXK3C1VBXQ1tEq5uU29_MJbHVe2KfhiRjxXjQ6F9WEx0rHn38cbyG7XyrTWk8QSnxiNsZ51Fcux2bhsQHj7-se8IclisBTr6Mt8wd2OIKPkV7acEkWjNmh0ae_bqBxOHg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nZOu_uPd8wokuoquGMouv7e4uJytXSxxEklqrlKHHn8CptKthmf2yo45XJ5dPqeiLXQExyCX3ADI5Yv354AUb1dMkbrqlf11p6QjDp1Ws7QNjN8mk3ZP1yaj-Rbp3EBZKMh-Ibojq895cwrmvyAHZBDGB7nymBkpg8SgcgXPhYnjaEEY_nNiWdK-qTCV8nTGFsmPHWneD0MQzDrNNKdY74p3UKiT-GRCfSZo9tGF9WFdfDIzV2f7pNAcixBRGTwm9CzdxX1_DgVxUgs0GNeObuDGBTZrcKLK3c217lLEFovv8J2d2LdKZpiI0TUTwpHYuanlOym5Ho8xjJmKl36uLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac632d5b91.mp4?token=L6rif___MmHkZI07hBKHvQ0I5dDawcKZ4EbwyPDoJh4DOdFvFiPUpFJV7oggsWIMVrEEWf7oOVbpqJ96QEdUlF2NJNtpKF8213FT4Qco7NLw6qukYs1GTcZ7vJoLB-B2o7sXDvY7FceYkt99OLomdogxemq567bm8U3IEmwKHmtJ1GndoJtOEbsxfaGy3IKLJljOPzc1FoJEx_-Q2lNztyp5XfOhCT4P96p6oxsqLWdpoTrsO8Ow6s9vkV7AD0waZXvp2O0apXlpPLI-sW04lum5J4_fV5Af-B1iV6OYyUOpSxj0E_vAPVAJ8qasxNo3baibu2Hh3LaedW7GOgJHrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac632d5b91.mp4?token=L6rif___MmHkZI07hBKHvQ0I5dDawcKZ4EbwyPDoJh4DOdFvFiPUpFJV7oggsWIMVrEEWf7oOVbpqJ96QEdUlF2NJNtpKF8213FT4Qco7NLw6qukYs1GTcZ7vJoLB-B2o7sXDvY7FceYkt99OLomdogxemq567bm8U3IEmwKHmtJ1GndoJtOEbsxfaGy3IKLJljOPzc1FoJEx_-Q2lNztyp5XfOhCT4P96p6oxsqLWdpoTrsO8Ow6s9vkV7AD0waZXvp2O0apXlpPLI-sW04lum5J4_fV5Af-B1iV6OYyUOpSxj0E_vAPVAJ8qasxNo3baibu2Hh3LaedW7GOgJHrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سی‌ان‌ان: زلزلۀ ۷.۴ ریشتری غرب کلمبیا را لرزاند  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/455436" target="_blank">📅 06:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سقوط جنگندۀ اوکراینی هنگام شلیک موشک هوا به هوا
🔹
نیروی هوایی اوکراین اعلام کرد که خلبان یک جنگندۀ میگ-۲۹ هنگام شلیک موشک هوا به هوا در منطقۀ اودسا، کنترل هواپیما را از دست داد و باعث آتش گرفتن آن شد.
🔹
این حادثه زمانی رخ داده که جنگندۀ اوکراینی به‌دنبال هدف قرار دادن یک پهپاد روسی بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/455435" target="_blank">📅 06:37 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71faae8b44.mp4?token=uuhDH9GcsbRAwPuya1StqYKELpV-7_c6Ldx4MfuJ5qNFn_n6ZfgI1uS3Cq_kezVL8keFasPmEtxHDWL39BXhFZfMqnBj_SVjP1AQS-HFOSeE_N_HnBKMMvc1bvhvXyKpimeEICUwwr4O_fl6oi9PdtneH3p_9-NiQpklsejCCF380hDj-RB_osAh2LF6wBGsvutdoQeGBpePyogPo1jzcJaaraS81kGJtSGmo1BT2aVz3D_fh4a3nzOkuGiMc7SIQ4EFv0u-glTMmtBVQepZc9WUgO8NDbMvnEQGmMxtW8ngcWo70SaSS_AZ9iwnydBDlfTLu_AI3PRVTuCpKpHKqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71faae8b44.mp4?token=uuhDH9GcsbRAwPuya1StqYKELpV-7_c6Ldx4MfuJ5qNFn_n6ZfgI1uS3Cq_kezVL8keFasPmEtxHDWL39BXhFZfMqnBj_SVjP1AQS-HFOSeE_N_HnBKMMvc1bvhvXyKpimeEICUwwr4O_fl6oi9PdtneH3p_9-NiQpklsejCCF380hDj-RB_osAh2LF6wBGsvutdoQeGBpePyogPo1jzcJaaraS81kGJtSGmo1BT2aVz3D_fh4a3nzOkuGiMc7SIQ4EFv0u-glTMmtBVQepZc9WUgO8NDbMvnEQGmMxtW8ngcWo70SaSS_AZ9iwnydBDlfTLu_AI3PRVTuCpKpHKqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی گل عجیب با پایانی باور نکردنی
🔹
یک جشن گل معمولی در فوتبال برزیل به صحنه‌ای باور نکردنی تبدیل شد، جایی که مدافع کوریتیبا پس از تصور گلزنی و دویدن به سمت هواداران برای شادی، ناگهان داخل تونل کنار زمین سقوط کرد!
🔹
او پس از سقوط توانست از تونل خارج شود؛ اما VAR پس از بررسی صحنه، گل را به دلیل آفساید مردود اعلام کرد تا بازیکن برزیلی عملاً هم جشن گل را از دست بدهد و هم با مصدومیت مواجه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455434" target="_blank">📅 06:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6XVkS9BxHnJl9cmriFU3jHRSSTJ5pKJc_MIhAd5XEzIsNUKjCD8Z_sBxxd7xm4BqMxCs6tnTe4LwHbVdl5JUKqonk2RPfSDNjOpsBOrANWPqdWNhDomvEhcHXeQzvFm7QmLJXjzAIBokzhLq2OLq5_LWwRnXKvSuevcoWEm8PE0MCUJuS8ua1SHXTeOtAO6kAIj_4sqm9em-tJE_Du3fnY4T7wbPvfuEi5TAI4TdZ5-xbaoAaHb1rO1aNLKJ4VOBGvPTvJ3Kn0N2kzQyRIbnv_gTFv2a5D9L2HlwWuiknYmDHsc2bQs01exzKbJiwIPN2PVDKBk5o3d7S7fP5rpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ آمریکا به اکوسیستم تنگۀ هرمز
🔹
تصاویر ماهواره‌ای از نشت گستردۀ نفت در بخش‌هایی از جنوبی تنگۀ هرمز خبر می‌دهد.
🔹
این نشتی از نفتکش‌های متخلفی است که با تحریک آمریکا قصد عبور از تنگۀ هرمز را داشته‌اند.
🔹
پیش‌تر ایران اعلام کرده بود، خسارت آسیب‌های زیست محیطی را از کشتی‌های متخلف مطالبه خواهد کرد.
🔹
طبق برآورد تصاویر ماهواره‌ای، سطح نشت نفت در جنوب خلیج فارس ۳۹۰ کیلومتر مربع برآورد می‌شود؛ این رقم معادل نصف مساحت شهر تهران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/455433" target="_blank">📅 05:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajXOQP48l0m1nPSwaMJhQQFHMellJkHII45Fqcsdyd7eWhhUL6rDPPrTXMn-lWNsOxric-feei2WsbF-Rq8MZUPBh_Ups6MYuklHMNhLI1Ugkd0v8dVxhYTo8Xa6KPF_J1NVUca1oifyzpN-ObU0o0816CvezQLlDqLnS38OjrJal1SkL4NaQR96Wx7b1r7IY0dSeCKj44izxQAAB3Pubrf3SnJesJFUsjIytheCvZ5WgwL1U25J1ZRIYnGcQz6pzo7kt-xnzCJenajKZBAfM9lZQdJCsSN7qX5qMTYT9pAhBkXzZCwKDkilrDjoJqsrsCgvpXe3G0bN-jyPkntQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چادر بر تن متهم؛ احترام به حجاب یا اهانت به چادری‌ها؟
🔹
انتشار تصویر متهم زن در پروندۀ قتل حمیدرضا رجب‌زاده با پوشش چادر، بحث دربارۀ پوشش بازداشت‌شدگان را دوباره بر سر زبان‌ها انداخته است.
🔹
استفاده از چادر توسط متهمان را در گذشته هم در پرونده‌های مختلفی شاهد…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/455432" target="_blank">📅 04:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455431">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8319e8a5be.mp4?token=LQEsupL3cQ7x9HatzvLjXIvG245I0s_DJRZeZ3NOjPMVkrYqDs6X_3hFMANLpwCRHErj4u3XuIdXk3m3O8H15ZOrSU2HPxWyd64_2k6LJZ-zJmyjockTO_mLdQw3XPJ5lyISOrNE0diHHzMVCmmEJnL6drAYbO05CAiIi_9OioM6LpSgyNqz0d5r6tkPhInEkyhel25IYszsfsdMXPFazaOR4S9YtsTLItNl-pnidho2GqPHR-aBVsu6ufdNyysfDrpqQ0MOPXCoaArU86rGTB2_bQV03O4Y_46ah5BqGompkjMvj0Wqkhobv9PkvhHlSqhrV69tLry_U1xv1bNX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8319e8a5be.mp4?token=LQEsupL3cQ7x9HatzvLjXIvG245I0s_DJRZeZ3NOjPMVkrYqDs6X_3hFMANLpwCRHErj4u3XuIdXk3m3O8H15ZOrSU2HPxWyd64_2k6LJZ-zJmyjockTO_mLdQw3XPJ5lyISOrNE0diHHzMVCmmEJnL6drAYbO05CAiIi_9OioM6LpSgyNqz0d5r6tkPhInEkyhel25IYszsfsdMXPFazaOR4S9YtsTLItNl-pnidho2GqPHR-aBVsu6ufdNyysfDrpqQ0MOPXCoaArU86rGTB2_bQV03O4Y_46ah5BqGompkjMvj0Wqkhobv9PkvhHlSqhrV69tLry_U1xv1bNX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): نادان اشتباهش را نمی‌فهمد و نصیحت را نمی‌پذیرد
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/455431" target="_blank">📅 03:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyXXjdFVneO99mJIMKOkQCtizcFSZ7xQkpRy3LHYIeI6EK2WMUZqrIWXfXZRX0u4ncol1DUNqFsKTfCBENf42Zp8uu7wywOQgbBeNpl6eVA5AWIdyweAvCW8kDGm17hIfTmfKnK1yw9IKiPfAlWK8vm6xZi5TUy82NBGFoZfsBSfGOVjgAP3ElhKm-9UlBkxHvNyiPb0IKm2uhY1iA5ShiEOpwsJigKUuIrzQ5OJpcWhV6LBxUAmQwQluNlPKNOYoMxk7G7ZaNb6je610ZfTh5yPU8da7vL4GYDRTcBBxA_HvdVTEMcWzwKQZY72L1qvDMbMF_dXyca9_x0fbZGUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک فاکتوری ایران رونمایی شد!
🔹
رسانۀ تایم گزارش داده، اخذ اطلاعات، استعلام، اخذ بهای خدمات و در انتها صدور یک فاکتور تنها بروکراسی لازم برای عبور امن از تنگۀ هرمز است.
🔹
ایران این روند را «ترتیبات ایرانی» نام‌گذاری کرده و از طریق یک فاکتور شیر ۲۰ درصد نفت جهان را به دست گرفته است.
🔹
به گفتۀ این رسانه، حملات این روزهای ایران نه از مسیر موشک بلکه از راه فاکتور پیگیری می‌شود و این ذخایر راهبردی نفت آمریکا است که هزینۀ لفاظی‌های ترامپ را می‌پردازد.
🔹
هزینه‌ای که فقط در یک قلم سبب شده ذخایر آمریکا ۲۵ درصد تخلیه و به کمترین میزان در ۴۳ سال اخیر برسد.
🔸
از روز یکشنبه تاکنون نفت از نزدیکی کانال ۷۰ دلار به مرز ۸۸ دلار رسیده و اقتصادهای غربی و شرقی را زیر فشار برده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455430" target="_blank">📅 03:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc9HPTXuLADF7bE36gVUDvJC1Sr5-u5uAgiJliqFQZ4NklgmHtqxQ4w-lEjyT0FquQ7HG27U_pc8Znthm9AR1HPuD8MVZzyw4VrtjNHaXIwifBIr3Pjq3RE9GGWWT2EdLmGCSvflixcd7TGOalVPbQTS6msWB6PrumMcFMWyFCBOznFNb74gC0phae2uddfHp3_qWnprclX7ugAfacJfJgh5RtY_zeRFKAJlVQbiiPsTlhnxKPybedj5vD9CcQ5D4AmmS9-dALFRnXLqX1MhdL2zfXQA9-URuy-oQsOFtYEnFD17n9MB1C6Hmsz7K9oSbTdKBVIPdLNQv0A_-7Z4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپلمات فلسطینی: قربانیان غزه از ۷۵ هزار شهید عبور کرد
🔹
سفیر تشکیلات خودگردان فلسطین در مسکو: شمار شهدای حملات رژیم صهیونیستی به نوار غزه از اکتبر ۲۰۲۳ تاکنون از ۷۵ هزار نفر گذشته است.
🔹
در این حملات وحشیانه که با حمایت غرب و سکوت مجامع بین‌المللی انجام شده، حداقل ۲۵۰ هزار فلسطینی نیز مجروح شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/455428" target="_blank">📅 02:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455427">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPI5wgF_3spuNeVwg7HIe0p1gxa85TFpYIV9DHC8KwpGxJGNx5uhyPXjSJLEBWOuFgivXP9zJXINdj634sDJKGVwAAmjE8cKgBrSTPOlX_8b1x9Q-AIemR_SXnWEUEVzAl4rsHeuskO8owDbbxlmNr5maO4ZsCRU98Fdq7llepgYXy0Wz7JIuAnVS3Q6h9q7HDR7Kr3R19ArESbVG3hVODFUfOjI4VMD15ews_zw4LlRQYf0DJ2e8BQAxXAKbaZ6-5DZCaHQDqjWC9zVeMxirJS8c2__q0eykShRoBui8jiBiDhXKwyL9t72mK2ueKFyG04q3WSCrqBC6mb1MwQ_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدۀ هیجان‌انگیز تاج به استقلال
🔹
تاج امشب خبر داد که شاید سرنوشت قهرمان فصل قبل لیگ برتر که ناتمام ماند در جشن برترین‌های لیگ مشخص شود و استقلال کاپ را از آن خودش بکند.
🔹
باشگاه استقلال استدلال کرده چون در زمان توقف لیگ، صدرنشین جدول بوده و با همین جدول، استقلال به‌عنوان تیم اول به آسیا و لیگ نخبگان معرفی شده، بنابراین از نظر آن‌ها منطق و عدالت حکم می‌کند استقلال به‌عنوان قهرمان معرفی شود. سرپرست مدیرعاملی استقلال نیز تأکید کرده که «جام قهرمانی را باید به استقلال بدهند» و این جام را «حق هواداران استقلال» دانسته است.
🔸
وی گفته باشگاه برای این مطالبه، بیش از صد صفحه مستند حقوقی و نمونه‌های بین‌المللی آماده کرده تا نشان دهد در لیگ‌های مشابه، تیم صدرنشین در فصل نیمه‌تمام قهرمان اعلام شده.
اعضای هیئت‌رئیسه فدراسیون این درخواست را رد کرده بودند.
🔹
حالا تاج می‌گوید شاید آنها در مراسم برترین‌های لیگ برتر جام را به استقلال اهدا کنند. اظهارنظری که احتمال زیاد با واکنش منفی تیم‌های دیگر همراه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/455427" target="_blank">📅 02:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455426">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4c62bc0a.mp4?token=sNjQRfAWIxAUnHMNCnLXI_u6Owe_OAo8_FcX11YfhO6vO5Crui1oL0o-QvI28C85ZjFZAO2vJtbrF2N4Xw8JVXat7LoSeURoV3PmqeQCdm1eTzeG0BZNYgBwHfyAsZKpWp46noeMUe88QB3S8merEK9anj6oAndqaEOOv3B7_3IXnpoRQwFa2bdY1wkraTSm1mqjvs_4vGjU-sGNUflisEg4XmAQoWNqLrfpffi9rAF22i5nzWmINiPZuRKo8c6GBjbVmHsc0Xg5XNMzz8lLNSlAB8JWbuwZh1aA0nTqm1SPzLsqBi9Gu1cFwZCh0DA-7RRNL6zq45S5D8V35xHSiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4c62bc0a.mp4?token=sNjQRfAWIxAUnHMNCnLXI_u6Owe_OAo8_FcX11YfhO6vO5Crui1oL0o-QvI28C85ZjFZAO2vJtbrF2N4Xw8JVXat7LoSeURoV3PmqeQCdm1eTzeG0BZNYgBwHfyAsZKpWp46noeMUe88QB3S8merEK9anj6oAndqaEOOv3B7_3IXnpoRQwFa2bdY1wkraTSm1mqjvs_4vGjU-sGNUflisEg4XmAQoWNqLrfpffi9rAF22i5nzWmINiPZuRKo8c6GBjbVmHsc0Xg5XNMzz8lLNSlAB8JWbuwZh1aA0nTqm1SPzLsqBi9Gu1cFwZCh0DA-7RRNL6zq45S5D8V35xHSiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ پهپادی جدید به یک پالایشگاه نفت در لیبی
🔹
شرکت ملی نفت لیبی اعلام کرد که کارخانه ترکیب و بسته‌بندی نفت در پالایشگاه «الزاویه» هدف حملۀ پهپادی مجدد قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/455426" target="_blank">📅 02:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455425">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca8fd7a3a.mp4?token=soKF8Uq2_FoTBzJ6Y7jS_j0uG7hv65Jgl5wdipDmF6SnqZCX1VJzyL18pjJ8a33VJvU_9G3N7gBflWIVsXfqvKtLHMDLCrLkk1_oLxatC2Tl96c0Om8I9qWmQyJqlQFk5cm103_jS_PglcMSUp9Zg0wsUxsiTm0xNOx2bTL_I6a0r6JXQBWIf38H5lcIUpafcrjwtJI0L89-psrzr2uzkGQn86lnt1aoWlwejUq2fBRZTBMrRYe9ncw_r4nG2wTdcLVM7pedcuEUG3_ohA3HxO9NkzOCrp1SESpSnWG3NaZ6txrOHg3aShiPMgDWW-mMG4U5bmZhnGHv83feU8K3Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca8fd7a3a.mp4?token=soKF8Uq2_FoTBzJ6Y7jS_j0uG7hv65Jgl5wdipDmF6SnqZCX1VJzyL18pjJ8a33VJvU_9G3N7gBflWIVsXfqvKtLHMDLCrLkk1_oLxatC2Tl96c0Om8I9qWmQyJqlQFk5cm103_jS_PglcMSUp9Zg0wsUxsiTm0xNOx2bTL_I6a0r6JXQBWIf38H5lcIUpafcrjwtJI0L89-psrzr2uzkGQn86lnt1aoWlwejUq2fBRZTBMrRYe9ncw_r4nG2wTdcLVM7pedcuEUG3_ohA3HxO9NkzOCrp1SESpSnWG3NaZ6txrOHg3aShiPMgDWW-mMG4U5bmZhnGHv83feU8K3Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رامین رضاییان: تا چندروز بعد از بازی با مصر از خواب می‌پریدم فکر می‌کردم صعود کردیم.
@Sportfars</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/455425" target="_blank">📅 01:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455424">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شهردار کی‌یف، پایتخت اوکراین از حملۀ موشکی روسیه به این شهر خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/455424" target="_blank">📅 01:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455423">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2069b5638c.mp4?token=p_vwWCMO29xWw5BdAxzNYzDfO8oaBjZva6KXIDE4l9URC5JrrydhX7MbEe3KP7fsXYRyQg7cF5T6dO0YqSttc4BrlNLSvtLU6UR8XrFHfHgpYebIOZcfJWqRMs2gDQgt0CMW_Y4zv-WchoWJ4MGhXLHPXVXGsFd7mqW9e9iEYXnS3M6PK1a9Ie2_JeoE7npv-Q1RNBwlb6f1wrPFVjzkKkCmUyLdyA1Ir03_RukTLqpIh3B0Bmd2Cjkhfu6XDGqgzWMBfAakczIfxXP13wYSLQRPVnBkD1jWaT1WwS1c-Ues09Njbn0WrAysNkPqLRvCU0xhc8OC5etC1KvjUBvV-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2069b5638c.mp4?token=p_vwWCMO29xWw5BdAxzNYzDfO8oaBjZva6KXIDE4l9URC5JrrydhX7MbEe3KP7fsXYRyQg7cF5T6dO0YqSttc4BrlNLSvtLU6UR8XrFHfHgpYebIOZcfJWqRMs2gDQgt0CMW_Y4zv-WchoWJ4MGhXLHPXVXGsFd7mqW9e9iEYXnS3M6PK1a9Ie2_JeoE7npv-Q1RNBwlb6f1wrPFVjzkKkCmUyLdyA1Ir03_RukTLqpIh3B0Bmd2Cjkhfu6XDGqgzWMBfAakczIfxXP13wYSLQRPVnBkD1jWaT1WwS1c-Ues09Njbn0WrAysNkPqLRvCU0xhc8OC5etC1KvjUBvV-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رقم فسخ قرارداد باورنکردنی رضاییان با استقلال
🔹
قرارداد رامین رضاییان با استقلال یک سال پیش از پایان فسخ شد؛ چراکه بند فسخی در آن بوده که در صورت پرداخت یکی از طرفین لغو می‌شده است.
🔹
بختیاری‌زاده، سرمربی استقلال پیش‌تر به رضاییان اولتیماتوم داده بود که زودتر سر تمرینات آبی‌پوشان حاضر شود.
🔹
حالا رامین رضاییان می‌گوید بختیاری‌زاده، سرمربی تیم و مدیریت باشگاه علاقه‌ای به تمدید قرارداد با او نداشته و اصلاً با وی تماس نگرفته‌اند. به‌همین دلیل وی با پرداخت تنها ۱۰۰ میلیون تومان توانسته از این تیم جدا شود.
🔹
به گفتۀ رضاییان مسئولان باشگاه به این دلیل چنین رقم فسخ کمی گذاشته‌اند که فکر می‌کردند بازی او تمام شده و ارزش بند و قرارداد بیش از این را نداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/455423" target="_blank">📅 01:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455422">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حملات توپخانه‌ای مزدوران سعودی به جنوب غرب یمن
🔹
منابع خبری گزارش دادند که مناطقی در شهرستان التعزیه واقع در استان تعز هدف حملات توپخانه‌ای مزدوران سعودی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/455422" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455421">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaxmmJlCKQZfsHMv-TYROLH3k-CN-IiLWLSGVvsIoSoF72TXF_axp-UNc6GsLjTccxDIshVj3PG7QWR4YPYFyEmtRJFB2a3adv18IDdvAB6Nk1fKAR2p_y4lraNVtTM2Gpzs5Ise0BTDDssffAytPoqaIBecNZyEnmEXMwWIGbBmBIBHZstru8qp-JHSB0EgK8PjRcUmSNMkLEmBXjqamkFN8v9_hd7nw2YfX_AaLi7rZYOyYrLXIs8xl5j5YpEdMtwPDKTgAs2L9sBt_juQdii6eOagBbHEIUYEEFkdjHwzXoFBP7mEs12yNKwBme3Um_laD9lU6ctxjCJFTCBMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لشکرکشی نفتکش‌های عربستانی به سوی تنگۀ هرمز
🔹
گروهی از نفتکش‌های مرتبط با عربستان از دریای عمان به سمت تنگۀ هرمز روانه‌ شده‌اند.
🔹
ناوگان ترانزیت نفت عربستان توان عبور از باب‌المندب را ندارند و در تنگۀ هرمز هم باید ترتیبات ایرانی را رعایت کنند‌.
🔸
تنها راه بدون نظارت ایران و محور مقاومت برای نفتکش‌های عربستانی حرکت از کانال سوئز، دورزدن آفریقا و گذر از دماغۀ امیدنیک است که طول سفر را ۲۵ روز افزایش می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/455421" target="_blank">📅 00:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455420">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/699415d3e1.mp4?token=fyOHhWn2Xp8Ez8Icb8tq-7n_1xFjSRJHWYfVDZBGFFw2vPDjAl9OFJegWFpXgDJiB5M-rXB4lS2fBNwfs2OojLyYuuDPz_yZptdYd8QyYD7jCLN4YDwnBShY7wO2m0WDiEwkZpOMLzVR2bRiDkaXohRk1VwKZlJ7buIwGQHnuZDwYlut90z6amdiYjrAWjPXkgOZJ1DwoyY22hn0ITSR9EDNaUzVfol0UdkqbOvswRub95GCWAxfr3TSv9R3zcf6SLyHaeR-jV2VkOGh1gqSSPLx8CmJl8_3eeTW8g-hp9BjAWyw8ZDjkErv9y6hergHDqAIvd8pDQDyIavG9tY_oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/699415d3e1.mp4?token=fyOHhWn2Xp8Ez8Icb8tq-7n_1xFjSRJHWYfVDZBGFFw2vPDjAl9OFJegWFpXgDJiB5M-rXB4lS2fBNwfs2OojLyYuuDPz_yZptdYd8QyYD7jCLN4YDwnBShY7wO2m0WDiEwkZpOMLzVR2bRiDkaXohRk1VwKZlJ7buIwGQHnuZDwYlut90z6amdiYjrAWjPXkgOZJ1DwoyY22hn0ITSR9EDNaUzVfol0UdkqbOvswRub95GCWAxfr3TSv9R3zcf6SLyHaeR-jV2VkOGh1gqSSPLx8CmJl8_3eeTW8g-hp9BjAWyw8ZDjkErv9y6hergHDqAIvd8pDQDyIavG9tY_oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیال‌بافی ترامپ: تنگۀ هرمز باز و در کنترل آمریکا است
🔹
رئیس جمهور آمریکا شامگاه دوشنبه با ادعای اینکه تنگۀ هرمز را به‌صورت کامل از مین‌های آبی پاکسازی کرده‌اند، گفت که ایران اما هنوز می‌تواند مشکل ایجاد کند.
🔹
ترامپ در پاسخ به سوالات خبرنگاران در دفتر کار خود، مدعی شد:‌ «ما یک محاصره بی‌عیب و نقص [علیه ایران] داریم. آنها ورشکسته هستند و پولی ندارند».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/455420" target="_blank">📅 00:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mblb53ol9Mlx26pc6QQ8BqMRGSgJ-HjIvnY_VqJPVkDcctz3M19Qw0DyfFqGkMc-7Qt0otOrelfJ1kvSMGyoutRuUu4bKdGzsCLzg-6wX8vKHzbBzk-9LLHQFCOxSTmavOBQxNZpAm6EtQ2yGpc_YlQY6QZ3ZfTwtgNYttc5D2l7bVhx69VocBqWsrGdTenYRL7wP_nxEUf4kvLzjzd6brGO4gQsZ91NvJGmhbAt26X6SmaRPNFpJJn2tZ4MMIbkWNi541vpoHykTTT9XQxhyKghjMmzT7OcLkiclZLz3Fzjsw_44sGUujleq676PF4onvvJev8HtA1aKo03rurr5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzsqquAMC0oD-OkYKRb8hMCm2jMvK70ARrQ7oZFpHgD-OA-c2WeF2fjfqfE8hhgccZZbDvli2kyoPfJ6w3LXNW1hJ6hh5-M7s55UBAWx149Svo3bUWH9CmG1fIIpCbjBH3yQPExl7bBQHSc92hIyl7DE9A89oXyypzzDe0IGCfZcqIjsP4VfYTYRCpXkPjQVZGqnAGMD2IfplDiPhWaVWa4SDU40yNlUNBZzZVtxf3otwJO7dzVtW5Hs7-8UW8ddw_fDubr3z_2PoBxQpw43ncR9kyYq7W1k5Jbl22VqDbN9fWy7xVljNaa3GYK2WEewhzbgkAdIRzaI_6fzvMatJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtHY8vhECUfhzBDVV2UyooVfyLqhydNIiUw2TMRHOTozudjQQh6WI7EV8E3z8ugtMg1HNzSgmSwgBJpZdRCrQ19_rP-yMn1Er5QWH4EDzsHWSOdsKgy0qITRixnP86TsXXey3nQB3O0NvjS62-A04bN0WMZMhmt4lyd-alz8H_bcSoYM8pSksYxYXT3-pac0cZDDbpf3UP4u6BSDKcwPYsCk3Ua6o1k-vHePSazaFlbD50xyWO3iHLUcM61fAbDgNfCHlL1wsYQOML1Z4nN32USwubzpWvJmEJFOyHBDyvGTOl6FihENVDjEWlXawkiHasiS3kvzgexrN0d4QHeH_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ai4G2rfdi_CB9_UH-Kkuyc-dF9nnzxgQcZ1jIy_6e8oquKEQI4tYE4AjYY3uQvdT1xtkILN1YVkwQ1nn59omLqmdoqr8caeUgXCYERRzzi71IObO6e8VeMQYnntd9AxVIvCCrIxUp08oyoXA1dVdX2O2rr8WpTlGmQCe-vTzKDdJmp-tJxBOHZ18qZegltwb3-Wld5kjnGdnUf1pTNwPX4PffU6sOXJ3p1lCWVX1NXjoSPXuftiXtFXSQ_n5fVnw2zOomGtlNYlIyOJy997MLW9mIRy6dvtH9eaAZgAYbwiA04aQpPupoyp9i98207nc0g9S4mXcErmQuGIuHiLzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f1SC3AJlFm0bOsiERLJZ6CWEic12zbkcr9JxEL93Nw_a0YkiUgUnm67zW_o0MEOm-klLUL6tI4XCTDiFYHF3YPztF37XS_zJIQNym73O1CTDlUhvy3Vufgh6JYM8b011SgWGY4NlsiPbv2e83ZjCfsNhf1jYQdNznGPrlg61I-9a_O0opsooiVPIl8mACtEnqgBIF5ZD7EzfNp1tKrO5uMc4jSXCyLjGQlkK0deDjFgJWEhJaoGQJC-SeND0erWDNl4pj_PJMTFcT5MTKK3v9jTlCzpdl8CHmqrJXOrQMdnEoe7TanIiS5SwM_kCRkH8WzMCtSkPYpKzL2H2tbJnYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲۰ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/455415" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455405">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zyn9gjRoLpl7ZcwOEd0etHONZi_skilh1AflTACiSS8KZiQCAhD7Ss0yaDOToV6SLrdsr9XikGim3S6Nvw-wwyWpYoGVHhAIwO7ZPazciGa_Q2rTQdCMTyw5yKmks22VSpv3tz4hUGi4UDmdrD-zoiwKzMI61VLsxJhgVAoDDbt5BzpW8kYrwuC4up9WZh8rNCW9mKrhPDG63tcrIkBzV49Gsk_PXK99hl3iMnxIAzs79sw9OTf2YPKQrPq1X2ylDcbS-As0oEMWP4JvwOvL0iWA3BAAk4l3fz9fNxe6wmRgGMuJ4848y9mJNY64arJFadMzWl5MsK_KAvPs9FnHGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bJ5FKXTQLX4KHhbA57xYp_a4-gUXAyJRr6XoD7nsuDPw2dGOLMEq7R3o1JPSQ84-27DYFQwa2-5kAkUuKNuUNI42ji1XZAsjc8qi67Ogm-38lZ_Al03jQzQSTdyqhajHG71N8crAZFz04gJSL4YKF9_ZP3_R8pmlCeoe3PWXZv18hE2BNgzq7DU1cXuTVi6ljuWZRSLnPFapWrJiQqaNC5PXh8mUsImbiK9oLyDs_HmOs2Bm6eflgq7iIF2wX7eBUbc7vYCtsCwKl1mBr7-XUkKJ6pwLF0R6by20SmA9hV8yUSiyxM7juNFtNEcmRO6s1CprWlResxfvjpKgIIvvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHq6TDlYzfar4q0ssva25Fo3VfqncdpAVH1lu7I5-DSsbGXAuPxQwhysuT2rWg63LIhbIyLE8G0MOifr7-6cwPv6iZBBLi7yPDImaEdwpwizMPAp30_coCuuOgXxLBr0HRWyopfXIkm5elE8TLE3JGbcnRFj6u2QN1k6dIkoz8kuIVIcSMFvWgRN1oiX5YHss9xwx7hBR1V5Q2UaslduL-QFbnPZFNa8a1PHqfuQG2-GnkFlreg-u_ORELaarqAua5nZzQI_HilrE7lzAD3pFE_4tVLrQ5fp6YIepc16R6X4eu9TAVLREMARDNPjVgiWjNCdwrDTjDuHVaD5WJQ5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVWN8XTUZGm0vX_xpzPUYSSpW3tnOIFZkEIx8v626bscnQ78fbR0Rmxml9xREOUn8ebtEXMIuYpBMdyn7Rlzt7_csCmwtpgCNB3D_pxWbeowlQziORWhvtbl4IC2pnO01gcnCepnPieEEzMBAE3iPxuu065nle7jz5eJz9z5Oqo27yYL3oiEHPeT3DbVqjsbMsqV-FkWUvU_LMM6lgf5ml2iIYYLJjdE4H6Cvj0HG-ldSYLPGIctjJ0YGXnOU2WCPNunmmI_rW44RRKskz1ayifksL_Qneqpk5MpTxhSkz6AcOXAdxMZV1EuEtZUg0MDMMYm7L32AMPOZEPtLtdFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vx1c2SOGWn3g8BfL36OxPb1B9mM5xjmjQ0v75SGUznctuaOK9z1Ucvk2Aino3G01EsejRpbC50x4Iu6xUG_YjNYjOI4FfWErfIBFFbuGk7yljsc1yBJ8Gcp8E5A1sEkxbK8f1f-aib2KrWSwcsazs1rM0r9jpeozJQWSkT4kZbWWjGs7SFjy_pVCNlVlCp_tXBygXLsS89eOyGC-NBnqJLPUBVUW8I4zGdelkbkUeh2xxsMCBoIe3hfiClOJUG0j3mswqvLGiwEigaVm6zqvLHPMwhRRP7zx4Y3SVJQaKDinKzZUmC-ykV04Abtvm_lR7E8MIV7cTJRhnVVJv7BzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/shigRJTHPAnLcP6xpqTuXY2zugrqT9Eue9KcVSHJfhO9isDkMtCO_Cc0MhPFGsSmEuynQe5JIq_iBvD3I3wQGgky4yBmQsaDiG0Gw2041IFObrMixtO8fsuGcIdQJx0evAjih5rQq7SJ8EFAl8Lkklv_GfoeuMfdPWCVjYFhtt3fqZPOZi1YSTRk7Uet7J0NjNuYAI-1OvOy_2KT3qgBE9l7CJFszdybO7SlDcubj9xQyeHz5tRZ6L8yq8QyjGZanOXGhsAbdVz7zjU_k07n9DTKMYgS0nkfPqzOBrh2t8wIcGW1xnHGOSmCXA2H-sSstBt_CzX-h_YyMEfCYv1QJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpAipUnTMrW7tM3w1w2YtiLEis0KPHyL7f-ld0i2Wasxs9dGlp4Cn2qJTqLn4L1lG43JRavTD1bCVNOeYcxWnqEVeEe3ydiVlVw1j_zSFPvqynwsLPccholh-7Aj9FCdGVXEZRWwbZPnOqeabPrAjZxEseWJNKhbXYGfIOMyCyB-VByB0Rr4RqH1kkVwlM63vjaD7cT53kz-UuItbF018rjTyzudgK0Olkkjc7f9kF1_TwkWzX6KKuhA7lHDU5uKA_CPx7n1NXteKPucqe_VzzakGWK1cDpso2_lxZtpE5OPNtfMOpyfmyZtl0sEplsbFXDHwc-m_fT8Gnp8M8jPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PH6kcQP_Xgo_W9MYIe87inqyXCnzGKdSOc0gl0l94GWjsa2mnGy6GON6Oo8CQ8EOarqbUHy23SMZWZ1dy1smCqzF28-wcO6bIaYuj136Gje6BANE3QuJIDj6OV3cdBCmPevaxwQnrvI2B_EpQIDOrQowJM0EsCsv5ZYKqYjmxSF5ucka_-yDaP2jXP6tjfUvRxiCdEP_K4QjRGNK0duWFbaiVhWahpPph1wu8th3A9X5zvSPdXbewbLxiCq0_4mlKaynJSfwkGvN-sHdn-LC8LtNciLbjLMreP7r64sRTraAyeNs_St2VtkLE7Zp1KcF0eDyJAap8kl-qgpMcajbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBFkmfcPUFZduVz7eP-aC-e5qlrxJdgG9E4S1dnpzU0Cx4YjDA8nr62gCeDnDHyC8O7m90IVj70GBnqyIckZ-_9ynzWJxcVxizsOfhDeYSDlvOQPay7gPpe3ZAFLKmV4XHMnz9K-YOWbgHsjdJIcvNSV8L4IDCjuNipSacq9po9gYapLTeDUf0_-endL-BoqKlrkYAYWJ-GZEqtqhfaFaSpBltNa-IGovXNttZEhKs_BZ7EFcQPQxF11Blip-Va_68O2Mlb3GAs_9BjaH2INexoj_az2op5-HnMft1yLxX5g8FeWkc2wH96dUNJFAh6duM_Qd89kA9f6uYXxlldXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4X3ZnEmC2NH-7yvlDIMp2yOJ4MsKlXs1YWDElrgzKXwcX1bKmnRogNiTHt-GQIIqeGoI685o6xZY6DLeaZltr2DAgchR4NCurYrqpE0D8cq7f9s5kTGWGLUhdFXXdxC6-OKVU2uKqWPlEQBZ5ijcDf5c09R-1_ApRLtOjC1SQkq_G9jbIi7YnE942TlVfOJmh0tX9uHBgAlmxgi-_VHzSgLQRuIfj3wiqzHBfo77iUrNPR3vA23kzuQzUXvvFmx_BOR-eIVaBJMNGWoiDjrTejSxUP0eO-oyeK2ZnhVrTU3A7ws4vovls3kKXw3n9G42vFm0rOwEBg5vwPIvPUvyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/455405" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455404">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4136877665.mp4?token=ZyXADOrIrzn7JamP5YmWH6dAe2QgrGmuFhCyyBHTRgdO9lfQSLiEc-wpxPDhLevoaDP1uNu2MGrGFqT9CMQCFV3A2jbziwV0CmLDkx5P83cHVKMZ7_Y_uFfcqaFBFBBKi-3Sprv1Vgxh1_gM43RibZEMEmjI1MY2qoQu1iQNpoCkGbGpIdUWMjHVSjELzXoMUnACKKHc8KK3uiPlPl5uJ-u0ZUNXiy45ozZzXK1Qi3BzskTEqXFS7AC5KTzZK94xwEtc7PF7nz7eTgB65XkdkBiAhhlLi9myYWO83zbHTJdybfuRAEtlGztXEBasjVuMmHK4RKT7a-B8wlBEuDeA-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4136877665.mp4?token=ZyXADOrIrzn7JamP5YmWH6dAe2QgrGmuFhCyyBHTRgdO9lfQSLiEc-wpxPDhLevoaDP1uNu2MGrGFqT9CMQCFV3A2jbziwV0CmLDkx5P83cHVKMZ7_Y_uFfcqaFBFBBKi-3Sprv1Vgxh1_gM43RibZEMEmjI1MY2qoQu1iQNpoCkGbGpIdUWMjHVSjELzXoMUnACKKHc8KK3uiPlPl5uJ-u0ZUNXiy45ozZzXK1Qi3BzskTEqXFS7AC5KTzZK94xwEtc7PF7nz7eTgB65XkdkBiAhhlLi9myYWO83zbHTJdybfuRAEtlGztXEBasjVuMmHK4RKT7a-B8wlBEuDeA-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ آغاز تحقیقات از متهمان اصلی پروندهٔ حمیدرضا رجب‌زاده
🔹
سخنگوی پلیس: پس از دستگیری متهمان اصلی پرونده «حمیدرضا رجب‌زاده»، تحقیقات توسط کارآگاهان پلیس آگاهی دربارۀ علت و چگونگی وقوع جنایت در جریان است.
🔹
همچنین متهم زن پرونده که درحال فرار و خروج از کشور…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/455404" target="_blank">📅 00:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455403">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9IbzrbNAJm3YDHhdWHUe7Y3BPbrYO4qn5ymbv18p1JBmY7q5kKQGLiwaNP8qtpIBwuMP8N1xjWbXibN6lf-wYj_Jrm8ShiceF4iz79hP-Tyr0sG-lDu8piUhi90Y834H_gZJbYbC_jrArU-0rWRtjho5RxMiSpHjdsehMRDaFJFYn-hXoatcdyZ_nUUGobID32mqHUrzvgKOoVyzCbZzmukm8OxSwoQNCBXnRQDx6ka7-Yz4OABt3JqntXZjP95vpGMf0BLZ28FC_nooQPhsohIvQQACq0-sXE-cOwnjSI8fFrkAtJDiqvuUNjjn8ARIwsselwQkrIx-26_Ts69hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: جهان آمریکا را به خاطر انسداد تنگۀ هرمز مؤاخذه کند
🔹
وزیر امور خارجه در گفت‌وگوی تلفنی با همتای آلمانی: ناامنی تحمیل شده بر تنگۀ هرمز منحصرا ناشی از تجاوز نظامی آمریکا و رژیم صهیونیستی علیه ایران است و جهان باید هیأت حاکمۀ آمریکا را به‌خاطر پیامدهای امنیتی و اقتصادی مترتب بر انسداد تنگۀ هرمز مؤاخذه کند.
🔹
امن‌ شدن تنگه هرمز مستلزم توقف اقدامات تجاوزکارانه و مداخلات غیرقانونی آمریکا از جمله محاصرۀ دریایی و دیگر نقض‌های تعهدات آمریکا است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/455403" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455402">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280903eb5d.mp4?token=IuqGMITqxod-1ZeYs72kAyUO9AIbmF0w3-N38lp3bdvX97gCp-J789XJ-7rGA7Hn7vwdXdVCywa5F2kFs2bXrW7EvNTv4V8JxYsr8LUzrAXfqD-l0N71UgfLOQPwzlEx2IfmvjSu1wlvnVYMRRvwuowqnHBMhz1ItUNFzgzeJ7frgZDpsqwBV_Wd0GgePYArJStWtOrs2Qr5hPXTGRkEFpfh82f1U5yTv7HbFE9QPGq7hFl1qM8iawe7dcSkgfjl_IxD99zeGeIjXQXRQDx7StT39xsubMBA6w6iezNtMKTFgqnvkipfFe0FOkuHHNVOE0m80Qtv_xXtQuVkYClK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280903eb5d.mp4?token=IuqGMITqxod-1ZeYs72kAyUO9AIbmF0w3-N38lp3bdvX97gCp-J789XJ-7rGA7Hn7vwdXdVCywa5F2kFs2bXrW7EvNTv4V8JxYsr8LUzrAXfqD-l0N71UgfLOQPwzlEx2IfmvjSu1wlvnVYMRRvwuowqnHBMhz1ItUNFzgzeJ7frgZDpsqwBV_Wd0GgePYArJStWtOrs2Qr5hPXTGRkEFpfh82f1U5yTv7HbFE9QPGq7hFl1qM8iawe7dcSkgfjl_IxD99zeGeIjXQXRQDx7StT39xsubMBA6w6iezNtMKTFgqnvkipfFe0FOkuHHNVOE0m80Qtv_xXtQuVkYClK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یاد شهدای میناب در محفل عزای حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/455402" target="_blank">📅 23:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455401">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUHepa_Q2_gZCL5UhRcceplOq7vETDbwnQkZCcbHm5kTwUG14XS9HgIzNeSp6a2l9nFP5776co0ZezmbRFBqPR7F2jg1s04Bk4J07YI9fWpKXovxvj0OeHQgfdakygHGGPbgdz4ydIstadmohriP5oIcYeQJ65hMDcEgnERx65r_WiaiOPp_1b16199W-wD_K0lmkre2faQWTLz0u3wLCUxqkzCntJP8R3eUb6Mii-FmfvYGNedo26ZpexZkMzZ4bY_GRmWsRuHygzBOaOC4Z5ZupLgFEBZEdrRUldCvaTaQ3ar0Bkh5xmOFdgeiI8subTVZm4Xri0zOVuwBN4BICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چادر بر تن متهم؛ احترام به حجاب یا اهانت به چادری‌ها؟
🔹
انتشار تصویر متهم زن در پروندۀ قتل حمیدرضا رجب‌زاده با پوشش چادر، بحث دربارۀ پوشش بازداشت‌شدگان را دوباره بر سر زبان‌ها انداخته است.
🔹
استفاده از چادر توسط متهمان را در گذشته هم در پرونده‌های مختلفی شاهد بوده‌ایم.
🔹
یکی از آن‌ها، دختر قمه‌کش شوشتری بود که با موهای باز مشکی‌رنگ در میان اغتشاشگران قمه می‌چرخاند اما بعد از دستگیری با پوشش چادر رنگی  در صفحۀ تلویزیون حاضر شد.
🔹
یا شبنم نعمت‌زاده دختر وزیر پیشین که مانتویی بود پس‌از محکومیت به فساد مالی، در دادگاه‌ها  طوری چادر به ‌سر کرد که فقط بینی‌اش معلوم بود!
🔹
پلیس به فارس گفته ما الزامی برای چادر سرکردن افراد نداریم اما از آن‌جایی که متهم زن باید حجاب شرعی داشته باشد در این پرونده که متهم پوشش نامناسبی داشت مجبور به استفاده از پوششی شدیم که برای این مواقع پیش‌بینی شده و آن هم چادر بود.
🔹
کارشناسان می‌گویند که باید برای پوشش متهمان زن تدبیری ویژه اندیشید؛ اختصاص چادر برای متهمان بدپوشش، از یک سو بی‌احترامی به زنان محجبه بوده و از سوی دیگر شائبۀ مجرم‌بودن زنان چادری را اشاعه می دهد.
🔹
برخی کارشناسان هم می‌گویند باید پوششی دیگر همچون مانتوی ساده و بلند را در ورودی مقرهای انتظامی و امنیتی قرار داد تا متهمان زن درصورت نامناسب بودن وضعیت از آن استفاده کنند که خرید و اختصاص این نوع پوشش نیازمند تغییر قوانین و تخصیص بودجه ازسوی دولت یا وزارت کشور است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/455401" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455400">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
حماسه خون‌خواهی و میدان‌داری کاشمری‌ها در شب ۱۶۳
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/455400" target="_blank">📅 23:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455399">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cb4fd355.mp4?token=CH2pjvxM2qUtjtD0eE3i8cWofwS5rLjX8rfRMxPyvAwC9rCkiVTyughNRApsK5b_2_k5Qwlo47v-MoC5g9HkkUxIAeUzgugcacWU8iv3pwQclKlGzahnVH7ykbuC05G71Mm9Vush8G_vHj8keiZ9486RuiwCqNa6jMS-QnFToSO5yupo4PQQwyoGN5T_uMcCQtKSzWtoXvIkcN5DE3wJmZflef2QlAtku11LnHAV_kU4KMjie_XBBpzVnMFUZam-szLiD6gTStvKiszmPJJ07uXXZxLTZcZ1mSAuBtJlTdL_ikHjbeM6W2lFEv2xnEate3S1NjCmMLAAah3rXHnmfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cb4fd355.mp4?token=CH2pjvxM2qUtjtD0eE3i8cWofwS5rLjX8rfRMxPyvAwC9rCkiVTyughNRApsK5b_2_k5Qwlo47v-MoC5g9HkkUxIAeUzgugcacWU8iv3pwQclKlGzahnVH7ykbuC05G71Mm9Vush8G_vHj8keiZ9486RuiwCqNa6jMS-QnFToSO5yupo4PQQwyoGN5T_uMcCQtKSzWtoXvIkcN5DE3wJmZflef2QlAtku11LnHAV_kU4KMjie_XBBpzVnMFUZam-szLiD6gTStvKiszmPJJ07uXXZxLTZcZ1mSAuBtJlTdL_ikHjbeM6W2lFEv2xnEate3S1NjCmMLAAah3rXHnmfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خون‌خواهی رهبر شهید بر دستان بروجردی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/455399" target="_blank">📅 23:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455398">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52d79a4d93.mp4?token=EReY_QTf8g9FC0b5gE9rdt0qugnP8YcuRsvRnUBvy9N8nQrS0vHv23U875N48iCz72LdEKrPltfzyFCBZX7hO4HJoNLiVlR0TJ7y_8Iw2AdiS4mU47VqhfkwIuVHGtXp_pkxqv1X-sG0GT59DJ_cqG98ZeseKjg4rzu5zsI_ZvAT0zjUCPwCpz8eNOU6onYrwWyyTEfOrPp0BGbuk4iXPlAgiD7QuwnT-W2UOqH8BEMBiImltqP6o11o739r9IBGRSYKBlVIEFbz30Nv2Ch3uyqwoBQIQwMawMrznEsz-majO0sHrjCpgEK2p9DCMJU0R7d6mlg3IydFsXFCkz_tZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52d79a4d93.mp4?token=EReY_QTf8g9FC0b5gE9rdt0qugnP8YcuRsvRnUBvy9N8nQrS0vHv23U875N48iCz72LdEKrPltfzyFCBZX7hO4HJoNLiVlR0TJ7y_8Iw2AdiS4mU47VqhfkwIuVHGtXp_pkxqv1X-sG0GT59DJ_cqG98ZeseKjg4rzu5zsI_ZvAT0zjUCPwCpz8eNOU6onYrwWyyTEfOrPp0BGbuk4iXPlAgiD7QuwnT-W2UOqH8BEMBiImltqP6o11o739r9IBGRSYKBlVIEFbz30Nv2Ch3uyqwoBQIQwMawMrznEsz-majO0sHrjCpgEK2p9DCMJU0R7d6mlg3IydFsXFCkz_tZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع موج ۱۶۳ در چهارمحال‌ و بختیاری با نوای نوحه‌ و سینه زنی همراه شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455398" target="_blank">📅 23:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455397">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lplJ6F1x8n57_I0HK1mJtJadSqamTbvoke8Yn-lWmUZTDT42RsNu2iJXOgRht4L4lZy8U56B_ecemvoz96nY_gnur04qO-xY_piFLrtvB5uRQS2KXT4tcjtQ9HDQi0jMvj0BGj4ntSaBsP1JM0UnF5QbNmu6R7LYMD5b862E03cQVjWbSiTV3S-F0PUz6zztWxbPbWN3RXhRNDC5skMNvONFuKTC-ny3CDO2WVseWVzMQ5rgmmXqHP1Kj8gntZQF-CuK4j_Wqa98s5_GWWPNFm91_r1gOVBILJxo_-nQEw2oX8LXfs4hmp_h01oHtWpFuSVkIgme52-sbmJzEPCUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاج: قصد داریم قرارداد قلعه‌نویی را برای جام ملت‌ها تمدید کنیم
⚽️
اعضای هیئت‌رئیسه اعتقاد داشتند که باید برای جام ملت‌ها جوانگرایی صورت بگیرید که این نظر خود قلعه‌نویی هم است.
⚽️
پاداش آقای قلعه‌نویی به‌عنوان سرمربی تیم ملی ۷۰ میلیارد تومان بوده است.
⚽️
در فیفادی پیش‌رو ۳ بازی تدارکاتی انجام خواهیم داد؛ بازی با روسیه قطعی شد؛ ۲ تیم اروپایی و یک تیم از آسیا که در جام جهانی هم حضور داشتند حریفان تدارکاتی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/455397" target="_blank">📅 23:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455396">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4cf20f78.mp4?token=C1eWvLuRniDee2ii5tRbhlISlDhljWNvsYYUZPLOjDAznryNRgiZZxZOzYZUp0e_8j8-4SpVfki_WxYvpG-iaVkSzJR8KZTyMxWMXjlsGQlr1eSSEFciUsYi6Mar2Z_qLs7DDf9nHeEBlCBk58NemPaBFnmtJNTizoKSVuBnbWO5EyF9AeVfhRlB8WmvQbkDM2vAnq04odSbmpmS4YuoW-JSVC4O8jo_OvbkeYmEMV0ONpuEvPT-1g3rLwQog60Hi_dlZAx1BSdnmCdMOOtgAupwFwPWr1HcIz83XBcog2A6uFrPUrEDTFtwfIfpWOlQU6Z11tevAcy3lLADG5TdPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4cf20f78.mp4?token=C1eWvLuRniDee2ii5tRbhlISlDhljWNvsYYUZPLOjDAznryNRgiZZxZOzYZUp0e_8j8-4SpVfki_WxYvpG-iaVkSzJR8KZTyMxWMXjlsGQlr1eSSEFciUsYi6Mar2Z_qLs7DDf9nHeEBlCBk58NemPaBFnmtJNTizoKSVuBnbWO5EyF9AeVfhRlB8WmvQbkDM2vAnq04odSbmpmS4YuoW-JSVC4O8jo_OvbkeYmEMV0ONpuEvPT-1g3rLwQog60Hi_dlZAx1BSdnmCdMOOtgAupwFwPWr1HcIz83XBcog2A6uFrPUrEDTFtwfIfpWOlQU6Z11tevAcy3lLADG5TdPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۳ شب پایداری گنابادی ها در حمایت از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/455396" target="_blank">📅 23:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455395">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8836ef1e8e.mp4?token=u0GX4a3GNCeGGq28XXbolKSENuPkHmQ5plFxQcDA_kfRXlUoE_YvweXE5pOTeH450hJBrneaGE9C0o930NnoTvgr8vdbCBI1EAQthxXLD8OmDWQJunpCsuzQlWEx8oCpZJu91sehr9oLhXwdqJOyAY9aG53_fhGriVl5OrBq9rMd_NJ_Nv0u5CQeDpC7huIvfhRs4veyj4Nfq-kJVxwnXYb8lzDyI5lBbZK7TR68za_J93xYwaZbZ1mPONP0CLVAD9yb2oCa54uSh9NWPYnplqnToecceh-LWCd7QpyE6l2Al4tRYwr_n-yytfle6Xqgqj05cqyQXKtyC_neMWWe1U0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8836ef1e8e.mp4?token=u0GX4a3GNCeGGq28XXbolKSENuPkHmQ5plFxQcDA_kfRXlUoE_YvweXE5pOTeH450hJBrneaGE9C0o930NnoTvgr8vdbCBI1EAQthxXLD8OmDWQJunpCsuzQlWEx8oCpZJu91sehr9oLhXwdqJOyAY9aG53_fhGriVl5OrBq9rMd_NJ_Nv0u5CQeDpC7huIvfhRs4veyj4Nfq-kJVxwnXYb8lzDyI5lBbZK7TR68za_J93xYwaZbZ1mPONP0CLVAD9yb2oCa54uSh9NWPYnplqnToecceh-LWCd7QpyE6l2Al4tRYwr_n-yytfle6Xqgqj05cqyQXKtyC_neMWWe1U0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجدید بیعت گرگانی‌ها با ولایت و انقلاب در ۱۶۳ شب حماسه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/455395" target="_blank">📅 23:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455394">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3156abfe8c.mp4?token=qmuNiDvxDn6l5WlOLdf8gpFTDdooR1ZmyQld-49aZbFEuTuMZPTF-lxxBGo34EgCADDXB016WyJ3rPDHXhDSyFQkxf3pYyqZlAQ3TtgEOKhhRXQ996P1Pomg9WAc13B6iqxLNuNP5Q-cFWThhMxlFD8AqxIXKzI2ZIOzAw9-Nla0P8rwtEevQuoB5DZj34WYEuXyyPyNo3NP2u8FOGd1rv4lj0XRHNTnWKWugXIA7pgcu6BeWyHDzYfihLBe6tiyFJCCVxTZVnwRr6ZhEoZ5X0td71oQ2jdV89aUGP6NDUzHZnIsjgd8ODi7nclhxQHlhdJD54ci35V1-Rn0w2rr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3156abfe8c.mp4?token=qmuNiDvxDn6l5WlOLdf8gpFTDdooR1ZmyQld-49aZbFEuTuMZPTF-lxxBGo34EgCADDXB016WyJ3rPDHXhDSyFQkxf3pYyqZlAQ3TtgEOKhhRXQ996P1Pomg9WAc13B6iqxLNuNP5Q-cFWThhMxlFD8AqxIXKzI2ZIOzAw9-Nla0P8rwtEevQuoB5DZj34WYEuXyyPyNo3NP2u8FOGd1rv4lj0XRHNTnWKWugXIA7pgcu6BeWyHDzYfihLBe6tiyFJCCVxTZVnwRr6ZhEoZ5X0td71oQ2jdV89aUGP6NDUzHZnIsjgd8ODi7nclhxQHlhdJD54ci35V1-Rn0w2rr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گردهمایی بزرگ اندیشمندان شیعه و اهل سنت در حرم امام رضا(ع) در آستانه رحلت پیامبر اکرم(ص)
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/455394" target="_blank">📅 22:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455393">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آژیر هشدار آزمایشی فردا در جاسک هرمزگان به صدا در می‌آید
🔹
به منظور آمادگی و ارزیابی عملکرد تجهیزات، تست آژیر هشدار توسط نیروهای نظامی از ساعت ۱۰ صبح سه‌شنبه در سطح شهر جاسک انجام می‌شود.
🔹
این اقدام صرفاً یک مانور و تست فنی است و هیچ ارتباطی با وقوع حادثه یا شرایط اضطراری ندارد و شهروندان نگرانی نداشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/455393" target="_blank">📅 22:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455392">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c800cb1309.mp4?token=Z1IgtI9tTo3tF5uz3scUVcA3rwj03MlsLtjwcVmp1pfBTIzNc63msbOV4sHc4UgqZOA_RCS9RZqFkCC_AruOrDY7sROwjXiR2pC8lP6_SuSQtXYTVhGu5TNSkdWcfCYRAMA-S0TtgUXqP4kbOgt7d_MHDw-anyf4XD6-r9vbSpvGg5lak3WikqOqIcGPx9Fsl1tqrRSS0KOfZdQD-ak94deANaROq4gq457IVjZMivc-XF2MkO6xV06UxT8coIYAFN4nTyZodP10GOaQE5x540xdM2heQz5y_8xb1DcRwVJYH0OuIdaPF1h3cvQus13CUsSQbdDhnHuKZUlcIvSwRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c800cb1309.mp4?token=Z1IgtI9tTo3tF5uz3scUVcA3rwj03MlsLtjwcVmp1pfBTIzNc63msbOV4sHc4UgqZOA_RCS9RZqFkCC_AruOrDY7sROwjXiR2pC8lP6_SuSQtXYTVhGu5TNSkdWcfCYRAMA-S0TtgUXqP4kbOgt7d_MHDw-anyf4XD6-r9vbSpvGg5lak3WikqOqIcGPx9Fsl1tqrRSS0KOfZdQD-ak94deANaROq4gq457IVjZMivc-XF2MkO6xV06UxT8coIYAFN4nTyZodP10GOaQE5x540xdM2heQz5y_8xb1DcRwVJYH0OuIdaPF1h3cvQus13CUsSQbdDhnHuKZUlcIvSwRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کنوانسیونی که زبانِ رضا پهلوی را دراز کرد
🔹
همزمان با بحث‌ها درباره کنوانسیون رژیم حقوقی دریای خزر و در حالی که دولت مسئولیت نهایی آن را به مجلس واگذار کرده، رضا پهلوی نیز با فرصت‌طلبی خود را مدافع تمامیت ارضی ایران نشان داده است؛ موضعی که با سابقه خاندان پهلوی در حاتم‌بخشی بحرین به عنوان بخشی از خاک ایران و مواضع اخیر جریان سلطنت‌طلب در تضاد است.
🔹
رضا پهلوی که در اواخر اردیبهشت امسال، برای نام بردن از دریای خزر از واژه «بحر خزر» استفاده کرده بود، امروز شهامت پیدا کرده و با اقدامات نمایشی و نوعی ملی‌گرایی قلابی، نام «دریای کاسپین» را به زبان آورده و به خود اجازه می‌دهد تا درباره تمامیت ارضی ایران و پیامدهای حقوقی این کنوانسیون سخن بگوید.
🔹
نکته جالب توجه اما تناقض و رویکرد دوگانه پهلوی‌چی‌ها در قبال منافع ملی و تمامیت ارضی ایران است. این جریان در طول ماه‌های گذشته دائماً ادعا می‌کردند که ایران هیچ حق و حقوقی برای مدیریت تنگه هرمز ندارد.
🔹
به‌عنوان مثال مدیر تیم رسانه‌ای رضا پهلوی و دبیر خبر سابق شبکه سلطنت‌طلب منوتو، بستن یا کنترل تنگه هرمز توسط ایران را ناقض قوانین بین‌المللی دانسته و آن را نفی کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/455392" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455391">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/108142470c.mp4?token=Mqqg-2Gz8i4j87fIbtpanp6egLibv8ZPkm31QPA1x5hto969bGcP6bU1AnjV9ixvPmKOQx2KE4ALtNWqJQl9CLD1rBwoCiHdvCsTS6T3cghgmC8CxIUoPmpqZ46Pw-aIxxMx_uhvZzCcira6fSmRVE-MuBZHIeVIlMIg97RYtn8LpbgvCCuewkg6kmXJZ5YwAZQJdFMvCQrYDYRJMwDlPrAk6cCr_rxiqkGIU-SvLn0JOYFSv9txUE8xenGWUfCjrAdID-SIddCftulpMJOIfqBkVGroRk1b-tL3t2M18wkiV9GjQ_Su4YPP6Up6YwnpZog7Vor_lpr7Bmg5XevjxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/108142470c.mp4?token=Mqqg-2Gz8i4j87fIbtpanp6egLibv8ZPkm31QPA1x5hto969bGcP6bU1AnjV9ixvPmKOQx2KE4ALtNWqJQl9CLD1rBwoCiHdvCsTS6T3cghgmC8CxIUoPmpqZ46Pw-aIxxMx_uhvZzCcira6fSmRVE-MuBZHIeVIlMIg97RYtn8LpbgvCCuewkg6kmXJZ5YwAZQJdFMvCQrYDYRJMwDlPrAk6cCr_rxiqkGIU-SvLn0JOYFSv9txUE8xenGWUfCjrAdID-SIddCftulpMJOIfqBkVGroRk1b-tL3t2M18wkiV9GjQ_Su4YPP6Up6YwnpZog7Vor_lpr7Bmg5XevjxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رگبار تابستانی با رعدوبرق در آسمان مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/455391" target="_blank">📅 22:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455390">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bd9832e9.mp4?token=KyWQR0vk9xnbPQJS_Bu9vh1-7aqVdVFHH9OZv574MjeAu5pKCwxS1ni2sjadANZLz2lZnYr1yT2_Fu58TicYCKbNg9Wn9JUI75FzrS44v-qzlbXb7twbM2d-Ky6iggxFnQrtCdHlWbWcNRIlCDlnmu_HZhArVk0nqUf-xpD1Pty1UlKZU2C8gXyVl4V3i3uhRtWYI63hU9lPqzl5x8nDm7nf4oQ99KyiHW08J4e3YA_7x-UvLxvWD7p_cGhsojg33VRHERfDsrCO8ZBcjR5sREjex1y4VPBDCgCeYUKMGOsAM0pKSssfEyFPFTtPU2kXZj2ogohh5XOkvqsj343wdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bd9832e9.mp4?token=KyWQR0vk9xnbPQJS_Bu9vh1-7aqVdVFHH9OZv574MjeAu5pKCwxS1ni2sjadANZLz2lZnYr1yT2_Fu58TicYCKbNg9Wn9JUI75FzrS44v-qzlbXb7twbM2d-Ky6iggxFnQrtCdHlWbWcNRIlCDlnmu_HZhArVk0nqUf-xpD1Pty1UlKZU2C8gXyVl4V3i3uhRtWYI63hU9lPqzl5x8nDm7nf4oQ99KyiHW08J4e3YA_7x-UvLxvWD7p_cGhsojg33VRHERfDsrCO8ZBcjR5sREjex1y4VPBDCgCeYUKMGOsAM0pKSssfEyFPFTtPU2kXZj2ogohh5XOkvqsj343wdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی سپاهان از لباس خود در فصل جدید با الهام از نمادهای ایرانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/455390" target="_blank">📅 22:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-455389">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs6I-kTfPHR0AliFsOtJDp-Lke8lAmpixlRCO-tQE91c5s_Q1ge7-YqXzTrXA0hJ71AhZHNB44SuQZx-rHd9GGIRtk99wWO5cSUKDG0Timr5klwqA-oNt2FHMIGve9KMhIe9gJZKZ4PxF4uxsw_gZi3sjW_Lln-Y7HKWgimo8_Q7xpogISODOmLde8LAyYDcVfhA8NOsIyFL0OBhZY99wkiRNGVuHfAvNxXOG1y_6vPIy_QvdBbBUoWGEgjUhkzGom_diJFfvgHzvwXaphqEKTGL_W8nL0_yjeFTxkhEbLR3-kt9BKDW7QcSvQl6ddC2zAIAaqypuVlCytdiOHYxoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظامی سابق آمریکا: روند خروج ما از منطقه آغاز شده
🔹
اسکات ریتر، نظامی بازنشستۀ آمریکایی: ارتش آمریکا بخش قابل‌توجهی از ذخایر موشک‌های دورایستا و مهمات دقیق خود را مصرف کرده و ذخایر تاماهاوک نیز کاهش یافته.
🔹
در نتیجه آمریکا برای حمله به اهداف عمیق در داخل…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/455389" target="_blank">📅 22:17 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
