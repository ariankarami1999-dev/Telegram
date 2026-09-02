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
<img src="https://cdn4.telesco.pe/file/R1HZZNtyKhHoULqsmat5ydJQJDdZTvK5WwR_8l6rx-IOAF1Ba2DaAdFmwp0NXGhMZX_fwIhCPeKKIBNeBGUCu2jkdGdItxRfHZVTaP8lHTN1gz8jBF9M-evlkrbTUBbq5hMc4VEY_cdmGagwpjk8ODfAUptwJArX9pYlSDAW_eKr1p15nYFlVVw6aePmrRqjWTToNCnND9Hn8yCTiFs8TVELx-dES1p99KoJMNfrOA20r83RBiAT0y8DRoITbbk-sUdTOOegtsO_1bhu8y49lp-FVuke4uwdRVfkB2PN48kfMX8X7wJecVmCtlV1HYLv4gRiUwUiYZubc9OX4_I7cQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 113K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 20:13:26</div>
<hr>

<div class="tg-post" id="msg-71013">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5fMGAXuaXGaC4m5gyoouDGIpcDGhaSQW1MBkRIA22pBz-K2lZjJHjP-g3FW3fHzbULrY4v3flI05N-dFxujZz3tjohuFbqQTD5E5slT4rKl9xd7e_kLCp6ErjF9cYf5m4dDd-fLt4KLmLWc_xzjfENcYQgVSXJwyABWpQJgQiuOMKLS-o67ru0lLC8Wro9inpjwb0F0BmGcb2DibqTO4IFNXG9z3Rq-lIpj9GOLfB192hco3aVJA19MVW0EB_Q0LXyM7QxNh2dEBO1utjIXIb6h1qGh6QE58aMxAEhCVnfbNxEuALOSkGoQ25Dc3VVULwEQuE0u32FOSEEEgsbfMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDQc7T_0bOY3oinUIIRDSis4McC7mSMWbxC6G6Dd-dDxSCvLC4UB-l2QwO8KK_2INGVM7Eq8OZNzCV-0y8OFWm5ozL5u7SJD1k6qgO_S1RZ19V7I8TU5KM8HnElgmMNrRoBlY9cvDCfA0RDwDE1_30y3dkJWCML863apjBgiry8i_QW7KSspWL22cszI6k-5X2Bx1eLWwU86jW3rHVLBa57Wc7f9UzUAX9mGwBZTVaGdw_MzdsccxUGKYFK2xXEfTXSQbTn5oDaZ_qMRtyHB-mb0dXNGUeGllz48IwTJA2YwAgyT9kLLPBEgsAIHI3ZEcaDMALtJk0n3e7sRjbhouw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21e8023466.mp4?token=I7TSvjg2gvIfhTrpVVWTtiajbtsA0GkJtTp4ntbfNGd0uuesQlLJ5ytvr_RwGlbICP1ovSIM17gc5n3omLlUg7MwsVXJK0RzDoyhpjGe1GUl-jJkZQvWosL9RxVGz6fYfHwFEM-q-LIETnpK6ZRULjdtGGqGOfazfcKgQI-J4bu4t_K3Ua7HGPI48FUWxJLkbImFhMKSBPch3X2nCacm42JBakh2PvR_5ABU4kCGcZPF6DjsyRS_2xQtwav3ESyRwUSEMmR7QLdMne-CGYCQwGQaOdylzE5-4l4VEkekhnNqeFZvy468g-oNIjHu53wkbrZ-37rfx3yJKmINTJaH5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21e8023466.mp4?token=I7TSvjg2gvIfhTrpVVWTtiajbtsA0GkJtTp4ntbfNGd0uuesQlLJ5ytvr_RwGlbICP1ovSIM17gc5n3omLlUg7MwsVXJK0RzDoyhpjGe1GUl-jJkZQvWosL9RxVGz6fYfHwFEM-q-LIETnpK6ZRULjdtGGqGOfazfcKgQI-J4bu4t_K3Ua7HGPI48FUWxJLkbImFhMKSBPch3X2nCacm42JBakh2PvR_5ABU4kCGcZPF6DjsyRS_2xQtwav3ESyRwUSEMmR7QLdMne-CGYCQwGQaOdylzE5-4l4VEkekhnNqeFZvy468g-oNIjHu53wkbrZ-37rfx3yJKmINTJaH5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
حملات جنگنده های اسرائیلی به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/news_hut/71013" target="_blank">📅 20:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71012">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=fkknasdlyaj71SKNQ6_a0BnxKCh_kOWVp6rN7_E1Ns9gQx1DkDTYSYMKt8AEVaz90RyLStTF4gA3PARcMOQe943rF5x5wKHodWjXLC6Xn-nqQ_kl2eX-_IKkkNy4ZnkLqn4HF2kI_S7YHuOGNGzDKYZbmfAt87-N5NLGuN1G4lzSHGScnW8FYeTa0650PkssO3motT-XsThqTx2Nwaw44tFJ5RuEi3ZabQ9s5cVlSRwnZvyFsCS26WQUjsJbETDgXoQZaQmLTuqMdDmMOcOWUGVgAI4hghj1rxXZ8EuaZyY8uIHuTFMcw5gEoUiFV3EXAqf9M7_AxtT0BYo9nF2zow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600c9063c3.mp4?token=fkknasdlyaj71SKNQ6_a0BnxKCh_kOWVp6rN7_E1Ns9gQx1DkDTYSYMKt8AEVaz90RyLStTF4gA3PARcMOQe943rF5x5wKHodWjXLC6Xn-nqQ_kl2eX-_IKkkNy4ZnkLqn4HF2kI_S7YHuOGNGzDKYZbmfAt87-N5NLGuN1G4lzSHGScnW8FYeTa0650PkssO3motT-XsThqTx2Nwaw44tFJ5RuEi3ZabQ9s5cVlSRwnZvyFsCS26WQUjsJbETDgXoQZaQmLTuqMdDmMOcOWUGVgAI4hghj1rxXZ8EuaZyY8uIHuTFMcw5gEoUiFV3EXAqf9M7_AxtT0BYo9nF2zow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مردی در نیویورک آمریکا پس از برخورد مستقیم صاعقه به پایش جان سالم به در برد
@News_Hut</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/news_hut/71012" target="_blank">📅 19:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71011">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuiNmWMs1c6Q0FTLPyNML_qWy9G5R0IX5JEnzGOumXy76CQPTE9-wIAZdpJ5vT0ZEMHUSX_P97K557qMaBw7_jZFCdJ-dgEvaip7sCpKZmUe_L5d1mmeLLf86Yt3J5CNePd1lYpbUFg_1MO15jhSIgJajIR5_1r8mYeIjdHBRm4o3kQEmNCo1Kd-lpTpsIorDl3s1BzaF9JLpAUMTddICsl-ge03tdxHy6cpvru0jkcxDCO7x3WV6qG5DQ8kS3LkZ3hcSD0V3z2GpLgRe-rrTSxFuLvzLG4_JyqvFdBG6NYa_YITv1w076z-t3X-fbQ7Wfjr0_w_PU1nU8P53rdUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
حالا که تنگه هرمز تحت کنترل ایالات متحده است، آیا باید نام آن را به «تنگه ترامپ» تغییر دهیم؟ این تنگه هم درست مثل خودِ آمریکا، «داغ‌تر» از هر زمان دیگری خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/news_hut/71011" target="_blank">📅 18:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71010">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/news_hut/71010" target="_blank">📅 18:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71009">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=RZjMEJCz2JojqW7T1D-7pYiH4getjHxvAv2itND65usCVV1mujvGjI1flVbs3CX7aLm6KdAYzSc4ayjH7yM28Y2uKgyYmHUvLc6aFC3ehJccxKGPnkhAjcFFxxNJm5N8zFQiJKG1L9ecHtkdm2uLgaYPcLk3m6MBq8pGs1ewAd9yiKonvk_EgxwqZPAAySYf3lqHH1zhs_nQbGo33PfFoG49Iv-zC4M5emG6GLW2kGKOkPhxcJsQH1XhlzItbjtxh_3syCUMqZlPaelMaujQkCCkEZZzbC17T9L_62tAiCcXDrErGB9U9LKUoQgaIUokVEZAshvaziZ1md3MW1MDwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f635b0ff.mp4?token=RZjMEJCz2JojqW7T1D-7pYiH4getjHxvAv2itND65usCVV1mujvGjI1flVbs3CX7aLm6KdAYzSc4ayjH7yM28Y2uKgyYmHUvLc6aFC3ehJccxKGPnkhAjcFFxxNJm5N8zFQiJKG1L9ecHtkdm2uLgaYPcLk3m6MBq8pGs1ewAd9yiKonvk_EgxwqZPAAySYf3lqHH1zhs_nQbGo33PfFoG49Iv-zC4M5emG6GLW2kGKOkPhxcJsQH1XhlzItbjtxh_3syCUMqZlPaelMaujQkCCkEZZzbC17T9L_62tAiCcXDrErGB9U9LKUoQgaIUokVEZAshvaziZ1md3MW1MDwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما اکنون کنترل تنگه هرمز را در دست داریم. ما آن را کنترل می‌کنیم.
دیشب ۲۸ قایق و کشتی را از کار انداختیم. ما کنترل آن را در اختیار داریم، آن‌ها هیچ‌چیز به دست نمی‌آورند و ما آن کشتی‌ها را نابود کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/news_hut/71009" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71008">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=TVJRojnAj5wO_5XnECAvqk9wzOwdtLNn8qy1ZCFnTHy7Kg3Mw6hMBl27CdIlta4C7BDgIV6L_ELFqNSrTNIgvXBr3J1RneaSxmtJbfovJ5bVwok_wrH0uwX3WRdT2WoDs4jf8-zWIpsWGEul7qKCma1Ey2-eYBRpC78TTbZoMH601dAur66KXwi1MsbJCq5RMPCBwcgCQEaSmWMeZnSmvyIw3Vk-LKPzhiMkPJKoSYsWJfddKGfuHs9tI0i740qtS-wbWriizobBR3klkDS95SzPzFn4GbNOHNQAznLmNPP0Hu4qWjFeFbBD9lw0RQbYMk39jl9hb8oYrtZaX63HPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/116dfeb2e5.mp4?token=TVJRojnAj5wO_5XnECAvqk9wzOwdtLNn8qy1ZCFnTHy7Kg3Mw6hMBl27CdIlta4C7BDgIV6L_ELFqNSrTNIgvXBr3J1RneaSxmtJbfovJ5bVwok_wrH0uwX3WRdT2WoDs4jf8-zWIpsWGEul7qKCma1Ey2-eYBRpC78TTbZoMH601dAur66KXwi1MsbJCq5RMPCBwcgCQEaSmWMeZnSmvyIw3Vk-LKPzhiMkPJKoSYsWJfddKGfuHs9tI0i740qtS-wbWriizobBR3klkDS95SzPzFn4GbNOHNQAznLmNPP0Hu4qWjFeFbBD9lw0RQbYMk39jl9hb8oYrtZaX63HPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇧🇭
لحظه اصابت پهپاد شاهد-۱۳۶  به مقر ناوگان پنجم نیروی دریایی آمریکا در منامه، بحرین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/news_hut/71008" target="_blank">📅 18:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71007">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8kp4bjeUF0zsV5Ia0vIVCs1I6WO-NIpzUx_nEqvbxN0Ff3j4TWI8u9OxT4NQEJka6qkX0LNG7V-uVwaOyhn2jF2mykFom1iKVlWUZXANl9VDNyIZ31BkV3TDNRXlECEmIsfar0JesdxfXtuBzBTfBEWU5ed8FLCE6LJy9avAyqGuuVK92Zl4Yit84WwSBffuzVQgPKRdsmkEMiiQAqGamsYZXN02ztDWA6E-Srtdtnp6WU5U3lTAOPF6FAuz5GbuuqUxh-XJUMohwzk3aSCzZwQHo5KoAiUoHTQ66J9padQwnD4l4tu-gzxLb7uqJSC6sNM7gaj_I-VbG2xTM0zXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه:
ایالات متحده به هدف قرار دادن ایران به دلیل حملات به کشتی‌ها ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/news_hut/71007" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71006">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71006" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/news_hut/71006" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71005">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WicxAaqXNTY-EkEgclpjCwOaC3G7B1WW3M8yTfXh0Ttphh5cLdzyw8yrwlmkhMWnkNXvm2fuigamrGupXx69A6S87Dm1stqIZv4BhXba9sCHDoyZXyX36gJuEKfARjybrPszpGMJM7g8lc_7a0b23bXTGRMnz-z-neN7WSztKKdJ7nKSBtjK0NnwAUnuMnJkOr48SW34M7FvdxHxyUNQFjEH8aV18XColnWIxDcLXQ_WxwqKb1d8kFRBCmzHQlM7kTZnzbeD-ZllVD243d_khMVAIRdvLMRCAgl43KFOENw3clhTTZMddzy-bUBlE67_kIsw4pD9v-Sqad_5QFzoGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/news_hut/71005" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71004">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26734edca1.mp4?token=n7Zk_R74YU9iEMFUFjgchrM6XXZ5B8egIWx_jTccD1k_pwxZf0-4ogSLKEKnaLMJTj6ncz5lH7vkYa2Kq99t4TtNv7cu27k43c-u_r4XGZOAHiNjNz5QNxOuXRhBgjGW9fI5GIpYjVM32Q_QX2vbkkTeVW2xlk2LliR_DYU5N-P75KH9y_NoJE-xHtI3C2XWtFOjelEK-L-p_19-DwVwBA4Jpo8bVzJSyDN5ia0_FSqzQdRtcz6yYPJEenAZedwT5IirYXtwyN_jcaAgAFoIt6npkm5QAcQdwPprIypjhwSur8Vy2Svr5kSFr30jz98YHBg_ehT1N3z_2KM3ucmRzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26734edca1.mp4?token=n7Zk_R74YU9iEMFUFjgchrM6XXZ5B8egIWx_jTccD1k_pwxZf0-4ogSLKEKnaLMJTj6ncz5lH7vkYa2Kq99t4TtNv7cu27k43c-u_r4XGZOAHiNjNz5QNxOuXRhBgjGW9fI5GIpYjVM32Q_QX2vbkkTeVW2xlk2LliR_DYU5N-P75KH9y_NoJE-xHtI3C2XWtFOjelEK-L-p_19-DwVwBA4Jpo8bVzJSyDN5ia0_FSqzQdRtcz6yYPJEenAZedwT5IirYXtwyN_jcaAgAFoIt6npkm5QAcQdwPprIypjhwSur8Vy2Svr5kSFr30jz98YHBg_ehT1N3z_2KM3ucmRzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
اینترنشنال:
⁉️
🇺🇸
🇮🇱
از شهروندان پرسیدیم پاسخ شما به پرسش ترامپ درباره زمان قیام مردم ایران چیست؟
یک شهروند با ارسال پیام صوتی به ایران‌اینترنشنال خطاب به دونالد ترامپ می‌گوید: «چه تضمینی وجود دارد که ما بیرون بیاییم و تو بعدش مذاکره نکنی؟ ترامپ، کار را به نتانیاهو بسپار که او بلد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/71004" target="_blank">📅 18:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71003">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=M1YFtlvegtipylG83i9QHpshHCDvdkPcsyYggJeguTCRV0xut4tpO6cNpY-B_75a3zmqSmT2MmnBT2GtyVKn7aqsAJED9l8gnP1FuaZu2ESUnAtNL3JLFWDQDek_J493uKepmfZwrJX4ncXy_D3QflJNC0QTY5bJxxirvbpN0xQQcEYyLTz1rEWz2xDPRDEAKgHHcsYJjHARUAJbjLGIIAdI7JYBaJfMxj5IS2NU9zSYgqwQbIYuhrju_XtWeQ4SWt8CaL5L5aWNR8fLB1dVQ4fh_sUIHUr9aVoGW33pHAqLWnKFwMKDEGuPfAXqOM95tZ3NTbGpeI79nIrk_Og4rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4349c8ad3.mp4?token=M1YFtlvegtipylG83i9QHpshHCDvdkPcsyYggJeguTCRV0xut4tpO6cNpY-B_75a3zmqSmT2MmnBT2GtyVKn7aqsAJED9l8gnP1FuaZu2ESUnAtNL3JLFWDQDek_J493uKepmfZwrJX4ncXy_D3QflJNC0QTY5bJxxirvbpN0xQQcEYyLTz1rEWz2xDPRDEAKgHHcsYJjHARUAJbjLGIIAdI7JYBaJfMxj5IS2NU9zSYgqwQbIYuhrju_XtWeQ4SWt8CaL5L5aWNR8fLB1dVQ4fh_sUIHUr9aVoGW33pHAqLWnKFwMKDEGuPfAXqOM95tZ3NTbGpeI79nIrk_Og4rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
فردوسی پور:تاج و دوستاش نزدیک ۲۰ میلیارد از پول بیت المال رو گذاشتن تو جیبشون.
چند وقت پیش تیم ملی جوانان ایران واسه برگزاری یه اردو قبل بازی‌های آسیایی، به ترکیه سفر می‌کنه.
تو آنکارا، هزینه هتل‌شون طبق سند خودِ فدراسیون، 116,160 یورو شده.
بعد برنامه ۳۶۰ زنگ زده به همون هتل گفتن که قیمت‌ها اصلا این نیست و انگار مسئولین فدراسیون قیمت‌ها رو الکی بالا بردن! و هزینه ای که کردن چیزی حدود ۳۶ هزار یورو بوده.
خلاصه تاج شیرین نزدیک ۷۰ هزار یورو کرده تو جیب خودش و دوستاش
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/71003" target="_blank">📅 17:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71002">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=lzx7Lp8i5ofRG25bgBSTtJiF0Eo5RQKpw4sqFvUd-7PY7TqTEfVoWWw5KnI-JXhJ7BlzYKxSm74sxtQJygNLBrnlMBydwXd0vV8J9W-YlJBaCYd2jy2-whMOnHCXVaH9XuI4Zbty-fsIaF3xZoiwa55kyjj1fhzX6ufg7YtR6h60DzJJ-rsiVsg_aPwq5y4FMR0isSt3Zodzof1k-6Ush8ZiPGXXyQRejCR4HHj5DZfTcKFtDX8UNzPdkIU3WRYUA4gXyNSxsioy2WtuiP1uVHm0lYuHfRCZPztIkz1XzXtg4J65uHlisIeXqcaTESbjqrWDUT_i51a4UyKUMlxH7D9K9EYiYzze8Za2bFGp3vXqwWp5Pqn3hrScLSdKeyj_1s4CfSra3eujGy3FfIAN5iLxy3Pc1Tl5Ul0-pVLgV4-4TomdhRK7mmI-1UTw_SCEDUkyqj_ROrw5eASaZ4y3xQ7_wlrQvaQEgSkzmQqWE3do2QbB9pUI7_6v3C5f0fhzHIVl7g0pNF83O5Hv5-K0w_ENKa00uFdDFDKMBXcFScrHv10qdK6dQ7UjcfuPCe5fh7_SXDxl5Uzvh71gPTzt3ucmppWq71dAJCAHuI_l33WhRFU_tAiiq4zGB7quPbbw0rszUxKhBZ_UQ87oMQeTqakafpY7mlI6DLPXgbxIGUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1896637f6.mp4?token=lzx7Lp8i5ofRG25bgBSTtJiF0Eo5RQKpw4sqFvUd-7PY7TqTEfVoWWw5KnI-JXhJ7BlzYKxSm74sxtQJygNLBrnlMBydwXd0vV8J9W-YlJBaCYd2jy2-whMOnHCXVaH9XuI4Zbty-fsIaF3xZoiwa55kyjj1fhzX6ufg7YtR6h60DzJJ-rsiVsg_aPwq5y4FMR0isSt3Zodzof1k-6Ush8ZiPGXXyQRejCR4HHj5DZfTcKFtDX8UNzPdkIU3WRYUA4gXyNSxsioy2WtuiP1uVHm0lYuHfRCZPztIkz1XzXtg4J65uHlisIeXqcaTESbjqrWDUT_i51a4UyKUMlxH7D9K9EYiYzze8Za2bFGp3vXqwWp5Pqn3hrScLSdKeyj_1s4CfSra3eujGy3FfIAN5iLxy3Pc1Tl5Ul0-pVLgV4-4TomdhRK7mmI-1UTw_SCEDUkyqj_ROrw5eASaZ4y3xQ7_wlrQvaQEgSkzmQqWE3do2QbB9pUI7_6v3C5f0fhzHIVl7g0pNF83O5Hv5-K0w_ENKa00uFdDFDKMBXcFScrHv10qdK6dQ7UjcfuPCe5fh7_SXDxl5Uzvh71gPTzt3ucmppWq71dAJCAHuI_l33WhRFU_tAiiq4zGB7quPbbw0rszUxKhBZ_UQ87oMQeTqakafpY7mlI6DLPXgbxIGUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طراح ارشد موتور (بمب‌افکنB1-Lancer) متولد سیرجانه!
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/71002" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71001">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618f407212.mp4?token=ge13axpbD29N7ShSSnfOEEcuyWkucHEAOmAlDanza3u00YSoXZs-lzvEM5UIFzZjxBTx1iYV2AXeEDub6MMhlye1P5jkWzJocSOjw3xCHCt0mBcXJjGUKbeockSXAedxymJo1gm-P2721KbojmFmLeg63JYogoNDBOXZOV6KcmYGZ5K6puNUhIwNqTLSnclljB6oh4gJWGciQJjmUQKPQ3JgGGucApVablFEOXowI14Zms2AfewMCWab_GtZ25uVRKaXXCZoBPwUSsb7rWzab5Z6VlVrieLEKEYSuMpb1QIfrIV9lW9O2fvtx6-qJ4Hzv1OXJBlnd3W0f150AOu-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618f407212.mp4?token=ge13axpbD29N7ShSSnfOEEcuyWkucHEAOmAlDanza3u00YSoXZs-lzvEM5UIFzZjxBTx1iYV2AXeEDub6MMhlye1P5jkWzJocSOjw3xCHCt0mBcXJjGUKbeockSXAedxymJo1gm-P2721KbojmFmLeg63JYogoNDBOXZOV6KcmYGZ5K6puNUhIwNqTLSnclljB6oh4gJWGciQJjmUQKPQ3JgGGucApVablFEOXowI14Zms2AfewMCWab_GtZ25uVRKaXXCZoBPwUSsb7rWzab5Z6VlVrieLEKEYSuMpb1QIfrIV9lW9O2fvtx6-qJ4Hzv1OXJBlnd3W0f150AOu-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بررسی قیمت چند داروی پرمصرف از شهریور ۱۴۰۴ تا شهریور ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71001" target="_blank">📅 16:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71000">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=uv1DB6xBbVwIakwLVdQ4nZ9ssEmESqhfa6lpklH3OSgZzFB1YxmpZZJE8p0VtnpHMvG5jHEiW4EID2frrQt6DrEw3t9jSQiGpwv_Gy1st6pbC_GsvlhRphvJcarV1r_F0iDaknL-hs57-uA-LX44t6gA2EZI5kq5Le-IQuWqQGU8DELGmXWdOs_2aQ85MnBr45LQQNU1OfxqqRT0Togmrz9AT94-_D7jvRZa7i7yOKqsjhlHFDVF_SbFX7g31fUjf4sfEDEskvQA9En5pTAQaYibJkk-Kwj5SAFPFflxjfnAtlF2huGYY6oK1SoXcS5Op6vfSSdu1m99L1ETflndjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df28769cb3.mp4?token=uv1DB6xBbVwIakwLVdQ4nZ9ssEmESqhfa6lpklH3OSgZzFB1YxmpZZJE8p0VtnpHMvG5jHEiW4EID2frrQt6DrEw3t9jSQiGpwv_Gy1st6pbC_GsvlhRphvJcarV1r_F0iDaknL-hs57-uA-LX44t6gA2EZI5kq5Le-IQuWqQGU8DELGmXWdOs_2aQ85MnBr45LQQNU1OfxqqRT0Togmrz9AT94-_D7jvRZa7i7yOKqsjhlHFDVF_SbFX7g31fUjf4sfEDEskvQA9En5pTAQaYibJkk-Kwj5SAFPFflxjfnAtlF2huGYY6oK1SoXcS5Op6vfSSdu1m99L1ETflndjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرت زدن وزیر ورزش و معاون وزیر خارجه و تمیز کردن دندان توسط وزیر خارجه هنگام سخنرانی پزشکیان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71000" target="_blank">📅 15:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70999">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcFUN7YKD6yVwVtOMJ22MF5fYbGtcQXXKYbD5qhAAAfV0FXJ0GCFRBnpafGYvpDOag1VKIVR0-YqX19t1RsHgtxHaI7R3dU4xDRutuLqLwKIQi4JzdekPc1q67N1xSPstZDnVcytOOkEI2F_QqPm7JlkSWWNxJ2q5M6SD5ckdiRrMd55lBzwnkE21qJ5F0f0WzAuaGx7K6isVSRLVhXnnCW98H-_Rr5NKqJo8kddoxsMF1xJvxAp4Jag5ON7u-uZutpyrpU_ANdqAyDwCo5ynxUjdJRzwejOEYV2DVDmWFpjtmWe5b5chaKZ7KOENpOKV2IW2qo0e_9O7o3VshNT0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارش تأییدشده‌ای مبنی بر درگیری یک نفتکش در یک حادثه امنیتی دریافت کرده که منجر به دو مورد تلفات انسانی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/70999" target="_blank">📅 15:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70998">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bqt2X-v4QV3z3uq0j2VIC0EwVKd0cG3UvghSvnaJ3XItPuOAi5idLImmcpTxLBfcz9VQ98QJssGPTBYBV6JxJA3Dpmf682j_R57e7_SQWT6_16gcMgsNPcPadx2todzYzKMpt7fguY7wMNKCgY5xPC82PPBexRVTU9oxnDKQItIMPCPe7xBaOD0AzmEulXI54hbtVOn9qnRc9DBAd383I18Hj5dsucKohYID6NVHJTD5FgZUV4SGnxMlFkS-rEpLBAT-siFE40tOiwkYIN6S8bSsgr60dtx-o0ZHeWts01JGYNqfzeO6C9iuQv_H_dzrMjchivbrdMywAs0biZ8m1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
فیلد مارشال محسن رضایی:
با این دست‌وپازدن‌ها، نه تنها در بیرون آمدن از آن ورطه هولناکی که برای خود رقم زده‌اید ناکام خواهید ماند، بلکه به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، بنیان‌های شما را درهم خواهد کوبید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/70998" target="_blank">📅 14:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70997">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13235e9918.mp4?token=vDSs8U-iF_5uPHE8GUOGLm-raejao0Ny_AM4-7VNKiPnVX7PJijsPHpExi9GwPrOQ9IRQc4xWVp8XK6Dyu0J-pXIkbzk5M76eZRJLljH-9yrS39GBNU9p5fkv0a3f4GIKwsPI02nbDECp7YBp8aEZODWc0zj7hRpHbWMhXx14c4IWCeu6Z6Ze8_PBVs5Odt-6DvoOnLq__gVe8hzhmwBn5J88ZpI6z7R5JiAmXlCjct1F3Vi_9eEkBDWGi920D0nbRWwHOx8vVg-wDQiCKKEQg-cUHouwxj3KNFxG6g9V9DYH2Adb7a9QSxaqucin-F9TcOqsv1Tqz0t6tnseDRKPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13235e9918.mp4?token=vDSs8U-iF_5uPHE8GUOGLm-raejao0Ny_AM4-7VNKiPnVX7PJijsPHpExi9GwPrOQ9IRQc4xWVp8XK6Dyu0J-pXIkbzk5M76eZRJLljH-9yrS39GBNU9p5fkv0a3f4GIKwsPI02nbDECp7YBp8aEZODWc0zj7hRpHbWMhXx14c4IWCeu6Z6Ze8_PBVs5Odt-6DvoOnLq__gVe8hzhmwBn5J88ZpI6z7R5JiAmXlCjct1F3Vi_9eEkBDWGi920D0nbRWwHOx8vVg-wDQiCKKEQg-cUHouwxj3KNFxG6g9V9DYH2Adb7a9QSxaqucin-F9TcOqsv1Tqz0t6tnseDRKPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
پوتین خطاب به پزشکیان:
تو این شرایط سخت، داریم سعی می‌کنیم هر کمکی که لازم دارید، بهتون برسونیم
.
قبلاً هم دربارش با هم صحبت کردیم و داریم کالاها و اقلام موردنیازتون رو تأمین می‌کنیم.
با وجود شرایط نظامی و سیاسی فعلی، همکاری‌های تجاری و اقتصادی‌مون رو با همون روند و قدرت سال گذشته ادامه می‌دیم.
همون‌طور که بارها گفتم، ما تو روسیه کنار مردم ایران هستیم و باهاشون اعلام همبستگی می‌کنیم. شجاعت و مقاومت شما واسه دفاع از منافع ملی‌تون واقعاً قابل تحسینه.
لطفاً سلام من و حمایت صمیمانه‌ام رو هم به رهبر جمهوری اسلامی، مجتبی خامنه‌ای برسونید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70997" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70996">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">1
💵
= 200.000
💸
🔼
یک دلار آمریکا=دویست هزارتومان   @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70996" target="_blank">📅 14:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70994">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=T9BVyJeWBrWUCKUVOreqsVgCG2mxNYTDgXHC0YkmOWs4oCyKeqEy_qRAkKaXYAp7W2l3W3gzmx9aILK5h56vzbYuFSW5pTSzMhsyiZ4KrFoHWFXxqHKzqUs9Xq7UZFRT9SFa-QsU3AjGBWABChXlxtb2lQpn0oaZxzFUvVCCN3P_gqqGYoGPXlXPVCgML0kNBVSqOtlzu0ueA5g_-C-RpkCWYcPGgyTNNB0Eeqs3HFRWaidDI8QdULP_4YtQDgCPAbZiMDwiDxmEIYZzHk41MWAVNfjLJMF6KheT8uh7DuWNSCz6sLXFQUO-jgdkmbfgihrYnuFaShyZtn8y5TFmNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a6a11bf6.mp4?token=T9BVyJeWBrWUCKUVOreqsVgCG2mxNYTDgXHC0YkmOWs4oCyKeqEy_qRAkKaXYAp7W2l3W3gzmx9aILK5h56vzbYuFSW5pTSzMhsyiZ4KrFoHWFXxqHKzqUs9Xq7UZFRT9SFa-QsU3AjGBWABChXlxtb2lQpn0oaZxzFUvVCCN3P_gqqGYoGPXlXPVCgML0kNBVSqOtlzu0ueA5g_-C-RpkCWYcPGgyTNNB0Eeqs3HFRWaidDI8QdULP_4YtQDgCPAbZiMDwiDxmEIYZzHk41MWAVNfjLJMF6KheT8uh7DuWNSCz6sLXFQUO-jgdkmbfgihrYnuFaShyZtn8y5TFmNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
ناو «یو‌اس‌اس آبراهام لینکلن» در تاریخ ۲ سپتامبر و پس از ۲۸۶ روز حضور بی‌وقفه در دریا — که رکوردی مدرن برای نیروی دریایی ایالات متحده محسوب می‌شود — وارد بندر «لائم چابانگ» تایلند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70994" target="_blank">📅 13:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70993">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل درباره ایران:
هم‌زمان با افزایش فشارها بر آن‌ها، تشدید تنش‌ها و تنگ‌تر شدن حلقه محاصره — آن فشار اقتصادی خفقان‌آوری که رژیم افراطی بر مردم خود تحمیل کرده است — احتمال دارد که آن‌ها واقعاً دست به حمله بزنند.
چرا؟ زیرا ممکن است برای رهایی از دوراهیِ میان «خفقان» و «جنگ»، گزینه دوم را انتخاب کنند. ما از نظر دفاعی برای چنین وضعیتی آمادگی داریم.
اکنون در ایام تعطیلات هستیم و آن‌ها معمولاً در تعطیلات یهودیان دست به حمله می‌زنند؛ هرچه باشد، آن‌ها از یهودیان بیزارند.
اما ما — هم در حوزه دفاعی و هم تهاجمی — و با هماهنگی ایالات متحده در این جبهه آماده‌ایم. بله، در همین جبهه.
با این وجود، سناریوهایی وجود دارد — مانند حمله به اسرائیل — که ما به هیچ وجه آن‌ را تحمل نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70993" target="_blank">📅 13:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70992">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=oN684zzEGkagynSgoHvl-PSFbhx4z69RHxUxQsjT4m-KlkxEvYxW4wa396fSqe_Kx_WfNrvJiYNwHC9knko3tcQYPWOiPSZI9UiM1RzttsC2Oq-uG3ZhcxJwpbyVFQcqWgfdiFIynoxGpOT21Aw7EB4f-ju6-mM02TljaP75kpFHjOoFHFD5kJCg_N1RxyHavXeEpc03sUZPBy6EnkgBGMQpmp67VnNehHhejRJbS8jTM6MjW_owLQN_W7WxHJ031B2q5Bq6GSIGW7vfqtuyR7xDaPSiYaon1omGdIhLLt9WIaRzX1AHVOSAlnvXse49_i7VeN1okAls7lzE_w-mqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd8120289.mp4?token=oN684zzEGkagynSgoHvl-PSFbhx4z69RHxUxQsjT4m-KlkxEvYxW4wa396fSqe_Kx_WfNrvJiYNwHC9knko3tcQYPWOiPSZI9UiM1RzttsC2Oq-uG3ZhcxJwpbyVFQcqWgfdiFIynoxGpOT21Aw7EB4f-ju6-mM02TljaP75kpFHjOoFHFD5kJCg_N1RxyHavXeEpc03sUZPBy6EnkgBGMQpmp67VnNehHhejRJbS8jTM6MjW_owLQN_W7WxHJ031B2q5Bq6GSIGW7vfqtuyR7xDaPSiYaon1omGdIhLLt9WIaRzX1AHVOSAlnvXse49_i7VeN1okAls7lzE_w-mqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو از فروش طلا، به دلایل کاملا نامعلومی بیش از 5 میلیون بازدید داشته!
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70992" target="_blank">📅 13:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70991">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70991" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70991" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70990">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0_TbRrE_WbbIRsAd5cDYdt1HZh6FBd3QBJsYkZasQFuDyF05g0ZL_YnABVoeTHn9QXnAt9G-Nm4uVIB5Dectfd2q6ACviCAOCuXEALeL7X7fOFhGf-A0qE6GQJx3GqA2wY7t-McPqPKklXn2VgRBcjpTStuQqg1VYy2fZEnKZ-_EAvWl91vz16QX-XcGYDt5ub1G3izSWWOdIBA5Ye9xuA8Z8HCLXVXw5rqxN5uHTKawdaOgaB-7WwknuPU5CV6j57k-2fTRVbnVsR_toEMXMlxGbvLVshGo3CXspnQz_Kc4QpRiaWqd8ckJ1-BIlxO4ChSn6zGAJJWb-PGGZOmPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70990" target="_blank">📅 13:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70989">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1829295007.mp4?token=iLpRTRdb7jw8FTRWjJgJgVTcpsIqTqOeQfcO2f4zGyNVCdGamSdUuhjR5FsqAkGoefs3CNySVq-65LVNjgcX3__Kfmg4wn-b5XxV1AOlv5Qby9fuCSCpH9dPjcSnuxVN6AZEs-148xZF1TRV75c0fZlXsTg1jFT4-Q4_ThHAxws2khTmD9CZ_WrYcQ3rg1vyvOiog_9408qPVVZlh2EIxqv6Ac1x9MQM90Xib0toJQ_fREyBSTT0GZNQrZ7cQKxyaNocNW0UNJIFQ-J4xe6m03FjxNUKi7hHxdkUw_S7B5evYVoCa5BpeIyvCwSB0SrJkXHtHvzBOO5bqfgv3XFt_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1829295007.mp4?token=iLpRTRdb7jw8FTRWjJgJgVTcpsIqTqOeQfcO2f4zGyNVCdGamSdUuhjR5FsqAkGoefs3CNySVq-65LVNjgcX3__Kfmg4wn-b5XxV1AOlv5Qby9fuCSCpH9dPjcSnuxVN6AZEs-148xZF1TRV75c0fZlXsTg1jFT4-Q4_ThHAxws2khTmD9CZ_WrYcQ3rg1vyvOiog_9408qPVVZlh2EIxqv6Ac1x9MQM90Xib0toJQ_fREyBSTT0GZNQrZ7cQKxyaNocNW0UNJIFQ-J4xe6m03FjxNUKi7hHxdkUw_S7B5evYVoCa5BpeIyvCwSB0SrJkXHtHvzBOO5bqfgv3XFt_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇨🇳
⭕️
حسین مرعشی دبیرکل حزب کارگزاران:
🍆
چین سفر قالیباف به چین (و گسترش روابط تهران-پکن) را مشروط به موارد زیر کرده است:
۱- باز کردن تنگه توسط ایران
۲- دریافت نکردن هیچ‌گونه عوارضی
۳- پایان دادن به اختلافات خود با عربستان
۴- پایان دادن به اختلافات خود با آمریکا!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70989" target="_blank">📅 12:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70988">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعاتی پیش دو فروند کشتی نفتکش که با تحریک ارتش آمریکا خدمۀ خود را پیاده کرده و برای گذر از مسیر غیرقانونی در اختیار عوامل آمریکا قرار گرفته بودند، با رفتن روی مین منفجر و متوقف شدند و در آتش می سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70988" target="_blank">📅 11:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70987">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJtky5z1WrJU09CkmnFZBrwM3AmN17EIkDdRr0wDPODMh3hhHmFyHAWGKtQBdUd86GS_4iLuSwzQzcrTbyRB5RkJ8bJlIetc5N0j5dtthrl_p61hQUVVIB5xUg1CUHdDIbpkXFF-qJc9vIBLmpGcrC5VzZJgmNJL-ot29rR2lDQLGtNwNEWOBvyCko4I2mIoGf23rj4lCJ46fIe9HiM7lbyk-bCArLQjHBv8TuoIl9_fLY0L_hhRqTctKKpTKjHx5_XT9HrV_Jpe7BGxpQPOe4ZOfLo4umd_1vaiW3f0NWs8eiSbzovNNQ35m_Uea_wSSYWQQ6HQHoOuv5GHhlqtFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
من برخلاف گزارش «ای‌بی‌سی نیوز» (که اخبار جعلی منتشر می‌کند)، سعی ندارم ایران را به پای میز مذاکره بکشانم. برایم کوچک‌ترین اهمیتی ندارد که آن‌ها توافقی را امضا کنند که از نظر خودشان بی‌ارزش است.
وضعیت فعلی ما را بسیار بیشتر می‌پسندم؛ چرا که تقریباً کنترل کامل تنگه هرمز را در دست داریم و اقتصاد آن‌ها نیز در حال فروپاشی کامل است. آن‌ها صرفاً دارند زمان را سپری می‌کنند تا با سرنوشت اجتناب‌ناپذیر خود روبرو شوند.
مردم ایران چه زمانی قرار است قیام کنند و بجنگند؟
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70987" target="_blank">📅 11:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70986">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=nLC-kWYNcJCoVUt4AmqBz2poCJ9l9mwNYwXTJkE04VyqshK2gigQIzbtmh8OkPr6rNlXElxl-GzrAPQAllkNi1zhotH2R4mho1jAPyQOcR-XIGmN4Eacmp55gVqe1Z5YaxZLie8X2FopXttGHp3lNtc2eHErbqvjNCj3Pg_BtDepIlR08O9TQOct_WiVuJYG_jvdh35xYntTrY3Tx3W-4HGerXEtqao_5fTL7eCBjweD30skv9T7QZSGkjPKKqCqTDLMZngFKk-aAVwbenACAlbzv8S4LX-BFttjNygZZSdgqoz2qnGfmmPa0tnFsgEJKAToWc04SlqUHuuXEoqfaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc462e7e.mp4?token=nLC-kWYNcJCoVUt4AmqBz2poCJ9l9mwNYwXTJkE04VyqshK2gigQIzbtmh8OkPr6rNlXElxl-GzrAPQAllkNi1zhotH2R4mho1jAPyQOcR-XIGmN4Eacmp55gVqe1Z5YaxZLie8X2FopXttGHp3lNtc2eHErbqvjNCj3Pg_BtDepIlR08O9TQOct_WiVuJYG_jvdh35xYntTrY3Tx3W-4HGerXEtqao_5fTL7eCBjweD30skv9T7QZSGkjPKKqCqTDLMZngFKk-aAVwbenACAlbzv8S4LX-BFttjNygZZSdgqoz2qnGfmmPa0tnFsgEJKAToWc04SlqUHuuXEoqfaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عطریانفر، عضو شورای اطلاع‌رسانی دولت:
پزشکیان اول توسط شورای نگهبان برای شرکت تو انتخابات ریاست‌جمهوری رد صلاحیت شد ولی شخص علی خامنه‌ای صلاحیتش رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70986" target="_blank">📅 11:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70984">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EodhnD-DGysUWNu2JKgxJWhQxt7Sf62drKC01s0yYQa-enQexTcKwDWR6siEd7g7qVaoFnyHa6UrdpQaIWM2fFqb8aJG08Nz1V4FjMF9qS875vDPe3Y-woHiIphLzFaO3wkpyX0qQDoRTj5W7LpoflNdprl8zJIsmfzE0Jv6jpNhKEQU08DhFR-gBUN8MCwSC7X8LEON9Ejih8qCVPBcBk6lx25GJnE-AD-e3UTDkMICTN8IZ-R5NwCEmMmmjELtFdQmAXHHlJkmumYHGiMD8Goc0w4FxzEEFAMQkWOPXS6JsdoVBXXuQSJCjMfQN593YZEhdomy_LWwSzkCy98jWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=IeoIt4sxbMmqXogEAGHh29oO2ZN03ElfCtGPPaFSChrmfq5lDY3aA2LSIzUVEz7_VfZ64s656zXJVTh2LKsdRHnbvGufBZpa1yHAVYoylAlu4YIRHf8xmtNOc7q2kTjiwLY1eRJ4tNwwnl7pMkdDoN2bClCFgOIafh26zDc2Zdtr8qwXfji1ny4Z-v_dAaae1fewesW8090lxjo0UzxnmldYHVGRb9usO_Um9Ord-wzcizi5ZpjZ5sc7-WIKKHj6exz7EiU26PgTAz3_0ACf-hCxpSi2QpNpRM-d0BPC07tQSc2yNZl0244NeohX_CLmr9Czz9YK6mOkesKd-ZjdgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f0caae86.mp4?token=IeoIt4sxbMmqXogEAGHh29oO2ZN03ElfCtGPPaFSChrmfq5lDY3aA2LSIzUVEz7_VfZ64s656zXJVTh2LKsdRHnbvGufBZpa1yHAVYoylAlu4YIRHf8xmtNOc7q2kTjiwLY1eRJ4tNwwnl7pMkdDoN2bClCFgOIafh26zDc2Zdtr8qwXfji1ny4Z-v_dAaae1fewesW8090lxjo0UzxnmldYHVGRb9usO_Um9Ord-wzcizi5ZpjZ5sc7-WIKKHj6exz7EiU26PgTAz3_0ACf-hCxpSi2QpNpRM-d0BPC07tQSc2yNZl0244NeohX_CLmr9Czz9YK6mOkesKd-ZjdgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
🇮🇷
پوتین در دیدار با پزشکیان:
خواهش میکنم سلام گرم من رو به آیت الله سید مجتبی خامنه ای برسونید
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70984" target="_blank">📅 10:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70983">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=axQuvNryNzx10VlwQnDpLxOPkV4AiMPtEQPSEZgBib_QTZ_5MObaqTaN9cO7Slz9sZwfurdlGaMvccmBZuG8QT6vd8YwE2BdKDXoQ3P0IAPNVaorHbsuai1WrGXxcOQpyU_cBjWefp124LlJaKyo2T61RI6ZDD9BBT1Ccs3aFRRExHYblPZpEBBi-D1-oPQCU_hBhXJ0mI3wQ6gIVmuZsFEPRw612MqMfnB2FgqtZLncNuyncyAjB-ZWLlc2g5GDb9PAX64LaBoZ0CW4kcFcqL5lMVvLyD2L16OMzud6X8YCPTwPNmj9-4bFWyHh-WaHHMcvrSZW2-WXNoQeU7tfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48458cadfa.mp4?token=axQuvNryNzx10VlwQnDpLxOPkV4AiMPtEQPSEZgBib_QTZ_5MObaqTaN9cO7Slz9sZwfurdlGaMvccmBZuG8QT6vd8YwE2BdKDXoQ3P0IAPNVaorHbsuai1WrGXxcOQpyU_cBjWefp124LlJaKyo2T61RI6ZDD9BBT1Ccs3aFRRExHYblPZpEBBi-D1-oPQCU_hBhXJ0mI3wQ6gIVmuZsFEPRw612MqMfnB2FgqtZLncNuyncyAjB-ZWLlc2g5GDb9PAX64LaBoZ0CW4kcFcqL5lMVvLyD2L16OMzud6X8YCPTwPNmj9-4bFWyHh-WaHHMcvrSZW2-WXNoQeU7tfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رکورد دار عمل زیبایی بین آقایونه و تا حالا بیش از 300 عمل زیبایی انجام داده!
پسری که عمل زیبایی نکنه اسکله، تا حالا 200 میلیون خرج ابروم کردم، 150 میلیون خرج لبام شده
😶
استایلم فقط 400 میلیونه، 500 میلیون دادم که خط سینه بندازم. پسر باید به خودش برسه.
هزینه روزمره‌ام روزی 100-150 میلیونه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70983" target="_blank">📅 10:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70982">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⏺
🇮🇱
نخست‌وزیر نتانیاهو:
آیت‌الله‌ها می‌خواهند من در انتخابات شکست بخورم؛ حزب‌الله و حماس هم همین‌طور؛ و البته ترکیه نیز خواهان شکست من است. آن‌ها این را آشکارا بیان می‌کنند.
صادقانه از خود بپرسید: دشمنان اسرائیل می‌خواهند چه کسی در این انتخابات پیروز شود؟ به شما می‌گویم: آن‌ها نمی‌خواهند من پیروز شوم.
ما برای کل جهان آزاد می‌جنگیم. آن‌ها این را می‌دانند و به همین دلیل است که می‌خواهند ما شکست بخوریم.
ما اجازه نخواهیم داد آن‌ها پیروز شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70982" target="_blank">📅 09:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70981">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=rnTZ7ccg0Kvkw4CsQxuIDo3yEfrimqOZUwBywnKFETWdooxYetq8yK9JYb7xQAlnin8EcXaf1JovNdRyUl835j7BzuvJetOFGz_YH0BIRST4mflyRQyWZnzfoa8jxtqyaNl9FFWKKWGQwhC5ppmzrNUFNARTKFUv3moAGau_pUKhBF9wTiVTwiE1CjsZa_uQv62vT6ro7dNYVAZ6FlHkHhNqpLu-2AlHgZ4wOnGHn-3FdB5U0vGMR4VhS-wKDEPVdl2sBP3mhubsSCGbgdVpX9qIFxxTqjIOqEIr_1xxqjPh-CzYkOhAEpqTJBzj47UkkouZnThc0Xl6N02XYpDo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=rnTZ7ccg0Kvkw4CsQxuIDo3yEfrimqOZUwBywnKFETWdooxYetq8yK9JYb7xQAlnin8EcXaf1JovNdRyUl835j7BzuvJetOFGz_YH0BIRST4mflyRQyWZnzfoa8jxtqyaNl9FFWKKWGQwhC5ppmzrNUFNARTKFUv3moAGau_pUKhBF9wTiVTwiE1CjsZa_uQv62vT6ro7dNYVAZ6FlHkHhNqpLu-2AlHgZ4wOnGHn-3FdB5U0vGMR4VhS-wKDEPVdl2sBP3mhubsSCGbgdVpX9qIFxxTqjIOqEIr_1xxqjPh-CzYkOhAEpqTJBzj47UkkouZnThc0Xl6N02XYpDo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
سنتکام ویدیویی را از حملات به ایران منتشر کرد؛
سنت‌کام، فرماندهی مرکزی آمریکا اعلام کرد نیروهای آمریکایی در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
بر اساس این بیانیه، مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، زیرساخت‌های مرتبط با مین‌گذاری و مراکز ارتباطی سپاه پاسداران هدف قرار گرفتند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70981" target="_blank">📅 09:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70980">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70980" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70980" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70979">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR-oWidxX8FJ5h-3VYMT_PKscKHmVK_iduQx_1Zr5IlnGTv-p_EDtA67E9lRRi13JXJOx12fUxiWSQYdrE0HJMJyu2Z2H6IhkqK_RH2ZR7MroCTssCSHIAN67C66Je_ImXzpP80k5UJgBC7fcNcNMcJcbPP6lxJbo6NgWmxNwTOIPNR_WZ8XwjCAMc5E91387nWx-6iS7RLHTtuVkrOqJ-yfwNqmpiYK6b3AgbenznyFy_U1x8Lifd_ctaGPR5ZFy30ZS9NZANB645B1vfohryNFadHwzjOCfO2s71OURp74wS0PDkhRQAJh-zw_XieijrxGDf5SBfS8mpUKNyMZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
سایت جهانی
TrexBet
می‌برتت وسط
جنگ
بزرگ!
⚽️
استقلال
🆚
پرسپولیس
⚽️
اینجا فقط فوتبال نیست… دربی‌ـه!
۹۰ دقیقه جنگ، کری‌خونی و هیجان تا آخرین سوت!
🦖
🦖
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70979" target="_blank">📅 02:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70978">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در کویت و بحرین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70978" target="_blank">📅 01:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70977">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUVVpqrVrUV1Rv9Ys0ZsO-Y8MBxTveRdLIRkeyh9Gf9md0l1yv2K_JJ5fte4SGMrNP0yGyitG_SH56rZ5nSFWvZH_Biwdtc7XgxfjRJ2WzOeSfgxVzq8p74Vn_wtj0ZGYcZ80ixxPNwpvu0jAZvi7LJv_CsPzlYY8pVSjO_rBEdUJT8s9XL3e201L0MWkZQOCg6sMKCcgVFP87nXlFtE3eR7Dk9JurfGTqhgMkzqbMBi5NeGUTeVgJjTedCpLaZTuBbfYqWPq6FUR-x4p5YGwFIaRHdcmR_Ao78cAGTR_C1mq-iWbqtpWFfdXzAGfocFHmALVNSM58CO3geEm4vYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70977" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70974">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⏺
🇯🇴
نیروهای مسلح اردن:
پدافند هوایی کشور ۱۳ موشک بالستیک را که وارد حریم هوایی پادشاهی شده بودند، رهگیری کرده است.
به گفته ارتش، ۱۰ موشک رهگیری و منهدم شدند و سه موشک دیگر در مناطقی دور از مراکز جمعیتی سقوط کردند.
در این حمله هیچ‌گونه تلفات جانی یا مجروحی گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70974" target="_blank">📅 01:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70970">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/boF8Rjwqb6hyyBuNiLP_9qxp-BakNxyqiZjTekbs3JBKBqyI6X1SRvidgwtHvisICm2fIIdmJLvyjOcu0mn2v2jMOq4noewQIgGRB3V6drxDF1APi4tzpeOM-z3Iip3PXKDD2VxhYFGBhbAiKHgPB19qCE7qxe57jN8wTCHh0UAfxf2N_MyW3iHgN4pgTNLSRoE3pa0k9rozE1k71UIF2YrSPKKPpMLLnig8tmN4rqIYcP0VhSl608E8lAaQcBLFEY4c-YHMEJQdsl47H-wvyGrUIHmy8X4zSA0yNC7vpOjTUZMZ0NMJhgSug263wF6gaXvmOqD42bPr4DJItCe_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/703c34050b.mp4?token=o6cJbPWqDKCfl-3DqaEvIvnpIUQ4WZMZ6N9CJrESOnhaLwEtZwjh5u30VxkP-ut22rPRWgc68x-RUbswFJVN0DCGqS3v70KlwUzG3pN-n939j4Y2SVzyZdoBgZ46CSkEkk0hwDlnk_5RWbHRwecX6LzWwmvSSlL1op9S2tkO8y188lrkY57qONX6DwNv9uicN7vkMGJWYdiXhHl0Vd78mlsB06lMD8HHsUPKUrHpmNktA7ABlqEy9Iit0Y7JjcCKHfGyREpzpUlW_EZr6YNc9k8qn-HUySmOIqn_26c8pjrpHW4CkJdrpHlP8C417KLeskrHHYOY5aVI_7A4pezZug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/703c34050b.mp4?token=o6cJbPWqDKCfl-3DqaEvIvnpIUQ4WZMZ6N9CJrESOnhaLwEtZwjh5u30VxkP-ut22rPRWgc68x-RUbswFJVN0DCGqS3v70KlwUzG3pN-n939j4Y2SVzyZdoBgZ46CSkEkk0hwDlnk_5RWbHRwecX6LzWwmvSSlL1op9S2tkO8y188lrkY57qONX6DwNv9uicN7vkMGJWYdiXhHl0Vd78mlsB06lMD8HHsUPKUrHpmNktA7ABlqEy9Iit0Y7JjcCKHfGyREpzpUlW_EZr6YNc9k8qn-HUySmOIqn_26c8pjrpHW4CkJdrpHlP8C417KLeskrHHYOY5aVI_7A4pezZug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
امشب از نقاط مختلف کشور به سمت مواضع آمریکا موشک شلیک شده؛
🤩
تسنیم:
امشب یکی از گسترده‌ترین شلیک‌های موشکی ایران (به نسبت درگیری‌های اخیر) به سمت پایگاه‌ها و مناطق آمریکایی انجام شده است
ایران هشدار داده بود که حمله دشمن آمریکایی با پاسخ چند برابری مواجه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70970" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70969">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند
⏺
روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)" با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
عملیات انتقامی نیروهای اسلام ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70969" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70966">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2a4aGzC3d-468TK0lgCCE_VZR2dgYyjD4ym8a7e3LoatLHpjk3ntXz5y0RnKIAzWD15NZnHkpCKLr__SAz8o0zDRTXgngxAARPMnrih0Uk3WNtlI5yr1GKuQeBZvqGQnSqtVQlRka36rrUEGi01fbGuHrKVcWkZPJPwJPaXxDAXbb4Eqnbq7Dbxh-BJ7N84gCz45I9AQcPHFv6WcxzcOWnxZc1lssLhdkIZfaQCjvq_j5xUVNB-D1zsbUKlbhRqVDfJ85fyRBK95wW8teyWIdwVBvSUk1xfLZcqpGYO8o69SkoHj5UxkJ1l1c6qMr47lpRH4ocYbEOlLEI5ejEDTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=H8tpHMshtmeqR6KuD47RsIFYxJ1E8qIcV6I242QSNHhHqwRdsPvUgaJf4rp4o4mh3ZJIdOK02MtFKb3d9DJdp7ihxH-mWybgZ-ZmFbv_prQACRJyyfJdoEhfZaPN-GuKWxeVbsBBY0MOW8LYTe2ixEgnWpz4UdhTKnqCguSYRxs9itWyLWYozNFPypKTRJUXalR5XbyS7UJO5CWOA0F2ynCOXLMaJErzy7D7TT6ndNBw2iptqQMLdqTwrEDBgBTY-6HRSQlLfpsLB-T4YtXWiKk47xWxIa9egJVTed6_zUPzE6GXaabeqr9YJvAjVscVqnAbqGEMhnMbWwKUtZjZ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b67f6c5b37.mp4?token=H8tpHMshtmeqR6KuD47RsIFYxJ1E8qIcV6I242QSNHhHqwRdsPvUgaJf4rp4o4mh3ZJIdOK02MtFKb3d9DJdp7ihxH-mWybgZ-ZmFbv_prQACRJyyfJdoEhfZaPN-GuKWxeVbsBBY0MOW8LYTe2ixEgnWpz4UdhTKnqCguSYRxs9itWyLWYozNFPypKTRJUXalR5XbyS7UJO5CWOA0F2ynCOXLMaJErzy7D7TT6ndNBw2iptqQMLdqTwrEDBgBTY-6HRSQlLfpsLB-T4YtXWiKk47xWxIa9egJVTed6_zUPzE6GXaabeqr9YJvAjVscVqnAbqGEMhnMbWwKUtZjZ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه امشب یه خبر بد هم داریم، در طی حملات آمریکا تو بندر کوهستک حوالی سیریک، ترکش حملات می‌خوره تو یه مراسم عروسی و چهارنفر جونشون رو از دست می‌دن
🖤
#hjAly‌
@HutNewsPlus</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70966" target="_blank">📅 00:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70965">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USjmOnLbXxHrXKizlhxA52bivaK5Kjgay7OMVyOOOQzYvyEmcRyT0B5SWm4zCrFc_IyH09vKe-4-1Tf1bUaLnwB6sioYueUiV9JjsKKCAaec5LIh7ra3yk-NWYc2D1aj2y4HwjnTyTHgUipo2wkFcC2xo27ACZ1WjtJWi4Qqn4jG7f9Mu_js1MXfseLK-JpX-9e0VKT2XDSVLh2mKyYKCEJlZi56GbfXtzaz8Z1n66SA25BigZDyYTSGOTTZ9RsDshzHNzCUJMXGFoMn8NNTfOlI48XhIhS7es0ywr_5DvatTmfqOCONOpxIPH2MnckNwdOn5o41zwh7w65EQhxQNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.  @News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70965" target="_blank">📅 00:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70962">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=W4rd9o8u7dfC8rvW69bqmwuhzg9w2kQjcg5hA0e_7_cD6yyBkO1KpBszFBoP22kuG8_WxEcgP-sbiuhf1ZDPz0oJshY2UP9gPRQAESkya6YCyFfvN_sHX88H5lTdugLxWdRpqnrh1b4D5Kob_thePUtYFsrIIuq-UJp0CfOoa28U4uN86IwNYcYkA_lHxyN9CKNDA-mwmj7BeVuYvigv6WFoKg67Jbm2GtSLFp3hPniZv2u46c457SkAt5sQNB5r0_NiMQeXbdkEbl9D4YDbGynB3d3Ll2sTTvvqi6F1ZaIoDot8UxipaTedcYO5VEfOorKSPc6-YY7sI4fZPB-rdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=W4rd9o8u7dfC8rvW69bqmwuhzg9w2kQjcg5hA0e_7_cD6yyBkO1KpBszFBoP22kuG8_WxEcgP-sbiuhf1ZDPz0oJshY2UP9gPRQAESkya6YCyFfvN_sHX88H5lTdugLxWdRpqnrh1b4D5Kob_thePUtYFsrIIuq-UJp0CfOoa28U4uN86IwNYcYkA_lHxyN9CKNDA-mwmj7BeVuYvigv6WFoKg67Jbm2GtSLFp3hPniZv2u46c457SkAt5sQNB5r0_NiMQeXbdkEbl9D4YDbGynB3d3Ll2sTTvvqi6F1ZaIoDot8UxipaTedcYO5VEfOorKSPc6-YY7sI4fZPB-rdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تو وکیل آباد مشهد یه ماشین به تجمعات زده ٢٠ نفر کشته و زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/70962" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IheemEU9hD3xHqqE4kS1y_DwGGmsNOrsqyKCLDoAzbUUSLHgAXpUZpyzq7xQTFa_2CPCNk2pk0v1Q4F9kvcWH5PH9N6eklrcqQ1uxyL6ss2QFQNwTBR-1nyKMt9Md13rQ2trxCnW9sEyVTTwOV_IkcYNPKgbvxNk_wriecVVpx1dqTprNFB4E1Z0QMXleh-7v2O2GjtxmrHLRQzokX-Biad8kbzpeHDpHtVHJ_5F2w5a6PZ0dyNiKDcMxg7MvKDxz6h_oGMFq4iE15Rcf3iK_N-hTb5rLdoVc68SUVjCrssPTn_UTiOHpBmiLmL5P-Vj9RBRshNGnsFjs8yLhjGKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=JsFSPkmu81aqBdoH5cnH6olURY0awFSmwNCteNLNEQUQA-EzSfCIFMKhyXeaY5tWo7njjylvVVBOBLy044h6FU0yhw7gdUaPPQ91AEJwt69JrLpXy8vg6Q4G0WjoPIalYVbgSOotOBwI8GLIYXZlFw2UgZphpzwi6bAKSbcMm77RE0JrmeKS4YrJoqaBCFTndQx_QAnu8kpPOiVWUDyykOfItq2iXRAHJz19BduZtnWwthxBOcNbOs_ET43PFNYnxTxJYSB9b6bLqoyBsgF2VC1TXXw3BJ4ijwXOF5dXMNwfwvwSIgVnh79gJF-1och3q-A2BrBNc0wrefWVQIFf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/791bfa967f.mp4?token=JsFSPkmu81aqBdoH5cnH6olURY0awFSmwNCteNLNEQUQA-EzSfCIFMKhyXeaY5tWo7njjylvVVBOBLy044h6FU0yhw7gdUaPPQ91AEJwt69JrLpXy8vg6Q4G0WjoPIalYVbgSOotOBwI8GLIYXZlFw2UgZphpzwi6bAKSbcMm77RE0JrmeKS4YrJoqaBCFTndQx_QAnu8kpPOiVWUDyykOfItq2iXRAHJz19BduZtnWwthxBOcNbOs_ET43PFNYnxTxJYSB9b6bLqoyBsgF2VC1TXXw3BJ4ijwXOF5dXMNwfwvwSIgVnh79gJF-1och3q-A2BrBNc0wrefWVQIFf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به دکل سیریک که با پهپادهای انتحاری لوکاس(کپی شاهد) انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70960" target="_blank">📅 23:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541d79e411.mp4?token=tABDNBKZQJjCtWSZwcDymkQKGV8YRSc77A_6rLxRpNt5WTrdadslcML9Ikzk6TkoWv_Y5oqTTvq5D73EgBO68v0yvsPg3pWerrC3oUR3EKtsoVtflqit5Gh8bF-6mA-w4Tky7-Y0kY4vFvg8lcQZLo9BqBO6Kmbugb02HfZIs2pyWeQy-ijqEarFZM0tnYtkH67aUtAHqy4d2oIi3XJdL7pJ3fxRqjUlm4Ks-X7PXlmGEG55t3LoVwQngUQonco79eERaN8K6sBicdhVr5hdITT_aIFwJ8UhvJsfxIFGKwNTLGtpLkbpjcYpK9l1MHsQ-SeZZaPPc4KG-Tm7LdnXJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541d79e411.mp4?token=tABDNBKZQJjCtWSZwcDymkQKGV8YRSc77A_6rLxRpNt5WTrdadslcML9Ikzk6TkoWv_Y5oqTTvq5D73EgBO68v0yvsPg3pWerrC3oUR3EKtsoVtflqit5Gh8bF-6mA-w4Tky7-Y0kY4vFvg8lcQZLo9BqBO6Kmbugb02HfZIs2pyWeQy-ijqEarFZM0tnYtkH67aUtAHqy4d2oIi3XJdL7pJ3fxRqjUlm4Ks-X7PXlmGEG55t3LoVwQngUQonco79eERaN8K6sBicdhVr5hdITT_aIFwJ8UhvJsfxIFGKwNTLGtpLkbpjcYpK9l1MHsQ-SeZZaPPc4KG-Tm7LdnXJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
اصابت موشک های سپاه در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70959" target="_blank">📅 23:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
‼️
وضعیت دکل مخابراتی کوهستک سیریک که امشب بهش حمله شد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70958" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خود ترامپ، هگزت و بسنت هم پشماشون از این حجم از کله‌خری سپاهیا ریخته
#hjAly‌</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70957" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
از بیدگنه هم دوتا موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70956" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
شلیک دور جدید موشک های سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/70955" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">من فکر نمی‌کنم ترامپ قبل انتخابات دست به حمله‌ی گسترده‌ای بزنه، سنا تو تصویب بودجه برای جنگ نقش اصلی رو داره نباید بیفته دست دموکرات ها
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70954" target="_blank">📅 23:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70953">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=XW1OTUDDtvcHDnR8MP-H7T25kHo9TiP7CQwouUUTuZdoDKJUw5iKVcIh231NXXx-D3bd6WKWgGsaa32zHlBCu0oFpLe52jLGneRG6YRCRZcKnUEXXzSbBl6y_SjaKJWzom1i385-TgKYSNRMa8tB8vmQb996HyCUl25AeVhVodEjAAUQcddaGIy9UiAPU0iwX-nVScBF0ysgTWK2Wmc4f5naLTYxRAIK_yncXmN1Wg_3plDp57AZ6Efeo-DVhejSdL3N_W_RRrVVA9Kj1v4oJYuBckT86fjXrX5T19B-vuHWB631NsX6aXT3mjlBUvrKPxYb9Pw7iKvAcebfirRHag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c95b26a1b.mp4?token=XW1OTUDDtvcHDnR8MP-H7T25kHo9TiP7CQwouUUTuZdoDKJUw5iKVcIh231NXXx-D3bd6WKWgGsaa32zHlBCu0oFpLe52jLGneRG6YRCRZcKnUEXXzSbBl6y_SjaKJWzom1i385-TgKYSNRMa8tB8vmQb996HyCUl25AeVhVodEjAAUQcddaGIy9UiAPU0iwX-nVScBF0ysgTWK2Wmc4f5naLTYxRAIK_yncXmN1Wg_3plDp57AZ6Efeo-DVhejSdL3N_W_RRrVVA9Kj1v4oJYuBckT86fjXrX5T19B-vuHWB631NsX6aXT3mjlBUvrKPxYb9Pw7iKvAcebfirRHag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم‌اکنون حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/70953" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70952">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=Kba92_2vGNGlgF9ur4oXh1bwkkRJlwy37o5y1IA8350hEcgHMVN1FTlv2iwtByafJF4QHSM28r3_xwFTmmNNbaCzwXdZAS-mSQhF9Z_TpQoxUvk0oVX_4CIyAyWH5qlpqmmqivGgG4_nPCoYrLshR3X1djohopUN-E22Td8NuVAkPcQJx6GzTg9VwNQmOsP1ur1GBjg8BLimivKJgnA5THMIZVrVXyZYf7Po0qsoCFhrJUxC6GHBY8ERc_tj0Vw2bUpTqTGQ3oemwiVCYlLq2s3E-GYE3KC1O8YYfEdXGz7-HFZLMJhkl3_dqjpwkmvPIkAXKM58ExcN-f0msP5HAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfcd58ff7e.mp4?token=Kba92_2vGNGlgF9ur4oXh1bwkkRJlwy37o5y1IA8350hEcgHMVN1FTlv2iwtByafJF4QHSM28r3_xwFTmmNNbaCzwXdZAS-mSQhF9Z_TpQoxUvk0oVX_4CIyAyWH5qlpqmmqivGgG4_nPCoYrLshR3X1djohopUN-E22Td8NuVAkPcQJx6GzTg9VwNQmOsP1ur1GBjg8BLimivKJgnA5THMIZVrVXyZYf7Po0qsoCFhrJUxC6GHBY8ERc_tj0Vw2bUpTqTGQ3oemwiVCYlLq2s3E-GYE3KC1O8YYfEdXGz7-HFZLMJhkl3_dqjpwkmvPIkAXKM58ExcN-f0msP5HAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات موشکی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/70952" target="_blank">📅 22:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70951">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رسانه های حکومت: آمریکا یه مراسم عروسی تو سیریک رو زده و چن نفر کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70951" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70950">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">همچنان هیچ ویدیویی از موشک های سپاه تو آسمون کشور های منطقه، منتشر نشده
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70950" target="_blank">📅 22:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70949">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  اگر ایران پاسخ دهد، انها از بین خواهند رفت  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/70949" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70948">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/70948" target="_blank">📅 22:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70947">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=Co1ayYHa06pBKeWfUoDdFySaO_sNxb4yrygjLMLlWKr6gvDJ_95lDnT21yRdI4x9jaF-2mfbZTOeDJc_Iw2ISDy7jTKGFDxibLTDp2-Ojbv0EA5U9Oq7DPc6PlJolZfq-ivFsNSsWtoNcbDyEkqxBcOo1kD9o_YbCsZwwC2a8sWEdWv5cZg6jt1pA9eCmCRNGz3CgeuIWqpuu_vvJVfYWO6nu-WdE9xZ7FBB7WIDUZpumE0R-gWnTIbY8jOoX-5aF0DLo7mKd_P7v7VUJD2bpO2yWoblSevtsJM7j1K27UtL6HjedXMSaMb0GbleovQi8rThLa-UFDEnbvC5hEbgFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=Co1ayYHa06pBKeWfUoDdFySaO_sNxb4yrygjLMLlWKr6gvDJ_95lDnT21yRdI4x9jaF-2mfbZTOeDJc_Iw2ISDy7jTKGFDxibLTDp2-Ojbv0EA5U9Oq7DPc6PlJolZfq-ivFsNSsWtoNcbDyEkqxBcOo1kD9o_YbCsZwwC2a8sWEdWv5cZg6jt1pA9eCmCRNGz3CgeuIWqpuu_vvJVfYWO6nu-WdE9xZ7FBB7WIDUZpumE0R-gWnTIbY8jOoX-5aF0DLo7mKd_P7v7VUJD2bpO2yWoblSevtsJM7j1K27UtL6HjedXMSaMb0GbleovQi8rThLa-UFDEnbvC5hEbgFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب ناموفق موشک سپاه تو خمین
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/70947" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».  رئیس جمهور گفت که این حملات سیستم‌های…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70946" target="_blank">📅 22:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70945">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=Zri3MsPR4BBH6AgpVxHSP9VFzHyk5wrfdqj69Ccs-kncmks7gpFj0LggRjAu1HpnEunLDwNadXgO8uwO-Tq7He7IK7kr7OPTmEKaueyuobqYzqBmbb9-Munk3pKdRBq_pvMgKyklQrkMaOyyoL6cmaoeRVHMaKj3U6YAv_GzIzyaVGKsHwrpNoDsEDV-Va9W_N5LozacVYlnj98P_n4Rkd_jwzQ0czYPx_j-o7Xrjzqygb5QeOdy8UCOE7cuzpTL1TRlgU8MvXjcBL-jzn5ZMByvEePNnKmttlgy5OzSed_ABTnrQ4BbtKIHwTumLJiQ5bS-5MtBqDIhERUA8ZM0qGjvpQo-xGTdHppA2a8QCoQvrhk4sVGI4aO_f0SIpoD3fjsT89LmMITIjkbYzkReDzVFPGJZY_DNrSVSuKeZeSakpVj1OIqn2fQsvATVr7kTdXDaUF_4nhp_DIQzwfVnaUFjupcNhghYkOxEo2ylZ3Gyp2IhiZ-UqEA5G8bSR3RSywanAcjZONvalHrgZBtqKAP8_dyWR6Q5kcPcErOc5wKBh9ppmDvvMj-wbY0BNAzMQmst3T683fT2_bsweXuq6gHqBPd2ymcTOWPNIkMZ2QLwEGKjFvs-qefUC9dQqZvs0wJ0v8GZPSp8W9-2dzh1Zii1tol1WNHptDOELWwZ4Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=Zri3MsPR4BBH6AgpVxHSP9VFzHyk5wrfdqj69Ccs-kncmks7gpFj0LggRjAu1HpnEunLDwNadXgO8uwO-Tq7He7IK7kr7OPTmEKaueyuobqYzqBmbb9-Munk3pKdRBq_pvMgKyklQrkMaOyyoL6cmaoeRVHMaKj3U6YAv_GzIzyaVGKsHwrpNoDsEDV-Va9W_N5LozacVYlnj98P_n4Rkd_jwzQ0czYPx_j-o7Xrjzqygb5QeOdy8UCOE7cuzpTL1TRlgU8MvXjcBL-jzn5ZMByvEePNnKmttlgy5OzSed_ABTnrQ4BbtKIHwTumLJiQ5bS-5MtBqDIhERUA8ZM0qGjvpQo-xGTdHppA2a8QCoQvrhk4sVGI4aO_f0SIpoD3fjsT89LmMITIjkbYzkReDzVFPGJZY_DNrSVSuKeZeSakpVj1OIqn2fQsvATVr7kTdXDaUF_4nhp_DIQzwfVnaUFjupcNhghYkOxEo2ylZ3Gyp2IhiZ-UqEA5G8bSR3RSywanAcjZONvalHrgZBtqKAP8_dyWR6Q5kcPcErOc5wKBh9ppmDvvMj-wbY0BNAzMQmst3T683fT2_bsweXuq6gHqBPd2ymcTOWPNIkMZ2QLwEGKjFvs-qefUC9dQqZvs0wJ0v8GZPSp8W9-2dzh1Zii1tol1WNHptDOELWwZ4Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».
رئیس جمهور گفت که این حملات سیستم‌های راداری در جنوب غربی ایران در نزدیکی تنگه هرمز را که در حال بازسازی بودند، هدف قرار داده است و افزود که ناو هواپیمابر جورج واشنگتن کاملاً مجهز است تا در صورت نیاز به عملیات خود ادامه دهد.
ترامپ همچنین احتمال توافق جدید با ایران را رد کرد و گفت تلاش‌های دیپلماتیک قبلی شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70945" target="_blank">📅 21:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70944">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس از آغاز حملات موشکی سپاه به مواضع آمریکا در منطقه خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70944" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
"اگر آنها تلافی کنند، ضربه بسیار سخت‌تری خواهند خورد. و اگر دوباره این کار را انجام دهند، دیگر نخواهند بود."
"آنها متوقف نمی‌شوند. آنها دیوانه و احمق هستند."
"آنها سعی کردند رادار خود را بازسازی کنند زیرا نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و سپس به آن ضربه زدیم."
"من فکر می‌کنم توافق با آنها ارزش کاغذی را که روی آن نوشته شده است، ندارد. ما به آنها فرصت‌های زیادی دادیم."
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70943" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70942">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در گفتگو با فاکس‌نیوز:
اگر ایران به حملات آمریکا واکنش‌های مکرر نشان دهد، ممکن است «به‌عنوان یک کشور کاملاً نابود شود».
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70942" target="_blank">📅 21:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=U7Wc_RByIWgsdATSWOQVsvZ-P3FY7_KB56kPjaQ_v2WksgFfMazlo3EJamGYhBNMISLEeZ6ImP5P9PnvjjEOiNiNLj0UwBH-C5yQr47V2cyvreQl-J34tIc7VXIC9RIb9iWgh_m6O30RfmM9VuAlmJGhCTyzJqNlvgQXL8GvELpqItE9w4luF-QFluPjSRkrn1XldGhYChA5XdFMHOQpE2CjeKgM1zJhNIjnPeon4VpdNYvcb8JbMywnkS6F24uKGkIH5zx5j6rwDTpmrGO5XQe1oM5ALeN5lo57TrnNR7WR40pn63S6fFKt3D9e_XD97p_Jt6iMNUITmL9zSGNvUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=U7Wc_RByIWgsdATSWOQVsvZ-P3FY7_KB56kPjaQ_v2WksgFfMazlo3EJamGYhBNMISLEeZ6ImP5P9PnvjjEOiNiNLj0UwBH-C5yQr47V2cyvreQl-J34tIc7VXIC9RIb9iWgh_m6O30RfmM9VuAlmJGhCTyzJqNlvgQXL8GvELpqItE9w4luF-QFluPjSRkrn1XldGhYChA5XdFMHOQpE2CjeKgM1zJhNIjnPeon4VpdNYvcb8JbMywnkS6F24uKGkIH5zx5j6rwDTpmrGO5XQe1oM5ALeN5lo57TrnNR7WR40pn63S6fFKt3D9e_XD97p_Jt6iMNUITmL9zSGNvUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیویی دیگر از موشک سپاه که در خمین سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70941" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=fS8ATgPCWXzc09_PVG9jtbbVm9jQ-g1WBYlsaYhr7wv4FJ2Cxk9dM3SKxhI5M_xgM2kBfKRIcNC0qGU6NFynBVX1td8o0JWzDBBEO7sbtwk0r3KBXMnHsqae0Dmd73TviD2wf3a-HSG1u6kxHllENpTA2Ze5Ja2TBpqphsKLIYFtvFTZAkuo83NfWwrtBeP4kyFJ1_whdODranEkM9FU_AgiG_kzeNE5Hna3ihRArYOMMmi5u2cUYmetbDoV9miz98YHKNcdU4naiVadD3HC163-Ru8LWEDodXVxJJsw_f2smJRVZJ3NMwHGR_VahDCwsAWDPCIqpbO8DFQQLbhJnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=fS8ATgPCWXzc09_PVG9jtbbVm9jQ-g1WBYlsaYhr7wv4FJ2Cxk9dM3SKxhI5M_xgM2kBfKRIcNC0qGU6NFynBVX1td8o0JWzDBBEO7sbtwk0r3KBXMnHsqae0Dmd73TviD2wf3a-HSG1u6kxHllENpTA2Ze5Ja2TBpqphsKLIYFtvFTZAkuo83NfWwrtBeP4kyFJ1_whdODranEkM9FU_AgiG_kzeNE5Hna3ihRArYOMMmi5u2cUYmetbDoV9miz98YHKNcdU4naiVadD3HC163-Ru8LWEDodXVxJJsw_f2smJRVZJ3NMwHGR_VahDCwsAWDPCIqpbO8DFQQLbhJnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نقص فنی موشک بالستیک سپاه پاسداران در آسمان خمین
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70940" target="_blank">📅 21:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIW1chs4xRpXpLA8NUz9aQkk3hXyRfpqCnkI8o6wazV73aVwlrP1CJrNL6ETEOhpasb6KOIt2sw1B1-xNk1rUvTb7Sf25LM9VkvEGbQiprDLeHYixkdA2JVigR_yXfpLuhQqNrjvWyqMNcSw7BqECvHfEEQFvjfQ909mAWd1hVnnkY4Y1XqgDskRoaLLc48zrt2wqFpJVmzjNrJK0gnXFdrmIIPoe_sNOXsFXyGWp8Y7tNKQCea5AiO_6JrfY4WbkKZIVrR7qxTO83JxWE43pU_NMTXMTPsz5iUfH4GccmXN8xO_3P_2eYyzK5e-DraDrQfV2ucbGS1ZiL6h3yaNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ستاد کل نیروهای مسلح: هزینه سنگینی بر دشمن آمریکایی تحمیل خواهیم کرد
🔴
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا:
در پاسخ به تجاوز هوایی ارتش آمریکا به نقاطی در سیستان و بلوچستان و هرمزگان، نیروهای مسلح جمهوری اسلامی ایران ضربات کوبنده و شکننده ای را به دشمن زبون و شرور آمریکایی وارد خواهند نمود.
ارتش تروریست آمریکا هر چقدر اصرار بر شرارت در منطقه داشته باشد باید خسارات بیشتر و سنگین تری را تحمل نماید.
بارها اعلام نموده ایم و اراده کرده ایم تحت هیچ شرایطی از حقوق ملت قهرمان ایران کوتاه نخواهیم آمد و هزینه های سنگینی را بر دشمن آمریکایی تحمیل خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70939" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
گزارش انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70938" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILWNbfIOihvxLQEfb6aiyN47cy3UL-XHQt1mJXYfyuZnCYsF7NaveSnkefcZCsiMlc4IPNdCDYDkLy58gUNhDzdp0BltSwc5As5UAUi4B9th7ZfbVu7LGQwjtpYK29tldRbZbKAIh8yJPfSMHnmfhFxCs2g1_TWo2g5j31yoyNu6pf8s1PJ6WAUqZtrp2Ac1uOTTM4fH-IqeUfXV_jyzPbdu6OE65C5FQBF1_pCLp4XYDqr8c_bz7_hrtbhv-V8Bv2oGAexkg9EGK56Wk5e06WsYDdyx2yBcWdp7yJ3hnYyWI9hdvtnFStgYUkXSqIIDur4e3a4oOk0Tjj3oaORRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:ایالات متحده همین حالا در حال هدف قرار دادن مواضع ایران در نزدیکی تنگه هرمز است.
🔴
این حملات گسترده و سهمگین هستند و در واکنش به دو اقدام صورت می‌گیرد:
نخست، تلاش نافرجام ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه‌ای که در حال حاضر فاقد هرگونه مین است (مین‌ها کاملاً پاکسازی یا منهدم شده‌اند!)؛
و دوم، شلیک هشت موشک از سوی ایران به سمت پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر ایرانِ شکست‌خورده بخواهد به این حمله کاملاً موجه پاسخ دهد، بار دیگر با ضرباتی بسیار شدیدتر و سنگین‌تر مواجه خواهد شد؛
🔴
اما آن حمله، بزرگترینِ حملات نخواهد بود، چرا که حمله اصلی در کمین است و پس از پایان آن، چیز زیادی از جمهوری اسلامی ایران باقی نخواهد ماند!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70937" target="_blank">📅 21:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⏺
معاون امنیتی و انتظامی استاندار سیستان و بلوچستان از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70936" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5M56qgVhULgioq56G1ki41LHpjRM-aEs5610H97mJt8MATX9h_YXAHAklrjpLE17qW_RJbXJsoYieKT4tWO-oxAcsmxLZTrA3iSzI0IMwZacGPlWgEZTZbQvHHT8xz2CEHOIBgmc8k76TDw80CfYL0rCz6YfuENhRlm5xHz5d249iQp3UDqZYM6ISIXrK_tzagCHTZiHS9AwGXXOF0NlpuE2hPVZGwe3dSVvWzda6wzr1DsA6w1chL6kZSVlfB7phyPHGzAfARkvUzinvW_1JrdKhl1zWqFvRMNhsXV_wuyPgVfWIX0BhFFTDU_VAtAbAHf4Doip3h0t_WuHJSUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70935" target="_blank">📅 20:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
تا اینجا در چابهار، جزیره قشم، بندرعباس، کنارک، جزیره لارَک و سیریک انفجار گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70934" target="_blank">📅 20:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgf9agRLTSh6qQpOgSECnjgp6nBkyLdoykad9sdZRtsSZFa6YwUiE4DhgaYKsBeyiD-fby8iHj1Nds0afzTsebxogpd2Zg2186xKX1HT8AH81wx_oELT4ftKv16zPW60-P26ADmTJPKiIX2XcIYxVS7_X_7M5vDUgzwl9Z1k_fL7WbTDFfVV5jc7r73UHf-Mn3XDgXbXd8U3yhbS_bx7yaKK6JBGmfqQQ2JhHz616rAT-BobvlZ7V5WLuQfLPXiKzLULpgONglCzqd3BSQU5b1LHHSIVXF1SYdwj-mfx16rZwQvOhP0jhupCYpFlJxNwxkOA0S7-Qe61TNDlZGpntw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
〰️
#فوری
؛سنت‌کام:
امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده حملات خود را به اهداف سپاه پاسداران انقلاب اسلامی در ایران آغاز کردند. این حملات در پی تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و همچنین نیروهای نظامی آمریکایی مستقر در منطقه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/70933" target="_blank">📅 20:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70932" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mEZyeCuqonx5rTSexv8zDc-bZoCDoYi9CQhxmZJ5l2eKKG5_UZM0q6F-nStGBkLWNC6eDi7aVwO1nA_VqQk-uaK8ylCCUd8mop7vqCrU14uxpQla9WyYcySbd_I5U_dI2uDY-V8z7-C2x2BLivbj-JNF1PJW-utPtTJHLVgGbSFR5661NAQzODA9-SBDIxNvNkmljkEttzbFJKhgTHK4mDJuZ60-p9Qa4YyimyriSB37iejiZNIeeTKAzzn0nMNH57aKJbLFH6mEGWT6Xdbg04pnHLUThVv96E_29Gvr2aZFXndHasowV2IsRLR9cwndrNftgGF7-rkGyps88QmObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70931" target="_blank">📅 19:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
گزارشات از صدای سه انفجار  در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70930" target="_blank">📅 19:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=QBZPPdyzcmvtjAqh1_amHegMrOmFLINt09ho9gyLy00uW-bGbV8I9GhPYDSkfooxkA_uwTfPEyy7TYTYRm1FiSmMgktpi0svRhjEor8t1H9ZnTKqws31OhXKsddblhYSNabTQCjunyDUQDT_twTWPJMExaBU97E_eKyDjDqvBxVf10YTsEPrrmgZqTCYwd5iYtVT-pRU-ipfWEoYqTqc44y9z-t_rRWtcSiW9OxZfqm8xCyOBBcDkJu5YiSO7JwXDpmFjD2a83DcGte4vHn-HBYMu2H3Lfue_kLgtq09R9KfhgwSeaFiGc6qBxGkW3hBB0wRJahfhTU7natXjyx6jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=QBZPPdyzcmvtjAqh1_amHegMrOmFLINt09ho9gyLy00uW-bGbV8I9GhPYDSkfooxkA_uwTfPEyy7TYTYRm1FiSmMgktpi0svRhjEor8t1H9ZnTKqws31OhXKsddblhYSNabTQCjunyDUQDT_twTWPJMExaBU97E_eKyDjDqvBxVf10YTsEPrrmgZqTCYwd5iYtVT-pRU-ipfWEoYqTqc44y9z-t_rRWtcSiW9OxZfqm8xCyOBBcDkJu5YiSO7JwXDpmFjD2a83DcGte4vHn-HBYMu2H3Lfue_kLgtq09R9KfhgwSeaFiGc6qBxGkW3hBB0wRJahfhTU7natXjyx6jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇳
دیروز تو دیدار پزشکیان و نخست وزیر هند، مسئولین به پزشکیان میگن پروتکل رو رعایت کن؛
🇮🇷
پزشکیان میگه :
بابا ول کن این پروتلکو
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70929" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T1VO2q_N9VPqvkgo_c_9ZDCltHm60-RKz31WDfPNoAfYSzpBr1DX7IJGsMzcefaMNcJ6upqlPJhNeJObkoqX25SD_nfSbEZPSEpMSBpkYSyQ5kIwuyn3hig9epI5lZnN4GHruxN82WfheiPLtp7X-1Wi5HDMhRSLBPI_5-1Iwrb0hSKwH6eV3ucggbhMg2jKBwnJfSdyfqBuAJKgos2SOJzACfQ62Q5h55aqYeKhm6HtFZ0ojtpbWhlZzZM5CwAx4HGQywKoRrLypBYge_1qHr1icAlJGv0Kt4W_RP_XhaHKCdA2BjslXD-aj863woQAvDwMeCSbBAmnD4Xv8-hXYY8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T1VO2q_N9VPqvkgo_c_9ZDCltHm60-RKz31WDfPNoAfYSzpBr1DX7IJGsMzcefaMNcJ6upqlPJhNeJObkoqX25SD_nfSbEZPSEpMSBpkYSyQ5kIwuyn3hig9epI5lZnN4GHruxN82WfheiPLtp7X-1Wi5HDMhRSLBPI_5-1Iwrb0hSKwH6eV3ucggbhMg2jKBwnJfSdyfqBuAJKgos2SOJzACfQ62Q5h55aqYeKhm6HtFZ0ojtpbWhlZzZM5CwAx4HGQywKoRrLypBYge_1qHr1icAlJGv0Kt4W_RP_XhaHKCdA2BjslXD-aj863woQAvDwMeCSbBAmnD4Xv8-hXYY8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
بسنت درباره ایران:
ما داریم سرِ مارِ ایران را زیر خاک می‌کنیم. این مار هنوز نمی‌داند که مرده است، اما وقتی خورشید غروب کند، دیگر تکان نخواهد خورد.
کارِ رژیم ایران تمام است.
و آن‌ها هم متوجه این موضوع خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70928" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgVR8Jzfkip6_lRtVOG3VfTPi0ca2I3w2rkbgyRtJDRSrpSZ5Ut82Cq3AojVhVoxA_8OgitUX434vhPOguNenkkhQH9o394rkS-KmAPperR5lvM5f7qRQISvtayc8mADEBgvGWAEATunTwkWaLMqLinOSgT0eu6S3zAafMiSxgbMXsSOgUNBI6MyDu2f9tYF3oarjGwMu9mG8lNzpmVdF8wPg2tpYhKiuUqbYYITQpTuiDSXBQ10EltpWEEPfDZV4wmZCf-HmeAqhoUOwC8mUHFTMmewOS5iaPeHomfdDs3ylwdlO6n5lu5RMUsROCmplP3a8bnzgxPygiEfaQs1RSDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgVR8Jzfkip6_lRtVOG3VfTPi0ca2I3w2rkbgyRtJDRSrpSZ5Ut82Cq3AojVhVoxA_8OgitUX434vhPOguNenkkhQH9o394rkS-KmAPperR5lvM5f7qRQISvtayc8mADEBgvGWAEATunTwkWaLMqLinOSgT0eu6S3zAafMiSxgbMXsSOgUNBI6MyDu2f9tYF3oarjGwMu9mG8lNzpmVdF8wPg2tpYhKiuUqbYYITQpTuiDSXBQ10EltpWEEPfDZV4wmZCf-HmeAqhoUOwC8mUHFTMmewOS5iaPeHomfdDs3ylwdlO6n5lu5RMUsROCmplP3a8bnzgxPygiEfaQs1RSDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت درباره ایران:
ترامپ می‌خواهد یک‌بار برای همیشه به این وضعیت پایان دهد.
مردم ایران ملتی بزرگ هستند و این فرصت را دارند که به نظام [بین‌الملل] بازگردند؛ آن‌ها تحت سرکوب قرار دارند.
نمی‌توان انتظار داشت که گروهی کوچک برای همیشه قدرت را در دست داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70927" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4sqSWtiPvqqAai1bvk9POl0qHVnELnsrIbAkeGcjq_SD_uuUcb6OTXIwRMNqrKIHRlx2sRZ-1rVZaKHL6NCUcivRHLJRC6SQT24rowtyY9kYGAvrL2ktOe7gCd_Vh297xsMu9gNMwJcQp3DIAINSOVivB80bs2NaQrOLQOxosfBMeie41L-S-_eWDsGSYD4wRlINgCk_xvJqi-jPEw6LC4I2mXU365RiRFX9lqIpkegEBuLG7313evkz9kRoAHA35UoYtdk6uX-Z73YPlAl6xKjy8qP8HHwTJjaJp3E9EbGh0griJcfy6OLNw5aB1PX-2Hh_KHz0xfPJYxglw5f3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
از زمان تشدید محاصره بنادر ایران، نیروهای آمریکایی مسیر ۸۴ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70926" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70925" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70925" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jS_2gT696TruZ4tVcF3IrhoLHelTq5PUx0OP4kaV0uVwoY02TqCuLEKIyqs5wL0JAi8VwuvnrXK-7iNFA03XsPJ2inHYAloyMWsJ0ezt1I3tadqHAb2w4wAM-DHrz0lkQa1QX8SHngWRCf63rlJ-LP6DBPzqcsDuLI-O5ux63OJ5pvBfOC1UtvoeZJ-lI8KaLyWfPszXm8e9yn_LGrLhSz77NaIWJqfdka6ZnXxDecaGHNPbdaccDkq3vQdRDsPCnJrkd8hPN5Yq4jzPy7Tzb1FroSRztABhzZ-YZrYudGIeMGPVOdHKgPztJQk6p0GZdqfrk3I4NFXvtPG8CHvZYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70924" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=p9ZI3R8Ynxnx1m1TIgBB4RTt8cFl5v75OPt-BMOWmRj0NcEpG7nnNJJgTMg_jlJo3a5jIm093j8CDSn80QZPWqBHO5MunvnvvYL8RFm8yNZx5pFXVCRfzAveAS3jralm5-SAv9xZOkiY9ouiZin4S2Ph4NAL2CS-VFUwzMU6dKuPB-mohuojjEMXqaYkSdExVWM3sX_DGynFyY9w5V4oLe0QDHnkJ09NhWcYakHpnm6Uv3KpL2DBM4Sopjma--9t9tqeTEiudap2TeRRB89ZRv6zs6nMn3VMreSUN9plUQQ0_0eHR4sBi7OkOb8UJtL64bMFT9rgyzEBXg4gYj3WUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=p9ZI3R8Ynxnx1m1TIgBB4RTt8cFl5v75OPt-BMOWmRj0NcEpG7nnNJJgTMg_jlJo3a5jIm093j8CDSn80QZPWqBHO5MunvnvvYL8RFm8yNZx5pFXVCRfzAveAS3jralm5-SAv9xZOkiY9ouiZin4S2Ph4NAL2CS-VFUwzMU6dKuPB-mohuojjEMXqaYkSdExVWM3sX_DGynFyY9w5V4oLe0QDHnkJ09NhWcYakHpnm6Uv3KpL2DBM4Sopjma--9t9tqeTEiudap2TeRRB89ZRv6zs6nMn3VMreSUN9plUQQ0_0eHR4sBi7OkOb8UJtL64bMFT9rgyzEBXg4gYj3WUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت وزیر خزانه‌داری آمریکا:
می‌بینیم که — باورکردنی نیست — این رژیم در کشوری که احتمالاً سومین ذخایر بزرگ انرژی جهان را دارد... بنزین وارد می‌کند. بله، بنزین وارد می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70923" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=JDO-jeQZ6T4ykkAIUK1V6n-cPS8bsPORUL9C0Ku1vdlogHdsRzpHUmU0UoWJCEt9Mj9MlL7yCELDQD7B5FW3VoxFmODsNchHVUm47vhuLRwOkBzmZeXYEjqarVGMRul0CSNMT_OARcbdy-5T5drRRP3LAo3N6VSeyuTG8mQ67EKKD-0r--mDclyseVSc0vQTUKQocb9QZ5HOcIFLraHy1DnSTLg5nZo59T2U0-YZ04WDPxtdvh1wAeujou9zjonHkSKOBti76PgbVJJ00wwhgfsyHDT7QrxS9KORSRIoCjZVMY5VKieH2zBfq1QPh_GunnFhgGxWrX6J5mjn0HnP2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=JDO-jeQZ6T4ykkAIUK1V6n-cPS8bsPORUL9C0Ku1vdlogHdsRzpHUmU0UoWJCEt9Mj9MlL7yCELDQD7B5FW3VoxFmODsNchHVUm47vhuLRwOkBzmZeXYEjqarVGMRul0CSNMT_OARcbdy-5T5drRRP3LAo3N6VSeyuTG8mQ67EKKD-0r--mDclyseVSc0vQTUKQocb9QZ5HOcIFLraHy1DnSTLg5nZo59T2U0-YZ04WDPxtdvh1wAeujou9zjonHkSKOBti76PgbVJJ00wwhgfsyHDT7QrxS9KORSRIoCjZVMY5VKieH2zBfq1QPh_GunnFhgGxWrX6J5mjn0HnP2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
متأسفانه شعبه‌ای از یک بانک مصری در دبی وجود داشت که بیش از ۱.۸ میلیارد دلار را به سوی رژیم سرازیر کرده بود.
ما از اختیارات قانونیِ «قانون میهن‌پرستی» (Patriot Act) — که پیش‌تر از آن استفاده نکرده بودیم — بهره بردیم و در حال تعطیل کردن فعالیت‌های آن شعبه هستیم.
ما آن‌ها را مستقیماً تحریم نکردیم، زیرا نمی‌خواستیم کار به بانک مادر در مصر کشیده شود؛ اما همه باید بدانند که ما هویت آن‌ها را می‌شناسیم و خودشان هم می‌دانند که چه کسانی هستند.
احتمالاً همین هفته تحریم‌هایی را علیه یک بانک اعلام خواهیم کرد و هفته بعد نیز تحریم دیگری را اعلام می‌کنیم.
ما با متحدانمان در اینجا در حال گفتگو هستیم؛ آن‌ها همگی پای کار آمده‌اند و شاهد حمایت‌های گسترده‌ای بوده‌ایم — چه از سوی اتحادیه اروپا، بانک مرکزی اروپا، بریتانیا، امارات متحده عربی و چه از جانب بحرین.
ما قصد داریم این رژیم را از نظر اقتصادی خفه کنیم.
و همان‌طور که رئیس‌جمهور ترامپ گفت، دلیل بی‌نتیجه ماندن آن تفاهم‌نامه (MoU) این بود که آن‌ها آمادگی دستیابی به توافق را نداشتند.
وظیفه من این است که اطمینان حاصل کنم آن‌ها خواهان توافق باشند؛ و قطعاً هم خواهان آن خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70922" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=hFrbH1BA08UHAel2iMDTtVNjcv5kCeS9QywrvVKGUGxqoeIeMoUWKvopXUOpv-LDfLJk6eaHSD0GhLjjGalqO_sa2Dsa8YBlMQ80zpgX_37U1g-7L66MpwJaatTJCXeKIGj6df8hqpJgL6WtsFARnVQK1bbuuoHW1gC2mSG9K7Mr4p5B47dBZyuElfLqiDXlOv_wxUjr2DHExO-Ptd9fxK7lVWR72U_hR4-1mryfwCbiQDcxDvNKcBksJgXJDuJxXSmzBz0cl_L3ciPpGWvI_DqgxUeulwF_SAWZaL4_vg42hZRnOXg5nHxOaLOpJulaOpJKlxusxbv45d54TfQ82w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=hFrbH1BA08UHAel2iMDTtVNjcv5kCeS9QywrvVKGUGxqoeIeMoUWKvopXUOpv-LDfLJk6eaHSD0GhLjjGalqO_sa2Dsa8YBlMQ80zpgX_37U1g-7L66MpwJaatTJCXeKIGj6df8hqpJgL6WtsFARnVQK1bbuuoHW1gC2mSG9K7Mr4p5B47dBZyuElfLqiDXlOv_wxUjr2DHExO-Ptd9fxK7lVWR72U_hR4-1mryfwCbiQDcxDvNKcBksJgXJDuJxXSmzBz0cl_L3ciPpGWvI_DqgxUeulwF_SAWZaL4_vg42hZRnOXg5nHxOaLOpJulaOpJKlxusxbv45d54TfQ82w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
آمریکا قصد دارد با نقض تفاهم‌نامه، از مسیر جنوبی تنگه هرمز عبور کند و ما اجازه چنین کاری را نخواهیم داد.
پیش از جنگ، روزانه دست‌کم ۱۲۰ کشتی از تنگه هرمز عبور می‌کردند.
حتی اگر اکنون یک یا دو کشتی موفق به عبور از تنگه شوند، این وضعیت به هیچ‌وجه با شرایط پیش از جنگ قابل مقایسه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70921" target="_blank">📅 17:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
ما در ۱۵ ماه گذشته، در حوزه نظامی به اندازه یک دهه پیشرفت داشته‌ایم.
در هر دوره از درگیری، عملکرد و نحوه نبرد ما نسبت به دوره‌های پیشین بهتر بوده است.
نیروهای مسلح در هر دو حوزه توانمندی‌های تهاجمی و تدافعی، به مؤثرترین شکل ممکن در حال بازسازی و تقویت هستند.
این اقدامات مرهون آن است که فناوری ما بومی است و جوانانمان این کار را انجام می‌دهند؛ از این رو، نیازی به روی آوردن به دشمن نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70920" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=uLvt1XKmRsmq81z60dIQrauagOR8oRKBGUb4ua85jJCkRYb3BK22BixvR8szY5nGQ8hMvA68qPn6yd2gjwfgs2qK-bPcPU_6HNKqYdqgwoS_nBFVGYvWk5HRed0r565Eqt_8DhBa44qTmWJk6gavRV6aUjLCrNy0L0Rhge_CCRplxq7e2psP_vhMvwhQfnDJxsmKqKs7rvz7nfKXmrzJSK6PdcsB6gIWnqxjMltzyHIv_Zw49Pt3fDOtnfO9HCvBPzyDcisCMfktvKdQVG_gxqecZBtJVFDTfI1L1JNyygX6jo2Yv4uGtDsp_QRwvupDViCJl1C88_LFgcq8E0ybqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=uLvt1XKmRsmq81z60dIQrauagOR8oRKBGUb4ua85jJCkRYb3BK22BixvR8szY5nGQ8hMvA68qPn6yd2gjwfgs2qK-bPcPU_6HNKqYdqgwoS_nBFVGYvWk5HRed0r565Eqt_8DhBa44qTmWJk6gavRV6aUjLCrNy0L0Rhge_CCRplxq7e2psP_vhMvwhQfnDJxsmKqKs7rvz7nfKXmrzJSK6PdcsB6gIWnqxjMltzyHIv_Zw49Pt3fDOtnfO9HCvBPzyDcisCMfktvKdQVG_gxqecZBtJVFDTfI1L1JNyygX6jo2Yv4uGtDsp_QRwvupDViCJl1C88_LFgcq8E0ybqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خانم بخاطر اینکه شوهرش دائم بهش اسپنک میزده، ماهیتابه می‌بنده دور باسنش تا این دفعه شوهرش ادب بشه!
اما همچین صحنه‌ای رقم میخوره و یه شاهکار خلق میشه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70919" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f47777b.mp4?token=n-1wo6YCpI9r9WnFAebcDgKQ5tmn-xtQIigZmDpAgvRH-cT3hZXqE557jqTA7ImHeeg-FZ6B8Ewzad2PMgwIZOrGCC21C016-Zp7STgeIVyATuPkl-6FdwHTt5pCQmRJegpBnw3ot8LR-UAD_ass2mUIbcEDbpOwUEkYFCngAg5pnbcmqVeepzU98PVsWMUqKxLE7zcb44UFYogVEDvsCo3jUuDOphSYB_L2CViRtznZAQZ7Xr-gAym6SgLY6xIcuEm-Y76O4FKvJzZ-hXcGcXqyJhTN5DhoIJPgvb5-uQ0C3ZuXiQlUy2P0vRLMiw9QyF3saPrshk0Lm7Qb1lEhNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f47777b.mp4?token=n-1wo6YCpI9r9WnFAebcDgKQ5tmn-xtQIigZmDpAgvRH-cT3hZXqE557jqTA7ImHeeg-FZ6B8Ewzad2PMgwIZOrGCC21C016-Zp7STgeIVyATuPkl-6FdwHTt5pCQmRJegpBnw3ot8LR-UAD_ass2mUIbcEDbpOwUEkYFCngAg5pnbcmqVeepzU98PVsWMUqKxLE7zcb44UFYogVEDvsCo3jUuDOphSYB_L2CViRtznZAQZ7Xr-gAym6SgLY6xIcuEm-Y76O4FKvJzZ-hXcGcXqyJhTN5DhoIJPgvb5-uQ0C3ZuXiQlUy2P0vRLMiw9QyF3saPrshk0Lm7Qb1lEhNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره اندام های تناسلی  حضرت آدم و حوا:
حضرت آدم وقتی اومد به زمین دید لای پاش یه گوشت اضافه هست و میخواست اونو بِبُره
چون حس میکرد بدرد نخوره و فقط تکون میخوره
که یهو حضرت حوا از آسمون ظاهر میشه به آدم میگه نکنه میخوای مارو بدبخت بیچاره کنی؟
حضرت حوا بهش میگه جریانو و اون منصرف میشه
آخرشم میگه حضرت آدم وقتی حوا رو دید اون گوشت دراز مانند لای پاش دید یهو تکون میخوره که فهمید نه مثل اینکه بدرد بخوره و منصرف شد از بریدنش
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70918" target="_blank">📅 16:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=JnXQoBrRzmVtxp_W9tQa9kriTlgLCgV0ZRFUYhdNbbYPB3H4aEFeqaWpiVtBCF-qjsG-gWH8lQfRz83tcMb08kFxmHCxgPM8JGpsjOc8JcMPKg1zyUijxSqZGVlC_J6rIX9x6YlMkCjIC45kxq1k4iGAJSX-WYh0vF_YhnjxmY1iMkey1PLfiB9RxDsEuAu3Zi-BP82T1qGLI_DXD4RpLfztqq3F85XIAr8I6qFypXRVzPKA2li2uYdiDILfXh3rIiqCqsu2n480RllRYPTwWjrQnQvzA9VDSgaBQ3QK3jVY93DjRghtUQvhE1HEdP4WhipC2ifl6lFKXDEbGUu6pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=JnXQoBrRzmVtxp_W9tQa9kriTlgLCgV0ZRFUYhdNbbYPB3H4aEFeqaWpiVtBCF-qjsG-gWH8lQfRz83tcMb08kFxmHCxgPM8JGpsjOc8JcMPKg1zyUijxSqZGVlC_J6rIX9x6YlMkCjIC45kxq1k4iGAJSX-WYh0vF_YhnjxmY1iMkey1PLfiB9RxDsEuAu3Zi-BP82T1qGLI_DXD4RpLfztqq3F85XIAr8I6qFypXRVzPKA2li2uYdiDILfXh3rIiqCqsu2n480RllRYPTwWjrQnQvzA9VDSgaBQ3QK3jVY93DjRghtUQvhE1HEdP4WhipC2ifl6lFKXDEbGUu6pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر روز عجیب تر از دیروز
😳
جدیدا یه عده میرن به این شکلی که می‌بینید، یه مداد دستشون میگیرن، رو زمین میخوابن، میچرخن و نقاشی میکشن!
اسمشم گذاشتن " نقاشی با بدن..."
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70917" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=L2fOfIBPOVTNRDy7a_5xPBBbRjR4m0t662l8O6YEpqZvpVd3puxLPUM1eRSQLcpSunMgQyLeN6mbtcLVtaOHvO5vwWmwvgQ9swhQhHOW8Vu1ZqwX_wLLAozUWkyTQXrWBC_ZUqxcmlcWQJM1FTSOxPdtWoVeoggG9ZL2HRuKFHHYyZWXCD9xQNClWGHN7MtTcHvlIOMh16_GAi_nNkfOTkAoUbSRZI23IgYi9pfaKCyjhmmPo5CT1OMnDYvOEJapcH3QydobMjd0lXvwDk3l6c9w0Ate-FwJcUdRK3i60N-LAVEdBQhbjCJIffU_-kJIFgY3w2Nc9PMoTz0qUuM2wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=L2fOfIBPOVTNRDy7a_5xPBBbRjR4m0t662l8O6YEpqZvpVd3puxLPUM1eRSQLcpSunMgQyLeN6mbtcLVtaOHvO5vwWmwvgQ9swhQhHOW8Vu1ZqwX_wLLAozUWkyTQXrWBC_ZUqxcmlcWQJM1FTSOxPdtWoVeoggG9ZL2HRuKFHHYyZWXCD9xQNClWGHN7MtTcHvlIOMh16_GAi_nNkfOTkAoUbSRZI23IgYi9pfaKCyjhmmPo5CT1OMnDYvOEJapcH3QydobMjd0lXvwDk3l6c9w0Ate-FwJcUdRK3i60N-LAVEdBQhbjCJIffU_-kJIFgY3w2Nc9PMoTz0qUuM2wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⏺
فرماندار ماکو:
آیا دولت مقصر گرونی هست؟؟؟ خیر ما مردم مقصریم باید به خودمون رحم بکنیم
قیمت ها خیابون به خیابون فرق میکنه تقصیر ملت هست که تو ذهن هاشون فکر بدی دارن
یه عده گوشی و قلم گرفتن بر علیه دولت مینویسن نه آقا ملت به خودش رحم نمیکنه و خودمون باعث گرونی هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70916" target="_blank">📅 15:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70913">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ti5e8J-HP2thW1DFaKV8mej9UaK7YS8dYV_1iqAdxrxEahuq13Z_dkMn79P5iCi8GZIWDXGA5heHa18CscJbXIZ8J5rdzaa6tJxTW1uhe6ZyCvXKNryiWSUgWNZTebgZiw5CvfGhLCosFsGHLPO_Hdb2itxZ19RxWVitb2gjFMCNPqYjJhh0XSC_njt20LA5oX7bfa3-u1apZO8W6xWkVkuupYTPOnMGHfCRb8TVkBjj0b0DYlpQ47Bgf8zqB0g8UpBVxmoOY_1WW2rqpCyl_DNZVbYaU5rj41z4p5mfNykSuR3K0OIhCn2RDFVWG1NwjuKbIHtzBo4cYbrTk6vy2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AYiyjxUP1tw_s_L-hyjILEiDOfCZzPA2PaHWvmMtt-GlNpcAG_VjydBufR4LXs9wKEjiBMIyGcPHGWkjq7vUqgPt1Juq3E-6SuOZWODSxOH2tUBOqAOAtOgzusuOhFApi3B7dcAB1YmcydT7FbAXZSpFVD8iFoprR9K4Thi4hpKboUU8KZqkOGc9j1u8aR6SMaffKrXAuOtvJig0VwTd_ROEBFPGfiJkL0h8cfg1awsl-QTuTaW-cKFKYuOMhgJokV3LcioHk7bo5l4JVlx6g-8KQJiAOf6J6-0DWzZvYk49XCex_qCihUPGkoH8vrOojWSEJQ4YSBCzEuoJuv6g1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f05211278.mp4?token=NoRFa50u8oxPKbk_bu-bZiQEMfJoml3kFklXmI8v25mDpFLVLpVCf6CeU26DuitP0Kt8kcu-zpcb2JcCmaCqa6z96q5zNcO7E69bQv0dZcgsRII7v6Dc_xVAXtQwvD5t0bfZwe0IO6HQl8GNYXW_fYi3UZm_VP18g4LrfdWmeOgMF3R2P9cY1Z9sIu2hme81w9t6rus4ebgyvS8uBTI7NemTMv5HfbBg4zPoRy-9yRVm0L-uJW-mAUzgPlJU0pHy-7OI8K4qNRxHCvqxZw0z8zU-_17BdYcwF9SpKlqcgj1JIDO_OBDsMXRJwbg6DKIEnic0MtrE6-o0YHCd8lPiOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f05211278.mp4?token=NoRFa50u8oxPKbk_bu-bZiQEMfJoml3kFklXmI8v25mDpFLVLpVCf6CeU26DuitP0Kt8kcu-zpcb2JcCmaCqa6z96q5zNcO7E69bQv0dZcgsRII7v6Dc_xVAXtQwvD5t0bfZwe0IO6HQl8GNYXW_fYi3UZm_VP18g4LrfdWmeOgMF3R2P9cY1Z9sIu2hme81w9t6rus4ebgyvS8uBTI7NemTMv5HfbBg4zPoRy-9yRVm0L-uJW-mAUzgPlJU0pHy-7OI8K4qNRxHCvqxZw0z8zU-_17BdYcwF9SpKlqcgj1JIDO_OBDsMXRJwbg6DKIEnic0MtrE6-o0YHCd8lPiOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ز غوغای جهان فارغ!
شمال تهران
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70913" target="_blank">📅 15:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70912">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983da46010.mp4?token=fLmWKYzZvLKyDpym4H7UP8pX9JzNQ3KtXC5fOMkG73vO6YmrYE6rlP7smo5A96i46OPqjSETFMmB4WKBNiG9vDSHhsD-eWaHEXuVXRZ_2c0OnrFQnPvhUL8ancwNo-mTGky7i5N9ndSqAJ5FlokO9XXKfXi0e1Bd_mSgApuJN7JCvNGfp-wAKbVqdvDNDx0E61la1Z7vD6ScaEuz5rWPis2VlXJdRfgeH7Xy1XbLsVHwJWiN1oK6g6ObeA4iHzKOk19G9pF9NXS4kDbJOIdfK_-3RTBgIjqH3x2oLsRXOqNEu1H5hJP_ObzUk_SQvem0zcOThWQsoZtauArYhutadj7Q_vQ2ewC5De4OJa4VORg4Fi9O44W1p1skTTqoLFlo2EJAsS--Q-5rbKeQTqEFyluO-CQDucLyJKmN0mNnqtHMZlCe6qNql0wdiThuUd-4TS1vITXGgtHMI81M3LVTow3OjiZMB4hgjb2Qh27X3RbLRd4MMorz4UrcPCXs9LlbRXaEEtx8-4OMgyP6D7y3kFHxlzoh6acdf8En8OHLqE7IrBlyNvI8zlndMhpexfTWPtEf-vSl-4RiyAXv6NQR2-kwuPfH5TAWjRFum8ZApLImyc3jXufbEyyuIxHDW1FF7va1L3Gmxar-DYEK4CJljlg8p71Y4OIZlL-mPBsa6fk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983da46010.mp4?token=fLmWKYzZvLKyDpym4H7UP8pX9JzNQ3KtXC5fOMkG73vO6YmrYE6rlP7smo5A96i46OPqjSETFMmB4WKBNiG9vDSHhsD-eWaHEXuVXRZ_2c0OnrFQnPvhUL8ancwNo-mTGky7i5N9ndSqAJ5FlokO9XXKfXi0e1Bd_mSgApuJN7JCvNGfp-wAKbVqdvDNDx0E61la1Z7vD6ScaEuz5rWPis2VlXJdRfgeH7Xy1XbLsVHwJWiN1oK6g6ObeA4iHzKOk19G9pF9NXS4kDbJOIdfK_-3RTBgIjqH3x2oLsRXOqNEu1H5hJP_ObzUk_SQvem0zcOThWQsoZtauArYhutadj7Q_vQ2ewC5De4OJa4VORg4Fi9O44W1p1skTTqoLFlo2EJAsS--Q-5rbKeQTqEFyluO-CQDucLyJKmN0mNnqtHMZlCe6qNql0wdiThuUd-4TS1vITXGgtHMI81M3LVTow3OjiZMB4hgjb2Qh27X3RbLRd4MMorz4UrcPCXs9LlbRXaEEtx8-4OMgyP6D7y3kFHxlzoh6acdf8En8OHLqE7IrBlyNvI8zlndMhpexfTWPtEf-vSl-4RiyAXv6NQR2-kwuPfH5TAWjRFum8ZApLImyc3jXufbEyyuIxHDW1FF7va1L3Gmxar-DYEK4CJljlg8p71Y4OIZlL-mPBsa6fk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
اژه‌ای، رئیس قوه قضاییه:جمهوری اسلامی از هر وقت دیگه‌ای، بیشتر آماده‌ست!
کسایی که تو ایران هستن، همگی درمورد امنیت ایران یک‌صدا هستن.
اگه باز محاسبه غلطی بخوان بکنن که آشوبی یا اغتشاشی تو‌ ایران راه بندازن، مطمئن باشن که پاسخ نیروهای انتظامی، امنیتی، اطلاعاتی و قوه‌قضائیه از قبل هم قاطع‌تر خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70912" target="_blank">📅 14:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70911">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjI2_ZGubSUk0NBG8KY2tj1nyHwsEe5oa_I-Ec1SO_6qa4-BpmmF2iGlJfIY3uE3FMT5gV2xxIyI43Il7SiDCc0wgK7OHKysEAG5_Nb-4Byfiv_pBdOzVM-fXpXXvME9mQnRzJok9_zj9gnJzaABh78jRvw-BGsdeg2jfREWlsNGYmTZAtZ7TJcL04wafNieop7X-o_wi5_k08a7vrCqYrcj5KPtFVieoETd_Eck3J4R_e7edcOt5jm19fRiiHMTga9hiaKMIyWu1xvhmqDZPQFi5T9-oqT9Gt2-4nq2YGuwDliRyeKcnD16WdSVVKR5oi7ldWUeO8tcIP8ig7t6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
ترامپ یک مطلب از Breitbart News را در تروث سوشال بازنشر کرد.
⏺
تیتر مطلب؛
ترامپ پس از نخستین تبادل آتش با ایران طی هفته‌های اخیر، وعده داد که «سخت» پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70911" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70910">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=aOjunD4L-NeDllsX82lYkxVoCgZM1XJKloJMBDDMKulb-KnDecxk357DQjRfV07azYbpWY87-IJ0aIbsbeXMtgM3I-UMP8wvT3jgnZbFB-rXgoZx85ByBbQ-75quKv8WC36t7Zsg68q1LwNebbmLjWiVMfK4L7KDOksVN5ymYH67DP2pMwkD8qi4upa0ZHYwoXYjCUX_a4kv-yhgOh1QCR8vozgybBGbyx-u51ddUBMMOgOxRqBF-U-x6UzDwu85KrSoJxCB981UPvCSSfls8ZKdUjDjCELXOO1-7DeWBSQ4yyegISEM1BMJdwB4CU006CeYcXNqz-D579y-T-s4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=aOjunD4L-NeDllsX82lYkxVoCgZM1XJKloJMBDDMKulb-KnDecxk357DQjRfV07azYbpWY87-IJ0aIbsbeXMtgM3I-UMP8wvT3jgnZbFB-rXgoZx85ByBbQ-75quKv8WC36t7Zsg68q1LwNebbmLjWiVMfK4L7KDOksVN5ymYH67DP2pMwkD8qi4upa0ZHYwoXYjCUX_a4kv-yhgOh1QCR8vozgybBGbyx-u51ddUBMMOgOxRqBF-U-x6UzDwu85KrSoJxCB981UPvCSSfls8ZKdUjDjCELXOO1-7DeWBSQ4yyegISEM1BMJdwB4CU006CeYcXNqz-D579y-T-s4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کسبه پاساژ پایتخت بورس کامپیوتر تهران می‌گویند مشتری نیست و سابقه نداشته که پاساژ تا این حد خلوت باشد. یکی از آنها صراحتا اشاره کرد، گرخیدیم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70910" target="_blank">📅 13:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70909">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=CIZBIwLcaVtp4zeozseA7Ae1cjkL0rFBJSRuneiLQjWeVpWVVcR22xoqRhvPzBw71rILKgzVyrdYYyv1eikjDY7MuWYZzRJz1XQp-IESKyRd7KEMpH23bk5HRVbJ1KD5Y1fZVW2mcozzX3GGu_bExS_NyHNjKA0XtWjo1xygqPrfmWq7jwQG0Jaq6jWYmIKQSoHrE11j7fM3-8WA8T3pYCuIz3WOBrHIZIbcsQa17E3m6j5-F0EpyxnAEc_sXu7VgF2eMp9q4srTnhZ0z13xixEG8R1cNknG4IOETQC28-5mS7-yXILdIwRajT0HRnm1-v9r-wg05_P4GOugPB00-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=CIZBIwLcaVtp4zeozseA7Ae1cjkL0rFBJSRuneiLQjWeVpWVVcR22xoqRhvPzBw71rILKgzVyrdYYyv1eikjDY7MuWYZzRJz1XQp-IESKyRd7KEMpH23bk5HRVbJ1KD5Y1fZVW2mcozzX3GGu_bExS_NyHNjKA0XtWjo1xygqPrfmWq7jwQG0Jaq6jWYmIKQSoHrE11j7fM3-8WA8T3pYCuIz3WOBrHIZIbcsQa17E3m6j5-F0EpyxnAEc_sXu7VgF2eMp9q4srTnhZ0z13xixEG8R1cNknG4IOETQC28-5mS7-yXILdIwRajT0HRnm1-v9r-wg05_P4GOugPB00-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از دندونپزشک‌ها میرن میپرسن کدوم کار زیبایی تو دندونپزشکی رو نمیذاری بچه خودت انجام بده؟
به طرز عجیبی تقریبا همشون میگن کامپوزیت و لمینیت!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70909" target="_blank">📅 12:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70908">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=KFLLB1xdjPDkTBqzFwuVTuMQYZRRKVNkWZjFEYiwZcQ33ZWSy8S1-ZkD6WLYknKMGX8IzBbdWDLkbvH7q9c6DECCIeeqhANwbrfWUuLHLEzwdYZ23_wY3vhySCi5DZmUpCkgRyNfzTmtF9D86FNN1XSXofa2uxJNVWRw8jTE7j06_RnWOy4fCPHVSdbuefqkzPcoQ9UwXbRflgnXpiK1o9urQQs5cEYbr6Btm8_FH1ji751WDvi0ksQHU5oK0V8Gipg7uhHKQfAttYpWl4oN30NkVhYcHUJIWVvFqr426aUBpPSHWzNOcxHL_0Eko6EFAAMKNPmNR1yXl1oLo7TlRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=KFLLB1xdjPDkTBqzFwuVTuMQYZRRKVNkWZjFEYiwZcQ33ZWSy8S1-ZkD6WLYknKMGX8IzBbdWDLkbvH7q9c6DECCIeeqhANwbrfWUuLHLEzwdYZ23_wY3vhySCi5DZmUpCkgRyNfzTmtF9D86FNN1XSXofa2uxJNVWRw8jTE7j06_RnWOy4fCPHVSdbuefqkzPcoQ9UwXbRflgnXpiK1o9urQQs5cEYbr6Btm8_FH1ji751WDvi0ksQHU5oK0V8Gipg7uhHKQfAttYpWl4oN30NkVhYcHUJIWVvFqr426aUBpPSHWzNOcxHL_0Eko6EFAAMKNPmNR1yXl1oLo7TlRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
غیرحضوری شدن مدارس امسال شایعه است؛ برنامه دولت به حضوری بودن مدارس است مگر اینکه اتفاقی بیافتد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70908" target="_blank">📅 12:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70907">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70907" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70906">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz0tFK1uTVv_SoJOyKRDZmHGCQJlP6sXdSCW09wHyd6WoJjwtw5Sbnyu1wKB4U711CBqib0IJ3LsBmDeomkv_r6TWWj7VO_oNqr7j3rA9wWKNpJ02axd1jLfbxhyHhYRQGckK5k3IsckaYT7kTlxH0PbkXZAO_mlTCRcr4c5Z5-bq5WVNYQs12LpL4XOiCWT5mkuLNZk-anQn8OLr9_1xrnjX51JU_Z2rHc5BVom7KrWaetf_oymOaO_PiXdFP-4XCa48tC9QMLy8qzS9DYCGaYBrEI-80GffDM70dhXNE_UElgkdmIhZWHzucHEK60HatOJoOdobbO8b4Ln5mTp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70906" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70905">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=gyfLAIUO9IQFc56XnhhUo9yBWIDRVCgnldr3RMsIcAfnzl4m0PwZB8-9wCTZjJVWecXSmJ_10X244h32MoAgCddXVqtiEGZpKUfDEXgYQEqpKC2mG_49YEViewFiOGNC3DtoIush9WIjRxm91XZ4R6TWzwney6dJPMw6Ncu70d6aW1qRQVsEp41hyWiMOCgvoT2MQ4UazOzrVflGWG3dxnYEh2Ek2Qgq-b4zYPUjz1Fu4A0OTZpyxkLIodhDeJxBIYe8c6as04m5tl0d8ejGEwebW39Yq2Sp-AJtdhXY-X-qtQaY0G5tDFEHOvDoMB-7Cq9ALLwSgumlJwE3ieizSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=gyfLAIUO9IQFc56XnhhUo9yBWIDRVCgnldr3RMsIcAfnzl4m0PwZB8-9wCTZjJVWecXSmJ_10X244h32MoAgCddXVqtiEGZpKUfDEXgYQEqpKC2mG_49YEViewFiOGNC3DtoIush9WIjRxm91XZ4R6TWzwney6dJPMw6Ncu70d6aW1qRQVsEp41hyWiMOCgvoT2MQ4UazOzrVflGWG3dxnYEh2Ek2Qgq-b4zYPUjz1Fu4A0OTZpyxkLIodhDeJxBIYe8c6as04m5tl0d8ejGEwebW39Yq2Sp-AJtdhXY-X-qtQaY0G5tDFEHOvDoMB-7Cq9ALLwSgumlJwE3ieizSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ترفند یه آقا برای فروش بیشتر:
برا اینکه فروشتون بیشتر بشه پای مشتری رو بخورید
😟
اگه پاشو نداد که بخوری بپرس ازش ببین کجا رو دوس داره بخور براش.
بازار خرابه مجبورش کنید اعتماد کنه بهتون.
بعد خوردن جنستو براش معرفی کن و اگه نخرید بازم براش بخورید.
بعد مشتری میگه هروقت بیام همیشه اینجوری سرویس میدی و اینجوریه که فروشتون میره بالا
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70905" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70904">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=YmeSWfqZh31hXp6F72shfejI3cM8ca9SmKXmEYF3vAAYI7w1zAc44RTnKzr8hEs57ciJGYZRI91bs1_HVlMbukR86O8PNd5Od9hMDjxHA1RmfPfC1NLbo5vjIhPBxqpFd5uvEll5icQJBWk9BPHpGNx1oYOcWWzZH4OJoGASX28HQ049RWPHMTCX3yMrx-_svNO-FWJkXBjMY1ZeCT6MrJyFDVRA9K7gmE5SVjrcMb4KkNUYIE4rkf7zZK6UdYyvWi9ls1KgArsd1ozd-aWki6Wdov6K7F1sgj7so7AvZ8y0hxpCktzeGxsVZO_jaP-mFQu_il21c4rSckcYQCMdAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=YmeSWfqZh31hXp6F72shfejI3cM8ca9SmKXmEYF3vAAYI7w1zAc44RTnKzr8hEs57ciJGYZRI91bs1_HVlMbukR86O8PNd5Od9hMDjxHA1RmfPfC1NLbo5vjIhPBxqpFd5uvEll5icQJBWk9BPHpGNx1oYOcWWzZH4OJoGASX28HQ049RWPHMTCX3yMrx-_svNO-FWJkXBjMY1ZeCT6MrJyFDVRA9K7gmE5SVjrcMb4KkNUYIE4rkf7zZK6UdYyvWi9ls1KgArsd1ozd-aWki6Wdov6K7F1sgj7so7AvZ8y0hxpCktzeGxsVZO_jaP-mFQu_il21c4rSckcYQCMdAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بسنت، وزیر خزانه‌داری آمریکا:
تنها چیزی که برای رهبرانِ ایران مهمه اینه که سرشون به گردنشون چسبیده بمونه [ زنده بمونن ].
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70904" target="_blank">📅 11:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70903">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=a4XfO5SXrDbEmYLZC4wVJh3jJTHkDtAqNOwz4IqLYeKth107SAxIwTgGMlTjkxq3eDSUuTe_T-GACf_z3U55h3qp3CEV0XBjcJomPWBx45lHJ9X5Q65H5qTAlXVpxQ70oZwFdMAb9nusqOYIpQssM5pTbYnYjfAF_IAnh6GuDjrS8qOlXpDX-O9n27gkumzHolneVhGFPqmC1bmngHnLzRu0WcwRFEuxmyWHmwaMGV_2E_ZDEdXualZpSCHQc0HlbxKNxuII9YImW0AFJms_gnjjGvAFX4-tUbXQ6Jc8rOurOFKaUjtU5juTEzBxGtk8q3jY3FS3tsT-iVbRKKYF5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=a4XfO5SXrDbEmYLZC4wVJh3jJTHkDtAqNOwz4IqLYeKth107SAxIwTgGMlTjkxq3eDSUuTe_T-GACf_z3U55h3qp3CEV0XBjcJomPWBx45lHJ9X5Q65H5qTAlXVpxQ70oZwFdMAb9nusqOYIpQssM5pTbYnYjfAF_IAnh6GuDjrS8qOlXpDX-O9n27gkumzHolneVhGFPqmC1bmngHnLzRu0WcwRFEuxmyWHmwaMGV_2E_ZDEdXualZpSCHQc0HlbxKNxuII9YImW0AFJms_gnjjGvAFX4-tUbXQ6Jc8rOurOFKaUjtU5juTEzBxGtk8q3jY3FS3tsT-iVbRKKYF5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حمید رسایی:
هم‌راستایی من با اسرائیل در مسائل مهم کشور(جنگ و مذاکره) مثل داستان دویدن یوسف و زلیخا به سمت در است.
زلیخا برای گناه می‌دوید، یوسف برای دوری از گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70903" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70902">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=WP8zlTpenJLavJGNAHjEMLF405tPWxTjWa0fa5ii39tdoZAja2ne6OBAEm7_6L9cKNfUqlCd7zzOhFq-w44khzGmYYzynnZQzUadnIw0v1BfyLXoRVFl8TzFYHIeHHeCKRTOcxj292PtmeyU_9hi9EzXspx6EqxiK_H9OfwZFeuHJIYdzKgyvnCQLTWU07DFP2fAvxTGkJWf-IpmJdg9pdfLV3YqbtujRu6l0Lq85BvJ9SLGfuvKLW59ELrLXroVN6c9EZ58xBm3sEaZUOnQnWgCOoa6ZMSC53izO-enQDdevROI-jqDtmmxe0lI62N7AJxrN76jKhKcv6s3ER3q3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=WP8zlTpenJLavJGNAHjEMLF405tPWxTjWa0fa5ii39tdoZAja2ne6OBAEm7_6L9cKNfUqlCd7zzOhFq-w44khzGmYYzynnZQzUadnIw0v1BfyLXoRVFl8TzFYHIeHHeCKRTOcxj292PtmeyU_9hi9EzXspx6EqxiK_H9OfwZFeuHJIYdzKgyvnCQLTWU07DFP2fAvxTGkJWf-IpmJdg9pdfLV3YqbtujRu6l0Lq85BvJ9SLGfuvKLW59ELrLXroVN6c9EZ58xBm3sEaZUOnQnWgCOoa6ZMSC53izO-enQDdevROI-jqDtmmxe0lI62N7AJxrN76jKhKcv6s3ER3q3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجددا در سراسر کشور، حجاب‌بان و گشت ارشاد راه اندازی شده، توی بازار تهران حجاب‌بان گذاشتن و هر کس بی‌حجاب باشه، بهش گیر میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70902" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70901">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=uLazzb_ousOg404oxQzHjiTn_sN5-2x8fCzLrEvpPPVxsEdZhD-ltVcfPb_POMRuoFVJHk_iIt_K5D0SgnpKqkjiZs7VAoSlBoyQFqCricBmmkLTTYLQOaXovfw3At_KClTzsamugvr9AVesHWpok7pe9IC6sx9pMd5LJ87lC9Vaw4YT-AYzrQXw8dLENkJupaZNEXk-bsorvRgOBhaePXEu0GbWJvd1zfG3jjSUdL_Yi-ZWtkJ2mYPni6DA6kqku0s458OfMuFkfO_ChuC01P5V-YsQDtBUmS7W29l6wgl4Zp8GkdN9-jCaTQI6tNpnQD2JqN95zmU3aLwIa4BP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=uLazzb_ousOg404oxQzHjiTn_sN5-2x8fCzLrEvpPPVxsEdZhD-ltVcfPb_POMRuoFVJHk_iIt_K5D0SgnpKqkjiZs7VAoSlBoyQFqCricBmmkLTTYLQOaXovfw3At_KClTzsamugvr9AVesHWpok7pe9IC6sx9pMd5LJ87lC9Vaw4YT-AYzrQXw8dLENkJupaZNEXk-bsorvRgOBhaePXEu0GbWJvd1zfG3jjSUdL_Yi-ZWtkJ2mYPni6DA6kqku0s458OfMuFkfO_ChuC01P5V-YsQDtBUmS7W29l6wgl4Zp8GkdN9-jCaTQI6tNpnQD2JqN95zmU3aLwIa4BP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر ماشینش رو داده بود دست دوس دخترش و داشت بهش آموزش میداد که این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70901" target="_blank">📅 10:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70900">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=YgrzL4C2rpTVYfkggM7zRRzAhwQf5axAVAqpgepeMyvIV2kr6mHXqqIywZ1dwBTfi48usgPsDr8Xk6G4LxwvuRQ_7V3cV7o9327_8EY8PVseFFiGd-IR9AuwVsg1aF4QNjvPRGhVST9he1Rx_enomBtlH-B8rVVygpiyfOp1Jhy5F0v9BWhCHeL4yy5uPYBplPCOKZ_GtKxZJ2A2e8eHR0e9_Rf6ojv7-n1AXA5HjCGtKtpPgzyt769OkItLvpFEnGKO_ygYz3n1DQkE-RnJdW9zTX1Qn4zoxVvnLjwPVVTwNq0exnjh7g_RGKnfxkyBXdRioJTO6c863UuBbzKHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=YgrzL4C2rpTVYfkggM7zRRzAhwQf5axAVAqpgepeMyvIV2kr6mHXqqIywZ1dwBTfi48usgPsDr8Xk6G4LxwvuRQ_7V3cV7o9327_8EY8PVseFFiGd-IR9AuwVsg1aF4QNjvPRGhVST9he1Rx_enomBtlH-B8rVVygpiyfOp1Jhy5F0v9BWhCHeL4yy5uPYBplPCOKZ_GtKxZJ2A2e8eHR0e9_Rf6ojv7-n1AXA5HjCGtKtpPgzyt769OkItLvpFEnGKO_ygYz3n1DQkE-RnJdW9zTX1Qn4zoxVvnLjwPVVTwNq0exnjh7g_RGKnfxkyBXdRioJTO6c863UuBbzKHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇳
خب، این آقا سانت رامپال، رهبر یه گروه تو هنده که پیروهاش اونو خدا می‌دونن
.
این آقا برای خودش یه اتاق شیشه‌ای مجهز به کولر درست کرده تا وقتی اعضای فرقه میان پیشش و پاش رو می‌بوسن، آقا گرمش نشه و عرق نکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70900" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
