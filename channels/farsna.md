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
<img src="https://cdn4.telesco.pe/file/ocKYKs9iU315xM4wHHhfrLd0x9QiDVbveYlc4rKECH2cyQFrKMZei-VrfsjIu9zBGsLRRsu2st9hFVm4B3G3I8sXOaHef5m589DIYK2f6JqgZmbvh8A6BStTM4RDG0gKDtv-CdnfnH1Va6WR_rEACpK4GZIkLiCQEbVb3eRRAbLw32RPXAV2PLqwWOQZjNUefb5thxw6XiKBc8yuWtlwUEf27RhReZEpAzO430V68zqevFBvOb7rPQbF2uNKb6m1gXiNSxdjEbiKgzaCvRHQDdRbBzzynNAUtPKVN1EoJ5hdGtsOA4OYS6RfA1kItNoAyaO2EbqDsSQPzxuePxI3Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-468471">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umYXyjpBQaCePeY2I64Jmu3ELs19jewm3bQYVQPa33K6reVbx3WpFUm9D704DzzPwrs_Ri12Cyh9RKYi_D-CsZUz53bqL6nnbWYW1Gi9dix131eAsD5dWk3wu27N7GWvh-PzbuQBqsLywNqVsLnHaInMKpzHS_ifCiYlMFUtnZ9mXUDV6-VkJzjzYf_sC5Orn5pS729sXXpQxuxZflnqoi4oP6x8jPtDcXn-8sELQY62E7rFISCetswq-41ig3aG5ilx4V67YuOyPSaKAwy_h1r2_xtLai_ZL1qMCbI6tocgby9wl1gIwu3bhwk2S8tPznV9-sH8Yd_iyZomxYqcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود سامانۀ بارشی به تهران از شنبه شب
🔹
هواشناسی استان تهران: از شنبه‌شب بانفوذ یک سامانه بارشی، به‌تدریج افزایش ابر در استان آغاز می‌شود و روز یکشنبه در مناطق شمالی تهران رگبار پراکنده مورد انتظار است.
🔹
برای روز جمعه افزایش نسبی دما، به‌ویژه در نیمه جنوبی و مناطق مرکزی استان، پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/468471" target="_blank">📅 21:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468468">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kE6XWPsXV4yThnDuR5iq-55Pf67L1kvp9Pqp5AlvuuesMgFfhfnAfJ8FPavsyVqUEnqvFoS0_bReaQe8ZenPVJhsCtkhEgYGtaGoKXrUyDzDT5FuN_Co-0AqbSHj2hBF6MUo0nU_OmIM2WIqjJEeI40Dgmr2fjGPFS4NDIGUfuicst0NdZ1qRAhjMlw_AW7t54mMdC7_j7U6q282-e1GuhVBXkIXIsP1Rpu5FU2C-XKKfgOtM-3TwE28EkPR324BvmQvVzy7Yafq-tXwn1swkVZtJ03fVZjRNSXro1F06wj47pLirvx9v3nZ4S5n3Wx6rJFCUKN17v6y6HvptEHqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4V4RTMn7mIAoINPKnhsGJXBjYvEjhsoAVwIPPz1a7nlqNe0M-4NiveLPqiNKWPwoDMWhWplwtGKfk8qCJn3XxMaAqSePprF0I1hk_YZWAQpKI7GcP0qwd55jU6yzQTig_aBN6zDfrC9tqqerfmtDVktUUtlkCLRyzzW_GjekSZ9UTfFiF-eZJJDGSllt1vcAUPvGsz0LDDKTDfeqiRUU_YJcL_M8TBzfb7sKwvbbCtCCiH-utcTkDoY4PjHuoLRcD84-v29vu_rgC3XNDJGv4n82IQJMbe0otZBJ2of5msIbeymZG4ZemXsgDyMkd4Iwo2QPCQOV14QB--zUtbGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gx8NiiKBfAbHUOuQ7kxkEYIiKICs1_Abi9g7_yZ0PlJaplmUeUTx1Ndi624vQ9-CKjUbLqKiyBATy31JMlt5E3wb0FRyI3we4e-Tga1QoNtfSb5oXgysqK9KWML8uZTz_Z_iP7aUwP3nomPTF_QSuKrRn5Ho_6B-5ev6fNqDUukGYNViFflzEIJXRoj4N-Ol8algZT2qOz4sN23FcTf3T5Cc7EhjgNPcP0sgGErfw3sztQBOp3OlF9cI28mLXTagagfLtvtjhfoa9a_2GwNH6uuvViLXXTYKNUOUdYtPu67ArsQ91bBVsGvdzyuFFCxfCWseRbh5RAdeA7rEkzUi8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
اخبار امیدآفرین ۲۴ ساعت گذشته را یک‌جا بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/468468" target="_blank">📅 21:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468467">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f06ced276.mp4?token=EKQ5mpOoux3ywWUiIixFXKhIQr_mkyY6e50ESLkGetRZPXpmxDlcVTpb2e7rNnCPe6Bm0by9_4-nbxJLhhq45R18uFvoY64o8F3FrAUJaapOLimP15LJQct4owpz9HAf6arTqilJeIE7_kzKXwe_l0H__qZ8kLA4ApZMK92HO1hnKOF-6ZmE3hXq19Ifwnd2mgVNFO4LTfnOyEGb4o6uMgjszlz5H-pqu-2JQ9FZhkjp1Y39izL97K62VQ2sV4rBXzvEBRGc4XSfiQf1j4QEIT2oQ_Neks_Nu4ZSz43n1bBMtd-PM-dFu8NvVuiLhEZp8Iobt8zAyvSDzJSSbsi_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f06ced276.mp4?token=EKQ5mpOoux3ywWUiIixFXKhIQr_mkyY6e50ESLkGetRZPXpmxDlcVTpb2e7rNnCPe6Bm0by9_4-nbxJLhhq45R18uFvoY64o8F3FrAUJaapOLimP15LJQct4owpz9HAf6arTqilJeIE7_kzKXwe_l0H__qZ8kLA4ApZMK92HO1hnKOF-6ZmE3hXq19Ifwnd2mgVNFO4LTfnOyEGb4o6uMgjszlz5H-pqu-2JQ9FZhkjp1Y39izL97K62VQ2sV4rBXzvEBRGc4XSfiQf1j4QEIT2oQ_Neks_Nu4ZSz43n1bBMtd-PM-dFu8NvVuiLhEZp8Iobt8zAyvSDzJSSbsi_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم از کالابرگ راضی‌اند؛ فروشندگان اما حرف‌های دیگری دارند
@Farsna</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/farsna/468467" target="_blank">📅 21:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468466">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4knki7JAv1GIRuUAa79yp0dVhW03Du18bc54ysIcp_HbwOCx1bowBjuBbIIScLAiDa_So7L5bnDzzEsy_7uXzWkdOxVlMbmZ1ivdP4Po6-8B7P_hr1jSRBZ3wxCkfTl-tXqLSc3TwhVQjYe1lK5mHm7JaHls7yLJ0tbVdCaaRspq5qB6NEkPfxNDeA6dNEJwjur5z2HGiwaz2UytaOaOL02H76x-SqR4KIb22_aoOcgwxx_rkftKpeQBb-u1Y9qhom4E8C4frbCj-ZA4xn6mcYTEW8qdtf4upxpJMtzK4iESfk0ZBsHvoG0i46-gFInZDqh2YIYboRJyMezwkEGEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: دولت متجاوز سعودی با حمله به بنادر یمن مسئول به‌خطر افتادن امنیت دریایی منطقه خواهد بود
🔹
سخنگوی نیروهای مسلح یمن: حملات هوایی و موشکی دشمن سعودی به جزیرۀ میون، خطوط کشتیرانی دریایی را به طور مستقیم تهدید می‌کند و ما، دولت سعودی متجاوز را مسئول هرگونه…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/farsna/468466" target="_blank">📅 21:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468465">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzGd7C6iySXUor3b6yQXzSFA-sXWhHyqLcSe4wk4uMGnDoIXhDh3w92cEdr3Z7Vlz0iPTisL6miZrJMcQHoLsXJe3m8JV-2XhDhQj6I13ilouvqwCGFgwX2Mox_Tz-YiLbSdF30IHCl9vJYyQvBj3QmbAfsVahKX8r1RXRGFyWpx3dyyBj0TerKEvzGwgdh8JNNaKkylw4mRI0CNZBM8PjB17NXv7RMhLJKheshrUCjDyXLJcRbXdtNwWt4pVCsR1We053CzMLsSs6u1gXTUBch3JyLYRqb0cYDKQH40IDX_-av4MVyXIHsieeduYl_iiK6MV_k5_vlNoQTrQ7EzuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: باید شرایط جنگ اقتصادی را به فرصتی برای حل مشکلات کشور و چالش های انباشته تبدیل کنیم
🔹
به تفرقه‌افکنی‌ها توجه نکنید و تمام ظرفیت خود را برای حل مشکلات مردم به کار بگیرید.
@Farsna</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/468465" target="_blank">📅 21:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed99beeb7b.mp4?token=Kcf3WMkQdSSUFzEm4B_z0rFZOAZRN8sUKQ9ILoT9zkQCokhhyJLBE7hChfgLS-C79xj3NnTqob8nDW-pxmRieg4JlK3Tci7nvrUlckZ2HNecd7u-PnT5XviiLdtfrulSnKyjqycWshUYoq7UPZkpl09nSeUfjWNEIENPiOYJ-UbZP21ejdZtnyyxOc7A2P4efpkzqKHryfHKQjjc9HCdPC8WWi6LBxqbOgrk_HX06OKMLQJCUg1diHWsZmzPotsx3xN4t4FrHCLn8u5qOQDkGnlnudTHB1tUD_I5HeBovWiJ84lfQkYnPT-oSTVE8xFB-8T1WaBQ5C2V4lcDRE3U3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed99beeb7b.mp4?token=Kcf3WMkQdSSUFzEm4B_z0rFZOAZRN8sUKQ9ILoT9zkQCokhhyJLBE7hChfgLS-C79xj3NnTqob8nDW-pxmRieg4JlK3Tci7nvrUlckZ2HNecd7u-PnT5XviiLdtfrulSnKyjqycWshUYoq7UPZkpl09nSeUfjWNEIENPiOYJ-UbZP21ejdZtnyyxOc7A2P4efpkzqKHryfHKQjjc9HCdPC8WWi6LBxqbOgrk_HX06OKMLQJCUg1diHWsZmzPotsx3xN4t4FrHCLn8u5qOQDkGnlnudTHB1tUD_I5HeBovWiJ84lfQkYnPT-oSTVE8xFB-8T1WaBQ5C2V4lcDRE3U3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جوانان ایرانی به گزافه‌گویی وزیر خارجه آمریکا اینگونه واکنش نشان دادند
@Farsna</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/468464" target="_blank">📅 21:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468463">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpjgA5Ir7DfF7P5VksKQUuNls0spGauSWfTeq3Bq2Lnln8rBTHVboeDSYVVGnz-yGn8AoZ1fmEu5783jwhOf_rVSitvQAXgDCEyA_3gsfKNtoHa1h9bak4z7B9eN-HIFFdgeo39s575XBwo-sUXDV758cbpjuwtVuERDQmjkD8rASDTcsLdtf8nhYoDvkXjVgJ3qVkK8jj85mCxVSI3jNbhUezKSPTultY_Ysag1iGp8TKl8IhfKP13bgrvL0SYs1MvvWSHPbpSIK9r1nB7tUFRfVJfthirUsTGIVb24-g1Z6PoRusLqSxp5-1ztH0k96pwHAi9exuTSINTMt7Y9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفر رئیس اف‌بی‌آی به روسیه پس‌از ۱۳ سال
🔹
رسانه آمریکایی ام‌اس‌نَو به نقل از منابع آگاه گزارش داد که رئیس اف‌بی‌آی کش پاتل برای انجام مذاکرات وارد روسیه شده است.
🔹
باتوجه به‌این‌که سازمان اف‌بی‌آی بر اجرای قانون در داخل آمریکا تمرکز دارد، این یک سفر غیرمعمول محسوب می‌شود و اولین سفر رئیس این نهاد به روسیه از سال ۲۰۱۳ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/farsna/468463" target="_blank">📅 21:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468462">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/447a4feeef.mp4?token=UCYElxRo-EIEzMli13waAvYDANw5M60dTh56UVtHW4noS0SeP_Y3i9bcPPK2M_sQp_1S7F-ewTSRP2oo3SV9TKuWFqRE_CL7yqUPoSeSqVY3TmnJ3JDuh4fvDAvoXV0Gft9ecfld8e7GVRmf4ddxi8bY_xJtfFd8Vh5i56adAvJ3AjExBZgKHgRYuE54akPdLI76KCjC2aoegkgW9GHdi8wEXltHG96YeBXAq8RlhSTxHnqA5EPn_K4aLaqBX4CNLYDizEi7_mxTmqJeebyUhj4eP9Kxw4EyyUwakyBjP-6RRi8MgfIdW6mWLRXLs8brWyrrhtM38X_CMaVa9xePc7r_ZLsGLCMszTNSpeWys-7OM4i7CUcRWLSaqJhyOrQ9gTBDunQZ1qzmhyZf3a8oliURNj-Kidg_FQZpFrtbsGpS-yI3W4mDqab8ZLV59pxCqbfRSAQ7IsVIdnhENiOcQuDAgiuZ_CfhFYPSwWTFFaq1sTIMgp7TEDCVFNwR1j_TakIar7Q9hjmy_PQtgZRM_M7m2-Vq-rQc3e4DP6wBogSrIuzZGXtXc2GQYm3uYix5eJwzXwisst4Y-wbUBg2_5fi0xbe1qOEsZsNTNGgsLYebei0_81J4UR76AKAeYPMzbqcD7PQ8AJAAvnVRrYEX8V67x11Uec_2em6XivW5erw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/447a4feeef.mp4?token=UCYElxRo-EIEzMli13waAvYDANw5M60dTh56UVtHW4noS0SeP_Y3i9bcPPK2M_sQp_1S7F-ewTSRP2oo3SV9TKuWFqRE_CL7yqUPoSeSqVY3TmnJ3JDuh4fvDAvoXV0Gft9ecfld8e7GVRmf4ddxi8bY_xJtfFd8Vh5i56adAvJ3AjExBZgKHgRYuE54akPdLI76KCjC2aoegkgW9GHdi8wEXltHG96YeBXAq8RlhSTxHnqA5EPn_K4aLaqBX4CNLYDizEi7_mxTmqJeebyUhj4eP9Kxw4EyyUwakyBjP-6RRi8MgfIdW6mWLRXLs8brWyrrhtM38X_CMaVa9xePc7r_ZLsGLCMszTNSpeWys-7OM4i7CUcRWLSaqJhyOrQ9gTBDunQZ1qzmhyZf3a8oliURNj-Kidg_FQZpFrtbsGpS-yI3W4mDqab8ZLV59pxCqbfRSAQ7IsVIdnhENiOcQuDAgiuZ_CfhFYPSwWTFFaq1sTIMgp7TEDCVFNwR1j_TakIar7Q9hjmy_PQtgZRM_M7m2-Vq-rQc3e4DP6wBogSrIuzZGXtXc2GQYm3uYix5eJwzXwisst4Y-wbUBg2_5fi0xbe1qOEsZsNTNGgsLYebei0_81J4UR76AKAeYPMzbqcD7PQ8AJAAvnVRrYEX8V67x11Uec_2em6XivW5erw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اراک شب‌ها با حضور گستردهٔ مردم، صحنه‌ای تماشایی خلق می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/468462" target="_blank">📅 20:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468461">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc0e3ef73.mp4?token=OzKj8Od8Ig8VuAYnU1UJe0j8fdlUTJqLYj6WxVjqpp-jaGD6T-wbxqXMBdIMbHMHltEA5vNNGyv4mB6pgE2FXjYggFkG_3AD1vdF-sp_PKBuLD8sfNfhXITi7p9CvtlTKlEHv--WyLaWMYIdctK0UbdWNAMvtgijz_jHE1Gf3rZvHSUZKPejuFThjKVRA_60UcQvrs-iOw7sQW33YYfqvx0jw1JwloOVMWIVFYEGdvjhl_wCdJVo5kbEavgQ5zQ-cEuYKPmosLZNdJn7h12bRVilhtbKUbLkd9CjMJ05LUE_uOoHpxBnkOxev-DZKbCAVbZo50wNaVSNZPieloSZig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc0e3ef73.mp4?token=OzKj8Od8Ig8VuAYnU1UJe0j8fdlUTJqLYj6WxVjqpp-jaGD6T-wbxqXMBdIMbHMHltEA5vNNGyv4mB6pgE2FXjYggFkG_3AD1vdF-sp_PKBuLD8sfNfhXITi7p9CvtlTKlEHv--WyLaWMYIdctK0UbdWNAMvtgijz_jHE1Gf3rZvHSUZKPejuFThjKVRA_60UcQvrs-iOw7sQW33YYfqvx0jw1JwloOVMWIVFYEGdvjhl_wCdJVo5kbEavgQ5zQ-cEuYKPmosLZNdJn7h12bRVilhtbKUbLkd9CjMJ05LUE_uOoHpxBnkOxev-DZKbCAVbZo50wNaVSNZPieloSZig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: برای رسیدن به هدف هم می‌جنگیم و هم مذاکره می‌کنیم
🔹
باید در زمان لازم با تمام توان بجنگیم و هروقت در میدان به پیروزی نظامی می‌رسیم باید عرصۀ پیروزی را در حوزۀ سیاسی تثبیت کنیم و امتیازات لازم را برای قوی‌شدن بگیریم.
🔹
منظور ما جنگ بی‌پایان و مذاکرۀ طولانی نیست. جنگ می‌کنیم تا دشمن را مستاصل کنیم تا مجبور شود به خواسته‌های ما تن دهد.
@Farsna</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/468461" target="_blank">📅 20:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468460">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmTESEkLYmVn-IO0Dud6PcnzmcuH2KyjjmytJ4dXMphnCwXeGlZk7GtchvbFxIUpK09O35vicgV2aZiW8ehGxYWrusPo2sAdlJ2eu9F9QPfJa8qwz-Hm2wukkMLZagYKQtsuYM9YQK0tRlcIm3SBxU9nzJO2t3RaksrH2U79HETLccEKMyJTeHOGe0NFcR1FMui1YlbB1iG7plWq2AUL7lC-cBMXZ_UYhCanqZlf-Hfx0GnwmNvAtjJtFEEARtmDJ6aWRVJzxJwTZo5wv3Gt4EsU5XZTATnONBD20yzsAHl4JM1uIEANgULeQL8ALnbhdyuWRqSvqjLyLJ4C-fZHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: دولت متجاوز سعودی با حمله به بنادر یمن مسئول به‌خطر افتادن امنیت دریایی منطقه خواهد بود
🔹
سخنگوی نیروهای مسلح یمن: حملات هوایی و موشکی دشمن سعودی به جزیرۀ میون، خطوط کشتیرانی دریایی را به طور مستقیم تهدید می‌کند و ما، دولت سعودی متجاوز را مسئول هرگونه عواقبی می‌دانیم که در نتیجه این اقدامات رخ می‌دهد و امنیت کشتیرانی دریایی را به خطر می‌اندازد.
@Farsna</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/468460" target="_blank">📅 20:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468459">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b9f8b9f1.mp4?token=iyB6aTy2KhwZfv5QYJD5aB0-9jli9ieQk9UHxedldOCclXJ3mwOcdIILK0UJSSwZ93z2UvwqBijw22HhlnTJwl5VfcCXtcKv5YTfJHvRS22KmrYUnWQF73G1qKPawKS3RT5F0Emmv396S1XrB6VI_VEfp34aTc0G2U6jGH8OGunBhAPqtNfI7yH2-y-auN5jWQp13acOj3tdK4hcQXFDuOUAFU6kwn1lZWDcjEhEn0rN-O6wM0bnpk6y7qd-p80BFU_tGSZD-eha8t-RfEJqYb8BiulcwZW05Ua7O1Qp59zUpEvahC1Q2r2PDxRuajb0hx7I6aIZQAVyURsKY3bYog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b9f8b9f1.mp4?token=iyB6aTy2KhwZfv5QYJD5aB0-9jli9ieQk9UHxedldOCclXJ3mwOcdIILK0UJSSwZ93z2UvwqBijw22HhlnTJwl5VfcCXtcKv5YTfJHvRS22KmrYUnWQF73G1qKPawKS3RT5F0Emmv396S1XrB6VI_VEfp34aTc0G2U6jGH8OGunBhAPqtNfI7yH2-y-auN5jWQp13acOj3tdK4hcQXFDuOUAFU6kwn1lZWDcjEhEn0rN-O6wM0bnpk6y7qd-p80BFU_tGSZD-eha8t-RfEJqYb8BiulcwZW05Ua7O1Qp59zUpEvahC1Q2r2PDxRuajb0hx7I6aIZQAVyURsKY3bYog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظریف این‌گونه ترکمانچای را تئوریزه کرد
🔹
ظریف در ابتدای دولت معاون رئیس‌جمهور بود که به‌دلیل تابعیت ایرانی-آمریکایی فرزندانش مطابق قانون برکنار شد. @Fars_Plus</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/468459" target="_blank">📅 20:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468458">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rilbeYC_AiTeEbu9EwgeV0Xut9WZ-L-ku89I0Br27Uzum_ev3zLMuHNIE_Ekzfw-N15LACw4Xu7DsYOoyuK-lRTXu9sAU3Y5VMliProZGB0uESVJ8H7efqMZA73cQiv12ItcHS5utIHzxn_-uZ_PuchK7j0yriupcgQZgrYH_nUBHdtvKrIrQEyq_9vkEc_rENYu2X1jKYw0sCQOWcCGbwdOqLhvvfIyTQWRACsJdKRiH1_5RgjliS6YQUxkt2c07EQl856wpad1EEVdvuarZMBWt3wO9WNI2ed3T4WpCHBguVC5eScBG_n6pv5DZ1O7vaIY5IIceIv7uwOu_kypkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسلام به سبک الهام علی‌اف؛ تا جایی که به‌صرفه باشد
🔹
بحث ممنوعیت حجاب در مدارس جمهوری آذربایجان، این روزها داغ است؛ اما در میان اعتراضات داخلی و خارجی به این قانون، نکته قابل توجهی وجود دارد؛ دولت باکو که این روزها به بهانۀ متحدالشکل کردن لباس فرم مدارس، مانع پوشش اسلامی می‌شود، همین چند سال پیش در جنگ قره‌باغ علیه ارمنستان به شکل گسترده به مفاهیم و شعارهای دینی پناه برده بود.
🔹
یکی از مهم‌ترین این موارد در آغدام ایراد شد؛ شهری که مسجد آن در جریان سال‌های درگیری آسیب دیده بود. علی‌اف در برابر مسجد ویران‌شده، از خداوند تشکر کرد و گفت که خوشحال است ۴ بار به مکه رفته است.
🔹
او همچنین از نمازخواندن همراه خانواده‌اش در داخل کعبه سخن گفت و تأکید کرد که نخستین دعایش، آزادسازی سرزمین‌های جمهوری آذربایجان از اشغال بوده است.
🔹
دولت جمهوری آذربایجان با این اقدامات، دو پیام را هم‌زمان منتقل می‌کرد: از یک سو، خود را مدافع سرزمین و ملت معرفی می‌کرد و از سوی دیگر، می‌کوشید حمایت مسلمانان خارج از مرزهایش را نیز به دست آورد.
🔗
حکومت علی‌اف می‌خواهد چه تعریفی از اسلام در کشورش حاکم باشد و چه کسی حق دارد این تعریف را تعیین کند؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/468458" target="_blank">📅 20:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468457">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57f556abb3.mp4?token=j73PM7eSRJFdPTm7cZ9pjeo0uNWP5IKuDr59Pci7cNqzvZZ7XiylLFSrxwAgErFhnuzncLVxU-g8g8ysLL_sPtBeXd22SRWkCK7hzu2D_YeLFLeHccl3kIT8_VfWtPQAxeu1xfT4IITMUUsp8VqgHmCTzH1q6MZhYGIrgZeGIHW2aNZHbUvbp-8llK8I_yYOA1ty8hULrt-q7F1gFlqv-zMF105gbQoJxgoQFBwIeCe3Ni_V1xq3Nubzh_1NSOCIU_eBDQImIcgSmkDdEX8VTu7T_yhKoZLlOFy5U7dxcXn3P3YV-aatotmNaSd-8f2ZNt3s_S64q6crmCh9AzgMLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57f556abb3.mp4?token=j73PM7eSRJFdPTm7cZ9pjeo0uNWP5IKuDr59Pci7cNqzvZZ7XiylLFSrxwAgErFhnuzncLVxU-g8g8ysLL_sPtBeXd22SRWkCK7hzu2D_YeLFLeHccl3kIT8_VfWtPQAxeu1xfT4IITMUUsp8VqgHmCTzH1q6MZhYGIrgZeGIHW2aNZHbUvbp-8llK8I_yYOA1ty8hULrt-q7F1gFlqv-zMF105gbQoJxgoQFBwIeCe3Ni_V1xq3Nubzh_1NSOCIU_eBDQImIcgSmkDdEX8VTu7T_yhKoZLlOFy5U7dxcXn3P3YV-aatotmNaSd-8f2ZNt3s_S64q6crmCh9AzgMLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قطع چهارباره سخنرانی وزیر جنگ آمریکا توسط مخالفان تجاوز نظامی علیه ایران
🔹
مخالفان جنگ روز چهارشنبه در طول چهار دقیقه، چهار بار سخنرانی وزیر جنگ آمریکا پیت هگزث را قطع کردند.
🔸
معترضان با به‌دست گرفتن بنرهایی مخالفت خود را با تجاوز نظامی علیه ایران ابراز نمودند.
🔹
یکی از معترضان با اشاره به نقش آمریکا در جنایات رژیم صهیونیستی در نوار غزه گفت که کودکان فلسطینی از شدت گرسنگی جانشان را از دست می‌دهند و تأکید کرد که وزیر جنگ آمریکا یک «جنایتکار جنگی» است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farsna/468457" target="_blank">📅 20:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468456">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff57fce1b.mp4?token=pPOSJlH7s7BuBXuo3OnAGssa7m5mqsU8Co3J9x4C4vE2jVTTYIuRDOF78dRe10-RqvwLMjzZRpMIdvYCqOdwLmCTOutMCU9hNXEAgOdsvu7giqjmMq_MIetkUcormPUhH8sacHnsp1EI6oflFjCW2fhjiKgIZ1nt-fdhu2keZS5xCzwhWKls-WopSFfRSBbI1M5lpaiik-rTXsjfewccnCcXwxUGn9DYTsZGH5F4qPzg9qFIGlV04BDcXkqEkfpDftwGIQKaD-1ek4tgORHOUdcArhRhmRbVIT3O5m1qdnsAu-vSXiN86-50yRTLrjtN5gyzD0IiwJhGlf4xH41KQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff57fce1b.mp4?token=pPOSJlH7s7BuBXuo3OnAGssa7m5mqsU8Co3J9x4C4vE2jVTTYIuRDOF78dRe10-RqvwLMjzZRpMIdvYCqOdwLmCTOutMCU9hNXEAgOdsvu7giqjmMq_MIetkUcormPUhH8sacHnsp1EI6oflFjCW2fhjiKgIZ1nt-fdhu2keZS5xCzwhWKls-WopSFfRSBbI1M5lpaiik-rTXsjfewccnCcXwxUGn9DYTsZGH5F4qPzg9qFIGlV04BDcXkqEkfpDftwGIQKaD-1ek4tgORHOUdcArhRhmRbVIT3O5m1qdnsAu-vSXiN86-50yRTLrjtN5gyzD0IiwJhGlf4xH41KQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اگر ایرانی‌ها سلاح هسته‌ای داشتند، من به رهبر ایران زنگ می‌زدم و می‌گفتم: «آقای رهبر عالی، حالتان چطور است؟ کاری هست که بتوانیم برای شما انجام بدهیم؟»  @Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/468456" target="_blank">📅 20:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468455">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b543d8f54.mp4?token=KmG8dh4xl9Zfe7vvsEwpsaqrClK_Ost-l0vPUMPcsKvJ4aaT4hJsW50CSPxd2538eiCPwJStjgZbVAL1THGj2d7ulB4ctk7sVtqmAeSi2ylbAS5YGG1ifyFLxlI8OcNefrVwzNYGQ5SO0Ea1ewaq5vQlQKBfHuIMezyqq026qv182IsQbACa_HT0NGL3lkowwZqi6PPqj0t_MkrjnxZq3CDJznaqgVuPG91Ar6Sm-5Q1VvNk7AseTqBCXOg8yTW9soW7DzDphrd_jyAOrG7tivJjDx8ZuLejxQr-zWbq9aCGYv6oIBQ3Sy_yPyOrgRXO5VGY-XGwfZsJdD4xirLsehxZcIF4ot8FhdmmHIh9kv1hqfeNO_O5uZJQi8M1vcQLyyMGzohjeX2dfQsJ0yPgw1TXYPAPM40tpant2Cc4cZ_Ff9-grZcKoAK9s5x3i63XKuPJtwusA3Zrbq_d3V3AQR9ZjxYfSMPnERRFCs0qWygitBk9v7N6rfRigMbKlnN8BQ8pnLd3h9cls2I_0J79NYR8rXMLShBbspW3INE9RLiximC_S0nhbVrZqm_etWtLLPeYVN4IOTDaoeLMGhdo8ftHjN0DSutLz-AfldBmvyDiUCKRvRl8-qCTKW0NoHvlpU8tO1XekGJEIKn5l8glBUHZAqUcVracC4G8Ig5Pv2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b543d8f54.mp4?token=KmG8dh4xl9Zfe7vvsEwpsaqrClK_Ost-l0vPUMPcsKvJ4aaT4hJsW50CSPxd2538eiCPwJStjgZbVAL1THGj2d7ulB4ctk7sVtqmAeSi2ylbAS5YGG1ifyFLxlI8OcNefrVwzNYGQ5SO0Ea1ewaq5vQlQKBfHuIMezyqq026qv182IsQbACa_HT0NGL3lkowwZqi6PPqj0t_MkrjnxZq3CDJznaqgVuPG91Ar6Sm-5Q1VvNk7AseTqBCXOg8yTW9soW7DzDphrd_jyAOrG7tivJjDx8ZuLejxQr-zWbq9aCGYv6oIBQ3Sy_yPyOrgRXO5VGY-XGwfZsJdD4xirLsehxZcIF4ot8FhdmmHIh9kv1hqfeNO_O5uZJQi8M1vcQLyyMGzohjeX2dfQsJ0yPgw1TXYPAPM40tpant2Cc4cZ_Ff9-grZcKoAK9s5x3i63XKuPJtwusA3Zrbq_d3V3AQR9ZjxYfSMPnERRFCs0qWygitBk9v7N6rfRigMbKlnN8BQ8pnLd3h9cls2I_0J79NYR8rXMLShBbspW3INE9RLiximC_S0nhbVrZqm_etWtLLPeYVN4IOTDaoeLMGhdo8ftHjN0DSutLz-AfldBmvyDiUCKRvRl8-qCTKW0NoHvlpU8tO1XekGJEIKn5l8glBUHZAqUcVracC4G8Ig5Pv2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی کمتردیده‌شده از سفر رهبر شهید انقلاب به استان زنجان در مهر ۱۳۸۲
@Farsna</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/468455" target="_blank">📅 20:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468454">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtzS-T-nGnKUj3rOyoL6ugFtN9DL0WT7oSObHDQNXrzzMnM2_LyR8dliuFVTLYsB8T772tsaN-6F7XMouPG28GwS6Nn8lVFXCLNo9le5koaQmv-d0o9vd70G67VkLCSTwGxOgBHYXN7QDn930PvU5zOG-HcfzdEgJocUhnXEWTFKE8wIqjaMTdiSoiXeA2Cu4GcW95Zm-3164NROje-wo8wCwvPHpXrnLdHuHKncUAJ9yLCw9QDE2Bn8yEmjX_yviJNtBHar8MdZqOuoQss1Ob95j7MzMlqymGFFxNEHCn6xca-nMzNhwC4AjyAJh7SUSLtYc8VYwQq_9zmbzNM1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک بانوی دیگر در سیستان‌و‌بلوچستان
🔹
فرمانده یکی از حوزه‌های بسیج خواهران مهرستان در جنوب سیستان‌وبلوچستان درپی تیراندازی تروریست‌های وابسته به آمریکا و رژیم صهیونیستی جلوی درِ منزل به‌شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/468454" target="_blank">📅 20:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468453">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-text">🎥
تقدیر نماینده ولی‌فقیه در استان از خبرنگار قرآنی خبرگزاری فارس
@Fars_Chb
-
Link</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/468453" target="_blank">📅 20:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468452">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAiaQNqieLMlLq3tyLEXuSsccaAIegFMwQ08ydMd-FZtdpXJPordo2X7apt7dzbmSiWVbMGychfL4cRYAgCsUmfhXcQkCrAF0JlQia6fVmPZnawCyg54F9nuYXt00JFo7Js2BGtY323YhBpebCDgyC4bglt7rqh9_AvboYqypYFi9pSJ-dPmiCgG6_pcJaFLy5slxBuDY1JNGs32PhA2Ex8M8i0T7fMM7ZknGIwZEFavAxZk7f3-56jgXfhfjAfjXgF__BM73tK378vKlaDS8bdZyKYwVo-TCtaRYOVXXZVHDzrZMJ87tITCP8jBzAtur3n8S30VcHAd_NcHUW9vqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جانشین رئیس سازمان بسیج: ۱۰۰۰ گردان جان‌فدا در کشور تشکیل شده است
🔹
سردار قریشی: آموزش و ساماندهی ۱۰۰۰ گردان جان‌فدا در سطح کشور صورت گرفته. تشکیل این گردان‌ها درپی درخواست مردم برای آموزش نظامی و حضور سازمان‌یافته در کنار نیروهای مسلح انجام می‌شود.
🔹
نیروهای مسلح ما تکمیل هستند اما همین اعلام آمادگی، پشتیبانی و حضور سازمان‌یافته در نقاط مختلف پیروزی نهایی را ما را رقم خواهد زد.
@Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/468452" target="_blank">📅 20:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468451">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjzppAwkH05P2k-e17bhEdHiYz5J-BOKZJLFj4CEn8lT9xG5ukyiTYD8X6E2NruLWvJ4g5NbQ7uP3W8iD1QN2Kv6ySGztCEtLmSQ8AtTkxRzAvKJlJFYqsTYkK4YYGE6D3fG4c2w-A-dX6cvCuvsFSKVKtyNXb19QUNAzFNJF7HCLQ10Gf_nVJu2mw_qZeTxFpjkA6NXOxJlLWCGHRuBwvIHCw6z1Q79cgVAHy9BBDL5O7FfABtEmXCabBVxQgIhKz1fsNCmNEEJoEIwLAT3XvdPdPy0M8Po5YHqLo1a0f7iCIwVaKZXqYyjFJjdPYrzpAsq9kTbyCmSldsAhzX8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت مدافع وطن اعزامی رفسنجان در درگیری با تروریست‌ها در زاهدان
🔹
شهید محمدرضا رحیمی، اعزامی از لشکر فاطمیون رفسنجان، در درگیری روز گذشته با گروهک‌های تروریستی در منطقهٔ کورین زاهدان به درجهٔ رفیع شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/468451" target="_blank">📅 20:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468450">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0owFiYGH_I4wZQ5RhzzuQwvyyUW6fGwGNNneVogGZElaflvdZQlVw79v0EUSdeNhul71uTkur2-n3Oe54ad2jc37PYs8vL1tAR9UaclyalNoyueMItXeiDebTK5JCH7_pEeVJXDuQvrHLraePaxJOWXVDmk1dSo3bHMBZAUrHf65NC6C8IfbTw974h94XdPPLdt8nBpMTvLPIIzDWMD0KQAX-yRN0seuVwFQC0PzQQEYcY0tw95ww7_V9tG0RwhWFN8CWcfKa2DYHFTXJ7KhKjwRZcxN32PAMkZ579QJI6Y7Qw3LnkAxurXV_VYqOrkDsGcjqU-XruYY6gc8dEI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکایت ۳ میلیون شِکِلی رئیس پیشین شاباک از نتانیاهو
🔹
رونین بار، رئیس پیشین شاباک، از نتانیاهو به اتهام افترا شکایت کرد و خواستار ۳ میلیون شِکِل غرامت شد.
🔹
نتانیاهو پیش‌تر «بار» را متهم کرده بود که اطلاعات مربوط به حملۀ قریب‌الوقوع حماس در ۷ اکتبر را عمداً از او پنهان کرده است.
🔹
«بار» در مقابل مدعی شده که بارها درباره تحولات غزه و تقویت توان حماس به نتانیاهو هشدار داده، اما او این هشدارها را نادیده گرفته است.
🔸
چندی پیش روزنامۀ هاآرتص گزارش داده بود محمد بن‌زاید، رئیس امارات، پیش از عملیات ۷ اکتبر ۲۰۲۳ دربارۀ احتمال حمله حماس به نتانیاهو هشدار داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/468450" target="_blank">📅 19:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468449">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فرود اضطراری پرواز تهران-استانبول در تبریز
🔹
پرواز شماره ۹۷۰۰ ایران‌ایرتور با ۱۱۶ مسافر که از تهران عازم استانبول بود، به‌دلیل نقص فنی ساعت ۱۸ امروز در فرودگاه تبریز فرود اضطراری کرد.
🔹
تمامی مسافران در سلامت کامل به سالن ترانزیت منتقل شدند و اقدامات برای رفع نقص فنی یا تأمین پرواز جایگزین درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/468449" target="_blank">📅 19:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468447">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q81jHLR23jARhXwWxy9OL9ytrlgZaIYLfMleb1ppx3tdI3xEaJ_T16R8Teix-uTIvfUSL7TcCFvj-KPmH0-AjjEiK2TYtISl3ka2oiFamyLPKKt7L7kwm0fv3Pq362wHCSKmGldewM4v4KEJCGy5YZ0J0qhlyfUc7ha1sEhlJQoBQl2Ss2-wJWy6y_Uq7HJPdSkJ8VQ3unqLMmeZHCewY68pV1KiFuX3BVOWWjkztK6m9SlUIGluk7gOQGa0EKBuQ30Hwr1LIjN4KQNRlwPvCld4ye_aAQB5QAfn92MjSXBwVujw5wcoUcDunazhAp2_s_uUO6r9Y6GvwQvUpqXBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5qo3qXF2TLpjwGn17J-qkh3AqJD8vtfJ8Ocw-gdF4Y16wDw5qlrpaoTJIPjTCUrSJdb6OGk0_aQNQdwgZCy_FFXh2n9Emk6K0PopyUo-c266IeYquZxDB0M6TzazrwpGLmlOsI7_moMzQde0dgkwVY34g1xISGEa4_NfJHjmgZwO7cmeLiAN1oEyyxSJKKfIdzflDJKlZNVwxB9B_sepwLMonltXrl26DvAgJ-d1db4iFhmPduySxATHzA2knfSi8ZgT62Dp7J_5oUCrc2EgVR-l2vhLi27XlWP6YbqJ-gYpmShdXp5i2-DOu_PxMyEJJ9yXnFv3JhR0e_ZnBGPmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ام‌دی‌ها به آسمان ایران برمی‌گردند
🔹
سازمان هواپیمایی کشوری با بررسی شرایط فنی، مجوز ادامه پرواز هواپیماهای خانواده MD را با رعایت الزامات و دستورالعمل‌های صلاحیت پروازی صادر کرد.
🔹
براساس نامهٔ مدیرکل دفتر صلاحیت پرواز، موتورهای JT8D-200 که تا ۳۱ شهریور از…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/farsna/468447" target="_blank">📅 19:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468446">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">📌
حضور  نماینده ایران در مسابقه جهانی ژیمناستیک هلند با حمایت بیمه دی
🔹
هومن جعفری، تنها نماینده ایران
در مسابقات جهانی ژیمناستیک ۲۰۲۶ در  روتردام هلند   با حمایت بیمه دی  به این مسابقات که در هفته جاری برگزار می شود اعزام می شود .
🏆
بیمه دی حامی قهرمانان کشور</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/468446" target="_blank">📅 19:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468445">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/468445" target="_blank">📅 19:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468444">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2ags4qo75D1OMdYiQTlILT7CH5v-mXjWMXUedb_Z2f6Vs2a5hs4zVXzEIzB4KaF6VoO0yHNOoMXYdkGwpgQ0ZxotmO6xuM165FtCTMS14bqeJcAeRgzxgGH5PoN3SFpbWnmoQfjLUQayPurA8g5gA1c4D8faTYFIglllXUjxC5P6CY0tVYIwQ5zYdJgUAr_xZO4ZwVDLRpRG3jEXroHhnaT3S2QT3ZM7k8GwZ2jDqf7yQh4Vj23KF8KIgiDWYQmMgxt6_UL5tXKztONLfhCDIj76nV_Va1lV10jMQVk4ULyisZnVo1k3Z_faot-F4ahy5m2SgdW12lhueemVo3oKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست ضدحجاب علی‌اف، صدای ترکیه را هم درآورد
🔹
درپی انتشار تصاویر اعتراض کودکان جمهوری‌آذربایجان در بیرون مدارس به مصوبۀ ضدحجاب، مشاور ارشد رئیس‌جمهور ترکیه با انتقاد از باکو، محروم‌کردن دانش‌آموزان محجبه از آموزش در جمهوری آذربایجان غیرقابل قبول است و از…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/farsna/468444" target="_blank">📅 19:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468443">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86b8e5aeea.mp4?token=GQRRVPihHrjx4E7l-vGnyGGw1p05F7Uvp7QU2qqd8UJjqSRH9jLydZ7sTOqDPVUgdPYPeOZGc1AptQzfjDG3eKcUYEqHZkmVzQ-S2fe3RyqIsyNOKZVmp-R9NllOq76AAkwIevddklgvZuFuqEB3zvNXZwtArfcTE1LdXyIaAujQGzHqXCDEciUZHAtC333txHD9OuGIV-hM_GwBE5NtgZ8qK3lDIIl6oG3VnWwmIXDE8s6mZ7n9zY-YdUHn-wUWB1nJVk1ZPhCudMGzV4g8XhDMsuXfWUvuUpUqTVmVXr6s8-6BUjBrPVHzBx7bWxDHPpubQKoHE78acViR80WVCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86b8e5aeea.mp4?token=GQRRVPihHrjx4E7l-vGnyGGw1p05F7Uvp7QU2qqd8UJjqSRH9jLydZ7sTOqDPVUgdPYPeOZGc1AptQzfjDG3eKcUYEqHZkmVzQ-S2fe3RyqIsyNOKZVmp-R9NllOq76AAkwIevddklgvZuFuqEB3zvNXZwtArfcTE1LdXyIaAujQGzHqXCDEciUZHAtC333txHD9OuGIV-hM_GwBE5NtgZ8qK3lDIIl6oG3VnWwmIXDE8s6mZ7n9zY-YdUHn-wUWB1nJVk1ZPhCudMGzV4g8XhDMsuXfWUvuUpUqTVmVXr6s8-6BUjBrPVHzBx7bWxDHPpubQKoHE78acViR80WVCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قاچاقچیان ۲۰۰ شیء تاریخی در تور نیروهای امنیتی
🔹
بیش از ۲۰۰ قطعه تاریخی و فرهنگی که اعضای یک باند ۱۰ نفره قصد داشتند با سوءاستفاده از شرایط جنگی از کشور خارج کنند، با اقدام اشراف اطلاعاتی نیروهای امنیتی کشف شد.
🔹
این مجموعه شامل آثاری از سفالینه‌های پیش از اسلام تا اشیای قرون میانۀ اسلامی است و کارشناسان میراث فرهنگی در حال بررسی و ارزش‌گذاری آن‌ها هستند.
🔹
بخشی از آثار، از جمله اشیای محوطه باستانی قالاچی بوکان، با هماهنگی وزارت میراث فرهنگی به استان‌های مبدأ بازگردانده می‌شوند. کتیبه‌ها و آجرهای کتیبه‌دار ایلامی متعلق به خوزستان نیز در میان آثار کشف‌شده قرار دارند.
@ّFarsna -
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/468443" target="_blank">📅 19:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468442">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dd088ef2c.mp4?token=Yd-NM4tp41ZekPqEJjdwj-MyXte19_wnOSaVhhL7QSaiC30opFeoSl-hIrnEXJg3BsKi41oPbFSBiOnE8-pWvOqVHSEAcFux_aUDSp1hG-FWckL-ORNlWOyPqesW7pnvcfLUsUY5Ius-8rZ0lTiLFvRVkwM7k_I2_YzCZVHr0-EcOOFiDzE68YJbYfexC6YnElQOJ_QaSmkxLrOZ3PeDbVMXvXH8Fb1_77OI0PLEjR8zxHLed5VQp-BIKO3WrfwC-VmYfQPRmb7ev1nGZkBJCE5LEj5ZKOAlaC9d_plmHSqxouTqD7V-B_VRpRNqQkMY8HBEoT2lSG8fAs2LbScFFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dd088ef2c.mp4?token=Yd-NM4tp41ZekPqEJjdwj-MyXte19_wnOSaVhhL7QSaiC30opFeoSl-hIrnEXJg3BsKi41oPbFSBiOnE8-pWvOqVHSEAcFux_aUDSp1hG-FWckL-ORNlWOyPqesW7pnvcfLUsUY5Ius-8rZ0lTiLFvRVkwM7k_I2_YzCZVHr0-EcOOFiDzE68YJbYfexC6YnElQOJ_QaSmkxLrOZ3PeDbVMXvXH8Fb1_77OI0PLEjR8zxHLed5VQp-BIKO3WrfwC-VmYfQPRmb7ev1nGZkBJCE5LEj5ZKOAlaC9d_plmHSqxouTqD7V-B_VRpRNqQkMY8HBEoT2lSG8fAs2LbScFFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع بزرگ جان‌فدایان تمدن ایران در تخت‌جمشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/468442" target="_blank">📅 19:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468441">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDHwqpfNoXk5V2JXVejc3Kuc_p0ahAtiXgyGyH-LcK2RyBwiWi-9SEOh73R3opiAPpqejsah_Bf4Zll8UgzpkrFsHk8KVviw4YOAj-U9n-4JM2kkY9DAjl47s6zxcujKc0dBLVK0giHi1ZV-sT69FB7EekmzjY7klXykyka8XRNlN5EmEFjg3XcYkqCYLnenUHshiHrtGNtZaRde_Imgbvjdtm7fvZFIBdMSGaEJOwCJgsjLgjSm1ROMrTtFJDw5f_vIKH8-LTNagHo_E5PzVSADXxABEzuIM3D5oEF-J_IuX0CUk9nFfrXJhxtvPDskJugKtJcI_apb__9h4wf1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوگین در گفت‌وگو با فارس: روایت غرب از ایران تحریف‌شده است
🔹
الکساندر دوگین، فیلسوف و اندیشمند روس: غرب، به‌عنوان تمدن دجال، تصویری تحریف‌شده از ایران به‌عنوان جامعه‌ای عقب‌مانده، تاریک و ناآگاه، که تحت سلطهٔ مفاهیم و باورهای دینی قرار دارد، شکل داده است.…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/468441" target="_blank">📅 19:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468440">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e5a1a316.mp4?token=So80bAbY0-1BwimZOY48hQUFJVfs_8FwiroEoTDf89b_090jLAu27BTPYd_LoAYe7Q01rQi6BBunX_epkd_rtPSOWBF3mJ6Jhz4sqLZmEZjfMBolYGJTZnxAURa56kilrzxOA4vyUjWtPhR0i_9IWmrpy1x_wY9oVsmNXdsFCcX02kxHZKAj8pRKm83yOEtxIDEE1PgHEXE_tplC9FiLfUf0SncL_tJLxtfQEWglHNLjh3s6qH-_rhNOTNe2OUPXxvP4jxMLrCqC41b8Ey5BGyhA80P2WlStDudqY5uVA_13JKTKURHrd0aySmfPV4Oi5h2cqp2vTERAhDgBs8ZaUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e5a1a316.mp4?token=So80bAbY0-1BwimZOY48hQUFJVfs_8FwiroEoTDf89b_090jLAu27BTPYd_LoAYe7Q01rQi6BBunX_epkd_rtPSOWBF3mJ6Jhz4sqLZmEZjfMBolYGJTZnxAURa56kilrzxOA4vyUjWtPhR0i_9IWmrpy1x_wY9oVsmNXdsFCcX02kxHZKAj8pRKm83yOEtxIDEE1PgHEXE_tplC9FiLfUf0SncL_tJLxtfQEWglHNLjh3s6qH-_rhNOTNe2OUPXxvP4jxMLrCqC41b8Ey5BGyhA80P2WlStDudqY5uVA_13JKTKURHrd0aySmfPV4Oi5h2cqp2vTERAhDgBs8ZaUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایش خیره‌‌کننده نوجوان کرمانی در بازوبسته‌کردن سلاح تیربار پی‌کا بدون استفاده از دست
@Farsna</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/468440" target="_blank">📅 19:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468439">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7TfAQZYVx-PX-tKph_YE15o-JPlVMVww29fXPf5d7EAVErWfNfPP1h9of3vQegVIlcf-rV4KoMkfITlSPO2ScjGhSLxvWca-f4Dat7nNupdl0rdrLvuxQEHDD4X91L3aFMBBlwnV2lmc0bPx8-xwy3J-v5zzp1j6TOhcEVsmnjZxboep6hJCq8Ks2YChW3gAKib2rdU7klncC8plYj_DO0r3hLLBMgdqr7nP1SC8lUjGBRo647mBXb1K7T0WmjC4I2lXrCCvikIYcx9zCT2APe2CMRY-6-lMjuMrF_qC3mf2BbGEw_pHziJEYZb8h7k1NxH1jsvKU9Wz-weElkdTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توسعۀ میدان نفتی سهراب کنار سفرۀ پرندگان مهاجر در هورالعظیم
🔹
هم‌زمان با فصل آمدن پرندگان مهاجر به تالاب هورالعظیم، خشکسالی، تأمین‌نشدن کامل حقابه و صدور مجوز توسعه میدان نفتی سهراب، آینده این زیستگاه را با نگرانی‌های جدی روبه‌رو کرده است.
🔹
در سال‌های اخیر،…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/468439" target="_blank">📅 19:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468438">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYZwnIBMvPmt9YBnDeYYMhLJEkRRmSVG8oO9Oxo9EUkGW101XE4UU1VaJnUZQ3Yl9WnMUif_vhm2FLnxDYrpdbWLqZz7t3IgAgJqyvRs37_uZi6BhMbKC7yAiRWEBwy7KKz4CIWZBVQ7LDDXY-XPnyl040Zsi6EmQQs5w3_QTndU5YOjLfnqZxnQvtWuILe9HvqEmQelD8E04y2jghspuLkqEOLo30IiuD6Xscw27_rNzVDt3QOR-RMEpT9RKw1K6D8DggO1Ih_k8Q_4M0YkTk_37Ze-q1WAGRMNqMduTZT0u3SIHS7cYWvz_OD-2H6hhWBYbNVcZHSf6tNAfWTpzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار خیبر و پرسپولیس نه گل داشت و نه برنده
⚽️
خیبر ۰ - ۰ پرسپولیس
@Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/468438" target="_blank">📅 19:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hr1w7mry36Grcztt8JheV9G-Zx5_egdCyXN43J5Ya5d7UhzN7Ptns4AhEVDMDddUo9Dnee5JHmgNle_ApijBK92KFhdybsE4QCDOTsbzlvwOSMwbAR7bb2dUj62exbuCp89P_AP7YmY6EZYXAZ48bKHCGLz473_1o_HbK0iCmgCpQ-qOHSxCsx2dUtAScYaYCftXiD3m5ksSZvi99ro4uF8dxF8w6L2V2iGfkrLMyEcG5x6pxGFrLu-0cMAdqABkAiVafIJedU6Y6n0z7U2-RN10gdIX8Y_FTzeeIKS1haMw1kFCWeeH3CTQqSD_BFKe8Ln6rcfUC6IHfThvStdLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3Mb9462UC_WgJs8SQQUMN8TN01va3rcsF3IniwBM-ta-25fK8xUx2tmoWQ-B7IIP8Pf6lz-EVSDIqbL3_hQWprmt9oQ4FYGXWlO9KVIoeaJ3PydotolOukfTk9HIDR3rvrBx3BNxbfAX6Xoa05td_bz5cbLPSZZrJdo0muoaWD5KW2wbutP9hHAgqdLYioHPfkxZymaXaHkEfV1ZJZf_6_10TRtPrUTj-fQJYzVopojCzen-J25cmBLlGojkPyAbzuSQ5S8-drdikzUAz08_2rvhc50qHHfdWssUJ0gjFY6ZwCN4mpG-gte9jQ_FRxrgS3gbsDH8NLe3HqWn9bqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HgVLyHgiHRpyN3Zc9VrGUi1RdyD7Kmun4SYs-HE4_AhAIX_w2C0JybPwl1qdcxXPOI9ifShklyF_bvlF5yMTcKRbdBS7b_7Twcc5mlnpB6cZgETUM5tmmGzzCOlX7FESRg-FCGXV0dv525-oqrKCVpahI8YmngdczkMXT9_Ha58wFRGzcIAy7vEE7h5BvEVJxPzWBudpf3AlJwtMU4Y9S9xFlykOxgAuuA2sPd9X_APIlWWkYMV8u01SPtBSoiN5_Szg4DAnsXtprQPRpQzkMc5vhPwEuGyj-BhOyQBlhc3B7G_9VjOc14XiMXwNzVrN9ymgrbBKiZR9DVAx7HGzTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dh9ntOp513je26fqao64LMGofEansZ5TeMbGAj8wujN11vSxjCFYg0qbwlcCFwduQe30mQvTPwrM56NcM96NwOvh-zOZwQ-Ie2NiqBj989f0BKjmypIVv7xEVX9QBXcbOoyIb4teY6l_fqNYPUe5y0NXuaJ2HkNwJI51Q34ZnNI5_BsJE-C03rnX4EbwjGQVIc28ThKLrAIXs4u32pVdtisDqvzqtyJwHUc53pc25bhk3YqMkedZBXJkfap2kvqfg51SE4OKrJU40yO7uN4U35zimb5hNI3nP_3ltoFJw0WnxYkJttdDqL6NNBVYDuRnJEIrlgvb7ICstFm3BZzPUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csXHdUkn1URJf8cSwHG7_Vt-9PKkYSxWSmhE1Rf4hiLtuseHolwwneKJzynMUs5q24kiqf8UCtGncSV5xaAHSEmodqD5nxacgdKJjIN6Gf0etLx1Y3tKUbQnAjkcbpQXKJcsU8l5RjLcTrfAEP7A3qM_rsjpH2gd4iCOKturMizbGmAhUJvXxoJGbZb-OPd2jeaDBu_dPYuvsRPI5T6B-rEbCcPq7gwVqQlewxm52O-WXc2swQecn4PM9IiUoEijFJiSqgZBRHigTQ2LrUrKajE-4zWBZQZD-4Byv6yqLFOXahBuh-F9X7YDQCUISdFH9o9yNyMGDsmR0l53rEvz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TC-8kZ0bg6SA43WN01EsVdHhOoSlSxTxq_qNKdReK-aK1zzh6FUD4yDOa3DHXkHTdcwaxjwyYE3vIo5wrxmdqUMKT6cfqz6N80YHF-bC082NscvMslLjeJOC-1qD6yKrdUR2nhO9CJOCeAYcqiQRRIed0qEapHAlo9R0STvlMBinXo9AmiU87Nx75ZnmQWv_ZO_JhokdOFcZnGATBHUPL-7R4askuRMi8dmBGaMYk3pQMdZIvtbC4FkApdIOrCgpRe8Mj00yMlPz-qKXaseV_mpFVrKlrGO2W_sb0qpWeQl3Ycnr9oM_-_iNR2JNiqXnN_yVFRK677Iq8ccSkPFCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxfLfWkfA-aIcpn_9A09n_mcJpYyngw42_17jw01JDAm_9lj_xAYZKXVSkHW4Jv1twkqJXCpNl2LRXaPyGm93BluWZ9j_kYvsjCZgaYjDzYlhqdFfDLbMp1yHC9EEdNFQbwuciU5rNgLVpn7DBblFAi90yyZPZFZGb2YSM1CjZtyu05DWiLqwpkN3idkzGXo0hLcbJDKvEx37FXTFrrCnMGcmtu04hHtQH11KGxBPE3JiwsumtAP3gF0ETzPTE-HyLsP62dyZj6F18TsDb_C2bMPkWtI9AXyl64kP_H62n3sBDTGjq-x1FIEF4gbvNU8AzoUgKWn7I0fcGbU8K709w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یادبود پیرغلامان حسینی در خانۀ مداحان
◾️
مراسم یادبود حاج حسین محمدی و حاج سیدمصطفی موسوی، از پیرغلامان اهل‌بیت عصمت و طهارت و به یاد درگذشتگان حاج حسین برهانی در خانه مداحان برگزار شد.
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/farsna/468431" target="_blank">📅 19:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZK1wFIMwtGbrXcFVMd3G1iBmhYmrt0deF4I2ZSnyS9B6QpWeiZmPiaD5NbRIfYRO-oRUaRk1UWDb0C0mUKn3nYSLkHsZrPdqFrLT3gW-9BjjapnFj7fR6JvWIf8vvxzXyFajT2_DYYI-kQscrfoCMTgIoTa7V5aJGI_qsLGv4SYbgCAF-4g48C2EnrpzmfLo7lmkdT07_649Of2C5QeSruFsGBIK9e9apuCXZYGv0BRkAguUn11C_Qxe8vS2iIPDyQjPsWrInAZmw4bcseYvcJ3lGJIY3O2pALkdcC6-Z_tXgR4rGd7CfHppfsa0XGhiJzPXutSumU2zwrw8YgWfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
المیادین: نیروهای مسلح یمن به ۷ کیلومتری شهر تعز رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/468430" target="_blank">📅 18:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f54c5cee1.mp4?token=FBVgO84AxeY2m1Hj3GYjPmg0ia2uXhMDcBs1eOM9Iq3Xn4NZO2Ocn24MOujaqt-uQcaEtrdtGsgR5ZR1m3PbLTaqmf_S-fzqWVgot6uOcXxIyQsSaK1OKqXweS9MAELNcdZRtJqNxH_iFcx4sgVqMckflqiL93Xi3K1eQ5G0zu7HfyFFucoF3LHcnZL9feeg7tjAxEZdafn-Kv1JJHsidYunwdIoKS9FiVTXtS90JFOpLSev0fLR1PLia48vFjyewEQsn9QqO0gMSDRSSn2a3wqePtf6IltQDBglqoOHAjtQ6bMfGoi_9jULS8Jjmc_pfqivR9oluG0CF0kO9Z2QuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f54c5cee1.mp4?token=FBVgO84AxeY2m1Hj3GYjPmg0ia2uXhMDcBs1eOM9Iq3Xn4NZO2Ocn24MOujaqt-uQcaEtrdtGsgR5ZR1m3PbLTaqmf_S-fzqWVgot6uOcXxIyQsSaK1OKqXweS9MAELNcdZRtJqNxH_iFcx4sgVqMckflqiL93Xi3K1eQ5G0zu7HfyFFucoF3LHcnZL9feeg7tjAxEZdafn-Kv1JJHsidYunwdIoKS9FiVTXtS90JFOpLSev0fLR1PLia48vFjyewEQsn9QqO0gMSDRSSn2a3wqePtf6IltQDBglqoOHAjtQ6bMfGoi_9jULS8Jjmc_pfqivR9oluG0CF0kO9Z2QuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس سیاسی عرب: ایرانیان با تکیه بر فرهنگ تاب‌آوری و ضربات نامتقارن نبوغ خود را در برابر قدرت نظامی آمریکا نشان دادند
🔹
روایت‌پردازی آمریکا مبنی بر تسلط بر تنگۀ هرمز کاملاً کذب است. در یک روز ۶ کشتی در تنگه هدف قرار گرفتند؛ رقمی بی‌سابقه از ماه فوریه تاکنون؛ این در حالی است که ترامپ مدعی بود توانمندی‌های ایران را نابود کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/468429" target="_blank">📅 18:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e1bc2416.mp4?token=AiA5WBlo5LcOX7ddplXwlRrbcXItaXkD02qV7wfK_mO0bYir1LltRbvQh_EuQLUbugqcm4cFtYQczPcMfcBYTDfzSydGMsS-fFTIRY_RcIU3FvEdnh-08mmqHN7ffkCXOdMA1lMGwFTrCBSYVnI3rqx9rusf79OONdbbFRIJ7D6wAhXe66sisUEuFdGyoBBWk1Jsxih-YSKB-aeBht4Xyd_XXNbVfjPsE-y9oKr9eYUQh6kEGZz-B4wa4Gra6LHirAp1p6x2ochzAmXekDN7IHEuwFACeXiTeCju-VmJgQYQ4bdZGOt8F0OD3tQMVR5TkKvvC7m9j7-Bkb80Pys1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e1bc2416.mp4?token=AiA5WBlo5LcOX7ddplXwlRrbcXItaXkD02qV7wfK_mO0bYir1LltRbvQh_EuQLUbugqcm4cFtYQczPcMfcBYTDfzSydGMsS-fFTIRY_RcIU3FvEdnh-08mmqHN7ffkCXOdMA1lMGwFTrCBSYVnI3rqx9rusf79OONdbbFRIJ7D6wAhXe66sisUEuFdGyoBBWk1Jsxih-YSKB-aeBht4Xyd_XXNbVfjPsE-y9oKr9eYUQh6kEGZz-B4wa4Gra6LHirAp1p6x2ochzAmXekDN7IHEuwFACeXiTeCju-VmJgQYQ4bdZGOt8F0OD3tQMVR5TkKvvC7m9j7-Bkb80Pys1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی امید به دستانی مهربان گره می‌خورد
@Farsna</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/468428" target="_blank">📅 18:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9964cb0d8a.mp4?token=Bb1vvY__cscqL3-lcWk2lnwv86q4ipPzWzvBAne7jrRofNFkz-_KRjnkr37Mi7mmAhwPUaeANs9ccUFhzD32p-eHc_Ya0i_UBSd4DJY0cTCi4-03Hcb1A8Z_2R3e9bVABPEDBzRRbjjZJo_W4Z5K6dccOoHG3p7CPW-pbaq4V7DeeC2Z4zS0WjghebnMmjPZasFeyGa75pcl7FquGLhSncmyhVO_vknV-irIoCYbDSP_9A_oZbB02APjqfnNGnT1c6UEhYMa4yLboFsQt_yEFxr4RizeUjYxNR_xJ1dkCX3yfthbw8kPG16IxoC9uuSPRtMR2ZJzEL1ubQfv-B1Z2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9964cb0d8a.mp4?token=Bb1vvY__cscqL3-lcWk2lnwv86q4ipPzWzvBAne7jrRofNFkz-_KRjnkr37Mi7mmAhwPUaeANs9ccUFhzD32p-eHc_Ya0i_UBSd4DJY0cTCi4-03Hcb1A8Z_2R3e9bVABPEDBzRRbjjZJo_W4Z5K6dccOoHG3p7CPW-pbaq4V7DeeC2Z4zS0WjghebnMmjPZasFeyGa75pcl7FquGLhSncmyhVO_vknV-irIoCYbDSP_9A_oZbB02APjqfnNGnT1c6UEhYMa4yLboFsQt_yEFxr4RizeUjYxNR_xJ1dkCX3yfthbw8kPG16IxoC9uuSPRtMR2ZJzEL1ubQfv-B1Z2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران با جاذبه‌های گردشگری‌اش در نمایشگاه چین حاضر شد
@Farsna</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/468427" target="_blank">📅 18:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468419">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQtbsWC3dH59vahF_UV5o1-3me8DylTHyTxPIWvHbWT-swHfAV8AugOmyUfIRuzXXunTJc5uYqqtRkQVRxyeE4TeV7PLH0oHcd5m4N9nx6QwosF43vxQ8CqEt6hQf5z42fNIUml1O5PEaw_uRu8misMs6A-NiuPhNgi45cEhIdUot3HPXayyUK3vt0ooR2sYqppGOMdgvCQ3NL_VHBg84V9L2oG2RxpXW4PkiOf8zDObgtqaAgUzAolwIJED2qUtIh7Y12XaDJZOOxkEGbAvVXpEFpczJ5ryY2FCpU-pyq0TlSSS25jcxzV0Fj9Z3lr3D6xvzC25gooEoGzMcYNdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
الکساندر دوگین در گفت‌وگو با فارس: انقلاب ایران تمدن اپستین را به‌چالش کشید
🔹
پروفسور الکساندر دوگین، فیلسوف و اندیشمند روس در مصاحبه با فارس دربارهٔ نقش تمدنی انقلاب اسلامی ایران گفت: انقلاب امام خمینی صرفاً یک موضوع داخلی نبود؛ جامعهٔ ایران قیامی علیه…</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/468419" target="_blank">📅 18:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468414">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hjEBJChOK1sIMV0lX2McP9pwAy7a04PGRb0B4RNj1BAbAKJusXIXnnnXe4xg4IIMmn15kA7lFTi9LrgKtQfupqq3-geVjhOs9SbRZ90H_bqj0cJBPHGMxLVRU_X5vEk_y58enGJfL_OOtyeVS6QPaphh-RV9fvq-6Ks2A5FpilB7lN4csu7ywv2KYZAVOgtLXUguQ9dJkgdaYDK6r8l2E7PyGVvtMoJ7hEKolpKnX8UaqSk2yb-rCFdizdaVAplpi6ndRygWUN4bA19kzOXtOB6lj7QA3dbF1e4hwCSWDFylKA_W8SD-fZ_XQN8DN6SelFEzSO1t3bvo-eQZJXfDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHixVwx9Qjc9rOvrrwbFRQK6ur2MKnA2qRvAV0C0qSJAf9TEBjB3uqG3oXcReHWmcH-mYJJObgtIebizqJfPN-cQYzbQv1R3X3jo6UfrSWxXQCFS822i_6tfmQHap1q1U3vfUSDtBz1W1m2HypuowPrON23YWVIHB6YZTTgq18yF_LCtn61Oe35EkGKzsLj4cParNiIy2BVLYO9egUSukU5olyjaAKtmt8H7KHYzTR0t07iD0drw8kPl9E6S9HgG6wXmu0UCn3sE_EhtglFOTnyUmhEwLmMKqkLoq7-XFNNRwuNdauLuZpI0roG24tcR--23yJ4y_SXhyc_YQZAQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M-j8US91-rp1gsPp0U_4kgZ-WPtb14a-TSEle5SspLjF3XCwsq0j5t--yLABA76bm3uIJm4P2NxVnv6B3ryNZ4vMyilUOGTBjkCq9rxABecWokcYfz-K0UppddzJnCMs-fpjCwlNljY6MZjGCmnXh7fUUlD7tDoSSgXrpgEsWFWS1gDarvJBU5rTaTFF937jlDuSe52gAwSoTpCrXfdbhmwYdo-NC584qJcvVI6Crbnxg9esvBWKc2Ia0rCM15Qbmt0Wp0ML8TIpmeN0bJPRgj9C0drcwUY2slfuQWyKu3bG2bpyVSZTAa5u2VGJOe_edJhBMnRPDlM5id3n1L7cFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sYVQC_Zol0EtN4pgzPvLJq3_5c1p7ukoPtt4M15yYHwK2PH0Mn9tCKM4-NqZ2f1q_J3qdPEFewRcHFt2TPaKOP3BohwdGrEoUNeG9jNWwSADAiRWOljYMSnXIl68cRYRaodKmbbiFCEFjkXRU8QHWrqd1UBXqQ3tHPx6n0G-fsTZ5wtaoHTl2WoX30c7DVB6csbVhodIglWHkWASjiVpK3PS0EwLSdnBvrGp1se6TcTKbVx3XssGqxI8LXvtUVxGhJso1ynH_CWCejxxTiq4K6DiWG_6wb376sokwZ0XDuxx3kq4pD5hQ39b8IcKquqibrza4D_q0ynCDbIhIs88jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YTzGKWgz8ZKJrOlFIwn84dwiU-2uyQYtki0qQsD7V9193kxKRfcaw6Q_NN-sk8GZbYbGo-z82yFeFvwOmlCQlChlWI2eaeiapjJWBx0Yd5DLYx5CWwhQi9DWF07zCmlk267bYdCDmiQSBqK8aZs5Ccc5KSTowXhNwoBySmPe9VkvBLPxKuuttA5mjkUDhVVf58FVN7Wt7bzVhUHPJiW8lquK8T6B_mqSOHg4ZrWb5sxG3WVA2sk7q3x2bFXElEARm_7YEicsIlYSz9ZIyEu71olv1n83Y7fZmTNzWF-0XNpyf9BU23ZZQnw1HMsXAfT9zsLeOQmG-lTxH5AKwy7YXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر حضور وزیر پیشنهادی دفاع در منزل شهید نصیرزاده
🔹
وزیر پیشنهادی دفاع در منزل شهید سرلشکر خلبان عزیز نصیرزاده، از ارائه برنامه مصوب این شهید با اصلاحات ضروری ناشی از جنگ‌‎های تحمیلی ۱۲ روزه و جنگ رمضان به مجلس خبر داد.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/468414" target="_blank">📅 17:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468413">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎥
فرماندهی صنعت نفت سعودی تعطیل شد
🔹
درپی حملهٔ موشکی شب گذشتهٔ یمن به آرامکو در الظهران و آسیب ۳ طبقهٔ فوقانی یکی‌از برج‌های آن، همهٔ برج‌های این مرکز فرماندهی نفت عربستان تخلیه و فعالیتش متوقف شد.
🔸
مجتمع الظهران، مرکز عملیات اصلی آرامکو و محل استقرار مرکز…</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/468413" target="_blank">📅 17:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468411">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e41b2f69.mp4?token=h79bamfZpOLgy9p4w148fXkoG8heDtaOChId_mYf90MHqzQmpxAOE1vymDwu5fKevUD1kFuTbrK5cyoXbYuB4ox6NrhN64PBmXTw75JibM4VM_cHLFXYC89Kdlg4BZaC8Hdp3cDK5zzRGK68a2zowN8cR485f_LrzDr8kqlruqNVkdGD8hygypKLZISkVUInM699cBue1xM6g3KDLTtHotMODUvgVnXALRJOCXWjG0k_koo5B_2iSJlhyb-xC9_l1lslEZplwDhHkEIyeiXqO0gyl42QuAUMl1_l7Yl91JziDxWE5TXj-gWb-Z5XF4OKx1038QPn4vSvPuyn_XWNwYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e41b2f69.mp4?token=h79bamfZpOLgy9p4w148fXkoG8heDtaOChId_mYf90MHqzQmpxAOE1vymDwu5fKevUD1kFuTbrK5cyoXbYuB4ox6NrhN64PBmXTw75JibM4VM_cHLFXYC89Kdlg4BZaC8Hdp3cDK5zzRGK68a2zowN8cR485f_LrzDr8kqlruqNVkdGD8hygypKLZISkVUInM699cBue1xM6g3KDLTtHotMODUvgVnXALRJOCXWjG0k_koo5B_2iSJlhyb-xC9_l1lslEZplwDhHkEIyeiXqO0gyl42QuAUMl1_l7Yl91JziDxWE5TXj-gWb-Z5XF4OKx1038QPn4vSvPuyn_XWNwYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عهد حماسی مردم قصرشیرین کرمانشاه در مراسم جان‌فدایان
ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/468411" target="_blank">📅 17:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468410">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1b18ce95.mp4?token=HOZ-rgFnfvE6HQ20JH1Mfa5goQBhcxB0Xoj9Mkf30GY5IX_F9RrDlYjB7wfLy6e6903D02gjkHBDadJQcx7cZrDCXK3bfy2ZM-iz0UPnjW9gFUA7avu31f_dyeou6xldnZaiVxYXH7_vS3-JG3xJPt_aFhxOS8gqFNZhDGtLQyM8ZwVsEkQo0mwi5c4EF2-ydjDgqPjfjEbGAIUhxXGh8eSjm7oIbu_XWrAfL5UoHS4OPUBBmBQFBsRGDeBGWjvxTjJoaT49iM3YuLvEHg5lKXp6l-12SNuhAfJqwqydw4QzH0AcAo9ixx6Wrc6eLGzuaHGPCX0_v53Pu1uui7pe2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1b18ce95.mp4?token=HOZ-rgFnfvE6HQ20JH1Mfa5goQBhcxB0Xoj9Mkf30GY5IX_F9RrDlYjB7wfLy6e6903D02gjkHBDadJQcx7cZrDCXK3bfy2ZM-iz0UPnjW9gFUA7avu31f_dyeou6xldnZaiVxYXH7_vS3-JG3xJPt_aFhxOS8gqFNZhDGtLQyM8ZwVsEkQo0mwi5c4EF2-ydjDgqPjfjEbGAIUhxXGh8eSjm7oIbu_XWrAfL5UoHS4OPUBBmBQFBsRGDeBGWjvxTjJoaT49iM3YuLvEHg5lKXp6l-12SNuhAfJqwqydw4QzH0AcAo9ixx6Wrc6eLGzuaHGPCX0_v53Pu1uui7pe2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عطر نان‌های محلی ایران در جشنوارهٔ نان کرمان پیچید
@Farsna</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/468410" target="_blank">📅 17:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468409">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga9fsWVvFA8BmDxyQOozvlCywqmj5OYOqKq7-pnTWOr6Nhdeb3iHKr0P2iYPJJv9HhqZbVVvunFdOJcFHBeW5rpj0M77tCszGgGMuVarvGxlD_7jmxGAFshLWxjqdU4gVPx6aLAgXuN-24SGcpLwdmFINup-KxPLLAXPPwy31N3Ewr6nyTaQtGMQnrui1P6lqcklodx5yw1-tkjGEUNmL4ZYfICHmC38_9Pe-MbaH8NbM8FMj0bSjTJF8D33K2mEQCGfZPiPEhZ8tzWUOHTCBRp9U6GCgTporHCJkUvLZ55lIy9Dqhkbi96nXFH3JnaXVPkaazlwzklHscpGduODvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار یمن به سهامداران شرکت آرامکوی عربستان
🔹
نیروهای مسلح یمن در ادامه تحمیل معادله تنش در برابر تنش علیه حکومت سعودی به سهامداران شرکت آرامکو توصیه کردند تا دیرتر نشده سرمایه خود را از این شرکت خارج کنند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/468409" target="_blank">📅 17:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468408">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromانتشارات فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue1pQyPnR59VNGAtOngebt_tRNxHPd16dCtTjsOTEtujaU-3ITm32R5-pZqCiqckI2hPbJVH_RsijbYE9YpFobdyjdfiegitbjlxsqqjAqUZfYnemRSW3EQWgCyZUjInQwSSE6UFvqrEl7a7n2pOd1rD29drsrvQ9Drp8OCGDIgGyTof1dG_smef6f6y6SSwwcFP1rg6chj6VC_InZd2xKTRfgnp5nOD1Cw_hXI90nn_JS2AGa9wmjoHxhP1NIhLuSXlHLS7EnjGfm19Cd2pilU_RqxY5qh9Deh4Ux88Pno94flueYgj7CUnEWLiLhDPPYfKuLxNHZolFY2pOHet1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
انتشارات فارس؛ مرکز جامع کتب رسانه
، جایی برای کشف تازه‌ترین منابع دنیای رسانه و فناوری!
نزدیک به ۲ هزار عنوان از حدود ۷۰ ناشر؛ از رسانه و علوم شناختی تا هوش مصنوعی، همه در یک مقصد.
🚀
🔍
برای یادگیری، پژوهش یا پیدا کردن کتابی متفاوت، اینجا را از دست ندهید!
راه‌های تهیه کتاب:
‌
🛒
برای خرید آنلاین روی لینک کلیک کن
📱
ارسال پیامک عنوان کتاب به ۵۰۰۰۱۶۷۶
📞
تماس با ۶۶۹۷۳۹۹۶ یا ۶۶۹۷۳۷۹۴
🏢
فروشگاه حضوری: خیابان انقلاب، روبه‌روی دانشگاه تهران، مجتمع پارسا، انتشارات فارس
‌
✅
انتشارات فارس مرکز جامع کتب رسانه</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/468408" target="_blank">📅 17:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468407">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf7c7a582d.mp4?token=Sak63NXv-d_umMzn8xHbm79IqDCIqcNVvlsz_4AN2hWdoA-1nUKlVGk1XuySfUairYwPoL5NkXJ631qzCYt9tr89krgZCwk8cUpr0BxheFUptgCfu2Husr8nFzec07Kqhh7Rm5oXKZOi39azkAA0Ap2M7P_ys5Q2jOy9pcakvaOd8EJmEfBJw-K7WKP_RnEQM1kFxht3MOGLuRWysUDqqwV16YUIIWnkr3IviO4zTAcxFWzjzTs1pcsYzzW0HttUmXn6aHcTgjoua98XNsqxk4j_lVzhHSHrupmV5B2-seMiX_sPK_nLX6KCWVT7G6NnP-LJAV3oVcNSEzvVDQiIT7j5L15dI-XlThOJrMGkg00PqB9ufqeqH1F2WfC003LKh1OB6o2qfCFMPXJJpHoOpq_BuAxY3Bchlij4xjDLNT4EoFOxbXqLDsUyGl-cVDsgjywHXEUHmSwUn_O8_0BOG8wzT6zJre40LNEgsgQxk_mm5lj3say6QtOpEkE85fq5i5rZtef-f69wssIgOxkVVMazEHWtvA6tmuUWhdpSMKUovn60A-j1uU-G7_rjewMcZeG_Qu0CBvQLj5-TXYScuAUwpbavhL0yxsg4hufQBF-5j-oKOL0kglcN6ZeKn1Zv4x_sjAy-mTEGzKXhVXoYLXnUkpHPngNiUEVEBrw8tiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf7c7a582d.mp4?token=Sak63NXv-d_umMzn8xHbm79IqDCIqcNVvlsz_4AN2hWdoA-1nUKlVGk1XuySfUairYwPoL5NkXJ631qzCYt9tr89krgZCwk8cUpr0BxheFUptgCfu2Husr8nFzec07Kqhh7Rm5oXKZOi39azkAA0Ap2M7P_ys5Q2jOy9pcakvaOd8EJmEfBJw-K7WKP_RnEQM1kFxht3MOGLuRWysUDqqwV16YUIIWnkr3IviO4zTAcxFWzjzTs1pcsYzzW0HttUmXn6aHcTgjoua98XNsqxk4j_lVzhHSHrupmV5B2-seMiX_sPK_nLX6KCWVT7G6NnP-LJAV3oVcNSEzvVDQiIT7j5L15dI-XlThOJrMGkg00PqB9ufqeqH1F2WfC003LKh1OB6o2qfCFMPXJJpHoOpq_BuAxY3Bchlij4xjDLNT4EoFOxbXqLDsUyGl-cVDsgjywHXEUHmSwUn_O8_0BOG8wzT6zJre40LNEgsgQxk_mm5lj3say6QtOpEkE85fq5i5rZtef-f69wssIgOxkVVMazEHWtvA6tmuUWhdpSMKUovn60A-j1uU-G7_rjewMcZeG_Qu0CBvQLj5-TXYScuAUwpbavhL0yxsg4hufQBF-5j-oKOL0kglcN6ZeKn1Zv4x_sjAy-mTEGzKXhVXoYLXnUkpHPngNiUEVEBrw8tiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجهیزات و خودروهای مزدوران سعودی هدف پهپادهای یمن شد  @Farsna</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/468407" target="_blank">📅 16:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468406">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کارخانه اینتل آمریکا در اسرائیل منفجر شد
🔹
براساس گزارش رسانه‌های اسرائیلی، انفجاری در کارخانه شرکت اینتل در شهر کریات گات در جنوب سرزمین‌های اشغالی، ۳ کارگر را مصدوم کرد که حال ۲ نفر از آن‌ها وخیم گزارش شده است.
🔹
کارخانه اینتل در کریات گات که با نام «فب ۲۸» شناخته می‌شود، یکی از مهم‌ترین تأسیسات تولیدی این شرکت آمریکایی در خارج از آمریکا و از ارکان حیاتی صنعت نیمه‌هادی رژیم صهیونیستی به شمار می‌رود.
🔹
این کارخانه که در سال ۱۹۹۶ آغاز به کار کرد، تولیدکنندهٔ تراشه‌های نیمه‌هادی برای سرورها، ایستگاه‌های کاری و رایانه‌های شخصی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/468406" target="_blank">📅 16:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468405">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3272863e3f.mp4?token=Y2sgq-Ui0MJYwXh7oO7m1HOXXuEyGzOGyRSkEg9tc3rYGFe3LPRlMb9OzflPosP0ZzvvxRsLXUhqiZ4QWruF41jbbVq5qLubo5oV6rIjCI8YPnD2my-yPVHDrQ_C39SlesaXD7AQQQKdLKq5SjczS6WFBNJs3Q47b0TM8LT0EjQ3S_zyDekRfO5dyGVcMmWxZ_rppeWlX9cKVoVWfWEInbwycAd9jjdmX4iOI6bEg3SzjQR7W0qtAbjpR4kGJ8a78Vtg3Q5JQh12TzE38H0rZVTCfpQTlskQmkOqnOZhR5BNTwJ54e2axsJFJHdAFJH_7-nhykeQG1n9Bs0lhs77WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3272863e3f.mp4?token=Y2sgq-Ui0MJYwXh7oO7m1HOXXuEyGzOGyRSkEg9tc3rYGFe3LPRlMb9OzflPosP0ZzvvxRsLXUhqiZ4QWruF41jbbVq5qLubo5oV6rIjCI8YPnD2my-yPVHDrQ_C39SlesaXD7AQQQKdLKq5SjczS6WFBNJs3Q47b0TM8LT0EjQ3S_zyDekRfO5dyGVcMmWxZ_rppeWlX9cKVoVWfWEInbwycAd9jjdmX4iOI6bEg3SzjQR7W0qtAbjpR4kGJ8a78Vtg3Q5JQh12TzE38H0rZVTCfpQTlskQmkOqnOZhR5BNTwJ54e2axsJFJHdAFJH_7-nhykeQG1n9Bs0lhs77WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ استارلینک چگونه در حمله به ایران مشارکت داشت؟
🔹
گزارش اخیر رویترز نشان می‌دهد بر اساس اسناد افشاشدۀ پنتاگون، «استارلینک» ستون فقرات شبکۀ نظامی آمریکا برای هدایت پهپادهای انتحاری مانند لوکاس در حمله به ایران بوده است.
🔹
طبق این گزارش، دیش‌های استارلینکی که…</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/468405" target="_blank">📅 16:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468398">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eK1xrZjPvgN76n20FQKYpS6aB5iVKefGsVPivDQPCrtmt6hMbrZ_J8Q2_63C3vDCq7YwrlzByADsA2oB_fuopXjC961Fe_xw52oqCgnQj2DCXP_4RWfYPSKTevaBMEBJjWxhKO7bnpnhR-D0h0MuC5Jm2ClMhvlgPyV7-h5oWIycFptKqKbXMmonQGnGJoNb0cbJUcnSEIr_HGbmNk2K_Dg7frE9vg4tS92kHiTw9-JJNli3nQhp4C0fW_kXqIGg7GiZ4BfmFshc95lPMAye7S7ISnrO0CCyzzm-edyPPMCMToFVT4HrsPmPicF1XbotlPI2NfV2FdlNuL1wkHkLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdIO5CzoROpsPvgpeB473Z7IUE5q455cMBTU9VLQ5UcDM-t-2KTxTIprKXhWCLxxzGbNmKsW8VGzYhE4EzQBpvSV0Av-HdILBedWTwfEsl9X7QP3EZ5An5LXHylWVgVOEosUxKa2qyJH9-5kYB7dtIE6bbUe5WTBuP0dS7wNYL3pdBx-syQ_gqGFfgCm4D1lYXCQD4Xs3VoxjFr4Of1fdbETSjzQIdTHgg3GtyGiVbnIzlIe1gQx8Lx22hbsmS8FZGT_aQr7vpgMjHiyx6_6BIypcjO4I1mHtw4mkpUt0XurwhHy0lwFDD0Ts8E1RmuCYE1hYSPAu11TSaj7lyz9vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkdte265ffHKkovx__Usjw77GrhLMqwo1L7k6YqTmykRxoh0PR94DiXPPGQWkumNiZB752V8Zxubyq4Rd861fMuZoSi2pvC7F3ormX_SKbtKbr2D2IL1aS431LCp1v-gULjCvyJYXSbZF5Q29b44TkAAcJkzESk_Hy9CGHn9As3NZEruu3nPQGOaptE1XJ_4SmvUUDHLIQEZ_JHK4gR3fNhWeLkmaT6Ryd_W8Q35ieKGQHgchpDQUDv4dgq250eRqsn_w3dbT3O46KCk9jLcWU1FhsE0qn-ku_-SKUYVfhOfBN7Httva3-vX8X8MknS1-ht2tnW9Hm0hDAi3VgrfNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3h8_UhL9nYJL5towWdXPdrvjNwzPk22ZGRvpdSfWoNJMBhvuwxV_AdAN3euf5cWmhuvfUOZ7wbrtNqrNhB6VhO6uMI3epXsRyToD-Aeu6_A2u-Ql5EU9-XNuErUENqYtHlAzTTfW66zLV4ouk1ysjdli3rJgmFd3mrt9rVzwyZU545ShP_h4XDpZJMymstmw-ZkRUhQPOKan6qlhmk8n03ZbyJkGnrNCxy7-3fQdIhvQNceTTLiYzQTGOcj_BS_MTygK0-qsMNCxCWo1a17u1NVOpDjU-fi_-hlprs2adsMOGs3axZp0J743TE9Kv6kl23JTFc7WFtUmScWhpS8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRHj_aW0r4mbbwRjdDU9S4NVAhk6RlZ2HaQnIV_GMnYU4-QKaKwfp5nAEah2gNzryBU7YWkQn5_Kv_e-YAnJPeVdhwNtRk1nWdCVPowIYBMPhkUAsNM6WeA_2P5TgH9b9yGcN5JsoFKpAMVZ2sbaQT2aRi87OGO71S6pHUEQISiVfIgBFExXiHcT1bqFuyZARsgCA23YMysyZvPmHBI_p-MGIfbsQUD997DAg3WnXzUJM2pk1HBAMgRcuOCCCJdT3_RyKK5kaCo5fIZeLwBPLdPpD1HUeKrJG6ubEWfUhl4PXf1Cf6VNqOzskySvcpKnwFkzngP_gd99D_NP_ZjrsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dpv9ushtHNWs-RH1vukxtWGrP4OLwoAEPOJlxTuc2OQkHGtyxLWHFjgdy9_vtcW_Bdmq6jkGcdnFK-1ax7OnUeYZ2xjt36_8PzSqtynVsxSMtk2T1DGlygsrBkLrAeGjpMQpYd9H3A8F8CZly7LT1o_2VfjzuNh4dgeKDVHvbz0zibXRGSq6ZtiXUOoAsBXUDo84wLOtHOTx9Oyl5omfVfaO6XwJh-ttQyJjjzIRKtTh2WkSzBExXuNuKtaci8EdhxzYXa13IhhKvVSmMzyeUFUFFtmKyL6VeJycmwe4CJbmg9ZQH0-SZdz8N7fUMp15-8yofA7D6UfXJ7AKUoP-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgNX_ye9chl5RuUpHCLxBqgSokXll1-PScVEZQa97sWT5NdddFGEmBWBS8VFmnsSOwO7QPdibcxksss6y3pWaRBDeKUGHe8MB_7Sj_7LRCBnHerQW5TKVAQvKdj2xsGh8iMKjVdKclsynHAGNpW0iQmvy5Uo5VbRGxchqWTwWVVU-NyrF1FNfABTX5ojqYwqsGtwPQPQLErHuED2ajukICpjV03XDuB5ORWMT0WCjXXw8ai3wk8XNm3V6wJtiVK3vZCdTjHRd87CDG7BzgydIHA4QwxBE9OG7WU1b2jyx6XRLwVpRo6RXl4DN4R51sspNAiTXTv1izNF6GJmvGbTrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
بانوی گرمابخشِ دست رزمندگان جنگ تحمیلی و مدافع حرم درگذشت
🔹
فاطمه فلکیان معروف به «ننه‌عصمت» که به‌دلیل بافتن دستکش برای رزمندگان جنگ تحمیلی، مرزبانان و رزمندگان مدافع حرم مشهور بود، درگذشت.
🔹
دستکش‌های ننه عصمت در سال‌های گذشته به نمادی برای مقاومت و جهاد…</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/468398" target="_blank">📅 16:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468397">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0fa9c476.mp4?token=RwqrUEFqbJxwlZQEo9KzQXym_502NSvzPcWKFBaROARmLNcW3Xngxuxh8Xc27W0nO5mhugUOh2UfrIekL-LvTJh7b8lKgCbBdbjQzwzhmx5-LrGtDZK-qprCXysVBOGLowx9S_LHXVocWfGlwIL7Grd4gQvp6GcdTuA26A8BA5fu-49amzA9BvBiVzHH7Brb1I63wnfp5oBoduVc8I1WceAWVYU_TcqienNr7GjLem5Zq95Jx1PhV70LIChb6A1uP_k2pj50LU9OTHr2hkAxxlxQKB7PZPQpaZQpwcAVwsS2P0FluYqNXd4d2uFzHNxzPSTNVmPFLCgYPyw_8oZ7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0fa9c476.mp4?token=RwqrUEFqbJxwlZQEo9KzQXym_502NSvzPcWKFBaROARmLNcW3Xngxuxh8Xc27W0nO5mhugUOh2UfrIekL-LvTJh7b8lKgCbBdbjQzwzhmx5-LrGtDZK-qprCXysVBOGLowx9S_LHXVocWfGlwIL7Grd4gQvp6GcdTuA26A8BA5fu-49amzA9BvBiVzHH7Brb1I63wnfp5oBoduVc8I1WceAWVYU_TcqienNr7GjLem5Zq95Jx1PhV70LIChb6A1uP_k2pj50LU9OTHr2hkAxxlxQKB7PZPQpaZQpwcAVwsS2P0FluYqNXd4d2uFzHNxzPSTNVmPFLCgYPyw_8oZ7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری دیگر از کشتی کانیتربر متخلف در تنگهٔ هرمز که هدف مین دریایی شد  @Farsna</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/farsna/468397" target="_blank">📅 16:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468396">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5fwV-YmRwsHrOM23upPDUM7sPQ7c-ffDMCpJHNGWmuNKly2RtBC4o3jqWoYoJXTblHcnT4mb48mei1RyxaJY4dhW2UuOdYrx4pJFMyc9Zz3bh8kT0ve_kwQh_xzID2_7IWJK4zHZELgo3eH6zWP863SCc3TasyHq5ze0L30JegZCzxRAAznMak7VM9aZfXduYCSErSCvdwVBd9b_-0COPm3nTj7RE7Y_M6oIZ_WKO6xVMwTJEO8ggFJBxvLftHVQUonMWD5dugd7WQgGTlKRMxmRNLdW8UmHe4LAS2VulT507R12frOJJLjwT0cXfvNGoHTr8Xt_rfc8OpiOUAkeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲  گروگان‌گیر در سیستان‌وبلوچستان به دام افتادند
🔹
رئیس پلیس آگاهی فارس: یک مرد ۴۲ ساله ۱۴ مرداد امسال، هنگام کار در یک میوه‌فروشی، از سوی سرنشینان ۲ خودروی ناشناس ربوده شد.
🔹
کارآگاهان پس از شناسایی محل سکونت متهمان در سیستان‌وبلوچستان، ۲ نفر از عوامل گروگان‌گیری را دستگیر کردند.
🔹
با تنگ‌شدن عرصه بر آدم‌ربایان، گروگان آزاد شد و به آغوش خانواده بازگشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/468396" target="_blank">📅 16:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468395">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e1f81f31.mp4?token=mDkGsZXHlZwPJP-D8W_Tn7Q8KTs2m82tD7w5Z3vxgKJWJXBwvRZQYGZDfaGMUPTVLC8jyqbItKoUvWZAWurgO_JzgRz2Nf6W6PhXyJrLGa519HMODkHIfbgqZc0O65tk7qwnKjisfr_71iqpNQWWUz5vsgxsDgqkz1DZsdBfXP-B0LvRtsuBQLkEPL5oCTgIUZGbN9zhK0S0X-tRY-IpxqGifZRDW-3NvxZuYjKztt9UYNrgXn0y9p9aoJP6EGCge9Yp7fI6OeekTYuGJYmMWE71SBpkawBAfRKUBV05yudCddq91BDrR71FBUPsenEFOdVbcmu_4cwCMu1HS7f-hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e1f81f31.mp4?token=mDkGsZXHlZwPJP-D8W_Tn7Q8KTs2m82tD7w5Z3vxgKJWJXBwvRZQYGZDfaGMUPTVLC8jyqbItKoUvWZAWurgO_JzgRz2Nf6W6PhXyJrLGa519HMODkHIfbgqZc0O65tk7qwnKjisfr_71iqpNQWWUz5vsgxsDgqkz1DZsdBfXP-B0LvRtsuBQLkEPL5oCTgIUZGbN9zhK0S0X-tRY-IpxqGifZRDW-3NvxZuYjKztt9UYNrgXn0y9p9aoJP6EGCge9Yp7fI6OeekTYuGJYmMWE71SBpkawBAfRKUBV05yudCddq91BDrR71FBUPsenEFOdVbcmu_4cwCMu1HS7f-hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آقای رشیدپور؛ باور کنیم شما دغدغهٔ تربیت کودکان را دارید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/468395" target="_blank">📅 16:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468394">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYIIAgw64aysZafuwQOnJB0AKpqEC3Iy5IopGotzK7az2kN3gCRQxQ-LLE1AjaRL07XLlykdU8HtQOWD1AjpHS6u2SlSBN413Fb8hQhBo5YLCrgn1o8z4ow3hVd-F3mud-XKLxPWmQqqGnHpoA6_h-7ADu_-T_O3oeM43-FeMyL2HZcX_DZVM4S5ADzjggTqn6dE6gmRFrvi97NPcc6FAHtU0-ebARDVBxJLb5aBZ2YpJz4fzh1ds_VS2FkOC-fnDuqm0fKRGoYSya2eayE7oMGdIR6Be_P3fYfY2DzTgduiOEDbKaxEEEijep3XWTmSGOOYXumQrvnmKBFg75SSEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمان ثبت‌نام کنکورهای ارشد و دکتری اعلام شد
🔸
دکتری: ۳ تا ۹ آبان ۱۴۰۵
🔸
کارشناسی ارشد: ۱۶ تا ۲۲ آذر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/468394" target="_blank">📅 16:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468393">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سند مالکیت نیشکر هفت‌تپه و کوی مدرس اهواز صادر شد
🔹
سازمان ثبت اسناد: با حل ۲ مشکل ثبتی ۷۰ ساله، سند مالکیت شرکت کشت‎وصنعت نیشکر هفت‌تپه و همچنین سند مالکیت محوطه باستانی شوش صادر شد.
🔹
همچنین با صدور سند مالکیت اهالی کوی مدرس، مشکل ۴۰ساله مالکیت در این محدوده برطرف شد و اراضی مستثنیات سد کارون ۳ نیز پس از حدود ۴۰ سال صاحب سند مالکیت شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/468393" target="_blank">📅 15:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468392">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXuX6JlzcbRktKc5qRGjZ7imKrM_CfmhK1fpYZ62MhW3Hu975etXN-_O9gz1QdiflL9j9RQL2pqTco1_t_q51S8wo3OTUe_fgWg1qQqPoQIfDhsaGWFZuydNygQqeP_FFmvgqb6d_98lix5p3fCgVSbsXB4qA4UmLdpaDi1tmWBQTl_UvOYBU4olCOrb3UbUOquZOeKJovfZg_F4cAwIzDbig8c2OrjCy2mNipbCnvy29StT26KyACTeTGOH4L-kwsSEQunS73G6PJWAqdQCDkfiXdBxwOVgY2GSCfhWxrYGoMLnUXdXIT33gurnreKAi7XCvt_d2o7ym_heQcqOlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم انفصال از خدمت مدیرعامل‌های فعلی و پیشین هلدینگ خلیج‌فارس قطعی شد
🔹
دیوان محاسبات کشور با رد درخواست اعاده دادرسی، حکم یک‌سال انفصال موقت از خدمات دولتی عبدالعلی علی‌عسگری و محمد شریعتمداری، مدیران‌عامل پیشین و فعلی هلدینگ خلیج‌فارس، را قطعی و لازم‌الاجرا…</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/468392" target="_blank">📅 15:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468391">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdVrMEr0m0AmiGpzIxTIbdhFz4ppQQ6ldEH8-KGHRhD99FxqveQ6bk6-5xQCi0v6HQ_-YT8qHe8V70PZ5naDopWgBf7w5q32qFyTGtMbWy511dTTjIxno3h73_hXekEzK7Y8C2dZMZMAUqC9eZyLfMHNMVADmYX9KD_auJkbLP5_cC29nmuX2g7200jDmKQyvhFhRj-VeacYV_zy_FkyZmq9NBxCJtW3E6xEssDrZd29NGFJNGVun_uvGfbs7MI1aFy2zU0qJpaEL4DTcwwmBtXHTctdIWgg4QlrIQdMAXKASnS_oJxahuylRByT9YL0uEjk5kjawwE5orKvhhZkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشکیل پروندۀ قضایی برای بلاگر هتاک اینستاگرامی
🔹
درپی انتشار محتوای توهین‌آمیز و هتاکانه از سوی یک بلاگر اینستاگرامی، با ورود دادسرای تهران برای نامبرده پرونده قضایی تشکیل و برخورد مقتضی صورت گرفت.
🔸
این بلاگر اینستاگرامی در فضای مجازی، اقدام به تولید محتوای هتاکانه و توهین‌آمیز کرده بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/468391" target="_blank">📅 15:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468390">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959217c881.mp4?token=ZXUW_QV6gvKdinZ_pHKrjJ-kQGGXNrpidfF4i5lFl9dK65jS-xiPEpbfOzNcBAtr9PHnQ_VuNUZusVaT6IojxTu1gTqCROB6x-R7XKeXuYFYNBmoDIcpawm-3w3tOGOiHQbtwkOO3XuivprxY5whTuvhFKK2zSQC_Q-0Toe8-QP20TsjD67BIBK6Y9A2xIA4rTYUr1oUM4ces58rKCc811F8-ek-WEYQTWG9YRfcjlHgPTPL29PO6J4AU9ET-5PuF_uH4roIi0s3-pdXaw2KIaD0vvWcxltXc9-Ijg7c78EsF2GxkQUhd-B0OShQy8Wqb5rHVYP_JcChjBxRkDvlYIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959217c881.mp4?token=ZXUW_QV6gvKdinZ_pHKrjJ-kQGGXNrpidfF4i5lFl9dK65jS-xiPEpbfOzNcBAtr9PHnQ_VuNUZusVaT6IojxTu1gTqCROB6x-R7XKeXuYFYNBmoDIcpawm-3w3tOGOiHQbtwkOO3XuivprxY5whTuvhFKK2zSQC_Q-0Toe8-QP20TsjD67BIBK6Y9A2xIA4rTYUr1oUM4ces58rKCc811F8-ek-WEYQTWG9YRfcjlHgPTPL29PO6J4AU9ET-5PuF_uH4roIi0s3-pdXaw2KIaD0vvWcxltXc9-Ijg7c78EsF2GxkQUhd-B0OShQy8Wqb5rHVYP_JcChjBxRkDvlYIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ استانداری هرمزگان: تاکنون موردی از فوت سرنشینان لنج صیادی که صبح امروز مورد حملهٔ پهپاد ناشناس قرار گرفت، گزارش نشده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/468390" target="_blank">📅 15:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468388">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KKMUS2MM401miWqk38F2BhgdT-LABt3tG6ZhXvJEXxuf6wSO1Q4kGn4kYdK4KNn6pmlI0fSJ_u5MAP3r4PdOM5JpNe-gxAbOypBZenWEujqac9VIzvkOYA9hlA7cTfuu7c3-3YPa_VQ5Kiy58Em--DiZxBTxaqcLFtWnBR24fXJSO__NdTzwn6P905ZPyBbZhBOHlfCark-kwBSJ5Ro7NXwLagVXEupfeBL54r4bK-tRh1SVMdf30iFd0kwDRccz7KkMA5t9WXtmPdak-1r7bIhhaL0CGEqs_0N7KmuxTaZXsr300tm1ST8ZedzBDSrSAVr7eMnCcoBTV8CNZEH2ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/li4QfPusC-_Q-pe6BjawaXgViJSutoW6ITpBS5lEsVcGpMR7L74SMkAslW9oOAE6WOJuQ64BPDU5_tBVYGSEuchYByhUhgNr_jny3pE54YQCMe6_MlEDUFrj_io9_xYiVLCj4_EaFe0U1IYE9M3qWaW13g3gcM5MwdGudrORG_6IOvFy9BiswGOGkpC38KRNA8xSjeijUa_ESPVMHWOIC48hnb2xxfY_EiCIVclSEadcNB_Kv8PY2POX1DmDUiBCmJVeVhNh0eqva06q8SveSTXayXPn9XJsloNs1lxxeAzHkH8Ga-pYva-RM8M9kt5pQQJHw2PY1Mqj724hXIfNmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خشم کاربران ایکس از ممنوعیت حجاب در مدارس آذربایجان
🔹
کاربران غیرایرانی با انتشار تصاویر و ویدئوهایی از دختران محجبه آذربایجانی از اقدام دولت آذربایجان در ایجاد ممنوعیت برای حضور دانش آموزان و دبیران با حجاب در مدارس این کشور انتقاد کردند.
🔹
کاربران خارجی با اشاره به اکثریت جمعیت مسلمان کشور آذربایجان اقدام دولت علی‌اف در ایجاد ممنوعیت برای دختران و زنان محجبه آذربایجانی را نشانه حماقت آن توصیف می کنند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/468388" target="_blank">📅 15:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468387">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4914da11.mp4?token=rxi60V15Qfwd4026EcJSHmi2UOoDoRYTYQs2KHj6cT4XY_48J16VIfJM_QeasdjPKSY0czadJzLQ6pb3p3kB_l5haqcfAwhK44Yx3eQZ2QC7ytvbYqusF1NosiBGxvtAUkw91-Xzm6_y9MWtQ2TSNIc1nRPC7niRdnBWY9A-gjD4eSD_B_1ZysbT8IWzPXtkJQLX1flX_9aq12SrAalnVbzd6bIu1y1LNH1uwiQWPkf2sU6_cwbI0pjTymSkhWp5aBlO417c5GUwOgXDIkQyn7ZXiJDyO_brevAnobONxnYoiKYE6X_vk974Vbx4AJNt49g9stAySxQgOwBs1fyMSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4914da11.mp4?token=rxi60V15Qfwd4026EcJSHmi2UOoDoRYTYQs2KHj6cT4XY_48J16VIfJM_QeasdjPKSY0czadJzLQ6pb3p3kB_l5haqcfAwhK44Yx3eQZ2QC7ytvbYqusF1NosiBGxvtAUkw91-Xzm6_y9MWtQ2TSNIc1nRPC7niRdnBWY9A-gjD4eSD_B_1ZysbT8IWzPXtkJQLX1flX_9aq12SrAalnVbzd6bIu1y1LNH1uwiQWPkf2sU6_cwbI0pjTymSkhWp5aBlO417c5GUwOgXDIkQyn7ZXiJDyO_brevAnobONxnYoiKYE6X_vk974Vbx4AJNt49g9stAySxQgOwBs1fyMSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای مشاهده‌شده در نظرآباد آموزشی بود
🔹
درپی مشاهدهٔ یک هواپیما در آسمان نظرآباد البرز، مشخص شد این پرنده از نوع آموزشی فوق‌سبک و متعلق به فرودگاه پیام کرج بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/468387" target="_blank">📅 15:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468386">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/898eecf6ee.mp4?token=YDzLR4j-dIoIydyYlwnC9di0klbkciCR0cALGHd893zEKvFEM4YUE4SnlQ9v_kMPmuE-XOLbwcW7_sl88u_w-Bpx8YQ2yTwa5nf10xa38RySR7s8p9chh2B2BT52kQF8zpethljKSaYESNjQYtzgmwCGvMo6LWnON0lYsHNfddOeLreIkI9XcDavdhkFjdMnZC1305TRZNLrgFmlWiLYHeuG9tVTt1uVQG8klTLEI8ZqZraVD9tscp9rgD1CHXTwkbEaV_0xUf0ZJMYAHzT9-YUsS5oq8UAvTSRENxydjwToFN7oMQUkzc4tRyaiT6_SccZ4yV0VIogVrhS4rEqJGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/898eecf6ee.mp4?token=YDzLR4j-dIoIydyYlwnC9di0klbkciCR0cALGHd893zEKvFEM4YUE4SnlQ9v_kMPmuE-XOLbwcW7_sl88u_w-Bpx8YQ2yTwa5nf10xa38RySR7s8p9chh2B2BT52kQF8zpethljKSaYESNjQYtzgmwCGvMo6LWnON0lYsHNfddOeLreIkI9XcDavdhkFjdMnZC1305TRZNLrgFmlWiLYHeuG9tVTt1uVQG8klTLEI8ZqZraVD9tscp9rgD1CHXTwkbEaV_0xUf0ZJMYAHzT9-YUsS5oq8UAvTSRENxydjwToFN7oMQUkzc4tRyaiT6_SccZ4yV0VIogVrhS4rEqJGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دادستان تهران: سامانه‌ٔ ضمانت الکترونیک حتی در روزهای تعطیل و ساعات غیراداری از زندانی‌شدن افراد جلوگیری می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/468386" target="_blank">📅 15:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468385">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370bd006a6.mp4?token=AZ2so6AJt7frpa_w13nd2mhHUxsUILwLz8ujdG1vIdzuEZXDVyVDKzIZ4IghxMF6FmPcVMpIXO2OBk-EsWfVGiWEEAQHtJAYCT_Ba8Pfm9B_gGkFXz_BV4uMTsEx9AvwuknWxgKcR6UjYQSuO-va-i5SW91tVOob_S5w-sK6PP7LEBPbQTqxVYAhBNdMaIdsJRcAnXZVPbqb4B-gKxE9PmK3XMfoDIKFbGM7kNrbGwOESg-It8eq_gD2RrvztF-Y6fCpAvf2E46l8Z8xIYcj1uC_ZFMSnKYqlaDP0QvmN5EZX8FC3lmFMy5OovfPiDChY9lja0kWwbN8_uCApd5KmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370bd006a6.mp4?token=AZ2so6AJt7frpa_w13nd2mhHUxsUILwLz8ujdG1vIdzuEZXDVyVDKzIZ4IghxMF6FmPcVMpIXO2OBk-EsWfVGiWEEAQHtJAYCT_Ba8Pfm9B_gGkFXz_BV4uMTsEx9AvwuknWxgKcR6UjYQSuO-va-i5SW91tVOob_S5w-sK6PP7LEBPbQTqxVYAhBNdMaIdsJRcAnXZVPbqb4B-gKxE9PmK3XMfoDIKFbGM7kNrbGwOESg-It8eq_gD2RrvztF-Y6fCpAvf2E46l8Z8xIYcj1uC_ZFMSnKYqlaDP0QvmN5EZX8FC3lmFMy5OovfPiDChY9lja0kWwbN8_uCApd5KmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زنگنه، عضو کمیسیون برنامه‌وبودجهٔ مجلس: مشکلی برای اجرای طرح افزایش اعتبار کالابرگ وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/468385" target="_blank">📅 15:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468384">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259d22a2ed.mp4?token=c6HOYfYIUzpQMWM507jwVe6Ymg5U8IeHFsYoM4z6gZoarat5EUF8h5-gbZOa3PQLTSkBs4rFCe1JJG03UxplJQOtdNW6DWdZQTPyouptAhM6lL7m0gdbKhMwfmqTeRUvWCHqPRu7RJb9nxV4-5Vxg8bygODQ-mvgGYXWqncgmKHSDbtcm33A23qOgjKBbxQ8WDFuS-rqkIqWFtcmSs6bdMhrngteYTdW0ldynJjJFBQ3_aXIH8Mq3NKOH2vSFLVmrGlU18bwUIRv1oiaiPvmpPHYZO6Jxf502RCaJjt2ekSi_Yn7adGJoZgjxgbLxhpGqRdRr_gwZ9g85Y7SOqVoUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259d22a2ed.mp4?token=c6HOYfYIUzpQMWM507jwVe6Ymg5U8IeHFsYoM4z6gZoarat5EUF8h5-gbZOa3PQLTSkBs4rFCe1JJG03UxplJQOtdNW6DWdZQTPyouptAhM6lL7m0gdbKhMwfmqTeRUvWCHqPRu7RJb9nxV4-5Vxg8bygODQ-mvgGYXWqncgmKHSDbtcm33A23qOgjKBbxQ8WDFuS-rqkIqWFtcmSs6bdMhrngteYTdW0ldynJjJFBQ3_aXIH8Mq3NKOH2vSFLVmrGlU18bwUIRv1oiaiPvmpPHYZO6Jxf502RCaJjt2ekSi_Yn7adGJoZgjxgbLxhpGqRdRr_gwZ9g85Y7SOqVoUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاهش یک فرایند قضایی از ۱۴ هزار دقیقه به ۲ دقیقه!
🔹
رئیس مرکز فناوری اطلاعات قوه‌قضائیه: با به‌کارگیری سامانهٔ ضمانت الکترونیک فرایند ۱۰ روزه ظرف چند دقیقه انجام می‌شود. سیم‌کارت، بیمهٔ عمر و سایر دارایی‌ها هم به‌تدریج به چرخهٔ ضمانت الکترونیک افزوده خواهد…</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/468384" target="_blank">📅 15:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468383">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1eb42e3d1.mp4?token=lOqaFvLDtcY9z6di3g2PGojpz5taUl-qomXtuUrIHQmt0u3XxNqnTIHM19bu0KX_djrLofgiRee0pMoGDhFFJLlV0MaAFV_Qug_O-IOoJpuDeHX90PFvL3nnlUG_GR4G0q5jhHOWgxG86GjiLh-Idn-Qxaen5Tv11Fae7f7HSjdidJLpQHaWnF8zivZQ7xUkKuuBoz-23BKUPfs03ZIKvlfLeH7dm34YMvLT4w8dfiaqt2-L6jt9-fdutzvO81z1GcvMDaghU1WWuJMXrSHZWQXszWamDU1gHK8d48oNdwZa_wu0MCItLtM3GLo1jHEIMX_goDDu_rUDKMBCCT6KWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1eb42e3d1.mp4?token=lOqaFvLDtcY9z6di3g2PGojpz5taUl-qomXtuUrIHQmt0u3XxNqnTIHM19bu0KX_djrLofgiRee0pMoGDhFFJLlV0MaAFV_Qug_O-IOoJpuDeHX90PFvL3nnlUG_GR4G0q5jhHOWgxG86GjiLh-Idn-Qxaen5Tv11Fae7f7HSjdidJLpQHaWnF8zivZQ7xUkKuuBoz-23BKUPfs03ZIKvlfLeH7dm34YMvLT4w8dfiaqt2-L6jt9-fdutzvO81z1GcvMDaghU1WWuJMXrSHZWQXszWamDU1gHK8d48oNdwZa_wu0MCItLtM3GLo1jHEIMX_goDDu_rUDKMBCCT6KWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان بازداشت‌های یک‌شبه با ضمانت الکترونیک
🔹
رئیس قوه‌قضائیه با حضور در یکی از نواحی دادسرای تهران از این ناحیه بازدید و به‌صورت میدانی نحوه ضمانت الکترونیک در این دادسرا را بررسی قرار داد.
🔹
در این بازدید یک وکیل دادگستری ضمن ابراز رضایت از اقدام صورت‌گرفته…</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/468383" target="_blank">📅 15:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468382">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7fa61331.mp4?token=K17TCm_1gE3Ae-nJOJ0TiRm6ee7yvaKKM83a824tGh8n2RvaTR45eSOZ8r_VmK3zCBxw5g-F3X_yF7y9myDJVcu2fsu67gtNGgHIwifY9uvCb-gnoII-SY2iJfwY2G7sQ6Syt1mdbUNNGniOK1LLa4JJX_V8GoxFpHRSxpzsUYO6uYDzx6PeAoNmbXMw8VI0Vf4HYHwNeqnFqSAOpn8kwXd7N113ZzwKDCoyAJUfXaTBiuBLMYmE6InaroR0BnVWNrXZFkrVlfR_vkGSMtAtHf2B7wwpqs8wU5rAIWy9EVYg4hATadp7SFYhIws4A9K1k93jC3Aqz47vsCZS6cM-rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7fa61331.mp4?token=K17TCm_1gE3Ae-nJOJ0TiRm6ee7yvaKKM83a824tGh8n2RvaTR45eSOZ8r_VmK3zCBxw5g-F3X_yF7y9myDJVcu2fsu67gtNGgHIwifY9uvCb-gnoII-SY2iJfwY2G7sQ6Syt1mdbUNNGniOK1LLa4JJX_V8GoxFpHRSxpzsUYO6uYDzx6PeAoNmbXMw8VI0Vf4HYHwNeqnFqSAOpn8kwXd7N113ZzwKDCoyAJUfXaTBiuBLMYmE6InaroR0BnVWNrXZFkrVlfR_vkGSMtAtHf2B7wwpqs8wU5rAIWy9EVYg4hATadp7SFYhIws4A9K1k93jC3Aqz47vsCZS6cM-rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صادرات دارو روی ریل رشد
🔹
رئیس سازمان غذاودارو: صادارات دارو در یک سال گذشته با وجود محدودیت‌ها حدود ۵۰ درصد افزایش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/468382" target="_blank">📅 14:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468381">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjrOcLM2lEexrRcLxjTdFNhEpPOfXvQv4DwmtI01_njWpzOzwFEvS4jakkMFGTT31GGFl7Uo3zxZrGxFzUHWGXRxaQkGY_PYC3fhImfY9xS_aogqyqkRGTu_I9n9hlEJT6OFhYq6BKOAkROnzrDJFhn2_VuqCmJCYrJopxLBjwF26hSXcwyeGEsHNKvzkqCtJs5qsqzqDRRzCHScafDz62tu_ui8Cdf9kjV6rgitmpya6EeuRXfViVePR6QKMw7ngiZAKKfv-m3ZV10iG5a_DtgqBIboXY1GOlJFjsiF_iCQ0zMsW6YF53IEmW1M0JjWl6lwf_ON_vOmJPHPH_PHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشتیبانی ۸۰۰ میلیون یورویی بانک شهر از بازسازی تأسیسات آسیب‌دیده پارس جنوبی
سرپرست وزارت نفت در بازدید از روند بازسازی پالایشگاه پنجم مجتمع گاز پارس جنوبی در فازهای ۹ و ۱۰، از حمایت‌های بانک شهر از صنایع نفت، گاز و پتروشیمی قدردانی کرد و بر نقش تأمین مالی بانکی در تسریع بازسازی زیرساخت‌های آسیب‌دیده و بازگشت ظرفیت‌های تولیدی تأکید کرد.
بانک شهر با مشارکت در تأمین مالی بیش از ۸۰۰ میلیون یورویی پروژه بازسازی این پالایشگاه، از احیای تأسیسات آسیب‌دیده و تقویت پایداری تأمین انرژی کشور حمایت می‌کند.
این پروژه با کارفرمایی شرکت نفت و گاز پارس و مشارکت شرکت‌های مهندسی و ساختمان صنایع نفت (اویک) و پایندان، در قالب قرارداد مهندسی، تأمین کالا، ساخت و تأمین مالی (EPCF) اجرا می‌شود.
مدیرعامل بانک شهر نیز با تأکید بر اهمیت حمایت از صنایع راهبردی کشور، توسعه خدمات مالی و اعتباری، تأمین تجهیزات و تسریع بازگشت واحدهای آسیب‌دیده به چرخه تولید را از محورهای همکاری این بانک با صنعت نفت و گاز عنوان کرد.
تسریع در بازسازی تأسیسات پارس جنوبی، به‌ویژه در آستانه فصل سرد سال، از اهمیت ویژه‌ای در حفظ ظرفیت تولید گاز و پایداری تأمین انرژی کشور برخوردار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/468381" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468377">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SA2ZebbkmbX1vGiYA7gkYfSz4Jw5slMoIs707qrIkC1un0iHmbNAX5cwJTwY_VH3qACexLEYVEfdLC-47_I5qnAvT_u-Q7dWdD5czRfM-52rkabDdcZ_IP4gx8ndXSo56kAMNyM_iiOYsAS_diVJ6qlOM1euYmVmQSRBmkqq6luxLrNYqKkGnkOMKWJqwyaQmM_AWc8ewg0Uh0uDG2lAprMMt36fROLlaTqjAMGsbBYSRcTAaX1Un-2rO1MjempqE-_hB8LyVpw7ZWKTe580zCGs3EO_vQHVZgZxFI0O-U8ylsjKah9ovBCZGnJs76xtLHxBgRwHI6h_UhHOjRpOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERhs_xIaY8qlNF2GnRSUOShr_Z5PWfbM6PIKeJkFpc1HyYF9XfUiIIY4RQei4C0ZdZAwp-j7O7w7gU1ftv0Hqigyg07XhwF7Iyq7amCxqDmytFOybnkj0pxSsiIMWRmSjKvWreEVes9AZdDB2xM-_utwtgDaqKbvCwbqW8Dpfpt9UE3P1CvCjf2f2_RRuKJj9_ci5i_c-w0yOA5kCMfuw-AXo1Z72U9_KWS0miYYi81drnqj-qKqFikvKaIndECDwU03Y7Psd4LoGxVQ6uT8_kYq6Ari-2gfXp3J-o4SYsyGGZq5IH8Qoam6IdmfufiRUkxnxghE_2oP9ooUZ-cw0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZDxGaW9Ks6Eb2Ur75MNBaELgwLX5hF3pZUOLLc5GWUdRwRstyMzYVoyymZoPChJxFNG5Z22yLGmeDf3Y01vwaNSuT_Unm7WtK0mQD2KAbC3VzUcZwMpqgGucFsIE9GfQejrqYQYiwnBY_cPd58PJRfDvrck53rCfqVVdhPZCs12KDdjL2ou6tQcReFJSBJExFsYZUQVGi-83azhJfPenvYdi3mTCx1c6IpYmkvfpwFO6IEj9-B2z_2CnKH42U9ND4FNoxGI2w6JKmXYyOcYrE9frZr2uPIm7xfDA7tL154UHUd_aulD5l3Z2kwBh70Hd-dHBfw2iV-WFwqWgpiWN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqM37OmcNsh6YZmZOPpaAs7Wo9Mp48WF6VlxTpgepRRckGqNUlNpagyUR7bBy6nfPkOfYzR0QlorB-A2yDOf5mvWcuWRCc62osmcMh6zuwO6d7mQ1oyhdpgZda9sEtGCpdyoZx1wGCO_VLAFVGwIzjzPQGNRLAplV4JBiTD2J2GVPgD4i5zM_LL8ha3mc9Py8J3IwnnicUPXwzbO5zxz4V4rnORQj5bWCw_6lTE1wfOedNirKHqF3N6RCIaQ-6re2qcKt_j8U8zxslRSFW3EdbRDc4iVEQl7rX8MvhbEaAJ-UR-Pk8vxJZEhXva60POVujFNVxbs-WWH3mMwr-fDYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در راستای تقویت ایمنی و تداوم تولید صورت گرفت؛
🔰
جذب ۲۳۳ نیروی ایمنی و آتش‌نشانی در مجتمع‌های مس ایران
🔻
معاون سرمایه انسانی و پشتیبانی شرکت ملی صنایع مس ایران از جذب ۲۳۳ نیروی ایمنی و آتش‌نشانی در چهار مجتمع این شرکت طی سال جاری خبر داد و تأکید کرد سرمایه‌گذاری در این حوزه، سرمایه‌گذاری برای حفظ جان انسان‌ها و استمرار تولید است.
🔹
عباس پورافغان در اختتامیه سومین دوره المپیاد علمی و عملیاتی آتش‌نشانان ایمیدرو در شهر سرچشمه، با اشاره به دشواری‌های حرفه آتش‌نشانی گفت: مطالعات نشان می‌دهد آتش‌نشان ممکن است در یک حادثه عملیاتی طی ۲۲ دقیقه حدود ۴۶۵ کیلوکالری انرژی مصرف کند و میانگین ضربان قلب او به ۸۷درصد حداکثر ضربان قلب برسد.
ادامه خبر در مس‌پرس:
mespress.ir/x6V3
@mespress_ir</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/468377" target="_blank">📅 14:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468376">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/468376" target="_blank">📅 14:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468375">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8bd95a66.mp4?token=Jgus9Ic_wVXaxSbSctyHSyCm-T9czbd0a69UFH-q0eQWTjZtuSyFbN4Hw-NKHOQkThp4stA4OTOgVAQIqXC80W-pPhjq3kEMNv0dACNIegZ3Uq4q2dxqlKt47iuZ0qrYLDi9UzNgfM-bWJcMsPCMgoJUmVYzOXK9nKtX4iFz-EWLu34G8js2jdltaq-MHXGqSQR8XruM-a2Ko3O-xBhdOzRb_yiPhwwGtxuoOrMjTrnGJ5Q_B2qNqmgkxEW4Jbtx7xvEY_44NwJWnB09UcdKtAfF2shL_VjrucrTCsmGevplI2S_XRGRIITMwGwmW6oTXXyPl9OqgDuJb64Uo4MHZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8bd95a66.mp4?token=Jgus9Ic_wVXaxSbSctyHSyCm-T9czbd0a69UFH-q0eQWTjZtuSyFbN4Hw-NKHOQkThp4stA4OTOgVAQIqXC80W-pPhjq3kEMNv0dACNIegZ3Uq4q2dxqlKt47iuZ0qrYLDi9UzNgfM-bWJcMsPCMgoJUmVYzOXK9nKtX4iFz-EWLu34G8js2jdltaq-MHXGqSQR8XruM-a2Ko3O-xBhdOzRb_yiPhwwGtxuoOrMjTrnGJ5Q_B2qNqmgkxEW4Jbtx7xvEY_44NwJWnB09UcdKtAfF2shL_VjrucrTCsmGevplI2S_XRGRIITMwGwmW6oTXXyPl9OqgDuJb64Uo4MHZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم فلسطین توسط دانشجویان معترض فرانسه به‌اهتزاز درآمد  @Farsna</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/468375" target="_blank">📅 14:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468374">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef5a1b7bfc.mp4?token=KfMLhPWImyCgE-g6pcxNL1EA0YdDXTVF9k-ot4LCRRI6rDovU0uyknOtOgApM0SgMcWQEVgaF_geS3jhs64UrBtBP9teTpBNutxWP6nwHYSnC1my_Sk6NXTzahA_lwvJdflXrZSM-yq4AwVJ8tuQ_u7zG5w2wrB_RQG3dJK_7dlpt3cO6fQ_lMV1FTNdU0wWZCB1JDFD1anNNzJEyCre_hlVHvryhpGVYyTdHDgQGvFO0XbMTjs0BNk5jMb-XdmPO-B6Z3-kGEA5wmPM_sE2HYLCNgHuT0mwHrgaaTOvZZTj3XpsOgARdWdQuXqRwav9_ukpeJMVOe4gTXTLaKAduw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef5a1b7bfc.mp4?token=KfMLhPWImyCgE-g6pcxNL1EA0YdDXTVF9k-ot4LCRRI6rDovU0uyknOtOgApM0SgMcWQEVgaF_geS3jhs64UrBtBP9teTpBNutxWP6nwHYSnC1my_Sk6NXTzahA_lwvJdflXrZSM-yq4AwVJ8tuQ_u7zG5w2wrB_RQG3dJK_7dlpt3cO6fQ_lMV1FTNdU0wWZCB1JDFD1anNNzJEyCre_hlVHvryhpGVYyTdHDgQGvFO0XbMTjs0BNk5jMb-XdmPO-B6Z3-kGEA5wmPM_sE2HYLCNgHuT0mwHrgaaTOvZZTj3XpsOgARdWdQuXqRwav9_ukpeJMVOe4gTXTLaKAduw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تروریست برنو به‌دست در خط پایان
🔹
علی‌سینا مصطفوی، عنصر مسلح با سابقۀ چند اقدام تروریستی در کرمان از جمله اقدام به تیراندازی در میدان آزادی و اقدام به تیراندازی به‌سمت سربازان وظیفه و خودرو‌های عبوری در استان کرمان به دار مجازات آویخته شد. @Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/468374" target="_blank">📅 14:43 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468373">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0380c18fc7.mp4?token=vFsWiMZs5s3xQv7uU4FAqbqhT6kliUskqPp7wCv0I2YSEOOMyhVt81DJWzAObT67U8GrUzcUkyPEq-xY_IjZIxJUqGGEJKYcl9VSukYugot-ozF4luuMws8tDHV228PWAFdBc9urdjmhZ5Oo5KRqWeOWWKvwwbP5ID7OkQlNS1qxtKzgsJNijI_dNInRHN_Ugw481GO-EW2XaehZIjcPXyXK9pUxOFc6s6hlLEO6FgHRnbkoF9WB36_gfwLVN3yzDF0w5i91lEJb928eY2912sLHrRoqv_NVfM5y7p9qjv5wxzRzrNXk7H7HK3wgmhQAT3QUXb9WVrjDBHeNnT2d2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0380c18fc7.mp4?token=vFsWiMZs5s3xQv7uU4FAqbqhT6kliUskqPp7wCv0I2YSEOOMyhVt81DJWzAObT67U8GrUzcUkyPEq-xY_IjZIxJUqGGEJKYcl9VSukYugot-ozF4luuMws8tDHV228PWAFdBc9urdjmhZ5Oo5KRqWeOWWKvwwbP5ID7OkQlNS1qxtKzgsJNijI_dNInRHN_Ugw481GO-EW2XaehZIjcPXyXK9pUxOFc6s6hlLEO6FgHRnbkoF9WB36_gfwLVN3yzDF0w5i91lEJb928eY2912sLHrRoqv_NVfM5y7p9qjv5wxzRzrNXk7H7HK3wgmhQAT3QUXb9WVrjDBHeNnT2d2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
ملاک‌های جدید تعیین وسع اقتصادی برای دریافت کالابرگ چیست؟  @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/468373" target="_blank">📅 14:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468372">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59dc0ea4f.mp4?token=lfh_vOM5v4X7QcfXR1RGEVPeHKeDou5J9kixxmnR55CRSgDTxMK32yFfqKBqPf8R5i1mT8QUGFCRvU5bjOFWCN8VwvXXH6vWBWjEk0P-mvAxZJrN_R2wjnwj2H8WFIkAyOVwVRI5qFDFlGlcBismotzNGhpG21MMRLHOQvaYYEalG6lnffhkasgLpX2XXNDA0kZL6hxNhm5fh4kmMsyiZQH97Ul2-D5eceWH60qHg1K15_EAYem09nOuyo4KBBuaiUxfFfu4wTjPkX5LNtspu-YvFF26TanJI6bEfEU1cGOm-NVSsBqadcJiHvGsENECwZXR6j9INu6N3gRlLLzftQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59dc0ea4f.mp4?token=lfh_vOM5v4X7QcfXR1RGEVPeHKeDou5J9kixxmnR55CRSgDTxMK32yFfqKBqPf8R5i1mT8QUGFCRvU5bjOFWCN8VwvXXH6vWBWjEk0P-mvAxZJrN_R2wjnwj2H8WFIkAyOVwVRI5qFDFlGlcBismotzNGhpG21MMRLHOQvaYYEalG6lnffhkasgLpX2XXNDA0kZL6hxNhm5fh4kmMsyiZQH97Ul2-D5eceWH60qHg1K15_EAYem09nOuyo4KBBuaiUxfFfu4wTjPkX5LNtspu-YvFF26TanJI6bEfEU1cGOm-NVSsBqadcJiHvGsENECwZXR6j9INu6N3gRlLLzftQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  عربستان حمله به فرودگاه دمام را تأیید کرد
🔹
سازمان هواپیمایی عربستان خبر داد فرودگاه ملک فهد در دمام هدف حمله قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/468372" target="_blank">📅 14:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468371">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqnhgOYRrERK85w8gCNPse9eh8B9cHFu5aRGhSSn-oDgB0YtOcTQg2YOMoWe6yXcsytaMenR1-Cg1jw5OtGnXJffU_RSqp6MG_mO1DTAKbWUOCxmEtP-5NBlTFjKXzajOTdl-w2kHfgOsb7dasNppV0hqNSgeGOdeKWRHXV6RD7BxFGDCATsjriuvw5dESolOSlxtA3QnbK3KRDvWbGVueE8rIme0_EzNrVr-UUIfQc4-PjR8VuFZQvE_2wG22H9XS0GrgoCSTGyF_JZ_CUHYN321RV37aaxs60PWTUZ6fD0e7nbhKlWQVO7RwFLB-nGfZ-c5s1JFlPWrtW8StI9HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی انگلیس هم حادثه برای کشتی کانتینربر در تنگهٔ هرمز را تأیید کرد
🔹
سازمات تجارت دریایی انگلیس: دیروز یک کشتی کانتینری با ظرفیت ۱۹ هزار تن، هنگام حرکت در مسیر خروجی از تنگهٔ هرمز، هدف اصابت یک پرتابهٔ ناشناس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/468371" target="_blank">📅 14:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468369">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c19a77bc22.mp4?token=LocB1Xd3Gh2ZJVfxjNQLj48xvnEHveT7T2YZyTCC0TUzwyfrshH56BGaYM0-UMVKb81D6dn0S4hzmpQPt-mHT6WJjZN71ax1dtaS9nWLHRhuXO5fxOXhcJ9Nxg_oPrlNCEpSJ58QpizwDDGnAJ0CKZVwCK-CENcbTBPFkSofOEa6ueEDWykYg1wluPydvAqCTyL1DCiW_dJy8pMjVYdYS546ZFSBlhCr4LxtNLDI42k3oiQ2O8KSpCjQAGyRMfDecy2R8h7u_470Vdvyg2E5N2CLqSH01Q0tqKcG6K-XZcwOq8urmADEg9dPDvBUScUQCNhw9-gmNSqjxfQsh9_tag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c19a77bc22.mp4?token=LocB1Xd3Gh2ZJVfxjNQLj48xvnEHveT7T2YZyTCC0TUzwyfrshH56BGaYM0-UMVKb81D6dn0S4hzmpQPt-mHT6WJjZN71ax1dtaS9nWLHRhuXO5fxOXhcJ9Nxg_oPrlNCEpSJ58QpizwDDGnAJ0CKZVwCK-CENcbTBPFkSofOEa6ueEDWykYg1wluPydvAqCTyL1DCiW_dJy8pMjVYdYS546ZFSBlhCr4LxtNLDI42k3oiQ2O8KSpCjQAGyRMfDecy2R8h7u_470Vdvyg2E5N2CLqSH01Q0tqKcG6K-XZcwOq8urmADEg9dPDvBUScUQCNhw9-gmNSqjxfQsh9_tag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویری از لحظهٔ برخورد کشتی کانتینربر بامین در مسیر ناایمن تنگهٔ هرمز  @Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/468369" target="_blank">📅 14:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468366">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vEO-xCUFpPMNatdSZa4cr7qIJ09vxQEpGzd3C0fz9HzcZTvfMWjDNKMXk8Ivi1OV_tC2Ek0WzTZFG3Bfwwg8fCegIpb30MsxBcAzfhOBcNXR3FKnJ_-K9psH-hm9CnbIOJm4stOl7SzanN8ZckgSFbQSZ0ZhXwf3dh0oNZzU1L3p7bt-XO7K4xxDjyv4IFl5BLGD9tPZEcJjuMcZIdjM1wpXj7vPTjD6PStN6sZ5lsPchkaxLb2WNbQ-jdX9Ez9RwLG1Xr8Mw5F3SrusOQ8QZNyZ2Oy5TxVR-eIAVHUQam9QfhtaWk5Zv9UbyuO1XfK-YLzWYXUMYiRMZ6BjB_fMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axatD2zNC0ud7U_mpoFx4OOhhG1uOjm5OavTP4Z03q9UEpm3uBdTxoqxvBc_jnQjKVFMIE6LhsMbbgt6CjyThsu7KoHq3ga7CsRhWN7ZoiD4iA7nHbax_VqDHWg8SuoX_J_XKgK7QbaeZFYJrsXculDcoA---6afwZ-GPRVKltOMmKRjQEPeFieycvOEiU9m6ykkioZnOxkRqMEzRGN0XUTrv8Wo2kZCWo7w6inYGr2TDzs2PAn8Wu5VnyFm0l3NSRHwUOxG-azRqLLqMG8HGxDxoPvFYHr8KGmfgAlEV5Ygk9pMg7YAHy2HB6_ud0666mOObdHQUGk6FTw1Qu9gjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtWZ_HWEsE1Y_eDLpu-wZXPeGkvBW-nfIYgIRjVhouCkPqP-0FcdL6ILu3paL8z_vlocyJM4mjxgir6xhzmjRM63dN8ICgR4jdwoH_U7tKq4a3FeTXWcTYY5S_9q6t_qpPOZ1c9vKljUEO2KqyJR3tt42sSkjfvoEdQbwZ4tUyy2UQgMFxuzWdMmidC31tCHlKonSxEthir-ocIzyur5BLVBHn9cr9u3fmb5dyXmyou7j6jq0VZ3nbDkCYEcVjxDpHJb7ZRuIp8VOQp00HU9i1uu15xUIJDcf3gJW1QQyimuSR9c8gmTGFWbstuLAon18Pulh_0Oc5mG29wCRzaejg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
کشتی کانتینربر متخلف با ۲۵۰۰ کانتینر در جنوب تنگهٔ هرمز غرق شد
🔹
نیروی دریایی سپاه: یک کشتی کانتینربر متخلف که قصد عبور از مسیر غیرمجاز و پرخطر تنگهٔ هرمز را داشت با اصابت به یک مین دریایی منفجر و دچار آتش‌سوزی شدید شد.
🔹
این کشتی با بار بیش‌از ۲۵۰۰ کانتینر…</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/468366" target="_blank">📅 13:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468365">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2709a41cad.mp4?token=c99c78K1xdiZ2SLB1zOtWNlKdyLyy3YoT-Y-ov8Vu7STeUh91aR3MgLslXWfGJR4iLWd6GlYR5XPlepV2fCSd2a7v4LNb0JnQvIejplG_bPpE5soy37JKuJ-qdC6j385DmEgXdrDJb4LZaSnSAsuYXOqFRXZBkJzTOYB1DD5hWnAoQz3sEqcChZg2_w_HFci6ZLTxnwEOTCJ98XYu8D8E--vy2YT7zH7xw0wuDTyLSO3P1EWvr4_8a0jCzoAFvsTBagykyM9YMziCon7k6MYAG6kHK6tbuRU9cxMhavVkkaTJvXAa619QzVEPE47kzM9FB9-4KGeoYK3QPfDhcj8NacmlWUBeOdwnq4CKhRMjJjry2eHYSzbPisyyggUKuKw6Q-ffueXxm3DLouTRj4DWdxgKihE6lkSIselnzgSyser3erKV2R5zClcJcHL2L5TwOTPSPBFyJOUc_EmWfsKcaX57Snr4z7KZm5hnO-k583ic0NNPK_GIS23IRPVKyITRrqbDf9eUH9g-jlAA3QU-dbIV48xwIN9AVGHVnhyjonO6bO0QskJjF4T7ELW7dOedra0HUlZOIgMOzO3-0YZhv9sRdo-C8Y3OyEQBj5G7u3s1Aq6tiR0xlsv0HV9QPvgmVkvMKxHZqMS2XU6lE5N8IjC_fdvLu7mMO2kAexQRTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2709a41cad.mp4?token=c99c78K1xdiZ2SLB1zOtWNlKdyLyy3YoT-Y-ov8Vu7STeUh91aR3MgLslXWfGJR4iLWd6GlYR5XPlepV2fCSd2a7v4LNb0JnQvIejplG_bPpE5soy37JKuJ-qdC6j385DmEgXdrDJb4LZaSnSAsuYXOqFRXZBkJzTOYB1DD5hWnAoQz3sEqcChZg2_w_HFci6ZLTxnwEOTCJ98XYu8D8E--vy2YT7zH7xw0wuDTyLSO3P1EWvr4_8a0jCzoAFvsTBagykyM9YMziCon7k6MYAG6kHK6tbuRU9cxMhavVkkaTJvXAa619QzVEPE47kzM9FB9-4KGeoYK3QPfDhcj8NacmlWUBeOdwnq4CKhRMjJjry2eHYSzbPisyyggUKuKw6Q-ffueXxm3DLouTRj4DWdxgKihE6lkSIselnzgSyser3erKV2R5zClcJcHL2L5TwOTPSPBFyJOUc_EmWfsKcaX57Snr4z7KZm5hnO-k583ic0NNPK_GIS23IRPVKyITRrqbDf9eUH9g-jlAA3QU-dbIV48xwIN9AVGHVnhyjonO6bO0QskJjF4T7ELW7dOedra0HUlZOIgMOzO3-0YZhv9sRdo-C8Y3OyEQBj5G7u3s1Aq6tiR0xlsv0HV9QPvgmVkvMKxHZqMS2XU6lE5N8IjC_fdvLu7mMO2kAexQRTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان بازداشت‌های یک‌شبه با ضمانت الکترونیک
🔹
رئیس قوه‌قضائیه با حضور در یکی از نواحی دادسرای تهران از این ناحیه بازدید و به‌صورت میدانی نحوه ضمانت الکترونیک در این دادسرا را بررسی قرار داد.
🔹
در این بازدید یک وکیل دادگستری ضمن ابراز رضایت از اقدام صورت‌گرفته در دستگاه قضایی گفت: موکل من ملکی در اراک برای وثیقه معرفی کرده که الان ظرف چند دقیقه این ملک توقیف و به‌عنوان وثیقه در پرونده قرار گرفت، همین مسیر اگر می‌خواست به‌صورت سنتی انجام شود، حداقل یک هفته زمان می‌برد.
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/468365" target="_blank">📅 13:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468364">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در رودبار کرمان
🔹
سپاه رودبار: امروز به‌دلیل خنثی‌سازی مهمات در حوالی رودبارجنوب، احتمال شنیدن صدای انفجار وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/468364" target="_blank">📅 13:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468363">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f60420a9b.mp4?token=cM5vVA4965mMPpktqM1gAYlgddwtf5_RdTrT1DM_TbuQMKXpS7RddJP5F87Kkd0UHUrmhf7pE9YZ0BrJzASkolVSEw39WBMFAIc9ydpnx_OcqWh-Pr_GvH18f5eQvv1GbJaVQfsPwGz2gTBWfGECdCuzFYnhnRLTi3EZF_klCooLgIjVvTkLFbILICjn3yUnpB0fT9UCcQNm_J4oxfrdLQ1aYkdQeiSSlAUsxlZGidDpQYpAqKgHTSe6wqwemohhmcIHG4gP3GeL-44NjCXFIdAQ9r2PzOiKwweYzkJMEx1YoocuWNSc-VbV3--DnOQgJ2hnNilTRXMZ_OQjOc6cnGWX7Yd9aGdXfgFLdYkdvUsDbfGJ07HNkBVi4zFWtw0E0L2BE2dDkFNMUm0NjOFLqcXtMCTxuaZ3FsXX0e-vZXWmwJMH8phUR-tehHJROQrBypHRoVN9cquhPrkT1bJrFTYp2jLTN1BV7VxCRFy9uCL-FxiC1UeypQsZGWITW6dpHtJrzLFuIcLa5gGZNw_dMwFy0T9vBvdBN_LWcF7M7dG7cs2hRzTIHHwawu4barZWQT5M9l1vd7kU6QyyQrouF2LrewdFYlqXylrvXF6IbHERDkad6UL0svOT-7kGjar8HHFKOWmxqX8X68lshX2kfpZ7lgHoEu4MAUXutbc2ffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f60420a9b.mp4?token=cM5vVA4965mMPpktqM1gAYlgddwtf5_RdTrT1DM_TbuQMKXpS7RddJP5F87Kkd0UHUrmhf7pE9YZ0BrJzASkolVSEw39WBMFAIc9ydpnx_OcqWh-Pr_GvH18f5eQvv1GbJaVQfsPwGz2gTBWfGECdCuzFYnhnRLTi3EZF_klCooLgIjVvTkLFbILICjn3yUnpB0fT9UCcQNm_J4oxfrdLQ1aYkdQeiSSlAUsxlZGidDpQYpAqKgHTSe6wqwemohhmcIHG4gP3GeL-44NjCXFIdAQ9r2PzOiKwweYzkJMEx1YoocuWNSc-VbV3--DnOQgJ2hnNilTRXMZ_OQjOc6cnGWX7Yd9aGdXfgFLdYkdvUsDbfGJ07HNkBVi4zFWtw0E0L2BE2dDkFNMUm0NjOFLqcXtMCTxuaZ3FsXX0e-vZXWmwJMH8phUR-tehHJROQrBypHRoVN9cquhPrkT1bJrFTYp2jLTN1BV7VxCRFy9uCL-FxiC1UeypQsZGWITW6dpHtJrzLFuIcLa5gGZNw_dMwFy0T9vBvdBN_LWcF7M7dG7cs2hRzTIHHwawu4barZWQT5M9l1vd7kU6QyyQrouF2LrewdFYlqXylrvXF6IbHERDkad6UL0svOT-7kGjar8HHFKOWmxqX8X68lshX2kfpZ7lgHoEu4MAUXutbc2ffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا با وجود افزایش تعرفه اینترنت، کیفیت بهبود پیدا نکرده است؟  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/468363" target="_blank">📅 13:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468362">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سخنگوی سپاه: پس از جنگ ۴۰ روزه به سلاح‌های پیشرفته‌تری دست یافته‌ایم
🔹
ایران در جریان جنگ ۴۰ روزه، عمدتاً بر تسلیحات نسل قدیم خود تکیه داشت؛ اما از آن زمان تاکنون، به سلاح‌های بسیار پیشرفته‌تری دست یافته است. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/468362" target="_blank">📅 13:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468361">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سخنگوی سپاه: پس از جنگ ۴۰ روزه به سلاح‌های پیشرفته‌تری دست یافته‌ایم
🔹
ایران در جریان جنگ ۴۰ روزه، عمدتاً بر تسلیحات نسل قدیم خود تکیه داشت؛ اما از آن زمان تاکنون، به سلاح‌های بسیار پیشرفته‌تری دست یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/468361" target="_blank">📅 13:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468360">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alqpCIuiJnmADLQwuaCspqe0oH1rm2WSMyVHvkKuoxzUsAcT1a3myW6k2DdDdf6cczSE0seIUP_rqKWt03ZxcjBPU7AYFh954bAUGGI6EUdF41Rt7cyl-GKuGFAJ6DhQ2Wt6x0b-k3bQkxvNSZCfPAjonqn-ORtMLBZDvWsaGx_ngFLuVCChnKzlmowiiIl2EYzg3sgKrrqYxlXd-7AumtwZ_9zda4bDqNsPTGjGvZqe7ZwbUOTwA7vjT6sH1K0MHqubgCI-hfSe-crQL0U4K8AIgMdbHPqX00PvFKf2jrzfsGSB2goRY_MBiSl8rjmdJRKWyk8Gup4aTfcD7QVHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت مامور پلیس مهرستان درپی حملۀ تروریستی
🔹
پلیس سیستان‌وبلوچستان: درپی حملهٔ تروریستی افراد مسلح به خودروی پلیس در مهرستان، گروهبان یکم محمدعلی شهریاری، به‌شهادت رسید.
🔹
مزدوران تروریست پس‌از این جنایت از صحنه متواری شدند که اقدامات لازم برای دستگیری عاملان…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/468360" target="_blank">📅 12:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468359">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
کشتی کانتینربر متخلف با ۲۵۰۰ کانتینر در جنوب تنگهٔ هرمز غرق شد
🔹
نیروی دریایی سپاه: یک کشتی کانتینربر متخلف که قصد عبور از مسیر غیرمجاز و پرخطر تنگهٔ هرمز را داشت با اصابت به یک مین دریایی منفجر و دچار آتش‌سوزی شدید شد.
🔹
این کشتی با بار بیش‌از ۲۵۰۰ کانتینر صبح امروز در آبهای جنوبی تنگهٔ هرمز از شدت آتش‌سوزی غرق شد.
🔹
شناورهای بومی و صیادان نهایت ایمنی در تردد از این مسیر را داشته تا با کانتینرهای شناور بر روی آب برخورد نکنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/468359" target="_blank">📅 12:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468358">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kc7zqnw_qr2axrtOi3FlAydbpt-bQAL_oaLFUquO3gFAcRjllimYo5xWxvqWujoPXl-z_jQNdT4MdN3tPBT9YW61i-ruDgWfWV9uDQVL0g6HiT1t3ZNxEAAOXX_wr8ad_FLUZh64EOsYT_zIJfW5B2NA925z3ry8ZdgSt2lvPNZLzHcC9bsOYrt-TgoAk_9S1OEBOIYPLaNWwRrObX_zxKxuOHbJfozW9puOxjqfly2qY-y_2QQM2ufm3wahT5wgdP-qvbBYbVQ0-WX0He-MqJD44pzSF5idNKLnRUkIv0Bcz4Ritg7BjrDsR6j3uUosuyag3GOpFFkalB_PKuFbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت مامور پلیس مهرستان درپی حملۀ تروریستی
🔹
پلیس سیستان‌وبلوچستان: درپی حملهٔ تروریستی افراد مسلح به خودروی پلیس در مهرستان، گروهبان یکم محمدعلی شهریاری، به‌شهادت رسید.
🔹
مزدوران تروریست پس‌از این جنایت از صحنه متواری شدند که اقدامات لازم برای دستگیری عاملان آن ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/468358" target="_blank">📅 12:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468357">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtmOaXOmAmuxKnRojj4ZsyjnjeuAQu8TNKt7FOCPScNBP2Dj3JPxVjjGwLaZayp9VEYhS7ik8ol48PbP0U4yW9_kezHkfNYz8o-FU4SGfy4p_x2OtWRSVwa-48-8GQyPjf3Bz2ztOGdKipeijFevvLEgfm-cYMaVMbpdwvr1O3WAHG-FvSSO4mFeQIDeHnJoVO9jQG8AthLH0oRvnqd7DMtTLzHJGRdF5pyHlVJKvXBnl58WwG2G_tbF7j5Tna3SyyL_FbfQpJ860-H865mgCXrLrYUOeJfbVuQbP9JljYW8X-Pvotz3iH4wo0QaaL0PgF1cEKPhlhVWEvQp9O4eig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس هفته را نزولی تمام کرد
🔹
شاخص کل بورس در پایان معاملات امروز با کاهش ۳۴ هزار واحدی به ۸ میلیون و ۴۲۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/468357" target="_blank">📅 12:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468356">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab6b0238e.mp4?token=stFa6iAYjuRZhrNj4-OuGnwwfreucQhT9OTvssYxkC9v_ok_SeATCDV0RIsdDk1_mGHTpWL1JE5OidagfyhxRBN0Wu4baBGTWxtdFVLLjZc6IWT0J8Nf2LiTT-fA2ZuBEygIVL1pm2dr4L_bwwuVn-vbXi9VeMtLbje9B9yifBA1S4yzMWtgmpausaXZvrrLQxI3QRoQ0oBRy9yybGP6-sncmYz_lmdZrz8_GRvHD0B3iHyUi99klFRPDwlKMbw-rOAVotwIzbwfSFfyg2Cu6zl-aYPE2hwpimmuV2r9PnlhWZMj9_uG2iqAOs3Cyv6LiB8hqI2FK01RgAeixXQ_9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab6b0238e.mp4?token=stFa6iAYjuRZhrNj4-OuGnwwfreucQhT9OTvssYxkC9v_ok_SeATCDV0RIsdDk1_mGHTpWL1JE5OidagfyhxRBN0Wu4baBGTWxtdFVLLjZc6IWT0J8Nf2LiTT-fA2ZuBEygIVL1pm2dr4L_bwwuVn-vbXi9VeMtLbje9B9yifBA1S4yzMWtgmpausaXZvrrLQxI3QRoQ0oBRy9yybGP6-sncmYz_lmdZrz8_GRvHD0B3iHyUi99klFRPDwlKMbw-rOAVotwIzbwfSFfyg2Cu6zl-aYPE2hwpimmuV2r9PnlhWZMj9_uG2iqAOs3Cyv6LiB8hqI2FK01RgAeixXQ_9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرمانده انتظامی خراسان‌رضوی: طی عملیات‌هایی در استان،‌ ۲ تُن مواد مخدر کشف و ۷۰۰ خرده‌فروش و ۱۵۰۰ معتاد متجاهر دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/468356" target="_blank">📅 12:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468355">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru4EEr8zLaTK0TT8DtT2hEZeDmFtKnVJcNFhbgjSyJ_J-4TuOXY0NL0Ot6zONYS7RetUg3Y1JnM-ZY_QGU9qL74tscJhxWKQgfO_ZPnNk7Aumzx0vJJ81ptZ1Jonav_LdUjUiavm2VgYOUMCBSLQlBDTZjB9P9SL9XSZKw1C9IJ8wkhfTc-SNaqDwkAOaqS_sQSAIMlJUX0KtYmO1e6QLV5De4dqFzxNzKhQuPVQxUiAWRRB_qthnYM8_iLKP-F2HlT3kA7atv5iqvogC4iheRxou1lhfpIuWKh_HK_KacfTOSialATQSqjtOYQwEojmzx6hhQtxz1zHPWo31Z4luQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴.۸ میلیارد یورو ارز به چرخهٔ اقتصادی کشور برگشت
🔹
رئیس پلیس امنیت اقتصادی: تا دیروز با رسیدگی به حدود ۱۱۰۰ پرونده مربوط به تعهدات ارزی، بیش از ۴ میلیارد و ۸۰۰ میلیون یورو از این تعهدات ایفا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/468355" target="_blank">📅 12:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468354">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkujOupvLrU-q-jFU0NbC9WDm1Y8rv-SpV6dvnRL2QFWXdRuFu1XOqV-HhnyvSXUV778EQREsTbyQp0g-urPZFNCqX2m-CtfKj3TML2Kg4BPT-szJoOMdIamJogHzcPOM4apceGSj8f4MaiPDxNuTmck_lHNbC7J9Rpw9fPyzNpxsVTClmgbT_8thyQZKQ2DEidIEEoDMQXlTEGT--LZS6n-emiX5ZsnkCJ2nlDrZA0zRcqV0v3Wa8zwFY7oatodsN_MK6j7cNWqPRBtBvcH7pYDwHnQrr6Q3SfvZyfQyTmKt89F6pvEzK_OttZKk-QSWQR6ew55tDP0xEeUTo97SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس بانک‌مرکزی برای شرکت در نشست سالانۀ صندوق بین‌المللی پول و بانک جهانی به تایلند رفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/468354" target="_blank">📅 12:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468353">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4QokXsuALfkUGaTzGS9nAJHZfDrngBiA5xsO1b8Qp4IFs9_I-ZoA1L2Uz4Mam5nqz5HERa_oRcxjpA2_5LPCcEhGb5UTJJKzrP8GjRlRUhDidLkRQbceU-wn_LMh1sTxbFGKZtqycaB98yrHGVe5rmeNEgv2TLBcuQRehRerHa3Khu60vHg4JiTliguSmi_QMV3fDdqz1bwT3K1kocxHC-_TX_FpmOi0GFM-no_4uHz_2AmcUkssX1AbkltLa6bKAQRvvAFWvBIrIYTJnb4voiOnlkIiYRNfqDHOp-7dh7iud-2dqokx5BBprXtTZ8DvEQO_IvhfvPRk_TAtk5iDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
فرماندهی صنعت نفت سعودی تعطیل شد
🔹
درپی حملهٔ موشکی شب گذشتهٔ یمن به آرامکو در الظهران و آسیب ۳ طبقهٔ فوقانی یکی‌از برج‌های آن، همهٔ برج‌های این مرکز فرماندهی نفت عربستان تخلیه و فعالیتش متوقف شد.
🔸
مجتمع الظهران، مرکز عملیات اصلی آرامکو و محل استقرار مرکز…</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/468353" target="_blank">📅 12:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468352">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9582b95da.mp4?token=blaGiNR0j6g0yCaOyErWtk5ha5xyuYpCeUe9H7KLN5jvUMTFb8WWhLXMQNyms61Y2Ndw4PTrOp7lyFO0Nk1RJuCVfC7XysiDYFn4ifI5rFn3VihJlAsw4iMcswvuU0zmRYBp7xK3quyfTBhfv3tIVEDEjkmqADPkHjwlEHPfTR6yi4jybsEYEGEq0nH1p9WOI_vN3nD9Nw5iqu8WK3AqV3-cwGec8NNvQDcf4CYWyNm36E21lXyJw6UiwimBngiyw9XMU8384qYFXwo5AUMKcpYN1yW9KHicZ1oCqXk8-YbnxIC5S4wosv4ddg_Tq16jcJ1CnvGHaDB2HARWF4kkpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9582b95da.mp4?token=blaGiNR0j6g0yCaOyErWtk5ha5xyuYpCeUe9H7KLN5jvUMTFb8WWhLXMQNyms61Y2Ndw4PTrOp7lyFO0Nk1RJuCVfC7XysiDYFn4ifI5rFn3VihJlAsw4iMcswvuU0zmRYBp7xK3quyfTBhfv3tIVEDEjkmqADPkHjwlEHPfTR6yi4jybsEYEGEq0nH1p9WOI_vN3nD9Nw5iqu8WK3AqV3-cwGec8NNvQDcf4CYWyNm36E21lXyJw6UiwimBngiyw9XMU8384qYFXwo5AUMKcpYN1yW9KHicZ1oCqXk8-YbnxIC5S4wosv4ddg_Tq16jcJ1CnvGHaDB2HARWF4kkpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الکساندر دوگین در گفت‌وگو با فارس: انقلاب ایران تمدن اپستین را به‌چالش کشید
🔹
پروفسور الکساندر دوگین، فیلسوف و اندیشمند روس در مصاحبه با فارس دربارهٔ نقش تمدنی انقلاب اسلامی ایران گفت: انقلاب امام خمینی صرفاً یک موضوع داخلی نبود؛ جامعهٔ ایران قیامی علیه جهان مدرن و هژمونی غرب به‌پا کرد.
🔹
این را پیروان آیت‌الله خمینی به‌خوبی درک می‌کردند و دشمنان ایران هم آن را فهمیدند. اینجا نقش‌ها تقسیم‌شده بود؛ یک‌سو سپاه [حضرت] مهدی(عج) و سوی دیگر سپاه دجال. انقلاب اسلامی ایران با تمدن بعل، اپستین و دجال درافتاد و آن‌ها با سوءاستفاده از رسانه و هنر، تصویری کاریکاتوری و غیرواقعی از جامعهٔ ایران ساختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/468352" target="_blank">📅 12:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468351">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مبالغ جدید وام دانشجویی اعلام شد
وام تحصیلی
🔹
کارشناسی: ۷ میلیون تومان
🔹
کارشناسی ارشد و دکتری حرفه‌ای: ۱۰ میلیون تومان
🔹
دکتری تخصصی، دکتری مستقیم و دستیاری: ۱۵ میلیون تومان
🔸
برای متأهلین به ترتیب ۱۴ میلیون تومان، ۲۰ میلیون تومان و ۳۰ میلیون تومان است.
وام شهریه
🔹
کاردانی و کارشناسی: ۵ میلیون تومان
🔹
کارشناسی ارشد و دکتری حرفه‌ای: ۷ میلیون تومان
🔹
دکتری تخصصی ناپیوسته: ۱۰ میلیون تومان
وام ضروری
🔹
تولد فرزند و ازدواج: ۲۰ میلیون تومان
🔹
حادثه‌دیدگان، بیماری خاص، لوازم کمک‌آموزشی و بلایای طبیعی: ۱۵ میلیون تومان
🔹
وام عتبات عالیات ۵ میلیون تومان و با تشخیص رئیس صندوق ۲۰ میلیون تومان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/468351" target="_blank">📅 11:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468350">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFEMLcKLePvpqDOB3JOdM8yxYpxjY5F7CMlrjiwzzFf2g6OeU0ZttlgGsrVSrpQlqjZoxqcOFQZ7F-olhnaUXaH0GMNNHzR_oAgIxMg8V6Qb0yZqUxuouRpO6EPrVtMIYYy7LSft-6nqA6KQ3kAzjlzy8CEXzqkHcqbUT2Yszn8-ahWdaU2qN5yVxgB9uH3n5LN-YvDBHx22m8aF22QToJw8XHH0SOGmRk5WsCBXGaPiMon1UQQnM9Ap5oTpMSJyZMzI_6QYayeppsCmY7GAyBcMT5gFdx8walEGEVB8MCwwmsTzrAvqO4tGMiyawedbZfgAKPwLpax2Y98C_Yfkmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ انتقام به‌هم‌خوردن آتش‌بس انرژی را از زلنسکی می‌گیرد؟
🔹
سیستم امنیتی اوکراین گزارش کرده که فعالیت استارلینک در اوکراین محدود شده و دولت اوکراین نگران است که این موضوع به‌درخواست ترامپ و پس‌از به‌هم‌خوردن آتش‌بس انرژی اعلام‌شده توسط ترامپ انجام شده باشد.…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/468350" target="_blank">📅 11:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468349">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجار مهمات عمل‌نکرده در سروستان
فارس
🔹
فرمانداری سروستان فارس: امروز به‌دلیل انهدام مهمات عمل‌نکرده در شهرستان، احتمال شنیدن صدای انفجار ناشی‌از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/468349" target="_blank">📅 11:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468348">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
برخورد پهپاد با لنج صیادی در محدودهٔ بندر کلاهی
🔹
استانداری هرمزگان: یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدودهٔ بندر کلاهی برخورد کرد.
🔹
براساس اطلاعات اولیه، درپی این حادثه ۳ نفر مصدوم شده‌اند. مصدومان درحال انتقال به ساحل هستند. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/468348" target="_blank">📅 11:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468347">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d0e2ae3d.mp4?token=CWF7bgZXsb7ujg1WA94NHJ-XWTHqnZzxDSnqNTg_DdqZWSf8NBYGJB7EHkND-ts9OgyzYcaubt4jXTFY6qlMnTt1UgXC_wZ_8whuxKyIwa-k97xT26WiXbBdeyJL7gaQkKmD6AnhdZQ__wHVn7R_oyLQGlAVCZfe33gghVXlIY3p8f89YXD6qiJDTr4FYu_v3A0h4-PajvAtgmANbJVOwL3Z3mcPBIKl1si0vYfq3QJMrD3w4frG3_GKhUiSZXIsaf9uCn2t12SwQ6DuZcpyesxtLApwOa2WMFfw73pN50YkhwC-FYDMtV10L7N2YkdSj-BylHtiy1Yb0RuHSYnssw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d0e2ae3d.mp4?token=CWF7bgZXsb7ujg1WA94NHJ-XWTHqnZzxDSnqNTg_DdqZWSf8NBYGJB7EHkND-ts9OgyzYcaubt4jXTFY6qlMnTt1UgXC_wZ_8whuxKyIwa-k97xT26WiXbBdeyJL7gaQkKmD6AnhdZQ__wHVn7R_oyLQGlAVCZfe33gghVXlIY3p8f89YXD6qiJDTr4FYu_v3A0h4-PajvAtgmANbJVOwL3Z3mcPBIKl1si0vYfq3QJMrD3w4frG3_GKhUiSZXIsaf9uCn2t12SwQ6DuZcpyesxtLApwOa2WMFfw73pN50YkhwC-FYDMtV10L7N2YkdSj-BylHtiy1Yb0RuHSYnssw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر علی‌سینا مصطفوی، تروریست مسلح و عامل دشمن آمریکایی صهیونی در جریان جنگ رمضان که صبح امروز اعدام شد  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/468347" target="_blank">📅 11:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468346">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8OCg3Goq2ftZqyA4uFrfYk8peEkc7ZCLzhKbW67LamAyCOJzeZeaPiS5HcvpDDrXxjZsCfLDW02ODtN1ZQUhSHbFn155EcVebasPiiCILBiHCsbt1kvnBq44WiyaekLIW4HjbO3NnrP_eWDweAW_ncs8dw6ACTUvhrxYyLXaVOHlq2O0RuTYwczJaXIK8lXPYy_dp88Zu0qid-ztVV18Vt4yEMac-1-h6RbW79pszSE2bZ-aQqXy8uKJmfJ6p98UGKPmFDOwCsT4QHZPGrops-B6ZwGvKZBMaAI3Lw6p3EAFaPce1eNjKMxsrh0oMQ6IwkvcthNozL4ZVq42XATdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوآوری مالی در سایه تنظیم‌گری؛ چگونه می‌توان میان توسعه و مدیریت ریسک تعادل ایجاد کرد؟
گسترش فناوری‌های مالی در سال‌های اخیر، شیوه دسترسی مردم به خدمات مالی و مدیریت دارایی را تغییر داده است. از خدمات بانکداری دیجیتال، تا پلتفرم‌های جدید سرمایه‌گذاری و خریدوفروش دارایی، نوآوری‌های مالی توانسته‌اند دسترسی به خدمات را آسان‌تر و راهکارهای تازه‌ای برای پاسخگویی به نیازهای کاربران ایجاد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/468346" target="_blank">📅 11:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468345">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">📌
حضور  نماینده ایران در مسابقه جهانی ژیمناستیک هلند با حمایت بیمه دی
🔹
هومن جعفری، تنها نماینده ایران
در مسابقات جهانی ژیمناستیک ۲۰۲۶ در  روتردام هلند   با حمایت بیمه دی  به این مسابقات که در هفته جاری برگزار می شود اعزام می شود .
🏆
بیمه دی حامی قهرمانان کشور</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/468345" target="_blank">📅 11:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468344">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/468344" target="_blank">📅 11:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468342">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9ad5053.mp4?token=DyKMUezSWmqzH_i1pb91EHEMU-CYBrlIE8jHsQphzXYRERF23lE2LNtWGiHpzHYf0DkdJ5Pi7bbaDCAM5CAR-whCiQQ6FExvuQp_rq-Lsl0pr1s7yUrtsIjLMcuI1KJt_sN9_NYPOpdaLGzZQyv1SiJcv0OQHDhlQ95LKlqCEKe_YOjwvZNg0xHhsw4jchuXdRkbiafqHp-WtHIaOaFjx81PdqiuZZgvk2ASCf58rIiS22F9Nv01cAGn1BxIJeCZDolpoO_lHfBsbLTAgC38A7S9p-9icdXTrpepGtPa4mIi8RWhu8DRQFPS76N53HoZvXTROyAGFPIGOtyh01UvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9ad5053.mp4?token=DyKMUezSWmqzH_i1pb91EHEMU-CYBrlIE8jHsQphzXYRERF23lE2LNtWGiHpzHYf0DkdJ5Pi7bbaDCAM5CAR-whCiQQ6FExvuQp_rq-Lsl0pr1s7yUrtsIjLMcuI1KJt_sN9_NYPOpdaLGzZQyv1SiJcv0OQHDhlQ95LKlqCEKe_YOjwvZNg0xHhsw4jchuXdRkbiafqHp-WtHIaOaFjx81PdqiuZZgvk2ASCf58rIiS22F9Nv01cAGn1BxIJeCZDolpoO_lHfBsbLTAgC38A7S9p-9icdXTrpepGtPa4mIi8RWhu8DRQFPS76N53HoZvXTROyAGFPIGOtyh01UvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخورد پهپاد با لنج صیادی در محدودهٔ بندر کلاهی
🔹
استانداری هرمزگان: یک پهپاد با یک لنج صیادی متعلق به شهرستان سیریک در محدودهٔ بندر کلاهی برخورد کرد.
🔹
براساس اطلاعات اولیه، درپی این حادثه ۳ نفر مصدوم شده‌اند. مصدومان درحال انتقال به ساحل هستند.
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/468342" target="_blank">📅 10:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468341">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqsmsd9YCaRDq3r0oBeRUQy3bUa9s6oug-wqUScKg5IbENcHDyG5cdjtiFqO8oamtfjFadSIoGJ8CgeA5ll_KYPL7A49eNZ-BCivEmaoDawdb1g5rvMykBa6JwzAvZzdX4s84IEBfDoVDs3PlcL6fvKyGJYbGoAixDtwcrch_Iu0riU21IvcnTloPrjgXoEM1ED8XYhgecGQMyPObHr9AskwUOTsJ6tCNiOm0z_URxMgMMJhHJEkbTADXblygQCzMr9Pi_jrohmEW03_ff5eSGc3Ym67388BtTYh55eHRSx9Y7z4UvfDI24_nVg0SETeIwUfhTB-FRbdOYfR57M_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: پوتین حرف‌های ترامپ را نمی‌خواند
🔹
رئیس‌جمهور اوکراین: روسیه بلافاصله پس‌از اعلام طرح آتش‌بس انرژی توسط ترامپ به تاسیسات انرژی ما حمله کرد؛ مشخص است که پوتین حرف‌های ترامپ را نمی‌خواند. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/468341" target="_blank">📅 10:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468340">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d875783812.mp4?token=so1cFVzMmqFb576AvFq3VT9S3RulIPxfeIoFDzGZ1Ey8rjCD9cBedyYqlOhVzm3YF3OWHxscuCd3kXvG2Ax4hVlX1h22dHBIUHIsTcrWWpbuIisxs8BDHXuouCfjLR23_NR8z8OAwI3vCKeZgWbRwsOFgcwjWG-hL36NSh-UH1qrgfMA2hXQpSAb7z3l8XWipvYy0bgh5NxII1EWYO005SVPajadBjNC7n07qDVly184krHKyBWzmYJeeOn87c056RP2ye7l9vwN9cgjImvzHIgQXul5jMGiGkiYLofXYpMWlY4i7XHphhDPQ3MIi7nkYg-qGPot3jd7-iVlYbgptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d875783812.mp4?token=so1cFVzMmqFb576AvFq3VT9S3RulIPxfeIoFDzGZ1Ey8rjCD9cBedyYqlOhVzm3YF3OWHxscuCd3kXvG2Ax4hVlX1h22dHBIUHIsTcrWWpbuIisxs8BDHXuouCfjLR23_NR8z8OAwI3vCKeZgWbRwsOFgcwjWG-hL36NSh-UH1qrgfMA2hXQpSAb7z3l8XWipvYy0bgh5NxII1EWYO005SVPajadBjNC7n07qDVly184krHKyBWzmYJeeOn87c056RP2ye7l9vwN9cgjImvzHIgQXul5jMGiGkiYLofXYpMWlY4i7XHphhDPQ3MIi7nkYg-qGPot3jd7-iVlYbgptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سعید جلیلی: سایۀ جنگ باید از سر کشور برداشته شود
🔹
آنچه باید در برنامۀ کشور قرار بگیرد، این است که نه‌تنها به جنگ پایان داده شود، بلکه سایۀ جنگ نیز از سر کشور برداشته شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/468340" target="_blank">📅 10:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468339">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eu2mffYdl5douxRTvj3aPGrc4dOpAg0PtQUIRcxT9ARcKae-rMkLA56NIDIDx8R_mOLpMtodj7FgmRIRXVCA7Znjl9Zas_l9tfe94mNdo7T8m4iVEgaBuKGMlqsMB_tBO8m51BxVyVhLCHnZgj1L3o_lu0EsFHG2xgDx-MNmdbHgnJJcYbkoX78y2jhqLVTCUqyvZHoE2UI7G9eE1tA4aNGdPU0rAaDSaorZxkR_s7aZUeu6Y5RYIpnBjbY1Bzpb7hegxhvPDepcVdGY4eiLu6OJOfsXVyJ1ZzY0JUP6PSjvH4bVZq6b_j1RN3PrlU6-zuGPjnMaFOn_7rbxqpqUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
اقلام کشف‌شده از علی‌سینا مصطفوی تروریست مسلح و عامل دشمن در جریان جنگ رمضان که امروز اعدام شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/468339" target="_blank">📅 10:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468336">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDcr7-rrX5WLuhcPAzSCDzLCAPLpypjIVXbjKf-LTeH_d1QybO27ATLHx00-c6xCSYru4JyZCPvnp2hTknLC0cTcK69TlBujJlYxX_TlxTckO0q6nCd5ej-d3w37v7W8c8q-Rp11qz9B_hjtuWrYpNZM5yueryflhGtkuoYsx_ul_qK1_YGjGuJFLE0cvaaWx8nQpT47oWvGkMXxeFy6zo2_FSSJaG4ig_1dXVLrV0w8QsixtWWIM5cGB-qjQH95NNbsoz_RrEg0kH11rozDIMNERF4LVNK94AKNq9OszsBaCsiiga7qrlPTqlupnXRxGE12oDA6xsjq57ZT-QV1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HO3joU2LzvD4PXCtrBNFq5qooGuxe0VpQpmq0aVzw1Ep-epDm4AvU26FjXyy2WjcyZDSIBsZI7NpTssHpY9N6qaKaQez11wizLf4NvUbqKZD8zRJUQoFbjCFx07rMV5LnNmcK5k5ITgMXZArot4_F9bq4EpSxsqAGeTEIpHVmfh2_AeVzJgGMb_YeuX4pivw7HLe5N0Ifh1Z8pC1kv0jOog2fF2qh1UbkkPMVbQllffO6VVemIrPxIqn94iS6gIb65rgMLJ6A7QLNnwBAUVmRwGQ2_WgGxctdaHKaGfZjsWszPAzBYjr_-ZzJXjp8avguEZuv9PG1dJExklaBctYbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNG0qUeAuCeb_SYLBuy02QsaYNsnW6lgnrjm8Eif7eMb4VA1TxYKhVH93jNR5PVJo1h6bccQGAXIun1fx7sSyTDqFYMC9eG9ATGJMctXNXUWjRDcs-ttu6YsDAyadafoLdUT-b1oUGhf1Ql3ZEsbNjsBopzoRl0S-mOGuszNpG9OmWKc5oCtXRpSwEwcIo8mAZ1i-1_kBY7tDAG3dWynDL2wV3sWDMT0dIQGZrZ3X89rl0ElIqxC7jmtDTZ81HJlOFCNMw8MsqfU2B5cdkq20OfNnvjP-mV2v_BLv13S4wU4IPTZFLficSIRRjdDXrPkI6cF50PZ1gvu6Irhddi2ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعدام تروریست مسلح در کرمان
🔹
حکم اعدام علی‌سینا مصطفوی، تروریست مسلح و عامل دشمن آمریکایی صهیونی در جریان جنگ رمضان، که منجر به مجروحیت تعدادی از شهروندان و یک دختر خردسال شده بود، به دار مجازات آویخته شد.
🔹
علی‌سینا مصطفوی فرزند غلامحسین، از عناصر مسلح…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/468336" target="_blank">📅 10:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-468335">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jt9VMFGDjJw7iKqWt5NlA3MvEL2PMQXAibl9ihQDGQNFH683V57YQ4Lns7Nu_tY8UOrkMv5rvs84xw0g08yST3tjzCYzKTFjI3EwD9ljNyZynK6krswISTdE9O86SZztmSPvT6UMKh0OcZ-eHwQ8KqRJnqzr4UmVImAt3Rj1OmovSHLfKgx_FobZFDNecdm4wBO-ECi0DJj6ie2Wc1Vh7_Rbm12RYwSu55CObbnQfiuWEJhfsyKwkFLLpZan420o2lbWqxECYfCfJbMLrUthDL-rJlz9vrqZV-zWtKim8dShmieA0QLH7jfzDbLfh716MUM2edkaDXfB_DxMUXaAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات اسرائیل زیر سایۀ افشاگری‌های حنظله
🔹
گروه هکری حنظله در پیامی با اشاره به باقی‌ماندن ۱۳ روز تا انتخابات رژیم صهیونیستی، از آغاز مرحلۀ جدید فعالیت‌های خود با محوریت انتشار اطلاعات و افشاگری دربارۀ مقامات و شبکه‌های صهیونیستی خبر داد.
🔹
حنظله در این پیام، انتخابات اسرائیل را «روز بزرگ دروغ دموکراسی» خواند و اعلام کرد که از این پس، فعالیت‌های این گروه با تمرکز بر انتخابات و انتشار اطلاعات مربوط به مقامات و ساختارهای رژیم صهیونیستی ادامه خواهد یافت.
🔹
حنظله از آغاز «کابوس شبانه مقامات صهیونیستی» سخن گفت و تأکید کرد که فعالیت‌هایش از محافل سیاسی تل‌آویو تا دیگر مراکز مرتبط با مقامات این رژیم را هدف قرار خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/468335" target="_blank">📅 09:42 · 22 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
