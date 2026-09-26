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
<img src="https://cdn4.telesco.pe/file/rW97uyEmIqPnptTPdoFB1n3NA8ipH_vH-FXYAZto-dc7rCmTp8ipD01FvMdMX1Aa6xu4ky0NTh7-9OI7hrtYnpOYnLX1MTy_hJdyMApTwP9Kbi-FE9wWCh9n8qudxlL26skjbLz7FUQi1xtpe9hZatAPC41TxYYcBoxwuIcUmi4t4Uuk3HNdMLr1vt4K0rB6BLw36un3zJTgH1j9zH6VUHh6bQjPpLJvB8N5MtasbO19uWdF6bUJzLxiG5jIg04HHQJwEvoUF0IQFsgkdnJyevPCExf0zQohE4ByKKEKWpk4c7wVFeUGNQckXlrOVEfeD7kxnFWfpyI6AsDzVwFvEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 252K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 06:11:45</div>
<hr>

<div class="tg-post" id="msg-84047">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729ba5bf0c.mp4?token=VwJvRuzUIDSnxY9WRBLZ5okKlKxgKFIx5bxdzBJ0CxlddRtadKJ09joSQ2iIEZXl82Cjs_NTIDcfPv4AvTkf3fM39I1Rodqwjaj3zY6iWQsJCrZAM0-FnpPWBpwsr0UJyOYBy6bpUfqi3KM_UrPuQDlwdW7AkQEt9x0zsbki3lxt-NpNlo14ocZqwOpSYxuYYBaZjnpGMpJqux10MI34tUS3NmDjuvdZDC5bjsRPIGJP4Doyl5axjytsLFrk93cfs9H0bYVWdZ65GpbfXZL48BaWSlPeFKrDzBKBViQE39O7C-oFZmDoYK5ZiYu07KZ7ILcCRjbBx0x2cC7MH9hgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729ba5bf0c.mp4?token=VwJvRuzUIDSnxY9WRBLZ5okKlKxgKFIx5bxdzBJ0CxlddRtadKJ09joSQ2iIEZXl82Cjs_NTIDcfPv4AvTkf3fM39I1Rodqwjaj3zY6iWQsJCrZAM0-FnpPWBpwsr0UJyOYBy6bpUfqi3KM_UrPuQDlwdW7AkQEt9x0zsbki3lxt-NpNlo14ocZqwOpSYxuYYBaZjnpGMpJqux10MI34tUS3NmDjuvdZDC5bjsRPIGJP4Doyl5axjytsLFrk93cfs9H0bYVWdZ65GpbfXZL48BaWSlPeFKrDzBKBViQE39O7C-oFZmDoYK5ZiYu07KZ7ILcCRjbBx0x2cC7MH9hgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا همه خفه شید فقط ایشون بخونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/funhiphop/84047" target="_blank">📅 00:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84046">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEU3ltcNdwDeaWEkyDyboMqz_SIsp6suZbhmDjzks-Pk6gzDdfa0YcDGdEoq1IAuiN08RdwVGP2RklMUkMlj7LreLOBtWr2qd1i73O5GbSXXIKADt8xtC1aQTwX52kKn1OUUPBSYSMbfzHiJDXEb-1jlc2Es_ZqWX0-H3-JqOsHbY7nhnBziN9eDMW1KkKIXIUFaMYS9NvJ1CnGa3kHU6RvDdsACr7Mk-5F_VcEwYyylfsVW2mMdQsSS9Jqn-j-1yBbNm61ZMoK8be_KTXau92P4TpvR3skMNT45QzGn7_kTg37UhcgnTJpWNHTkMohGw-cO8RYFE3hZRBLVida8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/84046" target="_blank">📅 00:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84044">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cywJKGlSfA9g6PxXdxHM7Fg49R7xdCXrjVmlXwOf_1I8R5srubyb7t_TCTMcCdnJhaaB3AcJtBMvzzJIktkhfzizrkQoHBQKTqVHHO7p-iR2aIZu3it7USq2I-hSLfffBj3cfE7PqXd0MMcAF5bgwIWdYIJ79Xmqjir755lERSqFTO-Ji0xp9ibr0YInV1UcZLHb2L62hkXsFYThfgVMuRVpZg8R9Gl2NCjUjggoQultrbq4aUj0MajNqPLAm2lG8grMJvEEiJSSTb9uoKAFnsrJRSYtuqWD9MITuZqMtcFokBXkqIU3WOo7ZX-S0xxPFPRbhGb8FOkq1IrVQ9HC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YjroKVV05qCPi3-Ahep5UijLjmBXgpkqk3Azh5A4B78krJ_OML_8ySrkU65znKMH-sPUZc50ZYsZ-IFyVZiqwxGJhdWyQHHShKVucaY-8h9iDr0QOkc7FuJLltm0-BTkPRJSu-UgPAosdpKf8w8QWkA8i3uoFYexqp_Ck7Ng0ymF9aF1xLKIwja7j2Q3RiycJ9Uf5hPa6WJFOnWI81yPWqc3x115yTO41Jugr7KVS8u_5xE6CAzJdoLoMCmTms29HBd4ZoEOjPqlpGRauejmA-9g5jgKVs6bNUy2Q4PE8lN5ZypzT8QIy-K_0IqAyemk11Y5_cQylCx_QTMHSqnmyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط نزنیم حرف خالی
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/84044" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84043">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwJzoGRS6O23N7gZ683vIDr6m14H93If84fITLZVW9ngtrojZuRp1YH_pi_G2dsHzn_d6zqEUzbEWqYva_321lG3jOl-hBwobNjwIp10n3qGy58-X99VUhUGo4DS1vvY00nZt2bEQzizOQ8Qw4yn2nxaiCVR0wE--CKj9YzfmYGKWSjCkxi26C1xJiJ8cidh8wE0uUYXXqGGG1_apkq7emreRlsFpKJ6S6J_uHEcsQEXRrF_CZtNvmUAqp_TZ0Ejf8QleQFnUiO9yZkggBSs1_tmaxNUPS3Mxsfn6lZdbVcPKMliW1Q46zXsA7jixYIKQaXnp-CUKaHR10fYMueP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بعد از اینکه پزشکیان بخاطر سخنرانیش تو سازمان ملل حسابی بین تندروها محبوب شد حالا بخاطر اینکه تو مصاحبه با فاکس نیوز گفت اورانیوممون رو میدیم دوباره داره ازشون فحش میخوره :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84043" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84042">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrpb_SePrE5zj_sZD5dMs_eTeLG_44lZCxo52c4-K-oEknk2wK57kMV8qv4rkPjSpNMMfNibiIu01_BB4-rHEiqszVaUXlvslb60Nrw-Y-6UBkR3N_G87R7JTo0Bk5efQt-pnHdOBg9qcanTkX4PntCA7R-BzlauPWbVY2JR0RAXsOkenuQTXT65msg6pq1L9rA92zzmSHSrWOP7XstVDVWRvMuX0bc3nuAy5xyNwneSmNmzrFuEFDNStiZm0cYHsrQbn8jLS2SY5Em01-acTA0rGiIB_US5tKogJ0jM7Nu-nE-J5bq5OqmiWtZTe7OR_XBZmCZqLdhL_lexSsJVaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپفارسی دیگه پول نمیده فقط یوتوب
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/84042" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84041">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84041" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/84041" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84040">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC3CMgX9vH3hLZv01HR7gHDReMtO9j6lbNwggVv5EfWNttf4Nt2xjtKZ_PQ92DByDn5OQkvgPpEKl76Aiki6gW0i5aedce2etUcX_CLV6h4BLKR-eT6YIwjkT15n4s5JKXDJYGlJdI6SdtpqC5-mUnSR3f6scIjVS-nMV8QAuy6sWFE8gUQA84ILipp10QwupMnyQ0T4Dp6OIvUhudlL7SdHaJXctda3yOM313X8hGP8HMePQEbiiVT7QLEHmxx-FnF9GY4tPWggiMpwEPC7Mwb3tDFvJluipl9IKdXMrlBH1nDQDVZNACK3uImb8Zej323MVIhMb8e0I7sud_PYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
⭕️
اولیتت برای انتخاب سایت چیه
❓
امنیت مالی مهم ترین چیزیه که یه سایت پیشبینی باید داشته باشه
⚡️
ریتزوبت با انواع  درگاه های شارژ و‌ در گاه مخصوص و اختصاصی کارت به کارت امنیت مالی رو به کاربراش عرضه میکنه
⚡️
از همه‌مهم‌تر واریز و برداشت در ریتزوبت کاملا خودکار و اتوماتیک انجام میشه تمام پرداخت جوایز زیر 15 دقیقه س
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g3
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/84040" target="_blank">📅 21:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84039">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/84039" target="_blank">📅 18:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84038">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84038" target="_blank">📅 16:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84037">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LayH3zFRmgw70H1QoGXhtoyXJKokaVWeFurYfcFQti4_6npHQiT1GyAiDd2tXJgRRt6hRCY-tE3Yz2xVQmdAch8ilVTFV-pI97-wVcWzxA8Vi6Qj5Hgd-yWuwNhRCNdZvy6h5_Aqn0YhSFppwSIj18111N3AX8LDMayknTslWKlxcUal5cah-RLnnmnLxziN4yNx79MKuLFQ8eew-Kf2WJL9eYx46vvi-UyUiNvbjIcHVqmWKlEtx8v0r7Wb2lHQecpxCwDc5TPB63TEMm_JYpMBIdmv5cLSQRtmBEwXHwbHYMI8mIxn6C87gwp2o9ERPkfEFyfP4TmGRKoB2_3c4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان و دکی به نام "ماما کشتمش" ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84037" target="_blank">📅 16:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84036">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03c7b6e9a0.mp4?token=Cs_OibKIExzle5AEgBITrS-wqmoeM6Wo6-bE6whgagevzLvNrBpnXKU5Mhxh40Xega6iBri-ki9OASgDbNVUUVh36l_fRFWa2oo-BthHGdOatv0OrTqymLzNV05UMjdFQMQfnmcX0_OUTgRfZpKJaIQWcB67tI8C1r_a1ahCxn5ix6iIJXJNp-mI2K46kTxSzgFTEi2pvTA4ObDmEbvUs9mM6-MkrHigvLK2P9JQpPAyci7A39cpJuW8p8sjGhsWq3e0tnLCp-QFle3tlXxC-hLGlKiB7JxPTXftjnD2Kco-ATLefNB4oSpe-qB0NP42eaiH4e5C-hf757As81aGXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03c7b6e9a0.mp4?token=Cs_OibKIExzle5AEgBITrS-wqmoeM6Wo6-bE6whgagevzLvNrBpnXKU5Mhxh40Xega6iBri-ki9OASgDbNVUUVh36l_fRFWa2oo-BthHGdOatv0OrTqymLzNV05UMjdFQMQfnmcX0_OUTgRfZpKJaIQWcB67tI8C1r_a1ahCxn5ix6iIJXJNp-mI2K46kTxSzgFTEi2pvTA4ObDmEbvUs9mM6-MkrHigvLK2P9JQpPAyci7A39cpJuW8p8sjGhsWq3e0tnLCp-QFle3tlXxC-hLGlKiB7JxPTXftjnD2Kco-ATLefNB4oSpe-qB0NP42eaiH4e5C-hf757As81aGXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون دختر که دریک سگش شده بود گفت استپ فادر ایرانیش بزرگش کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84036" target="_blank">📅 16:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84035">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خدایا این کارتون ساختن با هوش مصنوعی چه کصشری بود دیگه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84035" target="_blank">📅 15:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84034">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خدایا این کارتون ساختن با هوش مصنوعی چه کصشری بود دیگه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84034" target="_blank">📅 15:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84033">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8O2QGSXmm7CX4_szuKjOunEUHGZIXix4n_TPZPq2Ghnno63a7Kn1QlVnCh5B0h1s5nUknmvxtRZDu2vwQEX9Cy6Q5sWAmRX2_y2rVWemjns0gjmEPkZIzeC4TUu7MuIShT5fXSeCvgbzcSzJ9REbJg_8KfePFfFkImK6daWzscrHeltF4aDLXGBXfiGLjpiuNKcs1ts_0DWrbOwrp4HgfT6XlSQdJ_zAsv-h7bIF1dHyrGZDaDqJeCQG7Nlkz19RRVsSEWnM_wkktAaN3Kht6AA1AiW3rPny4MR4VfsD-oPTpBYVvraScx7tv9qe4c9-f9FbIXa8Yx0sOa0-_XK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو با اون بیفی که کردی یچی فراتر از این حرفایی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84033" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84032">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZwCx_tWa5W1B7RGQsK1Hj1XIDHfbS8-LVuvHvJfHlH_XayEWTI7QqaYTZQYabScpOtKKElLyeP6cTR_gvEC2yypEOl5TqSkYVCULeezKHOnxXAWmqpUumfimLIWzGYjoPti5XBToRx6BhWA1H4RMedl54fgLrv5uW1D_e4N3GI64trg5HtifGztxziKLdrqA4euOokwEWBxinmJyzjLTaCd9i7tm3FP9VTUfFnGAAh84yyYBNS5XttROo01NMsANnP2HN1l8DBCTru0iCzmi14Xw_ADLaQAfP8n7l1KAcL5ZnrxVx4ZCR0pQwo67j1JlEcYBkph92uFQLzLjnm0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کصشریه دیگه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84032" target="_blank">📅 12:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84031">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لایو دیشب رضا پیشرو که بیشتر راجب کصشرای کنسرتش صحبت کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84031" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84030">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/84030" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آ
موزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84030" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84029">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93b447af2.mp4?token=vNWjkjodsNI2dVu7DkNRzftuHD2M9cN34TxkA_4PHjJgEtrs8YrazndiLBI6hChtc3n8r-QvU_fDpwhar6k_7KoDeZpdHl1Wvso-62CmBnykIeWJUb04S7bae1I40VUzXnyoqTVtYGyLGE3KDGPJ57DtZJDkn4vcjTgN0e65U1sGHhR-YfTu7AwVXhvy598ep3DPjfSNB8YySPUqAct5dXjiMwbhN9JkUYDQbkaZFxs13JK7K_2UVCHTvib_jLgOXI3dOaIS1c3YCDbaAtxRuJ-slf1lAo5RbInpYSteLxrqQvBTCBboemtUjb4_kVuoXYc9AFHr1_2qiuJJEnChfgFPMY5LD_FlFaciEVuAQSxRNiwCRJ5SIugjYJA3nAmeNSwvYP4PGYgc9hGJFUQc_leC9TQV7LUqmR118B1VsPufmppaNPDyyHczAkWwH5PS-3AlTkPwA2KypAEXMWDmEN4QqX9LkORNOJBSyCBgKDEutg0b9W3QypLaOJldYlX4tYMF-WZiPkAVyBeOQq9jO3BzprJ_vEigdJ1X88dmWIGLkd5np_Oo6IygSPZAvBwSUbA1ZA-1tqbxDXVMYDZS_BDsExt3bND-S43EawqZSuCO7byG6rRWklU9O5kNSn-BGcbW-UCWBU-1zDzkWOs4Kmd7bDwetrfAkx4KMm5eB4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93b447af2.mp4?token=vNWjkjodsNI2dVu7DkNRzftuHD2M9cN34TxkA_4PHjJgEtrs8YrazndiLBI6hChtc3n8r-QvU_fDpwhar6k_7KoDeZpdHl1Wvso-62CmBnykIeWJUb04S7bae1I40VUzXnyoqTVtYGyLGE3KDGPJ57DtZJDkn4vcjTgN0e65U1sGHhR-YfTu7AwVXhvy598ep3DPjfSNB8YySPUqAct5dXjiMwbhN9JkUYDQbkaZFxs13JK7K_2UVCHTvib_jLgOXI3dOaIS1c3YCDbaAtxRuJ-slf1lAo5RbInpYSteLxrqQvBTCBboemtUjb4_kVuoXYc9AFHr1_2qiuJJEnChfgFPMY5LD_FlFaciEVuAQSxRNiwCRJ5SIugjYJA3nAmeNSwvYP4PGYgc9hGJFUQc_leC9TQV7LUqmR118B1VsPufmppaNPDyyHczAkWwH5PS-3AlTkPwA2KypAEXMWDmEN4QqX9LkORNOJBSyCBgKDEutg0b9W3QypLaOJldYlX4tYMF-WZiPkAVyBeOQq9jO3BzprJ_vEigdJ1X88dmWIGLkd5np_Oo6IygSPZAvBwSUbA1ZA-1tqbxDXVMYDZS_BDsExt3bND-S43EawqZSuCO7byG6rRWklU9O5kNSn-BGcbW-UCWBU-1zDzkWOs4Kmd7bDwetrfAkx4KMm5eB4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
واقعا چرا ریتزوبت انقدر در بین ایرانی ها محبوب شد
⁉️
➕
ریتزوبت اولین سایت پیش‌بینی فوتبال ، که تمام ارزهای دیجیتال رو برای شارژ حساب پوشش میده
💳
درگاه کارت به کارت امن ریالی برای کاربران ایرانی
⚡️
اینجا با خیال راحت شرطبندی کن و درآمد دلاری کسب کن
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r3
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84029" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84028">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOxkABdNqvxePUCDSTo50wkiIHOiOVjcXRcJ-5Ibd0EyT4LUV9P_eKhJedz5OHNBmZ_1-M_de08Zkxt7YO2vsOSvDzu49txHa2Jbv44zEVW3kE1_ApqFlMbZlaDTYCeyYeNWS0Zlo4e2v5H1NTeDKBUAiCqST0-kaGVDAWIWcq_o5PpKqAJdVRAhq8apFLHfuO4hk1Hz2SJWpwFAJybvXjS8hwdfP-Sibn0xdCOrzOjaWmGAZEU8VkiyFYh9fBchfsRgHdxnZRoBkNxY4Y5lyym8wj4v0St-EbKFQYMDzhwYKD96PPJIYSvf7d0fCclOUNsTH1Mbm-HKXh6ofG9LnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی‌همه‌چیز من این فیلم رو واقعا دوست داشتم.
الان با چه رویی برم دوباره ببینمش و به بقیه بگم سلیقه‌م با بیگ‌شگی یکیه؟
(اگه مشکلی ندارید فیلمی که می‌بینید رو شاه مشهد دوستش داشته‌ باشه و هنوز این شاهکار فرا بشری رو ندیدید، همین امروز ببینیدش؛
اسمش: Léon: The Professional)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84028" target="_blank">📅 05:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84027">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c419d7c7.mp4?token=Q90awmHM8BKJMWuW5eCCY7tIXNsBCrTPXYQWy0xnQ6wNR1k4xLGnhwi611wbZxN8oqAC5BdtpVT6nREQn-5hVtC9LEME4yEn9-pQPV2L4ipGz4EgMp78DUxRw5S9p2ocGw217741PvFKcjeCd_N1mZw-RSP647jWMxLQj15FSfsGsLQHN6xtE3xdXS8-VnZbB8BUtPOrcDOEFD4RmGrw37VxO7ObxH_MMVNxS82BWNlM0GkTlykhAY5LVRp1yzCGAbMXwk2KVV4ZoIm1zKkgWvgrC8peBTO6TGIkA2eyaXTovWVmta8JDe62MtjLvs4UdUm2MGasjcMDa0PttCiBQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c419d7c7.mp4?token=Q90awmHM8BKJMWuW5eCCY7tIXNsBCrTPXYQWy0xnQ6wNR1k4xLGnhwi611wbZxN8oqAC5BdtpVT6nREQn-5hVtC9LEME4yEn9-pQPV2L4ipGz4EgMp78DUxRw5S9p2ocGw217741PvFKcjeCd_N1mZw-RSP647jWMxLQj15FSfsGsLQHN6xtE3xdXS8-VnZbB8BUtPOrcDOEFD4RmGrw37VxO7ObxH_MMVNxS82BWNlM0GkTlykhAY5LVRp1yzCGAbMXwk2KVV4ZoIm1zKkgWvgrC8peBTO6TGIkA2eyaXTovWVmta8JDe62MtjLvs4UdUm2MGasjcMDa0PttCiBQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84027" target="_blank">📅 04:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84026">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eia6Ttp5uIlrO6xm8S-tPNmiDH-iAP0nnrPKkzxRW2x9EDydzobNEFDJoMr9Tn5NV5D0IMCZ5WF_th4hvLxXY6pzkcWEN26PdTILyme-0RtCFWKfdzV8BgLRMEUFvfJUVVAU7E81O2sEqzORe8S3qAb5Ot3qCnK9j5FpUfzjLo1rAnrZ333J09m60FtaeqOvCinmu5ciOke8EonczdHh-DkW5ZuamyOg9kGWGd-Br7bGfh-UTka5Gcaaq87QKGOkDMaZKo2Y14SNRnHmeXTjQrmHI_P-Jb5n8Abr--juqyqEcJLXIGsAvFc7r3Dy4950F91CP2Um__9OHMVDfcNbsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84026" target="_blank">📅 03:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84025">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پزشکیان: ترامپ مدام می‌گفت: "من می‌خواهم هدیه‌ای به مردم ایران تقدیم کنم"، اما هدیه‌ای که به ما دادند، موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی بود. آنها در واقع می‌خواهند با ایجاد حوادثی در کشور، راه را برای فروپاشی نظام و دولت هموار کنند. من عمیقاً…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84025" target="_blank">📅 02:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84024">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/195d939cba.mp4?token=TS0TU3pKADeOOLVDfHqZt0NMyPJSr0AdpE7J9dK5k9_gKM5VSGqIOO7AbJmxB72q1N2N7l96RYgkIo9Y_xSQo-BbfvJbTzHPWkUhoswgXpR8kQ8H69mFkRsIoxPxX-FjnHedGRFqGLcEXePMtd3b55W3khED0MRV9ocJhsJQ9DkSKj7Z9Nu2xdz37pcUQYvTvmB7TdFmxeI1LmqNZBCZ-ss1jbQwhp8rqU2Qsa3dXKP8CJyzDak5jEE6iv3NwqycRM0YC9HKsw8Daut2_ce3vGBOknyWX81w3oci6X7-I301ww_hGianQ92DeZaezGKV1h9X3hg-DWOr4tmjyI2K6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/195d939cba.mp4?token=TS0TU3pKADeOOLVDfHqZt0NMyPJSr0AdpE7J9dK5k9_gKM5VSGqIOO7AbJmxB72q1N2N7l96RYgkIo9Y_xSQo-BbfvJbTzHPWkUhoswgXpR8kQ8H69mFkRsIoxPxX-FjnHedGRFqGLcEXePMtd3b55W3khED0MRV9ocJhsJQ9DkSKj7Z9Nu2xdz37pcUQYvTvmB7TdFmxeI1LmqNZBCZ-ss1jbQwhp8rqU2Qsa3dXKP8CJyzDak5jEE6iv3NwqycRM0YC9HKsw8Daut2_ce3vGBOknyWX81w3oci6X7-I301ww_hGianQ92DeZaezGKV1h9X3hg-DWOr4tmjyI2K6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ مدام می‌گفت: "من می‌خواهم هدیه‌ای به مردم ایران تقدیم کنم"، اما هدیه‌ای که به ما دادند، موشک‌های هدایت‌شونده، سلاح‌های سنگین و ویرانی بود.
آنها در واقع می‌خواهند با ایجاد حوادثی در کشور، راه را برای فروپاشی نظام و دولت هموار کنند.
من عمیقاً باور دارم که انسان‌ها نباید باعث مرگ یکدیگر شوند.
ما باید موجودات برگزیده آفرینش باشیم.
وقتی می‌توانیم مسائل را از طریق گفتگو حل کنیم، نباید به خشونت و کشتار متوسل شویم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84024" target="_blank">📅 02:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84023">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=NuMmyJsQqQIv1jsd3FYMpWIAiJRcSE5ySgmu1vBv7J1dh4jfQ90LlNt6VlUFYx6pNNvKojsq8Ui9GYuMIl1CsC1WKIZbGBWKQdRnSKjspTeN8-84tuXYwUDeV8iGcTpSa8C7ZisKs8876hAvtV6wBYBGeVOybBt3kE7Vr_VadtTs_hnjIhPl4ign_JPZauYhPubYz5wdDyD1SAKrST782TZ-LykeZaZhaEps8tYuQZNgnTuqLCd3gxUJMzmXpqKhQ55FdKzNAgsNaQj0Pry7tEFBvHTTLeTyXI1yG0XBlx2wyeMqfwLO0tzgNK89_bc6-2t5HBkCEX4a5H9qvRzRKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=NuMmyJsQqQIv1jsd3FYMpWIAiJRcSE5ySgmu1vBv7J1dh4jfQ90LlNt6VlUFYx6pNNvKojsq8Ui9GYuMIl1CsC1WKIZbGBWKQdRnSKjspTeN8-84tuXYwUDeV8iGcTpSa8C7ZisKs8876hAvtV6wBYBGeVOybBt3kE7Vr_VadtTs_hnjIhPl4ign_JPZauYhPubYz5wdDyD1SAKrST782TZ-LykeZaZhaEps8tYuQZNgnTuqLCd3gxUJMzmXpqKhQ55FdKzNAgsNaQj0Pry7tEFBvHTTLeTyXI1yG0XBlx2wyeMqfwLO0tzgNK89_bc6-2t5HBkCEX4a5H9qvRzRKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما هرگز به مردم خودمان حمله نخواهیم کرد.
مجری فاکس:
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی اقدامات تروریستی علیه ما انجام داد؟ چه کسی به مدرسه میناب حمله کرد؟
مجری:
در تاریخ‌های ۸ و ۹ ژانویه، شما قطعاً نیروهای امنیتی داشتید که به شهروندان ایرانی حمله کردند و آنها را کشتند.
پزشکیان:
خیر به هیچ وجه اینگونه نبود، آنها همه تروریست‌های مسلح شده توسط آمریکا موساد یا کردها بودند که به قصد سرنگونی و ایجاد آشوب می‌خواستند کاری کنند و فکر می‌کردند ۳ روزه کار این نظام و کشور تمام می‌شود اما ما مقاومت کردیم و نگذاشتیم اینگونه شود.
آنها مردم عادی نبودند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84023" target="_blank">📅 02:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84022">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مجری فاکس ‌نیوز: آیا شما هر معترضی که به خیابان بیاد رو اعدام می‌کنید؟ پزشکیان: هر کسی که بخواهد اعتراض کند، به طور کامل حق این کار را دارد.  اتفاقا ما با بعضی از این معترضان هم نشستیم و با آن‌ها گفتگو کردیم. اما اگر کسی بخواهد به خیابان بیاید و بر علیه سیاست…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84022" target="_blank">📅 02:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84021">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5add83729.mp4?token=XbEG0GN8_aOQuCC4Yu18vP0z6Ggo3rmXmRnO-i6bdpnKvGtlyQFp3KrGUaWKMuBAff7djRKvMT6qx2R6oeTnIOTPWzVvmoq81M0jKVK2msGT5yEsZIUmCCn2W16el-n-Mftog7PVzPovkwRBsmSGb4_8sNHRJ-XVE6VDuO6m7i5A6_w0XsopR7YygFhR-yoFx8mcpivNLruD7EIncMkh0Jr_8z697g76Rl513QEXEmN_4wclzxl-34ENTGwN6jWs9XoAG8CMQX4jP0TJeLkcINKOgx6PfNzeQ6x9V5_dkty6K6ZFzHfr8_Jqjzg5738DfbKlrL4l1u24DJfTT_Qnaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5add83729.mp4?token=XbEG0GN8_aOQuCC4Yu18vP0z6Ggo3rmXmRnO-i6bdpnKvGtlyQFp3KrGUaWKMuBAff7djRKvMT6qx2R6oeTnIOTPWzVvmoq81M0jKVK2msGT5yEsZIUmCCn2W16el-n-Mftog7PVzPovkwRBsmSGb4_8sNHRJ-XVE6VDuO6m7i5A6_w0XsopR7YygFhR-yoFx8mcpivNLruD7EIncMkh0Jr_8z697g76Rl513QEXEmN_4wclzxl-34ENTGwN6jWs9XoAG8CMQX4jP0TJeLkcINKOgx6PfNzeQ6x9V5_dkty6K6ZFzHfr8_Jqjzg5738DfbKlrL4l1u24DJfTT_Qnaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس ‌نیوز:
آیا شما هر معترضی که به خیابان بیاد رو اعدام می‌کنید؟
پزشکیان:
هر کسی که بخواهد اعتراض کند، به طور کامل حق این کار را دارد.
اتفاقا ما با بعضی از این معترضان هم نشستیم و با آن‌ها گفتگو کردیم.
اما اگر کسی بخواهد به خیابان بیاید و بر علیه سیاست و قانون کاری انجام دهد، این امری متفاوت است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84021" target="_blank">📅 02:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84020">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پرزیدنت پزشکیان یه مصاحبه تصویری هم با فاکس نیوز کرده که الان پخش شده و با دیدنش می‌تونم به جرعت بگم که حجم و سطح طنز پرزیدنت ما، قابل قیاس با هیچ پرزیدنتی تو تاریخ بشریت نیست.
واقعا الکی نیست که چهارم شدیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84020" target="_blank">📅 01:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84019">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جمهوری کلمبیا اعلام کرد که روابط دیپلماتیک خود را با جمهوری اسلامی قطع می‌کند. این تصمیم به دلیل ادعاهایی مبنی بر ارتباط رژیم ایران با گروه‌های تروریستی و قاچاقچیان مواد مخدر در سطح بین‌المللی، نقض حقوق بشر، مسدود کردن تنگه هرمز و همچنین جلوگیری از بازرسی‌های آژانس بین‌المللی انرژی اتمی از برنامه هسته‌ای این کشور اتخاذ شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84019" target="_blank">📅 01:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84018">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMHazAGVKPO1tAwyGqkoryvnPa2pdCxJZ8KqIrEt1ItS1-4MhIVi-e6NoWFsYAwaV05MyieyQh7qkVIkcj3LMbtezEWDInLXgh1auVFHWlhbXjjp8jG1LtOyFrIkvE6ojMSO4z3dPM8rB57hZW0oAKe_DJiFKd4xt7G0PRzfUdPP7ULJSd2XpPWkxgWTEuCUDPxgKfxN_UYzRkZhaoW4teEz4ACSokBbYVYJwV4pII3zFg3gFd_PlXYN158mfG0RgsJ1aYrpwBwqexLM37CKJZH3zdR1hf9wfIJfL_uZp9zYvYMtLUrWEABj5MY_V5mic9EyOqvWD8sNL_xK9VeUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت مسعود پزشکیان در مصاحبه با NBC News:
ما به هیچ وجه قصد ترور ترامپ و یا هیچ یک از
اعضای خانواده‌ش
رو نداشتیم و این پروپاگاندای یهودی‌هاست.
برخلاف
ادعای روبیو
، ما اصلا دوست نداریم جنگ رو تا انتخابات میان‌دوره‌ای آمریکا کش بدیم چون هر چی زودتر تموم شده بهتره.
ما هنوزم به توافق اسلام‌آباد معتقدیم و امیدواریم آمریکا هر چه زودتر و قبل از انتخابات، جنگ رو پایان بده و به این توافق برگرده تا ما هم بتونیم بهش برگردیم.
ما آماده‌ایم دسترسی کامل نظارت بر سایت‌های هسته‌ای‌مون رو فورا بعد از اتمام جنگ به نهادهای نظارتی بدیم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84018" target="_blank">📅 01:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84017">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf00916eca.mp4?token=bZZxmYnydvtSw_eA1sC7XLsGzLmUCz83S06OQ7DUgMUBofP39POm_LfVbPiFJWryG53x7MSLYbyxw5LJweUUxP1GWdnPBn9eVtFCd0njvcl-ROiGQF0tmRAfpXIXejgmB6z0xq8NliT66NFA13cm0T0jAOoJaJeJyO8_VfhmjBWukJtIsJgEwl891tt9KHVAeUPJSSpMT0QVDpBGiL32k9lsQRetdhlcIVZsv-wqQg-473ejCctfpny_CUQvN6ohXfCPYHTa_YrDeUycfXWEepHhELpj6jhRGaINO6hRUT419vU8oL-e78VccWe6BCJXFTuZ2oSR46Jhx6DIgJgzyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf00916eca.mp4?token=bZZxmYnydvtSw_eA1sC7XLsGzLmUCz83S06OQ7DUgMUBofP39POm_LfVbPiFJWryG53x7MSLYbyxw5LJweUUxP1GWdnPBn9eVtFCd0njvcl-ROiGQF0tmRAfpXIXejgmB6z0xq8NliT66NFA13cm0T0jAOoJaJeJyO8_VfhmjBWukJtIsJgEwl891tt9KHVAeUPJSSpMT0QVDpBGiL32k9lsQRetdhlcIVZsv-wqQg-473ejCctfpny_CUQvN6ohXfCPYHTa_YrDeUycfXWEepHhELpj6jhRGaINO6hRUT419vU8oL-e78VccWe6BCJXFTuZ2oSR46Jhx6DIgJgzyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده‌ی اسرائیل تو سازمان ملل اون استارلینک نتانیاهو رو برد پیش نماینده‌ی ایران تو سازمان ملل و خواست بهش کادو بده که بیاره ایران اما نماینده‌ی ایران قبولش نکرد.
💔
نماینده‌ی اسرائیل در سازمان ملل: 1
پوریا عرب: 28929853059-
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84017" target="_blank">📅 01:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84016">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتانیاهو یدونه دیش استارلینک اورده بود با خودش، به دبیر سالن داد و گفت بدیدش به نماینده های ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84016" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84015">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=CTsrTlNa4qqmnCfA6r1AXDdF3o8HMO4SYZ2wcOtRmYnue_d49mECunpGJUrIbTTl1khweItWhmyCfcoF8lGW1gkrYJv0Hr1jiSN3uj6pjhjPm_DPEz16p3sIBIUEITeWxydlos9qSaO-uFPrUVek4dyeC7yyBFM52AvZUKSjzNTvIyAgobODKJGJ03VSAM5ytZ6Vo5QRX5_X2J7cvq181B_GA65ZpPtkMgQHKjGGVAFCWqtW3BCnOmKAnTEcH2NPS-Uds7Mt3S_Sza8dGBCnTLjJW8tSFTrRbRzSHvagBTshi_Je9wB5gKqR5Y4LSFYW76buN9Upzp5HTdL2PvTvN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a45f24bb7.mp4?token=CTsrTlNa4qqmnCfA6r1AXDdF3o8HMO4SYZ2wcOtRmYnue_d49mECunpGJUrIbTTl1khweItWhmyCfcoF8lGW1gkrYJv0Hr1jiSN3uj6pjhjPm_DPEz16p3sIBIUEITeWxydlos9qSaO-uFPrUVek4dyeC7yyBFM52AvZUKSjzNTvIyAgobODKJGJ03VSAM5ytZ6Vo5QRX5_X2J7cvq181B_GA65ZpPtkMgQHKjGGVAFCWqtW3BCnOmKAnTEcH2NPS-Uds7Mt3S_Sza8dGBCnTLjJW8tSFTrRbRzSHvagBTshi_Je9wB5gKqR5Y4LSFYW76buN9Upzp5HTdL2PvTvN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی بنیامین نتانیاهو، نخست وزیر اسرائیل در سازمان ملل درباره پروپاگانداهای علیه اسرائیل:
🔺️
می‌خواهم چند سوال از شما بپرسم؛ کدام رژیم نسل‌کشی، یک میلیون دوز واکسن فلج اطفال را به جمعیت دشمن (غزه) تزریق می‌کند؟
🔺️
کدام رژیم نسل‌کشی، توزیع 2 میلیون تن مواد غذایی را به غزه امکان‌پذیر می‌سازد؟ این یعنی یک تن غذا برای هر نفرز متهم کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84015" target="_blank">📅 22:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84014">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7315b22a6.mp4?token=eq7NUvzb_1Ndl447FcxSS7q8j_SwkEaeBgtmv1PraPzHya1slE-uMbCl3MEKc9G7GxYs7VNWnBsguj7eeVwvQwWft5wKId5yKeQhNQs91voDibGOxTMN0WNmxiXOLjIBil2zi_5Fev7esBOXvPIgPTcDSHMrcu7telgJW0yOOn0atf9DwEH-2Yqq-2o823TmKw60qWr0FllVrgpzGk9s5fvDvxNg8zYbdRtLoYLPRrEWIWTwMR0_Kdek-cd_qOHrmTIPFr7tSOwceXgWsoYNrHcZG2m1lAxAMSP7vY1fKUF2f6fJT2ne9kUA1k97kLpa1BleruFQsXbyAY9Qj7oIRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7315b22a6.mp4?token=eq7NUvzb_1Ndl447FcxSS7q8j_SwkEaeBgtmv1PraPzHya1slE-uMbCl3MEKc9G7GxYs7VNWnBsguj7eeVwvQwWft5wKId5yKeQhNQs91voDibGOxTMN0WNmxiXOLjIBil2zi_5Fev7esBOXvPIgPTcDSHMrcu7telgJW0yOOn0atf9DwEH-2Yqq-2o823TmKw60qWr0FllVrgpzGk9s5fvDvxNg8zYbdRtLoYLPRrEWIWTwMR0_Kdek-cd_qOHrmTIPFr7tSOwceXgWsoYNrHcZG2m1lAxAMSP7vY1fKUF2f6fJT2ne9kUA1k97kLpa1BleruFQsXbyAY9Qj7oIRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی بنیامین نتانیاهو، نخست وزیر اسرائیل در سازمان ملل درباره جنگ غزه:
🔺️
در حالی که حماس تمام تلاش خود را برای قرار دادن غیرنظامیان فلسطینی در معرض خطر انجام داد که اغلب با استفاده از زور و تهدید صورت میگرفت، اسرائیل تمام تلاش خود را برای دور نگه داشتن آن‌ها از خطر انجام داد.
🔺️
ما میلیون‌ها پیامک برای هشدار دادن به غیرنظامیان برای ترک مناطق درگیری ارسال کردیم؛ ما میلیون‌ها تماس تلفنی برقرار کردیم و میلیون‌ها برگه اطلاع‌رسانی درباره حملات پخش کردیم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84014" target="_blank">📅 22:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84013">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهوی جنایتکار بد در ادامه‌ی سخنان زشتش:
می‌خواهم خبرهای خوبی را به شما بدهم.
اینجا فقط مسئله زمان است که چه زمان این اتفاق شگفت‌انگیز در ایران رخ خواهد داد.
قدرت مردم، قدرت حاکمان را سرنگون خواهد کرد!
می‌خواهم شما با دقت به حرف‌های من گوش دهید. یک روز، و ممکن است این روز خیلی دور نباشد، مردم ایران آزاد خواهند شد.
رژیم قتل‌عام آن‌ها، با دروغ‌هایش، با فسادش و با ظلمش سرنگون خواهد شد.
این رژیم شیطانی سقوط خواهد کرد، و همه ما در آن روز جشن خواهیم گرفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84013" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84012">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde372e04e.mp4?token=bwHpm3xZcGgUW7j9V9Wp7duUpDyYCk8sQK5w5FvmForOfUUNADXHbeemeo9ytzV0De-VmW6lUYjdC3avKjTm7SiiKVuPp7nMx2xl-XofqaLg90gN6GXXoWlwCUIXVWr-PGFeDBRMSnT0h86QTeAeaWv2lccC9m4os6CfbSYmUH8gB-g9wnT7-UO2hnLJY8KLja7xNyxIs_sBd_AGjpZKc-aj3rpceTPmRMxPW6jie8N4sxTTHWnxXhlJVXmM7V7ftrlsrgSRMYXRbjo6KjHi6DsEiRdTarq3_58cjctCtUPLLAl3uzqsMSsm_WbVGh4Um36tKj3Mmh1rVfg1SZC49w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde372e04e.mp4?token=bwHpm3xZcGgUW7j9V9Wp7duUpDyYCk8sQK5w5FvmForOfUUNADXHbeemeo9ytzV0De-VmW6lUYjdC3avKjTm7SiiKVuPp7nMx2xl-XofqaLg90gN6GXXoWlwCUIXVWr-PGFeDBRMSnT0h86QTeAeaWv2lccC9m4os6CfbSYmUH8gB-g9wnT7-UO2hnLJY8KLja7xNyxIs_sBd_AGjpZKc-aj3rpceTPmRMxPW6jie8N4sxTTHWnxXhlJVXmM7V7ftrlsrgSRMYXRbjo6KjHi6DsEiRdTarq3_58cjctCtUPLLAl3uzqsMSsm_WbVGh4Um36tKj3Mmh1rVfg1SZC49w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی نتانیاهوی جنایتکار بد در مجمع سازمان ملل:
از آنهایی که اکنون (به نشانه اعتراض به وضعیت حماس و غزه) سالن را ترک کرده‌اند یک سوال دارم:
شما کجا بودید وقتی که ظالمان ایرانی، دهها هزار شهروند غیر مسلح ایرانی را به قتل رساندند و سلاخی کردند؟
وقتی که آن‌ها هزاران نفر از خود مردمشان را به قتل رساندند و سلاخی کردند، شما کجا بودید و چه کردید؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84012" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84011">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaYI2sAI_lC7Z8NkrkcYE0BJzkC3i-wtNpTmx7q0xy4-ILPS46xvvuucBVQwSSr-YQ0tMh7Kyj4IJLQHCcQ1qnNhPGD85fKJee9QgUsC0LdinXuITJJ20iAoHLbUZAj4wbHvHOTT5ReozJ45y9Sb-VGMcNmLpuyyDB-_k9eeOu6AvBrLl13US2scoZG8vPYzdcrbVHL8n7ea-v_8M6ZUVn8A4X5I3nq-8Q-zA4E98DlmqvFR4DY1R7QKIJ20_zDP1GUfbty3gFt6ihffvF74Nq2C1Gm7XGJ9avQtNQdfx86Xl9GmCpLXI1k9Suw-fVlE2US3yBP3pqAIcETxBxdLZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84011" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84010">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84010" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84009">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">همین گه نتانیاهو رفت بالا نماینده های نصف کشورا پاشدن رفتن</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84009" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84008">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/no2-Z_Bhz75HHjcicJY3xtLHnlSRz-CIgfm1ynnC3da6mgYGGORuBDAy7pWjEd2MffEI4o-6sGQXBOAGWPh1uiqclzKFMo0kbCQIp1e1vEjAqohRv-xvbrW8o8S1svgda0T_tnz54d3OQtwv9FvUeGrsnUV_23yIHVF7uUkIJ-0HumW3vUfxLn7kDNfC9He43ZnHcys6AnGNgKR9VLhghWocWAHq76iC_acC0QVn7bp_CW1IghR_fz2C5_sqc5pEEavXroAF8_HzWvRIgWkNt2ZleQ_0Vuueyk1C3PPGiTGjWr0gH8f15NCLmd_-bwswIiGFM0sl3fKUq6QQV_W_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
تیم ایرانی به رهبری دکتر عراقچی تو نیویورک دارن با آمریکایی‌ها روی یک توافق که جنگ رو کامل
(با بمباران اتمی)
پایان می‌ده مذاکره‌ی سنگین می‌کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84008" target="_blank">📅 20:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84007">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امروز پنجشنبه‌ست و طبق روال پنجشنبه‌های هر هفته، موزیک ویدیوی جدید محمود ویناک اینبار به نام "Jolly Chimp" ریلیز شد. SoundCloud YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84007" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84006">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3eea5-ZLR62WDjpbA7bOIn4Xutz7yi1Wy7P3Idmb9riihCF0LQbavbEYiJyWnpsy7OuNTd64ru5URLm6jWJezCpVRDme0g9BEKwgwDFWOlYMURYxGtv_sIKY526S0LR9zV7YacmfAFYQNxMYxaH_wOP3_ZdCtmi0ypwlLjJWrY8G_dhSFPWNPlsgw9qZ5ON6v7DdgRNqiVAfD6jw0zsFIfnJ57r5DAIuQQhivH_tLfCjA_XyfHM9Hg8mkqe-E8CdHYn8T4yMfICoyo_0ngA-Bwkv72-JxOYLRr15qgjjtJXP1p6ZLjUv4pmU1hTcTuivLj7LyQRBei9Qq9lIAatTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز پنجشنبه‌ست و طبق روال پنجشنبه‌های هر هفته، موزیک ویدیوی جدید محمود ویناک اینبار به نام "Jolly Chimp" ریلیز شد.
SoundCloud
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84006" target="_blank">📅 20:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84005">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGUExOy0kf3guGdHWPBET7tTDeHhW8-ptTFQ8xfMuE43zU_DbUhwmEWWuiX_7GgkYDhpTXo9qp1tH-Qz9wNTb3nVPhaP6hMhG2J3s1mOYdABZqu7t1hPwMkCMCifAXMRH-MljaOIEVDyYfPwF3eTi3OcqGCIHtdNdc75cVa2av-61PYTB4qO9PYf-McuKjiKh59v6Y7y7XD6g4edUUGcl1m-rydBAbmUXAn0Om_dOSmcgQnzs1kGn4X_Kd0di1h0axh8e4bfKkxQVCdWTgNq4wYyNhv2_QjIfGPcdAr9aqXkWLltp_1lPsUD6RbATlImtpz2UzE6KYpSQVLhAsYEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا امیر محمد یک خواننده ها
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84005" target="_blank">📅 19:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84004">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRrj5BtAvG6IIUp-AaLEOKZwife4KYpkTw0uEK-MMykNPWNxBtSKNv776At4vUQhn8rULatq8LVmy7oa7uOvm6iS2RUxP2xGokF4wN6Nzudgwovh-ZPe1WJxSqjoqyjWPJW4xaFvnXWI-lWY72XrgUaqb_QqcppBQY9C-MYRx_i-uPcICHowKTmiW54D2KURuKvYEaq24lkGqzWmYbf_nX5e0yfnklmlXs6cT5yBy0P7RdvLmgzqRvZNCmnop1rxCW4c6EunUMmy6MZ4fPfIgyygXpnGtP1Qw4WYX03eKF4dwcRafZ8jscK-G6o7-t6gWkUPUcdpC3jkG-78iEPxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران جذاب ژنرال.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84004" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84003">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF0O_0I7nqRlzUdtFxV6cOlqP3J0cGrRnY9RzsKQsmx4Sw03-kZBlPMAsFNkCTgajISq_-v5zZlQYMFXExwBT5d1BwB4nNzrNoZqpYjoYtvaKe3cILBaeU1IcZTLVx47rO1KfRNwpTrSTcTBp2FCpYRFFvp-xb5M08cfGmTapiWQNIb9XRCTW4cU99pQlaAA-wq3Yy3jTeY-NBW3rBR0btjhJA72M_vlmn0eTrG0qKnEl_ERpHek6F8zv5yzxFvgfGYGwU4UuSRJFdhCoUL-EXUlLlSndyBrN8k3BMrFsFDutu30ujTdzTlg7fQ-TULJRKOkX8bDpYlRWsiutWbVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G2
🅰
🛒
ورود به سایت
👇
✅
https://oqleixugysh.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84003" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84002">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=r6aaNHhsh7NSUxilKbcsKev9FOoILR2mT3NC4JnAILtyaw4n__YBLnq-bL2EEZw1jcH_6xc3PL3Be4dxFJpqUEAw90mssBlzaglr00bjRGYSoxqZVF4_EF05xTXYgsb6DiZF2jMyLfnQQ-xLssmAChAK91dTgGTIIuZ4WNnOJUP9gK6IUvqDPMp7TRQNHpzCs7IMQTwNEvwMFE9Mx0j5d9CYto5mgStzLQ0_OJbwGlCwHY51rOXWVZE4j_efEfzZonGbC0pJ23bFvkRFykVvXkTsR46scCA_vYvaJaokhNsLa5EFRcPWA63ImJgTah4Dcit0GRiAttYxDpoZvCKMnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=r6aaNHhsh7NSUxilKbcsKev9FOoILR2mT3NC4JnAILtyaw4n__YBLnq-bL2EEZw1jcH_6xc3PL3Be4dxFJpqUEAw90mssBlzaglr00bjRGYSoxqZVF4_EF05xTXYgsb6DiZF2jMyLfnQQ-xLssmAChAK91dTgGTIIuZ4WNnOJUP9gK6IUvqDPMp7TRQNHpzCs7IMQTwNEvwMFE9Mx0j5d9CYto5mgStzLQ0_OJbwGlCwHY51rOXWVZE4j_efEfzZonGbC0pJ23bFvkRFykVvXkTsR46scCA_vYvaJaokhNsLa5EFRcPWA63ImJgTah4Dcit0GRiAttYxDpoZvCKMnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیرانوند مشت زد تو صورت بازیکن ازبکستان تا نشون بده مشکل اعصاب روان داره و نباید بره سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84002" target="_blank">📅 18:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84001">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بازم مساوی بازم مساوی</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84001" target="_blank">📅 18:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84000">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بازم مساوی بازم مساوی</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84000" target="_blank">📅 18:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83999">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8KShIAi1fNKQcGqZgZv07dtz8A9S0m5zucKZ8y8bKNDp51k7PgMGzg_z9NNR-iGrsYkvK7_4dBUeQaNb5AuIVa4X2dWiejS1cNsC96gjUN3OiTMq376iCajf_rO9TpNcDbg3SiP3m9Waa313jMMKNyoailgfs7hWXhGZrVZJkmEwA9ona3Hx75wwAOPOrEEWNhp6t0_PW2afy7o42jkhoc5qXRXw2aTtEMCJ8pebdQfGQk0fUOOllNaMiwDxaaTaetCxz0OGJXAHyZN4iVzko4RjXHEgWwfIITkKh5SEK7tm7r5vofLuOK-QJOC93bVZcru2_SMPEc9N1Uht2UXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسی به هیچ وجه
ترامپ:
دیروز در فرودگاه با رئیس‌جمهور شی دیدار کردم و به‌نظر میرسه قوی، سرحال و آماده‌ست؛ بهتر از همیشه. بانوی اول شی هم، مثل همیشه، زیباست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83999" target="_blank">📅 16:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83998">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شاید باورتون نشه ولی کوروش تو چنلش هنوز با پوتک درگیره</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83998" target="_blank">📅 16:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83997">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQlhINZl1TNfHYf7MYAlXtKqX9EOYQmPNADKTq2sz_aai5cGaMzy4w-eHUB4me-3ZxRvemnC1-IkQ09PrhQQNA85defPTaovqrvPQuj3CdKrLw4Qwd_l47T0OARuVqS64wgUfBXAUJtA77a_oDFWUD-wemmJ6gViT2wUIEdg205ZDwiIrtD2db6R5tvkumtS40hP5w-ZN3qaRPHV-6PPd51JkIeBhQ0MucCnRvUORX8509BRg4HoxBO0dkifkIUB_h7h3WUpAmTxt6CPXZ1RZFnbDK5ZMQpbmKUmuTJHWSRQ-SP9OnK-3w6Jgh2fcn8rHP43vdywo5fgmWxaqIcwqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال: اینا تو وان حموم خونشون ناخدا بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83997" target="_blank">📅 15:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83996">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNQqJvgYI9bXeY3333ZZH-mu4EG_hH6FhLGvnBG0OeRaNP-4Z8g13v2dFM41WEcLWQidm-xEz0JO76Kd1926g2t7jMkYb3qhZGSI_WSThL4_FyJLh-aUAxn3arzJEqCJB0o-ft2CLsbDJIgIeY5upQ9clsiNLfPdLTRkeyDkoZQzAw08gFFA_u1tqAQ2KtoTgZImGaK8vrDdjGkAlhlShIzPNp5ovRaISLfMiJauKoC1NiVZm65L4uHmQHVZU9E7y5Q0ECL49BMuJ-nTl_TAUPTF_UMsGcUApDM-UqQ3w-um6Hhrrwh7n_jppuiA5AiLpjohfM6WYmYBq3ujgIsPsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد به سلامتی به کدوم سمت انسانیت عازم هستید؟
حموم؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83996" target="_blank">📅 15:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83995">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پس پزشکیان کی قراره بیاد بگه گور بابای دنیا ما رفتیم بمب اتم بسازیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83995" target="_blank">📅 14:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83994">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=SMyqwEDjPOrzgF63IRTBaRHX-_7wXT94siV0tx8O9UicZb1ydnhS_Km1VRgx9M-MgISEkmKGBShlmsw9jEEO0Mlvowo7-uY_-Z0UIVghyTB-Auot-5wAKcit7B0dWQYlSyt4BtjkTKoSqJQ9NHUMCcWvwQpwC_QluLsBi1JEilyRIOUZW4M8y1Vu-cn0qG3rH2FMVEZ95hgeoE1JlpKWGt0RBw0bx9jKtepjWbuklvZkmygKVNmTlo0M-bT79qzNsjOXg4lj4Yp4lrSHOrOsX31olHQNw4ES5LKf288BZodV34deW6kwuHH1rdM-jST6V1IyZ1M7IMmKif-3uk_5gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a90129a70d.mp4?token=SMyqwEDjPOrzgF63IRTBaRHX-_7wXT94siV0tx8O9UicZb1ydnhS_Km1VRgx9M-MgISEkmKGBShlmsw9jEEO0Mlvowo7-uY_-Z0UIVghyTB-Auot-5wAKcit7B0dWQYlSyt4BtjkTKoSqJQ9NHUMCcWvwQpwC_QluLsBi1JEilyRIOUZW4M8y1Vu-cn0qG3rH2FMVEZ95hgeoE1JlpKWGt0RBw0bx9jKtepjWbuklvZkmygKVNmTlo0M-bT79qzNsjOXg4lj4Yp4lrSHOrOsX31olHQNw4ES5LKf288BZodV34deW6kwuHH1rdM-jST6V1IyZ1M7IMmKif-3uk_5gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور هائیتی یه ایرانی درون داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83994" target="_blank">📅 14:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83993">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اسکات بسنت: نمیدانم نمایندگان ایران در نیویورک چگونه قرار است به ایران بازگردند.
پ‌ن: منظورش اینه هواپیما های ایران تحریم شدن و اجازه خروج از ایران ندارن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83993" target="_blank">📅 13:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83992">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">باورم نمیشه برا یه سریال نگاه کردن مجبورم ۱۰ تا چنل صیغه یابی جوین بشم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83992" target="_blank">📅 13:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83990">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=mTTv7AXvFK5zmWp8_SJ5P8FdL4jiji8wz95wmOXOx5eScoqyI25PHmfW3IqVTBDAawIate62zhqpjbi04aMj5C-KhH4IY_YdJUJXoa9DyVUhDB8tv2z0274883xoHuO09C6fau1aKHPb31PV8IDJZL4emkC614zj9L7Ks5edz4csm5n0HHWd5aPP8WT2rg2ZPUeD6FYk3SBgJ2t6j5qYwInhqsfGDo3wUR0Q6wgArVMI_pLjo7PtszbWrwod9hRsFj7w1mRkQ0JSHsiA9Vjhbi-VED45N7QObq83T1MPWoO1PyA-QjwgX65S1VHNQjfb5_siNL_d3R0L3rwiUT16-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d913b3b07.mp4?token=mTTv7AXvFK5zmWp8_SJ5P8FdL4jiji8wz95wmOXOx5eScoqyI25PHmfW3IqVTBDAawIate62zhqpjbi04aMj5C-KhH4IY_YdJUJXoa9DyVUhDB8tv2z0274883xoHuO09C6fau1aKHPb31PV8IDJZL4emkC614zj9L7Ks5edz4csm5n0HHWd5aPP8WT2rg2ZPUeD6FYk3SBgJ2t6j5qYwInhqsfGDo3wUR0Q6wgArVMI_pLjo7PtszbWrwod9hRsFj7w1mRkQ0JSHsiA9Vjhbi-VED45N7QObq83T1MPWoO1PyA-QjwgX65S1VHNQjfb5_siNL_d3R0L3rwiUT16-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگیرو رو استیج عصبی کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83990" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83989">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نارنگی برا پولداراس ما فقط سرما میخوریم
🤙
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83989" target="_blank">📅 12:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83988">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/804d882599.mp4?token=CSU4FzfABoXho8LaVviaF1oVT7zDCepwm4l-rc12Q5jySk6PQS_jVyli3PgFciJ2a5o7lcByesK_YzDKG5O3qX_Nt-eoHxk1fzylDGFrMF7ZjIdOTlACFCKNL0baSGXIRcUCsAsaUJDLBNStHnOG_TNnsO5FTEh7yGM-9iyCDuX4oh1OR4qiTBkxD2lJfXefRw7vGfXQlhPgX-iENV7YXQJzjipy6_or1zK40zXqI-qFYbHACDaqllWMR0sTRiq5iv4xC0ZQClMdD-q6GwuUnO17gyYyJrmeXU43E17JDhdHUkIEQwO1uxmJgkD3R09pudCrSaXphyGad85oEMHKPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/804d882599.mp4?token=CSU4FzfABoXho8LaVviaF1oVT7zDCepwm4l-rc12Q5jySk6PQS_jVyli3PgFciJ2a5o7lcByesK_YzDKG5O3qX_Nt-eoHxk1fzylDGFrMF7ZjIdOTlACFCKNL0baSGXIRcUCsAsaUJDLBNStHnOG_TNnsO5FTEh7yGM-9iyCDuX4oh1OR4qiTBkxD2lJfXefRw7vGfXQlhPgX-iENV7YXQJzjipy6_or1zK40zXqI-qFYbHACDaqllWMR0sTRiq5iv4xC0ZQClMdD-q6GwuUnO17gyYyJrmeXU43E17JDhdHUkIEQwO1uxmJgkD3R09pudCrSaXphyGad85oEMHKPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شی جی پینگ همیشه یه نگاییدم خاصی تو نگاهشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83988" target="_blank">📅 11:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb0P3UJjFN-C2zCN644JY2LLaNDHi5pShl1FnnKQnUG7exHfgWqFZ6rezE1XbTQLPxX2-JrtffgoaWNvgD7oIrTMOfgHFd7FrmxtAEbixPtQbMU3ZypYmxOFAEHAIduerxvF94hxy69ffBxj0QvwpNmEvFXVP0D_u_LJFbmqw7RUs1qmDFZD6SYe0uHHtz20nqAUnh-Cpy4XyTWgrOlG0Y3xW0QGl8hcPGBacgWDvGMOQrBEFDDmw-uv95CRIqlOybhe_pm_wiISNhyUk5tyjj00-1uDinnaJsjZZwuL99IwwBhqbP9AozaEYVJ_k9fcEguO6ShExil_d2SPyFRl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
نروژ - دانمارک
⏰
ساعت ۲۲:۰۰
🌎
📲
پرتغال - ولز
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R2
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83987" target="_blank">📅 11:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGRsXlijPIM4upvEZClJ0gf2ljKC5Ag6vb5VUR2BV1D7b7QsIGknH_iqSrtc9CTAqG1_AzYpjnrKFL8HxY2Fg5OKkh7mYAP1-qobooWP2lo9kZwkw-zobemvA5kW1kn2XxbMwvFtEPk3PVEKVo41ZUeUOhQEk2psSOgtUPpwQ3JgUJCGBllqyR5wlAnq4Jd3iwxpSzizZUorji4EJDtRIG1TXJhuDws55eZHea9VTKtD2ykEHl9DtOav30WsSrHwA7pCRphZkCLY3303LJ05PH-XjLWLMtfuFyT7aUCG1jY7NTpcbSooOKYcR7m1U_db1oPBSzuW9qFvPCzSdWZHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش شبکه خبر از اول مهر و بازگشایی مدارس:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83986" target="_blank">📅 11:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83985">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSGgDkarG7G3S4tBDOTSyG8ifytznygsrtU-UOBl0MYC7VROhp9S_6e39otrWdyLb4O_GApBz13yUa498ix-nODR8XvTT-C8I0ILGLmfNYv5kgGQ3ZfwL_N6TiHtVAPQ4UK9Z8yOKQN7opBXJq91iVTJq6WURWYG0yG394U35-VDUx2TLNz-yEsYqKEhfWjS9vvfUA3R64mTvJOqPnVA7d8hX0ANqyLHC_baB2YjaSs6HjOobKQSC21aJWOHOd7towtqWhSkm-Q_2KCCNOwoeAoN6ZgYe1UomXy9_jZIJ9aM2tzfu3yvaCx424hlGEM0eJxB2O2l0B6vE8OvE7jL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسپلورمو از این کصشرایی که با هوش مصنوعی چند قسمتی درست میکنن نجات بدید
مخصوصا از کچالو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83985" target="_blank">📅 09:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWscC0oLjmYqwddq4VhIIgzwQYuqo4bjQkFjpuEHicr6dMB53DktJtD47btPLVVvD-nNFFnhpI0-xxyEdQ1PQk_9QKMCDHE7l8wrRT-X30jWoqx0ke4AMh3bV0ditmJFGy0uRPQ6KUlIhOKk41DLZG1FLfI2MfxNRAneGB4S3TOXyDau7wUUvSPJ-S2RDzu9V5h8JcR1i0nsYgnPggqLORqn8q-F-l5QeoMbX8Ih63Cl7OX02qSuZZJugxZYxLLo1v0Lo9sTQfDweprDqd3FOKAb2t_CaBGFMqUYzPftkVX8shHu7_mk5XQIvXj-EVOEivAhah5AAnUas35TM_oYVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83984" target="_blank">📅 09:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83983">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogzuVybHYTxR1BIzJFUyJ88ZfnVKS_Zoe9UL2nOL9SpOmGIhK82Y4n1n43Q7L4q4rPn7_Xe5vu8DXxkI-hV00Mv1SAmJtwVfk5OB5jY_1o26m2CiXeA6kM-WKaTVbRLkspxBLaveKVgo5GdySIWSvABR7aHaMIC8KujVz6qs7cfSN2uvaVuUMkYiwTeunIdZxv51-2N8nxK1vNKDodI1GSjBthDv8OjxmZM83LsVObkLSSKDwidiuAbzZxRfkmSgOeAMx3fElsALj5ImV-2RT2iOO5RH0qmhoZO8UefFeVkttZbdN0KrHsHzrVcbpgaAu6Z4nY-51wgEFVzgeopq6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید پسر شایع
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83983" target="_blank">📅 23:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83982">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بانک مرکزی امارات فعالیت بانک ملی ایران را در این کشور ممنوع کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83982" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83981">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83981" target="_blank">📅 21:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83980">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.   Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83980" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83979">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLOnGCn9c8eUGYwLO8s4t5YnDOMDgXOs4gJ8buIt-VZz4v8RrOvQMfbyrIyDQu2NNKX8fG0XOFeHGR09h4ww3mc9il4Hu3xXllssrggodot8lBKPVqY_veybo1gJ9usfGn8GH1z9LUQmlwWTjIyCkGjc4xo0Sjro-ZQ0BaybMqXKlB8O4VpRCDWClPY6abclq5O4xZPRUuFWCD1YIBtwLmmBvz-TbqOaJU8uz7w14mJzMxZEMunAQumRSxfL8DxThGl2yEFnNK2Ix_5EjYFTBrkmlf1MCY8C1mewXKXo0TM-uDX6NHPmAOJZCwkuPq7u5qNuW1LK0uoY7A3jugXzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دورچی به نام “WIND”منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/83979" target="_blank">📅 21:12 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83978">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=EpGDLHCnhoUKYxObG7Q55Kbhu-OGvF72YHQaf6zHY6I_zv9BbDSOfbwsmWstHMj8gS4vV3FizzkFqsdU4lEhJ0okkAr6tMhJyPRF1aRKpgP7Wis4LO2muTsGd91BN3qu2dm3rJoGdsNc3KI15MWgz7k7X6g6fSQll4ltoHsO6L2KjBk3jFBo4SzXmLJZLOkohzz4_ZVoHIHK0kxHZvFU8a643VzZgbzE-gTQYN6eulzoPbdVpEVMUx7z1MnXlokUiOiXLJg56Vwts_45t8SPaTzqiswOzeV1tcHDgmORF6hf2j-6GSJea5WSV2bWbVNDuEApfmZy1VVDX8kL6be8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e7880dfe0d.mp4?token=EpGDLHCnhoUKYxObG7Q55Kbhu-OGvF72YHQaf6zHY6I_zv9BbDSOfbwsmWstHMj8gS4vV3FizzkFqsdU4lEhJ0okkAr6tMhJyPRF1aRKpgP7Wis4LO2muTsGd91BN3qu2dm3rJoGdsNc3KI15MWgz7k7X6g6fSQll4ltoHsO6L2KjBk3jFBo4SzXmLJZLOkohzz4_ZVoHIHK0kxHZvFU8a643VzZgbzE-gTQYN6eulzoPbdVpEVMUx7z1MnXlokUiOiXLJg56Vwts_45t8SPaTzqiswOzeV1tcHDgmORF6hf2j-6GSJea5WSV2bWbVNDuEApfmZy1VVDX8kL6be8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دورچی بالاخره دوباره مواد رو شروع کرد
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83978" target="_blank">📅 21:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83975">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-5LaDKKBmiux1UEAbc7-YKjtVuc3emqd8leYBmX-KjHwabk3ZnrOxXlZNDH3Fw3OwrQcJHRfWK_dm7XlNpiThF5ayyyx5m3yeQ0Spy7hvGmiCqndW8MDtT4M5TjSUvqGdANMtR11B8Ey9MKPDpRSmFvFG4lo2Anf3ZhaFWsaFTcLRIyPfZcalQIq3ye6e53tbOIMLpSYbZg_ZSe4F52sptCoSUco_ZPjrTtyc_6KICiJLRKFiH5HD1E-OAR4hEEnEkcp9xi4vZePRMIiDvxMqnmwor03XEnY15hJj7sTTO0uqWXxGfkDrDW1oyXTzYFKrJjpRO-Q8WNwC1jheMWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی دو روز شکل آدم بود باز طاقت نیاورد ریش‌هاش رو بگا داد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83975" target="_blank">📅 20:41 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83974">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b34ea74eb2.mp4?token=Ma8J7sJudKsQYl4u1oHj8e8XBu-TM5x4nfq8WrRuYr80p_jcQbADYsfMuMZatqPTQqlz8FHof-kosL-3AUrTxfigwaIobpPScGBl3bY3mvAthu9ORWRedmTcbM4Os98hNqsxxi3-pQ5hNOisTH1_3gJYNsXN25-UdulGSus-JhpbDxhxL66s1WCsRrfW40HVpetzAy1Mo8_EzsAbuYBj2WC44nwGClsqKvSJrBt1Apg4-kUzJgxCLHdF66nqIzPxf9_IZIRNOR9cXqx6n5-k7rLg7cv94pzKjaQ5C8z-OuEUDKy1Z3Td_dD3hb4V99eEzu_hXvtqVvIjNqozxTl7zZzYVNMUCw29OJDgKv1DXdpeCide40iqtgZVfPlYBUq5UsnoDw0kEXJtm1b_WVEAaW2O3EeE8edKVfEel4KLg7vVdmFB93xG0LPZZNmr_QcXkFQKXZ9d7JAOoKRe2atHIgySTMClFqbt7z8nfilz_hDorUSZXLzeDHQ2N8oTcu71KEE0VqnijV6y85d4HD22J9BQOez3DxS5ME98g8NVH88Upvn08H4hfnXJ5Wostv8ji9ptnLJDGGTG-fQea17Jn16BcSma8epVLvkChbVAwXGcHhO6UN5VtfaD1CfF3k98L-GgBQaI8FFjOyo3RNfJ1iG6ar3VxUUcG1pbguOw3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b34ea74eb2.mp4?token=Ma8J7sJudKsQYl4u1oHj8e8XBu-TM5x4nfq8WrRuYr80p_jcQbADYsfMuMZatqPTQqlz8FHof-kosL-3AUrTxfigwaIobpPScGBl3bY3mvAthu9ORWRedmTcbM4Os98hNqsxxi3-pQ5hNOisTH1_3gJYNsXN25-UdulGSus-JhpbDxhxL66s1WCsRrfW40HVpetzAy1Mo8_EzsAbuYBj2WC44nwGClsqKvSJrBt1Apg4-kUzJgxCLHdF66nqIzPxf9_IZIRNOR9cXqx6n5-k7rLg7cv94pzKjaQ5C8z-OuEUDKy1Z3Td_dD3hb4V99eEzu_hXvtqVvIjNqozxTl7zZzYVNMUCw29OJDgKv1DXdpeCide40iqtgZVfPlYBUq5UsnoDw0kEXJtm1b_WVEAaW2O3EeE8edKVfEel4KLg7vVdmFB93xG0LPZZNmr_QcXkFQKXZ9d7JAOoKRe2atHIgySTMClFqbt7z8nfilz_hDorUSZXLzeDHQ2N8oTcu71KEE0VqnijV6y85d4HD22J9BQOez3DxS5ME98g8NVH88Upvn08H4hfnXJ5Wostv8ji9ptnLJDGGTG-fQea17Jn16BcSma8epVLvkChbVAwXGcHhO6UN5VtfaD1CfF3k98L-GgBQaI8FFjOyo3RNfJ1iG6ar3VxUUcG1pbguOw3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب رو بیت کاگان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83974" target="_blank">📅 20:09 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83973">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_NDbFKUty5oNHOsQeHucBAmP-FiIF2BqsfNCJtSXk1su1OwAzTRVnnVAgBKn3_X3SYvb-j9DTUzeLn65GB34sswhNXt-23ZIj226ktGvfK3dohOJJR_Y1JFq-lEPzri4F8q32m7-IuX59BNE6EzgpDu_z94NVq1t7RQoyQoMSG618lPxw9agl3090xLdqAoRAhhmZryO1wnw3_CvYovoJHFF82e3DhCyeP4N7lp_eJicslV_63ie1N358wxPDE3zaIACCeQWdrcqhrkT6IdjH5AffnA4ltYUu6qoaHiTEj4yYPfIwMCVCYyr4WW8NJj6ALUrmfoP6SIOYXk64PR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قالیباف:
رئیس‌جمهور پزشکیان فقط از طرف یک دولت صحبت نکرد؛ بلکه صدای یک تمدن ۳۰۰۰ ساله بود. او صدای قدرتمند شجاعت، مقاومت و قدرت جمهوری اسلامی ایران بود.
زنده باد ملت سربلند و مقاوم ایران.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83973" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83972">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اینهمه بونوس و جوایز کجا دیدی؟
😍
👏</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83972" target="_blank">📅 19:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83970">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42f87a67.mp4?token=ji4S4ok3PCr_hEkO0dX2p3umnbs8fW-kmJ60Og8bE8g-WmVkwKdLb2Em17aXDaKM3qmykkdKLlMj6reyTKyi0cUKebl0I5k5a1W4RE01JaVjtVI7Ja_UkzU5YbhNNlnf3pyKx0k9DEBXUSlmgzJUs-D4FWS0rRZE_X9i4DwPYj0A0ZzOviiJ35M3b6CwD9oR-uNmLAlbu7iPuQJ7xRV5SPSiDWrhRIsNMp-QPSKJ2ywberNmJk311H8mekJom6fqbxxLVNSCFGE1OicSh5fANBgmWTadiIhNs_buzapU-9So7uGqPzcYD7hG9g9MS2r4ZMAohKjaGZtDnSFNZFRZcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42f87a67.mp4?token=ji4S4ok3PCr_hEkO0dX2p3umnbs8fW-kmJ60Og8bE8g-WmVkwKdLb2Em17aXDaKM3qmykkdKLlMj6reyTKyi0cUKebl0I5k5a1W4RE01JaVjtVI7Ja_UkzU5YbhNNlnf3pyKx0k9DEBXUSlmgzJUs-D4FWS0rRZE_X9i4DwPYj0A0ZzOviiJ35M3b6CwD9oR-uNmLAlbu7iPuQJ7xRV5SPSiDWrhRIsNMp-QPSKJ2ywberNmJk311H8mekJom6fqbxxLVNSCFGE1OicSh5fANBgmWTadiIhNs_buzapU-9So7uGqPzcYD7hG9g9MS2r4ZMAohKjaGZtDnSFNZFRZcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو:
من فکر کنم تاکتیک ایرانی‌ها اینه که منتظرن چون فکر می‌کنن تو انتخابات آینده دموکرات ها پیروز میشن و اگه پیروز بشن دیگه ترامپ مجبوره بیخیال ایران بشه و از جنگ خارج بشه.
و خب جواب من اینه که خ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83970" target="_blank">📅 19:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83969">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تسنیم:
عراقچی دیروز خودسرانه و بدون اطلاع دادن به نهادهای مربوطه و مجتبی خامنه‌ای، زنگ زده به ویتکاف و باهاش لاس زده و مذاکره تکنیکی کرده و برا همین باید توبیخ شه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83969" target="_blank">📅 19:00 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حین سخنرانی پزشکیان، نماینده‌های:
1. ایالات متحده آمریکا
2. بریتانیا
3. آلمان
4. فرانسه
5. اسرائیل
6. سوریه
7. لبنان
8. عربستان
9. مصر
10. امارات
11. الجزایر
12. لهستان
13. سوئد
14. دانمارک
15. کانادا
16. ژاپن
17. جمهوری آذربایجان
18. مالزی
19. نیوزیلند
20. استرالیا
21. جمهوری خلق کنگو
22. اکوادور
23. قبرس
24. ایسلند
25. مکزیک
سالن مجمع‌بین‌المللی‌سازمان‌ملل رو ترک کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83968" target="_blank">📅 18:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83967">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83967" target="_blank">📅 18:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83966">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=trF_3tftdpAhZRR_8J_sbU_KVPezkvLOol-VLV8_5BSSrmZE4lufOBeJfnZ-fpWVwyMk5BU0H0hjhPUhc5n6_4TJvyhgnXtfhL4IS2pvYfqDV_UYOoZAC0fmhvCyVvVukGrTQNWTYz5JD7FUCSt7wj-VKD3kiRjZFtQJMV3rz1e3bqyKvIhR3KnGP9veYJI2D0PWYcmo-tmPvY_eleElPrJX-huivLPTSBKmcReE8-DqjnGBBOK9BWy5ejO98F8VoYuAsYBRDnAOTkdF0kaPtj5CI9ZFtQJU9zHBZfmWpNj1ADIdzi-DZ8Y6Q7MmqnTErHIDBRCgXkQLwAVQs1BnAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdad076ac.mp4?token=trF_3tftdpAhZRR_8J_sbU_KVPezkvLOol-VLV8_5BSSrmZE4lufOBeJfnZ-fpWVwyMk5BU0H0hjhPUhc5n6_4TJvyhgnXtfhL4IS2pvYfqDV_UYOoZAC0fmhvCyVvVukGrTQNWTYz5JD7FUCSt7wj-VKD3kiRjZFtQJMV3rz1e3bqyKvIhR3KnGP9veYJI2D0PWYcmo-tmPvY_eleElPrJX-huivLPTSBKmcReE8-DqjnGBBOK9BWy5ejO98F8VoYuAsYBRDnAOTkdF0kaPtj5CI9ZFtQJU9zHBZfmWpNj1ADIdzi-DZ8Y6Q7MmqnTErHIDBRCgXkQLwAVQs1BnAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت آمریکایی در حالی که پزشکیان در مجمع عمومی سازمان ملل متحد سخنرانی می‌کرد، سالن را ترک کرد.
این درحالی است که نماینده ایران زمان سخنرانی ترامپ محل را ترک نکرده بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83966" target="_blank">📅 18:24 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83965">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDSOR-TY7ESf338ekPiAWtuqgzoQIXM-FDHC9N0ZmKFmg0lkfsBRmXM8t2NzI9NF1FsSYKBn7n9kX6E9ddjA_UFuk6ndKiSSyAY5ch6_sddxn-j2bbLwdSBmvvPfuRYoSsRKtRPqt_XTvQc_eeCR_YzCl3Sbd0yyTYYYQtjCpZLa0joyuRJHhs-dCr0lLmQQjJQhbWW2teiLLGDu5p4Tl2Z1jCzG4smy0fsg7d-pSTq8dExRqEsBdAl3H-1_hxfESiCcH4gKf3Gpsk-ucoz3QxRcJ6kYjKGD83KiY0C_SxB5UauPqUVe12lWL44D84vc-gxW80QdfEcBn-v0-F1LPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان با عکس رهبر قبلی جمهوری اسلامی داره سخنرانی میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83965" target="_blank">📅 17:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83964">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAv_ibFf9pVmeO5qmrQi6l32YK6FlGeF96XrkqWaRP0wGnLzvHLECPSP_x7l2wTaCBpRSBruzIZbjCC1wMAiJD0N2wBeBtdjnXTDlvr-iG0l0hI05fX9pPlELIN9U6d0_FpwzgWJW8fk1QjhpUFpEdHlTUUCn8iMMEdtGd17l6PBbxRtHfz1mCcNVb0BfteGjTuZWAB4OgVtipwtTiI95TLijBmABKOVY4-ey-u11DWvDoy1FICH4hIAfAHGbaHilQCSUfTu2Mt5i65GXLpanoMRGzM7VDIcF-hdNq-vJLGY0QCdAK02zSSK7n8Ts-0rI-MBvWm7w_OEl_8ZlsCXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظار کوروش از فناش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83964" target="_blank">📅 17:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83963">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تو سراوان باز بین نیروی های نظامی و افراد مسلح ناشناس درگیری شروع شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83963" target="_blank">📅 16:16 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83962">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🕸🕷</strong></div>
<div class="tg-text">اقا تر بزنه ابرو ی مملکت میره</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83962" target="_blank">📅 15:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83961">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO20UTQ3qSCBDfLrGn-vwSx1wjpD2OoDdteh5ZO_6Td0Rn9QNR5hBDR29bP421oKWs7VNlwVNElfHWosU8UOtzrbjzdYRQRY6CuDOmJHJPkzJthrE5jrjwhWXi46YKDInQ_BJtRo5nZVfkyDbsCUSM2yjTV72u_M425LgVSLyJ8aEvr7M3GmY0SgReYOBDUaXX2zyGTGVb4Lyfh1cXf8zRrFTYnrzMAstj6b23BoJ9qYBnU4Cel8nOfZ115m0H96rcfKPriOzO3IeNbl0REu4IUJjklgNYIi78LROtZVXwtJ_qPcLbGa3wID4lEz_5AkePRJm0FxbrN70x7EKxJ4QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بترکونی رئیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83961" target="_blank">📅 15:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83960">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کوروش وانتونز:
به زودی یه برنامه یوتیوبی میزنم که هیچکس دیگه نخواد چنل پوتک رو دنبال کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83960" target="_blank">📅 14:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83959">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">استاد خوش چشم تحلیلگر ارشد صداسیما: کیری قوی ایم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83959" target="_blank">📅 13:45 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83958">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شرکت کننده های عشق ابدی قشنگ ۲۰۰.۳۰۰ سال وسطن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83958" target="_blank">📅 13:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83955">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEHjDS1Fa8JM4zTq97g9THC23M7Vqr298uesi6TYZjK_l7uRPxF3z_3Eyn8HWTopTsTsQD7eRaHDXL_4OmpSEhZUrEkMpToD3jPym4xufEG5Cj2KAqmAeBtWae43iYmpDtT3v4aCZ_tTZb13eMTvhTsW-ypAf4kCWIah6A6SLKLgxtpA_868lMoC8nhGAMYKwD-4W3cR5EvGHGjPV0DVB51zeY7MftvZpM-wR9n6OAjmD1et8fHc9vaVTJpZeD8Pbw5i8JAjY2gYhmoViJAM3FXfFAmLoTnjc7OqiHECdP4TUX64-mxXira3dlcOllhPHBO0SC9aom-LdKsqnKQABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو حالتی هستیم که تورم به ۱۵۰ درصد رسیده، محاصره شدیم و هیچی وارد و خارج نمیشه و داریم بگا میریم، به دلیل بگا رفتن پالایشگاه ها و پتروشیمی ها و کارخونه های فولاد بعضی اجناس تولید داخلی حتی ده برابر شده، تو پمپ بنزین ها باید دوساعت صف وایسیم که ۲۰ لیتر بنزنین بدن بهمون
و تو این شرایط دغدغه‌های ذهنی ویدا سادات:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83955" target="_blank">📅 12:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83953">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odeHX-OG4R2S1ZE4eQvFeNV6yHMmXkXLBBMKIZkXOmgLuaY2OmEvVAAxXBb9z-SeG2bzp-gGtdpK_DZI-8M4Nb9KTjqLBJLiJWy2CUTJ2MLP3Ovp1s2qsytOkXC8mH2VR2AAneAAkw_m9ciV2PZ_U_gmDjRqm6XWZve2F1Dkw11nPIufe4lbh9_f_JLLUtZ3sPpUvNZ-wOAm4EK_caKphvrZLM5w2mQJec-Fo5spVK1_3ElKRqEijZEbtCxCwfzME23MCQ9dxzv6axMKiRxQkYfQu4moGGVYeKB7hjXg6fO0jsvgNXs-xHN_Ff6om0-X1PRvUn4W7iuD2CqKcNU-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاپیتان بیژن بودا، از خلبانان نیروی هوایی شاهنشاهی ایران و از اعضای خانواده نیروی هوایی، درگذشت
او سابقه پرواز با دو جنگنده F-4 Phantom II و F-14 Tomcat را در کارنامه خود داشت و از خلبانان باتجربه این دو جنگنده به شمار می‌رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83953" target="_blank">📅 09:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83952">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اونی که امروز نمیره عقل نداره، بچه زرنگ امروز میره با معلما رفیق میشه از شنبه دیگه نمیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83952" target="_blank">📅 09:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83951">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مدرسه چطوره</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83951" target="_blank">📅 08:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83950">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyyvGvX2xyoY52BKUz4AZpof10lNG-gvW6FuDOZXJi-qr-FnFSrnmfZdoyHkmSOphRfBveM0T07rY6c9ynBrtPV9BeGZ3miS5100Tb7UvE9U-zIn3wllmpIp17d7LkR9INV1hBLdMFV3dZ34nbI9wlG8d7vsC6FIs8ON6HIG8lQOkc_efhsTRXYWZ8_X7lkZIc06mimIlLQejd6EilydbIWiqh7r28oX-5ffkn7SjUt2mI6iw2ZPUNynOIOM_rGlO6WalyvHCuQW_om9c9O2a133RNfC2CggAPJhsPlLtWFCCw_Ur-hhTHXHnNJebxupBNBtAAo9ZltDGT6Pe7anfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نیویورک بگید مسعود اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/83950" target="_blank">📅 03:08 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83949">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آخجون ویلسون دوباره مست کرده</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/83949" target="_blank">📅 01:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83948">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر پسر عموی مهدی چیکارا میکنه سپاه یه موشک ول داد سمت یه کشتی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/83948" target="_blank">📅 00:59 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83947">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7044b34344.mp4?token=Q3V5TtQ47uv56puVjLORZ-pP9bXpmfU8iRL6OyIfiBh2eZN6u-0yctvN-Ot6-gRCsb7jTNfG0CGAjqKIohLSBjNDEvo93lHn-6XuFw4uIJsn4vqagdD2dhyDIA3EvekPt6sQqrdHURH767rFI4P5bQx6tYg2DUAO-1hyl08UVeQknQv_IohddB176AwZTx_BrstD3Dl_h-Fstjuc9xwGWaijU34OPEXWSBjV7fWHP36oC1ruDpj6vJ2bwU8VqRgJSwu_D2BUg_WD1xhT0GlacfpVEbZnkj_TmRrhN49-T_ci2F6-r4L_mX4epEPKtSLVntKAKi-wNu6rdqsm7YSxjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7044b34344.mp4?token=Q3V5TtQ47uv56puVjLORZ-pP9bXpmfU8iRL6OyIfiBh2eZN6u-0yctvN-Ot6-gRCsb7jTNfG0CGAjqKIohLSBjNDEvo93lHn-6XuFw4uIJsn4vqagdD2dhyDIA3EvekPt6sQqrdHURH767rFI4P5bQx6tYg2DUAO-1hyl08UVeQknQv_IohddB176AwZTx_BrstD3Dl_h-Fstjuc9xwGWaijU34OPEXWSBjV7fWHP36oC1ruDpj6vJ2bwU8VqRgJSwu_D2BUg_WD1xhT0GlacfpVEbZnkj_TmRrhN49-T_ci2F6-r4L_mX4epEPKtSLVntKAKi-wNu6rdqsm7YSxjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یعنی کیرم تو این زندگی ای که من میکنم
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/funhiphop/83947" target="_blank">📅 00:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-83946">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ناموسا بعد از بیف وانتونز با پوتک هروقت چنل کوروشو باز میکنم یه کصشری به پوتک انداخته، بس کن کولی خسته شدیم</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83946" target="_blank">📅 23:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83944">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lK3WKK0qlqVJR2l3il8w7TbdLB3o8oca4X8a9OPTmBAUsOi7KIvf-2SJUkEL3OBzBHWgt1jfFdhgaO1n13Z0ID7LAIVOeaHQYNlvO4FP5oGJZ5fOw9DqzHYldwHa7-b70HauTjrfzhV0xuINEjzkJV6KuECHD8SwjLAK9Tj7sevj7Iqxv6PVpw8OwuItK4Gh3gvmPninaOtizIBQpQUuDgvVuNEQ5JJ_uJaZZUPLG55_SAZ0ABD5hhYr-AJzmy9-u5WAawit9qr35dhsDLpSLlqe4pn-JhunC9eexrcpoPAlof5pzsh8jvcRZ9AhpQJcoyymLx_YABbiIkSjrWKaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MHATPtEQAOOWmzWp7LwQVODnD2zQWVaFpGkD9byN3dQPYSn4KKYnaKCslXmDNPaqIh0HjKot97BKVLsCBGqnrqGZMWlCzF0Thsjx3y08Bris1A_prFzp7Dsw2cBN7q1AM5g9-Q1B2F58S_xI7RInb2JerLU0AvNUHvyOnxeCBVMzMMeeeuOOgpILR7JlD2MGkWLjRMK10kjrywJY4hj1DIy9MUZosErIUtnzM6z56X0lDTzcfH9fxD6ANY0JUKafNuriZO7Oe8S8VQW2b0a2s5Fxd4L_w5mmxWOGTnZCEOOu_KYX17RkbFJ3FJ9HGGmqKoBkrm0glfI_WAFPNUNPHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پول دونیته ها حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/83944" target="_blank">📅 23:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83943">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=SgVVCI-Emkm-5MruiGeLsC8cIHavdmHd1gYRP1iwoGvg3dPptCZfg2sE9oYe5SB9QoiKkMAUV5sn-hpES3ZajdefbDSjfgvqEbdOttj5nOx_uDtYizi7RSvQoMAFc4iTt6F9u23ID1vgTQw1vItJKifB-24dsojWTd8DhHgmUTPXekUXDWEye25nR6bWRhxq0FOivYPH6Pm_1WqNBskkALjJD3_N-BWHEnByEPSqOMHaOtWPA5Gz1xOTHf3bDXiPHIvpLkhrJ8-2Nnf-dRkcmXW2L1GxkSA9jIYvLSSa-I7NuKdWkptcsjoS4Zsckgy3-LleDFrHlel4wBK0Fh6GLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f44a5e37f.mp4?token=SgVVCI-Emkm-5MruiGeLsC8cIHavdmHd1gYRP1iwoGvg3dPptCZfg2sE9oYe5SB9QoiKkMAUV5sn-hpES3ZajdefbDSjfgvqEbdOttj5nOx_uDtYizi7RSvQoMAFc4iTt6F9u23ID1vgTQw1vItJKifB-24dsojWTd8DhHgmUTPXekUXDWEye25nR6bWRhxq0FOivYPH6Pm_1WqNBskkALjJD3_N-BWHEnByEPSqOMHaOtWPA5Gz1xOTHf3bDXiPHIvpLkhrJ8-2Nnf-dRkcmXW2L1GxkSA9jIYvLSSa-I7NuKdWkptcsjoS4Zsckgy3-LleDFrHlel4wBK0Fh6GLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا این شاهکارو یادشونه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83943" target="_blank">📅 23:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83941">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRapBadVpn - فیلترشکن</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1Lf8e89qB0QJplF5J9Yrs15yLqyh-tftnN25J6Ar0holfsuiktW3wqYRzqNUJK0PbPqc-IK4ZsR8FeESognqmPq55qxCEAoL0TFlKrtqqFreDr8dCyDsCl0hrxVCAyDP2T0a8bwfnSLP0l4gvmGXAyXj8UgVzuMfo-c17mUHDErlMPJrIPNN95lVvPFqE9XEQMSOr6wFE98ArjCuejw-Ni4J4DMbcYo1dRAF6zArgNTXLtFNz0Uwm65yLXX2K7h3DDsXMFyTJciwESO5LmpjvJ--Gbmw0KqrqIcZZtyD97DGmXpQ6ytlScm4NbJC2p1Y-YtB5gmUjMnnzgR68ajVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
وصل شدن آسونه؛ خوب وصل موندن مهمه!
اگه از قطعی‌های پشت‌سرهم، سرعت پایین و عوض کردن مداوم VPN خسته شدی،
RapBaad VPN
رو امتحان کن.
🌍
سرورهای متنوع جهانی
🚀
اتصال سریع و پایدار
🔒
امنیت بالا
📡
پینگ پایین
💻
پشتیبانی 24/7
🔥
بسته‌ها از
۴ تا ۱۰۰ گیگ
💵
هر گیگ فقط زیر
۴,۰۰۰ تومان
و مهم‌تر از همه؟
لازم نیست به تعریف ما اعتماد کنی
😏
اول تست رایگان بگیر، کیفیتشو ببین، بعد خرید کن.
👇
ورود و دریافت تست از لینک زیر
🔺
@RAPBAADVPN_BOT - Test
🔺
@RAPBAADVPN_BOT - Test</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83941" target="_blank">📅 23:24 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83939" target="_blank">📅 22:53 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83938" target="_blank">📅 22:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ر.پ برای سخنرانی در نشست سالانه کنکوردیا و دیدار خصوصی با نمایندگان دیپلماتیک کشورهای حاضر در مجمع عمومی سازمان ملل متحد، وارد نیویورک شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/83937" target="_blank">📅 21:15 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
