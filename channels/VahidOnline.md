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
<img src="https://cdn1.telesco.pe/file/L-Nv1sQHRBgGzLFTmRvxT6jnIwhrhqhAZHdlA09P6NusykDvqr9Vw8uIBZ6CpoSrLsw2mszoyTr27MNWEWkT-5eRKfLKNUdAa0HB6kwQ8yBQpeHI4LRlY__fK-ZdpCwud0v54z0DCX2nCFetRCJ5CQharleht8m5iIx-f2NXGHpKLsE-4VzbAys5G6C4kwNxXo7qAu2neAOHlHpog8DUPWGZBSK45qPVXHmUxxGHH0K6m29WzfviJpW362YAtW7bvmfS4WAq_vNDKjj-Juj1znaN74cf3ANTioCWVvX3RRhQakUrlMk53KdgjcI6nyqlpE3didstW0DXHxfOW1H7mQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 06:07:11</div>
<hr>

<div class="tg-post" id="msg-76130">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/COCvEbpTiOiWAxhyuvLw5UPeLdJ1q0NdmIe4u6Af9bvVkdirPyRKtLrEJKug40qJKA6GoDRQHs1GDPXrqBbQQQGjRZlCbr3PIIZTsd5hX4Yz1BW4xOyx9KoA4_jl2gWXseXcOQITAPgXSogRIj9lTsri3TcN8Xl2O4o7dwCH0k3CsK9KVRX8LPLKRKyx1v9uJoqvt0Kenw7CsGsREZH252zSdc7xB2hVBU1KuBlUqXCBN2TBUeafMzmvCm0tWKASwnnWGRVwocpGnciVnNTXMp2q3j8y1ZPd1yXn4JoasYIoEE0TLYP0fBFAOpLvF1ygW1VaIx0C55NjsbTJXhQm4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش کویت گفت دقیقه‌ای پیش اعلام کرد که سامانه‌های پدافند هوایی آن در حال حاضر مشغول مقابله با «اهداف هوایی متخاصم» هستند.
@
VahidHeadline
پیشتر
سپاه اعلام کرد
که به پایگاه آمریکا در اردن حمله کرده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/VahidOnline/76130" target="_blank">📅 05:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76129">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mmEIkHlkoLNrH6QWysJQ7giB0xcUYENFXv4jbor_ba4SJgYF9IDZW2lN2tKgntAT6fJv0YKpZbd28XNzn0goz4uQ2YHYzthR6H0OdxGHQjJu4vplWR3w86BX8n5nfVYASqbkK0rRcsdaWicOFWAOGLVdC6FbSH2BDaxt3n3HATuyYI5rE6bTpyvWF0VmmDOzn8d5LyvFyd964k-rOYy1pevfuMwzpz8tCWH_FTCRQspz_Enw35v43gjBX4Dgvpdih4XS6E-B66e9ib8wLgnmiQQJrfCFKCQesIrt9gn03ViOx2_txAQKsBNDsm4XI2yqb3rTc4ymGYxGu-s7CovcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه از حمله به ۲۱ هدف در پایگاه‌های آمریکا در منطقه خبر داد و گفت نیروی هوافضای سپاه با موشک‌های سوخت جامد دوربرد، چهار «هدف مهم»، از جمله آشیانه‌های جنگنده‌های اف-۳۵ در پایگاه هوایی و مرکز فرماندهی و کنترل ارتش آمریکا در الازرق اردن را هدف قرار داد و منهدم کرد.
@
VahidOOnLine
توییت اکانت وزارت کشور بحرین، ترجمه ماشین:
آژیر هشدار به صدا درآمده است. از شهروندان و افراد مقیم درخواست می‌شود آرامش خود را حفظ کنند، به نزدیک‌ترین مکان امن بروند و اخبار را از طریق کانال‌های رسمی دنبال کنند.
moi_bahrain
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/VahidOnline/76129" target="_blank">📅 05:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n3ejOe0R1FUWSV_rWT0iJjFf_hP9Y9rtEAq0AuxDeB0iGuJHMGzeHeqBmnj2M-zDSPO70StDz2o1LzmlOzevZMzMzbCL1XsUwGok86nlCO89jOdK6eGgDRIw0_czXdkPpMJzfDqZbVe1VWUM_kl7PnlYIoKIKtLvS_l8X7ERkroW0Qg0tF6UKW4blcXVczgZFyau9RLXbsP8i82lXdd3h4iSPIGY3OjZqNlpDNII7M_2Xy1bz_mE-wyAB_1yr1arz2rdb-xheXKy6CI6mKJx5tYUvyq5p0k7L2jCoWEnsjUTyN8EpPPF01n-4L9clVx3Eqiwti8jNSZXUmzTrCKVHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار فاکس‌ نیوز، جنیفر گریفین می‌گوید که یک مقام ارشد آمریکایی به او گفت که سه‌شنبه شب به وقت واشنگتن ۲۰ هدف در داخل ایران هدف قرار گرفت. این مقام گفت اگرچه حملات آمریکا به گفته سنتکام پایان یافته است، ارتش آمریکا آماده است تا در صورت تصمیم جمهوری اسلامی برای تلافی، واکنش نشان دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/VahidOnline/76128" target="_blank">📅 04:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkendx6_btI-p2YnlIhJVkQJmB5EoYAIHgzvD4sfSCm2Rmfam6yD_9Y2SG5KysWa46fnuCHc7Q4UyyqVDmpXrESXaoN4bcAc1deHIJhXyFaa-npv9x0RHvZ_l7fp6MOAmsRRW9dQQbXcFqcrjcwHYXr1BLT3xEL1RwjT03Cj5t-PlrZYOxezZ7HFuzVeY1NNnKWamDu_n9d01ER7IwGtjkA7ImR0kCsmwdrXDBhp8LpdqeoOQirJzjTfe7wc7quMhAUrrgYqAlYZUbdwOss0Mbbghqt7Yisc-fl8sMGmGuaibtSBcPzNXS5RiLeOD8mnN78PzKlEnQT7QeH3TNAssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم الانبیا اعلام کرد ارتش و سپاه در پاسخ به حمله‌های جدید آمریکا علیه جمهوری اسلامی، برخی از پایگاه‌های آمریکا در منطقه هدف حمله‌های قرار دادند.
این قرارگاه تاکید کرد در صورت تکرار حملات آمریکا، جمهوری اسلامی «حملات سهمگین و گسترده‌تری» علیه بانک اهداف تعیین شده در منطقه انجام خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/VahidOnline/76127" target="_blank">📅 04:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2fc27bcc31.mp4?token=brF4lEjsSDW-cQCqZ6pgU61vhmPjIdcspRPmOABGRMyshDQsK00_12lmEEBShwbYTlo_kKz7WnS-c8UN8KJEBSO-urKzw0cbtgHx7kBvlaHcUDE59mIHaQGJwdsXJdEr91KvnIBU7Jas-BZDyDSirlWs7Xbeo0Lz4uut4BMNBQ9ccHD102nfhTf_wgSnF9P-MsJhDTd53H42DqrWhvGzsPJXAFr0OHWte9mgT65lbtX6cR_sTaCJU6JVR_3SNVapyDeoh-iIz-frQDgectHs-oUZw_d8nCrc8UH6kwcbvX7OAht_W3xhqG4vRMBhETsmH5_ae7WyeJgWvKRnZet4dg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2fc27bcc31.mp4?token=brF4lEjsSDW-cQCqZ6pgU61vhmPjIdcspRPmOABGRMyshDQsK00_12lmEEBShwbYTlo_kKz7WnS-c8UN8KJEBSO-urKzw0cbtgHx7kBvlaHcUDE59mIHaQGJwdsXJdEr91KvnIBU7Jas-BZDyDSirlWs7Xbeo0Lz4uut4BMNBQ9ccHD102nfhTf_wgSnF9P-MsJhDTd53H42DqrWhvGzsPJXAFr0OHWte9mgT65lbtX6cR_sTaCJU6JVR_3SNVapyDeoh-iIz-frQDgectHs-oUZw_d8nCrc8UH6kwcbvX7OAht_W3xhqG4vRMBhETsmH5_ae7WyeJgWvKRnZet4dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید  ساعت ۴و۳۶ دقیقه
خمین ۳ تا موشک پرتاب شد
همین الان پنج تا موشک از خمین شلیک شد ساعت ۴:۳۵
سلام وحید جان  همین الان ازنا لرستان زدن
ساعت4:37
ساعت ۴:۳۵ از خمین چهارتا موشک زدن
از خمین حدود ۴ تا موشک فرستادنننن همین الان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/VahidOnline/76126" target="_blank">📅 04:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iB2H3EtH4wMjuC-SRHszUl8Psdu7WcMzQwr2x64tw3lxGmVt7Rw9tNI_TPyhR31NWtx1BMUv3tHIc2xEV-k0AC7zPTfhf73-b5TfabAJXBXOcki5PLCPqgqrgrISi6sUz894HskqOS5zbfrprjqrpMokwK15nLogeTJJsj6fAFxgCzVRKYPfHHCfRg-SjfHqAzzjAqaa2Gjc4we92DaDojcD1YJ6Mtdx4OrvJkVgC9YbtucxGqggoFch4Wri1YAIgqm1Vr7C-1UtmbJxgGl_zFqNiPtncaqwKTwo92XvM4d0Gc29naG7PwTtgGXlYfmllJ4gBdmpzLL10LMUZdo-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
آمریکا حملات خود را در پاسخ به حمله ایران به آپاچی تکمیل کرد
"
پست سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده، سنتکام، روز ۹ ژوئن به دستور فرمانده کل قوا، حملات دفاعی خود علیه ایران را در پاسخ به سرنگونی هلیکوپتر آپاچی ارتش آمریکا در روز گذشته تکمیل کردند.
نیروهای سنتکام با استفاده از مهمات هدایت‌شونده دقیق شلیک‌شده از جنگنده‌های نیروی هوایی و نیروی دریایی آمریکا، سامانه‌های پدافند هوایی ایران، ایستگاه‌های کنترل زمینی و سایت‌های راداری نظارتی در نزدیکی تنگه هرمز را هدف قرار دادند.
این عملیات پاسخی متناسب به حملات اخیر علیه نیروهای آمریکایی و کشتی‌های تجاری بین‌المللی در حال عبور از آب‌های منطقه بود.
نیروهای آمریکایی همچنان هوشیار و در موضع آمادگی برای دفاع در برابر تجاوزات توجیه‌ناپذیر ایران باقی می‌مانند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/VahidOnline/76125" target="_blank">📅 04:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه:
"
سپاه پاسداران: یک فروند پهپاد MQ9 دشمن رهگیری و منهدم شد
در جریان درگیری‌های هوایی جاری در تنگۀ‌هرمز یک فروند پهپاد MQ9 که از آسمان شمال خلیج‌فارس قصد نزدیک شدن و مداخله در صحنۀ نبرد را داشت، در آسمان شهرستان جم استان بوشهر مورد اصابت آتش رزمندگان قهرمان پدافند هوایی نوین سپاه قرار گرفت و منهدم شد."
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/VahidOnline/76124" target="_blank">📅 04:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76123">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d621f55f6.mp4?token=AUTC0RYXou8BURYeI_aNC-rj75W0PGM49jjoBf7RMh21ag5bz59A0-2HBSJQhnXri1zVZEc1VXAZmYR41VVBgP5J7LlbFC1KOscLdwX3sialHZ3Gqg_BMxRjlQTiYTVW6-G9OGi03ELo9WE3CvB1TYRNYhSWTHy9DWFXaJWGtn-E8T_TueCwgSYKITqLkQa05DmPTYC4_2ZIAwflakhdU_sMBfjIxtbwsuIczYjTGMZSVE66bIOfxzYlR9xXmbmjioQEAkdMxC76k9U6YWoeh9pt9HoC2VUYNhrvXIDm2JJsMn8fpd9jKYr3sTrY1-nns1hpw0baBfZ3rqFcO2NsVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d621f55f6.mp4?token=AUTC0RYXou8BURYeI_aNC-rj75W0PGM49jjoBf7RMh21ag5bz59A0-2HBSJQhnXri1zVZEc1VXAZmYR41VVBgP5J7LlbFC1KOscLdwX3sialHZ3Gqg_BMxRjlQTiYTVW6-G9OGi03ELo9WE3CvB1TYRNYhSWTHy9DWFXaJWGtn-E8T_TueCwgSYKITqLkQa05DmPTYC4_2ZIAwflakhdU_sMBfjIxtbwsuIczYjTGMZSVE66bIOfxzYlR9xXmbmjioQEAkdMxC76k9U6YWoeh9pt9HoC2VUYNhrvXIDm2JJsMn8fpd9jKYr3sTrY1-nns1hpw0baBfZ3rqFcO2NsVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما:  دو انفجار در بندر عباس
هنوز درباره محل دقیق انفجارها و جزئیات اصابت‌های احتمالی، اطلاعات دقیقی در دسترس نیست.
دو‌ مخزن آب در سیریک و‌ بندر کوهستک بطور کامل تخریب شده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/VahidOnline/76123" target="_blank">📅 04:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76122">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
یک صدای انفجار هم تو اهواز اومد 03:53
سلام وحید جان، اهواز ساعت 3:53 صدای بمب شنیده شد.
سلام همین الان اهواز رو زدن
همین الان اهواز صدا انفجار زدن پنجره لریزید
یه صدای شدیدی اومد که خونمون لرزید همه همسایه ها ریختن بیرون
سری قبل کولر روشن بود اصلا صدا نمیرسید این خیلی شدید بود
آپدیت:
خبرگزاری مهر: صدای انفجار در اهواز شنیده شد
منابع محلی از شنیده شدن صدائی شبیه به انفجار در اهواز خبر می‌دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/VahidOnline/76122" target="_blank">📅 03:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76121">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
‌
از جم شلیک کردن ساعت ۳:۳۳
نصفش تو هوا منفجر شد،بقیه‌اش هم نمیدونم کجا قراره فرود بیاد.
بعد از انتشار پست: وحید جان نزدن،تو آسمون منفجر شد،صدای اون بود.
سلام وحید جان شهرستان جم رو همین الان  ۳ و نیم صبح زدن، یه صدایی اومد ولی چون پنجره‌ بسته است لرزشش خیلی بیشتر بود
ساعت ۳:۳۴  شهر جم رو زدن
اول فکردیم موشک بلند شد
ولی بعدش خورد زمین ترکید
سلام فک کنم جم رو زدن یه صدای انفجاری اومد الان 3:35
توی جم این پدافند بود فعال شد اون صدای انفجار هم پهپاد زدن باهاش
قشم: دوباره یه لرزش دیگه ۳:۳۹
احتمالا بندرعباسه ما داریم حس می‌کنیم
وحید هنوز صدای انفجار قشم داره حس میشه
همین
الان پشت سر هم
سلام وقت بخیر ۳:۳۸ بندر عباس پایگاه هوایی رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/VahidOnline/76121" target="_blank">📅 03:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76120">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBaZ7yMivsi5G0m2DMGB1rCXV5JBpUozmgAqUpt_MmHKLdzX2MCxAti8cPEzdWJW_7UCLmlBX8jup2A--4p6aZH7vDrCaAb9_80Z9-pYbT8oKB95HxiN5Z24-gD_n4qRHUF54Ali4mPDnH2CTSu1dzJ0RcjnSYheSmxmgiw7J4dpbNIwso7EXQ4Q0byr4Cwfa14EZOKalKgLlbGQWyJcmiyIg_vnBWES23erqzjJSY6c9ygWPApD_E7ka0GupdWDRriVxQ2-Slz0yP8f88WeLHUhjV7RmCBlhMBl4sDUtJiZ4xQHRqwXTD-HssVdy_gqCv0DEXJeazrkvzbwdqyZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک جانسون، رییس مجلس نمایندگان آمریکا، گفت پیشاپیش از دور جدید حملات آمریکا به جمهوری اسلامی با خبر شده بود. او این حمله‌ها را «متناسب و محدود» توصیف کرد و گفت این عملیات سامانه‌های راداری، موشکی و مراکز فرماندهی و کنترل را هدف گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/VahidOnline/76120" target="_blank">📅 03:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76119">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پیام‌‌های دریافتی تایید نشده:
سلام وحید جان، ۰۳:۱۸ و ۰۳:۱۹ دوتا صدای انفجار اومد بندرعباس
الانم دوتا وحشتناک تر
🤯
همین الان بندرعباس صدا اومد ۳:۲۱
سلام وحید همین الان دوتا انفجار شدید بندرعباس
وحید بندرعباس انفجار شدید
همين الان بندرعباس صدا اومد ٣:٢٢ دقيقه
درود بندر ۳.۲۳ انفجار پیاپی + ۳.۲۲
و مجدد ۳.۲۴ بندرعباس
دوتا صدای وحشتناک ۳:۲۳
همین الان بندرعباس
سلام وحید سیریک سمت روستایی طاهرویی صدای انفجار شدیدی اومدم فکر کنم نیرو دریایی سپاه رو زدن
سلا وحید جان، همین الان بندرعباس صدای دوتا انفجار پشت سر هم اومد، ترسناک بود
صدای انفجار بندرعباس همین الان دوبار صدا اومد
صدای نسبتا شدید و خطرناک
وحید ساعت ۳:۲۴ بندرعباس صدای دو تا انفجار
بندرعباس ۴ انفجار
قشم ساعت ۳:۲۳ بامداد ۲۰ خرداد
در محدوده طولا یه لرزش نسبتا شدید احساس شد ولی صدای انفجار خاصی نیومد، شاید زلزله شاید هم انفجارات حمله‌های اخیر بوده که لرزشش رو حس کردیم، خونه کامل لرزید
سلام وحید جان همین حالا قشم ۲ تا صدای انفجار اومد ، دومی نزدیکتر یا شدید تر بود
بندر دوتا انفجار خیلی شدید پشت سرهم اومد سمت پارک جنگلی
ساعت ۳:۲۳ بامداد بندرعباس یه چیزی منفجر شد
سلام سمت پایگاه هوایی بندرعباس رو میزنن
#قشم
، 03:23، 20 خرداد صدای بلند انفجار شنیده شد. (شاید صدای انفجار بندرعباس بوده)
سلام بندعباس صدای انفجار الان چهارشنبه ۳:۲۴
نزديك  پایگاه هوایی بندرعباس خونه ماست به فاصله پنج دقیقه چهار انفجار بزرگ صدا اومد
اقا وحید بندر خیلی صدا  انفجار میاد
سلام وحید جان بندرعباس 3:24 دوبار زدن صدای خیلی زیادی اومد همراه با لرزش
وحید جان درود
ساعت 3:24 دقیقه بامداد چهارشنبه 4 انفجار شدید سمت فرودگاه و پایگاه هوایی بندرعباس
۳:۲۳ دقیقه ۴ ۵ تا پشت هم زدن بندر رو
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/VahidOnline/76119" target="_blank">📅 03:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76118">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdW0pJqgekdoZdU37_HSAGQ4Zzmui479mJmafYXZ5oBNoHbJUpcB3FvfiukikiKsuCh6zEEbT2r1s0Cj1gN-moJ3JVE2V8eN5eIve10rNDfSlzG9BcySwSM4axgQ0Fcxl4jETeERbjQpsxBGcXKv78vbOuvURu8SSqGtntLrhw9DRLlQGNYDbW1STul7sXmT1mdoRv4LgTGeA9iMG6HGvHrrqxRRRe00Ee8Df5PFProL-3nPgHyuViPrACmgkVdGZqdHABqIscR4eMVGzCvCZZ3jql-Hidt0p31nZtAeVmL8ttzv4F0Y3fDaSl-R3hIf0MH2r622FVxiVBdNuDIQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر به نقل از منابع محلی و ساکنان روستاهای اطراف، از شنیده شدن مجدد صدای چندین انفجار در محدوده شهرستان جاسک خبر داد. پیش‌تر حملات نظامی به بندر جاسک و کوه مبارک توسط منابع آگاه تایید شده بود و این حادثه، دومین موج از صداهای انفجار در این منطقه از آغازین ساعات بامداد چهارشنبه به شمار می‌رود.
@
VahidOOnLine
من هم حدود ساعت ۲:۳۰ چند پیام از جاسک دریافت کرده بودم.
خبرنگار آکسیوس هم به نقل از مقام آمریکایی گفته یک موج حمله دیگه انجام شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/VahidOnline/76118" target="_blank">📅 03:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76117">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">موج حملات آمریکا «فروکش کرده است»
رسانه‌های ایران از «فروکش کردن» موج حملات آمریکا خبر دادند که می‌تواند نشانه‌ای از «مقطعی و محدود» بودن این حملات، تلقی شود. چنانچه سنتکام آنها را «متناسب» خوانده بود.
خبرگزاری تسنیم  همچنین تصاویری ویدیویی منتشر کرده و مدعی شده که یک پهپاد شاهد ایران در آسمان عراق مشاهده شده و آژیرهای خطر در کویت و بحرین که میزبان پایگاه‌های نظامی آمریکا هستند به صدا در آمده است
اما هنوز جزییات رسمی در این باره از سوی رسانه‌های بین‌المللی مخابره نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/VahidOnline/76117" target="_blank">📅 02:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76116">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرنگار صدا و سیما در سیریک: در پی حمله امشب آمریکا به سیریک، ۲ مخزن آب بخش بمانی مورد اصابت قرار گرفته و آب آشامیدنی این بخش قطع شده است.
"خبرگزاری صداوسیما" در خبر دیگری نوشته: هیچ بندر تجاری در جزیره قشم هدف قرار نگرفته است. در پی شنیده شدن ۶ انفجار در قشم برخی کانال های خبری از حمله به یک بندر تجاری در قشم خبر داده بودند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/VahidOnline/76116" target="_blank">📅 02:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76115">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TfjUyXrucMq82jDT45RdU97z0PdppMeWwxJo6PJ2D6l2ayKmgmSUxF4Kbe0aP3ekVs4_2U_GqGs0UrlzYeNkXL-B4K6ANTQdvlEYLxHgk6AzD7hhOdJSSOEb43kqXR_wvi9FBid_9o_b8tU9iK0yhdL_c8771TsH7HVYioLobBySt7hyGt_kQDf7CyKJHaLxPhYQNg7zcC6vfEC4ZgJhvptTwRVmMKFmo2kW4NRGQpOHTk1IwEl-VS0YV3UeSnUIFHHgzG4cqYn18LGGhEAD4Z3BxBU_cjSUlGYIvbY-CtAmJFoU1Mh0-ONRTipTT-Wdawv1wsZY3igLIAj8FrJGCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت تازه عباس عراقچی، ترجمه ماشین:
با وجود شکست‌هایش در میدان نبرد، ایالات متحده تصمیم گرفت عزم ما را بیازماید.
نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نخواهند گذاشت.
اگر می‌خواهید در امان باشید، منطقه ما را ترک کنید.
تاریخ خلیج فارس فصل‌های بسیاری درباره سرنوشت‌های شومِ بیگانگانِ مداخله‌گر دارد.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/76115" target="_blank">📅 02:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76114">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HxHx168HB76_EZ0CWyi8uwNrII1qpTk0PxhrkLecJ57VZdwyILVjJ3LO2elxiiAdbyE8FNqgVLZwTWuptMZh4Ios2e64a2ZN4kOFcspHNFi6sG-pkDcFTeVEEMvVu7xVkmn_R-UItPk1Wbyg5sHqKV3qAxgs54BbSh_UZyBC8f5yhWZRpp5_Q61gO8CnkQle6IXv8jUfT3WjdJ_3EnPcc1CwjBugkrHsSHDlBnK3VffUaHLkSUFiJr51c1c-7v8cISoZ5csMcPPOxFoHAy-JTLNLRiU5Ercz4tn7mtKQtN3_u2lvHkTKqAvCnKPfg8-8Lxb1w0rH7cQfqKWEq5ocZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان گفت که حملات جدید سنتکام با قصد هشدار دادن به جمهوری اسلامی است.
او گفت ایالات متحده معتقد است که این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/76114" target="_blank">📅 01:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76113">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41278e3d2c.mp4?token=SAOYRSYs9SAqk1SezOeaYLJTL7IEN0hsq23SuWmX7VPXP8aU-mcub363zQGTOYHiatHvT9SuxHGtHUIpEV-6NsIrHtrsSD0ThU6OwdkcyN3extykcrxF4eBL-D38tzMgjoit6pmNkMnWHkuS0uj1FnCQQeVaQ-66jFNuFi__o5K0LZCIpP_0YV5NwfTSBI0biuqpRdSDpGsDxQ1Yd-MFL1cNxhjIi0ymYUPlStoCNXlh1_QM-00kJu8gxvCn5TNbiW_Cd1UPvkavL_tO4ltBiGua4sFDh6mC1yjgcev61aSUmnX_Oam18FQPCzg9ZAiC6Pb5A5CUKdQvlvTv8Y--UA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41278e3d2c.mp4?token=SAOYRSYs9SAqk1SezOeaYLJTL7IEN0hsq23SuWmX7VPXP8aU-mcub363zQGTOYHiatHvT9SuxHGtHUIpEV-6NsIrHtrsSD0ThU6OwdkcyN3extykcrxF4eBL-D38tzMgjoit6pmNkMnWHkuS0uj1FnCQQeVaQ-66jFNuFi__o5K0LZCIpP_0YV5NwfTSBI0biuqpRdSDpGsDxQ1Yd-MFL1cNxhjIi0ymYUPlStoCNXlh1_QM-00kJu8gxvCn5TNbiW_Cd1UPvkavL_tO4ltBiGua4sFDh6mC1yjgcev61aSUmnX_Oam18FQPCzg9ZAiC6Pb5A5CUKdQvlvTv8Y--UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام آمریکایی گزارش داد که حملات آمریکا به جمهوری اسلامی ادامه دارد و اهداف شامل سامانه‌های پدافند هوایی و رادار است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 196K · <a href="https://t.me/VahidOnline/76113" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76112">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPORqQOxprVkgjoKxbTf0clKo3PkWsLNEpoEpmT52O8NHD58v560G5Kb2W-AdVy7sTFEICftIRGrU5RSLsN5t5Z-XvEcMHOaKCxxDaLY-galGrIFPbTSwtj-3ol-A2cMqZWxdFd7x5OOsE0pvXLFxHz19V7OBFOEctfQ_9j52I4Rvag5bE8-9VS6hha-jx-f34JJUycKdstRWEKQ0oHfkONzxSI0vThPsHFz1-HG1_wBTKJibZ7fHUvNpKrfPVOGRCWlAvFk6jGgCi_HOVxQC--gYh43SAuI03yz90aW_yB2jAHrevLFgbPPNwtCbjTUodVZ-AcapR735qIQ7rOfmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، سه‌شنبه‌شب، در گفتگو با شبکه خبری «ای‌بی‌سی» (ABC) درباره آغاز عملیات نظامی واشنگتن علیه ایران گفت: «من فکر می‌کنم پاسخ دادن امر بسیار مهمی است. آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین حالا که صحبت می‌کنیم، در حال پاسخ دادن به آن‌ها هستیم.»
ترامپ با تاکید بر موضع قاطع خود افزود: «این اقدام پاسخی به کاری است که آن‌ها شب گذشته با هلیکوپتر ما انجام دادند و من معتقدم این واکنش باید بسیار قوی و قدرتمند باشد و حملات جاری نیز دقیقا همین‌گونه است.»
@
VahidOOnLine
"خبرگزاری صدا و سیما":
سیریک اصابت یک پرتابه تایید شده اما مکان و نحوه اصابت مشخص نشده است
برخی منابع از شنیده شدن صدای انفجار و فعالیت پدافند در بندرعباس، قشم و سیریک خبر می دهند.
"به گفته یک منبع آگاه ۶ صدای انفجار در قشم شنیده شده که بر اثر پرتابه های دشمن بوده است.
ظاهراً این پرتابه ها از جنگنده شیلک شده است."
من از جاسک هم چندین پیام داشتم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/76112" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76111">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HA_cdnODD1waQ7iQ5v2dmGGyUOfoclbFYm4WIGADHUj1q9h8iRdovrDbNJ6dZSkk-DWD3-whllueewlK9AUD0OYDlAB1yg9Ilj2fuMy3yMr1ip7tFkFyCJH7XSi1LnBb-fgXEflEQt08KS2PLIJfbzw5JcGjcLqTfVohxlkxCBYs0BS7ldLT_HblTi9_PPGtLBkvCr-i5WxCpKCW9orfWappfb4qeaCPsypdOWLEGSd705djbwj9apF-V0PTuOgwIb46sNT2ctTDqZL0ZXduLLeX-HZWqpjIylGQIUabCBfMP7wzw9WvKvYGx71D-gWtJFfSg-G-uzKidY347f18vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
سنتکام: حملات در پاسخ به سرنگونی بالگرد آغاز شد
ترجمه ماشین:
فرماندهی مرکزی ایالات متحده آمریکا، سنتکام، اعلام کرد نیروهایش امروز ساعت ۵ عصر به وقت شرق آمریکا، به دستور فرمانده کل قوا، حملات دفاع از خود علیه ایران را آغاز کردند. این اقدام در پاسخ به سرنگونی هلیکوپتر آپاچی ارتش آمریکا در روز گذشته انجام شده است. این مأموریت پاسخی متناسب به تجاوز بی‌دلیل ایران است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76111" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76110">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پیام‌های دریافتی از ساعت ۰۰:۳۰
صدای چندتا انفجار بزرگ پشت سرهم شهرستان سیریک
وحید جون سیریک صدای  انفجار اومد
وحید بندرعباس صدای انفجار میاد
چهارتا انفجار سیریک هرمزگان سه تای آخری کناره های ساحل
وحید بندرعباس صدای انفجار اومد الان
صدای سه تا انفجار شدید از سیریک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76110" target="_blank">📅 00:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76109">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ep5lf03Uy2W_3b2oKCxwe-pndW-xhTCxVDHQVRYz8J3EHy_Rz2Mw3xzGI96ld7ZubTSjjNmUnFDktrxmB_45_p6i_LJf0tST9o1MiIfEgve8rqiR0ofwUWrSVbZbf6qbDRFQ_JtSQrfbwBxHc1RvJ3_GcxwKk0zDp11HHq5IX52-X4ci5a75MThPPxQi2PnbmwiTuw5O7EQLSg4KFgarbboE3uMfqRY5kzk19TqkyiS-j1VUnafjw_uqRT9Fe7iZ0IrL_Iak95rab_CkhD3PDkp7kp74tE3diJbYwfx4mbisqJ3Us7vzbe_jgl9lrcIoElGZLX1fe-8AW1SQUksPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نظامی نوشت: «در ۲۴ ساعت گذشته هیچ عملیات نظامی هجومی هوایی در تنگه هرمز انجام نشده است».
@
VahidOOnLine
پیش‌تر خبری بدون ذکر نام پخش شده بود که:
معاون وزیر خارجه جمهوری اسلامی ایران، روز سه‌شنبه، ۱۹ خردادماه، در گفتگو با «الجزیره» اعلام کرد که هلیکوپتر آپاچی ارتش ایالات متحده که روز گذشته در تنگه هرمز سقوط کرد، به طور عمدی توسط ایران هدف قرار نگرفته است.
این مقام رسمی با تاکید بر اینکه ایران پشت این حمله نبوده، در عین حال هشدار داد که به دلیل شرایط به شدت ملتهب و متشنج منطقه، ممکن است بروز چنین حوادثی در این فضا «عمدی» تلقی و تعبیر شود.
همزمان، دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگوی تلفنی روز سه‌شنبه با روزنامه «وال‌استریت ژورنال» با کوچک جلوه دادن حادثه سقوط هلیکوپتر آپاچی گفت این اتفاق «مسئله چندان مهمی نبود» و تأکید کرد که «حال خلبان خوب است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76109" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gJevVMV9h87aSuJ5su3CUyQZ8QyUO1-CXZsOKRrAPJKe8zVxHhSN0-YQqlMGOZe_MY73jGKubwDlubdTiIXyPHSpriwQzdI1waNJQYoZ6siixrpN3GoNmsENZpLhyEYApDIldnh6jwFuzOXMJeRdBXS_iRLr_UJt_9CtU2vAZtZL1Rr53t720UO8V9kgakQ7WeyMDixUPn_E8SIlFJwNpvpXEA5FUB7RJd2IaBgY70oTVp6tr0hKFidI_GBL-s_2ZQLSirwA8bw6Q4XG1vfP8qKKYZDmiPrKr-SwEvyU2vwyyMRfPycGuGzPtAzJZ_4zptf_95YAXYFWFp6IMDMbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PXqqxlSGzzUXlNLr4eyJEE4AuOSUjwPXZhhRJUOvWAwn8c4dUoC26d8ONWxWdHFs27T7KM7V52ePJKSiIlvzjvasdswk0pPaprzma8hVNUqEqzdC0tSqpi3541jlGpHVDbDvoC_luqiORpbUFgQF6mLTyWhSrXa9zcdFiQ6_ksmJr3On2WBYREFEzZ32kGY_LgGNI-k_u8e9LQayxG4xonIeLyJX17ugnKLzgETQcCwtx-FrkK0JjhZ-VcLTuXscBq53kDWULP_MqAbuKQY-7hU4Hq_o4c18DQ-bsAmhhu7IK6u-8ZGTVDOkHMGfDqkH4sUkcTc20dr5imZaFlrJww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگوی تلفنی روز سه‌شنبه با روزنامه «وال‌استریت ژورنال» با اشاره به اثرات شدید تحریم‌ها اعلام کرد که محاصره دریایی بنادر ایران باعث شده این کشور «بسیار فقیر» شود و واشنگتن این محاصره را تا هر زمان که لازم باشد حفظ خواهد کرد.
ترامپ همچنین با کوچک جلوه دادن حادثه سقوط اخیر هلیکوپتر آپاچی آمریکا گفت این اتفاق «مسئله چندان مهمی نبود» و تأکید کرد که «حال خلبان خوب است».
بر اساس گزارش سنتکام، سرنشینان این آپاچی پیش از نجات، دو ساعت را در تاریکی شب روی آب سپری کردند و یک مقام ارشد آمریکایی فرار آن‌ها از این سانحه را معجزه‌ای همچون «دست خدا» توصیف کرده است.
@
VahidOOnLine
وال‌استریت ژورنال نوشت که حادثه سرنگونی بالگرد آپاچی در تنگه هرمز برای ترامپ «کم اهمیت» بوده است.
این در حالی است که پیش‌تر ترامپ در تروث سوشال تاکید کرد که «ایالات متحده ناگزیر باید به این حمله پاسخ دهد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76107" target="_blank">📅 00:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LXOkTSZDfCM5P65vBD-yRJGv4-eMONhxIuc42BdPm0w3r6-ouA2s91SQPr5PJT23Mc5-TzgAYnol8SgjVk6hqtuQrReW0FvLUcAx8tB3IU4DyZi5ykAUC-k725-7c4C6y-LBfdyqYkRmxT2PZj3xWzUPHQy3WZJb_LXE3OqE3aPzrt2cHVxfH2ZboFxmPP7JQrrOH_J9zUw7NjIFSThdqCMxxq6AZaXWZjdsUNFYlaOGXwVAtMDZ1tqXoTYuSjpXn92tfk94_W8IoMY7LkhVI8glYQiseYWEKxoi6kf7QR6PxJeEdPu3TIEaixVkteN93faA6NqeHZb2WVRn7c6iYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عراقچی، ترجمه ماشین:
نیروهای خارجی در نزدیکی قلمرو ما همواره در معرض خطرند؛ چه به‌دلیل خطاهای انسانی خودشان، چه حوادث ساده، و چه احتمال گرفتار شدن در آتش متقابل.
برای کاهش خطر، بهترین راه‌حل این است که آنجا را ترک کنند.
ما زبان دیپلماسی را ترجیح می‌دهیم، اما زبان‌های دیگری را هم بلدیم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76106" target="_blank">📅 22:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/spOQ1ik9CPP3wK9T3k_oQd3HrS26U0Q8hSnf26HI990kwb1ryJYQjYZl4FfSC0XbY3q9vDb0t2HNJmiWjaCZuynWdFE2W9JhJGnZvoVZjEHUn2Oc9b7On2N9YGEcesxo45QnwoThrIPCRlqcs-o49UtAxy-d4hDlzPwNdHlWXW_GAwTv9ynTM4lVgFYJrEMPoUfxP19sXCOs0pzy_wfQmPRF-sr__3JWXlOh6jtNT_weFl-EaWBrYgWpdXqgtBgLiSkY2lvhE9GCgbHHPzOEBjHjMWlLN9OKBl0YLag2DjFZVa7naGJO0IVx_jrPSLLiYzAoTSqnK9OsNnNYoy_gag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری سی‌ان‌ان به نقل از دو مقام آمریکایی گزارش داد که هلی‌کوپتر نیروی زمینی ارتش این کشور که در سواحل عمان سقوط کرد، توسط یک پهپاد ایرانی سرنگون شده است.
یک منبع آگاه دیگر  تایید کرد که یک پهپاد از نوع «شاهد» به این هلی‌کوپتر آمریکایی برخورد کرده است.
یک مقام آمریکایی به اکسیوس گفت تحقیقات هنوز مشخص نکرده که آیا این برخورد عمدی بوده است یا نه.
😱
‍
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76105" target="_blank">📅 21:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F8ARwItN2DuxoPGrYluy2y1Ehk8R_J5Ss9vuGjkFnHwvEWTYXIskoubVe0oSWGNHCHQA2QVOEv6MkxEoqNipY2xhZM5-diH6CRTeAYQo_e__B_7C6ub07BV5xA9f-2NR5qBK_6DvlzdfWLyRFCl5JPmzZrlPk-zSNEmDttzbjvh2hP9lsBvwYy5nPcWvYxjwCZPENFMWtu48MPADVrz1tkyxkDfM3SiTnGzn32CzwayH7pzaJsKPA5Ac9YYFu2L_vyZr9LAqgUWMTLbHlAXqsH79ezJV1tfWkJP4SsOPWlZCvxYBkcPazvaQh5CrRtGg7MZCyo5lyJ1fY_D7LXPj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
ما زبان دیپلماسی را ترجیح می‌دهیم، اما به زبان‌های دیگری بسیار روان‌تر سخن می‌گوییم. تعهداتتان را زیر پا بگذارید، آن‌وقت ما به زبانی روی می‌آوریم که در آن بهترینیم.
خودتان بر اسبی سوار می‌شوید که زین کرده‌اید!
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/76103" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76102">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KsUj1L8t9W7rsoUv--y2F8KEqZodjmtbkSwGzO5I8mn_kKKxTF_eMDhDPp_Y9Zbpf_9vjLE19FOjKKeaj-1aPI0J1mVEWE7T9FWxgBYuzKlQ7p4Vp8q8QvyIEu8Zvy1KhzBXQ2zV83ccs07eoVbSm_R2MLiQtbRrxucXy_3FE0Sk58-X4tMUPTCIveLlHyIjYce3uhhDu1xiRrqppwU86120ibmVk-uhOm1GbeIG-VxVy7uArxGdizA8SPJgimIGnNR0Q-xewY4dVnFLZIxOSXipgZaafK6Wv--OBNCanRMggb6xqcPIzFtZBT4N2zlwszZ0WaKVEGmZovZ0ck5nFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: ایرانی‌ها بالگرد پیشرفته ما را سرنگون کردند، ناچاریم پاسخ بدهیم
ترجمه ماشین:
به‌تازگی از سوی ارتش بزرگمان به من اطلاع داده شد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی بسیار پیشرفته ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کرده‌اند. دو خلبان در این حادثه حضور داشتند که هر دو سالم و بدون آسیب هستند. با این حال، ایالات متحده ناگزیر است به این حمله پاسخ دهد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76102" target="_blank">📅 20:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TXsmDhodT6bQ7pJz4mOnhnZW6JeBvZFGxgp3MsYtLEMoHv9muQSYZViMi7Hx2yKCq2lhoBUheljvpTVCVxsZGDeRF7cFB7Tc_aYJnHjPoXvsrlsjGP2yPf_g8mzOrYR7c95VWipTn_Q05c8C57wzHJwVzCD-wra88etgJ3vOnHraZMOjU0TA-k_fcJcQPlSoLtztejo-I7ZxiDS2Ny5yWB4_dnz-BVp3wQ3aELQGm0hRLQUzq5oXEoN9Nvtb92sAyRtyUeST7xDDCtcN9FFslMIuSkIw-P5v8VJztMvxgrP58Z82D_3BbdQCoB6MofeSM6fsjLjtQRSpEwr-n7DCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f396691769.mp4?token=gwZUtaSpQ-6tzxKTkHX3wr4jBO-PAgdf-yohMiFcUj7bOglXQywrMZ8xppbApAH8qKm83Pv6ubcdENKUut8_qBQv_yQNKga7lzX2wUsyPBWXh9Rd3EBj4jUOo_cLmFZBli-Ja8FYozX5TcaVEpXUYRJFVtFGgthHFGIWYTPc0bOaJx52Xfbf-mwQEcYrT1d-V935XFnEeY5Xy38Jq-6WT-YUprwyZ2ixNvPEDYVnudN9BZKSigYvCq8RXyae1fkpdJ2ppt36UJVUf6v1btQBRETk24gQlWTeDKiaHMEfmw5ivl-y7tvNhN6IpZb_iZCFRbRFrQhOTQ_YMTPDJ7sB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f396691769.mp4?token=gwZUtaSpQ-6tzxKTkHX3wr4jBO-PAgdf-yohMiFcUj7bOglXQywrMZ8xppbApAH8qKm83Pv6ubcdENKUut8_qBQv_yQNKga7lzX2wUsyPBWXh9Rd3EBj4jUOo_cLmFZBli-Ja8FYozX5TcaVEpXUYRJFVtFGgthHFGIWYTPc0bOaJx52Xfbf-mwQEcYrT1d-V935XFnEeY5Xy38Jq-6WT-YUprwyZ2ixNvPEDYVnudN9BZKSigYvCq8RXyae1fkpdJ2ppt36UJVUf6v1btQBRETk24gQlWTeDKiaHMEfmw5ivl-y7tvNhN6IpZb_iZCFRbRFrQhOTQ_YMTPDJ7sB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طالبان به تجمع مدافعان حقوق زنان و مخالفان حجاب در غرب افغانستان حمله کرد
AngelaGhayour_
مقام‌های امنیتی افغانستان روز سه‌شنبه ۱۹ خرداد تظاهراتی که در حمایت از حقوق زنان را در ولایت غربی هرات برگزار شده را متفرق کرد.
این اعتراض پس از آن آغاز شد که پلیس امر به معروف طالبان گروهی از زنان را به اتهام نقض قوانین اجباری پوشش بازداشت کرده بود.
به گزارش خبرگزاری رویترز، شاهدان گفتند که در جریان حمله طالبان یک نفر کشته شده، چندین نفر دیگر زخمی شده‌اند و ده‌ها نفر از جمله زنان و دختران بازداشت شده‌اند.
..
به گزارش رویترز، هرات که مدت‌ها به‌عنوان یکی از پویاترین شهرهای اجتماعی و فرهنگی افغانستان شناخته می‌شد، دستخوش تغییرات قابل توجهی شده است.
...
شاهدان گفتند اعتراض‌ها زمانی آغاز شد که مأموران امر به معروف تلاش کردند زنانی را که با الزامات پوشش اجباری مخالفت می‌کردند بازداشت کنند.
برخی از ساکنان گفتند مأموران حتی زنانی را هدف قرار دادند که از پیش نیز پوشش مورد نظر، شامل پوشاندن کامل صورت و بدن، را رعایت کرده بودند.
@
VahidAfLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76100" target="_blank">📅 19:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M0hTVGzhAom7OQxwSBTnc6-D0bZJ1UD9RuQboj38Ew9EDA961NsTKyUlYCCwkKtUFz-Nmlf0pOgnIJBEuq56V3puBONbJyljjwf9ZxzUBKSXDkkgXrnocF1F7q1QdiwQo1igLo7b2n2T5G0a997q63kyW2Xo-Hm_sBs7JxCsn7w0gd0GI2QEsrUEFjf_jCH2fUt_KwbMkS8Iwmf6bwd4Sok3HPIgBWTJjlj7g_BYpCqUlBqysUigFyIuFP3uOVjFcXfqEYdPTLBeVdFVp96ou66YPeTjhrvVkQMJWvKvXayoRR1D5Mtg5m9wUyhSabi9itG-HXa5ttGTn5JkPz7vWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا پیغمبری، جوان ۲۶ ساله و از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴، توسط دادگاه انقلاب تهران، بابت اتهام «محاربه» به اعدام محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76099" target="_blank">📅 18:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/677a13e326.mp4?token=CCI-o-Lw0fXTRK5TpDMqZ50OviALaYLDkHa56tHGsyvhEG9fhL-9vJFBdevJ7B8zl7Qvb8jUcts-zuAGYCR4M-mONbMICGcKMDDxKKM8ZAEaCd8npZnCOwhxN7kDSKMcG8m2kabiS870lcnzyDb55DLVLySoei6b3ZblzykT1Y1wxwpiwFmKDWmDi8SQLlGdRW6V3vyuA7BjMvKBhDdaXgD69IBmNBdoz6aSrwx1iX71hjqxhhb6tf7ARXv4HrzYjuIcu9yhh9dKhe0ljt9kjtBLUs79cBvd4R_co9mBIxOpzjkH7FWe5dl-nU8gA_5Zn7g_yKFGcxYGY5Ql2Q0wuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/677a13e326.mp4?token=CCI-o-Lw0fXTRK5TpDMqZ50OviALaYLDkHa56tHGsyvhEG9fhL-9vJFBdevJ7B8zl7Qvb8jUcts-zuAGYCR4M-mONbMICGcKMDDxKKM8ZAEaCd8npZnCOwhxN7kDSKMcG8m2kabiS870lcnzyDb55DLVLySoei6b3ZblzykT1Y1wxwpiwFmKDWmDi8SQLlGdRW6V3vyuA7BjMvKBhDdaXgD69IBmNBdoz6aSrwx1iX71hjqxhhb6tf7ARXv4HrzYjuIcu9yhh9dKhe0ljt9kjtBLUs79cBvd4R_co9mBIxOpzjkH7FWe5dl-nU8gA_5Zn7g_yKFGcxYGY5Ql2Q0wuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه شب هنگام بازگشت از نیویورک به واشنگتن، در گفتگو با خبرنگاران اعلام کرد که ایالات متحده به دستیابی به یک توافق بسیار خوب، محکم و قدرتمند با جمهوری اسلامی بسیار نزدیک شده است.
ترامپ با رد وجود هرگونه نقطه اختلاف بزرگ در مذاکرات، گفت: «اگر بخواهید حقیقت را بدانید، شانس خوبی داریم و باید بتوانیم ظرف یک ساعت توافق را نهایی کنیم.»
رئیس‌جمهوری آمریکا با ترجیح راهکار دیپلماتیک بر گزینه نظامی هشدار داد که بمباران ایران در مقطع کنونی، به قیمت جان انسان‌های بی‌شمار و بسته‌شدن چندماهه تنگه هرمز تمام خواهد شد و فرصت توافق را کاملا از بین می‌برد.
او با تاکید بر موفقیت راهبرد واشنگتن افزود: «سند امضاشده نهایی، کارسازتر از بمباران خواهد بود. ثابت شده که محاصره دریایی اهرم بسیار قدرتمندی است و بسیار قوی‌تر از بمباران عمل کرده است.» ترامپ در پایان اشاره کرد که ترکیب تهاجم اولیه و محاصره، ضربه سختی به اقتصاد ایران وارد کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76098" target="_blank">📅 17:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta6C1AhFROjynFropgZs9oidjj_ho5xYptgdJw5AEveRb9tCIpPe0EU2DkymfTAwwn_69gTAvuT0TzuKw9FOLuAg5ea9bAT1tU6E2HPz7BbIiZ1vh6Hc0mRTVm_dfV0k4qXwpx99r7a4ePl3huCoijs83CU2AnllGoYXUt13oyfheoGMLG0Vacrw5dgY5BYDKUo0fVpIy6AZpva3xRUBZBVLv7kLHPMf0tS5_WhU1gzElDxw8E_R21u9qvp8ovrrhgwnRd_m93ute_SlGjYprX_IrKrOC5yqsBXZnurMgghQH1b8TrOTZIJCHeEUQS624oXtco7TNVOHMsyQ7UEp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو عضو نیروی پدافند هوایی ارتش ایران در حمله دیروز اسرائیل کشته شدند
تاکنون در حملات دوشنبه و سه‌شنبه اسرائیل کشته‌ای گزارش نشده بود و ۱۵ زخمی اعلام شده بود.
ارتش اسرائیل دیروز گفت حمله «همه‌جانبه‌ای» به سامانه‌های پدافندی راهبردی ایران کرده است.
بنابر بیانیه‌ ارتش اسرائیل، در جنگ ۱۲ روزه پدافند ایران ضعیف شد اما بعد «سامانه‌های پدافندی در نقاط مختلف ایران» مستقر شدند تا توانشان را بازسازی کنند که در این حملات این سامانه‌ها منهدم شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76097" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHYNSaIK4Qi7SL7U8RPx134nvMMZMI9TYQ-rFfid9o7FAWCRhy464lZGl-dVZfSsu4z3JWPXLbZqFyMnGLuc0CrtKLckgpI-nUtDjJSLjRyMBJnJfCD1XHVvrWsJk1KMSuxiwmonGRVWyDLlwtDKZMBKYKcbB0aKp-y_vhroVIr1E0ZLh_lC9j2PlNf7lJ9d6vM-IgAGr6QuFRkISYDBg0p_rAMrTlQDyoxJ7JVo6S2-Lx0LPTZflCavhL4OFJR2yHYKYFZybGD5D1EQLopSeguWST-qlefNypAjfXsMrV-eKN2Q8v8KHL7wkDZrudo1eExB6wJDxvNz3MrffPhm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، در بیانیه‌ای اعلام کرد دو خدمه یک فروند بالگرد تهاجمی «ای‌اچ-۶۴ آپاچی» ارتش آمریکا که در نزدیکی سواحل عمان دچار سانحه شده بود، توسط نیروهای آمریکایی نجات یافته‌اند.
بر اساس بیانیه سنتکام، این حادثه ساعت ۷:۳۳ عصر به وقت شرق آمریکا در روز ۱۸ خرداد ۱۴۰۵ رخ داد. این بالگرد در زمان وقوع سانحه در حال گشت‌زنی بر فراز آب‌های منطقه بود.
سنتکام اعلام کرد دو نظامی حاضر در این بالگرد ظرف حدود دو ساعت نجات یافتند و در وضعیت پایدار قرار دارند. این نهاد همچنین افزود که علت وقوع حادثه همچنان تحت بررسی است.
یک مقام آمریکایی به شبکه ای‌بی‌سی گفت دو خلبان این بالگرد پس از سقوط در آب، توسط یک شناور سطحی بدون سرنشین یا پهپاد دریایی از آب گرفته شده و به خشکی منتقل شدند.
به گفته این مقام، پهپاد دریایی مورد استفاده در این عملیات طراحی مشابه یک قایق تندرو داشته است.
@
VahidHeadline
هنوز مشخص نیست که آیا این هلیکوپتر بر اثر آتش نیروهای ایرانی سرنگون شده، دچار نقص فنی شده یا با مشکل دیگری مواجه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76096" target="_blank">📅 17:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76092">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EgNZVczGrfeD0pGCHJgXFYtaMwvri-F9fyjY_DBzUBW6AkGnKaNCaAoh3kQEAR3QSqbxqrzKE_wQT0bsv01pn20eTrBC--hTM70EoKWtr04FzfZMIy1UDNQCqmOizcf9PdDVZZxVfjoqK1BTzQnqkrA8OhkdVeQ06Px77xoQg37gcYKS7-IUCPwPrIbOtQniAXQ4TOrZD71WQq6kldi2ifXRQp42agGkcaIXafU62SKZ9WyQjoQaA_jQ6Y70ed_4r5P9daSbPV0c9AVcR7Zl-twfVcbQoM_n_eJs-hiQAtwNAbuC64afKtXUmBTJf8nvzZzTSLX2xhnE2VHtqjFwRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NJopRTIHM8loYB5NmG2fpyZsqZBPYthexAkDkBkYJc97VkHmTa3zlbjZrmeNdJ4FZe3dgAT2gVdCA0iA7NChi4EKD5uVdOQuGiFOy5TLThEOEYsdb0N5ifaKW99c-rRKpzFhH1GiIv_Kh6zKKkKetRaBVWjZ41SYFW7D1B48HFjORUjkvS6pWyOEiDW6v54Llx6HjPhAo-8kf8oC_V94Ql6Bgwh6KZjTnJqQ3mqn43VkgP5PX1DvlcIGRYeQSmXW0PS1JVTIAhDOj46TIlmOjCT9B839qImAd8mPMIysAUOah8AEqagk_9Q_fMP7qcBTWL5vl_La0mcxQTOPa3GDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NYA516Uk9VuL3_XnK-PcZzNmHr4j6zS0cH5DO87shj0Zvy6shgOPAQMOfmwJ8k8Lk2TszbenGhcXLiviNRp9samwIfs2Z1fZWVokF381oErqr4MyIpLtK6pwIp0eeDUcK3iT4xihv1Ifaucf3hSDwXGR-KkbQ9_J1yYRLzv-B_5SFXxN7p8CF29Ux-n3VPr9bePbHMyefPNMMqMj06kE5AzEslrUi_gqMuVlCk_NWNKZzbxxHe4A33kBSUw5hRyCD6r5fjHfE_cFJi6xc9EEqqUsNJFykJkZFJkJuBNY0iE4KesI2aBg91VztXV2uLRSEEIOqptLQAyMHvyNf_nMRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8642136842.mp4?token=G0tk89foMeuO5C7y6M-t8rPsNBrJZph3eZC4EoJykS1xbh4bb0Zir4OdirzJvj_JbitocxIpUsEJKgyWjh0qiHVpD8dV3G0Nmx3-etcbGtnCY260JBXIbHlEjOQvagiZZHtpmu83lKyoplXUF4xLcBXMyuWgjFfDfOtI3--1INDe0KvVdUv8rt94b8fg4htapiaRRkpYJMJKBV-784FzpA2JQA8i8Fakvf_Pl8R2jWPRcaVCKIFpcw8VqQyOgVk2i_R9ex6TNRJX1laLe84Qb9-bQpT140LBqUjKQA7YIV0O-B55AccCFAc7r6eMskjWASSs2dgZq9kpeEoE5bTIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8642136842.mp4?token=G0tk89foMeuO5C7y6M-t8rPsNBrJZph3eZC4EoJykS1xbh4bb0Zir4OdirzJvj_JbitocxIpUsEJKgyWjh0qiHVpD8dV3G0Nmx3-etcbGtnCY260JBXIbHlEjOQvagiZZHtpmu83lKyoplXUF4xLcBXMyuWgjFfDfOtI3--1INDe0KvVdUv8rt94b8fg4htapiaRRkpYJMJKBV-784FzpA2JQA8i8Fakvf_Pl8R2jWPRcaVCKIFpcw8VqQyOgVk2i_R9ex6TNRJX1laLe84Qb9-bQpT140LBqUjKQA7YIV0O-B55AccCFAc7r6eMskjWASSs2dgZq9kpeEoE5bTIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از برقراری تدریجی دسترسی به اینترنت در ایران، ویدیویی در شبکه‌های اجتماعی منتشر شده است که فرزند جاویدنام نسترن زارع‌منش را در حالی نشان می‌دهد که پشت پیانو نشسته و هم‌زمان با نواختن ملودی، یاد مادرش را گرامی می‌دارد.
نسترن زارع‌منش، ۳۹ ساله و مادر دو فرزند ۱۰ و ۱۵ ساله، ساکن تهران بود که ۱۸ دی ۱۴۰۴ در جریان انقلاب ملی با شلیک گلوله نیروهای سرکوبگر جمهوری اسلامی به سینه و گلو جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76092" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76091">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PrfAT11O5ozS61N8kEYAHnvDNbIxv_-hKesRf-KQHxgAFprPI4wwllULLB9-iMCHiDMvgJ-8ndyyerbNkhPiimmYWaMUBNauiqIdbpENsh91X_8QiAoFMfFxtFIpCvr61B31pHoT_cQZUaSKuMlg6CEqJhgBE658r32FOCLL1v0c_5UceMk09MMDWVHr03UF6-Oj6jZJeR5idhLCFjodZwMzoLiS6pvFscO1Vb0dctoe4QtTDfJt5ZBHYkVa5a6yE9XQjP3e2LevNMjb5Rz9FzK0Iy8ULFMIdd0PPTQ7cpn3VVDjJkpsGgvTdjywfKpHPaAamf1ptP6ma0YBQvY5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون ترامپ، در مصاحبه با فاکس‌نیوز ابراز اطمینان کرد آمریکا و جمهوری اسلامی می‌توانند درباره پرونده هسته‌ای به یک توافق بلندمدت برسند.
او گفت صرف‌نظر از اینکه اسرائیل از این موضوع خوشش بیاید یا نه، چنین توافقی به نفع آمریکا است و واشینگتن به پیگیری آن ادامه می‌دهد.
ونس با اشاره به نگرانی درباره اینکه تهران ممکن است در حال بازی دادن واشینگتن باشد، گفت: یکی از مهم‌ترین عوامل موفقیت این توافق نهایی این نیست که جمهوری اسلامی چه چیزی روی کاغذ می‌نویسد، بلکه این است که آیا واقعا به برخی از الزامات توافقی که به آن می‌رسیم پایبند می‌ماند یا نه.
او با تاکید بر اینکه آمریکا تعهد جمهوری اسلامی به چنین توافقی را در بلندمدت راستی‌آزمایی خواهد کرد، گفت
:
بیایید صادق باشیم. ایرانی‌ها نمی‌خواهند این جنگ ادامه پیدا کند. ادامه جنگ به نفع آن‌ها نیست. آن‌ها پای میز مذاکره آمده‌اند و پیشنهادهای واقعی را مطرح می‌کنند. اگر به این توافق برسیم، یک موفقیت بزرگ برای مردم آمریکا خواهد بود.
@
VahidOOnLine
جی دی ونس در گفتگو با شبکه فاکس نیوز: موضع رییس‌جمهوری کاملا روشن بوده است. اسرائیل اهداف خاص خود را دارد، اما هدف اصلی آمریکا در قبال ایران این است که اطمینان حاصل شود ایران به سلاح هسته‌ای دست پیدا نمی‌کند
جی دی ونس: در ماه‌های گذشته و در واقع طی حدود یک سال و نیم اخیر، شرایطی ایجاد شده که رییس‌جمهوری معتقد است ــ و من هم فکر می‌کنم درست می‌گوید ــ می‌توان به یک راه‌حل بلندمدت برای مسئله هسته‌ای ایران دست یافت
ونس: ممکن است اسرائیل از چنین توافقی خوشش بیاید یا خوشش نیاید، اما ما معتقدیم این مسیر به نفع ایالات متحده آمریکا است.
به همین دلیل به دنبال آن خواهیم رفت، زیرا این همان چیزی است که رییس‌جمهوری آمریکا برای انجام آن انتخاب شده و همان کاری است که برای خدمت به مردم آمریکا باید انجام دهیم
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/76091" target="_blank">📅 06:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76090">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yor7IqOMJ2fv1g47pN5Pl8xiw-Ch_7QbKQa8CIe5nDb1rHUeLTDcjc1Tba6VQslDDiiqL4ETuPDd3NuKy_mz0m0Owf8-psiDts9OIBru_DM96vsWUuPS-aN8L_XwR8mimuxNy3Ff_riguJFSDc-W8hld1lysErCOU0tfqhvadlm4uifNTJpVbqOjMhPNf80K5-5K0d8IqJPIJsnBd6ee6ogBpjX1KZuv7h5BySLD8ks-_CfgyMeJSmQ7vyx7tkqunXgdYreLabGfEmNU0xfaBcNjQWXe2A2oC_dK-7BPMR6hfXgkZNLGC6MAicisCz4_yHgYBEI_4S2UJLaESBs1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه با تاکید بر موضع سرسختانه واشنگتن در قبال برنامه‌های هسته‌ای تهران، با تقدیر از همراهی لیندزی گراهام، سناتور برجسته آمریکایی گفت:
«لیندزی در تمام این مسیر پابه‌پای من جنگیده و ما تیم بسیار سرسختی بوده‌ایم. من فکر می‌کنم در حال پیروز شدن در این نبرد هستیم، اما طی دو هفته آینده با اعلام پیروزی کامل، برنده واقعی آن خواهیم شد. این یک پیروزی کامل خواهد بود که بسیار زود رخ خواهد داد.»
رئیس‌جمهوری آمریکا در ادامه با اشاره به نابودی گسترده زیرساخت‌های نظامی ایران، این وضعیت را مصداق تحقق «صلح از طریق اقتدار» دانست و خاطرنشان کرد:
«ما در حال حاضر مشغول مذاکره هستیم و آن‌ها به شدت می‌خواهند یک توافق بسیار خوب انجام دهند. آن‌ها اکنون حاضرند همه‌چیز را به ما واگذار کنند و توافق کنند که ایران هیچ سلاح هسته‌ای نداشته باشد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76090" target="_blank">📅 02:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-yy9ad6XtWKjSoyfy1WfJ2K45npBR1POHFIXHA_aNv4dF9BeaGDYGYqVcOTC15uK4TVCvo50OHYoargqBC-kVXHsPCYhm1wV0kGbdsxgMoIKSFl8QNg2-tp3m9UeboecxkDuCaRQQ2jXYM5hsr40pym3kLWSSBwwDCe3a-V5niQlxvFvmCOekSkA304Z6o58veYub6-qeD31wJXv6tsSgxCFd1OwCGJGfsYOvVcCJTy1ffjj7qQX3mbtb8DZofoYOirrr1mcEOzPb4ci-5f0ggEH0wnNjgqSTcaT6TxmmDK40Yn62RUdywXrxavMM5HBgIZsHhmPuxBe2icZ0g0rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران در اظهاراتی جدید به حمله موشکی شب گذشته از خاک یمن به سوی اسرائیل واکنش نشان داده و آن را نشانه‌ای آنچه «هوشمندی جبهه مقاومت» خوانده، دانسته است.
آقای قاآنی روز دوشنبه گفت: «اقدام به موقع و با اقتدار یمن قهرمان نشان از هوشمندی جبهه مقاومت دارد اگر لازم شد دیگران نیز می‌آیند. شرارت‌های رژیم صهیونی و آمریکا در این منطقه عکس‌العمل جبهه متحد مقاومت را در پی خواهد داشت. رزمندگان بدون مرز مشرف برگلوگاههای عبور شما هستند به تعرض ادامه دهید گلوی شما را خواهند گرفت.»
یکشنبه شب ارتش اسرائیل اعلام کرد که پرتاب یک موشک از خاک یمن به سوی اسرائیل را رصد کرده و کمی بعد از رهگیری آن خبر داد.
کمی بعد حوثی‌های یمن حمله به اسرائیل را تایید کردند و گفتند که «منطقه اشغالی یافا» را هدف قرار داده‌اند.
حوثی‌ها همچنین در بیانیه‌ای «ممنوعیت کامل و مطلق» تردد دریایی اسرائیل در دریای سرخ را اعلام کردند:
«ما در قبال محاصره ناعادلانه تحمیل‌شده بر مردم خود و مردم محور جهاد و مقاومت در فلسطین، غزه، ایران، لبنان و عراق ساکت نخواهیم نشست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76089" target="_blank">📅 02:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76088">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a40e8ba.mp4?token=pX0q9EEHg5NjFj3ZlcFdByRN7GSiV_y8JkBnu391_lsN3uVgcUoOTFb4ia1Ia-e9Ohox6COGPbkIOujPvyrKmWZp0REJ0oQrMT14qaEiPKnE34GhDR2yzU-5awwbz7TWjatlspePFFOlVbrTpaGxmz7OnMqKgOtuEXpjM56I99iftl0s1VnKKsYnlQfQ_FsrJ9JPZ6ewkqRTkFJw7Uk_-cXCNPctonW7Gp7apRY6gGNrxPq_Gzdu85mqiIynJcA5ps76d_gK3g3Bukyo47IBblXS47d4UXDi2YQaz6wsV4to9grez1aRbehWIGxD3LLgKgsA6LjRwkUAzwVDGYekPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a40e8ba.mp4?token=pX0q9EEHg5NjFj3ZlcFdByRN7GSiV_y8JkBnu391_lsN3uVgcUoOTFb4ia1Ia-e9Ohox6COGPbkIOujPvyrKmWZp0REJ0oQrMT14qaEiPKnE34GhDR2yzU-5awwbz7TWjatlspePFFOlVbrTpaGxmz7OnMqKgOtuEXpjM56I99iftl0s1VnKKsYnlQfQ_FsrJ9JPZ6ewkqRTkFJw7Uk_-cXCNPctonW7Gp7apRY6gGNrxPq_Gzdu85mqiIynJcA5ps76d_gK3g3Bukyo47IBblXS47d4UXDi2YQaz6wsV4to9grez1aRbehWIGxD3LLgKgsA6LjRwkUAzwVDGYekPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسی حکومتی در صداوسیمای جمهوری اسلامی مدعی شد آمریکا در جنگ ۴۰روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته است.
او گفت: «برای ما کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها هیچ کاری ندارد» و افزود جمهوری اسلامی به درخواست «عالمانه و عاجزانه» کشورهای منطقه خویشتن‌داری کرده است.
پیش‌تر، دونالد ترامپ، ریس‌جمهوری آمریکا، چهارم خرداد در مراسم «روز یادبود»، یاد ۱۳ نظامی آمریکایی کشته‌شده در جریان جنگ ایران را گرامی داشت و گفت آن‌ها جان خود را فدا کردند تا اطمینان حاصل شود که ایران «هرگز به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
"روایت فتح"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76088" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76087">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">زمین‌لرزه در هرمزگان
پیام‌های دریافتی:
سلام وحید جان
زلزله همین الان بندر عباس ساعت ۱۲:۴۰
آقا وحید بندرعباس همین الان زلزله اومد
قشنگ زمین لرزید
00.39 بندرعباس زلزله شد
زمین لرزه نسبتا شدید ساعت ٣٩ دقیقه بامداد بندرعباس
داداش همین الان بندرعباس زلزله‌ اومد
🔄
آپدیت:
‌
خبرگزاری فارس: زلزله‌ای به بزرگی ۵ و در عمق ۲۲ کیلومتری زمین، منطقۀ سرگزی احمدی در شمال هرمزگان را لرزاند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76087" target="_blank">📅 00:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76086">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPscJAwfqru5w-ClTr0RY1Ngdh5j0q9KVS7tvNtI-_48eH_YOz1qR53-vu8pBrUW86ZQA2Zy531TTFolNT_W4emY_rYDxC3gvTVGva2pHBPXUndCkfuaGrkpS_HLslXCWVFh-IyOB3bdVUMRDErXULnUKPoufGnftHsBEzn1m3a9OySxQw6ZV_pdqIOpTAE9ikYBsb8z-isde6IrFS57FhEvaJYvGP_UetTizHtQmQWZlL6W714YC9NgFpsGUyA9X9kmBSKVuyNEfPzPxcn4RawMLcHu2ude5gT_L1dsNrZ9AJoY1qWSWhUq5q6RUp24em_ven1rkpvLdDTZi09aiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سارا اسمیت، سردبیر بخش آمریکای شمالی بی‌بی‌سی، در یک تماس تلفنی کوتاه با دونالد ترامپ درباره گفت و گوی تلفنی روز گذشته او با بنیامین نتانیاهو، نخست وزیر اسرائیل، پرسید.
وقتی از آقای ترامپ سؤال شد که آیا نتانیاهو با حمله موشکی به ایران در روز یکشنبه از درخواست او سرپیچی کرده است، رئیس‌جمهور آمریکا این موضوع را رد کرد و گفت: «نه، نه. موشک‌ها از قبل شلیک شده بودند. آن‌ها از قبل در راه بودند.»
او سپس افزود: «اگر به او بگویم کاری انجام دهد، انجام می‌دهد.»
این تماس کمتر از یک دقیقه طول کشید.
در بخش دیگری، سارا اسمیت از آقای ترامپ پرسید که برای متوقف کردن حملات اسرائیل به ایران به نتانیاهو چه گفته است.
«تنها چیزی که گفتم این بود که باید از عقل و منطق استفاده کنیم. ما به امضای یک توافق بسیار قدرتمند و بسیار خوب نزدیک هستیم. بدون سلاح هسته‌ای، بدون هیچ چیز دیگر.»
او ادامه داد: «می‌دانید، باید از مقدار زیادی عقل سلیم استفاده کنیم. همه چیز خوب بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76086" target="_blank">📅 00:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
وحید جان گیشا یه جارو زدن یه انفجار وحشتناک بود
[از روی صدای یک انفجار چطور میشه تشخیص داد که دلیلش حمله بوده یا چی؟]
وحید جان ۱۲ و ۱ دقیقه صدای انفجار خیلی خیلیییی بزرگ
گیشا
سلام از گیشا
یه صدای خیلی بلند انفجار اومد
همین ده دقیقه پیش
همه ی همسایه ها اومدن دم پنجره
نمی‌دونم چی بود خیلی عجیب بود
همه جا لرزید
📡
@VahidOnline
۲۰ دقیقه صبر کردم ولی پیام‌های زیادی دریافت نکردم.
آپدیت:
ما وسط گیشاییم و خونه هم ساکته، کوچیکترین صدایی نیومده
وحید جان راست میگن دقیقا ۱۲ و یک دقیقه در گیشا صدای انفجار بزرگ اومد،اما فقط یکی و واقعا نمیدونم چی بود، ضمنا برخورد به زمین و یا عمیق نبود.
من گیشا زندگی میکنم ، با اینکه امروز ظهر هم گفتند یک جا یک جای گیشا را زدند متوجه نشدم
حتی الان هم که پیام گذاشتی داشتم می‌خوندم اما متوجه انفجاری نشدم
من گیشا هستم چیزی نشنیدم
آپدیت:
بعدش کلی پیام دیگر هم در تایید و تکذیب شنیده شدن صدا دریافت کردم ولی چون بعد از انتشار پست بودند نمیشه خیلی روشون حساب کرد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76085" target="_blank">📅 00:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzsmHCTqI_E865F8mn33D19NlBtDp-xHXfhdAaEw4tPCqr9_DfMzuHRjZkZsVlm_3xGhNgrTfMMuqhXyVMlqyWY7Kqm9FDJz6g1XmiD9xh59-elC-GNLkqYZJzuzpAPTCmKCpsoQfoZ4Zm0HZ7reLaop7_Jc0B9Lft1G53ntkQSyuycu-icp_Lq9-bLk_3-NHDh5Ea5OHYLpvZqey-OKkgCDYFXQJtbSgQeEWtHLXU3SHoWCMG1_fZmQ39YK5BEyUZ9SSeTNrMkLhVqpam7iVLvG0tiZeiQklNKACN1IaIzHeMcFgM-bY221miiNBit3V-mzmlLiVXV9jFRga82U3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبری سی‌بی‌اس، روز دوشنبه ۱۸ خرداد ماه گزارش داد، دولت دونالد ترامپ قصد دارد روند لغو تابعیت ۱۷ شهروند آمریکایی را که به تقلب در پرونده‌های مهاجرتی یا برخی جرایم متهم هستند، آغاز کند.
بر اساس این گزارش، وزارت دادگستری آمریکا این افراد را به پنهان کردن اطلاعات مهم، ارائه اطلاعات نادرست در روند دریافت تابعیت یا ارتکاب جرایم مختلف متهم کرده است.
سی‌بی‌اس نوشت این اقدام بخشی از کارزار گسترده دولت ترامپ برای استفاده از سازوکار قانونی سلب تابعیت از افرادی است که به گفته مقام‌های آمریکایی، شهروندی این کشور را از طریق تقلب یا پنهان‌کاری به دست آورده‌اند.
در میان افرادی که هدف این اقدام قرار گرفته‌اند، نام چند نفر که به جرایمی از جمله سوءاستفاده جنسی از کودکان، کلاهبرداری مالی، پولشویی، تقلب مهاجرتی و استفاده از هویت‌های جعلی متهم یا محکوم شده‌اند، دیده می‌شود.
تاد بلانش، معاون دادستان کل آمریکا، گفت دولت در برابر سوءاستفاده از روند دریافت تابعیت «هیچ‌گونه مدارا» نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76084" target="_blank">📅 23:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ02TdcB8M8b4g5eKebKtUbHBtkk5cpO5_nSnSNd42pymJtlTWimLbauGK2wIPoHkSy16_P3IlxbPSKsBu3kUED4kw1o5aoad3cDjuAnT5IUUlarPw2jSAUxfI-wlUF7B-6FnY-eu2yjdI23Al8cgoJopqhOxP2kii_XBdiOpMQLXzQd83qpahKCl3Bm8_gh9Mb5ireOteWsNr_1sZSiIaRnZqr3bj14d7xGFHAZPkZ2FxjZfjzCJjo9HEKnvnfspNfkxsxH511XRr_rM2N5RGOsyXvLIR5rQfBklQOPz9KnC98N-7wp8s0dO6RYAnAs8_TBGVtllZBT1Jy6-3JV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری سی‌ان‌ان، شامگاه دوشنبه ۱۸ خرداد ماه، به نقل از یک منبع اسرائیلی و یک مقام آمریکایی آگاه گزارش کرد اسرائیل در حال آماده شدن برای حمله‌ای گسترده به تهران بود، اما دونالد ترامپ، رئیس‌جمهوری آمریکا، در تماس تلفنی با بنیامین نتانیاهو از او خواست از انجام حملات تلافی‌جویانه بیشتر خودداری کند.
به گفته منبع اسرائیلی، ترامپ در این تماس از نتانیاهو خواست دامنه واکنش اسرائیل را محدود کند تا از تشدید تنش‌ها جلوگیری شود.
بر اساس این گزارش، نتانیاهو در نخستین تماس که شامگاه یکشنبه به وقت آمریکا انجام شد، در برابر درخواست ترامپ مقاومت کرد و اصرار داشت اسرائیل باید به حملات ایران پاسخ دهد.
با وجود اخطار ترامپ در گفتگوی یکشنبه شب، ارتش اسرائیل برخی اهداف را در ایران، از جمله یک مجتمع مهم پتروشیمی، هدف قرار داد.
این شبکه همچنین نوشت لحن گفتگوهای اخیر ترامپ و نتانیاهو به اندازه تماس‌های هفته گذشته تند نبوده است. به گزارش سی‌ان‌ان، در تماس‌های هفته گذشته تنش میان دو طرف به حدی رسیده بود که ترامپ با الفاظ تندی با نخست‌وزیر اسرائیل صحبت کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76083" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qttqmcMHp5CH9q2W6b36PtAB37SKQPJaG-IGwkf6HafJsIIpyP9CEJMZA02f4bWbKCxxScSsU9Ks7jah85ArTbmNYACnb3a324oTDs61zjwpLsItIW14FLL6KysbGzT-MIhfxFrj6X5ebgSuAbrJFtq1yusyA9P0Ks66h7uhkmyaavIvPAiuIca-dsDZ4bFAf9x80U1evaQ_cCI6mPXOB3TrXTpQsktdePWwwTa7hHvQINkdqiA1mIepMsLqFUdXLZCkyKYHXgKu9voJ2fhy7iSQnYF4E7Naj8EzMGBEv1EK_DlDBVyKJ43YdkPHmRnEvN72dI0zfehr0uHUvfS6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان، درباره حملات موشکی اخیر جمهوری اسلامی به اسرائیل نوشت که دشمن در کوتاه‌ترین زمان ممکن ناچار به التماس مجدد برای پذیرش توقف آتش از سوی تهران شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76082" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r6Szcm9XDNJuZcaYFPalESyyltbeMEy5p7czzEEXCTo_xUVIq57hA-sqh3NNIZqmMXL-bBrCYmntLiWDzJ8-CqjaMIEgAP5GadgRoBfqHY5nO7iZEgDcknouOS0kWQYAipr_1SfmIpeum2dUKMYMUUEtAqYcHJfiZ1RJ0JvIEFTDhEh9QAVCeA5v0FSWG1LoVtOw6riNd6dq5u5A-WE6wrQTpEPRqN7esd8eVDXg-d_2nfrncdmYTf-u5F-DFxIIzPZkcvd2CdOCl_XdjRqZv6MLOWN9rLA6RU8dWYHlS6u4MMe_fVQrCYOK2Wg3tafYVzuC7cYYHLUhALK2s3NaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kAiAVanRo-lOrASSmvA6DOEdLUIO1hH4Nj7I5nYNlsyanLM1PJgkO-98EMU8zZMDzSP-GpwBum4rEWLJhHODWoZ-bseKylMiHivrVsqvd_nfDPwVYn7Xp9_z2sbDvrZZ9CiT8Po8Btr_HI6-vzqqZ4Q4c5LO-OAberd8VAgc9LLT3oiBu7Hj7xR7nr761XrkzuJdBSDz8ue2X7IEWdHVZmUvGEJffuwk09fSIsmN8-eEK5rW7KV6gUOb-ttNAgGGp0AIxhBnsznV8Al0NgHiuWnpiE7pXgvq_iwPUu7tPrPxTijzSWmTrZLDIcrMKD8gbbhCIC6ZCA0cRRxG6-Ztqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ گفت: «به بی‌بی گفتم خیلی مراقب باش چه کار می‌کنی، چون ممکن است خیلی زود در برابر ایران تنها بمانی».
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز دوشنبه در گفتگو با کانال ۱۲ تلویزیون اسرائیل اعلام کرد توانسته دامنه حمله اسرائیل به ایران را محدود کند و بنیامین نتانیاهو را برای کاهش تنش‌ها تحت فشار قرار داده است.
ترامپ گفت: «من موفق شدم شدت حمله اسرائیل به ایران را کاهش دهم.»
او همچنین افزود شماری از کشورهای منطقه از او خواسته‌اند بر نتانیاهو فشار بیاورد تا از تشدید درگیری‌ها جلوگیری شود.
رئیس‌جمهوری آمریکا در ادامه گفت در مورد حمله به ایران به نخست‌وزیر اسرائیل هشدار داده است: «به نتانیاهو گفتم خودت را در برابر ایران تنها خواهی یافت.»
ترامپ همچنین گفت نتانیاهو «با تاخیر مرا در جریان حمله به ایران قرار داد، اما من موفق شدم این حمله را کاهش دهم.»
کانال ۱۲ تلویزیون اسرائیل عصر دوشنبه ۱۸ خردادماه به نقل از یک مقام رسمی دولت نتانیاهو اعلام کرده بود اسرائیل حملات به ایران را به درخواست دونالد ترامپ متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76080" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XWWvh9NtvEr0rL3P4f54GmYTI4K9NKg5btGxlPb-0iBkas2bbIlIVS3VeOkRvkw4Sn6c_rtcCrva2EjYz4dv39gDIQrxYh3-StKx-r8xO1RpILOVqzivnG1_rc-ygiJYEMY483L5TRI0yYtVS2oBcEb_vcVh1c8aBkogIaoLt0ScBGJIGLrdmwd4rGQVqiSq0Qa0O26kHARkLT_wEVD093kKwQxE5pXtZqawIMYkhIBwCbMIBBaLCEi1FLwVpybUB6IRTyuRdSAF_MSo6P8DvRbmtrLc3ioHi6i8BnOXKqIFJ4QQcpBPy9UgdiWrfdWF4f9aDmp8XPqcFk7Hv5GBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: نیروهای آمریکا نفتکشِ متخلف را در خلیج عمان از حرکت بازداشتند
پست اکانت فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
تامپا، فلوریدا — نیروهای آمریکایی روز ۸ ژوئن یک نفتکشِ بدون بار را در خلیج عمان از کار انداختند؛ پس از آن‌که این کشتی با تلاش برای حرکت به‌سوی یک بندر ایرانی، محاصره جاری علیه ایران را نقض کرد.
فرماندهی مرکزی ایالات متحده، سنتکام، نفتکش
M/T Marivex
با پرچم پالائو را هنگامی که در آب‌های بین‌المللی خلیج عمان به‌سوی ایران در حرکت بود، از کار انداخت. یک جنگنده
F/A-18 سوپر هورنت
از ناو
USS Abraham Lincoln (CVN 72)
پس از آن‌که خدمه کشتی از اجرای دستورهای نیروهای آمریکایی سر باز زدند، یک مهمات دقیق‌زن را به بخش‌های مهندسی و هدایت کشتی شلیک کرد. کشتی Marivex دیگر به‌سوی ایران حرکت نمی‌کند.
از زمان آغاز محاصره در ۱۳ آوریل، نیروهای سنتکام هفت کشتیِ متخلف را از کار انداخته‌اند، ۱۳۴ کشتیِ فرمان‌بردار را به مسیر دیگری هدایت کرده‌اند و اجازه عبور به ۴۲ کشتیِ حامل کمک‌های بشردوستانه داده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76079" target="_blank">📅 20:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgSm2lweuGNn81SikrMmbRD6PIVBrj1B_An4UvTAEkqu75KCmAr5-LR8zWkDcE68_rYtNba2oo6PC7nnqfChmSX544K0Ey6gGcIX_atiRuWWci2FwRwAl7MeNuK_YLJz1_UIaWr6Rc2sNODaRwYVeop9Q-pRBWfjRXUy_PFWj3Vt-kc5GnvfAuxH74mMqn09xEPqdwf37GoDisLiJinPOAGNxo8t3Ii2vXWpflSk7Q6g6-FhOvJqBZF4gj1_m2byAWyZ6Nr9cZqtk78IaMvd9AeV5rBoUtp8mq3WWTE_tOwEhncoRR9AJQRrrbDaxeI-l4nIotiHHVHMR5vtb4uc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.  به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.   اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع…</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/76078" target="_blank">📅 19:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lY2i4oP1tZj91nryditD6L8LEebJkX8dnBNaMkoTeDyR6b2EHax2TAzjiq0pycayG1pI9ZqZNMFcZs8zXESsJTnjxCVPaISpGosvq8XvkTOEY5ktKbJYXc3CXRbXJNBZ3diFpJA9DWuK-NEEqR-tEtJCFM3-8MXP0cb35dUKgzjrGntF-D-iHHBguvA7eu5eQt44_QZ9f8gD6Om3JwvQCZn4r_JvbdD7C8nw8BVeA1UTkQGhZ5_ai1cp2GYANpokttCdeVDcG0oqLsOuGI9YpJQTIiH2VywErbtXn48Da6OCokGl4J6OhW6IRpHg-52KZOJWwcGLksccsE0haF7sTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران وضعیت پرواز‌ها به حالت عادی برگشته است
سازمان هواپیمایی کشوری ایران عصر دوشنبه اعلام کرد که فضای هوایی کشور به شرایط عادی بازگشته و عملیات هوانوردی مطابق با اطلاعیه‌های هوانوردی (نوتام)، از سر گرفته خواهد شد.
ایران ساعاتی پیشتر گفته بود که تمام پروازها از فرودگاه‌های کشور لغو شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76077" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oB4fN1RTXLUxlsJbiJzU6ny0UOTC3z58ExhpzT2whZD8ZuO7J5HlfkjxF0tFSDVtB5iC0ZezGzFLMUjfBSVVkBjGWWWYGnUP3X1HCO970FVX6VVgfnXTsrJjV-myDzLkU1Hw0JQfRjHDhKr5OW0tqS-76NKG_LLTSuM07unLxcdwGxn4ainZjoMA2sNbpYgCYTf3ODyhtf1D4zNlZltLl_-y8m1VEU_BTDVsVKrxsvt79MK_1m9HuygMjA6rTrnpQm7KNSDnYSPVg4s2bcc0WK8RBguXEBV8pZQD9aBW60SPAKQ_4-bd9PTcT0p4bPr302YDloIfRsrjHA-Yh9bt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد یک موشک بالستیک که از یمن شلیک شده بود، در منطقه‌ای خالی از سکنه در نزدیکی مرزهای عربستان سعودی و یمن سقوط کرد.
به گزارش رویترز، وزارت دفاع عربستان سعودی اعلام کرد این موشک به سمت یکی از کشورهای منطقه در حرکت بود.
همزمان حوثی‌های یمن، تحت حمایت جمهوری‌ اسلامی، اعلام کردند دوشنبه یک حمله موشکی به منطقه یافا در اسرائیل انجام داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76076" target="_blank">📅 19:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYKZwl0pTk0WGwLmtdHqHYnrSmEr6sf21EOddbefU7zGpgP8BVEFOWGPpK3ssI5Y1YZRJY-dt0kqIgZ0GS3qmVTG9htmz8Ow_qWsW5OQ7iIdKNtaU9iMk9E1ejoWrBl7Z7iPvGhoXVnNnrl5f0SpPb5oP0Ni22R9W_vu5j84tCZ0Jw7oDjqW8FCstaN9xF-H9AU4tvRkBhkpQY-Gxdqd_BMoJQnRb-qQ2n4u8MlMeWIPGfYKEHRAfx3-GD2P4xYPEpswgopVaaV51xwNHA2xyzd_5XK91V7Y3bERhsAgeWz_lgvz56eAsbBsQVFycbc7TftbB4EqhNqXEK0pdjHubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اظهارات مطرح‌شده از سوی ارتش اسراییل مبنی بر مشارکت ایالات متحده در رهگیری موشک‌های بالستیک شلیک‌شده از جمهوری اسلامی به سوی اسراییل را رد کرد.
به گزارش سی‌ان‌ان، این مقام آمریکایی گفت ارتش ایالات متحده هیچ‌یک از موشک‌های ایرانی که بامداد دوشنبه به سمت اسراییل شلیک شدند را رهگیری نکرده است.
این موضع‌گیری در حالی مطرح می‌شود که در دورهای پیشین درگیری میان ایران و اسراییل، آمریکا با استفاده از سامانه‌های دفاعی خود در رهگیری برخی موشک‌های شلیک‌شده به سوی اسراییل مشارکت داشت.
@
VahidHeadline
نباید اینجوری نگاه کرد که تعداد موشک‌ها چقدر بوده و نیاز به کمک داشتند یا نه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76075" target="_blank">📅 19:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76073">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aB3m9UE0yHfbD3vQ89rRwrNG1xGexc28Z_G3X9eGpWCkQagIvZLWXxBCn9zC8TOH3WKY3CFLQ7dm-ddrnY_1HZ6xX3brR2c2mezSAqQSNxa8BDzkkysUwy_DaHl3WOngmt_L3rHSAxJvNFrROYBqI9xyN-ieEnsYFPXd9gS8CZCahkVDpWqxhATMDmLLmaI42Vn0IJepvjG2QLX_ZfAWBi95CEU4A_U9Bv3-1Z08onY5BbKF_agIAKmPyMKmGzQSs3xBhYryJIjkIMeBAX69rObXUy_HDCfcHgmI3L4Ltv_XQ55oSbgpiAnV7dN_ni2ZzXfoC3Ho7JB2H_NYpXPU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fca0bb1962.mp4?token=k4uQO_FCz2TlUKLvUvF7KTleHDByhdbfn9wafm2HCttTyGSGnPLmcZoSWbQp6NaBO9V1ejYgaQtG_zmkgna3DMEbX9amsf4sOckp8wE-Q7ndyTcs5vHkDp83FYmer-22I8wcetZ5ZT7UVZoL-uQy3UVR1iCQHwmo5418PorB9pe_TmmOvMnEZjBN5St-fH6HlyhcOlfnVLYWJ3fENLlIFgVhoXfnKeYAWB76s-EWnscLwsqI5Rehtmo6KiYDAgWr-F6pQnDOIc6wdPCuAS3h-eU9S-EeKNfg-nouYqJ27_L2NJGMf1wyIj7hCFnlXuGNf6vd8LePtqNBc4pUO4JAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fca0bb1962.mp4?token=k4uQO_FCz2TlUKLvUvF7KTleHDByhdbfn9wafm2HCttTyGSGnPLmcZoSWbQp6NaBO9V1ejYgaQtG_zmkgna3DMEbX9amsf4sOckp8wE-Q7ndyTcs5vHkDp83FYmer-22I8wcetZ5ZT7UVZoL-uQy3UVR1iCQHwmo5418PorB9pe_TmmOvMnEZjBN5St-fH6HlyhcOlfnVLYWJ3fENLlIFgVhoXfnKeYAWB76s-EWnscLwsqI5Rehtmo6KiYDAgWr-F6pQnDOIc6wdPCuAS3h-eU9S-EeKNfg-nouYqJ27_L2NJGMf1wyIj7hCFnlXuGNf6vd8LePtqNBc4pUO4JAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل روز دوشنبه ۱۸ خرداد با اشاره به توقف حملات متقابل اسرائیل و ایران گفت «آتشباری متوقف شده اما اگر رژیم تروریستی (ایران) اشتباه کند، ما به شدت پاسخ خواهیم داد».
بنیامین نتانیاهو در اولین پیام ویدئویی خود پس از آغاز موج تازه حملات ایران و اسرائیل، افزود: «ایران و حزب‌الله از همیشه ضعیف‌تر و ما قوی‌تر از همیشه هستیم».
به گفته او، «ایران و حزب‌الله تلاش کردند معادله جدیدی را به ما تحمیل کنند که از نظر ما غیرقابل تحمل و غیرقابل قبول است. آن‌ها فکر می‌کردند که از خاک لبنان و از ایران به اسرائیل حمله می‌کنند و ما سکوت خواهیم کرد. این اتفاق نیفتاد و نخواهد افتاد، نه در زمانی که من رهبر هستم».
نخست‌وزیر اسرائیل تصریح کرد: «ما حمله خواهیم کرد، با قدرت پاسخ خواهیم داد. به نابودی تمام زیرساخت‌های تروریستی آن‌ها در جنوب لبنان ادامه می‌دهیم، و امنیت را به شمال باز خواهیم گرداند. اگر به موقع و با قدرت اقدام نکرده بودیم، امروز این‌جا نبودیم».
نتانیاهو همچنین گفت که ایران به سلاح هسته‌ای دست نخواهد یافت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76073" target="_blank">📅 19:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LosybnwIWD7SmNK4xprcUN14bjDv6NmEz-kUB3o2n-zoQbFX2no_WTCYkSF4VMkVCKrl074ygwoNOKSUEJP3dhl4r2s0QfHAbm62ygUXqsNuH4Vd0cTyx1HUkVecdYSp0C8S2w2HumvWeew56webhxKUR0XONREMTURZ7dK5oVNDq1UOSkWEyy0JTkUC1JMeXeG9gyVU0ZHmr_rEFL_6TqCa6Z8tOum2uDnf6DuP5KLQUz7mBWbJNbpDFSNgQbKeFXRvlxXUpMAt74wisSlQekJbpyKaTodBdp2D7pcgIjUz-_eumNyjXoAFP_rmLVCcY-5UsW7Y9XpqO-MVe8WDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هشدار تخلیه فوری برای مناطقی از لبنان صادر کرده.
J74wabx
ارتش اسرائیل با صدور یک «هشدار فوری» از ساکنان جنوب لبنان، به‌ویژه در منطقه «زقوق المفدی» خواست خانه‌های خود را ترک کرده و به سمت شمال حرکت کنند.
آویخای ادرعی، سخنگوی عرب‌زبان ارتش اسرائیل، در شبکه اجتماعی ایکس نوشت: «در پی نقض توافق آتش‌بس از سوی گروه تروریستی حزب‌الله، ارتش اسرائیل ناگزیر است با قدرت اقدام کند. ارتش اسرائیل قصد آسیب رساندن به شما را ندارد.»
او همچنین هشدار داد: «هر فردی که در نزدیکی نیروهای حزب‌الله، تأسیسات آن یا تجهیزات و امکانات رزمی این گروه حضور داشته باشد، جان خود را به خطر می‌اندازد.»
این در حالیست که ایران امروز گفت عملیات جنگی علیه اسرائیل را متوقف کرده است اما هشدار داد اگر حمله به لبنان ادامه پیدا کند با شدتی بیشتر از قبل پاسخ خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76072" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/puk4m700tIVQgskTxrAtVVsx3ySTv3aGWSUrTCZLiS8d-a5AgtEXBjSc3faLvfToG1AHYqcJzvRSGqchFO60USAvqVG02fxlppNF4DBGTZAWCreybtBGRr5uGmuyJmmQENs27bbV19kQsTLm4h8O0QiIuv1HJUSkgmEzgnusEnMP-7gksATdvQ7m_KDM3Ew8sH3jRxiP-np04WNSlEtJPuvgl34xMlCVFaYQcjMfSE3rmLcdVwnIFbRgV6zwS8VT_-hBZ0UoXY_gtyr5fQDBoeeRqIEucfoNbU86iyK67OjZMemozDNuHH0Ewm-fUoJB0UMG3JIvCmRyLW2lqCzsWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranSaat25
(وطنه*)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76071" target="_blank">📅 18:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76070">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mK7YdSzm7IzXYciC98vdGFVNdrTCTP3oIB6f5ZrO09GNrKrf2EAvqjBP_OcOIGpmc28cHJhO-j6ReM-3gMqKbsu9MIuDmcbf-LwRxeJJ6oiG-fT6wMybZmFtSyqn3RC2WDc-X1EtF4Pad9JxwRSC6WA3PpqwfX02wiuoslpWGOUqzYHuvwo4VwChWz3uOG-9VOjSFjVqMh0nLvdljLglLr7dYos-xsrX69KtWqrz1TyPBEi60O32umteY8fWJRZoOFmGbCAyGt2kAd00ZAgybqQ8LbzE1DNhSWgSnnE9LbN_Ex-mqWyDk-bwuSQb6_TDCcfVn6ZDIQQI5BziO9C9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Atlansick
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76070" target="_blank">📅 18:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76069">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XaBYk8Cr5o2027Qb2Iz-e3iTn2XsTUFMnb-0mYhXg4d-4xiIfnzlAAf8Le2CreGcS-X8_x8trRGcgJw3QuOlM6pSTAixCfZ9Gd-KmucTxRJFcIY8yXR6NoLplxYYnefimpjsQYxtVJjlUW9fzgum3J4l5HfBXWnS4SThI7HiFGKiQbVvhhAprWkpeSOXqnfmyDs1XT8lvDAEdfsvLgE2qGuGARONvN-DV8PtZ7t1bw2KU8CDsFYBmkrYRDfqOkx_Dlr2EmWYkSJZAMvcLbG0SeRy2JTxp6SNL46p998SV7h0jNTn1kN_1VoUw4gz5e_x57Zyqzz1Om_f3FVvUqIrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی جمهوری اسلامی ایران، در پیامی که روز دوشنبه ۱۸ خرداد منتشر شد، هشدار داد در صورت تکرار اقدامات آمریکا و اسرائیل، منطقه با پیامدهای گسترده‌ای روبه‌رو خواهد شد.
ذوالقدر در این پیام نوشت: «تهدید معتبر را از جایی غیر از واشنگتن و تل‌آویو جست‌وجو کنید.» او افزود: «اگر ائتلاف شیطانی صهیونی-آمریکایی دیگر بار دست از پا خطا کند، منطقه برایش جهنم خواهد شد.»
دبیر شورای عالی امنیت ملی در بخش دیگری از این پیام مدعی شد که جمهوری اسلامی طی «چهل و هفت سال و صد روز مقاومت»، از میدان جنگ تا عرصه سیاست و دیپلماسی، معادلات امنیتی جهان را تغییر داده است.
این پیام پس از آن منتشر شد که قرارگاه مرکزی خاتم‌الانبیا اعلام کرد عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل پایان یافته است. رسانه‌های رسمی اسرائیل نیز از توقف حملات این کشور به ایران به درخواست دونالد ترامپ خبر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76069" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76068">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fzqsz_qR1ltcONVFJkR0LrDRCjlAkpnD-2TNm30-4FUmU-R89lkP2shqezyy85UFxjQl0aTHp7RYDfHhswOyn0iQJheihbnMnJ5e0-qmJWZGeIPXovbxtkwOQPUdIMhA34T9FN-Rp4Q98LGRXg9bpvKuRlsYtqRjO8qpgEYtYpg1-mPBoIEazYkR6IXlFVPsHtkB_DaYobczWnGE3-G3pO21NE3o44V56jq5LPXG89UzWTgP9cv4DwmzgYiXQzi0dqaDvrQyY5tQu-QrAQrGyY_flYaHK0mfHPThr0oMXQbcFtprqiEahdWCrONq1V7zqbWwDRpA9Boe9oUwKiIqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، اعلام کرد هرگونه حمله به شهرهای شمالی این کشور با حمله به ضاحیه در جنوب بیروت پاسخ داده خواهد شد و ارتش اسرائیل به عملیات خود در لبنان علیه سازمان «تروریستی» حزب‌الله ادامه خواهد داد.
او افزود: ما تهدیدات جمهوری اسلامی را کاملا رد می‌کنیم. هرگونه تلاش تهران برای پیوند دادن لبنان و ایران و حمله به اسرائیل، همان‌طور که یک‌شنبه اتفاق افتاد، با شدت زیادی پاسخ داده خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76068" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76066">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c3ab90b1c.mp4?token=auFxRQXmVeFPQsWoZINJsoCuqrozGc6X-bTFi4LcFaDnhE3dvyrAryVlLbf6T3NeW-xTPj4VVOEr-EV8t1X9CDjPW8bdiDuzdhh74y2centlDAC_h2FDkFo5J1oa-K8CpN94Blyuphl24_b7Q-MrcdTf9NEP0nl3AsD-Jfzd4C_WqmE02okSsgFUAHoa6QAtp7h0Rv_K6JSlirJsVmbnl3pHLyfUoKjgH4G6plu-FsjvUk166U_pjkhdPcg5qLE790bioMy0vSepAoyDanJaTbWkMQt71T28xoStAYqirybPF1T7Cw69sskTrAgEm2V-sJsI7xg0BdPdkwZ4s1vsyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c3ab90b1c.mp4?token=auFxRQXmVeFPQsWoZINJsoCuqrozGc6X-bTFi4LcFaDnhE3dvyrAryVlLbf6T3NeW-xTPj4VVOEr-EV8t1X9CDjPW8bdiDuzdhh74y2centlDAC_h2FDkFo5J1oa-K8CpN94Blyuphl24_b7Q-MrcdTf9NEP0nl3AsD-Jfzd4C_WqmE02okSsgFUAHoa6QAtp7h0Rv_K6JSlirJsVmbnl3pHLyfUoKjgH4G6plu-FsjvUk166U_pjkhdPcg5qLE790bioMy0vSepAoyDanJaTbWkMQt71T28xoStAYqirybPF1T7Cw69sskTrAgEm2V-sJsI7xg0BdPdkwZ4s1vsyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسراییل، روز دوشنبه ۱۸ خرداد، ویدیویی را از لحظه حمله به یک سامانه پدافندی جمهوری اسلامی منتشر کرد.
ارتش اسراییل گفته نابودی سامانه‌های پدافند هوایی ایران، آزادی عمل هوایی بیشتری برای عملیات‌های بعدی فراهم می‌کند و بخشی از تلاش این کشور برای مقابله با تهدیدهای جمهوری اسلامی به شمار می‌رود.
@
VahidHeadline
و در پستی دیگر ویدیوی دوم بالا رو درباره مجتمع پتروشیمی در ماهشهر منتشر کردند.
بدون هیچ شرحی درباره اقدام نظامی خودشون نسبت به اون مجتمع پتروشیمی
نه در متن پست نه در خود ویدیو
اگر قبلا تایید نکرده بودند که به اونجا حمله کردند این طور پست گذاشتن بیشتر شبیه به تهدید به نظر می‌رسید. شاید الان هم همینطور باشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76066" target="_blank">📅 18:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76065">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GnBK1F_mtJi9-CvhhBc9SNcvuaycQ8FS_49Qdn72F9hM1qq5b95FvqACYYySHaqTh0wt9etiMKW0p1RnpVPArjydVbylXj-induHayINPkIS21yO1jjU5W8lEDcajBHSBOs6_3SEaE_42hVT-rwfo63I9WQYR9hRqFyBd63skcOtgZaxqTlrdfZoczZxgFwVa_AZjEnuVfRdk2_etv_MtLBLaVtUaMMyNTX9uywj66Lm0qsnuur0WwCvhEQTdzm2pe6O8MMaiXCLET1s27MafcVheJ3I4FOBMHIiorfofcuZH8N2YlQGzsk5nCsqtLEqW98yMeT75iR-Dle0fEb8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت محمدباقر قالیباف:
"معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را بر هم زدیم.
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود."
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76065" target="_blank">📅 18:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkr3IYWWfgbfNJLCKx46QZQ6PbADwC9i-jMrCy_kueMqMc_CG7jqnvokdujWVSPiDASBHqSIXKRHIQyRySUrjbG55uY2TgmdVeNwDaL2vSr8FKRTveksmcfFvAQ703JNFmK5LMcupX7GkM71isr7mX_b4J78xVMk1gwOd66sog26Ha5OOyfoEQQNBnPvN0Lh3boZ2w8qnvxRR9PeWbtIc4xuz_TDOxdmvZJomvJghO5Ww7CMiqkoWNLOoeBEi8-ZSHe98SEeU8VHbkYXGdOQL-ScwN3DZeB4Dco1hKoIXc4j2WC0P5Z85z2u1Svc5BlWkQHB1rD4hTmQx-uujxOLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های دولتی لبنان گزارش دادند یک حمله هوایی اسرائیل روز دوشنبه ۱۸ خرداد یک خودرو را در شهر صور در جنوب لبنان هدف قرار داده است.
خبرگزاری ملی لبنان اعلام کرد: «یک حمله هوایی دشمن، خودرویی را با موشک در شهر صور و در نزدیکی ساختمان صلیب سرخ لبنان هدف قرار داد.» تاکنون جزئیاتی درباره تلفات احتمالی یا هویت سرنشینان این خودرو منتشر نشده است.
این حمله ساعتی پس از آن صورت گرفت که جمهوری اسلامی ایران و اسرائیل پس از ۱۶ ساعت درگیری نظامی اعلام کردند حمله به یکدیگر را متوقف می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76064" target="_blank">📅 18:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHkVvmjJZ941eXGiT8YbeV5ZC7DbyCWyb6_mlANOuSe5szmBFthOaUvQFvy6hrExuM7Z9vgfYYzuj3Lep1lVPYiB59PM8qCGhNBJqzFdgC0EX6LrsPTIKeem_vxw5sW6KWRXndwqx2NbVcPbXs64t3kBUf9J8WpSERRyhEQL3KyNVguQ90Pc3k4XDWXvDswS3TY3XdPex5sfTnAgIq1baa-TXeMAPovzVw4NQcGvZWtVYRxYx0qxa23EPuSNz6-sSNgNMLsEHaSS3PiLb7J68OpDu06Boj3eRs955ZUjPWGQxBPVnf4ndf9RQFo3gK3R-WOKHTGs2HJqUM2mvOKcqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس سازمان اورژانس ایران، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اعلام کرد در جریان حملات اسراییل به ایران، ۱۵ نفر مجروح شده‌اند و تاکنون هیچ موردی از جان‌باختن شهروندان گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76063" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAxljtLlzVKwGiP2a_ynOLhZryNRMaWbl16Rxd4C8_lJl_YgYAZE7C2ZpQHONkREyTVR4okqAvJ3OKksjy9fQj2YXNnh0M4cvTR5hmm3tmmtR--GhI3oteArn5T4nC_wgPWKGBB1asuKKp4fELm1YEoFPajPwv8TnNHmIrADpYbZxf0JGYq6dBaIqTwOV3uNUJYRXS4FFa1i3ziHLiwzPPc3YXOHTaYKZPWHPKrG72djfddkxa0_THA5Fgc5klzyqt79kf00a-1nLnfVP3dEnK7_tufdIK3mNYtzngSi8diDeoSTBqBTXD1L730v00b5Uh1qbp2G1sD7D4-IZcsWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایسنا عصر روز دوشنبه، ۱۸ خردادماه، به نقل از شرکت فرودگاه‌ها و ناوبری هوایی ایران خبر داد که «همه پروازهای فرودگاه‌های کشور تا اطلاع ثانوی لغو شد».
این اداره همچنین از تمام مسافران خواست تا «جهت حفظ نظم و پیشگیری از هرگونه سردرگمی، تا زمان اعلام وضعیت عادی از سوی مراجع ذی‌صلاح به فرودگاه‌ها مراجعه نکنند».
این خبر ساعتی پس از آن منتشر شده که قرارگاه مرکزی خاتم‌الانبیاء سپاه در آغاز بعدازظهر روز دوشنبه با انتشار بیانیه‌ای از توقف عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل خبر داد.
همزمان رئیس سازمان حج و زیارت خبر داده است که «با توجه به شرایط پروازهای بازگشت حجاج احتمال تأخیر در برخی پروازها حتی تا ۷۲ ساعت وجود دارد».
او اضافه کرد: «برای فردا (سه‌شنبه ۱۹ خرداد) ۱۰ پرواز پیش‌بینی شده که امیدواریم بخش عمده آن‌ها انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76062" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXJXWTBpoYFB9VyL50YGtquUDl_bj5j6JeFBqZCJnnvFCreGjUG3bNM1YOEj3E4KNKEpKJvijNLIWqVMoomI62JYlFRYpJ5AiIjbIk3tQ0mrvdTLlbJd427Vd57iyfOr_4LKsorTRmclYaEVhetEyz-pyBSt226nZVhCARL7MSLqf9a66T2PQJlSQQ3oO523uSofCIYl6vRwksAYwZZqFDFKLRNuu2eDeaR9lvw9m974vqDMItms4aAihh9Fq-A36KqGzQgx1GscCLET4HKjU0zSLWaL-Qqzppu4fWctXjentBrrAtsh9_ZJrGAsXfyvPkUUHFa5JNzeAclW2egw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا، روز دوشنبه ۱۸ خرداد اعلام کرد که اتحادیه اروپا به‌دلیل تهدید آزادی تردد دریایی توسط جمهوری اسلامی، تحریم‌هایی را علیه شماری از افراد و نهادهای ایرانی اعمال کرده است.
کالاس این اظهارات را در جمع خبرنگاران و در حاشیه نشست وزیران دفاع اتحادیه اروپا در قبرس مطرح کرد.
هنوز جزئیات بیشتری درباره این تحریم‌ها ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76061" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b31564948.mp4?token=E2TQUdogCRrnxCw2nnzS7SSSluADiP_nQzRRB9jHJBUekWP7TLEoOaL0CtD83FtQWSfrRHYppqWx0rkTSNscGmg7zFLMoShvtLdHXYGTbR-Bhw_B8DJT2cAfO9aI5Yi49m72WMxad6u0ExbyzjOHHc3pbAIsPRsdoj7kFTYR9xDDv7ZYray4JeJd5P0IK2OfFcHJj-CJlBiigJ8UaeIwu-JIIEY7arwXRRlzxBg62rtaN5jDpqClJZv01JrSFRX79RZOphVlxtDFxBmEk_6cupju798EG7ObhkJrsBXLAEOnFv5ok3OlSsSl3aS1LaKVz7l7EA8dMdyuHH9g5A7cnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b31564948.mp4?token=E2TQUdogCRrnxCw2nnzS7SSSluADiP_nQzRRB9jHJBUekWP7TLEoOaL0CtD83FtQWSfrRHYppqWx0rkTSNscGmg7zFLMoShvtLdHXYGTbR-Bhw_B8DJT2cAfO9aI5Yi49m72WMxad6u0ExbyzjOHHc3pbAIsPRsdoj7kFTYR9xDDv7ZYray4JeJd5P0IK2OfFcHJj-CJlBiigJ8UaeIwu-JIIEY7arwXRRlzxBg62rtaN5jDpqClJZv01JrSFRX79RZOphVlxtDFxBmEk_6cupju798EG7ObhkJrsBXLAEOnFv5ok3OlSsSl3aS1LaKVz7l7EA8dMdyuHH9g5A7cnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی از لحظه حمله‌ الهه و شهربانو منصوریان به اتاق ریاست فدراسیون ووشو و شکستن دوربین مداربسته منتشر شده است.
طی سال‌های اخیر
خواهران منصوریان
بارها به ساختمان فدراسیون یا کمپ تیم‌های ملی حمله کرده یا با مدیران درگیر شده‌اند، اما همواره از حمایت نهادهای حکومتی برخوردار بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76060" target="_blank">📅 15:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf21K7092vzdDPbQFPg2MoMUoAeSWUmWd1_gwHuFkSuwss8uw1aMuIQmtK3Rgw12ZOMVXd3OEHN8WOXD1Ynv85cUd441BedAL-TkakTKKQgl8DGZNQCl1RxvTMwfkblE2myGS8dEH8A4tFu8Zn8aRu7plhQmFcDa0hvLZ42148kDWRotQux1n0HUVZ9Y4y6wFVVG53hVKvD1HNbdB9xDOz4GJdSVGUYRNNesoce2rWOGZUg8-5ss-CPhWELHra5ibbKiO8BnalIqwpw2CDE5u27c7vvsVYKltRnToP8GGvfERGPA87DtIz3p1PIW5PE23Gztf9A0jWSXNAe-F66Arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سپاه پاسداران از «توقف عملیات» علیه اسرائیل خبر داد
♦️
قرارگاه مرکزی خاتم‌الانبیا سپاه پاسداران، روز دوشنبه ۱۸ خرداد ماه با اعلام آنکه نیروهای مسلح جمهوری اسلامی ایران در واکنش به حملات اسرائیل به منطقه ضاحیه و جنوب لبنان «پاسخی دردناک» به این کشور داده‌اند، از «توقف عملیات» نظامی خبر داد.
بر اساس بیانیه قرارگاه خاتم‌الانبیا، پرتاب موشک به اسرائیل «در راستای حمایت از مردم مظلوم لبنان» توصیف شده است.
در این بیانیه آمده است که این پاسخ برای اسرائیل و حامیانش باید «درس عبرت» باشد.
قرارگاه خاتم‌الانبیا همچنین اعلام کرد «توقف عملیات نیروهای مسلح» در دستور کار قرار گرفته است.
با این حال، در این بیانیه هشدار داده شده که در صورت ادامه حملات و اقدامات اسرائیل، به‌ویژه در جنوب لبنان، جمهوری اسلامی ایران «اقدامات بسیار شدیدتر و کوبنده‌تر از قبل» انجام خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/76059" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76057">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PeTxH4asAwxzWmEb0KYtfjSJ7LgWCMthbEu04YaDCfit3vy-RWy7AcWyOYHMDl1WOXmpSEDO9mUIfq6gv25qgLBmxr__LpdJHNBPsnT4W_Kx2lmYJWufqv-VoUK8qNF7UNtO8wDPGO79waGeb46gtCX7I0p62c6R7ji1unSimMZJ1lZ60tRHNTmvum4Q4_sQ3Y_NKf1Jp99hTwsHAeFCCAPu7iic4TrO6jL6Yqu3MTStkqCn9H44hIl7WvmBmhiZzbKUuX1qv8sKKj8K6K1ALnWtFQ5TPDDUu1x9gXaEkTNKPpx6HONo0FiLcsyufXVjfjVbw3jsTp8AsJ9OV5oesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tvBPqg49BwlM5Z41VWp3FDYKy_f4PYy6HkWxc9-Nvwcxbb6nftTdidJBnADMvIxh26Bn3dYjNFTruEK5a9n9ULVQyHfTGm6jlmgvmfnt9tDs52h4FHr_CNSlvYqtotxX8IRpi_y4QFFEhqR2oADT54vf3YH4eWjyts9SgKcZjmPZSiyjS56BDdbcjnR9B5NDp4TFlFNp85eX-hYmcAIOXjwe-SQKPkmSFcITDteGSihEf-btTX7ME4UtyL7qLN8P21i7KTZSyA53nK2e3KM8-0zz0YRuUbF-ZRm7yBIawPt-Ssi-lFOm4q8PuYrkG3Ss-wUb23M4K8HoQhcTZB4kmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «تیراندازی» را متوقف کنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دو طرف، اسرائیل و ایران، به دنبال برقراری فوری آتش‌بس هستند! مذاکرات نهایی درباره «صلح» در جریان است، مگر آنکه نادانی یا حماقت مانع آن شود. محاصره تا زمانی که «توافق نهایی» حاصل شود، همچنان برقرار خواهد ماند و با تمام قدرت و اثر کامل اجرا خواهد شد. امور باید به‌سرعت پیش برود. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/76057" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMiBHXuOni0h5ePpOtvSP5C_K_KH6jpPToyi9TBjY19J9X4DWGQ1Q-pSU-BJiZXq2xiOxmmLwO17YrT0uYoe2WbznHbWIyVdiiLAhfVxTtPjRCdS6y8V5KHeu_TUwSNNQtjUIzsXAo3J0EMtQykwqukldQMMSF7rZb_8E6sI1Y4GMGcpFbMcTjicwMgBm4CWSavNQpzNjmPFSkA2PLbC-pL-f_KIBxmlcir6qwHG2ErHOSQilMj6jm43bjEyvoQP7Txm66DZ9Uq7Tcgw_F_1IpErI1ReTgCJ_L0fEGXZVZ4XjuZMnxfw-XlHRZridPi_FoCYdPkON5GVw4jx3C9j_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی گزارش داده‌اند که نیروی هوایی اسرائیل همچنان حملات خود را در نقاطی از کشور ادامه می‌دهد.
بر اساس این گزارش‌ها، فرودگاه شیراز در جنوب کشور نیز در میان اهداف حملات اخیر قرار داشته است.
هنوز جزئیات دقیقی درباره میزان خسارت، وضعیت پروازها و تلفات احتمالی منتشر نشده است.
@
VahidHeadline
در خبری دیگر:
خبرگزاری مهر وابسته به سازمان تبلیغات اسلامی نوشته:
"پهپاد متخاصم دشمن آمریکا_صهیونیستی توسط پدافند هوایی در آسمان تهران هدف قرار گرفت و منهدم شد./ مهر"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 509K · <a href="https://t.me/VahidOnline/76056" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-h8toECyVXn4mwM4ren5uUVtA1gQOOxF9F7ek0l8dkmmOXdLHmfUa5iJS80Tq02qeQMPXbr3n8tBQa7BFvJPkO6AWMxs-1ORBj3_-xFCCGmus2_v1MnA5GV5l7Q5aUiQJlNVn2ECRDKvuswuQTaOZ5Y6lsl5qm3YmHjs7L-lLnAVS9KFD3l6aONCMaqy9wihO9NvLZlJFrUjSzeDyHvBFN1CtrUKrX8cQwm3ld1qkEzDp_vBd2j7p9g6crkyjgHh11s1_oE_aYj1yZARrLwEfVJXnri-5XeyOeGtLgH8bxTNqTZUErDCXNd1cHGA71cNGwK-xNhfQfQi8VFXuKWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای گفت در پاسخ به حمله اسرائیل به صنایع پتروشیمی ایران به صنایع پتروشیمی حیفا حمله موشکی کرده است.
بنابر این بیانیه، هدف قرار دادن اهداف غیرنظامی و تاسیسات نفتی «بازی خطرناکی» است که زیرساخت‌های انرژِی منطقه را تهدید می‌کند.
پتروشیمی کارون ماهشهر که در بیانیه سپاه نامش برده نشد، تاسیساتی است که هدف حمله اسرائیل قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 503K · <a href="https://t.me/VahidOnline/76055" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پیام‌های دریافتی:
‌
وحید تهران صدای مهیب وحشتناک
ساعات 11:33 دقیقه جنوب تهرانسر صدای انفجار اومد
سلام ساعت ۱۱:۳۰ رباط کریم صدای انفجار
تهران صدا و موج شدید انفجار ۱۱:۳۲
همین الان صدای تک انفجار غرب تهران
زدن تهران صدا واضح انفجار
ساعت ۱۱:۳۳: صدای یک انفجار شنیده شد - تهران آزادی
صداش خیلی زیاد نبود حوالی غرب باید باشه احتمالا
اسلامشهر صدای انفجار ساعت ۱۱:۳۲
تهران الان صدای انفجار اومد
تهران غرب ۱۱:۳۳ تک انفجار بزرگ
سلام وحید جان.۱۱:۳۳ تهران صدا انفجار اومد.من غربم صدا دور بود ازم
۱۱:۳۳ دقیقه صدای انفجار ملارد فکر کنم زدن
ما سمت مهرآبادیم ساعت ۱۱:۳۲ صدای انفجار اومد
صدای انفجار در اسلامشهر ساعت ۱۱:۳۴
وحید ما غربیم 11.33 صدا انفجار امد
یه صدای تک انفجاری اومد الان انگار سمت یافت اباد
بهشت‌زهرام. از نزدیک اینجا صدای انفجار اومد. ساعت یازده‌و‌سی‌و‌دو.
همین الان اسلامشهر تهران ۲ تا صدای انفجار
سلام وحید جان، صدای انفجار در فردیس
غزب تهران سمت پونک همین الان صدای انفجار
تهران اطراف اتوبان نواب صدای انفجار
شهرک غرب
صدای مهیب انفجار از دور اومد
وحید قلعه حسن خان دو تا صدا انفجار قوی
سلام باقرشهر کهریزیک صدای انفجار 11:33
وحید داداش سمت دریاچه ۳ تا انفجار ولی دور بود
11:32
گرمدره صدای بمی داشت تک صدا بود ولی دلم یجوری شد
سلام وحید جان من سمت مهرشهر هستم ساعت 11:31
صدای انفجار خیلی وحشتناکی اومد
از شرق کرج یا غرب تهران
ساعت ۱۱:۳۳ سمت ملارد صدای انفجار وحشتناک اومد
سلام ۱۱:۳۳ صدای انفجار اومد از جنوب تهران از دور بود
تهران سمت شریعتی ساعت۱۱:۳۲ صدای خیلی دور انفجار اومد
از ملارد ساعت ۱۱:۳۳ یدونه صدا اومد
وحید اسلامشهر دوتا صدای خیلی وحشتناک اومد
ساعت ۱۱:۳۴ اسلامشهر ۲ انفجار با فاصله یک دقیقه
ما سمت چهارراه ولیعصریم دقیقا ۱۱:۳۳ دای انفجار از دور اومد
سلام ما عظیمیه کرج ساعت 11:33 صدا شنیدیم، دور بود
سلام من نزدیک مهرآبادم یدونه صدا اومد بنظرم بلند بود اما خیلی نزدیک نبود
بازم هم مهرشهر کرج صدای یک انفجار
ساعت ۱۱:۳۵
درود گلشهر صدای انفجار اومد همین حالا
ما تو یافت ابادیم صدایی که اومد نسبتا دور بود ولی خیلی مهیب بود
سلام وحید جان من سمت شمال تهرانم ۱۱:۳۳ دقیقه صدای انفجار دور ولی سنگین اومد
آپدیت:
پیام‌های زیادی درباره فعالیت پدافند در مناطق مختلف تهران دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 511K · <a href="https://t.me/VahidOnline/76054" target="_blank">📅 11:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKzBdURTKuLwI0Hy_YOfkOOOc7CknKcfjGV_1NbeymxEofPs3nVUElk5evN5ESztrZ_bLGlB4bNGL0Z25juxsVCKpW7vekzdbMWBR3jZU5Id3BAtxHrXpOP_5W1dEXqDwkyuHwNIRDIAmlKSIMhwgXDikh0ulEDzmB8jTUTgB1jLDtiXQlN_ySMAx5VSN-CDyiKnaQflFF_57wEJKprVZm16t1YAusQNFXotCQfoA05LYi97PKfzFy3oCoY_Yi8eoWeZyzz2u445RYXQhFoAkfGjQi8rvY-M6mJhz8bmyY6qpyXE6yHWkJuEZeRbY0dFfjwtToviy72wJOMfbY5rQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ایلان ماسک: "تنگه هرمز به نام اهورا مزدا از آیین زرتشت نامگذاری شده است."
elonmusk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 444K · <a href="https://t.me/VahidOnline/76053" target="_blank">📅 11:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76052">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOBe4gx7ghLCFad-o7396r48TiT08IPjCz_njorYOSp8AfaMqsRVWM7T50TZ0UwDEutJAxDLOYDafMsPpL-ivFuknZ--1fy3gwFf1BiPVbusO3IR8zjiwLp9xeAX8cj_RDCIv2S9VHBsUyvNvDjM6nmKH0befetm2nJmaXa_1p3sJTpRU_U1rUvz6adcI8KKsp5h1yX5kPhiCfs77YKW4ynO5PystzQXo1XYPd4pLFH_vDFxgy2EcvtMm68myiL2iN0lEb00itVEiYmSLzxVWFP2oNgtb_-p97pyibyOtnl6xstwIciPCo50KRovyETAEIC9pYjn1lzEuznF4Ut9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نخستین کنفرانس خبری خود پس از آغاز حملات ایران به اسراییل گفت که اتفاقات ساعات‌ گذشته، به بی‌اعتمادی موجود میان تهران و واشنگتن دامن خواهد زد.
بقایی در نشست خبری خود گفت تبادل پیام میان ایران و آمریکا تاکنون در فضایی لبریز از بی‌اعتمادی انجام شده و به گفته او، آتش‌بس نیز «به طور مستمر و مکرر» از سوی طرف مقابل نقض شده است. او تاکید کرد جمهوری اسلامی هر زمان که لازم بداند برای دفاع از «امنیت کشور» اقدام خواهد کرد.
سخنگوی وزارت امور خارجه همچنین آمریکا را مسوول تحولات اخیر منطقه دانست و گفت اسراییل بدون هماهنگی با واشنگتن اقدامی انجام نمی‌دهد.
به گفته او، وزارت خارجه آمریکا حمایت از اسراییل را دلیل اصلی جنگ علیه ایران دانسته و جمهوری اسلامی از همکاری و هماهنگی کامل فرماندهی مرکزی ارتش آمریکا، سنتکام، با اسراییل در حوزه‌های دفاعی و تهاجمی اطلاع دارد.
بقایی با اشاره به تفاهم آتش‌بس ۱۹ فروردین، آمریکا را مسوول هرگونه نقض آن دانست و گفت پیامدهای تشدید تنش در منطقه متوجه واشنگتن خواهد بود.
او همچنین از «رافائل گروسی»، مدیرکل آژانس بین‌المللی انرژی اتمی، انتقاد کرد و گفت در صورت تصویب قطعنامه‌ای علیه ایران در شورای حکام آژانس، تهران «پاسخ مناسب» خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/76052" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76051">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/025351cf82.mp4?token=WkekflisnLiPnKmRO1XVHG8Kb1Y4LL0VuihEbAMqgI3e_HDqp2PXv1jiYbThdF6Uh10ZRK4DsKVuUDrtv5sxiL_5dQbMzp0ydLVGpADLf5m2JN1GlaDQXb-kryyR06qKWry9CNu-CQiUUZX-YiVmtaPU6A4Ss3BDvAobHZMG-xuA-JvIq1UWHonJQLqMDsAwNNtSTy9xK6CJ17RemvuTTbDiLraL8_SCRhRyKEEsx_paJ2dvO7xeJjZ8sP2cI9qjORDflqu4CmeE8OCdWlFv4oh-yuFnbmBJgxibstRekyFrjlceIcBVpV4mOx1-QFd1yRifxnJZbFKgM77cQ8Sh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/025351cf82.mp4?token=WkekflisnLiPnKmRO1XVHG8Kb1Y4LL0VuihEbAMqgI3e_HDqp2PXv1jiYbThdF6Uh10ZRK4DsKVuUDrtv5sxiL_5dQbMzp0ydLVGpADLf5m2JN1GlaDQXb-kryyR06qKWry9CNu-CQiUUZX-YiVmtaPU6A4Ss3BDvAobHZMG-xuA-JvIq1UWHonJQLqMDsAwNNtSTy9xK6CJ17RemvuTTbDiLraL8_SCRhRyKEEsx_paJ2dvO7xeJjZ8sP2cI9qjORDflqu4CmeE8OCdWlFv4oh-yuFnbmBJgxibstRekyFrjlceIcBVpV4mOx1-QFd1yRifxnJZbFKgM77cQ8Sh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت ارتش اسرائیل با انتشار ویدیوی بالا نوشت: "در دوره اخیر، سامانه‌های پدافندی در چندین منطقه مختلف در ایران مستقر شده بودند، ... این حمله منجر به انهدام این سامانه‌ها شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76051" target="_blank">📅 11:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76050">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQxYDHLFxpLm6jMZ-X-KalExbxSeit5jcAI5dICvXs0RKPnrVZFjcK8t9CiuPKhcIbTWngYuNSsiOnT33QyMOvq5KizO9mKYzCAnrpzWufOiDlPNLBBX7UFkhf73XUcqd84m-HrzVh2eAh0z1RfveBJkNnw1suI73HKvopZ9WzD9Iz4xa1PBTRe0D_B670qBoSOopOzjea25Bxk2TFSWqs5IPxwrLdZt0IysbNslSjoXkFCiHzarmYA1mLCvMVLQyE8WpdmMrYxQMWSAdP4HCkm5j2v4qXjBAIY9xYB9EJFmx48UIItty_ys-Eg2woP1mQ5FAEbJBexX1QZrEmR0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه قطر اعلام کرد «محمد بن عبدالرحمن آل ثانی»، نخست وزیر و وزیر امور خارجه این کشور، در تماس تلفنی با «عباس عراقچی»، وزیر امور خارجه جمهوری اسلامی، درباره تلاش‌های میانجیگرانه میان ایالات متحده و ایران و همچنین تحولات لبنان گفت‌وگو کرده است.
بر اساس بیانیه وزارت امور خارجه قطر، نخست وزیر این کشور در این تماس بر حمایت دوحه از تلاش‌ها برای مهار تنش‌ها و دستیابی به توافقی جامع که به تقویت امنیت و صلح در منطقه کمک کند، تاکید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/76050" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rlPPrOJ7pW6tspT17iXD0403adRYGedBJ5JyfEWALtJBvcJ_Ams06vLJLeFp4ffpAmDbWr1o8XNyu3lXEpGGsp0-Qf0-ACn4PGukMFlOakg5KFD9flQU3yjUQt0OAjWIHe07MWTeV270n4J0D4hnJvjW0GQy3dwMCod6AFt_goKjsBZE9qXu4XvrzasC4N_PubBctNxI5mEbbbliWuPuxYtKf31X6FEmsGbbu-XHY8pZ51oxUiWFkwZcrTvCMfqEpxieQGncrinb9IufIhaG1dgswdKa-IUTmSpKjy1Vw_M-7ilINo-0eYPE1bJvPZtDU2wbWE4xJ4A-xe54Fdonig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NQeyd1se9fF9moXb0YVhhbrHYpYm9Wll7hzZ87jJg1WJHIxh3zpXai9nqA28BAhWqxllQCqOY3qegvBhmKla12OoyAIAO3ZjLpkNlIyYy0fiDcWc42lGBgCttondyJJU7GfWcb6PkZzTJspa-EBjyNVqDnFR9IJdD-AidAk-9gOhGOGxrVpP2zTBqSvT1DB3g7MRNlndl_pnGZIoJEtaUbGQa_b2ej8D2xhUiXr9UlPzTIc7hCcTSPlNI8W1x2_V5icVZqqM0cyHaasJI2ta91CpaXiHif2foi49tG_C9tzOvQB_-0ho2nhoIQZJsZrzOVl6ZnCyREd5bSsi5V15Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qk4s88oo_0n2C1TcUDkNGTV9P-uOcSd8CKUcbz8KqHeJLNZ4xeHbcrNXzwK76HRk_yuZ8AzHEDOabEjCRZvuUaM00HTP8miX32UxttS46rhW8Yz_42Jg-KTtkMgdMX5XdoOfOBhVz6QPi6puGzgOpLTGldsvDruXO_S1mQoVR-7cvAG8_-hfvNGZS5IWuUCtoXI3GVoVdQK9r03SidfoyMMCquiX8J2rwFvCjTQ4CUZDxRPEaNESGPuK1oydflFhcDK1nxp6eG9XVY3mCxOJMEbhEs0rJIt9DVwQSEogr7hRDTjOO8af4c1V1MYO2YJFrFglCAvaXkkmoe2zV91g-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/551c6649bd.mp4?token=mdaD2rT-SevZsNIIXAxSoY0j3QHkWYXoyGIKUV2KEwzl9-dIzBV-OeYDJDGV7wn9-GGfuNRRoPPoEM-HtJI1VPPm158jVF0fxeLNvlPA9Ug3-cpOyOiwYwaFCDmFn0otA83luVkEanY2-_YFBY62qrAmSb5eHN3Z7dUFwK0Cssmv52rc9PMQ38RLVhkGwVrWKLUJWcQYzo0T90K7JQrhGFDOgyciFcIOIGzwaY8WciwzOUgOYp3QamX0jAZQprRMJRWkKGqXFd9tJXMY5ARSid_geMaQ3KFzMTOqmRBx-Gs7He3R7zNKYYTrITJs13R_xrOtQIDb3VAr3gEwkdidYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/551c6649bd.mp4?token=mdaD2rT-SevZsNIIXAxSoY0j3QHkWYXoyGIKUV2KEwzl9-dIzBV-OeYDJDGV7wn9-GGfuNRRoPPoEM-HtJI1VPPm158jVF0fxeLNvlPA9Ug3-cpOyOiwYwaFCDmFn0otA83luVkEanY2-_YFBY62qrAmSb5eHN3Z7dUFwK0Cssmv52rc9PMQ38RLVhkGwVrWKLUJWcQYzo0T90K7JQrhGFDOgyciFcIOIGzwaY8WciwzOUgOYp3QamX0jAZQprRMJRWkKGqXFd9tJXMY5ARSid_geMaQ3KFzMTOqmRBx-Gs7He3R7zNKYYTrITJs13R_xrOtQIDb3VAr3gEwkdidYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
ما کاشان هستیم
اینجا قشنگ صدای موشک رو حس کردیم که داره رد می‌شه
همین الان ساعت ۱۰ و ۱ دقیقه.
از خمین همین الان موشک زدن
شلیک موشک از ابهر ساعت ۱۰
خمین ۹.۵۷
وحید طرفای ابهر خرمدره ازناب زنجان موشک زدن ساعت ۱۰.۰۲
سلام شلیک موشک از استان مرکزی
وحید جان سلام ساعت ۹.۵۸ دقیقه یه موشک از ابهر زدن
سلام از کاشان هم همین الان موشک زدن
شلیک موشک از زنجان ده صبح
سلام از خوانسار صدای موشک اومد، رد موشک هم توی آسمون هست.
همین الان از زنجان دو تا موشک بلند شد
هم‌زمان پست ارتش اسرائیل:
ارتش اسرائیل شناسایی کرده است که مدتی پیش موشک‌هایی از ایران به سمت حریم کشور اسرائیل شلیک شده‌اند.
سامانه‌های پدافندی در حال رهگیری این تهدید هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/76046" target="_blank">📅 10:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76045">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e62b7f335.mp4?token=HXxlvs62QzJoWnuCPNPjTBPaL1BysQt0wPoZAyKdpLU5-po5zyDfv9B71b55WUmsbnN-xl9mXnHGla3FS7YfM3yBal2JNlEf_RlZUa3QgHGITl3HtV-YANZq_dWnyk60rH6G6QteqJRcoe_CFj1L7S_wjZQbxtBTppyLqqSdrAHf4l2Kz-0efyXgJh0vKsLEIiw9i66taPlxCz9GkFFbMyHCtEq2cuVieJ1fEWpniHf4OG8OntWNktnpBpWzKgYRuh7KkoICDZjZIRAvy8_ekeiPyiwiTdydqsj8Un_RRv0KWHkgqYRN4gGBDPIgkthqvgUe1Y9AXlM2NvCkzrDc7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e62b7f335.mp4?token=HXxlvs62QzJoWnuCPNPjTBPaL1BysQt0wPoZAyKdpLU5-po5zyDfv9B71b55WUmsbnN-xl9mXnHGla3FS7YfM3yBal2JNlEf_RlZUa3QgHGITl3HtV-YANZq_dWnyk60rH6G6QteqJRcoe_CFj1L7S_wjZQbxtBTppyLqqSdrAHf4l2Kz-0efyXgJh0vKsLEIiw9i66taPlxCz9GkFFbMyHCtEq2cuVieJ1fEWpniHf4OG8OntWNktnpBpWzKgYRuh7KkoICDZjZIRAvy8_ekeiPyiwiTdydqsj8Un_RRv0KWHkgqYRN4gGBDPIgkthqvgUe1Y9AXlM2NvCkzrDc7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اعلام خبر حمله موشکی به اسرائیل در تجمع هواداران گروه‌های مسلح شیعه در تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 473K · <a href="https://t.me/VahidOnline/76045" target="_blank">📅 09:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhWHrE5PdIKQhNmHZb-pKNAIO735Q1DjjLo3H58fswwdc_Ivhg_5Xq5aKXw0pXUSXbJOSYv3zHMfe8K0EFkhn0Z1O5g67NkPdJQv2s18ZX-70dMlq4S_2Ha0viXugjSSGYAeWmXMKXYTIoUjOyJ_ZhizBy1bmZQNapPvmymkaoW-Eyb2Y80RnwvF4wX-KoWER-n78e_ljyaJGVL_803QaLjEHd5n2kUKzTIhpeROjLFqUu8GFnx3oLc0bc_nFjrpbr0TfM84y0C-eUB8XpzT_XfDr6kfYVq9BSUwlpvOFeqQ9if7y0sf0yN-lvAW9pRdlXaLwbRXZPMFzK03onc5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که تمامی موشک‌های پرتاب‌شده از سوی جمهوری اسلامی در صبح دوشنبه به سوی اسرائیل رهگیری شدند.
ارتش اسرائیل افزود که پرتابه‌ای که به یک زمین باز در کرانه باختری اصابت کرد، احتمالاً یک قطعه بزرگ باقی‌مانده پس از عملیات رهگیری بوده است.
در همین حال، پس از آنکه هشدار اولیه در اورشلیم درباره حمله موشکی جمهوری اسلامی صادر شده بود، برای این منطقه وضعیت پایان هشدار اعلام شد، زیرا موشک جمهوری اسلامی موفق به رسیدن به خاک اسرائیل نشد.
@
VahidHeadline
به گفته نیروهای امدادی اسرائیل، اصابت یک قطعه از موشک‌های شلیک شده از ایران، به چند خانه در یکی از شهرک‌های کرانه باختری آسیب وارد کرد.
در این حادثه مجروحیت گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/76044" target="_blank">📅 09:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e89e6ed06.mov?token=B-JJVE_zBGYvUS5_21-LhMlVMmiclF72EG4DI0fVlrDNF1rXG4PiYbl7hdYCe5kSHxCZw_AXz5yN4QFkp4JjwnOGFFWJ8IqGIA3kZqrJMdvCgUdXTmgrq0p--N1cDqtzSwY6_3fshn0T8ne_7cg1xuptHDE2vXkTBnn0QV9RxsdOkqAJQn3nMo_li6aTZZQ_Vo_FOoWatCpz2XxgmeZ-KvX2h8xd0JFittJcXkfjpuBQLtw_HuyEgGSvLw_0ihhY9sdSTltBT617V0rFs-hd5Ip833nkzmLOkg53zuzdf-VhWdludNV462REDPStHRgycK1In5ERtma7lTTPl3lpwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e89e6ed06.mov?token=B-JJVE_zBGYvUS5_21-LhMlVMmiclF72EG4DI0fVlrDNF1rXG4PiYbl7hdYCe5kSHxCZw_AXz5yN4QFkp4JjwnOGFFWJ8IqGIA3kZqrJMdvCgUdXTmgrq0p--N1cDqtzSwY6_3fshn0T8ne_7cg1xuptHDE2vXkTBnn0QV9RxsdOkqAJQn3nMo_li6aTZZQ_Vo_FOoWatCpz2XxgmeZ-KvX2h8xd0JFittJcXkfjpuBQLtw_HuyEgGSvLw_0ihhY9sdSTltBT617V0rFs-hd5Ip833nkzmLOkg53zuzdf-VhWdludNV462REDPStHRgycK1In5ERtma7lTTPl3lpwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@
iliaen
ارتش اسرائیل حمله به سایت‌های پتروشیمی در جنوب غرب ایران را تایید کرد
به دنبال گزارش خبرگزاری فارس مبنی بر حمله به مجموعه پتروشیمی کارون در ماهشهر که خساراتی به دنبال داشته، ارتش اسرائیل حمله به سایت‌های پتروشیمی در جنوب غرب ایران را تایید کرد و گفت به اهداف متعددی در مجموعه پتروشیمی ماهشهر حمله کرده و جزئیات مربوط به این حمله را به زودی ارایه خواهد داد.
ارتش اسرائیل پیش‌تر گفته بود که مواضع حکومت ایران را در غرب و مرکز ایران هدف گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 453K · <a href="https://t.me/VahidOnline/76043" target="_blank">📅 08:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac9a29e4c7.mp4?token=qOe0GSMBpTxS_HdRFdESRHSMIo7Z3oJmF-VQjm22n_F125QqyqfC7gVf1wTtEgcBpMYudFPZ1Ckvet7vvD75qduF9iE8-RCxs_bHuMIsBuk6IJtC8G855O7zKfZiHIcW39vMm8fpvU-R-NcuQtLtiHuCP0fcm7cOwSRQaa_NNZLeB5ZKI4BiFkkFsV5tchpJqNxCpxRQUtpne2NoB8rQzYPqsUpig2FOfR3UPlFizBycxsF1Qfw7JH5cu1CbR2XCK7D5T1l0CSge-U85LxPJdpKT5ZXtw8zlU9_HmTEKG9G31QXR9etvYG_t35EGMvJeYF7JtrUUsfn4IqNqIPC8dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac9a29e4c7.mp4?token=qOe0GSMBpTxS_HdRFdESRHSMIo7Z3oJmF-VQjm22n_F125QqyqfC7gVf1wTtEgcBpMYudFPZ1Ckvet7vvD75qduF9iE8-RCxs_bHuMIsBuk6IJtC8G855O7zKfZiHIcW39vMm8fpvU-R-NcuQtLtiHuCP0fcm7cOwSRQaa_NNZLeB5ZKI4BiFkkFsV5tchpJqNxCpxRQUtpne2NoB8rQzYPqsUpig2FOfR3UPlFizBycxsF1Qfw7JH5cu1CbR2XCK7D5T1l0CSge-U85LxPJdpKT5ZXtw8zlU9_HmTEKG9G31QXR9etvYG_t35EGMvJeYF7JtrUUsfn4IqNqIPC8dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابت موشک به شهرک یهودی‌نشین ایتامار نزدیک شهر نابلوس و در بخش شمالی کرانه باختری رود اردن
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 457K · <a href="https://t.me/VahidOnline/76042" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBR5wayG9A9lSu0zaWjXZw1PlRbYCdJsk5l0t5XkN4zP0-6CK90GKukwxrvZwWq8UXLH4m5EKthgJgcf4dZqFmxvV_uMPEEITdpLY3sJ8xEAoU3-Z_QjGKJSg-D3dwuFlj9p2t1rchsNgmoFkw-0LdLrx-gi5FTPkMBCGZGOpt5z6CmfVZSVuIiYUldK1CV2pC4SJjm3H-4szcSDkXxUsoQHTaR0Xq5Og1Gjh3GDgLyM4515PaOXRb4o1Un87EtKeNbHuMqk4K2Fj2PxeeJDacaHPkICqP_VGplVDBUlT0sRGmuExjLABuHK5tA0ZufEqVwqWQc7Q2L91AK-ej5rAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بامداد دوشنبه از رصد موشک‌های پرتاب شده از سوی ایران به سمت اسرائیل خبر داد و اعلام کرد: سامانه‌های پدافندی در حال رهگیری این تهدید هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/76041" target="_blank">📅 08:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76040">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیام‌های دریافتی در پی گزارش‌ها از شنیده شدن صدای انفجار در ماهشهر:
وحید پتروشیمی کارون تو ماهشهر زدن
آقا وحید سلام پتروشیمی کارون منطقه ویژه ماهشهر زدن دستور دادن کارگران و پرسنل برگردن خونه هاشون
سلام ماهشهر پتروشیمی کارون ساعت ۷:۳۰ یک انفجار رخ داد
وحید جان منطقه ویژه ماهشهر صدای وحشتناکی اومد. میگن شرکت کارون رو زده
آپدیت:
پیام دریافتی: کانال ماهشهر هم اعلام کرد
پتروشیمی کارون رو زده
اما صدای انفجار مثل انفجارهای قبل نبود
همه نشنیدن
معلوم نیست با چی زده این بار
🔄
آپدیت:
خبرگزاری فارس، نزدیک به سپاه: " تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
حیاتی، معاون امنیتی و انتظامی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
خبر تکمیلی در خصوص خسارات و تلفات احتمالی متعاقبا اعلام خواهد شد."
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/76040" target="_blank">📅 07:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76030">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eCLt7IZL77KShOuYb0l9Do389fnvgvKmrNGRCXsohyMcbsoQoVakuWPUgnX6oHqvnI33_O0gvKxP9YrcoJS3eK1yXfY3UU85FYMmnSFLEbz_ZB1drDPB0zfhYiHY-5bp6y7-1KvvA5XXnjGm-8z9w694u2BTRyo0XoKpg496g1sDTC4_gIjuO7v_y-AURRpfdMQz3j1Yc7gWqi3Q9SPc8IgdwVi5j3lzGUjZmzB4-WbBDR3rr7ac5IASJdmOKne_XnS0gMwKCDZVY7_NFZ-kP4rK92xx0ELXOesHOgXPrIujhbe-bDHFx0v9jL9A1FrRujkmUAgFbMAxNLn5XYo-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pecAYElhVz4BG_NJCVwNEHtLX7UahrrByDsHd02298htu_0JNLdwQ7Z8RJ_vJpV8r9zJJ-Ar-w0xaiD2pg2_V1MWvOHU7KBqVbvrFhRGGN4M3MCCXcW2V5UVEcgFmRK5fOxYwKvlcDWqFauuhLYsq-dQ3Wbv-A8gQeb8oL4gKq-7E5gc11y_hMAUZ4r40sMsycA5Ew8uoc5YGrH6Zf6Z8dre8VEpL1z81eKiM2v8hdyNg1GWRe9PDXVH3B5mxv-yAtvCMg73rmTN4XzL6pnfipphl4PtVqHe-YfxfOVyJlbKuOr0IKILsqCbmVX-WsSBS4HCA72vbgE1OcUxS7B4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VI22V4Axc52GtwUo2KiOZEPaRO8Yzyqz9Ezhvr8JHaORMnLdusy-q6FYQM9c5pG-aE4tqrOdWTmiEL5qe8si7o9h3anhYSE7GtYoZ5LXTOJ0KtxSwxGkmLRzxWOiB0WRNFKpkQpNgE1g7GaHJ7kSkQrh9oZhERJBttNwynXsHzlvwMDtETDBZ6-08MDJvbN5h3j9u3B46fh3NrFBom8loT71IYOn1y-KCRsGO2lGg2_FpjR_OMt07j5amckOwo0yfe8mYO0vJR3yKCYTE0CHMqtnGzUe1pmqeOR6hKkGf76v2qIXj8e8CXoCq8SZxN7jS5BILsF382uCBsF6Vax0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KUiqLRNS-eYJP1eaGJYxcxcZdWtg9TAKnHugN1rGCtvBr07y3HMObxT6RqPxNLPC6haaHHS80YekliN5gxKHQrVHyxSiss8TE5kO907F7gducxpThZYBMUEvo9iXWwTyE6a9luTfC1iH5fjpwVpDXwI5-iCyXoavtkcweossq4Be-kmW86JWSwhKyZQvSMRu7pwxT52Bui0xQOWsb4QrIFfXHEsgas7Ugl8HFPcrVvvnIAzuIjva7qesK_d-0HPgYio948o08Pf7KLT_MbUUYVTNBYJ35dkhFbw-7n9PM5n5kwVD1QX0coqPHmD2kPr74DO5FjushHdAi0JDLOuAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D6jQhhMusmHau6VxoqMl8Xhj1gJr1xXUa94F7uwG3KyJ2OcrYy5iflNsokNpMfyl9sEM4tYz78SPBzLihqBmpuKVvSPVkQZv0-pRe054se11JFC6Kkj_UiB51hvTuq5k21XToTAQzqgXBR2rrkCBAjJSyD1Yl_u9SnAxe_0cSo-Hvwhv5PI5GAqlIPm5_egYz-j35pkdqXkOxaCPveRmYg4C_8ob0PnlbRfxWsmr92DxzeK59W7c4oChIC8dbchRDPyXQBtYD0aXHzU7sr1e010K41fP1KS6CJOTEWyPmbaZPPWRHTBwlZIsPrC0YG48Exh_Q_zqyeIsEBSoXpavBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08feac2b13.mp4?token=vrsA-bdIB0h45HSAxHWA9rUE1ob0E1QjlhOnj3vsQ2Jbl1HW52jCRp-ItKf-1qtUTW_DKhkRACRaDxD8qxGSS_anB7Eafbr9rvFbhez9xpLURKbyHt1nHsdn2ZWVhyUJIMwTdd1D9UdBZlpauYbyewVYmcg451LZoMPe2cP_o0AdPzdeL5Mo_GkaI1S06tNlWXZpwJ_Z22xLTiDxxjerG6f7iO_O_Sqw09jMKh7f03cFoWEq4dldnWb8HWxGNxNtx492LVv9VwaFLsTL_gVUa1KSe235D-eV5EXlWFLb1uX1EQhIvzH7NuIw8lbSPcSd8RhWv8ywrgZZhS4CHt796A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08feac2b13.mp4?token=vrsA-bdIB0h45HSAxHWA9rUE1ob0E1QjlhOnj3vsQ2Jbl1HW52jCRp-ItKf-1qtUTW_DKhkRACRaDxD8qxGSS_anB7Eafbr9rvFbhez9xpLURKbyHt1nHsdn2ZWVhyUJIMwTdd1D9UdBZlpauYbyewVYmcg451LZoMPe2cP_o0AdPzdeL5Mo_GkaI1S06tNlWXZpwJ_Z22xLTiDxxjerG6f7iO_O_Sqw09jMKh7f03cFoWEq4dldnWb8HWxGNxNtx492LVv9VwaFLsTL_gVUa1KSe235D-eV5EXlWFLb1uX1EQhIvzH7NuIw8lbSPcSd8RhWv8ywrgZZhS4CHt796A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
۷:۴۰ پرتاب موشک از بیدگنه
بیدگنه شلیک موشک بالستیک همین الان
همین الان ۷:۴۰ موشک از بیدگنه رفت
دوباره از ویلاشهر نجف‌آباد موشک زدن
وحید جان همین الان از کرج موشک پرتاپ کردن
7:39 دقیقه از ملارد صدای پرتاب موشک
یکی دیگه همین الان اصفهان
شمال اصفهان یدونه موشک دو دقیقه پیش پرتاب شد
الان دوباره موشک زدن ٧/٤٢
اینجا،اصفهان یک بار ساعت ۷:۳۰ دقیقه یک بار هم الان،۷:۴۰ موشک پرتاب کردند.
۷:۴۰ از سمت ملارد انگار یک موشک زدن.
وحید همین الان از جهانشهر کرج صدای پرتاب موشک میاد خیلی صداش شدیده.
سلام وحید 7:40 صدایی شبیه به برخواستن موشک از نزدیکی مهرشهر کرج
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76030" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VQyg2mFMkjmfyr0LXos0ZQaM9ZBv-fTXw8QD589Degt24De-wcRIg2XEJV-q5NoqVZV24MNH7EjVmCZBzhYUpfaqGJG5O2utv3BCWDqgPC84yAJ51K_aTyemqWNCgkhLcnX7W7Ax3pGpSLEfrjb3j4mXTch1R_7ygYgYKNHXOrzy-E5WOAtRIkXqOmr8kED2K7TE0ANla9DWs2Vg1_T5-oDq83WHw31Qkq0J_1k863Mi7lKg5KMeiPc3Qebem3pS6QoBzKlybEdhSktx7SjdB-QmUBaoAC5bYZPJqUkZT2wJWai5h2J1u5n1ekMf91rHPvSZy973IeRSZtGj_8j8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
۳تا موشک از کرمانشاه همین الان
وحید کرمانشاه همین الان صدای وحشتناک اومد
سلام ۷.۳۰ صدای انفجار از کرمانشاه . احتمالا پرتاب موشک
سلام وحید جان
7:28 بندرماهشهر صدای انفجار اومد
وحید 7:30 دقیقه ارومیه یه صدای سنگین اومد
الان ۷:۳۱ از ویلاشهر نجف‌آباد موشک زدن
الان کرمانشاه صدای انفجار شدید
شلیک موشک از ارومیه
خرم آباد 2 تا موشک از پایگاه امام علی انداختن
از ارومیه موشک فرستادن
پرتاب موشک از نجف آباد
اصفهان شلیک موشک
سلام وحید جان از خمینی شهر یکی زدن
آقا وحید همین الان شلیک موشک از فلاورجان اصفهان
شلیک موشک از ارومیه
با صدای انفجار زیاد
سلام وحید آنلاین همین الان ساعت ٧/٣٠ از اصفهان موشک زدن
سلام وحید جان همین الان موشک زدن سمت اسرائیل از اصفهان
موشک الان زدن از پادگان پشت ویلاشهر نجف آباد
سلام ماهشهر ۷:۲۶ دقیقه صدای یک انفجار شدید اومد
از کرمانشاه ۴ شلیک، نه ۳ تا
ماهشهر حدود ۷:۳۰ صدای انفجار اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76029" target="_blank">📅 07:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIU14Z-_KarbrWrynZP6cykdcz-D5CnU_0ZEdlBe70TU6SdXj1ywfbyyqx3HziYC8SH20DhtukaKfcaNtGORsRb7QKBV5u32b4WqAN6BJUYw3K3WWGpkBbzOmc3uu3CuzaQPD3bLwy3qeNiKF2VhV7JDLw7LtmG--S7tmYajq0pYKQDZenmQACKZT_j9VJ_y0of4CAe2-U96JZsOXZ8tideJhgZZRT3IO0QmFuCMtU3rYRK5B7z5urOB_cCd-Erv86gnHhSmjWSL3-1ANimlWhTJbHmuwbgtWAnU9k2LCbEneJzJ_oVU8Oib4_hQblPwkVM09uEPhpuXt5fRNTXe2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی بعد از موج حملات موشکی ایران به شمال اسرائیل، خبرگزاری تسنیم، نزدیک به سپاه پاسداران، در تحلیل و تفسیری درباره ابعاد نظامی این حمله گزارش کرده که در حملات موشکی و پهپادی یکشنبه شب، سپاه پاسداران از «پهپادی ناشناخته» که از موتور جت بهره می‌برد، استفاده کرده است.
کارشناس نظامی تسنیم همچنین از شلیک موشک‌های خیبرشکن با کلاهک‌های خوشه‌ای در جریان این حملات خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76028" target="_blank">📅 07:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rg1uhIcUHcirweXmiww7G4iHn-_GbZpQOY2Vn8YH4hHW_G7QmgjxFCjNxpve6yvyEHqHu9wllYgD6oNEyEldi-wda9HPl9Pj8Ph9KWI5sPqDh8q8j5RBDWzGHbWyQxb9FXItbcU7WRDD51MbO84oVamcrK5Q1GLN1voLABGZzag4xuo25ks8vD702IfSpH1GBwjvFizZh5fuWKf6zwOvj1nRL3YAW4RKeTl0x30AMl8UG4eVMVLOMuH3HBRifrhSeTuoe8ehcG5sw6gw-iG5A-c_wWdjAu-nLa5i4o9504xgj6wbitIgd0rghA7FfHNYCKLhlT5ev_35hphaUOXJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یخیئل لایتر، سفیر اسرائیل در آمریکا، در پیامی در اکس نوشت: ارتش اسرائیل پس از شلیک موشک‌های بالستیک ایران به سمت اسرائیل، سایت‌های پرتاب موشک زمین‌به‌زمین و همچنین زیرساخت‌هایی را که به بخش انرژی مرتبط نبوده‌اند، هدف قرار داده است.
لایتر افزود: «ایران امروز ۱۱ موشک بالستیک به سمت اسرائیل شلیک کرد. هر یک از این موشک‌ها می‌تواند یک محله کامل را با خاک یکسان کند و صدها نفر را بکشد. هیچ کشور دارای عزت‌نفس در جهان چنین حمله‌ای را تحمل نمی‌کند و اسرائیل نیز نخواهد کرد.
سفیر اسرائیل در ادامه نوشت: «مردم لبنان، حزب‌الله به‌عنوان نیروی نیابتی ایران را رد کرده‌اند و به ایران گفته‌اند از کشورشان خارج شود. اگر حزب‌الله به اسرائیل شلیک کند، مراکز فرماندهی آن در ضاحیه به‌شدت هدف قرار خواهند گرفت. این موضوع هیچ ارتباطی با ایران ندارد. همه از این رژیم ایرانیِ دیوانه خسته شده‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76027" target="_blank">📅 07:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDM2neptRwqXsJlTXGI3dkJsf24Yny-YaX3wLm7t_HtoE9J_5KyQBsaksas6STg3ZqYNQiGzNcQ3Uk9zhzDp391wNZn4KleQy2GgFGJxR11hAEpAZtYMHL4u-IM8K1913Pn22xcupxdSAOe5X1bv5soFTqXVzISM7OXTqAq4U0omhV9JN2KThr-NTIaDH6SshRDr8HGiDF8F0FCDvcmAN_S2bvL7KA8ExHVlvC9LmZMCcnBfDDkWPQSIUz5wqOhpZwRcmycNHEqW04Tde_yXgHx44tg9hQcSgU2wZ4pXZNrG9jGXsULyFrcuUgevbrNwZ4MUkixUpYidaH-YVPTKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
یک مقام آمریکایی به رسانه‌های این کشور گفته است که ارتش ایالات متحده در حملات شبانه اسرائیل به ایران هیچ نقشی نداشته است.
نشریه آکسیوس به نقل از یک مقام وزارت دفاع آمریکا گزارش داده که این حملات اسرائیل «نسبتا محدود» بوده است.
این گزارش در حالی منتشر می‌شود که دونالد ترامپ، رئیس جمهور آمریکا، پیش از حملات از بنیامین نتانیاهو، نخست‌وزیر اسرائیل، خواسته بود در بحبوحه تلاش‌های دیپلماتیک جاری از اقدام تلافی جویانه علیه ایران خودداری کند.
آکسیوس پیش‌تر گزارش داده بود که آقای نتانیاهو به صورت غیررسمی یا به تعبیر این رسانه «تلویحا موافقت کرده بود» که این درخواست ترامپ را بپذیرد.
حملات شبانه اسرائیل ساعاتی پس از شلیک موشک‌های ایران به شمال اسرائیل انجام شد و در حالی صورت گرفت که واشنگتن همچنان می‌گوید در تلاش برای نهایی کردن توافقی با تهران و جلوگیری از تشدید بیشتر تنش‌ها در منطقه است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/76026" target="_blank">📅 07:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kcfELKgvQkhDrJaepSIejYe9D8tmauxmLgPYadU3rql8uba3uTvdDcuF1E2wOnKqRpJX2bPS7BgPa-ZbRvdFqHrVHqfnpfQYjTqKBzf_IiUkMPcR9Eyn27h5AQvnQGurf7t66BGEQ2E-jdwH8Ohp0OPRueeW8GS-rhP3JecU6e7lJxXgRKCa23M9dFS6jNIyGlYxlZk-BNvFODDfx8pSZ9mRyI017YPcN1Qm5thBX6L4FWt5sQ0Xx8Yl0Nia08Zdd2iVDdPzmCOLrbzucTfELgdKCAAF_6Fad5Xzbleivqg_Uf9ibb5lGdy9F5r18JwSllQUdXOM_dxwG9fZbSusaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل پس از حمله‌های یکشنبه شب سپاه به شمال اسرائیل و حمله‌های متقابل ارتش اسرائیل به غرب و مرکز ایران در بامداد دوشنبه اعلام کرد که ارتش اسرائیل یک موشک شلیک شده از یمن را رصد کرده و سامانه‌های پدافندی در حال رهگیری آن هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/76025" target="_blank">📅 06:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vai3Os2Bg26YdQuAHO5XgNmQNZkhgL9v0_ELsx3QXGM1pTbpsv7gsaxVpkl6UcZ2wXP84-ktApTfeq0AOVkT5am_hdKXwW6zrgIT1JvgxkxlfvnMAhqKewGcNule84DkKnaFYQbyjRQKWg95j1MKTHsoyu5YzyX91Zq3BTjVl8DqNjWRneHe2PgoN4PIaVCWdytL-ZXdeR-W303t77K88t9bGV9bPpJNHcKW--6su5HE9o0cNrC6-VrvAaaIn0ciPN4_TMHzasOzc01o-RKsVUB-oRrjs17zgiiEwVA7Pcrw6ZIfwRyxoSzdfJBOKKR7sT_b0yf-2AXcIwJkq0R-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس گزارش داد که عربستان سعودی در منطقه‌ای که پایگاه هوایی شاهزاده سلطان، میزبان نیروهای آمریکایی است، آژیر خطر موشکی به صدا درآورد.
@
VahidHeadline
آپدیت:
خبرگزاری صداوسیما، وابسته به رادیو و تلویزیون جمهوری اسلامی، به نقل از «یک منبع نظامی» اعلام کرد که جمهوری اسلامی هیچ شلیکی به سوی پایگاه هوایی در الخرج در عربستان سعودی انجام نداده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/76024" target="_blank">📅 06:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7CUryjsmSkTgGPs5slhRW5McFUyTZLfQ6VR09HheCwhQMjal9RvFbuUU2QM-hmUjOTkr2E2PXfHGDmQ89U86FZP2c7Ea0rivUGSfXcZskdi14OvcDBBno5HiO0hGQFDaXxHSnexckZzrn_gJeGy0WXsrYwU0n0XSlFsCBKJr7K3OVC22Az6chLjvA2ebg3rMytXghisokAKvyOt5iZx8APA1erZQMPQuekbMhRh1XrWz2rQwB0dAxFbY5dKXQ7toTfFyJAmy1oZVhws6zxmC0pWDUxwuWQz715fV6aU3JGLNbwCQrFAJ2ORO27euUFxvIO1gEc69l04SeC5eSippg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌نشانی تهران اعلام کرد: صبح دوشنبه دست کم صدای ۲ انفجار حوالی ساعت ۴:۴۳ و ۴:۴۵ در نقاط مختلفی از غرب تهران شنیده شد و ادعاهایی درباره هدف قرار گرفتن فرودگاه مهرآباد منتشر شده است. سخنگوی آتش نشانی تهران از آماده باش آتش‌نشانی خبر داد، اما اعلام کرد که نقاط شهری در تهران هدف قرار نگرفته‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76023" target="_blank">📅 05:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f0cplfRyFG0VbI6a0oEZqzD05bQyVo8Jw1i7YeIVPLMOtE3Eagy-T-MB5iBsLHEQ3NcGgrbWV-40OiUS9G13g8YGY0Kx2MTty5h2IxXU8QCOBHxvegQE-13sFqfYPrhRuv2FB7gNgLBjfRNDFvG7HzDda0HToUFp7BMw6CoAo0r4Gpt1v09FGBQfUElHy-_W0zoTBO4lk9WBfnILDp4sXqYOw3Lex_8IW3So9P7aUl2fpViKkEQUzvZG4QHaZT8cufATPfdUQc2SXuGp9RF2UH8KstjeUwu1n8NdEC0_zO32kxebgN3bEW7qZfvxG3BJxTw5-aV_xENTt1d-oscF-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک خبرنگار اسرائیلی حوزه دفاعی به نام امیر بوخبوط می‌گوید که نیروی هوایی اسرائیل صبح دوشنبه به ده مکان در ایران حمله کرده است که از جمله سامانه‌های پدافند هوایی و موشک‌های بالستیک در آن‌ها قرار داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76022" target="_blank">📅 05:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76021">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UoXo4XwKDxkbYKmbSyqu1RwfWNC0xf9CdadBcuT8t-P7x-6Sl7uZIEJw6I8KqPZeXfVQkGqmy-t_iZkpwc4fTI63iWQE0_D3gQ78U0XPkb-_Lj3WSsJUotbbKdFoR5i9SDxEDGLf0bz2PRnF-r9TX5vqcVYB1DMwv_od4xrBXAC7e0ei415B37qt7NSP6bBjdIBqVWs5u_g00H2OHXKg_KVbeevBr1HQuthjcACu4FSa52cOAAdg-jIkImmEDalVeWNNlBQoS9gfCQbcThHnPuBOEeKGVBccgSDRUOp46r25iY587A-a3Q_rXZuPNXF3LwRpDx6WioGfG8br1jjZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درپی اعلام حمله هوایی ارتش اسرائیل به نقاطی در غرب و مرکز ایران، سپاه پاسداران انقلاب اسلامی بیانیه‌ای صادر کرد و نوشت که اسرائیل «با استفاده از موشک‌های بالستیک هواپرتاب اقدام به حمله به اهدافی» در خاک ایران کرده است.
ارتش اسرائیل حمله هوایی به مرکز و غرب ایران را اعلام کرده اما هنوز نوع سلاح‌های به‌کاررفته در این حملات را اعلام نکرده است.
خبر این حملات درحالی منتشر می‌شود که یک مقام آمریکایی به اکسیوس گفته بود دونالد ترامپ، رئیس‌جمهور آمریکا، روز یک‌شنبه در تماس تلفنی با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از او خواسته بود فعلاً از حمله تلافی‌جویانه به ایران خودداری کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76021" target="_blank">📅 05:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KuQC7bGU_ktGq6g67VnbDwBwx3rxqjFVRnTErIrMWY3Ha2d8yj3fcjmAmyB-u06Y989gkd2kKWvJyKfcymZlVnkG5rPzqHBMWPlajCJlakanz6hbNH4BCCSnZoqWtyfS5g7waVN-K2jzlU3qXgsQzLtc_m33AHdr6gBuIdI5uEPBuwAcGD3Tr3gW9GTBBpV5Iy9jWo-9qO3b2vOyw6cKZuhCMae-AkKBs8Lu2kLrQUpZhddaMSZZBEceFTCy3snoFXEd0mXi_3G_EVIw_37cl66SPC-t82eSf7rd9Nn7s1phsK31BKEAYPEbHKNyErLRMEz0DkuDfVYtAqqWHv945w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ju4o3VOxmKDq4N-H1CHoUdN9rfO3r1abwqkMBPF_OC2tTt0BH50_Ejsaf1vad_CYJDm99efB8Z_nXX0sKyrlkU2g560pGblGtKxCuJnNn9_-RzUAZJfVLt3hd4P6IYVbG8PKLPy2nFyeM0oYSphZ0zUfsPW0iOiMkHrxhIWFAUv-_3Y0AJi9K-I4sLvOEiMmuCLECg6va_uB-fCV4hHzoCrGVfOfZe95R7HjsNpqPiazy1knxnjxncbJB-P80rG4oKIjZXdood2_AL8JEX2DCNn2MIS4oz9wc5SH0LwrojlKorIR4lJCf-YckfIj-UMwlR-h-GiDNAkb_oW44L29Rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کانال ۱۲ اسرائیل از حمله نیروی هوایی این کشور به فرودگاه مهرآباد تهران خبر داد.
@
VahidOOnLine
درحالی که هنوز ارتش اسرائیل اعلام نکرده حمله‌های بامداد دوشنبه در پاسخ به حمله‌های یکشنبه شب سپاه پاسداران به شمال اسرائیل را با چه تجهیزات و تسلیحاتی انجام داده است، کانال ۱۴ تلویزیون اسرائیل گفت که جنگنده های اسرائیلی اهدافی را در ایران هدف قرار داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76019" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SYOWki1BfQYRIJf8tGlIy-keRydGvXzUZefd7JCkYz9g8OoJXXViuYAdN7gO1S9Bp_SyJ5EuhyYfP4v9-vWB_DyKmSFr4tl7sfkeZ17_WO_aTSLppzWG4sFiqcqqgBHzAMRXU5rq03o02asddXBZGT8tByGAmami2VIbyWM8n_2z9Cs3zqmCIOsaJfYZaBJgyU67p1_PhwJXNyBbhMav80Y7Eb538jRkCH9HQe_2sjEGrcrin5HXR98WbylM2F4ncn_KL_CYRSz7Fp_tb_e2SZTV5iNdeCK4wB5Iw2-ytT3IEjyRoljLJZilSnC8w3-X2t1flslnwWMbl5E1eEkGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👆
نجف اباد ساعت ۴:۴۰ فکر کنم با پهپاد زدن
سار پیام‌های دریافتی:
کرج هستیم الان  دوشنبه ساعت ۴:۴۳ دقیقه صبح  از راه دور صدای انفجار بسیار بزرگی اومد
سلام وحید سمت شهرک غرب ۴:۴۳ دو بار تا الان صدا اومد خفیف بود
ما رباط کریم هستیم
ساعت ۴:۴۵ صبح ۴ بار صدای انفجار اوم
وحید ساعت 4:44 صدای انفجار نزدیک سمت جنوب تهران (باقرشهر)  شنیده شد طوری ک خونه لرزید
سلام،چهاردانگه دوبار صدای بلند اومد ساعت ۴:۴۳ دقیقه
سلام وحید سمت مهرآباد ساعت 4:45 دو تا صدای انفجار شبیه دوران جنگ اومد
ما شمال غرب تهران چند دقیقه پیش و دقایق قبلش صدای انفجار مهیبی شنیدیم ولی دور بود. صدای جنگنده هم نیومد
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76018" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rjGucp8JvwLBVh25gIQTb6oNsojiZ6Qw6VRMQsLWOVmqjll5Pc3T4QbCmC1NOqt3gffWul0pk4ASsGLuXHJ-3LnHnpbpWcJ8W1sR48W5gdtG2DxrBaDFmsN7BnEXgKg5KNEK-WapJfBgHFtY2o_vuO4W5AHTsBX4jiG6bhXjuZdo9PbgciJJy7mdKjulOiAAsqSoH6OnJIPXG2IJ5bFFi7nrB1iynEEj6XcVx_r5do_iPd-K8l9YUOhqJ5FNEUyuOGc3NnWS4VWLPkVtuZcdNClO0XZ0e7LSLF0ajGH9UBcTYGaPAewOpNCd_k4ySm7ojgkQCuVzlIpKUl_oJhB1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👆
دریافتی با شرح: نجف‌آباد
سایر پیام‌های دریافتی ساعت ۴:۴۵
سلام ساعت ۴:۴۵
سمت خزانه دوبار صدا انفجار اومد
صدای بمب جنوب تهران ۴:۴۵
سلام همین الان صدای دو انفجار از میدان المپیک
داره میزنننه
فردیس کرج ۴:۴۵
همین الان صدای مهیب سمت مهرآباد
ساعت ۴:۴۴ سمت غرب صدای عجیب و بلند اومد ، لرزش خفیف سعادت آباد
تهران اندیشه
دوبار صدای انفجار همین الان
سلام اصابت موشک غرب تهران تا الان دوتا انفجار 4::44
صدای دو انفجار با فاصله کرج
ساعت 4:43 دقیقه غرب تهران صدای تک انفجار
دو دقیقه بعد دوباره صدای انفجار اما دور تر
صدا انفجار داره میاد سمت غربه انگار
دوتا صدای انفجار غرب تهران
تهران زرگنده ساعت ۰۴:۴۳ صدای دو انفجار اومد
الان ساعت 4:43 دقیقه و 4: 45 دقیقه صبح غرب تهران صدای انفجار کوبنده شدید
همین الان دو تا صدای انفجار در اصفهان شنیده شد.
سلام وحید. شهرک اکباتان. صدای انقجار اومد دو بار همین الان. ساعت ۴:۴۳ و ۴:۴۵ دقیقه
صدای انفجار , کرج , ساعت ۰۴:۴۲ , ۱۸ خرداد ۱۴۰۵
صدای انفجار , کرج , ساعت ۰۴:۴۵ , ۱۸ خرداد ۱۴۰۵
کرج صدای انفجار 4:45
جنوب غرب تهران دو سه تا صدا مثل انفجار از دور اومد
صدای دو انفجار مرکز تهران ۴ و ۴۵ دقیقه صبح
یه صدای گروم مانندی اومد اما دوره مرزدارانیم ساعت ۴:۴۳ بعدی ۴:۴۵
سلام وحید جان ساعت 4:40 دقیقه رباط کریم حداقل 4 تا صدای انفجار اومد
ساعت ۴:۴۳ و ۴:۴۵
۲ تا صدای مهیبی اومد نمیدونم چی بود
سمت خیابان زنجان
زد صدا اومد شهران ۴:۴۳
دوباره زد
نزدیک نیست ولی صدا میاد
۴:۴۵ تهران شهران
وحید ۴:۴۳ صدای انفجار دریاچه چیتگر
کرج مهرشهر دو تا انفجار به همراه لرز ساعت 4:40
احتمال میدم سمت فردیس باشه
وحید تهرانم سمت شرق یه صدا هایی میاد شبیه انفجار ولی نمیتونم تشخیص بدم
۴.۴۵ دقیقه تهران سمت غرب ۲ تا صدا انفجار
سلام غرب تهران دو بار صدای انفجار اومد
سلام وحید ساعت ۴:۴۵ دقیقه شرق صدای انفجار اومد.البته دور بود.
وحید ۴:۴۲ پرند صدای انفجار مهیب حداقل دوتا
سمت م معلمم یافت اباد
همین اطراف بوده صداش همراه با لرزش بود
دوتا صدا انفجار 4.43
وحید جان ساعت ۴:۴۵ سه تا صدا شبیه انفجار سمت غرب شنیده شد.
وحید جان شهرری همین الان دوجا رو زدن شیشه ها لرزید
ساعت ۴:۴۵ ۱ انفجار دیگه شنیده شد
دومی صدای مهیب تر بود
جنوب غرب تهران سمت تهرانسر همین الان صدای دو تا انفجار اومد حس میکنم موشک بود
سلام تهران سمت شرق و غرب صدای خیلی بدی اومد
۲ تا پشت سر هم ساعت 4:43
مرکز شهر سمت ۷تیر. ۳تا صدای انفجار از دور اومد الان ساعت ۴:۴۵
وحید جان صدای دو تا انفجار به فاصله یکی دو دقیقه حدود ساعت ۴:۴۴ از نزدیک ستارخان شنیدم
سمت صادقیه تهران تا الان دو بار صدا شنیده شد
از ساعت ۴:۴۰ تا ۴:۴۵
اما بنظر دور بود معلوم نیست کجا بود
سلام مرکز شهر تهران ساعت ۴:۴۳ دوتا صدای انفجار پشت سرهم اومد ولی صدا دور بود
سلام اسلامشهر ساعت 4:42 بامداد صدای خیلی بلند اومد
صدا انفجار تهران ساعت 4:44 سمت پیامبر مرکزی
دو تا صدای انفجار مانند اطراف اصفهان چند دقیقه پیش( فکر کنم نجف آباد ۴:۴۲)
ساعت ۴:۴۵ و ۴:۴۰ دوتا صدا انفجار اومد
سمت مهراباد
سلام اقا وحید ، سمت شهرری رو فکر کنم زدن خیلیی صدای بدی اومد من از خواب پریدم
سلام وحید جان  الان
دو بار بیدگه ملارد رو زد
کرج مهرشهر
صدای دو انفجار ۴:۴۳ و ۴:۴۶
وحید حوالی ۴:۴۰ تهران صدای انفجار شنیدم
دو مرتبه بود، اولی اومد بعد از ۵ دقیقه دومی ترکید
4:45 فردیس 2 صدای انفجار از دور دست
دوتا صدای بدجور اومد ساعت ۴‌.۴۰
سمت خانی آبادم ولی صدا یکم دور بود
ولی زیاد بود مثل غرش بود
شهریار صدای چند انفجار بیشتر سمت رباط کریم می خورد باشه
درود وحید جان ساعت ۴:۴۳ دقیقه ۳تا صدای انفجار توو پرند شنیدیم
سلام ساعت4:42دقیقه صبح صدای انفجار در اشتهارد شنیده شد 2مین بعدش هم بازم صدای انفجار صدای بمی داشت
سلام اقا وحید من اسلامشهرم با صدا انفجار بیدار شدم
صدا صدای زدن بود،سه تا انفجار شنیدم
وحیدجان سمت شرق اتوبان بسیج صدای 2تا انفجار اومد ساعت 4:45
رباط کریم صدای شدید انفجار
چهار پنج تا
غرب تهران ۴ و ۴۰ صبح صدای دو تا انفجار اومد اولی شدید بود از خواب پریدم
ساعت ۴:۴۵  دو بار صدای انفجار اومد کرج
تهرانسر ساعت ۰۴:۴۳ صدای انفجار شنیدیم و از خواب پریدیم.
اصفهان چند تا انفجار شنیده شد
ساعت ۴:۴۲ دقیقه، از سمت غرب تهران دو تا صدای تک انفجار اومد. یکی دور و یکی نزدیک
درود صدای چهار انفجار شدید اومد ما سمت نسیم شهر هستیم جوری بود از خواب بیدار شدیم
ما نزدیکی اکباتان زندگی می‌کنیم و توی پنج دقیقه ی اخیر سه تا صدای انفجار شنیدیم
کرج صدای انفجار میاد
قطعا حمله شده
رعد و برق و غیره نیست
اصفهان دوبار صدای انفجار 4:42صبح
هیچ صدای جنگنده یا موشکی نیومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76017" target="_blank">📅 05:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پیام‌های دریافتی از ساعت ۴:۴۰
سلام وحید جان
4:40 دقیقه انفجار از سمت سپاه تبریز طرف متظریه اومد
۴:۴۰: وحید ارومیه یه صدایی اومد نمیدونم چی بود
صدای انفجار شدید در ار‌ومیه
مشخص نیست صدای چیه
سلام آقا یک صدای مهیبی همین الان از ارومیه اومد ساعت ۴:۳۹. شب هم البته چندین تا موشک از اینجا فرستاده شده بود.
سلام وحید ارومیه ساعت 3:39 صبح صدا اومد و انگار زدن چون خونمون لرزید و دقیقا مثل موقع جنگ بود
وحیدجان نجف‌ آباد صدای چند انفجار شدید. ۴:۴۲
وحیددد
دارنن  اصفهانو میزنن
نجف اباددد  سمت ویلا شهر
دوتا زدن همه جا ترکید
لرزید داریم سکته میکنیم
شاباد موج انفجار شدید
سلام وحید غرب تهران صدای انفجار شدید اومد همین الان ۴:۴۳
وحید اینجا صدا انفجار اومد ۳ بار
خیلی بلند و نزدیک. ما کامل از خواب پریدیم
بدون صدای جنگنده بود.
نجف آباد اصفهان
خمینی شهر دوبار صداری انفجار اومد
وحید زد الان تهران رو
یوسف آباد ۴:۴٣ صدای انفجار از دور شنیدیم.
مجدد ۴:۴۵ صدا اومد.
۴:۴۲دقیقه همین الان دو انفجار پی در پی اسلامشهر
انفجار مرکز تهران ساعت ۴:۴۳
وحید زدددددددد
بالاخره زد
همین الان ۴:۴۳
غرب تهران سمت جنت آباد صدای وحشتناک اصابت موشک یا بمب
صدای جنگنده نیومد
دوباره الان ۴:۴۵ دومی  رو زد
توضیحات اینکه چند دقیقه قبلش برق نوسان شدید کرد
صدای دو تا انفجار همین الان نجف آباد اصفهان
انفجار لرزش شیشه صادقیه تهران
غرب تهرانسر یدونه صدا
اسلامشهر همین الان صدای انفجار مهیب شنیده شد
سلام ساعت ۴:۴۱ صبح، صدای انفجار شدید تو تبریز اومد، جوری که از خواب پریدم، قطعا پدافند و اینا نبود...
وحید جان از سمت قروه کردستان صدای سه انفجار شنیدیم با فاصله ۱۵ دقیقه، به نظرم موشک خوردیم چون لرزشش زیاد بود
سلام وحید جان
ساعت ۴:۴۴ صبح اسلامشهر مرجان آباد
۲ انفجار شدید پشت سر هم
جنت آباد جنوبی صدای انفجار - ساعت ۴:۴۴ صبح - ادامه دار نبود در حد دو سه تا بود
۴:۴۵ مجدد زدن
ساعت ۴:۴۴ دوشنبه صدای ٢ انفجار با فاصله ١ دقیقه از هم غرب تهران
الان صدای دو تا انفجار شدید اومد . اصفهان
سلام از انديشه
وحيدجان فكر كنم ٢تا صداي انفجار بمبي اومد اينجا
صدای انفجار از دور
غرب تهران ۴:۴۳ حدودا
ساعت ۴:۴۲ دو تا صدای انفجار توی قائمیه اسلامشهر  اومد
پشت سر هم
آنقدر شدید بود شیشه ها به شدت لرزید
ساعت ۴:۴۲ صدای انفجار خیلی خفیف شمال اصفهان
انگار خیلی دور بود از ما
فکر کنم ۳ تا بود
اسلامشهر ساعت ۴.۴۴ دقیقه صدای  سه تا انفجار اومد
وحید حان مرکز تهرانیم، ساعت ۰۴:۴۴ صدای ۳ تا انفجار شنیدیم.
وحید سلام. صدا دوتا انقجار ۴/۴۱ نجف اباد
صدای انفجار فردیس
وحید نجف اباد صدای انفجار بلند  چند تا شیشه های خونمون لرزید مثل چی
بیدار شدیم ۴.۴۳
یه جارو زدن داره مثل چی ازش دود میره سمت همین نیرو انتظامیو اینا که توی جنگم زدن
الان صدای دوتا انفجار اومد
شیشه ها لرزید
مثل صدای لانچ موشک بود
شاید جای رو زدن ولی صدای جنگنده نیومد
خمینی شهر
سلام نجف آباد الان صدای ۱۰ تا انفجار اومده و جنگنده
سلام نجف اباد ساعت ۴:۴۲ دو تا انفجار خیلی بزرگ کامل مثل وقتایی که میزدند بود. صدای زیاد و بعدم موجش اومد
سلام وحید همین الان صدا انفجار اومد سمت تهرانسر در حدی که شیشه لرزید
دوباره الانم اومد ولی دور بود
4:41 صدای انفجار اومد
04:44یکی دیگه.
فکر کنم بیدگنه رو زدن
چند دقیقه پیش تو استان کردستان شهرستان قروه سه تا صدا اومد آسمون صافه ولی اطراف رو زدن احتمالا
غرب تهران صدای انفجار
مجدد
وحید داداش صدا انفجار کردستان
سلام كرج ٤:٤٣ صدا انفجار طوري از دور اومد. رعدو برق نبود
بازم الان صدا اومد
ساعت 4:42 صدای انفجار خفیف و لرزش زمین سمت صادقیه تهران
4:44 صدای دوم شدید تر بود. صادقیه
توهم زدم یا صدا اومد؟ سمت ملارد
زدن وحییید زدنننن
انلاین شو وحید بد دارن میزنن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76016" target="_blank">📅 05:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76015">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYETQt0dDP0fALoCWTVr3sYA8Gp7F3SqWS8JJq5uwkuNe4B2BD-IxD2ouZQ9GhuMCgtIcb5kPamLCqrVCmXEjTpDVcFOYz2LRylyAnReagXdtE_S_MGsgqcB_KQhmFP4jqRcnTiThCckXx1UGg_GAilRMqMtmYeacRgMohzmQOcaZshZ8jET5ZNLK78WzZqqxL8ylDPeV4NkW5oqT6OQs-qjFNSpOQyaoKcKKfA_3TLuLDle9Jb4nP2yyvmrYjdcw8EpTmtHSzzYEaFjPACaP1btH7vnc40YPvqyV7UA2yFI4ZQsKKlXWWu4QLHaxJweCp8RfLVfKLN0jU7eIG4PKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل با انتشار بیانیه‌ای از حملات هوایی به چند نقطه ایران خبر داده و گفته است: «نیروی هوایی اسرائیل، تحت هدایت رکن اطلاعات ارتش، اندکی قبل به اهداف نظامی رژیم تروریستی ایران در غرب و مرکز ایران حمله کرد.»
پیش از این سپاه پاسداران هشدار داده بود که در صورت اقدام متقابل اسرائیل با شدت بیشتری واکنش نشان خواهد داد.
جزئیات بیشتری درباره ماهیت اهداف مورد حمله، میزان خسارات یا تلفات احتمالی منتشر نشده است.
این حملات پس از آن انجام می شود که ایران ساعاتی پیش چندین موج حمله موشکی به شمال اسرائیل انجام داد و سپاه پاسداران اعلام کرد این حملات آغاز یک هفته عملیات مستمر خواهد بود. همزمان، مقام‌های اسرائیلی هشدار داده بودند که در برابر حملات ایران واکنش نشان خواهند داد.
این تحول در حالی رخ می دهد که دونالد ترامپ، رئیس جمهور آمریکا، در ساعات گذشته از بنیامین نتانیاهو خواسته بود از اقدام تلافی‌جویانه خودداری کند تا روند مذاکرات و توافق احتمالی با ایران آسیب نبیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76015" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd9OLI_RFj2II-T0ECFUfguZ2wlJVnrOzDVmv8ldWkvRyeyYqzzNIf1ySmW4qhn6W26YFQ8yCexrwsFNSbEwOKYq4ZqFDq0LANbxHbJI-ObTsawzLkxRrD3ycx-g-tfOqpQXcEd0hYHlfXTXeRsqgHkHOQtAwvSAf8fGvbd8mlm-vRkSzIQGyXH1Lb4W1J3kvp04MptqkNFaSBGpaPR5Qf2kxfv-uKdrizSaQNoR7S9IxSXvw89TWjVfZYY0PXuzN33QrKMHYYQAOOFKjPuz1wjvqBa8brhe37e49QWkcTHGSNBs2DiUktAv0yIb9OSS_tlA3B0slhjSZETdXtDSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه‌های رسمی ایران از شنیدن انفجار و حمله هوایی به چند شهر ایران از جمله تهران، اصفهان، تبریز و نزدیک به کرج خبر می‌دهند.
bbc.in
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76014" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH6rIo4K9kk68BZK5XwTUJEPdEiDYINTjt1s7z2hjavAiCux5njoqoxkVj3pHpjIMq8FMPIYXGG5l-8Dq9-9yyOfSZNfmepAXin9N9AOmec6gVt6dF9-c0brV7oVaUFnEh_fuOtLo89EsJZNmAN8HxaO2UMw3XPTUbHQPP6mN8k9UtU62eNgjSL157QECtmQt3dPqPBgb_lPIdDGU8fJugh7RrYni37ZqCjHic_RSFhZytrB7QxHPHM1o76ZJzOV-mHUU4eYVH8vPvQFV5IgONIZcFl3nMrPYyW2u797jq9ktkOkWu0YXz1BhoXXUJeJH8kBR-RnGRuyKQRWdQNHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در تهران، اصفهان و تبریز در بامداد دوشنبه خبر داد. خبرگزاری تسنیم از وقوع انفجار در کرج در بامداد دوشنبه خبر داد. ارتش اسرائیل نیز اعلام کرد نیروی هوایی این کشور «مدتی پیش» اهداف نظامی متعلق به «حکومت ایران» را در غرب و مرکز ایران هدف قرار داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76013" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zjbp0l-MAoGNS49_H2DcwqDqtrUVPyO4EmOqJIh7y7T8riHu9xhGGdgNY6o5wPNOZ2kVD4vmV_xMcxbPc1Y2ebLnZMlqMJTznQwEt1kb5_YCObO9F6uPw0grqSXz5bLHQr-1QyhaRIju_b02-FnH8ZrylO3SsrhGATQuW8da_J5SkIVGof8yw44smgcV04Pmlf_XsVwx68ZMsyKZwK_bp6ZwFQ_8i2Xz5ICkzB37u9GZBG16-Vv7GkQIP0oaecx1-iVr9iSAco4iph_0OpTxoKTI7-AERiqVq3Y2Ek5iNxSfTGYGpbo0SWfPJkjdtYwO_XUKei2QMN68nS_ALPA12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش اکسیوس، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با درخواست دونالد ترامپ، رئیس‌جمهوری آمریکا، برای به تعویق انداختن پاسخ به حملات موشکی بالستیک ایران موافقت کرده  تا به واشنگتن چند روز دیگر فرصت داده شود تلاش‌های دیپلماتیک برای دستیابی به توافق با تهران ادامه یابد.
بر اساس این گزارش به نقل از یک مقام ارشد آمریکایی و یک مقام ارشد اسرائیلی، ترامپ در تماس تلفنی یکشنبه شب از نتانیاهو خواسته از انجام حمله تلافی‌جویانه خودداری کند، زیرا به گفته مقام آمریکایی، او معتقد بوده «ما به انجام یک توافق خوب نزدیک هستیم».
طبق این گزارش، نتانیاهو تلاش کرده با این درخواست مخالفت کند و ترامپ را متقاعد کند که اجازه حمله به ایران را بدهد، اما در نهایت «تا حدی به‌طور غیررسمی» با درخواست رئیس‌جمهور موافقت کرده است.
این مقام آمریکایی گفته است که این گفت‌وگو بسیار آرام‌تر از تماس پرتنش هفته گذشته درباره طرح‌های اسرائیل برای حمله به بیروت بوده است؛ زمانی که ترامپ به‌طور علنی اعتراف کرده بود بر سر نتانیاهو فریاد زده و الفاظ تندی به کار برده بود.
پس از این تماس، این مقام گفته است: «فکر می‌کنیم رئیس‌جمهور کمی زمان خریده است. او بسیار قاطع است که ما به توافق با ایران نزدیک شده‌ایم. فکر نمی‌کنم در حال حاضر حمله اسرائیل قریب‌الوقوع باشد.»
او همچنین گفته است: «ما در یک لحظه حساس هستیم — چرا باید وقتی در راند چهارم هستید، یک توافق احتمالی را به خطر بیندازید؟ رئیس‌جمهور فکر می‌کند سه ماه است درگیر این موضوع هستیم و اکنون زمان پایان دادن به آن است.»
با این حال، هنوز تصمیم رسمی در اسرائیل گرفته نشده و طبق گزارش شبکه ۱۲، نتانیاهو تا نیم ساعت پیش همچنان در حال برگزاری نشست با مقامات ارشد امنیتی درباره این موضوع بوده است.
@
‌VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76012" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76011">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mGmsNKXR4Gc9MctTY_I95WvYcIV5_xtlPqkF_jvJ-4N1hFzmZ4r99HG-4GzrWpOQhahHqhjjHrb2GkdsazaMxowUiu0A95rFk4m_cz2Rq45fmWJ1h7t5kdgWuF7irmpSiJDvkyv4AA6yDwEeUkRXURMMpXajNvJd_YwFoyTVSeXSJf17A90uMdsZvr0QgQAeRGcRRR4IUNb1RQZyRY7yI56VMHAQPUb_p2YwzWGjFhBZmK_GrSD7uYnA3oYZ9GnGoEV5HUDpyI6VyUyJ_BNKx0mAJgYzjCtcu_xG51fzfs4sS0j5DwsGpn9oep9EA-oZr9t-Wur1wjqvgG1YzIyLag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید هر توافقی که او با حکومت ایران کند نخست وزیر اسرائيل خواهد پذیرفت
رئیس‌جمهوری آمریکا در گفت‌وگویی تلفنی با فایننشال تایمز گفت که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، چاره‌ای جز پذیرش هر توافقی که آمریکا در مورد آن با رژیم ایران مذاکره و نهایی کند نخواهد داشت.
دونالد ترامپ گفت زیرا «تصمیم‌گیرنده اصلی رئیس‌جمهوری ایالات متحده» است.
دونالد ترامپ به فایننشال تایمز گفت: «او (بنیامین نتانیاهو) هیچ انتخابی نخواهد داشت. این من هستم که تصمیم می‌گیرم. همه تصمیم‌ها را من می‌گیرم. او (نتانیاهو) تصمیم‌گیرنده نیست.»
به گزارش فایننشال تایمز، آقای ترامپ این اظهارات را اندکی پس از آن مطرح کرد که جمهوری اسلامی در جدی‌ترین نقض آتش‌بس از زمان توافق آتش‌بس در اوایل آوریل، چندین موشک بالستیک به سوی اسرائیل شلیک کرد.
آقای ترامپ تأکید کرد که حملات موشکی جمهوری اسلامی تغییری در تمایل او برای به نتیجه رساندن مذاکرات میان آمریکا و حکومت ایارن ایجاد نکرده است.
او به فایننشال تایمز گفت: «این موضوع هیچ تأثیری بر توافق نخواهد داشت.»
ارتش اسرائيل به صدای آمریکا گفت که جمهوری اسلامی یازده موشک به اسرائيل شلیک کرد. ارتش اسرائيل پیشتر گفت که حملات موشکی جمهوری اسلامی را دفع کرده است.
در همین حال در واکنش به حملات موشکی جمهوری اسلامی، ارتش اسرائیل در بیانیه‌ای به صدای آمریکا گفت که رئیس ستاد کل ارتش اسرائیل، ایال زمیر، در حال ارزیابی وضعیت در مجمع ستاد کل است. ارتش اسرائيل به صدای آمریکا گفت: «نیروی دفاعی اسرائیل به محض صدور دستور، با قاطعیت به دشمن حمله خواهد کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76011" target="_blank">📅 02:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76010">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرگزاری تسنیم: "صدایی که دقایقی پیش در تهران شنیده شد مربوط به رعد و برق است و این صدا ارتباطی با پدافند یا موضوع نظامی نداشته است."
من هم پیام‌هایی گرفته بودم که بعدش با «ببخشید انگار رعد و برق بود» آپدیت شدند
.
زیاد پیش میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76010" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76009">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NeEOa4mBluq8Mwty44sQMOOEfYQQf7EOrao3R2rx5gSxcsCTIk-6VaSqtT_hdF2FaPVJK9e9VEtqFOZc_PQ_La2_FNq5nEXwrjiW8UUTjn3EXAgpInvIJkUvo9gjM9eEowV8oABuQet-XTW_GwwCn0OW7Q81583PO4WYQsxB40HiLRTsqEDOOZbK2pHE9hi7dPve_RkUv07DtkvMuOmXB7GVkeRsIp5Ur5q4o7p0p20sAJ4lJz5SGF0n_fLeL-IPQT7yGCNaUGcH5kyb3qFeF9FMzcnf1-YSgOF88_7Jyj__yQdOLnJhlkIJxoepR1V_4fC8oretlbbYaLh_GzPWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">shamidartii
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/76009" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76008">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qli-5Edgp6gF9KC7yQnHskLqGtEtDYEIavdgZqfpUaAjH3SXHbnc1gQYE5Jk_LtX7Hym3QdM7U5FaLXfFCfgDZp2ANnnwn8jmVAphbWmrXhqf0p6dCDj0RAefyQFVGusoYqCxQEhNvavUcv6B2UfxjqaL_6sxOgucDaiqoOq8XFzoLtV-rEPbqN9BCrzWByIfzT3UhUk5L27WMRuJYZtA18AJIiIUYCyhrSmC-J22VgFnKRdhZFJauhDDSGmUQbbIKzKlibJrPAwXcVcWDQ3JODds5lfn082xV4tdVChSUGI3KxRIRwgko4HB5q_YrpiM7ReJEstnHqZTSOqTm_WAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با به اوج رسیدن نگرانی از آغاز درگیری مجدد نظامی میان ایران و اسرائیل، سازمان هواپیمایی ایران اعلام کرد تمامی پروازهای شهر فرودگاهی امام خمینی از بامداد دوشنبه ۱۸ خرداد تا اطلاع ثانوی متوقف خواهد شد.
در اطلاعیه این سازمان آمده است: «مسافران از مراجعه به فرودگاه خودداری کرده و اخبار بعدی را از مراجع رسمی پیگیری کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/76008" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
