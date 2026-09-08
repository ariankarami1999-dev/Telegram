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
<img src="https://cdn1.telesco.pe/file/dlIAK319fV7Z8hJlbu8Yeo8wT8bN6f1usvCg8wg0n_YgO6mOh-y62iySK-wSeCchSDm0pgDEICbzFp_8MKc9i1HUHdFwsnkQW0X5u2_tXoaSu48KY86NyL3nJ2iroT14J0egcgIPlTuPwQiidcpK7Pg6Wjlp_pRX1TNeomF8P2FFj5D5C5c1SzmdhoepuXXrS6t6r2UjVplFBLUMHHsIfepDuyUTVPjekPfoYgOuszy3BnXjlqtDOhFqQ3-Bmk43bjbaymDDY_7DMl6ti__IRfcKlsPV9rjlyfYMcxqKc5zVmv1sQVEhzxzRajgkZAxKNy8gc16Ea3OpoBmtTQouqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKVfB-wwZIu41M4Y5hR3bEGdL8-mkqXc6PM3qQN1Qh83FX9G5mSbj9EqkhfAUzM1TMTQoUMXgfPOUyyQgQiquffIugrjXnWYBEkd3d_5w6CuUJokA2aVdt5Ep-YGaeIbFJ9wNWPyh4f-vnytfgTLOWnnDwjU-Wg_mVDVxPS0O1Zot1_eXqgvHeFM57bgKaT6FP7VbAKn3aPFW9rGhhg3gHSO-p4Fbgle6yRxuTgXEP6q2qgzscMDSk0t7I6D-QPzhdjsMRSgsBzyXw2cqisfT2-d3BrGzuOLzhmd6zB8ieoz1DBwIQM_yX6aO6TWUnQUustZVhp4XwMW0GO3pBIYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا، روز سه‌شنبه ۱۷ شهریور ۱۴۰۵، اعلام کرد در چارچوب «عملیات طرد اقتصادی»، ۳۶ شرکت و فرد مرتبط با بخش هوانوردی ایران را در فهرست تحریم‌های خود قرار داده است. این اقدام شامل ۲۷ شرکت هواپیمایی فعال در ایران و همچنین شماری از شرکت‌های واسطه، نمایندگان فروش و ارایه‌دهندگان خدمات باربری در کشورهای ثالث است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/VahidOnline/78277" target="_blank">📅 20:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M6uziUzW5jqU22NKAFMO5pvWVWWhvNJkAk9OAdM87GKVvcv4MCK8lYhobNr2pn8lLiE-GwH-mcJ28ZyGcUwK3F96heVdgFoplGwG-YJ03rxnACb5Hl_sXHAsVNFaMp6zHc6HsF4EWJxvNImVive1VSPEQIUYZAXsQseit3TmamiAoep6BJKTQAcF67GY9mDPTxWvYJ8q7wlCVKc7KlnBaOBO71oNsERCw5riXMBW3GFbz95CdsMWiL-vNegQ8x2flwAgi2lo25XMVW9eKOW9fjoFclXxGxeWZLViMBaRsFRP8muf_m0cm23pEzJP3sbC4Hn2f_JDCcnYtkML2-WO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kCgK3G8SSqPKveljTKpWN5oSb81Kg_OYeUKiunHkIhAqVhMlN3_wLUEqF-X0PTFShoSHbeUMwhjkxSf9rWCWTHijjnkYBMuilxQAjSJIAfEsyCIkfj3b8bE6KtoASc4YBSXq3mjl6-UwxD1b5tC9bhzKxiHmp5_nqg-Bo1kuXFruZklazFinUF_FihJEFwvOm6veZQEhnXB2iQKPDTf24w5nvhTQvnab6WuYkein6oabl1eMJjJ1KesraFVYA2dqofWFTv5fiLbrR0XXXwvG5EaGvBcppf1mEeVE0NsrbhOHmka-zomOgNRDbSEZyi9rj6yC9DCzHccdPtmN9v7hZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک زیردریایی بدون سرنشین متعلق به ارتش آمریکا را در محدوده آب‌های تنگه هرمز توقیف کرده است.
سپاه پاسداران توقیف این زیردریایی را «غنیمت گرفتن» توصیف کرده و اعلام کرد که تا ساعاتی دیگر تصاویری از آن را منتشر خواهد کرد.
این زیردریایی هوشمند حدود ۵۸۰ سانتی‌متر طول و نزدیک به سه تن وزن دارد و می‌تواند تا ۱۰ روز بدون نیاز به بازگشت به مرکز هدایت، عملیات خود را ادامه دهد.
@
VahidOOnLine
روابط عمومی ارتش جمهوری اسلامی ایران، روز سه‌شنبه ۱۷ شهریور اعلام کرد که یک پهپاد MQ-1 در آسمان بندرعباس شناسایی شده و با شلیک سامانه پدافند هوایی ارتش، سرنگون شده است. این پهپاد تهاجمی از سوی ارتش آمریکا مورد استفاده قرار می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/VahidOnline/78275" target="_blank">📅 18:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgwMjuANJ9yUzCs96q6eN17XzVtXO0jFvoX1eEQ7ngzwq3FncLUWpIKzVeN3R70PCWPQ1teOFSgHies7QGJBw1Uxp5ucljSbgT9zZYbH0XUIoDqZL0OwaIw4kFt9MQBU4-DYQzKDBkozK1ErhkkZ_7mNLoHbKuWHuQiBMDX_rWQSytQKIDZZdu5lnNuNxgK0k7jXk8KlhOSV6rsLqdhgJveLpSUO7JsVFGQ6kN_uyzOKpSwWMtFqD5Cq9awbvpWBtqT0C6_X2QQ7draoHwrXo5GCjgwJGbWuGvHtANK9_awDQR-d4_v2v5PHx4tt3-EYx0zdVd-XqRRRdZPJXhTU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبدالرئوف اسحاقی، فرمانده حوزه مقاومت بسیج پارود در شهرستان راسک استان سیستان و بلوچستان، روز سه‌شنبه ۱۷ شهریور در جریان حمله افراد ناشناس کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/VahidOnline/78274" target="_blank">📅 18:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KOpGa5ul3cYV3OWvvUKJOupYgjJlkNzkHTmmFX7w3hkhMt4K8B8kSj879D67icY4S6yRkVjM9HoM70JN8KYMxg3_MvDhwqH76PD8X-XuIJ1PdA9dJbDbXV2UWEzDegSZ-h-jpJS8T0CKDoOspKwFi7u_rXix3JUCV7s5vbRLdBV7OjKcaDW27w4W9IkbmWE7RFEma_vOkDY_e_OD4yAPgGMBtoRmMOQ1YawGApMp7xzGt1v7hzxOMSOFx0ErrKvo1RdY6q7XsKzfKzVQovOfCAZkcHoPdOhRhrDUnJbr0CYS5LdGh1aBPyFKKYmiC4ZyypElnI_N-d4eC7pk8E196g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j8WymiYBW8LYWFkXX8M6hP_69vxy6CMaTISFPqYQP84zpqdX8x5S1G6r6mlfz2DdnbzsxLQwvy3JNCwsCZroqrXJ5BY-ofGzSXduRP0pFKW6CL5FD7m-62bWgJ6SqxOcl26_7G2P3K9QkgglTEaf5nLJv3XBnab3srTYNtvLgeKsdxOMj99v02dbyhArAKLHYpfqAswFhBkv7Wj11TevXA3jX4q7b7nZ1tWNqeGsNpMEtM3TUHcnQnTl945oUv0iUefWR8SY21vAKPrSar6nTKAUPs2QPH8bJkh5w1OKkFSYjrC-e26h36T2T9aa6s7RLGKVIedlCkt3yE-npbsUJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/urUEtt4GubzGTphlZQ0tL6g0ReCaRmuHfaje0ZpmKkZj7C6PFa9XVJ95XNv8ppooKWJe4VTrZjNVTCJWnolqedEnalLTdQRktpSv2n_79Z4fFnB3jcbfGh2MS0w8XZQNq7pML2chf3BSBMkgfwj4ZomUgH0zskqZmhHLrghiOpIy-iDRiP-llRv6Kl1GT0Ng4LTi1nlvY0enuP13GftlZ97caMUy5_RpsKY2EgmCdWZKqTMrqc5rAto8ZhbztQkh0XeY308zSWWM0rt15DDefRSGXoqyCASvm2JV0EstlE0qnd1Z2su0ssX7ISSNXB7vHH4Ejkc9vMpbZLe-eeOYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MrXz2c4TvaVZ04ANemWaQv5-WkS-S8NSUKwCbnHlIiiixuulsQ7mIbQS6vhETYhvbTmgUwX1drM37XBmefeEpRwXxPVIGC0tqzwz44-zjef4JJViMY4Ph1JkcC2wCzmp-KT9u8BYakakGFg3v3ctcoNXIZIDz66F51fEB_OXgN8s7SCkq2baP9yuhuVucne6WXzxFRfh-boAW3JR8S52tZszbQPg7snc3fGBNfCA3L7QSuFR74F6diGkjkCt_Yljl_bkZSG_TstnYp0gZkxbFrykwoQBrDIfBkUu6F1G6Z_otrllYyZk09p0ttgnXkhMhmRvXdgKh4SCvzjQjYJmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f_3Ftf-zrwkhV7tXR9kcNF9qcIGyW_MvvaUrhCKXcJUB21CbscHIrgD8_AoBizWMMjBDuQRBmQlcwt2PNafJrYyKLG1yQUCpV0LnrDLxyVdsEPFi1OUL9553hguLL_qg6IYdCS5DugY3Q2C94MG7eMZ0514ShrMgR70IxaH96Hvl7NTuEgNrpVwOQhuEm6zQaWnSZbr6qUBeRFVwCUUxAW8IkOKCg_d12c8r1bXDNH7cAHVQVy5y9TCa3oUCbF77OHCKvVjW8Z8keiNHlVCgDlNd5NeYpWlIy4l8d1lo2WOPigeXdTfoECB9Nx-bJn39b8GL70PqODozB3342lNrCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=Hp6FXgdHIbVk_amcb2Wcaf7_dUGaxRPBhCcBdNNgXL5C42GHpL_75L0boalkAqUKlLHHvNrYbmWQ5LpDSMwqRR6oGT6Mp8tAZ3PUEMG7qsfkB_VrdObnnkmVhRakE08TH8ZN58pXzYuxYeu79XuU9XBdPqqJHwho-VarJuBCr6q4X-Wm5U-CER9y-Q4_cG3XibZDFG0y6Ll8iIF-nkkTbo7shiqnR5gTKsYqXm84l7-rgNY3by4E0z3vRe3vXU9m8UY6svsdQo98SquMWA-HN9mhAnh2XYKDAuOi3XR58Si-N4qEOK7s5pWWLPykx6VvZ4dSVuUBjbGhx8aj8QwafQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e0b5c1294.mp4?token=Hp6FXgdHIbVk_amcb2Wcaf7_dUGaxRPBhCcBdNNgXL5C42GHpL_75L0boalkAqUKlLHHvNrYbmWQ5LpDSMwqRR6oGT6Mp8tAZ3PUEMG7qsfkB_VrdObnnkmVhRakE08TH8ZN58pXzYuxYeu79XuU9XBdPqqJHwho-VarJuBCr6q4X-Wm5U-CER9y-Q4_cG3XibZDFG0y6Ll8iIF-nkkTbo7shiqnR5gTKsYqXm84l7-rgNY3by4E0z3vRe3vXU9m8UY6svsdQo98SquMWA-HN9mhAnh2XYKDAuOi3XR58Si-N4qEOK7s5pWWLPykx6VvZ4dSVuUBjbGhx8aj8QwafQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عرفان میرزایی، خواننده رپ ۲۱ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان دستگرد اصفهان جان باخته است.
درباره چگونگی مرگ او دو روایت متفاوت منتشر شده؛ ایران‌وایر از اجرای حکم اعدام و ایندیپندنت فارسی از مرگ بر اثر شکنجه خبر داده است.
بر اساس گزارش ایران‌وایر، میرزایی پس از شناسایی در ارتباط با اعتراضات بازداشت و با اتهام «محاربه» به اعدام محکوم شد.
این رسانه می‌گوید حکم او روز یکشنبه ۱۵ شهریور بدون اطلاع قبلی خانواده اجرا شد و تلاش نزدیکانش برای جلوگیری از اعدام نیز نتیجه‌ای نداشت.
ایران‌وایر همچنین به نقل از منابع خود گزارش داده است که خانواده میرزایی پیش‌تر برای خودداری از اطلاع‌رسانی درباره پرونده و حکم اعدام تهدید شده بودند.
به گفته این منابع، آثار متعدد جراحت و کبودی نیز پس از مرگ بر بدن و صورت او مشاهده شده و پیکرش با محدودیت‌های امنیتی در روستای غرغن فریدن به خاک سپرده شده است.
در مقابل، ایندیپندنت فارسی به نقل از نزدیکان میرزایی روایت متفاوتی از مرگ او ارایه کرده و نوشته است که این جوان در نتیجه شکنجه و ضرب‌وجرح شدید در دوران بازداشت جان باخته است.
خانواده او گفته‌اند هنگام تحویل پیکر، شکستگی‌هایی در دست‌ها، پا و لگن مشاهده کرده‌اند که آن را ناشی از بدرفتاری در زندان می‌دانند.
بر اساس این گزارش، میرزایی اواخر فروردین ۱۴۰۵ در یک ایست بازرسی در شاهین‌شهر بازداشت شد؛ ماموران پس از بازرسی تلفن همراه او و مشاهده ویدیوهایی مرتبط با حضورش در اعتراضات، وی را به زندان دستگرد منتقل کردند. نزدیکانش می‌گویند او در ماه‌های بازداشت برای گرفتن اعتراف اجباری تحت فشار و شکنجه قرار داشته است.
دادبان تاکید می‌کند، تفاوت جدی میان دو روایت درباره علت مرگ عرفان میرزایی، ضرورت انجام تحقیقی مستقل، بی‌طرفانه و شفاف درباره مرگ او در بازداشت را دوچندان می‌کند. اصل ۳۸ قانون اساسی شکنجه برای گرفتن اقرار یا اطلاعات را ممنوع و اعتراف حاصل از اجبار را فاقد اعتبار می‌داند؛ ضمن آنکه هر مرگ مشکوک در زندان، به‌ویژه همراه با ادعای شکنجه و آثار جراحت، مستلزم بررسی موثر و پاسخگویی مسئولان است.
dadban4
دو منبع به ایران‌اینترنشنال گفتند دلیل جان‌باختن او، شکنجه شدید در زندان دستگرد اصفهان بوده است.
اطلاعات رسیده حاکی است پیکر او هنگام خاکسپاری، آثار متعدد شکنجه داشته و دست و صورت و لگن‌اش به شدت متورم بوده است.
بنا به اطلاعات رسیده، ماموران امنیتی به دلیل ترس از تجمع مردم، اجازه خاکسپاری عرفان میرزایی در اصفهان را ندادند و پیکر او روز دوشنبه ۱۶ شهریور در روستای غرغن شهرستان فریدن به خاک سپرده شد.
زمان دقیق بازداشت عرفان میرزایی مشخص نیست اما منابع می‌گویند که او در ارتباط با اعتراض‌های دی‌ماه بازداشت شده بود.
بنابر این اطلاعات، ماموران پس از بازداشت، ویدیویی را در تلفن همراه میرزایی پیدا کردند که درگیری میان معترضان و نیروهای حکومتی را نشان می‌داد و از آن به‌عنوان مدرکی علیه او در پرونده استفاده شده است.
iranintl.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/78268" target="_blank">📅 16:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx8oihzi8plpwSrtrT8JeXS8JfGdROM9zNqDQs3gGQ37Qe5DaFpJmrh-xtCHVzUnHi6CBav5wuXN4BttTCKxkOz4ylp0J9JvAASMjnD-GK3vLaAKkT-Dqc92reouTCa131HA0kc461ODOlbIBLcs_4EX9lYA8agmlgtR60PaAwvMUH3u_Mz0EKRr7Ak0CzQ6Cc2Cw8fL1Q958Vv5N5Ne4W_8che9vbq6B0jZqk2QHWFHGQXuZw59nFo377Z4AxIPEXWQyMMaWz4PIkd6oQweV-sSN26vjwHVaU5sBBRtueDlCeRVM308Q4ynGLeae20aFWRdDSNXueh4kS4CUdjTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آسوشیتدپرس مقام‌های سعودی اعلام کردند موجی از حملات حوثی‌های مورد حمایت حکومت ایران به عربستان سعودی در ساعات اولیه روز سه‌شنبه، ۷۳ نفر را مجروح کرده است.
سرلشکر ترکی المالکی، سخنگوی ائتلاف به رهبری عربستان سعودی که در یمن می‌جنگد، گفت حوثی‌ها «تأسیسات غیرنظامی و اقتصادی» را در شهرهای ابها، جازان، نجران و خمیس مشیط در عربستان سعودی هدف قرار داده‌اند.
او گفت ائتلاف به رهبری عربستان سعودی «با نهایت قاطعیت، تمام اقدامات عملیاتی لازم را برای بازدارندگی شبه‌نظامیان تروریست حوثی» انجام خواهد داد.
به نوشته این خبرگزاری آمریکایی، این حملات در حالی صورت گرفته است که درگیری‌ها میان حوثی‌ها و نیروهای دولت یمن که مورد حمایت عربستان سعودی هستند، طی چند هفته گذشته تشدید شده است؛ درگیری‌هایی که آتش‌بس چهار ساله در جنگ داخلی یمن را از بین برده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/78267" target="_blank">📅 08:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B7BtMlRpuqqQp8Mu4iKyircr9iwtl29maeomKlPbDWk1MlThliHs009Pnt1BU4b__Wf5BVVKyawuZ2s7TY6GgUjyO_0_5D6H7voWrH0h-z8Rk_YltnnuDXwIKY9lHnXuPJSNHZB9VI6kFgC0kiyBDrU_oQBNt-fsWjpR91_W1HVpArM1MFK64VNL-dd76DGhRgEMdUlVUix9Bgx15r2REJTX0kdOC9z1ET-yBQ0u2V2ZsjPS5vD7AgtIxzRk0WlWpK0kHiScYAnQSXua3QBD58GdngvXN4mE3j2OyyQFBwgHtf4NbfXaCcjENjjTWo9-s2yi1dDOX7OTfRinVF1bnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی ما در جنگ با ایران پیروز شویم، قیمت نفت به‌شدت سقوط خواهد کرد؛ درست مثل هر چیز دیگری که دارد سقوط می‌کند (اما بیشتر!).
بنزین گالنی سه دلار، اما در نهایت به زیر دو دلار در هر گالن خواهد رسید.
همه این‌ها به‌سرعت اتفاق خواهد افتاد و ایران هرگز سلاح هسته‌ای نخواهد داشت.
MAGA!
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/78266" target="_blank">📅 04:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/980dd40283.mp4?token=ZTlKnuYNfI-cGpU0olKRytrn_EAr9Gusfu65Hr7swf17-aZhsjDSuiz30JssXjtkVtqBJTs2sZQhooevDLP9ENmbE31Bexs9A5LOiaTlUn6BA2I-7_TuxdYJoOr9pyFXJ46YYcGQbcVe484dsT0dizK2IRl3gpZVglaYfLcyBnQHQDxoaLg-T_bDcrJN4ebbA-uwZcHe4gV0n0GQjyA_KlGhQMTjEA9EAv54zarOWKxsf8X1_66zuGVzxjLt2CNLSHqC1Px3mqi6fyoMy72eVBbqrW3jkQoRJc6q8MdDMjUfTg7av4GsOy_BKjlIhcRKqX3LSZcXsra5acI_WIFzfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/980dd40283.mp4?token=ZTlKnuYNfI-cGpU0olKRytrn_EAr9Gusfu65Hr7swf17-aZhsjDSuiz30JssXjtkVtqBJTs2sZQhooevDLP9ENmbE31Bexs9A5LOiaTlUn6BA2I-7_TuxdYJoOr9pyFXJ46YYcGQbcVe484dsT0dizK2IRl3gpZVglaYfLcyBnQHQDxoaLg-T_bDcrJN4ebbA-uwZcHe4gV0n0GQjyA_KlGhQMTjEA9EAv54zarOWKxsf8X1_66zuGVzxjLt2CNLSHqC1Px3mqi6fyoMy72eVBbqrW3jkQoRJc6q8MdDMjUfTg7av4GsOy_BKjlIhcRKqX3LSZcXsra5acI_WIFzfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجید ابن‌الرضا، سرپرست وزارت دفاع، مدعی شده است که نیروهای نظامی این کشور توانایی هدف قرار دادن ناوهای رزمی آمریکا را دارند.
روز گذشته محسن رضایی نیز گفت: برای اولین بار موشک ضدناوشکن را بالای سر یک ناو آمریکایی آزمایش کردیم. این موشک خاص، جهنمی برای آمریکایی‌ها به وجود آورد و فرار کردند.
فرماندهی مرکزی ارتش آمریکا - سنتکام - روز گذشته در
پستی که در شبکه ایکس منتشر کرد
تلویحا به حمله به دو ناو خود اشاره کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/78265" target="_blank">📅 04:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VFQIoLJKm8t4sShzER2KbwjNm38bhJDgVoh7ypco-z65p3TEsedfGZf7j15-MZKEUdALeQPKfeYRQcZQkEaa1GDBUHb46Qok_q-jJVy3mulZKaX8FRhuXHA3A9dF_mY4jQF4hHHPzfBIQj9fMusLmz2gh-tzydhu0HPZDznd14Fs14ARGz9AU1U_tSsqveTOKOZye-_2tp7rj2JB8cHgUuQrmkDX_5FNim1WGi4qf8iq1UkI3UXzs-M2hA8a_Y_jk6IDZ4z5-xNo17NiPu3x8YMS_aOkjFx9sawwxDtymbtGahcFS9E5eLZ-spLYjVpuS-JVvjM7UQoSBsazsDLrtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال کریمی، پدر امیرمحمد کریمی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴ در مرودشت، روز ۱۵ شهریور به زندگی خود پایان داد.
امیرمحمد کریمی، فرزند ۱۹ ساله او، ورزشکار و عضو سابق تیم ملی نوجوانان تکواندو ایران بود که ۱۹ دی‌ماه ۱۴۰۴ در جریان اعتراضات مرودشت با اصابت گلوله کشته شد.
پیکر او در روستای جونجان از توابع مرودشت به خاک سپرده شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78264" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIp3vkz0t4MKlWAh4AvWaq2nlyfrzwDXb9FObXBvVJ7qaSHWJSJ--VgQ5KVeKWEuV8boLtPTk9gWmbPkJHqS2j_BCdRmNkGMkKQAcZ6nBC8qvMBkaSoywgvPQBp5u2pwM_kM9ljLcu4UrRrpJzoVC4NOmPWeTnxcHBacZc_yHfTL0j9juhCRaFToBHZTuAMfZqwGE3dFVh67fU9JxyEqtD85PO92iZylcCWT_JaJ8Qw-P1TAmMgPO-NKOEOnx4Jx8Os5DTJapxAQaPfkbzqUBi186qvlKAaeIRMBRHHsXpBdSpHarlw-KybLsRZdV3tnosn1tui_nAImT13jqWMx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیدا حیدری، نامزد ابوالفضل سلیمانی الموتی، از جان‌باختگان اعتراضات دی‌ماه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ به زندگی خود پایان داد.
منابع حقوق بشری ایران، به نقل از خانواده آیدا حیدری نوشته‌اند که این جوان ۲۵ ساله، حدود هشت ماه پس‌از کشته‌شدن نامزدش جان خود را گرفته است.
خانواده آیدا حیدری گفته‌اند که آیدا و ابوالفضل قرار بود همین ماه مراسم ازدواج خود را برگزار کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78263" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mMa7-prYDYfK27h1YBgZJVb5SVUesl4-5QCp5-b2xPaCNw3iuPRBWAba9Y21rLLyShxMHqbuxKK6OCIiC8SQwSI2O67juD0YuwfUVmroWnyR-Rr15QGQdjLvPLtHH_hE30SJj0tBYsXvvEPRvSthdCgPZDKKpBaoLTNJ57Mx6NHezMduA-XP-xnlM6aQCysGkNbToOOZSSL-f4M7UOxqIlyGA6st0H3a8VxEHLeRj6vsI5Ais2V5-w2PJPOAX8iADBMzDkD7eWnfdMqgmNv9wWqFmaphlC3QsZ-P-o-YJT50UNp3X-xW2SBsJ-Tc6ZhUYmyLS3KmVGk0DQCwNUPkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته‌شده با هوش مصنوعی از حمله جنگنده‌های آمریکایی به جزیره خارک در تروث‌سوشال منتشر کرد که روی آن عبارت «خداحافظ خارک» نوشته شده است.
realDonaldTrump
رییس‌جمهوری آمریکا چند تصویر دیگر نیز در این شبکه اجتماعی منتشر کرد؛ یک نمودار آماری که روی آن نوشته شده «ارزش پول ایران از بین رفته است»، دیگری نموداری که روی آن نوشته شده «ایران با یک ابرتورم مواجه است» و نمودار سوم که روی آن نوشته شده «صادرات نفت ایران سقوط کرده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/78261" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78260" target="_blank">📅 22:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p6zufTwr2TqA8UR7kRthZLeVObYft2ABwneI2SmuJIwnV-RiAEGCJouXwahv4mGKNmVzc10MpIeLcKbnPjCZomesBxGC2xqh9zNSwOUyrFTcAP10senPv0W3NKpOcg2sAF7xIcQaYXcqBXHqVH_wwyooUjaorlT5C01ra_fJ8yJSZXGBslkvor6VUFxWQGKftLeaKJ8wY1_JO-Awa3R9-O7HMPVMxEOMqsyZsKlphrcDX6XpCgGckotOrvVZbTVeUSA2D-LqUZfl5lcjyFgUKV8JKuZ1Gk_XzVHKfN9VgIObUlngAKv4sDX3nNvUMv5GqV2Jq9FydJEeGr-R_uaVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78259" target="_blank">📅 21:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=ijb4876oAFTLvsbziRq-tArnVsfZIGVidfM3K6poCEOY55qq8WlZwX2iH5QdETmdFrQ1uvR1Sh-gQzmQ7RvCiS5ukOW3f5FBbg2Of-yUxSXQWcE3mtL52owxpvuIvoUyT1hOAUcplECDwXTZqPvVpdzzPbV2N0EtaB0eRf5UbeTLtJ1QqrUjdfkeEfYZI46Fv7cPUTXXTqq_fN0JEcdy_H_Zk5JEepE-z29Pn-x5u4JY3vVKIVKrBEHo-dB5kmNaObcXDyiTk3VD9iN8CQCeHaWe8kb8opt44nNzAu6OsqQu4DltDYP6QOeTTgRXZl8vleI3-qUBh7-2yChJh6QdkA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f1fd10186.mp4?token=ijb4876oAFTLvsbziRq-tArnVsfZIGVidfM3K6poCEOY55qq8WlZwX2iH5QdETmdFrQ1uvR1Sh-gQzmQ7RvCiS5ukOW3f5FBbg2Of-yUxSXQWcE3mtL52owxpvuIvoUyT1hOAUcplECDwXTZqPvVpdzzPbV2N0EtaB0eRf5UbeTLtJ1QqrUjdfkeEfYZI46Fv7cPUTXXTqq_fN0JEcdy_H_Zk5JEepE-z29Pn-x5u4JY3vVKIVKrBEHo-dB5kmNaObcXDyiTk3VD9iN8CQCeHaWe8kb8opt44nNzAu6OsqQu4DltDYP6QOeTTgRXZl8vleI3-qUBh7-2yChJh6QdkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نرخ سوم بنزین به ۱۰ هزارتومان افزایش یافت
فاطمه مهاجرانی، سخنگوی دولت گفت نرخ سوم بنزین از بامداد ۱۷ شهریور به لیتری ۱۰ هزار تومان افزایش می‌یابد.
سهمیه ماهانه ۶۰ لیتر بنزین با نرخ لیتری ۱۵۰۰ تومان و ۵۰ لیتر با نرخ لیتری ۳۰۰۰ تومان بدون تغییر باقی می‌ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/78258" target="_blank">📅 21:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78257">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M6b2SsipOB8eYW4f7xTWt9aLG7W6CYp1TmivRKuqM2sH51T0R42SOgJ3qoZ6SshvE1D0tqFmy6wrUm3eEOm0jveORO0Mt5nbHTySCgJQtbEBnmLrf7AWxMCoj1OUPtu_i6xLKalwJDc3B0I0jdkgb8wU1XJlhamd1E64Mus9GCsZ7VdbVKkZ3mtfA2CzHqQGACw_RA4ZKp05gRqZpDGG8ueC7hWt0409WKUZhDwznNjER2vptXMLlFos743BmmIamhDdoHOxQIaIv2jMKRd5R9J8h-gCeoGytXxzvYHw7Ycu6v1znZn-N4r0nl9yRK-hjRbQe4z7bS9hcUSUdcDplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که سپاه پاسداران، بامداد یکشنبه ۱۵ شهریور ماه در بیانیه‌ای
اعلام کرده بود
یک شناور بدون سرنشین سنتکام را در تنگه هرمز هدف قرار داده است، ارتش آمریکا این ادعا را رد کرد و آن را «دروغ محض» خواند.
رسانه‌های دولتی ایران گزارش داده بودند که این شناور بدون سرنشین آمریکایی قصد ورود به منطقه‌ای از تنگه هرمز را داشته که ایران آن را ممنوعه اعلام کرده است.
کاپیتان تیم هاوکینز، سخنگوی فرماندهی مرکزی آمریکا (سنتکام)، در گفتگو با آسوشیتدپرس گفت ادعای سپاه پاسداران «دروغ محض» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78257" target="_blank">📅 17:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=SYx9A7ynhDT6faweYi5cKBrRK67R-611kElMBw3ED2I9qQFkyNwMUH46vRa6IHCgMb3LpaPKQFIxNw46t5rhc6Nn7bj7jnQVzB_Pt7IbcLtTSSPPExOsiOtQpYg5GxO48VW7Ffr4w0AqhPV7Br94CW9jwJLGlkr3nxL-OajhlQBq7qKNL5A8VO13mT66WniAxnQqqMk2BrVVNrFn1QZXjSzmtbKroEys9aGUd56V0JSxm7D2QjVveGzHlcsmle155FSvaK7W91JGZErb3rpL4joY0JgTOB_FLBa-f5qEuZAN5D1Bb12COOFNM83S8XAZ-IwRbPZhbpIqOHILmFE7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9239224ea3.mp4?token=SYx9A7ynhDT6faweYi5cKBrRK67R-611kElMBw3ED2I9qQFkyNwMUH46vRa6IHCgMb3LpaPKQFIxNw46t5rhc6Nn7bj7jnQVzB_Pt7IbcLtTSSPPExOsiOtQpYg5GxO48VW7Ffr4w0AqhPV7Br94CW9jwJLGlkr3nxL-OajhlQBq7qKNL5A8VO13mT66WniAxnQqqMk2BrVVNrFn1QZXjSzmtbKroEys9aGUd56V0JSxm7D2QjVveGzHlcsmle155FSvaK7W91JGZErb3rpL4joY0JgTOB_FLBa-f5qEuZAN5D1Bb12COOFNM83S8XAZ-IwRbPZhbpIqOHILmFE7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: قاعده بازی عوض شده و دوران پاسخ متناسب به پایان رسیده است
رئیس مجلس شورای اسلامی روز یکشنبه ۱۵ شهریور، یک روز پس از حمله آمریکا به چند نفتکش ایرانی در خلیج فارس، گفت دوران «پاسخ‌های متناسب» به پایان رسیده است. او همزمان به وجود مشکلات اقتصادی در کشور اذعان کرد.
محمدباقر قالیباف در سخنانی در جلسه علنی مجلس تهدید کرد: «هرگونه تجاوز به منافع و امنیت ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر دریافت خواهد کرد.»
قالیباف که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای بعد از آتش‌بس با آمریکا است، در بخش دیگری از نطق روز یکشنبه گفت: «نوسانات شدید قیمت ارز، تورم، بیکاری و مدیریت بازار، چالش‌های اساسی هستند که به معیشت مردم فشار جدی وارد کرده است.»
او افزود: «در کنار میدان نظامی، امروز اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است.»
این سخنان یک روز بعد از آن است که قیمت دلار در بازار آزاد ایران تا مرز ۲۲۸ هزار تومان بالا رفت و از سوی دیگر آمارهای رسمی نیز نشان‌گر افزایش شدید تورم در ماه‌های اخیر است.
علی مدنی‌زاده، وزیر اقتصاد ایران، نیز روز یکشنبه گفت واکنش تهران در برابر تشدید فشارهای اقتصادی آمریکا «مقاومت اقتصادی در کنار اصلاحات اقتصادی» است و این دیدگاه را که تحریم‌ها باعث تغییر مسیر ایران خواهند شد، رد کرد.
او با اشاره به اظهارات مقام‌های ارشد دولت دونالد ترامپ درباره اقدام آمریکا برای قطع رابطه ایران با اقتصاد جهانی گفت: «تصور اینکه بتوان با فشار بر اقتصاد ایران، تصمیمات یک ملت را تغییر داد، اشتباه است.»
وزیر اقتصاد ایران افزود: «مسئولیت اصلاح اقتصاد ایران بر عهده دولت و مردم ایران است، نه وزارت خزانه‌داری آمریکا.»
این در حالی است که همزمان وزیر خزانه‌داری آمریکا اعلام کرد ترکیب محاصره دریایی و تحریم‌های گسترده، صادرات نفت و دسترسی جمهوری اسلامی ایران به درآمدهای آن را به‌شدت محدود کرده است.
اسکات بسنت در گفت‌وگو با شبکه فاکس‌نیوز که روز یکشنبه منتشر شد، با اشاره به نقش چین به‌عنوان خریدار اصلی نفت ایران گفت محاصره دریایی مانع خروج محموله‌های تازه شده و برآورد کرد که «احتمالاً تنها حدود ۳۰ میلیون بشکه نفت خام ایران باقی مانده که چین هنوز نخریده است».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/78256" target="_blank">📅 17:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O5knj2RB2SYTCeUcqmkT06W6G-MH7S4QBQrC9c5JPCm3-LW5QUOz_hN4g7lJECLi3e6fmwLRbVJU057W8mqQqOo5sCwol9K7Kmdm3TBWsZgAGzem2dkpzlWISdp_tyPCs08lUwo4QCfjMt4AwWYEZFy_lwuaMl9d17PMITdPk-d6rwsblNhwUjdprU8I2dS8iQTVMNrhaCTiZ_4YwvTQ60V302sbog9Me0H8vwOGQ_o-HwwD3kb05gHhzwwBfj4pgIfXKyiITLV8RQPG6kI9nwh9FQj5hMVXP3p87MXEyWIAUZ49HLYn4d3hrGXRx2XtvZLKDGNv9ocsCWepmTJICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران پس از عبور از مرز ۲۳۰ هزار تومان، به کانال ۲۲۶ هزار تومان بازگشت.
بر پایه گزارش اقتصاد۲۴، نرخ دلار صبح امروز یکشنبه ۲۲۶ هزار و ۱۰۵ تومان بود. وب‌سایت‌های اطلاع‌رسانی طلا و ارز پیش‌تر برای ساعتی از جهش قیمت دلار به بالای ۲۳۰ هزار تومان خبر داده بودند.
بهای دلار در ادامه با شیب نسبتاً تند عقب نشست. اقتصادنیوز این افت را به ورود بانک مرکزی به بازار نسبت داد و نوشت این بانک به دنبال جذب نقدینگی در بازار است.
حواله دلار در مرکز مبادله ارز و طلای ایران نیز ۱۶۰ هزار و ۹۸۳ تومان اعلام شد که شکافی بیش از ۶۵ هزار تومان با بازار آزاد ایجاد می‌کند.
حتی با احتساب اصلاح امروز، رقم کنونی نزدیک به ۱۰ درصد بالاتر از آغاز هفته گذشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78255" target="_blank">📅 17:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EIUX18CaR1JjIIqJAulXaP7ZNkbEa9cYyVd4SmMLF7ocd7VJOz7IYedczfsk4wBAqjz21sW-EPV29J_ZJiB-8AiDR4VXCveY5JupW4A_ZkEt6R8XPotBc0auljfgdU3BmlR_IPTpLdYaZ_SywjH1dUG24eNj0BFHn1oMngLHHgc09DJ_ewcm8-H7BE_XtDQW9POVgNPQ0H88LomdESWlLj0VlMeC5yeixXpQ8TWGQ5Do-0wuP67xpN3YbnMXRFmWmUrA5QSMcLohEY8Od7LS1B4EQlDXyaIww3R9hM4BZHgAgq9lJ5sN1P7A-e-OeevjRpDNKZx5A9lUDHzbSAhdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NlDt6tzTZqySh3EpBwVTZoLLoWeFv99ITTP5bneNDElrgudHG1xKMtVNmipI6xnDOXAgoJp_BRNcmvgdAIK29JZbVaCUWMwrzbAIm6OOFCW9SuNNfRsYgv5QIv5Bwug3o6fzwGSguBei-woLyi_KApP6Npmixh1L-lD4R_fX2lSrRcCK5Lar53jRpgbfwlKC571II1-iJo-77E5GmW7WLMfpz4cVkOz1SsqBnfQa5GLaJN1drsW-HHkLfPFbvbZTYRIXgZaAClgMDs9TxfOu6woRe4R_hlwJwX8eTwsZq9cJPBdbjNdng8sdjelGoi98c72dnOhQ3zfky10hdKb-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LNy08-wRupNLIWtVTeMSUfUmqiUY4uQfWXsU5iY8B_3k00k8mwod-S8WTFvcvTBXWOctVLmLBLj40UATgMO6d9q1S6y9rzXB01WqmkDnXu9-IEo483fibfFHZi5h0U06OrdHYIPT7Sz2ko5S0mNzvQYwgGN3lwd1H3slK4DzYCpmwUflxPIn5vbwNpUw2JCYfcTj0BkI4PAws-q-4sk241iU12ERba-imsRmWPvZMZv5ROCORy7rF3szaIBzt0PX5KXvIDH-ExWSOkLsvp1OrJ7ZCO_2YowPX_FUsxBz7EI2m0VXwHV_oIOQgFyOemeSCUe1zi0deU_kmkKMsB9z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nhm0SWg0tvKnG8ZhtoEFBQmmpmQDGQGwPj14BiNQZNkDXV_-QCSVa9h3NHUGeafObh4hb6WmvyzZAgqYxJou4ysFfEB7Ac7Nj3Al-YgcgId7OQkUveob79JMriUY52PSWslApIEPqiZHTAHDwiOIPhMk937o1_b9S3bl9QYiFyebOGfuceQutCALizY0RJpqAX9sg-3psyIfkorKt8bA3E6giVLB1CNy4zAaSohK_i6RnZthsVeSHNO4FNZbgmZw7vY0GGwOoi7dQNMyihJ5tyAZHEu45BtKlty2VHW1I9oh9_FwmXvssnGtEmX43wKBbfp6WetK1AYzAS_DFkA9Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VVf1UeIdxze44_VKTzGEX7tpN-9Br6rIHJu_mr6O354sfM3RJpz32dbaMH4SknSOTgomrJ5prYhZLDrK7PWcf82ix1nxQFObOFe3WXLe1iKKTC6iI0Efqkf1FY5eqx9bNNtGI8G17j0az1jqne5wBuewL45ff-oCViGSSZ8_lGjmLWCn3xj2roTGXG5d5D5qiTQD4xWDevgEg836hyzWJo2ZNDw4YwQ3VMhyEX5HyXrp1WR_D-VlAfEgyxcaNGNRVeOfWaHriLjdtZLub9MlGK-oWssIN1Dm0Ln3KtkrcB7dWiabDYXNN414KhoXfEEmJyguficOZEoI5wrHaSxJSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">BadAngel66636
آرمین تیموری راد ۱۹ ساله
پدرش: امید تیموری راد ۴۷ ساله
عموش: امیر تیموری راد ۴۲ ساله
نوشته بودند ۱۸ دی در فردیس کرج به دست ماموران سرکوبگر حکومت کشته شدند.
روی مزارشون نوشته شده ۱۹ دی
و نوشته بودند:
به جز این سه نفر، همسر امید تیموری‌راد و مادر آرمین هم در پی اصابت گلولەهای جنگی، بە شدت مجروح شدە است:
@VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78250" target="_blank">📅 17:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78249">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LLoELs_H9KTgZr7tIeqYXWvIAno9NqCL66QMcly4nD-jXqjnV244azgPinMqVFto8Dp24RDd_q1IdyCUbwwacYbVYQIDK3YOdynZ8ILqL9XBFgL2sNJQ4qZuHG5ht06SKScEI8-axDtKuUHtmUtHky9JQaxFNp0qUBuRLd1gIB-JNBUa_5QDGWH59LJe4OtnwRw9I-qpE-7lT5VIXWyJ62-eexs168-sKBxuMEwyWpvO9sAzkaFd2NJTQZnVxyf4XcqOPqAkbJDmV8QN7LQckgxaHYw_vUKPYmVB_cHjz7PfkKgZkZaIRncEzq5bc15l7AJKa_SsJU2uGLXBcDmBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران می‌گوید یک فروند شناور مدیریت‌پذیر از راه دور ارتش آمریکا را هدف قرار داده است.
روابط عمومی سپاه پاسداران در بیانیه‌ای اعلام کرد که این شناور قصد ورود به «منطقه حفاظت شده» تنگه هرمز را داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78249" target="_blank">📅 09:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=fzk31nPNLb2yZTG7hPgut3dYSjr1dXmGjx7Z60fxYxa1InmxRJmCJXYAeuC1sfiRlG7B9JnhSaPrvUwn_bzm4LUCvrIWP6CDk9O6Ufslq5OhtfySgbq1K4LTaxOmujDOaAfHlK-KKrkKBCGh16_pwJgpmqBnwef5GuimB2wJl29ZN4t3lY8HKMDn_Pr1vkjG6IYk4QuiDj4pJjdiIi3WSrG8draFLzK-WHPhT52MNfeOOtdTZjSMXrxCsrvCHkZ1Yp9EZg_epK00T-dAIcFZwcRpWlWhXNruatkrcAeOoHHeY7vpHnZQY38p5kIjm8JcECtRbLsOHiIIZsd7WST9GA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5782c4c6b3.mp4?token=fzk31nPNLb2yZTG7hPgut3dYSjr1dXmGjx7Z60fxYxa1InmxRJmCJXYAeuC1sfiRlG7B9JnhSaPrvUwn_bzm4LUCvrIWP6CDk9O6Ufslq5OhtfySgbq1K4LTaxOmujDOaAfHlK-KKrkKBCGh16_pwJgpmqBnwef5GuimB2wJl29ZN4t3lY8HKMDn_Pr1vkjG6IYk4QuiDj4pJjdiIi3WSrG8draFLzK-WHPhT52MNfeOOtdTZjSMXrxCsrvCHkZ1Yp9EZg_epK00T-dAIcFZwcRpWlWhXNruatkrcAeOoHHeY7vpHnZQY38p5kIjm8JcECtRbLsOHiIIZsd7WST9GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام ویدیویی از غرق شدن نفتکش M/T Kylo در دریای عمان منتشر کرد و نوشت در قعر دریا به نیروی دریایی ایران پیوست:
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 397K · <a href="https://t.me/VahidOnline/78248" target="_blank">📅 04:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d7NwQET03NbJ0PzN00rplz6J8iMhZW-ku6-AWwFQrUrlVWt7SxrXmXQGdIOu0R4x6IDH6B9jpFKVmIqjzQZ-jIzJZ5CPYiXAZIjcFhBO8x5eFpNvvamWqvg5jt9pwUBcCxGtksMEnSkhzSeGic9Tn2_SYjus2lk4ojlEvLWO65aPOSzAobrIg30yZOrZKlACzWbMr-DpkDNG_uBYzavTK-AVunOxoye8VNdrE30EyQoxkA-QJlyhvH5TuzesC7tJo-tzp3ZamsVheEty7OdsXx4O97sw1vG1JZgZGEpMSIYK_Y2SO2e1qEjmF-zedt9o3aH7Eas62O1fhFQngye8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، بامداد یکشنبه، با انتشار بیانیه‌ای اعلام کرد که نیروی هوافضای این نهاد با استفاده از چند موشک بالستیک، یک ناو هواپیمابر و یک ناوشکن ارتش ایالات متحده را هدف قرار داده است. در این بیانیه آمده است که این شناورها در محاصره دریایی و مسدود کردن مسیر کشتی‌های ایرانی مشارکت داشته‌اند و پس از این حمله «دچار خسارت شده» و «منطقه درگیری را ترک کرده‌اند». سپاه پاسداران همچنین با اشاره به تایید وقوع درگیری‌ها از سوی سنتکام، این عملیات را پاسخی به اقدامات نظامی واشنگتن دانسته و هشدار داده است که در صورت تداوم فشارهای نظامی و محاصره دریایی، پاسخ‌های نظامی گسترده‌تری متوجه نیروهای آمریکایی خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/78247" target="_blank">📅 02:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLcbBao4nj38tUlNdQWGX7aLOGfvTeDDQ5gknwqPjTzOFkGaKT792SHyXIqYlIWJyMs3i5onLK8CB1lYmOHOUlhLWspMZn-4qG3h1mkCnNZjvTLeS9v6YUJogoBNuP-8ZW_64ovt95_9NupasjhHY1er1VDd7Fygsf8fOSHBop3VsSMwqtfLd3pvpKyA0nAcA_PHgDSiWrSW4EYq29I0saE5k5vlNaRzJX5p0A291I77CW-ydkxLUeQ_aSLEDLX10Ty44ZIXDm87P4Zb7oPbe5-4KEv8JZBcG0Ah5_mpli-KalvINW1a0n_iEPRC5m612fULwuEpHeKMG7urGpnxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم نیروی دریایی سپاه پاسداران انقلاب اسلامی روز شنبه در بیانیه‌ای اعلام کرد که سه نفتکش را که از «مسیرهای غیرمجاز در تنگه هرمز عبور می‌کردند، و همچنین سه شناور دیگر آمریکایی را در مناطق دیگر هدف قرار داده است.»
نیروی دریایی سپاه در این بیانیه به هدف قرار گرفتن سه نفتکش ایرانی توسط نیروهای آمریکایی در صبح امروز اشاره کرده و گفته است که این حملات خساراتی به‌بار آورده است.
@
VahidHeadline
علی محمدی، معاون سیاسی نیروی دریایی سپاه، روز شنبه در گفتگو با خبرگزاری فارس، گفت: «در ۱۰ روز منتهی به هشتم شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.»
او گفت:‌ «حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل اراده نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/78246" target="_blank">📅 23:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=Vjp6QLrST9hrmDzJp4TAeJGzqtz_wM66OEIP6los7tdwIQPgG6ct1lECprY-wwSk0AquvPvVEz0ccxyPGx_-VjkWGDbO-CQUv3BzRUxG5FuYjw15aWfl7g75ORA7DABRHaDYhuB2bhRDfNjcji0y20bOo8TsiHKqhBnGApxexENK2sGajfJd6d2F99uL9WDDTu2U1N83AdMDKSxDUNouD6OPc-Z3bpJTYXX9BdGqbh-dmlfGF9emAN8AfmZB1bcPEW56alON1tRaAzyk6zk6XvE0lAvkvOM0ovRGGcDw1KhuZqahXUKivsX5N2RWL6IAK08a9qothY7rQxawYrpOmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f413c1eb0.mp4?token=Vjp6QLrST9hrmDzJp4TAeJGzqtz_wM66OEIP6los7tdwIQPgG6ct1lECprY-wwSk0AquvPvVEz0ccxyPGx_-VjkWGDbO-CQUv3BzRUxG5FuYjw15aWfl7g75ORA7DABRHaDYhuB2bhRDfNjcji0y20bOo8TsiHKqhBnGApxexENK2sGajfJd6d2F99uL9WDDTu2U1N83AdMDKSxDUNouD6OPc-Z3bpJTYXX9BdGqbh-dmlfGF9emAN8AfmZB1bcPEW56alON1tRaAzyk6zk6XvE0lAvkvOM0ovRGGcDw1KhuZqahXUKivsX5N2RWL6IAK08a9qothY7rQxawYrpOmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس مرکز فوریت‌های پزشکی استان کردستان اعلام کرد که در پی آتش گرفتن یک تانکر حامل مواد سوختی در محور سنندج–همدان، دست‌کم ۱۱ نفر جان باختند و پنج نفر دیگر زخمی شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/78245" target="_blank">📅 20:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/giRCZ59Sjcu0hLrV7OD2rLdFm33zOvsmIUxuepArvNsR17yocOAmmgAadCeADyjPCjmCVTfte0OCtYLs-Gpl9irH_jEG7PB6FwWpWDKwlAVXcK-bJPIooIKplthixIWXJ2nPYGpZzOlbXaubYLRuIYx9eYmeGRz_KkTzQZTW9Z4xMzwuizwL00QxX3wjgDkB9e0g7XL-5Aca-69kc1MQYu4et9z8-8E1FC3sCooPFHFEW_IAXUM4duzrptEwFOYm0YlrsDOnTcWvMeoyqGqMqaEu4nyVXBaPgUloludQTRMpEfumEB3sy4Wfva4tFVnj2mtycaNybhELZ1nStzODag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا  گزارشی درباره چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کرده است.
گزارش‌ها حاکی از آن است که این کشتی‌ها در چارچوب فعالیت‌های نظامی جاری در منطقه، هدف آتش با هدف از کار انداختن آن‌ها قرار گرفته‌اند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/78244" target="_blank">📅 19:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرانه‌ها(مهدی محمودیان)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWMW_R4QmSWTVi42c8sw8YmtVppcQL4uLat94S-_nlTn4Pgk0lNDJ5jl2iCzydPhSSvBb2thjYT0egGLXwZji8FygwnPbIUCoGHs4EATPOAEs3oWMjLCJbzBJter3qfzHVeJSLErHSbuv2JMwLXcInEuC1aHWGXmxN_nAqAlZ_We9WlCJoACcNm-gksGRJlpieUfWnT9C0WjEgPyeRkVg967nm3MmqErBm3wgOzTPLVxtU0yix5_veYddEvoXF2Odiwa2mtm4YG1oyFazrxfnPaXb1_WtUJ46sRC_iqXX_Of8LmFwEGAsG8B6v70gUvm9pgQqZzqud8l5yBCT_Ai9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pV5hoD28ZB0l-a8PCv9ppc10gr8tCCBYkvwlhtV4SjdlAAFEcUB9EsnJ-yS9uscIZlMGZcn6j5okPw37xTqUPAWz0ksaf57Bk8VD8G_J2oCBptDvik3DSF_74GrgPCmSbS76BS_vmY4QvZ2Evx1DYcClBFCuzmWf27uLZdn5O8uBNgITI8LArP47FE7elP-_FxcTt_uXrJrSQeTeRHFmcGuFRMpBXSyTloRPclgt5TFkE77pT_blxA3-3ifG4PW4Yms87xtism3gC3PjqsvQv2iWUaz9dXhQ8c_yYu1gCFJJw4rIcnlzFWZOC0Aswq2CHFySqDWgoN2Vrrp3bnmZEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❇️
مادر دو معترض جان‌باخته، در لاهیجان بازداشت
🔹
مادر دو جانباخته اعتراضات ایران نزهت میرراضی، معروف به «مامان نزهت»، مادر علی و عماد شوش، دو تن از جان‌باختگان اعتراضات سراسری ایران، روز جمعه ۱۳ شهریور در لاهیجان بازداشت و به مکانی نامعلوم منتقل شده است.
🔹
نیروهای امنیتی نزهت میرراضی را در حالی بازداشت کردند که تاکنون اطلاعاتی درباره نهاد بازداشت‌کننده، محل نگهداری و اتهامات احتمالی مطرح‌شده علیه او منتشر نشده است.
🔹
بازداشت این مادر دادخواه یک روز پس از آن روی داد که او با انتشار ویدئویی به پیشواز زادروز یکی از دو فرزند کشته‌شده‌اش، عماد شوش، رفته بود. خانم میرراضی همزمان با افزایش فشارهای امنیتی در استان گیلان و جلوگیری نیروهای اطلاعاتی و انتظامی از برگزاری مراسم زادروز هومن صباغ بر سر مزار او در لاهیجان صورت گرفته است.
🔹
نزهت میرراضی در دو دوره از اعتراضات سراسری ایران دو فرزند خود را از دست داده است.علی شوش، شاعر، بازیگر تئاتر و نوازنده اهل لاهیجان، در جریان اعتراضات سراسری «زن، زندگی، آزادی» در سال ۱۴۰۱ جان باخت. هه‌نگاو می‌گوید او در جریان اعتراضات در اصفهان به دست نیروهای حکومتی کشته شد.
🔹
عماد شوش، برادر علی، نیز از اعضای فعال خانواده‌های دادخواه بود و بر اساس گزارش‌ها، در جریان اعتراضات سال ۱۴۰۱ سابقه بازداشت داشت.
🔹
عماد شوش روز ۱۸ دی ۱۴۰۴ در جریان اعتراضات در لاهیجان بر اثر شلیک مستقیم نیروهای حکومتی و اصابت چهار گلوله جان باخت.
🔹
در هفته‌ی گذشته نیز جعفر پناهی به دیدار مادر این خانواده رفته بود.
@MahmoudianMehdi</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/78242" target="_blank">📅 18:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=Jzf87Zj0ll8PrinMDFZo8Tm1Y7qzku14khzsxnGlQ9mIYeJyDJxYy42Hn_slWLL4_d_Q16xLmeM0H3b5dWlCJXjrRNT25GfyQGQuGpsjytsPH-nEDLgLBALU26UruK0LV-KsSxrQD4TjPRuw50B7Why2hIKvvw-KKka1nZvt0s_KxnVYWeXXsY9ubeId9zpkiBiQE4DdxGslogIe2MSVWVq5DDLw7IQpSQANqnODVyoYCLo7gk7a2nx2d-IcYvS_k-XiQd1PV7fL69oxUykHXSokR9R1EPO5a2SgNoa1quUgpaq0QiS7W0Q4VGiJXWDpaq6bBYh7fvEhr-FtnM9rRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=Jzf87Zj0ll8PrinMDFZo8Tm1Y7qzku14khzsxnGlQ9mIYeJyDJxYy42Hn_slWLL4_d_Q16xLmeM0H3b5dWlCJXjrRNT25GfyQGQuGpsjytsPH-nEDLgLBALU26UruK0LV-KsSxrQD4TjPRuw50B7Why2hIKvvw-KKka1nZvt0s_KxnVYWeXXsY9ubeId9zpkiBiQE4DdxGslogIe2MSVWVq5DDLw7IQpSQANqnODVyoYCLo7gk7a2nx2d-IcYvS_k-XiQd1PV7fL69oxUykHXSokR9R1EPO5a2SgNoa1quUgpaq0QiS7W0Q4VGiJXWDpaq6bBYh7fvEhr-FtnM9rRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست اکانت سنتکام:
'
سنتکام پس از هدف قرار گرفتن ۲ ناو جنگی نیروی دریایی آمریکا توسط ایران، ۳ نفتکش سپاه پاسداران را منهدم کرد
'
ترجمه ماشین:
تامپا، فلوریدا —
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) روز ۵ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی موشک‌های بالستیک به سوی دو ناو جنگی نیروی دریایی آمریکا در حال گشت‌زنی در آب‌های منطقه شلیک کرد، سه نفتکش حامل نفت خام ایران را هدف قرار دادند.
یک ناو هواپیمابر آمریکا و یک ناوشکن مجهز به موشک‌های هدایت‌شونده با موفقیت از چندین حمله بدون تحریک قبلی ایران گریختند. هیچ‌یک از نیروهای آمریکایی آسیب ندیدند.
پس از حملات ناموفق ایران، سنتکام نفتکش‌های حامل نفت خام سپاه پاسداران،
M/T Downy
در نزدیکی ساحل جزیره خارک و
M/T Stark 1
در نزدیکی جاسک را به‌طور دائمی از کار انداخت. نیروهای آمریکایی همچنین نفتکش خالی
M/T Kylo
(که با نام «Noxen» نیز شناخته می‌شود) را در دریای عمان به‌طور کامل منهدم کردند؛ این شناور پس از آنکه به خدمه دستور داده شد کشتی را ترک کنند، در چندین نقطه حیاتی هدف قرار گرفت تا غیرقابل استفاده شود.
این سه نفتکش ایرانی بخشی از یک شبکه سایه چندمیلیارددلاری هستند که منابع مالی سپاه پاسداران و نیروهای نیابتی منطقه‌ای آن را تأمین می‌کند. ایران هیچ ابزاری برای دفاع از آن‌ها ندارد.
دریاسالار برد کوپر، فرمانده سنتکام، گفت: «پیام به سپاه پاسداران روشن باشد: اگر به دو کشتی ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه کشتی شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و در معرض آسیب ایران را نابود خواهیم کرد.»
CENTCOM
دقایقی بعد در پستی دیگر:
«پیام به سپاه پاسداران باید روشن باشد: اگر به دو فروند از کشتی‌های ما شلیک کنید، ما هزینه اقتصادی حتی سنگین‌تری به شما تحمیل خواهیم کرد — سه فروند از کشتی‌های شما را از بین خواهیم برد. ما در دفاع از نیروهای آمریکایی تردید نخواهیم کرد و در صورت لزوم، ناوگان نفتی محدود و آسیب‌پذیر ایران را نابود خواهیم کرد.» — دریاسالار برد کوپر، فرمانده سنتکام
CENTCOM
پیت هگست وزیر جنگ آمریکا:
ساده است: اگر ایران به کشتی‌های آمریکا شلیک کند، ما نفتکش‌هایش را نابود خواهیم کرد (و غرقشان خواهیم کرد). تنها کاری که باید بکنند این است که شلیک به @‌USNavy را متوقف کنند.
ناوگان نفتکش‌های ایران بی‌دفاع است — ایران نه نیروی دریایی دارد و نه نیروی هوایی. هواپیماها، کشتی‌ها و زیردریایی‌های ما می‌توانند همه آن‌ها را، در حوزه‌های @‌CENTCOM و @‌USPACOM، هدف قرار دهند.
PeteHegseth
خبرگزاری صداوسیمای جمهوری اسلامی گزارش کرده که خدمه دو نفتکشی که امروز از سوی آمریکا مورد حمله قرار گرفته بودند «با قایق‌های نجات به ساحل منتقل شدند.»
براساس این خبر یکی از این نفتکش‌ها «خالی و دومی حامل محموله نفت» بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78241" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mZ6lb1P2rqrlm4Pp2zScRfdjqESr079VEQI4NXS0TJjn-Dk5Ur3YQ99ELSBfkvDCVpRBO_BPS43_33i3FQMyZME_RDWKAXeGSSMzbso9tiXIcHKiBTTRAU7b6UbHd5x8Em2RS9OZZA9s0XjsnxCS3lONvozzbJNXRV5ZtYslxRtTWl1_h7N3vB314-HEWBaPaftrOkjWU6y9DR6e_MM1pOm37UwNldYz-Rj_A4Ag1GDM4S7W04xcIBHy72ZpNvMtxwVd22fqXSIs7QR9VGqJZKc9Lrnb660FfOE2aSJuWEm4Ln1nM03aprbwNZycGnQ7K5jLu5RWH26arM8U_Axf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز شنبه ۱۴ شهریور با جهشی دیگر به ۲۲۸ هزار تومان رسید و بهای یورو نیز از ۲۶۳ هزار تومان عبور کرد.
وب‌سایت‌هایی که نرخ غیررسمی ارز در ایران را به نمایش می‌گذارند، همچنین بهای پوند انگلیس را ۳۰۷ هزار و درهم امارات را بیش از ۶۲ هزار تومان اعلام کرده‌اند.
این افزایش مجدد تنها یک روز بعد از آن رخ داده که عبدالناصر همتی، رئیس‌کل بانک مرکزی ایران، کمبود جدی ارز برای واردات را رد کرد و کاهش شدید پول ملی ایران را ناشی از افزایش تقاضای «احتیاطی، سفته‌بازانه و خروج سرمایه» دانست.
قیمت دلار در ابتدای شهریور از مرز ۲۰۰ هزار تومان عبور کرد و طی دو هفته گذشته به شکل مداوم افزایش یافته است.
این در حالی است که همتی هفته پیش گفته بود ایران «به‌اندازهٔ کافی» ارز در اختیار دارد و بانک مرکزی در صورت نیاز آمادهٔ تزریق تا دو میلیارد دلار به بازار است، اما این اظهارات مانع ادامهٔ افزایش نرخ ارز نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78240" target="_blank">📅 17:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IFcTHLs_WrlFA16fAoUZfVxmR_PgDkqy9fP8FWOSs55M6MnJ16NftsDr7t2nBCLj1ONv9xmJh9InorMDjAwnZT0e15pnsqVhsn6lUSItBnKfZMAxDTHHqzgTrEVZpfg9M0nflPoD82sMqo5N16QgMo1JNy_9_-DRDH1no1EblZB1RBhTPnmDxZSdbzTIhwXUHqrbSZHxcLt9aHEBMu2oYyFZgzHsoX7khnhsM3tfQobA8ZMncwoxcjo7shJwzVLxffc08NW5cQdu_OKr36nQ7sOOXbctIPqdLZ-TksbpEpE8RZ_GngKNxhrgwRSTFBt0KNW0UbESLgi7EggrTO6xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه ایالات متحده روز جمعه ۱۳ شهریور از موافقت با فروش پنج میلیارد دلار بمب، کیت‌های هدایت و دیگر تجهیزات نظامی به عربستان سعودی خبر داد.
این وزارتخانه اعلام کرد این فروش، توان دفاع هوایی عربستان را برای مقابله با تهدیدهای کنونی و آینده منطقه‌ای تقویت و هماهنگی تجهیزات این کشور با سامانه‌های نیروهای آمریکایی و دیگر شرکای واشینگتن در خلیج فارس را بیشتر می‌کند.
عربستان سعودی از زمان آغاز جنگ آمریکا و اسرائیل علیه ایران بارها هدف حملات موشکی و پهپادی نیروهای ایرانی و حوثی‌های مورد حمایت تهران در یمن قرار گرفته است.
وزارت خارجه آمریکا کنگره را از این معامله مطلع کرده است؛ این فروش برای نهایی شدن همچنان به تأیید قانون‌گذاران آمریکایی نیاز دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78239" target="_blank">📅 17:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19446f537f.mp4?token=Mh4jSdnOQskZM2-bkxLgLWr-zC9MjeDfnJ8wDs8-0dVuPH-vNg9XjVXKl3vwBiPLYv7l6Oq9gQNtcdqbyJRCg54cm-mIAmS3FgjknrEIwRkSq-RqxMW376vEmFyA-MJCkPEQJ_6nj56S-NSIDO-Nixkm7yoY_gZvWc3QP8JCknpxpKCIqZmjzFLYS65IuCrG7jJqBs4m1_22P4t9z0CafpmQ_mlbAl7GIwJ0U2dsg26h5NUOvXghVB2Yyu9nippPgh5CGTyIj2JmK5WX3u8yCxH_aEemvA7FaZ8FjpJDnBmZ8HOCJ9yfzKjhpnNW1ZyLCiKXig-k5zzTRY_vn4_vrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19446f537f.mp4?token=Mh4jSdnOQskZM2-bkxLgLWr-zC9MjeDfnJ8wDs8-0dVuPH-vNg9XjVXKl3vwBiPLYv7l6Oq9gQNtcdqbyJRCg54cm-mIAmS3FgjknrEIwRkSq-RqxMW376vEmFyA-MJCkPEQJ_6nj56S-NSIDO-Nixkm7yoY_gZvWc3QP8JCknpxpKCIqZmjzFLYS65IuCrG7jJqBs4m1_22P4t9z0CafpmQ_mlbAl7GIwJ0U2dsg26h5NUOvXghVB2Yyu9nippPgh5CGTyIj2JmK5WX3u8yCxH_aEemvA7FaZ8FjpJDnBmZ8HOCJ9yfzKjhpnNW1ZyLCiKXig-k5zzTRY_vn4_vrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های ایران از شنیده شدن صدای چند انفجار در نزدیکی جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و هدف قرار گرفتن یک نفتکش کوچک ایرانی خبر داده‌اند.
خبرگزاری تسنیم گزارش داد این نفتکش صبح شنبه ۱۴ شهریور در شش مایلی جزیره خارک و در محدوده لنگرگاه، «هدف قرار گرفته است.»
تسنیم می‌گوید این هدف‌گیری «با چهار پرتابه نیروهای آمریکایی» انجام شده است.
به گفته منابع محلی، این حادثه تلفات جانی نداشته و کارکنان در حال تخلیه نفتکش هستند. وب‌سایت عصر ایران نیز اصابت چهار پرتابه به این شناور را گزارش کرده است.
خبرگزاری فارس پیشتر اعلام کرده بود که صدای انفجارها از محدوده خلیج فارس شنیده شده، اما نشانه‌ای از دود مشاهده نشده و منشأ صداها مشخص نیست.
نورنیوز نیز به نقل از منابع محلی، گزارش «حمله موشکی آمریکا به یک نفتکش ایرانی» را منتشر کرد، اما آن را تأییدنشده خواند.
خبرگزاری دانشجو هم ویدیویی را منتشر کرده که می‌گوید مربوط به این نفتکش هدف قرار گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78238" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=d_S-tMz1Gwxc8ToBqjw1qtVBF2EqAFE4oCyYG8LVq8gVLM1Oiokpz1uqu0WqYlP5_3ys2LIY-wN_vyQXQJBcELymh0jjGTEzgkqJs3Xl2x0lutQpEHWhaTkZIrMkPwV9YCDjPF1niRl6ARCMpl94fwsVlSPJ4LEmCcXUBBzTDezBxMBu2tNUm5Vb6Tww8KljDccc5O6kDisbqv_yqiFYOvuRRRlgYCjXI6RJ5Hv2VcDhQ1WfrLx6b2vqvyPtugCIbcuRXwqc-3QHbz78ZKUdW09cove6jn6rNeCoh0jAJOkkPWXMqBVYF6IRE6CeRsR7H_sCfwdUMWW0NwyW39U9Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ee2041b46.mp4?token=d_S-tMz1Gwxc8ToBqjw1qtVBF2EqAFE4oCyYG8LVq8gVLM1Oiokpz1uqu0WqYlP5_3ys2LIY-wN_vyQXQJBcELymh0jjGTEzgkqJs3Xl2x0lutQpEHWhaTkZIrMkPwV9YCDjPF1niRl6ARCMpl94fwsVlSPJ4LEmCcXUBBzTDezBxMBu2tNUm5Vb6Tww8KljDccc5O6kDisbqv_yqiFYOvuRRRlgYCjXI6RJ5Hv2VcDhQ1WfrLx6b2vqvyPtugCIbcuRXwqc-3QHbz78ZKUdW09cove6jn6rNeCoh0jAJOkkPWXMqBVYF6IRE6CeRsR7H_sCfwdUMWW0NwyW39U9Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتین خواجوی‌نیا، دانش‌آموز ۱۶ ساله رشته کامپیوتر، شامگاه ۱۸دی۱۴۰۴ در جریان اعتراضات مقابل فرمانداری شهر قدس، قلعه حسن‌خان، با شلیک گلوله جنگی کشته شد.
مادر آرتین ویدیویی از جمع‌آوری کفش‌های فرزندش منتشر کرده است؛ کفش‌هایی از دوره‌های مختلف زندگی او که حالا به یادگار مانده‌اند.
مادر این نوجوان کشته شده، نوشته است: «از اولین تا آخرین قدم‌های تو را مرور می‌کنم پسر قهرمانم. از لحظه‌به‌لحظه بزرگ شدنت حالا فقط خاطراتی برای من مانده که هر ثانیه از مقابل چشمانم می‌گذرد.»
«از آن نوزاد زیبا با آن لباس زرد در آغوشم تا آن مرد بلند قامتی که باید برای دیدنش سرم را بالا می‌بردم، تو همیشه یادگار مادر شدن من خواهی ماند.»
او فرزندش را «قهرمان جاودانه من» خطاب کرده و نوشته است: «هر لحظه و هر جا یادت جاوید و راهت پرنور.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78237" target="_blank">📅 17:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/78236" target="_blank">📅 23:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/toJRrN-7M4RFnIiTKfnCoFVfeb9eBfBcqmSMfeXu7vDAu1V2cZXdVZUXhw3teFBb_yhTwAy4trFip0qgSYMWbuvYsWDUiG4S2KACcClikqhgMK4m46C4Ap1omKgxWO0fB-hesL4BiVcypNBj5_NxKyvzQA2HtGCWIQuaSIdTvqg5sPoSYSlq_Nycs-I4hUvCTy0Nq9m6Cwga1RcZFxfSemcWGqMbAEIKeSAmECqcAVeBIKOflbLV67VBxrkCXefiVYncMb04_u1zPAbyCsSqjblR_agAavpz1A_ntTS3089q-eeaQOsACKHx3EAcdlWAFXUVhrxwPhH21unfstoWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده آمریکا همراه با بریتانیا، فرانسه، و آلمان در تلاش است شورای حکام آژانس بین‌المللی انرژی اتمی هفته آینده قطعنامه‌ای تصویب کند که پرونده هسته‌ای جمهوری اسلامی را برای نخستین بار در ۲۰ سال گذشته به شورای امنیت سازمان ملل متحد گزارش دهد.
خبرگزاری رویترز روز جمعه ۱۳ شهریور به نقل از دیپلمات‌ها و با استناد به متن پیشنهادی قطعنامه گزارش داد که چهار کشور در حال رایزنی با دیگر اعضای شورای حکام ۳۵ عضوی آژانس برای تصویب این قطعنامه هستند.
مذاکرات درباره متن نهایی همچنان ادامه دارد و پیش‌نویس هنوز به طور رسمی به شورای حکام ارائه نشده است.
بر اساس پیش‌نویسی که رویترز مشاهده کرده است، شورای حکام از مدیرکل آژانس خواهد خواست قطعنامه جدید و قطعنامه‌های پیشین مرتبط با برنامه هسته‌ای جمهوری اسلامی را برای اعضای آژانس، شورای امنیت و مجمع عمومی سازمان ملل ارسال کند.
در متن پیشنهادی همچنین بار دیگر از جمهوری اسلامی خواسته شده است موارد نقض توافق پادمانی خود را «فوراً» برطرف کند و اقداماتی را که آژانس و شورای حکام ضروری می‌دانند انجام دهد تا مدیرکل آژانس بتواند درباره صحت و کامل بودن اظهارنامه‌های هسته‌ای حکومت ایران اطمینان لازم را ارائه کند.
اقدام آمریکا، بریتانیا، فرانسه و آلمان ادامه قطعنامه‌ای است که شورای حکام روز ۲۲ خرداد ۱۴۰۴ تصویب کرد. در آن قطعنامه جمهوری اسلامی به دلیل همکاری نکردن کامل با تحقیقات آژانس درباره آثار اورانیوم در مکان‌های اعلام‌نشده، ناقض تعهدات خود در زمینه منع گسترش تسلیحات هسته‌ای شناخته شد.
یک روز پس از تصویب آن قطعنامه، در ۲۳ خرداد ۱۴۰۴، اسرائیل حملات به تأسیسات هسته‌ای ایران را آغاز کرد و ایالات متحده آمریکا نیز پس از آن به عملیات پیوست. بر اساس گزارش رویترز، تأسیسات غنی‌سازی اورانیوم ایران در این حملات تخریب شدند یا به‌شدت آسیب دیدند.
جمهوری اسلامی از زمان این حملات به بازرسان آژانس اجازه نداده است به تأسیسات بمباران‌شده بازگردند یا وضعیت باقی‌مانده ذخایر اورانیوم غنی‌شده را راستی‌آزمایی کنند. شورای حکام طی یک سال گذشته دو قطعنامه دیگر نیز تصویب کرده و از حکومت ایران خواسته است موجودی اورانیوم غنی‌شده خود را اعلام و دسترسی کامل بازرسان آژانس برای راستی‌آزمایی آن را فراهم کند.
آژانس بین‌المللی انرژی اتمی برآورد کرده است جمهوری اسلامی پیش از حملات به تأسیسات هسته‌ای، ۴۴۰.۹ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار داشت. بر اساس معیارهای آژانس، در صورت غنی‌سازی بیشتر، این مقدار می‌تواند برای تولید مواد شکافت‌پذیر مورد نیاز حدود ۱۰ سلاح هسته‌ای کافی باشد. آژانس میزان غنی‌سازی ۶۰ درصدی جمهوری اسلامی را «مایه نگرانی جدی» دانسته است.
جمهوری اسلامی می‌گوید قصد تولید سلاح هسته‌ای ندارد و فعالیت‌های هسته‌ای خود را صلح‌آمیز می‌داند. ایران به عنوان عضو پیمان منع گسترش سلاح‌های هسته‌ای حق استفاده صلح‌آمیز از فناوری هسته‌ای، از جمله غنی‌سازی اورانیوم، را دارد؛ اما آژانس می‌گوید جمهوری اسلامی تنها حکومتی است که بدون داشتن سلاح هسته‌ای، اورانیوم را تا سطح ۶۰ درصد غنی کرده است.
رویترز گزارش داده است در سال‌های اخیر هر بار آمریکا، بریتانیا، فرانسه و آلمان پیش‌نویس قطعنامه‌ای درباره برنامه هسته‌ای جمهوری اسلامی به شورای حکام ارائه کرده‌اند، آن قطعنامه تصویب شده است. با این حال، اقدام عملی شورای امنیت علیه جمهوری اسلامی ممکن است با مانع روبه‌رو شود؛ روسیه و چین که از متحدان حکومت ایران به شمار می‌روند، از اعضای دائم شورای امنیت و دارای حق وتو هستند.
@
VahidHeadline
نمایندگی جمهوری اسلامی در سازمان ملل در وین اعلام کرد این اقدام آمریکا، بریتانیا، فرانسه و آلمان نشانه «شکست کامل توهم مکانیسم ماشه» است.این نمایندگی افزود این اقدام نیز «هیچ سودی» برای این کشورها نخواهد داشت.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/78235" target="_blank">📅 21:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XdOuWtv5UmlhhrLunlywWLM3NQLnj1-ui8z8w23Tt3KPKUxAdWM4KnZ_w0ZGV1OeZGhidDlF2y3rdwNTZuJg8AvmBh1vVdI8wBQIaAo9rHettorFNpQC0uSenDOxDSAiYbF3IuBWAON-fro3KxjbVR12AYnm_dF-VmR_dDYXqds0CgJvcuQjH9GwI56RCh-aWj5hAFRDziD1gM6dhZvbXZKDDh66kuBp15FaPtnUxYVevTnGTBrW8NaHZIRNOue0POXXgtmGjiWdqtAVVp3BOsonWaR3tpWDa7JLjyKoLvgA6A_1TH2OorXRyRNG0nyTf7bCmyqQ06PeNLWor_y1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه شامگاه جمعه گزارش داد که موشک‌های پرتاب شده از سوی ایران، در شمال اردن رهگیری شدند. به گزارش این رسانه تصاویر رهگیری موشک‌های ایرانی در شمال اردن منتشر شد.
ساعاتی پیش از این گزارش، برخی کانال‌های تلگرامی نزدیک به سپاه پاسداران، اعلام کرده بودند موشک‌هایی از اصفهان، کرمان و کرمانشاه پرتاب شده است.
@
VahidOnLive
وزارت خارجه قطر جمعه ۱۳ شهریور در بیانیه‌ای اعلام کرد این کشور طرف درگیری نیست و حمله به خاک قطر را نمی‌توان توجیه کرد.
این وزارتخانه افزود موفقیت نیروهای مسلح قطر در رهگیری حملات جمهوری اسلامی، از خطر این حملات نمی‌کاهد.
وزارت خارجه قطر همچنین در این بیانیه نوشت «تاسف‌بار»است که با وجود مستند شدن رسمی حمله به راس لفان، وقوع این حمله زیر سوال برده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78234" target="_blank">📅 20:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JXd35j7zCe2ZQ98ja8ffy60bBSvOz9YK6flu7PMGEjjnvdb08p5Jx2rvhHxUzmpnrAMIpIKjvyarpq-Y6UoDk-d-cuVnN63Z_Qhuh0K7KifpAcWw5oiFUAGUKzlFYAMglY4ZgCSVdD59XtI8FWCj8veTqS2EmSAE7_u4DGSKnA63o8o6I7aApjZHFukdm-XpuR9PBQE6AqEpnvZ3c7GM90qav9hi0wg1azhsurcfcfbQHjJLSaL-Ubfzx1YMXBN75lNmPuRBu9FQilmgSKpk7YIS3jlGR-ib7ZNTEqsPYgH4dKEiYEhJy0N4ZUy1pUOksjJ7-BSnB74rs6cWoId6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا یک بانک مستقر در ترکیه و دو شرکت وابسته به آن را به دلیل تسهیل انتقال ده‌ها میلیون دلار برای نیروی قدس سپاه پاسداران و فراهم کردن دسترسی جمهوری اسلامی به شبکه بانکی بین‌المللی تحریم کرد.
وزارت خزانه‌داری آمریکا روز جمعه ۱۳ شهریور اعلام کرد «گلدن گلوبال بانک» و دو شرکت زیرمجموعه آن، «گلدن گلوبال وارلیک کیرالاما» و «گلدن گلوبال پورتفوی یونتیمی»، در چارچوب عملیات «طرد اقتصادی» به فهرست تحریم‌ها افزوده شده‌اند. هر سه نهاد در ترکیه مستقر هستند.
وزارت خزانه‌داری آمریکا همچنین در حساب رسمی خود در شبکه اجتماعی «ایکس» اعلام کرد این اقدام بخشی از عملیات «طرد اقتصادی» است و هدف آن قطع «شریان‌های حیاتی مالی» جمهوری اسلامی در ترکیه است. به گفته این وزارتخانه، گلدن گلوبال بانک و شرکت‌های وابسته به آن ده‌ها میلیون دلار تراکنش برای نیروی قدس سپاه پاسداران تسهیل کرده و دسترسی مهمی به خدمات بانکداری کارگزاری در اختیار جمهوری اسلامی قرار داده‌اند؛ دسترسی‌ای که امکان جابه‌جایی بین‌المللی منابع مالی حکومت ایران را فراهم می‌کند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، با اشاره به کارزار دولت پرزیدنت ترامپ برای قطع منابع مالی جمهوری اسلامی گفت مؤسسات مالی همچنان درمی‌یابند که ایالات متحده در اجرای عملیات «طرد اقتصادی» جدی است.
او افزود آمریکا امیدوار است بانک‌های بیشتری نیاز به تحریم نداشته باشند، اما این مسئله به این بستگی دارد که جامعه بین‌المللی به سرعت حمایت از حکومت ایران را متوقف کند. آقای بسنت همچنین تأکید کرد ایالات متحده به همراه متحدان و شرکای خود به اقدامات علیه شبکه‌های مالی جمهوری اسلامی ادامه خواهد داد.
بر اساس اعلام وزارت خزانه‌داری آمریکا، گلدن گلوبال بانک برای فراهم کردن امکان انتقال درآمدهای نفتی جمهوری اسلامی از چین به ترکیه ایجاد شده بود؛ درآمدهایی که پس از انتقال به ترکیه می‌توانست به پول نقد و طلا تبدیل شود.
وزارت خزانه‌داری می‌گوید این بانک همچنین آگاهانه پیشنهاد ارائه خدمات بانکداری کارگزاری به مؤسسات مالی جمهوری اسلامی را داده و از این طریق انجام تراکنش از طریق حساب‌های تحت کنترل نیروی قدس سپاه پاسداران و شبکه‌های وابسته به آن را امکان‌پذیر کرده است.
در اطلاعیه وزارت خزانه‌داری همچنین به شبکه «سیتکی آیان»، بازرگان ترکیه‌ای، اشاره شده است. ایالات متحده این شبکه را پیش‌تر در سال ۱۴۰۱ به دلیل نقش آن در انتقال صدها میلیون دلار درآمد حاصل از فروش نفت مرتبط با نیروی قدس سپاه پاسداران تحریم کرده بود.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، جمعه ۱۳ شهریور در شبکه اجتماعی ایکس نوشت از زمان برقراری دوباره محاصره آمریکا، هیچ محموله نفت خام ایران نتوانسته با موفقیت از تنگه هرمز عبور کند و به چین برسد.
او افزود نفت خام در کشتی‌های گرفتار در داخل تنگه انباشته شده و امکان جایگزین کردن ذخایر صادرشده وجود ندارد.
بسنت نوشت: «مسیر حیاتی صادرات ایران در حال قطع شدن است؛ نفت سرگردان، ظرفیت محدود ذخیره‌سازی و درآمدهایی که به‌سرعت در حال کاهش است.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78233" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78232">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DYF-45MgEqdIVuAwNIO-UccJS3tpAPbhWfEBWzvYwpAmCb3APqWxZvMY0mG4pxN6dGjGU6B5s-8bhGMiCS14vaVufG3YQJkfrwQ2zKensAw1Jo-RszSfBwYcR6EhVFia5pE13FFH9_UqFU2QZpLRihwYx3Tmeo1OAN0FhlKSFYwVUdjGvgu_mClaFYCdaKMy0trsLA1yBXPDOdubX65Qx2HyLp8Y7PVckALQOgRT8m0osj8S7j8yjhcVXxpjkwEMhKG277IRR89bogrBBw80KcPsqYXtvtPXut8wNn9Gecxbxhk4Bc0qUAHj92oXPaNHEIDJJl_pEL5UTbrWgzr2eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
دیوانه‌های چپ رادیکال، دموکرات‌های احمق و کمونیست‌ها ترجیح می‌دهند ما در جنگ ایران شکست بخوریم تا اینکه رئیس‌جمهور دونالد جی. ترامپ جنگ را برای آمریکا ببرد.
به عبارت دیگر، آن‌ها ترجیح می‌دهند ما ببازیم تا اینکه ما پیروز شویم!
این‌ها آدم‌های بسیار بیماری هستند که از TDS شدید رنج می‌برند؛ چیزی که گاهی از آن با عنوان «سندرم جنون ترامپ» (TRUMP DERANGEMENT SYNDROME) یاد می‌شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78232" target="_blank">📅 20:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78231">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byNFRBhsJ_cZXS0BKy13fkcSdyqBzEjXrhfEUS2mytVOrQjsUdmmLQyeiPYmFXIAGBwp0HDesjgbshYZzyN6LHb05djvH-nej4-JPJNBKMrxEoq1ThlsTo06Nk0_W8Qjv9Ze0EHtVb_dHtOD_Us5QYGS7HCCpAyJLf-nnZnMRZq5fcEr-ei9GWwIW2w_eMApSeiu_MB7APhohtBhJFol1s1sOU2vb7YlekCCSYBJm7bBoTeucc_9UOYXuXiohA2UjrSUXl0bOENaczAjnDKisfxzb88wkFt3aeWiNdvkDTM9tz4mzJXw_XaTJTpG7F7P1ICw20abDN-XyJDv3KaMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «فایننشال تایمز» روز جمعه ۱۳ شهریور در گزارشی اعلام کرد اختلافات میان ایالات متحده و جمهوری اسلامی ایران بیش از پیش بر سر آینده تنگه هرمز متمرکز شده است؛ چرا که دولت دونالد ترامپ بازگشت به یادداشت تفاهم اسلام‌آباد را رد کرده، در حالی که تهران خواهان احیای این توافق به عنوان زمینه‌ای برای کاهش تنش‌ها و ازسرگیری عبور نفت از تنگه هرمز است.
بر اساس این گزارش، تلاش‌های دیپلماتیک برای بازگرداندن طرفین به تفاهم‌نامه اسلام‌آباد که شامل توقف اقدامات نظامی، بازگشایی تنگه هرمز و آغاز مذاکرات جامع‌تر بود، با مخالفت واشنگتن روبرو شده است. آمریکا اکنون خواستار توافقی جدید و فراگیرتر است که علاوه بر وضعیت تنگه هرمز، پرونده هسته‌ای ایران را نیز شامل شود.
در مقابل، مسعود پزشکیان تاکید کرده که کشورش آماده است به محض بازگشت آمریکا به تعهدات خود در توافق موقت، به تعهداتش عمل کند.
با این حال، واشنگتن بر اهرم فشار میدانی حساب باز کرده و با تقویت حضور نظامی، مین‌روبی و ایجاد مسیرهای امن، سعی دارد ثابت کند ایران دیگر نمی‌تواند از تنگه هرمز به عنوان یک کارت فشار بر بازار انرژی استفاده کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78231" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SAR1rVCXH5KMEEzFsFBszLDm0ZL2vfKD2hMtpC28PBXEgDAaD3pdhHBrNZDBNW0PxCaspnAyPcvSseDef1eEZTEiuV01pQWHL8m5x_dy7J5Zl_nkcbGQjcTjTZM4PU_kz43zO9FnR0dXvu0yCIgEVzyIW-3D-Pi7smeepRPzsDWvnkhYBosDqO981NMs-tI0UCsLh2IQjrAjGsvecrYLHatef0ZhVhbo-hv3HWdlWN716qaK4fb2QsxH0zussJP52C4wPfOnjL13ZFw2LZmvgV1WnUiYjK4jtER_ztD6tleFLmNmaSiX7MAEmZhJpDD1H7L-Pd9cf2ik1zOjC8IjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت گازوئیل در آمریکا با ثبت رکورد تازه‌ای به بیش از پنج و نیم دلار در هر گالن رسید.
انجمن اتوموبیل آمریکا روز جمعه ۱۳ شهریور اعلام کرد که قیمت گازوئیل در این کشور در حال حاضر به پنج دلار و ۸۵ سنت به ازای هر گالن رسیده، در حالی که یک سال پیش قیمت آن سه دلار و ۷۱ سنت بود.
هر گالن حدود ۳.۸ لیتر است.
انجمن یادشده این افزایش قیمت را ناشی از اختلالات در حمل‌ونقل سوخت به‌دلیل جنگ آمریکا با ایران عنوان کرده است.
گازوئیل، سوخت حیاتی مورد استفاده در حمل‌ونقل جاده‌ای، کشاورزی و ساخت‌وساز محسوب می‌شود و بیم آن می‌رود که افزایش چشمگیر قیمت آن، نرخ تورم را افزایش دهد.
قیمت بنزین معمولی در آمریکا نیز چهار دلار و ۱۵ سنت به ازای هر گالن است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78230" target="_blank">📅 19:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/amvXggeITBVzIZNzsSBlFUEzz3Xdtd8OKbn-nQfas9X6YX4l0Fg_Mc2YbulvRgTnZDhb6nNgUZG94e64by63mXrg1wptFPgSunUdTLJsiXbuM30aNisO2fHVR6KtNmmv0uaDLkXQkZmG2j5okGl3Nk4KXck_THB4ta7nOeRbORDzIGQ0lkke8_YOXtEaK_8jmGVOf7Oi1P1sRMSOGOaHfn-c8rew5Fq3vF5skY2nZYElI_JGpGbcMfX7mVlHOzHzVHdVp8__T6_H-yW-nKhWP8HAN9DigdM73Vu37LhhyatP_p72e0O_7gELdzTZV5M-qk0WLHvhMYP1TwpvnGI45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌هایی که من دیروز دریافت کرده بودم:
▪️
آزمون Pte  زبان برای ساکنان ایران لغو شد
▪️
موسسه‌ی پیرسون هم تمام آزمون‌هاش رو برای ساکنین ایران کنسل کرد.
امروز صبح روی سایت اعلامیه زدن یک دفعه.
مشهورترین‌هاش برای ایرانی‌ها امتحان مدیکال کانسیل استرالیا و وزارت بهداشت عمان هست.
و امتحان‌ زبان PTE
▪️
ما جمعی از پزشکا برای مهاجرت استرالیا تلاش میکردیم و هزینه ازمونمون ۳۰۰۰ دلار بود
الان لغو شده بدون هیچ توضیح خاصی
دوستان هتل و پرواز بوک کرده بودند برن هند پیام بدن الان میگه نمیشه باید کارت اقامت کشور دیگه ارائه بدی
خبر:
موسسه بریتانیایی «پیرسون» که برگزار کننده آزمون‌ زبان انگلیسی «پی‌تی‌ئی» و آزمون ای‌ام‌سی (شورای پزشکی استرالیا) است، در بیانیه‌ای اعلام کرد که به دلیل تحریم‌های جدید آمریکا علیه ایران، آزمون‌های داوطلبان ساکن ایران را لغو می‌کند.
پیشتر در تاریخ ۷شهریور۱۴۰۵، تعداد دیگری از برگزارکنندگان آزمون‌های مهارت‌های زبان‌های خارجی، از جمله دولینگو و تافل، اعلام کرده بودند که این آزمون‌ها دیگر در ایران برگزار نخواهد شد.
پیرسون در اطلاعیه‌ای درباره لغو آزمون پی‌تی‌ئی آورده است: «در پی تعلیق 'مجوز عمومی G' توسط دفتر کنترل دارایی‌های خارجی (OFAC) در وزارت دارایی آمریکا، از ساعت ۱۲:۰۰ بامداد هشتم سپتامبر ۲۰۲۶ به وقت شرق آمریکا تا اطلاع ثانوی، ما قادر به برنامه‌ریزی یا برگزاری آزمون برای داوطلبان ساکن ایران‌ نخواهیم بود، مگر آنکه بتوانند مدرکی دال بر اقامت اصلی خود در خارج از ایران ارایه کنند.»
در ادامه این اطلاعیه آمده است: «آزمون‌هایی که در حال حاضر برای داوطلبان مشمول این محدودیت برنامه‌ریزی شده‌اند، لغو خواهند شد. به‌خاطر این مشکل که برای آنها ایجاد شده، پوزش می‌طلبیم.»
سرنوشت شمار زیادی از دانشجویانی که قصد مهاجرت با هدف ادامه تحصیل به کشورهای اروپایی، آمریکا، آمریکای شمالی و استرالیا را دارند تحت تاثیر این اقدامات قرار خواهد گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78229" target="_blank">📅 19:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=rxnVToQ6JvLyR88ysLx7hofzTcTMr3E9hf_JS2qAERHUTNtwzExyzTQWnMl4G0VAzkwFqtaiN_4OfuUG1ds3erXsJqjAzi9arGfxjSPBK8KnZbvYnxgtgHbqwb1fJ8znu9-xmCuTFQ5jVc_a2rX3JPeeFlQ5H0Klg2HTpVcmJ3RAw4eW3nY-NjrtkFi0fXAIm7Rdg_M_M5pFYzTZeOJlBHzcPkFfjpyID0mtxBA8NWTXXmyqKLelNH6AhpsnMhZeqpms1GJtKnoW8krQfMF8ny8ba4X10cbeenCsYJw5KCmes2hBSo6utmygerkTWCoLAGqpW-mi9hosn72W-m74oA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/113b0b4eab.mp4?token=rxnVToQ6JvLyR88ysLx7hofzTcTMr3E9hf_JS2qAERHUTNtwzExyzTQWnMl4G0VAzkwFqtaiN_4OfuUG1ds3erXsJqjAzi9arGfxjSPBK8KnZbvYnxgtgHbqwb1fJ8znu9-xmCuTFQ5jVc_a2rX3JPeeFlQ5H0Klg2HTpVcmJ3RAw4eW3nY-NjrtkFi0fXAIm7Rdg_M_M5pFYzTZeOJlBHzcPkFfjpyID0mtxBA8NWTXXmyqKLelNH6AhpsnMhZeqpms1GJtKnoW8krQfMF8ny8ba4X10cbeenCsYJw5KCmes2hBSo6utmygerkTWCoLAGqpW-mi9hosn72W-m74oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
الان از اصفهان موشک زدن یه دونه
سلام وحید جان
ساعت 7:12 دقیقه از اصفهان موشک شلیک کردن ( از سمت [....] اصفهان)
همین الان [...] اصفهان موشک رفت
19:13 از سمت [...] اصفهان موشک زدن
همین الان ۱۹:۱۲ از سمت [...] اصفهان
فکر کنم [...] بود
بالسیک شلیک شد به سمت [...] رفت
از اصفهان همین الان موشک زدن صدای وحشتناکی داد
اقا همین الان یه موشک از سمت اصفهان شلیک شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78228" target="_blank">📅 19:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rldvf1IZQlSwx9Pm2OSKOwoh8wHuMSabWH_2F8-bDmYigmHkOMBZOduQVXkNt0ntcx-eLURGjOcXPJ3C3fdPKwjUbLOwoROubU4ywHD-rKN3Ia9Tm7t38j11-4Zx1wA7TV3CZ3m_6y0W2j3LDWhgfwZWOHBHBT7UXIhgX1_hQ1MV9FU68pSbTCsI4orRIXinaS28OI330vxSJA1_Y6-NDHrM6I6QOqYJpXNIa6UMAnGzgU8GNUOvLAq1L0UEmBNsViMb7gTUY3xuBI3lxb6QaPMdnnPRiNxHNs_s_jHWFIwthVt_J6zIICxZXsl5VR_P7wzF5-2KDBWHVN0BB4wYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست پنج‌شنبه ۱۲ شهریور به نقل از یک مقام ارشد منطقه‌ای گزارش داد عمان پیشنهاد جمهوری اسلامی برای دریافت مشترک هزینه خدمات از کشتی‌های تجاری عبوری از تنگه هرمز را رد کرده است.
این مقام گفت مسقط حتی با دریافت داوطلبانه هزینه خدمات زیست‌محیطی و امنیتی از کشتی‌ها موافقت نکرده است.
یک مقام آمریکایی نیز به نیویورک‌پست گفت شرایط توافق پیشنهادی میان جمهوری اسلامی و عمان برای تقسیم درآمد نهایی نشده است.
این اظهارات در حالی مطرح شد که حسین محبی، سخنگوی سپاه پاسداران، پیش‌تر از دستیابی تهران و مسقط به توافق در این زمینه خبر داده بود.
رویترز هفتم مرداد گزارش داده بود عمان طرحی با حمایت کشورهای خلیج فارس به جمهوری اسلامی ارایه کرده است که بر اساس آن، مدیریت تنگه هرمز به شکل منطقه‌ای انجام می‌شد و شرکت‌های کشتیرانی می‌توانستند به‌صورت داوطلبانه برای تامین هزینه‌های ناوبری، حفاظت زیست‌محیطی و عملیات جست‌وجو و نجات مبالغی پرداخت کنند.
عمان پیش‌تر نیز با دریافت اجباری هزینه از کشتی‌های عبوری از این آبراه مخالفت کرده بود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78227" target="_blank">📅 02:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jRrywlqVBWo9f4RaWMbkM6Y3L3lbZcZDlUuAAFn_viAhaWoQpEuKiPlYUkBYTiReHrP32rAVBZRGbRt-H39ULRv_rWZ6BSnX8iO_6qB5LOs-uCVRVJ4PcBCXYD_9hL8vvhQVH2b0183HpbuXfo_Zc7ezujToM06L-vo1igix0Es6_Ome0gi1GmasNOi40_kq-J2_w0gQ3vwKg2CYhlHC8mvnRyl-JmX_t6UgVOmp98v-F6EEIriDLLyRXCR3NIvSdq3MKB6lz4qxmtXTXYcfABUOA59p0UWS3MeEX1fV6bv0jvNnz3rFJYJvdUAZnU_4tt9GJkb3Wx01ouO6HVcUdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QXhmMHH8ZDNq6DD6O8yojoSDDda5zxDFlAibZnSMhkwg_eBq6xzg3ry0sIEnwxDK5DwyrZwj_RgWF1XqylpWKLESNuR86XM7llJfYDq1v_hKQSgqca__84jox1U5oTGKrrvsFREcfwbdIaFQaFHi0vNKkslhvpHCtt2kNi7m0looXQMCfS8FcIo-pbBdLj9KPwbtXi12YI31iuz3ztyKosLO9ZgyzYaGfL-wD6S_OJiR4bte4kThFMPNaHOr7axb3NwsHnrGyEngk2y8XorHmnrEyxTF2uOhHHyZcdQd_ryIdalWQHtHrSbN9psd4tr0sIhslbP3CCmbspXUA_FWDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگو با شبکه جی‌بی نیوز گفت:
«آن‌ها سه سایت داشتند و شاید حالا کوه کلنگ گزلا را هم داشته باشند، اما ما روی همه این مناطق دوربین داریم. می‌دانیم چه کسی وارد می‌شود و چه کسی خارج می‌شود.»
او در ادامه درباره توان اطلاعاتی آمریکا افزود: «حتی می‌توانیم از فضا اسم افراد را بخوانیم. آن‌ها حتی نمی‌توانند بدون اینکه ما متوجه شویم جابه‌جا شوند. ما دقیقا می‌دانیم چه خبر است و از این بابت کاملا مطمئن هستیم.»
@
VahidOOnLine
گفت:
ما کنترل کامل تنگه هرمز را در اختیار داریم. هر شب ۳۰ تا ۴۰ قایق آن‌ها را از بین می‌بریم و رادارهایشان را هدف قرار می‌دهیم.
او همچنین افزود اقتصاد ایران «در حال فروپاشی» است و افزود: تورم ممکن است به ۳۰۰ درصد برسد، پولشان تقریبا بی‌ارزش شده و نرخ برابری آن با دلار حدود دو میلیون به یک است و هر روز هم بدتر می‌شود. آن‌ها واقعا در وضعیت بسیار بدی قرار دارند.
@
VahidOOnLine
گفت:
با جلوگیری از هسته‌ای شدن ایران، اروپا و بریتانیا را هم نجات دادم
«من کشور شما را هم از این تهدید نجات می‌دهم، چون اگر ایران سلاح هسته‌ای داشت، احتمال اینکه از آن در اروپا استفاده کند بیشتر از آمریکاست، زیرا توان موشکی برای رسیدن به اروپا را دارد، نه آمریکا.»
او همچنین افزود ایران تنها «دو تا چهار هفته» با دستیابی به سلاح هسته‌ای فاصله داشته و حملات آمریکا این روند را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78225" target="_blank">📅 02:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پاسخ جی‌دی ونس معاون رئیس‌جمهور آمریکا به پرسش‌های خبرنگاران
بخش‌های مربوط به ایران با تشخیص و ترجمه ماشین
متن زیرنویس:
https://telegra.ph/vance-09-03-3
خلاصه‌ای از اون متن مفصل به تشخیص ماشین:
1️⃣
ونس: «تنها دلیل اینکه بحران جهانی انرژی نداریم، رهبری ترامپ است»
▪️
«دلیل اینکه قیمت بنزین اکنون این‌قدر بالاست این است که ایرانی‌ها به کشتیرانی تجاری شلیک می‌کنند.»
▪️
«فقط دیروز حدود ۱۵ میلیون بشکه از تنگه هرمز خارج کردیم.»
▪️
«ایرانی‌ها دارند می‌فهمند که کنترلشان بر تنگه هرمز عملاً از بین رفته و این اهرم هر روز کم‌ارزش‌تر می‌شود.»
▪️
«توصیه من به ایرانی‌ها این است که دست از رفتار مثل آدم‌های دیوانه بردارند و به کشتیرانی تجاری شلیک نکنند.»
▪️
درباره حمله به مراسم عروسی: «در این مورد مشخص، من فکر نمی‌کنم اطلاعاتی داشته باشیم که چیزی را به این سو یا آن سو ثابت کند.»
▪️
«ایالات متحده هرگز در جنگ غیرنظامیان را هدف قرار نمی‌دهد.»
▪️
«در حال بررسی آن هستیم.»
2️⃣
ونس درباره ایران: «فشار اقتصادی، نظامی، دیپلماتیک و مخفیانه؛ همه روی میز است»
▪️
«ابزارهای اضافی زیادی هم در اختیار داریم. رئیس‌جمهور از برخی از آن‌ها استفاده می‌کند و از برخی هم نه.»
▪️
«هر اتفاقی که ممکن است بیفتد روی میز است: فشار اقتصادی، فشار نظامی، فشار دیپلماتیک، فشار مخفیانه.»
▪️
«ایرانی‌ها مثل تروریست‌ها در تنگه هرمز رفتار می‌کنند.»
▪️
درباره احتمال حمایت از مخالفان ایران: «البته، من قرار نیست درباره‌اش صحبت کنم.»
3️⃣
ونس: «آمریکا تنها کشوری است که می‌تواند کنترل تنگه هرمز را تضمین کند»
▪️
«ما تنها کشور دنیا هستیم که می‌تواند کنترل تنگه هرمز را تضمین کند.»
▪️
«ایرانی‌ها دوست دارند صفر میلیون بشکه از تنگه هرمز خارج شود. دیشب ۱۵ میلیون بشکه از تنگه هرمز خارج شد؛ و این به‌خاطر ایالات متحده آمریکاست.»
▪️
«اگر ما این کار را نکنیم، هیچ‌کس دیگری نخواهد کرد.»
▪️
«پیام ما به ایرانی‌ها ساده است: باید شلیک به کشتیرانی تجاری را متوقف کنید.»
▪️
«ما با آن‌ها صحبت نمی‌کنیم و صحبت هم نخواهیم کرد مگر اینکه شلیک به کشتیرانی تجاری را متوقف کنند.»
4️⃣
ونس: «برای پایان درگیری با ایران ضرب‌الاجل مصنوعی تعیین نمی‌کنیم»
▪️
«باز هم، من اسمش را جنگ نمی‌گذارم.»
▪️
«عملیات عمده رزمی حدود شش هفته طول کشید.»
▪️
«با عملیات Midnight Hammer تأسیسات هسته‌ای‌شان را نابود کردیم.»
▪️
«با Epic Fury، پایگاه صنعت دفاعی آن‌ها برای تولید سلاح و همچنین بخش بزرگی از توان نظامی متعارفشان را نابود کردیم.»
▪️
«یک ضرب‌الاجل مصنوعی تعیین نمی‌کنیم.»
▪️
«غیرمسئولانه خواهد بود اگر راهبرد و جدول زمانی‌مان را برای کشوری مثل ایران تشریح کنیم.»
5️⃣
ونس: «توان ایران برای مختل کردن زندگی عادی آمریکایی‌ها بسیار محدود است»
▪️
«اطمینان زیادی داریم خاک کشور امن است.»
▪️
«ایرانی‌ها تلاش خواهند کرد کارهای زیادی انجام دهند که توان انجامشان را ندارند.»
▪️
«اگر توان ایران را برای مختل کردن زندگی عادی آمریکایی‌ها در نظر بگیرید، به نظرم بسیار محدود است.»
▪️
«صفر نیست، اما بسیار محدود است.»
▪️
«من خیلی بیشتر نگران حملات سایبری از سوی بازیگران دیگر می‌بودم.»
6️⃣
ونس: «چین به برخی درخواست‌های آمریکا درباره ایران پاسخ مثبت داده است»
▪️
«ما قطعاً چندین گفت‌وگو با چینی‌ها داشته‌ایم.»
▪️
«فکر می‌کنم چینی‌ها به برخی درخواست‌های ما پاسخ مثبت داده‌اند.»
▪️
درباره تماس مستقیم ترامپ و شی: «در واقع نمی‌دانم آیا رئیس‌جمهور مستقیماً با شی صحبت کرده یا نه.»
7️⃣
ونس: «کشورهایی در خفا برای مجازات ایران به آمریکا کمک می‌کنند»
▪️
«فکر می‌کنم جمهوری خلق چین قطعاً بسیار مسئولانه‌تر از ایرانی‌ها رفتار کرده است.»
▪️
«اگر به ترکیه، آذربایجان، امارات، عربستان سعودی، قطر و بسیاری از کشورهای ائتلاف عربی خلیج [فارس] نگاه کنید... کشورهای زیادی هستند.»
▪️
«گاهی حاضر نیستند علناً بگویند، اما در خفا کارهای خوب زیادی انجام می‌دهند تا به ما کمک کنند مطمئن شویم ایرانی‌ها بابت شلیک به کشتیرانی تجاری هزینه می‌دهند.»
▪️
«این کار همچنین منابع اقتصادی لازم برای بازسازی برنامه هسته‌ای‌شان را از آن‌ها می‌گیرد.»
▪️
«تا اینجا ندیده‌ایم که تلاش کنند چنین کاری انجام دهند.»
▪️
«همه این‌ها در خدمت این است که مطمئن شویم ایران به یک قدرت دارای سلاح هسته‌ای تبدیل نمی‌شود.»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78224" target="_blank">📅 01:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ونس: نسبت به احتمال نقش آمریکا در حمله به مراسم عروسی در سیریک بدبین هستم
🔸
معاون رئیس‌جمهور ایالات متحده می‌گوید تحقیقات دربارۀ «ادعای حمله به یک مراسم عروسی» در جنوب ایران ادامه دارد.
🔸
جی‌ دی ونس که روز پنجشنبه ۱۲ شهریور در کاخ سفید به پرسش‌های خبرنگاران پاسخ می‌داد، در پاسخ به سوالی در این زمینه گفت: هنوز اطلاعات کافی در اختیار نداریم اما ارتش ایالات متحده «بر خلاف سپاه پاسداران» هرگز غیر نظامیان را هدف قرار نمی‌دهد؛ اما گاهی ممکن است «اشتباهاتی» رخ دهد.
🔸
معاون دونالد ترامپ در ادامه گفت: نکتۀ مهم این‌ است که حتی در صورت بروز اشتباه هم، نیروهای مسلح ایالات متحده، «باز هم بر خلاف سپاه پاسداران»، از اشتباهاتشان درس می‌گیرند تا چنین اشتباهاتی تکرار نشود.
🔸
ونس در نهایت با تأکید بر این‌که تحقیقات ادامه دارد و هنوز اطلاعات کامل نشده، گفت شخصاً نسبت به احتمال نقش آمریکا در بروز این حادثه «بدبین» است.
🔸
به گفتۀ مقام‌های ایرانی، در جریان حمله شامگاه ۱۰ شهریور آمریکا به یک مراسم عروسی در کوهستک سیریک در نزدیکی تنگهٔ هرمز، چهار تن از جمله یک کودک کشته و ده‌ها تن زخمی شدند.
🔸
وزارت دفاع آمریکا از ۹ اسفند‌ ۱۴۰۴ و حادثۀ حمله به یک مدرسه ابتدایی دخترانه در میناب هم اعلام کرده که مشغول تحقیق است، اما بیش از شش ماه پس از حادثه و با وجود فشار کنگره، هنوز حاضر به انتشار نتیجۀ تحقیقات نشده است.
🔸
مقام‌های جمهوری اسلامی می‌گویند که در جریان حمله به مدرسه شجرۀ طیبه، بیش از یکصد دانش‌آموز،‌ معلم و اعضای خانواده‌های دانش‌آموزان کشته شدند.
@
VahidHeadline
بعدا ویدیویی زیرنویس شده شامل حرف‌های احتمالی دیگر می‌گذارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78222" target="_blank">📅 22:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A6wGidt-erlMFVXTbM5snY845fs7CZh9tSXqJwfOjPVj3WP34DYmwvx9DRgYCKGjgwVFQbSxhrAeoxH3ViFubTYqtH09kDb4sJSIdkD8QHOIdP9jBDkP587nvvbdwLU8c7_29gwXFwhP3Q9wKLNaT5HNFCn3r6Vkv3RRHlu1ULobIi1rgIdZY90gJWNTXu5h78k85uAtWQshdf_EhbojhhMMuOFP7c2Za8oqDsPkgQGOd4thyH5-Re1L9urYYuR5RHj6UdgozbqkmIVtkyWVAIhhiOdDZ4BYcdNuPcagatzb2ieTZz4P8N3w_8cr56gsHTUeI2bz59IVT1wiTZZk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a2_XNXvTeSPeGdeA39VOjPpXk7caL03wasSk6HugGmzaBPt_G1px1UiQYKiVLamrBtXy6OauinFF1JskjlO6ziwU24jN9P8UHu0YQdI91hFpwPojy8iL1YWY8kTa8hDqH5RBRQJ3xOhR24NFG1NHFXj30sfWfIYUR1r8iRune_zkiGnB-kFtdexlUe281uKykVv76Uts-xe1veS01gYw_5mWF2iCZLysG_QfJ_vip-dcPNBj8wPve0StJ5Kb92j2x3_iPyacSHTomnCDvgWuMVcb9jVq6pg5CoYvcLR6lafnwTI54KCT26Lkm2AlIwQPpD1jgn1ofRpAOdYsjEAlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hX9mpNAnkQC6Pb0_tHBV7JrMkgqtr09ErPPxkSxMn7RzofmyLyWVY4T-Zn81a-rHxlCRTTUTVn7mo27Vj60JzHc4uNCsU68NGOAU0uEosBmmHWnVPtZ0nOPaXhGZ2ZvMZY0xvPRpZ96goSBJlPDxvYXEqu5sGhRBK0h26s-wsE9M12etW12Kv49DXQ5iN7K5CXybxgVmRGG9BmqEpIg5cRymXyYdlBOhSyPLN_oHRD9ckAVG3qeEdDtD3lTufSY7rImkKhupYIXx_W012-7lTgskX5Qx_jq7qMJfI4lyXjQOKrEy4dSf25Hrix-lyYFHafHwchwL2dQ1Wsa_bPbIQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📝
درباره حمله به مراسم عروسی در سیریک چه می‌دانیم؟
🔹
همزمان با حملات هوایی آمریکا به شهرستان سیریک در شب ۱۰ شهریور ۱۴۰۵، انفجاری خانه‌ای را در بندر کوهستک تخریب کرد که در آن مراسم عروسی برگزار می‌شد. بر اساس گزارش‌های منتشرشده، تاکنون پنج نفر، از جمله یک کودک چهار ساله، جان باختند و ۶۵ نفر مجروح شدند.
🔹
تصاویر محل حادثه، صدای چند انفجار در ویدیوی دوربین مداربسته، بیانیه سنتکام و تکذیب‌نشدن حمله از سوی سخنگوی این نهاد، انتساب حملات آن شب به آمریکا را تقویت می‌کند.
🔹
همزمان در شبکه‌های اجتماعی ادعا شده بود که انفجار خانه نتیجه «پرتاب ناموفق موشک سپاه» بوده است؛ اما تاکنون هیچ گزارش رسمی یا مدرک معتبری این ادعا را تایید نمی‌کند.
🔹
برخی حساب‌ها برای اثبات این ادعا، ویدیوهای قدیمی یا نامرتبط را منتشر کرده‌اند. تنها گزارش مشابه درباره یک پرتاب ناموفق سپاه در همان شب، مربوط به خمین در استان مرکزی بوده و ارتباطی با سیریک در جنوب ایران ندارد.
🔹
با وجود شواهدی که از حمله آمریکا به سیریک وجود دارد اما هنوز مشخص نیست دقیقا چه پرتابه‌ای به خانه محل برگزاری عروسی برخورد کرده است.
🔹
این در حالی است که در ویدیوی دوربین مداربسته، صدای پهپاد شنیده می‌شود و پدر عروس نیز در یک مصاحبه تصویری به شنیدن صدای پهپادها اشاره می‌کند؛ شواهدی که احتمال استفاده همزمان از موشک و پهپاد در عملیات را تقویت می‌کند.
🔹
این در حالی است که قطعاتی از موشک کروز SLAM-ER در منطقه دیده شده، اما میزان تخریب خانه با انفجار کامل سرجنگی ۳۶۰ کیلوگرمی این موشک سازگار به نظر نمی‌رسد.
🔹
احتمال دارد خانه با مهماتی کوچک‌تر، (مثلا پهپاد لوکاس با سرجنگی حدود ۱۸ کیلوگرمی) هدف قرار گرفته باشد و قطعات SLAM-ER به اصابت دیگری در همان محدوده (دکل مخابراتی در فاصله حدود ۱۳۰ متری) مربوط باشند.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78219" target="_blank">📅 20:15 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KlC_ppN6w4jNRiuSqDSuCvGo1KlQ2L3NYEsz3k2443xL1Afs7nCP6gRQR-dz5tawT3x1_aPIZrcWeaHMvIEf8SuC9Jvp5ZPhruKdZZLGAaMcBUoSKVoyNyV4wGoa480Ch_DwjNqnxkPHYRE3n_nZbsbcXIrvZlaPEFzIp4Vfw-2VkblAsSwbY97lrgafrNcr7Qz8S342-R_xk1IHFFqSTussEQhbjA7xWpxkxbaPQTWozoqRmyJtFhvcxVGpro2c4LKHcBoVzYqdb1xDupRVkIWDYdKE-ARGDfNmY_KYUl14xBoZzwhcpx-A8_9pGnLjm_j1Y2zvYzjg3p7IYDq4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست‌ها که در گوشه کادرشون نوشته شده Ad تبلیغاتی هستند که به خود تلگرام سفارش داده میشن.
من نمی‌تونم جلوی نمایش‌شون رو بگیرم:
https://t.me/VahidOnline/73400
https://t.me/VahidOnline/77482
https://t.me/VahidOnline/77989
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78218" target="_blank">📅 19:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twhatFmn-l389oKtkCPaBijaKhZqqxubsS9og1zQMQJpk-fPkdY7pRP3YoSKDvDbLNkB_nI0BLw57D300E2TQ-osbCCVbc31sy_0PS4JfcqJZcDgjo3pS6mYd4Aj9x1JEqdjsdEcDB2FctaAGtMDdXKTvSJvtn-bX44-382J0EKFKAB3h5REW12yvZSXmEx_YHBLV60_FlNy1NKEv2u5cvGOxyLw0j1OOeysj2VqxilpYD2HN1dzp9-_EEmtT0ZyfHZlhXQLUPFHHHywfd5M5fnccmP3-ZbXWBmZ4XsJafCyI5tfvpNsa9XX_l28ptUQ6EQ1E-9ZErQ0TF06ZBBSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
برای آن آشغال‌های خائنی که حاضر نیستند درباره عملیات نظامی ما در ایران گزارش دقیق بدهند: ما عملاً مقادیر نامحدودی مهمات با کیفیت متوسط تا بالا در اختیار داریم؛ بسیار بیشتر از آنچه بتوانیم در این جنگ یا هر جنگ دیگری ــ که وقوعش بسیار بعید است! ــ مصرف کنیم. علاوه بر این، ما در سطحی بی‌سابقه در حال تولید مهمات هستیم. در حال ذخیره‌سازی و آماده شدن برای هر وضعیت احتمالی هستیم که ممکن است پیش بیاید. این مهمات را برای خودمان، ایالات متحده آمریکا، نگه می‌داریم، به‌جای اینکه آن‌ها را به دیگران بفروشیم؛ اما فروش به متحدان نیز به‌زودی دوباره آغاز خواهد شد.
همچنین لطفاً همه بدانند که دولت بایدن بسیار بیشتر از میزان مهماتی که ما در ایران مصرف کرده‌ایم، مهمات را کاملاً رایگان در اختیار اوکراین قرار داد. صدها میلیارد دلار بدون دریافت هیچ هزینه‌ای به اوکراین و ناتو داده شد؛ پولی که اروپا حاضر بود بابت آن بپردازد ــ اگر فقط از آن‌ها خواسته می‌شد. اما ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
از توجه شما به این موضوع متشکرم.
رئیس‌جمهور دونالد جی. ترامپ
truthsocial.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78217" target="_blank">📅 18:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cB3JhYaLSAlQnlgqeqtwp_auQ-JF2bzsSVNxg0Cqi8yhykc4ZQgJK4vpoOOMHY2hzIK-Wvs-TVjMtgnsfI11XxYjKSww9Yg93cpMaoEggvSknlvCXAZYlRdz_5WXXJClqnUihdo6cmLac5PFQoyjjPVaDz8yYzvakqVGeEInoo5BmbYAR4Iyk3dHuk8e3GsCsd-7drpeXFvrEqUJJoQGQvHq-YABGfDnX4Q5v-8sOZi7Pw4Cw-IutZLN_ksGmWCCxetCfcETm_UsJv6C-HpP0Bux69gh_z8KyLG5O5XCxKBm5vIyZiGZLRvrFOK1PGOluVkAhZMZQKMrPOKN_1Qjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رئیس‌جمهوری اسلامی ایران، روز پنجشنبه ۱۲ شهریور هشدار داد که «ماه‌های تاریکی» در انتظار اقتصاد ایالات متحده است و از مردم آمریکا خواست اقدام به ذخیره‌سازی سوخت و بنزین کنند.
او تاکید کرد که «جنایات جدید آمریکا»، دکترین دفاعی خود را به تاکتیک‌های «نامتوازن» و «چندلایه» تغییر داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78216" target="_blank">📅 17:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pDayUoyUKtgynzcBAfJT0rXJbJ9nTNX1n8_Ke3u5x1QQl8Zhh_RMLLyYiKlsQOm8qibRuW1lzGoAOUCwaorVyc53n5SGlskUAXK36254iKkoVjVrZOR3Aj_2cL1Ufpce6WTQVCjBJHQ0sYX7DppJlidpcVK6ch1u6kOd4RTGjI1N03y5UOmIlGO1YIBOJZ2vp_hyga_6DtndWBeTJ6YndFMfa7H8fyqRpYutvHxdTXLSgjq0r5eGPFLrWFMcy0EFWLbp9wNXqBJXDBdV1HgaJiFtl0xtBVOjBe9URODqA45YwOEFSpIsX3TRjVJ6qgtrBZJPHHCAtz1-BXmt3OiUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">916208
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78215" target="_blank">📅 16:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KBAjWnP6Udy9Zq8NrEb_SwiJY46HXX56EdhVhhQNLDr-K2ZqNsak-R1hQJnHNe3wm-u-JpT9E4ehILa1k2y-V4vfLjLyQ-cOlIc0ZR4_lB6LKh-XqDrZM-n4WBXphZLTKSRq9Mqq1qrqNKTSybeZCuM5-RCNQZoXRfv8TUfJjwuLCzEhtv8myEByxrdyZxtrE83TOMOg6ABc4Edi1dXHZH_CdVqtdGypmLplkqbPW9h32g7Tij5p1mONRJBKc3tCRzbwvkNHOG6Gfe21F6AsyC-0KIk8FZ8T4Z9hgs0jLaF9AIvBmTgwEy4sX_oDkYRQ4j4sRRafot3c7Ep_deNvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا با انتشار تصویری در شبکه اجتماعی تروث سوشال، مجموع حجم نفت و گاز مایعی که پیش از جنگ از تنگه هرمز عبور می‌کرد را با میزان کنونی آن مقایسه کرد و نوشت: «حجم نفت هرمز بازگشته است!»
ترامپ در این تصویر، مجموع حجم نفت و گاز مایع عبوری از تنگه هرمز در زمان پیش از جنگ را حدود ۲۰ میلیون بشکه در روز در نظر گرفت و میزان عبور این مایعات در حال حاضر را ۱۸ میلیون بشکه اعلام کرد.
این در حالی است که سامانه پیگیری موقعیت نفتکش‌ها در جهان، میزان عبور نفت و گاز مایع در ماه گذشته را به‌صورت میانگین ۷.۵۴ میلیون بشکه در روز اعلام کرده است.
بر اساس داده‌های این سامانه، حداکثر میزان عبوری در یک روز، ۱۰ میلیون بشکه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78214" target="_blank">📅 16:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78211">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BoXEQO5hc7S6v8EYRnu6n9ZfMPmbTr3JjS6jVafINBH7h9bCKDvIRbiys2KWRlVQ2Ktos7-I9NIeXgL_fdvDcf_IpiJJKboSPetbkI7xLynkXyTvK9wdhC-SMBmP4vyPe3LTjt2V50gGLFrQBIiqzyTt8nqUgcWpJfqdk9GfULWjzR6y84bTUkK_-Fiu83i-ihbfud9H3rnPTnusosb9DAkcXZBiOLTg3-52qx2bBU6ZURuk-chyS8145jOPTfo6BJENTzokufOP5cIm-sJoxpizjNx_u8G-4NXjoSvBTn4U7gr2yC42-4ryeCouJc6U6sYGnqmRuKALU5xFouxrmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iZMdqrcbfcVl4FJnYfx-EEB4sRDpBqU3WAGscA_s6Avh2CjAmLp7dU_ZIAym3lz-kWnbR8HjKA0sHSNyepHNn-Vag-04YFS0pi6591jxBPtQMFNpKegCt5jJ2dNMeqAp_8VC__Y8pPBCtuVxkzmoYKMLqquj52dxwhthWAfrgkVW6ynvj3OqpTWYbBoj39G25oZmyKuxbCkORmjvTrltRP_7ke0B717_G86XhSO_aPB8E3ujKWuV4c6obhY6mEKX-dlw7pg1devveejlAWDzrXp6eSWuaXIvPqA1zr6a8ik5qeUD4aJS0nqwXLbZsMhYfNOW7HW4GctOYO5u1FL0nQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=Q4nrEsgYmKryNVX1XRUvAnKRp0dsYHnoPDew1CQXftwlpLc6uwiMbJt6AhnXU3gMuIHcyW0BfhDUbG_SokB9X176UTmCH88B0BYbvrCxFuoI7Q5aitsRWx3J5AUX8LKLcmmV3tgaW7au2f8QHdV3cXJ4_DEfeGJ6zKH9jxtku9uf1xByAuId26m_MwEWN0sRENuhVN2Q163I8SDD1Ctjv1_B1srLzzfXCgpV1a_nxOCeZwK_nwcCjeem3gaRzDEO2_TNS18mI0QPoHgeOglugnrg8gkkDSJhx-96XjO3_P7H1QfKXr5rorA0Ja_ENyneWmK5xaT9ylQikNSsqX92kA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6484aadc92.mp4?token=Q4nrEsgYmKryNVX1XRUvAnKRp0dsYHnoPDew1CQXftwlpLc6uwiMbJt6AhnXU3gMuIHcyW0BfhDUbG_SokB9X176UTmCH88B0BYbvrCxFuoI7Q5aitsRWx3J5AUX8LKLcmmV3tgaW7au2f8QHdV3cXJ4_DEfeGJ6zKH9jxtku9uf1xByAuId26m_MwEWN0sRENuhVN2Q163I8SDD1Ctjv1_B1srLzzfXCgpV1a_nxOCeZwK_nwcCjeem3gaRzDEO2_TNS18mI0QPoHgeOglugnrg8gkkDSJhx-96XjO3_P7H1QfKXr5rorA0Ja_ENyneWmK5xaT9ylQikNSsqX92kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">dadban4
:
"امیرعلی قنبرزاده، بازیکن تیم نونهالان آکادمی بسکتبال پاس، روز ۱۹ دی ۱۴۰۴ در گرمدره استان البرز کشته شد.
مادر او با انتشار این ویدیو نوشته است:
«امیرعلی عزیزم، دل بارانا برات خیلی تنگ شده، جات برای مامان خیلی خالیه.
شادی را به گور خواهند برد، آنان که رنج را در ما آفریدند.
ما مادران نه می بخشیم و نه فراموش می کنیم.»
امیرعلی قنبرزاده در جریان اعتراضات، جلوتر از دیگران حرکت می کرد و دست هایش را باز کرده بود تا از سایرین محافظت کند.
او در همان حال با اصابت سه گلوله جنگی به سرش، جان خود را از دست داد."
abelbalb
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/78211" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78210">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFH8LbefLS-qjAaBg_G-k7Oe5hZqJoa6gPpnb9_-Jui9abuHE8V8FzAaDRE0n8mjGrJHCspWUjXiTH30nNe4aGp8gmYZfy41Zu912RM8kxde6HZ4LF_9P3pWxQLFIqCqlDDzjvMJRJOb72ECxHHlczBMxT7RjUu5BOBKyNxsU3Ylz2aTekp1GRs3E8U_0HM7CAbKSlio6OWkGOP3fGC4tgF6lFNeseobpZwhSMsRhCPyX7si82E21qka2W9roXkpajdE37vvQ3VLIGUlIjnIS6bBQDOzUiX0zhXciD-8jo71qa7TcKcUNFdLN6LmsspoIsmtYaRc7uDpEpea7ZvQwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، نزدیک به سپاه پاسداران، از کشته شدن سه خلبان ارتش جمهوری اسلامی ایران در حمله سه‌شنبه شب آمریکا به ایران خبر داد.
این خبرگزاری با انتشار اسامی و تصاویر این خلبانان گفته است دو نفر از آن‌ها از خلبانان نیروی دریایی و یکی از آن‌ها از خلبانان نیروی هوایی ارتش بودند، اما اعلام نکرد در کجا و چگونه کشته شدند.
با این حال، اسامی اعلام‌شده سه نفر از هفت نفری هستند که روز چهارشنبه ۱۱ شهریور اعلام شد در حملات آمریکا به شهرهای اهواز و آغاجاری کشته شدند.
در جریان حملات شامگاه سه‌شنبه آمریکا، به‌‌گفتهٔ مقام‌های ایران، مناطقی از جمله فرودگاه جیرفت در جنوب استان کرمان، عسلویه، کرمانشاه، مناطقی در استان خوزستان، شهرهای چابهار و کنارک در استان سیستان و بلوچستان، سیریک، لاوان، قشم و بندرعباس در استان هرمزگان هدف قرار گرفتند.
سخنگوی وزارت بهداشت صبح پنجشنبه از کشته شدن «۱۸ نفر و مجروح شدن ۱۴۲ نفر» در جریان حملات اخیر آمریکا خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78210" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JPh-yBw2_Uxqi9VorJaiLbcXtJZiTHehS67721Z6lkLU4sc6KKHRommxwC0lwEd9SaVCYxVHrAeXCAAiI814QMYg-X_eh_ymrsDWwCDV8Q-z0HUu2PbJb0zBXkNp8_tA0XohrSp9Tz1px0vvmnlAPJtUqKefL3hZDXW4UzUt5DiYMN6AiV8ioy74ovYEm4ygs3lW7t22yvPj1UAGYY8xRBltoGkjEx8560RkR-Uizy0IMaIJV83WyC5J5SzYlir9-8TeTt6BeQgTFgdIu4PczcM2h9he-CN2cNQQ8MhQRfLnpPMot0AlRNehMQmjrs05Op_DPvjT1k8hWD_uAjlOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">quotes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78208" target="_blank">📅 15:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D2rq3QOHWqgqldAOJOXXSiq5D78UF3yt_cepJCBLSJ8UiGb5TbEiUn0OphSugEfXuYZ2s643L70W7Z1ws8kLxH9x9JnSbe6d_c0XZ0y_rGuZj2nBf8i_oMRVhb23XWZAvg0yOd-B3LP0ZOS_b9KWjki23y3m9gMxUxfGIUdDt9a16C96ziAN7OyNnYmWtk33AJRLMW2i0yacoD3iIAOViAq4vyQ-LdtBNtNpaCedbKGzkZUa78t_lFyQxSsWodQ0mSqMkqh7lG7Y-Bj13HrvAH448dZ0aaPRGTCytjE4y8WPAmyT9C0TcWXCgTbcyNGNvKYUiI87GC3rn3c2umhlaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، پنج‌شنبه ۱۲ شهریور در مراسم روش هشانا با کارکنان وزارت دفاع اعلام کرد حمله جمهوری اسلامی به این کشور، اسرائیل را از همه محدودیت‌ها رها خواهد کرد و این کشور حتی زیرساخت‌های انرژی را نیز هدف قرار خواهد داد.
وزیر دفاع اسرائیل گفت: تمام زیرساخت‌های ملی، نظامی و غیرنظامی، از جمله زیرساخت‌های انرژی را هدف قرار خواهیم داد و ایران را به اعماق عصر حجر و تاریکی بازخواهیم گرداند.
کاتز همچنین افزود: فشار اقتصادی و نگرانی از قیام و سقوط حکومت ممکن است جمهوری اسلامی را به اقدامات از سر استیصال سوق دهد.
او گفت: حکومت آیت‌الله‌ها در ایران به‌خوبی می‌داند چرا پس از آنکه دو بار ضربات سختی به آنها وارد کردیم، برنامه هسته‌ای را نابود کردیم، خامنه‌ای را کشتیم و به توانایی‌های راهبردی آنها آسیب شدیدی زدیم، به اسرائیل حمله نمی‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78207" target="_blank">📅 15:00 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SykwRdiW5wkzPG1c5J_JAUcfBwXDwqj43df2s4SLGwF6Jng-YZ73QBLEZpkgBaliT2V0RyMyGDPO30M9ZmJioiQN1Cx0-fdXIL6nyFVB8RisI2zFLztEkRY4Y58SbiD1mKDxA7DOWWMXnpfDMvkQAeIrK40h5MG1z8wr7utIHELaA_1MkcNNRkEiCAfAczpzU4SaMof9QzzWnVR-ze-nQTna6pkoS1RQ6ii6uwhUg9jSpx8QeevJ1Gs5pSYVaFa07QnI1dsZIt6afc2G87B6H5GtYH0UI595AQNMaNr3ZDEYGqG3WB-QJMneslVpGbXrkONten6Iq2QAnJgQajVNoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت خودروسازی سایپا، روز پنجشنبه ۱۲ شهریور ماه و چند روز پس از آغاز ثبت‌نام طرح فروش فوق‌العاده، با صدور اصلاحیه‌ای رسمی، بهای مصوب چهار محصول عرضه‌شده را به بهانه «افزایش هزینه گواهی اسقاط خودروهای فرسوده و سایر عوارض قانونی شماره‌گذاری» به‌طور چشمگیری بالا برد.
بر اساس جدول جدید منتشرشده، بهای مصرف‌کننده «کوییک اس» و «سهند اس دوگانه‌سوز» هر کدام ۳۳ میلیون تومان گران‌تر شده و به ترتیب به یک میلیارد و ۳۲ میلیون و ۵۱۰ هزار تومان و یک میلیارد و ۱۲۳ میلیون و ۶۸۸ هزار تومان رسیده است.
در بخش خودروهای مونتاژی و وارداتی نیز قیمت «سیتروئن سی۳-ایکس‌آر نسخه وی‌یک» با افزایش ۱۱۵ میلیون و ۵۰۰ هزار تومانی به ۳ میلیارد و ۳۸۹ میلیون و ۳۲۲ هزار تومان و قیمت «چانگان سی‌اس ۵۵ پلاس» با جهش ۱۹۸ میلیون تومانی به ۵ میلیارد و ۸۱۹ میلیون و ۱۲ هزار تومان افزایش یافته است.
این در حالی است که متقاضیان در روزهای گذشته بر مبنای نرخ‌های اولیه اقدام به ثبت درخواست کرده بودند و حالا این محصولات با موعد تحویل ۹۰ تا ۱۲۰ روزه با نرخ‌های جدید تحویل داده خواهند شد.
روز چهارشنبه ۱۱ شهریور، بازار آزاد نیز با موج تازه‌ای از گرانی همراه شد و چند خودروی داخلی دیگر جهش قیمت داشتند.
به‌طوری‌که تارا اتوماتیک با رکوردشکنی و رشد حدود ۱۰۰ میلیون تومانی به محدوده ۳ میلیارد و ۷۵ میلیون تومان رسید. بر اساس گزارش فرارو، در همین روز دنا پلاس اتوماتیک با افزایش ۲۵ میلیونی به ۳ میلیارد و ۱۹۰ میلیون تومان و پژو ۲۰۷ اتوماتیک پانوراما به ۲ میلیارد و ۹۸۰ میلیون تومان رسید و محصولاتی نظیر شاهین اتوماتیک پلاس و سورن پلاس دوگانه‌سوز نیز به‌ترتیب در سطوح قیمتی ۳ میلیارد و ۳۰ میلیون و ۲ میلیارد و ۴۱۰ میلیون تومان معامله شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78206" target="_blank">📅 14:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NucBpBrLmuSzQSdpVaJnabsOI0v5gUSeK_UcIk-hDSqRchjV5tmLf7XPhbSO8yvBSn__EOKwNA1HyBR15nLMrDcw4AWBAZinBBHJy7MOK0K0ZeJahwHm-0MWgsLQGzItjOTIuA1AlSbjQjj9j1CKBIB3Ht4pbW2uIig04gwKVNM8z7vgPJSuhEHPOcKu7nyvho2txt0I8ejR6VsUg9GaEOu0n-RJH_X3UaCWx8tntzyTGEk0cItsD1SFUulGAbXdcdfahWPFKq7RLpPS4KS1QYtMP8i2co6uMndd1th2_vxRuJzRmiGbCmLQoeMdKwXJ7X4930eCH-94Et05QF8KPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین شریعتمداری، مدیرمسئول روزنامه کیهان، پنج‌شنبه ۱۲ شهریور در یادداشتی نوشت که ارتش و سپاه باید از «اهرم» عبور کابل‌های فیبر نوری بین‌المللی در خلیج فارس و تنگه هرمز برای «مقابله با آمریکا و متحدانش» استفاده کنند.
مدیرمسئول روزنامه کیهان نوشت: «در عمق آب‌های خلیج فارس و تنگه هرمز یکی از شاهراه‌های فیبر نوری بین‌المللی جای گرفته است. شاهراهی که بیشترین ارتباطات اینترنت، تماس‌های بین‌المللی، تراکنش‌های بانکی، سرویس‌های ابری (iCloud) و حتی ارتباطات هوش مصنوعی و دیتاسنترها از همین کابل‌ها عبور می‌کنند.»
حسین شریعتمداری، نماینده خامنه‌ای در روزنامه کیهان، تاکید کرد: «سخن با مسئولان کشور و مخصوصا با ارتش و سپاه است؛ خوب نگاه کنید! کابل‌های اینترنت جهانی از زیر آب‌های تنگه هرمز و خلیج همیشه فارس برایمان دست تکان می‌دهند و با هزار زبان می‌گویند چرا نقش ما را در این جنگ فراموش کرده‌اید؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78203" target="_blank">📅 14:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wdh8v6zBPW2KoAyknQZxrB2PyNpNuL30_Rtiaqd5BbPeMRiILfqcAgVQ9eAC49P6khSQPuIaA0T-9yTyTM8PxxZok9I4Cy6QiAJrbnAvOYxgDLhh4JaTZsV7lIHmE9d_SCl0mlX1BZ0mipCqB1lt2AZl4GYMK0N0cL0sazu4M1qplGUKrTQ8cBTDM2tkxRT-iM-qtbxVOa_TMtZi5P1iGwU0cn1efCt6DSY0YgeXupzFaHGJ7j3HYL3UW7zyMsydZzmACrinSCaJ_D0bVQ_7EszAwxjWWP_K-DOH4h2cd3vW6nS1NT4Li2VGeJjOTe4FbXMCyzTXYmYAg4wPBSv6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه افزایش نرخ ارز در ایران، قیمت پوند بریتانیا پنج‌شنبه ۱۲ شهریور در بازار آزاد برای نخستین بار از مرز ۳۰۰ هزار تومان عبور کرد و تا زمان تنظیم این گزارش به ۳۰۰ هزار و ۲۸۰ تومان رسید.
در همین حال، دلار در بازار آزاد با قیمت بیش از ۲۲۲ هزار تومان معامله شد و قیمت یورو نیز از ۲۵۸ هزار تومان عبور کرد.
قیمت سکه امامی نیز از ۲۳۵ میلیون تومان عبور کرد و نیم‌سکه به ۱۲۰ میلیون تومان رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78202" target="_blank">📅 14:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mlGDKndsExL_1SyMvhq6Zl3eVAze8XOzhRGQHJuuw-kJ7hc6pOx5R0DSRExbB6AXRAdx8hgfZH4YjBzklNXIxr6SwXngOTcUI0cpMIWn06kNfYup4CquV-uKUjamNttk4JDGswu14iPYYRro8T2MSd5hTI7iSFMQOQ4f2IZRiky0EBkZJyCh0KrOi7jlYbpzvXMwioPKLXG7IoifPkc7-swS_06vsJxDVerNSUCVv0Yqtg7f2xiqCc6TNhHx-ibSXkc9TxJNAa_aRsCyu5TG9YIDr9VoPI_YRPnBw1XXwnFrV8iAamkoFsiuTZxi4sr6BX8C23GtixNG7VDxfI_xog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوان عالی کشور حکم ۱۲ سال و شش ماه و یک روز حبس، مصادره تمامی اموال و دو سال محرومیت از کافه‌داری برای صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای «ساعدی‌نیا»، را تایید کرده است.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، روز پنج‌شنبه ۱۲ شهریور ۱۴۰۵ اعلام کرد این حکم به‌دلیل حمایت ساعدی‌نیا از اعتراضات دی‌ماه ۱۴۰۴ و تعطیل‌کردن واحدهای صنفی زیر مجموعه این برند صادر شده است.
براساس اعلام قوه قضاییه، صادق ساعدی‌نیا به اتهام «فعالیت رسانه‌ای و تبلیغی علیه امنیت کشور به نفع گروه‌های معاند» به ۱۲ سال و شش ماه و یک روز حبس تعزیری و مصادره تمامی اموال منقول و غیرمنقول خود به نفع دولت محکوم شده است.
دادگاه همچنین او را پس از پایان دوران حبس، به دو سال محرومیت از فعالیت در حرفه کافه‌داری محکوم کرده است.
قوه قضاییه انتشار مطالب اعتراضی در اینستاگرام، حمایت از فراخوان‌ها، تعطیل‌کردن کافه‌ها و فروشگاه‌های مجموعه و تشویق کارکنان به شرکت در اعتراضات را از مصادیق اتهامات او اعلام کرده است.
براساس کیفرخواست، صادق ساعدی‌نیا با سه عنوان اتهامی شامل «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های مخالف جمهوری اسلامی» و «فعالیت تبلیغی علیه نظام» محاکمه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78201" target="_blank">📅 14:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hY5CQxHDl_w_SCUvgj1UuGc6hGGFCcm_epXyD8QZxoZ7sUuust4E1yuE7B2ebOhzJT6_Q6FNwDMZ7cJmWDkmJRntuIUYzkhgZd2sSK6pr_PQrUvMrI9VTGTr4dPszBhGJxDyyn8UgG1DtHrWfQEKqydULICcyGppLCyL8gmKDVRaJJNuMohYPfyd_D3jpSUKKohBgL_RpE8UHTZEZc-AmofyyCCxayeFgu1MgWMSYX5o-Osq1Xq72dNniYyVPJ961pV-SUqgLSdZLWVMgHwFjVUcVmYRfSaRIjRcme_I_eg3wJobHZMx3h-5JnRlG75WRCo3xJZlp6REzqoKe0UUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: هشدار در کویت
ترجمه ماشین:
⚠️
هشدار: خطر قریب‌الوقوع
تهدید امنیتی
از همه خواسته می‌شود در مکان‌های امن باقی بمانند و برای حفظ ایمنی عمومی، از پنجره‌ها و فضاهای روباز و در معرض خطر دوری کنند.
دفاع مدنی – وزارت کشور
آپدیت:
کویت: ایران حمله کرده
متن پست ارتش کویت، ترجمه ماشین:
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران است.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجار شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همه خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78200" target="_blank">📅 05:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آکسیوس:
ویتکاف در بحبوحه تشدید فشارها علیه ایران با مقام قدرتمند اماراتی دیدار کرد
ترجمه ماشین:
استیو ویتکاف، فرستاده کاخ سفید، آخر هفته گذشته با مشاور امنیت ملی امارات متحده عربی دیدار کرد تا درباره گام‌های بعدی در قبال ایران گفت‌وگو کند؛ این را دو منبع مطلع از این دیدار گفته‌اند.
چرا مهم است:
این گفت‌وگوها که کاخ سفید آن‌ها را اعلام نکرده بود و تاکنون نیز گزارشی درباره‌شان منتشر نشده بود، در شرایطی انجام شد که دولت ترامپ در تلاش است تنگه هرمز را بازگشایی کند و هم‌زمان ایران را از نظر اقتصادی تحت فشار شدید قرار دهد. ویتکاف در جزیره ساردینیا در دریای مدیترانه با شیخ طحنون بن زاید آل نهیان (TBZ) دیدار کرد.
▪️
امارات شریک کلیدی عملیات تحت رهبری آمریکا برای بازگشایی تنگه و هدایت نفتکش‌ها در عبور از آن بوده است. این کشور همچنین برای موفقیت کارزار فشار اقتصادی آمریکا علیه ایران نقشی حیاتی دارد.
▪️
طحنون بن زاید یکی از قدرتمندترین چهره‌های امارات است: او برادر محمد بن زاید، رئیس امارات، مشاور امنیت ملی این کشور و معاون حاکم ابوظبی است و بر منافع گسترده سرمایه‌گذاری و فناوری امارات نظارت دارد.
▪️
به گفته منابع، ویتکاف و طحنون بن زاید درباره گام‌های بعدی در بحران ایران تبادل نظر کردند و درباره مسائل دیگری نیز گفت‌وگو داشتند.
▪️
کاخ سفید به درخواست برای اظهارنظر پاسخ نداد.
زمینه خبر:
این دیدار چند روز پس از آن انجام شد که اسکات بسنت، وزیر خزانه‌داری آمریکا، «عملیات طرد اقتصادی» (Operation Economic Outcast) را اعلام کرد؛ تعهدی برای اعمال تحریم‌های سنگین علیه کشورها و نهادهایی که با جمهوری اسلامی تجارت می‌کنند.
▪️
به گفته یک منبع مطلع از این تماس، بسنت پیش از اعلام این طرح با طحنون بن زاید گفت‌وگو کرده بود.
▪️
در همان روزی که ویتکاف با طحنون دیدار کرد، وزارت خزانه‌داری آمریکا برای قطع دسترسی شعب اماراتی «بانک مصر» از نظام مالی آمریکا به‌دلیل معاملات این بانک با ایران اقدام کرد. اقدام پیشنهادی، تراکنش‌های دلاری این بانک را مسدود خواهد کرد.
▪️
بانک مرکزی امارات اعلام کرد «بررسی فوری» تراکنش‌هایی را که شعب این بانک مصری با ایران داشته‌اند، انجام خواهد داد.
نگاهی دقیق‌تر:
چند روز پیش از اعلام تحریم‌های دولت ترامپ، امارات تصمیم گرفت تمام تجارت، مبادلات بازرگانی و تراکنش‌های مالی با ایران را متوقف کند.
▪️
این تصمیم اقدامی چشمگیر بود، زیرا امارات — و به‌ویژه دبی — یکی از مراکز اصلی تجارت و صادرات مجدد برای ایران محسوب می‌شد. حجم تجارت دو کشور در سال ۲۰۲۴ به ۲۸ میلیارد دلار رسیده بود.
▪️
یک منبع دیگر مطلع از موضوع گفت مقام‌های اماراتی به دولت ترامپ گفته‌اند برای آنکه هر کارزار فشار اقتصادی علیه ایران مؤثر باشد، باید همه کشورهای کلیدی که با جمهوری اسلامی تجارت می‌کنند در آن گنجانده شوند.
پشت پرده:
به گفته دو منبع مطلع، تحریم‌های ثانویه قریب‌الوقوع دولت ترامپ علیه ایران یکی از عوامل تصمیم امارات بود، اما دلیل اصلی آن نبود.
▪️
به گفته منابع، ۱۱ اوت یک هیئت ایرانی برای گفت‌وگوهای دیپلماتیک کم‌سروصدا با مقام‌های اماراتی به ابوظبی سفر کرد.
▪️
منابع گفتند ایرانی‌ها در این گفت‌وگوها اعلام کردند که خواهان کاهش تنش و بهبود روابط هستند — پس از آنکه ایران در جریان جنگ هزاران موشک و پهپاد به سوی امارات شلیک کرده بود.
▪️
به گفته منابع، ایرانی‌ها حتی از امارات برای تأمین غذا و دارو درخواست کمک کردند و از اماراتی‌ها خواستند با تحریم‌های آمریکا همکاری نکنند؛ درخواستی که بلافاصله رد شد.
▪️
اما در چند روز بعد، سپاه پاسداران حملات خود به نفتکش‌های شرکت ملی نفت امارات را که تلاش می‌کردند از تنگه هرمز عبور کنند، تشدید کرد.
▪️
منابع گفتند اماراتی‌ها خشمگین شدند و تصمیم گرفتند تمام روابط تجاری با ایران را تعلیق کنند.
موضوعی که باید زیر نظر داشت:
مقام‌های آمریکایی گفتند مارکو روبیو، وزیر خارجه آمریکا، اوایل این هفته به همه سفارتخانه‌های آمریکا در سراسر جهان دستور داد درباره «عملیات طرد اقتصادی» یک پیام رسمی دیپلماتیک به عالی‌ترین سطوح دولت‌های میزبان خود ارائه کنند.
▪️
به سفارتخانه‌های آمریکا دستور داده شد از کشورها بخواهند «فوراً و به‌صورت نظام‌مند» تمام تجارت با ایران را قطع و فعالیت‌های تجاری غیرقانونی ایران را شناسایی کنند.
▪️
مقام‌های آمریکایی گفتند در این پیام دیپلماتیک تأکید شده است که کشورها، شرکت‌ها و افرادی که به تجارت با ایران ادامه دهند، در معرض تحریم و قطع دسترسی به نظام دلاری قرار خواهند گرفت.
▪️
یکی از مقام‌ها گفت پیام ویژه‌ای برای نمایندگی‌های دیپلماتیک آمریکا در ابوظبی، مسقط، هنگ‌کنگ، دوحه، لندن، برلین و چند پایتخت آسیای مرکزی ارسال شده است. در این پیام به آن‌ها دستور داده شده از دولت‌های میزبان خود بخواهند تمام شعب بانک‌های ملی و صادرات ایران را که با سپاه پاسداران مرتبط هستند، تعطیل کنند.
گام بعدی:
یک مقام آمریکایی گفت دولت ترامپ در حال تشکیل یک کارگروه بین‌سازمانی برای هماهنگی اجرای کارزار فشار اقتصادی علیه ایران و نظارت بر اجرای آن است.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78199" target="_blank">📅 03:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NvTiTKqRshYyH_pgyQbsr9MSu5eGkRCFmqHoZyyTet8ofD1oYVpkPYm1yqHC-_Wddxpz17_qHRqfJgkvgHdESvPcQaIrdNmutt2q4s-GRV9v-IYSbEm1JZd4T7RIUCmbDQm8G2M67fQoQOAsaT4_q5Uaabo408r7axj6Wx-RgF-geEfVFXqnyLmw0VgxwCLLsxW6A5RkNN8ZzbNTVQ6kRX7wv7CaTH9XDrvfWTY8HAhHMh84525_Gt0-_3ijfoEhiAAEnsk5d8hBmhXO5ZO5ACnvlhbgVzGpCo5QUmMwxoVrHCBHgVIAyS87wLrsBZvAlPCMO32fqwfo5S4r5lecjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=SjVB1FqySD5Bit365YlpmRW4F8O_JYxtIi5XfR15X-CH5tWGvqp9PFnLO5c1axaAKbE4BvJVlLgi8v5dm50EZwIvZIUTx5ibRbPh7X71X-2F_eNoSVtFIQE2KVv-CcRVIlkrUvB_o1vfWWz09xpC7lcD6wQm0Sl6_-HBMTLFLXxLnkWR9LKKEjrCIZCVIS1wGlfx34xl2dQfFcVLAntLv4VWmCRfyvCEuo-fIvIR14dge8TzYzZseA9hM-kw-rrDmzhcpxs3FHu3FRYFgNa2tgViEBMFAS_vEqCfhzaZL99Lhmsas5o4Jq1HhLqX0Ixz79k2C3coDj4NeR_59NlFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e08d6ca26.mp4?token=SjVB1FqySD5Bit365YlpmRW4F8O_JYxtIi5XfR15X-CH5tWGvqp9PFnLO5c1axaAKbE4BvJVlLgi8v5dm50EZwIvZIUTx5ibRbPh7X71X-2F_eNoSVtFIQE2KVv-CcRVIlkrUvB_o1vfWWz09xpC7lcD6wQm0Sl6_-HBMTLFLXxLnkWR9LKKEjrCIZCVIS1wGlfx34xl2dQfFcVLAntLv4VWmCRfyvCEuo-fIvIR14dge8TzYzZseA9hM-kw-rrDmzhcpxs3FHu3FRYFgNa2tgViEBMFAS_vEqCfhzaZL99Lhmsas5o4Jq1HhLqX0Ixz79k2C3coDj4NeR_59NlFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان حملات شب گذشته آمریکا به روستای کوهستک در سیریک، علاوه بر یک برج مخابراتی، دستکم دو خانه مسکونی هم هدف حمله قرار گرفتند.
کوهستک دیشب پنج بار هدف قرار گرفت که به نظر می‌رسد چهار موشک به یک محل اصابت کرده است.
بر اساس تصاویر دوربین مدار بسته، سه موشک اول به خانه محل عروسی اصابت می‌کند.
به نظر می‌رسد موشک چهارم به دکل مخابراتی همراه اول و موشک پنجم دوباره به محل عروسی اصابت می‌کند.
دکل مخابراتی با خانه محل عروسی حدود ۱۱۲ متر فاصله داشته است و چند خانه اطراف هم آسیب دیده است.
@
VahidHeadline
به گزارش خبرگزاری مهر، خانه مسکونی محل برگزاری عروسی ۱۳۶ متر با دکل مخابراتی که هدف حمله موشک‌های آمریکایی بود، فاصله داشت.
مقام‌های امداد و نجات جمهوری اسلامی و رسانه‌های دولتی ایران اعلام کردند بر اثر این حمله ۴ نفر کشته و ۶۸ نفر دیگر زخمی شدند.
کوچکترین قربانی این حمله، امیرعلی کریمی چهار ساله بوده است.
@
VahidOOnLine
آپدیت:
بی‌بی‌سی چند ساعت بعد خبرش رو ویرایش کرد و اسم سلاحی که نوشته بود رو عوض کرد ولی همچنان نوشتند موشک.
گویا پیش‌تر نیویورک‌تایمز هم درباره نوع پرتابه ادعای مشابهی مطرح کرده بود ولی بعدا پس گرفت.
با جست‌وجو دیدم یکی اینجا خیلی مفصل بررسی کرده:
Mk20002000B
آپدیت:
حال‌وش روز چهارشنبه ۱۱ شهریور ۱۴۰۵، به نقل از شماری از شاهدان محلی خبر داد که پیش از انفجار، صدای دو پهپاد در منطقه شنیده شده است.
این رسانه، علی ملاحی، صاحب خانه و پدر عروس، را یکی از شاهدان معرفی کرده است. او گفته پیش از وقوع انفجار صدای دو پهپاد را شنیده و پس از آن، ساختمان هدف قرار گرفته است.
شماری دیگر از ساکنان کوهستک نیز از مشاهده یک پهپاد یا شنیدن صدای آن خبر داده‌اند.
منابع محلی همچنین می‌گویند خسارت‌های واردشده به خانه تنها ناشی از ترکش انفجار در یک محل دیگر نبوده و یک یا چند پرتابه مستقیما به ساختمان اصابت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78197" target="_blank">📅 01:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=KEThGf7Mnjc5uz_St8hdk-nD3TnmKrOMevie5UljK23-YfQVk53C7Intnysv5_k53zihcK02kUCGp7TNMnGSRomZhg13CVIu0kI-oFA9-8TdJBupNwMtVqP7vDlUr3joUoQ_b6uQA68-OaLn0zGP9Mh4MDPYXhr9dno9OG9EWm7qKNEJxOMUsEoTPQzl1q0ExEfcD1MaIH6TKxNz6z-Rk0ua72Tm4E8pXfr2pI424SNZJrQpIoInowVmB10fUBraJ9Mzf9jMQ454ExUaCf3Q5C9O5l8EFcsjdCwu4W0KD5RQZNPPetER-_mmum8pujQGLhASrZ97EZQucZzHrSXae1Tq0hmvC_uID9HvGhZyIU6_oCVmH1PgVMSwc1RX3Cr5sGheKeyFlVAj84xBLj-rvl8FEUxtZBfsMzCSRbp9oXfLXFhlc2McVLDNy3g9mZqU1o3Lhjq4FR1c0U8aJ0YPYbCTrjsosAdlHIIkRi9njdyvAfGqaznhXDUWeeMlTN5rIy1ow_K8YKLThiyjhGTPEDefaDmQJvaGiSqcNeZsmgdD-AysSmpMajB-zltn6a_IHoivHdZ_Z0TqJbjitoFghk3ohSg2tfzBq1xzLEHs2AC99-HuWW-DrPHDXdGvybqZxk1xj1DLLChNXa6a6HhsvpDBlZz-_5hdFWBWo0pbnX8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2c4ae3e5e5.mp4?token=KEThGf7Mnjc5uz_St8hdk-nD3TnmKrOMevie5UljK23-YfQVk53C7Intnysv5_k53zihcK02kUCGp7TNMnGSRomZhg13CVIu0kI-oFA9-8TdJBupNwMtVqP7vDlUr3joUoQ_b6uQA68-OaLn0zGP9Mh4MDPYXhr9dno9OG9EWm7qKNEJxOMUsEoTPQzl1q0ExEfcD1MaIH6TKxNz6z-Rk0ua72Tm4E8pXfr2pI424SNZJrQpIoInowVmB10fUBraJ9Mzf9jMQ454ExUaCf3Q5C9O5l8EFcsjdCwu4W0KD5RQZNPPetER-_mmum8pujQGLhASrZ97EZQucZzHrSXae1Tq0hmvC_uID9HvGhZyIU6_oCVmH1PgVMSwc1RX3Cr5sGheKeyFlVAj84xBLj-rvl8FEUxtZBfsMzCSRbp9oXfLXFhlc2McVLDNy3g9mZqU1o3Lhjq4FR1c0U8aJ0YPYbCTrjsosAdlHIIkRi9njdyvAfGqaznhXDUWeeMlTN5rIy1ow_K8YKLThiyjhGTPEDefaDmQJvaGiSqcNeZsmgdD-AysSmpMajB-zltn6a_IHoivHdZ_Z0TqJbjitoFghk3ohSg2tfzBq1xzLEHs2AC99-HuWW-DrPHDXdGvybqZxk1xj1DLLChNXa6a6HhsvpDBlZz-_5hdFWBWo0pbnX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ
بخش‌های مرتبط با ایران به تشخیص و ترجمه ماشین
و متن زیرنویس تا اونجایی که جا می‌شد در یک پست:
🔺
خبرنگار:
ترامپ، شما امروز در تروث سوشال نوشتید: «مردم ایران چه زمانی قیام می‌کنند و می‌جنگند؟» خب، اگر این چیزی است که می‌خواهید، آیا سیا را می‌فرستید تا ایرانی‌ها را مسلح کند؟
🔻
ترامپ:
خب، نمی‌خواهم این را به تو بگویم، پیتر. خیلی دوست دارم به تو بگویم، اما گفتنش مناسب نیست. اما من... یعنی، من وضعیت دشوارشان را درک می‌کنم. همین حالا دارند به آن‌ها شلیک می‌کنند.
می‌دانید، این آقایان اینجا در ناز و نعمت نشسته‌اند و چیزهایی را می‌بینند، اما آنجا اوضاع چندان راحت و مرفه نیست. تا سه ماه پیش، ۵۲ هزار معترض کشته شده بودند. می‌توانید تصورش کنید؟ و حالا می‌شنوم که این تعداد احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر هم بیشتر شده. نزدیک به ۶۵ هزار معترض کشته شده‌اند.
پس وقتی آن سؤال را مطرح می‌کنم، به‌نوعی جوابش را هم می‌دانم. تنها پاسخ این است که به آن‌ها شلیک می‌شود. رژیم هر روز ضعیف‌تر و ضعیف‌تر می‌شود و در مقطعی دیگر نمی‌توانند به این راحتی شلیک کنند، چون فکر می‌کنم مردم دیگر این را تحمل نخواهند کرد.
اما من آن سؤال را مطرح کردم چون، می‌دانید، وقتش رسیده است. اما بیشترِ... بیشتر مردم نمی‌توانند مردم خودشان را این‌طور بکشند. بیشتر مردم سعی می‌کنند منطقی برخورد کنند، گفت‌وگو می‌کنند و بعد ممکن است حکومت سرنگون شود. در ایران، مردم را می‌کشند. وقتی برای اعتراض بیرون می‌آیند، آن‌ها را می‌کشند. درست بین دو چشمشان شلیک می‌کنند.
آن‌ها دو روش دارند: مسلسل و تک‌تیرانداز، و از هر دو استفاده می‌کنند؛ گاهی مسلسل‌ها و گاهی تک‌تیراندازها. تک‌تیراندازها را بیشتر دوست دارند، چون کافی است جمعیتی ۲۰۰ هزار نفری باشد و یک نفر همین‌جا با گلوله‌ای بین دو چشمش به زمین بیفتد، و سه تک‌تیرانداز این کار را انجام دهند؛ و تماشای آن وحشتناک است. واقعاً وحشتناک است.
برای همین است که این اتفاق نمی‌افتد. و چه کسی می‌تواند سرزنششان کند؟ چه کسی می‌تواند سرزنششان کند؟ اما رژیم هر روز ضعیف‌تر می‌شود.
—————-
ما  داریم تنگه هرمز را کنترل می‌کنیم. ما داریم هر روز کشتی‌های زیادی را خارج می‌کنیم که میلیون‌ها بشکه نفت حمل می‌کنند. در بیشتر موارد این کار را بدون مشکل انجام می‌دهیم. هر از گاهی آن‌ها یک پهپاد می‌فرستند و ما آن را ساقط می‌کنیم.
اما ما کنترل داریم؛ کنترل بسیار قدرتمندی. آن‌ها تلاش می‌کردند سامانه‌های راداری و یک سامانه موشکی و سامانه‌ای برای ریختن مین را بازسازی کنند. می‌دانید، ما همه مین‌ها را در تنگه هرمز از بین بردیم. آن‌ها تلاش می‌کردند موشکی بسازند که مین می‌ریزد. چه کسی چنین کاری می‌کند؟ تا حالا موشکی ساخته‌اید که مین بریزد؟ من هرگز چنین چیزی نشنیده بودم، اما این کاری بود که آن‌ها می‌کردند.
داشتند آن را می‌ساختند. تقریباً تمام شده بود، پس ما نابودش کردیم. دیدیم که داشتند آن را می‌ساختند. ما هر کاری را که می‌کنند می‌بینیم. نمی‌توانند تکان بخورند. حتی نمی‌توانند به دستشویی بروند بدون اینکه ما ببینیم. پس آن را دیدیم. نابودش کردیم.
...
بنابراین دیشب محکم به آن‌ها حمله کردیم؛ خیلی محکم. آن‌ها یک ضربه خیلی کوچک زدند، اما ما دیشب خیلی محکم به آن‌ها حمله کردیم. همه تجهیزات جدیدی را که تلاش کرده بودند در امتداد تنگه هرمز بسازند نابود کردیم؛ بعضی دفاعی و بعضی تهاجمی.
آن‌ها سعی می‌کردند کشتی‌ها را ببینند، چون نمی‌توانند کشتی‌ها را ببینند. می‌دانید، ما تعداد زیادی از کشتی‌ها را از بین برده‌ایم. آن‌ها نمی‌توانند ببینند، چون رادار ندارند، چون ما آن را منفجر کردیم، و دیشب چیزهای بسیار بیشتری از فقط رادارشان را منفجر کردیم.
دیشب حمله بسیار سنگینی بود و آماده‌ایم هر زمان که بخواهیم، حمله دیگری انجام دهیم.
....
بنزین با آن قیمت فروخته می‌شد؛ چون نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
...
اما مسئله خیلی ساده است. ایران نمی‌تواند سلاح هسته‌ای داشته باشد. به‌محض اینکه تمام شود، که فکر نمی‌کنم خیلی بیشتر طول بکشد، نمی‌دانم چقدر دیگر می‌توانند تحمل کنند، اما می‌دانید، هرچه باشد، اهمیتی ندارد.
و انتخابات روی من تأثیری ندارد. اول اینکه، من نامزد نیستم. اما حزب من نامزد دارد و من قرار است به حزبم کمک کنم. اما فکر می‌کنم حزب من به این واقعیت احترام می‌گذارد که ما اجازه نمی‌دهیم ایران سلاح هسته‌ای داشته باشد.
————-
🔺
خبرنگار:
آقای رئیس‌جمهور، چقدر درباره تغییر نام تنگه هرمز به «تنگه ترامپ» جدی هستید؟ و اگر جدی هستید، چطور این کار را انجام می‌دهید؟ چطور این کار را می‌کنید، آقای رئیس‌جمهور؟
🔻
ترامپ:
فقط همین‌طوری مطرح شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78196" target="_blank">📅 22:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=llSyiLST5LjN3LTytLGqdIdS4L4VLL_XFqY9j6Y6m0PpJLZQsp15XAllicqn9s0wdoIvYuQ3Wsw7c6KTIWveY3-2YNy74UjkA9o10KlRbSBd0XwkR-cx8IDMdlhNVbiJ2xaTAJRh5Mb_tvB44OCG6juZs5rNegurY5jIH-e4tjbZsIEEtCScFU4ay5DytXeuKM5F7YYUlAPaSFKOg1w29TWzaGlKF674tLHiSMycMcJipZad97PC3sP0PghFSGEkkSI3hZ0ibtxRCiY7VVxWYvpVgMTxY9TPjtEokZXiymDrK8__CoV1hZGzM2vKzNp7Bc7ye-lSPl5j_q_wMdR2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/583f7fe047.mp4?token=llSyiLST5LjN3LTytLGqdIdS4L4VLL_XFqY9j6Y6m0PpJLZQsp15XAllicqn9s0wdoIvYuQ3Wsw7c6KTIWveY3-2YNy74UjkA9o10KlRbSBd0XwkR-cx8IDMdlhNVbiJ2xaTAJRh5Mb_tvB44OCG6juZs5rNegurY5jIH-e4tjbZsIEEtCScFU4ay5DytXeuKM5F7YYUlAPaSFKOg1w29TWzaGlKF674tLHiSMycMcJipZad97PC3sP0PghFSGEkkSI3hZ0ibtxRCiY7VVxWYvpVgMTxY9TPjtEokZXiymDrK8__CoV1hZGzM2vKzNp7Bc7ye-lSPl5j_q_wMdR2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کریس رایت، وزیر انرژی آمریکا، و دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، روز چهارشنبه توافقی نفتی را در کاراکاس امضا کردند که بر اساس آن ایالات متحده کنترل اکثریتی بر ۶۵ میلیارد بشکه از ذخایر نفت ونزوئلا به دست می‌آورد.
این میزان حدود یک‌پنجم ذخایر عظیم نفتی ونزوئلا را شامل می‌شود. دونالد ترامپ، رئیس‌جمهور آمریکا، این توافق را «بزرگ‌ترین معامله نفتی در تاریخ جهان» توصیف کرده است.
بر اساس این توافق، آمریکا به ۱۷ میدان نفتی ونزوئلا دسترسی ترجیحی خواهد داشت؛ تأسیساتی که برخی از آنها پیشتر در اختیار شرکت‌های روسی و چینی بوده‌اند.
همزمان، شرکت شورون نیز از توافق جداگانه‌ای به ارزش هفت میلیارد دلار برای توسعه دو میدان نفتی دیگر در کمربند اورینوکو خبر داده است. شورون می‌گوید این سرمایه‌گذاری می‌تواند تولیدش در ونزوئلا را طی پنج سال بیش از دو برابر کند.
وزیر انرژی آمریکا پیش‌بینی کرده است تولید نفت ونزوئلا تا پایان دهه جاری به بیش از دو میلیون بشکه در روز برسد؛ حدود دو برابر سطح تولید در ژانویه، زمانی که نیروهای آمریکایی نیکلاس مادورو را سرنگون کردند و دلسی رودریگز قدرت را در دست گرفت.
این توافق با انتقادهایی نیز روبه‌رو شده و منتقدان دولت رودریگز را به واگذاری حاکمیت ونزوئلا بر منابع نفتی خود متهم کرده‌اند. دولت ونزوئلا در مقابل می‌گوید این توافق به این کشور برای بهره‌برداری از ظرفیت‌های انرژی و جذب سرمایه‌گذاری کمک خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78195" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nL1WyFgyix8kKs6KsmDP2KqxTgQd3Qg7aJOKUZ6Rux7zpXZxFsvY4kDL5xtvfwJNNbx7L0iZXLDQ1yoh9EYeNTzts3hyOi8GNWq-BJpqkiX9zeypAHrpJroQnMNcIydWNAA9_cBhMS297x77aHtp0vLVbUlO3lC_zq_Vf9wY_U4-YgWmPVVqhgF0c1J70owssndAymqRM5uRQGJwgE5UBQbjYY-pttiVvWWZw0q6Xz_AZoROOiZArEU4FDR1MX08APTvVE4U5QCgkCe_VHbVQWwXSsElQxv9NEmG3vF6QnI71DNHRc4uwm8pc2GYpKnzhAH6n_OupevFFIOunaEhbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=taX4ofoEw55HmcjdJv59K2eFO04NyRBj1b0mBPoCLwlqEXFfTvWrn7OpL2rt-Ei6CFLFV_t3hSYPZkaRMHJc0H2I9KViY8WFqLUxA650xS7Jj0C6DnbZoXOtUe9NYv4W2J7WS_49Zp42-0cbnhlsMgwVClv1CdJbzWc8ahVdjGEI_OTa4ozDuzepBFXbQQwkT2cmug_Gwezc5DQ-ACsCHt1aZZg6xJgr_-i8-jqU8cc9wQpDJp1OoQKMDQmQKUniSJtM2RyxNEeVQx1eO45pO_LeneP7qvVKHjwjWkkpGFCSNgfTO1jDkadyPE465FnhAr-zbMmsAj5m4hoUXx2hgw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b44a8875b1.mp4?token=taX4ofoEw55HmcjdJv59K2eFO04NyRBj1b0mBPoCLwlqEXFfTvWrn7OpL2rt-Ei6CFLFV_t3hSYPZkaRMHJc0H2I9KViY8WFqLUxA650xS7Jj0C6DnbZoXOtUe9NYv4W2J7WS_49Zp42-0cbnhlsMgwVClv1CdJbzWc8ahVdjGEI_OTa4ozDuzepBFXbQQwkT2cmug_Gwezc5DQ-ACsCHt1aZZg6xJgr_-i8-jqU8cc9wQpDJp1OoQKMDQmQKUniSJtM2RyxNEeVQx1eO45pO_LeneP7qvVKHjwjWkkpGFCSNgfTO1jDkadyPE465FnhAr-zbMmsAj5m4hoUXx2hgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با شبکه نیوزمکس گفت که ایالات متحده لزوما به دنبال فروپاشی جمهوری اسلامی ایران نیست، هرچند تحولات درونی و قیام مردم امکان‌پذیر است.
او همچنین به مخاطرات شخصی پیش‌روی رهبران و فرماندهان نظامی ایران با افزایش فشارها اشاره کرد.
بسنت ادعاهای ایران درباره کنترل بر تنگه هرمز را رد کرد و گفت با عبور حدود ۱۷ میلیون بشکه نفت در روز گذشته، کنترل ایران بر این تنگه بی‌معناست. او همچنین گزارش‌ها درباره وجود مین یا برخورد دو کشتی با مین در تنگه هرمز را تکذیب کرد و رسانه‌ها را به بازنشر سریع ادعاهای نادرست ایران متهم ساخت.
وزیر خزانه‌داری آمریکا، با اشاره به تداوم خرید نفت ایران توسط چین تاکید کرد که تنها حدود ۳۰ میلیون بشکه نفت ایران روی آب باقی مانده و این ذخایر نیز به‌زودی به پایان خواهد رسید.
بسنت روز گذشته نیز در جریان سخنرانی در مجمع اقتصادی جی۲۰، تاکید کرده بود که فشارهای اقتصادی یا به ایجاد شکاف و دودستگی در سپاه پاسداران و احتمالا مقابله مردم با آن‌ها منجر می‌شود یا مقام‌های تهران تصمیم می‌گیرند که به میز مذاکره بازگردند.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفت‌وگو با شبکه آی‌۲۴ درباره حکومت ایران گفت: «نیروهای ما می‌توانند هر لحظه در آنجا باشند. ما این حکومت را شکست خواهیم داد.»
نتانیاهو درباره اینکه آیا منظور او از شکست دادن، سقوط کردن حکومت است، گفت: «بله، سقوط خواهد کرد و ما آن را سرنگون می‌کنیم.»
نتانیاهو در پاسخ به این سوال که آیا رومان گوفمن، رییس موساد، برای سرنگونی جمهوری اسلامی فعالیت می‌کند، گفت: «همه دستگاه‌های ما تحت هدایت من برای سرنگونی این حکومت و شکست آن فعالیت می‌کنند.»
نتانیاهو گفت: «در نهایت با سر اختاپوس، برخورد خواهیم کرد، بازوها را قطع خواهیم کرد و محور شر ایران را هدف قرار خواهیم داد. این کار را با قدرت بسیار انجام دادیم؛ خلبانان ما آنجا بودند و هر لحظه می‌توانند آن جا باشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78193" target="_blank">📅 21:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ueEaSNNsHxEicFwaepEXlYwwHLGr0Q2CgYTqTnHHzUVN1_YPm9QwNNkzy6GskuCn5G9uEERvUl9Gz8njYJPJ961hVmwq-cwH4Katw3GTj1EuYL7FoVtWDJnzZC15D_m-6_H8ZUVZq9MsDWCO-UJZ0AOog9GoNoATMqJLbqf7qDNW3p79c2InT_88yZjZmfVBV_yP6KJAfm-F2xDG0lcQP4WSPo0PtENyUqZq_Bt5PQaAeCYgUJXGt3BMK6mJ_7OSyyb3An_mXv-aF5z_0kJDWUi2TkYOmtaX03ZNd8hgKDymTVkvp5gHFl9IKLnQsgKIt-v1P9uMecGH-YM4T9lH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی جمهوری اسلامی، با هشدار به ایالات متحده گفت تهران در جنگ جاری از «راهبردی جدید» استفاده خواهد کرد.
رضایی، چهارشنبه ۱۱ شهریور ۱۴۰۵، در پستی در ایکس نوشت که تلاش‌های آمریکا برای خروج از شرایط کنونی نتیجه‌ای نخواهد داشت و افزود: «به‌زودی خواهید دید که راهبرد جدید ایران در میدان نبرد، دیپلماسی و مقابله با محاصره اقتصادی، پایه‌های شما را درهم خواهد شکست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/78192" target="_blank">📅 19:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bsNq0X_qDcPohYg6yvT0h2FbR3QsfU7gusEUPNcaIu9iBtx6zeLD00Q3XXERq3U9pA7uDQFg1lWnlKcTU_9J_CxTYPcChsbsMBAPKsjy-U0tN73Y0D7wiq6fZut5C-eH_Xdvov68DgfCmfAkFbKDvQmXRe4qIQuXJwgvTIu5VyiWst-5y1F-jPtybpI0J7UXaPISa6JHFVu_nPRce8EpCN1ozp90HaaGSSQeLQ8NfW-J_O1y8GIrZ2xIYp7ouE9Q7FYs1-hvRaK0VAIZ_-vhrbYksf1JXNX2E1CYE_IiAEmijJAPAlI4jX5HuSWQEoKfQBOMWRN7Q51BWfxa4PA30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
حالا که آن را تحت کنترل ایالات متحده آمریکا درآورده‌ایم، آیا باید نام «تنگه هرمز» را به «تنگه ترامپ» تغییر دهیم؟؟؟ درست مثل خود آمریکا، این تنگه هم «داغ‌تر» از هر زمان دیگری خواهد بود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
Now that we have it under U.S.A. control, should we change the name Hormuz Strait to TRUMP STRAIT??? Like America itself, it would be “hotter” than ever before! Thank you for your attention to this matter. President DONALD J. TRUMP
realDonaldTrump
در خبری دیگر:
ترامپ در گفت‌وگو با پادکست «دن پاتریک»، درباره حملات سه‌شنبه شب آمریکا در اطراف تنگه هرمز، گفت: «ما اکنون کنترل تنگه هرمز را در اختیار داریم. ما آن را کنترل می‌کنیم. دیشب ۲۸ کشتی را از بین بردیم. ما آن را کنترل می‌کنیم، آنها چیزی دریافت نمی‌کنند و ما کشتی‌ها را از بین بردیم.»
ترامپ همچنین درباره حکومت ایران گفت که جمهوری اسلامی دو هفته با داشتن یک سلاح هسته‌ای فاصله داشت. او افزود: «اگر آنها سلاح هسته‌ای داشتند، اسرائیل از بین می‌رفت، خاورمیانه از بین می‌رفت و آنها به شهرهای ایالات متحده حمله می‌کردند. چون آنها دیوانه هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/78191" target="_blank">📅 19:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oX78YgTFIX9ksQgzLngqjsX6N-hYv0rq6ZoppfJ1SElI71pHHYkT_qfu-virUi10zea8XnMEAgiSGuQpJMLRZtaAIbDHoMHrW3sHjVY20vMi1ZZuijDKXaPfDj2ojRsB2eU_1YnB3BT1sJKuc3KsAxwHo6gkDGNxDDranvl0T8TVQfpCsMBCKF8B7lnapt87BzDZx6kmXpq51i-KLVV5rs77NUfg-cmIf85kbIAc8kpApH4FRSE6rdR01m3HD0A4w2TDab9QV23HK79331hXH1GAK3sSynzgHowfIx464rmloLPL7FBLttgBI3Ar2UCGcGbBYxx1fkQmiXsFvE7Pbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس مجلس شورای اسلامی گفت: آمریکایی‌ها باید به تعهدات خود عمل کنند تا ما اقدام به بازگشایی تنگه هرمز کنیم.
محمدباقر قالیباف، در دیدار با مسئول ارتباطات اسلامی حماس گفت جمهوری اسلامی مذاکره را رد نمی‌کند، اما آن را «ابزاری برای مبارزه» می‌داند.
او گفت کنار گذاشتن مبارزه با آمریکا و اسرائیل به معنای شکست است.
او افزود جمهوری اسلامی در جریان مذاکرات، پایان جنگ علیه ایران و متحدانش در «جبهه مقاومت» را در ماده نخست تفاهم‌نامه مطرح کرد، در حالی که به گفته او، طرف مقابل در متن اولیه ۱۵ ماده‌ای خواستار توقف کامل فعالیت‌های موشکی، هسته‌ای و فعالیت‌های «جبهه مقاومت» شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78190" target="_blank">📅 19:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KI2bHJHGgkMiCY3yuaCBUTNw4sH2RB0no7SVa7_gdRLu2DX-Q612CTVr1PQ1wu1cvGCZAR1g60PoqCHeema-ifVYlFxseSPJN1Pcw7LarLJlJip2gFDoFApiBPV_VRtIubn1-orFicVlRjufZLjc_-QCLURg9crqhvP8x9drYaB-d8X77JLt9SNDr5NJj6qKuSxMzysYyfkXU2_WPEZju6kPjInWLffRHAJxNB3RY0MQ4BMi1Nrrr3afUIeNNgn-HBIjPPAAuHuuYwhcY1vwrx9m34pMXOgjpoFdxIzfKWtiZCL7ywLLgsxdVErGeLSP-xL5QWiorw3CA1iflenbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس آمارهای اعلام شده از سوی شرکت ملی پخش فرآورده‌های نفتی ایران، میانگین مصرف روزانۀ بنزین در نخستین هفتۀ شهریورماه از مرز ۱۴۸ میلیون لیتر گذشته است.
بر اساس این آمارها، بیشترین میزان تقاضای روزانه در ۸ روز نخست آخرین‌ماه تابستان، بیش از ۱۵۴ میلیون لیتر بوده و در این بازه در مجموع بیش از یک میلیارد و ۲۰۰ میلیون لیتر بنزین عرضه شده است.
کاهش شدید ظرفیت تولید در ماه‌های اخیر در اثر حملات آمریکا به تأسیسات نفتی ایران از یک‌سو و مشکلات دولت برای وارد کردن بنزین از سایر کشورها از سوی دیگر، باعث افزایش قیمت بنزین و حتی مطرح شدن احتمال بالاتر رفتن قیمت این فراورده و افزایش شدید تقاضا برای آن شده است.
مسعود پزشکیان رئیس‌جمهور و شماری دیگر از مقام‌ها تأکید کرده‌اند که دولت توان چندانی برای وارد کردن بنزین و بخصوص عرضۀ آن با قیمت‌های قبلی ندارد.
دولت ایران اما در عین حال ادعا می‌کند که تشکیل صف در برخی جایگاه‌های عرضۀ بنزین، ناشی از هیجان و بار روانی بوده و مشکلی در تأمین بنزین مورد نیاز کشور وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/78189" target="_blank">📅 17:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78188">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l016Vk-wwEJ1O65ljWUQZW5bZYTgLiuL0h6NhJJA4wAi6U-0ccUs4KHC55Y39BPvkX25pPhuXW4zXu4g8ZfH4MOL1-f7yZevYNn9dURtxfIn8Gru1FQhK6utAfBAQ2iVkeVuQgfAvL32q9KsKcdl2UylceVVC-ZbRn5pAfrHBYoCqKyNBdBB8UsKv_KM4uWGz5D2KJUdU6BJQrv_zCY4pK0BLo6prIcz7wrTrn8NGoe-r6NlmVXro2xnzEYCkMeho3LPbVNTufpkoqZ9C1zp_no5swQBqPXYzN2nVASZCdJ9BCtxMTTmk0UWldQKug04ik5QyyMFUWLKcez68OjMSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارزهای خارجی در ایران بامداد چهارشنبه ۱۱ شهریور و ساعاتی پس از دور جدید حملات آمریکا، رکورد تازه‌ای ثبت کرد و قیمت یورو، پول واحد اروپایی، برای نخستین بار از مرز ۲۵۵ هزار تومان گذشت.
وب‌سایت‌های اعلام نرخ ارز قیمت دلار از جمله «نوسان»، قیمت دلار آمریکا را حدود ۲۲۰ هزار تومان گزارش کردند. قیمت درهم امارات هم به بیش از ۶۰ هزار تومان رسیده است.
افزایش قیمت نرخ ارزهای خارجی در بازار آزاد ایران از زمان اعلام امارات در قطع روابط مالی با ایران و آغاز برنامهٔ فشار اقتصادی آمریکا موسوم به «عملیات طرد اقتصادی» شدت گرفته است.
در دو هفته اخیر پول ملی ایران در مقابل ارزهای عمده خارجی بیش از ۱۰ درصد دیگر از ارزش خود را از دست داده است.
روز چهارشنبه قیمت سکه طلای موسوم به «امامی» هم با وجود کاهش جهانی قیمت طلا، ۲۲۴ میلیون تومان گزارش شد.
عبدالناصر همتی، رئیس‌کل بانک مرکزی، روز ۱۰ شهریور ادعای کمبود منابع ارزی و احتمال فروپاشی اقتصاد ایران را رد کرد و گفت بانک مرکزی آماده است برای مهار بازار تا دو میلیارد دلار ارز عرضه کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78188" target="_blank">📅 16:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XoUf2NYgR9cWPL3hVJ-a3er1cMEKXlO1hbWxgJmdbCyYKL4MwG8gneD1d24-XvZ0JSuKdpdojh9u0Mns7Be3Zvptc1Z_pOTkqwncd0pFf_RWK4hkB7JLksWrb-cPqISNMUj_4Bq_pYph9GOs-CDbkOlqnboSDP9DDCVKGh-JNZD6ayoOLdwL0zBfYJ2XFDmy1fzuy_pdvqoeFQdFPZO9KWA8_v6-7khmW1fUTs8lgYfJUHpfnBQ-JO5DUo2mjIvQbXQ0MCWyyntBddW9CNeJskLa9zwqEaRnwEwy376PxvcqmRBGqVyMcnyKQJP6r1aQys_BhF8IAC9h30pvgob-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس به نقل از مقام‌های آمریکایی گزارش داد که ارتش ایالات متحده در جریان موج حملات شامگاه سه‌شنبه دهم شهریور به اهدافی در جنوب ایران، «دو نفتکش دولتی» این کشور را نیز هدف قرار داده است.
بر اساس این گزارش، این دو نفتکش در نزدیکی سواحل ایران و در شمال خط محاصره دریایی آمریکا لنگر انداخته بودند و پهپادهای آمریکایی با شلیک موشک موتورخانه‌های آن‌ها را هدف قرار دادند.
فرماندهی مرکزی ارتش آمریکا، سنتکام، در بیانیهٔ رسمی خود پس از حملات سه‌شنبه‌شب اشارهٔ مشخصی به حمله به نفتکش‌ها نکرد، اما در تصاویر ویدئویی که از حملات منتشر کرد، صحنه‌ای از اصابت موشک به نفتکش نیز دیده می‌شود.
اکسیوس می‌گوید این نخستین بار است که ارتش آمریکا نفتکش‌های ایرانی را نه برای جلوگیری از نقض محاصره دریایی، بلکه در واکنش به حملات ایران به کشتی‌های عبوری از تنگه هرمز هدف قرار می‌دهد.
یک مقام آمریکایی این اقدام را بخشی از سیاست تازه‌ای موسوم به «نفتکش در برابر نفتکش» توصیف کرده که به‌گفتۀ او دونالد ترامپ برای بازدارندگی از حملات بیشتر ایران به کشتی‌ها تأیید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78187" target="_blank">📅 16:36 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78183">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F8m4zIuBZs2i1zSxnpd1-vDvCURYPnDkLcW_7IF_qQYRi5Hlzh8vjqfK3BFjBF1SUQH1SsXyj3SgvxVMpmvmO2aPo3ZjxWAlaU7nJrEehaTgtAZdOK8iEDzZwCqEbDEmGBr4NQ860SH6zcfsZ8EyOeBE_RbXmU1NhCWXWwYE_q0OwHolVAObRp0y_3ASCYb-hoDZ0semv8jZ4xeNKSLg7ldTkynzCT5Bz2uQ0kXd9XhzHR5vJmKHBXh6fe0CMRiznRxepkf1nDQQANyUcHc1P5epzWyfgFBhM1X4mFaf-Uct-iBNB2nSAlXxx1vnrFSW1u43-f6-js-vDYR5wEMzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tK2gA7hVmGvJmoJXRhtI5ivsxGJ1FObNeJmv3LN8l8MTXS46lImIiaRjcm7csaEbI7Jn50Gx7X4vbQkRldRyZpgVL2zPK8Bg8aLByq0Edq40-4GZ87tGBQV_Em7kF8L55ZeGSNkQQwxO3rpRvgN4NjtnTo_Td43qDySScqGaATXNOnRkLXtdllPclsOkvWPjK1fFttaIbQ6FBc-3Xx9EBZUjXBP77F2ygAtIjVZ2xqTYBYeTWVPLjRmHaC_NX1Xz1W_tSOCzrB63DQcuUp9Vj-W7CnBT5Qef2dYEu2v_-BKYa0b_n__UmeGnPagvyNKX1VwVbh75tu9gPxkJqb1YBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=FM31hsiRcmW5EpY-Eu5KtyfKu-yWLjMO6Tua-cGOX36R3xTmJGjsjM1aItG00ZBCFkWHYXW3dPAMvxmazmJyGHG-Xu4SwVJjeZXBCiaWEg7X5DIqJQWEtaeh_oImoj_9eKuRoHHRvD5kafFHNgSUky8AC7NImleEDyQFROBjAd-vnW8QpxJ8CIJvv-gn624RphWu5Uuqok9ytWRmcgygfBtDije3T5wy9vxXnndBANvFcyl5U4WM9RosL0aH1M3CwRyAtgexWyI0_1jqSF7JgXfUoEZYWb7B9o5xS3rEp2_UCTJltq0d-7P1jqexz-OtWRD7Ik2R3CIWEJxeuLdQpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937ffb9011.mp4?token=FM31hsiRcmW5EpY-Eu5KtyfKu-yWLjMO6Tua-cGOX36R3xTmJGjsjM1aItG00ZBCFkWHYXW3dPAMvxmazmJyGHG-Xu4SwVJjeZXBCiaWEg7X5DIqJQWEtaeh_oImoj_9eKuRoHHRvD5kafFHNgSUky8AC7NImleEDyQFROBjAd-vnW8QpxJ8CIJvv-gn624RphWu5Uuqok9ytWRmcgygfBtDije3T5wy9vxXnndBANvFcyl5U4WM9RosL0aH1M3CwRyAtgexWyI0_1jqSF7JgXfUoEZYWb7B9o5xS3rEp2_UCTJltq0d-7P1jqexz-OtWRD7Ik2R3CIWEJxeuLdQpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح چهارشنبه؛ وضعیت چند منزل مسکونی در کوهستک (هرمزگان).
@iliaen</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78183" target="_blank">📅 09:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05113c6026.mp4?token=LIZastW2cPa-mbR28JhAk6763NzQ3U0qw2DQ7kTZEbRz6d6BJY8-RIiprvwRRCuZfM6PWE0QkWF6tJ_g2pE6reNPgfEz-G1gKMzKMPN27QvQ7wrPHj9BDFf7fDEaXcMEJEQ_AE1hycwQyfXaNGRY179thfVeh_HiiN31EWiMnxaYm4FPinWRLbmCLD4uS_pJ-upPsCvH-6gFoc3RpvbmCTa3tsvf_RGL6b6rD_tfmdGx_yuHVdjmzEGgeaqAQ-cPXQpiEzbJVsgUQZXJZhnET2BTNuwk4uoT2NuI-bsy8cu41b7aUsMf0qVoIaoHJutZdMdGqdM9DeIgHonsooXVfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05113c6026.mp4?token=LIZastW2cPa-mbR28JhAk6763NzQ3U0qw2DQ7kTZEbRz6d6BJY8-RIiprvwRRCuZfM6PWE0QkWF6tJ_g2pE6reNPgfEz-G1gKMzKMPN27QvQ7wrPHj9BDFf7fDEaXcMEJEQ_AE1hycwQyfXaNGRY179thfVeh_HiiN31EWiMnxaYm4FPinWRLbmCLD4uS_pJ-upPsCvH-6gFoc3RpvbmCTa3tsvf_RGL6b6rD_tfmdGx_yuHVdjmzEGgeaqAQ-cPXQpiEzbJVsgUQZXJZhnET2BTNuwk4uoT2NuI-bsy8cu41b7aUsMf0qVoIaoHJutZdMdGqdM9DeIgHonsooXVfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روستای کوهستک در سیریک هرمزگان
ویدیوی منتشر شده در منابع حکومتی از مکانی که مورد حمله هوایی آمریکا قرار گرفت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/78182" target="_blank">📅 09:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MrAL5QYlRADc9IsQeEri_OozWmD6mOGo8jrL_bdGRzxnRMdaiEizN9BK6grkhqjQhtQ9PIAS_1Ao2_T-X0qu-8-jS2eMybzGpU4aPbn_Jjc-adZi1tbSss76UTPNF3ISmANpIk9cE01j9ds0XmC2mX4NFOtuwUm9feL834ZX15hcRtW6qkpedcmKTuvuTG9LcaNlmd5dZTQKMu0Rue131lHXGwFJ4E7PyrKmnuVZqHs69WemLU78DgHNQV_YFpKWh0qRtLoWqlQINXwPgnAKW-k0EIYhfXn4DrJ3zxBhKlP7sRoTnEmD969iC9PBnX8miSovyXaVbB0iXMkl4PwCCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من تلاش نمی‌کنم ایران را، آن‌طور که ABC Fake News گزارش داده، به پای میز مذاکره بکشانم.
اصلاً برایم مهم نیست که آن‌ها توافقی امضا کنند که برای خودشان هم ارزشی ندارد.
من موقعیت فعلی‌مان را خیلی بیشتر می‌پسندم؛ با کنترل تقریباً کامل بر تنگه هرمز و اقتصادی که در ایران کاملاً در حال فروپاشی است.
آن‌ها فقط دارند روند اجتناب‌ناپذیر را طی می‌کنند.
مردم ایران چه زمانی به پا خواهند خاست و خواهند جنگید؟
رئیس‌جمهور DJT
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 467K · <a href="https://t.me/VahidOnline/78181" target="_blank">📅 04:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=JyLDgZZA4AosGLSNkuaYFZ6QWIKj4lJBdm3Sj6rXBzIOMKt83F7XdSkCT8HMdI_-kf91qC5BcqshXYhvR-ezSSWWOvyy3lJ093a2EFQPPi2HoGsGUdbV2ogUXiglcz2HzwP3JcmhVoGXA_a0spuMb9ystInmmCaogRM7GZtfJwS-3Zj82t673kUCK38q4WMZ0gA3fuL9WQPmFNmIGDYXKBl2TPEmecVTVDZmjFgLts7J9XVN_W6scTj712u_-Y6lNmfz1OXX4Xjv0yuhOBKTRjFSSIqZwSh6VS3D3os5mXFeCll2or0MQmx-VU07x7x7D75NuAQQUfUcLo0YOG-j5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec60d5ccce.mp4?token=JyLDgZZA4AosGLSNkuaYFZ6QWIKj4lJBdm3Sj6rXBzIOMKt83F7XdSkCT8HMdI_-kf91qC5BcqshXYhvR-ezSSWWOvyy3lJ093a2EFQPPi2HoGsGUdbV2ogUXiglcz2HzwP3JcmhVoGXA_a0spuMb9ystInmmCaogRM7GZtfJwS-3Zj82t673kUCK38q4WMZ0gA3fuL9WQPmFNmIGDYXKBl2TPEmecVTVDZmjFgLts7J9XVN_W6scTj712u_-Y6lNmfz1OXX4Xjv0yuhOBKTRjFSSIqZwSh6VS3D3os5mXFeCll2or0MQmx-VU07x7x7D75NuAQQUfUcLo0YOG-j5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شروط پکن برای سفر قالیباف به چین'
حسین مرعشی، دبیرکل "حزب کارگزاران سازندگی"، گفت: خیلی روشن به ما گفته‌اند که
۱- تنگه هرمز را باز می‌کنید
۲- عوارض نمی‌گیرید
۳- با عربستان سعودی مسئله‌تان را حل می‌کنید
۴-  با آمریکا مسئله‌تان را حل می‌کنید
بعد قالیباف به چین بیاید.
قالیباف در اردیبهشت سال جاری، با پیشنهاد مسعود پزشکیان و تایید رهبر جمهوری اسلامی به عنوان «نماینده ویژه ایران در امور چین» منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/78180" target="_blank">📅 04:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">منابع حکومتی:
روابط عمومی سپاه:
🔹
مردم شریف و انقلابی اردن؛ یکبار دیگر دست شیطان از آستین ارتش کودک‌کش آمریکا به درآمد و با بمباران وحشیانه به مراسم جشن عقد یک زوج جوان اهل تسنن در منطقه سیریک هرمزگان، عمق کینه خود را به امت اسلام به نمایش گذاشت.
🔹
ارتش تروریستی شکست خورده آمریکا که از رویارویی مستقیم با رزمندگان اسلام عاجز است، با استیصال مردم مظلوم را به خاک و خون کشید و مراسم جشن عقد پاک مردم را به عزا تبدیل کرد.
🔹
ارتش جنایتکار آمریکا که در آغاز تجاوز خود به ایران اسلامی ۱۶۸ کودک دانش آموز را در مدرسه میناب و ۲۱ کودک ورزشکار را در ورزشگاه لامرد به شهادت رسانده بود، شب گذشته در این حمله ناجوانمردانه حدود ۷۰ نفر از مهمانان این مراسم را مورد اصابت قرار داد که ۴ نفر از آنان از جمله یک کودک خردسال به شهادت رسیده و حال تعدادی از مجروحان وخیم هست.
🔹
در قصاص این جنایت، رزمندگان نیروی هوافضای سپاه پاسداران انقلاب اسلامی در یک حمله سنگین با موشک‌های بالستیک، آشیانه‌های هواپیماهای بدون سرنشین دور پرواز آر کیو ۴ و ام کیو ۹ را در پایگاه هوایی آمریکا در اردن موسوم به پرنس حسن مورد حمله قراردادند که تعدادی از پهپادها منهدم و تعدادی از خلبانان و خدمه فنی پروازی به هلاکت رسیدند.
🔹
همچنین چندین زیر ساخت فنی آنها به آتش کشیده شد.
🔹
مردم شریف و پاکدل اردن، اردن قدمگاه مقدس انبیاء الهی است، نباید جایگاه ولیدهای شیطان بماند. امروز با این جنایت های سبعانه، حجت بر همگان تمام است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/78179" target="_blank">📅 02:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=cQfHqD7ycwwDpq0XKCqTeizb-fl-ChXA3unh2qj7VHJDuCafVxxlGVmbo6LPS1-oUGtIKFmkFCvppejCzSl2xngqMJB7KmXEwNx7H0lnSsIy-K-gRdxoD3VV8ll0WjMkMPpJXu9hRM_Mpn6TbEOJoltm1CNfYK8hcSifXJhd5NwE03A9a8crQ0TQZB-JAm-TRmwXgwU56l0bnCrxHkqV0__5F-CPqNKR2yOOZlsiNM1ktQuV42YveGekOKS6qiTmvvIVS1U2Tkkr4m127-BGWseETYTJpdPsNSVNlBsFW4MfSy79bfs8hEDMbJlYJ_iH5NnN5YBNi2zF98Z47BFjVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ec549d5483.mp4?token=cQfHqD7ycwwDpq0XKCqTeizb-fl-ChXA3unh2qj7VHJDuCafVxxlGVmbo6LPS1-oUGtIKFmkFCvppejCzSl2xngqMJB7KmXEwNx7H0lnSsIy-K-gRdxoD3VV8ll0WjMkMPpJXu9hRM_Mpn6TbEOJoltm1CNfYK8hcSifXJhd5NwE03A9a8crQ0TQZB-JAm-TRmwXgwU56l0bnCrxHkqV0__5F-CPqNKR2yOOZlsiNM1ktQuV42YveGekOKS6qiTmvvIVS1U2Tkkr4m127-BGWseETYTJpdPsNSVNlBsFW4MfSy79bfs8hEDMbJlYJ_iH5NnN5YBNi2zF98Z47BFjVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متنی که اکانت سنتکام به همراه ویدیوی بالا منتشر کرده، ترجمه ماشین:
سنتکام حملات به اهداف سپاه پاسداران در ایران را به پایان رساند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در روز اول سپتامبر، موجی از حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندند.
نیروهای آمریکایی اهداف سپاه پاسداران انقلاب اسلامی را هدف قرار دادند که شامل مواضع پدافند هوایی، سامانه‌های راداری، تجهیزات و تأسیسات دریایی، توانمندی‌های مین‌گذاری و مراکز ارتباطی بود.
این حملات پس از تلاش‌های اخیر سپاه پاسداران برای حمله به کشتیرانی تجاری در تنگه هرمز و نیروهای نظامی آمریکایی انجام شد.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه مشغول فعالیت هستند و همچنان هوشیار، مرگبار و آماده‌اند تا به اجرای عملیات‌هایی که فرمانده کل قوا دستور می‌دهد، ادامه دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/78178" target="_blank">📅 02:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IGicn3lA8NKf_skvzWRzgTLbZZuMsHflb9tBLFIhozfj1O9bBs0-MTQ8rP2VzVSdKzZ8YUJhh3uPbGMU39DBOjAbX93vqBlcDEkwxhixydNysahhcf0Q_lVFmvKdfXqKFXNMTX6s7Wyy-jHorVNCV1ppS95qI9KGDxNtKvgpFJwFNP8E55USe5pvEEIiP5HOQ5QkwrSVxKSAScyeRb0zXxe-mCSuY9yHdd81UYsTGD6TlrHeA99LttCEHpeFKmoLTr78FQnIu_BhH5xyXZbRMKyrkGYmet4QK5jRZvfehZSGZYvUnoJ7i8BlYKTE5FGxpQJrM-1R5RGfwEPhjzMcQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DSDhEqhtm-aYSWaqJWdta_cVI3tn0Y504lDtr9lJBA2LgewgYa5afnOxVXrXuvUx4SdDJmsolr7W_yovPlaWw1-xIaaln3vhLjmh51Bp__2wdTlFy4uKQobESldPECaRH5svbHAbEfhGmQa7ap2_dTNPTfgoK-yVeg1EwYYWVbJAOs8hXshh_mtiOUPWGTgY5e_sf3uWgiQhl5iK3u9ewUsU1n8B782OhyK7QCTVlH7E_2B553VNMlhTtDzVipBZBFtjluua_MLobSEblKbgKwD2E6JwDto9KLfU4PGgcjVDDNX-krVPruGBn2yUHxcY8gA6Nr1vcrhhC3E1n4k4Ew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">"ستاد کل ارتش کویت" در فاصله چند دقیقه دو اطلاعیه منتشر کرد که گویا دومی فقط یک کلمه بیشتر داره. ترجمه ماشین:
اولی:
⚠️
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات پهپادهای متخاصم است.
KuwaitArmyGHQ
دومی:
⚠️
پدافند هوایی کویت در حال حاضر در حال مقابله با حملات موشکی و پهپادهای متخاصم است.
KuwaitArmyGHQ
ادامه متن:
"ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، این صداها ناشی از رهگیری اهداف متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان خواسته می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی مراجع ذی‌صلاح را رعایت کنند."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78176" target="_blank">📅 01:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78175">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0abfd3996d.mp4?token=ljZaA01eov2yhe3eYAD2b8qz-3VLARorHnBiRrikNgAAPGXqTXnXdayavRLsQRSfQkCJfcb5-N1sYgEQlCW1QzZZig_vtE2KqPa6es4wjB1_Utr-IpDGaR5rGh_-czeo-wfDmDldpk50N_Pj1f_zCmonmFHuHcJcY0IO-ixPKq6oMZoD3MS4yLLDtYlBzqYjPzKBOUafqVxia4yRCYHfT5plse5d0N3I-BmTa5WaVLKfMLkRabCbeOCvjAjxjiy_cKd9N-4Flb9gvn9at9XynOi28D5SKqIKsID6_HEsxi7lVNWhhh_eXNbzOmk363F_W-LmnxHpqKJe_enPmkVacg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0abfd3996d.mp4?token=ljZaA01eov2yhe3eYAD2b8qz-3VLARorHnBiRrikNgAAPGXqTXnXdayavRLsQRSfQkCJfcb5-N1sYgEQlCW1QzZZig_vtE2KqPa6es4wjB1_Utr-IpDGaR5rGh_-czeo-wfDmDldpk50N_Pj1f_zCmonmFHuHcJcY0IO-ixPKq6oMZoD3MS4yLLDtYlBzqYjPzKBOUafqVxia4yRCYHfT5plse5d0N3I-BmTa5WaVLKfMLkRabCbeOCvjAjxjiy_cKd9N-4Flb9gvn9at9XynOi28D5SKqIKsID6_HEsxi7lVNWhhh_eXNbzOmk363F_W-LmnxHpqKJe_enPmkVacg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌زمان ویدیوی دریافتی از شهرستانی در استان ایلام
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78175" target="_blank">📅 01:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8CEswkYcQyJn1AIF4dQFUYlw38xIe9-XqCwIeYMRt5GJ5R3FzTBfvrHLEKPIX6XiQh_8zc9tXhWkF_oKj7EWGaWlpUvH33aEBusJxxVMWdyLhQuhuVN369TvxEa7QXbrfhVBexnVs7iAxe_b4XpaqyGqU0SdUZM4kSEtS881mMg-wk2JptSsBwtGP3_tzWHmPnZ2_kmGxY58QBPflpcUciUads2NQHFdjP5agQKN22lkPnTf_S6vyP1-dIDj4ZYzMey4bWemzE5jx-bZiZQcJeHUeGt1QVu_ffizQvVOCzfei8ANrDVFxRnaLgeA4m0f7oxQHX2w1fZQa7GdxqkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: صدور هشدار در کویت
ترجمه ماشین:
هشدار: خطر قریب‌الوقوع
............. تهدید امنیتی .............
همه موظف‌اند در مکان‌های امن بمانند و برای تضمین ایمنی عمومی، از پنجره‌ها و مکان‌های روباز و در معرض خطر فاصله بگیرند.
دفاع مدنی — وزارت کشور
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 412K · <a href="https://t.me/VahidOnline/78174" target="_blank">📅 01:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=TBcmNd2LixF4yj6VBZlokFKPfh8fvxgFHjaBgy-k9yrElR5A8a9d1LAk3hOgzcz9_EZlm8cDJDlppdjyngPSdwDKCom72LPyiak3pu2OaiEB7BY7b413gR8o3pN0MHNapw1khcnQYf0Z9B60S4kkEBMRVx7c3FTzLp96CtWc-BJ_e7Xbho7wrinagu6GF_iURA9jlWFGB_aiqZv-yfZS5a15T7-vAXYE1uhCp_BghQudGaMmmpjt3KRmwXNS7dUZIFIQIIUlJxYmWOFJsGmioV2-Yn5gWi8DTYHWLtOzkSMBav1KzQSSzfa0w1lK1a4OBi3N5GrL6ycgNTExqzyfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=TBcmNd2LixF4yj6VBZlokFKPfh8fvxgFHjaBgy-k9yrElR5A8a9d1LAk3hOgzcz9_EZlm8cDJDlppdjyngPSdwDKCom72LPyiak3pu2OaiEB7BY7b413gR8o3pN0MHNapw1khcnQYf0Z9B60S4kkEBMRVx7c3FTzLp96CtWc-BJ_e7Xbho7wrinagu6GF_iURA9jlWFGB_aiqZv-yfZS5a15T7-vAXYE1uhCp_BghQudGaMmmpjt3KRmwXNS7dUZIFIQIIUlJxYmWOFJsGmioV2-Yn5gWi8DTYHWLtOzkSMBav1KzQSSzfa0w1lK1a4OBi3N5GrL6ycgNTExqzyfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پلیس راهور جمهوری اسلامی ایران:
یک دستگاه هیوندای با سرعت بالا با یک دستگاه چانگان در مسیر موازی برخورد کرده که در پی این برخورد تعادل خودرو بر هم خورده و با جمعیتی که در حمایت از نظام و نیروهای مسلح در حاشیه خیابان حضور داشتند، برخورد می‌کند
راننده حالت عادی نداشته و پس از برخورد با بشکه‌ها و علائم ترافیکی، با جمعیت برخورد می‌کند و در نتیجه این حادثه تعدادی از شهروندان فوت می‌کنند و برخی نیز مصدوم می شوند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/78173" target="_blank">📅 01:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=M6CYst3QWaxUUyFIauzj0TTa2c-obf-PCxA7dW6cPvU7lUVfnZXruruPx-s6tag7zmHcthPh_T0KjI124Wm9BOy6b1haCZduozThaW7kw2BLQLkEv0gjzK2JJCG5Oj1R8vQZIk-0w7eOQgru-ukxu1bX941rzuWOPYQxffN1KUP9IhpmocR3S86ybokL8NHe_G4ukVGxEabAkGUY70YtS0MeDVg1v0RUqmTEsEq2Nf8OOyJy39fQC9WkXeC_pT35R8UgktCzPTVIPMHHWPej0oqslilFfIv5Obj8LNwBh1G_42fxk83mR8Sd9xY0z7SpKE95ZVtAleZMIIepEL6Dzw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=M6CYst3QWaxUUyFIauzj0TTa2c-obf-PCxA7dW6cPvU7lUVfnZXruruPx-s6tag7zmHcthPh_T0KjI124Wm9BOy6b1haCZduozThaW7kw2BLQLkEv0gjzK2JJCG5Oj1R8vQZIk-0w7eOQgru-ukxu1bX941rzuWOPYQxffN1KUP9IhpmocR3S86ybokL8NHe_G4ukVGxEabAkGUY70YtS0MeDVg1v0RUqmTEsEq2Nf8OOyJy39fQC9WkXeC_pT35R8UgktCzPTVIPMHHWPej0oqslilFfIv5Obj8LNwBh1G_42fxk83mR8Sd9xY0z7SpKE95ZVtAleZMIIepEL6Dzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پیکر بی‌جان
ویدیوهای منتشر شده در منابع حکومتی: یکی در
#مشهد
با خودرو کوبیده به تجمع بسیجیان
سه‌شنبه ۱۰ شهریور
Vahid
دست‌کم چهار کشته در برخورد خودرو به تجمع‌کنندگان در مشهد
دقایقی پیش خبرگزاری‌های ایران گزارش دادند که راننده خودرویی که به میان تجمع‌کنندگان در بلوار وکیل‌آباد مشهد راند، بازداشت شده است.
خبرگزاری صداوسیما گفت که در این حادثه «۴ نفر کشته و بیش از ۱۰ نفر زخمی شده‌اند.»
پلیس راهنمایی و رانندگی مشهد گفت که یک ماشین «هیوندای جنسیس با سرعت بالا منحرف شده» و پس از آن به میان جمعیت برخورد کرده است.
گفته می‌شود این خودرو به «تجمع‌ شبانه حامیان حکومت ایران» برخورد کرده است.
هنوز علت این حادثه از سوی مقام‌های مشهد اعلام نشده است.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 503K · <a href="https://t.me/VahidOnline/78170" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XGS3ib_QeXgo8LTj5IfGj_6xA8Y578TWhtdX-xdKx1YNvmeuG8Qru46n2ZQOkPGJUwz9-jNBaFXq6L1fy5FCQ0Dpr8disvgvlz3NeyaBQQNW9Wqwbms7zxG0i_FH39n5ellmKI6G4UI66LuIAfZKBsRJz5EFwONuhz4k3eFXiid-vrLNWIG5kpsYihAml9RYhEfkS2vf4bks35L8l0IQXQRPCUxNcAxiuW-SYOtREiY6dvLWC3b5TdPA9OZOVnzAldLIs7cC1XD9Htl5Pm_ivh0iC9oBtzF-sWaIrRJ7ksifTLZLd798-JAKW8cT2wRolNdTpFEWwy_NuKczfLZm4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OZflLWoAcXvJy5Ci8Fe3AUhRn7bcz7Zfg_Ny7rx1ZnsSLXcHhpKHvkFV2uUAW-3qt2U7HUdFDs1ffO_aXo_NsNGT9U54JMDn8UjSfZlU6q9Hc9PvIrSOzdgNWDbzV65KyEWc8dmdgB0AYzmCasVFloqI_8pIGrkyMiFxhw3SbLuxaC6yvxnKDRPKD8sPTesnaO32_2efAOwMwaQh0xsF1-OOQCjO3r-Hh0RSPooIaC-AXt5RxN4l9Kr4Vwvr9I0eCMq1mDcWiBi-esRBzy0j5pVi0-FSI3--d1GCp-qsGxji2W_a6Nr1H-Tan3ob_OgRDInKSR0o23GM5j8UP1vcQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت دکل مخابراتی کوهستک که در منطقه مسکونی واقع شده بود.
@iliaen</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/78168" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/620ad89cef.mp4?token=e-bsFlUYXMB7qDCmG7U3aKv64Dmbt6Z_XSw0-cAtDpfybPH4h1gSFNZ7GP4RI8waA7J297LsXqQazZluiXlN8PpVxLR0cFqJJuvGGFPLbWKmKE3HcmGqbTK3eigIPFnOTCf2ZcdXsQuhNZkgINsByKYiHLzhwuevmNsRHwW3YWuth2XWX4whuJISZQFD6KAqvfnydPs0VVnbtAz1O9hHSN303QNXmFGZaM24c2Ersc6HhXmU0cmBUhGnoyZELgTkJQ1u4N51UqIdKWZ2LWSSIaKOR83fms-G-OHKF4NW2sCe_XHe8rpAXBHKdVBE4JyIEt1cyDETXY00JPbiId8ATw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/620ad89cef.mp4?token=e-bsFlUYXMB7qDCmG7U3aKv64Dmbt6Z_XSw0-cAtDpfybPH4h1gSFNZ7GP4RI8waA7J297LsXqQazZluiXlN8PpVxLR0cFqJJuvGGFPLbWKmKE3HcmGqbTK3eigIPFnOTCf2ZcdXsQuhNZkgINsByKYiHLzhwuevmNsRHwW3YWuth2XWX4whuJISZQFD6KAqvfnydPs0VVnbtAz1O9hHSN303QNXmFGZaM24c2Ersc6HhXmU0cmBUhGnoyZELgTkJQ1u4N51UqIdKWZ2LWSSIaKOR83fms-G-OHKF4NW2sCe_XHe8rpAXBHKdVBE4JyIEt1cyDETXY00JPbiId8ATw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آپدیت: '
در حمله به سیریک ۴ شهروند کشته و ۶۵ نفر زخمی شدند
'
ایران گفته است در حملات هوایی آمریکا به بندر کوهستک شهرستان سیریک، چهار نفر از جمله یک زن و یک کودک که در مراسم عروسی شرکت داشتند کشته و ۶۵ نفر مجروح شدند.
رئیس دانشگاه علوم پزشکی هرمزگان گفت دو نفر در محل کشته شدند و دو نفر در بیمارستان جان باختند و «شش نفر از مجروحان در بخش مراقبت‌های ویژه بستری‌ شده‌اند و ۲۶ نفر هم در بخش‌های جراحی تحت درمان قرار دارند.»
@
VahidHeadline
در همین رابطه یک منبع محلی به بی‌بی‌سی فارسی گفت به گمان او هدف حمله هوایی «یک دکل مخابراتی» که در فاصله «چند متری خانه محل برگزاری عروسی و آن طرف خیابان» قرار داشته بوده است.
@
VahidHeadline
در پیام‌هایی که من دریافت کرده بودم هم نوشته بودند هدف حمله یک
دکل مخابراتی
بوده و در اون حمله شهروندانی در خانه‌های اطراف، از جمله در یک
عروسی
، کشته یا زخمی شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/78167" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=cOZglR5mKZNFDtJMBKpxRpHksSl3UAJSPzNvm1Mkm-1yd09NfuVJ65Y_3DnkXlBfq3o_nCb3UcDC-2RBlP26A5UhS_kkaVqo2rfeKN9WKd8t6_86PlIn3J2t-yPsEocsd9lF9UCBu4tregEg6lZhNsLtIOe2RKJXGrLCr_NGZGDU40zp-KYTygImZvEGb-ncSDfphuNsXi560bkvwvxvgiKH4qtsdnbwO97_kATAYZDnX2cNGSFsKHrQtUg5tnmV9ynOPtv0dyGoaXbu4KngaLB9zTuziwoP3R0jkW_UPt5RvDC6H9rMn61xqdk-cc2cAgkfzldycUQT9_mzd14PoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=cOZglR5mKZNFDtJMBKpxRpHksSl3UAJSPzNvm1Mkm-1yd09NfuVJ65Y_3DnkXlBfq3o_nCb3UcDC-2RBlP26A5UhS_kkaVqo2rfeKN9WKd8t6_86PlIn3J2t-yPsEocsd9lF9UCBu4tregEg6lZhNsLtIOe2RKJXGrLCr_NGZGDU40zp-KYTygImZvEGb-ncSDfphuNsXi560bkvwvxvgiKH4qtsdnbwO97_kATAYZDnX2cNGSFsKHrQtUg5tnmV9ynOPtv0dyGoaXbu4KngaLB9zTuziwoP3R0jkW_UPt5RvDC6H9rMn61xqdk-cc2cAgkfzldycUQT9_mzd14PoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از بیدگنه
سلام همین الان از بیدگنه موشک زدن
سلام از فردیس موشک فرستادن
سلام وحیدجان
ساعت ۲۳:۱۳ از سمت جنوب مهرشهر کرج صدای بلند شدن موشک میاد.
سلام الان از بیدگنه موشک زدن
از کرج موشک زدن چندتا
از بیدگنه ملارد بود احتمالا
درود همین الان صدای بلند شدن موشک از فردیس کرج اومد
همین الا از ملارد بیدگنه موشک شلیک شد
همین الان از بیدگنه چندتا موشک شلیک کرد
سلام از ملارد موشک زدن ساعت ۱۱:۱۲
+ ده‌ها پیام مشابه دیگر از این منطقه پرجمعیت که نمی‌رسم بخونم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/78166" target="_blank">📅 23:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیام‌های دریافتی:
سلام همین الان از کرمانشاه موشک زدن ۱۱و۰۷ دقیقه
داداش کرمانشاه پردیس دقیقا همین الان صدا اومد
همین الان از کرمانشاه موشک پرتاب کردن
صدا انفجار شدید کرمانشاه الان
وحید همین الان از کرمانشاه موشک فرستادن ۲۳:۰۸
کرمانشاه الان موشک زدن
کرمانشاه صدا جنگنده میاد وحشتناک [صدای پرتاب موشک با جنگنده زیاد اشتباه گرفته میشن.]
10:08 کرمانشاه موشک رفت
همین الان از کرمانشاه موشک فرستاد ...
سلام وقت بخیر الان هم از کرمانشاه صدای شبیه پرتاب موشک اومد ۲۳:۱۰
کرمانشاه دارن موشک میزنن، هنوز ادامه داره ۲۳:۱۱
موج دوم موشک از کرمانشاه ۲۳.۱۲
آپدیت:
پیام‌های کرمانشاه تا پنج تا موشک ادامه داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/78165" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پیام‌های دریافتی:
الان موشک از،یزد زدن
از یزد موشک زدن الان
سلام وحید جان
همین الان از یزد موشک بلند شد
همین الان از یزد موشک زدن
وحید یزد همین الان موشک بلند شد ازش
الان از یزد موشک پرتاب شد
🔄
همین الان دوتا دیگه
دو تا دیگه از یزد زدن
۲۳:۰۸ دوباره از
#یزد
موشک زدن.
۳ تا موشک دوباره یزد بلند شد
سومین موشک هم شلیک شد
ساعت 11:08 دوتا موشک دیگه از یزد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78164" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qbbcImgBErpCe1jTl8uaJZ_K1ZEPYgfKM7_M7kr0NIKrbmuQFgOXTDt9SCCNkycILqFg1x7LYxpdZ1nxBcP_eqcRuQRDszjPKnxYg7HpcVWyBDIXFwiOmk6sWDr_uAkh2aoAW2dz01v3UcRnMBjAX1nFpCCn_gsvO-9ShUTriN9yp3lVgRu-EFZWJQ3kcRIQm7rMR7-7ny-2hq2LfaFSB5lUpdEO3JDCC3BIR-KKTb-EwAZI4snPy7Y6261BCm3aVvTNlU-JiA6RUfX1GJZwo4f0kmnKAdCUHXFHuvcLiyzdh7HMjTcKEU5iBwYFJZG-wED1lr-_8A9lyDwGCZ5ZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TJyjVq0vHIF1QuIia6dW6eH5iplOkcTczon3eR2WAz6P5wwBGJI8yX9AtyKfxHgdKkzuC4gAQ0JeZQGs6qh_fd6O7t2BTs5HkPZdN_vzm4BGEn98PxO2YaBvUS5yLsMIdikw3bccviy6FtS4DNiZw12HcUM7PymOigAS5UvvaxBd-aVMyZv5WMAfW6C0mg38p8U4UTuQ4ke1wVP2avl-TvB43Fenamcs_9iBA54AAYyRXlYAZC3GvUCeqeM_SQsUVkZjhZccwoXd0GdV9pvEtuIwnnkZ7d5mH99tKVZfV9iKGmHRQ8G7Wo4MUrvNRrcAOiRhS8sq1m9cUl1OBYAN9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=Qa-WOJnHX2FPhVGI8sfLH9oGaG2v-FnI_4E2l4MqMHOMJ42kCsUxQeztrbq8eqp_kkDdoaICZSLYbCIbKGET1scSVH6Vdtccjvr8Udu8VNOew0aoT0nmx5kjoItu1C8xP_83jF9WesTp6jheZkj1h9OjyBxHqEUfxVqckTRsCZ20XD9DLbr6OhvPGvTtOaMqph5_E0sWu8a_h2yWzpZYZ-qjOJBrfVCb5-l3uGk136PcYDFJUjFrDBtxs5R4hd87-lK0T5KDDZLWMk2mhUaLaSbUujhnhJ-wkdebtuq_ySsFygvbIJFAmczJYcUCM2GxY7pDnQntompR1TNZOq5Gow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=Qa-WOJnHX2FPhVGI8sfLH9oGaG2v-FnI_4E2l4MqMHOMJ42kCsUxQeztrbq8eqp_kkDdoaICZSLYbCIbKGET1scSVH6Vdtccjvr8Udu8VNOew0aoT0nmx5kjoItu1C8xP_83jF9WesTp6jheZkj1h9OjyBxHqEUfxVqckTRsCZ20XD9DLbr6OhvPGvTtOaMqph5_E0sWu8a_h2yWzpZYZ-qjOJBrfVCb5-l3uGk136PcYDFJUjFrDBtxs5R4hd87-lK0T5KDDZLWMk2mhUaLaSbUujhnhJ-wkdebtuq_ySsFygvbIJFAmczJYcUCM2GxY7pDnQntompR1TNZOq5Gow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی: سه موشک از
#خمین
پرتاب شد
تصویر دریافتی سوم از آسمان ازنا در لرستان
سه‌شنبه ۱۰ شهریور
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78160" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=fnNrE9i45aaIu_2hsIYrIR9irrr1U8dIr-izKx27dk0mFmXmEAzVi8gOXZdZ6xzQF3D3L5ipsSfqKvw_9_iLkg91J92pj-D8iFm6EvjiiZ3p_KIfURXK3UY4woyh-gjlNL04RmFk7lqLaP1T9FF2545SVyG9BOkuCJvTb13LDyFkcg5Oyu_hPDSs3hztG9WQwW35PEmHUXe0RjBOfDy4Q5El40XEOeMkQzIhP31pWqJ1FwZZpqQORqfDKLsGtUzgIyxDD39qB54_mUQgMABxRxERjebkZPy0HKaB05ip8wUEftgPM-65AE20PygDovgnkAsLxpqWsCQrwqCYHXwA7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=fnNrE9i45aaIu_2hsIYrIR9irrr1U8dIr-izKx27dk0mFmXmEAzVi8gOXZdZ6xzQF3D3L5ipsSfqKvw_9_iLkg91J92pj-D8iFm6EvjiiZ3p_KIfURXK3UY4woyh-gjlNL04RmFk7lqLaP1T9FF2545SVyG9BOkuCJvTb13LDyFkcg5Oyu_hPDSs3hztG9WQwW35PEmHUXe0RjBOfDy4Q5El40XEOeMkQzIhP31pWqJ1FwZZpqQORqfDKLsGtUzgIyxDD39qB54_mUQgMABxRxERjebkZPy0HKaB05ip8wUEftgPM-65AE20PygDovgnkAsLxpqWsCQrwqCYHXwA7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
خمین همین الان دوتا موشک زد
سومی رو هم زد
سه تا موشک از خمین زدن
سه صدای شلیک موشک از الیگودرز - احتمالا سمت خمین باشه
شلیک مجدد موشک از خمین، بیش از 3تا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78159" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پیام‌های دریافتی:
قشم دو انفجار شدید اطراف شهر
شد ۴بار پشت سر هم و شدید
ساعت ۲۲و ۲۸ دقیقه
۲۲.۲۹
دوتا انفجار بزرگ بندرعباس
سومین و چهارمین انفجار بندرعباس  ۲۲.۳۰
سلام قشم رو الان خیلی بد زدن
بندرعباس ۱۰:۲۹ سه تا صدا
چندتا صدای دیگه هم داره میاد
بندرعباس دو صدای انفجار
بندر دوباره دوتا انفجار
وحید شد ۴ تا
وحید جان بندرعباس مجدد 22:28 صدای سه تا انفجار از سمت ساحل اومد
ما خونمون بغل فرودگاس
شهرک صنعتی طولا قشم یا ناحیه سپاه چهارتا انفجار، صدای سوت موشک قبل از انفجار هم اومد
۲۲:۲۸
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/78158" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78157">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lMPrXdovPwbUht6vv21kK6hJpjOIhEL9SqhAYplLjEe7FEBdFXku37UxU0d_OnE0llzkmfJ7BJbI3Xbq6vO05GsGh6R8i6eMeEeCNwaVLDFEOCFHw_oz7Xkir5rtWoqF44lZxmSbKj0DYuSQodmJrlKPQBWMffEj6A0A4-3yHDJn_4ufPup3_YxWB3xuAnZPdMubLitmClWXL6jgThdBNy2e9F5Ah8pEPM3dbvwSIplh2XvCnUi99IkwF8wmupGBjnLmz4rWV4tt480B-ajv3I4YfHBHPrCCyswbLIxC6eQo_T3Sxo2Q1nSp3Y1UEzNdaCBv7V7Ncgxb2DdLzMpJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا، روز سه‌شنبه ۱۰ شهریور در گفت‌وگو با شبکه فاکس نیوز بازگشت به «تفاهم‌نامه اسلام‌آباد» را رد کرد و گفت توافق با ایران «ارزش همان کاغذی که روی آن نوشته شده را هم ندارد».
ترامپ درباره پاسخ جمهوری اسلامی به حملات آمریکا گفت: «اگر آنها پاسخ بدهند، با شدت بسیار بیشتری هدف قرار خواهند گرفت.»
او حملات انجام‌شده را «بسیار بزرگ» توصیف کرد و افزود اگر درگیری برای سومین بار تشدید شود، ایران «به‌عنوان یک کشور به‌طور کامل از بین خواهد رفت».
رییس‌جمهور آمریکا گفت حملات اخیر، سامانه‌های راداری در جنوب‌غرب ایران و نزدیکی تنگه هرمز را هدف قرار داده‌اند؛ سامانه‌هایی که به گفته او ایران در حال بازسازی آنها بوده است.
ترامپ گفت نیروهای آمریکایی بخش قابل‌توجهی از شبکه راداری ایران را منهدم کرده‌اند و افزود: «آنها تلاش کردند رادارهایشان را دوباره بازسازی کنند، چون نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریبا آماده شود و بعد آن را هدف قرار دادیم.»
او همچنین گفت ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» به‌طور کامل برای ادامه عملیات در صورت نیاز آماده است.
ترامپ بازگشت به «تفاهم‌نامه اسلام‌آباد» را نیز رد کرد و گفت توافق با ایران «ارزش همان کاغذی که روی آن نوشته شده را هم ندارد». او افزود آمریکا فرصت‌های زیادی برای دستیابی به توافق در اختیار جمهوری اسلامی قرار داده است.
رییس‌جمهور آمریکا همچنین گفت متحدان واشنگتن در منطقه خلیج فارس پیش از حملات اخیر در جریان این عملیات قرار گرفته بودند و رهبران ایران درباره عزم او دچار «اشتباه خطرناکی» شده‌اند.
ترامپ در پایان سخنان خود درباره مقام‌های جمهوری اسلامی گفت: «آنها دست‌بردار نیستند؛ آنها دیوانه و احمق‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78157" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1885075f5.mp4?token=EcFC_5URwZIW6967j0naIrQ1t6Lfy8HtquoAh0JuNsuON1aHHQmdCTJZw_XWXC1prhUMMMgxcwL30qFFbRJNhtt3zBf00jDzz4J9MF1Gwivlzu4t_x6wrCaS5vwxxkpeIPv8LGUlQoc_hBFOunbXeiSadOFMqBObh6mb3-gmkCR6K6cc00xPLFVHTGXVONl_H6H9QJ5hFHV6tO0Otr9U_PtRr0y_Ezk4aGYkx1Vuhyt9dPgRT8iHSJ5VqxgzFMAdBj3V5ZXkaDdTNcsG-_URC7_4Gh3PjsFXZz-5N_6d7_BuQEq-uUu-SfvJsjUNNQjUEmDpXkimrNAJWH8wyCmDMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1885075f5.mp4?token=EcFC_5URwZIW6967j0naIrQ1t6Lfy8HtquoAh0JuNsuON1aHHQmdCTJZw_XWXC1prhUMMMgxcwL30qFFbRJNhtt3zBf00jDzz4J9MF1Gwivlzu4t_x6wrCaS5vwxxkpeIPv8LGUlQoc_hBFOunbXeiSadOFMqBObh6mb3-gmkCR6K6cc00xPLFVHTGXVONl_H6H9QJ5hFHV6tO0Otr9U_PtRr0y_Ezk4aGYkx1Vuhyt9dPgRT8iHSJ5VqxgzFMAdBj3V5ZXkaDdTNcsG-_URC7_4Gh3PjsFXZz-5N_6d7_BuQEq-uUu-SfvJsjUNNQjUEmDpXkimrNAJWH8wyCmDMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
پرزیدنت ترامپ به فاکس نیوز گفت که امشب شمار زیادی از رادارهای ایران هدف قرار گرفته‌اند.
پرزیدنت ترامپ گفت: «آن‌ها تلاش کردند رادارهایشان را بازسازی کنند، چون نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و بعد آن را هدف قرار دادیم.»
رئیس‌جمهور گفت اگر ایران پاسخ دهد، «ضربات بسیار سخت‌تری خواهند خورد... اگر کار به بار سوم برسد، آن‌ها به‌عنوان یک کشور کاملاً نابود خواهند شد.»
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78156" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78155">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رسانه‌های وابسته به سپاه از آغاز حملات موشکی و پهپادی ایران به مواضع آمریکا خبر دادند
خبرگزاری فارس، وابسته به سپاه پاسداران، شامگاه سه‌شنبه ۱۰ شهریور به نقل از مشاهدات میدانی خبرنگاران خود از شلیک موشک‌ها و پهپادهای جمهوری اسلامی به سوی مواضع آمریکا خبر داد.
همزمان، خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت «عملیات قاطع نیروهای مسلح ایران» در پاسخ به حملات آمریکا آغاز شده و «پایگاه‌ها و منافع آمریکا در منطقه زیر ضرب موشک‌ها و پهپادهای ایران قرار می‌گیرند».
تاکنون مقام‌های آمریکایی درباره این حملات جمهوری اسلامی اظهار نظر نکرده‌اند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78155" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYhb5UY7tHgt0jaeWwQhWPS3ZlK0ERCK8wBsUT-XA418wIYgy2PBmS-U5zbPCzNGoq3qmpWP5FNZuoukXDs-bW57CzLgF8lh5xugxwsvgD6_CJPYM1ZP6O3EwTRc9LwOlyz3fQPwXdqHF-ELgL7L9-jGwcQIJeIoKbWd74HAHL1Rk-jj1G3RbtUYBaVxFCN0KyeAFiQ87lpIN5dl4bpOY9OIzo2oioCe7OlBlcu0ZMIFN_5SIFY2wSpmXyj2E1vNp02XrbqHkenpTYKf7tUXVgAqoE9F5s52SUo4hrkwXcf0-c-dp-8U328FD1Zf19AhQPv9YjUW0RKX25YkrX-9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با تری ینگست، خبرنگار فاکس‌نیوز و در پی آخرین حملات آمریکا به مواضع جمهوری اسلامی، هشداری صریح خطاب به تهران صادر کرد.
ترامپ با اشاره به پاسخ احتمالی ایران گفت: «اگر دست به تلافی بزنند، بسیار سخت‌تر هدف قرار خواهند گرفت؛ و اگر دوباره چنین کاری کنند، دیگر وجود خارجی نخواهند داشت.» او با انتقاد شدید از اقدامات تهران افزود: «آن‌ها دست برنمی‌دارند؛ رفتاری دیوانه‌وار و احمقانه دارند.»
رئیس‌جمهوری آمریکا در ادامه به جزئیات حملات اخیر اشاره کرد و گفت: «آن‌ها سعی داشتند رادارهای خود را بازسازی کنند چون هیچ دیدی نداشتند؛ ما صبر کردیم تا ساخت آن تقریبا تمام شود و سپس آن را زدیم.»
ترامپ همچنین با ابراز بی‌اعتمادی کامل به مسیر دیپلماسی با حکومت ایران تاکید کرد: «معتقدم توافق با آن‌ها حتی به اندازه کاغذی که روی آن نوشته می‌شود هم ارزش ندارد. ما شانس‌های زیادی به آن‌ها دادیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78154" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صداوسیما: فرودگاه جیرفت هدف حمله آمریکا قرار گرفت
خبرگزاری صداوسیمای جمهوری اسلامی شامگاه سه‌شنبه ۱۰ شهریور گزارش داد دقایقی پیش فرودگاه غیرنظامی جیرفت هدف حمله آمریکا قرار گرفته است.
این رسانه افزود اطلاعات تکمیلی درباره این حمله منتشر خواهد شد.
@
VahidOnLive
اسکندر پاسالار، فرماندار عسلویه، به خبرگزاری فارس، وابسته به سپاه پاسداران، گفت: «حوالی ساعت ۲۰:۱۰ شامگاه سه‌شنبه، صدای یک انفجار در شهرستان عسلویه گزارش شده است.»
فرماندار عسلویه گفت که از خسارات جانی و مالی این انفجار جزئیاتی مخابره نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78153" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78152" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c7f913a5d.mp4?token=dIobFy7_NylFunWJPdSyJpMH2PC8IGfFkYsxAyALkH10X6BVYmUZeqCslHKx60F1gVWkibH7cGvPb52DENW5GjNNDGrb_ilpC5c_nvFswLIQVeJoT0N2rGBeKtmoKVx2w8_elwLNdSx8MrLA30HmfseVDm11YNyVhXpomMMAWLafhaw7Kj68ujPte80Dm3tVSTzzMy7ab7ZKx2VW_IH95oxCt4eUIN_kMqYOu6y5r9NL1U_2POfgCFiF8juHWvlxLDgcdsdhnRmYHOFuGDICRZlKO_LrLDQRmecplvqyghAe9RUzBSql2MP6B4jaHNDymSvjeJlbxQrB7rZa3zhctw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c7f913a5d.mp4?token=dIobFy7_NylFunWJPdSyJpMH2PC8IGfFkYsxAyALkH10X6BVYmUZeqCslHKx60F1gVWkibH7cGvPb52DENW5GjNNDGrb_ilpC5c_nvFswLIQVeJoT0N2rGBeKtmoKVx2w8_elwLNdSx8MrLA30HmfseVDm11YNyVhXpomMMAWLafhaw7Kj68ujPte80Dm3tVSTzzMy7ab7ZKx2VW_IH95oxCt4eUIN_kMqYOu6y5r9NL1U_2POfgCFiF8juHWvlxLDgcdsdhnRmYHOFuGDICRZlKO_LrLDQRmecplvqyghAe9RUzBSql2MP6B4jaHNDymSvjeJlbxQrB7rZa3zhctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های زیادی دریافت کردم که نوشتند حدود ساعت ۲۱:۲۵ از
#خمین
موشک شلیک شده ولی پرتاب موفق نبوده و برگشته.
ویدیوهای دریافتی: سه‌شنبه ۱۰ شهریور
Vahid
آپدیت:
منابع جمهوری اسلامی بعدا این ویدیوهای دریافتی رو با شرح هدف قرار گرفتن پهپاد آمریکایی منتشر کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/78150" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام‌های دریافتی:
صدا ۹:۰۵ بندرعباس
وحید بندرو دوباره زدن همین الان
صدای انفجار بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/78149" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ip9J9qe6RnHFHl3LRU1TE-Y0B0rcgXfK9zY0vvIEOkwvMPzxOShgJ838fqxOuqSDsDJ5K6Y0KcGRNqC6h58MLqVmMcpIOXDtEUlbfrld5F01j87vTGkPxXs6a0KI9GuAfah3Co0Z5tX899moG-redIyTAtBr0jW-BQl0mc2-ffDcD9csUY1ryfeePa_9HFRW3825UWiYrBSwh8fjgs0sdb1bTbFipsnOHZjvHaO6G9n4hkaqQl850YcWU1cEMQWi-5yMU__mhMrqHaD-LcaVltzdJ_Ntf49GSeMsJ6alRWHUnk5FN2QPV1nRIN6KyDvGjMEMXH0dQBziqnGFRN-meg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر ایران پاسخ دهد، حملات آمریکا شدیدتر و گسترده‌تر خواهد شد
ترجمه ماشین:
ایالات متحده همین حالا، در حالی که صحبت می‌کنیم، در حال حمله به اهدافی ایرانی در نزدیکی تنگه هرمز است.
این حملات گسترده و قدرتمند هستند و در تلافی تلاش نافرجام ایرانی‌ها برای افزودن مین‌های دریایی به تنگه انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (همه آن‌ها به‌طور کامل جمع‌آوری یا منفجر شده‌اند!)، و همچنین در تلافی شلیک هشت موشک از سوی ایرانی‌ها به پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه دست به تلافی بزند، بار دیگر و در سطحی بسیار شدیدتر و بالاتر مورد حمله قرار خواهد گرفت؛ اما آن هم بزرگ‌ترین حمله از همه نخواهد بود. آن حمله هنوز در انتظار است و وقتی به پایان برسد، چیز بسیار کمی از جمهوری اسلامی ایران باقی خواهد ماند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78148" target="_blank">📅 21:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78147">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام‌های دریافتی:
سلام صدای چند انفجار اومد بندرعباس ۸٫۵۰
۸:۵۲ قشم یه انفجار حس شد
بندرعباس صدای 2 انفجار دیگه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78147" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_kVcGjOkNQeGVAsloYwm53_B4VMWcIRVzWaL3JEQjWsIa_4adeybdO5NH3JWae2Q8aqvfJeSbJ97S6WL-PsUy5wBazS6e4FkEyGxz3Kj2_lLDS-Lc-zILW9PhELXrqArUYr-Pb4vR-gkFG6kHaCHw8VKxzzD9ORIkNFppLqv_fG4CSCHTX5XaI7MrlbgkjFsfc1yvqJsGqj_3Ge-v0_L9zbKbkLFyVFd3mxYX1bwHTqNMAZbPVWqnZo3TpCiM5GdAXHqSQ0slrLxbFRnHWSktRMoQ39oQgf1WKs4R4S9bE3IatQ4R1F6mOiTDxB7Q6mgQMScKheyLJ13IR5xigknw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۱۰ شهریور، در پی شروع دور جدید حملات ارتش آمریکا به مواضع نظامی در ایران، خبرگزاری آکسیوس این اقدام را صحه‌ای بر گزارش خود مبنی بر طرح آمریکا برای حملات مداوم و دوره‌ای به مواضعی در شهرهای حاشیه تنگه هرمز دانست.
پایگاه خبری آکسیوس به نقل از مقامات آمریکایی گزارش داد که دونالد ترامپ و مقامات ارشد دولت او در حال بررسی طرح‌هایی برای انجام حملات محدود در تنگه هرمز و مناطق اطراف آن هستند. هدف اصلی این حملات، جلوگیری از بازسازی سامانه‌های راداری، پدافند هوایی و توانمندی‌های موشکی ایران اعلام شده است.
به گفته آکسیوس این طرح که توسط فرماندهی مرکزی آمریکا (سنتکام) تدوین شده و مورد حمایت پیت هگست، وزیر جنگ قرار گرفته، به دنبال مهار تلاش‌های تازه ایران برای تهدید شناورها و نفت‌کش‌هاست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78146" target="_blank">📅 20:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pyF5O-4hTmRu7_n8BMb2_qL0Y-y-0cIdxPDLtSaIXQgSJJ8LbSSc6_YZOH_mhSVfEMO7teGi6Y2QLPdgTDbWHjCwgQauALwWJLCbXWRMmWILddcXsvlwPDiaUCtTnBwErtkWnLKSzt0ViRDLgK_Z1ZCI9Ym2FfOjbDV8yY9EXRue-R4Z_NiBTiUJNJJpBNVGg_S4XsgtdNWC6nZq36VnQhu2z_DaVUgB0NAIT8FeHrhmOpctpgITIotnHtfsAgOVGjiqHAeCWduIazyPaDsIMvmp6wc_SRmxqAj2NwbrDKFDOBqAWRSLRiBfOrDnS1i6XeyxhQgScpHOFGPxYCsJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سنتکام در این لحظه منتشر شد. چیزی که پیش‌تر در منابع دیگر پخش شد درست نیست:
امروز ساعت ۱۲ ظهر به وقت شرق آمریکا [ساعت ۱۹:۳۰ به وقت تهران]، نیروهای ایالات متحده حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران را آغاز کردند.
این حملات پس از تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و نیروهای نظامی آمریکایی مستقر در منطقه انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78145" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/goS6VGNpUCwnkZHfhJ4iEhOidw71G4kFtbYhVm_oUHTiAOhBEj6e6wy--TmgUw2hbwa3lHThfhDEf1acxz_N1UhIo4lbpP9odXT9l7cTEgVOkU7vFZyuXM2EuyG8ac3cYZXD8m3McyPuGlSo0ySVn_QFtcuvE433ZK6DAKTCkomteG7KdjZ_CgFz0NL_xrO1k8hKXrLgcF1R1-tAPV1jVLS4f4yzwIuEUXZe7UC1RhrQ5WsjUFVYUsTH45UzdsOIjkzl_S0J6YnMylBgjfr7l6wErYQ1q3VCyjzsQPcMG37qs14tMRj9CllU14xRDbn16yLGg9UzkVrb2xVN5amknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیمای جمهوری اسلامی از شنیده شدن صدای چند انفجار در قشم در شامگاه سه‌شنبه خبر داد و نوشت: «دقایقی قبل صدای بیش از ۵ انفجار اطراف روستای مسن قشم شنیده شد.»
این خبرگزاری نوشت: «دقایقی پیش، صدای ۴ انفجار هم از سمت تنگه هرمز در قشم شنیده شد.»
رسانه‌های ایران از شنیده شدن صدای انفجار در بندرعباس، سیریک و چابهار نیز خبر داده‌اند.
معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، می‌گوید تاکنون هیچ‌گونه اصابت یا حادثه‌ای در هرمزگان گزارش نشده است.
@
VahidOOnLine
علی خلیل‌آبادی، معاون امنیتی و انتظامی استاندار سیستان و بلوچستان، در گفت‌وگو با خبرگزاری دولتی ایرنا از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/78144" target="_blank">📅 20:04 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
