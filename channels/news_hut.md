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
<img src="https://cdn4.telesco.pe/file/tii12tyDIUX0tYNVbOdNprZNALc3QaI_S2unNAZ9L21VapsfkSipwbXxvhKrncfo_g2jQCGjqRjlS1jtsKijNKHsEBYdpaPdZTttcFwIJ_oRLzDDeZwxMvWrGTaQqpwbUVbA5O-zN9hXSwDgJx-hPmgWongNbmoDpKI-Tw2lfUSsxs7sJvovM_ZvQZQrRKmq429lKt9_mEmcGoGrfZc8BfFsWyTEhixEprGRegjrgyvvWZZRWDdGy_HGDyQOTz4vU2XFhGP58vWonSBrfvPwN9aakEUgBMjsaZg7q6M8ltyX8Qg3iw4AhNKN9zVoPv27jzMKxc_SKkxbcHMS1crInQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 142K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 18:55:34</div>
<hr>

<div class="tg-post" id="msg-69198">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNX_bokSQAccR6kVHVtR474LHqOT503rw5_BHNFmPDgh-9onXXhj4aWTaYYIJJLk4BkUNuNCAoi0ESrGTI_mbG5uYdXIYrkXoAp1m56DaK3aG1PmlwP2bbO_NU3EKuf4dfvjRnALafAdSojIP13HA6vouFLQojtPpJBZ2AAQ24ntS6WIZ3qD_e0008met0oMEqQ7lFkiPll4ydg8oqCOwMaGJXAwyLTnZtSc0Z-gnPFERsFsZu8X728rG1hnBNxmI5LD9rNVeE9x4L21LF54tyAxhtHqP9iTt23U4sQHYh7VFkg_fRCCgnMXgQqA6koJV6qwBnS8Bl6C_aCwdyXl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک‌راوید:
معاون رئیس‌جمهور، ونس، روز سه‌شنبه با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیدار کرد. یک مقام اسرائیلی اعلام کرد که هگست، وزیر دفاع، امروز با نتانیاهو دیدار خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/news_hut/69198" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69197">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MycRyAoWngXUzyWj0oKSRjEdj5Ia7IYP1qltZbNyVIOMuNAYJqcMe6smIG2tHabEUl8DjYhIyHs-uQ9C9y-Z0IO96hquwxW_mVdV8putds-RXuGe8UJQcRf6o8yfYwa2wqbnr4Rh4wpLwtu6h50IBrmfvbs623i0zqP8csCd29jsp2KHsf3XN_yCjT7LHKVM5eVtxGxJdBTTX3Mq88izNe0xZWpKpTDhKxbkU9qe6AFqX33erP-wh4PPp_IQu_PgTd7-nxjlkI3_x0Z0CZPRH6B_wJRcw50twa3whNPwQ1rpDF3IaKh45Efme3dPLmrzzfVXFDvar95UPql_Xg1NHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تلفات حمله مشترک آمریکا و عربستان به حشدالشعبیِ عراق تا اینجای کار؛
- 20 کشته
- 32 زخمی
@News_Hut</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/news_hut/69197" target="_blank">📅 18:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69196">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5BUkmqrRa0MpGi5ErXFKI-wILaVTYNDACrYEzty5lLiIfhJ28SgufF_b0M21RRnsrAM3lm5ZXFziEYt0wakRTbOyhjd3cHDZ8HtfB4VVndnDijytM9DZnpXjkfZ3UZczy3WeQsxDHah8z-20Gi61rDnKBVrjuPTNVqPgWDiWDdSrp8eam1SDkn9It56TYRWe2EhfpCuM_2Al4MMglpBMn5Mxp8lF9cm4dyuKza_KmPlZ8FhQMPLFP3X1hAoDIgJ-xwoAt1htOvI6FKgAQ0U_l0zmKyRjfEU3dHoauQkLoagCDLHW8Wg8U1qpwOS1njgQdxN6PqC0tLsQ7ZRWeNJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇷🇺
پروفایل عجیب پاول دوروف مالک تلگرام در واکنش به تحت تعقیب قرار گرفتنش
@News_Hut</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/news_hut/69196" target="_blank">📅 17:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69195">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=T-a4B4LICphF-fuepJ8qVXVMUJsDcimtEl20oCpu0wYxHEfO_B5GpefiCEx5Oawt18OS3wSgVhZTrpbZWfNtDH-1CxVQsX8nrPPG8TE5JwZaFgn9hs_RKIDvjVbI1_L97SBdKZpdTlwiK_N2YVXRRwCBku50IYWbutlbZDKXwnDvYUlOoadMLnwX7k9ZXrvQGBM_qnp_pr0_5h6iqVpfdXac-kXSk160W3B4a24QsrOmATIyskX-EjLHFK4-ExJedHOLKfy_hEBWFMX3gVv3jdk2-U3WnALVp52wFUBpN9MIbXnWy5N0IY1U9KSPiiI0apYQUAeywlDDsicnTUYkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=T-a4B4LICphF-fuepJ8qVXVMUJsDcimtEl20oCpu0wYxHEfO_B5GpefiCEx5Oawt18OS3wSgVhZTrpbZWfNtDH-1CxVQsX8nrPPG8TE5JwZaFgn9hs_RKIDvjVbI1_L97SBdKZpdTlwiK_N2YVXRRwCBku50IYWbutlbZDKXwnDvYUlOoadMLnwX7k9ZXrvQGBM_qnp_pr0_5h6iqVpfdXac-kXSk160W3B4a24QsrOmATIyskX-EjLHFK4-ExJedHOLKfy_hEBWFMX3gVv3jdk2-U3WnALVp52wFUBpN9MIbXnWy5N0IY1U9KSPiiI0apYQUAeywlDDsicnTUYkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.
هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا رو گول زده و برده خونه
⚠️
ویدویوی کاملش ده دقیقه‌ست اگه خواستین می‌زارم ربات ببنید
🔗
🔞
مشاهده ویدیوی کامل
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/69195" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69194">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czrVqqFWjtdfPIgvGzUiYT2jcyD1s5TLFmmPkm42TnjfI3rs6JajebJzsPcpC-zVl_8vnxNqhhuUGTYZccnRuxDnuDRpqxNSm8DVj_Q0zS2IfnEJDTRDr8r1w74QTvxQ3s81LnAhO0EO_EYzbcwRjdDFzN7AeXJMEcyk3xbeHUspQYy7YJ664jEmAAluQxm7wl8hGLIcHVkZnfZFxjzjifkuIpQeXJZ_sjvEuCWbVV07cmxd9o-hO3djJz32czoa15uf0qq-kvbZu7lRjTP81GQY8KQD_9wsX-msG_pM13irT1zFJHpos57jbc6Spqr7Uw0ls5nn-VoDE3VFJdzL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی ارتش جمهوری اسلامی   اعلام کرد بقایای پیکر امیر سرتیپ خلبان مجید کاظمی یکی  از  خلبانهای  2 جنگنده سرنگون شده Su-24MK که توسط F-15Q های قطری سرنگون شده بودند را در خلیج فارس پیدا کرده است و از سرنوشت ۳ خلبان دیگر اطلاعی در دست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69194" target="_blank">📅 16:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=o0hf31UDR4vAvJi8fWk4DKLiOirMAlhmlS-Apq87P_6q_W6JatOfbv08I3i7d2l4wcq7l-jJ4iZ3nEJY5Ity_nQuNyv3lCzr7uDERsUS2LfaESZ4TxdV6Pt73pRKec4GCGpr84mr_Zj1BYO2PxvaupWGpGmkmXRVabUGWvCfXUf-3ri8xYPn2L_AGNWHsFCHsBrcR2Vtnfxqv14DeDQ3xBuJT6vMsesN8OCfOY5uelGpF16hC9DZ7FC2DS6Z-33JnRo2afu3cqhoWj3jycEv7eGQ6kEU-gqmydCtRVADugdrxA73dgfy5mYcklJLIuqFcHDw5mdXJHbCcBDFA19c_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=o0hf31UDR4vAvJi8fWk4DKLiOirMAlhmlS-Apq87P_6q_W6JatOfbv08I3i7d2l4wcq7l-jJ4iZ3nEJY5Ity_nQuNyv3lCzr7uDERsUS2LfaESZ4TxdV6Pt73pRKec4GCGpr84mr_Zj1BYO2PxvaupWGpGmkmXRVabUGWvCfXUf-3ri8xYPn2L_AGNWHsFCHsBrcR2Vtnfxqv14DeDQ3xBuJT6vMsesN8OCfOY5uelGpF16hC9DZ7FC2DS6Z-33JnRo2afu3cqhoWj3jycEv7eGQ6kEU-gqmydCtRVADugdrxA73dgfy5mYcklJLIuqFcHDw5mdXJHbCcBDFA19c_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=axBO2XWuaCc8uJ1rkPCrz8s_6Yo1TVdnQWZofAQIpAv7PLv9-fzqKGda0HcQ2yyvzcd53FLDbe_RBbtu2gHO4j6Yz6y8gFLtuI13YddLgmxzwv5Ut5uENZ9fNEHtStj97aBz3pIX5EZCyOdWouPwbHinzvA3y-Fr62UQhCA7gJmGTQL6FiBUUs-_Ugl8iT9G3ehTKJGsvMp_yNEkXiQIQ-A-1JU0sfUWtf9gknRMh77DS6MzW3afgFbrb8LIKqFOccGYvy3xmDgOqG08qSl4u74JsZZEWQgvJeZ6jZaUqgvwkp0-1OF0_Tc1vSQXtyP3NiSHbRkmdwGF76nLaj49Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=axBO2XWuaCc8uJ1rkPCrz8s_6Yo1TVdnQWZofAQIpAv7PLv9-fzqKGda0HcQ2yyvzcd53FLDbe_RBbtu2gHO4j6Yz6y8gFLtuI13YddLgmxzwv5Ut5uENZ9fNEHtStj97aBz3pIX5EZCyOdWouPwbHinzvA3y-Fr62UQhCA7gJmGTQL6FiBUUs-_Ugl8iT9G3ehTKJGsvMp_yNEkXiQIQ-A-1JU0sfUWtf9gknRMh77DS6MzW3afgFbrb8LIKqFOccGYvy3xmDgOqG08qSl4u74JsZZEWQgvJeZ6jZaUqgvwkp0-1OF0_Tc1vSQXtyP3NiSHbRkmdwGF76nLaj49Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZNIaNZz0Oy6Lm9J6RG6BdrpZiRj5dD1OBhv766NuxrZKYvBWbcR4Nn7TOZIXz5yusN3Wvr3s3rYY_al4h1kQtitZvIJ5vonjj24XYBBVKFSEOdOmJCJFmmG6TXVBRbeUqFW0w8CVTktKgmrYz6NBe7cLO4Zj7FAtaw_HFviIf7e9KM0M2VSmK8avbf061BeDV49m1j854gIw0ca1QTSoOgE_f1S-GBOu56YEExnqo-iGk7-4N_XUKxPV7UxSXV7mRjDoGACS2pbZsp-uooFFSijSa-SDgdAqIuCSWvzC4NxRKRHrYlmsDu6dbOVv98pkGsQlptRwmbz5nmxkUB-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=rWvjkMjZH_yH8hutcze4z4ihEwq0mTWfe87xGKHgpRpJYwmXD5bFK9iZT7fiP5pMmTqB5qdGK75YcP-W4_ha4ety-QQfTF_XQlj6yYLqI_gd__SLlt7y-1BiNVL-iNLihVAGRW744RpIDSVXfbVzhlKgw7IXCTUFYwUZVw77R_wrWzuPeFc_cDvgZCTUbpCck7Eqjw1ZCU9tf4qUwZWjIMNRsVJTsX4374Zm6r_B3ASkYTbK8zzU67llcoaYHyhSEwYTFnrb3sv6u7uSFMbj_4tPr2c7zUDR18fmhNdcw5rzvR5Sd_GiYrHGfyzJcJgDjqX1sc1ZdxDiQd-XmfZnBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=rWvjkMjZH_yH8hutcze4z4ihEwq0mTWfe87xGKHgpRpJYwmXD5bFK9iZT7fiP5pMmTqB5qdGK75YcP-W4_ha4ety-QQfTF_XQlj6yYLqI_gd__SLlt7y-1BiNVL-iNLihVAGRW744RpIDSVXfbVzhlKgw7IXCTUFYwUZVw77R_wrWzuPeFc_cDvgZCTUbpCck7Eqjw1ZCU9tf4qUwZWjIMNRsVJTsX4374Zm6r_B3ASkYTbK8zzU67llcoaYHyhSEwYTFnrb3sv6u7uSFMbj_4tPr2c7zUDR18fmhNdcw5rzvR5Sd_GiYrHGfyzJcJgDjqX1sc1ZdxDiQd-XmfZnBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHaZ4pTdSy8L4GDtzgq4GnqLZhHPz0n8DygUwG-GZjHu90UeeXueUQf1FbK35nA2hz4WnU2e7MS9NPvbrPamhfVP8FBnsmSAjmqsFmejPSur9ROAz3ynT_T8O58XYYWelTFf3-OLRdvQSqDQALz40pq9XMRLOB5ErZUseDcQa97p0F_R-_LENZrL0VYP-1NlEZjbbjiyWP3WZObfwCcRtLJ9JNgsJDprDUJpT5q0S0BNALmi_cU55E6SSf3U_EPblMYThI2y_u0-IDXW0Q721w_aTjxipSy--jD9A-IW0QM5aVCunJ1z69KunBYP-PoQd0MNtbS1-odawd_NrXRVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuKddmUeErh1O8tH7ywLcdMiQPhTBbnMySB2rxAqxlp9L4xDfHda4E4xbc4YpyHJD37ue3W7S89RalUt3pLDppSgygmzcHUAvY5Hfu59iFbCl2rB-hKpOrugDMJOgI8aM15kZpxIwDRV8j1md-Su8dxcuD0ajhmItndLImYahpWcHIkxmOcDdYFGNTFwGYf-D51VlshM6GF4rPUDWHO4FMSW76tMNJdbsHThIJA5Ei70qtz4rIW8YOuI7nWcZA90WFbQAgYy3I__EpwvOwArZOTOSdrcdtfAV5HZucp2iQXuThxKyz9luc9LxAqXWRXnixpWtJxoKNFVyawPN0vY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=X2996PbZI241PaIn25W1YiTQPgIDmu2uJGDsM5ATid3YVhcTMxyFBBk9SpiAZ_iqMIQDOb6mLm5yMQyQpshqX0vpMWiUvR8Rf1MQmcXqIDg0gGwXL59Y0xJzMEHvWu9sAEeWXJoPa_DiJuZXG5j9qGFavj90O2Z4_B7ECM0wnenmK381cihqNm7mFHpJDxoigK03cfULKZC_gSM4ayOEv09_oC1kMZ_qebWDxk3ISeR09kV129BCao6fKABL4q398JM48RnGN6MuQ49oF_4KpqXIUsR47wIdke8r0oNfLCeMPvfR-DVd82qQWQ3hCw3DAeihZf6QO3nRDTAiDcCVxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=X2996PbZI241PaIn25W1YiTQPgIDmu2uJGDsM5ATid3YVhcTMxyFBBk9SpiAZ_iqMIQDOb6mLm5yMQyQpshqX0vpMWiUvR8Rf1MQmcXqIDg0gGwXL59Y0xJzMEHvWu9sAEeWXJoPa_DiJuZXG5j9qGFavj90O2Z4_B7ECM0wnenmK381cihqNm7mFHpJDxoigK03cfULKZC_gSM4ayOEv09_oC1kMZ_qebWDxk3ISeR09kV129BCao6fKABL4q398JM48RnGN6MuQ49oF_4KpqXIUsR47wIdke8r0oNfLCeMPvfR-DVd82qQWQ3hCw3DAeihZf6QO3nRDTAiDcCVxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuQfLyQa76fPWCwu5JFDBEu5ufsePzg4B0sWoEDceRPmUwECyevkcubRKElyU6SGU5BAHaDr5hmrB903DBXj59UMQ0C-1Efdra_bQrL6mY-MxxkGmIP7PTkLOfMWtDNdhbpcypfnnXvVndXtww5NtSHtc4Hwjjh5exkFNnATEB_N_NDZ5LEQvBKeS4idLsxZ67YE43o80pqGHzVU9YMLfWcAZPA-QjIWGJZv7qee55fu1OwkFgNK0ofZy6bt8DkdQsxlrgZRrQOMtMZdYR9PwVCSyPfSkrRx3xA4Y0253zKmp2mJ_sX7ZfFds1dmXiw8XlPldr6PO5lG121PJ40ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f04q5kr_inKjUkXA-fAxRCi0JXJ8pFOnyfaxpcUVLtAEaapfW6xO1J-ybL8cy7MV61pV1JjZYBX3_spztVUk4ry2-YukezZvrzcrmILosGPB30bOq99FFnpAbtWeB_FnibaePcLA8ou8LplY6mL6WE21iOUTs2c9XBmgM-dICtCsVKqOHhyElA7Iw2HWO3ljXLNOJa_hmLcZBtsghbWMwsl7kjL__FRCH_D-DFw27yZbJpe668F5RC59DMEFkxscUy2Z5PrKjkRH3aQBNPP3QhzrcObB4NuYt-ekpZfJQjsOQOR9SR9ruT6Y4R3kruCnCisqmYDap9SnsURVsSW1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=nDyxe39lrg97YNMLWT-XY4i9OL0qdyr3HQPxFyBLWRxyA_aDZTHgDCyD-xs8FVw9JlNU8DbaWLBuFfnpqlVCwK0DLJFBTXQheGw6KhqokszQgWYtPebsw81arUbh6026juJHHP9aBrSodnfDn7qF39TfIBvTVLte5Zq0TOz0Vw1rxwNww_eFLCMqJjsrT-rFOO-z-JarDrs9RZbjABfS3gsT684JtRgh_42cicc2DteDs-mRYD2muRkc34BOEv30PnPhXJh0ICGcydeTBwXYm26pKz4hOE5h9IfWtlPv-7UQtbyVhDLWlYsOxK7WhWbrGPoNF_k2AdXsTFnk2jnV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=nDyxe39lrg97YNMLWT-XY4i9OL0qdyr3HQPxFyBLWRxyA_aDZTHgDCyD-xs8FVw9JlNU8DbaWLBuFfnpqlVCwK0DLJFBTXQheGw6KhqokszQgWYtPebsw81arUbh6026juJHHP9aBrSodnfDn7qF39TfIBvTVLte5Zq0TOz0Vw1rxwNww_eFLCMqJjsrT-rFOO-z-JarDrs9RZbjABfS3gsT684JtRgh_42cicc2DteDs-mRYD2muRkc34BOEv30PnPhXJh0ICGcydeTBwXYm26pKz4hOE5h9IfWtlPv-7UQtbyVhDLWlYsOxK7WhWbrGPoNF_k2AdXsTFnk2jnV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=dNMPk1r9DhONkAz9W9O30NEI1dsyiaCgaZb4MSXO3DVzljop7c5ANlkcnEXyILDEf2c_PlTU1idyP5VNkx6UBf5cRJHhcKm1hQAzmqsCFkGVUE2wxzFI3C7pnjTNMO-fHVD7Zqt116yu_CcFoygO8p1l9qu5wzCVnWsjkGnw9yM_gHy3VnOUR2RiWoLU5slgc9V63yKQGqbllD7KbmMm9eq4JVSv48pCCNVw3ZgKlXHax3xRxIov9jfGGssn35i7P1anCTDRBOBlsuDKyaG6MoWEaVZEMehjgzOpJvb2Z1BMk1qVi-r1YXyZ95Hlbh6P0dnQheXz2NEHGiYO2T3ONg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=dNMPk1r9DhONkAz9W9O30NEI1dsyiaCgaZb4MSXO3DVzljop7c5ANlkcnEXyILDEf2c_PlTU1idyP5VNkx6UBf5cRJHhcKm1hQAzmqsCFkGVUE2wxzFI3C7pnjTNMO-fHVD7Zqt116yu_CcFoygO8p1l9qu5wzCVnWsjkGnw9yM_gHy3VnOUR2RiWoLU5slgc9V63yKQGqbllD7KbmMm9eq4JVSv48pCCNVw3ZgKlXHax3xRxIov9jfGGssn35i7P1anCTDRBOBlsuDKyaG6MoWEaVZEMehjgzOpJvb2Z1BMk1qVi-r1YXyZ95Hlbh6P0dnQheXz2NEHGiYO2T3ONg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTGZyj8yLFc8tJ52ej5C2aIR8eLS-flrwkPArKO1nSj_64cv4J3N3ErQe_vXPXoCi4qRYRny3BtG1rKgaYy-76M_8tw1f5ltJctqAD93n6f25xJ4uMc2jaaN6kZN_U4qPRlUUVitfqqnKQ6uCAvOzmX1AHEQ10HT5PMCm1SYJ3G-eagNmpy40PUF8HCIzTslbcimV-RyVrpQj8WRdrVMme4ZelcwGu-rGXI1E9DPp-CxpyvSWwQk5tSibS53hWDN2iJjymLwfedb2dAVcKgxpJy3ypwHJY3DKva93lCd6rtxRHPLdKrpoyu80f89m3rLN4oj-ZpUdhWPUM1Uv33MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=LdQwf-7_WLo0HfB4aZ7XDGfxyval--2h5GEhbyHgBO9sZ-gQsD_cMfq2QkdFGl5ShNL0wVwDXW1YHLFa-Nklqkfi20-GN3x6ZB5vVX6ltOZSDlEp1JzlWWNYAHbX6DPXDjau7wwnBgQfcV3xA91H2kqZpFq4dDjV_tFXpLpDSuURiCESbk8I3sOaUEt0xyTWOBARpCqo-Z-bBv2XAic7XnpAinSnStwUoabommEtUzyOKhU2JRcNJwZqQKTgxCkJ4wJSw8AB27znQ1ahSvlwhT5c7AO8laEVDWit9xVVVpf_wXFpjO5MUxBKiqgDnoOKbA_qLfNd83gYUoUjusN1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=LdQwf-7_WLo0HfB4aZ7XDGfxyval--2h5GEhbyHgBO9sZ-gQsD_cMfq2QkdFGl5ShNL0wVwDXW1YHLFa-Nklqkfi20-GN3x6ZB5vVX6ltOZSDlEp1JzlWWNYAHbX6DPXDjau7wwnBgQfcV3xA91H2kqZpFq4dDjV_tFXpLpDSuURiCESbk8I3sOaUEt0xyTWOBARpCqo-Z-bBv2XAic7XnpAinSnStwUoabommEtUzyOKhU2JRcNJwZqQKTgxCkJ4wJSw8AB27znQ1ahSvlwhT5c7AO8laEVDWit9xVVVpf_wXFpjO5MUxBKiqgDnoOKbA_qLfNd83gYUoUjusN1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=cutrD9X1GmzNSmEU4egm7NtBEhZbjJs8y3HQowJ6yzAqru2-HWbFIMj1a2A3s_AA1KGSu8s3MP2woU5veP-fxp3zL6eO7Z7djylipZQAtvEmTHkz4HV4pWmaS2e-xdhmpVikoBvbI7uJb8Q3LFpZ7su8s4z2V1tkO8Mh2CaPGI3_zvmXzCXAenNyGqptaXVbdK29ahdU43e8wwEM2QvP4elbFPiR4P9vVBr3VUV8XDGi1F-J86VU-G1Cl18vlQBpMjtPqKESNvwZcbFOny2Y_UNdndxQffPp4rGx-s_DhlB_viD1yjkaiDLT-1ZJGfpdwLB6NcJGxQK4VhzAJb-VNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=cutrD9X1GmzNSmEU4egm7NtBEhZbjJs8y3HQowJ6yzAqru2-HWbFIMj1a2A3s_AA1KGSu8s3MP2woU5veP-fxp3zL6eO7Z7djylipZQAtvEmTHkz4HV4pWmaS2e-xdhmpVikoBvbI7uJb8Q3LFpZ7su8s4z2V1tkO8Mh2CaPGI3_zvmXzCXAenNyGqptaXVbdK29ahdU43e8wwEM2QvP4elbFPiR4P9vVBr3VUV8XDGi1F-J86VU-G1Cl18vlQBpMjtPqKESNvwZcbFOny2Y_UNdndxQffPp4rGx-s_DhlB_viD1yjkaiDLT-1ZJGfpdwLB6NcJGxQK4VhzAJb-VNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=vGImj1bxQvz1NswauDzss8GvC0-XWz6d7Dnwqd9U3F4ZsEYO-2hWV11zup654ipLncBKax2BhRDHV7DBuKjiFY1XM6LbMpxVjMD48W7L9P8ETXN7qUXsGg-1nPXK3ofOnsJhrCWHRPFBX8gUtaZ56V15G3-KfVo_AwAkLkQQzLBsmM4BjdZ1asWTIGaGLriMxABCFyKI7uA9d-lQ04lQXc9ZhRqBQ7SBDxwHJF39a88Z8MyfXCeNp8sPSUFulZjIlh2vHuqny2y1HA4ET6yzAqGh82QqTU7J9JwzvRI86HVMQLoejKWtuYpCnZ9H9J_6UKiLeAwSn1ycBH6DqrLuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=vGImj1bxQvz1NswauDzss8GvC0-XWz6d7Dnwqd9U3F4ZsEYO-2hWV11zup654ipLncBKax2BhRDHV7DBuKjiFY1XM6LbMpxVjMD48W7L9P8ETXN7qUXsGg-1nPXK3ofOnsJhrCWHRPFBX8gUtaZ56V15G3-KfVo_AwAkLkQQzLBsmM4BjdZ1asWTIGaGLriMxABCFyKI7uA9d-lQ04lQXc9ZhRqBQ7SBDxwHJF39a88Z8MyfXCeNp8sPSUFulZjIlh2vHuqny2y1HA4ET6yzAqGh82QqTU7J9JwzvRI86HVMQLoejKWtuYpCnZ9H9J_6UKiLeAwSn1ycBH6DqrLuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=MsCAC8akjb_WkApy_1obh2DDhThBI8hZNmbbmj2x3hLeMImgnwiM3v87lgpamc2V7US03KSq8XtsE3SQjEBDlVjiiUAHIqtzGxhHWopU02CBibWsEUCTBiU1cJXElnM9cmBPAEuLKoayOVYsWxL81uX0y6N2tC27ibWuK7Kus_fKgcCVSmQ2waVT60AH2ha0jEoiWE8TfklDVxyBOjSCd6PiLmyYv8BA7Z9BYqxEvkSMzfvfVnYHh8Hv-Cu8G1bSr5BASuMqrR1FKXF8fWJol2OTO_hqGItQuHZu1GlNo9os_lCzA3h0k1_e80NhEuxHMoN55cZvTpiFZ1LlYO74BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=MsCAC8akjb_WkApy_1obh2DDhThBI8hZNmbbmj2x3hLeMImgnwiM3v87lgpamc2V7US03KSq8XtsE3SQjEBDlVjiiUAHIqtzGxhHWopU02CBibWsEUCTBiU1cJXElnM9cmBPAEuLKoayOVYsWxL81uX0y6N2tC27ibWuK7Kus_fKgcCVSmQ2waVT60AH2ha0jEoiWE8TfklDVxyBOjSCd6PiLmyYv8BA7Z9BYqxEvkSMzfvfVnYHh8Hv-Cu8G1bSr5BASuMqrR1FKXF8fWJol2OTO_hqGItQuHZu1GlNo9os_lCzA3h0k1_e80NhEuxHMoN55cZvTpiFZ1LlYO74BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWnjfiksSHODzqsjSoMpCGguSDcm6QH6LoZuHS4DlYqIeB4G2s_yXlAfGZpFXGvmJFTcBmMBr-QvLaFtN9f4SuZVr2EF6iO9rAndrK_2bu_vjF_qFVJlVv13KxWEIe3j_eWKvQLrKXxbIoFcM7H5NHGCt3tmwu_8Usd3vLRTlturEqIRqLBwpdM6lAQOic0X_NLucPYeTnEglw7uTBvgIOTcCTM6AJ0RVxFAmEIGKo2b4mJxCu3Zc9Scu17JRmH_e90fs54nac9HMNn1Jipiu1qHMekKu22qrJ3vGaTHUCITWT_TbYplR-S5ZGyEaArE6AnJR5NFniRvUdjEfOKHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsgPmNdXpkWgr0GqvHPySJzeJ566fnvYFFxefaVT_3xQB3hbchQwDB_O_7lJJLlLR5XOCkgPKe0un3-ftinzY33vQayI7vWx3bvsnnYvRgg7TexTcBFVG-TsurvrxR7odyZId8-w_BJ9-SyQ3bENvXnNS5AUB4k65KgfOCVUlshdfvpcvL3c_MtggzlHDiDdPrmY0NFJp-RJEh00u-nx30iq2a9iz0t0xU0CMmCcDDAWq7HPyGgF2j8yiSnv3KaW9qrSwxoRjWgupW-lL0s0UW4kbm6QDduAzD1lksALjM9TW56xQKFhfqQbjUfkmBLpIYisKEMc8czNtmXqIe66yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=L1_PB-sTx38K4hgFCP7Pp-GbaaeQVxISXpj08KVSECode-mMjFiihbMlY5namVBhLPoIFhdEaC4p3zb-2ysVPuk8KbNgYT6PEgL6jTYQ_8UMuH_03-8Ie1reFEDbq3sLAd2t5c7_d9w_gMj3o7V2H-VQkMiXiDpUAfs5zueoU8-6fvAYfgRSqJURD0_vIl_G4uAB1K694crM7iP63OHtxwFeMUtjPq2HHt5kDNA0gc2YbyYzdalVsJvpNoJIp6B3QC2k3cc2eP_sdea2pjmP0AZubXnPK8W04vwm-wJBLukOWEMP2z_7XEIik6E-25Zps-JPeT5xpeoATny-ewawtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=L1_PB-sTx38K4hgFCP7Pp-GbaaeQVxISXpj08KVSECode-mMjFiihbMlY5namVBhLPoIFhdEaC4p3zb-2ysVPuk8KbNgYT6PEgL6jTYQ_8UMuH_03-8Ie1reFEDbq3sLAd2t5c7_d9w_gMj3o7V2H-VQkMiXiDpUAfs5zueoU8-6fvAYfgRSqJURD0_vIl_G4uAB1K694crM7iP63OHtxwFeMUtjPq2HHt5kDNA0gc2YbyYzdalVsJvpNoJIp6B3QC2k3cc2eP_sdea2pjmP0AZubXnPK8W04vwm-wJBLukOWEMP2z_7XEIik6E-25Zps-JPeT5xpeoATny-ewawtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPhbUa28BfA6KaNsWeGbNbOJr-L_AYTJ8dRTQ2T6GXh9Yv6osyNsl6EcuRjbJo6ecJ8On-AAYkgRkjXhD6pUOJOoOQDDqq96U0kmprGMKbMAb40bK1cCWz2B46NzYjGjF8VrMMBy9wm-iFXDHsl7L86i-UynR1uwk1tbS0uQXquU_uamZoJOBe2XnJXDDiS0Ux8cyCcwDMvAinigoPqcPH3024knRTEdRJHs2_-qiYxIejORO69m6CbNf38OMDX8S2ygJvaG0b05dBjYCUv4f5u-BAX_r40rPPxJw_GPlIzaZpAOP6OGZAkPTfcjp4aA5pCFSGHHBKpAOJ_pdTXDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7iDJd-T7eUE-K1OxgBi2Hx0mPf0hFtPVJ0cmmMgRlfbDOhXtESKu563VF5UfYcEOd4w_-l4qE1U15GjZQ6jGg6CmYsyRFr8_WaUCBxZyVIfXPQVPvY0PscjWCoVHEZsZuNVXU6KISCQTsuXuB-6ycKhfkCJzzeT1V685wWAXMndW1MJcPxoN7XO0N6fRIT_70wFWC_DcGFwyKRsl-IcnpGq_JCNp250RBIaOMy71fPnZir6SdQyiCu8cDqYeGjyccn_o724elg6RXKUR5xtmgqHFqU_OkD8WlFUnbt8Jb6KXmHUAwGww2Mvat2WdSprAmGnW4LKFYQF1MenIWc-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hGjgDQ56W-AAiLQjl6FPH7tBQbxsqO6Qkr_s25E_1OdGxjrTiAz5NahKusNaWGCe32umTPSJZaDvfJW3Ma5Jx1h1tBQ1Lz9NE2rU2ZylN3cCwjxNCgYaI4wXqYh9iuedtTdYfnip-rFbTcI2oUmAuikbo4o4a4EzRIipDGJf0MaiPsoDLDvEQBnMUd4EQYdysUfXge6sO_oy3aiqV3G7grAczw6NyWbRQx1qBBFEL93pmOB8CI6J7hQJblvVdNxYQuKRrXI1-9YuHgDs0m-XqrxOmp78Wv-diFC7gOYefUxtb1dFbtB-3lC0vMzZDnVUBu6nkxIgOiDMxeH3dFZDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g4qZQdQNSoeeRntRgVRqOBxHVgBeCkYhQAT4Qv0AgVCHQ3Hs1ZYLJMA1Iyrn_dZc4o_Xpk5wFbyiiWpgkPe5twnCG_A22gPhHdvMRgKEkTypNIIPrgn7JeZuXf0OrXTn_yJuer-koZwlo1W6QRdIcImrKhktSEod0DSHHXHNmp7cQGluAyD1zSwfCbLfkNuX00gEg5IC9-5Qahl14Ft9ogeOjWmP4XK4S7Bcfj-nd6nfsuDfiUf1k0dYMUuKdC6nhamgUCBFfCNtf230Eo6u7JYxG3RgZ59ITJ74Gyk84ITPOQYnjyQTbnLspArNYLgVxjHCJioJf8Zrhl0Z38wNoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=kCGiMyBafsNaXMxQZMvmUVo5XPu9PhMJuzLL7K3zKQQpPXzMldT1Ao1isoe6V0Sd20fwF637nFQYE3btseb5uz4OxzeEWnpyfkS-uTDazGoCGOo1cAIrO8WLY5SVBnQ91RRArYo_JYYoNgB-DpILgh9MILiu4FL37TSU9QSgXJ7138wl0Z_Odca57SGNZuvtmitQiAJGwGWqbJHEVPTAhvSvbGJgysKOhfRbSV_3hJGkTwLbjP9yC5EElxf1CKifGfJDKDv2-fvgPg6ZD0R3sWi70dyFtNfX6OqUrcniQN58dbHBpI1_U46Omhrq8UKGsqMwjygrcVRlJV4jH5KOKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=kCGiMyBafsNaXMxQZMvmUVo5XPu9PhMJuzLL7K3zKQQpPXzMldT1Ao1isoe6V0Sd20fwF637nFQYE3btseb5uz4OxzeEWnpyfkS-uTDazGoCGOo1cAIrO8WLY5SVBnQ91RRArYo_JYYoNgB-DpILgh9MILiu4FL37TSU9QSgXJ7138wl0Z_Odca57SGNZuvtmitQiAJGwGWqbJHEVPTAhvSvbGJgysKOhfRbSV_3hJGkTwLbjP9yC5EElxf1CKifGfJDKDv2-fvgPg6ZD0R3sWi70dyFtNfX6OqUrcniQN58dbHBpI1_U46Omhrq8UKGsqMwjygrcVRlJV4jH5KOKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MOvLXLqKJ1eOujnpQd6roxkFi72vDmW9wdUybmgbaPEJ37IUN43nYYqtb7wfzYCxKlMW6_eo8OsxPoF_-ZmamQ1HpVDXAkDnburTGfjRnxMjOJZ5rvV0d8qF6yqmIXU6Yxn4xp8vsIj_lKVJyosXpeDIXjpzTVNRBqw4X1R2KayYlQCrTlouBsGYlWW_gTlh7SeYb7q_exrqC5OWbvuONjNSRMoFx0qhPLAoNNAnaupdROeIYeQ_4UXBJdtCADiw7pw9qz_GtN_JFaNPHV0UwZ9M0eQRFUyla11lOc2-0dPNbUZvSj0B2H1scpJAgSaNPE00CxOlP5sHJTaGyNy3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=Ph7F-ldDtmQD5k8tieEhryfcyCrmiCi1a_3DugOCjoLbK2XMi0OqgT9ZzkrFKKD0kyPU2psy_S5_bIiXoiw8cM1QrqZy9CzZpYwMqw0pFX_bbn-oCbhhybdZRRzCgnXr5OtNa8JSlEOfMkLUGoN4nBdDuN_oaqiZwPm1Ww4ZEUHfI5_jFFfO3ArQ_ykRtUCUVQPO6Th6lcE_2dosTKCMNyJMLnBJV3IVMo1ypkJCIq0sOMYhek_ghp2jQ9wXfdzzRNmYLq4PNC2oWZtLFrD92jvlr81zmfxeke7bw_zQlbIiuCXD5Ea2205yu5tn4Uw2enfiN6b0gdLRqWQWhxfSUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=Ph7F-ldDtmQD5k8tieEhryfcyCrmiCi1a_3DugOCjoLbK2XMi0OqgT9ZzkrFKKD0kyPU2psy_S5_bIiXoiw8cM1QrqZy9CzZpYwMqw0pFX_bbn-oCbhhybdZRRzCgnXr5OtNa8JSlEOfMkLUGoN4nBdDuN_oaqiZwPm1Ww4ZEUHfI5_jFFfO3ArQ_ykRtUCUVQPO6Th6lcE_2dosTKCMNyJMLnBJV3IVMo1ypkJCIq0sOMYhek_ghp2jQ9wXfdzzRNmYLq4PNC2oWZtLFrD92jvlr81zmfxeke7bw_zQlbIiuCXD5Ea2205yu5tn4Uw2enfiN6b0gdLRqWQWhxfSUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpke248n0xanhAUJ7rH_-L3XHq9SbckgcdaqLQ7wioCordx23W5-0vtn2v9ogOP1-X_AuJEo3-HwyoVqPFl_fHgk_dk3U55p4qH9-ctevf5I99DxzhDSP6MGh2Xnw3JHFsEijvzX7IKCmuR38hEprFLdCvAXRFXcB6ggvqIAMi5cGqmV2WU4l4v_yOG-J2q2uImGI98pGchExwAp2uLYNMztGb1WNUOEamGq4_by9hYOS3uWh4SBAaL-GYl8xNdOcLiEJFmCjgisLSnJuhUa2-Ha33kRZdbtSL2BThVFmyPC_z_hri1H_C_iFj8UzWgtNMPRaSi3nsZGMnGjGLfY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAmHO1ASObrWp1eeQtAgVLr7mVvfWt_yx-Xy1MmLFXbhWqzljCpVfjbv-CkToXvNKAhe4Kc5PbJOYVyJHdtLpYCVx74YK-colse1tnzTEqeVNfeiErC895D7TqCvlXcrBTOtKbOldX5az86QaBVFNlf5HxB4wFONR13a7lWdTWi6q_h_LB9NXShUtoz1wZ6HSJ-ydmjkl4ObiF4WQMXiwjnhwspLagZMr1Y9iRkmZpPSFTaUtT1D34FWvCXgxQ_drmIg3BxnMWCynlaL2pTKfVK_Hj9Fw6moXJsZTHwoG7qg9ZMpb-zyMb90hJ62mGqxoza7rwoyC1yWYVc3xL_O-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=ApuIO6zHaHwf7e4pibjqCLfy78KgwYGj4STubb8dR7SqP2tM4JpVUcSaMrb1yMKa64aqI_rRDMz3LlIW__u-lgTm97qUsV4TeCqNwaYM-MqgpRlITZNJaAtl_d3y8OTYtYifeByNDDGqHqHZnZFMD9qm7Lfu9aYDwq-iQzHHhSY_UvxtaYGZZgiW6HDVtJDlzpqgjPaHlpppWPdFzJzDleB6bqhFWDi81bToPDgRE_xF-bBkyUzBMDpDK9_ZXgr53gxkYvkvdQJzhnmWGqwNCFcTdxhqsdU2BUHJHfZ-CYNfAFZDk0lch5qVa7eGsPMYo2_51SXtSqrXuOHUWfrJYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=ApuIO6zHaHwf7e4pibjqCLfy78KgwYGj4STubb8dR7SqP2tM4JpVUcSaMrb1yMKa64aqI_rRDMz3LlIW__u-lgTm97qUsV4TeCqNwaYM-MqgpRlITZNJaAtl_d3y8OTYtYifeByNDDGqHqHZnZFMD9qm7Lfu9aYDwq-iQzHHhSY_UvxtaYGZZgiW6HDVtJDlzpqgjPaHlpppWPdFzJzDleB6bqhFWDi81bToPDgRE_xF-bBkyUzBMDpDK9_ZXgr53gxkYvkvdQJzhnmWGqwNCFcTdxhqsdU2BUHJHfZ-CYNfAFZDk0lch5qVa7eGsPMYo2_51SXtSqrXuOHUWfrJYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4Q_QoIBgmWPNV6lVdgBRHJkzaDd4xQfZOSUBhetr4WgkZhpe-7Txbz8qWXYwQMC2cO6ljFQ8UB75bhbxxGTG8QsWVOZOchQyeaDe_bZIghlywh5yt9cTGThhR7mY216uId4ILv1hlSQJ3YYsQQoVmm9T4DtRRMptjiRmevSEE8z5goBwuqoDewAzD0EG_waVe0vW9LHc8wmKVclBnDx2hNzBryWWfMe19cO9rCfJNBm4IKMn_toAysIY89rO9trXPYZEKYUj9VKbfmClsidXCKXRR0wBvHv4mU--3Jx0SvncHmO-UTNWj3biqk2JiuMhl2zPnyQEL02glTgDIZ17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=Wz_jMs98t6y-mBCM5q8i78d-GYQMjPEx9jKhPaqFh7_m9-14qCk70mQ_XJR824X2mRVXvSij5DKj0qjzbR39wOw5NpaCPgV73WaRApSU5mzpEkCznoHkHp9HuoVZTsSPqQPLZcdh0TJq4gdftqPLkHz1NaMhTuDvAikBVjSX-NouiREop3PGsR_V0CFbvu66Je6wSD6TImY7pvxiMzPzIH__k8O1Vp4LkqN3_497Rv5JkqYyXr9QIOIr-xCLg_mBs9ZUoMsj43xvFUo1K1mroytjzhIJjBag4PNR5FqC27oqLlgqTGunsnnefampf4bF6mkOHXSoKx-l84-7p1zFJC8Il8jqPla0F2NA2yaqA9bG_1_X-4MU9eqkQHRCcA5Lv9zXNjMGCFTYHWuIOtyXYAMSKCaLjsyPhTYwheo7WiQhC1j7OEByzaU2-8whBSxgDdPJ-I2XzCJgI3Ed2iS6Nc1B8UDlxLpG6Vau1Ku0sSz3VeoQuWnUNdozplzBFidnfEjbj_dXe4KuZDRcC2_8fbvNxhwxV7dRpD8Bk5S4OiL-ssT2Fkeih8BrK3bvgXHv54psNaLtjyJNIZJybzCXuGHPCLKtbaK5vj-ziE85NuIiSHVdbhabU3h5_0b5P92QhcVSjMbgqGKPZR2oNU2Q6fvdIxKq2U0k1fBIl-wUoPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=Wz_jMs98t6y-mBCM5q8i78d-GYQMjPEx9jKhPaqFh7_m9-14qCk70mQ_XJR824X2mRVXvSij5DKj0qjzbR39wOw5NpaCPgV73WaRApSU5mzpEkCznoHkHp9HuoVZTsSPqQPLZcdh0TJq4gdftqPLkHz1NaMhTuDvAikBVjSX-NouiREop3PGsR_V0CFbvu66Je6wSD6TImY7pvxiMzPzIH__k8O1Vp4LkqN3_497Rv5JkqYyXr9QIOIr-xCLg_mBs9ZUoMsj43xvFUo1K1mroytjzhIJjBag4PNR5FqC27oqLlgqTGunsnnefampf4bF6mkOHXSoKx-l84-7p1zFJC8Il8jqPla0F2NA2yaqA9bG_1_X-4MU9eqkQHRCcA5Lv9zXNjMGCFTYHWuIOtyXYAMSKCaLjsyPhTYwheo7WiQhC1j7OEByzaU2-8whBSxgDdPJ-I2XzCJgI3Ed2iS6Nc1B8UDlxLpG6Vau1Ku0sSz3VeoQuWnUNdozplzBFidnfEjbj_dXe4KuZDRcC2_8fbvNxhwxV7dRpD8Bk5S4OiL-ssT2Fkeih8BrK3bvgXHv54psNaLtjyJNIZJybzCXuGHPCLKtbaK5vj-ziE85NuIiSHVdbhabU3h5_0b5P92QhcVSjMbgqGKPZR2oNU2Q6fvdIxKq2U0k1fBIl-wUoPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=L9SqLK7wFPxW000p4vO2kyyQm6Exu1m39YlhGSfGt_QvNU2ZKNY4Sa8iqGdfpXrJlhOtx4SZnJjF6MTouP9cYPci3AzNMLyUsOIgYj2U2RE6noKxeqK2ybJ1eom_SknK_jPa5EQjQL_BUgI6h4R4VPQrvJyuyJlnsQk4gDSTHIJIL6NgMWXXO5bcNG3FeXdSclGr0wGcvMXeXiZenEsWoXUoj3WC433T8gUr5aOqQ6Vyz8rzuFarQUCyQbfhzQJrlglY4NrdCe8exVmD5j_81Qy3m1ZKtGHG8oRt-l5XPNE3M1fH1lPyXJewmCJFk1q_8MIhYet53wQQi2TdHTNS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=L9SqLK7wFPxW000p4vO2kyyQm6Exu1m39YlhGSfGt_QvNU2ZKNY4Sa8iqGdfpXrJlhOtx4SZnJjF6MTouP9cYPci3AzNMLyUsOIgYj2U2RE6noKxeqK2ybJ1eom_SknK_jPa5EQjQL_BUgI6h4R4VPQrvJyuyJlnsQk4gDSTHIJIL6NgMWXXO5bcNG3FeXdSclGr0wGcvMXeXiZenEsWoXUoj3WC433T8gUr5aOqQ6Vyz8rzuFarQUCyQbfhzQJrlglY4NrdCe8exVmD5j_81Qy3m1ZKtGHG8oRt-l5XPNE3M1fH1lPyXJewmCJFk1q_8MIhYet53wQQi2TdHTNS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbcsduXqG1CtN40dZ8tAGcMv1ovJMGvHtGJM2GXVJSTGAbPaelG5hW2EZQjLKezGSeXsJNx5LNh6PBxkVBO0q-qqlM1rMefcm90LQOgbNPRewh6R1JC2rtoxrEuCB1IDsTaJZanYuqz6WBD3tJR-NAroJ_M2AsHwLsCJqN0AQfpv443Zp3prj-2NqdcZ2G4eNFa89M30GQRqwrJgkXVzLn-G55banPdPzBnfyPlUsW5waNaZnUbMtwP7F0LS3eE7cA7_ilI3_5VUm2fiqQrRMtLNGrVANOIzO3_FKnlOVYfYm867xc6HlOVlLcQ-49Zg5XXpUygKSrsP32afSohsJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=BCb23-ZiIc-T3PzbiwO56Z9enCtKman52I-COFEMFWUPpcal45R8I70xD-To79xaI1p2DhqR75lXWf4cEE7sWAAM1O8uaHD1m-Ej8xPArqwEAwhRGC4ERbNiZhubN7iX-jNRQlnhgW8tQwiTWb7SzPSSXsL8cXsY6rxmnCQll3KG4lb9KiAXP13PEBOj8D_09sG7Zc1W06uHNLfGPjgnmpxbpTnCApuktURceVeW2Py6D1TqXdlsS_orhD4apmATmembX9U-Z2a-k0abR8mIxUePjF0S2ja7_W5koUA70JXjk6LRIvL6E7U0BpmE3tUYHX6UO-Fo33hrzAuSDmKTCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=BCb23-ZiIc-T3PzbiwO56Z9enCtKman52I-COFEMFWUPpcal45R8I70xD-To79xaI1p2DhqR75lXWf4cEE7sWAAM1O8uaHD1m-Ej8xPArqwEAwhRGC4ERbNiZhubN7iX-jNRQlnhgW8tQwiTWb7SzPSSXsL8cXsY6rxmnCQll3KG4lb9KiAXP13PEBOj8D_09sG7Zc1W06uHNLfGPjgnmpxbpTnCApuktURceVeW2Py6D1TqXdlsS_orhD4apmATmembX9U-Z2a-k0abR8mIxUePjF0S2ja7_W5koUA70JXjk6LRIvL6E7U0BpmE3tUYHX6UO-Fo33hrzAuSDmKTCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=pUlrcgbN5WoEDZr92Vg0mqZzx4-P11glvx0wZ18Zwh-Q4mT4-0isiJ7IFQJ-C5YqLmshDPCBaHA-Dg3Y0JpExb97CuP4qO38TTir4COg82IJE1G3lywCiJt0muKQdVmr8_XZ3BmMy7PDuhvC0l7ide8DDxWpT6whRP85-rjhuAvBS-gmCHsygLkFV-NAMF9sFQTaBH0HOsLQLZpcnAOkJ8iv0tEauqSRxE4PeVRgQR5HUVO3-bvzx4Mi_T8YUcNa1UFrKrnJ0c40PkXrKZgB8OwcspW6_P3i2YrvFaKq7aFe2NTTPRKCYQvmFNiLmJKCWoTVsHNhwvU1dUWKbRZf1A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=pUlrcgbN5WoEDZr92Vg0mqZzx4-P11glvx0wZ18Zwh-Q4mT4-0isiJ7IFQJ-C5YqLmshDPCBaHA-Dg3Y0JpExb97CuP4qO38TTir4COg82IJE1G3lywCiJt0muKQdVmr8_XZ3BmMy7PDuhvC0l7ide8DDxWpT6whRP85-rjhuAvBS-gmCHsygLkFV-NAMF9sFQTaBH0HOsLQLZpcnAOkJ8iv0tEauqSRxE4PeVRgQR5HUVO3-bvzx4Mi_T8YUcNa1UFrKrnJ0c40PkXrKZgB8OwcspW6_P3i2YrvFaKq7aFe2NTTPRKCYQvmFNiLmJKCWoTVsHNhwvU1dUWKbRZf1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWL1HhLoLQrNDbxhamn4UoFVwDv80nUHeVdR1u7zJc8Br9xY0I3Km0Qcbp6myFNKgbnBLG-0NaFmnXwAf6WITgMCwyBInHL9M4tyzPGXyjk2i1tBpZj8YKm0vIDaTIUPgJOESj2KZa7wm8he2KTPuyjGfwgSEWqzQFn3HLRpDaLsWffKfx0E5pSDJa3WApPSgPNA3W3EipyqEX5fPWe7dEDDluItch9_uA1cW6_nJc7mQeWubK-yUGIMA_Q1qBrkfYFA47XYfnF5DOCta2-0gY-L6tdLyVsaQ9ZszsHvxdyZU8GI6jD_SE8YbQ_ssmobjP--xD2iOoBcTwNBdhXsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=Clw2Am8ZjWit7416NuDfXYQrwLCeiV3Vv7d1C8IzaGsPGcntZQeZuvpRNcQ7QdQMNMq3Jv_0p_37KkO4xeNycs7ExNDYcoyX2nqT5r1x6iDDisfa3ClhANsN-Dj5Va1vYYjo97aD2EgebKZiimFHnj_cDDrfP76yfU8hOPZ7XINRByfjnpBDeOMjJDJewJ5OLfEjXMR70rRABn5kJHj-iFtEV8JwyOgDOLlFx-9GLnamGhWqUVmpSYEZA5wXgo8s4oBBH_5X8tzI-6SGQOQF9FjGsxpIkzToJYHMy6nTR91iO2kekNZyfGBASRihtFnHsj1Ns_EMdQ0DikBqVd151Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=Clw2Am8ZjWit7416NuDfXYQrwLCeiV3Vv7d1C8IzaGsPGcntZQeZuvpRNcQ7QdQMNMq3Jv_0p_37KkO4xeNycs7ExNDYcoyX2nqT5r1x6iDDisfa3ClhANsN-Dj5Va1vYYjo97aD2EgebKZiimFHnj_cDDrfP76yfU8hOPZ7XINRByfjnpBDeOMjJDJewJ5OLfEjXMR70rRABn5kJHj-iFtEV8JwyOgDOLlFx-9GLnamGhWqUVmpSYEZA5wXgo8s4oBBH_5X8tzI-6SGQOQF9FjGsxpIkzToJYHMy6nTR91iO2kekNZyfGBASRihtFnHsj1Ns_EMdQ0DikBqVd151Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udZB2sEYJc5LoHvfvFSzG2q5NFaoSfQLg8VpHngbxd_-7w3QxEQ7hStvNS6UZkHdn2I7-F4Ht7S7K-bbm2VqP1clHQPjjH9h2-kwAGuL5FQN5xFH0BZB4_Hs__TRrgyhRjInLRwLEL4IPllvuXLVq2Hgj_8NpElTKSyotVJsLjf005JfIUx0TBpRGqnSoTAOl5osd1NMThZJ1jBVNn1Wn7FsZYhSqd_PjEnE8CMjkbe17cSr9OyF1KDYazqel2GqjGvJ5AOUfva1CZKg7dE94X9kvjt8UbBQ0B9aGEgViQjQBkbULnCwwtoEwQWPRgXlcfV-1g_UvULboLP8yoTJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMgixi12ZmtVVWUzXxNC0pawP4RuGZS0M4y7oPqec8C35XsRymk2JRUilupAapmIdY_6dIzTf36bQ4tNz3FaHlCMpGlXx-QtNCydDA-17PbdjZTq1d3G_1LPwX2QdEQnrmgIbWK42g5DXxOZvPxu6DnByGBrkNhd7_60PGokO4seZy85f-xH6W8IZDXLjPmg7bYJ0CRakYFTxZKjMWbsQHXjTrj_1C-UaEgHOsOR7WItdQqTp3LqJEZsBSaVM0GZx_bbxsSJDHHLB11rBdjsh1zXLWwkrcTMSqJkLgNZXmySYIMjslzz19fmQWjIxf0emmveSrBGABvijHBwx-K00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhxccAmGbhegMR3InN-19NpjhIDI_tvrsGjfIN5dpC0ED7nRWhkLeFxV9ZLgNyWFWgeERGUWHrNU5WIF1Adwa5hv-J_1YyFvNDRtUHjmGda-NQQRREwCln3eUc1XmfCeqrCdFPI2ayq5BceZg59tE-D1rqxooRO_mGF6asG2KRzgtWnyFgmF442PEB-KXzGQdR1e2oXWxCfPqgCt-SaKGRUAoHf7PronmGoAGIxOqVVQvvSBe_QwiDMU61p6inMmMUAESw0xgo5JxwCkhr4wlOxHG8Rn5MS6y8OOOXnhSiiG6vGCbanV0WveNSWTek1VVBmbbCk0Tc35l6Np73DKMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlceqOHY9sBDTq5F4xLaHqhZRrP2RT1sGAPMn2uKyi0bPOLcd8DCfe3xLGZFsahpvPHwzdNDqOoG13Nbg8K8Z5XSkNd2UjOlSeUNd6uFuke-MdBKumlukAPbusUCx-gaCRkk7LD9oAVIsBVumdueq101KegbGuPk8MoIWaO2GD8oiXi4kvRboGy6GgS9GX2ARF2lvVJYyrhsG7CwD5PQYF1foc6LiRJIRfLIlUhpxzJI8vrkGBCR9HKQ3Z3HfhG1C1hcSbaIBUOCthaKfN-SBhS1-UNGKcUm9Uak0fKZdVsoUnyJuz0VLUssxuuLOvm0xxA2PMIFJ2O17iqVtvkeNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=JQPSu147M50eHJCUZKAC6riY5vIsdtqxPpZLIarKlRs-80RFkjwLvSxY1XM5UvLd2yKzjeZfhJGfGMi3Duqiqw9QrBSgCgVi1BO7KBs1Xqwc52WXEr3R7poA1YnMw4ue0UTAC9rEuZFDMYlPs8PXJJXWS09dgZA26pzBB3Pqh752rKpUI1dRdk3erNaWTmtQyTYVDGwwTl8n03PQL5x1qq3kz8l_AaDDkyUrYTO8se3Q4JC_E9kfBr4QhpmizdPdUUfIFBPnlpzesj_Nh_CUvUMuflV5mkEYaeyCHv_1Pd-TjpGVI0BIdBMnFYDgM_u9wGnfh_fYmc4Ng1E1LPctiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=JQPSu147M50eHJCUZKAC6riY5vIsdtqxPpZLIarKlRs-80RFkjwLvSxY1XM5UvLd2yKzjeZfhJGfGMi3Duqiqw9QrBSgCgVi1BO7KBs1Xqwc52WXEr3R7poA1YnMw4ue0UTAC9rEuZFDMYlPs8PXJJXWS09dgZA26pzBB3Pqh752rKpUI1dRdk3erNaWTmtQyTYVDGwwTl8n03PQL5x1qq3kz8l_AaDDkyUrYTO8se3Q4JC_E9kfBr4QhpmizdPdUUfIFBPnlpzesj_Nh_CUvUMuflV5mkEYaeyCHv_1Pd-TjpGVI0BIdBMnFYDgM_u9wGnfh_fYmc4Ng1E1LPctiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJT7akhVUa6NTivgnwYwO3iNQ2R5QfAyGbPpeAlqdM4PMjFCvqduCe6AnArb3MCwVIveGYwnn9Sj3jREGfqaJitoA_pqctNXQugj1sLsNlPICkliCDugawtbWofs-9IK8impp2Qoe239o8wh315j2zpJ7Jl-pBhczMYf0oboHmHpBwpu47DoFkQJRsjOY9wtZi8XLDPB-u377l8FolrLdb3zzQPRZ2LqBPA7lSYwJgxSFWBHiiYGx6E2b0IMa6AAOaK0bpot6dqvMv02GrHh5hf96Xhcu88qe639J8swDc1ZYHEaurSg-ZEcmXspd03JiXdypj0MqNqd_x9PB0NARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=nzWHjlfcr2AAfLYd5lXPx6II8lRzVTl6Y9OGUXRl20lg4hnBTS_gN9iq_aPedydpUS7jDBPlC8DB-h77mR0coltuxhG5lGGWm6nsYOcJVpkM1XF0zNvikWYuww7VK_etIGtJrQ1NxJl78NT70mk08fGyy-qs_77NjNrqwUWr2mt8K6EtbzYJ_ukpdf_Q_-FiGk1Jje4yrmk-9rKhbx8huzC_dbVObjGK3UolOiZWGDoYJ8CSJIOIZaqlx06zVtR1L0l8T2uYcuDByFz6MQgzxLA6ETl5C0vY9pl4be-ndY2uAEDaaS40TKtizqyW4Fr87VTFXjO1G4QcIRx4O9IB9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=nzWHjlfcr2AAfLYd5lXPx6II8lRzVTl6Y9OGUXRl20lg4hnBTS_gN9iq_aPedydpUS7jDBPlC8DB-h77mR0coltuxhG5lGGWm6nsYOcJVpkM1XF0zNvikWYuww7VK_etIGtJrQ1NxJl78NT70mk08fGyy-qs_77NjNrqwUWr2mt8K6EtbzYJ_ukpdf_Q_-FiGk1Jje4yrmk-9rKhbx8huzC_dbVObjGK3UolOiZWGDoYJ8CSJIOIZaqlx06zVtR1L0l8T2uYcuDByFz6MQgzxLA6ETl5C0vY9pl4be-ndY2uAEDaaS40TKtizqyW4Fr87VTFXjO1G4QcIRx4O9IB9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gk4IZws1yZDXkoi20iU0WOX7Fzy1Qe8GCPeT5e6j12UNiWFoR3-QXtL86RbHE5RN1WfG2rL7ddWUCmwsya4zThMQOghPdbO_kIElxbt_Y8lbGOsFtZ5V26IqJQWxFlQt2e-MilsV4ZDi1V_52IHq2GDTOXIVAUgs6EU6qRVArUqMtKWDDd5ZhOXSd2pesMzwQfN7hXaSLrIu8MwU1nbtg0KGxwd2jRMlmQQ2pS_kVYcsJKWDhiPXTOUY8I9IjuzK1llaR6SoxjgEtZb9gJRj9RMHLEYzFyyj8boDjQh7503lOlwXXZEcXa-7MgIrYgXJ7631XF7deamL7qMvQmQk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7JnXapUcdISBvNKdV2zhy58eFlAX8Z_l7HRIpHcXqvqYulz-a0zJSD82dgKIUAfsQES74qd3wMCVAoTPz1MHfSQTHr3d4sbkKvawQr0L7PlAOS64h252caFiyZYsTmwEBgzo_1voZGPY4zGtD6BfIfge4pAZaRhZI-0nPFdGptzQN3wCv1sy8NN7aRkadAXNyde4tUr1wmyRC7wXhqjJv4bc2QxDURWPtBGqoVy9Hi57sk4TmnVSkkAj_qYeL11CRscSrx_l8Vi9ZjpwPz2T-mp3zBTtldXuEjDUD2CCQ1CoEIugQb-JmmIXuvAJ22zRrh__G0bkVHjpoVRbW8yUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKdMwZrUJ6jEMqqMuvTqqB2B1yBmaJXqJU87knQDE3xsTU1uy2mW6t0Al7Z60mE-oDLufyun8_AZHAaUU4k-KS4PW32yJ2jI6CIXb0GP-VybA10HdRZGRLFhpdL8hJnPyD7LntcXVdDzDIccXdgL0Jwaf_gqyXlkUThTgp51Gwcb4MHjdsZOb2Hq6-GChewOGMVhbgzJYzr3uYwLE42OrNn4gg6yMarDgJH36-e56DqELtpsXx3WQDYxaJ-3Ptj-nNwG7Y_Laa_TXpqtZpBv4y1DWqAC0eO3dKA1yYklxN0C1eUTXBrvV0VnnRXkNV6EsJ3o2Ln-ysxAzm7AowvMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8gJ9YDU9Lk8gezq4x0j6wxTJrMT0MiVw2Vyeq5ItG6L_uhJYNf9mJ2MXixFk6XfxQ7WjoKZ8GMNrLQfiG6HTzJ605q0itDyffb8c9YyBeoUQx7jk2FkPkdr0CAN2tlPjSsVufX19bBtuZn4JyOBIWEacP1VOBNEVFhXHNIaVUwd2J6o_tdxMNm89JFiqXHUhu4YHHY0KYg_loNS0cFNwNkakFimE_VgOkBUfuWU1jQr5Hl5T6kVYmyACCaths2y0FqQxVXr4Ai0pDMWQgm0zFN8b6ofBZs3jZ6OmG8x9B6MpzgnVQvjDNnzN15H_odFoaqBvfemDLwkxRwqnaJWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKSnNVcivZ5BaLzwMSkKLsHpcgQDVGHVI4JxNQdavf6LyASzhSV6GWZ368GB-5wM8GHyoAIfpeiuEch8YytzRGsXfKLB358DP6s8i1KwfKReIqp7b2NaTqsjviXappbMsnCvorByvpzDExpGRFxV-CJgMzJTGsnTbmTCjV1Y7z79IKg3amg9phMGhOs8p3RSm0JfJGoQVNlVOZ6o6nrPvUhif4_V76XAeKg9OEWkskFON2436N6VmvZF1eHLK_Cg2qhcBJtQBTHEhR2npzUoGnmvc-XHLloQIcW-2B2lL08kv5nVpbLX7byFl6ZqwvdysZqbCQxaXrLyVKAiU4H7SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aRpaza3Is-dCan_N9lEXJRM-ir2w2nJ6lVPvWBU2NL6Fje1GSoA25D_x3nTmkgaT52ySbBo9-3nJwZoh8Y1AVwgI-94znSlbu1cnuqdLID-PVgozu2InE3yV3sp70CTIn-1_bBjTNDeey2mxnWVtWEu1ekAjA2GUN3iI0givHEBwwhmKv-fIARtcQ1JOuYlLR8Wso3OUo5BeePSMkf4Fmmz2WBoDw9iYR19510NNxcxkLxEkSOSq_8IKXmhJVby854JdIMwWb526jYOIln3lM5VfjcG1YP9dCcd6X3QuX1KsRtvxJESu3JSBVEUDnCUAVJUD5u5M_58D_-Af5NiukQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hc8rpjCahybnI0-A8gCEmiRh0Ln77yMaaUEPx0cUV1kRPQ0qF-GS7AfTm_IypnPQglHbnjB2HYGEhW-U9wA0sEW6IAgRJLSswHO9wtCsWT1bTIBAtUkWHjIcH2AW1iSGYeUOF7RUHFjkkoK52rSgXS3wYDSKO3dGw0vODoX2YZpOScN0gyl-uEEqXQDEFVXt7Fd6kaVigadku1Q5Us0r9GeG676zrWmc9p_nbmK8dJ2vELldclVEDl4ebU_lJBWM2aO9GLqxV6jPRLBNOoM4oZbHQj00qHJ_3ihmTjLnLzIVhIeWlGH5u6peIm1fELAT1jA-J6QX9WlpwYU0e4Wemg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=A1XUkWMb3RNgbiSojcNze7SnU1EK-YSrTsUBadyTCyF1DNYw3ltgtf13mhgTyzqxoCeSGHnXnwzEfIUo7u8Dz6ENCThoYwLV7krT6vAXN39X-TfnwoH4L8a6C7uanFDRsecHJjILcmuDIgNx73MlKWHt1evebH8QGg0_agsDOZajn4C9ptbvPY0H5hY_MXh9qaLXt-5wP3Gwg6vDW5bzlelzrOE1yiSpLBAFfH8it2KLGn0DBW66D1p98H2FKGbQhNdTZAA20vdfzZLcyzh1dVjy-wzsvl67J3F0Q92aEMv_WVxNYB93d1UNbZa-Cnw9KGwOjiecygZqVgiUbxToPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=A1XUkWMb3RNgbiSojcNze7SnU1EK-YSrTsUBadyTCyF1DNYw3ltgtf13mhgTyzqxoCeSGHnXnwzEfIUo7u8Dz6ENCThoYwLV7krT6vAXN39X-TfnwoH4L8a6C7uanFDRsecHJjILcmuDIgNx73MlKWHt1evebH8QGg0_agsDOZajn4C9ptbvPY0H5hY_MXh9qaLXt-5wP3Gwg6vDW5bzlelzrOE1yiSpLBAFfH8it2KLGn0DBW66D1p98H2FKGbQhNdTZAA20vdfzZLcyzh1dVjy-wzsvl67J3F0Q92aEMv_WVxNYB93d1UNbZa-Cnw9KGwOjiecygZqVgiUbxToPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYP9rvPMNqbQSbqQRV3uqHrbm2pbaMdlL2FEbznJn4EclKqEOrq-GRbGPQv-PkyUEg59MqTAJuPvrABrirpaAg_q8D7V64fafjQ4fDmjO_x51rp3E-UC7RrvDQsj3XrXLlVMkNb3UsodrBdql1QCwlsEkSb3d9RFduC5xuFjASBFFVDWsaSVaxtqwqA7iolyXfSTeDJmCK5-GZb6TIC2KzDly6mLZNLKjh-L_EVNFsxJdsRGzeOxrMVppFFxu6TsHL36SfLNIL0RofQjfMMFtSgBVlCXbnqAVPgbq8IITs6b_8ByB_kSCGH66y9VhjBMJAFfOTdmVyTnE9YtmK5_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=KO8a0S7gS4GzXTWJr45QvuogdPLn30vBDa3V064ZPt8k1dhnlwQQ_9WJIWvcySUzOjofkKjm_CQsSyVW1-NEBl6AwYB_1GOnOayF6-Dfu6kyS37aV5OD8jdaUEpfUGM5V77fUWrDon2cAxd4Kgek-dkgNzP5jNKZO290rbreWhvNKFmfjeKPeYmQMKEFx2OuMhNsflNoikCwiR1MPjT6uwqXvdzQmWHNHzfOPCud2mHYoZpItLMjQ7LsfTLkbZPf0sdhqPFLXLA4yjWxQP-RtNzVsBOE-2v2sVmUnPq_7OWxLCFnWROrduLcZaEgRgxHz_ziIVERTa0DPK7BYQETEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=KO8a0S7gS4GzXTWJr45QvuogdPLn30vBDa3V064ZPt8k1dhnlwQQ_9WJIWvcySUzOjofkKjm_CQsSyVW1-NEBl6AwYB_1GOnOayF6-Dfu6kyS37aV5OD8jdaUEpfUGM5V77fUWrDon2cAxd4Kgek-dkgNzP5jNKZO290rbreWhvNKFmfjeKPeYmQMKEFx2OuMhNsflNoikCwiR1MPjT6uwqXvdzQmWHNHzfOPCud2mHYoZpItLMjQ7LsfTLkbZPf0sdhqPFLXLA4yjWxQP-RtNzVsBOE-2v2sVmUnPq_7OWxLCFnWROrduLcZaEgRgxHz_ziIVERTa0DPK7BYQETEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=RYgr8c0tAlpnV-rQdUEgnMEuwFWk9MvLHpwA6lZ1d07YEZhtZQX3hi7cjHiw36RvZ9ZyBjUwfcmtjIOs9xlEURw2ZEEDR69R_E6zSGCivlsifOJMel034SbTdYVPGtRZuQ0-pHj_oxNZpIV1Pg4Li-CQ49yVgyE_yHlZK_F17ar00hqRt05TuIc6jON5hCqEqQCyje7ere4PYWi7wOJDXEsWnq64aAzsH6JHbTdf3MkFqgCZf2wMcutIkcbH7HMdETsyqZWiuwSHu-mQNMEzVPkqXitQNTWt2_ZPLC8TEb_V7rVCMMBlNFn_oBNUti0-nW4olrrfiT6VFJkFaQyk1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=RYgr8c0tAlpnV-rQdUEgnMEuwFWk9MvLHpwA6lZ1d07YEZhtZQX3hi7cjHiw36RvZ9ZyBjUwfcmtjIOs9xlEURw2ZEEDR69R_E6zSGCivlsifOJMel034SbTdYVPGtRZuQ0-pHj_oxNZpIV1Pg4Li-CQ49yVgyE_yHlZK_F17ar00hqRt05TuIc6jON5hCqEqQCyje7ere4PYWi7wOJDXEsWnq64aAzsH6JHbTdf3MkFqgCZf2wMcutIkcbH7HMdETsyqZWiuwSHu-mQNMEzVPkqXitQNTWt2_ZPLC8TEb_V7rVCMMBlNFn_oBNUti0-nW4olrrfiT6VFJkFaQyk1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=NTKjOEQ_kYQye0vq04xV8NCRqIeulHjA32WC-aPJ1jtDGC7Ot90TAla0UgEQaWUwwYNNGPW-bgDOP4tBLnn_pu-3J4hK_H5wgo5ehYOGISk9LsefnVyM1gqRGQ4mAuJMOKWZibA9RNXIw4GN3H6KwPhhOCU4I0BfmqVjctbIHHj9BBiV-7CuqPB54zdqGBhQAlUmzePKjEJibEiaNv0mOJgkB3R3wWMqB6yZO5JwQCsw575j-pExaYOFs6f5yVipX1SIRxhiQQgFaI-LA6e4RdhqidpXsnq7Nyioa09I_zYiE4_LXBVvj96sKRFHrggu5N-lMNTRRoMA4iO_f4Op5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=NTKjOEQ_kYQye0vq04xV8NCRqIeulHjA32WC-aPJ1jtDGC7Ot90TAla0UgEQaWUwwYNNGPW-bgDOP4tBLnn_pu-3J4hK_H5wgo5ehYOGISk9LsefnVyM1gqRGQ4mAuJMOKWZibA9RNXIw4GN3H6KwPhhOCU4I0BfmqVjctbIHHj9BBiV-7CuqPB54zdqGBhQAlUmzePKjEJibEiaNv0mOJgkB3R3wWMqB6yZO5JwQCsw575j-pExaYOFs6f5yVipX1SIRxhiQQgFaI-LA6e4RdhqidpXsnq7Nyioa09I_zYiE4_LXBVvj96sKRFHrggu5N-lMNTRRoMA4iO_f4Op5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=Of4DDBC5R9PRwFAd6kx4pcY8g1tARKtCdWghUSFwg5iuzqnRJwebKs1mipuizqyFKb6RBmTaoJTMRv_CI8A2ytlg9H7RBfVBWYzJkJa-sEg9tSdns_9otZsqEnuTm1F6pSFu5QxqiL0J86D74kEod-wEhSfb-9AnZeT38mRrdN77XZL8cISdyjb-5gODBkr5vtGpN3P6OScPS90v-UIlX-7mgWOd_o_TRUOZTFJu942PU6G7G2gENzyLR2qXwMozISvgo1ViXOJutm85HFgyAaodJj6N1l_G17yHyf632Suzxe_Zf-0VyUP7f97K9zzwqbMBSPkkPZ_2Obr8XBfFxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=Of4DDBC5R9PRwFAd6kx4pcY8g1tARKtCdWghUSFwg5iuzqnRJwebKs1mipuizqyFKb6RBmTaoJTMRv_CI8A2ytlg9H7RBfVBWYzJkJa-sEg9tSdns_9otZsqEnuTm1F6pSFu5QxqiL0J86D74kEod-wEhSfb-9AnZeT38mRrdN77XZL8cISdyjb-5gODBkr5vtGpN3P6OScPS90v-UIlX-7mgWOd_o_TRUOZTFJu942PU6G7G2gENzyLR2qXwMozISvgo1ViXOJutm85HFgyAaodJj6N1l_G17yHyf632Suzxe_Zf-0VyUP7f97K9zzwqbMBSPkkPZ_2Obr8XBfFxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9Hjpn1Kf7iE5D4raGOlgJAYl4zq2AUQkMfL8iMojqbvShb9IUW0OkWq4P6trIU9wB71Nvszv4p2AVs_Vmg5O93UnaEa6gjq4vmIrzFsQYIC-Uqt_OJ43N-4ltX9SUEQP3zSihGSdbzq5wmn_neyRuQGObxIYB81uC9a4NA8mAFvbJI8TVy2K1T16r09d2SmcvfZOMC8jPqH3TpcqYd7f-hF3YhnbNPjXdaSOc41shrvUUbDA0Avum0Qt2REJVAbKZTjBQ1-7QD9WyaWRBurZJ8S8DdXYfQSEEJCXUCl-XfCtDCO5r12BrG-OIY-AOjap6E__zvMfoXtElHEzHl0kMRHOVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9Hjpn1Kf7iE5D4raGOlgJAYl4zq2AUQkMfL8iMojqbvShb9IUW0OkWq4P6trIU9wB71Nvszv4p2AVs_Vmg5O93UnaEa6gjq4vmIrzFsQYIC-Uqt_OJ43N-4ltX9SUEQP3zSihGSdbzq5wmn_neyRuQGObxIYB81uC9a4NA8mAFvbJI8TVy2K1T16r09d2SmcvfZOMC8jPqH3TpcqYd7f-hF3YhnbNPjXdaSOc41shrvUUbDA0Avum0Qt2REJVAbKZTjBQ1-7QD9WyaWRBurZJ8S8DdXYfQSEEJCXUCl-XfCtDCO5r12BrG-OIY-AOjap6E__zvMfoXtElHEzHl0kMRHOVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLIxlBYJmXZN2sRnQcmeET5s_PkUgGrqq-Z3FbkCwjx5Z0rPRudT267YCbdra0xjevBkkvhZ9Df7VLRnod1u_JUHgSTygQwlJ252LKsctoANfL28mzwKuS0zSlrxIQ16LdtYZeST0hPTGFbK7SRWb2a4FlFZxY4KmI7iF407hune8W340-4psnGwX_quB3HK93AhFsdM9KPSwU--ITzpyzbTWRtBVJiiSNz5I-RdNoCIzDBCQLtDLvTIFomvLf_wduZUk-SpTgb3_0jIcJbN91hjPZZ9mLdGXgdSghNFLyBQG761KEbrWmh98iRaSJCQ5zo1xdMA1ZteAoT5ZkU30yaaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLIxlBYJmXZN2sRnQcmeET5s_PkUgGrqq-Z3FbkCwjx5Z0rPRudT267YCbdra0xjevBkkvhZ9Df7VLRnod1u_JUHgSTygQwlJ252LKsctoANfL28mzwKuS0zSlrxIQ16LdtYZeST0hPTGFbK7SRWb2a4FlFZxY4KmI7iF407hune8W340-4psnGwX_quB3HK93AhFsdM9KPSwU--ITzpyzbTWRtBVJiiSNz5I-RdNoCIzDBCQLtDLvTIFomvLf_wduZUk-SpTgb3_0jIcJbN91hjPZZ9mLdGXgdSghNFLyBQG761KEbrWmh98iRaSJCQ5zo1xdMA1ZteAoT5ZkU30yaaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=U-NXumjbAvPb0Y71HzHDO3-2QbIIqd8McFozcl4baDVIFcvFTB0Ub1JI52PL5eH1wrO2xKK14az3pb91EbITo-0iWGXkg9jPMoWt_geYJY6DmVQhQ0WBp3OlJqjWQnjgYDxi9JKRhzzPjLzxFwXX1pw-D6ShkbI6FZVXSd-wdBMQ7LHGwWPNIdnbTuxXY0sF3104tmfp_RGLTKwcKFIEFy-km6KeAMnWfe3BmnbGdqc7nkiY_sMtMsoGWk4RjJhhh_hPabhuGmcvA40J5qQjynyAq_krLUVg3koRzXRk4axUWiU3YnCzkfqLyAgMH0XlzJoYejcNINUP8QJYx4oSfQNcZWGlc7LB2iGfkh8nvkmSdEKLfd4FGAR82lVHMsLcaFSViqtrFoqHmuLNnxT67-r4UWxlvXoMyImkbwECBs_DKFoTKf0zdomgZZRdaVSc-SbyQxgXI9IYQMjpUrG1lPKIvbWsfbn7f4sIk-KDcdH6fGBQPMJ7ve_fhOYbthPUHYMPvb10KbzZ4MNiU1t0EhkmTkFh8ij_nVNzcc7rYVNi7VJTdyOLo0KNiFmQNAySkWpjHf_hVVGrSy2xc2BvKN-G9XP0KRpU4KgWRdffUafPD4FA6XABcy1IWtsm1QDVv5RBFHrSTylL2BwMaWVtiBvz6o7ryxQJbIQqrmIwo7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=U-NXumjbAvPb0Y71HzHDO3-2QbIIqd8McFozcl4baDVIFcvFTB0Ub1JI52PL5eH1wrO2xKK14az3pb91EbITo-0iWGXkg9jPMoWt_geYJY6DmVQhQ0WBp3OlJqjWQnjgYDxi9JKRhzzPjLzxFwXX1pw-D6ShkbI6FZVXSd-wdBMQ7LHGwWPNIdnbTuxXY0sF3104tmfp_RGLTKwcKFIEFy-km6KeAMnWfe3BmnbGdqc7nkiY_sMtMsoGWk4RjJhhh_hPabhuGmcvA40J5qQjynyAq_krLUVg3koRzXRk4axUWiU3YnCzkfqLyAgMH0XlzJoYejcNINUP8QJYx4oSfQNcZWGlc7LB2iGfkh8nvkmSdEKLfd4FGAR82lVHMsLcaFSViqtrFoqHmuLNnxT67-r4UWxlvXoMyImkbwECBs_DKFoTKf0zdomgZZRdaVSc-SbyQxgXI9IYQMjpUrG1lPKIvbWsfbn7f4sIk-KDcdH6fGBQPMJ7ve_fhOYbthPUHYMPvb10KbzZ4MNiU1t0EhkmTkFh8ij_nVNzcc7rYVNi7VJTdyOLo0KNiFmQNAySkWpjHf_hVVGrSy2xc2BvKN-G9XP0KRpU4KgWRdffUafPD4FA6XABcy1IWtsm1QDVv5RBFHrSTylL2BwMaWVtiBvz6o7ryxQJbIQqrmIwo7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/POPJkXpF_i_2ju3zPADwafGkULelIcswHUGMnbGSbalI81Gr8shVDouth8iSZ5Hv_mrIIotbdbw6iOi3-yDq7BvRhinNT537GWBfnIiB-81QE8hcp2QjLRcp21BufOsa6rvm66jQz2I_wXKCOxcv5iDcXCBTFLfoF4I0SwNTNkhQvpoLWB-fWrrmFtyEAOXnKPUgsSeb98hety5AKNGiFTD7ybOopFejf-TdV98_1569GBWgXtSDg9zG_qhdDwfyg7NBu-9d_nD05_-tt0A-6cXDZ5qRskaWX6QUO5PzzK18QpEWVofVc3Bxwxnl_-Zc4q1IGBeCshByJUHVgXgqmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqYXJrrxHbV5M5TvrM9zJxpP3q9Tj36TztnIwh__hKOUokVGjNt4HtTSa4yzDC81qe2t6qsyy_YO6ehuIRWL7xZNcLLK0OvcfXEYuOwBzvseI6xQXR2o5Wcr_fqKdKi1hhV4ITPAxp878TsaYt7fGwkwkRjqLyGeSpm9OiT2_ANzWe2mM4wko3fH5rabQ8juNRfeYqjLPcWYe1cQQ79Idy3uekJUSZBAi8jxrgpdmaz8GDtJ9SOD4Nde-Deav94SVb4xGBUJarJwR91teWeHiak0aXigb6NsxVEl-sngjxqdANvq9M0T23O0YeKbyo4BTra4dkZmvAPO0OmwbNRisA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=v6yiptGH1j-JwTa2t7h_qQzHyudGpERuq2k7Dst22Hf02dQ9Hokh2Si4Xh-JjsrGe5n6mHueDEt3BqtJOIs4C0dr_WpnX7YOckRyRUW_DqtcCHMIj26RIlbnp-uGw7eTf6MpWJjL0pbo-RgzetePoh8fUza6oZS4CKMTJaUXjYSKuM4QsJ4yOnqLC77qGR1a_XufZch-Y21lveN3vkSigjAfW1gb3RWkH9BKlkBFA3twuzDGA7eR4vdCdyzhtgO3wbwij5Yl8w5Bv-OgfZQmWOOisFhxB767iV9Rt1H24Ui2wCqoRScPOBpOY33sL78iRzjb-8Ipl5oM0C-QgMeuoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=v6yiptGH1j-JwTa2t7h_qQzHyudGpERuq2k7Dst22Hf02dQ9Hokh2Si4Xh-JjsrGe5n6mHueDEt3BqtJOIs4C0dr_WpnX7YOckRyRUW_DqtcCHMIj26RIlbnp-uGw7eTf6MpWJjL0pbo-RgzetePoh8fUza6oZS4CKMTJaUXjYSKuM4QsJ4yOnqLC77qGR1a_XufZch-Y21lveN3vkSigjAfW1gb3RWkH9BKlkBFA3twuzDGA7eR4vdCdyzhtgO3wbwij5Yl8w5Bv-OgfZQmWOOisFhxB767iV9Rt1H24Ui2wCqoRScPOBpOY33sL78iRzjb-8Ipl5oM0C-QgMeuoDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=jCGJqr0EpO5BsOi15hu0Ygvp42EyvltRGFiNausjlDikldR26bTY1nNEf7mMDtXE1zFikQZmx64TQt9naK4YMJA5pY8s0Pa8Vaxr07bqhim2jMfvx5NwE8QbYr61y6a7WoW4Y7Aw7PDNHbzcDosqvzTtPVBEi8RAhpwgSBm6o8i9SPHJ8_0RnnIo8CE7dVFoCgbIWiEQNhVLWrI2l2g1AcSmzbxOSscd0KlSf-Jvhisiq0t8g3cLoZ2ZnwbMa8X6gPP4-TaxqcculGL6V9hCDcu7HF4gm7_2b_cWPfjDaVrsKWIO7XGmJAiJIj-60pHDWPIL_8XOziXLsBSiR36UxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=jCGJqr0EpO5BsOi15hu0Ygvp42EyvltRGFiNausjlDikldR26bTY1nNEf7mMDtXE1zFikQZmx64TQt9naK4YMJA5pY8s0Pa8Vaxr07bqhim2jMfvx5NwE8QbYr61y6a7WoW4Y7Aw7PDNHbzcDosqvzTtPVBEi8RAhpwgSBm6o8i9SPHJ8_0RnnIo8CE7dVFoCgbIWiEQNhVLWrI2l2g1AcSmzbxOSscd0KlSf-Jvhisiq0t8g3cLoZ2ZnwbMa8X6gPP4-TaxqcculGL6V9hCDcu7HF4gm7_2b_cWPfjDaVrsKWIO7XGmJAiJIj-60pHDWPIL_8XOziXLsBSiR36UxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=YgyK_sN7InNxciXOAWMI7sxRklF0Ah0jLiuYS2hUpJdSx8bN8A_5p6qlLFBQqKPt0V6K6GtpneKPkniuUZksqVLp8P4vn6NlP_9_uciY7Qz4zhDyfRZ1aQEE2PHndKLJmIKwbRvWdSVGqCDOJxkR0yQAK7f3mDzKu7MARpPgORYFbTbfU9wrHRkPANsSrh5uzOUSB88KYrX7PO-_e6PN1NhHXgztkL4IbCXLE9d-_LCBtjfFHi9w7HhfGNiaRKY8KXPoBmPVEk70C7A-cNb6-c1qLJGJQMbgkTeFONrk5fwpUSABfhL4CmrZKiYGtqkFAyTLs0rpUe39BzZk4AjTjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=YgyK_sN7InNxciXOAWMI7sxRklF0Ah0jLiuYS2hUpJdSx8bN8A_5p6qlLFBQqKPt0V6K6GtpneKPkniuUZksqVLp8P4vn6NlP_9_uciY7Qz4zhDyfRZ1aQEE2PHndKLJmIKwbRvWdSVGqCDOJxkR0yQAK7f3mDzKu7MARpPgORYFbTbfU9wrHRkPANsSrh5uzOUSB88KYrX7PO-_e6PN1NhHXgztkL4IbCXLE9d-_LCBtjfFHi9w7HhfGNiaRKY8KXPoBmPVEk70C7A-cNb6-c1qLJGJQMbgkTeFONrk5fwpUSABfhL4CmrZKiYGtqkFAyTLs0rpUe39BzZk4AjTjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=HVIOOU004M7W0gddKozb7DkwdQ5gxQmL-SfO_o_fUmqU87qSJHrpZV2z_O4X3POwiV9w4B6mXFy9DNnfORkkDWx_m9nuqgi8pnT7keqQmUdG2cMgzKS4XAE0r4GYRvC95BsZZiszFPVAU0eS1K0ct6rq9aP8Q9bZ_hpWwZgLdKkThobn8oZN9_K0lBZf8O5Y-XmNaF25bguDZWaxJ0h_Q0-OVbIBPSg2fH3oIRychs4QxmsqNTHlIRR4VGnhiS9l_2GpIfM-WwW40jP28tm6gcW-lwZZGVWA4Ijq4C6mm3pxrpMOGKVmMjCoRfr6KflmzoD-nITYDBsyHTGdjJjePA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=HVIOOU004M7W0gddKozb7DkwdQ5gxQmL-SfO_o_fUmqU87qSJHrpZV2z_O4X3POwiV9w4B6mXFy9DNnfORkkDWx_m9nuqgi8pnT7keqQmUdG2cMgzKS4XAE0r4GYRvC95BsZZiszFPVAU0eS1K0ct6rq9aP8Q9bZ_hpWwZgLdKkThobn8oZN9_K0lBZf8O5Y-XmNaF25bguDZWaxJ0h_Q0-OVbIBPSg2fH3oIRychs4QxmsqNTHlIRR4VGnhiS9l_2GpIfM-WwW40jP28tm6gcW-lwZZGVWA4Ijq4C6mm3pxrpMOGKVmMjCoRfr6KflmzoD-nITYDBsyHTGdjJjePA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=LBpX7Pk7PBinVehpRp4SHBMdpN513k6z7NDtJb2cKAsq_yakWZcQV7fNRv_9mN-psn6wTyQnUwNXs9Ns_1qO92DzXQbu409OuiR4pvEQWZgaNAuNMrySo8c0J05HSiaEL-hvvM8Fzs01cHfcgyAAW2urNwzZNm2qrZxPEiF_uUSQtgKXn5T3XsY2WFrNcMag6wIWLAF3bCmLMdHnFjSY1-_Rv-XfhzBy8WV64zY-hKde9LSH7pInWpbPhzttO5Qc-mbj9OHI10KV98t55LdKWFwwgO-lBc4jnhh3mAfJB4V_K_oyzQfpp1otChnVkDozvTZt0kbj8L16a4TYN6095A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=LBpX7Pk7PBinVehpRp4SHBMdpN513k6z7NDtJb2cKAsq_yakWZcQV7fNRv_9mN-psn6wTyQnUwNXs9Ns_1qO92DzXQbu409OuiR4pvEQWZgaNAuNMrySo8c0J05HSiaEL-hvvM8Fzs01cHfcgyAAW2urNwzZNm2qrZxPEiF_uUSQtgKXn5T3XsY2WFrNcMag6wIWLAF3bCmLMdHnFjSY1-_Rv-XfhzBy8WV64zY-hKde9LSH7pInWpbPhzttO5Qc-mbj9OHI10KV98t55LdKWFwwgO-lBc4jnhh3mAfJB4V_K_oyzQfpp1otChnVkDozvTZt0kbj8L16a4TYN6095A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=aZqdB5-l7EKCRO-QjpTR07-rXBJ-_LkZ6N_xb437bYku46FzK68OyjHluap3zMy-p7VCG4yIj8u9MODU7oUUaurhbHhzDhIgSFGOxS2Fk89zAtRJiX8NDvpQsikbTe1cWa2JUky32w0mDlE1M2DWLc1xCuNjr5JSmthryeiVO_5pqRSL3v40fd5M7WvTnASvHlVqJUU-yJVLbZOj-2DY1BdFd2OgYlQMFmVMxRxYvOBjGmohZ6Ac9kGomwF7xv7RgPhVHmUZsl3NxD1757DTpIvFuRfvXseFwGTALCBst0O-snf5k300trJOH2yCTAdxf3D47sgII3yswKLnSOayDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=aZqdB5-l7EKCRO-QjpTR07-rXBJ-_LkZ6N_xb437bYku46FzK68OyjHluap3zMy-p7VCG4yIj8u9MODU7oUUaurhbHhzDhIgSFGOxS2Fk89zAtRJiX8NDvpQsikbTe1cWa2JUky32w0mDlE1M2DWLc1xCuNjr5JSmthryeiVO_5pqRSL3v40fd5M7WvTnASvHlVqJUU-yJVLbZOj-2DY1BdFd2OgYlQMFmVMxRxYvOBjGmohZ6Ac9kGomwF7xv7RgPhVHmUZsl3NxD1757DTpIvFuRfvXseFwGTALCBst0O-snf5k300trJOH2yCTAdxf3D47sgII3yswKLnSOayDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDkcWfdMKM6hb4PReJEA8HJ7wKpc42YwbCDNGepVVhwvSpgex1fVnup2_jNMaJ3CwRi-DuoE4mcIZL3nR3dJfij6DeNtgmEgmY93th0_TUH3IwM1_Kiw8BP7DyaXfh6sesuc6nMZul3Paq5xUlM7-sCDX-T9ua3xrUD7MCrXWY-3EWx17MDiNvp-v7_PbyrDMSYiB-1zCZGW2h2SSkInkhstqJL7GBzbibIhmVibuBmEA3u8QIYc-ng2y7nLoROVnbcf-HexEcid1N4avvU6kZ53LfiSHNTIrCkxzGtwTck6EQZD2eTW128p-kikZMrKDXFQBViQWEQhHW8BsQsL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfnivghV_DkQqx5KOJqPOfgEYLLnMar6qzwwQKxYa2cMsRfJk66ik0Nxjsgh0JuRkfx565D28qXCI1VxxVM-AO7nnjXyI0XVe65dsyeQlG5zHsI6w6hiCQBOTcOTalu61RHAMFJcIls0ezsdUzhe4jGSZCI-qshBxj9dcIZ2ff4dk5YB-nkEH01HoXUxfUHjVZlietb_hLZBJENP7rOhuNPZAZN0QLW1wL5hJd57KScVM-Ourq0qOexvev7BRQ6vKczjsL_lfswAqEOd2ngXceGZiR_04qM1n7P7PqV5IJd9kOSfzZeaJ99wuvU4ojxrFb_qON9j9dpiqqEzglvT1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=HwBN-BddKu8tsfqCj-PuIbzqF6sZUQ7xRF_rbThnAbM1N32pTuG8r98XMmn4Vz9kE4ARJjIG7QDuHH6R2Bw_ZbbfWie2M47_IDzWSUJr_Ho9Bwzv8Vo5ohMpi47OBPtTBIIJ-YVSoYUnLcPXWhv-cm-jGiDYDLcBb5wBfatxc4X3lCm7jnCa_CbnA0fXZ3Vt-P6oOc9QlKc-qevNgoF209ncTMnh5tP0TdxBSRMYXUV1vH-Ge7pV_HGEwQPgbxDjLW0mJjGjF-VdiUqGUaPhKWJjSCDgvPxfsjW0Mj8fggfFiB0B9sH0TtQn80t85vo6iZla--b6bVeTbItFQXAfPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=HwBN-BddKu8tsfqCj-PuIbzqF6sZUQ7xRF_rbThnAbM1N32pTuG8r98XMmn4Vz9kE4ARJjIG7QDuHH6R2Bw_ZbbfWie2M47_IDzWSUJr_Ho9Bwzv8Vo5ohMpi47OBPtTBIIJ-YVSoYUnLcPXWhv-cm-jGiDYDLcBb5wBfatxc4X3lCm7jnCa_CbnA0fXZ3Vt-P6oOc9QlKc-qevNgoF209ncTMnh5tP0TdxBSRMYXUV1vH-Ge7pV_HGEwQPgbxDjLW0mJjGjF-VdiUqGUaPhKWJjSCDgvPxfsjW0Mj8fggfFiB0B9sH0TtQn80t85vo6iZla--b6bVeTbItFQXAfPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=g7sHmbo_Yq6xrgzp3zBUn0t93gZMbbBXSnvHY_83o2VFp-nkHtL9jGhl7vWjzU-GtN-A2mPGi9lNaF_JBy290ogOWHZZkbtk0NpFmO6HccLdBbifHzpUnDeCnlkJifjlxmF6QPLL3o1IxOStrJMxFGqavRyYP-ptcoXCfP2iyd3--Vc9RM9cHH0iVBhZ7mFSRWokl9ST-0fpu66bvjw58FaVH9sDRTwRMO526kgsmSKWDja4PYfl7Cojwu80mhuKOoPbBl33PrDv9HJ1ZwvoApKtn5T_HCWG2aEJhyHUIYFScmHhnsIfWhCgZ5q4LIj00iUBfOKtGEUR27F1Axj9S3IURlif1t_qTCoocbkpMCngt2YxpJEnVpLCjIa2VmXpAvhtt8UqGKdtge9kTk3OzR65rj5FarfkxLZiroutE3Vg_4gYT9qkYq2k_HDwcuXUaRol6C4A7nWyuyclvC697J5irYnqtYHKISvrrwJqtWxawUrvbrrd0f0zjWpyThuqCAroObTDA51J-9CQ1ZC49Xo5tD1IJYSw2fMwU7hwVx6jrmlRDBuFhwLChPlVu8aX7e7qsz4GgnS8wybvZT1Ij0AUm9DsbwmtYcBklGowkWwtFa4ECPKiyXo4_4YYidbVt9OYp0_ahdR4r4N9bvkFKJrSiGQcfJE5QmySgHAoHUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=g7sHmbo_Yq6xrgzp3zBUn0t93gZMbbBXSnvHY_83o2VFp-nkHtL9jGhl7vWjzU-GtN-A2mPGi9lNaF_JBy290ogOWHZZkbtk0NpFmO6HccLdBbifHzpUnDeCnlkJifjlxmF6QPLL3o1IxOStrJMxFGqavRyYP-ptcoXCfP2iyd3--Vc9RM9cHH0iVBhZ7mFSRWokl9ST-0fpu66bvjw58FaVH9sDRTwRMO526kgsmSKWDja4PYfl7Cojwu80mhuKOoPbBl33PrDv9HJ1ZwvoApKtn5T_HCWG2aEJhyHUIYFScmHhnsIfWhCgZ5q4LIj00iUBfOKtGEUR27F1Axj9S3IURlif1t_qTCoocbkpMCngt2YxpJEnVpLCjIa2VmXpAvhtt8UqGKdtge9kTk3OzR65rj5FarfkxLZiroutE3Vg_4gYT9qkYq2k_HDwcuXUaRol6C4A7nWyuyclvC697J5irYnqtYHKISvrrwJqtWxawUrvbrrd0f0zjWpyThuqCAroObTDA51J-9CQ1ZC49Xo5tD1IJYSw2fMwU7hwVx6jrmlRDBuFhwLChPlVu8aX7e7qsz4GgnS8wybvZT1Ij0AUm9DsbwmtYcBklGowkWwtFa4ECPKiyXo4_4YYidbVt9OYp0_ahdR4r4N9bvkFKJrSiGQcfJE5QmySgHAoHUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=GTQYLBhp5kZuH7QVtqXgHwkX-8Frjoj4toCVXrvY3rTt7JiM_--nQyALnWbaTT76eSdW-3hf6xelF81OAsnZG-YbWHgZ4yPv5zumaXnWOzEhkR4ci2d55nevefdKemLUSttfb52WgcQqQP-hpkUY_5ep0FO2hhJ1isgyAKpMdB0t1kEUR2q79P6U0PcaljrvS-Prwh57fhReOHHqcOAFMM9kFXVVzaOkFVjLRLBF_yY2juPifUGroKJ2cx1Ot8xUtE92GfAW5mci2d-nT80TrJiRaaEPxx-na5jNc1XJPoA2EbZyV6cPBsLKMPAHWvp9DsXK6aZoTb5U9378tjns8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=GTQYLBhp5kZuH7QVtqXgHwkX-8Frjoj4toCVXrvY3rTt7JiM_--nQyALnWbaTT76eSdW-3hf6xelF81OAsnZG-YbWHgZ4yPv5zumaXnWOzEhkR4ci2d55nevefdKemLUSttfb52WgcQqQP-hpkUY_5ep0FO2hhJ1isgyAKpMdB0t1kEUR2q79P6U0PcaljrvS-Prwh57fhReOHHqcOAFMM9kFXVVzaOkFVjLRLBF_yY2juPifUGroKJ2cx1Ot8xUtE92GfAW5mci2d-nT80TrJiRaaEPxx-na5jNc1XJPoA2EbZyV6cPBsLKMPAHWvp9DsXK6aZoTb5U9378tjns8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEMlKiFF_PFyXL7qOezB6JZx602WJEvY8ibTiB2k5IhfZ4Gi0V27U4UP1faf_FDLydGHxW2i__0dcW0QpqSpQPUhEHUyM9mM4VheFA1q8RTi8K4-LfilF0roMifwIZpLYAu-AI8XRrFU-PdfiFwadtAUBqJoI1PvuFwvIueNo6k6L2sJQP3qVu9OehTGn-supa_Jux-JkeJqNqE69_RoRXkkK7-5R9tZQEPXnRzcwFfnY8GmktT00DXMGO_dvsdKdHwTwA87FqsXAxpfSYAXQ0EAtU1elOeMQO5gja6sfBFv8BjsZ8wBCc50MYU-TOGdlH6tyryDCcmLcOgABMpVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=O7TscEDAc789sogqxP-X6TLwzQ25zuCEXpTvpfPwcGK2z7V3XS2e0ZzzQFq9GOTWEupka0gY_CxvyZGWxExYg_Yryrcg5-fqv42bSJn-MX1STYRT69Nq-b1b87pgQpNAwQMepAWbdYRoM-Gzd9KPpddWFj8usJyWt3yUYrnKfoa_r45HVV5U3QcwGtR1ZoRwHG8oAG_bjaQRWQJGf6Dg0WkU_59_O3rtMa3ZxvfZ1flj4KW8xk1r7VGeO9uulS-KEUfeHE3REopjgU8asToVamHmr__J-5r2SxIaLoNeFTxiybF3EcYuYLbB9OS541pLaqfAWy05uw1jWAq3zGDCKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=O7TscEDAc789sogqxP-X6TLwzQ25zuCEXpTvpfPwcGK2z7V3XS2e0ZzzQFq9GOTWEupka0gY_CxvyZGWxExYg_Yryrcg5-fqv42bSJn-MX1STYRT69Nq-b1b87pgQpNAwQMepAWbdYRoM-Gzd9KPpddWFj8usJyWt3yUYrnKfoa_r45HVV5U3QcwGtR1ZoRwHG8oAG_bjaQRWQJGf6Dg0WkU_59_O3rtMa3ZxvfZ1flj4KW8xk1r7VGeO9uulS-KEUfeHE3REopjgU8asToVamHmr__J-5r2SxIaLoNeFTxiybF3EcYuYLbB9OS541pLaqfAWy05uw1jWAq3zGDCKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgmZNJm7T4Bt-bn-hQgDHGF4OqtsI_dMiQ_NCr99FaBkC4uTX2RUaBaRsR6-5TWRp1Qlu412qo-R1q5dT_rvSabhUrU7ZM_lYB_hG9kz4YKs9M8mGqBlMYo_n3_mFJpOc2ViHWlUb4xvLf0vgdG0mMKbXC1ROY91GgggtjksqVRAy5ZYmmD_5yA7rufgD1TGgL-xoqVLtxgKsLs0FkpyQoELT7LFKyXFJ7e5uLcMk7-AGFnTNWdAWQ6OnlI9u7IagnAMK-xFkOz53XxOWaPjLQdwPELf6CT1PBbvTV6WeWNC0nKcvh-LIFZSkdRNlsA_krdvzspnN4Z2aTt88Ol0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bQemOpvPyKMObsRcVr9MGd6NVpYxOpgtjSrw0A06XAwYRpWC-bE7OgwYbDMaxzp4qu942aZNdFVmIJ6QIGeC-K6ZF9-IMkaAoJTFjaLmWieR99ZTHCh82Chr7bIgXT4sDrbf9gYzmXozptHOCZJkSbJ-fJGWY81hcEO64GuLfUA01unHaSTALcnN8N8c-P0E6z6W9wIeznZ_kSbnptAdf6rXuYq1_Vxil5x3bna7sHuQ_MDGQna9Ct47A0-yhHNNsHlCOR4FuFP439sjmh-AtBL5g7kusUtMoe-KpC5wWrNLG48cXDDFNYRwZN9eDsX9ppVQB5E19_J39EPiVMVsyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=uW6vGtX5kIk-joNvmwLPQ0zPeJ5_kGCJwqiYcJwo5iQfnCVXePDAttT-YOHlfCgLpqgo-0GYQpsEaUlL8kVPAfkj1O5S3ffTDq67kw37gUAZvxKgvbKgmgR3Da927wiq-YGwbmRU7cU5N4MOlm6sQuTfkogVq4DhBEXaTFI2uGc2dJ5NaQe4TCCWHLr4gqwSdvaRGRUaDOFkx4lBpHsIbEzYl1myO7UQ0fZnxdiqOQX-j8pmWSWsiuIeUKoifaavvaskruNzZ5G34MmdUbsn8IVmQG3B0xR9vvPNtPYi_vPU5TMpid3cn-Ta4T60CtquOi6iiCr41gKNAIjMFKxB3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=uW6vGtX5kIk-joNvmwLPQ0zPeJ5_kGCJwqiYcJwo5iQfnCVXePDAttT-YOHlfCgLpqgo-0GYQpsEaUlL8kVPAfkj1O5S3ffTDq67kw37gUAZvxKgvbKgmgR3Da927wiq-YGwbmRU7cU5N4MOlm6sQuTfkogVq4DhBEXaTFI2uGc2dJ5NaQe4TCCWHLr4gqwSdvaRGRUaDOFkx4lBpHsIbEzYl1myO7UQ0fZnxdiqOQX-j8pmWSWsiuIeUKoifaavvaskruNzZ5G34MmdUbsn8IVmQG3B0xR9vvPNtPYi_vPU5TMpid3cn-Ta4T60CtquOi6iiCr41gKNAIjMFKxB3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=uNumiZcDEVcVti6nFjDOfKIZANhBobyFGjb7da-ajFkrVuYD9cKysZrYkGDl_QnOmiXdUiD-mIJNO_SvYn-hKZ-LsJngFgLQUPDs5Xt0oLuqkogvJsMIpPdH7BOY_VrbQBulAO-zbipclJpkVMl0W33h1nzQogxnIdVJ0f2CKQyZ8maHo29jh47hMWZXk9HhxLQZ6CUbo_n5g4JG6SqpeFP_ZD8PHhHpst6CT_hqclAda4z1LwX1fDt4Mx2UGVoqH1rxLaLr1KQzTuUB7OV17z-Rax-TRlP8BpY98kiw9s1SUKafFoAUF1yF1mHE4TqcePv-gns9mybsO92JmnlFrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=uNumiZcDEVcVti6nFjDOfKIZANhBobyFGjb7da-ajFkrVuYD9cKysZrYkGDl_QnOmiXdUiD-mIJNO_SvYn-hKZ-LsJngFgLQUPDs5Xt0oLuqkogvJsMIpPdH7BOY_VrbQBulAO-zbipclJpkVMl0W33h1nzQogxnIdVJ0f2CKQyZ8maHo29jh47hMWZXk9HhxLQZ6CUbo_n5g4JG6SqpeFP_ZD8PHhHpst6CT_hqclAda4z1LwX1fDt4Mx2UGVoqH1rxLaLr1KQzTuUB7OV17z-Rax-TRlP8BpY98kiw9s1SUKafFoAUF1yF1mHE4TqcePv-gns9mybsO92JmnlFrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwQwqwJdY9LYBf_dX195tdSQgCbP28B98d4JCe3noURYp9VUMfbD85opi9dRL9EK3fgnX5BNQcZc8OwevKPJArMpkAQyJZwNhR53W65n8w5l5NYjSrGklfFaCAYn6kIFhII0uMzXEuDDIJJLaOFUNAcgk7oKhIXh3Ncq58OMnkWtcq0J_mHzzkjrwBw4dUCbGKmHJ_t4X9g8bBf1Nbfveezkoc_PElXf3peFMYUIDwviig13JAlu0lN1ocEpNWrP-qIhUjLjAOsP7fZc37OlUbXqX9OfGAhsSwZrcVk4livyXw6_qdiZpLvG_-CKhQWAD8n3-kvZ4Y3vxV5Sh1-zPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhS2p12twQwKD8FIikxH57SzykIV3sWdv7ZrMAKYO21PJaZx8E6HdBwu1fj6MNgaiIAfpvycX2dbmFXwhGrKl9NlVUwTo6NqHoa64vKvig3t4VEyaYmtIT8FS9n3W404sj2IwWibdi-q6z96OOVOCri9G6Wr25Cd5hXQrb3SROSJy6LKvoLjq7QWRQ1qj87Ah3kW_faclx24B5LrltT5efpoAyOecnL8uC9tfDSs3OlX3aQkoinHYiAoIaKQCgyj2_1K5gYL8ZI2JCuaWA6k07jGBQaAf04CMN7PfO_nrBzu4alcLbfYPISN7C5ue3nVxqZ7TYEOypIG5h-njfi2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYBUZVmKfMtgWgWW2Q36F9l6ZEDscJbg27uAeEqdZWw1ba2t-Q-MbKtZAJhDZBmDjd32rUuZkciWjbThgZroyOSw1eiJAHrPQvLpZsgTo1T4vqZ58bdMUuOspyU_m4gkUAIs6Uw_bMpu5MLtDn7-pOvSN5EAgZZrWaNTm1FTop9BbT05_EMx3pneKpNtMVB0GojZpFCIE5XEX9Tppu6KuhnaATf5jiSmKap0L6iDFft63NDGhlrRl1emPWxqWGJjo4-Iubmicrn8hKj1SdCF44iXiBWo8F9IihRejzZamq2C2IWd4jgTvvytmKa8wayPx81IFrO75QGJ--juwotc6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=cjQY7AUuxKYPtw3S5Yftqrv6CMg-YkFDogiGm4xmFVLv58nOqWklLQkrO_wQdd3x_bQpG0xFezyDSFcsyz5DD7iy-Jdavl8x9MVqw5eqAeSjj8E2MfLFyFgPKn-knO4Z5VQNBFKztz-PqlUYussOuGHyLcyxgWhraOVJ2kZ_PhSfC5w8zvyDaAvOx1Leq_Jmn-3YaMIufXBxjoW6IqEnglcLaPQ9j0buI5G-TE6WEWPI_Nv54tcomI7KOe0Nfj9w6IowWNTRt_zr9I7EoBN8Nw7gvXtjx4opaXQr4XFxcZnM4v8LN1Jw0Y5h2UEaZco23x_tBd6ntiS_t1HIiuCCyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=cjQY7AUuxKYPtw3S5Yftqrv6CMg-YkFDogiGm4xmFVLv58nOqWklLQkrO_wQdd3x_bQpG0xFezyDSFcsyz5DD7iy-Jdavl8x9MVqw5eqAeSjj8E2MfLFyFgPKn-knO4Z5VQNBFKztz-PqlUYussOuGHyLcyxgWhraOVJ2kZ_PhSfC5w8zvyDaAvOx1Leq_Jmn-3YaMIufXBxjoW6IqEnglcLaPQ9j0buI5G-TE6WEWPI_Nv54tcomI7KOe0Nfj9w6IowWNTRt_zr9I7EoBN8Nw7gvXtjx4opaXQr4XFxcZnM4v8LN1Jw0Y5h2UEaZco23x_tBd6ntiS_t1HIiuCCyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=JsDDV_9KOhuWxzqnrVMUeAcGvOXvFIapdAVWW0W0KrXPYOQz-_jF0wRDkWBB1p_i5lt-xbjbC4a86qPmhxXNwio4o_lM8lu-buoSY4LaVajuf_l-Tsd5lYjr06YRl6cJpyE3jLTHgkORjSoP2V6sGv-pgGqkntNqjEzcq5_u1Tmsr77NHk8W5g0smr5AutdR8ukHgLTnDne8FRFFHB0X4E2JJ_yuYsHmkbzklrhjYrSrARvpApfCaJfhsrhPNdYDC_HkZ1Li_Rv4kMUXWhW2V0T3WkvBPR6P4q_-98s8ExX7_D5BKXB9TIcigssXUzMXNjWdI2ys8ff0keC4MjAy1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=JsDDV_9KOhuWxzqnrVMUeAcGvOXvFIapdAVWW0W0KrXPYOQz-_jF0wRDkWBB1p_i5lt-xbjbC4a86qPmhxXNwio4o_lM8lu-buoSY4LaVajuf_l-Tsd5lYjr06YRl6cJpyE3jLTHgkORjSoP2V6sGv-pgGqkntNqjEzcq5_u1Tmsr77NHk8W5g0smr5AutdR8ukHgLTnDne8FRFFHB0X4E2JJ_yuYsHmkbzklrhjYrSrARvpApfCaJfhsrhPNdYDC_HkZ1Li_Rv4kMUXWhW2V0T3WkvBPR6P4q_-98s8ExX7_D5BKXB9TIcigssXUzMXNjWdI2ys8ff0keC4MjAy1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=WAIDYJ2tqOGV1dbeqrj0H8H4Rc4m1kR9TmOIEkw4PYrUWxbdAK2a1z2XAx0yZyW1Nnvi66JTjRCoq_HXQDBB3ifchG8IGAuL6ezBMi_nsB2MiJGLXo1NcKQ3itpLF3PX7uAcgdNT2pYtSGeqD1jgkbQsmuCZo6MWcvNYJ20jHbsl4KDqmyqMzcM7fJocwM8WToJQdsD_TVOuMdbvVOfpBbcp7h3md-xHBI9laCqDNNvZSyDt7LaH1ARxgb7uR7dpYdo-THdVBqu2KmAXXD5GzlyXT05xkrmzBnhC8bMnoKTlf-vlRdNSjVb0pLfD1Nzi3fMglgmSLNwqeJZapqgp5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=WAIDYJ2tqOGV1dbeqrj0H8H4Rc4m1kR9TmOIEkw4PYrUWxbdAK2a1z2XAx0yZyW1Nnvi66JTjRCoq_HXQDBB3ifchG8IGAuL6ezBMi_nsB2MiJGLXo1NcKQ3itpLF3PX7uAcgdNT2pYtSGeqD1jgkbQsmuCZo6MWcvNYJ20jHbsl4KDqmyqMzcM7fJocwM8WToJQdsD_TVOuMdbvVOfpBbcp7h3md-xHBI9laCqDNNvZSyDt7LaH1ARxgb7uR7dpYdo-THdVBqu2KmAXXD5GzlyXT05xkrmzBnhC8bMnoKTlf-vlRdNSjVb0pLfD1Nzi3fMglgmSLNwqeJZapqgp5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2f1dKS385MEQAReioQj2molpP2HlitPDCu7vizh7Tl3uXkRraQsiblU3maFyOKBZoXu7Jf6GPPqMYCi-yjIhzPPjnpXfyPzx8wMa7xvAynjTMh4HsYFAVdX0580Xc8VVhCSHCHZ9iR2eVbp18uK7FEwuCKkuhgtjnHKgerEgnM7IBZ3M8eVFbmSeReseWZu2ifuUpqpRtaDAa9yHncTsm3r3xMx5c_-Ax_9j7xmV0HFX6kuJ9EjVDas_TgMdiHp7eUvs4WaH7jSISA8r4Fov4gf0QagOVUVnylpRfW0xRHJQ63Ov21-wZkyGi2FEWtbN6swID_iUmkmuGTLpvrmNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGvxj0Yl7sIhMF8kmN-YnOQfj2ljoulcrSDKls7Al59TO-XYjnXANMwUt0X4hnA7150yY3yOhdfngtHaHNaZJg_mrz1_8XbumdQF7EeQEIh9eR6DlTlqD9Or2_AE9R6ggyxzxk25I4rqKCxlu5gfnXvFmvFNeQaF4Q8f4GX_ltkDF5Y4Xxo4Fsc4a1g_gLAZXpyI_aZl-v9MiCjx2gNk4QG38i1wPsfhz_BgDy5Rkyzyk_AxqeXwaXFn34qwT1x41AlyN4qtPaEhwf8K8Mx8ZZ9LC9OV-kiV5PMADtu0U-RD1jno6ond4umR7kpKJsyDLnB5QUXI-WTtcgZW1jptEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3mjtfFrooF06GOBZWmRoALEzPbJTtXBs8Y4-BDjny5M0Vv6sMew-KXI-xM5xVVfnul82PJcS7tWGKOapDg_yuFa4oNnx4Ke26bt_4fPLbVjlcfDwsB6topvigTctGCCGANLynGY1DswmxyI3-O9Ug2eh_MTkRu5perghDpgEdcNGQqx4K7vqwrJ4jSiWba2dAZ43W9bKgWfPFsuyBr0BghojSlkL7Pw4b2zv603HvY_yRnP8KJ0l6XZTziNus2PKQ0Q5xrx4mClao7pYlbDQauvTHIQZae32Lu3RGmqt1cnsT0HmovpgZFdRCAhOgtaSGbQSfEOMrXl2gG5jKbkMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
