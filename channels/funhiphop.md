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
<img src="https://cdn4.telesco.pe/file/pzGnC89cWHWwgTakiB4-wYMV4MyEG5q8n517ACjJFe8O_y54u4s-Lv2UGk_ADIvsibavbNG2EdUiWb0-0Zd1dA1eSfDWYioGeDqKSi98Xukxr6zrOQA8Q8EnJDc8_I4mj1iUHVgMOrpTkmMGxwel5cEihli0FDNhhuRw3eAeq1aEG-r_SHBX6vMJ7tKWh8SoI3I1BlBM0ShmqhfiX71uSsRpX-eOZF7AtVDjIrcmNHg6mC6N7J5xhg6kHTDmzQ_nchD3aJ3TtkTaksHSjRxKu-5vMY6_D0dcq3h5zqVLUkD0PUZmKKmsmCvH70T6XP--ky0-_gjoj5nb3_rD9t4yyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 22:28:47</div>
<hr>

<div class="tg-post" id="msg-77739">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_K6SOe1wvCCUaHRUNiGVLTujfEceX1VJMY8ZXsYoIJNudSnolM1BKVsyubgMsKDu6Ou7jJXZpkXnJRojpELZWqjPN3NXEyK5vYOgMN2rUMcvNZetsHM7bS6Pa19Y8iYVBBZ9p8rQm6sR6PzVsI3kEN0xYbO8n6_hmWUUG-dAz9skGLf1I686A0E4TbbzAMfu-biu3ZJppU3QbvurJnGO0m_9KcLi8sZ7r-HpowivyFsS5dJd54SHFx4JW1ha4Z2lRdom9h_lCfDZDkDo-2Vz9ulNMyBNrdL68dEGnF8PP_v2WvmJ2HVyMfvaTjZy53m4lO2fkzo7axE0MIx11o1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف خدایا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/funhiphop/77739" target="_blank">📅 22:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77738">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIK_0l96Msbuid1UXezdWdYBjWL23UUZxNNp_4tf_0lJ6ll5YFBm7Nf4P6aErf1cMedB_gy58W7q59IK9vjnwQ4bEo-0i7U2l_0-RzeXSqjX0yhTLokc_TmNGV5ax-rk30ShEqkHgVxF-bU3qHdlHB6zg8NZMT_bkj1kT_qxdNSa4XVdoFbSL9B43QsExn-kW5JSwDrurLJtMdVOCV5FuLRVQa73wKYVfy7PvYScK0WojTbCZIvC5HUZIyPFJnWN2VYQxzNzp2NKFXXV9myRztJBwpJC328oODvSg2OiAHQ6R5wk4fqyYMSWNixR5hr3CXUTTv8ZiIJ0NvoxBVLsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه)
کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)
هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو میخورید و قید پولتونو میزنید
🫶🏼
Channel ID:
@RezoraVPN
Robot ID:
@RezoraVPN_bot</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/funhiphop/77738" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77737">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید میخوام فلش بک بزنم به حدود ۲ ماه پیش  عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد نتیجه توئیت عراقچی چیشد؟ رفتار خودسرانه یکی از باند های قدرتمند…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/funhiphop/77737" target="_blank">📅 21:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77736">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb26cPcqUrojE-dLGU4nzfM3SKXP07oNUKiicN__3jtlSrlzdIfECeKTT6Ze9UtQBIlPXY9g97je-_-azCfUSaShOIeq764Xq89aXlVBTh32UmbmXV59_pAmDrZWP-ogr7nHLGiDyyjG3ipDEfIO2SJqvnjDPKxaBp6KT_IZ9ED_uIARNSbvpt1S1z754MWdI8TCaN8eb7maLz-onMA4g6hZ_n2L8qYJLmfhvK0FzrgOnWxpDy_KdQYzBcQYTVntpDN-dhgEjJPuNFPIOcwurgyZYnE-Si0f7Zo4p-X9ySfk82luuDW25l3zipcjBB3l7L-N30bb4Da1_AL56JrHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Kendrick Lamar
📌
GNX
📌
Mr.Morale & The Big Steppers
📌
Black Panther The Album Music From And Inspired By
📌
Damn. Collectors Edition
📌
Damn
.
📌
Untitled Unmastered
📌
To Pimp A Butterfly
📌
Good Kid m.A.A.d City (Deluxe
)
📌
Good Kid m.A.A.d City
📌
Section.80
📌
Overly Dedicated
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/77736" target="_blank">📅 21:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmJzRB0vmZ6cC5Dm-8hDuAzzssiGWgvyvQe8FjMlwbyS4zAvbifhs-T1_1GSDCG_pEhtedV767k6QUnM_YF7B2ffRpe1Bw7o_l4E_MZT_mgVli1w7DlqF3IUHNu-983HKDf0A3X7JRHpkyjoRLOKanWjeHi80ufK_FAV39URUS7t4tTCx2TEzpw715-jXZUOq7l-4ZVc1cTvJfc9bd-PVRBpFqp-1Ts3evns7V4IVY97nw2PG4DZjhKWiIQI4Y5dENod3Gd8b5XiSIivA3hRQsEhR-9oYTZqCYsuiFd4uVUTpK47YbdZja6vtBdfFrIuRpVDJOy9a8JrXy1Z75bgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیدم مردم افغانستان میخوان قیام کنن، میرم اونجا هم یه سر برینم امیدوارم اشتباه شده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/funhiphop/77735" target="_blank">📅 20:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77734">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مردم افغانستان برای امشب علیه طالبان فراخوان دادن و قراره به خیابون بیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/funhiphop/77734" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید
میخوام فلش بک بزنم به حدود ۲ ماه پیش
عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد
نتیجه توئیت عراقچی چیشد؟
رفتار خودسرانه یکی از باند های قدرتمند سپاه و بسته موندن تنگه هرمز، ایجاد جنگ داخلی، حمله خبرگزاری فارس و تسنیم به عباس عراقچی و …
الان هم به احتمال خیلی زیاد توافقی که ترامپ ازش صحبت میکنه با باند قالیباف و عراقچی بدست اومده و این میتونه تنش رو در بین مقامات باقیمانده به حداکثر برسونه
باید کمی صبر کنیم که ببینیم واکنش باند مخالف توافق به این توئیت چیه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/77733" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77732">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">میشه بگید ژنرال یه عکس دیگه بزاره؟ من نتونستم ساعتشو ببینم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/77732" target="_blank">📅 19:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV7V1fLCxGofK2XwGYvHhDlTVpnWM5_MS7pnodaWEVJNeKBEZT7bRmPQC5_fNgE_3Rr5QZZeezTrzJW4IIMP46CwFcrYhqxuHst5erJ6qVQ43a6hmoOHmE1xM7pnRUZ6aWxaxJB_WU2zC3elHc6MiQ8cIkiWAvwHfjublQFHwVBzRAccu745-WVpWKJNEMMUDZdNYC9oDAe2mqIstfrw1xDJSxTG-y_sGaYN3TSk2hxpp3ApH-ha-OCbhOpmpPYmhQGqj6AAOut1evJjHvQmfaW73hUzojhf8hIkw8U-1Ux-8FKFQTWBkQ7ldneb2Wvx4-iyiumiYYBwJ7Xd_hSuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالگخیز توییت عباسو ریتوییت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/funhiphop/77730" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rre38sxhiIz5zJSfFrDhDIpgDD28skit617sBn92t2dLFOOu_z4Fadk0u--_5HBDqakCaJ7rbTr-5EkxhsslykpztFeuPTBwKZ9hz2-BUPI-ECqRu6QFLyOG6SPB47jchT6997g9jf264xtFxmiIPMhdkWcfO4pxaDPahD5rvGVLQGJtIKuBu_h-UKnS0rb9ZS9ffNzCk1vDya-6Z_w9SledS9DkDANWId-Dr0Y_n0NG2TiTnprfisLDwoJeS7JAwQMa4v8L6ooQJKDqhPR3y9XpodsGIdkcEubqRETckqk_2zZwsXBUfpLgZtR6HY4fmD7NA85_UGWbWwILzQQgIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سری آخری که عراقچی گفت به توافق خیلی نزدیکیم هفته بعدش آمریکا و اسرائیل حمله کردن پس تا یک هفته دیگه جنگ میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/77729" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عراقچی:
توافق با آمریکا هیچوقت انقد نزدیک نبوده و مذاکرات به جدی ترین حدش رسیده، بزودی جزئیات رو با مردم به اشتراک میذاریم.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/77727" target="_blank">📅 18:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شاهکار ترین عکس روز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/funhiphop/77726" target="_blank">📅 18:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdUkp_l9a9Raz8oZPNIOrykRfBfn47OLwMxDuk7fsgm5G7TMWU-uyaxFrtBpes5lOEksBWm2LmTEp4bz1b3QdYbQrjMYJFz6EfJHuU3TK2KWY2GHxb9vtHQlqDEb9ZNaGzYRWo4VkvH3zcc4t4dZtgM0-aD9am8-jSe2K3kDLgYq9LnXnzrNAuS7gz52W13XF_fVI7JKXJ7myU0L-jQrFrkdmsmdu3SPjMt3mxt6k196FqFEOlVguHiBOYGwuELiq04L7feSHUQ_BJovJFYkyAGvAFkjxrvDg6EcuECwL406R1mseHp4LdfcpviB5HJGc-etEFmdpzX0s144DmSeag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار ترین عکس روز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/funhiphop/77725" target="_blank">📅 18:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvK89XsK5jtltgdFkYV14LqEKa8yGt_MgNrUrcR37ZDwZrkXeelf9n_Eer1-5Qc0zfhUTzlSH0y-TjpQ5n1jzeIerhrREVQEBqYEMiEj5deYGuSxlIjDLS2qpk6O_RVaboG6FnCEb7KnHXbRjV7_zvNwwbTSW2Efv_rk118Gojyy_Mct-UlAMBGuRgBoITzi4Uc47AJTjsZJXF8eNX4Q6tUAPcOVB_yoGriDFcj_Ud5Ycap2dRl_6IJAYb2FU9wznd_-ZuLQTcyNtL9bVJXe9WOkfmeD2mOOlnT3cXqlFipEDa73Vhu3YPR3SFBv3u3WBo7kJa0E89JzBYMPyEJ6Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کره جنوبی هم خوبه ها، حالا در حد تیم ژنرال نه ولی خوبه
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/77724" target="_blank">📅 17:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX_x0pAOBG1yeu8m85ZVLpWxyDdsgb-AVSW0smeCyzF19YKT8lY1sdjY94yn6aO3Y7RImYpBCzO6-PsHoibbssl993kjqYchEpJVI1KbWjYo2KX9kvszgYOrGGgf6cki-oicQpSXhnss_VX4wd7e-WQfV279vAqQ1ZYAkDKqgw7yB9rcsE7wHRr8lgJejMyOn1Hm9aUp87DiFQ91o1fImCeHvjqHR20uk8PP_JSC1T6rHsJQkt5ffwTVHfz9NOvXND4wNUu08OhtVcVC4SKvygg4W8WlCQaI4ftoVfJr3_nYKqNbZoumDsGGif3tdveHPD0h1P_5b_73jdmnxhibPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو روزی که همه ویژه برنامه جام‌جهانی رو با رامبد و دیبالا و... شروع کردن ابوطالب رفته «علی پروین، مادرقحبهههه برو دیگه» رو دعوت کرده باهاش برنامه ساخته.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/77723" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/funhiphop/77722" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f19qpbyjZ3JHGyJVstNxuyjz0MJ4jobV0K4OLXgFjG-Wg9AK8pw_9iesxHlSjr_-VAJ0vdSjTrOyFahjnGuVQTC4EgLpoA-_u6JBwiEWN98Atmp8geBjkwh8G0PV07LWMbpViyGV6IYWcqf59frBEtePxvdAODQFm0A-wiX61XVjDClKsy4PoJEuXTpQaanUrMKMqalDOjASBWHTfFVf9SgO8la9BmGQm3BRgm9nnxYE6wqfU2HTmAFcT_FgdyLbV-Wm_VrmIsrxJZy1AwEUUEft1aWbJ1HcLkFIYAxXis1XI1WTluKOHAroyQ5FOf1EXBRKgN_s7lL6Zvwj6tJ82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g22
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/77721" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رویترز دیروز: لشکر 82 هوابرد آمریکا خارک را تصرف خواهد کرد.
رویترز امروز: جی‌دی ونس و مم‌باقر قالیباف توافق امضا میکنند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/77720" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فاکس نیوز درمورد مفاد توافق احتمالی:
مواد هسته‌ای ایران نابود و خارج خواهد شد، برنامه هسته‌ای آن متلاشی می‌شود و هیچ پولی آزاد نخواهد شد تا زمانی که تعهدات خود را انجام دهد.
یک مقام کاخ سفید گفت که تنگه هرمز به طور کامل باز خواهد شد و ایران موافقت خواهد کرد که از حمایت «گروه‌های تروریستی» دست بردارد. (دقیقا کی موافقت خواهد کرد آخه حرامز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/77719" target="_blank">📅 17:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=XWacPQYgIJBBwGem_7XIWsaVyxBJwVmSZIClwSbViI6F3AC_DhTojFwTHxdA_R-J098zwhxzt6ymuiyfESX0qYPpqn2kuVh7tsZx45je_dmWm2CZp3aNe3mHOA-Wx0mbs_HndA0epk7ITdVpsotoJV6O1oF4KDLazQ7YEuhWu1fBLizdwKsdRV0fgXmfiPDrutLkCqaSHrlUL0t44gMUF1tOXLOXo3o3tvd-N3QJsLwgnXdPnPr8kY6tt50iMX217km6x0SWRKv2hgMbJmf5FzhH-rZB8NuHj34lGHFnWdnCaGKSaODxSiNF2vj23QEpxTLM1EsA7e-J0RNhFsfH0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=XWacPQYgIJBBwGem_7XIWsaVyxBJwVmSZIClwSbViI6F3AC_DhTojFwTHxdA_R-J098zwhxzt6ymuiyfESX0qYPpqn2kuVh7tsZx45je_dmWm2CZp3aNe3mHOA-Wx0mbs_HndA0epk7ITdVpsotoJV6O1oF4KDLazQ7YEuhWu1fBLizdwKsdRV0fgXmfiPDrutLkCqaSHrlUL0t44gMUF1tOXLOXo3o3tvd-N3QJsLwgnXdPnPr8kY6tt50iMX217km6x0SWRKv2hgMbJmf5FzhH-rZB8NuHj34lGHFnWdnCaGKSaODxSiNF2vj23QEpxTLM1EsA7e-J0RNhFsfH0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/77718" target="_blank">📅 17:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ یهو ریج بیت مودش فعال شد گرفت رو مذاکرات و رسانه‌های ایرانی:
شرایطی که ایران به اخبار جعلی فاش کرده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده بود ندارد.
آنچه گفتند، از جمله بیانیه ضعیف و ناامیدکننده‌شان درباره داشتن یک توافق، هیچ ربطی به حقیقت ندارد.
افرادی بسیار بی‌شرف برای معامله کردن.
با آنها، چیزی به نام معامله با حسن نیت وجود ندارد.
شگفت‌انگیز! همچنین، حمله پهپادی کاملاً دفع شده آنها دیشب علیه کشتی‌های هندی که از تنگه هرمز خارج می‌شدند، کاملاً غیرقابل قبول است.
بهتر است هر چه سریع‌تر خودشان را جمع و جور کنند!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77717" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeDRJIGSC4Vf8jMD2v2MpydKvGZAc2H9T9oAQS51xnEmQpLPJKTpVbiWnSW7r6MUB5tExajKJVQCkXIku6v49zTiMPZz8brRZBCOuK4u0J65qZUIbSBEZMNG4miMpd_hJZ84vypva3xEdxqAoXwFQQwF2zCAvvgz7CacMewmBHq7n7r2tTmmKfDF0aOB9qvKvPh-MeMyS5y7X9T9HpVlfCfMqB3Tzhu_uMuWjaiwybdKzMClYdzY5ChgJ7cWA1hd-y5Q_5a7bvFZVJHqwWhaOqdyvq2k3cuIvAZU0_cxmYv4lh2U-X5r6-NgUPk_swtpNn7zJbNnpsmAB1vbo0-vyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ارباب سعی میکنیم درست بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77716" target="_blank">📅 16:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77714" target="_blank">📅 16:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">من تازه فهمیدم چرا علیرضا منصوریان کچل بود، خواهراش کنده بودنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77713" target="_blank">📅 15:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrD1mehQK486aw7woypXQWNoo1q6XNm7oXicsstdu0WTud0BGve033zjA15W-GFZwDhH7nENx9y3sS9k9kCvP600pBDHpYjkrotUuWbXTe5eHOKtkbaCkTE1IThwhk_I8ivtagqnIw1tkwIvWW8cv0sAQeAQdghsGupU05OaHGHTDqmz_WA7r62uYj_Pyp5LzVjxzHALyPgTgRCPwo6GwFS4il9XHDeWwv75OCsGc77S3ABS32SHv_tbcZFHjt8zY2xEtNnKmT8xFVSd_4OVZ03-upChKzTZXJ6uoV6TkFNqyiVPARkeoi0vAjJqTuk9daMp3ryf7TnO8gKfeGSGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77712" target="_blank">📅 15:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=tQUDXRVGQivrfeR-ywMullHUJimyb1z7Kh1yeXLy0NLXaSYvRqqkR98m8dLLQgd67oKGK_7KTimsjTWMXglJqL7gm7NEcrOIocQqTJP_8GKAJuVaiEfc1GXOBpLcmajmm2VTzOO-maF096M47Uuds78W0vWFx45cBZxvKMp318B4enBlDMTEOQ4SRbCbi5uLxQ6_h_S00qeGaykQ5O98klGyEqqy4GgbaDcWckBAMxGTU_mHrxZxL2sOB6mHFXPsko9y73Xnv2sSvPZtt0SQL42HU8anyouOzIrJoqoopuMtZkspY7HopIGSwC23LCcjj5R4jFWEFDgVCWsuEwcAWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=tQUDXRVGQivrfeR-ywMullHUJimyb1z7Kh1yeXLy0NLXaSYvRqqkR98m8dLLQgd67oKGK_7KTimsjTWMXglJqL7gm7NEcrOIocQqTJP_8GKAJuVaiEfc1GXOBpLcmajmm2VTzOO-maF096M47Uuds78W0vWFx45cBZxvKMp318B4enBlDMTEOQ4SRbCbi5uLxQ6_h_S00qeGaykQ5O98klGyEqqy4GgbaDcWckBAMxGTU_mHrxZxL2sOB6mHFXPsko9y73Xnv2sSvPZtt0SQL42HU8anyouOzIrJoqoopuMtZkspY7HopIGSwC23LCcjj5R4jFWEFDgVCWsuEwcAWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توهین بسیار زشت صهیونیست‌ها به رهبر معظم انقلاب.
🔹
صهیونیست‌های ساکن سرزمین‌های اشغالی که فهمیده‌اند کار جز کودک‌کشی بلد نیستند، اینبار در اقدامی توهین‌آمیز یک مقوا با سیمای زیبای آیت الله سید مجتبی خامنه‌ای به همراه رنگ‌های مختلف را در رژه روز همجنس‌گرایان نمایش دادند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77711" target="_blank">📅 15:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEf_R2xfFXHH4qgITV7WSigJqlD9ot3FTGZIDqm9tOqa8vwDWqkm8PVjnIxBbiEsFgAaGK1w8AHvDD7GEwCiyeWSy7cjBfKZE1Ka_SRP9lWTHLXHAWcRd_nKKPlLNUPhfOzmPSj57uuJ4MBxwahF-RhajSWdJMvOhoE8rrDnOtCBas-Wu0b2gQG-puYCioPqW6ldGgVyQzlxXIQUR5WhvCFthQ4B-SaRWJbsYtmvWoKkxgRVs_C5g0pfgRol7GoaaeyJ52cp84E9gLtIUiq3DLm-zDUz349kJgkVCErpZRomgYZvSWUXoOROZhohUM33mQDN9LiE0FCzJIAnnwCzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#رشید_مظاهری
را فراموش نکنیم
رشید مظاهری دروازه‌بان سابق استقلال و تیم ملی پس از حمایت از مردم بازداشت شده و ازش هنوز هم خبری نیست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77709" target="_blank">📅 14:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77708">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBW9ijgjTUicSpMQEw95ynPPTJXC8g0cp3cUIjxEAFlPzdfrRSOqkkexjCjEAnLcDjQhNshIk7NO9vkLHywwZrD_ng0oiy2ytfQOHc4ZJFh_cSUfL2iT_SkF-Eui5w7Y1ZgNu3veVYx03OaKTSALw9x2U7j1aC0twscPsND1MdZeBdsX54ovfForvpZwMxBgqkhRjCjqpX1-ZZAKAVukJId7w0oPz_0hHtPA4ZWjad13Veyn_fDfgP6DiKEF5K0Yo9XIcMPkjAowUQf3a_ifhHyG-i0WkC3KiO7wG4xt73CVbZofR7xt3UYab0lwgeP_ikpIt9gUxm-J4oNg3RWlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیر دیگه کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77708" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojCVAsb8VY-J8aIwG_cqOF_DjZ4zYYyjcytDc6xB9q3ryCZ6cD3BH4PyExqJqkqscZUNDXCPz02YDyK8ppQnjx9w9vSlxoM6Jr76mgSV0zXVXsqGN6VbhHzErjCzxPwmM-wtZXz6OuV43E9Ywx9HCGPw01afTlnXvypk8TeBtQ33BFJ_QQ9wgkL8fQXLlqJA-yF2vQuChLuvtYiQhXpOIsXpgUAdeCL94fzHfIUcHhUbp1xS43mEJzwLp_XzRUFKCoHv26uW8JqXnijAW0Cpdhug6X38p5zZ1y3w1vbPlrsJ2ZEzC0uR0LLXF--oA2YBuIvfwQlrvkymXgexdWJ0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیسو
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77707" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد: ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77699" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد:
ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی که منجر به لغو حملات آمریکا به ایران شد.
تنگه هرمز پس از امضا به طور کامل بدون محدودیت یا عوارض باز خواهد شد.
هر دو طرف متعهد می‌شوند که در این ۶۰ روز علیه یکدیگر یا هر کشور منطقه‌ای دیگر اقدام نظامی نکنند.
این پیشرفت در مذاکرات پس از تمایل آمریکا به آزادسازی ۱۲ تا ۱۵ میلیارد دلار تحت نظارت قطر
برای خرید وسایل بشردوستانه
ناشی شده است.
یک مقام ارشد آمریکایی گفت هدف استراتژیک تغییر رژیم «فعلاً» کنار گذاشته نشده است.
انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.
بند آتش‌بس لبنان همچنان باز است: آمریکا مایل است به اسرائیل اجازه دهد به تهدیدات نوظهور پاسخ دهد، در حالی که ایران خواستار آتش‌بس کامل است.
مذاکرات آینده ظرف دو هفته (مطالبه آمریکا) یا ۶۰ روز (مطالبه ایران) به محدودیت‌های موشکی، حمایت ایران از نیابتی‌ها، خروج آمریکا از خلیج و تضمین‌های بین‌المللی خواهد پرداخت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77698" target="_blank">📅 13:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77697">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فوری
پیت هگست 44 تا پرس سینه رفت و ویدیو شو منتشر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77697" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اسرائیل بمباران جنوب لبنانو از سر گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77696" target="_blank">📅 12:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYNr52KS1rjtk6mc6sfJgQF-XH-tO0KOYNKve0D3YQ3iNVkepVJPoWbiLMm2DusBpU8Rl4w2MAIvAPXyBxVpLVzFoezQ_iU4YSKbNGwvU6EPWEA81DgKWXhwFs082oPhr_DK4Ss4ziDJUIYbzcXaC0ASHUPyngax7EqQYIeSmIm2pfuCZcZ-JdJZPXhdPKQut_3x2KX_7uGbUIcpXGaAW5j_hFYrroNXQaYGfXNvdRLwdQu3HWo3VhDFoQBpOK7N2qznAkADrdPA56TeUJlncE4AwxWTPrTaUVw3crrtwQYKuhFz7sZxhL5qZyAl330pH-YbZIXgEP78UJ9_PCYj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش اسلامی سال 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77695" target="_blank">📅 12:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77694" target="_blank">📅 12:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzjrJM7kIDdZkEcv_jEo6S1NUSdR9AgcBWXzpI345tJ-X22xCikCLv2vBi9dnlQ3vLhUSY2UCIqsl64obL48zMooO6x-XmsP_SdEtyoS1TBXx-5uOUYU9vffJCnNXoqMniNA9yzVWpOdbWibPvwpyHWnSffUEAy8gCzofNextaDXdpYxfqSvBEN6owCND2bYvA5luZMfptmraNviDgLJg1E_k305tUit7NrP1Xt2Q77qWBg2IAShHc66IuLm5bLjD6Lr4HnutSu5QkQRB3vBM6mi4glYNwxfNeJ8h3re33UMftFGkIyXiXjBiFbzdlJUGITsVoApnRVf64apT3R1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77693" target="_blank">📅 12:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfHchuibUaMoYi_WjebWBItH1G9qFXty2OVsnIy3mF4pmEOTLX48818_4PDFNw4v7wjPM8AGq7mclviRILVpMS7JfJc0g5Y5fO5wMHwoGSRI5owWuvMex6bB8ZPJXSwaC_BgG8JwDPlIvltXyRxXigjq2upgCALSq_DAdTUDvvQUmjLXHN5B8WED73dj5FckgJCbbEJsO74wYZF00eCr3aMtXlJBf0X-vJG8BF-ki20a2JB9GK8TD4rA0x9cyaaf9R7ahl6g9x0-YBG8iw89BWhZncSEh1Trj1OaMVzkkcQuryQB--wQAfyRppNC7A2om-8-PaQLXm0Po2kI-AeWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهران منصوریان ساعت 11:08 صبح رو بهت بخیر میگن.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77691" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI37lA54W2--nKfOSwV1bIZAv3yF5xluy4UCjeG2uRAygc2-euDxGoJLxsqISS2TBj_ME8XzqHAXEs0fyGSohIr6xiiO9sOuFJ2RLPH3THa6evtb1VC90yMowh3tPCuTtv0tRrVlVxan0bsbszZ45JtdKxA0TIzg1_8qaL28F39wbjcsTDjAfah6K9aLGhw3PPHlETP1bghYn7P76B-5HE73UkD3sG68_elgNLZFIf5gp-sTB5--lQ_lSIH1vTwpcVqc0RZXauO5T_ty10uUZA8QF5OhrmosR4zRZS_fgDRzdVIvF5aJF4qLF3furch63bUQV6WGGTXDqPUkZ1ODIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاحیه جام‌جهانی
❌
فیلم سوپر BBC
✅
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77690" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77689" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77689" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxbhcZzaHw6tzTkspw6yoMw9RTya--yqUcdgXlcIMTg8BaNUfCOEBeGuJy7a2ilQgS96kkNEjKo_JniqXp1BUeP_nKHGMycRSDg7I2lrNCFjToVdnzScRM0Wd2Quy6MgsiRYjZY9gV5ouRJ8nvUXFMzH_K7G7o1rdbPUnhCLbrQBfmDAelyu3WWnXPPX9GJHahOEo9eabnXh7UHvRDHbrXaVq3hr-0rKP3VSKkadoDfARU8Dr8RsfMy5VQ-W5xQOeF9gbdRg-ZghcvXXhYrFOniArEVYHANHtSP4ANaccpggeTyMxt2VekMXsEXq73G9-sQfbLiVabUvdjiwwMOShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r22
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77688" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77687">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شاهکار جدید جواد خیابانی:
خلیج فارس خاک ماست
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77687" target="_blank">📅 10:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcee0eb614.mp4?token=R1OguoUZM3bZCHf317jZdiaXvsO1oTDxcXSzslUcl5e8yl_xdi8daMcnDnZJDu3qKy74h_b3xsi6cmUO_kgypPmGrQQV9Qv8d94MvzmHcAld6tpqMoT6HHBpCTlnAxJfodXBSExB8mfBkYUSJpt4SCJxxav2vVBkyFsZO-ZsDoGvCpSDZ0-cOAfT7pVPt8tVFy-d-kFEpXACQxKunEj63qUtoQGKWErkB-tcd5D6KsjP0RMZLVAyy61ZsJVJusfBadhPXKFL24RAhPx1_ccbZCe4LtVNW2CwWGJSILBhhJYGUKWDg4KJhp15FWlRD54maOC6OAuxChMpuq9wGuGFbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcee0eb614.mp4?token=R1OguoUZM3bZCHf317jZdiaXvsO1oTDxcXSzslUcl5e8yl_xdi8daMcnDnZJDu3qKy74h_b3xsi6cmUO_kgypPmGrQQV9Qv8d94MvzmHcAld6tpqMoT6HHBpCTlnAxJfodXBSExB8mfBkYUSJpt4SCJxxav2vVBkyFsZO-ZsDoGvCpSDZ0-cOAfT7pVPt8tVFy-d-kFEpXACQxKunEj63qUtoQGKWErkB-tcd5D6KsjP0RMZLVAyy61ZsJVJusfBadhPXKFL24RAhPx1_ccbZCe4LtVNW2CwWGJSILBhhJYGUKWDg4KJhp15FWlRD54maOC6OAuxChMpuq9wGuGFbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بنده خدایی هم به توافق اوباما که بدون ریختن یک کیلو بمب، حدود ۱۰ هزار کیلوگرم اورانیوم رو از بین برد می‌گه شکست مفتضحانه ولی خیلی جدی معتقده ریختن چند هزار تن بمب و بگا دادن کل اقتصاد جهانی یه پیروزی تمام عیار بود چون بعدش ایران قبول کرده بهش قول بده که…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77686" target="_blank">📅 09:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77685">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b774ac8b5.mp4?token=f6AnBKxX-j8AB7EDZojnQVYFvqHzJPEVffj19FoLfUbuDHnfST5Js2oytksWkO1uMDdHjswOUeLVHa_9QQjEyaFqDNM8hLeWICb76IDGxufQ5lx8e4ic-nCpXHg8KuxXzWrp5RdP04Alp8Feq4Ml1oDEx_93q_E6Vm_8ZuLuWEBDsmNo4jRzSEQ7oPO4s0mamy8W6WMudzmacNrWIqmylbOg6-sBHdjol1uRXNnULPherdy0yM6lwjGx9KWcDzc2WiHhzMgHLPdM7J0YvRaH79C9CizTgbY4UM-M70KrWJRIQ7a3HJwsKzOjr5bMJbUluYJCO6f639t1UD94t55TZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b774ac8b5.mp4?token=f6AnBKxX-j8AB7EDZojnQVYFvqHzJPEVffj19FoLfUbuDHnfST5Js2oytksWkO1uMDdHjswOUeLVHa_9QQjEyaFqDNM8hLeWICb76IDGxufQ5lx8e4ic-nCpXHg8KuxXzWrp5RdP04Alp8Feq4Ml1oDEx_93q_E6Vm_8ZuLuWEBDsmNo4jRzSEQ7oPO4s0mamy8W6WMudzmacNrWIqmylbOg6-sBHdjol1uRXNnULPherdy0yM6lwjGx9KWcDzc2WiHhzMgHLPdM7J0YvRaH79C9CizTgbY4UM-M70KrWJRIQ7a3HJwsKzOjr5bMJbUluYJCO6f639t1UD94t55TZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بنده خدایی هم به توافق اوباما که بدون ریختن یک کیلو بمب، حدود ۱۰ هزار کیلوگرم اورانیوم رو از بین برد می‌گه شکست مفتضحانه ولی خیلی جدی معتقده ریختن چند هزار تن بمب و بگا دادن کل اقتصاد جهانی یه پیروزی تمام عیار بود چون بعدش ایران قبول کرده بهش قول بده که سلاح هسته‌ای نداشته باشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77685" target="_blank">📅 07:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77684">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrPU9VyT0U7GI94a7685QUHNF3n18UJIIJNL5zheb3jw3HYADZI6EWiNpGfTRzRB5jar6-86ozA2RmH1ZEYPhY1hQ8FL5WG33HZ0Jfmjf26YBnPD-fyFjGzLJWYFKRNb7y-pyT5MeTOjeQfWi8y8IQmpaMuOJIWkh2BCUwaGuKI-JAdXuyPDf8-A7o69FEIcGQw6ooE1E6Mtez5q3vw7lczSp-xENdJXJOXzQgfI7sqorjQmhkmy-H4NClThfVkipO8UVmoeRazn4bAKhmrI51GiW31MH_MAffs3MyydZt-EyRmHpi7GNw2UT0oJXtCCJp_Vf8itIBWe6I7RUSA4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمنا می‌کنم هر کجای این کشور نابغه پرور که هستید همین الان متوقف شید و سعی کنید یه مدت تحلیل و تفکر و کلا اینجور چیزا رو بذارید کنار ممنون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77684" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77683">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه کودن زاده‌ای هم نیم ساعت پیش اینارو گفته بود ولی از شدت کصشعر دلم نیومده بود بذارم:
ما امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود.
این ۹۵٪ از هدف ما بود. و، آنها این کار را به قدرتمندترین شکل ممکن انجام داده‌اند.
ما، آه، با ایران توافق کردیم.
معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
اه، نیروهای ما خیلی زود شروع به بازگشت خواهند کرد.
تقریباً، اه، تقریباً کامل شده است.
ما هر چیزی که می‌خواستیم را گرفتیم. نکته بزرگ این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت.
آنها بندی داشتند که توسعه نخواهند داد. من گفتم، «خرید چطور؟» آنها گفتند، «خب، ما آن را پوشش ندادیم.» پس دو روز بعد آنها با آن هم موافقت کردند.
ما هر چیزی که می‌خواستیم را گرفتیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77683" target="_blank">📅 03:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77682">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عرازشه ای که میگید آمریکا نباید فوتبال و سیاست رو باهم قاطی کنه پس میشه بگید دقیقا سردار آزمون چرا دعوت نشد؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77682" target="_blank">📅 02:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77681">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_SaVhXItKOTngu34dMHZC7GYu2TpEaM0E8AwWqtTZF7mFf-nfuHZHru86CLGL2qFh8gVroTKnk464WtzsRnYh4vPQDbvstzNKc983VrHd0KuWvdXw7CzSNh-6w2CIu2BQJ8kzeleCdI2U2fLasQSNwqv1zNcXT1CnVVvcuN_FkXuEcPeUnep1dMpdz9jDP5UqLa7p4AdarYAtKXYOsid7PDwWq_tKaL8rQ4BgB1fKBR_-m3kZK1oi11VnRTw4GHUZSbGEIzfd9lXlXnJolOK73tt-cWUAHvPwL2uRrTdF2xzNFj6eAR0NQhIuWrZ8lIZAzdp6-0G3BKva4Z-2pmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست ترور بیکینی باتم اومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/77681" target="_blank">📅 01:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">میناب انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77680" target="_blank">📅 01:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77679">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تسنیم: متن تفاهم تا این لحظه در مراجع ذی‌صلاح  ایران به تایید نهایی نرسیده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77679" target="_blank">📅 01:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چه علاقه‌ای به گوز داری مشتی</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77678" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بازم گوز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77677" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77676" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnuXSzLKm9zNmllH1UcSTu9fdSqmUUJJj_Csm0m9Rv8ql84hKw3O3Uauj9l4MiUbsZ8A96D3d6nZalRm00sOJGXmV4dp87BZVFqJjp-_GLE0sbKAfFD3RBZObhRjUaVCMe2C324qWL6vpVuKRcsJ2-8QVpnNsn_Px_fGJVkN1pTZj2ey6lhm1AJxbDomtGCAvX2KsVS__UpGDZsUZa61Xx8Kk7xxPw12zYZIem4iPeURxy-tBZmV06kbMFToRUnjCzctiUtQY1u56K1PqlZm2YkYK3HwxzTydWIf7tUke8CGRecztqPV9IZJpuYbHW1ohCkSiLa2zNjsYfZpVZkNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه اواکس هم داره فعالیت میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77675" target="_blank">📅 01:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پرواز سنگین جنگنده های آمریکایی برفراز عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77674" target="_blank">📅 00:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گناوه صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77673" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">درگیری ارتش امریکا و سپاه در خلیج فارس
تایید نشده هنوز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77672" target="_blank">📅 00:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سلام فریب جان هم اکنون صدای توافق از خونه همسایه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77671" target="_blank">📅 00:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77670" target="_blank">📅 00:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77669">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77669" target="_blank">📅 00:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77668">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خبرنگار: آیا رژیم ایران عوض شده؟
دالگخیز: بله، نه یک بار بلکه دو بار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77668" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77667">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">3 تا توافق رسان KC-135R هم از اروپا دارن میان خاورمیانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77667" target="_blank">📅 00:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77666">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسانه های مختلف خبر توافقو میدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77666" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77665">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77665" target="_blank">📅 00:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77663" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
فقط برای مدت محدود
💢
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۴ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
---
📦
20 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۴۹ تومن
📦
30 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۷۲ تومن
📦
50 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۹۹ تومن
📦
100 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۱۶۹ تومن
📦
150 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۳۹ تومن
📦
200 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۹۹ تومن
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77662" target="_blank">📅 23:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP4I7DavyKfxhT6kn7or4PzSzDiuaYiLg--EzIc-K318Y3-_nXSf2mPMlvv_yrfcRITSUOeD2hUZemp3kVfckMjlE2osUm48wf1cYturKFS7UsCOm8s4T_aQZixNL25-Oo7si5HGaIWc0CgjJRkFmDxek7gTfFrxLAaBCuWu94jghBXGUU6JnUk32PUkHOa2WN2Nu5TwGfAwnaefUGK3b_b1XIxGf2iWgXW3h2Ky4GP1lx0sUWSYsg2GRDtkYkaj7vBR0Kvx6MckWy0FxvM0Dbn9qL43Q89M8FCdf4gGkqHsJWRaE611LsHJm8N3zo69J15ZMEUcjnyYdru2eBPhCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77661" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77660" target="_blank">📅 23:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromcина</strong></div>
<div class="tg-text">این برای امشبه؟؟؟؟؟</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77659" target="_blank">📅 22:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=CtXO2kabSG1yc0IA388eUciKbEg0WFX-0mi5wF9waqzQE7yoD9Dl8EcN9SPiJZ3Zqg-TS_vJqLOHIxfB48W7FBiKt_LOzNErYMtzVuz1A6gJi-0VtyaioH0wwx90c9BF6eCO9MZMHF69Siw0GQJtKdU6lIEksAJJwmJO9TzFXrQbsymjd6p2pm-hQgPfhYcr57wBg5R8smeiXhlblVyr9P5-jY_Sxi3hSBUV87Ax7sDHMF1g_-dOrBalJbBYLbdIs1qr7NGngpdEm4eLlpgqgJ0CXXdbCBSbBUZKY7zFqtsbeZr92qGrBFYQwJAsizLQnZjp-sFoq-u3j1IMWKCr9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=CtXO2kabSG1yc0IA388eUciKbEg0WFX-0mi5wF9waqzQE7yoD9Dl8EcN9SPiJZ3Zqg-TS_vJqLOHIxfB48W7FBiKt_LOzNErYMtzVuz1A6gJi-0VtyaioH0wwx90c9BF6eCO9MZMHF69Siw0GQJtKdU6lIEksAJJwmJO9TzFXrQbsymjd6p2pm-hQgPfhYcr57wBg5R8smeiXhlblVyr9P5-jY_Sxi3hSBUV87Ax7sDHMF1g_-dOrBalJbBYLbdIs1qr7NGngpdEm4eLlpgqgJ0CXXdbCBSbBUZKY7zFqtsbeZr92qGrBFYQwJAsizLQnZjp-sFoq-u3j1IMWKCr9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته  باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77658" target="_blank">📅 22:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته
باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77657" target="_blank">📅 22:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">توووی دروازه
مکزیک گل زد
اولین گل جام جهانی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77656" target="_blank">📅 22:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77655">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جام جهانی شروع شدددددد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77655" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp8WkPVeuLdNfsAmtvn0h4BJfO0WfwhTBGPHTm3RCFdWdVjFPrMCh49Rk1DuMOwIlhcJtURZovJHuxOblQNIT8tcYP3ph-hSfJIiHfL2yjeXqYI_I6UQD0iYgYx2BSS-zwhh_Bmp5y6nBKII_cvvpvOHzcMMMCGNgdsj8z5Obyc20DmnrgB9BEfMTvHE3WgiM-MnKETUhzcmyiw_9T6KJlIJJ88cF2mhG5uARI4JOfqw7VF7G5Dbkj2QcxSoeAJyNc3YcjOIAhJeBjXDgumCS3P0p-oPTVStoVZpdJg5j6aDqHfCIY1hE1252tomC65Kaqhi9CK822wxqi_aa7CxJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس هنوز نمی‌دونه توافق نهایی شده:
من از نمایندگانی بودم که خلیج خارگ و نیروهای پشتیبان آن را از نزدیک دیده‌ام؛ پای ناپاک شما به آنجا نخواهد رسید و اگر بیایید، زنده باز نخواهید گشت.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77654" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77653" target="_blank">📅 22:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دالگخیز
🔙
عمو ترامپ  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77652" target="_blank">📅 21:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیویورک تایمز: امیدها برای یک پیشرفت دیپلماتیک پس از آنکه تیم ملی میانجی‌گری قطر روز چهارشنبه بدون پیشرفت در مذاکرات تهران را ترک کرد، کمرنگ شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77651" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77650">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ به نیویورک پست:
توافق مورد انتظار برای آغاز مذاکرات هسته‌ای با تهران «تقریباً کاملاً نهایی شده است.»
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77650" target="_blank">📅 21:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیبالا هم از خودشونه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77649" target="_blank">📅 21:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ریدم
عادل فردوسی دیبالا رو بعنوان مهمون اورده برنامش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77648" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77647" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77646" target="_blank">📅 21:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW6XeHocy1xB5txZGdHQ99PJm2QQo-gQGRqzMUSPnezm6hKtd2jNodiQxq3XBC74pt1uy3GGy06qVvphGQ919TfpiPE5KPav0smG-E_nAbZPLlCHTwJvybsE3RkvtKpC14wJTcJsMJlGFvPzXkau-tAKdmhEBfdaJo8pVKa2JKcbybWr8HZjIE8PA-mDcRZXRV7-3KBOImwzQZdkcjbvO5WpHqNPIYw4KMPgxSLV7gewT3Ak_XdXTED5the45hoTUXFLrLGGWTzajLcEHI2DMj4IDdouUUAD0oarD0A5upAIya1dLEmOlijqdJAs3xbTHgH0yj9ON4FKSWjehNnb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه:
بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران را امشب لغو کرده‌ام.
مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات کامل، توسط همه طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران تأیید شده است.
محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل ادامه خواهد داشت — زمان و مکان امضا به زودی اعلام خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77645" target="_blank">📅 21:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">07. Pashmam</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/funhiphop/77644" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">06. Adama</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/77643" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">05. Khatereh</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/funhiphop/77642" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77641">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">04. Setareh</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77641" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/77641" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77640">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">03. Tehran</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77640" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/77640" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77639">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">02. Beef</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77639" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/funhiphop/77639" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77638">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">01. Dor Dor</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/77638" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77637">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwh-uvSOR3F2oqxFeqPjqlVFbDh9XJd9SN1lKXUgVX3X07JgsKDRwHwboFGdsp2KhmxImX1zsFE9BAFQGrSYXmnM9Jijt1lZtfVF_BW8edDGc7JO_KMlSK6NagW63DDxR1Bj1vqhcS-QpVN61NJK_vyw1Oocvqnkr4-UO0HVHLfbybs9emjqfqp_MefeZmf-IxclTE1WYf4g1-IbBl-c7lN2GcxJ9Zuuw5vE8zVsyrZ4hRzcGV97COvHVItCZtFq7ygLOHWDbmISb0M9xM9h1Wrf_ldJas9chF7jRTHjNl64aj3Fl1oeKMhfAug7alwa0iMYHazvS3MLEr6vje80zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید مانیاک به نام تیریپ تو تهران منتشر شد
📺
YouTube
🪀
Spotify
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77637" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77636">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بالاخره بعد مددت ها یه ترک خوب از تیجی شنیدم، همونم خودش نداده لیک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/77636" target="_blank">📅 19:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77635">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxpODA31zUyCz8XLSdvekdqFppv7B6ew3cR6_nib9-5Uj4_D-2gkCtdgpsXhI7mE8KGCdvgdQlXP_VXxRCC_CnE2BQiT6j6Vlg47_xUItDD6nf6M5qyKxJZoAMCdZxAJGWb8JPzGlZIU-V87S53Z6QX2_B-nDP0Hje8v1Z1chlJyMd_FEfgGpED8aLJV_vIp39oaIdpacttaCijvwkK3mVX4WI2VF8i1yXy3mh-9MY2W_XAjZrzANsoAUGJQd-7EqYwW5-YQ_LFGxR3QkuPNc_543XZmEvqgsGcY3TLO29EfRjcsVCnkSQimYhwBxo0mV2QyCWyff2t0JUk3Euj3QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندساله که اسم توییتر عوض شده و شده X ولی گوشیه من هنوز توییتر نوشته، حس نوستالژیک و قشنگی داره‌
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77635" target="_blank">📅 18:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رامین بچه کونی:
برای اتفاقات روی سکوها آماده هستیم و نمیذاریم بازی با انگلیس تکرار شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77634" target="_blank">📅 18:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">با اکانت توییترم که کنار اسمم
🇮🇱
🎒
🇮🇷
🇺🇸
هست،
توییت زدم وطنم وتنم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77633" target="_blank">📅 18:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEJdpttMx_fJyGsYmaYrrEPyNze3kN5eWEg1NCabAcl7QsLoOf6eu8PU_AwV9iumb9x7DAuUdqEVkfZafKo0csU8Too0Udx-1s4G0nPKttxp5ntEch-AYhGyxnNkasInJlyiMn4IcuPR6Z6d21bVCJhTlftM_ljpBxBkd1e1VFRckXOxDAsLWq3Tg5RYesU8RpKs3K0Sw_T437XCPVvSTRiulb4yKCfi1XBLL_RUg-L_-vLOdgumIMwfKaSV-RvQoqO3Pjm19POgiL8A5C3prMEQ9ErAQ-5z3O_lAbwPH9nOCZwt3tmVL-IrKyn7Gson2t6brglDxvZBfHeAPx5_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جون عزیزتون این چطور پزشک شده</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77632" target="_blank">📅 18:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQHFg-RwGRE1eXS18mvQLIFWs3kuk_amaLEZVvpezOoVspQAWwH7O99JD8zB-b3HVmk0KehiHKCLi98xZ3dECcNQXCJ7VO5TDKVF7M9xPZRvmlkLRRwuyQp5EiGFT2eyuF-gYHCSaT5nKvaNbPTLbZaPmtB2V3qUQ1hL7H6UywQCELWd7aqPtSM3FUy6CAHrHALFQm1mOmBpuQAf5Z43sP1VxnGAkpPB2DOwRH64sWJPNq3IiehPbernC8gi4c_iXgxPlqlOT4GOfU193q5PnO9EtaFUFVIU504eKNkeNPA3_EqWrwlJANTXeWNBUvHRoYsSQXCMoIY8Cvlh2LID6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام اسراییل برای حملات امشب لیست ترور داده !!!!
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77631" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNo-jsNasXuE1ItV-Dm8KNWcz1GZJeflxspfALxo5ioQnW1-EK2BsiHa6BDhkGntbni4wJiEAJbwBfHnAIIZZWfAtHhIvKZMJV13Asd5RdyiNUVouzTBgyQfwdVjRg5S1l59xoZHa-1IuqUS2gaSyAWeOVVQzDeaueO978TFFGlSmdw-oBAdue1g8xeUqQzFC7wg52EKb_uFAHX15nRsf_VG-cF6pYfXMAZM_ZYw2KtPFCMJbTWwYoxHclVQhH2g4p2rb2rWbZcj6H0PKObkXYY5qZckCnkwMBnKP4cOBeEIf1vPUl2T_GrTIv_BIdPc8XWt6sm8fLS8Epo4_EnPew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد خیابانی : اسم اصلی من جمشید هستش نه جواد.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77630" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77629" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77628">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgjxBXS44onrDQtsyXcaPS30ozceW0MUa13ZLnvcY4t61WQK-feePzrw-xDbxFhZfIaqxx5USDMbu2uGf2MfEsqE8pGMrBxj54YHKfb1yL2LFwAOgXmyIXtNk2pijs2mlh8cl7z4pPpBq5zgAiPK2QlKGJrMQgdviVf9aONKfExAl2O2ay3LJtC-UTGPeA-VBYev0Vwq48eO8la_ujqRGAsfhe6a-62EnHsx-bAJI1qSvPzeYYP2BEMBE19h9cuCFQbVQd1E-FaNSQX0yjLbr2jOVJV-kamSzm9yqADi6br9tjm1QduLLhWnxTf0NyPGDhppmB-gCazSHcqXerZ46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g21
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77628" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77626">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/683daff4c0.mp4?token=nwV2xlXNkPqQ9bJVK2sDyzBFT5jLjfoP3eAcXxBKpvuGEdwtgZStqPeGFlii_t3MfAvDlQiYjjiO5DbyAA9MSQdti4RyGxmDfX0tX-fb7nZII6Lu9c-UK-bdZQ0Vztlre8yrCu8A06BsSYMMEKFFx7vvkannlkmQXjTEgMd5zC61sjAl0MmLnVwfjqDDcj4YtRagBoNU9i-rJ-izSnffrLsaayPwImG8FOApj3Qd9I7rWsYY5Nvb9JPfbEoDgvrhCNJMdJE_3WcYChAsgQq9gRnjF89huFPWyZGlhZgJ2pnS9REUDp6SsxupjFnuTe_sMJXaSMe8bjo0Rdced4LrBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/683daff4c0.mp4?token=nwV2xlXNkPqQ9bJVK2sDyzBFT5jLjfoP3eAcXxBKpvuGEdwtgZStqPeGFlii_t3MfAvDlQiYjjiO5DbyAA9MSQdti4RyGxmDfX0tX-fb7nZII6Lu9c-UK-bdZQ0Vztlre8yrCu8A06BsSYMMEKFFx7vvkannlkmQXjTEgMd5zC61sjAl0MmLnVwfjqDDcj4YtRagBoNU9i-rJ-izSnffrLsaayPwImG8FOApj3Qd9I7rWsYY5Nvb9JPfbEoDgvrhCNJMdJE_3WcYChAsgQq9gRnjF89huFPWyZGlhZgJ2pnS9REUDp6SsxupjFnuTe_sMJXaSMe8bjo0Rdced4LrBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز درباره مدت زمان جنگ با ایران:
من دوست دارم همین حالا یک توافق انجام دهم، کمتر از 3 یا 4 هفته باقی مانده است؛ وقتی این کار را انجام دهید، می‌توانید یک قدم جلوتر بروید.
نمی‌دانم آیا آمریکا تمایل دارد کاری را انجام دهد که من واقعاً ترجیح می‌دهم انجام دهم یا نه (تصرف خارک). ما در دو جنگ 13 سرباز از دست داده‌ایم؛ هیچ‌کدام در ونزوئلا نبود، و ما کشور را تصرف کردیم. در ایران 13 نفر از دست دادیم.
در ویتنام، صدها هزار نفر از دست دادیم. آنها دیوانه می‌شوند چون من سه ماه در ایران بوده‌ام؛ من آن کشور را ویران کرده‌ام.
آنها به من گفتند که شما گفتید سریع‌تر از جنگ با ایران خارج می‌شوید. خوب، الان وضعیت بسیار بزرگ‌تری است چون ما بهتر از هر کسی که انتظار می‌رفت در چنین زمانی آن را انجام دهد، کار کرده‌ایم.
ببینید، ما 19 سال در ویتنام بودیم و کار را انجام ندادیم چون رهبری مناسبی نداشتیم، صادقانه بگویم. اگر من بودم، آن جنگ را ظرف 3 الی 4 ماه تمام می‌کردم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77626" target="_blank">📅 17:15 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
