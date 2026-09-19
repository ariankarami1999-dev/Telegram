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
<img src="https://cdn5.telesco.pe/file/eRSeeeySrNGfWjrabe7o3KWU7ceNymieZ__s1q_MOjfO42DGhv6rqap40I4-myINheI013Le5g0HGYxVXBPC-9Qb14N0InbWd_HWgOqqbYVIszmJXkX-E4rQX2Ge7-hrNTzO4BGJklD8c3BDBS8RQh45b8BhH4j1KHeW4s08DSt3pq09w03rkcd7HLct2eoI3b0bOGk4bQEUvgxfVsthWExpvO7kb7-JDWE84uzHvPD3wy7VU2Y0zMe_CJcPEWkx-LXo765A4ZsTforpfSVV9MA3KAGZvVVrsUKD6p-G7T9yqyTRbP67iOmSfYe6dVm-i5xWfdA_dEpr4HzcKDJlCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 408K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 21:48:15</div>
<hr>

<div class="tg-post" id="msg-106895">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gheOMi9XghpkbWQjKmEYjNDBD5tTIFpu0qRjETk9kzpn7iwBFtyw_kXTaDq9zF9rK49OvtubZUDabXA9ZlIZuC02fGfXj6DzujfdW3ykigURTSpFGvxL5L82u0iaNKxTwW2D8TmzFgrIumrq0HXFWXZm869-eGtVHPEsaHi0l0BSDH0rsj1XiQhehTY1LTc8tLubt8Vm1kVEKjZFK-nUryEo8I69_CoiywAFn1eJaOntdSwrZjficImw52jUaCMXPSNY0flYhClvgpYYFmbaWplUQEomN6g3zpns3nyU2kc99q5T4AkXSAu9gk8b5Bx9_HXvAlirY-s8pOSOzYxhTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست اتلتیکومادرید مقابل رئال‌مادرید با حضور خولیان آلوارز و غیبت سورلوث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/106895" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106894">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=ascoG8c-PqCahUVNiJiGt3o60GKTqfGP39nPGQsZyB0qwo6L_CL6dAppcyQPr4KUbKUGoZ_pDxPkOTKvc5VhMPJGDNhOZLfMGSVBslbAtbk91vYrzvdh7WKrsEIAfsQRynccl-UPhgJRJS0DxyNBi4pQw28LJZ4vOv-xx3--EVq1BAZ-KebgbOQ7Uxwd4QgFYsXe2rF1hiQr0E2jq6xewYjm_xe_Jq3QCuEwxHSWCPsgzHFDBVah7J4n7MPI1Ys0s4NmMUneYTTxBpB7AI-7camygNzc0-Ufl7enykHu152BIEYbf000_TRNUszHqP-N9kpWXl4ctfXqtlM7yYiTi35nFQZ6Bp-i8-bI0XdufAYpGxNqfDIrYATY4YJzDa-78-pW7p6sFRama06ltOLWIgNP4cNtj20uYVFTDqW8zR41K75_XxTAxkRGm_KESdK0hRjWThYVwEGPOZJaNpWJWf5ilhrc2K4aOdOe9_R0PKkOSD2lnnfKr_JfkUqxbEsZy5kXH1K5RDktDD7f1qftYnUEATlrKxZxx3qpXVaVttiCvnkEz1X1zqI1BUjvkf4U3OQRd2rQLnn54WA6We_lyDWE8gva9X3RglN98WZTZQnmUswU_oLk_USeAUguzlcrW8RM-o0f-W7V5GDhp03YUXOPebJkparBIvpIRSYlfJE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9f110d93f.mp4?token=ascoG8c-PqCahUVNiJiGt3o60GKTqfGP39nPGQsZyB0qwo6L_CL6dAppcyQPr4KUbKUGoZ_pDxPkOTKvc5VhMPJGDNhOZLfMGSVBslbAtbk91vYrzvdh7WKrsEIAfsQRynccl-UPhgJRJS0DxyNBi4pQw28LJZ4vOv-xx3--EVq1BAZ-KebgbOQ7Uxwd4QgFYsXe2rF1hiQr0E2jq6xewYjm_xe_Jq3QCuEwxHSWCPsgzHFDBVah7J4n7MPI1Ys0s4NmMUneYTTxBpB7AI-7camygNzc0-Ufl7enykHu152BIEYbf000_TRNUszHqP-N9kpWXl4ctfXqtlM7yYiTi35nFQZ6Bp-i8-bI0XdufAYpGxNqfDIrYATY4YJzDa-78-pW7p6sFRama06ltOLWIgNP4cNtj20uYVFTDqW8zR41K75_XxTAxkRGm_KESdK0hRjWThYVwEGPOZJaNpWJWf5ilhrc2K4aOdOe9_R0PKkOSD2lnnfKr_JfkUqxbEsZy5kXH1K5RDktDD7f1qftYnUEATlrKxZxx3qpXVaVttiCvnkEz1X1zqI1BUjvkf4U3OQRd2rQLnn54WA6We_lyDWE8gva9X3RglN98WZTZQnmUswU_oLk_USeAUguzlcrW8RM-o0f-W7V5GDhp03YUXOPebJkparBIvpIRSYlfJE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
نبرد اینتر و رم با تساوی دو بر دو خاتمه یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/106894" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106893">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=G0obT-ZYSUXI105g7d_hhfmSXc3mOT_CPosHeraUYRRpbbLFpjhymJ10EFAGH8QokSwd4rT2LHr6cp98RBx8NE8StpvRotjJ5vjxkBG-oBzCWRbrfxwFKc615Z1J2UyNn5mf8M5mqub84RJSkqvl2v4J3QkjetW2uF7sQWsI197or4PlVUb5WRFk_YP6XE8N1hW2acq6PfWcJVXzYYSAFphlDNsBFAy-UcDyNnu3tEEmYe-37Fr7TKXxIONciGnsHAiUETzFOhn-pMImJAtPpUdPNRNMvpgl8Gc47vFjSlebM44UZ59Fg0hC9ph1okO7rG3bkLFQXnpR5DWB454bUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c80348f50.mp4?token=G0obT-ZYSUXI105g7d_hhfmSXc3mOT_CPosHeraUYRRpbbLFpjhymJ10EFAGH8QokSwd4rT2LHr6cp98RBx8NE8StpvRotjJ5vjxkBG-oBzCWRbrfxwFKc615Z1J2UyNn5mf8M5mqub84RJSkqvl2v4J3QkjetW2uF7sQWsI197or4PlVUb5WRFk_YP6XE8N1hW2acq6PfWcJVXzYYSAFphlDNsBFAy-UcDyNnu3tEEmYe-37Fr7TKXxIONciGnsHAiUETzFOhn-pMImJAtPpUdPNRNMvpgl8Gc47vFjSlebM44UZ59Fg0hC9ph1okO7rG3bkLFQXnpR5DWB454bUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇹🇷
🇹🇷
دبل محمد صلاح در بازی با گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/Futball180TV/106893" target="_blank">📅 21:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106892">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otG_JQIKR0z3YzyhuHRZoiuVszbKDzMao5ieRBtiGJnATxT7A2niKbkg2YNnmLQa5-jQZbpyia1y-4L8HRCKCr72Yv4UeAc5AllnHblmEJyd-Y3hH0ZiPZ2i652NJI2gxHWdHRMwX5j4Y73SMwH2zPHmrOjPab_q_sMaCq9EzGql7fnOsqOdeofHKduYJX0y39L5DTGw2uXXg2S6-bNpHbO7Cjezd0jerch_zLK3zc_IiTCof8536SpDrgDMc3EhM-pgEN6kc7TrOhUXVZGdCGVkx62FnOpAfutRnvjmPfi8nbtToIFkbsTu_A6023wXOngm8bSBkZOC5Jn_0AMdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
شماتیک ترکیب بارسلونا مقابل سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/106892" target="_blank">📅 21:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106891">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d419048b91.mp4?token=du-mIYskChyWehxF9-mU1OfraLzcITw5MElDHu8QZXttJFhwmFHXmbXCXPlm76USrgQraSUULjzbHG0-FeKi2TH3KGQ87Y7LFSTazMGMOXZ_He8t-EL8HmSv6rjyJ_JopV1ZoBEQrOG1SibsMe6-oLCXbXXkEBjHnndAhdipA7IO0eF74GCWAIzdcm3-MHU4P-JgbHbsh-nlvjlWCbsVofp-Qzty1M0xQ4UJeyC7DcUmVDZxUVAd2jj1Vy7FaWpUvA21LvhfwtzRyBjrC37hqlHD0by-Cz8KYbIStyVjI20P9u9vtqs36fW1lrmtUboJKZDr02ZKl3XVXmp-rcrkUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d419048b91.mp4?token=du-mIYskChyWehxF9-mU1OfraLzcITw5MElDHu8QZXttJFhwmFHXmbXCXPlm76USrgQraSUULjzbHG0-FeKi2TH3KGQ87Y7LFSTazMGMOXZ_He8t-EL8HmSv6rjyJ_JopV1ZoBEQrOG1SibsMe6-oLCXbXXkEBjHnndAhdipA7IO0eF74GCWAIzdcm3-MHU4P-JgbHbsh-nlvjlWCbsVofp-Qzty1M0xQ4UJeyC7DcUmVDZxUVAd2jj1Vy7FaWpUvA21LvhfwtzRyBjrC37hqlHD0by-Cz8KYbIStyVjI20P9u9vtqs36fW1lrmtUboJKZDr02ZKl3XVXmp-rcrkUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
گلزنی محمد صلاح مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/106891" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106890">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=WZ4XmxY3NopF8HYEFociujC2H9zj-27uD-ZJkqdyVMzEvjFKBEkx_XjyPFtzdeDngdom8WsD6YEbmJE3j3jxFvVglRI13rwtoh7gNTR6h9bTCZsoSUPihsNAyjuR6CPGyDdaBTqzUD0emG4ODOrqpc8MyLk-gf5J9OPthycDy7Ydgd06hmfNXZRpvbVEJCX7h11hCcgM1-FDWTYKfaAjQMW2A4Q4lVq6e_JU3bb_MJBH4HaAizMZbWAD30w0Mq8aOuBNNhHca9gbWMrPOHvdnhQc7Fgw9eIOTszHXjac_b93aw1yzjx1SbAzvRNvu8lzT07DAd599NQGnPYHwyNnSFZfnMbbgsKhW3QgNFjmoVFcQebvfV2kr0ArGi2YHFcee__JJPXwDsg7nCZdyrgvHWf5C4-m6zRTMWMXAtOWYkmKzauTbdy4tTb5D_bShg6nx2RJ4kxe5LJCeUdXeO4foL04flYak-yLkBTGULCrFFkuPYibdecRyKsLZFCALEu70OigFLkYxrsxsg81BZzq2W_gIce6YqIShSc8B9KlLrmGM44R97aWc8Vj95Mj9kklU2mRs6OqFXHO4VP2PFI7PUUdRzi0GX9OU5rZWP01R4EIjL7oNn06A5-Bki2KVikPTsrxo5r8H_dbaF12ERBeteIMb4UmzhEqvpoIrW_tWp4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c0314b4edd.mp4?token=WZ4XmxY3NopF8HYEFociujC2H9zj-27uD-ZJkqdyVMzEvjFKBEkx_XjyPFtzdeDngdom8WsD6YEbmJE3j3jxFvVglRI13rwtoh7gNTR6h9bTCZsoSUPihsNAyjuR6CPGyDdaBTqzUD0emG4ODOrqpc8MyLk-gf5J9OPthycDy7Ydgd06hmfNXZRpvbVEJCX7h11hCcgM1-FDWTYKfaAjQMW2A4Q4lVq6e_JU3bb_MJBH4HaAizMZbWAD30w0Mq8aOuBNNhHca9gbWMrPOHvdnhQc7Fgw9eIOTszHXjac_b93aw1yzjx1SbAzvRNvu8lzT07DAd599NQGnPYHwyNnSFZfnMbbgsKhW3QgNFjmoVFcQebvfV2kr0ArGi2YHFcee__JJPXwDsg7nCZdyrgvHWf5C4-m6zRTMWMXAtOWYkmKzauTbdy4tTb5D_bShg6nx2RJ4kxe5LJCeUdXeO4foL04flYak-yLkBTGULCrFFkuPYibdecRyKsLZFCALEu70OigFLkYxrsxsg81BZzq2W_gIce6YqIShSc8B9KlLrmGM44R97aWc8Vj95Mj9kklU2mRs6OqFXHO4VP2PFI7PUUdRzi0GX9OU5rZWP01R4EIjL7oNn06A5-Bki2KVikPTsrxo5r8H_dbaF12ERBeteIMb4UmzhEqvpoIrW_tWp4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇹
گل‌اول اینتر به رم توسط لائوتارو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/106890" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106889">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/102cd70646.mp4?token=UFNK658DMZEnI3pe8UFKlIhguPIpiCeJNqVDKemE1jk9jvNaYx6Eln4tIc9XaGaINWODczuUHjTPzsilCsNfnSAOQZ3TBJ9Iz7m97XQaR4ofBFMBBG2sVoojCu-CnCsONeiXPCRPHC3bKYa0YrlQ2J_2z7mKrxhl85ii9zb6PxGI9njU5nwaWtDOkGizc0WXHPi7kat2-ctRpfVF5vk2dby03PHtEPVnt4MCn1zLvfauqW-2CAQi84TaBMmNRrIQcgStjGSeNx6YVBHbY_OpKI66fW4KODPZZdY7-_IWysnh4T8w_duy0LMuNNt1XGLnQwjt-7esnBcXDCYYqQD7vA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/102cd70646.mp4?token=UFNK658DMZEnI3pe8UFKlIhguPIpiCeJNqVDKemE1jk9jvNaYx6Eln4tIc9XaGaINWODczuUHjTPzsilCsNfnSAOQZ3TBJ9Iz7m97XQaR4ofBFMBBG2sVoojCu-CnCsONeiXPCRPHC3bKYa0YrlQ2J_2z7mKrxhl85ii9zb6PxGI9njU5nwaWtDOkGizc0WXHPi7kat2-ctRpfVF5vk2dby03PHtEPVnt4MCn1zLvfauqW-2CAQi84TaBMmNRrIQcgStjGSeNx6YVBHbY_OpKI66fW4KODPZZdY7-_IWysnh4T8w_duy0LMuNNt1XGLnQwjt-7esnBcXDCYYqQD7vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/Futball180TV/106889" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106888">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=V7g-VbFPqjQ_TEqm0CBsmeK_cLGgm5M8VwSBYAr819dIhu7KPfUvcg7UNLV4xCKS7Q2nAiDwc36XGjfCuywatgTG7JRM_Bm3Nh-0xUGL7qc8zvZKQjoAMX71oEOf1m09n2hyUcAhdSgsEgH2jqqiQXxUtnZb9hXG5-qHAKoJDuri47ml1Keaem88iNQsZ9vMjecmEY2qcmGJqzj6IVN278KNvHxDBgK0rHwsEAlkTzJJp7-Gl119cxoSGYBjhxvk_ZPje07RehXJr5lVpmhP_-lDruotmi_3V5LuMBt55hRucH5fWJXw1Yf3uRaM_D9mrMGnt1wZr85nImglmOYNioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ac971c9b.mp4?token=V7g-VbFPqjQ_TEqm0CBsmeK_cLGgm5M8VwSBYAr819dIhu7KPfUvcg7UNLV4xCKS7Q2nAiDwc36XGjfCuywatgTG7JRM_Bm3Nh-0xUGL7qc8zvZKQjoAMX71oEOf1m09n2hyUcAhdSgsEgH2jqqiQXxUtnZb9hXG5-qHAKoJDuri47ml1Keaem88iNQsZ9vMjecmEY2qcmGJqzj6IVN278KNvHxDBgK0rHwsEAlkTzJJp7-Gl119cxoSGYBjhxvk_ZPje07RehXJr5lVpmhP_-lDruotmi_3V5LuMBt55hRucH5fWJXw1Yf3uRaM_D9mrMGnt1wZr85nImglmOYNioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
⭕️
آخرین وضعیت سربازی بیرانوند از زبان مدیرعامل فجرسپاسی: معافیت بیرانوند تا پایان آذرماه است و این بازیکن در تراکتور می‌ماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/Futball180TV/106888" target="_blank">📅 20:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106887">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=qwyBd4VVRzLNRvsMD9z48ll-UR4dZUKx1p4CafgvbeIjqGXBFatDQwxegDgK8uK8xwM8CQePtwcs9n1vLatt3ejbeyPwtn7dAJFSb4LDDFN3rWvGg_sRqvr5Pa7ktsGaVQ91CA0cYEVzAcZYJ-07jsyGyRWTBgSJiSoASi8jHA37eMr_QlDvR2C1AJKRj4jm67wEASOzN_xGG91iSR8xVqO07g3ajrBCxZ_nj7OnEd9m6gqSdcdIOH7AV73URf7rYIDJWKrCpYdPQCDFCmO2nqJ12JUyBc-S8vrX6ww1Xvxy7sjbGQc-__-tCmEeBEmpU92mLp6KKw6k68__Bu_BNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76f9243a61.mp4?token=qwyBd4VVRzLNRvsMD9z48ll-UR4dZUKx1p4CafgvbeIjqGXBFatDQwxegDgK8uK8xwM8CQePtwcs9n1vLatt3ejbeyPwtn7dAJFSb4LDDFN3rWvGg_sRqvr5Pa7ktsGaVQ91CA0cYEVzAcZYJ-07jsyGyRWTBgSJiSoASi8jHA37eMr_QlDvR2C1AJKRj4jm67wEASOzN_xGG91iSR8xVqO07g3ajrBCxZ_nj7OnEd9m6gqSdcdIOH7AV73URf7rYIDJWKrCpYdPQCDFCmO2nqJ12JUyBc-S8vrX6ww1Xvxy7sjbGQc-__-tCmEeBEmpU92mLp6KKw6k68__Bu_BNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
انتقاد کاویانپور پیشکسوت پرسپولیس از کامنت‌ پرسپولیسی‌ها در پیج السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/Futball180TV/106887" target="_blank">📅 20:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106886">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzLSCkUPUOCvzQuI1J5zAvKAOSzBr5PduBJEQ4v_ACmMCwHRrYrW9k_ZYq9860QRIVvu-YaimdYVpnafZtdFtWi18N3KiXJQalVJBLlZDKZv0nVsgIQhZ0sWfYhDoA-6FhGA5ke-jMgEfvqPVu_kBGbc0pzTFO_sMXXkriEfH8BoKXGlCPffUEqEQ679yUA4pEZu6dTBpQBdCJW8T37PZtc5wRscvysHD0XO1rnMvB-NbdAXH85o3PHGkNHlo_gvdTqVtulFIe8iRUSQB8Qs9SYKEBXf5L4o3RerS-eilS03vsryqYQP5ieKQcQXdO2hT2_FoVrDqVpkaxz5bpfkSGXI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6d65328b4.mp4?token=ntnOPOySJ6nbLvc-zt_Xx4LkHvb22OwWiJT4DTd-s8HZ8q4TidKBS-ga9GyYN54P1UqmhnBXGGridhn8xKWghdUwpOSUSgDtyO9JM6ohsYb2oz6E8yLEXN0CxhlpqCnn4D7slZytE5yhI6xtRaBPq0MqvzrZjoUBWR59AnmpIxEEpZ0_er6WwkFQPwYRPqb82aDG-YYkApw5b_Gf73S3u8MlClefwQMWcq54AcZjmMIbH8bdh0rrehze666iOPeaTYjeaIE8FRTUpyBaQC__1_USe9fGWXPhy5LqWci4P1Fahbgf_w-cx5MKLdtOKb81Wh3NAb-sSt26zh_l8k6RzLSCkUPUOCvzQuI1J5zAvKAOSzBr5PduBJEQ4v_ACmMCwHRrYrW9k_ZYq9860QRIVvu-YaimdYVpnafZtdFtWi18N3KiXJQalVJBLlZDKZv0nVsgIQhZ0sWfYhDoA-6FhGA5ke-jMgEfvqPVu_kBGbc0pzTFO_sMXXkriEfH8BoKXGlCPffUEqEQ679yUA4pEZu6dTBpQBdCJW8T37PZtc5wRscvysHD0XO1rnMvB-NbdAXH85o3PHGkNHlo_gvdTqVtulFIe8iRUSQB8Qs9SYKEBXf5L4o3RerS-eilS03vsryqYQP5ieKQcQXdO2hT2_FoVrDqVpkaxz5bpfkSGXI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
گل‌اول آاس‌رم به اینتر توسط مانو کونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/106886" target="_blank">📅 19:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106885">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947613cda4.mp4?token=gxKdZq1BF2J0U6l7j2MJzj2soGp06snFlxE_PEGSucffrhHX9uOe2CuMM6d5JHTfzuAt4fHZsIpcYZnq3pO7WOQ0Rtwkd11neU9BjNLfCymccVQCAJQIHHFNz9ntvbfenSXTSXZ4YThgNlmdwKSWmEObU1KSP3Rv1xPnhs3aQfsUVyxVpYEaZv5MYI5y1Fy4F3bGjuHjH_bZHsGNY-czTPNE0GlCJAXXDFgElsHLcyodj53nJmhkABC9-00C-ETddrkF0reWyF8LTfkrx_Mh3e9Hvd8LcoyvWJzHifDmwJZwyYiVklI0NiIo8RXlnyXqKmzo5rcYd6dFFH47iVHT5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947613cda4.mp4?token=gxKdZq1BF2J0U6l7j2MJzj2soGp06snFlxE_PEGSucffrhHX9uOe2CuMM6d5JHTfzuAt4fHZsIpcYZnq3pO7WOQ0Rtwkd11neU9BjNLfCymccVQCAJQIHHFNz9ntvbfenSXTSXZ4YThgNlmdwKSWmEObU1KSP3Rv1xPnhs3aQfsUVyxVpYEaZv5MYI5y1Fy4F3bGjuHjH_bZHsGNY-czTPNE0GlCJAXXDFgElsHLcyodj53nJmhkABC9-00C-ETddrkF0reWyF8LTfkrx_Mh3e9Hvd8LcoyvWJzHifDmwJZwyYiVklI0NiIo8RXlnyXqKmzo5rcYd6dFFH47iVHT5zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
خواجوی گلر پرسپولیس: الگویم نویر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/106885" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106884">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=DgIvbhrLafWsHGnxq2tqK6gKQBlmMPW_i05AjIAIZ781KkKp8hw2pnZXy1llT7rPjMTw7JohdQouQI4NNQ4oHtYUBPFUYrk-lDlEPuTzURSF3dC0NMKpJB7oWhlCN1AwfYDmVK6FNBZuVTSe3HTNzUadv-6FExE4seKsOlu-HB9nseGYHUSVdYp7uA-Q7RW2xljcdIEEOiUFiFGws0Kfd-4uO-_DqfxeL0wkeqhl4uhEyETphITtvL5wHIG7wTpMahcYiUlA6F8ZTusJ-6a6wwc06T4d_dYTTYDoFdLC2dciPvQB_yZ3I8QceQrgvMrqu7wXV3ZoKhYNzN14fyAxWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=DgIvbhrLafWsHGnxq2tqK6gKQBlmMPW_i05AjIAIZ781KkKp8hw2pnZXy1llT7rPjMTw7JohdQouQI4NNQ4oHtYUBPFUYrk-lDlEPuTzURSF3dC0NMKpJB7oWhlCN1AwfYDmVK6FNBZuVTSe3HTNzUadv-6FExE4seKsOlu-HB9nseGYHUSVdYp7uA-Q7RW2xljcdIEEOiUFiFGws0Kfd-4uO-_DqfxeL0wkeqhl4uhEyETphITtvL5wHIG7wTpMahcYiUlA6F8ZTusJ-6a6wwc06T4d_dYTTYDoFdLC2dciPvQB_yZ3I8QceQrgvMrqu7wXV3ZoKhYNzN14fyAxWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های جنجالی یاشار سلطانی خبرنگار، درباره چرایی برهم خوردن توافق پایان جنگ از سوی نیروهای سپاه و جمهوری اسلامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/Futball180TV/106884" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106883">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ernpZntuzOA3X4jMjo03t-faV5YcnRh5dQ22Udx7F49YkcS9vKFaFm10QBqitRnVgeXBK9JJaI36swU8FQgL4vR0oPz6iexl9ovxUySrHQvYa5_r2V6E-EYn4jiD0Mw6_o5WcF2FI4wGawqx_BIcc3CYAVOfvWw91Z3S6cXcrn8W15YV1bsy3OR0EaLp001C38UnZlsTIjoN1PgYLhIitRjC8uXWEzaGfzy2gF23WPKySWQQW19vkK_XAYRUQXYdCtaWiKy3jsIOeajwqKqgCjtZ-M3yMsXI4SUvQS8nptbUyeXEw9ZZ84HCj-ncK1KolGtaTplWE_XNGMKfaLuHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهکار جدید کاربران برای تأمین نقدینگی به جای فروش طلا
🔹
با روند صعودی قیمت طلا، فروش دارایی برای رفع نیازهای کوتاه‌مدت نقدی توجیه اقتصادی خود را از دست داده است و حفظ طلا و استفاده از آن به عنوان وثیقه راهکار جایگزین بازار است.
🔹
وال‌گلد و بانک کارآفرین امکان دریافت وام تا سقف ۳۰۰ میلیون تومان را با پشتوانه‌ی طلای کاربران فراهم کرده‌اند. این تسهیلات کاملاً آنلاین، بدون ضامن و بدون چک از طریق اپلیکیشن وال‌گلد ارائه می‌شود.
برای دیدن شرایط وام کلیک کنید
برای دیدن شرایط وام کلیک کنید</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/Futball180TV/106883" target="_blank">📅 19:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106882">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da8b096322.mp4?token=B4Sef2LOb7gBbUXAkMFkb0s-M4cHSbRySlH382DOa3tETdbxEPI3kssCpPU6TSSG_8xlpA3YPEIZK2QucUbDoKpVQfKynd8pX8V8ivVqq71TsEF-NHutOSIFt-vTkjw_o6z3v_BbROPQYWPKohEw5Zh08ny1TZZpO_8rPBP-7-xmY8OsScAwyPT6nBYuzcddiwwybKsTvQNzoZp2QmtQC6hTkPclfAcnSGxLFqPpB2IaDyTDuCJeyKt0XnhMOfVWNbd7mVVcisdnt58juiyTIYALREURyEYwaHjeQ0bRuvgS-VrhbOyIqi5k5XMKw31gPC1zdh07hrcVtRAE_EVsFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da8b096322.mp4?token=B4Sef2LOb7gBbUXAkMFkb0s-M4cHSbRySlH382DOa3tETdbxEPI3kssCpPU6TSSG_8xlpA3YPEIZK2QucUbDoKpVQfKynd8pX8V8ivVqq71TsEF-NHutOSIFt-vTkjw_o6z3v_BbROPQYWPKohEw5Zh08ny1TZZpO_8rPBP-7-xmY8OsScAwyPT6nBYuzcddiwwybKsTvQNzoZp2QmtQC6hTkPclfAcnSGxLFqPpB2IaDyTDuCJeyKt0XnhMOfVWNbd7mVVcisdnt58juiyTIYALREURyEYwaHjeQ0bRuvgS-VrhbOyIqi5k5XMKw31gPC1zdh07hrcVtRAE_EVsFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌سوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/106882" target="_blank">📅 18:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106881">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA29D2CZK7CUnwbHG33gmjvQIvfKixf7jBGgHxGGhN9Emg6uUepO9RnHARwYHzjrQWHYu-hY9OJkH1_Pnh6GzXcyjdk7PAYucRV6O3dUt2sWLuvWuxyRFsY_t05YM0loL0CoR-mukeAO36tcZ2Ra35jcECjFZmg0WO34dNiNn10Bh7JJTXjFMAE8hXE5Lpmt1-scbO5eZifE6utS_hoWc7RLKtphg8H-HOJUntz3A0_H0MGOj91TK9qL3E99FpMaMhM0_DR5yeOo8qNeHmiENd0jf9nPgiEoq_wD0YxKTozJq-DLm8scBFhGIVSYu2r9fTeVBtTHeTY1Bm_U3MxcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اینتر مقابل رم؛ ساعت ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/106881" target="_blank">📅 18:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106880">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=Cg3YJKZYcbLXljyWSdRl_kkPKNWy2x8ObG70D1xRvj-lud2e6RpSLb2D3kD7TECBaUfwpcTA58IWa9NZ84WW-wuwp65Wx5IuE1JKbGcUGGKtpAK43gJru9THYYtaM9VT_Tgf8dR5UPfU1O9JFF-ewhpw6erveo5PpJPH5lZv9J2IlH7o7fjdJIpTG9owi5Pv_TCrWCd8TzKCi-X5YHBWf3cnBuh8BsjOPZ_9tc_Ha-2dVMWp_svsLB6xnwzy_wWl8QCJCuk4Era9DG3cC3ENmEAcmO6hf6X2h1DWlTXXASkDvKofwV-JBh-4TUWLds2bx1_0PGql6lbtB33WS1z1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9510f8cfbe.mp4?token=Cg3YJKZYcbLXljyWSdRl_kkPKNWy2x8ObG70D1xRvj-lud2e6RpSLb2D3kD7TECBaUfwpcTA58IWa9NZ84WW-wuwp65Wx5IuE1JKbGcUGGKtpAK43gJru9THYYtaM9VT_Tgf8dR5UPfU1O9JFF-ewhpw6erveo5PpJPH5lZv9J2IlH7o7fjdJIpTG9owi5Pv_TCrWCd8TzKCi-X5YHBWf3cnBuh8BsjOPZ_9tc_Ha-2dVMWp_svsLB6xnwzy_wWl8QCJCuk4Era9DG3cC3ENmEAcmO6hf6X2h1DWlTXXASkDvKofwV-JBh-4TUWLds2bx1_0PGql6lbtB33WS1z1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم برایتون به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/106880" target="_blank">📅 18:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106879">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گلگلگلگگلل آرسنال دومییییی خورد</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/106879" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106877">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3613208345.mp4?token=R8LpXSiaRmIlQxbuGlRlI44XGtk2XFkEzH_0XBEc1wuynwWKO6mUxBLTgLHmIbiQoejW1BkKkisi-3-u8LBFiL_2RNlFZ4ybJKHWABCH4EIpvrtinSJIMdIZD77w-xxmzuWbTEuKwyAwOMlwcq9Al58EdrIFwqI_FTNiKND_9z1NY98CRKxbs6ROPsk-v5o-cl-DySFw6fOvkYtskAYS2lbKW8popH5ixlAcqbsWLNphNJMmfiDz7VP4Jl3uwDuVtuYBWwTbeyJ66sFnOruiDiRd5Up_2gBs7zGkEJ9iwdp4lR29YJL14e4P8Cz5AwPE4eARuhdvp_OqbhKoAGtoGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3613208345.mp4?token=R8LpXSiaRmIlQxbuGlRlI44XGtk2XFkEzH_0XBEc1wuynwWKO6mUxBLTgLHmIbiQoejW1BkKkisi-3-u8LBFiL_2RNlFZ4ybJKHWABCH4EIpvrtinSJIMdIZD77w-xxmzuWbTEuKwyAwOMlwcq9Al58EdrIFwqI_FTNiKND_9z1NY98CRKxbs6ROPsk-v5o-cl-DySFw6fOvkYtskAYS2lbKW8popH5ixlAcqbsWLNphNJMmfiDz7VP4Jl3uwDuVtuYBWwTbeyJ66sFnOruiDiRd5Up_2gBs7zGkEJ9iwdp4lR29YJL14e4P8Cz5AwPE4eARuhdvp_OqbhKoAGtoGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل‌اول برایتون مقابل آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/106877" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106876">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ-vInd77-nmJGDM44vL5SasSR3_6W_6JHcF2UarmUNBV-9R6FAiGxjFiDRLmyahJtX_oZuRHZS5uLcnZdCrH4Sad1rGWukK3BJJ1DQwwueZm28QvFrLc23LmD2cRrkVJ18qDL6o8wWEow1xpT77C-Qd1Y2-o60ywM4vZBXpreTJY9K6KwA4nLj78RuZSwR3jB1Ej1CerqVoEff7TAmNYi8Wuvvp7vyklHsg5_ONx7WiEiVZoKy7fd0WXG5huPbfQgQMoL7hx8WecYjeMj6tOY_GONnL6G6qyQL_IWtmzgFP6iQxKHza4ySWHqPefcDKbpk9KclMmlIBIlHSqq_WKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/Futball180TV/106876" target="_blank">📅 18:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106875">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTNbwHE135VFlN-Dzuc4roA6qw7eM0Jh6yTpRbbwHxpYvzikhZCNCqCehdgIIq3faIP5oSjrr1cpymRPi0QEsW2uwruzQOQ-nPyzOIA9fnrFddC-jrrJp1zPCZIOjSLEGlRfAX44JRV07NAnMYcQI2Cc6_ZSgH2yVd1x4LeRt_rJmeCuMZ_TNmu6dqgmsnSJ0n3ErbxkG7vRl-FCpyDOj7hKRHdZbjMOswqOXmxA6hyRBaQjlwHXhIH2bCfZ1sfxbAGYpiF5cFRwfN3A-jiZpwqZtdKmWfd2obl6EUp1OGGihwUt6JzaP86cJsqxZbUp8AdsyzwJ4pXEcD4m9C2h7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دکو مدیرورزشی بارسلونا: تمدید قرارداد با رافینیا تا سال 2030 نهایی شده و بزودی اعلام رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/106875" target="_blank">📅 17:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106874">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=EBLmgFXnFrajBtEAUlUvnPDD-Kd579SkGY6U4icN608tc4dHa8kkgHHHyKkVg6_jKVCQdriKuz_raC4aGvgcgJU7Z_BPt_bx8A3nsLXzMCQPKdAGHZ36FgihX1cBQ8mAeI8byAQnijirtH8LfHitgYTaUCtPAfxhj07LeUqFrdeBiEkU7yi10ewiiAFmSykSDrZi77ReRKfyePRThOmequVByUN50F43YDVhlfK64GljKxC2z9kdlYlHei1W8tk6s5Eggumj87IbSRoo-ghDcOiKzXtzK5M1-yeiubJh8YaTchKJBJiJICHsQYtJ2FexCEgxQw19-6Gch-0piVWImE1NN26OK6xogY4aI1jfrP-sZjniICduuZJf5HM_vYxaJ-vn9JPUDIdxhiptH6_cGkjTyV1oByLzqzYKHaec390TXdTB-xTGYQT3cKRd2gEHBmeoFrLpTxzckAazO1qQ1v_OCfpxfINrFEJOd9oJdQPRS_QOXCA3djLXcj3plpluKyI9kEqxqwJXT-ShpJDuQvqDMOqjVxvZWePiypODOz0DTXqy4x0WzGwaNfVasKHBa0HZGooBTyV40DCGSe2pMFy_ZzCHRznWO9MWbQwUspXEgV-mK4l6lVE-AGHLKz5ECkaNeaEjA87sD8va8GdlkBLc8jmubCqiw4nBqT4KRqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc01f74867.mp4?token=EBLmgFXnFrajBtEAUlUvnPDD-Kd579SkGY6U4icN608tc4dHa8kkgHHHyKkVg6_jKVCQdriKuz_raC4aGvgcgJU7Z_BPt_bx8A3nsLXzMCQPKdAGHZ36FgihX1cBQ8mAeI8byAQnijirtH8LfHitgYTaUCtPAfxhj07LeUqFrdeBiEkU7yi10ewiiAFmSykSDrZi77ReRKfyePRThOmequVByUN50F43YDVhlfK64GljKxC2z9kdlYlHei1W8tk6s5Eggumj87IbSRoo-ghDcOiKzXtzK5M1-yeiubJh8YaTchKJBJiJICHsQYtJ2FexCEgxQw19-6Gch-0piVWImE1NN26OK6xogY4aI1jfrP-sZjniICduuZJf5HM_vYxaJ-vn9JPUDIdxhiptH6_cGkjTyV1oByLzqzYKHaec390TXdTB-xTGYQT3cKRd2gEHBmeoFrLpTxzckAazO1qQ1v_OCfpxfINrFEJOd9oJdQPRS_QOXCA3djLXcj3plpluKyI9kEqxqwJXT-ShpJDuQvqDMOqjVxvZWePiypODOz0DTXqy4x0WzGwaNfVasKHBa0HZGooBTyV40DCGSe2pMFy_ZzCHRznWO9MWbQwUspXEgV-mK4l6lVE-AGHLKz5ECkaNeaEjA87sD8va8GdlkBLc8jmubCqiw4nBqT4KRqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
‼️
🎙
ماجرای دست رد مهدوی کيا به قرارداد ۲‌.۵ میلیون دلاری!
🔻
مهدی مهدوی‌کیا: مدیر باشگاه داریان چین بعد از دوگل من به این تیم پیشنهاد قرارداد ۱.۵ میلیون دلاری را مطرح کرد اما بعد از جام جهانی به دلیل عملکرد، خوبم آقای عابدینی رقم رو به ۲.۵ میلیون دلار افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/106874" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106873">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106873" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/106873" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106872">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUolS0Mv22Sz64Kdi34UwZetWcmneG_ycamxq0V2UH1aq3Gn8gwM1t3SRvzn4S4kFYrhspCbadF7HHxcA82IWhJ8zVVXp4_cUlNJ-bZ2z-RAuMT_5mz5_TgxE1LRljyClhI-h8OQ-MvHSyr2u5Nsyz-15hddfs3LlVdbCaPN1wKuPWJ61ianh8lnmDqkhfD-ZPt7IWP5Q_1jZAnHPWSeMV50PzE4tv0OEpR849wIAmvNVkueotmMRpp_KVzj-2jkkw_M9hXTuZTV_OGf40kz2m2-lLrmjnonhKiOXMvKbCvIt4hbhoU8r7-4JrFzVr0Z5CmAZTp7bCdDvfhJydcWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
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
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/Futball180TV/106872" target="_blank">📅 17:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106871">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7ETsltDtERTkeJz5Kh0ChpZvOuOHM7qYqWvkCT2bAjN544SuvbaHZGdCEMmOCPn4AFyh8R7mHfneujFpB7RgeSyBGRJv5-KDv8nKCBoEG2hg-mcXQjcf9ZbjuE0wrWvhcIkaQt6MpVEAQpQMUz_vbuv0IY-3walNsqz11zk4jR_lxFQZh882nRP189s_VysHj4kkMcrxOD9Y6BbpGJZPOplfiE31ciFWjLCcSK8IpHx0BbcQaKdZtRPB-mf6o_LMKinKuRpPAUN7GxDD7XuBzmDMx70zW3HMm3hXLGTUz6CBx4m2mPHdbR1hHK6qyqMfpz2IQHr-GebmZmOicQNXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎤
ژوزه مورینیو در پاسخ به اینکه آیا از شرایط بارسلونا نگرانه :
🔻
از نظر تاریخی و فرهنگی، رئال مادرید قابل مقایسه با هیچ تیمی نیست؛ بنابراین من هم خودم را با هیچ تیمی مقایسه نمی‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/Futball180TV/106871" target="_blank">📅 17:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106870">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jB1NtDKvXYRsos5ZnCZLM1xpj57_DNUEaKgwqQvjiHfYrLEKTdmuj5p2bqI2t722zVuCAkVHzqVkNrlUmUpC1LoMRHB6Psd26FGJA71R8i1YRyilqqiDeVVAWU8GhXrQCWHu20TwmTETHUJDe_nly0ebTZkkKCar8-ywOSTw6tQmzcuOlLGng1KEKK8zbb-VvpimLQX4BDqT6Dzt7nnKyatYQ-N-fGzAWpxlXXvuxC1bTSfELB4FuQxt6BZWQkn-D-HzS88df7of0cceM9KZVdbdKGfsZB77jb8_lXTSH1kKt_bTLBx3-uf69mqgusobu5PxPaRMqoT_blGZiGmOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
❌
رسمی؛ مجتبی حسینی با توافقی دوجانبه از نساجی جدا شد
📊
2 پیروزی - 2 تساوی و 3 شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/106870" target="_blank">📅 17:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106869">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf935413.mp4?token=qzGfjOUAkFfcZBsMOR8AGbPZZe69KdfLbCylrexsbcikrXd85oT4fCNg5CeDmJ7Pp_VfpN1YIMYYEF2Z5XpHhRhskz0YLHsRwAu87PJpsLzhkweTeK0Jb2ktW6r5wXMC99M5fDPYw7ftpg8iSm_rHuPsxIabyiYdtjeYKiVhl1TQXvr6PQBnFzYdUieF_2jYQHQt59pMPCO9cmCB5V0Bka3rNE0CwEGZvs0Oq8OTcgct2fqXVSnRWlCy_0PO1rQ4KCP-AqLtH5cSauSL-8Vgw3foTMtCGYxxQ2CcyuGCCHYjyO7x7nTvjjE-Pjoo6dNiQtJon9gksUpFbSD7h6Rh4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf935413.mp4?token=qzGfjOUAkFfcZBsMOR8AGbPZZe69KdfLbCylrexsbcikrXd85oT4fCNg5CeDmJ7Pp_VfpN1YIMYYEF2Z5XpHhRhskz0YLHsRwAu87PJpsLzhkweTeK0Jb2ktW6r5wXMC99M5fDPYw7ftpg8iSm_rHuPsxIabyiYdtjeYKiVhl1TQXvr6PQBnFzYdUieF_2jYQHQt59pMPCO9cmCB5V0Bka3rNE0CwEGZvs0Oq8OTcgct2fqXVSnRWlCy_0PO1rQ4KCP-AqLtH5cSauSL-8Vgw3foTMtCGYxxQ2CcyuGCCHYjyO7x7nTvjjE-Pjoo6dNiQtJon9gksUpFbSD7h6Rh4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
سکانس‌جالب از قسمت جدید مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106869" target="_blank">📅 16:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106868">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98bb41c972.mp4?token=fXL2n9b1vkc4yaqIExJxSPPghdFuu41gSG2ltISVSpEtaLpqF5fB2cO4MudlDqAO9rFHbBmxv6pryhhHx6NF_OsS4zPtsbylepxofLbMANktKDTIRgkCNgW8TDfBnEQSzi_7m1zW5YYT2fM1S8Wao7bfVujRGwmKVjlHW7TVFTnRl1nfxl_fZNW4YDe-T1pAD6GTjBUxYMqbXjIcV2njCmYygJJbSeiLfPyS9hnhACJTiHTaMqeAVZJ3i5WtHTYyQh_IbQv5e7UpGx1hXv4BZ4gvboRMdihHWlZqUqemsPtnE-RuplVvJeDrRKD3sn380OO5LuIRk-wwbmHIeh2Rdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98bb41c972.mp4?token=fXL2n9b1vkc4yaqIExJxSPPghdFuu41gSG2ltISVSpEtaLpqF5fB2cO4MudlDqAO9rFHbBmxv6pryhhHx6NF_OsS4zPtsbylepxofLbMANktKDTIRgkCNgW8TDfBnEQSzi_7m1zW5YYT2fM1S8Wao7bfVujRGwmKVjlHW7TVFTnRl1nfxl_fZNW4YDe-T1pAD6GTjBUxYMqbXjIcV2njCmYygJJbSeiLfPyS9hnhACJTiHTaMqeAVZJ3i5WtHTYyQh_IbQv5e7UpGx1hXv4BZ4gvboRMdihHWlZqUqemsPtnE-RuplVvJeDrRKD3sn380OO5LuIRk-wwbmHIeh2Rdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
ژرژ ژسوس سرمربی تیم‌ملی پرتغال:
🔻
کریستیانو هم مثل بقیه بازیکناست؛ اگه عملکردش خوب باشه بازی می‌کنه و اگه خوب نباشه، بازی نمی‌کنه. آیا جایگاه ویژه‌ای داره؟ بله، دوران حرفه‌ای متفاوتی داشته و پنج توپ طلا برده، اما آیا این چیزها روی تصمیمات من تأثیر می‌ذاره؟ نه، اصلاً.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106868" target="_blank">📅 16:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106867">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a989591ba.mp4?token=GbSitypCeSNy8OQz-tKucB9idfUrXUhes-IaxoS7TLwVGqRXOPhK4_fCMjMJULVymz1uKsMkED1PyprFB-pgqZe51X_PTCMpc7yQ8kUhzx4Ak3wjkd-2muy-uGUJAWdh94PAT_lmlOO6leSsPRuhjiFFR0rt1FhEUvvwNlZBmbY8HV9gPkU2vtiCOOtWr-43F2mIKHAyQCNrk0m7wuApFkttlO2f5tftoPC5Y8P7dsVz2JvDYC11VP70cmSQVuarpxc5Wt4qg7cLjvkgPzrSAxGEmSb_Y7rTcqNCFO5hmrrDdCO1sDJ3z2mW1YsXAIH8pnuMzqkH8HJ6GccaHf3FoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a989591ba.mp4?token=GbSitypCeSNy8OQz-tKucB9idfUrXUhes-IaxoS7TLwVGqRXOPhK4_fCMjMJULVymz1uKsMkED1PyprFB-pgqZe51X_PTCMpc7yQ8kUhzx4Ak3wjkd-2muy-uGUJAWdh94PAT_lmlOO6leSsPRuhjiFFR0rt1FhEUvvwNlZBmbY8HV9gPkU2vtiCOOtWr-43F2mIKHAyQCNrk0m7wuApFkttlO2f5tftoPC5Y8P7dsVz2JvDYC11VP70cmSQVuarpxc5Wt4qg7cLjvkgPzrSAxGEmSb_Y7rTcqNCFO5hmrrDdCO1sDJ3z2mW1YsXAIH8pnuMzqkH8HJ6GccaHf3FoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
جمله قصار فنونی‌زاده خطاب به امید عالیشاه: با آدم بی‌ادب باید بی‌ادب رفتار کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106867" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106866">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvyPpW2abqWSIBLBSxmLNecQrApHhCrngneQHZSQSyF6QuYauDax4BZ9Uao5he28JJDjd9lluL5WLASlNP00LQb0-XJk5QsMiPNITxybmmKBtddt6O7bMHxv7k1FF6oZKeO7ihhy6zDIWs71TEV4c_4XHQL_0ZJ2RlQyEKl0pJBV8k0Zq5rfrwVO345XG5sLsBXl0eFqeLz60TNh-RDb_WUlKKrpOkubbqZIdtCWNJk6g0jZldioc_QuvqxowxBw1um9jZ7MLw-beEv1BGOxTHYwUrv7-rJ9nXb5tClO-Cug8R_DaAFrJiT9LE6BUlCWV7r21BytJ_uBNODbBtp7Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد ضعیف املیانو مارتینز از زمان حضور در باشگاه چلسی:
⚽️
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل برنتفورد دریافت 3گل
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل هال‌سیتی دریافت 2گل
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل آرسنال دریافت 2گل
⚽️
⚽️
⚽️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقابل برایتون دریافت 2گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106866" target="_blank">📅 15:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106865">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHPHGaeWRNgUSWAyTgWVILn1osuqoC-0keDsvFa3sqnecLluOi28vva9TXw2DP1UZr_DuPgZq-PftdrHy5YUPJKoLZ4bm0BRX6gy1CJK5UL2P2mtFfvfW6-88x0r_WWshMsqmsqEtIzMr8OcmNgd_jsU5JGfsR5o_PdcIi0JFy8SoGlEzlascIiq41MRfOxRvARJSErv9_AvhWJLsMMA_YZWlJOnr5r21hhpSUypcPvLo5XUaOpznTDqISS4ktKoago5NB2i51uWg1FsYDjs-TYgpitAazUnL0vz465mYeAqkT8aUZbD5t-bDWgfRKAk67POqanS64gSh2bCre-0Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
لیست‌تیم‌ملی آلبانی برای فیفادی بدون حضور یاسر‌آسانی ستاره تیم‌فوتبال استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106865" target="_blank">📅 15:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106864">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed8ff21de.mp4?token=JsqZs4QJv01FUklwntDXsQqqP6Pi8djllh7ikCsSnmVR987aum5KBDKiMosX57-UnCYBzua1Ykj3oLwVBzjj0CxUefPVRLhyPdmSrfDWKnh-vqE7-0onscymQP43cCN0-pqLgt40zeFwwh5mGgr4I_bgaog-L99qM4jVSFQftD_t5mz5ulyChZ6yzDXJQLRbjm252B8lBeGF7eL_jn92stgNXsZUt2lK8zTa5QZEzuvGhYr6LDdh4GVNDYv8hMdUXYNXbqipgN8tijhLv66JEbFQfguEbkGMEx-UFYbD_k1ZEl2l0An10DBfuc1bnthHgxxnruLtwyp4fpZgGbPDrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed8ff21de.mp4?token=JsqZs4QJv01FUklwntDXsQqqP6Pi8djllh7ikCsSnmVR987aum5KBDKiMosX57-UnCYBzua1Ykj3oLwVBzjj0CxUefPVRLhyPdmSrfDWKnh-vqE7-0onscymQP43cCN0-pqLgt40zeFwwh5mGgr4I_bgaog-L99qM4jVSFQftD_t5mz5ulyChZ6yzDXJQLRbjm252B8lBeGF7eL_jn92stgNXsZUt2lK8zTa5QZEzuvGhYr6LDdh4GVNDYv8hMdUXYNXbqipgN8tijhLv66JEbFQfguEbkGMEx-UFYbD_k1ZEl2l0An10DBfuc1bnthHgxxnruLtwyp4fpZgGbPDrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
سوال مهم از هانی رامبد؛ برای رشد پایین تنه حتما باید اسکات بزنیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106864" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106863">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87cfdef19.mp4?token=eVzVOGdLIDcD2EhrIkm1uzLfB-gEPKWnNN2BMmb89QdqkiREMCh0xgdf9vmHlQDaFkHhriGOhIIgIbZsWL-Te9yUnKpY9tGQEvDam9G4ccd93LgrNCPePZle5WraVRsRQQaLACgWd834l3Oxo6PRscYbGy98WqmC6TMWti1rXAr4tH-m-quiDg_ccKcmx8bmh34OG12R7RHcxqCMUfVYdkjCXBZSWZbNutj5iS5vo2Am__lfk4QaWeVJpxFoN5wki_5LQOcyPqA-vGEeWsCwtAao3TaeOsHNOnGgflQmTEQ0-G8OzfLinz2cUA4Cn4iD8OoEgsML2SpRoGREkxteZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87cfdef19.mp4?token=eVzVOGdLIDcD2EhrIkm1uzLfB-gEPKWnNN2BMmb89QdqkiREMCh0xgdf9vmHlQDaFkHhriGOhIIgIbZsWL-Te9yUnKpY9tGQEvDam9G4ccd93LgrNCPePZle5WraVRsRQQaLACgWd834l3Oxo6PRscYbGy98WqmC6TMWti1rXAr4tH-m-quiDg_ccKcmx8bmh34OG12R7RHcxqCMUfVYdkjCXBZSWZbNutj5iS5vo2Am__lfk4QaWeVJpxFoN5wki_5LQOcyPqA-vGEeWsCwtAao3TaeOsHNOnGgflQmTEQ0-G8OzfLinz2cUA4Cn4iD8OoEgsML2SpRoGREkxteZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚑
صحنه دلخراش مصدومیت یک‌بازیکن در هندوراس که پای بازیکن در آستانه قطع شدن رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106863" target="_blank">📅 14:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106862">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔥
👍
🇩🇪
شب فوق‌العاده اولیسه در برابر یونیون برلین با سه گل و یک پاس گل و هدیه‌ای از طرف نیمار؛ بایرن مونیخ ۷ - ۰ یونیون برلین⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106862" target="_blank">📅 14:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106861">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jb98IiMhRhEYO9w8XD0zMfAYSoeaetukRDV5rNotYM2T3pEjh9zuWtn1ppwrq5_rRvBqejdBQ8owTnQJhUi9s_0t6NMPaq5ISEtQ3F5gqo8zLiJC7QkfX6qtrBFoUgcr0QP-BBOss9oFv7oQsEzBV8wr8Hll78Op8N-gX_Yy7IZIQSqDoH9Cejd9QbeMaXHn5EdxwYNMBBbgeKcwtJEcMBvPEVAJ_W6IuPZ5akaKpNQrIRtEkOVxePZrOwhSJxNcUDShArcGwgtiLFTyh7mAr41y2x6i94l76c-TZt-rfMQMZDb1v9dmv0aSRpULl4BRANLJgcoITI6Cwx2Xw67TSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌پنجم پریمیرلیگ انگلیس: ترکیب تاتنهام مقابل استون‌ویلا؛ ساعت ۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106861" target="_blank">📅 13:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106860">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3121f63a1.mp4?token=HGp_Pp1fibdfGCgPmz1yGYUzBUhA7_1LshtrB2tTvx3s9k3WKHqrkqbc20Cn2DKwtB1pm_vfeIVWe6C6qZVtsW_b9BLQL9EIlTb22bYuJrVOkwobJHPxY40nbh2BUk8oaeaGEy_Tt0rDhS4PcNzvAPrEwrF54orLkpV_ouQkRv4JhOqy0yxI6-oZtgY-td-3lBhkwUlWS9-TaURwqfD3XcALcG-ebOWyfb9OToGBegLVBQkH1pqoZhGJrQ9noBI6zV8k_2E6dmmDlUjxqDd5l4500WIrDDWqFuutrhlGHOlacEuCsg2C0gpolqcVhGvQgqoA9JaDoTSG8JIMqcAWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3121f63a1.mp4?token=HGp_Pp1fibdfGCgPmz1yGYUzBUhA7_1LshtrB2tTvx3s9k3WKHqrkqbc20Cn2DKwtB1pm_vfeIVWe6C6qZVtsW_b9BLQL9EIlTb22bYuJrVOkwobJHPxY40nbh2BUk8oaeaGEy_Tt0rDhS4PcNzvAPrEwrF54orLkpV_ouQkRv4JhOqy0yxI6-oZtgY-td-3lBhkwUlWS9-TaURwqfD3XcALcG-ebOWyfb9OToGBegLVBQkH1pqoZhGJrQ9noBI6zV8k_2E6dmmDlUjxqDd5l4500WIrDDWqFuutrhlGHOlacEuCsg2C0gpolqcVhGvQgqoA9JaDoTSG8JIMqcAWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
▶️
ابوطالب حسینی با این ویدیو اعلام کرد که دیگه تو کار ساخت برنامه فان 360 عادل فردوسی‌پور نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106860" target="_blank">📅 13:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106859">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKvwa8ivpPXpVbY88AJvkcbj47Y7QJ5b7brX4gtvqvGGeMFk-XJmC_xzTQQKlCMEJIz-qAN1B7s8LtJJUq3YS9iDDVoq8InkDf8PuXh0eFeq4IoEpD0IuB0hKwPTeIaZiA7Wg_UtnavqZb_QtSQm_6B-WRayjVhSAUs8h0pWJt4ibBkbi2PDpeYE9v0HtQ6oO72-6Abbtson-TtEFQKoCasbSlmxVemKccv6DyaIS8ACLFSYPxRBnsvDzn62W9E08DKc5hiPOYJDNJqqifgO5yz_33f8zNVD6cpeli94dEkKowzxqLJiFYlp_Hizp7rxmlSeB1ZV8U5Ka48Y48Ixqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🏆
رافینیا: بدون‌شک برنده توپ‌طلا باید یامال باشد. او آمار فوق‌العاده‌ای داشته و قهرمان جهان شده. مردم حاضرند برای تماشای فوتبال او هر رقمی را بپردازند و من یکی از آن مردم هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106859" target="_blank">📅 13:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgDR8xNkWVzGegZIJGC1xSiOZ8_5OyVgrEL9qO8taintep_9Sw-9HooujlZFx6Tby7npWJn2fIG14eHFxB1vA35HsxOz9uVSbkYoUbRI1sHSpufUUtLNFRT8PD_VLofcivJtD8jO0keqXzj4Kddhr2BmfZzaDJ8Y5a7iwuMoW9_vKZgpR6h2NeEjJl3L3vFQG6ZGv95ND7H0sRbOWvgfXJd-XuQPyN7-jD1qsvcM-4G2_0Jb19qXZF3XPxybl4H797504UCz3X0Ja8KXB8A4CYTwuAamxGwxTv42OV9SCdyMWihgm9yDkPQKFhIiMyseSRv_I3NKvjb43shbhlcEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
رافینیا
: در ابتدای فصل یک‌پیشنهاد بزرگ از نظر مالی به دستم رسید که مقصد عربستان بود. این پیشنهاد می‌توانست آینده من و نسل‌های آینده خانواده‌ام را به کلی دگرگون کند اما بخاطر عشق و علاقه خودم به بارسلونا به سرعت با پیشنهاد مخالفت کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106858" target="_blank">📅 13:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da53ddde15.mp4?token=OplahypIfoXDqiyjHnldgPQ2K282c4FDyi79njPE_en8fOC-aMWk7s7xg0wbZno0ulhlc-SEe27Q1jLGkT3oRuHXZmxUoNz-0zSKGMt2XC-D2fFYKlyViX-6YF51EVMsj38dP8mquevLva6LKGmE24EO2w4iJmH5rJHX4FcyxUbhs9Vwcu30aHOZxUcm9mEJ-CnDcYdDQ_-zeMBJ0oYMVvFxUVyDHwQow02pGnubLKAcStdzKPA7KVEqtmdIxf6vmmf0il7gZp2s_ocNQ-tv7SqB4w1XfgSNL09U64IJgbo8_Uwqk6IsuzL4zS92XZ66NN5pWe3EOmVztUvAIOz7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da53ddde15.mp4?token=OplahypIfoXDqiyjHnldgPQ2K282c4FDyi79njPE_en8fOC-aMWk7s7xg0wbZno0ulhlc-SEe27Q1jLGkT3oRuHXZmxUoNz-0zSKGMt2XC-D2fFYKlyViX-6YF51EVMsj38dP8mquevLva6LKGmE24EO2w4iJmH5rJHX4FcyxUbhs9Vwcu30aHOZxUcm9mEJ-CnDcYdDQ_-zeMBJ0oYMVvFxUVyDHwQow02pGnubLKAcStdzKPA7KVEqtmdIxf6vmmf0il7gZp2s_ocNQ-tv7SqB4w1XfgSNL09U64IJgbo8_Uwqk6IsuzL4zS92XZ66NN5pWe3EOmVztUvAIOz7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
رژه کاروان ایران در مراسم افتتاحیه بازی‌های آسیایی ناگویا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106857" target="_blank">📅 13:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVKgWbkMakd6CReFpNjDbgjrJoWrvDeavosu1pC-2qRixd0afg1OgSPJPBDRjEoUMR4oHVeC-Cr_dQ96ES_Txl0kxlva69oWl9weaHfeUvkbcHWCgOLfes0F_5dwUmbPKQ23MpEaN8WHDzNv8lOd9d4tyM4mZyT6LuzJTkC6AsySmWzpJjQDIQB2ySznwcvmPXussUrA9Canlr8seNPrvnJ-2DWFFEHYqJu7WSKSRHWcBPf0x4JxNYkE3eztSnFW2ltn2ZnVwr--a6esu1AEBMttCX-YDIfV8Jw7QxsZBi_YyG2ZKI56rTiXcAfuMSWBkYRUivkbinqoZo-4Hv7dOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
نتایج مانوئل پلگرینی در تیم رئال بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106856" target="_blank">📅 12:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAs69U695Gns_B3cg2Q_7AtTty5f7ebIDx9turlQkpdwQ_xEFGQ_AWRA7yWWn8o-s5hl1M05qcPBgKZezzLsjr2ASDqe_-E0b-8th0Bp0kQQGZxYfYTrvQv6nCTPm1M0OhEyeAa4vFlNExxj3yIZA-Hq7f0CkhRoW867dpqgzUXbaAmvaKmhX5eDECXwF_0dzDIncFj3iHoUCCM_h5VvQOJpsr22JmYkhQ4Hepgrr9h9f--v0G4UCy-4qHYhwypFeIvNGbprSZf0pyIdBZN3fc4JwyTEjNBNCqs89yTd6BSXcsPb2MUZ7EzOQX4sZKrpNy5KSu56vzSnVdf7mTZYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🏆
با برد استقلال مقابل السد جایگاه 5 ام ایران حفظ شد و سه سهمیه مستقیم باقی موند؛ نتایج مسابقات استقلال و تراکتور مقابل تیم های قطری تاثیر زیادی روی حفظ این جایگاه داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106855" target="_blank">📅 12:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-sKHmHCUD-mHwY9WeIpcTB6Lovn0Aa-OfI4xSwcgPPrGi5UUwaOY5PoGcN_nZQllioJ6cu-51d8g6G4uVU6qpTbr0jZsTWyyfnaYwZfY0ObXMTFOzI1Ms0SsrLF2vdOsNqjyBVes_82aMKvtxMMwSyPy9uZ_guVZ7hKE8_wEYwS4GxtUW4RWqRnGw3OQ6VaYosR3SQ8j-iZqzo0xa9q46qrkyHkjlvYXOQFbkC2bGSxTsSWpe3s_CtyW85U6xHscf67M8tla012XSgNC3Zy2DvBAnsTZ5PsB0HBWmNIzUtMC4aPkVA-sL6DWPcKjoDbTgcqY8soDR_oWBwNN1pcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
لیست‌بارسلونا برای دیدار امشب با سویا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106854" target="_blank">📅 12:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltOb71cbpBgfgRZcKklx5LSb2jmXDbMc6DvW2l7RkdFwcYKWwDh0n6B7dO-X3wPSRmzaCtuPcZWE5nX3I4J6ddd_0pAQsd2m7LVZ9TEwzH3P_l0JKetsGzwSUzHh5tbSsY0sNN5XAHJsTa03Rwwls0QQGZi1KjeE861RIFv-_TmAcioMJ0XZhfcRzjxrFtgQWl3MLxsEBUtYAkUpn-PV0kAPUr4sjk27GDpDzPffuQAFNZf27Om_nEFQ9OEkA9yiaW_WlKInj2K8oaAtTG1xUIxOnkBD6EgZAYIn1aqlLTstuKe4Jtj6Jt-7Tq-s643bUwz3qMe4-lyRUCasmeaq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
▶️
مسابقه دوی نیمه ماراتن بانوان که امروز در بوستان ولایت تهران برگزار شد که حجاب شرکت کنندگان بدون محدودیت خاصی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106853" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106852">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106852" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106852" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106851">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOeoGwwEeFcC9lqDf9tBT5zFXoBj3C6IeYdKZt4uDnp83PrQCo5HzQHYrFRt7FBaHmisV208Frp_8DdR595I3QJWifYn5lJUyJJWmK-2JxzA7Jm0LguDW18pfPlCcMZfboGVobjFqaREHvMzz01vf0ydwHjzQkX1hV5ppoHqSWadl0bDcNL1d6tCTcmznCl3TyT3ScMCC0VRB6KYrjisg9q28CJ5cMCNaIz2bSXzGWpwhFZTI_9to9PAwojs36pSjf9LJuBmxqC28P6NwNqzIpcFu8Ci7nbZkafriZ_a2mB18GON9RYNROHCyfGxqE0fWChwXyxDxkW6ij1XID769Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106851" target="_blank">📅 12:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👍
▶️
🇪🇸
🇪🇸
در دیدار خونگی رئال بتیس برابر ختافه، ۱۱ نفر از مسن‌ترین و باسابقه‌ترین هوادارای رسمی باشگاه، بازیکنا رو موقع ورود به زمین همراهی کردن. این مراسم بخشی از برنامه‌های هفته افراد سالمند بنیاد رئال بتیس بود که با هدف قدردانی از هواداران سالخورده و یادآوری نقش اونها در خانواده بتیس برگزار شد.⁣
از اونجایی که بتیس توی بازه اصلی هفته افراد سالمند، یعنی ۷ تا ۱۳ مهر، بازی خونگی نداشت، باشگاه این مراسم رو زودتر و در دیدار برابر ختافه برگزار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106850" target="_blank">📅 11:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106849">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPm3iEzbEdMZWYdf7K8lCma1BzYT2CciPzZjcn4u9YqKtk40IpfJBEdS8gANS9yb89_ROA5PeS-5N7QmM1ZbMA_3iFV0fFpZ1wwHBfvhVd8ioiVVDeQWNXRNupVaEWImlZTNnCJPgWszwa4hvvkP08WSn2IUe9lBTJyBjPTL1Qw1PPJpPlE12_qCfpJiGl2SdOsNHxN3Gu0Dvjy1SSlW8unQZIKO4iRjF2YEngo-1r8svi2pNjBFE4gb7umthA6da6JaKlnNkmLnNGnp5Sgeb3K4aMXUffrrmCT4euqjRal-Ll9WWQkduViPI8ztrrgRIJjI4NdJmc8eVzKbsJiSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
😆
وضعیت سه‌فصل اخیر اندریک در رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106849" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106848">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32f6de555a.mp4?token=IFZCKpgcMA-qHVIKV9UFuyW5DNdIMErKs-dvCUzc9JdojrgtaKsgBsqm9NrgOxPYHeqtmqpFIZP5ylzF6GenPIMD4hkzjCmafzJu_bCdxTmfxQPh8nVlbi8NwIGRdB8tRC4g4kQKERhj2qNuLRzceyx0TVam5XXgdocs1tkPiiijgNtieljTctQSqNFQONLzRIf8qmQxUV3o5MQJ_pSKOfTuq0g7rS2oIosVtDFxwyPAJccKsVRFfl9y_ve1SzOn_cdMICWftgGPpUc5gXzxjGflILCi39N6TB7FnIEFU4qZJs5A_cJFZidcK3HuW8Q_dsF03uzkUNMwgBs_TBemZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32f6de555a.mp4?token=IFZCKpgcMA-qHVIKV9UFuyW5DNdIMErKs-dvCUzc9JdojrgtaKsgBsqm9NrgOxPYHeqtmqpFIZP5ylzF6GenPIMD4hkzjCmafzJu_bCdxTmfxQPh8nVlbi8NwIGRdB8tRC4g4kQKERhj2qNuLRzceyx0TVam5XXgdocs1tkPiiijgNtieljTctQSqNFQONLzRIf8qmQxUV3o5MQJ_pSKOfTuq0g7rS2oIosVtDFxwyPAJccKsVRFfl9y_ve1SzOn_cdMICWftgGPpUc5gXzxjGflILCi39N6TB7FnIEFU4qZJs5A_cJFZidcK3HuW8Q_dsF03uzkUNMwgBs_TBemZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
وضعیت رئال‌بتیس که خیلی شیک‌ و بی سر و‌صدا خودش رو در جمع تیم‌های برتر لالیگا رسونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106848" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106847">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=QlA2oM9CZqOdzM_n_-UoOY5_mAlTqeQEMxnpnYKKoY5ZebiLfz44enNKZiJTqywOKNFlhGqoXtZaS8Ng2oRZlclGRpzpIxMs3hKCcQYHNmcKHua0ceIp0jbh7O26lCOrObhihayGsqOrqTEo6MA8w97izdaUGb4JDk6drPC-k36psd2NwK_633Y0l4aNRznZtWCo3yBnd3-e8mLNfPFor4UwXjvK9TfXWnwjdr-EL0hWXUNWSNSZShG3PBdZp7Yflmg1KNlKVFtVl4qhUA5va0iDnZ5sVRn9Jy62vZRA-yb0KHC0VG6J1eXt7ESrrii7kPtyeL_C_W9-yKUxvVxsRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7feae8a28.mp4?token=QlA2oM9CZqOdzM_n_-UoOY5_mAlTqeQEMxnpnYKKoY5ZebiLfz44enNKZiJTqywOKNFlhGqoXtZaS8Ng2oRZlclGRpzpIxMs3hKCcQYHNmcKHua0ceIp0jbh7O26lCOrObhihayGsqOrqTEo6MA8w97izdaUGb4JDk6drPC-k36psd2NwK_633Y0l4aNRznZtWCo3yBnd3-e8mLNfPFor4UwXjvK9TfXWnwjdr-EL0hWXUNWSNSZShG3PBdZp7Yflmg1KNlKVFtVl4qhUA5va0iDnZ5sVRn9Jy62vZRA-yb0KHC0VG6J1eXt7ESrrii7kPtyeL_C_W9-yKUxvVxsRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇸🇦
استادیوم آرامکو عربستان که 2 سال پیش یه زمین بایر بود حالا تبدیل به ورزشگاه لوکسی شده و در مراحل پایانی واسه افتتاح هست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106847" target="_blank">📅 10:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106846">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=fNhSscCi4MyKNfMFDZtTsnc4LBTAtBqe5G-2vh-d5i9zwKIrLwoFOIvWMFsTZPRjLhYkTulMHEdTlAxc7kCcrqAyN3XvyaaXScRAMYJ3K6OLfMOVsRRW5oBwPJgPut9YLMtQummQKkKb-dE-Nd2y3U0j8eqqq6mQTdGk9CaD85bnj6ZISYJsTciMVDjHfWGEGtuEGdHOghIVdYF_9bEVLq0qc_BAQAWyQg_I_DCi93kA2HC51sXm2n04jmQ4qxmPy-dlLz6GFjOtxlbjI4Z3hYf7DLZ6nCZpg3-kuMA1qzLhus5Ty08w-583FAj507OlBUFHYJRBMNjkAa1SjpJ6sTU2Fz6sZfGRG38X_ZFuOjFASOUDhEpRDFo-4sOHlJ0spTN0K91RemDSh9DUFxvAglG7bpnhzbEI7ZsYeCxsLK-h9rQHcIMnAFIZeRtwIKDqXIqJMb_rCEHEjsFDR0K60_sAdr0asUUnajEMiCC_dwnNwbUsRJIz_HlgzAnsXUdB-BRNVL_x1m3ebJ6uSxz7YooNIS-trGse5jwuZcj8pDc5cr4rJOUOoVDNm-Y1AciIHpRkbS1q9ASdxZqTvJjF_xmCchwmvoBm7UeII92Ky0L98rEK1nJW09ypaTiHJjgBFJUxv7YWAn3NfPie4FQcXlZbry1SpIT2A3I4FLsME9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ca24d608.mp4?token=fNhSscCi4MyKNfMFDZtTsnc4LBTAtBqe5G-2vh-d5i9zwKIrLwoFOIvWMFsTZPRjLhYkTulMHEdTlAxc7kCcrqAyN3XvyaaXScRAMYJ3K6OLfMOVsRRW5oBwPJgPut9YLMtQummQKkKb-dE-Nd2y3U0j8eqqq6mQTdGk9CaD85bnj6ZISYJsTciMVDjHfWGEGtuEGdHOghIVdYF_9bEVLq0qc_BAQAWyQg_I_DCi93kA2HC51sXm2n04jmQ4qxmPy-dlLz6GFjOtxlbjI4Z3hYf7DLZ6nCZpg3-kuMA1qzLhus5Ty08w-583FAj507OlBUFHYJRBMNjkAa1SjpJ6sTU2Fz6sZfGRG38X_ZFuOjFASOUDhEpRDFo-4sOHlJ0spTN0K91RemDSh9DUFxvAglG7bpnhzbEI7ZsYeCxsLK-h9rQHcIMnAFIZeRtwIKDqXIqJMb_rCEHEjsFDR0K60_sAdr0asUUnajEMiCC_dwnNwbUsRJIz_HlgzAnsXUdB-BRNVL_x1m3ebJ6uSxz7YooNIS-trGse5jwuZcj8pDc5cr4rJOUOoVDNm-Y1AciIHpRkbS1q9ASdxZqTvJjF_xmCchwmvoBm7UeII92Ky0L98rEK1nJW09ypaTiHJjgBFJUxv7YWAn3NfPie4FQcXlZbry1SpIT2A3I4FLsME9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
🇮🇷
آنالیز فنی جالب تراکتور در بازی مقابل شباب الاهلی امارات که باعث شکست نکونام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106846" target="_blank">📅 10:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106845">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=OV6WG5vFRXLVB7yLmzG9Ro1HT_b2KhT2AWEHvSDaHj4LNGLUNw1XQZ4xOWeqHMKwE5DKVlnC3B9QQ_dCNtKPpC3IeyO7qQM70SS2-I7n5HFvWaswqBEvz2Cvk3pFtY6mtI767xjdl7gYaOkBNjArYv3SpcL6Fpeo_H_QSytIvEaIJ5O92GTTzHUKEIJd8g3y6_wakM1z2HymI4f9VWdFb5ZQy2WfCyQ1dt1OuvvYSrPVBee_CtEFmcxRykf-ZBiZcJOLx3kOQu1svtg2KBUwJ3yWyfRpDrOOjOYd0KOswKzDW9N7MBU6QmfYsfUGA7XDnbEFSw3_KLZTFYE9lmDFdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec418d62cc.mp4?token=OV6WG5vFRXLVB7yLmzG9Ro1HT_b2KhT2AWEHvSDaHj4LNGLUNw1XQZ4xOWeqHMKwE5DKVlnC3B9QQ_dCNtKPpC3IeyO7qQM70SS2-I7n5HFvWaswqBEvz2Cvk3pFtY6mtI767xjdl7gYaOkBNjArYv3SpcL6Fpeo_H_QSytIvEaIJ5O92GTTzHUKEIJd8g3y6_wakM1z2HymI4f9VWdFb5ZQy2WfCyQ1dt1OuvvYSrPVBee_CtEFmcxRykf-ZBiZcJOLx3kOQu1svtg2KBUwJ3yWyfRpDrOOjOYd0KOswKzDW9N7MBU6QmfYsfUGA7XDnbEFSw3_KLZTFYE9lmDFdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇪🇸
امباپه: "اگر میتونستم، کریستیانو، زیدان و رونالدو رو به رئال مادرید میاوردم. من فکر می‌کنم آدم کیفیت و مهارتش رو هیچوقت از دست نمیده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106845" target="_blank">📅 09:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106844">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSeg6JXpZiFUvncOx6Twn86k8NO-UuoVk9Xommj8SXqfajr7FjpJ6l2cMsSXhJRbhpireLAgixAOJ9Vq_KDwezAZwqojxX00k3GHqyaB1ZYpU6WdvX0wpNXiKB3RJyrDUkfF1EQHcad8yCO_TrFg5x3AbqmYLLhyktWSnabTRl85cL-OQ3Z-9B_z-qvwSv9y3yWlXhSfYTf-2Zjq3AspXNrBcwU2i-yuWa6-HUthg5pbvTvu49E7ft8RS9BRsFyEHE6U7YtmlXcL0KT2giyYU9SN4vvagaIcceLDvmGcuj24PCrqBwbI2Ynt8U79w3J6frUSFkviA-aykZ1RVSZnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👀
از عجایب مملکت؛ یک‌نیسان آبی با ۹۵۲ میلیون تومان خلافی بالاخره توقیف شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106844" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106843">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=AtpEfzPWXpyuKLQuL2BatwI6BmqVxNi6NU938mLxIcgjkmjEzfQqcw5wIW3ExJIkr4-XRkwX5rgGKMUqErjzaZRAtRu14URWu4kdH-mQujNvW8EObqMG7eC0gZ584vzec6B3vmQMdSvn7VTores8SScGLhmSJUciBg79F9MIaAqZzhMrY02nEDnupOstzTGFYaoCHN-W2s1bE6D2_gIREJt57194s76vVhoLtK0m7LgwFqhUu8qh5RbRxvGmwhE3UXRt-qdHhiG3s-_6fQrrwn_lQEZX05SpPY-PwLnL8dteIM0c_1ARSHTD-bYixtxe5D7aqacPhfeQWrtH_KzCXY7mPAplaxyJPuRp65ZoyAqBdZ2JqUGx6Sy3b7KmCI-1XNQjVjAyZl85pNwp8Pj0QmbiTZ740O7c_e0MUzedvAQBAi9gKQ24_IDqD00HSiwndA6aRkE15OHKGZ1MfmtoP_0svPSm1cL88IFx7wMVAEpw8byoInvmGXBduWadw9MonPeRjVjzPNgKmZ2i4q2Tsb3ssCu4RCuJFIQl29Mr3oe4INo56zvcvL8IZLBxCzgM3kYbEkl6YBihogOWwdLEZkzgbzqqAPTWam3UUHfT-o1Rov-bBYkbI_ofS12759KpuLiUj6LafBYF1MqyLJeOW66GhMzYKS6OGMHTtzQKBBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c2ecca4f.mp4?token=AtpEfzPWXpyuKLQuL2BatwI6BmqVxNi6NU938mLxIcgjkmjEzfQqcw5wIW3ExJIkr4-XRkwX5rgGKMUqErjzaZRAtRu14URWu4kdH-mQujNvW8EObqMG7eC0gZ584vzec6B3vmQMdSvn7VTores8SScGLhmSJUciBg79F9MIaAqZzhMrY02nEDnupOstzTGFYaoCHN-W2s1bE6D2_gIREJt57194s76vVhoLtK0m7LgwFqhUu8qh5RbRxvGmwhE3UXRt-qdHhiG3s-_6fQrrwn_lQEZX05SpPY-PwLnL8dteIM0c_1ARSHTD-bYixtxe5D7aqacPhfeQWrtH_KzCXY7mPAplaxyJPuRp65ZoyAqBdZ2JqUGx6Sy3b7KmCI-1XNQjVjAyZl85pNwp8Pj0QmbiTZ740O7c_e0MUzedvAQBAi9gKQ24_IDqD00HSiwndA6aRkE15OHKGZ1MfmtoP_0svPSm1cL88IFx7wMVAEpw8byoInvmGXBduWadw9MonPeRjVjzPNgKmZ2i4q2Tsb3ssCu4RCuJFIQl29Mr3oe4INo56zvcvL8IZLBxCzgM3kYbEkl6YBihogOWwdLEZkzgbzqqAPTWam3UUHfT-o1Rov-bBYkbI_ofS12759KpuLiUj6LafBYF1MqyLJeOW66GhMzYKS6OGMHTtzQKBBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پورن‌استار ایرانی که در ایام‌جنگ اخیر با دختران خوشکل و زیبای اسرائیلی رابطه خشن جنسی برقرار می‌کرد، دست به توبه به درگاه خدا زد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106843" target="_blank">📅 09:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106842">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s5fGN2inmCjsg6fKLaRLXZFbxWjhtqDs2PeWBfCZk5dVXF-b1P5nbzL_Yon_1TgxZzPLAzvkjo-x6c2x1zIJyH29p0-1H15FMWFfjDDtje5EY12pqIMLso1I91gI25vPmmmGz3wlwmjEgZ5Jibn5PjJtAfFdoTqwxr35NyrLCchtfS04T9rnJeB2_zqUQB30vGYJ0jM20fTaXvFtWYc441KsSQ5IEBS4YZfBF1aYWgZ04WbbmrTqpHKabxLgvVB5_dFQLvq6oYNAxiauXz2uh_dfgR4szEVrrtsKi56rFHubAXyYKel5PBBsO8dBmdgVmIuGUAzp-jr3UtXm5vFvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔥
فیتیله بعد از ۱۱ سال پخشش رو دوباره از شبکه ماهواره‌ای Fx2، شروع کرد.
هر جمعه ساعت ۱۰ صبح.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106842" target="_blank">📅 08:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=R53kJ18ZxjizlXUW8zcjOmRxGhScSiHDuS7tS-nZk40Te5rTdlqHhgTgtJv05ec1MsLerZh3L3JEs14EDaEvHM2f-ZoH0vJRul1d88FYlXwtQFOpMDCi1cPiHgxr8TtqtHdZsGugt1EPcs2xB0Y4Jw1z7XpACadXWoh2WFg6Ytmu6iQjCDAQPlCnB4PYl-9hH4erL_wKKPcE5f8dHfMR2GLc537Sl30b2wpO_zyFd1eLEWbKm7EKEERhGTRqq54PZ-ZhEceLPj2SlsGb5l-4oBmvC9qQNo6ztwYdTIvlZ5d4CGRMOoJO_L1b4s1rC62_mlGGyLjG7BEgqb1Phd2cJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583a7cae1d.mp4?token=R53kJ18ZxjizlXUW8zcjOmRxGhScSiHDuS7tS-nZk40Te5rTdlqHhgTgtJv05ec1MsLerZh3L3JEs14EDaEvHM2f-ZoH0vJRul1d88FYlXwtQFOpMDCi1cPiHgxr8TtqtHdZsGugt1EPcs2xB0Y4Jw1z7XpACadXWoh2WFg6Ytmu6iQjCDAQPlCnB4PYl-9hH4erL_wKKPcE5f8dHfMR2GLc537Sl30b2wpO_zyFd1eLEWbKm7EKEERhGTRqq54PZ-ZhEceLPj2SlsGb5l-4oBmvC9qQNo6ztwYdTIvlZ5d4CGRMOoJO_L1b4s1rC62_mlGGyLjG7BEgqb1Phd2cJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پاس گل جالب دنیس درگاهی با ضربه سر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106841" target="_blank">📅 08:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106840">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106840" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106839">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/106839" target="_blank">📅 00:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106838">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106838" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106837">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKKiIL7QxLgJ6HBm6wMHI_dcjlhfG5brWqpJm0YN52--S48q2QVoUldCknkJtHrvD6_Ivmp_cvz5oHhuqjII2FvhpAX8A-5KGVW6v5KxcE0m3DBne2XPtsCRnyM1cCeokg8UBrZvDj2ZUQTW1IzNB8P1vE7i83onGmE0Y2OVlhsCphltPDSzhOdHCJvALUdPPZd-EgcTAYFEuQ8IQqja4GOSGIB6wWXM0UZm2x81K5NH0oreWshkb7-79EJqPFDp1cszJf5RIf0oxOZNkAxCXiWEFMSrwk904_Y5ZSiVWSmFsMPUjVModq6kOwv5iGDzgoPmYnzdYuieVPwtgOsAag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لامین یامال درباره علاقه‌اش به نیمار:
🔻
همیشه سعی کردم بازیکنی باشم که با خوشحالی بازی می‌کند، و نیمار تجسم واقعی شادی در یک فوتبالیست بود.
🔻
نیمار از آن بازیکن‌هایی بود که فقط با دیدن بازی‌اش لذت می‌بردی. نوع بازی‌اش باعث می‌شد تماشایش سرگرم‌کننده باشد.
🔻
تقریباً تمام دوران کودکی‌ام، صبح که بیدار می‌شدم یک کلیپ از دریبل‌های نیمار می‌دیدم، بعد یک کلیپ از گل‌هایش... او واقعاً بازیکن خاصی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106837" target="_blank">📅 00:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106836">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teuaoDPqeHCRrEGtttaE9dEYzCbU-YAKFYcMqyx79Dz6Eegt8NMl6rnglHw7RSrIzvhh2cfi5UQYYhhF043Cy0GUj13b2lxmvcXmqdFXUO08FLtQwm1ZEWsfuNu5e1UPSbI_84oAlEQzg1m_he0WtNiVJxc8JdkgIxSQS8uvrlU7z5zXCVflapPF9sPZl8Pg4OC3Ys6kjr255uSRkDxMSeVhqW0-rKL3Ce2grCd4J7RymfdGyk2Q_FUCCwPhmHWw7gv_l5Y5En9MCODIoYuBRxDEqch-cRwuP1eysswFr4j3pGd7HheSUpeopUW5fh_5Az2vOtjBI3M1pTlHO56AJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
يحیی‌گل‌محمدی و تیمش دهوک در هفته هشتم لیگ‌عراق مقابل حریفشان به تساوی رسیدند. این ششمین تساوی یحیی و تیمش در لیگ‌عراق بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106836" target="_blank">📅 00:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106835">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gl9jAfSQUaWJ_lOthIyZat1gnTqg0W-5ajlbcmHtD-fopakMPrUWaQAo6i16o2BYjs9dlIVEPCTKdAv8o7BKCNab7D15QRWeo8eGNGc2AkG5ANIpNHwzCxXKojzC_F41sebKiPQhSt4zZz1r_c7EYofQ03UOO34D1LWOsYltWWIdjpFNZ2whbLs38EJypP7X0H9cKrDcULdYqP2wDMbBmvKpdk9OrcODzWXdf2FtnUj9SuJHfKb1iBDa7ewY_vbW6x0MDbR2Jr54MnA7Mllw8K5RVJf8pt5xMiw2PRXJKSqqEhtA9HlKLU6nkq8hem7VPWSZMi19rehOYzjIf08W7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
‼️
لامین‌یامال: تا پارسال پاس گل و دریبل زدن را بیشتر دوست داشتم ، اما الان گل زدن از نظرم بهتره ، گل میزنی و تمام، کارت را انجام دادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106835" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106834">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=fd-wAUxCWXG4QiycIUmJE2wbjb-AithSpwtZfHU8AR12HY2j_Rszxl-wpjjOvv49UPmO31iqQZr_UCWVqVDw34AZ03uPjseZLDzhMLFdj8iBHSMZdQ1ik94p-mLQvYIpJtp44Rg1Xjkk5TlMyqDHOR1yCTCcVKjl2k4-s8s_aOo3lymQaq7Qb0mxv_3FCT0q6_Rc3N06iMQePIcLzKg2HMu-0xV7PhYU8czVaLX8FlqL2EuJPSyswed2bf2C9LP6HmZpJhTUxR3JJu-DrzqUuZbdEK6mzcWjM_Kb0YgtzE5p6Txj5EoeEb66M_mp4m_vY8aLCT0rJj7RIhU2gBaY8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1135acc96f.mp4?token=fd-wAUxCWXG4QiycIUmJE2wbjb-AithSpwtZfHU8AR12HY2j_Rszxl-wpjjOvv49UPmO31iqQZr_UCWVqVDw34AZ03uPjseZLDzhMLFdj8iBHSMZdQ1ik94p-mLQvYIpJtp44Rg1Xjkk5TlMyqDHOR1yCTCcVKjl2k4-s8s_aOo3lymQaq7Qb0mxv_3FCT0q6_Rc3N06iMQePIcLzKg2HMu-0xV7PhYU8czVaLX8FlqL2EuJPSyswed2bf2C9LP6HmZpJhTUxR3JJu-DrzqUuZbdEK6mzcWjM_Kb0YgtzE5p6Txj5EoeEb66M_mp4m_vY8aLCT0rJj7RIhU2gBaY8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمد تقوی، در برنامه هت‌تریک درباره پیروزی استقلال در برابر السد در لیگ نخبگان آسیا گفت: «استقلال نمی‌تواند در لیگ برتر مثل لیگ نخبگان بازی کند، چون نوع بازی تیم‌های ایرانی متفاوت است. دفاع منسجم استقلال اجازه نمی‌داد بازیکنان السد، به راحتی بازی کنند.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106834" target="_blank">📅 00:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=WDIyssel08-OZWJGOOpWCZaFE1Rw64Ffi0h8pZgzoQz1yk2qGZslpo9hjjhfLbyDZRivSFytZRNavAzBB6UqkijW46lg_JuU65dwPvvKX3k9b4CVNlg8xbkciP0QF_JJzm4Pb6cujeW0iC_5FkT9UBGbbmfHGpP6nC3B8LUK9MuxgwtZJKcxH_5WqC4zoCwoOMCeb-Qfb5S8zUPl3bHR9Q2U5F_a4icMcihfrkN9lb0K3kS07X0iG-DtsEixxSeHbUNuQMdGbBgIUaq1ouAtXIFWfFUJFX1XVKwyiGGo2071Ch7xUKuZyUSA--OXpWUAodpR51rI2WMgARy7pK5DGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914fe9902d.mp4?token=WDIyssel08-OZWJGOOpWCZaFE1Rw64Ffi0h8pZgzoQz1yk2qGZslpo9hjjhfLbyDZRivSFytZRNavAzBB6UqkijW46lg_JuU65dwPvvKX3k9b4CVNlg8xbkciP0QF_JJzm4Pb6cujeW0iC_5FkT9UBGbbmfHGpP6nC3B8LUK9MuxgwtZJKcxH_5WqC4zoCwoOMCeb-Qfb5S8zUPl3bHR9Q2U5F_a4icMcihfrkN9lb0K3kS07X0iG-DtsEixxSeHbUNuQMdGbBgIUaq1ouAtXIFWfFUJFX1XVKwyiGGo2071Ch7xUKuZyUSA--OXpWUAodpR51rI2WMgARy7pK5DGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
گل‌های دیدار بایرن مونیخ - بوینیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106833" target="_blank">📅 00:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=jk-c50J4DRyQ7M6sNDk6R7fpknoDP-h4ROGJedOSyqNl75EidTIevDAIhXiXtlfw1kGC7WIGLErkRTueR0YEoFs_9hCXf137U0YZBL_TbGNYc-jNsnGVBnGXvfy6xXqBs7j6hJzTpDezTCW8WHmvv0Ye9v6MhgPCz5gtxGnP2o2dF7H-Yi6qzat3LXekpJaVk25h9Z3JvgPjIggFmDCWEZgerv29qsKsSZweSj1D60OZALlJsmMGcYOKGBW_9MS5WceqxFZ07tsjzltmhFlHzIv-SEPTM5cY4bRGT6eKMg6-LjWDM8ZzAx6V0rgcPpD54XQfQr1un-22FNod_YbECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e28dd692.mp4?token=jk-c50J4DRyQ7M6sNDk6R7fpknoDP-h4ROGJedOSyqNl75EidTIevDAIhXiXtlfw1kGC7WIGLErkRTueR0YEoFs_9hCXf137U0YZBL_TbGNYc-jNsnGVBnGXvfy6xXqBs7j6hJzTpDezTCW8WHmvv0Ye9v6MhgPCz5gtxGnP2o2dF7H-Yi6qzat3LXekpJaVk25h9Z3JvgPjIggFmDCWEZgerv29qsKsSZweSj1D60OZALlJsmMGcYOKGBW_9MS5WceqxFZ07tsjzltmhFlHzIv-SEPTM5cY4bRGT6eKMg6-LjWDM8ZzAx6V0rgcPpD54XQfQr1un-22FNod_YbECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇩🇪
سوپرگل دیدنی اولیسه مقابل یونیون برلین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106832" target="_blank">📅 22:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNNPm40H2JfqufdYdUn7ssHANL-VJqSmPnPcQwNxqxYSVUT4YwKZvZ3BKLcBxlh87WFTs5FiB5m02OVR4sAEK0hjXyA_LqfgZqN93o1-f9vPx2NvoyToR1cazV4Br8vPSj8wvaESHV7C3Kf8dHs4hwvNLgMaQR3fkB-FQ-QHfa7HXMVNoz6E2fbH1odEiBuH73MwWNIP1K6xANTFKtuFYxxpzyLbH-LXPib3Nu8H4QS-f96iEIvdS0lW4jCzBXaSHYIYitXD0gViic9nxE1s0-R9rVMNMLUq2VNz5t8-9DP5FX4E1YyOX2nweU4o1c5EUN23xxkDKH_er7jE1_5k0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
🇪🇸
پس از دو بازی غیبت بدلیل مصدومیت، آلوارز به دیدار یکشنبه مقابل رئال‌مادرید رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106831" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRV29eaRiQXVl4YZRWauTrBqRvc8kkRFVWVblvgsSbvxSGHH0LFDZ-ZYudBzF_0adP5SJx3eI-z9wtBUsCRycLhFP_ETlTu7K39w0yeXoVb9nvPLtPKMaRliFVz-81maFUhOISkK3UMjyEorgGWs8BoenMg_eN5VmfmeZozQGbM2__rvZgcYMJFh53LPZ0C6i7kPhVJJlVzQ_5Hy2h0grd5MoSSedBwAF7GYSoutumE-sepA0IfgYcaW-NStnZJN-V79kTTF3ubrId-hC5nDteLrXu2BXqB-bMyzYsdKeqRlagQD7JNg_O2a-B-kDuvWIVV8LuZBT1zcotTMaaHA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
داکنز نازون پس از عدم موفقیت در بازگشت به استقلال، راهی النصر لیبی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106830" target="_blank">📅 22:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=OxnjK6VK70_6_59fOLOUpLlz__MXhQcvAudfR5IVG9HFKzR2zhBdgvnnoWU2IEwrNiiEudnr08qnDd1IWS1mXd-3yENEnIwx489zQ1evuhhPkSyjOMWNVnbdajOh8t5fSjI7JOgT2SR4HlXw2yUE6zoRkCM72AU80oA5hE1aQfgYPa9ZZEVWOHSOdGJGZdxs3mbt3p3vJLkpz7bLlxgk64RFTAhmuRO9giSAAwtSlZEcn3zrKUi21MXNuVKu4AL41guovzpLMSj32RbpEpu38ZM379S7JcefNCzcEMX9_fkbxQU2yW-j5sgSnhddzF2RFDcqxoO2_TGR8WV_FfDN3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3aa9abbc6.mp4?token=OxnjK6VK70_6_59fOLOUpLlz__MXhQcvAudfR5IVG9HFKzR2zhBdgvnnoWU2IEwrNiiEudnr08qnDd1IWS1mXd-3yENEnIwx489zQ1evuhhPkSyjOMWNVnbdajOh8t5fSjI7JOgT2SR4HlXw2yUE6zoRkCM72AU80oA5hE1aQfgYPa9ZZEVWOHSOdGJGZdxs3mbt3p3vJLkpz7bLlxgk64RFTAhmuRO9giSAAwtSlZEcn3zrKUi21MXNuVKu4AL41guovzpLMSj32RbpEpu38ZM379S7JcefNCzcEMX9_fkbxQU2yW-j5sgSnhddzF2RFDcqxoO2_TGR8WV_FfDN3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف‌فروش آیفون ۱۸ در اولین روز فروش رسمی‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106829" target="_blank">📅 22:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106827">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijWllxATk5l30YkyyfSE92md5WKpO4ASNQgQA5SzueNVjjAtzL4lmpq4DcoRph6Qi5QiQAQIdhl8wjh41zp26WLu66iF60b8b6yr8Qlu7UUeZfYXJxFqnA5tGC21j_nT3qj7AA62zwCpws5pY0vWZfaLshKFwoiJTj669kHu4ROLYcim0nAF3YvEkRYgcLcKzc-491KaWCKHvQgMIVsuL_o33NdiSnJHxdapcNaQGpk_s5qx-6yRR1C_1--EsilSqxvCtFv2nn7WgklkNEtBbNQDCW5-uHiX_Hkr1KQnsdJC-tLhdO9ilDCfr6PXIrpwnUUgr7JZ-i7vvbKeEYYT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5jRXdSkTMW6vLg_91DvVuwIlZL_BR0JwhU1nw-EOOYyV4kOKs2FFl9pNGxTFyClfDIctdbhXbBwHJ01JoNNQUyV2z87fnmeyHhsuJH-d9Da0UL97TCF6YIga4RlriyuqaHrhkwFs7pf-8_AIxusp0Yi25Rt5ogfUChx06WmGDdldXw2lj7HLP7Y6wZWREJSIdX0ql3ez0IoDMPTdj8mbF8z47sn1PtGFfQ9gBw42ze0sC3exs8PSY22Ty2ieGeMAu7ezvcdr3IP717DsgCbrBRt0XmV2iVsMbymtF6sYlu7QXFQPl1z99CkeItnHNXJCFfta4iNasXzsoLXYZDGzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🗓
سه سال پیش در چنین روزی
رونالدو برای اولین و آخرین بار اومد ایران و دوتا بازی بعدی النصر تو ایران رو پیچوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106827" target="_blank">📅 21:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3rczYX7rR11wEGJeAi55bpySc_kGtlk-puybZ-Y_V0windFmNSBQ8fwvQzKztMW_V_REOltkd077-DUyhhBNYf4X5Qrk0BQ-2tZFryvwpneDT6pg2JfrObxIAPaPjJPlNIsv1Ghe0ptdwyzZQH6N8fc1_-Segne5MZebqxO9n93tBVe1E4bSc614ANIy-a_Mgf_3MQooar6pbzCWDMk8EiQ-yf3cKRfkhmxf90hdONNGAjbfYiMvxFCZaWSQuJ4N0zZseoIrbi1X6Uv46914JGN0hkEpDhpwtg8J1FjnDrn1XZUdJel4_XRM0EBRJXtitYkrU6fR4BCUQ3UzBQwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب بایرن‌ مونیخ مقابل یونیون برلین | هفته 4 بوندسلیگا 2026/27
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106826" target="_blank">📅 21:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106825">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQfI7QRsoJS71mcqfra6G4essWr-TIp4WQ9vDmXtBsCl1kj2-PwoPIMbHy-g7B2M6ylW-__zuzlXWW4Ol2qUcbespeGdkckegIpo74ZXWxlG5Cy1H_2COfVGeLUh5GPeau6cvDN0zolBe6YCKru2cvaDWSoenas5ND2kOeaLix4sy-OLs90PZ6shflK96azvDjUXHahYdmZNXSvt1tQuhJHKSU8iL_nJNc880xDG3Wph17PI_CsodoJQaCmgqEsgu4srKz_v66sAUHbQ1GRs8h1PeNrsCe8mwzV4stRY9cFQdjsTLCInjz8xXqO0CayEsqCFLJRifcYDPnAYu5yuZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇹
لیست تیم‌ملی ایتالیا برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106825" target="_blank">📅 20:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106824">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa894a6b5.mp4?token=mxKfjXCHnw8YgRzlcCAFht7zh_-ZCcDb6Oo7ZcqZ6x3VW1XJwzJAqBbVarP1E7AqqNkW2nOfE_sVIIIVh366cttX5YJUWIQul84Ch963yU7ZN2uL9qqZsvwSoN9cFPflH2rg5CXB-2gUWUpM7CS974u3aHLYh_6tw_P_c3-Ecqo44OygS8xyBcbf3mwPQHtSiHkUAWsGo3JEP0rSYliWeEaSPFmAmEF4NAzhfb0lhKAwnFRA8dvxQpvWxIZfYjFF95mRLP42Ec8zdNd-R5jn1mY4hww4FNdZ_wqJ-j6uBKE0zS9CaYt0oZZ3FeznHhEmv4sNSIyh5DnVSGrL065AVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa894a6b5.mp4?token=mxKfjXCHnw8YgRzlcCAFht7zh_-ZCcDb6Oo7ZcqZ6x3VW1XJwzJAqBbVarP1E7AqqNkW2nOfE_sVIIIVh366cttX5YJUWIQul84Ch963yU7ZN2uL9qqZsvwSoN9cFPflH2rg5CXB-2gUWUpM7CS974u3aHLYh_6tw_P_c3-Ecqo44OygS8xyBcbf3mwPQHtSiHkUAWsGo3JEP0rSYliWeEaSPFmAmEF4NAzhfb0lhKAwnFRA8dvxQpvWxIZfYjFF95mRLP42Ec8zdNd-R5jn1mY4hww4FNdZ_wqJ-j6uBKE0zS9CaYt0oZZ3FeznHhEmv4sNSIyh5DnVSGrL065AVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🎬
👍
پدرهای عزیز به این‌دیدگاه عقاید جالب علی فروتن حتما گوش بدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106824" target="_blank">📅 20:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106823">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed690df00.mp4?token=XB7WZGkqnxKroCXhrGEmXydzNSPes593IZbtOF9aFY7I7uLDSofiH5r6cuC6OXfWiZsYcnI5xgH3x074M72BSuWfmV4xZ3KSbH0z6TRLXaQ-fEhYs1VnN_yOdjxMDZbbkVbTkCibp8izraW4XcLJJ1A0oD8-rRENW8ZtS-Q4jJygrxxrR4sWZnTJCGcIXcvpaRKH70TYZSk8MPg2-kw53U43RolxZeTOlbgutLaf52GgHz8cDJaLh9LltR-4g_HklVDa7C3ee_aLEIhnaf5-PrdNXIJDJWkEkh9Y_oA4Cyzen5sjKWL9cR53Q9TLqHneMcg4DNPXHVgE5vzUUmPnkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed690df00.mp4?token=XB7WZGkqnxKroCXhrGEmXydzNSPes593IZbtOF9aFY7I7uLDSofiH5r6cuC6OXfWiZsYcnI5xgH3x074M72BSuWfmV4xZ3KSbH0z6TRLXaQ-fEhYs1VnN_yOdjxMDZbbkVbTkCibp8izraW4XcLJJ1A0oD8-rRENW8ZtS-Q4jJygrxxrR4sWZnTJCGcIXcvpaRKH70TYZSk8MPg2-kw53U43RolxZeTOlbgutLaf52GgHz8cDJaLh9LltR-4g_HklVDa7C3ee_aLEIhnaf5-PrdNXIJDJWkEkh9Y_oA4Cyzen5sjKWL9cR53Q9TLqHneMcg4DNPXHVgE5vzUUmPnkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
مسابقه دوی نیمه ماراتن بانوان که امروز در بوستان ولایت تهران برگزار شد که حجاب شرکت کنندگان بدون محدودیت خاصی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106823" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106822">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7o73LYtyPoSbY8I5eGPCiviF-5pzcRAHnNsYtUsDINLm2Dc2cb0fquTXMC94zAgpk8aueiN-LlV8eoJ6-MkUqPHq949HHCYswnuWsR_mtaO8q-hIa2T1wahUpwMtectGxPoNOHMf2OV8RN5bUQ88v7XOcfDQ1lIAbvi8dMQUiqgm8KkOELelE1XzkOfIrzZazkc2Bp1t9BDRUGGpXVt1Xm6CehmMFN89LC8j_lXPwWxXrS8BW1zDWerfbpH1_v022zqhZsjB61Phw5NuXUQCLaGApfz_cjo_yVzgDmMQ7cU9_7E4uOn5dTiMYfXZQRieIwz3KcaPhKRk4GDtRw52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇫🇷
لیست تیم‌ملی فرانسه برای فیفادی در اولین حضور زیدان روی نیمکت سرمربیگری خروس‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106822" target="_blank">📅 19:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106821">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69347998c.mp4?token=ibfEupiz7dFa37YXwmlUjJV6D4Qbe0jviSl6E6rV03ifRGWEvSlfW7O7xr-6BoDKzZIdzKd78mBRkDNDjkayA9rzVEc2TvOTousDkYuQCYIUitDeSIBNDbtjw29PUobHluFkxI33U3Iru9VkJA1glYkOGR8hyyabpJb6Gj0qFMJBHPCQSH9gxQY0G_ALyJyUAvOe4BqdpsxRqYyMGFgq_1lBpR8wY4C1COb8kusG5hRtXBtrA4Metlbhq75S_LQGMmdVDQNZGu0_d-MJT12NTzAZk8RdWORuuOZma-ow9nrYN_OB0ANk4-FnutcLqCax1I--bwajrv1GupYfg0ncAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69347998c.mp4?token=ibfEupiz7dFa37YXwmlUjJV6D4Qbe0jviSl6E6rV03ifRGWEvSlfW7O7xr-6BoDKzZIdzKd78mBRkDNDjkayA9rzVEc2TvOTousDkYuQCYIUitDeSIBNDbtjw29PUobHluFkxI33U3Iru9VkJA1glYkOGR8hyyabpJb6Gj0qFMJBHPCQSH9gxQY0G_ALyJyUAvOe4BqdpsxRqYyMGFgq_1lBpR8wY4C1COb8kusG5hRtXBtrA4Metlbhq75S_LQGMmdVDQNZGu0_d-MJT12NTzAZk8RdWORuuOZma-ow9nrYN_OB0ANk4-FnutcLqCax1I--bwajrv1GupYfg0ncAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد عزیزی: دچار شرم نیابتی شدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106821" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106820">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854ffbdefd.mp4?token=FY2XADmLY8YXr_FRJH365Ai8v3SEuvgefw4y7e1P1S1zQV6EJVjonl23yr6Mu0WMSX9jxdVNa2jBM9-7MNY2lFEVoemCEmoalLlexLGOwwE2uNmbjXTw-3kQU9qn49XbRDAURuwYvghU05guf7okRG0zgdAgqKonpjvxDiktt7g_mIoboWaWPmhxN8R7mv73pdYmsyr8e8RKhtsx2AKHJXc2zUiOTxtEwrRvvRGqYsQ_X_auWIl7rthW6xlX8F7SLnzYVibFAqCezZZ50kyOkS3Hj0W0C--6XZpxDLwfA9JaCOnItIpfGInFxksT6JCFFkGhTlt_umjBZyCBNxyi0lcuXqTWBFyabFyXWeRdo7P2aOYXAms_LzS4t9E2dvwyRFm3t2jF6Y-D_Mw3HwKjD4SDMgh4KsN0Lxr9LA8ANU_fUa-g64PVfSxK4rFRBnyK4hlLlC0c3DkzUFhTJsn0nRDuuMdQmCRh9sflFk0rduAu6TmdKRnjVAelH4nk4_AudEXs2KyMAVkklZN7nDyJgFNHZv99i7SZUZmnad8pik7GiPXLZ1mrWMp9_ws3Wu_0YixIVe7XWLW1xRaeMrNdL-2LBO2EQz2U3ABzxpLLxOedcKclHCm5TJpjwP0sUUhcnD1oses6Y4ENt2DIDu73MlhkbAqwMqpYX-K3XICpxHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854ffbdefd.mp4?token=FY2XADmLY8YXr_FRJH365Ai8v3SEuvgefw4y7e1P1S1zQV6EJVjonl23yr6Mu0WMSX9jxdVNa2jBM9-7MNY2lFEVoemCEmoalLlexLGOwwE2uNmbjXTw-3kQU9qn49XbRDAURuwYvghU05guf7okRG0zgdAgqKonpjvxDiktt7g_mIoboWaWPmhxN8R7mv73pdYmsyr8e8RKhtsx2AKHJXc2zUiOTxtEwrRvvRGqYsQ_X_auWIl7rthW6xlX8F7SLnzYVibFAqCezZZ50kyOkS3Hj0W0C--6XZpxDLwfA9JaCOnItIpfGInFxksT6JCFFkGhTlt_umjBZyCBNxyi0lcuXqTWBFyabFyXWeRdo7P2aOYXAms_LzS4t9E2dvwyRFm3t2jF6Y-D_Mw3HwKjD4SDMgh4KsN0Lxr9LA8ANU_fUa-g64PVfSxK4rFRBnyK4hlLlC0c3DkzUFhTJsn0nRDuuMdQmCRh9sflFk0rduAu6TmdKRnjVAelH4nk4_AudEXs2KyMAVkklZN7nDyJgFNHZv99i7SZUZmnad8pik7GiPXLZ1mrWMp9_ws3Wu_0YixIVe7XWLW1xRaeMrNdL-2LBO2EQz2U3ABzxpLLxOedcKclHCm5TJpjwP0sUUhcnD1oses6Y4ENt2DIDu73MlhkbAqwMqpYX-K3XICpxHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
دیوید بکام: "من هنوزم باورم نمیشه که اونو اینجا تو میامی داریم و داره واسه تیممون بازی می‌کنه. همه ما دلمون می‌خواد لئو تا ابد بازی کنه. هیچ‌کس تو 39 سالگی همچین کاری رو تو این سطح انجام نمیده. پس حقشه که کاندید توپ طلا باشه. به نظر من که باید ببرتش!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106820" target="_blank">📅 19:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106819">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dccf6f34c.mp4?token=GbS6W1ualySsZ0qhnI6z1prVicqM_iIuZyC0CFcpDqK6yBYShcNmGUGE_GqE41hp_n-oW_Ai0WP7tIXU5v3vId-erdyKaOmdUAAuqy2rpVm0S32o0ykqWD23U75skgWRtIbvfph9XWgEIoWdujywa2mgeuCAVqfs26EJssPMa-n3RbSgkBDh7hdpLV_QnBldp_FkBhdSQzSKP92cjJmx3tpTxGpMXAJ5wQoJqNBMd1f9wLIRjbl4CXwJa-2LEudvGVdkw3Huf7jyEVLiFwxUOt0Klq8znAc2KQ8d4XI1NKAh93HpOMAMNLT5x1KlcMsP9e8BL1qC_T-qIZEFSIGzq04yrqCiocIBxCiT5HSzpnybgIeanfvy_3KjHpRhqHPNp_ETJtoE0JcfChpbSaLWKd0bU8GADrTYJwBwmSEXMjCqzfXHunIAltVVTOqT5GRhyMwBBIMNekkWLpxEQQfOvpckZKk865Qr4CFs7HfyvXlKKTJDsOn_LqVs38YZmmYA2p1oogXQiM_s2b8CvT2H67v9AXiTa9BtUlkpvKcqOxFJnalBGdSN-AUj7BX2hbpRK5yC1XlIcSfzJ96xYBgVW9BjRzWhJN1yV4NqcCQyweB-dD0tiyCIx8zmBmrvuIMDoaKQE60dZ6Gj7Di3JdWFckmiz3Ot5D0SZCfsGzx9KYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dccf6f34c.mp4?token=GbS6W1ualySsZ0qhnI6z1prVicqM_iIuZyC0CFcpDqK6yBYShcNmGUGE_GqE41hp_n-oW_Ai0WP7tIXU5v3vId-erdyKaOmdUAAuqy2rpVm0S32o0ykqWD23U75skgWRtIbvfph9XWgEIoWdujywa2mgeuCAVqfs26EJssPMa-n3RbSgkBDh7hdpLV_QnBldp_FkBhdSQzSKP92cjJmx3tpTxGpMXAJ5wQoJqNBMd1f9wLIRjbl4CXwJa-2LEudvGVdkw3Huf7jyEVLiFwxUOt0Klq8znAc2KQ8d4XI1NKAh93HpOMAMNLT5x1KlcMsP9e8BL1qC_T-qIZEFSIGzq04yrqCiocIBxCiT5HSzpnybgIeanfvy_3KjHpRhqHPNp_ETJtoE0JcfChpbSaLWKd0bU8GADrTYJwBwmSEXMjCqzfXHunIAltVVTOqT5GRhyMwBBIMNekkWLpxEQQfOvpckZKk865Qr4CFs7HfyvXlKKTJDsOn_LqVs38YZmmYA2p1oogXQiM_s2b8CvT2H67v9AXiTa9BtUlkpvKcqOxFJnalBGdSN-AUj7BX2hbpRK5yC1XlIcSfzJ96xYBgVW9BjRzWhJN1yV4NqcCQyweB-dD0tiyCIx8zmBmrvuIMDoaKQE60dZ6Gj7Di3JdWFckmiz3Ot5D0SZCfsGzx9KYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انزو مارسکا سرمربی سیتیزن‌ها:
🔺
تردید هوادارا پس از رفتن مربیای اسطوره‌ای طبیعیه. این شک و تردیدها برای هوادارای منچستریونایتد و آرسنال هم بعد از رفتن سر الکس و ونگر وجود داشت. برای هوادارای سیتی هم همین مسئله صادقه، چون پپ هم یه مربی معمولی نبود. اونم مثل سر الکس و ونگر، یه اسطوره بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106819" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106818">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106818" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106818" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106817">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXhX1l9j-bnU_DMxqsxokOy18-6zMdjPJh9u9RbG3QH6w3WRb2HUKdwTY2SgOVIkcJAR36M3uA0TcVhRR4dOxxjC6jxO2TR_cZliuP4RuLDNeU5Y5TVaHVrUTd83rOcujm_Xn2KmBXPsIkD_CRz7P9gXQrSUt2fxrB3GokOprD9ukiK2MXimXdhkTj6Qaz_YdAaUo94T7AQibntuNhC2s4Q_u2g-HqTipCmzNqmrKeFw7x57TvcOrgw_ZVbK6doGGLVXeL3aGthUaQsRI82uybRVUF1tEF-KMZWCf76FJQgC10IK_textRvX5fWB0hxREkhQnHiDbvhA4Ze8TggqbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106817" target="_blank">📅 18:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106816">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabf7dd06b.mp4?token=XUeQYuz_LpWUmmXehlyZoQTExw2_6YQNPdr7HgPem7GwAYlAnskIvNhyhB1jZDBWRg90SP7Q07HFYt3iK2xxKO_gqdLrbQV3yELclPt4fglMER33x29pdn5PkqmQHE8dsdgJQ1eyGNDlOwj1khLDXbZgT3t-oCq1ZRGYWq53IyXJFPRI5e2OHwzxHEi8WvVwMgLWds7cSXA9Yqp4PaSrc6nm-qfeqNCAjxvVxHd2oKScbI2JMcvxO27mubTzevGLCt3jFIuYfiykEFwGqFRx3ihYWXSaR7umBGpEAddLK1HZcj61dAJUtf37zd7DfVlRTUAf_5NK7_xI0pmDRygDow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabf7dd06b.mp4?token=XUeQYuz_LpWUmmXehlyZoQTExw2_6YQNPdr7HgPem7GwAYlAnskIvNhyhB1jZDBWRg90SP7Q07HFYt3iK2xxKO_gqdLrbQV3yELclPt4fglMER33x29pdn5PkqmQHE8dsdgJQ1eyGNDlOwj1khLDXbZgT3t-oCq1ZRGYWq53IyXJFPRI5e2OHwzxHEi8WvVwMgLWds7cSXA9Yqp4PaSrc6nm-qfeqNCAjxvVxHd2oKScbI2JMcvxO27mubTzevGLCt3jFIuYfiykEFwGqFRx3ihYWXSaR7umBGpEAddLK1HZcj61dAJUtf37zd7DfVlRTUAf_5NK7_xI0pmDRygDow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
فرشید اسماعیلی: دلم میخواهد دوباره به استقلال برگردم و دلتنگی شدیدی دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106816" target="_blank">📅 18:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106815">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbRncL5NdAttvapoHGsdAKgk2MAhQMCx2qFleTGJZlXk6i1ZBKWyDY3uZcvr9V2TXGp6VPseraz1iZRF66wZFlXKHLUTvSOetDUaf_WJFA60EZwSy1CuQ_A5y-IDo0qUvGBBtqDD-ypnhfl6hOCrLJOwBR1gBah7cnL5rv8Cw7rn9fBtpvaNePlIsvW41EALtphI6qRltu4sVL6QTCfb1EjIpKCPG9-3NbBeUgEg-Ksd0uuIYgx73PSebLDfcD8FoGR71dCWzpxUUS3UC7vn8rqgurFcnhWlhieHtx_c5Qvco1xTMgvgbqqSH-6XQ_Rc2Ey9BFqGMsXRZ60hdkTf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
لامین یامال: من در تمام افتخاراتم از امباپه پیشی گرفته‌ام. به عنوان بهترین بازیکن جهان، شاید فقط دو نفر باشیم. من فکر می‌کنم که امسال شایسته توپ طلا هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106815" target="_blank">📅 17:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106814">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd6e64a79.mp4?token=iPfT0d55IrtBfaTawpy6l1EfRbop8OhGR0QjNfzWES00MUI6jCJWDP60RMc7fuQw2pBdAeiOSoFqrhhoa-oq0soqvbmUQ-pljaa2sA6ymqXyeCO6EHUdzSKGfm5IKg63gAfrFmDq1BZyof0rSNIMWQ54IBlcj10JSyluW5dEvIMZy1pC647htyVBqBvofkavxHzFBkH0DxTlYrzRv87dIukLv789Y1Zycw3iSiHcSzygjWMuJAYGtIN9PWeyLCD0aZGIV-_0fgoL62AeAL4maWb4Tp4DFAbFMWz8VPO0BFTfrblpFYvr21iY62fmW5nCt39gI2KO7oFQb_KcoAQTkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd6e64a79.mp4?token=iPfT0d55IrtBfaTawpy6l1EfRbop8OhGR0QjNfzWES00MUI6jCJWDP60RMc7fuQw2pBdAeiOSoFqrhhoa-oq0soqvbmUQ-pljaa2sA6ymqXyeCO6EHUdzSKGfm5IKg63gAfrFmDq1BZyof0rSNIMWQ54IBlcj10JSyluW5dEvIMZy1pC647htyVBqBvofkavxHzFBkH0DxTlYrzRv87dIukLv789Y1Zycw3iSiHcSzygjWMuJAYGtIN9PWeyLCD0aZGIV-_0fgoL62AeAL4maWb4Tp4DFAbFMWz8VPO0BFTfrblpFYvr21iY62fmW5nCt39gI2KO7oFQb_KcoAQTkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نظر ژابی‌آلونسو درباره مالکیت جدید چلسی که به یک فرد ایرانی واگذار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106814" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106813">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpZ1fUpg7J7QP6wMVPsOZHohmpDYha3e5HuLNctq8QXfSHz1vTGm1P6BqUhFNRP-6Byms5iZqcN6jUCpZO5zmVNSivO8M6fCbXP2l3NlQzqsn3ERQs6xXYYsg1t4C8fcATtMZMJpn3hcm9m4J7Xjqp6jW9vZB9AQbceANqL7mh76LoKrnwMLncSqsPkUNviznHJLu1PMxjWqsfCWgaU8lnBa_AiYJz5RDvI8oKecosSC6NA2ior41Zg9X0aWB51HTTrE1PArRGIBZ0Y0jDiA6vWhGYpXb55I7gwksW_083vhiNSfIzGygugofb1E2FBovW_rvAQjxnuG3-Or3tPO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رافینیا: می‌خواهم قراردادم را تمدید کنم و دوران حرفه‌ای‌ام را در بارسلونا به پایان برسانم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106813" target="_blank">📅 17:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106812">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac9522ee8.mp4?token=aWq7vfPHqFMmfpDeyFD54U4GNkq_q2iISjeUcd-ItKPDzUGw6kPV75Pw3ayVhslC_iDvBmc4cjBn44wVeSPYpKJILIucZl_B-VCo0jJQ-qAyo0fz9ZollP69r2pUdXE5Fdxx9icRO6RWeH_bwSJ648kXGaH9uiDqg0MTOB_8kqSTaNRD5gF5fuqJv1vl7rAylFt39u9p10tN7eyyIQYqy0T9ERiNP4SS9GEMQJp3wSRTDSnT-f2XFRt2lKc-W8_lTJrRdZCcnvCYdenlNtr9ddfJED-M0R2kEsAlc2aKuxWRSjN7bRrZ3_NB7KD6Wft36gtrWTeSs5X3BSzaFqqggA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac9522ee8.mp4?token=aWq7vfPHqFMmfpDeyFD54U4GNkq_q2iISjeUcd-ItKPDzUGw6kPV75Pw3ayVhslC_iDvBmc4cjBn44wVeSPYpKJILIucZl_B-VCo0jJQ-qAyo0fz9ZollP69r2pUdXE5Fdxx9icRO6RWeH_bwSJ648kXGaH9uiDqg0MTOB_8kqSTaNRD5gF5fuqJv1vl7rAylFt39u9p10tN7eyyIQYqy0T9ERiNP4SS9GEMQJp3wSRTDSnT-f2XFRt2lKc-W8_lTJrRdZCcnvCYdenlNtr9ddfJED-M0R2kEsAlc2aKuxWRSjN7bRrZ3_NB7KD6Wft36gtrWTeSs5X3BSzaFqqggA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
بابک مرادی بازیکن اسبق آبی‌ها: یک کیلو و ۸۰۰ گرم طلا بخشیدم به استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106812" target="_blank">📅 17:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106811">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45512a16b8.mp4?token=HssiTpfri-KT4CT5v_ivXzy7hsXzDiaD5BGEjeI6HuZw3bOpb1KC5yVfa0tytPSw0zs_wccEBLHjAZWOnysZDEoaz1V7A-TKX5MyhyvdDbge5-QrTw3AxvtigLqgPEvWzC-hjF6tO1ReU_Iga55V54E_kWOIJbyzC4dVLNmG4fnlzJQ4IbHvo5of-Iz4ww3NJTVgroKvonBNf2138tzdBlNwDRrGAZ0rJlvINlhrxdGWsTbR_kzwBzn6c-xrOV-vEPb9uuf25Xhwgg-c-XJN5L3FyTiE_1LkL9lI4a86S7rQrAwxl62mTT1FKjy0clHSYF7SrneuoL1tURoxnDm8doWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45512a16b8.mp4?token=HssiTpfri-KT4CT5v_ivXzy7hsXzDiaD5BGEjeI6HuZw3bOpb1KC5yVfa0tytPSw0zs_wccEBLHjAZWOnysZDEoaz1V7A-TKX5MyhyvdDbge5-QrTw3AxvtigLqgPEvWzC-hjF6tO1ReU_Iga55V54E_kWOIJbyzC4dVLNmG4fnlzJQ4IbHvo5of-Iz4ww3NJTVgroKvonBNf2138tzdBlNwDRrGAZ0rJlvINlhrxdGWsTbR_kzwBzn6c-xrOV-vEPb9uuf25Xhwgg-c-XJN5L3FyTiE_1LkL9lI4a86S7rQrAwxl62mTT1FKjy0clHSYF7SrneuoL1tURoxnDm8doWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
چرا فیتیله‌ای‌ها دیگه پخش نشد؟! افشاگری عجیب علی فروتن از سکانسی که باعث توقیف برنامه فیتیله‌ای‌ها شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106811" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF4y4C2v6USDiZNVMhlaahI7kbRglkYFHYR9j2OQcxD4LD3UvTgqnfsb1c-yoohvi-4gFSEgYbwgfrA3xB8g612a-p9cd2Ge6azZsYghTBhO-WGfjTMYABpdQgHUuuRyMrFYNdp_SfJDhATrUwsL1ibAoXj4Q17As9J2imKvizTnRcd8vAg36OfbjBnofX9LiRQswig7mDe7vT8JV0tk80utdYgl5Hghz9A-zLpI1MQWwDQ4iDQSuHrvOtQJxVI-8DJQRvihNSjLshAHzu7c9zbz_HpqZxT0LBU7Hd7l4a4h3XXtw-OIbCl0gyTDWElSbpMVCDZYfurmt-3GucYqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
۵ قهرمانی لیونل‌مسی در ۱۱۵ بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106810" target="_blank">📅 16:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106809">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171fd833db.mp4?token=SvIEnc-F7gzgljhSFmeqW9wVBVCU39MdwXLmDsAXc-GfOB_W1iEWYNjd2BRAu4yW0u36WA5WqTXx01T32rd85t6P5Z3g0woEpkQLWzTKFpuUXxFDcOYGFkl-ETjsOUWem91x40Jmfa6HaIqOrAnWeKkg03ngZUAFW982Moayc1FOu6G5l9dCMa1p6LvpUOgaz_GuHUpw3rdiwcJRGp5Fe15PxCWWLk4RQwA3mfEQ7QBmsLZGLlv2YD6SUCQEEpl6Fp5VNazfcBLWR8boevPqoUs0nKH7ZHj0rXDG8ZOGtvD6fOQZ2C0iai7Uxnn81ztoeMZX2ugnI_aEy5ol-vggHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171fd833db.mp4?token=SvIEnc-F7gzgljhSFmeqW9wVBVCU39MdwXLmDsAXc-GfOB_W1iEWYNjd2BRAu4yW0u36WA5WqTXx01T32rd85t6P5Z3g0woEpkQLWzTKFpuUXxFDcOYGFkl-ETjsOUWem91x40Jmfa6HaIqOrAnWeKkg03ngZUAFW982Moayc1FOu6G5l9dCMa1p6LvpUOgaz_GuHUpw3rdiwcJRGp5Fe15PxCWWLk4RQwA3mfEQ7QBmsLZGLlv2YD6SUCQEEpl6Fp5VNazfcBLWR8boevPqoUs0nKH7ZHj0rXDG8ZOGtvD6fOQZ2C0iai7Uxnn81ztoeMZX2ugnI_aEy5ol-vggHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی نشون داد پَرش و ضربه سر هم خوب بلده.
😮
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106809" target="_blank">📅 15:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106808">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=ULWw9Kbt0FKnmIaz9-yjwIWrZI58wQInkKYh9SXFU78fGIlvtRrm-UizFhJBIkuOudM0EjwogY1zPmMGNJMBIl-A2BkF6hyq8czVJ61yoMfXcl6uSZxjhYbjXaMsS-2bVPK1OPQXCkX4IIXI8dkqUpblQX1-LLjFdtlKAruhM4VXcYppss0aOnUmXR9FoSeIDXp1KxPptvLsEO3CAhxMehXyZPE0M-O8Xf2BAnoc-sZAzzf7x-H6qJ-PxWrUKOKduqIDn0vdrY9NVRLnLlbmF74qcbWuOev2tgHeHk0cFGTn60QQ1Bp853-eYdbJzrmAp8UJstWv91v8R8rrF305Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb5c6a4f7.mp4?token=ULWw9Kbt0FKnmIaz9-yjwIWrZI58wQInkKYh9SXFU78fGIlvtRrm-UizFhJBIkuOudM0EjwogY1zPmMGNJMBIl-A2BkF6hyq8czVJ61yoMfXcl6uSZxjhYbjXaMsS-2bVPK1OPQXCkX4IIXI8dkqUpblQX1-LLjFdtlKAruhM4VXcYppss0aOnUmXR9FoSeIDXp1KxPptvLsEO3CAhxMehXyZPE0M-O8Xf2BAnoc-sZAzzf7x-H6qJ-PxWrUKOKduqIDn0vdrY9NVRLnLlbmF74qcbWuOev2tgHeHk0cFGTn60QQ1Bp853-eYdbJzrmAp8UJstWv91v8R8rrF305Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
اعتراض تند رسول خطیبی به حمید مطهری و تیمش بعد از باخت لحظه‌آخری فجرسپاسی به فولاد در اهواز
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106808" target="_blank">📅 15:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106807">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4hgHh6j4YkjQAnaaCDHk-pHwPQw7DcslG69M-B82zNm_go41Jw3mKyeapd7jBTOuwDuQiC5eoXQqSnE4PsST55H29IWbhYFhBIuK_OA5vtI_5RFa5P8XCb-SZ6TZ6re2YpluCzvJ5hjbBpx0vhiADlMt1aABZXGIxL3otSA2vCzE3E5P9n02QQvFIr9XhVkq95i__YrrvKJ09I0dLUgqVh2UllZd92itHevmUtu2MqQr7wcZPy2T3mjLLVflPup08hWoWtI6nDTV-e7beWWMoD6ICQ_grPQkd3W0xAvtGn_xcJJBNtARTMQPC43VbzFmpQcJqeG5tjEbGKCZ96kKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌐
گزارش هیئت مستقل حقیقت‌یاب سازمان ملل درباره مدرسه میناب: مدرسه یک مکان غیرنظامی بوده و در عین حال این مدرسه در مجاورت یک مجموعه دریایی وابسته به سپاه پاسداران قرار داشت. اطلاعات مربوط به مدرسه در سامانه‌های هدف‌گیری و بانک اهداف آمریکا آپدیت نشده بود. هیئت این حمله را یک حمله کور/تفکیک‌ناپذیر اعلام کرده که موجب مرگ غیرنظامیان شده. بر همین اساس، هیئت آن را جنایت جنگی تحت حقوق بین‌الملل ارزیابی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106807" target="_blank">📅 15:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106806">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=Cf-M-EAxhg5ZaIn478vx0IDyRL6PQcI-0yDg2ymcj3P3z2VuR-m8JTVkCLRJTvcg0Zk3qimskWC40Qh-cbWB_aFk_VjYE9GkhDp49f0gVg4p33VFmKpzwn4tBA_XJ29yc0mvC3kEr0zjJXiKJS6xMS9PJ4OWRHYGmHVXwllSqINgNwm6uHSXl-93wFZmHPsr3xfRJGS6WFnnwlKODhgsCw_xijDFqqGLcH2rEzQpETf4oOAhdFvT37cPP1Gy0vM3_Lw1N1Ejv6YQkcs-v0YHSlFKAshjIdvq46yCcwLyFSU9v5J06GdK7r5_EIvTE_AANsokhen3BehPJh_MCps-nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40dc07061.mp4?token=Cf-M-EAxhg5ZaIn478vx0IDyRL6PQcI-0yDg2ymcj3P3z2VuR-m8JTVkCLRJTvcg0Zk3qimskWC40Qh-cbWB_aFk_VjYE9GkhDp49f0gVg4p33VFmKpzwn4tBA_XJ29yc0mvC3kEr0zjJXiKJS6xMS9PJ4OWRHYGmHVXwllSqINgNwm6uHSXl-93wFZmHPsr3xfRJGS6WFnnwlKODhgsCw_xijDFqqGLcH2rEzQpETf4oOAhdFvT37cPP1Gy0vM3_Lw1N1Ejv6YQkcs-v0YHSlFKAshjIdvq46yCcwLyFSU9v5J06GdK7r5_EIvTE_AANsokhen3BehPJh_MCps-nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✔️
▶️
مهمترین اشتباه در محبوب ترین حرکت بالاسینه؛ به توصیه استاد هانی‌رامبد عزیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106806" target="_blank">📅 14:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106805">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGSF3BCzefs6aWLecYY9QQxQQjpepnqNrNTiXERdCvK9U6PT2r09FaxbXXhYP1wqrik_PJ1IbO5yYnU8Ar7sip-xdvxahtkwYMAnVc8d4eIBnGkmLeYiTbjtXYiy1VjyLol2Cj0ckL670E56l97TyXlczzSqYY0eM5rSRoJhX3jbHQtJ9LbaoZdZhDeNornCMZCAwUYC5RakYFsvvaM7zqgflTEtJqkZLXmZdOcMufP8Io8O9_pk8zDUx6FPwIVj3nOxPOPRc7Bqof0yVMv4eEb_X_XShfXlkNJDrsHGn75M2PCYFTY8hXDf_SMgFW_3SBAQTzbXouckybFmEMSXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیبو کورتوا درباره برنامه‌هاش برای آینده:
کار من بعد از خداحافظی از فوتبال؟ شاید کار توی بخش مربیگری دروازه‌بانان رئال مادرید و ساخت یک آکادمی درجه‌یک تا به جای خریدن یه تیبو کورتوای دیگه، خودمون یکیو پرورش بدیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106805" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106804">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTVlMeGVCh13ZHvgEsjId2Rb39A2lgjJxSGX6CuNZnS6k8J-i-hNfHotKCCm4J4KkLTV9oroFrvymdDH1L-kUNIdbLZ8a20-XMPiRpn0PIf7CTt41LnnuKYE2YA8qy4KsT6R8sKzWJiias6_Il3HN_Q9D5FAjVIUnaic_PX8dAdUS-1DBUtUZMgpicbssZUtUqkmL5VA4BLVCf8hXK6iMYAoh6LBfIqxAFHsAeKWZ1Jtqht8bGQ1fVTVwrRspdFIoj7X7s_-bGhXUXTJOktPWFoC_iTx9Lp5HTrKzP2wDlC7jBnbHh200k3Tuel3v7AtsGLcgfyhMnlAK22zcCWKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هری کین درباره توپ طلایی:
"من دوست ندارم درباره خودم صحبت کنم... 73 گل، خودشون حرف‌های زیادی برای گفتن دارند."
"این بهترین فصل زندگی من بود، و این تفاوت بزرگی ایجاد می‌کند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106804" target="_blank">📅 14:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106803">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=vT5IX4aZbNwfSMbANx-NFJRZiXPw7Fnpq_Zc19T_kRfTsbhDFW56BXr_Bi4dNOpM_zWdOUSY4DlsF1Z-SMMzpWkIKhW5fH694D3HXZdDa2eGPQndd3rA_Eoh3sA0sNhX0vvcTWi0pA4Thsq7lARV0YuRaU3MyYNJAS6gBYzWc8MFe7d3JjqwSlX3xp9dT8D4naXUsxT5uWntIIH3BAKdalaOOfPlMcTV1PQ9xkQ1R5zYOXd1lC2N__0iD-Iepd-voDz7PIAV12D5dSIoFFRt6b_AU0RZqBgHP23R5os8HninpUHoQTsIFWmo_oYMehKbKh6WxsyxbIw1H2xfgJ9zQhNbzUvp4VlOnGlR7g5-apqcekk05Q-i9mmcTZG088f4qkIDZolkAhxJcvy9I66t4oIeJtofbf-FKAwVS1Lkh4UKvQMpOGGYS7CO4RNsCHpeKxzghv4NCwPmKvVpaCe3lZ9Mv6T4PanLandbmRVBlnUV9EwCg57fiE_AGg3J5InnFu84uO7h9k5h5GwgIrD7PAvyOiqt03OsaHl1e52jkftIM29nXK7N9LTH6H65vCdaJ9gh5Vk8LSp4UMq4uYEnxzuW_MQUnMvhFXOwZro1V3izejWL24RRABxYHR4x2DmLM_55Xjm9Pod3X1Uis-wFguwfElUxhnLm1k3s8z0pMeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325a2dc7b7.mp4?token=vT5IX4aZbNwfSMbANx-NFJRZiXPw7Fnpq_Zc19T_kRfTsbhDFW56BXr_Bi4dNOpM_zWdOUSY4DlsF1Z-SMMzpWkIKhW5fH694D3HXZdDa2eGPQndd3rA_Eoh3sA0sNhX0vvcTWi0pA4Thsq7lARV0YuRaU3MyYNJAS6gBYzWc8MFe7d3JjqwSlX3xp9dT8D4naXUsxT5uWntIIH3BAKdalaOOfPlMcTV1PQ9xkQ1R5zYOXd1lC2N__0iD-Iepd-voDz7PIAV12D5dSIoFFRt6b_AU0RZqBgHP23R5os8HninpUHoQTsIFWmo_oYMehKbKh6WxsyxbIw1H2xfgJ9zQhNbzUvp4VlOnGlR7g5-apqcekk05Q-i9mmcTZG088f4qkIDZolkAhxJcvy9I66t4oIeJtofbf-FKAwVS1Lkh4UKvQMpOGGYS7CO4RNsCHpeKxzghv4NCwPmKvVpaCe3lZ9Mv6T4PanLandbmRVBlnUV9EwCg57fiE_AGg3J5InnFu84uO7h9k5h5GwgIrD7PAvyOiqt03OsaHl1e52jkftIM29nXK7N9LTH6H65vCdaJ9gh5Vk8LSp4UMq4uYEnxzuW_MQUnMvhFXOwZro1V3izejWL24RRABxYHR4x2DmLM_55Xjm9Pod3X1Uis-wFguwfElUxhnLm1k3s8z0pMeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تأثیر غیرمستقیم تحصیلات بر فوتبال، از زبان بهترین بازیکن جام جهانی ۲۰۲۶ و برنده توپ طلای ۲۰۲۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106803" target="_blank">📅 14:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106802">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=fhKI1RUs4UlSjrfSzxv_RDucq6xKYtdmdTkGr7v0VQDRK-SKkDgwNcr4bveTfpTNqiz0GoRLW-rNn6HUeMMzyTuYqUAV3ijxIol3q7omVG9Do5bOU2zp2LmdW6AKu_VHNNo6PleeTZnIaCwWnlhdMU8lDoS-13caSqR2DFn5hNmUGPih_SA_Hr2NXhfSVLtFZ3f1dcXpHiPowhuRXZCn7_YVe5mvaOI3HFd17PyulcccLBfNVt5qcr_kcFBG_UFejTit9RS17HdCtkuOKil8yi_peDSIDFnwOYN3ZwPCKUlA7UXeXVSAyyGwgmb4NaeLILGs5AoDePfG5KsEWv7b5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2929cbe0df.mp4?token=fhKI1RUs4UlSjrfSzxv_RDucq6xKYtdmdTkGr7v0VQDRK-SKkDgwNcr4bveTfpTNqiz0GoRLW-rNn6HUeMMzyTuYqUAV3ijxIol3q7omVG9Do5bOU2zp2LmdW6AKu_VHNNo6PleeTZnIaCwWnlhdMU8lDoS-13caSqR2DFn5hNmUGPih_SA_Hr2NXhfSVLtFZ3f1dcXpHiPowhuRXZCn7_YVe5mvaOI3HFd17PyulcccLBfNVt5qcr_kcFBG_UFejTit9RS17HdCtkuOKil8yi_peDSIDFnwOYN3ZwPCKUlA7UXeXVSAyyGwgmb4NaeLILGs5AoDePfG5KsEWv7b5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
زیباترین گل‌های کاندید پوشکاش سال ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106802" target="_blank">📅 13:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106801">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=oejV5gTnhgmwFtpO9PuDyvdEfphk_6YqtRpa7kRstq1uOyIAb5Xe_uOHLUAHLumxNVG_FqDZQeH7ik0pmFfHjRW_6D70cBsAQ6TJ2jZ69kPs1Dg4-bi_36c7NoxNV5F8gSevrVh-J5QRhC11oILennVUcsxPrxDkWS7AqgIRn59e6KNIjzJyd8xzmP5IdfYv6uhp02BXagqhthiQJr3KPS1E5YZtW1rrPds9kat_J-doOWBgrgDY-f0fUqVO5J-KUlNZLd9A2cVqbfcbkmPkuSvnfKnq7Bu23lmqdfn7yRqq5Fh48PxuXeyR6V3-gk6IqzTmPHhzGsaOYfV33aEsMIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37652c08b0.mp4?token=oejV5gTnhgmwFtpO9PuDyvdEfphk_6YqtRpa7kRstq1uOyIAb5Xe_uOHLUAHLumxNVG_FqDZQeH7ik0pmFfHjRW_6D70cBsAQ6TJ2jZ69kPs1Dg4-bi_36c7NoxNV5F8gSevrVh-J5QRhC11oILennVUcsxPrxDkWS7AqgIRn59e6KNIjzJyd8xzmP5IdfYv6uhp02BXagqhthiQJr3KPS1E5YZtW1rrPds9kat_J-doOWBgrgDY-f0fUqVO5J-KUlNZLd9A2cVqbfcbkmPkuSvnfKnq7Bu23lmqdfn7yRqq5Fh48PxuXeyR6V3-gk6IqzTmPHhzGsaOYfV33aEsMIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✔️
توضیحات مجتبی‌پوربخش مجری اسبق تلویزیون درباره افتخارآفرینی کیمیا علیزاده در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106801" target="_blank">📅 13:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106800">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4UORp8v0EJWrRx2yflnhhlXfZYA9B4HgiXVkFZWz7Ms0mbjIFW9U1HZQxIxwA7fVY2-Vv8ETly93-2T-u2RSscpdCwAnXBAxuPTJT0_Zdewatss6eQyYIrEnJpqqpKuHi9ne2UxI4KDkOBQ_wjr6g3HRudnhbAlfnRFysSxAmoAdfcK54DmIP0znsNvQ0gZq5bXQiEgBSKPYbqJmgY3il2mTFnCWWdJkCzObNvB4KjV0bLGkD05PEnp6Zokmn9SNSWm1dDUiH7lCIPeNtQMK7loCVujAZpPK-0gaKu0BoGIffpvFDtHpTUaBABGYXdILcPe710Uv0Q9QYG5PfQCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
لیست تیم‌ملی انگلیس برای فیفادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106800" target="_blank">📅 13:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‼️
🎙
صحبت‌های عجیب و‌ دردناک مهدوی‌کیا از دخالت خانواده‌ها در مسیر رشد استعدادها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106799" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106798" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106798" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCN0AhYsUqu_Vo3EmjrE6JiWbBr9VmWRT5jmg2koBX9Dv2ZpA0_CsKe8PkaPDizB-dIbZ4Pe7jEdoO45_FagOS06U9LbWQBcwDD6SjTgwg073OR6g1NHgxaVr1VJpsgSa_R6Cu47E7q9dW8xnDZN_J3grk6W6iAKno4dzakpDs3QT6AdK_YnoJDS3Nfh3fKtRz1-UyuOHxvqF1W4yW7G9yxZIhFPN-9GwylHfJiTbam-DL0C6Y5EZxwsdHF02vJOFEii3FBHHrh8jUNnaBVe6mykP2p3pN6scxlly9GSStOPvxUHlRPBoOBOaCRYrIyjDLM1p69xceaBuhkqoVQR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
چلسی
🆚
برنتفورد
انیون برلین
🆚
بایرن مونیخ
لنس
🆚
موناکو
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106797" target="_blank">📅 12:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2lhWSQ3-7Ae1l-6eowyQbBSQ-AsdTlwQcy5qZA0zKHp166WQzJRvKLM23UZjHFHe2qsbGnT0CiZJqS9Fi9rZJ6878NzDuz4OE2vyOB2iXaqappzSGT7TVBk54lVywD09p7xyr0x-7l31hV2jdjSz4hZmVJEQz71Rlz76Yl1gsJmPanD8v5JQ2zL_AXV9ULEatW7bXCaETOYlz1l6EnmWaaceTBfcGiEsQxKXSvG0vADNcaSqpHlmpE_tT2qwBCwTBJEVLn4U30mRhZGDSO-89j10-8iTngWih737SeyMeYdSloE_Sb3vAg0SJTRNkaM6lNGhgwHMfmdUBNr6LWiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
رافینیا، با هت‌تریک خود مقابل راسینگ، در 7 بازی اول فصل 2026/27، به 14 گل و پاس گل رسید و رکورد بهترین شروع فصل لیونل مسی در باشگاه بارسلونا را شکست. مسی در 11 بازی مشابه، 11 گل و پاس گل به ثمر رسانده بود (فصل 2012/13).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106796" target="_blank">📅 12:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=CxiM48dlb1TQT7xzSG9Nz83PZxXbcozztujo8ogY2MWtnf6FguARK_y6z_zHWGMK2irq_6ORLkUmMAdOFhV0tRRqGsF9XBc3HxMoouCzjAD2rhypPLbAbF8TDTOktmZw9cXjeJY1iBN_f8vZkRcgxLYS07t8fhl2rOdOKJ3M8gnrTrOFBGjEqhZdLsZh304-ZCSIs-QjijCzcqLQ2y8Z1wlDEgA5loBchxlL40fSXW38aBq4oZHz9x933eeZupPnBSllPhDEStCBKb_wiPUl4Whx9sdy-KDqyvvopq2ep9F-7kXFjyyBSh5V0_bo-LFd4tL8kVksPKwUWLRb8sQRLU-btnTP4OwYDyQPaiehpHxlH57gReQNDdU6v_dypgsbFm4awL9jZFVZZI7aAGTH0KbJp4vNjn48KCXLX--_b5NnisjVg2EqxnhZtWFsrVeLv5-CAM9OSQGpq1qiB3Mwzoc0oDrkgYqfFEiXrRIqKWdIaIxsl7hdlqAzkNH4KNODOgbj7GhzdROYEhD4GL3Exm1O3M-VJslgRQOAu0uKHF4pr6c4-xTDn3cBjhqcDDyojvv9GBk_stFAql8LuHOujm06GCbgYVuUE7DKxKjCQ_H6aTvc76ygfYGpZ9icwF908S1rmVXzmkSlNf5WJNNuBK9PMowtwtPIX23SI_Agb4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f364f9a06a.mp4?token=CxiM48dlb1TQT7xzSG9Nz83PZxXbcozztujo8ogY2MWtnf6FguARK_y6z_zHWGMK2irq_6ORLkUmMAdOFhV0tRRqGsF9XBc3HxMoouCzjAD2rhypPLbAbF8TDTOktmZw9cXjeJY1iBN_f8vZkRcgxLYS07t8fhl2rOdOKJ3M8gnrTrOFBGjEqhZdLsZh304-ZCSIs-QjijCzcqLQ2y8Z1wlDEgA5loBchxlL40fSXW38aBq4oZHz9x933eeZupPnBSllPhDEStCBKb_wiPUl4Whx9sdy-KDqyvvopq2ep9F-7kXFjyyBSh5V0_bo-LFd4tL8kVksPKwUWLRb8sQRLU-btnTP4OwYDyQPaiehpHxlH57gReQNDdU6v_dypgsbFm4awL9jZFVZZI7aAGTH0KbJp4vNjn48KCXLX--_b5NnisjVg2EqxnhZtWFsrVeLv5-CAM9OSQGpq1qiB3Mwzoc0oDrkgYqfFEiXrRIqKWdIaIxsl7hdlqAzkNH4KNODOgbj7GhzdROYEhD4GL3Exm1O3M-VJslgRQOAu0uKHF4pr6c4-xTDn3cBjhqcDDyojvv9GBk_stFAql8LuHOujm06GCbgYVuUE7DKxKjCQ_H6aTvc76ygfYGpZ9icwF908S1rmVXzmkSlNf5WJNNuBK9PMowtwtPIX23SI_Agb4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
فرزانه جمامی، سرمربی پیشین بسکتبال زنان استقلال: تمام اعضای خانواده‌ام بجز من طرفدار تیم پرسپولیس بودند و هنگام دربی اذیت میشدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106795" target="_blank">📅 11:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106794">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhCcd5XybBvy1GuKbLGiI6GBLeYsbUDZI1QRZZs2VkZ2q9ThScJYeOF9aQcf2PPr8waA3Iu73IdDl3M-sr8XfZpnGkYIqqg0cxhmxxNndzsPHlHHQi0HKi28In6w3osIfjgk1PKyd3WwLvvknKO8AedI7VZuurCEDSmPp0B7BeBBQlUPvOD9CGiRbUU92CY39QmLqIyUVo9too-westN1zZ_8jS2YQ8-2XwXt-pjIdiOE-1jkPy19ldYV9UP00HFva7B78GpNyOWP5NMgAAXlukJnlOn4ocd9Usk-xqNpeV3bYFavB24hMemqG3eHYXaMlbXIXTpOv7yRLiS7If2BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه شروع آموریم و کریک در پریمیرلیگ با منچستریونایتد؛ اخراج بعدی در راهه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106794" target="_blank">📅 11:33 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
