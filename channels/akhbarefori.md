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
<img src="https://cdn4.telesco.pe/file/pXIkCSCivbrlut1VqJMNmvewP4iqpZNi3Fs0jd8Tn6N6e6LYD9J0ZnMkjOZ8O1mSGB1-wxx3z078K1oWKuo25hfW1cDoKmBdO8zJ172NmaukyW1ONz8eorqTK_oiZ94xQ5UPhctizKzlvG4FSldWlbsrrUoz2iUrHjjgFS5Ad7oXl9uo2jUaoTRKf9TAQ7SZFpMf4C-9TNJE6WmFvTSLe5sYHv4jZGQg3QkgZeZgIq0zxndNRYett4NRFONJqoceov0Y4UWVK-j3oiTGtHJE__aW3_VR7AylaJq07j4hI3qw8xmKwqntQZm5QvlPQ6Jd6diJiAEHjD4Vy0cxuLXR_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 16:29:26</div>
<hr>

<div class="tg-post" id="msg-687661">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126464f667.mp4?token=Nd6t5jy0BrLliHyOMutPLEziQU7gqF9RcemDfgQwI3b3p5mUWSX8eSc5Ypvilimfu8yTlcogW5eZUoK1xhBApulxR3LYmH9MwJ_T6oBwO5-W1ZYSBURuCKRWWWwfW7botiHTC7hygfypsrAsv7gjKWhnOxIvvuAri-MiEM7m0xKFbSYNVm-vhc9eJTCeUPpLIX3_PTt96U8is4xvMLWTpyNJ3MdiHUu1Vm-LQUvrbl7qgxJJZ9PWsYfmBX_A6L2qoqUO0TShnTiMOnIA5bo6ZmHuoT3Aje4mKIZe-GozO9ql5t0PrFxSEtSyavr5NBABxC3mUVHgvwbCzsbuaszq0JEh8XdG2WyztyzwO3ZJIUN1Xd6ueZmEk2ZGVKM828wRhnzhRDkx8eeXpB1uU-8TgtdehBce--7vl1ErUoaEvoMNJHPI5Tz2G6xQlxCpoAzNDLqDy4i_mEcKM4R_p1hE0-W-TwGMv3x3CcXPwHCS3M4Fw9pheci33xLUjiu31M1bTCgAIxlsxqwJZZU9zAtb30iuYPBFylHUw1n0BAOmFgpoerCrsuGcKItmZJcMZXlZ8mbkXMNkYMIO6hMyvfT53QFszxhG0CSJg7aJRCi7KroMtUbDciYE_xEgoOQpvWQ94AWEhS5ETfj4k2-39Hf64eZ0u2Yfi8Rlgk9YPlqrIx8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126464f667.mp4?token=Nd6t5jy0BrLliHyOMutPLEziQU7gqF9RcemDfgQwI3b3p5mUWSX8eSc5Ypvilimfu8yTlcogW5eZUoK1xhBApulxR3LYmH9MwJ_T6oBwO5-W1ZYSBURuCKRWWWwfW7botiHTC7hygfypsrAsv7gjKWhnOxIvvuAri-MiEM7m0xKFbSYNVm-vhc9eJTCeUPpLIX3_PTt96U8is4xvMLWTpyNJ3MdiHUu1Vm-LQUvrbl7qgxJJZ9PWsYfmBX_A6L2qoqUO0TShnTiMOnIA5bo6ZmHuoT3Aje4mKIZe-GozO9ql5t0PrFxSEtSyavr5NBABxC3mUVHgvwbCzsbuaszq0JEh8XdG2WyztyzwO3ZJIUN1Xd6ueZmEk2ZGVKM828wRhnzhRDkx8eeXpB1uU-8TgtdehBce--7vl1ErUoaEvoMNJHPI5Tz2G6xQlxCpoAzNDLqDy4i_mEcKM4R_p1hE0-W-TwGMv3x3CcXPwHCS3M4Fw9pheci33xLUjiu31M1bTCgAIxlsxqwJZZU9zAtb30iuYPBFylHUw1n0BAOmFgpoerCrsuGcKItmZJcMZXlZ8mbkXMNkYMIO6hMyvfT53QFszxhG0CSJg7aJRCi7KroMtUbDciYE_xEgoOQpvWQ94AWEhS5ETfj4k2-39Hf64eZ0u2Yfi8Rlgk9YPlqrIx8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کار دولت شهید رییسی: وقتی گفتند بالگرد شهید رییسی فرود اضطراری کرد و نمی‌دانند کجاست، من مطمئن شدم که ایشان شهید شده‌اند/ با گذر زمان اگر زوایای پنهانی در خصوص سقوط بالگرد وجود داشته باشد، آشکار می‌شوند
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبرفوری :
🔹
آقای مخبر گفتند خبر رسیده که هلیکوپتر شهید رییسی فرود اضطراری کرد و نمی‌دانند کجاست، من همانجا مطمئن شدم که ایشان شهید شدند.
🔹
با مدیر کل اطلاعات استان آذربایجان غربی تماس گرفتم و ایشان گفتند دوباره با آقای آل هاشم تماس گرفتم و جواب داد و قطع شد.
🔹
ستاد کل نیروهای مسلح گفتند، دلیل خاصی را پیدا نکردیم و ما هم پذیرفتیم، با گذر زمان اگر زوایای پنهانی داشته باشد، آشکار می شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/687661" target="_blank">📅 16:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d90fdacc5f.mp4?token=G8ubNawdStymTXCTkILTu40JREWuRuzAjGxykgcYxs3hq0oCWeEGKJfy0rX8hp2lH8W7acPXRSVzIW4By0y01cpDHuDiwQ3WYELPJuc8NbNKK7pEzCiLImDDG6ouLMquiS8_Csb4SrNfKeaCaACDZmhLUPwrhkUNJgUBTgkaK_fvbsSQQbKRV5DZc2OyuqYQO8uxrqPkABSVVM2a5zkChNunm0M8Pba4cNQ4TXbuGmvxzyqR_1XMYKlnLzdGC50FA6U4sQE1-NkzHZmckp5n4BEc198SxivnSdBCJONTQRw9zIN3bXwiqePGuEiqNJDuMivzM8UK_fJ3Uqd-B-vvTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d90fdacc5f.mp4?token=G8ubNawdStymTXCTkILTu40JREWuRuzAjGxykgcYxs3hq0oCWeEGKJfy0rX8hp2lH8W7acPXRSVzIW4By0y01cpDHuDiwQ3WYELPJuc8NbNKK7pEzCiLImDDG6ouLMquiS8_Csb4SrNfKeaCaACDZmhLUPwrhkUNJgUBTgkaK_fvbsSQQbKRV5DZc2OyuqYQO8uxrqPkABSVVM2a5zkChNunm0M8Pba4cNQ4TXbuGmvxzyqR_1XMYKlnLzdGC50FA6U4sQE1-NkzHZmckp5n4BEc198SxivnSdBCJONTQRw9zIN3bXwiqePGuEiqNJDuMivzM8UK_fJ3Uqd-B-vvTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گودرزی رئیس اتحادیه مشاوران املاک تهران: میانگین قیمت مسکن از ۱۰۰ میلیون تومان عبور کرده است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/687660" target="_blank">📅 16:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8127b1da2d.mp4?token=gfsd6D0XJgZh7iVvJLcCtYOFeAB9_zF0ByNz_9AI1WOWmTbVAHqJqD7sOHcgVLSxKEnxVp-2_soK6u92bm-e04KUIvDeGtVWdqW9Zijrm5_A-VmKEWsFnQMKIQp2xJSqvZEwAaam4I80SKeMGIEKgJ-0LYe-C_V8GIQ8FfMw6THnvn4ToVrSgTiNj_XA25gGqadxQhqfo1oLx-70LuBuIgMYwaJ1HKLr_7xTrHXlqCKHtZeOUAtA5WlSb-1zmxpf7w2HQTzq0Jk13ixKncyC61oGtG5b3sHviC0LHa4xD6ZQvrY6bVQE0ab-tBYBXCRQxD9fRUf7fWJ0L6FagUCAgnPdiLh3hYOyxmoa312gwkm7R0tYSSsQv0EhPtXkP8wfTr50-wyrSniI1c5v5XRa3kn7CSfanwe0n_1jzGnyjL6bbwv4pausCVOOTqeyhsF6fsyJFrend7UVHOkDY8Tgwd1SPir1M77qn-o5NV_YLb8NOaPf9l36QRePN4A4Ee0vInbzzjYtH2V8PtR4RHg7MDWnbzQE0DW_08X_tHo-idZ9GmAdS7EAgR5kp8uFWDUC7ohtgEU-9-4R6mvcflo1OcbFLLi2OQg1rOvbya5Krf6aLYwGiu79M7pUJg_8fTeocMhO3Bn2xuPinUQ_y6iydEMhIDJVfled57CBCkXasD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8127b1da2d.mp4?token=gfsd6D0XJgZh7iVvJLcCtYOFeAB9_zF0ByNz_9AI1WOWmTbVAHqJqD7sOHcgVLSxKEnxVp-2_soK6u92bm-e04KUIvDeGtVWdqW9Zijrm5_A-VmKEWsFnQMKIQp2xJSqvZEwAaam4I80SKeMGIEKgJ-0LYe-C_V8GIQ8FfMw6THnvn4ToVrSgTiNj_XA25gGqadxQhqfo1oLx-70LuBuIgMYwaJ1HKLr_7xTrHXlqCKHtZeOUAtA5WlSb-1zmxpf7w2HQTzq0Jk13ixKncyC61oGtG5b3sHviC0LHa4xD6ZQvrY6bVQE0ab-tBYBXCRQxD9fRUf7fWJ0L6FagUCAgnPdiLh3hYOyxmoa312gwkm7R0tYSSsQv0EhPtXkP8wfTr50-wyrSniI1c5v5XRa3kn7CSfanwe0n_1jzGnyjL6bbwv4pausCVOOTqeyhsF6fsyJFrend7UVHOkDY8Tgwd1SPir1M77qn-o5NV_YLb8NOaPf9l36QRePN4A4Ee0vInbzzjYtH2V8PtR4RHg7MDWnbzQE0DW_08X_tHo-idZ9GmAdS7EAgR5kp8uFWDUC7ohtgEU-9-4R6mvcflo1OcbFLLi2OQg1rOvbya5Krf6aLYwGiu79M7pUJg_8fTeocMhO3Bn2xuPinUQ_y6iydEMhIDJVfled57CBCkXasD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش عبدالله ویسی به خداداد عزیزی: واقعا خجالت می‌کشم در این مورد صحبت کنم/ تویی که فحش می‌دهی! شما خودت ناموس داری
🇮🇷
✊
@
AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/akhbarefori/687659" target="_blank">📅 16:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687657">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4102d349a.mp4?token=LlogjiVs4agwTOvFS24CrnF2hluHsBoBQvbnJxL6SqAOv6qo4aafK898VF8EkahVLId-llR27lmvdoOnI6PECGEXG67O7wV3iUk5Be38edQdjSd_BdH6mTO1fU8ORWx__WQtmzaJeZZ8qRXr9VvrdPcI_qtwzLLrR3IvrltD-m6JV3ua6rYDl3RIRRqhAYNE4jkobSgJg_cAPNpjWfnwD4C75Dx3tdXulwrJz9P7-rbKWWHQZSnbsoXURyyJLHO4GfWMMQb-IW_u9zxK3n0ZfcuQWxgm1IzXeQsOU_92bEEaDCndqiUstYva47nKw0G1cMT5Gk_R1HQtE4LQjgK6zqKDqp_7-OUo3WbcgD4w3zeL3rU-CkV6OrqbNGjszUcBx0DqSaoA8nSwQfwgcFHvEO7tGJK306Z4md0LRRFdXfx6-LnsWsLI7ipmGZOwCgZ_Qxk3Ssnpeej67v-AMeMKtp_SJSEboApKv_t-HzGE5ZEpEyZBjOd7ZHwRy5fTIm287OP5yd_jU1_ewb_BRIP0OkITZb6bYt38FWmVwjXSK1ryMyMe9TYMwewDeXBfSR4uAwkihZCRQkTin8303SBfoGECJY5V2yosgHezZPDmPXo2EM3K1qQoW1JFiKiCX7LHmWPR6F5V-psFjXwsqKIkw3NL9qbj-YxR_B8D_4Sqdqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4102d349a.mp4?token=LlogjiVs4agwTOvFS24CrnF2hluHsBoBQvbnJxL6SqAOv6qo4aafK898VF8EkahVLId-llR27lmvdoOnI6PECGEXG67O7wV3iUk5Be38edQdjSd_BdH6mTO1fU8ORWx__WQtmzaJeZZ8qRXr9VvrdPcI_qtwzLLrR3IvrltD-m6JV3ua6rYDl3RIRRqhAYNE4jkobSgJg_cAPNpjWfnwD4C75Dx3tdXulwrJz9P7-rbKWWHQZSnbsoXURyyJLHO4GfWMMQb-IW_u9zxK3n0ZfcuQWxgm1IzXeQsOU_92bEEaDCndqiUstYva47nKw0G1cMT5Gk_R1HQtE4LQjgK6zqKDqp_7-OUo3WbcgD4w3zeL3rU-CkV6OrqbNGjszUcBx0DqSaoA8nSwQfwgcFHvEO7tGJK306Z4md0LRRFdXfx6-LnsWsLI7ipmGZOwCgZ_Qxk3Ssnpeej67v-AMeMKtp_SJSEboApKv_t-HzGE5ZEpEyZBjOd7ZHwRy5fTIm287OP5yd_jU1_ewb_BRIP0OkITZb6bYt38FWmVwjXSK1ryMyMe9TYMwewDeXBfSR4uAwkihZCRQkTin8303SBfoGECJY5V2yosgHezZPDmPXo2EM3K1qQoW1JFiKiCX7LHmWPR6F5V-psFjXwsqKIkw3NL9qbj-YxR_B8D_4Sqdqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش داریوش ارجمند به شایعه درگذشت خودش/ تا خداوند نخواد و زمانش نرسه اتفاق نمی‌افتد
🇮🇷
✊
@
AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/687657" target="_blank">📅 16:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687656">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdNuWgcUojWk5e-f3eEJ39DlbwsOCGX7SI0BwmKoNqHRW0aOHk-mZZzaA4SVBdnzhA5eB14I_haUno-a9J43SEcFhp46N0XvjrWz12h_4Z178fc5R1QozLBxVr7lx4_UWk6A_gIZ1z1Au2ZAm8UdRZmyvounP5ia1Pa6oeltI3_RGNeMQxK_qVMQzNqvs8nx9XrWy0D0C3biZr4rDEn1eZs-4S-uvTs_NBTHwn4lsi4ul-sWU2t8VOUc02-CNPHr0b7PpbzwZj-dWk7cachSq3xjkNKgThjmQO6BK_SVcVYGArndfSLMR5S7iE_5nUjyXBD8T6o0SPFLEjB0_r_kPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ از رنگ موی جدید خود رونمایی کرد
🔹
حالت جدید موی ترامپ تروریست مجددا سوال‌هایی درباره مصنوعی بودن آن ایجاد کرده است.
#Devil
📲
🇮🇷
✊
@AkhbareFor
i
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/687656" target="_blank">📅 15:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02757fb391.mp4?token=nqrDvK7JyyrkRXf3WPiV-uFvDTtPsMHyzFlwm1b0pxYHoMrj1QMRVRCgO_MEXD_qo71TXHZ-JqO-NID-3FPiwm2zmrpzWHdP0K5q0Q6cj5dVHQ0B5DUfeTiQcNZirX1YRVYNroU_0zBtW6on0ICq6bngtZirrMlj7dj4t9GBioqhfk39KblBkL9pU4IZ-IMJqsh0u803TAkj_c-yNBYIcI7tv-SIjhYskmiyqdsiM0OEIvFrfMX8EHEZng_gMz_4mC3-0GlrtvqZfhjmJsnc3wREtAAZUVZ6VwS5yC62QU-pBajHajhD_PmpUVNWMsrHw26Xy-VSgdjruy-H_ZhVug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02757fb391.mp4?token=nqrDvK7JyyrkRXf3WPiV-uFvDTtPsMHyzFlwm1b0pxYHoMrj1QMRVRCgO_MEXD_qo71TXHZ-JqO-NID-3FPiwm2zmrpzWHdP0K5q0Q6cj5dVHQ0B5DUfeTiQcNZirX1YRVYNroU_0zBtW6on0ICq6bngtZirrMlj7dj4t9GBioqhfk39KblBkL9pU4IZ-IMJqsh0u803TAkj_c-yNBYIcI7tv-SIjhYskmiyqdsiM0OEIvFrfMX8EHEZng_gMz_4mC3-0GlrtvqZfhjmJsnc3wREtAAZUVZ6VwS5yC62QU-pBajHajhD_PmpUVNWMsrHw26Xy-VSgdjruy-H_ZhVug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم‌های وایرال شده از ایونتی در تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/687654" target="_blank">📅 15:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قیمت کاغذ ۱۵۰ تا ۲۰۰ درصد افزایش یافت
حمید نیکدل، رئیس اتحادیه فروشندگان کاغذ و مقوای تهران در
#گفتگو
با خبرفوری:
🔹
قیمت کاغذ نسبت به سال گذشته بین ۱۵۰ تا ۲۰۰ درصد افزایش یافته است.
🔹
با توجه به اینکه حدود ۸۰ درصد کاغذ مورد نیاز کشور وارداتی است، عدم تخصیص ارز باعث شده تجار با مشکل مواجه شوند.
🔹
در حال حاضر موجودی انبارها مناسب است اما با توجه به اینکه بار جدید وارد نمی‌شود، ممکن است طی دو تا سه ماه آینده با مشکل شدید مواجه شویم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/687653" target="_blank">📅 15:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ستاد فرماندهی مرکزی تروریستی ایالات متحده: از زمان از سرگیری محاصره دریایی ایران، ۹۲ کشتی تجاری را منحرف، ۳ کشتی را از کار انداخته و ۲ کشتی را بازرسی کرده‌ایم./ الجزیره
📲
🇮🇷
✊
@AkhbareFor
i
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/687652" target="_blank">📅 15:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5a9bcbefe.mp4?token=UAVU_q62ULfSGh43cAlnnaaMTZNVwVlePwYbFJhzHaoLbQXQB82aNrph0TNt2Y6aFnwVvqhhrhq9TdJpIFOdshdTYL4uHWCBQuyZI_4aTlmH1a1j0gu9rQFcsWPCDYQj2ifs2kdzXYM4qktIYEP1v_EvUUDCqx61ctZik9nYB74zBTrh16XdQUmoglegNE5kO-x_FFHPPEoutd8LmlWsq04I7uUzviXcDIiBwUqGqWaw5TAhNg8q2tzd3ktWutmIU-WhAmG4dBF5mhCI34Wt6yg3_82bBMJl-kGETsRyRF57qYWvBwFxB1HnsuZcEKvx3P0oIR0TwgjcUX1gxf3_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5a9bcbefe.mp4?token=UAVU_q62ULfSGh43cAlnnaaMTZNVwVlePwYbFJhzHaoLbQXQB82aNrph0TNt2Y6aFnwVvqhhrhq9TdJpIFOdshdTYL4uHWCBQuyZI_4aTlmH1a1j0gu9rQFcsWPCDYQj2ifs2kdzXYM4qktIYEP1v_EvUUDCqx61ctZik9nYB74zBTrh16XdQUmoglegNE5kO-x_FFHPPEoutd8LmlWsq04I7uUzviXcDIiBwUqGqWaw5TAhNg8q2tzd3ktWutmIU-WhAmG4dBF5mhCI34Wt6yg3_82bBMJl-kGETsRyRF57qYWvBwFxB1HnsuZcEKvx3P0oIR0TwgjcUX1gxf3_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرب شست سپاه به ناو هواپیمابر و ناوشکن آمریکایی
🔹
روایت محمدسالار پایداری از حوادث شب گذشته در تنگه هرمز
🇮🇷
✊
@AkhbareFor
i
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/687651" target="_blank">📅 15:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTfTcW2QTpV7v8mpo8WCkR24W_L7yxvA2vF8v-xKqeWbxAUKbrYyXfmzkofDhj5Knc01GRpJkgu6BdHaoNNjFY1pmmxfJuHlKsbXIwX3nX98h_vy0oUAhq3CXDsXoTeMHWPMoomvOEsoMuQyA7uSUzQb6n2iQRj0piLnkyqrfc_gDL7kEhw4t5l4p2vzSWUSy3j7yn1X60Qk0eHRerdD_dxkuQQpM2BndG1aIX6L5MXUqDgV3V1zhiH1szafIbUKwv5ClRulV-eBJiYKdo-11f3H9zn7t8HroymrHpJC8g3NChnJ7wpW-gi9ItYnb9CAsLJbGmqyHz8qhEfG2ziorg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سارا خلیفه مجری مشهور تلویزیون مصر به اتهام قاچاق مواد مخدر به اعدام محکوم شد
🔹
این مجری معروف مصری ۳۹ ساله، تأمین مالی یک شبکه ۲۸ نفره رو برعهده داشته که آزمایشگاه‌های تولید مواد مخدر در قاهره راه انداخته بودن و بیش از ۷۵۰ کیلو مواد مخدر و مواد اولیه وارداتی و همچنین مهمات و تسلیحات از این شبکه کشف و ضبط شده.
📲
🇮🇷
✊
@AkhbareFor
i
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/687650" target="_blank">📅 15:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
حملۀ هوایی صهیونیست‌ها به علی‌الطاهر با وجود ادعای تسلط بر آن  الجزیره:
🔹
جنگنده‌های رژیم صهیونیستی شهرک المنصوری و ارتفاعات منطقه علی‌الطاهر در جنوب لبنان را بمباران کردند. بمباران ارتفاعات علی الطاهر در حالی است که رژیم صهیونیستی روز پنجشنبه گذشته مدعی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/687649" target="_blank">📅 15:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687648">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11720895cf.mp4?token=Cu_zdIcaGF6MXp4pxhm0LpcXCWZyX0HpGqaezA7GCbZidtNAhm6FRDmP37an7es99X4Ic4xTSo6y96ienk5XhCylKAdax24sREeQwbKUcIXU_GlTicNKGpsTpDz-wsZfwjk9fpwI4utR4D9WtNIkyAiuN7yBpOLARPjwqbaqfQlHp8n8zSYG6upKBR4_sCZv80MwpUBbC1AbHAXv1DPRjMjQ4kz-Y5Lbh5wlffGY6GlK1uJIIsl2G3qNrRtRQdL7NOHFh832T0mOcUS5gED5R2O-l3-MXtKD8YtmgTQgiNigEcT7PjjLVR9rRzKAz1gCKRSlc8j3iqRSA2ID17j_Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11720895cf.mp4?token=Cu_zdIcaGF6MXp4pxhm0LpcXCWZyX0HpGqaezA7GCbZidtNAhm6FRDmP37an7es99X4Ic4xTSo6y96ienk5XhCylKAdax24sREeQwbKUcIXU_GlTicNKGpsTpDz-wsZfwjk9fpwI4utR4D9WtNIkyAiuN7yBpOLARPjwqbaqfQlHp8n8zSYG6upKBR4_sCZv80MwpUBbC1AbHAXv1DPRjMjQ4kz-Y5Lbh5wlffGY6GlK1uJIIsl2G3qNrRtRQdL7NOHFh832T0mOcUS5gED5R2O-l3-MXtKD8YtmgTQgiNigEcT7PjjLVR9rRzKAz1gCKRSlc8j3iqRSA2ID17j_Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی وایرال شده از انتخابات دانش‌آموزی در آمریکا؛ دانش‌آموز پایه هفتم با تقلید از ترامپ، وعده‌ووعید می‌دهد تا رأی همکلاسی‌هایش را بگیرد
📲
🇮🇷
✊
@AkhbareFor
i
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/687648" target="_blank">📅 15:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687647">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJYpyPoQ1Hmgf8gYSdd36tFFpPWDKBxKLdc5N5y2OeCW-K-zdS3LSCQf3_GGH1vitirEvnAhEer0KaCnRid3ZX188glv-IgPaQ-awmc8cR52b_6MJVooQtu9lCTNYYYin0xTAOWIHaoJjkdjLvsJnhQNClrJ5mZ44ypVCDYzkAv3tlEv_JS6hk90ZRWtv-eMvSGKNWGEXDthq_Sox_wnjZpmkXlylYIpxaYelhRnwa0oed55iugrWM2VjQ8PW-r-NkLdX5b4Nl2CaQ7yClU62wMtou914gza2B7g9AOgdj3OOVXc6dNov3ehXwcQu8cB5YG7gJVvh5gfEDnlU4Ta6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت خطاب به مدیرعامل بانک اقتصادنوین:
🔸
اقدام مسئولانه شما در حمایت از تامین دارو، شایسته سپاس است
🔹
وزیر بهداشت، درمان و آموزش پزشکی اقدام مسئولانه بانک اقتصادنوین در حمایت از تامین داروهای مورد نیاز کشور و تقویت توان مالی شرکت‌های دارویی را شایسته سپاس و تقدیر خواند.
🔻
اطلاعات بیشتر:
https://enbank.ir/s/mfa9ZF
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/687647" target="_blank">📅 15:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VT30utj4z-5PLhW-Ltl6WRJZ7VJkDySvoOsdZngXFwyxCG4mqQgxiJq1qzR-FqO5_K3EkhPooa6YHeppSoWp2jBnE0WkCRyYLcWBLXPEWgj2KZGDgsyZjeEbAyYqac_fmr_ly2Q6xSPZ-0FiUk_WKUxF0NuYnX8hobDLB75nUcC-WkY5zuMXMngi_e10aQrR0xZ8qFWtlnqpKCZw8duLqNxoj0SBIGkHJXcv9gB_XbexdClG_DRt-szirBnZkEaW4Kmt4plj9jBzeVTWrXH68qZETFFTxxwkBV4WFEEJeYn8XG1smakXgNSBMn8XZxBld4SRVN0sRv8hz9CtAVEA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منچ‌اوسینت: از صبح امروز دست‌کم ۳ نفتکش هنگام تردد در «مسیر عمانی» تنگه هرمز، پس از هشدار نیروی دریایی سپاه درباره بسته بودن این مسیر، تغییر مسیر داده و برگشته‌اند
🔹
این شناورها شامل VELOS AMBER، BRAVO و AL SHEEHANIYA هستند.
🇮🇷
✊
@AkhbareFor
i
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/687645" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea69493b85.mp4?token=qadJcj_wF1jClKxBLLxmQB9oPPfj6SfVqn-agAVcQCqeAhJnL5PyziXzH8gsK0loxX4fr5SlQ1DuK3wKuxgVZH9Nl1OlwvIopcqBYA7o1XwpXSaZubVx_7cdbrqRWsAwbfzTb8FxC2UiOmHzg0aNm3ALrxqzApEvZ64az9N8Yp99zT7I3MSrSX2G_TTZXYo2iP-7JipcuDyRg7lLh2cAcDtN7w574HC9SaD4wi8l746ioRMMFy2GTlx9SduvZSgcoSQ5asRKB7OMLL44cmpUbZHmjZu1qfWcLak4aZI0ImF230jDcLBSR9bj7yWBd4b07R1M5t6U5lmnYAcDOt4EVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea69493b85.mp4?token=qadJcj_wF1jClKxBLLxmQB9oPPfj6SfVqn-agAVcQCqeAhJnL5PyziXzH8gsK0loxX4fr5SlQ1DuK3wKuxgVZH9Nl1OlwvIopcqBYA7o1XwpXSaZubVx_7cdbrqRWsAwbfzTb8FxC2UiOmHzg0aNm3ALrxqzApEvZ64az9N8Yp99zT7I3MSrSX2G_TTZXYo2iP-7JipcuDyRg7lLh2cAcDtN7w574HC9SaD4wi8l746ioRMMFy2GTlx9SduvZSgcoSQ5asRKB7OMLL44cmpUbZHmjZu1qfWcLak4aZI0ImF230jDcLBSR9bj7yWBd4b07R1M5t6U5lmnYAcDOt4EVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدام شغل‌ها در عصر هوش مصنوعی دوام بیشتری خواهند آورد؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/687644" target="_blank">📅 14:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dab340d8a.mp4?token=hxpw0jIptkfRkAz-KTLu1AIU8EfkhqSNfmXmcFjAUxu23qEdXSG9poaqSDEUCw4xpXo0YGKT1DwuZZENaphxJkJQvEsT_rupdMMUqZzgpLsbj1SF3QqU0-FD_Tip2JOze95M1iGwIbGhVeFAKsF_ivO6KH1XksDH-4qT1bF81tJj4aAMgQkuxjSGcFXSBrKw-OTehmT1LMmD8lYXqW7UAN1QYuACYAkr8ziP8j-8PI4WRlBi6zuwreEUsN_F8odNLNPdzX3zeC7CLZY9mroRzt9RuFU6lSyktdpZeGsD_E3tMqZz_uZxuMZPyBqM_6jt6LfREpjqH8XYc_LW4Gbr6n-x6LMbVgvjx6bI0juVWpX6PbejCIxFAmLp3oykesNVOZTyQVRrA1-GVVreWLhK0lyUUQmE2AEvZNZCq6STD20sCWX69wa9lSFXkM4vX2uIiZWJzgD9HXfsOk0mpWdRLfkG-xgxHd9JP8itMri3kZ3ZO3ylOuU_TGtLa85g8hgb3hguxY_bku_92BZU4ewg7YXao_jZ7sYFXca_Bq_7E-FcyAsK-0sCf-mm5r87f-vLblpB1CfhIVNQ18RuPGYR-4YNDgGyoZKVPHpcOeab3QZdWIua_Kq0G7lRzsAaMfwNlTQr_aHZpUgnyHUwOqueZxOIxsAcm-fd7rMVL4IJLMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dab340d8a.mp4?token=hxpw0jIptkfRkAz-KTLu1AIU8EfkhqSNfmXmcFjAUxu23qEdXSG9poaqSDEUCw4xpXo0YGKT1DwuZZENaphxJkJQvEsT_rupdMMUqZzgpLsbj1SF3QqU0-FD_Tip2JOze95M1iGwIbGhVeFAKsF_ivO6KH1XksDH-4qT1bF81tJj4aAMgQkuxjSGcFXSBrKw-OTehmT1LMmD8lYXqW7UAN1QYuACYAkr8ziP8j-8PI4WRlBi6zuwreEUsN_F8odNLNPdzX3zeC7CLZY9mroRzt9RuFU6lSyktdpZeGsD_E3tMqZz_uZxuMZPyBqM_6jt6LfREpjqH8XYc_LW4Gbr6n-x6LMbVgvjx6bI0juVWpX6PbejCIxFAmLp3oykesNVOZTyQVRrA1-GVVreWLhK0lyUUQmE2AEvZNZCq6STD20sCWX69wa9lSFXkM4vX2uIiZWJzgD9HXfsOk0mpWdRLfkG-xgxHd9JP8itMri3kZ3ZO3ylOuU_TGtLa85g8hgb3hguxY_bku_92BZU4ewg7YXao_jZ7sYFXca_Bq_7E-FcyAsK-0sCf-mm5r87f-vLblpB1CfhIVNQ18RuPGYR-4YNDgGyoZKVPHpcOeab3QZdWIua_Kq0G7lRzsAaMfwNlTQr_aHZpUgnyHUwOqueZxOIxsAcm-fd7rMVL4IJLMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزت الله ضرغامی: آیت‌الله جنتی به دلیل کهولت سن، امکان ملاقات و گفت‌وگو ندارد
🔹
آیت‌الله جنتی امسال وارد صدمین سال زندگی خود می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/687643" target="_blank">📅 14:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71ee84a1a.mp4?token=JejnqPopwNOStRH7xnK2IuCwLXGCandwG2fnHbQEL0ZpYezRK6ZrOZNGfo641pxK33CILe2PAb9yQsgiFPKwMECHyTDMWzwC4g5aWa1fUYGbcBk9VbW8Oz8XB8xscXJO89aGRe5MupdSju3QhSxaK01EwOcOHewSFn_nN5pfz6K777Vn2DwpbkxsGJd40nF0SnR5nFsJPWb8mhmlcgxVKiiWJ1XL2k8JBBlMrMhW0bAVyGOg-otSptbFzcIGikp1P339vVyHjbJLkw44H_77-r7rJcR5QRDStNR8BWCTQNxQ3YhJn-T09HsxmnhnKcIcSkFfepY8dFexONXFQeHgWypKnfSKFHSz5Y6mEiuyXUr2gHYNwZ5IENDciNzMqGWiAcjTIrkkrTARaEt7aIJHgu6nXkB1A6pHmS6Zj1gWuxTSTYCdD_250MRFvPXv8EL8nBj7bBgfyfO1HQCeGpdnJWjRMvWpPGrkS8jM2ipgpVAl6bqqRUhxYq6Beo621L7LLn3j0aclwdWzzVuTVBPEPWl9UisgDQ6Jrn7S5zm0oPlKXHNwOosg9mgSbz62i7-m7NBSuD3qW-6IItFxHp3kNQqLA4sSpm4t6vsIu7U3VvlEZuHnwMaW3U9QqzFWupjU9cBxhbWbZLDdhG3yDrw7DKQ_tV2lgJNXe87jP9XrvxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71ee84a1a.mp4?token=JejnqPopwNOStRH7xnK2IuCwLXGCandwG2fnHbQEL0ZpYezRK6ZrOZNGfo641pxK33CILe2PAb9yQsgiFPKwMECHyTDMWzwC4g5aWa1fUYGbcBk9VbW8Oz8XB8xscXJO89aGRe5MupdSju3QhSxaK01EwOcOHewSFn_nN5pfz6K777Vn2DwpbkxsGJd40nF0SnR5nFsJPWb8mhmlcgxVKiiWJ1XL2k8JBBlMrMhW0bAVyGOg-otSptbFzcIGikp1P339vVyHjbJLkw44H_77-r7rJcR5QRDStNR8BWCTQNxQ3YhJn-T09HsxmnhnKcIcSkFfepY8dFexONXFQeHgWypKnfSKFHSz5Y6mEiuyXUr2gHYNwZ5IENDciNzMqGWiAcjTIrkkrTARaEt7aIJHgu6nXkB1A6pHmS6Zj1gWuxTSTYCdD_250MRFvPXv8EL8nBj7bBgfyfO1HQCeGpdnJWjRMvWpPGrkS8jM2ipgpVAl6bqqRUhxYq6Beo621L7LLn3j0aclwdWzzVuTVBPEPWl9UisgDQ6Jrn7S5zm0oPlKXHNwOosg9mgSbz62i7-m7NBSuD3qW-6IItFxHp3kNQqLA4sSpm4t6vsIu7U3VvlEZuHnwMaW3U9QqzFWupjU9cBxhbWbZLDdhG3yDrw7DKQ_tV2lgJNXe87jP9XrvxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: من مدافع طرح مقابله با نفوذ هستم اما نمی‌شود کشور را قفل کنیم و بگوییم همه از ما اجازه بگیرند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/687642" target="_blank">📅 14:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687641">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ec73b8b7.mp4?token=rpPQVuOl1gofqHkpoV3-1BqDc5Uw6mSy43FcqTd4j4JdW4sws3GnI5LEV0uIYc-YyR8oIt1a-KdFoxhcAzU3wtZVjHvVzciS42Wgow5jbV2bJ7D0jdOgF0435PGQmB9dH5QGcPzqTwXYqZtcjkPg5EQEUCJY5KlnHIJCDNv5q2eYLerp5-qLWyQIwAEAELzPwfRyw0fnsELcSfF2wHdwr9QPKqV0WlqMlaXYosEKlgm9zxQUJ8cuCYNUDLWfnou0a0aTDE0nV7hL03TKGQLk5GSziHftEfSHoSkI5Sf8jZztkmfg2bjlACm_5pwc0OZ0elyEM7ChuWVHZ_wOq4aD4CpUQn0AeX0Mw_ss9BcAttVNQbf6k10anT7g4TuC2A2cq4vAOCay8dP_Tq5UjuElunly745yTmzl81P4Ba7T4oK41xhi3_ViIfod5LtdwuA_Bc-Sakd0iBSIIHu-QwKQxice5EZThIQSkQTjt0Lql9xsX7cS9btKE-Hm6Xh2PRilIHZJVqNHKcaUWfAkaDoJJHtXyukrtcWbsrOfWe0-6WR_KtnTxxqV-HSyRRpL6U6al0m_HNS7kPC8FPovI6II4ibIuH9l4WLtmuAh7DtlqCRXepODYGdCKfCugp6AsX6v93RBw_wMtanojXk_IRjaGtuancWcbZfJ6l2FKaxHn8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ec73b8b7.mp4?token=rpPQVuOl1gofqHkpoV3-1BqDc5Uw6mSy43FcqTd4j4JdW4sws3GnI5LEV0uIYc-YyR8oIt1a-KdFoxhcAzU3wtZVjHvVzciS42Wgow5jbV2bJ7D0jdOgF0435PGQmB9dH5QGcPzqTwXYqZtcjkPg5EQEUCJY5KlnHIJCDNv5q2eYLerp5-qLWyQIwAEAELzPwfRyw0fnsELcSfF2wHdwr9QPKqV0WlqMlaXYosEKlgm9zxQUJ8cuCYNUDLWfnou0a0aTDE0nV7hL03TKGQLk5GSziHftEfSHoSkI5Sf8jZztkmfg2bjlACm_5pwc0OZ0elyEM7ChuWVHZ_wOq4aD4CpUQn0AeX0Mw_ss9BcAttVNQbf6k10anT7g4TuC2A2cq4vAOCay8dP_Tq5UjuElunly745yTmzl81P4Ba7T4oK41xhi3_ViIfod5LtdwuA_Bc-Sakd0iBSIIHu-QwKQxice5EZThIQSkQTjt0Lql9xsX7cS9btKE-Hm6Xh2PRilIHZJVqNHKcaUWfAkaDoJJHtXyukrtcWbsrOfWe0-6WR_KtnTxxqV-HSyRRpL6U6al0m_HNS7kPC8FPovI6II4ibIuH9l4WLtmuAh7DtlqCRXepODYGdCKfCugp6AsX6v93RBw_wMtanojXk_IRjaGtuancWcbZfJ6l2FKaxHn8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صولت مرتضوی: پزشکیان، خاتمی، روحانی و احمدی‌نژاد به اندازه شهید رییسی سابقه کار اجرایی نداشتند/ شهید رییسی در همه حوزه‌ها سرآمد بود
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبرفوری:
🔹
آیت الله شهید رییسی عشق خدمتش سیری ناپذیر بود و میگفتند هرچه بیشتر کار میکنم، خستگی ناپذیرتر میشوم، رهبر شهید گفتند دلم برای شهید رییسی سوخت.
🔹
هیچ مدیری با سابقه اجرایی شهید رییسی، رییس جمهور نشده است؛ اجرایی‌ترین شخصیت در طول تاریخ بود.
🔹
سوابق اجرایی آقای خاتمی، روحانی و احمدی نژاد با سوابق اجرایی آقای رییسی قابل مقایسه بود؟
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/687641" target="_blank">📅 14:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3056374e.mp4?token=B9KwwgI8pAKDZP7GZZfFDob2HSNRuwx9BEwMWnNbF3NjdKIlYPdJleoH_w8V7s8Yv4P2jxxO9D2k9Kq2i7ktoiPA6ywqDywQXHjnRdfoc435UKvW6605M10BqcaImeNZLw8BeIJaAm-7bdi9YujkV3iOsHItMzUkWOgdGCiOoXjBPh58WzcG-yB9dHtPEwBW7YkwIGrCixjYUP1CBhnzSEDJMJvwmn1tZZd7Y0jmRXodn6SWcYtpJwI73erBbsmRz46N7uXR1cuQZUo83U_u6XKKKuSyiew0XRu8u-fQSIRx8QWGiY0NfCH4SN0D-hxAk6uoAJ12dc9hY3-1Lopepw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3056374e.mp4?token=B9KwwgI8pAKDZP7GZZfFDob2HSNRuwx9BEwMWnNbF3NjdKIlYPdJleoH_w8V7s8Yv4P2jxxO9D2k9Kq2i7ktoiPA6ywqDywQXHjnRdfoc435UKvW6605M10BqcaImeNZLw8BeIJaAm-7bdi9YujkV3iOsHItMzUkWOgdGCiOoXjBPh58WzcG-yB9dHtPEwBW7YkwIGrCixjYUP1CBhnzSEDJMJvwmn1tZZd7Y0jmRXodn6SWcYtpJwI73erBbsmRz46N7uXR1cuQZUo83U_u6XKKKuSyiew0XRu8u-fQSIRx8QWGiY0NfCH4SN0D-hxAk6uoAJ12dc9hY3-1Lopepw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرقت گوشی آیفون ۱۳ یک زن در تهران در کمتر از ۵ ثانیه
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/687640" target="_blank">📅 14:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f177f43c5.mp4?token=MeuXUFWoNK77_ZkeZ3CLdVKu6VwngbtZwXJcJxsYR5JSmY7FMsBY8pgyAc9ehr4_4bNWVjr458uo3pGamn_F1n1uzpqhSFbwdnGkeXP0zjVU7jfAVllIK0oxvy4rl8w6zbN5rGRSWbnxp2iL33ABc4BprS2Ns8pdFOghGoLfxRjCAICDS_0Mc-ZJn9wzq2OFMH7kBtlLI-PwLtxWjIOiSo6JAI7uRgqbhvzXhc4gT5BxtLdADCld126EkTfXLaENK7ZuG8aED8KFShKxGnb_JK7DNY7B3vJnlQCPqhZNm7_KPH1tqHAAreve4cIvAS5ggxkIkA2TgQYeecfKUO5YilfAHp2v81-ftyjDqmcwK9pT9_zaDYziLdA8YjsMlXXrmvjAqHDuWF7cNrN__GhZXuAJOEKPCS0kCysgCJ_h1UgnZQm1XbXBNeyS36kx9BLxRKTQCBXK5oaAS5XK1JAx4tlYKA7fmIzy1JG847OB5rh2NEm3QlEejG2PwJ-wYQ1tIQvXlMJhVdvJCUxU8Yz8SbOIPvTeDLO6t2LgZ0BBG4veGYfxplIvGw62U8_Gs3Pgly_hjfRPVFftVkpD_YwtWenMTqpa41NS9yCjiaaAcgGga1BOZuBRE4YrQYjF62kF9RFTJnKqsKT7SWUjpfGqfFD8iQfVHHRd4teLPk31obI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f177f43c5.mp4?token=MeuXUFWoNK77_ZkeZ3CLdVKu6VwngbtZwXJcJxsYR5JSmY7FMsBY8pgyAc9ehr4_4bNWVjr458uo3pGamn_F1n1uzpqhSFbwdnGkeXP0zjVU7jfAVllIK0oxvy4rl8w6zbN5rGRSWbnxp2iL33ABc4BprS2Ns8pdFOghGoLfxRjCAICDS_0Mc-ZJn9wzq2OFMH7kBtlLI-PwLtxWjIOiSo6JAI7uRgqbhvzXhc4gT5BxtLdADCld126EkTfXLaENK7ZuG8aED8KFShKxGnb_JK7DNY7B3vJnlQCPqhZNm7_KPH1tqHAAreve4cIvAS5ggxkIkA2TgQYeecfKUO5YilfAHp2v81-ftyjDqmcwK9pT9_zaDYziLdA8YjsMlXXrmvjAqHDuWF7cNrN__GhZXuAJOEKPCS0kCysgCJ_h1UgnZQm1XbXBNeyS36kx9BLxRKTQCBXK5oaAS5XK1JAx4tlYKA7fmIzy1JG847OB5rh2NEm3QlEejG2PwJ-wYQ1tIQvXlMJhVdvJCUxU8Yz8SbOIPvTeDLO6t2LgZ0BBG4veGYfxplIvGw62U8_Gs3Pgly_hjfRPVFftVkpD_YwtWenMTqpa41NS9yCjiaaAcgGga1BOZuBRE4YrQYjF62kF9RFTJnKqsKT7SWUjpfGqfFD8iQfVHHRd4teLPk31obI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکید رهبر انقلاب به پرهیز از ضعیف نمایی، دستورالعمل راهبردی برای تمام عرصه‌هاست   رئیس مجلس:
🔹
حفظ «انسجام درونی» و «قدرت بازدارندگی خارجی» دو ابزار مهم برای مقابله با دشمن است و هرگونه سخن یا عملی که به تضعیف این دو ستونِاساسی منجر شود،  نه تنها خلاف تدبیر…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/687638" target="_blank">📅 14:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daa9e39ed.mp4?token=hdGToIVFin469JDtvMhf7EeValM2Z_BJI4QaIWcTED2Yiiqaeesl94vBgRrLK5HX0hSPjTj8tJl2v_vRnH9YHNlTkGBAN_M_YpxVVC3uZnljkIO2nroM5chm9wgZXoghI5OWrHMNPQME76jgmDnJ8whk5W8xOiuxVka_0X_1_cNQNnFy1GTsibuLRW6ltJNNfsJZU5D7PhOKJ68sXJYUfFSB48CPRU4O1h_ozBLwkcGi542S518Bsr5aXeMJU_Q9AjrqZiI42Ai1IK9tn5oTaUVJvudj4mqMHuDOa0WmBtWNCMgqmW7aFhztTTCJRaoeY1IxZQ0baCImscXRvRKOjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daa9e39ed.mp4?token=hdGToIVFin469JDtvMhf7EeValM2Z_BJI4QaIWcTED2Yiiqaeesl94vBgRrLK5HX0hSPjTj8tJl2v_vRnH9YHNlTkGBAN_M_YpxVVC3uZnljkIO2nroM5chm9wgZXoghI5OWrHMNPQME76jgmDnJ8whk5W8xOiuxVka_0X_1_cNQNnFy1GTsibuLRW6ltJNNfsJZU5D7PhOKJ68sXJYUfFSB48CPRU4O1h_ozBLwkcGi542S518Bsr5aXeMJU_Q9AjrqZiI42Ai1IK9tn5oTaUVJvudj4mqMHuDOa0WmBtWNCMgqmW7aFhztTTCJRaoeY1IxZQ0baCImscXRvRKOjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط یک ربع زمان می‌خواد تا روسری بلااستفاده قدیمی تبدیل بشه به شومیز مهمونی #فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/687637" target="_blank">📅 14:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687636">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Rz9rweoiVHpjBY-0YjLMdzrWhl6dAJtWuqjqgv7Cz9GeiRGFiNrFvBN6fSaBjrR_CoFU4Yvp9KkG6TAzw7-c0cgCdGoxvZFJV0HigTSeOMXNkwyHxKOm_iKPeu-yFLXaQkDHsCutIAT-m9q4tyE41w7GRxos5nzrsuQRMzsVEjTwSQsOAHZmtkrsOjeMk0TtP7gEwD_dD4kIoK2ozCoxNTc0vpwFWNyvHTS3PztfUFkKYXMnfZ4IaS3djCiqptFlo1tuJtpt2Daj76_Ksiau8wr3pv4Z7h-0EIKUXhzGbzVxOqKYmDYUkcua0klPfJpYVjBmG8k8z03jQTbIyu6L9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبور چادرملو از برنامه تولید علیرغم جنگ تحمیلی و ناترازی انرژی
🔹
به گزارش خبرآنلاین، شرکت معدنی و صنعتی چادرملو تا پایان مرداد با تولید بیش از ۱۰.۲ میلیون تن محصول، موفق به تحقق ۷۰ درصد از برنامه تولید سال مالی جاری شد.
🔹
برنامه تولید کنسانتره آهن تر در سال مالی جاری ۸.۵ میلیون تن تعیین شده که با تولید بیش از ۶ میلیون تن تا پایان مرداد، بیش از ۷۱ درصد این برنامه محقق شده است.
🔹
همچنین از مجموع برنامه ۳.۷ میلیون تنی تولید گندله، بیش از ۲.۵ میلیون تن محصول در این مدت تولید شده که معادل ۶۸ درصد برنامه سالانه است.
🔹
در بخش تولید آهن اسفنجی نیز از برنامه ۱.۵۵ میلیون تنی سال مالی جاری، ۹۶۳.۵ هزار تن تولید شده و ۶۲ درصد برنامه محقق شده است.
🔹
برنامه تولید شمش فولاد در سال مالی ۱۴۰۵ نیز ۱.۰۵ میلیون تن تعیین شده که با تولید بیش از ۷۷۰ هزار تن شمش فولاد در هشت ماهه سال مالی، ۷۳ درصد آن محقق شده است.
🔹
این میزان تولید در حالی به ثبت رسیده که صنعت فولاد و معدن کشور طی ماه‌های اخیر با محدودیت‌های ناشی از ناترازی انرژی و پیامدهای جنگ تحمیلی رمضان و همچنین محدودیت‌های صادراتی مواجه بوده است.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/687636" target="_blank">📅 14:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687634">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d0721409.mp4?token=WdyiY0o6ojErPXeerbLhX8-md_wLONuGe_QctbrFOmJNxZOpGHNFQNV884QEptz1FVwgbmVIsZzEM9Nmy6ZjBeTb00Ng3LGDDLQMWN2XDyxhVmZrvE69waLPyp2JpGVgFiNdctvko3Ad1jzBGTYcyw-z6HSnEB3pe_Icr7xIMqjVoKwBqT5nKGpxmHk0WtvheQS2t07l001fR4SIzNo3vX0q6Vpr9vC4cE-PuGWuQZW8VXK1K4cpluuT1S9wyKe47-EYXA9qgiIQQfOYehMXvPbg1FeAeANRBJSNwOZrrXKTAZyfuLzZJQZTbO9oQFROEFfQd1VH5PG_hV310Qd0Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d0721409.mp4?token=WdyiY0o6ojErPXeerbLhX8-md_wLONuGe_QctbrFOmJNxZOpGHNFQNV884QEptz1FVwgbmVIsZzEM9Nmy6ZjBeTb00Ng3LGDDLQMWN2XDyxhVmZrvE69waLPyp2JpGVgFiNdctvko3Ad1jzBGTYcyw-z6HSnEB3pe_Icr7xIMqjVoKwBqT5nKGpxmHk0WtvheQS2t07l001fR4SIzNo3vX0q6Vpr9vC4cE-PuGWuQZW8VXK1K4cpluuT1S9wyKe47-EYXA9qgiIQQfOYehMXvPbg1FeAeANRBJSNwOZrrXKTAZyfuLzZJQZTbO9oQFROEFfQd1VH5PG_hV310Qd0Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر تو بودی جای خالی رو با چی پُر میکردی؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/687634" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687633">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XefOWVNzrSl-elSb-QmzPG_ebFMGPBd7qfakDxu2JzBRoA4MBw0MrhBCDsVCqlS6A5-eVDEn6PlVqNNjYMwFIlm89FYQxSfaeqPe-5wX9_E0udLxIChjbiTqUtkvJJpsm5h5kivgWDt_LczoyguHuNdl53Qmbdz0D6EsFhCPiR6jnMrRRRo8_ul1RGrjtoG9W3Jyyifrxf2F5SGk0SpKd9TH_akapfyiRVl21DOj89WvBC-mOBMocM7EfeMt9GD28UOnlx9gTVjo7O1J7n3xm4qer4vDBt5gYqNfRAvSXCM6aGvNwtOuv-45bt-m_ghRCC3_7Ki2AmQIYceZ3iyVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت پهپاد انتحاری شاهد به بالن جاسوسی آمریکا در اربیل عراق
🔹
این اصابت مربوط به شب‌های گذشته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/687633" target="_blank">📅 13:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687632">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d21ecf180.mp4?token=uPFMtlJMR_C3DbxKY2GxKpO-TkjVO6BIp_8fcXCeXq1MvcrV2NPxXFkZJO5NygpwfpirBpgd0bU-3e1PuBlBPv95_Q2LDCsgJo5CenktvdwuJqT6AHgle7U_r3vujwND3ZmGXJUQUzU2Hd9pjIhM_VtH3IWArbXq4UuAXnHr-UeOiWRfdFmfHW0-QEF_ePouXVM7G14oyvdXVO1CTxmUogNXp8l05ax0joSq055qGq_I0jfJwCyL5d7-ygbVedNuAUI_K63k0zLw_BhfEIm6Es4c4DMU7mecnEG_nAP5I-vwN-fIfpQeAjYOCjexE9NNzPnnGYlvM6hWiiEIxc__tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d21ecf180.mp4?token=uPFMtlJMR_C3DbxKY2GxKpO-TkjVO6BIp_8fcXCeXq1MvcrV2NPxXFkZJO5NygpwfpirBpgd0bU-3e1PuBlBPv95_Q2LDCsgJo5CenktvdwuJqT6AHgle7U_r3vujwND3ZmGXJUQUzU2Hd9pjIhM_VtH3IWArbXq4UuAXnHr-UeOiWRfdFmfHW0-QEF_ePouXVM7G14oyvdXVO1CTxmUogNXp8l05ax0joSq055qGq_I0jfJwCyL5d7-ygbVedNuAUI_K63k0zLw_BhfEIm6Es4c4DMU7mecnEG_nAP5I-vwN-fIfpQeAjYOCjexE9NNzPnnGYlvM6hWiiEIxc__tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: تلاش می‌کنیم قطعی برق متوقف شود
🔹
این درحالیست که وزیر نیرو روزهای اخیر مدعی شد قطعی برق متوقف شده اما همچنان خاموشی‌ برنامه ریزی شده پابرجاست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/687632" target="_blank">📅 13:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884a21e818.mp4?token=kKsjynO9DmhcF_US37ekU_ShfY9ZSfCqjYtcDlCl0mdaZr698mYaitIR1XfTNZBc9EEaylkjtVfC6fRJ71mtTxkSgKO0G4wFz3zmvrY2ew28pbg907fKyPR2fW-qNwTWNBx69Tx3NMR2nGEAmAeFHQZY2c2CCgpSklMngQJ0_Qc4kqHjTAxubIJRboCCdXFjKsyUXYOqsuHTVNM-2UZUo3yncstLvcxChofE8UHFpXh5pxc_m_x6I5h-yctVAZXiwig5rp_2uhMcpUkyHHo9rRQTVosKUo9uAs90WnmQoM06VxsTIRz9WL3CVtaiZkPBzlPCkl4lx_-u_nMXqZ5nvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884a21e818.mp4?token=kKsjynO9DmhcF_US37ekU_ShfY9ZSfCqjYtcDlCl0mdaZr698mYaitIR1XfTNZBc9EEaylkjtVfC6fRJ71mtTxkSgKO0G4wFz3zmvrY2ew28pbg907fKyPR2fW-qNwTWNBx69Tx3NMR2nGEAmAeFHQZY2c2CCgpSklMngQJ0_Qc4kqHjTAxubIJRboCCdXFjKsyUXYOqsuHTVNM-2UZUo3yncstLvcxChofE8UHFpXh5pxc_m_x6I5h-yctVAZXiwig5rp_2uhMcpUkyHHo9rRQTVosKUo9uAs90WnmQoM06VxsTIRz9WL3CVtaiZkPBzlPCkl4lx_-u_nMXqZ5nvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوضاع اشفته بازار موبایل
🔹
قیمت گوشی‌ها همچنان نوسان دارد و افزایش نرخ ارز، فشار بیشتری به بازار وارد کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/687630" target="_blank">📅 13:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMa6TNBujHTWr_9usuOlLc2nfg_KT-36JC8RIuIOJ8YZHhR2nNg73oP7sr8PtbqETLvfeeFlkyqNCXwHMg4nKvM5RfT8W3wpF8NpTLtPFvuTgvRVpTBWxMQjzCFDp8v3K_dByR0DeHZFBbo64LJfgfjIPnKRsxnGJrSsWBC9rt3lvcQY77-C2Ts_MffeXPyAjugLjpCejb4kVvwvA1Haicik9VLrm3C0x9E37arO9L6I_8rH6IKr4Qd5l9ugtWw2ZKQcCA4RPf3Jp-BvSPFvn42U90QD-jXw0dYcltoz1RFK1U32SOjqWS1w2_dfE4-v-_rYSsvx7jdwpoGljddoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرصت دوباره سرمایه‌گذاری در صندوق نقره یاس
🟢
از دوشنبه ۱۶ شهریور ماه صندوق نقره یاس بازگشایی می‌شود.
🟢
یاس در پذیره‌نویسی خود با استقبال قابل‌توجهی روبه‌رو شد؛ ۱,۰۰۰ میلیارد تومان در چند ثانیه به فروش رسید و حدود ۲,۶۰۰ میلیارد تومان سفارش خرید برای آن ثبت شد که با توجه به ظرفیت ۱۰۰۰ میلیارد تومانی، تعداد زیادی موفق به سرمایه‌گذاری نشدند.
🟢
اگر در پذیره‌نویسی موفق به خرید یاس نشدید یا به سرمایه‌گذاری در نقره علاقه‌مندید، از دوشنبه از ساعت ۱۲ می‌توانید با جست‌وجوی نماد «یاس» از طریق تمام کارگزاری‌ها، این صندوق را خریداری کنید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/687629" target="_blank">📅 13:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gs7B8n_6gBqWiUQnALT3GBF8XOnxYvajBvxGXYQGfEsLCJuxj6J_BBHJVCzfkGpQy8bVsjHBmMVv5id1tnJQ-8pfPd4weIdXmqGZN7Z1IpDnFH9wwkajxLhDiaG_bmF3Gq0kgPxlkrUmDBnqAA6DhMT7oFgh-x8s-Y0SQ-CUM_-7REXU_aYTaO4u3LcpNaPEh47_0dRwW6DZezZp-tDUSMfBNaE-q1p9ldUhVrp6xCQmVnGwSqVQCWEww_cNBDNIFTqz376cyglKhO90MwIdZG6ax-BnUzzjUbX9gCjwhUzip8mcTZMsvyj0vgZCuGMUclzVC2uAy3Wkg-Q88t77uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حدود نیمی از مصرف بنزین کشور با کارت سوخت جایگاه انجام می‌شود
🔹
بر اساس بررسی‌ها سهم استفاده از کارت سوخت شخصی از ۷۴ درصد در دی و بهمن سال گذشته، به ۶۰ درصد در مرداد و ۵۲ درصد در انتهای مرداد و اوایل شهریور رسیده است.
🔹
در مقابل، سهم کارت سوخت جایگاه از ۲۶ درصد به حدود ۴۸ درصد افزایش یافته؛ یعنی نزدیک به ۵۰ درصد بنزین مصرفی کشور بدون رصد دولت انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/687628" target="_blank">📅 13:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کنایه وزیر کار دولت شهید رییسی به حسن روحانی: قربان تیپ خوشگلت بروم برجام را توجیه می‌کنی ، مشکل واکسن کرونا چه بود که آن را وارد نکردی!
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبرفوری:
🔹
آقای روحانی می‌رفت و برجام را امضا می کرد ، چه کسی نگذاشت ؟ اینکه دولت ما چنین اجازه ای را نداد به ضرس قاطع تکذیب می‌کنم.
🔹
آقای روحانی قربان تیپ خوشگلت بروم، این برجام را توجیه می‌کنی، مشکل واکسن کرونا چه بود؟ آن را هم کسی به شما گفت وارد نکن و مردم را درمان نکن؟
🔹
مصاحبه های آقای روحانی را ببینید که میگفتند ما امکان انتقال پول نداریم و پول نداریم ، دنیا به ما واکسن نمی‌دهد. ایشان فکر میکند حافظه تاریخی ملت ایران ضعیف است.
🔹
شاید بشود بگوییم آقای روحانی تفکرش این بود که چون این دیگ برای من نمیجوشد در آن هیچ چیز نجوشد.
🔹
حرف بدون پشتوانه زدن راحت است و متاسفانه در کشور ما کسانی که حرف بدون پشتوانه میزنند، مورد مواخذه قرار نمیگیرند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/687627" target="_blank">📅 13:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_lh8sIgR4tFDG4laCZK1x7E5D-HFMmYtM2FEQNy09zoBdQ1Zg-kZOJ2w-Ic3vTTP47ALtVVFBa1kjneRxUqtpliaTqr-HwxcHy59byE2Sy59VJyFR7p60WU2YQJvSDNhSE4wHO5TqaBLGzUq2BDkyVcIMWQe2UTjHcceHyKgGGgGdLT264faXYl6O6jUDIXpAv0fKfZ_cXbAgjERB42TXNY4-WrLrCSL_VQKkT5XBroOS3gkyXnQz9-uBuZZewrKCYOV8KSXoEr-Yv7S-VXCsXLa49_1KYmlAJgiLC9Lw3RoxCnHeHrSI3jA7YwO_KL73I2wCw88fEsiEy5r0C6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش ۱۷ درصدی تردد مسافران در مسیرهای هوایی و دریایی کیش
🔹
تردد مسافران در مسیرهای هوایی و دریایی کیش طی هفته گذشته با افزایش ۱۷ درصدی نسبت به هفته ماقبل همراه شد و در مجموع ۲۲ هزار و ۱۸۴ مسافر از طریق فرودگاه بین‌المللی و بندرگاه این جزیره جابه‌جا شدند.
🔹
بر اساس آمار اعلام‌ شده، فرودگاه بین‌المللی کیش طی این مدت با ثبت ۱۲۲ پرواز ورودی و خروجی، پذیرای ۱۲ هزار و ۸۱۰ مسافر بود. همچنین بندر تجاری کیش نیز به ۹ هزار و ۳۷۴ مسافر خدمات‌رسانی کرد.
🔹
در بخش حمل‌ونقل دریایی، طی هفته گذشته یک‌هزار و ۸۱۲ دستگاه خودرو نیز از مسیرهای دریایی کیش تردد کردند؛ آماری که در کنار رشد جابه‌جایی مسافران، بیانگر افزایش تردد در مسیرهای ورودی و خروجی این جزیره است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/687626" target="_blank">📅 13:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc7ac4f298.mp4?token=cU2Rs8U3QgBuaOUg7BldAAS9hJMhpE0GDPcxah0dZvMBNOsAvSWl4JCrCCeIMBX2DPXYiOvYi53ieIQASg0cRWJ4bRhX2cC-3n4DKfehgloFcKvvrgyd7Apq3xiMOiWQed9cQyGJhxSpOtU-T8sIBe6q9r5TGy30Tv8cLem8DEtZDJap9ybFX0AVnrkAAzbf8QBMbomp9yjB9auEPXNmmnZ2Go4t3dITA5Mj_Iu3do_lXtNR6SX2Ch25wFv1fN5MLcOLBhe36Ek7-8GvJZnFmIh4uJ5usUKHvx8mvy5dRYabIeCbls0h5y3_T2bgtSGL63uyIdZW0JlvmVQQ-DaMCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc7ac4f298.mp4?token=cU2Rs8U3QgBuaOUg7BldAAS9hJMhpE0GDPcxah0dZvMBNOsAvSWl4JCrCCeIMBX2DPXYiOvYi53ieIQASg0cRWJ4bRhX2cC-3n4DKfehgloFcKvvrgyd7Apq3xiMOiWQed9cQyGJhxSpOtU-T8sIBe6q9r5TGy30Tv8cLem8DEtZDJap9ybFX0AVnrkAAzbf8QBMbomp9yjB9auEPXNmmnZ2Go4t3dITA5Mj_Iu3do_lXtNR6SX2Ch25wFv1fN5MLcOLBhe36Ek7-8GvJZnFmIh4uJ5usUKHvx8mvy5dRYabIeCbls0h5y3_T2bgtSGL63uyIdZW0JlvmVQQ-DaMCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات چینی یک قدم به استقلال کامل نزدیک‌تر شد؛ حالا می‌تواند بدون کمک انسان، باتری خودش را تعویض کند
🤖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/687625" target="_blank">📅 13:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687624">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پول تازه‌ای به بانک‌ها تزریق نشد
🔹
عملیات بازار باز هفته گذشته بدون تغییر در محدوده ۷۰ هزار میلیارد تومان باقی ماند.
🔹
رقمی که با سررسید شدن همان میزان ریپو، عملاً به معنای تزریق یا جمع‌آوری صفر پول از سیستم بانکی بود.
🔹
این در حالی است که تقاضای بانک‌ها برای منابع همچنان در سطوح بالای ۴۰۰ همت قرار دارد.
🔹
بانک مرکزی با ادامه سیاست انقباضی و سخت‌گیرانه به دنبال مهار رشد نقدینگی و تورم است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/687624" target="_blank">📅 13:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687622">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-rMy_VMnSUfZs0riILR2rtpeXdl74XtsOAKvznUMSJdWOHx7h7SCIEYI_i7zkwtTlMgtK4au0KxXF4e85SHZIh_VuPBGYSRjVrL-7i0lcWHdQ1MezOHH6htNck3I_FSNjDXf1ZkVF2rITiTWbGvZNVwBZ46COKMW9LRHeAocfx5rtlkV4KYixYNBRBO9pfUccin7DnLXx8ZWNs-XHHW9M1WV1BHJsJlYUZx-IJbcCAPwxIUJ8GEiyAk_MnIkp3YMTKwdis0S_toL11LmtCfBAsihHGcoUv0uw9-79ruK-MdZ64Tt_nGLxXv-ohx4xYa4lVgtfKm-E_OgRNHnfeFWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۵ شهریور ۱۴۰۵؛ ساعت ۱۲:۵۰
🔹
روند صعودی در بازار ارز و طلا امروز یکشنبه ۱۵ شهریور ادامه یافت و دلار آزاد وارد محدوده ۲۲۴ هزار و ۵۰۰ تومان شد.
🔹
هم‌زمان، هر گرم طلای ۱۸ عیار از مرز ۲۳ میلیون و ۵۲۰ هزار تومان عبور کرد و سکه بهار آزادی نیز در کانال ۲۳۱ میلیون تومان تثبیت شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/687622" target="_blank">📅 12:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا مدعی شده این ویدیو لحظه غرق شدن نفتکش ایرانی در دریای عمان است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/687621" target="_blank">📅 12:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
بهره‌برداری از نخستین مجتمع آموزشی ـ فرهنگی هوشمند کشور با حضور رئیس‌جمهور
🔹
نخستین دبیرستان شبانه‌روزی هوشمند پلیس کشور
با عنوان «مجتمع آموزشی و فرهنگی سپهبد شهید محمد باقری»، با حضور رئیس‌جمهور ، فرمانده  کل انتظامی کشور ، وزیر آموزش و پرورش و جمعی از مقامات عالی‌رتبه لشکری و کشوری، افتتاح و به بهره‌برداری رسید.
🔹
این مجتمع با
۳۵ هزار مترمربع زیربنا
، در هفت طبقه و با ظرفیت آموزش
۱۲۰۰ دانش‌آموز
، طی مدت‌زمان
۲۲۰ روز
، با راهبری فراجا و با اتکا به توان مهندسی و اجرایی شرکت ارکان سازه، احداث و تجهیز شده است.
🔹
این مجموعه با برخورداری از
زیرساخت‌های نوین آموزشی، فناوری‌های روز و استانداردهای بین‌المللی
و با رویکردی منطبق بر فرهنگ ایرانی ـ اسلامی طراحی و اجرا شده و با تکمیل تجهیزات،
آماده فعالیت آموزشی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/687620" target="_blank">📅 12:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687619">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
میزان ابتلا به کرونا از آستانه هشدار عبور کرد
رئیس مرکز مدیریت بیماری‌های واگیر:
🔹
از حدود سه هفته قبل شاهد افزایش موارد کووید-۱۹ در کشور بوده‌ایم.
🔹
میزان موارد مثبت کرونا اکنون از آستانه هشدار پایین عبور کرده است.
🔹
میزان موارد آنفلوانزا نیز در هفته گذشته مقداری افزایش داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/687619" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/157ab4d234.mp4?token=UPUAF0YyHcG6bwaOKPXyAd2YQ7u5e3MofyxLXKHEhLCURVp5qzJgaIC8gIyUAnxbkTp5FA_XYmTDPNgS_ocOpgUPmiRH1X4VJyp1s4EVDTzhy1sUphOcyMm9XsHXiu2BpNtyJKCRfBExBIH8y8TCA96K7SI0mob5QKn8yLT21Pussa1cl1xXZHlMoh65b69WXSTwSBt8IDa9hhZknQAl00yWd-PefobyiqCSWkn1Z-u-0g-ebCJxB7szm0lYOYvv3wK91-NPraGCEyVi9dSK3bIRSVckSdJ2nDGBuH-YavjTGKfwokBWU4O2DnTKouC9ZvnlXG_OXEs_fF--7KsNojOcTSM0P_K-XKFpb2RK37suHhgFsLKTKz7gFaviqCnzY9IRMUiw4VbPCZRpu8mDlX_Bd83J5wdVKGVfkz0X7pAcQ9a9RQtiznfCkrET-c2HkTYZergqABweoQmWDdej9EaPqV2TUpk_nqKIdZDdv2jE92vPzfA0NkLK3I0Br9Hu57v-mIqoaPlgMpl_Cf_iDkTZ-tUAHPYDEj1pwEpQXNO7Y9xcK4QaTuhDdtwHHGQcKHcvFaIkgWSdrbstrTwvmqbMWi7TzQIP4OjFwpGBi7isMTNbTt15hVJ6dIA9B2co_U7o3mLb2-7XuzWRlMuU3ZdWVhc3F12KThGnK9ZJB-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/157ab4d234.mp4?token=UPUAF0YyHcG6bwaOKPXyAd2YQ7u5e3MofyxLXKHEhLCURVp5qzJgaIC8gIyUAnxbkTp5FA_XYmTDPNgS_ocOpgUPmiRH1X4VJyp1s4EVDTzhy1sUphOcyMm9XsHXiu2BpNtyJKCRfBExBIH8y8TCA96K7SI0mob5QKn8yLT21Pussa1cl1xXZHlMoh65b69WXSTwSBt8IDa9hhZknQAl00yWd-PefobyiqCSWkn1Z-u-0g-ebCJxB7szm0lYOYvv3wK91-NPraGCEyVi9dSK3bIRSVckSdJ2nDGBuH-YavjTGKfwokBWU4O2DnTKouC9ZvnlXG_OXEs_fF--7KsNojOcTSM0P_K-XKFpb2RK37suHhgFsLKTKz7gFaviqCnzY9IRMUiw4VbPCZRpu8mDlX_Bd83J5wdVKGVfkz0X7pAcQ9a9RQtiznfCkrET-c2HkTYZergqABweoQmWDdej9EaPqV2TUpk_nqKIdZDdv2jE92vPzfA0NkLK3I0Br9Hu57v-mIqoaPlgMpl_Cf_iDkTZ-tUAHPYDEj1pwEpQXNO7Y9xcK4QaTuhDdtwHHGQcKHcvFaIkgWSdrbstrTwvmqbMWi7TzQIP4OjFwpGBi7isMTNbTt15hVJ6dIA9B2co_U7o3mLb2-7XuzWRlMuU3ZdWVhc3F12KThGnK9ZJB-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس مجلس در نطق پیش از دستور: در کنار میدان نظامی، اصلی‌ترین نبرد ما در میدان تولید و معیشت مردم است؛ مردم سختی را تحمل می‌کنند اما سوء مدیریت و کم‌کاری را نه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/687618" target="_blank">📅 12:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
قالیباف: آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است؛ هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/687617" target="_blank">📅 12:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
قالیباف:
آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است؛ هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/687616" target="_blank">📅 12:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687613">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyDQanKOFBKJRBTZK-SRvhFkc5Sk8Q_8R33caNITDm6OqiPeFWl7oZAdaNavDixQHgVTJbSf4GNASC6eazHkjWztwM_vGKLjZb2efwCR2TRAWQCgPDWClx4G7nH-8rOd44O84BOI6IUDjjx4cCXJ-6Gs-J_47f5wYRclLmSWdF6opPnjFK_VcSHIASF97sQMIF7GKQQafRLvzt0QfW3UDeG8dcB_CM0F-uRuducU9BaguCuZjR2SDnBzGU-cisg-p_68hnxLwPeyy3l_Wfi9HF5Bu_lx5_t9b0oPcwG8aQ1mqfTXSdZaXxX8aNfo806SGJ1yruv3rGuSS7_WEPQo9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q02U99VTxsq9XVNbK7totlPv7mnxes0yin4FP9NUgaH1Vtww_J2eMLBJtOqz_Xih3pF7rXai1s9ZYisk_77wYmimYAjmMENwQpO4Mphgp4NRcl-plQgDGUyeTHkcXZdzncLPoxMGzy5hfJTkxqlo5G4XFz8AIcNTbPFJZI3Qv5V9l3jQDI_vNFvyUmBvuOSDLqay4uncHqD8kb5yOIbq6eJ9IJFHBRLHdxXEKBFzCVMSsn-JqeVBc2PvLQ68STGSicT_4fqvSGp05BeIEVrRKWCMbYNHONUwTUY1LvhnI0Vkq49SHG-jAX8j1NTqgp_a19gwkjZub34_7VtTjBbCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرعت عمل در بازسازی پل‌های بمباران شده در جنگ
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/687613" target="_blank">📅 12:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687612">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وضعیت سربازان آمریکا در تایلند
🔹
پس از توقف ناو آبراهام لینکلن در تایلند، تصاویر متعددی از وضعیت نامناسب سربازان آمریکایی در تایلند منتشر شده‌است.
🔹
سربازان آمریکایی که ماه‌ها در‌ ناو لینکلن در وضعیت نامناسبی بودند حالا در خیابان‌های بدنام تایلند باعث رسوایی…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/687612" target="_blank">📅 12:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687611">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTj3sciWmSRn2rJgBaz91Pf-veBjPRomh-reQCTldTi6i8XjNPAd_VLTPfr8QF4cdmm6_dyekkNLngDiHkR2m5UOGmqA_BXLCoePsAitpj-_PoxBysXm1Gw2lVhR102gt5VKjDhvI1fq55jjg66en-JOagaW450dWK9QnhL-XeelpI2HBg3VAeV2bcNyekYmAhiy6Zkx-jzRLRFQw6gIxz9TSWLHEzwWOtz1sXB_82s6KEs88xL64OHje7i0RYd6JcoN1Rd6gi7QHkbcO5cFRo_F-FwLioO_MkKL8q2SR4O0vHYO5ryzgtVMsJfD-J15pH2dlyqeWJrhbCwXUTm8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نیرو: تلاش می‌کنیم قطعی برق متوقف شود
🔹
این درحالیست که وزیر نیرو روزهای اخیر مدعی شد قطعی برق متوقف شده اما همچنان خاموشی‌ برنامه ریزی شده پابرجاست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/687611" target="_blank">📅 12:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687610">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d334b1bd6.mp4?token=D5ftqbYZhUIwbPCdJSmtGrDtBSO4IX2DSAFwlRqNJ0Lp_NJlgQM0akcsQC1wH-GL2jK8GcE82yKKvphMFYSeBkadPA9VqTqga-DVdFHPYVGmKLqP-1U7jXWNMTvhokUbRXWsk_EqHUMEiBhf46zXd5M2YqY9syXOd0ONqbUC7SATPBYYa9oLFbcHPUdQEGqWXmQglLrifkKBo5g3IBhwKPFF-JT8n4cOoZ4WBsNZEkzmbZAboRBRTtd5QHkfUNoLwkmrcHWJ0L0GDd-7Q91QtQdtelq9h1KKeWR9fBY9j7FZQgayUu7XBVtcmJaz7maDPv43xZhqY35lH_o9F7BcZk4QBggoLWd6Gh6_3vaaCyo6ROVI5OEVw4yQ57MhsHLguXAdaZMgH7kL8Mzma-w-7usmZwT8w3QLogB3BRcVLevw9n09TU2FjyqHdVElhqjDXslTe8ZSPow7GqS1PzYsafOGnajjKHK3sVmAoSf1uI4EUImLNpzL1KD1UFUxSLiChzgEachfD0RtQW_DC-zek8XW7xDrK0pZ7lLtrit7-K8YvbZTG1YdR6jyfCNhv4blTAbtBzfBcnf11DArhhbm2YWNYcoDn3Kywda5rxR0A3-4JLAHjO7B1iBWNp35j4pHxRelWwjuSTDeQmgbBjMA_seiymNPhjq9dpWV3zJSVgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d334b1bd6.mp4?token=D5ftqbYZhUIwbPCdJSmtGrDtBSO4IX2DSAFwlRqNJ0Lp_NJlgQM0akcsQC1wH-GL2jK8GcE82yKKvphMFYSeBkadPA9VqTqga-DVdFHPYVGmKLqP-1U7jXWNMTvhokUbRXWsk_EqHUMEiBhf46zXd5M2YqY9syXOd0ONqbUC7SATPBYYa9oLFbcHPUdQEGqWXmQglLrifkKBo5g3IBhwKPFF-JT8n4cOoZ4WBsNZEkzmbZAboRBRTtd5QHkfUNoLwkmrcHWJ0L0GDd-7Q91QtQdtelq9h1KKeWR9fBY9j7FZQgayUu7XBVtcmJaz7maDPv43xZhqY35lH_o9F7BcZk4QBggoLWd6Gh6_3vaaCyo6ROVI5OEVw4yQ57MhsHLguXAdaZMgH7kL8Mzma-w-7usmZwT8w3QLogB3BRcVLevw9n09TU2FjyqHdVElhqjDXslTe8ZSPow7GqS1PzYsafOGnajjKHK3sVmAoSf1uI4EUImLNpzL1KD1UFUxSLiChzgEachfD0RtQW_DC-zek8XW7xDrK0pZ7lLtrit7-K8YvbZTG1YdR6jyfCNhv4blTAbtBzfBcnf11DArhhbm2YWNYcoDn3Kywda5rxR0A3-4JLAHjO7B1iBWNp35j4pHxRelWwjuSTDeQmgbBjMA_seiymNPhjq9dpWV3zJSVgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعله‌ور شدن موتور هواپیمای مسافربری کوآنتاس در نیوزیلند
🔹
هواپیمای بوئینگ ۷۳۷-۸۰۰ کوآنتاس هنگام پرواز به سمت کوئینزتاون، پس از مشاهده شعله از موتور، مسیر خود را به نزدیک‌ترین فرودگاه تغییر داد؛ حدود ۱۵۸ سرنشین داشتند و گزارشی از تلفات منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/687610" target="_blank">📅 12:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687608">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a159a5bee3.mp4?token=PFP9RBMoaYLfFZQ4cWGn4AZyXg3sn-WsF1WgVsgE-YSYspQcYEONlnCYqtdSfzN9Nt8PUTAxbf2263TokVU5oIU-kjPRc4WqxDXv70OE82MIPKAMGK5KX1zBSLUalH5MGoelyo6lDlvnE7scJtg-YTEjVbz_hgKV-5uRi0k6fRnxdKcxiN9zoNx4fnGAUlBqL-QxJ3rr-I8tQV55tMMFh3ZFa3rvftOcnbTgBSH6tGalTOHe07L7qYRn2eSdHANvMOUCxWSF42XB8RqInvVqNdUJNAqHmlKfnxAIqXFAvAKjYg2g-kZ0Y5AjaTuLnByzmTQjBQUc_iRvVT3VG_ztdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a159a5bee3.mp4?token=PFP9RBMoaYLfFZQ4cWGn4AZyXg3sn-WsF1WgVsgE-YSYspQcYEONlnCYqtdSfzN9Nt8PUTAxbf2263TokVU5oIU-kjPRc4WqxDXv70OE82MIPKAMGK5KX1zBSLUalH5MGoelyo6lDlvnE7scJtg-YTEjVbz_hgKV-5uRi0k6fRnxdKcxiN9zoNx4fnGAUlBqL-QxJ3rr-I8tQV55tMMFh3ZFa3rvftOcnbTgBSH6tGalTOHe07L7qYRn2eSdHANvMOUCxWSF42XB8RqInvVqNdUJNAqHmlKfnxAIqXFAvAKjYg2g-kZ0Y5AjaTuLnByzmTQjBQUc_iRvVT3VG_ztdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه میخواین رابطه‌تون طولانی‌ بشه و ده سالگی خودش رو ببینه، قول بدید این پنج نکته رو‌ر عایت کنید #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/687608" target="_blank">📅 12:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687607">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدمـاتجهيــــز | Damatajhiz</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57d3af292.mp4?token=tu4kPl2QbjWJAkm-Mh5wCIrK1BO7_XqPJ0AsJtWU2NlY6P0I04Y6Xk2abSiKVTy7vKuRiP52lwoDw1AOf2t8Op-Y27YB8jVFUGt_6JTsz5d_95Dn4XpCvfbpd64f91d2bFvw8O0o__m3I4s3WJ6UB_2VJMUlz5pV0ajU4lE-kGEqfs0XIzJIBJvN6yfcY8U1KWMGk2rmXF6M_GGy5mKxgHwT0PBYulwMBhGLzOc7CQ5wiEDiINJtZehXbhtBnPMO3p9_6TMONwHm7T6EBEyGPi3vs-cgIt3UKuLE2RvhHsUnEH7uhkDEQrpQmes1fPxQHepxojrhA1Kkp-0_zrZldA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57d3af292.mp4?token=tu4kPl2QbjWJAkm-Mh5wCIrK1BO7_XqPJ0AsJtWU2NlY6P0I04Y6Xk2abSiKVTy7vKuRiP52lwoDw1AOf2t8Op-Y27YB8jVFUGt_6JTsz5d_95Dn4XpCvfbpd64f91d2bFvw8O0o__m3I4s3WJ6UB_2VJMUlz5pV0ajU4lE-kGEqfs0XIzJIBJvN6yfcY8U1KWMGk2rmXF6M_GGy5mKxgHwT0PBYulwMBhGLzOc7CQ5wiEDiINJtZehXbhtBnPMO3p9_6TMONwHm7T6EBEyGPi3vs-cgIt3UKuLE2RvhHsUnEH7uhkDEQrpQmes1fPxQHepxojrhA1Kkp-0_zrZldA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
دمـاتجهيــز؛
انتخـاب ،قیمت ،تامین و تولیـد
تجهیـزات تهویـه و تاسیسـات با
اصالت
گارانتی
(از سـال ۱۳۸۳)
داكت اسپليت
+
ارسال رایگان تهران
كولرگـازي واسپليت
+
نصب رایگان
👌
فن كويل و تجهيزات كنترل
🏊‍♀️
استخــر، سونـا و جكـوزي
🔥
دیگ و تجهيزات موتورخانـه
☕️
تخفيف ويژه
دمـاتجهيـز تا
15%
- انــواع ايـرواشـر
- بـرج خنـك كننـده
- چيلـر و ميني چيـلـر
- زنت آپارتماني و صنعتي
- هواسـاز آپارتماني وصنعتي
🌎
www.DamaTajhiz.com
☕️
☕️
🙏
☕️
☕️
021-88822550 خط ويـژه
Join
🆔
@dama_tajhiz</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/687607" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687606">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMBxxuJnEzLksBSMCu7W-fnZ9fk-2_PWPbMFdRKNSUcfC5koELlAmRxZQB5UV7npGZq1ShEmGgBf5m7G5Kuep4h2bXljqAfNyOqk3tR93BavNlemvsgQSHrsr0bbi5tQZWBplLsyA83D1--GluuIchLteqF-qn_gyQmMNToBxJiSek6bYqV4LahCu7GZRjD6RayIOLgFznarhKU3Jr4RZop0gswjzAIGbI5rdpOoQcEBH0jEEH-5j2LczRiHKGe7mHXmI-wdfBFwrWyIhejXrRDQ_NpO9In4PyxmhbwNwoFbdVkdn4MqPYeSqo0F5Y3nPYslZ40KMxKeiMC5At6CAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوربس: هزینه‌های جنگ برای آمریکا بعد از جنگ هم ادامه خواهد یافت
فوربس:
🔹
هزینه‌های جنگ‌ها به ندرت به طور کامل محاسبه می‌شوند و جنگ فعلی آمریکا با ایران نیز از این قاعده مستثنی نیست.
🔹
حتی اگر این درگیری فردا پایان یابد، هزینه‌های پس از جنگ متعددی وجود خواهد داشت که برخی از آنها طی سال‌ها و حتی دهه‌ها ادامه خواهند یافت.
🔹
حتی اگر توافق تنگه هرمز حاصل شود، بازسازی ظرفیت تولید نفت آسیب دیده در طول جنگ، تأثیر ماندگاری بر قیمت‌ها پس از پایان جنگ خواهد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/687606" target="_blank">📅 11:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687605">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وزیر جنگ رژیم‌صهیونیستی: تا خلع سلاح حزب‌الله از منطقه امنیتی لبنان خارج نمی‌شویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/687605" target="_blank">📅 11:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687604">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
چند تخلف تا توقیف گواهینامه؟
رئیس پلیس راهور تهران بزرگ:
🔹
سرعت غیرمجاز بیش از ۵۰ کیلومتر، ۱۰ نمره منفی و سبقت غیرمجاز در راه‌های دوطرفه، ۵ نمره منفی دارد؛ تکرار تخلفات و پر شدن نمره منفی، به ضبط گواهینامه و ممنوعیت رانندگی منجر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/687604" target="_blank">📅 11:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687603">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xhp5KYORTFO2wRfhEldRxLT8QUT007FRkhdkRi6e7iQ4vgC5zyrSOFxAM9f_C-qX35cc24dA3va3mbzbiDzRlq3coVZWI6Xt5eeiQ8Yg1NACT09saMsgk7fkwOXPPSVR-lQzHBWH2J1zFCl3-XSOYwBDJqGUVpaPHDq-dwBM_sJN25Pke-L9YBGe6t7bkWOT6RuPcadHlO_WGprQbNpY26Hsg33Rbwywwc1T3jS1_VkNOqAxBzx_5Zq8WZX0snbpupZVpnwO_ic9VVJUiOWQoQPS-lXWkulUtuGKzzYBISIY47_ix5aBeiVNtSHfcDCF0QwC3rlw8vEU-9eQ7rloWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صاحب این طوطی که توانایی پرواز نداره، براش یه کوادکوپتر گرفته تا هر روز چند ساعتی باهاش پرواز کنه
🦜
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/687603" target="_blank">📅 11:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687602">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صادرات طلا و جواهر ایران تقریبا به صفر رسید
حجت شفائی، رئیس اتحادیه تولید کنندگان و صادرکنندگان طلا، جواهر، نقره و سنگ‌های قیمتی ایران در
#گفتگو
با خبرفوری:
🔹
به دلیل تحریم‌های فلزات گران‌بها از دوره اول ریاست‌جمهوری ترامپ، عملاً صادرات طلا و جواهر ایران تقریبا به صفر رسیده است و در سال‌های اخیر، صادرات بسیار محدودی از اصفهان و تهران انجام می‌شود که در مقایسه با کشورهایی مانند ترکیه، ناچیز است.
🔹
جواهرات و سنگ‌های قیمتی نیز عملا صادرات قابل‌توجهی ندارند و مشکلات داخلی مانند ناهماهنگی بین استاندارد، گمرک و بانک مرکزی نیز به عنوان تحریم داخلی بر این مشکل افزوده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/687602" target="_blank">📅 11:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687601">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
فهرست شناورهای متخلف در سایت «نهاد مدیریت آبراه خلیج فارس» به‌روز‌رسانی شده است  متن کامل پیام پی‌جی‌اس‌ای:
🔹
فهرست شناورهای متخلف در سایت به روز‌رسانی شده است. برخی از این موارد با اطلاعات داوطلبانه مردم به دست آمده است که پی‌جی‌اس‌ای مراتب قدردانی خود را…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/687601" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687600">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAcMgBuKPYkBl3cH0t00nw-fronYJSbTsEHuI6Wx-1xq4WO7uV7KbNcbQnmtYUlH1Xpm90cBAGeUrekKQKfAZkklzaYUwM8PJS07bclgE7W2JV8AM2_pVKCcMCt6XNIFq27ZduEcK1geiYjC6Kycskoxr1Ms_GMRXqmeGX8ee6OwUbgt-4c2Y7Ty2zbBDcv2ll5IbkgujpgB1pj5xeEeCz4x1vaLkgFriQSPn6o6Mkcyr75xjMOZAS-Ypsre2ItDhP9FbbqUU7gRGlfA_vWRwk4_F0bDIdD1CWfKUMDNFodJ8hhiXqN0cJ0kuKIDAckzF4JVB2PwX2I6Hs_PGPGBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاندار کردستان در پی انفجار تانکر سوخت ۲ روز عزای عمومی اعلام کرد
🔹
در پی حادثه دلخراش انفجار تانکر حامل سوخت در محدوده پلیس‌راه سنندج ـ همدان که تاکنون منجر به جان‌ باختن ۱۱ نفر و مصدومیت هفت نفر شده است، استاندار کردستان، ۲ روز عزای عمومی در استان اعلام…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/687600" target="_blank">📅 10:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687599">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpUWp-L_UAladNOXMYvL2ORYNz8mlKKAMTtSSycsTxxqwUqMoTNzghHGGC1usEjDtorK1lEgXz0EyTg5RoFkFF4tSSSfJVf6LTXKuP4kztZRujDUPG7Fxof0FVhjcYf01Jc_KCvvLafzg4iRWk3S2BD-w0wKapAoaQ5UZbSYY9g9qgRFG6ZPSHzdgv2Sm0vFcNih1g5KFE9IMn-_Ac8-x9nTbaBVqFgbQAdWA-qJ-6QHnwFaq9sa2c1KcmB6JM-2_RXqRU39zgdon8U48RInltl9gTwA5Et3r9Ug9Fc5jVAcGpd7o-2XHqGOF7UaIpjSO4dQCQ7xE8qlYB7JaWxioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر آمریکایی: فشار اقتصادی ایران، در نهایت به تسلیم آمریکا می‌انجامد
‏برت اریکسون:
🔹
درد اقتصادی فقط وقتی مؤثر است که به تسلیم یا تغییر رژیم بیانجامد.
محتمل‌ترین سناریو: رنج کوتاه‌مدت برای مردم ایران،
سپس تسلیم آمریکا و دادن امتیازات اقتصادی کلان به تهران.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/687599" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687598">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a7f5d352.mp4?token=LQZwUKYQY7A-g48ieyODCbsNVtwY5Zm1EVL_8h_ZLoBMkat3S-bzqfW5wv4ibOlR6nU96W-O2WphluK1Qr4n2o_rwY-XXmYvm3LXzDPvCJ0uPMoLXSzwEhSK7gp5AfXOnO1aR1LAnDF8isjtSAQ8WO8N0E8pNz-WyMTjDnhexDaq_GMuNWk646363fOKW6UpXp8jV7vjx7hD21yVL2TLWJH5CXG_D_SjgRvlKYkc-XkB6k9OnUhxJEM_xAmBuBrBE5Z_Z-ARsaBYW8mIaFU620J-IPTdWaqkwrP9NdfaZLR7l1Pp3Bx3assZwXnPSYTL6OiXXF7ZTObNG79qfbD7hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a7f5d352.mp4?token=LQZwUKYQY7A-g48ieyODCbsNVtwY5Zm1EVL_8h_ZLoBMkat3S-bzqfW5wv4ibOlR6nU96W-O2WphluK1Qr4n2o_rwY-XXmYvm3LXzDPvCJ0uPMoLXSzwEhSK7gp5AfXOnO1aR1LAnDF8isjtSAQ8WO8N0E8pNz-WyMTjDnhexDaq_GMuNWk646363fOKW6UpXp8jV7vjx7hD21yVL2TLWJH5CXG_D_SjgRvlKYkc-XkB6k9OnUhxJEM_xAmBuBrBE5Z_Z-ARsaBYW8mIaFU620J-IPTdWaqkwrP9NdfaZLR7l1Pp3Bx3assZwXnPSYTL6OiXXF7ZTObNG79qfbD7hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخواست دوباره دختر موشک صورتی از سردار سید مجید موسوی در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/687598" target="_blank">📅 10:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687597">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpHHTEw_AZQKVLHqHbiUTm7DEJPYmEcGuWcf9n7myOBEMdUAndAfqx1MuRwh2YjYMJCnYQSmDuRMGooXWEmRanZBsrJ1He2vNP8aEi4zCudpXWjaLAJvnbszyPpTLMDxGVeoT8nCK4b8ssoe71lmprlz7ZIBuX1rnjhy8BaFlwb3kzpSVlrDMiNH0lhFF3Wxb3wd-KwSFA9THtIoAnnbneO8WaVge_BVCSx6sCBt6gxHLy5pUf_vyx9Y3oZkL70ZxYJrzARKoYnyRxb3TGR3lI0B5-81obT9LpbhCFwFjR67eM7bgrxI_fQ_3V3qdp8D59ntEr6M_FzolzupnQEsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آژانس اطلاعاتی آمریکا: ایران مصمم به ادامه جنگ است
الشرق الاوسط:
🔹
بر اساس گزارش‌های اطلاعاتی آمریکا در هفته‌های اخیر، ایران نسبت به توانایی خود برای حمله به اهدافی در خاورمیانه اعتمادبه‌نفس بیشتری پیدا کرده است.
🔹
به نظر می‌رسد ایران مصمم است این درگیری را برای ماه‌ها ادامه دهد تا ایالات متحده را با چالش و فشار مواجه کند.
🔹
حتی در صورت نبود اختلالات جدی، حملات سایبری احتمالاً همچنان برای ایران روشی جذاب خواهد بود تا از طریق آن حمایت افکار عمومی آمریکا از جنگی را که از ابتدا نیز محبوبیت چندانی نداشته است، تضعیف کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/687597" target="_blank">📅 10:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687596">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f0ea32c5.mp4?token=K37zu_EQu87p8NhFzCcKnFTckArEvir5ChBnSNpJWd_Jigh48hSfhYca3HYhMR0hgFrF82QM-s7-DH6opNk7psNQT5aR98sfvjOzkZdVl6hB5j4kAbKNMadOPat8GOaAHgdhzjuRH-PuEkWxh1tHXsxRyQDuyqlHU9kRTIqHKuMre9Syxi4JHB17tZamQM8tiIXF2Y5CsxHQvqjE7KybpzjGnbT3ojdlp1Ht8MHZYNY5whREtdDfoWQsgjEoXstU7hh_jQptp9nW0JVkofeRhDQfhv_Obsi6yNcB0SJcQwAYnnh_ngNrYfacLaGIJSqQ38s64Vht1BzLpmCgZ4DsWSj46DnFoEAZjyZocb8LKsY4KXB58exiUZatHBhk00ddMIxnjaQd8aW7g-A2oVctx-IQ2WiiSMRer95C4bhzhS2QB59ctbVhWYEfyQkMgMgJA4tjsw9hqT7g1V7PMCbv4iv2uJfQESlhEJcD4HCwu1Do7i8J3E6k6sdpVkyEWwQPFa6paqoEBQpnAE-HPKSZOFID1N0h7cwMjlxFNN9nHaWY1KZIy-bSP6rxAGOP6UQ1teUC6fJVUyGNxjHKH8eoMEZljR22bBbNjIFBQi5yIcRU1EPO1P3OixliS27ANTv_YHh2CQn9pkqDtLZSiMOGBRevQParH1we01RdPl5ZKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f0ea32c5.mp4?token=K37zu_EQu87p8NhFzCcKnFTckArEvir5ChBnSNpJWd_Jigh48hSfhYca3HYhMR0hgFrF82QM-s7-DH6opNk7psNQT5aR98sfvjOzkZdVl6hB5j4kAbKNMadOPat8GOaAHgdhzjuRH-PuEkWxh1tHXsxRyQDuyqlHU9kRTIqHKuMre9Syxi4JHB17tZamQM8tiIXF2Y5CsxHQvqjE7KybpzjGnbT3ojdlp1Ht8MHZYNY5whREtdDfoWQsgjEoXstU7hh_jQptp9nW0JVkofeRhDQfhv_Obsi6yNcB0SJcQwAYnnh_ngNrYfacLaGIJSqQ38s64Vht1BzLpmCgZ4DsWSj46DnFoEAZjyZocb8LKsY4KXB58exiUZatHBhk00ddMIxnjaQd8aW7g-A2oVctx-IQ2WiiSMRer95C4bhzhS2QB59ctbVhWYEfyQkMgMgJA4tjsw9hqT7g1V7PMCbv4iv2uJfQESlhEJcD4HCwu1Do7i8J3E6k6sdpVkyEWwQPFa6paqoEBQpnAE-HPKSZOFID1N0h7cwMjlxFNN9nHaWY1KZIy-bSP6rxAGOP6UQ1teUC6fJVUyGNxjHKH8eoMEZljR22bBbNjIFBQi5yIcRU1EPO1P3OixliS27ANTv_YHh2CQn9pkqDtLZSiMOGBRevQParH1we01RdPl5ZKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تودهنی فرمانده سابق سنتکام به مجری صدای آمریکا!
ژنرال دیوید پترائوس:
🔹
شکافی میان نیروهای ایران وجود ندارد؛ رویای فروپاشی حکومت شکست خورد و استقرار پایگاه‌های آمریکا در منطقه جواب نداد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/687596" target="_blank">📅 10:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687595">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
پرداخت معوقات رتبه‌بندی بازنشستگان ۱۴۰۰ تا ۱۴۰۲
سخنگوی وزارت آموزش و پرورش:
🔹
پرداختی‌های بازنشستگان سال‌های ۱۴۰۰، ۱۴۰۱ و ۱۴۰۲ پرداخت شده؛ مطالبات تعدادی از بازنشستگان سال‌های ۱۴۰۲ به دلیل کامل نبودن فایل‌هایشان پرداخت نشده که طی یکی دو روز آینده پرداخت خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/687595" target="_blank">📅 10:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687594">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puBmhRjXaUzmTJhGBhHi0HgGsG-2XjklBiZxTW0r7MvOXD6w_0OcefXEhnV94MQi5r3xwbKBVBcoshZ9_kLbHxEsyOw4KQdJ4OakDpglcD7xshyE_QPoyqWd7qad9Z912cUEpfwQ8BCOSXVzfL7WcT9_LnGHY3xTcfZoN2kUrtwRUYlwbbYwwc5_P11YL0SWgbRUH5BQsHrSFXnSP8LhKd_MLkQ5Jhyslzrh4cOA7WXLNWaN9-JWmXfuiEEbsav91rKEXWHLgjY3xiVSYThkA_6ocjJiqM6pb5AfgpsOVD_C9FpbAI_Oom-LScInq-RnaekVFPTJTlCRdv-bPX1Dew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای پلاک شهرهای ایران و نماد هر شهر
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/687594" target="_blank">📅 10:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687593">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ثبت‌نام ایران خودرو برای ۱۳ محصول برای متقاضیان خودروهای فرسوده
🔹
منتخبان پس از دریافت پیامک، ۷ روز برای تکمیل وجه فرصت دارند و خودروها نیز حداکثر ظرف ۹۰ روز تحویل می‌شوند.
🔹
نکته مهم اینکه این فراخوان ثبت‌نام عمومی جدید برای همه متقاضیان نیست و فقط شامل افراد منتخب دوره قبلی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/687593" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687592">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
خوراک لوبیا رو‌ به سبک آشپزهای حرفه‌ای درست کن  مواد لازم برای سه نفر:
🔹
لوبیا چیتی ۲/۵ پیمانه
🔹
سیب زمینی درشت یک‌عدد
🔹
پیاز یک‌عدد
🔹
رب دو قاشق غذاخوری
🔹
نمک، فلفل، زرد‌چوبه، پودرسیر، گلپر
🔹
عصاره گوشت
🔹
قارچ ۲۵۰ گرم #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/687592" target="_blank">📅 10:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687590">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e0b143cc.mp4?token=MAVYm9wbFkZLMm_UkU2lN47f0kGx_y-GPUcgO-1L8IETqAkWhfl7wWg2fIx7YPqLilmd3cGZouIO3vFki-JSUuJZ8PWShw-1_MLLqTD6F1U19FzJ6Dzq38zNYiZrNA6_0KCQnViAPipuGu1oQO0tQJfo2O1Zs-Muv7IXGiHZrbwhqF0Ufw5JXGdoLxXFADgnTa5c8fFm7esYsVnaGic8_EEXBDhfpgsDbGl4wlXD4On_S8R7kbsh_Wt2o5s37A_VVIC9htPRre8YFLkEPaBlzIn9HeX-LpF--0otEUhNo-Pmwg1rb8wqWfAXuFFqB1yBlP-HG1GyyiLmb6SENko2zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e0b143cc.mp4?token=MAVYm9wbFkZLMm_UkU2lN47f0kGx_y-GPUcgO-1L8IETqAkWhfl7wWg2fIx7YPqLilmd3cGZouIO3vFki-JSUuJZ8PWShw-1_MLLqTD6F1U19FzJ6Dzq38zNYiZrNA6_0KCQnViAPipuGu1oQO0tQJfo2O1Zs-Muv7IXGiHZrbwhqF0Ufw5JXGdoLxXFADgnTa5c8fFm7esYsVnaGic8_EEXBDhfpgsDbGl4wlXD4On_S8R7kbsh_Wt2o5s37A_VVIC9htPRre8YFLkEPaBlzIn9HeX-LpF--0otEUhNo-Pmwg1rb8wqWfAXuFFqB1yBlP-HG1GyyiLmb6SENko2zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدل GPT-6 Astra معرفی شد؛ قدرتمندترین مدل OpenAI تا امروز!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/687590" target="_blank">📅 09:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687587">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTP_5owZzH0UGYKdjSmqWclcxEbqOCAKtbvbzBSN4iPPmdCpoAyVAGz9EGvn7Y3bTOaWSwIPIvktGWvVmRngCqPqQbj3iGIAwZ7kQ_by_WJIzRBQiwkh8_oKO6cIpkEovy6Oat5vlcO3eZJYlyfTFeF1CAon3ZpH11cGZcl5uD6mjZKdCVqwR8j1mPpYZmauMvRl4nsc7dWORt5Cu7NAyHS8cDHct2VbCD43y8xphH-wfrzy8tWzksGDzEiUCjoL3TJLO2MvF02CWZl6vsOX7OarGF1JfVAFQ9XHObyNK40JtK-ogZdJRSL7oeJOMXO_23GiZrCTyJmwYwomTY1GCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: آمریکایی‌ها در تعطیلات آخر هفته با افزایش بی‌سابقه قیمت بنزین مواجه شدند
🔹
در آمریکا در تعطیلات بنزین به رکورد ۴٫۰۳ دلار رسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/687587" target="_blank">📅 09:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687586">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a5b67fae.mp4?token=M9NHYSQc_maNw0RfW0kpZPMWnM6wcTO75Gwpam2sUmbro8H5wXNhuP58NmbCSq8NGAmDejfyGD8KGNum75Ko3hTSbYvWudapGLeNYE-E7fZ8fhFtSpU2M3HrD_UH4l2k_el4tb1M-OZ4xeCVsLR_1-uaer99336eqeA2i7VwMWoemxu4YmYY-09dJvRFTe035cVglnePrICvxd4Cp99kkQaWCkgSX1hnR50-G8iaUwpcmYiG801z1fvBLnh7C3dikOICd3nSgXDkvoGJ0EhNDzeSTOQKnlPy3EsWLWKp0tRzxbfj038MEjWKY60QLr31bJj0HPxyq96RYMUl34sKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a5b67fae.mp4?token=M9NHYSQc_maNw0RfW0kpZPMWnM6wcTO75Gwpam2sUmbro8H5wXNhuP58NmbCSq8NGAmDejfyGD8KGNum75Ko3hTSbYvWudapGLeNYE-E7fZ8fhFtSpU2M3HrD_UH4l2k_el4tb1M-OZ4xeCVsLR_1-uaer99336eqeA2i7VwMWoemxu4YmYY-09dJvRFTe035cVglnePrICvxd4Cp99kkQaWCkgSX1hnR50-G8iaUwpcmYiG801z1fvBLnh7C3dikOICd3nSgXDkvoGJ0EhNDzeSTOQKnlPy3EsWLWKp0tRzxbfj038MEjWKY60QLr31bJj0HPxyq96RYMUl34sKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا مدعی شده این ویدیو لحظه غرق شدن نفتکش ایرانی در دریای عمان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/687586" target="_blank">📅 09:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687585">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef115f097.mp4?token=Y52ydwx24Elb8HAHkMyzZFMIjIRwSOkUNVyQcEgwhIpAHDROrCBy5NEJfswdDVcNKF0KVERRZOXWZD0YlWmVnGAwuIeiHDEyHuwvxEEs7D9j2oaanNrsr0obOB0jf6ovXR1MiXHurcdO_Fe50bVa7QU6-dZGUxebirnSLw2jyKDpykRRiw82HRFetSkfXX8upuCVzXyVbFo6dnwkeEBobjc0GufK0bpGrC9aMwKqClSCbdqNjPQ1EW39D94Pc3T94FMwPIt-qUezc9PYKPpNX9ur1D5VzAZknHCPLREIFeyOfu0IM8Jp86biAnWqMIznANtm3RrHFddbYyFQ6lOdHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef115f097.mp4?token=Y52ydwx24Elb8HAHkMyzZFMIjIRwSOkUNVyQcEgwhIpAHDROrCBy5NEJfswdDVcNKF0KVERRZOXWZD0YlWmVnGAwuIeiHDEyHuwvxEEs7D9j2oaanNrsr0obOB0jf6ovXR1MiXHurcdO_Fe50bVa7QU6-dZGUxebirnSLw2jyKDpykRRiw82HRFetSkfXX8upuCVzXyVbFo6dnwkeEBobjc0GufK0bpGrC9aMwKqClSCbdqNjPQ1EW39D94Pc3T94FMwPIt-qUezc9PYKPpNX9ur1D5VzAZknHCPLREIFeyOfu0IM8Jp86biAnWqMIznANtm3RrHFddbYyFQ6lOdHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا تاکنون وصیتنامه‌ای از رهبر شهید منتشر نشده است؟
زاکانی، شهردار تهران در جمع دانشجویان:
🔹
متاسفانه، تمامی کتاب‌های کتابخانه رهبر شهید در اصابت نهم اسفند ماه از بین رفته است.
🔹
حالا اینکه وصیتنامه در کتابخانه بوده یا نه فعلا از وصیتنامه خبری نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/687585" target="_blank">📅 09:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687584">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fbb61dc4.mp4?token=ag8VQGtMs1OxaM1yLk3l1GmeyMDX43vT4IsWY-fDXCzM4RvETiO_n-u-E6FltMznU1cCrHYR7L4ArIb_sjEX1WuQTrigdUXOtw8h-6CQhHo5ghPAiB1Zuk-ihruwIsOg523DrVlqkZ6tSgfqyxVCMwVLoOc58b8Bd8eJHJh9wNCl409WPFbORjM5mUqzfDyaM1uBvadANAFmYNhPaCc2q3JSuRTIbiPyb7lZv5AnNq9VLkauRmcn1SuhydBb88DGJxpib_pI47rH0glJk7v-gsISBX1FXQtVcY2DHS8_j08iOcZymUqkt_x0EFzKCq6e34eckA3Iz5eaemmQSqAMeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fbb61dc4.mp4?token=ag8VQGtMs1OxaM1yLk3l1GmeyMDX43vT4IsWY-fDXCzM4RvETiO_n-u-E6FltMznU1cCrHYR7L4ArIb_sjEX1WuQTrigdUXOtw8h-6CQhHo5ghPAiB1Zuk-ihruwIsOg523DrVlqkZ6tSgfqyxVCMwVLoOc58b8Bd8eJHJh9wNCl409WPFbORjM5mUqzfDyaM1uBvadANAFmYNhPaCc2q3JSuRTIbiPyb7lZv5AnNq9VLkauRmcn1SuhydBb88DGJxpib_pI47rH0glJk7v-gsISBX1FXQtVcY2DHS8_j08iOcZymUqkt_x0EFzKCq6e34eckA3Iz5eaemmQSqAMeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یووال نوح هراری، تاریخ‌نگار و نویسنده‌: پول از میان می‌رود و نظام مالی مبتنی بر هوش مصنوعی جهان را اداره خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/687584" target="_blank">📅 09:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687582">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d70bd09e.mp4?token=dQR9jnaOs3dvKc1CGCVyv82tTb8ZNXSXT58gINlaK4MD1YJK6Q0SFN2Ww8AljkFlQ8ivvwqfh1LKapKtKaA436RQKdwUf562MKXlOBCFHVHQyuy_q_dXIJq-SUpLNJOMAK1IM8c5Guyqd0AvkT8yPbGWqJI4EQi_T_nTwK9rMStkdSPvJLMgydEsbJfzlaCz5PNomF0IgWhgjsnP7bC3CEqMHCFTKKhGy5JUCP7LJl-F5_IylB6Q7ve3rS2N3dlVS4CHCWpmIGniLCfzUL0JityP6V1rhM3FSFOp4ZzlFu0Pmnn0KxbMLOjVqQ6AjCeh6Wtfl14ZwKmLkUd2QxF5iEBF2lDApNm4m2Mvn_Zf7V4I7AWw52oD3SuA9FTdozqkTX4fP32JMNyly9GyUY6cYkhRBmwtI_LlOP1_Bq5cVTOSgqoaXdmVwoUnZwDAlcVVwwilbmVG-qmtbWcT3c4n_SsJ8IITH_0lLeUtZ5YvuM9IM2IY74eqLSAEJXjulmrc_Vpb7myq-Ysd3cL-hkoTVREIj5GYVYWnatX7N_CBP_prLQwr9o2YuVp6l5natKxwdUFy9516t1bYqbe8vvACyTphPTOvg91vdvNDeNuFpLXsJh4GvFBX5EQ8xsGpfXLV_UjZl3T0884KOUGYD4EA_1cud3_pc3WChE9247XQu6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d70bd09e.mp4?token=dQR9jnaOs3dvKc1CGCVyv82tTb8ZNXSXT58gINlaK4MD1YJK6Q0SFN2Ww8AljkFlQ8ivvwqfh1LKapKtKaA436RQKdwUf562MKXlOBCFHVHQyuy_q_dXIJq-SUpLNJOMAK1IM8c5Guyqd0AvkT8yPbGWqJI4EQi_T_nTwK9rMStkdSPvJLMgydEsbJfzlaCz5PNomF0IgWhgjsnP7bC3CEqMHCFTKKhGy5JUCP7LJl-F5_IylB6Q7ve3rS2N3dlVS4CHCWpmIGniLCfzUL0JityP6V1rhM3FSFOp4ZzlFu0Pmnn0KxbMLOjVqQ6AjCeh6Wtfl14ZwKmLkUd2QxF5iEBF2lDApNm4m2Mvn_Zf7V4I7AWw52oD3SuA9FTdozqkTX4fP32JMNyly9GyUY6cYkhRBmwtI_LlOP1_Bq5cVTOSgqoaXdmVwoUnZwDAlcVVwwilbmVG-qmtbWcT3c4n_SsJ8IITH_0lLeUtZ5YvuM9IM2IY74eqLSAEJXjulmrc_Vpb7myq-Ysd3cL-hkoTVREIj5GYVYWnatX7N_CBP_prLQwr9o2YuVp6l5natKxwdUFy9516t1bYqbe8vvACyTphPTOvg91vdvNDeNuFpLXsJh4GvFBX5EQ8xsGpfXLV_UjZl3T0884KOUGYD4EA_1cud3_pc3WChE9247XQu6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داگلاس مک‌گرگور، مشاور پیشین پنتاگون و سرهنگ بازنشسته ارتش آمریکا: ایران مثل عراق یا افغانستان نیست که با تهدید و فشار از هم بپاشد اما آمریکا مانند کشتی تایتانیک، زیر آب رفته و درحال غرق شدن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/687582" target="_blank">📅 09:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687580">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سپاه پاسداران: ناو هواپیمابر و ناوشکن ارتش متجاوز آمریکا مورد حمله قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/687580" target="_blank">📅 09:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXmkDk4xLw8CxCKx_rFgVkYUlHktzOdsPaJKuHR3o8jYPPbSqT_WQJqxJOmhJBvNfZTB_SAWNU6TpbZmJcQCxMBMrjuAvLaCF5d2blP-WDyuxr9sLzyP9F8P-oJXHZxCZ-9iIpQSTJDbmKsyvCaKlK1ikKBTw7lN9kBldqV99079OA9C13Y2BT1TEjchdVRM9q-0p3-ajZWYTfBSHWQP0_m4aBwXCsYjGB1ENA51mbuvzeKpCxB79erZicImRacr2Cxbct7pOyPBDAuG2CKGIGdRbeLqbvf6PTrlFyiNbafMZKi_KC8UO7yGsG_jP12E6krqTQSktG0Jdm9STsapaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7bqKyV2tZGvOoMXSyOUwPmqr2QY5v74sfJykLL2OXElU2ZwZXsNfN_hRbKGuoq-F25v3pXa7rT3cjJnrMuNUMs6IVu08Eqat2Pkq7JsTdeuo9SJsuNOoSxxsXZMlyIVPxq9uwwB484e4TeOg0AfVfa1RjkY8LVWNeHYBcC0ILdSEof-KRfzxvaSNidrelqZxbukXsMTRU_h_JJ4M2a2L5EYQ0wLeFQXzsGntlsMnKkA3szPBctha5aZSGBhbKuP0tCw9EMkWXejnITH_NSCWcB0BS3qWalP9YSqFBmSI6sFWCwBG0NNyfkkkJ8_gwj6CVxO9MUsJJpHcy25weP__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCaZYVIffT5ihLlEYjsGwgLLzmUXoDl1LzorqrMdP19Vh-P6Q1UUFe0VAaVw8q1wbLgKjxH38tEVlezmVJ9cLaEx80iPHHQIboiZ4f9QoHsPgG4Of0mKQjKm-s-hRBCVe0zKDD5vQdMRujTgsTW12kKM3_wOjhDb0kobmyh23ZmmuFF4RSMlJCVvilkFcRmkFqaA0UwFnxoXDo7kyd3rnbmpmPk740VxTgqx8mQFCcsX2It6uK0cDD4RBiLvAI7waoj_O1dV9o9ODNgfQUFzgXmImVZ4RijVGcUkW5gll-mCAu_nzkmY2ryi_0PgdYxz0_mE0kxf239eVvyV0v72WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/roVNQyeQ4xyzaliiyR4sNKntI_936kmTmOCh9twaEIMwtDINnalkbfz3bRY8KrE3YowUiAsJrm9-k1Bs5g_Br8P4PiCcm9hpYe2a9Bg5pnVp6fO_iEigK5ywybKilo7QA7DxT21eruvnXdlvg-QlT86EJAUtCQHgBTMdflRCKkwfjjqt36-7bSrMQxqTbHPfP5hV-SMWwWPNGcYj86vp4UWFk6kNYNrckYoitPUYMte8h4RPfjMxLJ7oKmM5dKv3fBcPxSjrlnM_wIo7-jXRhvKPdvEdGNvqVdNvLhMyxatoZ0vQERqoYzePOfhRT8GoF60LVVof6SzlwjMPrDYw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3BWrwO0FcNSiL3MJ8mKVG7DjVlHVQYQ7UcsPnAnXIj17pKPu6axd6CjfCznq2DQIA8qzlzWl1ZP_-on_oJvuKKYnN1rEFwEyHmwwn31vSMnUscbUt_E0XL2r8o0SyRrv1FPBCjAWzJhO2VqGIxZg9tqXA_R53_CEv3ilVif7XSDJtFcurysniD8-un6UaPZyEaWtFW2nRMMyfYBZj62ZKYp2Ynzy4lRSiK7ls2qGJe2YQMfircPgeZ-VkpyS286FQbRDbuOx3dyBqpdPA9LvbobKWpYGAyMuIPbtndxvqOOlEi2nR1-z--2hVSCwyzn3w2v05JRXrOzX_2Po0AJ-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند خمیر کاربردی که خیلی به کارتون میاد
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/687573" target="_blank">📅 08:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687572">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4309078e57.mp4?token=CNGMQaYYCCDcMwYf1aCl7nSgBqyVX1e7FW9B89N18W5yaupNQYtueibftoiBJRpkeoQJK-R1-85J_OCetL5E-UT6Y00GjN41iINc1pVfjIEHcE6Ezs6b2fDjbDsT9Zbwj8uoR7bibsGj4kq8s5mIE5LMuHQyiIkecO8oFuUmg2Ed-beF8qbJZm5SrK2lZMJaMxSaf9hN30f5aABX3dNeE7VhLTIwUK-5vHcEJoIA1CALrGRFDEkQqkrGSyKNWz6cGYFOGWfj76ATEM4qum-7rVxp6xS-TLbayD0v9yH0edMfi2kqubDg-unTga_EDt0idJ37M12KoHEHhBd4k3WEaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4309078e57.mp4?token=CNGMQaYYCCDcMwYf1aCl7nSgBqyVX1e7FW9B89N18W5yaupNQYtueibftoiBJRpkeoQJK-R1-85J_OCetL5E-UT6Y00GjN41iINc1pVfjIEHcE6Ezs6b2fDjbDsT9Zbwj8uoR7bibsGj4kq8s5mIE5LMuHQyiIkecO8oFuUmg2Ed-beF8qbJZm5SrK2lZMJaMxSaf9hN30f5aABX3dNeE7VhLTIwUK-5vHcEJoIA1CALrGRFDEkQqkrGSyKNWz6cGYFOGWfj76ATEM4qum-7rVxp6xS-TLbayD0v9yH0edMfi2kqubDg-unTga_EDt0idJ37M12KoHEHhBd4k3WEaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از فردا در نیمه شمالی کشور هوا سردتر می‌شود
هواشناسی:
🔹
بعدازظهر امروز و اوایل شب سامانۀ بارش‌زایی از شمال‌غرب وارد خواهد شد و در نیمۀ شمالی بارش‌ها آغاز می‌شود. دوشنبه و سه‌شنبه دما در نیمۀ شمالی کشور کاهش می‌‌یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/687572" target="_blank">📅 08:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687571">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idmemnj0a5HHA0SjZPcJFY10A_YPwJVTNDip-owlnpSV5kyGEKM_ju_FT5X9npoFPr9vra2YbgbqciPShPkSh6V0KwgBGu90jbnl2SepAkZYMze5jL5r780dtyIV5T66p31TOOuiOzoKeKzcQXaudcgkecmY54CG65Xbz4MAFw6p-amowXZocYVXO7vQxvZgOBtPAb8FY-jfgL4bBxwhykRdLBK3u0Uu8JuUCbS_2MUMo14W-YScnUrpZLMTshwM3o-nUhPEoAAinyeDqGQj0sNi_9jvKd-cjzz79I50Z43lJ7_HauKXBpYuft36iWhRKVmle9OjCLrKj2_aLk5MWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پروفسور جیانگ: اگر ایران کشورهای خلیج فارس را مجبور به ترک پترودلار کند، اقتصاد ایالات متحده با فروپاشی و انقلاب خیابانی روبرو خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/687571" target="_blank">📅 08:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687569">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0190e555.mp4?token=RCpZuFkuShVhQUwHjA0ZXJwPaUgp5ZiYFJFSWagH9m90i57PSZc91cXvqC9gH0doZ4Q-hrpXYdwXz92JZ-pdWNoevGJlt6_h-SgA8JE2_mPeGqqMvYxPPonRPlLfvg0SE7WlElvH9P8Dr9FzllS65ovTzaVgeINE1oae82Bz19kH73QXqLAoR9V65hXNxL3tNKVXM6EmCz0at8fTY4BX7FqWUiG2iYkDMzFpF-DMpGbNNheAFn1fIEOFdgAn11n3R0m8OrpYalqq6ngo6XvzHsaT-1DjOO3cHJIcBBIm3NpZlwxvyeDNKQ5lnRovsxIK984xtzZFbYOqpGGZHcxyRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0190e555.mp4?token=RCpZuFkuShVhQUwHjA0ZXJwPaUgp5ZiYFJFSWagH9m90i57PSZc91cXvqC9gH0doZ4Q-hrpXYdwXz92JZ-pdWNoevGJlt6_h-SgA8JE2_mPeGqqMvYxPPonRPlLfvg0SE7WlElvH9P8Dr9FzllS65ovTzaVgeINE1oae82Bz19kH73QXqLAoR9V65hXNxL3tNKVXM6EmCz0at8fTY4BX7FqWUiG2iYkDMzFpF-DMpGbNNheAFn1fIEOFdgAn11n3R0m8OrpYalqq6ngo6XvzHsaT-1DjOO3cHJIcBBIm3NpZlwxvyeDNKQ5lnRovsxIK984xtzZFbYOqpGGZHcxyRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مچ پات خشکه؟ این ۴ حرکت رو امتحان کن  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/687569" target="_blank">📅 08:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687568">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‌
♦️
سپاه: شمپاد آمریکایی مورد حمله قرار گرفت
روابط‌عمومی سپاه:
🔹
نیروی دریایی قهرمان سپاه پاسداران انقلاب اسلامی یک فروند شمپاد (شناور مدیریت پذیر از راه دور) ارتش تروریستی آمریکا که قصد ورود به منطقۀ حفاظت شده تنگۀ هرمز را داشت مورد حمله قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/687568" target="_blank">📅 07:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687567">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
حملۀ اشتباهی جنگندۀ سعودی به مواضع خودی در یمن
🔹
وبگاه خبری «الخبر الیمنی» گزارش داد که یک جنگنده سعودی روز گذشته مواضع نیروهای «العمالقه» را در استان تعز بمباران کرده است.
🔹
طبق این گزارش، ده‌ها تن از مزدوران وابسته به ریاض در این حمله کشته و زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/687567" target="_blank">📅 07:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687565">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c9528ee97.mp4?token=DV3tdbyr6Z-jRn3QtC6lZT4ln-AaRHSaVWA2-Z_4SgdgHv7uCp5KgV8ZyIsKilz9RtejXThwMBxTaoduQ48xvyoHsPMRA88NSDGy5KSHxfge4nxsLlNTpkwbzMjGqhlMy47x0TMBPqyeBGU7PSH3_1dPHq4AJ4THG9FkQw51IwZW9axWNQdWRZehzAZtNQJML_S2f_H3auNNkGBWJCCS6pZhAMcK9fNq6aNebnfYHhA5aJYz4LnEC14awXvLfWn8yEjk-hjfPDKHNNBCA-2N7HGfNbc-KnYMiHW5ScSP45xfjgzmEPuvsVMVTdUMAHtFdqrsj0Q6HRK7Oj7c7T9HFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c9528ee97.mp4?token=DV3tdbyr6Z-jRn3QtC6lZT4ln-AaRHSaVWA2-Z_4SgdgHv7uCp5KgV8ZyIsKilz9RtejXThwMBxTaoduQ48xvyoHsPMRA88NSDGy5KSHxfge4nxsLlNTpkwbzMjGqhlMy47x0TMBPqyeBGU7PSH3_1dPHq4AJ4THG9FkQw51IwZW9axWNQdWRZehzAZtNQJML_S2f_H3auNNkGBWJCCS6pZhAMcK9fNq6aNebnfYHhA5aJYz4LnEC14awXvLfWn8yEjk-hjfPDKHNNBCA-2N7HGfNbc-KnYMiHW5ScSP45xfjgzmEPuvsVMVTdUMAHtFdqrsj0Q6HRK7Oj7c7T9HFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آتشفشان در اندونزی
🔹
آتشفشان «آناک کراکاتوا» در اندونزی بامداد امروز فوران کرد که موجب لغو پروازهای جاکارتا شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/687565" target="_blank">📅 07:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687564">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d869f2116f.mp4?token=GK7DK1Wb4sEjd-Du3DnqFcJ69_BNjYzQhwehWt7zeuQHgwzheb4x1hmuODFmcs1N2OdHE5-skMrFWTuDzm58EVaz_OhJA7VH70BtB73gRH5y4IOC9wW67aDOmNIsAJzIiLYLK_iLsVfVudkCMD0oj2-mObNctQIPnTNcmFT4WVp9UNtOTmrNPeXBrcaiozlT-U9c1VcJLq56FrvfFeG7hcRyySArXWE1QdFwLVikWrNjsu7Jkj1GVxVDLnFWvRzf6uUxMtg2BxnM8RHWwYH2TbVruWDq6wcuMEGEO7T5QzBGLMYYriL0ULh0CEKkbcwh3VWf4n4LE_QIGa4ICUnGWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d869f2116f.mp4?token=GK7DK1Wb4sEjd-Du3DnqFcJ69_BNjYzQhwehWt7zeuQHgwzheb4x1hmuODFmcs1N2OdHE5-skMrFWTuDzm58EVaz_OhJA7VH70BtB73gRH5y4IOC9wW67aDOmNIsAJzIiLYLK_iLsVfVudkCMD0oj2-mObNctQIPnTNcmFT4WVp9UNtOTmrNPeXBrcaiozlT-U9c1VcJLq56FrvfFeG7hcRyySArXWE1QdFwLVikWrNjsu7Jkj1GVxVDLnFWvRzf6uUxMtg2BxnM8RHWwYH2TbVruWDq6wcuMEGEO7T5QzBGLMYYriL0ULh0CEKkbcwh3VWf4n4LE_QIGa4ICUnGWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فروریختن مناره و تخریب کامل کلیسای تاریخی اوهایو
🔹
آتش‌سوزی در کلیسای سابق سنت اگنس در تولدو، اوهایو، باعث فروریختن مناره این کلیسا شد. علت آتش‌سوزی هنوز مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/687564" target="_blank">📅 07:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بانک مرکزی از نظارت بر پلتفرم‌های آنلاین طلا کنار کشید
🔹
پیگیری‌ها از بانک مرکزی نشان می‌دهد بانک مرکزی قصد دارد «سامانۀ ناظر» را که بر موجودی طلای پلتفرم‌های فروش آنلاین طلا نظارت می‌کند، کاملا در اختیار ستاد مرکزی مبارزه با قاچاق کالا و ارز قرار دهد.
🔹
این یعنی بانک مرکزی مستقیم بر فعالیت پلتفرم‌های فروش آنلاین طلا نظارت نمی‌کند.
🔹
با اتصال پلتفرم‌ها به سامانۀ، موجودی طلا و دارایی هر کاربر به صورت آنلاین قابل رصد است، اما مسئولیت آن با بانک مرکزی نخواهد بود./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/687563" target="_blank">📅 07:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
لغو ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها
معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
🔹
ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها، با اجماع کامل همه اعضای ستاد ویژه ساماندهی و راهبری فضای مجازی برداشته شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/687562" target="_blank">📅 07:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
کارت شرکت در آزمون کاردانی به کارشناسی ناپیوسته ۱۴۰۵ از امروز منتشر می‌شود
🔹
آزمون کاردانی به کارشناسی ناپیوسته ۱۴۰۵, جمعه ۲۰ شهریور برگزار می شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/687561" target="_blank">📅 07:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
کالابرگ سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲ شارژ شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/687560" target="_blank">📅 07:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_kUamt0BPwupmrkKhpaZVb8A1FOTNiwAZbetYvAPxI1Sxn9i2Zp3zla5VmEZJSDS5FSID-t7Pqh5A-5KrfjPegH01NDE0Au4xZLFwePeEwLBit6wanf-HmdNJWCmRrfhrMLhML-QDGSfi1xtHpdYPA3F9ewCePaPndVGeuMfPsFmrMiYwNlxnBA-fPA2uSZDRDIPmvWLORHiaHu2e8tx2xtVbHbYN_Y7ULLiROvXwTM8Aw7yR4gtMiw5qFEHgVDEVc2bUtXW6F94jNv4Rhdks1i6tMItXV6QTCXuAaeWBKX2-CjWgqWClWd-FbWLE1esulvlsr8L4tAgB0kbL_PwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۵ شهریور ماه
۲۴ ربیع‌الأول ۱۴۴۸
۶ سپتامبر ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/687559" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687558">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGoldiran | گلدیران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80aba6e820.mp4?token=Wd7qEnBLRzt9RsJ0PlKvVMgxLiCqBajCFou4AlR0Wsk_mpsW5F9s6LtsBhonyem_y_dXnlf0Yp8UM3b3NFesQjCv9Qp-1AErT2_WenxN00SJYqJgvpEGI7FKq3JyUR7RxBKA28PyvlbQfPc1VVjiF6LsljIcD3zP8CvIkNzqk48RkqYfCLwtTfHIHYON65N2m5hZLLMr9W1NCIZAFl1RXj6X4mhPjx0NHHGPInz-odOrB5flsXt6TZ44TMk7jtuZ1_5m3Fq4aWF8ZRuXoIsFIZUfAsRg1Y0ixHGu_CRMUy5kiUZDSpCN0WNqT_bS4hJTWTh3rq8RDNBp8fE1cB-FrJHbgsSXAYtHly72GfIP23_vc8dxOIlz6pY41RFT7MhsmGIgMDGz9LvnRHhaQ-KmgeB__qnYLnpaA5IH99L8H1kV-0S41z1y3TzRv0JS3M-8YnLDtD6Vx7e7gl_c4YVHULQYnr5PQzZxaQOQPpRwG1eXZ2OGDDCjx47DoEYqTuuHsqK7CPpvRH2jS3_3HjAC6kD_ujoNv5_cYgRkNtTobpH8qfakHPwNJDlaOqlXiwh4Owhi54w8sqEb-wR4L1eYYyD0ipPUvv9d-Ar_C4LCR3TqCkgagrYEq5WGN3IUstv5pVNYevArJ0sm9ljXQeWJZIPEHAEFhMSBs-_a4lD6FwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80aba6e820.mp4?token=Wd7qEnBLRzt9RsJ0PlKvVMgxLiCqBajCFou4AlR0Wsk_mpsW5F9s6LtsBhonyem_y_dXnlf0Yp8UM3b3NFesQjCv9Qp-1AErT2_WenxN00SJYqJgvpEGI7FKq3JyUR7RxBKA28PyvlbQfPc1VVjiF6LsljIcD3zP8CvIkNzqk48RkqYfCLwtTfHIHYON65N2m5hZLLMr9W1NCIZAFl1RXj6X4mhPjx0NHHGPInz-odOrB5flsXt6TZ44TMk7jtuZ1_5m3Fq4aWF8ZRuXoIsFIZUfAsRg1Y0ixHGu_CRMUy5kiUZDSpCN0WNqT_bS4hJTWTh3rq8RDNBp8fE1cB-FrJHbgsSXAYtHly72GfIP23_vc8dxOIlz6pY41RFT7MhsmGIgMDGz9LvnRHhaQ-KmgeB__qnYLnpaA5IH99L8H1kV-0S41z1y3TzRv0JS3M-8YnLDtD6Vx7e7gl_c4YVHULQYnr5PQzZxaQOQPpRwG1eXZ2OGDDCjx47DoEYqTuuHsqK7CPpvRH2jS3_3HjAC6kD_ujoNv5_cYgRkNtTobpH8qfakHPwNJDlaOqlXiwh4Owhi54w8sqEb-wR4L1eYYyD0ipPUvv9d-Ar_C4LCR3TqCkgagrYEq5WGN3IUstv5pVNYevArJ0sm9ljXQeWJZIPEHAEFhMSBs-_a4lD6FwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☀️
این تابستان، خرید راسل با هدیه نقدی همراه است.
در جشنواره تابستانی جی‌پلاس، با خرید و نصب ساید بای ساید چهار درب Russell، هدیه‌ای ویژه در انتظار شماست.
تمام خریداران این محصول پس از نصب، حداقل ۱۰ میلیون تومان هدیه نقدی دریافت می‌کنند و بر اساس قرعه‌کشی، این مبلغ می‌تواند تا ۲۰ میلیون تومان افزایش پیدا کند.
برای مشاهده جزئیات محصول و خرید، به فروشگاه اینترنتی گلدیران پلاس مراجعه فرمایید:
goldiranplus.ir
مشاهده آدرس فروشگاه‌ها
@goldirangroup
گلدیران | روی خوش زندگی</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/687558" target="_blank">📅 01:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687557">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5072b66a5.mp4?token=lctbIftGvMFZ2jGrtyp3_HfzNsE0zhLogkirzFQ3eZ3R6Ho3BYKzBdxjvyx-ZjDpfF4gvmAZo8jbCwsiAriqWD0em_UI2s9OlakY0D91KnSYp828_z7jCA5Lo3AKDFDjB0GtT7lZi5HwoVd9ndzh18BgkCMw6OLNkh6cb0dzYIbSR-P-kM4N7GG0yDde8iWvjuHb1vHWdpLrfY218slq93S7ZABN_T0abhsuh0zfITxP766dOfS0gzWZqtStqZlORhx7ga2MAH0grGOU8JruN_p59_go9ZsFb1niz6dtuC8CchI0Utyzxd3WZ2fHIAHjdNTlXh7ZCNcASACMFVORtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5072b66a5.mp4?token=lctbIftGvMFZ2jGrtyp3_HfzNsE0zhLogkirzFQ3eZ3R6Ho3BYKzBdxjvyx-ZjDpfF4gvmAZo8jbCwsiAriqWD0em_UI2s9OlakY0D91KnSYp828_z7jCA5Lo3AKDFDjB0GtT7lZi5HwoVd9ndzh18BgkCMw6OLNkh6cb0dzYIbSR-P-kM4N7GG0yDde8iWvjuHb1vHWdpLrfY218slq93S7ZABN_T0abhsuh0zfITxP766dOfS0gzWZqtStqZlORhx7ga2MAH0grGOU8JruN_p59_go9ZsFb1niz6dtuC8CchI0Utyzxd3WZ2fHIAHjdNTlXh7ZCNcASACMFVORtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از ۴۰ سالگی، چه ویتامین‌‌هایی برای بدنت ضروریه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/akhbarefori/687557" target="_blank">📅 00:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687556">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
منابع یمنی از کشته شدن حداقل ۳۳ نفر از شبه‌نظامیان «العمالقه» (همسو با امارات) در حملات نیروهای ارتش و انصارلله یمن خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/akhbarefori/687556" target="_blank">📅 00:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9FQp0q1FyzU1zSVtgngiBOgKgdqofhj_9NayuZ5EVO5zKDtv9f9hLZivCck9DCZFMsnz6d9_JaHVP-uab_hq6g6W5CBdlHWd28Bvpa8qsmuTUo1VkTMUTjnMF78yhmesdWKNfL4u2noSjBYcKZonMXwzgJuhmivgpAo5EJADNQ8UNRI5kuPUV8ERmYVslIzYryHdjMUNYcm6qo037Z7IPUmxvB9zGEj6RZOHQGRfoqdx4i-TDi8PG9Vd4zhP21bjIP2tfyJl4v3z2zmatye0WHKFefQDoKLrpSzWvqOJS5iwYG-HkcaUoX-mjaZKhf8Wnyo0oR07QFwbPPAmImJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رقیب نتانیاهو برای ایران چه برنامه‌ای دارد؟ | از «منطقه کشتار» هسته‌ای تا بازگشت عملیات موساد | توهمات ناتمام صهیونیست‌ها
🔹
با نزدیک شدن به انتخابات پارلمانی اسرائیل، رقابت برای نخست‌وزیری وارد مرحله حساس‌تری شده است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3242959</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/akhbarefori/687555" target="_blank">📅 00:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687554">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5558d5321a.mp4?token=AyfzVdxWw_oAMM3Y4PvN1d-0TVGezkSfG_JZdFn3IiNnutFIZ7HPnfTtbQ3cYiWJB4-bYl8QBQXKrhCsblkNmWjJ3sRb4XNN-Xusxx7I7qMJ7MFxrRrUqANMGBQi2H1Vwk4JbygnvUWS62SE9yrauzP_6gRyWZBd9KLw__4kFveFEFo4JOSeZnaRBGbdJAI9nCUIo1wkWbmQ3cQhG8QnO6AgQI87ZbrvTz8EAjSx-6qJX-oMrV0Kb44qbZTegGxlF0YFK4BbeRt1WhgtdEro3x1O9olrpvqwea9fe_3x_O4KfSkeiy_qrkAwSKHLcAqvEu_2uJVqFhzGoyNEelzHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5558d5321a.mp4?token=AyfzVdxWw_oAMM3Y4PvN1d-0TVGezkSfG_JZdFn3IiNnutFIZ7HPnfTtbQ3cYiWJB4-bYl8QBQXKrhCsblkNmWjJ3sRb4XNN-Xusxx7I7qMJ7MFxrRrUqANMGBQi2H1Vwk4JbygnvUWS62SE9yrauzP_6gRyWZBd9KLw__4kFveFEFo4JOSeZnaRBGbdJAI9nCUIo1wkWbmQ3cQhG8QnO6AgQI87ZbrvTz8EAjSx-6qJX-oMrV0Kb44qbZTegGxlF0YFK4BbeRt1WhgtdEro3x1O9olrpvqwea9fe_3x_O4KfSkeiy_qrkAwSKHLcAqvEu_2uJVqFhzGoyNEelzHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبتهای تامل‌برانگیز آزیتا لاچینی درباره زندگی...
🔹
اگر درست زندگی نکنیم، چی میشه؟ به کی ضرر می‌زنیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/akhbarefori/687554" target="_blank">📅 00:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687553">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
انتشار برای اولین بار، تصاویر منتشر نشده از رصد و اقدام علیه شناورهای متخلف
🔹
اقدام و مدیریت قاطع نیروی دریایی سپاه در تنگه هرمز؛ هر گونه اقدام مشکوک مورد هدف قرار می‌گیرد.
🔹
ایالات متحده بزرگترین تهدید برای امنیت کشورهای منطقه و تجارت دریایی است؛ پشتیبانی و اسکورت ایالات متحده دروغی بزرگ است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/687553" target="_blank">📅 00:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687552">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
اولیانوف نماینده روسیه: در جلسه شورای حکام روز دوشنبه درباره ایران بحث خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/687552" target="_blank">📅 00:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687550">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
خبرهای جذاب امروز را به انتخاب مخاطبان خبرفوری بخوانید و ببینید و نظر بدهید
🔹
🔹
فاز جدید جنگ ایران و آمریکا | حمله به نفتکش ایرانی در جزيره خارک
👇
khabarfoori.com/fa/tiny/news-3242835
🔹
پشت‌پرده شایعه حمله اتمی آمریکا به تهران چیست؟
👇
khabarfoori.com/fa/tiny/news-3242751
🔹
ماجرای اعزام ناو از کره به خلیج فارس | ایران با کره جنوبی وارد جنگ می شود؟
👇
khabarfoori.com/fa/tiny/news-3242872
🔹
جزئیات فعالیت شبکه فحشا در شهرداری | نقش یک مسئول شهرداری در سازماندهی شبکه فاش شد
👇
khabarfoori.com/fa/tiny/news-3242669
🔹
خبر تکان‌دهنده درباره سرنوشت غم‌انگیز خواننده زن قبل از انقلاب
👇
khabarfoori.com/fa/tiny/news-3242916
🔹
خبرهای لحظه‌ای جنگ را اینجا دنبال کنید
🔹
khabarfoori.com/fa/tiny/news-3242976</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/akhbarefori/687550" target="_blank">📅 00:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687549">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
بازداشت عوامل رژۀ موتوری منتسب به سازمان منافقین در حوالی کرج
🔹
روز گذشته ویدئویی در فضای مجازی منتشر شد که در آن ظاهرا تعدادی از هواداران سازمان منافقین در خیابان‌هایی که گفته شده در حوالی شهر کرج قرار دارد، اقدام به حرکت با موتورسیکلت و خودرو کرده‌اند.
🔹
تمامی افرادی که در این کلیپ حضور داشته‌اند، توسط نیروهای امنیتی شناسایی و دستگیر شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/akhbarefori/687549" target="_blank">📅 00:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687548">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR8pqSm5EUAeWNh8qI7doAyK2GMdUBnid8EW3tGsQtliCzkxHynATxabJqgCFgnL39ZDu1MDmCXtppE3a-Nz9c97TzGfVoLb4SIlIUWVV3s6pfTuhp893EyxC9OqiKX4kSwaa1NWZ00FDVZNc-39rtrtBJQAddMVOeq3RkJbQh0MFS8_3sJhn0IoJfojl5cSQ5OGgMMFndVwj0ZImUt9f4d8YUEC7fSDcPaE2ogN-egt4B5V_4btTuOOCRsv7WJdEdSt3xzqq8kj2vixBVQCc3Wii4C9hrXH43t_TQ9URSEkH23-f5GU1rrYZcOprQXxAJnjOheuvYZ1RL7bE9mFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦋
خاص بپوشید، متفاوت دیده شوید
🦋
حوریا عبایا | HORIA ABAYA
مجموعه‌ای از عباهای لوکس، مجلسی و روزمره با طراحی اختصاصی
✨
با پارچه‌های خاص و وارداتی، همراه با گلدوزی و نگین‌کاری‌های ظریف و منحصربه‌فرد
از مدل‌های مینیمال و روزمره تا عباهای فاخر و خاص،
برای استایلی زنانه، شیک و متفاوت
🤍
📍
خرید حضوری از شوروم حوریا عبایا در فرمانیه تهران
📦
ارسال با تیپاکس به سراسر ایران
مشاهده مدل‌ها، قیمت و ثبت سفارش
👇🏻
📸
اینستاگرام:
https://www.instagram.com/horia_abaya
کانال بله:
https://ble.ir/horia_abaya
📲
سفارش و مشاوره:
09103156129</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/687548" target="_blank">📅 00:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687547">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMUDRaOXfuKBUFERsX-SfQX_F6raVIW7CBDSgSMJ2PRBS1Q3o3-m8sIwSyw6tyTtEio7TlkVG5z3RFBo15Wk1THzsYFr9fuqX4uhxIlzinKaNHNh-vBCIAPFhLRiFnxvPFjHrltVrxdeiy-Dw02Y4JG-qwsMBOsHpoZr5IYmKHw5IreE02fs8kUumrxWAfspHGToAKjJvMyltDUdUtYPyn6T5lYhgBe5GG0YDW62nRxVh9GGW6CeFcWM2HGi4qHrz5I2xz6q7sReS_s2XswzzKMNSYzjAKDusHEmFL8_izaMBi6nn7rCd_fAm2-eZuEnYWuy3UdBVfn98fFLOvMThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/687547" target="_blank">📅 00:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687546">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صولت مرتضوی: حسن روحانی همه مسائل کشور را به برجام پیوند زده بود و حتی تلف شدن گاومیش‌ها در خوزستان از کم آبی را به برجام پیوند می‌زد/ رشد اقتصادی در دولت حسن روحانی کمتر از ۱ درصد بود و شهید رییسی رشد اقتصادی را به ۷ درصد رساند
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبرفوری :
🔹
ترامپ برجام را پاره کرد و بسیاری از مفاد برجام را هم دولت اوباما اجرا نکرد و زیر میز زدند. دولت رییسی گفت اقتصاد بدون برجام هم قابل اجرا است؛ رشد اقتصادی را به ۷درصد، نرخ بیکاری را از ۱۰۰ درصد به ۷/۶ درصد، میزان نقدینگی را از ۵۰ درصد به ۲۹درصد، تورم را از ۵۰ درصد به ۳۲ درصد، صادرات نفتی را از ۳۰۰ تا ۴۰۰ هزار بشکه نفت در روز به یک میلیون و ۷۰۰ هزار بشکه رساند؛ اینها بدون برجام بود یا با برجام؟
🔹
در جلسه‌ای آقای روحانی اعلام کرده بود اگر کسی در مملکت ۳۰۰ تا ۴۰۰ هزار بشکه نفت در روز صادر کند، بگویید او را وزیر نفت بگذارم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/687546" target="_blank">📅 23:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687545">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4d13812.mp4?token=g9S3Ahrrj07nqZKmwpWXscnNH6SdEhuWxRyD7pdKnZPhpvWa8cAuXMT7UDMOsvxkDIx8KVjbFwTPtlgoYAwEmWiUGXCVCTEx2_bXytyhGr3nmlWpDGLIHgpPILLHY1pQ7TDwv-KE4o4e5Pwwk_8BbkWLVpw-bBeDajHwWSW-AvXca1j-MPLU4Gh9w-u1e1LYlC-e9q2Uq324q0Ifoj7Xx4QstejjHFkLfBxi5lCI_mSKe75ExAUxnMF_lo6utTt-rHLue-h5-mvmedFwJFp4n55AC2kcwJhx4UGJfnAwXUUT3YVlwnOYgriYwX9xxON9w0mRTasHbXHa-PCSyU4wCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4d13812.mp4?token=g9S3Ahrrj07nqZKmwpWXscnNH6SdEhuWxRyD7pdKnZPhpvWa8cAuXMT7UDMOsvxkDIx8KVjbFwTPtlgoYAwEmWiUGXCVCTEx2_bXytyhGr3nmlWpDGLIHgpPILLHY1pQ7TDwv-KE4o4e5Pwwk_8BbkWLVpw-bBeDajHwWSW-AvXca1j-MPLU4Gh9w-u1e1LYlC-e9q2Uq324q0Ifoj7Xx4QstejjHFkLfBxi5lCI_mSKe75ExAUxnMF_lo6utTt-rHLue-h5-mvmedFwJFp4n55AC2kcwJhx4UGJfnAwXUUT3YVlwnOYgriYwX9xxON9w0mRTasHbXHa-PCSyU4wCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی پزشکیان آسانسور را ممنوع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/akhbarefori/687545" target="_blank">📅 23:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687544">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان شرقی(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a553f8c48.mp4?token=RIXYmApoOC1q_AeKwHvj_CjVVN5kzZTYRptepqzJL5TK2jeilDoUHgxS7kGM-yeNJYge1xNSbYznlo1T6aCmgBMw4L6qcPndm2s2OK6rekyDzJx5ejmi4aJ_9eakpaMyqy6zYRSxuIxuHw_nOsT4BQj8N_RQOzuMdeAiFBX4vwFABSLH52WkEXDikL31XGHWukI4wOgjE9VSEpiV_uwpjhbHyBLISXOus9ln2zEdpsQyJoP3BM6RPFG7Fmh0hWA-8u79l7ZKcsxTiOuAyFIEbddJrSRfLFvxPTbVeNgYlvYURKlogA7cr8GnUFqUWUqql47UBam4NN1c43zUDUmh_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a553f8c48.mp4?token=RIXYmApoOC1q_AeKwHvj_CjVVN5kzZTYRptepqzJL5TK2jeilDoUHgxS7kGM-yeNJYge1xNSbYznlo1T6aCmgBMw4L6qcPndm2s2OK6rekyDzJx5ejmi4aJ_9eakpaMyqy6zYRSxuIxuHw_nOsT4BQj8N_RQOzuMdeAiFBX4vwFABSLH52WkEXDikL31XGHWukI4wOgjE9VSEpiV_uwpjhbHyBLISXOus9ln2zEdpsQyJoP3BM6RPFG7Fmh0hWA-8u79l7ZKcsxTiOuAyFIEbddJrSRfLFvxPTbVeNgYlvYURKlogA7cr8GnUFqUWUqql47UBam4NN1c43zUDUmh_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصمیم جنجالی داور؛ از کرنر گلگهر تا گل تراکتور
🔹️
داور ابتدا به سود گل‌گهر کرنر گرفت اما لحظاتی بعد تصمیمش را تغییر داد و ضربه دروازه اعلام کرد؛ تراکتور هم بلافاصله بازی را شروع کرد و در ادامه مهاجم این تیم در موقعیت تک‌به‌تک گلزنی کرد.
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/687544" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687543">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy56NaymjI-jmzjSnmS8FElzDTPyC4IbAVRLL0iQYaznkdCW72nXzhnHdDy6YeQpOIEhpmhSxr-FeGUdNjL9LmaAwIH-75Hl6Zvx8nL_dQCKI0sIgxcrGJSVcU8cXaccE5PZC83u9VVfQ-pLwze96DGO5wgh5sbVloh1T4AXHODGYRe_CEpBzsm_mB7bOSASd_lrhQ4hQwxANGegtLsxAaDaCFrhKUuR5suRFu7sGO3VGHYXVMI6_JnLA61P02AHwsCKb2zeQfWlg1Ooc8VNwmdrGDL_jrVzCs7h6QR7xowLt7ss_yOe8t-klehG0ZNMDmvX0ITUSN2dr8lqHLjyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«فخوز» به تابلو بازگشت؛ اعتماد سهامداران به آينده فولاد خوزستان
🔹
فروردین‌ماه ۱۴۰۵، تنها یک ماه پس از آغاز جنگ، شرکت فولاد خوزستان هدف حمله دشمن قرار گرفت و در جریان این حادثه، بخش‌هایی از این مجموعه با آسیب جدی مواجه شد. با این حال، اتکا به توان فنی و دانش بومی و تلاش مستمر کارکنان و متخصصان شرکت موجب شد فولاد خوزستان در مدت‌زمان کوتاهی وارد مرحله بازسازی و ریکاوری شود.
🔹
حالا پس از گذشت حدود پنج ماه از آن حادثه، نماد «فخوز» بار دیگر به تابلو معاملات بازگشته و واکنش بازار به بازگشایی سهم، قابل توجه بوده است.
👇
👇
akharinkhabar.ir/local/10996072/
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/687543" target="_blank">📅 23:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687542">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
هشدار هواشناسی برای شمال کشور؛ بارندگی شدید در راه است
یک کارشناس سازمان هواشناسی:
🔹
بارندگی شدید از روزهای دوشنبه و سه‌شنبه در سواحل شمالی آغاز می‌شود و با تشدید رگبارها، هشدار نارنجی برای مناطق صادر خواهد شد، مسافران و کوهنوردان احتیاط کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/687542" target="_blank">📅 23:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687541">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
غرامت دهید تا از تنگه هرمز عبور کنید
عباس گلرو، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس در
#گفتگو
با خبرفوری:
🔹
طرح امنیت پایدار تنگه هرمز در مرحله پایانی بررسی در کمیسیون است. این طرح می‌تواند تنگه هرمز را به یک منبع درآمدی بسیار ارزنده برای کشور تبدیل کند. نوع رفتار با شناورهای کشورهای مختلف طبیعتا متفاوت خواهد بود، هر یک از دولت‌ها وضعیت متفاوتی دارند و علیه کشورهای متخاصم نیز اقداماتی انجام خواهد شد.
🔹
یکی از بندهایی که جدیدا در کمیسیون امنیت ملی مطرح شده، پرداخت غرامت از سوی کشورها، سازمان‌ها و افراد حقیقی و حقوقی است که در جنگ تحمیلی گذشته خسارت‌هایی را به جمهوری اسلامی ایران وارد کردند. در غیر این صورت، شناورهای متعلق به این کشورها نیز با ممنوعیت عبور از تنگه مواجه خواهند شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/687541" target="_blank">📅 23:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687540">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
معاون سیاسی نیروی دریایی سپاه: روزانه ۲ تا ۵ شناور در تنگۀ هرمز هدف قرار گرفته شده‌اند
علی محمدی:
🔹
در ۱۰ روز منتهی به ۸ شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.
🔹
حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل ارادۀ نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/687540" target="_blank">📅 23:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687539">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
چهارمین حمله رژیم صهیونیستی به سوریه طی ساعات اخیر
🔹
نظامیان رژیم صهیونیستی مستقر در پادگان الجزیره، منازل مردم روستای معریه در حومه یرموک سوریه را گلوله باران کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/akhbarefori/687539" target="_blank">📅 23:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687538">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
واکنش سفارت ایران در آنکارا به بیانیه سفیر آمریکا در ترکیه
🔹
سفارت ایران در آنکارا، اظهارات اخیر سفیر آمریکا را تلاشی برای پنهان‌سازی سیاست یکجانبه‌گرایانه واشنگتن در قبال ایران خواند و تأکید کرد: تغییر واژگان، ماهیت عملیات طرد اقتصادی را تغییر نمی‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/687538" target="_blank">📅 23:21 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
